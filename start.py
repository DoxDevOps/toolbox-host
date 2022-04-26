import os
import time

time.sleep(10)
os.system(". flask/bin/activate && FLASK_APP=app.py FLASK_ENV=development flask run --port 6070")

