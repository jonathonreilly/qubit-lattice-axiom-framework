"""R5-2 (C): independent recheck, on R4-1's per-shell data (loaded with allow_pickle=False), of INFINITE-ORBIT kernels
f_m = exp(-m/L^2) * cubic(m/L^2) on ALL shells m>=1, with the mean-box conditions imposed on the INFINITE sums
(sum_m C_m f_m m^k = 0, k=0,1,2;  (pi/16) sum C_m f_m m^2 ln m = -1).  For L <= 2.5 the weights beyond the
enumerated shells (m > 160) are < exp(-25)*poly, so the per-realization sum over m<=160 equals the infinite-orbit
operator up to that tail (bounded below).  Output: rms over frames of (B_g phi - Bbar phi)/|box phi| vs l."""
import numpy as np, sys
R41 = sys.argv[1]
d = np.load(R41 + '/r41_B_M160_seed11_eta1.0.npz', allow_pickle=False)
S = d['S']; I = d['I']; ells = d['ells']; M = S.shape[2]
C = np.load(R41 + '/C_siegel.npy', allow_pickle=False)     # m = 0..200 (Siegel, R4-1 A)
Mfull = len(C) - 1
mv = np.arange(1, Mfull+1).astype(float); Cm = C[1:]
for L in (1.5, 2.0, 2.5):
    x = mv/L**2; base = np.exp(-x)
    cols = np.stack([base*x**j for j in range(4)], 1)*Cm[:, None]          # g-columns on m = 1..Mfull
    A = np.stack([cols.T @ mv**k for k in range(3)] + [cols.T @ (mv**2*np.log(mv))])
    coef = np.linalg.solve(A, np.array([0, 0, 0, -16/np.pi]))
    g = cols @ coef; f = g/Cm
    c = -(np.pi/2)*np.sum(g*mv*np.log(mv))
    tail_f = np.abs(f[M:]).max() if Mfull > M else 0.0
    # bound of the omitted tail m in (Mfull, inf): |f_m| <= exp(-m/L^2)*sum|coef|*(m/L^2)^3 / min C (C_m >= 0.0117 for m <= 128; crude)
    mt = np.arange(Mfull+1, 4000).astype(float); xt = mt/L**2
    tail_bound = np.sum(np.exp(-xt)*np.abs(coef).sum()*np.maximum(1, xt)**3)
    print(f"\nL={L}: c={c:+.4f}, coef={np.array2string(coef, precision=4)}, max|f_m| on 161..200 = {tail_f:.2e}, "
          f"sum_(m>200) |g_m| bound = {tail_bound:.1e}")
    print(f"   moments over m<=200: S0={g.sum():.1e} S1={(g*mv).sum():.1e} S2={(g*mv**2).sum():.1e}")
    fM = f[:M]
    rows = []
    for j, l in enumerate(ells):
        box = -2/l**2
        bbar = c + np.sum(g[:M]*I[j])
        Bg = c + S[:, j, :] @ fM
        rel = (Bg - bbar)/abs(box)
        rows.append((l, bbar/box, np.sqrt(np.mean(rel**2)), rel.std()))
        print(f"   l={l:5.1f}  mean/box={bbar/box:9.5f}   rms rel dev={rows[-1][2]:.3e}   sd={rows[-1][3]:.3e}")
    o = np.array(rows); big = o[:, 0] >= 6
    print(f"   slope d ln rms / d ln l (l>=6): {np.polyfit(np.log(o[big,0]), np.log(o[big,2]), 1)[0]:+.2f}")
