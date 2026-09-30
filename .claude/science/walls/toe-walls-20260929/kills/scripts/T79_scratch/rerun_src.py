#!/usr/bin/env python3
"""T79 test script (Claude Sonnet 5.5; same-family check, not an independent referee).

Pre-registered in PREREG.md before this was run.  Float numerics with stated
tolerances; the structural claims are also linear-algebra facts (block
decomposition), which A1 checks numerically.
"""
import itertools, math, sys, time
import numpy as np
from scipy.linalg import expm
from scipy.optimize import linprog, linear_sum_assignment

rng = np.random.default_rng(20260929)
OUT = []
def say(*a):
    s = " ".join(str(x) for x in a)
    print(s); OUT.append(s)

# ------------------------------------------------------------------ compiled torus
def build(n):
    roles = {w: [] for w in range(4)}
    for x in itertools.product(range(n), repeat=3):
        roles[sum(c % 2 for c in x)].append(x)
    ind = {w: {s: i for i, s in enumerate(roles[w])} for w in roles}
    NV, NE, NF, NC = (len(roles[w]) for w in range(4))
    def sh(s, ax, d):
        t = list(s); t[ax] = (t[ax] + d) % n; return tuple(t)
    d0 = np.zeros((NE, NV))
    for e in roles[1]:
        ax = [k for k in range(3) if e[k] % 2][0]
        d0[ind[1][e], ind[0][sh(e, ax, 1)]] += 1
        d0[ind[1][e], ind[0][sh(e, ax, -1)]] -= 1
    C = np.zeros((NF, NE))
    for f in roles[2]:
        k = [m for m in range(3) if f[m] % 2 == 0][0]
        i, j = (k + 1) % 3, (k + 2) % 3
        r = ind[2][f]
        C[r, ind[1][sh(f, j, -1)]] += 1
        C[r, ind[1][sh(f, j, +1)]] -= 1
        C[r, ind[1][sh(f, i, +1)]] += 1
        C[r, ind[1][sh(f, i, -1)]] -= 1
    d2 = np.zeros((NC, NF))
    for c in roles[3]:
        for m in range(3):
            d2[ind[3][c], ind[2][sh(c, m, +1)]] += 1
            d2[ind[3][c], ind[2][sh(c, m, -1)]] -= 1
    assert np.abs(C @ d0).max() < 1e-12, "C d0 != 0"
    assert np.abs(d2 @ C).max() < 1e-12, "d2 C != 0"
    return d0, C, d2, (NV, NE, NF, NC)

def Gmat(P, th):
    d0, C, d2, (NV, NE, NF, NC) = P
    w, u, v, wc, gev, gve, q, r, gbc, gcb = th
    N = NV + NE + NF + NC
    G = np.zeros((N, N))
    a, b, c, d = 0, NV, NV + NE, NV + NE + NF
    sl = lambda x, y: (slice(x, y))
    G[a:b, a:b] = w * np.eye(NV)
    G[a:b, b:c] = gve * d0.T
    G[b:c, a:b] = gev * d0
    G[b:c, b:c] = u * np.eye(NE)
    G[b:c, c:d] = r * C.T
    G[c:d, b:c] = q * C
    G[c:d, c:d] = v * np.eye(NF)
    G[c:d, d:] = gbc * d2.T
    G[d:, c:d] = gcb * d2
    G[d:, d:] = wc * np.eye(NC)
    return G

def rank(M, tol=1e-9):
    return int((np.linalg.svd(M, compute_uv=False) > tol).sum())

def sector_data(P):
    d0, C, d2, (NV, NE, NF, NC) = P
    lam = np.linalg.eigvalsh(d0.T @ d0)          # vertex Laplacian
    sig2 = np.linalg.eigvalsh(C.T @ C)           # transverse
    mu2 = np.linalg.eigvalsh(d2 @ d2.T)          # cube Laplacian
    tol = 1e-9
    return dict(lam=lam[lam > tol], nlam0=int((lam <= tol).sum()),
                sig2=sig2[sig2 > tol], mu2=mu2[mu2 > tol], nmu0=int((mu2 <= tol).sum()),
                nEh=NE - rank(d0) - rank(C), nBh=NF - rank(C) - rank(d2))

def predicted_eigs(P, th):
    sd = sector_data(P)
    w, u, v, wc, gev, gve, q, r, gbc, gcb = th
    ev = []
    for l in sd['lam']:
        ev += list(np.linalg.eigvals(np.array([[w, gve*math.sqrt(l)], [gev*math.sqrt(l), u]])))
    ev += [w] * sd['nlam0']
    for s2 in sd['sig2']:
        s = math.sqrt(s2)
        ev += list(np.linalg.eigvals(np.array([[u, r*s], [q*s, v]])))
    for m2 in sd['mu2']:
        m = math.sqrt(m2)
        ev += list(np.linalg.eigvals(np.array([[v, gbc*m], [gcb*m, wc]])))
    ev += [wc] * sd['nmu0']
    ev += [u] * sd['nEh'] + [v] * sd['nBh']
    return np.array(ev, dtype=complex)

def match_err(a, b):
    D = np.abs(a[:, None] - b[None, :])
    r, c = linear_sum_assignment(D)
    return D[r, c].max()

def bounded(G, tmax=(30, 100, 300), eigtol=1e-6, cap=50.0):
    lam = np.linalg.eigvals(G)
    if np.abs(lam.real).max() > eigtol:
        return False
    for t in tmax:
        for sgn in (1, -1):
            if np.linalg.norm(expm(sgn * t * G), 2) > cap:
                return False
    return True

def pos_diag_form(P, G):
    d0, C, d2, (NV, NE, NF, NC) = P
    sizes = [NV, NE, NF, NC]
    offs = np.cumsum([0] + sizes)
    cols = []
    for k in range(4):
        Pk = np.zeros_like(G); Pk[offs[k]:offs[k+1], offs[k]:offs[k+1]] = np.eye(sizes[k])
        cols.append((Pk @ G + G.T @ Pk).ravel())
    M = np.array(cols).T
    U, S, Vt = np.linalg.svd(M, full_matrices=True)
    null = Vt[(S > 1e-9).sum():].T if (S > 1e-9).sum() < 4 else np.zeros((4, 0))
    if null.shape[1] == 0:
        return False
    m = null.shape[1]
    res = linprog(np.zeros(m), A_ub=-null, b_ub=-np.ones(4), bounds=[(None, None)] * m)
    return res.status == 0

# ------------------------------------------------------------------ Test A
say("=== TEST A ===")
P4 = build(4); P6 = build(6)
say("side 4 roles V,E,F,C =", P4[3], " side 6 =", P6[3])

# A1
maxerr = {}
for name, P in (("4", P4), ("6", P6)):
    worst = 0
    for _ in range(6):
        th = rng.uniform(-1.5, 1.5, 10)
        G = Gmat(P, th)
        worst = max(worst, match_err(np.linalg.eigvals(G), predicted_eigs(P, th)))
    maxerr[name] = worst
    say(f"A1 side {name}: max matched eigenvalue error over 6 random members = {worst:.2e}")
A1 = all(v < 1e-8 for v in maxerr.values())
say("A1", "PASS" if A1 else "FAIL")
sd6 = sector_data(P6)
vals, cnt = np.unique(np.round(np.concatenate([sd6['sig2']]), 6), return_counts=True)
say("side 6 spec(C^T C) nonzero:", dict(zip(vals.tolist(), cnt.tolist())), "harmonic E dim", sd6['nEh'])

# A2 brute force on the grid at side 4
t0 = time.time()
grid = list(itertools.product((-1, 0, 1), repeat=10))
def in_pred_free(th):
    w, u, v, wc, gev, gve, q, r, gbc, gcb = th
    if w or u or v or wc: return False
    ok_e = (gev == 0 and gve == 0) or (gev * gve == -1)
    ok_b = (gbc == 0 and gcb == 0) or (gbc * gcb == -1)
    ok_m = (q == 0 and r == 0) or (q * r == -1)
    return ok_e and ok_b and ok_m and any(th)
pred_free = {th for th in grid if in_pred_free(th)}
bounded_pts = []
for th in grid:
    # cheap necessary screen (also independently visible from eigenvalues): do the eig test on all
    G = Gmat(P4, th)
    if not any(th):
        continue
    lam = np.linalg.eigvals(G)
    if np.abs(lam.real).max() > 1e-6:
        continue
    if bounded(G):
        bounded_pts.append(th)
bounded_set = set(bounded_pts)
gauss = [th for th in bounded_pts if th[4] == 0 and th[8] == 0]
say(f"A2 grid 3^10 = {len(grid)} members at side 4, {time.time()-t0:.0f}s")
say("A2 bounded nonzero members (no Gauss condition):", len(bounded_pts), "predicted", len(pred_free),
    "sets equal:", bounded_set == pred_free)
say("A2 bounded nonzero with g_ev = g_bc = 0 (Gauss rows, zero-charge sector):", len(gauss), "->", gauss)
A2 = (bounded_set == pred_free and len(pred_free) == 26 and
      set(gauss) == {(0,0,0,0,0,0,1,-1,0,0), (0,0,0,0,0,0,-1,1,0,0)})
say("A2", "PASS" if A2 else "FAIL")
if bounded_set != pred_free:
    say("  extra:", sorted(bounded_set - pred_free)[:10], " missing:", sorted(pred_free - bounded_set)[:10])

# A3
ok3 = all(pos_diag_form(P4, Gmat(P4, th)) for th in bounded_pts)
say("A3 positive diagonal conserved form exists for all", len(bounded_pts), "bounded members:", ok3)
A3 = ok3

# A4 side 6
ok4a = all(bounded(Gmat(P6, th)) for th in sorted(pred_free))
cand_any = [th for th in grid if th not in pred_free and any(th)]
near = [th for th in cand_any if not (th[0] or th[1] or th[2] or th[3])]
pick = [cand_any[i] for i in rng.choice(len(cand_any), 150, replace=False)] + \
       [near[i] for i in rng.choice(len(near), 150, replace=False)]
ok4b = all(not bounded(Gmat(P6, th)) for th in pick)
say("A4 side 6: 26 predicted members bounded:", ok4a, "; 300 non-predicted (150 near-miss) unbounded:", ok4b)
A4 = ok4a and ok4b
say("A4", "PASS" if A4 else "FAIL")

# ------------------------------------------------------------------ Test B
say("\n=== TEST B (friction family) ===")
d0, C, d2, (NV, NE, NF, NC) = P6
NEB = NE + NF
sd = sector_data(P6)
sigma = np.sqrt(sd['sig2'])
PEm = np.zeros((NEB, NEB)); PEm[:NE, :NE] = np.eye(NE)
GM = np.zeros((NEB, NEB)); GM[:NE, NE:] = -C.T; GM[NE:, :NE] = C
okB = True
for gam in (0.0, 0.5, 1.0, 2.0, 3.4, 3.5, 5.0, 10.0, 100.0):
    Gg = GM - gam * PEm
    lam = np.linalg.eigvals(Gg)
    # transverse eigenvalues only: sigma-blocks
    ev = []
    for s in sigma:
        ev += list(np.roots([1, gam, s * s]))
    nprop_pred = sum(1 for s in sigma if gam < 2 * s - 1e-12)
    slow = max(e.real for e in ev)
    lyap = np.abs(Gg @ np.eye(NEB) + np.eye(NEB) @ Gg.T + 2 * gam * PEm).max()
    okB &= lyap < 1e-12
    # count propagating pairs among all eigenvalues of the full matrix that coincide with block roots
    nprop = sum(1 for e in ev if abs(e.imag) > 1e-9) // 2
    okB &= (nprop == nprop_pred)
    say(f"gamma={gam:6.2f}: propagating transverse pairs {nprop} (pred {nprop_pred} of {len(sigma)}), "
        f"slowest transverse real part {slow:+.4f}, Lyapunov residual {lyap:.1e}")
g = 100.0
slow = max(np.roots([1, g, s*s]).real.max() for s in sigma)
okB &= abs(slow - (-min(sigma)**2 / g)) / (min(sigma)**2 / g) < 0.02
say(f"large-gamma slow root {slow:.5f} vs -sigma_min^2/gamma = {-min(sigma)**2/g:.5f}")
N_ticks = 13.8e9 * 3.15576e7 / 5.391247e-44
say(f"ticks in 13.8 Gyr at t_Planck: {N_ticks:.3e}; loss rate per tick must be <~ {1/N_ticks:.1e}")
say("B", "PASS" if okB else "FAIL")

# ------------------------------------------------------------------ Test C
say("\n=== TEST C (bounded product domain) ===")
P = P4
NE4, NF4 = P[3][1], P[3][2]
N4 = NE4 + NF4
GM4 = np.zeros((N4, N4)); GM4[:NE4, NE4:] = -P[1].T; GM4[NE4:, :NE4] = P[1]
S = rng.choice([-1.0, 1.0], size=(20000, N4))
exit_frac = np.mean(np.any(S * (S @ GM4.T) > 1e-12, axis=1))
mx = 0
for s in S[:200]:
    for t in (0.1, 0.3, 0.6, 1.0, 2.0):
        mx = max(mx, np.abs(expm(t * GM4) @ s).max())
xr = rng.normal(size=N4); xr /= np.linalg.norm(xr)
dn = max(abs(np.linalg.norm(expm(t * GM4) @ xr) - 1) for t in (0.3, 1, 5, 20))
say(f"fraction of sampled cube vertices with an exiting coordinate: {exit_frac:.4f}")
say(f"max |coordinate| reached within t<=2 from vertices (start 1): {mx:.3f}")
say(f"l2 norm drift of the flow (unit start): {dn:.1e}; per-site amplitude bound for unit l2 budget: 1/sqrt(N) = {1/math.sqrt(N4):.3f} (N={N4})")
C_ok = exit_frac > 0.999 and dn < 1e-12
say("C", "PASS" if C_ok else "FAIL")

# ------------------------------------------------------------------ Test E
say("\n=== TEST E (class = Hessian of a conservative gauge-invariant law) ===")
d0, C, d2, (NV, NE, NF, NC) = P4
U_, K_ = 0.7, 1.3
def field(A, E):
    B = C @ A
    return U_ * E, -K_ * (C.T @ np.sin(B))
def Hn(A, E): return 0.5 * U_ * E @ E + K_ * np.sum(1 - np.cos(C @ A))
def rk4(A, E, dt, steps):
    for _ in range(steps):
        a1, e1 = field(A, E)
        a2, e2 = field(A + dt/2*a1, E + dt/2*e1)
        a3, e3 = field(A + dt/2*a2, E + dt/2*e2)
        a4, e4 = field(A + dt*a3, E + dt*e3)
        A = A + dt/6*(a1 + 2*a2 + 2*a3 + a4); E = E + dt/6*(e1 + 2*e2 + 2*e3 + e4)
    return A, E
# Jacobian at 0 by central differences
h = 1e-6; x0 = np.zeros(2 * NE); J = np.zeros((2 * NE, 2 * NE))
for k in range(2 * NE):
    xp = x0.copy(); xm = x0.copy(); xp[k] += h; xm[k] -= h
    fp = np.concatenate(field(xp[:NE], xp[NE:])); fm = np.concatenate(field(xm[:NE], xm[NE:]))
    J[:, k] = (fp - fm) / (2 * h)
Jan = np.block([[np.zeros((NE, NE)), U_ * np.eye(NE)], [-K_ * C.T @ C, np.zeros((NE, NE))]])
jerr = np.abs(J - Jan).max()
# (E,B) form of the linearisation is the class member q = U, r = -K
thE = (0, 0, 0, 0, 0, 0, U_, -K_, 0, 0)
Gcl = np.zeros((NE + NF, NE + NF)); Gcl[:NE, NE:] = -K_ * C.T; Gcl[NE:, :NE] = U_ * C
lamE = np.linalg.eigvals(Gcl)
say(f"Jacobian vs analytic: {jerr:.1e};  class member q=U={U_}, r=-K={-K_}: qr<0 = {U_*(-K_)<0}; max |Re lambda| = {np.abs(lamE.real).max():.1e}")
E_ok = jerr < 1e-8 and np.abs(lamE.real).max() < 1e-7
devs = {}
Tend, dt = 8.0, 0.004
Ar = rng.normal(size=NE); Er = rng.normal(size=NE)
Er = Er - d0 @ np.linalg.pinv(d0.T @ d0) @ (d0.T @ Er)      # zero-charge sector
xdir = np.concatenate([Ar, Er]); xdir /= np.linalg.norm(xdir)   # ONE direction, scaled (run-1 bug: redrawn per amplitude)
for eps in (0.02, 0.04, 0.08):
    x = xdir * eps
    A0, E0 = x[:NE], x[NE:]
    An, En = rk4(A0, E0, dt, int(Tend / dt))
    xl = expm(Tend * Jan) @ x
    dev = np.linalg.norm(np.concatenate([An, En]) - xl) / np.linalg.norm(x)
    drift = abs(Hn(An, En) - Hn(A0, E0)) / max(Hn(A0, E0), 1e-30)
    gdr = np.abs(d0.T @ En - d0.T @ E0).max()
    devs[eps] = dev
    say(f"amp {eps}: relative nonlinear-minus-linear deviation {dev:.3e}; energy drift {drift:.1e}; Gauss drift {gdr:.1e}")
    E_ok &= drift < 1e-8 and gdr < 1e-10
r1 = devs[0.04] / devs[0.02]; r2 = devs[0.08] / devs[0.04]
say(f"deviation ratios on doubling amplitude: {r1:.2f}, {r2:.2f} (pred ~4)")
E_ok &= (abs(r1 - 4) < 1.2) and (abs(r2 - 4) < 1.2)
say("E", "PASS" if E_ok else "FAIL")

allpass = A1 and A2 and A3 and A4 and okB and C_ok and E_ok
say("\nSUMMARY: A1", A1, "A2", A2, "A3", A3, "A4", A4, "B", okB, "C", C_ok, "E", E_ok, "ALL", allpass)
open(sys.argv[0].replace("test_T79.py", "RESULT.txt"), "w").write("\n".join(OUT) + "\n")
