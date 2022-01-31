from flask import Flask, request, jsonify, send_from_directory, render_template
import bcrypt

db = {}

app = Flask(__name__)

@app.route('/add-user', methods=['POST'])
def add_user():
    # requires username and password in post data
    # check that username is exists and correct
    data = request.get_json()
    if 'username' not in data:
        return jsonify({'error': 'username not found'}), 400
    if data['username'] in db:
        return jsonify({'error': 'username already exists'}), 400

    # check that password is exists and correct
    if 'password' not in data:
        return jsonify({'error': 'password not found'}), 400
    if len(data['password']) < 8:
        return jsonify({'error': 'password must be at least 8 characters'}), 400

    # store username and password in db
    hash_pw = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())

    db[data['username']] = hash_pw
    return jsonify({'success': 'user creation successful'})

@app.route('/login', methods=['POST'])
def login():
    # requires username and password in post data
    # check that username is exists and correct
    data = request.get_json()
    if 'username' not in data:
        return jsonify({'error': 'username not found'}), 400
    if data['username'] not in db:
        return jsonify({'error': 'username not found'}), 400

    # check that password is exists and correct
    if 'password' not in data:
        return jsonify({'error': 'password not found'}), 400

    # check that password is correct
    if not bcrypt.checkpw(data['password'].encode('utf-8'),
                          db[data['username']]):
        return jsonify({'error': 'password not correct'}), 400

    return jsonify({'success': 'login successful'})


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)

if __name__=='__main__':
    app.run(host="0.0.0.0", port=80)

