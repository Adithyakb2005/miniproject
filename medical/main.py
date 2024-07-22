# from addp import *
# patients=[]
# appointments = []
# medical_histories = []

# def main():
#     while True:
#         print(" 1.add patient ")
#         print(" 2.add appointment ")
#         print(" 3.add medical history ")
#         print(" 4.view patients ")
#         print(" 5.view appointment ")
#         print(" 6.view medical historty ")
#         print("7.exit")
#         ch=input("enter your choice:")
#         if ch=='1':
#             add_patient(patients)
#         elif ch == '2':
#             add_appointment(appointments)
#         elif ch == '3':
#             add_medical_history(medical_histories)
#         elif ch == '4':
#             view_patients(patients)
#         elif ch == '5':
#             view_appointments(appointments)
#         elif ch == '6':
#             view_medical_history(medical_histories)
#         elif ch == '7':
#             print("Exiting program.")
#             break
#         else:
#             print("Invalid choice. Please enter a number from 1 to 7.")

# if __name__ == "__main__":
#     main()

from addp import *

patients=[]
def main():
    while True:
        print("\nPatient Management System Menu:")
        print("1. Add New Patient")
        print("2. View All Patients")
        print("3. Search for a Patient by Name")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_patient(patients)
        elif choice == '2':
            view_patients(patients)
        elif choice == '3':
            search_patient(patients)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

main()