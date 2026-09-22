"""the-fall-from-the-ledgers-consistency, attempt a2 (w-jonathonsmac4f50-j5024).  Exact: Fractions, Gaussian rationals, sympy.

Clocked walk (block 54): H_w = phi H phi, phi = sqrt(w), u = log w, H = sum_a sigma_a S_a.  Momentum density pi_j = Re psi^dag S_j psi;
bond current J_a^j[chi] (block 63) of a state chi; C_j[v] the symmetric hop along j weighted by the bond function v (block 63).
Energy density e_x = Re psi^dag(x) (H_w psi)(x) = d<H_w>/du_x (block 55).  Ledger F = sum_x w_x D_x (block 60), D_x a function of the
plaquette curls of the bond strains (block 64).
"""
import itertools
import os
import random
import sys
from fractions import Fraction as F

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gauss_lattice import G, I, MINUS_I_HALF, Torus, inner, sig

RESULTS = []


def want(label, ok, detail=""):
    RESULTS.append((label, bool(ok)))
    print(("PASS " if ok else "FAIL ") + label + ((" :: " + str(detail)) if detail != "" else ""), flush=True)


def smul(f, v):          # multiply a spinor field by a real scalar field v
    return [(a[0] * c, a[1] * c) for a, c in zip(f, v)]


def add(f, g):
    return [(a[0] + b[0], a[1] + b[1]) for a, b in zip(f, g)]


def C_apply(T, a, v, f):
    fp, fm = T.shift(f, a, 1), T.shift(f, a, -1)
    vm = T.shift(v, a, -1)
    return [((v[n] * fp[n][0] + vm[n] * fm[n][0]) * F(1, 2), (v[n] * fp[n][1] + vm[n] * fm[n][1]) * F(1, 2)) for n in range(T.N)]


def Hw(T, phi, f):
    return smul(T.H(smul(f, phi)), phi)


def force_density(T, phi, psi, j):
    """block 66 T3: f_j(x) = Re[(C_j[d_j phi] psi)^dag H phi psi + psi^dag C_j[d_j phi] H phi psi](x)."""
    v = T.fwd(phi, j)
    chi = T.H(smul(psi, phi))
    return [(inner(a, b) + inner(c, d)).re for a, b, c, d in zip(C_apply(T, j, v, psi), chi, psi, C_apply(T, j, v, chi))]


rng = random.Random(20260922)


def rand_state(T, amp=3):
    return [(G(rng.randint(-amp, amp), rng.randint(-amp, amp)), G(rng.randint(-amp, amp), rng.randint(-amp, amp))) for _ in range(T.N)]


# ================================================================== (a) the exact momentum balance, every state
T = Torus((3, 4, 5))
phi = [F(rng.randint(2, 9), rng.randint(2, 9)) for _ in range(T.N)]
psi = rand_state(T)
dpsi = [(-I * v[0], -I * v[1]) for v in Hw(T, phi, psi)]
ok = True
for j in range(3):
    Sj = T.S(psi, j); dSj = T.S(dpsi, j)
    pidot = [(inner(dpsi[n], Sj[n]) + inner(psi[n], dSj[n])).re for n in range(T.N)]
    phipsi = smul(psi, phi)
    div = [sum(T.back(T.J(phipsi, a, j), a)[n] for a in range(3)) for n in range(T.N)]
    f = force_density(T, phi, psi, j)
    ok = ok and all(pidot[n] + div[n] + f[n] == 0 for n in range(T.N))
# the commutator behind it: i[phi, S_j] = -C_j[d_j phi]
comm_ok = True
for j in range(3):
    lhs = [(I * (a[0] - b[0]), I * (a[1] - b[1])) for a, b in zip(smul(T.S(psi, j), phi), T.S(smul(psi, phi), j))]
    rhs = C_apply(T, j, T.fwd(phi, j), psi)
    comm_ok = comm_ok and all(l[0] == -r[0] and l[1] == -r[1] for l, r in zip(lhs, rhs))
want("A1 (a) EXACT, EVERY STATE: for H_w = phi H phi, d(pi_j)/dt + sum_a back_a J_a^j[phi psi] = -f_j at every site, with block 66's "
     "force density f_j = Re[(C_j[d_j phi] psi)^dag H phi psi + psi^dag C_j[d_j phi] H phi psi]; behind it i[phi, S_j] = -C_j[d_j phi] "
     "(random rational rates and Gaussian-integer state on a 3x4x5 torus, not stationary)", ok and comm_ok)

# ================================================================== (a) the force at first order in the rate gradient: e du cos k_j
T4 = Torus((4, 4, 4))
unit = {0: G(1), 1: G(0, 1), 2: G(-1), 3: G(0, -1)}
coins = {(0, 1): (G(1), G(1)), (0, -1): (G(1), G(-1)), (1, 1): (G(1), G(0, 1)), (1, -1): (G(1), G(0, -1)), (2, 1): (G(1), G(0)), (2, -1): (G(0), G(1))}
phi1 = [F(rng.randint(-9, 9), rng.randint(1, 9)) for _ in range(T4.N)]
ok = True; seen_cos = set()
for nk in itertools.product(range(4), repeat=3):
    s = [unit[n].im for n in nk]
    if sum(v * v for v in s) != 1: continue                                # energy-1 plane waves: exact Gaussian-integer coins
    a0 = next(a for a in range(3) if s[a] != 0)
    chi = coins[(a0, int(s[a0]))]
    wave = [tuple(unit[sum(nk[d] * x[d] for d in range(3)) % 4] * chi[t] for t in range(2)) for x in T4.sites]
    Hwave = T4.H(wave)
    E = 1                                                                  # H wave = wave
    ok = ok and all(Hwave[n][t] == wave[n][t] for n in range(T4.N) for t in range(2))
    norm = inner(chi, chi).re
    for j in range(3):
        cj = unit[nk[j]].re                                               # cos k_j in {1, 0, -1}
        seen_cos.add(cj)
        # first-order coefficient of f_j in eps for phi = 1 + eps phi1: Re[(C_j[d_j phi1] psi)^dag H psi + psi^dag C_j[d_j phi1] H psi]
        v = T4.fwd(phi1, j)
        f1 = [(inner(a, b) + inner(c, d)).re for a, b, c, d in zip(C_apply(T4, j, v, wave), Hwave, wave, C_apply(T4, j, v, Hwave))]
        # e^(0) = E |chi|^2 ; u = 2 log phi -> u^(1) = 2 phi1 ; centred difference (u(x+e_j) - u(x-e_j))/2 = phi1(x+e_j) - phi1(x-e_j)
        cen = [a - b for a, b in zip(T4.shift(phi1, j, 1), T4.shift(phi1, j, -1))]
        ok = ok and all(f1[n] == E * norm * cen[n] * cj for n in range(T4.N))
want("A2 (a) THE FORCE AT FIRST ORDER IN THE RATE GRADIENT: for phi = 1 + eps phi1 and every energy-1 plane wave of the 4^3 torus (24 "
     "waves, three directions each), the eps-coefficient of f_j is exactly e * (u(x+e_j) - u(x-e_j))/2 * cos k_j (e = E|chi|^2 at "
     "zeroth order, centred difference of u = 2 log phi on the site): the walk falls with its weight times cos k_j - fully for a smooth "
     "amplitude, not at all at k_j = pi/2, and UPWARD for a species reflected along j (cos k_j = -1; blocks 68, 72)",
     ok and seen_cos == {1, 0, -1}, f"cos k_j values met: {sorted(seen_cos)}")

# ================================================================== (b) the lattice ledger of curls: divergence-free for every rate field
T3 = Torus((3, 3, 3))
w = [F(rng.randint(1, 9), rng.randint(1, 9)) for _ in range(T3.N)]
Bs = {(a, j): [F(rng.randint(-5, 5), rng.randint(1, 5)) for _ in range(T3.N)] for a in range(3) for j in range(3)}
Bsym = {(a, j): [sp.Symbol(f"B_{a}{j}_{n}") for n in range(T3.N)] for a in range(3) for j in range(3)}


def ledger(B, wts):
    """F = sum_x w_x D_x, D_x = sum over plaquettes (a<b) at x and components j of curl^2 + a cubic curl term (a generic function)."""
    tot = 0
    for n in range(T3.N):
        Dn = 0
        for a in range(3):
            for b in range(a + 1, 3):
                for j in range(3):
                    na = T3.nb(n, a, 1); nb_ = T3.nb(n, b, 1)
                    curl = (B[(b, j)][na] - B[(b, j)][n]) - (B[(a, j)][nb_] - B[(a, j)][n])
                    Dn += curl ** 2 + curl ** 3 / 3
        tot += wts[n] * Dn
    return tot


Fsym = ledger(Bsym, w)
subs = {Bsym[k][n]: Bs[k][n] for k in Bsym for n in range(T3.N)}
Egrad = {k: [sp.diff(Fsym, Bsym[k][n]).subs(subs) for n in range(T3.N)] for k in Bsym}   # dF/dB_a^j(x) at the random B
div_ok = all(sum(Egrad[(a, j)][n] - Egrad[(a, j)][T3.nb(n, a, -1)] for a in range(3)) == 0 for j in range(3) for n in range(T3.N))
nonzero = any(v != 0 for k in Egrad for v in Egrad[k])
want("B1 (b) THE LATTICE IDENTITY WITH RATES: for F = sum_x w_x D_x with D_x any function of the plaquette curls at x (here curl^2 + curl^3/3), "
     "random rational rates w and strains B on the 3^3 torus, sum_a back_a dF/dB_a^j = 0 at every site EXACTLY, whatever the rates: a "
     "relabelling of the strains does not carry the rates, so nothing replaces 'divergence-free'. With the strains' equations J[phi psi] = "
     "-dF/dB the static system then demands sum_a back_a J_a^j[phi psi] = 0, while the walk's law (A1, stationary) gives -f_j: static "
     "solutions exist only for contents with f = 0 - this ledger forbids the fall rather than owing it", div_ok and nonzero)

# ================================================================== (b)/(c) no content-blind ledger owes the lattice fall
# at first order in the rate gradient a plane wave has e = E|chi|^2 and J_a^i = cos k_a s_a s_i |chi|^2/E (uniform), f_j = E|chi|^2 cos k_j c_j.
# A ledger whose identity sees the content through e and J with content-independent coefficients would need, for all k on the shell,
# E^2 cos k_j c_j = A_j E^2 + sum_{a,i} B_jai cos k_a s_i s_a  (A, B independent of k).  Pythagorean points make this an exact linear system.
pts = [(F(0), F(1)), (F(1), F(0)), (F(0), F(-1)), (F(3, 5), F(4, 5)), (F(4, 5), F(-3, 5)), (F(5, 13), F(12, 13)), (F(-12, 13), F(5, 13)),
       (F(8, 17), F(-15, 17)), (F(7, 25), F(24, 25))]
rows, rhs = [], []
for (s1, c1) in pts:
    for (s2, c2) in pts[:5]:
        for (s3, c3) in pts[:3]:
            s = [s1, s2, s3]; c = [c1, c2, c3]
            E2 = sum(v * v for v in s)
            if E2 == 0: continue
            row = [E2] + [c[a] * s[i] * s[a] for a in range(3) for i in range(3)]
            rows.append(row); rhs.append(E2 * c1)                          # j = 1, c_1 = 1
M = sp.Matrix(rows); bvec = sp.Matrix(rhs)
r1 = M.rank(); r2 = M.row_join(bvec).rank()
want("B2 (b)/(c) NO CONTENT-BLIND LEDGER OWES THE LATTICE FALL: at first order in the gradient the plane-wave force E|chi|^2 cos k_j c_j "
     "is not A_j e + sum B_jai J_a^i for any coefficients independent of the content: the exact linear system over Pythagorean wave "
     "vectors (rational sines and cosines) has rank(M) < rank([M | b]), i.e. no solution", r2 > r1, f"{len(rows)} wave vectors, rank {r1} vs {r2}")

# ================================================================== (c) leading order: agreement
k = sp.Symbol("k", real=True)
lead_ok = sp.series(sp.cos(k), k, 0, 2).removeO() == 1
want("C1 (c) AT LEADING ORDER IN THE WAVE NUMBER the two sides agree: cos k_j = 1 + O(k_j^2), so f_j = e (centred d_j u) + O(k^2 e du) for "
     "a smooth amplitude, which is block 66 T2's requirement with e on the site and the centred difference of u on the same site; the "
     "relative mismatch is (cos k_j - 1) = -k_j^2/2 + ..., and -2 for a species reflected along j", lead_ok)

npass = sum(1 for _, o in RESULTS if o)
nfail = len(RESULTS) - npass
print(f"TOTAL: PASS={npass} FAIL={nfail}")
if nfail == 0:
    print("SUMMARY: PARTIAL, exact on the lattice: (a) d(pi_j)/dt + div J[phi psi] = -f_j for every state (block 66 T3 re-derived), and at "
          "first order in the rate gradient f_j = e (centred d_j u) cos k_j exactly for plane waves; (b) a ledger F = sum_x w_x D_x(curls) "
          "stays divergence-free for EVERY rate field, so with the strains' equations it demands div J[phi psi] = 0 and has no static "
          "solution for a content with f != 0 - on the lattice it forbids the fall; and no ledger that sees the content only through e and "
          "J with content-independent coefficients reproduces cos k_j; (c) the fall is owed by the ledger only at leading order in the wave "
          "number (continuum, block 66 T2/T4: e on the site, centred du), with relative mismatch cos k_j - 1; at the lattice level it is an "
          "independent clause")
    print("HIT: on the lattice, the ledger F = sum_x w_x D_x(plaquette curls) satisfies sum_a back_a dF/dB_a^j = 0 for every rate field, so "
          "the static equations force div J[phi psi] = 0 and admit no content with a nonzero force density - it forbids the fall; the "
          "clocked walk's force at first order in the rate gradient is exactly e (centred d_j u) cos k_j, which no ledger seeing the content "
          "through e and J with content-independent coefficients reproduces; agreement with block 66's requirement holds at leading order "
          "in the wave number only")
