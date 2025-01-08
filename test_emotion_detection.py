import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        phrase_list = ["I am glad this happened",
                       "I am really mad about this",
                       "I feel disgusted just hearing about this",
                       "I am so sad about this",
                       "I am really afraid that this will happen"]
        response_list = ["joy", "anger", "disgust", "sadness", "fear"]
        for index in range(len(phrase_list)):
            response = emotion_detector(phrase_list[index])
            self.assertEqual(response['dominant_emotion'], response_list[index])

unittest.main()