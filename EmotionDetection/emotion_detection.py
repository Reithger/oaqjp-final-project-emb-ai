import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_form = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, headers = headers, json = json_form)
    emotions = ["anger", "disgust", "fear", "joy", "sadness"]
    if(response.status_code == 400):
        out = {}
        for emotion in emotions:
            out[emotion] = None
        out["dominant_emotion"] = None
        return out
        
    formatted = json.loads(response.text)
    relevant = formatted['emotionPredictions'][0]['emotion']
    text_emotion = {}
    largest = emotions[0]
    for emotion in emotions:
        text_emotion[emotion] = relevant[emotion]
        if(relevant[emotion] > relevant[largest]):
            largest = emotion
    text_emotion["dominant_emotion"] = largest
    return text_emotion

#print(emotion_detector("Testing out this good phrase"))