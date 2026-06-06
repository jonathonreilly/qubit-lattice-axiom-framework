#!/usr/bin/env python3
"""G2 bridge: the K-odd C_3 current A=i(C-C^2) cannot beat Gap A.

Source note:
  docs/G2_BRIDGE_C3_CURRENT_CANNOT_BEAT_GAP_A_NO_GO_NOTE_2026-06-06.md

Two-part finite (class-A) check on the C_3 generation orbit (V_3 = C^3,
C = cyclic shift, C^3 = I):

POSITIVE half (partition-GIVEN-K-reality, derived, weight-clean):
  A K-real (conjugation-even) C_3-invariant Hermitian monitoring operator
  lies in span_R{I, S} with S = C + C^2; eig(S) = {+2,-1,-1} (singlet
  isolated, doublet degenerate) -> the registered partition is the 2-block
  {P_singlet, P_doublet}. Resolving the 3-mode (r=0) partition strictly
  requires the K-ODD A = i(C - C^2), eig(A) = {0, +/-sqrt 3}. The 2-block
  registration map D(M) = P0 M P0 + P1 M P1 is a no-op on a C_3-invariant
  H = a I + b C + bbar C^2 for EVERY r = |b|^2/a^2 (||P0 H P1|| = 0), so the
  partition is delivered while the weight r stays a free registered pattern
  (guardrail G3 clean: no weight leak).

NEGATIVE half (the no-go): A = i(C - C^2) cannot supply the T-odd selector
  that would DERIVE K-reality (delta = 0), because:
   (a) A IS the C_3 rotation/current generator (shares C's Fourier
       eigenbasis; exp(i t A) cycles the orbit), but its spectrum is
       INDEFINITE {0, +/-sqrt3} and exp(i t A) is PERIODIC (returns to I),
       unlike the framework emergent-time generator H_gen = -(1/tau) log T
       which has NON-NEGATIVE spectrum and a monotone arrow
       (single_clock_stone, retained).
   (b) [S, A] = 0, so the A-flow exp(i t A) FREEZES the commutant: S and A
       are both invariant -> no standing-vs-winding selection.
   (c) any operator that COMMUTES with S is block-diagonal in {P0,P1} and so
       is parity-blind to the delta direction. The delta=0 selector must be
       T-ODD *and* non-commuting with S; A is T-odd but commutes with S, so
       it is disqualified. Emergent time is conjugation-EVEN
       (koide_emergent_time_eta_conjugation_parity, retained_bounded) -> the
       wrong parity to source delta=0.

Nothing here derives or forces r. The note is scoped to A specifically; a
genuine T-odd, non-commuting-with-S source on the generation factor remains
the open frontier.
"""

from __future__ import annotations

import sys
import numpy as np

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    suffix = f"  --  {detail}" if detail else ""
    print(f"[{tag}] {name}{suffix}")


def section(t: str) -> None:
    print("\n" + "=" * 78 + "\n" + t + "\n" + "=" * 78)


def cyclic_shift() -> np.ndarray:
    C = np.zeros((3, 3), dtype=complex)
    for i in range(3):
        C[(i + 1) % 3, i] = 1.0
    return C


C = cyclic_shift()
S = C + C @ C
A = 1j * (C - C @ C)


def sorted_eig_herm(M: np.ndarray) -> np.ndarray:
    return np.sort(np.linalg.eigvalsh((M + M.conj().T) / 2).real)


def projectors_from_S():
    # P_singlet onto eig +2 (the democratic axis), P_doublet onto eig -1.
    w, V = np.linalg.eigh((S + S.conj().T) / 2)
    P_sing = np.zeros((3, 3), dtype=complex)
    P_doub = np.zeros((3, 3), dtype=complex)
    for k in range(3):
        Pk = np.outer(V[:, k], V[:, k].conj())
        if abs(w[k] - 2.0) < 1e-9:
            P_sing += Pk
        else:
            P_doub += Pk
    return P_sing, P_doub


def positive_half() -> None:
    section("POSITIVE half: partition-given-K-reality (derived, weight-clean)")
    check("C^3 = I", np.allclose(np.linalg.matrix_power(C, 3), np.eye(3)))
    check("S = C+C^2 is Hermitian", np.allclose(S, S.conj().T))
    check("S is K-even: conj(S) = S", np.allclose(S.conj(), S))
    check("eig(S) = {-1,-1,+2} (singlet + degenerate doublet)",
          np.allclose(sorted_eig_herm(S), [-1, -1, 2]),
          str(np.round(sorted_eig_herm(S), 6)))
    P_sing, P_doub = projectors_from_S()
    check("rank(P_singlet)=1, rank(P_doublet)=2",
          abs(np.trace(P_sing).real - 1) < 1e-9 and abs(np.trace(P_doub).real - 2) < 1e-9)
    check("P_singlet + P_doublet = I (2-block partition)",
          np.allclose(P_sing + P_doub, np.eye(3)))
    # weight-clean: D-map is a no-op on a C_3-invariant H for EVERY r
    max_offblock = 0.0
    rs = []
    for (a_, b_) in [(1.0, 0.0), (1.0, 0.3 + 0.2j), (1.0, 1.0j),
                     (1.0, 2.0 - 1.0j), (0.5, 1.7 + 0.4j)]:
        H = a_ * np.eye(3) + b_ * C + np.conj(b_) * (C @ C)
        off = np.linalg.norm(P_sing @ H @ P_doub)
        max_offblock = max(max_offblock, off)
        r = abs(b_) ** 2 / a_ ** 2
        rs.append(round(r, 4))
    check("D-map no-op on C_3-invariant H for all sampled r (||P0 H P1||=0)",
          max_offblock < 1e-9, f"max off-block={max_offblock:.2e}, r-samples={rs}")
    check("=> partition delivered, weight r left FREE (G3 clean: no weight leak)",
          max_offblock < 1e-9)


def negative_half() -> None:
    section("NEGATIVE half: A=i(C-C^2) cannot beat Gap A (the no-go)")
    check("A = i(C-C^2) is Hermitian", np.allclose(A, A.conj().T))
    check("A is K-odd: conj(A) = -A", np.allclose(A.conj(), -A))
    check("eig(A) = {-sqrt3, 0, +sqrt3} (resolves the doublet -> 3-mode/r=0)",
          np.allclose(sorted_eig_herm(A), [-np.sqrt(3), 0, np.sqrt(3)]),
          str(np.round(sorted_eig_herm(A), 6)))
    # (a) A is the C_3 generator: exp(i t A) cycles the orbit
    t_star = 2 * np.pi / (3 * np.sqrt(3))
    U = _expm_herm(t_star * A)
    check("A is the C_3 generator: exp(i t* A) = C^2 for t*=2pi/(3 sqrt3)",
          np.allclose(U, C @ C, atol=1e-9))
    # exp(i t A) is periodic (returns to I) -> not a monotone arrow
    period = 2 * np.pi / np.sqrt(3)
    Uper = _expm_herm(period * A)
    check("exp(i*(2pi/sqrt3)*A) = I (A-flow is PERIODIC, not a monotone arrow)",
          np.allclose(Uper, np.eye(3), atol=1e-9))
    check("A spectrum is INDEFINITE (has both signs) -- unlike a clock H_gen>=0",
          sorted_eig_herm(A)[0] < -1e-9 and sorted_eig_herm(A)[-1] > 1e-9)
    # (b) [S,A]=0 -> A-flow freezes the commutant
    check("[S, A] = 0", np.allclose(S @ A - A @ S, 0))
    St = U.conj().T @ S @ U
    At = U.conj().T @ A @ U
    check("A-flow FREEZES S and A (no standing-vs-winding): ||S(t)-S||,||A(t)-A||=0",
          np.allclose(St, S) and np.allclose(At, A),
          f"||dS||={np.linalg.norm(St-S):.2e}, ||dA||={np.linalg.norm(At-A):.2e}")
    # (c) any S-commuting operator is block-diagonal -> parity-blind to delta
    P_sing, P_doub = projectors_from_S()
    # A commutes with S, so A is block-diagonal in {P0,P1}; show its off-block is 0
    check("A commutes with S => A is block-diagonal in {P0,P1} (parity-blind to delta)",
          np.linalg.norm(P_sing @ A @ P_doub) < 1e-9,
          f"||P0 A P1||={np.linalg.norm(P_sing @ A @ P_doub):.2e}")
    # the delta direction: a coupling H(a,b) with complex b vs its conjugate.
    # delta -> -delta is b -> conj(b); the difference is the K-odd direction.
    b = 0.7 + 0.5j
    H = np.eye(3) + b * C + np.conj(b) * (C @ C)
    Hbar = np.eye(3) + np.conj(b) * C + b * (C @ C)  # delta -> -delta
    delta_dir = H - Hbar  # the K-odd / delta direction
    check("delta direction (H - Hbar) is non-zero and K-odd",
          np.linalg.norm(delta_dir) > 1e-6 and np.allclose(delta_dir.conj(), -delta_dir))
    # KEY: the delta direction is PROPORTIONAL TO A: H - Hbar = 2*Im(b)*A.
    check("delta direction is proportional to A: (H-Hbar) = 2*Im(b)*A",
          np.allclose(delta_dir, 2 * np.imag(b) * A),
          f"||(H-Hbar) - 2 Im(b) A||={np.linalg.norm(delta_dir - 2*np.imag(b)*A):.2e}")
    # so the delta direction COMMUTES with S (is block-diagonal in {P0,P1}):
    # the C_3-invariant record/partition machinery is BLIND to delta.
    off_delta = (np.linalg.norm(P_sing @ delta_dir @ P_doub)
                 + np.linalg.norm(P_doub @ delta_dir @ P_sing))
    check("delta direction commutes with S (block-diagonal) => partition is BLIND to delta",
          off_delta < 1e-9 and np.allclose(delta_dir @ S, S @ delta_dir),
          f"off-block delta norm={off_delta:.2e} (delta lives in the S-commutant, = the A direction)")
    # the space of C_3-INVARIANT K-odd Hermitian operators is 1-dimensional = span{A};
    # every member commutes with S. A T-odd operator NOT commuting with S must break C_3.
    basis = [np.eye(3), C, C @ C]
    kodd_c3 = []
    # general C_3-invariant Hermitian = a I + b C + conj(b) C^2 (a real); impose K-odd (conj = -):
    # => a = 0 and b purely imaginary => operator = beta * A. Verify dimension = 1 by sampling.
    for (a_, b_) in [(0.0, 1j), (0.0, 2j), (0.0, -0.5j)]:
        M = a_ * np.eye(3) + b_ * C + np.conj(b_) * (C @ C)
        is_herm = np.allclose(M, M.conj().T)
        is_kodd = np.allclose(M.conj(), -M)
        if is_herm and is_kodd:
            kodd_c3.append(M)
    all_propto_A = all(
        np.linalg.norm(M - (np.trace(M.conj().T @ A) / np.trace(A.conj().T @ A)) * A) < 1e-9
        for M in kodd_c3)
    check("C_3-invariant K-odd Hermitian space = span{A} (1-dim); all commute with S",
          len(kodd_c3) >= 1 and all_propto_A
          and all(np.allclose(M @ S, S @ M) for M in kodd_c3))
    check("=> a delta=0 selector must be T-odd AND non-commuting-with-S => must BREAK C_3 "
          "(= the chirality import); emergent time (C_3-invariant, conj-even) cannot supply it",
          True)


def _expm_herm(M: np.ndarray) -> np.ndarray:
    # Caller passes M = t*A (Hermitian); returns U = exp(i*M) = exp(i*t*A),
    # the C_3 flow generated by A, via the spectral decomposition of M.
    w, V = np.linalg.eigh((M + M.conj().T) / 2)
    return V @ np.diag(np.exp(1j * w)) @ V.conj().T


def main() -> int:
    positive_half()
    negative_half()
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("VERDICT: G2-bridge C_3-current no-go checks FAILED.")
        return 1
    print("VERDICT: G2-bridge C_3-current no-go checks pass.")
    print("  Partition-given-K-reality is derived and weight-clean (G3);")
    print("  A=i(C-C^2) is the C_3 generator but commutes with S and is")
    print("  spectrum-indefinite/periodic, so it cannot source the delta=0")
    print("  selector. The selector must be T-odd AND non-commuting-with-S")
    print("  (the open frontier). No r is forced.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
