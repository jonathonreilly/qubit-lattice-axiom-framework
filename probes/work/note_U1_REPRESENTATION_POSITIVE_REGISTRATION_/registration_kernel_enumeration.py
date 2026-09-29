"""Independent checks of the U(1) representation-positive registration-kernel note, with own code.

(1) Exact enumeration of every sharp Lueders registration (set partitions of a mode set) on 3..8 modes, plus random
    positive non-sharp channels with exact rational amplitudes, against the note's claims: a_q >= 0, a_0 = 1,
    two outcomes on three modes always overlap, kappa > 0 iff nonconstant, sharp 3-mode kernels and 2/5, 8/5.
    kappa is derived two ways: the Fourier formula and a Kraus-level variance formula that never forms a_q.
(2) The Fourier theorem on random nonnegative-coefficient families, with kappa from 60-digit finite differences.
(3) Exact negative-log forces on a 4D torus at N = 8..32 against the continuum Maxwell operator: convergence order.
(4) The orientation-completed plaquette Hessian on real-space 4D tori (L = 4, 5, 6), gauge null counts, momentum-space
    ranks up to L = 8, temporal-only and anisotropic controls, infrared cone.
"""
import sys, itertools, random, math, time
from fractions import Fraction as Fr
import numpy as np

PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")

# ------------------------------------------------------------------ (1) registration channels
def set_partitions(lst):
    if not lst:
        yield []; return
    first, rest = lst[0], lst[1:]
    for p in set_partitions(rest):
        for i in range(len(p)):
            yield p[:i] + [[first] + p[i]] + p[i + 1:]
        yield [[first]] + p

def fourier_from_amplitudes(modes, S):
    """S[j][n] amplitude of outcome j on mode n (exact).  Returns dict q -> a_q for q >= 0 with T = a_0 + 2 sum a_q cos(q th)."""
    m = len(modes); a = {}
    for q in range(0, max(modes) - min(modes) + 1):
        tot = Fr(0)
        for row in S:
            for n in modes:
                if n + q in row: tot += row[n] * row[n + q]
        a[q] = tot / m
    return a

def kappa_fourier(a):
    T0 = a[0] + 2 * sum(v for q, v in a.items() if q >= 1)
    return 2 * sum(q * q * v for q, v in a.items() if q >= 1) / T0, T0

def kappa_kraus(modes, S):
    """kappa = -T''(0)/T(0) straight from the Kraus amplitudes: T'' = (1/M) sum_j 2[(sum n s)^2 - (sum s)(sum n^2 s)]."""
    m = len(modes); T0 = Fr(0); T2 = Fr(0)
    for row in S:
        s0 = sum(row[n] for n in modes); s1 = sum(n * row[n] for n in modes); s2 = sum(n * n * row[n] for n in modes)
        T0 += s0 * s0; T2 += 2 * (s1 * s1 - s0 * s2)
    return -T2 / T0, T0 / m

t0 = time.time(); n_sharp = 0; bad_neg = bad_kappa = bad_norm = bad_nonconst = bad_pigeon = 0
kappas_3 = {}
for msize in range(3, 9):
    for modes in itertools.combinations(range(-4, 5), msize):
        for part in set_partitions(list(modes)):
            S = []
            for block in part:
                S.append({n: Fr(1) if n in block else Fr(0) for n in modes})
            a = fourier_from_amplitudes(modes, S)
            k1, T0 = kappa_fourier(a); k2, T0b = kappa_kraus(modes, S)
            n_sharp += 1
            if a[0] != 1: bad_norm += 1
            if any(v < 0 for v in a.values()): bad_neg += 1
            if k1 != k2 or T0 != T0b: bad_kappa += 1
            nonconst = any(v > 0 for q, v in a.items() if q >= 1)
            overlap = any(len(b) >= 2 for b in part)
            if nonconst != overlap or (k1 > 0) != nonconst: bad_nonconst += 1
            if len(part) < msize and not overlap: bad_pigeon += 1
            if len(part) == 2 and msize == 3 and modes == (-1, 0, 1):
                kappas_3.setdefault((tuple(sorted(tuple(b) for b in part)),), (k1, {q: str(v) for q, v in a.items() if q >= 1}))
print(f"sharp channels enumerated exactly: {n_sharp} ({time.time()-t0:.0f}s)")
check("every sharp channel on 3..8 modes has a_0 = 1 (trace preservation)", bad_norm == 0)
check("every sharp channel has all a_q >= 0", bad_neg == 0)
check("Fourier kappa equals the Kraus-level variance kappa, exactly, for every sharp channel", bad_kappa == 0)
check("kappa > 0 exactly when some outcome overlaps two modes; two-block channels on >= 3 modes always overlap", bad_nonconst == 0 and bad_pigeon == 0)
print("three-mode two-outcome sharp channels (kappa, nonzero a_q):", kappas_3)
vals = sorted({v[0] for v in kappas_3.values()})
check("three-mode sharp two-outcome partitions give exactly kappa in {2/5, 8/5}", vals == [Fr(2, 5), Fr(8, 5)])
nz3 = sorted(str({q: x for q, x in v[1].items() if x != '0'}) for v in kappas_3.values())
check("their kernels are 1+(2/3)cos(theta) (a_1 = 1/3, twice by reflection) and 1+(2/3)cos(2 theta) (a_2 = 1/3)", nz3 == sorted(["{1: '1/3'}", "{1: '1/3'}", "{2: '1/3'}"]), str(nz3))
# the third (fully resolved) case is constant
S = [{n: Fr(1) if n == m_ else Fr(0) for n in (-1, 0, 1)} for m_ in (-1, 0, 1)]
a = fourier_from_amplitudes((-1, 0, 1), S)
check("full resolution of the three modes gives the constant kernel, kappa = 0", all(v == 0 for q, v in a.items() if q >= 1) and kappa_fourier(a)[0] == 0)

# random positive channels with exact rational amplitudes
random.seed(20260929)
def rational_unit_vector(J):
    while True:
        q = random.choice([6, 10, 12, 15])
        p = [random.randint(0, q) for _ in range(J - 1)]
        if sum(x * x for x in p) <= q * q:
            u = [Fr(x, q) for x in p]; r2 = sum(x * x for x in u)
            return [2 * x / (1 + r2) for x in u] + [(1 - r2) / (1 + r2)]
bad = badk = badn = badnc = 0; nrand = 0
for trial in range(600):
    msize = random.randint(3, 6); modes = sorted(random.sample(range(-5, 6), msize)); J = random.randint(2, 4)
    cols = [rational_unit_vector(J) for _ in modes]          # cols[n][j] = amplitude of outcome j on mode n, sum_j amp^2 = 1
    assert all(sum(x * x for x in c) == 1 for c in cols)
    S = [{n: cols[i][j] for i, n in enumerate(modes)} for j in range(J)]
    a = fourier_from_amplitudes(modes, S)
    k1, T0 = kappa_fourier(a); k2, T0b = kappa_kraus(modes, S)
    nrand += 1
    if a[0] != 1: badn += 1
    if any(v < 0 for v in a.values()): bad += 1
    if k1 != k2 or T0 != T0b: badk += 1
    if J < msize and not (k1 > 0): badnc += 1                # fewer outcomes than modes forces overlap
    if k1 > 0 and not any(v > 0 for q, v in a.items() if q >= 1): badnc += 1
check(f"{nrand} random positive channels with exact rational Kraus amplitudes: a_0 = 1 and every a_q >= 0", bad == 0 and badn == 0)
check("the same channels: Fourier kappa = Kraus-variance kappa exactly, and J < number of modes forces kappa > 0", badk == 0 and badnc == 0)

# a two-outcome channel that could have zero second moment would need every outcome supported on <= 1 mode: none exists on three modes
found = 0
for supports in itertools.product([frozenset(s) for r in range(0, 4) for s in itertools.combinations((-1, 0, 1), r)], repeat=2):
    if len(supports[0]) <= 1 and len(supports[1]) <= 1 and supports[0] | supports[1] == {-1, 0, 1}: found += 1
check("no pair of outcome supports of size <= 1 covers the three modes (the note's counting step)", found == 0)

# ------------------------------------------------------------------ (2) Fourier theorem numerically
import mpmath as mp
mp.mp.dps = 60
random.seed(7); badk = badmax = badneg = 0; ntest = 0
for trial in range(60):
    nh = random.randint(1, 12)
    a = {n: (Fr(random.randint(0, 9), random.randint(1, 30)) if random.random() < 0.6 else Fr(0)) for n in range(1, nh + 1)}
    if all(v == 0 for v in a.values()): a[random.randint(1, nh)] = Fr(1, 7)
    K0 = 1 + 2 * sum(a.values())
    kap = 2 * sum(n * n * v for n, v in a.items()) / K0
    Kf = lambda th: 1 + 2 * sum(mp.mpf(v.numerator) / v.denominator * mp.cos(n * th) for n, v in a.items())
    V = lambda th: -mp.log(Kf(th) / Kf(0))
    h = mp.mpf(10) ** -6
    d2 = (-V(2 * h) + 16 * V(h) - 30 * V(0) + 16 * V(-h) - V(-2 * h)) / (12 * h * h)
    d3 = (V(2 * h) - 2 * V(h) + 2 * V(-h) - V(-2 * h)) / (2 * h ** 3)
    ntest += 1
    if abs(d2 - mp.mpf(kap.numerator) / kap.denominator) > mp.mpf(10) ** -18 or abs(d3) > mp.mpf(10) ** -12: badk += 1
    grid = np.linspace(-math.pi, math.pi, 2001)
    Kg = 1 + 2 * sum(float(v) * np.cos(n * grid) for n, v in a.items())
    if Kg.max() > float(K0) + 1e-12 or abs(Kg[1000] - float(K0)) > 1e-12: badmax += 1
    if not kap > 0: badneg += 1
check(f"{ntest} random nonnegative-coefficient kernels (up to 12 harmonics): V''(0) from 60-digit differences equals the closed form, V'''(0)=0", badk == 0)
check("the identity is the global maximum of each kernel on a 2001-point grid, and V''(0) > 0", badmax == 0 and badneg == 0)
# negative-character control
a1 = Fr(-1, 5); K = lambda th: 1 + 2 * float(a1) * math.cos(th)
check("negative-coefficient control: 1 + 2 a cos(theta) with a = -1/5 has V''(0) = 2a/(1+2a) < 0 and its identity is not a maximum", 2 * a1 / (1 + 2 * a1) < 0 and K(math.pi) > K(0))

# ------------------------------------------------------------------ (3) forces converge to the Maxwell operator
def make_field(seed):
    rng = np.random.default_rng(seed)
    modes = []
    for mu in range(4):
        for _ in range(3):
            m = rng.integers(-2, 3, size=4); c = rng.normal() * 0.6; ph = rng.uniform(0, 2 * math.pi)
            modes.append((mu, m, c, ph))
    return modes
def A_fn(modes, y):          # y list of 4 arrays (positions in [0,1) units)
    out = [np.zeros_like(y[0]) for _ in range(4)]
    for mu, m, c, ph in modes:
        arg = 2 * math.pi * sum(int(m[i]) * y[i] for i in range(4)) + ph
        out[mu] += c * np.sin(arg)
    return out
def maxwell_fn(modes, y):    # M_mu = sum_nu d_nu F_{mu nu} = sum_nu (d_nu d_mu A_nu - d_nu d_nu A_mu)
    out = [np.zeros_like(y[0]) for _ in range(4)]
    for mu_a, m, c, ph in modes:
        arg = 2 * math.pi * sum(int(m[i]) * y[i] for i in range(4)) + ph
        s = -c * np.sin(arg) * (2 * math.pi) ** 2                # second derivative factor  d_i d_j -> -(2pi)^2 m_i m_j sin
        for mu in range(4):
            for nu in range(4):
                # A_{mu_a} contributes to M_mu through  d_nu d_mu A_nu (needs nu==mu_a)  and  -d_nu d_nu A_mu (needs mu==mu_a)
                if nu == mu_a and nu != mu: out[mu] += s * int(m[nu]) * int(m[mu])
                if mu == mu_a and nu != mu: out[mu] -= s * int(m[nu]) * int(m[nu])
    return out
def forces(theta, Vp, N):
    g = [np.zeros((N,) * 4) for _ in range(4)]
    def P(mu, nu):
        return theta[mu] + np.roll(theta[nu], -1, axis=mu) - np.roll(theta[mu], -1, axis=nu) - theta[nu]
    for mu in range(4):
        for nu in range(4):
            if nu == mu: continue
            Vp_p = Vp(P(mu, nu))
            g[mu] += Vp_p - np.roll(Vp_p, 1, axis=nu)
    return g
kernels = {"1+(2/3)cos(th) [kappa 2/5]": ([Fr(1, 3)], {1: Fr(1, 3)}), "1+(2/3)cos(2th) [kappa 8/5]": (None, {2: Fr(1, 3)}), "three harmonics (1/5,1/10,1/20)": (None, {1: Fr(1, 5), 2: Fr(1, 10), 3: Fr(1, 20)})}
modes_f = make_field(31)
for name, (_, a) in kernels.items():
    K0 = 1 + 2 * sum(a.values()); kap = float(2 * sum(n * n * v for n, v in a.items()) / K0)
    Vp = lambda th, a=a, K0=K0: -(-2 * sum(float(v) * n * np.sin(n * th) for n, v in a.items())) / (float(K0) if False else 1) / (1 + 2 * sum(float(v) * np.cos(n * th) for n, v in a.items()))
    errs = []
    for N in (8, 16, 32):
        ax = np.arange(N) / N
        y = np.meshgrid(ax, ax, ax, ax, indexing='ij'); aa = 1.0 / N
        theta = []
        for mu in range(4):
            yy = [y[i] + (0.5 * aa if i == mu else 0.0) for i in range(4)]
            theta.append(aa * A_fn(modes_f, yy)[mu])
        g = forces(theta, Vp, N)
        yy_c = [[y[i] + (0.5 * aa if i == mu else 0.0) for i in range(4)] for mu in range(4)]
        M = [maxwell_fn(modes_f, yy_c[mu])[mu] for mu in range(4)]
        num = max(np.abs(g[mu] / (kap * aa ** 3) - M[mu]).max() for mu in range(4)); den = max(np.abs(M[mu]).max() for mu in range(4))
        errs.append(num / den)
    orders = [math.log2(errs[i] / errs[i + 1]) for i in range(2)]
    print(f"   {name}: relative force error at N=8,16,32: {[f'{e:.2e}' for e in errs]}, observed orders {[round(o, 2) for o in orders]}")
    check(f"exact negative-log force / (kappa a^3) converges to the Maxwell operator sum_nu d_nu F_mu nu at order 2 for {name}", errs[-1] < 1.5e-2 and errs[0] > errs[1] > errs[2] and all(1.8 < o < 2.3 for o in orders))

# ------------------------------------------------------------------ (4) orientation-completed Hessian
def plaquette_hessian(L, kt, ks):
    n = L ** 4; idx = lambda x, mu: (((x[0] * L + x[1]) * L + x[2]) * L + x[3]) * 4 + mu
    Hm = np.zeros((4 * n, 4 * n))
    for x in itertools.product(range(L), repeat=4):
        for mu in range(4):
            for nu in range(mu + 1, 4):
                xm = list(x); xm[mu] = (xm[mu] + 1) % L; xn = list(x); xn[nu] = (xn[nu] + 1) % L
                v = {}
                for lk, sg in ((idx(x, mu), 1), (idx(tuple(xm), nu), 1), (idx(tuple(xn), mu), -1), (idx(x, nu), -1)):
                    v[lk] = v.get(lk, 0) + sg
                w = kt if mu == 0 else ks
                ks_ = list(v.keys())
                for p in ks_:
                    for q in ks_: Hm[p, q] += w * v[p] * v[q]
    return Hm
def symbol(k, kt, ks):
    q = np.exp(1j * np.asarray(k)) - 1
    H = np.zeros((4, 4), dtype=complex)
    for mu in range(4):
        for nu in range(mu + 1, 4):
            w = kt if mu == 0 else ks
            # F_{mu nu} = q_mu A_nu - q_nu A_mu
            v = np.zeros(4, dtype=complex); v[nu] = q[mu]; v[mu] = -q[nu]
            H += w * np.outer(v.conj(), v)
    return H
for L in (4, 5, 6):
    t0 = time.time()
    for label, kt, ks in (("isotropic", 1.0, 1.0),):
        Hm = plaquette_hessian(L, kt, ks)
        ev = np.linalg.eigvalsh(Hm)
        nz = int((ev > 1e-9).sum()); null = len(ev) - nz
        check(f"L={L} real-space Hessian (dimension {4 * L ** 4}): kernel dimension is L^4 + 3 (pure gauge plus four constant modes) and rank 3(L^4 - 1)", null == L ** 4 + 3 and nz == 3 * (L ** 4 - 1), f"rank {nz}, kernel {null} ({time.time()-t0:.0f}s)")
        # eigenvalues equal the union over momenta of the symbol eigenvalues
        sy = []
        for k in itertools.product(range(L), repeat=4):
            sy.extend(np.linalg.eigvalsh(symbol([2 * math.pi * m / L for m in k], kt, ks)).tolist())
        check(f"L={L}: real-space spectrum equals the union of the 4x4 momentum blocks", np.abs(np.sort(ev) - np.sort(np.array(sy))).max() < 1e-9)
        if L == 4:
            Ht = plaquette_hessian(L, 1.0, 0.0)
            evt = np.linalg.eigvalsh(Ht)
            print("   L=4 temporal-only (kappa_s = 0): rank", int((evt > 1e-9).sum()))

def rank_at(k, kt, ks, sub=None):
    Hs = symbol(k, kt, ks)
    if sub is not None: Hs = Hs[np.ix_(sub, sub)]
    return int((np.linalg.eigvalsh(Hs) > 1e-10).sum())
for L in (4, 6, 8):
    ok_iso_all = ok_iso_sp = ok_t_sp = ok_t_spblock = ok_iso_spblock = ok_null = True; nk = 0
    for k in itertools.product(range(L), repeat=4):
        if not any(k): continue
        kk = [2 * math.pi * m / L for m in k]
        nk += 1
        Hs = symbol(kk, 1.0, 1.0); q = np.exp(1j * np.asarray(kk)) - 1
        ok_null &= np.linalg.norm(Hs @ q) < 1e-12                   # gauge null vector is the 4-vector q
        ok_iso_all &= rank_at(kk, 1.0, 1.0) == 3
        if k[0] == 0:            # purely spatial momentum
            ok_iso_sp &= rank_at(kk, 1.0, 1.0) == 3
            ok_iso_spblock &= rank_at(kk, 1.0, 1.0, [1, 2, 3]) == 2
            ok_t_sp &= rank_at(kk, 1.0, 0.0) == 1
            ok_t_spblock &= rank_at(kk, 1.0, 0.0, [1, 2, 3]) == 0
    check(f"L={L} ({nk} nonzero momenta): the isotropic Hessian has the gauge null q and rank exactly 3 at every one", ok_null and ok_iso_all)
    check(f"L={L}: at purely spatial momenta the isotropic Hessian has rank 3 and its spatial A_i block rank 2 (two transverse polarizations)", ok_iso_sp and ok_iso_spblock)
    check(f"L={L}: at purely spatial momenta the temporal-only Hessian has rank 1 and an empty spatial block (no magnetic restoring direction)", ok_t_sp and ok_t_spblock)
# temporal-only away from q_0 = 0
L = 6; r3 = 0; r_other = 0
for k in itertools.product(range(L), repeat=4):
    if k[0] == 0: continue
    kk = [2 * math.pi * m / L for m in k]
    rk = rank_at(kk, 1.0, 0.0)
    r3 += (rk == 3); r_other += (rk != 3)
check("temporal-only Hessian has rank 3 at every momentum with nonzero temporal component (it is a pure electric block, not zero), rank 1 on the purely spatial ones", r_other == 0 and r3 > 0)

# infrared cone: real-time root of the transverse symbol kappa_t |q_0|^2 + kappa_s sum |q_i|^2 with k_0 = i omega
def omega_root(kvec, kt, ks):
    s2 = sum(math.sin(x / 2) ** 2 for x in kvec)
    return 2 * math.asinh(math.sqrt(ks / kt * s2))
rows = []; cone_ok = True
for ratio in (Fr(1, 4), Fr(1), Fr(4), Fr(9)):
    errs = []
    for L in (16, 64, 256):
        kvec = [2 * math.pi / L, 0, 0]
        w = omega_root(kvec, 1.0, float(ratio)); speed = w / (2 * math.pi / L)
        errs.append(abs(speed - math.sqrt(float(ratio))) / math.sqrt(float(ratio))); rows.append((str(ratio), L, round(speed, 6)))
    # relative error falls like k^2: factor 16 per factor 4 in L
    cone_ok &= errs[2] < 5e-4 and 12 < errs[0] / errs[1] < 20 and 12 < errs[1] / errs[2] < 20
print("   cone speeds (kappa_s/kappa_t, L, omega/|k|):", rows)
check("the infrared cone speed is sqrt(kappa_s/kappa_t) with relative error falling as k^2 (from the analytically continued transverse symbol)", cone_ok)

if FAIL == 0:
    print(f"SUMMARY: no falsifier fires: all {n_sharp} sharp registrations on 3..8 modes and 600 random exact positive channels give a_q >= 0, kappa > 0 iff nonconstant, and the 3-mode sharp kernels 2/5 and 8/5; exact negative-log forces converge at order 2 to the Maxwell operator for three kernels; the real-space Hessian on 4D tori L = 4, 5, 6 has kernel L^4 + 3, two transverse polarizations at spatial momenta up to L = 8, temporal-only rank 1 there, cone sqrt(kappa_s/kappa_t); {PASS} checks pass")
else:
    print(f"SUMMARY: {FAIL} of my own checks failed; see the [FAIL] lines above")
sys.exit(0)
