from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "たこやき"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

    @app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "末吉",
        "凶",
        "小凶",
        "大凶"
    ]
    random_omikuzi = random.choice(omikuji_list)

    if random_omikuzi == "大吉":
    return {"大吉！素晴らしい幸運が舞い込むでしょう。"}
    else if random_omikuzi == "中吉":
    return {"中吉！努力が実を結び、良い結果が待っています。"}
    else if random_omikuzi == "小吉":
    return {"小吉！ちょっとした幸運があなたの元にやってきます。"}
    else if random_omikuzi == "吉":
    return {"吉！安定した幸せな日々が続くでしょう。"}
    else if random_omikuzi == "末吉":
    return {"末吉！努力が実り始め、良い方向に進む時期です。"}
    else if random_omikuzi == "凶":
    return {"凶。悪いことが起こるかもしれませんが、気を引き締めてください。"}
    else if random_omikuzi == "小凶":
    return {"小凶。注意が必要な日です。慎重に行動しましょう。"}
    else:
    return {"大凶。厳しい状況が訪れるかもしれませんが、乗り越えましょう。"}