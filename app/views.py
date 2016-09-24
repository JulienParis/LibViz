from app import app
from flask import Flask, render_template

from werkzeug.routing import Rule
#app = Flask(__name__)

### import global variables for Z2N
from Z2N_vars import collections, title, subtitle, version
from Z2N_vars import node_str_dict as nodeStruct
from Z2N_vars import edge_str_dict as edgeStruct

from Z2N_vars_app import URLroot_artlabo, licenceCC

### place this import after Z2N_vars import to avoid circular reference for 'creatURL' 
import Z2N_scripts

### import scraping/JSON graph generator script
import Zotero_2_JSON

### create selection names list format from 'collections' : [selection_name, dataset_name]
collections_names = [ ]
for key, coll in collections.items():
    coll_list = [ key, coll['dataSet_name'] ]
    collections_names.append( coll_list )
collections_names.sort()
print 'collections_names :', collections_names

### global entries and structures from Z2N_vars.py
global_names = {
        'titleApp'          : title,             # name/brand of the app
        'subtitleApp'       : subtitle,          # explanation of what the app does
        'version'           : version,           # explanation of what the app does
        'collections_names' : collections_names, # list of collections with their keys, ids, ... 
        'ns'                : nodeStruct,        # integrate Jinja global ns in JS calling inside HTML/JS
        'es'                : edgeStruct         # integrate Jinja global es in J
    }


@app.route('/')
@app.route('/index')
@app.route('/'+URLroot_artlabo)
def index():
    print '-'*5 , ' collections_names list: ', collections_names
    return render_template("index.html",
                           glob      = global_names,
                           licenceCC = licenceCC,
                           index     = True
                           #isHome = True
                           #titleApp          = title ,
                           #subtitleApp       = subtitle ,
                           #collections_names = collections_names, 
                           #ns                = nodeStruct, 
                           #es                = edgeStruct  
                           )

### automatically creates specific routes for every dataset in collections
@app.route('/<selection>')
@app.route('/'+URLroot_artlabo+'/<selection>') ######
def data_rendering(selection):
    
    print
    print '-'*10, 'VIEW PAGE ', selection, '-'*50
    print 'selection :', selection    
    
    collection     = collections[selection]
    print 'collection :', collection
    shortName         = "/"+selection
    print 'shortName :', shortName

    ZoteroURL      = collection['url_WEB']
    
    #coll_name      = collections_names
    #selection      = coll_name[0]
    groups         = [ g['name'] for k, g  in collection['urlsDict'].items() ]
    #lineTypes      = [ k for k, g  in collection['edgesDashDict'].items() ]
    supertags      = collection['supertags']
    presetsFilters = collection['presetsFilters']
    print "presetsFilters", presetsFilters
    
    legend         = [ {"name":k, "hex": g["hex"] } for k, g  in collection['nodesColorsDict'].items() ]
    legendGroups   = [ {"name":g["name"], "hex": g["hex"] } for k, g  in collection['urlsDict'].items() ]

    outfileDict    = Z2N_scripts.Outfile_(selection)
    outfile_d3name = outfileDict['of_d3name']
    
    return render_template("D3_network.html",
                           glob           = global_names,
                           licenceCC      = licenceCC,
                           #isGraph     = True,
                           selection      = selection,
                           ZoteroURL      = ZoteroURL,
                           groups         = groups,
                           #legend        = legend,
                           #legendGroups  = legendGroups,
                           #lines       = lineTypes,
                           presetsFilters = presetsFilters,
                           supertags      = supertags,
                           dataSet_name   = collection['dataSet_name'],
                           dataSet_url    = shortName,
                           dataSet_infos  = collection['dataSet_infos'],
                           data_JSON      = outfile_d3name,
                           )


### refreshing the dataset / call scrapping script / and render template
## usual routing
@app.route('/refresh/<selection>')
@app.route('/'+URLroot_artlabo+'/refresh/<selection>')
def refresh(selection):
    
    print
    print '-'*10, 'REFRESHING PAGE ', selection, '-'*50
    print 'selection :', selection    
    
    collection     = collections[selection]
    print 'collection :', collection
    shortName         = "/"+selection
    print 'shortName :', shortName

    ZoteroURL      = collection['url_WEB']

    #coll_name      = collections_names
    #selection      = coll_name[0]
    groups         = [ g['name'] for k, g  in collection['urlsDict'].items() ]
    supertags      = collection['supertags']
    presetsFilters = collection['presetsFilters']

    legend         = [ {"name":k, "hex": g["hex"] } for k, g  in collection['nodesColorsDict'].items() ]
    legendGroups   = [ {"name":g["name"], "hex": g["hex"] } for k, g  in collection['urlsDict'].items() ]

    outfileDict    = Z2N_scripts.Outfile_(selection)
    outfile_d3name = outfileDict['of_d3name']

    outfile_name   = outfileDict['of_name']
    
    
    
    ### rewrites the JSON file for the selection
    if collection['API'] == 'Zotero':
        Zotero_2_JSON.refresh_JSON( selection, collection, outfile_name )



    return render_template("D3_network.html",
                           glob           = global_names,
                           licenceCC      = licenceCC,
                           #isGraph     = True,
                           selection      = selection,
                           ZoteroURL      = ZoteroURL,
                           groups         = groups,
                           #legend        = legend,
                           #legendGroups  = legendGroups,
                           presetsFilters = presetsFilters,
                           supertags      = supertags,
                           dataSet_name   = collection['dataSet_name'],
                           dataSet_url    = shortName,
                           dataSet_infos  = collection['dataSet_infos'],
                           data_JSON      = outfile_d3name,
                           )

