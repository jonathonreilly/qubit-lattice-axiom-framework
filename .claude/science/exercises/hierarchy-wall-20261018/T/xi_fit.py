"""decay length of the finished field: fit ln C(r) on r in [2, r_hi] where C > 0.01; slope of ln xi vs mu at large K.
Compare with Lemma C bound xi <= 2d e^2 e^{2d|mu|} (proved) and the KJMA grain picture xi ~ e^{mu/(d+1)} (comparator)."""
import sys, numpy as np
for fn in sys.argv[1:]:
    Z = np.load(fn); tK, MU, d, L = Z["tK"], Z["MU"], int(Z["d"]), int(Z["Lbig"])
    C = Z["C_big"]
    print(f"\n{fn}: d={d} L={L}")
    for it in (len(tK) - 1, len(tK) - 3, 5):
        xs = []
        for j, mu in enumerate(MU):
            c = C[it, j]; r = np.arange(len(c))
            ok = (r >= 2) & (c > 0.01) & (r <= L // 4)
            if ok.sum() >= 2:
                sl = np.polyfit(r[ok], np.log(c[ok]), 1)[0]
                xs.append(-1 / sl if sl < 0 else np.inf)
            else:
                xs.append(np.nan)
        xs = np.array(xs)
        good = np.isfinite(xs) & (xs < L / 8) & (MU >= 0)
        slope = np.polyfit(MU[good], np.log(xs[good]), 1)[0] if good.sum() >= 3 else np.nan
        print(f" t={tK[it]:.2f}: xi(mu) = {np.round(xs, 2).tolist()}")
        print(f"   d ln xi / d mu over mu>=0 with xi<L/8: {slope:.3f}  (KJMA 1/(d+1) = {1/(d+1):.3f}; Lemma C bound slope {2*d})")
