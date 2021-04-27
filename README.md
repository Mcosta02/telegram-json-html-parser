Telegram JSON Parser
------------------------------------------

The idea of this script is to parse a JSON file generated from "BitNada-Results" telegram group with trading system results. 
The main idea is to extract relevant data to analyse whether the setup is profitable or not.

The script offers two options of output:
  - a new json file formatted with clear data from the trading system results (output-2021.json file will be generated on the project root)
  - a reported with sorted by two groups: BTC or USDT currenct trading, monthly, take-profit levels, and so on.(see an example at end of this file)


Main Functions:
---------------
clear_data -> Function will read the JSON file and load the following variables:

  - symbol
  - signal date
  - signal time
  - result (WIN or LOSS)
  - targets achieved
  - setups
  - % win/rate
  
generate_file -> Function will generate a new formatted JSON file

Technologies:
-------------
- Python

Instalation:
------------

1. git clone https://github.com/Mcosta02/telegram-json-html-parser.git
2. pip install -r requirements.txt
3. py app.py (to generate the report)

* before running app.py you have to upload the JSON file from "BitNada-Results" telegram group on the root directory named "result-2021.json". 
The default installation already contains the result file from 01-01-2021 to publication date.


Report:
-------
![image](https://user-images.githubusercontent.com/22096119/115947939-5f2f6980-a50e-11eb-87de-bc069a180f95.png)
