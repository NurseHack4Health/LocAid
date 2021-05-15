from src.data_layer.bot_io import UserInput
from src.logic_layer.request_item import spacy_engine, filter_noun
from src.utils.custom_entities import bot_item_response_default
from fastapi import APIRouter
router = APIRouter()


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
