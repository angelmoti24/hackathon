from controller.handler import WordCloud

def initialize_endpoints(api):
    api.add_resource(WordCloud, "/wordcloud")
    