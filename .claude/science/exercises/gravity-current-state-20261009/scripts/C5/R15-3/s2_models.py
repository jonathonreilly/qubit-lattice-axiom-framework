"""R15-3 s2: explicit local PSD Gaussians with auxiliary irreps.
M1 (axis-only near miss): six h pairs gapped + two A2 pseudo-scalar pairs coupled to h by O(k) (T2 route) and O(k^2) (E route).
M2 (character-sharp 4-branch model): soft content G = 2A2 + 2T2 (A2 aux + the T2 part of h); A1 and E parts of h gapped.
For each: PSD check over the zone, gapless-branch count and slopes along several directions,
stabilizer characters of the gapless positive-frequency eigenspace, and h-TT content of each gapless branch."""
import numpy as np, sys
from common import *

G = proper_cubic_group(); irr = irreps(G)
idx = lambda R: [i for i, S in enumerate(G) if np.allclose(S, R)][0]
C4 = stabilizer_element(G, [0, 0, 1], 4); C3 = stabilizer_element(G, [1, 1, 1], 3); C2p = stabilizer_element(G, [1, 1, 0], 2)
s2 = 1 / np.sqrt(2)
# h coordinates in SYM2 orthonormal basis: 0..2 = h_xx,h_yy,h_zz ; 3 = sqrt2 h_yz ; 4 = sqrt2 h_zx ; 5 = sqrt2 h_xy
eps1 = np.array([-1, -1, 2, 0, 0, 0]) / np.sqrt(6)   # E component 1 (2zz-xx-yy)
eps2 = np.array([1, -1, 0, 0, 0, 0]) / np.sqrt(2)    # E component 2 (xx-yy)
trv = np.array([1, 1, 1, 0, 0, 0]) / np.sqrt(3)

def symbol(k, model, prm):
    kx, ky, kz = k
    sx, sy, sz = np.sin(k)
    L = 2 * (1 - np.cos(k))                  # second-difference symbol (>=0)
    if model == "M1":
        nq = 8                                # 6 h + a1 + a2
        V = np.zeros((nq, nq), complex)
        V[:6, :6] = prm['m2'] * np.eye(6)
        V[6, 6] = prm['c1'] * L.sum(); V[7, 7] = prm['c2'] * L.sum()
        # a1 couples to (D_x h_yz + D_y h_zx + D_z h_xy) ; h_yz = h3/sqrt2 etc.
        b1 = np.zeros(6, complex); b1[3] = 1j * sx * s2; b1[4] = 1j * sy * s2; b1[5] = 1j * sz * s2
        # a2 couples to e1(L) eps2(h) - e2(L) eps1(h), with e(L) the E-part of the second-difference symbol (-L ~ -k^2)
        e1 = (2 * L[2] - L[0] - L[1]) / np.sqrt(6); e2 = (L[0] - L[1]) / np.sqrt(2)
        b2 = -(e1 * eps2 - e2 * eps1)
        V[6, :6] = prm['g1'] * b1.conj(); V[:6, 6] = prm['g1'] * b1
        V[7, :6] = prm['g2'] * b2; V[:6, 7] = prm['g2'] * b2
        K = np.eye(nq)
    elif model == "M2":
        nq = 7                                # 6 h + a
        V = np.zeros((nq, nq), complex)
        # gap A1 and E parts of h; T2 part (3,4,5) gets a Laplacian stiffness
        Pg = np.outer(trv, trv) + np.outer(eps1, eps1) + np.outer(eps2, eps2)
        V[:6, :6] = prm['m2'] * Pg
        for j in (3, 4, 5):
            V[j, j] = prm['ct'] * L.sum() + prm['ca'] * L[j - 3]   # cubic anisotropy: extra stiffness along own axis
        V[6, 6] = prm['c'] * L.sum()
        b1 = np.zeros(6, complex); b1[3] = 1j * sx * s2; b1[4] = 1j * sy * s2; b1[5] = 1j * sz * s2
        V[6, :6] = prm['g'] * b1.conj(); V[:6, 6] = prm['g'] * b1
        K = np.eye(nq)
    n = V.shape[0]
    H = np.zeros((2 * n, 2 * n), complex); H[:n, :n] = V; H[n:, n:] = K
    return H, n

def rho(R, model):
    a2 = irr['A2'][idx(R)][0, 0]
    blocks = [sym2_rep(R)] + [np.array([[a2]])] * (2 if model == "M1" else 1)
    nq = sum(b.shape[0] for b in blocks)
    Rq = np.zeros((nq, nq)); o = 0
    for b in blocks:
        d = b.shape[0]; Rq[o:o + d, o:o + d] = b; o += d
    return np.kron(np.eye(2), Rq)

def modes(k, model, prm):
    H, n = symbol(np.asarray(k, float), model, prm)
    J = np.block([[np.zeros((n, n)), np.eye(n)], [-np.eye(n), np.zeros((n, n))]])
    lam, vec = np.linalg.eig(J @ H)
    om = (1j * lam).real
    return om, vec, H, n

def psd_check(model, prm, N=24):
    """min eigenvalue of H(k), relative to the k-scale of the soft block: zone grid (k != 0) plus a radial small-k scan."""
    mn = np.inf
    g = np.linspace(-np.pi, np.pi, N, endpoint=False)
    for kx in g:
        for ky in g:
            for kz in g:
                if kx == 0 and ky == 0 and kz == 0: continue
                H, n = symbol(np.array([kx, ky, kz]), model, prm)
                mn = min(mn, np.linalg.eigvalsh(H).min())
    rng = np.random.default_rng(1)
    mn_small = np.inf
    for _ in range(200):
        d = rng.normal(size=3); d /= np.linalg.norm(d)
        for t in (1e-4, 1e-3, 1e-2, 1e-1, 0.5):
            H, n = symbol(t * d, model, prm)
            mn_small = min(mn_small, np.linalg.eigvalsh(H).min() / t**2)
    return mn, mn_small

def label(z):
    w = np.exp(2j * np.pi / 3)
    for name, v in [("+1", 1), ("-1", -1), ("+i", 1j), ("-i", -1j), ("w", w), ("wbar", w.conjugate())]:
        if abs(z - v) < 1e-6: return name
    return str(np.round(z, 4))

def analyse(model, prm, title):
    print(f"\n=== {title} ===  params {prm}")
    a, b = psd_check(model, prm)
    print(f"  min eigenvalue of H(k): zone grid 24^3 (k!=0) {a:.3e}; small-k radial scan, min eig/|k|^2 = {b:.3e}  (PSD if both >= 0)")
    dirs = {"z (C4)": [0, 0, 1], "x (C4)": [1, 0, 0], "111 (C3)": [1, 1, 1], "110 (C2')": [1, 1, 0], "generic (1,2,5)": [1, 2, 5], "generic (2,1,3)": [2, 1, 3]}
    stab = {"z (C4)": C4, "111 (C3)": C3, "110 (C2')": C2p}
    for nm, d in dirs.items():
        kh = np.asarray(d, float); kh /= np.linalg.norm(kh)
        out = []
        for t in (1e-3, 2e-3):
            om, vec, H, n = modes(t * kh, model, prm)
            pos = np.sort(om[om > 1e-12])
            out.append(pos)
        gl = out[0][out[0] < 0.05]                  # gapless group at t = 1e-3
        ng = len(gl)
        slopes = gl / 1e-3; slopes2 = out[1][:ng] / 2e-3
        print(f"  {nm:16s}: gapless branches {ng}; omega/|k| at |k|=1e-3: {np.round(slopes, 5)}; at 2e-3: {np.round(slopes2, 5)}; gapped min {out[0][ng]:.3f}")
        # eigenvectors of gapless positive-frequency modes
        t = 1e-3
        om, vec, H, n = modes(t * kh, model, prm)
        sel = np.where((om > 1e-12) & (om < 0.05))[0]
        PT = tt_projector(kh)
        for j in sel:
            v = vec[:, j]
            nrm = np.real(v.conj() @ H @ v)
            v = v * np.sqrt(om[j] / nrm)          # quantum normalisation v^dag H v = omega
            hq = v[:6]
            res_h = 2 * om[j] * np.real(hq.conj() @ hq)
            res_tt = 2 * om[j] * np.real(hq.conj() @ PT @ hq)
            print(f"      branch omega/|k|={om[j]/t:.5f}: h-weight 2w|h|^2={res_h:.3e}, h-TT weight={res_tt:.3e}, TT fraction of h-part={res_tt/max(res_h,1e-300):.4f}")
        if nm in stab:
            W = vec[:, sel]
            M = np.linalg.pinv(W) @ rho(stab[nm], model) @ W
            ev = np.linalg.eigvals(M)
            print(f"      stabilizer eigenvalues on the gapless positive-frequency space: {sorted(label(z) for z in ev)}")

if __name__ == "__main__":
    analyse("M1", dict(m2=1.0, c1=1.0, c2=0.7, g1=0.3, g2=0.3), "M1: six gapped h pairs + two A2 pairs")
    analyse("M2", dict(m2=1.0, ct=1.0, ca=0.5, c=0.6, g=0.3), "M2-bad: soft A2-T2 coupling at O(k) (expected NOT PSD: soft-soft couplings must be O(k^2))")
    analyse("M2", dict(m2=1.0, ct=1.0, ca=0.5, c=0.6, g=0.0), "M2: soft content 2A2 + 2T2 (no O(k) soft-soft coupling; A2-T2 coupling first allowed at O(k^3))")
