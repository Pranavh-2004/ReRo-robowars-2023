# Team 405 Found - ReRo 24hr Hackathon

Welcome to Team 405 Found's repository for the ReRo 24hr Hackathon! This project demonstrates our solution to remotely control a bot using Python. Our bot is designed to follow a line path from start to finish by processing sensor data and issuing motor commands accordingly.

---

# 👥 Team Members

- Kshitij Koushik Kota - PES1UG23CS908 [GitHub](https://github.com/kshitijkota)
- Pranav Hemanth - PES1UG23CS433 [GitHub](https://github.com/Pranavh-2004)
- Sampriti Saha - PES1UG23CS505 [GitHub](https://github.com/Sampriti2803)
- Pranav Rajesh Narayan - PES1UG23CS435 [Github](https://github.com/pranav-rn)
- Roshini Ramesh - PES1UG23CS488 [Github](https://github.com/roshr22)

---

## 📋 Project Description

In this hackathon, we created a Python-based solution to enable our bot to follow a line autonomously. The bot reads sensor data representing line detection and determines motor actions in real time. The objective was to reach the endpoint efficiently and accurately.

---

## 🚀 Project Structure

### `client_robowars1.py`

- This file contains the main client-side code that reads sensor data from the bot and sends control commands to adjust the bot’s movement.
- The bot uses a sensor array with 5 sensors (labeled `s1` to `s5`) to detect the line. A value of `1` means the sensor detects the line; otherwise, it's `0`.

### `server_robowars1.py`

- This file simulates a server environment to test the bot’s client-side script.
- It establishes a socket connection and sends sample sensor data to the client, allowing us to simulate the competition’s live server environment.

---

## 📡 Communication Protocol

The bot connects to an ESP32 board using Python sockets. Here’s an overview of the data exchange:

1. **Input Format:** JSON object `{'s1':0, 's2':0, 's3':0, 's4':1, 's5':0}` (left-to-right sensor data).
2. **Output Format:** Motor commands in the format `'motor "f" "50" "b" "50"\n'`, where:
   - `"f"` and `"b"` represent forward and backward movement, respectively.
   - The first `50` controls the left motor, and the second `50` controls the right motor.

### Example Communication

- **Input from Server:** `{'s1':0, 's2':1, 's3':1, 's4':0, 's5':0}`
- **Output from Client:** `'motor "f" "40" "b" "60"\n'`

---

## ⚙️ Setup Instructions

### Running the Client

To run the client script and simulate control commands:

1. Ensure Python is installed.
2. Run the client script with the provided server IP and port.

```bash
python client_robowars1.py <ip_address> <port>
```

### Simulating the Server

For testing purposes, run the server script to simulate sensor data:

```bash
python server_robowars1.py
```

---

## 🔧 Testing and Error Handling

- **Exception Handling:** Both client and server scripts handle exceptions to avoid connection errors.
- **Socket Closure:** Each script ensures socket connections are closed using a finally block to maintain stability.
- **Logs:** Print statements log data flow for real-time debugging.

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.
