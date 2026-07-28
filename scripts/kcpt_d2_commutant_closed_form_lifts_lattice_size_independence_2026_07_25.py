#!/usr/bin/env python3
"""KCPT Unit 28 runner.

Closed-form lifts for Comm(D2), and how far the group law survives growing L.

Every prior unit in this lane read the structure of the signed-permutation
commutant Comm(D2) off an EXHAUSTIVE enumeration, which capped the lane at
L in {4, 6}.  This runner takes the enumeration off the critical path: the
translation sign fields are written down in CLOSED FORM from the staggered
phases, while the point-group permutations are built from scratch and their
sign fields are obtained constructively by BFS at five tested sizes.  The
enumeration is then used only as an independent anchor where it is affordable.

  T1  closed-form translation lift.  t_nu = (x -> x + e_nu, zeta_nu) with
      zeta_nu(x) = (-1)^{sum_{mu > nu} x_mu} lies in Comm(D2) for every even
      L >= 4; the sign solution with s(0) = +1 is unique, so exactly two lifts
      +-t_nu.  L = 2 is excluded because D2 cancels to zero there.
  T2  analytic commutator.  [t_a, t_b] = (-1)^{1 - delta_ab} I, whose
      bimultiplicative extension is beta(s,t) = (-1)^{(sum s)(sum t) - s.t}.
  T3  order and 2-torsion.  (t_nu)^k has sign field zeta_nu^k, order exactly L,
      (t_nu)^L = +I; q((L/2) v) = (-1)^{(L/2)^2 sum_{i<j} v_i v_j}.
  T4  constructive point-group lifts.  All 48 B_3 matrices lift, two lifts each.
  T5  size independence, exactly where it is exact.  96N constructed elements
      at each tested L; equality with Comm(D2) is anchored by the
      exhaustive enumeration at L in {4, 6, 8, 10} only, and is a LOWER BOUND
      at L = 12.

This runner imports the Unit 25 module (same scripts/ directory) and builds D2,
the support structures and the reference enumeration through it verbatim.  No
quantity is ever computed from the value it is compared against: the sign fields
come from the closed form or from BFS propagation over the D2 support graph, the
commutator signs come from actual signed-permutation products, and the
completeness gates carry explicit WRONG-VALUE REJECTORS (single-site sign flips,
the seven alternative exponent masks, and a determinant-1 integral shear that is
not a signed permutation) which must all fail to commute.
"""

import gc
import importlib
import itertools
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
for _p in (_HERE, "scripts"):
    if _p not in sys.path:
        sys.path.insert(0, _p)

u25 = importlib.import_module(
    "kcpt_d2_graded_signed_permutation_commutant_characterization_2026_07_25"
)

AUDIT_INPUT_PATHS = (
    "scripts/kcpt_d2_graded_signed_permutation_commutant_characterization_2026_07_25.py",
)

# ---------------------------------------------------------------- gate harness
_P = [0]
_F = [0]


def gate(name, cond, msg=""):
    ok = bool(cond)
    if ok:
        _P[0] += 1
        print("  PASS  {:<22} {}".format(name, msg), flush=True)
    else:
        _F[0] += 1
        print("  FAIL  {:<22} {}".format(name, msg), flush=True)
    return ok


# ------------------------------------------------------------------- constants
# Lattice sizes.  Constructive checks run everywhere; the exhaustive enumeration
# anchor runs only where it fits the memory budget.
L_ALL = (4, 6, 8, 10, 12)
L_ENUM = (4, 6, 8, 10)
L_CLOSURE = (4, 6)

# Regression anchors for the enumerated census.
#   ANCHOR_LIFT_PER_COSET : liftable automorphisms per translation coset.
#   ANCHOR_SUPPORT_STAB   : |Stab_0| inside the SUPPORT-GRAPH automorphism group.
# These are two different objects.  They agree for L >= 6, and they do NOT agree
# at L = 4, where the D2 support graph carries automorphisms beyond the affine
# ones and only the affine ones admit a sign lift.  The L = 4 and L = 6 values are
# the ones pinned in the landed Unit 25 module's own XREF table and gated there
# (L = 4: nStab = 720, nAut = 46080, nLift = 3072; L = 6: nStab = 48,
# nAut = nLift = 10368).  The L = 8 and L = 10 values are this unit's own
# measurements.  Independence comes from comparing the exact enumerator with
# the separate construction, not from treating these regression constants as
# external anchors.
ANCHOR_LIFT_PER_COSET = 48
ANCHOR_SUPPORT_STAB = {4: 720, 6: 48, 8: 48, 10: 48}
ANCHOR_SUPPORT_AUT = {4: 46080, 6: 10368, 8: 24576, 10: 48000}

SUBSETS3 = [(), (0,), (1,), (2,), (0, 1), (0, 2), (1, 2), (0, 1, 2)]

SHEAR = np.array([[1, 1, 0], [0, 1, 0], [0, 0, 1]], dtype=np.int64)


def build_b3():
    """The 48 signed 3x3 permutation matrices, built from scratch."""
    mats = []
    for perm in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            A = np.zeros((3, 3), dtype=np.int64)
            for r in range(3):
                A[r, perm[r]] = sg[r]
            mats.append(A)
    return mats


B3 = build_b3()


def det3(A):
    return int(
        A[0, 0] * (A[1, 1] * A[2, 2] - A[1, 2] * A[2, 1])
        - A[0, 1] * (A[1, 0] * A[2, 2] - A[1, 2] * A[2, 0])
        + A[0, 2] * (A[1, 0] * A[2, 1] - A[1, 1] * A[2, 0])
    )


def is_signed_perm_matrix(A):
    return (
        np.array_equal(np.abs(A).sum(axis=0), np.ones(3, dtype=np.int64))
        and np.array_equal(np.abs(A).sum(axis=1), np.ones(3, dtype=np.int64))
        and set(np.unique(A).tolist()) <= {-1, 0, 1}
    )


# ----------------------------------------------------- lattice-level machinery
def affine_perm(A, shift, lat):
    """Permutation of the site basis induced by x -> A x + shift (mod L)."""
    coords, idx, N = lat["coords"], lat["idx"], lat["N"]
    img = coords @ np.asarray(A, dtype=np.int64).T + np.asarray(shift, dtype=np.int64)
    out = np.empty(N, dtype=np.int64)
    for i in range(N):
        out[i] = idx(int(img[i, 0]), int(img[i, 1]), int(img[i, 2]))
    return out


def mask_sign_field(mask, coords):
    """(-1)^{sum_{mu in mask} x_mu} as an exact integer sign array."""
    ex = np.zeros(len(coords), dtype=np.int64)
    for mu in mask:
        ex = ex + coords[:, mu]
    return np.where(ex % 2 == 0, 1, -1).astype(np.int64)


def zeta_mask(nu):
    """The closed-form exponent mask {mu : mu > nu} for the nu-translation."""
    return tuple(mu for mu in range(3) if mu > nu)


def propagate(p, sup, D2):
    """Sign lift of the permutation p by BFS propagation from s(0) = +1.

    Uses the commutation condition s_i s_j D2[p_i, p_j] = D2[i, j] on the edges
    of the support-graph BFS spanning tree, i.e. s_j = s_i D2[i,j] D2[p_i,p_j].
    Returns None when a tree edge has no image edge (D2[p_i, p_j] = 0), which is
    an inconsistency of the propagation itself.
    """
    N = sup["N"]
    order = sup["order"]
    parent = sup["parent"]
    s = np.ones(N, dtype=np.int64)
    for j in order[1:]:
        j = int(j)
        i = int(parent[j])
        a = int(D2[i, j])
        b = int(D2[p[i], p[j]])
        if a == 0 or b == 0:
            return None
        s[j] = s[i] * a * b
    return s


def sp_identity(N):
    return (np.arange(N, dtype=np.int64), np.ones(N, dtype=np.int64))


def sp_minus_identity(N):
    return (np.arange(N, dtype=np.int64), -np.ones(N, dtype=np.int64))


def sp_pow(g, k, N):
    r = sp_identity(N)
    for _ in range(k):
        r = u25.compose(r, g)
    return r


def commutator(a, b):
    return u25.compose(u25.compose(a, b), u25.compose(u25.sp_inv(a), u25.sp_inv(b)))


def central_sign(g, N):
    """Return +-1 when g is a central scalar, else None."""
    p, s = g
    if not np.array_equal(p, np.arange(N, dtype=np.int64)):
        return None
    v = int(s[0])
    if not np.all(s == v):
        return None
    return v


def flip_sites(L, N):
    """Deterministic site set for the single-site sign-flip rejector.

    Exhaustive over all N sites at the two smallest lattices; a deterministic
    stride-(N//32) 32-site subset above that, to keep the wall time bounded.
    """
    if L in L_CLOSURE:
        return list(range(N)), True
    step = N // 32
    return [i * step for i in range(32)], False


def constructed_fingerprints(lat, pg_perms):
    """Injective fingerprints of the 48*N constructed permutation parts.

    The composite T_v o Lift_A has permutation part x -> A x + v; its images of
    the four probe sites 0, e_0, e_1, e_2 are packed into one int64 key.  Two
    distinct fingerprints certify two distinct permutations, so counting the
    distinct fingerprints is a sound lower-bound-and-equality count for the
    constructed set (no injectivity is assumed of the fingerprint map).
    """
    L, N, coords, idx = lat["L"], lat["N"], lat["coords"], lat["idx"]
    probes = [0]
    for k in range(3):
        e = [0, 0, 0]
        e[k] = 1
        probes.append(idx(e[0], e[1], e[2]))
    probes = np.array(probes, dtype=np.int64)
    fps = np.empty((len(pg_perms), N), dtype=np.int64)
    for a, pA in enumerate(pg_perms):
        base = coords[pA[probes]].astype(np.int64)            # (4, 3)
        img = (base[None, :, :] + coords[:, None, :]) % L      # (N, 4, 3)
        q = (img[:, :, 0] * L + img[:, :, 1]) * L + img[:, :, 2]
        fps[a] = ((q[:, 0] * N + q[:, 1]) * N + q[:, 2]) * N + q[:, 3]
        del base, img, q
    return fps


# ------------------------------------------------------------------- per-L run
def run_L(L):
    print("\n[L = {}]".format(L), flush=True)
    sfx = "L{}".format(L)

    lat = u25.build_lattice(L)
    N = lat["N"]
    D2 = lat["D2"]
    coords = lat["coords"]
    sup = u25.support_structures(D2)

    # ---------------------------------------------------- T1 closed-form lifts
    e3 = np.eye(3, dtype=np.int64)
    trans_perm = [affine_perm(e3, e3[nu], lat) for nu in range(3)]
    zeta = [mask_sign_field(zeta_mask(nu), coords) for nu in range(3)]
    tlift = [(trans_perm[nu], zeta[nu]) for nu in range(3)]

    g1 = [u25.commutes_with_D2(tlift[nu], D2) for nu in range(3)]
    gate("G1_TRANSLIFT_" + sfx, all(g1),
         "closed-form zeta_nu lift commutes with D2 on all {}^2 entries: {}/3"
         .format(N, sum(g1)))

    prop = [propagate(trans_perm[nu], sup, D2) for nu in range(3)]
    g2_match = [prop[nu] is not None and np.array_equal(prop[nu], zeta[nu])
                for nu in range(3)]
    g2_s0 = [prop[nu] is not None and int(prop[nu][0]) == 1 for nu in range(3)]
    gate("G2_UNIQUE_" + sfx,
         sup["connected"] and len(sup["order"]) == N
         and all(g2_match) and all(g2_s0) and all(g1),
         "support graph connected ({} sites), BFS propagation from s(0)=+1 "
         "reproduces zeta_nu exactly {}/3 -> sign solution unique, two lifts +-"
         .format(N, sum(g2_match)))

    # -------------------------------------------------- T2 analytic commutator
    beta_meas = np.zeros((3, 3), dtype=np.int64)
    beta_central = 0
    for a in range(3):
        for b in range(3):
            c = central_sign(commutator(tlift[a], tlift[b]), N)
            if c is not None:
                beta_central += 1
                beta_meas[a, b] = c
    beta_target = np.array([[(1 if a == b else -1) for b in range(3)]
                            for a in range(3)], dtype=np.int64)

    classes = [np.array(v, dtype=np.int64)
               for v in itertools.product((0, 1), repeat=3)]

    def beta_ext(s, t):
        r = 1
        for a in range(3):
            for b in range(3):
                if s[a] and t[b]:
                    r *= int(beta_meas[a, b])
        return r

    def beta_formula(s, t):
        return (-1) ** ((int(s.sum()) * int(t.sum()) - int(s @ t)) % 2)

    n_ext_ok = sum(1 for s in classes for t in classes
                   if beta_ext(s, t) == beta_formula(s, t))
    gate("G4_BETA_" + sfx,
         beta_central == 9 and np.array_equal(beta_meas, beta_target)
         and n_ext_ok == 64,
         "[t_a,t_b] central 9/9 and = -1 iff a!=b; bimultiplicative extension "
         "matches (-1)^[(sum s)(sum t) - s.t] on {}/64 class pairs"
         .format(n_ext_ok))

    if L in L_CLOSURE:
        reps = []
        for v in classes:
            g = sp_identity(N)
            for nu in range(3):
                if v[nu]:
                    g = u25.compose(g, tlift[nu])
            reps.append(g)
        n_prod_ok = 0
        n_prod_central = 0
        for i, s in enumerate(classes):
            for j, t in enumerate(classes):
                c = central_sign(commutator(reps[i], reps[j]), N)
                if c is not None:
                    n_prod_central += 1
                    if c == beta_ext(s, t) and c == beta_formula(s, t):
                        n_prod_ok += 1
        gate("G4X_LIFTPROD_" + sfx, n_prod_central == 64 and n_prod_ok == 64,
             "commutators of ACTUAL lift products on all 8x8 class reps are "
             "central {}/64 and match the extension {}/64"
             .format(n_prod_central, n_prod_ok))
        del reps

    # ---------------------------------------------- T3 order and 2-torsion (q)
    order_ok = True
    powsign_ok = 0
    ident = sp_identity(N)
    for nu in range(3):
        g = ident
        for k in range(1, L + 1):
            g = u25.compose(g, tlift[nu])
            is_id = (np.array_equal(g[0], ident[0]) and np.array_equal(g[1], ident[1]))
            if k < L and is_id:
                order_ok = False
            if k == L and not is_id:
                order_ok = False
            if np.array_equal(g[1], zeta[nu] ** k):
                powsign_ok += 1
    half = [sp_pow(tlift[nu], L // 2, N) for nu in range(3)]
    q_meas = {}
    q_form = {}
    for v in classes:
        g = ident
        for nu in range(3):
            if v[nu]:
                g = u25.compose(g, half[nu])
        q_meas[tuple(v.tolist())] = central_sign(u25.compose(g, g), N)
        pairs = int(v[0] * v[1] + v[0] * v[2] + v[1] * v[2])
        q_form[tuple(v.tolist())] = (-1) ** (((L // 2) ** 2 * pairs) % 2)
    q_agree = sum(1 for k in q_meas if q_meas[k] == q_form[k])
    q_minus = sorted(k for k in q_meas if q_meas[k] == -1)
    if L % 4 == 0:
        dich_ok = (q_minus == [])
        dich = "L=0 mod 4 -> q trivial on all 8 v"
    else:
        dich_ok = (q_minus == [(0, 1, 1), (1, 0, 1), (1, 1, 0), (1, 1, 1)])
        dich = "L=2 mod 4 -> q=-I on the four v with >=2 odd entries"
    gate("G6_ORDER_Q_" + sfx,
         order_ok and powsign_ok == 3 * L and q_agree == 8 and dich_ok,
         "(t_nu)^k sign field = zeta_nu^k {}/{}, order exactly {} with "
         "(t_nu)^L=+I; q matches formula 8/8; {}; q=-I set {}"
         .format(powsign_ok, 3 * L, L, dich, q_minus if q_minus else "empty"))

    # ------------------------------------------- G5 sign-dressing rejectors (a)
    sites, exhaustive = flip_sites(L, N)
    n_flip_rejected = 0
    n_flip_tested = 0
    for nu in range(3):
        for j in sites:
            s = zeta[nu].copy()
            s[j] = -s[j]
            n_flip_tested += 1
            if not u25.commutes_with_D2((trans_perm[nu], s), D2):
                n_flip_rejected += 1
    gate("G5A_FLIP_" + sfx, n_flip_rejected == n_flip_tested and n_flip_tested > 0,
         "single-site sign flips of zeta_nu break commutation {}/{} ({} site set"
         ", 3 nu)".format(n_flip_rejected, n_flip_tested,
                          "exhaustive N=" + str(N) if exhaustive
                          else "deterministic 32-site stride N//32"))

    # ------------------------------------------- G5 sign-dressing rejectors (b)
    n_mask_rejected = 0
    n_mask_tested = 0
    n_mask_correct_ok = 0
    for nu in range(3):
        good = zeta_mask(nu)
        for m in SUBSETS3:
            s = mask_sign_field(m, coords)
            ok = u25.commutes_with_D2((trans_perm[nu], s), D2)
            if m == good:
                if ok:
                    n_mask_correct_ok += 1
            else:
                n_mask_tested += 1
                if not ok:
                    n_mask_rejected += 1
    gate("G5B_MASK_" + sfx,
         n_mask_rejected == 21 and n_mask_tested == 21 and n_mask_correct_ok == 3,
         "the 7 alternative exponent masks per nu all break commutation {}/21; "
         "the mask {{mu : mu > nu}} commutes 3/3".format(n_mask_rejected))

    # ------------------------------------------- T4 constructive B_3 lifts (G7)
    pg_perms = []
    pg_lifts = []
    n_b3_lift = 0
    zero3 = np.zeros(3, dtype=np.int64)
    for A in B3:
        pA = affine_perm(A, zero3, lat)
        sA = propagate(pA, sup, D2)
        if sA is not None and u25.commutes_with_D2((pA, sA), D2):
            n_b3_lift += 1
            pg_perms.append(pA)
            pg_lifts.append((pA, sA))
    n_pg_distinct = len({p.tobytes() for p in pg_perms})
    gate("G7_B3_" + sfx,
         n_b3_lift == 48 and n_pg_distinct == 48 and sup["connected"],
         "all 48 B_3 matrices lift by consistent sign propagation {}/48, "
         "48 distinct permutation parts; connected support graph -> exactly two "
         "lifts +- each".format(n_b3_lift))

    # --------------------------------------------------- G8 non-B_3 rejector
    p_sh = affine_perm(SHEAR, zero3, lat)
    sh_bijection = (len(set(p_sh.tolist())) == N)
    s_sh = propagate(p_sh, sup, D2)
    sh_commutes = (s_sh is not None and u25.commutes_with_D2((p_sh, s_sh), D2))
    gate("G8_SHEAR_" + sfx,
         sh_bijection and det3(SHEAR) == 1 and not is_signed_perm_matrix(SHEAR)
         and not sh_commutes,
         "shear [[1,1,0],[0,1,0],[0,0,1]] det=1, lattice bijection, not a signed "
         "permutation: propagation {} -> NOT liftable"
         .format("inconsistent" if s_sh is None else "consistent but commutation fails"))

    # ---------------------------------------------- G9 constructed element count
    fps = constructed_fingerprints(lat, pg_perms)
    n_fp = int(np.unique(fps).size)
    del fps
    constructed = 2 * 48 * N
    gc.collect()

    # --------------------------------------- exhaustive-enumeration anchor block
    enum = None
    if L in L_ENUM:
        ce = u25.enumerate_commutant(lat, sup)
        Comm = ce["Comm"]
        nStab, nAut = ce["nStab"], ce["nAut"]
        nLift, nComm = ce["nLift"], ce["nComm"]
        enum = (nStab, nAut, nLift, nComm)

        pn = 8 * N
        targets = {}
        for nu in range(3):
            targets[trans_perm[nu].tobytes()] = ("t", nu)
        for a, pA in enumerate(pg_perms):
            targets.setdefault(pA.tobytes(), ("A", a))
        counts = dict.fromkeys(targets, 0)
        for k in Comm:
            pref = k[:pn]
            if pref in counts:
                counts[pref] += 1

        n_t_in = 0
        n_t_two = 0
        for nu in range(3):
            b = trans_perm[nu].tobytes()
            if (u25.key(tlift[nu]) in Comm
                    and u25.key((trans_perm[nu], -zeta[nu])) in Comm):
                n_t_in += 1
            if counts[b] == 2:
                n_t_two += 1
        gate("G3_ENUM_" + sfx, n_t_in == 3 and n_t_two == 3,
             "closed-form t_nu and -t_nu both present in the enumerated Comm "
             "{}/3, and the enumerated lifts of that permutation are exactly "
             "two {}/3".format(n_t_in, n_t_two))

        n_A_in = 0
        n_A_two = 0
        for pA, sA in pg_lifts:
            if u25.key((pA, sA)) in Comm and u25.key((pA, -sA)) in Comm:
                n_A_in += 1
            if counts[pA.tobytes()] == 2:
                n_A_two += 1
        gate("G7E_ENUM_" + sfx, n_A_in == 48 and n_A_two == 48,
             "each constructed point-group lift and its negative lie in the "
             "enumerated Comm key set {}/48, with exactly two enumerated lifts "
             "each {}/48".format(n_A_in, n_A_two))

        gate("G9S_SUPPORT_" + sfx,
             nStab == ANCHOR_SUPPORT_STAB[L] and nAut == ANCHOR_SUPPORT_AUT[L]
             and nAut == nStab * N and nLift <= nAut
             and nLift == ANCHOR_LIFT_PER_COSET * N,
             "support-graph Aut census nStab={} nAut={} (=nStab*N); liftable "
             "nLift={} = 48N{}".format(
                 nStab, nAut, nLift,
                 "; support-graph Aut is STRICTLY LARGER than the liftable "
                 "subgroup here ({} > {})".format(nAut, nLift) if nAut > nLift
                 else "; support-graph Aut equals the liftable subgroup"))

        gate("G9_COUNTS_" + sfx,
             n_pg_distinct == 48 and n_fp == 48 * N and constructed == 96 * N
             and nComm == 96 * N and nLift == 48 * N and nComm == 2 * nLift
             and constructed == nComm,
             "constructed {} distinct fingerprints x 2 signs = {} = 96N; "
             "enumerated nComm={} = 96N = constructed (EXACT equality)"
             .format(n_fp, constructed, nComm))

        if L in L_CLOSURE:
            gens = list(tlift) + [sp_minus_identity(N)] + list(pg_lifts)
            clos = u25.closure(gens)
            gate("G10_CLOSURE_" + sfx,
                 len(clos) == 96 * N and clos.keys() == Comm.keys(),
                 "closure of {{t_x,t_y,t_z,-I}} + 48 point-group lifts ({} gens)"
                 " has order {} and key set EQUAL to the enumerated Comm"
                 .format(len(gens), len(clos)))
            del clos, gens

        del Comm, ce, counts, targets
        gc.collect()
    else:
        gate("G9_COUNTS_" + sfx,
             n_pg_distinct == 48 and n_fp == 48 * N and constructed == 96 * N,
             "constructed {} distinct fingerprints x 2 signs = {} = 96N: this is"
             " a LOWER BOUND |Comm(D2)| >= 96N (no enumeration run at L={})"
             .format(n_fp, constructed, L))

    row = dict(L=L, N=N, constructed=constructed, n_fp=n_fp, enum=enum,
               q_minus=q_minus, flips=(n_flip_rejected, n_flip_tested, exhaustive))

    del lat, sup, D2, coords, trans_perm, zeta, tlift, prop, pg_perms, pg_lifts
    del half, p_sh, s_sh
    gc.collect()
    return row


def main():
    print("KCPT Unit 28 -- closed-form lifts and lattice-size independence")
    print("D2, support structures and the reference enumeration come from "
          "scripts/kcpt_d2_graded_signed_permutation_commutant_characterization"
          "_2026_07_25.py")
    print("constructive L = {}; exhaustive-enumeration anchor L = {}"
          .format(L_ALL, L_ENUM))

    l2 = u25.build_lattice(2)
    l2_sup = u25.support_structures(l2["D2"])
    gate(
        "SCOPE_L2_DEGENERATE",
        np.count_nonzero(l2["D2"]) == 0 and not l2_sup["connected"],
        "L=2 forward/backward neighbours coincide, D2 cancels to zero, "
        "and lift uniqueness is excluded",
    )
    del l2, l2_sup

    rows = []
    for L in L_ALL:
        rows.append(run_L(L))

    print("\n[SUMMARY]")
    print("  {:>3} {:>5} {:>8} {:>10} {:>8} {:>8} {:>8}  {}"
          .format("L", "N", "constr", "nComm", "nLift", "nStab", "nAut", "q=-I set"))
    for r in rows:
        if r["enum"] is None:
            print("  {:>3} {:>5} {:>8} {:>10} {:>8} {:>8} {:>8}  {}"
                  .format(r["L"], r["N"], r["constructed"], ">= " + str(96 * r["N"]),
                          "-", "-", "-", r["q_minus"] if r["q_minus"] else "empty"))
        else:
            nStab, nAut, nLift, nComm = r["enum"]
            print("  {:>3} {:>5} {:>8} {:>10} {:>8} {:>8} {:>8}  {}"
                  .format(r["L"], r["N"], r["constructed"], nComm, nLift, nStab,
                          nAut, r["q_minus"] if r["q_minus"] else "empty"))

    print("\n[CROSS-L]")
    gate("XL_96N", all(r["constructed"] == 96 * r["N"] for r in rows),
         "constructed count = 96N at every L in {}".format(L_ALL))
    gate("XL_ENUM_EQ",
         all(r["enum"][3] == 96 * r["N"] and r["enum"][2] == 48 * r["N"]
             for r in rows if r["enum"] is not None),
         "enumerated nComm = 96N and nLift = 48N at every L in {} "
         "(equality with the construction is anchored ONLY here)".format(L_ENUM))
    gate("XL_DICHOTOMY",
         all((r["q_minus"] == []) == (r["L"] % 4 == 0) for r in rows)
         and all(r["q_minus"] == [(0, 1, 1), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
                 for r in rows if r["L"] % 4 == 2),
         "2-torsion dichotomy holds at every L: q trivial for L=0 mod 4, "
         "q=-I on exactly 4 points for L=2 mod 4")

    print("\n" + "=" * 72)
    print("TOTAL: PASS={} FAIL={}".format(_P[0], _F[0]))
    sys.exit(0 if _F[0] == 0 else 1)


if __name__ == "__main__":
    main()
