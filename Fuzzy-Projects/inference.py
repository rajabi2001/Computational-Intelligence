from collections import defaultdict


class Inference():

    def __init__(self , membership_dict):

        self.membership_dict = membership_dict
        self.diagnosis_dict = defaultdict(int)


    def infer(self):

        # rule 1
        temp = self.diagnosis_dict["sick_4"]
        output_rule = min(self.membership_dict["age"]["very_old"] , self.membership_dict["chest_pain"]["atypical_anginal"])
        self.diagnosis_dict["sick_4"] = max(temp, output_rule)

        pass