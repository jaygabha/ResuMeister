pip install Flask==2.2.2
pip install resume-parser
pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.3.1/en_core_web_sm-2.3.1.tar.gz
pip install importlib-metadata==3.2.0
python -m spacy download en_core_web_sm
python -m nltk.downloader stopwords
python -m nltk.downloader punkt
python -m nltk.downloader averaged_perceptron_tagger
python -m nltk.downloader universal_tagset
python -m nltk.downloader wordnet
python -m nltk.downloader brown
python -m nltk.downloader maxent_ne_chunker