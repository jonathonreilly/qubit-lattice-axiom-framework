#!/usr/bin/env python3
"""SU(3) link-star reduction: exact invariant-projector evaluation of the
star, three evenness identities (dagger, bar, transpose), the polarized
Cayley-Hamilton reduction with its det-polarization term, local rigidity of
pair data (full-rank Jacobian), and the transpose sheet carrying only the
chiral sign — an exhibited multilinear escape in this witness, invisible to
the scoped real weights.

Paired note:
docs/THETA_SU3_LINK_STAR_PAIRWISE_REDUCTION_LOCAL_RIGIDITY_TRANSPOSE_SHEET_AND_CHIRAL_SIGN_ESCAPE_BOUNDED_THEOREM_NOTE_2026-07-02.md

Class-A finite checks only: exact linear algebra (invariant projectors =
joint null spaces of the Lie-algebra action — NO group integration anywhere),
exact trace-identity checks at deterministic pseudo-random points (fixed
seed), and a full-rank Jacobian certificate. No fits, no external
comparators, no measured values, no Monte Carlo.

Sections:
  A. Machinery ground: generator conventions verified against expm for every
     rep slot (guards the conjugate-representation sign); the projector is
     idempotent, Hermitian, and satisfies sigma(V) Pi = Pi on deterministic
     test elements (the defining property of the Haar average); the
     singlet-rank table over {1, F, Fb}^3 matches representation theory
     (exactly nine nonzero channels, each rank 1; the design-time
     expectation of five was corrected by the machine — the third slot
     carries conj(D_T)).
  B. Star and evenness: the star of a real class weight is real; invariant
     under diagonal conjugation; invariant under simultaneous dagger AND
     simultaneous entrywise conjugation (bar — the SU(3) outer flip) AND
     simultaneous transpose; the epsilon channel I(F,F,Fb) is nonzero and
     conjugate-paired with I(Fb,Fb,F); removing the epsilon channels
     changes the star (the reduction is via evenness, not channel absence).
  C. Invariant algebra: polarized Cayley-Hamilton for 3x3 —
     tr(ABC) + tr(ACB) equals the pairwise-trace formula PLUS the
     det-polarization term (exact); the det-polarization is
     transpose-invariant while the chiral datum d = tr(ABC) - tr(ACB) is
     transpose-odd; parity table: dagger(d) = -conj(d), bar(d) = conj(d),
     so Re(d) is dagger-odd and Im(d) is bar-odd — every real-linear
     component of d is odd under a flip that real-weight stars are even
     under.
  D. Rigidity and sheets: at fixed generic (A, B), the 10 x 8 real Jacobian
     of the pair-data map on C has full rank 8 (no continuous
     pair-data-preserving deformation exists: local rigidity); the
     simultaneous-transpose triple preserves ALL 18 pair data exactly while
     flipping the sign of d (|d| > 0.1: the sheets are genuinely distinct
     diagonal orbits) — and the star takes the SAME value on both sheets.

Expected close: TOTAL: PASS=17 FAIL=0
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


def expiH(H: np.ndarray) -> np.ndarray:
    w, U = np.linalg.eigh(H)
    return U @ np.diag(np.exp(1j * w)) @ U.conj().T


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


def conj_slot_gen(T: str, X: np.ndarray) -> np.ndarray:
    # generator of V |-> conj(D_T(V)): D ~ 1 + i eps G  =>  conj D ~ 1 - i eps conj(G)
    return -np.conj(rep_gen(T, X))


def kron3(a: np.ndarray, b: np.ndarray, c: np.ndarray) -> np.ndarray:
    return np.kron(np.kron(a, b), c)


def invariant_projector(R: str, S: str, T: str) -> np.ndarray:
    dR, dS, dT = dim_of(R), dim_of(S), dim_of(T)
    rows = []
    for X in GM:
        rows.append(kron3(rep_gen(R, X), np.eye(dS), np.eye(dT))
                    + kron3(np.eye(dR), rep_gen(S, X), np.eye(dT))
                    + kron3(np.eye(dR), np.eye(dS), conj_slot_gen(T, X)))
    A = np.vstack(rows)
    _, s, vh = np.linalg.svd(A)
    null = vh[int(np.sum(s > 1e-9)):].conj().T
    return null @ null.conj().T


def sigma_of(R: str, S: str, T: str, V: np.ndarray) -> np.ndarray:
    return kron3(rep_mat(R, V), rep_mat(S, V), np.conj(rep_mat(T, V)))


def I_RST(R: str, S: str, T: str, S1, S2, S3) -> complex:
    Pi = invariant_projector(R, S, T)
    M = kron3(rep_mat(R, S1), rep_mat(S, S2), rep_mat(T, S3).T)
    return complex(np.trace(Pi @ M))


REPS3 = ["1", "F", "Fb"]
CW = {"1": 1.0, "F": 0.35, "Fb": 0.35}  # real class weight w = 1 + c (chi_F + chi_Fb)


def star(S1, S2, S3, drop_epsilon: bool = False) -> complex:
    tot = 0.0 + 0j
    for (R, S, T) in product(REPS3, repeat=3):
        if drop_epsilon and (R, S, T) in [("F", "F", "Fb"), ("Fb", "Fb", "F")]:
            continue
        tot += CW[R] * CW[S] * CW[T] * I_RST(R, S, T, S1, S2, S3)
    return complex(tot)


# ---------------------------------------------------------------------------
# Section A: machinery ground
# ---------------------------------------------------------------------------
print("Section A: projector machinery ground")

ok_gen = True
for r in ["F", "Fb"]:
    for X in [GM[0], GM[4], GM[7]]:
        for t in [0.3, 0.9]:
            g = expiH(t * X)
            lhs = rep_mat(r, g)
            w, U = np.linalg.eigh(t * (rep_gen(r, X) if r == "F" else None) if False else t * X)
            # direct: rep of e^{itX}: for F it's g; for Fb it's conj(g); verify
            # against expm of the claimed generator
            G = rep_gen(r, X)
            wg, Ug = np.linalg.eigh(t * G) if np.allclose(G, G.conj().T) else (None, None)
            if wg is None:
                # generator may be non-Hermitian only through the conj; use series
                E = np.eye(3, dtype=complex)
                term = np.eye(3, dtype=complex)
                for k in range(1, 40):
                    term = term @ (1j * t * G) / k
                    E = E + term
            else:
                E = Ug @ np.diag(np.exp(1j * wg)) @ Ug.conj().T
            ok_gen = ok_gen and np.allclose(lhs, E, atol=1e-10)
ok_conj_slot = True
for T in ["F", "Fb"]:
    for X in [GM[1], GM[5]]:
        t = 0.7
        g = expiH(t * X)
        lhs = np.conj(rep_mat(T, g))
        G = conj_slot_gen(T, X)
        E = np.eye(3, dtype=complex)
        term = np.eye(3, dtype=complex)
        for k in range(1, 60):
            term = term @ (1j * t * G) / k
            E = E + term
    ok_conj_slot = ok_conj_slot and np.allclose(lhs, E, atol=1e-10)
check("A1 generator conventions match the exponentiated reps for F, Fb and"
      " the conjugate slots (guards the conjugate-rep sign)",
      ok_gen and ok_conj_slot)

TESTV = rand_su3(3)
ok_inv = True
ok_proj = True
for (R, S, T) in [("F", "Fb", "1"), ("F", "F", "Fb"), ("Fb", "Fb", "F"),
                  ("F", "F", "F")]:
    Pi = invariant_projector(R, S, T)
    ok_proj = ok_proj and np.allclose(Pi, Pi.conj().T) \
        and np.allclose(Pi @ Pi, Pi, atol=1e-10)
    for V in TESTV:
        ok_inv = ok_inv and np.allclose(sigma_of(R, S, T, V) @ Pi, Pi,
                                        atol=1e-9)
check("A2 projectors are Hermitian idempotents with sigma(V) Pi = Pi on"
      " deterministic test elements (the defining Haar-average property)",
      ok_proj and ok_inv)

EXPECT_RANK = {}
for (R, S, T) in product(REPS3, repeat=3):
    EXPECT_RANK[(R, S, T)] = 0
# content of slot 3 is conj(D_T): T = F contributes Fb-content and vice
# versa. Singlet channels of R x S x conj(T):
for key in [("1", "1", "1"), ("F", "Fb", "1"), ("Fb", "F", "1"),
            ("F", "1", "F"), ("Fb", "1", "Fb"), ("1", "F", "F"),
            ("1", "Fb", "Fb"), ("F", "F", "Fb"), ("Fb", "Fb", "F")]:
    EXPECT_RANK[key] = 1
ok_rank = True
bad = []
for (R, S, T) in product(REPS3, repeat=3):
    r = int(round(float(np.trace(invariant_projector(R, S, T)).real)))
    # trace of a projector = rank
    want = EXPECT_RANK[(R, S, T)]
    if r != want:
        ok_rank = False
        bad.append(((R, S, T), r, want))
check("A3 singlet-rank table over {1,F,Fb}^3 matches representation theory"
      " (nine rank-1 channels, all others rank 0)",
      ok_rank, f"mismatches: {bad}" if bad else "all 27 channels as expected")

# ---------------------------------------------------------------------------
# Section B: star and evenness identities
# ---------------------------------------------------------------------------
print("Section B: star and evenness")

S1, S2, S3 = rand_su3(3)
A2_, B2_ = rand_su3(2)

G0 = star(S1, S2, S3)
check("B1 the star of a real class weight is real",
      abs(G0.imag) < 1e-12, f"G = {G0.real:.12f}, imag = {G0.imag:.2e}")

ok_diag = True
for g in rand_su3(2):
    Gd = star(g @ S1 @ g.conj().T, g @ S2 @ g.conj().T, g @ S3 @ g.conj().T)
    ok_diag = ok_diag and abs(Gd - G0) < 1e-10
check("B2 diagonal-conjugation invariance (exact projector evaluation)",
      ok_diag)

Gdag = star(S1.conj().T, S2.conj().T, S3.conj().T)
check("B3 dagger-evenness: G(S^dag triple) = G", abs(Gdag - G0) < 1e-12)

Gbar = star(S1.conj(), S2.conj(), S3.conj())
check("B4 bar-evenness (SU(3) outer flip): G(conj triple) = G",
      abs(Gbar - G0) < 1e-12)

Gt = star(S1.T, S2.T, S3.T)
check("B5 transpose-evenness: G(S^T triple) = G", abs(Gt - G0) < 1e-12)

eps_val = I_RST("F", "F", "Fb", S1, S2, S3)
eps_conj = I_RST("Fb", "Fb", "F", S1, S2, S3)
check("B6 the epsilon channel is nonzero and conjugate-paired:"
      " I(F,F,Fb) = conj I(Fb,Fb,F)",
      abs(eps_val) > 0.01 and abs(eps_val - np.conj(eps_conj)) < 1e-10,
      f"I(F,F,Fb) = {eps_val:.6f}")

G_noeps = star(S1, S2, S3, drop_epsilon=True)
check("B7 removing the epsilon channels changes the star: the pairwise"
      " reduction is via evenness, not channel absence",
      abs(G_noeps - G0) > 1e-3,
      f"|G - G_noeps| = {abs(G_noeps - G0):.6f}")

# ---------------------------------------------------------------------------
# Section C: invariant algebra (exact identities at deterministic points)
# ---------------------------------------------------------------------------
print("Section C: polarized Cayley-Hamilton and the chiral datum")


def det_polar(A, B, C):
    tot = 0.0 + 0j
    for co in product([0, 1], repeat=3):
        m = co[0] * A + co[1] * B + co[2] * C
        tot += (-1) ** (3 - sum(co)) * np.linalg.det(m)
    return tot


ok_ch = True
for _ in range(4):
    A = RNG.normal(size=(3, 3)) + 1j * RNG.normal(size=(3, 3))
    B = RNG.normal(size=(3, 3)) + 1j * RNG.normal(size=(3, 3))
    C = RNG.normal(size=(3, 3)) + 1j * RNG.normal(size=(3, 3))
    t = np.trace
    lhs = t(A @ B @ C) + t(A @ C @ B)
    rhs = (det_polar(A, B, C)
           + t(A) * t(B @ C) + t(B) * t(A @ C) + t(C) * t(A @ B)
           - t(A) * t(B) * t(C))
    ok_ch = ok_ch and abs(lhs - rhs) < 1e-10
check("C1 polarized Cayley-Hamilton (3x3): tr(ABC) + tr(ACB) = pairwise"
      " traces + det-polarization term (exact)", ok_ch)

A3_, B3_, C3_ = rand_su3(3)
dp0 = det_polar(A3_, B3_, C3_)
dpT = det_polar(A3_.T, B3_.T, C3_.T)
d0 = np.trace(A3_ @ B3_ @ C3_) - np.trace(A3_ @ C3_ @ B3_)
dT = np.trace(A3_.T @ B3_.T @ C3_.T) - np.trace(A3_.T @ C3_.T @ B3_.T)
check("C2 det-polarization is transpose-invariant; the chiral datum"
      " d = tr(ABC) - tr(ACB) is transpose-odd",
      abs(dp0 - dpT) < 1e-12 and abs(dT + d0) < 1e-12,
      f"d = {d0:.6f}")

ddag = (np.trace(A3_.conj().T @ B3_.conj().T @ C3_.conj().T)
        - np.trace(A3_.conj().T @ C3_.conj().T @ B3_.conj().T))
dbar = (np.trace(A3_.conj() @ B3_.conj() @ C3_.conj())
        - np.trace(A3_.conj() @ C3_.conj() @ B3_.conj()))
check("C3 parity table: dagger(d) = -conj(d) and bar(d) = conj(d) — every"
      " real-linear component of d is odd under a flip the star is even"
      " under",
      abs(ddag + np.conj(d0)) < 1e-12 and abs(dbar - np.conj(d0)) < 1e-12)

# ---------------------------------------------------------------------------
# Section D: local rigidity and the transpose sheet
# ---------------------------------------------------------------------------
print("Section D: pair-data rigidity and the transpose sheet")

AA, BB, CC = rand_su3(3)


def pairdata_C(C):
    t = np.trace
    vals = [t(C), t(AA.conj().T @ C), t(AA @ C), t(BB.conj().T @ C), t(BB @ C)]
    out = []
    for v in vals:
        out += [v.real, v.imag]
    return np.array(out)


EPS = 1e-6
J = np.zeros((10, 8))
base = pairdata_C(CC)
for a in range(8):
    Cp = expiH(EPS * GM[a]) @ CC
    J[:, a] = (pairdata_C(Cp) - base) / EPS
sv = np.linalg.svd(J, compute_uv=False)
check("D1 local rigidity: the 10x8 Jacobian of the pair-data map on C has"
      " full rank 8 — no continuous pair-data-preserving deformation of C"
      " exists at fixed (A, B)",
      sv[7] > 1e-2, f"smallest singular value = {sv[7]:.4f}")


def all_pairdata(A, B, C):
    t = np.trace
    vals = [t(A), t(B), t(C),
            t(B.conj().T @ A), t(B @ A),
            t(C.conj().T @ A), t(C @ A),
            t(C.conj().T @ B), t(C @ B)]
    out = []
    for v in vals:
        out += [v.real, v.imag]
    return np.array(out)


pd0 = all_pairdata(AA, BB, CC)
pdT = all_pairdata(AA.T, BB.T, CC.T)
check("D2 the simultaneous-transpose triple preserves ALL 18 pair data"
      " exactly", float(np.max(np.abs(pd0 - pdT))) < 1e-12,
      f"max deviation = {float(np.max(np.abs(pd0 - pdT))):.2e}")

dv = np.trace(AA @ BB @ CC) - np.trace(AA @ CC @ BB)
dvT = np.trace(AA.T @ BB.T @ CC.T) - np.trace(AA.T @ CC.T @ BB.T)
check("D3 the sheets are genuinely distinct diagonal orbits: |d| > 0.1 and"
      " d flips sign on the transpose sheet (d is a diagonal-conjugation"
      " invariant)",
      abs(dv) > 0.1 and abs(dvT + dv) < 1e-12,
      f"d = {dv:.6f}")

Gsheet0 = star(AA, BB, CC)
GsheetT = star(AA.T, BB.T, CC.T)
check("D4 the star takes the SAME value on both sheets (transpose-evenness"
      " on the rigidity witness): the chiral sign is the exhibited"
      " multilinear escape here and the scoped real weights cannot read it",
      abs(GsheetT - Gsheet0) < 1e-12,
      f"G = {Gsheet0.real:.10f} on both sheets")

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
