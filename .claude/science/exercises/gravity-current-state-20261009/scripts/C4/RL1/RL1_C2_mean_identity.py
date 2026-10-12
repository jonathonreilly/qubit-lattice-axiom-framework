"""RL1 (C2): check the exact identity E[H(x,y)] = Hbar(tau) (mean of realization inverse = Neumann series of the mean kernel)
at small 4D diamonds where the realization noise is still manageable; Hbar from RL1_B (Volterra, grid h_fine=0.02)."""
import numpy as np, sys
sys.argv = [sys.argv[0], "4", "1", "1"]
exec(open("RL1_C_bd_inverse_mc.py").read().split('if __name__ == "__main__":')[0])
d = np.load("RL1_B_Hbar_h0.02.npz"); taus, Hb = d["taus"], d["H"]
for T, R in [(1.0, 40000), (1.5, 40000), (2.0, 40000), (2.5, 20000), (3.0, 20000)]:
    H, L, phi, Nm = run(T, 4, R, lambda P: np.zeros(P.shape[0]))
    m, se = H.mean(), H.std(ddof=1)/np.sqrt(R)
    print(f"T={T}: <N>={Nm:.2f}  MC E[H]={m:+.4f} +- {se:.4f}   Volterra Hbar={np.interp(T, taus, Hb):+.4f}   z={(m-np.interp(T, taus, Hb))/se:+.2f}   E[L]={L.mean():.4f} vs exp(-pi T^4/24)={np.exp(-np.pi*T**4/24):.4f}")
    sys.stdout.flush()
