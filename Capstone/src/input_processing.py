# input_processing.py (within same directory as app.py)

def senior(age):
    if age > 65:
        return int(1)
    else:
        return int(0)
    
def format_model_inputs(input_dict):
    age = int(input_dict['age'])
    gender = int(input_dict['gender'])
    married = int(input_dict['married'])
    senior_citizen = senior(age)
    tenure_months = int(input_dict['tenure_months'])
    num_referrals = int(input_dict['num_referrals'])
    has_internet_service = int(input_dict['has_internet_service'])
    has_unlimited_data = int(input_dict['has_unlimited_data'])
    has_phone_service = int(input_dict['has_phone_service'])
    has_multiple_lines = int(input_dict['has_multiple_lines'])
    has_premium_tech_support = int(input_dict['has_premium_tech_support'])
    has_online_security = int(input_dict['has_online_security'])
    has_online_backup = int(input_dict['has_online_backup'])
    paperless_billing = int(input_dict['paperless_billing'])
    payment_method = int(input_dict['payment_method'])
    avg_long_distance_fee_monthly = float(input_dict['avg_long_distance_fee_monthly'])
    total_long_distance_fee = float(input_dict['total_long_distance_fee'])

    
    return [age, gender, married, senior_citizen, tenure_months, num_referrals, has_internet_service,has_unlimited_data,
             has_phone_service,has_multiple_lines, has_premium_tech_support, has_online_security, has_online_backup,
             paperless_billing,payment_method, avg_long_distance_fee_monthly, total_long_distance_fee]