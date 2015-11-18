# curl -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"url":"https://www.youtube.co/watch?v=yZjSfnLUTPk"}' 127.0.01:5000/api/v1.0/ytdl

from flask import Flask, jsonify, request, render_template
from util import get_url
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        f = request.form
        url =  get_url(request.form['url'])
        return render_template('dl.html', url=url)
        return "at your service"
    else:
        return render_template('index.html')


@app.route('/api/v1.0/ytdl', methods=['GET', 'POST'])
def get_json():
    content = request.json
    return jsonify(get_url(content['url']))

@app.errorhandler(500)
def internal_error(error):
    return "500 error", 500

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)


