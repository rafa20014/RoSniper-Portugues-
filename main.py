import requests as r #line:1:import requests as r
from threading import Thread #line:2:from threading import Thread
import os #line:3:import os
import uuid #line:4:import uuid
import time #line:5:import time
import datetime #line:6:import datetime
with open ("limiteds.txt","r")as f :#line:8:with open("limiteds.txt", "r") as f:
    limiteds =f .read ().replace (" ","").split (",")#line:9:limiteds = f.read().replace(" ", "").split(",")
with open ("cookie.txt","r")as f :#line:11:with open("cookie.txt", "r") as f:
    cookie =f .read ()#line:12:cookie = f.read()
user_id =r .get ("https://users.roblox.com/v1/users/authenticated",cookies ={".ROBLOSECURITY":cookie }).json ()["id"]#line:15:user_id = r.get("https://users.roblox.com/v1/users/authenticated", cookies={".ROBLOSECURITY": cookie}).json()["id"]
x_token =""#line:16:x_token = ""
def get_x_token ():#line:17:def get_x_token():
    global x_token #line:18:global x_token
    x_token =r .post ("https://auth.roblox.com/v2/logout",cookies ={".ROBLOSECURITY":cookie }).headers ["x-csrf-token"]#line:21:cookies={".ROBLOSECURITY": cookie}).headers["x-csrf-token"]
    print ("Entrei na conta.")#line:22:print("Entrei na conta.")
    while 1 :#line:24:while 1:
        x_token =r .post ("https://auth.roblox.com/v2/logout",cookies ={".ROBLOSECURITY":cookie }).headers ["x-csrf-token"]#line:27:cookies={".ROBLOSECURITY": cookie}).headers["x-csrf-token"]
        time .sleep (248 )#line:28:time.sleep(248)
def buy (O0O0OOO0OO0O0OO00 ,OOO00OOO000OO00OO ,O0000OOOO0O0O00O0 ):#line:31:def buy(json, itemid, productid):
    print ("Comprando o item sem parar...")#line:32:print("Comprando o item sem parar...")
    OOOO00OOOOOOO0O00 ={"collectibleItemId":OOO00OOO000OO00OO ,"expectedCurrency":1 ,"expectedPrice":0 ,"expectedPurchaserId":user_id ,"expectedPurchaserType":"User","expectedSellerId":O0O0OOO0OO0O0OO00 ["creatorTargetId"],"expectedSellerType":"User","idempotencyKey":"random uuid4 string that will be your key or smthn","collectibleProductId":O0000OOOO0O0O00O0 }#line:44:}
    while 1 :#line:46:while 1:
        OOOO00OOOOOOO0O00 ["idempotencyKey"]=str (uuid .uuid4 ())#line:47:data["idempotencyKey"] = str(uuid.uuid4())
        OOO00OO0O00O000O0 =r .post (f"https://apis.roblox.com/marketplace-sales/v1/item/{OOO00OOO000OO00OO}/purchase-item",json =OOOO00OOOOOOO0O00 ,headers ={"x-csrf-token":x_token },cookies ={".ROBLOSECURITY":cookie })#line:49:headers={"x-csrf-token": x_token}, cookies={".ROBLOSECURITY": cookie})
        if OOO00OO0O00O000O0 .reason =="Too Many Requests":#line:51:if bought.reason == "Too Many Requests":
            print ("Fiz muitas tentativas...")#line:52:print("Fiz muitas tentativas...")
            time .sleep (0.5 )#line:53:time.sleep(0.5)
            continue #line:54:continue
        try :#line:56:try:
            OOO00OO0O00O000O0 =OOO00OO0O00O000O0 .json ()#line:57:bought = bought.json()
        except :#line:58:except:
            print (OOO00OO0O00O000O0 .reason )#line:59:print(bought.reason)
            print ("Json decoder error whilst trying to buy item.")#line:60:print("Json decoder error whilst trying to buy item.")
            continue #line:61:continue
        if not OOO00OO0O00O000O0 ["purchased"]:#line:63:if not bought["purchased"]:
            print (f"Falha na compra tente novamente.. Info: {OOO00OO0O00O000O0} - {OOOO00OOOOOOO0O00} Rafinha#7195|discord.gg/sorteios")#line:64:print(f"Falha na compra tente novamente.. Info: {bought} - {data} Rafinha#7195|discord.gg/sorteios")
        else :#line:65:else:
            print (f"Sucesso! Consegui comprar o item! Informação: {OOO00OO0O00O000O0} - {OOOO00OOOOOOO0O00} Rafinha#7195|discord.gg/sorteios")#line:66:print(f"Sucesso! Consegui comprar o item! Informação: {bought} - {data} Rafinha#7195|discord.gg/sorteios")
        OOO00O00O0O0O0O0O =r .post ("https://catalog.roblox.com/v1/catalog/items/details",json ={"items":[{"itemType":"Asset","id":int (limited )}]},headers ={"x-csrf-token":x_token },cookies ={".ROBLOSECURITY":cookie })#line:70:headers={"x-csrf-token": x_token}, cookies={".ROBLOSECURITY": cookie})
        try :#line:71:try:
            OO0000OO0000O000O =OOO00O00O0O0O0O0O .json ()["data"][0 ]["unitsAvailableForConsumption"]#line:72:left = info.json()["data"][0]["unitsAvailableForConsumption"]
        except :#line:73:except:
            print (f"Erro ao obter o estoque. Informação: {OOO00O00O0O0O0O0O.text} - {OOO00O00O0O0O0O0O.reason}")#line:74:print(f"Erro ao obter o estoque. Informação: {info.text} - {info.reason}")
            OO0000OO0000O000O =0 #line:75:left = 0
        if OO0000OO0000O000O ==0 :#line:77:if left == 0:
            print ("Não fui rápido o suficiente para obter alguma cópia. Rafinha#7195|discord.gg/sorteios")#line:78:print("Não fui rápido o suficiente para obter alguma cópia. Rafinha#7195|discord.gg/sorteios")
            return #line:79:return
Thread (target =get_x_token ).start ()#line:83:Thread(target=get_x_token).start()
print ("Rafinha#7195|discord.gg/sorteios")#line:85:print("Rafinha#7195|discord.gg/sorteios")
while x_token =="":#line:86:while x_token == "":
    time .sleep (0.01 )#line:87:time.sleep(0.01)
cooldown =60 /(39 /len (limiteds ))-0.8 #line:92:cooldown = 60/(39/len(limiteds))-0.8
while 1 :#line:93:while 1:
    start =time .perf_counter ()#line:94:start = time.perf_counter()
    for limited in limiteds :#line:96:for limited in limiteds:
        try :#line:97:try:
            info =r .post ("https://catalog.roblox.com/v1/catalog/items/details",json ={"items":[{"itemType":"Asset","id":int (limited )}]},headers ={"x-csrf-token":x_token },cookies ={".ROBLOSECURITY":cookie }).json ()["data"][0 ]#line:100:headers={"x-csrf-token": x_token}, cookies={".ROBLOSECURITY": cookie}).json()["data"][0]
        except KeyError :#line:101:except KeyError:
            print ("Fui bloqueado, espere um minuto.")#line:102:print("Fui bloqueado, espere um minuto.")
            time .sleep (60 -int (datetime .datetime .now ().second ))#line:103:time.sleep(60-int(datetime.datetime.now().second))
            continue #line:104:continue
        if info .get ("priceStatus","")!="Off Sale"and info .get ("collectibleItemId")is not None :#line:106:if info.get("priceStatus", "") != "Off Sale" and info.get("collectibleItemId") is not None:
            productid =r .post ("https://apis.roblox.com/marketplace-items/v1/items/details",json ={"itemIds":[info ["collectibleItemId"]]},headers ={"x-csrf-token":x_token },cookies ={".ROBLOSECURITY":cookie })#line:109:headers={"x-csrf-token": x_token}, cookies={".ROBLOSECURITY": cookie})
            try :#line:111:try:
                productid =productid .json ()[0 ]["collectibleProductId"]#line:112:productid = productid.json()[0]["collectibleProductId"]
            except :#line:113:except:
                print (f"Algo deu errado com o id dos items - {productid.text} - {productid.reason}")#line:114:print(f"Algo deu errado com o id dos items - {productid.text} - {productid.reason}")
                continue #line:115:continue
            buy (info ,info ["collectibleItemId"],productid )#line:117:buy(info, info["collectibleItemId"], productid)
    taken =time .perf_counter ()-start #line:119:taken = time.perf_counter()-start
    if taken <cooldown :#line:120:if taken < cooldown:
        time .sleep (cooldown -taken )#line:121:time.sleep(cooldown-taken)
    os .system ("cls")#line:123:os.system("cls")
    print ("Verificação completa (TRADUZIDO POR Rafinha#7195|discord.gg/sorteios).\n" f"Tempo demorado: {round(time.perf_counter()-start, 3)}\n" f"Tempo Ideal: {round(cooldown, 3)}")
