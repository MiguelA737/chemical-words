import json

periodicTable = {
    "h" : "H",
    "he" : "He",
    "li" : "Li",
    "be" : "Be",
    "b" : "B",
    "c" : "C",
    "n" : "N",
    "o" : "O",
    "f" : "F",
    "ne" : "Ne",
    "na" : "Na",
    "mg" : "Mg",
    "al" : "Al",
    "si" : "Si",
    "p" : "P",
    "s" : "S",
    "cl" : "Cl",
    "ar" : "Ar",
    "k" : "K",
    "ca" : "Ca",
    "sc" : "Sc",
    "ti" : "Ti",
    "v" : "V",
    "cr" : "Cr",
    "mn" : "Mn",
    "fe" : "Fe",
    "co" : "Co",
    "ni" : "Ni",
    "cu" : "Cu",
    "zn" : "Zn",
    "ga" : "Ga",
    "ge" : "Ge",
    "as" : "As",
    "se" : "Se",
    "br" : "Br",
    "kr" : "Kr",
    "rb" : "Rb",
    "sr" : "Sr",
    "y" : "Y",
    "zr" : "Zr",
    "nb" : "Nb",
    "mo" : "Mo",
    "tc" : "Tc",
    "ru" : "Ru",
    "rh" : "Rh",
    "pd" : "Pd",
    "ag" : "Ag",
    "cd" : "Cd",
    "in" : "In",
    "sn" : "Sn",
    "sb" : "Sb",
    "te" : "Te",
    "i" : "I",
    "xe" : "Xe",
    "cs" : "Cs",
    "ba" : "Ba",
    "la" : "La",
    "ce" : "Ce",
    "pr" : "Pr",
    "nd" : "Nd",
    "pm" : "Pm",
    "sm" : "Sm",
    "eu" : "Eu",
    "gd" : "Gd",
    "tb" : "Tb",
    "dy" : "Dy",
    "ho" : "Ho",
    "er" : "Er",
    "tm" : "Tm",
    "yb" : "Yb",
    "lu" : "Lu",
    "hf" : "Hf",
    "ta" : "Ta",
    "w" : "W",
    "re" : "Re",
    "os" : "Os",
    "ir" : "Ir",
    "pt" : "Pt",
    "au" : "Au",
    "hg" : "Hg",
    "tl" : "Tl",
    "pb" : "Pb",
    "bi" : "Bi",
    "po" : "Po",
    "at" : "At",
    "rn" : "Rn",
    "fr" : "Fr",
    "ra" : "Ra",
    "ac" : "Ac",
    "th" : "Th",
    "pa" : "Pa",
    "u" : "U",
    "np" : "Np",
    "pu" : "Pu",
    "am" : "Am",
    "cm" : "Cm",
    "bk" : "Bk",
    "cf" : "Cf",
    "es" : "Es",
    "fm" : "Fm",
    "md" : "Md",
    "no" : "No",
    "lr" : "Lr",
    "rf" : "Rf",
    "db" : "Db",
    "sg" : "Sg",
    "bh" : "Bh",
    "hs" : "Hs",
    "mt" : "Mt",
    "ds" : "Ds",
    "rg" : "Rg",
    "cn" : "Cn",
    "nh" : "Nh",
    "fl" : "Fl",
    "mc" : "Mc",
    "lv" : "Lv",
    "ts" : "Ts",
    "og" : "Og"
}

# for key, value in periodicTable.items():
#     if(key.capitalize() != value.capitalize()):
#         print("Warning: " + key + " and " + value + " doesn't match")

def checkChemicalWord(charArr):
    if(len(charArr) == 0):
        return True, ""

    i = 0
    try:
        el = periodicTable[charArr[i]] + " "
        
        charArr.pop(i)

        check, chemicalWord = checkChemicalWord(charArr)
        if(not check):
            raise Exception()
            
        return True, (el + chemicalWord)
    except:
        try:
            el = periodicTable[str(charArr[i] + charArr[i + 1])] + " "
            charArr.pop(i + 1)
            charArr.pop(i)
            

            check, chemicalWord = checkChemicalWord(charArr)
            if(not check):
                raise Exception()
                
            return True, (el + chemicalWord)
        except:
            return False, ""
            

input = open("words_dictionary.json", "r")
output = open("chemical_words.log", "w")

words = json.load(input)

chemicalWordCount = 0
nonChemicalWordCount = 0

for word in words:
    charArr = list(word)

    check, chemicalWord = checkChemicalWord(charArr)
    if(check):
        chemicalWordCount = chemicalWordCount + 1
        output.write(chemicalWord + "\n")
        print(chemicalWord)
    else:
        nonChemicalWordCount = nonChemicalWordCount + 1

output.write("\nChemical Word Count: " + str(chemicalWordCount) + "\n")
print("\nChemical Word Count: " + str(chemicalWordCount))
output.write("Non-Chemical Word Count: " + str(nonChemicalWordCount) + "\n")
print("Non-Chemical Word Count: " + str(nonChemicalWordCount))

