'''
Simple Reactive Agent - Gas Controller System
'''

import time
from random import randint

agent = "noGas"

noGasLeak = 0
lowGasLeak = 1
largeGasLeak = 2

environment = [
                            [1, 2, 0, 0, 2],
                            [0, 2, 1, 0, 2],
                            [0, 1, 2, 0, 0]
                                                  ]

######
### Contar números repetidos:
rep = 0
for i in range (0, len(environment) - 1) :
    if (environment [ i ] == environment [ i + 1 ]):
        rep += 1
        if (i == len (environment) - 2):
            print(environment [ i ], ',', rep + 1)
    else:
        print(environment [ i ], ',', rep + 1)
        rep = 0
#######


def printOut (environment):
    for area in environment:
        print(area)
    print(31*"\n")

# Environment
def stateEnvironment(environment):
    for area in environment:
        actual = 0
        for place in area:
            area[actual] = randint(0,2)
            actual +=1

    return environment

printOut(environment)
time.sleep(0.5)

# Agent
def gasController(environment):
    for area in environment:
        actual = 0
        for place in area:
            if place != noGasLeak:
                area[actual] = "Fixed"

                printOut (environment)
                time.sleep(0.5)

                area[actual] = noGasLeak
                actual += 1
            
            else:
                save = area[actual]
                area[actual] = agent
                printOut(environment)
                area[actual] = save
                time.sleep(0.5)

                actual += 1

                print (actual)
                #continue

    return environment

while True:
    printOut (gasController(environment))
    environment = stateEnvironment(environment)
    #printOut(environment)
    time.sleep(2)
    #printOut(environment)
    break






