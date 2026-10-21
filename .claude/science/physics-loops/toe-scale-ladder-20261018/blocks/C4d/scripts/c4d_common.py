"""Shared helpers for block C4d (own code; does not import C4/C4b/C4c code).
Conventions as C4: O = 24 signed permutation matrices of det +1; T = those whose
underlying permutation |R| is even (|T| = 12).  Sites are integer 3-tuples."""
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
assert len(O) == 24 and len(T) == 12


def cheb(a, b):
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]), abs(a[2] - b[2]))


def add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def rot(R, a):
    v = R @ np.array(a)
    return (int(v[0]), int(v[1]), int(v[2]))


def ball(r, c=(0, 0, 0)):
    return [add(c, d) for d in itertools.product(range(-r, r + 1), repeat=3)]


def dist_set(a, S):
    return min(cheb(a, s) for s in S)


def canon_rho(rho):
    """normalise a relative vector up to sign (lexicographically positive)."""
    m = tuple(-x for x in rho)
    return max(rho, m)


def near_rhos(r):
    out = set()
    for d in itertools.product(range(-r, r + 1), repeat=3):
        if d != (0, 0, 0):
            out.add(canon_rho(d))
    return sorted(out)


def pair(x, y):
    return frozenset((x, y))


def box(p, r):
    """sites within Chebyshev r of both sites of pair p (Lemma K box)."""
    x, y = tuple(p)
    return [s for s in ball(r, x) if cheb(s, y) <= r]


def is_near(p, r):
    x, y = tuple(p)
    return cheb(x, y) <= r
