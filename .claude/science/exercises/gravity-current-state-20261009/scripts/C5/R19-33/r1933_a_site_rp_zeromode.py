"""R19-33 (a) IR control: repeat the O(kappa^2) site-RP linear-sector test with K = pseudo-inverse of
-Delta_3 on the torus (zero mode removed; K no longer entrywise >= 0), and with the bridge sign
flipped (repulsive), to show (i) the K2-GR failure is not an IR/zero-mode artifact, (ii) attraction is
the RP-compatible sign of the Newton term."""
import numpy as np, importlib.util, sys
spec = importlib.util.spec_from_file_location("s", __file__.replace("_zeromode", "")); s = importlib.util.module_from_spec(spec)
sys.argv = ["x"]; src = open(__file__.replace("_zeromode", "")).read().split("rng = np.random.default_rng(5)")[0]
exec(src, s.__dict__)
rng = np.random.default_rng(9)
for phi0_kind in ("zero", "const", "random"):
    print("== phi_0 = %s, K = pinv(-Delta_3) (zero mode removed) ==" % phi0_kind)
    for L in (3, 4, 5, 6):
        for m in (1.0, 0.25):
            R, C1, Lap, idx = s.half_chain(L, m); N = L ** 3
            phi0 = np.zeros(N) if phi0_kind == "zero" else (np.ones(N) if phi0_kind == "const" else rng.normal(size=N))
            mu = R @ phi0 - phi0
            K = np.linalg.pinv(Lap)
            u, A_s = s.slice_quantities(phi0, L, m, idx)
            row = []
            for disc in ("K2", "D2"):
                for br in ("Newton", "GR"):
                    w = K @ (u + A_s) if br == "GR" else K @ u
                    M = s.M2_linear(mu, C1, K, w, disc, br)
                    e = np.linalg.eigvalsh(M)
                    row.append("%s-%s %+.2e/%+.2e" % (disc, br, e[0], e[-1]))
            # repulsive Newton (sign flip), K2 and D2, at the screened K of the main run
            Ks = np.linalg.inv(Lap + 0.09 * np.eye(N))
            for disc in ("K2", "D2"):
                Mr = -s.M2_linear(mu, C1, Ks, Ks @ u, disc, "Newton")
                row.append("%s-Newton-REPULSIVE min %+.2e" % (disc, np.linalg.eigvalsh(Mr)[0]))
            print(" L=%d m=%.2f :: " % (L, m) + " | ".join(row))
