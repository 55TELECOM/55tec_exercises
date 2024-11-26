
import math
import os
import random
import re
import sys
from datetime import datetime

def timeConversion(s):
    try:
        return datetime.strptime(s, '%I:%M:%S%p').strftime('%H:%M:%S')
    except ValueError:
        print('Insira o formato correto de dados: HH:MM:SS(AM/PM)')
        
if __name__ == '__main__':

    os.environ['OUTPUT_PATH'] = './resultado_exec3_jhoey.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')    

    s = input().replace(' ', '')

    result = timeConversion(s) 
    if result != None:
        print(f"O horário militar de {s} é {result}")
    
    fptr.write(result + '\n')

    fptr.close()
