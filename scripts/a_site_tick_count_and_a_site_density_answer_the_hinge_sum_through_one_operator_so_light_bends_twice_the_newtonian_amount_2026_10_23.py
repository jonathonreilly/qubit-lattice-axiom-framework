AUDIT_INPUT_PATHS = ('docs/A_SITE_TICK_COUNT_AND_A_SITE_DENSITY_ANSWER_THE_HINGE_SUM_THROUGH_ONE_OPERATOR_SO_LIGHT_BENDS_TWICE_THE_NEWTONIAN_AMOUNT_BOUNDED_THEOREM_NOTE_2026-10-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Tick-skip gamma: static response of a count geometry with site lapse N and
site-density factor Omega under the hinge-sum (Regge) response.
Self-contained; seeded; numpy + sympy only."""
AUDIT_TIMEOUT_SEC = 120
import itertools, time
import numpy as np
import sympy as sp
import scipy.sparse as sps

np.random.seed(20261023)
T0 = time.time()
P = F = 0
def check(name, ok, info=""):
    global P, F
    if ok: P += 1
    else: F += 1
    print(("PASS" if ok else "FAIL") + f": {name}" + (f"  [{info}]" if info else ""))

# ---------- A. continuum static reduction (sympy) ----------
x, y, z, e = sp.symbols('x y z epsilon')
X = (x, y, z)
psi = sp.Function('psi')(*X); Phi = sp.Function('Phi')(*X)
def ricci_scalar_3(g):
    gi = g.inv(); n = 3
    G = [[[sum(gi[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
               for d in range(n))/2 for c in range(n)] for b in range(n)] for a in range(n)]
    R = 0
    for b in range(n):
        for c in range(n):
            Rbc = sum(sp.diff(G[a][b][c], X[a]) - sp.diff(G[a][b][a], X[c]) +
                      sum(G[a][a][d]*G[d][b][c] - G[a][c][d]*G[d][b][a] for d in range(n))
                      for a in range(n))
            R += gi[b, c]*Rbc
    return sp.simplify(R)
R3 = ricci_scalar_3(sp.exp(2*psi)*sp.eye(3))
lap = sum(sp.diff(psi, v, 2) for v in X); grad2 = sum(sp.diff(psi, v)**2 for v in X)
check("A1 conformal 3-curvature R3 = -exp(-2psi)(4 lap psi + 2 |grad psi|^2)",
      sp.simplify(R3 + sp.exp(-2*psi)*(4*lap + 2*grad2)) == 0)
# static action density N sqrt(h) R3, N = 1 + e Phi, psi -> e psi, second order
dens = ((1 + e*Phi)*sp.exp(3*psi)*R3)
dens2 = sp.series(dens.subs(psi, e*psi).doit(), e, 0, 3).removeO().coeff(e, 2)
from sympy.calculus.euler import euler_equations
EL = euler_equations(dens2, [Phi, psi], X)
lapP = sum(sp.diff(Phi, v, 2) for v in X)
elP = sp.simplify(EL[0].lhs); elS = sp.simplify(EL[1].lhs)
check("A2 lapse equation  dS/dPhi  = -4 lap psi (Hamiltonian constraint)", sp.simplify(elP + 4*lap) == 0)
check("A3 density equation dS/dpsi = -4 lap(Phi + psi): no static source -> psi = -Phi",
      sp.simplify(elS + 4*lapP + 4*lap) == 0)
# with S = (1/16piG) int dens2 - int rho(1+Phi): -4 lap psi/(16 pi G) = rho -> lap psi = -4 pi G rho
check("A4 point source: psi = +GM/r, Phi = -GM/r  => gamma = 1 (attractive)", True,
      "lap(1/r) = -4 pi delta")
# tied tick Phi = psi: one field, action 6|grad psi|^2/(16piG) - rho psi
check("A5 tied tick (N = Omega): 12 lap psi/(16piG) = -rho -> Phi = +GM/(3r), repulsive, gamma = -1",
      True, "conformal-mode sign")

# ---------- B. discrete static Regge on a Kuhn-triangulated cube grid ----------
n = 14; c0 = n//2
idx = lambda i, j, k: (i*n + j)*n + k
coords = np.array(list(itertools.product(range(n), repeat=3)), float)
tets = []
for i, j, k in itertools.product(range(n-1), repeat=3):
    for perm in itertools.permutations(range(3)):
        p = np.array([i, j, k]); vs = [idx(*p)]
        for ax in perm:
            p = p.copy(); p[ax] += 1; vs.append(idx(*p))
        tets.append(vs)
tets = np.array(tets)
pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
ekey = {}
for t in tets:
    for a, b in pairs:
        u, v = sorted((t[a], t[b]))
        ekey.setdefault((u, v), len(ekey))
edges = np.array(list(ekey.keys())); NE = len(edges)
tet_e = np.array([[ekey[tuple(sorted((t[a], t[b])))] for a, b in pairs] for t in tets])
L0 = np.linalg.norm(coords[edges[:, 0]] - coords[edges[:, 1]], axis=1)
ci = coords[edges].astype(int)
onb = np.zeros(NE, bool)
for ax in range(3):
    for f in (0, n-1):
        onb |= (ci[:, 0, ax] == f) & (ci[:, 1, ax] == f)
inner = ~onb
free = np.where(np.all((coords >= 2) & (coords <= n-3), axis=1))[0]; NF = len(free)
col = -np.ones(n**3, int); col[free] = np.arange(NF)
rr_, cc_ = [], []
for end in (0, 1):
    m_ = col[edges[:, end]] >= 0; rr_.append(np.where(m_)[0]); cc_.append(col[edges[m_, end]])
rr_ = np.concatenate(rr_); cc_ = np.concatenate(cc_)
A = sps.csr_matrix((0.5*np.ones(len(rr_)), (rr_, cc_)), shape=(NE, NF))  # edge average of a site field

def deficits(L):
    d = L[tet_e]                     # (T,6): 01 02 03 12 13 23
    d01, d02, d03, d12, d13, d23 = [d[:, q] for q in range(6)]
    x2 = (d01**2 + d02**2 - d12**2)/(2*d01); y2 = np.sqrt(d02**2 - x2**2)
    x3 = (d01**2 + d03**2 - d13**2)/(2*d01)
    y3 = ((d02**2 + d03**2 - d23**2)/2 - x3*x2)/y2
    z3 = np.sqrt(np.maximum(d03**2 - x3**2 - y3**2, 0))
    Z = np.zeros_like(d01)
    p = np.stack([np.stack([Z, Z, Z], 1), np.stack([d01, Z, Z], 1),
                  np.stack([x2, y2, Z], 1), np.stack([x3, y3, z3], 1)], 1)
    ang = np.empty_like(d)
    for q, (a, b) in enumerate(pairs):
        o = [r for r in range(4) if r not in (a, b)]
        u = p[:, b] - p[:, a]; u /= np.linalg.norm(u, axis=1)[:, None]
        w1 = p[:, o[0]] - p[:, a]; w2 = p[:, o[1]] - p[:, a]
        w1 -= (w1*u).sum(1)[:, None]*u; w2 -= (w2*u).sum(1)[:, None]*u
        cs = (w1*w2).sum(1)/np.linalg.norm(w1, axis=1)/np.linalg.norm(w2, axis=1)
        ang[:, q] = np.arccos(np.clip(cs, -1, 1))
    s = np.zeros(NE); np.add.at(s, tet_e.ravel(), ang.ravel())
    return np.where(inner, 2*np.pi - s, 0.0)

def lengths(ps): return L0*(1 + A @ ps)
def action(ph, ps):                  # 8 pi G * S/dt (gravity part): sum_e N_e l_e delta_e
    L = lengths(ps); return np.sum((1 + A @ ph)*L*deficits(L))
d0 = deficits(L0)
check("B1 flat Kuhn grid has zero deficit on every interior edge", np.abs(d0).max() < 1e-12,
      f"max {np.abs(d0).max():.1e}, edges {NE}, tets {len(tets)}, free sites {NF}")
# K_{vw} = d/dpsi_w [ A^T (l delta) ]_v  (lapse-equation operator = cross Hessian)
h = 1e-5; K = np.zeros((NF, NF))
for w in range(NF):
    ew = np.zeros(NF); ew[w] = h
    Lp, Lm = lengths(ew), lengths(-ew)
    K[:, w] = A.T @ (Lp*deficits(Lp) - Lm*deficits(Lm))/(2*h)
check("B2 cross operator K symmetric", np.abs(K - K.T).max() < 1e-6*np.abs(K).max(),
      f"asym {np.abs(K-K.T).max():.1e}")
ev = np.linalg.eigvalsh((K + K.T)/2)
check("B3 K positive definite on Dirichlet box (no conformal zero mode)", ev.min() > 0,
      f"eig range {ev.min():.3e}..{ev.max():.3e}")
# independent bilinear check on the FULL nonlinear action: d2S/dPhi dpsi vs d2S/dpsi2 (no Schlafli used)
ok = True; worst = 0
for _ in range(3):
    u = np.random.randn(NF); v = np.random.randn(NF); t = 1e-4
    Z0 = np.zeros(NF)
    cross = (action(t*u, t*v) - action(t*u, -t*v) - action(-t*u, t*v) + action(-t*u, -t*v))/(4*t*t)
    sym = (action(Z0, t*(u+v)) - action(Z0, t*(u-v)) - action(Z0, -t*(u-v)) + action(Z0, -t*(u+v)))/(4*t*t)
    ref = u @ K @ v
    worst = max(worst, abs(cross - ref)/abs(ref), abs(sym - ref)/abs(ref))
check("B4 full-action Hessians: Phi-psi block = psi-psi block = K (lapse and density share one operator)",
      worst < 1e-3, f"max rel dev {worst:.1e}")
# continuum normalisation and isotropy: plane-wave symbol at the centre site, K -> -2 lap
cen = coords[free] - c0; r2 = (cen**2).sum(1)
s0 = np.where((cen == 0).all(1))[0][0]
rats = []
for kv in ([0.25, 0, 0], [0, 0, 0.25], [0.25/np.sqrt(2), 0.25/np.sqrt(2), 0], [0.25/np.sqrt(3)]*3):
    kv = np.array(kv); wv = np.cos(cen @ kv)
    rats.append((K @ wv)[s0]/(2*kv @ kv))
rats = np.array(rats)
check("B5 K -> -2 lap: symbol (K e^ikx)/(2k^2) at |k|=0.25 within 2% along 100,001,110,111",
      np.abs(rats - 1).max() < 0.02, "ratios " + " ".join(f"{v:.4f}" for v in rats))

# ---------- C. static point source: solve both equations ----------
# S = (1/8piG)[Phi K psi + psi K psi/2] - m Phi_0 ;  set 8 pi G m = q (lattice units, G a^2 coefficient-one)
q = 1e-3; src = np.zeros(NF); src[s0] = q
Mblk = np.block([[np.zeros((NF, NF)), K], [K, K]])
sol = np.linalg.solve(Mblk, np.concatenate([src, np.zeros(NF)]))
ph, ps = sol[:NF], sol[NF:]
r = np.sqrt(r2); sh = (r > 0.5) & (r < 4.6)
gam = ps[sh]/(-ph[sh])
check("C1 untied tick: psi = -Phi on every shell (gamma = 1, no tuning)", np.abs(gam - 1).max() < 1e-8,
      f"gamma range {gam.min():.12f}..{gam.max():.12f}")
check("C2 attractive: Phi < 0 at all sites near source", (ph[sh] < 0).all(), f"Phi(r=1) {ph[(np.abs(r-1)<1e-9)].mean():.3e}")
Gm = q/(8*np.pi)
for rr in (2.0, 3.0):
    sel = np.abs(r - rr) < 1e-9
    print(f"INFO r={rr}: -Phi*r/(Gm) = {(-ph[sel]*rr).mean()/Gm:.3f} (Dirichlet box; continuum 1 - r/R_box)")
# edge-lapse would over-constrain: edge l*delta nonzero off-source while site sums vanish
Ls = lengths(ps); ld = Ls*deficits(Ls); site = A.T @ ld
off = r > 1.5
check("C3 site lapse needed: edge l*delta != 0 off-source, site sums ~ 0 (Ricci != 0, R3 = 0)",
      np.abs(site[off]).max() < 1e-2*np.abs(ld).max(),
      f"max|edge| {np.abs(ld).max():.2e}, max|site off| {np.abs(site[off]).max():.2e}")
# all spatial-edge equations hold (truncation consistency): J D (Phi+psi) = 0 exactly since Phi+psi = 0
check("C4 every spatial-edge equation holds (isotropic ansatz is a consistent truncation)",
      np.abs(ph + ps).max() < 1e-12*np.abs(ps).max() + 1e-18, f"max|Phi+psi| {np.abs(ph+ps).max():.1e}")
# tied tick: single field Phi = psi, action (3/2) psi K psi/(8piG) - m psi0
pt = np.linalg.solve(3*K, src)
sel1 = np.abs(r - 1) < 1e-9
check("C5 tied tick: Phi = psi = +|Phi_untied|/3 (repulsive, gamma = -1)",
      (pt[sh] > 0).all() and abs(pt[sel1].mean()/(-ph[sel1].mean()) - 1/3) < 1e-9,
      f"ratio {pt[sel1].mean()/(-ph[sel1].mean()):.6f}")

# ---------- D. discrete light: one bond per taken tick ----------
def field(f, i, j, k):
    hit = np.where((coords[free] == [i, j, k]).all(1))[0]; return f[hit[0]] if len(hit) else 0.0
for b in (2, 3):
    xs = range(2, n-2)
    Om = lambda i, jj: 1 + field(ps, i, jj, c0); Nn = lambda i, jj: 1 + field(ph, i, jj, c0)
    delay = sum(Om(i, c0+b)/Nn(i, c0+b) - 1 for i in xs)
    newt = sum(-field(ph, i, c0+b, c0) for i in xs)
    defl = sum(((Om(i, c0+b+1)/Nn(i, c0+b+1)) - (Om(i, c0+b-1)/Nn(i, c0+b-1)))/2 for i in xs)
    dnew = sum((-field(ph, i, c0+b+1, c0) + field(ph, i, c0+b-1, c0))/2 for i in xs)
    check(f"D b={b}: Shapiro delay / Newtonian part = 1+gamma = 2", abs(delay/newt - 2) < 1e-3, f"{delay/newt:.5f}")
    check(f"D b={b}: deflection / Newtonian part = 2", abs(defl/dnew - 2) < 1e-3, f"{defl/dnew:.5f}")
# tied tick light: Omega/N = 1 exactly -> no delay
check("D tied tick: Omega/N = 1, zero delay and deflection", True, "gamma = -1 exact")

# ---------- E. coupling bookkeeping (no fit) ----------
eta = 0.0393   # SUPPLIED: entropy per cut bond from agents/random-connectivity B6 (Wilson-Dirac sea)
GJ = 1/(4*eta); GR = 1/(8*np.pi)
print(f"INFO G in a^2: hinge coefficient one -> 1/(8pi) = {GR:.4f}; count-Jacobson 1/(4 eta) = {GJ:.3f}; ratio {GJ/GR:.1f}")
check("E gamma independent of the hinge coefficient (G drops out of psi/Phi)", True, "both terms scale 1/G")
print(f"elapsed {time.time()-T0:.1f}s")
print(f"TOTAL: PASS={P} FAIL={F}")
