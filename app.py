import json
import pandas as pd
from sqlalchemy import create_engine

# connect sqlalchemy
engine = create_engine('sqlite://', echo=False)

# functions
def clear_data():
    
    with open('result-2021.json', encoding="utf8") as f:
        data = json.load(f)
        mylist = []
        for i in data['messages']:
            # convert data to list
            try:
                # parse data
                pos = i['text'].find('Horario')
                if pos:
                    split_data = i['text'][:pos].split(" ")
                else:
                    split_data = i['text'].split(" ")
                
                
                # load variables
                trade_id = split_data[3][:5]
                symbol = split_data[0]
                tdate = split_data[1]
                ttime = split_data[2]
                target = i['text'][:pos].count('ALVO ')
                closed = i['text'][:pos].count('ENCERRADA')
                split_data[2][:1]
                setup = split_data[4][:1]

                if 'USDT' in symbol:
                    currency = 'USDT'
                else:
                    currency = 'BTC' 

                # result
                result = ""
                if "WWW" in i['text']:
                    result = "WIN"
                if "LLL" in i['text']:
                    result = "LOSS"


                # remove trade_id from mylist if current trade_id achieved a new take_profit target 
                # if trade_id == "15756":
                #     print("****************")
                #     print('split_data', split_data)
                if target > 1:

                    for item in mylist:
                        if item['trade_id'] == trade_id and closed != 1:
                            mylist.remove(item)
                            mylist.remove(item) # fix bug not identified


            except:
                pass

            # covert format
            if result != "" and closed == 0:
                
                mylist.append({
                        'trade_id': trade_id,
                        'symbol': symbol, 
                        'day': tdate[:2],
                        'month': tdate[3:],
                        'time': ttime[:5],
                        'result': result,
                        'target': target,
                        'setup': setup,
                        'currency': currency
                    })
                        
        return mylist
    f.close()

def print_duplicates():
    df = pd.DataFrame(clear_data())
    df.to_sql('data', con=engine)
    
    duplicates  = engine.execute("SELECT trade_id FROM data GROUP BY trade_id HAVING COUNT(*) > 1 ").fetchall()[0] 
    return duplicates

def backtest():
    pass

def generate_new_json_file():
    with open('output-2021.json', 'w') as f:
        mylist = clear_data()
        json.dump(mylist, f)

def calculate_total_per_currency():
    
    df = pd.DataFrame(clear_data())
    df.to_sql('total_per_currency', con=engine)

    # select currency
    currencies = engine.execute("SELECT currency FROM total_per_currency GROUP BY currency").fetchall()
    for currency in currencies:
        
        print("#########################", currency, "#########################")
        months = engine.execute("SELECT month FROM total_per_currency WHERE currency = ? GROUP BY month", currency).fetchall()

        for month in months:
            print("## *********************** MONTH:", month[0], "***********************")
            
            # montlhy parameters 
            targets = engine.execute("SELECT target, result, count(*) FROM total_per_currency WHERE currency = ? and month = ? and target > 0 GROUP BY target, result", (currency[0], month[0],)).fetchall()
            stop_loss = engine.execute("SELECT count(*) FROM total_per_currency WHERE currency = ? and month = ? and target = 0", (currency[0], month[0],)).fetchall()[0][0]
            print('All levels StopLoss', stop_loss)
            for target in targets:
                
                higher_wins = engine.execute("SELECT count(*) FROM total_per_currency WHERE currency = ? and month = ? and target >= ? ", (currency[0], month[0], target[0] )).fetchall()[0][0]
                total_win = target[2]            

                # increment stop_loss with previous take_profit
                if target[0] > 1:
                    stop_loss += pv_target
                
                win_rate = (higher_wins / (stop_loss + higher_wins)) * 100
                print('## Take-profit: ', target[0], '|', 'total_win:', higher_wins, '|', 'stop_loss', stop_loss, '|', 'win_rate:', round(win_rate,2), '%' )
                pv_target = total_win

        print("###########################################################")
        print("")

calculate_total_per_currency()
