from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)

@app.route("/", methods=["POST"])
def stress_cpu():
    subprocess.Popen(["python3", "stress_cpu.py"])
    return "Stressing CPU in the background!"

@app.route("/", methods=["GET"])
def get_private_ip():
    private_ip = socket.gethostbyname(socket.gethostname())
    return f"Private IP Address: {private_ip}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
