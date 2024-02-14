class BMI_health:
    def __init__(self):
        print("โปรแกรมคำนวณ BMI และตรวจสุขภาพ")
        self.height = float(input("ความสูงของคุณ? (เซนติเมตร): "))  # รับค่าความสูงจากผู้ใช้
        self.weight = float(input("น้ำหนักของคุณ? (กิโลกรัม): "))  # รับค่าน้ำหนักจากผู้ใช้
        self.gender = int(input("เพศของคุณ? (1 สำหรับชาย, 2 สำหรับหญิง (อย่าป้อนอย่างอื่นนอกจากนี้!)): "))  # รับค่าเพศจากผู้ใช้

    def calculate_bmi(self):
        if self.gender == 1:  # ถ้าผู้ใช้เป็นเพศชาย
            self.bmi = self.height - 110  # คำนวณค่า BMI สำหรับเพศชาย
        else:
            self.bmi = self.height - 100  # คำนวณค่า BMI สำหรับเพศหญิง

    def text_gender(self):
        if self.gender == 1:
            self.gender = "ชาย"  # เปลี่ยนค่าเพศให้เป็นข้อความ "ชาย"
        else:
            self.gender = "หญิง"  # เปลี่ยนค่าเพศให้เป็นข้อความ "หญิง"

    def health_level(self):
        if self.weight > self.bmi:
            self.Lv_health = "อ้วน"  # กำหนดระดับสุขภาพเป็น "อ้วน" ถ้าน้ำหนักมากกว่า BMI
        else:
            self.Lv_health = "สุขภาพดี"  # กำหนดระดับสุขภาพเป็น "สุขภาพดี" ถ้าน้ำหนักน้อยกว่าหรือเท่ากับ BMI

    def display_info(self):
        print("--------------------------------------------------")
        print(f"ความสูงของคุณ: {int(self.height)} เซนติเมตร และ น้ำหนักของคุณ: {int(self.weight)} กิโลกรัม")
        print(f"เพศของคุณ: {self.gender}")
        print(f"BMI ของคุณ: {self.bmi:.1f}")
        print(f"ระดับสุขภาพของคุณคือ: {self.Lv_health}")
        print("--------------------------------------------------")


bmi = BMI_health()  # สร้างอ็อบเจ็กต์ชนิด BMI_health
bmi.calculate_bmi()  # เรียกใช้เมทอด calculate_bmi
bmi.text_gender()  # เรียกใช้เมทอด text_gender เพื่อแปลงค่าเพศให้เป็นข้อความ
bmi.health_level()  # เรียกใช้เมทอด health_level เพื่อตรวจสุขภาพ
bmi.display_info()  # แสดงข้อมูลผลลัพธ์
