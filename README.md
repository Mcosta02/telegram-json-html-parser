Telegram JSON and HTML Parser
------------------------------------------

The idea of this script is to parse a JSON or HTML file generated from "BitNada-Results" telegram group with trading system results. The main idea is to extract fundamental 
information in order to analyse whether the setups are profitable or not

Main Functions:
---------
clear_data -> Function will read the JSON file and load the following variables:

  - symbol
  - signal date
  - signal time
  - result (WIN or LOSS)
  - targets achieved
  - setups
  
generate_file -> Function will generate a new formatted JSON file


Technologies:
---------
- Python
