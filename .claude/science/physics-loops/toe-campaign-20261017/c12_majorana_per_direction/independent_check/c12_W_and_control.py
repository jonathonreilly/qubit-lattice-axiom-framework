"""(a) Item 5 of the c12 note: the W-dressed realization U_R W, W = prod_v exp(-i pi B_v/4).
    - per-element pair eigenvalue under U_R W (clean creators);
    - group law: does V_g = U_g W^{n(g)} satisfy V_g V_h = V_gh up to fermion parity
      (as automorphisms of the operator algebra), for n = 1 on all g, n = 1 on g != e,
      and n = [sgn(g) = -1]?
    - consequence for eta_f under a consistent twist.
(control for c) the dressing-independence analysis of pairspace.py applied to the c12
    code itself (where single Majoranas are local operators) must detect dependence."""
import itertools, sys
from collections import Counter
import numpy as np
from mpd_core import *
from check4_grouplaw import closure, comp, ID, MINUS, C4, C3, axisC2, edgeC2
import pairspace as ps

L = 10
lat = Lattice(L)
n = lat.n
_LOC = {}
for r in range(7):
    for sub in itertools.combinations(range(6), r):
        P = lat.mono([((0, 0, 0), d) for d in sub])  # site 0 = local bits
        _LOC[(P[0], P[1])] = (sub, P[2])            # gamma_sub = i^k X^x Z^z


def site_bits(P, s):
    return ((P[0] >> (3 * s)) & 7, (P[1] >> (3 * s)) & 7)


def rot_pauli(P, M, eps):
    """exact image of Pauli P under gamma_{v,d} -> eps(d) gamma_{Mv, Md}."""
    sites = set()
    m = P[0] | P[1]
    while m:
        b = m & -m
        sites.add((b.bit_length() - 1) // 3)
        m ^= b
    out = (0, 0, P[2])
    dp = dir_perm(M)
    # P = i^k0 prod_s X^xs Z^zs (X's left of Z's globally = product over sites since sites commute)
    for s in sorted(sites):
        xs, zs = site_bits(P, s)
        sub, k = _LOC[(xs, zs)]
        v = lat.coords(s)
        sgn = 1
        for d in sub:
            sgn *= eps[d]
        W = lat.mono([(apply(M, v), dp[d]) for d in sub])
        add = (W[0], W[1], (W[2] - k + (0 if sgn > 0 else 2)) % 4)
        out = mul(out, add)
    return out


Bz = [lat.to_pauli(lat.B_mono(v))[1] for v in lat.all_sites()]


def phiW(P, power=1):
    """W^p P W^-p with W = prod exp(-i pi B_v/4): each anticommuting B_v gives (-i B_v)^p."""
    for _ in range(power % 4):
        Q = P
        for s, z in enumerate(Bz):
            if anticommute(Q, (0, z, 0)):
                P = mul((0, z, 3), P)
    return P


def phiP(P):
    c = sum(anticommute(P, (0, z, 0)) for z in Bz) % 2
    return (P[0], P[1], (P[2] + 2 * c) % 4)


sec = dict(zip(ORIENTS, (1, 1, 1)))
T = Tableau(n)
for m in lat.generators(sec):
    T.insert(lat.to_pauli(m))
assert T.consistent

pC4, pC3 = dir_perm(C4), dir_perm(C3)
G = None
for e4 in admissible_eps(C4):
    for e3 in admissible_eps(C3):
        Gc = closure([(pC4, e4), (pC3, e3)])
        if len(Gc) == 48 and MINUS in Gc:
            G = Gc
            break
    if G:
        break
lift = {}
for g in G:
    lift.setdefault(g[0], g)          # one lift per rotation
Rs = rotations()
M_of = {dir_perm(M): M for M in Rs}
sgnO = {dir_perm(M): perm_sign(dir_perm(M)) for M in Rs}

# ---- per-element pair eigenvalues -----------------------------------------
def path(x, y):
    labs, cur = [], list(x)
    for a in range(3):
        while cur[a] != y[a]:
            st = 1 if y[a] > cur[a] else -1
            v = list(cur)
            if st < 0:
                v[a] -= 1
            labs += lat.edge_labels(tuple(v), a)
            cur[a] += st
    return labs

print("per-element pair eigenvalue, clean string creators:")
for cls, Ms, x in [("axis", axisC2, (1, 2, 0)), ("edge", edgeC2, (2, 0, 1))]:
    for M in Ms:
        eps = lift[dir_perm(M)][1]
        y = apply(M, x)
        S = lat.mono(path(x, y))
        lamU = T.sign_of(mul(dag(S), rot_pauli(S, M, eps)))
        lamUW = T.sign_of(mul(dag(S), rot_pauli(phiW(S), M, eps)))
        print("  %s C2 %s: lambda(U_R) = %+d   lambda(U_R W) = %+d" % (cls, M, lamU, lamUW))

# ---- group law ---------------------------------------------------------------
tests = [lat.to_pauli((0, lat.edge_labels((0, 0, 0), a))) for a in range(3)] + \
        [lat.to_pauli(lat.B_mono((0, 0, 0)))] + [lat.gamma((1, 0, 0), d) for d in range(6)] + \
        [lat.to_pauli((0, lat.edge_labels((1, 2, 3), 1)))]
even_tests = tests[:4] + tests[-1:]


def phiV(g, P, nfun):
    p = g[0]
    return rot_pauli(phiW(P, nfun(p)), M_of[p], g[1])


def law(nfun, tset):
    bad = 0
    tot = 0
    for p1, p2 in itertools.product(lift, repeat=2):
        g, h = lift[p1], lift[p2]
        gh = comp(g, h)
        gh_l = lift[gh[0]]          # chosen lift of gh (differs from gh by +-1 = P conj)
        lhs = [phiV(g, phiV(h, Q, nfun), nfun) for Q in tset]
        r1 = [phiV(gh_l, Q, nfun) for Q in tset]
        r2 = [phiV(gh_l, phiP(Q), nfun) for Q in tset]
        tot += 1
        if not (lhs == r1 or lhs == r2):
            bad += 1
    return bad, tot

ident = tuple(range(6))
for name, nfun in [("n = 0 (U_g)", lambda p: 0),
                   ("n = 1 for all g (U_g W, incl. identity)", lambda p: 1),
                   ("n = 1 for g != e (U_g W)", lambda p: 0 if p == ident else 1),
                   ("n = [sgn g = -1] (W on C4 and edge C2 only)", lambda p: 1 if sgnO[p] < 0 else 0)]:
    b1, t1 = law(nfun, tests)
    b2, t2 = law(nfun, even_tests)
    print("group law up to (-1)^F, %-45s: failing (g,h) pairs %4d / %d on all test ops; %4d / %d on even ops only"
          % (name, b1, t1, b2, t2))

print("eta_f under the consistent sgn-twist V_g = U_g W^[sgn g=-1]:")
for cls, Ms, x in [("axis", axisC2, (1, 2, 0)), ("edge", edgeC2, (2, 0, 1))]:
    vals = set()
    for M in Ms:
        eps = lift[dir_perm(M)][1]
        y = apply(M, x)
        S = lat.mono(path(x, y))
        pw = 1 if perm_sign(dir_perm(M)) < 0 else 0
        vals.add(-T.sign_of(mul(dag(S), rot_pauli(phiW(S, pw), M, eps))))
    print("  %s C2: eta_f = %s" % (cls, sorted(vals)))

# ---- control for (c): dressed creator space in the c12 code ------------------
print("control: full flux-dressed creator space in the c12 code (window margin 2):")
gens_all = [(("B", v, None), lat.to_pauli(lat.B_mono(v))) for v in lat.all_sites()] + \
           [(("S", v, (a, b)), lat.to_pauli(lat.plaq_mono(v, a, b))) for v in lat.all_sites() for (a, b) in ORIENTS]
nbytes = (n + 7) // 8
def bits(i):
    return np.unpackbits(np.frombuffer(i.to_bytes(nbytes, "little"), np.uint8), bitorder="little")
def linf(p, q):
    return max(abs(p[i] - q[i]) for i in range(3))
def wrapv(p):
    return tuple(((c + L // 2) % L) - L // 2 for c in p)
for cls, M, x in [("axis", axisC2[1], (1, 0, 0)), ("edge", edgeC2[2], (2, 0, 1))]:
    eps = lift[dir_perm(M)][1]
    y = apply(M, x)
    lo = [min(x[i], y[i]) - 2 for i in range(3)]
    hi = [max(x[i], y[i]) + 2 for i in range(3)]
    box = list(itertools.product(*[range(lo[i], hi[i] + 1) for i in range(3)]))
    W = sorted(3 * lat.site(v) + t for v in box for t in range(3))
    Wa = np.array(W)
    ps.comm_row = lambda Q, W_, Wa=Wa: np.concatenate([bits(Q[1])[Wa], bits(Q[0])[Wa]])
    wmask = sum(1 << q for q in W)
    rot = lambda P, M=M, eps=eps: rot_pauli(P, M, eps)
    touching = [(lab, P) for lab, P in gens_all if (P[0] | P[1]) & wmask]
    xs_w = {wrapv(x), wrapv(y)}
    def near(lab):
        v = lab[1]
        a, b = lab[2]
        cs = [v, lat.add(v, DIRS[a]), lat.add(v, DIRS[b]), lat.add(lat.add(v, DIRS[a]), DIRS[b])]
        return any(linf(wrapv(c), u) <= 1 for c in cs for u in xs_w)
    Bflip = lambda lab: 1 if wrapv(lab[1]) in xs_w else 0
    r = ps.analyse(W, touching, near, Bflip, rot, T)
    rc = ps.analyse(W, touching, lambda lab: False, Bflip, rot, T)
    print("  %s C2 %s x=%s: dressed space dim %d, lam0 %+d, F(b)=-1 for %d basis vectors, K offdiag nonzero %d -> constant=%s;"
          " clean-only space: dim %d lam0 %+d constant=%s"
          % (cls, M, x, r["dim"], r["lam0"], r["Fbad"], r["Kbad"], r["constant"], rc["dim"], rc["lam0"], rc["constant"]))
