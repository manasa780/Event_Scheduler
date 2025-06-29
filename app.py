from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import threading
import time
import json
import os

app = Flask(__name__)

DATA_FILE = 'events.json'

# Load and save functions
def load_events():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_events(events):
    with open(DATA_FILE, 'w') as f:
        json.dump(events, f, indent=4)

# In-memory store
events = load_events()

# Function to get next available numeric ID
def get_next_id():
    if not events:
        return 1
    return max(int(event["id"]) for event in events) + 1

# Reminder function
def check_reminders():
    while True:
        now = datetime.now()
        upcoming = []
        for event in events:
            start_time = datetime.strptime(event['start_time'], "%Y-%m-%d %H:%M")
            if 0 <= (start_time - now).total_seconds() <= 3600:
                upcoming.append(event)
        if upcoming:
            print("\nUpcoming Events within the next hour:")
            for e in upcoming:
                print(f"- {e['title']} at {e['start_time']}")
        time.sleep(60)

# Start reminder thread
threading.Thread(target=check_reminders, daemon=True).start()

@app.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    try:
        new_event = {
            "id": get_next_id(),
            "title": data['title'],
            "description": data['description'],
            "start_time": data['start_time'],
            "end_time": data['end_time']
        }
        events.append(new_event)
        save_events(events)
        return jsonify({"message": "Event created successfully!", "event": new_event}), 201
    except KeyError:
        return jsonify({"error": "Missing required fields."}), 400

@app.route('/events', methods=['GET'])
def list_events():
    sorted_events = sorted(events, key=lambda e: datetime.strptime(e['start_time'], "%Y-%m-%d %H:%M"))
    return jsonify(sorted_events)

@app.route('/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    data = request.get_json()
    for event in events:
        if event['id'] == event_id:
            event.update({k: v for k, v in data.items() if k in ['title', 'description', 'start_time', 'end_time']})
            save_events(events)
            return jsonify({"message": "Event updated successfully!", "event": event})
    return jsonify({"error": "Event not found."}), 404

@app.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    global events
    new_events = [e for e in events if e['id'] != event_id]
    if len(new_events) == len(events):
        return jsonify({"error": "Event not found."}), 404
    events = new_events
    save_events(events)
    return jsonify({"message": "Event deleted successfully!"})

if __name__ == '__main__':
    app.run(debug=True)