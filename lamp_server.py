from flask import Flask, request, render_template, send_from_directory
import RPi.GPIO as GPIO
app = Flask(__name__)
lamp_status = False

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/toggle")
def toggle():
	global lamp_status
	lamp_status = not lamp_status
	if lamp_status:
		GPIO.output(8, GPIO.HIGH)
	else:
		GPIO.output(8, GPIO.LOW)
	return redirect("http://192.168.2.19/", code=302)

@app.route("/res/<path:path>")
def send_res(path):
	return send_from_directory('res', path)

if __name__ == "__main__":
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

	app.run(host='0.0.0.0', port=80)
