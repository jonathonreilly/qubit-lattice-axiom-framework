---
claim_id: gauge_vacuum_plaquette_full_two_slice_static_rho_identification_narrow_no_go_note_2026-08-22
claim_type: bounded_theorem
claim_scope: "At beta=6 on the finite periodic L_s=3 SU(3) Wilson lattice, the zero-fit forward identification C=s M D_loc diag(rho_static) M is rejected on the shared B_1 character sector by independent full-two-slice and static marked-factor-deletion ensembles. The frozen production packet has healthy acceptance, blocks longer than ten measured autocorrelation times, hot/cold agreement, full rank in the exact 15-dimensional symmetry basis, B_3-to-B_4 model drift of 0.01 primary-residual standard errors, a 17.73-standard-error largest coordinate discrepancy, zero rank failures and zero exceedances in 4096 null-centered replicate-studentized stratified two-ensemble block-bootstrap replicates, finite-resolution p=1/4097, and an exact one-sided 95% binomial upper bound 0.000731113 below the predeclared 0.001 gate. The chi-square tail is diagnostic only because the covariance is estimated. This rejects only the B_4-truncated static-rho plus fourth-power-local-factor identification on that finite surface; it does not reject Wilson gauge theory, prove that the physical residual is non-diagonal, establish an infinite-character or thermodynamic-limit result, or retire a TOE obligation."
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The fixed finite computation exactly certifies a statistical rejection under its declared protocol; population equality, an exact finite-volume integral, cutoff/volume limits, and the physical middle-operator law remain open."
trace_class: negative_route_pruning
target_claim_id: gauge_vacuum_plaquette_spatial_environment_character_measure_theorem_note
target_blocker_text: "the runner confirms algebraic consistency once a rho_env sequence is supplied, but it does not compute rho_(p,q)(6) from the unmarked spatial Wilson integral or independently verify that the residual operator spectrum equals those coefficients"
source_of_blocker_text: audit_ledger
reachability_to_target: prunes
artifact_role: runner_certificate
next_trace_action: "construct a common-Wilson-integral estimator for the general compressed middle operator and test held-out entries, then control character cutoff and finite-volume dependence"
conditional_surface_status: "statistical rejection only for the frozen L_s=3, beta=6, shared-B_1, auxiliary-B_4 protocol and the jointly supplied static-rho plus fourth-power-local-factor model"
hypothetical_axiom_status: null
admitted_observation_status: null
depends_on:
  - minimal_axioms
  - gauge_vacuum_plaquette_transfer_operator_character_recurrence_note
  - gauge_vacuum_plaquette_local_environment_factorization_theorem_note
  - gauge_vacuum_plaquette_spatial_environment_character_measure_theorem_note
runner: scripts/frontier_gauge_vacuum_plaquette_full_two_slice_compression_actual_l3_2026_08_22.py
runner_cache: logs/runner-cache/frontier_gauge_vacuum_plaquette_full_two_slice_compression_actual_l3_2026_08_22.txt
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Full Two-Slice Wilson Test of the Static-Environment Identification

**Date:** 2026-08-22

**Role:** finite-volume discriminator for the open gauge-vacuum
operator-compression bridge

**Claim type:** `bounded_theorem`

The conclusion is a narrow negative-route-pruning result inside that bounded
computational class, not a theorem-grade physical no-go.

**Primary runner:**
[`scripts/frontier_gauge_vacuum_plaquette_full_two_slice_compression_actual_l3_2026_08_22.py`](../scripts/frontier_gauge_vacuum_plaquette_full_two_slice_compression_actual_l3_2026_08_22.py)

**Cached receipt:**
[`logs/runner-cache/frontier_gauge_vacuum_plaquette_full_two_slice_compression_actual_l3_2026_08_22.txt`](../logs/runner-cache/frontier_gauge_vacuum_plaquette_full_two_slice_compression_actual_l3_2026_08_22.txt)

## Result up front

The production computation rejects one proposed shortcut through the
gauge-vacuum plaquette lane. On the finite periodic `L_s=3` `SU(3)` lattice at
`beta=6`, let `C_full` be the normalized marked-plaquette character matrix of
the literal full Wilson two-slice kernel. The tested identification is

```text
C_model = s M_beta D_beta^loc diag(rho_static) M_beta,
```

where:

- `M_beta=exp[(beta/2)J]` is the marked spatial half-weight multiplier;
- `D_beta^loc` is the fourth power of the normalized one-link mixed-kernel
  character coefficients;
- `rho_static` is measured independently from the actual 80-plaquette static
  spatial environment by the marked-factor-deletion identity; and
- `s` is fixed only by the common trivial entry `C_(0,0)=1`.

No matrix element, coupling, exponent, or environment coefficient is fitted
to `C_full`. On the shared `B_1={(0,0),(0,1),(1,0),(1,1)}` sector, using a
`B_4` auxiliary model projected onto `B_1`, the production result is

```text
symmetry-basis rank          = 15 / 15
chi-square / rank diagnostic = 503.75 / 15
bootstrap exceedances        = 0 / 4096
bootstrap rank failures      = 0 / 4096
bootstrap p resolution       = 1 / 4097 = 0.000244081
bootstrap 95% upper          = 0.000731113
largest discrepancy          = 17.73 standard errors
B_3 -> B_4 model shift        = 0.01 primary-residual standard errors
```

The largest discrepancy is the real fundamental diagonal entry:

```text
C_full[(0,1),(0,1)]  = 0.451465
C_model[(0,1),(0,1)] = 0.373961
combined SE           = 0.00437
```

Thus, under the frozen sampling, covariance, and bootstrap protocol, the
static-environment diagonal vector combined with the supplied fourth-power
local packet is statistically inconsistent with equality to the full
two-slice character matrix on this `B_4`-truncated tested surface.

This is not a failure of the Wilson transfer construction. It does not show
that the actual residual is non-diagonal, and finite Monte Carlo evidence is
not a deductive proof that the population matrices are unequal. It shows that
this fixed protocol does not license simply renaming the static
three-dimensional deletion coefficients as that residual while retaining the
tested local factor. An independent longer run, a valid alternative covariance
calibration, or an exact finite-volume evaluation could falsify the statistical
conclusion.

## 1. Exact physical surface tested

The full ensemble is the temporal-gauge one-step Wilson weight on two spatial
slices. Each slice has 81 links and 81 spatial plaquettes. The action used by
the runner contains exactly:

- 81 incoming spatial half-plaquette factors with coefficient `beta/6`;
- 81 outgoing spatial half-plaquette factors with coefficient `beta/6`; and
- 81 mixed-link factors with coefficient `beta/3`.

For link configurations `U_0,U_1`, the sampled exponent is

```text
(beta/6)[sum_p Re Tr W_p(U_0) + sum_p Re Tr W_p(U_1)]
 + (beta/3) sum_l Re Tr[U_1(l) U_0(l)^dagger].
```

The runner recomputes a hostile local link update against the full exponent.
It also executes a wrong-action mutation in which the spatial half weights
are doubled; that mutation is rejected.

For every marked face, it measures

```text
C_(lambda,mu)
 = <conj(chi_lambda(W_1)) chi_mu(W_0)>_full,
```

and averages over all 81 translated/oriented faces. The outgoing conjugation
is checked by a hostile orientation control.

The exact Wilson transfer and marked-source grammar are supplied by
[`GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md).
That source does not supply the residual identification tested here.

## 2. Independent static comparator

The static ensemble is the full 81-plaquette three-dimensional Wilson measure
at the same `beta=6`. For each face the marked Wilson factor is divided out
configuration by configuration, and the normalized character ratios are
computed. The exact finite-volume deletion identity and its direct
80-plaquette cross-check are supplied by
[`GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_CHARACTER_MEASURE_THEOREM_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_CHARACTER_MEASURE_THEOREM_NOTE.md).

The full and static ensembles use disjoint seeds. Each has four chains, two
hot and two cold. The forward test therefore does not estimate the comparator
from the same configurations used to estimate `C_full`.

The fourth-power local diagonal is the finite packet constructed in
[`GAUGE_VACUUM_PLAQUETTE_LOCAL_ENVIRONMENT_FACTORIZATION_THEOREM_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_LOCAL_ENVIRONMENT_FACTORIZATION_THEOREM_NOTE.md).
That source explicitly does not prove that its consumer-side packet is the
physical mixed-kernel compression. The present test consequently constrains
only the product of that local packet with the static residual ansatz.

The import inventory is explicit. The finite periodic `L_s=3` geometry,
Wilson action, and `beta=6` coupling define the supplied simulation surface;
they are not derived from the minimal axioms. The recurrence source supplies
the marked multiplier grammar, the local-factor source supplies only its
consumer-defined fourth-power packet, and the static-environment source
supplies its finite marked-deletion estimator. All numerical matrix entries in
this note are computed from those declared inputs. No observed plaquette
target, fitted physics parameter, external empirical value, or audit verdict
is imported. Independent audit alone controls the claim's audit and effective
status.

## 3. Forward test and cutoff control

Directly applying `D^(-1)M^(-1)` is numerically unsuitable. On `B_2`, the
diagnostic amplification

```text
cond(D) cond(M)^2 = 1.092e10
```

makes an inverse-space claim fragile. The physics test is therefore entirely
forward. Each leave-one-block static estimate is transformed through the
model; each leave-one-block full estimate is normalized on its own. Because
the two ensembles are independent, their jackknife covariance matrices are
added.

The full character matrix is sampled on `B_2`. The primary comparison uses
its literal `B_1` block. The model is built successively on `B_1`, `B_2`,
`B_3`, and `B_4`, then projected onto that same `B_1` target. This matters
because

```text
P_1 exp(3J_2) P_1 != exp(3 P_1 J_2 P_1).
```

The observed model drifts are

```text
||P_1 C_model,2 P_1 - C_model,1||_F = 1.885e-1
||P_1 C_model,3 P_1 - C_model,2||_F = 4.449e-3.
||P_1 C_model,4 P_1 - C_model,3||_F = 4.236e-5.
```

The last shift is `0.01` of the largest corresponding primary-residual
standard error, below the predeclared two-standard-error error-budget gate.
This ratio is not called a paired significance: its denominator includes the
full and static uncertainty relevant to the primary comparison. The
`B_1`-only model is therefore not used for the conclusion.

This is a finite cutoff check, not an infinite-character convergence proof.

## 4. Sampling and covariance health

The production protocol is fixed at four chains per ensemble, 900
thermalization sweeps, 2400 measurement sweeps, sampling every four sweeps,
and 12 equal blocks per chain. It supplies 48 blocks per ensemble.

| Check | Full two-slice | Static comparator | Gate |
|---|---:|---:|---:|
| acceptance | `0.544..0.546` | `0.509..0.511` | inside `0.25..0.80` |
| samples per block | `50` | `50` | — |
| maximum measured `tau_int` | `2.40` | `2.21` | block `>10 tau_int` |
| maximum hot/cold chain deviation | `3.90` grand-mean SE | `1.13` grand-mean SE | `<5` |

The normalized residual covariance is positive semidefinite at numerical
tolerance. Rather than discover a numerical subspace from the same data, the
runner uses the exact character identity

```text
C_(bar(lambda),bar(mu)) = conjugate(C_(lambda,mu))
```

and removes the fixed `C_(0,0)=1` coordinate. That gives an explicit
15-dimensional real symmetry basis on `B_1`; the covariance has full rank
`15/15` there. The largest discrepancy lies in a real diagonal character
entry, not in an antisymmetric or imaginary equilibration-control direction.

The displayed chi-square value `503.75` has an asymptotic known-covariance
tail of `9.09e-98`, but that tail is diagnostic only: the covariance is
estimated from these finite blocks. The decision gate instead uses 4096
deterministic, null-centered bootstrap replicates. Each replicate resamples
the 12 blocks within each of the four full chains and each of the four static
chains, recomputes both nonlinear normalizations and the forward model, then
centers the resulting residual on the observed residual to impose the null.
It also recomputes the two-ensemble leave-one-block covariance inside that
replicate and uses it to studentize the null residual. A non-PSD, nonfinite,
or rank-deficient replicate is conservatively counted as an exceedance; the
certificate additionally requires zero such rank failures.

Zero replicates reach the observed studentized statistic, giving the
finite-resolution value and exact one-sided 95% binomial upper bound

```text
p_boot = (0+1)/(4096+1) = 0.000244081 < 0.001.
p_boot,95% upper = 0.000731113 < 0.001.
```

The frozen production configuration is itself a gate; non-pilot CLI
overrides cannot emit this certificate. The conclusion does not depend on the
ill-conditioned inverse diagnostic, the asymptotic tail, or the rank-limited
`B_2` diagnostic.

## 5. Scientific consequence

The following `B_4`-truncated finite identification is rejected on the tested
shared-`B_1` surface:

```text
physical compressed middle operator
  = D_beta^loc diag(rho_static)
```

with `D_beta^loc` and `rho_static` typed exactly as above.

The result separates three questions that earlier packets kept open:

1. Is the combined physical middle operator `Q` diagonal in the marked
   character basis?
2. If it is diagonal, are its values the static full-strength spatial
   deletion coefficients?
3. Is the fourth-power one-link packet the correct physical local factor in
   the compressed full-slice kernel?

This runner tests only the conjunction used by the displayed forward model.
It cannot assign the discrepancy uniquely between questions 2 and 3, because
the measured matrix sees their product. It also cannot reject question 1:
a general symmetry-constrained middle operator has not yet been estimated and
tested predictively.

The highest-leverage continuation is therefore to derive a common-Wilson-
integral estimator for a general Hermitian, positive, conjugation-symmetric
middle operator `Q`, then test it on held-out matrix entries or independent
ensembles. Only if its off-diagonal sector is negligible should a corrected
diagonal law be sought. Extra statistics on the already rejected static law
are low leverage.

## 6. Axiom decision

No edit to
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) is warranted.
That memo deliberately leaves transfer operators, source/action selection,
physical-observable identification, and dynamics downstream of the four
minimal axioms. The present mismatch is exactly a downstream physical-law
question. It neither contradicts Lattice, Qubit, Admissibility, or Record nor
demonstrates that a new primitive is necessary or unique.

Adding a static-diagonal compression rule to the axioms would stipulate the
very identification rejected here. Adding a general matrix residual would
likewise promote an as-yet unclassified effective object to ontology. Both
would choose physics instead of deriving it.

No TOE obligation, audit verdict, or lane percentage is changed by this
source packet. A future audited positive `Q` law could move the gauge lane; a
narrow rejection alone does not.

## 7. What is and is not claimed

**Claimed:**

- the implemented finite `L_s=3`, `beta=6` two-slice Wilson action passes its
  exact census, delta, and orientation controls;
- the independent static-diagonal zero-fit forward model is stable from
  auxiliary `B_3` to `B_4` at the resolution of the test;
- that model is rejected on shared `B_1` under the declared production and
  covariance protocol.

**Not claimed:**

- a no-go for Wilson gauge theory or the gauge-vacuum plaquette lane;
- proof that the actual physical residual is non-diagonal;
- a separate falsification of `D_beta^loc` or `rho_static` individually;
- an infinite-character, continuum, or thermodynamic-limit result;
- a reference plaquette value or a repinning of any observable;
- a retained result before independent audit;
- an axiom or primitive update.

## 8. No-Go Discipline Gate

Because the packet contains a negative conclusion, the N1--N8 protocol is
applied. The broad statement “the gauge seam cannot work” fails this gate and
is not shipped.

### N1 — alternative-route enumeration

The following materially distinct challenges to the exact bounded rejection
were executed. Each is dispositioned as `ATTEMPTED`; no unexecuted route is
used to support the negative claim. The runner and SHA-bound cache are the
current-cycle evidence for these attempts; none is marked `RULED OUT BY PRIOR`,
and this unaudited packet attributes no retained grade to itself or its source
notes.

| Challenge to the narrow rejection | Exact execution/disposition |
|---|---|
| Wrong full-slice action or factor census | **ATTEMPTED.** The production sweep and `local_delta_control` share `two_slice_local_log_weight`; that implementation is checked against an independent full recomputation of all `81+81+81` factors, and the doubled-spatial-strength mutation fails. See the [primary runner](../scripts/frontier_gauge_vacuum_plaquette_full_two_slice_compression_actual_l3_2026_08_22.py) and its SHA-bound [cache](../logs/runner-cache/frontier_gauge_vacuum_plaquette_full_two_slice_compression_actual_l3_2026_08_22.txt). |
| Wrong character orientation or conjugation reduction | **ATTEMPTED.** The production sampler and hostile control share `character_cross_moment`; the independent outer-product expectation passes and the unconjugated mutation fails. The exact conjugation-orbit basis then has dimension and rank `15/15`. See the primary runner and cache above. |
| Failure of the declared acceptance, blocking, autocorrelation, or hot/cold diagnostics | **ATTEMPTED.** Four disjoint-seed chains per ensemble pass acceptance, `block>10 tau_int`, and the declared grand-mean chain-deviation gate in the primary runner and cache. This does not rule out every slow mode; N7 keeps that population-level attack open. |
| Misimplementation of the declared covariance, normalization, resampling, or coordinate protocol | **ATTEMPTED.** Independent small-array controls check trivial-channel normalization, charge projection, the 15-coordinate ordering, jackknife covariance, within-chain resampling, null centering, binomial-tail arithmetic, and strict gate boundaries. Every bootstrap replicate recomputes and full-rank checks its own two-ensemble covariance before comparison. Alternative valid calibrations remain an N7 falsifier. |
| Resolved `B_3`-to-`B_4` projection drift exceeds the declared shared-`B_1` budget | **ATTEMPTED.** Successive projected model drifts fall from `1.885e-1` to `4.449e-3` to `4.236e-5` through `B_4`; the last is `0.01` primary-residual SE. Independent `expm` and coefficient-power controls pin the multiplier and local-factor formulas. No `B_5` or infinite-sector tail is claimed. |
| Ill-conditioned algebraic inverse | **ATTEMPTED.** The conclusion is computed entirely forward; the `1.092e10` inverse amplification is printed only as a non-gating diagnostic. |

Broader positive gauge routes survive, but they do not negate the fixed
protocol's statistical rejection:

| Broader route | Evidence/disposition |
|---|---|
| General middle operator `Q` | **OPEN nearby positive construction.** [`GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_CHARACTER_MEASURE_FINITE_BOX_CONVOLUTION_REALIZATION_UNIQUENESS_NARROW_NOTE_2026-05-17.md`](GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_CHARACTER_MEASURE_FINITE_BOX_CONVOLUTION_REALIZATION_UNIQUENESS_NARROW_NOTE_2026-05-17.md) gives an explicit positive swap-symmetric off-diagonal operator, showing that positivity and symmetry do not force the tested diagonal class. A physical common-integral estimator remains unexecuted. |
| Two-slice-derived corrected diagonal | **OPEN nearby positive construction.** The literal doubled-slice deletion runner estimates a different diagonal candidate while explicitly separating deletion from algebraic stripping; a compression-aware diagonal law remains unexecuted. |
| Rank-aware analytic/recoupled contraction | **OPEN reopening route.** [`BETA6_PLAQUETTE_CLOSURE_NOTE_2026-05-29.md`](BETA6_PLAQUETTE_CLOSURE_NOTE_2026-05-29.md) records a rank-aware contractor or new analytic compression; neither is executed by this packet. |

The literal-factor-deletion matrix in
[`scripts/frontier_gauge_vacuum_plaquette_residual_environment_spectrum_actual_l3.py`](../scripts/frontier_gauge_vacuum_plaquette_residual_environment_spectrum_actual_l3.py)
is not another execution of the algebraic-stripping route; its own boundary
says so.

### N2 — wall-independence audit

Define three remaining positive-program walls:

- `W_Q`: identify the physical combined middle operator and its structure;
- `W_N`: control the character cutoff beyond the observed `B_4` stability;
- `W_L`: control finite-volume dependence.

These walls do not support the fixed-protocol statistical rejection; they
bound any stronger physical or limiting conclusion. `W_N` does not identify
`Q`, and `W_Q` on one box does not prove cutoff
control. Neither supplies `W_L`; a volume sequence does not determine the
operator structure. Within `W_Q`, “wrong local factor” and “wrong residual
values” are not independently resolved by this measurement because only
their product enters the forward model.

The required pairwise closure test is therefore:

| Wall pair | Closing the first closes the second? | Closing the second closes the first? | Independent? | Reason |
|---|---:|---:|---:|---|
| `W_Q` / `W_N` | No | No | Yes | Identifying the finite combined operator does not control omitted characters; a tail bound does not identify that operator. |
| `W_Q` / `W_L` | No | No | Yes | An operator at one volume gives no volume law; a volume sequence does not determine its internal structure. |
| `W_N` / `W_L` | No | No | Yes | Character-tail control at one volume gives no finite-size law; finite-size control does not bound omitted characters. |

Sampling is not kept as a free explanatory wall for the narrow result:
acceptance, autocorrelation, hot/cold agreement, covariance support, and
independent seeds all pass their declared gates.

### N3 — hidden-condition scan

| Phrase/object | Actual status in this packet |
|---|---|
| `D_beta^loc` | supplied finite fourth-power packet; not a proved physical compression |
| `rho_static` | independently measured static 80-plaquette boundary coefficients |
| `diag(rho_static)` | tested ansatz, not inferred from centrality of the static density |
| `B_4` stability | finite error-budget check, not an infinite-sector theorem |
| `L_s=3` | finite periodic lattice, not a thermodynamic proxy by declaration |
| `p` value | supported-covariance hypothesis test under the fixed production protocol |
| `ansatz` | explicit load-bearing null model, fully typed in Sections 1--3 rather than a hidden premise |
| `normalization` | explicit load-bearing transformation fixed by the trivial channel and independently controlled in the runner |
| `sector` | explicit load-bearing finite domain: shared `B_1`, sampled `B_2`, auxiliary models through `B_4` |
| `boundary` | either the defined static coefficients or cited source-scope context; no extra condition is hidden by the word |
| `axiom` / `primitive` | cited governance context only; neither supplies the Wilson action, model, or numerical conclusion, as N6 records |
| `wall` | the three stronger-positive-program limits are explicit in N2 and are not premises of the fixed-protocol rejection |

The literal trigger scan has no remaining unclassified hit. No fitted
plaquette target, observed reference value, inverse reconstruction, or
axiom-selected gauge law enters the result.

### N4 — residual matching

Every prior wall or apparent witness cited for this claim is matched below.
The current residual is the bounded conjunction

```text
C_full - s M D_loc diag(rho_static) M = 0
```

on the finite `L_s=3`, `beta=6`, shared-`B_1`, auxiliary-`B_4` surface. It
tests the static-to-stripped identification only together with the separately
supplied fourth-power local packet, so the rejection cannot assign blame
between those two ingredients.

| Cited source and exact locator | Residual in that source | Current claimed residual | Exact match? |
|---|---|---|---:|
| [`GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_CHARACTER_MEASURE_THEOREM_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_CHARACTER_MEASURE_THEOREM_NOTE.md), `docs/GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_CHARACTER_MEASURE_THEOREM_NOTE.md:12-14,183-190` | Identify the measured static boundary coefficients with the algebraically stripped full two-slice source residual after an exact compression and stripping construction. | A finite `B_4` forward conjunction with the separately supplied `D_loc`, read on shared `B_1` and rejected statistically. | **No**: the finite truncation, supplied local factor, and statistical decision surface differ from the exact residual left open there. |
| [`GAUGE_VACUUM_PLAQUETTE_COMPRESSION_SCOPE_RHO_COMPLETE_INTERFACE_NARROW_THEOREM_NOTE_2026-06-12.md`](GAUGE_VACUUM_PLAQUETTE_COMPRESSION_SCOPE_RHO_COMPLETE_INTERFACE_NARROW_THEOREM_NOTE_2026-06-12.md), `docs/GAUGE_VACUUM_PLAQUETTE_COMPRESSION_SCOPE_RHO_COMPLETE_INTERFACE_NARROW_THEOREM_NOTE_2026-06-12.md:23-30,117-134` | Readout completeness after a diagonal residual is supplied; physical diagonality and static-to-stripped identification are excluded. | A Wilson-derived forward equality for one proposed diagonal residual. | **No**. |
| [`scripts/frontier_gauge_vacuum_plaquette_residual_environment_spectrum_actual_l3.py`](../scripts/frontier_gauge_vacuum_plaquette_residual_environment_spectrum_actual_l3.py), `scripts/frontier_gauge_vacuum_plaquette_residual_environment_spectrum_actual_l3.py:10-15,305-307` | Literal deletion before compression; explicitly not the algebraically stripped operator. | Compression-aware full-forward equality. | **No**. |
| [`BETA6_PLAQUETTE_CLOSURE_NOTE_2026-05-29.md`](BETA6_PLAQUETTE_CLOSURE_NOTE_2026-05-29.md), `docs/BETA6_PLAQUETTE_CLOSURE_NOTE_2026-05-29.md:96-112,392-406` | Broader analytic/thermodynamic `P(6)` closure, including environment data, operator compression, and analytic-class control. | One finite-volume, finite-character operator-identification conjunction. | **No**. |

After dropping non-matches, the prior-witness count is zero. That does not
weaken the bounded certificate because it relies on the new direct runner and
cache, not on a prior no-go or wall as proof. All four citations above are
boundary context only; none is counted as evidence that the current composed
residual was previously tested.

### N5 — rhetoric and resolution audit

| Resolution | Execution declaration | Licensed statement |
|---|---|---|
| per-element | **checked and executed** | all coordinates of the normalized shared `4x4` matrix enter the supported-covariance test |
| per-site | **checked and not executed —** all 81 faces are symmetry-averaged | no individual-face equality is tested or certified |
| per-mode | **checked and partially executed —** `B_1` physics surface, `B_2` sampled box, auxiliary models through `B_4` | no `B_5` or infinite-character statement |
| per-block | **checked and executed** | 48 leave-one-block transforms in each independent ensemble |
| lattice-wide | **checked and partially executed —** one periodic `L_s=3` lattice at `beta=6` | no volume sequence or thermodynamic statement |

The runner prints matching `per_element:`, `per_site:`, `per_mode:`,
`per_block:`, and `lattice_wide:` lines. “Rejected” always refers to the
displayed static-rho forward identification on that bounded surface.

### N6 — partial-closure path and primitive scan

The positive partial-closure path is

```text
general Q estimator
 -> symmetry/positivity classification
 -> held-out prediction
 -> corrected diagonal law if licensed
 -> B_5/tail and L_s sequence.
```

The approved primitive registry supplies no gauge-residual selector. Minimal
Admissibility supplies a probability-distribution slot, not the Wilson action
or its compressed transfer operator. No primitive is being relabeled as a
wall, and no axiom update closes `W_Q`, `W_N`, or `W_L`.

### N7 — strongest steelman

**Hostile argument against the negative claim.** Forty-eight blocks per
ensemble, a measured autocorrelation margin, hot/cold agreement, and 4096
null-centered bootstrap replicates do not constitute a proof of the exact
finite-volume population matrix. A longer independent simulation could expose
slow modes missed by the measured `tau_int`; a different valid dependent-data
calibration could change the tail; or an exact finite-volume contraction could
land inside the equality class. The strongest supporting authority is the
[static-environment source](GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_CHARACTER_MEASURE_THEOREM_NOTE.md),
which at lines 23--27 labels its `beta=6` values computed inputs rather than
exact arithmetic and at lines 183--191 leaves the compression-aware comparison
open. The terminal falsifier is concrete: reproduce the same normalized
shared-`B_1` residual with independently seeded longer chains and conservative
blocking/calibration, or compute it by an independent exact/controlled
contraction.

That steelman defeats a categorical physical no-go, so this packet demotes to
the fixed-protocol `bounded_theorem` certificate stated in the frontmatter. It
does not defeat the deterministic statement that the frozen computation and
its declared decision rule return a statistical rejection. The population
equality and any stronger no-go remain open.

Nearby positive constructions also remain live. Unmarked spatial plaquettes
couple the nonmarked mixed-link integrations, so the true middle object may be
a positive conjugation-symmetric matrix `Q`; an explicit finite-box
[positive off-diagonal witness](GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_CHARACTER_MEASURE_FINITE_BOX_CONVOLUTION_REALIZATION_UNIQUENESS_NARROW_NOTE_2026-05-17.md)
shows that positivity and symmetry do not force a diagonal class. A corrected
diagonal from a two-slice conditional measure also remains possible, and the
[local-factor source](GAUGE_VACUUM_PLAQUETTE_LOCAL_ENVIRONMENT_FACTORIZATION_THEOREM_NOTE.md)
states that its fourth-power packet is constructed rather than a derived
physical compression. These routes preserve a predictive Wilson gauge law and
define the general-`Q` held-out continuation.

### N8 — cross-cycle echo

The result agrees with the prior scope corrections rather than silently
reusing their walls:

| Similar prior wall | Retired? | Mechanism since that cycle | Could that mechanism apply here? |
|---|---|---|---|
| Static density equals the stripped residual by literal deletion ([campaign ledger](../.claude/science/physics-loops/gauge-plaquette-spatial-env-character-20260710/NO_GO_LEDGER.md), `.claude/science/physics-loops/gauge-plaquette-spatial-env-character-20260710/NO_GO_LEDGER.md:3-12`) | **No audit-grade retirement asserted.** The campaign ledger records literal deletion as a falsified proof route while leaving physical equality open. | The ledger required construction and stripping of the full compressed two-slice operator; this packet executes a bounded forward discriminator but still tests `D_loc` and `rho_static` jointly. | **Yes.** Carry the ledger reopening condition into the common-integral general-`Q` construction and held-out test. |
| Supplied-diagonal completeness versus physical membership ([scope correction](GAUGE_VACUUM_PLAQUETTE_COMPRESSION_SCOPE_RHO_COMPLETE_INTERFACE_NARROW_THEOREM_NOTE_2026-06-12.md), `docs/GAUGE_VACUUM_PLAQUETTE_COMPRESSION_SCOPE_RHO_COMPLETE_INTERFACE_NARROW_THEOREM_NOTE_2026-06-12.md:17-30`) | **No audit-grade retirement asserted.** The current audit row is unaudited; the source supplies conditional algebra and excludes physical membership. | This packet statistically rejects one supplied static-diagonal instance in forward form; it does not construct the physical operator. | **Yes.** Preserve the conditional algebra while replacing the supplied diagonal by a common-integral general `Q`. |
| Actual mixed-kernel compression bridge ([local-factor boundary](GAUGE_VACUUM_PLAQUETTE_LOCAL_ENVIRONMENT_FACTORIZATION_THEOREM_NOTE.md), `docs/GAUGE_VACUUM_PLAQUETTE_LOCAL_ENVIRONMENT_FACTORIZATION_THEOREM_NOTE.md:110-122,134-141`) | **No.** Its current audit row is unaudited. | No independent derivation has isolated the physical `D_loc`; the present conjunction cannot allocate its mismatch. | **Yes.** The general-`Q` estimator can absorb the combined operator first, after which a local-factor split can be tested separately. |
| Static coefficient evaluation versus static-to-stripped identification ([environment gate](GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_CHARACTER_MEASURE_THEOREM_NOTE.md), `docs/GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_CHARACTER_MEASURE_THEOREM_NOTE.md:8-14,142-190`) | **No audit-grade retirement asserted.** Its current audit row is unaudited; the source computes low-rank static coefficients and leaves identification open. | Exact marked-factor deletion plus independent Monte Carlo supplies the static vector; this packet statistically rejects its direct use in the bounded conjunction. | **Yes.** Reuse independent estimation and a common Wilson integral for `Q`, not the rejected renaming. |
| Broad beta-six environment/compression/analytic wall ([closure synthesis](BETA6_PLAQUETTE_CLOSURE_NOTE_2026-05-29.md), `docs/BETA6_PLAQUETTE_CLOSURE_NOTE_2026-05-29.md:96-112,382-406`) | **No.** No audit-grade retirement is attributed here. | Rank-aware contraction or a new analytic compression remains the recorded reopening route. | **Yes.** A stable low-complexity `Q` would be such a compression; failure across cutoff and volume would instead sharpen the wall. |

The present packet executes the previously named discriminator and gives its
narrow negative answer. It does not turn those earlier conditional
constructions into broad no-go authorities.

**Strongest honest disposition:** `bounded-with-corrected-wall-count`: the
frozen finite protocol returns a statistical rejection of the declared
static-rho forward identification. This is not a `no_go` disposition.

**Gate result:** PASS for that bounded fixed-protocol certificate after the N7
demotion. FAIL for a categorical finite-volume equality no-go, a universal
gauge no-go, a proof of nondiagonality, an infinite/thermodynamic conclusion,
or an axiom update; none is shipped.

## Verification

Run:

```bash
python3 scripts/frontier_gauge_vacuum_plaquette_full_two_slice_compression_actual_l3_2026_08_22.py
```

Expected final line:

```text
TOTAL: PASS=16 FAIL=0
```

The production runner exits successfully only when implementation controls,
sampling health, chain agreement, cutoff stabilization, covariance support,
and the predeclared rejection gate all pass.
