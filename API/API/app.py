from flask import Flask, jsonify, request, g
from flask_cors import CORS
import mysql.connector


app = Flask(__name__)


CORS(app, resources={r"/api/*": {"origins": "*"}})
@app.after_request
def add_cors_headers(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


# Create a connection to the database
def get_db():
    if not hasattr(g, 'db'):
        g.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="entreprise"
        )
    return g.db

# Close the connection to the database
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'db'):
        g.db.close()

@app.route('/api/v1/employees', methods=['GET'])
def get_employees():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees")
    rows = cur.fetchall()
    employees = []
    for row in rows:
        employee = {
            'id': row[0],
            'firstName': row[1],
            'lastName': row[2],
            'emailId': row[3]
        }
        employees.append(employee)
    cur.close()
    return jsonify(employees)


@app.route('/api/v1/employees', methods=['POST'])
def add_employee():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO employees (id, firstName, lastName, emailId) VALUES (%s, %s, %s, %s)", (request.json['id'], request.json['firstName'], request.json['lastName'], request.json['emailId']))
    conn.commit()
    cur.close()
    return jsonify({'message': 'Employee added successfully'})

@app.route('/api/v1/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM employees WHERE id = %s", (id,))
    conn.commit()
    cur.close()
    return jsonify({'message': 'Employee deleted successfully'})

@app.route('/api/v1/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("UPDATE employees SET firstName=%s, lastName=%s, emailId=%s WHERE id=%s", (request.json['firstName'], request.json['lastName'], request.json['emailId'], id))
    conn.commit()
    cur.close()
    return jsonify({'message': 'Employee updated successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
