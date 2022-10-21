import requests
from flask import Flask, render_template

app = Flask(__name__)


def fetchMeme():
    response = requests.get('https://meme-api.herokuapp.com/gimme')
    return response.json()


@app.get('/')
def LoginPage():
    data_url = fetchMeme()['url']
    return render_template('main.html', memes_image=data_url)


if __name__ == '__main__':
    app.run(debug=True)
