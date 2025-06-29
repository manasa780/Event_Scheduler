# 📅 Event Scheduler System (Flask API)

This project is a simple Event Scheduler API built with Flask in Python.  
It allows users to create, view, update, and delete events. It also supports event reminders for events happening within the next hour.

---

## ✅ Features

- Add new events
- View all scheduled events
- Update an existing event
- Delete an event
- Reminders for upcoming events (prints in terminal)

---

## 🚀 How to Run

### 1. Clone or Download

Place the project in a folder like:

event_scheduler/
├── app.py
├── events.json
├── requirements.txt
├── README.md

### 2. Create Virtual Environment

python -m venv venv
.\venv\Scripts\activate

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Run the App

python app.py

Server will run at:
http://127.0.0.1:5000

📬 API Endpoints


➤ POST /events — Create Event

Headers: Content-Type: application/json

Body Example:

{
  "title": "Doctor Appointment",
  
  "description": "Visit KIMS Hospital",
  
  "start_time": "2025-06-29 14:00",
  
  "end_time": "2025-06-29 15:00"
}

➤ GET /events — View All Events

Returns a list of events sorted by start time.

➤ PUT /events/<event_id> — Update Event

Example: PUT /events/1

Body Example:

{
  "title": "Dentist Visit",
  
  "description": "Updated time",
  
  "start_time": "2025-06-29 16:00",
  
  "end_time": "2025-06-29 17:00"
}

➤ DELETE /events/<event_id> — Delete Event


Example: DELETE /events/1

🛠 Sample Data (events.json)

[
  {
   
    "id": 1,
    
    "title": "Doctor Appointment",
    
    "description": "Visit KIMS Hospital",
    
    "start_time": "2025-06-29 14:00",
    
    "end_time": "2025-06-29 15:00"
  }
]

🔔 Reminder Feature


Every 1 minute, the system checks for events starting within the next hour and prints:


Upcoming Events within the next hour:


- Doctor Appointment at 2025-06-29 14:00



🙋 Contact
For any issues, contact:
Manasa Kore | koremanasa570@gmail.com


