
from fuzzification import Fuzzification
from inference import Inference
from defuzzification import Defuzzification

class ProvideResult(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ProvideResult, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def get_final_result(input_dict: dict) -> str:

        myfuzzification = Fuzzification(input_dict)
        membership_dict = myfuzzification.fuzzificate()
        # print(membership_dict)

        myinference = Inference(membership_dict)
        diagnosis_dict = myinference.infer()
        # print(diagnosis_dict)

        mydifuzzification = Defuzzification(diagnosis_dict)
        return mydifuzzification.defuzzificate()

        
