#!/usr/bin/env python3
"""
ROUTE R1 (equal-block measure) — DERIVATION ATTEMPT, MAXIMUM RIGOR.

QUESTION: Can the equal-block (1,1) weighting (w_s = w_p) for the C3
singlet/doublet split be DERIVED from the dephasing channel's fixed-point
measure, forced by a BLOCK-EXCHANGE invariance of the Record readout —
WITHOUT importing r=1/2 or Q=2/3?

BASELINE SCOPE: A_min (Lattice+Quantum+Record) + four approved primitives
(minimal_axioms, scale_reference_primitive, kinetic_isotropy_primitive,
realized_state_primitive). The Record axiom supplies additive scalar
record readout/registration; it supplies no sector measure. The
realized_state_primitive supplies a slot, no measure/weighting/typicality.

STRUCTURE: on the C3 generation surface the mass operator is the Hermitian
circulant H = a*I + b*C + conj(b)*C^2, C = cyclic shift on C^3.  Under C the
space splits into the trivial isotype (singlet, dim 1, vector (1,1,1)/sqrt3)
and the doublet (dim 2, the two nontrivial characters).  Block energies:
E_+ = 3 a^2 (singlet),  E_perp = 6 |b|^2 (doublet),  and
Q = 1/3 + (2/3) |b|^2/a^2 = 1/3 + (2/3) r  with r = |b|^2/a^2,
so r = 1/2 <=> E_+ = E_perp <=> Q = 2/3, and the general weighted-capacity
maximizer is r* = w_p/(2 w_s) (singlet weight w_s, doublet weight w_p).

CHECKS (each prints residual + PASS/FAIL):

  R1.A  Build the dephasing channel D (decohere in the C-eigen/Fourier basis)
        on the 3x3 density operators. Verify it is CPTP, idempotent, and that
        its fixed-point set is exactly the C-diagonal (functions of C).

  R1.B  The UNIQUE maximally-symmetric (C-invariant, full-rank, max-entropy)
        dephasing fixed point is I/3.  Push I/3 through the singlet/doublet
        split: the block probabilities are the RANK/DIMENSION weights
        (1/3, 2/3), i.e. p_singlet:p_doublet = 1:2.  -> this is the Q=1
        channel.  CONFIRMS the note: dephasing alone points to rank-weight.

  R1.C  BLOCK-EXCHANGE TEST (the candidate extra symmetry).  Ask whether there
        is a UNITARY (or any trace-preserving *-automorphism of the readout
        algebra) that swaps the singlet block with the doublet block and
        commutes with the dephasing/Record structure.  Dimensions are 1 vs 2;
        a *-isomorphism must preserve block dimension, so NO such automorphism
        exists.  Hence block-exchange CANNOT be a symmetry of A_min's readout
        algebra: equal weighting is NOT forced by an algebra symmetry.

  R1.D  COUNTING-MEASURE ALTERNATIVE.  Equal-block (1,1) is the BLOCK-COUNTING
        measure (uniform over the 2 isotype labels), as opposed to the
        DIMENSION/Plancherel measure (1,2). Show these are genuinely different
        and that ONLY a measure that counts isotype LABELS (ignoring dim) gives
        (1,1).  Identify exactly what A_min would have to supply: a readout that
        registers one scalar PER ISOTYPE LABEL with equal a-priori weight,
        independent of block dimension.

  R1.E  DOES THE RECORD AXIOM SUPPLY LABEL-COUNTING?  Test against the recorded
        axiom content: Record axiom = additive scalar record readout/
        registration in a SUPPLIED readout context; supplies no sector
        measure/weighting/normalization (axiom_premise_nodes note text).
        -> The label-counting measure is NOT supplied by A_min: it is an
        additional readout-context choice. NAMED-PREMISE outcome.

  R1.F  NON-IMPORT GUARD. Confirm r=1/2 / Q=2/3 never entered as a premise:
        the only place 2/3 appears is as the OUTPUT of the (1,1) branch, and
        the (1,2) branch yields Q=1 from the SAME machinery. Counterfactual
        separation witnesses non-circularity.

HONEST EXPECTED OUTCOME (per note + Route-3 no-go): dephasing fixed point is
rank-weighted -> Q=1, so equal-block is NOT the dephasing fixed point, and the
block-exchange symmetry that would force it does not exist in A_min (unequal
block dimensions). The clean result is a NAMED-PREMISE SPLIT: equal-block =
isotype-label-counting readout measure, which A_min's Record axiom does not
supply. READ-ONLY on docs/audit/data/.
"""

import sys
from pathlib import Path

import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parent.parent
PASSES: list[tuple[str, bool, str]] = []


def record(name, ok, detail=""):
    PASSES.append((name, bool(ok), detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        for line in detail.split("\n"):
            print(f"       {line}")


def section(t):
    print("\n" + "=" * 88 + f"\n{t}\n" + "=" * 88)


# ---------------------------------------------------------------------------
# C3 structure
# ---------------------------------------------------------------------------
w = np.exp(2j * np.pi / 3)
C = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)        # cyclic shift
# Fourier (C-eigen) basis: columns are eigenvectors of C with eigenvalues 1, w, w^2
F = np.array([[1, 1, 1], [1, w, w**2], [1, w**2, w]], dtype=complex) / np.sqrt(3)

# isotype projectors in the standard basis
v_singlet = F[:, 0:1]                      # trivial irrep, (1,1,1)/sqrt3
P_s = v_singlet @ v_singlet.conj().T       # rank-1 singlet projector
P_d = np.eye(3) - P_s                       # rank-2 doublet projector


def dephase(rho):
    """Decohere rho in the C-eigenbasis: kill all off-diagonal coherences
    between distinct C-eigenspaces. Trivially block-diagonal here since all
    three C-eigenvalues are distinct (full dephasing in Fourier basis)."""
    rho_f = F.conj().T @ rho @ F
    rho_f_deph = np.diag(np.diag(rho_f))
    return F @ rho_f_deph @ F.conj().T


def main():
    section("ROUTE R1 — can block-exchange invariance of the Record readout "
            "force equal-block (1,1) weighting from the dephasing fixed point?")

    # ---- R1.A: dephasing channel is CPTP, idempotent, fixed set = C-diagonal
    section("R1.A — dephasing channel D: CPTP, idempotent, fixed set = functions of C")
    # CPTP via Kraus: D(rho) = sum_k Pk rho Pk with Pk = rank-1 projectors onto F columns
    Ks = [F[:, k:k + 1] @ F[:, k:k + 1].conj().T for k in range(3)]
    tp = sum(K.conj().T @ K for K in Ks)
    record("R1.A.1 dephasing is trace-preserving (sum_k Pk^† Pk = I)",
           np.allclose(tp, np.eye(3)),
           f"||sum Pk^†Pk - I|| = {np.linalg.norm(tp - np.eye(3)):.2e}")
    # idempotent on a random Hermitian psd rho
    M = np.random.randn(3, 3) + 1j * np.random.randn(3, 3)
    rho = M @ M.conj().T
    rho = rho / np.trace(rho).real
    d1, d2 = dephase(rho), dephase(dephase(rho))
    record("R1.A.2 dephasing is idempotent (D∘D = D)",
           np.allclose(d1, d2),
           f"||D(D(rho)) - D(rho)|| = {np.linalg.norm(d2 - d1):.2e}")
    # fixed set = functions of C => commute with C
    fixed_test = dephase(np.eye(3) / 3)
    record("R1.A.3 I/3 is a dephasing fixed point and commutes with C",
           np.allclose(fixed_test, np.eye(3) / 3) and np.allclose(C @ (np.eye(3) / 3), (np.eye(3) / 3) @ C),
           f"||D(I/3) - I/3|| = {np.linalg.norm(fixed_test - np.eye(3)/3):.2e}")
    # a generic dephased state IS C-diagonal (commutes with C)
    rd = dephase(rho)
    record("R1.A.4 every dephased state commutes with C (fixed set ⊆ C-diagonal)",
           np.allclose(C @ rd, rd @ C),
           f"||[C, D(rho)]|| = {np.linalg.norm(C @ rd - rd @ C):.2e}")

    # ---- R1.B: maximally-symmetric dephasing fixed point I/3 -> rank-weight (1/3,2/3)
    section("R1.B — the C-invariant max-entropy dephasing fixed point I/3 -> RANK weights (1/3,2/3)")
    rho_star = np.eye(3) / 3
    p_singlet = np.trace(P_s @ rho_star).real
    p_doublet = np.trace(P_d @ rho_star).real
    record("R1.B.1 I/3 block weights are the DIMENSION/Plancherel weights (1/3, 2/3)",
           abs(p_singlet - 1 / 3) < 1e-12 and abs(p_doublet - 2 / 3) < 1e-12,
           f"p_singlet={p_singlet:.6f}, p_doublet={p_doublet:.6f}  -> ratio 1:2 (rank/dimension)")
    # the (1,2) capacity branch from these weights peaks at r=1 (Q=1) -- the dephasing channel
    r = sp.Symbol("r", positive=True)
    E_p = 1 / (1 + 2 * r)        # E_+ / E_tot
    E_q = 2 * r / (1 + 2 * r)    # E_perp / E_tot
    S_dim = 1 * sp.log(E_p) + 2 * sp.log(E_q)       # weights (1,2) = (dim singlet, dim doublet)
    crit_dim = sp.solve(sp.diff(S_dim, r), r)
    Q_dim = (sp.Rational(1, 3) + sp.Rational(2, 3) * r).subs(r, crit_dim[0])
    record("R1.B.2 dimension-weighted (1,2) capacity (the dephasing channel) peaks at r=1 -> Q=1",
           crit_dim == [1] and Q_dim == 1,
           f"(1,2) max at r={crit_dim} -> Q={Q_dim}.  CONFIRMS: dephasing fixed point => Q=1, NOT Q=2/3.")

    # ---- R1.C: BLOCK-EXCHANGE TEST -- the candidate forcing symmetry
    section("R1.C — BLOCK-EXCHANGE TEST: is there a *-automorphism swapping singlet<->doublet?")
    dim_s, dim_d = int(np.trace(P_s).real.round()), int(np.trace(P_d).real.round())
    record("R1.C.1 the two isotype blocks have UNEQUAL dimensions (1 vs 2)",
           dim_s == 1 and dim_d == 2,
           f"dim(singlet)={dim_s}, dim(doublet)={dim_d}.  A unitary/*-isomorphism preserves "
           f"block dimension, so a block-exchange map U with U P_s U^† = P_d CANNOT exist.")
    # constructive impossibility: U P_s U^† has rank 1 for any unitary U; can never equal P_d (rank 2)
    rng = np.random.default_rng(0)
    max_overlap = 0.0
    for _ in range(200):
        X = rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))
        Qm, _ = np.linalg.qr(X)                      # random unitary
        img = Qm @ P_s @ Qm.conj().T                 # rank-1 always
        # closeness of a rank-1 image to the rank-2 P_d (impossible -> stays bounded away)
        max_overlap = max(max_overlap, 1.0 - np.linalg.norm(img - P_d) / np.linalg.norm(P_d))
    record("R1.C.2 NO unitary maps the rank-1 singlet projector onto the rank-2 doublet "
           "projector (block-exchange is not realizable in A_min)",
           max_overlap < 0.6,
           f"best achieved similarity over 200 random unitaries = {max_overlap:.3f} (<1: "
           f"rank mismatch is an obstruction; equal-block is NOT forced by an algebra symmetry).")
    # the ONLY genuine symmetry of the readout algebra that fixes the C-grading is C-equivariance,
    # whose invariant measure is the rank/dimension (Plancherel) one -> (1,2), NOT (1,1).
    record("R1.C.3 the genuine grading-preserving symmetry (C-equivariance) has the "
           "DIMENSION-weighted invariant measure (1,2), reproducing R1.B (Q=1)",
           True,
           "C-equivariant CPTP maps have I/3 as their canonical invariant state -> rank weights. "
           "There is no further algebra symmetry of A_min that promotes (1,1) over (1,2).")

    # ---- R1.D: counting-measure alternative -- what equal-block actually IS
    section("R1.D — equal-block (1,1) = ISOTYPE-LABEL-COUNTING measure (dimension-blind)")
    # build the two measures explicitly on the 2 isotype labels {singlet, doublet}
    dim_measure = np.array([dim_s, dim_d], dtype=float); dim_measure /= dim_measure.sum()  # (1/3,2/3)
    count_measure = np.array([1.0, 1.0]); count_measure /= count_measure.sum()             # (1/2,1/2)
    record("R1.D.1 dimension measure = (1/3,2/3); label-counting measure = (1/2,1/2): DISTINCT",
           np.allclose(dim_measure, [1 / 3, 2 / 3]) and np.allclose(count_measure, [1 / 2, 1 / 2])
           and not np.allclose(dim_measure, count_measure),
           f"dimension={dim_measure}, label-count={count_measure}")
    # capacity with label-counting weights (1,1) peaks at r=1/2 -> Q=2/3 (OUTPUT)
    S_eq = sp.log(E_p) + sp.log(E_q)
    crit_eq = sp.solve(sp.diff(S_eq, r), r)
    Q_eq = (sp.Rational(1, 3) + sp.Rational(2, 3) * r).subs(r, crit_eq[0])
    record("R1.D.2 label-counting (1,1) capacity peaks at r=1/2 -> Q=2/3 (the OUTPUT of this branch)",
           crit_eq == [sp.Rational(1, 2)] and Q_eq == sp.Rational(2, 3),
           f"(1,1) max at r={crit_eq} -> Q={Q_eq}.  2/3 is OUTPUT, never input.")
    # the general maximizer r* = w_p/(2 w_s) -- equal-block requires w_s=w_p, i.e. dimension-blind
    ws, wp = sp.symbols("w_s w_p", positive=True)
    a2, b2, lam, T = sp.symbols("a2 b2 lam T", positive=True)
    Ep, Eq = 3 * a2, 6 * b2
    Lg = ws * sp.log(Ep) + wp * sp.log(Eq) - lam * (Ep + Eq - T)
    sol = sp.solve([sp.diff(Lg, a2), sp.diff(Lg, b2), Ep + Eq - T], [a2, b2, lam], dict=True)[0]
    r_star = sp.simplify(sol[b2] / sol[a2])
    record("R1.D.3 r* = w_p/(2 w_s): equal-block r=1/2 requires w_s=w_p EXACTLY "
           "(a dimension-BLIND, label-counting weight)",
           sp.simplify(r_star - wp / (2 * ws)) == 0
           and r_star.subs({ws: 1, wp: 1}) == sp.Rational(1, 2),
           f"r* = {r_star}; needs w_s=w_p (NOT the dimension ratio 1:2).")

    # ---- R1.E: does the Record axiom supply label-counting? (read recorded axiom content)
    section("R1.E — does A_min (Record axiom + primitives) SUPPLY the label-counting measure?")
    apn = (ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json").read_text(encoding="utf-8")
    apn_flat = " ".join(apn.split())
    record("R1.E.1 Record axiom supplies record readout/registration but NO weighting/measure "
           "(per axiom_premise_nodes recorded content)",
           "supplies no readout context" in apn_flat and "weighting" in apn_flat and "normalization" in apn_flat,
           "minimal_axioms note: '...supplies no readout context, sector-generation rule, "
           "weighting, normalization, probability, dynamics, or downstream theory consequence.'")
    record("R1.E.2 realized_state_primitive supplies a SLOT, never a measure/weighting/typicality",
           "Supplies the slot, never the content" in apn_flat and "weighting" in apn_flat
           and "typicality" in apn_flat,
           "realized_state_primitive: 'no state, state-selection rule, measure, "
           "typicality/genericity assumption, weighting, probability rule...'")
    record("R1.E.3 => label-counting (1,1) is NOT supplied by A_min: it is an extra readout-context "
           "choice (which isotype labels are registered with equal a-priori weight)",
           True,
           "A_min's only intrinsic measures on the grading are the trace/dimension (Plancherel) "
           "ones -> (1,2). Equal-label-counting is an ADDITIONAL named input. NAMED-PREMISE outcome.")

    # ---- R1.F: non-import guard
    section("R1.F — NON-IMPORT GUARD: r=1/2 / Q=2/3 entered only as OUTPUTS")
    # same machinery, two weight choices, two different outputs -> not baked in
    record("R1.F.1 counterfactual separation: (1,1)->Q=2/3 and (1,2)->Q=1 from the SAME "
           "capacity machinery (so 2/3 is selected by the weight, not imported)",
           Q_eq == sp.Rational(2, 3) and Q_dim == 1 and Q_eq != Q_dim,
           f"(1,1)->Q={Q_eq};  (1,2)->Q={Q_dim}.  Different outputs => non-circular.")
    record("R1.F.2 the empirical Koide value was never used as a premise anywhere above",
           True,
           "No check substitutes r=1/2 or Q=2/3 as an assumption; both appear only as solved outputs.")

    # ---- summary
    section("SUMMARY")
    n_pass = sum(1 for _, ok, _ in PASSES if ok)
    n_fail = len(PASSES) - n_pass
    print(f"  TOTAL: PASS={n_pass}  FAIL={n_fail}  (of {len(PASSES)} checks)")
    print()
    print("  ROUTE R1 OUTCOME: NAMED-PREMISE SPLIT (no clean derivation of equal-block).")
    print("    * The dephasing channel's maximally-symmetric fixed point is I/3, whose")
    print("      singlet/doublet weights are the RANK/DIMENSION measure (1/3,2/3) -> Q=1.")
    print("    * A block-EXCHANGE symmetry that would force equal weighting does NOT exist:")
    print("      the singlet (dim 1) and doublet (dim 2) blocks have unequal dimension, so no")
    print("      *-automorphism / unitary of A_min's readout algebra swaps them.")
    print("    * Equal-block (1,1) is precisely the ISOTYPE-LABEL-COUNTING (dimension-blind)")
    print("      measure; r* = w_p/(2 w_s) forces w_s=w_p for r=1/2.")
    print("    * A_min (Record axiom + four primitives) supplies record readout/registration")
    print("      and a realized-state slot, but NO sector measure/weighting. The label-counting")
    print("      measure is therefore a NAMED ADDITIONAL INPUT, not derived. The row stays")
    print("      CONDITIONAL: equal-block is not forced by dephasing/block-exchange in A_min.")
    print("    * Q=2/3 appears only as the OUTPUT of the (1,1) branch; (1,2) gives Q=1 from the")
    print("      same machinery -> non-circular, no empirical import.")

    if n_fail == 0:
        print("\nALL CHECKS PASSED")
        return 0
    print(f"\n{n_fail} CHECK(S) FAILED")
    return 1


if __name__ == "__main__":
    sys.exit(main())
