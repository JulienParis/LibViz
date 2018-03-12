# -*- coding: utf-8 -*-

### global variables and collections for Z2N ###
### to retrieve in Zotero   ###

import os

### name application
title       = "LibViz" #ideas for a name : "Bibloom" - "REFNET" - "VIZZOT" - "REF2NET"
subtitle    = "explore and play with references"
            #"FROM ZOTERO REFERENCES TO NETWORKS" # alternative : "make graphs to play with from references"
            #"what your library looks like"
version     = "beta 0.4" ####
metas       = """dataviz,data visualisation,zotero,graph,bilography,bibliographic references,force layout,force directed layout,
PING,artlabo,opensource,open source,open data,creative commons,
d3,d3.js,javascript,python,flask,HTML,CSS,JSON,bootstrap"""
description = "make interactive graphs from Zotero bibliographic references"

### default weight
w_dft      = 25
w_bigtag   = 4
w_biggroup = 2

#### routing to urls in Zotero's API
url_API_Zotero   = 'https://api.zotero.org/groups/' #336106/collections/'
url_WEB_Zotero   = 'https://www.zotero.org/groups/' #336106/collections/'
items_API_Zotero = '/items/top?start=0&limit=1000'

### this import is placed after to avoid circular reference problem
### when calling 'url_API_Zotero' in createURL
from Z2N_scripts import create_API_URL, create_API_URL_noColl, create_WEB_URL ## create zotero api/web url


### JSON outfile graph structure
### allows simultaneous global changes in : HTML / JS / PY
node_str_dict = {
            'id'            : 'ID',
            'reference'     : 'reference',
            'label'         : 'label',
            'authors'       : 'authors',
            'note'          : 'note',
            'abstractNote'  : 'abstractNote',
            'url'           : 'url',
            'type'          : 'type' ,
            'group'         : 'group',
            'tags'          : 'tag',
            'connex'        : 'connex',
            'category'      : 'category',
            'supertag'      : 'supertag',
            'weight'        : 'weight',
            'color'         : 'color',
            'dataset'       : 'dataset',
            'dataset_'      : 'dataset_'
            }
edge_str_dict = {
            'id'     : node_str_dict['id'],
            'source' : 'source' ,
            'target' : 'target' ,
            'label'  : node_str_dict['label'] , ### optional
            'group'  : node_str_dict['group'],
            'weight' : node_str_dict['weight'],
            'dash'   : 'dash'
            }


###########################################################################
####### collections of Zotero folders/references / EXTENDABLE LIST ########
###########################################################################
###
### color gradient hue : http://tools.medialab.sciences-po.fr/iwanthue/ ###

### main collection list / should be stocked in mongo or SQL database to able user interaction (add collection for instance)
collections = {

    '1camp': {

        'API'           : 'Zotero',
        'dataSet_name'  : '[1.camp]',
        'dataSet_infos' : {
                            'presentation' : """Presentation ...""",
                            'authors'      : """Authors...""",
                            'methodology'  : """Methodology...""",
                            'credits'      : """Credits / link to Zotero group...""",
                        },
        'dataSet_key'   : '336106',
        'url_ROOT'      : create_API_URL('336106'),
        'url_WEB'       : create_WEB_URL('336106'),
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
        'presetsFilters': {"radialFilter": [], "hideFilter" : [] , "breakFilter" : [] }, ## selection by .class and by .id !!!
        'supertags'     : ['technosciences', 'savoirs communs', 'aliens', 'territoires']

        }

    ,

    #'aliens_in_green' : {
    #
    #    'API'           : 'Zotero',
    #    'dataSet_name'  : 'ALIENS IN GREEN',
    #    'dataSet_infos' : {
    #                        'presentation' : 'Presentation ...',
    #                        'authors'      : 'Authors...',
    #                        'methodology'  : 'Methodology...',
    #                        'credits'      : 'Credits / link to Zotero group...',
    #                    },
    #    'dataSet_key'   : '506887', ### aka group key
    #    'url_ROOT'      : create_API_URL('506887'),
    #    'url_WEB'       : create_WEB_URL('506887'),
    #    'urlsDict'      : {
    #                        'N8IKC3JJ'  : {'name' : 'antagonistic organisations'  , 'len' : 0, 'hex' : '#b8d39a'},
    #                        'VMXEDTC2'  : {'name' : 'controversial organisations' , 'len' : 0, 'hex' : '#61835a'},
    #                        '4VTS6RH6'  : {'name' : 'effects'                     , 'len' : 0, 'hex' : '#67d863'},
    #                        'W64DR56S'  : {'name' : 'scandals'                    , 'len' : 0, 'hex' : '#c5ce6c'},
    #                        'DRTKSWNF'  : {'name' : 'scientific articles'         , 'len' : 0, 'hex' : '#96d6a3'},
    #                        '7VQU2DSV'  : {'name' : 'substances'                  , 'len' : 0, 'hex' : '#608b32'}
    #                    },
    #    'nodesColorsDict' : {
    #            node_str_dict['group']     : {'name' : 'red'  , 'hex' : '#8eba7d' },
    #            node_str_dict['tags']      : {'name' : 'blue' , 'hex' : '#a57eb7' },
    #            node_str_dict['reference'] : {'name' : 'lime' , 'hex' : '#c57753' }
    #                    },
    #    'edgesDashDict' : {
    #            'ref-ref'  : '5',
    #            'ref-tag'  : '4 4',
    #            'ref-group': '3 3'
    #                    },
    #    'switch_color'  : 'hex',
    #    'presetsFilters': {"radial": [], "hide" : [] , "breakLinks" : [] },
    #    'supertags'     : []
    #
    #    }
    #
    #,

#     'substances' : {

#         'API'           : 'Zotero',
#         'dataSet_name'  : 'Substances & endocrine disruption',
#         'dataSet_infos' : {
#                             'presentation' : """
# Database ENDOCRINE DISRUPTION shows -substances- disrupting endocrinian system in human (males and females) and also in non humans, with their -biological effects- and -societal effects- on them.
# It shows -controversial organisations- producing endocrine disruptors and -antagonist organisations- which struggle against them.
# <br>
# Through the database it is possible to watch a large set of -scientific articles- in order to evaluate ways of action of endocrine disruptors.
# \n
# Pathways to investigate the different sets of datas, their structure and relationships :
# a - Recognizing the tags ? Please click in LEGEND . See the different COLORS of each tag, and learn to make distinction.
# b - Hierarchising the tags ? Please click the tag SUBSTANCE + RADIAL.

# You see a circle with the different substances indexed in the database
# You can add all the BIOLOGICAL AND SOCIETAL EFFECTS directly connected with these SUBSTANCES.
# And, when you have watched different nodes associating substances and effects, to connect them to organisations which produces substances,
# and organisation which produce conflicts with the controversial organisations and uses.
#                                                 """
#                                                 ,
#                             'authors'      : """The different persons involved in the collective group Aliens in green, mostly the artist group Bureau d'etudes and the writer Ewen Chardronnet,
#                                                 have contributed to collect datas and to put them in the Zotero database. The support of Ping and specially Julien Bellanger,
#                                                 the support of Labomedia and mostly Benjamin Cadon give us the understanding of the tools than we decide to use for this project :
#                                                 the use of Zotero database and the transcription in a D3JS visualisation.
#                                                 \
#                                                 The work of transcription from Zotero to D3JS, the machinery and the graphic design of the dataviz is produced by Julien Paris.
#                                                 """,
#                             'methodology'  : """The first moment of the project was the indexation of scientific articles related to hormones and specifically xeno-hormones and endocrine disruptors
#                                                 in a Zotero data base. From this scientific corpus it was possible to create a matrix of potential inquiries interconnecting substances,
#                                                 biological and societal effects, organisations and scandals related to the diffusion and effects of substances on humans and non humans organisms.
#                                                 \
#                                                 This dataviz is a tool for the conception of argumentations and narratives relative to endocrine disruptors but also the power and interests related to them.
#                                                 """,
#                             'credits'      : """Contact dataviz : jparis.py-at-gmail.com
#                                                 \Contact Aliens in green : bureaudetudes-at-gmail.com, e.chardronnet-at-gmail.com
#                                                 \Administrative support of the conception : association Champ des possibles, 03210 Saint Menoux (France)
#                                                 \Co-financement for the development : CNC-Dicream
#                                                 """,
#                         },
#         'dataSet_key'   : '506887', ### aka group key
#         'url_ROOT'      : create_API_URL('506887'),
#         'url_WEB'       : create_WEB_URL('506887'),
#         'urlsDict'      : {
#                             'N8IKC3JJ'  : {'name' : 'ANTAGONISTIC ORGANISATIONS'  ,     'len' : 0, 'hex' : '#502c81'},
#                             'MCZITC29'  : {'name' : 'BIOLOGICAL EFFECTS'  ,             'len' : 0, 'hex' : '#502c81'},
#                             'VMXEDTC2'  : {'name' : 'CONTROVERSIAL ORGANISATIONS'  ,    'len' : 0, 'hex' : '#502c81'},
#                             '4VTS6RH6'  : {'name' : 'EFFECTS'  ,                        'len' : 0, 'hex' : '#502c81'},
#                             '9EXBK2DP'  : {'name' : 'ENDOCRINE DISRUPTION'  ,           'len' : 0, 'hex' : '#502c81'},
#                             'W64DR56S'  : {'name' : 'SCANDALS'  ,                       'len' : 0, 'hex' : '#502c81'},
#                             'DRTKSWNF'  : {'name' : 'SCIENTIFIC ARTICLES'  ,            'len' : 0, 'hex' : '#502c81'},
#                             'DRFADGNQ'  : {'name' : 'SOCIETAL EFFECTS'  ,               'len' : 0, 'hex' : '#502c81'},
#                             '7VQU2DSV'  : {'name' : 'SUBSTANCES'  ,               'len' : 0, 'hex' : '#502c81'},
#                         },
#         'nodesColorsDict' : {
#                 node_str_dict['group']     : {'name' : 'red'  , 'hex' : '#8eba7d' },
#                 node_str_dict['tags']      : {'name' : 'blue' , 'hex' : '#a57eb7' },
#                 node_str_dict['reference'] : {'name' : 'lime' , 'hex' : '#000000' }
#                         },
#         'edgesDashDict' : {
#                 'ref-ref'  : '1',
#                 'ref-tag'  : '1 3',
#                 'ref-group': '3 3'
#                         },
#         'switch_color'  : 'hex',
#         'presetsFilters': {"radialFilter": ["SUBSTANCES"], "hideFilter" : ["group", "tag"] , "breakFilter" : ["ref-group", "ref-tag"] }, ## selection by .class and by .id !!!
#         'supertags'     : []

#         }

#     ,

 'endocrine-disruption' : {

        'API'           : 'Zotero',
        'dataSet_name'  : 'Endocrine disruption',
        'dataSet_infos' : {
                            'presentation' : """
                                                Database ENDOCRINE DISRUPTION shows -substances- disrupting endocrinian system in human (males and females) and also in non humans, with their -biological effects- and -societal effects- on them.
                                                It shows -controversial organisations- producing endocrine disruptors and -antagonist organisations- which struggle against them.
                                                <br>
                                                Through the database it is possible to watch a large set of -scientific articles- in order to evaluate ways of action of endocrine disruptors.
                                                \n
                                                Pathways to investigate the different sets of datas, their structure and relationships :
                                                a - Recognizing the tags ? Please click in LEGEND . See the different COLORS of each tag, and learn to make distinction.
                                                b - Hierarchising the tags ? Please click the tag SUBSTANCE + RADIAL.

                                                You see a circle with the different substances indexed in the database
                                                You can add all the BIOLOGICAL AND SOCIETAL EFFECTS directly connected with these SUBSTANCES.
                                                And, when you have watched different nodes associating substances and effects, to connect them to organisations which produces substances,
                                                and organisation which produce conflicts with the controversial organisations and uses.
                                                """
                                                ,
                            'authors'      : """The different persons involved in the collective group Aliens in green, mostly the artist group Bureau d'etudes and the writer Ewen Chardronnet,
                                                have contributed to collect datas and to put them in the Zotero database. The support of Ping and specially Julien Bellanger,
                                                the support of Labomedia and mostly Benjamin Cadon give us the understanding of the tools than we decide to use for this project :
                                                the use of Zotero database and the transcription in a D3JS visualisation.
                                                \
                                                The work of transcription from Zotero to D3JS, the machinery and the graphic design of the dataviz is produced by Julien Paris.
                                                """,
                            'methodology'  : """The first moment of the project was the indexation of scientific articles related to hormones and specifically xeno-hormones and endocrine disruptors
                                                in a Zotero data base. From this scientific corpus it was possible to create a matrix of potential inquiries interconnecting substances,
                                                biological and societal effects, organisations and scandals related to the diffusion and effects of substances on humans and non humans organisms.
                                                \
                                                This dataviz is a tool for the conception of argumentations and narratives relative to endocrine disruptors but also the power and interests related to them.
                                                """,
                            'credits'      : """Contact dataviz : jparis.py-at-gmail.com
                                                \Contact Aliens in green : bureaudetudes-at-gmail.com, e.chardronnet-at-gmail.com
                                                \Administrative support of the conception : association Champ des possibles, 03210 Saint Menoux (France)
                                                \Co-financement for the development : CNC-Dicream
                                                """,
                        },
        'dataSet_key'   : '506887', ### aka group key
        'url_ROOT'      : create_API_URL('506887'),
        'url_WEB'       : create_WEB_URL('506887'),
        'urlsDict'      : {
                            '9EXBK2DP'  : {'name' : 'ENDOCRINE DISRUPTION'  ,           'len' : 0, 'hex' : '#502c81'},
                        },
        'nodesColorsDict' : {
                node_str_dict['group']     : {'name' : 'red'  , 'hex' : '#8eba7d' },
                node_str_dict['tags']      : {'name' : 'blue' , 'hex' : '#a57eb7' },
                node_str_dict['reference'] : {'name' : 'lime' , 'hex' : '#000000' }
                        },
        'edgesDashDict' : {
                'ref-ref'  : '1',
                'ref-tag'  : '1 3',
                'ref-group': '3 3'
                        },
        'switch_color'  : 'hex',
        'presetsFilters': {"radialFilter": ["SUBSTANCES"], "hideFilter" : ["group", "tag"] , "breakFilter" : ["ref-group", "ref-tag"] }, ## selection by .class and by .id !!!
        'supertags'     : []

        }

    ,


    'mediasFR' : {

        'API'           : 'Zotero',
        'dataSet_name'  : 'Media owners in France',
        'dataSet_infos' : {
                            'presentation' : """Based on a previous work published in "Le Monde Diplomatique" this dataset represents the structure of french medias ownership :
                                                from the few main wealthy families owning major industrial groups to almost every french press organisation """,
                            'authors'      : """Datas gathered in Zotero by Julien Paris from layout by Jeremie Fabre & Marie Beyer""",
                            'methodology'  : """All references are picked from Wikipedia and then referenced in Zotero in three different groups :
                                                "persons" (owning majority of the media/industrial groups) / "industrial groups" / press (newspaper, tv channels, internet newspaper)""",
                            'credits'      : """Credits / link to Zotero group...""",
                        },
        'dataSet_key'   : '680968', ### aka group key
        'url_ROOT'      : create_API_URL('680968'),
        'url_WEB'       : create_WEB_URL('680968'),
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
        'presetsFilters': {"radialFilter": ["tag"], "hideFilter" : ["group"] , "breakFilter" : ["ref-group"] }, ## selection by .class and by .id !!!
        'supertags'     : []

        }

    ,

    'free_openSource_lib' : {

        'API'           : 'Zotero',
        'dataSet_name'  : 'Free and open source softwares',
        'dataSet_infos' : {
                            'presentation' : """Free/Libre and Open Source Software and Libraries Bibliography """,
                            'authors'      : """... """,
                            'methodology'  : """... """,
                            'credits'      : """...""",
                        },
        'dataSet_key'   : '10885', ### aka group key
        'url_ROOT'      : create_API_URL_noColl('10885'), ######## !! no collection inside library
        'url_WEB'       : create_WEB_URL('10885'),
        'urlsDict'      : {
                            ''  : {'name' : 'library' , 'len' : 0, 'hex' : '#325d58'},
                        },
        'nodesColorsDict' : {
                node_str_dict['group']     : {'name' : 'red'  , 'hex' : '#8eba7d' }, ###############
                node_str_dict['tags']      : {'name' : 'blue' , 'hex' : '#a57eb7' },
                node_str_dict['reference'] : {'name' : 'lime' , 'hex' : '#c57753' }
                        },
        'edgesDashDict' : {
                'ref-ref'  : '1',
                'ref-tag'  : '1 1',
                'ref-group': '3 3'
                        },
        'switch_color'  : 'hex',
        'presetsFilters': {"radialFilter": ["reference"], "hideFilter" : ["group"] , "breakFilter" : ["ref-group"] }, ## selection by .class and by .id !!!
        'supertags'     : []

        }

    ,

    'eval_instit_open' : {

        'API'           : 'Zotero',
        'dataSet_name'  : 'Evaluation institutionnelle et open access',
        'dataSet_infos' : {
                            'presentation' : """Bibliographie Zotero partagee realisee dans le cadre du colloque "Open Access et evaluation de la recherche : vers un nouvel ecosysteme ?" (13-14 octobre 2016, Toulouse, France).""",
                            'authors'      : """... """,
                            'methodology'  : """... """,
                            'credits'      : """...""",
                        },
        'dataSet_key'   : '696651', ### aka group key
        'url_ROOT'      : create_API_URL('696651'),
        'url_WEB'       : create_WEB_URL('696651'),
        'urlsDict'      : {
                            'SNVCAAHC'  : {'name' : 'eval. institutionnelle'    , 'len' : 0, 'hex' : '#325d58'},
                            'W3ZT48XZ'  : {'name' : 'eval. ouverte'             , 'len' : 0, 'hex' : '#325d58'},
                            'UPHW9G8J'  : {'name' : 'e-reputation'              , 'len' : 0, 'hex' : '#325d58'},
                            'EXTZ9QIE'  : {'name' : 'eval. instit. en question' , 'len' : 0, 'hex' : '#325d58'},
                        },
        'nodesColorsDict' : {
                node_str_dict['group']     : {'name' : 'red'  , 'hex' : '#8eba7d' }, ###############
                node_str_dict['tags']      : {'name' : 'blue' , 'hex' : '#a57eb7' },
                node_str_dict['reference'] : {'name' : 'lime' , 'hex' : '#c57753' }
                        },
        'edgesDashDict' : {
                'ref-ref'  : '1',
                'ref-tag'  : '1 1',
                'ref-group': '3 3'
                        },
        'switch_color'  : 'hex',
        'presetsFilters': {"radialFilter": ["group"], "hideFilter" : [] , "breakFilter" : [] }, ## selection by .class and by .id !!!
        'supertags'     : []

        }

    ,

    'bcn_smart_city_commons' : {

        'API'           : 'Zotero',
        'dataSet_name'  : 'Barcelona Smart City Commons',
        'dataSet_infos' : {
                            'presentation' : """Mappeig d'actors, activitats i programes municipals dins del context de "ciutat intelligent" amb orientacio commons.""",
                            'authors'      : """... """,
                            'methodology'  : """... """,
                            'credits'      : """...""",
                        },
        'dataSet_key'   : '457033', ### aka group key
        'url_ROOT'      : create_API_URL('457033'),
        'url_WEB'       : create_WEB_URL('457033'),
        'urlsDict'      : {
                            'GPE7XPCR'  : {'name' : 'activitats'                 , 'len' : 0, 'hex' : '#325d58'},
                            '789A3ZB5'  : {'name' : 'actors'                     , 'len' : 0, 'hex' : '#325d58'},
                            'EF62A2WJ'  : {'name' : 'comunicacio'                , 'len' : 0, 'hex' : '#325d58'},
                            'X6PFG7BT'  : {'name' : 'comuns'                     , 'len' : 0, 'hex' : '#325d58'},
                            '2RWEV6NZ'  : {'name' : 'literatura'                 , 'len' : 0, 'hex' : '#325d58'},
                            'QNKDR957'  : {'name' : 'mecanismes'                 , 'len' : 0, 'hex' : '#325d58'},
                            'P7JR797V'  : {'name' : 'referenciels internacionals', 'len' : 0, 'hex' : '#325d58'},
                        },
        'nodesColorsDict' : {
                node_str_dict['group']     : {'name' : 'red'  , 'hex' : '#8eba7d' }, ###############
                node_str_dict['tags']      : {'name' : 'blue' , 'hex' : '#a57eb7' },
                node_str_dict['reference'] : {'name' : 'lime' , 'hex' : '#c57753' }
                        },
        'edgesDashDict' : {
                'ref-ref'  : '1',
                'ref-tag'  : '1 1',
                'ref-group': '3 3'
                        },
        'switch_color'  : 'hex',
        'presetsFilters': {"radialFilter": ["reference"], "hideFilter" : [] , "breakFilter" : [] }, ## selection by .class and by .id !!!
        'supertags'     : []

        }


    ,

    'urbanmedialabwaste' : {

        'API'           : 'Zotero',
        'dataSet_name'  : 'Urban Media Lab Waste',
        'dataSet_infos' : {
                            'presentation' : """This is the digital reference library for URBAN MEDIA LAB: WASTE, a graduate-level seminar in the School of Media Studies at The New School taught by Jessica Blaustein, Spring 2014.""",
                            'authors'      : """... """,
                            'methodology'  : """... """,
                            'credits'      : """...""",
                        },
        'dataSet_key'   : '242813', ### aka group key
        'url_ROOT'      : create_API_URL('242813'),
        'url_WEB'       : create_WEB_URL('242813'),
        'urlsDict'      : {
                            'PB2V5ETU'  : {'name' : '0 introduction'               , 'len' : 0, 'hex' : '#325d58'},
                            'WV4H35NE'  : {'name' : '1 material'                   , 'len' : 0, 'hex' : '#325d58'},
                            'T8PUQ74G'  : {'name' : '2 manufacture'                , 'len' : 0, 'hex' : '#325d58'},
                            'JD88R4KW'  : {'name' : '3 package'                    , 'len' : 0, 'hex' : '#325d58'},
                            '64K6XTKQ'  : {'name' : '4 data'                       , 'len' : 0, 'hex' : '#325d58'},
                            '7BSJDJZS'  : {'name' : '5 information management'     , 'len' : 0, 'hex' : '#325d58'},
                            '8PHFX4IE'  : {'name' : '6 disposal'                   , 'len' : 0, 'hex' : '#325d58'},
                            'G6XPS2XM'  : {'name' : '6a e-waste'                   , 'len' : 0, 'hex' : '#325d58'},
                            '6XJB3GFF'  : {'name' : '6b e-use'                     , 'len' : 0, 'hex' : '#325d58'},
                            'D59XD5DQ'  : {'name' : '6c solid waste'               , 'len' : 0, 'hex' : '#325d58'},

                            'WBEDT88F'  : {'name' : 'industry sources'             , 'len' : 0, 'hex' : '#325d58'},
                            'IFVE38TS'  : {'name' : 'methodology'                  , 'len' : 0, 'hex' : '#325d58'},
                            'P6TPRZ6J'  : {'name' : 'data gathering'               , 'len' : 0, 'hex' : '#325d58'},
                            'APGKQF3E'  : {'name' : 'projects'                     , 'len' : 0, 'hex' : '#325d58'},

                            'N434BTWU'  : {'name' : 'architecture & land use'      , 'len' : 0, 'hex' : '#325d58'},
                            'IZ3EW62R'  : {'name' : 'informal cities'              , 'len' : 0, 'hex' : '#325d58'},
                            'SNWGKNTA'  : {'name' : 'litterature'                  , 'len' : 0, 'hex' : '#325d58'},
                            '5GS332CS'  : {'name' : 'theoretical backgrounds'      , 'len' : 0, 'hex' : '#325d58'},
                        },
        'nodesColorsDict' : {
                node_str_dict['group']     : {'name' : 'red'  , 'hex' : '#8eba7d' }, ###############
                node_str_dict['tags']      : {'name' : 'blue' , 'hex' : '#a57eb7' },
                node_str_dict['reference'] : {'name' : 'lime' , 'hex' : '#c57753' }
                        },
        'edgesDashDict' : {
                'ref-ref'  : '1',
                'ref-tag'  : '1 1',
                'ref-group': '3 3'
                        },
        'switch_color'  : 'hex',
        'presetsFilters': {"radialFilter": ["group"], "hideFilter" : [] , "breakFilter" : ["ref-tag"] }, ## selection by .class and by .id !!!
        'supertags'     : []

        }

        ,

    'atelier-controverse' : {

            'API'           : 'Zotero',
            'dataSet_name'  : 'Atelier controverses CNAM',
            'dataSet_infos' : {
                                'presentation' : """... """,
                                'authors'      : """... """,
                                'methodology'  : """... """,
                                'credits'      : """...""",
                            },
            'dataSet_key'   : '1307836', ### aka group key
            'url_ROOT'      : create_API_URL('1307836'),
            'url_WEB'       : create_WEB_URL('1307836'),
            'urlsDict'      : {
                                '4GNHM5CM'  : {'name' : 'culturelle'               , 'len' : 0, 'hex' : '#325d58'},
                                'Z7QPH9M9'  : {'name' : 'sociale'                  , 'len' : 0, 'hex' : '#325d58'},
                                '5MZXSX9Q'  : {'name' : 'territoriale'             , 'len' : 0, 'hex' : '#325d58'},
                                'ZN6IUZXZ'  : {'name' : 'economique'               , 'len' : 0, 'hex' : '#325d58'},
                                '967XD3W7'  : {'name' : 'atelier'                  , 'len' : 0, 'hex' : '#325d58'},

                            },
            'nodesColorsDict' : {
                    node_str_dict['group']     : {'name' : 'red'  , 'hex' : '#8eba7d' }, ###############
                    node_str_dict['tags']      : {'name' : 'blue' , 'hex' : '#a57eb7' },
                    node_str_dict['reference'] : {'name' : 'lime' , 'hex' : '#c57753' }
                            },
            'edgesDashDict' : {
                    'ref-ref'  : '1',
                    'ref-tag'  : '1 1',
                    'ref-group': '3 3'
                            },
            'switch_color'  : 'hex',
            'presetsFilters': {"radialFilter": ["group"], "hideFilter" : [] , "breakFilter" : [] }, ## selection by .class and by .id !!!
            'supertags'     : []

            }

        ,

'nathalie-magnan' : {

            'API'           : 'Zotero',
            'dataSet_name'  : 'Nathalie Magnan',
            'dataSet_infos' : {
                                'presentation' : u""" 
                                                The LibViz datavisualisation NATHALIE MAGNAN shows different fields of activities explored by
                                                Nathalie Magnan in her teachings, writings, translation works, activism and art practices. 
                                                \n
                                                For readibility purposes we made 6 simples categories : ART / ACTIVISME / CYBERFEMINISME /
                                                ENSEIGNEMENT / PRESSE / THEMES / THEORIE DES MEDIAS. Main explored topics are
                                                identified in THEMES.
                                                """,
                                'authors'      : u""" 
                                                The Zotero library was coordinated by Ewen Chardronnet. The different persons involved in the
                                                organisation of « TRANS/BORDER : Les Enseignements de Nathalie Magnan » and of the « Edit-a-thon
                                                Wikipédia Art+Feminism » organised in Paris (Gaité lyrique), Bourges (Ecole nationale supérieure d’art /
                                                Bandits-Mages) and Bruxelles (Ecole de recherche graphique), have contributed to collect datas and to
                                                put them in the Zotero database. 
                                                \n
                                                The support of Ping and specially Julien Bellanger, the support of
                                                Labomedia and mostly Benjamin Cadon gave us the understanding of the tools we decided to use for
                                                this project : the use of Zotero database and the transcription in a D3JS visualisation. The work of
                                                transcription from Zotero to D3JS, the machinery and the graphic design of the dataviz was produced by
                                                Julien Paris.
                                                """,
                                'methodology'  : u"""
                                                The first task of the project was the collect, digitalisation and indexation of Nathalie Magnan
                                                works&articles in a Zotero data base, wether they were online or not. The indexation has been done in
                                                french, but cover her english work as well. From this corpus it was possible to extend the dataset in order
                                                to create a matrix of potential meta-relations interconnecting Nathalie Magnan main research fields,
                                                thematics and people or organisations she worked with. This dataviz is a tool for the navigation in the
                                                large sprectrum of actions, theoretical works, argumentations and narratives covered by Nathalie Magnan.
                                                """,
                                'credits'      : u""" 
                                                Contact dataviz : jparis.py-at-gmail.com \ Contact for Nathalie Magnan’s Zotero library : e.chardronnet-
                                                at-gmail.com \ LibViz was developed with the support of the CNC-Dicream in the context of the Aliens
                                                in Green project (aliensingreen.eu).
                                                \n
                                                Ewen Chardronnet wants to thank Reine Prat, Isabelle Carlier, Marie Lechner, Isabelle Arvers, Chloé
                                                Desmoineaux.
                                                """,
                            },
            'dataSet_key'   : '1411268', ### aka group key
            'url_ROOT'      : create_API_URL('1411268'),
            'url_WEB'       : create_WEB_URL('1411268'),
            'urlsDict'      : {
                                'IPPP3DAC'  : {'name' : 'Nathalie Magnan' , 'len' : 0, 'hex' : '#325d58'},
                            },
            'nodesColorsDict' : {
                    node_str_dict['group']     : {'name' : 'red'  , 'hex' : '#8eba7d' }, ###############
                    node_str_dict['tags']      : {'name' : 'blue' , 'hex' : '#a57eb7' },
                    node_str_dict['reference'] : {'name' : 'lime' , 'hex' : '#c57753' }
                            },
            'edgesDashDict' : {
                    'ref-ref'  : '1',
                    'ref-tag'  : '1 1',
                    'ref-group': '3 3'
                            },
            'switch_color'  : 'hex',
            'presetsFilters': {"radialFilter": [], "hideFilter" : [] , "breakFilter" : ["ref-group"], "collapsers" : "all" }, ## selection by .class and by .id !!!
            'supertags'     : []

            }

    ### it should be possible to extend this list ...



}
