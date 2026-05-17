# Time-Dimension d_t = 1 Proof-Walk Lattice-Independence Bounded Note

**Date:** 2026-05-08
**Claim type:** bounded_theorem
**Proposal allowed:** false
**Status authority:** source-note proposal only; audit verdict and
effective status are set by the independent audit lane.
**Primary runner:** [`scripts/frontier_dt1_time_dimension_proof_walk_lattice_independence.py`](../scripts/frontier_dt1_time_dimension_proof_walk_lattice_independence.py)

## Claim

Given the existing one-generation chiral-content, anomaly-system, and
single-clock codimension-1 evolution structure used by
[`ANOMALY_FORCES_TIME_THEOREM.md`](ANOMALY_FORCES_TIME_THEOREM.md),
the proof that anomaly cancellation forces the temporal dimension

```text
d_t = 1
```

(the time / chirality piece of the 3+1 spacetime claim) does not use
lattice-action machinery as a load-bearing input. The proof-walk uses
only:

- chiral-content multiplicities;
- SU(2) and SU(3) Dynkin-index bookkeeping in the anomaly traces;
- exact rational arithmetic in the anomaly equations;
- the Clifford-algebra classification of the volume-element parity;
- the cited Clifford-volume / sublattice-parity chirality grading;
- the cited single-clock codimension-1 evolution structure.

This is a bounded proof-walk of an existing theorem note. It does not
add a new axiom, a new repo-wide theory class, or a retained status
claim. It does not propose a status promotion.

## Boundaries

This note does not close:

- the spatial dimension `d_s = 3`. **`d_s = 3` is given directly by the
  framework axiom A2 (`Z^3` substrate) per
  `MINIMAL_AXIOMS_2026-05-03.md`. It is
  NOT derived from a proof-walk in this note and NOT derived from
  anomaly cancellation in
  [`ANOMALY_FORCES_TIME_THEOREM.md`](ANOMALY_FORCES_TIME_THEOREM.md).**
  The narrow proof-walked claim here is the temporal piece `d_t = 1`
  only;
- the bare external ABJ anomaly-to-inconsistency admission (i) of
  [`ANOMALY_FORCES_TIME_THEOREM.md`](ANOMALY_FORCES_TIME_THEOREM.md).
  This admission is inherited as-is from the source note: the proposed
  internal companion (PR 402, lattice Wess--Zumino / Fujikawa `Z^4`
  theorem) was closed without merge and the cited file does not exist
  on `main`;
- the staggered-Dirac realization gate;
- any claim that multiple lattice realizations exist in the framework;
- any continuum-limit numerical claim such as plaquette, mass, or
  coupling values;
- any follow-on proof-walk for other algebraic bookkeeping notes;
- any parent theorem/status promotion. The cited single-clock
  codimension-1 evolution theorem and the Clifford-volume / sublattice-
  parity chirality grading (the latter routed to
  `STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md`,
  per the F-C routing fix below) are both `unaudited` on `main` as of
  2026-05-17 (ledger snapshot; the earlier `proposed_retained,
  audit-pending` wording is stale and has been corrected). This note
  treats them as black boxes at their current tier and does not
  re-derive them or propose their promotion. Any future audit-status
  change on those companions propagates directly into this proof-walk's
  effective tier.

## Proof-Walk

The chain that forces `d_t = 1` lives in Steps 2--4 of the source
theorem note. Step 1 (anomaly trace evaluation) and Step 5 (final
combine) are listed for completeness; they do not introduce additional
load-bearing inputs beyond those already named.

| Step in the cited time theorem | Load-bearing input | Lattice-action input? |
|---|---|---|
| Step 1: left-handed anomaly traces `Tr[Y]`, `Tr[Y^3]`, `Tr[SU(3)^2 Y]`, `Tr[SU(2)^2 Y]` | matter multiplicities `(6, 2, 3, 3, 1, 1)` and Dynkin indices `T(fund) = 1/2` | no |
| Step 1: ABJ anomaly-to-inconsistency implication | bare external admission (i) inherited as-is from the source note | no |
| Step 2: opposite-chirality SU(2)-singlet completion exists | bare cancellation requirement plus the cited Clifford-volume / sublattice-parity chirality grading from [`STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md`](STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md) (Step 4 there derives `{ε, D_staggered} = 0` from site-chirality + no-rooting irreducibility). Earlier wording cited [`CPT_EXACT_NOTE.md`](CPT_EXACT_NOTE.md), but that note defines `ε(x) = (-1)^(x_1+x_2+x_3)` only as the **charge conjugation operator C** (algebraically orthogonal role); see fix-record below. | no |
| Step 3: chirality operator `gamma_5` requires even total spacetime dimension | Clifford-algebra classification of `omega = gamma_1 ... gamma_n` | no |
| Step 3: combine with `d_s = 3` from A2 substrate axiom | axiom A2 input (substrate-axiom input, not derived here) | no |
| Step 3 conclusion: `d_t` must be odd, `d_t in {1, 3, 5, ...}` | exact integer parity of `d_s + d_t` | no |
| Step 4: single-clock codimension-1 evolution excludes `d_t > 1` | cited [`AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`](AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md) (`unaudited` per 2026-05-17 ledger; earlier wording "proposed_retained, audit-pending" is stale). Per the upstream parent's [F-B framing-fix](ANOMALY_FORCES_TIME_FB_FRAMING_FIX_NOTE_2026-05-17.md), this row is the **inherited (admission (iv))** branch of the parent's `d_t = 1` decomposition; the Step 3 row above is the **derived** branch (`d_t ∈ {1, 3, 5, ...}`). | no |
| Step 5: combine Steps 2--4 to conclude `d_t = 1` | output collection | no |

The checked proof path does not cite the Wilson plaquette action,
staggered phases, Brillouin-zone labels, link unitaries, lattice scale,
`u_0`, a Monte Carlo measurement, or a fitted observational value.

## Exact Arithmetic Check

The runner reproduces the source-note algebraic facts that feed
Steps 1--4 with `fractions.Fraction`:

- the LH-anomaly traces using the structural multiplicities
  `(6, 2)` and Dynkin index `1/2`:

  ```text
  Tr[Y]_LH         = 0
  Tr[SU(2)^2 Y]_LH = 0
  Tr[SU(3)^2 Y]_LH = 1/3
  Tr[Y^3]_LH       = -16/9
  ```

  The two nonzero traces are exactly the inconsistency that drives
  Steps 2--4;

- the standard-model hypercharge assignment that satisfies anomaly
  cancellation after the Step 2 SU(2)-singlet completion:

  ```text
  Y(Q_L) = +1/3,  Y(L_L) = -1,
  Y(u_R) = +4/3,  Y(d_R) = -2/3,  Y(e_R) = -2,  Y(nu_R) = 0
  ```

  with `Tr[Y] = 0`, `Tr[SU(3)^2 Y] = 0`, `Tr[Y^3] = 0` for the full
  spectrum;

- the integer parity check that drives Step 3: for `d_s = 3` (A2
  input), `d_s + d_t` is even iff `d_t` is odd;

- the Clifford volume-element commutation rule
  `omega gamma_mu = (-1)^(n-1) gamma_mu omega`, which is central
  (commutes) for `n` odd and anticommutes for `n` even, so a chirality
  operator that anticommutes with all `gamma_mu` exists only for
  even `n`;

- the explicit enumeration of `d_t in {0, 1, 2, 3, 4, 5}` against the
  three constraints (chirality grading, parity, single-clock
  codimension-1 exclusion of `d_t > 1`), confirming `d_t = 1` is the
  unique satisfying value.

## Dependencies

- [`ANOMALY_FORCES_TIME_THEOREM.md`](ANOMALY_FORCES_TIME_THEOREM.md)
  for the time theorem being proof-walked.
- [`STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md`](STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md)
  for the Clifford-volume / sublattice-parity chirality grading
  `ε(x) = staggered γ_5` cited at Steps 2 and 3 of the source note. Step
  4 of that companion derives `{ε, D_staggered} = 0` from site-chirality
  + no-rooting irreducibility. (Routing corrected 2026-05-17: earlier
  wording pointed at [`CPT_EXACT_NOTE.md`](CPT_EXACT_NOTE.md), which
  defines `ε(x) = (-1)^(x_1+x_2+x_3)` only as the charge conjugation
  operator `C`. The two roles share notation but are algebraically
  orthogonal. See fix-record note linked below.)
- [`AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`](AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md)
  for the single-clock codimension-1 evolution structure cited at
  Step 4 of the source note.
- [`NATIVE_GAUGE_CLOSURE_NOTE.md`](NATIVE_GAUGE_CLOSURE_NOTE.md)
  for the chiral-content origin used at Steps 1 and 2 of the source
  note.
- [`LH_ANOMALY_TRACE_CATALOG_THEOREM_NOTE_2026-04-25.md`](LH_ANOMALY_TRACE_CATALOG_THEOREM_NOTE_2026-04-25.md)
  for the LH-anomaly-trace bookkeeping.
- `MINIMAL_AXIOMS_2026-05-03.md`
  for the framework axiom A2 (`Z^3` spatial substrate) that supplies
  `d_s = 3` directly.
- `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`
  for the open realization-gate context that this note does not close.

These are imported authorities for a bounded theorem. The row remains
unaudited until the independent audit lane reviews this note, its
dependencies, and the runner.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_dt1_time_dimension_proof_walk_lattice_independence.py
```

Expected:

```text
TOTAL: PASS=N FAIL=0
VERDICT: bounded proof-walk passes; the time-dimension forcing chain
that gives d_t = 1 uses no lattice-action quantity as a load-bearing
input.
```

## Fix record (2026-05-17, downstream surgical-fix wave)

Three hostile-audit-grade issues were patched on this note:

- **F-C (stale citation routing, propagated from upstream):** Step 2 of
  the proof-walk and the Dependencies list previously cited
  [`CPT_EXACT_NOTE.md`](CPT_EXACT_NOTE.md) for the
  Clifford-volume / sublattice-parity chirality grading that
  anticommutes with the staggered Dirac operator. CPT_EXACT_NOTE only
  defines `ε(x) = (-1)^(x_1+x_2+x_3)` as the **charge conjugation
  operator C** (no `γ_5` content; algebraically orthogonal role).
  Corrected routing target:
  [`STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md`](STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md),
  whose Step 4 derives `{ε, D_staggered} = 0`. Inherits the same fix
  applied upstream in
  [`ANOMALY_FORCES_TIME_ADMISSION_III_ROUTING_CORRECTION_NOTE_2026-05-17.md`](ANOMALY_FORCES_TIME_ADMISSION_III_ROUTING_CORRECTION_NOTE_2026-05-17.md).
- **F-A (stale dependency tier):** the Boundaries and Step 4 rows
  previously said the single-clock codimension-1 evolution theorem and
  the Clifford-volume grading were "proposed_retained, audit-pending";
  the 2026-05-17 ledger snapshot has both at `unaudited`. Corrected
  inline.
- **F-B (admission-inheritance acknowledgment):** the proof-walk's
  Step 3/Step 4 split already mirrors the upstream parent's `d_t = 1`
  decomposition (Step 3 derives `d_t ∈ {1, 3, 5, ...}`; Step 4 excludes
  `d_t > 1`). The Step 4 row now explicitly links to the upstream
  [F-B framing-fix](ANOMALY_FORCES_TIME_FB_FRAMING_FIX_NOTE_2026-05-17.md)
  and identifies itself as the **inherited (admission (iv))** branch.

See companion fix-record:
[`DT1_TIME_DIMENSION_PROOF_WALK_DOWNSTREAM_FIX_NOTE_2026-05-17.md`](DT1_TIME_DIMENSION_PROOF_WALK_DOWNSTREAM_FIX_NOTE_2026-05-17.md).

Paired verifier:
`scripts/frontier_dt1_time_dimension_proof_walk_downstream_fix.py`.

None of these edits change the proof-walk's claim, its bounded-theorem
character, the lattice-independence verdict, or the list of load-bearing
inputs. They make the citation routing correct, the dependency tiers
honest, and the upstream-admission inheritance explicit.
