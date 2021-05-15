import spacy
from src.utils.custom_entities import subjects
spacy_engine = spacy.load('en_core_web_sm')


def filter_noun(input_spacy_doc):
    """
    Take spacy doc, returns list of nouns
    :param input_spacy_doc: Spacy doc
    :return: List of nouns
    """
    noun_list = []
    for noun in input_spacy_doc.noun_chunks:
        if noun.text.lower() not in subjects:
            noun_list.append(noun.text)
    return noun_list
