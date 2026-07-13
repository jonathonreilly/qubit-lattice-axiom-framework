# R-Half Open Backlog Formation-Law Probe Batch

**Date:** 2026-07-13
**Type:** bounded support theorem
**Claim type:** bounded_theorem
**Artifact role:** exact support batch
**Status:** branch-local exact support and frontier discovery; independent audit
authority only.
**Primary runner:**
[`scripts/frontier_rhalf_open_backlog_probes_2026_07_13.py`](../scripts/frontier_rhalf_open_backlog_probes_2026_07_13.py)
**Cached output:**
[`logs/runner-cache/frontier_rhalf_open_backlog_probes_2026_07_13.txt`](../logs/runner-cache/frontier_rhalf_open_backlog_probes_2026_07_13.txt)

## Purpose and authority boundary

This note starts exact probes on every open science item in the `r=1/2`
formation backlog.  It extracts finite algebraic reductions and falsifiers;
it does not adopt a formation convention or promote a physical conclusion.

The licensing-consolidation proposal formerly carried by PR 5326 is closed
and unmerged as of this block's start.  Its proposed licensing criterion is
therefore not consumed as current-main authority here.  When this note uses
the two weights `w=1/3` and `w=1/2`, it uses them only as the two already
exhibited formation resolutions on current main.  When it converts `w` to
`r`, it explicitly conditions on the declared energy dictionary

```text
r = (1-w)/(2w).
```

That dictionary remains a modeling input, not a derived framework law.

## Probe summary

| Backlog item | Exact result in this batch | What remains open |
|---|---|---|
| Formation selector | `w=1/3` and `w=1/2` are normalized weights obtained from equal per-event hazards on two different event resolutions: carrier members versus K-orbit cells. | Which objects are formation-stage event atoms, and what dynamics sets their relative hazards. |
| Registration bridges | For a supplied Hermitian spectral decomposition, a three-projector controlled-copy instrument can register `lambda_k^2`; it does not select the positive spectral branch. Three distinct squared labels pay the algebraic `ND3` comparator, while nonzero support is a separate stronger condition. | Derivation of the pointer/readout identification, positivity of `lambda_k`, distinct physical spectral values, and formation support. |
| Law equivalence across epochs | One fixed formation-weight law need not give the same marginal vector when complete record environments differ. Transport-equivalent complete conditions are sufficient in the explicit covariant probe. | A formation-law theorem that makes complete conditions equivalent across the compared epochs. |
| Time homogeneity and history faithfulness | A separate supplied transfer law likewise need not give the same matrix in changed conditions. A linear realized history becomes a cycle plus one seam; removing that seam recovers the line, while marking it only identifies the extra datum. | A physical transfer/time law and an operator representation with a cut or a supplied rule for the marked seam. |
| K-stage supply | On `C_n`, carrier-uniform and K-orbit-cell-uniform formation are different measures. On `C_3` they give `1/3` and `1/2` respectively. | Whether the K quotient/orbit is supplied before formation events are counted. |
| Many-slice transfer | A one-parameter two-state Markov correlation law interpolates exactly between quenched and annealed histories. | A formation law selecting the persistence parameter or a different correlation structure. |
| Krein remainder | For the standard doubled transfer and fundamental symmetry, the canonical J-positive half is invariant exactly on the Hermitian tie. | Other fundamental symmetries, positive graph subspaces, metrics, quotients, or noncanonical readouts remain open. |
| Quadratic two-slice transfer factor `A_2(W)=W^2+I/4` | Positive `A_2(W)` can coexist with non-Hermitian `W`, and `A_2(W)` cannot distinguish `W` from `-W`. | A branch/readout law that reconstructs the physical `W` data from `A_2(W)`, if that is the intended route. |
| Beyond two-slice `C_3` | The K-orbit count and the two competing uniform weights are computed for general finite `C_n`. | A physical reason that selects a particular `n`, resolution, and many-slice law. |

## 1. Formation resolution and normalized hazards

Let the fine carrier event set be

```text
A_carrier = {s, d_1, d_2}
```

and let K identify the paired members into

```text
A_cell = {s, d},  d = {d_1,d_2}.
```

Uniform formation events on the two sets give

```text
w_carrier = 1/3,
w_cell    = 1/2.
```

Equivalently, in a normalized two-channel hazard model with singlet hazard
`h_s` and aggregate doublet hazard `h_d`,

```text
w = h_s/(h_s+h_d).
```

Equal hazards per quotient cell give `h_s:h_d=1:1` and `w=1/2`.  Equal
hazards per carrier member give the aggregate ratio `h_s:h_d=1:2` and
`w=1/3`.  Conditional on the declared energy dictionary, these become
`r=1/2` and `r=1`.

This is a reduction, not a selector theorem.  Normalization does not decide
which event resolution or hazard law is physical.  It identifies a sharp
formation-dynamics target: determine the atomic event object before applying
the counting or hazard normalization.

## 2. Projective registration probe

For a supplied Hermitian spectral decomposition

```text
W = sum_k lambda_k P_k,  lambda_k real,
```

define the finite record write

```text
V|psi> = sum_k |k> tensor P_k|psi>.
```

Then `V^dagger V=I` and the extracted record blocks are `P_k`.  This is the
three-label version of the current bounded controlled-copy/Kraus machinery.
Calibrating the record-register pointer to

```text
M_R = sum_k lambda_k^2 |k><k|
```

gives the exact pullback

```text
V^dagger (M_R tensor I) V
  = sum_k lambda_k^2 P_k
  = W^2
```

on the supplied Hermitian spectral decomposition.  This constructs an exact
finite instrument that records the squared spectral values, conditional on
the pointer projectors and calibration being supplied.  For the explicit
full-support state `rho=I/3`, the runner separately computes
`Tr(P_k rho)=1/3` for all three outcomes rather than stipulating occurrence.

Hermiticity/real spectrum is load-bearing for the nonnegative-square reading:
the runner includes the complex-spectrum control `i^2=-1`.  Under the stated
Hermitian premise, the construction separates three bridges that must not be
conflated:

1. `W^2` or squared-value registration gives nonnegative values but erases
   the sign of `lambda_k`.
2. The positive square root gives `|lambda_k|`, which is the absolute-value
   branch, not a derivation of `lambda_k >= 0`.
3. The algebraic `ND3` comparator requires three distinct registered values.
   Under this calibration that means three distinct values of `lambda_k^2`.
   Three distinct signed spectral values alone are insufficient: `(-1,1,3)`
   has only the two squared values `(1,1,9)`.
4. Nonzero probabilities for all three instrument outcomes are a separate,
   stronger support condition.  The explicit `rho=I/3` witness shows that
   full support is compatible with the instrument; it neither derives a
   formation state nor guarantees that every outcome is realized in a finite
   history.

Thus the existing finite record-write machinery supplies a concrete route to
test `B_map` and, conditional on distinct squared labels, the algebraic `ND3`
comparator.  It does not pay for `B_plus`, physical spectral distinctness, or
formation support by itself.

## 3. Epoch equivalence for formation weights and transfer matrices

The two open law questions have different codomains and must not be joined by
an unstated bridge.

For the formation-marginal question, write

```text
phi_t = F(c_t),  F:C_form -> Delta({s,d}).
```

Using the same function `F` at two epochs is law identity.  It need not give
the same marginal vector when permanent records or their environments make
the complete conditions inequivalent.  The runner defines a nontrivial
transport on two distinct condition tuples and an explicitly covariant
finite `F`; transport-equivalent conditions give the same `phi`, while a
changed record environment gives a different `phi` under that same `F`.

For time homogeneity, introduce a separate supplied matrix-valued transfer
law

```text
W_t = G(d_t),  G:C_transfer -> End(H).
```

The same finite logic holds: transport-equivalent `d_t` give the same matrix
under the explicit covariant `G`, while changed conditions can give different
matrices under the same `G`.  Conversely, a noninjective `G` can give equal
matrices for inequivalent conditions.

This probe does not supply a map `phi_t -> W_t` and does not derive condition
`H` from the G3 formation-law premise.  It isolates two parallel theorem
targets: epoch equivalence on `C_form` for identical marginals, and either
epoch equivalence on `C_transfer` or a direct transfer-dynamics theorem for
`H`.

## 4. History representation and the compactification seam

The directed linear history

```text
0 -> 1 -> ... -> T
```

has edge set `{(t,t+1):0<=t<T}`.  Compactification to `Z/(T+1)Z` adds exactly
the seam `(T,0)`.  Removing that edge recovers the linear history exactly.
Marking it only identifies the extra datum; a supplied operator rule must
still exclude it from forward transfer or assign it a special role.

For the explicit nested permanent-growth witness

```text
R_t = {0,...,t-1},  |R_t|=t,
```

every linear edge obeys `R_t subset R_(t+1)`, while `R_T` is not a subset of
`R_0` across the seam.  The witness does not establish a global obstruction
to all periodic representations.  It establishes that an ordinary
homogeneous wrap edge is not the forward-history edge of this nontrivial
growing record sequence.  A cut, seam operator, open boundary, or other
supplied faithful representation remains a live constructive route.

## 5. K-stage supply and the `C_n` generalization

Let K act on `C_n` momentum labels by `k -> -k mod n`.  The number of K-orbit
cells is

```text
q_n = (n+1)/2,  n odd,
q_n = n/2 + 1,  n even.
```

For the distinguished `k=0` singlet, uniform carrier-member formation gives
weight `1/n`, while uniform orbit-cell formation gives `1/q_n`.  These differ
for every `n>=3`.  At `n=3`,

```text
1/n   = 1/3,
1/q_n = 1/2.
```

This exact generalization shows that the `r=1/2` candidate is specific to the
`C_3` quotient-cell resolution together with the declared energy dictionary.
It also links the K question to the selector: supplying a K orbit at the
formation stage would make the quotient cell a candidate supplied object.
Treating that object as a formation event atom is a separate licensing and
formation-law bridge, and uniform hazards over such atoms would still need a
dynamical derivation.

## 6. Many-slice correlation family

For commuting scalar step weights represented abstractly by `x` and `y`, the
two existing prescriptions are

```text
T_N^q = (x^N+y^N)/2                       (quenched),
T_N^a = ((x+y)/2)^N                       (annealed).
```

Start a symmetric two-state Markov chain in its stationary distribution and
use persistence probability `p` between orbit representatives.  The exact
N-step product expectation is

```text
M_N(p) = (1/2,1/2) Z (P(p) Z)^(N-1) (1,1)^T,
Z      = diag(x,y),
P(p)   = [[p,1-p],[1-p,p]].
```

Then

```text
M_N(1)   = T_N^q,
M_N(1/2) = T_N^a.
```

For `x=2`, `y=3`, the runner recovers `T_2^q=13/2`, `T_2^a=25/4`, and a
third exact value at intermediate persistence.  Quenched versus annealed is
therefore the endpoint of a larger correlation-law choice.  The calculation
does not select `p`.

## 7. Canonical Krein positive-half classification

For arbitrary finite `W`, define

```text
D = W direct_sum W^dagger,
J = [[0,I],[I,0]],
P_+ = (I+J)/2.
```

The doubled transfer is J-self-adjoint:

```text
D^dagger J = J D.
```

Its leakage from the canonical J-positive half is exactly

```text
(I-P_+) D P_+
  = 1/4 [[Delta, Delta],[-Delta,-Delta]],
Delta = W-W^dagger.
```

Consequently `range(P_+)` is D-invariant if and only if `W=W^dagger`.
This is an exact classification of one canonical positive-half construction.
It is not a general Krein no-go: different fundamental symmetries, invariant
graph subspaces, positive metrics, quotients, or record readouts were not
classified by this probe.

## 8. Quadratic two-slice transfer factor `A_2(W)=W^2+I/4`

The exact witness

```text
W = (i/10) I,
A_2(W) = W^2 + I/4 = (6/25) I
```

has positive-definite `A_2(W)` and non-Hermitian `W`.  Moreover

```text
A_2(W) = A_2(-W).
```

Thus `A_2(W)` is a viable positive observable candidate on this witness, but it
does not reconstruct the sign/phase branch of `W`.  A readout or formation
law would have to supply that extra information if the downstream physical
identification requires it.

## Assumptions and imports

| Item | Class | Role and boundary |
|---|---|---|
| Lattice, Qubit, Admissibility, and Record | registered framework premise | Supplies the lattice, one-site possibility, local-rule, and permanent-record baseline; it does not supply the `C_3`/K carrier, formation selector, probability, readout observable, dynamics, or time law. |
| Two formation resolutions | current-main unaudited exact support | Supplies the already-exhibited carrier and quotient-cell alternatives, not a selector. |
| Energy dictionary `r=(1-w)/(2w)` | declared non-satisfying modeling condition | Used only for conditional conversion from formation weight to `r`; it does not satisfy a derivation dependency. |
| Supplied Hermitian spectral decomposition and numeric calibration | bounded construction premise | Supplies real `lambda_k`, projectors, and pointer values needed by the projective registration instrument; not derived here from the four axioms. |
| Full-support state `rho=I/3` | branch-local finite witness | Demonstrates compatibility of nonzero three-outcome support with the instrument; it is not a physical formation-state supplier. |
| Complete conditions `c_t,d_t` and law functions `F,G` | abstract supplied probe variables | Separates formation-weight law identity/equivalence from transfer-matrix law identity/equivalence; no `F -> G` bridge is supplied. |
| K action `k -> -k` | bounded algebraic probe premise | Used to compute orbit resolutions; no formation-stage supply conclusion is imported. |
| Markov persistence `p` | probe parameter | Exhibits a transfer-law family; it is neither fitted nor selected. |
| Standard doubled Krein pair `(D,J)` | current-main candidate construction | Only its canonical `P_+` projection is classified. |

No observational target, fitted selector, new axiom, or audit verdict is used.

## What this batch does not claim

This batch does not claim:

- unconditional selection of `w=1/2` or `r=1/2`;
- adoption of the closed, unmerged licensing-consolidation proposal;
- derivation of the energy dictionary;
- a framework-wide Born rule, spectral-mass identification, positive branch,
  or three-value registration theorem;
- law equivalence across changing record environments;
- a physical time law or a faithful periodic history representation;
- that K or its orbit is supplied at formation;
- selection of a quenched, annealed, or intermediate many-slice law;
- a general Krein obstruction;
- recovery of `W` from the quadratic transfer factor `A_2(W)=W^2+I/4`;
- any audit, review, publication, or ratification outcome.

## Load-bearing target and premise surfaces

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
  supplies the current registered framework boundary.
- [`KOIDE_FORMATION_GATE_RELOCATION_TIED_MEASURE_PER_CELL_WEIGHT_COMPATIBILITY_BOUNDED_THEOREM_NOTE_2026-07-12.md`](KOIDE_FORMATION_GATE_RELOCATION_TIED_MEASURE_PER_CELL_WEIGHT_COMPATIBILITY_BOUNDED_THEOREM_NOTE_2026-07-12.md)
  supplies the declared energy dictionary and the two formation weights.
- [`KOIDE_FORMATION_WEIGHT_CONDITIONAL_SELECTION_UNIQUE_REGISTRATION_COMPATIBLE_LAWFUL_WEIGHT_BOUNDED_THEOREM_NOTE_2026-07-12.md`](KOIDE_FORMATION_WEIGHT_CONDITIONAL_SELECTION_UNIQUE_REGISTRATION_COMPATIBLE_LAWFUL_WEIGHT_BOUNDED_THEOREM_NOTE_2026-07-12.md)
  supplies the named `B_map`, `B_plus`, `B_abs`, and `ND3` bridges.
- [`RECORD_FORMATION_TO_KRAUS_ISOMETRY_BRIDGE_2026-06-06.md`](RECORD_FORMATION_TO_KRAUS_ISOMETRY_BRIDGE_2026-06-06.md)
  supplies the bounded finite projective-instrument semantics used by the
  registration construction.
- [`G3_CROSS_EDGE_INDEPENDENCE_IS_A_FORMATION_GATE_ATOM_MARGINAL_IDENTITY_FROM_QUALIFICATION_BOUNDED_THEOREM_NOTE_2026-07-12.md`](G3_CROSS_EDGE_INDEPENDENCE_IS_A_FORMATION_GATE_ATOM_MARGINAL_IDENTITY_FROM_QUALIFICATION_BOUNDED_THEOREM_NOTE_2026-07-12.md)
  supplies the law-equivalence residual.
- [`RECORDS_ONLY_OS_RECONSTRUCTION_UNTIED_FIRST_ORDER_MEASURE_BOUNDED_THEOREM_NOTE_2026-07-11.md`](RECORDS_ONLY_OS_RECONSTRUCTION_UNTIED_FIRST_ORDER_MEASURE_BOUNDED_THEOREM_NOTE_2026-07-11.md)
  supplies condition `H` and its two-slice boundary.
- [`TIME_AXIS_IS_THE_HISTORY_INDEX_RECORD_MONOTONE_DIRECTION_BOUNDED_NOTE_2026-07-03.md`](TIME_AXIS_IS_THE_HISTORY_INDEX_RECORD_MONOTONE_DIRECTION_BOUNDED_NOTE_2026-07-03.md)
  supplies the history-index faithfulness residual.
- [`KOIDE_K_SYMMETRIZED_UNTIED_MEASURE_RECORDS_ONLY_RECONSTRUCTION_BOUNDED_THEOREM_NOTE_2026-07-12.md`](KOIDE_K_SYMMETRIZED_UNTIED_MEASURE_RECORDS_ONLY_RECONSTRUCTION_BOUNDED_THEOREM_NOTE_2026-07-12.md)
  supplies the K-stage, many-slice, and doubled-carrier questions.
- [`KOIDE_QUASI_HERMITIAN_METRIC_OPERATOR_ESCAPE_CLOSURE_BOUNDED_THEOREM_NOTE_2026-07-12.md`](KOIDE_QUASI_HERMITIAN_METRIC_OPERATOR_ESCAPE_CLOSURE_BOUNDED_THEOREM_NOTE_2026-07-12.md)
  supplies the Krein and quadratic-transfer-factor remainder targets.

These linked notes supply the named target definitions, bounded physical
semantics, or candidate constructions consumed by the batch.  They are all
current-main surfaces; no retained-grade dependency claim is made.  The
finite identities introduced here are proved directly and checked by the
runner.

Non-load-bearing context handles, deliberately left out of the citation graph,
are
`KOIDE_FORMATION_WEIGHT_LAW_EXPRESSIBILITY_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-12.md`
and
`RECORD_FORMATION_CONTROLLED_COPY_WRITE_ISOMETRY_THEOREM_NOTE_2026-06-18.md`.
They locate sibling discussions but supply no theorem step used here.

## Verification

```text
python3 -m py_compile scripts/frontier_rhalf_open_backlog_probes_2026_07_13.py
python3 scripts/frontier_rhalf_open_backlog_probes_2026_07_13.py
```

Expected terminal line:

```text
SUMMARY: RHALF OPEN BACKLOG PROBES PASS=57 FAIL=0
```

## Status certificate

```yaml
actual_current_surface_status: exact-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite identities are exact under explicit construction conditions; the physical formation and licensing bridges remain open."
trace_class: frontier_discovery
reachability_to_target: unknown_frontier
conditional_surface_status: bounded exact support under the named finite
  construction premises
dependency_classes:
  - registered framework premise
  - current-main unaudited exact support
  - declared non-satisfying modeling condition
  - bounded construction premise
open_imports:
  - formation-stage event-atom licensing and hazard law
  - spectral readout and positive branch
  - epoch-equivalence and transfer/time law
  - history faithfulness and K-stage supply
review_loop_disposition: pass_with_bounded_claims
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "The batch supplies exact reductions and discriminating constructions, not a formation-law selection or audit verdict."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
