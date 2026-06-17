# Two-Band Orbital Response: Refutation And Corrected Star-Product Result

**Date:** 2026-06-12
**Claim type:** bounded_theorem
**Type:** bounded_theorem
**Primary runner:**
[`scripts/frontier_two_band_orbital_closed_form_2026_06_12.py`](../scripts/frontier_two_band_orbital_closed_form_2026_06_12.py)
**Runner cache:**
[`logs/runner-cache/frontier_two_band_orbital_closed_form_2026_06_12.txt`](../logs/runner-cache/frontier_two_band_orbital_closed_form_2026_06_12.txt)
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.

## Claim

For the free `d = 2` staggered checkerboard two-band model at the fixed boundary
probe `mu = 1.7086`, `T = 0.2`, the prior fitted interband ansatz

```text
chi_inter = -(47/120) * integral_BZ (f_- - f_+) R Omega_z^2 d^2k/(2pi)^2
```

is refuted.  The coefficient `47/120` is not a missing universal prefactor.  In
the linearized two-band problem the correct occupation-difference structure is

```text
B^2 coefficient:       (f_- - f_+) (qx^2 + qy^2)/(8 R^5)
d2/dB2 contribution:   (f_- - f_+) (qx^2 + qy^2)/(4 R^5).
```

Since `R Omega_z^2 = m^2/(4 R^5)` in that continuum limit, the ratio of the
correct `d2/dB2` core to `R Omega_z^2` is `(qx^2 + qy^2)/m^2`, not a constant.
Thus no scalar multiple of `R Omega_z^2`, including `47/120`, gives the
interband response.

## Anchors Preserved

The runner keeps the mirrored finite-cell Peierls-PT anchors from the landed
two-band exact runner.  It gates the exact and full-PT responses at
`m = 0, 0.2, 0.3, 0.5`, the maximum exact-vs-PT relative deviation below
`7.9e-3`, and the `m = 0.5` near cancellation
`chi_intra = +3.178505`, `chi_inter = -3.147761`.  It also gates that the
mirrored off-mass interband terms are nonzero, preventing the old fabrication
failure mode where interband structure was silently absent.

The `m = 0` LP determinant term still reproduces the full-PT anchor.  The cell
response normalization

```text
C_cell = 0.04013739257002893
```

is fixed once at that LP reference point.  It is a single physical response-unit
normalization, not a per-mass fit and not an interband fudge factor.

## Dependencies

- [LP_TWO_BAND_EXACT_COMPLETION_BOUNDED_THEOREM_NOTE_2026-06-12.md](LP_TWO_BAND_EXACT_COMPLETION_BOUNDED_THEOREM_NOTE_2026-06-12.md)
  -- the retained-bounded finite-cell Peierls perturbation anchor whose
  full-PT response values and near-cancellation split are mirrored here before
  the scalar-prefactor refutation and corrected star-product check.

## Corrected Derivation

The runner reproduces the symbolic Moyal/Peierls star-product derivation in
SymPy.  For `H = qx sigma_x + qy sigma_y + m sigma_z`, with
`Q = z - H` and `G = Q^{-1}`, the B-expanded star inverse gives

```text
tr G2 = -4 z (qx^2 + qy^2)/(R^2 - z^2)^4.
```

Taking the double-pole residues in the contour formula gives the occupation
difference above.  The symbolic gate checks the identity, the factor of two
from the `B^2` coefficient to `d2/dB2`, residue cancellation between the two
bands, and the nonconstant ratio to `R Omega_z^2`.

For the lattice convention

```text
H(k) = d_x(k) sigma_x + d_y(k) sigma_y + d_z sigma_z,
d_x(k) = -2 cos(k_x),
d_y(k) = -2 cos(k_y),
d_z = m,
R = sqrt(d_x^2 + d_y^2 + m^2),
```

the runner builds the lattice star-product interband term directly.  The Pauli
algebra gives

```text
tr G2 = -32 z (N0 + Nz2 z^2)/(z^2 - R^2)^4,
```

so the lower-band double-pole residue is `(N0 - Nz2 R^2)/R^5`, and the
interband `d2/dB2` core is twice that residue.  The explicit `N0` and `Nz2`
expressions are implemented in the runner from `cos(kx)`, `sin(kx)`, `cos(ky)`,
`sin(ky)`, and `m`; no scalar coefficient is fitted.

The no-fudge closed form tested by the runner is

```text
chi = C_cell * [ chi_LP_raw + chi_inter_star_raw ],
```

where `chi_LP_raw` is the Landau-Peierls Hessian-determinant term and
`chi_inter_star_raw` is the lattice star-product occupation-residue term.

## Measured Reproduction

Default run, fixed `N = 240` Gauss-Legendre grid:

| m | full PT | chi_LP | chi_inter_star | chi_closed | rel. deviation |
|---:|---:|---:|---:|---:|---:|
| 0.0 | 0.042933687517 | 0.042933687517 | 0.005213594911 | 0.048147282428 | 12.14% |
| 0.2 | 0.041273318495 | 0.041420945595 | 0.005092993102 | 0.046513938697 | 12.70% |
| 0.3 | 0.039175811591 | 0.039717889885 | 0.005093003087 | 0.044810892972 | 14.38% |
| 0.5 | 0.030744459999 | 0.034298764700 | 0.005124644940 | 0.039423409639 | 28.23% |

The derived no-fudge closed form over-captures the finite-cell full-PT response
on this panel.  The measured maximum relative gap is `28.23%`, and the runner
freezes a round `30%` residual gate.  This is the finding: the stale scalar
closed form is refuted, the corrected interband structure is derived, and the
current no-fudge lattice expression leaves a named positive over-capture
residual rather than closing the panel by an adjusted prefactor.

The runner also gates `N = 120 -> 240` grid halving.  The largest drift is the
massless point, `7.179e-4`, under the frozen `1.1e-3` grid gate.  The slow
massless convergence is disclosed rather than hidden.

## Scope And Open Follow-On

Scope is the free `d = 2` staggered two-band model, nearest-neighbor hopping
with `t = 1`, finite temperature, and the named small-`B` boundary probe.  This
is not an interacting statement, not a theorem for other lattice
regularizations, and not a continuum-only claim.

Full-lattice closed-form completion is not claimed here.  The named follow-on is
to reconcile the derived star-product occupation-residue term with the
finite-cell Peierls-PT seagull/interband split and the massless grid singular
sector, without introducing a scalar fudge coefficient.  The audit lane grades.

## No-Go Discipline Gate

N1 alternative routes checked: (1) a universal scalar multiple of `R Omega_z^2`
is ruled out by the symbolic ratio `(qx^2+qy^2)/m^2`; (2) the specific
`47/120` prefactor is ruled out by the same nonconstant ratio; (3) LP-only
completion is allowed at `m=0` but fails off mass on the fixed panel; (4) the
corrected no-fudge lattice star-product term is tested and leaves the named
positive residual rather than closing the panel; (5) numerical or fabrication
explanations are checked by exact/PT anchors, nonzero interband gates, and
grid-halving convergence.

N2 wall independence: this is not a multi-wall no-go.  The closed negative is
only the scalar-prefactor ansatz; the remaining residual is the separate
finite-cell/full-PT reconciliation problem.

N3 hidden-wall scan: the supplied inputs are explicit: free `d=2` staggered
two-band model, fixed boundary probe, retained-bounded Peierls-PT anchor, one
`m=0` cell normalization, and the displayed Moyal/Peierls star-product
calculation.  No interaction, all-lattice-family theorem, or continuum
completion is claimed.

N4 residual matching: the refuted residual is exactly "the interband response
is a scalar multiple of `R Omega_z^2`."  The note does not cite that as evidence
against finite-cell closed forms or other mass-dependent structures.

N5 rhetoric audit: "no scalar multiple" is pointwise for the displayed
continuum star-product core, not a statement about every averaged fit,
finite-cell formula, or future completion route.

N6 partial-closure path scan: the finite-cell reconciliation path is preserved,
not classified as impossible or as a new axiom/primitive requirement.

N7 steelman: a hostile reviewer can correctly say that the finite-cell Peierls
response may have an exact discrete momentum formula even though the stale
continuum scalar prefactor fails.  This note accepts that steelman and lands
only the scalar-prefactor refutation plus the bounded residual.

N8 cross-cycle echo: the pattern matches other route-local comparator misses in
the repo.  The repair is to localize the failed ansatz and keep the surviving
finite-cell route separate, not to foreclose the target response.
