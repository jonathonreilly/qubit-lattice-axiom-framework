"""K2-T1 (pre-registered in ../PREREG.md): independent rebuild of the free overlap's OS transfer content on Z^4.
Own gammas; D built numerically; C(t;p) by FFT over p4; transfer eigenvalues by block-Hankel GEVP; branch points E1(p) by
numerical root finding of det of the continued X~X; global minimisation of E1 over the BZ."""
import numpy as np, sys
from scipy.optimize import brentq, minimize
np.set_printoptions(precision=4, suppress=False)
s = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.diag([1., -1.]).astype(complex)]
Z2 = np.zeros((2, 2)); I2 = np.eye(2)
g = [np.block([[Z2, -1j * sk], [1j * sk, Z2]]) for sk in s] + [np.block([[Z2, I2], [I2, Z2]])]   # g1,g2,g3,g4
for a in range(4):
    assert np.allclose(g[a], g[a].conj().T)
    for b in range(4): assert np.allclose(g[a] @ g[b] + g[b] @ g[a], 2 * (a == b) * np.eye(4))
g5 = g[0] @ g[1] @ g[2] @ g[3]; assert np.allclose(g5 @ g5, np.eye(4))
N4 = 8192; p4 = 2 * np.pi * np.arange(N4) / N4

def Xmat(p, p4v, M, r=1.0, wilson_mass=None):
    """X = sum i g_mu sin p_mu + r sum (1 - cos p_mu) - M ; arrays over p4v."""
    P = [p[0], p[1], p[2]]
    X = np.zeros((len(p4v), 4, 4), complex)
    for k in range(3): X += 1j * g[k] * np.sin(P[k])
    X += 1j * g[3][None] * np.sin(p4v)[:, None, None]
    sc = r * (sum(1 - np.cos(P[k]) for k in range(3)) + 1 - np.cos(p4v)) - M
    return X + sc[:, None, None] * np.eye(4)[None]

def Dinv_overlap(p, M):
    X = Xmat(p, p4, M)
    XX = np.conj(np.swapaxes(X, 1, 2)) @ X
    w, V = np.linalg.eigh(XX)
    isq = V @ (V.conj().swapaxes(1, 2) / np.sqrt(w)[:, :, None])
    D = np.eye(4)[None] + X @ isq
    return np.linalg.inv(D)

def Dinv_wilson(p, m, r):
    X = Xmat(p, p4, -m, r)        # D_W + m = i g sin + r sum(1-cos) + m
    return np.linalg.inv(X)

def corr(Dinv, tmax):
    # C(t) = (1/N4) sum_p4 e^{i p4 t} Dinv(p4)
    C = np.fft.ifft(Dinv, axis=0)   # ifft: (1/N) sum e^{+2pi i k n/N}
    return C[:tmax + 1]

def hankel(C, Gam, n, shift):
    H = np.zeros((4 * n, 4 * n), complex)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            H[4*(i-1):4*i, 4*(j-1):4*j] = Gam @ C[i + j - 1 + shift]
    return H

def gevp(H0, H1, tol=1e-11):
    H0 = 0.5 * (H0 + H0.conj().T); H1 = 0.5 * (H1 + H1.conj().T)
    w, V = np.linalg.eigh(H0); keep = w > tol * w.max()
    Wm = V[:, keep] / np.sqrt(w[keep])
    lam = np.linalg.eigvalsh(Wm.conj().T @ H1 @ Wm)
    return np.sort(lam)[::-1], keep.sum()

def rel_min(H):
    e = np.linalg.eigvalsh(0.5 * (H + H.conj().T)); return e.min() / np.abs(e).max()

# --- calibrate Gamma on Wilson r=1, m=+0.5
cands = {'+g4': g[3], '-g4': -g[3]}
pc = np.array([0.3, -0.2, 0.5]); Cw = corr(Dinv_wilson(pc, 0.5, 1.0), 20)
ok = {k: rel_min(hankel(Cw, G, 6, 0)) for k, G in cands.items()}
print("calibration (Wilson r=1, m=0.5) H0 min/max:", {k: f"{v:+.2e}" for k, v in ok.items()})
Gam = cands[max(ok, key=ok.get)]; print("Gamma chosen:", max(ok, key=ok.get))
# controls
Cn = corr(Dinv_wilson(pc, 0.5, 0.0), 20)
print(f"control NEG1 naive r=0: H0 min/max {rel_min(hankel(Cn, Gam, 6, 0)):+.2e}, H1 min/max {rel_min(hankel(Cn, Gam, 6, 1)):+.2e}, GEVP lam {gevp(hankel(Cn,Gam,6,0), hankel(Cn,Gam,6,1))[0][:6]}")
lamw, rk = gevp(hankel(Cw, Gam, 6, 0), hankel(Cw, Gam, 6, 1))
print(f"control POS Wilson: rank {rk}, lam {lamw}")
sys.stdout.flush()

def contXX_det(p, p4c, M):
    """det of X~(p4c) X(p4c) with analytic continuation (X~ = -i g.sin + scalar), p4c complex."""
    X = Xmat(p, np.array([p4c]), M)[0]
    Xt = -(X - np.trace(X) / 4 * np.eye(4)) + np.trace(X) / 4 * np.eye(4)   # flip the gamma (odd) part
    return np.linalg.det(Xt @ X).real

def E1_numeric(p, M):
    """branch points: zeros of det(X~X) at p4 = iE (z = e^{-E}) or p4 = pi + iE (z = -e^{-E}); returns (E1_pos, E1_neg)."""
    out = []
    for off in [0.0, np.pi]:
        f = lambda E: contXX_det(p, off + 1j * E, M)
        Es = np.linspace(1e-6, 8, 2000); fs = np.array([f(E) for E in Es])
        idx = np.nonzero(np.sign(fs[:-1]) != np.sign(fs[1:]))[0]
        # det = omega^8 >= 0 touches zero (double root): use min of |omega^2| proxy instead -> scalar part
        out.append(Es)
    return out

def omega2(p, p4c, M):
    X = Xmat(p, np.array([p4c]), M)[0]
    Xt = -(X - np.trace(X) / 4 * np.eye(4)) + np.trace(X) / 4 * np.eye(4)
    return (Xt @ X)[0, 0]       # X~X is scalar for the free kernel (checked below)

def E1(p, M):
    """branch points from the numerically built continued X~X: fit omega^2 as a polynomial in c = cos p4 from 3 samples,
    verify the fit at a 4th complex point, solve omega^2 = 0; c > 1 -> z = e^{-E} (+), c < -1 -> z = -e^{-E} (-)."""
    cs = [0.3, -0.5, 0.9]; vals = [omega2(p, np.arccos(c), M) for c in cs]
    coef = np.polyfit(cs, np.array(vals).real, 2)
    pc = 0.7 + 0.4j; chk = omega2(p, pc, M); pred = np.polyval(coef, np.cos(pc))
    assert abs(chk - pred) < 1e-9 * max(1, abs(chk)), (chk, pred)
    assert abs(coef[0]) < 1e-10          # omega^2 is linear in cos p4 (checked numerically, not assumed)
    res = {'+': np.inf, '-': np.inf}
    if abs(coef[1]) > 1e-14:
        c0 = -coef[2] / coef[1]
        if c0 >= 1: res['+'] = np.arccosh(c0)
        if c0 <= -1: res['-'] = np.arccosh(-c0)
    return res

def pole_direct(p, M):
    """smallest singular value of D(p4 = iE) on the principal branch (omega = +sqrt(omega^2) > 0 for E < E1)."""
    e1 = E1(p, M)['+']
    top = min(e1, 20.0) - 1e-9
    def smin(E):
        X = Xmat(p, np.array([1j * E]), M)[0]; w2 = omega2(p, 1j * E, M).real
        if w2 <= 0: return np.inf
        D = np.eye(4) + X / np.sqrt(w2)
        return np.linalg.svd(D, compute_uv=False).min()
    Es = np.linspace(1e-9, top, 4000); vals = np.array([smin(E) for E in Es])
    i = int(np.argmin(vals))
    from scipy.optimize import minimize_scalar
    a, b = Es[max(i - 1, 0)], Es[min(i + 1, len(Es) - 1)]
    r = minimize_scalar(smin, bounds=(a, b), method='bounded', options={'xatol': 1e-13})
    return (r.x, r.fun) if r.fun < 1e-6 else (None, r.fun)

def pole(p, M):
    """zero of det D at p4 = iE (light pole) or pi + iE (time doubler), principal branch omega = sqrt continued."""
    out = {}
    for off, lab in [(0.0, '+'), (np.pi, '-')]:
        def f(E):
            X = Xmat(p, np.array([off + 1j * E]), M)[0]
            w2 = omega2(p, off + 1j * E, M)
            return w2
        out[lab] = None
    return out

# --- check X~X scalar
pt = np.array([0.4, 1.1, -0.7]); X = Xmat(pt, np.array([0.3 + 0.2j]), 1.0)[0]
Xt = -(X - np.trace(X) / 4 * np.eye(4)) + np.trace(X) / 4 * np.eye(4); XX = Xt @ X
print(f"X~X scalar check: off-scalar norm {np.abs(XX - XX[0,0]*np.eye(4)).max():.1e}")

rng = np.random.default_rng(5)
corners = [np.array(c, float) * np.pi for c in [(0,0,0),(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1),(1,1,1)]]
moms = corners + [rng.uniform(-np.pi, np.pi, 3) for _ in range(40)] + [rng.normal(0, 0.15, 3) for _ in range(10)]
for M in [0.5, 1.0, 1.5, 1.9]:
    print(f"\n=== M = {M} ===")
    nbad = 0; worstH0 = 1; worstH1 = 1; negs = []; maxres = 0; cornerpoles = []; stats = []
    for ip, p in enumerate(moms):
        if ip == 0:
            p = np.array([0.02, 0, 0])   # V4: moved from 1e-3 (FFT aliasing ~ e^{-E N4})
        C = corr(Dinv_overlap(p, M), 20)
        H0 = hankel(C, Gam, 6, 0); H1 = hankel(C, Gam, 6, 1)
        r0, r1 = rel_min(H0), rel_min(H1); worstH0 = min(worstH0, r0); worstH1 = min(worstH1, r1)
        lam, rk = gevp(H0, H1)
        S = np.sqrt(np.sum(np.sin(p) ** 2)); beta = 1 - M + np.sum(1 - np.cos(p))
        e1 = E1(p, M); inOmega = beta < np.sqrt(1 + S ** 2)
        lam_pole = np.exp(-np.arcsinh(S))
        top = lam[0]
        cut_hi = max(np.exp(-e1['+']) if np.isfinite(e1['+']) else 0, 0)
        has_pole = abs(top - lam_pole) < 1e-6 and top > cut_hi + 1e-6
        others = lam[1:] if has_pole else lam
        # spin degeneracy: pole appears twice (Dirac) -> drop all copies equal to lam_pole
        others = lam[np.abs(lam - lam_pole) > 1e-6] if has_pole else lam
        above = others[others > cut_hi + 1e-6]
        neg = lam[lam < -1e-8]
        if neg.size: negs.append((round(beta, 3), neg.min(), -np.exp(-e1['-']) if np.isfinite(e1['-']) else None))
        if ip < 8 and has_pole: cornerpoles.append(ip)
        Ep, smn = pole_direct(p, M)
        direct = Ep is not None
        dE = abs(Ep - np.arcsinh(S)) if direct else np.nan
        gev_err = abs(top - lam_pole) if direct else np.nan
        stats.append((direct, inOmega, dE, gev_err, ip < 8 and ip > 0 and direct))
        ceiling = max(cut_hi, np.exp(-Ep) if direct else 0) + 1e-6
        above = lam[lam > ceiling]
        bad = (direct != inOmega) or (direct and dE > 1e-8) or above.size > 0
        if ip < 8: print(f"  corner {ip}: beta {beta:+.2f}, pole {has_pole}, top lam {top:.6f}, e^-E1(+) {cut_hi:.6f}, E1(+) {e1['+']:.4f}, E1(-) {e1['-']:.4f}, rank {rk}, H0 {r0:+.1e}, H1 {r1:+.1e}")
        if bad: nbad += 1; print(f"  MISMATCH p={p}: inOmega {inOmega} direct pole {direct} dE {dE} above-ceiling {above}")
        if r0 < -1e-9 or (M <= 1 and r1 < -1e-9): print(f"  H-NEG p={np.round(p,4)}: H0 {r0:+.2e} H1 {r1:+.2e} S {S:.3f} beta {beta:+.3f}")
    st = np.array([(a, b, c if c == c else 0, d if d == d else 0, e) for a, b, c, d, e in stats], float)
    print(f"  direct poles: {int(st[:,0].sum())}/{len(st)}; agree with Omega: {int((st[:,0] == st[:,1]).sum())}; max |E_pole - arcsinh S| {st[:,2].max():.1e}; poles at nonzero corners {int(st[:,4].sum())}; GEVP top error max {st[:,3].max():.1e} (diagnostic)")
    print(f"  M={M}: momenta {len(moms)}, mismatches {nbad}, worst H0 min/max {worstH0:+.2e}, worst H1 min/max {worstH1:+.2e}, poles at nonzero corners {[c for c in cornerpoles if c>0]}")
    print(f"  negative-lambda momenta: {len(negs)}; all with beta<0: {all(b < 0 for b, _, _ in negs)}; examples {negs[:3]}")
    sys.stdout.flush()

# --- global minimum of E1 over the BZ (both signs), numeric branch points
print("\n=== global threshold minimum (numeric branch point, grid 24^3 + Nelder-Mead 200 starts) ===")
def E1min_sign(p, M, lab):
    v = E1(np.array(p), M)[lab]; return v if np.isfinite(v) else 50.0
for M in [0.5, 2 - np.sqrt(2), 1.0, 1.5, 1.9]:
    best = {}
    for lab in ['+', '-']:
        grid = np.linspace(-np.pi, np.pi, 24, endpoint=False)
        bv, bp = 99, None
        for a in grid[::2]:
            for b in grid[::2]:
                for c in grid[::2]:
                    v = E1min_sign((a, b, c), M, lab)
                    if v < bv: bv, bp = v, (a, b, c)
        starts = [bp] + [rng.uniform(-np.pi, np.pi, 3) for _ in range(200)]
        for st in starts:
            r = minimize(lambda q: E1min_sign(q, M, lab), st, method='Nelder-Mead', options={'xatol': 1e-8, 'fatol': 1e-10, 'maxiter': 2000})
            if r.fun < bv: bv, bp = r.fun, r.x
        best[lab] = (bv, np.round(np.mod(np.array(bp) + np.pi, 2 * np.pi) - np.pi, 4))
    formula = min(abs(np.log(abs(1 - M))) if M != 1 else np.inf, np.log(3 - M))
    print(f"  M={M:.4f}: E1min(+) {best['+'][0]:.6f} at {best['+'][1]} | E1min(-) {best['-'][0]:.6f} at {best['-'][1]} | X3 corner formula {formula:.6f}")
    sys.stdout.flush()

# --- Hankel rank growth (X3-C (i))
pr = np.array([0.7, -0.4, 1.2])
for M in [1.0]:
    C = corr(Dinv_overlap(pr, M), 40); Cw2 = corr(Dinv_wilson(pr, 0.5, 1.0), 40)
    rks = []; rkw = []
    for n in range(2, 9):
        for CC, lst in [(C, rks), (Cw2, rkw)]:
            H0 = hankel(CC, Gam, n, 0); e = np.linalg.eigvalsh(0.5 * (H0 + H0.conj().T)); lst.append(int((e > 1e-11 * e.max()).sum()))
    print(f"\nHankel numerical rank n=2..8 at p={pr}: overlap {rks}; Wilson r=1 {rkw}")
print("done")
