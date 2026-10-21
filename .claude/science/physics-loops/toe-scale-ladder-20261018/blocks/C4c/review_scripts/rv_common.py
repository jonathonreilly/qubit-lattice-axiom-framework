import itertools, numpy as np
_C = {"P": 0, "F": 0}
def check(name, ok, info=""):
    _C["P" if ok else "F"] += 1
    print(("PASS " if ok else "FAIL ") + name + ((" :: " + str(info)) if info != "" else ""), flush=True)
def total():
    print(f"TOTAL: PASS={_C['P']} FAIL={_C['F']}", flush=True)
def perm_parity(p):
    p = list(p); s = 1
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]: s = -s
    return s
def groups():
    O, T = [], []
    for p in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            M = np.zeros((3, 3), int)
            for i in range(3): M[i, p[i]] = sg[i]
            if round(np.linalg.det(M)) == 1:
                O.append(M)
                if perm_parity(p) == 1: T.append(M)
    return O, T
