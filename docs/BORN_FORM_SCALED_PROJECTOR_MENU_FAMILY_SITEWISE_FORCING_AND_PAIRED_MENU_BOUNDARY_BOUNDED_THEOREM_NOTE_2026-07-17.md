---
claim_id: born_form_scaled_projector_menu_family_sitewise_forcing_and_paired_menu_boundary_bounded_theorem_note_2026-07-17
claim_type: bounded_theorem
claim_scope: "Conditional finite-dimensional theorem at one M_2(C) site: on the scaled-projector domain (nonnegative multiples of rank-one projectors and of the identity), a menu-independent grading normalized on every finite scaled-projector partition has the unique Born trace form. The rank-one menu schemas force the directional form, while identity-multiple menus determine only the identity ray. A separate exact construction shows that the finite paired subfamily (equal-weight antipodal pairs plus identity multiples) admits non-trace gradings. This does not classify smaller sufficient families, select a physical menu family, or derive the grading and eligibility premises."
upstream_dependencies:
  - minimal_axioms
  - born_form_effect_menu_sitewise_forcing_and_product_menu_boundary_bounded_theorem_note_2026-07-17
runner: scripts/born_form_scaled_projector_menu_family_sitewise_forcing_2026_07_17.py
---

# Born Form On The Scaled-Projector Menu Family: Sitewise Forcing With No Literature Bridge Input, And The Paired-Menu Boundary

**Date:** 2026-07-17
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope:** bridge-conditional; the grading hypotheses are assumed here, not
adopted; the menu family the physical registration supplies is underived.
**Audit-status authority:** independent audit lane only. This note sets no
audit verdict and predicts none.
**Primitive status:** no primitive is approved, registered, edited, or
enlarged here. Every grading hypothesis below is conditional input only.
**Primary runner:**
[`scripts/born_form_scaled_projector_menu_family_sitewise_forcing_2026_07_17.py`](../scripts/born_form_scaled_projector_menu_family_sitewise_forcing_2026_07_17.py)
**Runner cache:**
[`logs/runner-cache/born_form_scaled_projector_menu_family_sitewise_forcing_2026_07_17.txt`](../logs/runner-cache/born_form_scaled_projector_menu_family_sitewise_forcing_2026_07_17.txt)

## Purpose

The landed parent note
[`BORN_FORM_EFFECT_MENU_SITEWISE_FORCING_AND_PRODUCT_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md`](BORN_FORM_EFFECT_MENU_SITEWISE_FORCING_AND_PRODUCT_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md)
contains two conditional results: normalization on every finite effect
partition forces the trace form, while a separate two-qubit construction
survives a joint relaxation of global orthogonal additivity and full
projective-menu eligibility. It explicitly treats the carriers, grading
domains, and eligible menu families as mathematical inputs and selects no
physical surface. The joint-relaxation result is not an H4-only, minimality,
or intermediate-family theorem.

This note studies one exactly delimited one-site family. Its proof is
self-contained; the parent is used only for comparison and for a previously
landed one-site hemisphere grading that is reproduced at the same resolution:

- **Forcing.** On the scaled-projector family — effects that are nonnegative
  multiples of one-site rank-1 projectors or of the identity — menu
  normalization plus effect-functionality already forces the Born trace form
  on that domain, at a single `M_2(C)` site, with no literature bridge
  input. The proof is a direct four-menu-schema argument (complement,
  same-direction split, axis cancellation, coins) and uses no effect with
  two distinct nonzero eigenvalues; the form-forcing runs on scaled rank-1
  menus, with coin menus used only to determine the identity ray.
- **Boundary.** The paired subfamily — menus that are disjoint unions of
  equal-weight antipodal pairs and identity multiples, the shape produced by
  classically mixing binary projective measurements without splitting or
  regrouping outcomes — does not force: the landed one-site rogue extends to
  it explicitly. A forcing family on this surface must therefore contain
  some menu outside the paired subfamily; the proof's nontrivial split
  instances and non-axis axis-cancellation instances are unpaired and
  supply them.

Thus the full finite-effect hypothesis is not needed for this conditional
one-site form theorem: scaled projectors and identity multiples suffice. On
the same mathematical surface, paired-menu normalization alone is
insufficient. No individual unpaired menu or smaller unpaired family is
proved sufficient, and no physical family is selected or registered.

## Authorities and Inputs

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) — source for
  the one-site `M_2(C)` possibility domain and the Record sentences "Only
  records are readable. A readout value is determined by record content
  alone." The axioms do not supply probabilities, weights, menus, update
  rules, or record-production processes.
- [`BORN_FORM_EFFECT_MENU_SITEWISE_FORCING_AND_PRODUCT_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md`](BORN_FORM_EFFECT_MENU_SITEWISE_FORCING_AND_PRODUCT_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md)
  — the direct comparison surface: its finite-effect theorem is stronger
  than T2's restricted-domain theorem, and its one-site lexicographic
  hemisphere grading and exact three-direction non-trace test are reproduced
  here at the same resolution. Its bonded-pair result changes both the
  carrier/additivity surface and menu eligibility, so it supplies no witness
  for the present one-site paired-menu theorem.
- `BORN_FORM_FROM_LAWFUL_GRADED_CONSTRAINT_COMPOSITE_GLEASON_BRIDGE_NOTE_2026-07-04.md`
  — non-load-bearing comparison only. Its composite carrier, full projective
  menus, and imported Gleason bridge are not used here. The path is plain
  text so this comparator is not represented as a source dependency.
- Literature comparators (never proof inputs): Wright-Weigert 2019 (a
  Gleason-type theorem for qubits from projective measurements and their
  classical mixtures — a differently delimited restricted family; a native
  translation of their exact class is a separate open increment); Busch 2003
  and Caves-Fuchs-Manne-Renes 2004 (the full effect-family pole).

## The Family

Work at one site, `A ≅ M_2(C)`, `P(n) = (1 + n·σ)/2` for unit Bloch
directions `n`. Define the scaled-projector effects

> `S = { c P(n) : c ∈ [0,1], n unit } ∪ { c 1 : c ∈ [0,1] }`,

and write `S_sharp` for the rank-1 part `{ c P(n) : c ∈ (0,1] }`. Every
element of `S` is an effect; a nonzero element determines its parameters
uniquely (`c P(n)` has eigenvalue pair `{c, 0}`, `c 1` has `{c, c}`, so `c`
and, for rank 1, `n` are recovered from the operator). A **scaled-projector
menu** is a finite family of nonzero elements of `S` summing to `1`.

**T1 (exact menu characterization).** A finite family
`{c_k P(n_k)}_k ∪ {d_j 1}_j` of nonzero scaled-projector effects is a menu
iff

> `Σ_k c_k n_k = 0` and `Σ_k c_k / 2 + Σ_j d_j = 1`.

Proof: expand in the basis `{1, σ_x, σ_y, σ_z}`; the identity component
gives the scalar condition, the Pauli components give the vector condition.
The family therefore contains, among others: every projective menu
`{P(n), P(−n)}`; every coin `{c 1, (1−c) 1}` and its refinements;
same-direction splits `{λP(n), μP(n), (1−λ−μ)P(n), P(−n)}`; the
axis-cancellation menus of T2; and three-element coplanar menus such as
`{(2/3)P(n_1), (2/3)P(n_2), (2/3)P(n_3)}` with `n_1 + n_2 + n_3 = 0`. It
does not contain any effect with two distinct nonzero eigenvalues (e.g.
`diag(1/2, 1/4)`), so it is a proper subfamily of the landed parent's
effect-partition family.

## Hypotheses

**(F1) grading exists on the scaled-projector domain.** There is
`w : S → [0,1]` with `w(0) = 0` and `w(1) = 1`; `w` is a function of the
effect alone — its value does not depend on which eligible menu embeds the
effect.

**(F2) scaled-projector menus are eligible.** For every scaled-projector
menu `{A_j}`, `Σ_j w(A_j) = 1`.

F1-F2 are restricted analogues of the landed parent's finite-effect inputs:
both the function domain and eligible partitions are restricted to `S`.
They are implied by the parent's finite-effect assumptions and they imply
normalization on bare binary projective menus, but neither converse is
asserted. Only finite menus are used; no countable clause is assumed.
Whether a physical registration supplies this family, a larger one, a
smaller one, or none is underived and is not decided here.

## Results

**T2 (forcing on the scaled-projector family, without an imported literature theorem).** Assume
F1-F2 at one site. Then there is a unique density matrix `σ` with
`w(E) = Tr(σE)` for every `E ∈ S`. The proof uses four menu schemas, all
inside `S`, and only the rank-1 schemas carry the forcing:

- **(a) Ray additivity.** Fix `n` and write `h(λ) = w(λP(n))`. For
  `λ, μ ≥ 0` with `λ + μ ≤ 1`, T1 validates the same-direction splits
  `{λP(n), μP(n), (1−λ−μ)P(n), P(−n)}` and
  `{(λ+μ)P(n), (1−λ−μ)P(n), P(−n)}` (the degenerate members with zero
  coefficient are dropped). Subtracting their normalizations gives
  `h(λ) + h(μ) = h(λ+μ)`. With `h ≥ 0` this gives monotonicity
  (`h(μ') = h(μ) + h(μ'−μ) ≥ h(μ)`), rational homogeneity by iteration, and
  the rational squeeze `q_1 h(1) ≤ h(t) ≤ q_2 h(1)` for rationals
  `q_1 < t < q_2`; hence `h(λ) = λ g(n)` for all real `λ ∈ [0,1]`, with
  `g(n) := w(P(n))`.
- **(b) Complement.** The projective menu `{P(n), P(−n)}` gives
  `g(n) + g(−n) = 1`.
- **(c) Axis cancellation.** For a unit `n` with components `n_a`
  (`a ∈ {x,y,z}`), set `L = |n_x| + |n_y| + |n_z| ∈ [1, √3]` and
  `c_0 = 2/(1+L) ∈ (0,1]`. By T1,

  > `{ c_0 P(n) } ∪ { c_0 |n_a| P(−sign(n_a) e_a) : n_a ≠ 0 }`

  is a menu: its vector part is `c_0 (n − Σ_a n_a e_a) = 0` and its scalar
  part is `c_0 (1 + L)/2 = 1`. Normalization, (a), and (b) give

  > `g(n) = (1 + L)/2 − Σ_a |n_a| g(−sign(n_a) e_a)
  >        = (1 − L)/2 + Σ_a |n_a| g(sign(n_a) e_a)
  >        = (1 + n·s)/2`,

  with `s_a := 2 g(e_a) − 1`. So `g` is affine in the Bloch direction, with
  its coefficients read off the three axis values.
- **(d) Coins.** Menus `{c 1, c' 1, (1−c−c') 1}` make `f(c) := w(c 1)`
  additive and bounded, hence `f(c) = c` by the same
  rational-homogeneity-plus-squeeze argument. Coins are not used in
  (a)-(c); they only complete the representation over the identity ray of
  `S`.
- **(e) State property and uniqueness.** `g(n) ∈ [0,1]` for all unit `n`
  forces `|s| ≤ 1` (evaluate at `n = −s/|s|` when `s ≠ 0`), so
  `σ := (1 + s·σ)/2` is a density matrix, and
  `w(cP(n)) = c g(n) = Tr(σ · cP(n))`, `w(c1) = c = Tr(σ · c1)` on all of
  `S`. Uniqueness: any representing density matrix reproduces the three
  axis values, which determine `s`.

No step uses a literature theorem, a composite, an effect outside `S`, a
projective frame-function analysis, or countable additivity. The runner
re-derives every load-bearing identity exactly, including the
axis-cancellation identity symbolically on a generic octant and on rational
witnesses in all octants and on the degenerate axis cases.

**T3 (paired-menu boundary).** Call a scaled-projector menu **paired** when
its multiset of elements is a disjoint union of equal-weight antipodal pairs
`{λP(m), λP(−m)}` and identity multiples `{d 1}` — the shape produced by
classically mixing binary projective measurements and coins without
splitting or regrouping outcomes. Then:

- **(T3a) The paired subfamily does not force.** Extend the landed parent's
  landed lexicographic hemisphere rogue `g` by
  `w(λP(n)) := λ g(n)`, `w(c1) := c`. On any paired menu the normalization
  sum is `Σ_i λ_i [g(m_i) + g(−m_i)] + Σ_j d_j = Σ_i λ_i + Σ_j d_j = 1` by
  the complement law and T1's scalar condition, so the extension satisfies
  F1-F2 restricted to paired menus; and it is no trace form, by the landed
  exact three-direction contradiction, reused at the same resolution. The
  same computation is witnessed a second time, self-contained in this note,
  by the smooth assignment `g_c(n) = (1 + n_z^3)/2`: it obeys the
  complement law and stays in `[0,1]`, its axis values force the unique
  trace-form candidate `s = (0, 0, 1)`, and at `m = (√3/2, 0, 1/2)` that
  candidate gives `3/4` while `g_c(m) = 9/16` — so the paired subfamily
  admits non-Born gradings that are not tied to the parent's hemisphere
  construction (a review-panel finding adopted here; both witnesses are
  runner-gated).
- **(T3b) Some unpaired menu is necessary.** For any eligible-menu family
  `M` contained in the paired subfamily, F1 plus normalization on `M` does
  not force the Born form: the T3a witness satisfies both. Any menu family
  on this surface whose normalization forces the Born form must therefore
  contain an unpaired menu. In the T2 proof, the nontrivial same-direction
  splits and the non-axis axis-cancellation menus (the latter have no
  antipodal pair at all for generic `n`) are the unpaired menus that carry
  this role.

T3 makes no claim about which intermediate families beyond the paired
subfamily force or fail: the scaled-projector family forces (T2), the
paired subfamily does not (T3a), and the exact boundary between them across
all intermediate families is not classified here.

**T4 (assumption-surface calibration and comparators).** The landed
finite-effect theorem uses a strictly larger domain and partition family;
T2 shows that neither the full effect algebra nor effects with two distinct
nonzero eigenvalues are needed for the present conditional one-site result.
The landed hemisphere grading and the independent cubic grading both survive
on bare projective and finite paired menus, while T2 excludes them once every
finite scaled-projector menu is eligible. This is a comparison of explicit
mathematical assumptions, not a physical-registration theorem.

The landed parent's two-qubit joint-relaxation result has a different
carrier, grading domain, additivity surface, and menu family, and supplies no
negative premise here. Wright-Weigert 2019 reaches a trace-form conclusion
for a differently delimited projective-simulable operational family with
mixture/outcome consistency. No containment between that class and `S` is
asserted; translating it into native registration language and classifying
minimal sufficient subfamilies remain open.

## No-Go Discipline Gate

The gate distinguishes two surfaces: **A**, the exact mathematical T3 claim
for finite one-site paired menus; and **B**, the open physical-registration
question behind F1-F2. Surface A is claimed only at its stated resolution.
Surface B is not declared closed.

### N1 — alternative routes

Five distinct attacks on surface A were attempted in this cycle:

| Marker and route | Attack and result |
|---|---|
| **ATTEMPTED — effect-parameter ambiguity** | Try to make `w(λP(n))` representation-dependent at zero, identity, duplicate-ray, or repeated-outcome collisions. The spectral uniqueness proved in The Family fixes every nonzero parameter; `w(0)` is fixed separately, and the runner checks the recovery identities. |
| **ATTEMPTED — scale/coin coupling** | Vary pair weights and arbitrary identity remainders to seek an extra normalization condition. T3's generic finite sum reduces every such menu to `Σ_i λ_i+Σ_j d_j=1`, exactly T1's scalar condition. |
| **ATTEMPTED — multiplicity, repeated directions, and alternative pairings** | Add any finite number of pairs and coins, repeat directions, or regroup the multiset into a different pairing. The global formula for `w` is element-wise and the normalization is a finite sum of complement identities, independent of order or pairing choice. |
| **ATTEMPTED — regularity rescue** | Require continuity or smoothness to remove the discontinuous hemisphere example. The polynomial `g_c(n)=(1+n_z^3)/2` is smooth, complement-respecting, and runner-checked. |
| **ATTEMPTED — hidden trace representative** | Fit the smooth witness to a qubit state using all three axis values, then test off axis. The axes uniquely give `s=(0,0,1)`, while the exact direction with `n_z=1/2` gives `9/16` instead of the trace value `3/4`. |

These are self-contained candidate proofs plus executable checks, not
borrowed audit verdicts. Their authority remains this reviewed source pending
the independent audit lane. Five corresponding routes were also checked for
surface B: Record/Qubit supplies the `M_2(C)` carrier but no weights;
Admissibility supplies no probability or menu-selection rule; the approved
primitive registry contains no grading/menu primitive; the landed parent
assumes rather than registers its grading domains and menus; and the
composite/literature routes add separate operational or theorem inputs.
All five are **ATTEMPTED** and leave physical registration open rather than
establishing a no-go.

### N2 — wall-independence audit

Surface A has one exact boundary: normalization on the finite paired
subfamily admits the displayed non-trace assignment. Surface B separates two
conditional inputs:

| Direction | Automatically closes the other? | Reason |
|---|---:|---|
| Derive a menu-independent grading on `S` (F1) → register and normalize every finite `S`-menu (F2) | **No** | A function on effects does not declare any physical menu eligible or normalized. |
| Register the mathematical `S`-menu family → derive a single menu-independent normalized grading (F1) | **No** | A set of alternatives does not by itself supply probabilities, noncontextuality, or values. |

F1 and F2 are therefore independent conditional inputs; neither is promoted
to axiom content.

### N3 — hidden-condition scan

| Phrase or surface | Classification |
|---|---|
| one-site `M_2(C)` | Framework carrier from `MINIMAL_AXIOMS_2026-06-29.md`; no probability content imported. |
| F1 grading/functionality | Explicit underived conditional input. |
| F2 eligibility and normalization of every finite `S`-menu | Explicit underived conditional input, independent of F1 as separated in N2. |
| Pauli/Bloch representation | Explicit finite-matrix convention and directly checked algebra. |
| "classically mixing" interpretation of paired shapes | Non-load-bearing context; no operational realizability is derived. |
| landed hemisphere grading | Prior one-site comparison reproduced here; the cubic witness makes T3 self-contained. |
| composite and literature comparisons | Non-load-bearing context; no theorem or class containment is imported. |

No measured value, physical selection, countable extension, composite
carrier, or outcome-processing closure is hidden in the proof.

### N4 — residual matching

| Cited surface | Residual there | Residual here | Match? |
|---|---|---|---:|
| Landed parent, one-site hemisphere section | Non-trace grading on binary projective menus | The same grading extended to finite paired scaled-projector menus | **Partial/yes only for the borrowed one-site restriction.** The extension is proved here. |
| Landed parent, bonded-pair joint relaxation | Non-Born grading after changing carrier, global additivity, and menu eligibility | One-site paired-menu normalization | **No.** Comparator only. |
| `BORN_FORM_FROM_LAWFUL_GRADED_CONSTRAINT_COMPOSITE_GLEASON_BRIDGE_NOTE_2026-07-04.md` | Positive composite projective closure with an imported theorem | One-site paired insufficiency / scaled-family forcing | **No.** Comparator only. |
| Wright-Weigert 2019 | Positive operational result for projective-simulable measurements with consistency assumptions | The present explicitly defined family `S` | **No containment asserted.** Comparator only. |

After nonmatches are dropped, only the parent's one-site grading is borrowed;
the cubic witness and arbitrary-paired-menu calculation are the actual
self-contained support for T3.

### N5 — resolution and rhetoric audit

| Resolution | Tested? | Disposition |
|---|---:|---|
| one `M_2(C)` site, finite paired menus exactly as defined | **Yes** | T3 applies. |
| all finite scaled-projector menus at one site | **Yes** | T2 gives the opposite, positive forcing result under F1-F2. |
| arbitrary intermediate subfamilies between paired and `S` | **No** | Explicitly unclassified. |
| countable menus, multiple sites, composites, or outcome-processed projective-simulable families | **No** | Outside scope; no negative is exported. |
| physical registration of F1-F2 | **No** | Open conditional surface, not a no-go conclusion. |

The only negative phrase is therefore the narrow one-site finite paired-menu
statement established by the explicit construction.

### N6 — partial-closure paths

- Every finite scaled-projector menu closes the conditional one-site form
  problem by T2.
- Every finite effect partition closes it on the stronger landed-parent
  surface.
- The composite Gleason route is a different stronger route with an imported
  theorem and explicit composite assumptions.
- Operational mixture/outcome consistency, as in Wright-Weigert 2019, is a
  plausible translation route, not a registered premise or a result here.
- An owner-approved future registration could supply F1, F2, or both; the
  current primitive registry supplies neither.

No new axiom is declared necessary, and convention/registration routes remain
live.

### N7 — strongest steelman

**Hostile steelman.** The paired counterexample may be an artifact of treating
outcome labels, weights, and decompositions as unique. Operationally
equivalent mixtures can be split or regrouped, and consistency across those
representations may impose precisely the missing additivity; Wright-Weigert's
projective-simulable construction is the strongest comparator for that
objection. Unless the assignment is well defined across every representation
allowed by the stated paired family, the claimed boundary is illusory.

The narrow mathematical claim survives: nonzero spectral parameters are
unique, `w` is defined globally on `S`, and the arbitrary finite paired sum
does not depend on outcome order, multiplicity, or pairing choice. Splitting,
regrouping, and general projective-simulable outcome processing can leave the
paired class and are not claimed to satisfy T3. The steelman therefore keeps
the physical/operational translation open but does not break the exact
finite-family theorem.

### N8 — cross-cycle echo

The closest prior mechanism is the review-narrowed landed parent. There,
broad product-menu language was repaired to a joint relaxation because
changing eligibility also changed the carrier of additivity. The same lesson
is applied here by keeping paired eligibility, full `S` eligibility,
noncontextuality, and outcome processing separate. The active review queue's
negative-claim rule is also applied: the five in-scope attacks, pairwise wall
table, hidden-condition table, residual table, resolution table, closure
paths, and hostile steelman are recorded here rather than replacing a failed
gate with boundary rhetoric.

**Gate disposition:** PASS for the narrow mathematical T3 statement; the
physical-registration surface remains open and is not a no-go.

## Non-Claims

- Does **not** claim any grading exists, on any family; F1-F2 are
  conditional input only.
- Does **not** select a menu family or grade, register or modify any
  primitive, or derive menu eligibility from the axioms.
- Does **not** claim the scaled-projector family is minimal, and does
  **not** classify intermediate families between the paired subfamily and
  `S`; the Wright-Weigert class is a comparator, not translated here.
- Does **not** extend beyond one site: composite menus, values, and record
  conditioning are outside scope, as in the landed parent's one-site
  comparison.
- Does **not** set an audit verdict; landing is not ratification, and
  independent audit remains required.

## Verification

The primary runner exactly checks the listed algebraic reductions and
representative witnesses (sympy, rational/symbolic arithmetic, single
process, one-site `M_2` objects only); the arbitrary-finite-family and
all-real-parameter steps are carried by the written proof, with the runner
gating their load-bearing identities:
the parameter-recovery lemma for `S`; the T1 characterization identity
symbolically and on witnesses (projective, coin, split, axis-cancellation
in a generic octant, all-octant rationals, degenerate axis cases, a
coplanar three-element menu) with a non-menu rejector; the ray-additivity
and coin eliminations as formal linear algebra; the monotonicity identity,
fixed rational-bracket proof scaffolding, and a non-monotone rejector; the
all-real density step itself is proof-only; the axis-cancellation affinity elimination to
`g(n) = (1 + n·s)/2`; the state bound `|s| ≤ 1` and the representation and
uniqueness identities on symbolic scaled effects; the paired-menu
normalization of the rogue extension as a formal identity under the
complement law; the unpairedness of the split and axis schemas; the reused
exact three-direction refutation with an affine control; and needle checks
pinning the axiom memo boundary, the landed parent's actual conditional
surface, and the source claim labels. The cache records SHA-256 fingerprints
for the runner, source note, landed parent dependency, and axiom memo so
dependency drift cannot remain false-green.

Measured runner total after final verification:
`TOTAL: PASS=60 FAIL=0`.
