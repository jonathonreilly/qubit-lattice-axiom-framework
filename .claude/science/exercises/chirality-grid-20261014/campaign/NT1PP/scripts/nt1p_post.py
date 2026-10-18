"""NT-1' post-processing of saved HIGH-level kernels (no physics runs): phase effect on the lowest mode.
usage: python3 nt1p_post.py"""
import numpy as np, glob
for f in sorted(glob.glob('pool_NT1P_*_NT1P_Zchi.npy')):
    Zc = np.load(f); Zm = np.load(f.replace('Zchi', 'Zmod')); Hc = 0.5 * (Zc + Zc.conj().T)
    ec, Vc = np.linalg.eigh(Hc); em, Vm = np.linalg.eigh(Zm.real)
    v = Vm[:, 0]; first = (v.conj() @ (Hc - Zm.real) @ v).real
    print(f"{f}: k={len(Zc)} lam_min chi {ec[0]:+.5e} mod {em[0]:+.5e} diff {ec[0]-em[0]:+.2e}; first-order phase shift <v|Hc-Zm|v> {first:+.2e}; "
          f"||Hc - Zm||_2 {np.linalg.norm(Hc - Zm, 2):.2e}; |<v_chi|v_mod>| {abs(Vc[:, 0].conj() @ v):.6f}; "
          f"lowest-mode weights (|v|^2 > 0.05): " + " ".join(f"{i}:{w:.2f}" for i, w in enumerate(np.abs(Vc[:, 0]) ** 2) if w > 0.05))
