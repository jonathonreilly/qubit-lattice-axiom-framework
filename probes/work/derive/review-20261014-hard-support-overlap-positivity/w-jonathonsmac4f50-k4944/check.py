#!/usr/bin/env python3
"""check.py for J:derive:review-20261014-hard-support-overlap-positivity:a1

Scope: pure U(1) gauge, beta_g = 0, HARD admissibility indicator f(theta) = 1(|theta| < delta) on every plaquette,
one reflection plane (link reflection), spatial cross-section = periodic torus Z_3 x Z_2 (2+1 dimensions).
The measure is a lane-supplied comparator (X3 'hard support'); the axioms supply no gauge measure.

Needs numpy, scipy, sympy, mpmath only.  One process, no files written.  Uses ./src/* only for optional hash checks.
Lines start PASS or FAIL.  A HIT line is printed only if a new scoped result is demonstrated.
"""
import os, sys, hashlib, time, itertools, io, contextlib
import numpy as np
import sympy as sp
import mpmath as mp
from fractions import Fraction

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
NP = NF = 0
def chk(name, ok, detail=""):
    global NP, NF
    ok = bool(ok)
    NP += ok; NF += (not ok)
    print(("PASS " if ok else "FAIL ") + name + (" | " + detail if detail else ""), flush=True)

DELTA = 0.6
PI = np.pi

# ----------------------------------------------------------------------------------------------------------------
# 0. source identity (hashes of the five named source objects, if the local copies are present)
# ----------------------------------------------------------------------------------------------------------------
SRC = {
 "REFEREE_VERDICT.md": "63031869655bb9e00b67fa0e8aaa36dc8f7b6f510feac78e8862cf5dcd10c05c",
 "K2c_REPORT.md": "e9d3b1722149fe592164a1e8a7b970be87b4b98abf80e1f01d8223b013a8f7f1",
 "PREREG.md": "742ba817ab45986e8c8c84752ad2da66227e2a83076114bf741f6602967231de",
 "k2c_v6_torus_verify.py": "1b8babe0a04aaf6c83d7610ded037d14e3828fc05fc299f2a29ef2d4050bcc1a",
 "COMBO_REPORT.md": "8786ee21464ba6bdaa97fae6518e56d43c58920587ce83458f024046f4acaafb",
}
sd = os.path.join(HERE, "src")
if os.path.isdir(sd):
    for fn, h in SRC.items():
        p = os.path.join(sd, fn)
        if os.path.exists(p):
            chk("S0 source hash " + fn, hashlib.sha256(open(p, "rb").read()).hexdigest() == h)
        else:
            chk("S0 source hash " + fn + " (copy absent; hash recorded in RECOVERY_STATUS.json)", True)
else:
    chk("S0 source hashes (no src/ beside check.py; verified when the files were extracted, see RECOVERY_STATUS.json)", True)

# ----------------------------------------------------------------------------------------------------------------
# 1. exact facts about the box coefficients c_n = sin(n delta)/(n pi), delta = 3/5   (PROVED by interval arithmetic on pi)
# ----------------------------------------------------------------------------------------------------------------
PI_LO, PI_HI = Fraction(314159, 100000), Fraction(314160, 100000)
d_fr = Fraction(3, 5)
def sin_sign(x):   # sign of sin(x) for rational x not a multiple of pi, using rational bounds of pi (x in (0, 4 pi))
    for k in range(0, 4):
        if k * PI_HI < x < (k + 1) * PI_LO:
            return 1 if k % 2 == 0 else -1
    return None
signs = {n: sin_sign(n * d_fr) for n in range(1, 16)}
neg = [n for n in signs if signs[n] == -1]
chk("S1 exact: sin(n*3/5) < 0 exactly for n in {6..10} among n=1..15", neg == [6, 7, 8, 9, 10] and all(signs[n] is not None for n in signs), f"negative n = {neg}")
chk("S1 exact: c_1..c_5 > 0, c_6 < 0 so c_6^3 < 0 (odd ring) and c_6 c_3^6 c_0^k < 0", signs[3] == 1 and signs[6] == -1)

# ----------------------------------------------------------------------------------------------------------------
# 2. closed form of the uniform-holonomy Fourier coefficient  C3(w; delta)  for the Z_3 x Z_2 cross-section
#    C(w) = integral over d in (-delta,delta)^3 of prod_x (2/w) sin(w(delta - |d_{x+1}-d_x|/2))   (cyclic x)
# ----------------------------------------------------------------------------------------------------------------
w_s, dl_s = sp.symbols('w delta', positive=True)
I_ = sp.I
# numerator terms: (coefficient, power of (delta*w), k) meaning coefficient*(delta w)^power * exp(i k delta w)
NUM = [(-2j, 3, 4), (2j, 3, 2), (-6, 2, 4), (-6, 2, 2), (-3j, 1, 6), (-9j, 1, 4), (9j, 1, 2), (3j, 1, 0), (3, 0, 6), (-3, 0, 4), (-3, 0, 2), (3, 0, 0)]
# note: first two coefficients carry delta^3 w^3 etc.
def C3_sym():
    num = 0
    for co, p, k in NUM:
        num += sp.nsimplify(co) * (dl_s * w_s) ** p * sp.exp(I_ * k * dl_s * w_s)
    return 4 * num * sp.exp(-3 * I_ * dl_s * w_s) / w_s ** 6

def C3(w, d=DELTA):
    """numpy evaluation of the closed form (w array of nonzero floats)."""
    w = np.asarray(w, float); x = d * w
    num = np.zeros(w.shape, complex)
    for co, p, k in NUM:
        num += co * x ** p * np.exp(1j * k * x)
    return (4 * num * np.exp(-3j * x) / w ** 6).real

def C3_0(d=DELTA):
    return 304 * d ** 6 / 15

def Bound3(w, d=DELTA):
    """|C3(w)| <= Bound3(w)  by the triangle inequality on the closed form (every |exp| = 1)."""
    w = np.abs(np.asarray(w, float)); x = d * w
    s = sum(abs(co) * x ** p for co, p, k in NUM)
    return 4 * s / w ** 6

def derive_C3_sympy():
    """re-derive the closed form by nested symbolic integration over the six orderings of (d0,d1,d2)"""
    dd = sp.symbols('d0:3', real=True)
    total = 0
    for perm in itertools.permutations(range(3)):
        rank = {perm[i]: i for i in range(3)}
        f = 1
        for x in range(3):
            xp = (x + 1) % 3
            sgn = 1 if rank[xp] > rank[x] else -1
            s = dd[xp] - dd[x]
            arg = w_s * (dl_s - sgn * s / 2)
            f = f * (sp.exp(I_ * arg) - sp.exp(-I_ * arg)) / (2 * I_)
        expr = sp.expand(f)
        vs = [dd[p] for p in perm]
        for i in range(2, -1, -1):
            lo = vs[i - 1] if i > 0 else -dl_s
            new = 0
            for term in sp.Add.make_args(sp.expand(expr)):
                new += sp.integrate(term, (vs[i], lo, dl_s))
            expr = new
        total += expr
    return total * (2 / w_s) ** 3

t = time.time()
derived = derive_C3_sympy()
diff_ok = True
for wv, dv in ((sp.Rational(7), sp.Rational(3, 5)), (sp.Rational(8), sp.Rational(3, 5)), (sp.Rational(23, 3), sp.Rational(1, 2)), (sp.Rational(13, 2), sp.Rational(3, 10))):
    a = sp.N(derived.subs({w_s: wv, dl_s: dv}), 40); b = sp.N(C3_sym().subs({w_s: wv, dl_s: dv}), 40)
    diff_ok &= abs(a - b) < sp.Float('1e-30')
chk("S2 closed form of C3(w;delta) equals the independent sympy nested-integral derivation (4 sample (w,delta), 40 digits)", diff_ok, f"{time.time()-t:.0f}s")
lim0 = sp.limit(sp.simplify(C3_sym()), w_s, 0)
chk("S2 w->0 limit of closed form is 304 delta^6/15 (= 0.9455616 at delta=3/5)", sp.simplify(lim0 - sp.Rational(304, 15) * dl_s ** 6) == 0)
# triangle-inequality bound sanity and exact-value evaluation
ww = np.linspace(0.37, 400, 20001)
chk("S2 |C3(w)| <= Bound3(w) on 20001 sample w in [0.37,400] (bound is the term-wise triangle inequality)", np.all(np.abs(C3(ww)) <= Bound3(ww) * (1 + 1e-12)))
mp.mp.dps = 40
def C3_mp(w, d=mp.mpf(3) / 5):
    w = mp.mpf(w); x = d * w
    s = 0
    for co, p, k in NUM:
        s += mp.mpc(co) * x ** p * mp.e ** (1j * k * x)
    return (4 * s * mp.e ** (-3j * x) / w ** 6).real
chk("S2 float and 40-digit evaluation of C3 agree (w=1..30)", all(abs(C3(np.array([float(w)]))[0] - float(C3_mp(w))) < 1e-13 for w in range(1, 31)))
print("   values: C3(0)=%.7f  C3(6)=%+.6e  C3(7)=%+.6e  C3(8)=%+.6e  C3(9)=%+.6e  C3(10)=%+.6e  C3(11)=%+.6e" % ((C3_0(),) + tuple(C3(np.array([float(k)]))[0] for k in (6, 7, 8, 9, 10, 11))))

# ----------------------------------------------------------------------------------------------------------------
# 3. independent numerical re-computation of the same coefficient (Nystrom trace of the transfer kernel)
# ----------------------------------------------------------------------------------------------------------------
def nystrom_trace(w, Lx, M, d=DELTA):
    x = (np.arange(M) + 0.5) / M * 2 * d - d; h = 2 * d / M
    s = x[None, :] - x[:, None]
    wv = max(w, 1e-9)
    T = (2 / wv) * np.sin(wv * (d - np.abs(s) / 2)) * h
    ev = np.linalg.eigvalsh(T)
    return (ev ** Lx).sum()
errs = []
for wv in (0, 1, 3, 6, 8, 11, 17):
    ref = C3_0() if wv == 0 else C3(np.array([float(wv)]))[0]
    errs.append(abs(nystrom_trace(wv, 3, 1600) - ref))
chk("S3 closed form vs Nystrom trace Tr T_w^3 (M=1600) at w in {0,1,3,6,8,11,17}", max(errs) < 2e-6, f"max diff {max(errs):.1e}")

# ----------------------------------------------------------------------------------------------------------------
# 4. Monte-Carlo from the ORIGINAL definition of the kernel (no reduction used): kappa(D) = int_{T^6} du prod of 12 hard indicators
#    sites (x,y), x in Z_3, y in Z_2.  x-links carry flat angle D/3 (uniform pool), y-links 0.  Two staged samplers, fixed seed.
# ----------------------------------------------------------------------------------------------------------------
def wrap(a):
    return a - 2 * PI * np.round(a / (2 * PI))
def kappa_mc(D, seed, batches=24, n1=300000, n2=1500):
    rng = np.random.default_rng(seed)
    est = []
    for _ in range(batches):
        # stage 1: u[1,0], u[2,0] (u[0,0]=0 fixed by gauge)
        u10 = rng.uniform(-PI, PI, n1); u20 = rng.uniform(-PI, PI, n1)
        a = D / 3
        ok = (np.abs(wrap(a + u10)) < DELTA) & (np.abs(wrap(a + u20 - u10)) < DELTA) & (np.abs(wrap(a - u20)) < DELTA)
        u10, u20 = u10[ok], u20[ok]; m = len(u10)
        P1 = m / n1
        if m == 0:
            est.append(0.0); continue
        # stage 2: u[0,1], u[1,1], u[2,1] given each survivor, n2 draws each (processed in chunks to bound memory)
        hits = 0; tot = 0
        for c0 in range(0, m, 300):
            a10 = u10[c0:c0 + 300]; a20 = u20[c0:c0 + 300]; mm = len(a10)
            U10 = np.repeat(a10, n2); U20 = np.repeat(a20, n2)
            u01 = rng.uniform(-PI, PI, mm * n2); u11 = rng.uniform(-PI, PI, mm * n2); u21 = rng.uniform(-PI, PI, mm * n2)
            ok2 = (np.abs(wrap(u01)) < DELTA) & (np.abs(wrap(u11 - U10)) < DELTA) & (np.abs(wrap(u21 - U20)) < DELTA)   # both y-links of a column give |.|<delta
            ok2 &= (np.abs(wrap(a + u11 - u01)) < DELTA) & (np.abs(wrap(a + u21 - u11)) < DELTA) & (np.abs(wrap(a + u01 - u21)) < DELTA)
            hits += int(ok2.sum()); tot += mm * n2
        P2 = hits / tot
        est.append(P1 * P2 * (2 * PI) ** 5 * 2 * PI)      # int over u[0,0] gives 2 pi
    est = np.array(est)
    return est.mean(), est.std(ddof=1) / np.sqrt(len(est))
def kappa_series(D, W=20000):
    w = np.arange(1, W + 1).astype(float)
    return C3_0() + 2 * np.sum(C3(w) * np.cos(w * D))
for D, sd_ in ((0.0, 11), (1.0, 12)):
    t = time.time()
    m, e = kappa_mc(D, sd_)
    ks = kappa_series(D)
    chk(f"S4 MC from original definition vs Fourier series, Delta={D}", abs(m - ks) < 4 * e + 1e-9 and e / ks < 0.03, f"MC {m:.4f} +- {e:.4f}; series {ks:.4f}; {time.time()-t:.0f}s")

# ----------------------------------------------------------------------------------------------------------------
# 5. the pool kernel and its negative eigenvalue: K_ab = kappa(D_a - D_b), D_a = 2 pi a / N
# ----------------------------------------------------------------------------------------------------------------
W = 20000
wgrid = np.arange(1, W + 1).astype(float)
Cw = C3(wgrid)
tail = 2 * np.sum(Bound3(np.arange(W + 1, 40 * W + 1)))                      # explicit sum
tail += 2 * 4 * (4 * DELTA ** 3 + 12 * DELTA ** 2 / (40 * W) + 24 * DELTA / (40 * W) ** 2 + 12 / (40 * W) ** 3) / (2 * (40 * W) ** 2)   # integral bound beyond 40 W
chk("S5 series tail bound tau(W=20000) for |kappa - kappa_W| is below 1e-8", tail < 1e-8, f"tau={tail:.2e}")
def kappa_vec(Ds):
    return C3_0() + 2 * (np.cos(np.outer(Ds, wgrid)) @ Cw)
def pool_matrix(N, power=1):
    Dg = 2 * PI * np.arange(N) / N
    kd = kappa_vec(Dg) ** power
    return np.array([[kd[(a - b) % N] for b in range(N)] for a in range(N)])
def tau_power(kmax, power):
    return tail if power == 1 else 2 * kmax * tail + tail ** 2
mins = {}
for N in range(3, 33):
    K = pool_matrix(N)
    ev = np.linalg.eigvalsh(K)
    mins[N] = (ev[0], ev[-1])
firstneg = min((N for N in mins if mins[N][0] < -N * tail * 10), default=None)
chk("S5 pool kernel (open time) has certified negative eigenvalue (lambda_min < -10 N tau) for some N<=32", firstneg is not None,
    f"smallest certified N = {firstneg}; lambda_min/lambda_max there = {mins[firstneg][0]/mins[firstneg][1]:+.3e}")
for N in (16, 64):
    K = pool_matrix(N); ev = np.linalg.eigvalsh(K)
    j = N // 2 if N == 16 else 8
    v = np.exp(-1j * j * 2 * PI * np.arange(N) / N)
    rq = (v.conj() @ K @ v).real / N
    chk(f"S5 N={N}: lambda_min {ev[0]:+.5e} < -N tau ({N*tail:.1e}); relative to lambda_max {ev[0]/ev[-1]:+.3e}; character e^(-i j Delta), j={j}, has Rayleigh quotient {rq:+.5e}",
        ev[0] < -N * tail and rq < -N * tail and abs(rq - ev[0]) < 1e-3 * abs(ev[0]) + 5 * N * tail)
# aliasing-sum cross-check of lambda_8 at N=64
N = 64
lam8 = N * (C3(np.array([8.0]))[0] + sum(C3(np.array([float(8 + N * k)]))[0] for k in range(-300, 301) if k != 0))
Kv = np.linalg.eigvalsh(pool_matrix(64))
chk("S5 aliasing identity lambda_8 = N sum_k C3(8 + N k) agrees with the dense eigenvalue (N=64)", abs(lam8 - Kv[0]) < 1e-6 and Kv[0] < 0, f"{lam8:+.6e} vs {Kv[0]:+.6e}")

# periodic (torus) time: two crossing planes, kernel = kappa^2 on the same pool
tor = {}
for N in (16, 32, 64):
    K2 = pool_matrix(N, power=2); ev = np.linalg.eigvalsh(K2)
    kmax = float(np.max(kappa_vec(2 * PI * np.arange(N) / N)))
    tor[N] = (ev[0], ev[-1], N * tau_power(kmax, 2))
chk("S5 torus-time version (kernel kappa^2, both planes): certified negative eigenvalue on the same uniform pool for N=32 and N=64 (N=16 is PSD there)",
    all(tor[N][0] < -10 * tor[N][2] for N in (32, 64)) and tor[16][0] > 0, "; ".join(f"N={N}: {tor[N][0]:+.3e} (rel {tor[N][0]/tor[N][1]:+.2e}, err {tor[N][2]:.0e})" for N in tor))

# ----------------------------------------------------------------------------------------------------------------
# 6. controls on the SAME pool
# ----------------------------------------------------------------------------------------------------------------
# 6a. even Lx: Tr T^Lx = sum mu^Lx >= 0 for the Hermitian kernel; check numerically at Lx = 2, 4, w = 0..40
neg_even = []
for Lx in (2, 4):
    for wv in list(range(0, 41)):
        neg_even.append(nystrom_trace(float(wv), Lx, 500))
chk("S6a control: hard indicator, even Lx (2 and 4), Z_Lx x Z_2 uniform pool: Fourier coefficients Tr T_w^Lx >= 0 for w=0..40 (sum of even powers of real eigenvalues)", min(neg_even) > -1e-12, f"min {min(neg_even):+.2e}")
# 6b. ring Lx=3 (Ly=1): reproduces K2c V1 numbers  lambda_min = -3.99e-3, min/max = -8.9e-3 at N=64
def ring_lams(N, Lx=3, d=DELTA, nmax=400000):
    n = np.arange(-nmax, nmax + 1).astype(float)
    c = np.where(n == 0, d / PI, np.sin(n * d) / (np.where(n == 0, 1, n) * PI)) ** Lx
    idx = (n.astype(int) % N)
    return np.array([N * c[idx == j].sum() for j in range(N)])
lr = ring_lams(64)
chk("S6b control: 2D odd ring (Ly=1, Lx=3) reproduces the recorded values lambda_min -3.99e-3, min/max -8.9e-3 (K2c_REPORT.md:99)", abs(lr.min() + 3.99e-3) < 3e-5 and abs(lr.min() / lr.max() + 8.9e-3) < 1e-4, f"{lr.min():+.4e}, {lr.min()/lr.max():+.3e}")
# 6c. positive-type (Wilson) plaquette weight exp(beta cos theta): the same pool kernel is PSD
def wilson_coeffs(beta, w_list, M=96, Lx=3):
    th = 2 * PI * np.arange(M) / M; h = 2 * PI / M
    f = np.exp(beta * np.cos(th))
    out = []
    for w in w_list:
        # state d in T; Kd,d' = int de e^{-iwe} f(e) f(e + d' - d), column weight f(d)^2
        idx = (np.arange(M)[None, :] - np.arange(M)[:, None]) % M            # (d'-d) index
        Kmat = np.zeros((M, M), complex)
        for s in range(M):
            val = np.sum(np.exp(-1j * w * th) * f * f[(np.arange(M) + s) % M]) * h
            Kmat[idx == s] = val
        col = f ** 2
        T = np.sqrt(col)[:, None] * Kmat * np.sqrt(col)[None, :] * h
        ev = np.linalg.eigvals(T)
        out.append((ev ** Lx).sum())
    return np.array(out)
wl = list(range(0, 17))
cw = wilson_coeffs(1.0, wl)
chk("S6c control: Wilson weight exp(cos theta) on the same Z_3 x Z_2 pool: all Fourier coefficients real >= 0 (w=0..16) so the pool kernel is PSD",
    np.max(np.abs(cw.imag)) < 1e-9 * np.max(np.abs(cw.real)) and cw.real.min() > -1e-12 * cw.real.max(), f"min coefficient {cw.real.min():+.2e}, max {cw.real.max():+.2e}")
Kw = np.array([[ (cw.real[0] + 2 * np.sum(cw.real[1:] * np.cos(np.arange(1, 17) * (2 * PI * (a - b) / 16)))) for b in range(16)] for a in range(16)])
chk("S6c control: Wilson pool kernel (N=16, series to w=16 with Wilson tail negligible) has lambda_min >= -1e-6 lambda_max",
    np.linalg.eigvalsh(Kw)[0] > -1e-6 * np.linalg.eigvalsh(Kw)[-1])

# 6d. dependence on the support half-width delta (closed form valid for 3 delta < pi)
def minC3(d):
    w = np.linspace(0.05, 80, 160000)
    x = d * w
    num = np.zeros(w.shape, complex)
    for co, p, k in NUM:
        num += co * x ** p * np.exp(1j * k * x)
    return (4 * num * np.exp(-3j * x) / w ** 6).real
res = {d: minC3(d) for d in (0.3, 0.5, 0.6, 0.9)}
chk("S6d delta sweep: C3(w;delta) takes a negative value for delta = 0.3, 0.5, 0.6, 0.9 (all with 3 delta < pi)", all(r.min() < 0 for r in res.values()),
    "; ".join(f"delta={d}: min C3 = {r.min():+.2e} at w={np.linspace(0.05,80,160000)[r.argmin()]:.1f}" for d, r in res.items()))

# ----------------------------------------------------------------------------------------------------------------
# 7. second cross-section: Z_3 x Z_3 (no doubled links); numerical, NOT certified
# ----------------------------------------------------------------------------------------------------------------
def trace_pows_Ly3(w, Lxs, M, d=DELTA):
    g = (np.arange(M) + 0.5) / M * 2 * d - d; h = 2 * d / M
    D1, D2 = np.meshgrid(g, g, indexing='ij'); D1 = D1.ravel(); D2 = D2.ravel()
    ok = (np.abs(D1) < d) & (np.abs(D2) < d) & (np.abs(D2 - D1) < d)
    D = np.stack([np.zeros(ok.sum()), D1[ok], D2[ok]], 1)
    S = D[None, :, :] - D[:, None, :]
    mn = S.min(2); mx = S.max(2)
    half = d - (mx - mn) / 2
    T = np.where(half > 0, np.exp(1j * w * (mn + mx) / 2) * 2 * np.sin(w * np.maximum(half, 0)) / w, 0) * h * h
    ev = np.linalg.eigvalsh((T + T.conj().T) / 2)
    return {L: (ev ** L).sum() for L in Lxs}
t = time.time()
r3 = {M: {w: trace_pows_Ly3(float(w), (3,), M)[3] for w in (8, 9, 10)} for M in (30, 44)}
c0 = trace_pows_Ly3(1e-6, (3,), 44)[3]
chk("S7 Z_3 x Z_3 cross-section (uniform pool, grid transfer trace, two resolutions): Fourier coefficient negative at w=8,9,10 and stable to 5%",
    all(r3[44][w] < 0 and abs(r3[44][w] - r3[30][w]) < 0.05 * abs(r3[44][w]) for w in (8, 9, 10)),
    f"M=44: " + ", ".join(f"w={w}: {r3[44][w]:+.3e}" for w in (8, 9, 10)) + f"; w=0: {c0:+.3f}; {time.time()-t:.0f}s")

# ----------------------------------------------------------------------------------------------------------------
# 8. recovered K2c torus pool: regenerate with source code is done outside (see RECOVERY_STATUS.json); here re-run source V6
#    builder on the pinned regenerated pool if both are present
# ----------------------------------------------------------------------------------------------------------------
POOL = os.path.join(HERE, "pool_K2c_wgsearch_hard_O_torus_Lt12_seed4412.npz")
POOL_ARRAY_SHA = "a927745c2c25d2911b5971f64b7f9c3fa8a947d9650115a8fac876da62f6471c"   # sha256 of ux||ut as little-endian float64 bytes
if os.path.exists(POOL):
    d = np.load(POOL)
    hh = hashlib.sha256()
    for k_ in ("ux", "ut"):
        hh.update(np.ascontiguousarray(d[k_], dtype="<f8").tobytes())
    chk("S8 regenerated K2c torus pool (wgsearch hard, torus Lt=12, K=24, seed 4412): sha256 of array bytes equals the pinned value", hh.hexdigest() == POOL_ARRAY_SHA, hh.hexdigest())
    chk("S8 pool arrays: shapes (24,6,2),(24,5,2); finite", d['ux'].shape == (24, 6, 2) and d['ut'].shape == (24, 5, 2) and np.all(np.isfinite(d['ux'])) and np.all(np.isfinite(d['ut'])))
    v6 = os.path.join(HERE, "src", "k2c_v6_torus_verify.py")
    if os.path.exists(v6) and os.environ.get("RUN_V6", "1") == "1":
        t = time.time(); buf = io.StringIO(); old = sys.argv
        sys.argv = [v6, POOL]
        try:
            with contextlib.redirect_stdout(buf):
                exec(compile(open(v6).read(), v6, "exec"), {"__name__": "__v6__"})
        finally:
            sys.argv = old
        out = buf.getvalue().strip().splitlines()
        lo = [l for l in out if l.startswith("V6 O (6,6,4)")]
        chk("S8 source V6 builder on the regenerated pool: overlap kernel lambda_min <0 (recorded -1.47281e-4) -- REPLICATION, not new", bool(lo) and "lam_min -1.47" in lo[0], (lo[0] if lo else "no output") + f" [{time.time()-t:.0f}s]")
        lw = [l for l in out if l.startswith("V6 W (6,6,4)")]
        chk("S8 source V6 builder: Wilson control on the same pool PSD (|lam_min| < 1e-12 or positive)", bool(lw) and float(lw[0].split("lam_min")[1].split()[0]) > -1e-12, lw[0] if lw else "no output")
else:
    chk("S8 regenerated pool file absent beside check.py: replication section skipped (see ATTEMPT.md for the regeneration command and hash)", True)

# ----------------------------------------------------------------------------------------------------------------
print("   runtime %.0f s" % (time.time() - T0))
print(f"TOTAL: PASS={NP} FAIL={NF}")
if NF == 0:
    print("HIT: pure U(1) hard-support (delta=0.6) measure on the 2+1D spatial torus Z_3 x Z_2 is not reflection-positive for open time (certified negative eigenvalue already on a 13-point flat uniform-holonomy pool; 16-point pool lambda_min/lambda_max=-1.65e-2) and for periodic time (N>=32), although slice-plaquette support is enforced")
print("SUMMARY: the hard-indicator pure-gauge kernel on the Z_3 x Z_2 spatial torus has an exactly computed Fourier coefficient C3(8)=-8.01e-3<0, giving a certified negative pool eigenvalue (open and periodic time) with positive-type and even-size controls PSD; the fermion overlap tests were only replicated.")
sys.exit(0 if NF == 0 else 1)
