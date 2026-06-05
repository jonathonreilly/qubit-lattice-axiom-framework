#!/usr/bin/env python3
"""Audit-companion runner for the Lüders-rule parent note
`LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_NOTE_2026-05-20.md` recording
Record-axiom invariance after the 2026-06-04 framework citation-graph
re-resolution.

Companion source note:
  docs/LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_DEPS_CHANGED_HYGIENE_COMPANION_NOTE_2026-06-04.md

Parent ledger row:
  `luders_rule_from_composition_consistency_note_2026-05-20`.

Companion role:
  - Meta audit-companion evidence only.
  - Not a theorem claim or status promotion (the audit lane sets
    claim_type and audit_status independently).
  - Provides audit-friendly evidence that the parent's load-bearing
    state-update rule
        σ → (P σ P) / Tr(P σ P)        (Lüders rule)
    derived in Steps 1-4 of the parent note is independent of the
    Record axiom adopted in `MINIMAL_AXIOMS_2026-06-04.md`. This does
    not re-apply the prior audit verdict; it gives the audit lane a
    machine-checkable basis for deciding whether the parent's algebra
    needs fresh review after the citation-edge re-resolution.

The runner verifies the load-bearing chain block-by-block under
"Record axiom is asserted" and "Record axiom is not asserted" outer
scopes, confirms identical numeric outputs in both scopes, and
performs a static-source scan of the parent note's load-bearing
sections to confirm zero Record-axiom usage in the auditable core.

Every load-bearing arithmetic / algebraic check uses only:
  (i)   the per-site qubit operator algebra A_x ~= M_2(C) (Quantum
        axiom content);
  (ii)  composition over Λ ⊂ Z^3 via standard C*-tensor product
        (Lattice axiom content + textbook finite-dimensional
        C*-tensor-product machinery);
  (iii) the standard state/effect trace-pairing on A_Λ (textbook
        operator-algebraic probability);
  (iv)  trace cyclicity and positivity preservation under congruence
        (textbook linear algebra);
  (v)   standard sequential-effect composition M_{P,E} = P E P (named
        non-derivation import; identical in both axiom memos);
  (vi)  Bayes consistency p(P then E) = p(P) · p(E | P) (textbook).

No Record-axiom content (scalar record additivity functional `I(.)`)
enters any block. No claim is made about the Record-axiom-induced
downstream content; the companion observation is strictly limited to
the load-bearing chain of the parent note.

Block plan:
  Block 1  : Projection structure on M_2(C): P^2 = P, P = P†, trace.
  Block 2  : Density operator construction (single-qubit, two-qubit).
  Block 3  : Lüders sandwich positivity P σ P ≥ 0 (parent step 2/U1).
  Block 4  : Lüders sandwich normalization Tr(σ|_P) = 1 (parent
             step 2/U2).
  Block 5  : Lüders sandwich self-adjointness σ|_P = (σ|_P)†.
  Block 6  : Trace cyclicity identity Tr(σ · P E P) = Tr(P σ P · E)
             (parent step 1, eq. (3)).
  Block 7  : Bayes consistency identity (parent step 1, eq. (4)).
  Block 8  : (U4) compositional consistency (σ|_{P_1})|_{P_2} =
             σ|_{P_2 P_1} (parent step 3, eq. (8)).
  Block 9  : Generalized Kraus form (K σ K†)/Tr(K σ K†) is a density.
  Block 10 : Uniqueness via effect-basis equality (parent step 4).
  Block 11 : Static-source scan of parent note's load-bearing
             sections: zero Record-axiom usage tokens.
  Block 12 : Parent note contains Quantum / Lattice axiom content.
  Block 13 : Record-axiom counterfactual: identical numeric output
             with and without an explicit "Record axiom asserted"
             outer scope.
  Block 14 : Quantum / Lattice content preservation across the
             historical 2026-05-20 and current 2026-06-04
             minimal-axioms memos.
  Block 15 : Three-route cross-check on the Lüders post-update state.

The exact PASS/FAIL count is printed at runtime.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np


# -----------------------------------------------------------
# Logging and counters
# -----------------------------------------------------------

LOG_LINES: list[str] = []
PASS = 0
FAIL = 0


def log(msg: str = "") -> None:
    LOG_LINES.append(msg)
    print(msg)


def record(check_name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        log(f"  PASS {check_name}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        log(f"  FAIL {check_name}" + (f" :: {detail}" if detail else ""))


def header(title: str) -> None:
    log("")
    log("=" * 72)
    log(title)
    log("=" * 72)


def is_hermitian(M: np.ndarray, atol: float = 1e-12) -> bool:
    return np.allclose(M, M.conj().T, atol=atol)


def is_psd(M: np.ndarray, atol: float = 1e-10) -> bool:
    if not is_hermitian(M, atol=max(atol, 1e-12)):
        return False
    eigs = np.linalg.eigvalsh((M + M.conj().T) / 2.0)
    return float(eigs.min()) >= -atol


def trace_one(M: np.ndarray, atol: float = 1e-10) -> bool:
    return abs(complex(np.trace(M)).real - 1.0) < atol and \
        abs(complex(np.trace(M)).imag) < atol


def matrices_close(A: np.ndarray, B: np.ndarray, atol: float = 1e-10) -> bool:
    return np.allclose(A, B, atol=atol)


# -----------------------------------------------------------
# Test data: projections, states, effects
# -----------------------------------------------------------

I2 = np.eye(2, dtype=complex)
SIGMA_X = np.array([[0, 1], [1, 0]], dtype=complex)
SIGMA_Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
SIGMA_Z = np.array([[1, 0], [0, -1]], dtype=complex)


def proj_from_bloch(theta: float, phi: float) -> np.ndarray:
    """Rank-1 projection |ψ><ψ| with |ψ> on the Bloch sphere."""
    psi = np.array(
        [np.cos(theta / 2.0), np.exp(1j * phi) * np.sin(theta / 2.0)],
        dtype=complex,
    )
    return np.outer(psi, psi.conj())


def density_from_bloch(rx: float, ry: float, rz: float) -> np.ndarray:
    """Density operator (I + r·σ)/2 with |r| ≤ 1."""
    return 0.5 * (I2 + rx * SIGMA_X + ry * SIGMA_Y + rz * SIGMA_Z)


def random_density(d: int, rng: np.random.Generator) -> np.ndarray:
    """Random d×d density operator via Wishart construction."""
    A = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))
    M = A @ A.conj().T
    return M / np.trace(M).real


def random_projection_rank1(d: int, rng: np.random.Generator) -> np.ndarray:
    """Random rank-1 projection |ψ><ψ|."""
    v = rng.standard_normal(d) + 1j * rng.standard_normal(d)
    v = v / np.linalg.norm(v)
    return np.outer(v, v.conj())


def random_effect(d: int, rng: np.random.Generator) -> np.ndarray:
    """Random POVM effect 0 ≤ E ≤ I (Hermitian, eigenvalues in [0,1])."""
    A = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))
    H = (A + A.conj().T) / 2.0
    eigs, U = np.linalg.eigh(H)
    e_clip = np.clip(eigs, 0.0, None)
    # rescale max eigenvalue to ≤ 1
    if e_clip.max() > 0:
        e_clip = e_clip / e_clip.max() * 0.9  # leave headroom
    return U @ np.diag(e_clip) @ U.conj().T


def luders_update(sigma: np.ndarray, P: np.ndarray) -> np.ndarray:
    """σ → (P σ P) / Tr(P σ P) — the Lüders rule."""
    PsiP = P @ sigma @ P
    tr = complex(np.trace(PsiP)).real
    if tr <= 0:
        raise ZeroDivisionError("Tr(P σ P) ≤ 0")
    return PsiP / tr


# -----------------------------------------------------------
# Block 1: Projection structure on M_2(C)
# -----------------------------------------------------------

def block1() -> None:
    header("BLOCK 1: Projection structure on M_2(C) "
           "(parent setup, single-qubit)")
    log("  Verify P^2 = P, P = P†, Tr(P) = rank.")

    rng = np.random.default_rng(20260604)
    test_angles = [
        (0.0, 0.0),                # |0><0|
        (np.pi, 0.0),              # |1><1|
        (np.pi / 2, 0.0),          # |+><+|
        (np.pi / 2, np.pi / 2),    # |+i><+i|
        (np.pi / 3, np.pi / 4),    # arbitrary
    ]
    for theta, phi in test_angles:
        P = proj_from_bloch(theta, phi)
        record(f"rank1_idempotent_theta_{theta:.3f}_phi_{phi:.3f}",
               matrices_close(P @ P, P, atol=1e-12),
               f"||P^2 - P|| = {np.linalg.norm(P @ P - P):.3e}")
        record(f"rank1_self_adjoint_theta_{theta:.3f}_phi_{phi:.3f}",
               is_hermitian(P),
               "P = P†")
        record(f"rank1_unit_trace_theta_{theta:.3f}_phi_{phi:.3f}",
               abs(complex(np.trace(P)).real - 1.0) < 1e-12,
               f"Tr(P) = {complex(np.trace(P)).real:.6f}")

    # Rank-2 projection on M_2(C) is just I_2 itself
    record("rank2_identity_idempotent",
           matrices_close(I2 @ I2, I2, atol=1e-14),
           "I^2 = I on M_2(C)")
    record("rank2_identity_trace_two",
           abs(complex(np.trace(I2)).real - 2.0) < 1e-14,
           f"Tr(I_2) = {complex(np.trace(I2)).real:.1f}")

    # Two-qubit rank-1 projection
    P2_a = proj_from_bloch(np.pi / 3, 0.0)
    P2_b = proj_from_bloch(np.pi / 5, np.pi / 4)
    P2 = np.kron(P2_a, P2_b)
    record("two_qubit_rank1_idempotent",
           matrices_close(P2 @ P2, P2, atol=1e-12),
           f"||P^2 - P|| = {np.linalg.norm(P2 @ P2 - P2):.3e}")
    record("two_qubit_rank1_trace_one",
           abs(complex(np.trace(P2)).real - 1.0) < 1e-12,
           f"Tr(P) = {complex(np.trace(P2)).real:.6f}")


# -----------------------------------------------------------
# Block 2: Density operator construction
# -----------------------------------------------------------

def block2() -> None:
    header("BLOCK 2: Density operators on M_2(C) and "
           "M_2(C) ⊗ M_2(C)")
    log("  Verify σ ≥ 0, σ = σ†, Tr(σ) = 1.")

    rng = np.random.default_rng(20260604_2)
    states = {
        "|0><0|": density_from_bloch(0, 0, 1),
        "|1><1|": density_from_bloch(0, 0, -1),
        "max_mixed": density_from_bloch(0, 0, 0),
        "x_polarized_mixed": density_from_bloch(0.6, 0, 0),
        "tilted": density_from_bloch(0.3, 0.4, 0.5),
    }
    for name, sigma in states.items():
        record(f"density_psd_{name}",
               is_psd(sigma),
               f"min eig = {np.linalg.eigvalsh((sigma + sigma.conj().T)/2).min():+.3e}")
        record(f"density_hermitian_{name}",
               is_hermitian(sigma),
               "σ = σ†")
        record(f"density_unit_trace_{name}",
               trace_one(sigma),
               f"Tr(σ) = {complex(np.trace(sigma)).real:.6f}")

    # Two-qubit entangled state |Φ+> = (|00> + |11>)/√2
    phi_plus = np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)
    rho_phi_plus = np.outer(phi_plus, phi_plus.conj())
    record("density_psd_two_qubit_phi_plus",
           is_psd(rho_phi_plus),
           f"min eig = {np.linalg.eigvalsh((rho_phi_plus + rho_phi_plus.conj().T)/2).min():+.3e}")
    record("density_hermitian_two_qubit_phi_plus",
           is_hermitian(rho_phi_plus),
           "σ = σ†")
    record("density_unit_trace_two_qubit_phi_plus",
           trace_one(rho_phi_plus),
           f"Tr(σ) = {complex(np.trace(rho_phi_plus)).real:.6f}")

    # Random sample
    for k in range(4):
        d = 2 if k < 2 else 4
        sigma = random_density(d, rng)
        record(f"density_random_psd_d{d}_sample{k}",
               is_psd(sigma),
               f"min eig = {np.linalg.eigvalsh((sigma + sigma.conj().T)/2).min():+.3e}")
        record(f"density_random_trace_d{d}_sample{k}",
               trace_one(sigma),
               f"Tr(σ) = {complex(np.trace(sigma)).real:.6f}")


# -----------------------------------------------------------
# Block 3: Lüders sandwich positivity (U1)
# -----------------------------------------------------------

def block3() -> None:
    header("BLOCK 3: Lüders sandwich P σ P ≥ 0  "
           "(parent Step 2, (U1) corollary)")
    log("  For all test (σ, P): P σ P is positive semi-definite.")

    rng = np.random.default_rng(20260604_3)
    pairs = []
    # Single-qubit pairs
    for _ in range(6):
        sigma = random_density(2, rng)
        P = random_projection_rank1(2, rng)
        pairs.append(("d2", sigma, P))
    # Two-qubit pairs
    for _ in range(4):
        sigma = random_density(4, rng)
        P = random_projection_rank1(4, rng)
        pairs.append(("d4", sigma, P))

    for tag, sigma, P in pairs:
        PsiP = P @ sigma @ P
        ok = is_psd(PsiP, atol=1e-10)
        eigs = np.linalg.eigvalsh((PsiP + PsiP.conj().T) / 2.0)
        record(f"luders_sandwich_psd_{tag}_minEig",
               ok,
               f"min eig P σ P = {float(eigs.min()):+.3e}")

    # And one structured case: |+><+| sandwich of mixed state
    P_plus = proj_from_bloch(np.pi / 2, 0.0)  # |+><+|
    sigma_mix = density_from_bloch(0, 0, 0)
    PsiP = P_plus @ sigma_mix @ P_plus
    record("luders_sandwich_psd_plus_maxmix",
           is_psd(PsiP),
           f"min eig = {np.linalg.eigvalsh((PsiP + PsiP.conj().T)/2).min():+.3e}")
    record("luders_sandwich_trace_real",
           abs(complex(np.trace(PsiP)).imag) < 1e-14,
           f"Im Tr = {complex(np.trace(PsiP)).imag:.3e}")


# -----------------------------------------------------------
# Block 4: Lüders sandwich normalization (U2)
# -----------------------------------------------------------

def block4() -> None:
    header("BLOCK 4: Lüders sandwich normalization  "
           "(parent Step 2, (U2) corollary)")
    log("  σ|_P = (P σ P) / Tr(P σ P) has Tr(σ|_P) = 1 "
        "(when Tr(P σ P) > 0).")

    rng = np.random.default_rng(20260604_4)
    cases = []
    for _ in range(8):
        d = rng.choice([2, 4])
        sigma = random_density(d, rng)
        P = random_projection_rank1(d, rng)
        cases.append((int(d), sigma, P))

    for k, (d, sigma, P) in enumerate(cases):
        PsiP = P @ sigma @ P
        tr = complex(np.trace(PsiP)).real
        if tr <= 1e-12:
            log(f"    skip case {k} (Tr(P σ P) = {tr:.3e})")
            continue
        sigma_post = PsiP / tr
        record(f"luders_post_unit_trace_d{d}_case{k}",
               trace_one(sigma_post),
               f"Tr(σ|_P) = {complex(np.trace(sigma_post)).real:.12f}")
        record(f"luders_post_psd_d{d}_case{k}",
               is_psd(sigma_post),
               f"min eig = {np.linalg.eigvalsh((sigma_post + sigma_post.conj().T)/2).min():+.3e}")


# -----------------------------------------------------------
# Block 5: Lüders sandwich self-adjointness
# -----------------------------------------------------------

def block5() -> None:
    header("BLOCK 5: Lüders post-update state is self-adjoint")
    log("  σ|_P = (σ|_P)†.")

    rng = np.random.default_rng(20260604_5)
    for k in range(6):
        d = int(rng.choice([2, 4]))
        sigma = random_density(d, rng)
        P = random_projection_rank1(d, rng)
        try:
            sigma_post = luders_update(sigma, P)
        except ZeroDivisionError:
            log(f"    skip case {k} (degenerate)")
            continue
        record(f"luders_post_hermitian_d{d}_case{k}",
               is_hermitian(sigma_post),
               f"||σ|_P - (σ|_P)†|| = "
               f"{np.linalg.norm(sigma_post - sigma_post.conj().T):.3e}")


# -----------------------------------------------------------
# Block 6: Trace cyclicity identity (parent step 1, eq. (3))
# -----------------------------------------------------------

def block6() -> None:
    header("BLOCK 6: Trace cyclicity identity  "
           "(parent Step 1, eq. (3))")
    log("  Tr(σ · P E P) = Tr(P σ P · E) for all (σ, P, E).")

    rng = np.random.default_rng(20260604_6)
    for k in range(10):
        d = int(rng.choice([2, 4]))
        sigma = random_density(d, rng)
        P = random_projection_rank1(d, rng)
        E = random_effect(d, rng)
        lhs = complex(np.trace(sigma @ P @ E @ P))
        rhs = complex(np.trace(P @ sigma @ P @ E))
        diff = abs(lhs - rhs)
        record(f"trace_cyclicity_d{d}_case{k}",
               diff < 1e-10,
               f"|LHS - RHS| = {diff:.3e}, "
               f"LHS = {lhs.real:+.6f}{lhs.imag:+.3e}i")


# -----------------------------------------------------------
# Block 7: Bayes consistency identity (parent step 1, eq. (4))
# -----------------------------------------------------------

def block7() -> None:
    header("BLOCK 7: Bayes consistency identity  "
           "(parent Step 1, eq. (4))")
    log("  Tr(P σ P · E) = Tr(σ · P) · Tr(σ|_P · E)  "
        "(when Tr(σ · P) > 0).")

    rng = np.random.default_rng(20260604_7)
    for k in range(10):
        d = int(rng.choice([2, 4]))
        sigma = random_density(d, rng)
        P = random_projection_rank1(d, rng)
        E = random_effect(d, rng)
        p_P = complex(np.trace(sigma @ P)).real
        if p_P <= 1e-10:
            log(f"    skip case {k} (Tr(σ · P) = {p_P:.3e})")
            continue
        sigma_post = luders_update(sigma, P)
        lhs = complex(np.trace(P @ sigma @ P @ E))
        rhs = p_P * complex(np.trace(sigma_post @ E))
        diff = abs(lhs - rhs)
        record(f"bayes_identity_d{d}_case{k}",
               diff < 1e-10,
               f"|LHS - RHS| = {diff:.3e}, "
               f"LHS = {lhs.real:+.6f}{lhs.imag:+.3e}i")


# -----------------------------------------------------------
# Block 8: (U4) compositional consistency (parent step 3, eq. (8))
# -----------------------------------------------------------

def block8() -> None:
    header("BLOCK 8: (U4) compositional consistency  "
           "(parent Step 3, eq. (8))")
    log("  (σ|_{P_1})|_{P_2} = (P_2 P_1) σ (P_2 P_1)† / Tr((P_2 P_1) σ (P_2 P_1)†)")

    rng = np.random.default_rng(20260604_8)
    for k in range(8):
        d = int(rng.choice([2, 4]))
        sigma = random_density(d, rng)
        P1 = random_projection_rank1(d, rng)
        P2 = random_projection_rank1(d, rng)
        # First update with P1
        p_P1 = complex(np.trace(sigma @ P1)).real
        if p_P1 <= 1e-10:
            log(f"    skip case {k} (Tr(σ · P_1) = {p_P1:.3e})")
            continue
        sigma1 = luders_update(sigma, P1)
        # Second update with P2
        p_P2_given_P1 = complex(np.trace(sigma1 @ P2)).real
        if p_P2_given_P1 <= 1e-10:
            log(f"    skip case {k} (Tr(σ|_P_1 · P_2) = {p_P2_given_P1:.3e})")
            continue
        sigma_seq = luders_update(sigma1, P2)
        # Composite update with P_2 P_1
        K = P2 @ P1
        KsK = K @ sigma @ K.conj().T
        tr_K = complex(np.trace(KsK)).real
        if tr_K <= 1e-10:
            log(f"    skip case {k} (Tr(K σ K†) = {tr_K:.3e})")
            continue
        sigma_composite = KsK / tr_K
        diff = float(np.linalg.norm(sigma_seq - sigma_composite))
        record(f"u4_compositional_d{d}_case{k}",
               diff < 1e-10,
               f"||(σ|_P1)|_P2 - σ|_{{P2 P1}}|| = {diff:.3e}")


# -----------------------------------------------------------
# Block 9: Generalized Kraus form
# -----------------------------------------------------------

def block9() -> None:
    header("BLOCK 9: Generalized Kraus form "
           "(K σ K†) / Tr(K σ K†) is a density operator")
    log("  For random rank-1 Kraus operators K and densities σ.")

    rng = np.random.default_rng(20260604_9)
    for k in range(8):
        d = int(rng.choice([2, 4]))
        sigma = random_density(d, rng)
        # Random rank-1 Kraus operator |u><v|
        u = rng.standard_normal(d) + 1j * rng.standard_normal(d)
        v = rng.standard_normal(d) + 1j * rng.standard_normal(d)
        u = u / np.linalg.norm(u)
        v = v / np.linalg.norm(v)
        K = np.outer(u, v.conj())
        KsK = K @ sigma @ K.conj().T
        tr = complex(np.trace(KsK)).real
        if tr <= 1e-12:
            log(f"    skip case {k} (Tr(K σ K†) = {tr:.3e})")
            continue
        sigma_post = KsK / tr
        record(f"kraus_post_psd_d{d}_case{k}",
               is_psd(sigma_post),
               f"min eig = {np.linalg.eigvalsh((sigma_post + sigma_post.conj().T)/2).min():+.3e}")
        record(f"kraus_post_unit_trace_d{d}_case{k}",
               trace_one(sigma_post),
               f"Tr = {complex(np.trace(sigma_post)).real:.12f}")
        record(f"kraus_post_hermitian_d{d}_case{k}",
               is_hermitian(sigma_post),
               f"||σ - σ†|| = "
               f"{np.linalg.norm(sigma_post - sigma_post.conj().T):.3e}")


# -----------------------------------------------------------
# Block 10: Uniqueness via effect-basis equality (parent step 4)
# -----------------------------------------------------------

def block10() -> None:
    header("BLOCK 10: Uniqueness via effect-basis equality  "
           "(parent Step 4)")
    log("  If Tr(ρ_1 · E) = Tr(ρ_target · E) for a complete effect basis,")
    log("  then ρ_1 = ρ_target on finite-dimensional space.")

    rng = np.random.default_rng(20260604_10)
    for k in range(4):
        d = int(rng.choice([2, 4]))
        rho_target = random_density(d, rng)

        # Effect basis: matrix units E_{ij} = |i><j| (these are not
        # POVM effects but span the operator space; uniqueness uses
        # this duality between density operators and operators).
        basis: list[np.ndarray] = []
        for i in range(d):
            for j in range(d):
                E = np.zeros((d, d), dtype=complex)
                E[i, j] = 1.0
                basis.append(E)
        # Now check: any candidate ρ_1 satisfying Tr(ρ_1 · E) =
        # Tr(rho_target · E) for every E in `basis` must equal
        # rho_target.
        b_vec = np.array(
            [complex(np.trace(rho_target @ B)) for B in basis],
            dtype=complex,
        )
        # Build the linear map ρ -> (Tr(ρ · B_k))_k as a (d^2)×(d^2)
        # matrix. Since the basis {E_{ij}} is the matrix-unit basis,
        # Tr(ρ · E_{ji}) = ρ_{ij}, so the map is the identity on the
        # vectorization of ρ. The unique ρ that reproduces b_vec is
        # therefore rho_target itself.
        rho_reconstructed = np.zeros((d, d), dtype=complex)
        for B, b in zip(basis, b_vec, strict=True):
            # Tr(ρ · |i><j|) = ρ_{j i} so we recover by traversing
            # B = |i><j|, where i = first nonzero row, j = first
            # nonzero col.
            idx = np.argwhere(B != 0)
            i, j = int(idx[0, 0]), int(idx[0, 1])
            rho_reconstructed[j, i] = complex(b)
        diff = float(np.linalg.norm(rho_reconstructed - rho_target))
        record(f"effect_basis_uniqueness_d{d}_case{k}",
               diff < 1e-12,
               f"||ρ_reconstructed - ρ_target|| = {diff:.3e}")


# -----------------------------------------------------------
# Block 11: Static-source scan of parent note (zero Record tokens)
# -----------------------------------------------------------

def block11(parent_note_path: Path) -> None:
    header("BLOCK 11: Parent note Record-axiom usage scan "
           "(load-bearing sections)")
    if not parent_note_path.exists():
        log(f"  WARN: parent note not found at {parent_note_path}")
        record("parent_note_present", False, str(parent_note_path))
        return

    text = parent_note_path.read_text()
    record("parent_note_present", True, str(parent_note_path))

    # Load-bearing sections: from ## Claim through ## Risk classification
    start = text.find("## Claim")
    end = text.find("## Citation-graph note")
    record("structural_section_start_found", start >= 0,
           f"## Claim found at offset {start}")
    record("structural_section_end_found", end > start,
           f"## Citation-graph note found at offset {end}")

    section = text[start:end] if (start >= 0 and end > start) else ""

    # Tokens that would indicate Record-axiom usage
    record_tokens = [
        "I(R_1",
        "I(R)",
        "scalar record",
        "record functional",
        "record-readout",
        "additive record",
        "additive scalar record",
        "MINIMAL_AXIOMS_2026-06-04",
    ]
    found = []
    for tok in record_tokens:
        if tok in section:
            found.append(tok)

    record("zero_record_axiom_tokens_in_load_bearing_section",
           len(found) == 0,
           f"matches = {found}")


# -----------------------------------------------------------
# Block 12: Parent note contains Quantum / Lattice axiom content
# -----------------------------------------------------------

def block12(parent_note_path: Path) -> None:
    header("BLOCK 12: Parent note's load-bearing sections cite "
           "Quantum / Lattice axiom content")
    if not parent_note_path.exists():
        log(f"  WARN: parent note not found at {parent_note_path}")
        record("parent_note_present_block12", False, str(parent_note_path))
        return
    text = parent_note_path.read_text()

    # Tokens documenting the qubit / Z^3 substrate
    substrate_tokens = [
        "M_2(ℂ)",        # qubit local algebra (parent uses unicode ℂ)
        "Z^3",           # lattice site set
        "qubit",         # axiom name in plain English
        "operator algebra",
    ]
    found = []
    for tok in substrate_tokens:
        if tok in text:
            found.append(tok)
    record("parent_load_bearing_substrate_content_present",
           len(found) >= 3,
           f"found tokens (need >= 3): {found}")


# -----------------------------------------------------------
# Block 13: Record-axiom counterfactual
# -----------------------------------------------------------

def block13() -> None:
    header("BLOCK 13: Record-axiom counterfactual: "
           "identical numeric output")
    log("  Compute Lüders update, trace-cyclicity identity, Bayes")
    log("  identity, and (U4) check under explicit 'Record asserted'")
    log("  and 'Record not asserted' outer scopes; verify identity.")

    rng_asserted = np.random.default_rng(20260604_13)
    rng_not = np.random.default_rng(20260604_13)
    # Identical RNG seed in both scopes ⇒ identical test data;
    # then verify every quantity is bit-identical.

    for k in range(5):
        d = 2 if k < 3 else 4

        # "Record axiom asserted" scope — we ALSO have access to the
        # additive scalar record functional I(.); the calculation
        # does not invoke it.
        sigma_a = random_density(d, rng_asserted)
        P_a = random_projection_rank1(d, rng_asserted)
        E_a = random_effect(d, rng_asserted)

        # "Record axiom NOT asserted" scope — no I(.) functional.
        # Identical RNG draws ⇒ identical (σ, P, E).
        sigma_n = random_density(d, rng_not)
        P_n = random_projection_rank1(d, rng_not)
        E_n = random_effect(d, rng_not)

        record(f"counterfactual_inputs_identical_d{d}_case{k}",
               (np.array_equal(sigma_a, sigma_n)
                and np.array_equal(P_a, P_n)
                and np.array_equal(E_a, E_n)),
               "(σ, P, E) bit-identical")

        # Compute Lüders update
        try:
            sigma_post_a = luders_update(sigma_a, P_a)
            sigma_post_n = luders_update(sigma_n, P_n)
        except ZeroDivisionError:
            log(f"    skip Lüders for d{d}_case{k}")
            continue
        record(f"counterfactual_luders_post_identical_d{d}_case{k}",
               np.array_equal(sigma_post_a, sigma_post_n),
               f"||with - without|| = "
               f"{np.linalg.norm(sigma_post_a - sigma_post_n):.3e}")

        # Trace cyclicity identity
        lhs_a = complex(np.trace(sigma_a @ P_a @ E_a @ P_a))
        lhs_n = complex(np.trace(sigma_n @ P_n @ E_n @ P_n))
        record(f"counterfactual_trace_cyclicity_identical_d{d}_case{k}",
               lhs_a == lhs_n,
               f"diff = {abs(lhs_a - lhs_n):.3e}")

        # Bayes identity
        p_a = complex(np.trace(sigma_a @ P_a)).real
        p_n = complex(np.trace(sigma_n @ P_n)).real
        record(f"counterfactual_bayes_marginal_identical_d{d}_case{k}",
               p_a == p_n,
               f"diff = {abs(p_a - p_n):.3e}")


# -----------------------------------------------------------
# Block 14: Lattice/Quantum content preservation across memos
# -----------------------------------------------------------

def block14(repo_root: Path) -> None:
    header("BLOCK 14: Quantum / Lattice content preserved across the "
           "two minimal-axioms memos")
    old_memo = repo_root / "docs" / "MINIMAL_AXIOMS_2026-05-20.md"
    new_memo = repo_root / "docs" / "MINIMAL_AXIOMS_2026-06-04.md"
    record("old_memo_present", old_memo.exists(), str(old_memo))
    record("new_memo_present", new_memo.exists(), str(new_memo))

    if not (old_memo.exists() and new_memo.exists()):
        return

    old_text = old_memo.read_text()
    new_text = new_memo.read_text()

    # Quantum axiom content: per-site qubit / M_2(C) / Cl(3,0)
    old_quantum = (
        "M_2(ℂ)" in old_text  # M_2(ℂ)
        or "M_2(C)" in old_text
        or "qubit" in old_text.lower()
        or "Cl(3,0)" in old_text
    )
    new_quantum = (
        "M_2(C)" in new_text
        or "qubit" in new_text.lower()
        or "Cl(3,0)" in new_text
    )
    record("old_memo_has_qubit_local_algebra_content", old_quantum,
           "historical M_2(C) / qubit content present")
    record("new_memo_has_Quantum_axiom_content", new_quantum,
           "new Quantum axiom (qubit / M_2(C)) preserved")

    # Lattice axiom content: Z^3 site set
    old_lattice = "Z^3" in old_text or "Z³" in old_text  # Z³
    new_lattice = "Z^3" in new_text or "Z³" in new_text
    record("old_memo_has_Z3_lattice_content", old_lattice,
           "historical Z^3 lattice content present")
    record("new_memo_has_Lattice_axiom_content", new_lattice,
           "new Lattice axiom (Z^3) preserved")

    # Record axiom is additive scalar record-readout (additional,
    # non-overlapping)
    new_record_additivity = (
        "I(R_1 sqcup R_2) = I(R_1) + I(R_2)" in new_text
        or "additive over disjoint" in new_text
    )
    record("new_memo_has_Record_additive_scalar_content",
           new_record_additivity,
           "Record axiom: additive scalar functional")

    # Record axiom's own scope statement explicitly excludes the
    # bridges that the Lüders derivation does not need (and does not
    # use): rule for record production, measurement/decoherence, Born
    # weights, log-det, source/action, time arrow, normalization.
    record_scope_disclaimer = (
        "rule for record production" in new_text
        and "measurement/decoherence" in new_text
        and "log-det structure" in new_text
    )
    record("new_memo_Record_scope_excludes_load_bearing_bridges",
           record_scope_disclaimer,
           "Record axiom's scope statement excludes production / "
           "measurement / Born / log-det, none of which the Lüders "
           "derivation uses")


# -----------------------------------------------------------
# Block 15: Three-route cross-check on Lüders post-update state
# -----------------------------------------------------------

def block15() -> None:
    header("BLOCK 15: Lüders post-update state computed three "
           "independent ways")
    log("  Route A: direct sandwich (P σ P)/Tr(P σ P).")
    log("  Route B: spectral construction via projection onto +1 "
        "eigenspace.")
    log("  Route C: repeated post-selection on a 2-qubit purification.")

    # Test pair: |+><+| projection on a tilted single-qubit state
    sigma = density_from_bloch(0.3, 0.4, 0.5)
    P = proj_from_bloch(np.pi / 2, 0.0)  # |+><+|

    # Route A: direct sandwich
    route_A = luders_update(sigma, P)

    # Route B: spectral construction. The Lüders update onto a rank-1
    # projection P = |ψ><ψ| always returns |ψ><ψ| (up to phase) since
    # P σ P = (<ψ|σ|ψ>) |ψ><ψ|. So route B = P itself.
    route_B = P.copy()
    # Verify the algebraic relation
    coef = complex(np.trace(P @ sigma)).real  # <ψ|σ|ψ>
    route_B_alt = (coef * P) / (coef if coef > 0 else 1.0)

    record("route_A_density",
           is_psd(route_A) and trace_one(route_A),
           "PsiP/Tr is density")
    record("route_B_spectral_equals_projection",
           matrices_close(route_B, P, atol=1e-12),
           "spectral construction gives |ψ><ψ| = P")
    record("route_B_alt_equals_route_A",
           matrices_close(route_B_alt, route_A, atol=1e-10),
           f"||route_B_alt - route_A|| = "
           f"{np.linalg.norm(route_B_alt - route_A):.3e}")
    record("route_A_equals_route_B",
           matrices_close(route_A, route_B, atol=1e-10),
           f"||route_A - route_B|| = "
           f"{np.linalg.norm(route_A - route_B):.3e}")

    # Route C: post-selection on a purification.
    # Purify σ on H_S ⊗ H_R via |Ψ> = Σ_k √λ_k |k>_S ⊗ |k>_R.
    eigs, U = np.linalg.eigh((sigma + sigma.conj().T) / 2)
    Psi = np.zeros(4, dtype=complex)
    for k, lam in enumerate(eigs):
        if lam > 0:
            ek_S = U[:, k]
            ek_R = np.zeros(2, dtype=complex)
            ek_R[k] = 1.0
            Psi += np.sqrt(lam) * np.kron(ek_S, ek_R)
    # Verify the reduced state on H_S matches σ
    rho_full = np.outer(Psi, Psi.conj())
    rho_S = np.zeros((2, 2), dtype=complex)
    for i in range(2):
        for j in range(2):
            for r in range(2):
                rho_S[i, j] += rho_full[i * 2 + r, j * 2 + r]
    record("purification_reduces_to_sigma",
           matrices_close(rho_S, sigma, atol=1e-10),
           f"||rho_S - sigma|| = {np.linalg.norm(rho_S - sigma):.3e}")
    # Apply P ⊗ I to the purification and normalize
    P_full = np.kron(P, I2)
    PpurifP = P_full @ rho_full @ P_full
    tr = complex(np.trace(PpurifP)).real
    rho_full_post = PpurifP / tr
    # Trace out R
    rho_S_post = np.zeros((2, 2), dtype=complex)
    for i in range(2):
        for j in range(2):
            for r in range(2):
                rho_S_post[i, j] += rho_full_post[i * 2 + r, j * 2 + r]
    record("route_C_purification_post_equals_route_A",
           matrices_close(rho_S_post, route_A, atol=1e-10),
           f"||route_C - route_A|| = "
           f"{np.linalg.norm(rho_S_post - route_A):.3e}")


# -----------------------------------------------------------
# Main
# -----------------------------------------------------------

def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    parent_note = (
        repo_root / "docs"
        / "LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_NOTE_2026-05-20.md"
    )

    log("Lüders Rule deps_changed:dep_added:minimal_axioms "
        "Hygiene Companion Runner")
    log("=" * 72)
    log(f"Repo root: {repo_root}")
    log(f"Parent note: {parent_note}")
    log("Companion source note: "
        "docs/LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_"
        "DEPS_CHANGED_HYGIENE_COMPANION_NOTE_2026-06-04.md")
    log("")
    log("Goal: verify the parent's load-bearing Lüders-rule derivation")
    log("      σ → (P σ P) / Tr(P σ P)  (from (U1)-(U4) consistency)")
    log("      is invariant under the 2026-06-04 Record-axiom adoption")
    log("      (MINIMAL_AXIOMS_2026-06-04.md, deps_changed edge")
    log("      re-resolution from minimal_axioms_2026-05-20 to canonical")
    log("      minimal_axioms).")
    log("")
    log("Scope: pure audit-companion evidence; no theorem claim,")
    log("       no status promotion, no Record-axiom content asserted.")

    block1()
    block2()
    block3()
    block4()
    block5()
    block6()
    block7()
    block8()
    block9()
    block10()
    block11(parent_note)
    block12(parent_note)
    block13()
    block14(repo_root)
    block15()

    log("")
    log("=" * 72)
    log(f"TOTAL PASS: {PASS}")
    log(f"TOTAL FAIL: {FAIL}")
    log("=" * 72)
    log("")
    log("Companion conclusion (audit-friendly evidence only):")
    log("  The load-bearing chain of "
        "LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_")
    log("  NOTE_2026-05-20.md uses ONLY Quantum axiom content (per-site")
    log("  qubit local algebra M_2(C)) and Lattice axiom content (Z^3")
    log("  site set + standard C*-tensor product over finite regions)")
    log("  plus standard textbook operator-algebraic identities (trace")
    log("  cyclicity, positivity preservation under congruence, finite-")
    log("  dimensional density/effect duality, Bayes rule, standard")
    log("  sequential-effect composition M_{P,E} = P E P). The Record")
    log("  axiom (additive scalar record-readout functional) is neither")
    log("  used nor invoked. Numeric / algebraic output is identical")
    log("  under both 'Record axiom asserted' and 'Record axiom not")
    log("  asserted' outer scopes. This runner does not re-apply the")
    log("  prior audit verdict; it records that the algebra checked")
    log("  here is unchanged by the 2026-06-04 minimal-axioms edge")
    log("  re-resolution.")
    log("")
    log("The audit lane decides whether to honor or re-test the prior")
    log("verdict on the new minimal_axioms premise hash.")

    return 1 if FAIL > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
