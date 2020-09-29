from flask import Flask, make_response
from flask import abort
from fibonacci import Solution

fibapp = Flask(__name__)

@fibapp.route('/')
def index():
    return "RESTful service in Python"

@fibapp.route('/fib/<int:x>', methods=['GET'])
def fib(x):
    """
    Given the condition in fibonacci.py, which is about the first and the second fibonacci number
    It would be better to generate an error when 0, 1 as parameter are computed
    rather than to return empty lists
    """
    if x >= 2:
        response = make_response(str(Solution(x)), 200)
    else:
        abort(404)
    return response

@fibapp.route('/health', methods=['GET'])
def test_health():
    return "service status: good"

if __name__ == '__main__':
    fibapp.run()

