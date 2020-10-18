from controllers.sentiment_analysis import SentimentAnalysis
from controllers.images import Images


def initialize_routes(api):
    api.add_resource(SentimentAnalysis, '/sa')
    api.add_resource(Images, '/img/<string:image>')