"""Claims 1-4: validity of all 8 sign sectors, flux, bare-permutation action of
stabilizing rotations, mixed-sector control. Exact Pauli algebra with phases.

Usage: python3 check_sectors.py L [full]
  full: check every generator image (otherwise one translation representative
        per generator type, which suffices by translation covariance).
"""
import itertools
import sys
import time
from collections import Counter, defaultdict

from pauli_bksf import (Code, Lattice, Span, edge_perm, permute_pauli, pmul,
                        rotations, sign_vs_canonical, order_of)

L = int(sys.argv[1]) if len(sys.argv) > 1 else 4
FULL = len(sys.argv) > 2 and sys.argv[2] == "full"
lat = Lattice(L)
t0 = time.time()
SECTORS = list(itertools.product([0, 1], repeat=3))
ROTS = rotations()
PERMS = [edge_perm(lat, M) for M in ROTS]

# ---- 60 classes of orderings (span comparison) ----
classes = {}
order_class = {}
if L == 4:
    for order in itertools.permutations(range(6)):
        code = Code(lat, order)
        gens = [g for _, g in code.generators()]
        key = Span(gens, lat.n).canonical_basis()
        classes.setdefault(key, []).append(order)
    reps = [v[0] for v in classes.values()]
else:
    # reuse L=4 class representatives (cached) to save time
    import json
    reps = [tuple(r) for r in json.load(open("reps_L4.json"))]
print(f"L={L}: {len(reps)} classes ({time.time()-t0:.1f}s)")
if L == 4:
    import json
    json.dump([list(r) for r in reps], open("reps_L4.json", "w"))
    print("class sizes:", Counter(len(v) for v in classes.values()))

results = {}
fail = 0
mixed_fail_count = Counter()
orbit_type = Counter()
summary_rows = []
for ci, order in enumerate(reps):
    code = Code(lat, order)
    # --- hop signs / flux (claim 2) ---
    hs = code.hop_signs()
    for c in range(3):
        assert len(hs[c]) == 1, ("hop sign not translation invariant", order, c, hs[c])
        h = next(iter(hs[c]))
        assert h in (1, -1), ("hop product not Hermitian", order, c, h)
    h = tuple(next(iter(hs[c])) for c in range(3))
    # flux-0 sector: (-1)^{s_c} == h_c ; flux-pi: (-1)^{s_c} == -h_c
    s0 = tuple(0 if h[c] == 1 else 1 for c in range(3))
    spi = tuple(1 - s0[c] for c in range(3))
    flux = {}
    for s in SECTORS:
        flux[s] = tuple(0 if (h[c] * (-1) ** s[c]) == 1 else 1 for c in range(3))  # 1 = pi
    assert sum(1 for s in SECTORS if flux[s] == (0, 0, 0)) == 1
    assert sum(1 for s in SECTORS if flux[s] == (1, 1, 1)) == 1

    gens0 = code.generators((0, 0, 0))
    labels = [lab for lab, _ in gens0]
    paulis0 = [g for _, g in gens0]
    plaq_c = [lab[2] if lab[0] == "P" else -1 for lab in labels]
    sp = Span(paulis0, lat.n)
    # --- claim 1: validity of each sector via relation phases ---
    # phase of a relation in sector s = phase at s=0 times (-1)^{sum_c s_c * n_c}
    rel_data = []
    for rel in sp.relations:
        R = sp.product(rel)
        assert R[0] == 0 and R[1] == 0 and R[2] in (0, 2), R
        nc = [0, 0, 0]
        i = 0
        r = rel
        while r:
            if r & 1 and plaq_c[i] >= 0:
                nc[plaq_c[i]] += 1
            r >>= 1
            i += 1
        rel_data.append((1 if R[2] == 0 else -1, nc))
    valid = {}
    for s in SECTORS:
        ok = all(ph * (-1) ** sum(s[c] * nc[c] for c in range(3)) == 1 for ph, nc in rel_data)
        valid[s] = ok
    k = lat.n - sp.rank
    # --- claims 3,4: rotations ---
    if FULL:
        test_idx = list(range(len(paulis0)))
    else:
        base = [i for i, lab in enumerate(labels) if lab[1] == (0, 0, 0)]
        test_idx = base
    stab_rots = []
    needs_corr = defaultdict(list)  # sector -> list of rotation indices needing sign correction
    for ri, (M, perm) in enumerate(zip(ROTS, PERMS)):
        # unsigned invariance: every generator image in span
        combos = []
        inv = True
        for i in (range(len(paulis0)) if FULL else test_idx):
            img = permute_pauli(paulis0[i], perm)
            cb = sp.decompose(img)
            if cb is None:
                inv = False
                break
            if i in test_idx or FULL:
                combos.append((i, img, cb))
        if not inv:
            continue
        stab_rots.append(ri)
        for s in SECTORS:
            bad = False
            for i, img, cb in combos:
                prod = sp.product(cb)  # s=0 signed product
                # count plaquettes per orientation in combo
                nc = [0, 0, 0]
                j = 0
                r = cb
                while r:
                    if r & 1 and plaq_c[j] >= 0:
                        nc[plaq_c[j]] += 1
                    r >>= 1
                    j += 1
                sign_prod = sign_vs_canonical(prod) * (-1) ** sum(s[c] * nc[c] for c in range(3))
                # image of the signed generator in sector s
                sgn_gen = (-1) ** s[plaq_c[i]] if plaq_c[i] >= 0 else 1
                sign_img = sign_vs_canonical(img) * sgn_gen
                assert sign_prod in (1, -1) and sign_img in (1, -1)
                if sign_prod != sign_img:
                    bad = True
                    break
            if bad:
                needs_corr[s].append(ri)
    orders = sorted(order_of(ROTS[ri]) for ri in stab_rots)
    otype = {1: "orbit?", 6: "D3", 4: "order4", 2: "C2"}[len(stab_rots)]
    orbit_type[otype] += 1
    zero_ok = (s0 not in needs_corr)
    pi_ok = (spi not in needs_corr)
    for s in SECTORS:
        if s not in (s0, spi) and s in needs_corr:
            mixed_fail_count[flux[s]] += 1
    row = dict(order=order, h=h, s_flux0=s0, s_fluxpi=spi, valid_all=all(valid.values()),
               k=k, stab=len(stab_rots), type=otype, zero_ok=zero_ok, pi_ok=pi_ok,
               mixed_fail={str(flux[s]): (s in needs_corr) for s in SECTORS if s not in (s0, spi)})
    summary_rows.append(row)
    if not (row["valid_all"] and zero_ok and pi_ok):
        fail += 1
    print(ci, order, "h=", h, "flux0 s=", s0, "valid8=", row["valid_all"], "k=", k,
          "stab=", len(stab_rots), otype, "zero_ok=", zero_ok, "pi_ok=", pi_ok,
          "mixed needing corr:", sorted(str(flux[s]) for s in needs_corr if s not in (s0, spi)),
          f"({time.time()-t0:.0f}s)", flush=True)

print()
print("orbit types (by stabilizer order):", dict(orbit_type))
print("codes failing (invalid sector or flux-0/pi needing correction):", fail)
print("mixed sectors (labelled by flux pattern, 1 = pi): #codes needing a sign correction")
for f, cnt in sorted(mixed_fail_count.items()):
    print("  flux", f, ":", cnt)
print("set of flux-0 sector labels in my convention:", Counter(r["s_flux0"] for r in summary_rows))
print(f"done in {time.time()-t0:.0f}s")
