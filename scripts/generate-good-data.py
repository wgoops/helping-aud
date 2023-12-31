import csv
import random
from datetime import datetime, timedelta

import csv
import random
from datetime import datetime, timedelta

# Number of rows
N = 10000

# Define office locations and associated doctor and patient prefixes
locations_prefixes = {
    "New York": ("NYD", "NYP"),
    "Los Angeles": ("LAD", "LAP"),
    "Chicago": ("CHD", "CHP"),
    "Houston": ("HUD", "HUP"),
    "San Francisco": ("SFD", "SFP"),
    "Miami": ("MID", "MIP"),
    "Boston": ("BOD", "BOP"),
    "Atlanta": ("ATD", "ATP"),
    "Dallas": ("DAD", "DAP"),
    "Denver": ("DED", "DEP"),
    "Seattle": ("SED", "SEP"),
    "Phoenix": ("PHD", "PHP"),
    "Detroit": ("DTD", "DTP"),
    "Philadelphia": ("PLD", "PLP"),
    "San Diego": ("SDD", "SDP")
}

doctors = [f"{doc_prefix}D{i:03}" for location, (doc_prefix, _) in locations_prefixes.items() for i in range(1, 4)]
unique_patients_count = int(N * 0.8)
patients = [f"{pat_prefix}P{i:03}" for location, (_, pat_prefix) in locations_prefixes.items() for i in range(1, int(N * 0.8 / len(locations_prefixes)) + 1)]

dob_start = datetime(1950, 1, 1)
diagnoses = ["Diabetes", "Hypertension", "Asthma", "Flu", "Cold", "Migraine", "Arthritis", "Bronchitis", "Tuberculosis", "Epilepsy", "Chickenpox", "Dengue"]
colors = ["Blue", "Red", "Green", "Yellow", "Purple", "Orange", "Violet", "Indigo", "Teal", "Pink", "Crimson", "Coral", "Aqua", "Mauve", "Olive", "Brown"]
insurance_companies = ["HealthCare Inc.", "Medical Shield", "Safe Health", "MedSecure", "LifeCare", "ProtectPlus", "WellnessGuard", "HealSure"]
medications = ["Metformin", "Lisinopril", "Ventolin", "Ibuprofen", "Aspirin", "Paracetamol", "Prednisone", "Amoxicillin", "Ciprofloxacin", "Levofloxacin", "Insulin", "Morphine", "Omeprazole", "Losartan", "Diazepam", "Hydrochlorothiazide", "Gabapentin", "Tramadol", "Cetirizine", "Azithromycin", "Warfarin", "Clopidogrel"]

yes_variants = ["Yes", "Yess", "Yea", "Yep"]


specialties = ["Cardiology", "Orthopedics", "Dermatology", "Neurology", "Pediatrics", "Radiology", "Psychiatry", "Ophthalmology", "Gynecology", "Endocrinology", "Gastroenterology", "Urology"]
# CSV writer

# CSV writer for clinic_details.csv
with open('clinic_details.csv', 'w', newline='') as csvfile:
    fieldnames = ["Office Location", "Clinic Address", "Number of Doctors",
                  "Specialties Offered", "Clinic Phone Number", "Clinic Rating",
                  "Operating Hours", "Doctors IDs"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for location in locations_prefixes:
        assigned_doctors = [doc for doc in doctors if doc.startswith(locations_prefixes[location][0])]

        writer.writerow({
            "Office Location": location,
            "Clinic Address": "Sample Address",
            "Number of Doctors": len(assigned_doctors),
            "Specialties Offered": ", ".join(random.sample(specialties, 3)),
            "Clinic Phone Number": f"(555) {random.randint(100, 999)}-{random.randint(1000, 9999)}",
            "Clinic Rating": round(random.uniform(3, 5), 1),
            "Operating Hours": "9:00 AM - 5:00 PM",
            "Doctors IDs": ", ".join(assigned_doctors)
        })

print("Clinic details generated!")

with open('fake_autogenerated_data.csv', 'w', newline='') as csvfile:
    fieldnames = ["Doctor ID", "Patient ID", "Patient DOB", "Visit Date", "Patient diagnosis", "Patient's Favorite Color",
                  "Insurance company", "Office Location", "Prescription issued?", "Medication"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(N):
        dob = dob_start + timedelta(days=random.randint(0, (datetime.today()-dob_start).days))
        visit_date = datetime(2020, 1, 1) + timedelta(days=random.randint(0, 365*2))
        diagnosis = random.choice(diagnoses)
        
        prescription_issued = "Yes"
        if diagnosis in ["Cold", "Flu"]:
            prescription_issued = random.choice(yes_variants) if random.random() < 0.98 else "No"
        else:
            if random.random() < 0.02:  # 2% chance to pick a yes variant
                prescription_issued = random.choice(yes_variants[1:])
                
        medication = random.choice(medications) if prescription_issued in yes_variants else "-"
        
        location = random.choice(list(locations_prefixes.keys()))
        doctor_prefix, patient_prefix = locations_prefixes[location]
        
        doctor_id = random.choice([doc for doc in doctors if doc.startswith(doctor_prefix)])
        if i < len(patients):
            patient_id = patients[i]
        else:
            patient_id = random.choice([pat for pat in patients if pat.startswith(patient_prefix)])

        writer.writerow({
            "Doctor ID": doctor_id,
            "Patient ID": patient_id,
            "Patient DOB": dob.strftime('%m/%d/%Y'),
            "Visit Date": visit_date.strftime('%m/%d/%Y'),
            "Patient diagnosis": diagnosis,
            "Patient's Favorite Color": random.choice(colors),
            "Insurance company": random.choice(insurance_companies),
            "Office Location": location,
            "Prescription issued?": prescription_issued,
            "Medication": medication
        })

print("Fake data generated!")