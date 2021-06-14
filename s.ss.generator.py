def writeInit(word):
    word = word.replace("_", " ")
    res = "    def __init__(self):\n"
    res += "        self.result = \"" + word + '"\n'
    return res

def writeFunction(word):
    word_s = word.replace("_", " ")
    res = "    def "+word+"(self):\n        self.result += \"." 
    res += word_s + "\"\n"
    return res

def writeClass(lst):
    class_name = lst[0]
    res = "class " + class_name + ":\n"
    res += writeInit(class_name)
    mod_lst = list(dict.fromkeys(lst[1:]))    # order preserving
    for word in mod_lst:
        res += writeFunction(word)
    res += "    def ret(self):\n"
    res += "        return self.result"
    return res

def writeMain(lst):
    class_name = lst[0]
    res = class_name + " = " + class_name + "()\n"
    for word in lst[1:]:
        res += class_name + "." + word + "()\n"
    res += "print(" + class_name + ".ret())"
    return res

def writeCode(src):
    if src[-1] == ".":
        src += " "
    wordlist = src.replace(" ", "_")
    wordlist = wordlist.split(".")
    res = ""
    res += writeClass(wordlist)
    res += "\n\n"
    res += writeMain(wordlist)
    return res

if __name__ == "__main__":
    print(writeCode("슈슉.슉.시.시발럼아.슈숙.시.시.시발럼아.슈슉 슈숙.슉.시.시발럼아.슈숙.시.시.시발롬아.슈슉 슈숙.슉.시.시발럼아.슈숙.시.시.시발럼아.슈슉 슈숙.슉.시.시발럼아.슈숙.시.시.시발롬아.슈슉 슈숙.슉.시.시발럼아.슈숙.시.시.시발럼아.슈슉"))
