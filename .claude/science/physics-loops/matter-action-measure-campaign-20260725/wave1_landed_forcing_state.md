# Wave 1 — Landed forcing state of the matter action

**Agent:** wave-1 landed-forcing-state scout. **Date:** 2026-07-25.
**Read against:** `origin/main` @ `e192e332f2` (fetched this session). The local
worktree is 1057 files behind main, so **every file and every ledger shard in
this report was read from `origin/main` via `git show`/`git grep`**, never from
the working tree.

**Rule compliance:** no commits, no pushes, no PRs; this file is the only file
written in the repo. No audit verdict is set or predicted anywhere below —
where I give a status it is a transcription of a live ledger shard field.

---

## 0. Headline

**The matter action is supplied at the very first link, and the repo already
contains the theorem that says so.**

There is no derived link between the four axioms and the staggered-Dirac
action. The first step out of the axioms is *already* an import. Everything the
lane calls "forcing" — Kawamoto-Smit phases, BZ corners, species counts,
Kähler-Dirac equivalence — is downstream of, and conditional on, that first
supplied step.

The negative is landed, not new:
`STAGGERED_DIRAC_MINIMAL_SURFACE_KINETIC_CORNER_NONFORCING_NO_GO_NOTE_2026-07-10.md`
proves by explicit countermodel that Lattice + Qubit + Admissibility + Record
do not select a nonzero first-order kinetic law. I rebuilt its load-bearing
algebra natively and exactly (§6): it holds.

Second headline, and the one that changes how this campaign must be run: **the
entire staggered-Dirac forcing lane is `unaudited` on the live ledger** (41 of
46 rows I checked), while the notes cross-cite each other in prose as
"retained". I measured this: **44 prose/ledger contradictions across 14 distinct
claim ids in this lane alone** (§5). The lane reads as a closed derivation and
is, on the ledger, an unaudited stack of mutually-flattering source proposals.

---

## 1. Surfaces read (mandatory framework refresher)

- `docs/MINIMAL_AXIOMS_2026-06-29.md` — the four-axiom memo, in full through
  §"Open Gates Outside The Axioms".
- `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` — full.
- `docs/audit/data/axiom_premise_nodes.json` — full.
- Source note of every approved primitive invoked below. The registry lists
  exactly four canonical premise nodes:
  `minimal_axioms`, `scale_reference_primitive`, `kinetic_isotropy_primitive`,
  `realized_state_primitive` (`axiom_premise_nodes.json`, `canonical_ids`).
  **None supplies an action, a measure, or any dynamics** — see §2.
- `docs/AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md` — full
  (43 lines).
- ~30 lane notes read in full or in relevant part; 142 staggered/Kähler notes
  materialized from `origin/main` for grepping.

---

## 2. The premise surface supplies no action — verbatim

`MINIMAL_AXIOMS_2026-06-29.md:105-111`:

> Admissibility is not a dynamics axiom. It determines availability by a
> nearest-neighbor rule: for each site, the available possibilities are
> determined by, and vary with, the nearest-neighbor conditions. It does not
> choose a Hamiltonian or transfer operator, supply transition probabilities or
> weights, **select a scalar or nonzero kinetic branch, assert a Dirac-square
> carrier**, define a time metric, or provide a record-production process or
> physical persistence dynamics.

`MINIMAL_AXIOMS_2026-06-29.md:114-118`:

> A realized kinetic branch, if proposed, is downstream content: it needs a
> retained derivation or bridge, or an approved-primitive registry update,
> before audit rows may use it as load-bearing content. The four axioms are
> compatible with such later content, but do not include it.

`MINIMAL_AXIOMS_2026-06-29.md:170` lists, among gates explicitly **outside**
axiom content:

> - source/action and physical-observable identification;

`PRIMITIVE_REGISTRY_CHECK.md:15-17`:

> Do not grant more than the primitive source note declares. Any dimensionless
> quantity, selector, weighting rule, normalization rule, probability rule,
> readout bridge, **dynamics, source/action**, or empirical match remains
> separate unless independently derived.

The three non-axiom primitives each disclaim dynamics in their own registry
entries: `kinetic_isotropy_primitive` "does not supply an absolute scale,
spacing-ratio theorem, **dynamics**, Lorentz-closure theorem, … selector";
`realized_state_primitive` "does not supply a state, state-selection rule,
measure, typicality or genericity assumption, weighting …";
`scale_reference_primitive` grants "a units conversion only".

**Consequence.** The obligation cannot mean "from the four axioms alone", and
it cannot mean "from axioms plus approved primitives" either — that surface is
closed against dynamics by construction. This is not a gap to be filled by
cleverness; it is a declared boundary of the premise surface.

---

## 3. (a) The forcing-lane map — forces / supplies / LIVE ledger status

Status column is `effective_status` read from
`docs/audit/data/ledger/<xx>/<claim_id>.json` on `origin/main`. **Not** from
note prose (§5 shows why that matters).

### 3.1 The spine

| # | claim id | FORCES | SUPPLIES | LIVE status |
|---|---|---|---|---|
| 1 | `staggered_dirac_substep1_grassmann_forcing_bridge_narrow_theorem_note_2026-05-16` | Within a declared **two-candidate** surface {Grassmann, *free* boson}: free boson excluded by `dim ℵ₀ ≠ 2`; single-pair Grassmann is the unique survivor and carries the Berezin `det(M)` readout | The two-candidate surface itself. Explicitly **not** statistics forcing | `unaudited` |
| 2 | `staggered_dirac_substep1_statistics_agnostic_no_forcing_note_2026-05-25` | **NO-GO**: hard-core boson has per-site dim 2 and generates the *same* ungraded algebra `M_{2^{|Λ|}}(ℂ)`; dimension + ungraded-algebra data cannot select fermions | — (it is the refutation) | `unaudited` |
| 3 | `staggered_dirac_substep1_jw_bridge_narrow_theorem_note_2026-05-17` | A JW string *constructs* cross-site CAR | Uniqueness — explicitly disclaimed | `unaudited` |
| 4 | `staggered_dirac_kinetic_class_forcing_narrow_theorem_note_2026-06-10` | Given the licensed bilinear surface: covariance collapses the kinetic family to **exactly two** flux classes `{K0,K1}`; P-SD discharged as a theorem on the `K1` branch | The licensed surface (adjacency-licensed, charge-conserving, NN bilinear). The `K1`-vs-`K0` **bit** (B-BIT) is *not* forced | `unaudited` |
| 5 | `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` | Given `K1`: on simply connected `Z³`, solutions form **exactly one** local gauge class = the KS representative | "the **supplied** local kinetic-scalarization surface" (P-KIN + P-SD) | `unaudited` |
| 6 | `staggered_dirac_minimal_surface_kinetic_corner_nonforcing_no_go_note_2026-07-10` | **NO-GO**: the four axioms do not select a nonzero first-order kinetic law or the 8-corner zero set. Explicit four-axiom countermodel | — (it is the refutation) | `unaudited` |
| 7 | `staggered_dirac_substep2_kahler_dirac_equivalence_narrow_theorem_note_2026-05-17` | Algebraic KD form-complex equivalence, *given* substep-1 + substep-3 | The Grassmann carrier and species count | `unaudited` |
| 8 | `staggered_dirac_substep3_bz_corner_hamming_orbit_narrow_theorem_note_2026-05-17` | Corner/Hamming orbit structure | the kinetic kernel | **`audited_conditional`** (terminal) |
| 9 | `staggered_dirac_substep4_labeling_no_go_note_2026-05-17` | **NO-GO**: species labeling not derivable from the minimal baseline | — | `unaudited` |
| 10 | `staggered_dirac_realization_gate_note_2026-05-03` | Bounded synthesis *given* premise table Π | Π: statistics, kinetic/P-FLUX, boundary holonomy, labeling | `unaudited` |

### 3.2 The one remaining kinetic bit (P-FLUX = `K1` vs `K0`)

| claim id | content | LIVE status |
|---|---|---|
| `p_flux_selection_from_matter_content_narrow_no_go_note_2026-06-10` | NO-GO: matter-content battery satisfied by **both** branches | `unaudited` |
| `p_flux_point_zero_set_from_retained_rows_narrow_no_go_note_2026-06-10` | NO-GO | `unaudited` |
| `p_flux_finite_species_density_from_determinant_matsubara_surface_narrow_no_go_note_2026-06-10` | NO-GO | `unaudited` |
| `p_flux_selection_via_fsb_k_and_z_certificate_conditional_theorem_note_2026-06-11` | Conditional: selects `φ=−1` **given** FSB-K + (Z) certificate | `unaudited` |
| `axiom_first_fermionic_stefan_boltzmann_narrow_theorem_note_2026-05-26` (FSB-K leg) | — | `unaudited` |
| `staggered_kernel_satisfies_z_point_cone_certificate_narrow_theorem_note_2026-06-11` ((Z) leg) | — | `unaudited` |

Three no-gos against deriving the bit; one conditional theorem for it, whose
**scope note asserts** "As of 2026-06-14 FSB-K is `retained_bounded` and the (Z)
certificate is `retained`". Both legs are `unaudited` on the live ledger.

### 3.3 The only rows in the lane carrying a live status

Of 46 lane rows checked, exactly five are not `unaudited`:

| claim id | status |
|---|---|
| `staggered_dirac_substep3_bz_corner_hamming_orbit_narrow_theorem_note_2026-05-17` | `audited_conditional` |
| `staggered_dirac_substep4_ac_lambda_simultaneous_diagonalization_bridge_narrow_theorem_note_2026-05-17` | `retained` |
| `staggered_dirac_chirality_parity_bridge_narrow_theorem_note_2026-06-06` | `retained_bounded` |
| `staggered_os0_supplied_action_ks_blocking_four_taste_module_narrow_theorem_note_2026-07-11` | `retained_bounded` |
| `spin_statistics_berezin_determinant_narrow_theorem_note_2026-05-10` | `retained_bounded` |

**Trap on the fourth.** It is the only retained row whose *name* contains
"SUPPLIED_ACTION", and it has been rewritten to carry no physics. Its own header
(`STAGGERED_OS0_SUPPLIED_ACTION_KS_BLOCKING_FOUR_TASTE_MODULE_NARROW_THEOREM_NOTE_2026-07-11.md:11-14`):

> **Legacy identity:** the stable file path and claim id are preserved for graph
> continuity. Their physical terms are **identity-only; they do not state the
> content or hypotheses of the theorem below.**

and `:17-19`: "This is an exact theorem about a defined finite periodic
difference operator. The signs, shifts, block map, and rephasing are
**definitions, not conclusions about a physical action**." Nobody should cite
this row as landed action content.

---

## 4. (b) How far up does forcing actually go — the four questions

### Q1. Is the GRASSMANN / anticommuting character forced? **NO — supplied.**

The note that carries the "Grassmann forcing bridge" name disclaims forcing in
its own claim scope,
`STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md:24-27`:

> This is collapse **within the two-candidate surface only**: it is NOT a
> statistics-forcing theorem — the hard-core-boson frame ties with (G) on every
> readout checked here, and the statistics-selection input (S2/FS) remains open
> (§8).

and `:496-505`:

> **(B-stat) Exhaustiveness of the two-candidate surface.** The collapse (D5)
> compares the single-pair Grassmann candidate against the free boson only. …
> the hard-core-boson frame … also has per-site dimension `2` and generates the
> same ungraded operator algebra `M_{2^{|Λ|}}(ℂ)`; dimension and ungraded
> operator-algebra data cannot distinguish it from the fermionic frame.
> Therefore "the matter sector IS Grassmann" (statistics forcing) does **not**
> follow from this note.

The independent no-go states the same conclusion positively,
`STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md:74-80`:

> **Conclusion (the no-go).** Substep 1 is a **compatibility, not a forcing**.
> … The Grassmann content remains an **admission candidate** (a statistics
> selection), not a theorem derived here from the baseline alone.

The two candidate closers are both dead ends on the live ledger:
`axiom_first_spin_statistics_theorem_note_2026-04-29` is `unaudited`, and the
Grassmann note itself records (`:449-450`) that "FS is not registered as an
approved primitive" — confirmed against `axiom_premise_nodes.json`, which lists
four nodes and no statistics primitive.

### Q2. Is the FIRST-ORDER (Dirac-type) form forced? **NO — supplied.**

`STAGGERED_DIRAC_MINIMAL_SURFACE_KINETIC_CORNER_NONFORCING_NO_GO_NOTE_2026-07-10.md:239-244`:

> **Theorem (minimal-surface kinetic/corner non-forcing).** Lattice, Qubit,
> Admissibility, and Record do not select a nonzero first-order staggered
> kinetic law or the associated eight-corner Bloch-symbol zero set. This remains
> true after additionally asking for a nonzero, Hermitian, number-conserving,
> nearest-neighbor, translation-invariant, and proper-cubic-invariant physical
> matter law.

The countermodel is the qubit-exchange interaction `Φ_{x,y} = I − SWAP_{x,y}`,
whose one-particle generator is the cubic graph Laplacian with Bloch symbol
`4 Σ_μ sin²(k_μ/2)` — **one** corner zero, not eight. Its N1 route table
(`:286-293`) records six independent attacks all failing, including the two
approved primitives: kinetic isotropy is marked `RULED OUT BY PRIOR` because
"the linked primitive explicitly supplies no dynamics, selector, or
Lorentz-closure theorem".

This is the single most important sentence in the whole lane, `:12-14`:

> The plus/minus plaquette-flux split and finite wrap holonomy are additional
> sharpened choices **after a kinetic surface is supplied.**

### Q3. Is the specific STAGGERED PHASE structure forced? **Forced up to one supplied bit — and only on a supplied surface.**

This is the one place real forcing happens, and it is genuinely sharp. Given
the licensed surface, symmetry does almost all the work
(`STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md:7-23`):

> covariance under the lattice automorphisms … collapses the kinetic family to
> EXACTLY TWO frame classes on simply connected regions: `K0` = uniform
> plaquette flux `+1` … and `K1` = uniform plaquette flux `−1` (representative
> the Kawamoto-Smit sign system `η⁰`) … The final selection `K1` vs `K0` (one
> bit; the kinetic-order bit) is **NOT forced** by the specified constraint set:
> `K0` is the computed countermodel (boundary B-BIT).

and, given `K1`, the KS class is unique
(`STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md:8-19`) — but
note that note's own first six words:

> **Claim scope:** On the **supplied** local kinetic-scalarization surface — the
> naive-Dirac kinetic form on nearest-neighbor `Z³` links (premise P-KIN)
> together with a site-local unitary scalarization hypothesis (premise P-SD) …
> This is bounded forcing of the Kawamoto-Smit gauge class under the declared
> local premises …, **not an unconditional derivation of the kinetic class
> itself from Lattice + Quantum alone.**

So the honest reduction is: **P-KIN's infinite-dimensional content is reduced to
exactly one bit** — a real and quotable achievement — but the bit is not
derived, and the surface it lives on is not derived either.

### Q4. Is the MASS term forced? **Not forced — and never attempted.**

It is *excluded from the surface by definition*.
`STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md:114`,
boundary B-S3:

> "Kinetic" = the edge-supported quadratic sector; on-site bilinears (**mass** /
> chemical potential) and quartic interactions are separate sectors

The realization gate's premise table Π (`:195-201`) has four rows — statistics,
kinetic/P-FLUX, boundary holonomy, labeling — and **no mass row at all**. No
note in the lane derives, bounds, or even scopes a matter mass term. This is a
clean hole, not a contested claim.

### Q5 (bonus). The MEASURE.

Worth separating, because it behaves differently from the action. *Conditional
on* the Grassmann carrier, the measure is essentially rigid: the same note's
(D4)/(D5) give the single-pair Berezin measure as "the **unique surviving**
matter-generator measure" with the `det(M)` partition readout. So the measure is
*more* constrained than the action — but strictly downstream of the statistics
supply, which Q1 shows is not forced. The Kähler-Dirac route is separately
silent: `KOIDE_KAHLER_DIRAC_SILENT_ON_MEASURE_NOTE_2026-05-30.md:5-6` — "This
note does not derive the Koide mass measure."

---

## 5. The prose-label trap, measured

Campaign rule (2) said not to lean on prose status labels. In this lane that is
not a precaution, it is load-bearing. I diffed every prose status label attached
to a lane claim id against the live shard (script:
`scratchpad/prose_vs_ledger.py`).

**44 contradictions, 14 distinct claim ids.** The pattern is *mutual*:

| note | line | prose says | LIVE ledger |
|---|---|---|---|
| `..._SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md` | 32 | `retained_bounded` | `unaudited` |
| `..._SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md` | 37 | `retained_pending_chain` | `unaudited` |
| `..._SUBSTEP1_GRASSMANN_FORCING_BRIDGE_...2026-05-16.md` | 438, 498 | `retained` (no-go) | `unaudited` |
| `..._GRASSMANN_FORCING_THEOREM_NOTE_2026-05-07.md` | 121 | `audited_conditional` | `unaudited` |
| `..._SUBSTEP1_U4_CONDITIONAL_...2026-05-17.md` | 388 | `audited_clean` | `unaudited` |
| `..._SUBSTEP4_AC_PHI_TRACE_EQUIPARTITION_...2026-05-17.md` | 385-387 | `audited_clean` ×3 | `unaudited` |
| `..._KINETIC_CLASS_FORCING_...2026-06-10.md` | 189 | `retained` | `unaudited` |

The Grassmann note calls the no-go "retained"; the no-go calls the Grassmann
note "retained_bounded". Both are `unaudited`. A reader who trusts either
sentence concludes the substep-1 question is settled in *both* directions.

**Also a title trap.** `STAGGERED_SCHEME_FORCED_BY_ONE_QUBIT_PER_SITE_LOCALITY_NARROW_THEOREM_NOTE_2026-06-06.md`
reads as a forcing theorem. Its same-day companion
`STAGGERED_DIRAC_EXERCISE_HONEST_REASSESSMENT_NOTE_2026-06-06.md:5-8` says it
"**Corrects** the 'essentially closed / forced ×6' framing of the prior
staggered-Dirac passes (**the staggered-scheme note** and the formal audit note
from the same day)", and at `:31-45` lists three hidden admissions: fermionic
statistics, a Euclidean-signature/time-direction import, and chirality `ε(x)`.
Both notes are `unaudited`; the title survives, the retraction is one file over.

---

## 6. Native rebuild of the load-bearing algebra

The one piece of mathematics my headline actually rests on is the 2026-07-10
countermodel's symbol. I rebuilt it from scratch in sympy — exact rationals and
symbols only, **no float is ever an input**, and every quantity derived rather
than quoted. Script: `scratchpad/verify_countermodel.py`. **TOTAL: PASS=29,
FAIL=0.**

What was verified independently of the note:

- `Φ = I − SWAP` built from scratch is Hermitian, nonzero, positive
  semidefinite, number-conserving, and commutes with `U ⊗ U` for a **generic
  symbolic** `U` — so it privileges no Pauli axis. All four properties the
  theorem's hypothesis names, confirmed, not assumed.
- The one-particle symbol derived from the 6 nearest-neighbour hops equals
  `6 − 2(cos k₁+cos k₂+cos k₃) = 2Σ_μ(1−cos k_μ) = 4Σ_μ sin²(k_μ/2)` — all three
  forms of the note's eq. (2) shown equal symbolically.
- At each of the 8 corners `{0,π}³` the symbol equals exactly `4h` with `h` the
  Hamming weight (checked corner by corner: 0, 4, 4, 8, 4, 8, 8, 12).
  **Exactly one** corner is null, and it is the origin.
- The first-order staggered comparator `Σ_μ sin²(k_μ)` vanishes at **all eight**
  corners.
- Therefore 1 ≠ 8: the countermodel is not the staggered kernel, so no universal
  selection claim can hold. **The no-go's algebra is sound.**
- Separately, using one shared plaquette functional and swapping only the `η`
  system: the KS system `η₁=1, η₂=(−1)^{x₁}, η₃=(−1)^{x₁+x₂}` has uniform
  plaquette flux `−1` on all three plane pairs, the uniform system has `+1`, and
  the two differ — the two-class `{K0,K1}` split of Q3 is real.

(I caught and removed one vacuous probe — a `True and 1 == 1` placeholder — and
replaced it with a real discriminating computation before reporting the total.)

---

## 7. (c) Where "supplied" first appears — the campaign target

**It appears at link one. There is no derived link before it.**

```
  Lattice + Qubit + Admissibility + Record  (+ 3 approved primitives)
        |
        |   <-- NOTHING DERIVED CROSSES THIS LINE
        |       axioms: ":105-111  not a dynamics axiom ... does not select a
        |                scalar or nonzero kinetic branch, assert a Dirac-square carrier"
        |       axioms: ":170      source/action ... outside axiom content"
        |       registry: ":15-17  dynamics, source/action ... remains separate"
        |       countermodel: 2026-07-10 no-go, verified natively in §6
        v
  ===== SUPPLY POINT (two independent imports, both at depth 0) =====
   (S) STATISTICS SELECTION: matter is Grassmann/fermionic, not hard-core-bosonic
       -> refuted as derivable by the 2026-05-25 no-go; FS unregistered
   (K) KINETIC SURFACE (P-KIN): the matter law is a nonzero FIRST-ORDER
       nearest-neighbor charge-conserving bilinear
       -> refuted as derivable by the 2026-07-10 no-go
        |
        v   everything below is CONDITIONAL on (S) and (K)
  covariance => exactly two flux classes {K0, K1}            [genuinely forced]
  the K1-vs-K0 bit (P-FLUX)                                  [SUPPLIED: 3 no-gos]
  given K1 => Kawamoto-Smit is the unique local gauge class  [genuinely forced]
  boundary holonomy (APBC/PBC)                               [SUPPLIED: convention]
  mass term                                                  [ABSENT: never scoped]
  species labeling                                           [SUPPLIED: no-go proves undérivable]
```

The single countermodel of the 2026-07-10 no-go defeats **(S) and (K)
simultaneously** — it is a pure qubit-exchange model with no anticommuting field
*and* no first-order law, satisfying all four axioms. So (S) and (K) are not
sequential; they are one joint supply at depth zero.

**The campaign target is therefore precisely:** *what additional datum, beyond
the four axioms and the three approved primitives, promotes the matter law from
"some covariant local qubit law" to "a first-order bilinear in an anticommuting
field"?* Everything else in the matter sector is bookkeeping on top of that
datum. Note the framework's own honest count: after that datum, only **one bit**
(P-FLUX) plus a holonomy convention plus a labeling convention remain — which is
a remarkably tight residual, and worth stating as the positive half of the
result.

---

## 8. (d) Prior-art sweep

Run against `origin/main` on my own headline conclusion, per campaign rule (1).

**Has anyone already tried to derive the action itself? No — and the repo is
explicit that nobody has.** `git grep` for "derive the physical matter action"
returns only notes *declaring they do not do it*:

- `ACPHILAMBDA_OCCUPANCY_GRAIN_RULE_CLASS_UNIVERSALITY_..._2026-07-11.md:367` —
  "This note does not derive the physical matter action or measure required to
  close that obligation, so this physical condition remains unresolved here."
- `KCPT_COUPLING_TRIPLE_BEREZIN_COUNT_BINARY_MEASURE_COLLAPSE_..._2026-07-17.md:457`
  — "derivation of the physical matter action and its measure (the criterion's
  target) | **open target**".
- `ACPHILAMBDA_RECORD_OUTCOME_ORBIT_OCCUPANCY_NON_SUPPLY_NO_GO_..._2026-07-04.md:190`
  — "does not derive the matter action that AC(i) asks for".

So conjunct 1 has genuinely never been attempted, exactly as CAMPAIGN.md says.

**But the negative is already largely landed.** Prior art *on my conclusion*:

| surface | date | what it already establishes | LIVE status |
|---|---|---|---|
| `staggered_dirac_minimal_surface_kinetic_corner_nonforcing_no_go_note_2026-07-10` | 07-10 | **Direct prior art.** Four axioms do not select a first-order kinetic law; explicit countermodel | `unaudited` |
| `staggered_dirac_substep1_statistics_agnostic_no_forcing_note_2026-05-25` | 05-25 | Statistics not forced; Grassmann is an admission candidate | `unaudited` |
| `bridge_gap_action_form_uniqueness_no_go_note_2026-05-06` | 05-06 | Sibling result for the **gauge** action: Wilson / heat-kernel / Manton all compatible; "The framework's derived action is action-form ambiguous" | `unaudited` |
| `staggered_dirac_exercise_honest_reassessment_note_2026-06-06` | 06-06 | `/exercise` run that caught the "forced ×6" over-claim; names 3 hidden admissions | `unaudited` |
| `p_flux_selection_from_matter_content_...` (+2 siblings) | 06-10 | The last remaining bit resists three independent derivation routes | `unaudited` |
| `koide_kahler_dirac_silent_on_measure_note_2026-05-30` | 05-30 | KD route derives no measure | `unaudited` |

**Abandoned/foreclosed campaigns found:** the `P-FLUX` selection programme
(three no-gos, June 2026) and the gauge-action-form programme (May 2026). Both
terminated negative. I found no abandoned campaign on the *matter* action
itself, because none was ever opened.

**This session's own lane confirms the supply from the other side.** The most
recent staggered surface on main,
`FREE_STAGGERED_D_DIMENSIONAL_TWO_STEP_MANY_BODY_TRANSFER_IDENTITY_NOTE_2026-07-20.md:192`:

> determined by a supplied kernel form*. It does not derive that form,

and `:441`: "the supplied kernel form, **which no gate can validate**." Every
RP/microcausality/transfer result this session produced sits on top of the same
depth-0 import.

---

## 9. Kill-check (campaign hard rule 1)

Is this route already foreclosed or ill-posed? **Partly foreclosed, and that is
the finding, not an obstacle.**

- The reading "derive the action from axioms alone" is **ill-posed** — §2, by
  the memo's own text.
- The reading "derive it from axioms + approved primitives" is **foreclosed** —
  the 2026-07-10 countermodel is a model of exactly that surface, and I verified
  its algebra natively (§6).
- The reading "cut a menu to a point by a selection principle" is **live but
  currently failing**: within the licensed surface the menu is already cut to
  **two** elements, and three independent no-gos say the last bit does not
  fall. RP and microcausality do not rescue it — this session's own notes
  consume the kernel as supplied rather than deriving it (§8).
- The reading "the action is irreducibly supplied" is **the best-supported
  one**, and is already ~80% written across six unaudited notes that nobody has
  composed.

I did not find a corpse to build on; I found a scattered, unaudited, mutually
mislabelled proof of the negative.

---

## 10. Non-claims

This report sets and predicts **no audit verdict**; every status above is a
transcription of a live shard field, and the pervasive `unaudited` state means
*awaiting audit*, not *refuted*. It introduces no axiom, no primitive, and no
new vocabulary. It derives no `r`, mass, coupling, or mixing angle. The §6
rebuild verifies a cited note's internal algebra; it does not promote that note.
No file in `docs/` was modified.
