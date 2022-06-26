
from collections import defaultdict


class Fuzzification():

    def __init__(self , input_dict):

        self.input_dict = input_dict
        self.membership_dict = defaultdict(dict)

        
        
        
    def slope_intercept(self,x1,y1,x2,y2):
        a = (y2 - y1) / (x2 - x1)
        b = y1 - a * x1     
        return a,b
    
    def fuzzificate(self):

        self.age_fuzzificate()
        print(self.membership_dict["age"])


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
        self.membership_dict["age"]["veryold"] = float("{0:.3f}".format(self.find_membership(crisp_input,points_list)))



    # def blood_pressure_fuzzificate(self):

    #     crisp_input = int(self.input_dict["blood_pressure"])
    #     points_list = []

    #     # for young
    #     points_list = [(29,1),(38,0)]
    #     self.membership_dict["blood_pressure"]["young"] = float("{0:.3f}".format(self.find_membership(crisp_input,points_list)))

    #     # for mild
    #     points_list = [(33,0),(38,1),(45,0)]
    #     self.membership_dict["blood_pressure"]["mild"] = float("{0:.3f}".format(self.find_membership(crisp_input,points_list)))

    #     # for old
    #     points_list = [(40,0),(48,1),(58,0)]
    #     self.membership_dict["blood_pressure"]["old"] = float("{0:.3f}".format(self.find_membership(crisp_input,points_list)))


    #     # for veryold
    #     points_list = [(52,0),(60,1)]
    #     self.membership_dict["blood_pressure"]["veryold"] = float("{0:.3f}".format(self.find_membership(crisp_input,points_list)))



       
        






