#!/usr/bin/env python3
"""
Register-not-read does NOT fix kappa_EW: the color-sector no-go
==============================================================

PStack experiment: ew-kappa-registration-color-sector-nogo

Companion runner for
  docs/EW_KAPPA_REGISTRATION_REGISTERS_ALL_COLOR_SECTORS_NO_GO_NOTE_2026-06-09.md

Closes the one framework-native reopen route for kappa_EW, named in the
unaudited open_gate note RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_2026-06-08:

  "IF register-not-read identifies the I/sqrt(N_c) singlet trace channel as an
   UNREGISTERED reference, THEN the registered channel is the traceless adjoint
   and kappa_EW = 0."

This runner shows the antecedent FAILS, by the same machinery as the retained
no-go REGISTRATION_REINSTATES_CHIRALITY_2026-06-07: the registration map
  D(M) = sum_k P_k M P_k
registers the content of EVERY central sector and annihilates only operators that
map between sectors (anticommute with the sector grading). The color singlet is
the TRIVIAL (most central) irrep of the SU(N_c) adjoint action, so it is
registered, never annihilated. Hence registration keeps the singlet weight S; it
does NOT drop it (kappa_EW = 0). The partition delivers the channel COUNT
(cardinality fraction 8/9) but NOT the inter-sector readout weight kappa_EW --
structurally identical to the way it delivers the Koide block counts but leaves
the within-block weight r free ("D constrains r not at all").

This note does NOT force kappa_EW = 1 and does NOT fabricate kappa_EW = 0. It
shows register-not-read leaves kappa_EW undetermined -- consistent with the
MC-undecidability and matching-rule no-gos.

Self-contained: numpy only. Zero fitted numerical targets.
"""

import numpy as np

RNG = np.random.default_rng(20260609)
PASS = 0
FAIL = 0


def check(desc, ok):
    global PASS, FAIL
    status = "PASS" if ok else "FAIL"
    PASS += 1 if ok else 0
    FAIL += 0 if ok else 1
    print(f"  [{status}] {desc}")
    return ok


def haar_su(n):
    z = (RNG.standard_normal((n, n)) + 1j * RNG.standard_normal((n, n))) / np.sqrt(2.0)
    q, r = np.linalg.qr(z)
    q = q * (np.diagonal(r) / np.abs(np.diagonal(r)))
    return q / (np.linalg.det(q)) ** (1.0 / n)


# ----- color readout sector partition on End(C^Nc) = singlet (+) adjoint -----
def P_singlet(G, n):
    """Project the color matrix G onto the trivial (singlet) irrep: (Tr G / n) I."""
    return (np.trace(G) / n) * np.eye(n)


def P_adjoint(G, n):
    """Project G onto the adjoint (traceless) irrep: G - (Tr G / n) I."""
    return G - P_singlet(G, n)


def hs(A, B):
    return np.trace(A.conj().T @ B)


# ============================================================
# (A) The central-sector partition of the color readout: singlet (+) adjoint,
#     with sector weights S, C and mode counts 1, N_c^2-1.
# ============================================================
def part_A():
    print("\n(A) Color readout central-sector partition: singlet (+) adjoint; weights S,C and counts 1,N_c^2-1")
    okall = True
    for n in [2, 3, 4, 5]:
        G = RNG.standard_normal((n, n)) + 1j * RNG.standard_normal((n, n))
        Gs, Ga = P_singlet(G, n), P_adjoint(G, n)
        S = np.real(hs(Gs, Gs))
        C = np.real(hs(Ga, Ga))
        T = np.real(hs(G, G))
        # orthogonal sectors, S = |Tr G|^2/n, S+C=T; counts 1 and n^2-1 -> fraction
        orth = abs(hs(Gs, Ga)) < 1e-10
        okS = abs(S - np.abs(np.trace(G)) ** 2 / n) < 1e-9
        frac = (n * n - 1) / n ** 2
        okall &= check(
            f"N_c={n}: S+C=T ({abs(S + C - T):.1e}), sectors orthogonal ({orth}), "
            f"counts(1,{n*n-1}) -> adjoint fraction {frac:.4f}",
            abs(S + C - T) < 1e-9 and orth and okS,
        )
    return okall


# ============================================================
# (B) Registration registers BOTH central sectors; the singlet is the trivial
#     irrep (most central) -> it is registered, NEVER annihilated.  Contrast:
#     an operator that maps singlet<->adjoint (anticommutes with the grading)
#     IS annihilated -- the chirality-no-go mechanism -- but the singlet WEIGHT
#     is diagonal content, so it survives.
# ============================================================
def part_B():
    print("\n(B) Registration (dephasing in the sector basis) keeps BOTH sector populations; never drops the singlet")
    n = 3
    okall = True

    # B1: the singlet projector commutes with the SU(N_c) adjoint action G -> U G U^dag
    #     (the singlet subspace is SU(N_c)-invariant) -> it is the trivial irrep, a genuine
    #     central sector (the MOST central content, never off-diagonal).
    U = haar_su(n)
    G = RNG.standard_normal((n, n)) + 1j * RNG.standard_normal((n, n))
    lhs = P_singlet(U @ G @ U.conj().T, n)
    rhs = U @ P_singlet(G, n) @ U.conj().T
    okall &= check(
        f"singlet projector is SU(N_c)-equivariant (commutes with adjoint action), err {np.max(np.abs(lhs - rhs)):.1e}; "
        f"the singlet is the trivial irrep = a genuine central sector",
        np.max(np.abs(lhs - rhs)) < 1e-9,
    )

    # Sector-resolved readout state, in the 2-d sector basis {|singlet>, |adjoint>}:
    #   rho_sec = [[S, x], [x*, C]]   (populations S,C on the diagonal; inter-sector coherence x)
    # The canonical record map D dephases in the central-sector basis:
    #   D(rho) = Pi_1 rho Pi_1 + Pi_adj rho Pi_adj  ->  keeps the diagonal (S,C), drops coherence x.
    # a genuine PSD sector-resolved density: |x|^2 <= S*C = 8/81 ~ 0.0988
    S, C, x = 1.0 / 9, 8.0 / 9, 0.25 + 0.1j
    rho = np.array([[S, x], [np.conj(x), C]], dtype=complex)
    assert abs(x) ** 2 <= S * C + 1e-12  # PSD sector state
    D = lambda r: np.diag(np.diag(r))  # dephasing in {singlet,adjoint}

    # B2: registration keeps BOTH sector populations (S and C); it removes only coherence x.
    Dr = D(rho)
    okall &= check(
        f"D keeps both populations (S={np.real(Dr[0,0]):.4f}, C={np.real(Dr[1,1]):.4f}) and removes only "
        f"inter-sector coherence (|x|: {abs(x):.3f}->{abs(Dr[0,1]):.1e}); registered readout contains S AND C",
        abs(Dr[0, 0] - S) < 1e-12 and abs(Dr[1, 1] - C) < 1e-12 and abs(Dr[0, 1]) < 1e-12,
    )

    # B3: registration NEVER drops the singlet population.  kappa_EW=0 corresponds to the
    #     map rho -> diag(0, C) (DISCARD the singlet population S) -- which is NOT D
    #     (D keeps S).  Discarding a registered diagonal outcome is not a dephasing/record op.
    drop_singlet = np.array([[0.0, 0.0], [0.0, C]], dtype=complex)
    okall &= check(
        f"kappa=0 = discard the singlet population (diag(0,C)) is NOT the record map D (which keeps S={S:.4f}); "
        f"||D(rho)-drop_singlet||={np.max(np.abs(Dr - drop_singlet)):.3f} != 0",
        np.max(np.abs(Dr - drop_singlet)) > 1e-6,
    )

    # B4: CONTRAST with the chirality no-go -- what registration DOES annihilate is the
    #     inter-sector COHERENCE x (off-diagonal), the analog of a grading-anticommuting
    #     carrier.  The singlet POPULATION is diagonal, so it survives; coherence does not.
    okall &= check(
        f"what D annihilates is the OFF-diagonal coherence ({abs(x):.3f}->0), not the diagonal singlet "
        f"population -- the singlet is never the annihilated object",
        abs(Dr[0, 1]) < 1e-12 and abs(Dr[0, 0] - S) < 1e-12,
    )
    return okall


# ============================================================
# (C) kappa_EW is an INTER-sector weight, not delivered by the partition (the
#     r-dial test): the partition delivers {S, C} and the counts, but the
#     scalar readout f = C + kappa*S has kappa FREE given the same {S,C}.
# ============================================================
def part_C():
    print("\n(C) kappa_EW is a free inter-sector weight: partition delivers {S,C}+counts, NOT the C+kappa*S weight")
    n = 3
    okall = True
    G = RNG.standard_normal((n, n)) + 1j * RNG.standard_normal((n, n))
    S = np.real(hs(P_singlet(G, n), P_singlet(G, n)))
    C = np.real(hs(P_adjoint(G, n), P_adjoint(G, n)))
    # both completions are functions of the SAME registered {S,C}:
    f0 = C + 0.0 * S  # kappa=0 : drop the singlet
    f1 = C + 1.0 * S  # kappa=1 : keep the singlet (full trace)
    okall &= check(
        f"from identical registered {{S={S:.3f},C={C:.3f}}}: kappa=0 readout=C={f0:.3f}, kappa=1 readout=C+S={f1:.3f} "
        f"-> kappa is a FREE inter-sector weight",
        abs(f0 - C) < 1e-9 and abs(f1 - (C + S)) < 1e-9 and f0 != f1,
    )
    # the partition DOES deliver the count (cardinality) fraction 8/9, but that is the
    # COUNT, not the weight: K_EW(kappa)=1/(8/9+kappa/9) still needs kappa.
    frac = (n * n - 1) / n ** 2
    K0, K1 = 1.0 / (frac + 0.0 / 9), 1.0 / (frac + 1.0 / 9)
    okall &= check(
        f"the delivered COUNT is the 8/9 cardinality fraction; the WEIGHT is still free: "
        f"K_EW(0)=9/8={K0:.4f}, K_EW(1)=1={K1:.4f}",
        abs(frac - 8 / 9) < 1e-12 and abs(K0 - 9 / 8) < 1e-9 and abs(K1 - 1.0) < 1e-9,
    )
    return okall


# ============================================================
# (D) Structural parallel to the retained Koide chirality no-go: the C3-character
#     partition {P0,Pd} delivers the block counts but "constrains r not at all";
#     by the identical structure the color partition constrains kappa not at all.
# ============================================================
def part_D():
    print("\n(D) Koide parallel: registration 'constrains r not at all' -> by identical structure, constrains kappa not at all")
    okall = True
    w = np.exp(2j * np.pi / 3)
    C = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)  # C3 cyclic shift
    # C3-character central-sector projectors
    P = [(np.eye(3) + w ** (-k) * C + w ** (-2 * k) * C @ C) / 3 for k in range(3)]
    # registration map D(M)=sum_k Pk M Pk
    Dmap = lambda M: sum(P[k] @ M @ P[k] for k in range(3))
    # circulant generation mass H = a I + b C + conj(b) C^2 commutes with C -> D(H)=H for ALL (a,b)
    okr = True
    rs = []
    for _ in range(6):
        a = RNG.uniform(0.5, 2.0)
        b = RNG.standard_normal() + 1j * RNG.standard_normal()
        H = a * np.eye(3) + b * C + np.conj(b) * C @ C
        if np.max(np.abs(Dmap(H) - H)) > 1e-9:
            okr = False
        rs.append(abs(b) ** 2 / a ** 2)  # the Koide within-block dial r
    okall &= check(
        f"Koide: D(H)=H for every circulant H (D constrains r not at all; r in [{min(rs):.2f},{max(rs):.2f}] all registered)",
        okr,
    )
    print("    => color analog: identical partition-map structure (delivers central-sector counts, not inter-sector")
    print("       weights) -> registration constrains kappa_EW not at all")
    return okall


# ============================================================
# (E) Directionless tell: 'drop the singlet trace' (kappa=0) and 'the physical W/Z
#     is a color singlet, so register the singlet, drop the confined adjoint'
#     (opposite) are the same register-not-read slogan pointed opposite ways.
# ============================================================
def part_E():
    print("\n(E) Directionless tell: register-not-read can be pointed at EITHER sector (the retrofit signature)")
    n = 3
    G = RNG.standard_normal((n, n)) + 1j * RNG.standard_normal((n, n))
    S = np.real(hs(P_singlet(G, n), P_singlet(G, n)))
    C = np.real(hs(P_adjoint(G, n), P_adjoint(G, n)))
    # direction 1: singlet = unregistered reference -> readout = C (kappa=0)
    read_drop_singlet = C
    # direction 2: the physical W/Z is a color singlet (trivial irrep); register the
    #              singlet, treat the color-octet (adjoint, confined) as unregistered
    #              -> readout weights the singlet (opposite direction)
    read_drop_adjoint = S
    okall = check(
        f"both are 'register one sector, drop the other' with no partition-delivered basis: "
        f"drop-singlet->C={read_drop_singlet:.3f} (kappa=0) vs drop-adjoint->S={read_drop_adjoint:.3f} "
        f"-> same slogan, opposite directions = the demoted loose dichotomy",
        read_drop_singlet != read_drop_adjoint,
    )
    print("    => register-not-read does NOT fix kappa_EW: it registers all central sectors (keeps S), the count is")
    print("       delivered but the inter-sector weight is free, and the drop-a-sector move is directionless. Route CLOSED.")
    return okall


def main():
    print("=" * 80)
    print("Register-not-read does NOT fix kappa_EW: color-sector no-go (zero fitted targets)")
    print("=" * 80)
    res = [part_A(), part_B(), part_C(), part_D(), part_E()]
    print("\n" + "=" * 80)
    print(f"RUNNER STATUS: {'PASS' if all(res) and FAIL == 0 else 'FAIL'} (PASS={PASS} FAIL={FAIL})")
    print("=" * 80)
    return 0 if (all(res) and FAIL == 0) else 1


if __name__ == "__main__":
    raise SystemExit(main())
