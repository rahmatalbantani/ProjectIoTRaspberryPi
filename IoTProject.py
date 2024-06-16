import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime, timedelta
import random
import time

# Path to your Firebase service account key JSON file
cred = credentials.Certificate('/home/mahesa/Desktop/Project/IoTProject/ProjectIoTRaspberryPi/ProjectIoT.json')

# Initialize the Firebase app with the service account and database URL
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://projectiot-60c9b-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

# Reference to your Firebase Realtime Database
ref = db.reference('/')

# Function to write data to a specified path in the database
def write_data(path, data):
    try:
        ref.child(path).set(data)
        print(f"Data written to {path}: {data}")
    except Exception as e:
        print(f"Error writing data to {path}: {e}")

# Function to read data from a specified path in the database
def read_data(path):
    try:
        data = ref.child(path).get()
        print(f"Data read from {path}: {data}")
        return data
    except Exception as e:
        print(f"Error reading data from {path}: {e}")
        return None

# Function to simulate sensor detecting changes and updating Firebase
def simulate_sensor():
    while True:
        # Simulate sensor detecting changes (random values for demonstration)
        buzzer_status = random.choice([True, False])  # Example: Random buzzer status
        led_status = random.choice([True, False])  # Example: Random LED status
        
        # Update buzzer and LED statuses in Firebase
        update_led_status(led_status)
        update_buzzer_status(buzzer_status)

        # Print current statuses (optional)
        print(f"LED status: {'active' if led_status else 'inactive'}")
        print(f"Buzzer status: {'active' if buzzer_status else 'inactive'}")

        # Save current status along with event data
        save_event_data(buzzer_status, led_status)

        time.sleep(5)  # Simulate sensor checking every 5 seconds

# Function to update LED status in Firebase
def update_led_status(status):
    try:
        ref.child('status/led').set(status)
        print(f"LED status updated: {status}")
    except Exception as e:
        print(f"Error updating LED status: {e}")

# Function to update buzzer status in Firebase
def update_buzzer_status(status):
    try:
        ref.child('status/buzzer').set(status)
        print(f"Buzzer status updated: {status}")
    except Exception as e:
        print(f"Error updating buzzer status: {e}")

# Function to save event data with current statuses
def save_event_data(buzzer_status, led_status):
    try:
        # Get the current date and time for the event
        tanggal_kejadian = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

        # Define the path and data
        path = f'data/event/{tanggal_kejadian}'
        data = {
            'name': 'Gempa terdeteksi',
            'buzzer_status': buzzer_status,
            'led_status': led_status
        }

        # Write the data to the database
        write_data(path, data)
    except Exception as e:
        print(f"Error saving event data: {e}")

# Example usage
if __name__ == "__main__":
    # Start simulating sensor to update Firebase with buzzer and LED statuses
    simulate_sensor()
