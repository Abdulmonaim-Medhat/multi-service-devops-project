import requests

SERVICE_A_URL = "http://service_a:5000"  # Docker Compose network name

def process_users():
    response = requests.get(f"{SERVICE_A_URL}/users")
    users = response.json().get('users', [])
    return {"count": len(users), "users": users}

if __name__ == '__main__':
    from flask import Flask, jsonify
    app = Flask(__name__)

    @app.route('/process')
    def process():
        result = process_users()
        return jsonify(result)

    app.run(host='0.0.0.0', port=6000)