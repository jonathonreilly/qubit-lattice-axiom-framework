"""T-2AMP: two isotropy-safe amplitudes on R1's native flavour menu.

Pairs (a) A2 + C111 (staggered), (b) A2 + S(111) (hw1 corner star along 111), on G' = Z2^3 x| O.
Labels P, S; primary placement blind (Q = u^c = d^c = L = e^c = V).  See ../PREREG.md.
Reuses R1's group/rep/averaging code (native_menu.py) and R1's score and control generator.
"""
import sys, itertools, time
import numpy as np

R1S = '/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/masswall/R1/scripts'
sys.path.insert(0, R1S)
import native_menu as nm

np.set_printoptions(precision=3, suppress=True, linewidth=150)
T0 = time.time()
G = [(t, R) for t in nm.TRANS for R in nm.ROT]
NGRP = len(G)
assert NGRP == 192
KTOT = 8
NE = 40
EG = np.logspace(-3, np.log10(0.6), NE)
E1, E2 = np.meshgrid(EG, EG, indexing='ij')
E1 = E1.ravel(); E2 = E2.ravel()
NGRID = E1.size
NDRAW = 5
READ_DRAWS = [0, 1, 2]

PAIRS = {
    'a': (('A2', np.array([1.0])), ('C111', np.array([1.0]))),
    'b': (('A2', np.array([1.0])), ('S', np.ones(3) / np.sqrt(3))),
}

def R(name):
    return nm._reps(name, G)

def monos(d, k):
    return list(itertools.combinations_with_replacement(range(d), k))

def bideg_images(pair, VL, VR, k1, k2):
    """orthonormal basis of span{h(n1,n2)} over bi-degree (k1,k2) equivariant maps (s1,s2) -> VL (x) VR."""
    (s1, n1), (s2, n2) = PAIRS[pair]
    g1 = np.einsum('gij,j->gi', R(s1), n1)
    g2 = np.einsum('gij,j->gi', R(s2), n2)
    rl = R(VL)
    rr = R(VR) if VR is not None else None
    dl = rl.shape[1]; dr = rr.shape[1] if rr is not None else 1
    vecs = []
    for c1 in monos(g1.shape[1], k1):
        m1 = np.ones(NGRP)
        for i in c1: m1 = m1 * g1[:, i]
        for c2 in monos(g2.shape[1], k2):
            mv = m1.copy()
            for i in c2: mv = mv * g2[:, i]
            if np.max(np.abs(mv)) < 1e-12: continue
            if rr is None:
                acc = np.einsum('g,gai->ai', mv, rl) / NGRP
                vecs.extend(list(acc))
            else:
                acc = np.einsum('g,gai,gbj->abij', mv, rl, rr) / NGRP
                vecs.extend(list(acc.reshape(dl * dr, dl * dr)))
    if not vecs: return np.zeros((0, dl * dr))
    A = np.array(vecs)
    u, s, vt = np.linalg.svd(A, full_matrices=False)
    if s[0] < 1e-12: return np.zeros((0, dl * dr))
    r = int(np.sum(s > 1e-8 * s[0]))
    return vt[:r]

def stabiliser(pair):
    (s1, n1), (s2, n2) = PAIRS[pair]
    return [i for i, (t, Rm) in enumerate(G)
            if np.allclose(nm.rep_matrix(s1, t, Rm) @ n1, n1) and np.allclose(nm.rep_matrix(s2, t, Rm) @ n2, n2)]

def char(name, idx):
    return np.array([np.trace(R(name)[i]) for i in idx])

# ---------------- models ----------------
DLAB = ['D_A1_A1_A2', 'D_A1_A2_A2', 'D_A1_C111_C111A2', 'D_A1_A2_C111', 'D_A1_A1_C111']
MODELS = []   # (arm, pair, V, placement, VL, VR)
for pair in ['a', 'b']:
    for V in ['P', 'S']:
        MODELS.append(('primary', pair, V, 'blind', V, V))
for pair in ['a', 'b']:
    for V in ['P', 'S']:
        MODELS.append(('chiralL-PS', pair, V, 'chiralL', V, 'triv3'))
for pair in ['a', 'b']:
    for V in DLAB:
        MODELS.append(('D-blind', pair, V, 'blind', V, V))
for pair in ['a', 'b']:
    for V in DLAB:
        MODELS.append(('D-chiralL', pair, V, 'chiralL', V, 'triv3'))
M = len(MODELS)
ARMS = ['primary', 'chiralL-PS', 'D-blind', 'D-chiralL']

def model_bases(pair, VL, VR):
    out = []
    for k1 in range(KTOT + 1):
        for k2 in range(KTOT + 1 - k1):
            B = bideg_images(pair, VL, VR, k1, k2)
            for row in B: out.append((k1, k2, row.reshape(3, 3)))
    return out

def yuk(bases, coef, e1, e2):
    Y = np.zeros((np.size(e1), 3, 3), complex)
    for c, (k1, k2, X) in zip(coef, bases):
        Y += (np.asarray(e1) ** k1 * np.asarray(e2) ** k2)[:, None, None] * c * X[None]
    return Y

print('=== residual groups and isotropy ===')
Wst = {}
for pair in ['a', 'b']:
    H = stabiliser(pair)
    rots = {tuple(G[i][1].ravel()) for i in H}
    a2s = {nm.a2(G[i][1]) for i in H}
    trs = sorted({tuple(G[i][0]) for i in H})
    print(f'pair {pair}: |H| = {len(H)}, distinct rotations {len(rots)}, a2 values {a2s}, translations {trs}')
    allidx = list(range(NGRP))
    for V in ['P', 'S'] + DLAB:
        chV = char(V, H)
        commut = np.sum(np.abs(chV) ** 2) / len(H)
        scal = all(np.allclose(R(V)[i], R(V)[i][0, 0] * np.eye(3)) for i in H)
        chW = char('W', H)
        invH = np.sum(chV ** 2 * chW) / len(H)
        chVg = char(V, allidx); chWg = char('W', allidx)
        invG = np.sum(chVg ** 2 * chWg) / NGRP
        print(f'   V={V:17s} sum m_i^2 (V|H) = {commut:.2f}  H scalar on V: {str(scal):5s}  '
              f'dim Inv_H(VxVxW) = {invH:.2f}  dim Inv_G(VxVxW) = {invG:.2f}')
    print(f'   dim Inv_H(W) = {np.sum(char("W", H)) / len(H):.2f}')
    ranks = {}
    for k1 in range(KTOT + 1):
        for k2 in range(KTOT + 1 - k1):
            ranks[(k1, k2)] = bideg_images(pair, 'W', None, k1, k2).shape[0]
    print(f'   universal LV: max rank of (s1,s2)->W images over k1+k2<=8: {max(ranks.values())} '
          f'(nonzero at {[k for k, v in ranks.items() if v]})')
sys.stdout.flush()

# ---------------- precompute ----------------
logs = np.full((M, NDRAW, 3, NGRID, 3), -80.0)
logV = np.full((M, NDRAW, NGRID, 3), -80.0)
ORD = {}
BASES = {}
for mi, (arm, pair, V, pl, VL, VR) in enumerate(MODELS):
    bases = model_bases(pair, VL, VR)
    BASES[mi] = bases
    if not bases:
        print(f'model {mi} {MODELS[mi]}: no structures'); continue
    for d in range(NDRAW):
        Us = []
        for f in range(3):
            rng = np.random.default_rng([mi, d, f, 2026])
            coef = rng.normal(size=len(bases)) + 1j * rng.normal(size=len(bases))
            Y = yuk(bases, coef, E1, E2)
            u, s, vh = np.linalg.svd(Y)
            s = s[:, ::-1]; u = u[:, :, ::-1]
            logs[mi, d, f] = np.log(np.maximum(s, 1e-35))
            Us.append(u)
            # numerical bi-degree orders of each singular value
            pts = np.array([[1e-3, 1e-3], [1e-4, 1e-3], [1e-3, 1e-4]])
            Yp = yuk(bases, coef, pts[:, 0], pts[:, 1])
            sp = np.linalg.svd(Yp, compute_uv=False)[:, ::-1]
            p = np.log(np.maximum(sp[1], 1e-300) / np.maximum(sp[0], 1e-300)) / np.log(0.1)
            q = np.log(np.maximum(sp[2], 1e-300) / np.maximum(sp[0], 1e-300)) / np.log(0.1)
            dead = sp[0] < 1e-13 * sp[0].max()
            ORD[(mi, d, f)] = [('inf' if dead[i] else f'e1^{np.round(2*p[i])/2:g} e2^{np.round(2*q[i])/2:g}') for i in range(3)][::-1]
        V_ = np.einsum('gji,gjk->gik', Us[0].conj(), Us[1])
        A = np.abs(V_)
        logV[mi, d, :, 0] = np.log(np.maximum(A[:, 0, 1], 1e-35))
        logV[mi, d, :, 1] = np.log(np.maximum(A[:, 1, 2], 1e-35))
        logV[mi, d, :, 2] = np.log(np.maximum(A[:, 0, 2], 1e-35))
    print(f'precomputed {mi:2d} {arm:10s} pair {pair} V={V:17s} {pl:7s} structures {len(bases):3d}  t={time.time()-T0:.0f}s')
    sys.stdout.flush()

def hs(x):
    return 0.5 * (x.max(-1) - x.min(-1))

def score(obs):
    """components [M, D, NGRID, 4] (up, dn, lep, ckm) and total [M, D, NGRID]."""
    lu, ld, le, lc = (np.log(np.asarray(obs[k])) for k in ['up', 'dn', 'le', 'ckm'])
    up = hs(logs[:, :, 0] - lu); dn = hs(logs[:, :, 1] - ld); lp = hs(logs[:, :, 2] - le)
    ck = np.abs(logV - lc).max(-1)
    comp = np.stack([up, dn, lp, ck], -1)
    return comp, comp.max(-1)

def arm_best(tot, arm):
    idx = [i for i, m in enumerate(MODELS) if m[0] == arm]
    return np.exp(tot[idx].min(-1).min(0)), idx   # per draw

DATA = {
    'MZ':  dict(up=[1.27e-3, 0.619, 171.7], dn=[2.90e-3, 0.055, 2.89], le=[0.48657e-3, 0.102718, 1.74624]),
    'GUT': dict(up=[0.48e-3, 0.235, 74.0], dn=[1.14e-3, 0.022, 1.00], le=[0.469652e-3, 0.0991466, 1.68558]),
    'MIX': dict(up=[2.16e-3, 1.27, 172.69], dn=[4.67e-3, 0.0934, 4.18], le=[0.511e-3, 0.1057, 1.777]),
}
for k in DATA: DATA[k]['ckm'] = [0.225, 0.041, 0.0037]

def passes(perdraw):
    return int(np.sum(perdraw[READ_DRAWS] <= 3.0)) >= 2

print('\n=== real data ===')
REAL = {}
for tag, obs in DATA.items():
    comp, tot = score(obs)
    rat_obs = (obs['up'][0] / obs['up'][2]) / (obs['dn'][0] / obs['dn'][2])
    print(f'\n--- set {tag}: observed (m1/m3)_up/(m1/m3)_dn = 1/{1/rat_obs:.0f} ---')
    for mi, (arm, pair, V, pl, VL, VR) in enumerate(MODELS):
        if arm != 'primary' and tag != 'MZ': continue
        fs = np.exp(tot[mi].min(-1))
        line = f'{arm:10s} pair {pair} V={V:17s} {pl:7s} best x per draw {np.round(fs, 1)}'
        if arm == 'primary':
            print(line)
            for d in range(NDRAW):
                g = int(np.argmin(tot[mi, d]))
                c = np.exp(comp[mi, d, g])
                s_u = np.exp(logs[mi, d, 0, g]); s_d = np.exp(logs[mi, d, 1, g])
                ru = s_u[0] / s_u[2]; rd = s_d[0] / s_d[2]
                Vabs = np.exp(logV[mi, d, g])
                print(f'    draw {d}: e1={E1[g]:.3g} e2={E2[g]:.3g}  factors up/dn/lep/ckm {np.round(c, 1)}  '
                      f'm1/m3 up {ru:.2e} dn {rd:.2e} (ratio 1/{rd/ru if ru>0 else np.inf:.2g})  |Vus,Vcb,Vub| {np.round(Vabs, 4)}')
        else:
            print(line)
    REAL[tag] = {arm: arm_best(tot, arm)[0] for arm in ARMS}
    for arm in ARMS:
        b = REAL[tag][arm]
        print(f'  SEARCH {arm:10s} best x per draw {np.round(b, 2)}  -> meets PASS fit criterion: {passes(b)}')
sys.stdout.flush()

print('\n=== exponent structure (primary, draw 0; per sector up/dn/lep; heavy -> light) ===')
for mi, m in enumerate(MODELS):
    if m[0] != 'primary': continue
    print(f'pair {m[1]} V={m[2]}: ' + ' | '.join(str(ORD[(mi, 0, f)]) for f in range(3)))
for mi, m in enumerate(MODELS):
    if m[0] == 'primary': continue
    print(f'{m[0]:10s} pair {m[1]} V={m[2]:17s}: up {ORD.get((mi, 0, 0), "no structures (massless)")}')

print('\n=== commutator check at a generic grid point (e1=e2=0.05), draw 0 ===')
for mi, m in enumerate(MODELS):
    if m[0] != 'primary' or not BASES[mi]: continue
    Ys = []
    for f in range(2):
        rng = np.random.default_rng([mi, 0, f, 2026])
        coef = rng.normal(size=len(BASES[mi])) + 1j * rng.normal(size=len(BASES[mi]))
        Ys.append(yuk(BASES[mi], coef, np.array([0.05]), np.array([0.05]))[0])
    Hu = Ys[0] @ Ys[0].conj().T; Hd = Ys[1] @ Ys[1].conj().T
    cm = np.linalg.norm(Hu @ Hd - Hd @ Hu) / (np.linalg.norm(Hu) * np.linalg.norm(Hd))
    su = np.linalg.svd(Ys[0], compute_uv=False)
    print(f'pair {m[1]} V={m[2]}: ||[Hu,Hd]||/(|Hu||Hd|) = {cm:.2e}; up singular values {su}')
sys.stdout.flush()

print('\n=== control: 300 random spectra (R1 generator) ===')
rng = np.random.default_rng(7)
NC = 300
cb = {arm: np.zeros((NC, NDRAW)) for arm in ARMS}
for i in range(NC):
    obs = {}
    for sec in ['up', 'dn', 'le']:
        r21 = 10 ** rng.uniform(-4, 0); r32 = 10 ** rng.uniform(-4, 0)
        obs[sec] = [r21 * r32, r32, 1.0]
    obs['ckm'] = list(10 ** rng.uniform(-3, -0.3, size=3))
    comp, tot = score(obs)
    for arm in ARMS:
        cb[arm][i] = arm_best(tot, arm)[0]
for arm in ARMS:
    pr = np.mean([passes(cb[arm][i]) for i in range(NC)])
    bmin = cb[arm][:, READ_DRAWS].min(1)
    print(f'{arm:10s} random PASS-criterion rate {pr:.3f}; best-of-3-draws within x3 {np.mean(bmin <= 3):.3f}, '
          f'x10 {np.mean(bmin <= 10):.3f}; quantiles 10/50/90 of best {np.round(np.quantile(bmin, [0.1, 0.5, 0.9]), 1)}')
    for tag in DATA:
        rb = REAL[tag][arm][READ_DRAWS].min()
        print(f'     {tag}: real best-of-3 x{rb:.2f}; random fraction at least as good {np.mean(bmin <= rb):.3f}')

print('\n=== readings (primary arm) ===')
pr = np.mean([passes(cb['primary'][i]) for i in range(NC)])
for tag in DATA:
    b = REAL[tag]['primary']
    fitpass = passes(b)
    anyfit = bool(np.any(b[READ_DRAWS] <= 3.0))
    if fitpass and pr <= 0.05: rd = '2AMP-PASS'
    elif (not anyfit) or pr > 0.20: rd = '2AMP-FAIL'
    else: rd = 'OPEN'
    print(f'{tag}: best per draw {np.round(b, 2)}; random pass rate {pr:.3f} -> {rd}')
print(f'done t={time.time()-T0:.0f}s')

# ---------------- POST-HOC diagnostics (added after the first run; not pre-registered) ----------------
print('\n=== POST-HOC diagnostics (added after first run; do not enter the reading) ===')
PRIM = [i for i, m in enumerate(MODELS) if m[0] == 'primary']
for tag, obs in DATA.items():
    comp, tot = score(obs)
    for mi in PRIM:
        mo = np.exp(comp[mi, :, :, :3].max(-1).min(-1))
        print(f'{tag} pair {MODELS[mi][1]} V={MODELS[mi][2]}: mass-only best x per draw {np.round(mo, 1)}')
for mi in PRIM:
    A = np.exp(logV[mi])
    dev = np.minimum(A, 1 - A).max()
    su = np.exp(logs[mi, :, 0]); sd = np.exp(logs[mi, :, 1])
    rr = (su[..., 0] / su[..., 2]) / (sd[..., 0] / sd[..., 2])
    h3 = np.exp(logs[mi, :, :, :, 0] - logs[mi, :, :, :, 2])   # m1/m3 every sector
    print(f'pair {MODELS[mi][1]} V={MODELS[mi][2]}: max over grid/draws of min(|V_ij|, 1-|V_ij|) = {dev:.1e}; '
          f'(m1/m3)_u/(m1/m3)_d quantiles 1/50/99% {np.round(np.quantile(rr, [0.01, 0.5, 0.99]), 3)}; '
          f'min m1/m3 over grid, all sectors/draws {h3.min():.2e}, 1% quantile {np.quantile(h3, 0.01):.2e}')
