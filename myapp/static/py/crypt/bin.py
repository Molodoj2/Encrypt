mode = input("number or ascii (N/A)>")
inpmode = input("fixed input or ask input(F/A)>")
inp = input("code>")
data: list[int] = []
IP = 0
DP = 0
BS = []
CS = []
iszero = []
out = ""
if inpmode == "F" or inpmode == "f":
    fixedi = 0
    inputforall = input("fixed input>")
while IP < len(inp):
    tok = inp[IP]
    add = ""
    print(data)
    if DP+1 > len(data)-1:
        data.append(0)
    if len(iszero) == 0:
        if len(CS) == 0:
            if tok == "+":
                data[DP] = data[DP] + 1
            elif tok == "-":
                data[DP] = data[DP] - 1
            elif tok == ">":
                DP = DP + 1
                if DP + 1 > len(data) - 1:
                    while not DP + 1 > len(data) - 1:
                        data.append(0)
            elif tok == "<":
                DP = DP - 1
            elif tok == ",":
                if inpmode == "f" or inpmode == "F":
                    data[DP] = ord(inputforall[fixedi])
                    fixedi = fixedi + 1
                else:
                    if mode == "n" or mode == "N":
                        try:
                            data[DP] = int(input("NUM>"))
                        except:
                            data[DP] = 0
                    else:
                        try:
                            data[DP] = ord(input("CHAR>"))
                        except:
                            data[DP] = 0
            elif tok == ".":
                if mode == "n" or mode == "N":
                    out = out+"\n"+str(data[DP])
                else:
                    out = out+chr(data[DP])
    if len(CS) == 0:
        if tok == "[":
            BS.append(IP)
            if data[DP] == 0:
                iszero.append(0)
    if len(CS) == 0:
        if tok == "]":
            if len(iszero)>0:
                iszero.pop()
            if data[DP] == 0:
                BS.pop()
            else:
                IP = BS[-1]
    if tok == "?":
        if len(CS) > 0:
            if CS[-1][1] == 0:
                IP = CS[-1][0]
            CS.pop()
    elif tok == "/":
        CS.append([IP, data[DP]])
    IP = IP + 1
print(out)
print("info:")
print("data:"+"".join(str(data)))
print("data index:"+str(DP))
print("instruction index:"+str(IP))
