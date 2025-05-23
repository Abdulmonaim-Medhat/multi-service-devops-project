from flask import Flask, request, jsonify

app = Flask(__name__)
users = []  # In-memory "database"

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({"users": users})

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    users.append(data)
    return jsonify({"message": "User added", "user": data}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)