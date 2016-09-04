
### script to transform Zotero's JSON to a graph JSON (nodes + links) ###
### generalizable to any JSON from Zotero's API

import json, urllib2
from pprint import pprint
#import os

### import global variables for Z2N
from Z2N_vars import w_dft, w_bigtag, w_biggroup, items_API_Zotero
from Z2N_vars import node_str_dict as ns
from Z2N_vars import edge_str_dict as es

### other possible libraries for API zotero / not used here
#import libZotero, pyzotero, zotero-cli
# doc libZotero  : http://programminghistorian.org/lessons/intro-to-the-zotero-api
# doc pyzotero   : https://github.com/urschrei/pyzotero
# doc zotero-cli : https://pypi.python.org/pypi/zotero-cli/0.2.1

print "-- bibliographic network --"
print "-- convert a JSON file with tags to a JSON network file for datavisualisation --"
#https://docs.python.org/2/library/json.html
#http://gappyfacets.com/2015/06/25/python-snippet-to-convert-csv-into-nodes-links-json-for-d3-js-network-data/

##########################################

### Retrieve JSON source
'''
example for a Zotero source in JSON :
https://api.zotero.org/groups/336106/items/
encoding  : windows-1252
'''

print "-"*50
print
print " -- loading Zotero JSON file source --"


def refresh_JSON ( selection, collection, outfile_name ) :
        
        #print 'collection :', collection
        dataSet_name    = collection['dataSet_name']
        url_ROOT        = collection['url_ROOT']
        urlsDict        = collection['urlsDict']
        nodesColorsDict = collection['nodesColorsDict']
        edgesDashDict   = collection['edgesDashDict']
        
        try :
                switch_color = collection['switch_color']    ### must be optional
        except :
                switch_color = 'name' 
        try :
                supertags    = collection['supertags']       ### must be optional
        except :
                supertags    = [ ]
        
        print
        print "+"*50
        print "--------- parsing -- %s -- collection ---------" %(dataSet_name)
        print "+"*50
        print
        
        ### load JSON from url / Zotero API
        data = [ ]
        #for url in urls :
        for key, infos in urlsDict.items() :
                url = url_ROOT + key + items_API_Zotero 
                print " --- from url : %s / %s " %(key, infos['name'])
                print " "*15, url
                response = urllib2.urlopen(url)
                data_    = json.load(response)
                
                print " "*15, 'len data_ : ', len(data_)
                print 
                infos['len'] = len(data_)
                data.extend(data_)
        
        print                               
        print "-"*50
        print
        print " -- test reading JSON file source --"
        print 
        print data[0]
        print "-"*50
        print 
        
        ##########################################
        nodesList     = [] ### to JSON
        nodesDict     = {}
        refIdsList   = []
        
        tagsDict      = {}
        
        groupsList    = []
        
        edgesList     = [] ### to JSON 
        
        ### cleaning / creating nodes' list
        counter_refs = 1
        print '____ creating nodes ____'

        for ref in data :
            print '-'*5, ref
            id_       = 'ref_' + ref[u'key']
            #id_       = 'ref_'+ str(counter_refs) ############ change to item KEY in Zotero 
            #print id_
            #ref_key_  = ref[u'key']
            
            refIdsList.append(id_)
            
            title_    = ref[u'data'][u'title'] ### == label
            try :
                note_ = ref[u'data'][u'note']
            except :
                note_ = '' 
            url_      = ref[u'data'][u'url']
            itemType_ = ref[u'data'][u'itemType']
        
            #read connex references
            connex_ = []
            connex_raw = ref[u'data'][u'relations']
            if connex_raw != {}:
                try :
                        connex_relations = connex_raw[u'dc:relation']
                except :
                        try  :
                                connex_relations = connex_raw[u'dc:replaces']
                        except :
                                connex_relations = connex_raw[u'owl:sameAs']
                        
                print 'ref :', id_, '/ connex : ', type(connex_relations)
                if type(connex_relations) is list:
                        for c_rel in connex_relations :
                                c_split = c_rel.split('items/', 1)[1].encode('UTF-8') 
                                c_rel_  = 'ref_' + c_split
                                #print 'ref :', id_, '/ connex : ', c_rel_
                                connex_.append(c_rel_)
                elif type(connex_relations) is unicode :
                        c_split = connex_relations.split('items/', 1)[1].encode('UTF-8') 
                        c_rel_ = 'ref_' + c_split
                        #print 'ref :', id_, '/ connex : ', c_rel_
                        connex_.append(c_rel_)
                print
                
            group_id  = ref[u'data'][u'collections'] #[0] ######## !!!! sometimes one ref is in several collections/groups
            ### fetch group name from group_id
            group_ = []
            for id_gr in group_id :
                listed_groups = urlsDict.keys()
                if id_gr in listed_groups :
                        group_.append( urlsDict[id_gr]['name']) ###############
            
            #if group_ not in groupsList :
            #    groupsList.append(group_)
                
            tags_raw  = ref[u'data'][u'tags']
            tags_    = []
            for tag in tags_raw :
                t = tag[u'tag'].encode('UTF-8')
                tags_.append(t)
                if t not in tagsDict :
                    tagsDict[t] = {'weight' : 1}
                else :
                    tagsDict[t]['weight'] += 1
            ref_dict = {
                         ns['id']       : id_.encode('UTF-8') ,
                         ns['label']    : title_,
                         ns['note']     : note_,
                         ns['url']      : url_.encode('UTF-8') ,
                         ns['type']     : itemType_.encode('UTF-8') ,
                         ns['group']    : group_, #.encode('UTF-8') ,
                         ns['tags']     : tags_,
                         ns['connex']   : connex_ , 
                         ns['category'] : 'reference',
                         ns['supertag'] : False,
                         ns['weight']   : w_dft,
                         ns['color']    : nodesColorsDict['reference'][switch_color],
                         ns['dataset']  : dataSet_name,
                         ns['dataset_'] : selection
                         }
            
            nodesList.append(ref_dict)
            nodesDict[title_] = ref_dict
            counter_refs += 1

        ### add groups as nodes in nodesList
        counter_groups = 1
        for group_key, group in urlsDict.items() :
        #for group in groupsList :
            #print group['name']
            gr_       = str(group['name'])
            id_       = 'group_'+ str(counter_groups)
            url_      = ''
            itemType_ = 'group name'
        
            group_dict = {
                          ns['id']       : id_.encode('UTF-8') ,
                          ns['label']    : gr_,
                          ns['url']      : url_.encode('UTF-8') ,
                          ns['type']     : itemType_.encode('UTF-8') ,
                          ns['group']    : gr_.encode('UTF-8') ,
                          ns['tags']     : '',
                          ns['category'] : 'group',
                          ns['supertag'] : True,
                          ns['weight']   : w_dft*w_biggroup ,
                          ns['color']    : nodesColorsDict['group'][switch_color] 
                         }
            
            nodesList.append(group_dict)
            nodesDict[gr_] = group_dict
            #print gr_, nodesDict[gr_]
            counter_groups += w_dft
            
        
        ### add tags as nodes in nodesList
        counter_tags = 1
        for tag, wgt_ in tagsDict.iteritems() :
            #print tag
            id_       = 'tag_'+ str(counter_tags)
            url_      = ''
            itemType_ = 'tag name'
            if tag in supertags:
                is_supertag = True
                is_sup      = w_bigtag
            else :
                is_supertag = False
                is_sup      = 1
            tag_dict  = {
                         ns['id']       : id_.encode('UTF-8') ,
                         ns['label']    : tag ,
                         ns['url']      : url_.encode('UTF-8') ,
                         ns['type']     : itemType_,
                         ns['group']    : '' ,
                         ns['tags']     : '',
                         ns['category'] : 'tag',
                         ns['supertag'] : is_supertag,
                         #ns['weight']   : wgt_['weight']*w_dft,
                         ns['weight']   : w_dft*is_sup,
                         ns['color']    : nodesColorsDict['tag'][switch_color] ##########################
                         }
        
            nodesList.append(tag_dict)
            nodesDict[tag] = tag_dict
            counter_tags += w_dft
        
        print " -- test reading nodesList -- "
        print
        for n in nodesList[0:4]:
                print 'node : ', n
                print
        print "-"*50
        print
        
        ###########################################
        ### creating edges' list
        counter_edges = 1
        print '____creating edges____'
        print
        
        ### list of sets keep track of ref-ref edges to avoid doubles
        connex_sets = []
        
        for n in nodesList:
                if n['category'] == 'reference':
                        #print 'n:', n
                        
                        ### ref-tag edges 
                        if n[ns['tags']] != '' :
                            src_    = n[ns['id']]
                            for tag in n[ns['tags']]:
                                id_     = 'edge_' + str(counter_edges)
                                #print nodesDict[tag]
                                trg_    = nodesDict[tag][ns['id']]
                                
                                #lab_    = ''
                                categ_  = 'ref-tag'
                                
                                edge_dict = {
                                        es['id']     : id_ ,
                                        es['source'] : src_ ,
                                        es['target'] : trg_ ,
                                        #es['label']  : lab_ ,
                                        es['group']  : categ_,
                                        es['weight'] : 1.0,
                                        es['dash']   : edgesDashDict[categ_],
                                    }
                                
                                edgesList.append(edge_dict)
                                counter_edges += 1
                        
                        ### ref-group edges
                        if n[ns['group']] != '' :
                            src_    = n[ns['id']]
                            for gr_ in n[ns['group']]:
                                #print 'gr_:', gr_
                                id_     = 'edge_' + str(counter_edges)
                                #print nodesDict[gr_]
                                trg_    = nodesDict[gr_][ns['id']]
                                #lab_    = ''
                                categ_  = 'ref-group'
                                    
                                edge_dict = {
                                        es['id']     : id_ ,
                                        es['source'] : src_ ,
                                        es['target'] : trg_ ,
                                        #es['label']  : lab_ ,
                                        es['group']  : categ_,
                                        es['weight'] : 1.0, 
                                        es['dash']   : edgesDashDict[categ_],
                                        
                                    }
                                    
                                edgesList.append(edge_dict)
                                counter_edges += 1
                        
                        ### ref-ref / connexes edges ############### PROBLEM NOT RESOLVED YET ####
                        if n[ns['connex']] != '' and n[ns['connex']] != [] :
                            src_    = n[ns['id']]
                            for conn_ in n[ns['connex']]:
                                trg_    = conn_
                                set_connex = {src_, trg_}
                                
                                if set_connex not in connex_sets and trg_ in refIdsList :
                                        
                                        print trg_, set_connex, 'NOT IN CONNEX_SETS'
                                        
                                        connex_sets.append(set_connex)
                                        
                                        id_     = 'edge_' + str(counter_edges)
                                        lab_    = ''
                                        categ_  = 'ref-ref'
                                
                                        edge_dict = {
                                            es['id']     : id_ ,
                                            es['source'] : src_ ,
                                            es['target'] : trg_ ,
                                            #es['label']  : lab_ ,
                                            es['group']  : categ_,
                                            es['weight'] : 1.0,
                                            es['dash']   : edgesDashDict[categ_]
                                            }
                                            
                                        edgesList.append(edge_dict)
                                        counter_edges += 1
                                
                                else :
                                        print set_connex, 'ALREADY IN CONNEX_SETS'
                        
                        #print 

        print " -- test reading edgesList -- "
        print
        for e in edgesList: #[0:3] :
                print 'edge : ', e
                #print
        print "-"*50
        print
        
        
        ##########################################
        
        ### generate JSON file / nodes + edges
        l_refs = len(data)
        l_grps = len(groupsList)
        l_tags = len(tagsDict)
        network_ = {"stats" : {"nodes": {
                               "refs number"   : l_refs,
                               "groups number" : l_grps,
                               "tags number"   : l_tags,
                               "nodes total number" : l_refs + l_grps + l_tags
                                   },
                               "edges" : {
                                        "edges number"  : len(edgesList)
                                        }
                                },
                    "nodes" : nodesList,
                    "links" : edgesList
                    }
        network_JSON = json.dumps(network_ , sort_keys = True,
                                  indent = 2,
                                  #ensure_ascii=False,
                                  #encoding='utf8',
                                  separators=(',', ': ')
        
                                  )
        print " -- print network_JSON as it is --"
        print " -- outfile_name : ", outfile_name
        print 
        print network_JSON[0:100], " ... "
        print
        outfile = open(outfile_name, 'w')
        outfile.write(network_JSON)
        outfile.close()
        
        #########################################
        ### debugging
        
        print
        print "-"*50
        print " -- end of script --"
        for key, infos in urlsDict.items() :
                print " -- refs in : ", infos['name'], ":", infos['len']
        print " -- stats : ", network_['stats']['edges']
        print 
