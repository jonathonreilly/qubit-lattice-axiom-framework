import sys, numpy as np
sys.path.insert(0, 'scripts')
import scale_ladder_gravity_regge_metric_universality_common_cone_2026_10_18 as R
U = np.ones(4); rng = np.random.default_rng(11)
for b in (0.3, -0.15):
    g0 = np.eye(4) + b*np.outer(U, U); Qe, _ = R.regge(g0)
    for _ in range(3):
        n = rng.standard_normal(3); n /= np.linalg.norm(n); km = rng.uniform(0.3, 1.2); ks = km*n
        kt = R.newton(lambda t: R.scalar(np.array([*ks, t]), g0), 1j*km)
        s_on = R.sv(Qe(np.array([*ks, kt]))); s_off = R.sv(Qe(np.array([*ks, 1.01*kt])))
        print(f"b={b:+.2f} k={km:.2f} on-shell sv5..7 " + " ".join(f"{x:.1e}" for x in s_on[4:7]) + "  off sv5..7 " + " ".join(f"{x:.1e}" for x in s_off[4:7]))
