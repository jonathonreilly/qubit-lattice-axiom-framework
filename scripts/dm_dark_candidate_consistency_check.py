#!/usr/bin/env python3
"""Dark-candidate consistency check for the DM lane: taste-cube census and N1 lifetime.

Evidence for the 2026-09-30 corrigendum on the DM candidate.

The April DM chain (3594 clean derivation, Steps 2-3) calls the two taste states
S_0 = |000> and S_3 = |111> "gauge singlets" and the dark matter candidates.
The May-06 mass step (DM_ETA_G1_COLEMAN_WEINBERG_BOUNDED_THEOREM_NOTE_2026-05-06,
via CL3_COLOR_AUTOMORPHISM_THEOREM Sections B, F, H) instead puts the dark
state |111> in the base x fibre embedding, where it is a colour fundamental with
C_F = 4/3 and Y = +1/3: the factor 8/3 = 2 C_F needs C_F = 4/3, not 0.  A third
candidate, the lightest right-handed neutrino N1, is called "the framework's DM
candidate" in DM_LEPTON_SYNTHESIS_NOTE_2026-04-19.

Parts 1-4 build the base x fibre embedding from its definition and list the
joint quantum numbers of all eight states:

    C^8 = (C^2)^{x3},  base = (b1, b2),  fibre = b3.
    SU(3)_c : Gell-Mann/2 on the 3-dim symmetric base subspace
              {|00>, (|01>+|10>)/sqrt2, |11>}, zero on the antisymmetric
              state (|01>-|10>)/sqrt2, tensor identity on the fibre.
    SU(2)_L : identity on the base tensor sigma/2 on the fibre.
    Y       : (1/3) P_sym - 1 * P_antisym on the base, identity on the fibre.

Part 5 evaluates N1's decay rate from the note's own washout parameter.

Scope.  Parts 1-4 hold inside the base x fibre embedding, which is itself a
bounded, unaudited input (CL3_COLOR_AUTOMORPHISM_THEOREM says identifying the
base with physical colour is a separate bridge).  They are not a derivation
that the framework must use this embedding, and they say nothing about states
outside the eight-state cube.  Part 5 is arithmetic on the note's supplied
inputs.  Same-family check by its author, not an independent referee.
"""

from __future__ import annotations

# Explicit bounded execution cap; scientific content is unchanged by this metadata.
AUDIT_TIMEOUT_SEC = 120

import itertools
import sys

import numpy as np

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def gell_mann() -> list[np.ndarray]:
    l = np.zeros((8, 3, 3), dtype=complex)
    l[0] = [[0, 1, 0], [1, 0, 0], [0, 0, 0]]
    l[1] = [[0, -1j, 0], [1j, 0, 0], [0, 0, 0]]
    l[2] = [[1, 0, 0], [0, -1, 0], [0, 0, 0]]
    l[3] = [[0, 0, 1], [0, 0, 0], [1, 0, 0]]
    l[4] = [[0, 0, -1j], [0, 0, 0], [1j, 0, 0]]
    l[5] = [[0, 0, 0], [0, 0, 1], [0, 1, 0]]
    l[6] = [[0, 0, 0], [0, 0, -1j], [0, 1j, 0]]
    l[7] = np.diag([1.0, 1.0, -2.0]) / np.sqrt(3.0)
    return [m for m in l]


def build_embedding() -> dict:
    """Operators on C^8 in the ordering |b1 b2 b3>, index 4 b1 + 2 b2 + b3."""
    ket = {(b1, b2): np.eye(4)[2 * b1 + b2] for b1 in (0, 1) for b2 in (0, 1)}
    e1 = ket[(0, 0)]
    e2 = (ket[(0, 1)] + ket[(1, 0)]) / np.sqrt(2.0)
    e3 = ket[(1, 1)]
    anti = (ket[(0, 1)] - ket[(1, 0)]) / np.sqrt(2.0)
    sym_basis = np.stack([e1, e2, e3], axis=1)  # 4 x 3
    p_sym = sym_basis @ sym_basis.conj().T
    p_anti = np.outer(anti, anti.conj())
    ident2 = np.eye(2)

    t_ops = []
    for lam in gell_mann():
        base_op = sym_basis @ (lam / 2.0) @ sym_basis.conj().T
        t_ops.append(np.kron(base_op, ident2))

    sx = np.array([[0, 1], [1, 0]], dtype=complex) / 2.0
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex) / 2.0
    sz = np.array([[1, 0], [0, -1]], dtype=complex) / 2.0
    j_ops = [np.kron(np.eye(4), s) for s in (sx, sy, sz)]
    y_op = np.kron(p_sym / 3.0 - p_anti, ident2)
    return {"T": t_ops, "J": j_ops, "Y": y_op}


def comm(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.abs(a @ b - b @ a).max())


def main() -> int:
    print("=" * 88)
    print("DM DARK-CANDIDATE CONSISTENCY: TASTE-CUBE CENSUS AND N1 LIFETIME")
    print("=" * 88)
    print("Same-family check by its author; the embedding is a bounded, unaudited input.")

    emb = build_embedding()
    t_ops, j_ops, y_op = emb["T"], emb["J"], emb["Y"]
    c3 = sum(t @ t for t in t_ops)
    c2 = sum(j @ j for j in j_ops)

    print("\n" + "=" * 88)
    print("PART 1: THE EMBEDDING IS A CONSISTENT SU(3) x SU(2) x U(1) ACTION")
    print("=" * 88)
    check(
        "SU(3) generators commute with SU(2) generators and with Y",
        max(comm(t, j) for t in t_ops for j in j_ops) < 1.0e-12 and max(comm(t, y_op) for t in t_ops) < 1.0e-12,
        "tensor-product structure",
    )
    check(
        "SU(2) generators commute with Y",
        max(comm(j, y_op) for j in j_ops) < 1.0e-12,
    )
    check(
        "SU(3) generators are normalised Tr(T^a T^b) = (1/2) delta^{ab} on the triplet block",
        all(
            abs(np.trace(t_ops[a] @ t_ops[b]) - (1.0 if a == b else 0.0)) < 1.0e-12
            for a in range(8)
            for b in range(8)
        ),
        "trace over C^8 = 2 x (1/2) delta: the fibre doubles the trace",
    )
    check("Y is traceless on C^8", abs(np.trace(y_op)) < 1.0e-12, f"Tr Y = {np.trace(y_op).real:.2e}")

    print("\n" + "=" * 88)
    print("PART 2: JOINT SPECTRUM (C_F, j(j+1), Y) OF THE EIGHT STATES")
    print("=" * 88)
    # Simultaneous diagonalisation: Y, C3, C2 mutually commute.
    combo = c3 + 0.37 * c2 + 0.11 * y_op
    w, v = np.linalg.eigh(combo)
    triples = []
    for k in range(8):
        vec = v[:, k]
        triples.append(
            (
                round(float((vec.conj() @ c3 @ vec).real), 6) + 0.0,
                round(float((vec.conj() @ c2 @ vec).real), 6) + 0.0,
                round(float((vec.conj() @ y_op @ vec).real), 6) + 0.0,
            )
        )
    census: dict[tuple, int] = {}
    for t in triples:
        census[t] = census.get(t, 0) + 1
    for t, n in sorted(census.items()):
        print(f"  {n} state(s) with (C_F, j(j+1), Y) = {t}")
    expected = {(1.333333, 0.75, 0.333333): 6, (0.0, 0.75, -1.0): 2}
    check(
        "Census is 6 x (3,2)_{+1/3} plus 2 x (1,2)_{-1}",
        census == expected,
        f"{census}",
    )

    print("\n" + "=" * 88)
    print("PART 3: IS ANY TASTE STATE A GAUGE SINGLET?")
    print("=" * 88)
    w_gauge = np.linalg.eigvalsh(c3 + c2)
    check(
        "Smallest eigenvalue of C_3 + C_2 on C^8 is 0.75, so no state has C_3 = C_2 = 0",
        abs(w_gauge.min() - 0.75) < 1.0e-12,
        f"min eigenvalue {w_gauge.min():.6f}",
    )
    stack = np.concatenate([np.stack(t_ops + j_ops).reshape(11 * 8, 8)], axis=0)
    rank = np.linalg.matrix_rank(stack, tol=1.0e-10)
    check(
        "No vector is annihilated by all SU(3) and SU(2) generators: joint null space is empty",
        rank == 8,
        f"rank of stacked generators = {rank} of 8",
    )
    check(
        "No state is Y-neutral either: Y takes only the values +1/3 and -1",
        all(min(abs(y - 1.0 / 3.0), abs(y + 1.0)) < 1.0e-9 for y in np.linalg.eigvalsh(y_op)),
        f"Y eigenvalues {np.round(np.linalg.eigvalsh(y_op), 6).tolist()}",
    )

    print("\n" + "=" * 88)
    print("PART 4: THE APRIL 'DARK' STATES S_0 = |000> AND S_3 = |111>")
    print("=" * 88)
    labels = ["".join(map(str, b)) for b in itertools.product([0, 1], repeat=3)]
    for lab in ("000", "111"):
        i = labels.index(lab)
        e = np.zeros(8, dtype=complex)
        e[i] = 1.0
        c3v = float((e.conj() @ c3 @ e).real)
        c2v = float((e.conj() @ c2 @ e).real)
        yv = float((e.conj() @ y_op @ e).real)
        tmax = max(float(np.linalg.norm(t @ e)) for t in t_ops)
        print(f"  |{lab}>: <C_F> = {c3v:.4f}, <j(j+1)> = {c2v:.4f}, <Y> = {yv:+.4f}, max_a |T^a|{lab}>| = {tmax:.4f}")
        check(
            f"|{lab}> is a colour fundamental doublet component with Y = +1/3, not a gauge singlet",
            abs(c3v - 4.0 / 3.0) < 1.0e-12 and abs(c2v - 0.75) < 1.0e-12 and abs(yv - 1.0 / 3.0) < 1.0e-12 and tmax > 0.4,
            f"(C_F, j(j+1), Y) = ({c3v:.4f}, {c2v:.4f}, {yv:+.4f})",
        )

    print("\n" + "=" * 88)
    print("PART 5: THE 'DM CANDIDATE' N1 (LIGHTEST RIGHT-HANDED NEUTRINO)")
    print("=" * 88)
    # Inputs supplied by DM_CANDIDATE_MASS_WINDOW_THEOREM_NOTE_2026-04-19 (M1, k_decay).
    m1 = 5.323e10  # GeV, lightest right-handed neutrino mass
    k_decay = 47.24  # washout parameter K = Gamma_D / H(T = M1) = m_tilde / m_star
    g_star = 106.75
    m_planck = 1.2209e19  # GeV
    hbar_gev_s = 6.582119569e-25  # GeV s
    age_universe_s = 4.35e17
    hubble = 1.66 * np.sqrt(g_star) * m1 * m1 / m_planck
    gamma = k_decay * hubble
    tau = hbar_gev_s / gamma
    print(f"  H(T=M1) = {hubble:.3e} GeV, Gamma_N1 = K H = {gamma:.3e} GeV, tau_N1 = {tau:.2e} s")
    check(
        "By the note's own washout parameter K = 47.24, N1 decays in about 3.5e-30 s",
        3.0e-30 < tau < 4.0e-30,
        f"tau = {tau:.2e} s",
    )
    check(
        "That lifetime is more than 40 orders of magnitude below the age of the universe: N1 cannot be dark matter",
        tau < 1.0e-40 * age_universe_s,
        f"tau/t_universe = {tau / age_universe_s:.1e}",
    )

    print("\n" + "=" * 88)
    print("BOTTOM LINE")
    print("=" * 88)
    print("  In the base x fibre embedding the mass step uses, every taste state is an SU(2)")
    print("  doublet component and the smallest eigenvalue of C_3 + C_2 is 0.75, so no taste")
    print("  state is a gauge singlet.  The states |000> and |111> that the April chain calls")
    print("  gauge singlets carry the quantum numbers of a left-handed quark doublet")
    print("  component here.  'Dark = gauge-singlet taste state' therefore has no referent in")
    print("  the embedding the mass derivation needs.  This is conditional on that")
    print("  embedding; it does not decide which embedding the framework uses.  The other")
    print("  landed 'DM candidate', N1, decays in about 3.5e-30 s by the note's own washout")
    print("  parameter.  The lane's candidates are not jointly consistent: the neutral April")
    print("  states do not exist in this embedding, the 3.94 TeV state carries colour, and N1")
    print("  is not stable.")

    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 88)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
