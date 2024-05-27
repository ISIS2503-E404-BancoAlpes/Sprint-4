from flask import redirect, url_for, session, request, render_template
from app import app, auth0
from urllib.parse import urlencode

@app.route('/')
def index():
    return "Bienvenido al microservicio de clientes!"

@app.route('/login')
def login():
    return auth0.authorize_redirect(redirect_uri=url_for('callback', _external=True))

@app.route('/callback')
def callback():
    auth0.authorize_access_token()
    resp = auth0.get('userinfo')
    userinfo = resp.json()
    session['jwt_payload'] = userinfo
    session['profile'] = {
        'user_id': userinfo['sub'],
        'name': userinfo['name'],
        'picture': userinfo['picture']
    }
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    return f"Hola {session['profile']['name']}!"

@app.route('/logout')
def logout():
    session.clear()
    params = {'returnTo': url_for('index', _external=True), 'client_id': app.config['AUTH0_CLIENT_ID']}
    return redirect(auth0.api_base_url + '/v2/logout?' + urlencode(params))
