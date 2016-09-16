
### global variables and collections for Z2N ###
### to retrieve in Zotero   ###

import os

### name application
title    = "LibViz" #ideas for a name : "Bibloom" - "REFNET" - "VIZZOT" - "REF2NET"
subtitle = "make graphs you can play with" #"FROM ZOTERO REFERENCES TO NETWORKS" # alternative : "make graphs to play with from references"
version  = "beta 2.0" ####

### default weight
w_dft      = 25
w_bigtag   = 4
w_biggroup = 2

#### routing to urls in Zotero's API
url_API_Zotero   = 'https://api.zotero.org/groups/' #336106/collections/'
items_API_Zotero = '/items/top?start=0&limit=1000'

### this import is placed after to avoid circular reference problem
### when calling 'url_API_Zotero' in createURL
from Z2N_scripts import createURL


### JSON outfile graph structure
### allows simultaneous global changes in : HTML / JS / PY
node_str_dict = {
            'id'       : 'ID',
            'reference': 'reference',
            'label'    : 'label',
            'note'     : 'note',
            'abstractNote' : 'abstractNote',
            'url'      : 'url',
            'type'     : 'type' ,
            'group'    : 'group',
            'tags'     : 'tag',
            'connex'   : 'connex',
            'category' : 'category',
            'supertag' : 'supertag',
            'weight'   : 'weight',
            'color'    : 'color',
            'dataset'  : 'dataset',
            'dataset_' : 'dataset_'
            }
edge_str_dict = {
            'id'     : node_str_dict['id'],
            'source' : 'source' ,
            'target' : 'target' ,
            'label'  : node_str_dict['label'] ,
            'group'  : node_str_dict['group'],
            'weight' : node_str_dict['weight'],
            'dash'   : 'dash'
            }


###########################################################################
####### collections of Zotero folders/references / EXTENDABLE LIST ########
###########################################################################
### color gradient hue : http://tools.medialab.sciences-po.fr/iwanthue/ ###

collections = {
    
    '1camp': {
        
        'API'           : 'Zotero',
        'dataSet_name'  : '[1.CAMP]',
        'dataSet_infos' : {
                            'presentation' : 'Presentation ...',
                            'authors'      : 'Authors...',
                            'methodology'  : 'Methodology...',
                            'credits'      : 'Credits / link to Zotero group...',
                        },
        'dataSet_key'   : '336106',
        'url_ROOT'      : createURL('336106'),
        'urlsDict'      : {
                            'F22AUXTI'  : {'name' : 'annuaire' , 'len' : 0, 'hex' : '#f7ffad'},
                            'A3IIWJG7'  : {'name' : 'lexique'  , 'len' : 0, 'hex' : '#4b5731'},
                            'G2P8TN8H'  : {'name' : 'veille'   , 'len' : 0, 'hex' : '#ffd617'},
                            'Q74J8B7H'  : {'name' : 'activites', 'len' : 0, 'hex' : '#abdbb6'},
                            'FMMA8WPK'  : {'name' : 'lectures' , 'len' : 0, 'hex' : '#01b617'}  
                        },
        'nodesColorsDict' : {
                node_str_dict['group']     : {'name' : 'red'  , 'hex' : '#8eba7d' },
                node_str_dict['tags']      : {'name' : 'blue' , 'hex' : '#a57eb7' },
                node_str_dict['reference'] : {'name' : 'lime' , 'hex' : '#c57753' }
                        },
        'edgesDashDict' : {
                'ref-ref'  : '5',
                'ref-tag'  : '4 4',
                'ref-group': '3 3'
                        },
        'switch_color'  : 'hex',
        'supertags'     : ['technosciences', 'savoirs communs', 'aliens', 'territoires']
        
        }
    
    ,
    
    'aliens_in_green' : {
        
        'API'           : 'Zotero',
        'dataSet_name'  : 'ALIENS IN GREEN',
        'dataSet_infos' : {
                            'presentation' : 'Presentation ...',
                            'authors'      : 'Authors...',
                            'methodology'  : 'Methodology...',
                            'credits'      : 'Credits / link to Zotero group...',
                        },
        'dataSet_key'   : '506887', ### aka group key
        'url_ROOT'      : createURL('506887'),
        'urlsDict'      : {
                            'N8IKC3JJ'  : {'name' : 'antagonistic organisations'  , 'len' : 0, 'hex' : '#b8d39a'},
                            'VMXEDTC2'  : {'name' : 'controversial organisations' , 'len' : 0, 'hex' : '#61835a'},
                            '4VTS6RH6'  : {'name' : 'effects'                     , 'len' : 0, 'hex' : '#67d863'},
                            'W64DR56S'  : {'name' : 'scandals'                    , 'len' : 0, 'hex' : '#c5ce6c'},
                            'DRTKSWNF'  : {'name' : 'scientific articles'         , 'len' : 0, 'hex' : '#96d6a3'},  
                            '7VQU2DSV'  : {'name' : 'substances'                  , 'len' : 0, 'hex' : '#608b32'}  
                        },
        'nodesColorsDict' : {
                node_str_dict['group']     : {'name' : 'red'  , 'hex' : '#8eba7d' },
                node_str_dict['tags']      : {'name' : 'blue' , 'hex' : '#a57eb7' },
                node_str_dict['reference'] : {'name' : 'lime' , 'hex' : '#c57753' }
                        },
        'edgesDashDict' : {
                'ref-ref'  : '5',
                'ref-tag'  : '4 4',
                'ref-group': '3 3'
                        },
        'switch_color'  : 'hex',
        'supertags'     : ['technosciences', 'savoirs communs', 'aliens', 'territoires']
    
        }

    ,
    
    'substances' : {
        
        'API'           : 'Zotero',
        'dataSet_name'  : 'ENDOCRINE DISRUPTION',
        'dataSet_infos' : {
                            'presentation' : 'Presentation ...',
                            'authors'      : 'Authors...',
                            'methodology'  : 'Methodology...',
                            'credits'      : 'Credits / link to Zotero group...',
                        },
        'dataSet_key'   : '506887', ### aka group key
        'url_ROOT'      : createURL('506887'),
        'urlsDict'      : {
                            '9EXBK2DP'  : {'name' : 'OESTROGENS'  , 'len' : 0, 'hex' : '#502c81'}
                        },
        'nodesColorsDict' : {
                node_str_dict['group']     : {'name' : 'red'  , 'hex' : '#8eba7d' },
                node_str_dict['tags']      : {'name' : 'blue' , 'hex' : '#a57eb7' },
                node_str_dict['reference'] : {'name' : 'lime' , 'hex' : '#c57753' }
                        },
        'edgesDashDict' : {
                'ref-ref'  : '1',
                'ref-tag'  : '2 1 2',
                'ref-group': '3 3'
                        },
        'switch_color'  : 'hex',
        'supertags'     : ['technosciences', 'savoirs communs', 'aliens', 'territoires']
    
        }
        
    ,
    
    'mediasFR' : {
        
        'API'           : 'Zotero',
        'dataSet_name'  : 'MEDIAS OWNERS - FRANCE',
        'dataSet_infos' : {
                            'presentation' : 'Based on a previous work published in "Le Monde Diplomatique" this dataset represents the structure of french medias ownership : from the few main wealthy families owning major industrial groups to almost every french press organisation ',
                            'authors'      : 'Datas gathered by Julien Paris from layout by Jeremie Fabre & Marie Beyer',
                            'methodology'  : 'All references are picked from Wikipedia and then referenced in Zotero in three different groups : "persons" (owning majority of the media/industrial groups) / "industrial groups" / press (newspaper, tv channels, internet newspaper)',
                            'credits'      : 'Credits / link to Zotero group...',
                        },
        'dataSet_key'   : '680968', ### aka group key
        'url_ROOT'      : createURL('680968'),
        'urlsDict'      : {
                            '3BAX9FGR'  : {'name' : 'Groupes industriels/media' , 'len' : 0, 'hex' : '#325d58'},
                            'ZBZBM9H7'  : {'name' : 'Personnes'                 , 'len' : 0, 'hex' : '#54b992'},
                            'NUBA9JCC'  : {'name' : 'Presse'                    , 'len' : 0, 'hex' : '#66aec2'}
                        },
        'nodesColorsDict' : {
                node_str_dict['group']     : {'name' : 'red'  , 'hex' : '#8eba7d' }, ###############
                node_str_dict['tags']      : {'name' : 'blue' , 'hex' : '#a57eb7' },
                node_str_dict['reference'] : {'name' : 'lime' , 'hex' : '#c57753' }
                        },
        'edgesDashDict' : {
                'ref-ref'  : '1',
                'ref-tag'  : '2 1 2',
                'ref-group': '3 3'
                        },
        'switch_color'  : 'hex',
        'supertags'     : ['technosciences', 'savoirs communs', 'aliens', 'territoires']
    
        }
        
        

    ### it should be possible to extend this list ...

    
    
}






