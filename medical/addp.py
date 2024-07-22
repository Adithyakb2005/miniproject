
def add_patient(patients):
    name=input("enter patient name: ")
    age=int(input("enter patient age: "))
    gender=input('enter patient gender: ')
    address=input('enter patient address: ')
    patients.append('name:',name,'age:',age,'gender:',gender,'address:',address) 






# def add_patient(patients):
#     name = input("Enter patient's name: ")
#     age = input("Enter patient's age: ")
#     patients.append({"name": name, "age": age})
#     print("Patient added successfully.")


# def add_appointment(appointments):
#     patient_name = input("Enter patient's name for appointment: ")
#     date = input("Enter appointment date (MM/DD/YYYY): ")
#     time = input("Enter appointment time: ")
#     appointments.append({"patient_name": patient_name, "date": date, "time": time})
#     print("Appointment added successfully.")


# def add_medical_history(medical_histories):
#     patient_name = input("Enter patient's name for medical history: ")
#     history = input("Enter medical history details: ")
#     medical_histories.append({"patient_name": patient_name, "history": history})
#     print("Medical history added successfully.")


# def view_patients(patients):
#     print("Patients:")
#     for patient in patients:
#         print(f"Name:{patient['name']},Age: {patient['age']}")


# def view_appointments(appointments):
#     print("Appointments:")
#     for appointment in appointments:
#         print(f"Patient: {appointment['patient_name']}, Date: {appointment['date']}, Time: {appointment['time']}")


# def view_medical_history(medical_histories):
#     print("Medical Histories:")
#     for history in medical_histories:
#         print(f"Patient: {history['patient_name']}, History: {history['history']}")


# List to store patient data (simulating a database)


# Function to add a new patient
# def add_patient(name, age, gender, diagnosis):
#     patients.append({
#         'name': name,
#         'age': age,
#         'gender': gender,
#         'diagnosis': diagnosis
#     })
#     print(f"\nPatient {name} added successfully!\n")


def view_patients(patients):
    print("\nList of Patients:")
    if patients:
        for patient in patients:
            print(f"Name: {patient['name']}, Age: {patient['age']}, Gender: {patient['gender']}, Diagnosis: {patient['diagnosis']}")
    else:
        print("No patients found.\n")

def search_patient(patients):
    print(f"\nSearch Patient by Name: {search_name}")
    found = False
    search_name = input("Enter patient's name to search: ")
    for patient in patients:
        if patient['name'].lower() == search_name.lower():
            print(f"Name: {patient['name']}, Age: {patient['age']}, Gender: {patient['gender']}, Diagnosis: {patient['diagnosis']}")
            found = True
    
    if not found:
        print(f"Patient with name '{search_name}' not found.\n")
