
from datetime import datetime, timedelta

class Clinic:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
        self.opening_hours = None
        self.closing_hours = None
        self.time_slot_duration = None

class Doctor:
    def __init__(self, name, specialty, phone):
        self.name = name
        self.specialty = specialty
        self.phone = phone

class Patient:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.appointments = []

class Appointment:
    def __init__(self, patient, doctor, date, slots):
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.slots = slots

class ClinicManagementSystem:
    def __init__(self):
        self.clinic = Clinic("Default Clinic", "Default Address", "0000000000")
        self.doctors = []
        self.patients = []

    def register_clinic(self, name, address, phone):
        self.clinic = Clinic(name, address, phone)

    def register_doctor(self, name, specialty, phone):
        self.doctors.append(Doctor(name, specialty, phone))

    def set_clinic_schedule(self, opening_hours, closing_hours, time_slot_duration):
        if self.clinic:
            self.clinic.opening_hours = opening_hours
            self.clinic.closing_hours = closing_hours
            self.clinic.time_slot_duration = time_slot_duration

    def add_patient(self, name, phone):
        self.patients.append(Patient(name, phone))

    def schedule_appointment(self, patient_name, doctor_name, date, slots):
        patient = next((p for p in self.patients if p.name == patient_name), None)
        doctor = next((d for d in self.doctors if d.name == doctor_name), None)

        if patient is None:
            print("Không tìm thấy bệnh nhân.")
            return

        if doctor is None:
            print("Không tìm thấy bác sĩ.")
            return

        if slots <= 3:
            print("Bệnh nhân chỉ có thể đặt tối đa 3 slot khám.")
            return

        appointment = Appointment(patient, doctor, date, slots)
        patient.appointments.append(appointment)
        print(f"Đã đặt lịch cho bệnh nhân {patient.name} với bác sĩ {doctor.name} vào {date} cho {slots} slot.")

    def display_info(self):
        if self.clinic:
            print(f"Phòng khám: {self.clinic.name}")
            print(f"Địa chỉ: {self.clinic.address}")
            print(f"Điện thoại: {self.clinic.phone}")
            print(f"Giờ mở cửa: {self.clinic.opening_hours} - Giờ đóng cửa: {self.clinic.closing_hours}")
            print("\nDanh sách bác sĩ:")

            if not self.doctors:
                print("Không có bác sĩ nào đăng ký.")
            else:
                for doctor in self.doctors:
                    print(f"- Tên: {doctor.name or 'Không có tên'}, Chuyên khoa: {doctor.specialty or 'Không có chuyên khoa'}, Điện thoại: {doctor.phone or 'Không có số điện thoại'}")

            print("\nDanh sách bệnh nhân:")
            if not self.patients:
                print("Không có bệnh nhân nào đăng ký.")
            else:
                for patient in self.patients:
                    print(f"- Tên: {patient.name or 'Không có tên'}, Điện thoại: {patient.phone or 'Không có số điện thoại'}")
                    for appointment in patient.appointments:
                        doctor_name = appointment.doctor.name if appointment.doctor else "Không có tên"
                        print(f"  - Lịch hẹn với {doctor_name} vào {appointment.date} cho {appointment.slots} slot.")
        else:
            print("Chưa đăng ký phòng khám.")

def main():
    cms = ClinicManagementSystem()
    
    cms.register_clinic("Phòng khám tai mũi họng", "123 Đường ABC", "12345678")
    cms.register_doctor("Nguyễn Du", "Chuyên khoa Nội", "12345678")
    cms.set_clinic_schedule(timedelta(hours=8), timedelta(hours=17), 45)
    cms.add_patient("Lap la", "12345678")
    cms.schedule_appointment("Lap la", "Nguyễn Du", datetime.now() + timedelta(days=1), 3)
    cms.display_info()

if __name__ == "__main__":
    main()
