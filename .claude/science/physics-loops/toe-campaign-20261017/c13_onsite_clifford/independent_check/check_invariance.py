"""C13 independent check, parts (1) and (2).

(1) For every code (all 60 classes, and all 720 orderings at L=4), every one of
    the 24 rotations, both uniform sectors: does site rotation + on-site
    Majorana signed permutation map the signed group to itself?
(2) Legitimacy of the on-site map (Hermiticity, anticommutation, homomorphism,
    translation covariance), and its identification with a CZ network
    composed with the bare permutation. Bare-action control.
"""
import itertools, json, random, sys, time
from model import (HalfEdge, Edge, ROTS, rot_dir, rot_order, classify_rotation,
                   compose_images)
from paulialg import (mul, prod, dag, is_herm, commutes, apply_clifford, X, Z,
                      SignedGroup, IDENT, pc)

random.seed(1)
info = json.load(open("codes.json"))["info"]
SECTORS = [(0, 0, 0), (1, 1, 1)]
REPS = {sz: next(x for x in info if x["orbit_size"] == sz) for sz in (4, 6, 12)}
results = {}


def log(*a):
    print(*a, flush=True)


def site0_gens(H, sector):
    return [g for _, _, g in H.generators(sector, sites=[0])]


def check_map(H, G, imgs, gens):
    """Return counts of statuses of images of gens."""
    c = {"in": 0, "minus": 0, "out": 0, "phase": 0}
    for g in gens:
        c[G.status(apply_clifford(g, *imgs))] += 1
    return c


# ------------------------------------------------------------ (2) legitimacy
log("== (2) legitimacy of the on-site map ==")
leg_fail = 0
for sz, rep in REPS.items():
    o = tuple(rep["rep"])
    H = HalfEdge(4, o)
    for M in ROTS:
        for trial in range(3):
            eps = [random.choice([1, -1]) for _ in range(6)]
            epsp = [random.choice([1, -1]) for _ in range(6)]
            iX, iZ = H.majorana_images(M, eps, epsp)
            # Pauli relations of the images on site 0's image site
            qs = list(range(6))  # site 0 qubits
            ims = [iX[q] for q in qs] + [iZ[q] for q in qs]
            for i in range(12):
                if not is_herm(ims[i]):
                    leg_fail += 1
                # square is +I
                sq = mul(ims[i], ims[i])
                if sq != IDENT:
                    leg_fail += 1
                for j in range(i + 1, 12):
                    want_anti = (j - i == 6)  # X_q vs Z_q same qubit
                    if commutes(ims[i], ims[j]) == want_anti:
                        leg_fail += 1
            # mu/nu images are what was asked: mu_d -> eps_d mu_{Rd}
            from paulialg import apply_clifford as ac
            rs = H.lat.rot_site(M, 0)
            for d in range(6):
                rd = rot_dir(M, d)
                m = ac(H.mu(0, d), iX, iZ)
                v = ac(H.nu(0, d), iX, iZ)
                tm = H.mu(rs, rd); tv = H.nu(rs, rd)
                if m != (tm[0], tm[1], (tm[2] + (0 if eps[d] > 0 else 2)) % 4):
                    leg_fail += 1
                if v != (tv[0], tv[1], (tv[2] + (0 if epsp[d] > 0 else 2)) % 4):
                    leg_fail += 1
            # homomorphism + hermiticity on random multi-site Paulis
            for _ in range(5):
                P = (random.getrandbits(H.n), random.getrandbits(H.n), random.randrange(4))
                Q = (random.getrandbits(H.n), random.getrandbits(H.n), random.randrange(4))
                if apply_clifford(mul(P, Q), iX, iZ) != mul(apply_clifford(P, iX, iZ), apply_clifford(Q, iX, iZ)):
                    leg_fail += 1
                Ph = P if is_herm(P) else (P[0], P[1], (P[2] + 1) % 4)
                if not is_herm(apply_clifford(Ph, iX, iZ)):
                    leg_fail += 1
                # translation covariance: phi(T_t P) = T_{Rt} phi(P)
                t = tuple(random.randrange(4) for _ in range(3))
                import numpy as np
                Rt = tuple(int(c) for c in M @ np.array(t))
                lhs = apply_clifford(H.translation(P, t), iX, iZ)
                rhs = H.translation(apply_clifford(P, iX, iZ), Rt)
                if lhs != rhs:
                    leg_fail += 1
log("legitimacy failures (Hermitian, square, (anti)commutation, mu/nu images, homomorphism, translation covariance):", leg_fail)
results["legitimacy_failures"] = leg_fail

# eps=eps'=1 map equals (on-site CZ network over pairs inverted between o, Ro) o bare permutation
cz_fail = 0
for o in itertools.permutations(range(6)):
    H = HalfEdge(4, o)
    for M in ROTS:
        Ro = rot_order(M, o)
        iX, iZ = H.majorana_images(M)
        bX, bZ = H.bare_images(M)
        pf = {d: i for i, d in enumerate(Ro)}
        pt = H.pos
        inv = [(d, e) for d in range(6) for e in range(d + 1, 6) if (pf[d] < pf[e]) != (pt[d] < pt[e])]
        partners = [0] * H.n
        for s in range(H.lat.N):
            for d, e in inv:
                partners[H.q(s, d)] ^= 1 << H.q(s, e)
                partners[H.q(s, e)] ^= 1 << H.q(s, d)
        cX = [(1 << q, partners[q], 0) for q in range(H.n)]
        cZ = [Z(q) for q in range(H.n)]
        U = compose_images((bX, bZ), (cX, cZ), H.n)
        for q in range(6 * 1):  # site 0 suffices by translation covariance (checked above)
            pass
        if any(U[0][q] != iX[q] or U[1][q] != iZ[q] for q in range(H.n)):
            cz_fail += 1
    if o == (0, 1, 2, 3, 4, 5):
        pass
log("eps=1 map == CZ-network o bare permutation: failures over 720 orderings x 24 rotations:", cz_fail)
results["cz_identity_failures"] = cz_fail

# ------------------------------------------------------------ (1) invariance
log("== (1) invariance ==")
# (a) full generator check, representatives, L = 4 and L = 6, eps = eps' = 1 and random admissible
for L in (4, 6):
    for sz, rep in REPS.items():
        o = tuple(rep["rep"])
        H = HalfEdge(L, o)
        for sec in SECTORS:
            gens = [g for _, _, g in H.generators(sec)]
            G = H.group(sec)
            assert not G.minus_one
            bad = 0; bare_bad = 0
            t0 = time.time()
            for M in ROTS:
                c = check_map(H, G, H.majorana_images(M), gens)
                bad += c["minus"] + c["out"] + c["phase"]
                cb = check_map(H, G, H.bare_images(M), gens)
                bare_bad += (cb["minus"] + cb["out"] + cb["phase"]) > 0
            stab_bare = 24 - bare_bad
            log(f"L={L} orbit{sz} code{rep['code']} o={o} sector={sec} log2dim={H.n - G.rank} "
                f"all-generator failures (eps=1, 24 R)={bad}; rotations preserving group under BARE map={stab_bare} "
                f"(expected |stab| = {24 // sz}) [{time.time() - t0:.1f}s]")
            results[f"full_L{L}_orb{sz}_sec{sec}"] = dict(fail=bad, bare_stab=stab_bare)

# (b) all 60 codes (rep ordering), L = 4 and L = 6, translation-reduced (site-0 generators)
for L in (4, 6):
    tot = 0; fails = 0
    for x in info:
        o = tuple(x["rep"])
        H = HalfEdge(L, o)
        for sec in SECTORS:
            G = H.group(sec)
            if G.minus_one or H.n - G.rank != 3:
                fails += 1
            gens = site0_gens(H, sec)
            for M in ROTS:
                c = check_map(H, G, H.majorana_images(M), gens)
                tot += 1
                fails += (c["minus"] + c["out"] + c["phase"]) > 0
    log(f"L={L}: all 60 codes x 2 sectors x 24 rotations (site-0 generators, eps=1): {tot} cases, failures {fails}")
    results[f"all60_L{L}"] = dict(cases=tot, fail=fails)

# (c) all 720 orderings, L = 4, translation-reduced
tot = 0; fails = 0
for o in itertools.permutations(range(6)):
    H = HalfEdge(4, o)
    for sec in SECTORS:
        G = H.group(sec)
        gens = site0_gens(H, sec)
        for M in ROTS:
            c = check_map(H, G, H.majorana_images(M), gens)
            tot += 1
            fails += (c["minus"] + c["out"] + c["phase"]) > 0
log(f"L=4: all 720 orderings x 2 sectors x 24 rotations: {tot} cases, failures {fails}")
results["all720_L4"] = dict(cases=tot, fail=fails)

# (d) mixed sectors control: which sectors survive? (eps=1, L=4, reps)
for sz, rep in REPS.items():
    o = tuple(rep["rep"])
    H = HalfEdge(4, o)
    row = {}
    for sec in itertools.product((0, 1), repeat=3):
        G = H.group(sec)
        gens = site0_gens(H, sec)
        ok = sum(1 for M in ROTS
                 if sum(v for k, v in check_map(H, G, H.majorana_images(M), gens).items() if k != "in") == 0)
        row[str(sec)] = ok
    log(f"orbit{sz}: rotations preserving signed group (eps=1) per sector:", row)
    results[f"sectors_orb{sz}"] = row

json.dump(results, open("check_invariance_results.json", "w"), indent=1)
