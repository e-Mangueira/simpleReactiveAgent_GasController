import random


class Ambiente(object):
    def __init__(self):
        self.locationCondition = {'A': '0', 'B': '0'}
        self.locationCondition['A'] = random.randint(0, 1)
        self.locationCondition['B'] = random.randint(0, 1)


class AgenteTrabalho(Ambiente):
    def __init__(self, Ambiente):
        print(Ambiente.locationCondition)
        # IsDirty = Ambiente.locationCondition[position] == 1
        # IsClean = Ambiente.locationCondition[position] == 0
        Score = 0
        localizacaoAgente = random.randint(0, 1)
        # print(localizacaoAgente)
        # if (localizacaoAgente == 0):
        #   print('Agente limpador foi colocado na posição A')
        #   if (IsDirty):
        #     print(' Posição A está sujo')
        # elif (localizacaoAgente == 0):
        #   print('Agente limpador foi colocado na posição B')
        if localizacaoAgente == 0:
            print ("Agente foi colocado aleatoriamente na localização A.")
   
            if Ambiente.locationCondition['A'] == 1:
                print ("Local A esta sujo.")
      
                Ambiente.locationCondition['A'] = 0;
                Score += 1
                print ("Local A foi limpo.")
             
                print ("Movimentando para o local B...")
                Score -= 1
                
                if Ambiente.locationCondition['B'] == 1:
                    print ("Local B esta sujo.")
                   
                    Ambiente.locationCondition['B'] = 0;
                    Score += 1
                    print ("Local B foi limpo.")
            else:
                Score -= 1
                print ("Movimentando para o local B...")
                
                if Ambiente.locationCondition['B'] == 1:
                    print( "Local B esta sujo.")
                  
                    Ambiente.locationCondition['B'] = 0;
                    Score += 1
                    print ("Local B foi limpo.")

        elif localizacaoAgente == 1:
            print ("Agente foi colocado aleatoriamente na localização B.")
          
            if Ambiente.locationCondition['B'] == 1:
                print ("Local B esta sujo.")
              
                Ambiente.locationCondition['B'] = 0;
                Score += 1
                print ("Local B foi limpo.")
              
                Score -= 1
                print ("Movimentando para o local A...")
               
                if Ambiente.locationCondition['A'] == 1:
                    print ("Local A esta sujo.")
               
                    Ambiente.locationCondition['A'] = 0;
                    Score += 1
                    print ("Local A foi limpo.")
            else:
                print ("Movimentando para o local A...")
                Score -= 1
               
                if Ambiente.locationCondition['A'] == 1:
                    print ("Local A esta sujo.")
                    
                    Ambiente.locationCondition['A'] = 0;
                    Score += 1
                    print ("Local A foi limpo.")

        print (Ambiente.locationCondition)
        print ("Desempenho: " + str(Score))

ambienteMontado = Ambiente()
oAgente = AgenteTrabalho(ambienteMontado)
