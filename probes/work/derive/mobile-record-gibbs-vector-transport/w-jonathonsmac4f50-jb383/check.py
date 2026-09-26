#!/usr/bin/env python3
"""Independent check of frozen draft #8567 (Codex) and one explicit three-dimensional candidate.
J:derive:mobile-record-gibbs-vector-transport:a1

K  Part B (1D KLS exchange): the sixteen-word certificate F(a,b,c,d) = h(a,b,c) - h(b,c,d) (symbolic z), and, by a
   different method, exact master-equation stationarity of the Gibbs law on every ring N = 4..9 (all configurations)
P  Part A: the plaquette circulation (1) with Gibbs-weighted rates preserves an arbitrary finite-range Gibbs law, and
   the stationary content current of plaquette circulations plus Metropolis swaps is exactly zero (small exact tori)
C  an explicit 3D candidate: KLS exchanges along x on a 3D torus with Gibbs energy -J sum_x-bonds - Jp sum_transverse.
   Stationary iff Jp = 0 (exact witness for Jp != 0); at Jp = 0 it is a stack of independent chains: transport along x,
   correlations only along x, no cubic covariance -> first failed condition for the research target.
"""
import itertools, random, sys, time
from fractions import Fraction as Fr
import sympy as sp

T0 = time.time()
FAIL = []
def check(name, ok, detail=""):
    print(f"{'PASS' if ok else 'FAIL'} {name}" + (f" :: {detail}" if detail else ""), flush=True)
    if not ok: FAIL.append(name)

print("== K Part B: the KLS certificate")
z = sp.Symbol('z', positive=True); kappa = sp.Symbol('kappa', positive=True)
r = {(0, 0): kappa, (1, 1): kappa, (0, 1): 2*kappa*z/(1 + z), (1, 0): 2*kappa/(1 + z)}
h = {w: 0 for w in [(0, 0, 0), (0, 0, 1), (1, 0, 0)]}
h[(0, 1, 0)] = -kappa
for w in [(0, 1, 1), (1, 1, 0), (1, 1, 1)]: h[w] = -2*kappa/(1 + z)
h[(1, 0, 1)] = kappa*(z - 1)/(1 + z)
okK1 = True
for a, b, c, d in itertools.product((0, 1), repeat=4):
    F = (r[(a, d)]*z**(a - d) if (b, c) == (0, 1) else 0) - (r[(a, d)] if (b, c) == (1, 0) else 0)
    if sp.simplify(F - (h[(a, b, c)] - h[(b, c, d)])) != 0: okK1 = False
check("K1 all sixteen words: F(a,b,c,d) = h(a,b,c) - h(b,c,d) for symbolic z, kappa (the draft's table)", okK1)

def ring_generator_residual(N, zv, lam):
    """exact: max over configurations of |(pi L)(eta)| / pi(eta) for the clockwise KLS exchange on a ring of N sites."""
    zf = Fr(zv); kap = Fr(1)
    rate = {(0, 0): kap, (1, 1): kap, (0, 1): 2*kap*zf/(1 + zf), (1, 0): 2*kap/(1 + zf)}
    def weight(s):
        e = sum(s[i]*s[(i + 1) % N] for i in range(N))
        return zf**e*Fr(lam)**sum(s)
    worst = Fr(0); cur_pos = True
    for s in itertools.product((0, 1), repeat=N):
        out = Fr(0); inflow = Fr(0)
        for i in range(N):
            j = (i + 1) % N
            a, d = s[(i - 1) % N], s[(j + 1) % N]
            if s[i] == 1 and s[j] == 0:                       # 10 -> 01 clockwise, out of s
                out += rate[(a, d)]
            if s[i] == 0 and s[j] == 1:                       # predecessor had 10 here
                t = list(s); t[i], t[j] = 1, 0
                inflow += weight(t)*rate[(a, d)]
        res = inflow - weight(s)*out
        worst = max(worst, abs(res))
    return worst
okK2 = True
for N in range(4, 10):
    for zv, lam in ((Fr(2), Fr(1)), (Fr(1, 3), Fr(3, 2)), (Fr(5, 2), Fr(2, 7))):
        if ring_generator_residual(N, zv, lam) != 0: okK2 = False
check("K2 exact master-equation stationarity of the Gibbs law on every configuration of rings N = 4..9 "
      "(z in {2, 1/3, 5/2}, three fugacities) - a different method from the word certificate", okK2)
# current positivity on a finite ring
def ring_current(N, zv):
    zf = Fr(zv); rate = {(0, 0): 1, (1, 1): 1, (0, 1): 2*zf/(1 + zf), (1, 0): 2/(1 + zf)}
    Z = Fr(0); J = Fr(0)
    for s in itertools.product((0, 1), repeat=N):
        w = zf**sum(s[i]*s[(i + 1) % N] for i in range(N))
        Z += w
        if s[0] == 1 and s[1] == 0: J += w*rate[(s[N - 1], s[2])]
    return J/Z
cur = ring_current(8, Fr(2))
check("K3 the class-1 clockwise current per bond is strictly positive (N = 8, z = 2, grand law at fugacity 1)", cur > 0, str(cur))
# transfer-matrix covariance (5): nearest-neighbour covariance nonzero for J != 0
Jv, mv = sp.Rational(1, 2), sp.Rational(1, 3)
T = sp.Matrix([[sp.exp(mv*0), sp.exp(mv/2)], [sp.exp(mv/2), sp.exp(Jv + mv)]])
check("K4 det T = e^mu (e^J - 1) != 0 for J != 0, so u = Lambda2/Lambda != 0 and Cov(sigma_0, sigma_1) != 0",
      sp.simplify(T.det() - sp.exp(mv)*(sp.exp(Jv) - 1)) == 0 and T.det() != 0)

print("== P Part A: plaquette circulation")
random.seed(8567)
def part_A_stationarity():
    """sites 0..3 a plaquette (cyclic), sites 4,5 exterior; 3 labels; random pair interactions touching the plaquette."""
    labels = range(3); sites = range(6)
    pairs = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 4), (1, 4), (2, 5), (3, 5), (4, 5)]
    Phi = {p: {(x, y): Fr(random.randint(-4, 4), 3) for x in labels for y in labels} for p in pairs}
    single = {s: {x: Fr(random.randint(-3, 3), 2) for x in labels} for s in sites}
    def H(eta): return sum(Phi[p][(eta[p[0]], eta[p[1]])] for p in pairs) + sum(single[s][eta[s]] for s in sites)
    def HS(eta): return sum(Phi[p][(eta[p[0]], eta[p[1]])] for p in pairs if p[0] < 4 or p[1] < 4) + sum(single[s][eta[s]] for s in range(4))
    # exact exponentials are avoided by working with weights w = exp(-H) as symbols? use rational energies and base e -> use sympy exp
    import math
    states = list(itertools.product(labels, repeat=6))
    E = {s: sp.exp(-H(s)) for s in states}
    def R(eta): return (eta[3], eta[0], eta[1], eta[2], eta[4], eta[5])      # x_i -> x_{i+1}
    def Rinv(eta): return (eta[1], eta[2], eta[3], eta[0], eta[4], eta[5])
    def chi(eta): return Fr(sum(1 if eta[i] == 1 else (-1 if eta[i] == 2 else 0) for i in range(4)), 4)   # orbit invariant
    eps = Fr(1, 3)
    def rp(eta): return (1 + eps*chi(eta))*sp.exp(HS(eta))
    def rm(eta): return (1 - eps*chi(eta))*sp.exp(HS(eta))
    worst = 0
    for s in random.sample(states, 150):
        inflow = E[Rinv(s)]*rp(Rinv(s)) + E[R(s)]*rm(R(s))       # from R^-1 s by +, from R s by -
        out = E[s]*(rp(s) + rm(s))
        val = sp.simplify(inflow - out)
        if val != 0: worst = val
    return worst == 0
check("P1 the plaquette circulation with a_+- = nu(1 +- eps chi), chi orbit-invariant, and rates a exp(H_S) is stationary "
      "for a random finite-range Gibbs law (exact, 150 random states of a 6-site system with 3 labels)", part_A_stationarity())

def part_A_current():
    """2D 3x3 torus, 2 labels: all plaquette circulations (+ and -) and Metropolis nearest-neighbour swaps; exact
    stationary label current (unwrapped displacement) in the Gibbs law is zero."""
    L = 3; sites = [(i, j) for i in range(L) for j in range(L)]; idx = {s: k for k, s in enumerate(sites)}
    zK = Fr(3, 2)                                  # weight factor per like-bond: pi ~ zK^(#like bonds)
    bonds = [(idx[(i, j)], idx[((i + 1) % L, j)]) for i, j in sites] + [(idx[(i, j)], idx[(i, (j + 1) % L)]) for i, j in sites]
    plaq = [[idx[(i, j)], idx[((i + 1) % L, j)], idx[((i + 1) % L, (j + 1) % L)], idx[(i, (j + 1) % L)]] for i, j in sites]
    disp = {}   # unwrapped displacement between neighbouring sites
    for (a, b) in bonds: pass
    def dvec(a, b):
        (ia, ja), (ib, jb) = sites[a], sites[b]
        di = (ib - ia + 1) % L - 1; dj = (jb - ja + 1) % L - 1
        return (di, dj)
    def weight(s): return zK**sum(1 for a, b in bonds if s[a] == s[b])
    J = [Fr(0), Fr(0)]
    for s in itertools.product((0, 1), repeat=L*L):
        if sum(s) != 4: continue
        w = weight(s)
        # plaquette circulations: rate = exp(H_S) * a ; with H = -log zK * #like bonds, exp(H_S) = zK^(-#like bonds touching S)
        for P in plaq:
            touch = [bd for bd in bonds if bd[0] in P or bd[1] in P]
            eHS = zK**(-sum(1 for a, b in touch if s[a] == s[b]))
            for direction in (1, -1):
                t = list(s)
                for k in range(4):
                    t[P[(k + direction) % 4]] = s[P[k]]
                if tuple(t) == s: continue
                rate = eHS*(Fr(3, 2) if direction == 1 else Fr(1, 2))     # a_+ != a_- : irreversible
                for k in range(4):
                    if s[P[k]] == 1:
                        dv = dvec(P[k], P[(k + direction) % 4])
                        J[0] += w*rate*dv[0]; J[1] += w*rate*dv[1]
        for a, b in bonds:
            if s[a] == s[b]: continue
            t = list(s); t[a], t[b] = s[b], s[a]
            rate = min(Fr(1), weight(tuple(t))/w)
            dv = dvec(a, b) if s[a] == 1 else dvec(b, a)
            J[0] += w*rate*dv[0]; J[1] += w*rate*dv[1]
    return J
Jc = part_A_current()
check("P2 3x3 torus, 4 records of class 1: stationary class-1 current of irreversible plaquette circulations plus "
      "Metropolis swaps is exactly zero (unwrapped displacement)", Jc == [0, 0], str(Jc))

print("== C an explicit three-dimensional candidate: KLS along x with transverse coupling")
def kls3d_residual(Lx, Ly, Lz, zx, zp, lam, state):
    """exact stationarity residual (pi L)(state) for the Gibbs law pi ~ zx^(x-like11 bonds) zp^(transverse 11 bonds) lam^N
    under clockwise-in-x KLS exchanges with the 1D heat-bath rates (depending on x-neighbours only)."""
    sites = list(itertools.product(range(Lx), range(Ly), range(Lz)))
    idx = {s: k for k, s in enumerate(sites)}
    def nb(s, ax, d):
        t = list(s); t[ax] = (t[ax] + d) % (Lx, Ly, Lz)[ax]; return idx[tuple(t)]
    xb = [(idx[s], nb(s, 0, 1)) for s in sites]
    tb = [(idx[s], nb(s, ax, 1)) for s in sites for ax in (1, 2) if (Ly, Lz)[ax - 1] > 1]
    rate = {(0, 0): Fr(1), (1, 1): Fr(1), (0, 1): 2*zx/(1 + zx), (1, 0): 2/(1 + zx)}
    def weight(c):
        return zx**sum(c[a]*c[b] for a, b in xb)*zp**sum(c[a]*c[b] for a, b in tb)*lam**sum(c)
    out = Fr(0); inflow = Fr(0); c = state
    for s in sites:
        i, j = idx[s], nb(s, 0, 1)
        a, d = c[nb(s, 0, -1)], c[nb(sites[j], 0, 1)]
        if c[i] == 1 and c[j] == 0: out += rate[(a, d)]
        if c[i] == 0 and c[j] == 1:
            t = list(c); t[i], t[j] = 1, 0
            inflow += weight(tuple(t))*rate[(a, d)]
    return inflow - weight(c)*out
Lx, Ly, Lz = 4, 2, 2
n = Lx*Ly*Lz
allstates = [s for s in itertools.product((0, 1), repeat=n) if sum(s) == 8]
zx, lam = Fr(2), Fr(1)
ok0 = all(kls3d_residual(Lx, Ly, Lz, zx, Fr(1), lam, s) == 0 for s in allstates)
check(f"C1 transverse coupling Jp = 0 (zp = 1): the Gibbs law is stationary on every one of the {len(allstates)} "
      "configurations with 8 records on the 4x2x2 torus (independent chains)", ok0)
wit = None
for s in allstates:
    res = kls3d_residual(Lx, Ly, Lz, zx, Fr(3), lam, s)
    if res != 0: wit = (s, res); break
check("C2 transverse coupling Jp != 0 (zp = 3): exact nonzero stationarity residual at an explicit configuration "
      "(the candidate's first failed condition)", wit is not None, f"state {wit[0]} residual {wit[1]}" if wit else "")
# at Jp = 0: correlations only along x; transverse covariance zero (independent chains), and the drive selects x
print("   C3 (PROVED in ATTEMPT, not a finite check): at Jp = 0 the grand Gibbs weight factorises over the Ly*Lz x-chains, so "
      "transverse covariances vanish in the grand law, and the drive along +x is not invariant under exchanging axes")

print(f"== done in {time.time()-T0:.0f}s")
if FAIL:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAIL))
else:
    print("SUMMARY: PARTIAL (independent verification, no new result): #8567 Part B's sixteen-word KLS certificate holds "
          "(symbolic) and exact master-equation stationarity holds on all rings N = 4..9; Part A's plaquette circulation "
          "preserves a random finite-range Gibbs law and its stationary content current vanishes exactly (3x3 torus). "
          "Explicit 3D candidate (KLS along x, transverse coupling Jp): Gibbs-stationary iff Jp = 0 (exact witness), and at "
          "Jp = 0 it is a stack of independent chains with no transverse correlation and no cubic covariance - first failed "
          "condition for the research target")
