from flask import Flask, redirect, jsonify, request, render_template
import json

app = Flask(__name__)

app.config['SECRET_KEY'] = 'top secret!'

a = []

@app.route('/', methods=['GET'])
def view():
    if request.method == 'GET':
        return render_template('home.html', items=a)

@app.route('/data', methods=['POST'])
def listings():
    if request.method == 'POST':
        listing = json.loads(request.data)
        print(listing)
        a.append(listing)
        return jsonify({'success': True}), 200


if __name__ == '__main__':
    app.run(debug=True)
