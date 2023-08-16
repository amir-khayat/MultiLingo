from flask import jsonify, request
from flask_app import app
from flask_app.models.flashcard import Flashcard

@app.route('/flashcards', methods=['GET'])
def flashcards():
    flashcards = Flashcard.get_all_flashcards()
    return jsonify(flashcards), 200

@app.route('/flashcards/<int:flashcard_id>', methods=['GET'])
def flashcard(flashcard_id):
    data = {'id': flashcard_id}
    flashcard = Flashcard.get_flashcard_by_id(data)
    return jsonify(flashcard), 200

@app.route('/flashcards/word/<string:word>', methods=['GET'])
def flashcard_by_word(word):
    data = {'word': word}
    flashcard = Flashcard.get_flashcard_by_word(data)
    return jsonify(flashcard), 200

@app.route('/flashcards/user/<int:user_id>', methods=['GET'])
def saved_flashcards_by_user(user_id):
    data = {'id': user_id}
    flashcards = Flashcard.get_saved_flashcard_by_user_id(data)
    return jsonify(flashcards), 200

@app.route('/add_flashcard', methods=['POST'])
def create_flashcard():
    data = {
        'word': request.json['word'],
        'pronunciation_audio_url': request.json['pronunciation_audio_url'],
        'translation': request.json['translation'],
        'definition': request.json['definition'],
        'ai_generated_image_url': request.json['ai_generated_image_url'],
        'saved': request.json['saved'],
        'user_id': request.json['user_id'],
        'language_id': request.json['language_id']
    }
    flashcard_id = Flashcard.save_flashcard(data)
    return jsonify({'success': True, 'flashcard_id': flashcard_id}), 200

@app.route('/flashcards/<int:flashcard_id>', methods=['PUT'])
def update_flashcard(flashcard_id):
    data = {
        'id': flashcard_id,
        'word': request.json['word'],
        'pronunciation_audio_url': request.json['pronunciation_audio_url'],
        'translation': request.json['translation'],
        'definition': request.json['definition'],
        'ai_generated_image_url': request.json['ai_generated_image_url'],
        'saved': request.json['saved']
    }
    Flashcard.update_flashcard(data)
    return jsonify({'success': True}), 200

@app.route('/flashcards/<int:flashcard_id>', methods=['DELETE'])
def delete_flashcard(flashcard_id):
    data = {'id': flashcard_id}
    Flashcard.delete_flashcard(data)
    return jsonify({'success': True}), 200
