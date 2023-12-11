import streamlit as st
import requests
from flask import Flask, send_file

app = Flask(__name__)

# Path to your video file
video_path = "video.mp4"

# Read the video file
with open(video_path, "rb") as video_file:
    video_content = video_file.read()

# Streamlit app to display video
st.video(video_content, format="video/mp4")

# Flask route to serve the video content
@app.route('/get_video')
def get_video():
    return send_file(video_path, mimetype='video/mp4')

if __name__ == '__main__':
    app.run(port=8502)
