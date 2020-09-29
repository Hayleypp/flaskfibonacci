### RESTful API service in Python using Flask

provision of combinations of fibonacci numbers that sum up to a certain number



##### Requirements

Python 2.x or 3.x (verified on 2.7 and 3.7, virtual environment: pipenv)

Flask



##### Usage

git clone   git@github.com:Hayleypp/flaskfibonacci.git

cd flask

flask run



##### Request

The request format is /fib/integer

For instance, in the case of "/fib/11, It returns [[2, 2, 2, 2, 3], [2, 2, 2, 5], [2, 3, 3, 3], [3, 3, 5], [8, 3]] 



##### Response

If the request is successful, the response will be returned with status code “200”. 

Otherwise “404’ would be. For example, input is 0, 1 or string type.