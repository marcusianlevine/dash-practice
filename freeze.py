from app import app
from flask_frozen import Freezer

s = app.server

s.config['FREEZER_BASE_URL'] = 'http://localhost/'
s.config['FREEZER_RELATIVE_URLS'] = True
s.config['FREEZER_DESTINATION'] = '/Users/mlevine/Code/dash-practice/build'

f = Freezer(s)

@f.register_generator
def dash_urls():
    yield '/'

if __name__ == '__main__':
    f.freeze()