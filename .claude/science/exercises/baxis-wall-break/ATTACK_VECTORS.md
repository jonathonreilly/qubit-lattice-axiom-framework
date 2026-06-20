# ATTACK_VECTORS — B-AXIS wall (Exercise Two: Elon-style first-principles reduction)

**Date:** 2026-06-20 • **Slice:** EXERCISE TWO of the `baxis-wall-break` exercise.
**Posture:** wall-breaking. Framework premises are treated as challengeable
assumptions for this exercise. Nothing here applies an audit verdict, adds an
axiom/primitive, or claims the wall is solved. Each vector below names the
requirement it deletes/reshapes and gives a *first small runner* — a fast finite
falsifier, in the spirit of "accelerate the feedback loop before automating."

**Refresher surfaces read:** `MINIMAL_AXIOMS_2026-06-05.md`;
`PRIMITIVE_REGISTRY_CHECK.md`; `SCALE_REFERENCE_PRIMITIVE_NOTE.md`;
`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`;
`REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`;
`docs/audit/data/axiom_premise_nodes.json` + `tier_a_admissions.json` (read-only);
`review-loop/SKILL.md`; `CONTROLLED_VOCABULARY.md`; the keystone
`AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`; the
consumer `ANOMALY_FORCES_TIME_THEOREM.md`; the unified no-go
`SINGLE_CLOCK_BAXIS_OBSTRUCTION_UNIFIED_NO_GO_NOTE_2026-06-20.md`; the route
`NO_GO_LEDGER.md`; and the three driving runners
`axiom_first_single_clock_codimension1_evolution_check.py`,
`single_clock_n5_irreducibility_factor_clock_2026_06_20.py`,
`single_clock_n2b_joint_clock_unit_check_2026_06_20.py`.

---

## Reduction frame: what does the fanout-959 chain ACTUALLY require?

The keystone is named "single-clock **codimension-1**" and is consumed by exactly
one downstream payload: `ANOMALY_FORCES_TIME_THEOREM` imports from it the upper
bound **`d_t ≤ 1`** (the *number* of time directions is at most one), which it
intersects with a computed chirality lower bound (`d_t` odd ⇒ `d_t ≥ 1`) to get
`d_t = 1`, signature (3,1). Read the consumer carefully (its own words):

- line 141: "the [anomaly] steps below constrain only the **count** `d_t`
  (parity and positivity), **not** [the label]";
- lines 123–124: "no admitted independent commuting transfer factor, so there is
  exactly **one admitted clock factor**: `d_t ≤ 1`".

So the entire load the keystone must carry downstream is a **count cap on the
number of evolution directions**. The B-AXIS premise was written as three clauses
(N2/N4/N5) bundled to support a *richer* statement — "one **labelled** axis, one
**absolute** unit, one **unique** generator" — than the consumer ever uses. This
mismatch is the reduction lever. The campaign's own "count-not-label firewall"
(unified no-go §5.3.4) records that the anomaly rule constrains the count, not the
label — but it files that fact as *a reason N4 can't be derived*. The Elon move is
to read the same fact the other way: **N4-as-axis-label is an over-specified
requirement that the target does not need; delete it and prove the count
directly.**

Three independent dials fall out of the bundle:

| clause | what it currently demands | what the target needs | reduction verdict |
|---|---|---|---|
| **N4** | a *label* (which of 4 axes) | a *count* (`d_t ≤ 1`) | **over-specified** — solve the count, drop the label (Vector A) |
| **N5** | exclude a "second clock" = any commuting factor flow of the supplied transfer | exactly one *independently-supplied* generator | **misframed** — spectral modes of one operator are not independent clocks (Vector B) |
| **N2b** | an *absolute* `1/time` unit | nothing downstream (the count uses no unit) | **inherited from a stale unit-bearing route** — the count is unit-free; the `c_t=c_s` primitive already fixes the only ratio the geometry needs (Vector C) |

The vectors below attack each dial as a separate, smaller problem, plus two
cross-cutting reframes (D, E) that change the carrier and the object.

---

## VECTOR A — Delete N4 (the label); derive the count `d_t ≤ 1` directly as a codimension statement

**Clause:** N4. **Reduction type:** *requirement stated too strongly* (a selector
problem misclassified; it is really a **counting / codimension** problem).

**Assumption challenged.** That the keystone must *select which* Euclidean axis is
time before it can say "one clock." The whole S₄/W transport apparatus exists only
because the requirement is phrased as "pick the time axis." The downstream consumer
never reads the label.

**The reduction.** The keystone already proves (S2′) that each slice
`Σ = {fixed value of the chosen coordinate} × Z³` is **codimension-1** and carries
a mutually-commuting equal-time tensor algebra. Turn this into a *label-free* count:
the supplied transfer `T̂²` is a positive Hermitian operator whose Stone generator
`H` generates **one** strongly-continuous one-parameter group `U(t)=exp(-itH)`.
The number of *independent supplied one-parameter evolution directions* is the
dimension of the supplied generator data, which is **1** (one `H`), regardless of
which lattice axis it is geometrically aligned with. The exchange symmetry `W`/S₄
that defeats N4-as-label is *irrelevant* to the count: `W` permutes which
geometric axis hosts the construction but does not create a second `H`. In other
words, **`d_t ≤ 1` is W-invariant and therefore survives exactly the transport
that kills the label.** The campaign proved `W M Wᵀ = M` and `W` transports every
anchor — but a transported single construction is *still a single construction*.

**Why this is new.** The campaign treated W-transitivity as fatal because it was
trying to fix the label. For the count, W-transitivity is *harmless* (it is an
automorphism of a structure that has exactly one transfer construction up to that
automorphism). No prior route, no NO_GO_LEDGER row, attempts to discharge the
*count* `d_t ≤ 1` while conceding the label as undefined-and-unneeded.

**Missing input to prove instead (if the count still won't close).** The honest
residual is: "how many independent positive transfer constructions does the A_min
surface supply?" The answer must be **at most one up to S₄** — i.e. the supplied
RP/SC data give a single S₄-orbit of transfer constructions, not several
inequivalent ones. That is a *finite* statement about the supplied surface, not a
label selection. (This is exactly where N5, Vector B, plugs in: "one construction
up to S₄" + "no independent commuting factor" = `d_t ≤ 1`.)

**First small runner (`baxis_count_codim_label_free_*.py`).** On the even
`(4,4,2,2)` staggered block already used by the keystone runner:
1. Build `T̂²` and its Stone generator `H`; confirm the supplied generator data is
   a single operator (the "number of supplied `H`'s" = 1) — trivial but it is the
   load-bearing object the consumer reads.
2. For each `g ∈ S₄` (the 24 axis permutations, via the existing `G_bare`
   machinery), conjugate the *whole* RP construction `g·(H, Σ, U(t))·g⁻¹` and check
   it is the *same* construction up to relabeling (resid 0) — i.e. the count of
   inequivalent constructions modulo S₄ is **1**.
3. Print `d_t_count_modS4 = 1` and assert it is invariant under all of `G_bare`.
4. **Falsifier leg:** exhibit a hypothetical surface that supplies *two*
   S₄-inequivalent transfer constructions (e.g. add a second, genuinely
   non-conjugate positive transfer) and show the count jumps to 2 — proving the
   count is a real discriminator, not a tautology.

**Stop condition.** If step 2 fails (some `g` produces a genuinely inequivalent
construction, not just a relabeling), the count route also needs the label and
Vector A is dead. If it passes, the deliverable is a label-free `d_t ≤ 1` that
makes N4 *unnecessary for the consumer* — a reframe that dissolves the clause for
its only downstream use. (It does NOT derive the label; it shows the label is not
load-bearing.)

---

## VECTOR B — Reframe N5: the "second clock" is functional calculus of ONE operator, not a second operator

**Clause:** N5. **Reduction type:** *misframed object* — a representation/algebra
confusion between the **linear span** `span{I, H}` and the **abelian algebra
generated by `H`** (its functional calculus `{f(H)}`).

**Assumption challenged.** That the per-mode flows `U_p(s) = exp(-is·n_p)` are
"independent clocks." They are not independent *operators*: on the supplied
surface `H_hat = Σ_p E(p) n_p` has **non-degenerate spectrum** (the `E(p)` are
distinct for distinct `|p|` on a generic block), so each `n_p` is a **function of
the single supplied generator**, `n_p = f_p(H_hat)`, obtainable by spectral
(Lagrange-interpolation) functional calculus. A flow `exp(-is·n_p)` is therefore
`exp(-is·f_p(H_hat))` — a **re-clocked version of the one supplied clock**, not a
new clock.

**The exact gap in the existing no-go.** The R-N5-IRR runner's `[GAUGE]` leg
(`single_clock_n5_irreducibility_factor_clock_2026_06_20.py`, lines 251–281) tests
only whether `n_0 ∈ span{I, H_hat}` — a **2-dimensional linear** test — and
correctly finds it does not (residual ≈ 0.65). But "not in the linear span of
`{I, H}`" is the wrong criterion for "is an independent clock." `H² `, `√H`,
`log H`, every spectral projector — none of these is in `span{I,H}` either, yet
none is a second clock; they are all the *same* clock read through a different
spectral function. The right algebra is the **commutant/bicommutant**: if every
candidate factor generator lies in `{H_hat}'' = ` (the abelian von Neumann algebra
generated by `H_hat`, here the algebra of all diagonal operators in `H_hat`'s
eigenbasis), then there is **no independent clock** — every "second clock" is a
function of the first. By the same `span{I,H}` logic the no-go uses, ordinary QM
with `H = Σ_n E_n |n⟩⟨n|` would have one independent clock per energy level, which
is absurd. The N5 no-go's "(L_s−1)-parameter physical-clock-admission ray" is
exactly the freedom to pick a *function* `f` of the one generator — that is a
**re-parametrization choice, not a second physical clock.**

**Why this is new.** Every N5 route in the ledger (algebraic-exclusion,
product-Stone non-uniqueness, Record-additivity, admission-firewall, R-N5-IRR)
either uses a *foreign* two-tensor-factor proxy `T_A⊗I, I⊗T_B` (two genuinely
independent supplied operators) or tests the *linear* span. **None tests whether
the per-mode factor flows lie in the functional-calculus algebra of the single
supplied `H_hat`.** The proxy is the category error: A_min supplies exactly *one*
transfer `T̂²` (the keystone's (R-RP2)/(R-SC2) supply), not two independent ones.
The `T_A⊗I, I⊗T_B` countermodel imports a second supplied operator that A_min does
not provide, then "discovers" a second clock that was inserted by hand.

**Sharpened N5 statement to prove.** *Every candidate second-clock generator that
commutes with the supplied `H_hat` and produces durable records is an element of
`{H_hat}''` (a function of `H_hat`); hence the supplied evolution is generated, up
to spectral re-parametrization, by the single one-parameter group of `H_hat`. A
genuinely independent commuting clock would require a second independently-supplied
positive transfer, which the A_min surface does not provide.* This **closes the
"second clock" question at the level the consumer needs** (one supplied generator
⇒ one clock factor ⇒ `d_t ≤ 1`), and relocates the only residual to "does A_min
supply a second independent transfer?" — answer: no (it supplies one `T̂²`).

**First small runner (`baxis_n5_functional_calculus_one_clock_*.py`).** Use the
SAME supplied `H_hat = Σ_p E(p) n_p` from the R-N5-IRR runner:
1. Confirm `H_hat` has non-degenerate spectrum on the block (gaps > tol). [If
   degenerate at chosen `(L_s, m)`, that degeneracy is itself the only place a true
   second commuting direction can hide — report it as the sharpened residual.]
2. For each mode `n_p`, **construct** `f_p(H_hat)` by Lagrange interpolation on the
   eigenvalues of `H_hat` and verify `‖n_p − f_p(H_hat)‖ ≈ 0` (i.e. `n_p` IS a
   function of the single generator). This is the decisive new computation the
   `span{I,H}` test missed.
3. Conclude: the "L_s-dimensional generator span" is the *tangent space of the
   abelian algebra `{H_hat}''`*, all of whose elements are functions of `H_hat`;
   the "second clock" `exp(-is·n_0)` equals `exp(-is·f_0(H_hat))`, a spectral
   re-clocking of the one supplied clock.
4. **Falsifier leg (the genuine boundary):** build the foreign proxy `H_A⊕H_B` on
   two *independent* tensor factors with **non-commuting** embedding (or, cleaner,
   two transfers that are NOT both functions of a common operator) and show `n_A`
   is provably **not** any `f(H_A⊕H_B)` — i.e. exhibit what a *real* second
   independent clock looks like, and confirm the supplied surface does not contain
   one (only the spectral-function family).

**Stop condition.** If step 2 fails for some `n_p` (a mode operator that is NOT a
function of `H_hat`), then `H_hat` has a degeneracy hosting a genuine independent
commuting direction, and N5 stays open *at that degeneracy* — a far narrower, more
honest wall than "L_s independent clocks." If step 2 passes, N5-as-"second-clock"
is dissolved into "one supplied generator, read through its own spectral functions."

---

## VECTOR C — Delete N2b for the downstream payload; quarantine the unit to the (already-primitive) scale/ratio layer

**Clause:** N2b. **Reduction type:** *premise inherited from a stale
unit-bearing route*; the target is **unit-free**, and the only dimensionless
time↔space ratio the geometry needs is **already an approved primitive**.

**Assumption challenged.** That the keystone needs an *absolute* clock unit `a_τ`
at all. The downstream payload (`d_t ≤ 1`, signature (3,1)) is a pure **count**:
it carries no seconds. N2a (the internal `1/(2a_τ)` denominator) is already
exact-support FORCED. The *absolute* unit `a_τ` enters no clause the consumer
reads. So for the keystone's actual job, **N2b is dead weight** — it is a residue
of an older ambition (mass-in-seconds) that the count statement does not inherit.

**Where the unit legitimately lives.** The registry already separates this:
- the single **absolute** dimensionful anchor is the approved
  `scale_reference_primitive` (`a⁻¹ = M_Pl`, units conversion only);
- the single dimensionless **time↔space graining ratio** is the approved
  `kinetic_isotropy_primitive` (`c_t = c_s` — "the emergent tick is grained on the
  same footing as the spatial edge", the time-direction analogue of cubic
  adjacency).

So the framework **already owns**, at approved-primitive grade, exactly the two
pieces a "clock" decomposes into: an absolute scale (scale-reference) and a
time/space form ratio (kinetic-isotropy). N2b is the *product* of these
(`a_τ` = a time spacing) — and a product of two already-granted quantities is not
a *new* missing premise; it is **double-counting**. The N2b no-go's sharp finding
("no A_min observable carries `1/time` units, so the joint rescaling `a_τ→c·a_τ`
is an exact gauge") is *consistent* with this: the rescaling is a gauge precisely
because the unit is supplied *elsewhere* (the scale-reference primitive), not by
A_min observables, and the count statement is gauge-invariant under it.

**Why this is new.** The N2b campaign (R-N2b-JOINT) tried to *derive* the absolute
unit from A_min rate gates and walled ratio-only. No route asks the prior question:
**does the keystone's downstream payload need the absolute unit at all, and if not,
is the residual `c_t=c_s` ratio already a primitive?** The kinetic-isotropy
primitive is cited by the keystone only in the "makes the surface *more*
exchange-symmetric" direction (S3′ line 400) — its role as **the supplier of the
one dimensionless time-graining datum** has never been connected to N2b.

**The sharpened claim to land.** *N2b is not a missing bridge of the codimension-1
keystone. The keystone's downstream content (`d_t ≤ 1`) is unit-free; the
`a_τ → c·a_τ` rescaling is an exact gauge of every clause it supplies. The only
dimensionless time↔space datum any geometric statement needs (`c_t = c_s`) is the
approved kinetic-isotropy primitive, and the only absolute scale is the approved
scale-reference primitive. Therefore N2b should be lifted out of B-AXIS entirely:
it is not a wall of this theorem; it is the (already-granted) scale/ratio layer.*
This **dissolves a clause** (per the exercise's "decisive" bar) by showing the
B-AXIS.1b premise is unnecessary for the keystone — without adding anything.

**First small runner (`baxis_n2b_unitfree_count_*.py`).**
1. Recompute the `d_t ≤ 1` chain end-to-end (chirality parity ⇒ `d_t` odd; one
   supplied generator ⇒ `d_t ≤ 1`) and verify **every quantity in it is
   dimensionless / an integer count** — no `a_τ` appears. (Grep-style: assert the
   count derivation has zero `a_τ` dependence by recomputing it at two different
   `a_τ` values and getting the identical integer.)
2. Re-run the exact `a_τ → c·a_τ, H→H/c` gauge (from the N2b runner) and confirm
   the count `d_t` is invariant (it must be — it never saw `a_τ`).
3. Instantiate the two primitives explicitly: absolute scale via
   `scale_reference_primitive` (one number `a⁻¹`), ratio via
   `kinetic_isotropy_primitive` (`c_t/c_s = 1`), and show that **(scale × ratio)**
   reconstructs a consistent `a_τ` *as a derived combination of two already-granted
   primitives*, not as a new admission. Print: "N2b = scale_reference ⊗
   kinetic_isotropy; no new bridge required for the count."
4. **Falsifier leg:** show a downstream claim that *does* need the absolute unit
   (a mass-in-seconds prediction) genuinely moves under the `a_τ` gauge — proving
   N2b is load-bearing *there* but provably not in the codimension-1 count. This
   keeps the no-go honest: N2b is real for unitful claims, vacuous for the count.

**Stop condition.** If step 1 finds any `a_τ` dependence in the count, N2b is a
real wall of the keystone and this vector fails. If clean, the deliverable is "N2b
out of B-AXIS" — B-AXIS shrinks from 3 clauses to (N4-count via A, N5-functional
via B), both of which are then about *counting one supplied generator*.

---

## VECTOR D — Smallest carrier: drop the staggered-Dirac carrier; does N4/N5 still bite on a bare 2-site `Cl(3,0)`-on-`Z³` toy?

**Clause:** N4 + N5. **Reduction type:** *delete the carrier* — test whether the
wall is a property of A_min or an artifact of the **staggered-Dirac/Kawamoto-Smit
realization** (a Tier-A *admission* `AC_phi_lambda`, NOT an axiom — see
`tier_a_admissions.json`).

**Assumption challenged.** That the staggered-Dirac surface is "THE carrier." It
is explicitly an admitted derivation target (`staggered_dirac_realization_gate`),
not part of A_min. The entire W/S₄ apparatus, the `(−1)^{x_τ x_1}` sign field, the
KS phase structure — all of it is carrier-specific. The exact-zero transport
residuals are bounded to *even cubic-symmetric staggered blocks* (odd-L falsifier
resid 6). **What does the wall look like on the bare A_min carrier with no
staggered structure at all?**

**The reduction.** A_min gives: `Z³` + nearest-neighbor cubic adjacency (Lattice),
one qubit / `Cl(3,0)≅M₂(C)` per site (Quantum), durable additive readout (Record).
*Nothing* in A_min mentions a 4th (time) coordinate, a staggered phase, or a
Euclidean 4-torus. The "4th axis" and W/S₄ are imported by the staggered
realization. Build the **smallest** A_min object that can host an evolution
question: a 2-site `Z³` patch (or even a single bond) with `M₂⊗M₂`, and ask
directly: *what is the minimal extra data that turns this into a one-parameter
evolution, and does that data have a label/second-clock ambiguity?* On the bare
carrier there are no four axes to permute — there is just a finite graph and a
need for a generator. This is the native-on-`Z³` framing the unified no-go §7
gestures at, but instantiated as a **concrete minimal finite toy** rather than a
prose reframe.

**Why this is new.** The campaign always works on the staggered surface (even §7's
native reframe is asserted, not built on a minimal carrier). No runner asks whether
N4/N5 even *exist* as questions before the staggered carrier is imposed. If they
don't bite on the bare carrier, then the wall is a property of the *admitted*
staggered realization, not of A_min — which **relocates the wall onto a Tier-A
admission** (a much weaker, more honest place than "A_min cannot supply time").

**First small runner (`baxis_bare_carrier_minimal_toy_*.py`).**
1. Build the bare A_min minimal object: 2 adjacent `Z³` sites, `M₂⊗M₂`, the cubic
   adjacency edge, additive scalar readout. **No** staggered phase, **no** 4th
   axis.
2. Enumerate the automorphism group of *this* structure (it is the graph
   automorphism × on-site `M₂` automorphisms — NOT B₄/S₄, since there is no 4th
   coordinate). Show the "which axis is time" question **has no referent** here:
   there is no 4-axis set to permute. N4-as-label is not even well-posed on the
   bare carrier.
3. Ask the count question instead: the minimal extra datum that makes this evolve
   is one generator `H` on `M₂⊗M₂`; show "number of independently supplied
   generators = 0 from A_min" (A_min supplies none — this is the *real* open gate,
   emergent-dynamics) and "= 1 once any single positive transfer is supplied"
   (then N5 reduces to Vector B on this tiny carrier).
4. **Comparison leg:** turn the staggered structure back ON (re-introduce the 4th
   axis + KS phases) and watch W/S₄ + the N4 label question *appear* — proving the
   ambiguity is injected by the admitted carrier, not by A_min.

**Stop condition.** If N4/N5 bite even on the bare carrier (some intrinsic A_min
structure forces a 4-axis ambiguity), the carrier is exonerated and the wall is
genuinely A_min-level. If they vanish on the bare carrier, **the wall is an
artifact of the `AC_phi_lambda` admission** — write it up as "B-AXIS is a property
of the staggered realization gate, not of A_min," which reframes the whole
keystone's missing-bridge from `missing_bridge_theorem` to `dependency on a Tier-A
admission`.

---

## VECTOR E — Read dynamics off the GENERATOR's semigroup, not the transfer matrix; recount the clock as `dim Z(alg generated by the dynamics)`

**Clause:** N5 (and the N4 count). **Reduction type:** *change the object* — stop
reading the clock off the **transfer matrix `T̂²`** (where the maximal `⊗_p`
factorization lives) and read it off the **one-parameter semigroup `{U(t)}` and
the algebra it generates**.

**Assumption challenged.** That `T̂² = ⊗_p diag(1, e^{−2E(p)})` being "maximally
factorized" means many clocks. The factorization is a property of the *transfer
matrix's tensor structure at one fixed step*, not of the *dynamics*. The keystone's
actual claim is about `U(t) = exp(-itH)`. The right invariant for "how many
clocks" is a property of the **generated algebra / its center**, not of how `T̂²`
happens to tensor-decompose.

**The reduction.** Define the clock-count as a single intrinsic number:
`n_clock := dim of the supplied one-parameter generator data`. The supplied data
is one `H`. The one-parameter group `{exp(-itH) : t∈R}` has a **commutant**
`{H}'`; the dynamics is "single-clock" iff the supplied evolution semigroup is the
one-parameter group of a single generator — which it is *by construction* (the
keystone is handed one `T̂²`, hence one `H`). The `⊗_p` factorization of `T̂²` is
the statement that `{H}'` is large (H non-degenerate ⇒ commutant is the abelian
diagonal algebra), which — as Vector B shows — means the factor flows are
*functions of H*, i.e. **inside the generated abelian algebra, contributing zero
to the count of independent generators.** Reading off the transfer matrix conflates
"the commutant of H is big" (true, harmless) with "there are many independent
generators" (false).

**Why this is new.** This is the operator-algebraic complement to Vector B: B says
"the factor generators are `f(H)`"; E says "therefore the *correct clock-count
observable* is generator-side (`dim` of supplied generators = 1), and the
transfer-side `⊗_p` count is the dimension of the commutant `{H}'`, a different
number that the consumer does not use." No ledger route distinguishes these two
counts; the entire N5 no-go is built transfer-side.

**First small runner (`baxis_generator_side_clock_count_*.py`).**
1. From the supplied `H_hat`, compute **two** numbers explicitly: (i)
   `n_gen := ` number of independently supplied one-parameter generators `= 1`;
   (ii) `dim {H_hat}' := ` dimension of the commutant (= L_s for non-degenerate
   spectrum on the L_s-mode block). Show these are different numbers and that the
   N5 no-go reports (ii) while the consumer needs (i).
2. Verify the supplied semigroup `{T̂²ⁿ}` and `{exp(-itH_hat)}` are generated by
   the single `H_hat` (Stone): the dynamics is one one-parameter group; the `⊗_p`
   structure is the spectral decomposition *of that one group*, not extra groups.
3. Print the reframed N5 statement: "single-clock ⟺ `n_gen = 1`; the supplied
   surface has `n_gen = 1`; `dim{H}' = L_s` is the size of the abelian symmetry of
   the one clock, not a second clock."
4. **Falsifier leg:** supply *two* genuinely independent generators (a real
   `H_1, H_2` not functions of a common operator) and show `n_gen` jumps to 2 while
   the structure is no longer one supplied transfer — confirming `n_gen` is the
   discriminating clock-count and that A_min's single-`T̂²` surface scores 1.

**Stop condition.** If `n_gen` cannot be made well-defined without already choosing
the generator (circularity), fold E into Vector B (functional-calculus is the
cleaner statement). If `n_gen = 1` holds robustly, E + B jointly **close N5** for
the consumer's purpose: one supplied generator, one clock, `d_t ≤ 1`.

---

## Cross-vector synthesis — the reduced B-AXIS

After deletion/reframing, the three-clause B-AXIS collapses toward a single,
*finite, A_min-internal* question the consumer actually needs:

> **How many independent positive transfer constructions (one-parameter
> generators), modulo the surface's geometric automorphisms, does the A_min
> surface supply?**

- **Vector A** makes the count label-free (W/S₄ is harmless to a count).
- **Vector B + E** show the per-mode "second clocks" are functions of the one
  supplied generator (spectral re-parametrization, not independent generators), so
  the count is **1** unless A_min supplies a *second independent* transfer.
- **Vector C** shows the absolute unit is not part of the count and is already
  carried by approved primitives — so N2b leaves B-AXIS.
- **Vector D** tests whether the remaining ambiguity is even an A_min property or
  an artifact of the admitted staggered carrier.

If A (count is label-free) + B/E (one supplied generator) hold on the runners, the
*actual* missing input shrinks to the genuinely-open emergent-dynamics gate
("A_min supplies no generator at all"), which is *honest and already known* — but
the **bundled B-AXIS over-claim (label + absolute unit + factor-exclusion) is
dissolved**, and the keystone's downstream `d_t ≤ 1` becomes conditional only on
"the surface supplies *at most one* independent transfer up to S₄," a finite check
rather than three separate missing bridges.

**What would make this decisive (per the exercise bar):** the Vector B runner
showing every factor generator `n_p = f(H_hat)` (functional calculus), combined
with the Vector A runner showing the count is S₄-invariant. Together they would be
a runner-backed reframe that *makes B-AXIS.2 (label) and B-AXIS.3 (second clock)
unnecessary for the keystone's only consumer* — not by deriving a label or a unit,
but by proving the requirement was over-specified. That is the "reframe that makes
the keystone's B-AXIS premise unnecessary" the EXERCISE.md names as decisive.

**What NOT to do (avoid re-pruned routes):** do not re-attempt OS/GNS, record
durability, registration cone, anomaly-chirality-as-label, KMS/APBC, Wilson gauge,
crossing-link/cocycle, reality/CPT grading, the per-axis Z₂ BC datum, or the
foreign `T_A⊗I, I⊗T_B` two-tensor proxy — all are in the NO_GO_LEDGER as N4/N5
transport/proxy failures. Do not try to *derive* the absolute unit `a_τ`
(R-N2b-JOINT already walled ratio-only). The new content here is strictly: (i)
solve the **count** not the label; (ii) test the second clock against the
**functional-calculus algebra of the one supplied generator**, not the linear
span or a foreign proxy; (iii) **delete** N2b from the keystone and quarantine it
to the existing scale/ratio primitives; (iv) test the bare A_min carrier.
