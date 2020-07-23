from yahoo_fin.stock_info import get_day_gainers, get_live_price, get_day_losers, get_top_crypto, get_data, get_day_most_active
from keys import client, sending, numbers_to_message
import time
from datetime import date, datetime
from twilio.rest import Client
import schedule


"Fuctions for each section of the message"


### Indicies Section ###

def spy_change():
    spy=get_data('spy', interval='1d')
    tick = spy['ticker']
    live_spy=get_live_price('spy')
    closing_price_spy=spy['close']
    spy_change=(live_spy - closing_price_spy[-2])/live_spy

    if spy_change >=0:
        result='up'
    else:
        result='down'
    return(f"{tick[0]} is trading at {'${:.2f}'.format(live_spy)}, {result} {'{:.2%}'.format(spy_change)}.")
    

def qqq_change():
    qqq=get_data('qqq', interval='1d')
    tick = qqq['ticker']
    live_qqq=get_live_price('qqq')
    closing_price_qqq=qqq['close']
    qqq_change=(live_qqq - closing_price_qqq[-2])/live_qqq
    
    if qqq_change >=0:
        result='up'
    else:
        result='down'
    return(f"{tick[0]} is trading at {'${:.2f}'.format(live_qqq)}, {result} {'{:.2%}'.format(qqq_change)}.")

def rut_change():
    rut=get_data('^rut', interval='1d')
    tick = rut['ticker']
    live_rut=get_live_price('^rut')
    closing_price_rut=rut['close']
    rut_change=(live_rut - closing_price_rut[-2])/live_rut
    
    if rut_change >=0:
        result='up'
    else:
        result='down'
    return(f"{tick[0]} is trading at {'${:,.2f}'.format(live_rut)}, {result} {'{:.2%}'.format(rut_change)}.")

### Metals ###

def gold_price():
    gold_live = get_live_price('gc=f')
    return str("Gold futures are trading at " '${:,.2f}'.format(gold_live)+".")

def silver_price():
    silver_live = get_live_price('si=f')
    return str("Silver futures are trading at " '${:.2f}'.format(silver_live)+".")
    

def dxy_change():
    dxy=get_data('dx-y.nyb', interval='1d')
    tick = dxy['ticker']
    live_dxy = get_live_price('dx-y.nyb')
    closing_price_dxy=dxy['close']
    open_price_dxy=dxy['open']
    dxy_change=(closing_price_dxy[-1] - open_price_dxy[-1])/closing_price_dxy[-1]
    
    if dxy_change >=0:
        result='up'
    else:
        result='down'
    return(f"{tick[0]} is trading at {'${:.2f}'.format(live_dxy)}, {result} {'{:.2%}'.format(dxy_change)}.")
### Crypto Section ###

def bitcoin_change():
    crypt=get_top_crypto()
    bitcoin=crypt['Name']
    bitcoin_price=crypt['Price (Intraday)']
    bitcoin_change=crypt['% Change']
    
    if bitcoin_change[0] >=0:
        result='up'
    else:
        result='down'
    return(f"{bitcoin[0]} is trading at {'${:,.2f}'.format(bitcoin_price[0])}, {result} {'{:.2%}'.format(bitcoin_change[0]/100)}.")


def ethereum_change():
    crypt=get_top_crypto()
    ethereum=crypt['Name']
    ethereum_price=crypt['Price (Intraday)']
    ethereum_change=crypt['% Change']
    
    if ethereum_change[0] >=0:
        result='up'
    else:
        result='down'
    return(f"{ethereum[1]} is trading at {'${:,.2f}'.format(ethereum_price[1])}, {result} {'{:.2%}'.format(ethereum_change[1]/100)}.")

### Most Active ###

def most_active():
    active=get_day_most_active()
    most_active1=active['Symbol']
    price_ma1=active['Price (Intraday)']
    change_ma1=active['% Change']
    ma1_tick=(most_active1[0])
    ma1_price=('${:,.2f}'.format(price_ma1[0]))
    ma1_change=('{:.2%}'.format(change_ma1[0]/100))
    
    most_active2=active['Symbol']
    price_ma2=active['Price (Intraday)']
    change_ma2=active['% Change']
    ma2_tick=(most_active2[1])
    ma2_price=('${:,.2f}'.format(price_ma2[1]))
    ma2_change=('{:.2%}'.format(change_ma2[1]/100))
    
    most_active3=active['Symbol']
    price_ma3=active['Price (Intraday)']
    change_ma3=active['% Change']
    ma3_tick=(most_active3[2])
    ma3_price=('${:,.2f}'.format(price_ma3[2]))
    ma3_change=('{:.2%}'.format(change_ma3[2]/100))
    
    tickers=(f"The most active stocks are {ma1_tick}, {ma2_tick}, and {ma3_tick}.\n")
    prices=(f"Their prices are {ma1_price}, {ma2_price}, and {ma3_price}.\n")
    change=(f"They moved by {ma1_change}, {ma2_change}, and {ma3_change}.")
    return(tickers+prices+change)

### Top 3 Gainers ###

def gainer():
    gainers=get_day_gainers()
    day_gainer1=gainers['Symbol']
    price_day_gainer1=gainers['Price (Intraday)']
    change_day_gainer1=gainers['% Change']
    dg1_tick=(day_gainer1[0])
    dg1_price=('${:,.2f}'.format((price_day_gainer1[0])))
    dg1_change=('{:.2%}'.format(change_day_gainer1[0]))

    day_gainer2=gainers['Symbol']
    price_day_gainer2=gainers['Price (Intraday)']
    change_day_gainer2=gainers['% Change']
    dg2_tick=(day_gainer2[1])
    dg2_price=('${:,.2f}'.format(price_day_gainer2[1]))
    dg2_change=('{:.2%}'.format(change_day_gainer2[1]))

    day_gainer3=gainers['Symbol']
    price_day_gainer3=gainers['Price (Intraday)']
    change_day_gainer3=gainers['% Change']
    dg3_tick=(day_gainer3[2])
    dg3_price=('${:,.2f}'.format(price_day_gainer3[2]))
    dg3_change=('{:.2%}'.format(change_day_gainer3[2]))

    tickers=(f"The top gainers are {dg1_tick}, {dg2_tick}, and {dg3_tick}.\n")
    prices=(f"Their prices are currently {dg1_price}, {dg2_price}, and {dg3_price}.\n")
    change=(f"Their prices rose by {dg1_change}, {dg2_change}, and {dg3_change}.")
    print(tickers+prices+change)


### Top 3 Losers ###
def loser():
    losers=get_day_losers()
    day_loser1=losers['Symbol']
    price_day_loser1=losers['Price (Intraday)']
    change_day_loser1=losers['% Change']
    dl1_tick=(day_loser1[0])
    dl1_price=('${:,.2f}'.format(price_day_loser1[0]))
    dl1_change=('{:.2%}'.format(change_day_loser1[0]/100))

    day_loser2=losers['Symbol']
    price_day_loser2=losers['Price (Intraday)']
    change_day_loser2=losers['% Change']
    dl2_tick=(day_loser2[1])
    dl2_price=('${:,.2f}'.format(price_day_loser2[1]))
    dl2_change=('{:.2%}'.format(change_day_loser2[1]/100))

    day_loser3=losers['Symbol']
    price_day_loser3=losers['Price (Intraday)']
    change_day_loser3=losers['% Change']
    dl3_tick=(day_loser3[2])
    dl3_price=('${:,.2f}'.format(price_day_loser3[2]))
    dl3_change=('{:.2%}'.format(change_day_loser3[2]/100))

    tickers=(f"The top losers are {dl1_tick}, {dl2_tick}, and {dl3_tick}.\n")
    prices=(f"Their prices are currently {dl1_price}, {dl2_price}, and {dl3_price}.\n")
    change=(f"Their prices dropped by {dl1_change}, {dl2_change}, and {dl3_change}.")
    return(tickers+prices+change)

### Message ###

def message():
    
    for n in numbers_to_message:
        client.messages.create(
        to=n,
        from_=sending, 
        body=f'{spy_change()}\n{qqq_change()}\n{rut_change()}\n{gold_price()}\n{silver_price()}\n{dxy_change()}\n{bitcoin_change()}\n{ethereum_change()}\n{most_active()}\n{loser()}'
        )
    # \n{gainer()}
    time=datetime.now()
    print(f"message sent at {time}")


## Scheduling ###

schedule.every().monday.at("16:05").do(message)
schedule.every().tuesday.at("16:05").do(message)
schedule.every().wednesday.at("16:05").do(message)
schedule.every().thursday.at("16:05").do(message)
schedule.every().friday.at("16:05").do(message)


while True:
    schedule.run_pending()
    time.sleep(1)
