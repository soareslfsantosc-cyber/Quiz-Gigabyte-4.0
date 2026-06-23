mport random
#######
#######
a = 1
q = 1
mem_q1 = 0
mem_q2 = 0
mem_q3 = 0
mem_q4 = 0
mem_q5 = 0
mem_q6 = 0
mem_q7 = 0
mem_q8 = 0
mem_q9 = 0
mem_q10 = 0
acerto = 0
erro = 0
def q1(acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10) :
    v = 1
    while v == 1 :
        v = 1
        print(f"Questão {q}\nQual o nome da tecnologia do gerenciamento das ventoinhas da gigabyte?")
        print("\n1 - Smart Fan\n2 - Fan Control\n3 - Cooling system\n4 - Smart Cooling\n5 - Expert Fan")
        Questão_1 = int(input("\nQual sua resposta : "))
        if Questão_1 == 1 :
            print("\nVocê acertou\n")
            print("A Gigabyte usa a tecnologia smart fan para gerenciar as ventoinhas do sistema\nessa tecnologia faz com que os usuários consigam controlar a velocidade da ventoinhas\n")
            v = 2
            acerto += 1
            erro = erro
            if q == 1 :
                mem_q1 = 1
            elif q == 2 :
                mem_q2 = 1
            elif q == 3 :
                mem_q3 = 1 
            elif q == 4 :
                mem_q4 = 1
            elif q == 5 :
                mem_q5 = 1
            elif q == 6 :
                mem_q6 = 1
            elif q == 7 :
                mem_q7 = 1
            elif q == 8 :
                mem_q8 = 1
            elif q == 9 :
                mem_q9 = 1
            elif q == 10 :
                mem_q10 = 1
            return(acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10)
        elif Questão_1 >= 1 and Questão_1 <= 5 and Questão_1 != 1 : 
            print("\nVocê errou\n")
            v = 2
            erro += 1
            acerto = acerto
            if q == 1 :
                mem_q1 = 0
            elif q == 2 :
                mem_q2 = 0
            elif q == 3 :
                mem_q3 = 0
            elif q == 4 :
                mem_q4 = 0
            elif q == 5 :
                mem_q5 = 0
            elif q == 6 :
                mem_q6 = 0
            elif q == 7 :
                mem_q7 = 0
            elif q == 8 :
                mem_q8 = 0
            elif q == 9 :
                mem_q9 = 0
            elif q == 10 :
                mem_q10 = 0
            return(acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10)
        else :
            print("\nPor favor, digite um número valido\n")
#####
def q2(acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10) :
    v = 1
    while v == 1 :
        print(f"Questão {q}\nQual o tipo de memória RAM que as placas mães atuais da gigabyte suportam?")
        print("\n1 - DDR4\n2 - DDR6\n3 - DDR2\n4 - DDR5\n5 - DDR3")
        Questão_2 = int(input("\nQual sua resposta : "))
        if Questão_2 == 4 :
            print("\nVocê acertou\n")
            print("As placas-mãe da Gigabyte mais recentes suportam o DDR5, que é a última\ngeração de memória RAM, oferece uma alta velocidade e maior eficiência energética\n")
            v = 2
            acerto += 1
            if q == 1 :
                mem_q1 = 1
            elif q == 2 :
                mem_q2 = 1
            elif q == 3 :
                mem_q3 = 1 
            elif q == 4 :
                mem_q4 = 1
            elif q == 5 :
                mem_q5 = 1
            elif q == 6 :
                mem_q6 = 1
            elif q == 7 :
                mem_q7 = 1
            elif q == 8 :
                mem_q8 = 1
            elif q == 9 :
                mem_q9 = 1
            elif q == 10 :
                mem_q10 = 1
            return(acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10)
        elif Questão_2 >= 1 and Questão_2 <= 5 and Questão_2 != 4 :
            print("\nVocê errou\n")
            v = 2
            erro += 1
            if q == 1 :
                mem_q1 = 0
            elif q == 2 :
                mem_q2 = 0
            elif q == 3 :
                mem_q3 = 0
            elif q == 4 :
                mem_q4 = 0
            elif q == 5 :
                mem_q5 = 0
            elif q == 6 :
                mem_q6 = 0
            elif q == 7 :
                mem_q7 = 0
            elif q == 8 :
                mem_q8 = 0
            elif q == 9 :
                mem_q9 = 0
            elif q == 10 :
                mem_q10 = 0
            return(acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10)
        else :
            print("\nPor favor, digite um número valido\n")
#####
def q3(acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10) :
    v = 1
    while v == 1 :
        print(f"Questão {q}\nQual o nome do codec de áudio utilizado em muitas placas-mãe?")
        print("\n1 - ALC1150\n2 - Realtek HD Audio\n3 - ALC1220\n4 - Creative Sound Amplificator\n5 - Creative Sound Blaster")
        Questão_3 = int(input("\nQual sua resposta : "))
        if Questão_3 == 3 :
            print("\nVocê acertou\n")
            print("Muitas placas-mãe da Gigabyre usam o ALC1220, que é a qualidade mais alta\n")
            v = 2
            acerto += 1
            if q == 1 :
                mem_q1 = 1
            elif q == 2 :
                mem_q2 = 1
            elif q == 3 :
                mem_q3 = 1 
            elif q == 4 :
                mem_q4 = 1
            elif q == 5 :
                mem_q5 = 1
            elif q == 6 :
                mem_q6 = 1
            elif q == 7 :
                mem_q7 = 1
            elif q == 8 :
                mem_q8 = 1
            elif q == 9 :
                mem_q9 = 1
            elif q == 10 :
                mem_q10 = 1
            return(acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10)
        elif Questão_3 >= 1 and Questão_3 <= 5 and Questão_3 != 3 :
            print("\nVocê errou\n")
            v = 2
            erro += 1
            if q == 1 :
                mem_q1 = 0
            elif q == 2 :
                mem_q2 = 0
            elif q == 3 :
                mem_q3 = 0
            elif q == 4 :
                mem_q4 = 0
            elif q == 5 :
                mem_q5 = 0
            elif q == 6 :
                mem_q6 = 0
            elif q == 7 :
                mem_q7 = 0
            elif q == 8 :
                mem_q8 = 0
            elif q == 9 :
                mem_q9 = 0
            elif q == 10 :
                mem_q10 = 0
            return(acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10)
        else :
            print("\nPor favor, digite um número valido\n")
#####
def q4(acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10) :
    v = 1
    while v == 1 :
        print(f"Questão {q}\nQual a velocidade máxima de transferência de dados suportada pelos slots M.2 PCIe 4.0 x4 das placas-mãe da Gigabyte?")
        print("\n1 - 8000 MB/s\n2 - 7000 MB/s\n3 - 1000 MB/s\n4 - 2000 MB/s\n5 - 5000 MB/s")
        Questão_4 = int(input("\nQual sua resposta : "))
        if Questão_4 == 2 :
            print("\nVocê acertou\n")
            print("Os slots M.2 PCIe 4.0 x4 das placas-mãe da Gigabyte suportam até 7000 MB/s, o que é rapido e ideal\n")
            v = 2
            acerto += 1
            if q == 1 :
                mem_q1 = 1
            elif q == 2 :
                mem_q2 = 1
            elif q == 3 :
                mem_q3 = 1 
            elif q == 4 :
                mem_q4 = 1
            elif q == 5 :
                mem_q5 = 1
            elif q == 6 :
                mem_q6 = 1
            elif q == 7 :
                mem_q7 = 1
            elif q == 8 :
                mem_q8 = 1
            elif q == 9 :
                mem_q9 = 1
            elif q == 10 :
                mem_q10 = 1
            return(acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10)
        elif Questão_4 >= 1 and Questão_4 <= 5 and Questão_4 != 2 :
            print("\nVocê errou\n")
            v = 2
            erro += 1
            if q == 1 :
                mem_q1 = 0
            elif q == 2 :
                mem_q2 = 0
            elif q == 3 :
                mem_q3 = 0
            elif q == 4 :
                mem_q4 = 0
            elif q == 5 :
                mem_q5 = 0
            elif q == 6 :
                mem_q6 = 0
            elif q == 7 :
                mem_q7 = 0
            elif q == 8 :
                mem_q8 = 0
            elif q == 9 :
                mem_q9 = 0
            elif q == 10 :
                mem_q10 = 0
            return(acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10)
        else :
            print("\nPor favor, digite um número valido\n")
#####
def q5(acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10) :
    v = 1
    while v == 1 :
        print(f"Questão {q}\nQual o nome da interface de BIOS usada pela Gigabyte?")
        print("\n1 - Gigabyte BIOS\n2 - UC BIOS\n3 - UEFI BIOS\n4 - Extreme BIOS\n5 - Advanced BIOS")
        Questão_5 = int(input("\nQual sua resposta : "))
        if Questão_5 == 2 :
            print("\nVocê acertou\n")
            print("A Gigabyte utiliza a interface a UC BIOS, que é uma interface intuitiva e fácil de usar\n")
            v = 2
            acerto += 1
            if q == 1 :
                mem_q1 = 1
            elif q == 2 :
                mem_q2 = 1
            elif q == 3 :
                mem_q3 = 1 
            elif q == 4 :
                mem_q4 = 1
            elif q == 5 :
                mem_q5 = 1
            elif q == 6 :
                mem_q6 = 1
            elif q == 7 :
                mem_q7 = 1
            elif q == 8 :
                mem_q8 = 1
            elif q == 9 :
                mem_q9 = 1
            elif q == 10 :
                mem_q10 = 1
            return(acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10)
        elif Questão_5 >= 1 and Questão_5 <= 5 and Questão_5 != 2 :
            print("\nVocê errou\n")
            v = 2
            erro += 1
            if q == 1 :
                mem_q1 = 0
            elif q == 2 :
                mem_q2 = 0
            elif q == 3 :
                mem_q3 = 0
            elif q == 4 :
                mem_q4 = 0
            elif q == 5 :
                mem_q5 = 0
            elif q == 6 :
                mem_q6 = 0
            elif q == 7 :
                mem_q7 = 0
            elif q == 8 :
                mem_q8 = 0
            elif q == 9 :
                mem_q9 = 0
            elif q == 10 :
                mem_q10 = 0
            return(acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10)
        else :
            print("\nPor favor, digite um número valido\n")
#####
def q6(acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10) :
    v = 1
    while v == 1 :
        print(f"Questão {q}\nQual o tipo de conector de alimentação utilizado pela Gigabyte?")
        print("\n1 - ATX 12V\n2 - EPS 12V\n3 - EPS 16V\n4 - PCIe 8-pin\n5 - 1,2,4")
        Questão_6 = int(input("\nQual sua resposta : "))
        if Questão_6 == 5 :
            print("\nVocê acertou\n")
            print("A Gigabyte usa os conectores ATX 12V, EPS 12V e PCI 8-pin para fornecer uma energia estável e eficiente\n")
            v = 2
            acerto += 1
            if q == 1 :
                mem_q1 = 1
            elif q == 2 :
                mem_q2 = 1
            elif q == 3 :
                mem_q3 = 1 
            elif q == 4 :
                mem_q4 = 1
            elif q == 5 :
                mem_q5 = 1
            elif q == 6 :
                mem_q6 = 1
            elif q == 7 :
                mem_q7 = 1
            elif q == 8 :
                mem_q8 = 1
            elif q == 9 :
                mem_q9 = 1
            elif q == 10 :
                mem_q10 = 1
            return(acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10)
        elif Questão_6 >= 1 and Questão_6 <= 5 and Questão_6 != 5 :
            print("\nVocê errou\n")
            v = 2
            erro += 1
            if q == 1 :
                mem_q1 = 0
            elif q == 2 :
                mem_q2 = 0
            elif q == 3 :
                mem_q3 = 0
            elif q == 4 :
                mem_q4 = 0
            elif q == 5 :
                mem_q5 = 0
            elif q == 6 :
                mem_q6 = 0
            elif q == 7 :
                mem_q7 = 0
            elif q == 8 :
                mem_q8 = 0
            elif q == 9 :
                mem_q9 = 0
            elif q == 10 :
                mem_q10 = 0
            return(acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10)
        else :
            print("\nPor favor, digite um número valido\n")
#####
def q7(acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10) :
    v = 1
    while v == 1 :
        print(f"Questão {q}\nQual o nome da tecnologia de overclocking da Gigabyte?")
        print("\n1 - Overclocking Expert\n2 - OC Guru\n3 - PerfDrive\n4 - Turbo Boost\n5 - Overclocking Boost")
        Questão_7 = int(input("\nQual sua resposta : "))
        if Questão_7 == 3 :
            print("\nVocê acertou\n")
            print("A Gigabyte utiliza o PerfDrive para overclocking, que permite os usuários ajustar\nas configuarações do sistema para um desempenho melhor\n")
            v = 2
            acerto += 1
            if q == 1 :
                mem_q1 = 1
            elif q == 2 :
                mem_q2 = 1
            elif q == 3 :
                mem_q3 = 1 
            elif q == 4 :
                mem_q4 = 1
            elif q == 5 :
                mem_q5 = 1
            elif q == 6 :
                mem_q6 = 1
            elif q == 7 :
                mem_q7 = 1
            elif q == 8 :
                mem_q8 = 1
            elif q == 9 :
                mem_q9 = 1
            elif q == 10 :
                mem_q10 = 1
            return(acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10)
        elif Questão_7 >= 1 and Questão_7 <= 5 and Questão_7 != 3 :
            print("\nVocê errou\n")
            v = 2
            erro += 1
            if q == 1 :
                mem_q1 = 0
            elif q == 2 :
                mem_q2 = 0
            elif q == 3 :
                mem_q3 = 0
            elif q == 4 :
                mem_q4 = 0
            elif q == 5 :
                mem_q5 = 0
            elif q == 6 :
                mem_q6 = 0
            elif q == 7 :
                mem_q7 = 0
            elif q == 8 :
                mem_q8 = 0
            elif q == 9 :
                mem_q9 = 0
            elif q == 10 :
                mem_q10 = 0
            return(acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10)
        else :
            print("\nPor favor, digite um número valido\n")
#####
def q8(acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10) :
    v = 1
    while v == 1 :
        print(f"Questão {q}\nQual é a velocidade máxima de transferência de dados do Wi-Fi 6E das placas-mãe Gigabyte?")
        print("\n1 - 11,7 Gbps\n2 - 11,8 Gbps\n3 - 9 Gbps \n4 - 9,6 Gbps\n5 - 12 Gbps")
        Questão_8 = int(input("\nQual sua resposta : "))
        if Questão_8 == 4 :
            print("\nVocê acertou\n")
            print("O Wi-Fi 6E suporte velocidades de transfêrencia de daos de até 9,6Gbps, o que é muito rapido\n")
            v = 2
            acerto += 1
            if q == 1 :
                mem_q1 = 1
            elif q == 2 :
                mem_q2 = 1
            elif q == 3 :
                mem_q3 = 1 
            elif q == 4 :
                mem_q4 = 1
            elif q == 5 :
                mem_q5 = 1
            elif q == 6 :
                mem_q6 = 1
            elif q == 7 :
                mem_q7 = 1
            elif q == 8 :
                mem_q8 = 1
            elif q == 9 :
                mem_q9 = 1
            elif q == 10 :
                mem_q10 = 1
            return(acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10)
        elif Questão_8 >= 1 and Questão_8 <= 5 and Questão_8 != 4 :
            print("\nVocê errou\n")
            v = 2
            erro += 1
            if q == 1 :
                mem_q1 = 0
            elif q == 2 :
                mem_q2 = 0
            elif q == 3 :
                mem_q3 = 0
            elif q == 4 :
                mem_q4 = 0
            elif q == 5 :
                mem_q5 = 0
            elif q == 6 :
                mem_q6 = 0
            elif q == 7 :
                mem_q7 = 0
            elif q == 8 :
                mem_q8 = 0
            elif q == 9 :
                mem_q9 = 0
            elif q == 10 :
                mem_q10 = 0
            return(acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10)
        else :
            print("\nPor favor, digite um número valido\n")
#####
def q9(acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10) :
    v = 1
    while v == 1 :
        print(f"Questão {q}\nQual o tipo de LAN suportado pelas placas-mãe Gigabyte?")
        print("\n1 - 6 GbE LAN\n2 - 10 GbE LAN\n3 - 5 GbE LAN\n4 - Gigabyte LAN\n5 - 2,5 GbE LAN")
        Questão_9 = int(input("\nQual sua resposta : "))
        if Questão_9 == 5 :
            print("\nVocê acertou\n")
            print("As placas-mãe da Gigabyte suportam 2,5 GbE LAN, que ofecere velocidades bem mais altas\nque o comum, sendo notoriamente melhor\n")
            v = 2
            acerto += 1
            if q == 1 :
                mem_q1 = 1
            elif q == 2 :
                mem_q2 = 1
            elif q == 3 :
                mem_q3 = 1 
            elif q == 4 :
                mem_q4 = 1
            elif q == 5 :
                mem_q5 = 1
            elif q == 6 :
                mem_q6 = 1
            elif q == 7 :
                mem_q7 = 1
            elif q == 8 :
                mem_q8 = 1
            elif q == 9 :
                mem_q9 = 1
            elif q == 10 :
                mem_q10 = 1
            return(acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10)
        elif Questão_9 >= 1 and Questão_9 <= 5 and Questão_9 != 5 :
            print("\nVocê errou\n")
            v = 2
            erro += 1
            if q == 1 :
                mem_q1 = 0
            elif q == 2 :
                mem_q2 = 0
            elif q == 3 :
                mem_q3 = 0
            elif q == 4 :
                mem_q4 = 0
            elif q == 5 :
                mem_q5 = 0
            elif q == 6 :
                mem_q6 = 0
            elif q == 7 :
                mem_q7 = 0
            elif q == 8 :
                mem_q8 = 0
            elif q == 9 :
                mem_q9 = 0
            elif q == 10 :
                mem_q10 = 0
            return(acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10)
        else :
            print("\nPor favor, digite um número valido\n")
#####
def q10(acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10) :
    v = 1
    while v == 1 :
        print(f"Questão {q}\nQual é a tecnologia de proteção contra sobretensão da Gigabyte?")
        print("\n1 - Overvoltage Protection\n2 - Undervoltage Protection\n3 - Fuse\n4 - Voltage Regulator Module\n5 - Voltage Protector Module")
        Questão_10 = int(input("\nQual sua resposta : "))
        if Questão_10 == 1 :
            print("\nVocê acertou\n")
            print("A Gigabyte utiliza a interface a UC BIOS, que é uma interface intuitiva e fácil de usar\n")
            v = 2
            acerto += 1
            if q == 1 :
                mem_q1 = 1
            elif q == 2 :
                mem_q2 = 1
            elif q == 3 :
                mem_q3 = 1 
            elif q == 4 :
                mem_q4 = 1
            elif q == 5 :
                mem_q5 = 1
            elif q == 6 :
                mem_q6 = 1
            elif q == 7 :
                mem_q7 = 1
            elif q == 8 :
                mem_q8 = 1
            elif q == 9 :
                mem_q9 = 1
            elif q == 10 :
                mem_q10 = 1
            return(acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10)
        elif Questão_10 >= 1 and Questão_10 <= 5 and Questão_10 != 1 :
            print("\nVocê errou\n")
            v = 2
            erro += 1
            if q == 1 :
                mem_q1 = 0
            elif q == 2 :
                mem_q2 = 0
            elif q == 3 :
                mem_q3 = 0
            elif q == 4 :
                mem_q4 = 0
            elif q == 5 :
                mem_q5 = 0
            elif q == 6 :
                mem_q6 = 0
            elif q == 7 :
                mem_q7 = 0
            elif q == 8 :
                mem_q8 = 0
            elif q == 9 :
                mem_q9 = 0
            elif q == 10 :
                mem_q10 = 0
            return(acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10)
        else :
            print("\nPor favor, digite um número valido\n")
#######
#
b = 1 #
c = 0 #
d = 0
q1_pass = 0
q2_pass = 0
q3_pass = 0
q4_pass = 0
q5_pass = 0
q6_pass = 0
q7_pass = 0
q8_pass = 0
q9_pass = 0
q10_pass = 0
#
while 1 == 1 :
    while b == 1 :
        v = 1
        q_sel = random.randint(1,10)
        if q_sel == 1 and q1_pass != 1 :
            (acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10) = q1(acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10)
            q1_pass = 1
            q += 1
        elif q_sel == 2 and q2_pass != 1 :
            (acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10) = q2(acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10)
            q2_pass = 1
            q += 1
        elif q_sel == 3 and q3_pass != 1 :
            (acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10) = q3(acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10)
            q3_pass =  1
            q += 1
        elif q_sel == 4 and q4_pass != 1 :
            (acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10) = q4(acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10)
            q4_pass = 1
            q += 1
        elif q_sel == 5 and q5_pass != 1 :
            (acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10) = q5(acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10)
            q5_pass = 1
            q += 1
        elif q_sel == 6 and q6_pass != 1 :
            (acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10) = q6(acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10)
            q6_pass = 1
            q += 1
        elif q_sel == 7 and q7_pass != 1 :
            (acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10) = q7(acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10)
            q7_pass = 1
            q += 1
        elif q_sel == 8 and q8_pass != 1 :
            (acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10) = q8(acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10)
            q8_pass = 1
            q += 1
        elif q_sel == 9 and q9_pass != 1 :
            (acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10) = q9(acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10)
            q9_pass = 1
            q += 1
        elif q_sel == 10 and q10_pass != 1 :
            (acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10) = q10(acerto,erro,mem_q1,mem_q2,mem_q3,mem_q4,mem_q5,mem_q6,mem_q7,mem_q8,mem_q9,mem_q10)
            q10_pass = 1
            q += 1
        if q1_pass == 1 and q2_pass == 1 and q3_pass == 1 and q4_pass == 1 and q5_pass == 1 and q6_pass == 1 and q7_pass == 1 and q8_pass == 1 and q9_pass == 1 and q10_pass == 1 :
            b = 0
            c = 1 
    while c == 1 :
        if mem_q1 == 0 :
            r1 = "Errada"
        elif mem_q1 == 1 :
            r1 = "Acertada"
        if mem_q2 == 0 :
            r2 = "Errada"
        elif mem_q2 == 1 :
            r2 = "Acertada"
        if mem_q3 == 0 :
            r3 = "Errada"
        elif mem_q3 == 1 :
            r3 = "Acertada"
        if mem_q4 == 0 :
            r4 = "Errada"
        elif mem_q4 == 1 :
            r4 = "Acertada"
        if mem_q5 == 0 :
            r5 = "Errada"
        elif mem_q5 == 1 :
            r5 = "Acertada"
        if mem_q6 == 0 :
            r6 = "Errada"
        elif mem_q6 == 1 :
            r6 = "Acertada"
        if mem_q7 == 0 :
            r7 = "Errada"
        elif mem_q7 == 1 :
            r7 = "Acertada"
        if mem_q8 == 0 :
            r8 = "Errada"
        elif mem_q8 == 1 :
            r8 = "Acertada"
        if mem_q9 == 0 :
            r9 = "Errada"
        elif mem_q9 == 1 :
            r9 = "Acertada"
        if mem_q10 == 0 :
            r10 = "Errada"
        elif mem_q10 == 1 :
            r10 = "Acertada"
        c = 0
        d = 1
    while d == 1 :
        print(f"Você terminou todas as perguntas\nacertando {acerto} perguntas e errando {erro} perguntas\n-")
        print(f"Estatisticas gerais\nQuestão 1 - {r1} | Questão 2 - {r2} | Questão 3 - {r3}\nQuestão 4 - {r4} | Questão 5 - {r5} | Questão 6 - {r6}")
        print(f"Questão 7 - {r7} | Questão 8 - {r8} | Questão 9 - {r9} | Questão 10 - {r10}\n-")
        print("Deseja jogar novamente\n1 - Sim\n2 - Não\n-")
        resp = int(input("Resposta :"))
        print("")
        if resp == 1 :
            a = 1 #
            b = 1 #
            c = 0 #
            d = 0 #
            q = 1 #
            q1_pass = 0
            q2_pass = 0
            q3_pass = 0
            q4_pass = 0
            q5_pass = 0
            q6_pass = 0
            q7_pass = 0
            q8_pass = 0
            q9_pass = 0
            q10_pass = 0
            mem_q1 = 0
            mem_q2 = 0
            mem_q3 = 0
            mem_q4 = 0
            mem_q5 = 0
            mem_q6 = 0
            mem_q7 = 0
            mem_q8 = 0
            mem_q9 = 0
            mem_q10 = 0
            acerto = 0
            erro = 0
            for i in range (550) :
                print("\n")
        if resp == 2 :
            a = 3
            b = 3
            c = 3
            d = 3
            break
#######
#######