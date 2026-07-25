# Wave 2 — draft note text and runner design for the underdetermination result

**Date:** 2026-07-25. **Read against `origin/main` @ `c815a83a5f`** (fetched this
session). Every file and every ledger status below was read from `origin/main`
via `git show` / `git ls-tree`, never from the working tree.
**Role:** campaign worker. This report sets, predicts, and estimates **no audit
verdict**. It adds no axiom, primitive, or repo vocabulary. It commits nothing,
pushes nothing, opens no PR, and edits no repo surface. This file is the only
file written.

---

## 0. DECISIVE FINDING — the wave-1 "decisive witness" is ELEVEN-DAY-OLD PRIOR ART, and the prior art already carries the half that limits it

I ran the mandatory prior-art sweep on my own headline **before** drafting. The
sweep hit. The campaign's Wave-1 headline — *the Hermitian commutant of the
diagonal `u ⊗ u` action is `span{I, SWAP}`; modulo inert shift and positive
rescaling the menu is exactly two points; the two points are separated by the
reversed ground sectors* — is in the corpus **four times**, all dated
**2026-07-14**, all under `docs/work_history/repo/review_feedback/`:

| Prior-art surface (`origin/main`) | What it already states, verbatim |
|---|---|
| `QUBIT_SYMMETRY_EXCHANGE_LAW_REDUCTION_PROBE_NOTE_2026-07-14.md:21-28` | "Then Schur-Weyl duality becomes an exact simplifier. The commutant of the diagonal `SU(2)` action `U tensor U` on two qubits is the span of identity and SWAP. Hence every Hermitian pair generator has the form `h_xy = a I + b SWAP`." |
| `SINGLE_INVARIANT_ACTION_STEELMAN_ATTACK_NOTE_2026-07-14.md:155-159` | "`h_xy = a I + b SWAP_xy.` Positive time/action scaling and a genuinely global scalar shift remove `a` and one positive magnitude. **They do not remove the sign of `b`.**" |
| `RELATIONAL_QUBIT_DISAGREEMENT_CANONICAL_LAW_ESCALATION_NOTE_2026-07-14.md:67-69` | "Under common `SU(2)` frame covariance, every two-qubit pair Hamiltonian is, up to a scalar, a multiple of SWAP. Quotienting a positive clock rescaling and a scalar energy shift **leaves precisely two nonzero orientations**." |
| `QUBIT_SYMMETRY_..._2026-07-14.md:54-57`, echoed at `FULL_LAW_INVENTORY_ADVERSARIAL_REDUCTION_NOTE_2026-07-14.md:335-337` | "`+SWAP` has a one-dimensional singlet ground space, while `-SWAP` has a three-dimensional triplet ground space." / "Checking only the minimum energy does not certify this reversal." |

There are repo runners for two of them:
`scripts/qubit_symmetry_exchange_law_reduction_probe_2026_07_14.py`,
`scripts/single_invariant_action_steelman_attack_probe_2026_07_14.py`.

**None of the four carries a claim id or a ledger row.** I checked
`docs/audit/data/ledger/` directly on `origin/main`: there is no shard for any of
them, and only six `work_history.*` shards exist repo-wide (none of these). The
`QUBIT_SYMMETRY` probe states its own status at `:7-10`: **"Authority: none."**
So the content exists as corpus prose with zero premise weight — which is exactly
why composing it into a claim-carrying, runner-gated note is still worth doing,
and exactly why the note must not present any of it as new.

### The half a careless draft would drop

The same prior art already names three limitations that Wave 1 did not report,
and each of them bites the campaign's headline:

1. **The covariance reading is itself a new physical premise, and the other
   reading kills *both* branches.**
   `QUBIT_SYMMETRY_..._2026-07-14.md:42-50`: "Under **common-basis covariance**,
   the invariant algebra is the two-dimensional span of identity and SWAP …
   Under **independent onsite covariance**, the commutant is only the identity,
   so no nontrivial pair interaction survives … The current Qubit prose supplies
   neither interpretation as a dynamical law. **Promoting the exchange result
   without choosing and defending the covariance meaning would hide a new
   physical premise in a symmetry slogan.**" Repeated at
   `RELATIONAL_QUBIT_..._2026-07-14.md:171-174`.
2. **"Exactly two" is a fact about the two-site edge class only, and the class
   enlarges to a continuum at three sites.**
   `SINGLE_INVARIANT_..._2026-07-14.md:161-176`: with a centre and two equivalent
   neighbours, `H_1 = SWAP_01 + SWAP_02` and
   `H_2 = SWAP_01 SWAP_02 + SWAP_02 SWAP_01` are both Hermitian, neighbour-exchange
   invariant and common-frame invariant; the dimensionless `eta` in
   `H_eta = H_1 + eta H_2` "changes a spectral gap ratio from `2` at `eta=0` to
   `1` at `eta=1/3`. Neither clock rescaling nor energy shift changes that
   ratio." There is also an independent **chiral** invariant at `:183-189`
   (`Tr(P_X P_Y P_Z) = 1/4 ± i/4`) whose coefficient "can therefore choose either
   hand without breaking the stated proper-rotation symmetry".
3. **The "inert identity shift" is not inert when the active-edge set is
   record-conditioned.** `RELATIONAL_QUBIT_..._2026-07-14.md:190-194`: an active
   edge adds `beta N_active`, "which is not a common scalar across those
   sectors. It changes their relative phase. A record-dependent active graph
   therefore needs an exact vacuum/edge-energy convention or a superselection
   argument; **'energy shift' cannot be discarded before the domain is fixed**."

### A fourth correction, from my own N4 pass

Wave 1 and `CAMPAIGN.md:120-124` say this result fills the gap named at
`ACPHILAMBDA_RECORD_OUTCOME_ORBIT_OCCUPANCY_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md`.
I read that sentence on `origin/main` (§ Scope, at `:110-116`): "it does not
prove that two inequivalent **matter actions or Gaussian measures** exist."
The object exhibited here is a **local Hermitian interaction on a qubit edge** —
not an action, not a Gaussian measure. **The residuals do not match**, so under
N4 that citation must be dropped as evidence and retained only as context. The
note below does that, and says so in its own N4 table. This is the single most
important correction the draft makes to the campaign's framing.

### What is left that is genuinely this note's own

- The classification stated as a **quotient count with a proof that the quotient
  is what it is** (three classes `b<0`, `b=0`, `b>0`; the `b=0` class is the
  inert law), rather than as a reduction route.
- The **frame-independent separator upgraded to an invariance theorem**:
  `m_min(Φ) :=` multiplicity of the least eigenvalue is invariant under
  `Φ ↦ sΦ + c(I⊗I)` for `s > 0` **and under every unitary conjugation**, so no
  relabelling of any kind can identify the two classes. (The 3-vs-1 fact is
  prior art; the invariance statement, and the use of it to answer the
  relabelling objection, is not.) This also executes the standing instruction at
  `FULL_LAW_INVENTORY_..._2026-07-14.md:337` that "checking only the minimum
  energy does not certify this reversal".
- The **`Z^3` band-location statement for the `+SWAP` branch**. The `−SWAP`
  branch's symbol `2Σ(1−cos k_μ)` is landed twice
  (`STAGGERED_DIRAC_MINIMAL_SURFACE_KINETIC_CORNER_NONFORCING_NO_GO_NOTE_2026-07-10.md:218-228`,
  recomputed at `ONSITE_CHARGE_CONSERVING_..._2026-07-12.md:231-245` eq. (11)-(12)).
  The `+SWAP` branch's band minimum at `k = (π,π,π)` appears nowhere in the
  corpus by my sweep.
- The **bipartite-relabelling test**, which nothing in the corpus runs, and which
  is what decides whether the band-location language survives (§3, gates `G9`).
- The **composition with the landed non-forcing no-go**: `I − SWAP` is that
  note's own single witness, and it is one of exactly two admissible classes.

---

## 1. Mandatory framework refresher — surfaces read this wave

Read in full from `origin/main`, not from memory and not from the worktree:

1. `docs/MINIMAL_AXIOMS_2026-06-29.md` (all 193 lines).
2. `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (all 46 lines).
3. `docs/audit/data/axiom_premise_nodes.json` — `canonical_ids` =
   `["minimal_axioms", "scale_reference_primitive", "kinetic_isotropy_primitive",
   "realized_state_primitive"]`, plus each node's full `note` field.
4. Source note of the one approved primitive this draft names (as a *rescue
   route that fails*, never as a premise):
   `docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`. Its boundary is
   respected **exactly**: it grants the structural OS0 kinetic-form isotropy
   `c_t = c_s` and nothing else — `:29-31` "It carries no dimensionless dynamical
   content … not a new dynamics", and the registry entry adds "not an absolute
   scale, spacing-ratio theorem, **dynamics**, or downstream Lorentz theorem".
   Nothing in this draft uses it as an input; the note's `N1` row for it is
   marked `RULED OUT BY PRIOR`, matching the landed July-10 table at `:291`.
   `scale_reference_primitive` and `realized_state_primitive` are named only in
   the `N6` registry scan and are not premises anywhere.
5. `docs/ai_methodology/skills/no-go-discipline/SKILL.md` (full, for N1-N8 form).
6. `docs/AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md` (full).
7. `docs/STAGGERED_DIRAC_MINIMAL_SURFACE_KINETIC_CORNER_NONFORCING_NO_GO_NOTE_2026-07-10.md`
   (full, 437 lines) — the house-style sibling and the load-bearing prior no-go.
8. `docs/FREE_STAGGERED_D_DIMENSIONAL_TWO_STEP_MANY_BODY_TRANSFER_IDENTITY_NOTE_2026-07-20.md`
   (full, 474 lines) — the current house style for frontmatter, the N1-N8 block,
   the "no `PASS` is asserted" closing, and the ordered-label-manifest /
   absence-gate runner discipline. Its `origin/main` text differs from the
   pre-review text at `fd883a3de1`; I diffed both and drafted against the landed
   (owner-rewritten) version.
9. `docs/ONSITE_CHARGE_CONSERVING_ENDPOINT_SYMMETRIC_COMMON_HAMILTONIAN_STRICT_QCA_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-07-12.md`,
   `docs/ACPHILAMBDA_RECORD_OUTCOME_ORBIT_OCCUPANCY_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md`,
   and the four 2026-07-14 prior-art surfaces in §0.
10. `docs/audit/data/ledger/` shards on `origin/main` for every row cited
    (§1.1). **No prose status label is used anywhere in this draft.**

### 1.1 Live ledger status of every row this draft names (read from shards)

| claim id | `effective_status` | `claim_type` |
|---|---|---|
| `staggered_dirac_minimal_surface_kinetic_corner_nonforcing_no_go_note_2026-07-10` | `unaudited` | `no_go` |
| `acphilambda_record_outcome_orbit_occupancy_non_supply_no_go_note_2026-07-04` | `unaudited` | `no_go` |
| `staggered_dirac_kinetic_class_forcing_narrow_theorem_note_2026-06-10` | `unaudited` | `bounded_theorem` |
| `onsite_charge_conserving_endpoint_symmetric_common_hamiltonian_strict_qca_dichotomy_bounded_theorem_note_2026-07-12` | `unaudited` | `bounded_theorem` |
| `record_faithful_cubic_neighbor_response_classification_bounded_theorem_note_2026-07-11` | `unaudited` | `bounded_theorem` |
| `minimal_record_instrument_dilation_scalar_exchange_nonselection_bounded_theorem_note_2026-07-11` | `unaudited` | `bounded_theorem` |
| the four 2026-07-14 prior-art surfaces | **no shard exists** | — |

`unaudited` means *awaiting audit*, not *refuted*. Reported as data.

### 1.2 Native exact rebuild backing this draft

Worker script (session-local, **not** a repo runner and **not** a gate):
`…/scratchpad/verify_menu.py` — **`TOTAL: PASS=43 FAIL=0`**, sympy-exact,
no float is an input anywhere. Every constant quoted in §2 and §3 is an output of
that script, not a quotation. Two of my own gate statements were **wrong on first
run and are recorded rather than silently corrected**: (i) I asserted
`σ_b(k+π) = σ_{−b}(k)` exactly; the truth is that they differ by the
`k`-independent constant `2b(|E| − 2d)` — which is what makes the relabelling
objection real and is now §3 `G9a`; (ii) I asserted the class-preserving
site-local unitaries are "`u` a phase", which is only correct once unimodularity
is imposed — within `SU(2)` the solution set is exactly `u = ±I`.

---

## 2. (a)+(b) THE DRAFT NOTE

Proposed path:
`docs/QUBIT_EDGE_COMMON_FRAME_INVARIANT_TWO_CLASS_MATTER_LAW_NONFORCING_BOUNDED_THEOREM_NOTE_2026-07-25.md`

**`claim_type` choice, stated with its reason rather than asserted:** I propose
`bounded_theorem`, not `no_go`. The load-bearing content is an exact finite
classification **on a supplied surface**; typing it `no_go` would inflate it into
a universal negative about "the matter law" that it does not prove, since the
surface declaration is precisely what is supplied. The negative is a corollary,
and the note carries the full N1-N8 gate because of it. The audit lane may retype
it; nothing here predicts or prefers a verdict.

````markdown
---
claim_id: qubit_edge_common_frame_invariant_two_class_matter_law_nonforcing_bounded_theorem_note_2026-07-25
claim_type: bounded_theorem
claim_scope: "Two-site edge-wise Hermitian laws on the one-qubit-per-site carrier over Z^3 ONLY, under four explicitly supplied hypotheses (common-frame covariance, edge-wise two-site support, edge-uniformity with translation and proper-cubic invariance, and autonomy), and modulo the explicitly supplied equivalence generated by positive rescaling and the additive identity shift. (R1) The real vector space of Hermitian H on C^2 (x) C^2 with [H, u (x) u] = 0 for every u in SU(2) has real dimension exactly 2 and equals span_R{I (x) I, SWAP} — PRIOR ART, stated at docs/work_history/repo/review_feedback/QUBIT_SYMMETRY_EXCHANGE_LAW_REDUCTION_PROBE_NOTE_2026-07-14.md:21-28 and three sibling 2026-07-14 surfaces, none of which carries a claim id or a ledger row; rebuilt natively and exactly here, not claimed as new. (R2) Modulo the supplied equivalence Phi -> s Phi + c (I (x) I) with s > 0, the admissible set has exactly three classes b < 0, b = 0, b > 0, where b is the SWAP coefficient; the b = 0 class is the inert law (constant one-excitation band), so requiring the law to be nonzero MODULO THE INERT SHIFT leaves exactly two classes, with positive-semidefinite representatives I - SWAP and I + SWAP. The two-orientation count is PRIOR ART at RELATIONAL_QUBIT_DISAGREEMENT_CANONICAL_LAW_ESCALATION_NOTE_2026-07-14.md:67-69. (R3) DERIVED HERE: the least-eigenvalue multiplicity m_min is invariant under the supplied equivalence AND under every unitary conjugation, and m_min(I - SWAP) = 3 while m_min(I + SWAP) = 1 (spectra {0 x3, 2 x1} and {2 x3, 0 x1}); hence the two classes are distinct and no relabelling of any kind identifies them. The 3-vs-1 ground-sector reversal itself is prior art at QUBIT_SYMMETRY_..._2026-07-14.md:54-57. (R4) DERIVED HERE: -(I - SWAP) = (I + SWAP) - 2(I (x) I), so adjoining orientation reversal (s < 0) to the equivalence MERGES the two classes into one; the count 'two' is therefore exactly equivalent to treating the energy orientation as physical, and the axioms supply no time metric or orientation. (R5) DERIVED HERE for the b > 0 branch: the edge-uniform one-excitation symbol on Z^3 is sigma(k) = a|E| + b(|E| - 2d) + 2b sum_mu cos k_mu with d = 3; at (a,b) = (1,-1) it reproduces the landed 6 - 2 sum cos k = 2 sum (1 - cos k_mu) = 4 sum sin^2(k_mu/2); the separator sigma(pi,pi,pi) - sigma(0) = -12 b equals +12 on the I - SWAP branch and -12 on the I + SWAP branch, is unchanged by the shift and scales by s > 0, and the band minimum sits at k = 0 for b < 0 and at k = (pi,pi,pi) for b > 0. (R6) DERIVED HERE, and it QUALIFIES R5: the sublattice relabelling k -> k + (pi,pi,pi) carries sigma_b to sigma_{-b} up to the k-independent constant 2b(|E| - 2d), so the band-location language is RELATIVE to the supplied momentum labelling; the implementing site-local unitary does NOT act on the admissible class, since (I (x) u) SWAP (I (x) u)^dag = (u^dag (x) u) SWAP lies in span{I, SWAP} exactly for u = +-I in SU(2), and (I (x) sigma_z) SWAP (I (x) sigma_z) = (II - XX - YY + ZZ)/2 is outside the span; the claim is therefore carried by the unitary-invariant m_min of R3, not by the band location. (R7) CONSEQUENCE, at exactly this strength: on the stated supplied surface the four axioms and the three approved primitives do not determine the matter law, because both classes satisfy every property named in the landed 2026-07-10 non-forcing theorem statement and differ in a supplied-equivalence-invariant and unitary-invariant datum. NOT CLAIMED: any action, Euclidean action, Berezin or Grassmann carrier, functional-integral measure, temporal direction, transfer operator, or measure statement of any kind — the object here is a local interaction and nothing else, so the obligation's 'and its measure' half is untouched and the 2026-07-04 no-go's 'two inequivalent matter actions or Gaussian measures' sentence is NOT filled by this note (residual mismatch, recorded in N4); that the menu is two in any sense beyond the supplied two-site edge-wise class (three-site invariants already carry a shift- and scale-invariant continuous parameter; chiral, longer-range, pairing, multi-mode and record-conditioned families are all outside); that the common-frame reading is axiom content (it is a supplied physical premise, and the independent-onsite reading leaves only scalars and no interaction at all); that the identity shift is inert on a record-conditioned active-edge set; that the staggered or Kawamoto-Smit law is wrong, impossible or empirically false (it is supplied, not forced); the K0/K1 flux bit, statistics selection, species labelling, grain, r, Q, delta, any mass, mixing angle or phase; any record-formation law; sharpness; any audit verdict."
upstream_dependencies:
  - minimal_axioms
  - staggered_dirac_minimal_surface_kinetic_corner_nonforcing_no_go_note_2026-07-10
  - onsite_charge_conserving_endpoint_symmetric_common_hamiltonian_strict_qca_dichotomy_bounded_theorem_note_2026-07-12
runner: scripts/qubit_edge_common_frame_invariant_two_class_matter_law_nonforcing_2026_07_25.py
---

# Common-Frame-Invariant Qubit-Edge Matter-Law Two-Class Classification And Non-Forcing

**Date:** 2026-07-25
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope:** two-site edge-wise Hermitian laws on the one-qubit-per-site carrier
over `Z^3`, under four supplied hypotheses and one supplied equivalence; the
axioms supply no dynamics.
**Audit-status authority:** independent audit lane only. This note sets no audit
verdict and predicts none.
**Primitive status:** no primitive is approved, registered, edited, or enlarged
here. No approved primitive is a premise of any result below.
**Primary runner:**
[`scripts/qubit_edge_common_frame_invariant_two_class_matter_law_nonforcing_2026_07_25.py`](../scripts/qubit_edge_common_frame_invariant_two_class_matter_law_nonforcing_2026_07_25.py)
**Runner cache:**
[`logs/runner-cache/qubit_edge_common_frame_invariant_two_class_matter_law_nonforcing_2026_07_25.txt`](../logs/runner-cache/qubit_edge_common_frame_invariant_two_class_matter_law_nonforcing_2026_07_25.txt)

**Upstream dependencies (graph-seeding links):**
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md);
[`STAGGERED_DIRAC_MINIMAL_SURFACE_KINETIC_CORNER_NONFORCING_NO_GO_NOTE_2026-07-10.md`](STAGGERED_DIRAC_MINIMAL_SURFACE_KINETIC_CORNER_NONFORCING_NO_GO_NOTE_2026-07-10.md);
[`ONSITE_CHARGE_CONSERVING_ENDPOINT_SYMMETRIC_COMMON_HAMILTONIAN_STRICT_QCA_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-07-12.md`](ONSITE_CHARGE_CONSERVING_ENDPOINT_SYMMETRIC_COMMON_HAMILTONIAN_STRICT_QCA_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-07-12.md).
Context-only, deliberately **not** linked and therefore deliberately **not**
graph edges, because each carries no premise weight for this note:
`docs/ACPHILAMBDA_RECORD_OUTCOME_ORBIT_OCCUPANCY_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md`,
`docs/STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md`,
`docs/RECORD_FAITHFUL_CUBIC_NEIGHBOR_RESPONSE_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-11.md`,
and the four 2026-07-14 prior-art surfaces named in §1, which carry no claim id
and no ledger row and must not seed a dependency edge.

## Purpose

[`STAGGERED_DIRAC_MINIMAL_SURFACE_KINETIC_CORNER_NONFORCING_NO_GO_NOTE_2026-07-10.md`](STAGGERED_DIRAC_MINIMAL_SURFACE_KINETIC_CORNER_NONFORCING_NO_GO_NOTE_2026-07-10.md)
proves at `:239-244` that Lattice, Qubit, Admissibility and Record "do not select
a nonzero first-order staggered kinetic law or the associated eight-corner
Bloch-symbol zero set", and it does so with **one** witness, the qubit-exchange
interaction `Φ = I − SWAP` (`:197`). A single witness leaves open whether the
witness branch is itself the forced one. This note answers that: on the same
edge-wise carrier, under an explicitly named common-frame covariance hypothesis,
the admissible laws form a **two-element** set modulo a supplied equivalence, and
the landed witness is one of the two.

The complementary half is equally important and is stated first so it is not
mistaken for a discovery. **The reduction to `a I + b SWAP`, the quotient by
positive rescaling and the additive shift, the surviving datum `sign(b)`, and the
reversed ground sectors are all prior art in this repository, dated 2026-07-14**
(§1). Those surfaces carry no claim id and no ledger row; this note rebuilds
their algebra natively and exactly, composes it into a single claim-carrying
statement, and adds four things they do not contain: the invariance theorem for
the separator, the `Z^3` band location of the second branch, the
bipartite-relabelling test, and the composition with the landed no-go.

## 1. Prior art, and exactly what is and is not new

| Result | Status in this note | Where it already is |
|---|---|---|
| commutant of diagonal `SU(2)` on two qubits `= span{I, SWAP}` | **prior art**, rebuilt natively | `docs/work_history/repo/review_feedback/QUBIT_SYMMETRY_EXCHANGE_LAW_REDUCTION_PROBE_NOTE_2026-07-14.md:21-28`; `…/FULL_LAW_INVENTORY_ADVERSARIAL_REDUCTION_NOTE_2026-07-14.md:316-319`; `…/RELATIONAL_QUBIT_DISAGREEMENT_CANONICAL_LAW_ESCALATION_NOTE_2026-07-14.md:146-152` |
| positive scale + scalar shift leave exactly `sign(b)` / "precisely two nonzero orientations" | **prior art**, rebuilt natively | `…/SINGLE_INVARIANT_ACTION_STEELMAN_ATTACK_NOTE_2026-07-14.md:155-159`; `…/RELATIONAL_QUBIT_..._2026-07-14.md:67-69` |
| ground sectors reversed, `1` vs `3` dimensional | **prior art**, rebuilt natively | `…/QUBIT_SYMMETRY_..._2026-07-14.md:54-57`; `…/FULL_LAW_INVENTORY_..._2026-07-14.md:335-337` |
| the covariance reading is a supplied physical premise; the independent-onsite reading leaves only scalars | **prior art, adopted as a stated hypothesis and gated** | `…/QUBIT_SYMMETRY_..._2026-07-14.md:42-50`; `…/RELATIONAL_QUBIT_..._2026-07-14.md:171-174` |
| the invariant family enlarges to a shift/scale-invariant continuum at three sites | **prior art, adopted as a stated non-claim** | `…/SINGLE_INVARIANT_..._2026-07-14.md:161-176` |
| `Φ = I − SWAP` one-excitation symbol `2Σ(1−cos k_μ)` | **landed prior art**, rebuilt natively | [`…NONFORCING_NO_GO_NOTE_2026-07-10.md`](STAGGERED_DIRAC_MINIMAL_SURFACE_KINETIC_CORNER_NONFORCING_NO_GO_NOTE_2026-07-10.md)`:218-223`; recomputed at [`…STRICT_QCA_DICHOTOMY_..._2026-07-12.md`](ONSITE_CHARGE_CONSERVING_ENDPOINT_SYMMETRIC_COMMON_HAMILTONIAN_STRICT_QCA_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-07-12.md)`:231-245` |
| `m_min` invariant under the supplied equivalence **and** under every unitary conjugation | **new here** (R3) | — |
| orientation reversal merges the two classes | **new here** (R4) | — |
| band minimum at `k = (π,π,π)` for the `+SWAP` branch | **new here** (R5) | — |
| bipartite-relabelling test at three levels | **new here** (R6) | — |

The four 2026-07-14 surfaces carry no claim id and no ledger row and are cited as
prior art only. `QUBIT_SYMMETRY_..._2026-07-14.md:7-10` states its own status:
"Authority: none."

## 2. Hypotheses (all supplied, none derived here)

**(H1) Carrier and support.** The physical matter law is a single Hermitian
operator `Φ` on `C^2 ⊗ C^2` attached identically to every nearest-neighbour edge
of `Z^3`, the total law being the edge sum. *Supplied.* The Lattice axiom
supplies nearest-neighbour adjacency
([`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)`:37-38`); it does
not say the law is a sum of two-site edge terms, and
[`…NONFORCING_NO_GO_NOTE_2026-07-10.md`](STAGGERED_DIRAC_MINIMAL_SURFACE_KINETIC_CORNER_NONFORCING_NO_GO_NOTE_2026-07-10.md)`:200-205`
uses the same edge-wise form as a construction, not as a derived class.

**(H2) Common-frame covariance.** `[Φ, u ⊗ u] = 0` for every `u ∈ SU(2)`.
*Supplied, and load-bearing in both directions.* The Qubit axiom's "No
possibility is privileged. Possibilities are distinguished by the supplied
algebraic structure alone" (`:52-53`) is read here as a **constraint** on the
law. That is a strictly stronger use than the landed no-go makes of the same
fact, where it is a **check** that one exhibited law privileges no axis
(`:202-205`). The alternative reading — independent onsite covariance — leaves
only scalars and therefore no nontrivial pair law at all. Neither reading is
axiom content; see `N3`.

**(H3) Edge-uniformity and lattice covariance.** The same `Φ` on every edge,
invariant under translations and proper cubic rotations (`:37-38`, `:57-58`).
*Supplied* as part of the class declaration.

**(H4) Autonomy.** `Φ` is time-independent. *Supplied.* A covariant family
`Φ(t) = J(t)·SWAP` satisfies (H2)-(H3) pointwise and retains an arbitrary
function.

**(H5) Nonzero modulo the inert shift.** `Φ ∉ R·(I ⊗ I)`. *Supplied.*

**(H6) Equivalence.** `Φ ∼ sΦ + c(I ⊗ I)` with `s > 0` real and `c` real.
*Supplied*, as a units choice plus an additive energy constant. Orientation
reversal (`s < 0`) is **not** in the group; R4 computes what adjoining it does.
The shift is inert only on a fixed active-edge set; see `Non-Claims`.

No approved primitive is a premise of (H1)-(H6) or of any result. The
[`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
appears only in `N1`/`N6` as a rescue route, and its own boundary supplies only
`c_t = c_s`, not dynamics, a selector, or a Lorentz-closure theorem.

## 3. Results

**(R1) The edge menu.** The real vector space of Hermitian `H` on `C^2 ⊗ C^2`
with `[H, u ⊗ u] = 0` for all `u ∈ SU(2)` has real dimension **exactly 2** and
equals `span_R{I ⊗ I, SWAP}`. Solving the 16-real-parameter Hermitian ansatz
against the three diagonal generators `σ_a ⊗ I + I ⊗ σ_a` leaves exactly two free
real parameters, and the identification is exact: with `d3` the fourth diagonal
parameter and `r12` the real part of the `(1,2)` off-diagonal entry,
`a = d3 − r12`, `b = r12`. Prior art (§1); rebuilt.

**(R2) The quotient.** Write `Φ = a(I ⊗ I) + b·SWAP`. Under (H6) the classes are
exactly `b < 0`, `b = 0`, `b > 0`. The `b = 0` class is `R·(I ⊗ I)`, excluded by
(H5); its one-excitation band is constant. Hence

> the admissible set modulo the supplied equivalence has **exactly two elements**,
> with representatives `I − SWAP` and `I + SWAP`.

Both are Hermitian, nonzero and positive semidefinite:
`spec(I − SWAP) = {0 ×3, 2 ×1}`, `spec(I + SWAP) = {2 ×3, 0 ×1}`, and
`SWAP² = I`, `spec(SWAP) = {+1 ×3, −1 ×1}`.

**(R3) A separator invariant under the equivalence *and* under every unitary.**
Let `m_min(Φ)` be the multiplicity of the least eigenvalue. Because `s > 0` makes
`λ ↦ sλ + c` an increasing bijection, `m_min` is invariant under (H6); it is a
spectral multiplicity, so it is invariant under every unitary conjugation. Then

```text
m_min(I − SWAP) = 3,        m_min(I + SWAP) = 1.
```

Therefore the two classes are distinct, and **no relabelling of any kind — global,
site-local, or momentum-space — can identify them.** The `3`-vs-`1` reversal is
prior art; the invariance statement and this use of it are not. This also
executes the standing instruction at
`docs/work_history/repo/review_feedback/FULL_LAW_INVENTORY_ADVERSARIAL_REDUCTION_NOTE_2026-07-14.md:337`
that "checking only the minimum energy does not certify this reversal".

**(R4) The count is exactly the orientation datum.** Exactly,

```text
−(I − SWAP) = (I + SWAP) − 2(I ⊗ I).
```

So the two classes are related by orientation reversal composed with an inert
shift: adjoining `s < 0` to (H6) **merges them into one class**, and `m_min`
exchanges the roles of least and greatest eigenvalue (`3 ↦ 1`). The statement
"the menu has two elements" is therefore exactly equivalent to the statement
"the energy orientation is physical", and
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)`:168` places the
time metric outside axiom content. This is computed and stated, not hidden inside
the quotient.

**(R5) `Z^3` band location.** Let `|E|` be the edge count of a finite edge-uniform
instance and `d = 3`. Acting on the one-excitation sector, `SWAP` on an edge moves
the excitation between its endpoints and acts as the identity elsewhere, so
directly from the edge sum

```text
σ(k) = a|E| + b(|E| − 2d) + 2b Σ_μ cos k_μ.                     (1)
```

At `(a, b) = (1, −1)` the constant cancels and (1) becomes
`6 − 2Σ_μ cos k_μ = 2Σ_μ(1 − cos k_μ) = 4Σ_μ sin²(k_μ/2)`, reproducing the landed
symbol of
[`…NONFORCING_NO_GO_NOTE_2026-07-10.md`](STAGGERED_DIRAC_MINIMAL_SURFACE_KINETIC_CORNER_NONFORCING_NO_GO_NOTE_2026-07-10.md)`:218-223`
and eq. (12) of
[`…STRICT_QCA_DICHOTOMY_..._2026-07-12.md`](ONSITE_CHARGE_CONSERVING_ENDPOINT_SYMMETRIC_COMMON_HAMILTONIAN_STRICT_QCA_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-07-12.md)`:244-245`.
Define the separator `Δ := σ(π,π,π) − σ(0)`. Then

```text
Δ = −12 b ;      Δ = +12 at b = −1 ;      Δ = −12 at b = +1 ;      Δ = 0 at b = 0.
```

`Δ` is unchanged by the shift `c` and scales to `sΔ` under `s > 0`, so `sign Δ`
survives (H6). Since `Σ_μ cos k_μ ∈ [−3, 3]` with the maximum attained only at
`k ≡ 0` and the minimum only at `k ≡ (π,π,π)`, the one-excitation band minimum is
at `k = 0` for `b < 0` and at `k = (π,π,π)` for `b > 0`. The `12` is not
hard-coded: at spatial dimension `d` the separator is `−4d·b`.

**(R6) The bipartite-relabelling test — and the qualification it forces.**
Three levels, all computed:

1. **One-excitation level.** `σ_b(k + (π,π,π)) − σ_{−b}(k) = 2b(|E| − 2d)`, a
   `k`-independent constant. So the two branches have **congruent** one-excitation
   bands, and the phrase "band minimum at `k = 0` versus `k = (π,π,π)`" is
   relative to the supplied sublattice/momentum labelling. Stated plainly rather
   than glossed.
2. **Class level.** The implementing site-local unitary does not act on the
   admissible class:
   `(I ⊗ u) SWAP (I ⊗ u)^† = (u^† ⊗ u) SWAP`, which lies in `span{I, SWAP}`
   **exactly** for `u = ±I` within `SU(2)`; concretely
   `(I ⊗ σ_z) SWAP (I ⊗ σ_z) = (II − XX − YY + ZZ)/2 ∉ span{I ⊗ I, SWAP}`.
   The relabelling therefore leaves the class rather than permuting it.
3. **Invariant level.** `m_min` is a unitary invariant (R3), so the separation is
   untouched by 1. On a finite bipartite instance the same holds many-body: on the
   4-cycle, `spec(Σ_edges SWAP) = {4 ×5, 2 ×7, 0 ×3, −2 ×1}`, whose
   least-eigenvalue multiplicity `1` differs from its greatest-eigenvalue
   multiplicity `5`, so no unitary together with a positive affine map relates the
   two branches there either.

**Consequence, at exactly this strength.** Both classes satisfy every property
named in the landed theorem statement at
[`…NONFORCING_NO_GO_NOTE_2026-07-10.md`](STAGGERED_DIRAC_MINIMAL_SURFACE_KINETIC_CORNER_NONFORCING_NO_GO_NOTE_2026-07-10.md)`:239-244`
— nonzero, Hermitian, number-conserving, nearest-neighbour, translation-invariant
and proper-cubic-invariant — and they differ in a datum invariant under the
supplied equivalence and under every unitary. Therefore, **on the supplied
surface (H1)-(H6), the four axioms and the three approved primitives do not
determine the matter law.** The staggered law is not thereby wrong; it is
supplied rather than forced. The exact residual datum whose supply would cut the
menu to a point is `sign(b)`, equivalently the ground-sector degeneracy of the
edge law, equivalently the energy orientation of (R4).

## 4. No-Go Discipline Gate

- **N1 alternative-route enumeration — ATTEMPTED.** Eight routes that would
  refute the consequence by selecting one class.

  | Route | Marker | Positive attack | Result |
  |---|---|---|---|
  | strengthen the covariance demand | `ATTEMPTED` | impose independent onsite covariance `[Φ, u_x ⊗ u_y] = 0` | kills **both** branches: the commutant drops to the scalars, so no nontrivial pair law survives; gate `G4c` |
  | reflection / transfer positivity | `ATTEMPTED` | demand a positive transfer operator | `exp(−τλ) > 0` for every real `λ`, so transfer positivity follows from hermiticity alone and is symmetric in `b`; gate `G10a` |
  | microcausality / Lieb-Robinson | `ATTEMPTED` | separate by a locality budget | `‖I − SWAP‖ = ‖I + SWAP‖ = 2` and both are supported on one edge, so every norm-and-range LR budget coincides; gate `G10b` |
  | approved kinetic isotropy | `RULED OUT BY PRIOR` | use `c_t = c_s` to force the first-order branch | the linked primitive supplies no dynamics, selector, or Lorentz-closure theorem; the landed no-go scores this route the same way at `:291` |
  | Record / realized-state selection | `ATTEMPTED` | let record content or the realized state pick a branch | the landed no-go's record surface at `:186-188` is indifferent to the edge law, and both classes attach to that identical axiom reduct |
  | positive semidefiniteness / stability | `ATTEMPTED` | demand a positive interaction | both are PSD (`{0×3, 2×1}` and `{2×3, 0×1}`); gate `G5` |
  | bipartite relabelling / sublattice gauge | `ATTEMPTED` | identify the branches by `k → k + π` | acts on the band language only; does not act on the class (`u = ±I` only) and cannot move `m_min`; gates `G9a-G9d` |
  | ground-sector nondegeneracy | `ATTEMPTED` | demand a nondegenerate ground sector | this **does** separate — and that is the point: it is the named residual datum, supplied by nothing in `A_min`; gate `G6` |

  The eight occupy distinct families: covariance, positivity/transfer, locality,
  approved primitive, Record/state, operator positivity, relabelling/gauge, and
  spectral degeneracy.

- **N2 wall-coupling audit — ATTEMPTED. The walls here are COUPLED, and the note
  claims only the collapsed set.** No pairwise-independence claim is made; the
  raw six-wall list collapses to three, and even the three are not independent.

  Raw walls: `W_frame` (which covariance reading), `W_support` (edge-wise
  two-site), `W_auton` (autonomy), `W_orient` (is `s < 0` an equivalence),
  `W_shift` (is the identity shift inert), `W_action` (a local interaction is not
  an action-and-measure).

  | Pair | Does closing the first close the second? | Coupled? |
  |---|---|---|
  | `W_frame`, `W_support` | **yes, one way**: closing `W_frame` in the independent-onsite direction leaves only scalars, which makes the support question vacuous | coupled |
  | `W_frame`, `W_auton` | both are clauses of the same supplied law-class declaration; neither is answerable without the other's semantics | coupled |
  | `W_orient`, `W_shift` | **yes, both ways in effect**: both ask what the physical equivalence on local laws is, and both are settled only by the record/time semantics the axioms exclude | coupled |
  | `W_action`, everything above | `W_action` strictly contains them: an action-and-measure statement needs a temporal direction and a functional-integral measure, neither of which any of the above supplies | nested, not independent |

  **Collapsed wall set: `{W_class, W_quotient, W_action}`**, where
  `W_class = W_frame ∪ W_support ∪ W_auton` and
  `W_quotient = W_orient ∪ W_shift`. These three are themselves three faces of
  one missing object — the physical semantics of the between-record law — and the
  note does not present them as independent.

- **N3 hidden-wall scan — ATTEMPTED.** Triggers searched: "we assume", "by
  construction", "as is standard", "the framework provides", "background",
  "naturally", "obviously", "registered", "canonical".

  | Hit | Classification |
  |---|---|
  | the frame group is `SU(2)` acting by conjugation (`Aut(M_2(C))` inner) | **promoted to an explicit hypothesis (H2)**, with the stronger-than-landed use stated in §2 |
  | "edge-wise two-site" | **promoted to (H1)**; the Lattice axiom licenses adjacency, not the two-site sum |
  | "autonomous generator" | **promoted to (H4)** |
  | the one-excitation reference state and the `|E|` bookkeeping constant | non-load-bearing: `|E|` cancels in `Δ` and in (1) at `(a,b) = (1,−1)`; gate `G7c` |
  | "positive rescaling" as the units group | **promoted to (H6)**, with R4 computing the consequence of enlarging it |
  | "inert identity shift" | **promoted to (H6) and to a Non-Claim**: it is not inert on a record-conditioned active-edge set |
  | Fourier transform, spectral theorem | mathematical infrastructure; no physical selector |
  | "registered"/"canonical" | absent from every result statement; the primitive registry check was run before any wall language |

- **N4 residual matching, per citation — ATTEMPTED, and one citation is DROPPED.**

  | Witness | Witness residual | Residual used here | Match? |
  |---|---|---|---|
  | [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)`:105-118`, `:168`, `:170` | axioms choose no Hamiltonian, kinetic branch, time metric, or source/action | the non-forcing consequence and R4's orientation gap | yes |
  | [`…NONFORCING_NO_GO_NOTE_2026-07-10.md`](STAGGERED_DIRAC_MINIMAL_SURFACE_KINETIC_CORNER_NONFORCING_NO_GO_NOTE_2026-07-10.md)`:239-244` | the axioms do not select a nonzero first-order staggered kinetic law | the same property list, now shown satisfied by **two** classes | yes; this note extends its one witness to a classification |
  | [`…STRICT_QCA_DICHOTOMY_..._2026-07-12.md`](ONSITE_CHARGE_CONSERVING_ENDPOINT_SYMMETRIC_COMMON_HAMILTONIAN_STRICT_QCA_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-07-12.md)`:231-245` | strict-QCA radius dichotomy; its §5 recomputes the `I − SWAP` graph-Laplacian identification | the symbol only | yes for the symbol; its QCA dichotomy is not used |
  | `docs/ACPHILAMBDA_RECORD_OUTCOME_ORBIT_OCCUPANCY_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md:110-116` | "does not prove that two inequivalent **matter actions or Gaussian measures** exist" | two inequivalent **local interactions** | **NO — DROPPED as evidence.** This note exhibits no action and no Gaussian measure. Cited as context only; that sentence is **not** answered here |
  | `docs/STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md` | the `K1`-vs-`K0` flux bit on a licensed first-order bilinear surface | a different surface and a different residual | **no**; context only, not evidence |

  After dropping the two non-matching citations the consequence still stands: it
  rests on R1-R6 and on the axiom text, not on either dropped row.

- **N5 rhetoric and resolution audit — ATTEMPTED.**

  | Resolution | What is established | What is not claimed |
  |---|---|---|
  | per-edge operator | exact 2-dimensional commutant; exact spectra and `m_min` | nothing about laws outside `span{I, SWAP}` |
  | per-mode (one-excitation) | exact symbol (1), the separator, the band minimum, the relabelling constant | no normalizable infinite-volume eigenvector; no continuum limit |
  | per-sector (many-body) | one finite bipartite instance (4-cycle) with an asymmetric spectrum | **no** infinite-volume many-body spectral claim |
  | lattice-wide | an edge-uniform quasi-local family | no claim that the extensive sum is a bounded operator |

  "Not determined" is used only at the model-theoretic law level on the supplied
  surface. Phrases retracted in drafting and enumerated in the runner's
  `RETRACTED_PHRASES`: "the axioms determine the matter action"; "this note
  derives the matter action"; "the measure is derived"; "the first proof that two
  inequivalent matter actions exist"; "fills the gap the 2026-07-04 no-go names";
  "the menu is exactly two points" without the qualifier "on the supplied
  two-site edge-wise class"; "the staggered action is wrong"; "Status: PASS".

- **N6 partial-closure and primitive/convention scan — ATTEMPTED.** The primitive
  registry check (`docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`) was
  run before any wall language: the registry lists exactly four nodes, and each
  of `scale_reference_primitive`, `kinetic_isotropy_primitive`,
  `realized_state_primitive` disclaims dynamics, selector and source/action in its
  own source note, so none is a wall and none supplies a selector.
  Closure paths found: (i) an owner-approved covariance reading would close
  `W_frame`, but the prior art is explicit that this is **new physics, not a
  convention**; (ii) a derived spectral record-faithfulness premise would close
  the consequence — `docs/RECORD_FAITHFUL_CUBIC_NEIGHBOR_RESPONSE_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-11.md`
  (`unaudited`) states its own exclusion is "conditional on supplied spectral
  faithfulness"; (iii) an orientation convention would close `W_quotient` **by
  merging the two classes**, i.e. it would change the answer rather than confirm
  it — flagged, not adopted. No path is misclassified as requiring a new axiom.

- **N7 steelman — ATTEMPTED, and one objection is CONCEDED as unclosed.**

  > (a) *"`k → k + π` is a relabelling of the same physics, so your two branches
  > are one theory in two coordinates."* Answered: the relabelling is congruent on
  > the one-excitation band only up to a constant, and the site-local unitary that
  > implements it takes the edge law **out** of the admissible class
  > (`u = ±I` only); `m_min` is a unitary invariant and is `3` versus `1`.
  >
  > (b) *"The count `2` is an artefact of your two-site restriction, so it is a
  > property of your hypothesis, not of the framework."* **CONCEDED AND NOT
  > ANSWERED.** The repository already carries the witness: at three sites
  > `H_1 + η H_2` has a dimensionless `η` that moves a spectral gap ratio from `2`
  > to `1`, and neither clock rescaling nor energy shift removes it
  > (`docs/work_history/repo/review_feedback/SINGLE_INVARIANT_ACTION_STEELMAN_ATTACK_NOTE_2026-07-14.md:161-176`).
  > The claim is therefore scoped to the supplied class throughout, and the true
  > residual off that class is at least a one-real-parameter continuum. The
  > note's value is that it makes the two-element count on the smallest class
  > exact and gated, not that the matter-law menu is two.
  >
  > (c) *"Your quotient is chosen so the answer comes out two."* Partly correct
  > and computed: R4 shows adjoining orientation reversal merges the classes, and
  > the Non-Claims record that the shift is not inert on a record-conditioned
  > active-edge set.

- **N8 cross-cycle echo — ATTEMPTED.** Structurally similar prior walls and their
  retirement mechanisms: the `K0`/`K1` flux bit (three June-2026 `p_flux_*`
  negatives plus one conditional composer); the gauge-sector action-form
  ambiguity (`bridge_gap_action_form_uniqueness_no_go_note_2026-05-06`); the
  statistics selection (`staggered_dirac_substep1_statistics_agnostic_no_forcing_note_2026-05-25`).
  Every one is `unaudited` on the live ledger; none has been retired. The one
  mechanism that could in principle close the present consequence is the
  record-faithfulness strengthening of `N6`(ii), and it is named as a live route
  rather than dismissed. No mechanism that retired a similar wall elsewhere has
  gone untried here.

**Status: no closure is claimed and no `PASS` is asserted.** The eight items are
answered as an honesty exercise, not as a certificate. Item N7(b) is a conceded,
unclosed objection, and the N4 table drops the citation the campaign framing
leaned on. Judgement belongs to the independent audit lane.

## 5. Non-Claims

- Does **not** claim R1, R2, or the `3`-vs-`1` ground-sector reversal as new.
  All three are prior art dated 2026-07-14 (§1), rebuilt natively here.
- Does **not** claim the common-frame reading (H2) is axiom content. It is a
  supplied physical premise; under the independent-onsite reading the commutant is
  the scalars and **no** nontrivial pair interaction survives, so the hypothesis
  does not merely narrow the menu, it creates it.
- Does **not** claim the menu is two outside the supplied two-site edge-wise
  class. At three sites the invariant family already carries a shift- and
  scale-invariant continuous parameter; longer-range, pairing, multi-mode,
  chiral (`Tr(P_X P_Y P_Z) = 1/4 ± i/4`) and record-conditioned families are all
  outside the class and are not classified.
- Does **not** claim the identity shift is inert in general. On a
  record-conditioned active-edge set the scalar term contributes a relative
  sector phase, so (H6) needs a vacuum/edge-energy convention or a
  superselection argument that this note does not supply.
- Does **not** claim the two-element count is quotient-independent. Adjoining
  orientation reversal merges the classes (R4); the count is exactly the
  statement that energy orientation is physical, and the axioms supply no time
  metric.
- Does **not** claim autonomy. A covariant `Φ(t) = J(t)·SWAP` retains an
  arbitrary function; (H4) excludes it by hypothesis, not by proof.
- Does **not** make any statement about a measure. No Euclidean action, Berezin
  or Grassmann carrier, functional-integral measure, temporal direction, or
  transfer operator is constructed, consumed, or claimed. The object is a local
  interaction. The obligation's "and its measure" half is untouched.
- Does **not** fill the gap named at
  `docs/ACPHILAMBDA_RECORD_OUTCOME_ORBIT_OCCUPANCY_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md:110-116`.
  That sentence concerns two inequivalent **matter actions or Gaussian measures**;
  the residuals do not match and the citation is dropped as evidence in `N4`.
- Does **not** claim the staggered, Kawamoto-Smit, or Kähler-Dirac law is wrong,
  inconsistent, or empirically false. It is supplied rather than forced.
- Does **not** select or derive the `K0`/`K1` flux bit, fermionic statistics,
  species labelling, the occupancy grain, `r`, `Q`, `δ`, or any mass, mixing
  angle, phase, or sector weight; and does not narrow, localize, weaken, or
  discharge any registered derivation obligation.
- Does **not** supply a record-formation law. A reversible law on a fixed carrier
  cannot make a record flag strictly grow, so everything here is between-record
  content.
- Does **not** make an infinite-volume many-body spectral claim. The 4-cycle
  instance of R6(3) is a finite bipartite support instance and carries no `Z^3`
  content.
- Does **not** set, predict, or estimate an audit verdict, and grades no row.
  Every status quoted is read from `docs/audit/data/ledger/` shards on
  `origin/main` and reported as data.

## 6. Verification

Primary runner:
[`scripts/qubit_edge_common_frame_invariant_two_class_matter_law_nonforcing_2026_07_25.py`](../scripts/qubit_edge_common_frame_invariant_two_class_matter_law_nonforcing_2026_07_25.py)
— sympy-exact throughout; no float is an input and no numeric tolerance is used.
The gate sequence is enforced against an ordered label manifest, one `PASS`/`FAIL`
line per gate plus a final total, and the cached transcript is committed at the
header path at landing time.

*Gates that carry the classification.* `G1`-`G3` compute the commutant dimension
from the diagonal `su(2)` generators by solving a 16-real-parameter Hermitian
ansatz, then solve the identification with `span{I, SWAP}` exactly and confirm
the group-level commutation against a generic symbolic `SU(2)` element. `G5`-`G6`
compute the spectra, positive semidefiniteness and `m_min` of both
representatives, and verify the multiplicity invariance under `sΦ + c(I ⊗ I)`
with `s` a positive symbol and `c` a real symbol. `G7` **rebuilds** the
one-excitation symbol from the edge sum rather than quoting the Laplacian, and
gates the separator, its shift-invariance and its scaling. `G8` gates the exact
extremal argument for `Σ cos k_μ`. `G9` runs the three-level relabelling test.

*Gates that establish what does NOT separate.* `G10a` (`exp(−τλ) > 0`) and
`G10b` (equal operator norms) show that transfer positivity and every
norm-and-range locality budget are blind to `sign(b)`. These are negative gates:
they certify that a route fails, not that the classification holds.

*Support-only gates, carrying no `Z^3` content.* `G11` is the 4-cycle many-body
instance. Its labels record which finite bipartite graph it instantiates and
nothing dimensional.

*Gate-strength caveats, stated rather than glossed.* `G4` mutations are the only
evidence that the constant `2` in `G1` is not an artefact of the ansatz; they are
construction mutations, not assertion flips, and they are listed with their exact
mutated values in the runner's own header comment. The `G9a` constant
`2b(|E| − 2d)` is a symbolic residual, not a discrimination; the discriminating
content of `G9` is `G9b`-`G9d`. No gate composes the classification with any
action, measure, or transfer construction — no such object exists in this note.
`G12` is an **absence** gate on the note's live claim surface (YAML `claim_scope`
plus every body section other than the `N5` bullet that quotes the retracted
phrases historically), and `G13` binds each computed constant to the sentence in
this note that carries it, so an edit to either side fails the gate. Both were
mutation-probed in each direction.
````

---

## 3. (c) RUNNER DESIGN — exact gates, with the CONSTRUCTION mutation for each

`scripts/qubit_edge_common_frame_invariant_two_class_matter_law_nonforcing_2026_07_25.py`.
sympy only; `Rational`/`Integer`/symbols; **no float is ever an input**; no
tolerance anywhere. Every value in the "expected" column below was produced by the
native rebuild (`PASS=43 FAIL=0`, §1.2), not quoted from any note.

### 3.1 Block A — the commutant (R1)

| Gate | Computes exactly | Expected | **CONSTRUCTION mutation** (not an assertion flip) | Mutated value |
|---|---|---|---|---|
| `G1` | real dimension of `{H = H^† : [H, σ_a⊗I + I⊗σ_a] = 0, a = 1,2,3}` by `linsolve` on the 16-real-parameter Hermitian ansatz | `2` | — (mutations are `G4`) | — |
| `G2` | solve `H_sol = a(I⊗I) + b·SWAP` for `(a, b)`; assert the residual matrix is identically zero | unique: `a = d3 − r12`, `b = r12` | replace the claimed basis element `SWAP` by `SWAP + ε(σ_z⊗σ_z)` for symbolic `ε` and re-solve | no solution for `ε ≠ 0`: the identification is basis-rigid, so a wrong basis cannot pass by luck |
| `G3` | `[I⊗I, u⊗u]` and `[SWAP, u⊗u]` for a **generic symbolic** `SU(2)` element `u = [[α, β], [−β̄, ᾱ]]` | both `0` | replace `u ⊗ u` by `u ⊗ v` with an independent generic `v` | commutators no longer vanish identically — the *diagonal* action is what is load-bearing |
| `G4a` | dimension with the frame constraint **removed from the construction** | `16` | this **is** the mutation | `2 → 16`: the constraint, not the ansatz, produces the `2` |
| `G4b` | dimension with only the `σ_z` one-parameter subgroup imposed | `6` | this **is** the mutation | `2 → 6`: the *full* group is load-bearing (a partially-imposed constraint would report `6`, catching a silent subgroup bug) |
| `G4c` | dimension under **independent onsite** covariance `u ⊗ v` | `1` | this **is** the mutation, and it is also `N1` route 1 | `2 → 1`: the alternative covariance reading destroys the menu instead of narrowing it |
| `G4d` | dimension under the **conjugate** action `u ⊗ ū`, plus the identification test | dim `2`, **but not** `span{I, SWAP}` | this **is** the mutation | dimension is still `2` while the identification **fails** — so a gate that checked only "dim `== 2`" would pass on the wrong action; `G2` is what catches it |
| `G4e` | dimension on **three** tensor factors under the diagonal action | `5` | this **is** the mutation | `2 → 5`: the `2` tracks two tensor factors, not the qubit dimension |

### 3.2 Block B — the two candidates and the separator (R2, R3, R4)

| Gate | Computes exactly | Expected | **CONSTRUCTION mutation** | Mutated value |
|---|---|---|---|---|
| `G5a` | `spec(I − SWAP)`, `spec(I + SWAP)`, hermiticity, PSD, nonzero | `{0×3, 2×1}`, `{2×3, 0×1}` | build the candidate as `I − i·SWAP` (construction change, not an assertion flip) | hermiticity rejector fires; PSD undefined — confirms the Hermitian ansatz is doing work |
| `G5b` | `SWAP² = I`, `spec(SWAP) = {+1×3, −1×1}` | as stated | build `SWAP` from the wrong index convention (transpose the middle block) | `SWAP² ≠ I`; catches a mis-built exchange operator, which would silently change every downstream constant |
| `G6a` | `m_min(I − SWAP)`, `m_min(I + SWAP)` | `3`, `1` | replace `m_min` (multiplicity) by `min` (energy) in the *construction* of the invariant | both give `0` — reproducing exactly the failure mode the corpus already warns about at `FULL_LAW_INVENTORY_..._2026-07-14.md:337`; the mutation makes the separator vanish, so a "minimum energy" implementation cannot pass |
| `G6b` | `spec(sΦ + c(I⊗I))` for positive symbol `s`, real symbol `c` | `{c×3, (c+2s)×1}` and `{(c+2s)×3, c×1}`; multiplicities unchanged | rebuild with `s` declared merely `real` instead of `positive` | the least eigenvalue is no longer determined, and the multiplicity claim fails — the positivity of `s` is exposed as load-bearing rather than assumed |
| `G6c` | `m_min(−(I − SWAP))` | `1` | this **is** the orientation mutation | `3 → 1`: the invariant flips, gating R4 |
| `G6d` | `−(I − SWAP) − ((I + SWAP) − 2(I⊗I))` | zero matrix | change the shift coefficient from `2` to a symbolic `c` and solve | forces `c = 2` uniquely — the merge identity is pinned, not asserted |

### 3.3 Block C — the `Z^3` symbol and separator (R5)

| Gate | Computes exactly | Expected | **CONSTRUCTION mutation** | Mutated value |
|---|---|---|---|---|
| `G7a` | rebuild `σ(k)` from the edge sum: diagonal part `a|E| + b(|E| − 2d)`, hop part `2b Σ cos k_μ` | eq. (1) | build the diagonal part with coordination number `2d + 1` (a plausible off-by-one in the edge count at the excited site) | the `(a,b) = (1,−1)` specialization no longer cancels `|E|` and no longer equals `6 − 2Σcos k` — `G7c` fires |
| `G7b` | specialize `(a,b) = (1,−1)` and compare to `6 − 2Σcos k`, `2Σ(1−cos k_μ)`, `4Σ sin²(k_μ/2)` | all three equal | rebuild `2Σ(1−cos)` as `2Σ(1−cos(2k))` | all three identities break simultaneously — the three-form identity is a real cross-check, not a restatement |
| `G7c` | `|E|`-independence of the specialized symbol | `|E|` cancels | keep `a` symbolic instead of `1` | `|E|` survives, showing exactly which specialization removes it (documents that `|E|` is bookkeeping, per `N3`) |
| `G7d` | `Δ = σ(π,π,π) − σ(0)` | `−12b` | replace the corner `(π,π,π)` by `(π,π,0)` in the construction | `Δ = −8b`, not `−12b` — a wrong corner is caught by the constant, not by a boolean |
| `G7e` | `Δ` at `b = −1`, `b = +1`, `b = 0` | `+12`, `−12`, `0` | — (covered by `G7d`, `G7f`) | — |
| `G7f` | `Δ` under `b ↦ sb` and any `c` | `−12sb`; sign `s`-independent, `c`-independent | make the shift `c` multiply `SWAP` instead of `I⊗I` in the construction | `Δ` acquires a `c` dependence — the *inertness* of the shift is thereby gated rather than assumed |
| `G7g` | `Δ` at `d = 1, 2, 3, 4` on the rebuilt construction | `−4b, −8b, −12b, −16b` | this **is** the dimension mutation | the `12` tracks `d = 3`; a hard-coded `12` would fail at `d ≠ 3` |
| `G8` | `Σ_μ cos k_μ` at all eight corners; the exact extremal argument | `3 − 2h` for corner Hamming weight `h`; max only at `k ≡ 0`, min only at `k ≡ (π,π,π)` | evaluate on a `d`-dependent corner set built from the same rule | corner values `d − 2h`; catches a corner enumeration hard-coded to `d = 3` |

### 3.4 Block D — the bipartite-relabelling test (R6)

| Gate | Computes exactly | Expected | **CONSTRUCTION mutation** | Mutated value |
|---|---|---|---|---|
| `G9a` | `σ_b(k + (π,π,π)) − σ_{−b}(k)`, and `∂/∂k_μ` of it | `2b(|E| − 2d)`; all three derivatives `0` | shift only `k_1` by `π` instead of all three | the residual becomes `k`-dependent — the gate distinguishes a genuine sublattice relabelling from a partial one |
| `G9b` | `(I ⊗ σ_z) SWAP (I ⊗ σ_z)`; test membership in `span{I⊗I, SWAP}` by solving for `(a, b)` | `(II − XX − YY + ZZ)/2`; **no** solution | run the same test with `W = I ⊗ I` (control) | membership solution exists (`a = 0, b = 1`) — proves the gate is a real discrimination and not a always-fail |
| `G9c` | `(I ⊗ u) SWAP (I ⊗ u)^† = (u^† ⊗ u) SWAP`, then solve membership together with `\|α\|² + \|β\|² = 1` | class preserved exactly for `u = ±I` (`α = ±1`, `β = 0`, `a = 0`, `b = 1`) | drop the unimodularity constraint from the construction | the solution set becomes empty and the characterization is lost — records that unimodularity is load-bearing (this is the error my own first pass made, §1.2) |
| `G9d` | `spec(W Φ W^†)` versus `spec(Φ)` for both candidates | identical multisets | conjugate by a non-unitary invertible `W` instead | spectra change — confirms the gate is testing unitary invariance rather than trivially true equality |

### 3.5 Block E — what does NOT separate, and the finite many-body instance

| Gate | Computes exactly | Expected | **CONSTRUCTION mutation** | Mutated value |
|---|---|---|---|---|
| `G10a` | `exp(−τλ)` positivity for symbolic real `λ`, `τ > 0`, on both spectra | positive on both | let `τ` be a free real symbol | positivity is no longer decidable — exposes that the Euclidean direction is a supplied convention, matching `N1` route 2 |
| `G10b` | operator norms `‖I − SWAP‖`, `‖I + SWAP‖` and the edge support | `2`, `2`; support `1` edge each | rescale one candidate by a symbolic `s > 0` in the construction | norms differ by `s` while `m_min` does not — shows the LR-type budget is exactly the quantity that the equivalence washes out |
| `G11` | 4-cycle: `spec(Σ_edges SWAP)` by exact `charpoly` | `{4×5, 2×7, 0×3, −2×1}`; `mult(min) = 1 ≠ 5 = mult(max)` | rebuild the graph as the 4-cycle **with a chord** (non-bipartite) | spectrum changes; the label manifest records which graph was instantiated, so a silently changed fixture fails `G14` |

### 3.6 Block F — manifest and drift detection

| Gate | What it does | **CONSTRUCTION mutation** |
|---|---|---|
| `G12` | **Absence gate.** Fails if any phrase in `RETRACTED_PHRASES` (the eight enumerated in `N5`) appears anywhere on the note's live claim surface — the YAML `claim_scope` plus every body section **other than** the single `N5` bullet that quotes them historically; the exclusion window ends at the next list item or heading, so a live claim cannot be hidden by appending it after the historical text | probed in **both** directions: inject each phrase into `claim_scope` (must fail) and into the `N5` bullet (must pass) |
| `G13` | **Constant-binding drift detector.** For each load-bearing constant the runner computes — `2`, `16`, `6`, `1`, `5` (Block A); `{0×3, 2×1}`, `{2×3, 0×1}`, `3`, `1` (Block B); `−12b`, `−4d·b`, `6 − 2Σcos k` (Block C); `2b(\|E\| − 2d)`, `±I` (Block D); `{4×5, 2×7, 0×3, −2×1}` (Block E) — assert that the **computed** literal occurs in the note sentence that carries it | mutate the runner's construction (any Block A-E mutation above) and re-run: the computed literal changes and `G13` fails against the unedited note. Independently, edit the note's constant and re-run: `G13` fails against the unchanged runner. **This is the gate that makes a wrong headline constant impossible to ship**, and it is the one the reviewer's precedent (mutating a headline constant left gates passing 20/0) specifically defeats |
| `G14` | **Ordered label manifest.** A frozen ordered tuple of every gate label above; the runner asserts the executed sequence equals it exactly (length, order, spelling) | delete one gate, rename one gate, and swap two gates — each must fail; this catches the silent-drop failure mode that a bare `PASS`/`FAIL` total cannot |
| `G15` | **Prior-art needle.** Presence check that each of the six prior-art `file:line` anchors of §1 resolves on the tracked tree, and that the note's §1 table names all four 2026-07-14 surfaces | delete one row from the note's §1 table — must fail. **Explicitly not a correctness oracle**: it verifies that the prior art is cited, never that it is right |
| `G16` | **Dependency-hygiene needle.** Assert that the YAML `upstream_dependencies` list contains exactly the three claim ids that appear as markdown links in the header block, and that no `work_history/` path appears as a markdown link anywhere in the note | add a markdown link to one of the 2026-07-14 surfaces — must fail, because that would seed a dependency edge to a surface whose own text says "Authority: none" |

**Expected deterministic summary line** (to be replaced by the real total when the
runner is written; the native rebuild backing this design is `43/0`):

```text
TOTAL: PASS=<n> FAIL=0
```

---

## 4. (d) EVERY HONEST WEAKNESS THE NOTE MUST STATE

All are in the draft's `Non-Claims`; collected here so none can be lost in an edit.

1. **Not new.** R1, R2 and the `3`-vs-`1` reversal are prior art dated
   2026-07-14, in four surfaces with no claim id and no ledger row, one of which
   states "Authority: none". Two repo runners already compute the algebra.
2. **The covariance reading (H2) creates the menu rather than narrowing it.**
   Under independent onsite covariance the commutant is the scalars: no
   nontrivial pair law at all. Prior art calls promoting the result without
   defending this reading "hiding a new physical premise in a symmetry slogan".
3. **Using no-privilege as a constraint is strictly stronger than the landed
   use.** The July-10 note uses `[SWAP, U⊗U] = 0` as a *check* on one exhibited
   law; this note uses it as a *constraint* generating the class.
4. **"Exactly two" is a property of the supplied two-site edge-wise class.** At
   three sites the invariant family already carries a dimensionless `η` moving a
   gap ratio from `2` to `1`, invariant under both clock rescaling and energy
   shift. The real residual off the class is at least a one-parameter continuum,
   plus a chiral invariant that can pick either hand.
5. **The identity shift is not inert on a record-conditioned active-edge set** —
   it becomes a relative sector phase, so the quotient needs a vacuum/edge-energy
   convention or a superselection argument that is not supplied.
6. **The count is exactly the orientation datum.** `−(I − SWAP) = (I + SWAP) −
   2I`, so adjoining `s < 0` merges the classes. "Two" ⇔ "energy orientation is
   physical", and the axioms supply no time metric.
7. **The band-location language is convention-relative.** `σ_b(k+π)` and
   `σ_{−b}(k)` differ by a `k`-independent constant, so the `k = 0` versus
   `k = (π,π,π)` reading depends on the supplied sublattice/momentum labelling.
   The claim must be carried by `m_min`, not by the band location.
8. **Autonomy is assumed.** `Φ(t) = J(t)·SWAP` is equally covariant.
9. **No measure content, of any kind.** No action, Berezin/Grassmann carrier,
   functional-integral measure, temporal direction, or transfer operator. The
   obligation's "and its measure" half is untouched. (Wave 1's measure work
   supports no positive measure claim here: it found the Berezin measure rigid
   given a carrier, with the residual scalar `r`-inert — which is a reason to
   claim nothing, not a licence to claim something.)
10. **The 2026-07-04 gap is NOT filled.** That sentence is about "two
    inequivalent matter actions or Gaussian measures"; this note exhibits two
    inequivalent local interactions. Residual mismatch; citation dropped as
    evidence under N4. This directly corrects `CAMPAIGN.md:120-124`.
11. **No infinite-volume many-body claim.** The 4-cycle is a finite bipartite
    support instance with no `Z^3` content.
12. **No record-formation content.** A reversible law on a fixed carrier cannot
    make a record flag strictly grow; everything here is between-record.
13. **Nothing selected.** No flux bit, statistics, species labelling, grain, `r`,
    `Q`, `δ`, mass, mixing angle or phase; no obligation narrowed or discharged.
14. **No audit verdict**, and every status is a shard read from `origin/main`.
15. **The `bounded_theorem` typing is a proposal with a stated reason**, not a
    determination; the audit lane may retype it.

---

## 5. Handoff

- If the kill agent finds that one class dies, R4 and R6 are the two places to
  look first: a constraint that fixes energy orientation, or one that privileges a
  sublattice labelling, would do it — and either would be a *supplied* datum, so
  the result would invert into a forcing theorem **conditional on that datum**,
  not an unconditional one.
- The single highest-value follow-on is the one `N6`(ii) names: a **derived**
  spectral record-faithfulness premise would cut the menu to a point
  framework-natively. `RECORD_FAITHFUL_CUBIC_NEIGHBOR_RESPONSE_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-11.md`
  (`unaudited`) states its own exclusion is conditional on that premise being
  supplied.
- Before anything ships, someone must run `git grep` over
  `docs/work_history/repo/review_feedback/` for the headline. This wave's own
  headline was already there, four times, eleven days old — and two of the four
  limitations it records would have been dropped.
