# DM Flagship Gate — Supplied PMNS Fit and Open Selection

**Type:** open_gate
**Primary runner:** `scripts/frontier_dm_flagship_supplied_segment_inertia.py`
**Primary coverage:** exact supplied determinant/inertia segment below. The
conditional fitted-point calculation is an explicit dependency on the linked
PMNS canonical note/runner, not a new physical derivation by this primary.
**Date:** 2026-04-17; scope corrected 2026-10-21
**Status:** the flagship remains open. This entry point reports a conditional
matrix map, one fitted numerical candidate, and a narrowly specified inertia
argument. It assigns no retained status and closes no physical selector gate.

## Conditional PMNS calculation

The [primary PMNS note](PMNS_FROM_DM_NEUTRINO_SOURCE_H_DIAGONALIZATION_CLOSURE_THEOREM_NOTE_2026-04-17.md)
uses the supplied Hermitian affine chart

```text
H = H_base + m T_m + delta T_delta + q_+ T_q,
H_base = [[0,E1,-E1-i gamma], [E1,0,-E2], [-E1+i gamma,-E2,0]],
T_m = [[1,0,0], [0,0,1], [0,1,0]],
T_delta = [[0,-1,1], [-1,1,0], [1,0,-1]],
T_q = [[0,1,1], [1,0,1], [1,1,0]],
gamma=1/2, E1=sqrt(8/3), E2=sqrt(8)/3,
q_+ + delta >= E1.
```

The three parameters are real. The charged-lepton axis basis `U_e=I` and
row permutation `sigma_hier=(2,1,0)` are separately supplied. Eigenvectors
of `H` are columns ordered by ascending eigenvalue; the row permutation then
orders the flavor axes. Row ordering is not a consequence of sorting the
eigenvalue columns. The charged-lepton trichotomy and Higgs-charge arguments
are historical provenance for these modeling choices, not certification of
their physical selection in this calculation.

On the nondegenerate spectrum and nonzero angle-denominator domain, the
primary note defines rephasing-invariant angles, Jarlskog invariant and the
phase using both sine and cosine with `atan2`. The phase is undefined at
vanishing mixing denominators; no globally smooth eigenbasis map across
spectral degeneracies is claimed.

The three historical target values are supplied fit inputs:

```text
(s12^2,s13^2,s23^2) = (0.307,0.0218,0.545).
```

The finite multistart search and local refinement locate
`(m,delta,q_+)=(0.657061342210,0.933806343759,0.715042329587)`.
It gives `sin(delta_CP)=-0.9874`, `cos(delta_CP)=-0.15849`,
`delta_CP=260.88 degrees` and `|J| approximately 0.0328`.
The phase is a conditional output at the fitted point, not an independently
validated experimental prediction. The previous `279.12 degrees` came from
an inverse-sine quadrant ambiguity. The correction changes neither the three
angle inputs nor the selected chart or row pairing.

One rounded candidate among accepted starts does not establish global
uniqueness, enumerate every basin, or prove a nonsingular fit Jacobian.
Nine modulus comparisons with supplied historical NuFit 5.3 intervals are
finite numerical comparisons, not an experimental likelihood or nine
independent predictions. No present experimental confidence claim follows.

## Inertia along the supplied segment

A continuous nonsingular Hermitian path preserves inertia, here written
`(n_negative,n_zero,n_positive)`. For the supplied chart, take the exact
rounded endpoint `(m_*,delta_*,q_*)=(0.657061,0.933806,0.715042)` and
`J_* = m_* T_m + delta_* T_delta + q_* T_q`. The path
`H(t)=H_base+t J_*`, `0<=t<=1`, is the specific segment considered in
`DM_NEUTRINO_SOURCE_SURFACE_P3_SYLVESTER_LINEAR_PATH_SIGNATURE_THEOREM_NOTE_2026-04-18.md`.

The dedicated primary constructs this matrix with exact rational six-decimal
coordinates and radical constants. It compares the exact determinant polynomial
to the prior independent control and uses rational interval bounds to certify
both derivative roots and the positive minimum.

Its determinant is cubic in `t`. Testing its endpoints and all interior
roots of the quadratic derivative establishes its minimum on that interval;
the supplied-endpoint calculation gives minimum approximately `0.878309>0`.
Thus that segment avoids singularity and joins the baseline and that endpoint
with inertia `(2,0,1)`. This statement concerns the rounded endpoint actually
used by that path calculation, not an unspecified neighborhood or every fit
candidate. The path need not remain in the separately imposed active chamber:
the baseline itself is outside `q_+ + delta >= E1`.

Opposite-inertia endpoints cannot connect to the baseline along a nonsingular
Hermitian path. Equal inertia alone does not prove connectivity within this
restricted affine chart. Neither observation classifies all components or
selects the physically realized one. A rule identifying the baseline-connected
component with the physical sheet remains an open physical identification;
the historical label `A-BCC` grants it no approved-axiom authority here.
The source note's broader historical status and component claims are not
imported by this narrow path statement.

## Downstream use and remaining obligations

Downstream transport or flavor calculations may evaluate this candidate with
the same chart, axis basis, row ordering and historical targets explicitly
supplied. Such evaluation does not turn the fitted PMNS matrix into a
retained derived input or establish a physical transport normalization.

The earlier upper-octant thresholds and unconditional lower-octant
falsification claim are not established by this finite fit. A discrepancy
can challenge this specified candidate and its premises; it does not exclude
every branch or every source construction. The historical charged-lepton
route and Higgs-charge gauge comparison do not remove the supplied-basis
and row-pairing requirements from this review.

Open obligations include physical source and branch selection, charged-lepton
basis and hierarchy pairing, global solution/component classification, a
microscopic selection law, solar splitting, absolute neutrino mass scale,
Majorana phases, and downstream carrier/transport completeness. The present
calculation neither resolves these obligations nor rules out alternate local
selector constructions. No parity, information-geometric, microscopic
polynomial, local-selector or split-2 repair is certified by this entry point.

## Historical source recovery and verification

The complete earlier flagship argument, route inventory, runner totals,
upper-octant analysis, charged-lepton route, review order and closing summaries
are preserved byte-for-byte at Git commit
`f24d17d97d372df977476e4a69674577f31af575` under this same path. The intermediate
PR revision is recoverable at `3c90f9860c3bae63ee64949e7178290f789dd982`.
Those records are historical source, not live conclusions of this scoped
entry point. Their claims and deferred repairs require separate review;
aggregate PASS totals establish neither scientific independence nor closure.

Reproduce only the current conditional fit with

```bash
PYTHONPATH=scripts python3 scripts/frontier_pmns_from_dm_neutrino_source_h_diagonalization_closure_theorem.py
```

Its linked primary note and refreshed cache describe the same supplied inputs
and finite checks. This entry point does not request an aggregate runner sweep,
audit verdict or retained promotion.

Reproduce the exact supplied-segment certificate with:

```bash
python3 scripts/frontier_dm_flagship_supplied_segment_inertia.py
```

The earlier broad current-main flagship is also preserved byte-for-byte at
`archive/notes/review_feedback/pr9844-flagship-2026-10-23/DM_FLAGSHIP_CLOSURE_REVIEW_NOTE_2026-04-17.md.txt`.
The supplied fit remains conditional on its separately bound PMNS calculation.
