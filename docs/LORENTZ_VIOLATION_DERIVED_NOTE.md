# Fixed-Action Cubic-Anisotropy Diagnostic

**Script:** `scripts/frontier_lorentz_violation.py` ([runner](../scripts/frontier_lorentz_violation.py))
**Runner cache:** [`frontier_lorentz_violation.txt`](../logs/runner-cache/frontier_lorentz_violation.txt)
**PStack:** `frontier-lorentz-violation-derived`
**Claim type:** bounded_theorem

**Current publication disposition:** not publication-usable. The calculations
below are conditional on a supplied kinetic operator, lattice spacing, and
continuum interpretation; they are not consequences of the four axioms.

## Scope and inputs

This note checks one selected model surface:

- a nearest-neighbor second-order finite-difference spatial kinetic symbol on
  a cubic lattice;
- a separately supplied spacing `a`;
- a relativistic-dispersion interpretation of that symbol; and
- for the numerical scale illustration only, the approved scale-reference
  units primitive `a^{-1} = M_Pl`.

The four axioms do not select that action or kinetic symbol and do not
establish the charge conjugation, parity, time-reversal, carrier, or SME-sector
assumptions needed for a physical CPT or phenomenology claim. The exact-CPT
source previously used by this lane is not used by this theorem. The
registered scale-reference primitive supplies a ruler only: it does not derive
`a/l_P = 1` as physics or supply any dimensionless dynamics.

## Derivation chain

The calculation proceeds from the supplied fixed-action inputs above.

### Step 1 -- spatial symmetry of the supplied cubic symbol

The selected spatial momentum symbol is invariant under the octahedral point
group `O_h`, the symmetry group of the cube, rather than under arbitrary
spatial rotations at finite `a`. The runner constructs the full signed-
permutation representation directly: all `3! * 2^3 = 48` distinct orthogonal
`3 x 3` integer matrices with one `+/-1` in each row and column. It verifies
exactly that identity and every transpose inverse are present, all `48^2`
products close in the set, and the determinant split is 24 proper plus 24
improper elements.

The runner then applies every element to deterministic hostile samples. It
checks both the supplied nearest-neighbor kinetic symbol

    K_a(p) = sum_i (4/a^2) sin^2(p_i a / 2)

and `sum_i n_i^4` on generic unequal components, axis/diagonal directions,
and momenta near Brillouin-zone faces. Both are
invariant under all `48` actions. As a negative control, the proper rotation
`R_z(pi/7)`, which is not a signed permutation and hence is outside `O_h`,
changes `K_a(p)` for the fixed hostile momentum used by the runner while
preserving the Euclidean norm. Thus the certificate distinguishes finite-`a`
cubic invariance from full rotational invariance. This is a statement about
the supplied symbol, not a derivation of a full spacetime Lorentz
representation from the axioms.

### Step 2 -- Leading finite-`a` cubic-anisotropy operator

The supplied finite-difference kinetic term per spatial direction is

    K_i = (4/a^2) sin^2(p_i a / 2)

Taylor-expanding for p_i a << 1:

    K_i = p_i^2 - (a^2/12) p_i^4 + (a^4/360) p_i^6 - ...

Summing over i = 1,2,3 gives the modified dispersion relation

    E^2 = m^2 + p^2 - (a^2/12) sum_i p_i^4 + O(a^4 p^6)

The leading correction is a dimension-6 operator (p^4 with a^2 coefficient).
No odd power appears in this particular Taylor series because the selected
symbol is even in momentum. That algebraic fact does not establish parity or
CPT for a complete matter action. The runner asks Sympy for the series of the
supplied sine symbol and asserts the exact coefficients `1`, `-a^2/12`, and
`a^4/360`; a separate fixed numerical sample confirms that the `p^6`
truncation residual is smaller than the `p^4` residual.

### Step 3 -- conditional Planck-scale illustration

Using the approved units reference `a^{-1} = M_Pl` and
`1 GeV^{-1} = hbar c = 1.973269804 x 10^{-16} m`, one obtains
`a = 8.1907451111 x 10^{-20} GeV^{-1}` and
`1/a = 1.2208901467 x 10^19 GeV`. Therefore:

    |delta E^2| / E^2 ~ (1/12)(E / E_Planck)^2

At `E = 1 GeV` this gives `a^2/12 = 5.5906921229 x 10^{-40} GeV^{-2}`,
or `5.6 x 10^{-40}` to two significant figures. This is a units illustration,
not a framework prediction. The quadratic suppression follows from the
selected even finite-difference symbol.

### Step 4 -- Angular structure: the cubic harmonic fingerprint

The operator sum_i n_i^4 (for unit vector n) decomposes, in the basis of
the STANDARD NORMALIZED real spherical harmonics Y_lm (orthonormal over
the unit sphere, Condon-Shortley convention). The runner implements the
corresponding closed normalized expression and exact sphere projection:

    sum_i n_i^4 = 3/5 + (4*sqrt(pi)/15) K_4(theta, phi)

where K_4 is the l=4 cubic harmonic:

    K_4 = Y_{40} + sqrt(5/14) (Y_{44} + Y_{4,-4})

Convention note (normalization correction, 2026-05-29). With *normalized*
Y_lm the coefficient on K_4 is 4*sqrt(pi)/15 ~= 0.4727, NOT 4/5. An earlier
revision of this note wrote 4/5; that value is only correct for an
unnormalized angular convention and is inconsistent with the normalized
K_4 above and with the runner's exact normalized projection. The identity is
fixed here to the normalized convention so that note and runner agree. The
isotropic part 3/5, the factor-of-3 anisotropy, and the `l = 2,6`-free
structure are unchanged by this correction; only the numerical weight on
the l = 4 anisotropy operator is corrected.

Sympy derivation of the coefficient. For n = (sin t cos p, sin t sin p,
cos t), expand f(t,p) = sum_i n_i^4 in normalized Y_lm. The only nonzero
projections are l = 0 and l = 4:

- <f | Y_{00}> = 6*sqrt(pi)/5, so the isotropic part is <f|Y_{00}> Y_{00}
  = 3/5 (since Y_{00} = 1/(2*sqrt(pi))).
- <K_4 | K_4> = 1 + 5/14 + 5/14 = 12/7 (the three normalized harmonics in
  K_4 are orthonormal, with coefficients 1, sqrt(5/14), sqrt(5/14)).
- <f | K_4> / <K_4 | K_4> = 4*sqrt(pi)/15.

Reconstructing `f = 3/5 + (4*sqrt(pi)/15) K_4` and simplifying gives
`trigsimp(f - rhs) = 0` identically. The runner independently integrates the
closed normalized expression over the sphere and asserts

- `<K_4 | K_4> = 12/7`;
- `<f | K_4> = 16*sqrt(pi)/35`; and
- `<f | K_4>/<K_4 | K_4> = 4*sqrt(pi)/15`.

It also evaluates the discarded `4/5` coefficient on the `[100]` axis and
asserts a nonzero residual. The same executed certificate verifies invariance
under all 48 O_h elements and the exact directional values `f_4([100]) = 1`
and `f_4([111]) = 1/3`.

### Step 5 -- what the calculation does not establish

The even scalar momentum symbol is compatible with spatial inversion, but a
real scalar function is not by itself a proof of time reversal or charge
conjugation for a specified fermion/gauge action. Consequently this runner
does not establish exact CPT and does not set the CPT-odd SME coefficients to
zero. Any such conclusion requires a separately specified complete action,
symmetry operators, their domains, and an audit-clean proof.

The physical selection bridge remains open: nothing here derives the supplied
nearest-neighbor kinetic operator, a relativistic carrier interpretation, a
framework-native choice of this carrier/action, or an SME sector response map.
The registered scale-reference primitive supplies only the units ruler. The
finite-group certificate therefore does not by itself establish physical
Lorentz violation.

## Experimental status

No experimental-consistency claim is made. Comparator rows from earlier
revisions are omitted because this packet supplies neither a sector-by-sector
SME response map nor a physical identification of the selected lattice
excitation with an experimental probe.

## Interpretation boundary

The robust output of this note is the algebra of the supplied momentum
symbol: its `p_i^4` Taylor term, normalized `l=4` cubic-harmonic decomposition,
and factor-of-three `[100]`/`[111]` angular ratio. It does not uniquely identify
an underlying microscopic theory, distinguish this framework from all other
models, or support a CPT or experimental-consistency verdict.

## Relation to frontier_lorentz_violation.py

The script `frontier_lorentz_violation.py` is the registered diagnostic runner
for this note. It computes the supplied lattice dispersion using the standard
second-order finite-difference Laplacian eigenvalue
`(4/a^2) sin^2(pa/2) = (2/a^2)(1 - cos(pa))`, which yields the canonical
expansion `p^2 - (a^2/12) p^4 + (a^4/360) p^6 + ...` directly.

Finite-group repair (2026-07-16): the runner now implements the Step 1 claim
instead of merely printing cubic-symmetry language. It explicitly enumerates
the 48 signed-permutation matrices, certifies their finite-group structure,
checks `K_a(p)` and `sum_i n_i^4` under every action on deterministic hostile
samples, and checks that `R_z(pi/7)` outside `O_h` changes the finite-`a`
symbol. The group certificate and the existing cubic-harmonic identity are both
load-bearing exit conditions, so either failure produces a nonzero exit.

Restricted-packet repair (2026-07-29): the registered runner was reduced from
an oversized historical phenomenology script to a compact, self-contained
algebraic certificate. Its complete source is below the audit packet's
40,000-character runner-source limit, and its exact current stdout is captured
in the SHA-pinned runner cache linked above and is below the 20,000-character
stdout limit. Four independent exit gates now explicitly assert the repair
targets: the `-a^2/12` Taylor coefficient, the `4*sqrt(pi)/15` normalized
projection, the `O_h` outside-group negative control, and the metre/GeV unit
conversion. The final summary prints every gate and exits nonzero if any
executed assertion fails.

Audit fix (2026-05-02): a previous version of the runner used
`(2/a^2) sin^2(pa/2)`, which is the half-normalized kinetic eigenvalue
and is internally inconsistent with the printed Taylor expansion. The
runner has been updated to the standard `(4/a^2)` form that matches
this note's Step 2. The compact certificate now extracts the three displayed
coefficients exactly and separately verifies residual improvement through
`p^6` at a fixed three-component momentum.

Normalization correction (2026-05-29): a previous version of this note
and runner wrote the cubic-harmonic decomposition with coefficient `4/5`
on `K_4 = Y_{40} + sqrt(5/14)(Y_{44} + Y_{4,-4})`. With the standard
normalized real spherical harmonics `Y_lm` (the
`scipy.special.sph_harm` / `sympy.Ynm` convention) the correct
coefficient is `4*sqrt(pi)/15 ~= 0.4727` (see Step 4). The runner now
derives the symbolic `trigsimp(f - rhs) = 0`, the exact norm and overlap,
and the projection `<f|K_4>/<K_4|K_4> = 4*sqrt(pi)/15` in one mandatory
Sympy path; it separately refutes `4/5` at the `[100]` axis. This is a
normalization correction only: the dimension-6 classification, the parity-even /
no-odd-power conclusion, the `3/5` isotropic average, and the
factor-of-3 `[100]`/`[111]` anisotropy are unchanged, because they
follow from the dispersion Taylor structure and pure geometry, not from
the `K_4` coefficient. The script exits non-zero if the identity check
fails.
