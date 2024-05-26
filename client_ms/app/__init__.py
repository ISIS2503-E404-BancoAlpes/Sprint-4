from flask import Flask, session
from flask_session import Session
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.config.from_object('config.Config')

# Setup session
Session(app)

# Setup OAuth
oauth = OAuth(app)
auth0 = oauth.register(
    'auth0',
    client_id=app.config['AUTH0_CLIENT_ID'],
    client_secret=app.config['AUTH0_CLIENT_SECRET'],
    api_base_url=app.config['AUTH0_BASE_URL'],
    access_token_url=app.config['AUTH0_BASE_URL'] + '/oauth/token',
    authorize_url=app.config['AUTH0_BASE_URL'] + '/authorize',
    client_kwargs={
        'scope': 'openid profile email',
    },
)
