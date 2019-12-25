
import obd
from flask import Flask


app = Flask(__name__)

import requests



def mph():
    obd.logger.setLevel(obd.logging.DEBUG)
    print(obd.__path__)
    # ports = obd.scan_serial()       # return list of valid USB or RF portsa
    # print(ports)
    #connection = obd.OBD(portstr="COM4")  # auto-connects to USB or RF port
    connection = obd.OBD(portstr="COM3")
    #cmd = obd.commands.SPEED  # select an OBD command (sensor)

    #response = connection.query(cmd)  # send the command, and parse the response
    # ports = obd.scan_serial()
    # print(ports)

    return connection

connection = mph()

@app.route('/mph')
def keepRunning():

    cmd = obd.commands.SPEED
    response = connection.query(cmd)  # send the command, and parse the response
    return str(response.value.to("mph").magnitude)


@app.route('/libs/face-api.js')
def getfaceapi():
    return requests.get("https://www.voby.us/libs/face-api.js").content


@app.route('/drowsydetector')
def drowsydetector():
    return requests.get("https://www.voby.us/drowsydetect.html").text


@app.route('/drowsydetectlive')
def drowsydetectlive():
    return requests.get("https://www.voby.us/drowsydetectlive.html").text


@app.route('/landmarks', methods=['POST'])
def landmarks():
    # DO AI
    return 'good'


@app.route('/libs/models/ssd_mobilenetv1_model-weights_manifest.json')
def routea():
    return requests.get("https://www.voby.us/libs/models/ssd_mobilenetv1_model-weights_manifest.json").content


@app.route('/libs/models/ssd_mobilenetv1_model-shard1')
def routeb():
    return requests.get("https://www.voby.us/libs/models/ssd_mobilenetv1_model-shard1").content


@app.route('/libs/models/ssd_mobilenetv1_model-shard2')
def routec():
    return requests.get("https://www.voby.us/libs/models/ssd_mobilenetv1_model-shard2").content


@app.route('/libs/models/tiny_face_detector_model-weights_manifest.json')
def routed():
    return requests.get("https://www.voby.us/libs/models/tiny_face_detector_model-weights_manifest.json").content


@app.route('/libs/models/tiny_face_detector_model-shard1')
def routee():
    return requests.get("https://www.voby.us/libs/models/tiny_face_detector_model-shard1").content


@app.route('/libs/models/mtcnn_model-weights_manifest.json')
def routef():
    return requests.get("https://www.voby.us/libs/models/mtcnn_model-weights_manifest.json").content


@app.route('/libs/models/mtcnn_model-shard1')
def routeg():
    return requests.get("https://www.voby.us/libs/models/mtcnn_model-shard1").content


@app.route('/libs/models/face_landmark_68_model-weights_manifest.json')
def routeh():
    return requests.get("https://www.voby.us/libs/models/face_landmark_68_model-weights_manifest.json").content


@app.route('/libs/models/face_landmark_68_model-shard1')
def routei():
    return requests.get("https://www.voby.us/libs/models/face_landmark_68_model-shard1").content


@app.route('/libs/models/face_landmark_68_tiny_model-weights_manifest.json')
def routej():
    return requests.get("https://www.voby.us/libs/models/face_landmark_68_tiny_model-weights_manifest.json").content


@app.route('/libs/models/face_landmark_68_tiny_model-shard1')
def routek():
    return requests.get("https://www.voby.us/libs/models/face_landmark_68_tiny_model-shard1").content


@app.route('/libs/models/face_recognition_model-weights_manifest.json')
def routel():
    return requests.get("https://www.voby.us/libs/models/face_recognition_model-weights_manifest.json").content


@app.route('/libs/models/face_recognition_model-shard1')
def routem():
    return requests.get("https://www.voby.us/libs/models/face_recognition_model-shard1").content


@app.route('/libs/models/face_recognition_model-shard2')
def routen():
    return requests.get("https://www.voby.us/libs/models/face_recognition_model-shard2").content


@app.route('/libs/models/face_expression_model-weights_manifest.json')
def routeo():
    return requests.get("https://www.voby.us/libs/models/face_expression_model-weights_manifest.json").content


@app.route('/libs/models/face_expression_model-shard1')
def routep():
    return requests.get("https://www.voby.us/libs/models/face_expression_model-shard1").content


@app.route('/libs/models/face_expression_model-shard2')
def routeq():
    return requests.get("https://www.voby.us/libs/models/face_expression_model-shard2").content


@app.route('/static/model.json', methods=['POST', 'OPTION'])
def model():
    return requests.get("http://127.0.0.1:5000/static/model.json").content


if __name__ == '__main__':
    app.run()