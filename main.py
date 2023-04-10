import requests as r
from threading import Thread
import os
import uuid
import time
import datetime

with open("limiteds.txt", "r") as f:
    limiteds = f.read().replace(" ", "").split(",")

with open("cookie.txt", "r") as f:
    cookie = f.read()


user_id = r.get("https://users.roblox.com/v1/users/authenticated", cookies={".ROBLOSECURITY": cookie}).json()["id"]
x_token = ""
def get_x_token():
    global x_token

    x_token = r.post("https://auth.roblox.com/v2/logout",
                     cookies={".ROBLOSECURITY": cookie}).headers["x-csrf-token"]
    print("Entrei na conta.")

    while 1:
        # Gets the x_token every 4 minutes.
        x_token = r.post("https://auth.roblox.com/v2/logout",
                         cookies={".ROBLOSECURITY": cookie}).headers["x-csrf-token"]
        time.sleep(248)


def buy(json, itemid, productid):
    print("Comprando o item sem parar...")

    data = {
        "collectibleItemId": itemid,
        "expectedCurrency": 1,
        "expectedPrice": 0,
        "expectedPurchaserId": user_id,
        "expectedPurchaserType": "User",
        "expectedSellerId": json["creatorTargetId"],
        "expectedSellerType": "User",
        "idempotencyKey": "random uuid4 string that will be your key or smthn",
        "collectibleProductId": productid
    }

    while 1:
        data["idempotencyKey"] = str(uuid.uuid4())
        bought = r.post(f"https://apis.roblox.com/marketplace-sales/v1/item/{itemid}/purchase-item", json=data,
            headers={"x-csrf-token": x_token}, cookies={".ROBLOSECURITY": cookie})

        if bought.reason == "Too Many Requests":
            print("Fiz muitas tentativas...")
            time.sleep(0.5)
            continue

        try:
            bought = bought.json()
        except:
            print(bought.reason)
            print("Json decoder error whilst trying to buy item.")
            continue

        if not bought["purchased"]:
            print(f"Falha na compra tente novamente.. Info: {bought} - {data} Rafinha#7195|discord.gg/sorteios")
        else:
            print(f"Sucesso! Consegui comprar o item! Informação: {bought} - {data} Rafinha#7195|discord.gg/sorteios")

        info = r.post("https://catalog.roblox.com/v1/catalog/items/details",
                      json={"items": [{"itemType": "Asset", "id": int(limited)}]},
                      headers={"x-csrf-token": x_token}, cookies={".ROBLOSECURITY": cookie})
        try:
            left = info.json()["data"][0]["unitsAvailableForConsumption"]
        except:
            print(f"Erro ao obter o estoque. Informação: {info.text} - {info.reason}")
            left = 0

        if left == 0:
            print("Não fui rápido o suficiente para obter alguma cópia. Rafinha#7195|discord.gg/sorteios")
            return


# Get collectible and product id for all the limiteds.
Thread(target=get_x_token).start()

print("Rafinha#7195|discord.gg/sorteios")
while x_token == "":
    time.sleep(0.01)

# https://apis.roblox.com/marketplace-items/v1/items/details
# https://catalog.roblox.com/v1/catalog/items/details

cooldown = 60/(39/len(limiteds))-0.8
while 1:
    start = time.perf_counter()

    for limited in limiteds:
        try:
            info = r.post("https://catalog.roblox.com/v1/catalog/items/details",
                           json={"items": [{"itemType": "Asset", "id": int(limited)}]},
                           headers={"x-csrf-token": x_token}, cookies={".ROBLOSECURITY": cookie}).json()["data"][0]
        except KeyError:
            print("Fui bloqueado, espere um minuto.")
            time.sleep(60-int(datetime.datetime.now().second))
            continue

        if info.get("priceStatus", "") != "Off Sale" and info.get("collectibleItemId") is not None:
            productid = r.post("https://apis.roblox.com/marketplace-items/v1/items/details",
                   json={"itemIds": [info["collectibleItemId"]]},
                   headers={"x-csrf-token": x_token}, cookies={".ROBLOSECURITY": cookie})

            try:
                productid = productid.json()[0]["collectibleProductId"]
            except:
                print(f"Algo deu errado com o id dos items - {productid.text} - {productid.reason}")
                continue

            buy(info, info["collectibleItemId"], productid)

    taken = time.perf_counter()-start
    if taken < cooldown:
        time.sleep(cooldown-taken)

    os.system("cls")
    print("Verificação completa (TRADUZIDO POR Rafinha#7195|discord.gg/sorteios).\n"
          f"Tempo demorado: {round(time.perf_counter()-start, 3)}\n"
          f"Tempo Ideal: {round(cooldown, 3)}")