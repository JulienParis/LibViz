'''          ZOTERO TO NETWORK
--------------------------------------------
A web application powered by Flask and d3.js
to generate networks/datavisualisations
with datas fetched from the Zotero API

It creates a network linking references with
their tags, groups, collections
---------------------------------------------
licence CC : BY - SA
---------------------------------------------
project by :
Julien Paris & Julien Bellanger

with the support of :
PING / LABOMEDIA
---------------------------------------------
summer 2016 / Nantes - France 
'''

from flask import Flask
import os

from Z2N_vars_app import static_dir ### custom static directory


#app = Flask(__name__)
app = Flask(__name__, static_path = static_dir ) ### change static directory adress to custom for Flask


#### TEST to change static folder's path instead of 'app = Flask(__name__, static_path = static_dir )'
#### ---- NOT WORKING YET !!!! --- 
#### from snippet / url : http://flask.pocoo.org/snippets/102/

#app = MyFlask(__name__, static_folder = None ) #('/static_flask')
#app.config['STATIC_FOLDER'] = static_dir
#app = Flask(__name__)
#app.config['STATIC_FOLDER'] = None
#
#app = Flask(__name__, static_folder = static_dir ) #('/static_flask')
#
#class MyFlask(Flask):
#    @property
#    def static_folder(self):
#        if self.config.get('STATIC_FOLDER') is not None:
#            return os.path.join( self.root_path,
#                                self.config.get('STATIC_FOLDER') )
#    @static_folder.setter
#    def static_folder(self, value) :
#        #### RETURNS ERROR HERE : 'can't assign to function call' and ends 'run.py'
#        self.config.get('STATIC_FOLDER') = value 


from app import views