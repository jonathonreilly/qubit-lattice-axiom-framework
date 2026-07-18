# Physical contact-sensitive source/response calibration stress — Cycle 387

Date: 2026-07-18

Type: bounded constructive blind-held calibration tournament

Authority: none

Audit: unset

Constitutional effect: none. This cycle changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, or audit-status surface and
drafts no axiom language.

Companion runner:

```text
scripts/physical_contact_sensitive_source_response_calibration_stress_cycle387_2026_07_18.py
```

## Result up front

Cycle 387 uses Cycle 374's 98-M2 apparatus as the frozen 98-M2 readout and obtains one bounded positive
calibration result. A single swap-symmetric, contact-conditioned
multiplicative calibration is fit on L=3,4 using only zero and one enabled
reservoir. It is frozen before blind held L=6 is opened. With no readout
retraining and no calibration refit, it predicts the two-enabled-reservoir
pointer response for:

- the Cycle-331 hard-core identity collision law;
- the same hard-core code with the already-declared signed onsite-Q2
  collision alternative;
- the Cycle-328 bosonic logical comparator; and
- the Cycle-328 independently labelled logical comparator.

The maximum held two-coordinate pointer residual is

```text
5.600968888702651e-4,
```

below the predeclared `1e-3` response tolerance. Converting that response back
through the same frozen calibration gives a maximum multiplicity residual
`0.004630557505736377`, below the predeclared `0.01` tolerance.

Direct additive composition does not describe the same finite pointer
coordinate: its smallest absolute held residual is
`0.029629307745172362`. The observed coordinate is instead monotone and is
well described by the frozen multiplicative form at this resolution. This is
a route-specific finite-model disposition, not a negative wall, no shared
obstruction, and no axiom pressure.

The inputs are called **candidate operational source coordinates** only. The
pointer response is dimensionless operational output. It is not energy, not
stress, not gravity, not a rate, and not an occurrence. It is also not called
a physical source, metric response, force, Record, or realized member.

## Frozen apparatus and split discipline

The Cycle-374 apparatus is not reselected. It remains

```text
depth                         2
program                       6
program name                  inverse_matter_coin_then_edge_fswap
matter operator               edge_FSWAP @ inverse_matter_coin
pointer projector             symmetric one-particle-per-cell ray
Cycle-331 seam               97 M2
pointer                       1 M2
readout patch                98 M2.
```

The exact Cycle-374 gather map is rechecked as a 4,096-coordinate permutation
at both endpoints with exact roundtrip. The program menu search is not run.
No held result can change the operator, depth, ray, pointer, or tolerance.

L=3,4 training contains only:

```text
L in {3,4}
(n_A,n_B) in {(0,0),(1,0),(0,1)}
contact code in {deleted,actual}
hard-core identity collision law.
```

Held data contain only L=6 and are opened after the calibration object has
been built. The two-coordinate cases `(1,1)` are absent from training. The
bosonic, independently labelled, and signed-collision cases are also absent
from training. No readout retraining or held-case refit occurs.

## Candidate coordinates and fixed calibration

The finite input tuple is

```text
(n_A, n_B, contact_code, declared comparator label),
```

where each `n_X` is the Boolean enable label of one already-installed
reservoir coupling. These are supplied candidate operational source
coordinates. They are not an identified energy-stress tensor or empirical
mass density.

Let `n=n_A+n_B`, and let `c` distinguish actual from deleted contact. The
calibration class is declared before held data:

```text
p_hat(n,c) = p_0(c) r(c)^n.
```

`p_0(c)` is the zero-coordinate training response and `r(c)` is the ratio of
the one-coordinate response to `p_0(c)`. Swap symmetry is imposed by pooling
A-only and B-only training rows. Their maximum discrepancy is below machine
precision.

The frozen coefficients are:

| contact code | `p_0` | `r` |
|---|---:|---:|
| deleted | `0.8524128395748263` | `0.8018863432296631` |
| actual | `0.7729580661127831` | `0.8027084830637017` |

All L3/L4 training values are size-stable. The training model residual is at
machine precision; held L6 was not consulted to obtain any coefficient.

## Blind held tournament

The decisive two-coordinate rows are:

| route | contact | observed | frozen prediction | signed residual | calibrated `n` residual |
|---|---|---:|---:|---:|---:|
| hard-core identity | deleted | `0.5477442451341502` | `0.5481199595627325` | `-0.00037571442858230775` | `0.003105667068317608` |
| hard-core identity | actual | `0.4977657325095556` | `0.4980485027698195` | `-0.0002827702602639093` | `0.002584220206359067` |
| hard-core signed Q2 | deleted | `0.5477442451341502` | `0.5481199595627325` | `-0.00037571442858230775` | `0.003105667068317608` |
| hard-core signed Q2 | actual | `0.4977657325095556` | `0.4980485027698195` | `-0.0002827702602639093` | `0.002584220206359067` |
| bosonic logical comparator | deleted | `0.5475598626738624` | `0.5481199595627325` | `-0.0005600968888701541` | `0.004630557505736377` |
| bosonic logical comparator | actual | `0.49759123507487835` | `0.4980485027698195` | `-0.0004572676949411436` | `0.004179674236027164` |
| independently labelled logical comparator | deleted | `0.5476938587655436` | `0.5481199595627325` | `-0.0004261007971889663` | `0.0035223243383666336` |
| independently labelled logical comparator | actual | `0.4977175100096359` | `0.4980485027698195` | `-0.0003309927601836127` | `0.0030250692192086426` |

The hard-core identity and signed-Q2 rows are strict variants of the physical
98-M2 route. The bosonic and independently labelled rows are lawful inherited
logical comparators on the common 4,096-state matter seam and frozen matter
readout. Cycle 328 explicitly leaves primitive synthesis of their Q factors
open, so this cycle does not relabel either comparator as a second 98-M2
physical compiler.

All 32 held rows—four routes, four `(n_A,n_B)` values, and two contact
codes—have zero lawful-sector leakage within tolerance. The maximum norm drift
is below `1.14e-14`.

## Additivity, monotonicity, and contact response

For each route and contact code, direct additivity would require

```text
p_11 - p_10 - p_01 + p_00 = 0.
```

It does not. The residuals are:

| route | deleted contact | actual contact |
|---|---:|---:|
| hard-core identity | `0.0330806550116346` | `0.029803805179849596` |
| hard-core signed Q2 | `0.0330806550116346` | `0.029803805179849596` |
| bosonic logical comparator | `0.03289627255134675` | `0.029629307745172362` |
| independently labelled logical comparator | `0.033030268643027494` | `0.02975558267993006` |

This rejects the direct affine/additive ansatz at the declared finite
resolution. It does not reject broader calibrations, other apparatuses,
other preparations, or a future physical source law.

The raw response is strictly monotone for every route and contact code:

```text
p_00 > p_10 = p_01 > p_11.
```

Actual-minus-deleted contact contrasts are nonzero and their magnitudes are
also monotone with the candidate multiplicity. For the hard-core route:

```text
n=0  -0.07945477346204322
n=1  -0.06307821812742653
n=2  -0.04997851262459463.
```

The bosonic and independently labelled `n=2` contrasts are respectively
`-0.04996862759898402` and `-0.049976348755907674`. The pointer remains
contact-sensitive throughout the tournament.

## Reciprocity, covariance, and physical code

The source-target swap residual `|p_10-p_01|` is below `4.5e-16` over every
route and contact setting. Thus the finite response respects A/B reciprocity
even though its composition is not additive.

The AB/BA physical matter encodings are both tested with the frozen pointer
map. Sampled decode, norm, and pointer-coordinate residuals remain below the
declared numerical tolerance. This tests the physical edge-role completion;
it does not derive endpoint-role genesis.

All 24 proper-cubic frames are tested, including twelve endpoint reversals.
The executable checks:

- the frozen readout intertwiner and symmetric ray;
- the inherited Cycle-315 seam update;
- hard-core Q1/Q2 candidate-input operators;
- bosonic Q1/Q2 comparator operators;
- the independently labelled local vertex; and
- the signed onsite-Q2 collision alternative.

Every residual is below the numerical tolerance. Proper-cubic covariance is
spatial covariance; it is not causal time.

## Mass and input ledgers

The Cycle-219 one-particle mass fixture and two-cell mass fixture remain

```text
0.4534056541748851,
```

with eigenvector residual `3.8571762755144336e-16`. The actual contact remains
nontrivial on 4,047 columns and its deletion operator norm remains
`1.9911500883709052`.

For hard-core and bosonic local Q1/Q2 operators, Hermiticity and commutators
with Q, endpoint matter number, and all three coefficient-two vector ledgers
are exactly zero. The independently labelled vertex retains unitarity and the
same Q/number/vector ledgers within numerical tolerance. These are input-law
ledgers. They do not identify the pointer response with any one ledger.

## Collision alternatives, deletions, and lawful domain

The signed onsite-Q2 collision comparator is unitary and proper-cubic. It is
exactly invisible to this frozen response across the tested cases. That is an
apparatus-specific collision-blindness result, not collision-law selection.

Deleting A or B from the two-coordinate actual-contact case changes the held
response by more than `0.12`; deleting both changes it by more than `0.27`.
Deleting contact changes the fine transcript by more than `0.3`. Deleting the
inverse matter coin, mapped edge FSWAP, or both recombination factors from the
readout changes the held coordinate by more than `1e-3`. These controls show
that the candidate coordinates, contact, and frozen apparatus are
load-bearing on this packet.

Malformed size, route, endpoint-bit, and contact-code inputs are rejected.
The permitted domain is exactly L3/L4 training and L6 held, two Boolean
endpoint coordinates, two contact codes, and the four declared comparator
labels.

## Supplied structure and novelty boundary

Supplied structure is:

1. the Cycle-315 complete matter seam, AB/BA encodings, matter coin, edge
   FSWAP, and actual Cycle-230 contact;
2. Cycle 331's hard-core exclusion code, reservoir preparation, source angle,
   coefficient-two ledgers, Q1 coin, and identity onsite-Q2 collision block;
3. Cycle 374's depth-two program-6 symmetric-ray pointer apparatus, primitive
   matrix-unit completion, and 98-M2 patch count;
4. the L3/L4 train split, zero/one-coordinate training menu, multiplicative
   model class, frozen tolerances, and blind L6 held menu;
5. the Cycle-328 bosonic and independently labelled logical comparator
   grammars; and
6. the signed onsite-Q2 collision comparator and every finite preparation,
   boundary, frame, and tolerance.

Derived here are the training coefficients, held transfer residuals,
additivity and monotonicity dispositions, source-target equality, and the
combined covariance/ledger/deletion/orientation certificate.

Not derived or selected are mediator statistics, a collision law, an
empirical unit, a universal coupling, physical input identification, a
physical energy/stress/source tensor, force, lapse, metric equation,
nonlinear backreaction, pointer branch, Record, actual member, or frequency
law.

Multiplicative attenuation models and train/held calibration are standard
methods. The bounded novelty claimed here is only their exact application to
this repository's frozen Cycle-374 apparatus and declared finite source-lane
comparators. Global novelty is not established. No Thirring engine is used or
compared.

## Dependency disposition

| wall | Cycle-387 movement | still open |
|---|---|---|
| `C_ref` | a frozen operational reference and training-only calibration object transfer to blind held cases | apparatus/model genesis, empirical reference, pointer occurrence, and actual member |
| `C_num` | one numerical response map is fixed before held data and transfers across the finite comparator menu | law selection, global domain, uncertainty/frequency, and empirical normalization |
| `C_wrap` | unchanged; contact code and update depth remain schedule labels | event equivalence, clock comparison, interval, rate, lapse, and causal-time bridge |
| `C_int` | actual-contact response stays nonzero across multiplicity/species comparators; direct additivity is falsified on this apparatus | interaction-selected occurrence, recurrent work ledger, protection, and physical calibration |
| `C_local` | the strict hard-core route remains a bounded 98-M2 all-frame AB/BA patch with zero held leakage | primitive network reuse, overlapping multi-edge deployment, and logical-comparator Q-factor synthesis |
| `C_source` | one fixed dimensionless multiplicative response calibration generalizes blindly across the declared finite tournament | physical source identification, universal coupling, energy/stress/tensor normalization, reciprocal clock/metric response, and nonlinear gravity |

The evidence supports a small conditional movement in the weakest lane, not a
far-side physical identification. Conservative planning estimates are:

| lane | integrated / strict / conditional | maturity |
|---|---:|---:|
| operational quantum / Records | `82/42/99` | `4.6/5` |
| causal time / clock | `53/33/91` | `3.6/5` |
| inertia / matter | `78/38/99` | `4.5/5` |
| gravity / source / resource | `45/18/76` | `2.6/5` |
| Born / probability / realized history | `45/16/97` | `2.9/5` |

## Negative-claim boundary

No bounded negative wall, minimum-content theorem, shared substrate
obstruction, or axiom-pressure claim is made. Therefore this cycle does not
invoke N1-N8 to ship a negative. The additive ansatz failure and signed-Q2
collision blindness are route-specific diagnostics with explicit live
alternatives: other response families, apparatuses, depths, preparations,
collision coins, statistics choices, multi-edge recurrences, and empirical
calibrations remain open.

There is no shared obstruction and no axiom pressure.

## Optimal next campaign

The highest-value continuation is a reciprocal multi-edge calibration test
that trains on one edge and predicts a separated target edge without changing
the frozen apparatus coefficients. It should compare the multiplicative
finite response against the existing Cycle-322 off-diagonal reciprocity and
Cycle-325 unit-weight route, require overlapping-network locality and a held
separation/size split, and keep all outputs operational until an independent
energy-stress/source or clock/metric bridge is derived.

## Verification

```text
python3 -m py_compile \
  scripts/physical_contact_sensitive_source_response_calibration_stress_cycle387_2026_07_18.py

PYTHONPATH=scripts python3 \
  scripts/physical_contact_sensitive_source_response_calibration_stress_cycle387_2026_07_18.py
```

Expected result:

```text
RESULT PHYSICAL_CONTACT_SENSITIVE_RESPONSE_CALIBRATION_BOUNDED_POSITIVE
```
