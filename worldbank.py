#from worldbank_app import app
import os.path
import sys
#sys.path.append("worldbank_app")
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from worldbank_app import app

app.run(host='0.0.0.0', port=3001, debug=True)