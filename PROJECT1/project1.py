# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from finta import TA
import yfinance as yf
import numpy as np
import pandas as pd
import yfinance as yf
from alpha_vantage.timeseries import TimeSeries
import datetime as dt
import copy
import matplotlib.pyplot as plt
import time
import json
from csv import writer
time.sleep(56)



# %%
import telepot
bot = telepot.Bot('1945858871:AAFQTbi7M0d5HAOSlrn6DL7IZ6CtaULc42M')
bot.getMe()



# %%
def candles(instrument):
        
    ohlc_intraday=pd.DataFrame()

    historicParam={
    "exchange": "NSE",
    "symboltoken": str(instrument),
    "interval": "FIVE_MINUTE",
    "fromdate": "2021-07-05 09:15", 
    "todate": "2021-08-14 15:25"
    }

    data=obj.getCandleData(historicParam)

    data=pd.DataFrame(data)["data"]
    open=[]
    close=[]
    high=[]
    low=[]
    volume=[]
    index=[]
    for i in range(len(data)):
        open.append(data[i][1])

    for i in range(len(data)):
        close.append(data[i][4])

    for i in range(len(data)):
        high.append(data[i][2])

    for i in range(len(data)):
        low.append(data[i][3])

    for i in range(len(data)):
        index.append(data[i][0])

    for i in range(len(data)):
        volume.append(data[i][5])


    ohlc_intraday["Index"]=np.array(index)
    ohlc_intraday["Open"]=np.array(open)
    ohlc_intraday["High"]=np.array(high)
    ohlc_intraday["Low"]=np.array(low)

    ohlc_intraday["Close"]=np.array(close)
    ohlc_intraday["Volume"]=np.array(volume)
    ohlc_intraday.set_index("Index",inplace=True)

    return ohlc_intraday


from smartapi import SmartConnect 
obj=SmartConnect(api_key="HXJag4Go")
data = obj.generateSession("G19398","9iiiiiiiiiii")
refreshToken= data['data']['refreshToken']
feedToken=obj.getfeedToken()
userProfile= obj.getProfile(refreshToken)


# %%
from py5paisa import FivePaisaClient

client = FivePaisaClient(email="jayeshpatel51999@gmail.com", passwd="jayesh@51999", dob="19791215")
client.login()


# %%

tame=time.time()
time.sleep(90)
kickers={'AARTIIND': 7, 'ABFRL': 30108, 'ACC': 22, 'ADANIENT': 25, 'ADANIPORTS': 15083, 'ALKEM': 11703, 'AMARAJABAT': 100, 'AMBUJACEM': 1270, 'APLLTD': 25328, 'APOLLOHOSP': 157, 'APOLLOTYRE': 163, 'ASHOKLEY': 212, 'ASIANPAINT': 236, 'AUBANK': 21238, 'AUROPHARMA': 275, 'AXISBANK': 5900, 'BAJAJ-AUTO': 16669, 'BAJAJFINSV': 16675, 'BAJFINANCE': 317, 'BALKRISIND': 335, 'BANDHANBNK': 2263, 'BANKBARODA': 4668, 'BATAINDIA': 371, 'BEL': 383, 'BERGEPAINT': 404, 'BHARATFORG': 422, 'BHARTIARTL': 10604, 'BHEL': 438, 'BIOCON': 11373, 'BOSCHLTD': 2181, 'BPCL': 526, 'BRITANNIA': 547, 'CADILAHC': 7929, 'CANBK': 10794, 'CHOLAFIN': 685, 'CIPLA': 694, 'COALINDIA': 20374, 'COFORGE': 11543, 'COLPAL': 15141, 'CONCOR': 4749, 'COROMANDEL': 739, 'CUB': 5701, 'CUMMINSIND': 1901, 'DABUR': 772, 'DEEPAKNTR': 19943, 'DIVISLAB': 10940, 'DLF': 14732, 'DRREDDY': 881, 'EICHERMOT': 910, 'ESCORTS': 958, 'EXIDEIND': 676, 'FEDERALBNK': 1023, 'GAIL': 4717, 'GLENMARK': 7406, 'GMRINFRA': 13528, 'GODREJCP': 10099, 'GODREJPROP': 17875, 'GRANULES': 11872, 'GRASIM': 1232, 'GUJGASLTD': 10599, 'HAVELLS': 9819, 'HCLTECH': 7229, 'HDFC': 1330, 'HDFCAMC': 4244, 'HDFCBANK': 1333, 'HDFCLIFE': 467, 'HEROMOTOCO': 1348, 'HINDALCO': 1363, 'HINDPETRO': 1406, 'HINDUNILVR': 1394, 'IBULHSGFIN': 30125, 'ICICIBANK': 4963, 'ICICIGI': 21770, 'ICICIPRULI': 18652, 'IDEA': 14366, 'IDFCFIRSTB': 11184, 'IGL': 11262, 'INDHOTEL': 1512, 'INDIGO': 11195, 'INDUSINDBK': 5258, 'INDUSTOWER': 29135, 'INFY': 1594, 'IOC': 1624, 'IRCTC': 13611, 'ITC': 1660, 'JINDALSTEL': 6733, 'JSWSTEEL': 11723, 'JUBLFOOD': 18096, 'KOTAKBANK': 1922, 'LALPATHLAB':11654, 'LICHSGFIN': 1997, 'LT': 11483, 'LTI': 17818, 'LTTS': 18564, 'LUPIN': 10440,  'MANAPPURAM': 19061, 'MARICO': 4067, 'MARUTI': 10999, 'MCDOWELL-N': 10447, 'METROPOLIS': 9581, 'MFSL': 2142, 'MGL': 17534, 'MINDTREE': 14356, 'MOTHERSUMI': 4204, 'MPHASIS': 4503, 'MRF': 2277, 'MUTHOOTFIN': 23650, 'NAM-INDIA': 357, 'NATIONALUM': 6364, 'NAUKRI': 13751, 'NAVINFLUOR': 14672, 'NESTLEIND': 17963, 'NMDC': 15332, 'NTPC': 11630, 'ONGC': 2475, 'PAGEIND': 14413, 'PEL': 2412, 'PETRONET': 11351, 'PFC': 14299, 'PFIZER': 2643, 'PIDILITIND': 2664, 'PIIND': 24184, 'PNB': 10666, 'POWERGRID': 14977, 'PVR': 13147, 'RAMCOCEM': 2043, 'RBLBANK': 18391, 'RECLTD': 15355, 'RELIANCE': 2885, 'SAIL': 2963, 'SBILIFE': 21808, 'SBIN': 3045, 'SHREECEM': 3103, 'SIEMENS': 3150, 'SRF': 3273, 'SRTRANSFIN': 4306, 'SUNPHARMA': 3351, 'SUNTV': 13404, 'TATACHEM': 3405, 'TATACONSUM': 3432, 'TATAMOTORS': 3456, 'TATAPOWER': 3426, 'TATASTEEL': 3499, 'TCS': 11536, 'TECHM': 13538, 'TITAN': 3506, 'TORNTPHARM': 3518, 'TORNTPOWER': 13786, 'TRENT': 1964, 'TVSMOTOR': 8479, 'UBL': 16713, 'ULTRACEMCO': 11532, 'UPL': 11287, 'VEDL': 3063, 'VOLTAS': 3718, 'WIPRO': 3787, 'ZEEL': 3812}
lickers=[]

# %%
investment=4000
risk=50   
portfolio=30000

prise=0
ltp=0

# selection()
# print(jikers)
# print("passthrough at ",time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

ohlcv_database=pd.DataFrame()

order=[]
order1=[]
price=0

position=""
position=""




# %%
def selection1():
    global lickers,kickers
    for ticker in kickers:
        try:
            print('analyzing for:', ticker)
            print("passthrough at ",time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            df=candles(kickers[ticker])
        
            req_list_=[{"Exch":"N","ExchType":"C","Symbol":ticker}]
                
            data=client.fetch_market_feed(req_list_)
            price=float(data['Data'][0]['PClose'])
                
            


            print("\n \n analyzzing for ",ticker)
            print(price)
            time.sleep(0.25)
            try:
                if df['Close'].iloc[-2]>df['Open'].iloc[-2] and ((df['Open'].iloc[-2]-price)/price)*100>.5:
                    lickers.append(ticker)

            except Exception as e:
                print(e)
                bot.sendMessage(1060689126, 'some error occurred')
               
              

        except Exception as e:
            print(e)
            bot.sendMessage(1060689126, 'some error occurred')
           


# %%


selection1()
try:
    print(lickers)
    bot.sendMessage(1060689126, lickers)

except:
    print('couldn,t send message')



# %%
high={}
low=0
times=99999999999999999
high1=1000000000

for ticker in lickers:
    high[ticker]=1000000000


# %%



# %%
yickers=[]
value={}
for ticker in yickers:
    value[ticker]=0

def selection2():
    global lickers,yickers,high,kickers,value
    for ticker in lickers:
        print('analyzing for: ',ticker)
        df=candles(kickers[ticker])
        time.sleep(.25)
        try:
            if df['Close'].iloc[-1]>df['High'].iloc[-2]:
                yickers.append(ticker)
                value[ticker]=abs((df['Close'].iloc[-1]-df['Open'].iloc[-2])/df['Open'].iloc[-2])

                high[ticker]=df['High'].iloc[-1]

        except Exception as e:
            print(e)
            bot.sendMessage(1060689126, 'some error occurred')

      




# %%
time.sleep(abs(300-(time.time()-tame)))

time.sleep(10)
selection2()


# %%
try:
    stock='hi'
    max=0
    for ticker in yickers:
        if value[ticker]>max:
            max=value[ticker]
            stock=ticker


    high=high[stock]
    low=0
except:
    print("no stock selected")

bot.sendMessage(1060689126, stock)


# %%
def market_order(instrument,investment,risk):
    global price,order,order1,start_time,stock,order1,ltp,kickers


    price=float(ltp)
    units=int(investment/price)
   
    if units>0:
        try:
            orderparams = {
                "variety": "NORMAL",
                "tradingsymbol": str(instrument)+'-EQ',
                "symboltoken": str(kickers[instrument]),
                "transactiontype": "BUY",
                "exchange": "NSE",
                "ordertype": "MARKET",
                "producttype": "INTRADAY",
                "duration": "DAY",
            
                

                "quantity": str(abs(units))
                }
            orderId=obj.placeOrder(orderparams)
            print("The order id is: {}".format(orderId))
            bot.sendMessage(1060689126, 'long position generatted')
        except Exception as e:
            print("Order placement failed: {}".format(e.message))
      



    if units<0:
        try:
            orderparams = {
                "variety": "NORMAL",
                "tradingsymbol": str(instrument)+'-EQ',
                "symboltoken": str(kickers[instrument]),
                "transactiontype": "SELL",
                "exchange": "NSE",
                "ordertype": "MARKET",
                "producttype": "INTRADAY",
                "duration": "DAY",
    
              
                "quantity": str(abs(units))
                }
            orderId=obj.placeOrder(orderparams)
            print("The order id is: {}".format(orderId))
            bot.sendMessage(1060689126, 'short position generatted')
        except Exception as e:
            print("Order placement failed: {}".format(e.message))
            bot.sendMessage(1060689126, 'could not place the order .... some error ocurred')    
        




    



def market_order1(instrument,investment,risk):
    global price,position,order,ltp,stock

    price=float(ltp)
    units=int(investment/price)



    if units>0:
        try:
            orderparams = {
                "variety": "NORMAL",
                "tradingsymbol": str(instrument)+'-EQ',
                "symboltoken": str(kickers[instrument]),
                "transactiontype": "BUY",
                "exchange": "NSE",
                "ordertype": "MARKET",
                "producttype": "INTRADAY",
                "duration": "DAY",
  

                "quantity": str(abs(units))
                }
            orderId=obj.placeOrder(orderparams)
            print("The order id is: {}".format(orderId))
            bot.sendMessage(1060689126, 'short position squared off')
        except Exception as e:
            print("Order placement failed: {}".format(e.message))
            bot.sendMessage(1060689126, 'could not place the order ..... some error ocurred')   
            





    if units<0:
        try:
            orderparams = {
                "variety": "NORMAL",
                "tradingsymbol": str(instrument)+'-EQ',
                "symboltoken": str(kickers[instrument]),
                "transactiontype": "SELL",
                "exchange": "NSE",
                "ordertype": "MARKET",
                "producttype": "INTRADAY",
                "duration": "DAY",

                
                "quantity": str(abs(units))
                }
            orderId=obj.placeOrder(orderparams)
            print("The order id is: {}".format(orderId))
            bot.sendMessage(1060689126, 'long position squarred off')
        except Exception as e:
            print("Order placement failed: {}".format(e.message))
            bot.sendMessage(1060689126, 'could not place the order .... some error ocurred')   



# %%
def trade_signal(instrument,l_s):
    
    global ltp,position,high,low,high1,stock,times,price



    signal=""
    if l_s=="":
    
        if ltp>high:
            signal="buy"
            times=time.time()
            position='long'

                        
      

    elif l_s=="long":
        if ltp<=low-low*.004:
            
            signal="sell and squareoffsell"
            times=time.time()
            position='short'
           
                    
    elif l_s=="short":
        if high1<price+price*.004:
            if ltp>=price+.004*price:
                signal="squareoffbuy"
                position=""

        elif high1>price+price*.004:
            if ltp>=high1:
                signal='squareoffbuy'
                position=""
            


    return signal    


# %%
def main():
    global investment,risk,ltp,position,prise,high,start_time,low,high1,kickers,stock,times
    



    df=candles(kickers[stock])
    
    timedate=time.localtime(times)
    
    t=timedate.tm_min%5
    tr=timedate.tm_min-t
    trr=timedate.tm_hour
    time.sleep(.25)
    if position=='long' and str(trr)+':'+str(tr) in df.index[-2]:
        
        
        
        low=df['Low'].iloc[-2]

    if position=='short' and str(trr)+':'+str(tr) in df.index[-2]:

    
        high1=df['High'].iloc[-2]
        



    req_list_=[{"Exch":"N","ExchType":"C","Symbol":stock}]
        
    data=client.fetch_market_feed(req_list_)
    ltp=float(data['Data'][0]['LastRate'])
        



    print("\n \n analyzzing for ",stock)
    print(ltp)


    l_s= position
    print(l_s)
    signal=trade_signal(stock,l_s)
    if 'buy' in signal:
        if time.time()<=start_time+5700:
    

            market_order(stock,investment,risk)
            print("New long position initiated for ",stock)

    if 'sell' in signal:
        market_order(stock,-1*investment,risk)
        print("New short position initiated for ", stock)

    if 'squareoffbuy' in signal:
        market_order1(stock,investment,risk)
      

    if 'squareoffsell' in signal:
        market_order1(stock,-1*investment,risk)






# %%

start_time=time.time()

timeout=start_time+60*60*5+45*60
times=time.time()

while time.time()<=timeout:
    try:
  
        main()
        print("passthrough at ",time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
   

    except Exception as e:
        print(e)
        
        



# %%




req_list_=[{"Exch":"N","ExchType":"C","Symbol":stock}]
    
data=client.fetch_market_feed(req_list_)
ltp=float(data['Data'][0]['LastRate'])

print("\n \n analyzzing for ",stock)
print(ltp)
if position=="long":
    market_order1(stock,-1*investment,risk)

if position=="short":
    market_order1(stock,investment,risk)

