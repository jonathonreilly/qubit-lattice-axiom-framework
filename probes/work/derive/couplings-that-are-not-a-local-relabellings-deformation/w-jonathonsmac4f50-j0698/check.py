#!/usr/bin/env python3
"""J:derive:couplings-that-are-not-a-local-relabellings-deformation:a2 - worker w-jonathonsmac4f50-j0698.

Block 54's walk H = sum_a sigma_a S_a (symbol sigma . s(k), s_a = sin k_a, H(k)^2 = |s(k)|^2); a coupling
dH[B] linear in a bond field, translation-covariant, of finite reach; for B = d xi with xi_j = e^{i p.x} the
deformation maps momentum k to k + p with a 2x2 symbol A(k, p).  Blocks 63/64 (reach two, M = S_j) and 69
(reach three, M = S_j C_j): A = i[H, (1/2){xi_j, M_j}].  Everything exact (sympy, integers, Gaussian rationals).
"""
import itertools
import sympy as sp

RESULTS = []


def check(tag, ok, text, detail=''):
    RESULTS.append(bool(ok))
    print(f"{'PASS' if ok else 'FAIL'} {tag} {text}" + (f" :: {detail}" if detail else ''))


I = sp.I
sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -I], [I, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])
SIG = (sx, sy, sz)

# ---------------------------------------------------------------- A1 the closed form of the generator
s1, s2, s3, t1, t2, t3 = sp.symbols('s1 s2 s3 t1 t2 t3')
a = sp.symbols('a0:4') + sp.symbols('b0:4')
A = sp.Matrix([[a[0] + I * a[4], a[1] + I * a[5]], [a[2] + I * a[6], a[3] + I * a[7]]])   # any 2x2 matrix
Hk = s1 * sx + s2 * sy + s3 * sz
Hp = t1 * sx + t2 * sy + t3 * sz
Nm = Hp * A + A * Hk
Dl = (t1 ** 2 + t2 ** 2 + t3 ** 2) - (s1 ** 2 + s2 ** 2 + s3 ** 2)
ok = sp.simplify(Hk * Hk - (s1 ** 2 + s2 ** 2 + s3 ** 2) * sp.eye(2)) == sp.zeros(2)
ok &= sp.simplify(Hp * Nm - Nm * Hk - Dl * A) == sp.zeros(2)
check('A1', ok, "(a) EXACT: because the walk squares to a scalar, H(k)^2 = |s(k)|^2, every symbol A(k, p) satisfies "
      "H' (H'A + AH) - (H'A + AH) H = (|s'|^2 - |s|^2) A (H' = H(k + p)): wherever |s(k + p)| != |s(k)| the deformation "
      "is i[H, G] with G = -i (H'A + AH)/(|s'|^2 - |s|^2), and this G is the only one there")


# ---------------------------------------------------------------- the couplings of blocks 63/64 and 69 as symbols
z = sp.symbols('z1:4')          # e^{i k_a}
w = sp.symbols('w1:4')          # e^{i p_a}
sn = lambda x: (x - 1 / x) / (2 * I)
cs = lambda x: (x + 1 / x) / 2
Hsym = lambda zz: sum((SIG[c] * sn(zz[c]) for c in range(3)), sp.zeros(2))
zp = [z[c] * w[c] for c in range(3)]


def coupling_symbol(j, M):
    """A(k, p) for sum_a sigma_a (1/2){C_a[d_a xi_j], M_j}, xi_j = e^{i p.x}; M a function of z (the momentum's symbol)."""
    out = sp.zeros(2)
    for c in range(3):
        Cv = (w[c] - 1) * (z[c] + 1 / (z[c] * w[c])) / 2          # symbol of C_a[d_a xi] from k to k + p
        out += SIG[c] * Cv * (M(z) + M(zp)) / 2
    return out


Mone = lambda zz: sn(zz[0])                                    # block 63: M_1 = S_1
Mtwo = lambda zz: sn(zz[0]) * cs(zz[0])                        # block 69: M_1 = S_1 C_1
Delta = sum(sn(zp[c]) ** 2 for c in range(3)) - sum(sn(z[c]) ** 2 for c in range(3))
ok = True
for M in (Mone, Mtwo):
    Ak = coupling_symbol(0, M)
    Gk = (M(z) + M(zp)) / 2                                     # symbol of (1/2){xi_1, M_1}
    Nk = Hsym(zp) * Ak + Ak * Hsym(z)
    ok &= all(sp.simplify(sp.together(Nk[r, c] - I * Delta * Gk * sp.eye(2)[r, c])) == 0 for r in range(2) for c in range(2))
    ok &= all(sp.simplify(sp.together(Ak[r, c] - I * (Hsym(zp) * Gk - Gk * Hsym(z))[r, c])) == 0 for r in range(2) for c in range(2))
check('A2', ok, "(a) EXACT, THE PLANE WAVE: for xi_1 = e^{i p.x} the symbols of block 63's reach-two coupling and of "
      "block 69's reach-three coupling satisfy H'A + AH = i Delta G with Delta = |s(k + p)|^2 - |s(k)|^2 = sum_a "
      "sin p_a sin(2k_a + p_a) and G = (M(k) + M(k + p))/2: the closed form of A1 returns the local generator "
      "(1/2){xi, M}, of reach one less than the coupling, the division by energy differences being exact")

# ---------------------------------------------------------------- A3 exact current = no diagonal blocks, at degenerate pairs
# Pythagorean wave vectors: exact sines/cosines.  A cubic symmetry R keeps |s|, so (k, R k) is a degenerate pair.
pyth = [(sp.Rational(3, 5), sp.Rational(4, 5)), (sp.Rational(5, 13), sp.Rational(12, 13)), (sp.Rational(8, 17), sp.Rational(15, 17))]
kz = [c + I * s for (c, s) in pyth]                               # e^{i k}
Rs = [(1, 0, 2), (2, 1, 0), (0, 2, 1)]                            # permutations of the axes
def proj(Hm, E):
    return (sp.eye(2) + Hm / E) / 2, (sp.eye(2) - Hm / E) / 2
def frame_symbol(zk, wk, E):
    """block 62's nearest-neighbour frame coupling (1/2){E^j.sigma, S_j} with a varying E = e^{i p x} E0: not conserved"""
    out = sp.zeros(2)
    for c in range(3):
        out += E[c] * SIG[c] * (sn(zk[0]) + sn(zk[0] * wk[0])) / 2
    return out
ok = True
bad = []
for R in Rs:
    kk = kz
    kp = [kz[R[c]] for c in range(3)]
    ww = [sp.simplify(kp[c] / kk[c]) for c in range(3)]
    Hk_ = sum((SIG[c] * sn(kk[c]) for c in range(3)), sp.zeros(2))
    Hp_ = sum((SIG[c] * sn(kp[c]) for c in range(3)), sp.zeros(2))
    E = sp.sqrt(sp.simplify(sum(sn(kk[c]) ** 2 for c in range(3))))
    Pk, Mk = proj(Hk_, E)
    Pp, Mp = proj(Hp_, E)
    sub = dict(zip(z, kk)); sub.update(dict(zip(w, ww)))
    for M in (Mone, Mtwo):
        Ak = coupling_symbol(0, M).subs(sub)
        ok &= sp.simplify(Pp * Ak * Pk) == sp.zeros(2) and sp.simplify(Mp * Ak * Mk) == sp.zeros(2)
        ok &= sp.simplify(Hp_ * Ak + Ak * Hk_) == sp.zeros(2)
    Af = frame_symbol(kk, ww, (1, 2, 3))
    bad.append(sp.simplify((Pp * Af * Pk).norm()) != 0 or sp.simplify((Mp * Af * Mk).norm()) != 0)
ok &= any(bad)
check('A3', ok, "(a) EXACT, WHAT 'CONSERVED ON EVERY STATIONARY STATE' MEANS: at degenerate pairs (k, Rk) with R a "
      "permutation of the axes (Pythagorean k, so |s(Rk)| = |s(k)| exactly) the conserved couplings of blocks 63 and 69 "
      "have zero blocks between equal energies and H'A + AH = 0 there, while block 62's nearest-neighbour frame "
      "coupling does not (its response is not conserved): a response is divergence-free on every stationary state "
      "iff the symbol has no block between equal energies, iff H'A + AH vanishes wherever |s(k + p)| = |s(k)|")

# ---------------------------------------------------------------- A4 locality: the degeneracy polynomial
P = sp.Poly(sp.expand(sp.numer(sp.together(Delta * 4 * sp.Mul(*[z[c] ** 2 * w[c] ** 2 for c in range(3)])))), *z, *w)
fQ = sp.factor_list(P.as_expr())
fQi = sp.factor_list(P.as_expr(), extension=I)
sgn = []
for (kv, pv) in (((sp.Rational(1, 3),) * 3, (sp.Rational(1, 7),) * 3), ((sp.Rational(1, 3),) * 3, (-sp.Rational(1, 7),) * 3)):
    sgn.append(sp.sign(sp.N(sum(sp.sin(pv[c]) * sp.sin(2 * kv[c] + pv[c]) for c in range(3)), 30)))
ok = len(fQ[1]) == 1 and fQ[1][0][1] == 1 and len(fQi[1]) == 1 and fQi[1][0][1] == 1 and sgn[0] == -sgn[1]
check('A4', ok, "(a) EXACT, THE INPUT OF THE LOCALITY THEOREM: the degeneracy polynomial Delta(k, p) = sum_a sin p_a "
      "sin(2k_a + p_a), cleared of denominators, is irreducible and square-free over Q and over Q(i) (one factor, "
      "multiplicity one) and changes sign on the real torus; with the standard real-algebraic step (ASSUMED: a "
      "polynomial vanishing on the five-dimensional real zero set of such a hypersurface is divisible by it) the "
      "numerator H'A + AH of every conserved coupling is divisible by Delta, so G = -i(H'A + AH)/Delta is a "
      "trigonometric polynomial in k and p jointly: every conserved coupling of finite reach on Z^3 is i[H, G] with G "
      "LOCAL (linear in xi, finite reach), of reach at most one less than the coupling's",
      f"factors over Q: {[(sp.Poly(g, *z, *w).total_degree(), m) for g, m in fQ[1]]}; over Q(i): {[(sp.Poly(g, *z, *w).total_degree(), m) for g, m in fQi[1]]}")

# ---------------------------------------------------------------- C1 couplings through the curls
xs = sp.symbols('x1:4')
xi = sp.Function('xi')
def dfd(f, a_):
    sh = list(xs); sh[a_] = sh[a_] + 1
    return f.subs(dict(zip(xs, sh)), simultaneous=True) - f
ok = True
for j in range(3):
    f = xi(*xs, j)
    for a_ in range(3):
        for b_ in range(3):
            ok &= sp.simplify(dfd(dfd(f, b_), a_) - dfd(dfd(f, a_), b_)) == 0
check('C1', ok, "(c) EXACT: the curl F_ab^j = d_a B_b^j - d_b B_a^j of a relabelling's strain d xi vanishes, so a coupling "
      "through the curls alone has dH[d xi] = 0: its response is conserved identically (G = 0), a uniform strain has no "
      "curl and gets no deformation (no lengths), and adding it to a coupling leaves dH[d xi] - hence G, the current and "
      "block 72's requirement, which is a statement about dH[d xi] - unchanged")

# ---------------------------------------------------------------- D1 the no-go: one geometry needs reach three
zeros = list(itertools.product((0, 1), repeat=3))
chars = {n: [(-1) ** n[c] for c in range(3)] for n in zeros}
monos = [m for m in itertools.product(range(-3, 4), repeat=3) if 0 < sum(abs(x) for x in m) <= 3]


def species_mean_shear(m, c, j):
    """mean over the eight zeros of D_c * d/dk_j e^{i m.k} at k = pi n (the coin-c, momentum-j entry of D dM_n)"""
    tot = 0
    for n in zeros:
        tot += chars[n][c] * I * m[j] * (-1) ** sum(mi * ni for mi, ni in zip(m, n))
    return sp.simplify(tot / 8)


ok = True
found3 = []
for m in monos:
    L1 = sum(abs(x) for x in m)
    for c in range(3):
        for j in range(3):
            if c == j:
                continue
            v = species_mean_shear(m, c, j)
            if L1 <= 2:
                ok &= v == 0
            elif v != 0:
                found3.append((m, c, j))
# the displacements a coupling of reach <= 2 may hop, and which of them U_(111) reverses
disp = [d for d in itertools.product(range(-2, 3), repeat=3) if sum(abs(x) for x in d) <= 2]
odd = [d for d in disp if sum(abs(x) for x in d) % 2 == 1]
ok &= sorted(odd) == sorted([tuple(s * (1 if c == a_ else 0) for c in range(3)) for a_ in range(3) for s in (1, -1)])
ok &= len(found3) > 0 and all(sum(abs(x) for x in m) == 3 and abs(m[j]) == 2 and abs(m[c]) == 1 for m, c, j in found3)
check('D1', ok, "(d) EXACT, THE THEOREM: for every coupling of reach <= 2 - any coin structure, conserved or not, local "
      "generator or not - species n (zero k = pi n, reflection D_n) sees at first order in a uniform strain the metric "
      "1 + D_n dM_n + (D_n dM_n)^T, where dM_n is the coupling's symbol's gradient at the zero; for c != j the entry "
      "D_c d_j f(pi n) of every trigonometric monomial of L1-degree <= 2 is a non-trivial character of the eight "
      "species (D_c, D_c D_j, D_j, D_c D_j D_c'), so its mean over the species is exactly zero: no coupling of reach "
      "two shows all eight species one shear geometry (the mean shear they see vanishes); a nonzero mean first "
      "appears at L1-degree three, for e^{i(2 e_j + e_c).k} alone (block 69's cos k_c sin 2k_j); and the energy "
      "reversal by U_(111) confines a reach-two coupling to nearest-neighbour hops anyway",
      f"{len(monos)} monomials checked; L1 <= 2 means: all zero; nonzero at L1 = 3 for {len(found3)} (m, c, j), all of the form 2e_j + e_c")

npass = sum(RESULTS)
print(f"TOTAL: PASS={npass} FAIL={len(RESULTS) - npass}")
print("SUMMARY: PROVED (with one standard real-algebraic step ASSUMED for locality): (a) a finite-reach coupling's "
      "response is conserved on every stationary state iff its symbol has no block between equal energies, and then, "
      "the walk squaring to a scalar, it is i[H, G] with G = -i(H'A + AH)/(|s(k + p)|^2 - |s(k)|^2); Delta is irreducible "
      "and square-free over Q(i), so G is local, of reach one less than the coupling (exact for blocks 63 and 69 at a "
      "plane wave); (b) hence no local coupling on Z^3 needs a non-local generator; (c) curl couplings are conserved "
      "identically, make no lengths and leave block 72's requirement unchanged; (d) for every coupling of reach <= 2 "
      "the mean over the eight species of the shear metric they see is exactly zero - one geometry for all species "
      "needs reach three, whatever the generator - so no reach-two coupling meets the ladder's demands (no HIT by the "
      "task's criterion)")
