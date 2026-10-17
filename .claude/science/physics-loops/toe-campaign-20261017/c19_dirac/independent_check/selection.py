"""Item 1 (selection rule, all ranges, real/imag, A1/A2), the mass space, and the Dirac dispersion."""
import numpy as np
from core import *
from bases import get

rng = np.random.default_rng(5)
fm = fixed_momenta(); KS = np.array(fm[0]) * np.pi / 4; KM = np.array(fm[1]) * np.pi / 4
D = [(1j ** w) * W for w, W in zip(W1, WR)]
Lf = lift(D)[0]
# isotypic projectors of the 12-dim internal space (lift 0)
def isoproj(ch, dim):
    P = sum(np.conj(ch[g]) * Lf[g] for g in range(48)) * dim / 48
    e, V = np.linalg.eigh((P + P.conj().T) / 2); return V[:, e > 0.5]
V12 = isoproj(CH12, 2); V52 = isoproj(CH52, 2)
print("E1/2 and E5/2 isotypic subspaces of the 12-dim shell: dims", V12.shape[1], V52.shape[1])
print("complex conjugation maps E1/2 subspace onto E5/2 subspace:",
      np.allclose(V52 @ V52.conj().T @ V12.conj(), V12.conj()))

def coupling(mst, k):
    """2x2 blocks of a staggered operator between the doublets: k -> k+Q. Both assignments."""
    B = bloch(mst, k + Q)
    return V52.conj().T @ B @ V12, V12.conj().T @ B @ V52
def maxc(names):
    out = {}
    for nm in names:
        bs = get(nm); mx = 0
        for m in bs:
            a, b = coupling(m, KS); a2, b2 = coupling(m, KM)
            mx = max(mx, np.abs(a).max(), np.abs(b).max(), np.abs(a2).max(), np.abs(b2).max())
        out[nm] = (len(bs), mx)
    return out
print("\n== staggered (momentum Q) terms: max |matrix element| between the k* doublet and the -k* doublet")
for S in ('onsite', 'r1', 'l1<=2', 'cube'):
    for ri in ('re', 'im'):
        for ch in ('A1', 'A2'):
            nm = f'Q_{S}_{ri}_{ch}'; (n, mx) = maxc([nm])[nm]
            # rank of the coupling map (real dimension of achievable 2x2 couplings)
            vecs = []
            for m in get(nm):
                a, _ = coupling(m, KS); vecs.append(np.concatenate([a.real.ravel(), a.imag.ravel()]))
            rk = np.linalg.matrix_rank(np.array(vecs), tol=1e-9) if vecs else 0
            print(f"  {nm:18s} dim {n:3d}: max coupling {mx:.2e}; real rank of coupling map {rk}")

print("\n== momentum-0 O-invariant terms: diagonal blocks within each doublet are multiples of 1 (Schur)")
for S in ('onsite', 'r1', 'l1<=2', 'cube'):
    for ri in ('re', 'im'):
        nm = f'P0_{S}_{ri}_O'; dev = 0
        for m in get(nm):
            for k in (KS, KM):
                Hk = bloch(m, k)
                for V in (V12, V52):
                    b = V.conj().T @ Hk @ V; dev = max(dev, np.abs(b - np.trace(b) / 2 * np.eye(2)).max())
                b = V52.conj().T @ Hk @ V12; dev = max(dev, np.abs(b).max())
        print(f"  {nm:18s}: max deviation from scalar / max off-diagonal {dev:.1e}")

# ---- Base model and the claimed mass
h0 = hop(-1.0, 0.2); Xb = get('X_r1')
def rndX():
    c = rng.normal(size=len(Xb)); m = addm(*Xb, coeffs=list(c))
    nrm = max(np.abs(M).max() for M in m.values()); return {k: v / nrm for k, v in m.items()}
X = rndX(); Hb = addm(h0, X, coeffs=[1, 0.05])
Mb = get('Q_onsite_im_A2')
def rndM(bs):
    c = rng.normal(size=len(bs)); m = addm(*bs, coeffs=list(c))
    nrm = max(np.abs(M).max() for M in m.values()); return {k: v / nrm for k, v in m.items()}
M = rndM(Mb)
print("\n== Dirac mass from an imaginary A2 staggered on-site term (random element, max-entry normalized)")
EN = np.linalg.eigvalsh(bloch(Hb, KS))[0]
for m in (0.002, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2):
    e = np.linalg.eigvalsh(fold(Hb, {k: m * v for k, v in M.items()}, KS))
    mD = (e[2] - e[1]) / 2
    print(f"  m = {m:.3f}: lowest four at k*: {np.round(e[:4] - EN, 6)};  m_D/m = {mD/m:.5f}; centre shift {(e[1]+e[2])/2-EN:+.2e}")

# is the node-space mass independent of X, t2? (the doublets are fixed subspaces)
a, _ = coupling(M, KS); print("  projected coupling singular values (per unit m):", np.round(np.linalg.svd(a, compute_uv=False), 5))
for t2, dl in ((0.2, 0.3), (-0.4, 0.1)):
    H2 = addm(hop(-1.0, t2), rndX(), coeffs=[1, dl]); e = np.linalg.eigvalsh(fold(H2, {k: 0.01 * v for k, v in M.items()}, KS))
    E0 = np.linalg.eigvalsh(bloch(H2, KS))[0]
    print(f"  t2={t2}, delta={dl}, new X: m_D/m at m=0.01 = {(e[2]-e[1])/2/0.01:.5f}")

# ---- Dirac dispersion: proper test with |q| up to several m_D / v
print("\n== Dirac dispersion E - E_N = +-sqrt(v^2 q^2 + m_D^2): v = Weyl velocity at m = 0")
dirs = rng.normal(size=(12, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
vW = np.mean([(np.linalg.eigvalsh(bloch(Hb, KS + 1e-5 * d))[1] - np.linalg.eigvalsh(bloch(Hb, KS + 1e-5 * d))[0]) / 2e-5 for d in dirs])
# note: (E1 - E0)/(2 dq) = v if E = +-v q
print(f"  Weyl node: E = E_N +- v_W |q| with v_W = {vW:.5f}  (runner divides its 'vel' by 2 before the Dirac fit)")
for m in (0.005, 0.02, 0.05):
    Mm = {k: m * v for k, v in M.items()}
    e0 = np.linalg.eigvalsh(fold(Hb, Mm, KS)); mD = (e0[2] - e0[1]) / 2; mid = (e0[1] + e0[2]) / 2
    for vtest, lab in ((vW, 'v_W'), (vW / 2, 'v_W/2')):
        dev = []; aniso = []
        for x in (0.25, 0.5, 1, 2, 4):
            q = x * mD / vW; Es = []
            for d in dirs:
                ee = np.linalg.eigvalsh(fold(Hb, Mm, KS + q * d)); Es.append(ee[2] - mid)
                dev.append(abs(Es[-1] - np.sqrt(vtest**2 * q**2 + mD**2)) / np.sqrt(vtest**2 * q**2 + mD**2))
            aniso.append(np.ptp(Es) / np.mean(Es))
        print(f"  m={m}: m_D={mD:.5f}; q up to 4 m_D/v_W = {4*mD/vW:.3f}; vs sqrt with {lab:6s}: max rel dev {max(dev):.2e};"
              f" angular spread at fixed |q| (x=.25..4): {np.round(aniso, 6)}")
# fit v from the massive band
m = 0.01; Mm = {k: m * v for k, v in M.items()}
e0 = np.linalg.eigvalsh(fold(Hb, Mm, KS)); mD = (e0[2] - e0[1]) / 2; mid = (e0[1] + e0[2]) / 2
qs = np.linspace(0.2, 3, 15) * mD / vW
fit = []
for d in dirs[:4]:
    E = np.array([np.linalg.eigvalsh(fold(Hb, Mm, KS + q * d))[2] - mid for q in qs])
    fit.append(np.sqrt(np.polyfit(qs**2, E**2, 1)[0]))
print(f"  fitted Dirac velocity at m=0.01 (E^2 vs q^2, 4 dirs): {np.round(fit, 5)}  vs v_W = {vW:.5f}")
