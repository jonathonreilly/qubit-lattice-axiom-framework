#!/usr/bin/env python3
"""J:derive:composite-bodies-rest-energy-without-a-larger-site-algebra:a4 -- worker w-macbookpro90c72-j16c3 (claude-opus-5-5).

Two walkers of block 54's walk with a contact attraction. 'ok' lines are exact (sympy, Fractions);
'note' lines are floating point (ring diagonalisation, 3D secular equation on a grid, propagation in a gradient).
"""
import itertools, math, sys, time
from fractions import Fraction as Fr
import numpy as np
import sympy as sp

T0 = time.time(); FAILS = []
def ok(tag, good, msg):
    print(("ok " if good else "FAIL ") + tag + ": " + msg)
    if not good:
        FAILS.append(tag)

I = sp.I
s = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
E2m = sp.eye(2)
S1 = [sp.kronecker_product(m, E2m) for m in s]; S2 = [sp.kronecker_product(E2m, m) for m in s]
up, dn = sp.Matrix([1, 0]), sp.Matrix([0, 1]); kp = sp.kronecker_product
Sv = (kp(up, dn) - kp(dn, up)) / sp.sqrt(2)
Tz = (kp(up, dn) + kp(dn, up)) / sp.sqrt(2); Tx = (kp(dn, dn) - kp(up, up)) / sp.sqrt(2); Ty = I * (kp(up, up) + kp(dn, dn)) / sp.sqrt(2)
BAS = [Sv, Tx, Ty, Tz]

# ------------------------------------------------------------------ C.chan: the two-walker kinetic term at K = 0 splits singlet/triplet
E = sp.symbols("E"); h = sp.symbols("h1:4", real=True); hh = sum(x ** 2 for x in h)
A0 = sum((h[j] * (S1[j] - S2[j]) for j in range(3)), sp.zeros(4, 4))                 # K = 0: h(K/2 + q) = h(q), h(K/2 - q) = -h(q)
R = (E * sp.eye(4) - A0).inv()
good = sp.simplify((Sv.H * R * Sv)[0] - E / (E ** 2 - 4 * hh)) == 0
T3 = [Tx, Ty, Tz]
for a in range(3):
    for b in range(3):
        val = sp.simplify((T3[a].H * R * T3[b])[0])
        pred = (1 if a == b else 0) / E - h[a] * h[b] / (hh * E) + h[a] * h[b] * E / (hh * (E ** 2 - 4 * hh))
        good &= sp.simplify(val - pred) == 0
    cross = sp.simplify((Sv.H * R * T3[a])[0])
    good &= sp.simplify(cross.subs({h[0]: -h[0], h[1]: -h[1], h[2]: -h[2]}) + cross) == 0      # odd in h: averages to 0 (q -> -q)
ok("C.chan", good, "at total wave vector 0 the kinetic term is h(q).(sigma1 - sigma2): <S|(E - A)^-1|S> = E/(E^2 - 4|h|^2), the "
   "triplet block is (1 - nn)/E + nn E/(E^2 - 4|h|^2) (n = h/|h|), singlet-triplet terms are odd in h; with <h_i h_j f(|h|)> = "
   "delta_ij <|h|^2 f>/3 the contact condition 1 = V G splits exactly into 1 = V I(E) (singlet) and 1 = V(2/(3E) + I(E)/3) "
   "(triplet, three states), I(E) = <E/(E^2 - 4|h|^2)>")

# ------------------------------------------------------------------ C.mom: exact moments <A^n>_q at any K, and the strong-binding series
x = sp.symbols("x1:4"); y = sp.symbols("y1:4")                      # x_j = e^{i q_j}, y_j = e^{i K_j/2}
def sinf(yy, xx, sg):
    z = yy * xx ** sg
    return (z - 1 / z) / (2 * I)
A = sp.zeros(4, 4)
for j in range(3):
    A += sinf(y[j], x[j], 1) * S1[j] + sinf(y[j], x[j], -1) * S2[j]
A = A.applyfunc(sp.expand)
SH = (x[0] * x[1] * x[2]) ** 8
def qavg(expr):
    p = sp.Poly(sp.expand(expr * SH), *x)
    return sum(c for m_, c in p.terms() if m_ == (8, 8, 8))
A2 = (A * A).applyfunc(sp.expand); A3 = (A2 * A).applyfunc(sp.expand); A4 = (A2 * A2).applyfunc(sp.expand)
M1 = A.applyfunc(qavg); M2 = A2.applyfunc(qavg); M3 = A3.applyfunc(qavg); M4 = A4.applyfunc(qavg)
good = M1 == sp.zeros(4, 4) and M3 == sp.zeros(4, 4)
K3 = sp.symbols("K1:4", real=True)
cosK = {y[j]: sp.exp(I * K3[j] / 2) for j in range(3)}
M2pred = 3 * sp.eye(4) - sum((sp.cos(K3[j]) * S1[j] * S2[j] for j in range(3)), sp.zeros(4, 4))
good &= all(sp.simplify(sp.expand((M2.subs(cosK) - M2pred)[a, b]).rewrite(sp.cos)) == 0 for a in range(4) for b in range(4))
kap, V = sp.symbols("kappa V", real=True)
sub = {y[0]: 1, y[1]: 1, y[2]: sp.exp(I * kap / 2)}               # motion along z
def proj(M):
    return sp.Matrix(4, 4, lambda a, b: sp.simplify(sp.expand((BAS[a].H * M.subs(sub) * BAS[b])[0]).rewrite(sp.cos)))
m2, m4 = proj(M2), proj(M4)
good &= all(m2[a, b] == 0 and m4[a, b] == 0 for a in range(4) for b in range(4) if a != b)
res = []
for i, nm in enumerate(["singlet", "triplet across", "triplet across", "triplet along"]):
    E2ser = 2 * m2[i, i] + (2 * m4[i, i] - 3 * m2[i, i] ** 2) / V ** 2          # E = V + m2/V + (m4 - 2 m2^2)/V^3 + ...
    c2 = sp.expand(sp.series(E2ser, kap, 0, 3).removeO().coeff(kap, 2)); M0 = sp.expand(E2ser.subs(kap, 0))
    res.append((nm, M0, c2))
good &= [(r_[1], r_[2]) for r_ in res] == [(12 - 24 / V ** 2, -1 + 8 / V ** 2), (4 + 16 / V ** 2, 1 - 2 / V ** 2),
                                         (4 + 16 / V ** 2, 1 - 2 / V ** 2), (4 + 16 / V ** 2, -1 - 4 / V ** 2)]
ok("C.mom", good, "<A>_q = <A^3>_q = 0 and <A^2>_q = 3 - sum_i cos K_i sigma1_i sigma2_i exactly (Laurent polynomials in e^{iq}, "
   "e^{iK/2}); for motion along z <A^2>, <A^4> are diagonal in singlet and Cartesian triplet, so E = V + m2/V + (m4 - 2m2^2)/V^3 "
   "per channel: singlet E^2 = V^2 + 12 - 24/V^2 - (1 - 8/V^2)K^2; triplet E^2 = V^2 + 4 + 16/V^2 + (1 - 2/V^2)K^2 when its "
   "direction is across the motion and - (1 + 4/V^2)K^2 when along it (+ O(V^-4), O(K^4))")

# ------------------------------------------------------------------ C.stat: which walkers bind at all
swap = sp.zeros(4, 4)
for a_, b_ in itertools.product(range(2), repeat=2):
    swap[2 * b_ + a_, 2 * a_ + b_] = 1
good = sp.simplify(swap * Sv + Sv) == sp.zeros(4, 1) and all(sp.simplify(swap * T - T) == sp.zeros(4, 1) for T in T3)
ok("C.stat", good, "a contact term acts only on the pair's amplitude at relative position 0, where exchange acts on the coins alone: "
   "antisymmetric walkers have it in the coin singlet only (in 1D the combination up-down minus down-up), symmetric walkers in "
   "the triplet only (1D: equal coins, or up-down plus down-up); so antisymmetric walkers bind only in the inverted channels; "
   "under one record per site the contact term acts on nothing")

# ------------------------------------------------------------------ C.fall: the timed identity, exact (1D chain, w_x = 4^x)
Lc = 7; good = True
def gen_1d(s1, s2, timed, lam, Vc):
    """two walkers on an open chain of Lc sites with fixed coins; w_x = lam^(2x) so sqrt(w) = lam^x (rational)."""
    idx = {(a, b): a * Lc + b for a in range(Lc) for b in range(Lc)}; Hm = {}
    def put(r_, c_, v):
        Hm[(r_, c_)] = Hm.get((r_, c_), 0) + v
    for (a, b), c_ in idx.items():
        for sgn, walker in ((s1, 0), (s2, 1)):
            for d in (1, -1):                                     # D = (i/2)(T - T^dag), (T psi)(x) = psi(x - 1): <x|D|x-1> = i/2
                pos = [a, b]; newp = pos[walker] + d
                if not 0 <= newp < Lc:
                    continue
                tgt = list(pos); tgt[walker] = newp
                amp = sp.Rational(1, 2) * I * (1 if d == 1 else -1) * sgn
                amp *= lam ** (pos[walker] + newp)                # sqrt(w_target) sqrt(w_source)
                put(idx[tuple(tgt)], c_, amp)
        if a == b:
            put(c_, c_, Vc * (lam ** (2 * a) if timed else 1))
    return Hm
lam = sp.Integer(2); Vc = sp.Rational(-3, 2)
for s1_, s2_ in ((1, 1), (1, -1)):
    for timed in (True, False):
        Hm = gen_1d(s1_, s2_, timed, lam, Vc)
        # joint translation T: (a, b) -> (a + 1, b + 1); test H T = lam^2 T H on vectors supported away from the right end
        dev = 0
        for a in range(1, Lc - 2):
            for b in range(1, Lc - 2):
                col = a * Lc + b; colT = (a + 1) * Lc + (b + 1)
                lhs = {r_: v for (r_, c_), v in Hm.items() if c_ == colT}
                rhs = {}
                for (r_, c_), v in Hm.items():
                    if c_ == col:
                        ra, rb = divmod(r_, Lc)
                        if ra + 1 < Lc and rb + 1 < Lc:
                            rhs[(ra + 1) * Lc + rb + 1] = lam ** 2 * v
                keys = set(lhs) | set(rhs)
                dev += sum(abs(sp.nsimplify(lhs.get(k_, 0) - rhs.get(k_, 0))) for k_ in keys)
        good &= (dev == 0) if timed else (dev != 0)
ok("C.fall", good, "with the contact term timed by the local clock the two-walker generator obeys H_w T = lam T H_w for the joint "
   "translation in a uniform gradient (exact, w = 4^x, both coin sectors), so force = -(energy) x grad u for the pair, binding "
   "energy included; untimed it fails")

# ------------------------------------------------------------------ floating point: ring diagonalisation (the task's check)
def block_mat(L, K, s1, s2, Vv):
    """K block in the relative coordinate: Psi(x1, x2) = e^{iK x2} phi(x1 - x2), D = (i/2)(T - T^dag), (T psi)(x) = psi(x - 1)."""
    Hk = np.zeros((L, L), complex)
    for r_ in range(L):
        Hk[r_, (r_ - 1) % L] += s1 * 0.5j - s2 * 0.5j * np.exp(1j * K)
        Hk[r_, (r_ + 1) % L] += -s1 * 0.5j + s2 * 0.5j * np.exp(-1j * K)
    Hk[0, 0] += Vv
    return Hk
L = 64; Vv = -1.5; err = 0.0; ferm = 0.0; herm = 0.0; comm = 0.0
for n in range(L):
    K = 2 * np.pi * n / L
    Hco = block_mat(L, K, 1, 1, Vv); Hct = block_mat(L, K, 1, -1, Vv)
    herm = max(herm, np.abs(Hco - Hco.conj().T).max(), np.abs(Hct - Hct.conj().T).max())
    co = np.linalg.eigvalsh(Hco); ct = np.linalg.eigvalsh(Hct)
    err = max(err, abs(co[0] + math.sqrt(Vv ** 2 + 4 * math.sin(K / 2) ** 2)), abs(ct[0] + math.sqrt(Vv ** 2 + 4 * math.cos(K / 2) ** 2)))
    # exchange of two walkers with equal coins: (X phi)(r) = e^{iKr} phi(-r); antisymmetric walkers live on (1 - X)/2
    X = np.zeros((L, L), complex)
    for r_ in range(L):
        X[r_, (-r_) % L] = np.exp(1j * K * r_)
    comm = max(comm, np.abs(Hco @ X - X @ Hco).max())
    wv, U = np.linalg.eigh((np.eye(L) - X) / 2); Ua = U[:, wv > 0.5]
    Hf = Ua.conj().T @ Hco @ Ua
    ferm = max(ferm, -np.linalg.eigvalsh((Hf + Hf.conj().T) / 2)[0] - 2 * abs(math.sin(K / 2)))
print(f"note (floating) ring of {L}, V = {Vv} (blocks Hermitian to {herm:.0e}, exchange commuting to {comm:.0e}): every K block's lowest level matches E = -sqrt(V^2 + 4 sin^2(K/2)) (equal coins) and "
      f"-sqrt(V^2 + 4 cos^2(K/2)) (opposite coins) to {err:.0e}; antisymmetric equal-coin pairs never go below the continuum "
      f"(largest excursion {ferm:+.0e})")

# ------------------------------------------------------------------ floating point: 3D contact pairs near rest (grid secular equation)
from scipy.optimize import brentq
sgn = [np.array(m_, complex) for m_ in ([[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]])]
N1 = [np.kron(m_, np.eye(2)) for m_ in sgn]; N2 = [np.kron(np.eye(2), m_) for m_ in sgn]
def kin(Lg, Kv):
    qq = 2 * np.pi * (np.arange(Lg) + 0.5) / Lg
    Q = np.stack(np.meshgrid(qq, qq, qq, indexing="ij"), -1).reshape(-1, 3)
    h1 = np.sin(np.asarray(Kv) / 2 + Q); h2 = np.sin(np.asarray(Kv) / 2 - Q)
    Am = sum(h1[:, j, None, None] * N1[j] + h2[:, j, None, None] * N2[j] for j in range(3))
    return np.linalg.eigh(Am)
def levels(Vv, Kv, centre, half=0.45, Lg=32, npts=46):
    wv, U = kin(Lg, Kv)
    def ev(Ee):
        G = np.einsum("nij,nj,nkj->ik", U, 1.0 / (Ee - wv), U.conj()) / len(wv)
        return np.linalg.eigvalsh(Vv * G) - 1
    grid = np.linspace(centre - half, centre + half, npts); vals = np.array([ev(Ee) for Ee in grid]); out = []
    for i in range(4):
        sg_ = np.sign(vals[:, i])
        for k_ in np.nonzero(sg_[:-1] != sg_[1:])[0]:
            out.append(brentq(lambda Ee: ev(Ee)[i], grid[k_], grid[k_ + 1], xtol=1e-13))
    out = sorted(out); merged = []
    for e_ in out:
        if not merged or abs(e_ - merged[-1]) > 1e-9:
            merged.append(e_)
    return merged
rows = []
for Vv in (-4.0, -6.0, -10.0, -20.0):
    kk = 0.04
    hw = min(0.45, 1.5 / abs(Vv))                     # the two channels sit 4/|V| apart
    eS0 = levels(Vv, (0, 0, 0), Vv - 6 / abs(Vv), half=hw); eT0 = levels(Vv, (0, 0, 0), Vv - 2 / abs(Vv), half=hw)
    eSk = levels(Vv, (0, 0, kk), eS0[0], half=0.02); eTk = levels(Vv, (0, 0, kk), eT0[0], half=0.02)
    cS = (eSk[0] ** 2 - eS0[0] ** 2) / kk ** 2
    ct = sorted((e_ ** 2 - eT0[0] ** 2) / kk ** 2 for e_ in eTk)
    rows.append(f"V {Vv:g}: singlet c^2 {cS:+.3f} (series {-1 + 8 / Vv ** 2:+.3f}), triplet across {ct[-1]:+.3f} "
                f"({1 - 2 / Vv ** 2:+.3f}), along {ct[0]:+.3f} ({-1 - 4 / Vv ** 2:+.3f})")
print("note (floating) 3D contact pairs, secular equation on a 32^3 grid, E^2 = M^2 + c^2 K^2: " + "; ".join(rows))

# ------------------------------------------------------------------ floating point: a bound pair falling in a gradient (the task's check)
import scipy.sparse as sps
from scipy.sparse.linalg import expm_multiply
def fall(s1, s2, timed, Vv, g=0.004, Lc_=90, tmax=24.0):
    xs = np.arange(Lc_) - (Lc_ - 1) / 2; sq = np.exp(g * xs / 2)
    rw, cl, vl = [], [], []
    for a in range(Lc_):
        for b in range(Lc_):
            c_ = a * Lc_ + b
            for sg_, wk in ((s1, 0), (s2, 1)):
                for d in (1, -1):
                    pos = [a, b]; np_ = pos[wk] + d
                    if 0 <= np_ < Lc_:
                        t_ = list(pos); t_[wk] = np_
                        rw.append(t_[0] * Lc_ + t_[1]); cl.append(c_); vl.append(0.5j * (1 if d == 1 else -1) * sg_ * sq[pos[wk]] * sq[np_])
            if a == b:
                rw.append(c_); cl.append(c_); vl.append(Vv * (sq[a] ** 2 if timed else 1.0))
    Hs = sps.csr_matrix((vl, (rw, cl)), shape=(Lc_ ** 2,) * 2)
    Hs = (Hs + Hs.conj().T) / 2
    # initial pair at rest: the K = 0 bound state's relative profile under a Gaussian in the centre coordinate
    Lr = 41; Kb = np.zeros((Lr, Lr), complex)
    for r_ in range(Lr):
        if r_ + 1 < Lr:
            Kb[r_ + 1, r_] += s1 * 0.5j - s2 * 0.5j; Kb[r_, r_ + 1] += -s1 * 0.5j + s2 * 0.5j
    Kb[Lr // 2, Lr // 2] += Vv
    wv, U = np.linalg.eigh((Kb + Kb.conj().T) / 2); phi = U[:, 0]
    psi = np.zeros(Lc_ ** 2, complex); sig_ = 7.0
    for a in range(Lc_):
        for b in range(Lc_):
            rr = a - b + Lr // 2
            if 0 <= rr < Lr:
                psi[a * Lc_ + b] = phi[rr] * math.exp(-((xs[a] + xs[b]) / 2) ** 2 / (4 * sig_ ** 2))
    psi /= np.linalg.norm(psi)
    Xop = np.array([(xs[a] + xs[b]) / 2 for a in range(Lc_) for b in range(Lc_)])
    ts = np.linspace(0, tmax, 13); out = expm_multiply(-1j * Hs, psi, start=0, stop=tmax, num=13, endpoint=True)
    X = np.array([np.real(np.vdot(v, Xop * v)) for v in out])
    c = np.polyfit(ts, X, 2)
    return 2 * c[0] / g
aco_t = fall(1, 1, True, -1.5); aco_u = fall(1, 1, False, -1.5); act_t = fall(1, -1, True, -1.5)
print(f"note (floating) pairs at rest in w = e^(0.004 x) on a 90-site chain, a/g: equal coins, contact timed {aco_t:+.3f}, untimed "
      f"{aco_u:+.3f}; opposite coins (the only contact pair of antisymmetric walkers) timed {act_t:+.3f}")
print(f"runtime {time.time() - T0:.0f} s")

if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAILS)); sys.exit(1)
print("SUMMARY: PARTIAL binding gives a rest energy inside M2(C), but in 3D a contact-bound pair falls like everything else only "
      "when its coin triplet points across the gradient, and only as the binding grows: exact channel split, strong-binding "
      "series and exchange selection")
print("HIT: in 3D a contact pair at rest splits exactly into a singlet channel 1 = V I(E) and a triplet channel "
      "1 = V(2/(3E) + I(E)/3), I = <E/(E^2 - 4|h|^2)>; with <A^2> = 3 - sum cos K_i sigma1_i sigma2_i and <A^4> the strong-binding "
      "dispersion is E^2 = V^2 + 4 + 16/V^2 + (1 - 2/V^2)K_perp^2 - (1 + 4/V^2)K_par^2 (triplet, relative to its direction) and "
      "V^2 + 12 - 24/V^2 - (1 - 8/V^2)K^2 (singlet): timed, a pair falls at -g only as |V| grows and only across its direction.")
print("HIT: a contact term sees only the pair's amplitude at coincidence, where exchange acts on the coins alone: antisymmetric "
      "walkers bind only in the coin singlet (1D: opposite coins), whose band is inverted at rest, so their pairs fall up "
      f"(executed {act_t:+.2f} g); symmetric walkers bind only in the triplet (1D: equal coins with c = 1, executed {aco_t:+.2f} g "
      f"timed and {aco_u:+.2f} g untimed, and the inverted opposite-coin pair); under one record per site none of these exists.")
