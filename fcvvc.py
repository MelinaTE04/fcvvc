# Module einbinden
import os
# Ausgabe
print("Name: fCVVC\nAutor: Melina Eckert\nDieses Programm erstellt Aufnahmelisten sowie Konfigurationen für UTAU-Datenbanken.\nGeben Sie einfach mit Komma getrennt und ohne Leerzeichen Ihre gewünschten Phoneme an.\n")
# Eingabe
kstring=input("Konsonanten: ") # Konsonanten
vstring=input("Vokale: ") # Vokale
reihe=int(input("Teilen nach: "))
name=input("Dateiname (ohne Erweiterung): ") # Anzahl der Silben einer Aufnahme
recoto=input("Reclist (rec) / Oto.ini (oto): ") # Aufnahmeliste oder OTO
if recoto=="oto":
    kastring=input("Konsonanten (Alias): ") # Alias für Konsonanten in UTAU
    vastring=input("Vokale (Alias): ") # -//- (Vokale)
    cv=input("CV: ") # Beispielotozeile für CV Silben (Anfang der Aufnahme)
    vc=input("VC: ") # Beispielotozeile für VC Silben (Anfang der Aufnahme)
    abstand=int(input("Silbenabstand: ")) # zeitliche Versetzung zweier Silben in ms
    suffix=input("Suffix: ") # Tonhöhe der Aufnahme, kann frei gelassen werden

# String in Liste umwandeln
def stringinliste(string):
    string=string+","
    neu=0
    alt=0
    liste=[]
    while neu<len(string):
        if string[neu]=="," or string[neu]==".":
            liste.append(string[alt:neu])
            alt=neu+1
        neu=neu+1
    return liste

# Eingaben umwandeln
kliste=stringinliste(kstring)
vliste=stringinliste(vstring)

# Reclist schreiben
if recoto=="rec":
    name=name+".txt"
    reclist=open(name, "w")
    for k in range(len(kliste)):
        v=0
        while v<len(vliste):
            start=v
            neu=v-start
            while neu<reihe and v<len(vliste):
                reclist.write("_"+kliste[k]+vliste[v]+kliste[k])
                v=v+1
                neu=v-start
            reclist.write("\n")  
    reclist.close()

# Oto schreiben
elif recoto=="oto":
    name=name+".ini"
    oto=open(name, "w")
    kaliste=stringinliste(kastring)
    valiste=stringinliste(vastring)
    cvliste=stringinliste(cv)
    vcliste=stringinliste(vc)
    for k in range(len(kliste)):
        v=0
        while v<len(vliste):
            start=v
            neu=v-start
            aufnahme=""
            while neu<reihe and v<len(vliste):
                aufnahme=aufnahme+"_"+kliste[k]+vliste[v]+kliste[k]
                v=v+1
                neu=v-start
            v=start
            neu=v-start
            while neu<reihe and v<len(vliste):
                oto.write(aufnahme+".wav="+kaliste[k]+valiste[v]+suffix+","+str(int(cvliste[0])+abstand*neu)+","+cvliste[1]+","+str(int(cvliste[2])-abstand*neu)+","+cvliste[3]+","+cvliste[4]+"\n")
                oto.write(aufnahme+".wav="+valiste[v]+kaliste[k]+suffix+","+str(int(vcliste[0])+abstand*neu)+","+vcliste[1]+","+str(int(vcliste[2])-abstand*neu)+","+vcliste[3]+","+vcliste[4]+"\n")
                v=v+1
                neu=v-start  
    oto.close()

# Fehler
else:
    print("Falsche Eingabe")

schliessen=input("Drücken Sie eine beliebige Taste zum Schließen des Programmes.")
