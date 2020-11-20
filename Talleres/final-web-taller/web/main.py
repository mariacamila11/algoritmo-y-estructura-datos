from flask import Flask, request, make_response, redirect, render_template, url_for

# se crea un objeto del tipo app
app = Flask(__name__)

@app.route('/')
def baseRoute():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/doctors')
def doctorsRoute():
    return render_template('doctors.html')

@app.route('/information')
def informationRoute():
    return render_template('information.html')

@app.route('/services')
def servicesRoute():
    return render_template('services.html')

@app.route('/contacts')
def contactsRoute():
    return render_template('contacts.html')
    
if __name__ == '__main__':
    app.run()
