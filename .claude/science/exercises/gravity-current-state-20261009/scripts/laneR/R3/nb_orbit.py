# N-b: second-chaos norm of a Lorentz-invariant pair kernel grows like T^6 in 4D (T^2 log T in 2D);
# a non-invariant (Euclidean-distance) kernel grows like T^4 (extensive).
# Monte Carlo of I(T) = int_D int_D K(x,y)^2 over a causal diamond D of height T (rho = 1).
import numpy as np
rng = np.random.default_rng(7)

def sample_diamond(n, T, d):
    # uniform points in the causal diamond |x| <= min(t, T - t), t in [0,T]
    out = []
    while sum(len(o) for o in out) < n:
        m = 4 * n
        t = rng.random(m) * T
        x = (rng.random((m, d - 1)) * 2 - 1) * T / 2
        r = np.linalg.norm(x, axis=1)
        keep = r <= np.minimum(t, T - t)
        out.append(np.column_stack([t[keep], x[keep]]))
    return np.vstack(out)[:n]

def vol_diamond(T, d):
    from math import gamma, pi
    if d == 2: return T * T / 2
    if d == 4: return pi * T**4 / 24
def I_pairs(T, d, kind, M=3_000_000):
    V = vol_diamond(T, d)
    P = sample_diamond(M, T, d); Q = sample_diamond(M, T, d)
    dt = Q[:, 0] - P[:, 0]; dx2 = ((Q[:, 1:] - P[:, 1:])**2).sum(1)
    if kind == "inv":
        tau2 = dt * dt - dx2
        K = ((tau2 >= 1) & (tau2 <= 2) & (dt > 0)).astype(float)   # future-timelike pairs, tau^2 in [1,2]
    else:
        e2 = dt * dt + dx2
        K = ((e2 >= 1) & (e2 <= 2) & (dt > 0)).astype(float)       # Euclidean shell: not Lorentz invariant
    m = K.mean(); se = K.std() / np.sqrt(M)
    return V * V * m, V * V * se

for d, Ts in [(4, [4, 6, 8, 11, 16]), (2, [4, 8, 16, 32, 64])]:
    for kind in ["inv", "noninv"]:
        vals = []
        for T in Ts:
            I, se = I_pairs(T, d, kind); vals.append(I)
            print(f"d={d} {kind:6s} T={T:3d}: I={I:.4e} +- {se:.1e}")
        lt, lv = np.log(Ts), np.log(vals)
        p = np.polyfit(lt[-3:], lv[-3:], 1)[0]
        print(f"   -> exponent from the 3 largest T: {p:.2f}")
