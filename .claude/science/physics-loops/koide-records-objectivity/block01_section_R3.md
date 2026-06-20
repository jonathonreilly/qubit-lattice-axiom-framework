# Block01 Section R3 — Independence Probe: Countermodel Family Shows r=1/2 Is Free Under A_min

**Date:** 2026-06-20
**Route:** R3 (independence probe — explicit countermodel family, mirroring the
W = log det + eps*Tr countermodel used on T1-d)
**Target:** `docs/KOIDE_RECORDS_OBJECTIVITY_CONDITIONAL_NOTE_2026-05-31.md`
(bounded_theorem; r=1/2, Q=2/3 conditional on two named inputs).
**Runner:** `scripts/koide_records_objectivity_independence_probe_R3_2026_06_20.py`
**Cache:** `logs/runner-cache/koide_records_objectivity_independence_probe_R3_2026_06_20.txt`
(TOTAL: PASS=17 FAIL=0)
**Outcome:** NO-GO for closure — r=1/2 (the equal-block input) is INDEPENDENT of
A_min + the four approved primitives. An explicit one-parameter family of
Record-compatible selectors gives `r*(t) = t/2` for all `t > 0`, every member
admissible. The two named inputs cannot both be derived from the baseline; the
row stays conditional / named-premise.

## Goal

Decide whether r=1/2 is PINNED or FREE under the framework baseline. Rather than
attempt to derive the equal-block input (R1) or the objectivity selector, R3
attacks the conditional from the model-theory side: construct an EXPLICIT
continuous, block-additive, Record-compatible measure/selector that gives
`r != 1/2` while satisfying every A_min + approved-primitive constraint. If such
a countermodel exists, r=1/2 is independent of A_min — a clean no-go showing the
two inputs cannot both be derived. If every Record-compatible block-additive
measure is forced to equal weights, that would support closure.

Hard guard honored: r and Q are OUTPUTS of the construction (computed from the
chosen weight via the functional-calculus extremum and the circulant spectrum);
the empirical Koide value Q=2/3 enters only at the very end (F5) as a read-only
LABEL of which already-built member matches — never to select the weight.

## The countermodel family (the core of R3)

On the Hermitian circulant mass operator `H = a I + b C + conj(b) C^2` over `Z^3`
(Lattice + Quantum), the {I, C, C^2} operator basis is Hilbert–Schmidt-orthogonal,
so the energy splits cleanly into the two C3 isotypes (verified numerically in
F1, residuals at 1e-12):

- scalar/singlet block `E_+ = 3 a^2`,
- traceless/doublet block `E_perp = 6 |b|^2`,

with `r := |b|^2/a^2` and `E_perp/E_+ = 2r`. Define the family of selectors

```
W_t = w_s log E_+ + w_p log E_perp,    t := w_p / w_s in (0, inf).
```

This is EXACTLY the Ad-invariant isotype bilinear `B_{alpha,beta}(A,A) =
(alpha+3beta) Tr(A_s^2) + alpha Tr(A_t^2)` from
`KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS` (scalar weight `w_s = alpha+3beta`,
traceless weight `w_p = alpha`), whose PD region `alpha>0, alpha+3beta>0` is
precisely `w_s, w_p > 0`. The cited no-go already proves PD + Ad-invariance +
isotype orthogonality do NOT pin the ratio; R3 turns that freedom into an
explicit countermodel and runs the pin-test against A_min + all four primitives.

## What the runner does (all 17 checks pass)

- **P0** Loads all four approved primitive ids; confirms the Record axiom note
  supplies no weighting/normalization, and the realized_state_primitive supplies
  the slot not the measure (register item 4: per-sector weight r is realized-state
  DATA; `r in {0, 1/2, 1}` are sector data, never forced).
- **F1** Functional-calculus-correct block energies `E_+ = 3a^2`, `E_perp = 6|b|^2`
  by HS operator-basis projection (numeric, 1e-12). The doublet is two DISTINCT
  real masses — no conjugate-pair "fusion" to one slot.
- **F2** Family extremum `r*(w_s,w_p) = w_p/(2 w_s)` (sympy, exact), i.e.
  `r*(t) = t/2`, CONTINUOUS and NON-CONSTANT in t. Three admissible members give
  three distinct outputs: `t=1 → r=1/2, Q=2/3`; `t=2 (rank/dim) → r=1, Q=1`;
  `t=1/2 → r=1/4, Q=1/2`.
- **F3** Admissibility of EVERY member: (F3.1) C-infinity continuity on the open
  energy cone; (F3.2) exactly TWO log channels — block-additive, matching the
  2-block Record pointer; (F3.3) Record-compatible — scalar readout `I_t` finitely
  additive over the two disjoint singlet/doublet records with `I_t(empty)=0`,
  durable, verified for several UNEQUAL weights; (F3.4) the `alpha=beta=1`
  isotype bilinear is PD + Ad-invariant with unequal weights (scalar 4, traceless 1).
- **F4** PIN-TEST. Enumerates the constraints actually supplied by Lattice,
  Quantum, Record (additivity + durability), PD, Ad-invariance, and the
  scale_reference / kinetic_isotropy / realized_state primitives, and checks each
  at `t=2` (the rank member, r=1, Q=1). ALL are satisfied — no predicate in
  A_min + primitives forces `t=1`. The weight ratio is pinned only by an EXTRA
  equal-weight / objectivity-max selector that is not in the baseline.
- **F5** Read-only LABEL: empirical `Q=2/3 → r=1/2 → t=1`, naming which member
  matches post hoc. Guard documented: this did not enter F2–F4 or the pin-test.

## Result and load-bearing residual

r=1/2 is FREE, not pinned. The explicit family `W_t` is a valid countermodel:
it is continuous, block-additive (exactly two channels), Record-compatible
(finitely-additive durable scalar readout over the two disjoint records), PD, and
Ad-invariant for every `t>0`, yet its maximizer `r*(t)=t/2` ranges over all
positive reals. Therefore **r=1/2 is independent of A_min + the four approved
primitives**: the equal-block input and the objectivity-max selector cannot both
be derived from the baseline.

The load-bearing wall is the **isotype block-weight ratio** `t = w_p/w_s`. It is
not a consequence of Lattice + Quantum + Record or of any approved primitive; it
is the same freedom named by `KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS` and is
classified as realized-state DATA by the realized_state_primitive register
(item 4). The only way to reach `t=1` (r=1/2) is to ADD an equal-weight /
objectivity-maximization selector — exactly the second named input of the
conditional note — which is outside the scoped baseline.

## Relation to R1 and the note

R3 is the model-theoretic dual of R1's named-premise split. R1 identified the
equal-block input as the isotype-label-counting (dimension-blind) measure and
showed the dephasing fixed point points the other way (to rank weights (1,2),
Q=1). R3 confirms this is not a gap in one derivation attempt but a genuine
independence: the baseline admits a whole continuum of equally-Record-compatible
selectors, so no derivation route inside A_min + primitives can pin r. This
matches the note's own N2 wall-independence finding and the Correction's
dephasing→Q=1 observation, and upgrades them to an explicit countermodel family.

## Honest status

Clean NO-GO for closure of THIS conditional under the scoped baseline; not a
no-go against the framework. A future theorem could still derive the equal-weight
selector or the objectivity-max principle from a NEW retained authority (e.g. a
records/Darwinism objectivity axiom), or select the rank/trace (Q=1) route
instead. Within A_min + the four approved primitives, r and Q remain
realized-state data and the row remains conditional / named-premise. No new
axiom or primitive was introduced; the countermodel lives entirely inside the
already-approved isotype-weight freedom.
