#!/usr/bin/env python3
"""The phase-type insertion class: the triality-phase weight is the exact
nonabelian generalization of the abelian theta slot; its flip table is
theta-like (dagger and bar conjugate the phase, transpose preserves the
star); it reads exactly the abelian/center shadow of orientation-odd data
(imaginary parts of pair-composite traces plus the epsilon channel); and no
single-link class-weight insertion — real or phased, any alpha — reads the
chiral sign, which the path-antisymmetrized multi-link chain observable
reads exactly.

Paired note:
docs/THETA_PHASE_INSERTION_TRIALITY_FLIP_TABLE_SINGLE_LINK_NOGO_CHAIN_READER_BOUNDED_THEOREM_NOTE_2026-07-02.md

Class-A finite checks only: exact invariant-projector evaluation (joint null
space of the Lie-algebra action; no group integration anywhere), exact trace
identities, and a 1D quadrature for the abelian shadow. Deterministic; no
fits, no external comparators, no measured values, no Monte Carlo.

Sections:
  A. Abelian shadow: on U(1) the truncated triality-phase weight is exactly
     the argument-shifted weight 1 + 2c cos(phi + alpha) — the abelian theta
     slot — with Fourier coefficients c e^{+-i alpha} at n = +-1.
  B. Flip table (projector-exact, several alpha): dagger and bar send
     alpha -> -alpha; transpose preserves G_alpha; diagonal conjugation
     preserves G_alpha; G_alpha is real (conjugate channel pairing).
  C. The read content: the alpha-odd part O = G_alpha - G_{-alpha} matches
     the exact channel formula; O is nonzero; the pair channels are exact
     transport composites I(F,1,F) = tr(S3 S1)/3 and I(1,F,F) = tr(S3 S2)/3
     — so O reads imaginary parts of pair-composite traces plus the epsilon
     channel; and O is transpose-EVEN while the chiral datum flips sign:
     no single-link class-weight insertion reads the chiral sign.
  D. The chain reader: D_chain = tr(S1 S2 S3) - tr(S1 S3 S2) is
     diagonal-conjugation invariant, transpose-ODD, nonzero, with the
     dagger/bar parity table (dagger: -conj, bar: conj) — the chiral sign is
     read by path-antisymmetrized multi-link observables.

Expected close: TOTAL: PASS=14 FAIL=0
"""
from __future__ import annotations

from itertools import product

import numpy as np

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    print(f"  [{status}] {name}")
    if detail:
        print(f"         {detail}")


RNG = np.random.default_rng(7)


def rand_su3(n: int = 1):
    out = []
    for _ in range(n):
        z = (RNG.normal(size=(3, 3)) + 1j * RNG.normal(size=(3, 3))) / np.sqrt(2)
        q, r = np.linalg.qr(z)
        q = q @ np.diag(np.diag(r) / np.abs(np.diag(r)))
        q = q / np.linalg.det(q) ** (1 / 3)
        out.append(q)
    return out


LAM = np.zeros((8, 3, 3), dtype=complex)
LAM[0][0, 1] = LAM[0][1, 0] = 1
LAM[1][0, 1] = -1j
LAM[1][1, 0] = 1j
LAM[2][0, 0] = 1
LAM[2][1, 1] = -1
LAM[3][0, 2] = LAM[3][2, 0] = 1
LAM[4][0, 2] = -1j
LAM[4][2, 0] = 1j
LAM[5][1, 2] = LAM[5][2, 1] = 1
LAM[6][1, 2] = -1j
LAM[6][2, 1] = 1j
LAM[7][0, 0] = LAM[7][1, 1] = 1 / np.sqrt(3)
LAM[7][2, 2] = -2 / np.sqrt(3)
GM = [LAM[i] for i in range(8)]


def dim_of(r: str) -> int:
    return 1 if r == "1" else 3


def rep_mat(r: str, g: np.ndarray) -> np.ndarray:
    if r == "1":
        return np.ones((1, 1), dtype=complex)
    return g if r == "F" else np.conj(g)


def rep_gen(r: str, X: np.ndarray) -> np.ndarray:
    if r == "1":
        return np.zeros((1, 1), dtype=complex)
    return X if r == "F" else -np.conj(X)


def kron3(a, b, c) -> np.ndarray:
    return np.kron(np.kron(a, b), c)


def invariant_projector(R: str, S: str, T: str) -> np.ndarray:
    dR, dS, dT = dim_of(R), dim_of(S), dim_of(T)
    rows = []
    for X in GM:
        g3 = -np.conj(rep_gen(T, X))
        rows.append(kron3(rep_gen(R, X), np.eye(dS), np.eye(dT))
                    + kron3(np.eye(dR), rep_gen(S, X), np.eye(dT))
                    + kron3(np.eye(dR), np.eye(dS), g3))
    A = np.vstack(rows)
    _, s, vh = np.linalg.svd(A)
    null = vh[int(np.sum(s > 1e-9)):].conj().T
    return null @ null.conj().T


def I_RST(R: str, S: str, T: str, S1, S2, S3) -> complex:
    Pi = invariant_projector(R, S, T)
    M = kron3(rep_mat(R, S1), rep_mat(S, S2), rep_mat(T, S3).T)
    return complex(np.trace(Pi @ M))


REPS3 = ["1", "F", "Fb"]
CBASE = 0.35


def cw(r: str, alpha: float) -> complex:
    if r == "1":
        return 1.0
    return CBASE * np.exp(1j * alpha) if r == "F" else CBASE * np.exp(-1j * alpha)


def star(S1, S2, S3, alpha: float) -> complex:
    tot = 0.0 + 0j
    for (R, S, T) in product(REPS3, repeat=3):
        tot += cw(R, alpha) * cw(S, alpha) * cw(T, alpha) \
            * I_RST(R, S, T, S1, S2, S3)
    return complex(tot)


# ---------------------------------------------------------------------------
# Section A: abelian shadow
# ---------------------------------------------------------------------------
print("Section A: abelian shadow of the triality-phase insertion")

NG = 2048
PHI = (np.arange(NG) + 0.31) * 2 * np.pi / NG
ALPHA0 = 0.7
w_u1 = 1 + CBASE * np.exp(1j * ALPHA0) * np.exp(1j * PHI) \
    + CBASE * np.exp(-1j * ALPHA0) * np.exp(-1j * PHI)
shifted = 1 + 2 * CBASE * np.cos(PHI + ALPHA0)
check("A1 U(1) case: the triality-phase weight IS the argument-shifted"
      " weight 1 + 2c cos(phi + alpha) — the abelian theta-slot shape",
      bool(np.allclose(w_u1.real, shifted, atol=1e-12))
      and bool(np.allclose(w_u1.imag, 0, atol=1e-12)))

c_plus = complex(np.mean(w_u1 * np.exp(-1j * PHI)))
c_minus = complex(np.mean(w_u1 * np.exp(1j * PHI)))
check("A2 its Fourier coefficients are the phased pair c e^{+i alpha},"
      " c e^{-i alpha} at n = +1, -1 (dual-label asymmetry = the theta"
      " reading of the flux sign)",
      abs(c_plus - CBASE * np.exp(1j * ALPHA0)) < 1e-12
      and abs(c_minus - CBASE * np.exp(-1j * ALPHA0)) < 1e-12)

# ---------------------------------------------------------------------------
# Section B: flip table
# ---------------------------------------------------------------------------
print("Section B: flip table of the phased star")

S1, S2, S3 = rand_su3(3)
ALPHAS = [0.4, 0.7, 1.3]

ok_dag = True
ok_bar = True
ok_T = True
ok_real = True
for al in ALPHAS:
    G = star(S1, S2, S3, al)
    Gm = star(S1, S2, S3, -al)
    ok_dag = ok_dag and abs(star(S1.conj().T, S2.conj().T, S3.conj().T, al)
                            - Gm) < 1e-12
    ok_bar = ok_bar and abs(star(S1.conj(), S2.conj(), S3.conj(), al)
                            - Gm) < 1e-12
    ok_T = ok_T and abs(star(S1.T, S2.T, S3.T, al) - G) < 1e-12
    ok_real = ok_real and abs(G.imag) < 1e-12
check("B1 dagger sends alpha -> -alpha: G_a(S^dag) = G_{-a}(S)"
      " (the parity-like flip conjugates the insertion)", ok_dag)
check("B2 bar sends alpha -> -alpha: G_a(conj S) = G_{-a}(S)", ok_bar)
check("B3 transpose preserves the phased star for EVERY tested alpha:"
      " G_a(S^T) = G_a(S)", ok_T)
check("B4 the phased star is real (conjugate channel pairing)", ok_real)

g0 = rand_su3(1)[0]
al = 0.7
check("B5 diagonal-conjugation invariance holds at alpha != 0 (the phased"
      " insertion is frame-licensed: a class-function weight)",
      abs(star(g0 @ S1 @ g0.conj().T, g0 @ S2 @ g0.conj().T,
               g0 @ S3 @ g0.conj().T, al) - star(S1, S2, S3, al)) < 1e-10)

# ---------------------------------------------------------------------------
# Section C: the read content and the single-link no-go
# ---------------------------------------------------------------------------
print("Section C: what the phase insertion reads")

G_p = star(S1, S2, S3, al)
G_m = star(S1, S2, S3, -al)
O = G_p - G_m

IF1F = I_RST("F", "1", "F", S1, S2, S3)
I1FF = I_RST("1", "F", "F", S1, S2, S3)
IFb1 = I_RST("Fb", "1", "Fb", S1, S2, S3)
I1Fb = I_RST("1", "Fb", "Fb", S1, S2, S3)
Ieps = I_RST("F", "F", "Fb", S1, S2, S3)
IepsC = I_RST("Fb", "Fb", "F", S1, S2, S3)
c = CBASE
pred = (c * c * (np.exp(2j * al) - np.exp(-2j * al)) * (IF1F + I1FF)
        + c * c * (np.exp(-2j * al) - np.exp(2j * al)) * (IFb1 + I1Fb)
        + c ** 3 * (np.exp(1j * al) - np.exp(-1j * al)) * Ieps
        + c ** 3 * (np.exp(-1j * al) - np.exp(1j * al)) * IepsC)
check("C1 the alpha-odd part matches the exact channel formula"
      " (projector vs formula)", abs(O - pred) < 1e-12,
      f"O = {O.real:.8f}")
check("C2 the read is nonzero: |O| > 0.05", abs(O) > 0.05,
      f"|O| = {abs(O):.6f}")

t = np.trace
check("C3 the pair channels are exact transport composites:"
      " I(F,1,F) = tr(S3 S1)/3 and I(1,F,F) = tr(S3 S2)/3 — the phase"
      " insertion reads imaginary parts of pair-composite traces (the"
      " abelian/center shadow) plus the epsilon channel",
      abs(IF1F - t(S3 @ S1) / 3) < 1e-12
      and abs(I1FF - t(S3 @ S2) / 3) < 1e-12)

d = t(S1 @ S2 @ S3) - t(S1 @ S3 @ S2)
dT = t(S1.T @ S2.T @ S3.T) - t(S1.T @ S3.T @ S2.T)
O_T = star(S1.T, S2.T, S3.T, al) - star(S1.T, S2.T, S3.T, -al)
check("C4 the single-link no-go: O is transpose-EVEN (O(S^T) = O(S)"
      " exactly) while the chiral datum flips sign (d(S^T) = -d, |d| >"
      " 0.1): no single-link class-weight insertion — real or phased, any"
      " alpha — reads the chiral sign",
      abs(O_T - O) < 1e-12 and abs(dT + d) < 1e-12 and abs(d) > 0.1,
      f"|d| = {abs(d):.4f}")

# ---------------------------------------------------------------------------
# Section D: the chain reader
# ---------------------------------------------------------------------------
print("Section D: the multi-link chain reader")

ok_diag_d = True
for g in rand_su3(2):
    dc = (t(g @ S1 @ g.conj().T @ g @ S2 @ g.conj().T @ g @ S3 @ g.conj().T)
          - t(g @ S1 @ g.conj().T @ g @ S3 @ g.conj().T @ g @ S2 @ g.conj().T))
    ok_diag_d = ok_diag_d and abs(dc - d) < 1e-12
check("D1 the path-antisymmetrized chain observable"
      " D = tr(S1 S2 S3) - tr(S1 S3 S2) is diagonal-conjugation invariant"
      " (frame-licensed, configurational)", ok_diag_d)

check("D2 D is transpose-ODD and nonzero: the chiral sign IS read by"
      " multi-link path-ordered observables",
      abs(dT + d) < 1e-12 and abs(d) > 0.1, f"D = {d:.6f}")

ddag = (t(S1.conj().T @ S2.conj().T @ S3.conj().T)
        - t(S1.conj().T @ S3.conj().T @ S2.conj().T))
dbar = (t(S1.conj() @ S2.conj() @ S3.conj())
        - t(S1.conj() @ S3.conj() @ S2.conj()))
check("D3 the chain reader's dagger/bar parity table:"
      " dagger(D) = -conj(D), bar(D) = conj(D)",
      abs(ddag + np.conj(d)) < 1e-12 and abs(dbar - np.conj(d)) < 1e-12)

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
