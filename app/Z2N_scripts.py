
### global scripts for Z2N ###

import os

from Z2N_vars_app import static_dir
from Z2N_vars     import url_API_Zotero, url_WEB_Zotero, items_API_Zotero

cwd              = os.getcwd()
SITE_ROOT        = os.path.realpath(os.path.dirname(__file__))
outfile_dir      = SITE_ROOT + static_dir + '/data'

def Outfile_(dataset) : ### name and adresses of a json file
        
        ### basic name : dataset_network.json
        outfile_filename = dataset +'_network.json'
        
        ### adress from root : root/static_dir/data/dataset_network.json
        outfile_name     = outfile_dir + "/" + outfile_filename
        
        ### adress from app : static_dir/data/dataset_network.json
        outfile_d3name   = static_dir + '/data/' + outfile_filename
        
        ### compiling
        outfileDict = {
                'of_filename' : outfile_filename,
                'of_name'     : outfile_name,
                'of_d3name'   : outfile_d3name
        }
        
        return outfileDict
    

def create_API_URL (dataSet_key) : ### generates Zotero API url from a dataset collection key
    
    url = url_API_Zotero + dataSet_key + '/collections/'
    return url

def create_WEB_URL (dataSet_key) : ### generates Zotero WEB url from a dataset collection key
    
    url = url_WEB_Zotero + dataSet_key + '/items/'
    return url


