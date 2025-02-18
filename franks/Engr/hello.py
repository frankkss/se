from flask import Flask, request, jsonify
import traci  # SUMO TraCI module

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the SUMO Traffic Simulation API!"

# Endpoint to start a SUMO simulation
@app.route('/start-simulation', methods=['POST'])
def start_simulation():
    try:
        # Path to your SUMO configuration file
        sumo_cmd = ["sumo-gui", "-c", "C:\s\RL-TrafficLight-Control-Adaptive-Traffic-Management\TLCS"]
        
        # Start the TraCI interface
        traci.start(sumo_cmd)
        return jsonify({"message": "Simulation started successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to interact with the simulation
@app.route('/set-traffic-light', methods=['POST'])
def set_traffic_light():
    try:
        data = request.json
        traffic_light_id = data['id']
        phase_index = data['phase']
        
        # Set traffic light phase
        traci.trafficlight.setPhase(traffic_light_id, phase_index)
        return jsonify({"message": "Traffic light updated"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to stop the simulation
@app.route('/stop-simulation', methods=['POST'])
def stop_simulation():
    try:
        traci.close()
        return jsonify({"message": "Simulation stopped"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)