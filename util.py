import youtube_dl

def get_url(url):
    ydl = youtube_dl.YoutubeDL()
    t = ydl.extract_info(url, download=False)
    if 'requested_formats' not in t:
        return {'url' : t['url']}
    else:
        for i in t['requested_formats']:
            if "video" in i['format_note']:
                return {'url' : i['url']}
