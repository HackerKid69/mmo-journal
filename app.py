from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///journal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'content': self.content,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

# Create database and tables
with app.app_context():
    db.create_all()

# Serve static files
@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/entries', methods=['GET'])
def get_entries():
    entries = Entry.query.order_by(Entry.updated_at.desc()).all()
    return jsonify([entry.to_dict() for entry in entries])

@app.route('/api/entries', methods=['POST'])
def create_entry():
    data = request.get_json()
    entry = Entry(content=data['content'])
    db.session.add(entry)
    db.session.commit()
    return jsonify(entry.to_dict()), 201

@app.route('/api/entries/<int:entry_id>', methods=['PUT'])
def update_entry(entry_id):
    entry = Entry.query.get_or_404(entry_id)
    data = request.get_json()
    entry.content = data['content']
    db.session.commit()
    return jsonify(entry.to_dict())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
