from flask import Blueprint
from flask import abort, make_response, jsonify


todo = Blueprint('todo', __name__)


@todo.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@todo.route('/', methods=['GET'])
def check_health():
    return jsonify({'health': 'okay'})


@todo.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'task': 1})


@todo.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})
