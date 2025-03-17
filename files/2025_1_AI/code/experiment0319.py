def is_complement(lit1, lit2):
    """判断两个文字是否互补"""
    if lit1.startswith('¬'):
        return lit1[1:] == lit2
    elif lit2.startswith('¬'):
        return lit2[1:] == lit1
    else:
        return False

def resolve(c1, c2):
    """生成两个子句的所有可能归结式"""
    resolvents = []
    for l1 in c1:
        for l2 in c2:
            if is_complement(l1, l2):
                new_clause = (c1 - {l1}) | (c2 - {l2})
                new_clause = frozenset(new_clause)
                resolvents.append(new_clause)
                # 如果生成空子句，直接返回
                if not new_clause:
                    return resolvents
    return resolvents

def resolution(kb, query):
    """命题逻辑归结推理系统"""
    clauses = set()
    # 将知识库的子句转换为frozenset
    for clause in kb:
        clauses.add(frozenset(clause))
    # 处理查询的否定，转换为子句
    negated = []
    for lit in query:
        if lit.startswith('¬'):
            negated.append(frozenset({lit[1:]}))
        else:
            negated.append(frozenset({'¬' + lit}))
    # 将否定后的查询加入子句集
    for clause in negated:
        clauses.add(clause)
    
    steps = []
    while True:
        new_clauses = set()
        clause_list = list(clauses)
        # 遍历所有可能的子句对
        for i in range(len(clause_list)):
            for j in range(i + 1, len(clause_list)):
                c1 = clause_list[i]
                c2 = clause_list[j]
                resolvents = resolve(c1, c2)
                for res in resolvents:
                    if res not in clauses and res not in new_clauses:
                        new_clauses.add(res)
                        steps.append( (c1, c2, res) )
                        # 如果生成空子句，直接返回成功
                        if not res:
                            steps.append("Contradiction found! 命题得证。")
                            return True, steps
        # 没有新子句生成，无法证明
        if not new_clauses:
            steps.append("无法生成新的子句，命题无法证明。")
            return False, steps
        # 将新子句加入集合
        clauses.update(new_clauses)

def print_steps(steps):
    """打印归结过程"""
    for step in steps:
        if isinstance(step, tuple):
            c1, c2, res = step
            print(f"归结 {set(c1)} 和 {set(c2)}，生成 {set(res)}")
        else:
            print(step)

# 示例测试
if __name__ == "__main__":
    # 示例1：知识库包含 A∨¬B 和 B，查询 A 是否成立
    kb = [{'A', '¬B'}, {'A'}]
    query = {'A'}
    print("示例1：")
    success, steps = resolution(kb, query)
    print_steps(steps)
    print("结论：" + ("命题成立" if success else "命题不成立"))
    print("\n")

    # 示例2：无法证明的情况
    kb = [{'A'}, {'¬B'}]
    query = {'C'}
    print("示例2：")
    success, steps = resolution(kb, query)
    print_steps(steps)
    print("结论：" + ("命题成立" if success else "命题不成立"))