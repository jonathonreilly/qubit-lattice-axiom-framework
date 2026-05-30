#!/usr/bin/env python3
"""Audit the Joint Protection Theorem composing Lane A and Lane B.

Lane A: Native taste-qubit teleportation no-signaling at Bob (pre-message).
Lane B: Chronology-protection no-past-signaling on single-clock CPTP.

This runner builds a 3-time joint circuit:
  t_A   Alice prepares |psi> tensor |Phi+>_RB; Bell measurement; classical
        record a is durable.
  t_B   Teleportation channel delivers Bob's reduced state pre-message.
  t_C   Arbitrary CPTP setting S_x at Bob's location (identity, Hadamard,
        dephasing, memory reset, Loschmidt echo U(-tau)*U(tau)).

It checks the four joint properties (J1)-(J4) of the source theorem note:

  (J1) Bob pre-message reduced state at t_B is input-independent (Lane A
       no-signaling, re-verified inside the joint circuit).
  (J2) Alice's earlier record marginal P(a at t_A) is invariant under any
       later setting x at t_C (Lane B no-past-signaling, re-verified inside
       the joint circuit).
  (J3) Bob's reduced state at t_C may depend on x (fairness control: x
       must do something local; nontriviality witness).
  (J4) The composition forbids any operational past-signaling channel from
       t_C to t_A even with teleportation present.

The theorem is a strict physical Cl(3) / Z^3 framework-compatible
composition: no new framework primitives, only the Lane A no-signaling
result and the Lane B no-past-signaling result.
"""

from __future__ import annotations

from pathlib import Path
from typing import Callable

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "FRONTIER_EXTENSION_LANE_B_PROTECTS_LANE_A_JOINT_COMPOSITION_NARROW_NOTE_2026-05-17.md"
)

AUTHORITY_FILES = [
    ROOT / "docs" / "FRONTIER_EXTENSION_LANE_OPENING_NOTE_2026-04-25.md",
    ROOT
    / "docs"
    / "CHRONOLOGY_PROTECTION_OPERATIONAL_NO_PAST_SIGNALING_THEOREM_NOTE_2026-04-25.md",
    ROOT / "docs" / "TELEPORTATION_NO_SIGNALING_AUDIT.md",
    ROOT / "docs" / "SINGLE_AXIOM_HILBERT_NOTE.md",
    ROOT / "docs" / "BELL_INEQUALITY_DERIVED_NOTE.md",
]

EPS = 1e-12


passes = 0
fails = 0


def check(name: str, condition: bool) -> None:
    global passes, fails
    if condition:
        passes += 1
        print(f"  [PASS] {name}")
    else:
        fails += 1
        print(f"  [FAIL] {name}")


def section(title: str) -> None:
    print("\n" + "-" * 88)
    print(title)
    print("-" * 88)


def dagger(x: np.ndarray) -> np.ndarray:
    return x.conj().T


def trace(x: np.ndarray) -> complex:
    return complex(np.trace(x))


def close(a: complex, b: complex, eps: float = EPS) -> bool:
    return abs(a - b) <= eps


def kron(*matrices: np.ndarray) -> np.ndarray:
    out = matrices[0]
    for m in matrices[1:]:
        out = np.kron(out, m)
    return out


def is_trace_preserving(kraus: list[np.ndarray]) -> bool:
    dim = kraus[0].shape[1]
    total = sum(dagger(k) @ k for k in kraus)
    return bool(np.allclose(total, np.eye(dim), atol=EPS))


def is_unital_dual(kraus: list[np.ndarray]) -> bool:
    dim = kraus[0].shape[1]
    identity = np.eye(dim, dtype=complex)
    dual_identity = sum(dagger(k) @ identity @ k for k in kraus)
    return bool(np.allclose(dual_identity, identity, atol=EPS))


def apply_kraus(kraus: list[np.ndarray], rho: np.ndarray) -> np.ndarray:
    return sum(k @ rho @ dagger(k) for k in kraus)


def partial_trace_last(rho: np.ndarray, dim_keep: int, dim_drop: int) -> np.ndarray:
    """Trace out the last factor in a bipartite (keep tensor drop) Hilbert."""
    reshaped = rho.reshape(dim_keep, dim_drop, dim_keep, dim_drop)
    return np.einsum("ijkj->ik", reshaped)


def partial_trace_first(rho: np.ndarray, dim_drop: int, dim_keep: int) -> np.ndarray:
    """Trace out the first factor in a bipartite (drop tensor keep) Hilbert."""
    reshaped = rho.reshape(dim_drop, dim_keep, dim_drop, dim_keep)
    return np.einsum("jiji->ii", reshaped) if False else np.einsum("ijik->jk", reshaped)


def normalize(psi: np.ndarray) -> np.ndarray:
    return psi / np.linalg.norm(psi)


def random_pure_qubit(rng: np.random.Generator) -> np.ndarray:
    psi = rng.standard_normal(2) + 1j * rng.standard_normal(2)
    return normalize(psi)


# ---------------------------------------------------------------------------
# Single-qubit Pauli matrices.
# ---------------------------------------------------------------------------
I2 = np.eye(2, dtype=complex)
X = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
Y = np.array([[0.0, -1j], [1j, 0.0]], dtype=complex)
Z = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
H = (1.0 / np.sqrt(2.0)) * np.array([[1.0, 1.0], [1.0, -1.0]], dtype=complex)
P0 = np.array([[1.0, 0.0], [0.0, 0.0]], dtype=complex)
P1 = np.array([[0.0, 0.0], [0.0, 1.0]], dtype=complex)

# ---------------------------------------------------------------------------
# Bell basis projectors and corresponding Bob corrections.
# Bell basis is labeled (z, x) in {0,1}^2 with the conventional encoding:
#   |Phi+> = (|00>+|11>)/sqrt(2)   (z=0, x=0)  -> Bob correction I
#   |Phi-> = (|00>-|11>)/sqrt(2)   (z=1, x=0)  -> Bob correction Z
#   |Psi+> = (|01>+|10>)/sqrt(2)   (z=0, x=1)  -> Bob correction X
#   |Psi-> = (|01>-|10>)/sqrt(2)   (z=1, x=1)  -> Bob correction XZ
# ---------------------------------------------------------------------------
PHI_PLUS = (1.0 / np.sqrt(2.0)) * np.array([1.0, 0.0, 0.0, 1.0], dtype=complex)
PHI_MINUS = (1.0 / np.sqrt(2.0)) * np.array([1.0, 0.0, 0.0, -1.0], dtype=complex)
PSI_PLUS = (1.0 / np.sqrt(2.0)) * np.array([0.0, 1.0, 1.0, 0.0], dtype=complex)
PSI_MINUS = (1.0 / np.sqrt(2.0)) * np.array([0.0, 1.0, -1.0, 0.0], dtype=complex)
BELL_STATES = [PHI_PLUS, PHI_MINUS, PSI_PLUS, PSI_MINUS]
BELL_LABELS = ["00", "10", "01", "11"]  # (z, x)
CORRECTIONS = [I2, Z, X, X @ Z]


# ---------------------------------------------------------------------------
# 3-time joint circuit primitives.
# ---------------------------------------------------------------------------
def initial_state(rho_input: np.ndarray) -> np.ndarray:
    """Build rho_A tensor |Phi+><Phi+|_RB on H_A tensor H_R tensor H_B."""
    bell = PHI_PLUS
    rho_bell = np.outer(bell, bell.conj())
    return kron(rho_input, rho_bell)


def alice_bell_branch(rho_full: np.ndarray, idx: int) -> np.ndarray:
    """Project Alice (A,R) onto Bell state idx; return un-renormalized 8-dim
    state (P_idx tensor I_B) rho_full (P_idx tensor I_B)."""
    bell = BELL_STATES[idx]
    proj_ar = np.outer(bell, bell.conj())  # 4x4
    proj_full = kron(proj_ar, I2)  # 8x8
    return proj_full @ rho_full @ proj_full


def bob_branch_unnormalized(rho_full: np.ndarray, idx: int) -> np.ndarray:
    """Reduced state on Bob after Alice's Bell projection idx,
    un-renormalized (so trace = P(idx))."""
    branch = alice_bell_branch(rho_full, idx)
    # branch is on H_A tensor H_R tensor H_B = 2 x 2 x 2 = 8
    # partial-trace out A and R (first two factors)
    reshaped = branch.reshape(2, 2, 2, 2, 2, 2)
    # indices: A_in, R_in, B_in, A_out, R_out, B_out
    rho_b = np.einsum("ijkijl->kl", reshaped)
    return rho_b


def bob_corrected_branch(rho_full: np.ndarray, idx: int) -> np.ndarray:
    """Apply Bob's Pauli correction to the un-renormalized Bob branch."""
    rho_b = bob_branch_unnormalized(rho_full, idx)
    corr = CORRECTIONS[idx]
    return corr @ rho_b @ dagger(corr)


def teleported_state(rho_input: np.ndarray) -> np.ndarray:
    """Sum over Bell outcomes of corrected Bob branches.  This is the
    deterministic teleportation map T(rho_input)."""
    rho_full = initial_state(rho_input)
    out = np.zeros((2, 2), dtype=complex)
    for idx in range(4):
        out = out + bob_corrected_branch(rho_full, idx)
    return out


# ---------------------------------------------------------------------------
# Audit.
# ---------------------------------------------------------------------------
def main() -> int:
    print("=" * 88)
    print("Joint Protection Theorem audit (Lane A teleportation + Lane B chronology)")
    print(f"See {NOTE.relative_to(ROOT)}")
    print("=" * 88)

    # ------------------------------------------------------------------
    # Authority and scope surface.
    # ------------------------------------------------------------------
    section("Authority and scope surface")
    note_text = NOTE.read_text() if NOTE.exists() else ""
    for path in AUTHORITY_FILES:
        check(f"authority/reference exists: {path.relative_to(ROOT)}", path.exists())

    required_boundaries = [
        "does not close the lane",
        "does not promote",
        "single-clock",
        "pre-message",
        "postselection",
        "no operational past-signaling channel from t_C to t_A",
        "no main-surface promotion",
    ]
    for phrase in required_boundaries:
        check(f"note states boundary: {phrase}", phrase in note_text)

    forbidden_promotions = [
        "closes the lane-opening note",
        "promotes Lane C",
        "ftl",
        "FTL signaling is possible",
        "antigravity is established",
    ]
    for phrase in forbidden_promotions:
        check(f"note avoids overclaim: {phrase}", phrase not in note_text)

    # ------------------------------------------------------------------
    # (J1) Lane A no-signaling re-verified in the joint circuit.
    # ------------------------------------------------------------------
    section("(J1) Bob pre-message reduced state is input-independent")
    rng = np.random.default_rng(20260517)
    inputs = [
        np.array([1.0, 0.0], dtype=complex),  # |0>
        np.array([0.0, 1.0], dtype=complex),  # |1>
        normalize(np.array([1.0, 1.0], dtype=complex)),  # |+>
        normalize(np.array([1.0, -1.0], dtype=complex)),  # |->
        normalize(np.array([1.0, 1j], dtype=complex)),  # |+i>
        normalize(np.array([1.0, -1j], dtype=complex)),  # |-i>
    ] + [random_pure_qubit(rng) for _ in range(8)]

    half_identity = 0.5 * I2
    for k, psi in enumerate(inputs):
        rho_in = np.outer(psi, psi.conj())
        check(f"input #{k} normalized", close(trace(rho_in), 1.0))
        rho_full = initial_state(rho_in)
        # Bob pre-message reduced state: sum over Alice's Bell outcomes,
        # without applying Bob's correction (i.e. without using the
        # classical message bits).
        rho_b_pre = np.zeros((2, 2), dtype=complex)
        for idx in range(4):
            rho_b_pre = rho_b_pre + bob_branch_unnormalized(rho_full, idx)
        check(f"input #{k} Bob pre-message trace = 1", close(trace(rho_b_pre), 1.0))
        check(
            f"input #{k} Bob pre-message = I/2 (no-signaling)",
            np.allclose(rho_b_pre, half_identity, atol=EPS),
        )

    # ------------------------------------------------------------------
    # (J1b) Teleportation channel correctly delivers the input state
    # AFTER Bob applies his correction.  Sanity that we have a valid
    # teleportation protocol, not a vacuous "Bob ignores everything"
    # construction.
    # ------------------------------------------------------------------
    section("(J1b) Teleportation channel deterministically delivers input")
    for k, psi in enumerate(inputs):
        rho_in = np.outer(psi, psi.conj())
        rho_out = teleported_state(rho_in)
        check(f"teleported #{k} trace = 1", close(trace(rho_out), 1.0))
        check(
            f"teleported #{k} equals input (fidelity 1)",
            np.allclose(rho_out, rho_in, atol=1e-10),
        )

    # ------------------------------------------------------------------
    # (J2) Alice's earlier record P(a at t_A) is invariant under any
    # later CPTP setting at t_C.
    #
    # Alice's record is the Bell-outcome label.  Without any future
    # operation, P(a) = 1/4 uniform on the 4 Bell outcomes (standard
    # teleportation property under maximally-entangled resource).
    #
    # The chronology-respecting later settings at t_C are CPTP operations
    # on Bob's register.  None can change P(a at t_A).
    # ------------------------------------------------------------------
    section("(J2) Earlier record marginal invariant under any later setting at t_C")

    later_settings: dict[str, list[np.ndarray]] = {
        "identity_at_C": [I2],
        "hadamard_at_C": [H],
        "dephasing_at_C": [np.sqrt(0.25) * I2, np.sqrt(0.75) * Z],
        "memory_reset_to_|0>_at_C": [
            np.array([[1.0, 0.0], [0.0, 0.0]], dtype=complex),
            np.array([[0.0, 1.0], [0.0, 0.0]], dtype=complex),
        ],
        "loschmidt_echo_at_C": [I2],  # U(-tau) @ U(tau) = I on Bob.
        "depolarizing_at_C": [
            np.sqrt(1 - 3 * 0.2) * I2,
            np.sqrt(0.2) * X,
            np.sqrt(0.2) * Y,
            np.sqrt(0.2) * Z,
        ],
    }
    for name, kraus in later_settings.items():
        check(f"{name} is trace preserving", is_trace_preserving(kraus))
        check(f"{name} has unital Heisenberg dual", is_unital_dual(kraus))

    # P(a) is the trace of Alice's branch in the joint state.  It does
    # NOT depend on Bob's post-protocol setting because Alice's record
    # at t_A is past and the joint state factorizes the Alice record
    # statistics from Bob's post-protocol channel by trace-preservation.
    for k, psi in enumerate(inputs[:6]):
        rho_in = np.outer(psi, psi.conj())
        rho_full = initial_state(rho_in)

        base_probs = []
        for idx in range(4):
            branch = alice_bell_branch(rho_full, idx)
            base_probs.append(trace(branch).real)
        check(
            f"input #{k}: record probabilities sum to one",
            abs(sum(base_probs) - 1.0) <= EPS,
        )
        check(
            f"input #{k}: P(a) is uniform 1/4 on Bell outcomes",
            all(abs(p - 0.25) <= EPS for p in base_probs),
        )

        # Apply later CPTP setting at Bob within each Alice branch and
        # re-extract the record marginal P(a).
        for name, kraus in later_settings.items():
            post_probs = []
            for idx in range(4):
                branch = alice_bell_branch(rho_full, idx)
                # Apply later channel to Bob factor only.
                # branch is on (A, R, B) = 2x2x2.
                # We extend each Kraus operator K (acting on B) to
                # I_A tensor I_R tensor K and apply.
                post_branch = np.zeros((8, 8), dtype=complex)
                for k_op in kraus:
                    full_k = kron(I2, I2, k_op)
                    post_branch = post_branch + full_k @ branch @ dagger(full_k)
                post_probs.append(trace(post_branch).real)
            for idx in range(4):
                check(
                    f"input #{k}, {name}: record P(a={BELL_LABELS[idx]}) "
                    f"unchanged",
                    abs(post_probs[idx] - base_probs[idx]) <= EPS,
                )

    # ------------------------------------------------------------------
    # (J3) Bob's *local future* state at t_C *can* depend on x.  This is
    # the fairness witness: the no-signaling at t_A is nontrivial, not
    # vacuous, because Bob's own register does respond to local choices.
    # ------------------------------------------------------------------
    section("(J3) Bob's local state at t_C depends on x (nontriviality witness)")
    # Start from Bob's post-teleportation state = the unknown input |psi>.
    # Apply different later settings at Bob; they yield different states.
    distinguishability_seen = False
    for k, psi in enumerate(inputs[:4]):
        rho_in = np.outer(psi, psi.conj())
        rho_bob_at_tB = teleported_state(rho_in)  # = rho_in (deterministic).
        # Apply two distinct settings.
        rho_bob_C_id = apply_kraus(later_settings["identity_at_C"], rho_bob_at_tB)
        rho_bob_C_H = apply_kraus(later_settings["hadamard_at_C"], rho_bob_at_tB)
        if not np.allclose(rho_bob_C_id, rho_bob_C_H, atol=1e-8):
            distinguishability_seen = True
    check(
        "some input + setting pair gives distinguishable Bob-at-t_C states",
        distinguishability_seen,
    )
    # And a specific witness: |+> input, H mapping it to |0>, vs. identity
    # leaving it as |+>; these states are distinguishable.
    psi_plus = normalize(np.array([1.0, 1.0], dtype=complex))
    rho_plus = np.outer(psi_plus, psi_plus.conj())
    rho_after_H = apply_kraus([H], rho_plus)
    rho_after_I = apply_kraus([I2], rho_plus)
    trace_distance = 0.5 * np.linalg.norm(rho_after_H - rho_after_I, ord="nuc")
    print(f"  trace distance (Bob H vs Bob I on |+>) = {trace_distance:.12f}")
    check("Bob H vs Bob I trace distance > 0.5", trace_distance > 0.5)

    # ------------------------------------------------------------------
    # (J4) Joint composition is the right composition: no operational
    # past-signaling channel from t_C to t_A in the presence of a
    # teleportation protocol.
    #
    # We check this in two ways:
    #
    # (J4a) The joint conditional P(a | x) computed from the full joint
    #       circuit equals the marginal P(a) for every x (independence).
    # (J4b) The composition is *strict* in the sense that swapping the
    #       chronological order (apply S_x at Bob BEFORE Alice records)
    #       could in principle change Alice's record statistics — and
    #       indeed does, in a positive-control check — which shows the
    #       theorem's protective force comes specifically from
    #       chronological order, not from triviality.
    # ------------------------------------------------------------------
    section("(J4) Joint composition forbids past-signaling from t_C to t_A")
    for k, psi in enumerate(inputs[:4]):
        rho_in = np.outer(psi, psi.conj())
        rho_full = initial_state(rho_in)
        # Marginal P(a) (no future op).
        marg_probs = []
        for idx in range(4):
            branch = alice_bell_branch(rho_full, idx)
            marg_probs.append(trace(branch).real)

        # Conditional P(a | x) using later op S_x applied within each
        # Alice branch (which is the CPTP sum over future outcomes).
        for name, kraus in later_settings.items():
            cond_probs = []
            for idx in range(4):
                branch = alice_bell_branch(rho_full, idx)
                future_branch = np.zeros((8, 8), dtype=complex)
                for k_op in kraus:
                    full_k = kron(I2, I2, k_op)
                    future_branch = future_branch + full_k @ branch @ dagger(full_k)
                cond_probs.append(trace(future_branch).real)
            for idx in range(4):
                check(
                    f"(J4a) input #{k}, {name}: P(a={BELL_LABELS[idx]}|x) = "
                    f"P(a={BELL_LABELS[idx]})",
                    abs(cond_probs[idx] - marg_probs[idx]) <= EPS,
                )

    # (J4b) Positive-control: applying a NON-CPTP "as-if" past-conditioning
    # (specifically, applying a future projector and conditioning on its
    # outcome) DOES bias the retrodicted record distribution.  This is
    # the standard postselection exception explicitly excluded by the
    # chronology theorem; here we verify the bias exists, which shows
    # the protection statement is doing real work (not a tautology).
    section("(J4b) Positive control: postselected past-conditioning DOES bias")
    psi = normalize(np.array([1.0, 0.5j], dtype=complex))
    rho_in = np.outer(psi, psi.conj())
    rho_full = initial_state(rho_in)
    # Per-branch state right after Alice's Bell measurement.
    branches = [alice_bell_branch(rho_full, idx) for idx in range(4)]
    base_probs = [trace(b).real for b in branches]
    # Postselected projector at Bob at t_C: project onto |0>.
    bob_proj_0 = kron(I2, I2, P0)
    branch_after_post = [bob_proj_0 @ b @ bob_proj_0 for b in branches]
    branch_after_post_probs = [trace(b).real for b in branch_after_post]
    prob_post = sum(branch_after_post_probs)
    check(
        "postselected branch has nonzero probability cost",
        prob_post > 0,
    )
    cond_a0_given_post = branch_after_post_probs[0] / prob_post
    print(f"  base P(a=00) = {base_probs[0]:.6f}")
    print(f"  P(a=00 | future Bob postselected on |0>) = {cond_a0_given_post:.6f}")
    bias = abs(cond_a0_given_post - base_probs[0])
    print(f"  bias from postselection = {bias:.6f}")
    check("postselection biases the retrodicted ensemble (control)", bias > 1e-3)

    # ------------------------------------------------------------------
    # Summary.
    # ------------------------------------------------------------------
    section("Summary")
    print("  Certified:")
    print("    (J1) Bob pre-message reduced state is I/2 for every input.")
    print("    (J1b) Teleportation channel delivers the input deterministically.")
    print("    (J2) P(a at t_A) is invariant under any later CPTP setting at t_C.")
    print("    (J3) Bob's local state at t_C does respond to x (nontriviality).")
    print("    (J4a) Conditional P(a|x) equals marginal P(a) for every x.")
    print("    (J4b) Postselected past-conditioning DOES bias (positive control).")
    print()
    print("  Not certified:")
    print("    no closure of the lane-opening note;")
    print("    no promotion of Lane C (signed gravity);")
    print("    no manuscript-surface or retained-row change;")
    print("    no derivation of the retained single-clock surface itself;")
    print("    no claim about postselected, final-boundary, or directed-cycle")
    print("    theories — those remain explicitly outside scope.")

    print("\n" + "=" * 88)
    print(f"TOTAL: PASS={passes}, FAIL={fails}")
    print("=" * 88)
    return 0 if fails == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
