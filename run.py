#!venv/bin/python
''' venv = name of virtual environnement'''
from app import app
import os

cwd       = os.getcwd()
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

print cwd
print SITE_ROOT

app.run(debug=True) ### restart server at every change in code