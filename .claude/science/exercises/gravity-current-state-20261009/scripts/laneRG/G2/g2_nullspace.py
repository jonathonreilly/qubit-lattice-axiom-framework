"""Lane RG probe G2, part 3: amplitude-weighted collision-invariant null space.

Rows: vacuum-sampled on-shell 2<->2 configurations (k1,k2 uniform; exact collision measure),
weighted by sqrt(w)|T_r|, T_r = Phi_r * T_0 (binomial filter ((1+cos k)/2)^r on each leg,
static gapless exchange T_0 = 1/Omega^2(q_t) + 1/Omega^2(q_u), forward cut |q| > 0.3).
Columns: odd periodic sin(n.k), |n|_inf <= R (half set), optionally plus the sawtooth k_x, k_y
(principal-zone values).  Row value = sum_legs s_i f(k_i), s = (+,+,-,-).
Rows normalised by sqrt(sum w|T_r|^2), so singular values are rate-weighted rms defects.

Reports, with BOTH a relative and an absolute (1e-12) zero test:
  sig_min(periodic only), sig_min(periodic + sawtooth), the sawtooth-alone defect,
  the best sawtooth+periodic defect (lstsq with sawtooth coefficient fixed to 1),
  and the log-domain sawtooth defect (no SVD floor) for comparison with 16^-r.
"""
import numpy as np, itertools
from scipy.special import logsumexp
from g2_lib import *

rng = np.random.default_rng(77)
d, m = 2, 1.0
eps = make_disp('KG', m)
k1, k2, k3, k4, w = sample_free(eps, d, 20000, rng)
qt, qu = wrap(k1 - k3), wrap(k1 - k4)
keep = np.minimum(np.linalg.norm(qt, axis=1), np.linalg.norm(qu, axis=1)) > 0.3
k1, k2, k3, k4, w, qt, qu = [a[keep] for a in (k1, k2, k3, k4, w, qt, qu)]
T0 = 1 / Omega2(qt) + 1 / Omega2(qu)
U = umklapp(k1, k2, k3, k4)
nwind = np.round((k1 + k2 - k3 - k4) / (2 * np.pi))
print(f"configs {len(w)}, umklapp measure fraction {np.sum(w[U])/np.sum(w):.3f}, "
      f"max |winding residual| {np.max(np.abs((k1+k2-k3-k4)/(2*np.pi)-nwind)):.1e}")
R = 4
ns = np.array([n for n in itertools.product(range(-R, R + 1), repeat=d) if any(n) and n > tuple(-np.array(n))], float)
P = sum(s * np.sin(kk @ ns.T) for s, kk in zip([1, 1, -1, -1], [k1, k2, k3, k4]))     # periodic block
S = 2 * np.pi * nwind                                                                  # sawtooth block (= k1+k2-k3-k4 exactly)
print(f"basis: {P.shape[1]} odd periodic + 2 sawtooth columns")
print("  r   sig_min(per)  sig_max(per) | sig_min(per+saw) | saw-alone defect | best saw+per defect | log10 saw defect (exact) | log10 16^-r")
for r in [0, 1, 2, 3, 4, 6, 8, 10, 12, 16]:
    lPhi = sum(np.sum(np.log((1 + np.cos(kk)) / 2 + 1e-320), 1) for kk in (k1, k2, k3, k4)) * r
    lwt = 0.5 * np.log(w) + np.log(np.abs(T0)) + lPhi
    lwt -= 0.5 * logsumexp(2 * lwt)
    wt = np.exp(lwt)
    Pw = P * wt[:, None]; Sw = S * wt[:, None]
    sp = np.linalg.svd(Pw, compute_uv=False)
    sa = np.linalg.svd(np.hstack([Pw, Sw]), compute_uv=False)
    saw = np.linalg.norm(Sw[:, 0])
    c, *_ = np.linalg.lstsq(Pw, -Sw[:, 0], rcond=None)
    best = np.linalg.norm(Sw[:, 0] + Pw @ c)
    # exact log-domain sawtooth (x-component) defect
    sel = nwind[:, 0] != 0
    lsaw = 0.5 * logsumexp(2 * lwt[sel], b=(2 * np.pi * nwind[sel, 0]) ** 2) / np.log(10) if sel.any() else -np.inf
    flag = 'ZERO(abs<1e-12)' if sa[-1] < 1e-12 else 'nonzero'
    print(f" {r:3d}  {sp[-1]:.3e}  {sp[0]:.3e} | {sa[-1]:.3e} {flag:16s}| {saw:.3e} | {best:.3e} | {lsaw:9.3f} | {-r*np.log10(16):8.3f}")
