from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import sys
sys.path.append('./gpt-helper')
# import stream

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


class Item(BaseModel):
    title: str
    question: str

is_chat_helper_start = False
pending_question = []
@app.put("/gptchat")
def update_item(item: Item):
    print("received item: ", item)
    if is_chat_helper_start == False:
        is_chat_helper_start = True
        pending_question.append(item)
        # start service in another thread
        return {"status": 'running'}
    else:
        pending_question.append(item)
        return {"status": 'pending'}