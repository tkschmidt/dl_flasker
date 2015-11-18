# curl -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"url":"https://www.youtube.co/watch?v=yZjSfnLUTPk"}' 127.0.01:5000/api/v1.0/ytdl

from flask import Flask, jsonify, request
import youtube_dl

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World"


@app.route('/api/v1.0/ytdl', methods=['GET', 'POST'])
def get_json():
    content = request.json
    print content
    ydl = youtube_dl.YoutubeDL()
    t = ydl.extract_info(content['url'], download=False)
    if 'requested_formats' not in t:
        print t['url']
        return jsonify({'url' : t['url']})
    else:
        for i in t['requested_formats']:
            if "video" in i['format_note']:
                print i['url']
                return jsonify({'url' : i['url']})


if __name__ == '__main__':
    app.run(debug=True)


