from flask import Flask, render_template, Response
from emotionEmoji import start_app
import cv2
import time

predict='HAPPEN'
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

    
@app.route('/before')
def before():
    return render_template('before.html')



@app.route('/HAPPY')
def HAPPY():
    return render_template('HAPPY.html')

@app.route('/SAD')
def SAD():
    return render_template('SAD.html')

@app.route('/ANGRY')
def ANGRY():
    return render_template('ANGRY.html')

@app.route('/FEAR')
def FEAR():
    return render_template('FEAR.html')

@app.route('/SURPRISE')
def SURPRISE():
    return render_template('SURPRISE.html')

@app.route('/DISGUST')
def DISGUST():
    return render_template('DISGUST.html')

@app.route('/NEUTRAL')
def NEUTRAL():
    return render_template('NEUTRAL.html')



@app.route('/')
def gen():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if ret:
            frame = cv2.resize(frame, (1366, 800))
            frame,pred = start_app(frame)
            print(pred)
            global predict
            predict=pred
            print("new one******************",predict)
            #print("value****************",list[0])
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
               
            '''cv2.imshow('Filter',frame)
            cv2.waitKey(1)'''
        else:
            break
       


'''@app.route('/detect')
def emodetect():
    res = detect()
    return res
    #return statement needed'''

@app.route('/new')
def new():
    return render_template('new.html',predict=predict)

@app.route('/video_feed')
def video_feed():
    return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__ == '__main__':
    app.run(debug=True)