from collections import defaultdict


class Inference():

    def __init__(self , membership_dict):

        self.membership_dict = membership_dict
        self.diagnosis_dict = defaultdict(float)


    def infer(self):

        # RULE 1: IF (age IS very_old) AND (chest_pain IS atypical_anginal) THEN health IS sick_4;
        temp = self.diagnosis_dict["sick_4"]
        output_rule = min(self.membership_dict["age"]["very_old"] , self.membership_dict["chest_pain"]["atypical_anginal"])
        self.diagnosis_dict["sick_4"] = max(temp, output_rule)

        # RULE 2: IF (maximum_heart_rate IS high) AND (age IS old) THEN health IS sick_4;
        temp = self.diagnosis_dict["sick_4"]
        output_rule = min(self.membership_dict["age"]["old"] , self.membership_dict["heart_rate"]["high"])
        self.diagnosis_dict["sick_4"] = max(temp, output_rule)

        # RULE 3: IF (sex IS male) AND (maximum_heart_rate IS medium) THEN health IS sick_3;
        temp = self.diagnosis_dict["sick_3"]
        output_rule = min(self.membership_dict["sex"]["male"] , self.membership_dict["heart_rate"]["medium"])
        self.diagnosis_dict["sick_3"] = max(temp, output_rule)

        # RULE 4: IF (sex IS female) AND (maximum_heart_rate IS medium) THEN health IS sick_2;
        temp = self.diagnosis_dict["sick_2"]
        output_rule = min(self.membership_dict["sex"]["female"]  , self.membership_dict["heart_rate"]["medium"])
        self.diagnosis_dict["sick_2"] = max(temp, output_rule)

        # RULE 5: IF (chest_pain IS non_aginal_pain) AND (blood_pressure IS high) THEN health IS sick_3;
        temp = self.diagnosis_dict["sick_3"]
        output_rule = min(self.membership_dict["blood_pressure"]["high"] , self.membership_dict["chest_pain"]["non_aginal_pain"])
        self.diagnosis_dict["sick_3"] = max(temp, output_rule)

        # RULE 6: IF (chest_pain IS typical_anginal) AND (maximum_heart_rate IS medium) THEN health IS sick_2;
        temp = self.diagnosis_dict["sick_2"]
        output_rule = min(self.membership_dict["heart_rate"]["medium"] , self.membership_dict["chest_pain"]["typical_anginal"])
        self.diagnosis_dict["sick_2"] = max(temp, output_rule)

        # RULE 7: IF (blood_sugar IS true) AND (age IS mild) THEN health IS sick_3;
        temp = self.diagnosis_dict["sick_3"]
        output_rule = min(self.membership_dict["blood_sugar"]["true"] , self.membership_dict["age"]["mild"])
        self.diagnosis_dict["sick_3"] = max(temp, output_rule)

        # RULE 8: IF (blood_sugar IS false) AND (blood_pressure IS very_high) THEN health IS sick_2;
        temp = self.diagnosis_dict["sick_2"]
        output_rule = min(self.membership_dict["blood_sugar"]["false"] , self.membership_dict["blood_pressure"]["very_high"])
        self.diagnosis_dict["sick_2"] = max(temp, output_rule)

        # RULE 9: IF (chest_pain IS asymptomatic) OR (age IS very_old) THEN health IS sick_1;
        temp = self.diagnosis_dict["sick_1"]
        output_rule = min(self.membership_dict["chest_pain"]["asymptomatic"] , self.membership_dict["age"]["very_old"])
        self.diagnosis_dict["sick_1"] = max(temp, output_rule)

        # RULE 10: IF (blood_pressure IS high) OR (maximum_heart_rate IS low) THEN health IS sick_1;
        temp = self.diagnosis_dict["sick_1"]
        output_rule = min(self.membership_dict["blood_pressure"]["high"] , self.membership_dict["heart_rate"]["low"])
        self.diagnosis_dict["sick_1"] = max(temp, output_rule)

        # RULE 11: IF (chest_pain IS typical_anginal) THEN health IS healthy;
        temp = self.diagnosis_dict["healthy"]
        output_rule = self.membership_dict["chest_pain"]["typical_anginal"]
        self.diagnosis_dict["healthy"] = max(temp, output_rule)

        # RULE 12: IF (chest_pain IS atypical_anginal) THEN health IS sick_1;
        temp = self.diagnosis_dict["sick_1"]
        output_rule = self.membership_dict["chest_pain"]["atypical_anginal"]
        self.diagnosis_dict["sick_1"] = max(temp, output_rule)

        # RULE 13: IF (chest_pain IS non_aginal_pain) THEN health IS sick_2;
        temp = self.diagnosis_dict["sick_2"]
        output_rule = self.membership_dict["chest_pain"]["non_aginal_pain"]
        self.diagnosis_dict["sick_2"] = max(temp, output_rule)

        # RULE 14: IF (chest_pain IS asymptomatic) THEN health IS sick_3;
        temp = self.diagnosis_dict["sick_3"]
        output_rule = self.membership_dict["chest_pain"]["asymptomatic"]
        self.diagnosis_dict["sick_3"] = max(temp, output_rule)

        # RULE 15: IF (chest_pain IS asymptomatic) THEN health IS sick_4;
        temp = self.diagnosis_dict["sick_4"]
        output_rule = self.membership_dict["chest_pain"]["asymptomatic"]
        self.diagnosis_dict["sick_4"] = max(temp, output_rule)

        # RULE 16: IF (sex IS female) THEN health IS sick_1;
        temp = self.diagnosis_dict["sick_1"]
        output_rule = self.membership_dict["sex"]["female"]
        self.diagnosis_dict["sick_1"] = max(temp, output_rule)

        # RULE 17: IF (sex IS male) THEN health IS sick_2;
        temp = self.diagnosis_dict["sick_2"]
        output_rule = self.membership_dict["sex"]["male"]
        self.diagnosis_dict["sick_2"] = max(temp, output_rule)

        # RULE 18: IF (blood_pressure IS low) THEN health IS healthy;
        temp = self.diagnosis_dict["healthy"]
        output_rule = self.membership_dict["blood_pressure"]["low"]
        self.diagnosis_dict["healthy"] = max(temp, output_rule)

        # RULE 19: IF (blood_pressure IS medium) THEN health IS sick_1;
        temp = self.diagnosis_dict["sick_1"]
        output_rule = self.membership_dict["blood_pressure"]["medium"]
        self.diagnosis_dict["sick_1"] = max(temp, output_rule)

        # RULE 20: IF (blood_pressure IS high) THEN health IS sick_2;
        temp = self.diagnosis_dict["sick_2"]
        output_rule = self.membership_dict["blood_pressure"]["high"]
        self.diagnosis_dict["sick_2"] = max(temp, output_rule)

        # RULE 21: IF (blood_pressure IS high) THEN health IS sick_3;
        temp = self.diagnosis_dict["sick_3"]
        output_rule = self.membership_dict["blood_pressure"]["high"]
        self.diagnosis_dict["sick_3"] = max(temp, output_rule)

        # RULE 22: IF (blood_pressure IS very_high) THEN health IS sick_4;
        temp = self.diagnosis_dict["sick_4"]
        output_rule = self.membership_dict["blood_pressure"]["very_high"]
        self.diagnosis_dict["sick_4"] = max(temp, output_rule)

        # RULE 23: IF (cholesterol IS low) THEN health IS healthy;
        temp = self.diagnosis_dict["healthy"]
        output_rule = self.membership_dict["cholesterol"]["low"]
        self.diagnosis_dict["healthy"] = max(temp, output_rule)

        # RULE 24: IF (cholesterol IS medium) THEN health IS sick_1;
        temp = self.diagnosis_dict["sick_1"]
        output_rule = self.membership_dict["cholesterol"]["medium"]
        self.diagnosis_dict["sick_1"] = max(temp, output_rule)

        # RULE 25: IF (cholesterol IS high) THEN health IS sick_2;
        temp = self.diagnosis_dict["sick_2"]
        output_rule = self.membership_dict["cholesterol"]["high"]
        self.diagnosis_dict["sick_2"] = max(temp, output_rule)

        # RULE 26: IF (cholesterol IS high) THEN health IS sick_3;
        temp = self.diagnosis_dict["sick_3"]
        output_rule = self.membership_dict["cholesterol"]["high"]
        self.diagnosis_dict["sick_3"] = max(temp, output_rule)

        # RULE 27: IF (cholesterol IS very_high) THEN health IS sick_4;
        temp = self.diagnosis_dict["sick_4"]
        output_rule = self.membership_dict["cholesterol"]["very_high"]
        self.diagnosis_dict["sick_4"] = max(temp, output_rule)

        # RULE 28: IF (blood_sugar IS true) THEN health IS sick_2;
        temp = self.diagnosis_dict["sick_2"]
        output_rule = self.membership_dict["blood_sugar"]["true"]
        self.diagnosis_dict["sick_2"] = max(temp, output_rule)

        # RULE 29: IF (ECG IS normal) THEN health IS healthy;
        temp = self.diagnosis_dict["healthy"]
        output_rule = self.membership_dict["ECG"]["normal"]
        self.diagnosis_dict["healthy"] = max(temp, output_rule)

        # RULE 30: IF (ECG IS normal) THEN health IS sick_1;
        temp = self.diagnosis_dict["sick_1"]
        output_rule = self.membership_dict["ECG"]["normal"]
        self.diagnosis_dict["sick_1"] = max(temp, output_rule)

        # RULE 31: IF (ECG IS abnormal) THEN health IS sick_2;
        temp = self.diagnosis_dict["sick_2"]
        output_rule = self.membership_dict["ECG"]["abnormal"]
        self.diagnosis_dict["sick_2"] = max(temp, output_rule)

        # RULE 32: IF (ECG IS hypertrophy) THEN health IS sick_3;
        temp = self.diagnosis_dict["sick_3"]
        output_rule = self.membership_dict["ECG"]["hypertrophy"]
        self.diagnosis_dict["sick_3"] = max(temp, output_rule)
        
        # RULE 33: IF (ECG IS hypertrophy) THEN health IS sick_4;
        temp = self.diagnosis_dict["sick_4"]
        output_rule = self.membership_dict["ECG"]["hypertrophy"]
        self.diagnosis_dict["sick_4"] = max(temp, output_rule)

        # RULE 34: IF (maximum_heart_rate IS low) THEN health IS healthy;
        temp = self.diagnosis_dict["healthy"]
        output_rule = self.membership_dict["heart_rate"]["low"]
        self.diagnosis_dict["healthy"] = max(temp, output_rule)

        # RULE 35: IF (maximum_heart_rate IS medium) THEN health IS sick_1;
        temp = self.diagnosis_dict["sick_1"]
        output_rule = self.membership_dict["heart_rate"]["medium"]
        self.diagnosis_dict["sick_1"] = max(temp, output_rule)

        # RULE 36: IF (maximum_heart_rate IS medium) THEN health IS sick_2;
        temp = self.diagnosis_dict["sick_2"]
        output_rule = self.membership_dict["heart_rate"]["medium"]
        self.diagnosis_dict["sick_2"] = max(temp, output_rule)

        # RULE 37: IF(maximum_heart_rate IS high) THEN health IS sick_3;
        temp = self.diagnosis_dict["sick_3"]
        output_rule = self.membership_dict["heart_rate"]["high"]
        self.diagnosis_dict["sick_3"] = max(temp, output_rule)

        # RULE 38: IF(maximum_heart_rate IS high) THEN health IS sick_4;
        temp = self.diagnosis_dict["sick_4"]
        output_rule = self.membership_dict["heart_rate"]["high"]
        self.diagnosis_dict["sick_4"] = max(temp, output_rule)

        # RULE 39: IF (exercise IS true) THEN health IS sick_2;
        temp = self.diagnosis_dict["sick_2"]
        output_rule = self.membership_dict["exercise"]["true"]
        self.diagnosis_dict["sick_2"] = max(temp, output_rule)

        # RULE 40: IF (old_peak IS low) THEN health IS healthy;
        temp = self.diagnosis_dict["healthy"]
        output_rule = self.membership_dict["old_peak"]["low"]
        self.diagnosis_dict["healthy"] = max(temp, output_rule)

        # RULE 41: IF (old_peak IS low) THEN health IS sick_1;
        temp = self.diagnosis_dict["sick_1"]
        output_rule = self.membership_dict["old_peak"]["low"]
        self.diagnosis_dict["sick_1"] = max(temp, output_rule)

        # RULE 42: IF (old_peak IS terrible) THEN health IS sick_2;
        temp = self.diagnosis_dict["sick_2"]
        output_rule = self.membership_dict["old_peak"]["terrible"]
        self.diagnosis_dict["sick_2"] = max(temp, output_rule)

        # RULE 43: IF (old_peak IS terrible) THEN health IS sick_3;
        temp = self.diagnosis_dict["sick_3"]
        output_rule = self.membership_dict["old_peak"]["terrible"]
        self.diagnosis_dict["sick_3"] = max(temp, output_rule)

        # RULE 44: IF (old_peak IS risk) THEN health IS sick_4;
        temp = self.diagnosis_dict["sick_4"]
        output_rule = self.membership_dict["old_peak"]["risk"]
        self.diagnosis_dict["sick_4"] = max(temp, output_rule)

        # RULE 45: IF (thallium IS normal) THEN health IS healthy;
        temp = self.diagnosis_dict["healthy"]
        output_rule = self.membership_dict["thallium"]["normal"]
        self.diagnosis_dict["healthy"] = max(temp, output_rule)

        # RULE 46: IF (thallium IS normal) THEN health IS sick_1;
        temp = self.diagnosis_dict["sick_1"]
        output_rule = self.membership_dict["thallium"]["normal"]
        self.diagnosis_dict["sick_1"] = max(temp, output_rule)

        # RULE 47: IF (thallium IS medium) THEN health IS sick_2;
        temp = self.diagnosis_dict["sick_2"]
        output_rule = self.membership_dict["thallium"]["medium"]
        self.diagnosis_dict["sick_2"] = max(temp, output_rule)

        # RULE 48: IF (thallium IS high) THEN health IS sick_3;
        temp = self.diagnosis_dict["sick_3"]
        output_rule = self.membership_dict["thallium"]["high"]
        self.diagnosis_dict["sick_3"] = max(temp, output_rule)

        # RULE 49: IF (thallium IS high) THEN health IS sick_4;
        temp = self.diagnosis_dict["sick_4"]
        output_rule = self.membership_dict["thallium"]["high"]
        self.diagnosis_dict["sick_4"] = max(temp, output_rule)

        # RULE 50: IF (age IS young) THEN health IS healthy;
        temp = self.diagnosis_dict["healthy"]
        output_rule = self.membership_dict["age"]["young"]
        self.diagnosis_dict["healthy"] = max(temp, output_rule)

        # RULE 51: IF (age IS mild) THEN health IS sick_1;
        temp = self.diagnosis_dict["sick_1"]
        output_rule = self.membership_dict["age"]["mild"]
        self.diagnosis_dict["sick_1"] = max(temp, output_rule)

        # RULE 52: IF (age IS old) THEN health IS sick_2;
        temp = self.diagnosis_dict["sick_2"]
        output_rule = self.membership_dict["age"]["old"]
        self.diagnosis_dict["sick_2"] = max(temp, output_rule)

        # RULE 53: IF (age IS old) THEN health IS sick_3;
        temp = self.diagnosis_dict["sick_3"]
        output_rule = self.membership_dict["age"]["old"]
        self.diagnosis_dict["sick_3"] = max(temp, output_rule)

        # RULE 54: IF (age IS very_old) THEN health IS sick_4;
        temp = self.diagnosis_dict["sick_4"]
        output_rule = self.membership_dict["age"]["very_old"]
        self.diagnosis_dict["sick_4"] = max(temp, output_rule)

        return self.diagnosis_dict
        
        
        