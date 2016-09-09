
### global variables and collections for Z2N ###
### to retrieve in Zotero   ###

import os

### name application
title    = "LIBVIZ" #ideas for a name : "REFNET" - "VIZZOT" - "REF2NET"
subtitle = "FROM ZOTERO REFERENCES TO NETWORK"

### default weight
w_dft      = 25
w_bigtag   = 4
w_biggroup = 5

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

### collections of Zotero folders/references
collections = {
    
    '1camp': {
        
        'API'           : 'Zotero',
        'dataSet_name'  : '[1.CAMP]',
        'dataSet_key'   : '336106',
        'url_ROOT'      : createURL('336106'),
        'urlsDict'      : {
                            'F22AUXTI'  : {'name' : 'annuaire' , 'len' : 0},
                            'A3IIWJG7'  : {'name' : 'lexique'  , 'len' : 0},
                            'G2P8TN8H'  : {'name' : 'veille'   , 'len' : 0},
                            'Q74J8B7H'  : {'name' : 'activites', 'len' : 0},
                            'FMMA8WPK'  : {'name' : 'lectures' , 'len' : 0}  
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
        'dataSet_name'  : 'ALIENS_IN_GREEN',
        'dataSet_key'   : '506887', ### aka group key
        'url_ROOT'      : createURL('506887'),
        'urlsDict'      : {
                            'N8IKC3JJ'  : {'name' : 'antagonistic organisations'  , 'len' : 0},
                            'VMXEDTC2'  : {'name' : 'controversial organisations' , 'len' : 0},
                            '4VTS6RH6'  : {'name' : 'effects'                     , 'len' : 0},
                            'W64DR56S'  : {'name' : 'scandals'                    , 'len' : 0},
                            'DRTKSWNF'  : {'name' : 'scientific articles'         , 'len' : 0},  
                            '7VQU2DSV'  : {'name' : 'substances'                  , 'len' : 0}  
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
    
    'oestrogens' : {
        
        'API'           : 'Zotero',
        'dataSet_name'  : 'OESTROGENS',
        'dataSet_key'   : '506887', ### aka group key
        'url_ROOT'      : createURL('506887'),
        'urlsDict'      : {
                            '9EXBK2DP'  : {'name' : 'OESTROGENS'  , 'len' : 0}
                        },
        'nodesColorsDict' : {
                node_str_dict['group']     : {'name' : 'red'  , 'hex' : '#8eba7d' },
                node_str_dict['tags']      : {'name' : 'blue' , 'hex' : '#a57eb7' },
                node_str_dict['reference'] : {'name' : 'lime' , 'hex' : '#c57753' }
                        },
        'edgesDashDict' : {
                'ref-ref'  : '10 1',
                'ref-tag'  : '2 1 2',
                'ref-group': '3 3'
                        },
        'switch_color'  : 'hex',
        'supertags'     : ['technosciences', 'savoirs communs', 'aliens', 'territoires']
    
        }
        
    
    
    ,
    
    'mediasFR' : {
        
        'API'           : 'Zotero',
        'dataSet_name'  : 'MEDIAS_FRANCE',
        'dataSet_key'   : '680968', ### aka group key
        'url_ROOT'      : createURL('680968'),
        'urlsDict'      : {
                            '3BAX9FGR'  : {'name' : 'Groupes'   , 'len' : 0},
                            'ZBZBM9H7'  : {'name' : 'Personnes' , 'len' : 0},
                            'NUBA9JCC'  : {'name' : 'Presse'    , 'len' : 0}
                        },
        'nodesColorsDict' : {
                node_str_dict['group']     : {'name' : 'red'  , 'hex' : '#8eba7d' },
                node_str_dict['tags']      : {'name' : 'blue' , 'hex' : '#a57eb7' },
                node_str_dict['reference'] : {'name' : 'lime' , 'hex' : '#c57753' }
                        },
        'edgesDashDict' : {
                'ref-ref'  : '10 1',
                'ref-tag'  : '2 1 2',
                'ref-group': '3 3'
                        },
        'switch_color'  : 'hex',
        'supertags'     : ['technosciences', 'savoirs communs', 'aliens', 'territoires']
    
        }
        
        

    ### it should be possible to extend this list ...

    
    
}






