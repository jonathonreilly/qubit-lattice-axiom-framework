"""C2: Kitaev, broadened Drude ratio r_delta = sum_{|lam-mu|<delta} |K_lm|^2 / sum |K_lm|^2 at Majorana beta=0
(fraction of current weight below frequency delta; ~ time window t ~ 1/delta). Takes the limits in the right
order: L large at fixed delta first, then delta -> 0. A nonzero Drude weight needs r_delta -> const > 0 as delta -> 0."""
import numpy as np
from c2_kitaev_majorana import build
rng = np.random.default_rng(99)
deltas = [0.4, 0.2, 0.1, 0.05, 0.025, 0.0125]
print("Kitaev isotropic, z-bond flips prob q; r_delta for delta = " + ", ".join(map(str, deltas)))
for q in [0.0, 0.005, 0.02, 0.1]:
    for L in [16, 24, 32, 40]:
        A0, B0, bonds = build(L)
        zb = np.array([t == 2 for (_, _, t, _) in bonds])
        ns = 1 if q == 0 else {16: 6, 24: 4, 32: 2, 40: 2}[L]
        R = []
        for s in range(ns):
            u = np.where((rng.random(len(bonds)) < q) & zb, -1.0, 1.0)
            A, B, _ = build(L, u=u)
            w, V = np.linalg.eigh(1j*A)
            K2 = np.abs(V.conj().T @ (1j*B) @ V)**2
            dw = np.abs(w[:, None] - w[None, :])
            tot = K2.sum()
            R.append([K2[dw < d].sum()/tot for d in deltas])
        R = np.array(R); m = R.mean(0); e = R.std(0)/np.sqrt(len(R))
        spacing = 12.0/(2*L*L)
        print(f"q={q:5.3f} L={L:3d} (level spacing ~{spacing:.4f})  r_delta = " + "  ".join(f"{a:.3f}+-{b:.3f}" for a, b in zip(m, e)), flush=True)
