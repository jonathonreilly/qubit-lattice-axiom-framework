"""E3 (a): 3D icosahedral quasicrystal = cut-and-project model set from Z^6, spherical perpendicular window, density 1
(NOT the polyhedral-window Ammann-Kramer tiling).  Label-blind proper-distance coupling (R3 kernel, R = 1.8), boson m2 = 1.
Open patches; local stiffness density e''_i (E3_a_core, validated to 3e-7 on a Z^3 ball at buffer 4).
Outputs: interior mean per channel for several window offsets gamma (the hull average), the icosahedral-isotropy check
(E_g mean = T_2g mean predicted, since l = 2 is irreducible under I_h), and saved per-site data for the noise analysis.
A density-1 Poisson patch of the same size is computed identically for comparison.
usage: python3 E3_a1_quasicrystal.py"""
import numpy as np, time
import E3_a_core as q, e23_core as c
rng = np.random.default_rng(99)
BUF = 4.0
def gen_gamma():   # generic window offset, uniform in the ball |gamma| < 0.6 (the window radius is 0.62): patch is a generic hull piece
    while True:
        v = rng.uniform(-0.6, 0.6, 3)
        if np.linalg.norm(v) < 0.6:
            return v
jobs = [('qc', 9.0, gen_gamma()) for _ in range(6)] + [('qc', 11.0, gen_gamma()), ('poisson', 11.0, None)]
for k, (kind, Rp, gam) in enumerate(jobs):
    t0 = time.time()
    if kind == 'qc':
        X, perp = q.ico_patch(Rp, gam)
    else:
        X = rng.uniform(-Rp, Rp, (int((2 * Rp)**3), 3)); X = X[np.linalg.norm(X, axis=1) < Rp]; perp = np.zeros_like(X)
    e1, e2 = q.local_stiffness(X)
    m = np.linalg.norm(X, axis=1) < Rp - BUF
    msg = f"{kind} Rp={Rp} N={len(X)} interior={m.sum()} [{time.time()-t0:.0f}s]"
    for ch, idx in c.CH.items():
        v = e2[m][:, idx]
        msg += f" | {ch}: mean {v.mean():+.5f} (per-direction means {', '.join(f'{x:+.5f}' for x in v.mean(0))}) per-site sd {v.std():.4f}"
    msg += f" | stress mean {e1[m].mean():+.1e} per-site sd {e1[m].std():.4f}"
    print(msg, flush=True)
    np.savez(f"E3_a1_{k}_{kind}_R{Rp:.0f}.npz", X=X, perp=perp, e1=e1, e2=e2, Rp=Rp, buf=BUF)
