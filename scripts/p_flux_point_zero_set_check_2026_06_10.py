#!/usr/bin/env python3
"""P-FLUX point-zero-set selector hunt -- candidate-supplier no-go (runner).

Companion to
docs/P_FLUX_POINT_ZERO_SET_FROM_RETAINED_ROWS_NARROW_NO_GO_NOTE_2026-06-10.md

Question.  The matter-content no-go
(P_FLUX_SELECTION_FROM_MATTER_CONTENT_NARROW_NO_GO_NOTE_2026-06-10)
sharpened the live escapes for the one-bit residual P-FLUX (phi = -1 vs
phi = +1) to three: (i) a point-like-zero-set requirement, (ii) a
kernel-equals-carrier / no-extra-massless-sector requirement, (iii) a
branch-neutral positivity/transfer theorem.  This runner hunts the
candidate suppliers for (i)/(ii) among the spectral/clustering rows and
the three-generation count/no-proper-quotient rows, then computes the
verdict on the licensed two-class surface (K0 = uniform flux +1 scalar
tight-binding; K1 = uniform flux -1 Kawamoto-Smit class).

Outcome computed here (the sharpening):

  1. ZERO-SET GEOMETRY (re-derived, not imported): K0's massless set is
     the codimension-1 surface  sum_mu cos p_mu = 0  — zero-mode count
     20 -> 68 -> 140 at L = 4, 8, 12 (growth exponent ~ 1.8, extensive);
     K1's is point-like: 8 -> 8 -> 8.  The separator is real.
  2. ESCAPE (i) HAS NO TESTED SUPPLIER: the clustering row's
     load-bearing L2 is conditional on a transfer gap Delta_T > 0.  At
     m = 0 the hypothesis fails on BOTH branches; under the shared
     staggered-mass deformation m*eps (eps anticommutes with BOTH
     branch operators) both branches gap to EXACTLY m — the hypothesis,
     where satisfiable on this surface, is satisfied branch-neutrally.
     The LR/locality data (range, per-edge norms) are branch-identical.
     The log-transfer quasilocality row is scoped to the free bilinear
     staggered two-step sector and has rate arcsinh(m) -> 0 at m = 0.
  3. ESCAPE (ii) DICHOTOMY (the new computed content): the retained
     count/no-proper-quotient package admits NO branch-separating
     reading.  Carrier-conditional (verbatim) reading: TRUE on both
     branches (both embedded carriers generate M_3(C), commutant dim 1,
     count 3).  Kernel-global reading: FALSE on both branches — K1's
     OWN full kernel is reducible (commutant dim 4: the four
     Hamming-class blocks), K0's is reducible (commutant dim 8); the
     kernel-global species counts are 8/4 (K1) and 20/8 (K0), never 3.
     The entire separation lives in the single non-retained clause
     "ker = carrier" (extra dim 0/0 vs 12/60), which appears in no
     linked count-row text — both count rows carry explicit
     carrier-only boundary clauses (verified textually).
  4. The Record route supplies nothing: the Record axiom text and the
     retained record-function row are conditional on a SUPPLIED finite
     decomposition; they bound nothing about kinetic kernels.
  5. Falsification: the candidate requirement (carrier package AND
     point-like zero set) is non-vacuous and well-targeted — it selects
     exactly K1 among {K0, K1, point-zero scalar comparator}; dropping
     the non-retained clause restores the PASS/PASS tie.

Sections:
  [A] exact branch construction + zero-set geometry + comparator
  [B] escape (i): spectral/clustering candidates are branch-neutral
  [C] escape (ii): the count/no-proper-quotient restatement dichotomy
  [D] escape (iii) boundary, Record route, falsification legs,
      turn-1 inversion-guard compliance

Deterministic, no network, no randomness, numpy only.
Exit code 0 iff FAIL = 0.
"""

import itertools
import json
import math
import os
import sys

import numpy as np

PASS = 0
FAIL = 0
CHECK = 0

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def report(ok, msg):
    global PASS, FAIL, CHECK
    CHECK += 1
    if ok:
        PASS += 1
        print(f"[PASS] {CHECK:2d}. {msg}")
    else:
        FAIL += 1
        print(f"[FAIL] {CHECK:2d}. {msg}")


def residual(msg):
    print(f"RESIDUAL (declared-open): {msg}")


# ----------------------------------------------------------------------
# constructions (re-derived on the linked single-mode surface;
# conceptually parallel to the matter-content no-go runner, file not
# imported)
# ----------------------------------------------------------------------

def sites_of(L):
    return list(itertools.product(range(L), repeat=3))


def build_h(L, t_fun, onsite=0.0):
    sites = sites_of(L)
    idx = {s: i for i, s in enumerate(sites)}
    N = len(sites)
    h = np.zeros((N, N), complex)
    for x in sites:
        for mu in range(3):
            xp = list(x)
            xp[mu] = (xp[mu] + 1) % L
            xp = tuple(xp)
            t = t_fun(x, mu)
            h[idx[xp], idx[x]] += t
            h[idx[x], idx[xp]] += np.conj(t)
        if onsite != 0.0:
            h[idx[x], idx[x]] += onsite
    return h, sites, idx


def t_K0(x, mu):
    return 1.0


def t_K1(x, mu):
    if mu == 0:
        return 1.0
    if mu == 1:
        return (-1.0) ** x[0]
    return (-1.0) ** (x[0] + x[1])


def translation(L, sites, idx, mu):
    N = len(sites)
    T = np.zeros((N, N))
    for x in sites:
        xp = list(x)
        xp[mu] = (xp[mu] + 1) % L
        T[idx[tuple(xp)], idx[x]] = 1.0
    return T


def c3_111(sites, idx):
    N = len(sites)
    R = np.zeros((N, N))
    for x in sites:
        R[idx[(x[2], x[0], x[1])], idx[x]] = 1.0
    return R


def plaquette_fluxes(L, sites, t_fun):
    fluxes = []
    for x in sites:
        for mu in range(3):
            for nu in range(mu + 1, 3):
                xm = list(x)
                xm[mu] = (xm[mu] + 1) % L
                xm = tuple(xm)
                xn = list(x)
                xn[nu] = (xn[nu] + 1) % L
                xn = tuple(xn)
                f = (t_fun(x, mu) * t_fun(xm, nu)
                     * np.conj(t_fun(xn, mu)) * np.conj(t_fun(x, nu)))
                fluxes.append(complex(f))
    return fluxes


def kernel(h, tol=1e-9):
    w, v = np.linalg.eigh(h)
    return v[:, np.abs(w) < tol]


def spectral_gap(h):
    w = np.linalg.eigvalsh(h)
    return float(min(abs(w)))


def joint_characters(ker, Ts):
    """Joint characters of the commuting restricted translations on the
    translation-invariant kernel (defensively verified)."""
    K = ker.shape[1]
    Tr = [ker.conj().T @ T @ ker for T in Ts]
    M = sum((3 ** a) * (Tr[a] + Tr[a].conj().T)
            + (3 ** (a + 3)) * 1j * (Tr[a] - Tr[a].conj().T)
            for a in range(3))
    _, v = np.linalg.eigh(M)
    chars = []
    for i in range(K):
        vec = v[:, i]
        c = []
        for a in range(3):
            lam = complex(vec.conj() @ Tr[a] @ vec)
            if np.linalg.norm(Tr[a] @ vec - lam * vec) > 1e-7:
                raise RuntimeError("not a joint eigenvector")
            c.append(lam)
        chars.append(tuple(c))
    return v, chars


def find_cube(chars):
    """Existential global per-direction dressing: a base line such that
    the character ratios realize the Klein cube {+-1}^3 with
    multiplicity exactly 1 each.  Returns {sign_triple: line_index} or
    None."""
    K = len(chars)
    for base in range(K):
        lam = chars[base]
        members = {}
        for j, c in enumerate(chars):
            d = tuple(c[a] / lam[a] for a in range(3))
            s = tuple(int(round(x.real)) for x in d)
            if all(abs(d[a] - s[a]) < 1e-7 and s[a] in (-1, 1)
                   for a in range(3)):
                members.setdefault(s, []).append(j)
        if len(members) == 8 and all(len(v) == 1 for v in members.values()):
            return {s: v[0] for s, v in members.items()}
    return None


def commutant_dim(ops):
    """Dimension of the commutant of the algebra generated by ops
    (= commutant of the generating set)."""
    n = ops[0].shape[0]
    rows = [np.kron(np.eye(n), A) - np.kron(A.T, np.eye(n)) for A in ops]
    C = np.vstack(rows)
    return int(n * n - np.linalg.matrix_rank(C, tol=1e-8))


def algebra_dim(gens, n):
    allm = [np.eye(n, dtype=complex)] + list(gens)
    rank = 0
    for _ in range(6):
        allm = allm + [a @ g for a in allm for g in gens]
        rank = np.linalg.matrix_rank(
            np.array([m.flatten() for m in allm]), tol=1e-7)
        if rank == n * n:
            break
    return int(rank)


def carrier_data(h, L, sites, idx, Ts, R):
    """Locate the embedded Klein-cube carrier in ker(h); return a dict
    with carrier-conditional and kernel-global readouts."""
    out = {}
    ker = kernel(h)
    K = ker.shape[1]
    out["ker_dim"] = K
    if K == 0:
        return out
    Pk = ker @ ker.conj().T
    out["T_invariant"] = all(
        np.allclose(Pk @ T @ Pk, T @ Pk, atol=1e-9) for T in Ts) and \
        np.allclose(Pk @ R @ Pk, R @ Pk, atol=1e-9)
    if not out["T_invariant"]:
        return out
    vecs, chars = joint_characters(ker, Ts)
    cube = find_cube(chars)
    out["cube"] = cube is not None
    if cube is None:
        return out
    out["extra_dim"] = K - 8

    # --- carrier-conditional (verbatim retained) readout on hw=1 ---
    hw1 = [s for s in cube if sum(1 for x in s if x == -1) == 1]
    hw1.sort(key=lambda s: s.index(-1))
    B = np.column_stack([vecs[:, cube[s]] / np.linalg.norm(vecs[:, cube[s]])
                         for s in hw1])
    Rr = ker.conj().T @ R @ ker
    M3gen_R = B.conj().T @ Rr @ B
    P = [np.diag([1.0 if i == j else 0.0 for i in range(3)])
         for j in range(3)]
    out["carrier_alg_dim"] = algebra_dim(P + [M3gen_R], 3)
    out["carrier_commutant"] = commutant_dim(
        [p.astype(complex) for p in P] + [M3gen_R])
    out["carrier_count"] = len(hw1)

    # --- kernel-global readouts ---
    Tr = [ker.conj().T @ T @ ker for T in Ts]
    out["kernel_commutant"] = commutant_dim(Tr + [Rr])

    def rnd(c):
        return tuple(complex(round(z.real, 6), round(z.imag, 6)) for z in c)
    classes = set(rnd(c) for c in chars)
    out["kernel_char_count"] = len(classes)
    seen = set()
    orbits = 0
    for c in classes:
        if c in seen:
            continue
        orbits += 1
        cur = c
        for _ in range(3):
            cur = (cur[2], cur[0], cur[1])
            seen.add(cur)
    out["kernel_c3_orbit_count"] = orbits
    return out


def note_text(relpath):
    with open(os.path.join(REPO, relpath), encoding="utf-8") as f:
        return f.read()


def ledger_status(row):
    with open(os.path.join(REPO, "docs/audit/data/audit_ledger.json"),
              encoding="utf-8") as f:
        rows = json.load(f)["rows"]
    if row not in rows:
        return None
    r = rows[row]
    return r.get("effective_status") or r.get("status")


# ----------------------------------------------------------------------
# main
# ----------------------------------------------------------------------

def main():
    print("=" * 72)
    print("[A] branch construction + zero-set geometry + comparator")
    print("=" * 72)

    Ls = (4, 8, 12)
    H0, H1, S, I = {}, {}, {}, {}
    for L in Ls:
        H0[L], S[L], I[L] = build_h(L, t_K0)
        H1[L], _, _ = build_h(L, t_K1)

    f0 = plaquette_fluxes(4, S[4], t_K0)
    f1 = plaquette_fluxes(4, S[4], t_K1)
    report(np.allclose(H0[4], H0[4].conj().T)
           and np.allclose(H1[4], H1[4].conj().T)
           and all(abs(f - 1) < 1e-12 for f in f0)
           and all(abs(f + 1) < 1e-12 for f in f1),
           "[A] both branches Hermitian; frame-invariant uniform flux "
           "K0 phi=+1, K1 phi=-1 (licensed two-class surface, re-derived)")

    z0 = {L: kernel(H0[L]).shape[1] for L in Ls}
    z1 = {L: kernel(H1[L]).shape[1] for L in Ls}
    report((z0[4], z0[8], z0[12]) == (20, 68, 140)
           and (z1[4], z1[8], z1[12]) == (8, 8, 8),
           f"[A] zero-mode counts: K0 (L=4,8,12) = "
           f"({z0[4]},{z0[8]},{z0[12]}); K1 = ({z1[4]},{z1[8]},{z1[12]})")

    sym0 = {L: sum(1 for m in itertools.product(range(L), repeat=3)
                   if abs(sum(np.cos(2 * np.pi * n / L) for n in m)) < 1e-9)
            for L in Ls}
    report(all(sym0[L] == z0[L] for L in Ls),
           "[A] K0 kernel = lattice trace of the codimension-1 symbol "
           "surface sum_mu cos p_mu = 0 (symbol count matches eigencount "
           "at L=4,8,12)")

    expo = math.log(z0[12] / z0[8]) / math.log(12 / 8)
    report(expo > 1.5 and z1[4] == z1[12],
           f"[A] zero-set geometry separator (computed): K0 growth "
           f"exponent {expo:.2f} (extensive, surface-like); K1 count "
           f"L-independent = 8 (point-like)")

    # point-zero scalar comparator: NN flux(+1) hopping + on-site -6;
    # symbol 2*sum cos p_mu - 6, unique zero p = 0
    HP = {L: build_h(L, t_K0, onsite=-6.0)[0] for L in Ls}
    zp = {L: kernel(HP[L]).shape[1] for L in Ls}
    R3_4 = c3_111(S[4], I[4])
    report((zp[4], zp[8], zp[12]) == (1, 1, 1)
           and np.allclose(R3_4 @ HP[4] @ R3_4.T, HP[4]),
           f"[A] comparator (scalar NN + on-site -6, declared OFF the "
           f"two-class surface): point-like zero set ({zp[4]},{zp[8]},"
           f"{zp[12]}) — 'point-like zero set' is non-vacuous and NOT "
           f"synonymous with first-order kinetic order")

    print()
    print("=" * 72)
    print("[B] escape (i): spectral/clustering candidates are")
    print("    branch-neutral on the licensed surface")
    print("=" * 72)

    st_cluster = ledger_status(
        "axiom_first_cluster_decomposition_theorem_note_2026-04-29")
    st_micro = ledger_status(
        "axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01")
    st_quasi = ledger_status(
        "transfer_matrix_log_quasilocality_narrow_theorem_note_2026-06-10")
    st_recon = ledger_status(
        "reconstructed_h_quasilocal_from_analytic_dispersion_"
        "microcausality_bridge_narrow_theorem_note_2026-06-06")
    report(st_cluster is not None and st_micro is not None
           and st_quasi is not None and st_recon is not None,
           f"[B] parser visibility: cluster-decomposition row "
           f"{st_cluster}; microcausality-LR theorem row {st_micro}; "
           f"log-transfer quasilocality row {st_quasi}; "
           f"analytic-dispersion bridge row {st_recon}. These "
           f"classifications are reported for context only; the selector "
           f"test below uses the rows' scope and branch computations.")

    cl_txt = note_text(
        "docs/AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md")
    report("conditional on a transfer-matrix spectral gap" in cl_txt
           and "explicitly out of the" in cl_txt,
           "[B] textual: the clustering row's load-bearing L2 is "
           "'conditional on a transfer-matrix spectral gap Delta_T > 0' "
           "by its own claim-scope text; unconditional clustering is "
           "explicitly out of its load-bearing scope")

    g0 = {L: spectral_gap(H0[L]) for L in (4, 8)}
    g1 = {L: spectral_gap(H1[L]) for L in (4, 8)}
    report(all(g < 1e-9 for g in list(g0.values()) + list(g1.values())),
           "[B] at m=0 (the licensed surface): spectral gap = 0 on BOTH "
           "branches (L=4,8) — the gap hypothesis fails branch-neutrally; "
           "the gap-conditional clustering row cannot fire on either side")

    ok_eps = True
    gaps = {}
    m = 0.5
    for L in (4, 8):
        eps = np.diag([(-1.0) ** sum(x) for x in S[L]])
        ok_eps &= np.allclose(eps @ H0[L] @ eps, -H0[L], atol=1e-12)
        ok_eps &= np.allclose(eps @ H1[L] @ eps, -H1[L], atol=1e-12)
        gaps[("K0", L)] = spectral_gap(H0[L] + m * eps)
        gaps[("K1", L)] = spectral_gap(H1[L] + m * eps)
    report(ok_eps and all(abs(g - m) < 1e-9 for g in gaps.values()),
           f"[B] shared mass deformation: eps(x)=(-1)^(x1+x2+x3) "
           f"anticommutes with BOTH branch operators; gap(h + 0.5 eps) = "
           f"0.5 EXACTLY on both branches (L=4,8) — where the gap "
           f"hypothesis is satisfiable on this surface it is satisfied "
           f"branch-identically, so gap-conditional clustering cannot "
           f"separate")

    dos0 = int((np.abs(np.linalg.eigvalsh(H0[12])) < 0.5).sum())
    dos1 = int((np.abs(np.linalg.eigvalsh(H1[12])) < 0.5).sum())
    nrm0 = sorted(abs(t_K0(x, mu)) for x in S[4] for mu in range(3))
    nrm1 = sorted(abs(t_K1(x, mu)) for x in S[4] for mu in range(3))
    report(nrm0 == nrm1 and dos0 > 20 * dos1,
           f"[B] LR/locality data branch-identical (range 1, per-edge "
           f"|t| multisets equal) so LR-type bounds are "
           f"branch-neutral; the data that DO separate are spectral "
           f"density near E=0 (L=12, window 0.5: K0 {dos0} vs K1 {dos1} "
           f"modes) — not consumed by the linked candidate rows")
    residual("the density-of-states / correlation-decay separator at "
             "criticality is real and computed, but the linked candidate "
             "rows do not state a requirement on it; supplying one is "
             "exactly "
             "escape (i), still open (boundary B-Z2)")

    print()
    print("=" * 72)
    print("[C] escape (ii): the count/no-proper-quotient restatement")
    print("    dichotomy — no reading separates")
    print("=" * 72)

    dat = {}
    for L in (4, 8):
        Ts = [translation(L, S[L], I[L], mu) for mu in range(3)]
        R = c3_111(S[L], I[L])
        dat[("K1", L)] = carrier_data(H1[L], L, S[L], I[L], Ts, R)
        dat[("K0", L)] = carrier_data(H0[L], L, S[L], I[L], Ts, R)

    d1, d0 = dat[("K1", 4)], dat[("K0", 4)]
    report(d1["cube"] and d1["carrier_alg_dim"] == 9
           and d1["carrier_commutant"] == 1 and d1["carrier_count"] == 3,
           "[C] carrier-conditional (VERBATIM retained) reading on K1: "
           "hw=1 projectors + restricted C3 generate M_3(C) (dim 9), "
           "commutant dim 1 (irreducible => no proper quotient), "
           "count = 3")
    report(d0["cube"] and d0["carrier_alg_dim"] == 9
           and d0["carrier_commutant"] == 1 and d0["carrier_count"] == 3,
           "[C] carrier-conditional reading on K0: IDENTICAL readouts "
           "(M_3(C) dim 9, commutant 1, count 3) on the embedded carrier "
           "=> the verbatim retained statement is TRUE on both branches "
           "and cannot separate")
    report(d1["kernel_commutant"] == 4,
           f"[C] kernel-global no-proper-quotient reading on K1: the "
           f"restricted algebra on the FULL kernel has commutant dim "
           f"{d1['kernel_commutant']} > 1 (the four Hamming-class "
           f"blocks) — proper invariant sectors EXIST, the kernel-global "
           f"reading is FALSE on the staggered branch itself")
    report(d0["kernel_commutant"] == 8,
           f"[C] kernel-global reading on K0: commutant dim "
           f"{d0['kernel_commutant']} > 1 — FALSE there too; the "
           f"kernel-global no-proper-quotient reading is branch-neutrally "
           f"FALSE (it separates nothing and is not the retained "
           f"statement anyway)")
    report(d1["kernel_char_count"] == 8 and d1["kernel_c3_orbit_count"] == 4
           and d0["kernel_char_count"] == 20
           and d0["kernel_c3_orbit_count"] == 8,
           f"[C] kernel-global species-count readouts: distinct joint "
           f"characters K1 {d1['kernel_char_count']}, K0 "
           f"{d0['kernel_char_count']}; C3-orbit classes K1 "
           f"{d1['kernel_c3_orbit_count']}, K0 "
           f"{d0['kernel_c3_orbit_count']} — NEVER 3 on either branch: "
           f"the retained 'count = 3' exists only after the carrier + "
           f"hw=1 restriction, which BOTH branches pass")

    npq_txt = note_text(
        "docs/THREE_GENERATION_OBSERVABLE_NO_PROPER_QUOTIENT_NARROW_"
        "THEOREM_NOTE_2026-05-02.md")
    cnt_txt = note_text(
        "docs/THREE_GENERATION_OBSERVABLE_COUNT_COROLLARY_NOTE_"
        "2026-05-03.md")
    st_npq = ledger_status(
        "three_generation_observable_no_proper_quotient_narrow_theorem_"
        "note_2026-05-02")
    st_cnt = ledger_status(
        "three_generation_observable_count_corollary_note_2026-05-03")
    report(st_npq == "retained" and st_cnt == "retained"
           and "On the retained finite" in npq_txt
           and ("does not assert the full physical staggered-carrier "
                "realization") in npq_txt
           and "Q : H_hw=1 -> H_red" in cnt_txt,
           "[C] textual license audit: both count rows retained, and "
           "both quantify ONLY over the finite carrier — the "
           "no-proper-quotient row declares 'On the retained finite C^3 "
           "carrier ... does not assert the full physical "
           "staggered-carrier realization'; the count corollary "
           "quantifies over quotients Q : H_hw=1 -> H_red — the "
           "kernel-global restatement is NOT licensed by their text")

    x1 = (dat[("K1", 4)]["extra_dim"], dat[("K1", 8)]["extra_dim"])
    x0 = (dat[("K0", 4)]["extra_dim"], dat[("K0", 8)]["extra_dim"])
    report(x1 == (0, 0) and x0 == (12, 60),
           f"[C] the separating increment isolated: ker-minus-carrier "
           f"dim K1 (L=4,8) = {x1}, K0 = {x0} — adding the single clause "
           f"'ker = carrier' to the retained battery flips K0 to FAIL; "
           f"that clause appears in NO retained text and is exactly "
           f"escape (ii), still unsupplied")
    residual("the kernel-global restatement of the count/no-proper-"
             "quotient rows is irreducibly NEW input: carrier-"
             "conditional readings tie (TRUE/TRUE), kernel-global "
             "readings tie (FALSE/FALSE); only the non-retained "
             "'ker = carrier' clause separates (boundary B-Z1)")

    print()
    print("=" * 72)
    print("[D] escape (iii) boundary, Record route, falsification,")
    print("    inversion-guard compliance")
    print("=" * 72)

    ql_txt = note_text(
        "docs/TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_"
        "2026-06-10.md")
    report("bilinear staggered two-step sector only" in ql_txt
           and abs(math.asinh(0.0)) == 0.0 and math.asinh(0.5) > 0,
           "[D] escape (iii) boundary: the log-transfer quasilocality "
           "row is by its own scope line 'free (U = 1) bilinear "
           "staggered two-step sector only', and its sharp rate "
           "arcsinh(m) -> 0 at m = 0. On the licensed massless surface "
           "this does not supply a branch-neutral point-zero-set or "
           "kernel-exactness selector.")

    ax_txt = note_text("docs/MINIMAL_AXIOMS_2026-06-05.md")
    rec_txt = note_text(
        "docs/RECORD_FUNCTION_FINITE_SECTOR_ALGEBRA_2026-06-05.md")
    st_rec = ledger_status("record_function_finite_sector_algebra_2026-06-05")
    report(("record supplies no readout context, decomposition" in ax_txt)
           and ("Given a supplied finite record-sector decomposition"
                in rec_txt)
           and st_rec == "retained",
           "[D] Record route killed by the rows' own conditionality: the "
           "Record axiom 'supplies no readout context, decomposition, "
           "... sector-generation rule'; the retained record-function "
           "row is conditional on a SUPPLIED finite decomposition — "
           "neither bounds the massless-sector dimension of a kinetic "
           "operator")

    # falsification leg 1: non-vacuity / targeting of the candidate
    Ts4 = [translation(4, S[4], I[4], mu) for mu in range(3)]
    datP = carrier_data(HP[4], 4, S[4], I[4], Ts4, R3_4)
    cand = {}
    cand["K1"] = (d1["cube"] and d1["extra_dim"] == 0
                  and z1[4] == z1[12])
    cand["K0"] = (d0["cube"] and d0["extra_dim"] == 0
                  and z0[4] == z0[12])
    cand["comparator"] = (datP.get("cube", False)
                          and zp[4] == zp[12])
    report(cand["K1"] and not cand["K0"] and not cand["comparator"],
           "[D] falsification leg 1 (non-vacuity): the candidate "
           "requirement (carrier package AND point-like zero set / "
           "kernel exactness) selects EXACTLY K1 among {K0, K1, "
           "comparator}: K0 fails the zero-set clause, the point-zero "
           "comparator fails the carrier clause — the requirement is "
           "non-vacuous and would force phi = -1 immediately IF any "
           "clause of it were retained")

    tie = (d1["cube"] and d1["carrier_count"] == 3
           and d0["cube"] and d0["carrier_count"] == 3)
    report(tie,
           "[D] falsification leg 2 (remove the non-retained input): "
           "dropping the zero-set/exactness clause and testing only the "
           "retained carrier-conditional content restores the PASS/PASS "
           "tie — the ENTIRE selection lives in the unsupplied clause")

    report(d1["kernel_char_count"] != 3 and d0["kernel_char_count"] != 3
           and d1["kernel_c3_orbit_count"] != 3
           and d0["kernel_c3_orbit_count"] != 3
           and d1["carrier_count"] == d0["carrier_count"] == 3,
           "[D] turn-1 inversion-guard compliance (computed): the "
           "matched count 3 forces nothing here — every kernel-global "
           "count readout differs from 3 on both branches, and the only "
           "reading that yields 3 (carrier + hw=1) ties; the count is "
           "consumed solely as a tested readout value, never as a "
           "forcing input (index-pairing no-go guards respected)")
    residual("predicate-G heritage (B-P1 of the matter-content no-go): "
             "the kernel-sector realization reading remains a declared, "
             "non-retained bridge on both branches (boundary B-Z3)")
    residual("finite volumes L in {4,8,12}, PBC; wrap-convention "
             "(L mod 4) carrier arithmetic inherited as branch-symmetric "
             "convention data (boundary B-Z4)")
    residual("the kernel-global readings tested are the two canonical "
             "ones (invariant-subspace/quotient structure; species-count "
             "readouts); readings that first restrict to the carrier tie "
             "by the parent witness — exhaustiveness over all "
             "conceivable restatements is not claimed (boundary B-Z5)")

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print("VERDICT: the point-like-zero-set / kernel-equals-carrier "
              "requirement (escapes (i)/(ii) of the matter-content")
        print("         no-go) has NO supplier among the tested candidate "
              "rows. The clustering row is gap-conditional and "
              "branch-neutral")
        print("         (gap 0/0 at m=0; identical gap m under the shared "
              "staggered-mass deformation); the")
        print("         log-transfer row is scoped/rate-limited at the "
              "massless surface; Record supplies no sector-dimension")
        print("         bound. The count/no-proper-quotient "
              "package admits NO separating reading: carrier-conditional")
        print("         readings are TRUE on both branches, kernel-global "
              "readings are FALSE on both branches (K1's own kernel")
        print("         is reducible, commutant dim 4; counts 8/4 vs 20/8, "
              "never 3). The entire selection lives in the single")
        print("         non-retained clause 'ker = carrier' (0/0 vs 12/60 "
              "extra modes) — exactly N6 escape (ii), still open.")
        print("         phi = -1 remains underived; B-BIT survives, "
              "sharpened: any future selector must supply that clause")
        print("         as genuinely separate input.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
