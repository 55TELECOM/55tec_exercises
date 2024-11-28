
import math
import os
import random
import re
import sys

def aVeryBigSum(ar):
    return sum(ar)

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = './55tec_exercises/algorithms/exec_1/resposta_jhoey/resultado_exec1_jhoey.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)
    print(result)

    fptr.write(str(result) + '\n')

    fptr.close()
