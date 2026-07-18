# Gauge-Vacuum Plaquette Spatial Environment Tensor-Transfer Bounded Packet

**Date:** 2026-04-17; 2026-05-18 (claim_scope narrowed to the finite
one-word support packet per audit verdict boundary instruction);
2026-05-23 (scope repaired to cite the finite tensor-word
packet and demote the full boundary-character law to an open target).
**Type:** bounded_theorem
**Claim scope (post-2026-05-23 narrowing):** the load-bearing claim is
only the bounded finite tensor-word packet already isolated by
[`GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md`](GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md):
at dominant-weight box `NMAX = 4`, Bessel mode sum
`MODE_MAX = 80`, and `beta = 6`, one explicit 25-state matrix
constructed from stipulated integral coefficients and finite
`SU(3)` fundamental / anti-fundamental fusion recurrences is
nonnegative entry-wise, conjugation-swap symmetric, and has
nonnegative unit-vector boundary readout. The coefficient and fusion
ingredients are used only as mathematical inputs to that constructed finite
matrix. This note does **not** claim the full
boundary-character identity
`z_(p,q)^env(beta) = <chi_(p,q), (T_beta^env,tensor)^(L_perp-1)
eta_beta^env>` for actual unmarked spatial-environment amplitudes.
The full untruncated tensor-transfer operator at `beta = 6`, the
Perron/boundary readout, convergence and positivity beyond the finite
box, multi-word coverage, and numerical evaluation of the
boundary-character identity remain open targets.
**Status authority:** source-note proposal only; audit verdict and
effective status are set by the independent audit lane. The
`bounded_theorem` label is a source-side claim-boundary declaration,
not an audit verdict.
**Script:** `scripts/frontier_gauge_vacuum_plaquette_spatial_environment_tensor_transfer.py`

## Question

Can one explicit finite matrix be constructed from the stipulated coefficient
table and finite `SU(3)` Pieri matrices, with its elementary positivity and
conjugation properties checked directly?

## Answer

Yes, for the finite matrix isolated in the bounded companion row. The runner
evaluates the stipulated coefficients on `0 <= p,q <= 4`, constructs the
fundamental and anti-fundamental Pieri matrices on that box, and checks one
explicit matrix word. No slicing derivation, physical placement, transfer-law
existence, or environment boundary state follows from this construction.

## Setup

From the exact transfer-operator / character-recurrence theorem already on
`main`:

- the plaquette source sector carries the exact self-adjoint source operator
  `J = (chi_(1,0) + chi_(0,1)) / 6`;
- the marked plaquette source lives on the `SU(3)` dominant-weight class basis;
- multiplication by `chi_(1,0)` and `chi_(0,1)` closes exactly on the
  dominant-weight graph through the standard six-neighbor recurrence.

The broader program has proposed local-factor, residual-environment, and
character-measure identifications. None of those identifications is an input or
conclusion of the finite matrix theorem here. In particular, the statements
`D_beta^loc = diag(a_(p,q)^4)` and `R_beta^env = C_(Z_beta^env)` require their
own physical/operator authority and remain open at this note's scope.

## Bounded ingredient 1: stipulated finite integral values

For the supplied integral convention, define the finite coefficients by

`c_lambda(beta) = integral_SU(3) chi_lambda(U)
exp[(beta/3) Re Tr U] dmu_Haar(U)`.

with

- `c_lambda(beta) >= 0`,
- `c_(p,q)(beta) = c_(q,p)(beta)`.

At `beta = 6`, these coefficients are evaluated through the disclosed
Bessel-determinant mode sums.

On the `NMAX = 4`, `MODE_MAX = 80`, `beta = 6` packet, the normalized values
are explicit. This note does not call them local tensor weights or claim
all-weight or untruncated coefficient closure.

## Bounded ingredient 2: finite Pieri matrices

The finite packet uses the fundamental and anti-fundamental
three-neighbor `SU(3)` Pieri recurrences on the same dominant-weight box. These
integer matrices are independent finite representation-theory inputs. The
constructed matrix word does not prove an all-slice or all-weight
spatial-environment transfer operator.

## Open target: boundary-character generation by the tensor-transfer law

The symbols `T_beta^env,tensor` and `eta_beta^env` denote proposed objects in
the broader program, not objects constructed by this note. The open target is
first to derive their physical/operator meaning and then prove and evaluate

`z_(p,q)^env(beta)
  = <chi_(p,q), (T_beta^env,tensor)^(L_perp-1) eta_beta^env>,`

and hence

`rho_(p,q)(beta)
  = z_(p,q)^env(beta) / z_(0,0)^env(beta)`

as the normalized tensor-transfer boundary amplitude sequence of the
actual unmarked spatial environment. That identity is not load-bearing
for this bounded packet and is not numerically evaluated by the runner.

**Runner-verified evidence on the truncated packet.** The runner
constructs one explicit nonnegative-entry matrix from the
truncated mathematical ingredients (stipulated character coefficients on the
`NMAX = 4` dominant-weight box at `MODE_MAX = 80` Bessel support, plus
`SU(3)` fusion intertwiners on that box) and verifies three
finite-packet properties:

- nonnegativity of the constructed matrix entries,
- conjugation-swap symmetry of the matrix,
- nonnegativity of the boundary amplitude under the unit-vector
  readout.

These verify **one finite tensor-word packet** on the truncated inputs.
They do not numerically evaluate
`<chi_(p,q), (T_beta^env,tensor)^(L_perp-1) eta_beta^env>` for general
`L_perp` or general boundary states, and they do not extend beyond the
one constructed matrix.

**Open target.** The physical transfer operator, its relation to any actual
spatial environment, and its boundary state all remain to be derived. The one
constructed finite matrix does not establish their existence or operator
class. All-weight convergence, positivity, multi-word coverage, and the
matrix-element identity remain part of that open target.

## No corollary about the physical operator class

The finite matrix theorem does not localize the physical gap to numerical
evaluation. Existence of the transfer law, the placement of a local factor,
the environment operator class, and the boundary-state identification all
remain open alongside any eventual numerical evaluation.

## What this closes

- bounded finite tensor-word support already represented by the
  bounded companion: one explicit `NMAX = 4`, `MODE_MAX = 80`,
  `beta = 6` matrix has nonnegative entries, conjugation-swap symmetry,
  and nonnegative unit-vector boundary readout;
- bounded construction from explicit finite mathematical inputs;
- a precise statement that the full tensor-transfer / Perron-boundary target
  is not reached by that construction.

## What this does not close

- explicit evaluated tensor-transfer matrix elements at `beta = 6`
- explicit physical boundary values `rho_(p,q)^env(6)` from this transfer route
- explicit Perron moments after the full spatial environment is included
- derivation of a physical local mixed-kernel factor
- existence or identification of an actual spatial-environment transfer operator
- analytic closure of canonical `P(6)`
- repo-wide repinning of the canonical plaquette

## Script boundary

The bounded packet above is structural but finite. The linked runner is
intentionally a finite support packet only:

- it audits a truncated dominant-weight box with `NMAX = 4`,
- it truncates the Bessel mode sum at `MODE_MAX = 80`,
- it checks one explicit nonnegative-entry matrix word built from those finite
  mathematical inputs,
- it does **not** evaluate the full `beta = 6` tensor-transfer matrix
  elements,
- it does **not** compute the `beta = 6` Perron state or the boundary
  coefficients `rho_(p,q)(6)`.

So the script is evidence only for the displayed finite matrix properties. It
is not evidence for a local Wilson factor, a tensor-transfer operator class, or
an environment solve.

## Commands run

```bash
python3 scripts/frontier_gauge_vacuum_plaquette_spatial_environment_tensor_transfer.py
```

Expected summary:

- `THEOREM PASS=4 SUPPORT=3 FAIL=0`

## Out of scope (open context only)

The following items are explicitly **NOT** load-bearing claims of this
note. They depend on separate authority rows / open derivations / open
construction work and are recorded only as open context:

1. **Full untruncated tensor-transfer operator at `beta = 6`.** The
   exact untruncated construction (positivity, convergence, full
   support beyond `NMAX = 4`, full Bessel-mode sum beyond
   `MODE_MAX = 80`) is not constructed or checked here.

2. **`beta = 6` tensor-transfer Perron solve.** The explicit `beta = 6`
   matrix elements, Perron state, and boundary coefficients
   `rho_(p,q)(6)` are **not** computed here. The script is a finite
   truncated support packet only.

3. **Multi-tensor-word generalization.** The runner verifies one
   explicit nonnegative-entry matrix word; the general case beyond
   that example is not claimed here.

The **in-scope content** of this note is the finite truncated support
packet that exhibits consistency of the stipulated finite coefficients and
finite fusion recurrences under one matrix word.
Theorems that depend on the full untruncated construction at `beta = 6`
must cite the unresolved open object directly.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note, change the audited claim scope, or close the open positive-theorem bridge.

The conditional verdict named the load-bearing gap as the bridge from local character/fusion ingredients to the actual spatial-environment boundary amplitudes. That gap remains the explicit out-of-scope open object of this note (full untruncated tensor-transfer at `beta = 6`, multi-tensor-word generalization, explicit `beta = 6` Perron solve, numerical evaluation of the boundary-character matrix-element identity).

A finite packet source note records the exact matrix object this row can
safely claim:

- [gauge_vacuum_plaquette_finite_tensor_word_packet_bounded_note_2026-05-10](GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md)
  records the finite 25-state `NMAX = 4`, `MODE_MAX = 80`, `beta = 6`
  tensor-word packet with the same nonnegativity, conjugation-swap, and
  unit-vector readout properties isolated here. This is the load-bearing
  one-hop authority for the bounded repair of this row.

A separate numerical cross-check exists for the stipulated coefficient table:

- [gauge_vacuum_plaquette_rho_pq6_wilson_environment_bounded_note_2026-05-09](GAUGE_VACUUM_PLAQUETTE_RHO_PQ6_WILSON_ENVIRONMENT_BOUNDED_NOTE_2026-05-09.md)
  evaluates the explicitly stipulated integral and normalized values
  `rho_(p,q)(6) = c_(p,q)(6) / (d_(p,q) c_(0,0)(6))` on the finite weight
  box `0 <= p,q <= 4` by independently implemented Schur-Weyl
  Bessel-determinant and Weyl-Cartan routes. This citation records only that
  finite numerical evaluation; it does not identify the values with a physical
  local factor, environment coefficient sequence, or tensor-transfer readout.

These finite calculations do **not** supply: the all-weight closed form, the
full untruncated tensor-transfer operator at `beta = 6`,
multi-tensor-word generalization, or the `beta = 6` Perron state of the
full spatial environment. Those gaps remain the open positive-theorem
target stated in the existing "What this does not close" and "Out of
scope" sections of this note.
