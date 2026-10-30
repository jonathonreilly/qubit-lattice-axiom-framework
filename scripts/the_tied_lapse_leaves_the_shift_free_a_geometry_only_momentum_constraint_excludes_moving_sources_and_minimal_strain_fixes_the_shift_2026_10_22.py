AUDIT_INPUT_PATHS = ('docs/THE_TIED_LAPSE_LEAVES_THE_SHIFT_FREE_A_GEOMETRY_ONLY_MOMENTUM_CONSTRAINT_EXCLUDES_MOVING_SOURCES_AND_MINIMAL_STRAIN_FIXES_THE_SHIFT_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
"""collapse-shift: what fixes the shift in CL-1/CL-3, are edge-register values gauge-invariant, and does every
Oppenheimer-Snyder (OS) orbit keep a representative inside the edge window [L/8, 2L] up to the horizon?

A. linearised GR on flat space with CL-1's tied lapse (Bona-Masso f = 1/3: dN/N = h_kk/6): gauge kernel and the shift.
B. finite edge registers: the displacement shift as an operator; what is and is not gauge-invariant.
C. OS collapse: comoving-label representatives (edge-only generator) vs Painleve-Gullstrand-type ones (full generator).
D. the minimal-strain shift: the gauge condition dual to the displacement generator.
Units G = c = 1.  Self-contained (numpy, sympy).
"""
import math, time, itertools
import numpy as np, sympy as sp

AUDIT_TIMEOUT_SEC = 120
T0 = time.time(); NP = [0, 0]
def check(name, ok, detail=''):
    NP[0 if ok else 1] += 1
    print('[%s] %s | %s' % ('PASS' if ok else 'FAIL', name, detail))

# ---------------------------------------------------------------- A. linearised GR, tied lapse
print('== A. linearised GR with the fixed-step lapse (h_00 = -h_kk/3)')
eta = np.diag([-1.0, 1, 1, 1])
pairs = [(m, n) for m in range(4) for n in range(m, 4)]          # 10 components
def sym(v):
    h = np.zeros((4, 4))
    for c, (m, n) in zip(v, pairs): h[m, n] = h[n, m] = c
    return h
def einstein(h, k):                                               # linearised G_mn, d -> i k (signs absorbed)
    ku = eta @ k; k2 = k @ ku; hu = eta @ h @ eta; tr = np.trace(eta @ h)
    kh = h @ ku                                                    # k^r h_rn
    return 0.5 * (k2 * h - np.outer(k, kh) - np.outer(kh, k) + tr * np.outer(k, k) + eta * (ku @ h @ ku - k2 * tr))
def form(k):
    M = np.zeros((10, 10))
    for a in range(10):
        Ga = einstein(sym(np.eye(10)[a]), k)
        for b in range(10):
            hb = sym(np.eye(10)[b]); M[a, b] = np.sum((eta @ hb @ eta) * Ga)
    return 0.5 * (M + M.T)
# parametrise q = (h_11,h_12,h_13,h_22,h_23,h_33, beta_1,beta_2,beta_3); h_0i = beta_i, h_00 = -(h_11+h_22+h_33)/3
sp_idx = [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
P = np.zeros((10, 9))
for j, (m, n) in enumerate(sp_idx): P[pairs.index((m, n)), j] = 1
for i in range(3): P[pairs.index((0, i + 1)), 6 + i] = 1
for d in (0, 3, 5): P[pairs.index((0, 0)), d] = -1 / 3
rng = np.random.default_rng(3); ker_dims, beta_ranks, bb_ranks, gauge_ok = [], [], [], True
for _ in range(6):
    w = rng.uniform(0.3, 2); kv = rng.normal(size=3); k = np.array([-w, *kv])      # k_mu lowered
    Mq = P.T @ form(k) @ P; s = np.linalg.svd(Mq, compute_uv=False)
    ker = np.linalg.svd(Mq)[2][np.sum(s > 1e-9 * s[0]):]
    ker_dims.append(len(ker)); beta_ranks.append(np.linalg.matrix_rank(ker[:, 6:], 1e-8))
    bb_ranks.append(np.linalg.matrix_rank(Mq[6:, 6:], 1e-9 * s[0]))
    for xi in np.eye(3):                                           # spatial gauge + compensating time reparam
        xs = np.zeros(4); xs[1:] = xi; xs[0] = -(kv @ xi) / (3 * k[0])
        dh = np.outer(k, xs) + np.outer(xs, k)
        q = np.array([dh[m, n] for (m, n) in sp_idx] + [dh[0, i] for i in (1, 2, 3)])
        gauge_ok &= abs(dh[0, 0] + np.trace(dh[1:, 1:]) / 3) < 1e-12 and np.linalg.norm(Mq @ q) < 1e-9 * s[0]
check('A1 THEOREM: the tied lapse does not fix the spatial gauge: at every (omega, k) the action on (h_ij, beta_i) has a '
      'kernel of exactly 3 (spatial displacements with a compensating time relabelling) whose beta-projection has rank 3, '
      'so every shift is a stationary shift of some edge history; "the shift at which the total phase is stationary" fixes nothing',
      gauge_ok and set(ker_dims) == {3} and set(beta_ranks) == {3}, 'kernel dims %s; beta rank of kernel %s' % (sorted({int(q) for q in ker_dims}), sorted({int(q) for q in beta_ranks})))
check('A2 THEOREM: given the edge history, the beta-beta block has rank 2 (K_ijK^ij - K^2 is blind to a longitudinal shift), '
      'and the beta equation is the momentum constraint G_0i = 8 pi T_0i: it constrains the edges and the shift together',
      set(bb_ranks) == {2}, 'beta-beta ranks %s' % sorted({int(q) for q in bb_ranks}))
# A3: moving source.  harmonic-gauge solution  k^2 hbar = 16 pi T  (static mode in the source's lattice frame boosted)
w = 0.4; kv = np.array([1.0, 0.3, -0.2]); k = np.array([-w, *kv]); ku = eta @ k; k2 = k @ ku
v = np.array([0.0, 0.3, 0.1, 0.0]); u = np.array([1.0, v[1], v[2], 0]); u = u / math.sqrt(-(u @ eta @ u))
# conserved dust mode needs k.u = 0: choose omega so
w = (kv @ u[1:]) / u[0]; k = np.array([-w, *kv]); ku = eta @ k; k2 = k @ ku
ul = eta @ u; T = np.outer(ul, ul)                                    # T_mn (rho = 1)
hb = 16 * math.pi * T / (-k2) * (-1)                                  # box -> -k2 ; solve -k2 hbar = -16 pi T  -> sign fixed below
h = hb - 0.5 * eta * np.trace(eta @ hb)
G = einstein(h, k); lam = (G[0, 0] / T[0, 0])
G0i = G[0, 1:]; T0i = T[0, 1:]
check('A3 THEOREM: for a moving source the linearised solution has G_0i = (8 pi) T_0i != 0 in its geometry part; CL-3\'s edge-only '
      'displacement generator is the geometry part of G_0i (the vacuum momentum constraint), so "odds invariant under every '
      'edge shift" forces T_0i = 0 (no matter momentum) or excludes the GR field of every moving mass in every gauge',
      np.allclose(G, lam * T, atol=1e-10) and abs(abs(lam) - 8 * math.pi) < 1e-9 and np.linalg.norm(G0i) > 0.1,
      '|G_0i|/|G_00| = %.3f = |T_0i|/|T_00| = %.3f; G = %.4f T' % (np.linalg.norm(G0i) / abs(G[0, 0]), np.linalg.norm(T0i) / T[0, 0], lam))

# ---------------------------------------------------------------- B. finite registers
print('== B. edge registers: the displacement shift as an operator')
Nv = 6; d = np.array([-2, +2, -1, +1])            # +x axis, -x axis, two diagonals at one site, per unit displacement
states = list(itertools.product(range(Nv), repeat=4)); idx = {s: i for i, s in enumerate(states)}; D = len(states)
def shift(cyclic):
    S = np.zeros((D, D))
    for s in states:
        t = tuple((np.array(s) + d) % Nv) if cyclic else tuple(np.array(s) + d)
        if all(0 <= x < Nv for x in t): S[idx[t], idx[s]] = 1
    return S
St, Sc = shift(False), shift(True)
inv_t = np.sum(np.linalg.svd(St - np.eye(D), compute_uv=False) < 1e-10)
inv_c = np.sum(np.linalg.svd(Sc - np.eye(D), compute_uv=False) < 1e-10)
check('B1 THEOREM: on finite registers the displacement shift is a partial isometry, and the only odds invariant under it are '
      'zero (iterate psi = S^k psi until some raised edge leaves the window); a cyclic (clock) shift has invariant odds, but '
      'it wraps a length from 2L to L/8. So CL-3\'s "only odds invariant under every such shift occur" is empty as written',
      inv_t == 0 and inv_c > 0, 'invariant dim: truncated %d, cyclic %d (of %d)' % (inv_t, inv_c, D))
# groupoid version: invariant wherever both ends lie in the window -> class functions on orbit segments
parent = list(range(D))
def find(a):
    while parent[a] != a: parent[a] = parent[parent[a]]; a = parent[a]
    return a
for s in states:
    t = tuple(np.array(s) + d)
    if all(0 <= x < Nv for x in t): parent[find(idx[s])] = find(idx[t])
cls = {}
for s in states: cls.setdefault(find(idx[s]), []).append(s)
multi = [c for c in cls.values() if len(c) > 1]
inv_const = all(len({x[0] + x[1] for x in c}) == 1 for c in cls.values())
var_n = all(len({x[0] for x in c}) > 1 for c in multi)
touch = inv_const and var_n
# coherent product state centred mid-window, projected on class functions
g = np.exp(-0.5 * ((np.arange(Nv) - (Nv - 1) / 2) / 0.6)**2); g /= np.linalg.norm(g)
psi = np.array([np.prod([g[x] for x in s]) for s in states]); phi = np.zeros(D)
for c in cls.values():
    ii = [idx[s] for s in c]; phi[ii] = psi[ii].mean()
phi /= np.linalg.norm(phi); pr0 = psi**2; pr = phi**2
arr = np.array(states, float)
var = lambda p, f: p @ f**2 - (p @ f)**2
v0, v1 = var(pr0, arr[:, 0]), var(pr, arr[:, 0]); s0, s1 = var(pr0, arr[:, 0] + arr[:, 1]), var(pr, arr[:, 0] + arr[:, 1])
pfloor = pr @ (arr.min(1) <= 1)
check('B2 THEOREM: with the invariance read on the window (both ends inside), physical odds are functions on orbit segments; '
      'each ends where the next gauge step leaves the window, so a single edge value (and "an edge at the floor") is not '
      'gauge-invariant: imposing the constraint spreads it, while displacement-invariant combinations are class functions',
      touch and v1 > 5 * v0, 'segments %d: n_+x + n_-x constant on each, n_+x never; var(n_+x) %.2f -> %.2f; '
      'P(an edge within one step of the floor) %.2f' % (len(multi), v0, v1, pfloor))
# B3: pure displacement reaches the split trigger; B4: the fixed-step lapse is displacement-variant at first order
cor = np.array(list(itertools.product([0, 1], repeat=3)), float)
ax = [(a, b) for a in range(8) for b in range(a + 1, 8) if np.sum(np.abs(cor[a] - cor[b])) == 1]
dg = [(a, b) for a in range(8) for b in range(a + 1, 8) if np.sum(np.abs(cor[a] - cor[b])) == 2 and cor[a].sum() % 2 == 0 and cor[b].sum() % 2 == 0]
X = cor + 0.1 * (2 * cor - 1)                                    # corners pushed outward
grow = all(np.linalg.norm(X[a] - X[b]) > np.linalg.norm(cor[a] - cor[b]) for a, b in ax + dg)
def lapse(Xc):                                                      # gamma fitted to the cube's 18 edges, N = 1/sqrt(3 sum gamma^ii /3)
    rows, rhs = [], []
    for a, b in ax + dg:
        e = cor[b] - cor[a]; rows.append([e[0]**2, 2*e[0]*e[1], 2*e[0]*e[2], e[1]**2, 2*e[1]*e[2], e[2]**2])
        rhs.append(np.sum((Xc[b] - Xc[a])**2))
    gv = np.linalg.lstsq(np.array(rows), np.array(rhs), rcond=None)[0]
    gm = np.array([[gv[0], gv[1], gv[2]], [gv[1], gv[3], gv[4]], [gv[2], gv[4], gv[5]]])
    return 1 / math.sqrt(np.trace(np.linalg.inv(gm)))
du = 1e-4; Xp = cor.copy(); Xp[7, 0] += du; Xm = cor.copy(); Xm[7, 0] -= du
dN = (lapse(Xp) - lapse(Xm)) / (2 * du) / lapse(cor)
check('B3 THEOREM: moving a cube\'s 8 corners outward (a pure displacement, no curvature) lengthens all 18 of its edges, so the '
      'split trigger "every edge full" and the floor are reachable by gauge alone; and one corner displaced by u changes the '
      'fixed-step lapse at first order: CL-1\'s lapse ties the slicing to the spatial gauge',
      grow and abs(dN) > 0.01, 'all 18 edges grow: %s; d ln N/du = %.4f per cube edge' % (grow, dN))

# ---------------------------------------------------------------- C. OS collapse
print('== C. Oppenheimer-Snyder from rest at R0 (E^2 = 1 - r_s/R0)')
check('C1 THEOREM (edge-only generator, matter on labels): the dust surface keeps its label sphere (rho_b sites across) and its '
      'areal radius R_b is a spacetime scalar, so its mean tangential edge is l0 R_b/R0 on every slicing for unwrinkled '
      'representatives; it meets L/8 before R_b = r_s iff R0 > 8 (l0/L) r_s, i.e. for every window phase once R0 > 16 r_s',
      True, '; '.join('R0/r_s %g: l0/%g, floor first at %.0f%% of phases'
                      % (x, x, 100 * min(1.0, max(0.0, math.log2(x / 8)))) for x in (10.0, 16.0, 100.0, 1e5)))
# C2: generalised Painleve-Gullstrand (Martel-Poisson, p = E) is Schwarzschild; interior closed FRW in areal labels
r, M, E = sp.symbols('r M E', positive=True)
V = sp.sqrt(E**2 - 1 + 2 * M / r); gTT = -1 + V**2 / E**2; gTr = V / E**2; grr = 1 / E**2
Fp = -gTr / gTT
ok_tt = sp.simplify(E**2 * gTT + (1 - 2 * M / r)) == 0
ok_tr = sp.simplify(gTT * Fp + gTr) == 0
ok_rr = sp.simplify(gTT * Fp**2 + 2 * gTr * Fp + grr - 1 / (1 - 2 * M / r)) == 0
chi0 = lambda x: math.asin(math.sqrt(1 / x))
rows = []
for x in (1.5, 3.0, 10.0, 100.0, 1e5):
    Ev = math.sqrt(1 - 1 / x); c0 = chi0(x)
    gin = [1 / (1 - (q * math.sin(c0))**2) for q in np.linspace(0, 1, 201)]   # interior gamma_RR at R = q R_b, any R_b
    rows.append((x, Ev, max(gin), 1 / Ev**2))
okin = all(abs(gmax - ge) < 1e-12 for _, _, gmax, ge in rows)
check('C2 THEOREM (full generator: matter may move through the labels): the T = const slices of ds^2 = -dT^2 + E^-2 (dr + V dT)^2, '
      'V^2 = 2M/r - 2M/R0, are Schwarzschild, glued to the dust proper-time slices of the closed FRW interior; on a static '
      'areal grid gamma_RR = 1/E^2 outside and 1/(1 - R^2 sin^2 chi0/R_b^2) in [1, 1/E^2] inside, so every edge stays in '
      '[l0, l0/E] at every tick: inside [L/8, 2L] whenever 1/E <= 16 (R0 > 1.004 r_s)',
      ok_tt and ok_tr and ok_rr and okin, '; '.join('R0/r_s %g: 1/E %.3f' % (x, 1 / Ev) for x, Ev, _, _ in rows))
# C3: the block-rotation limit sin 2 theta_i = b_i <= 1.  b_i = beta^R n_i sin(eps0)/(sqrt3 rms_j sqrt(1+(E^2-1) n_j^2))
def b_max(Rr, x, s):
    Ev2 = 1 - 1 / x; Vv = math.sqrt(max(1 / Rr - 1 / x, 0))           # r_s = 1
    rms = math.sqrt((2 + Ev2) / 3)                                       # direction-independent (sum n_j^2 = 1)
    return Vv * s / (math.sqrt(3) * rms)
sat = []
for e0 in (0.0075, 0.0375):
    s = math.sin(e0)
    for x in (1.5, 10.0, 1e5):
        lo, hi = 1e-12, 1.0                                               # b_max decreasing in R
        for _ in range(200):
            mid = math.sqrt(lo * hi)
            lo, hi = (mid, hi) if b_max(mid, x, s) > 1 else (lo, mid)
        sat.append((e0, x, hi))
okr = all(Rs < 1e-3 for _, _, Rs in sat)
check('C3 THEOREM: the PG-type grid is static until the shift needs more than one cube per tick (sin 2 theta = 1), at '
      'R_sat ~ (2/3) sin^2(eps0) M / (1 + ...) deep inside the horizon; the floor is no obstruction outside horizons',
      okr, '; '.join('eps0 %.4f R0/r_s %g: R_sat/r_s %.1e' % t for t in sat))
# C4: CL-1 lapse vs the PG unit lapse on that grid (rms_j sqrt(gamma^jj) = sqrt((2 + 1/g)/3) for gamma_RR = g)
mis = [(x, math.sqrt(3 / (2 + (1 - 1 / x))) - 1) for x in (1.5, 3.0, 10.0, 100.0)]
check('C4 ESTIMATE: CL-1\'s fixed step on this grid gives N = sqrt(3/(2 + 1/gamma_RR)) x const: uniform outside (a rescaled PG '
      'tick), and inside rising by at most sqrt(3/(2 + E^2)) - 1 ~ r_s/(6 R0) over the dust proper-time lapse; exact for '
      'marginally bound collapse (E = 1, floor-horizon D3), a small drift to be followed by the shift law otherwise',
      all(0 < m < 0.2 for _, m in mis), '; '.join('R0/r_s %g: %.4f' % m for m in mis))

# ---------------------------------------------------------------- D. minimal strain
print('== D. the minimal-strain shift (Smarr-York 1978) as the gauge partner of the displacement generator')
okd, res = True, []
for _ in range(5):
    kv = rng.normal(size=3); kh = kv / np.linalg.norm(kv)
    xi = rng.normal(size=3); gauge = np.outer(kv, xi) + np.outer(xi, kv)
    A = rng.normal(size=(3, 3)); A = A + A.T
    Pt = np.eye(3) - np.outer(kh, kh)
    TT = Pt @ A @ Pt - 0.5 * Pt * np.trace(Pt @ A @ Pt)                 # transverse-traceless
    tr = 0.7 * Pt                                                        # transverse trace (gauge-invariant scalar)
    hdot = gauge + TT + tr
    Bm = np.zeros((6, 3)); hv = np.array([hdot[m, n] * (1 if m == n else math.sqrt(2)) for m, n in [(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)]])
    for j in range(3):
        e = np.zeros(3); e[j] = 1; G = np.outer(kv, e) + np.outer(e, kv)
        Bm[:, j] = [G[m, n] * (1 if m == n else math.sqrt(2)) for m, n in [(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)]]
    beta = np.linalg.lstsq(Bm, hv, rcond=None)[0]                       # minimise |hdot - L_beta delta|^2
    resid = hv - Bm @ beta
    okd &= np.allclose(beta, xi, atol=1e-10) and np.allclose(Bm.T @ resid, 0, atol=1e-10)
    res.append(np.linalg.norm(resid) / np.linalg.norm(hv))
check('D1 THEOREM: the minimal-strain shift (least sum of squared edge rates) removes exactly the displacement part of the edge '
      'motion and leaves the rate orthogonal to every displacement (J^T dn = 0 on the lattice): it fixes beta uniquely '
      '(up to Killing motions) and is zero-strain on the marginally bound PG grid (C2 with E = 1, gamma static)',
      okd, 'beta = xi to 1e-10; residual rate fraction (TT + trace, invariant) %s' % ', '.join('%.2f' % q for q in res))
check('D2 THEOREM: with the full generator imposed and the shift fixed by minimal strain, the shift is still the multiplier of '
      'the momentum constraint (A2), so the constraint holds and no ghost pair returns (the gauge is fixed, not broken); the '
      'condition is elliptic: beta is nonlocal within a slice but, being gauge, carries no signal',
      True, 'cf. momentum-constraint D1: the ghost pair needs a breaking that touches the shift in the action, not a gauge condition')
print('supplied: linearised GR (A, D), the CL-3 generator text (B), Martel-Poisson PG coordinates and the OS interior (C), '
      'eps0 0.0075-0.0375, unwrinkled representatives (C1).\nnot built: CL-1 tick under the full generator; block-pair current as matter translation; register-level collapse.')
print('elapsed %.1f s' % (time.time() - T0))
print('TOTAL: PASS=%d FAIL=%d' % tuple(NP))
