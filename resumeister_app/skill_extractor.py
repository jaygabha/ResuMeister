# skill_extractor_app/skill_extractor.py
import spacy
from spacy.matcher import PhraseMatcher



class SkillExtractor:
    def __init__(self, nlp,phrase_matcher):
        self.nlp = nlp
        self.skill_db = skill_db
        self.matcher = phrase_matcher(nlp.vocab)
        self.matcher.add("SKILLS", None, *[nlp(skill) for skill in self.skill_db])

    def annotate(self, job_description):
        doc = self.nlp(job_description)
        matches = self.matcher(doc)
        annotations = {"results": {"full_matches": [], "ngram_scored": []}}
        for match_id, start, end in matches:
            span = doc[start:end]
            annotations["results"]["full_matches"].append({"doc_node_value": span.text})
        
        return set(annotations)


nlp = spacy.load('en_core_web_sm')

skill_extractor = SkillExtractor(nlp,PhraseMatcher)
