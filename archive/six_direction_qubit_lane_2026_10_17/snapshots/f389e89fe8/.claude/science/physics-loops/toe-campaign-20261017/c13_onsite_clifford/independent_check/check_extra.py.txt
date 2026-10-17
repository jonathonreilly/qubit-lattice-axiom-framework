"""C13 independent check, extras:
 - the Majorana identities of item 4 (A = mu mu, Z = -i mu nu), all 720 orderings;
 - code dependence of the on-site action: with the action U^{(o0)}_R built
   from one code's ordering o0, which of the 60 codes are O-invariant?
"""
import itertools, json
from collections import Counter
from model import HalfEdge, ROTS, rot_order
from paulialg import mul, apply_clifford

info = json.load(open("codes.json"))["info"]
REPS = {sz: next(x for x in info if x["orbit_size"] == sz) for sz in (4, 6, 12)}

bad = 0
for o in itertools.permutations(range(6)):
    H = HalfEdge(4, o)
    for s in (0, 21):
        for a in range(3):
            t = H.lat.shift(s, a)
            if H.A(s, a) != mul(H.mu(s, a), H.mu(t, a + 3)):
                bad += 1
        for d in range(6):
            zz = mul(H.mu(s, d), H.nu(s, d))
            if (zz[0], zz[1], (zz[2] + 3) % 4) != (0, 1 << H.q(s, d), 0):
                bad += 1
print("Majorana identity failures (A = mu mu, Z_d = -i mu_d nu_d), 720 orderings:", bad)

for sz, rep in REPS.items():
    o0 = tuple(rep["rep"])
    H0 = HalfEdge(4, o0)
    acts = [H0.majorana_images(M) for M in ROTS]
    inv_codes = []
    for x in info:
        H = HalfEdge(4, tuple(x["rep"]))
        G = H.group((0, 0, 0))
        gens = [g for _, _, g in H.generators((0, 0, 0), sites=[0])]
        n_ok = sum(all(G.status(apply_clifford(g, *U)) == "in" for g in gens) for U in acts)
        inv_codes.append(n_ok)
    print(f"action built from orbit{sz} rep code{rep['code']}: rotations preserving each of the 60 codes "
          f"(sector 000): {dict(Counter(inv_codes))}; codes O-invariant under this one action: "
          f"{[i for i, n in enumerate(inv_codes) if n == 24]}")
