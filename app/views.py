"""This is a module"""
from flask_api import FlaskAPI
from datetime import datetime
from instance.config import app_config
from manage import Database
from psycopg2 import connect


from app.models import Questions, Answers, User


def create_app(config_name):
    """This a fuction"""
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    database = Database()


    database.create_all(app)
    Questions


    @app.route('/api/v1/questions', methods=['GET'])
    def get_all_questions():
        return jsonify({'questions': questions})

    @app.route('/api/v2/questions/<int:_id>', methods=['GET'])
    def get_one_question(_id):
        quest = [question for question in questions if question['id'] == _id] or None
        if quest:
            return jsonify({'question': quest[0]})
        else:
            return jsonify({'message': "specific question not found"})
        return jsonify({'message': "You have no question yet"})

    @app.route('/api/v2/questions', methods=['POST'])
    def create_questions():
        data = request.get_json()
        question = data.get('question')
        date_posted = datetime.datetime.now()
        new_question = Questions(question, date_posted)
        new_question.save()
    return jsonify({
        'message': 'success, Question created',
        'question': new_question.save()
    }), 201

    @app.route('/api/v2/questions/<int:_id>/answers', methods=['POST'])
    def post_answer(_id):
        question = [question for question in questions if question['id'] == _id]
        if len(question) == 0:
            return jsonify({'message': 'No question found'})

        data = request.get_json()
        answer = data.get('answer')
        date_posted = datetime.datetime.now()
        post_answer = Answers(answer, date_posted)
        return jsonify({'Question': question}, {
            'message': 'success, Answer created',
            'Answer': post_answer.save()
        }), 201

    @app.route('/api/v2/auth/register', methods=['POST'])
    def post_register():
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        user = User(username, email, password)
        user.save()
        return jsonify({'message':"user created"})
            

    return app
