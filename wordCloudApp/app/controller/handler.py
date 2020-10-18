import re
import unicodedata
import pandas as pd
import base64
import cv2
#from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator
from nltk.corpus import stopwords as sw
from os import environ
from flask_restful import Resource
from json import JSONEncoder, loads
from flask import request, make_response




class JsonEncoder(JSONEncoder):
    def default(self, object):
        if isinstance(object, ObjectId):
            return str(object)
        return JSONEncoder.default(self, object)


class WordCloud(Resource):

    def post(self):
        payload = request.get_json(force=True)
        dataset = payload["dataset"]
        try:
            image = wordcloud(dataset)
            response = {
                "imageBase64": base64.b64encode(image.to_array()),
            }
            return make_response(response, 200)
        except Exception as e:
            response = {'error':str(e)}
            logger.error(f"WordCloud task could not be executed: {str(e)}")
            return make_response(response, 400)


def clean_text(text):
    cleaned_text = unicodedata.normalize('NFD', text).encode('ascii', 'ignore')
    cleaned_text = re.sub('[^a-zA-Z ]', " ", cleaned_text.decode("utf-8"), flags=re.UNICODE)
    text = u' '.join(cleaned_text.lower().split())
    text = text.lower().replace("  "," ").replace("https","").replace("bbva","").replace("xaguzar2","").replace("enero","").replace("va","").replace("cobrar","")
    text = re.sub("co ","",(re.sub(" $","",re.sub("^ ","",text))))
    text = [word.replace(".co/","") for word in text.split(" ") if word not in stopwords]
    text = [word for word in text if len(word)>2]
    text = " ".join(text)
    return text


def wordcloud(dataset):
    stopwords = sw.words("spanish")+ ["rt","https","xaguzar2","bbva","hola","peruano","año","mex","anos","vibqpmlgsg"]
    data=pd.read_pickle(f"datasets/{dataset}.pkl")
    data["cleanText"] = data.text.map(clean_text)
    imagen_act=cv2.imread(f"masks/{dataset}.png")
    wordcloud = WordCloud(mask=imagen_act,
                        max_font_size=200,
                        background_color="#393d3f",
                        colormap="Blues"
                        ).generate(text_cloud)
    return wordcloud
