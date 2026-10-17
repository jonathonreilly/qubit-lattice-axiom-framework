"""Item 3: Dirac dispersion, done as an asymptotic test.  Decompose the four node bands as
E = E_N + s(q) +- r(q), s = (E_up + E_lo)/2 - E_N (scalar part), r = (E_up - E_lo)/2, and compare r with
sqrt(v_W^2 q^2 + m_D^2) for q = x m_D / v_W, as m -> 0.  Also the runner's own Hamiltonian."""
import pickle, sys
import numpy as np
from core import *
from bases import get

rng = np.random.default_rng(5)
fm = fixed_momenta(); KS = np.array(fm[0]) * np.pi / 4
Xb = get('X_r1'); Mb = get('Q_onsite_im_A2')
def rnd(bs):
    c = rng.normal(size=len(bs)); m = addm(*bs, coeffs=list(c))
    nrm = max(np.abs(M).max() for M in m.values()); return {k: v / nrm for k, v in m.items()}
dirs = rng.normal(size=(10, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]

def analyse(Ffold, Fweyl, k0, label, ms=(1e-4, 1e-3, 1e-2, 0.05)):
    e = np.linalg.eigvalsh(Fweyl(k0)); EN = e[0]
    vW = np.mean([(np.linalg.eigvalsh(Fweyl(k0 + 1e-5 * d))[1] - np.linalg.eigvalsh(Fweyl(k0 + 1e-5 * d))[0]) / 2e-5 for d in dirs])
    # scalar curvature c of the Weyl pair: (E0+E1)/2 - E_N = c q^2
    qq = 1e-3; cs = [((np.linalg.eigvalsh(Fweyl(k0 + qq * d))[:2].sum() / 2) - EN) / qq**2 for d in dirs]
    c = np.mean(cs)
    print(f"[{label}] E_N = {EN:.6f}; Weyl v_W = {vW:.5f}; scalar curvature c = {c:.5f} (spread {np.ptp(cs):.1e}); "
          f"Dirac regime needs m_D << v_W^2/c = {vW**2/abs(c):.4f}")
    for m in ms:
        e0 = np.linalg.eigvalsh(Ffold(k0, m)); mD = (e0[2] - e0[1]) / 2; mid = (e0[1] + e0[2]) / 2
        devr = []; devfull = []; ani = []
        for x in (0.5, 1, 2, 4):
            q = x * mD / vW; rs = []
            for d in dirs:
                ee = np.linalg.eigvalsh(Ffold(k0 + q * d, m))
                r = (ee[2] - ee[1]) / 2; s = (ee[2] + ee[1]) / 2 - mid; target = np.sqrt(vW**2 * q**2 + mD**2)
                devr.append(abs(r - target) / target); devfull.append(abs((ee[2] - mid) - target) / target); rs.append(ee[2] - mid)
            ani.append(np.ptp(rs) / np.mean(rs))
        print(f"   m = {m:.0e}: m_D = {mD:.3e} (m_D/m = {mD/m:.4f}); q up to 4 m_D/v_W = {4*mD/vW:.2e}:"
              f" |r - sqrt(v_W^2 q^2 + m_D^2)|/sqrt <= {max(devr):.1e};  upper band E-E_N vs +sqrt: {max(devfull):.1e};"
              f" angular spread of upper band at fixed q: {max(ani):.1e}")
    return vW, c

h0 = hop(-1.0, 0.2)
X = rnd(Xb); M = rnd(Mb); Hb = addm(h0, X, coeffs=[1, 0.05])
analyse(lambda k, m: fold(Hb, {a: m * b for a, b in M.items()}, k), lambda k: bloch(Hb, k), KS, 'mine, t2=0.2, delta=0.05')

# runner's own Hamiltonian (dumped) -- convention H(k) = sum bl[sh] e^{+ik.sh}
try:
    R = pickle.load(open('runner_blocks.pkl', 'rb'))
except FileNotFoundError:
    print('runner_blocks.pkl missing'); sys.exit()
bl, blM, kst = R['bl'], R['blM'], R['kst']
def Hk(b, k):
    H = np.zeros((12, 12), complex)
    for sh, Mx in b.items(): H += Mx * np.exp(1j * np.dot(k, sh))
    return H
def Hfold(k, m):
    return np.block([[Hk(bl, k), m * Hk(blM, k).conj().T], [m * Hk(blM, k), Hk(bl, k + Q)]])
print("runner vel (its Weyl velocity) =", np.mean(R['vel']), "; runner then used v = vel/2 =", np.mean(R['vel']) / 2)
vW, c = analyse(Hfold, lambda k: Hk(bl, k), kst, 'runner H', ms=(1e-4, 1e-3, 1e-2, 0.05))
# the runner's own test points: d = 0.005..0.02 at m = 0.05
m = 0.05; e0 = np.linalg.eigvalsh(Hfold(kst, m)); mD = (e0[2] - e0[1]) / 2; mid = (e0[1] + e0[2]) / 2
for vt, lab in ((vW, 'v_W'), (vW / 2, 'v_W/2'), (0.0, 'v = 0 (flat)')):
    dv = []
    for d in (0.005, 0.01, 0.02):
        for n_ in dirs[:3]:
            ee = np.linalg.eigvalsh(Hfold(kst + d * n_, m)); t = np.sqrt(vt**2 * d**2 + mD**2); dv.append(abs((ee[2] - mid) - t) / t)
    print(f"   runner's test (m=0.05, |dk| <= 0.02, m_D/v_W = {mD/vW:.3f}) with {lab}: max rel dev {max(dv):.1e}")
