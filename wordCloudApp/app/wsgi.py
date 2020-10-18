import nltk
from main_app import flask_app

if __name__ == '__main__':
  nltk.download('stopwords')
  flask_app.run('0.0.0.0', port=5000, debug=True)