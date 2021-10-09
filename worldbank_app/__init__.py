from flask import Flask

app = Flask(__name__)

#from worldbank_app import routes
import sys
import os.path
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


from worldbank_app import routes
#import app
