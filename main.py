from typing import Optional

from fastapi import FastAPI

from fastapi.responses import HTMLResponse

import random  # randomライブラリを追加

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

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
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]

    return omikuji_list[random.randrange(10)]

@app.get("/lunch")
def lanch():
    lanch_list=[
        "おにぎり",
        "担々麺",
        "おまえ"
    ]
    return lanch_list[random.randrange(3)]

@app.post("/present")
async def give_present(present):
    return {"response": f"サーバです。メリークリスマス！ {present}ありがとう。お返しはキャンディーです。\n"}  # f文字列というPythonの機能を使っている

@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <script src="https://cdn.tailwindcss.com"></script>
            <title>24FI023自己紹介</title>
        </head>
        <body>
            <div class="bg-amber-400 p-5 text-stone-800">
                <h1 class="text-5xl font-bold">学籍番号:24FI023</h1>
            </div>
            <div class="pl-7 bg-stone-100 m-5">
                <h2 class="pt-3 text-2xl font-bold">最近好きなもの</h2>
                <ul class="mt-2">
                    <li>・観葉植物</li>
                    <li>・キーボード</li>
                    <li>・スピーカー</li>
                    <li>・サイクリング</li>
                </ul>
                <h2 class="pt-3 text-2xl font-bold">最近嫌いなもの</h2>
                <ul class="mt-2">
                    <li>・室内と外の気温差</li>
                    <li>・就活早期化</li>
                </ul>
            </div>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/sagisi")
async def give_money(money :int):
    return {"response": f"サーバです。{money}円ありがとうございます。お返しに{half(money)}円お渡しします。\n"}

def half(n):
    return n//2