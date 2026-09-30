"""Test B (+E, F): probe-5 Bell protocol, exact ensemble from non-equilibrium starts."""
import numpy as np, sys, json, time
from common import *

L = 24
ring = Ring(L)
SETS = [(0.0, np.pi/4), (0.0, -np.pi/4), (np.pi/2, np.pi/4), (np.pi/2, -np.pi/4)]  # (thA, thB)
TE = np.arange(0, 9.0)   # t = 0..8
side = np.where(np.arange(L) >= 12, 1.0, -1.0)

models = {s: Bell2(L, s[0], s[1], ring) for s in SETS}
P0 = {s: models[s].P(0.0) for s in SETS}   # settings are coin rotations: position marginal identical
Pbase = P0[SETS[0]]
for s in SETS:
    assert np.abs(P0[s] - Pbase).max() < 1e-14

x = np.arange(L)
def gauss(w, c=12):
    g = np.exp(-(x - c) ** 2 / (2 * w ** 2)); return g / g.sum()

# marginal (probability) of the equilibrium start along one ring
margA = Pbase.sum(1)
margB = Pbase.sum(0)
assert np.abs(Pbase - np.outer(margA, margB)).max() < 1e-14      # product law at t=0 (Test F: I_0 = 0)

def prod(a, b): return np.outer(a, b)
sgn = np.where(x >= 12, 1.0, -1.0)
starts = {
    '0 equilibrium': Pbase.copy(),
    '1 width x2 (prob width 2.1)': prod(gauss(2.0*1.5*0.7071*np.sqrt(2)/np.sqrt(2)*1.0/1.0*1.0 if False else 3.0/np.sqrt(2)), gauss(3.0/np.sqrt(2))),
    '2 width x0.4': prod(gauss(0.4*1.5/np.sqrt(2)*np.sqrt(2)*0.7071/0.7071*0.7071), gauss(0.4*1.5/np.sqrt(2)*np.sqrt(2)*0.7071/0.7071*0.7071)),
    '3 shifted by 2': prod(np.roll(margA, 2), np.roll(margB, 2)),
    '4 uniform': np.full((L, L), 1.0 / L**2),
    '5 point mass at (12,12)': np.zeros((L, L)),
    '6 correlated 1+0.5 sA sB': None,
}
starts['5 point mass at (12,12)'][12, 12] = 1.0
c6 = Pbase * (1 + 0.5 * np.outer(sgn, sgn)); starts['6 correlated 1+0.5 sA sB'] = c6 / c6.sum()
# fix widths: equilibrium marginal has std 1.5/sqrt(2)=1.06; x2 -> 2.12 ; x0.4 -> 0.42 (as Gaussian in probability with std)
starts['1 width x2 (prob width 2.1)'] = prod(gauss(2.0 * 1.5 / np.sqrt(2)), gauss(2.0 * 1.5 / np.sqrt(2)))
starts['2 width x0.4'] = prod(gauss(0.4 * 1.5 / np.sqrt(2)), gauss(0.4 * 1.5 / np.sqrt(2)))
for k in starts: starts[k] = starts[k] / starts[k].sum()

def analyse(name, rho0, gamma=0.0, verbose=True):
    res = {}
    runs = {}
    for s in SETS:
        runs[s] = models[s].evolve(rho0, TE, gamma=gamma)
    Ps = {s: np.array([models[s].P(t) for t in TE]) for s in SETS}
    D = np.array([[kl(runs[s][i], Ps[s][i]) for i in range(len(TE))] for s in SETS])
    TVd = np.array([[tv(runs[s][i], Ps[s][i]) for i in range(len(TE))] for s in SETS])
    # signalling time series
    Sig = []
    for i in range(len(TE)):
        pB = {s: (runs[s][i].sum(0) * (side > 0)).sum() for s in SETS}      # P(B=+)
        pA = {s: (runs[s][i].sum(1) * (side > 0)).sum() for s in SETS}      # P(A=+)
        sAB = max(abs(pB[(0.0, tb)] - pB[(np.pi/2, tb)]) for tb in (np.pi/4, -np.pi/4))
        sBA = max(abs(pA[(ta, np.pi/4)] - pA[(ta, -np.pi/4)]) for ta in (0.0, np.pi/2))
        Sig.append(max(sAB, sBA))
    Sig = np.array(Sig)
    # CHSH from records at t=8 and from |psi|^2
    def corr(rho): return float((rho * np.outer(side, side)).sum())
    E_rec = {s: corr(runs[s][-1]) for s in SETS}
    E_psi = {s: corr(Ps[s][-1]) for s in SETS}
    def chsh(E): return abs(E[(0.0, np.pi/4)] + E[(0.0, -np.pi/4)] + E[(np.pi/2, np.pi/4)] - E[(np.pi/2, -np.pi/4)])
    out = dict(name=name, gamma=gamma,
               D0=float(D[:, 0].mean()), D8=float(D[:, -1].mean()), ratio8=float(D[:, -1].mean() / max(D[:, 0].mean(), 1e-300)),
               ratio8_max=float((D[:, -1] / np.maximum(D[:, 0], 1e-300)).max()),
               TV0=float(TVd[:, 0].mean()), TV8=float(TVd[:, -1].mean()),
               S8=float(Sig[-1]), Smax=float(Sig.max()), tSmax=float(TE[Sig.argmax()]),
               chsh_rec=chsh(E_rec), chsh_psi=chsh(E_psi), E_rec=[E_rec[s] for s in SETS], E_psi=[E_psi[s] for s in SETS],
               maxdiff_eq=float(max(np.abs(runs[s][-1] - Ps[s][-1]).max() for s in SETS)),
               D_series=D.mean(0).tolist(), S_series=Sig.tolist())
    if verbose:
        print(f"{name:32s} g={gamma:4.2f} D0={out['D0']:.3f} D8={out['D8']:.3f} ratio={out['ratio8']:.3f} (max {out['ratio8_max']:.3f}) "
              f"TV8={out['TV8']:.3f} S8={out['S8']:.4f} Smax={out['Smax']:.4f}@t={out['tSmax']:.0f} CHSH_rec={out['chsh_rec']:.3f} CHSH_psi={out['chsh_psi']:.3f}", flush=True)
    return out

if __name__ == '__main__':
    import os
    t0 = time.time()
    results = []
    sel = sys.argv[1].split(',') if len(sys.argv) > 1 else None
    cap = float(os.environ['RATE_CAP']) if 'RATE_CAP' in os.environ else None
    for mdl in models.values(): mdl.cap = cap
    tag = sys.argv[2] if len(sys.argv) > 2 else 'all'
    for k, r0 in starts.items():
        if sel and k[0] not in sel: continue
        results.append(analyse(k, r0))
    print('time', time.time() - t0)
    json.dump(results, open(f'testB_results_{tag}.json', 'w'), indent=1)
    # Test F: mutual information of P_t
    print('--- Test F: mutual information I(xA;xB) under |psi_t|^2 (setting theta_A=0, theta_B=pi/4) ---')
    m = models[SETS[0]]
    for t in [0, 2, 4, 6, 8]:
        P = m.P(float(t)); a = P.sum(1); b = P.sum(0)
        mask = P > 1e-300
        I = float((P[mask] * np.log(P[mask] / np.outer(a, b)[mask])).sum())
        print(f't={t}: I = {I:.6f} nats')
