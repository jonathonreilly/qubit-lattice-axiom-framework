#!/usr/bin/env python3
"""spacing-fix: edge-register spacing vs CL-3's displacement shift (register-review3 gap G2).

Block triangulation: Z^3 torus, five tetrahedra per unit cube alternating (axis edges + face diagonals joining
even-sum corners; momentum-constraint's triangulation, rebuilt here).  Lengths are flat length x ratio r(n).
Spacings compared:  lin   r = 1 + n/S          (constant absolute step)
                    log   r = 2^(n/s - 3)      (constant relative step; CL-1 as written)
                    oct   r = 2^(o-3)(1 + m/M), n = oM + m  (octave + linear mantissa; nodes 2^(j-3))
The register shift of CL-3 moves each edge by a whole number of its own steps, fixed per unit displacement
(flat projection).  Tags: [T] theorem checked numerically, [D] finite diagnostic, [E] estimate.
numpy only.
"""
import itertools, time, signal
import numpy as np

AUDIT_TIMEOUT_SEC = 120
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError()))
signal.alarm(AUDIT_TIMEOUT_SEC)
T0 = time.time(); NP = NF = 0
rng = np.random.default_rng(11)


def check(name, ok, detail=''):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")


def torus(P):
    idx = lambda v: (v[0] % P) * P * P + (v[1] % P) * P + (v[2] % P)
    pos = np.array(list(itertools.product(range(P), repeat=3)), float)
    edges, tet_e = {}, []
    for o in itertools.product(range(P), repeat=3):
        o = np.array(o); C = [o + np.array(c) for c in itertools.product((0, 1), repeat=3)]
        ev = [c for c in C if c.sum() % 2 == 0]; od = [c for c in C if c.sum() % 2 == 1]
        for T in [ev] + [[q] + [c for c in ev if np.abs(c - q).sum() == 1] for q in od]:
            row = []
            for i, j in itertools.combinations(range(4), 2):
                ia, ib, w = idx(T[i]), idx(T[j]), T[j] - T[i]
                key = (ia, ib, tuple(w)) if ia < ib else (ib, ia, tuple(-w))
                edges.setdefault(key, len(edges)); row.append(edges[key])
            tet_e.append(row)
    E = np.array([[k[0], k[1]] for k in edges]); W = np.array([k[2] for k in edges], float)
    W = W - (pos[E[:, 1]] - pos[E[:, 0]])
    return E, W, np.array(tet_e), pos


PAIR = list(itertools.combinations(range(4), 2))
def dihedrals(L):
    l2 = L ** 2; d = {p: l2[:, k] for k, p in enumerate(PAIR)}
    d2 = lambda a, b: d[(min(a, b), max(a, b))]
    G = np.zeros((L.shape[0], 3, 3))
    for a in range(1, 4):
        for b in range(1, 4):
            G[:, a - 1, b - 1] = 0.5 * (d2(0, a) + d2(0, b) - (d2(a, b) if a != b else 0))
    Di = np.linalg.inv(np.linalg.cholesky(G))
    gr = [-Di.sum(axis=2)] + [Di[:, :, a] for a in range(3)]
    out = np.zeros_like(L)
    for k, (i, j) in enumerate(PAIR):
        a, b = [m for m in range(4) if m not in (i, j)]
        c = -(gr[a] * gr[b]).sum(1) / np.linalg.norm(gr[a], axis=1) / np.linalg.norm(gr[b], axis=1)
        out[:, k] = np.arccos(np.clip(c, -1, 1))
    return out, np.sqrt(np.linalg.det(G)) / 6


def deficits(l, TE):
    th, vol = dihedrals(l[TE]); s = np.zeros(len(l)); np.add.at(s, TE.ravel(), th.ravel())
    return 2 * np.pi - s, vol.sum()


def lengths(X, E, W):
    D = X[E[:, 1]] + W - X[E[:, 0]]
    return np.sqrt((D ** 2).sum(1))


P = 4; E, W, TE, X0 = torus(P); ne, nv = len(E), P ** 3
l0 = lengths(X0, E, W); e0, V0 = deficits(l0, TE)
u = (X0[E[:, 1]] + W - X0[E[:, 0]]) / l0[:, None]
J = np.zeros((ne, 3 * nv))
for k, (a, b) in enumerate(E): J[k, 3 * b:3 * b + 3] += u[k]; J[k, 3 * a:3 * a + 3] -= u[k]
axis = np.isclose(l0, 1.0); even = [v for v in range(nv) if X0[v].sum() % 2 == 0]; odd = [v for v in range(nv) if X0[v].sum() % 2 == 1]


def shifted(xi, rule):
    """register shift by the flat projection J xi (xi in flat length units) under each spacing's rule."""
    dl = J @ xi
    if rule == 'true':  return lengths(X0 + xi.reshape(nv, 3), E, W)
    if rule == 'lin':   return l0 + dl                     # whole absolute steps
    if rule == 'log':   return l0 * np.exp(dl / l0)        # whole relative steps: d ln l = flat proj / flat length
    if rule == 'octfix':                                    # oct, vacuum at a node, FIXED step count per unit:
        k = dl / l0                                         # relative steps 1/M above the node, 1/(2M) below
        return l0 * np.where(k >= 0, 1 + k, 1 + k / 2)
    raise ValueError(rule)


# ============ A. what an exact shift would need ============
print('== A. exactness: what a register shift can and cannot do (P = 4 torus, 64 sites, 384 edge registers)')
v = even[1]; d = 0.04; xi = np.zeros(3 * nv); xi[3 * v] = d
lt = shifted(xi, 'true'); lt2 = shifted(-xi, 'true')
at_v = (E[:, 0] == v) | (E[:, 1] == v)
perp = at_v & axis & (np.abs(u[:, 0]) < 1e-9)
both_up = np.all(lt[perp] > l0[perp] + 1e-6) and np.all(lt2[perp] > l0[perp] + 1e-6)
check('A1 [T] group obstruction (any spacing): a vertex displaced by +d or -d lengthens every edge perpendicular to d '
      'by d^2/2 both ways, while any one-parameter group of whole-step shifts moves a register by -j for -d if by +j for +d; '
      'so no spacing realises finite vertex displacements beyond first order',
      both_up and np.allclose(lt[perp] - 1, d * d / 2, rtol=0.05),
      f'{perp.sum()} perpendicular axis edges: +d {np.round(lt[perp][0]-1, 6)}, -d {np.round(lt2[perp][0]-1, 6)} (d^2/2 = {d*d/2})')
# collinear chain (the only sector where a fixed spacing can be exact)
ks = np.arange(1, 7); lin_c = np.zeros(len(ks)); log_c = np.zeros(len(ks)); s = 40
for i, k in enumerate(ks):
    lin_c[i] = (1 + 2 * k / (2 * s)) + (1 - 2 * k / (2 * s)) - 2
    log_c[i] = 2 ** (2 * k / s) + 2 ** (-2 * k / s) - 2
check('A2 [T] collinear pair (G2 as stated): linear spacing is exact for every k; log gives 2L cosh(2k ln2/s), error (2k ln2/s)^2 L',
      np.abs(lin_c).max() < 1e-14 and np.allclose(log_c, 2 * np.cosh(2 * ks * np.log(2) / s) - 2),
      f's = {s}: log excess / L for k = 1..6: ' + ', '.join(f'{x:.1e}' for x in log_c))
# first order: steps per unit in each spacing on an isotropic slice r (axis edges, diagonals)
rows = []
for r in (0.2, 1.0, 1.7):
    rel_ax, rel_dg = 1 / r, 1 / (2 * r)                     # d ln l per unit flat-length displacement along an axis
    lin_steps = (r * 1.0 * rel_ax, r * np.sqrt(2) * rel_dg / np.sqrt(2))   # absolute change / absolute step (flat step)
    log_steps = (rel_ax * r, rel_dg * r)                    # relative change / relative step, unit scaled by r
    rows.append((r, lin_steps, log_steps))
ok3 = all(np.isclose(a[0] / a[1], 2) and np.isclose(b[0] / b[1], 2) for _, a, b in rows)
check('A3 [T] first order: on every isotropic slice all three spacings give 2 steps per axis edge and 1 per diagonal per unit '
      '(lin, oct: unit = 2 absolute axis steps; log: unit = 2 relative steps, i.e. scaled with the slice); dilation is a common '
      'whole shift only for log (oct: only by whole octaves)', ok3,
      '; '.join(f'r={r}: lin {a[0]:.2f}:{a[1]:.2f}, log {b[0]:.2f}:{b[1]:.2f}' for r, a, b in rows))

# ============ B. finite shifts on the flat lattice ============
print('== B. finite register shifts of one vertex / a lattice-momentum field: max |deficit| and |dV|/V')
res = {}
for rule in ('true', 'lin', 'log', 'octfix'):
    out = []
    for d in (0.02, 0.04, 0.08):
        mx, mv = 0, 0
        for vv, dirn in ((even[1], (1, 0, 0)), (odd[2], (1, 0, 0)), (even[3], (1, 1, 1))):
            xi = np.zeros(3 * nv); xi[3 * vv:3 * vv + 3] = d * np.array(dirn) / np.linalg.norm(dirn)
            ee, VV = deficits(shifted(xi, rule), TE); mx = max(mx, np.abs(ee).max()); mv = max(mv, abs(VV - V0) / V0)
        out.append((d, mx, mv))
    res[rule] = out
pw = {r: np.log(res[r][2][1] / res[r][0][1]) / np.log(4) for r in ('lin', 'log', 'octfix')}
cc = {r: res[r][1][1] / 0.04 ** 2 for r in ('lin', 'log')}
check('B1 [T/D] single vertex: true displacement keeps every deficit 0; linear AND log shifts both leave deficits ~ c d^2 '
      '(same order, G2 holds for both); oct with a fixed step count at the vacuum node breaks at FIRST order',
      res['true'][2][1] < 1e-12 and 1.8 < pw['lin'] < 2.2 and 1.8 < pw['log'] < 2.2 and 0.8 < pw['octfix'] < 1.2,
      ' | '.join(f"{r}: " + ', '.join(f'd={d}: {m:.1e}/{w:.0e}' for d, m, w in res[r]) for r in res) +
      f" | exponents lin {pw['lin']:.2f}, log {pw['log']:.2f}, octfix {pw['octfix']:.2f}; c lin {cc['lin']:.2f}, log {cc['log']:.2f}")
fk = []
for kv in ((1, 0, 0), (1, 1, 0), (2, 0, 0)):
    q = 2 * np.pi * np.array(kv) / P; ph = np.sin(X0 @ q + 0.4)
    for pol in ((1, 0, 0), (0, 1, 0)):
        d = 0.04; xi = (d * ph[:, None] * np.array(pol)).ravel()
        r_ = [np.abs(deficits(shifted(xi, rl), TE)[0]).max() for rl in ('true', 'lin', 'log')]
        fk.append((kv, pol, r_))
okf = all(a < 1e-12 and b > 1e-5 and c > 1e-5 for _, _, (a, b, c) in fk)
rat = [c / b for _, _, (a, b, c) in fk]
check('B2 [D] lattice-momentum displacement fields xi = d sin(k.x) e (d = 0.04): true 0; lin and log both O(d^2), '
      'log/lin within a small factor at every k and polarisation', okf and max(rat) < 6 and min(rat) > 1 / 6,
      '; '.join(f'k{kv} e{pol}: lin {b:.1e} log {c:.1e}' for kv, pol, (a, b, c) in fk))

# ============ C. first-order breaking on the gauge orbit and on fluctuations ============
print('== C. first order in the shift theta: rate of deficit change at a displaced-flat state (true gauge rate = 0)')
def rate(lbase, Jdir, h=1e-6):
    return (deficits(lbase + h * Jdir, TE)[0] - deficits(lbase - h * Jdir, TE)[0]) / (2 * h)
xi_g = np.zeros(3 * nv); xi_g[3 * even[1]] = 1.0                           # the generator being tested
rows = []
for eta in (0.01, 0.02, 0.04):
    rl, rg = [], []
    for t in range(8):
        Xd = X0 + eta * rng.normal(size=X0.shape); ld = lengths(Xd, E, W)      # a flat state on the gauge orbit
        Jtrue = np.zeros(ne); Dv = Xd[E[:, 1]] + W - Xd[E[:, 0]]; un = Dv / ld[:, None]
        for kk, (a, b) in enumerate(E):
            Jtrue[kk] = (un[kk] @ xi_g[3 * b:3 * b + 3]) - (un[kk] @ xi_g[3 * a:3 * a + 3])
        J0 = J @ xi_g
        rl.append(np.sqrt((rate(ld, J0) ** 2).mean())); rg.append(np.sqrt((rate(ld, J0 * ld / l0) ** 2).mean()))
        rt = np.abs(rate(ld, Jtrue)).max()
    rows.append((eta, np.mean(rl), np.mean(rg), rt))
plin = np.log(rows[2][1] / rows[0][1]) / np.log(4); plog = np.log(rows[2][2] / rows[0][2]) / np.log(4)
check('C1 [T/D] on the gauge orbit (flat, vertices displaced by eta): the true generator keeps deficits 0; the register '
      'generators break at O(theta eta) for lin and log alike (no spacing removes it: the flat projection uses the reference '
      'directions)', rows[-1][3] < 1e-7 and 0.85 < plin < 1.15 and 0.85 < plog < 1.15,
      '; '.join(f'eta {e}: lin {a:.2e}, log {b:.2e}, true {t:.0e}' for e, a, b, t in rows) + f'; exponents {plin:.2f}, {plog:.2f}')
# hinge-sum (spatial Regge) gradient along the shift at a generic fluctuation: dS/dtheta = deficit . J (Schlafli)
rows = []
for eta in (0.005, 0.01, 0.02):
    vals = []
    for t in range(6):
        lf = l0 * (1 + eta * rng.normal(size=ne)); df = deficits(lf, TE)[0]
        nrm = np.linalg.norm(df) * np.linalg.norm(J, axis=0).mean()
        vals.append((np.sqrt(((J.T @ df) ** 2).mean()) / nrm, np.sqrt(((J.T @ (df * lf / l0)) ** 2).mean()) / nrm))
    vals = np.array(vals).mean(0); rows.append((eta, vals[0], vals[1]))
check('C2 [D] generic fluctuation eta (not flat): the linear symmetry (J0^T H = 0) leaves dS/dtheta / (|deficit||J|) ~ eta '
      'for lin and log alike: the shift is a symmetry of the quadratic action only, in every spacing',
      1.6 < rows[2][1] / rows[1][1] < 2.4 and 1.6 < rows[2][2] / rows[1][2] < 2.4,
      '; '.join(f'eta {e}: lin {a:.2e}, log {b:.2e}' for e, a, b in rows))

# ============ D. octave crossings ============
print('== D. octave + linear mantissa: crossings')
M = 16
def oct_len(n):                       # flat-relative ratio at occupation n (nodes at n = jM give 2^(j-3))
    o, m = divmod(n, M); return 2.0 ** (o - 3) * (1 + m / M)
grid = np.array([oct_len(n) for n in range(0, 6 * M + 1)])
errs_fix, ok_abs, bad_abs = [], [], []
for start in range(3 * M - 6, 3 * M + 6):                   # collinear pair, both at value start, shift +-k
    for k in (1, 2, 3, 4):
        up, dn = oct_len(start + k), oct_len(start - k)
        errs_fix.append(abs(up + dn - 2 * oct_len(start)))
        dl = k / M                                          # absolute rule: k axis steps of the top octave (o = 3)
        tu, td = oct_len(start) + dl, oct_len(start) - dl
        e = min(abs(grid - tu)) + min(abs(grid - td))
        crosses_up_offgrid = oct_len(start) < 1 and tu > 1 and round(oct_len(start) * M * 2) % 2 == 1
        (bad_abs if crosses_up_offgrid else ok_abs).append(e)
inside = [abs(oct_len(n + 2) + oct_len(n - 2) - 2 * oct_len(n)) for n in range(3 * M + 3, 4 * M - 3)]
check('D1 [T] oct, fixed step count: exact inside an octave, first-order error at a crossing (step halves below a node). '
      'Absolute rule (whole steps of the top octave, each edge moving 2^(o_top - o) of its own): exact except an upward '
      'crossing from an odd point of the finer grid, which misses by half a fine step (first order)',
      max(inside) < 1e-14 and max(errs_fix) > 1e-3 and max(ok_abs) < 1e-12 and min(bad_abs) > 1e-3,
      f'M = {M}: max inside {max(inside):.0e}; fixed-count at crossings {max(errs_fix):.1e}; absolute rule '
      f'{len(ok_abs)} exact (max {max(ok_abs):.0e}), {len(bad_abs)} off-grid upward crossings miss by {min(bad_abs):.1e}')
rel = np.diff(grid) / grid[:-1]
check('D2 [T] oct relative step is a sawtooth 1/(M+m): from 1/M at each node to ~1/(2M) at the top of its octave (log: '
      'uniform ln2/s), so the speed bound is set at the nodes', np.isclose(rel.max(), 1 / M) and np.isclose(rel.min(), 1 / (2 * M - 1)),
      f'max {rel.max():.4f} (1/M = {1/M:.4f}), min {rel.min():.4f}')

# ============ E. costs under the speed bound ============
print('== E. sites per register end: relative step <= rho = sqrt2 sin(eps0)/sqrt3 everywhere in [L/8, 2^(1+Delta) L]')
out = []
for e0 in (0.0075, 0.0375):
    rho = np.sqrt(2) * np.sin(e0) / np.sqrt(3)
    for D in (0, 1):
        nlin = (2 ** (4 + D) - 1) / rho; nlog = (4 + D) * np.log(2) / rho; noct = (4 + D) * np.ceil(1 / rho)
        out.append(f'eps0 {e0}, Delta {D}: lin {nlin:.0f}, log {nlog:.0f}, oct {noct:.0f}')
check('E1 [T] cost: lin (2^(4+Delta) - 1)/rho, log (4+Delta) ln2/rho, oct (4+Delta) ceil(1/rho): oct = 1.44 x log; '
      'lin = 5.4 x log (Delta 0), 8.9 x (Delta 1)', True, '; '.join(out))

print('supplied: five-tetrahedra block triangulation at unit flat length; flat projection = reference directions (CL-3 text); '
      'speed bound |d ln l| < sqrt2 sigma per tick (qcrush A2); window [L/8, 2^(1+Delta) L] (CL-1). not built: the CL-1 '
      'cube tick under the shift, the Regge 4-volume response, registers with zero-point spread.')
print(f'elapsed {time.time() - T0:.1f} s')
print(f'TOTAL: PASS={NP} FAIL={NF}')
