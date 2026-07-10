#!/usr/bin/env python3
"""Frontier: pointer conservation and controlled-copy record formation on a
qubit lattice patch.

Temporal sequel to the timeless gauge-STRUCTURE corollary
(`TWO_ENDPOINT_GAUSS_LAW_INVARIANCE_PROFILE_BOUNDED_THEOREM_NOTE_2026-06-05`,
the two-endpoint Gauss-law companion): that result constrains the gauge-invariant *algebra* at a
fixed time. Here we ask what the Record axiom -- additivity of the record
readout over disjoint record collections -- plus its dynamical realization
(quantum Darwinism: an objective record is redundantly imprinted on many
disjoint environment fragments) plus persistence (decoherence-stability)
imposes on the transfer step U / T that FORMS the record.

Framework anchors (named axioms, MINIMAL_AXIOMS_2026-06-29.md):
  - Qubit: per-site possibility domain with algebraic presentation M_2(C).
  - Lattice and Admissibility: Z^3 nearest-neighbor structure and one fixed
    local admissibility rule. The selected S + E_1..E_n carrier and its
    couplings are bounded model inputs, not the full six-neighbor star.
  - Record: scalar record readout is additive over disjoint collections,
    I(R_1 sqcup R_2) = I(R_1) + I(R_2), timeless. The axiom explicitly does
    NOT identify I with Holevo information or supply record production,
    persistence, or decoherence. This model separately supplies the singleton
    bridge I({k}) := J({k}).

The runner is fully self-contained (numpy only), uses <= 6 qubits, exact dense
operators, and emits a PASS/FAIL self-check. It proves the Heisenberg
pointer-conservation iff at the flow level, the step-level iff [U,Pi_S]=0
(with a noncommuting-Hermitian-logarithm CNOT witness: generator-level
commutation is NOT forced by one step), separately from the sufficient
controlled-copy recording construction; it does NOT claim that arbitrary commuting Hamiltonians
write redundant fragments, derive an action, fix a coupling, or beta=6. See the
verdict block at the end and the companion note for the firewall.

Memory care: largest object is a 64x64 density matrix (n=5 environment qubits
=> 6 qubits => 2^6 = 64). Trivial RSS.
"""

from __future__ import annotations

from itertools import combinations
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[1]

PASS = 0
FAIL = 0


def record(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" :: {detail}" if detail else ""
    print(f"{tag} {label}{suffix}")


def section(title: str) -> None:
    print()
    print("-" * 78)
    print(title)
    print("-" * 78)


# ---------------------------------------------------------------------------
# Single-qubit operators and tensor helpers
# ---------------------------------------------------------------------------
I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
PROJ0 = np.array([[1, 0], [0, 0]], dtype=complex)  # |0><0|
PROJ1 = np.array([[0, 0], [0, 1]], dtype=complex)  # |1><1|

KET0 = np.array([1, 0], dtype=complex)


def bloch_ket(theta: float, phi: float) -> np.ndarray:
    """A generic pure qubit on the Bloch sphere (off all principal axes when
    theta, phi are generic). Used as the system's initial state so that the
    z-pointer record is non-trivial AND a demolition (z-rotating) coupling
    genuinely scrambles it."""
    return np.array([np.cos(theta / 2),
                     np.exp(1j * phi) * np.sin(theta / 2)], dtype=complex)


def op(single: np.ndarray, pos: int, n: int) -> np.ndarray:
    """Embed a single-qubit operator at site `pos` of an n-qubit register."""
    mats = [I2] * n
    mats[pos] = single
    out = mats[0]
    for m in mats[1:]:
        out = np.kron(out, m)
    return out


def comm(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a @ b - b @ a


def kron_list(vs: list[np.ndarray]) -> np.ndarray:
    out = vs[0]
    for v in vs[1:]:
        out = np.kron(out, v)
    return out


# ---------------------------------------------------------------------------
# Quantum-information primitives (standard; reproven here, not imported)
# ---------------------------------------------------------------------------
def von_neumann(rho: np.ndarray) -> float:
    """von Neumann entropy in BITS (log base 2)."""
    w = np.linalg.eigvalsh(rho)
    w = w[w > 1e-12]
    return float(-np.sum(w * np.log2(w)))


def shannon_bits(probs: np.ndarray) -> float:
    p = np.asarray(probs, dtype=float)
    p = p[p > 1e-12]
    return float(-np.sum(p * np.log2(p)))


def partial_trace(rho: np.ndarray, keep: list[int], n: int) -> np.ndarray:
    """Partial trace of an n-qubit density matrix, keeping qubits `keep`."""
    keep = sorted(keep)
    traced = [q for q in range(n) if q not in keep]
    t = rho.reshape([2] * (2 * n))
    # Trace out `traced` qubits one at a time (axes shift as we go).
    offset = 0
    for q in traced:
        ax = q - offset
        t = np.trace(t, axis1=ax, axis2=ax + (n - offset))
        offset += 1
    k = len(keep)
    return t.reshape(2 ** k, 2 ** k)


def mutual_information(rho: np.ndarray, A: list[int], B: list[int], n: int) -> float:
    """Quantum mutual information I(A:B) = S(A)+S(B)-S(AB), in bits."""
    rA = partial_trace(rho, A, n)
    rB = partial_trace(rho, B, n)
    rAB = partial_trace(rho, sorted(A + B), n)
    return von_neumann(rA) + von_neumann(rB) - von_neumann(rAB)


def pointer_entropy(rho: np.ndarray, sys: int, n: int) -> float:
    """H(Pi_S) = Shannon entropy (bits) of the system POPULATIONS in the
    pointer (z) basis. This is the record-content the pointer carries: it is
    1 bit for a state with equal z-populations, regardless of coherences.
    (The von Neumann entropy of the reduced *state* is the wrong functional --
    it is 0 for any pure system state.)"""
    rS = partial_trace(rho, [sys], n)
    pops = np.real(np.diag(rS))
    return shannon_bits(pops)


def holevo_pointer_info(rho: np.ndarray, sys: int, frag: list[int], n: int) -> float:
    """Operationally: the information a fragment carries about the system
    POINTER observable Pi_S = sigma_z(S).

    We dephase the system in the pointer basis (the only information a
    *classical objective record* can certify) and return the resulting
    system<->fragment mutual information. This is the accessible
    classical-record content for the pointer observable: it equals the
    Holevo chi of the ensemble {p_k, rho_F|k} of fragment states conditioned
    on pointer outcome k.
    """
    # Dephase system in the pointer (z) basis.
    P0 = op(PROJ0, sys, n)
    P1 = op(PROJ1, sys, n)
    rho_deph = P0 @ rho @ P0 + P1 @ rho @ P1
    return mutual_information(rho_deph, [sys], frag, n)


# ---------------------------------------------------------------------------
# Model: system qubit S (site 0) + n environment qubits E_1..E_n (sites 1..n)
# ---------------------------------------------------------------------------
# A FULLY GENERIC, off-axis system Bloch state: nonzero x, y AND z components.
#   - nonzero z  => the z-pointer carries a nontrivial record H(Pi_S) in (0,1)
#                   AND a demolition (x-rotating) coupling genuinely moves z.
#   - nonzero x,y => the state carries coherence that decoherence must remove.
# This single state exercises BOTH the recording (non-demolition) demo and the
# scrambling (demolition) demo without any axis degeneracy.
SYS_THETA = 0.7   # polar angle (off z-axis): cos(0.7)=0.765 => bz != 0
SYS_PHI = 0.9     # azimuth (off x and y axes)


def make_state(n_env: int) -> np.ndarray:
    """Initial state: system in a generic off-axis Bloch state (nonzero x,y,z
    components, so the z-pointer entropy H(Pi_S) is a nontrivial record and a
    demolition coupling genuinely scrambles it), environment all in |0>."""
    vecs = [bloch_ket(SYS_THETA, SYS_PHI)] + [KET0] * n_env
    return kron_list(vecs)


def record_unitary_single(n_env: int, k: int, g: float, t: float) -> np.ndarray:
    """U for a non-demolition recording of S onto ONE fragment E_k only:
        U = exp(-i g t sigma_z(S) sigma_x(E_k)).
    Used to build a von Neumann measurement CHAIN (fresh fragment per step) and
    to FREEZE a fragment once its recording is complete."""
    n = n_env + 1
    H = g * (op(SZ, 0, n) @ op(SX, k, n))
    return unitary(H, t)


def evolve(psi: np.ndarray, U: np.ndarray) -> np.ndarray:
    return U @ psi


def density(psi: np.ndarray) -> np.ndarray:
    return np.outer(psi, psi.conj())


# --- Hamiltonians ----------------------------------------------------------
def H_nondemolition(n_env: int, g: float) -> np.ndarray:
    """Pointer-NON-demolition CONTROLLED coupling:
        H = g * sigma_z(S) (x) sum_k sigma_x(E_k).
    Commutes with Pi_S = sigma_z(S): [H, sigma_z(S)] = 0.
    Each environment qubit rotates conditioned on the system pointer value;
    this is the canonical Darwinism / controlled-NOT-like recording channel.
    """
    n = n_env + 1
    H = np.zeros((2 ** n, 2 ** n), dtype=complex)
    sz_s = op(SZ, 0, n)
    for k in range(1, n):
        H = H + g * (sz_s @ op(SX, k, n))
    return H


def H_demolition(n_env: int, g: float) -> np.ndarray:
    """Pointer-DEMOLITION coupling: replace the system handle sigma_z(S) by
    sigma_x(S), which does NOT commute with the pointer Pi_S = sigma_z(S):
        H = g * sigma_x(S) (x) sum_k sigma_x(E_k).
    The system handle and the pointer fail to commute, so the would-be record
    is in a basis that the dynamics itself rotates.
    """
    n = n_env + 1
    H = np.zeros((2 ** n, 2 ** n), dtype=complex)
    sx_s = op(SX, 0, n)
    for k in range(1, n):
        H = H + g * (sx_s @ op(SX, k, n))
    return H


def H_partial_demolition(n_env: int, g: float, theta: float) -> np.ndarray:
    """One-parameter family interpolating handle = cos(theta) sigma_z(S) +
    sin(theta) sigma_x(S). theta=0 is pure non-demolition, theta=pi/2 is pure
    demolition. The non-demolition COMMUTATOR norm ||[H, Pi_S]|| ~ |sin theta|.
    """
    n = n_env + 1
    handle = np.cos(theta) * op(SZ, 0, n) + np.sin(theta) * op(SX, 0, n)
    H = np.zeros((2 ** n, 2 ** n), dtype=complex)
    for k in range(1, n):
        H = H + g * (handle @ op(SX, k, n))
    return H


def unitary(H: np.ndarray, t: float) -> np.ndarray:
    """U = exp(-i H t) via eigendecomposition (H Hermitian)."""
    w, V = np.linalg.eigh(H)
    return (V * np.exp(-1j * w * t)) @ V.conj().T


# ---------------------------------------------------------------------------
# Redundancy R_delta (quantum Darwinism): number of disjoint single-qubit
# fragments F whose pointer information reaches (1 - delta) * H_S.
# ---------------------------------------------------------------------------
def redundancy_singletons(rho: np.ndarray, n_env: int, delta: float, H_S: float) -> int:
    """Count environment singletons E_k that each carry >= (1-delta) H_S of
    the system pointer information. (Singleton fragments => the count is the
    cleanest disjoint-fragment redundancy R_delta on this small patch.)"""
    n = n_env + 1
    thresh = (1.0 - delta) * H_S
    cnt = 0
    for k in range(1, n):
        info = holevo_pointer_info(rho, 0, [k], n)
        if info >= thresh - 1e-9:
            cnt += 1
    return cnt


# ===========================================================================
def main() -> int:
    print("=" * 78)
    print("Record-formation dynamics constraint -- explicit S + E_1..E_n test")
    print("temporal sequel to the two-endpoint Gauss-law gauge-structure companion")
    print("=" * 78)

    n_env = 4              # 5 qubits total
    g = 1.0
    # H_S = pointer entropy of the chosen generic system state (computed below
    # in Part 0 from the actual z-populations; this is the amount of record a
    # perfect objective copy carries).
    H_S_initial = pointer_entropy(density(make_state(n_env)), 0, n_env + 1)

    # -----------------------------------------------------------------------
    section("Part 0: framework anchors and pointer observable")
    # -----------------------------------------------------------------------
    n = n_env + 1
    Pi_S = op(SZ, 0, n)
    record("Qubit: per-site carrier is a qubit (2-dim), Pi_S = sigma_z(S)",
           Pi_S.shape == (2 ** n, 2 ** n))
    psi0 = make_state(n_env)
    rho0 = density(psi0)
    init_pointer_entropy = pointer_entropy(rho0, 0, n)
    record("system starts in a generic off-axis state: H(Pi_S) nontrivial in (0,1)",
           0.01 < init_pointer_entropy < 0.999,
           f"H(Pi_S)={init_pointer_entropy:.4f} bits (the record a perfect copy carries)")
    # No record exists before evolution: fragments know nothing about S.
    pre = max(holevo_pointer_info(rho0, 0, [k], n) for k in range(1, n))
    record("before any U step no fragment carries pointer info (no record yet)",
           pre < 1e-9, f"max I_pre={pre:.2e}")

    # -----------------------------------------------------------------------
    section("Part 1: NON-DEMOLITION coupling -- [H_int, Pi_S] = 0")
    # -----------------------------------------------------------------------
    H_nd = H_nondemolition(n_env, g)
    cnd = comm(H_nd, Pi_S)
    nd_comm_norm = float(np.linalg.norm(cnd))
    record("non-demolition: [H_int, Pi_S] = 0 exactly",
           nd_comm_norm < 1e-12, f"||[H,Pi_S]||={nd_comm_norm:.2e}")

    # Evolve to a time where each E_k has fully recorded the pointer bit.
    # For H = g sigma_z(S) sigma_x(E_k): the controlled rotation angle is
    # 2 g t per qubit; t = pi/(4g) gives a maximally distinguishing record
    # (system pointer up/down -> environment rotated to orthogonal +-x/-x).
    t_rec = np.pi / (4.0 * g)
    U_nd = unitary(H_nd, t_rec)
    psi_nd = evolve(psi0, U_nd)
    rho_nd = density(psi_nd)

    info_each = [holevo_pointer_info(rho_nd, 0, [k], n) for k in range(1, n)]
    record("non-demolition: every single E_k carries the full pointer record H_S",
           all(abs(x - H_S_initial) < 1e-6 for x in info_each),
           f"per-fragment I = {[round(x,4) for x in info_each]} (H_S={H_S_initial:.4f})")

    # Pointer is conserved: the system z-populations are unchanged by recording.
    rho_S_nd = partial_trace(rho_nd, [0], n)
    pops_nd = np.real(np.diag(rho_S_nd))
    pops_init = np.real(np.diag(partial_trace(rho0, [0], n)))
    record("non-demolition: system pointer populations preserved by recording",
           np.allclose(pops_nd, pops_init, atol=1e-9),
           f"pops={np.round(pops_nd,4)} (init {np.round(pops_init,4)})")

    # -----------------------------------------------------------------------
    section("Part 2: ADDITIVITY of the record readout over disjoint fragments")
    # -----------------------------------------------------------------------
    # Two DISTINCT record functionals -- do not conflate:
    #
    #   J(F) := holevo_pointer_info(S, F) -- the recoverable pointer content
    #       of a fragment F: dephase S in the pointer basis, take the S<->F
    #       mutual information (= Holevo content of the pointer ensemble). On
    #       redundant perfect copies J SATURATES: J(F1 u F2) = J(F1) = J(F2)
    #       = H_S. It is strictly SUB-additive, NOT additive: reading two
    #       copies of the same registered fact yields the fact once.
    #
    #   I_mass(F) := sum_{k in F} I({k}), with the bounded model bridge
    #       I({k}) := J({k}) for each singleton pointer record. Record grants
    #       finite additivity of I; it does NOT grant this singleton Holevo
    #       normalization. The latter is an explicit model input.
    #
    # The bridge between the two at the perfect-recording plateau is exact
    # and discriminating:
    #   I_mass(F1 u F2) - J(F1 u F2) = (m - 1) * H_S   (m disjoint fragments)
    # -- the surplus counts the SAME registered pointer fact once per disjoint
    # record (redundancy), not additional pointer content. The gates below
    # compute singleton J values, union J values, and H_S separately, then
    # check compatibility of the supplied singleton bridge with the additive
    # extension. They do not claim to derive Record additivity or I({k})=J({k}).

    P0 = op(PROJ0, 0, n)
    P1 = op(PROJ1, 0, n)
    rho_nd_deph = P0 @ rho_nd @ P0 + P1 @ rho_nd @ P1

    J = {k: mutual_information(rho_nd_deph, [0], [k], n) for k in range(1, n)}
    F1, F2 = [1, 2], [3, 4]
    m_frag = len(F1 + F2)
    # record-mass = additive extension of the supplied singleton readouts;
    # recoverable content J(F) = JOINT dephased mutual information (saturates).
    I_mass_union = sum(J[k] for k in F1 + F2)
    J_F1 = mutual_information(rho_nd_deph, [0], F1, n)
    J_F2 = mutual_information(rho_nd_deph, [0], F2, n)
    J_union = mutual_information(rho_nd_deph, [0], F1 + F2, n)
    record("supplied singleton bridge plus Record additivity is compatible with "
           "I_mass(F1 U F2) - J(F1 U F2) = (m-1)*H_S",
           abs((I_mass_union - J_union) - (m_frag - 1) * H_S_initial) < 1e-6,
           f"{I_mass_union:.4f} - {J_union:.4f} = {m_frag - 1}*{H_S_initial:.4f}")
    record("recoverable content J is strictly SUB-additive (saturation, NOT "
           "additivity): J(F1 U F2) = J(F1) = J(F2) = H_S",
           abs(J_union - H_S_initial) < 1e-6
           and abs(J_F1 - H_S_initial) < 1e-6
           and abs(J_F2 - H_S_initial) < 1e-6
           and (J_F1 + J_F2 - J_union) > 0.5 * H_S_initial,
           f"J(F1)={J_F1:.4f}, J(F2)={J_F2:.4f}, J(union)={J_union:.4f}, "
           f"sum-minus-union={J_F1 + J_F2 - J_union:.4f}")

    # Compatibility boundary: the recovered pointer information about the
    # H_S-bit pointer SATURATES at H_S (no super-additivity). Reading more
    # disjoint fragments adds redundant copies, never more recoverable content
    # than H_S. Verify
    # I(S : F1 U F2) = H_S even though the record-mass = 4 * H_S (4 copies).
    I_union_recovered = holevo_pointer_info(rho_nd, 0, F1 + F2, n)
    record("two-functional split: recovered pointer info saturates at H_S "
           "(no super-additivity) despite redundant copies",
           abs(I_union_recovered - H_S_initial) < 1e-6 and I_mass_union > 1.9 * H_S_initial,
           f"I(S:F1F2)={I_union_recovered:.4f}=H_S, record-mass={I_mass_union:.4f}={4}*H_S")

    # The deeper claim: this additive set-function structure is consistent
    # ONLY because all fragments certify the SAME pointer value (objectivity).
    # Verify objectivity: every pair of fragments agrees on the pointer
    # (their records are perfectly cross-correlated through S).
    def fragments_agree(rho_deph: np.ndarray, k1: int, k2: int) -> float:
        """Mutual information between two environment fragments on the dephased
        state -- they share exactly the H_S pointer bits (objective consensus)."""
        return mutual_information(rho_deph, [k1], [k2], n)

    agree = [fragments_agree(rho_nd_deph, a, b) for a, b in combinations(range(1, n), 2)]
    record("objectivity: every pair of fragments shares exactly the pointer "
           "record H_S (one consistent value)",
           all(abs(x - H_S_initial) < 1e-6 for x in agree),
           f"pairwise I = {[round(x,4) for x in agree]} (H_S={H_S_initial:.4f})")

    # -----------------------------------------------------------------------
    section("Part 3: REDUNDANCY R_delta (quantum Darwinism plateau)")
    # -----------------------------------------------------------------------
    delta = 0.1
    R = redundancy_singletons(rho_nd, n_env, delta, H_S_initial)
    record("non-demolition: redundancy R_delta = n_env (every fragment informative)",
           R == n_env, f"R_(delta={delta}) = {R} of {n_env}")

    # Classical plateau: I(S:F) as a function of growing fragment size is flat
    # near H_S (each added qubit adds redundant, not new, pointer info).
    plateau = []
    for size in range(1, n_env + 1):
        frag = list(range(1, 1 + size))
        plateau.append(holevo_pointer_info(rho_nd, 0, frag, n))
    flat = all(abs(x - H_S_initial) < 1e-6 for x in plateau)
    record("non-demolition: classical plateau I(S:F) = H_S for all fragment sizes",
           flat, f"plateau = {[round(x,4) for x in plateau]} (H_S={H_S_initial:.4f})")

    # -----------------------------------------------------------------------
    section("Part 4: PERSISTENCE under continued evolution")
    # -----------------------------------------------------------------------
    # PERSISTENCE has two genuine, distinct statements -- and a careful caveat.
    #
    # (4a) FUNDAMENTAL invariant: because Pi_S is a constant of motion
    #      ([U,Pi_S]=0), the system's pointer POPULATIONS are time-invariant for
    #      ALL evolution times. The pointer value therefore cannot conflict
    #      with an idle completed record. This does not by itself preserve the
    #      fragment state; the separate caveat below makes that distinction.
    U_step = unitary(H_nd, t_rec)
    psi_p = psi_nd.copy()
    pops_over_time = []
    for _ in range(8):
        psi_p = U_step @ psi_p
        pops_over_time.append(np.real(np.diag(partial_trace(density(psi_p), [0], n))))
    pops_frozen = all(np.allclose(p, pops_nd, atol=1e-9) for p in pops_over_time)
    record("persistence (4a): non-demolition freezes system pointer populations "
           "for ALL times (recorded value never changes)",
           pops_frozen, f"pops stay {np.round(pops_nd,4)}")

    # (4b) CAVEAT made explicit (honesty): a single COHERENT controlled rotation
    #      re-applied to the SAME fragment is reversible -- re-kicking E_1 rotates
    #      its pointer-conditioned states past orthogonality, so I(S:E_1)
    #      oscillates. A persistent record needs the physically correct
    #      Darwinism setup: each step writes onto a FRESH fragment (a von Neumann
    #      measurement chain) and a finished fragment goes idle. We verify that
    #      once E_k has recorded and is idle, its bit is PRESERVED while later
    #      steps record onto fresh fragments.
    U_e1 = record_unitary_single(n_env, 1, g, t_rec)
    psi_e1_once = U_e1 @ psi0
    psi_e1_twice = U_e1 @ psi_e1_once
    info_e1_once = holevo_pointer_info(density(psi_e1_once), 0, [1], n)
    info_e1_twice = holevo_pointer_info(density(psi_e1_twice), 0, [1], n)
    record("persistence caveat: re-kicking the same coherent fragment can erase "
           "its record, so fresh/idle/decoupling is a real hypothesis",
           abs(info_e1_once - H_S_initial) < 1e-6 and info_e1_twice < 1e-6,
           f"I_once={info_e1_once:.4f}, I_twice={info_e1_twice:.2e}")

    psi_chain = psi0.copy()
    chain_snapshots = []  # I(S:E_1) measured after each later fragment records
    for k in range(1, n):
        # record S onto fragment k only (fresh fragment), then leave it idle
        psi_chain = record_unitary_single(n_env, k, g, t_rec) @ psi_chain
        chain_snapshots.append(holevo_pointer_info(density(psi_chain), 0, [1], n))
    # E_1 recorded at step 1; its bit must stay = H_S as E_2..E_n record after it
    e1_persists = all(abs(x - H_S_initial) < 1e-6 for x in chain_snapshots)
    record("persistence (4b): in a fresh-fragment chain, an idle finished "
           "fragment keeps its full bit while later fragments record",
           e1_persists, f"I(S:E_1) after each later record = {[round(x,4) for x in chain_snapshots]}")
    # and redundancy GROWS monotonically along the chain (Darwinism proliferation)
    R_chain = redundancy_singletons(density(psi_chain), n_env, 0.1, H_S_initial)
    record("persistence (4b): redundancy accumulates to R = n_env along the chain",
           R_chain == n_env, f"final R = {R_chain} of {n_env}")

    # -----------------------------------------------------------------------
    section("Part 5: DEMOLITION CONTROL -- [H_int, Pi_S] != 0")
    # -----------------------------------------------------------------------
    H_dm = H_demolition(n_env, g)
    cdm = comm(H_dm, Pi_S)
    dm_comm_norm = float(np.linalg.norm(cdm))
    record("demolition control: [H_int, Pi_S] != 0 (handle is sigma_x(S))",
           dm_comm_norm > 1e-6, f"||[H,Pi_S]||={dm_comm_norm:.3f}")

    # Evaluate the demolition channel at the SAME recording time t_rec at which
    # the non-demolition channel forms a perfect record -- a matched comparison.
    U_dm = unitary(H_dm, t_rec)
    psi_dm = evolve(psi0, U_dm)
    rho_dm = density(psi_dm)

    info_dm_each = [holevo_pointer_info(rho_dm, 0, [k], n) for k in range(1, n)]
    R_dm = redundancy_singletons(rho_dm, n_env, delta, H_S_initial)
    record("demolition control: fragments fail to carry the pointer record H_S "
           "(at the same t_rec where non-demolition is perfect)",
           not all(abs(x - H_S_initial) < 1e-6 for x in info_dm_each),
           f"per-fragment z-pointer I = {[round(x,4) for x in info_dm_each]} (H_S={H_S_initial:.4f})")
    record("demolition control: redundancy collapses (R_delta < n_env)",
           R_dm < n_env, f"R_(delta={delta}) = {R_dm} of {n_env}")

    # (b) Non-persistence at the ROOT: under demolition the system pointer
    #     POPULATIONS are NOT conserved (mirror of 4a). The recorded value
    #     itself drifts in time, so any classical record made at one time is
    #     falsified at a later time -- no persistent objective record can exist.
    psi_s = psi0.copy()
    dm_pops = []
    for _ in range(8):
        psi_s = U_dm @ psi_s
        dm_pops.append(np.real(np.diag(partial_trace(density(psi_s), [0], n))))
    pops_drift = max(abs(p[0] - pops_nd[0]) for p in dm_pops)
    record("demolition control: system pointer populations DRIFT in time "
           "(recorded value is not frozen => record is non-persistent)",
           pops_drift > 1e-2,
           f"max |Delta pop_0| over steps = {pops_drift:.4f} (vs 0 for non-demolition)")
    # also: the would-be recorded value (system z-population) is non-monotone in
    # time -- it OSCILLATES (the system precesses), so no fragment can hold a
    # stable copy; a record written early is wrong later and vice-versa.
    dm_pop0 = [p[0] for p in dm_pops]
    increases = sum(1 for i in range(1, len(dm_pop0)) if dm_pop0[i] > dm_pop0[i - 1] + 1e-6)
    decreases = sum(1 for i in range(1, len(dm_pop0)) if dm_pop0[i] < dm_pop0[i - 1] - 1e-6)
    record("demolition control: would-be recorded value (pop_0) oscillates "
           "in time (non-monotone => no stable copy possible)",
           increases > 0 and decreases > 0,
           f"up={increases}, down={decreases}, pop_0 trace={[round(float(x),3) for x in dm_pop0]}")
    # AND demolition records the WRONG observable: it imprints sigma_x(S)
    # (the conserved handle), not the pointer sigma_z(S). Show the full
    # system<->E_1 correlation is nonzero while the z-pointer info is ~0.
    full_corr = mutual_information(rho_dm, [0], [1], n)
    z_pointer_corr = holevo_pointer_info(rho_dm, 0, [1], n)
    record("demolition control: records the WRONG observable -- full I(S:E_1)>0 "
           "but z-pointer info ~0 (record is in a non-pointer basis)",
           full_corr > 1e-2 and z_pointer_corr < 1e-2,
           f"full I(S:E_1)={full_corr:.4f}, z-pointer info={z_pointer_corr:.4f}")

    # (c) additivity-of-record fails: there is no single objective pointer that
    #     all fragments agree on (the demolition dynamics produces a basis the
    #     fragments do not share a consistent classical value in). We test the
    #     pointer-objectivity functional that succeeded in the ND case.
    P0d = op(PROJ0, 0, n)
    P1d = op(PROJ1, 0, n)
    rho_dm_deph = P0d @ rho_dm @ P0d + P1d @ rho_dm @ P1d
    agree_dm = [mutual_information(rho_dm_deph, [a], [b], n)
                for a, b in combinations(range(1, n), 2)]
    record("demolition control: fragments do NOT objectively agree on Pi_S",
           not all(abs(x - H_S_initial) < 1e-6 for x in agree_dm),
           f"pairwise I = {[round(x,4) for x in agree_dm]} (vs H_S={H_S_initial:.4f})")

    # -----------------------------------------------------------------------
    section("Part 6: MONOTONE LINK -- redundancy vs the non-demolition norm")
    # -----------------------------------------------------------------------
    # Sweep the interpolation handle = cos th sigma_z + sin th sigma_x.
    # ||[H,Pi_S]|| grows with sin(theta); show the objective-record quality
    # (min over fragments of pointer info, at the recording time) DEGRADES
    # monotonically as the non-demolition condition is violated.
    thetas = np.linspace(0.0, np.pi / 2, 9)
    quality = []
    comm_norms = []
    for th in thetas:
        Hth = H_partial_demolition(n_env, g, th)
        comm_norms.append(float(np.linalg.norm(comm(Hth, Pi_S))))
        Uth = unitary(Hth, t_rec)
        rho_th = density(Uth @ psi0)
        q = min(holevo_pointer_info(rho_th, 0, [k], n) for k in range(1, n))
        quality.append(q)
    # theta=0 is the maximum-quality, zero-commutator point.
    record("sweep: theta=0 (non-demolition) maximizes objective-record quality",
           abs(quality[0] - max(quality)) < 1e-9 and comm_norms[0] < 1e-12,
           f"quality(theta=0)={quality[0]:.4f}, max={max(quality):.4f}")
    # quality is (weakly) monotone decreasing as the commutator norm grows from 0.
    mono = all(quality[i] <= quality[i - 1] + 1e-6 for i in range(1, len(quality)))
    record("sweep: objective-record quality decreases as ||[H,Pi_S]|| grows",
           mono,
           f"q={[round(x,3) for x in quality]} vs ||c||={[round(x,3) for x in comm_norms]}")
    record("sweep: only the zero-commutator endpoint gives a perfect record "
           "(quality = H_S at theta=0, degraded elsewhere)",
           abs(quality[0] - H_S_initial) < 1e-6 and quality[-1] < quality[0] - 1e-3,
           f"q[0]={quality[0]:.4f}=H_S, q[-1]={quality[-1]:.4f}")

    # -----------------------------------------------------------------------
    section("Part 6b: POINTER-CONSERVATION IFF for [H,Pi_S]=0 (random-H theorem)")
    # -----------------------------------------------------------------------
    # The load-bearing all-H statement is pointer-population conservation, not
    # record formation. The clean statement is the Heisenberg equation for the
    # pointer populations P_k (spectral projectors of Pi_S):
    #     d/dt <P_k>_t |_{t=0} = i <[H, P_k]> ,
    # which vanishes for ALL states and ALL times  <=>  [H, P_k]=0  <=>
    # [H, Pi_S]=0. We certify both directions over RANDOM Hamiltonians (so the
    # result is about the COMMUTATION property, not the specific sigma_z(x)sigma_x
    # operator used in the worked example). This does NOT say QND alone writes a
    # record; Part 6c gives commuting non-recording counterexamples.
    rng = np.random.default_rng(20260605)

    def rand_herm(m: int) -> np.ndarray:
        A = rng.normal(size=(2 ** m, 2 ** m)) + 1j * rng.normal(size=(2 ** m, 2 ** m))
        return (A + A.conj().T) / 2

    w_pi, V_pi = np.linalg.eigh(Pi_S)
    pop_mask = np.abs(w_pi[:, None] - w_pi[None, :]) < 1e-9
    P0_op = op(PROJ0, 0, n)

    def project_commutant(H: np.ndarray) -> np.ndarray:
        Hd = V_pi.conj().T @ H @ V_pi
        return V_pi @ (Hd * pop_mask) @ V_pi.conj().T

    # SUFFICIENCY FOR POINTER CONSERVATION: ANY random H commuting with Pi_S
    # conserves pointer populations for all states & times. The operator
    # identity U^dag P_0 U=P_0 is the exact all-state check.
    preservation_fail = 0
    for _ in range(60):
        H = project_commutant(rand_herm(n))
        t = rng.uniform(0, 3)
        U_h = unitary(H, t)
        if np.linalg.norm(U_h.conj().T @ P0_op @ U_h - P0_op) > 1e-8:
            preservation_fail += 1
    record("pointer-conservation sufficiency: any random H with [H,Pi_S]=0 "
           "conserves pointer populations (not a record-formation claim)",
           preservation_fail == 0, f"failures = {preservation_fail}/60")

    # NECESSITY FOR POINTER CONSERVATION: every random H with [H,Pi_S]!=0 admits
    # a state instantaneously moving a pointer population, via
    # max|eig(i[H,P_0])| > 0.
    nec_detect = 0
    nec_total = 0
    for _ in range(60):
        H = rand_herm(n)
        if np.linalg.norm(comm(H, Pi_S)) < 1e-9:
            continue
        nec_total += 1
        iC = 1j * comm(H, P0_op)
        iC = (iC + iC.conj().T) / 2
        if np.max(np.abs(np.linalg.eigvalsh(iC))) > 1e-9:
            nec_detect += 1
    record("pointer-conservation necessity: every random H with [H,Pi_S]!=0 "
           "has a state that instantaneously moves P_0",
           nec_detect == nec_total and nec_total > 0,
           f"detected {nec_detect}/{nec_total} non-commuting samples")

    # -----------------------------------------------------------------------
    section("Part 6c: QND alone is NOT record-sufficient")
    # -----------------------------------------------------------------------
    # Scope boundary: [H,Pi_S]=0 is necessary for all-state persistent
    # pointer values, but it is not sufficient to make fragments carry records.
    # A record also needs a nontrivial imprint channel from S to the fragments.
    H_zero = np.zeros_like(H_nd)
    U_zero = unitary(H_zero, t_rec)
    rho_zero = density(U_zero @ psi0)
    info_zero = [holevo_pointer_info(rho_zero, 0, [k], n) for k in range(1, n)]
    R_zero = redundancy_singletons(rho_zero, n_env, delta, H_S_initial)
    record("QND-alone counterexample: H=0 commutes with Pi_S but writes no fragment record",
           np.linalg.norm(comm(H_zero, Pi_S)) < 1e-12
           and max(info_zero) < 1e-9 and R_zero == 0,
           f"max I={max(info_zero):.2e}, R={R_zero}")

    H_system_only = op(SZ, 0, n)
    U_system_only = unitary(H_system_only, t_rec)
    rho_system_only = density(U_system_only @ psi0)
    info_system_only = [holevo_pointer_info(rho_system_only, 0, [k], n) for k in range(1, n)]
    record("QND-alone counterexample: system-only pointer phase commutes but does not imprint E",
           np.linalg.norm(comm(H_system_only, Pi_S)) < 1e-12
           and max(info_system_only) < 1e-9,
           f"max I={max(info_system_only):.2e}")

    H_env_eigenstate = g * (op(SZ, 0, n) @ op(SZ, 1, n))
    U_env_eigenstate = unitary(H_env_eigenstate, t_rec)
    rho_env_eigenstate = density(U_env_eigenstate @ psi0)
    info_env_eigenstate = [
        holevo_pointer_info(rho_env_eigenstate, 0, [k], n)
        for k in range(1, n)
    ]
    record("QND-alone counterexample: nonzero commuting S-E interaction with E "
           "in an eigenstate writes no fragment record",
           np.linalg.norm(H_env_eigenstate) > 1e-9
           and np.linalg.norm(comm(H_env_eigenstate, Pi_S)) < 1e-12
           and max(info_env_eigenstate) < 1e-9,
           f"||H||={np.linalg.norm(H_env_eigenstate):.2f}, max I={max(info_env_eigenstate):.2e}")

    record("sufficiency construction needs both QND and nonzero controlled S-to-E imprint",
           nd_comm_norm < 1e-12 and min(info_each) > H_S_initial - 1e-6
           and max(info_zero) < 1e-9 and max(info_env_eigenstate) < 1e-9,
           f"controlled min I={min(info_each):.4f}; zero max I={max(info_zero):.2e}; "
           f"eigenstate max I={max(info_env_eigenstate):.2e}")

    # -----------------------------------------------------------------------
    section("Part 6d: STEP-LEVEL iff [U,Pi_S]=0 and scope witnesses")
    # -----------------------------------------------------------------------
    # The generator-level iff (Part 6b) is a statement about the continuous
    # flow (all states, ALL TIMES). The single-step analogue is:
    #     pointer populations preserved for ALL states by the step U
    #        <=>  U^dag P_k U = P_k  <=>  [U, Pi_S] = 0.
    # Certified over random unitaries both ways. Then two witnesses separate
    # the quantifiers. First, a perfect
    # record-forming step (controlled-NOT) has [U, Pi_S] = 0 but admits a
    # Hermitian generator H_log with [H_log, Pi_S] != 0 and exp(-i H_log) = U
    # EXACTLY -- so generator-level commutation [H_int, Pi_S] = 0 is a flow
    # property, NOT a necessary condition read off one finite record-forming
    # step. Second, a globally noncommuting unitary can agree with CNOT on the
    # entire fresh-fragment input subspace and form the same record there, so
    # record formation on that subspace does not force global [U,Pi_S]=0.

    step_suff_fail = 0
    for _ in range(60):
        U_c = unitary(project_commutant(rand_herm(n)), 1.0)
        if np.linalg.norm(U_c.conj().T @ P0_op @ U_c - P0_op) > 1e-8:
            step_suff_fail += 1
    record("step-level sufficiency: any random U with [U,Pi_S]=0 preserves "
           "pointer populations for all states (operator-identity check)",
           step_suff_fail == 0, f"failures = {step_suff_fail}/60")

    step_nec_detect = 0
    step_nec_total = 0
    for _ in range(60):
        U_r = unitary(rand_herm(n), 1.0)
        if np.linalg.norm(comm(U_r, Pi_S)) < 1e-9:
            continue
        step_nec_total += 1
        D = U_r.conj().T @ P0_op @ U_r - P0_op
        if np.max(np.abs(np.linalg.eigvalsh(D))) > 1e-9:
            step_nec_detect += 1
    record("step-level necessity: every random U with [U,Pi_S]!=0 moves some "
           "state's pointer population",
           step_nec_detect == step_nec_total and step_nec_total > 0,
           f"detected {step_nec_detect}/{step_nec_total} non-commuting samples")

    # The noncommuting-logarithm WITNESS on the minimal S+E pair:
    # CNOT = P0(S) x I + P1(S) x X(E). Eigenspaces: -1 on |1,->, +1 elsewhere.
    # H_log puts the pi branch on the -1 eigenvector and a 2*pi-shifted branch
    # on a +1-eigenspace vector that MIXES the Pi_S sectors -- Hermitian,
    # exponentiates to CNOT exactly, fails to commute with Pi_S.
    n2q = 2
    Pi_S2 = op(SZ, 0, n2q)
    CNOT = np.kron(PROJ0, I2) + np.kron(PROJ1, SX)
    ket1 = np.array([0.0, 1.0], dtype=complex)
    minus = np.array([1.0, -1.0], dtype=complex) / np.sqrt(2.0)
    plus = np.array([1.0, 1.0], dtype=complex) / np.sqrt(2.0)
    v_m = np.kron(ket1, minus)
    v_mix = (np.kron(KET0, KET0) + np.kron(ket1, plus)) / np.sqrt(2.0)
    H_log = (np.pi * np.outer(v_m, v_m.conj())
             + 2.0 * np.pi * np.outer(v_mix, v_mix.conj()))
    U_from_log = unitary(H_log, 1.0)
    record("witness: exp(-i H_log) reproduces the controlled-NOT step exactly",
           np.linalg.norm(U_from_log - CNOT) < 1e-12,
           f"||exp(-iH_log)-CNOT|| = {np.linalg.norm(U_from_log - CNOT):.2e}")
    wit_comm = float(np.linalg.norm(comm(H_log, Pi_S2)))
    record("witness: the generator fails to commute, ||[H_log,Pi_S]|| = 2*sqrt(2)*pi",
           abs(wit_comm - 2.0 * np.sqrt(2.0) * np.pi) < 1e-9,
           f"||[H_log,Pi_S]|| = {wit_comm:.6f} "
           f"(2*sqrt(2)*pi = {2.0 * np.sqrt(2.0) * np.pi:.6f})")
    record("witness: the step itself commutes, [CNOT, Pi_S] = 0 (step-level QND holds)",
           float(np.linalg.norm(comm(CNOT, Pi_S2))) < 1e-12,
           f"||[CNOT,Pi_S]|| = {float(np.linalg.norm(comm(CNOT, Pi_S2))):.2e}")
    psi_w = kron_list([bloch_ket(SYS_THETA, SYS_PHI), KET0])
    rho_w = density(CNOT @ psi_w)
    J_w = holevo_pointer_info(rho_w, 0, [1], n2q)
    H_S_w = pointer_entropy(rho_w, 0, n2q)
    pops_w_before = np.real(np.diag(partial_trace(density(psi_w), [0], n2q)))
    pops_w_after = np.real(np.diag(partial_trace(rho_w, [0], n2q)))
    record("witness: the CNOT step forms the full fresh-fragment record and "
           "preserves the pointer populations",
           abs(J_w - H_S_w) < 1e-9 and H_S_w > 0.01
           and np.allclose(pops_w_before, pops_w_after, atol=1e-12),
           f"J = {J_w:.6f} = H_S = {H_S_w:.6f}; pops preserved")

    # Fresh-subspace boundary witness. In computational-basis column order,
    # U_fresh maps |00>->|00>, |01>->|10>, |10>->|11>, |11>->|01>.
    # Its columns on the complete fresh-fragment subspace span{|00>,|10>}
    # equal CNOT's columns, so it makes the same record for every system input
    # a|0>+b|1> with E initially |0>. Its extension away from that occupied
    # subspace is globally noncommuting with Pi_S.
    U_fresh = np.zeros((4, 4), dtype=complex)
    U_fresh[[0, 2, 3, 1], np.arange(4)] = 1.0
    rho_fresh = density(U_fresh @ psi_w)
    J_fresh = holevo_pointer_info(rho_fresh, 0, [1], n2q)
    pops_fresh = np.real(np.diag(partial_trace(rho_fresh, [0], n2q)))
    fresh_comm = float(np.linalg.norm(comm(U_fresh, Pi_S2)))
    record("scope witness: perfect recording on every fresh-fragment input does "
           "not force global [U,Pi_S]=0",
           np.allclose(U_fresh.conj().T @ U_fresh, np.eye(4), atol=1e-12)
           and np.allclose(U_fresh[:, [0, 2]], CNOT[:, [0, 2]], atol=1e-12)
           and abs(J_fresh - H_S_w) < 1e-9
           and np.allclose(pops_fresh, pops_w_before, atol=1e-12)
           and fresh_comm > 1e-6,
           f"J={J_fresh:.6f}=H_S; ||[U_fresh,Pi_S]||={fresh_comm:.6f}")

    # -----------------------------------------------------------------------
    section("Part 7: ALL-STATE-PERSISTENCE class and construction controls")
    # -----------------------------------------------------------------------
    # (i) Conserved pointer: [H_int, Pi_S]=0 => Pi_S commutes with U => Pi_S
    #     is a constant of motion (Heisenberg). Verify U^dag Pi_S U = Pi_S.
    Pi_evolved = U_nd.conj().T @ Pi_S @ U_nd
    record("all-state persistence: U^dag Pi_S U = Pi_S for the controlled-copy step",
           np.allclose(Pi_evolved, Pi_S, atol=1e-10))
    Pi_evolved_dm = U_dm.conj().T @ Pi_S @ U_dm
    record("demolition control does NOT conserve Pi_S",
           not np.allclose(Pi_evolved_dm, Pi_S, atol=1e-6))

    # (ii) Construction control. The local single-fragment sum produces a
    #      product of conditional fragment states: dephased pairwise correlation
    #      is exactly the shared pointer entropy H_S, with no excess. A specific
    #      non-local env-env scramble below is a destructive control: it keeps
    #      the system pointer fixed but erases the two acted-on singleton records
    #      and injects excess pairwise correlation. This does not prove that
    #      every non-local record channel fails.
    base_pair = [mutual_information(rho_nd_deph, [a], [b], n)
                 for a, b in combinations(range(1, n), 2)]
    record("locality (local baseline): fragments are independent copies, "
           "dephased I(E_a:E_b) = H_S (only the shared pointer, no excess)",
           all(abs(x - H_S_initial) < 1e-6 for x in base_pair),
           f"pairwise I = {[round(x,4) for x in base_pair]} (H_S={H_S_initial:.4f})")

    # Now form the local record, then apply a non-local env-env entangling
    # unitary (commuting with Pi_S and acting only on the environment). It
    # destroys the acted-on singleton records while producing excess E_1:E_2
    # correlation; record erasure is part of the control, not held fixed.
    n2 = n_env + 1
    # env-env entangler: exp(-i (pi/4) sigma_x(E_1) sigma_x(E_2)) -- a genuine
    # 2-fragment entangling gate that commutes with Pi_S = sigma_z(S).
    H_ee = (np.pi / 4.0) * (op(SX, 1, n2) @ op(SX, 2, n2))
    U_ee = unitary(H_ee, 1.0)
    record("locality probe: non-local env-env gate still commutes with Pi_S",
           np.linalg.norm(comm(H_ee, Pi_S)) < 1e-10)
    psi_ec = U_ee @ psi_nd  # record first (psi_nd), then non-local env scramble
    rho_ec = density(psi_ec)
    P0e = op(PROJ0, 0, n2)
    P1e = op(PROJ1, 0, n2)
    rho_ec_deph = P0e @ rho_ec @ P0e + P1e @ rho_ec @ P1e
    pair_12 = mutual_information(rho_ec_deph, [1], [2], n2)  # the entangled pair
    excess = pair_12 - H_S_initial
    scrambled_J = [holevo_pointer_info(rho_ec, 0, [k], n2) for k in range(1, n2)]
    record("non-local destructive control erases acted-on singleton records and "
           "injects EXCESS pairwise correlation I(E_1:E_2) > H_S",
           scrambled_J[0] < 1e-9 and scrambled_J[1] < 1e-9
           and all(abs(x - H_S_initial) < 1e-6 for x in scrambled_J[2:])
           and excess > 1e-3,
           f"J(singletons)={[round(x,4) for x in scrambled_J]}; "
           f"I(E_1:E_2)={pair_12:.4f}, excess={excess:.4f}")

    # -----------------------------------------------------------------------
    section("Part 8: supplied conserved-charge transfer block class check")
    # -----------------------------------------------------------------------
    # A supplied OS-style transfer block T = exp(-H) built from a
    # reflection-positive, number-/charge-conserving action has the
    # all-state-persistence signature: a conserved pointer/charge observable that
    # commutes with T.
    # Model T by a positive, Hermitian (=> reflection-symmetric in the simplest
    # case) transfer operator that commutes with a conserved charge Q. This is a
    # finite class-membership check only; it is not a proof that any physical
    # framework OS transfer also supplies the fragment-imprinting record channel.
    Q = op(SZ, 0, n)  # the conserved charge / pointer playing Pi_S's role
    # A number-conserving local transfer block: diagonal-in-charge hops.
    H_T = (op(SZ, 0, n) @ op(SZ, 1, n)
           + 0.5 * (op(SX, 0, n) @ op(SX, 1, n) + op(SY, 0, n) @ op(SY, 1, n)))
    # the XX+YY ("hopping") term conserves total sigma_z over the pair? check:
    Q_total = sum(op(SZ, i, n) for i in range(2))
    record("supplied transfer block: hopping (XX+YY) conserves total charge Q_total on the bond",
           np.linalg.norm(comm(H_T, Q_total)) < 1e-10,
           f"||[H_T,Q_tot]||={np.linalg.norm(comm(H_T, Q_total)):.2e}")
    # Positivity of the genuine Euclidean transfer e^{-H_T}:
    T_eucl = (lambda w, V: (V * np.exp(-w)) @ V.conj().T)(*np.linalg.eigh(H_T))
    eig_T = np.linalg.eigvalsh(T_eucl)
    record("supplied transfer block: Euclidean-style transfer e^{-H} is positive",
           np.all(eig_T > 0), f"min eig = {eig_T.min():.4f}")
    record("supplied transfer block: commutes with the conserved charge => lies in the all-state persistence class",
           np.linalg.norm(comm(T_eucl, Q_total)) < 1e-10,
           f"||[T,Q_tot]||={np.linalg.norm(comm(T_eucl, Q_total)):.2e}")

    # -----------------------------------------------------------------------
    section("Part 9: NOT pinned -- coupling strength / action magnitude / beta")
    # -----------------------------------------------------------------------
    # The objective-record / non-demolition structure is INDEPENDENT of the
    # coupling g: any g>0 yields a perfect non-demolition record at the
    # appropriately rescaled time t = pi/(4g). So the formation constraint
    # fixes the FORM ([H,Pi_S]=0) but not the MAGNITUDE.
    forms_record_at = []
    for g_test in [0.25, 0.5, 1.0, 2.0, 3.7]:
        H_g = H_nondemolition(n_env, g_test)
        U_g = unitary(H_g, np.pi / (4.0 * g_test))
        rho_g = density(U_g @ psi0)
        q = min(holevo_pointer_info(rho_g, 0, [k], n) for k in range(1, n))
        forms_record_at.append(q)
    record("NOT pinned: any coupling g>0 forms an equally good record (form, not magnitude)",
           all(abs(x - H_S_initial) < 1e-6 for x in forms_record_at),
           f"record quality across g = {[round(x,4) for x in forms_record_at]} (all=H_S)")

    # -----------------------------------------------------------------------
    section("Part 10: source-note firewall (scope claims present in the note)")
    # -----------------------------------------------------------------------
    note = (REPO_ROOT / "docs"
            / "RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md")
    if note.exists():
        text = note.read_text(encoding="utf-8")
        for phrase in [
            "It does not derive a dynamics, an action, gauge bosons",
            "It does not pin the coupling strength",
            "says **nothing** about `beta = 6`",
            "does not derive the quantum-Darwinism bridge",
            "does not claim that either generator-level",
            "does not use OS-transfer membership as a record-formation proof",
            "does not establish the lattice/continuum or interacting-field",
        ]:
            record(f"source-note firewall present: {phrase[:48]}...", phrase in text)
    else:
        record("source-note present (firewall checks skipped: note not found)", False,
               "note file missing")

    # -----------------------------------------------------------------------
    section("VERDICT (honest)")
    # -----------------------------------------------------------------------
    print("""
BOUNDED ALGEBRAIC RESULTS, with explicit scope:

  On this explicit S + E_1..E_n model there are three load-bearing results,
  followed by scope witnesses and controls:

    - Exact pointer-conservation theorem (Part 6b): by the Heisenberg equation
      d<P_k>/dt = i<[H,P_k]>, the pointer populations are frozen for ALL states
      and ALL times IFF [H,Pi_S]=0. Verified over random H (60/60
      exact operator-identity sufficiency, 60/60 necessity). This is a theorem
      about the commutation property, not a record-formation necessity claim.

    - Exact all-state step theorem (Part 6d): pointer populations are preserved
      for ALL joint input states by U IFF [U,Pi_S]=0. The random sufficiency
      gate checks U^dag P_0 U=P_0 directly; the necessity gate finds a moving
      state from the nonzero Hermitian difference U^dag P_0 U-P_0.

    - Positive controlled-copy construction (Parts 1-4): the explicit nonzero
      local Hamiltonian H = g sigma_z(S) x sum_k sigma_x(E_k), at
      t = pi/(4g), forms a perfect redundant persistent objective record:
      R_delta = n_env, plateau = H_S, finished idle fragments persist, and
      fragments objectively agree. The bounded model supplies the singleton
      bridge I({k}) := J({k}); Record additivity extends it to
      I_mass(F)=sum_k J({k}), while recoverable union content J(F) SATURATES
      at H_S. Part 2 checks the plateau compatibility identity
      I_mass-J=(m-1)H_S without claiming to derive the singleton bridge.

    - QND-alone counterexamples (Part 6c): H=0, a system-only pointer phase,
      and a nonzero commuting S-E interaction with E held in an eigenstate
      conserve Pi_S but write no environment record.

    - Scope witnesses (Part 6d): the controlled-NOT step has [CNOT,Pi_S]=0,
      forms the full fresh-fragment record, and admits a Hermitian generator H_log with
      exp(-i H_log) = CNOT exactly and ||[H_log,Pi_S]|| = 2*sqrt(2)*pi != 0:
      generator-level commutation [H_int,Pi_S]=0 is the continuous-flow
      condition, not a property forced by one record-forming step. Separately,
      a globally noncommuting U_fresh agrees with CNOT on the complete
      span{|00>,|10>} fresh-fragment input subspace and forms the same record.
      Record formation on that subspace therefore does not force global
      [U,Pi_S]=0.

    - Demolition controls (Parts 5-6): a noncommuting sigma_x(S) handle records
      the wrong observable, collapses redundancy, makes the pointer populations
      oscillate, and reaches no objective pointer consensus. The interpolation
      shows this controlled-copy quality degrades as ||[H,Pi_S]|| grows for
      the tested handle family.

  All-state-persistence class and construction controls (Part 7-8):
    (a) [U,Pi_S]=0 characterizes all-state pointer persistence,
    (b) the positive construction has a nontrivial fragment-imprinting channel,
    (c) its local single-fragment sum produces independent conditional copies;
        a specific non-local env-env scramble erases the acted-on singleton
        records and injects EXCESS pairwise correlation I(E_a:E_b) > H_S,
    (d) a supplied number-conserving reflection-positive OS-style transfer
        block T = e^{-H} with [T,Q]=0 lies in the all-state conserved-charge
        class. The runner does not establish reflection positivity itself.

  Relative to the two-endpoint Gauss-law gauge-structure companion, this note
  adds exact all-state temporal commutator criteria and a separate sufficient
  finite controlled-copy construction. It does not derive a universal
  formation constraint on U/T.

HONEST LIMITS (no over-claim):
  - This is not a from-nothing derivation of dynamics. The positive
    record-formation result is a controlled-copy construction on
    the explicit finite model, conditional on modelling 'record' as a
    redundantly-imprinted, objective, persistent system observable (the
    quantum-Darwinism bridge) and on I({k}) := J({k}). The Lattice, Qubit,
    Admissibility, and Record axioms do not supply those identifications, the
    selected carrier/pointer, or the dynamics.
  - We do NOT claim arbitrary pointer-non-demolition Hamiltonians form records.
    H=0 is pointer-non-demolishing and writes no fragment. The sufficient
    record-forming construction uses the nonzero controlled-copy coupling,
    recording time, and fresh-fragment/idle-fragment persistence hypotheses.
    The runner also shows that re-using the same coherent fragment can erase
    the copy, so persistence is the fresh/idle/decoupled-fragment statement.
  - The pointer Pi_S=sigma_z(S) is an explicit bounded model input. Conservation
    does not uniquely select it from a possibly trivial or non-unique commutant.
  - It does NOT derive the action, the coupling g (Part 9: any g works), the
    transfer-matrix magnitude, or beta=6. It proves all-state conservation
    criteria and tests one explicit local controlled-copy channel as a
    sufficient record-writing construction.
  - It does NOT prove that a physical framework OS transfer writes records.
    Part 8 checks only conserved-charge transfer-class membership.
  - Pointer non-demolition is necessary and sufficient for all-state pointer
    persistence -- at the FLOW level for the generator ([H,Pi_S]=0, Part 6b)
    and at the STEP level for the unitary ([U,Pi_S]=0, Part 6d). The
    generator-level condition is not forced by a single record-forming step,
    and the global step condition is not forced by formation on the supplied
    fresh-fragment subspace. Neither condition is by itself sufficient for
    record formation. The lattice/continuum and interacting generalization is
    not established here.
  - We do NOT claim 'derived the action' or 'derived the dynamics'. We claim a
    pair of all-state pointer-conservation criteria and a controlled-copy
    sufficient construction on the explicit system, given the bounded bridges.
""")

    print("=" * 78)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 78)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
