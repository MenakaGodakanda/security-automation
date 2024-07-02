import os

# Directory containing incident reports
incident_dir = 'incidents/'

# Function to respond to incidents
def respond_to_incidents():
    print("Responding to incidents...")
    incident_files = os.listdir(incident_dir)
    for incident_file in incident_files:
        with open(os.path.join(incident_dir, incident_file), 'r') as f:
            incident = f.read().strip()
            # Respond to the incident (simple print statement for this example)
            print(f"Responding to incident: {incident}")

if __name__ == "__main__":
    respond_to_incidents()
