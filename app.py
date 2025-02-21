from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/wordcount', methods=['POST'])
def word_count():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({"error": "Invalid input"}), 400

    text = data['text']
    word_count = len(text.split())
    return jsonify({"word_count": word_count})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

