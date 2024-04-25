from flask import Flask, request

app = Flask(__name__)
@app.route('/getsetgo', methods=['GET'])
def getsetgo():
    try:
        url = request.args.get('url')
        if url.startswith('http://') or url.startswith('https://'):
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
            else:
                return f"Failed to download file from {url}. Status code: {response.status_code}"
        else:
            return "Invalid URL"
    except Exception as e:
        return f"An error occurred while downloading {url}: {e}"__name__
