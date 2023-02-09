# flask needs app.py to run

from flask import *
from whitenoise import WhiteNoise  # treat like black box

app = Flask(__name__)
app.wsgi_app = WhiteNoise(app.wsgi_app,
                          root='static/',
                          prefix='',
                          index_file="index.html",
                          autorefresh=True)  # plug into flask something to help us send files, needs root and prefix


if __name__ == "__main__":
    app.run(threaded=True, port=5000)
1