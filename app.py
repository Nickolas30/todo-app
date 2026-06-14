from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task = {'id': len(tasks) + 1, 'text': data['text'], 'done': False}
    tasks.append(task)
    return jsonify(task), 201

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return jsonify({'result': 'deleted'})

@app.route('/tasks/<int:task_id>/toggle', methods=['PUT'])
def toggle_task(task_id):
    for t in tasks:
        if t['id'] == task_id:
            t['done'] = not t['done']
    return jsonify({'result': 'updated'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)