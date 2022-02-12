"""
Script run requests to fake scammer site and fill fake forms. 
I didn't hack anything, didn't do anything that a normal person couldn't have done. 
No hacks, exploits, vulnerabilities, break-ins. Every action I took was publicly available 
to me and everyone else that went to scam site.

"""
import requests
import threading

url = 'http://wildberris.ru/PS5/includes/submit_order_limelight.php'

data = {
    
    #Form Data from scammers fake site. Copy and fill like 'name_data': 'value'

    'cc_number': '4007000000027',
    'cc_expmonth': '08',
    'cc_expyear': '21',
    'cc_cvv': '234',
}

def do_request():
    while True:
        
        response = requests.post(url, data=data).text
        print(response)

threads = []

for i in range(50):
    t = threading.Thread(target=do_request)
    t.daemon = True
    threads.append(t)


for i in range(50):
    threads[i].start()


for i in range(50):
    threads[i].join()

