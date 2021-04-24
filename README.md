Telegram JSON Parser
------------------------------------------

The idea of this script is to parse a JSON file generated from "BitNada-Results" telegram group with trading system results. The main idea is to extract relevant data to analyse whether the setup is profitable or not

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



Report:
-------
The following report will be printed

######################### ('BTC',) #########################
## *********************** MONTH: 01 ***********************
All levels StopLoss 101
## Take-profit:  1 | total_win: 41 | stop_loss 101 | win_rate: 28.87 %
## Take-profit:  2 | total_win: 20 | stop_loss 142 | win_rate: 12.35 %
## Take-profit:  3 | total_win: 20 | stop_loss 162 | win_rate: 10.99 %
## Take-profit:  4 | total_win: 18 | stop_loss 182 | win_rate: 9.0 %
## Take-profit:  5 | total_win: 23 | stop_loss 200 | win_rate: 10.31 %
## Take-profit:  6 | total_win: 36 | stop_loss 223 | win_rate: 13.9 %
###########################################################

######################### ('USDT',) #########################
## *********************** MONTH: 01 ***********************
All levels StopLoss 49
## Take-profit:  1 | total_win: 33 | stop_loss 49 | win_rate: 40.24 %
## Take-profit:  2 | total_win: 19 | stop_loss 82 | win_rate: 18.81 %
## Take-profit:  3 | total_win: 25 | stop_loss 101 | win_rate: 19.84 %
## Take-profit:  4 | total_win: 12 | stop_loss 126 | win_rate: 8.7 %
## Take-profit:  5 | total_win: 13 | stop_loss 138 | win_rate: 8.61 %
## Take-profit:  6 | total_win: 15 | stop_loss 151 | win_rate: 9.04 %
###########################################################
