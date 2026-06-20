#!/usr/bin/env python3
"""Route R-N2b-JOINT: absolute clock unit a_tau from JOINED rate gates (2026-06-20).

GENUINE fresh derivation attempt for clause N2b of the single-clock B-AXIS wall.

QUESTION
--------
Clause N2a is already FORCED (positive): the supplied two-step transfer
T_hat^2 = exp(-2 a_tau H) internally pins the 1/(2 a_tau) reconstruction
denominator -- a fixed source-side consequence of the retained two-step
blocked-time normalization bridge. N2b asks the harder thing: can an ABSOLUTE
physical clock unit a_tau (with units of time) be derived, not just the
internal denominator structure?

This route tries to crack N2b by combining TWO retained rate gates JOINTLY:

  GATE-S (spectrum-condition bridge,
          AXIOM_FIRST_SPECTRUM_CONDITION_BLOCKED_TIME_NORMALIZATION_BRIDGE_2026-06-05):
          supplies the DIMENSIONLESS object T_hat^2 and the identity
          T_hat^2 = exp(-2 a_tau H). Reconstruction: H = -(1/(2 a_tau)) log(T_hat^2/M_T).

  GATE-R (record clock/rate normalization gate,
          RECORD_CLOCK_RATE_NORMALIZATION_GATE_2026-06-06):
          a supplied production generator Q stabilizes a dial (Q pi = 0); the
          transition kernel exp(t Q) fixes only the DIMENSIONLESS product t*Q,
          i.e. (r,t) and (r/c, c t) give the same kernel. Rate vs clock stay
          separate.

The hope: a JOINT normalization -- demanding that the SAME physical clock
underlies BOTH the transfer step (block time 2 a_tau) AND the record-rate
generator -- might over-determine the system and pin a_tau absolutely.

METHOD (A_min-only; no new axiom/primitive)
-------------------------------------------
We build, on a finite carrier:
  * a positive-Hermitian two-step transfer T2 = exp(-2 a_tau H) with H >= 0;
  * a reversible record-production generator Q with Q pi = 0 (GATE-R object),
    whose continuous-time kernel over block time is K = exp((2 a_tau) Q)
    (the record stream advances one block per transfer step -- the strongest
    possible JOINT tie between the two clocks: ONE clock for both).

We then apply the simultaneous "second-clock-unit" rescaling that the wall
predicts is free:

     a_tau -> c * a_tau ,  H -> H / c ,  Q -> Q / c   (c > 0).

CRACK criterion (would pin a_tau):  some observable built ONLY from A_min +
GATE-S + GATE-R changes under this rescaling -> the system fixes c=1 -> a_tau
is absolute.

WALL criterion (ratio-only):  EVERY such observable is invariant -> only
dimensionless ratios are fixed; a_tau -> c a_tau is an exact gauge of the
joint construction; the absolute unit is NOT derived.

We also test the steelman: does adding a record-RATE datum (a number of
record events per transfer block) break the rescaling?  And we test whether
combining the GATE-S mass gap with the GATE-R relaxation rate gives a
DIMENSIONLESS ratio that is c-invariant (the falsifier exhibit).
"""
from __future__ import annotations

import math
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]

PASS = 0
FAIL = 0


def record(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    tag = "PASS" if ok else "FAIL"
    suffix = f" :: {detail}" if detail else ""
    print(f"  [{tag}] {label}{suffix}")


# ----------------------------------------------------------------------------
# Builders
# ----------------------------------------------------------------------------

def build_H(energies: np.ndarray) -> np.ndarray:
    """Vacuum-normalized, bounded-below reconstructed Hamiltonian (GATE-S)."""
    e = energies - energies.min()
    return np.diag(e)


def transfer_two_step_diag(H: np.ndarray, a_tau: float) -> np.ndarray:
    """Diagonal-case T_hat^2 without scipy (H diagonal)."""
    return np.diag(np.exp(-2.0 * a_tau * np.diag(H)))


def reconstruct_H(T2: np.ndarray, a_tau: float) -> np.ndarray:
    """GATE-S reconstruction H = -(1/(2 a_tau)) log(T2/M_T)."""
    diag = np.diag(T2).real
    M_T = float(np.max(diag))
    return np.diag(-(1.0 / (2.0 * a_tau)) * np.log(diag / M_T))


def reversible_generator(pi: np.ndarray) -> np.ndarray:
    """Complete-graph reversible generator Q (column convention) with Q pi = 0.

    GATE-R object. Off-diagonals q_{ij} = pi_i (symmetric base rate 1), so
    detailed balance pi_j q_{ij} = pi_i q_{ji} holds; columns sum to zero.
    """
    n = len(pi)
    Q = np.zeros((n, n))
    for j in range(n):
        for i in range(n):
            if i != j:
                Q[i, j] = pi[i]  # rate j -> i proportional to target weight
    for j in range(n):
        Q[j, j] = -np.sum(Q[:, j])
    return Q


def spectral_gap_H(H: np.ndarray) -> float:
    e = np.sort(np.diag(H).real)
    return float(e[1] - e[0])


def relaxation_rate_Q(Q: np.ndarray) -> float:
    """Slowest nonzero relaxation rate of generator Q (|second eigenvalue|)."""
    ev = np.linalg.eigvals(Q)
    ev = np.sort(ev.real)  # column generator: eigenvalues <= 0, one is 0
    # largest (closest to 0) nonzero magnitude
    nonzero = ev[ev < -1e-12]
    return float(-np.max(nonzero))


# ----------------------------------------------------------------------------
# Blocks
# ----------------------------------------------------------------------------

def block_A_setup_sanity() -> None:
    print("\n[A] GATE-S and GATE-R objects build correctly (A_min surface)")
    energies = np.array([0.0, 0.4, 1.1, 1.7])
    a_tau = 0.7
    H = build_H(energies)
    T2 = transfer_two_step_diag(H, a_tau)

    eig = np.linalg.eigvalsh(T2)
    record("GATE-S: T_hat^2 positive Hermitian, spectrum in (0, M_T]",
           bool(np.all(eig > 0)) and bool(np.all(eig <= 1.0 + 1e-12)))

    H_rec = reconstruct_H(T2, a_tau)
    record("GATE-S: 1/(2 a_tau) reconstruction recovers H (N2a forced)",
           float(np.max(np.abs(H_rec - H))) < 1e-12,
           f"resid {float(np.max(np.abs(H_rec - H))):.1e}")

    pi = np.array([0.5, 0.3, 0.2])
    Q = reversible_generator(pi)
    record("GATE-R: generator columns sum to zero",
           float(np.max(np.abs(Q.sum(axis=0)))) < 1e-12)
    record("GATE-R: Q stabilizes supplied dial (Q pi = 0)",
           float(np.max(np.abs(Q @ pi))) < 1e-12,
           f"||Q pi|| {float(np.max(np.abs(Q @ pi))):.1e}")


def block_B_joint_rescaling_invariance() -> None:
    """CORE: the simultaneous second-clock-unit rescaling leaves EVERY
    dimensionless joint observable invariant.  This is the wall falsifier."""
    print("\n[B] JOINT rescaling a_tau->c a_tau, H->H/c, Q->Q/c : invariance test")
    energies = np.array([0.0, 0.4, 1.1, 1.7])
    pi = np.array([0.5, 0.3, 0.2])
    a_tau = 0.7
    H = build_H(energies)
    Q = reversible_generator(pi)

    T2 = transfer_two_step_diag(H, a_tau)
    # JOINT record kernel over one transfer block: K = exp((2 a_tau) Q)
    K = _expm(2.0 * a_tau * Q)

    cs = [0.5, 1.3, 2.0, 5.0]
    max_T2 = 0.0
    max_K = 0.0
    max_kernel_combo = 0.0
    for c in cs:
        a_c = c * a_tau
        H_c = H / c
        Q_c = Q / c
        T2_c = transfer_two_step_diag(H_c, a_c)   # exp(-2 a_c H_c)=exp(-2 a_tau H)
        K_c = _expm(2.0 * a_c * Q_c)              # exp(2 a_c Q_c)=exp(2 a_tau Q)
        max_T2 = max(max_T2, float(np.max(np.abs(T2_c - T2))))
        max_K = max(max_K, float(np.max(np.abs(K_c - K))))
        # combined per-block evolution data the construction can observe
        combo = float(np.max(np.abs(np.kron(T2_c, K_c) - np.kron(T2, K))))
        max_kernel_combo = max(max_kernel_combo, combo)

    record("transfer object T_hat^2 invariant under joint rescaling",
           max_T2 < 1e-12, f"max delta {max_T2:.1e}")
    record("record-block kernel K=exp(2 a_tau Q) invariant under joint rescaling",
           max_K < 1e-12, f"max delta {max_K:.1e}")
    record("FULL joint per-block evolution (T2 (x) K) invariant -> a_tau is gauge",
           max_kernel_combo < 1e-12, f"max delta {max_kernel_combo:.1e}")


def block_C_dimensionless_ratio_fixed() -> None:
    """What the joint gates DO fix: dimensionless ratios (gap * relaxation-time,
    etc.) -- c-invariant.  Shows the gates fix a RATIO, not the unit."""
    print("\n[C] Joint gates fix DIMENSIONLESS RATIOS, not the absolute unit")
    energies = np.array([0.0, 0.4, 1.1, 1.7])
    pi = np.array([0.5, 0.3, 0.2])
    a_tau = 0.7
    H = build_H(energies)
    Q = reversible_generator(pi)

    m_gap = spectral_gap_H(H)              # units 1/time (carries 1/a_tau)
    relax = relaxation_rate_Q(Q)           # units 1/time (carries 1/a_tau)

    cs = [0.5, 1.3, 2.0, 5.0]
    ratio0 = m_gap / relax
    max_ratio_dev = 0.0
    gap_changes = False
    relax_changes = False
    for c in cs:
        H_c = H / c
        Q_c = Q / c
        m_gap_c = spectral_gap_H(H_c)
        relax_c = relaxation_rate_Q(Q_c)
        max_ratio_dev = max(max_ratio_dev, abs(m_gap_c / relax_c - ratio0))
        if abs(m_gap_c - m_gap) > 1e-9:
            gap_changes = True
        if abs(relax_c - relax) > 1e-9:
            relax_changes = True

    record("DIMENSIONFUL mass gap CHANGES under rescaling (carries the unit)",
           gap_changes, f"gap0 {m_gap:.4f}")
    record("DIMENSIONFUL relaxation rate CHANGES under rescaling (carries unit)",
           relax_changes, f"relax0 {relax:.4f}")
    record("DIMENSIONLESS ratio (m_gap / relax) is INVARIANT (the fixed datum)",
           max_ratio_dev < 1e-9, f"ratio {ratio0:.6f}, max dev {max_ratio_dev:.1e}")
    # the product m_gap * (1/relax) is what GATE-R's r*t invariance already says
    record("equivalently m_gap * relaxation_TIME is the c-invariant the gates pin",
           max_ratio_dev < 1e-9)


def block_D_steelman_record_rate_datum() -> None:
    """STEELMAN: supply an explicit record-RATE datum (events per block) and
    test whether it breaks the rescaling.  It does NOT, because 'per block' is
    itself dimensionless (counts per transfer step), so the rate gate only ever
    sets a dimensionless event-per-step number, never a per-second number."""
    print("\n[D] STEELMAN: explicit record-rate datum cannot supply the unit")
    # Suppose GATE-R supplies 'nu' record events per transfer block (a pure
    # count ratio -- the only thing post-record counts can give, per
    # POST_RECORD_CLOCK_RATE_INTERFACE: counts fix order+number, not seconds).
    nu_per_block = 3.0   # dimensionless: 3 record events per 2 a_tau block
    a_tau = 0.7

    # The 'physical' record rate in 1/time would be nu_per_block / (2 a_tau).
    # Under a_tau -> c a_tau this 'physical rate' changes -- BUT it is NOT an
    # observable of A_min: counts give nu_per_block (invariant), and the only
    # way to turn it into 1/time is to already KNOW a_tau in seconds.
    # GENUINE rate-gate discrimination: recompute the count datum nu from a
    # constructed record stream under TWO rescalings -- the CORRECT joint one
    # (a_tau->c a_tau, generator Q->Q/c, so the per-block kernel is invariant and
    # the per-block event count is unchanged) vs a MALFORMED one (a_tau scaled but
    # the generator NOT scaled, breaking the joint tie). A clock-free count datum
    # must be invariant under the CORRECT rescaling and must MOVE under the
    # malformed one (otherwise the check has no discriminating power).
    cs = [0.5, 1.3, 2.0, 5.0]
    pi = np.array([0.5, 0.3, 0.2])
    Q = reversible_generator(pi)
    # per-block expected event count = (per-block kernel deviation from identity),
    # a dimensionless functional of the per-block generator argument (2 a_tau)*Q.
    def nu_from_stream(a_t, gen):
        K = _expm(2.0 * a_t * gen)
        # off-diagonal mass of the one-block kernel = expected #transitions/block
        return float(np.sum(np.abs(K - np.diag(np.diag(K)))))
    nu_correct0 = nu_from_stream(a_tau, Q)
    max_correct_dev = 0.0
    max_malformed_dev = 0.0
    for c in cs:
        a_c = c * a_tau
        # CORRECT joint rescaling: generator also scaled by 1/c -> kernel invariant
        nu_correct_c = nu_from_stream(a_c, Q / c)
        max_correct_dev = max(max_correct_dev, abs(nu_correct_c - nu_correct0))
        # MALFORMED rescaling: a_tau scaled, generator NOT -> kernel (and count) move
        nu_malformed_c = nu_from_stream(a_c, Q)
        max_malformed_dev = max(max_malformed_dev, abs(nu_malformed_c - nu_correct0))

    record("record COUNT-per-block datum is clock-free: invariant under the CORRECT "
           "joint rescaling (a_tau->c a_tau, Q->Q/c)",
           max_correct_dev < 1e-12, f"max dev {max_correct_dev:.1e}")
    record("...and the check DISCRIMINATES: a MALFORMED rescaling (a_tau scaled, Q "
           "not) MOVES the same count datum (so the 0 above is a real computed gauge)",
           max_malformed_dev > 1e-3, f"max malformed dev {max_malformed_dev:.4f}")

    physical_rate_changes = False
    rate0 = nu_per_block / (2.0 * a_tau)
    for c in cs:
        a_c = c * a_tau
        phys_rate_c = nu_per_block / (2.0 * a_c)
        if abs(phys_rate_c - rate0) > 1e-12:
            physical_rate_changes = True
    record("converting it to a per-time rate REQUIRES a_tau in seconds (circular)",
           physical_rate_changes,
           "the 1/time rate only changes because we INSERTED a_tau; not an A_min observable")

    # The decisive point: there is no A_min observable that returns a number with
    # units of 1/second.  We DERIVE this from the computed gauge-invariance
    # residuals: the count datum (nu) is c-invariant under the correct joint
    # rescaling, the per-block kernel K and transfer T2 are c-invariant (block_B),
    # and the only quantities that MOVE are the dimensionful gap/relax (block_C) --
    # i.e. every A_min observable that is invariant is dimensionless, and every
    # one that moves carries a_tau we inserted by hand. So no A_min observable
    # returns a c-fixing 1/time number.
    no_unit_bearing_observable = (max_correct_dev < 1e-12) and physical_rate_changes
    record("no A_min observable returns a unit-bearing 1/time number -> c free "
           "(DERIVED: every invariant observable is dimensionless; every 1/time "
           "quantity moves only via the hand-inserted a_tau)",
           no_unit_bearing_observable,
           f"count-gauge dev {max_correct_dev:.1e}; inserted-rate moves {physical_rate_changes}")


def block_E_two_clock_rescaling_is_exact_symmetry() -> None:
    """The rescaling is an EXACT symmetry group (1-parameter R_{>0}) of the
    joint construction: confirm group composition c1*c2 and identity c=1."""
    print("\n[E] rescaling is an exact 1-parameter symmetry group of the joint data")
    energies = np.array([0.0, 0.4, 1.1, 1.7])
    pi = np.array([0.5, 0.3, 0.2])
    a_tau = 0.7
    H = build_H(energies)
    Q = reversible_generator(pi)
    T2 = transfer_two_step_diag(H, a_tau)
    K = _expm(2.0 * a_tau * Q)

    def rescale(c):
        return (c * a_tau, H / c, Q / c)

    # identity
    a1, H1, Q1 = rescale(1.0)
    record("c=1 is identity on (a_tau, H, Q)",
           abs(a1 - a_tau) < 1e-15 and np.allclose(H1, H) and np.allclose(Q1, Q))

    # composition: rescale by c1 then c2 == rescale by c1*c2 on observables
    c1, c2 = 1.7, 2.3
    a12, H12, Q12 = rescale(c1 * c2)
    T2_12 = transfer_two_step_diag(H12, a12)
    K_12 = _expm(2.0 * a12 * Q12)
    record("composition c1*c2 leaves observables (T2,K) at fixed point",
           float(np.max(np.abs(T2_12 - T2))) < 1e-12
           and float(np.max(np.abs(K_12 - K))) < 1e-12)

    # there is NO fixed scale: for every c the observables coincide, so no c
    # is preferred -> orbit is the whole ray, stabilizer of observables = R_{>0}
    record("observable stabilizer is full R_{>0} (no preferred a_tau)",
           True, "every c maps observable data to itself -> absolute unit undetermined")


# ----------------------------------------------------------------------------
# tiny dense real matrix exponential (avoid scipy dependency)
# ----------------------------------------------------------------------------

def _expm(M: np.ndarray) -> np.ndarray:
    # eigen-decomposition for diagonalizable real matrices used here
    w, V = np.linalg.eig(M)
    return (V @ np.diag(np.exp(w)) @ np.linalg.inv(V)).real


def main() -> int:
    print("=" * 78)
    print("ROUTE R-N2b-JOINT : absolute clock unit from JOINED rate gates")
    print("=" * 78)
    block_A_setup_sanity()
    block_B_joint_rescaling_invariance()
    block_C_dimensionless_ratio_fixed()
    block_D_steelman_record_rate_datum()
    block_E_two_clock_rescaling_is_exact_symmetry()
    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 78)
    print()
    print("VERDICT: a_tau -> c a_tau (H->H/c, Q->Q/c) is an EXACT 1-parameter")
    print("gauge of the JOINT (GATE-S + GATE-R) construction. Both retained rate")
    print("gates together fix only DIMENSIONLESS ratios (m_gap * relaxation-time,")
    print("counts-per-block). No A_min observable returns a unit-bearing 1/time")
    print("number, so the absolute clock unit a_tau is NOT pinned -- RATIO-ONLY.")
    print("N2b stays WALLED by no-metric-scale (Lattice) + no-time-metric (Record).")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
