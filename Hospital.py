import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

class HospitalManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")

        # Patient Data Variables
        self.patient_name = tk.StringVar()
        self.patient_age = tk.StringVar()
        self.patient_gender = tk.StringVar()
        self.patient_contact = tk.StringVar()
        self.patient_disease = tk.StringVar()

        # List to store patients
        self.patients = []
        self.load_patients_from_disk()

        # Create GUI
        self.create_widgets()

    def create_widgets(self):
        # Heading
        ttk.Label(self.root, text="Hospital Management System", font=("Arial", 24)).grid(row=0, column=0, columnspan=2, pady=20)

        # Patient Information Entry
        ttk.Label(self.root, text="Name:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        ttk.Entry(self.root, textvariable=self.patient_name).grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Age:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        ttk.Entry(self.root, textvariable=self.patient_age).grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Gender:").grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
        ttk.Combobox(self.root, textvariable=self.patient_gender, values=["Male", "Female", "Other"]).grid(row=3, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Contact:").grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)
        ttk.Entry(self.root, textvariable=self.patient_contact).grid(row=4, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Disease:").grid(row=5, column=0, sticky=tk.W, padx=10, pady=5)
        ttk.Entry(self.root, textvariable=self.patient_disease).grid(row=5, column=1, padx=10, pady=5)

        # Buttons
        ttk.Button(self.root, text="Register", command=self.register_patient).grid(row=6, column=0, columnspan=2, pady=20)
        ttk.Button(self.root, text="Show Patients", command=self.show_patients).grid(row=7, column=0, columnspan=2, pady=20)

    def register_patient(self):
        patient = {
            "Name": self.patient_name.get(),
            "Age": self.patient_age.get(),
            "Gender": self.patient_gender.get(),
            "Contact": self.patient_contact.get(),
            "Disease": self.patient_disease.get()
        }
        self.patients.append(patient)
        self.save_patients_to_disk()
        messagebox.showinfo("Success", "Patient registered successfully!")
        self.clear_entries()

    def clear_entries(self):
        self.patient_name.set("")
        self.patient_age.set("")
        self.patient_gender.set("")
        self.patient_contact.set("")
        self.patient_disease.set("")

    def show_patients(self):
        window = tk.Toplevel(self.root)
        window.title("Patients")

        ttk.Label(window, text="Registered Patients", font=("Arial", 20)).grid(row=0, column=0, columnspan=2, pady=20)

        for index, patient in enumerate(self.patients, start=1):
            patient_data = f"{index}. {patient['Name']}, {patient['Age']} years, {patient['Gender']}, Contact: {patient['Contact']}, Disease: {patient['Disease']}"
            ttk.Label(window, text=patient_data).grid(row=index, column=0, columnspan=2, padx=10, pady=5)

        ttk.Button(window, text="Close", command=window.destroy).grid(row=index+1, column=0, columnspan=2, pady=20)

    def save_patients_to_disk(self):
        """Save the patients list to a JSON file."""
        with open('patients.json', 'w') as f:
           json.dump(self.patients, f)

    def load_patients_from_disk(self):
        """Load patients from a JSON file if it exists."""
        if os.path.exists('patients.json'):
            with open('patients.json', 'r') as f:
                self.patients = json.load(f)

if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalManagement(root)
    root.mainloop()
