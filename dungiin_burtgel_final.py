import json
import os

SURAGCHID_FILE = "suragchid.txt"

# Ehnii medeelel. Fail baihgui uyd l ene medeelleer fail uusgene.
ehnii_suragchid = [
    {"ner": "Temka", 
     "dun": {"math": 96, "physic": 90, "history": 97}, 
     "huis": "eregtei"},
    {"ner": "Suhee", 
     "dun": {"math": 100, "physic": 98, "history": 97}, 
     "huis": "eregtei"},
    {"ner": "Saraa", 
     "dun": {"math": 100, "physic": 100, "history": 98}, 
     "huis": "emegtei"},
    {"ner": "Batuka", 
     "dun": {"math": 100, "physic": 98, "history": 95}, 
     "huis": "eregtei"},
    {"ner": "Ali", 
     "dun": {"math": 95, "physic": 95, "history": 95}, 
     "huis": "eregtei"},
    {"ner": "Saruul", 
     "dun": {"math": 93, "physic": 97, "history": 98}, 
     "huis": "emegtei"},
    {"ner": "Bulgaa", 
     "dun": {"math": 90, "physic": 90, "history": 100}, 
     "huis": "eregtei"},
    {"ner": "Nomio", 
     "dun": {"math": 95, "physic": 90, "history": 98}, 
     "huis": "emegtei"},
    {"ner": "Nandia", 
     "dun": {"math": 93, "physic": 90, "history": 95}, 
     "huis": "emegtei"},
    {"ner": "Tugsuu", 
     "dun": {"math": 98, "physic": 95, "history": 98}, 
     "huis": "eregtei"},
]


# ALDAA: Umnu ni program ajillah burt "suragchid.txt"-iig ehnii medeelleer
#        dahin bichij, nemsen/zassan medeelliig ustgaj baisan.
# ZASVAR: Fail baihgui uyd l uusgene (os.path.exists), baival zovhon unshina.
def suragchid_achaalah(file):
    if not os.path.exists(file):
        suragchid_hadgalah(file, ehnii_suragchid)
    with open(file, "r", encoding="utf-8") as f:
        return json.load(f)


def suragchid_hadgalah(file, suragchid):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(suragchid, f, ensure_ascii=False, indent=2)


# ALDAA: print(number, ".", suragchid) gej buh jagsaaltiig hevlej baisan.
# ZASVAR: suragch["ner"] gej zovhon neriig hevlene. enumerate dugaariig
#         (start=1 -> 1-ees ehelne) avtomataar ogno.
def suragch_haruulah(suragchid):
    for number, suragch in enumerate(suragchid, start=1):
        print(number, ".", suragch["ner"])


# ALDAA: return suragchid gej buh jagsaaltiig butsaadag baisan.
#        Tegeheer huuhed["ner"] deer TypeError garch songolt 3, 4, 5, 6, 7, 8
#        ajillahgui baisan (hamgiin gol aldaa).
# ZASVAR: Oldson neg suragchiig (return suragch) butsaana.
#         lower() -> Temka, temka, TEMKA gesen ali ni ch taarna.
def suragch_haih(suragchid, ner):
    for suragch in suragchid:
        if suragch["ner"].lower() == ner.lower():
            return suragch
    return None


# Ene function zuv baisan: huisiin dagaa suragchdiin nernuudiin jagsaalt butsaana.
def suragchid_huis(suragchid, huis):
    result = []
    for suragch in suragchid:
        if suragch["huis"] == huis:
            result.append(suragch["ner"])
    return result


# ALDAA: Umnuh "suragch_dungiingolc" ni dictionary deer sum(dun) hiij baisan,
#        mon argument-aar orj irsen utgiig dahin tootsood baisan.
#        Mon suragchiin buh hiceeliig ustgaval len(dun)=0 bolood
#        ZeroDivisionError garna.
# ZASVAR: dun.values()-iin niilberiig hiceeliin toonod huvaana.
#         Hooson bol 0 butsaana.
def suragch_dungiin_golc(suragch):
    dun = suragch["dun"]
    if not dun:
        return 0
    return sum(dun.values()) / len(dun)


# ALDAA: Umnu ni suragchid.append(...) gej dictionary deer append hiij baisan.
#        Dictionary deer append baihgui, [key] = utga gej nemdeg.
#        Mon buh suragch oldoh bish, ner-eer neg suragchiig oloh yostoi baisan.
# ZASVAR: Ner-eer suragchiig olood, dotorh "dun" dictionary-d hiceel nemne.
def suragch_dunnemeh(suragchid, ner, hiceel, dun):
    suragch = suragch_haih(suragchid, ner)
    if suragch is None:
        return False
    if hiceel in suragch["dun"]:      # ali hediin baival nemehgui
        return False
    suragch["dun"][hiceel] = dun
    return True


# Ner ali hediin baival nemehgui. Ene function zuv baisan.
def suragch_nemeh(suragchid, shine_suragch):
    if suragch_haih(suragchid, shine_suragch["ner"]):
        return False
    suragchid.append(shine_suragch)
    return True


# ALDAA: 1) shinedun gesen tanigdaagui huvisagch (argument ni shine_dun)
#        2) dictionary deer .append() hiij baisan
#        3) neg suragchiin orond buh suragchiig davtaj (for), return ni
#           loop dotor baisan tul ehnii suragch deer l duusdag baisan
#        4) hiceel argument-iig ashiglaagui
# ZASVAR: Loopgui. Ner-eer olson suragchiin hiceeliin utgiig solino.
def suragch_dunzasah(suragchid, ner, hiceel, shine_dun):
    suragch = suragch_haih(suragchid, ner)
    if suragch is None or hiceel not in suragch["dun"]:
        return False
    suragch["dun"][hiceel] = shine_dun
    return True


# ALDAA: 1) hiceel.remove(...) -> hiceel text, remove ni jagsaaltiin method
#        2) "if hiceel is None" buruu huvisagchiig shalgaj baisan
#        3) ustgah_dun argument heregtei bish (key ustgahad utga ni dagaj ustdag)
# ZASVAR: del -> dictionary-aas key-eer ustgana.
def suragch_dun_ustgah(suragchid, ner, hiceel):
    suragch = suragch_haih(suragchid, ner)
    if suragch is None or hiceel not in suragch["dun"]:
        return False
    del suragch["dun"][hiceel]
    return True


# Suragch ustgah. Jagsaalt dotorh yag ter dictionary-g remove hiine.
# (suragch_haih buh jagsaalt butsaadag baisan uyd ene aldaa garch baisan.)
def suragch_ustgah(suragchid, ner):
    suragch = suragch_haih(suragchid, ner)
    if suragch is None:
        return False
    suragchid.remove(suragch)
    return True


# Hereglegchees 0-100 hoorond zov too avna.
# try/except -> usegtei utga oruulbal program unahgui, dahin asuuna.
def too_avah(zaavar):
    while True:
        try:
            utga = int(input(zaavar))
            if 0 <= utga <= 100:
                return utga
            print("0-100 hoorond too oruul!")
        except ValueError:
            print("Zovhon too oruul!")


# ALDAA: "if not suragchid:" gesen shalgalt baisan, tuundee "while True" (menu)
#        orson baisan. Failaas 10 suragch unshigdsan tul suragchid hooson
#        BISH, ter uchir "if" ajillahgui, menu hevlegdehgui duusdag baisan.
# ZASVAR: "if not suragchid" ustgaj, menu-g "while True"-d shuud oruulsan.
if __name__ == "__main__":
    suragchid = suragchid_achaalah(SURAGCHID_FILE)

    while True:
        print("=======Dungiin Burtgel=======")
        print("1 - Suragchdiin ner")
        print("2 - Suragchdiin huis")
        print("3 - Suragchiin dun")
        print("4 - Suragchiin dungiin dundaj")
        print("5 - Dun zasah")
        print("6 - Shine suragch nemeh")
        print("7 - Suragch hasah")
        print("8 - Hiceel bolon dun nemeh")
        print("9 - Hiceel ustgah")
        print("0 - Garah")
        songolt = input("Tanii songolt (0-9): ").strip()

        if songolt == "1":
            suragch_haruulah(suragchid)

        elif songolt == "2":
            huis = input("Huisee oruul (emegtei/eregtei): ").strip().lower()
            huisuud = suragchid_huis(suragchid, huis)
            if huisuud:
                # ALDAA: "for suragch in suragchid: print(suragch)" gej huisees
                #        huru n buh suragchiig hevlej baisan.
                # ZASVAR: zovhon huisuud (taarsan nernuud)-iig hevlene.
                for ner in huisuud:
                    print("-", ner)
            else:
                print("Huisee zov bic!!")

        elif songolt == "3":
            ner = input("Suragchiin ner: ").strip()
            suragch = suragch_haih(suragchid, ner)
            if suragch:
                print(suragch["ner"], "-", suragch["dun"])
            else:
                print("Suragchiin ner zov bicsen eseh!")

        elif songolt == "4":
            ner = input("Suragchiin ner: ").strip()
            suragch = suragch_haih(suragchid, ner)
            if suragch:
                # ALDAA: suragch_dungiin_golc(suragch) deer zovhon ner (text)
                #        damjuulj baisan; suragch["dun"] avch bolohgui.
                #        Mon sum("dun")/len("dun") gej text deer sum hiij baisan.
                # ZASVAR: Oldson suragchiin dictionary-g damjuulna.
                print("Suragchiin dundaj dun -", round(suragch_dungiin_golc(suragch), 2))
            else:
                print("Suragchiin ner zov bicsen eseh!")

        elif songolt == "5":
            # ALDAA: Umnuh kod buruu argument-tai open(...), "zassan.txt"-iin
            #        neriig json.dump hiij, shinedun huvisagchiig
            #        tanihgui baisan. Ene buh n hereggui.
            # ZASVAR: Ner, hiceel, shine dun asuuj function duudaad hadgalna.
            ner = input("Suragchiin ner: ").strip()
            hiceel = input("Hiceeliin ner: ").strip().lower()
            shine_dun = too_avah("Shine dun: ")
            if suragch_dunzasah(suragchid, ner, hiceel, shine_dun):
                suragchid_hadgalah(SURAGCHID_FILE, suragchid)
                print("Dun zasagdlaa!")
            else:
                print("Iim ner esvel hiceel alga!!")

        elif songolt == "6":
            # ALDAA: Umnu ni suragch_haih(suragchid)-iig ner-gui duudaj,
            #        neriig string deer .append() hiij, dun-g set { } bolgoj,
            #        open(...) deer buruu argument ugch, f tanigdaagui
            #        baisan.
            # ZASVAR: Ner shalgaad, 3 dun + huis asuuj dictionary uusgene.
            ner = input("Nemeh suragchiin ner: ").strip()
            if suragch_haih(suragchid, ner):
                print("Suragch ali hediin bna!")
            else:
                shine_suragch = {
                    "ner": ner,
                    "dun": {
                        "math": too_avah("Math-iin dun: "),
                        "physic": too_avah("Physic-iin dun: "),
                        "history": too_avah("History-iin dun: "),
                    },
                    "huis": input("Huis (eregtei/emegtei): ").strip().lower(),
                }
                suragch_nemeh(suragchid, shine_suragch)
                suragchid_hadgalah(SURAGCHID_FILE, suragchid)
                print("Suragch nemegdlee!")

        elif songolt == "7":
            ner = input("Hasah suragchiin ner: ").strip()
            suragch = suragch_haih(suragchid, ner)
            if suragch is None:
                print("Iim ner baihgui!")
            else:
                # ALDAA: "suragch['ner']-g hasahdaa..." gej quote dotor bichsen
                #        tul neriin orond yag ter text hevlegdej baisan.
                # ZASVAR: neriig string-d + -aar nemne.
                batlah = input(suragch["ner"] + "-g hasahdaa itgeltei bna uu? (tiim/ugui): ").strip().lower()
                if batlah == "tiim":
                    suragch_ustgah(suragchid, ner)
                    suragchid_hadgalah(SURAGCHID_FILE, suragchid)
                    print("Amjilttai hasagdlaa!")
                else:
                    print("Hasah ni bolilgoo.")

        elif songolt == "8":
            ner = input("Suragchiin ner: ").strip()
            hiceel = input("Nemeh hiceeliin ner: ").strip().lower()
            dun = too_avah("Dun: ")
            if suragch_dunnemeh(suragchid, ner, hiceel, dun):
                suragchid_hadgalah(SURAGCHID_FILE, suragchid)
                print("Hiceel bolon dun amjilttai nemegdlee!")
            else:
                print("Suragch baihgui esvel ter hiceel ali hediin bna!")

        elif songolt == "9":
            ner = input("Suragchiin ner: ").strip()
            hiceel = input("Ustgah hiceeliin ner: ").strip().lower()
            if suragch_dun_ustgah(suragchid, ner, hiceel):
                suragchid_hadgalah(SURAGCHID_FILE, suragchid)
                print("Hiceel ustgagdlaa!")
            else:
                print("Iim suragch esvel hiceel alga!")

        elif songolt == "0":
            print("Bayrlalaa daraa uulziy!!")
            break

        else:
            print("Zovhon 0-9 hurtel songonuu!!")