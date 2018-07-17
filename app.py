from flask import Flask, redirect, jsonify, request, render_template
import json
import base64

app = Flask(__name__)

app.config['SECRET_KEY'] = 'top secret!'

a = []

@app.route('/', methods=['GET'])
def view():
    if request.method == 'GET':
        return render_template('home.html', items=a)

@app.route('/_ah/push-handlers/receive_message', methods=['POST'])
def listings():
    if request.method == 'POST':
        req_data = json.loads(request.data)['message']
        coded_string = req_data['data']
        history_id = eval(base64.b64decode(coded_string))['historyId']
        req_data['computed'] = {'history_id': history_id}
        a.append({req_data['publishTime']: req_data})
        return jsonify({'success': True}), 200


if __name__ == '__main__':
    app.run(debug=True)
