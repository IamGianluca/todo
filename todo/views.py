from flask import Blueprint
from flask import abort, current_app, g, make_response, jsonify

from todo.models import Task


todo = Blueprint('todo', __name__)


@todo.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@todo.route('/', methods=['GET'])
def check_health():
    return jsonify({'health': 'okay'})


@todo.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    """Retrieve all tasks."""
    return jsonify({'task': 1})


@todo.route('/todo/api/v1.0/tasks/<task_id>', methods=['GET'])
def get_task(task_id):
    tasks = Task.query.all()
    return jsonify(json_list=[todo.as_dict() for todo in tasks])
