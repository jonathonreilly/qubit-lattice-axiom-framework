"""B16 check 2j: mechanism for the staggered {G',C} defect. delta E = {E, G'[e0]} = -dG'/dA = -X^T E.
Compare |delta E| with |a d_0 E| on smooth transverse fields: an O(1) ratio growing like L means delta E has an
O(1)-relative (in units of E, not a dE) staggered component; contrast FWD. Measurement; PASS if STAG ratio ~ L^1 and FWD ~ L^0."""
from fractions import Fraction as Fr
import numpy as np
from chk_lat import Lat, uniform_timing
from chk1_timing import staggered
from chk1b_induced_generator import induced_generator, fwd_GA
from chk3_obstruction import sparse_gen
from chk3b_scaling import em_fields
res = {}
for name in ("FWD", "STAG"):
    res[name] = []
    for L in (8, 12, 16, 24):
        lat = Lat(L)
        X = fwd_GA(lat) if name == "FWD" else induced_generator(lat, *staggered(lat, 0), Fr(1))
        G = sparse_gen(lat, X, {b: (1 if b[1] == 0 else 0) for b in X})
        A, E, Fm = em_fields(lat)
        dE = -(G.T @ E)
        # reference: unit translation difference of E along e0 (central), same magnitude scale as a d_0 E
        sh = np.array([lat.lidx[(lat.sh(x, 0), j)] for (x, j) in lat.links])
        shm = np.array([lat.lidx[(lat.sh(x, 0, -1), j)] for (x, j) in lat.links])
        ref = -(E[sh] - E[shm]) / 2
        r = min(np.linalg.norm(dE - s * ref) for s in (1, -1)) / np.linalg.norm(ref)  # sign convention free
        res[name].append((L, r))
        print(f"  {name} L={L}: |dE - (-central d_0 E)| / |d_0 E| = {r:.4e}", flush=True)
sl = {k: np.polyfit(np.log([a for a, _ in v]), np.log([b for _, b in v]), 1)[0] for k, v in res.items()}
print("  slopes:", {k: round(v, 2) for k, v in sl.items()})
ok = abs(sl["STAG"] - 1) < 0.2 and sl["FWD"] < 0.2
print(("PASS" if ok else "FAIL") + ": C2j staggered G' moves E by an O(1) (in units of E) staggered amount -- its error relative to a d_0 E grows ~L -- while FWD's error stays bounded")
