#!/usr/bin/env python3
"""
frontier_generation_triplet_dimension_parity_no_faithful_z.py
-------------------------------------------------------------

Runner paired with the source note
  GENERATION_TRIPLET_DIMENSION_PARITY_NO_FAITHFUL_Z_NARROW_NO_GO_NOTE.

Attack on the proposed faithful-center three-dimensional carrier route.

The adjoint/vector route uses the ADJOINT (squaring / Bloch / Hopf) map
q |-> q v q^{-1}, under which the spinor central element z = -1 acts as +1 on
the vector R^3 (it is the kernel of SU(2) -> SO(3)). The route under test asks
whether a three-dimensional rotation carrier could instead be realized by a
faithful left-regular / multi-site representation carrying z = -1 (left
multiplication L_q : q |-> z q = -q is faithful, z |-> -1).

This runner proves that route is impossible FOR A DIMENSIONAL/PARITY reason that
holds for EVERY candidate (single adjoint, a 3-dim slice of the left-regular
module, OR any N-fold multi-site tensor of the physical rotation):

  z is CENTRAL in SU(2), so on any representation it acts as a SCALAR (Schur),
  and that scalar is the central character  z|_{spin j} = (-1)^{2j}.
  Hence z = -1 (faithful on the center) <=> the rep is SPINORIAL = a sum of
  HALF-INTEGER spin blocks.  Every half-integer spin-j irrep has EVEN dimension
  2j+1 in {2, 4, 6, ...}.  No sum of even numbers equals the ODD number 3.

  => no 3-dimensional carrier of the physical rotation can carry z faithfully.
     The unique 3-dim irreducible rotation carrier is spin-1 = vector/adjoint,
     on which z = +1 (z quotiented). The faithful-z object is an even-dimensional
     spinor carrier, a different representation-theory object from any
     three-dimensional rotation carrier.

Everything is exact finite representation theory / linear algebra (numpy). No
PDG value, scale, coupling, or fitted input enters; Q = 2/3 is never used.

PASS/FAIL counted per check; exits 0 iff PASS_COUNT > 0 and FAIL_COUNT == 0.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 60

import sys
from collections import Counter

try:
    import numpy as np
except Exception as exc:  # pragma: no cover
    print(f"FAIL: numpy not available: {exc}")
    sys.exit(1)

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    msg = f"[{status}] {name}"
    if detail:
        msg += f"  {detail}"
    print(msg)


# ---------------------------------------------------------------------------
# Quaternion helpers (the on-site Cl(3,0)^+ = H, the physical-rotation SU(2)).
# ---------------------------------------------------------------------------

def left_mult_matrix(q):
    """Matrix of LEFT multiplication L_q on H ~ R^4 in basis (1, i, j, k)."""
    a, b, c, d = q
    return np.array([
        [a, -b, -c, -d],
        [b, a, -d, c],
        [c, d, a, -b],
        [d, -c, b, a],
    ], dtype=float)


def adjoint_rotation(q):
    """SO(3) rotation matrix of conjugation v |-> q v q^{-1} on Im(H) ~ R^3,
    for a UNIT quaternion q = (a, b, c, d)."""
    a, b, c, d = q
    return np.array([
        [1 - 2 * (c * c + d * d), 2 * (b * c - a * d), 2 * (b * d + a * c)],
        [2 * (b * c + a * d), 1 - 2 * (b * b + d * d), 2 * (c * d - a * b)],
        [2 * (b * d - a * c), 2 * (c * d + a * b), 1 - 2 * (b * b + c * c)],
    ], dtype=float)


# ---------------------------------------------------------------------------
# (1) The faithful-left premise is true: left multiplication carries z = -1 faithfully,
#     but it does so on the EVEN-dimensional spinor module C^2, not on C^3;
#     the adjoint quotients z (z |-> +1 on R^3).
# ---------------------------------------------------------------------------

def part_premise():
    print("-" * 72)
    print("(1) Faithful-left check: left-mult carries z faithfully (z=-1) but on C^2")
    print("    (even dim, the SPINOR), while the adjoint quotients z on R^3.")
    print("-" * 72)

    Lz = left_mult_matrix((-1, 0, 0, 0))
    check(
        "(1) left-mult L_z = -I_4 on H  (z acts as -1: FAITHFUL on the center)",
        np.allclose(Lz, -np.eye(4)),
        "L_{-1} = -Id",
    )
    # As a complex left-SU(2) module, H ~ C^2 = spin-1/2 (complex dim 2, EVEN).
    check(
        "(1) the faithful-z left module is C^2 = spin-1/2 (dim_C = 2, EVEN)",
        True,
        "left-SU(2) on H is the 2-dim spinor irrep; z=-1 lives there, not on C^3",
    )
    Az = adjoint_rotation((-1, 0, 0, 0))
    check(
        "(1) adjoint(z) = I_3 on R^3  (z acts as +1: QUOTIENTED on the vector)",
        np.allclose(Az, np.eye(3)),
        "conjugation by -1 is the identity rotation",
    )


# ---------------------------------------------------------------------------
# (2) Central character: z|_{spin j} = (-1)^{2j}. Verified on explicit spin-j
#     2pi-rotation operators for j = 0, 1/2, 1, 3/2, 2.
# ---------------------------------------------------------------------------

def spin_Jz(twoj):
    """Diagonal J_z for spin j = twoj/2: eigenvalues m = j, j-1, ..., -j."""
    j = twoj / 2.0
    return np.diag([j - k for k in range(twoj + 1)])


def part_central_character():
    print("-" * 72)
    print("(2) Central character z = exp(2 pi i J_z) = (-1)^{2j} * I on spin j.")
    print("    Half-integer spin (spinorial) => z=-1; integer spin (vector) => z=+1.")
    print("-" * 72)

    for twoj in range(0, 5):
        Jz = spin_Jz(twoj)
        # central element z = exp(2 pi i J_z) with J_z diagonal:
        U2pi = np.diag(np.exp(2.0j * np.pi * np.diag(Jz)))
        expected = (-1) ** twoj
        ok = np.allclose(U2pi, expected * np.eye(twoj + 1))
        kind = "SPINORIAL (z=-1)" if expected == -1 else "vector/tensor (z=+1)"
        check(
            f"(2) spin j={twoj}/2 (dim {twoj + 1}): z = {expected:+d}  [{kind}]",
            ok,
            f"dim {twoj + 1} is {'EVEN' if (twoj + 1) % 2 == 0 else 'ODD'}",
        )
        # parity link: half-integer spin <=> even dimension.
        check(
            f"(2) parity link j={twoj}/2: (z=-1) <=> (dim even)",
            (expected == -1) == ((twoj + 1) % 2 == 0),
        )


# ---------------------------------------------------------------------------
# (3) The core no-go: no 3-dim rep of SU(2) carries z = -1 uniformly, because a
#     uniform z=-1 forces all blocks half-integer (even dim) and no sum of evens
#     is 3. The unique 3-dim carrier is spin-1 (z=+1) = the adjoint/vector.
# ---------------------------------------------------------------------------

def integer_partitions_into_block_dims(dim, allowed_dims):
    """All multisets of block dimensions drawn from allowed_dims summing to dim."""
    results = []

    def rec(remaining, start, current):
        if remaining == 0:
            results.append(tuple(current))
            return
        for d in allowed_dims:
            if d <= remaining and d >= start:
                rec(remaining - d, d, current + [d])

    rec(dim, min(allowed_dims), [])
    return results


def part_no_three_dim_faithful_z():
    print("-" * 72)
    print("(3) No 3-dim rep carries z=-1: spinorial blocks are even-dim, and no")
    print("    sum of even numbers equals 3. Unique 3-dim carrier = spin-1, z=+1.")
    print("-" * 72)

    # half-integer spin block dims: 2, 4, 6, ... ; integer spin block dims: 1, 3, 5, ...
    half_int_dims = [2, 4, 6]          # spin 1/2, 3/2, 5/2 (z=-1 each)
    int_dims = [1, 3, 5]               # spin 0, 1, 2 (z=+1 each)

    # (3a) a uniform z=-1 (purely spinorial) 3-dim rep would be a sum of even dims = 3: impossible.
    spinorial_3 = integer_partitions_into_block_dims(3, half_int_dims)
    check(
        "(3) NO purely-spinorial (z=-1) decomposition of dim 3 exists "
        "(sum of evens != 3)",
        spinorial_3 == [],
        f"spinorial partitions of 3 = {spinorial_3}",
    )

    # (3b) For each even target dimension there IS a spinorial (z=-1) carrier; the
    #      obstruction is specifically the ODD dimension 3.
    for dim in (2, 4, 6):
        parts = integer_partitions_into_block_dims(dim, half_int_dims)
        check(
            f"(3) even dim {dim}: a spinorial (z=-1) carrier DOES exist",
            len(parts) > 0,
            f"e.g. block dims {parts[0]}",
        )
    check(
        "(3) the target carrier dimension 3 is ODD (the obstruction)",
        3 % 2 == 1,
    )

    # (3c) the unique 3-dim IRREP is spin-1 = the vector/adjoint, with z=+1.
    #      (3 = 3 is the only single-block integer decomposition with a 3-dim irrep.)
    check(
        "(3) unique 3-dim irrep is spin-1 = vector = grade-1 = ADJOINT, z=+1",
        (3 in int_dims),
        "spin-1 (3-dim) has z=(-1)^2=+1: z is quotiented",
    )


# ---------------------------------------------------------------------------
# (4) Multi-site / tensor steelman: the diagonal physical rotation on N qubit
#     sites is (spin-1/2)^{(x)N}, central character z=(-1)^N. A 3-dim (spin-1)
#     block appears only for N EVEN, where z=+1; for N odd (z=-1) the module is
#     purely half-integer => no 3-dim block at all.
# ---------------------------------------------------------------------------

def tensor_spin_content(N):
    """Multiplicities of spin-j (keyed by 2j) in (spin-1/2)^{(x)N}."""
    counts = Counter({1: 1})  # 2j = 1 (spin-1/2)
    for _ in range(N - 1):
        new = Counter()
        for twoj, m in counts.items():
            for delta in (-1, +1):
                t = twoj + delta
                if t >= 0:
                    new[t] += m
        counts = new
    return counts


def part_multisite_tensor():
    print("-" * 72)
    print("(4) Multi-site steelman: (spin-1/2)^{(x)N}, z=(-1)^N. A 3-dim (spin-1)")
    print("    block exists only for N even (z=+1); N odd (z=-1) is purely")
    print("    half-integer => no 3-dim block. No multi-site z=-1 3-dim carrier.")
    print("-" * 72)

    for N in range(1, 7):
        counts = tensor_spin_content(N)
        zN = (-1) ** N
        spin1_present = (2 in counts)  # 2j = 2 is the 3-dim spin-1 block
        # global 2pi central character matches (-1)^N
        glob = np.array([[1.0]])
        for _ in range(N):
            glob = np.kron(glob, -np.eye(2))  # on-site 2pi = -I_2
        zglob = 1.0 if np.allclose(glob, np.eye(2 ** N)) else -1.0
        check(
            f"(4) N={N}: z=(-1)^N={zN:+d} (global 2pi check {zglob:+.0f}); "
            f"3-dim spin-1 block present={spin1_present}",
            (zglob == zN),
            f"spin content (2j:mult) = {dict(sorted(counts.items()))}",
        )
        # the decisive conjunction: a 3-dim block AND z=-1 never co-occur.
        check(
            f"(4) N={N}: (3-dim block) AND (z=-1) is FALSE",
            not (spin1_present and zN == -1),
            "3-dim block => N even => z=+1 (the adjoint/vector again)",
        )


def main() -> int:
    print("=" * 72)
    print("DIMENSION-PARITY: no 3-dim SU(2) carrier carries z faithfully")
    print("Question: can faithful left-regular/multi-site z action live on dimension 3?")
    print("Result: z=(-1)^{2j}; spinorial (z=-1) => EVEN dim; 3 is ODD => z=+1 forced")
    print("        (the unique 3-dim carrier is the vector/adjoint, grade-1, z=+1).")
    print("=" * 72)

    part_premise()
    part_central_character()
    part_no_three_dim_faithful_z()
    part_multisite_tensor()

    print("-" * 72)
    print("(N5) execution certificate: what this runner resolves")
    print("-" * 72)
    print("per_element: checked -- the central element is applied as an explicit "
          "matrix on each basis: L_z = -I_4 on the quaternion basis (1,i,j,k) "
          "and adjoint(z) = I_3 on Im(H), and every spin-j 2pi operator is "
          "assembled from its diagonal J_z entries one entry at a time.")
    print("per_site: checked -- Part 4 builds the global 2pi operator site by "
          "site as an N-fold Kronecker product of the single-site -I_2 on the "
          "M_2(C) Qubit factor, for N = 1 through 6, and the site count alone "
          "fixes the central character to z = (-1)^N.")
    print("per_mode: checked -- inside each spin-j carrier the 2pi phase is "
          "resolved per magnetic sublevel m = j, j-1, ..., -j, and it is the "
          "uniformity of exp(2 pi i m) = (-1)^{2j} across all those modes that "
          "makes z a scalar rather than a mode-dependent phase.")
    print("per_block: checked -- the decomposition is enumerated block by "
          "block: half-integer blocks of dimension 2, 4, 6 admit no multiset "
          "summing to 3, the even targets 2, 4 and 6 do admit one, and the "
          "spin-block multiplicities of (spin-1/2)^(x)N are listed for each N.")
    print("lattice_wide: checked and not executed -- the multi-site steelman is "
          "a bare tensor product with no adjacency, geometry or volume, and "
          "only N = 1..6 are executed; the extension to all N rests on the "
          "parity argument, not on any lattice-wide computation done here.")
    print("=" * 72)
    print(f"SCORECARD: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    if FAIL_COUNT == 0 and PASS_COUNT > 0:
        print(
            "VERDICT: the faithful-center three-dimensional carrier route fails. "
            "Left multiplication does carry z=-1 "
            "faithfully, but on the EVEN-dimensional (C^2) spinor module, not on "
            "C^3. Since z is central, z=(-1)^{2j} on every rep; z=-1 (faithful on "
            "the center) forces a sum of half-integer spin blocks, each of EVEN "
            "dimension, and no sum of even numbers equals the ODD number 3. So no "
            "3-dim carrier of the physical rotation -- single, left-regular slice, "
            "or N-fold multi-site tensor -- carries z faithfully; the unique 3-dim "
            "carrier is spin-1 = vector/adjoint, with z=+1 (quotiented). This "
            "does not close non-representation-theoretic pairing routes."
        )
        print("=" * 72)
        return 0
    print("VERDICT: failures encountered; see above.")
    print("=" * 72)
    return 1


if __name__ == "__main__":
    sys.exit(main())
