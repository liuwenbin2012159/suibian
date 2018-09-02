#双线搬砖
#1.获取HuoBi上ADA价格，此为死循环
#2.获取OKCoin上ADA价格，此为死循环
#3.计算是否盈利
#4.先对OKCoin进行交易，随后对HuoBi进行交易

from websocket import create_connection
import gzip
import time

def getAdaPriceOfHuoBi(ws):

    # 请求 KLine 数据
    # tradeStr="""{"req": "market.ethusdt.kline.1min","id": "id10", "from": 1513391453, "to": 1513392453}"""
    print("start to gain ada's price in HuoBi")
    # 请求 ada 行情 数据
    tradeStr="""{"req": "market.ethusdt.depth.step5", "id": "id10"}"""
    ws.send(tradeStr)
    compressData = ws.recv()
    result = gzip.decompress(compressData).decode('utf-8')
    ts = result[8:21]
    pong = '{"pong":' + ts + '}'
    ws.send(pong)
    print("result == " + result)

# def heartBeatWebsocket():
#     while (1):
#         compressData = ws.recv()
#         result = gzip.decompress(compressData).decode('utf-8')
#         print("result == "+result)
#         if result[:7] == '{"ping"':
#             ts = result[8:21]
#             pong = '{"pong":' + ts + '}'
#             ws.send(pong)



if __name__ == '__main__':
    try:
        print("hello liuwenbin")
        ws = create_connection("wss://api.huobi.pro/ws")
        print("hello jiejie")
    except :
        print('connect ws error,retry...')

    tradeStr = """{"sub": "market.ethusdt.depth.step5", "id": "id10"}"""
    # tradeStr = """{"sub":"market.ethusdt.detail","id":"id12"}"""
    ws.send(tradeStr)
    while(True):
        compressData=ws.recv()
        result=gzip.decompress(compressData).decode('utf-8')
        print("RESULT=="+result)
        ts=result[8:21]
        pong='{"ping":'+ts+'}'
        ws.send(pong)


        # 订阅 KLine 数据
    # tradeStr="""{"sub": "market.ethusdt.kline.1min","id": "id10"}"""



    #订阅 Market Depth 数据
    # tradeStr="""{"sub": "market.ethusdt.depth.step5", "id": "id10"}"""

    #请求 Market Depth 数据
    # tradeStr="""{"req": "market.ethusdt.depth.step5", "id": "id10"}"""

    #订阅 Trade Detail 数据
    # tradeStr="""{"sub": "market.ethusdt.trade.detail", "id": "id10"}"""

    #请求 Trade Detail 数据
    # tradeStr="""{"req": "market.ethusdt.trade.detail", "id": "id10"}"""

    #请求 Market Detail 数据
    # tradeStr="""{"req": "market.ethusdt.detail", "id": "id12"}"""

    # oo = ws.send(tradeStr)
    # print("oo=="+str(oo))

