pip install Flask==2.2.2
pip install resume-parser
pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.3.1/en_core_web_sm-2.3.1.tar.gz
pip install importlib-metadata==3.2.0
python3 -m spacy download en_core_web_sm
python3 -m nltk.downloader stopwords
python3 -m nltk.downloader punkt
python3 -m nltk.downloader averaged_perceptron_tagger
python3 -m nltk.downloader universal_tagset
python3 -m nltk.downloader wordnet
python3 -m nltk.downloader brown
python3 -m nltk.downloader maxent_ne_chunker