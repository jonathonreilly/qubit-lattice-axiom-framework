#!/usr/bin/env python3
"""KCPT Unit 27 — restriction localization of the Unit-26 central double-cover
extension class 1 -> {+-I} -> Comm(D2) -> T x| B3 -> 1, on the staggered lattices
L in {4, 6} (N = L^3 = 64, 216); |Comm| = 96N.

Claims re-derived independently here (all statements exact; verified at both L;
labels match the paired note):
  T1  restriction dichotomy: the class SPLITS over the entire point-group side
      (B3 order 48, O 24, A4 12, D3 6) via an explicit -I-free section subgroup S
      with pi|S bijective onto B3; and is NON-SPLIT over every translation-
      containing subgroup tested (T, T_even, T_even x| A4), certified by
      -I in K := <squares u commutators of the preimage>.
  T2  the translation commutator form beta(s,t) := [s~, t~] in {+-I} is central,
      bimultiplicative, alternating, B3-invariant, with closed form
      beta(s,t) = (-1)^{(sum s)(sum t) - s.t} and unit matrix [[1,-1,-1],...];
      among all 512 bimultiplicative {+-1}-forms on T/2T = F2^3 exactly 8 are
      alternating, 2 of those point-group invariant, and the unique nontrivial
      invariant one equals the measured beta -- each of the other 511 candidates
      (including the trivial all-+1 form) is rejected by an explicit wrong-value
      witness pair.
  T3  unit-translation lifts have order exactly L with (t~_mu)^L = +I; the
      2-torsion square class q((L/2)v) = (-1)^{(L/2)^2 sum_{i<j} v_i v_j} is
      trivial at L=4 and nontrivial at L=6 on {(3,3,0),(3,0,3),(0,3,3),(3,3,3)}.
  T4  Comm = T~ x| S internally (S = B3): T~ normal, T~ cap S = {+I}, and the
      product set T~*S equals Comm elementwise (96N distinct products), so the
      failure to split is already witnessed by T~ = pi^{-1}(T).
  T5  derived-cover identification: pi^{-1}(T_even x| A4) = [Comm, Comm] as a
      key-set equality (order 12N), the internal shadow of Unit 26's derived-
      subgroup double cover.

All group-theoretic decisions (composition, membership, closure, order,
commutator, square, section) use EXACT integer signed-permutation arithmetic on
elements (perm int64[N], sign int64[N]); floating point enters ONLY the
independent D2-spectrum anchor gate G20 (tolerance 1e-9).

This runner imports the landed Unit-25 enumeration module
`kcpt_d2_graded_signed_permutation_commutant_characterization_2026_07_25.py` as a
sibling (for build_lattice / support_structures / enumerate_commutant / compose /
key / closure / find_generators / sp_inv only). Every other helper
(trans_perm, linear_perm, b3_coord, det3, mat_closure, reference groups,
commutator, derived subgroup, K-computation, beta) is written fresh below,
adapted from the Unit-26 runner but NOT imported from it.
"""
import os
import sys
import time
import itertools
import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import kcpt_d2_graded_signed_permutation_commutant_characterization_2026_07_25 as u25


# ---------------------------------------------------------------- gate harness
_P = [0]
_F = [0]


def gate(name, cond, msg=""):
    ok = bool(cond)
    (_P if ok else _F)[0] += 1
    print("  {:4s}  {:46s}  {}".format("PASS" if ok else "FAIL", name, msg))
    return ok


# ---------------------------------------------------------------- XREF anchors
# External, exact integer anchors (from Unit-25/26 landed/inflight values and the
# two U27 recon probes). Gated, never used as a computation source.
XREF = {
    4: dict(N=64, nComm=6144, eig=[0, -4, -8, -12], mults=[8, 24, 24, 8],
            Ttilde=128, S=48, K_T=16, K_Teven=8, K_TevenA4=768,
            twoT=8, TevA4_down=384, comm_comm=768, q_minus=0),
    6: dict(N=216, nComm=20736, eig=[0, -3, -6, -9], mults=[8, 48, 96, 64],
            Ttilde=432, S=48, K_T=54, K_Teven=54, K_TevenA4=2592,
            twoT=27, TevA4_down=1296, comm_comm=2592, q_minus=4),
}


# ---------------------------------------------------------------- 3x3 helpers
def det3(A):
    return int(
        A[0, 0] * (A[1, 1] * A[2, 2] - A[1, 2] * A[2, 1])
        - A[0, 1] * (A[1, 0] * A[2, 2] - A[1, 2] * A[2, 0])
        + A[0, 2] * (A[1, 0] * A[2, 1] - A[1, 1] * A[2, 0])
    )


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
    """3x3 signed-permutation matrix of a 0-fixing linear permutation: strip the
    translation, read the images of the three unit vectors (value L-1 -> -1)."""
    t = coords[perm[0]] % L
    units = (idx(1, 0, 0), idx(0, 1, 0), idx(0, 0, 1))
    A = np.zeros((3, 3), dtype=int)
    for mu in range(3):
        img = (coords[perm[units[mu]]] - t) % L
        A[:, mu] = [(-1 if int(w) == L - 1 else int(w)) for w in img]
    return A


# ---------------------------------------------------------------- group helpers
def commutator(a, b):
    """Central-kernel commutator of two Comm elements.

    We use the Unit-26 convention compose(compose(a,b), compose(a^-1,b^-1)),
    which realizes the operator word b^-1 a^-1 b a. This differs from the literal
    a^-1 b^-1 a b by an inverse (an a<->b swap). Every use below reads ONLY
    membership in / the +-1 value within the central kernel {+-I}; since +I and
    -I are each self-inverse, that value is identical for both conventions, so the
    choice is immaterial to all gates.
    """
    return u25.compose(u25.compose(a, b), u25.compose(u25.sp_inv(a), u25.sp_inv(b)))


def derived_subgroup(gens):
    """[G, G] as the normal closure of the commutators of a generating set."""
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


def perm_closure(gen_perms, N):
    """Closure of a set of permutation arrays under composition (perm-only)."""
    idp = np.arange(N, dtype=np.int64)
    seen = {idp.tobytes(): idp}
    stack = [idp]
    while stack:
        g = stack.pop()
        for h in gen_perms:
            c = h[g]                      # perm part of compose(g, h)
            ky = c.tobytes()
            if ky not in seen:
                seen[ky] = c
                stack.append(c)
    return seen


def generated_subgroup(elements, N):
    """<elements> as a Comm-subgroup, via a deterministic reduced generating set
    (greedy over sorted keys) so the closure stays cheap even when the candidate
    list is large (e.g. all squares of a 2592-element preimage)."""
    cand = {}
    for g in elements:
        cand[u25.key(g)] = g
    idg = (np.arange(N, dtype=np.int64), np.ones(N, dtype=np.int64))
    id_key = u25.key(idg)
    gens = []
    cur = {id_key}
    curdict = {id_key: idg}
    for ky in sorted(cand.keys()):
        if ky in cur:
            continue
        gens.append(cand[ky])
        curdict = u25.closure(gens)
        cur = set(curdict.keys())
    return curdict


def K_subgroup(E_elems, witness_pairs, N):
    """K := <squares(E) u commutators(E)>. Since E/E^2 is elementary abelian,
    [E,E] <= E^2, so this equals <squares(E)> = E^2; we still feed the explicit
    witness commutators into the generator pool (they lie in E^2 anyway) to keep
    the construction faithful to the stated definition. Returns (Kdict, wit) where
    wit maps each labelled witness pair to its central value key."""
    cand = [u25.compose(g, g) for g in E_elems]
    wit = {}
    for label, (a, b) in witness_pairs.items():
        c = commutator(a, b)
        cand.append(c)
        wit[label] = u25.key(c)
    K = generated_subgroup(cand, N)
    return K, wit


# ---------------------------------------------------------------- beta form
def beta_formula(s, t):
    """Closed form (-1)^{(sum s)(sum t) - s.t}."""
    e = (sum(s) * sum(t) - sum(a * b for a, b in zip(s, t))) % 2
    return -1 if e else 1


def betaM(M, u, v):
    """Bimultiplicative F2-form (-1)^{u^T M v} for a 3x3 matrix M over F2."""
    e = 0
    for i in range(3):
        mi = M[i]
        ui = u[i]
        if ui:
            for j in range(3):
                e += mi[j] * v[j]
    return -1 if (e & 1) else 1


# ---------------------------------------------------------------- reference pts
def build_reference_groups():
    A_cyc = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=int)
    A_swap = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]], dtype=int)
    A_flip = np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=int)
    B3 = mat_closure([A_cyc, A_swap, A_flip])
    B3ref = set(B3.keys())
    Oref = set(k for k, A in B3.items() if det3(A) == 1)
    O_mats = [B3[k] for k in Oref]
    comm_mats = [A @ Bm @ A.T @ Bm.T for A in O_mats for Bm in O_mats]  # orth: inv=T
    A4ref = set(mat_closure(comm_mats).keys())
    # D3: body-diagonal S3 in O (det +1 preserving (1,1,1) up to sign). The
    # +-allowing definition is used; its order is reported by the caller's gate.
    diagv = np.array([1, 1, 1])
    D3ref = set(
        k for k, A in B3.items()
        if det3(A) == 1 and (np.array_equal(A @ diagv, diagv)
                             or np.array_equal(A @ diagv, -diagv))
    )
    return dict(A_cyc=A_cyc, A_swap=A_swap, A_flip=A_flip,
                B3=B3ref, O=Oref, A4=A4ref, D3=D3ref)


# ---------------------------------------------------------------- per surface
def run_L(L, refs):
    x = XREF[L]
    N = L ** 3
    print("\n" + "=" * 72)
    print("L = {}  (N = {})".format(L, N))
    print("=" * 72)
    t0 = time.time()
    tag = "L{}".format(L)

    lat = u25.build_lattice(L)
    coords, idx = lat["coords"], lat["idx"]
    D2 = lat["D2"]
    M = lat["M"]
    sup = u25.support_structures(D2)
    ce = u25.enumerate_commutant(lat, sup)
    Comm = ce["Comm"]
    nComm = ce["nComm"]

    idg = (np.arange(N, dtype=np.int64), np.ones(N, dtype=np.int64))
    central = (np.arange(N, dtype=np.int64), -np.ones(N, dtype=np.int64))
    id_key = u25.key(idg)
    m_key = u25.key(central)

    # perm -> canonical (first-seen) lift, dict insertion order of Comm
    lift_of = {}
    for g in Comm.values():
        lift_of.setdefault(g[0].tobytes(), g)
    comm_perm_bytes = set(lift_of.keys())

    # ---- G1: sizes
    gate(tag + ".G1.N_is_Lcubed", N == L ** 3, "N={} L^3={}".format(N, L ** 3))
    gate(tag + ".G1.nComm_96N", nComm == 96 * N and nComm == x["nComm"],
         "nComm={} 96N={}".format(nComm, 96 * N))

    # ---- G2: kernel of pi restricted to Comm is exactly {+I, -I}
    idperm = idg[0].tobytes()
    ker = [g for g in Comm.values() if g[0].tobytes() == idperm]
    ker_keys = set(u25.key(g) for g in ker)
    gate(tag + ".G2.kernel_is_pmI",
         len(ker) == 2 and ker_keys == {id_key, m_key},
         "|ker pi|={} = {{+I,-I}}: {}".format(len(ker), ker_keys == {id_key, m_key}))

    # ---- translations, T~
    tperm = {}
    for i in range(N):
        v = tuple(int(a) for a in coords[i])
        tperm[v] = trans_perm(coords[i], coords, idx, N)
    T_bytes = set(p.tobytes() for p in tperm.values())
    Ttilde = [g for g in Comm.values() if g[0].tobytes() in T_bytes]
    tlift = {v: lift_of[tperm[v].tobytes()] for v in tperm}   # canonical trans lift
    e_x, e_y, e_z = (1, 0, 0), (0, 1, 0), (0, 0, 1)
    tx, ty, tz = tlift[e_x], tlift[e_y], tlift[e_z]

    all_trans_present = T_bytes.issubset(comm_perm_bytes) and len(T_bytes) == N
    Ttilde_gen = u25.closure([tx, ty, tz, central])
    gate(tag + ".G3.all_translations_present", all_trans_present,
         "|T|={} all in Comm image: {}".format(len(T_bytes),
                                               T_bytes.issubset(comm_perm_bytes)))
    gate(tag + ".G3.Ttilde_order_2N",
         len(Ttilde) == 2 * N and len(Ttilde) == x["Ttilde"],
         "|T~|={} 2N={}".format(len(Ttilde), 2 * N))
    gate(tag + ".G3.Ttilde_closure_eq",
         set(Ttilde_gen.keys()) == set(u25.key(g) for g in Ttilde),
         "closure{{t~x,t~y,t~z,-I}} == T~ (size {})".format(len(Ttilde_gen)))

    # ---- S: canonical lifts of the 48 zero-fixing (linear) perms
    zero_fix = [pb for pb in comm_perm_bytes
                if int(np.frombuffer(pb, dtype=np.int64)[0]) == 0]
    canon_lifts = [lift_of[pb] for pb in zero_fix]
    S = u25.closure(canon_lifts)
    S_keys = set(S.keys())
    S_perm_bytes = set(g[0].tobytes() for g in S.values())
    S_mats = {}
    for g in S.values():
        S_mats[g[0].tobytes()] = b3_coord(g[0], coords, idx, L)
    S_mat_set = set(A.tobytes() for A in S_mats.values())
    gate(tag + ".G4.S_order_48", len(S) == 48 and len(S) == x["S"],
         "|S|={}".format(len(S)))
    gate(tag + ".G4.S_minusI_free", m_key not in S_keys, "-I not in S")
    gate(tag + ".G4.S_pi_bijective", len(S_perm_bytes) == 48,
         "distinct perms in S: {}".format(len(S_perm_bytes)))
    gate(tag + ".G4.S_matrices_eq_B3ref", S_mat_set == refs["B3"],
         "extracted matrix set == reference B3 ({} mats)".format(len(S_mat_set)))

    # ---- G5: sub-sections O / A4 / D3
    for name, mref, order in (("O", refs["O"], 24), ("A4", refs["A4"], 12),
                              ("D3", refs["D3"], 6)):
        sub = {u25.key(g): g for g in S.values()
               if S_mats[g[0].tobytes()].tobytes() in mref}
        sub_closure = u25.closure(list(sub.values()))
        sub_mats = set(S_mats[g[0].tobytes()].tobytes() for g in sub.values())
        ok_size = len(sub) == order
        ok_free = m_key not in sub
        ok_grp = set(sub_closure.keys()) == set(sub.keys())
        ok_bij = sub_mats == mref and len(sub) == len(mref)
        gate(tag + ".G5.section_" + name,
             ok_size and ok_free and ok_grp and ok_bij,
             "|S cap pi^-1({0})|={1} (=|{0}ref|={2}) subgroup={3} -I-free={4}"
             .format(name, len(sub), len(mref), ok_grp, ok_free))

    # ---- preimage helper
    def preimage(down_bytes):
        return [g for g in Comm.values() if g[0].tobytes() in down_bytes]

    # ---- G6: K over T~ = pi^{-1}(T)
    K_T, wit_T = K_subgroup(Ttilde, {"[t~x,t~y]": (tx, ty)}, N)
    K_T_perm = set(g[0].tobytes() for g in K_T.values())
    twoT_bytes = set(trans_perm((2 * coords[i]) % L, coords, idx, N).tobytes()
                     for i in range(N))
    gate(tag + ".G6.minusI_in_KT", m_key in K_T, "-I in K_T")
    gate(tag + ".G6.KT_order", len(K_T) == x["K_T"],
         "|K_T|={} (XREF {})".format(len(K_T), x["K_T"]))
    gate(tag + ".G6.KT_witness_commutator",
         wit_T["[t~x,t~y]"] == m_key, "[t~x,t~y] = -I")
    gate(tag + ".G6.piKT_eq_2T",
         K_T_perm == twoT_bytes and len(twoT_bytes) == x["twoT"]
         and len(K_T) == 2 * len(twoT_bytes),
         "pi(K_T)=2T (|2T|={}) and |K_T|=2|2T|={}"
         .format(len(twoT_bytes), 2 * len(twoT_bytes)))

    # ---- G7: K over pi^{-1}(T_even)
    Teven_bytes = set(tperm[v].tobytes() for v in tperm if sum(v) % 2 == 0)
    Teven_pre = preimage(Teven_bytes)
    l110 = lift_of[tperm[(1, 1, 0)].tobytes()]
    l101 = lift_of[tperm[(1, 0, 1)].tobytes()]
    K_Te, wit_Te = K_subgroup(Teven_pre, {"[l110,l101]": (l110, l101)}, N)
    gate(tag + ".G7.minusI_in_KTeven", m_key in K_Te, "-I in K_Teven")
    gate(tag + ".G7.KTeven_order", len(K_Te) == x["K_Teven"],
         "|K_Teven|={} (XREF {})".format(len(K_Te), x["K_Teven"]))
    gate(tag + ".G7.KTeven_witness",
         wit_Te["[l110,l101]"] == m_key, "[lift(1,1,0),lift(1,0,1)] = -I")

    # ---- structural generators of Comm (Unit-26): 3 trans + 3 linear + -I
    s_cyc = lift_of[linear_perm(refs["A_cyc"], coords, idx, N).tobytes()]
    s_swap = lift_of[linear_perm(refs["A_swap"], coords, idx, N).tobytes()]
    s_flip = lift_of[linear_perm(refs["A_flip"], coords, idx, N).tobytes()]
    struct_gens = [tx, ty, tz, s_cyc, s_swap, s_flip, central]
    struct_closure = u25.closure(struct_gens)

    # ---- G8: K over pi^{-1}(T_even x| A4), tie to [Comm,Comm]
    A4_linear = [linear_perm(np.frombuffer(k, dtype=int).reshape(3, 3),
                             coords, idx, N)
                 for k in refs["A4"]]
    even_trans_perms = [tperm[v] for v in tperm if sum(v) % 2 == 0]
    TevA4_down = perm_closure(even_trans_perms + A4_linear, N)
    TevA4_bytes = set(TevA4_down.keys())
    TevA4_pre = preimage(TevA4_bytes)
    K_TevA4, _ = K_subgroup(TevA4_pre, {}, N)
    Dcomm = derived_subgroup(struct_gens)
    gate(tag + ".G8.TevA4_down_order",
         len(TevA4_down) == x["TevA4_down"] and len(TevA4_down) == (N // 2) * 12,
         "|T_even x| A4 downstairs|={} = (N/2)*12".format(len(TevA4_down)))
    gate(tag + ".G8.minusI_in_KTevA4", m_key in K_TevA4, "-I in K_(TevA4)")
    gate(tag + ".G8.KTevA4_order", len(K_TevA4) == x["K_TevenA4"],
         "|K_(TevA4)|={} (XREF {})".format(len(K_TevA4), x["K_TevenA4"]))
    gate(tag + ".G8.preimage_order_12N",
         len(TevA4_pre) == 12 * N and len(TevA4_pre) == x["comm_comm"],
         "|pi^-1(TevA4)|={} = 12N".format(len(TevA4_pre)))
    gate(tag + ".G8.commutator_subgroup_order",
         len(Dcomm) == x["comm_comm"] and m_key in Dcomm,
         "|[Comm,Comm]|={} (12N) and -I in it".format(len(Dcomm)))
    gate(tag + ".G8.preimage_eq_commutator_subgroup",
         set(u25.key(g) for g in TevA4_pre) == set(Dcomm.keys()),
         "pi^-1(TevA4) == [Comm,Comm] (set equality)")

    # ---- G9: splitting-criterion coherence -- B3 preimage K must be -I-free
    B3_pre = preimage(set(zero_fix))
    K_B3, _ = K_subgroup(B3_pre, {}, N)
    gate(tag + ".G9.KB3_minusI_free",
         m_key not in K_B3,
         "-I not in K(pi^-1(B3)) (|K|={}); split side coherent".format(len(K_B3)))

    # ---- beta over all N^2 translation pairs (measured, via commutators)
    vs = sorted(tperm.keys())
    beta = {}
    all_central = True
    closed_form_ok = True
    for s in vs:
        gs = tlift[s]
        for t in vs:
            c = commutator(gs, tlift[t])
            ck = u25.key(c)
            if ck == id_key:
                b = 1
            elif ck == m_key:
                b = -1
            else:
                b = 0
                all_central = False
            beta[(s, t)] = b
            if b != beta_formula(s, t):
                closed_form_ok = False
    gate(tag + ".G10.beta_all_central", all_central,
         "all {} translation commutators in {{+I,-I}}".format(len(vs) ** 2))
    gate(tag + ".G11.beta_closed_form", closed_form_ok,
         "beta = (-1)^{(sum s)(sum t)-s.t} on all pairs")

    unit_M = [[beta[(a, b)] for b in (e_x, e_y, e_z)] for a in (e_x, e_y, e_z)]
    unit_expect = [[1, -1, -1], [-1, 1, -1], [-1, -1, 1]]
    gate(tag + ".G12.beta_unit_matrix", unit_M == unit_expect,
         "unit matrix {}".format(unit_M))

    bimult_ok = True
    for s in vs:
        for e in (e_x, e_y, e_z):
            ss = tuple((s[i] + e[i]) % L for i in range(3))
            for t in (e_x, e_y, e_z):
                if beta[(ss, t)] != beta[(s, t)] * beta[(e, t)]:
                    bimult_ok = False
    gate(tag + ".G13.beta_bimultiplicative", bimult_ok,
         "beta(s+e,t)=beta(s,t)beta(e,t) all s, unit e, unit t "
         "(second slot by symmetry G14)")

    alt_diag_ok = all(beta[(s, s)] == 1 for s in vs)
    alt_sym_ok = all(beta[(s, t)] * beta[(t, s)] == 1 for s in vs for t in vs)
    gate(tag + ".G14.beta_alternating", alt_diag_ok and alt_sym_ok,
         "beta(s,s)=+1 all s; beta(s,t)beta(t,s)=+1 all pairs")

    inv_ok = True
    for A in (refs["A_cyc"], refs["A_swap"], refs["A_flip"]):
        for s in vs:
            As = tuple(int(w) % L for w in (A @ np.array(s)))
            for t in vs:
                At = tuple(int(w) % L for w in (A @ np.array(t)))
                if beta[(As, At)] != beta[(s, t)]:
                    inv_ok = False
    gate(tag + ".G15.beta_B3_invariant", inv_ok,
         "beta(As,At)=beta(s,t) for 3 B3 generators, all pairs "
         "(=> all B3 by multiplicativity in A)")

    # ---- G16: uniqueness enumeration + mod-2 factoring
    def u_of(v):
        return (v[0] % 2, v[1] % 2, v[2] % 2)
    M_meas = {}
    mod2_ok = True
    for (s, t), b in beta.items():
        kk = (u_of(s), u_of(t))
        if kk in M_meas:
            if M_meas[kk] != b:
                mod2_ok = False
        else:
            M_meas[kk] = b
    F2 = list(itertools.product((0, 1), repeat=3))
    S3 = list(itertools.permutations(range(3)))

    def perm_vec(pi, u):
        return tuple(u[pi[i]] for i in range(3))

    n_total = 0
    n_alt = 0
    n_inv_alt = 0
    n_nontrivial_inv_alt = 0
    n_match = 0
    n_reject = 0
    match_M = None
    for bits in itertools.product((0, 1), repeat=9):
        n_total += 1
        Mc = [list(bits[0:3]), list(bits[3:6]), list(bits[6:9])]
        table = {(u, v): betaM(Mc, u, v) for u in F2 for v in F2}
        is_alt = all(table[(u, u)] == 1 for u in F2)
        if is_alt:
            n_alt += 1
            is_inv = True
            for pi in S3:
                for u in F2:
                    pu = perm_vec(pi, u)
                    for v in F2:
                        if table[(pu, perm_vec(pi, v))] != table[(u, v)]:
                            is_inv = False
                            break
                    if not is_inv:
                        break
                if not is_inv:
                    break
            if is_inv:
                n_inv_alt += 1
                nontrivial = any(table[(u, v)] == -1 for u in F2 for v in F2)
                if nontrivial:
                    n_nontrivial_inv_alt += 1
        witness = next(((u, v) for u in F2 for v in F2
                        if table[(u, v)] != M_meas[(u, v)]), None)
        if witness is None:
            n_match += 1
            match_M = Mc
        else:
            n_reject += 1

    # pull the unique matching form back to T and re-check against measured beta
    pullback_ok = match_M is not None and all(
        betaM(match_M, u_of(s), u_of(t)) == beta[(s, t)] for (s, t) in beta)
    match_is_nontrivial_inv_alt = False
    if match_M is not None:
        tbl = {(u, v): betaM(match_M, u, v) for u in F2 for v in F2}
        alt = all(tbl[(u, u)] == 1 for u in F2)
        inv = all(tbl[(perm_vec(pi, u), perm_vec(pi, v))] == tbl[(u, v)]
                  for pi in S3 for u in F2 for v in F2)
        nt = any(tbl[(u, v)] == -1 for u in F2 for v in F2)
        match_is_nontrivial_inv_alt = alt and inv and nt

    gate(tag + ".G16.beta_factors_mod2", mod2_ok and len(M_meas) == 64,
         "beta depends only on (s,t) mod 2 (64 classes consistent)")
    gate(tag + ".G16.count_total_512", n_total == 512, "512 F2 candidates")
    gate(tag + ".G16.count_alternating_8", n_alt == 8,
         "{} alternating".format(n_alt))
    gate(tag + ".G16.count_invariant_2", n_inv_alt == 2,
         "{} S3-invariant alternating".format(n_inv_alt))
    gate(tag + ".G16.count_nontrivial_invariant_1", n_nontrivial_inv_alt == 1,
         "{} nontrivial invariant alternating".format(n_nontrivial_inv_alt))
    gate(tag + ".G16.unique_match", n_match == 1 and match_is_nontrivial_inv_alt,
         "exactly 1 of 512 matches measured beta; it is the nontrivial invariant")
    gate(tag + ".G16.rejectors_511",
         n_reject == 511 and n_match + n_reject == 512,
         "{} candidates each rejected by an explicit witness pair".format(n_reject))
    gate(tag + ".G16.pullback_matches_all_pairs", pullback_ok,
         "unique M pulled back = measured beta on all N^2 pairs")

    # ---- G17: unit-lift orders
    for name, e in (("x", e_x), ("y", e_y), ("z", e_z)):
        g = tlift[e]
        p = idg
        order = None
        for kk in range(1, 4 * L + 1):
            p = u25.compose(p, g)
            if u25.key(p) == id_key:
                order = kk
                break
        gL = idg
        for _ in range(L):
            gL = u25.compose(gL, g)
        gate(tag + ".G17.unit_lift_order_" + name,
             order == L and u25.key(gL) == id_key,
             "order(t~_{})={} (=L) and (t~)^L=+I".format(name, order))

    # ---- G18: 2-torsion square class q
    h = L // 2
    q_meas = {}
    q_minus = []
    formula_ok = True
    for v in itertools.product((0, 1), repeat=3):
        s = tuple(h * a for a in v)
        gsq = u25.compose(tlift[s], tlift[s])
        ksq = u25.key(gsq)
        qv = 1 if ksq == id_key else (-1 if ksq == m_key else 0)
        q_meas[v] = qv
        expo = (h * h) * sum(v[i] * v[j] for i in range(3) for j in range(i + 1, 3))
        qf = -1 if (expo % 2) else 1
        if qv != qf:
            formula_ok = False
        if qv == -1:
            q_minus.append(s)
    gate(tag + ".G18.q_matches_formula", formula_ok,
         "q((L/2)v) = (-1)^{(L/2)^2 sum_{i<j} v_i v_j} on all 8 v")
    gate(tag + ".G18.q_minus_count", len(q_minus) == x["q_minus"],
         "q=-I count={} (XREF {})".format(len(q_minus), x["q_minus"]))
    if L == 6:
        expect_minus = {(3, 3, 0), (3, 0, 3), (0, 3, 3), (3, 3, 3)}
        gate(tag + ".G18.q_minus_set_L6", set(q_minus) == expect_minus,
             "-I 2-torsion set = {(3,3,0),(3,0,3),(0,3,3),(3,3,3)}")

    # ---- G19: semidirect decomposition
    conj_ok = True
    Ttilde_gens = [tx, ty, tz, central]
    for gen in struct_gens:
        ginv = u25.sp_inv(gen)
        for tg in Ttilde_gens:
            c = u25.compose(u25.compose(gen, tg), ginv)
            if c[0].tobytes() not in T_bytes:
                conj_ok = False
    prod_keys = set(u25.key(u25.compose(t, s))
                    for t in Ttilde for s in S.values())
    Comm_keyset = set(u25.key(g) for g in Comm.values())
    inter = set(u25.key(g) for g in Ttilde) & S_keys
    gate(tag + ".G19.struct_gens_generate_Comm",
         len(struct_closure) == nComm,
         "closure of 7 structural generators = |Comm| = {}".format(len(struct_closure)))
    gate(tag + ".G19.Ttilde_normal", conj_ok,
         "conjugates of T~ generators by all 7 struct gens land in T~")
    gate(tag + ".G19.Ttilde_cap_S_trivial", inter == {id_key},
         "T~ cap S = {+I}")
    gate(tag + ".G19.order_product",
         len(Ttilde) * len(S) == nComm,
         "|T~|*|S|={}*{}={} = |Comm|".format(len(Ttilde), len(S),
                                             len(Ttilde) * len(S)))
    gate(tag + ".G19.TS_product_set_eq_Comm",
         len(prod_keys) == nComm and prod_keys == Comm_keyset,
         "product set T~*S: {} distinct elements = Comm elementwise".format(
             len(prod_keys)))

    # ---- G20: independent D2 spectrum anchor (floating, tol 1e-9)
    w = np.linalg.eigvalsh(M.astype(float))
    wr = np.round(w)
    int_resid = float(np.max(np.abs(w - wr)))
    distinct = sorted(set(int(v) for v in wr.tolist()), reverse=True)
    got_mults = [int(np.sum(np.abs(w - lamk) < 1e-9)) for lamk in distinct]
    gate(tag + ".G20.spectrum_eigenvalues",
         distinct == x["eig"] and int_resid < 1e-9,
         "eig={} (int resid {:.2e} < 1e-9)".format(distinct, int_resid))
    gate(tag + ".G20.spectrum_multiplicities", got_mults == x["mults"],
         "mults={} (XREF {})".format(got_mults, x["mults"]))

    print("  [L={} wall {:.1f}s]".format(L, time.time() - t0))
    return dict(L=L, unit_M=unit_M, q_minus=len(q_minus))


# ---------------------------------------------------------------- main
def main():
    t0 = time.time()
    print("KCPT Unit 27 runner -- extension translation localization")
    print("exact integer group arithmetic; floating point only in G20 "
          "(D2 spectrum, tol 1e-9)")
    refs = build_reference_groups()
    print("reference groups: |B3|={} |O|={} |A4|={} |D3|={}".format(
        len(refs["B3"]), len(refs["O"]), len(refs["A4"]), len(refs["D3"])))
    gate("REF.groups_orders",
         len(refs["B3"]) == 48 and len(refs["O"]) == 24
         and len(refs["A4"]) == 12 and len(refs["D3"]) == 6,
         "B3=48 O=24 A4=12 D3=6 (D3 via +-allowing body-diagonal definition)")

    results = {}
    results[4] = run_L(4, refs)
    results[6] = run_L(6, refs)

    # ---- cross-surface gates (G21)
    print("\n" + "=" * 72)
    print("cross-surface gates")
    print("=" * 72)
    gate("X.G21.beta_unit_matrix_agree",
         results[4]["unit_M"] == results[6]["unit_M"]
         == [[1, -1, -1], [-1, 1, -1], [-1, -1, 1]],
         "same beta unit matrix at L=4 and L=6")
    gate("X.G21.q_differs_across_surfaces",
         results[4]["q_minus"] == 0 and results[6]["q_minus"] == 4,
         "q_minus_count 0 (L=4) vs 4 (L=6): (L/2)^2 parity even vs odd")

    ngates = _P[0] + _F[0]
    print("\n" + "=" * 72)
    print("TOTAL: PASS={} FAIL={}".format(_P[0], _F[0]))
    print("gates={} wall={:.1f}s".format(ngates, time.time() - t0))
    sys.exit(0 if _F[0] == 0 else 1)


if __name__ == "__main__":
    main()
