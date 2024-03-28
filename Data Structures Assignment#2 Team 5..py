class Patient:
    """Class to represent a patient"""

    # Constructor to initialize attributes:
    def __init__(self, id, name, medical_record, current_diagnosis):  # added _ for the protected attributes.
        self._id = id
        self._name = name
        self._medical_record = medical_record
        self._current_diagnosis = current_diagnosis
        self.appointment = None
        self.perscription = []


class Doctor:
    """Class to represent a doctor"""

    # Constructor to initialize attributes:
    def __init__(self, docname, docID, specialization):
        self.docname = docname
        self.docID = docID
        self.specialization = specialization
        self.schedule = []


class Perscription:
    def __init__(self, type, dosage):
        self._type = type
        self._dosage = dosage


class Queue:
    """Class to represent a queue of patients"""

    # Constructor:
    def __init__(self):
        self.queue = []  # Creating an empty queue.

    def enqueue(self, patient):  # function to add patients into the queue.
        self.queue.append(patient)

    def is_empty(self):  # function to check if queue is empty.
        return len(self.queue) == 0  # if the length (meaning number of elements) of the queue is 0 then it is empty.

    def dequeue(self):  # function to remove patients from the queue.
        if self.is_empty():  # checks if queue is empty
            return None
        return self.queue.pop(0)  # if queue is not empty it removes the first item (patient).

    def print_queue(self):  # function to print the queue.
        print("\nQueue of Patients:")
        for patient in self.queue:  # for all the patients added it prints their name and ID.
            print("ID:", patient._id, "Name:", patient._name)


class Stack:
    """Class to represent a stack of perscriptions"""

    # Constructor:
    def __init__(self):
        self.stack = []  # Creatng an empty stack.

    def push(self, perscription):  # function to add perscription to the stack.
        self.stack.append(perscription)

    def is_empty(self):  # function to check if the stack is empty.
        if len(self.stack) == 0:  # if the length (meaning number of elemnets) of the stack is 0 then it is empty.
            return 0

    def pop(self):  # function to remove perscription from the stack.
        if self.is_empty():  # first it checks if the stack is empty.
            return None
        return self.stack.pop()  # if its not empty then it removes the perscription.

    def print_stack(self):  # function to print the stack
        print("\nStack of Prescriptions:")
        for prescription in self.stack:  # for all the perscriptions added it prints their type and dosage.
            print("Type:", prescription._type, "Dosage:", prescription._dosage)


class Hospital:
    """Class to represent the hospital"""

    # Constructor:
    def __init__(self):
        self.patients = {}  # empty dictionary for patients.
        self.doctors = {}  # empty dictionary for doctors.
        self.patient_queue = Queue()  # calling the queue class.
        self.perscription_stack = Stack()  # calling the stack class.

    def new_patient(self, patient):  # function to add a new patient.
        self.patients[patient._id] = patient

    def update_record(self, patient_id, updated_details):
        if patient_id in self.patients:
            patient = self.patients[patient_id]
            patient._name = updated_details.get('name', patient._name)
            patient._medical_record = updated_details.get('medical_record', patient._medical_record)
            patient._current_diagnosis = updated_details.get('current_diagnosis', patient._current_diagnosis)
            patient.appointment = updated_details.get('appointment', patient.appointment)
            print("Record updated successfully.")
        else:
            print("This patient has no record available/found.")

    def delete_patient(self, patient_id):  # function to delete a patient.
        if patient_id in self.patients:  # if the patients ID is found delete the patient.
            del self.patients[patient_id]
        else:
            print("There is no patient found with this ID.")

    def schedule_appointment(self, patient_id, docID, appointment):  # function to schedule an appointment.
        if patient_id in self.patients and docID in self.doctors:
            patient = self.patients[patient_id]
            doctor = self.doctors[docID]
            patient.appointment = appointment
            doctor.schedule.append(patient)
        else:
            print("The patient or Doctor was not found.")

    def assign_perscription(self, patient_id, perscription):  # function to assign
        if patient_id in self.patients:
            patient = self.patients[patient_id]
            patient.perscription.append(perscription)
            self.perscription_stack.push(perscription)
        else:
            print("The given patient ID was not found.")

    def find_patient(self, patient_id):  # function to find a patient.
        if patient_id in self.patients:
            patient = self.patients[patient_id]
            return patient
        else:
            print("This patient was not found.")


def print_patient_details(patient):  # function to print patient details.
    print("ID:", patient._id)
    print("Name:", patient._name)
    print("Medical Records:", patient._medical_record)
    print("Current Diagnosis:", patient._current_diagnosis)
    print("Appointment :", patient.appointment)
    print("Perscriptions:")
    for prescription in patient.perscription:
        print("\tType:", prescription._type)
        print("\tDosage:", prescription._dosage)
        print()


# Test Cases for patient class, doctor class, and perscription class:
patient1 = Patient(1234, "Mahra Alameri", "None", "Fever")
patient2 = Patient(4321, "Aliya Alshabibi", "Diabetes Type 1", "High blood pressure")
patient3 = Patient(5678, "Khaled Alharmoodi", "Asthma", "Cough")
doctor1 = Doctor("Dr. Mohammed", 555, "General Doctor")
doctor2 = Doctor("Dr. John", 999, "Cardiologist")
doctor3 = Doctor("Dr. Fatima", 777, "Ear Nose and Throat Specialist")
prescription1 = Perscription("Ibuprofen", "1500mg")
prescription2 = Perscription("ACE inhibitors", "200mg")
prescription3 = Perscription("Lozenge", "15mg")

# Test cases for hospital class:
# Adding patients to the hospital:
hospital = Hospital()
hospital.new_patient(patient1)
hospital.new_patient(patient2)
hospital.new_patient(patient3)

# Adding doctors to the hospital:
hospital.doctors[doctor1.docID] = doctor1
hospital.doctors[doctor2.docID] = doctor2
hospital.doctors[doctor3.docID] = doctor3

# Test cases for scheduling appointments:
hospital.schedule_appointment(1234, 555, "Monday, April 1st 2024. 12:00pm.")
hospital.assign_perscription(1234, prescription1)

hospital.schedule_appointment(4321, 999, "Monday, April 1st 2024. 12:00pm.")
hospital.assign_perscription(4321, prescription2)

hospital.schedule_appointment(5678, 777, "Monday, April 1st 2024. 12:00pm.")
hospital.assign_perscription(5678, prescription3)

#Test case for updating patient record:
update_details = {'id': '1234', 'name': 'Mahra Al Ameri', 'medical_record': 'Allergies', 'current_diagnosis': 'Fever', 'appointment': 'Tuesday, April 2nd 2024. 10:00am.'}
hospital.update_record(1234, update_details)

#After updating let's print the updated record:
updated_patient = hospital.find_patient(1234)
if updated_patient:
    print("\nUpdated Patient Details:")
    print_patient_details(updated_patient)


# Test cases for the queue and stack:
queue = Queue()  # calling the Queue class and adding the patients to it.
queue.enqueue(patient1)
queue.enqueue(patient2)
queue.enqueue(patient3)
queue.print_queue()  # printing the queue before the dequeue.

dequeued_patient = queue.dequeue()  # the patient that was dequeued.
print("\nDequeued Patient:")
if dequeued_patient:
    print("ID:", dequeued_patient._id, "Name:", dequeued_patient._name)

print("\nAfter dequeue:")
queue.print_queue()  # printing the queue after the dequeue.

stack = Stack()  # calling the Stack class and adding the perscriptions to it.
stack.push(prescription1)
stack.push(prescription2)
stack.push(prescription3)
stack.print_stack()

popped_prescription = stack.pop()  # Pop a prescription off the stack.
print("\nPopped Prescription:")
if popped_prescription:
    print("Type:", popped_prescription._type, "Dosage:", popped_prescription._dosage)

print("\nAfter pop:")
stack.print_stack()  # Print the stack after pop

while True: #while loop to print patient details given the ID.
    patient_id = input("\nEnter patient ID: ") #takes in an input ID from the user
    print("Patient Details:")
    patient = hospital.find_patient(int(patient_id)) #if patient is found in the hospital
    if patient:
        print_patient_details(patient) #It prints the patient's details.
    break #to break out of the loop.
