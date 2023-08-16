from flask_app import app
from flask_app.controllers import users, languages, flashcards
from flask_cors import CORS

CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}}, support_credentials=True)

if __name__ == "__main__":
    app.run(debug=True)