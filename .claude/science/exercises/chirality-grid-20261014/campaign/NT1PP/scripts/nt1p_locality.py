"""NT-1' gate G-LEG (b2)/(c): locality of the measure's gauge-restoring current kbb[A] (PREREG section 5).
chi(m, y) = |d kbb_m / d A_y| by central differences (eps = 1e-4), at random admissible joined configurations.
usage: python3 nt1p_locality.py Lx T model seed [nconf]"""
import numpy as np, sys, time
from nt1p_lib import *
from lat2d import Geom, rand_half

Lx, T, model, seed = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], int(sys.argv[4])
nconf = int(sys.argv[5]) if len(sys.argv) > 5 else 2
S = Strip(Lx, T); G = Geom(Lx, T, False, -1); rng = np.random.default_rng(seed); t00 = time.time(); eps = 1e-4
MS = Measure(S, model, Ns=8)
print(f"# NT-1' locality Lx={Lx} Lt={2*T} model={model} seed={seed} nconf={nconf} eps={eps} N={S.N} nl={S.nl}", flush=True)
# link midpoints and pair distances on the cylinder
mid = np.array([((l[4] + 0.5, l[5]) if l[2] == 'x' else (l[4], l[5] + 0.5)) for l in S.L])
dxm = np.abs(mid[:, None, 0] - mid[None, :, 0]); dxm = np.minimum(dxm, Lx - dxm); dtm = np.abs(mid[:, None, 1] - mid[None, :, 1])
dist = np.rint(dxm + dtm).astype(int)
inner = (mid[:, 1] >= -T + 2) & (mid[:, 1] <= T - 1)          # links at least one spacing from both open ends
same_slice_x = np.array([[ (S.L[a][2] == 'x' and S.L[b][2] == 'x' and S.L[a][5] == S.L[b][5]) for b in range(S.nl)] for a in range(S.nl)])
dmax = dist.max(); out = {}
chis = []
for ic in range(nconf):
    ua = rand_half(rng, G, 0.25, 0.55); ub = rand_half(rng, G, 0.25, 0.55); ph = rng.normal(0, 0.25, (1, Lx))
    A = S.canon(S.joined(ua, ub, ph))
    base = MS.ray(A, 8); chi = np.zeros((3, S.nl, S.nl))        # [total, loc, Q]
    Ap = np.repeat(A, 2 * S.nl, 0)
    for y in range(S.nl): Ap[2 * y, y] += eps; Ap[2 * y + 1, y] -= eps
    CH = 16 if S.N <= 64 else (6 if S.N <= 96 else (4 if S.N <= 128 else 2))
    for c in range(0, len(Ap), CH):
        r = MS.ray(Ap[c:c+CH], 8)
        for j in range(0, r['kbb'].shape[0], 2):
            y = (c + j) // 2
            for ik, key in enumerate(('kbb', 'kloc', 'kQ')):
                chi[ik, :, y] = np.abs(r[key][j] - r[key][j + 1]) / (2 * eps)
    chis.append(chi)
    print(f"conf {ic}: gmin {base['gmin']:.3f}; |kbb| max {np.abs(base['kbb']).max():.2e} (loc {np.abs(base['kloc']).max():.2e}, Q {np.abs(base['kQ']).max():.2e}); "
          f"mbar bulk mean|.| {np.abs(base['mbar']).mean():.3e} max {np.abs(base['mbar']).max():.3e}; |hbar| max {np.abs(base['hbar']).max():.2e} [{time.time()-t00:.0f}s]", flush=True)
chi = np.max(np.array(chis), 0)
for ik, nm in enumerate(('total kbb', 'k_loc part', 'Q part')):
    prof = np.array([chi[ik][dist == d].max() if np.any(dist == d) else np.nan for d in range(dmax + 1)])
    profi = np.array([chi[ik][(dist == d) & inner[:, None] & inner[None, :]].max() if np.any((dist == d) & inner[:, None] & inner[None, :]) else np.nan for d in range(dmax + 1)])
    print(f"profile chi(d) [{nm}], all links  : " + " ".join(f"{v:.2e}" for v in prof))
    print(f"profile chi(d) [{nm}], inner links: " + " ".join(f"{v:.2e}" for v in profi))
    if ik == 0:
        dd = np.arange(1, dmax + 1); ok = np.isfinite(prof[1:]) & (prof[1:] > 0)
        nu = -np.polyfit(dd[ok], np.log(prof[1:][ok]), 1)[0]; ratio = prof[dmax] / prof[1]
        print(f"FIT total: nu = {nu:.3f} per spacing; chi(dmax={dmax})/chi(1) = {ratio:.2e} -> (b2) criterion nu>=0.3 and ratio<=1e-2: {nu >= 0.3 and ratio <= 1e-2}")
        sx = [chi[0][(dist == d) & same_slice_x].max() for d in range(1, Lx // 2 + 1)]
        print(f"same-slice x-link responses at x-separation 1..{Lx//2}: " + " ".join(f"{v:.2e}" for v in sx))
# F1: x-profile chi_x(s), pairs with |dt_mid| <= 0.5, s = x-separation of midpoints
svals = np.arange(0, Lx / 2 + 0.25, 0.5); sel_t = dtm <= 0.5 + 1e-9
for ik, nm in enumerate(('total', 'loc', 'Q')):
    px = [chi[ik][sel_t & (np.abs(dxm - s) < 1e-9)].max() if np.any(sel_t & (np.abs(dxm - s) < 1e-9)) else np.nan for s in svals]
    print(f"XPROFILE [{nm:5s}] s = " + " ".join(f"{s:.1f}" for s in svals) + " : " + " ".join(f"{v:.2e}" for v in px))
np.save(f"loc_chi_Lx{Lx}_Lt{2*T}_{model}_s{seed}.npy", chi)
print(f"done [{time.time()-t00:.0f}s]")
