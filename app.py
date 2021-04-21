import json
import codecs
# Opening JSON file and clear DATA.

def clear_data():
    
    with open('result-2021.json', encoding="utf8") as f:
        data = json.load(f)
        mylist = []
        for i in data['messages']:

            # convert data to list
            try:
                pos = i['text'].find('Horario')
                split_data = i['text'][:pos].split(" ")

                # load variables
                symbol = split_data[0]
                tdate = split_data[1]
                ttime = split_data[2]
                target = i['text'][:pos].count('ALVO ')
                split_data[2][:1]
                setup = split_data[4][:1]

                # result
                result = ""
                if "WWW" in i['text']:
                    result = "WIN"
                if "LLL" in i['text']:
                    result = "LOSS"

            except:
                pass

            # covert format
            if result != 0:

                mylist.append({
                        'symbol': symbol, 
                        'day': tdate[:2],
                        'month': tdate[3:],
                        'time': ttime[:5],
                        'result': result,
                        'target': target,
                        'setup': setup
                    })
                        
        return mylist
    f.close()

def generate_file():
    with open('output-2021.json', 'w') as f:
        mylist = clear_data()
        json.dump(mylist, f)

generate_file()