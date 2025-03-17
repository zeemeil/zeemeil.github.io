S=[]
# 读取子句集文件中子句，并存放在$列表中
# 一每个子句也是以列表形式存储
# -以析取式分
# 例如：~pV~qVr存储形式为['~p,~q,’r]
def readClauseSet (filePath):
    global S
    for line in open(filePath,mode ='r',encoding ='utf-8'):
        line = line.replace(' ','').strip()
        line = line.split('V')
        S.append (line)
        
# 一为正文字，则返回其负文字
# 为负文字，则返回其正文字

def opposite(clause):
    if '~' in clause:
        return clause.replace('~','')
    else:
        return '~' + clause
    
    
# 逻辑命题归结
def resolution():
    global S
    end = False
    while True:
        if end: break
        # father = S.pop()
        father = S
        for i in father[:]: 
            if end:break
            for mother in S[:]:
                if end:break
                j=list(filter(lambda x:x == opposite(i),mother))
                if j == []:
                    continue
                else:
                    print('\ni亲本子句：'+'V',join(father)+'和'+'V',join(mother))
                    father.remove (i)
                    mother.remove(j[0])
                    if (father ==[] and mother ==[]):
                        print('归结式：NIL')
                        end = True
                    elif father ==[]:
                        print('归结式：'+'V'.join(mother))
                    elif mother ==[]:
                        print('归结式：'+'V',join(mother))
                    else:
                        print('归结式：'+'V'.join(father)+'V'+'V'.join(mother))

if __name__ == "__main__":

    filePath = './input1.txt'
    readClauseSet(filePath)
    resolution()