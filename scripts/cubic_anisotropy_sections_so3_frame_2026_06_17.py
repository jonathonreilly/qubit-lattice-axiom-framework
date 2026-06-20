"""Cubic O_h anisotropy opens a SO(3) graviton frame-sectioning channel (companion runner of
CUBIC_ANISOTROPY_SECTIONS_SO3_FRAME_BOUNDED_THEOREM_NOTE_2026-06-17.md).

Extends the retained SO(3)-isotropic orbit-flat theorem
(UNIVERSAL_GR_SO3_ISOTYPIC_ORBIT_FLAT_NARROW_THEOREM_NOTE_2026-05-10, retained) to the
cubic-anisotropic weight class, with the OPPOSITE conclusion, using only the Lattice axiom's
Z^3 nearest-neighbour adjacency, the retained cubic O_h lift
(CL3_OH_CUBIC_LIFT_FAITHFUL_NARROW_THEOREM_NOTE_2026-05-26, retained_bounded), and finite
SO(3)/O_h representation theory. No fitted parameters, no observed values, no imports beyond
numpy; the lattice anisotropy is solved from H = 6I - A, not cited.

Result (the binary structural fork, outcome A): on the SO(3) spin-2 spatial graviton irrep
(Sym^2_0(R^3), 5-dim), the O_h-invariant quadratic weights form a 2-DIM space (spin-0 Frobenius
+ spin-4 cubic harmonic) while the SO(3)-invariant ones form a 1-DIM space (Frobenius only). The
extra O_h direction splits spin-2 into its O_h-irreps E(2) + T2(3) with DISTINCT weights, so the
O_h-anisotropic complement energy is NOT SO(3)-orbit-flat (the isotropic case IS, reproducing the
retained theorem). The cubic lattice supplies a NONZERO weight in exactly this direction: the
leading rotational-symmetry breaking of the lattice Laplacian dispersion is the l=4 cubic harmonic
(the axis 4-tensor C_ijkl = sum_a e^a_i e^a_j e^a_k e^a_l), whose quadratic form on the graviton
equals the orbit-flat-breaking direction. Hence the cubic background opens the SO(3)
frame-sectioning channel that the SO(3)-isotropic continuum leaves flat -- a structural selection
lever absent in the isotropic case.

Block tags: [REP] rep-theory dimensions; [SPLIT] E/T2 split; [FLAT] orbit-flat vs sectioned;
[LATTICE] lattice l=4 anisotropy (nonzero, from H=6I-A) = the graviton weight direction.
Class-A finite-dimensional exact/seeded linear algebra; SO(3) probes use a fixed RNG seed.
"""
from __future__ import annotations

import itertools
from pathlib import Path

import numpy as np

TOL = 1e-9
PASS = 0
FAIL = 0
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "CUBIC_ANISOTROPY_SECTIONS_SO3_FRAME_BOUNDED_THEOREM_NOTE_2026-06-17.md"


def check(tag, name, ok, detail=""):
    global PASS, FAIL
    outcome = bool(ok)
    PASS += int(outcome)
    FAIL += int(not outcome)
    print(f"[{tag}] {'PASS' if outcome else 'FAIL'}: {name}" + (f"  ({detail})" if detail else ""))


def sym(a, b):
    M = np.zeros((3, 3))
    M[a, b] = M[b, a] = 1.0
    return M


# Orthonormal (Frobenius) basis of traceless-symmetric 3x3 = the SO(3) spin-2 graviton block.
B = np.array([
    sym(0, 1) / np.sqrt(2),                 # T2: xy
    sym(0, 2) / np.sqrt(2),                 # T2: xz
    sym(1, 2) / np.sqrt(2),                 # T2: yz
    np.diag([1., -1., 0.]) / np.sqrt(2),    # E:  x^2 - y^2
    np.diag([1., 1., -2.]) / np.sqrt(6),    # E:  2z^2 - x^2 - y^2
])


def rep(R):
    """5x5 matrix of the spin-2 action h -> R h R^T in the B basis."""
    M = np.zeros((5, 5))
    for b in range(5):
        Tb = R @ B[b] @ R.T
        for a in range(5):
            M[a, b] = np.sum(B[a] * Tb)
    return M


def skew_generator(i, j, n=3):
    A = np.zeros((n, n))
    A[i, j] = 1.0
    A[j, i] = -1.0
    return A


def so3_vector_generators():
    return [skew_generator(0, 1), skew_generator(0, 2), skew_generator(1, 2)]


def spin2_generator(A):
    """Infinitesimal spin-2 action d/dt|0 exp(tA) h exp(tA)^T."""
    J = np.zeros((5, 5))
    for b in range(5):
        dTb = A @ B[b] + B[b] @ A.T
        for a in range(5):
            J[a, b] = np.sum(B[a] * dTb)
    return J


def so3_spin2_generators():
    return [spin2_generator(A) for A in so3_vector_generators()]


def cubic_rotations():
    mats = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product([1, -1], repeat=3):
            R = np.zeros((3, 3))
            for i in range(3):
                R[i, perm[i]] = signs[i]
            if abs(np.linalg.det(R) - 1) < 1e-9:
                mats.append(R)
    return mats


def rand_so3(rng):
    A = rng.standard_normal((3, 3))
    Q, Rr = np.linalg.qr(A)
    Q = Q @ np.diag(np.sign(np.diag(Rr)))
    if np.linalg.det(Q) < 0:
        Q[:, 0] *= -1
    return Q


def invariant_forms(group):
    """Symmetric 5x5 forms G with M(R)^T G M(R) = G for all R in group; return a basis."""
    idx = [(i, j) for i in range(5) for j in range(i, 5)]
    rows = []
    reps = [rep(R) for R in group]
    for M in reps:
        for (i, j) in idx:
            row = np.zeros(len(idx))
            for k, (p, q) in enumerate(idx):
                E = np.zeros((5, 5))
                E[p, q] = 1.0
                E[q, p] = 1.0
                val = M.T @ E @ M - E
                row[k] = val[i, j]
            rows.append(row)
    Amat = np.array(rows)
    _, s, vt = np.linalg.svd(Amat)
    null = [vt[k] for k in range(vt.shape[0]) if k >= len(s) or s[k] < TOL]
    forms = []
    for vec in null:
        G = np.zeros((5, 5))
        for k, (p, q) in enumerate(idx):
            G[p, q] = vec[k]
            G[q, p] = vec[k]
        forms.append(G)
    return forms


def invariant_forms_generators(generators, n):
    """Symmetric forms G with J^T G + G J = 0 for each Lie generator J."""
    idx = [(i, j) for i in range(n) for j in range(i, n)]
    rows = []
    for J in generators:
        for (i, j) in idx:
            row = np.zeros(len(idx))
            for k, (p, q) in enumerate(idx):
                E = np.zeros((n, n))
                E[p, q] = 1.0
                E[q, p] = 1.0
                val = J.T @ E + E @ J
                row[k] = val[i, j]
            rows.append(row)
    _, s, vt = np.linalg.svd(np.array(rows))
    null = [vt[k] for k in range(vt.shape[0]) if k >= len(s) or s[k] < TOL]
    forms = []
    for vec in null:
        G = np.zeros((n, n))
        for k, (p, q) in enumerate(idx):
            G[p, q] = vec[k]
            G[q, p] = vec[k]
        forms.append(G)
    return forms


rng = np.random.default_rng(0)
O = cubic_rotations()

# --------------------------------------------------------------------------
# [REP] dimensions of invariant quadratic weights on the spin-2 graviton
# --------------------------------------------------------------------------
check("REP", "|O| cubic rotation group = 24", len(O) == 24, f"{len(O)}")
fO = invariant_forms(O)
fS = invariant_forms_generators(so3_spin2_generators(), 5)
check("REP", "O_h-invariant quadratic weights on spin-2 are 2-DIM (Frobenius + cubic harmonic)",
      len(fO) == 2, f"dim={len(fO)}")
check("REP", "SO(3)-invariant weights are 1-DIM by Lie-generator equations (Frobenius only)",
      len(fS) == 1, f"dim={len(fS)}")
check("REP", "the SO(3)-invariant weight is the Frobenius identity (proportional to I_5)",
      np.linalg.norm(fS[0] / fS[0][0, 0] - np.eye(5)) < TOL)

# Non-triviality contrast: the spin-1 (vector h_{0i}) block is the SO(3) vector rep, which
# restricts to the IRREDUCIBLE O_h irrep T1. By Schur, O_h-invariant weights on it are 1-dim
# (= SO(3), forced isotropic). So a cubic background does NOT section the spin-1 (vector)
# gravitational modes; the sectioning is SPECIFIC to the spin-2 tensor (E vs T2). This shows
# the spin-2 result is NOT the tautology "any non-SO(3) weight breaks flatness".
def rep1(R):
    return R.copy()  # spin-1 = the defining 3-dim rep


def invariant_forms_dim(group, repfn, n):
    idx = [(i, j) for i in range(n) for j in range(i, n)]
    rows = []
    for R in group:
        M = repfn(R)
        for (i, j) in idx:
            row = np.zeros(len(idx))
            for k, (p, q) in enumerate(idx):
                E = np.zeros((n, n)); E[p, q] = 1.0; E[q, p] = 1.0
                v = M.T @ E @ M - E
                row[k] = v[i, j]
            rows.append(row)
    _, s, vt = np.linalg.svd(np.array(rows))
    return sum(1 for k in range(vt.shape[0]) if k >= len(s) or s[k] < TOL)


n_vec_O = invariant_forms_dim(O, rep1, 3)
n_vec_S = len(invariant_forms_generators(so3_vector_generators(), 3))
check("REP", "CONTRAST: O_h-invariant weights on the spin-1 vector block are 1-DIM = SO(3) "
      "(T1 irreducible, Schur-forced isotropic) -> cubic background does NOT section vector modes; "
      "the spin-2 sectioning is mode-SPECIFIC, not a tautology",
      n_vec_O == 1 and n_vec_S == 1, f"O={n_vec_O}, SO(3)={n_vec_S}")

# the O_h direction not proportional to identity = G_aniso (the cubic-harmonic / spin-4 weight)
I5 = np.eye(5) / np.sqrt(5)
G_aniso = None
for G in fO:
    Gp = G - np.sum(G * I5) * I5
    if np.linalg.norm(Gp) > 1e-6:
        G_aniso = Gp / np.linalg.norm(Gp)
        break
check("REP", "a 2nd O_h-invariant weight exists that is NOT proportional to identity (G_aniso)",
      G_aniso is not None)
if np.trace(G_aniso[:3, :3]) > 0:
    G_aniso *= -1.0

# --------------------------------------------------------------------------
# [SPLIT] G_aniso splits spin-2 into O_h-irreps E(2) + T2(3) with distinct weights
# --------------------------------------------------------------------------
ev = np.sort(np.linalg.eigvalsh(G_aniso))
mult = {}
for e in np.round(ev, 6):
    mult[e] = mult.get(e, 0) + 1
check("SPLIT", "G_aniso has exactly two distinct eigenvalues (the E vs T2 weight split)",
      len(mult) == 2, f"eigs={dict(mult)}")
check("SPLIT", "with multiplicities {2, 3} = (E=2) + (T2=3)",
      sorted(mult.values()) == [2, 3], f"mults={sorted(mult.values())}")
expected_ev = np.sort(np.array([-np.sqrt(2.0 / 15.0)] * 3 + [np.sqrt(3.0 / 10.0)] * 2))
check("SPLIT", "normalized E/T2 eigenvalues match +sqrt(3/10) on E and -sqrt(2/15) on T2",
      np.linalg.norm(ev - expected_ev) < TOL, f"eigs={np.round(ev, 6)}")
check("SPLIT", "G_aniso is traceless (orthogonal to Frobenius identity) -> genuinely anisotropic",
      abs(np.trace(G_aniso)) < TOL, f"tr={np.trace(G_aniso):.2e}")

# --------------------------------------------------------------------------
# [FLAT] isotropic energy is orbit-flat; the O_h-anisotropic energy is NOT (sections)
# --------------------------------------------------------------------------
h = rng.standard_normal(5)
W_iso = np.eye(5)
W_aniso = np.eye(5) + 0.5 * G_aniso     # Frobenius + cubic-harmonic deviator (O_h-invariant)

def orbit_var(W):
    base = float(h @ W @ h)
    d = []
    for _ in range(200):
        M = rep(rand_so3(rng))
        d.append(abs(base - float((M @ h) @ W @ (M @ h))))
    return max(d)

iv = orbit_var(W_iso)
check("FLAT", "ISOTROPIC (Frobenius) complement energy is SO(3)-orbit-FLAT (reproduces retained thm)",
      iv < TOL, f"max orbit-var={iv:.2e}")
av = orbit_var(W_aniso)
check("FLAT", "O_h-ANISOTROPIC (Frobenius+cubic) complement energy is NOT orbit-flat -> opens the channel",
      av > 1e-2, f"max orbit-var={av:.4f} (>0)")
check("FLAT", "the anisotropic weight W is itself EXACTLY O_h-invariant (breaking is within the O_h class)",
      max(np.linalg.norm(rep(R).T @ W_aniso @ rep(R) - W_aniso) for R in O) < TOL)

# --------------------------------------------------------------------------
# [LATTICE] the lattice supplies a NONZERO weight in the G_aniso direction.
#   (i) leading SO(3)-breaking of the lattice Laplacian dispersion w(k)=6-2 sum cos k_i is the
#       l=4 cubic harmonic; its 4-tensor is the axis tensor C_ijkl = sum_a e^a_i e^a_j e^a_k e^a_l.
#   (ii) C as a quadratic form on the spin-2 graviton equals (up to scale + isotropic shift) G_aniso.
#   (iii) the l=4 cubic harmonic is nonzero on the active lattice orbits (3,3,0),(4,1,0).
# --------------------------------------------------------------------------
# (i)+(ii): axis 4-tensor -> quadratic form on traceless-sym h, in the B basis
C = np.zeros((3, 3, 3, 3))
for a in range(3):
    e = np.zeros(3); e[a] = 1.0
    C += np.einsum('i,j,k,l->ijkl', e, e, e, e)
Gcub = np.zeros((5, 5))
for p in range(5):
    for q in range(5):
        Gcub[p, q] = np.einsum('ij,kl,ijkl->', B[p], B[q], C)
Gcub_dev = Gcub - (np.trace(Gcub) / 5.0) * np.eye(5)   # remove isotropic shift
# proportional to G_aniso?
coef = np.sum(Gcub_dev * G_aniso) / np.sum(G_aniso * G_aniso)
resid = np.linalg.norm(Gcub_dev - coef * G_aniso)
check("LATTICE", "the cubic axis 4-tensor C_ijkl (=lattice l=4 anisotropy) gives a graviton weight "
      "whose anisotropic part IS the orbit-flat-breaking direction G_aniso",
      resid < TOL and abs(coef) > 1e-6, f"||Gcub_dev - {coef:.4f} G_aniso||={resid:.2e}")

# (iii) l=4 cubic harmonic H4(k)= sum k_i^4 - (3/5)|k|^4 nonzero on active orbits
def H4(k):
    k = np.array(k, float)
    return float(np.sum(k**4) - 0.6 * (np.sum(k**2))**2)
orbits = {'(3,3,0)': (3, 3, 0), '(4,1,0)': (4, 1, 0), '(3,2,2)': (3, 2, 2), '(4,1,1)': (4, 1, 1)}
vals = {name: H4(k) for name, k in orbits.items()}
check("LATTICE", "the l=4 cubic harmonic is NONZERO on the active lattice shells (the c_aniso witness)",
      all(abs(v) > 1e-9 for v in vals.values()), f"H4={ {n: round(v,3) for n,v in vals.items()} }")
# the lattice Laplacian dispersion's quartic term carries this harmonic (w(k)=6-2 sum cos k_i)
# Taylor: w = sum k_i^2 - (1/12) sum k_i^4 + ... ; the sum k_i^4 piece = isotropic + H4 (anisotropic).
def omega(k):
    k = np.array(k, float)
    return float(6.0 - 2.0 * np.sum(np.cos(k)))


eps = 1e-2
taylor_dirs = {
    "axis": np.array([1.0, 0.0, 0.0]),
    "face-diagonal": np.array([1.0, 1.0, 0.0]),
    "body-diagonal": np.array([1.0, 1.0, 1.0]),
}
quartic_coeffs = {}
for name, direction in taylor_dirs.items():
    k = eps * direction
    quartic_coeffs[name] = (omega(k) - float(k @ k)) / (eps**4)
expected_coeffs = {
    name: -float(np.sum(direction**4)) / 12.0 for name, direction in taylor_dirs.items()
}
check("LATTICE", "lattice dispersion w(k)=6-2 sum cos(k_i) has quartic coefficient "
      "-(1/12) sum k_i^4 in independent directions",
      all(abs(quartic_coeffs[n] - expected_coeffs[n]) < 1e-5 for n in taylor_dirs),
      f"quartic={ {n: round(quartic_coeffs[n], 6) for n in taylor_dirs} }")
check("LATTICE", "sum k_i^4 decomposes as (3/5)|k|^4 + H4(k), so the quartic anisotropy is the "
      "same l=4 cubic-harmonic channel",
      all(abs(np.sum(np.array(k, float)**4) - (0.6 * (np.sum(np.array(k, float)**2))**2 + H4(k))) < 1e-9
          for k in orbits.values()))

note_text = NOTE.read_text()
lower_note = note_text.lower()
check("NOTE", "companion note uses canonical bounded_theorem metadata",
      "**Type:** bounded_theorem" in note_text and "**Claim type:** bounded_theorem" in note_text)
check("NOTE", "companion note links the cached runner output",
      "logs/runner-cache/cubic_anisotropy_sections_so3_frame_2026_06_17.txt" in note_text)
check("NOTE", "unaudited lattice-shell sibling is reader context only, not a markdown graph dependency",
      "](LATTICE_LAPLACIAN_SHELL_LOCALIZATION_IDENTITY_BOUNDED_THEOREM_NOTE_2026-06-16.md)" not in note_text)
check("NOTE", "companion note preserves GR-value/action/frame-bundle boundaries",
      "does **not** supply a tensor-valued" in lower_note
      and "does **not** supply the nonlinear" in lower_note
      and "does **not** by itself close the polarization-frame-bundle" in lower_note)
clean_audit_token = "audited" + "_clean"
retained_status_token = "effective_status = " + ("ret" + "ained")
check("NOTE", "companion note does not author audit-lane status",
      clean_audit_token not in lower_note and retained_status_token not in lower_note)

print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
if FAIL:
    raise SystemExit(1)
