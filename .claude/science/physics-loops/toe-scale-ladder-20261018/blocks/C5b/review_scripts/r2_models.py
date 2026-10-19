"""r2: Theorem L and the general identity W3 = -sum_nodes chi + sum_sheets Phi, tested against W3 from the
bulk integral on maps with known W3, own code only.
 (a) hedgehog n=2: U = exp(i psi(r) khat.sigma), psi: 0 -> pi, U = -1 outside r = R  (analytic W3 = +1, node chi = -1)
 (b) V_M of C5 (infinite range, O-covariant), M = 2 (W3 = -1) and M = 0 (W3 = +2)
 (c) sheet-plane model U = (1-P) + e^{-i k_z} P, P = QWZ lower band   (level pi is a single plane sheet)
 (d) coupled n=3: exp(-iK(k)) (hedgehog (+) e^{+i}), rank-2 P_< at level 0
"""
import numpy as np
import rlib as R

T = R.Tally()
wrap = lambda K: np.mod(K + np.pi, 2 * np.pi) - np.pi

# ---------------- (a) hedgehog
RAD = 2.4
def psi(r):
    x = np.clip(r / RAD, 0, 1)
    return np.pi * (x + (1 - x) * R.smoothstep(x))

def U_hh(K):
    K = wrap(K)
    r = np.linalg.norm(K, axis=-1)
    p = psi(r)
    with np.errstate(invalid='ignore', divide='ignore'):
        n = np.where(r[..., None] > 1e-14, K / np.maximum(r, 1e-300)[..., None], 0.0)
    return R.su2(np.cos(p), np.sin(p)[..., None] * n)

w = R.w3_grid_fd(U_hh, 64)
print(f'(a) hedgehog: W3 (bulk, N=64) = {w.real:+.6f} {w.imag:+.1e}i')
w2 = R.w3_grid_fd(U_hh, 80)
print(f'(a) hedgehog: W3 (bulk, N=80) = {w2.real:+.6f}')
T.check('(a) hedgehog bulk W3 = +1 (analytic degree)', abs(w - 1) < 1e-3 and abs(w2 - 1) < 1e-3)
chi, v, t, tv, _, _ = R.weyl_data(U_hh, np.array([1e-9, 2e-9, 3e-9]), 0.0)
print(f'    node at 0: chi={chi:+d}, v=diag {np.round(np.diag(v), 4)}, t={np.round(t, 4)}')
T.check('(a) node chi = -1 and W3 = -chi', chi == -1 and round(w.real) == -chi)
ch0, rk = R.chern_surface_faces(U_hh, R.cube_faces(np.zeros(3), 0.5), 0.0, np.pi, 30)
print(f'    level 0 box(0.5) Ch(P_<) = {ch0:+.6f} ranks {rk}')
T.check('(a) Theorem L level 0: W3 = -Ch(P_<|dB)', abs(ch0 + round(w.real)) < 1e-6)
d = 0.45 * RAD
for eps in (np.pi / 2, -np.pi / 2):
    chs, rk = R.chern_surface_faces(U_hh, R.cube_faces(np.zeros(3), d), eps, np.pi, 30)
    # direct sheet flux: band crossing eps, surface oriented by grad E
    if eps > 0:   # band E = +psi crosses; grad E outward; select band with E in (0, pi)
        phi_, eps_ = np.pi, np.pi - 1e-9      # window (-pi, pi) minus lower band: use window (0,pi) via two windows
        c_all, _ = R.chern_surface_faces(U_hh, R.cube_faces(np.zeros(3), d), np.pi - 1e-6, np.pi, 30)   # both bands -> 0
        c_low, _ = R.chern_surface_faces(U_hh, R.cube_faces(np.zeros(3), d), 0.0, np.pi, 30)           # E<0 band
        Phi = c_all - c_low        # Ch of the E>0 band, outward = grad E
    else:         # band E = -psi crosses; grad E inward
        c_low, _ = R.chern_surface_faces(U_hh, R.cube_faces(np.zeros(3), d), 0.0, np.pi, 30)
        Phi = -c_low
    print(f'    level {eps:+.4f}: box Ch(P_<) = {chs:+.6f} (ranks {rk}); direct sheet flux Phi = {Phi:+.6f}')
    T.check(f'(a) level {eps:+.3f} (sheet only): Theorem L W3 = -Ch', abs(chs + round(w.real)) < 1e-6)
    T.check(f'(a) level {eps:+.3f}: identity sign W3 = +Phi_sheet (Phi oriented by grad E)', abs(Phi - round(w.real)) < 1e-6)

# ---------------- (b) V_M
def make_V(M):
    def V(K):
        f = M - np.cos(K).sum(-1)
        g = np.sin(K)
        nrm = np.sqrt(f ** 2 + (g ** 2).sum(-1))
        return R.su2(f / nrm, g / nrm[..., None])
    return V

TRIM = [np.array(p, float) for p in np.ndindex(2, 2, 2)]
TRIM = [np.pi * p for p in TRIM]
for M, wexp in ((2.0, -1), (0.0, 2)):
    V = make_V(M)
    w = R.w3_grid_fd(V, 48, 0, 2 * np.pi)
    print(f'(b) V_{M:g}: W3 (bulk, N=48) = {w.real:+.8f}')
    T.check(f'(b) V_{M:g}: bulk W3 = {wexp:+d}', abs(w - wexp) < 1e-6)
    for eps in (0.0, np.pi):
        s_chi = 0; s_ch = 0; nn = 0; okall = True
        for p in TRIM:
            if abs(np.exp(-1j * eps) - V(p[None])[0][0, 0]) > 1e-9:
                continue
            chi, v, t, tv, _, _ = R.weyl_data(V, p, eps)
            ch, rk = R.chern_surface_faces(V, R.cube_faces(p, 0.4), eps, eps + np.pi, 16)
            okall &= abs(ch - chi) < 1e-6
            s_chi += chi; s_ch += ch; nn += 1
        print(f'    level {eps:.4f}: {nn} nodes, sum chi = {s_chi:+d}, sum box Ch = {s_ch:+.6f}')
        T.check(f'(b) V_{M:g} level {eps:.3f}: per-box Ch = chi and W3 = -sum chi = -sum Ch', okall and s_chi == -wexp)

# ---------------- (c) sheet-plane model
mq = 1.0
def Pqwz(K):
    d = np.stack([np.sin(K[..., 0]), np.sin(K[..., 1]), mq + np.cos(K[..., 0]) + np.cos(K[..., 1])], -1)
    n = d / np.linalg.norm(d, axis=-1)[..., None]
    return (np.eye(2) - (n[..., 0, None, None] * R.SX + n[..., 1, None, None] * R.SY + n[..., 2, None, None] * R.SZ)) / 2

def U_pl(K):
    P = Pqwz(K)
    return np.eye(2) - P + np.exp(-1j * K[..., 2])[..., None, None] * P

w = R.w3_grid_fd(U_pl, 48, 0, 2 * np.pi)
print(f'(c) plane model: W3 (bulk, N=48) = {w.real:+.8f}')
T.check('(c) plane model bulk W3 is a nonzero integer', abs(w - round(w.real)) < 1e-6 and round(w.real) != 0)
# Ch(P) on the torus with orientation (x,y): use a unitary whose window picks P: exp(-i 0.5 h.sigma) lower band
def U_qwz(K):
    d = np.stack([np.sin(K[..., 0]), np.sin(K[..., 1]), mq + np.cos(K[..., 0]) + np.cos(K[..., 1])], -1)
    n = d / np.linalg.norm(d, axis=-1)[..., None]
    return R.su2(np.cos(0.5) * np.ones(len(K)), -np.sin(0.5) * n)   # exp(-0.5 i n.sigma)
face = [(np.array([0, 0, 0.0]), np.array([2 * np.pi, 0, 0]), np.array([0, 2 * np.pi, 0]))]
chP, _ = R.chern_surface_faces(U_qwz, face, 0.0, np.pi, 60)
print(f'    Ch(P_qwz) on T^2, orientation (kx,ky) = {chP:+.6f}')
T.check('(c) level pi: plane sheet, grad E = +z, identity W3 = +Phi = Ch(P,(x,y))', abs(chP - round(w.real)) < 1e-6)
zc = np.pi
top = [(np.array([0, 0, zc + 0.5]), np.array([2 * np.pi, 0, 0]), np.array([0, 2 * np.pi, 0]))]
bot = [(np.array([0, 0, zc - 0.5]), np.array([0, 2 * np.pi, 0]), np.array([2 * np.pi, 0, 0]))]
chB, rk = R.chern_surface_faces(U_pl, top + bot, np.pi, 5.0, 60)
print(f'    Theorem L on the slab box T^2 x [pi-0.5, pi+0.5], phi = 5.0: Ch(P_<|dB) = {chB:+.6f} ranks {rk}')
T.check('(c) Theorem L on a slab (non-ball box): W3 = -Ch(P_<|dB)', abs(chB + round(w.real)) < 1e-6)

# ---------------- (d) coupled n = 3
L3 = []
rng = np.random.default_rng(7)
for _ in range(3):
    X = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)); L3.append((X + X.conj().T) / 2)
def U3(K):
    Kh = (0.12 * (np.cos(K[..., 0])[..., None, None] * L3[0] + np.sin(K[..., 1] + K[..., 2])[..., None, None] * L3[1]
                  + np.cos(K[..., 2] - 0.3)[..., None, None] * L3[2]))
    wv, Vv = np.linalg.eigh(Kh)
    E = Vv @ (np.exp(-1j * wv)[..., None] * np.conj(np.swapaxes(Vv, -1, -2)))
    B = np.zeros(K.shape[:-1] + (3, 3), complex)
    B[..., :2, :2] = U_hh(K); B[..., 2, 2] = np.exp(1j * 1.0)
    return E @ B
w = R.w3_grid_fd(U3, 64)
print(f'(d) coupled n=3: W3 (bulk, N=64) = {w.real:+.6f}')
T.check('(d) coupled n=3 bulk W3 = +1 (PW: W3[exp(-iK)] = 0)', abs(w - 1) < 2e-3)
from scipy.optimize import minimize
def deg_gap(k):
    lam = np.linalg.eigvals(U3(k[None])[0])
    i, j = np.argsort(np.abs(lam - 1))[:2]
    return abs(lam[i] - lam[j])
best = None
for x0 in np.random.default_rng(1).uniform(-0.3, 0.3, (6, 3)):
    res = minimize(deg_gap, x0, method='Nelder-Mead', options=dict(xatol=1e-13, fatol=1e-15, maxiter=40000))
    if best is None or res.fun < best.fun: best = res
p = best.x
lam = np.linalg.eigvals(U3(p[None])[0]); i = np.argmin(np.abs(lam - 1)); Enode = -np.angle(lam[i])
print(f'    Weyl node (two-fold degeneracy) at {np.round(p, 5)} (|lam_a - lam_b| = {best.fun:.1e}), quasienergy {Enode:+.5f}'
      f' -> level 0 holds a pocket around it, not the node')
chi, v, t, tv, _, _ = R.weyl_data(U3, p, Enode)
# sampled level-set check (not a certificate): spectrum distance to 1 on a 40^3 grid outside the box
g = (np.arange(40) + 0.5) * 2 * np.pi / 40 - np.pi
K = np.stack(np.meshgrid(g, g, g, indexing='ij'), -1).reshape(-1, 3)
out = np.abs(wrap(K - p)).max(-1) > 0.5
sd = np.abs(np.linalg.eigvals(U3(K[out])) - 1).min(-1)
ch, rk = R.chern_surface_faces(U3, R.cube_faces(p, 0.5), 0.0, np.pi, 30)
Eb = R.frames(U3(K[~out]), 0.0, np.pi)[1]
print(f'    chi={chi:+d}, |v^-1 t|={tv:.3f}; min dist(spec,1) outside box (sampled) = {sd.min():.3f}; '
      f'box Ch(P_<) = {ch:+.6f}, ranks {rk}; e^-i pi absent in box (sampled): {np.abs(np.abs(Eb) - np.pi).min():.3f}')
T.check('(d) coupled n=3: rank-2 P_< box Ch = chi = -W3', abs(ch - chi) < 1e-6 and chi == -round(w.real) and rk == {2} and sd.min() > 0.05)
T.total()
