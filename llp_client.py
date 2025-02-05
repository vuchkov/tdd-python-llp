class NamedEntityClient:
    def __init__(self, model):
        # self.model = spacy.load("en_core_web_sm")
        self.model = model

    def get_ents(self, sentence):
        doc = self.model(sentence)
        entities = [{ 'ent': ent.text, 'label': self.map_label(ent.label_)} for ent in doc.ents]
        return { 'ents': entities, 'html': '' }

    @staticmethod
    def map_label(label):
        label_map = {
            'PERSON': 'Person',
            'NORP': 'Group'
        }
        return label_map.get(label)
