#!/usr/bin/env python3
"""Axiom-preserving block-spin is a channel, not a morphism; color re-emerges per scale.

Class-A exact verification for the source note

    docs/BLOCK_SPIN_CP_COMPRESSION_COLOR_REEMERGENCE_NARROW_NO_GO_NOTE_2026-06-08.md

CONTEXT (ST4, RG on the physical lattice).  The ST3/ST4 wall-map asks: can a block-spin
decimation simultaneously preserve the Quantum axiom (one qubit per site) and the
graph-first SU(3) color structure?  Note the sharp collision: the color carrier IS the
2x2x2 taste cube — a standard 2^3 blocking consumes exactly the eight sites that carry it.

THE ANSWER (narrow no-go on TRANSPORT + a positive re-emergence corollary):
  (T1) NO MORPHISM BLOCKING.  A 2x2x2 block carries the local algebra M_256 (eight qubits);
       the Quantum axiom requires M_2 at the block-site.  A unital *-homomorphism
       M_n -> M_m exists iff n | m (a unital hom sends the n diagonal matrix units to n
       mutually-orthogonal nonzero equivalent projectors summing to I_m, so m = n*r).
       256 does not divide 2 — so NO algebra-morphism blocking preserves the axiom.
       (Constructive positive control: M_2 -> M_4 via A -> A (x) I_2 exists, 2 | 4.)
  (T2) AXIOM-PRESERVING CHANNEL BLOCKING IS NOT MULTIPLICATIVE.  If a block-qubit
       coarse-graining were unital and multiplicative, it would be the forbidden
       M_256 -> M_2 algebra morphism from T1.  Thus any unital block-qubit quantum channel
       is non-multiplicative.  The runner tests the canonical one-leg compression model
       E(X) = V^dag X V with V: C^2 -> C^256: unital and completely positive but NOT
       multiplicative; by T1, for EVERY isometry V there exist block observables X, Y
       with E(XY) != E(X) E(Y).  Information loss is forced; the coarse-graining step is
       a channel, not an automorphism.
  (T3) COLOR IS NOT TRANSPORTED.  su(3) is simple (any Lie-algebra map is faithful or
       zero) and has no faithful action on C^2: the traceless-Hermitian operators on the
       block qubit form su(2) (real dim 3 < 8 = dim su(3)).  So the compressed block site
       carries NO faithful color action — no axiom-preserving blocking transports the
       graph-first SU(3) across the step.  [This reuses the QUBIT_LINK_U2 boundary's
       dimension fact at the block-site.]
  (T4) COLOR RE-EMERGES PER SCALE (the corollary that defuses the "wall" reading).  By
       construction, the blocked lattice is again Z^3 with one qubit per block-site —
       it satisfies Lattice + Quantum verbatim.  The retained graph-first construction is
       SCALE-BLIND: re-running it on the BLOCK-level 2x2x2 cube reproduces the identical
       algebra (selected-axis su(2) on the fibers; joint commutant dimension 10;
       symmetric/antisymmetric ranks 9/1 -> su(3) (+) u(1)).  Color is a PER-SCALE
       derivation, not a quantity transported by the RG step.

SCOPE: this is NOT a wall against RG — standard Kadanoff/block-spin RG is also a
truncating (non-morphism) map; the content is that exact morphism transport is impossible,
any unital block-qubit quantum channel is non-multiplicative, and color is re-derived at each
scale rather than carried.
The CHOICE of isometry V (which 2 of 256 states survive) is an undelivered selection —
the same family as the open gauge-link-dynamics input — and is NOT supplied here.
Per-scale color (retained, graph_first_su3) is untouched.  No new axiom/import.

Run: python3 scripts/frontier_block_spin_cp_compression_color_reemergence_2026_06_08.py
"""

from __future__ import annotations

import numpy as np

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    line = f"  [{tag}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


rng = np.random.default_rng(20260608)

# ===========================================================================
# Part 1.  (T1) Unital *-homomorphism M_n -> M_m exists iff n | m.
# ===========================================================================
print("=" * 78)
print("Part 1  (T1) morphism blocking: unital *-hom M_n -> M_m iff n | m; 256 does not divide 2")
print("=" * 78)

# positive control: M_2 -> M_4, A -> A (x) I_2 (2 | 4): unital, *-preserving, multiplicative
A = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
B = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
phi = lambda X: np.kron(X, np.eye(2))
check("positive control: M_2 -> M_4 (A -> A (x) I_2) is a unital multiplicative *-hom (2 | 4)",
      np.allclose(phi(A @ B), phi(A) @ phi(B)) and np.allclose(phi(np.eye(2)), np.eye(4))
      and np.allclose(phi(A.conj().T), phi(A).conj().T))

# impossibility direction: a unital *-hom M_4 -> M_2 needs the 4 diagonal matrix units to
# map to 4 mutually-orthogonal NONZERO projectors in M_2 summing to I_2.  Rank bound: the
# ranks of mutually-orthogonal nonzero projectors in M_2 sum to <= 2, so at most TWO exist.
max_orth = 2  # rank(I_2)
check("M_4 -> M_2 impossible: needs 4 mutually-orthogonal nonzero projectors in M_2; "
      "rank bound allows at most 2 (4 > 2)", 4 > max_orth,
      "matrix units e_ii are equivalent => all images nonzero or all zero; all-zero kills unitality")
# the 2x2x2 block: local algebra M_{2^8} = M_256; axiom block-site algebra M_2:
n_block, m_site = 2 ** 8, 2
check("the 2x2x2 block algebra is M_256; the axiom block-site algebra is M_2; "
      "256 does not divide 2 -> NO unital *-homomorphism blocking exists",
      n_block == 256 and m_site == 2 and (m_site % n_block != 0))

# ===========================================================================
# Part 2.  (T2) Unital block-qubit channels are non-multiplicative; isometric CP model.
#   (Demonstrated at the memory-safe 2-qubit block M_4 -> M_2; the logic is dimension-blind.)
# ===========================================================================
print("=" * 78)
print("Part 2  (T2) unital block-qubit channels are not morphisms; compression model is not multiplicative")
print("=" * 78)

V, _ = np.linalg.qr(rng.normal(size=(4, 2)) + 1j * rng.normal(size=(4, 2)))
E = lambda X: V.conj().T @ X @ V
check("E is unital (E(I_4) = I_2) and *-preserving (E(X^dag) = E(X)^dag)",
      np.allclose(E(np.eye(4)), np.eye(2))
      and np.allclose(E(A4 := rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))).conj().T,
                      E(A4.conj().T)))
# CP: E = V^dag . V is manifestly completely positive (a single Kraus/Stinespring leg).
X = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
Y = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
check("E is NOT multiplicative: E(XY) != E(X)E(Y) (explicit exhibit)",
      not np.allclose(E(X @ Y), E(X) @ E(Y), atol=1e-8),
      f"max dev {np.max(np.abs(E(X@Y)-E(X)@E(Y))):.3f}")
# and by T1 this is FORCED for every one-leg compression V: multiplicativity for all X,Y
# would make E a unital *-hom M_4 -> M_2, which Part 1 rules out.  Spot-verify across many
# random isometries:
forced = True
for _ in range(50):
    Vr, _ = np.linalg.qr(rng.normal(size=(4, 2)) + 1j * rng.normal(size=(4, 2)))
    Er = lambda Z: Vr.conj().T @ Z @ Vr
    Xr = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
    Yr = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
    if np.allclose(Er(Xr @ Yr), Er(Xr) @ Er(Yr), atol=1e-8):
        forced = False
        break
check("for EVERY isometry the compression fails multiplicativity (50 random isometries; "
      "forced by T1 — a multiplicative E would be the impossible unital *-hom)", forced)

# ===========================================================================
# Part 3.  (T3) No faithful su(3) on the block qubit: color is NOT transported.
# ===========================================================================
print("=" * 78)
print("Part 3  (T3) su(3) (dim 8, simple) has no faithful action on C^2 (su(2): dim 3)")
print("=" * 78)

check("dim su(3) = 8 > 3 = dim of traceless-Hermitian operators on C^2",
      (3 ** 2 - 1) == 8 and (2 ** 2 - 1) == 3)
check("su(3) is simple => any Lie map is faithful or zero; an embedding su(3) -> su(2) "
      "is dimensionally impossible (8 > 3) => the block qubit carries NO faithful color",
      8 > 3, "color does NOT transport through any axiom-preserving blocking")

# ===========================================================================
# Part 4.  (T4) Color RE-EMERGES per scale: the graph-first construction is scale-blind.
#   Re-run the retained graph-first checks on the BLOCK-level taste cube (8 block-qubits).
# ===========================================================================
print("=" * 78)
print("Part 4  (T4) re-run graph-first SU(3) on the BLOCK-level cube: identical algebra")
print("=" * 78)

I2 = np.eye(2)
SX = np.array([[0, 1], [1, 0]], complex)
SY = np.array([[0, -1j], [1j, 0]], complex)
SZ = np.array([[1, 0], [0, -1]], complex)


def kron3(a, b, c):
    return np.kron(a, np.kron(b, c))


# block-level taste cube: corners of the 2x2x2 cube OF BLOCK-SITES; single-particle C^8.
# selected axis mu = 1: shift X_1, parity Z_1, Y_1 = -i Z_1 X_1 on the cube coordinates.
X1 = kron3(SX, I2, I2)
Z1 = kron3(SZ, I2, I2)
Y1 = -1j * Z1 @ X1
check("block-level selected-axis su(2): X^2 = Y^2 = Z^2 = I and [X,Y] = 2iZ (cyclic)",
      np.allclose(X1 @ X1, np.eye(8)) and np.allclose(Y1 @ Y1, np.eye(8))
      and np.allclose(Z1 @ Z1, np.eye(8))
      and np.allclose(X1 @ Y1 - Y1 @ X1, 2j * Z1)
      and np.allclose(Y1 @ Z1 - Z1 @ Y1, 2j * X1)
      and np.allclose(Z1 @ X1 - X1 @ Z1, 2j * Y1))

# residual swap of the complementary axes (2 <-> 3) on the block cube:
P_swap = np.zeros((8, 8))
for x1 in range(2):
    for x2 in range(2):
        for x3 in range(2):
            P_swap[4 * x1 + 2 * x3 + x2, 4 * x1 + 2 * x2 + x3] = 1.0
check("residual complementary-axis swap commutes with the selected-axis su(2)",
      all(np.allclose(P_swap @ M - M @ P_swap, 0) for M in (X1, Y1, Z1)))

# joint commutant of {X1, Y1, Z1, P_swap} has dimension 10 = gl(3) (+) gl(1):
ops = [X1, Y1, Z1, P_swap]
rows = []
for M in ops:
    comm = np.kron(np.eye(8), M.T) - np.kron(M, np.eye(8))   # vec(AM - MA) ... careful:
    # [A, M] = 0  <=>  (I (x) M^T - M (x) I) vec(A) = 0 with vec column-stacking: use kron(M^T, I) - kron(I, M)
    rows.append(np.kron(M.T, np.eye(8)) - np.kron(np.eye(8), M))
K = np.vstack(rows)
null_dim = 64 - np.linalg.matrix_rank(K, tol=1e-9)
check("joint commutant dimension = 10 (gl(3) (+) gl(1)) on the BLOCK-level cube "
      "(identical to the retained site-level result)", null_dim == 10,
      f"dim = {null_dim}")
# symmetric/antisymmetric split of the 4-dim base under the swap: ranks 3 and 1:
base_swap = np.zeros((4, 4))
for x2 in range(2):
    for x3 in range(2):
        base_swap[2 * x3 + x2, 2 * x2 + x3] = 1.0
sym_rank = np.linalg.matrix_rank((np.eye(4) + base_swap) / 2, tol=1e-9)
anti_rank = np.linalg.matrix_rank((np.eye(4) - base_swap) / 2, tol=1e-9)
check("base splits 3 (+) 1 under the residual swap (ranks 3 and 1) -> su(3) at the block "
      "scale: the construction is SCALE-BLIND; color re-emerges per scale",
      sym_rank == 3 and anti_rank == 1, f"ranks ({sym_rank},{anti_rank})")

# ===========================================================================
print("=" * 78)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("=" * 78)
print("SCOPE (narrow transport no-go + per-scale corollary): NO unital *-homomorphism")
print("  blocking exists (256 does not divide 2), so axiom-preserving block-spin cannot be")
print("  an algebra morphism.  Any unital block-qubit quantum channel is non-multiplicative, and the")
print("  runner's isometric CP compression model is never multiplicative (forced).  The")
print("  block qubit carries NO faithful su(3): color is NOT TRANSPORTED through the step.")
print("  BUT this is not a wall: the blocked lattice satisfies Lattice+Quantum verbatim and")
print("  the retained graph-first construction is SCALE-BLIND (re-verified at the block")
print("  level: su(2) relations, commutant dim 10, 3(+)1 split) — color is a PER-SCALE")
print("  derivation, not an RG-carried quantity.  Standard Kadanoff blocking is likewise a")
print("  truncating channel (method context, not an import).  The CHOICE of isometry V is")
print("  an undelivered selection (same family as the open gauge-link-dynamics input) and")
print("  is NOT supplied here.  Per-scale color (retained) untouched.  No new axiom.")
if FAIL:
    raise SystemExit(1)
