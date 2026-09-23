#!/usr/bin/env python3
"""J:derive:the-two-record-ledger-under-exclusion:a1 - worker w-jonathonsmac4f50-j99c8.

Objects (supplied, not adopted): block 54's reduced walk on a ring with a two-component coin,
clocked by block 53's rates, H_w = phi sigma_3 D phi, (D psi)(x) = (psi(x+1) - psi(x-1))/(2i),
w = phi^2 = e^u (block 78's runner, family D); block 55's ledger <H_w> + F and its density
e_x = Re chi_x^dag (H_w chi)_x; block 78/80's exclusion: two records on different sites, the
projector P onto those configurations, the compressed generator P H2 P, H2 = H_w x 1 + 1 x H_w.
Everything here is exact (sympy rationals, symbols for the rates where a derivative is taken).
"""
import itertools
import sympy as sp

RESULTS = []


def check(tag, ok, text, detail=''):
    RESULTS.append(bool(ok))
    print(f"{'PASS' if ok else 'FAIL'} {tag} {text}" + (f" :: {detail}" if detail else ''))


I = sp.I
R = sp.Rational


def walk(size, phi):
    """H_w = phi sigma_3 D phi on a ring (index 2x + c), entries in phi."""
    H = sp.zeros(2 * size, 2 * size)
    for x in range(size):
        for c in range(2):
            s = 1 if c == 0 else -1
            H[2 * x + c, 2 * ((x + 1) % size) + c] += s * phi[x] * phi[(x + 1) % size] / (2 * I)
            H[2 * x + c, 2 * ((x - 1) % size) + c] -= s * phi[x] * phi[(x - 1) % size] / (2 * I)
    return H


def site(i):
    return i // 2


def one_density(H, psi, size):
    n = (psi.H * psi)[0]
    Hp = H * psi
    return [sp.cancel(sp.re(sp.expand(sum(sp.conjugate(psi[2 * x + c]) * Hp[2 * x + c] for c in range(2)) / n))) for x in range(size)]


def pair(psi1, psi2, sgn):
    return psi1 * psi2.T + sgn * psi2 * psi1.T          # Psi_ij, sgn = -1 antisymmetric, +1 symmetric


def project(Psi):
    P = Psi.copy()
    for i in range(P.rows):
        for j in range(P.cols):
            if site(i) == site(j):
                P[i, j] = 0
    return P


def mask(M):
    return project(M)


def pair_energy_parts(H, Psi, size, compress=True):
    """slot densities e^[1]_x, e^[2]_x and the total, normalised by <Psi|Psi>;
    compress=True: P (H_w x 1 + 1 x H_w) P on the projected state (Psi must already be projected)."""
    nrm = sum(abs(v) ** 2 for v in Psi)
    A1 = H * Psi                     # (H x 1) Psi
    A2 = Psi * H.T                   # (1 x H) Psi
    if compress:
        A1, A2 = mask(A1), mask(A2)
    e1 = [0] * size
    e2 = [0] * size
    for i in range(Psi.rows):
        for j in range(Psi.cols):
            if Psi[i, j] == 0:
                continue
            e1[site(i)] += sp.conjugate(Psi[i, j]) * A1[i, j]
            e2[site(j)] += sp.conjugate(Psi[i, j]) * A2[i, j]
    f = lambda v: sp.cancel(sp.re(sp.expand(v / nrm)))
    return [f(v) for v in e1], [f(v) for v in e2]


# ------------------------------------------------------------------ block 78's ring of 6 (runner family D)
size = 6
phi_num = [1 + R((3 * x * x + x) % 5, 7) for x in range(size)]
Hn = walk(size, phi_num)
u1 = [R((x * x + 1) % 4, 3) if c == 0 else R((2 * x + 1) % 5, 4) for x in range(size) for c in range(2)]
v1 = [R(x % 3, 2) if c == 0 else R((x * x) % 3 - 1, 3) for x in range(size) for c in range(2)]
u2r = [R((x + 2) % 4, 5) if c == 0 else R(1, 2) for x in range(size) for c in range(2)]
v2r = [R((x * x + x) % 3, 2) if c == 0 else R((3 * x) % 4 - 2, 3) for x in range(size) for c in range(2)]
psi1 = sp.Matrix([a + I * b for a, b in zip(u1, v1)])
psi2r = sp.Matrix([a + I * b for a, b in zip(u2r, v2r)])
psi2 = psi2r - ((psi1.H * psi2r)[0] / (psi1.H * psi1)[0]) * psi1
psi2 = psi2.applyfunc(lambda z: sp.expand(z))
orth = sp.simplify((psi1.H * psi2)[0]) == 0

d1 = one_density(Hn, psi1, size)
d2 = one_density(Hn, psi2, size)
E1, E2 = sum(d1), sum(d2)
Psi = pair(psi1, psi2, -1)
free1, free2 = pair_energy_parts(Hn, Psi, size, compress=False)
PPsi = project(Psi)
hc1, hc2 = pair_energy_parts(Hn, PPsi, size, compress=True)
e_free = [a + b for a, b in zip(free1, free2)]
e_hc = [a + b for a, b in zip(hc1, hc2)]
E_free, E_hc = sum(e_free), sum(e_hc)

# ------------------------------------------------------------------ (a) the ledger identity under exclusion
phs = sp.symbols('f0:6', positive=True)
Hs = walk(size, list(phs))
nrmP = sum(abs(v) ** 2 for v in PPsi)
A1s, A2s = mask(Hs * PPsi), mask(PPsi * Hs.T)
Es = sp.expand(sum(sp.conjugate(PPsi[i, j]) * (A1s[i, j] + A2s[i, j]) for i in range(12) for j in range(12) if PPsi[i, j] != 0) / nrmP)
Es = sp.expand(sp.re(Es)) if Es.has(I) else Es
subs = dict(zip(phs, phi_num))
deriv = [sp.cancel(sp.expand((phs[x] / 2) * sp.diff(Es, phs[x])).subs(subs)) for x in range(size)]     # d/du_x = (phi_x/2) d/dphi_x
ok = orth and all(sp.simplify(deriv[x] - e_hc[x]) == 0 for x in range(size))
ok &= sp.simplify(sum(e_hc) - Es.subs(subs)) == 0                                                      # weight one
# the identity needs P to be rate-independent only: the unprojected pair (P = 1) obeys it with its own density
nrmF = sum(abs(v) ** 2 for v in Psi)
EsF = sp.expand(sum(sp.conjugate(Psi[i, j]) * ((Hs * Psi)[i, j] + (Psi * Hs.T)[i, j]) for i in range(12) for j in range(12) if Psi[i, j] != 0) / nrmF)
derivF = [sp.cancel(sp.expand((phs[x] / 2) * sp.diff(EsF, phs[x])).subs(subs)) for x in range(size)]
ok &= all(sp.simplify(derivF[x] - e_free[x]) == 0 for x in range(size))
ok &= any(sp.simplify(deriv[x] - e_free[x]) != 0 for x in range(size))
check('A1', ok, "(a) EXACT: for the projected antisymmetric pair of block 78's two orthogonal complex states on "
      "the ring of 6 (block 78's rate field), the derivative of the pair's compressed energy with respect to "
      "each site's tick rate u_x (taken symbolically in the six phi's, d/du_x = (phi_x/2) d/dphi_x) equals "
      "e^(2)_x = sum over the two slots of Re <Psi_P| P_x P H_w P |Psi_P>, the six densities sum to the "
      "energy (weight one), and they are not the free pair's: block 55 T1 holds for the compressed generator "
      "with the projected state's own density (block 80 T1 re-derived)",
      f"e^(2) = {e_hc}")

# ------------------------------------------------------------------ (a) the ledger kept along any motion
t = sp.symbols('t', real=True)
upath = [R(1, 3) * t * (x - R(5, 2)) + R(1, 7) * t ** 2 * ((x * x) % 3) for x in range(size)]   # a rate path u_x(t)
phit = [p * sp.exp(u / 2) for p, u in zip(phi_num, upath)]
Et = Es.subs(dict(zip(phs, phit)))
lhs = sp.diff(Et, t).subs(t, 0)
rhs = sum(e_hc[x] * sp.diff(upath[x], t).subs(t, 0) for x in range(size))
ok = sp.simplify(lhs - rhs) == 0
check('A2', ok, "(a) EXACT: along a path of rates u(t) at fixed projected state, d<P H2 P>/dt = sum_x e^(2)_x "
      "du_x/dt (checked on a two-parameter path); with the state moving by P H2 P the commutator term "
      "vanishes, so the ledger <P H2 P> + F is kept exactly when the field's law is dF/du_x = -(e^(2)_x - mu): "
      "block 55 T2(a)'s source becomes the projected pair's density", f"{lhs} = {rhs}")

# ------------------------------------------------------------------ (b) matched pulls
L = sp.eye(size)
Grad = sp.zeros(size, size)
for x in range(size):
    L[x, (x + 1) % size] -= R(1, 2)
    L[x, (x - 1) % size] -= R(1, 2)
    Grad[x, (x + 1) % size] += R(1, 2)
    Grad[x, (x - 1) % size] -= R(1, 2)
J = sp.ones(size, size) / size
G0 = (L + J).inv() - J                       # zero-mean inverse of block 53's operator 1 - (neighbour average)


def pull(c, s):
    """pull on coupling density c in the weak field u = -kappa G0 (s - mean): -sum_x c_x (grad u)_x, per kappa."""
    cv, sv = sp.Matrix(c), sp.Matrix(s)
    return sp.cancel(sp.expand((cv.T * Grad * G0 * sv)[0]))


ok = all(sp.simplify(x) == 0 for x in (G0 * sp.ones(size, 1)))
ok &= sp.simplify(L * G0 - (sp.eye(size) - J)) == sp.zeros(size, size)
ok &= (G0 - G0.T) == sp.zeros(size, size) and (Grad + Grad.T) == sp.zeros(size, size)
self_hc = pull(e_hc, e_hc)
ok &= self_hc == 0
# the exchange-symmetric split: each slot carries the same density
ok &= all(sp.simplify(a - b) == 0 for a, b in zip(hc1, hc2))
half = [v / 2 for v in e_hc]
ok &= pull(half, half) == 0
# a spatial split applied to source and coupling alike
eL = [e_hc[x] if x < 3 else 0 for x in range(size)]
eR = [e_hc[x] if x >= 3 else 0 for x in range(size)]
fLR, fRL = pull(eL, eR), pull(eR, eL)
ok &= fLR + fRL == 0 and fLR != 0
# block 76's additive source against the coupling the dynamics supplies
e_add = [a + b for a, b in zip(d1, d2)]
self_add = pull(e_hc, e_add)
ok &= self_add != 0
ok &= pull(e_free, e_add) == 0 and all(sp.simplify(a - b) == 0 for a, b in zip(e_free, e_add))
check('B1', ok, "(b) EXACT: in block 53's weak field u = -kappa G0 (s - mean) (G0 the zero-mean inverse of "
      "1 - neighbour average, symmetric; the centred gradient antisymmetric), the pull on a coupling density c "
      "is -sum c grad u, and sum_x c_x (grad G0 s)_x = -sum_x s_x (grad G0 c)_x, so the pulls of any split of "
      "the pair into parts that each source what they couple to are equal and opposite, and the pair's total "
      "self-pull vanishes, with the source e^(2) of A1; the exchange-symmetric split gives both records the "
      "density e^(2)/2 exactly, whose mutual pull is zero; block 76's ADDITIVE source e_1 + e_2 against the "
      "coupling e^(2) leaves the pair a nonzero self-pull - action = reaction under exclusion needs the "
      "projected density as the source",
      f"self-pull with e^(2): {self_hc}; split L/R pulls {fLR}, {fRL}; self-pull with e1 + e2: {self_add} (times kappa)")

# ------------------------------------------------------------------ (c) the densities on the ring of 6
ok = orth and sp.simplify(E_free - (E1 + E2)) == 0 and sp.simplify(E_hc - (E1 + E2)) != 0
ok &= E_free == R(16169964, 134909593)
delta = [sp.simplify(a - b) for a, b in zip(e_hc, e_add)]
ok &= sp.simplify(sum(delta) - (E_hc - E_free)) == 0 and any(v != 0 for v in delta)
# the symmetric pair as well
PsiS = project(pair(psi1, psi2, +1))
s1, s2 = pair_energy_parts(Hn, PsiS, size, compress=True)
e_hcS = [a + b for a, b in zip(s1, s2)]
check('C1', ok, "(c) EXACT (block 78 T3's ring of 6, rates and states): the one-record densities sum to block "
      "78's free value 16169964/134909593 = e_1 + e_2, the free antisymmetric pair's density is e_1 + e_2 site "
      "by site, and the projected pair's density e^(2) differs from it site by site (differences below), the "
      "differences summing to the exclusion's change of energy",
      f"e1 + e2 = {e_add}; e^(2) (antisymmetric) = {e_hc}; e^(2) (symmetric) = {e_hcS}; E_hc = {E_hc}")

# ------------------------------------------------------------------ (c') what the exclusion changes in the source
# (i) for any state in the range of P the compressed density is the free formula applied to that state
fr1, fr2 = pair_energy_parts(Hn, PPsi, size, compress=False)
ok = all(sp.simplify(a + b - c) == 0 for a, b, c in zip(fr1, fr2, e_hc))
# (ii) product states whose supports share no site: P does nothing, the density is additive, adjacent or not
size8 = 8
phi8 = [1 + R((2 * x + 1) % 5, 6) for x in range(size8)]
H8 = walk(size8, phi8)
a8 = sp.Matrix([(R(x + 1, 2) + I * R(c + 1, 3)) if x in (0, 1, 2) else 0 for x in range(size8) for c in range(2)])
da = one_density(H8, a8, size8)
rows = []
for sup in ((4, 5, 6), (3, 4, 5), (2, 3, 4)):
    b8 = sp.Matrix([(R(c + 2, 5) - I * R(x, 7)) if x in sup else 0 for x in range(size8) for c in range(2)])
    db = one_density(H8, b8, size8)
    Pp = pair(a8, b8, -1)
    PP = project(Pp)
    h1_, h2_ = pair_energy_parts(H8, PP, size8, compress=True)
    diff = [sp.simplify(p + q - da[x] - db[x]) for x, (p, q) in enumerate(zip(h1_, h2_))]
    rows.append((sup, PP == Pp, all(v == 0 for v in diff)))
ok &= rows[0][1:] == (True, True) and rows[1][1:] == (True, True) and rows[2][1:] == (False, False)
check('C2', ok, "(c) EXACT: what the exclusion changes in the source. For any state already on different "
      "sites, P H2 P and H2 have the same expectation and the same density (P commutes with the site "
      "projectors), so the source differs from the free one only through the state: the same-site components "
      "that P removes. Product states whose supports share no site are unchanged by P and have e^(2) = e_1 + e_2 "
      "exactly, adjacent or not; blocked hops change the dynamics, not the instantaneous source",
      f"ring of 8, record A on sites 0-2, record B on (support, P leaves the pair unchanged, additive): {rows}")

# ------------------------------------------------------------------ (d) NUMERIC: the weak-field premise of matched pulls
import math
vals = []
for seed in range(3):
    uu = [0.8 * math.sin(1.7 * x * (seed + 1) + seed) for x in range(7)]
    ph = [math.exp(v / 2) for v in uu]
    n7 = len(uu)
    dF = [2 * ph[x] ** 2 - ph[x] * ph[(x + 1) % n7] - ph[x] * ph[(x - 1) % n7] for x in range(n7)]   # F = sum_bonds (phi_x - phi_y)^2
    gr = [(uu[(x + 1) % n7] - uu[(x - 1) % n7]) / 2 for x in range(n7)]
    dq = [(2 * uu[x] - uu[(x + 1) % n7] - uu[(x - 1) % n7]) / 2 for x in range(n7)]                  # its quadratic (weak-field) part
    vals.append((sum(a * b for a, b in zip(dF, gr)), sum(a * b for a, b in zip(dq, gr))))
ok = all(abs(v[0]) > 1e-3 and abs(v[1]) < 1e-12 for v in vals)
check('D1', ok, "(d) NUMERIC, A LIMIT OF THE QUESTION ITSELF: with block 55's field energy F = (2/gamma) sum_bonds "
      "(phi_x - phi_y)^2 at STRONG field the law dF/du_x = -(e_x - mu) gives a body the self-pull "
      "-sum_x e_x (grad u)_x = sum_x (dF/du_x)(grad u)_x, which vanishes for the quadratic (weak-field) F and not for "
      "the full one (ring of 7, three rate fields of amplitude 0.8), for one free record as much as for a pair: "
      "matched pulls with the centred-gradient pull law are a weak-field statement, independent of the exclusion",
      "; ".join(f"full {a:+.4f}, quadratic {b:+.1e}" for a, b in vals))

npass = sum(RESULTS)
print(f"TOTAL: PASS={npass} FAIL={len(RESULTS) - npass}")
print("SUMMARY: PROVED at block 55 T3's level: for two records under exclusion the derivative of the "
      "compressed energy with respect to each tick rate is the projected pair's own energy density e^(2) "
      "(weight one; the ledger <P H2 P> + F is kept exactly when the field's source is e^(2) - mu; block 80 T1 "
      "re-derived), and with that source the pulls through the weak rate field of any split of the pair that "
      "sources what it couples to are equal and opposite - the exchange-symmetric split gives each record "
      "e^(2)/2 and no mutual pull; neither fails, so there is no HIT by the task's criterion; the only failure "
      "is a source other than e^(2): block 76's additive e_1 + e_2 leaves the pair an exact nonzero self-pull "
      f"({self_add} kappa on block 78's ring of 6); records whose supports share no site have e^(2) = e_1 + e_2 exactly - the exclusion changes the source only by removing same-site components of the state")
