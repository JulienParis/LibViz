
### script to transform Zotero's JSON to a graph JSON (nodes + links) ###
### generalizable to any JSON from Zotero's API

import json, urllib2
from pprint import pprint
#import os

### import global variables for Z2N
from Z2N_vars import w_dft, w_bigtag, w_biggroup, items_API_Zotero #items_API_Zotero = '/items/top?start=0&limit=1000'
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
        listed_groups   = urlsDict.keys()
        listed_groups_  = [ i["name"] for k,i in urlsDict.items() ]
        nodesColorsDict = collection['nodesColorsDict']  ### colors by default
        ##refColorsDict   = collection['urlsDict']['hex']  ### colors references depending on their group
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
        
        getZotItems_01    = '/items/top?start='
        getZotItems_02    = '&limit='
        getZotItems_start = 0
        getZotItems_load  = 100
        
        def createURL_Zot (start) :
                
                ### url like : 
                url = getZotItems_01 + str(getZotItems_start) + getZotItems_02 + str(getZotItems_load)
                
                return url
        
        for key, infos in urlsDict.items() :
                
                finished = False
                
                while finished == False :
                        
                        lastPartUrl = createURL_Zot(getZotItems_start)
                        url         = url_ROOT + key + lastPartUrl               #items_API_Zotero = '/items/top?start=0&limit=1000'
                        
                        print " --- from url : %s / %s " %(key, infos['name'])
                        print " "*15, url
                        
                        response = urllib2.urlopen(url)
                        data_    = json.load(response)
                        
                        if len(data_) == 0 :
                                print " "*15, 'len data_ : ', len(data_)
                                print
                                finished = True
                                getZotItems_start = 0
                        
                        elif len(data_) < 100 :
                                print " "*15, 'len data_ : ', len(data_)
                                print 
                                infos['len'] = len(data_)
                                data.extend(data_)
                                finished = True
                                getZotItems_start = 0
                                #getZotItems_start += (getZotItems_load ) #+1)
                                
                        else :      
                                print " "*15, 'len data_ : ', len(data_)
                                print 
                                infos['len'] = len(data_)
                                data.extend(data_)
                                getZotItems_start += (getZotItems_load ) #+1)
                                
        
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
                authors_  = ref[u'data'][u'creators'] ### == authors
            except :
                authors_  = '' 
            try :
                note_ = ref[u'data'][u'note']
            except :
                note_ = '' 
            url_      = ref[u'data'][u'url']
            itemType_ = ref[u'data'][u'itemType']
            try : 
                abstract_ = ref[u'data'][u'abstractNote']
            except :
                abstract_ = ''
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
            
            ### groups and colors 
            group_id  = ref[u'data'][u'collections'] #[0] ######## !!!! sometimes one ref is in several collections/groups
            print "group_id:", group_id
            
            ### fetch group name from group_id
            group_ = []
            for id_gr in group_id :
                if id_gr in listed_groups :
                        group_.append( urlsDict[id_gr]['name']) ###############
            print "group_ :", group_ ###########
            
            ### attribute color depending on group
            if len(group_id) == 1 and group_id[0] in listed_groups : ### default color for group if ref in several groups
                colorRef = urlsDict[group_id[0]][switch_color]
            else : ### color of the group
                colorRef = nodesColorsDict['reference'][switch_color]
                
            ### fetch tags
            tags_raw  = ref[u'data'][u'tags']
            tags_    = []
            for tag in tags_raw :
                t = tag[u'tag'].encode('UTF-8')
                tags_.append(t)
                if t not in tagsDict :
                    tagsDict[t] = {'weight' : 1}
                else :
                    tagsDict[t]['weight'] += 1
            
            ### create ref datas
            ref_dict = {
                         ns['id']           : id_.encode('UTF-8') ,
                         ns['label']        : title_,
                         ns['authors']      : authors_,
                         ns['note']         : note_,
                         ns['abstractNote'] : abstract_.encode('UTF-8'),
                         ns['url']          : url_.encode('UTF-8') ,
                         ns['type']         : itemType_.encode('UTF-8') ,
                         ns['group']        : group_, #.encode('UTF-8') ,
                         ns['tags']         : tags_,
                         ns['connex']       : connex_ , 
                         ns['category']     : 'reference',
                         ns['supertag']     : False,
                         ns['weight']       : w_dft,
                         #ns['color']        : colorRef, ###############
                         ns['color']        : nodesColorsDict['reference'][switch_color], ###############
                         ns['dataset']      : dataSet_name,
                         ns['dataset_']     : selection
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
            colorGrp  = group['hex']
            
            group_dict = {
                          ns['id']       : id_.encode('UTF-8') ,
                          ns['label']    : gr_,
                          ns['url']      : url_.encode('UTF-8') ,
                          ns['type']     : itemType_.encode('UTF-8') ,
                          ns['group']    : [gr_], #.encode('UTF-8') ,
                          ns['tags']     : [gr_],
                          ns['category'] : 'group',
                          ns['supertag'] : True,
                          ns['weight']   : w_dft*w_biggroup ,
                          #ns['color']    : nodesColorsDict['group'][switch_color]  #####################
                          ns['color']    : colorGrp  #####################
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
                         ns['tags']     : [tag],
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
                
                ### only loop through references
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
                        
                        ### ref-ref / connexes edges 
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
        l_grps = len(listed_groups)
        n_grps = listed_groups_
        l_tags = len(tagsDict)
        n_tags = [ k for k, v in  tagsDict.items() ]
        print " -- print n_grps :", n_grps
        print " -- print n_tags :", n_tags

        
        network_ = {"stats" : {
                                "refs_number"   : l_refs,
                                "groups_number" : l_grps,
                                "groups_names"  : n_grps,
                                "tags_number"   : l_tags,
                                "tags_names"    : n_tags,
                                "nodes_number"  : l_refs + l_grps + l_tags, 
                                "edges_number"  : len(edgesList),
                                "dfltColorsDict": [ {"name" : k,         "hex" : v['hex'] }  for k, v in nodesColorsDict.items() ] ,
                                "grpsColorsDict": [ {"name" : v["name"], "hex" : v['hex'] } for k, v in urlsDict.items() ]
                                },
                    "nodes" : nodesList,
                    "links" : edgesList
                    }
        print "-- network_['stats']", network_["stats"]
        
        network_JSON = json.dumps(network_ ,
                                  sort_keys = True,
                                  indent = 2,
                                  #ensure_ascii=False,
                                  #encoding='utf8',
                                  separators=(',', ': ')
        
                                  )
        print " -- print network_JSON as it is --"
        print " -- outfile_name : ", outfile_name
        print 
        print network_JSON[0:200], " ... "
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
        print " -- stats : ", network_['stats']
        print 
