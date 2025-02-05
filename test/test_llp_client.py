import unittest
from llp_client import NamedEntityClient
from test_doubles import LlpModelTestDouble


class TestLlpClient(unittest.TestCase):
    
    def test_get_ents_returns_dictionary_given_empty_string_causes_empty_spacy_doc_ents(self):
        model = LlpModelTestDouble('eng')
        model.returns_doc_ents([])
        llp = NamedEntityClient(model)
        ents = llp.get_ents("")
        self.assertIsInstance(ents, dict)

    def test_get_ents_returns_dictionary_given_nonempty_string_causes_empty_spacy_doc_ents(self):
        model = LlpModelTestDouble('eng')
        model.returns_doc_ents([])
        llp = NamedEntityClient(model)
        ents = llp.get_ents("Madison is a city in Wisconsin")
        self.assertIsInstance(ents, dict)

    def test_get_ents_given_spacy_PERSON_is_returned_serializes_to_Person(self):
        model = LlpModelTestDouble('eng')
        doc_ents = [{'text': 'Laurent Fressinet', 'label_':'PERSON'}]
        model.returns_doc_ents(doc_ents)
        llp = NamedEntityClient(model)
        result = llp.get_ents('...')
        expected_result = { 'ents': [{'ent': 'Laurent Fressinet', 'label': 'PERSON'}], 'html': ""}
        self.assertListEqual(result['ents'], expected_result['ents'])

    def test_get_ents_given_spacy_NORP_is_returned_serializes_to_Group(self):
        model = LlpModelTestDouble('eng')
        doc_ents = [{'text': 'Lithuanian', 'label_':'NORP'}]
        model.returns_doc_ents(doc_ents)
        llp = NamedEntityClient(model)
        result = llp.get_ents('...')
        expected_result = { 'ents': [{'ent': 'Lthuanian', 'label': 'Group'}], 'html': ""}
        self.assertListEqual(result['ents'], expected_result['ents'])
