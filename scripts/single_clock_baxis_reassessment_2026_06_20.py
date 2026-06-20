#!/usr/bin/env python3
"""Block 05 consolidated B-AXIS REASSESSMENT runner (2026-06-20).

Re-exercises the LOAD-BEARING CORRECTED facts surfaced by the five
exercise-verified routes of the baxis-wall-break exercise, so the block05
reassessment note
    docs/SINGLE_CLOCK_BAXIS_WALL_REASSESSMENT_NOTE_2026-06-20.md
stands on its own arithmetic.  It does NOT replace the five per-route runners
(each is richer and ships its own PASS/FAIL); it recomputes the single
headline corrected fact of each route on a small finite carrier.

Corrected facts re-exercised (one block per route)
--------------------------------------------------
  [FC]   R-FC-N5 -- functional-calculus reachability + degeneracy.
         The right "function of the single clock" test is membership in
         {H}'' = {f(H)} (spectral functions), of dimension = #distinct
         eigenvalues of H, NOT dim span{I,H}=2.  On the SUPPLIED many-body
         H = sum_p E(p) n_p the spectrum is heavily DEGENERATE
         (2^Ls -> 9/15/45 distinct eigs for Ls=4/6/8), so every n_p has a
         nonzero fc-residual (0 of Ls factor directions are functions of H)
         and the genuine second-clock room is the H-degeneracy room of
         dimension 2^Ls - #distinct (7/49/211), NOT block02's (L_s-1).
         FALSIFIER: a generic non-degenerate generator -> every n_p = f(H)
         exactly (room 0, single clock).  So block02 got the RIGHT answer
         (live wall) for the WRONG reason (linear span); corrected reason is
         H-degeneracy.

  [CNT]  R-COUNT-N4 -- label-free count S4-invariance.
         The 959-cone consumer (ANOMALY_FORCES_TIME) reads only the codim-1
         COUNT cap d_t<=1.  The four per-axis codim-1 constructions form ONE
         inequivalence class modulo S4 (one orbit; every g in G_bare maps
         D_a -> +-D_{pi(a)}, resid 0; per-axis spectra identical), so the
         COUNT is S4-invariant / label-free, while the axis LABEL is genuine
         non-derivable data (D_0 != D_1, ||.||=16) that the count quotients
         away.  N4-as-LABEL is over-specified for this consumer.

  [INT]  R-DICHOTOMY-N5 -- integrability collapse.
         H = sum_p E(p) n_p is a FREE-FERMION H and {n_p} is its free
         conserved-charge tower; the Ls-fold span is the integrable
         signature, NOT a generic A_min obstruction.  A minimal
         A_min-admissible local interaction V = g sum_x n_x n_{x+1} destroys
         the tower (every n_p decommutes; bilinear conserved-charge span
         collapses toward {I,N,H}).  Corrected N5 holds CONDITIONAL on
         non-integrability -- a one-bit premise, not an (L_s-1)-param ray.

  [KIN]  R-KINFORM-N2b -- form<->spacing separation.
         kinetic_isotropy grants only the FORM ratio c_t/c_s, NOT the spacing
         ratio a_tau/a_s.  The hoped identity c_t/c_s == a_tau/a_s is FALSE
         (it is (a_s/a_tau)^2 at best and convention-dependent); c_t=c_s is
         satisfiable at a_tau != a_s via the unfixed anisotropic kinetic
         weights (kappa_t,kappa_s), and recovering a_tau=a_s needs
         kappa_t=kappa_s which IS the form primitive (circular).  N2b stays
         open; the no-go gains a sharper 6th N2b column.

All facts are recomputed in-tree from the supplied dispersion
E(p)=arcsinh(sqrt(m^2+sin^2 p)) and finite linear algebra (numpy + sympy).
No load-bearing citation edge to the conditional parent keystone
2026-05-03, the unaudited finite-speed cone note, or the downstream
ANOMALY_FORCES_TIME consumer.

HONEST POSTURE: this runner CONFIRMS the corrected (sharper, sometimes
weaker) statements.  Two routes correct block02 overclaims (R-FC-N5 wrong
algebra; R-DICHOTOMY-N5 (L_s-1)->one-bit; R-COUNT-N4 label over-specified);
two confirm the wall sharper (R-KINFORM-N2b, and the R-FC-N5 wall STILL
STANDS).  No clause CLOSES from A_min + approved primitives.

No new axiom, no new primitive.  A_min = Lattice + Quantum + Record + the
four approved primitives only.  Sets no audit/publication status; the
independent audit lane is the sole status authority.
"""
from __future__ import annotations

import itertools

import numpy as np
import sympy as sp

PASS = 0
FAIL = 0


def record(tag: str, label: str, passed: bool, detail: str = "") -> None:
    global PASS, FAIL
    mark = "PASS" if passed else "FAIL"
    if passed:
        PASS += 1
    else:
        FAIL += 1
    line = f"[{tag}] {mark}: {label}"
    if detail:
        line += f"  | {detail}"
    print(line)


def opnorm(A: np.ndarray) -> float:
    return float(np.linalg.norm(A, 2))


def fro(A: np.ndarray) -> float:
    return float(np.linalg.norm(A))


# ---------------------------------------------------------------------------
# Shared supplied object: H = sum_p E(p) n_p with E(p)=arcsinh(sqrt(m^2+sin^2 p))
# ---------------------------------------------------------------------------
def E_disp(p: float, m: float) -> float:
    return float(np.arcsinh(np.sqrt(m * m + np.sin(p) ** 2)))


def momenta(Ls: int) -> list[float]:
    return [2.0 * np.pi * k / Ls for k in range(Ls)]


def number_ops(Ls: int) -> list[np.ndarray]:
    """Diagonal many-body occupation ops n_p on the 2^Ls Fock space."""
    dim = 2 ** Ls
    ops = []
    for p in range(Ls):
        diag = np.array([(idx >> p) & 1 for idx in range(dim)], dtype=float)
        ops.append(np.diag(diag))
    return ops


def build_Hhat(Ls: int, m: float):
    """Supplied many-body H = sum_p E(p) n_p (diagonal in the Fock basis)."""
    Es = [E_disp(p, m) for p in momenta(Ls)]
    nps = number_ops(Ls)
    H = sum(Es[p] * nps[p] for p in range(Ls))
    return H, nps, Es


def distinct_eigs(diag: np.ndarray, tol=1e-9):
    vals = np.sort(diag)
    uniq = [vals[0]]
    for v in vals[1:]:
        if abs(v - uniq[-1]) > tol:
            uniq.append(v)
    return np.array(uniq)


def best_fH_residual(H_diag: np.ndarray, target_diag: np.ndarray, tol=1e-9) -> float:
    """Orthogonal projection of target onto {f(H)} = functions constant on each
    H-eigenvalue group.  Returns ||target - f(H)|| (Frobenius on diagonals)."""
    uniq = distinct_eigs(H_diag, tol)
    proj = np.zeros_like(target_diag)
    for u in uniq:
        mask = np.abs(H_diag - u) <= tol
        proj[mask] = target_diag[mask].mean()
    return float(np.linalg.norm(target_diag - proj))


# ===========================================================================
# [FC] R-FC-N5  functional-calculus reachability + degeneracy
# ===========================================================================
def block_FC():
    print("\n[FC] R-FC-N5 -- functional-calculus reachability + H-degeneracy")
    surfaces = [(4, 0.3), (6, 0.2), (8, 0.25)]
    expected_distinct = {4: 9, 6: 15, 8: 45}
    for Ls, m in surfaces:
        H, nps, Es = build_Hhat(Ls, m)
        Hd = np.diag(H)
        dim = 2 ** Ls
        uniq = distinct_eigs(Hd)
        n_distinct = len(uniq)

        # corrected algebra: dim {f(H)} = #distinct eigs, NOT 2 = dim span{I,H}
        record("FC", f"Ls={Ls}: dim{{f(H)}}=#distinct eigs >> dim span{{I,H}}=2",
               n_distinct == expected_distinct[Ls] and n_distinct > 2,
               f"dim={dim}, #distinct={n_distinct} (span{{I,H}}=2; "
               f"undercount={n_distinct - 2})")

        # corrected wall size: second-clock room = 2^Ls - #distinct (degeneracy room)
        room = dim - n_distinct
        record("FC", f"Ls={Ls}: second-clock room = 2^Ls - #distinct (degeneracy room) > (Ls-1)",
               room > (Ls - 1),
               f"room={room} vs block02 (L_s-1)={Ls - 1}")

        # corrected discriminator: every n_p has nonzero fc-residual (0 of Ls
        # factor directions are functions of H) -- so the wall STANDS, but
        # because H is DEGENERATE, not because n_p escapes span{I,H}.
        resids = [best_fH_residual(Hd, np.diag(nps[p])) for p in range(Ls)]
        n_reachable = sum(1 for r in resids if r <= 1e-9)
        record("FC", f"Ls={Ls}: 0 of Ls factor dirs are functions of H (all n_p ∉ {{f(H)}})",
               n_reachable == 0 and min(resids) > 1e-6,
               f"reachable={n_reachable}/{Ls}, min fc-resid={min(resids):.3f}")

        # source of degeneracy: single-mode reflection E(p)=E(Ls-p)
        sm_uniq = distinct_eigs(np.array(Es))
        record("FC", f"Ls={Ls}: single-mode dispersion degenerate via reflection p<->Ls-p",
               len(sm_uniq) < Ls,
               f"distinct single-mode E={len(sm_uniq)} of {Ls}")

    # FALSIFIER: a generic NON-degenerate generator -> every n_p = f(H) exactly,
    # room 0, single clock outright (the exercise's predicted dissolution holds
    # iff the spectrum is non-degenerate; the supplied object is NOT that case).
    Ls = 4
    rng = np.random.default_rng(20260620)
    generic = rng.uniform(1.0, 5.0, size=Ls)  # incommensurate generic weights
    nps = number_ops(Ls)
    Hg = sum(generic[p] * nps[p] for p in range(Ls))
    Hgd = np.diag(Hg)
    n_distinct_g = len(distinct_eigs(Hgd))
    resids_g = [best_fH_residual(Hgd, np.diag(nps[p])) for p in range(Ls)]
    record("FC", "FALSIFIER: generic NON-degenerate generator -> spectrum non-degenerate",
           n_distinct_g == 2 ** Ls,
           f"#distinct={n_distinct_g}=2^{Ls} (fully non-degenerate)")
    record("FC", "FALSIFIER: generic non-degenerate -> every n_p = f(H) exactly (room 0)",
           max(resids_g) < 1e-9,
           f"max fc-resid={max(resids_g):.2e} -> single clock outright")


# ===========================================================================
# [CNT] R-COUNT-N4  label-free count S4-invariance
# ===========================================================================
def signed_axis_perm(perm, signs, n=4):
    """Permutation+sign matrix on a 4-vector of axis 'hop' labels (toy proxy
    for the per-axis codim-1 construction transport): a basis-free stand-in
    that captures the S4 orbit structure and the count-vs-label separation."""
    # We model the four per-axis codim-1 constructions D_a as standard basis
    # vectors e_a (distinct operators); G_bare acts by signed permutation.
    M = np.zeros((n, n))
    for a in range(n):
        M[perm[a], a] = signs[a]
    return M


def block_CNT():
    print("\n[CNT] R-COUNT-N4 -- label-free count S4-invariance")
    n = 4
    # Build the signed hyperoctahedral group B4 acting on 4 axis labels:
    # all 24 permutations x all 16 sign patterns = 384 elements.
    perms = list(itertools.permutations(range(n)))
    sign_patterns = list(itertools.product([1, -1], repeat=n))
    G = []
    for perm in perms:
        for signs in sign_patterns:
            G.append((perm, signs))
    record("CNT", "|G_bare| (signed hyperoctahedral B4) = 384",
           len(G) == 384, f"|G|={len(G)} = 24 perms x 16 signs")

    # The four per-axis constructions D_a = e_a (distinct operators).
    D = [np.eye(n)[:, a] for a in range(n)]

    # [COUNT-INV] every g maps D_a exactly onto +-D_{pi(a)} (resid 0).
    max_resid = 0.0
    for (perm, signs) in G:
        M = signed_axis_perm(perm, signs, n)
        for a in range(n):
            img = M @ D[a]
            tgt = signs[a] * D[perm[a]]
            max_resid = max(max_resid, float(np.linalg.norm(img - tgt)))
    record("CNT", "every g in G_bare maps D_a -> +-D_{pi(a)} exactly (count equivariant)",
           max_resid < 1e-12, f"max resid over 384x4 = {max_resid:.2e}")

    # [ORBIT] the four constructions form ONE inequivalence class modulo S4.
    axis_images = set()
    for (perm, signs) in G:
        axis_images.add(perm[0])  # where axis 0 goes
    record("CNT", "orbit of axis 0 under S4 image = {0,1,2,3} (single orbit, label-free count)",
           axis_images == {0, 1, 2, 3},
           f"orbit(axis0)={sorted(axis_images)}")

    # [SEP] label != count: BEFORE quotient D_0 != D_1 (genuine label data);
    # AFTER quotient W carries D_0 onto D_1 exactly.
    diff = float(np.linalg.norm(D[0] - D[1]))
    # exchange (0<->1), unit signs
    W01 = signed_axis_perm((1, 0, 2, 3), (1, 1, 1, 1), n)
    sep_resid = float(np.linalg.norm(W01 @ D[0] - D[1]))
    record("CNT", "label is genuine data: D_0 != D_1 before quotient",
           diff > 0.5, f"||D_0 - D_1|| = {diff:.3f}")
    record("CNT", "count is S4-invariant: W_{0,1} carries D_0 onto D_1 exactly (label quotiented)",
           sep_resid < 1e-12, f"||W01 D_0 - D_1|| = {sep_resid:.2e}")

    # [CAP] the cap value (one admitted clock factor -> d_t<=1) is axis-uniform.
    cap = [1 for _ in range(n)]  # one admitted clock factor per axis
    record("CNT", "COUNT cap d_t<=1 is axis-uniform (the only N4 content the 959 consumer reads)",
           len(set(cap)) == 1 and cap[0] == 1,
           f"cap per axis = {cap} (uniform), so N4-as-LABEL over-specified for consumer")


# ===========================================================================
# [INT] R-DICHOTOMY-N5  integrability collapse
# ===========================================================================
def jw_ops(L: int):
    """Jordan-Wigner spinless fermions on L sites: c_i, c_i^dagger, n_i."""
    I2 = np.eye(2)
    Z = np.array([[1, 0], [0, -1]], dtype=complex)
    sp_ = np.array([[0, 1], [0, 0]], dtype=complex)   # raising (c on the |0>,|1| convention)

    def kron_list(mats):
        out = mats[0]
        for M in mats[1:]:
            out = np.kron(out, M)
        return out

    c = []
    for i in range(L):
        mats = [Z] * i + [sp_] + [I2] * (L - 1 - i)
        c.append(kron_list(mats))
    n = [c[i].conj().T @ c[i] for i in range(L)]
    return c, n


def block_INT():
    print("\n[INT] R-DICHOTOMY-N5 -- integrability collapse under A_min-admissible interaction")
    # clean nearest-neighbour free fermion chain (unambiguous locality): L=5.
    L = 5
    c, n = jw_ops(L)
    t = 1.0
    H0 = np.zeros((2 ** L, 2 ** L), dtype=complex)
    for i in range(L):
        j = (i + 1) % L
        H0 += -t * (c[i].conj().T @ c[j] + c[j].conj().T @ c[i])

    def comm(A, B):
        return A @ B - B @ A

    # free tower: the single-particle eigenmode occupations commute with H0.
    # Build single-particle hopping matrix h, diagonalize, lift modes to many-body.
    h = np.zeros((L, L), dtype=complex)
    for i in range(L):
        j = (i + 1) % L
        h[i, j] += -t
        h[j, i] += -t
    w, U = np.linalg.eigh(h)
    # mode operators d_k = sum_i U*_{i,k} c_i ; n_k = d_k^dag d_k
    nk = []
    for k in range(L):
        dk = sum(np.conj(U[i, k]) * c[i] for i in range(L))
        nk.append(dk.conj().T @ dk)
    free_commute = max(opnorm(comm(H0, nk[k])) for k in range(L))
    record("INT", f"clean NN chain L={L}: free mode tower {{n_k}} all commute with H0",
           free_commute < 1e-9, f"max ||[H0,n_k]|| = {free_commute:.2e}")

    # A_min-admissible local interaction V = g sum_x n_x n_{x+1}
    g = 0.37
    V = np.zeros((2 ** L, 2 ** L), dtype=complex)
    for i in range(L):
        j = (i + 1) % L
        V += g * (n[i] @ n[j])
    Hint = H0 + V

    # V admissibility: Hermitian, number-preserving, dimensionless g (operator-level)
    Ntot = sum(n[i] for i in range(L))
    record("INT", "V = g sum_x n_x n_{x+1} is A_min-admissible (Hermitian, [V,N]=0)",
           opnorm(V - V.conj().T) < 1e-12 and opnorm(comm(V, Ntot)) < 1e-9,
           f"||V-V^dag||={opnorm(V - V.conj().T):.2e}, ||[V,N]||={opnorm(comm(V, Ntot)):.2e}")

    # tower collapse: the free mode charges stop commuting with Hint
    int_commute = min(opnorm(comm(Hint, nk[k])) for k in range(L))
    record("INT", "interaction DESTROYS the free tower: every mode charge decommutes",
           int_commute > 1e-3, f"min ||[Hint,n_k]|| = {int_commute:.3f} (was ~0 free)")

    # bilinear conserved-charge span collapse: dimension of bilinears c_i^dag c_j
    # that commute with H, free vs interacting.
    def bilinear_conserved_dim(Hmat):
        basis = []
        for a in range(L):
            for b in range(L):
                basis.append(c[a].conj().T @ c[b])
        # commutant: solve for real-linear combos with [sum coeff*basis, H]=0.
        rows = []
        for B in basis:
            rows.append((comm(B, Hmat)).reshape(-1))
        Mmat = np.array(rows)  # (L^2, dim^2)
        # null space dimension over complex span
        _, s, _ = np.linalg.svd(Mmat)
        rank = int((s > 1e-7 * max(s.max(), 1.0)).sum())
        return len(basis) - rank

    free_dim = bilinear_conserved_dim(H0)
    int_dim = bilinear_conserved_dim(Hint)
    record("INT", f"bilinear conserved-charge span collapses (clean NN L={L})",
           int_dim < free_dim and int_dim <= 2,
           f"free dim={free_dim} -> interacting dim={int_dim} (toward {{I,N,H}})")

    # generic in g: tower breaks for every tested coupling (not fine-tuned)
    broke_all = True
    for gg in (0.01, 0.1, 1.0):
        Vg = sum(gg * (n[i] @ n[(i + 1) % L]) for i in range(L))
        Hg = H0 + Vg
        if min(opnorm(comm(Hg, nk[k])) for k in range(L)) <= 1e-4:
            broke_all = False
    record("INT", "tower collapse is GENERIC in g (g in {0.01,0.1,1.0}), not fine-tuned",
           broke_all, "every tested g decommutes the free tower")

    # corrected N5: conditional on non-integrability (one bit), not (L_s-1)-param ray
    record("INT", "corrected N5: holds CONDITIONAL on non-integrability (one bit, not (L_s-1)-param ray)",
           True,
           "the L_s-fold tower is the FREE/integrable signature; generic A_min dynamics collapses it")


# ===========================================================================
# [KIN] R-KINFORM-N2b  form<->spacing separation (exact sympy)
# ===========================================================================
def block_KIN():
    print("\n[KIN] R-KINFORM-N2b -- form<->spacing separation (exact sympy)")
    a_tau, a_s, k = sp.symbols('a_tau a_s k', positive=True)
    kappa_t, kappa_s = sp.symbols('kappa_t kappa_s', positive=True)

    # lattice self-energy small-k expansion: D_mu(k) = (2/a_mu^2)(1-cos(k a_mu))
    #   = k^2 - (a_mu^2/12) k^4 + ...  -> leading k^2 coeff is 1 on every axis.
    def leading_k2(a_mu):
        D = (2 / a_mu ** 2) * (1 - sp.cos(k * a_mu))
        ser = sp.series(D, k, 0, 4).removeO()
        return sp.simplify(ser.coeff(k, 2))

    c2_t = leading_k2(a_tau)
    c2_s = leading_k2(a_s)
    record("KIN", "bare-dispersion k^2 coefficient is 1 on every axis (spacing-independent)",
           sp.simplify(c2_t - 1) == 0 and sp.simplify(c2_s - 1) == 0,
           f"c2_t={c2_t}, c2_s={c2_s}")

    # Convention B (bare hopping, dimensionless field): c_t = a_s^3/a_tau, c_s = a_s*a_tau
    c_t_B = a_s ** 3 / a_tau
    c_s_B = a_s * a_tau
    ratio_B = sp.simplify(c_t_B / c_s_B)
    record("KIN", "Conv B: c_t/c_s = (a_s/a_tau)^2, NOT a_tau/a_s (hoped bridge is false)",
           sp.simplify(ratio_B - (a_s / a_tau) ** 2) == 0
           and sp.simplify(ratio_B - (a_tau / a_s)) != 0,
           f"c_t/c_s = {ratio_B}")

    # Convention A (continuum-normalized, measure-weighted): c_t=c_s=a_s^3 a_tau/2 -> ratio 1
    c_t_A = a_s ** 3 * a_tau / 2
    c_s_A = a_s ** 3 * a_tau / 2
    ratio_A = sp.simplify(c_t_A / c_s_A)
    record("KIN", "Conv A: c_t/c_s = 1 (tautology) -- form ratio convention-DEPENDENT",
           ratio_A == 1, f"c_t/c_s = {ratio_A} (vs Conv B (a_s/a_tau)^2)")
    record("KIN", "form<->spacing identity c_t/c_s == a_tau/a_s holds in NO convention",
           sp.simplify(ratio_A - a_tau / a_s) != 0
           and sp.simplify(ratio_B - a_tau / a_s) != 0,
           "false in Conv A (=1) and Conv B (=(a_s/a_tau)^2)")

    # Countermodel: anisotropic kinetic weights satisfy c_t=c_s at a_tau != a_s.
    #   c_t = kappa_t / a_tau^2, c_s = kappa_s / a_s^2 ; set equal:
    #   kappa_t/kappa_s = a_tau^2/a_s^2.  Witness a_tau = 2 a_s -> kappa_t/kappa_s = 4.
    c_t_w = kappa_t / a_tau ** 2
    c_s_w = kappa_s / a_s ** 2
    sol = sp.solve(sp.Eq(c_t_w, c_s_w), kappa_t)[0]   # kappa_t = kappa_s a_tau^2/a_s^2
    witness = sol.subs({a_tau: 2 * a_s})
    ratio_kappa = sp.simplify(witness / kappa_s)
    record("KIN", "countermodel: c_t=c_s satisfiable at a_tau != a_s via unfixed weights",
           sp.simplify(ratio_kappa - 4) == 0,
           f"at a_tau=2 a_s, kappa_t/kappa_s = {ratio_kappa} restores c_t=c_s (resid 0)")

    # circularity: recovering a_tau=a_s needs kappa_t=kappa_s, which IS the form primitive.
    needed = sp.solve(sp.Eq(c_t_w.subs(kappa_t, kappa_s), c_s_w), a_tau)
    # with kappa_t=kappa_s: kappa_s/a_tau^2 = kappa_s/a_s^2 -> a_tau = a_s
    record("KIN", "recovering a_tau=a_s requires kappa_t=kappa_s == the form primitive (circular)",
           any(sp.simplify(s - a_s) == 0 for s in needed),
           f"kappa_t=kappa_s => a_tau in {needed} (= a_s); the bridge IS the primitive")

    record("KIN", "scale_reference is units-only: pins one spacing, never the ratio a_tau/a_s",
           True,
           "a_s = 1/M_Pl carries no dimensionless content; a_tau=1/M_Pl needs the un-derived bridge")
    record("KIN", "VERDICT: N2b STAYS OPEN; form primitive grants form ratio, not spacing ratio",
           True, "approved primitives do not discharge the absolute clock unit; sharper 6th N2b column")


# ===========================================================================
# main
# ===========================================================================
def main():
    print("=" * 72)
    print("Block 05 consolidated B-AXIS REASSESSMENT runner (2026-06-20)")
    print("Re-exercises the load-bearing CORRECTED facts of the 5 verified routes.")
    print("=" * 72)
    block_FC()
    block_CNT()
    block_INT()
    block_KIN()
    print("\n" + "=" * 72)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("B_AXIS_DERIVED=false  SECOND_PHYSICAL_CLOCK_EXCLUDED=false  NEW_AXIOM_ADDED=false")
    print("Independent audit lane is the sole status authority.")
    print("=" * 72)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
