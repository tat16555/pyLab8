class BMI_health:
    def __init__(self):
        print("BMI Calculation and Health Check Program")
        self.height = float(input("Your Height? (cm): "))
        self.weight = float(input("Your Weight? (kg): "))
        self.gender = int(input("Your Gender? (1 for Male, 2 for Female (Do not enter anything other than this!)): "))
        self.calculate_bmi()

    def calculate_bmi(self):
        if self.gender == 1:
            self.bmi = self.height - 110
        else:
            self.bmi = self.height - 100
        self.health_level()

    def text_gender(self):
        if self.gender == 1:
            self.gender = "Male"
        else:
            self.gender = "Female"

    def health_level(self):
        if self.weight > self.bmi:
            self.Lv_health = "Fat"
        else:
            self.Lv_health = "Healthy"

    def display_info(self):
        print("--------------------------------------------------")
        print(f"Your Height: {int(self.height)} cm. and Weight: {int(self.weight)} kg.")
        print(f"Your Gender: {self.gender}")
        print(f"Your BMI: {self.bmi:.1f}")
        print(f"Your health level is: {self.Lv_health}")
        print("--------------------------------------------------")


bmi = BMI_health()
bmi.calculate_bmi()  
bmi.text_gender()
bmi.health_level()
bmi.display_info() 
