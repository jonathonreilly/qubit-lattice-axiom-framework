"""Shared helpers for block C4c (own code). Conventions as C4/C4b: O = 24 signed permutation
matrices of det +1; T = even ones (|R| an even permutation)."""
import itertools
import numpy as np

PASS = 0
FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(("PASS " if ok else "FAIL ") + name + ((" :: " + detail) if detail else ""), flush=True)
    return ok


def total():
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}", flush=True)


def build_O():
    out = []
    for p in itertools.permutations(range(3)):
        for s in itertools.product((1, -1), repeat=3):
            M = np.zeros((3, 3), int)
            for i in range(3):
                M[p[i], i] = s[i]
            if round(np.linalg.det(M)) == 1:
                out.append(M)
    return out


O = build_O()
T = [M for M in O if round(np.linalg.det(np.abs(M))) == 1]


def cheb(a, b):
    return int(np.max(np.abs(np.subtract(a, b))))
