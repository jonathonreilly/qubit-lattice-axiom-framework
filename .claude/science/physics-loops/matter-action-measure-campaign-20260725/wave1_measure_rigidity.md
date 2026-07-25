# Wave 1 — the MEASURE half: is the Berezin measure rigid, and does that help?

Campaign: derive the physical matter action and its measure, or prove it
irreducibly supplied.
Date: 2026-07-25. Read against `origin/main` @ `e192e332f2`.

**Drift discipline.** This worktree's `docs/audit/data/ledger/` is ~1007 shard
files behind `origin/main`, and at least two rows I rely on differ. **Every
ledger status quoted below was re-read from `origin/main`** (via
`git archive origin/main docs/audit/data/ledger`), not from the worktree. Every
prose file I quote was diffed against `origin/main` and is byte-identical
(13/13 files checked). Two worktree-vs-origin ledger deltas found and corrected
in flight: `flavor_missing_axiom_carrier_measure_note_2026-05-30` is
`audited_conditional` on `origin/main` (worktree said `unaudited`), and
`koide_berezin_detc_vs_detr_fork_mechanism_note_2026-06-04` is
`audited_renaming` (worktree said `unaudited`).

**Mandatory framework refresher — surfaces read.**
`docs/MINIMAL_AXIOMS_2026-06-29.md` (all 193 lines);
`docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (all 46 lines);
`docs/audit/data/axiom_premise_nodes.json` (all four `canonical_ids`:
`minimal_axioms`, `scale_reference_primitive`, `kinetic_isotropy_primitive`,
`realized_state_primitive`); and the source note of every approved primitive
invoked below — `docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`,
`docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`,
`docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md`. Plus the obligation note in full and
the Berezin/carrier lane listed in §0.

**Runner (this wave, native, exact).**
`.claude/science/physics-loops/matter-action-measure-campaign-20260725/measure_rigidity.py`
→ `runner_output.txt`. **`TOTAL: PASS=128 FAIL=0`.** Pure sympy over `Rational`
and symbols; no floats as inputs; a from-scratch finite Grassmann engine
(monomial-dict exterior algebra, insertion-sort signs, left/right derivatives,
nilpotent `exp`, native Pfaffian by signed perfect matchings). No literature
value consumed. No audit status asserted or predicted anywhere.

---

## HEADLINE

**The hypothesis is TRUE and USELESS, and I can now say exactly why.**

The Berezin measure *is* rigid: on a fixed carrier, the translation-invariant
linear functionals on `Lambda_N` form a space of dimension exactly **1** —
computed at `N = 1..6` (`B1`), against a full functional space of dimension
`2^N` (`B6`). So the measure carries one scalar of freedom and nothing else.

But rigidity **cannot touch the grain question, for three independently
computed reasons**, and the third one is new:

1. **The scalar is `r`-inert.** `K`-reality cuts the scalar from `C^x` to `R^x`
   (`D2`); any nontrivial positivity requirement cuts it to `R_{>0}`
   (`F7/F7b`); and `r = |b|^2/a^2` and `Q = Tr(H^2)/(Tr H)^2` are degree-0
   homogeneous, so `R_{>0}` cancels identically (`D4/D4b`). The entire residual
   measure freedom is exactly the freedom that drops out of the observable.
2. **Rigidity is *relative to a carrier* — it takes `N` as INPUT.** The
   invariant-functional space is a line **for every** `N` (`E1`); the family
   over `N` is a disjoint union of lines with no canonical comparison map. A
   theorem of the form "given the carrier, the measure is unique" cannot
   select the carrier. And no pair of normalizations equates the horns:
   `c_6*det3 = c_12*det3^2` identically forces `c_6 = c_12 = 0`, verified by
   explicit coefficient extraction, `coeff(a^3) = c_6`, `coeff(a^6) = -c_12`
   (`F5`), with the degree obstruction `3` vs `6` (`E3`) and the general
   statement that `kappa*det M = (det M)^2` has **no** solution at all for any
   `n >= 1` (`C6b`, `F6`).
3. **NEW — the generator-count translation of the horn binary is not even
   faithful.** At **fixed** generator count `2n = 12` and with the **same**
   unique measure, **both** horn values are realized by choosing the action's
   kernel: `W (+) W -> det3^2` (count-twice) and `W (+) I_3 -> det3`
   (count-once) (`F4`, `F4b`, `F4c`). So the binary is not a carrier-dimension
   datum either. It is a joint **carrier-and-action** datum, and the action is
   precisely what `MINIMAL_AXIOMS_2026-06-29.md:170` places outside axiom
   content.

Sharpest single sentence: **the measure is rigid, the rigidity is purchased
with a supplied invariance property, and what it buys is a scalar that cancels
in `r`.** The freedom does not shrink; it relocates to the two places the
framework already had it — the carrier and the action.

---

## §0 KILL-CHECK AND PRIOR-ART SWEEP (run BEFORE the rest, per campaign rule 2)

The route is **not** dead, but the headline of part (a) is **twelve-and-a-half
weeks of prior art**, and I nearly reported it as new. Recording it first.

### (0a) The Berezin uniqueness fact is already in the corpus, verbatim

`docs/OCCUPANCY_READOUT_EXPONENT_BEREZIN_SUBSUMPTION_BOUNDED_THEOREM_NOTE_2026-06-09.md:35-37`:

> 3. **Berezin uniqueness (B3):** translation invariance forces the Grassmann
>    functional to be unique up to scale (computed) — **no measure freedom exists
>    in the fermionic realization.**

and the same note, `:52-55`, already reached my conclusion (2):

> 6. **Adversarial multiplicity (B6):** in the complex-mode realization the
>    exponent-2 atom (`a²`) is obtainable *only* by doubling the field content
>    (computed: two independent modes → `a²`) — i.e. by changing the
>    *realization*, never by a readout choice.

and `:113`:

> the tested Berezin realization has no measure freedom that can select the
> occupancy exponent.

**Live status (`origin/main`): `occupancy_readout_exponent_berezin_subsumption_bounded_theorem_note_2026-06-09`
— `effective_status = unaudited`, `audit_status = unaudited`.**
So the fact is *stated* in the corpus but is not a landed authority. This wave's
contribution to (a) is therefore a **native rebuild at exact grade with the gate
made explicit**, not a discovery. I say so plainly rather than re-selling it.

### (0b) The measure-side collapse at fixed count is also prior art (8 days old)

`docs/KCPT_COUPLING_TRIPLE_BEREZIN_COUNT_BINARY_MEASURE_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-07-17.md`
T4 proves, dimension-independently by the top exterior power, that every
constant homogeneous odd-linear substitution at held measure acts on the
zero-source output by `det S`, and `:249-252`:

> 6. **No constant-scalar conversion.** No constant `kappa` satisfies
>    `kappa * det3 = det3^2` identically on entrywise-real triples: the
>    forced values at the exact witnesses `(1,0,0)` and `(2,0,0)` are `1` and
>    `8`

and `:335-339`:

> 3. **Neither horn forced** (runner B5): at the entrywise-real witness
>    `(3,1,1)` the count-once Berezin integral is `20` and the count-twice
>    12-generator Berezin integral is `400`; both are nonzero and
>    well-defined, and nothing on the surface prefers either.

I **reproduce both natively** (`C5`: `20` and `400`; `C6b`/`F6`: no `kappa`),
and generalize the second from two witnesses to all `n >= 1` by the polynomial
degree split (`C6`, `F6`). Live status: `unaudited`.

That note is also explicit about its own boundary, `:295-299`:

> It does not derive the physical action or its measure, and it does not
> touch the closure criterion's "action and its measure" unknowns or narrow
> the grain obligation

and it is careful about the count translation, `:112-115`:

> the correspondence between the graining slot count and the generator count
> is declared bookkeeping; no framework clause identifies occupancy slots with
> Grassmann generators, and T3 makes no equivalence claim.

**My `F4` is the computed witness showing that caution was necessary**: the
correspondence *cannot* be upgraded to an equivalence, because one carrier
dimension carries both horn values. That is the one genuinely new piece here.

### (0c) The axioms-do-not-supply-the-measure result is prior art too

`docs/ACPHILAMBDA_MEASURE_BINARY_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md:58-72` —
one of the three route maps the obligation itself names:

> ```text
> Lattice + Qubit + Admissibility + Record
> + scale/kinetic/realized-state primitives
> do not choose
>   generator-channel / orbit / holomorphic count-once
> over
>   dimension / sector / real count-twice.
> ```
> ... None of those clauses selects a physical generation readout partition, a
> carrier-measure scoring rule, a determinant/Pfaffian order, a Born/interface
> rule, or a weighting/normalization over the singlet/doublet carrier.

Live status: `unaudited` (`no_go`). Its "Remaining Live Routes" item 1
(`:138-140`) is literally this campaign's target.

### (0d) PROSE-VS-LEDGER CONTRADICTIONS FOUND IN THIS LANE

Per the campaign's rule 6, I did not lean on prose. Two concrete hits, both on
rows a reader of this lane would otherwise trust:

| prose claim | file:line | live `origin/main` ledger |
|---|---|---|
| "`FLAVOR_MISSING_AXIOM_CARRIER_MEASURE_NOTE_2026-05-30.md` is the **retained-bounded** carrier-measure boundary theorem" | `docs/ACPHILAMBDA_MEASURE_BINARY_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md:42-44` | `flavor_missing_axiom_carrier_measure_note_2026-05-30` = **`audited_conditional`** |
| "No-forcing boundary ... **retained_no_go** per `STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md`"; and "D5 ... prior ledger grade **retained_bounded**" | `docs/STAGGERED_DIRAC_GRASSMANN_FORCING_THEOREM_NOTE_2026-05-07.md` premise table | both **`unaudited`** (`..._statistics_agnostic_no_forcing_note_2026-05-25`; `..._substep1_grassmann_forcing_bridge_narrow_theorem_note_2026-05-16`) |

### (0e) Kill-check verdict

Not foreclosed, not ill-posed, but **strictly narrower than briefed**: the
measure question was already answered in the corpus (unaudited) in the
direction "rigid, and therefore unhelpful". The live value of this wave is
(i) the native exact rebuild with the gate stated, (ii) the classification of
*what* remains free with each item adjudicated against landed content, and
(iii) `F4`.

---

## §1 (a) THE BEREZIN UNIQUENESS FACT — stated precisely, proven natively, gated

### 1.1 Exact statement

Let `V` be a complex vector space with ordered basis `theta_1, ..., theta_N`
and let `Lambda_N = Lambda(V)` be the exterior (Grassmann) algebra, so
`dim Lambda_N = 2^N` (`A3`, checked `N = 1..6`). Let `d_i` denote the left
Grassmann derivative.

> **(U) Uniqueness.** The space of complex-linear functionals
> `L : Lambda_N -> C` satisfying `L(d_i f) = 0` for every `i in {1..N}` and
> every `f in Lambda_N` is **exactly one-dimensional**, and is spanned by the
> top-coefficient functional `f |-> [coefficient of theta_1...theta_N in f]`.
>
> **(U') Equivalent hypothesis.** The same space is obtained by imposing odd
> translation invariance `L(f(theta + eta)) = L(f(theta))` for all odd
> parameters `eta_i`.

### 1.2 Native proof

Write `theta_T` for the ordered monomial on `T subset {1..N}`.

*(⊆)* Each `d_i` strictly lowers Grassmann degree by one, so
`im(d_i) subset span{theta_T : |T| <= N-1}` for every `i`. In particular no
`d_i` output ever contains the top monomial (`B4`, computed `N = 1..6`).

*(⊇)* For any `T` with `|T| <= N-1`, choose `i not in T`. Then
`d_i theta_{{i} u T} = (-1)^p theta_T` with `p` the position of `i` in the
ordered monomial. Hence every sub-top monomial lies in the span of the images.

Therefore `span(u_i im d_i) = span{theta_T : |T| <= N-1}`, a subspace of
codimension exactly 1 — verified by rank: `rank = 2^N - 1` at `N = 1..6`
(`B3`: `1, 3, 7, 15, 31, 63`). Its annihilator is one-dimensional and is
spanned by the top-coefficient functional. ∎

For (U'), expand `prod_{i in T}(theta_i + eta_i)`, push all `eta` letters left
with the induced signs, and demand that the coefficient of every **nonempty**
`eta`-monomial vanish. The resulting linear system is built and solved directly
in the runner: its null space has dimension 1 and is supported exactly on the
top monomial (`B7`, `B8`, `N = 1..4`), and coincides with the derivative
characterization (`B9`).

### 1.3 The gate — stated exactly, because it is load-bearing

**(U) is conditional on the invariance hypothesis, and that hypothesis is
supplied, not derived.** Without it there is no rigidity at all: the full
functional space has dimension `2^N` (`B6`: `2, 4, 8, 16, 32, 64`). Dropping a
**single** one of the `N` derivative conditions already breaks uniqueness — the
solution space jumps from 1 to 2 (`B5`, `N = 2..5`). Every condition is
load-bearing.

Nothing in Lattice, Qubit, Admissibility or Record mentions Grassmann
generators, let alone invariance under odd translation of them.
`MINIMAL_AXIOMS_2026-06-29.md:161` lists

> - the staggered-Dirac/finite-Grassmann realization and `AC_phi_lambda`;

among the gates **outside** axiom content, and `:170` lists

> - source/action and physical-observable identification;

The one landed authority on this algebra says the same about its own
hypotheses. `docs/SPIN_STATISTICS_BEREZIN_DETERMINANT_NARROW_THEOREM_NOTE_2026-05-10.md`
(live: `retained_bounded` / `audited_clean`), `:148-154`:

> - Does **not** derive (G1)-(G3) themselves from a deeper axiom. They
>   are the *definition* of the Grassmann generators.

**Construction-mutation probes on (U)** (campaign rule 4 — not assertion
probes): rebuilding the entire engine with the **right** derivative instead of
the left gives `dim = 1` unchanged (`F1`, `N = 2..5`); rebuilding it with a
deliberately **sign-stripped** derivative also gives `dim = 1` (`F2`). So the
uniqueness *dimension* is carried by the degree filtration, not by any sign
convention — the result is convention-free, which is the honest way to gate it.

### 1.4 What the rigid measure actually computes (and what it does not)

With the ordering `theta_i = generator 2i`, `thetabar_i = generator 2i+1`, the
top-form functional applied to `exp(-thetabar M theta)` returns `sigma_n det M`
with the sign **computed**, `sigma_n = +1` for `n = 1, 2, 3` (`C1`, `C1b`);
reversing the generator order multiplies by `(-1)^{N(N-1)/2}` (`D1`), a scalar.
Native rebuilds of the two identities the lane leans on:
`Pf([[0,K],[-K^T,0]]) = (-1)^{n(n-1)/2} det K` at `n = 1, 2, 3` (`D6`, by
signed perfect matchings), and `det_R R(K) = |det_C K|^2` at `n = 1, 2` (`D6b`).

**Where the physics enters is the action, not the measure.** Construction probe
`F3`: on the *same* carrier with the *same* unique measure, adding a quartic
term `g * thetabar_1 theta_1 thetabar_2 theta_2` changes the value to
`a^3 + b^3 + c^3 - 3abc - a*g`, and `F3b` confirms it returns to `det3` exactly
at `g = 0`. The measure contributes one operation — extract the top coefficient
— and *all* coupling dependence enters through `S`.

---

## §2 (b) WHAT IS ACTUALLY FREE — item by item, adjudicated against landed content

| datum | freedom after (U) | fixed by landed framework content? |
|---|---|---|
| normalization scalar | `C^x` → `R^x` under `K`-reality → `R_{>0}` under positivity | **NO**, and it does not matter: it cancels in `r` |
| carrier / generator count `N` | integer, unconstrained by the measure | **NO** — the whole staggered-Dirac carrier lane is `unaudited` |
| polarization (`theta` vs `thetabar`) | acts on the measure only by `det(P) = ±1` | not measure content at all — it is carrier + action content |
| pairing / conjugation (`K`/CPT) | fixes the *phase* of the scalar only | **NO** for anything else |

### 2.1 The normalization scalar — free, and inert

`K`-compatibility (`L o conj = conj o L`) forces `Im(c) = 0` (`D2`, solved
exactly). Positivity fixes the sign: scaling the functional by `c` scales every
Gram built from it by `c`, so a Gram that is positive definite at `c = +1` —
exact witness `diag(m_1, m_2)` with `m_i > 0` (`F7`) — is negative definite at
`c = -1` (`F7b`). Modulus untouched. And the surviving `R_{>0}` is exactly the
group under which `r = |b|^2/a^2` and `Q = Tr(H^2)/(Tr H)^2` are invariant
(`D4`, `D4b`, degree-0 homogeneity).

No approved primitive supplies it, and each says so by name:
`docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md:14-16` —

> Do not grant more than the primitive source note declares. Any
> dimensionless quantity, selector, weighting rule, normalization rule,
> probability rule, readout bridge, dynamics, source/action, or empirical
> match remains separate unless independently derived.

`docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md:38-40` — the primitive carries

> no state, averaging over alternatives, measure, ... normalization rule, or value

**Net: the one thing the measure genuinely owns is a positive real number that
provably cancels in the observable.** That is the precise sense in which
"Berezin measures are rigid" is a true statement with no physical payload.

### 2.2 The carrier and generator count — the whole ballgame, and not landed

`origin/main` ledger, read directly from the shards:

| row | `effective_status` |
|---|---|
| `staggered_dirac_realization_gate_note_2026-05-03` | `unaudited` |
| `staggered_dirac_grassmann_forcing_theorem_note_2026-05-07` | `unaudited` |
| `staggered_dirac_substep1_grassmann_forcing_bridge_narrow_theorem_note_2026-05-16` | `unaudited` |
| `staggered_dirac_substep1_statistics_agnostic_no_forcing_note_2026-05-25` | `unaudited` |
| `occupancy_readout_exponent_berezin_subsumption_..._2026-06-09` | `unaudited` |
| `kcpt_coupling_triple_berezin_count_binary_measure_collapse_..._2026-07-17` | `unaudited` |
| `flavor_missing_axiom_carrier_measure_note_2026-05-30` | `audited_conditional` |
| `koide_berezin_detc_vs_detr_fork_mechanism_note_2026-06-04` | `audited_renaming` |
| `spin_statistics_berezin_determinant_narrow_theorem_note_2026-05-10` | `retained_bounded` |
| `acphilambda_occupancy_determinant_power_split_exact_support_note_2026-07-04` | `retained` |
| `acphilambda_fermionic_realification_pfaffian_power_identity_..._2026-07-12` | `retained` |

The three rows at `retained`/`retained_bounded` grade are all pure finite
algebra over a **supplied** carrier, and each says so itself. The strongest
one — `acphilambda_fermionic_realification_pfaffian_power_identity_..._2026-07-12`,
`retained` / `audited_clean` — states at `:146-151`:

> The theorem domain is a supplied Grassmann action, Berezin measure, and
> determinant carrier. Framework derivation of the charged-lepton carrier,
> global CAR structure, physical single-sector readout, `K`/CPT-orbit occupancy
> grain, registered `r`, `delta`, and R-eta readout lies outside this theorem.

And the carrier is not merely underived, it is *contested* on the corpus's own
surface. `docs/STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md:75-81`:

> The Axiom 1 / Axiom 2 baseline admits the Grassmann/fermionic reading (via a
> JW frame choice) but also admits the hard-core-boson reading; the two are the
> same ungraded operator algebra ... The Grassmann content remains an
> **admission candidate** (a statistics selection), not a theorem derived here
> from the baseline alone.

which `docs/STAGGERED_DIRAC_GRASSMANN_FORCING_THEOREM_NOTE_2026-05-07.md:100-106`
concedes:

> 2. **Unconditional forcing: FALSE (T3).** ... "The matter measure is uniquely
>    Grassmann" does **not** follow from the Lattice+Quantum baseline plus
>    dimension/operator-algebra data

So the measure-rigidity theorem's *hypothesis* — that we are on a Grassmann
carrier at all — is itself an open selection.

### 2.3 Polarization — not a measure datum

The top-form functional is the coefficient of `theta_1 ... theta_N`, which does
not reference which generators are called `theta` and which `thetabar`.
Relabelling by a permutation `P` multiplies the functional by `det(P) in {±1}`
(`D5`, `N = 4` and `N = 6`, three seeds each) — i.e. it lands inside the
scalar freedom of §2.1 and nowhere else. Polarization enters through **which
quadratic forms are writable** on the carrier (paired `thetabar M theta` versus
Pfaffian `(1/2) xi^T A xi`) and through the carrier's own pairing structure —
both action/carrier content. This is consistent with, and locates, the
polarization-conditionality that
`OCCUPANCY_READOUT_EXPONENT_..._2026-06-09.md:41-46` already carries as an open
condition ("which Berezin cell applies is conditional on the **polarization of
the matter realization**").

### 2.4 Pairing / conjugation — fixes a phase, nothing else

The top-form functional is `C`-linear and is defined with no reference to any
conjugation. Imposing `K`-compatibility constrains the *scale* to be real
(`D2`) and imposes nothing on `N`, on the polarization, or on the action. In
particular, the measure supplies **no** reality structure and therefore cannot
answer the stage residual that the section-tie note carries.

---

## §3 (c) DOES THE MEASURE SIDE FIX WHAT THE READOUT SIDE COULD NOT?

**Computed answer: NO. Not partially, not in one horn — not at all.**

### 3.1 The two freedom counts, side by side

The previous campaign computed, on the readout side
(`.claude/science/physics-loops/koide-mode-content-campaign-20260724/wave2_defend_ex2.md:302-307`;
restated at `wave3_live_obligation.md:270`; **untracked session output, on no
branch**):

```text
dim { finitely additive I }  on a 1-atom alphabet  =  1
                             on a 2-atom alphabet  =  2
                             on a 3-atom alphabet  =  3
```

→ on the 2-letter record alphabet, one free ratio `nu = w_1/w_0` survives the
overall scale, and Record constrains it by exactly nothing.

This wave computes, on the measure side (`B1`, `B6`, `E1`):

```text
dim { all linear functionals on Lambda_N }          =  2^N
dim { translation-invariant functionals on Lambda_N } =  1     for every N = 1..6
```

→ on a fixed carrier, one free scale `c` survives, and it is `r`-inert (§2.1).

**The measure's one parameter is not `nu`, and it does not constrain `nu`.**
The readout's residual is a ratio between two inequivalent record letters; the
measure's residual is an overall normalization of a top-form. The two live in
different slots, and the measure's slot cancels in the observable.

### 3.2 The horn binary is a carrier datum — rebuilt natively

Prior art declared the translation (`KCPT_..._2026-07-17.md:34-38`, T3: horn
`m` uses `6m` generators, flagged at `:112-115` as bookkeeping, not an
equivalence). I rebuilt both sides exactly on my own engine:

- 6 generators, kernel `W(a,b,c) = a I + b C + c C^2` →
  `det3 = a^3 + b^3 + c^3 - 3abc` (`C2`, `C3`);
- 12 generators, two disjoint copies → `det3^2` exactly, factorizing as the
  square of the 6-generator value (`C4`, `C4b`);
- at `(a,b,c) = (3,1,1)`: **20** and **400** (`C5`) — reproducing
  `KCPT_..._2026-07-17.md:335-339` independently.

And no scalar bridges them, for **all** `n`, not just at witnesses:
`deg(det M) = n`, `deg((det M)^2) = 2n` (`C6`); `kappa*det M = (det M)^2` has
no solution whatsoever, since the `det^2` coefficient is the nonzero constant
`-1` (`C6b`, `F6`); and allowing the two carriers *independent* normalizations
does not help — `coeff(a^3) = c_6`, `coeff(a^6) = -c_12` forces both to vanish
(`E2`, `F5`).

### 3.3 NEW — but the binary is not a *pure* carrier datum either

This is the computation that goes past the prior art, and it cuts against the
tidy story.

At **fixed** generator count `2n = 12` and with the **same** unique top-form
measure, choose the kernel:

```text
kernel  W (+) W    on 12 generators  ->  det3^2   (the count-TWICE value)   (F4)
kernel  W (+) I_3  on 12 generators  ->  det3     (the count-ONCE value)    (F4b)
```

Both computed exactly on the same engine; the values differ (`F4c`). **The
generator-count translation of the horn binary therefore cannot be upgraded
from bookkeeping to an equivalence** — exactly the caution
`KCPT_..._2026-07-17.md:112-115` recorded, now with the witness that forces it.
The binary is a joint **carrier-and-action** datum, and by
`MINIMAL_AXIOMS_2026-06-29.md:170` the action is outside axiom content.

### 3.4 NEW — and the *only* thing making the measure horn-blind is the supplied invariance

Within the full `2^N`-dimensional functional space, the horn conversion **is**
available. On the 12-generator count-twice carrier, the "partial-top"
functional — top monomial of copy 1, constant term of copy 2 — returns exactly
the count-once value `det3` (`C7`). It is a perfectly good linear functional; it
is simply not translation invariant, and the runner exhibits the failure:
`L'(d_6 (theta_0...theta_6)) = 1 != 0` (`C7b`).

So the clean statement "the measure cannot convert the horns" is **true only
because translation invariance was imposed**, and translation invariance is a
supplied defining property of Berezin integration, not framework content
(§1.3). The rigidity and its uselessness come from the same assumption.

---

## §4 (d) PLAIN ANSWER

**The measure is derivable *given the carrier*, up to a positive real scalar
that cancels in `r` — and it inherits, verbatim and undiminished, the freedom
that the carrier and the action carry.**

More precisely, and this is the wave's deliverable:

1. Given (i) a Grassmann carrier with a fixed generator count and (ii) the
   translation-invariance hypothesis, the measure is **unique up to one
   scalar** (`B1`, `B7`, exact, `N <= 6`). Prior art at
   `OCCUPANCY_READOUT_EXPONENT_..._2026-06-09.md:35-37`, `unaudited`; rebuilt
   natively here.
2. That scalar is cut to `R^x` by `K`-reality (`D2`), to `R_{>0}` by positivity
   (`F7/F7b`), and is then **identically inert in `r` and `Q`** (`D4/D4b`).
3. Hypothesis (i) is not landed: the carrier lane is `unaudited` end-to-end and
   the corpus's own no-forcing note keeps the Grassmann selection an admission
   candidate (§2.2).
4. Hypothesis (ii) is not framework content, and dropping it restores enough
   freedom to convert the horns outright (`C7`).
5. The grain binary is not localized in the carrier dimension either — one
   carrier dimension realizes both horns under two different actions (`F4`).

**Therefore: the measure half of the obligation's first conjunct is not the
soft half.** It is a one-scalar appendage to the carrier-and-action question,
and solving it completely — which is essentially already done — moves the
obligation by zero. The obligation's difficulty is entirely in "the physical
matter action" and in the carrier that action lives on.

This is a **sharp negative on the wave's hypothesis as a route**, and it is a
clean one: it converts "maybe the measure is more constrained than the action"
into "the measure is maximally constrained *and that is why it is empty*."

---

## §5 NON-CLAIMS

1. No derivation of `r`, `Q`, `delta`, an occupancy law, a graining horn, a
   stage selection, a physical matter action, a carrier, or a measure.
2. No claim that (U) is new. It is prior art at
   `OCCUPANCY_READOUT_EXPONENT_..._2026-06-09.md:35-37` (`unaudited`); this
   wave rebuilds it natively and states its gate.
3. No claim that any row is retained, retired, promoted, demoted, or should be.
   No audit verdict is set or predicted. Every status quoted is a read of
   `origin/main` ledger shards, reported as data.
4. No new axiom, primitive, vocabulary, tag, or class is proposed.
5. `F4` is a statement about the declared finite probe surface (the `C_3[111]`
   coupling triple and its doubling), not about any physical carrier. It shows
   a *translation cannot be upgraded to an equivalence*; it does not select a
   horn, and does not contradict `KCPT_..._2026-07-17.md`, which explicitly
   declined to make the equivalence claim.
6. The positivity step in §2.1 is scoped: it says any nontrivial positive
   semidefinite Gram built from the functional flips sign under `c < 0`
   (linearity plus one exact witness). It is not a reflection-positivity
   theorem, and no RP surface is claimed or consumed.
7. Nothing here is on any branch. No file outside this campaign directory was
   touched; nothing was committed, pushed, or opened as a PR.

---

## §6 VERIFICATION

```bash
python3 .claude/science/physics-loops/matter-action-measure-campaign-20260725/measure_rigidity.py
```

```text
TOTAL: PASS=128 FAIL=0
```

Blocks: `A` algebra sanity (nilpotency, anticommutation, `dim = 2^N`, graded
Leibniz both parities); `B` uniqueness (`B1-B6` derivative form `N <= 6`,
`B7-B9` translation form `N <= 4`, `B5` mutation probe); `C` Gaussian values,
horn arithmetic, degree obstruction, and the non-invariant conversion witness;
`D` normalization / `K`-reality / positivity / scale-inertness / polarization /
native Pfaffian and realification; `E` per-carrier line count and horn-scale
obstruction; `F` construction-mutation probes (`F1` right derivative, `F2`
sign-stripped derivative, `F3` quartic deformation, `F4` fixed-carrier both
horns, `F5-F6` explicit coefficient extraction rather than solver trust,
`F7` Gram sign).

No check passes by literal stipulation. Every constant reported (`+1` signs,
`20`, `400`, `det S` factors, `2^N`, `2^N - 1`) is computed, and the two
horn-value constants are cross-checked against the independent prior-art runner
values quoted in §0b.

---

## §7 HANDOFF — where the wave says to point next

1. **Stop treating the measure as a lever.** Any wave whose plan is "constrain
   the Berezin measure harder" is spending effort on a one-parameter object
   that cancels. §3.1 and §2.1 are the reason.
2. **The live sub-question is the CARRIER, and it is contested, not merely
   open.** `STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md:75-81`
   says the baseline admits a hard-core-boson reading of the same ungraded
   algebra. If that stands, "the matter action" does not have a determinate
   Grassmann carrier to be written on, and the obligation's first conjunct is
   ill-posed *below* the action, at the level of statistics selection. A wave
   should adjudicate that note against `origin/main` directly.
3. **`F4` reframes the grain question.** Since one carrier dimension carries
   both horns, any future selection argument must constrain the **kernel's
   block structure**, not the generator count. That is a different and probably
   harder target than the one the lane has been chasing, and it should be
   stated before anyone invests in a count-based selector.
4. **Two prose-vs-ledger contradictions (§0d) are live in this lane** and both
   inflate a grade. Worth a hygiene pass, out of scope here.
