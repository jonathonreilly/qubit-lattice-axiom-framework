"""(b) the single node of the step W = D_b; (c) finite range => W3 = 0, numerical tests."""
import time
from scipy.optimize import minimize
from scipy.stats import unitary_group
from c12chk_lib import *
from c11lib import sphere_chern, rand_H

NP = NF = 0
def rep(ok, msg):
    global NP, NF
    NP += bool(ok); NF += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {msg}", flush=True)
rng = np.random.default_rng(7)
t0 = time.time()

# ------------------------------------------------------------------ (b)
for b in (1, -1):
    for m in (2.0, 2.5):
        f = make_Db(b, m=m)
        # fine grid, full 12x12 spectrum
        N = 48; ks = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi   # midpoint grid (does not contain -k*)
        K = np.array(list(itertools.product(ks, ks, ks)))
        d = np.concatenate([np.min(np.abs(np.linalg.eigvals(f(K[s:s + 8192])) + 1), axis=1) for s in range(0, len(K), 8192)])
        kmin = K[np.argmin(d)]
        far = np.linalg.norm(wrapk(K + KST), axis=1) > 0.3
        dfar = d[far].min()
        # minimisation of min |lambda + 1| from 300 random starts
        obj = lambda k: np.min(np.abs(np.linalg.eigvals(f(k)[0]) + 1)) ** 2
        hits = []
        for _ in range(120):
            r = minimize(obj, rng.uniform(-np.pi, np.pi, 3), method='Nelder-Mead', options=dict(xatol=1e-10, fatol=1e-16, maxiter=4000))
            if r.fun < 1e-10: hits.append(np.linalg.norm(wrapk(r.x + KST)))
        allm = max(hits) if hits else np.nan
        # analytic: on the complement eigenvalue 1; on D_b eigenvalues n4 +- i|n_vec|
        U0 = f(-KST)[0]; ev0 = np.sort_complex(np.linalg.eigvals(U0))
        # cone: eigenphases of the 2 eigenvalues nearest -1 at -k* + delta n
        sp = []; tilt = []
        for _ in range(12):
            n = rng.normal(size=3); n /= np.linalg.norm(n)
            for dl in (1e-4,):
                ev = np.linalg.eigvals(f(-KST + dl * n)[0]); ph = np.angle(-ev); idx = np.argsort(np.abs(ph))[:2]; p = np.sort(ph[idx])
                sp.append((p[1] - p[0]) / 2 / dl); tilt.append((p[1] + p[0]) / 2 / dl)
        ch, gap = sphere_chern(lambda k: f(k)[0], -KST, -1.0, [(0,), (1,), (0, 1)], 0.05)
        ok = (dfar > 0.2 and len(hits) > 0 and allm < 1e-4 and np.allclose(np.ptp(sp), 0, atol=1e-6)
              and abs(np.mean(sp) - 1 / (3 - m)) < 1e-5 and np.abs(tilt).max() < 1e-6
              and abs(abs(ch[0]) - 1) < 1e-3 and abs(ch[0] + ch[1]) < 1e-3 and abs(ch[2]) < 1e-3
              and np.sum(np.abs(ev0 - 1) < 1e-12) == 10 and np.sum(np.abs(ev0 + 1) < 1e-12) == 2)
        rep(ok, f"b1 D{'+' if b>0 else '-'}, m={m}: spectrum at -k* = {{1 (x10), -1 (x2)}}; on the 48^3 midpoint grid min|lambda+1| "
            f"outside 0.3-ball = {dfar:.3f}; {len(hits)}/120 Nelder-Mead minimisations reach |lambda+1|<1e-5, all within {allm:.1e} of -k*; "
            f"cone speeds {np.min(sp):.6f}..{np.max(sp):.6f} (1/(3-m) = {1/(3-m):.4f}), tilt <= {np.abs(tilt).max():.1e}; "
            f"FHS Berry charges (lower, upper, pair) = {ch[0]:+.4f}, {ch[1]:+.4f}, {ch[2]:+.4f}")
# Berry-charge sign relative to W3: compare with the inverse letter
chi_ = sphere_chern(lambda k: make_Db(1, inv=True)(k)[0], -KST, -1.0, [(0,), (1,)], 0.05)[0][0]  # first run: single-band selection crashed c11lib gap estimate (checker bug)
ch_ = sphere_chern(lambda k: make_Db(1)(k)[0], -KST, -1.0, [(0,), (1,)], 0.05)[0][0]  # first run: single-band selection crashed c11lib gap estimate (checker bug)
rep(abs(chi_ + ch_) < 1e-3, f"b2 inverse letter (W3 = -1) has the opposite lower-band charge at E = pi: {ch_:+.3f} vs {chi_:+.3f}")
print(f"   ({time.time()-t0:.0f}s)")

# ------------------------------------------------------------------ (c)
def const(M):
    return lambda K: np.broadcast_to(M, (len(np.atleast_2d(K)),) + M.shape)
RL = lambda K: bl_batch(RLX, K); RT = lambda K: bl_batch(RTX, K)
def expH(H, s): return lambda K: expiH_batch(H, K, s)
def onsite_u():
    H = sym_onsite(rng); H = (H + H.conj().T) / 2; H /= np.linalg.norm(H, 2)
    w, V = np.linalg.eigh(H * rng.uniform(0.5, 3)); return (V * np.exp(1j * w)) @ V.conj().T

# c1: strictly finite-range covariant words (S^p, R_L, Rt, A0, constant symmetric on-site unitaries).  Integrand is a trig
#     polynomial, so the midpoint rule is exact once N exceeds its degree: N = 16 and 20 must agree.
vals = []
for t in range(6):
    L = rng.integers(4, 8); fs = []
    for _ in range(L):
        c = rng.integers(0, 5)
        if c == 0: p = int(rng.choice([-2, -1, 1, 2])); fs.append(lambda K, p=p: S_batch(K, p))
        elif c == 1: fs.append(RL)
        elif c == 2: fs.append(RT)
        elif c == 3: fs.append(const(A0))
        else: fs.append(const(onsite_u()))
    f = word(fs)
    a, b2 = W3(f, 12), W3(f, 16); vals.append((L, a, b2))
print("   c1 finite-range covariant words: " + "; ".join(f"len {L}: W3(N=12) {a.real:+.1e}, W3(N=16) {b2.real:+.1e}" for L, a, b2 in vals))
rep(all(abs(a) < 1e-8 and abs(b2) < 1e-8 for _, a, b2 in vals), "c1 W3 = 0 (to 1e-8) for 6 random finite-range covariant words in S^p, R_L, Rt, A0, on-site unitaries")

# c2: words with covariant exp(iH) letters (quasi-local, range-2 H) mixed with the above; W3 -> 0 under refinement
vals = []
for t in range(4):
    fs = []
    for _ in range(4):
        c = rng.integers(0, 3)
        if c == 0: fs.append(expH(rand_H(rng), rng.uniform(0.5, 3)))
        elif c == 1: p = int(rng.choice([-1, 1, 2])); fs.append(lambda K, p=p: S_batch(K, p))
        else: fs.append(RL)
    fs.append(expH(rand_H(rng), rng.uniform(0.5, 3)))
    f = word(fs); vals.append((W3(f, 12), W3(f, 20)))
print("   c2 exp(iH) words: " + "; ".join(f"N=12 {a.real:+.1e}, N=20 {b2.real:+.1e}" for a, b2 in vals))
rep(all(abs(b2) < 1e-4 for _, b2 in vals), "c2 W3 -> 0 for 4 random words with covariant exp(iH) letters, shifts and R_L")
# positive control: same kind of word times D+ gives 1
f = word([expH(rand_H(rng), 1.5), make_Db(1), S_batch, RL]); ctrl = W3(f, 20)
rep(abs(ctrl - 1) < 1e-3, f"c2 control: inserting D+ into such a word gives W3 = {ctrl.real:+.6f}")

# c3: non-covariant random finite-depth circuits on C^n: Haar on-site layers and random partial shifts
def circuit(n, depth):
    fs = []
    for _ in range(depth):
        fs.append(const(unitary_group.rvs(n, random_state=rng)))
        A = rng.integers(-1, 2, (n, 3)).astype(float)
        fs.append(lambda K, A=A: np.einsum('ni,ij->nij', np.exp(-1j * np.atleast_2d(K) @ A.T), np.eye(len(A))))
    return word(fs)
vals = []
for n, dep in ((2, 6), (3, 8), (4, 8), (4, 12)):
    f = circuit(n, dep); vals.append((n, dep, W3(f, 16), W3(f, 28)))
print("   c3 circuits: " + "; ".join(f"n={n} depth={d}: {a.real:+.1e} / {b2.real:+.1e}" for n, d, a, b2 in vals))
rep(all(abs(b2) < 1e-8 for *_, b2 in vals), "c3 W3 = 0 for non-covariant random finite-depth circuits (Haar layers + partial shifts), N=28")

# c4: a finite-range unitary not written as a circuit: U = 1 - P + z P, P = (1 + h.sigma)/2, h a trig-polynomial unit vector
def proj_unitary(hfun, zfun):
    def f(K):
        K = np.atleast_2d(K); h = hfun(K); P = 0.5 * (np.eye(2)[None] + sum(h[:, i, None, None] * PAULI[i][None] for i in range(3)))
        return np.eye(2)[None] - P + zfun(K)[:, None, None] * P
    return f
def hpoly(K):
    kx, ky, kz = K.T; h = np.stack([np.sin(kx), np.cos(kx) * np.sin(ky), np.cos(kx) * np.cos(ky)], 1)
    c, s = np.cos(kz), np.sin(kz)
    return np.stack([c * h[:, 0] - s * h[:, 1], s * h[:, 0] + c * h[:, 1], h[:, 2]], 1)   # rotated about axis 3 by kz
def hdirac(K):
    kx, ky, kz = K.T; h = np.stack([np.sin(kx), np.sin(ky), 1.0 + np.cos(kx) + np.cos(ky)], 1)
    return h / np.linalg.norm(h, axis=1)[:, None]
z = lambda K: np.exp(-1j * np.atleast_2d(K)[:, 2]); z3 = lambda K: np.exp(-1j * np.atleast_2d(K).sum(1))
v1 = W3(proj_unitary(hpoly, z3), 24); v1b = W3(proj_unitary(hpoly, z3), 32)
v2 = W3(proj_unitary(hdirac, z), 32)
rep(abs(v1b) < 1e-8 and abs(abs(v2) - 1) < 1e-3,
    f"c4 finite-range projector-twist U = 1 - P + z P (P trig-polynomial, kz-rotated): W3 = {v1.real:+.1e} (N=24), {v1b.real:+.1e} (N=32); "
    f"control with a Chern-1 quasi-local P: W3 = {v2.real:+.5f}")
# c5: truncating D+ to finite range: Laurent-polynomial GL map (inverse NOT finite range) keeps W3 = 1, consistent with S6 needing the inverse
def trunc_D(r, Nf=32):
    ks = 2 * np.pi * np.arange(Nf) / Nf; KK = np.array(list(itertools.product(ks, ks, ks)))
    F = make_Db(1)(KK).reshape(Nf, Nf, Nf, 12, 12)
    C = np.fft.fftn(F, axes=(0, 1, 2)) / Nf ** 3      # C[a] with F(k) = sum_a C[a] e^{+i k.a}
    X = {}
    for a in itertools.product(range(-r, r + 1), repeat=3):
        if sum(map(abs, a)) <= r: X[tuple(-x for x in a)] = C[a[0] % Nf, a[1] % Nf, a[2] % Nf]   # bl uses e^{-ik.a}
    return lambda K: bl_batch(X, K), X
ft, X = trunc_D(6); Kt = rng.uniform(-np.pi, np.pi, (300, 3))
terr = np.abs(ft(Kt) - make_Db(1)(Kt)).max(); vt = W3(ft, 24)
uerr = np.abs(ft(Kt) @ np.conj(np.swapaxes(ft(Kt), 1, 2)) - np.eye(12)).max()
rep(abs(vt - 1) < 1e-3 and uerr > 1e-6,
    f"c5 Fourier-truncated D+ (l1-range 6, sup error {terr:.1e}, not unitary: {uerr:.1e}) is a Laurent-polynomial GL map with W3 = {vt.real:+.5f}: "
    f"S6 genuinely needs a Laurent-polynomial INVERSE (unitarity supplies it), consistent with S6")
print(f"TOTAL PASS={NP} FAIL={NF} ({time.time()-t0:.0f}s)")
