from addp import *

patients = []

def main():
    while True:
        print("\nPatient Management System Menu:")
        print("1. Add New Patient")
        print("2. View All Patients")
        print("3. Search for a Patient by Name")
        print("4. Exit")
        
        ch= input("Enter your choice: ")
        
        if ch=='1':
            add_patient(patients)
        elif ch== '2':
            view_patients(patients)
        elif ch== '3':
            search_patient(patients)
        elif ch== '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice.")

main()
