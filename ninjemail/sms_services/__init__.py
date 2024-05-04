from sms_services import getsmscode
from sms_services import smspool
from sms_services import fivesim

def get_sms_instance(sms_info):
    """
    Retrieves an instance of an SMS provider based on the given SMS information.

    Args:
        sms_info (dict): A dictionary containing the SMS service name and associated data.

    Returns:
        object: An instance of the SMS provider based on the provided SMS service.
    """
    service_name = sms_info['name']

    if service_name == 'getsmscode':
        data = sms_info['data']
        data.update({'project': 1, 'country': 'hk'})
        sms_provider = getsmscode.GetsmsCode(**data)
    elif service_name == 'smspool':
        data = sms_info['data']
        data.update({'service': 395})
        sms_provider = smspool.SMSPool(**data)
    elif service_name == '5sim':
        data = sms_info['data']
        data.update({'service': 'google'})
        sms_provider = fivesim.FiveSim(**data)

    return sms_provider
