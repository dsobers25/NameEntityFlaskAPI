class NamedEntityClient():
    def __init__(self, model):
        # tightly cuppled to spacy dep
        # this should depend on an abstraction
        # We do not want to load this model everytime we create a new instance of this class
        # self.model = spacy.load("en_core_web_sm")  % tightly cuppled to spacy dep.
        self.model = model

    def get_ents(self, sentence):
        doc = self.model(sentence)
        entities = [{ 'ent': ent.text, 'label' : self.map_label(ent.label_) } for ent in doc.ents]
        return {'ents': entities, 'html': ''}

    @staticmethod
    def map_label(label):
        label_map = {
            'PERSON'  : 'Person',
            'NORP'    : 'Group',
            'LOC'     : 'Location',
            'LANGUAGE': 'Language',
            'GPE'     : 'Location'
        }

        return label_map.get(label) 