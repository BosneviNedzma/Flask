from flask import Flask, jsonify, redirect, abort
app = Flask(__name__)


@app.route('/user/<username>')
def show_user_profile(username):
    return f'Korisnički profil: {username}'

@app.route('/Pacijent')
def about():
    return 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'


@app.route('/PodaciPacijenta/<ime>/<prezime>/<grad>')
def podaci(ime, prezime, grad):
    podaci = {
        'Ime' : ime, 
        'Prezime' : prezime,
        'Grad u kojem se bolnici nalazi' : grad,
        'Drzava' : "Bosna i Hercegovina"
    }  
    
    return jsonify(podaci)

@app.route('/Pacijent/<redni_broj>')
def pacijent(redni_broj):
    return 'Redni broj pacijenta: ' + str(redni_broj)

@app.route('/greskaZaGreskom')
def greska():
    return redirect('https://www.youtube.com/watch?v=fJ1gPPDCCDU&ab_channel=VojkoV')


@app.route('/dijagnoza/<ime>/<broj_tableta>')
def dijagnoza(ime, broj_tableta):
    return '<h1>Ako ' + ime + ' pije ' + broj_tableta + ' sada dnevno, sa vremenom ce piti duplo manje, ako bude poštovao/la preporuke.'

@app.route('/provjera/<int:id>')
def get_provjera(id):
    if id > 1000:
        return '<h1>ID je izvan vašeg opsega</h1>', 400
    else:
        return '<h1>Vas ID je ispravan!</h1>', 200
    
if __name__ == '__main__':
    app.run()
 


