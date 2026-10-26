#!/usr/bin/env python3
"""a-clause-for-one-light-cone, attempt 1.

Question: does any clause of the lane force alpha = K/4 (member's travelling
disturbances at the walker's top speed)?  Write rho = K/(4 alpha); the member's
two transverse-traceless modes have omega^2 = rho * wbar^2 * p^2 with
p^2 = sum_j 4 sin^2(q_j/2) (block 62 T4, quoted); the walker H = sum sigma_a S_a
has E = +-|s(k)|, s_j = sin k_j.  alpha = K/4  <=>  rho = 1.

Families
  S  setting: quoted formulas re-derived; the lane's clauses leave rho free
  A  exact one-sided threshold: same-band one-quantum emission/absorption by the
     free massless walker is excluded for all (k,q) iff rho >= 1
  B  pair-creation kinematics for a member quantum (the other side)
  C  block 135's operator identity re-run on a 5^3 torus (independent code),
     and the same identity for a walker with hop coefficient v: it fixes rho = v^2
  D  the kinetic_isotropy_primitive reading, and full-dispersion equality no-go

Exact arithmetic: Fractions and sympy; family C uses integer-valued complex
matrices (Gaussian integers times powers of 1/2 are scaled out; all entries and
all partial sums are small integers, exact in float64).
"""
import itertools
import random
import sys
import time
from fractions import Fraction as Fr

import numpy as np
import sympy as sp

T0 = time.time()
PASS = 0
FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
        print("PASS", name, detail)
    else:
        FAIL += 1
        print("FAIL", name, detail)


# --------------------------------------------------------------------------
# exact rational trigonometry
# --------------------------------------------------------------------------
def cs_from_t(t):
    """(cos, sin) of the angle with tan(angle/2) = t, exactly."""
    t = Fr(t)
    d = 1 + t * t
    return (1 - t * t) / d, 2 * t / d


def sub_angle(c1, s1, c2, s2):
    """cos, sin of (angle1 - angle2)."""
    return c1 * c2 + s1 * s2, s1 * c2 - c1 * s2


def add_angle(c1, s1, c2, s2):
    return c1 * c2 - s1 * s2, s1 * c2 + c1 * s2


def double(c, s):
    return c * c - s * s, 2 * s * c


def sqrt_cmp_less(A, B, P):
    """exact test of (sqrt A - sqrt B)^2 < P for rationals A,B >= 0, P >= 0."""
    m = A + B - P
    if m < 0:
        return True
    return m * m < 4 * A * B


def sqrt_cmp_geq_sum(A, B, C):
    """exact test of sqrt A + sqrt B >= sqrt C."""
    m = C - A - B
    if m <= 0:
        return True
    return 4 * A * B >= m * m


# ==========================================================================
# Family S: setting
# ==========================================================================
al, K, w, ad, ab = sp.symbols("alpha K wbar alphadot beta", positive=True)
a_t = sp.Function("a")
t = sp.symbols("t")
p2 = sp.symbols("p2", positive=True)

# S1: restricted TT action  alpha*adot^2 - K p^2 a^2/4  (quoted: block 149 premises,
#     docs/ADMISSIBILITY_RULE_A_FREE_WALKER...:27; block 62 T4 :73) -> omega^2 = K p^2/(4 alpha)
Lag = al * sp.diff(a_t(t), t) ** 2 - K * p2 * a_t(t) ** 2 / 4
eom = sp.diff(sp.diff(Lag, sp.diff(a_t(t), t)), t) - sp.diff(Lag, a_t(t))
om = sp.symbols("omega", positive=True)
res = sp.simplify(eom.subs(a_t(t), sp.cos(om * t)).doit() / sp.cos(om * t))
omega_sol = sp.solve(sp.Eq(res, 0), om)
check("S1 TT mode: omega^2 = K p^2/(4 alpha) = rho p^2",
      len(omega_sol) == 1 and sp.simplify(omega_sol[0] ** 2 - K * p2 / (4 * al)) == 0)

# S2: kinetic sign (block 60 T3(b), quoted c_k = 12 alpha + 36 beta): at beta=-alpha it is -24 alpha < 0
ck = 12 * al + 36 * (-al)
check("S2 c_k at beta=-alpha equals -24 alpha, negative for every alpha>0 (no K/alpha dependence)",
      sp.simplify(ck + 24 * al) == 0 and sp.simplify(ck.subs(al, 1)) < 0)

# S3: Legendre coefficient c = beta/(alpha+3 beta) = 1/2  iff  beta = -alpha  (block 112 T1 condition; no K)
cc = sp.symbols("cc")
beta_r = sp.symbols("beta_r", real=True)
s3 = sp.solve(sp.Eq(beta_r / (al + 3 * beta_r), sp.Rational(1, 2)), beta_r)
check("S3 closure condition c=beta/(alpha+3beta)=1/2 <=> beta=-alpha (independent of K)",
      s3 == [-al])

# S4: every lane condition used here is a condition on beta/alpha or on signs; sweep rho
def lane_ok(Kv, alv):
    betav = -alv
    sign_ok = (12 * alv + 36 * betav) < 0                 # block 60 T3
    osc_ok = (alv > 0 and Kv > 0 and (alv + betav) == 0)  # modes need K>0, alpha>0 (block 62 T4); closing ratio beta=-alpha (block 112 T1)
    close_ok = (betav / (alv + 3 * betav) == Fr(1, 2))    # block 112 T1
    return sign_ok and osc_ok and close_ok


allok = True
rhos = [Fr(1, 100), Fr(1, 9), Fr(1, 4), Fr(1, 2), Fr(1), Fr(2), Fr(9), Fr(100)]
for r in rhos:
    alv = Fr(1)
    Kv = 4 * alv * r
    allok = allok and lane_ok(Kv, alv)
check("S4 lane conditions (sign, closure, oscillation) hold for rho in %s" % [str(r) for r in rhos], allok)

# S5: rho is a ratio of two squared speeds, invariant under a common rescaling of time
L_, rho_, pp = sp.symbols("L rho pp", positive=True)
ratio = sp.simplify((rho_ * (L_ * w) ** 2 * pp) / ((L_ * w) ** 2 * pp))
check("S5 rho = omega_member^2/omega_walker^2 at long wavelength is invariant under w -> L w (block 60 T1(a))",
      sp.simplify(ratio - rho_) == 0)

# ==========================================================================
# Family A: exact threshold for same-band emission
# ==========================================================================
k_, h_ = sp.symbols("k h", real=True)
# A1: sin k - sin(k-2h) = 2 cos(k-h) sin h ; |p|^2 - |s(k)-s(k-q)|^2 = sum 4 sin^2 h sin^2(k-h)
chk1 = sp.simplify(sp.sin(k_) - sp.sin(k_ - 2 * h_) - 2 * sp.cos(k_ - h_) * sp.sin(h_))
chk2 = sp.simplify(4 * sp.sin(h_) ** 2 - (2 * sp.cos(k_ - h_) * sp.sin(h_)) ** 2
                   - 4 * sp.sin(h_) ** 2 * sp.sin(k_ - h_) ** 2)
check("A1 sin k - sin(k-q) = 2cos(k-q/2) sin(q/2); gap = 4 sin^2(q/2) sin^2(k-q/2) per axis",
      chk1 == 0 and chk2 == 0)

# A2: exact sweep of  ||s(k)|-|s(k-q)|| < |p(q)|  (rho = 1; implies rho >= 1)
random.seed(20261025)


def rand_t():
    return Fr(random.choice([0, 1, -1, 2, -2, 3, -3, 1, 5, 7, 11, 13])) / random.choice([1, 2, 3, 5, 7, 11])


def vec_data(kt, ht):
    """returns |s(k)|^2, |s(k-q)|^2, |p(q)|^2, |s(k+q)|^2, |s(q)|^2 for q = 2h componentwise."""
    A = B = P = Cc = Sq = Fr(0)
    for tk, th in zip(kt, ht):
        ck_, sk_ = cs_from_t(tk)
        ch_, sh_ = cs_from_t(th)
        c2h, s2h = double(ch_, sh_)
        _, skm = sub_angle(ck_, sk_, c2h, s2h)     # sin(k - 2h)
        _, skp = add_angle(ck_, sk_, c2h, s2h)     # sin(k + 2h)
        A += sk_ * sk_
        B += skm * skm
        Cc += skp * skp
        P += 4 * sh_ * sh_
        Sq += s2h * s2h
    return A, B, P, Cc, Sq


nA = 0
okA = True
for _ in range(6000):
    kt = [rand_t() for _ in range(3)]
    ht = [rand_t() for _ in range(3)]
    if all(th == 0 for th in ht):
        continue
    A, B, P, Cc, Sq = vec_data(kt, ht)
    nA += 1
    if not sqrt_cmp_less(A, B, P):
        okA = False
        break
check("A2 exact sweep (%d points incl. zero-sine components): (|s(k)|-|s(k-q)|)^2 < |p(q)|^2, hence no emission/absorption for any rho>=1" % nA, okA)

# A3: general proof for rho<1 and exact witnesses
a_ = sp.symbols("a", positive=True)
ident = sp.simplify(sp.sin(k_) - sp.sin(2 * a_ - k_) - 2 * sp.cos(a_) * sp.sin(k_ - a_))
check("A3 identity: sin k - sin(2a-k) = 2 cos a sin(k-a)  (emission along an axis with q = 2(k-a))", ident == 0)

pyth = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29), (9, 40, 41), (48, 55, 73), (65, 72, 97)]
nwit = 0
okW = True
rho_list = []
for (x, y, z) in pyth:
    for (cx, sx) in ((Fr(x, z), Fr(y, z)), (Fr(y, z), Fr(x, z))):   # cos a, sin a, both orders
        rho = cx * cx
        if rho >= 1:
            continue
        rho_list.append(rho)
        c2a, s2a = double(cx, sx)
        found = 0
        for tt in [Fr(n, d) for n in range(1, 60) for d in (1, 2, 3, 4, 5, 7, 8, 10, 13)]:
            ckk, skk = cs_from_t(tt)
            # window: sin k >0, sin(k-a)>0, sin(2a-k)>0
            _, s_ka = sub_angle(ckk, skk, cx, sx)
            _, s_2ak = sub_angle(c2a, s2a, ckk, skk)
            if not (skk > 0 and s_ka > 0 and s_2ak > 0):
                continue
            # k angle in (a,2a)  <=>  these three signs (angles within (0,pi))
            half_q = sub_angle(ckk, skk, cx, sx)       # (cos, sin)(q/2), q/2 = k-a
            sin_h = half_q[1]
            q_abs_p = 2 * abs(sin_h)                    # |p(q)| along the axis
            ck2, sk2 = double(*half_q)                  # cos q, sin q
            _, s_kq = sub_angle(ckk, skk, ck2, sk2)     # sin(k - q)
            lhs = abs(skk) - abs(s_kq)
            rhs = cx * q_abs_p                           # sqrt(rho) |p(q)|, sqrt(rho)=cos a
            if lhs != rhs or q_abs_p == 0:
                okW = False
            found += 1
            nwit += 1
            if found >= 6:
                break
        if found == 0:
            okW = False
check("A4 exact emission witnesses: E(k)-E(k-q) = sqrt(rho)|p(q)| with q != 0, %d witnesses over rho in %s"
      % (nwit, sorted(set(str(r) for r in rho_list))), okW and nwit > 0)

# A5: universal witness for rho = cos^2 a < 1: k = 3a/2, q = a (so k-q = a/2 > 0): E(k)-E(k-q) = cos a * |p(q)|
check("A5 universal witness k=3a/2, q=a: sin(3a/2) - sin(a/2) = 2 cos a sin(a/2) = sqrt(rho)|p(q)|, with sin(a/2)>0 and q=a != 0 for every a in (0,pi/2)",
      sp.simplify(sp.sin(3 * a_ / 2) - sp.sin(a_ / 2) - 2 * sp.cos(a_) * sp.sin(a_ / 2)) == 0)

# A6: ratio along an axis for k>q>0 is cos(k-q/2) -> 1 along k=2q, q->0 (supremum 1, not attained)
kk, qq = sp.symbols("kk qq", positive=True)
ratio_axis = sp.simplify((sp.sin(kk) - sp.sin(kk - qq)) / (2 * sp.sin(qq / 2)))
check("A6 axis ratio (sin k - sin(k-q))/(2 sin(q/2)) = cos(k-q/2) for k>q>0; along k=2q it tends to 1 as q->0 (supremum 1)",
      sp.simplify(ratio_axis - sp.cos(kk - qq / 2)) == 0 and sp.limit(sp.cos(2 * qq - qq / 2), qq, 0) == 1)

# A7: for rho = c^2, c = n/40 (n=1..39): the universal witness, exactly (s = sin(a/2) = sqrt((1-c)/2) > 0)
s_half = sp.symbols("s_half", positive=True)
okA7 = True
for n in range(1, 40):
    c = sp.Rational(n, 40)
    sin3 = s_half * (1 + 2 * c)          # sin(3a/2) = sin(a/2)(3 - 4 sin^2(a/2)) = sin(a/2)(1+2cos a)
    okA7 = okA7 and sp.simplify(sin3 - s_half - c * 2 * s_half) == 0 and (1 + 2 * c) > 0
check("A7 universal witness for rho=(n/40)^2, n=1..39: E(k)-E(k-q) - sqrt(rho)|p(q)| = 0 using sin(3a/2)=sin(a/2)(1+2cos a)", okA7)

# ==========================================================================
# Family B: pair creation by a member quantum (supplied quantum energy sqrt(rho)|p(q)|, filled lower band)
# ==========================================================================
h1, h2, h3, rr = sp.symbols("h1 h2 h3 rho", real=True)
hs = [h1, h2, h3]
lhs_B1 = sum(4 * sp.sin(x) ** 2 * sp.cos(x) ** 2 for x in hs) - rr * sum(4 * sp.sin(x) ** 2 for x in hs)
rhs_B1 = sum(4 * sp.sin(x) ** 2 * (sp.cos(x) ** 2 - rr) for x in hs)
check("B1 |s(q)|^2 - rho |p(q)|^2 = sum 4 sin^2(q_j/2)(cos^2(q_j/2) - rho)", sp.simplify(lhs_B1 - rhs_B1) == 0)

# B2: subadditivity |s(k)| + |s(k+q)| >= |s(q)| (so pair energy >= |s(q)|), exact sweep
okB2 = True
nB2 = 0
for _ in range(4000):
    kt = [rand_t() for _ in range(3)]
    ht = [rand_t() for _ in range(3)]
    A, B, P, Cc, Sq = vec_data(kt, ht)
    nB2 += 1
    if not sqrt_cmp_geq_sum(A, Cc, Sq):
        okB2 = False
        break
check("B2 exact sweep (%d pts): |s(k)|+|s(k+q)| >= |s(q)|  (minimal pair energy at momentum q is |s(q)|)" % nB2, okB2)

# B3: for rho<1 pair creation closed when every cos^2(q_j/2) > rho (then sqrt(rho)|p| < |s(q)| <= pair energy)
okB3 = True
cnt3 = 0
for rho in (Fr(9, 25), Fr(16, 25), Fr(25, 169), Fr(1, 4), Fr(99, 100)):
    for _ in range(300):
        ht = [rand_t() for _ in range(3)]
        cos2 = [cs_from_t(th)[0] ** 2 for th in ht]
        if not all(c > rho for c in cos2):
            continue
        if all(th == 0 for th in ht):
            continue
        P = sum(4 * cs_from_t(th)[1] ** 2 for th in ht)
        Sq = sum((double(*cs_from_t(th))[1]) ** 2 for th in ht)
        cnt3 += 1
        if not (rho * P < Sq):
            okB3 = False
check("B3 rho<1: rho|p|^2 < |s(q)|^2 whenever all cos^2(q_j/2) > rho (%d exact cases)" % cnt3, okB3 and cnt3 > 0)

# B4: for rho >= 1 and small axis q: F(0,q)=|s(q)| <= sqrt(rho)|p| <= F(k*,q)=2|cos(q/2)|  => resonance by IVT
okB4 = True
cnt4 = 0
for rho in (Fr(1), Fr(5, 4), Fr(4), Fr(25), Fr(400)):
    # axis q = (2h,0,0): need cos^2 h + 2 >= rho sin^2 h ; pick small rational h
    for th in (Fr(1, 40), Fr(1, 20), Fr(1, 10), Fr(1, 5)):
        ch, sh = cs_from_t(th)
        if not (ch * ch + 2 >= rho * sh * sh):
            continue
        c2h, s2h = double(ch, sh)
        Fmin2 = s2h * s2h                      # |s(q)|^2
        target2 = rho * 4 * sh * sh            # rho |p|^2
        Fk2 = 4 * (ch * ch + 2)                # (2|cos h-vector|)^2 with k* = pi/2 - h in every axis
        cnt4 += 1
        if not (Fmin2 <= target2 <= Fk2):
            okB4 = False
check("B4 rho>=1: |s(q)|^2 <= rho|p|^2 <= (pair energy at k*)^2 for small axis q (%d cases), so a pair resonance exists (IVT)" % cnt4,
      okB4 and cnt4 > 0)

# B4b: closed form on the axis: cos^2 h + 2 >= rho sin^2 h  <=>  sin^2 h <= 3/(1+rho)
sh2 = sp.symbols("sh2", positive=True)
cond = sp.simplify((1 - sh2) + 2 - rr * sh2 - (3 - (1 + rr) * sh2))
check("B4b on the axis the open-resonance condition cos^2 h + 2 >= rho sin^2 h is exactly sin^2(q/2) <= 3/(1+rho): satisfiable for every rho",
      cond == 0)

# B5: rho = 1 exact resonance for every q (k = -q/2): |s(-q/2)|+|s(q/2)| = |p(q)|
chk = sp.simplify(sum(4 * sp.sin(x) ** 2 for x in hs) - (2 * sp.sqrt(sum(sp.sin(x) ** 2 for x in hs))) ** 2)
check("B5 rho=1: pair (-q/2, +q/2) has energy exactly |p(q)| for every q (block 149 T5, re-derived)", chk == 0)

# B6: case split over rho = n/40, n = 1..160
okB6 = True
for n in range(1, 161):
    rho = Fr(n, 40)
    if rho < 1:
        okB6 = okB6 and (rho < 1)                      # emission: A5/A7 (universal witness)
    else:
        # exists small axis half-angle with sin^2 h <= 3/(1+rho): take sin^2 h = 1/(1+rho)/2... exact rational check
        sh_sq = Fr(1, 2) * Fr(3) / (1 + rho)
        okB6 = okB6 and ((1 - sh_sq) + 2 >= rho * sh_sq)
check("B6 case split, rho = n/40, n=1..160: rho<1 -> walker emission witness (A5,A7); rho>=1 -> pair channel open at a small axis q (B4b)", okB6)

# ==========================================================================
# Family C: block 135's identity, independent re-run on the 5^3 torus; walker with hop coefficient v
# ==========================================================================
L = 5
NS = L ** 3
DIM = 2 * NS


def sid(x):
    return ((x[0] % L) * L + (x[1] % L)) * L + (x[2] % L)


sites = [(a, b, c) for a in range(L) for b in range(L) for c in range(L)]
I2 = np.eye(2, dtype=complex)
sig = [np.array([[0, 1], [1, 0]], dtype=complex),
       np.array([[0, -1j], [1j, 0]], dtype=complex),
       np.array([[1, 0], [0, -1]], dtype=complex)]


def Tsite(a, p):
    M = np.zeros((NS, NS), dtype=complex)
    for s in sites:
        y = list(s)
        y[a] += p
        M[sid(s), sid(y)] = 1                    # (T psi)(x) = psi(x+e)
    return M


Tm = [[Tsite(a, 1), Tsite(a, -1)] for a in range(3)]
H2 = sum(np.kron(Tm[a][0] - Tm[a][1], sig[a]) for a in range(3))      # H = (-i/2) H2
P2 = [np.kron(Tm[j][0] @ Tm[j][0] - Tm[j][1] @ Tm[j][1], I2) for j in range(3)]   # P_j = (-i/4) P2_j


def proj(s):
    M = np.zeros((NS, NS), dtype=complex)
    M[sid(s), sid(s)] = 1
    return np.kron(M, I2)


def comm(A, B):
    return A @ B - B @ A


def shift_idx(d):
    idx = np.zeros(DIM, dtype=int)
    for s in sites:
        tt = tuple(s[i] - d[i] for i in range(3))
        for c in range(2):
            idx[2 * sid(s) + c] = 2 * sid(tt) + c
    return idx


IDX_CACHE = {}


def sidx(d):
    d = tuple(x % L for x in d)
    if d not in IDX_CACHE:
        IDX_CACHE[d] = shift_idx(d)
    return IDX_CACHE[d]


def energy_density(H2v, x):
    P = proj(x)
    return (-1j / 4) * (P @ H2v + H2v @ P)       # Re psi^dag (H psi) at x, H = (-i/2) H2v


def averaged_energy(H2v, x, average=True):
    if not average:
        return energy_density(H2v, x)
    S = 0
    for e in itertools.product([1, -1], repeat=3):
        S = S + energy_density(H2v, tuple(x[i] + e[i] for i in range(3)))
    return S / 8


def bond_B(a, y, v):
    M = np.zeros((NS, NS), dtype=complex)
    M[sid(tuple(y[i] + (1 if i == a else 0) for i in range(3))), sid(y)] = 1
    Bm = np.kron(M, sig[a]) * v                  # hop coefficient v on the bond term
    return Bm + Bm.conj().T


def base_currents(v):
    x0 = (0, 0, 0)
    K0 = {}
    for i in range(3):
        B = bond_B(i, x0, v)
        for j in range(3):
            K0[(i, j)] = (-1j / 16) * (B @ P2[j] + P2[j] @ B)     # K_i^j = (1/4){B, P_j}
    return K0


def Theta(K0, i, j, y, transverse=True, forward=True):
    others = [l for l in range(3) if l != j]
    S = 0
    cnt = 0
    for sj in ((0, 1) if forward else (0,)):
        for s1 in ((1, -1) if transverse else (0,)):
            for s2 in ((1, -1) if transverse else (0,)):
                if not transverse and (s1, s2) != (0, 0):
                    continue
                d = list(y)
                d[j] += sj
                d[others[0]] += s1
                d[others[1]] += s2
                idx = sidx(d)
                S = S + K0[(i, j)][np.ix_(idx, idx)]
                cnt += 1
    return S / cnt


def double_div(K0, **kw):
    R = 0
    for i in range(3):
        for j in range(3):
            for si in (0, 1):
                for sj in (0, 1):
                    y = [0, 0, 0]
                    if si:
                        y[i] -= 1
                    if sj:
                        y[j] -= 1
                    R = R + (-1) ** (si + sj) * Theta(K0, i, j, tuple(y), **kw)
    return R


def best_fit(Lm, Rm):
    num = np.vdot(Rm, Lm)
    den = np.vdot(Rm, Rm)
    c = (num / den).real
    return c, np.abs(Lm - c * Rm).max()


x0 = (0, 0, 0)
fit = {}
for v in (1, 2, 3):
    H2v = v * H2
    Ep = averaged_energy(H2v, x0)
    LHS = 0.25 * comm(H2v, comm(H2v, Ep))          # -[H,[H,E']] with H = (-i/2) H2v
    K0 = base_currents(v)
    RHS = double_div(K0)                            # D Theta_v : sum_ij  nabla_i nabla_j Theta_ij
    c, res = best_fit(LHS, RHS)
    fit[v] = (c, res, abs(LHS).max(), abs(RHS).max())
    check("C%d walker hop coefficient v=%d: -[H,[H,e']] = c * sum nabla_i nabla_j Theta_ij exactly, c = v^2 = %d"
          % (v, v, v * v), res == 0 and c == float(v * v) and abs(LHS).max() > 0,
          "(c=%r, residual=%r, |LHS|max=%g)" % (c, res, abs(LHS).max()))

# C4: mutants fail (the check is not vacuous); v = 1
H2v = H2
K0 = base_currents(1)
Ep = averaged_energy(H2v, x0)
LHS1 = 0.25 * comm(H2v, comm(H2v, Ep))
LHS_unavg = 0.25 * comm(H2v, comm(H2v, averaged_energy(H2v, x0, average=False)))
c_u, r_u = best_fit(LHS_unavg, double_div(K0))
check("C4a mutant: unaveraged site energy e (not e') has no constant c (block 135 T2 factor prod cos q)", r_u > 1e-9, "(residual=%g)" % r_u)
c_t, r_t = best_fit(LHS1, double_div(K0, transverse=False))
check("C4b mutant: stress without the transverse average (phi_j = (1+T_j)/2 only) has no constant c (block 135 T3(b))", r_t > 1e-9, "(residual=%g)" % r_t)
c_f, r_f = best_fit(LHS1, double_div(K0, transverse=False, forward=False))
check("C4c mutant: stress K_i^j at the bond itself (no phi_j) has no constant c", r_f > 1e-9, "(residual=%g)" % r_f)
c_s, r_s = best_fit(LHS1, -double_div(K0))
check("C4d mutant: opposite sign gives c = -1, not +1 (orientation of the check)", c_s == -1.0 and r_s == 0, "(c=%r)" % c_s)

# C5: consequence.  The member demands e'' = rho * (D Theta) (block 112 T3 / block 135 T4(a)), rho = K wbar^2/(4 alpha);
# a walker with hop coefficient v supplies e'' = v^2 (D Theta_v), D Theta_v != 0.  Equal iff rho = v^2.
vals = {v: fit[v][0] for v in fit}
check("C5 the source-link identity fixes rho = v^2 (C1-C3): alpha = K wbar^2/(4 v^2); the clause alone does not fix alpha/K",
      all(vals[v] == v * v for v in vals) and all(fit[v][3] > 0 for v in fit))

# ==========================================================================
# Family D: the registered primitive, and equality of full dispersions
# ==========================================================================
# D1: Euclidean TT action alpha (d_tau a)^2 + (K/4)(d_x a)^2 is symmetric under tau <-> x iff alpha = K/4
tau_c, x_c = sp.symbols("c_tau c_x", positive=True)
sol_D1 = sp.solve(sp.Eq(al, K / 4), al)
swap_cond = sp.simplify((al - K / 4))
check("D1 READING: TT sector Euclidean coefficients (alpha for d_tau^2, K/4 for d_x^2) exchange iff alpha = K/4",
      sol_D1 == [K / 4] and sp.simplify(swap_cond.subs(al, K / 4)) == 0)

# D2: full lattice dispersions: omega_m^2 - omega_w^2 = sum_j 4 sin^2 h (rho - cos^2 h); at rho=1 it is sum 4 sin^4 h
D2 = sum(4 * sp.sin(x) ** 2 * (rr - sp.cos(x) ** 2) for x in hs)
check("D2 omega_m^2 - omega_w^2 at rho=1 equals sum_j 4 sin^4(q_j/2) >= 0 (zero only at q = 0 mod 2pi)",
      sp.simplify(D2.subs(rr, 1) - sum(4 * sp.sin(x) ** 4 for x in hs)) == 0)

# D3: no rho makes the full dispersions equal: axis q: rho = cos^2 h for all h, impossible
ok_D3 = True
for rho in (Fr(1, 4), Fr(1, 2), Fr(1), Fr(3, 4), Fr(2)):
    diffs = []
    for th in (Fr(1, 3), Fr(1, 2)):
        ch, sh = cs_from_t(th)
        diffs.append(4 * sh * sh * (rho - ch * ch))
    ok_D3 = ok_D3 and not (diffs[0] == 0 and diffs[1] == 0)
check("D3 no rho in the test set equates the full member and walker dispersions at two axis momenta: exact equality of cones (not just long-wavelength speeds) is unattainable",
      ok_D3)

# ==========================================================================
print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
print("runtime %.1f s" % (time.time() - T0))
if FAIL == 0:
    print("HIT: (kinematics, continuum momenta, supplied one-quantum energy sqrt(rho)|p(q)| with rho = K/(4 alpha)) the free massless walker E=|sin k| "
          "cannot emit or absorb one member quantum in its own band for any (k, q != 0) iff rho >= 1 (alpha <= K/4), with an exact emission witness "
          "(k = 3a/2, q = a, cos a = sqrt(rho)) for every rho < 1; for every rho >= 1 a member quantum with sin^2(q/2) <= 3/(1+rho) on an axis "
          "has a resonant walker particle-hole channel (intermediate-value argument), so no stability clause selects rho = 1; and block 135's "
          "source identity, re-run independently on a 5^3 torus, holds for a walker of hop coefficient v exactly with constant v^2, so the "
          "source-link clause fixes rho = v^2 (alpha = K wbar^2/(4 v^2)), not alpha/K by itself.")
    print("SUMMARY: PARTIAL a stability clause gives only the one-sided bound alpha <= K/4 (sharp), the source link gives rho = v^2 for the walker's hop coefficient, and alpha = K/4 needs both a source-link clause and a statement that the walker's hop coefficient is one edge per tick (the kinetic_isotropy_primitive at matter scope) or an extension of that primitive to the member's kinetic form.")
else:
    print("SUMMARY: FAILED some checks; no claim is made.")
sys.exit(0 if FAIL == 0 else 1)
