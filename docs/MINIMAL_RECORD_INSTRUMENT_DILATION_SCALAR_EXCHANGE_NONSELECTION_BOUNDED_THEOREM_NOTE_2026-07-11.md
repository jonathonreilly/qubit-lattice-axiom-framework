---
claim_id: minimal_record_instrument_dilation_scalar_exchange_nonselection_bounded_theorem_note_2026-07-11
claim_type: bounded_theorem
claim_scope: "Exact classification of one-Kraus no-record completions of a supplied two-outcome rank-one instrument on a one-excitation edge sector, plus a counterexample in which a common-frame-invariant I-SWAP branch changes eventual absorbing outcome-label weights while the outcome-forgotten channel has minimal Kraus/Choi rank three. The result uses supplied CP-instrument composition and trace weights; it does not realize the labels as framework Records, construct a cubic QCA, derive time or the Born rule, or establish that the axioms require amendment."
upstream_dependencies:
  - minimal_axioms
  - record_observable_quotient_and_rank_one_formation_outcome_operation_normal_form_bounded_theorem_note_2026-07-11
  - kraus_choi_representation_normalization_reconciled_narrow_theorem_note_2026-06-05
runner: scripts/minimal_record_instrument_dilation_scalar_exchange_nonselection_2026_07_11.py
---

# Outcome-Forgotten Minimal Dilation: Exchange-Branch Nonselection

**Date:** 2026-07-11

**Type:** bounded theorem

**Status authority:** independent audit only. This source note changes no axiom,
primitive, or audit verdict.

Primary runner:
[`scripts/minimal_record_instrument_dilation_scalar_exchange_nonselection_2026_07_11.py`](../scripts/minimal_record_instrument_dilation_scalar_exchange_nonselection_2026_07_11.py)

Cached output:
[`logs/runner-cache/minimal_record_instrument_dilation_scalar_exchange_nonselection_2026_07_11.txt`](../logs/runner-cache/minimal_record_instrument_dilation_scalar_exchange_nonselection_2026_07_11.txt)

## Result

Minimal Stinespring dilation removes redundant representations of a **fixed**
CP map. It does not select the map. More sharply, after fixing two rank-one
outcome branches and full normalization on a supplied one-excitation sector,
the one-Kraus no-record completion has an arbitrary unitary polar factor. A
common-frame-invariant `I-SWAP` family survives that classification, gives
distinct outcome-forgotten channels of minimal Kraus/Choi rank three, is not
dilation gauge, and changes later and eventual absorbing outcome-label weights.

Therefore:

> minimal outcome-forgotten-channel rank does not select the exchange angle and
> does not by itself exclude an `I-SWAP` coherent branch from the supplied
> normalized outcome-resolved instrument class.

Minimal outcome-forgotten-channel rank does not select the exchange angle.

This is a bounded one-excitation-sector nonselection theorem. It is not a
framework-Record theorem or lattice-wide dynamics no-go.

## Repo-science reconciliation

The classification was attempted only after replaying the actual existing
instrument lane:

- `PERSISTENT_RECORD_INSTRUMENT_CONSTRUCTION_NARROW_THEOREM_NOTE_2026-05-22.md`
  constructs the block-column isometry for a supplied normalized Kraus family,
  but explicitly leaves physical Kraus-family selection open.
- `RECORD_FORMATION_TO_KRAUS_ISOMETRY_BRIDGE_2026-06-06.md`
  derives the projective `K_r=P_r` write map in a supplied finite pointer model.
- `RECORD_FORMATION_CONTROLLED_COPY_WRITE_ISOMETRY_THEOREM_NOTE_2026-06-18.md`
  realizes that write with a fresh controlled-copy fragment, but selects no
  general Hamiltonian, coupling, event rate, or probability rule.
- `RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md`
  proves pointer non-demolition conditions and explicitly does not make them a
  general record-writing selector.
- `BLOCKING_ISOMETRY_REDUCES_TO_POINTER_FRAME_ADMISSION_NARROW_THEOREM_NOTE_2026-06-09.md`
  shows that, once the pointer projectors are supplied, the projective write is
  fixed up to record-register gauge while the pointer frame remains physical
  input.
- `RECORD_OPEN_SYSTEM_RESET_CHANNEL_INTERFACE_2026-06-05.md`
  supplies an exact finite reset/export interface and keeps its Hamiltonian,
  environment stream, and rate open.
- [`RECORD_OBSERVABLE_QUOTIENT_AND_RANK_ONE_FORMATION_OUTCOME_OPERATION_NORMAL_FORM_BOUNDED_THEOREM_NOTE_2026-07-11.md`](RECORD_OBSERVABLE_QUOTIENT_AND_RANK_ONE_FORMATION_OUTCOME_OPERATION_NORMAL_FORM_BOUNDED_THEOREM_NOTE_2026-07-11.md)
  proves `J_P(rho)=Tr(E_P rho)P` for a supplied rank-one locked-output outcome
  operation, while leaving the full instrument and coherent no-record block
  open.

The corresponding retained/source runners reproduce at `29/0`, `75/0`,
`37/0`, and `30/0` for the persistent-instrument, Kraus bridge,
controlled-copy, and blocking-isometry checks respectively. Audit status is
not inferred from runner success.

The finite CP/Kraus/Choi representation used below is the scoped mathematical
authority in
[`KRAUS_CHOI_REPRESENTATION_NORMALIZATION_RECONCILED_NARROW_THEOREM_NOTE_2026-06-05.md`](KRAUS_CHOI_REPRESENTATION_NORMALIZATION_RECONCILED_NARROW_THEOREM_NOTE_2026-06-05.md).
The contextual notes above are reading-gate provenance, not additional
load-bearing dependency edges.

## 1. Exact completion classification

Let `H` be finite-dimensional, let `{P_r}_{r=1}^m` be a complete orthogonal
rank-one resolution of identity, and fix `0<q<1`. Supply the nonempty outcome
operations

```text
J_r(rho) = (1-q) P_r rho P_r,
K_r = sqrt(1-q) P_r.                                      (1)
```

Complete them by one no-record Kraus operator `K_empty`. Full-instrument
normalization is

```text
K_empty^dag K_empty + sum_r K_r^dag K_r = I.              (2)
```

Using `sum_r P_r=I`, equation (2) is equivalent to

```text
K_empty^dag K_empty = q I.                                (3)
```

Because input and output carriers have equal finite dimension and `q>0`, the
polar decomposition gives the complete classification

```text
K_empty = sqrt(q) U,       U in U(H).                     (4)
```

Conversely every `U` in (4) satisfies (2). An overall phase of `U` leaves its
CP outcome operation unchanged, so the physically distinct one-Kraus
no-record operations contain a projective-unitary family. Normalization fixes
the no-record **effect** `qI`; it does not fix the conditional coherent map.

The outcome-resolved block-column isometry is

```text
V_U |psi> = |empty> sqrt(q) U|psi>
          + sum_r |r> sqrt(1-q) P_r|psi>.                 (5)
```

Equation (2) gives `V_U^dag V_U=I`. For the outcome-resolved instrument, every
nonzero outcome requires its distinct classical label. For the
outcome-forgotten system channel, the minimal Stinespring environment dimension
equals the linear span/Choi rank of `{U,P_1,...,P_m}`. Thus minimalization can
remove special linearly dependent choices of `U`; it cannot remove a generic
unitary outside the projector span.

## 2. Common-frame-invariant nearest-neighbor witness

Take the one-excitation sector of one unoriented edge,

```text
H_edge = span{|L>, |R>}.
```

On this sector the site exchange is

```text
SWAP |L> = |R>,      SWAP |R> = |L>,
```

and the exchange/Laplacian family is

```text
U_theta = exp[-i theta (I-SWAP)]
        = exp(-i theta)[cos(theta) I + i sin(theta) SWAP]. (6)
```

Here `scalar-exchange` means invariant under a common one-site frame rotation
`G tensor G` and even under reversal of the unoriented edge; it does **not**
mean proportional to identity on the two-dimensional sector. The full
two-qubit `SWAP` commutes with every common-frame generator
`sigma_i tensor I + I tensor sigma_i`, and `I-SWAP` is also edge-reversal
even. At `theta=pi/2`, `U_theta=SWAP` exactly. Choose `q=1/3` and outcome projectors
`P_L=|L><L|`, `P_R=|R><R|`.

At both `theta=pi/4` and `theta=pi/2`:

- the three-outcome instrument is exactly normalized;
- the one-step effects are the same:
  `E_empty=qI`, `E_L=(1-q)P_L`, `E_R=(1-q)P_R`;
- the nonempty outcome operations `J_L,J_R` are the same;
- `{U_theta,P_L,P_R}` is linearly independent because `sin(theta) != 0` and
  `U_theta` has an off-diagonal SWAP component;
- the outcome-forgotten channel has Choi rank three, so both Stinespring
  dilations are minimal with environment dimension three.

The full instruments are not equal: their no-record CP operations differ.
That difference is physical rather than Stinespring gauge because it changes
the outcome-forgotten system channel on `|L><L|`.

## 3. Outcome-label sensitivity and append-only permanence

Compose the instrument on the carrier until the first nonempty outcome. An
`L/R` outcome appends its label to a fresh idle register and terminates that
carrier's pre-outcome process. This is an explicit append-only classical-label
model. Identifying that register with a framework Record would additionally
require a `Z^3` site realization, local Admissibility, and a proof that the
label locks one admissible site possibility. None is supplied here. The live
two-site carrier itself is not claimed to be absorbing.

For initial `rho=|L><L|`, the supplied two-step history weights are

```text
w_theta(empty,L) = q(1-q) cos^2(theta),
w_theta(empty,R) = q(1-q) sin^2(theta).                   (7)
```

With `q=1/3`,

```text
w_pi/4(empty,R) = 1/9,
w_pi/2(empty,R) = 2/9.                                   (8)
```

So the exchange angle changes an outcome-resolved label history. It is not null
for the supplied `L/R` label readout. Applying the framework record-observable
quotient would first require the separate label-to-Record realization bridge.
Coarse-graining away the outcome side would hide this distinction.

The stronger absorbing first-outcome distribution also differs. Summing over
any number `n` of no-record branches before the first nonempty outcome gives

```text
Pr_theta(first nonempty outcome = R)
  = (1-q) sum_{n>=0} q^n Tr(P_R U_theta^n rho U_theta^{-n}). (9)
```

The exact periodic geometric sums are

```text
Pr_pi/4(first nonempty outcome = R) = 1/5,
Pr_pi/2(first nonempty outcome = R) = 1/4.                (10)
```

Both eventual `L/R` distributions normalize to one. Hence the exchange
coherent branch changes the final absorbing label distribution even though the
one-step effects and nonempty outcome branches are identical.

## 4. What the counterexample decides

It closes the following narrow route:

```text
fixed nonempty outcome branches
    + full normalization
    + one-Kraus no-record completion
    + minimal rank of the outcome-forgotten channel
    + operational outcome-label sensitivity
    -> unique/non-scalar coherent carrier.                (11)
```

Implication (11) is false on the supplied finite edge. Minimality removes
redundant dilations of each fixed channel but cannot choose among the distinct
minimal channels labeled here by `theta`.

This result is stronger than tensoring an outcome-null SWAP spectator onto an
instrument: the exchange acts on the same pre-outcome carrier and changes the
eventual label. It therefore survives the supplied label-readout quotient and
the minimal-environment test. Survival under the framework record-observable
quotient remains conditional on a label-to-Record realization.

## 5. What remains open

The result does not construct a simultaneous translation-covariant cubic QCA.
In particular, exponentiating a sum of overlapping edge exchanges is not
silently identified with a strict finite-radius tick. The following stronger
selectors remain live:

- derive the record effects from Admissibility rather than supply `P_L,P_R`;
- impose a simultaneous cubic-lattice composition law and classify every
  strict local unitary cell;
- require a direction-resolving spectral formation bridge of the type isolated
  by the cubic neighbor-response classifier;
- derive the firing order/rate instead of supplying discrete instrument
  composition;
- select the continuum scaling and test whether scalar branches fail the
  relativistic/unitary limit.

Those are the ordered effect, instrument, time, cubic-tick, and continuum
campaigns. This finite witness cannot prejudge them.

## 6. Axiom-set implication

This does not establish that the axioms require amendment. More specifically,
the theorem does not establish that the
[`minimal axioms`](MINIMAL_AXIOMS_2026-06-29.md) require amendment. It proves
that one candidate derivation strategy—minimal dilation applied after supplied
outcome branches and normalization—does not select the coherent carrier. A
stronger theorem may still follow from effect selection, a governed process
primitive, a strict cubic-tick classification, or the continuum consistency
conditions. None is equivalent to changing an axiom merely because it is not
yet derived.

Accordingly the campaign continues to effect selection/Born. The owner stop
condition is not triggered.

## Boundaries

- CP structure, the trace weight rule, the finite-dimensional Kraus/Choi
  theorem, `q`, and sequential composition are supplied mathematical/physical
  hypotheses; this note does not derive the Born rule.
- The pointer projectors and the `L/R` readout are supplied. Their selection is
  the next campaign.
- The witness initial state `rho=|L><L|` and the rule to repeat only while the
  outcome is empty and stop at the first `L/R` outcome are supplied. They are
  not state-selection or event-order derivations.
- The fresh append-only outcome register is not derived as a framework Record;
  no `Z^3` site, Admissibility, locked-possibility, or same-carrier absorption
  claim is made.
- The scalar-exchange witness is exact only on the supplied nearest-neighbor
  one-excitation sector. No instrument on the full two-qubit edge algebra, full
  cubic-lattice, per-mode, infinite-volume, or continuum result is asserted.
- `theta=0 mod pi` is a rank-degenerate special case for the
  outcome-forgotten channel; the two tested nonzero angles have rank three.
- `q=0` removes the coherent no-record branch and `q=1` removes nonempty
  formation; the theorem assumes `0<q<1`.
- Outcome-side coarse graining can erase the distinction. The witness uses the
  supplied resolved outcome labels.

## Reproduction

```bash
python3 scripts/minimal_record_instrument_dilation_scalar_exchange_nonselection_2026_07_11.py
```

The runner checks exact unitarity, normalization, isometry, Kraus/Choi rank,
effect equality, nonempty-outcome-branch equality, two-step weights, eventual
absorbing label weights, channel inequivalence, and source-boundary markers.
