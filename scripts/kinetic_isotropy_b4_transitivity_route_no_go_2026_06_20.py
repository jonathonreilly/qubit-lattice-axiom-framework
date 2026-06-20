#!/usr/bin/env python3
"""
Route no-go for deriving kinetic isotropy (c_t = c_s) from B4/S4
transitivity.

CLAIM (route boundary, NOT a primitive update). The registered kinetic-isotropy
primitive remains the approved structural OS0 kinetic-form isotropy c_t = c_s.
This runner certifies three structural facts showing that a derivation route
which treats the four Euclidean axes as already B4/S4-equivalent is circular:
the missing time-space metric symmetry is equivalent to the target equality.

It does NOT derive c_t = c_s and does NOT retire or narrow the approved
primitive. A future non-circular metric-layer theorem may still derive the
same equality.

THREE CHECKS:

(C1) THE INVARIANT-DIMENSION WALL. On the space of quadratic diagonal kinetic
     forms (coefficients of p_mu^2), the spatial cubic group O_h (signed
     permutations of the 3 spatial axes, time fixed; |O_h| = 48) leaves a
     TWO-dimensional invariant space (c_t and c_s independent). Only the full
     hypercubic group B4 (signed permutations of all 4 axes; |B4| = 384)
     collapses it to ONE dimension (c_t = c_s). Exact Reynolds-projector rank
     over Q, on the full 10-dim space of symmetric 4x4 matrices and on the
     4-dim diagonal subspace.

(C2) THE CIRCULARITY CERTIFICATE. The generator that extends O_h to B4 is the
     time-space axis swap W. With the kinetic metric G = diag(c_t,c_s,c_s,c_s),
     a purely spatial swap is a symmetry of G for ALL (c_t,c_s) [so O_h is
     automatic], but the time-space swap W satisfies
         W^T G W - G = diag(c_s - c_t, c_t - c_s, 0, 0),
     which vanishes IFF c_t = c_s. Hence "the 4 axes are B4/S4-equivalent" is
     LOGICALLY IDENTICAL to the conclusion c_t = c_s, not antecedent to it:
     every B4/S4-transitivity route to isotropy is circular. Exact sympy.

(C3) POSITIVE-TRANSFER WITNESS. On a geometrically square lattice (a = 1 on
     all four axes), an anisotropic free Euclidean scalar with c_t != c_s can
     have positive one-step transfer eigenvalues and PSD Osterwalder-Schrader
     reflection Gram matrices on the tested finite mode grid. This refutes the
     route "square geometry plus reflection positivity selects c_t = c_s";
     it is not a replacement normalization theorem.

Class-A, finite-dimensional, deterministic. Expected: TOTAL: PASS=N FAIL=0.
"""

from itertools import permutations, product
from pathlib import Path
import numpy as np
import sympy as sp

PASS = 0
FAIL = 0
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/KINETIC_ISOTROPY_B4_TRANSITIVITY_ROUTE_NO_GO_2026-06-20.md"


def check(name, ok, detail=""):
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))


def banner(t):
    print("\n" + "=" * 76 + f"\n{t}\n" + "=" * 76)


# ---------------------------------------------------------------------------
# Group builders: signed-permutation matrices (exact integer entries).
# axes ordered (t, x, y, z) = (0,1,2,3).
# ---------------------------------------------------------------------------
def signed_perm_matrices(perm_indices, sign_axes):
    """All signed-permutation 4x4 matrices whose underlying permutation permutes
    the index set `perm_indices` (others fixed) and whose sign flips range over
    subsets of `sign_axes`."""
    mats = []
    fixed = [i for i in range(4) if i not in perm_indices]
    for perm in permutations(perm_indices):
        # base permutation: perm_indices[k] -> perm[k]; fixed axes stay
        mapping = {src: dst for src, dst in zip(perm_indices, perm)}
        for f in fixed:
            mapping[f] = f
        for signs in product((1, -1), repeat=len(sign_axes)):
            M = sp.zeros(4, 4)
            sgn = {ax: s for ax, s in zip(sign_axes, signs)}
            for src in range(4):
                dst = mapping[src]
                M[dst, src] = sgn.get(src, 1)
            mats.append(M)
    return mats


def dedup(mats):
    seen = {}
    for M in mats:
        seen[sp.ImmutableMatrix(M)] = M
    return list(seen.values())


# O_h: spatial cubic = signed perms of {x,y,z}, time fixed (no time flip). |O_h|=48
O_h = dedup(signed_perm_matrices([1, 2, 3], [1, 2, 3]))
# B4: full hypercubic = signed perms of all four axes. |B4| = 2^4 * 4! = 384
B4 = dedup(signed_perm_matrices([0, 1, 2, 3], [0, 1, 2, 3]))


# ---------------------------------------------------------------------------
# C1 -- the invariant-dimension wall (exact Reynolds rank over Q)
# ---------------------------------------------------------------------------
banner("C1  invariant-dimension wall:  O_h -> 2,  B4 -> 1")

check("|O_h| = 48", len(O_h) == 48, f"got {len(O_h)}")
check("|B4| = 384", len(B4) == 384, f"got {len(B4)}")

# basis of symmetric 4x4 matrices (10-dim)
sym_basis = []
for i in range(4):
    for j in range(i, 4):
        E = sp.zeros(4, 4)
        E[i, j] += 1
        E[j, i] += 1
        sym_basis.append(E)  # E[i,i] becomes 2 on diagonal; fine as a basis elt


def vec_sym(M):
    """Coordinate vector of a symmetric matrix in the 10-dim basis (upper tri)."""
    out = []
    for i in range(4):
        for j in range(i, 4):
            out.append(M[i, j])
    return sp.Matrix(out)


def reynolds_invariant_dim(group, restrict_diagonal=False):
    """dim of the space of symmetric matrices S with g S g^T = S for all g."""
    # Build averaging operator on the 10-dim symmetric space, then rank of (R) =
    # dim of its image = invariant dim (R is a projector).
    n = len(sym_basis)
    cols = []
    for B in sym_basis:
        acc = sp.zeros(4, 4)
        for g in group:
            acc += g * B * g.T
        acc = acc / len(group)
        cols.append(vec_sym(acc))
    R = sp.Matrix.hstack(*cols)  # 10x10 projector matrix (columns = images)
    if restrict_diagonal:
        # project further onto diagonal forms: keep only invariant matrices that
        # are diagonal. Compute invariant space basis then intersect with diagonal.
        # Simpler: average diagonal basis vectors and rank those.
        diag_basis = []
        for i in range(4):
            E = sp.zeros(4, 4)
            E[i, i] += 1
            diag_basis.append(E)
        dcols = []
        for B in diag_basis:
            acc = sp.zeros(4, 4)
            for g in group:
                acc += g * B * g.T
            acc = acc / len(group)
            dcols.append(vec_sym(acc))
        return sp.Matrix.hstack(*dcols).rank()
    return R.rank()


dim_Oh_sym = reynolds_invariant_dim(O_h)
dim_B4_sym = reynolds_invariant_dim(B4)
dim_Oh_diag = reynolds_invariant_dim(O_h, restrict_diagonal=True)
dim_B4_diag = reynolds_invariant_dim(B4, restrict_diagonal=True)

check("O_h invariant symmetric-matrix dim = 2", dim_Oh_sym == 2, f"got {dim_Oh_sym}")
check("B4 invariant symmetric-matrix dim = 1", dim_B4_sym == 1, f"got {dim_B4_sym}")
check("O_h invariant DIAGONAL-form dim = 2 (c_t, c_s independent)",
      dim_Oh_diag == 2, f"got {dim_Oh_diag}")
check("B4 invariant DIAGONAL-form dim = 1 (c_t = c_s forced)",
      dim_B4_diag == 1, f"got {dim_B4_diag}")

# Exhibit the O_h invariants explicitly: diag(1,0,0,0) and diag(0,1,1,1) are O_h-
# invariant; their time-space mix is what B4 forbids.
ct, cs = sp.symbols("c_t c_s", positive=True)
G = sp.diag(ct, cs, cs, cs)
oh_inv = all(sp.simplify(g * G * g.T - G) == sp.zeros(4, 4) for g in O_h)
check("G = diag(c_t,c_s,c_s,c_s) is O_h-invariant for symbolic c_t != c_s",
      oh_inv, "every spatial signed-perm fixes G")


# ---------------------------------------------------------------------------
# C2 -- the circularity certificate (exact symbolic)
# ---------------------------------------------------------------------------
banner("C2  circularity certificate:  time-space swap symmetric  <=>  c_t = c_s")

# spatial swap x<->y (in O_h): symmetry of G for ALL c_t,c_s
W_xy = sp.zeros(4, 4)
W_xy[0, 0] = 1
W_xy[1, 2] = 1
W_xy[2, 1] = 1
W_xy[3, 3] = 1
spatial_def = sp.simplify(W_xy.T * G * W_xy - G)
check("spatial swap x<->y is a G-symmetry for ALL (c_t,c_s) [O_h automatic]",
      spatial_def == sp.zeros(4, 4), "defect identically 0")
check("spatial swap is in B4 and in O_h",
      any(W_xy == g for g in B4) and any(W_xy == g for g in O_h), "")

# time-space swap t<->x : the generator extending O_h to B4
W_tx = sp.zeros(4, 4)
W_tx[0, 1] = 1
W_tx[1, 0] = 1
W_tx[2, 2] = 1
W_tx[3, 3] = 1
defect = sp.simplify(W_tx.T * G * W_tx - G)
expected = sp.diag(cs - ct, ct - cs, 0, 0)
check("time-space swap defect  W^T G W - G = diag(c_s-c_t, c_t-c_s, 0, 0)",
      sp.simplify(defect - expected) == sp.zeros(4, 4), f"defect = {defect.tolist()}")

sol = sp.solve(sp.Eq(defect, sp.zeros(4, 4)), [ct], dict=True)
# defect == 0 reduces to c_t = c_s
zero_cond = sp.simplify(defect.subs(ct, cs))
check("defect vanishes IFF c_t = c_s",
      zero_cond == sp.zeros(4, 4) and sp.simplify((cs - ct)) != 0,
      "substituting c_t->c_s kills the defect; nonzero otherwise")

check("time-space swap is in B4 but NOT in O_h (the missing generator)",
      any(W_tx == g for g in B4) and not any(W_tx == g for g in O_h), "")

# Therefore: assuming any B4 element that moves the time axis is a G-symmetry
# already assumes c_t = c_s. The S4/B4-transitivity route is circular as a class.


# ---------------------------------------------------------------------------
# C3 -- layer-independence: anisotropic c_t != c_s is reflection-positive on a
#       geometrically square (a=1) lattice => r is not fixed by geometry/cone/RP
# ---------------------------------------------------------------------------
banner("C3  positive-transfer witness: c_t != c_s is RP-positive on a square lattice")


def transfer_eig(ct_v, cs_v, m2, kvec):
    """Smaller root lambda in (0,1) of  c_t (lambda + 1/lambda - 2) = E(k),
    E(k) = c_s sum (2 - 2 cos k_i) + m^2.  Returns lambda(k)."""
    E = cs_v * sum(2 - 2 * np.cos(k) for k in kvec) + m2
    # c_t lambda^2 - (2 c_t + E) lambda + c_t = 0
    b = 2 * ct_v + E
    disc = b * b - 4 * ct_v * ct_v
    lam = (b - np.sqrt(disc)) / (2 * ct_v)
    return lam, E


def rp_gram_min_eig(ct_v, cs_v, m2, kvec, nslices=6):
    """OS reflection Gram M_ij = G(t_i + t_j; k), t_i = 1..nslices, with
    G(tau;k) ~ lambda^{|tau|}. PSD <=> reflection positive in that mode."""
    lam, _ = transfer_eig(ct_v, cs_v, m2, kvec)
    ts = np.arange(1, nslices + 1)
    M = lam ** (ts[:, None] + ts[None, :])
    w = np.linalg.eigvalsh(M)
    return lam, w.min()

# anisotropic: c_t = 2.5, c_s = 1.0  (xi = c_t/c_s = 2.5, genuinely LV)
CT, CS, M2 = 2.5, 1.0, 0.10
kmodes = [(kx, ky, kz)
          for kx in np.linspace(0, np.pi, 4)
          for ky in np.linspace(0, np.pi, 4)
          for kz in np.linspace(0, np.pi, 4)]

lam_ok = True
gram_ok = True
worst_gram = np.inf
for kv in kmodes:
    lam, E = transfer_eig(CT, CS, M2, kv)
    if not (0.0 < lam < 1.0):
        lam_ok = False
    _, mineig = rp_gram_min_eig(CT, CS, M2, kv)
    worst_gram = min(worst_gram, mineig)
    if mineig < -1e-10:
        gram_ok = False

check("anisotropic (c_t=2.5, c_s=1): transfer eigenvalue lambda(k) in (0,1) for all modes",
      lam_ok, "positive one-step transfer")
check("anisotropic: OS reflection Gram PSD for all modes (reflection positive)",
      gram_ok, f"worst min-eigenvalue = {worst_gram:.2e}")

# sanity: the isotropic case is ALSO RP-positive -> RP holds across the family,
# so RP does not select isotropy.
iso_lam_ok = all(0.0 < transfer_eig(1.7, 1.7, M2, kv)[0] < 1.0 for kv in kmodes)
check("isotropic (c_t=c_s=1.7) also RP-positive -> positivity is not unique to isotropy",
      iso_lam_ok, "positive-transfer witness stays non-selective")

# the anisotropy is genuinely Lorentz-violating: small-k front speeds differ.
# continuum dispersion c_t w^2 = c_s |k|^2 => speed^2 = c_s/c_t != 1.
speed2 = CS / CT
check("anisotropy is genuinely Lorentz-violating: front-speed^2 = c_s/c_t != 1",
      abs(speed2 - 1.0) > 1e-6, f"speed^2 = {speed2}")


# ---------------------------------------------------------------------------
banner("SOURCE NOTE GUARD")
note_text = NOTE.read_text(encoding="utf-8")
flat_note = " ".join(note_text.split())
required_note_tokens = [
    "**Claim type:** no_go",
    "This note does not amend, narrow, retire, or re-approve that primitive.",
    "deriving `c_t = c_s` by treating the four Euclidean axes as already `B4`/`S4`-equivalent is circular",
    "Gate result: PASS for this narrow route no-go.",
    "The approved primitive is unchanged and not retired here.",
]
check("source note states the narrow route no-go and preserves the primitive",
      all(token in flat_note for token in required_note_tokens),
      "note wording guard")
forbidden_note_tokens = [
    "shrink the primitive",
    "primitive being reduced",
    "already-admitted",
    "lone surviving metric-layer residual",
]
check("source note does not ship primitive-reduction or admission-ladder language",
      all(token not in note_text for token in forbidden_note_tokens),
      "governance wording guard")


# ---------------------------------------------------------------------------
banner("SUMMARY")
print("C1: the diagonal-form invariant space is 2-dim under O_h, 1-dim under B4 ->")
print("    deriving c_t=c_s == supplying the O_h->B4 (time-space) generator.")
print("C2: that generator is a metric symmetry IFF c_t=c_s -> every B4/S4-")
print("    transitivity argument for isotropy is CIRCULAR as a class.")
print("C3: a c_t!=c_s free-scalar witness is reflection-positive on a square")
print("    lattice, so square geometry plus RP does not select c_t=c_s.")
print("NET: the B4/S4 transitivity route is circular as a derivation of kinetic")
print("     isotropy. The approved primitive is unchanged and not retired here.")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
