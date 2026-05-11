import os, random, math
from flask import Flask, session, url_for, request, redirect, render_template, jsonify
from flask_session import Session
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Permite transporte HTTP para desenvolvimento local (importante para o Spotify Callback)
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(64)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# CREDENCIAIS SPOTIFY (Mantenha as suas originais aqui)
CLIENT_ID = "3e3ae82b8e834bc0a68dd4b9c462c268"
CLIENT_SECRET = "0f2e1d2fec4e489583e484c6a5a84b9e"
REDIRECT_URI = "http://127.0.0.1:5000/callback"
SCOPE = "user-read-currently-playing user-top-read user-read-recently-played"

# LISTA DE INTERESSES PARA O SETUP
INTERESTS_LIST = [
    "JDM / Drift", "Stance / Euro", "Som Automotivo", "Track Days", 
    "Techno / Melodic", "Phonk", "Hip Hop / Trap", "Indie Rock", 
    "House Music", "Festas & Raves", "Gastronomia", "Viagens", 
    "Produção Musical", "Vinil", "Gamer", "Sneakers", "BMW Life", "Turbo Culture"
]

users_db = []

def generate_bots(lat, lon):
    """Gera almas musicais orbitando a sua localização real"""
    global users_db
    names = ["Rodrigo", "Felipe", "Lucas", "Bia", "Enzo", "Valentina", "Gabriel", "Julia"]
    musics = ["Starboy", "505", "Blinding Lights", "FE!N", "Die For You", "Nightcall"]
    bios = [
        "Vibe automotiva e som no talo! 🏎️💨",
        "Ouvindo techno e pensando no próximo track day.",
        "Procurando conexões reais através da música.",
        "JDM culture is my life. BMW lover.",
        "Se a batida for boa, eu tô lá.",
        "A música é o que me move."
    ]
    for i in range(20):
        # Gera órbita ao redor da Pietra (raio de ~5km)
        off_lat, off_lon = random.uniform(-0.02, 0.02), random.uniform(-0.02, 0.02)
        users_db.append({
            'id': f"bot_{i}", 
            'name': random.choice(names), 
            'age': random.randint(19, 28),
            'lat': lat + off_lat, 
            'lon': lon + off_lon, 
            'music': random.choice(musics),
            'bio': random.choice(bios),
            'photo': f"https://i.pravatar.cc/600?img={i+20}"
        })

@app.route('/')
def index(): 
    return render_template('home.html')

@app.route('/login')
def login():
    auth = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, 
                        redirect_uri=REDIRECT_URI, scope=SCOPE, show_dialog=True)
    return redirect(auth.get_authorize_url())

@app.route('/callback')
def callback():
    auth = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI)
    session['token_info'] = auth.get_access_token(request.args.get('code'))
    return render_template('loading.html')

@app.route('/save_location', methods=['POST'])
def save_location():
    data = request.json
    session['location'] = {'lat': data['lat'], 'lon': data['lon']}
    if not users_db: 
        generate_bots(data['lat'], data['lon'])
    return jsonify({'status': 'ok'})

@app.route('/setup')
def setup(): 
    return render_template('setup.html', interests=INTERESTS_LIST)

@app.route('/save_profile', methods=['POST'])
def save_profile():
    interests = request.form.get('interests', '').split(',')
    session['user_profile'] = {
        'age': request.form.get('age'),
        'bio': request.form.get('bio'),
        'fav_music': request.form.get('fav_music'),
        'interests': [i for i in interests if i]
    }
    return redirect(url_for('music_sync'))

@app.route('/music')
def music_sync():
    token = session.get('token_info')
    if not token: return redirect('/')
    
    sp = spotipy.Spotify(auth=token['access_token'])
    
    try:
        curr = sp.current_user_playing_track()
        
        # Detecção de Silêncio Real
        if curr is None or not curr.get('is_playing'):
            track, artist, img = "Silêncio...", "", ""
        else:
            track = curr['item']['name']
            artist = curr['item']['artists'][0]['name']
            img = curr['item']['album']['images'][0]['url']
        
        session['current_music'] = track
        return render_template('music.html', user={
            'name': sp.current_user()['display_name'], 
            'photo': img, 
            'music': track, 
            'artist': artist
        })
    except:
        return redirect('/')

@app.route('/radar', methods=['POST'])
def radar():
    # Redireciona para o tutorial de gravidade
    return render_template('search.html')

@app.route('/discover_list')
def discover_list():
    my_loc = session.get('location')
    token = session.get('token_info')
    if not my_loc or not token: return redirect('/')
    
    # Puxa sua foto real do Spotify para o centro da galáxia
    sp = spotipy.Spotify(auth=token['access_token'])
    me = sp.current_user()
    my_photo = me['images'][0]['url'] if me['images'] else "https://i.pravatar.cc/300"

    matches = []
    for bot in users_db:
        dist = math.sqrt((my_loc['lat']-bot['lat'])**2 + (my_loc['lon']-bot['lon'])**2) * 111
        bot['distance'] = f"{dist:.1f} km"
        matches.append(bot)
    
    # Renderiza a órbita com potential_matches e a user_photo
    return render_template('discover.html', 
                           potential_matches=matches, 
                           user_photo=my_photo)

@app.route('/chat')
def chat():
    # Rota para o próximo estágio do projeto
    return "<h1>Syncora Chat</h1><p>Em breve: Converse na mesma frequência.</p>"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)