


import numpy as np


class Defuzzification():

    def __init__(self , diagnosis_dict):

        self.diagnosis_dict = diagnosis_dict
        self.epsilon = 0.005

    def slope_intercept(self,x1,y1,x2,y2):
        a = (y2 - y1) / (x2 - x1)
        b = y1 - a * x1     
        return a,b

    def defuzzificate(self):

        sum_i = 0
        sum_ix = 0
        list1 = ["sick_1","sick_2","sick_3","sick_4"]
        list2 = ["healthy","sick_1","sick_2","sick_3"]
        points1 = [(0,0),(1,1),(2,0),(3,1),(4,0)]
        points2 = [(0.25,1),(1,0),(2,1),(3,0),(3.75,1)]
        
        for i in range(4):
            a1,b1 = self.slope_intercept(points1[i][0],points1[i][1],points1[i+1][0],points1[i+1][1])
            a2,b2 = self.slope_intercept(points2[i][0],points2[i][1],points2[i+1][0],points2[i+1][1])

            for j in np.arange(i,i+1,self.epsilon):
                m1 = min(self.diagnosis_dict[list1[i]] , a1*j+b1)
                m2 = min(self.diagnosis_dict[list2[i]] , a2*j+b2)
                m = max(m1,m2)

                sum_i += m
                sum_ix += m*j

        result = sum_ix/sum_i
        
        return self.get_results(result)

    def get_results(self, result):

        answerlist = []
        answer = ""

        if result < 1.78 :
            answerlist.append("healthy ")
        elif result >= 1 and result <= 2.5:
            answerlist.append("sick1 ")
        elif result >= 1.78 and result <= 3.25:
            answerlist.append("sick2 ")
        elif result >= 1.5 and result <= 4.5:
            answerlist.append("sick3 ")
        if result > 3.25 :
            answerlist.append("sick4 ")

        for i in range(len(answerlist)):

            if i != 0:
                answer += "& "

            answer += answerlist[i]

        answer += ": {0:.3f}".format(result)

        return answer



    
if __name__ == "__main__":
    
    diagnosis_dict = {}
    diagnosis_dict["healthy"] = 0
    diagnosis_dict["sick_1"] = 0
    diagnosis_dict["sick_2"] = 0
    diagnosis_dict["sick_3"] = 0
    diagnosis_dict["sick_4"] = 1

    mydifuzzification = Defuzzification(diagnosis_dict)
    print(mydifuzzification.defuzzificate())