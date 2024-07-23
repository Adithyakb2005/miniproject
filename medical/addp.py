def add_patient(patients):
    name = input("Enter patient's name: ")
    age = input("Enter patient's age: ")
    gender = input("Enter patient's gender: ")
    diagnosis = input("Enter patient's diagnosis: ")
    
    patient = {'name': name, 'age': age, 'gender': gender, 'diagnosis': diagnosis}
    patients.append(patient)
    print("Patient added successfully.")


def view_patients(patients):
    print("\nList of Patients:")
    if patients:
        for patient in patients:
            print(f"Name: {patient['name']}, Age: {patient['age']}, Gender: {patient['gender']}, Diagnosis: {patient['diagnosis']}")
    else:
        print("No patients found.")
def search_patient(patients):
    name = input("Enter patient's name to search: ")
    found = False
    for patient in patients:
        if patient['name'].lower() == name.lower():
            print(f"Patient found - Name: {patient['name']}, Age: {patient['age']}, Gender: {patient['gender']}, Diagnosis: {patient['diagnosis']}")
            found = True
            break
    if not found:
        print(f"Patient with name '{name}' not found.")

