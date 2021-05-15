import spacy
spacy_engine = spacy.load('en_core_web_sm')
from src.data_layer.bot_io import UserInput
from src.utils.custom_entities import subjects, bot_item_response_default
from fastapi import APIRouter
router = APIRouter()


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


@router.post("/request_item")
def request_item(user_input: UserInput):
    """
    Receive user's text input, replies list of items that user requested
    """
    if not len(user_input.text) >= 1:
        raise Exception("User input text must have at least one word")

    # Tokenize input string, return list of nouns
    spacy_doc = spacy_engine(user_input.text)
    noun_list = filter_noun(spacy_doc)
    return f"{bot_item_response_default}: {noun_list}"
