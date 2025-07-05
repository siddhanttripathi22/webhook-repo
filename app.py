from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from flask_cors import CORS
from datetime import datetime, timezone
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# MongoDB setup
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client.webhookdb
events = db.events

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    action_type = None
    author = "string"
    from_branch = "string"
    to_branch = "string"
    timestamp = datetime.now(timezone.utc)

    if 'pusher' in data:  # Push
        action_type = "push"
        author = data['pusher']['name']
        to_branch = data['ref'].split('/')[-1]
    elif 'pull_request' in data:
        pr = data['pull_request']
        from_branch = pr['head']['ref']
        to_branch = pr['base']['ref']
        author = pr['user']['login']
        if data['action'] == "opened":
            action_type = "pull_request"
        elif data['action'] == "closed" and pr.get('merged', False):
            action_type = "merge"
    else:
        return jsonify({"msg": "Unhandled event"}), 400

    doc = {
        "action_type": action_type,
        "author": author,
        "from_branch": from_branch,
        "to_branch": to_branch,
        "timestamp": timestamp
    }

    events.insert_one(doc)
    return jsonify({"msg": "Event recorded"}), 200

@app.route('/events', methods=['GET'])
def get_events():
    results = events.find().sort("timestamp", -1).limit(10)
    formatted = []

    for e in results:
        time_str = e["timestamp"].strftime('%d %B %Y - %I:%M %p UTC')
        event_obj = {
            "type": e['action_type'],
            "message": "",
            "timestamp": e['timestamp'].isoformat()
        }

        if e['action_type'] == "push":
            event_obj["message"] = f"{e['author']} pushed to {e['to_branch']} on {time_str}"
        elif e['action_type'] == "pull_request":
            event_obj["message"] = f"{e['author']} submitted a pull request from {e['from_branch']} to {e['to_branch']} on {time_str}"
        elif e['action_type'] == "merge":
            event_obj["message"] = f"{e['author']} merged branch {e['from_branch']} to {e['to_branch']} on {time_str}"

        formatted.append(event_obj)

    return jsonify(formatted)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
