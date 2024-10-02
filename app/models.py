from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ChatHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_input = db.Column(db.String, nullable=False)
    ai_response = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<ChatHistory {self.id}: {self.user_input} - {self.ai_response}>'