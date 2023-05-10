source venv/bin/activate
python /home/pi/project/app.py &
export DISPLAY=:0
chromium-browser --kiosk 0.0.0.0:8080/current
