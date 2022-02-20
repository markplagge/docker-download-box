import flask 
from flask import Flask, render_template
import random
import yaml

app = Flask(__name__)

welcome = "Welcome to Starbase 003"
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
    days += random.randint(1,10)
    with open(warning_file,'w') as f:
        yaml.dump(d,f)
    return days,services


def generate_warning_services():
    days, services = get_warning_services()
    warning = f"{days} days since last major holodeck malfunction"
    srv_msg = []
    nl = '\n'.join(srv_msg)
    service_list = f"<ul>\n{nl}\n</ul> "
    return warning,services



@app.route('/')
def index():
    warning, services = generate_warning_services()
    return render_template('main.html',welcome=welcome,subtitle=subtitle,warning=warning,services=services)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=9999)
    