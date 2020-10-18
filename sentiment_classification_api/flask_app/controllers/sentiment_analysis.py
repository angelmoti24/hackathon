from flask_restful import Resource
from flask import request, make_response
from logging import getLogger
from schemas.schemas import sentiment_analysis_schema
from jsonschema import validate
from fasttext import load_model


logger = getLogger()
model = load_model('/app/bin/watman.ftz')

class SentimentAnalysis(Resource):

    def post(self):
        try:
            logger.error("Hola")
            logger.error(request)
            payload = request.get_json()
            logger.error(payload)
            validate(instance=payload, schema=sentiment_analysis_schema)
            comments = payload['comments']
            predictions = model.predict(comments)
            response = dict()
            labels_map = {
                '__label__0': 'negative',
                '__label__1': 'positive'
            }
            for i in range(len(comments)):
                response[str(i)] = {
                    'prediction': labels_map[predictions[0][i][0]],
                    'confidence': predictions[1][i].tolist()[0]
                }
            logger.error(response)
            return make_response(response, 200)
        except Exception as e:
            logger.error(e)
            return make_response({'error': f'{e}'}, 500)