#!/usr/bin/env python3
"""J:derive:the-two-record-ledger-under-exclusion:a2 -- worker w-macbookpro90c72-j3fae (claude-opus-5-5).

Two records under one-record-per-site exclusion with block 78's clocked reduced walk. The pair is treated as ONE body:
its active mass (the ledger's source) and its passive mass (what a uniform gradient pulls). Every line is exact
(Fractions, sympy rationals).
"""
import sys, time
from fractions import Fraction as F
import sympy as sp

T0 = time.time(); FAILS = []
def ok(tag, good, msg):
    print(("ok " if good else "FAIL ") + tag + ": " + msg)
    if not good:
        FAILS.append(tag)

# ------------------------------------------------------------------ block 78's ring of 6 (runner D1), reproduced
size = 6; d = 2 * size
site = [i // 2 for i in range(d)]
def ring_A(phi):
    """A = i (phi sigma_3 D phi), D psi(x) = (psi(x+1) - psi(x-1))/(2i): real antisymmetric; H = -i A."""
    a = [[0] * d for _ in range(d)]
    for x in range(size):
        for c in range(2):
            s = 1 if c == 0 else -1
            a[2 * x + c][2 * ((x + 1) % size) + c] += sp.Rational(s, 2) * phi[x] * phi[(x + 1) % size]
            a[2 * x + c][2 * ((x - 1) % size) + c] -= sp.Rational(s, 2) * phi[x] * phi[(x - 1) % size]
    return a
phi0 = [1 + F((3 * x * x + x) % 5, 7) for x in range(size)]
ip = lambda u, v: sum((p * q for p, q in zip(u, v)), F(0))
u1 = [F((x * x + 1) % 4, 3) if c == 0 else F((2 * x + 1) % 5, 4) for x in range(size) for c in range(2)]
v1 = [F(x % 3, 2) if c == 0 else F((x * x) % 3 - 1, 3) for x in range(size) for c in range(2)]
u2r = [F((x + 2) % 4, 5) if c == 0 else F(1, 2) for x in range(size) for c in range(2)]
v2r = [F((x * x + x) % 3, 2) if c == 0 else F((3 * x) % 4 - 2, 3) for x in range(size) for c in range(2)]
n1 = ip(u1, u1) + ip(v1, v1)
cr = (ip(u1, u2r) + ip(v1, v2r)) / n1; ci = (ip(u1, v2r) - ip(v1, u2r)) / n1
u2 = [ur - (cr * p - ci * q) for ur, p, q in zip(u2r, u1, v1)]
v2 = [vr - (cr * q + ci * p) for vr, p, q in zip(v2r, u1, v1)]
psi1 = [sp.Rational(a.numerator, a.denominator) + sp.I * sp.Rational(b.numerator, b.denominator) for a, b in zip(u1, v1)]
psi2 = [sp.Rational(a.numerator, a.denominator) + sp.I * sp.Rational(b.numerator, b.denominator) for a, b in zip(u2, v2)]
def pair(sign):
    return {(i, j): psi1[i] * psi2[j] + sign * psi2[i] * psi1[j] for i in range(d) for j in range(d)}
def project(W):
    return {k: v for k, v in W.items() if site[k[0]] != site[k[1]] and v != 0}
def norm2(W):
    return sp.nsimplify(sum(sp.expand(v * sp.conjugate(v)) for v in W.values()))
def apply1(Hm, W, slot):
    out = {}
    for (i, j), v in W.items():
        for k in range(d):
            if slot == 0 and Hm[k][i] != 0:
                out[(k, j)] = out.get((k, j), 0) + Hm[k][i] * v
            if slot == 1 and Hm[k][j] != 0:
                out[(i, k)] = out.get((i, k), 0) + Hm[k][j] * v
    return out
def dotc(W1, W2):
    return sum(sp.conjugate(v) * W2.get(k, 0) for k, v in W1.items())

# ------------------------------------------------------------------ L.a: the ledger identity with the rates as symbols
ph = sp.symbols("f0:6", positive=True)
A_sym = ring_A(ph); H_sym = [[-sp.I * A_sym[r][c] for c in range(d)] for r in range(d)]
A_num = ring_A([sp.Rational(p.numerator, p.denominator) for p in phi0]); H_num = [[-sp.I * A_num[r][c] for c in range(d)] for r in range(d)]
sub0 = {ph[x]: sp.Rational(phi0[x].numerator, phi0[x].denominator) for x in range(size)}
good = True; res = {}
for sign, name in ((-1, "antisymmetric"), (1, "symmetric")):
    W = project(pair(sign)); nW = norm2(W)
    E_sym = sp.expand((dotc(W, apply1(H_sym, W, 0)) + dotc(W, apply1(H_sym, W, 1))) / nW)
    E_num = sp.nsimplify(E_sym.subs(sub0))
    dens_der = [sp.nsimplify(sp.expand(ph[x] / 2 * sp.diff(E_sym, ph[x])).subs(sub0)) for x in range(size)]
    # the local density: sum over slots of Re <PPsi| P_x^[s] H^[s] |PPsi> / <PPsi|PPsi>
    h1, h2 = apply1(H_num, W, 0), apply1(H_num, W, 1)
    dens_loc = []
    for x in range(size):
        tot = sum(sp.conjugate(v) * h1.get(k, 0) for k, v in W.items() if site[k[0]] == x) + \
              sum(sp.conjugate(v) * h2.get(k, 0) for k, v in W.items() if site[k[1]] == x)
        dens_loc.append(sp.nsimplify(sp.re(sp.expand(tot)) / nW))
    good &= all(isinstance(v, sp.Rational) for v in dens_der + dens_loc + [nW, E_num])     # exact rationals, no numeric guesses
    good &= all(a == b for a, b in zip(dens_der, dens_loc))
    good &= sp.simplify(sum(dens_der) - E_num) == 0 and sp.im(E_num) == 0
    res[name] = (E_num, dens_der)
# the one-record densities and block 78's values
def ring_A_frac(phi):
    a = [[F(0)] * d for _ in range(d)]
    for x in range(size):
        for c in range(2):
            s_ = 1 if c == 0 else -1
            a[2 * x + c][2 * ((x + 1) % size) + c] += F(s_, 2) * phi[x] * phi[(x + 1) % size]
            a[2 * x + c][2 * ((x - 1) % size) + c] -= F(s_, 2) * phi[x] * phi[(x - 1) % size]
    return a
A_fr = ring_A_frac(phi0)
def one_energy_density(u, v):
    """e_x = Re sum_{i at x} conj(psi_i)(H psi)_i / |psi|^2 with psi = u + i v, H = -i A: Re = u_i (Av)_i - v_i (Au)_i."""
    Au = [sum((A_fr[r][c] * u[c] for c in range(d)), F(0)) for r in range(d)]
    Av = [sum((A_fr[r][c] * v[c] for c in range(d)), F(0)) for r in range(d)]
    nrm = ip(u, u) + ip(v, v)
    return [sum((u[i] * Av[i] - v[i] * Au[i] for i in range(d) if site[i] == x), F(0)) / nrm for x in range(size)]
e1d = [sp.Rational(q.numerator, q.denominator) for q in one_energy_density(u1, v1)]
e2d = [sp.Rational(q.numerator, q.denominator) for q in one_energy_density(u2, v2)]
E_free = sum(e1d) + sum(e2d); E_hc = res["antisymmetric"][0]
good &= E_free == sp.Rational(16169964, 134909593) and E_hc == sp.Rational(12349656, 122046701)
diff = [sp.simplify(a - (b + c)) for a, b, c in zip(res["antisymmetric"][1], e1d, e2d)]
ndiff = sum(1 for x in diff if x != 0)
ok("L.a", good, "on block 78's ring of 6 (its rates phi_x = 1 + ((3x^2 + x) mod 5)/7 and its two orthogonal complex states), with "
   "the six rates as symbols: d<P H2 P>/du_x = (phi_x/2) dE/dphi_x equals the local density sum over slots Re<P Psi|P_x H|P Psi> "
   "at every site, for both exchange signs, and sums to the pair's energy (weight one); the antisymmetric pair gives "
   f"E_hc = {E_hc} (block 78's value), the one-record densities sum to E_free = {E_free}; the pair's density differs from "
   f"e1 + e2 at {ndiff} of 6 sites")

# ------------------------------------------------------------------ L.fall: the pair's passive mass, exact (open chain, w = 4^x)
Lc = 6; dc = 2 * Lc; good = True
def chain_H(lam):
    """H_w = phi sigma_3 D phi on an open chain with phi_x = lam^x (w = lam^(2x)); H = -i A."""
    Hm = [[0] * dc for _ in range(dc)]
    for x in range(Lc):
        for c in range(2):
            s = 1 if c == 0 else -1
            if x + 1 < Lc:
                Hm[2 * x + c][2 * (x + 1) + c] += -sp.I * sp.Rational(s, 2) * lam ** x * lam ** (x + 1)
            if x - 1 >= 0:
                Hm[2 * x + c][2 * (x - 1) + c] -= -sp.I * sp.Rational(s, 2) * lam ** x * lam ** (x - 1)
    return Hm
Hc = chain_H(sp.Integer(2))
st = lambda i: i // 2
def col(i, j):            # P H2 P applied to the basis pair (i, j): hops of either record, never onto the other's site
    out = {}
    for k in range(dc):
        if Hc[k][i] != 0 and st(k) != st(j):
            out[(k, j)] = out.get((k, j), 0) + Hc[k][i]
        if Hc[k][j] != 0 and st(k) != st(i):
            out[(i, k)] = out.get((i, k), 0) + Hc[k][j]
    return out
checked = 0
for i in range(dc):
    for j in range(dc):
        if st(i) == st(j) or not (1 <= st(i) <= Lc - 3 and 1 <= st(j) <= Lc - 3):
            continue
        lhs = col(i + 2, j + 2)
        rhs = {(k + 2, l + 2): 4 * v for (k, l), v in col(i, j).items()}
        good &= set(lhs) == set(rhs) and all(sp.simplify(lhs[k] - rhs[k]) == 0 for k in lhs)
        checked += 1
ok("L.fall", good, f"on an open chain with w = 4^x the compressed pair generator obeys P H2_w P T = 4 T P H2_w P for the joint "
   f"translation T ({checked} interior columns, exact): the exclusion projector commutes with T and with the exchange, so in a "
   "uniform gradient the pair's crystal momentum changes at -g <P H2 P> for either exchange sign: its passive mass is its "
   "whole compressed energy")

# ------------------------------------------------------------------ L.pull: active against passive, and the additive source
ratio_add = sp.Rational(E_free) / sp.Rational(E_hc)
good = ratio_add != 1 and ratio_add == sp.Rational(16169964, 134909593) / sp.Rational(12349656, 122046701)
ok("L.pull", good, "by L.a the pair's source (active mass) is sum_x e_x = <P H2 P>, and by L.fall that is also what a uniform gradient "
   "pulls (passive mass): S/E = 1 for the pair as one body, so block 55 T3's pulls between the pair and any body with S = E are "
   f"matched; block 76's additive source e1 + e2 would give S/E = E_free/E_hc = {ratio_add} = {float(ratio_add):.4f} on this "
   "ring, and the pulls between the pair and another body would differ by that factor")
print(f"runtime {time.time() - T0:.0f} s")

if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAILS)); sys.exit(1)
print("SUMMARY: PARTIAL for two records under exclusion the ledger holds with the compressed density, and the pair's active and "
      "passive masses are both its compressed energy, so action = reaction survives with the pair as one body; the additive "
      "source of the free sea would break it by an exact factor")
print("HIT: for two records under one-per-site exclusion (either exchange sign) the compressed timed generator obeys "
      "P H2_w P T = lambda T P H2_w P for the joint translation in a uniform gradient, exactly, so the pair falls with its whole "
      "compressed energy; the ledger's source sum_x d<P H2 P>/du_x is the same energy, so S/E = 1 and block 55 T3's pulls "
      "between the pair and any body with S = E are matched.")
print(f"HIT: block 76's additive source e1 + e2 gives the pair S/E = E_free/E_hc = {ratio_add} (about {float(ratio_add):.3f}) "
      "on block 78's ring of 6, so with that source the pulls between the pair and another body do not match: under exclusion "
      "the source must be the compressed density.")
