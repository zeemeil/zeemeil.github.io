
S = []

def readClauseSet(filePath):
    global S
    S = []  # 清空之前的子句集
    for line in open(filePath, mode='r', encoding='utf-8'):
        line = line.replace(' ', '').strip()  # 修正空格处理
        if line:
            clause = line.split('V')
            S.append(clause)

def opposite(literal):
    if literal.startswith('~'):
        return literal[1:]
    else:
        return '~' + literal

def resolution():
    global S
    used_pairs = set()  # 记录已处理的子句对避免重复
    new_clauses = []    # 存储新生成的子句
    
    while True:
        new_added = False
        # 遍历所有可能的子句对
        for i in range(len(S)):
            for j in range(len(S)):
                if i == j:
                    continue  # 不自归结
                clause1 = S[i]
                clause2 = S[j]
                pair_key = frozenset((i, j))  # 使用集合避免顺序影响
                if pair_key in used_pairs:
                    continue
                used_pairs.add(pair_key)
                
                # 遍历子句1中的每个文字
                for lit1 in clause1:
                    # 寻找子句2中的互补文字
                    for lit2 in clause2:
                        if opposite(lit1) == lit2:
                            # 生成归结式
                            resolvent = []
                            # 添加子句1中非lit1的文字
                            for lit in clause1:
                                if lit != lit1:
                                    resolvent.append(lit)
                            # 添加子句2中非lit2的文字
                            for lit in clause2:
                                if lit != lit2:
                                    resolvent.append(lit)
                            # 去重
                            resolvent = list(set(resolvent))
                            # 检查是否为空子句
                            if not resolvent:
                                print(f"\n归结 {clause1} 和 {clause2}，生成 NIL")
                                print("矛盾，命题得证！")
                                return True
                            # 检查是否已存在
                            if resolvent not in S + new_clauses:
                                print(f"\n归结 {clause1} 和 {clause2}，生成 {resolvent}")
                                new_clauses.append(resolvent)
                                new_added = True
        
        # 将新子句加入集合
        S += new_clauses
        new_clauses.clear()
        # 若未生成新子句则无法证明
        if not new_added:
            print("无法生成新的子句，命题不成立。")
            return False

if __name__ == "__main__":
    filePath = 'input1.txt'
    readClauseSet(filePath)
    print("初始子句集：", S)
    result = resolution()
    print("结论：命题成立" if result else "结论：命题不成立")