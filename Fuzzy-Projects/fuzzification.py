
from collections import defaultdict
from unittest import case


class Fuzzification():

    def __init__(self , input_dict):

        self.input_dict = input_dict
        self.membership_dict = defaultdict(lambda: defaultdict(float))

        
        
        
    def slope_intercept(self,x1,y1,x2,y2):
        a = (y2 - y1) / (x2 - x1)
        b = y1 - a * x1     
        return a,b
    
    def fuzzificate(self):

        self.age_fuzzificate()
        self.blood_pressure_fuzzificate()
        self.blood_sugar_fuzzificate()
        self.chest_pain_fuzzificate()
        self.cholestrol_fuzzificate()
        self.ecg_fuzzificate()
        self.exercise_fuzzificate()
        self.heart_rate_fuzzificate()
        self.old_peak_fuzzificate()
        self.sex_fuzzificate()
        self.thallium_scan_fuzzificate()
        
        return self.membership_dict


    def find_membership(self,crisp_number,points_list):

        xp,yp = 0,points_list[0][1]
        fuzzy_number = -1


        for i in points_list:
            xn,yn = i

            if crisp_number > xp and crisp_number <= xn:
                a , b = self.slope_intercept(xp,yp,xn,yn)
                fuzzy_number = a*crisp_number + b
            
            xp = xn
            yp = yn
        
        if fuzzy_number == -1 :
            fuzzy_number = yn

        return fuzzy_number




    def age_fuzzificate(self):

        crisp_input = int(self.input_dict["age"])
        points_list = []

        # for young
        points_list = [(29,1),(38,0)]
        self.membership_dict["age"]["young"] = float("{0:.3f}".format(self.find_membership(crisp_input,points_list)))

        # for mild
        points_list = [(33,0),(38,1),(45,0)]
        self.membership_dict["age"]["mild"] = float("{0:.3f}".format(self.find_membership(crisp_input,points_list)))

        # for old
        points_list = [(40,0),(48,1),(58,0)]
        self.membership_dict["age"]["old"] = float("{0:.3f}".format(self.find_membership(crisp_input,points_list)))


        # for veryold
        points_list = [(52,0),(60,1)]
        self.membership_dict["age"]["very_old"] = float("{0:.3f}".format(self.find_membership(crisp_input,points_list)))



    def blood_pressure_fuzzificate(self):

        crisp_input = int(self.input_dict["blood_pressure"])
        points_list = []

        # for low
        points_list = [(111,1),(134,0)]
        self.membership_dict["blood_pressure"]["low"] = float("{0:.3f}".format(self.find_membership(crisp_input,points_list)))

        # for medium
        points_list = [(127,0),(139,1),(153,0)]
        self.membership_dict["blood_pressure"]["medium"] = float("{0:.3f}".format(self.find_membership(crisp_input,points_list)))

        # for high
        points_list = [(142,0),(157,1),(172,0)]
        self.membership_dict["blood_pressure"]["high"] = float("{0:.3f}".format(self.find_membership(crisp_input,points_list)))

        # for veryhigh
        points_list = [(154,0),(171,1)]
        self.membership_dict["blood_pressure"]["very_high"] = float("{0:.3f}".format(self.find_membership(crisp_input,points_list)))


    def cholestrol_fuzzificate(self):

        crisp_input = int(self.input_dict["cholestrol"])
        points_list = []

        # for low
        points_list = [(151,1),(197,0)]
        self.membership_dict["cholestrol"]["low"] = float("{0:.3f}".format(self.find_membership(crisp_input,points_list)))

        # for medium
        points_list = [(188,0),(215,1),(250,0)]
        self.membership_dict["cholestrol"]["medium"] = float("{0:.3f}".format(self.find_membership(crisp_input,points_list)))

        # for high
        points_list = [(217,0),(263,1),(307,0)]
        self.membership_dict["cholestrol"]["high"] = float("{0:.3f}".format(self.find_membership(crisp_input,points_list)))

        # for veryhigh
        points_list = [(281,0),(374,1)]
        self.membership_dict["cholestrol"]["very_high"] = float("{0:.3f}".format(self.find_membership(crisp_input,points_list)))


    def heart_rate_fuzzificate(self):

        crisp_input = int(self.input_dict["heart_rate"])
        points_list = []

        # for low
        points_list = [(100,1),(141,0)]
        self.membership_dict["heart_rate"]["low"] = float("{0:.3f}".format(self.find_membership(crisp_input,points_list)))

        # for medium
        points_list = [(111,0),(152,1),(194,0)]
        self.membership_dict["heart_rate"]["medium"] = float("{0:.3f}".format(self.find_membership(crisp_input,points_list)))

        # for high
        points_list = [(152,0),(210,1)]
        self.membership_dict["heart_rate"]["high"] = float("{0:.3f}".format(self.find_membership(crisp_input,points_list)))


    def ecg_fuzzificate(self):

        crisp_input = float(self.input_dict["ecg"])
        points_list = []

        # for normal
        points_list = [(0,1),(0.4,0)]
        self.membership_dict["ecg"]["normal"] = float("{0:.3f}".format(self.find_membership(crisp_input,points_list)))

        # for abnormal
        points_list = [(0.2,0),(1,1),(1.8,0)]
        self.membership_dict["ecg"]["abnormal"] = float("{0:.3f}".format(self.find_membership(crisp_input,points_list)))

        # for hypertrophy
        points_list = [(1.4,0),(1.9,1)]
        self.membership_dict["ecg"]["hypertrophy"] = float("{0:.3f}".format(self.find_membership(crisp_input,points_list)))
       
        
    def old_peak_fuzzificate(self):

        crisp_input = float(self.input_dict["old_peak"])
        points_list = []

        # for low
        points_list = [(1,1),(2,0)]
        self.membership_dict["old_peak"]["low"] = float("{0:.3f}".format(self.find_membership(crisp_input,points_list)))

        # for risk
        points_list = [(1.5,0),(2.8,1),(4.2,0)]
        self.membership_dict["old_peak"]["risk"] = float("{0:.3f}".format(self.find_membership(crisp_input,points_list)))

        # for terrible
        points_list = [(2.5,0),(4,1)]
        self.membership_dict["old_peak"]["terrible"] = float("{0:.3f}".format(self.find_membership(crisp_input,points_list)))


    def chest_pain_fuzzificate(self):

        crisp_input = int(self.input_dict["chest_pain"])
        
        if crisp_input == 1:
            self.membership_dict["chest_pain"]["typical_angina"] = 1.000
        elif crisp_input == 2:
            self.membership_dict["chest_pain"]["atypical_angina"] = 1.000
        elif crisp_input == 3:
            self.membership_dict["chest_pain"]["non_anginal_pain"] = 1.000
        elif crisp_input == 4:
            self.membership_dict["chest_pain"]["asymptomatic"] = 1.000
        

    def exercise_fuzzificate(self):

        crisp_input = int(self.input_dict["exercise"])
        # 0 for false and 1 for true
        self.membership_dict["exercise"]= float(crisp_input)
        
        
    def thallium_scan_fuzzificate(self):

        crisp_input = int(self.input_dict["thallium_scan"])
        
        if crisp_input == 3:
            self.membership_dict["thallium_scan"]["normal"] = 1.000
        elif crisp_input == 6:
            self.membership_dict["thallium_scan"]["medium"] = 1.000
        elif crisp_input == 7:
            self.membership_dict["thallium_scan"]["high"] = 1.000
        else:
            print("error for amount of thallium_scan")
            exit(1)


    def blood_sugar_fuzzificate(self):

        crisp_input = int(self.input_dict["blood_sugar"])
        
        # 0 for false and 1 for true
        if crisp_input >= 120:
            self.membership_dict["blood_sugar"] = 1.000
        else:
            self.membership_dict["blood_sugar"] = 0.000


    def sex_fuzzificate(self):

        crisp_input = int(self.input_dict["sex"])
        # 0 for male and 1 for female
        self.membership_dict["sex"]= float(crisp_input)

