class MedicationManagementSystem:
    def __init__(self):
        self.symptom_to_medication_mapping = {
            "ปวดหัว": ["พาราเซตามอล", "อะสไปริน"],
            "ไข้": ["พาราเซตามอล", "อะสไปริน", "อินฟลูเอนซา"],
            "ไอ": ["ดิเทนไฮดรอมีน", "โคเดนไฮดรามีน"],
            "ตัวร้อน": ["พาราเซตามอล", "อินฟลูเอนซา"],
            # เพิ่มอาการและยาตรงกันต่อไป
        }

        self.disease_to_medication_mapping = {
            "หวัด": ["อินฟลูเอนซา", "พาราเซตามอล"],
            "เจ็บคอ": ["กลูโคส", "ลูกพีช"],
            "โรคหลอดเลือดสมอง": ["อัสไพริน", "คลอพิเดกรล"],
            "โรคเบาหวาน": ["เมโทรไนดีเอ็น", "ไอบูโพรเฟน"],
            # เพิ่มโรคและยาตรงกันต่อไป
        }

    def find_medication(self, symptom_or_disease):
        if symptom_or_disease in self.symptom_to_medication_mapping:
            return self.symptom_to_medication_mapping[symptom_or_disease]
        elif symptom_or_disease in self.disease_to_medication_mapping:
            return self.disease_to_medication_mapping[symptom_or_disease]
        else:
            return ["ไม่พบยาที่เกี่ยวข้องกับอาการหรือโรคนี้"]

# ตัวอย่างการใช้งาน
medication_system = MedicationManagementSystem()

# รับ input จากผู้ใช้เพื่อระบุโรคหรืออาการ
symptom_or_disease_input = input("กรุณาป้อนโรคหรืออาการที่เป็น (แยกด้วยช่องว่าง): ")

# แยก input เป็นรายการอาการหรือโรค
symptoms_or_diseases = symptom_or_disease_input.split()

# ค้นหายาที่เหมาะสม
medications = []
for item in symptoms_or_diseases:
    medications.extend(medication_system.find_medication(item))

# แสดงผลลัพธ์
print(f"อาการหรือโรคที่เป็น: {', '.join(symptoms_or_diseases)}")
print(f"ยาที่เหมาะสม: {', '.join(medications)}")