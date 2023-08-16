from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.base_model import BaseModel
import json

class Flashcard(BaseModel):

    json_fields = ['id', 'word', 'pronunciation_audio_url', 'translation', 'definition', 'ai_generated_image_url', 'saved', 'created_at', 'updated_at']
    def __init__( self , data ):
        self.id = data['id']
        self.word = data['word']
        self.pronunciation_audio_url = data['pronunciation_audio_url']
        self.translation = data['translation']
        self.definition = data['definition']
        self.ai_generated_image_url = data['ai_generated_image_url']
        self.saved = data['saved']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users = []

    @classmethod
    def get_all_flashcards(cls):
        query = "SELECT * FROM flashcards;"
        results = connectToMySQL('MultiLingo').query_db(query)
        flashcards = []
        for flashcard in results:
            flashcards.append(cls(flashcard))
        return flashcards
    
    @classmethod
    def get_flashcard_by_id(cls, data):
        query = "SELECT * FROM flashcards WHERE id = %(id)s;"
        results = connectToMySQL('MultiLingo').query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def get_flashcard_by_word(cls, data):
        query = "SELECT * FROM flashcards WHERE word = %(word)s;"
        results = connectToMySQL('MultiLingo').query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def get_saved_flashcard_by_user_id(cls, data):
        query = """ 
                SELECT * FROM flashcards
                WHERE flashcards.user_id = %(id)s AND flashcards.saved = 1;
            """
        results = connectToMySQL('MultiLingo').query_db(query, data)
        flashcards = []
        for flashcard in results:
            flashcards.append(cls(flashcard))
        return flashcards
    
    @classmethod

    def get_language_flashcard_by_user_id(cls, data):
        query = """ 
                SELECT * FROM flashcards
                WHERE flashcards.user_id = %(id)s AND flashcards.language_id = %(language_id)s;
            """
        results = connectToMySQL('MultiLingo').query_db(query, data)
        flashcards = []
        for flashcard in results:
            flashcards.append(cls(flashcard))
        return flashcards
    
    @classmethod
    def save_flashcard(cls, data):
        query = "INSERT INTO flashcards (word, pronunciation_audio_url, translation, definition, ai_generated_image_url, saved, user_id, language_id, created_at, updated_at) VALUES (%(word)s, %(pronunciation_audio_url)s, %(translation)s, %(definition)s, %(ai_generated_image_url)s, %(saved)s, %(user_id)s, %(language_id)s, NOW(), NOW());"
        return connectToMySQL('MultiLingo').query_db(query, data)
    
    @classmethod
    def update_flashcard(cls, data):
        query = "UPDATE flashcards SET word = %(word)s, pronunciation_audio_url = %(pronunciation_audio_url)s, translation = %(translation)s, definition = %(definition)s, ai_generated_image_url = %(ai_generated_image_url)s, saved = %(saved)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('MultiLingo').query_db(query, data)
    
    @classmethod
    def delete_flashcard(cls, data):
        query = "DELETE FROM flashcards WHERE id = %(id)s;"
        return connectToMySQL('MultiLingo').query_db(query, data)
    
        