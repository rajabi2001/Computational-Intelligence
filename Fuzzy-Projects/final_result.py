
from fuzzification import Fuzzification
from inference import Inference

class ProvideResult(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ProvideResult, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def get_final_result(input_dict: dict) -> str:

        myfuzziofication = Fuzzification(input_dict)
        membership_dict = myfuzziofication.fuzzificate()
        print(membership_dict)

        myinference = Inference(membership_dict)
        pass
