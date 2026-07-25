#!/usr/bin/env python3
"""KCPT Unit 26 runner.

Comm(D2) is a non-split central double cover of T @ B3, and End_Comm = C[D2].

This runner imports the Unit 25 module (same scripts/ directory) and reuses its
lattice / support / commutant / group construction verbatim.  Every gate here
DERIVES its quantity from that machinery and compares it against an independent
anchor constant.  A gate fails (and stays failing) whenever the derived object
disagrees with its anchor; nothing is computed from its own comparison target.

Theorems:
  T1  structure       kernel {+-1}, image I = T @ B3, |Comm| = 96 N.
  T2  double cover     non-split central extension 1 -> {+-1} -> Comm -> T@B3 -> 1;
                       derived subgroup = T_even @ A4 lifted.
  T3  bicommutant      End_Comm(C^N) = C[D2], dim 7, multiplicity-free.
"""

import os
import sys
import time
import itertools
import numpy as np
from collections import Counter

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import kcpt_d2_graded_signed_permutation_commutant_characterization_2026_07_25 as u25

# ---------------------------------------------------------------- gate harness
_P = [0]
_F = [0]


def gate(name, cond, msg=""):
    ok = bool(cond)
    if ok:
        _P[0] += 1
        print("  PASS  {:<26} {}".format(name, msg))
    else:
        _F[0] += 1
        print("  FAIL  {:<26} {}".format(name, msg))
    return ok


# ---------------------------------------------------------------- 3x3 helpers
def det3(A):
    return int(
        A[0, 0] * (A[1, 1] * A[2, 2] - A[1, 2] * A[2, 1])
        - A[0, 1] * (A[1, 0] * A[2, 2] - A[1, 2] * A[2, 0])
        + A[0, 2] * (A[1, 0] * A[2, 1] - A[1, 1] * A[2, 0])
    )


def mat_order(A):
    I3 = np.eye(3, dtype=int)
    B = A.copy()
    k = 1
    while not np.array_equal(B, I3):
        B = B @ A
        k += 1
        if k > 64:
            return -1
    return k


def mat_closure(gens):
    I3 = np.eye(3, dtype=int)
    seen = {I3.tobytes(): I3}
    frontier = [I3]
    while frontier:
        nf = []
        for X in frontier:
            for G in gens:
                Y = G @ X
                ky = Y.tobytes()
                if ky not in seen:
                    seen[ky] = Y
                    nf.append(Y)
        frontier = nf
    return seen


def reference_B3():
    mats = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            A = np.zeros((3, 3), dtype=int)
            for r in range(3):
                A[r, perm[r]] = signs[r]
            mats.append(A)
    return mats


def order_spectrum(mats):
    return dict(Counter(mat_order(A) for A in mats))


def det_set(mats):
    return set(det3(A) for A in mats)


# ---------------------------------------------------------------- lattice maps
def trans_perm(v, coords, idx, N):
    p = np.empty(N, dtype=np.int64)
    for i in range(N):
        x = coords[i]
        p[i] = idx(int(x[0] + v[0]), int(x[1] + v[1]), int(x[2] + v[2]))
    return p


def linear_perm(A, coords, idx, N):
    p = np.empty(N, dtype=np.int64)
    for i in range(N):
        y = A @ coords[i]
        p[i] = idx(int(y[0]), int(y[1]), int(y[2]))
    return p


def b3_coord(perm, coords, idx, L):
    """B3 coordinate of a permutation in I: strip translation, read the linear
    action on the three unit vectors, mapping coordinate value L-1 to -1."""
    t = coords[perm[0]] % L
    units = (idx(1, 0, 0), idx(0, 1, 0), idx(0, 0, 1))
    A = np.zeros((3, 3), dtype=int)
    for mu in range(3):
        img = (coords[perm[units[mu]]] - t) % L
        A[:, mu] = [(-1 if int(v) == L - 1 else int(v)) for v in img]
    return A


def linear_verified(perm, A, coords, idx, L, N):
    t = coords[perm[0]] % L
    for i in range(N):
        y = (A @ coords[i] + t) % L
        if int(perm[i]) != idx(int(y[0]), int(y[1]), int(y[2])):
            return False
    return True


# ---------------------------------------------------------------- group helpers
def commutator(a, b):
    return u25.compose(u25.compose(a, b), u25.compose(u25.sp_inv(a), u25.sp_inv(b)))


def derived_subgroup(gens):
    """Normal closure of the commutators of the generating set = [G, G]."""
    comms = [commutator(a, b) for a in gens for b in gens]
    D = u25.closure(comms)
    conj = list(gens) + [u25.sp_inv(g) for g in gens]
    for _ in range(12):
        extra = []
        for d in list(D.values()):
            for g in conj:
                c = u25.compose(u25.compose(u25.sp_inv(g), d), g)
                if u25.key(c) not in D:
                    extra.append(c)
        if not extra:
            break
        D = u25.closure(list(D.values()) + extra)
    return D


def eig_projectors(D2, N):
    """Return (ordered eigenvalues, dims, projectors) of the 7 D2-eigenspaces
    via the Hermitian operator i*D2."""
    H = 1j * D2.astype(complex)
    w, V = np.linalg.eigh(H)
    rw = np.round(w.real, 6)
    vals = sorted(set(rw.tolist()))
    dims = [int(np.sum(rw == v)) for v in vals]
    projs = []
    for v in vals:
        cols = np.where(rw == v)[0]
        Vk = V[:, cols]
        projs.append(Vk @ Vk.conj().T)
    return vals, dims, projs


def eig_characters(projs, P, S):
    """chi_k(U) = tr(U P_k) = sum_i S[i] * P_k[perm[i], i], over all U in Comm."""
    nComm, N = P.shape
    ar = np.arange(N)
    K = len(projs)
    chis = [np.empty(nComm, dtype=complex) for _ in range(K)]
    chunk = 2048
    for c0 in range(0, nComm, chunk):
        c1 = min(c0 + chunk, nComm)
        Pblk = P[c0:c1]
        Sblk = S[c0:c1].astype(complex)
        for k, Pk in enumerate(projs):
            vals = Pk[Pblk, ar[None, :]]
            chis[k][c0:c1] = np.sum(Sblk * vals, axis=1)
    return chis


# ---------------------------------------------------------------- anchor table
XREF = {
    4: dict(
        N=64, lam=[0, -4, -8, -12], mults=[8, 24, 24, 8],
        nComm=6144, nH=1536, nI=3072, nTrans=64, canon=48,
        invol=359, liftsq_minus=192, derived=768, abeln=8,
        pi_derived=384, even_size=32, minpoly_cs=[4, 8, 12], deg=7, ker=8,
        eigdims=[4, 12, 12, 8, 12, 12, 4], hcapc=768, dcap=192,
        d3_spectrum={1: 1, 2: 3, 3: 2}, a4_spectrum={1: 1, 2: 3, 3: 8},
        o_spectrum={1: 1, 2: 9, 3: 8, 4: 6}, full_hg=6144, hg_cap=3072,
    ),
    6: dict(
        N=216, lam=[0, -3, -6, -9], mults=[8, 48, 96, 64],
        nComm=20736, nH=5184, nI=10368, nTrans=216, canon=48,
        invol=799, liftsq_minus=400, derived=2592, abeln=8,
        pi_derived=1296, even_size=108, minpoly_cs=[3, 6, 9], deg=7, ker=8,
        eigdims=[32, 48, 24, 8, 24, 48,32], hcapc=2592, dcap=648,
        d3_spectrum={1: 1, 2: 3, 3: 2}, a4_spectrum={1: 1, 2: 3, 3: 8},
        o_spectrum={1: 1, 2: 9, 3: 8, 4: 6},
    ),
}

A_R4_ANCHOR = np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1]], dtype=int)


# ---------------------------------------------------------------- analysis
def analyze(L, refs):
    x = XREF[L]
    N = x["N"]
    print("\n[PHASE A] build L={} (N={})".format(L, N))
    lat = u25.build_lattice(L)
    coords, idx = lat["coords"], lat["idx"]
    D2, M = lat["D2"], lat["M"]
    lam = list(lat["lam"])
    mults = list(lat["mults"])
    sup = u25.support_structures(D2)
    ce = u25.enumerate_commutant(lat, sup)
    Comm = ce["Comm"]
    nComm = ce["nComm"]
    grp = u25.build_group(lat)
    H = grp["H"]
    nH = grp["nH"]
    g_r4 = u25.make_g_r4(lat)
    print("        nComm={} nH={} lam={} mults={}".format(nComm, nH, lam, mults))

    R = dict(N=N, lam=[int(v) for v in lam], mults=[int(v) for v in mults], nH=nH)

    # lift lookup: one representative per permutation image
    lift_of = {}
    for g in Comm.values():
        lift_of.setdefault(g[0].tobytes(), g)
    I_list = list(lift_of.values())
    nI = len(lift_of)
    R["nI"] = nI

    ar = np.arange(N)

    # kernel of the permutation-part map
    ker = [g for g in Comm.values() if np.array_equal(g[0], ar)]
    ker_signs = sorted(int(g[1][0]) for g in ker) if ker else []
    ker_const = all(np.all(g[1] == g[1][0]) for g in ker)
    R["ker_size"] = len(ker)
    R["ker_ok"] = (len(ker) == 2 and ker_const and ker_signs == [-1, 1])

    # translations present in I
    trans_present = 0
    trans_perms = {}
    for i in range(N):
        tp = trans_perm(coords[i], coords, idx, N)
        trans_perms[tp.tobytes()] = coords[i]
        if tp.tobytes() in lift_of:
            trans_present += 1
    R["trans_present"] = trans_present

    # canonical 0-fixing coset representatives = Stab_I(0)
    canon = [g[0] for g in I_list if int(g[0][0]) == 0]
    R["canon"] = len(canon)
    # linearity + B3 coordinate of each canonical rep
    A_set = {}
    lin_ok = 0
    for p in canon:
        A = b3_coord(p, coords, idx, L)
        if linear_verified(p, A, coords, idx, L, N):
            lin_ok += 1
        A_set[A.tobytes()] = A
    R["lin_ok"] = lin_ok
    R["A_set"] = set(A_set.keys())
    R["A_eq_ref"] = (set(A_set.keys()) == refs["B3"])
    # canonical reps closed under composition
    canon_bytes = set(p.tobytes() for p in canon)
    closed = True
    for pi in canon:
        for pj in canon:
            comp = pj[pi]
            if comp.tobytes() not in canon_bytes:
                closed = False
                break
        if not closed:
            break
    R["canon_closed"] = closed

    # T normal in I: conjugate every translation by the three linear reps
    A_cyc = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=int)
    A_swap = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]], dtype=int)
    A_flip = np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=int)
    lin_perms = [linear_perm(A, coords, idx, N) for A in (A_cyc, A_swap, A_flip)]
    normal_ok = True
    for lp in lin_perms:
        lpi = np.argsort(lp)
        for i in range(N):
            tp = trans_perm(coords[i], coords, idx, N)
            conj = lp[tp[lpi]]  # lp . t . lp^{-1} as permutation
            if conj.tobytes() not in trans_perms:
                normal_ok = False
                break
        if not normal_ok:
            break
    R["normal_ok"] = normal_ok

    # B3 as a matrix group: closure of the three generators
    B3_mat = mat_closure([A_cyc, A_swap, A_flip])
    R["B3_mat"] = len(B3_mat)
    R["B3_mat_eq_ref"] = (set(B3_mat.keys()) == refs["B3"])

    # structural generators: 3 translation lifts + 3 linear lifts + central -1
    central = (ar.copy(), -np.ones(N, dtype=np.int64))
    struct_gens = []
    gens_found = True
    for mu in range(3):
        e = np.zeros(3, dtype=int)
        e[mu] = 1
        tp = trans_perm(e, coords, idx, N)
        g = lift_of.get(tp.tobytes())
        if g is None:
            gens_found = False
        else:
            struct_gens.append(g)
    for lp in lin_perms:
        g = lift_of.get(lp.tobytes())
        if g is None:
            gens_found = False
        else:
            struct_gens.append(g)
    struct_gens.append(central)
    R["gens_found"] = gens_found
    if gens_found:
        clos = u25.closure(struct_gens)
        R["struct_closure"] = len(clos)
    else:
        R["struct_closure"] = -1

    # involutions in I and their lift-squares
    invol = 0
    liftsq_minus = 0
    same_sq = True
    for g in I_list:
        p = g[0]
        if np.array_equal(p, ar):
            continue
        if np.array_equal(p[p], ar):
            invol += 1
            s = g[1]
            sq = s * s[p]
            v0 = int(sq[0])
            if not np.all(sq == v0):
                same_sq = False
            if v0 == -1:
                liftsq_minus += 1
    R["invol"] = invol
    R["liftsq_minus"] = liftsq_minus
    R["same_sq"] = same_sq

    # derived subgroup [Comm, Comm]
    D = derived_subgroup(struct_gens) if gens_found else {}
    R["derived"] = len(D)
    R["abeln"] = (nComm // len(D)) if D else -1
    R["minus1_in_D"] = (u25.key(central) in D) if D else False
    piD = set()
    for d in D.values():
        piD.add(d[0].tobytes())
    R["pi_derived"] = len(piD)
    # translations inside pi(D)  ==  even-parity sublattice
    even_vs = set()
    for pb in piD:
        p = np.frombuffer(pb, dtype=np.int64)
        v = coords[p[0]]
        if np.array_equal(p, trans_perm(v, coords, idx, N)):
            even_vs.add(tuple(int(c) for c in v))
    ref_even = set(
        tuple(int(c) for c in coords[i]) for i in range(N) if int(coords[i].sum()) % 2 == 0
    )
    R["even_size"] = len(even_vs)
    R["even_eq"] = (even_vs == ref_even)
    # B3-image of derived = A4
    a4_mats = {}
    for pb in piD:
        p = np.frombuffer(pb, dtype=np.int64)
        A = b3_coord(p, coords, idx, L)
        a4_mats[A.tobytes()] = A
    a4_list = list(a4_mats.values())
    R["a4_order"] = len(a4_list)
    R["a4_spectrum"] = order_spectrum(a4_list)
    R["a4_dets"] = det_set(a4_list)
    R["a4_in_B3"] = all(k in refs["B3"] for k in a4_mats)

    # ---- T3: minimal polynomial of D2 (exact int64) ----
    cs = sorted(-l for l in lam if l != 0)
    R["cs"] = cs
    Iden = np.eye(N, dtype=np.int64)
    factors = [D2] + [M + c * Iden for c in cs]
    P = factors[0].copy()
    for f in factors[1:]:
        P = P @ f
    R["minpoly_zero"] = (not bool(np.any(P)))
    drop_nonzero = []
    for kk in range(len(factors)):
        Q = None
        for jj in range(len(factors)):
            if jj == kk:
                continue
            Q = factors[jj].copy() if Q is None else Q @ factors[jj]
        drop_nonzero.append(bool(np.any(Q)))
    R["drop_nonzero"] = drop_nonzero
    R["deg"] = 1 + 2 * len(cs)

    # dim End_Comm via the U25 character-sum machinery
    raw_dim, dim_end = u25.char_dim(Comm)
    R["dim_end"] = dim_end
    R["dim_end_raw"] = raw_dim
    # C[D2] subset End_Comm: spot-check a deterministic sample commutes with D2
    keys_sorted = sorted(Comm.keys())
    step = max(1, len(keys_sorted) // 500)
    sample = keys_sorted[::step]
    commute_ok = all(u25.commutes_with_D2(Comm[k], D2) for k in sample)
    R["commute_ok"] = commute_ok
    R["commute_sample"] = len(sample)

    # ker D2
    zero_idx = lam.index(0)
    R["ker_dim"] = int(mults[zero_idx])

    # eigenspace dims + projector characters
    vals, dims, projs = eig_projectors(D2, N)
    R["eigdims"] = dims
    R["eig_sum"] = int(sum(dims))
    P_arr, S_arr = u25.group_arrays(Comm)
    chis = eig_characters(projs, P_arr, S_arr)
    K = len(projs)
    cmat = np.empty((K, K), dtype=complex)
    for j in range(K):
        for k in range(K):
            cmat[j, k] = np.mean(chis[j] * np.conj(chis[k]))
    diag = np.real(np.diag(cmat))
    offmax = 0.0
    for j in range(K):
        for k in range(K):
            if j != k:
                offmax = max(offmax, abs(cmat[j, k]))
    R["char_diag_dev"] = float(np.max(np.abs(diag - 1.0)))
    R["char_offmax"] = float(offmax)
    R["char_K"] = K

    # ---- tie-backs: H cap Comm ----
    Hkeys = set(H.keys())
    Ckeys = set(Comm.keys())
    HcapC = Hkeys & Ckeys
    R["hcapc"] = len(HcapC)
    Dkeys = set(D.keys())
    R["dcap"] = len(Dkeys & HcapC)
    R["d_ne_hcapc"] = (Dkeys != HcapC)
    # body-diagonal dihedral D3
    d3_mats = {}
    for k in HcapC:
        p = Comm[k][0]
        A = b3_coord(p, coords, idx, L)
        d3_mats[A.tobytes()] = A
    d3_list = list(d3_mats.values())
    R["d3_order"] = len(d3_list)
    R["d3_spectrum"] = order_spectrum(d3_list)
    R["d3_dets"] = det_set(d3_list)
    R["d3_set"] = set(d3_mats.keys())
    R["d3_eq_ref"] = (set(d3_mats.keys()) == refs["D3"])

    # A_r4
    A_r4 = b3_coord(g_r4[0], coords, idx, L)
    R["a_r4"] = A_r4
    R["a_r4_eq"] = np.array_equal(A_r4, A_R4_ANCHOR)
    R["a_r4_in_B3"] = (A_r4.tobytes() in refs["B3"])
    R["a_r4_det"] = det3(A_r4)

    # O = <D3, A_r4>
    O_mat = mat_closure(d3_list + [A_r4])
    O_list = list(O_mat.values())
    R["o_order"] = len(O_list)
    R["o_spectrum"] = order_spectrum(O_list)
    R["o_dets"] = det_set(O_list)
    R["o_eq_ref"] = (set(O_mat.keys()) == refs["O"])

    # full-closure route (L=4 only)
    if L == 4:
        HG = u25.closure(grp["gens_H"] + [g_r4])
        R["full_hg"] = len(HG)
        HGkeys = set(HG.keys())
        HGcap = HGkeys & Ckeys
        R["hg_cap"] = len(HGcap)
        hg_A = set()
        for k in HGcap:
            hg_A.add(b3_coord(HG[k][0], coords, idx, L).tobytes())
        R["hg_route_eq"] = (hg_A == set(O_mat.keys()))

    return R


def run_gates(L, R):
    x = XREF[L]
    N = x["N"]
    print("\n[PHASE B] gates L={}".format(L))
    gate("SPECTRUM_L{}".format(L),
         R["lam"] == x["lam"] and R["mults"] == x["mults"] and R["nH"] == x["nH"],
         "lam={} (anchor {}), mults={} (anchor {}), |H|={} (anchor {})".format(
             R["lam"], x["lam"], R["mults"], x["mults"], R["nH"], x["nH"]))
    gate("STRUCT_L{}".format(L),
         R["nI"] == x["nI"] and R["ker_ok"],
         "|I|={} (anchor {}), ker(pi)={{+-1}} size {}".format(R["nI"], x["nI"], R["ker_size"]))
    gate("KERNEL_L{}".format(L),
         R["ker_ok"] and R["ker_size"] == 2,
         "kernel = {{+1,-1}} size {} (anchor 2)".format(R["ker_size"]))
    gate("TRANS_L{}".format(L),
         R["trans_present"] == x["nTrans"] and R["normal_ok"] and R["canon"] == x["canon"],
         "T present {}/{}, normal={}, |I/T|={} (anchor {})".format(
             R["trans_present"], x["nTrans"], R["normal_ok"], R["canon"], x["canon"]))
    gate("CANON_LINEAR_L{}".format(L),
         R["lin_ok"] == x["canon"] and R["A_eq_ref"] and R["canon_closed"],
         "linear {}/{}, A-set==B3 {}, closed {}".format(
             R["lin_ok"], x["canon"], R["A_eq_ref"], R["canon_closed"]))
    gate("B3GEN_L{}".format(L),
         R["B3_mat"] == 48 and R["B3_mat_eq_ref"],
         "<A_cyc,A_swap,A_flip> = {} == B3 {}".format(R["B3_mat"], R["B3_mat_eq_ref"]))
    gate("STRUCTGENS_L{}".format(L),
         R["gens_found"] and R["struct_closure"] == x["nComm"],
         "7-gen closure = {} (anchor 96N={}=2*{}*48)".format(
             R["struct_closure"], x["nComm"], x["nTrans"]))
    gate("INVOL_L{}".format(L),
         R["invol"] == x["invol"] and R["liftsq_minus"] == x["liftsq_minus"]
         and R["liftsq_minus"] > 0 and R["same_sq"],
         "involutions {} (anchor {}), lift-sq=-1 {} (anchor {})".format(
             R["invol"], x["invol"], R["liftsq_minus"], x["liftsq_minus"]))
    gate("DERIVED_L{}".format(L),
         R["derived"] == x["derived"] and R["abeln"] == x["abeln"],
         "|[Comm,Comm]|={} (anchor 12N={}), abelianization={} (anchor 8)".format(
             R["derived"], x["derived"], R["abeln"]))
    gate("MINUS1_DERIVED_L{}".format(L),
         R["minus1_in_D"],
         "-1 in [Comm,Comm] = {}".format(R["minus1_in_D"]))
    gate("PIDERIVED_L{}".format(L),
         R["pi_derived"] == x["pi_derived"],
         "|pi([Comm,Comm])|={} (anchor 6N={})".format(R["pi_derived"], x["pi_derived"]))
    gate("EVENSUB_L{}".format(L),
         R["even_size"] == x["even_size"] and R["even_eq"],
         "pi(D) cap T = even sublattice size {} (anchor N/2={}), set-eq {}".format(
             R["even_size"], x["even_size"], R["even_eq"]))
    gate("A4IMAGE_L{}".format(L),
         R["a4_order"] == 12 and R["a4_spectrum"] == x["a4_spectrum"]
         and R["a4_dets"] == {1} and R["a4_in_B3"],
         "B3-image(D) order {} spectrum {} dets {}".format(
             R["a4_order"], R["a4_spectrum"], R["a4_dets"]))
    gate("MINPOLY_L{}".format(L),
         R["minpoly_zero"] and all(R["drop_nonzero"]) and R["deg"] == x["deg"]
         and R["cs"] == x["minpoly_cs"],
         "D2*prod(M+cI)=0 {}, drop-one nonzero {}, deg {} cs {}".format(
             R["minpoly_zero"], R["drop_nonzero"], R["deg"], R["cs"]))
    gate("ENDCOMM_CD2_L{}".format(L),
         R["dim_end"] == 7 and R["deg"] == 7 and R["commute_ok"],
         "dim End_Comm={} == deg minpoly={} == dim C[D2]; commute-sample {}/{}".format(
             R["dim_end"], R["deg"], R["commute_sample"], R["commute_sample"]))
    gate("KERDIM_L{}".format(L),
         R["ker_dim"] == x["ker"],
         "dim ker D2 = {} (anchor 8)".format(R["ker_dim"]))
    gate("EIGDIMS_L{}".format(L),
         R["eigdims"] == x["eigdims"] and R["eig_sum"] == N,
         "eigenspace dims {} (anchor {}), sum {}".format(R["eigdims"], x["eigdims"], R["eig_sum"]))
    gate("CHARNORM_L{}".format(L),
         R["char_K"] == 7 and R["char_diag_dev"] <= 1e-9 and R["char_offmax"] <= 1e-12,
         "7 chars norm 1 (max dev {:.2e}), cross max {:.2e}".format(
             R["char_diag_dev"], R["char_offmax"]))
    gate("HCAPCOMM_L{}".format(L),
         R["hcapc"] == x["hcapc"] and R["dcap"] == x["dcap"] and R["d_ne_hcapc"],
         "|H cap Comm|={} (anchor 12N={}), |D cap (H cap Comm)|={} (anchor 3N={}), D!=HcapC {}".format(
             R["hcapc"], x["hcapc"], R["dcap"], x["dcap"], R["d_ne_hcapc"]))
    gate("D3_L{}".format(L),
         R["d3_order"] == 6 and R["d3_spectrum"] == x["d3_spectrum"]
         and R["d3_dets"] == {1} and R["d3_eq_ref"],
         "coords(H cap Comm) order {} spectrum {} dets {} bodydiag-eq {}".format(
             R["d3_order"], R["d3_spectrum"], R["d3_dets"], R["d3_eq_ref"]))
    gate("AR4_L{}".format(L),
         R["a_r4_eq"] and R["a_r4_in_B3"] and R["a_r4_det"] == 1,
         "A_r4 == [[0,1,0],[-1,0,0],[0,0,1]] {}, in B3 {}, det {}".format(
             R["a_r4_eq"], R["a_r4_in_B3"], R["a_r4_det"]))
    gate("OCLOSURE_L{}".format(L),
         R["o_order"] == 24 and R["o_spectrum"] == x["o_spectrum"]
         and R["o_dets"] == {1} and R["o_eq_ref"],
         "<D3,A_r4> order {} spectrum {} dets {} O-eq {}".format(
             R["o_order"], R["o_spectrum"], R["o_dets"], R["o_eq_ref"]))
    if L == 4:
        gate("FULLCLOSURE_L4",
             R["full_hg"] == x["full_hg"] and R["hg_cap"] == x["hg_cap"]
             and R["hg_route_eq"],
             "|<H,g_r4>|={} (anchor 6144), cap Comm={} (anchor |Comm|/2={}), route-eq {}".format(
                 R["full_hg"], R["hg_cap"], x["hg_cap"], R["hg_route_eq"]))


def main():
    t0 = time.time()
    print("=" * 72)
    print("KCPT U26  Comm(D2) double cover + End_Comm = C[D2]")
    print("=" * 72)
    B3ref = reference_B3()
    refs = {}
    refs["B3"] = set(A.tobytes() for A in B3ref)
    refs["O"] = set(A.tobytes() for A in B3ref if det3(A) == 1)
    diagv = np.array([1, 1, 1])
    refs["D3"] = set(
        A.tobytes() for A in B3ref
        if det3(A) == 1 and (np.array_equal(A @ diagv, diagv) or np.array_equal(A @ diagv, -diagv))
    )
    gate("REF_B3", len(refs["B3"]) == 48, "reference B3 size {}".format(len(refs["B3"])))
    gate("REF_O", len(refs["O"]) == 24, "reference O (det +1) size {}".format(len(refs["O"])))
    gate("REF_D3", len(refs["D3"]) == 6, "reference D3 (body-diagonal) size {}".format(len(refs["D3"])))

    results = {}
    for L in (4, 6):
        results[L] = analyze(L, refs)
        run_gates(L, results[L])

    print("\n[PHASE B] cross-L gates")
    gate("CROSSL_B3",
         results[4]["A_set"] == refs["B3"] and results[6]["A_set"] == refs["B3"]
         and results[4]["A_set"] == results[6]["A_set"],
         "A-set(L4)==A-set(L6)==B3 (48 matrices)")
    gate("CROSSL_D3",
         results[4]["d3_set"] == results[6]["d3_set"] and results[4]["d3_set"] == refs["D3"],
         "coords(H cap Comm) same 6 matrices at L=4 and L=6")

    print("\n" + "=" * 72)
    print("TOTAL: PASS={} FAIL={}".format(_P[0], _F[0]))
    print("wall-clock: {:.1f}s".format(time.time() - t0))
    sys.exit(0 if _F[0] == 0 else 1)


if __name__ == "__main__":
    main()
