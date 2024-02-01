import psutil
import json
from flask import Flask, jsonify

app = Flask(__name__)

def get_pc_data():
    cpu_usage = psutil.cpu_percent()
    mem_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')

    data = {
        'cpu_usage': cpu_usage,
        'mem_total': mem_info.total / (1024 ** 3),
        'mem_used': mem_info.used / (1024 ** 3),
        'mem_free': mem_info.free / (1024 ** 3),
        'disk_total': disk_info.total / (1024 ** 3),
        'disk_used': disk_info.used / (1024 ** 3),
        'disk_free': disk_info.free / (1024 ** 3)
    }

    return json.dumps(data)

@app.route('/api/pc-data')
def pc_data():
    return jsonify(get_pc_data())

if __name__ == '__main__':
    app.run(debug=True)