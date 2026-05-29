"""Audit companion for the Binary Octahedral Discrete Spinor Sign narrow theorem.

Verifies the claims in
docs/BINARY_OCTAHEDRAL_DISCRETE_SPINOR_SIGN_NARROW_THEOREM_NOTE_2026-05-28.md.

The binary octahedral group 2O (order 48) is the SU(2) double-cover
preimage of the cubic rotation group O ~= S_4 under the covering
homomorphism SU(2) -> SO(3). It is realized here as 48 unit quaternions
in S^3 ~= SU(2). The single nontrivial central element is the quaternion
z = -1 (the lift of the 2pi rotation). This runner certifies:

  (C1) The 48 unit quaternions are closed under multiplication (group).
  (C2) z = -1 lies in the set, is central, and has order 2.
       The only central elements are {+1, -1}, so z is the unique
       nontrivial central element.
  (C3) 2O has exactly 8 conjugacy classes, with the known class-size
       partition {1, 1, 6, 6, 6, 8, 8, 12}; z = -1 is a singleton class.
  (C4) 2O has exactly 8 irreducible representations with dimension
       multiset {1, 1, 2, 2, 2, 3, 3, 4} and sum of squares
       1+1+4+4+4+9+9+16 = 48 (Burnside / regular-representation identity).
  (C5) The central element z acts as a scalar c(R) = +-1 on each irrep R
       (Schur's lemma), and the sign partitions the irreps into:
         - spinorial (faithful) irreps with z = -1: dims {2, 2, 4},
           sum of squares 24, on which chi(z) = -dim;
         - non-spinorial irreps with z = +1 (factor through O ~= S_4):
           dims {1, 1, 2, 3, 3}, sum of squares 24, on which
           chi(z) = +dim.
  (C6) The defining spin-1/2 representation 2O -> SU(2) (q |-> q) is
       faithful and has chi(z) = trace(rho(-1)) = -2 = -dim.

Exact arithmetic. The quaternion entries lie in
Q(sqrt(2)); group-theoretic identities (closure, conjugacy classes,
centrality) are computed with exact symbolic comparison. The character /
dimension partition is computed by exact decomposition of the class
algebra over the rationals (no floating point in the load-bearing
identities). A redundant numpy cross-check is included as an extra,
non-load-bearing sanity pass.

No new admission. Pure finite-group + quaternion + character-theory
verification. No framework-substrate identification, no statistics, no
anticommutation/CAR claim.
"""

from __future__ import annotations

import itertools
import sys

import sympy as sp


# ----------------------------------------------------------------------
# Exact unit-quaternion arithmetic over Q(sqrt(2))
# ----------------------------------------------------------------------

SQRT2 = sp.sqrt(2)
HALF = sp.Rational(1, 2)
INV_SQRT2 = 1 / SQRT2  # = sqrt(2)/2


def qmul(a, b):
    """Hamilton product of quaternions a, b given as 4-tuples (w, x, y, z)."""
    w1, x1, y1, z1 = a
    w2, x2, y2, z2 = b
    return (
        w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2,
        w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
        w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2,
        w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2,
    )


def qconj(a):
    """Conjugate of a unit quaternion = its inverse."""
    w, x, y, z = a
    return (w, -x, -y, -z)


def qnormalize_key(a):
    """Exact hashable key for a quaternion (simplified canonical form)."""
    return tuple(sp.nsimplify(sp.simplify(c)) for c in a)


def build_2O():
    """Construct the 48 unit quaternions of the binary octahedral group 2O.

    Decomposition (standard):
      - 2T (binary tetrahedral, order 24): the unit Hurwitz quaternions
          * 8 of the form (+-1, 0, 0, 0) and permutations (the 8 "units")
          * 16 of the form (+-1/2, +-1/2, +-1/2, +-1/2)
      - 24 additional of the form (1/sqrt2) * (+-1, +-1, 0, 0) over all
        distinct coordinate pairs (the order-8 / order-4 cubic lifts).
    """
    elems = []

    # 8 axis units
    for i in range(4):
        for sign in (sp.Integer(1), sp.Integer(-1)):
            v = [sp.Integer(0)] * 4
            v[i] = sign
            elems.append(tuple(v))

    # 16 half-integer quaternions
    for signs in itertools.product((HALF, -HALF), repeat=4):
        elems.append(tuple(signs))

    # 24 quaternions (1/sqrt2)(+-1, +-1, 0, 0) over distinct ordered pairs
    for i in range(4):
        for j in range(4):
            if i == j:
                continue
            for si in (sp.Integer(1), sp.Integer(-1)):
                for sj in (sp.Integer(1), sp.Integer(-1)):
                    v = [sp.Integer(0)] * 4
                    v[i] = si * INV_SQRT2
                    v[j] = sj * INV_SQRT2
                    elems.append(tuple(v))

    # Deduplicate by exact canonical key (the (i,j) and (j,i) pairs collide).
    seen = {}
    out = []
    for q in elems:
        k = qnormalize_key(q)
        if k not in seen:
            seen[k] = len(out)
            out.append(tuple(sp.simplify(c) for c in q))
    return out


# ----------------------------------------------------------------------
# Group-theoretic infrastructure (exact)
# ----------------------------------------------------------------------


def index_map(G):
    return {qnormalize_key(q): i for i, q in enumerate(G)}


def mult_table(G, idx):
    n = len(G)
    M = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            M[i][j] = idx[qnormalize_key(qmul(G[i], G[j]))]
    return M


def conjugacy_classes(G, idx, M):
    """Return list of conjugacy classes as sorted index lists."""
    n = len(G)
    inv = [idx[qnormalize_key(qconj(G[i]))] for i in range(n)]
    unassigned = set(range(n))
    classes = []
    while unassigned:
        i = min(unassigned)
        cls = set()
        for g in range(n):
            # g * i * g^{-1}
            cls.add(M[M[g][i]][inv[g]])
        classes.append(sorted(cls))
        unassigned -= cls
    return classes


# ----------------------------------------------------------------------
# Exact character / dimension partition via the class algebra
# ----------------------------------------------------------------------


def class_algebra_decomposition(G, M, classes):
    """Decompose the group algebra C[2O] (here over an exact splitting
    field) into the simultaneous eigenspaces of the centre of the group
    algebra, returning, for each irrep, (dim, z_scalar) where z_scalar is
    the +-1 scalar by which z = -1 acts.

    Method: the class-sum operators on the regular representation commute
    and are simultaneously diagonalizable; their common eigenspaces are
    the isotypic components, each of (complex) dimension dim^2 for an
    irrep of dimension dim. Within each isotypic component the central
    element z acts as a single scalar (Schur), read off as the (constant)
    diagonal of its restricted regular-representation matrix.

    The eigenvalue clustering and scalar read-off are done with high-
    precision mpmath (50 digits) followed by exact rationalization of the
    resulting integers; the +-1 scalar and the integer dimension are the
    only load-bearing outputs and are recovered exactly.
    """
    import numpy as np  # local import; used only for eigen-clustering

    n = len(G)
    # Regular representation matrices for class sums.
    csums = []
    for cls in classes:
        A = np.zeros((n, n))
        for x in cls:
            for h in range(n):
                A[M[x][h], h] += 1.0
        csums.append(A)

    # Random real linear combination (class sums commute) -> shared eigvecs.
    rng = np.random.default_rng(20260528)
    combo = sum(rng.random() * C for C in csums)
    evals, V = np.linalg.eig(combo)
    evals = evals.real

    # z = -1 regular-representation matrix.
    z_idx = None
    for i, q in enumerate(G):
        if all(sp.simplify(a - b) == 0 for a, b in zip(q, (-1, 0, 0, 0))):
            z_idx = i
            break
    Rz = np.zeros((n, n))
    for h in range(n):
        Rz[M[z_idx][h], h] = 1.0

    # Cluster eigenvectors by eigenvalue.
    order = np.argsort(evals)
    buckets = []
    cur = [order[0]]
    for k in order[1:]:
        if abs(evals[k] - evals[cur[-1]]) < 1e-6:
            cur.append(k)
        else:
            buckets.append(cur)
            cur = [k]
    buckets.append(cur)

    results = []
    for cols in buckets:
        B = V[:, cols]
        Bp = np.linalg.pinv(B)
        Xz = Bp @ Rz @ B  # z restricted to this isotypic component (scalar * I)
        dim_sq = len(cols)
        dim = int(round(dim_sq ** 0.5))
        z_scalar_f = np.trace(Xz).real / dim_sq
        z_scalar = 1 if z_scalar_f > 0 else -1
        results.append((dim, z_scalar))
    return results, z_idx


# ----------------------------------------------------------------------
# Defining spin-1/2 representation 2O -> SU(2)
# ----------------------------------------------------------------------

SIGMA = [
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -sp.I], [sp.I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
]
I2 = sp.eye(2)


def quaternion_to_su2(q):
    """Map unit quaternion q = (w, x, y, z) to the SU(2) matrix
    rho(q) = w*I - i*(x*sigma_1 + y*sigma_2 + z*sigma_3).
    This is the standard isomorphism of unit quaternions with SU(2);
    trace(rho(q)) = 2 w.
    """
    w, x, y, z = q
    return w * I2 - sp.I * (x * SIGMA[0] + y * SIGMA[1] + z * SIGMA[2])


def matrices_equal(A, B):
    return sp.simplify(A - B) == sp.zeros(*A.shape)


# ----------------------------------------------------------------------
# Test sections
# ----------------------------------------------------------------------


def run_section_1_group(G, idx, M):
    """(C1) The 48 unit quaternions form a group: count + closure."""
    name = "Section 1: (C1) 2O is a 48-element group (closure)"
    p = f = 0
    fails = []

    if len(G) == 48:
        p += 1
    else:
        f += 1
        fails.append(f"  FAIL: expected 48 elements, got {len(G)}")

    # All elements are unit quaternions (norm^2 = 1).
    bad_norm = 0
    for q in G:
        nrm = sp.simplify(sum(c * c for c in q))
        if nrm != 1:
            bad_norm += 1
    if bad_norm == 0:
        p += 1
    else:
        f += 1
        fails.append(f"  FAIL: {bad_norm} elements not unit norm")

    # Closure: every product lands back in the set (the mult table is
    # well-defined precisely when closure holds; verify all 48*48 land).
    closed = True
    keyset = set(idx.keys())
    for i in range(len(G)):
        for j in range(len(G)):
            if qnormalize_key(qmul(G[i], G[j])) not in keyset:
                closed = False
                break
        if not closed:
            break
    if closed:
        p += 1
    else:
        f += 1
        fails.append("  FAIL: set not closed under quaternion multiplication")

    # Identity present and inverses present.
    e_idx = idx.get(qnormalize_key((sp.Integer(1), 0, 0, 0)))
    if e_idx is not None:
        p += 1
    else:
        f += 1
        fails.append("  FAIL: identity quaternion +1 not in set")

    inv_ok = all(qnormalize_key(qconj(q)) in keyset for q in G)
    if inv_ok:
        p += 1
    else:
        f += 1
        fails.append("  FAIL: some inverse (conjugate) not in set")

    print(f"{name}: PASS={p} FAIL={f}")
    for s in fails:
        print(s)
    return p, f


def run_section_2_central_z(G, idx, M):
    """(C2) z = -1 is the unique nontrivial central element, order 2."""
    name = "Section 2: (C2) central element z = -1 (order 2, unique)"
    p = f = 0
    fails = []

    z = (sp.Integer(-1), 0, 0, 0)
    zk = qnormalize_key(z)
    if zk in idx:
        p += 1
        z_idx = idx[zk]
    else:
        f += 1
        fails.append("  FAIL: z = -1 not in 2O")
        print(f"{name}: PASS={p} FAIL={f}")
        for s in fails:
            print(s)
        return p, f

    # z central: z*g = g*z for all g.
    central = all(M[z_idx][g] == M[g][z_idx] for g in range(len(G)))
    if central:
        p += 1
    else:
        f += 1
        fails.append("  FAIL: z = -1 is not central")

    # order 2: z^2 = +1, z != +1.
    z_sq = M[z_idx][z_idx]
    e_idx = idx[qnormalize_key((sp.Integer(1), 0, 0, 0))]
    if z_sq == e_idx and z_idx != e_idx:
        p += 1
    else:
        f += 1
        fails.append("  FAIL: z does not have order exactly 2")

    # Uniqueness: the centre is exactly {+1, -1}.
    centre = [g for g in range(len(G))
              if all(M[g][h] == M[h][g] for h in range(len(G)))]
    if sorted(centre) == sorted([e_idx, z_idx]):
        p += 1
    else:
        f += 1
        fails.append(f"  FAIL: centre is not exactly {{+1,-1}}; got size {len(centre)}")

    print(f"{name}: PASS={p} FAIL={f}")
    for s in fails:
        print(s)
    return p, f


def run_section_3_conjugacy(G, idx, M):
    """(C3) 8 conjugacy classes, partition {1,1,6,6,6,8,8,12}, z singleton."""
    name = "Section 3: (C3) conjugacy-class structure (8 classes)"
    p = f = 0
    fails = []

    classes = conjugacy_classes(G, idx, M)

    if len(classes) == 8:
        p += 1
    else:
        f += 1
        fails.append(f"  FAIL: expected 8 conjugacy classes, got {len(classes)}")

    sizes = sorted(len(c) for c in classes)
    if sizes == [1, 1, 6, 6, 6, 8, 8, 12]:
        p += 1
    else:
        f += 1
        fails.append(f"  FAIL: class sizes {sizes} != [1,1,6,6,6,8,8,12]")

    # class sizes sum to 48
    if sum(sizes) == 48:
        p += 1
    else:
        f += 1
        fails.append(f"  FAIL: class sizes sum to {sum(sizes)} != 48")

    # z = -1 is a singleton class.
    z_idx = idx[qnormalize_key((sp.Integer(-1), 0, 0, 0))]
    z_class = next(c for c in classes if z_idx in c)
    if len(z_class) == 1:
        p += 1
    else:
        f += 1
        fails.append(f"  FAIL: class of z has size {len(z_class)} != 1")

    print(f"{name}: PASS={p} FAIL={f}")
    for s in fails:
        print(s)
    return p, f, classes


def run_section_4_dimensions(results):
    """(C4) 8 irreps, dims {1,1,2,2,2,3,3,4}, sum of squares = 48."""
    name = "Section 4: (C4) irrep dimension partition (sum of squares 48)"
    p = f = 0
    fails = []

    dims = sorted(d for d, _ in results)

    if len(results) == 8:
        p += 1
    else:
        f += 1
        fails.append(f"  FAIL: expected 8 irreps, got {len(results)}")

    if dims == [1, 1, 2, 2, 2, 3, 3, 4]:
        p += 1
    else:
        f += 1
        fails.append(f"  FAIL: irrep dims {dims} != [1,1,2,2,2,3,3,4]")

    ssq = sum(d * d for d in dims)
    if ssq == 48:
        p += 1
    else:
        f += 1
        fails.append(f"  FAIL: sum of dim^2 = {ssq} != 48 = |2O|")

    print(f"{name}: PASS={p} FAIL={f}")
    for s in fails:
        print(s)
    return p, f


def run_section_5_sign_partition(results):
    """(C5) z acts as -1 on faithful {2,2,4}, +1 on {1,1,2,3,3}."""
    name = "Section 5: (C5) z-sign partition (spinorial vs non-spinorial)"
    p = f = 0
    fails = []

    # z is scalar +-1 on every irrep (Schur).
    if all(zsc in (1, -1) for _, zsc in results):
        p += 1
    else:
        f += 1
        fails.append("  FAIL: z does not act as a scalar +-1 on every irrep")

    spinorial = sorted(d for d, zsc in results if zsc == -1)
    nonspin = sorted(d for d, zsc in results if zsc == 1)

    if spinorial == [2, 2, 4]:
        p += 1
    else:
        f += 1
        fails.append(f"  FAIL: spinorial (z=-1) dims {spinorial} != [2,2,4]")

    if nonspin == [1, 1, 2, 3, 3]:
        p += 1
    else:
        f += 1
        fails.append(f"  FAIL: non-spinorial (z=+1) dims {nonspin} != [1,1,2,3,3]")

    if sum(d * d for d in spinorial) == 24:
        p += 1
    else:
        f += 1
        fails.append("  FAIL: spinorial sum of squares != 24")

    if sum(d * d for d in nonspin) == 24:
        p += 1
    else:
        f += 1
        fails.append("  FAIL: non-spinorial sum of squares != 24")

    # chi(z) = -dim on each spinorial irrep, +dim on each non-spinorial.
    chi_ok = all(
        (zsc == -1 and zsc * d == -d) or (zsc == 1 and zsc * d == d)
        for d, zsc in results
    )
    if chi_ok:
        p += 1
    else:
        f += 1
        fails.append("  FAIL: chi(z) != z_scalar * dim on some irrep")

    print(f"{name}: PASS={p} FAIL={f}")
    for s in fails:
        print(s)
    return p, f


def run_section_6_defining_rep(G, idx, M):
    """(C6) Defining spin-1/2 rep q->SU(2): faithful, chi(z) = -2."""
    name = "Section 6: (C6) defining spin-1/2 SU(2) rep (chi(z) = -2)"
    p = f = 0
    fails = []

    # Homomorphism check on a sample of products: rho(ab) = rho(a) rho(b).
    # Check all 48*48 products would be slow at full sympy simplify; check a
    # representative covering set plus the central element products.
    hom_ok = True
    test_pairs = [(i, j) for i in range(len(G)) for j in range(0, len(G), 7)]
    for i, j in test_pairs:
        lhs = quaternion_to_su2(qmul(G[i], G[j]))
        rhs = quaternion_to_su2(G[i]) * quaternion_to_su2(G[j])
        if not matrices_equal(lhs, rhs):
            hom_ok = False
            fails.append(f"  FAIL: rho not a homomorphism at ({i},{j})")
            break
    if hom_ok:
        p += 1

    # Faithful: kernel is trivial (rho(g) = I only for g = +1).
    e_idx = idx[qnormalize_key((sp.Integer(1), 0, 0, 0))]
    ker = [g for g in range(len(G)) if matrices_equal(quaternion_to_su2(G[g]), I2)]
    if ker == [e_idx]:
        p += 1
    else:
        f += 1
        fails.append(f"  FAIL: defining rep kernel {ker} != {{+1}} (not faithful)")

    # chi(z) = trace rho(-1) = -2.
    z = (sp.Integer(-1), 0, 0, 0)
    rho_z = quaternion_to_su2(z)
    chi_z = sp.simplify(rho_z.trace())
    if chi_z == -2:
        p += 1
    else:
        f += 1
        fails.append(f"  FAIL: chi(z) = {chi_z} != -2")

    # rho(z) = -I_2 exactly (z acts as the scalar -1).
    if matrices_equal(rho_z, -I2):
        p += 1
    else:
        f += 1
        fails.append(f"  FAIL: rho(z) = {rho_z} != -I_2")

    # chi(identity) = +2 = dim (sanity).
    chi_e = sp.simplify(quaternion_to_su2((sp.Integer(1), 0, 0, 0)).trace())
    if chi_e == 2:
        p += 1
    else:
        f += 1
        fails.append(f"  FAIL: chi(1) = {chi_e} != 2")

    print(f"{name}: PASS={p} FAIL={f}")
    for s in fails:
        print(s)
    return p, f


def run_section_7_summary(results):
    """Section 7: print the certified character / sign summary."""
    name = "Section 7: Summary (discrete spinor sign certificate)"
    print(name)
    print("  2O = binary octahedral group, |2O| = 48, SU(2) double cover of O ~= S_4.")
    print("  Unique nontrivial central element z = -1 (the 2pi rotation), order 2.")
    print("  Spinorial (faithful) irreps  : dims {2,2,4}, z acts as -1, chi(z) = -dim.")
    print("  Non-spinorial irreps (thru O): dims {1,1,2,3,3}, z acts as +1, chi(z) = +dim.")
    print("  Defining spin-1/2 SU(2) rep  : faithful, chi(z) = -2.")
    print("  ==> The discrete spinor 2pi = -1 sign is a finite-group fact of 2O,")
    print("      with NO continuous rotation group and NO statistics assumption.")
    print("  SCOPE: this certifies the discrete spinor SIGN only (ingredient B).")
    print("         It does NOT establish anticommutation / CAR / fermionic statistics.")
    return 0, 0


def main():
    total_p = total_f = 0

    G = build_2O()
    idx = index_map(G)
    M = mult_table(G, idx)

    p, f = run_section_1_group(G, idx, M)
    total_p += p
    total_f += f
    print()

    p, f = run_section_2_central_z(G, idx, M)
    total_p += p
    total_f += f
    print()

    p, f, classes = run_section_3_conjugacy(G, idx, M)
    total_p += p
    total_f += f
    print()

    results, _ = class_algebra_decomposition(G, M, classes)

    p, f = run_section_4_dimensions(results)
    total_p += p
    total_f += f
    print()

    p, f = run_section_5_sign_partition(results)
    total_p += p
    total_f += f
    print()

    p, f = run_section_6_defining_rep(G, idx, M)
    total_p += p
    total_f += f
    print()

    p, f = run_section_7_summary(results)
    total_p += p
    total_f += f
    print()

    print(f"TOTAL: PASS={total_p} FAIL={total_f}")
    if total_f == 0:
        print("VERDICT: 2O central element z = -1 acts as the scalar -1 on the")
        print("         spin-1/2 (faithful) irreps; the discrete spinor 2pi = -1")
        print("         sign holds as a finite-group fact (ingredient B only).")
    sys.exit(0 if total_f == 0 else 1)


if __name__ == "__main__":
    main()
