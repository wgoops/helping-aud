from flask import Flask, render_template, request, jsonify
import os
import csv
from datetime import datetime
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def validate_csv(file_stream):
    reader = csv.DictReader(file_stream)

    # Check CSV headers
    expected_headers = ["Doctor ID", "Number of Diagnoses", "Number of Medications", "Number of Patients", "Last Appointment Date", "Total Cost Billed"]
    if set(expected_headers) != set(reader.fieldnames):
        return False, "CSV headers do not match the expected format."

    for row in reader:
        # Validate Doctor ID (assuming it's alphanumeric)
        if not row["Doctor ID"].isalnum():
            return False, f"Invalid Doctor ID: {row['Doctor ID']}"

        # Validate integer fields
        for field in ["Number of Diagnoses", "Number of Medications", "Number of Patients"]:
            try:
                int(row[field])
            except ValueError:
                return False, f"Invalid value for {field}: {row[field]}"

        # Validate Last Appointment Date
        try:
            datetime.strptime(row["Last Appointment Date"], '%Y-%m-%d')
        except ValueError:
            return False, f"Invalid Last Appointment Date: {row['Last Appointment Date']}"

        # Validate Total Cost Billed as a float
        try:
            float(row["Total Cost Billed"])
        except ValueError:
            return False, f"Invalid Total Cost Billed: {row['Total Cost Billed']}"

    return True, "CSV is valid!"

@app.route('/', methods=['GET'])
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Validate the CSV
        with open(filepath, 'r') as f:
            valid, message = validate_csv(f)

        os.remove(filepath)  # Delete file after validation

        if valid:
            return jsonify({"status": "success", "message": "CSV is valid!"})
        else:
            return jsonify({"status": "failure", "message": message}), 400

    return jsonify({"error": "Invalid file type"}), 400

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)