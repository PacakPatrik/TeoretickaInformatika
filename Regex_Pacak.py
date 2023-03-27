import string as st

def automat(vzor):
    counter = 0
    stav = 0
    prechodovaFunkce = {}
    abeceda = []
    while True:
        if counter>len(vzor)-1:
            break
        charakter=vzor[counter]

        if charakter=="#":  
            for cislo in st.digits:
                prechodovaFunkce[(stav, cislo)]=stav+1
                abeceda.append(cislo)
            stav += 1
        elif charakter=="$":  
            for znak in st.ascii_letters:
                prechodovaFunkce[(stav, znak)]=stav+1
                abeceda.append(znak)
            stav+=1
        elif charakter=="&":  
            for znaky in st.digits+st.ascii_letters:
                prechodovaFunkce[(stav, znaky)]=stav+1
                abeceda.append(znaky)
            stav += 1
        elif charakter=="*":  
            charakter_pred = vzor[counter-1]
            if charakter_pred=="$":
                for znak in st.ascii_letters:
                    prechodovaFunkce[(stav, znak)]=stav
                    abeceda.append(znak)
            elif charakter_pred=="#":
                for cislo in st.digits:
                    prechodovaFunkce[(stav, cislo)]=stav
                    abeceda.append(cislo)
            elif charakter_pred=="&":
                for znaky in st.digits+st.ascii_letters:
                    prechodovaFunkce[(stav, znaky)]=stav
                    abeceda.append(znaky)
            else:
                prechodovaFunkce[(stav, charakter_pred)]=stav
        elif charakter=="|":  
            charakter_po = vzor[counter+1]
            if charakter_po=="$":
                for znak in st.ascii_letters:
                    prechodovaFunkce[(stav-1,znak)]=stav
                    abeceda.append(znak)
            elif charakter_po=="#":
                for cislo in st.digits:
                    prechodovaFunkce[(stav-1, cislo)]=stav
                    abeceda.append(cislo)
            elif charakter_po=="&":
                for znaky in st.digits+st.ascii_letters:
                    prechodovaFunkce[(stav-1, znaky)]=stav
                    abeceda.append(znaky)
            else:
                abeceda.append(charakter_po)
                prechodovaFunkce[(stav-1, charakter_po)]=stav
            counter+=1
        else:
            abeceda.append(charakter)
            prechodovaFunkce[(stav, charakter)]=stav+1
            stav+=1
        counter+=1

    pocatecni_stav=0
    stavy=list(range(stav))
    koncovy_stav=[stav]
    return abeceda, stavy, prechodovaFunkce, pocatecni_stav, koncovy_stav

def KA(slovo,abeceda,stavy,prechodovaFunkce,pocatecni_stav,koncovy_stav,):
    stav = pocatecni_stav
    for charakter in slovo:
        if charakter not in abeceda:
            return False
        try:
            stav = prechodovaFunkce[(stav, charakter)]
        except KeyError:
            return False
    if stav in koncovy_stav:
        return True
    else:
        return False

vysledky=[]


vzor_auto=automat("&##&@&&.$$")
x=KA("p22a@gm.cz", *vzor_auto)
vysledky.append(x)

vzor_auto=automat("&&*@&&*.$$$*")
x=KA("pacakpatrik@gmail.com", *vzor_auto)
vysledky.append(x)

x=KA("pacakpatrik@gmail.om", *vzor_auto)
vysledky.append(x)

vzor_auto = automat("#########")
x=KA("606245245", *vzor_auto)
vysledky.append(x)

x=KA("60624524", *vzor_auto)
vysledky.append(x)
print(vysledky)
