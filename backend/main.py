from flask import Flask, request, jsonify
from config import app,db
from models import Contact


@app.route('/contacts', methods=['GET'])
def get_contacts():
    contacts = Contact.query.all()
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify({"contacts": json_contacts})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    
    app.run(debug=True)