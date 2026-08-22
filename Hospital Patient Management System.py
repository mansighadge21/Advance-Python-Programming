class Patient:
    def __init__(self, patient_id, name, treatment_cost):
        self.patient_id = patient_id
        self.name = name
        self.treatment_cost = treatment_cost

    def get_category(self):
        if self.treatment_cost >= 50000:
            return "Special"
        else:
            return "General"

    def display(self):
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Treatment Cost: ₹", self.treatment_cost)
        print("Category:", self.get_category())
        print()


class Hospital:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def display_patients(self):
        print("Patient Records")
        print("---------------")
        for patient in self.patients:
            patient.display()


hospital = Hospital()

hospital.add_patient(Patient(201, "Aarav", 35000))
hospital.add_patient(Patient(202, "Sneha", 72000))
hospital.add_patient(Patient(203, "Kabir", 28000))
hospital.add_patient(Patient(204, "Ananya", 65000))

hospital.display_patients()