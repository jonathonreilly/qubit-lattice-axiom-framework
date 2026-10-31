#!/usr/bin/env python3
"""x9: Gaussian leading coefficient of the second difference of the plaquette-energy
reflection correlation (EXISTENCE §19, T29), and the exact Gaussian conditional/coarse split.
Criteria: checks/x9_criteria.md (pre-registered). Free lattice Maxwell, one colour."""
import os, sys, time, resource
import numpy as np

t_start = time.time()

def khat2(T):
    k = 2 * np.pi * np.arange(T) / T
    return 4 * np.sin(k / 2) ** 2, k

def G_torus(T, dmax, cutoff=None):
    """G_T(d) for d=0..dmax; optional sharp low-momentum restriction |k_mu|<pi/cutoff (signed k)."""
    kh, k = khat2(T)
    ks = np.where(k > np.pi, k - 2 * np.pi, k)  # signed momenta in (-pi, pi]
    k1 = kh[:, None, None]; k2 = kh[None, :, None]; k3 = kh[None, None, :]
    spat = k1 + k2 + k3
    num = k1 + k2  # broadcast (T,T,1)
    if cutoff is not None:
        lim = np.pi / cutoff
        m1 = (np.abs(ks) < lim)
        mask_sp = m1[:, None, None] & m1[None, :, None] & m1[None, None, :]
    G = np.zeros(dmax + 1)
    for i0 in range(T):
        if cutoff is not None and not (abs(ks[i0]) < np.pi / cutoff):
            continue
        den = kh[i0] + spat
        with np.errstate(divide='ignore', invalid='ignore'):
            r = np.where(den > 0, num / np.where(den > 0, den, 1.0), 0.0)
        if cutoff is not None:
            r = r * mask_sp
        s = r.sum()
        G += s * np.cos(k[i0] * np.arange(dmax + 1))
    return G / T ** 4

def dense_G(T=4, dmax=3):
    # links indexed (x, mu); x in Z_T^4
    V = T ** 4
    def idx(x, mu):
        x = [c % T for c in x]
        return ((((x[0] * T + x[1]) * T + x[2]) * T + x[3]) * 4 + mu)
    n = 4 * V
    rows = []
    for x0 in range(T):
        for x1 in range(T):
            for x2 in range(T):
                for x3 in range(T):
                    x = [x0, x1, x2, x3]
                    for mu in range(4):
                        for nu in range(mu + 1, 4):
                            c = np.zeros(n)
                            e_mu = [0] * 4; e_mu[mu] = 1
                            e_nu = [0] * 4; e_nu[nu] = 1
                            c[idx(x, mu)] += 1
                            c[idx([a + b for a, b in zip(x, e_mu)], nu)] += 1
                            c[idx([a + b for a, b in zip(x, e_nu)], mu)] -= 1
                            c[idx(x, nu)] -= 1
                            rows.append(((tuple(x), mu, nu), c))
    C = np.array([r[1] for r in rows])
    M = C.T @ C
    Mp = np.linalg.pinv(M, rcond=1e-10, hermitian=True)
    def cvec(x, mu, nu):
        for key, c in rows:
            if key == (tuple(x), mu, nu):
                return c
    c0 = cvec([0, 0, 0, 0], 1, 2)
    out = []
    for d in range(dmax + 1):
        cd = cvec([d % T, 0, 0, 0], 1, 2)
        out.append(c0 @ Mp @ cd)
    return np.array(out)

fails = []
print("x9: Gaussian second-difference coefficient (lattice Maxwell, one colour)")
# ---- A3 dense check first (small)
Gd = dense_G(4, 3)
Gm = G_torus(4, 3)
err = np.max(np.abs(Gd - Gm))
print(f"A3 dense pinv vs momentum on 4^4: G_dense={np.array2string(Gd, precision=10)}; max|diff|={err:.2e}")
if not err < 1e-10:
    fails.append("A3")

Ts = [16, 24, 32, 48]
Gs = {}
for T in Ts:
    Gs[T] = G_torus(T, 12)
def A(G, d, h):
    return 0.5 * (G[d] ** 2 - 2 * G[d + h] ** 2 + G[d + 2 * h] ** 2)
print("A0 G_T(d), d=1..8:")
for T in Ts:
    g = Gs[T][1:9]
    print(f"  T={T:2d}: " + " ".join(f"{v:.6e}" for v in g))
    if np.any(g <= 0):
        fails.append(f"A0 T={T}")
print("A1 A_T(d,h):")
for T in Ts:
    row = []
    for d in (1, 3, 5):
        for h in (1, 2):
            a = A(Gs[T], d, h)
            row.append(f"A({d},{h})={a:.6e}")
            if not a > 0:
                fails.append(f"A1 T={T} d={d} h={h}")
    print(f"  T={T:2d}: " + "  ".join(row))
for d in (1, 3):
    rel = abs(A(Gs[32], d, 1) - A(Gs[48], d, 1)) / A(Gs[48], d, 1)
    print(f"A2 d={d}: |A32-A48|/A48 = {rel:.3e}")
    if not rel < 1e-2:
        fails.append(f"A2 d={d}")
g = Gs[48]
lc = [g[d] * g[d + 2] - g[d + 1] ** 2 for d in range(1, 7)]
print("A4 (info) log-convexity G(d)G(d+2)-G(d+1)^2, d=1..6 (T=48): " + " ".join(f"{v:.3e}" for v in lc),
      "all>=0" if all(v >= 0 for v in lc) else "NOT all >= 0")
dd = np.arange(2, 9)
slope = np.polyfit(np.log(dd), np.log(g[2:9]), 1)[0]
print(f"A4 (info) fitted decay exponent of G(d), d=2..8, T=48: {slope:.3f}")
print(f"Explicit leading coefficients (one colour, Phi=F^2/2): A_48(1,1)={A(g,1,1):.6e}, A_48(3,1)={A(g,3,1):.6e}")
print(f"  ratios A(1,1)/C(1) = {A(g,1,1)/(0.5*g[1]**2):.4f}, A(3,1)/C(3) = {A(g,3,1)/(0.5*g[3]**2):.4f}")

# ---- B: exact Gaussian split for sharp low-momentum sigma-algebra
print("B (informational): T=64, sharp low-momentum sigma-algebra |k_mu|<pi/l")
T = 64
Gfull = G_torus(T, 4)
res = []
for l in (4, 8, 16):
    Gl = G_torus(T, 4, cutoff=l)
    Gh = Gfull - Gl
    cond = 0.5 * Gh[1] ** 2 + Gl[1] * Gh[1]
    coarse = 0.5 * Gl[1] ** 2
    ident = abs(cond + coarse - 0.5 * Gfull[1] ** 2)
    coarseD = 0.5 * (Gl[1] ** 2 - 2 * Gl[2] ** 2 + Gl[3] ** 2)
    AD = A(Gfull, 1, 1)
    res.append((l, Gl[0]))
    print(f"  l={l:2d}: V_l=G_l(0)={Gl[0]:.4e}; coarse term={coarse:.4e}; ratio to C(1)={coarse/(0.5*Gfull[1]**2):.3e}; "
          f"identity err={ident:.1e}; D: coarse={coarseD:.3e}, ratio to A(1,1)={coarseD/AD:.3e}")
    if not ident < 1e-12:
        fails.append(f"B identity l={l}")
ex = np.log(res[2][1] / res[1][1]) / np.log(16 / 8)
print(f"B1 fitted exponent of V_l between l=8 and l=16: {ex:.3f} ->",
      "consistent" if -4.5 <= ex <= -3.5 else "not consistent")
print("RESULT:", "PASS (A0-A3)" if not fails else "FAIL " + ", ".join(fails))
peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6
print(f"wall {time.time()-t_start:.1f} s, peak RSS {peak:.0f} MB (macOS ru_maxrss bytes/1e6)")
