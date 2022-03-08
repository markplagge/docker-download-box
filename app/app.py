import flask 
from flask import Flask, render_template
import random
import yaml

app = Flask(__name__)

welcome = "Welcome to Starbase 0420-69"
subtitle = "Holodeck Entertainment Management System"
warning_file = "warning_file.yaml"

def get_warning_services():
    global warning_file
    with open(warning_file,'r') as f:
        d = yaml.load(f, Loader=yaml.FullLoader)
    days = d['days']
    services = d['services']
    print(d)
    print(services)
    ports = d['service_urls']
    default_server = d['default_server'] 
    urls = {}
    for service,port in ports.items():
        urls[service] = f'{default_server}:{port}'
        if service in d['service_ovr'].keys():
            urls[service] = f'{d["service_ovr"]}:{port}'

    top_service_names = d['top_services']
    top_services = {}
    for top_service in top_service_names:
        top_services[top_service] = urls[top_service]

    days += random.randint(1,10)
    with open(warning_file,'w') as f:
        yaml.dump(d,f)
    return days,services,urls, top_services


def generate_warning_services():
    days, services,urls = get_warning_services()
    warning = f"{days} days since last major holodeck malfunction"
    srv_msg = []
    nl = '\n'.join(srv_msg)
    service_list = "<ul>\n" + f"{nl}" + "\n</ul> "


    return warning,services,urls



@app.route('/')
def index():
    warning, services, urls, top_services = generate_warning_services()
    print("-----")
    print(urls)
    print("-----")
    
    ts_names = list(top_services)
    ts_d = top_services
    print(ts_names)
    print(ts_d)
    return render_template('main.html',ts_names=ts_names,ts_d=ts_d,welcome=welcome,subtitle=subtitle,warning=warning,services=services,urls=urls)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=9999)
    
