"""C4d-07: range-1 k-clique walks (k = 2..8), exact single-term deduction.

Reduction (NOTE, Lemma D): for a range-r U(1) QCA with frozen singles, if U is diagonal on all
configurations of size <= k then it is diagonal on every (k+1)-configuration that is NOT an
r-clique (diameter > r).  So U is diagonal iff every clique walk W_k (U restricted to the span of
k-cliques, which it preserves) is diagonal.  At r = 1 the cliques are the subsets of unit cubes, k<=8.

This script assumes P(k-1) (U diagonal on <= k-1 magnons; proved for k-1 = 1 by C4b Lemma 2 and
for k-1 >= 2 by the previous run of this script) and derives constraints on W_k from
  (U)  unitarity of W_k on the clique space;
  (S)  isometry of U on the KNOWN (k+1)-configurations: X = Y u {w} with w at distance > r from Y:
       U X = (W_k Y) (x) w   if Y is a k-clique   (spectator lemma)
       U X = phase * X       if Y is not a clique (P(k-1) + reduction)
  (Sd) the same for U^dagger (W_k^dagger; alpha^-1 has the same range).
Deduction: a constraint whose only surviving term is m|x|^2 or c*x (c a nonzero known constant)
forces x = 0.  Unknowns are keyed by the orbit of (Y', Y) under G x Z^3.
Usage: python3 c4d_07_clique_walks.py k [T|O]"""
import sys, itertools, time
import numpy as np
from c4d_common import check, total, T, O, cheb, add, sub, ball

k = int(sys.argv[1]); gname = sys.argv[2] if len(sys.argv) > 2 else "T"
G = {"T": T, "O": O}[gname]
r = 1
t0 = time.time()


def diam_ok(S):
    S = list(S)
    return all(cheb(a, b) <= r for a, b in itertools.combinations(S, 2))


def box(S):
    S = list(S)
    lo = [max(s[i] for s in S) - r for i in range(3)]
    hi = [min(s[i] for s in S) + r for i in range(3)]
    return [p for p in itertools.product(*[range(lo[i], hi[i] + 1) for i in range(3)])]


_cliq_cache = {}


def cliques_in_box(Y):
    """k-cliques inside box(Y) (support of W_k|Y>, Lemma K generalised)."""
    Yf = frozenset(Y)
    if Yf in _cliq_cache:
        return _cliq_cache[Yf]
    B = box(Y)
    out = [frozenset(c) for c in itertools.combinations(B, len(Y)) if diam_ok(c)]
    _cliq_cache[Yf] = out
    return out


def norm(S):
    m = min(S)
    return tuple(sorted(sub(s, m) for s in S))


Gm = [np.array(R) for R in G]


def key(Yp, Y):
    best = None
    for R in Gm:
        a = [tuple(int(v) for v in R @ np.array(s)) for s in Y]
        b = [tuple(int(v) for v in R @ np.array(s)) for s in Yp]
        m = min(a)
        kk = (tuple(sorted(sub(s, m) for s in a)), tuple(sorted(sub(s, m) for s in b)))
        if best is None or kk < best:
            best = kk
    return best


_key_cache = {}


def K(Yp, Y):
    t = (Yp, Y)
    if t not in _key_cache:
        _key_cache[t] = key(Yp, Y)
    return _key_cache[t]


# translation classes of k-cliques (lexmin at origin)
cube = list(itertools.product((0, 1), repeat=3))
classes = set()
for c in itertools.combinations(cube, k):
    classes.add(norm(c))
classes = [frozenset(c) for c in sorted(classes)]
print(f"[k={k},{gname}] clique translation classes: {len(classes)}", flush=True)
allkeys = set()
for Y in classes:
    for Yp in cliques_in_box(Y):
        allkeys.add(K(Yp, Y))
stay = {K(Y, Y) for Y in classes}
print(f"[k={k},{gname}] unknowns (orbit-keyed amplitudes): {len(allkeys)}, stay: {len(stay)}", flush=True)


def far(w, Y):
    return all(cheb(w, y) > r for y in Y)


def Wcol(Y, adj):
    """symbolic W_k|Y> (adj: W_k^dag|Y>) : dict Y' -> (key, conjflag)."""
    out = {}
    for Yp in cliques_in_box(Y):
        out[Yp] = (K(Yp, Y), False) if not adj else (K(Y, Yp), True)
    return out


def known_image(X, adj):
    """known image of a (k+1)-configuration X (forward or backward), or None if unknown.
    returns ('sym', Y, w) for clique+spectator, ('diag',) for diagonal, None otherwise."""
    for w in X:
        Y = X - {w}
        if far(w, Y):
            if diam_ok(Y):
                return ("sym", Y, w)
            return ("diag",)
    return None


constraints = []   # list of dict term -> count ; term = (lit1, lit2) with lit = ('one',) or (key, conj)


def lit_conj(l):
    return l if l[0] == "one" else (l[0], not l[1])


def add_term(d, l1c, l2):
    t = tuple(sorted([l1c, l2], key=repr))
    d[t] = d.get(t, 0) + 1


# (U) unitarity of W_k : <W Y1 | W Y2> = 0, Y1 anchored class, Y2 any clique with overlapping image
for Y1 in classes:
    c1 = Wcol(Y1, False)
    cand = set()
    for Z in c1:
        for Y2 in cliques_in_box(Z):
            if Y2 != Y1:
                cand.add(Y2)
    for Y2 in cand:
        c2 = Wcol(Y2, False)
        d = {}
        for Z, a1 in c1.items():
            if Z in c2:
                add_term(d, lit_conj(a1), c2[Z])
        if d:
            constraints.append(("U", Y1, Y2, d))
print(f"[k={k},{gname}] unitarity constraints: {len(constraints)}  ({time.time()-t0:.0f}s)", flush=True)

# (S)/(Sd)
nS = 0
for adj in (False, True):
    for Y1 in classes:
        c1 = Wcol(Y1, adj)
        B1 = box(Y1)
        wset = set()
        for b in B1:
            for w in ball(r, b):
                if far(w, Y1):
                    wset.add(w)
        for w1 in sorted(wset):
            X1 = Y1 | {w1}
            acc = {}  # X2 -> term dict
            for Yp, a1 in c1.items():
                Z = Yp | {w1}
                for w2 in Z:
                    Ypp = Z - {w2}
                    if diam_ok(Ypp):
                        for Y2 in cliques_in_box(Ypp):
                            if not far(w2, Y2):
                                continue
                            X2 = Y2 | {w2}
                            if X2 == X1:
                                continue
                            a2 = (K(Ypp, Y2), False) if not adj else (K(Y2, Ypp), True)
                            add_term(acc.setdefault(X2, {}), lit_conj(a1), a2)
                    else:
                        if far(w2, Ypp) and Z != X1:
                            add_term(acc.setdefault(Z, {}), lit_conj(a1), ("one",))
            for X2, d in acc.items():
                constraints.append(("Sd" if adj else "S", X1, X2, d))
                nS += 1
print(f"[k={k},{gname}] spectator constraints: {nS}  ({time.time()-t0:.0f}s)", flush=True)

# deduction
zero = set()
order = []
changed = True
while changed:
    changed = False
    for ci, (kind, A, B, d) in enumerate(constraints):
        live = {}
        for t, c in d.items():
            if any(l[0] != "one" and l[0] in zero for l in t):
                continue
            live[t] = c
        if len(live) != 1:
            continue
        (t, c), = live.items()
        l1, l2 = t
        kk = None
        if l1[0] == "one" and l2[0] != "one":
            kk = l2[0]
        elif l2[0] == "one" and l1[0] != "one":
            kk = l1[0]
        elif l1[0] == l2[0] and l1[1] != l2[1]:
            kk = l1[0]
        if kk is not None and kk not in zero:
            if kk in stay:
                print("!! stay amplitude forced to zero by", kind, sorted(A), sorted(B))
            zero.add(kk); order.append((kk, ci)); changed = True
rest = allkeys - zero
print(f"[k={k},{gname}] forced zeros: {len(zero)}; surviving: {len(rest)}  ({time.time()-t0:.0f}s)", flush=True)
check(f"[k={k},{gname}] no stay amplitude is forced to zero (diagonal W_k stays allowed)", not (stay & zero))
check(f"[k={k},{gname}] every non-stay amplitude of W_k is forced to zero (W_k diagonal)", rest == stay,
      f"{len(rest - stay)} non-stay survivors")
if rest - stay:
    for kk in sorted(rest - stay)[:10]:
        print("   survivor:", kk)
for kk, ci in order[:3]:
    kind, A, B, d = constraints[ci]
    print("   e.g.", kk, "<-", kind, sorted(A), sorted(B))
total()
