"""OBS-2 analysis of yuk_kin_*.json: controls (staggered reflection, cubic covariance, continuum log, N-convergence)
and per-pair corner velocity tensors dv_a = B_a + Sigma1 (per y_s y_s')."""
import json, numpy as np, itertools
SY = ['0', 'x', 'y', 'z']
def load(N, m, D):
    return json.load(open(f"yuk_kin_N{N}_m{m}_D{D}_mH{m}.json"))
def key(a, b):
    return a + b if SY.index(a) <= SY.index(b) else b + a
def dv(r, c, v, a, b):
    e = r[c][v][key(a, b)]
    return np.array(e['B']) + e['S1']
P = {'0': '0', 'x': 'y', 'y': 'z', 'z': 'x'}     # C3 about (111): x->y->z->x
perm_ax = [1, 2, 0]                                 # axis a -> P(a)
Ns = [24, 32, 48, 64, 96]; ms = ['0.1', '0.05', '0.025']; Ds = ['0.0', '0.5']
print("== Control 5 (staggered reflection): on-site pair '00', Delta 0: dv at hw1 corners vs origin; K = dv_par - dv_perp")
for N in (48, 96):
    r = load(N, '0.1', '0.0')
    print(f"  N={N}: x {dv(r,'x','sym','0','0')}, o {dv(r,'o','sym','0','0')}, K_x = {dv(r,'x','sym','0','0')[0]-dv(r,'x','sym','0','0')[1]:.2e}")
print("== Control 3 (cubic covariance, C3 about 111): max |dv^(P c)_{P a}[P s P s'] - dv^(c)_a[s s']| over pairs, variants")
for N, m, D in itertools.product((32, 96), ('0.1',), Ds):
    r = load(N, m, D); mx = 0.0; scale = 0.0
    for v in ('sym', 'int', 'ext'):
        for a, b in itertools.combinations_with_replacement(SY, 2):
            for c in 'xyz':
                x0 = dv(r, c, v, a, b); x1 = dv(r, P[c], v, P[a], P[b])
                mx = max(mx, np.abs(x1[perm_ax] - x0).max()); scale = max(scale, np.abs(x0).max())
                off = r[c][v][key(a, b)]['offdiag']; mx = max(mx, 0)
    offm = max(r[c][v][k]['offdiag'] for c in 'xyz' for v in ('sym','int','ext') for k in r[c][v])
    print(f"  N={N} m0={m} Delta={D}: max covariance residual {mx:.2e} (scale {scale:.2e}); max off-diagonal d b_a/d q_b = {offm:.2e}")
print("== Control 2b (continuum log): Sigma1 and B for '00' at corner x, m0 = mH halved")
for D in Ds:
    for N in (48, 64, 96):
        r1 = load(N, '0.1', D); r2 = load(N, '0.05', D); r3 = load(N, '0.025', D)
        s = [r[ 'x']['sym']['00']['S1'] for r in (r1, r2, r3)]; B = [np.mean(r['x']['sym']['00']['B']) for r in (r1, r2, r3)]
        print(f"  Delta={D} N={N}: dS1(0.1->0.05) {s[1]-s[0]:+.4e}, (0.05->0.025) {s[2]-s[1]:+.4e} [continuum -4.390e-03];  dB {B[1]-B[0]:+.4e}, {B[2]-B[1]:+.4e}")
print("== N-convergence and m0 dependence: corner x, variant sym, dv_a (a = x,y,z) per pair")
for D in Ds:
    for a, b in itertools.combinations_with_replacement(SY, 2):
        rows = []
        for m in ms:
            vals = [dv(load(N, m, D), 'x', 'sym', a, b) for N in Ns]
            rows.append(vals)
        print(f" Delta={D} pair {a}{b}:")
        for m, vals in zip(ms, rows):
            aniso = [v - v.mean() for v in vals]
            print(f"   m0={m:5s} " + " | ".join(f"N{N}: iso {v.mean():+.4e} an ({an[0]:+.3e},{an[1]:+.3e},{an[2]:+.3e})" for N, v, an in zip(Ns, vals, aniso) if N in (32, 48, 96)))
