def string_to_analogy(s):
    questions, answers, correct = s.split(",")
    a, b, _, c, _ = questions.split(":")

    ret = [a,b,c,answers.split(),correct]
    print(ret)
    return ret

if __name__ == '__main__':
    print("Preprocessing available")
    string_to_analogy("after:regrets::before:_,thresholds prologues misgivings memories pitfalls,misgivings")
