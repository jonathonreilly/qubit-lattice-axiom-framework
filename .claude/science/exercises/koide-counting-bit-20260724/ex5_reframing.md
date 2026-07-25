# EXERCISE FIVE — Reframing the counting bit across the repo's own boundaries

**Date:** 2026-07-24 · **Sector:** EX5 (reframing) · **Base:** `origin/main` @ `1652deb63b`
**Status:** exercise report. No commits, no PRs, no audit verdicts, no axiom or
primitive proposals. Every "assumption" label below is for the purpose of this
exercise only.

## 0. Framework refresher — surfaces actually read

| surface | read | what I took from it |
|---|---|---|
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | full | Lattice/Qubit/Admissibility/Record wording; the **Qualification**; "A state is a configuration of records"; "A law privileges no states"; Record additivity is **over finite pairwise-disjoint records** with `I(empty)=0`; central-sector decomposition, weighting, within-sector data, formation rules explicitly **not** supplied |
| `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` | full | the three approved primitives and the "do not grant more than the source note declares" clause |
| `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md` | full | units conversion only; zero dimensionless content (not load-bearing here) |
| `docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md` | full | pointwise evaluation only; the **counterfactual test**; **State-Contingency Register item 4 names `r` itself** |
| `docs/audit/data/axiom_premise_nodes.json` | full | the four canonical ids; the `minimal_axioms` note string, which explicitly excludes **"law-level dependence on an unfixed choice"** |
| `docs/ai_methodology/skills/review-loop/SKILL.md` | premise/axiom sections | axiom-vs-approved-primitive boundary; Record guardrails; "within-sector data" and "central-sector decomposition" listed as non-supplied |
| `docs/repo/CONTROLLED_VOCABULARY.md` | not needed | **I propose no new repo name.** Everything below is stated in existing vocabulary |

Lane surfaces read (landed, `origin/main`): `CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md`,
`GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05.md`, `KOIDE_REAL_REP_BLOCK_COUNT_PERMITTED_NOT_FORCED_NOTE_2026-05-30.md`,
`KCPT_ORBIT_COUNT_IS_THE_PARTITION_NOT_THE_WEIGHT_...NOTE_2026-06-06.md`,
`KOIDE_R_HALF_POLARIZATION_SELECTOR_TESTED_STATIC_READOUT_NO_GO_NOTE_2026-06-08.md` (the 8-lens row),
`ACPHILAMBDA_RECORD_OUTCOME_ORBIT_OCCUPANCY_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md`,
`AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md`,
`KCPT_COUPLING_TRIPLE_BEREZIN_COUNT_BINARY_MEASURE_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-07-17.md`,
`KCPT_AMBIENT_LATTICE_SYMMETRY_KERNEL_ISOLATION_AVERAGED_COMPLEX_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-07-19.md`.

Scratchpad runners (not repo files; reproduce with `python3 <path>`):
- `…/scratchpad/ex5_check.py` — **46 exact gates, PASS=46 FAIL=0** (sympy, no floats).
- `…/scratchpad/ex5_kernel_cone.py` — **K1–K5**, exact integer, rebuilds the landed `4^3` staggered kernel from the construction.

Full paths:
`/private/tmp/claude-502/-Users-jonBridger-Toy-Physics--claude-worktrees-quirky-wiles-92e3b4/66008b76-8d97-42b5-b1e1-4e60c09bb2e9/scratchpad/ex5_check.py`
`/private/tmp/claude-502/-Users-jonBridger-Toy-Physics--claude-worktrees-quirky-wiles-92e3b4/66008b76-8d97-42b5-b1e1-4e60c09bb2e9/scratchpad/ex5_kernel_cone.py`

---

## 1. Headline

**The counting bit is not one bit, and the cone is not one free parameter. They
are the same freedom counted twice, and on the framework's own landed lattice
carrier the continuous half of it is not free at all — it is forced flat.**

Exactly (gate C1):

```
r  =  (g_0 / g_1)  ×  (mu_d / mu_s)
```

where `(g_0, g_1)` is the point on the C_3-invariant form cone and
`(mu_s, mu_d)` is the slot/graining multiplicity of the singlet and doublet
isotypes. Only the **product** is `r`. The repo's two presentations pin
different halves of it and each calls its own half "the residual":

- `GENERATION_WEIGHT_DIAL_STRUCTURE` and the counting-bit synthesis silently pin
  the Gram at the HS point `diag(3,6,6)` (`g_0/g_1 = 1/2`) and vary the slot rule
  → the residual looks like **one discrete bit** `mu_d/mu_s ∈ {1,2}`.
- `KOIDE_REAL_REP_BLOCK_COUNT_PERMITTED_NOT_FORCED` derives the **2-parameter
  cone** `diag(g00,g11,g11)` with `g00:g11` free, implicitly holding the slot
  rule fixed → the residual looks like **one continuous parameter**.

Gate C6 exhibits the collision as an exact degeneracy:
`(HS Gram, per-block slots)` and `(flat Gram, per-mode slots)` are **different
horn labels with the same `r`**. This is why the same object `diag(3,6,6)` is
read as `r = 1/2` in the counting-bit synthesis ("equal HS energy per block,
`3a^2 = 6|b|^2`") and as "manifestly the `(1,2)` weighting", i.e. `r = 1`, in
`KOIDE_REAL_REP…` item 5. Both readings are internally correct; the object
`diag(3,6,6)` **alone does not determine `r`**. Naming the residual "one
counting bit" is therefore a presentation artifact: it is a bit only after the
Gram is fixed by fiat to a point of the very cone the sibling note says is free.

Then (gates K1–K5, exact integer, on the framework's own landed carrier):

**On the landed `4^3` staggered corner-wave kernel `C^8`, the space of symmetric
bilinear forms invariant under the induced ambient lattice symmetry group
(order 96, rebuilt from the construction) is exactly ONE-dimensional and is
spanned by the identity — the flat point.** There is no cone at ambient-covariant
level. Combined with `r = (g_0/g_1)(mu_d/mu_s)` and `g_0 = g_1`, the surviving
freedom is only `mu_d/mu_s ∈ {1,2}`, i.e. `r ∈ {1, 2}`; and `r = 2` gives
`Q = 5/3`, outside the Koide range. So the ambient-covariant reading points at
**`r = 1`, `Q = 1`** — the value that *refutes* the charged-lepton target — and
`r = 1/2` survives only by restricting covariance to a subgroup that is **not** a
lattice symmetry of the generation block (gate K2: the block-preserving subgroup
has order 4; gate K3: it does **not** contain the cyclic 3-shift of the three
generation labels).

This is not adopting a horn. It is the observation that the framework's own
covariance clause, applied to its own landed carrier, leaves **no** cone freedom,
and that the repo's two-horn picture is downstream of an unfixed reduction of the
covariance group.

---

## 2. (a) PRE-RECORD vs RECORDED — Record additivity is r-blind by jurisdiction, not by countermodel

### 2.1 What the landed no-go actually tested (and why it is the wrong direction)

`ACPHILAMBDA_RECORD_OUTCOME_ORBIT_OCCUPANCY_NON_SUPPLY_NO_GO_NOTE_2026-07-04`
builds two content-determined, finitely additive, `I(empty)=0` readouts with
`F_R = 2 F_C` and concludes Record does not select the determinant power.

That witness moves **both** exponents by the same factor 2. By the identity of
§1 it is **exactly r-neutral** (gate H4). The landed no-go therefore tests the
one direction in which the answer cannot matter for `r`. Nobody has pointed
additivity at the direction that does.

### 2.2 Pointing it at the right direction (countermodel, gates H1–H3)

Take a record model, let each record's content be `singlet-locked` or
`doublet-locked`, and define
`I_w(C) = Σ_{records in C} w(content)` for `w_1 = (1,1)` and `w_2 = (1,2)`.
Both laws are content-determined, both are additive on every pairwise-disjoint
union, both give `I(empty)=0`, both use the same formula in every state, and
they differ **precisely** in `mu_d/mu_s`, hence in `r` (`1/2` vs `1`).
Additivity is silent.

### 2.3 The structural reason (this is the real content)

Additivity is a law about the **join of disjoint records**. The counting bit is a
law about the **alternative menu of a single record**. The Record axiom's own
clauses keep these apart:

> "A site never carries more than one record."
> "When present, a record locks **exactly one** admissible local possibility."

The singlet and the doublet are not two disjoint records that can be joined —
they are two isotypes of the alternative space available to **one** locking
event on one carrier. `⊔` never operates between them. Finite additivity
constrains `I` on the join-semilattice of disjoint collections and imposes
**nothing** on the single-record content map `content ↦ value`, which is where
`(mu_s, mu_d)` lives. Hence:

> **Additivity jurisdiction no-go (proposed, unaudited).** Record's finite
> additivity clause has no jurisdiction over the isotype weight ratio, because
> the ratio is a property of the alternatives of one record and additivity is a
> property of joins of distinct records. This holds for *every* additive
> content-determined readout, not merely the two in the landed countermodel.

This is strictly stronger than the landed non-entailment result and it is
pointed at the r-controlling direction.

### 2.4 The one clause that *does* bite — and the exact bridge it needs

The no-go inverts into a **positive conditional**: additivity acquires
jurisdiction over `r` **iff** the isotype multiplicity is realized as a
multiplicity of pairwise-disjoint **records**. Under that identification, the
one-record-per-site clause forces `mu_d = mu_s = 1` (one carrier, one record),
i.e. the orbit-count horn `r = 1/2`. The missing step is exactly the one the
Berezin note already flags in its R5b:

> "no framework clause identifies occupancy slots with Grassmann generators"

**Named obligation (pre-record vs recorded):** *slot–record identification.* Is
an occupancy slot a record, or a pre-record alternative? Record answers the
first case decisively (one per site) and is silent in the second. The counting
bit is thus a **pre-record structure** in the current framing, and only becomes
Record-constrained if the slot-record bridge is derived.

**First artifact (a):** a lemma + runner
`record_additivity_jurisdiction_isotype_weight_no_go` that (i) formalizes
`I` as a finitely additive content-determined function on the finite Boolean
algebra of disjoint record collections; (ii) proves that the restriction map to
single-record contents is *surjective onto all weight assignments*, so no
additivity constraint survives; (iii) exhibits the H1–H3 countermodel pair as
the r-controlling witness; (iv) states the converse conditional above. This is
a ~60-line exact runner; every gate is finite combinatorics.

---

## 3. (b) SELECTOR vs DIAL — the dial housing is a misfiling, and the obligation as written is the *right* obligation

`REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11` §"Informative State-Contingency
Register", item 4, houses `r` as realized-state data:

> "**Per-sector registered weight patterns** (e.g. the charged-lepton block
> weight `r`) — registered patterns of the realized state … dial settings
> (`r = 0, 1/2, 1`) are sector data, never forced."

Apply the primitive's **own** counterfactual test — "a value that would change
had another law-admissible state been realized is registered data". Three
independent checks say `r` fails that test:

1. **Readout is law, not state.** Record: "a readout value is determined by
   record content alone". That is a function `content ↦ value`; `(g_0,g_1)` and
   `(mu_s,mu_d)` are parameters *of that function*. Whatever the state supplies,
   the map is law-level. `minimal_axioms`' own registry string excludes
   "law-level dependence on an unfixed choice" from what is supplied.
2. **The sector-spread argument.** The register itself says different sectors sit
   at different dial settings. Within **one** realized state there is one world;
   a quantity taking three values simultaneously is not a value the state
   supplies — it is a *function of sector label*, i.e. within-sector law data.
3. **The derivations do not read `r` off any state.** Every landed derivation
   (`GENERATION_WEIGHT_DIAL_STRUCTURE` Step 3; the section-tie endpoint
   arithmetic; the counting-bit synthesis table) obtains `r` by imposing a
   **balance/graining law** with weights. Nothing anywhere evaluates `(a,b)` at a
   supplied realized state.

**Finding (b1).** Register item 4 is a category misfiling. `r` is not
state-contingent data; it is an **unfixed law-level choice**, which is exactly
what the axiom node declines to supply and what the realized-state primitive
explicitly declines to house ("supplies the slot, never the content").

**Finding (b2).** The consequence is *worse*, not better, for the lane. Housing
`r` as realized-state data reads as "the framework awaits a measurement". The
correct status is "the framework's readout **law** is underdetermined". Under
the honest status, every `r`-dependent number — including `Q = 2/3` — is
conditional on an unfixed law-level choice, not registered data.

**Finding (b3).** Therefore the obligation as written in
`AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md` ("a closing
theorem must derive…") is **the right obligation** and the dial framing does not
dissolve it. The dial framing *mis-routes* it into a registry that by its own
text cannot hold it. (Separately: see §6, the obligation's *closure criterion*
is stated in an r-neutral direction and needs repair.)

**Decisive falsifier / first artifact (b):** `realized_state_home_disambiguation`
— a runner that (i) fixes a finite family of law-admissible states of the toy
record model; (ii) computes `r` at each under the *state* reading
(`r = |b|^2/a^2` of the realized operator) and under the *law* reading (`r`
forced by the graining law); (iii) gates constancy across the family. If `r` is
constant, it is not registered data by the primitive's own test → item 4 must be
withdrawn and the derivation obligation stands. If `r` varies, then `Q = 2/3` is
measured input, the "reduces to one counting bit" framing is not a reduction of a
prediction, and the lane must say so. **Either outcome is a landable negative.**

---

## 4. (c) DYNAMICS vs KINEMATICS — a closed pincer on the current foundation

- **Kinematic side.** `KOIDE_R_HALF_POLARIZATION_SELECTOR…NO_GO_2026-06-08` tested
  8 static selection-principle lenses: 0 of 8 survived. The just-completed FS
  computation adds that the Frobenius–Schur indicator is constant `(+1,0,0)`
  across the cone. §7 below explains *why* this had to happen and generalizes it
  to **all** representation-theoretic invariants, closing the kinematic side as a
  class rather than as an enumeration.
- **Dynamical side.** `MINIMAL_AXIOMS_2026-06-29` §"Relation To Dynamics":
  Admissibility "does not choose a Hamiltonian or transfer operator, supply
  transition probabilities or weights, select a scalar or nonzero kinetic
  branch … or provide a record-production process". No axiom supplies dynamics.

So a dynamical selector is unavailable *by construction* and a kinematic
representation-theoretic selector is unavailable *by §7*. The intersection is
empty on the current foundation.

**The one axiom-supplied object that escapes the pincer is the Admissibility
menu.** Admissibility does supply, per site, a *set*: "for each site, the
available possibilities are determined by, and vary with, the nearest-neighbor
conditions". A set has a cardinality; a cardinality resolved by isotype is
exactly `(mu_s, mu_d)`. This is the only place in the four axioms where a
**count** is supplied rather than posited, and it is the axiom-side anchor of the
"cell menu" leg (which §6 shows is one of the only two r-controlling legs).

**Named object (c):** *isotype-resolved admissibility menu multiplicity*
`mu(isotype) = |A(x; neighbours) ∩ isotype|`, where `A` is the per-site available-
possibility set supplied by the Admissibility axiom.
**Tool:** the isotype decomposition of the menu under the generation action;
`rho = mu_d/mu_s`.
**First artifact (c):** a runner over the repo's existing concrete rule surfaces
(`EXTENSIONAL_NEAREST_NEIGHBOR_RULE_DEEP_PROBE_2026-07-13.md`,
`CONDITION_ALPHABET_IDENTIFICATION_…_2026-07-04.md`,
`EMPTY_STATE_BOOTSTRAP_ALL_OPEN_AVAILABILITY_ORBIT_DICHOTOMY_…_2026-07-04.md`)
that enumerates `A(x)` for the instantiated rule, decomposes it under the
generation action, and reports `rho`. **Honest caveat:** the Admissibility axiom
names *one fixed* rule but does not specify it; if no landed instantiation
resolves the generation isotypes, this route reports **empty** and that is the
finding.

---

## 5. (d) CENTRAL-SECTOR vs WITHIN-SECTOR — the repo has *not* placed it consistently, and the covariance group is the crux

### 5.1 The inconsistency

`MINIMAL_AXIOMS` and the review-loop premise list name **both** "central-sector
decomposition" **and** "within-sector data" as non-supplied. The lane places the
bit in both:

- `KCPT_ORBIT_COUNT_IS_THE_PARTITION_NOT_THE_WEIGHT…2026-06-06` proves, and
  titles, that the K/CPT **orbit count delivers the partition, not the weight**,
  and that the orbit count is **r-invariant** ("Explicit `r=1/2` and `r=1` states
  have identical orbit cardinality (= 2)").
- The 2026-07-16/17 KCPT lane nevertheless carries **"one occupancy slot per
  K-orbit versus one slot per channel atom"** as the r-controlling binary.

Both can be true only under a careful distinction the lane does not make: orbit
*cardinality* is r-invariant (it is a property of the partition), while a
*measure on the orbit set* is r-controlling (it is a weight). The 06-06 note's
own phrase for the error is "converts a cardinality into a per-sector weight".
The 07-16/17 lane re-imports the same object under the "slot" name. **This is a
live within-lane inconsistency** and it should be reconciled before any horn work
continues.

### 5.2 A carrier mismatch under the same heading (gates A6–A9)

Two different operator classes are in play and they are not the same carrier:

| class | eigenvalues | K-orbit structure | where used |
|---|---|---|---|
| Hermitian circulant `Y = aI + bC + b̄C^2` | **all three real**; the two doublet eigenvalues are two *independent* reals, `lam_1 - lam_2 = 2√3 b_i` (gates A6, A7) | no conjugate pair to fuse | where `r = |b|^2/a^2` and `Q` are *defined* |
| entrywise-real `W = aI + bC + cC^2` | `lam_0` real, `lam_2 = conj(lam_1)` (gate A8) | genuine 2-element K-orbit | where `det3 = lam_0·|lam_1|^2` and the whole count binary live |

They intersect exactly at `b_i = 0`, where the doublet **degenerates**
(gate A9). So the "count the K-orbit once" prescription is well-posed only on the
degenerate slice; off it, on the class where `r` actually lives, there is no
conjugate pair to count once. `KOIDE_REAL_REP…2026-05-30` item 3 says exactly
this ("the fusion that motivated the route is inapplicable to the retained
operator class"); the 2026-07 lane did not reconcile with it.

### 5.3 The crux: which group must the weight form be covariant under? (gates G1–G12, K1–K5)

The cone is the set of forms invariant under **left multiplication by `C`** on
`R[C_3]` ≅ the three generation directions. Computed dimensions of the invariant
symmetric-form space on that 3-space:

| group imposed | dim of invariant forms | consequence |
|---|---|---|
| `C_3` about (111) alone | **2** (G1, G5) | the cone; `r` free |
| `C_3` + the antilinear/inversion reflection `Θ = diag(1,1,-1)` | **2** (G2) | no change — matches the landed `Θ`-residual-zero result |
| full (111)-**line** stabiliser `D_3 ⊂ O` (adds the 2-fold about (1,-1,0)) | **2** (G6, G7) | still no change |
| `C_3` + any **odd** axis relabelling realised properly (`(x y)` composed with `z → -z`, det `= +1`) | **1** (G8, G9) | **collapse** |
| full proper cubic group `O` on the carrier | **1** (G4) | **collapse**, by Schur — the vector rep `T_1` is irreducible |

And the two named points, located inside the carrier picture `G = αI + βJ`:

- **flat point** `diag(1,1,1)` ⟺ `β = 0` — the lattice/Euclidean adjacency metric (G10);
- **HS point** `diag(3,6,6)` ⟺ `G = 6I − J`, i.e. **off-diagonal `g_xy = −1` between distinct lattice axes** (G11, G12).

So `r = 1/2` requires the readout form to correlate *distinct lattice axes* with
weight `−1`; the axiom-supplied lattice metric is the flat point.

**The landed-carrier test (K1–K5).** Rebuilding the framework's own `4^3`
staggered corner-wave carrier from its construction (`D2` from the `eta` phases,
`V8` from the corner subsets):

- `|G| = 96` induced kernel symmetry group — reproduces the landed value (K1);
- the subgroup preserving the **hw=1 generation block** has order **4** (K2) and
  does **not** contain the cyclic 3-shift of the three generation labels (K3) —
  the staggered `eta` convention breaks it, and the landed note independently
  records that the `G`-orbit of one hw=1 vector spans the whole 8-dim kernel;
- **the space of `G`-invariant symmetric forms on the full 8-dim kernel is
  exactly 1-dimensional, spanned by the identity** (K4, K5).

This matches, on the symmetric-form side, the landed
`KCPT_AMBIENT_LATTICE_SYMMETRY…2026-07-19` result that "Ambient invariance
together with K-reality forces the norm form", `a_c · I_8`.

**Finding (d).** The counting bit has been *placed* as a within-sector weight on
a supplied central-sector decomposition. On the framework's own supplied
covariance (ambient lattice symmetry), there **is no** within-sector weight
freedom: the invariant form is unique up to scale and flat. The 2-parameter cone
is an artifact of restricting covariance to a subgroup that (i) is the stabiliser
of a chosen body diagonal, and (ii) on the landed carrier is not even a
block-preserving lattice symmetry. **The counting bit is downstream of an
underived covariance-group reduction, not independent of it.**

---

## 6. (e) Re-deriving the four-way equivalence — two legs control `r`, two do not

The reading is exact: write the readout as `Σ_channels mu_c · log lam_c`; the
exponent of a channel *is* its slot multiplicity; `r = (g_0/g_1)(mu_d/mu_s)`, so a
leg controls `r` **iff it changes `rho = mu_d/mu_s`**. Holding the Gram at HS:

| leg | horn 1 `(mu_s, mu_d)` | horn 2 | `rho` | verdict |
|---|---|---|---|---|
| **L1 orbit-vs-atom slot** — one slot per K-orbit vs one per channel atom | `(1,1)` | `(1,2)` | `1 → 2` | **CONTROLS `r`** (`1/2 → 1`) |
| **L2 determinant grain** — `det_C` vs `det_R = |det_C|^2` | `(1,2)` | `(2,4)` | `2 → 2` | **r-NEUTRAL** |
| **L3 cell menu** — `3a^2 = ε, 6|b|^2 = ε` vs `6|b|^2 = 2ε` | `(1,1)` | `(1,2)` | `1 → 2` | **CONTROLS `r`** |
| **L4 generator count** — 6 generators (`det3`) vs 12 (`det3^2`) | `(1,2)` | `(2,4)` | `2 → 2` | **r-NEUTRAL** |

Gates D-L1…D-L4, D5, D6, D7, D8. The landed Berezin note already computes L4's
neutrality in its own T2.3 ("r-neutral doubling … the singlet exponent and the
doublet exponent double together"), and is careful to call T3 a *declared
reading*, never an equivalence. The exercise's finding is that **L2 is neutral
for the same reason** and that the two neutral legs are equivalent to each other,
the two controlling legs are equivalent to each other, and the two groups are
**not** equivalent to one another. The four-way equivalence is **2 + 2**.

### 6.1 The mechanism behind the conflation

On the entrywise-real locus `lam_0` is real, so "multiply by the conjugate"
means two different things that look identical:

- multiply by `conj(lam_1)` — touches the **doublet only**: `rho: 1 → 2`. Controls `r`.
- multiply by `conj(det3)` — touches **everything**, and because `lam_0` is real
  the singlet exponent also increments: `rho: 2 → 2`. Neutral.

**K-fixedness of the singlet channel is exactly what makes the two doublings look
alike and exactly what makes them different.**

### 6.2 Direct consequence — the landed closure criterion is stated in the r-neutral direction

`AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md`:

> "A closing theorem must derive the physical matter action and its measure, then
> distinguish the count-once `det_C`/holomorphic realization from the count-twice
> `|det_C|^2`/realified realization…"

That is leg **L2**, exponents `(1,2)` vs `(2,4)`. **Discharging the obligation
exactly as written would not select `r`.** The criterion needs repair: the
r-controlling statement is "does the readout run over the channel **set** (3
atoms) or the **quotient set** (2 K-orbits)", not "one power or two".

### 6.3 Is there a third canonical count? No (gates E1–E4)

For the Z/2-set of channels `X` (`|X| = 3`, `|X^K| = 1`):
- Burnside: `|X/K| = (|X| + |X^K|)/2 = 2` — the orbit measure `(1,1)`;
- groupoid/stack cardinality `Σ_orbits 1/|stab| = |X|/|K| = 3/2` — per isotype
  `(1/2, 1)`, whose `rho = 2` is **identical** to the atom measure's. Gate E3:
  **the stacky measure supplies no third horn.**

So the binary is exactly "coarse orbit measure vs stabilizer-weighted measure",
and gate E4 shows the two differ **precisely by the K-fixed count** `|X^K|`.

### 6.4 "Counting" is the wrong metaphor

There is one real number `r`, presented as a product of a continuous cone
coordinate and a discrete slot ratio, neither of which is separately observable.
The right description is **a choice of measure on the orbit groupoid of the K
action on the channel set, together with a choice of metric on the carrier** —
and the two choices are not independent (gate C6). "One counting bit" understates
the freedom when the Gram is free, and overstates it when the Gram is pinned by
covariance (§5.3: then *no* continuous freedom remains).

---

## 7. Why every reality-type lens had to fail — a one-line generalization of the 8-lens and FS results

Along the cone `diag(g_0, g_1, g_1)` the **representation does not change**: the
cone is the space of invariant *forms* for a fixed C_3-action on a fixed space.
Therefore **every** invariant that is a function of the representation alone —
Frobenius–Schur indicator, complex/real/quaternionic type, orientation,
CPT/antiunitary type, character, dimension, and any future such invariant — is
**constant on the cone**, necessarily.

That is the structural theorem behind "0 of 8 survived" and behind the just-
computed constant `(+1,0,0)`: those were empirical exhaustions of a class that is
closed *a priori*. It also fixes the shape of any live route:

> **A selector for `r` must be a functional of the pair (representation,
> additional supplied structure `S`) where `S` is not determined by the
> representation and does vary over the cone.**

The framework supplies exactly two candidate `S`: the **lattice covariance
structure** (§5.3 — computed, and it collapses the cone to a point) and the
**Admissibility menu** (§4 — an axiom-supplied *set*, hence an axiom-supplied
count). Everything else on the foreclosed list is a representation-level object
and is covered by the theorem above.

---

## 8. Proposals — concrete object, tool, first artifact

| # | named object | tool acting on it | first artifact (what gets built first) | decisive? |
|---|---|---|---|---|
| **P1** | the **ambient-covariance requirement on the readout weight form**, applied to the landed corner-wave kernel | invariant-form dimension count under the induced order-96 group; Schur on `T_1` | promote `ex5_kernel_cone.py` into a repo runner + narrow note: "the ambient lattice symmetry leaves a one-dimensional invariant symmetric-form space on the landed kernel carrier; the C_3 cone is a subgroup-relative object; the generation block is not ambient-invariant (order-4 stabiliser, no 3-cycle)" | **YES** — either `r = 1` is forced at ambient level (a publishable negative that refutes the target inside the framework), or the bridge "weight form = ambient-invariant form" fails and the lane learns exactly which clause it needs |
| **P2** | the **product identity** `r = (g_0/g_1)(mu_d/mu_s)` and its degeneracy `(HS, per-block) ≠ (HS, per-mode) = (flat, per-block)` | exact algebra (already done: gates C1–C6) | a repair note reconciling `GENERATION_WEIGHT_DIAL_STRUCTURE` (Gram pinned, bit free) with `KOIDE_REAL_REP_BLOCK_COUNT_PERMITTED_NOT_FORCED` (bit pinned, Gram free); withdraw "reduces to one counting bit" unless the Gram pin is independently derived | **YES** — it either produces the missing Gram derivation or demotes the reduction claim |
| **P3** | the **r-neutral / r-controlling classification of the four legs**, and the misstated closure criterion | the `rho = mu_d/mu_s` functional (gates D-L1…D8) | a narrow note repairing `AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md`'s closure criterion from "det_C vs |det_C|^2" (neutral) to "channel set vs K-orbit quotient set" (controlling) | **YES** for the obligation's correctness; it does not itself select a horn |
| **P4** | **Record-additivity jurisdiction** over the single-record alternative menu | finite Boolean-algebra restriction argument + the H1–H3 countermodel | `record_additivity_jurisdiction_isotype_weight_no_go` runner and lemma (§2.4) | **YES** as a negative; plus the converse conditional (slot=record ⟹ `r = 1/2`) as a named bridge obligation |
| **P5** | the **isotype-resolved Admissibility menu multiplicity** `mu(isotype) = \|A(x; nbrs) ∩ isotype\|` | isotype decomposition of the menu; `rho` | runner over the landed rule-instantiation surfaces enumerating `A(x)` and reporting `rho` | **Possibly** — honest risk: the axiom names one fixed rule without specifying it; if no landed instantiation resolves the generation isotypes, this reports empty |
| **P6** | the **realized-state home** of `r` | the primitive's own counterfactual test | `realized_state_home_disambiguation` runner (§3) | **YES either way** — either register item 4 is withdrawn and the derivation obligation stands, or `Q = 2/3` is registered data and the lane must stop calling it a reduction |

Recommended order: **P1 → P2 → P3 → P4**. P1 is the only one that can *close* the
wall; P2/P3 are cheap repairs that stop further work being spent on legs that
cannot move `r`; P4 retires a whole boundary.

---

## 9. Honest limits — what this sector did NOT establish

1. **P1 is not a proof that `r = 1`.** It proves the invariant-form space on the
   landed kernel is 1-dimensional and flat. The bridge "the physical readout
   weight form is an ambient-invariant symmetric form on that carrier" is
   **not derived** — it is the named obligation P1 must discharge. Without it,
   K4/K5 is a strong structural indication, not a closure.
2. **The slot ratio `mu_d/mu_s` is untouched by P1.** Flat Gram plus per-block
   gives `r = 1`; flat plus per-mode gives the out-of-range `r = 2`. The
   in-range conclusion `r = 1` uses the physical range `Q ≤ 1`, which is a
   comparator constraint, not a derivation.
3. **The `4^3` carrier is one finite surface.** Whether the order-96 group and
   its 1-dimensional invariant-form space persist at other `L` is untested here.
   That is the first robustness gate P1 must add.
4. **I did not test whether a different staggering convention restores a
   block-preserving 3-cycle.** K3's negative may be convention-relative; the
   honest statement is "not block-preserving under *this* landed `eta`".
5. **P5 may be empty.** I did not verify that any landed admissibility-rule
   instantiation resolves the generation isotypes.
6. **No route on the foreclosed list is re-proposed.** P1 is a covariance-group
   argument, not a reality-type invariant; §7 explains why reality-type lenses
   were bound to fail and does not resurrect them. P4 is a Record-clause
   jurisdiction argument, not the multiplicative bridge, not the delta-pattern
   leg, and not a chirality argument.
7. **Nothing here is an audit verdict, a promotion, or a new premise.** No repo
   file was modified except this report.
