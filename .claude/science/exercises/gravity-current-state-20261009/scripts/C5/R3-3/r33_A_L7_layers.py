"""R3-3 (a): mean link / layer kernels of the anisotropic Lorentz-random lattice L7 = diag(sqrt7,1,1,1) Z^4.
Units: physical x = (sqrt7 n0, n1, n2, n3); x^2 = -7 n0^2 + |n|^2 (signature -+++); rho = 1/sqrt7.
For future-timelike v: m = tau^2 = 7 n0^2 - |n|^2 in {1,2,...}.
(1) interval count N(v) = #{w in L7 : 0 << w << v} computed directly for n0 <= NMAX_DIRECT.
(2) Gamma_L-invariance of N: reduce large-n0 vectors by integral spacelike reflections; check N invariant on directly computed pairs.
(3) mean kernel of any interval-count (layer) operator: sum_m C_m theta(t) delta(x^2+m); C_{m,n} = density of vectors of norm m and
    interval count n per unit invariant hyperboloid measure lambda_m = delta(x^2+m) d^4x, from counting in Euclidean balls.
"""
import numpy as np, itertools, time, sys
t0 = time.time()
M = 40            # max tau^2 kept
NMAX_DIRECT = int(sys.argv[2]) if len(sys.argv) > 2 else 8   # direct interval counts for n0 <= this
def Q(n): return -7*n[...,0]**2 + (n[...,1:]**2).sum(-1)
# ---------- (1) direct interval counts ----------
def future_cone_points(n0max):
    pts = []
    for a in range(1, n0max+1):
        r = int(np.floor(np.sqrt(7)*a))
        g = np.arange(-r, r+1)
        X, Y, Z = np.meshgrid(g, g, g, indexing='ij')
        s = X**2+Y**2+Z**2
        k = s < 7*a*a
        pts.append(np.stack([np.full(k.sum(), a), X[k], Y[k], Z[k]], 1))
    return np.concatenate(pts)
S = future_cone_points(NMAX_DIRECT)          # all strictly future-timelike w with w0 <= NMAX_DIRECT
def Ncount(v, cap=None):
    w = S[S[:, 0] < v[0]]
    d = v[None, :] - w
    ok = (d[:, 0] >= 1) & (7*d[:, 0]**2 > (d[:, 1:]**2).sum(1))
    return int(ok.sum())
direct = {}
for a in range(1, NMAX_DIRECT+1):
    r = int(np.floor(np.sqrt(7)*a))
    g = np.arange(-r, r+1)
    X, Y, Z = np.meshgrid(g, g, g, indexing='ij'); s = X**2+Y**2+Z**2
    k = (s < 7*a*a) & (7*a*a - s <= M)
    V = np.stack([np.full(k.sum(), a), X[k], Y[k], Z[k]], 1)
    for v in V:
        key = (int(v[0]), *sorted(map(abs, map(int, v[1:]))))   # cubic symmetry of n1..n3 is in Gamma_L
        if key not in direct:
            direct[key] = Ncount(v)
print(f"[1] direct interval counts: {len(direct)} cubic classes with n0<={NMAX_DIRECT}, m<={M}  ({time.time()-t0:.1f}s)")
# ---------- (2) reflections ----------
roots = []
for r in itertools.product(range(0, 4), range(-9, 10), range(-9, 10), range(-9, 10)):
    r = np.array(r)
    q = int(Q(r))
    if q <= 0 or not r.any(): continue
    # reflection x -> x - 2B(x,r)/Q(r) r integral iff 2 B(e_i, r)/q integral for basis e_i
    Bv = np.array([-7*r[0], r[1], r[2], r[3]])
    if np.all((2*Bv) % q == 0):
        roots.append((r, Bv, q))
print(f"[2] integral spacelike reflection roots with r0<=3, |ri|<=9: {len(roots)}  (Q values {sorted(set(q for _,_,q in roots))})")
def reduce(V):
    V = V.copy()
    for it in range(200):
        best = V.copy(); improved = False
        for r, Bv, q in roots:
            c = 2*(V @ Bv)//q
            W = V - c[:, None]*r[None, :]
            W[W[:, 0] < 0] *= -1   # stays future (spacelike reflections preserve time orientation); guard only
            better = W[:, 0] < best[:, 0]
            if better.any():
                best[better] = W[better]; improved = True
        V = best
        if not improved: break
    return V
def keyof(v): return (int(v[0]), *sorted(map(abs, map(int, v[1:]))))
# invariance check: vectors with n0 in (NMAX_DIRECT//2, NMAX_DIRECT] whose reduction is smaller: compare direct counts
chk = 0; bad = 0
for key, nval in list(direct.items()):
    if key[0] < 3: continue
    v = np.array([key])
    rv = reduce(v)[0]
    if rv[0] < key[0]:
        chk += 1
        if direct.get(keyof(rv)) != nval: bad += 1
print(f"    Gamma_L-invariance of N(v): {chk} directly computed classes reduce to a smaller n0; mismatches = {bad}")
# ---------- (3) counting in Euclidean balls ----------
Rphys = float(sys.argv[1]) if len(sys.argv) > 1 else 150.0
cnt = {}   # (m, N) -> count
unres = 0
unres_n0 = {}
total_v = 0
n0max = int(Rphys/np.sqrt(14)) + 2
for a in range(1, n0max+1):
    rr = int(np.floor(np.sqrt(7)*a))
    g = np.arange(-rr, rr+1)
    X, Y = np.meshgrid(g, g, indexing='ij'); X = X.ravel(); Y = Y.ravel()
    lo = 7*a*a - M - X**2 - Y**2; hi = 7*a*a - 1 - X**2 - Y**2
    rows = []
    for z in range(0, rr+1):
        k = (z*z >= lo) & (z*z <= hi)
        if not k.any(): continue
        for zz in ([z] if z == 0 else [z, -z]):
            rows.append(np.stack([np.full(k.sum(), a), X[k], Y[k], np.full(k.sum(), zz)], 1))
    if not rows: continue
    V = np.concatenate(rows)
    E2 = 7*V[:, 0]**2 + (V[:, 1:]**2).sum(1)
    V = V[E2 <= Rphys**2]
    if len(V) == 0: continue
    RV = reduce(V); total_v += len(V)
    m = (7*V[:, 0]**2 - (V[:, 1:]**2).sum(1))
    for mv, rv in zip(m, RV):
        kk = keyof(rv)
        n = direct.get(kk)
        if n is None:
            unres += 1; n = -1; unres_n0[int(rv[0])] = unres_n0.get(int(rv[0]),0)+1
        cnt[(int(mv), n)] = cnt.get((int(mv), n), 0) + 1
def lam(m, R):
    rmax = np.sqrt(max(R*R - m, 0)/2.0)
    r = np.linspace(0, rmax, 20001)
    f = 4*np.pi*r**2/(2*np.sqrt(r**2+m))
    return np.trapezoid(f, r)
print(f"[3] counting to Euclidean radius R = {Rphys} (n0 <= {n0max}); vectors {total_v}; unresolved reductions: {unres} by reduced n0 {dict(sorted(unres_n0.items()))}  ({time.time()-t0:.1f}s)")
ms = sorted(set(k[0] for k in cnt))
Ctot = {}; Clay = {}
print("    m   C_m(total)   C_m by interval count n (n:C)")
for mv in ms:
    L = lam(mv, Rphys)
    tot = sum(v for (mm, n), v in cnt.items() if mm == mv)/L
    Ctot[mv] = tot
    parts = {n: v/L for (mm, n), v in cnt.items() if mm == mv}
    for n, c in parts.items(): Clay[(mv, n)] = c
    print(f"   {mv:3d}  {tot:9.4f}   " + "  ".join(f"{n}:{c:.4f}" for n, c in sorted(parts.items())))
avg = np.mean([Ctot.get(mv, 0.0) for mv in range(1, M+1)])
print(f"    mean of C_m over m=1..{M}: {avg:.4f}   (Siegel average = rho = 1/sqrt7 = {1/np.sqrt(7):.4f})")
# ---------- (4) mean link kernel and BD-weighted layer kernel ----------
def layer_C(n): return {mv: Clay.get((mv, n), 0.0) for mv in ms}
link = layer_C(0)
W = sum(link.values()); m1 = sum(c*mv for mv, c in link.items()); m2 = sum(c*mv**2 for mv, c in link.items())
rho = 1/np.sqrt(7)
WP = np.sqrt(6*rho)       # Poisson link weight int rho exp(-rho pi s^2/24) ds
m1P = rho*24/(rho*np.pi)  # int s rho e^{-a s^2} ds = rho/(2a), a = rho pi/24
print(f"[4] mean LINK kernel: sum_m C^link_m theta delta(x^2+m), support m in {sorted(mv for mv,c in link.items() if c>0)}")
print(f"    W_LRL = sum C^link = {W:.4f};  <m>_link = {m1/W:.3f};  <m^2>_link = {m2/W:.3f}")
print(f"    Poisson comparator at same rho: W_P = sqrt(6 rho) = {WP:.4f}; <s>_P = {m1P/WP:.3f}")
print(f"    max link tau^2 found: {max(mv for mv,c in link.items() if c>0)}  (all v0=1 vectors are links: m=7-|n|^2 in 1..7)")
from scipy.special import k1
print("    FT (spacelike k): F(k) = sum C (2 pi sqrt m/k) K1(k sqrt m);  ratio to massless 2 pi W/k^2:")
for k in [1e-3, 1e-2, 0.1, 0.3, 1.0]:
    F = sum(c*2*np.pi*np.sqrt(mv)/k*k1(k*np.sqrt(mv)) for mv, c in link.items())
    sgrid = np.linspace(1e-6, 40, 400001)
    FP = np.trapezoid(rho*np.exp(-rho*np.pi*sgrid**2/24)*2*np.pi*np.sqrt(sgrid)/k*k1(k*np.sqrt(sgrid)), sgrid)
    print(f"      k={k:6.3f}: LRL F/(2piW/k^2) = {F/(2*np.pi*W/k**2):.6f}   Poisson F/(2piW_P/k^2) = {FP/(2*np.pi*WP/k**2):.6f}")
# BD 4D layer weights (Poisson-designed): link, 1-, 2-, 3-element intervals with (1,-9,16,-8)
wBD = {0: 1, 1: -9, 2: 16, 3: -8}
CBD = {mv: sum(wBD[n]*Clay.get((mv, n), 0.0) for n in wBD) for mv in ms}
mom = [sum(c*mv**j for mv, c in CBD.items()) for j in range(3)]
momlog = sum(c*mv*np.log(mv) for mv, c in CBD.items() if c != 0)
print(f"[5] BD-weighted layer sum on LRL: sum C = {mom[0]:.4f} (must be 0 to kill 1/k^2), sum C m = {mom[1]:.4f} (0 to kill ln k),"
      f" sum C m ln m = {momlog:.4f}")
nmax_m = {n: max([mv for (mv, nn) in Clay if nn == n] or [0]) for n in range(4)}
print(f"    largest tau^2 in layers n=0..3: {nmax_m}")
print(f"    Poisson BD (comparator) satisfies the analogous moment conditions by design; on LRL they fail -> mean of the Poisson-tuned")
print(f"    operator is not a d'Alembertian (leading 1/k^2 term survives with weight {mom[0]:.4f}).")
print(f"total time {time.time()-t0:.1f}s")
