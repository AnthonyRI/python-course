stack =[]

def eval_forth(file):
    res = ""
    fl = open(file)
    ch = fl.readlines()
    for line in ch:
        word = str.split(line)
        if word[0] == 'add':
            try:
                while stack[1]:
                    if (isinstance(int(stack[0]), int)) is True and (isinstance(int(stack[1]), int)) is True:
                        #if stack[0] == int and stack[1] == int:
                        stack.append(int(stack.pop(0))+int(stack.pop(0)))
            except:
                pass
        elif word[0] == 'put':
            if (isinstance(int(word[1]), int)) is True:
            #if word[1] == int:
                stack.append(word[1])
            elif (isinstance(word[1], str)) is True:
            #elif word[1] == str:
                res = word[1].replace("'", "")
                res = res.replace('"', '')
                stack.append(repr(res))
        elif word[0] == 'pop':
            stack.pop(0)
        elif word[0] == 'print':
            print stack[0]
        elif word[0] == 'sub':
            try:
                while stack[1]:
                    if (isinstance(int(stack[0]), int)) is True and (isinstance(int(stack[1]), int)) is True:
                        #if stack[0] == int and stack[1] == int:
                        stack.append(int(stack.pop(0))-int(stack.pop(0)))
            except:
                pass
        elif word[0][0] == '#':
            pass
        else:
            raise "Syntax Error - wrong operator", word[0]


eval_forth('sample.frt')