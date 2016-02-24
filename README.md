# Feature Request App

## Features

- Creating and editing requests
- Priorities reshuffle existing requests

## How to Use

To use this project, follow these steps:

1. Install Python 2.7
2. Clone the repository
3. Install requirements (`$ mana.p install -r requirements.txt`)
4. Run the project locally via (`$ manage.py runserver`)
5. Load in the initial data via (`$ manage.py migrate`)
5. Access [locally](http://localhost:8000)

## How To Use Heroku [For a demo of Heroku deployment, click here](https://sheltered-cliffs-66207.herokuapp.com/)

1. Install and setup Heroku Deployment Tools
2. Clone the repository
3. Inside the repository setup heroku via (`$ heroku create`) - This should add 'heroku' remote to local repository
4. Push your code to your heroku instance (`$ git push heroku master`)
5. Load in the initial data via (`$ heroku run python manage.py`)
6. Access URL (hint: run `$ heroku open` to get the URL)

## Further Reading

- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)
