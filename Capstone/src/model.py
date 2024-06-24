import joblib


class Model:
    def __init__(self):
        self.model = joblib.load('model/catboost_model.pkl')

    def predict(self, input_features):
        return self.model.predict(input_features)
    

    # Add in this code chunk temporarily (delete it after this run)
# beneficiary_example = {
#     "age": 40,
#     "gender": 0,
#     "married":1,
#     "senior_citizen":0,
#     "tenure_months": 30,
#     "num_referrals": 8,
#     "has_internet_service": 1,
#     "has_unlimited_data":1,
#     "has_phone_service": 1,
#     "has_multiple_lines": 1,
#     "has_premium_tech_support": 0,
#     "has_online_security":1,
#     "has_online_backup":0,
#     "paperless_billing":1,
#     "payment_method":1,
#     "avg_long_distance_fee_monthly":15,
#     "total_long_distance_fee":40
# }
# model_inputs = list(beneficiary_example.values())

# print(model_inputs)                  
# print(Model().predict(model_inputs)) 