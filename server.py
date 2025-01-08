'''
Imports from flask and local module EmotionDetection
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def redirect_call():
    '''
    Default path function to display user interface for applet
    '''
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_call():
    '''
    /emotionDetector pathway to take user form data and interpret it
    for emotions
    '''
    text_to_analyze = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    emotions = ["anger", "disgust", "fear", "joy"]
    out = "For the given statement, the system response is "
    for emotion in emotions:
        out += "\"" + emotion + "\": " + str(result[emotion]) + ", "
    out += " and \"sadness\": " + str(result["sadness"]) + ". The dominant emotion is <b>"
    out += result["dominant_emotion"] + "</b>."
    return out #render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
