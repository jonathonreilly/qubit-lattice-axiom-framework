"""Global-color orientation of the matter state is predictively vacuous.

Context. The gauge-link / color-einselection campaign's admissions-collapse note
converged on TWO irreducible gauge-structure admissions, one of which is the
GLOBAL color-singlet / Gauss-law physical-state condition on the matter color
density rho_color on the irreducible fundamental carrier C^3. That collapse note
recorded that "the realized matter STATE is a global SU(3) singlet" is NOT
entailed by "observables are SU(3)-invariant".

This runner makes the RETIRE-MODE refinement of the global color-neutrality
admission. The data carried by a color state rho splits, under the global SU(3)
action rho -> U(g) rho U(g)^dag, into:

  * its ORIENTATION  -- the position of rho within its SU(3) orbit, and
  * its INVARIANT content -- the spectrum / Casimirs of rho (purity Tr rho^2,
    including the Tr rho^2 - 1/3 purity order parameter).

PREMISE (named, conditional). The color observable algebra is the SU(3)-invariant
subalgebra (the gauge principle: observables commute with the global SU(3)
action). The color SU(3) itself is the retained commutant structure of
graph_first_su3_integration_note; "observables are SU(3)-invariant" is the
corpus-standard reading under which the global color-neutrality admission is
even posed.

THEOREM (orientation retirement / predictive equivalence). Conditional on the
premise, for every state rho, every g in SU(3), and every observable O:

        Tr( U(g) rho U(g)^dag  O ) = Tr( rho  O ).

Hence every record-level consequence (a scalar readout of an observable) is
invariant under a global SU(3) rotation of the state: the ORIENTATION component
of the global color-neutrality admission is predictively vacuous -- requiring a
particular color orientation (a named color frame / direction) is a retire-able
source proposal, not a physical admission. What is NOT retired is the INVARIANT content: the
spectrum / purity of rho_color is preserved by the rotation and remains
observable-distinguishable via two-copy invariants (Part B's registrable
surface). So the admission splits into ORIENTATION (retired here) plus PURITY
(the genuine residual).

r-DIAL TEETH (the load-bearing guard). The same argument must NOT force the
Koide block-weight r. It cannot: the global color SU(3) acts only on the color
tensor factor; the generation/mass pattern (which carries r) is color-singlet
and is left pointwise fixed. r is an SU(3)-invariant of the state, NOT an
orientation coordinate -- so the orientation-retirement blade (which retires a
flat gauge direction along which an exact symmetry acts) touches no invariant
and hence cannot touch r. Observables DO depend on r (the mass pattern) and do
NOT depend on color orientation; the asymmetry is exactly that color orientation
has an exact symmetry group (SU(3)) making it gauge, while r has none.

NO campaign residual discharged: this retires ORIENTATION data of the STATE; it delivers no
frame, no partition, no twirl weight, and no depolarization -- purity is
untouched. It does not deliver a LOCAL connection, so it does not discharge or
short-circuit the static local color-frame redundancy.

All checks are exact finite-dimensional linear algebra on C^3, C^3 (x) C^3, and
the gen (x) color space C^3 (x) C^3; random SU(3) elements with a fixed seed are
witnesses for already-proven identities, NOT Monte-Carlo fits in the logic path.
Memory-safe (<= 9x9 dense only; no inverses of large matrices).
"""

import numpy as np

PASS = 0
FAIL = 0
TOL = 1e-10


def check(name, cond):
    global PASS, FAIL
    if cond:
        PASS += 1
        print(f"PASS  {name}")
    else:
        FAIL += 1
        print(f"FAIL  {name}")


def haar_unitary(n, rng):
    z = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))) / np.sqrt(2.0)
    q, r = np.linalg.qr(z)
    d = np.diagonal(r)
    return q @ np.diag(d / np.abs(d))


def special_unitary(n, rng):
    U = haar_unitary(n, rng)
    root = np.exp(1j * np.angle(np.linalg.det(U)) / n)
    return U / root


def rand_density(n, rng):
    a = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n)))
    rho = a @ a.conj().T
    return rho / np.trace(rho).real


def gell_mann():
    l = []
    l.append(np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], complex))
    l.append(np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], complex))
    l.append(np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], complex))
    l.append(np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], complex))
    l.append(np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], complex))
    l.append(np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], complex))
    l.append(np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], complex))
    l.append(np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], complex) / np.sqrt(3.0))
    return l


I3 = np.eye(3)
GM = gell_mann()
rng = np.random.default_rng(160160)


def commutant_dim(reps):
    """dim of the algebra of operators commuting with all generators in `reps`,
    each acting on the same C^d, via the null space of stacked [O, X] = 0."""
    d = reps[0].shape[0]
    rows = []
    for X in reps:
        # vec([X,O]) = (I (x) X - X^T (x) I) vec(O)
        rows.append(np.kron(I3 if d == 3 else np.eye(d), X) - np.kron(X.T, np.eye(d)))
    M = np.vstack(rows)
    # complex null space dimension
    s = np.linalg.svd(M, compute_uv=False)
    return int(np.sum(s < 1e-9))


# ---------------------------------------------------------------------------
# Color commutant checks. 3 (x) 3bar = 8 (+) 1: bilinears in the ADJOINT are non-observable; the
#     singlet (number operator) is the only invariant; commutant = scalars.
# ---------------------------------------------------------------------------
g = special_unitary(3, rng)
check("color commutant 1: g in SU(3) (unitary, det=1)",
      np.max(np.abs(g.conj().T @ g - I3)) < TOL and abs(np.linalg.det(g) - 1) < TOL)

# adjoint action g X g^dag preserves the traceless (8) subspace and fixes I (1)
X = sum(rng.standard_normal() * m for m in GM)          # traceless Hermitian
check("color commutant 2: adjoint preserves traceless 8-block (tr stays 0)",
      abs(np.trace(g @ X @ g.conj().T)) < TOL)
check("color commutant 3: singlet (identity / number operator) is fixed",
      np.max(np.abs(g @ I3 @ g.conj().T - I3)) < TOL)

# an off-diagonal fundamental bilinear E_12 = a1^dag a2 lives in the adjoint:
# it is NOT invariant -> NOT an observable
E12 = np.zeros((3, 3), complex)
E12[0, 1] = 1.0
check("color commutant 4: off-diagonal bilinear E_12 (adjoint) is NOT SU(3)-invariant",
      np.max(np.abs(g @ E12 @ g.conj().T - E12)) > 1e-3)

# single-carrier SU(3)-invariant observable algebra = scalars (Schur, dim 1)
check("color commutant 5: single-carrier color commutant = scalars (Schur, dim 1)",
      commutant_dim(GM) == 1)

# ---------------------------------------------------------------------------
# Predictive-equivalence checks: every SU(3)-invariant observable O gives identical
#     expectations on rho and on U(g) rho U(g)^dag. Demonstrated on a two-carrier
#     space C^3 (x) C^3 where the invariant algebra is non-trivial; O is built
#     exactly (aI + b*SWAP) and a set of SU(3) elements WITNESSES that it commutes
#     with the rep (no averaging / no twirl is performed -- this set is a
#     commutation witness, not a depolarizing average).
# ---------------------------------------------------------------------------
su3_witnesses = [special_unitary(3, rng) for _ in range(12)]
# A genuinely (exactly) SU(3)-invariant observable on C^3 (x) C^3: O = aI + b*SWAP
# commutes with every g (x) g (SWAP intertwines the two identical carriers).
SWAP = np.zeros((9, 9), complex)
for i in range(3):
    for j in range(3):
        SWAP[3 * i + j, 3 * j + i] = 1.0
O_exact = 0.7 * np.eye(9) + 1.3 * SWAP                  # commutes with every g(x)g
check("predictive equivalence 1: O = aI + b*SWAP is exactly SU(3)-invariant on C^3(x)C^3",
      all(np.max(np.abs(O_exact @ G - G @ O_exact)) < TOL
          for G in [np.kron(h, h) for h in su3_witnesses]))

max_dev = 0.0
for _ in range(8):
    h = special_unitary(3, rng)
    carrier_rotation = np.kron(h, h)
    rho = rand_density(9, rng)
    rho_rot = carrier_rotation @ rho @ carrier_rotation.conj().T
    dev = abs(np.trace(rho @ O_exact).real - np.trace(rho_rot @ O_exact).real)
    max_dev = max(max_dev, dev)
check("predictive equivalence 2: <O>_rho = <O>_{g rho g} for invariant O (exact)",
      max_dev < TOL)

# ---------------------------------------------------------------------------
# Purity-residual checks. ORIENTATION moves but the INVARIANT content (spectrum / purity) is fixed;
#     every SU(3)-invariant of rho is a function of its spectrum (orientation-
#     blind). Two SU(3)-related states agree on the two-copy purity; a different-
#     spectrum state is DISTINGUISHED by purity -> purity is the residual.
# ---------------------------------------------------------------------------
rho = rand_density(3, rng)
g2 = special_unitary(3, rng)
rho_rot = g2 @ rho @ g2.conj().T
check("purity residual 1: orientation MOVES: rho_rot != rho as operators",
      np.max(np.abs(rho_rot - rho)) > 1e-3)
check("purity residual 2: spectrum (all SU(3)-invariants) preserved exactly",
      np.max(np.abs(np.sort(np.linalg.eigvalsh(rho)) -
                    np.sort(np.linalg.eigvalsh(rho_rot)))) < TOL)
purity = lambda r: np.trace(r @ r).real
check("purity residual 3: purity (two-copy invariant) agrees for SU(3)-related states",
      abs(purity(rho) - purity(rho_rot)) < TOL)
rho_diff = 0.5 * rho + 0.5 * (I3 / 3.0)                 # genuinely different spectrum
check("purity residual 4: purity DISTINGUISHES a different-spectrum state (residual is real)",
      abs(purity(rho) - purity(rho_diff)) > 1e-3)

# ---------------------------------------------------------------------------
# r-dial guard checks. gen (x) color; global color SU(3) acts as I (x) g. The mass
#     pattern (carrying r) is color-singlet: its observables are M (x) I and are
#     EXACTLY fixed by the color rotation; r is distinguished by observables but
#     NOT moved by orientation. Contrast: a non-invariant color op DOES move.
# ---------------------------------------------------------------------------
# two generation states with DIFFERENT block-weight r (doublet/singlet split)
def gen_state(r):
    # singlet weight 1-x, doublet weight x split as a diagonal pattern; r ~ x
    x = r / (1.0 + r)
    return np.diag([1.0 - x, x / 2.0, x / 2.0])

rA, rB = 0.5, 1.0
genA, genB = gen_state(rA), gen_state(rB)
color = rand_density(3, rng)
g3 = special_unitary(3, rng)
Gcol = np.kron(I3, g3)                                  # color-only global rotation

# an r-readout observable: doublet-vs-singlet population on the gen factor
Pdoublet = np.diag([0.0, 1.0, 1.0])
M_r = np.kron(Pdoublet, I3)                             # color-singlet mass-pattern obs

rhoA = np.kron(genA, color)
rhoA_rot = Gcol @ rhoA @ Gcol.conj().T
rhoB = np.kron(genB, color)

check("r-dial guard 1: r-readout UNCHANGED by color-orientation rotation (exact)",
      abs(np.trace(rhoA @ M_r).real - np.trace(rhoA_rot @ M_r).real) < TOL)
check("r-dial guard 2: r-readout DOES distinguish rA != rB (observables depend on r)",
      abs(np.trace(rhoA @ M_r).real - np.trace(rhoB @ M_r).real) > 1e-3)
# WHY r is safe: the only symmetry in play (color SU(3)) fixes r exactly; there
# is NO symmetry moving r, so the orientation blade cannot reach it.
check("r-dial guard 3: color SU(3) fixes r: no orientation rotation alters the r-readout",
      abs(np.trace(rhoA @ M_r).real - np.trace(rhoA_rot @ M_r).real) < TOL)
# non-vacuity: a non-invariant color operator DOES move under the same rotation
O_co = np.kron(I3, E12 + E12.conj().T)
check("r-dial guard 4: non-invariant color op DOES move (rotation is non-trivial)",
      abs(np.trace(rhoA @ O_co).real - np.trace(rhoA_rot @ O_co).real) > 1e-3)

# ---------------------------------------------------------------------------
# Negative control: predictive equivalence is SPECIFIC to the
#     invariant subalgebra -- it FAILS for a non-invariant (adjoint) operator.
# ---------------------------------------------------------------------------
rho9 = rand_density(9, rng)
h5 = special_unitary(3, rng)
two_carrier_rotation = np.kron(h5, h5)
rho9_rot = two_carrier_rotation @ rho9 @ two_carrier_rotation.conj().T
O_noninv = np.kron(E12 + E12.conj().T, I3)             # adjoint on carrier A
check("negative control: equivalence FAILS for a non-invariant operator",
      abs(np.trace(rho9 @ O_noninv).real - np.trace(rho9_rot @ O_noninv).real) > 1e-3)

# ---------------------------------------------------------------------------
# Discipline guards wired to fresh computations (no check(True)).
# ---------------------------------------------------------------------------
# (a) orientation retirement does NOT depolarize: a polarized state stays
#     polarized under rotation (purity preserved) -> no twirl / frame / depol.
rho_pol = np.diag([0.7, 0.2, 0.1]).astype(complex)
order_param = lambda r: (np.trace(r @ r).real - 1.0 / 3.0)
check("discipline guard 1: purity untouched: polarized stays polarized (no depolarization delivered)",
      abs(order_param(rho_pol) - order_param(g2 @ rho_pol @ g2.conj().T)) < TOL
      and order_param(rho_pol) > 1e-3)
# (b) no frame / partition delivered: single-carrier invariant projectors are
#     only 0 and I (commutant = scalars) -- no nontrivial pointer set produced.
check("discipline guard 2: no frame delivered: only SU(3)-invariant projectors are 0, I (Schur)",
      commutant_dim(GM) == 1)
# (c) Static local color-frame redundancy is not short-circuited: the statement is GLOBAL (one g for all sites),
#     delivering NO local connection. Witness: a global rotation commutes with a
#     site-translation/permutation P, so it supplies no per-edge (link) data.
P = np.kron(np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], complex), I3)  # site shift (x) color
Gglob = np.kron(I3, g3)  # same g on the color factor of every site -- global
check("discipline guard 3: global rotation commutes with site-shift (no local link delivered)",
      np.max(np.abs(Gglob @ P - P @ Gglob)) < TOL)

print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
