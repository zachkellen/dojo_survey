from flask import flash, request
from mysqlconnection import connectToMySQL


class Survey():
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_survey(cls, data):
        query = "INSERT INTO students (name, location, language, comment) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);"
        new_survey = connectToMySQL('dojo_survey_schema').query_db(query, data)
        return new_survey

    @staticmethod
    def validate_survey(survey):
        is_valid = True
        if len(survey['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(survey['location']) < 3:
            flash("Location must be at least 3 characters.")
            is_valid = False
        if len(survey['language']) < 3:
            flash("Language must be at least 3 characters.")
            is_valid = False
        if len(survey['comment']) < 1:
            flash("A comment is required.")
            is_valid = False
        return is_valid