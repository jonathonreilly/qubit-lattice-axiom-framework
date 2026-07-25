# Wave 2 — Prior art and composition: what a new note must ADD vs merely CITE

**Agent:** wave-2 prior-art/composition scout. **Date:** 2026-07-25.
**Read against:** `origin/main` @ `c815a83a5f` (fetched this session; the local
worktree is far behind, so every file and every ledger shard below was read
from a `git archive origin/main` extraction, never from the working tree).

**Rule compliance.** No commit, no push, no PR. The only file written in the
repo is this report. No audit verdict is set, predicted, or estimated; every
status below is a transcription of a live `effective_status` shard field. No
axiom, primitive, or new vocabulary is proposed. My own load-bearing algebra
is rebuilt natively in exact sympy (§6) and is labelled a **worker probe, not
a runner gate**.

---

## 0. HEADLINE — the campaign has walked into its own trap

**The two-point-menu witness is ELEVEN DAYS OLD, it is already on
`origin/main`, and it is already computed by an exact sympy runner there.**

`scripts/qubit_symmetry_exchange_law_reduction_probe_2026_07_14.py` (committed
to `origin/main`) contains these gates, verbatim from the source:

```
check("B diagonal SU(2) commutant has complex dimension two", len(basis) == 2, ...)   # :87
check("B identity lies in the computed commutant", ...)                               # :92
check("B SWAP lies in the computed commutant", ...)                                   # :93
check("B identity and SWAP are independent", ...)                                     # :94
check("C independent onsite SU(2) commutant has dimension one", len(basis) == 1, ...) # :108
check("D SWAP spectrum is triplet plus singlet", ...)                                 # :121
check("D plus-SWAP ground sector is the rank-one singlet", ...)                       # :127
check("D minus-SWAP ground sector is the rank-three triplet", ...)                    # :128
```

Its source note states the campaign's headline in the campaign's own words:

> Then Schur-Weyl duality becomes an exact simplifier. The commutant of the
> diagonal `SU(2)` action `U tensor U` on two qubits is the span of identity
> and SWAP.
>
> — `docs/work_history/repo/review_feedback/QUBIT_SYMMETRY_EXCHANGE_LAW_REDUCTION_PROBE_NOTE_2026-07-14.md:21-23`

> **What The Reduction Does Not Select** — Both `+SWAP` and `-SWAP` have the
> same locality and covariance. Their triplet and singlet ground sectors are
> reversed: `+SWAP` has a one-dimensional singlet ground space, while `-SWAP`
> has a three-dimensional triplet ground space. … Therefore sign and scale do
> not follow from the classification.
>
> — same file, `:52-59`

and a sibling states the quotient argument — the exact sentence Wave 1
reported as its own delta:

> For common qubit-frame covariance, two-site Hermitian invariants are
> `h_xy = a I + b SWAP_xy`. Positive time/action scaling and a genuinely
> global scalar shift remove `a` and one positive magnitude. **They do not
> remove the sign of `b`.**
>
> — `docs/work_history/repo/review_feedback/SINGLE_INVARIANT_ACTION_STEELMAN_ATTACK_NOTE_2026-07-14.md:152-159`

**Three further findings, in descending order of consequence:**

1. **The completeness statement is also in `docs/` proper**, in a
   ledger-registered note, one day after the 07-10 countermodel:
   `RECORD_FAITHFUL_CUBIC_NEIGHBOR_RESPONSE_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-11.md:180-182`
   — "**Demand common `SU(2)` naturality on an undirected two-qubit edge:** the
   commutant is spanned by `I` and `SWAP`". It is a one-line ungated
   refutation leg (§3.2), but it is the completeness claim.

2. **The campaign's chosen SEPARATOR does not survive the campaign's own
   quotient.** I verified exactly (§6, D01/D01b/D03/F01/F02): on the
   one-excitation carrier, `k -> k+(pi,pi,pi)` *is* `b -> -b` up to the inert
   constant `-12b`; re-anchored, the two symbols are **identical**; both menu
   points have one-excitation bandwidth `12`; and the uniform link-sign flip
   that relates them multiplies every square plaquette by `(-1)^4 = +1`, so
   **both menu points sit in the SAME landed frame class `K0`** of the 06-10
   two-flux-class theorem. The band-minimum location is a gauge coordinate,
   not an invariant. The 07-14 separator (ground-sector degeneracy 1 vs 3) is
   strictly stronger and survives shift, positive rescale, *and* every
   unitary.

3. **"The menu is COMPLETE — exactly two laws" is FALSE as stated about the
   matter law, and the corpus already refutes it with a gated runner.**
   `SINGLE_INVARIANT_ACTION_STEELMAN_ATTACK_NOTE_2026-07-14.md:161-177` shows
   the invariant family **enlarges immediately on three sites**, with a
   dimensionless spectral-gap ratio moving `2 -> 1`, gated at
   `scripts/single_invariant_action_steelman_attack_probe_2026_07_14.py:239`.
   I reproduced both values exactly (§6, E04/E05/E07). Two-point completeness
   is a statement about the **two-site edge term under a supplied
   sum-of-identical-pair-terms ansatz**, not about the matter law.

Net: the negative is not "~80% written across six uncomposed notes". On the
edge-menu leg it is **~100% written and ~100% gated**, in a corpus the
campaign did not sweep. What remains genuinely unwritten is narrow, and it is
named in §5.

---

## 1. Mandatory framework refresher — surfaces read this wave

Read in full from `origin/main`, not from memory:

| Surface | What I took from it |
|---|---|
| `docs/MINIMAL_AXIOMS_2026-06-29.md` (all 194 lines) | four-axiom text; Qualification `:74-79`; dynamics disclaimer `:103-118`; open gates `:156-173` incl. `:170` source/action |
| `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (all 46 lines) | six-step check; `:13-16` "dynamics, source/action … remains separate unless independently derived" |
| `docs/audit/data/axiom_premise_nodes.json` (full) | `canonical_ids` = `minimal_axioms`, `scale_reference_primitive`, `kinetic_isotropy_primitive`, `realized_state_primitive` |
| primitive source notes, via the registry node text | `kinetic_isotropy_primitive` grants **only** the structural OS0 kinetic-form isotropy `c_t = c_s` and nothing else — explicitly "not an absolute scale, spacing-ratio theorem, **dynamics**, or downstream Lorentz theorem"; `realized_state_primitive` "does not supply a state, state-selection rule, **measure**, …"; `scale_reference_primitive` "units conversion only" |
| `docs/audit/data/ledger/` — all 3867 shards | every status below; independent no-go census re-run (§2.0) |
| ~20 lane notes + 4 archived probe notes + 3 runners | §2-§4 |

I invoke **no** approved primitive as a proof input anywhere in this report. I
cite `kinetic_isotropy_primitive` once, only to record what it excludes, and I
do not extend it past `c_t = c_s`.

---

## 2. (a) Every surface carrying part of this negative

### 2.0 Status context, re-measured independently

I re-ran the no-go census directly over the shards rather than trusting
Wave 1: **438 `claim_type: no_go` rows on `origin/main` — 437 `unaudited`,
1 `audited_conditional`, 0 at any retained grade.** Wave 1's number is
correct. Consequence for composition: **every "cite" target below is
`unaudited`.** A new note cannot lean on any of them as a retained authority;
it can only cite them as source-note prior art at their live grade.

### 2.1 The `docs/` (ledger-registered) carriers

| # | claim id | What it establishes for THIS negative | LIVE `effective_status` |
|---|---|---|---|
| 1 | `staggered_dirac_minimal_surface_kinetic_corner_nonforcing_no_go_note_2026-07-10` | The four axioms do not select a nonzero **first-order staggered** kinetic law or its 8-corner zero set; explicit `Phi = I - SWAP` countermodel with symbol `4 sum sin^2(k_mu/2)`, one corner zero | `unaudited` |
| 2 | `record_faithful_cubic_neighbor_response_classification_bounded_theorem_note_2026-07-11` | **The completeness statement** (`:180-182`), AND a separate gated exactly-two classification on the directed-neighbor surface (`:40`), AND the exact discriminator name (`:120`) | `unaudited` |
| 3 | `staggered_dirac_kinetic_class_forcing_narrow_theorem_note_2026-06-10` | Covariance up to site-local `U(1)` frame collapses the licensed bilinear family to **EXACTLY TWO** flux classes `{K0,K1}`; the `K1`-vs-`K0` bit is **NOT forced** (`K0` is the computed countermodel, boundary `B-BIT`) | `unaudited` |
| 4 | `staggered_dirac_substep1_statistics_agnostic_no_forcing_note_2026-05-25` | Statistics not forced: hard-core boson has per-site dim 2 and the same ungraded algebra; "Substep 1 is a **compatibility, not a forcing**" | `unaudited` |
| 5 | `staggered_dirac_substep1_grassmann_forcing_bridge_narrow_theorem_note_2026-05-16` | The **Grassmann forcing bridge** disclaims statistics forcing in its own scope (`:24-27`) and names `(B-stat)` exhaustiveness as the surviving boundary (`:496-505`) | `unaudited` |
| 6 | `minimal_record_instrument_dilation_scalar_exchange_nonselection_bounded_theorem_note_2026-07-11` | Common-frame invariance of the `I-SWAP` family stated on the **full two-qubit edge carrier** and restricted exactly to the one-excitation sector (`:160-190`); dilation minimality does not select the exchange angle | `unaudited` |
| 7 | `p_flux_selection_from_matter_content_narrow_no_go_note_2026-06-10` (+2 siblings, same date) | Three independent routes fail to derive the last kinetic bit | `unaudited` (all three) |
| 8 | `staggered_dirac_substep4_labeling_no_go_note_2026-05-17` | Species labeling not derivable from the minimal baseline | `unaudited` |
| 9 | `bridge_gap_action_form_uniqueness_no_go_note_2026-05-06` | **Sibling result, gauge sector:** Wilson / heat-kernel / Manton jointly compatible; "The framework's derived action is action-form ambiguous" | `unaudited` |
| 10 | `koide_kahler_dirac_silent_on_measure_note_2026-05-30` | The Kähler-Dirac route derives no measure (`:4-5`: "This note does not derive the Koide mass measure") | `unaudited` |
| 11 | `acphilambda_record_outcome_orbit_occupancy_non_supply_no_go_note_2026-07-04` | **The declared-gap note.** Readout-level non-entailment only; explicitly declines the matter-law-level claim (`:112-116`) | `unaudited` |
| 12 | `staggered_dirac_exercise_honest_reassessment_note_2026-06-06` | `/exercise` run correcting the "forced ×6" framing; names 3 hidden admissions | `unaudited` |
| 13 | `extensional_nearest_neighbor_rule_deep_probe_2026-07-13` | Admissibility's rule statement is compatible with **two inequivalent finite global algebras** — a same-shape non-entailment on the *rule*, not the law | **`retained_bounded`** |
| 14 | `pairwise_commuting_endpoint_symmetric_edge_hamiltonian_classification_and_strict_qca_boundary_bounded_theorem_note_2026-07-12` | A *different* exact edge-density classification (endpoint-SWAP-symmetric, overlap-commuting) → `c II + r(ZI+IZ) + g ZZ` | `unaudited` |

Row 13 is the only retained-grade row in the whole list and it is **not** about
the matter law. Nothing here is available as a retained authority.

### 2.2 The archived carriers the campaign did not sweep

`docs/work_history/repo/review_feedback/` is a 450-file archive whose own
README calls it "**historical detailed review packets** … Do **not** use this
directory as the live queue." These four files have **no ledger row and no
claim id** (I checked: `find docs/audit/data/ledger -iname '*qubit_symmetry*'`
etc. return nothing) — they are `Authority: none` campaign evidence archived
under commit `9caad99bab "archive: preserve TOE bridge campaign evidence
through cycle335"`. They **are** nodes in
`docs/audit/data/citation_graph_manifest.json`, so they are indexed corpus
surfaces, and each has a **live exact runner in `scripts/`**.

| File (all `2026-07-14`, all in `docs/work_history/repo/review_feedback/`) | Runner on `origin/main` | What it already contains |
|---|---|---|
| `QUBIT_SYMMETRY_EXCHANGE_LAW_REDUCTION_PROBE_NOTE_2026-07-14.md` | `scripts/qubit_symmetry_exchange_law_reduction_probe_2026_07_14.py` | commutant = span{I,SWAP}, dim 2 (`:87-94`); independent-onsite reading gives dim 1 (`:108-111`); `SWAP` spectrum triplet+singlet (`:121`); **+SWAP singlet-1 vs −SWAP triplet-3 ground-sector reversal** (`:127-128`) |
| `SINGLE_INVARIANT_ACTION_STEELMAN_ATTACK_NOTE_2026-07-14.md` | `scripts/single_invariant_action_steelman_attack_probe_2026_07_14.py` | "common-SU2 pair invariants have dimension two" (`:194`); **the shift/positive-rescale quotient leaving sign(b)** (`:152-159`); **three-site enlargement, gap ratio 2→1** (`:161-177`, gated `:239`) |
| `FULL_LAW_INVENTORY_ADVERSARIAL_REDUCTION_NOTE_2026-07-14.md` | `scripts/full_law_inventory_adversarial_reduction_probe_2026_07_14.py` | `## 9. Exchange-Reduction Audit` (`:314`): "The diagonal `SU(2)` commutant calculation is correct: `commutant(U tensor U) = span{I,SWAP}`" (`:316-319`), plus six named boundaries |
| `RELATIONAL_QUBIT_DISAGREEMENT_CANONICAL_LAW_ESCALATION_NOTE_2026-07-14.md` | `scripts/relational_qubit_disagreement_canonical_law_escalation_probe_2026_07_14.py` | "the commutant of `U tensor U` is `span{I,SWAP}` … `h = a I + b SWAP`" (`:147-150`); "**Positive scale and scalar shift do not remove that sign**" (`:168-169`) |

### 2.3 The exact reusable sentences (quote these; do not re-derive them)

**The declared gap the campaign is filling — quote verbatim, it is the reason
the note exists:**

> Since `F_R=2F_C`, this witness proves underdetermination of the raw
> determinant-power normalization; **it does not prove that two inequivalent
> matter actions or Gaussian measures exist.** Calling either functional a
> physical occupancy law would require the action/readout bridge that is
> absent from this construction.
>
> — `ACPHILAMBDA_RECORD_OUTCOME_ORBIT_OCCUPANCY_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md:112-116`

**The landed countermodel and its exact scope:**

> **Theorem (minimal-surface kinetic/corner non-forcing).** Lattice, Qubit,
> Admissibility, and Record do not select a nonzero first-order staggered
> kinetic law or the associated eight-corner Bloch-symbol zero set. This
> remains true after additionally asking for a nonzero, Hermitian,
> number-conserving, nearest-neighbor, translation-invariant, and
> proper-cubic-invariant physical matter law.
>
> — `STAGGERED_DIRAC_MINIMAL_SURFACE_KINETIC_CORNER_NONFORCING_NO_GO_NOTE_2026-07-10.md:239-244`

> This no-go is about selection, not mathematical definability. … The
> conclusion denied is that the framework premises designate it as the
> physical kinetic law. — same file, `:255-258`

> Because `SWAP` commutes with every common one-site frame change
> `U tensor U`, the law privileges no one-site possibility or Pauli axis.
> — same file, `:202-204`

**The completeness statement, already written:**

> - **Demand common `SU(2)` naturality on an undirected two-qubit edge:** the
>   commutant is spanned by `I` and `SWAP`; this favors the scalar exchange
>   class rather than deriving spatial-to-Bloch locking.
>
> — `RECORD_FAITHFUL_CUBIC_NEIGHBOR_RESPONSE_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-11.md:180-182`

**The pre-existing warning against exactly the move the campaign wants:**

> "No possibility is privileged" does not itself say whether local basis
> changes act together or independently. … The current Qubit prose supplies
> neither interpretation as a dynamical law. **Promoting the exchange result
> without choosing and defending the covariance meaning would hide a new
> physical premise in a symmetry slogan.**
>
> — `QUBIT_SYMMETRY_EXCHANGE_LAW_REDUCTION_PROBE_NOTE_2026-07-14.md:40-50`

**The residual after the supply, worth keeping as the positive half:**

> The final selection `K1` vs `K0` (one bit; the kinetic-order bit) is NOT
> forced by the specified constraint set: `K0` is the computed countermodel
> (boundary B-BIT). P-KIN's premise content is thereby reduced from an
> infinite-dimensional declaration … to exactly the flux-`−1` selector bit.
>
> — `STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md:19-25`

**Statistics not forced:**

> **Conclusion (the no-go).** Substep 1 is a **compatibility, not a forcing**.
> … The Grassmann content remains an **admission candidate** (a statistics
> selection), not a theorem derived here from the baseline alone.
>
> — `STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md:74-80`

> This is collapse **within the two-candidate surface only**: it is NOT a
> statistics-forcing theorem — the hard-core-boson frame ties with (G) on
> every readout checked here.
>
> — `STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md:24-27`

**Sibling precedent for the shape of the claim (gauge sector):**

> The framework's derived action is action-form ambiguous; distinct admissible
> actions remain compatible with the current support.
>
> — `BRIDGE_GAP_ACTION_FORM_UNIQUENESS_NO_GO_NOTE_2026-05-06.md:7-13`

---

## 3. (b) What is genuinely NEW — stated unflatteringly

### 3.1 What the 07-10 no-go actually proves with `Phi = I − SWAP`

Exactly one thing: **a universal selection claim is false because one model of
all its premises carries a different physical law** (`:246-253`). `Phi` is used
as a *single existence witness*. The note computes its symbol, shows the zero
set is `{k ≡ 0}` (one corner, not eight), and stops. It never classifies the
class `Phi` lives in, never counts its dimension, and never exhibits a second
member. `SWAP`'s commutation with `U ⊗ U` appears at `:202-204` purely as a
*verification* that `Phi` satisfies the Qubit no-privilege clause — not as a
classification lemma. The word "commutant" does not appear in the note.

So the campaign is right that the 07-10 note does not carry completeness.

### 3.2 But the completeness IS carried — twice, and one of the two is gated

- **`docs/`, ungated:** `RECORD_FAITHFUL…2026-07-11.md:180-182` states it
  (§2.3). I read the paired runner
  `scripts/record_faithful_cubic_neighbor_response_2026_07_11.py` and listed
  all 27 of its gates: `G01-G03`, `I01-I07`, `C01-C05`, `K01-K06`, `F01-F03`.
  **None computes the commutant.** The leg is prose only. That is the single
  strongest argument that a new note has something to do.
- **`scripts/`, GATED:** `qubit_symmetry_exchange_law_reduction_probe_2026_07_14.py:87-94`
  computes it exactly, and `single_invariant_action_steelman_attack_probe_2026_07_14.py:194`
  computes it a second time independently. Both are on `origin/main`.

**A new note claiming "the commutant is exactly 2-dimensional" as its
contribution would be re-reporting a landed, running computation.**

### 3.3 Delta table — Wave-1 witness component by component

| Wave-1 component | Already on `origin/main`? | Where |
|---|---|---|
| commutant of `u⊗u` = span{I,SWAP}, dim 2 | **YES, gated** | probe runner `:87-94`; second computation at steelman `:194`; prose at `RECORD_FAITHFUL…:180-182`, `FULL_LAW…:316-319`, `RELATIONAL…:147-150` |
| quotient by inert identity shift + positive rescale | **YES** | `SINGLE_INVARIANT…:152-159`; `RELATIONAL…:168-169` |
| surviving invariant is `sign(b)` → a 2-point set | **YES** | same two lines |
| both signs satisfy every property the 07-10 theorem names | **YES** | `QUBIT_SYMMETRY…:54` "Both `+SWAP` and `-SWAP` have the same locality and covariance" |
| a shift/scale-invariant physical separator | **YES, and a better one** | `QUBIT_SYMMETRY…:54-57` ground-sector 1 vs 3, gated at probe `:127-128` |
| mutation: independent-onsite covariance → dim 1 | **YES, gated** | probe `:108-111` |
| **mutation: `u ⊗ conj(u)` → dim 2, different basis** | **no** | genuinely absent |
| **mutation: `σ_z` subgroup → dim 6** | **no** | genuinely absent |
| **the `Z^3` one-excitation Bloch symbol `2b(Σcos k − 3)`** | **no** — but see §4 | it is not an invariant |
| **explicit tie to the 07-04 declared gap** | **no** | nobody has connected them |
| **composition into one no-go about the matter action** | **no** | the actual hole |

### 3.4 Is the witness a special case of something landed?

Partly, and the campaign should say so plainly:

- The **exactly-two shape** is a special case of a landed, gated pattern. The
  same note that carries the commutant leg proves, with a runner (`I01`: rank
  22 on 24 coefficients; `I02`: nullity 2), that the directed-neighbor
  equivariant map space is **also exactly two-dimensional**, `F(c) = a[Σc]I +
  bΣ(c_+ − c_-)Γ`, with the sharp discriminator "**scalar even response versus
  spatial-vector odd response**" (`:120`). In that landed normal form the
  07-10 countermodel is named as the explicit point `(m,a,b) = (6,−1,0)`
  (`:103-104`). **The campaign's two menu points are `(6,−1,0)` and `(6,+1,0)`
  — two points inside the landed `b = 0` scalar-even branch, differing in the
  sign of `a`, a parameter the landed classification already quantifies over.**
- Worse for the framing: that note's conditional corollary (given supplied
  spectral faithfulness) forces `b ≠ 0` and therefore **excludes the whole
  `b = 0` branch — both campaign menu points at once**. That does not defeat
  the non-forcing conclusion (`:130`: "The spectral-faithfulness sentence is
  not a theorem of the four axioms"), but it means the campaign's "two points"
  are two members of one conditionally-excludable class, not two branches of a
  live fork.
- The **two-flux-class** theorem (`…KINETIC_CLASS_FORCING…2026-06-10`) is a
  landed "exactly two" on the licensed bilinear surface, quotienting by
  site-local `U(1)` frame. §4 shows the campaign's bit is *inside* one of its
  two classes.

---

## 4. (c) THE COMPLETENESS QUESTION — answered, and the answer is bad twice

**Q: does any landed note already state the completeness?**
**A: yes** — `RECORD_FAITHFUL…2026-07-11.md:180-182` (ungated prose, in a
ledger-registered `unaudited` note), and the archived 07-14 probe corpus
states it four times with two independent exact runners. It is not new.

**Q: is "the menu is complete, exactly two laws" even true?**
**A: only for the two-site edge term under a supplied ansatz — and the corpus
already publishes the refutation of the general reading.**

`SINGLE_INVARIANT_ACTION_STEELMAN_ATTACK_NOTE_2026-07-14.md:161-177` exhibits,
on three sites with a center and two equivalent neighbors,

```
H_1 = SWAP_01 + SWAP_02 ,   H_2 = SWAP_01 SWAP_02 + SWAP_02 SWAP_01 ,
H_eta = H_1 + eta H_2
```

both Hermitian, neighbor-exchange invariant, and common-frame invariant, with
a **dimensionless** gap ratio moving from `2` at `eta=0` to `1` at `eta=1/3` —
"Neither clock rescaling nor energy shift changes that ratio." I rebuilt this
exactly (§6, E01-E07): `I, H_1, H_2` are independent; spectra `[-1,1,2]` and
`[-4/3,2/3,8/3]`; ratios `2` and `1`; and my constant-mutation at `eta=1/4`
gives `8/7 ≠ 1`, so `1/3` is computed, not labelled.

The 2-point count therefore rides on the *supplied* ansatz "a sum of identical
nearest-neighbor **two-site** terms" — premise (2) of the reduction probe's own
three declared premises (`QUBIT_SYMMETRY…:13-18`, alongside (1) an autonomous
strongly continuous reversible generator and (3) common-basis covariance).
**A note that says "the menu is complete: exactly two matter laws" would be
refuted on `origin/main` by a runner that is already green.**

### 4.1 New finding: the campaign's separator fails its own quotient

This is mine, verified exactly (§6), and it is the load-bearing correction.

- `k → k+(π,π,π)` acts on the one-excitation symbol **exactly as `b → −b`**,
  up to the constant `−12b` (D01). Re-anchoring both symbols at their own
  `k=0` value makes them **identical** (D01b). Both menu points have
  one-excitation bandwidth `12` (D03).
- The relabeling that does this is the bipartite site-local sign
  `V(x) = (−1)^{x_1+x_2+x_3}` — a **site-local frame change**, exactly the
  equivalence the landed 06-10 theorem already quotients by ("each up to
  site-local `U(1)` frame", `:10-11`).
- Equivalently, at the link level: a uniform link-sign flip multiplies every
  square plaquette by `(−1)^4 = +1` (F01), so `b>0` and `b<0` carry the **same
  uniform plaquette flux** and therefore lie in the **same landed class `K0`**.

So "band minimum at `k=0` versus `k=(π,π,π)`" is a gauge coordinate. It is
*not* "a separator invariant under every positive rescaling and shift" in any
sense that separates physics, because the relevant equivalence is larger than
shift+rescale and the corpus already uses the larger one.

**The separation is real but lives one carrier up.** On the full two-qubit
edge carrier the site-local sign sends `SWAP` to an operator that is neither
`±SWAP` nor in `span{I,SWAP}` at all (D04/D05) — it exits the class — so the
two laws remain inequivalent there. The invariant that carries this is the
07-14 one: **ground-sector degeneracy 1 (singlet) vs 3 (triplet)**, which I
verified is unchanged under `s>0` rescale and `c` shift (C04) and, being a
degeneracy, under every unitary.

**Campaign action required: replace the band-minimum separator with the
ground-sector-degeneracy separator, and cite `QUBIT_SYMMETRY…:54-57` for it.**

---

## 5. (d) The narrowest honest claim, and the cite-vs-prove split

### 5.1 What a new note may honestly claim

Everything about the two-site edge menu is taken. The one thing nobody has
done is **compose the scattered negative into a single statement about the
object the obligation names, and connect it to the declared gap.** So:

> **Proposed narrowest claim.** On the current four-axiom surface plus the
> three approved primitives, the physical matter law is not determined: two
> laws that satisfy every property the 2026-07-10 non-forcing theorem names
> are inequivalent under the full framework-native equivalence (common
> one-site frame change, site-local frame change, constant shift, positive
> rescaling), the invariant that separates them being the edge ground-sector
> degeneracy `1` versus `3`. This supplies, at matter-law level, the witness
> whose absence `ACPHILAMBDA_RECORD_OUTCOME_ORBIT_OCCUPANCY_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md:112-116`
> records in its own words. The count `2` is **not** claimed for the matter
> law: it holds only for the two-site edge term under a supplied
> identical-pair-term ansatz, and the invariant family enlarges on three
> sites.

Three boundaries the note must carry on its face, or a reviewer will and
should reject it:

- **(B-cov)** the count is carried by the *common-basis* reading of "no
  possibility is privileged"; the independent-onsite reading gives dimension
  one and no nontrivial pair interaction at all. Quote
  `QUBIT_SYMMETRY…:40-50` and do not resolve the reading.
- **(B-ansatz)** the count is two-site; three sites enlarge it
  (`SINGLE_INVARIANT…:161-177`).
- **(B-branch)** both menu points are the landed `b = 0` scalar-even branch and
  the landed conditional spectral-faithfulness corollary would exclude both
  together (`RECORD_FAITHFUL…:100-110, :130`).

### 5.2 CITE, do not re-prove

| Object | Cite (at its live grade, all `unaudited` unless noted) |
|---|---|
| commutant `= span{I,SWAP}`, dim 2 | `RECORD_FAITHFUL…2026-07-11.md:180-182` **and** `scripts/qubit_symmetry_exchange_law_reduction_probe_2026_07_14.py:87-94` |
| shift + positive-rescale quotient; `sign(b)` survives | `SINGLE_INVARIANT_ACTION_STEELMAN_ATTACK_NOTE_2026-07-14.md:152-159`; `RELATIONAL…:168-169` |
| ground-sector 1 vs 3 separator | `QUBIT_SYMMETRY…:52-59`; runner `:121, :127-128` |
| covariance-reading dependence (dim 2 vs 1) | `QUBIT_SYMMETRY…:40-50`; runner `:108-111` |
| three-site enlargement, ratio 2→1 | `SINGLE_INVARIANT…:161-177`; runner `:239` |
| the four-axiom countermodel and its exact scope | `…NONFORCING_NO_GO…2026-07-10.md:239-258` |
| the two-flux-class collapse and `B-BIT` | `…KINETIC_CLASS_FORCING…2026-06-10.md:7-25, 384-392` |
| statistics not forced | `…STATISTICS_AGNOSTIC…2026-05-25.md:74-80`; `…GRASSMANN…2026-05-16.md:24-27, 496-505` |
| the declared gap being filled | `ACPHILAMBDA…NON_SUPPLY_NO_GO…2026-07-04.md:112-121` |
| measure silence on the KD route | `KOIDE_KAHLER_DIRAC_SILENT_ON_MEASURE_NOTE_2026-05-30.md:4-5` |
| gauge-sector precedent for the claim shape | `BRIDGE_GAP_ACTION_FORM_UNIQUENESS_NO_GO_NOTE_2026-05-06.md:7-13` |
| axiom-surface exclusions | `MINIMAL_AXIOMS_2026-06-29.md:103-118, :170`; `PRIMITIVE_REGISTRY_CHECK.md:13-16` |

### 5.3 ADD (build natively in note + runner)

1. **The equivalence statement itself.** Nobody has written down the full
   framework-native equivalence (common frame × site-local frame × shift ×
   positive rescale) and asked which of the two candidate separators survives
   it. §4.1 is the answer and it is new. This is the note's only genuinely new
   *theorem-shaped* content, and it is a **correction** to the campaign's own
   Wave-1 framing, not a confirmation of it.
2. **The gauge-triviality of the sign bit at one-particle level** — that the
   two menu points share a plaquette flux and therefore one landed class `K0`
   (F01/F02). This connects the campaign's witness to the 06-10 theorem, which
   nobody has done.
3. **The composition**: one place where the seven scattered negatives (rows
   1, 3, 4, 5, 7, 8, 11 of §2.1) are stated as one sentence about the matter
   action, with the 07-04 declared gap named as the target.
4. The two absent mutations (`u ⊗ conj(u)`; `σ_z` subgroup), as construction
   mutations demonstrating the count is demand-carried.

### 5.4 DO NOT claim

- "The menu is complete: exactly two matter laws." Refuted on `origin/main` by
  a green runner (§4).
- "The commutant being 2-dimensional is new." It is eleven days old and gated.
- "Band minimum at `k=0` vs `k=(π,π,π)` is an invariant separator." §4.1.
- Any retained-grade citation of any no-go. There are none (§2.0).
- Any statement that this discharges, narrows, or weakens the obligation.

---

## 6. Worker probe — native exact rebuild (NOT a runner gate)

`…/scratchpad/wave2_prior_art_probe.py`, pure sympy over exact rationals and
symbols; **no float is ever an input**. **WORKER-PROBE TOTAL: PASS=40 FAIL=0.**
This is a worker probe supporting *this report's* claims. It is not a gate, it
grades nothing, and no note may cite it.

- **A (commutant).** Generic 16-real-parameter Hermitian `4×4` solved against
  the three diagonal generators `σ_a⊗I + I⊗σ_a`: exactly **2** free real
  parameters, and the solution equals `α(I⊗I) + β·SWAP` **exactly**;
  independently, `SWAP` commutes with `u⊗u` for a **generic symbolic** `u`.
  Construction mutations: no frame demand → 16; independent onsite frames →
  **1**; `u ⊗ conj(u)` → 2 but the basis is **not** `{I,SWAP}` (so the reading
  fixes the basis, not only the count).
- **B (symbol).** Derived from the action of `Σ_edges(aI + b·SWAP)` on a
  one-flip state, not quoted: `σ(k) − σ(0) = 2b(Σcos k_μ − 3)`; corner
  separator `−12b`; at `b=−1` it reproduces the 07-10 graph Laplacian.
  Constant mutation over `d = 1,2,3,4` gives `−4d`, so `12` tracks `d=3`.
- **C (landed separator).** `+SWAP`: bottom eigenvalue `−1`, degeneracy **1**.
  `−SWAP`: bottom eigenvalue `−1`, degeneracy **3**. Degeneracy unchanged
  under `s>0` rescale and `c` shift.
- **D (campaign separator fails).** `k→k+(π,π,π)` equals `b→−b` up to the
  inert constant `−12b`; re-anchored the symbols are identical; both
  bandwidths `12`. But on the full edge carrier the same site-local sign sends
  `SWAP` outside `span{I,SWAP}` entirely, so the many-body separation survives.
- **E (three sites).** `I, H_1, H_2` independent; spectra `[-1,1,2]` and
  `[-4/3,2/3,8/3]`; gap ratios `2` and `1`; mutation `eta=1/4 → 8/7 ≠ 1`.
- **F (gauge triviality).** Uniform link-sign flip multiplies each square
  plaquette by `(−1)^4 = +1`; the bipartite sign takes opposite values on every
  `Z^3` edge.

**Two probe errors caught and recorded rather than silently fixed.** (i) I
first asserted `k`-shift `≡ b→−b` on the nose; it is true only modulo the
inert constant `−12b` — the corrected form is what §4.1 uses. (ii) I used the
inverted gap-ratio convention and got `1/2` where the 07-14 note reports `2`;
the note's convention is lower-gap-over-upper-gap and reproduces exactly.

---

## 7. Non-claims

This report sets, predicts, and estimates **no** audit verdict, and grades no
row; every status is a transcription of a live `docs/audit/data/ledger/` shard
field on `origin/main`, and `unaudited` means *awaiting audit*, not *refuted*.
It proposes no axiom, no primitive, no convention, and no new repo vocabulary.
It derives no `r`, `Q`, `delta`, mass, coupling, mixing angle, phase, grain,
or sector weight. It selects no action and no measure. It asserts no defect in
any note's physics: the 07-10, 07-11, and 07-14 surfaces are cited as prior art
at their own declared scope, and the 07-14 archive is explicitly `Authority:
none` by its own header. The §6 probe verifies this report's own reasoning; it
promotes nothing and may not be cited as a gate. No file in `docs/` or
`scripts/` was modified.
