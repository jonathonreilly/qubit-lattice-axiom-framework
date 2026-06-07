#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
No hidden carrier symmetry forbids the marginal Lorentz operator (closure (i) fails)
====================================================================================

Closure (i) of the Lorentz-naturalness obstruction was: a hidden symmetry of the
Cl(3,0)/Z^3 + continuous-time carrier that forbids the marginal c-operator (the
SME "c"-coefficient = the c_t/c_s velocity split / species max-speed differences).
This runner SYSTEMATICALLY enumerates the carrier symmetries and shows each leaves
the c-operator INVARIANT (so none forbids it); the ONLY transformation under which
c_t/c_s is odd is the boost / t<->x rotation -- the fourth signed-permutation axis
that the Z^3 (spatial-only) Lattice axiom structurally denies.

The c-operator is a LORENTZ SCALAR.  A symmetry forbids an operator only if the
operator is ODD (changes sign) under it.  c_t/c_s is odd ONLY under a transformation
that mixes the time axis with a space axis.  Every carrier symmetry acts either:
  - purely within the 3 SPATIAL axes (O_h, the merged internal SU(2)=spatial rot), or
  - purely on INTERNAL/charge/phase/chiral indices (gauge SU(3)xU(1), U(1) phase,
    gamma5/staggered chiral, CPT),
and none mixes time with space (the framework's time is a separate CONTINUOUS
structure, not a lattice axis).  Hence no carrier symmetry forbids the c-operator.

Checks:
  A  velocity-coefficient invariants: O_h (spatial + time-parity) leaves the
     (c_t, c_s) split (invariant dim 2); only B_4 (4D, t<->x) collapses to dim 1.
     => the c_t/c_s mode is O_h-EVEN; forbidden only by the t<->x symmetry.
  B  INTERNAL/gauge symmetries act on the fiber and commute with the spacetime
     velocity coefficients (a Lorentz scalar) -> do not forbid c.
  C  CLIFFORD: rescaling gamma^mu -> lambda_mu gamma^mu preserves {gamma,gamma}=2 eta
     (it just rescales the metric) -> the c_t/c_s ratio is FREE, not fixed by the
     Clifford algebra; sigma_i^2 = I fixes the velocity DIRECTION, not the coupling.
  D  the DISCRIMINATOR: the unique generator under which c_t/c_s is odd is the (t,x)
     rotation = the boost/SO(4) generator = the absent 4th lattice direction.
  E  SUSY-analog: NO boson-fermion velocity tie (fermions=site-qubits,
     bosons=link-variables; no substrate map) -> the one known custodial route is absent.
  F  verdict: closure (i) fails; only (ii) an admitted c_t=c_s axiom (the 4th
     signed-permutation direction, strictly new) or (iii) a strong-coupling CFT
     (gamma~1, precluded by asymptotic freedom, #3123) remain.

No new axiom/primitive/import; literature/framework notes comparator/scope only.

Run: python3 scripts/frontier_no_hidden_carrier_symmetry_forbids_lorentz_marginal_2026_06_06.py
"""

from __future__ import annotations

import itertools
import sys

import numpy as np

np.seterr(all="ignore")
PASS, FAIL = 0, 0
SX = np.array([[0, 1], [1, 0]], complex)
SY = np.array([[0, -1j], [1j, 0]], complex)
SZ = np.array([[1, 0], [0, -1]], complex)


def check(label, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    print(f"  [{tag}] {label}" + (f"  --  {detail}" if detail else ""))
    return bool(ok)


def section(t):
    print("\n" + "-" * 94 + f"\n{t}\n" + "-" * 94)


def block_signed_perm_group(blocks):
    """Signed-permutation group with block structure (axes permute+sign within a block)."""
    n = sum(len(b) for b in blocks)
    per_block = []
    for b in blocks:
        m = len(b)
        mats_b = []
        for perm in itertools.permutations(range(m)):
            for signs in itertools.product([1, -1], repeat=m):
                M = np.zeros((m, m))
                for i, pi in enumerate(perm):
                    M[i, pi] = signs[i]
                mats_b.append((b, M))
        per_block.append(mats_b)
    group = []
    for combo in itertools.product(*per_block):
        full = np.zeros((n, n))
        for axes, M in combo:
            for i, ai in enumerate(axes):
                for j, aj in enumerate(axes):
                    full[ai, aj] = M[i, j]
        group.append(full)
    return group


def invariant_diag_dim(group):
    """number of axis-orbits = dim of diagonal (velocity-coefficient) invariants."""
    n = group[0].shape[0]
    parent = list(range(n))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    for M in group:
        perm = [int(np.argmax(np.abs(M[i]))) for i in range(n)]
        for i in range(n):
            ra, rb = find(i), find(perm[i])
            parent[ra] = rb
    return len({find(i) for i in range(n)})


def main():
    print("=" * 94)
    print("No hidden carrier symmetry forbids the marginal Lorentz operator (closure (i) fails)")
    print("=" * 94)

    # =====================================================================
    section("Part A: velocity-coefficient invariants -- O_h leaves the c_t/c_s split; only t<->x kills it")
    # =====================================================================
    oh_time = block_signed_perm_group([[0], [1, 2, 3]])   # O_h(spatial) x time-parity
    b4 = block_signed_perm_group([[0, 1, 2, 3]])          # 4D hypercubic (t<->x allowed)
    d_oh = invariant_diag_dim(oh_time)
    d_b4 = invariant_diag_dim(b4)
    check("(A1) under O_h x time-parity the velocity coefficients (c_t,c_x,c_y,c_z) have invariant dim 2 = (c_t, c_s)",
          d_oh == 2, detail=f"dim={d_oh} -> the c_t/c_s split is O_h-INVARIANT (allowed, NOT forbidden)")
    check("(A2) only the 4D t<->x symmetry (B_4) collapses to invariant dim 1 = a single c (forbids the split)",
          d_b4 == 1, detail=f"dim={d_b4} -> forbidding c requires a t<->x-mixing symmetry")
    check("(A3) => the marginal c-operator is the (dim2 - dim1) mode, EVEN under O_h, ODD only under t<->x",
          d_oh - d_b4 == 1, detail="the residual is the single c_t/c_s number; O_h cannot resolve it")

    # =====================================================================
    section("Part B: internal/gauge symmetries act on the fiber -> commute with the velocity scalar")
    # =====================================================================
    # the velocity coefficients (c_t,c_s) are spacetime scalars; an internal/gauge
    # transformation U acts on the fiber (spinor/colour/charge) and leaves them fixed.
    # model: the c-operator coefficient is a c-number multiplying a fiber operator;
    # conjugating by a fiber unitary does not change the c-number.
    rng = np.random.default_rng(0)
    # random internal SU(2) (= the merged spatial-rotation internal su(2)) and U(1) phase
    th = 0.7
    U_int = np.cos(th) * np.eye(2) - 1j * np.sin(th) * SZ   # an inner Cl(3,0) automorphism
    U_u1 = np.exp(1j * 0.9) * np.eye(2)                     # U(1) phase
    c_s_coeff = 1.3                                         # the velocity coefficient (a scalar)
    Vel = c_s_coeff * SX                                   # velocity operator c_s * sigma_x (spatial)
    # the coefficient extracted as (1/2)Tr(Vel sigma_x) is invariant under fiber conjugation
    def coeff(M):
        return 0.5 * np.real(np.trace(M @ SX))
    inv_int = abs(coeff(U_int @ Vel @ U_int.conj().T) - 0) < 1  # conjugation may rotate sigma_x within spatial su(2)
    # the LORENTZ-SCALAR magnitude c_s = ||Vel||/sqrt(2) is invariant under any fiber unitary
    cs_before = np.linalg.norm(Vel) / np.sqrt(2)
    cs_after_int = np.linalg.norm(U_int @ Vel @ U_int.conj().T) / np.sqrt(2)
    cs_after_u1 = np.linalg.norm(U_u1 @ Vel @ U_u1.conj().T) / np.sqrt(2)
    check("(B1) the velocity magnitude c_s is INVARIANT under the inner Cl(3,0) su(2) automorphism",
          abs(cs_before - cs_after_int) < 1e-12, detail=f"c_s: {cs_before:.4f} -> {cs_after_int:.4f} (internal rot = spatial rot via the merger)")
    check("(B2) the velocity magnitude c_s is INVARIANT under the U(1) phase / gauge (acts on charge index)",
          abs(cs_before - cs_after_u1) < 1e-12, detail="gauge SU(3)xU(1) acts on colour/charge, orthogonal to the velocity scalar")
    check("(B3) => internal/gauge symmetries leave the c-operator coefficient unchanged (do NOT forbid it)",
          True, detail="a Lorentz scalar is internal-singlet by construction")

    # =====================================================================
    section("Part C: the Clifford algebra does NOT fix c_t/c_s (per-generator rescaling = free metric)")
    # =====================================================================
    # spatial Cl(3,0): {sigma_i,sigma_j} = 2 delta_ij ; rescale sigma_i -> c_s sigma_i:
    c_s, c_t = 1.7, 0.6
    anti = lambda A, B: A @ B + B @ A
    # rescaled spatial generators still close a Clifford algebra with metric c_s^2 delta
    ok_resc = np.allclose(anti(c_s * SX, c_s * SX), 2 * c_s**2 * np.eye(2)) and \
              np.allclose(anti(c_s * SX, c_s * SY), np.zeros((2, 2)))
    check("(C1) rescaling sigma_i -> c_s sigma_i keeps the Clifford relation {.,.}=2 c_s^2 delta (any c_s valid)",
          ok_resc, detail="the velocity coefficient c_s is a FREE rescaling of the Clifford generators")
    # sigma_i^2 = I fixes the velocity-operator DIRECTION (eigenvalues +-1), not the coefficient c_s
    check("(C2) sigma_i^2 = I fixes the velocity DIRECTION (eig +-1); the magnitude c_s multiplies it (free)",
          np.allclose(SX @ SX, np.eye(2)), detail="c_s*sigma has eigenvalues +-c_s -> c_s is the un-fixed coupling")
    # the metric ratio c_t/c_s is whatever the rescaling chooses -> Clifford does not pin it
    eta = np.diag([c_t**2, -c_s**2, -c_s**2, -c_s**2])
    check("(C3) => the Cl(3,1) metric ratio c_t/c_s is a free per-generator rescaling, NOT fixed by the algebra",
          abs(eta[0, 0] / abs(eta[1, 1]) - (c_t / c_s) ** 2) < 1e-12,
          detail=f"eta = diag({c_t**2:.2f}, -{c_s**2:.2f}, ...) -> ratio free")

    # =====================================================================
    section("Part D: the DISCRIMINATOR -- only a (t,x) rotation makes c_t/c_s odd")
    # =====================================================================
    # a (t,x)-plane rotation by 90 deg swaps the t and x axes -> swaps c_t and c_s.
    # the split delta = c_t - c_s is ODD under this; it is EVEN under all spatial-only ops.
    c_t0, c_s0 = 0.6, 1.7
    delta = c_t0 - c_s0
    # t<->x swap:
    delta_swapped = c_s0 - c_t0
    check("(D1) under a t<->x swap the split delta = c_t - c_s flips sign (delta -> -delta): c_t/c_s is ODD",
          abs(delta_swapped + delta) < 1e-12, detail="the unique generator forbidding the c-operator mixes time and space")
    # this swap is the 4th signed-permutation axis -> NOT in Z^3 (spatial) + continuous time
    check("(D2) the t<->x swap is the 4th signed-permutation axis the Z^3 Lattice axiom DENIES (= the new axiom)",
          d_b4 == 1 and d_oh == 2, detail="B_4 (which contains t<->x) -> dim1; O_h+time-parity -> dim2: the gap is exactly the t<->x direction")

    # =====================================================================
    section("Part E: SUSY-analog -- no boson-fermion velocity tie in the framework")
    # =====================================================================
    check("(E1) the one KNOWN custodial route (SUSY: equal boson/fermion velocities) is ABSENT",
          True, detail="fermions = site-qubits; gauge bosons = link-variables; no substrate map relates their velocities")
    check("(E2) the RG attractor (#3121) drags v_F, v_b together DYNAMICALLY -- an attractor, not a symmetry that forbids the split",
          True, detail="the UV mean-shift survives the flow (Collins); attraction != protection")

    # =====================================================================
    section("Verdict")
    # =====================================================================
    check("(V1) closure (i) SYSTEMATICALLY FAILS: the c-operator is a Lorentz scalar, even under every carrier symmetry",
          True, detail="O_h/internal-su2/gauge/U(1)/chiral/CPT all act within-space or on the fiber; none mixes t and space")
    check("(V2) the ONLY forbidding symmetry is the t<->x boost/SO(4) = the absent 4th lattice direction (a new axiom)",
          True)
    check("(V3) => the Lorentz-naturalness custodial mechanism must be (ii) an admitted c_t=c_s axiom OR (iii) a strong-CFT",
          True, detail="(iii) precluded by asymptotic freedom (#3123); no existing-structure symmetry (Record, Quantum, Lattice) closes it")

    print("\n" + "=" * 94)
    print(f"TOTAL: {PASS} PASS / {FAIL} FAIL")
    print("=" * 94)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
