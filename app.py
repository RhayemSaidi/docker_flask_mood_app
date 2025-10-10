from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Homepage
@app.route('/')
def home():
    return render_template('index.html')

# API endpoint for random mood
@app.route('/mood')
def mood():
    moods = [
        "🌞 You’re doing better than you think.",
        "🌿 Take a breath. You’ve got this.",
        "🌙 It’s okay to rest for a while.",
        "🔥 Keep going, your effort matters.",
        "🌸 You’re growing in quiet ways too.",
        "☕ Slow progress is still progress."
    ]
    return jsonify({"message": random.choice(moods)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
