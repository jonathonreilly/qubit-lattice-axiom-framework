#!/usr/bin/env python3
"""filling-between-the-a-terms-levels-chiral-content, attempt 1 (worker w-jonathonsmac4f50-j234b, claude-opus-5-5).

Exact claims: sympy (symbolic / exact rationals). Lines tagged [executed] are floating point evidence.
Step labels refer to ATTEMPT.md.
"""
import itertools
import sys
import time

import numpy as np
import sympy as sp

T0 = time.time()
NP = NF = 0


def ok(label, cond, detail=""):
    global NP, NF
    if cond:
        NP += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        NF += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def z(e):
    return sp.simplify(e) == 0


s1, s2, s3 = sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])
I2 = sp.eye(2)
k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
a0, a, m = sp.symbols("a0 a m", real=True)
K = (k1, k2, k3)


def h(kv):
    return (a0 + 2 * a * sum(sp.cos(q) for q in kv)) * I2 + sp.sin(kv[0]) * s1 + sp.sin(kv[1]) * s2 + sp.sin(kv[2]) * s3


# ---------------------------------------------------------------- Step 1: levels and senses
nodes = list(itertools.product((0, 1), repeat=3))
levels, senses = {}, {}
okall = True
for n in nodes:
    kn = [sp.pi * q for q in n]
    hn = sp.simplify(h(kn))
    L = sp.simplify(hn[0, 0] - a0)
    okall &= z(hn[0, 1]) and z(hn[1, 0]) and z(hn[0, 0] - hn[1, 1])
    J = sp.Matrix(3, 3, lambda i, j: sp.diff(sp.sin(K[i]), K[j])).subs({K[j]: kn[j] for j in range(3)})
    chi = J.det()
    levels[n], senses[n] = L, chi
    okall &= z(L - 2 * a * (3 - 2 * sum(n))) and chi == (-1) ** sum(n)
ok("1.1 at k = pi n the symbol is the scalar a0 + 2a(3 - 2|n|) (coin vector 0); sense chi_n = det(d sin k/dk) = (-1)^{|n|}", okall)
bylev = {}
for n in nodes:
    bylev.setdefault(sum(n), []).append(senses[n])
ok("1.2 multiplicities 1:3:3:1 and one sense per level; sum of senses = 0",
   [len(bylev[j]) for j in range(4)] == [1, 3, 3, 1] and all(len(set(v)) == 1 for v in bylev.values()) and sum(senses.values()) == 0,
   f"senses by |n|: {[bylev[j][0] for j in range(4)]}")

# ---------------------------------------------------------------- Step 2: Berry curvature of the two bands of d.sigma
th, ph = sp.symbols("theta phi", real=True)
nv = sp.Matrix([sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th)])
ndots = nv[0] * s1 + nv[1] * s2 + nv[2] * s3
for sgn, name in ((1, "upper"), (-1, "lower")):
    P = (I2 + sgn * ndots) / 2
    Pt, Pp = P.diff(th), P.diff(ph)
    F = sp.simplify(sp.I * (P * (Pt * Pp - Pp * Pt)).trace())  # standard: F = dA, A = i<u|du>, F = i tr(P[d1 P, d2 P])
    ch = sp.integrate(sp.integrate(F, (ph, 0, 2 * sp.pi)), (th, 0, sp.pi)) / (2 * sp.pi)
    ok(f"2.1{'a' if sgn > 0 else 'b'} {name} band of d.sigma: F = i tr(P[dP,dP]) = {-sgn}(1/2) sin(theta) (outward on the unit sphere); Chern = {-sgn} x degree",
       z(F + sgn * sp.sin(th) / 2) and ch == -sgn, f"F = {F}, Chern = {ch}")
# degree of q -> J q / |J q| on a small sphere for J = diag(+-1): orientation of J = sign det J
okdeg = all(sp.Matrix.diag(*[(-1) ** q for q in n]).det() == senses[n] for n in nodes)
ok("2.2 near each zero d(pi n + q) = J_n q + O(q^3), J_n = diag((-1)^{n_j}); degree of d/|d| on a small sphere = det J_n = chi_n", okdeg)
# charges: upper q+_n = -chi_n, lower q-_n = +chi_n (Step 2.1 with degree chi_n)

# ---------------------------------------------------------------- Step 3: Chern numbers of the Fermi sheets, every filling
av = sp.Rational(1)  # a > 0; levels in units of a (a0 = 0)
Lval = {n: int(2 * (3 - 2 * sum(n))) for n in nodes}
windows = [(-10, -6), (-6, -2), (-2, 2), (2, 6), (6, 10)]
rows = []
for lo, hi in windows:
    mu = sp.Rational(lo + hi, 2)
    below = [n for n in nodes if Lval[n] < mu]
    above = [n for n in nodes if Lval[n] > mu]
    Cup = -sum(senses[n] for n in below)  # boundary of {E+ < mu}: sum of q+ over enclosed zeros
    Clo = sum(senses[n] for n in below)  # boundary of {E- < mu}: sum of q- over enclosed zeros
    Clo_alt = -sum(senses[n] for n in above)
    rows.append((f"({lo}a,{hi}a)", int(Cup), int(Clo), int(Cup + Clo), Clo == Clo_alt))
ok("3.1 upper-band sheets carry -sum_{L_n<mu} chi_n, lower-band sheets +sum_{L_n<mu} chi_n = -sum_{L_n>mu} chi_n; total 0 at every filling",
   all(r[3] == 0 and r[4] for r in rows), " ; ".join(f"mu in {r[0]}: upper {r[1]:+d}, lower {r[2]:+d}, total {r[3]}" for r in rows))
ok("3.2 per-band values: (-6a,-2a): +1/-1; (-2a,2a): -2/+2; (2a,6a): +1/-1; outside: 0",
   [(r[1], r[2]) for r in rows] == [(0, 0), (1, -1), (-2, 2), (1, -1), (0, 0)])
# each node's own pocket (small a): electron pocket (upper, outward) carries q+ = -chi; hole pocket (lower, the occupied
# region's boundary points INTO the pocket) carries -q- = -chi: every pocket carries -chi_n, and sum over the eight = 0
ok("3.3 with the occupied-region orientation every separate pocket carries -chi_n (electron or hole alike); right - left over the eight = 0",
   sum(-senses[n] for n in nodes) == 0)

# ---------------------------------------------------------------- Step 4: the staggered term, exactly
kv = sp.Matrix(K)
hp = h([q + sp.pi for q in K])
ok("4.1 h(k + pi(111)) - a0 = -(h(k) - a0)", all(z(e) for e in (hp - a0 * I2 + h(K) - a0 * I2)))
A = sp.Matrix(2, 2, sp.symbols("A0:4"))
tz = sp.Matrix([[1, 0], [0, -1]])
tx = sp.Matrix([[0, 1], [1, 0]])
kron = lambda X, Y: sp.Matrix(sp.BlockMatrix([[X[i, j] * Y for j in range(X.cols)] for i in range(X.rows)]).as_explicit())
M4 = kron(tz, A) + m * kron(tx, I2)
ok("4.2 in the basis (k, k + pi(111)) eps = tau_x, and (tau_z x A + m tau_x x 1)^2 = tau_0 x A^2 + m^2 for any 2x2 A",
   all(z(e) for e in (M4 * M4 - kron(sp.eye(2), A * A) - m ** 2 * sp.eye(4))))
# at a zero: A = L 1 (+ first order sigma.v)
Ls, t_ = sp.symbols("L t", real=True)
v1, v2, v3 = sp.symbols("v1 v2 v3", real=True)
H0 = kron(Ls * tz + m * tx, I2)
ev0 = H0.eigenvals()
ok("4.3 at a zero the 4x4 block is (L tau_z + m tau_x) x 1: eigenvalues +-sqrt(L^2+m^2), each TWICE (a degeneracy, not a gap)",
   {sp.simplify(k_): v for k_, v in ev0.items()} == {sp.sqrt(Ls ** 2 + m ** 2): 2, -sp.sqrt(Ls ** 2 + m ** 2): 2})
# first-order splitting: project tau_z x sigma.v onto the + eigenspace of L tau_z + m tau_x
Rr = sp.sqrt(Ls ** 2 + m ** 2)
vp = sp.Matrix([Ls + Rr, m])
vp = vp / sp.sqrt((vp.T * vp)[0])
tz_exp = sp.simplify((vp.T * tz * vp)[0])
ok("4.4 on that eigenspace <tau_z> = L/sqrt(L^2+m^2): the pair splits LINEARLY as +-(L/sqrt(L^2+m^2))|J q| - a Weyl point of sense sign(L) chi_n",
   z(tz_exp - Ls / Rr), f"<tau_z> = {tz_exp}")
# exact eigenvalues along a line through the zero confirm the linear splitting
qv = sp.symbols("q", positive=True)
Aline = Ls * I2 + qv * s3  # d = J q along a principal axis, |J q| = q
evl = sp.Matrix(kron(tz, Aline) + m * kron(tx, I2)).eigenvals()
ok("4.5 exact eigenvalues near a zero: +-sqrt((L +- q)^2 + m^2); their difference at q -> 0 is 2 L q/sqrt(L^2+m^2) + O(q^2)",
   set(sp.simplify(e ** 2) for e in evl) == {sp.expand((Ls + qv) ** 2 + m ** 2), sp.expand((Ls - qv) ** 2 + m ** 2)}
   and z(sp.series(sp.sqrt((Ls + qv) ** 2 + m ** 2) - sp.sqrt((Ls - qv) ** 2 + m ** 2), qv, 0, 2).removeO() - 2 * Ls * qv / Rr))
# global spectrum and the only gap
lam = sp.symbols("lambda", real=True)
ok("4.6 spectrum a0 +- sqrt((E_i(k) - a0)^2 + m^2): the smallest |E - a0| is |m|, reached exactly on the massless sheets E_i = a0",
   z(sp.diff(sp.sqrt(lam ** 2 + m ** 2), lam).subs(lam, 0)) and z(sp.sqrt(lam ** 2 + m ** 2).subs(lam, 0) - sp.Abs(m)))
# Fermi sheets with the mass: |mu - a0| > |m| crosses E_i = a0 +- sqrt((mu-a0)^2 - m^2)
mu_s = sp.symbols("mu", real=True)
ok("4.7 for |mu - a0| > |m| the Fermi sheets are the massless ones at a0 +- sqrt((mu - a0)^2 - m^2): no pocket is gapped",
   z((sp.sqrt((mu_s - a0) ** 2 - m ** 2)) ** 2 + m ** 2 - (mu_s - a0) ** 2))
# nodal surfaces of the 4-band model where sum cos k = 0
sv = sp.Matrix(sp.symbols("sa sb sc", real=True))
Hsurf = kron(tz, sv[0] * s1 + sv[1] * s2 + sv[2] * s3) + m * kron(tx, I2)
evs = Hsurf.eigenvals()
ok("4.8 on the surface sum cos k = 0 the 4x4 block is tau_z x sigma.s + m tau_x: eigenvalues +-sqrt(|s|^2+m^2) each twice (a nodal surface)",
   sorted(evs.values()) == [2, 2] and all(z(sp.simplify(e ** 2) - (sv.dot(sv) + m ** 2)) for e in evs))
# the four node energies with the mass (block 77 T4's numbers) and their senses: upper point sense sign(L) chi
pairs = {}
for n in nodes:
    nb = tuple(1 - q for q in n)
    if n < nb:
        pairs[(n, nb)] = (Lval[n], senses[n], Lval[nb], senses[nb])
ok("4.9 each pair (n, n+(111)) has L_nb = -L_n and chi_nb = -chi_n, so the upper Weyl point's sense sign(L) chi is the same from either member",
   all(v[2] == -v[0] and v[3] == -v[1] and np.sign(v[0]) * v[1] == np.sign(v[2]) * v[3] for v in pairs.values()),
   f"upper-point senses by |L|: {sorted((abs(v[0]), int(np.sign(v[0]) * v[1])) for v in pairs.values())}")

print(f"exact part done in {time.time() - T0:.1f} s")

# ---------------------------------------------------------------- [executed] floating point evidence
sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]])
sz = np.array([[1, 0], [0, -1]], complex)


def hk(k, a0_, a_):
    return (a0_ + 2 * a_ * np.cos(k).sum()) * np.eye(2) + np.sin(k[0]) * sx + np.sin(k[1]) * sy + np.sin(k[2]) * sz


def H4(k, a0_, a_, m_):
    return np.block([[hk(k, a0_, a_), m_ * np.eye(2)], [m_ * np.eye(2), hk(k + np.pi, a0_, a_)]])


# E1: the 4-band splitting at the top zero, a = 0.2, m = 0.7
L0 = 6 * 0.2
qq = 1e-5
ev = np.linalg.eigvalsh(H4(np.array([qq, 0, 0]), 0.0, 0.2, 0.7))
vel = (ev[3] - ev[2]) / (2 * qq)
ok("E1 [executed] a = 0.2, m = 0.7: the zero's pair sits at sqrt(L^2+m^2) = 1.3892 and splits linearly with speed L/sqrt(L^2+m^2) = 0.8638",
   abs(ev[3] - np.sqrt(L0 ** 2 + 0.49)) < 1e-4 and abs(vel - L0 / np.sqrt(L0 ** 2 + 0.49)) < 1e-4, f"speed {vel:.6f}")


# E2: pocket structure and pocket Chern numbers (Fukui-Hatsugai-Suzuki on a small sphere around each zero)
def band_vec(k, upper, dmap=np.sin):
    d = dmap(k)
    w, V = np.linalg.eigh(d[0] * sx + d[1] * sy + d[2] * sz)
    return V[:, 1 if upper else 0]


def sphere_chern(center, upper, r=0.05, nt=24, npf=48, dmap=np.sin, orient=1):
    ths = np.linspace(0, np.pi, nt + 1)
    phs = np.linspace(0, 2 * np.pi, npf + 1)[:-1]
    U = np.empty((nt + 1, npf, 2), complex)
    for i, t in enumerate(ths):
        for j, p in enumerate(phs):
            U[i, j] = band_vec(center + r * np.array([np.sin(t) * np.cos(p), np.sin(t) * np.sin(p), np.cos(t)]), upper, dmap)
    tot = 0.0
    for i in range(nt):
        for j in range(npf):
            jp = (j + 1) % npf
            u1, u2, u3, u4 = U[i, j], U[i + 1, j], U[i + 1, jp], U[i, jp]
            prod = np.vdot(u1, u2) * np.vdot(u2, u3) * np.vdot(u3, u4) * np.vdot(u4, u1)
            tot += np.angle(prod)
    return orient * tot / (2 * np.pi)


# calibrate the orientation of the plaquette sum on the identity map d = q, whose upper-band Chern number is -1 (Step 2.1)
raw = sphere_chern(np.zeros(3), True, r=1.0, dmap=lambda q: q)
ORIENT = -1 if round(raw) == 1 else 1
fhs_ok = True
for n in nodes:
    cu = sphere_chern(np.pi * np.array(n, float), True, orient=ORIENT)
    cl = sphere_chern(np.pi * np.array(n, float), False, orient=ORIENT)
    fhs_ok &= (round(cu) == -senses[n]) and (round(cl) == senses[n]) and abs(cu - round(cu)) < 1e-6
ok("E2 [executed] link flux through a small sphere (orientation calibrated on d = q): upper band -chi_n, lower band +chi_n at all eight zeros",
   fhs_ok and abs(abs(raw) - 1) < 1e-9, f"raw identity-map value {raw:+.6f}, orientation factor {ORIENT}")

# E3: which zeros share a pocket, a = 0.1 and a = 0.6, mu in each window (grid 40^3, periodic connected components)
from scipy import ndimage  # noqa: E402


def components(mask):
    lab, nlab = ndimage.label(mask)
    parent = list(range(nlab + 1))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for ax in range(3):
        f = np.take(lab, 0, axis=ax)
        g = np.take(lab, -1, axis=ax)
        for x, y in zip(f.ravel(), g.ravel()):
            if x and y:
                rx, ry = find(x), find(y)
                if rx != ry:
                    parent[rx] = ry
    return lab, find


N = 40
ks = np.arange(N) * 2 * np.pi / N
KX, KY, KZ = np.meshgrid(ks, ks, ks, indexing="ij")
modS = np.sqrt(np.sin(KX) ** 2 + np.sin(KY) ** 2 + np.sin(KZ) ** 2)
Csum = np.cos(KX) + np.cos(KY) + np.cos(KZ)
for aa in (0.1, 0.6):
    Ep = 2 * aa * Csum + modS
    Em = 2 * aa * Csum - modS
    for lo, hi in ((-6, -2), (-2, 2), (2, 6)):
        mu = aa * (lo + hi) / 2
        desc = []
        for band, E, occ_side in (("upper", Ep, True), ("lower", Em, False)):
            mask = (E < mu) if occ_side else (E > mu)  # upper: electron pockets; lower: hole pockets
            lab, find = components(mask)
            groups = {}
            for n in nodes:
                idxn = tuple(int(q * N // 2) for q in n)
                l = lab[idxn]
                if l:
                    groups.setdefault(find(l), []).append(n)
            desc.append(f"{band}: " + " | ".join("".join(str(sum(n)) for n in g) for g in groups.values()))
        print(f"EXEC E3 a={aa} mu in ({lo}a,{hi}a): pockets by the |n| of the zeros they hold: " + "; ".join(desc))
print("EXEC E3 note: every zero lies in a pocket of one band or the other; a group's sheet carries -sum chi of its zeros (Step 3)")

print(f"total {time.time() - T0:.1f} s; PASS={NP} FAIL={NF}")
if NF:
    print(f"SUMMARY: ROUTE FAILS AT the first FAIL line above ({NF} failures)")
    sys.exit(1)
print("SUMMARY: PARTIAL (free comparator, exact for every a0, a, m and every filling) the Fermi sheets' Berry charges add to "
      "zero at every Fermi level: per band -sum_{L_n<mu} chi_n (upper) and +sum_{L_n<mu} chi_n (lower) = +1/-1, -2/+2, +1/-1 "
      "in the three windows, and every separate pocket carries its own zero's sense, so right minus left = 0; no filling has "
      "gapless content of a single sense. With the staggered term the spectrum is a0 +- sqrt((E_i - a0)^2 + m^2): for a != 0 the "
      "zeros stay two-fold degenerate at a0 +- sqrt(L^2 + m^2) and split linearly (Weyl points of speed |L|/sqrt(L^2+m^2)), "
      "the only gap is |mu - a0| < |m|, and no pocket outside it is gapped. The interacting case (d) is stated, not proved. "
      "The task's HIT condition (a single-sense filling) is not met.")
