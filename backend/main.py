from flask import Flask, request, jsonify
from config import app,db
from models import Contact


@app.route('/contacts', methods=['GET'])
def get_contacts():
    contacts = Contact.query.all()
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify({"contacts": json_contacts})

@app.route("/create", methods=['POST'])
def create_contact():
    first_name = request.json.get("first_name")
    last_name = request.json.get("last_name")
    email = request.json.get("email")
    
    if not first_name or not last_name or not email:
        return (
            jsonify({"message": "Missing data"}),
             400,
        )

    new_contact = Contact(first_name=first_name, last_name=last_name, email=email)
    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}, 400)
    return jsonify({"message": "Contact created successfully"}),201

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    
    app.run(debug=True)