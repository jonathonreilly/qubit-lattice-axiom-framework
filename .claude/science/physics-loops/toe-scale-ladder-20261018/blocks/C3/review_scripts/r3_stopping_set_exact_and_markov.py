"""R3: (i) exact finite check of the B2 stopping-set resampling, with ties;
(ii) negative control: Anc(x) without its boundary is NOT a stopping set and
the resampled field then has the wrong law; (iii) exact covariance and the
B2 inequality; (iv) C5: graphical construction vs exact Markov jump-chain
final law on a 3-site path (exact recursion vs Monte Carlo, 4 SE).
Graph for (i)-(iii): path 0-1-2-3, T uniform on {1,2,3} (atoms -> ties),
U in {0,1}; rule: xi = own bit if no strictly earlier neighbour, else
1 + (sum of earlier-neighbour records) mod 2 (zeros allowed, deterministic).
"""
import itertools, random, math
from fractions import Fraction as F
from collections import Counter
from rv_common import Checks
C = Checks("r3")
N = 4
NB = {i: [j for j in (i-1, i+1) if 0 <= j < N] for i in range(N)}
vals = [(t, u) for t in (1, 2, 3) for u in (0, 1)]
OM = list(itertools.product(vals, repeat=N))
p1 = F(1, len(vals)); pw = p1**N

def anc(om, x):
    A = {x}; st = [x]
    while st:
        y = st.pop()
        for z in NB[y]:
            if om[z][0] < om[y][0] and z not in A:
                A.add(z); st.append(z)
    return A

def S(om, A):
    s = set()
    for x in A:
        a = anc(om, x); s |= a
        for y in a: s |= set(NB[y])
    return frozenset(s)

def Sanc_only(om, A):
    s = set()
    for x in A: s |= anc(om, x)
    return frozenset(s)

def rec(om):
    r = {}
    for x in sorted(range(N), key=lambda i: om[i][0]):
        e = [r[y] for y in NB[x] if om[y][0] < om[x][0]]
        r[x] = (1 + sum(e)) % 2 if e else om[x][1]
    return r

A, B = [0], [3]
SA = {om: S(om, A) for om in OM}
SB = {om: S(om, B) for om in OM}
SAo = {om: Sanc_only(om, A) for om in OM}
R = {om: rec(om) for om in OM}
# stopping-set property
stop_ok = all(all(SA[om2] == SA[om] for om2 in OM if all(om2[i] == om[i] for i in SA[om])) for om in OM[::37])
C.ok("S_A = Anc U boundary: {S_A=S} determined by omega|_S (sampled exhaustively on every 37th omega)", stop_ok)
law_star = Counter(); law_bad = Counter()
Efg = F(0); Ef = F(0); Eg = F(0); disagree = F(0); Ecoupled = F(0); Eindep = F(0)
fA = lambda om: R[om][0]; gB = lambda om: R[om][3]
same_SA = True; same_xiA = True; same_B_when_disjoint = True
for om in OM:
    Ef += pw*fA(om); Eg += pw*gB(om); Efg += pw*fA(om)*gB(om)
for om in OM:
    s, so = SA[om], SAo[om]
    for om2 in OM:
        st = tuple(om[i] if i in s else om2[i] for i in range(N))
        bd = tuple(om[i] if i in so else om2[i] for i in range(N))
        law_star[st] += pw*pw; law_bad[bd] += pw*pw
        if SA[st] != s: same_SA = False
        if R[st][0] != R[om][0]: same_xiA = False
        disj = not (s & SB[om2])
        if disj and R[st][3] != R[om2][3]: same_B_when_disjoint = False
        if not disj: disagree += pw*pw
        Ecoupled += pw*pw*fA(om)*gB(st); Eindep += pw*pw*fA(om)*gB(om2)
C.ok("omega* (omega on S_A, omega' elsewhere) has exactly the law of omega", all(law_star[o] == pw for o in OM) and len(law_star) == len(OM))
C.ok("S_A(omega*) = S_A(omega) and xi_A(omega*) = xi_A(omega) for every pair", same_SA and same_xiA)
C.ok("if S_A(omega) and S_B(omega') are disjoint then xi_B(omega*) = xi_B(omega')", same_B_when_disjoint)
C.ok("E f(xi_A(w)) g(xi_B(w*)) = E fg exactly", Ecoupled == Efg)
C.ok("E f(xi_A(w)) g(xi_B(w')) = Ef Eg exactly", Eindep == Ef*Eg)
cov = Efg - Ef*Eg
C.ok(f"|Cov| = {abs(cov)} <= P(S_A(w) meets S_B(w')) = {disagree} (||f||=||g||=1, f,g in {{0,1}} so factor 1 suffices; 2x stated)", abs(cov) <= disagree)
bad = sum(1 for o in OM if law_bad[o] != pw)
C.ok(f"negative control: resampling outside Anc(x) only (no boundary) gives a WRONG law ({bad} atoms differ)", bad > 0)

# (iv) C5: 3-site path, rates lambda(eta) = 1 + (kappa-1)*[#formed nbrs with content 1]/2, contents XOR / coin
kappa = 3
NB3 = {0: [1], 1: [0, 2], 2: [1]}
def lam(state, x):
    f = [state[y] for y in NB3[x] if state[y] is not None]
    return F(1) + F(kappa-1)*F(sum(f), 2), f
def content_law(f):
    if f:
        v = 0
        for s in f: v ^= s
        return {v: F(1)}
    return {0: F(1, 2), 1: F(1, 2)}
from functools import lru_cache
@lru_cache(None)
def final(state):
    blanks = [x for x in range(3) if state[x] is None]
    if not blanks: return {state: F(1)}
    rates = {x: lam(state, x) for x in blanks}
    tot = sum(r for r, f in rates.values())
    out = Counter()
    for x, (r, f) in rates.items():
        for v, q in content_law(f).items():
            ns = list(state); ns[x] = v
            for fs, pr in final(tuple(ns)).items():
                out[fs] += r/tot*q*pr
    return dict(out)
exact = final((None, None, None))
C.ok("exact jump-chain final law normalised", sum(exact.values()) == 1)
rng = random.Random(7)
lmax = kappa
M = 40000; cnt = Counter()
for _ in range(M):
    ev = []
    for x in range(3):
        t = 0.0
        while True:
            t += rng.expovariate(lmax); V, U = rng.random(), rng.random(); ev.append((t, x, V, U))
            if V <= 1/kappa: break
    ev.sort(); st = [None]*3
    for t, x, V, U in ev:
        if st[x] is not None: continue
        r, f = lam(st, x)
        if V <= float(r)/lmax:
            if f:
                v = 0
                for s in f: v ^= s
            else: v = 1 if U < 0.5 else 0
            st[x] = v
    cnt[tuple(st)] += 1
worst = 0.0
for s, p in exact.items():
    ph = cnt[s]/M; se = math.sqrt(float(p)*(1-float(p))/M)
    worst = max(worst, abs(ph-float(p))/se)
C.ok(f"graphical construction final law matches exact Markov jump chain on P3, kappa=3 (worst |z| = {worst:.2f} <= 4)", worst <= 4 and sum(cnt.values()) == M)
C.done()
