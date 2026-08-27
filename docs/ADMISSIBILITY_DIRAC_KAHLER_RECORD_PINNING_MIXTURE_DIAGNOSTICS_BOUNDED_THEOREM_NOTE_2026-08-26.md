---
claim_id: admissibility_dirac_kahler_record_pinning_mixture_diagnostics_bounded_theorem_note_2026-08-26
final_path: docs/ADMISSIBILITY_DIRAC_KAHLER_RECORD_PINNING_MIXTURE_DIAGNOSTICS_BOUNDED_THEOREM_NOTE_2026-08-26.md
claim_type: bounded_theorem
claim_scope: "Exact finite linear-algebra diagnostics for four declared class-0 substitutions on Block 171's 12x4 matrix bench: a nonzero conditional mixture residual, restoring-vector ranks, six-profile common-vector obstruction, row-block support, a specified hermitization comparison, and a seven-point fixed-background q sweep. No record instrument, physical conditional law, conjugation bridge, response mechanism, classical no-go, or continuum statement is supplied."
runner: scripts/admissibility_dirac_kahler_record_pinning_mixture_diagnostics_2026_08_26.py
status: proposed_retained
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "the finite profiles have no framework-derived record/instrument interpretation, and the q reversal is not global conjugation at the fixed complex background"
source_of_blocker_text: review_loop
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Derive an admissible record instrument or conditional law independently from the Minimal Axioms, and separately derive a transformation with a valid physical interpretation before reusing these finite diagnostics."
conditional_surface_status: "stacked on unmerged ancestor artifacts; scientific content is proposed for retention and remains audit-required"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact finite-dimensional ranks, residuals, support counts, and matrix identities, with a measured counterexample to the draft conjugation interpretation"
audit_required_before_effective_retained: true
bare_retained_allowed: false
parent_ref: origin/physics-loop/toe-axiom-closure-block201-covariant-rule-identification-20260826
parent_commit: d460d14f89c38c4c2a8774fc62cc103d0ae706a1
current_main: 76df4becc8233080bc5a10a4baf55f83e80f8f2d
registered: 0
adopted: 0
axiom_movement: none
---

# Finite substitution-profile diagnostics and their missing physical map

**Date:** 2026-08-26

**Type:** `bounded_theorem`

**Status:** `proposed_retained` — author proposal only; independent audit is
required before any effective retained status.

**Standing:** conditional support on an unmerged PR stack. Nothing is
registered, adopted, or added to the axioms.

## Result

The runner preserves the following exact finite calculations on Block 171's
committed `Site('12x4', 12, 4)` matrix bench.

1. Four separately substituted profiles fail one *declared conditional mixture
   test* when the native `W9` mid-slice profile is used as its coefficient
   vector. All four exact residual components are nonzero, their signs are
   `(+,-,+,+)`, and their exact sum is zero. The associated `4 x 4` system has
   ranks `(4,4)` and a unique componentwise nonnegative unit-sum restoring
   vector. That vector differs exactly from all four tested candidate vectors.
2. Each of six selected `W9`/`W2` level systems separately has ranks `(4,4)`
   and a componentwise nonnegative unit-sum solution. Their combined `25 x 4`
   system has ranks `(4,5)`, so no single four-component coefficient vector
   solves all six selected systems.
3. The four substitutions change zero entries in the selected slot-5 row
   block, while the combined `W9-L5`/`W2-L5` `9 x 4` system has ranks `(4,5)`.
   This is an entrywise support certificate, not causal or statistical
   isolation, because every profile uses the inverse of the full matrix.
4. The base action has `56` nonzero entries in its anti-Hermitian part. After
   the specified substitution-by-substitution hermitization, `W9-L5` equals
   `W2-L5` for the base matrix and all four substituted matrices. The separate
   three-level `W9` system has ranks `(4,5)` before and after that replacement.
5. At the fixed spatial dial `(g_re,g_im)=(1/3,1/4)`, the declared residual is
   non-even under the seven sampled `q` values. However, direct exact
   comparison gives

   ```text
   nnz(Q(-1) - conjugate(Q(1))) = (96,92,92,92,92)
   ```

   on the base matrix and four substitutions. Thus `q -> -q` is not global
   conjugation in this experiment. The non-even response is retained; the
   draft phase-conjugation and intensity-only interpretations are withdrawn.

These are finite matrix/profile facts. The Minimal Axioms do not identify the
four substitutions as mutually exclusive outcomes, supply their conditional
law, select the native mid-slice vector as formation weights, or give the
`q` reversal a physical transformation law.

## Authority and dependencies

The construction is inherited from, and does not alter:

- [Block 201 finite covariant encodings](ADMISSIBILITY_DIRAC_KAHLER_COVARIANT_RULE_IDENTIFICATION_BOUNDED_THEOREM_NOTE_2026-08-26.md)
- [Block 171 committed matrix bench](ADMISSIBILITY_DIRAC_KAHLER_GENERATOR_TRILEMMA_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-21.md)
- [Minimal Axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Axiom/premise registry](audit/data/axiom_premise_nodes.json)
- [Gravity-mainline campaign charter](../.claude/science/physics-loops/CAMPAIGN_20260824_GRAVITY_MAINLINE.md)

The exact implementation is
[the Block-202 runner](../scripts/admissibility_dirac_kahler_record_pinning_mixture_diagnostics_2026_08_26.py).

## Finite definitions

On the committed bench,

```text
N = 24, T = 6, c = 1, tstar = 5, lx = 4,
selected read rows = (20,21,22,23),
substituted rows   = (12,13,14,15),
substitutions      = {(3,x): 0}, x in {0,1,2,3}.
```

For the declared test only, define

```text
P0  = profile(W9,5) on the unsubstituted matrix,
w   = profile(W9,3) on the unsubstituted matrix,
Px  = profile(W9,5) after the single substitution {(3,x):0},
R   = P0 - sum_x w_x Px.
```

The definitions of `P0`, `w`, and `Px` are exact. Calling the `Px` conditional
outcome profiles or `w` formation weights is an additional interpretation and
is not used as a conclusion.

The exact runner reports

```text
R componentwise nonzero = (True,True,True,True),
sign(R)                  = (+,-,+,+),
sum(R)                   = 0,
restoring ranks          = (4,4),
restoring vector         = unique, nonnegative, unit-sum.
```

The runner stores the full exact rational restoring vector. Its decimal display
is `(0.251125,0.247420,0.072998,0.428457)` and is never used by a verdict.

For the six selected systems `family in {W9,W2}` and
`level in {5,4,2}`, the runner constructs four profile equations per system and
one shared normalization equation. All six individual systems have ranks
`(4,4)`, while the combined matrix and augmented matrix have ranks `(4,5)`.
This is a theorem about one declared four-column ansatz, not an exhaustive
latent-variable or response-model theorem.

## Interpretation boundary

- “Substitution” means replacing one committed carrier entry according to the
  inherited dictionary. It does not mean measurement, intervention, collapse,
  or state update.
- “Mixture” names the displayed affine identity under declared conditional and
  weight readings. Failure of the identity shows that those two readings cannot
  both hold for these profiles; it does not say which reading fails.
- “Six-profile incompatibility” means that one four-component coefficient
  vector cannot solve the six selected linear systems. It does not exclude a
  refined latent space, another response family, or a physical classical model.
- “Unchanged row block” is entrywise support information only. The global
  inverse prevents any isolation inference.
- Hermitization statements concern only the specified matrix replacement and
  selected profiles. They do not identify a physical source or mechanism.
- The `q` sweep holds a complex spatial background fixed. Its non-even response
  is not a conjugation, phase, intensity, interference, or quantum certificate.
- No gravity structure, generic-parameter theorem, continuum limit, or axiom
  amendment is supplied.

## No-Go Discipline Gate

The negative statement gated here is deliberately narrow: **for the six
selected finite profile systems and the declared four-column substitution
ansatz, no single four-component coefficient vector solves all profile
equations together with unit normalization.** It is not a claim that no record
model, latent-variable model, classical response model, or physical instrument
exists.

### N1 — alternative-route enumeration

| normalized route | attack and exact outcome | honesty marker |
| --- | --- | --- |
| direct algebraic elimination | Row-reduce the complete `25 x 4` system over `QQ_I`; coefficient rank `4` and augmented rank `5` make a solution impossible. | `ATTEMPTED` |
| solve-then-cross-check | Solve each of the six full-rank `4 x 4` systems independently and substitute each resulting vector into the other five systems; none is common because the exact combined system is inconsistent. | `ATTEMPTED` |
| normalization relaxation | Remove the final unit-sum row and test the 24 profile equations alone; normalized profile rows already carry the affine constraint, so the rank mismatch remains. | `ATTEMPTED` |
| coefficient-field extension | Extend the exact `QQ_I` entries to an arbitrary characteristic-zero field; the nonzero augmented minor that gives rank `5` remains nonzero, so a complex or real coefficient choice cannot repair this same four-column system. | `ATTEMPTED` |
| alternate carrier/latent refinement | Add columns, split the held-fixed class-value label, or allow a different coefficient vector for each selected profile. These routes can evade the obstruction because they change the ansatz; they therefore defeat any broader physical no-go but do not refute the stated fixed-ansatz theorem. | `ATTEMPTED` |

The route families differ in terminal obligation: direct solvability,
cross-system compatibility, affine normalization, scalar-field dependence, and
ansatz refinement. The last route is the explicit escape that forces the
claim's narrow scope. Exact profile authority comes from
[Block 171](ADMISSIBILITY_DIRAC_KAHLER_GENERATOR_TRILEMMA_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-21.md);
no retained authority is cited as having ruled out an untested route.

### N2 — wall-independence audit

The theorem has four explicit walls rather than an inflated list:

- `W1`: exactly the four declared substitution columns;
- `W2`: one coefficient vector must be shared by all selected systems;
- `W3`: exactly the inherited `W9/W2` profile definitions;
- `W4`: exactly levels `5,4,2` on the one committed bench.

| pair | closing first closes second? | closing second closes first? | independent? |
| --- | :---: | :---: | :---: |
| `W1,W2` | no | no | yes |
| `W1,W3` | no | no | yes |
| `W1,W4` | no | no | yes |
| `W2,W3` | no | no | yes |
| `W2,W4` | no | no | yes |
| `W3,W4` | no | no | yes |

Changing the coefficient dimension does not determine whether weights must be
shared; changing a profile definition does not choose the tested levels; and
changing the bench does not select an instrument. No wall follows from another.

### N3 — hidden-wall scan

| phrase class | occurrence and classification |
| --- | --- |
| “declared” / “by construction” | The four columns and shared-vector rule are load-bearing conditions; they are promoted explicitly to `W1` and `W2`. |
| “framework provides” / “naturally” / “obviously” | No positive use occurs. The note says the framework does **not** provide the outcome or formation-weight interpretation. |
| “background” | The fixed complex spatial dial belongs only to the separate `q` sweep and is non-load-bearing for the six-system rank theorem. |
| “standard” | Hermitization and exact rank are definitions used in the runner, not imported physical principles. |
| “registered” / “canonical” | The only use is the explicit statement that nothing is registered or adopted; no premise weight is inferred. |

The scan adds no hidden wall beyond `W1-W4`.

### N4 — residual matching

| cited source | source residual | residual here | exact match? | disposition |
| --- | --- | --- | :---: | --- |
| [Block 171](ADMISSIBILITY_DIRAC_KAHLER_GENERATOR_TRILEMMA_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-21.md) | defines the committed finite matrix and profiles | incompatibility of one shared vector across six derived systems | no | construction authority only, not counted as a no-go witness |
| [Block 201](ADMISSIBILITY_DIRAC_KAHLER_COVARIANT_RULE_IDENTIFICATION_BOUNDED_THEOREM_NOTE_2026-08-26.md) | missing selector/bridge for finite covariant encodings | fixed four-column common-vector inconsistency | no | stack parent only, not counted as a witness |
| [Minimal Axioms](MINIMAL_AXIOMS_2026-06-29.md) | supplies no record instrument or conditional law | fixed linear-system rank mismatch | no | premise boundary only, not counted as a witness |

No prior no-go is used to prove the rank mismatch. The runner's exact augmented
rank is the sole negative certificate, so dropping all three nonmatching
citations leaves the proof intact.

### N5 — rhetoric audit and five resolution levels

N5: per_element: Four class-0 cell substitutions and the native W9(mid) profile are declared finite algebraic probes. The Minimal Axioms do not supply an outcome instrument, conditional law, formation weights, measurement update, gravity variable, or continuum interpretation; nothing is registered or adopted.
per_site: On Site(12x4,12,4), the declared W9-L5 mixture residual has four nonzero exact rational components with signs (+,-,+,+) and zero sum. The associated 4-by-4 system has ranks (4,4), a unique nonnegative unit-sum solution, and that solution differs from all four declared candidate profiles.
per_mode: The six W9/W2 level profiles each admit a nonnegative unit-sum four-weight with ranks (4,4), while their 25-by-4 stack has ranks (4,5). This excludes only one common four-component coefficient vector for these declared profiles, not richer latent spaces or classical models.
per_block: The selected slot-5 row block has exact substitution deltas (0,0,0,0), yet the clean W9-L5/W2-L5 stack has ranks (4,5); this is an entrywise row-block certificate, not causal isolation. After the specified hermitization W9-L5 equals W2-L5, while the separate W9 three-level stack remains rank-inconsistent.
lattice_wide: At fixed spatial dial (1/3,1/4), the residual is non-even under q -> -q, but Q(-1)-conj(Q(1)) has exact nonzero-entry counts (96,92,92,92,92). Therefore q flip is not global conjugation here, no phase or intensity mechanism is selected, every claim remains finite-instance proposed_retained, and TOE movement is zero.

Only the `per_site`, `per_mode`, and `per_block` calculations are executed as
positive matrix tests. `per_element` and `lattice_wide` are checked boundaries:
the runner explicitly records that no framework instrument or physical
mechanism is executed there. Accordingly the note never promotes “no common
four-weight” beyond the selected `per_mode` systems.

### N6 — partial-closure path scan

| possible path | status | what it could close |
| --- | --- | --- |
| [Axiom/premise registry](audit/data/axiom_premise_nodes.json) | current authority, scanned | contains no approved record-instrument or conditional-law primitive; no existing primitive closes `W1` or `W2` |
| [Block 171](ADMISSIBILITY_DIRAC_KAHLER_GENERATOR_TRILEMMA_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-21.md) | proposed finite construction | supplies the matrix/profile map but not mutually exclusive outcomes or formation weights |
| convention/reframe route | open | could rename the four profiles as diagnostic substitutions and thereby remove the physical-record wall without changing the rank theorem; this is the repair adopted here |
| explicit instrument import followed by retirement audit | open | could supply physical outcome/conditional semantics, after which the six-system test would need to be rebuilt for that instrument |

The note does not say that a new axiom is required. A convention reframe already
closes the naming overclaim, while a genuine physical instrument remains an
open import-bearing derivation route.

### N7 — hostile steelman

A hostile reviewer should reject any claim that these four substitutions
exhaust record formation: the class-value label is held fixed, the selected
profiles arise from a global inverse, and the Minimal Axioms do not say that the
four matrices are mutually exclusive conditionals. A refined latent space, an
instrument with additional outcome labels, or context-dependent response
weights can evade the `25 x 4` obstruction. The actionable terminal obligation
is to derive such an instrument from approved premises and then reconstruct its
profile matrix. This steelman is convincing against a physical or classical
no-go, so those broader claims are withdrawn; it does not alter the exact
fixed-ansatz rank inequality.

### N8 — cross-cycle echo and decision cut

The repository scan finds structurally similar “missing selection map” walls in
[Block 201](ADMISSIBILITY_DIRAC_KAHLER_COVARIANT_RULE_IDENTIFICATION_BOUNDED_THEOREM_NOTE_2026-08-26.md): finite encodings survive while physical selection remains open. That wall has not been retired; its proposed mechanism—derive an independent selector and bridge—applies here as “derive an independent record instrument and response map.” Block 171's earlier profile construction likewise did not retire this semantic wall. No prior wall is cited as permanently closed, and no convention ratification is mistaken for new physics.

Decision: retain the exact finite residuals, ranks, support counts, and
hermitization identities as `proposed_retained`. Withdraw the physical
record-formation, contextuality/interference, conjugation, and
intensity-exclusion readings. Register no premise, adopt no object, move no TOE
percentage, and require independent audit before effective retention.

## Verification contract

The runner declares 31 claim-only mutations. Each mutation must fail exactly
its mapped gate. Baseline output must remain below the runner-output cap; the
canonical cache must carry the runner hash and full input fingerprint.

## Decision

This block is a useful exact finite discriminator, not yet a physical rule.
The repaired version keeps every independently reconstructed rank and residual,
adds the missing conjugation countercheck, and narrows the conclusion to what
those calculations establish.
