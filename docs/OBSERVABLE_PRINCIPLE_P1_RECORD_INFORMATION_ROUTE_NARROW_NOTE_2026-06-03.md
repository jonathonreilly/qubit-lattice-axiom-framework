# Observable-Principle P1 Bridge — Record / Recorded-Information Route Narrow Note

**Date:** 2026-06-03
**Claim type:** no_go
**Type:** no_go
**Claim scope:** narrow no_go that tests the **recorded-information reframe** as
a candidate derivation of the admitted P1 premise (scalar additivity on
independent subsystems) of
[`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`](OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md)
from the framework's own measurement structure. The reframe proposes the
pipeline "qubit (probability) until record (information)": amplitude `psi`
(multiplicative for independent tensor systems) → Born `p = |psi|^2`
(multiplicative) → a **record** forms → recorded **information** `I = -log p`
(**additive**: `I_AB = I_A + I_B`). The claim is that the physical scalar
observable is the recorded information (additive) because (i) A1 is a
measurement framework so observables **are** records/measurement-outcomes, and
(ii) a physical record is a **sequence of definite marks** whose size is
additive **by concatenation** (a free-monoid structural fact), so P1 would
reduce to A1 + record-additivity = **derived**, not admitted.

> **Statement (the record route re-introduces the same `-log` choice).** Two
> crux facts decide it.
>
> - **Crux 1 — A1 does not force "observable = record."** A1 commits only the
>   per-site qubit operator algebra (`M_2(ℂ) ≅ Cl(3,0)`) and the `Z^3`
>   substrate; **measurement, records, and the Born rule are explicit
>   derivation lanes, not axiom content** (`MINIMAL_AXIOMS_2026-05-20.md`:
>   "records, Born probabilities … are not additional primitives in A1-A2").
>   "the physical scalar observable = the recorded information" is therefore an
>   **additional identification**, not an axiom consequence (§3.1, runner T6).
> - **Crux 2 — the `-log` at the record is the same free choice as P1.** The
>   framework's actual record object is a Kraus instrument
>   `W = Σ_r K_r ⊗ |r⟩` whose branches are labeled by an orthonormal record
>   basis `{|r⟩}` and quantified by the **Born probability**
>   `p_r = Tr(K_r ρ K_r†)`
>   (`PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md`,
>   `BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md`). On
>   independent tensor branches that weight is **multiplicative**
>   (`p_AB = p_A · p_B`). Passing to an **additive** recorded scalar requires
>   the map `p ↦ -log p`. But this is exactly the selection of the additive
>   representative `q → 0` (`log`) from the multiplicative family
>   `Φ_q(p) = p^q` (equivalently the v-chain `F_p = |det|^p` in the modulus
>   variable `r = |Z|`) — i.e. condition **(Add) = P1** (Cauchy classifier;
>   additivity is the **hypothesis**). The record's own Born quantification is
>   **exponent-blind** — the normalized/Born gradient returns the same
>   expectation field for **every** exponent — i.e. the **(BLIND)** face of the
>   `OBSERVABLE_PRINCIPLE_P1_EXPONENT_SELECTOR_DICHOTOMY_NARROW_NOTE_2026-06-02.md`
>   (#2504) dichotomy, which singles **nothing** (§3.3, runner T5). So the
>   record route lands in **(BLIND)** (Born quantification of the branch) or
>   **(ADD) = P1** (the `-log` recorded size); there is no third option.
> - **The free-monoid kernel is genuinely additive but inert.** Concatenation
>   length on the free monoid `A^*` satisfies `|w₁w₂| = |w₁| + |w₂|` and is the
>   unique equal-weight homomorphism `A^* → (ℝ,+)` up to scale (§3.4, runner
>   T3 — reproven, with free-monoid length cited only as comparator). But to
>   make "record **size** = number of marks" reproduce the framework's
>   **continuous** additive readout `W = log|det(D+J)|`, the size of a Born
>   branch of probability `p` must be set to `∝ -log_b p` (the Shannon/Kraft
>   optimal code length) — which **is** the `-log p` choice of Crux 2. The
>   alternative, a **bare integer mark-count**, is (a) not pinned by A1 (no
>   axiom assigns marks to branches) and (b) **integer-quantized**, hence a
>   **different object** that cannot equal the continuous `log|det|` v-chain
>   observable (`-log_2(1/3)` is not an integer; §3.5, runner T4).

**Result.** The recorded-information reframe does **not** derive P1; it
**re-describes** it (verdict `circular_log_reintroduced`). A1 does not supply
"observable = record" (Crux 1); the framework's record carries the
multiplicative Born weight and the `-log` that makes the recorded scalar
additive is the **same** free choice as P1, the **(Add)** face (Crux 2); and the
free-monoid concatenation length — though a genuine additive, unique-up-to-scale
invariant — does not single out the additive **quantification** of a Born branch
over the multiplicative one without re-importing the `log`. This **confirms and
extends** #2456 / #2504 / #2517 and the structural-reframing no_go: the
"information at the record" candidate collapses into the same
multiplicative→additive (`exp`/`log`) dichotomy. This note does NOT close
P1; it pins the record route as P1-equivalent. It does **not** promote, demote,
or set the audit status of any framework row.

**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome; later status is generated by the audit pipeline
after independent review. The `no_go` label is a source-side claim-boundary
declaration, not an audit verdict.
**Source-note proposal disclaimer:** this note is a source-note proposal; audit
verdict and downstream status are set only by the independent audit lane.
**Primary runner:**
[`scripts/audit_companion_observable_principle_p1_record_information_route_2026_06_03.py`](../scripts/audit_companion_observable_principle_p1_record_information_route_2026_06_03.py)

## 0. Honest framing up front

The P1 derivation lane has been attacked across roughly a dozen routes and
consolidated in the Route D no-go
(`OBSERVABLE_PRINCIPLE_P1_BRIDGE_ROUTE_D_SHARPENED_NO_GO_NOTE_2026-05-17.md`) and
the campaign closure synthesis
(`OBSERVABLE_PRINCIPLE_P1_CAMPAIGN_CLOSURE_SYNTHESIS_NOTE_2026-05-18.md`). Three
recent notes sharpen the picture:

- `OBSERVABLE_PRINCIPLE_P1_EXPONENT_FIXING_IRREDUCIBILITY_NARROW_NOTE_2026-05-31.md`
  (#2456, on main) proves the det-vs-tr **form** is a theorem on the
  operator-product axis, and the **exponent-fixing** step is the irreducible
  P1-equivalent atom: every selector that fixes the exponent is one of
  **(Add)/(Loc)/(Pot)** (all P1), while the **normalized/Born gradient** is
  exponent-blind and selects nothing. It explicitly classifies the
  cumulant / `W = log Z` identification as **(Add) = P1**.
- `OBSERVABLE_PRINCIPLE_P1_EXPONENT_SELECTOR_DICHOTOMY_NARROW_NOTE_2026-06-02.md`
  (#2504, branch `claude/p1-exponent-selector-dichotomy-2026-06-02`; referenced
  textually to avoid a dangling citation edge) upgrades #2456 to a
  **BLIND-or-ADD dichotomy** over a precisely-defined sector-composition
  selector class `𝒞`: every member either is orbit-invariant under
  `{r ↦ r^p}` (BLIND, singles nothing) or references the bare generator value
  and the only singling law is additivity (ADD = P1, unique `log`). It records
  the one open forward path **(a′)**: a genuinely new retained primitive that
  introduces a privileged scale by a **separate physical mechanism outside
  `𝒞`**.
- `OBSERVABLE_PRINCIPLE_P1_SYMMETRY_TYPE_ENERGY_READOUT_NARROW_NOTE_2026-06-02.md`
  (#2517, branch `claude/p1-symmetry-type-energy-readout`; referenced textually)
  tests the **energy ledger** as a path-(a′) candidate and finds it
  P1-equivalent: "energies add" and "`W = log Z` is additive" are the same
  `exp`/`log` content at two levels, with the intensive/Born variant in face
  BLIND.

**This note tests the next path-(a′) candidate: the record / recorded-information
ledger.** It is the most physically appealing remaining candidate because the
framework's own slogan is "qubit (probability) until record (information)," and a
**record** plausibly supplies an additive structure by **concatenation** (a
free-monoid fact) that is not, on its face, a `log`-of-probability choice.

**The honest finding is `circular_log_reintroduced`.** The record route does not
escape `𝒞`. It re-enters the dichotomy at exactly two points: A1 does not
license "observable = record" (so the route needs an extra identification just to
start), and once started, the record's branch weight is the **multiplicative**
Born probability, so the additive recorded scalar is reached only through
`p ↦ -log p` = (Add) = P1. The free-monoid concatenation length is a real
additive invariant, but it is **inert** for this purpose: making record-**size**
match the continuous `log|det|` readout forces size `∝ -log p` (the same choice),
and the bare integer mark-count is a different (quantized) object that A1 does
not assign. This is positive structural content — it closes the record-ledger
instance of path (a′) and explains **why** (the `-log` is the bridge between the
multiplicative Born weight and any additive recorded scalar) — but it is a
`no_go`, not a closure.

This note explicitly DOES NOT:

- claim P1 is false; `W = log|det(D+J)|` remains the natural physical choice;
- claim #2504's path (a′) is fully foreclosed — only the **record /
  recorded-information ledger** instance of it is closed here;
- claim the free-monoid concatenation-length fact is wrong — it is a reproven
  theorem (runner T3); only the **identification of record-size with a Born
  branch's quantification** is found to re-import the `log`;
- promote or alter the status of
  `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`, #2456, #2504, #2517, the
  `det`-character note, the two-stage synthesis, the Route D consolidated no-go,
  the structural-reframing no-go, the six `retained_no_go` rows, the
  Kraus-instrument / Born-rule rows, the staggered-Dirac realization gate, or any
  upstream row;
- add a new framework axiom or repo-wide vocabulary tag or class name.
  "Record route," "recorded information," "record size," "mark-count,"
  "free-monoid length," "Crux 1/2" are local descriptive labels; "(BLIND),"
  "(ADD)," "(Add)," "(Loc)," "(Pot)," "face," "orbit," "Pattern L," "F_p,"
  "block-diagonal," "independent subsystems" are mapped to the existing
  #2456 / #2504 / structural-reframing vocabulary, not new repo tags.

## 1. Mandatory four exercises

### Exercise 1 — Assumption audit

Each premise consumed, with type and ledger status:

| Premise | Type | Status / source |
|---|---|---|
| One-qubit operator algebra `M_2(ℂ) ≅ Cl(3,0)` at each site; `Z^3` substrate; records/Born are derivation lanes, not axiom content | framework baseline | `MINIMAL_AXIOMS_2026-05-20.md` (runner T6) |
| Amplitude multiplicativity for independent tensor systems; Born `p = |psi|^2` multiplicative (`p_AB = p_A · p_B`) | standard quantum kinematics | reproven runner T1 (modulus-phase form) |
| The record is a Kraus instrument `W = Σ_r K_r ⊗ |r⟩`, branches labeled `{|r⟩}`, quantified by `p_r = Tr(K_r ρ K_r†)` | framework measurement machinery | `PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md` (`retained_bounded`); `BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md` (`audited_conditional`); runner T6 (string presence) |
| `Z[J] = det(D + J)`, modulus `r = |Z|` factorizes on block-diagonal `D` | finite determinant context | imported as in the parent note; same Berezin/Grassmann origin (staggered-Dirac realization gate) |
| `t ↦ t^q` is a homomorphism `(ℝ_+, ×) → (ℝ_+, ×)` for every real `q` | elementary algebra | runner T2 (the exponent-freedom fact) |
| `-log` is the additive coordinate of `(ℝ_+, ×)`; additive + continuous `⇒ c·log` | functional-equation classification | reproven runner T2/T4; Cauchy 1821 / Aczél 1966 comparator only |
| Free-monoid length: `|w₁w₂| = |w₁| + |w₂|`; unique equal-weight homomorphism up to scale | elementary algebra | reproven runner T3; free-monoid length cited as comparator |
| Shannon/Kraft optimal code length `ℓ(p) = -log_b p` for a symbol of probability `p` | information theory | comparator (Shannon 1948); the identification of record-size with `ℓ(p)` is the tested step |

**Decisive observations.**

1. The route consumes two contents beyond standard math and the framework
   baseline: **(R1)** the identification "the physical scalar observable = the
   recorded outcome/information," and **(R2)** the identification "record-size of
   a Born branch = `-log p` (Shannon/Kraft length)." (R1) is **not** licensed by
   A1 (records are a derivation lane, not axiom content; observation 2). (R2) is
   the `-log p` step = (Add) = P1 (observation 3).
2. **Does A1 force (R1)?** No. `MINIMAL_AXIOMS_2026-05-20.md` commits only the
   per-site qubit algebra and `Z^3`; "Dynamics, non-projective measurement
   instruments, records, Born probabilities … are **not additional primitives in
   A1-A2**." The Born-rule note is itself `audited_conditional` (a derivation
   target, not an axiom). So "observable = recorded information" is an
   **additional identification** the route must admit. (R1) does not reduce the
   admitted-premise count; it adds a premise.
3. **Does (R2) escape P1?** No. The recorded branch carries the **multiplicative**
   Born weight `p_r` (runner T1, T6). The candidate recorded scalars form the
   family `Φ_q(p) = p^q` (each multiplicative on independent branches; runner
   T2); the **additive** representative is `q → 0` (`log`), and selecting it is
   the Cauchy classifier whose hypothesis is additivity (runner T2). The
   record's own **Born/normalized** quantification is exponent-blind (returns the
   same field for every `q`; runner T5) — the **(BLIND)** face, which singles
   nothing. So (R2) is either (BLIND) (singles nothing) or (ADD) = P1.

**Conclusion of Exercise 1.** The record route consumes (R1) "observable =
record" (not licensed by A1) and (R2) "record-size = `-log p`" (= (Add) = P1).
It does not reduce the parent note's admitted-premise count; it relocates P1 to
the record's quantification step and adds an identification premise on top.

### Exercise 2 — Elon Musk first-principles

Strip to first principles. The slogan "qubit (probability) until record
(information)" has three moves: (M1) the pre-record state carries an **amplitude**
`psi`, multiplicative on independent tensor systems; (M2) Born gives a
**probability** `p = |psi|^2`, still multiplicative; (M3) a **record** forms and
one reads off **information** `I = -log p`, which is **additive**. The reframe's
force is entirely in M3: the multiplicative→additive switch (the `log`) happens
"at the record," so — the claim goes — additivity is a structural property of the
record, not a chosen readout.

First-principles check: **what, physically, is "the record," and what is additive
about it?**

In the framework the record is the Kraus instrument `W = Σ_r K_r ⊗ |r⟩`: a set
of orthonormal pointer states `|r⟩` carrying the post-measurement classical
labels, with branch weight `p_r = Tr(K_r ρ K_r†)`. The **recorded object** is the
label `r` together with its weight `p_r`. There are exactly two things one can
quantify:

- **the weight `p_r`** — a **counterfactual** assignment over what could have
  happened, **multiplicative** on independent branches (`p_AB = p_A p_B`); this
  is the pre-measurement Born probability, carried through;
- **the "size" of the record** — the number of physical marks. To be a *scalar
  observable comparable to the v-chain* `W = log|det(D+J)|`, this size must be a
  **continuous** real that **adds** over independent sub-records.

Now the decisive fork. To make "record size" the additive scalar M3 wants, the
size of a single Born branch of probability `p` must be set to some `Φ(p)` with
`Φ(p_A p_B) = Φ(p_A) + Φ(p_B)`. **That is the Cauchy equation**, and its
continuous solution is `Φ = c log` — the `-log p` of M3. So "the record's size is
additive" is **not** an independent structural fact about marks; it is the
demand that the size be the additive coordinate of the multiplicative Born
weight, which is **(Add) = P1**. The `log` in M3 is not "located at the record";
it is the **same** selection of the additive representative from the
multiplicative family, relabeled as "information."

What about the **bare** number of marks (the genuine free-monoid length, before
any `-log`)? Concatenating record-A then record-B gives `|A| + |B|` marks: a real
additive invariant (runner T3). But this number is **not** the `-log p` of a Born
branch unless one *defines* the branch to be written with `≈ -log_b p` marks
(Shannon/Kraft) — which is exactly (R2) again. Left as a bare count, it is (i)
**unpinned by A1** (no axiom says how many marks a branch of probability `p`
gets), and (ii) **integer-quantized**, so it **cannot** equal the continuous
`log|det|` v-chain observable (runner T4: `-log_2(1/3)` is irrational). The
free-monoid additivity is real but **inert**: it gives an additive structure on
*words*, but the map *from a Born branch to a word* is precisely where the `log`
re-enters.

**First-principles bottom line.** "Information at the record is additive" is the
`-log` of the multiplicative Born weight = (Add) = P1; the only genuinely
record-native additive object (mark-count) is unpinned by A1 and quantized, hence
not the v-chain observable. The slogan relocates P1 to the record's
quantification step; it does not derive it.

### Exercise 3 — Literature search

External authorities directly relevant:

1. **C. E. Shannon (1948).** "A Mathematical Theory of Communication," *Bell
   Syst. Tech. J.* 27, §6 (entropy uniqueness) and §9 / source-coding (the
   optimal code length `ℓ(p) = -log_b p`, Kraft inequality). **Comparator** for
   the record route: Shannon's information `I = -log p` and the optimal record
   length are *defined* via `log`; the additivity over independent symbols is the
   **hypothesis** (Shannon's property 3), exactly P1. Source coding does not
   derive additivity; it assumes independence and optimizes length to `-log p`.
2. **L. Boltzmann (1877) / M. Planck (1901).** `S = k log W` (entropy as the log
   of the multiplicity). **Comparator**: the `log` converting the multiplicative
   count of microstates `W` into the additive entropy `S` is the **same**
   multiplicative→additive bridge; `S` additive `⟺` `W` multiplicative is the
   Cauchy step. Cited as comparator only.
3. **J. von Neumann (1932).** *Mathematical Foundations of Quantum Mechanics*,
   ch. V-VI (the measurement / projection process; the "cut" between quantum
   system and classical record). **Comparator** for Crux 1: von Neumann's
   measurement introduces the classical record as a **separate postulate** (the
   projection postulate), not as a consequence of the unitary kinematics — paralleling
   the framework's treatment of records as a derivation lane, not an axiom.
4. **Free-monoid length** (standard algebra; e.g. Lothaire, *Combinatorics on
   Words*, 1983, ch. 1). The free monoid `A^*` on alphabet `A` has length
   `|·| : A^* → (ℕ,+)` a monoid homomorphism with `|w₁w₂| = |w₁| + |w₂|`, and it
   is the unique homomorphism to `(ℕ,+)` assigning value 1 to each letter (up to
   scale). **Comparator** for §3.4: concatenation length is genuinely additive,
   but it is an invariant of **words**, not of Born **branches**; reproven in the
   runner, cited only as comparator.
5. **A.-L. Cauchy (1821).** *Cours d'Analyse*, §V; **J. Aczél (1966).**
   *Lectures on Functional Equations and Their Applications*, §2.1 Thm 1. The
   continuous solution of `f(xy) = f(x) + f(y)` on `(ℝ_+, ×)` is `c·log`.
   **Comparator** for the `-log` bridge: additivity is the **hypothesis**.
6. **R. Landauer (1961); C. H. Bennett (1982).** The thermodynamics of a physical
   record / erasure (`kT ln 2` per bit). **Comparator**: the physical record's
   information cost is measured in `log` (bits/nats); the additive ledger of a
   record is the `log` ledger by construction, not independently of it.

**Literature observation.** Every quantification of "recorded information" in the
literature — Shannon information, Boltzmann/Planck entropy, code length,
Landauer cost — measures the record in `log` units and takes additivity over
independent components as the **hypothesis**, never deriving it from a
non-additive structure. The one genuinely non-`log`, additive record invariant
(free-monoid length) is an invariant of words, and is connected to `-log p` only
through the optimal-coding identification, which re-imports the `log`. This
matches the runner's reproven finding.

### Exercise 4 — Math search (Tao-style)

**Pose the bare math problem.** A record of an independent composite branch is a
pair `(r, p)` with label `r` and Born weight `p`, where on independent sub-branches
`p_AB = p_A · p_B` (multiplicative). (i) Classify the additive real "recorded
scalars" `Φ(p)` over independent branches. (ii) Does the free monoid of marks
supply an additive scalar that is **not** of this form and that matches the
continuous v-chain readout? (iii) Is the record's Born quantification able to fix
an exponent at all?

**Math answer.**

- (i) **Additive recorded scalar ⇒ `log`.** `Φ(p_A p_B) = Φ(p_A) + Φ(p_B)` is
  Cauchy on `(ℝ_+, ×)`; continuous solutions are `Φ = c log` (runner T2, T4). On
  the family `Φ_q(p) = p^q` every member is multiplicative and **no** `q ≠ 0` is
  additive (runner T2); the additive representative is `q → 0` (`log`). So "the
  recorded information is additive" **is** the selection of `log` = (Add) = P1.
- (ii) **Free-monoid length is additive but inert.** `|w₁w₂| = |w₁| + |w₂|` and
  length is the unique equal-weight homomorphism `A^* → (ℝ,+)` up to scale
  (runner T3). But to set the v-chain readout `W = log|det(D+J)|` equal to a
  record's mark-count, the branch of probability `p` must be assigned
  `|w(p)| ∝ -log_b p` marks (Shannon/Kraft), which is the `-log p` of (i)
  (runner T4: `size(p) = c(-log p)` is the additive bridge; a non-log monotone
  size such as `1 - p` is **not** additive). A **bare** integer count is
  quantized and cannot equal the continuous `log|det|` (`-log_2(1/3)` is
  irrational; runner T4). So the free monoid gives no additive scalar that both
  escapes `log` and matches the v-chain observable.
- (iii) **Born quantification is exponent-blind.** The normalized/Born gradient
  `(1/q) p^{-q} ∂(p^q)/∂θ = ∂(log p)/∂θ` for **every** `q` (runner T5): the
  record's Born readout singles **nothing** among `{Φ_q}`. Only the **bare**
  (additive-size) selector breaks the tie, and it forces `q·p^q = 1` — the
  `q → 0` (`log`) limit — i.e. it **is** (Add) = P1.

**Math danger flag (per discipline).** The additive-recorded-scalar ⇒ `log`
content **is** the Cauchy classifier; using it to "derive `log`" would be
circular (additivity is the hypothesis). This note does **not** use it to derive
`log`; it uses it to prove the record route **re-introduces** the same choice —
the recorded scalar is additive **iff** it is the `-log` of the multiplicative
Born weight, and the free-monoid escape is inert. That is an honest `no_go`, not
a disguised closure. The circularity is flagged explicitly in §3.6.

**Conclusion of math search.** The recorded-information ledger does not escape
`𝒞`: the additive recorded scalar is `-log p` = (Add) = P1, the record's Born
quantification is BLIND, and the free-monoid concatenation length — though a
genuine additive invariant — does not single out the additive quantification of a
Born branch over the multiplicative one without re-importing the `log`.

## 2. The pipeline and where the choice re-enters

| Stage | Object | Composition on independent tensor branches | Additive? |
|---|---|---|---|
| Pre-record amplitude | `psi` | multiplicative `psi_AB = psi_A psi_B` | no |
| Born probability | `p = |psi|^2` | multiplicative `p_AB = p_A p_B` | no |
| **Record (Kraus branch)** | label `r`, weight `p_r = Tr(K_r ρ K_r†)` | weight multiplicative `p_AB = p_A p_B` | **no** (the weight is still multiplicative) |
| Recorded information | `I = -log p` | additive `I_AB = I_A + I_B` | **yes — but only via the `-log` map = (Add) = P1** |
| Record mark-count (free monoid) | word `w`, length `|w|` | additive by concatenation `|w_A w_B| = |w_A| + |w_B|` | **yes — but the map `branch ↦ word` is `|w(p)| ∝ -log p` (re-imports `log`) or a bare quantized count (not the v-chain observable, unpinned by A1)** |

The pipeline shows the `log` is **not** a structural property of "the record." The
recorded object is the branch `(r, p_r)`, whose weight is **multiplicative**. The
additive line "Recorded information `I = -log p`" inserts the `-log` map by hand,
and that map is exactly the (Add) selection of the additive representative from
`{Φ_q = p^q}`. The free-monoid row is the genuine record-native additive
structure, but it is on *words*, and the bridge from a Born branch to a word is
either the same `-log` (optimal coding) or a bare integer count that is not the
continuous v-chain observable and is not assigned by A1.

## 3. Load-bearing steps

### 3.1 Crux 1 — A1 does not force "observable = record"

`MINIMAL_AXIOMS_2026-05-20.md` states A1 as "Reality is a qubit at every lattice
site," with the equivalent algebraic content "the primitive local operator
algebra is the one-qubit algebra `A_x ≅ M_2(ℂ)`, equivalently `Cl(3,0)`," and A2
as "the lattice sites form `Z^3`." It then states explicitly:

> "Dynamics, non-projective measurement instruments, records, Born
> probabilities, continuum limits, particle sectors, gauge structure, and
> gravity **are not additional primitives in A1-A2**; they enter only through
> their named derivation lanes."

So A1 commits an **operator algebra and a substrate**, not a measurement
ontology. There is no axiom content of the form "physical observables **are** the
recorded outcomes / the post-measurement classical record." The Born rule itself
is a derivation **target** (`BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md`
is `audited_conditional`, and `MINIMAL_AXIOMS` lists it as a "derivation lane").
Therefore the reframe's premise (i) — "A1 is a measurement framework so
observables ARE records/measurement-outcomes" — is an **additional
identification**, not an A1 consequence (runner T6). This alone blocks the
"P1 retained from the measurement axiom" reading: even granting everything
downstream, the route does not derive P1 *from A1*, because it must first admit
observable-=-record.

### 3.2 The framework's record carries the multiplicative Born weight

The framework's record object is the finite Kraus instrument
(`PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md`, `retained_bounded`):
`W = Σ_r K_r ⊗ |r⟩` with orthonormal record basis `{|r⟩}`,
`Σ_r K_r† K_r = I`, and branch weight `p_r = Tr(K_r ρ K_r†)`. The Born-rule
bridge (`BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md`) gives
`p(E) = Tr(ρ E)`. On independent tensor branches the weight is **multiplicative**:
`p_AB = p_A · p_B` (runner T1, reproven in modulus-phase form so `|psi|^2`
factorizes exactly). The recorded object therefore inherits the **multiplicative**
Born weight; it does not come pre-equipped with an additive scalar.

### 3.3 Crux 2 — the additive recorded scalar is the `-log` = (Add) = P1; the Born readout is BLIND

Candidate recorded scalars `Φ(p)` of the branch weight form the family
`Φ_q(p) = p^q`; each is multiplicative on independent branches
(`(p_A p_B)^q = p_A^q p_B^q`, runner T2), and the **additive** member is `q → 0`
(`log`): `I = -log(p_A p_B) = -log p_A - log p_B` (runner T2). No `q ≠ 0` power is
additive (runner T2). Selecting the additive representative is the Cauchy
classifier (`Φ(p_A p_B) = Φ(p_A) + Φ(p_B) ⇒ Φ = c log`), whose **hypothesis is
additivity** — this is **(Add) = P1** verbatim, mapped from the v-chain modulus
`r = |Z|` to the Born weight `p` (the modulus and the probability share the same
multiplicative composition law).

The record's **own** quantification — the Born / normalized readout — is
**exponent-blind**: the normalized gradient
`(1/q) p^{-q} ∂(p^q)/∂θ = ∂(log p)/∂θ` for **every** `q` (runner T5). It returns
the same expectation field independent of `q`, so it singles **nothing** among
`{Φ_q}`. This is the **(BLIND)** face of #2504. Only the **bare**
(additive-size) selector breaks the tie, and it forces `q·p^q = 1`, i.e. the
`q → 0` (`log`) limit = (Add) = P1 (runner T5). Hence the record route lands in
**(BLIND)** (Born quantification, singles nothing) or **(ADD) = P1** (the `-log`
recorded size) — the BLIND-or-ADD dichotomy, with no third option.

### 3.4 The free-monoid concatenation-length fact (reproven; comparator)

**Statement.** Let `A` be a finite alphabet and `A^*` the free monoid of words
under concatenation. The length map `|·| : A^* → (ℕ, +)` satisfies
`|w₁ w₂| = |w₁| + |w₂|` (it is a monoid homomorphism), and it is the **unique**
homomorphism `A^* → (ℝ, +)` (up to overall scale `c`) that assigns equal value to
each single letter.

**Reproof (runner T3).** Additivity holds for all word pairs over a finite test
alphabet (`|w₁ w₂| = |w₁| + |w₂|` checked exhaustively). For uniqueness: an
arbitrary per-letter weighting `wt : A → ℝ` extends to the homomorphism
`h(word) = Σ_{letters} wt(letter)`; requiring `h(word) = c·|word|` on the test
words has the unique solution `wt(letter) = c` for every letter (SymPy `solve`),
so `h = c·|·|`, unique up to scale. Free-monoid length is cited (Lothaire 1983)
only as comparator; the additivity and uniqueness are reproven here.

This is a **genuine** additive, unique-up-to-scale invariant — the strongest
form of the reframe's premise (ii). The next subsection shows it is nonetheless
**inert** for deriving the v-chain additive readout.

### 3.5 The free-monoid kernel is inert: size = `-log p` (re-imports `log`) or a quantized non-observable

To use the free-monoid length as the physical scalar observable comparable to the
v-chain `W = log|det(D+J)|`, one must specify the map **`branch ↦ word`**: how
many marks a Born branch of probability `p` is recorded with. Two options:

- **Size `= -log_b p` (Shannon/Kraft optimal length).** Then
  `size(p) = c·(-log p)` and `size(p_A p_B) = size(p_A) + size(p_B)` (runner T4)
  — additivity holds **because** `-log` is the additive coordinate of
  `(ℝ_+, ×)`. This is the **same** (Add) = P1 step of §3.3. The `log` is back. A
  non-`log` monotone size such as `g(p) = 1 - p` is **not** additive over
  independent branches (runner T4), confirming additivity singles out `log`.
- **Size `=` bare integer mark-count.** This is (a) **not pinned by A1** — no
  axiom assigns a mark-count to a branch of probability `p` (Crux 1: records are
  a derivation lane); and (b) **integer-quantized**, so it **cannot** equal the
  continuous v-chain `log|det|` readout — e.g. `-log_2(1/3) = log 3 / log 2` is
  irrational (runner T4). It is a **different object** (an integer record length,
  not the continuous v-chain observable), and even as such it is unpinned by A1.

Either way, the free-monoid additivity does not single out the additive
**quantification** of a Born branch over the multiplicative one without
re-importing the `log` (option 1) or leaving the v-chain observable behind and
A1-unpinned (option 2). The kernel is real but inert.

### 3.6 Where the choice re-enters (circularity, flagged)

The `-log` re-enters at the **map from a Born branch to its recorded scalar**.
The record carries the **multiplicative** Born weight `p_r` (§3.2). Any
**additive** recorded scalar over independent branches is, by Cauchy,
`Φ = c log` (§3.3) — this is the `-log p` of the slogan's M3 and the
`size = -log_b p` of the free-monoid option 1 (§3.5). The record picture
relocates the multiplicative→additive selection from "the v-chain generator
`F_p = |det|^p`" to "the recorded scalar of a Born branch `Φ_q(p) = p^q`," but it
is the **same** selection of the additive representative `q → 0` (`log`) from a
multiplicative family — **(Add) = P1**. The circularity is explicit: the
additive-recorded-scalar ⇒ `log` content **is** Cauchy/Shannon-Khinchin; the
result proven here is **circularity (re-description)**, not a derivation of
`log`.

### 3.7 Time supplies no extra escape

Two roles of time, distinguished cleanly:

- **(a) time-as-generator.** In the framework's realized free quadratic sector
  the Hamiltonian is `Ĥ = -log(T̂²)/(2a_τ)`
  (`OBSERVABLE_PRINCIPLE_P1_SYMMETRY_TYPE_ENERGY_READOUT_NARROW_NOTE_2026-06-02.md`,
  #2517, referenced textually): "energies add" `⟺` "`T̂²` multiplicative" is the
  same `exp`/`log` move one level up. This is the #2517 circularity; it does
  **not** help here.
- **(b) time-as-recording-sequence.** Records accumulate along derived time: each
  Born click appends a mark, so the running record is a word and its length is
  additive by concatenation. This is **exactly** the free-monoid structure of
  §3.4 — additive in **mark-count**. But the mark-count contributed by a single
  Born click of probability `p` is again the `-log p` assignment (§3.5, option
  1), or a bare quantized count (option 2). So (b) supplies the genuine
  free-monoid additive structure but **not** a non-circular additive
  quantification of a Born branch: it reduces to the same `-log` choice (option
  1) or the A1-unpinned quantized count (option 2).

Both time roles reduce to the `-log` choice. Time does not open a new path-(a′).

## 4. What this closes / what remains admitted

### 4.1 What this closes (positive content despite negative outcome)

- **Closes the record / recorded-information ledger instance of #2504's path
  (a′).** The most physically appealing remaining path-(a′) candidate — that a
  **record** supplies additivity by concatenation, not by a `log`-of-probability
  choice — does not escape `𝒞`. It re-enters at (BLIND) (Born quantification) or
  (ADD) = P1 (the `-log` recorded size).
- **Identifies the exact circularity point.** The `-log` re-enters at the **map
  from a Born branch to its recorded scalar** (§3.6): the record carries the
  multiplicative Born weight, and any additive recorded scalar is the `-log` =
  (Add) = P1. The "switch happens at the record" slogan relocates the choice; it
  does not remove it.
- **Isolates the genuinely-additive free-monoid kernel and proves it inert.** The
  concatenation length is a real additive, unique-up-to-scale invariant (§3.4,
  reproven), but the map `branch ↦ word` is either `-log p` (re-imports `log`) or
  a quantized non-observable unpinned by A1 (§3.5). This is the precise residual
  the task asked for: single-record physical **size** is **not** additive
  *independently of* the `log`-of-probability choice in any way that yields the
  continuous v-chain observable.
- **Confirms Crux 1 (A1 ≠ measurement ontology).** A1 commits the per-site
  algebra and `Z^3` only; "observable = record" is an additional identification,
  so the route cannot derive P1 *from A1* even granting the downstream steps.

### 4.2 What remains admitted

- **P1 itself** (the exponent-fixing additivity step) remains an admitted
  physical-principle selection premise of `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`.
  This note does not retire it; it pins the record route to it.
- The parent note's audit row keeps its live ledger status
  (`audited_conditional`); this `no_go` provides additional structural backing.

### 4.3 Forward paths (out of scope of this note)

- **(a′)** of #2504 remains open for primitives that introduce a privileged scale
  by a mechanism that is **neither** a sector-composition selector **nor** the
  energy/free-energy ledger (#2517) **nor** the record / recorded-information
  ledger (this note). No such primitive is identified.
- **(b)** Accept P1 (the exponent-fixing step) as a permanent classification
  premise (current state of the parent note).

### 4.4 No-Go Discipline Gate

**Status:** PASS for this narrow negative route claim. The negative claim is not
"P1 is impossible" and not "no route exists"; it is that the **record /
recorded-information** route re-introduces the same `-log` = (Add) = P1 choice and
does not derive P1 from A1.

**N1 — Alternative route enumeration.**

| Route tested against the negative claim | Marker | Why it does not break this narrow no_go |
|---|---|---|
| "Observable = record" from A1 | RULED OUT BY CONTEXT | A1 commits only the per-site algebra + `Z^3`; records are a derivation lane (Crux 1; runner T6). |
| Recorded information `I = -log p` is additive | ATTEMPTED | The `-log` is the additive coordinate of the multiplicative Born weight = (Add) = P1 (runner T2). |
| Record-size = number of marks (free-monoid length) | ATTEMPTED | Additive on words, but `branch ↦ word` is `-log p` (re-imports `log`) or a quantized non-observable unpinned by A1 (runner T3/T4). |
| Born / normalized quantification of the branch | RULED OUT BY PRIOR CONTEXT | Exponent-blind = (BLIND); singles nothing (runner T5; #2504). |
| time-as-recording-sequence | ATTEMPTED | Free-monoid concatenation; mark-count of a Born click is the `-log p` assignment (§3.7). |
| time-as-generator `H = -log(T²)` | RULED OUT BY PRIOR CONTEXT | The #2517 circularity, one level up; does not help here. |
| Convention/reframe accepting P1 as a classification premise | OPEN FOR USER/REPO POLICY | Names/ratifies the premise; not a derivation. |

**N2 — Wall-independence audit.** The walls collapse to one load-bearing wall:
the recorded scalar of a Born branch is additive **iff** it is the `-log` of the
multiplicative Born weight = (Add) = P1, and the free-monoid escape is inert.
Crux 1 (A1 ≠ measurement ontology) is a separate, independent blocker on the
"derive from A1" reading.

**N3 — Hidden-wall scan.** "Record," "information," "mark-count," "free-monoid
length," "Born weight," "concatenation," "(BLIND)," "(ADD)" are used as standard
terms / mapped to existing #2456-#2504 vocabulary. The `-log p` identification is
explicitly named as the tested step, not smuggled in as retained framework
content. The load-bearing result is the elementary Cauchy / exponent-blindness /
free-monoid algebra, not the audit status of any framework row named for
orientation.

**N4 — Residual matching.** The residual attacked is exactly "make the recorded
scalar of a Born branch additive without the `-log`-of-probability choice."
Pattern-L references are used only where the residual is additivity selection;
the free-monoid length is kept separate and is shown inert, not used as a witness
against itself.

**N5 — Rhetoric audit.** The claim is at the record-route resolution. It does not
assert a lattice-wide no-go, a per-site no-go, or a no-go against the free-monoid
length fact (which is a theorem), nor against a hypothetical new path-(a′)
primitive outside the record/energy/sector-composition classes.

**N6 — Partial-closure path scan.** A convention/reframe path remains: the repo
may accept the exponent-fixing step as a named classification premise. This is
not called a new axiom and is not foreclosed; it is simply not a derivation.

**N7 — Steelman.** A hostile reviewer could propose that the bare integer
mark-count, taken as the *fundamental* observable (replacing the continuous
`log|det|` v-chain readout), is additive and `log`-free. That would not
contradict this note: it would be a **different** observable (an integer record
length), it would still need an A1-licensed assignment of marks to branches
(Crux 1), and it would not reproduce the framework's continuous v-chain readout
(runner T4 quantization witness). It is a genuinely new primitive that must be
stated and audited separately; this note does not claim such a primitive is
impossible, only that the record route as posed (recovering the v-chain additive
readout) re-imports the `log`.

**N8 — Cross-cycle echo.** The same wall shape appears in Route D, the
structural-reframing (cumulant/free-energy), the locality / extensivity no-gos,
and the energy-readout note (#2517). None has been retired by a retained selector
or primitive outside the additive class. This note adds the record /
recorded-information ledger to that list and isolates the free-monoid kernel as
inert; it does not claim universal P1 impossibility.

## 5. Comparison with route portfolio

| Route | Axis / mechanism | Outcome | Relation to this note |
|---|---|---|---|
| Route D consolidated no-go | direct-sum `F_p` selection | no_go | this note pins another candidate Route D leaves at "P1 admitted" |
| Structural reframing (cumulant / free energy) | `W = log Z` identification = (II.b) | `retained_no_go` | the recorded-entropy `-Σ p log p` is the same (II.b); subsumed |
| Exponent-fixing irreducibility (#2456) | (Add)⇔(Loc)⇔(Pot) + Born exclusion | no_go | supplies (Add)=P1 and the Born-BLIND fact this note reuses |
| Exponent-selector dichotomy (#2504) | BLIND-or-ADD over class `𝒞` | no_go | the record route lands in BLIND or ADD; tests path (a′) |
| Energy-readout (#2517) | energy/free-energy ledger | no_go | sibling path-(a′) closure; this note closes the record ledger instead |
| **This note — record / recorded-information ledger** | **Kraus branch weight (multiplicative) → recorded scalar; free-monoid length** | **no_go (`circular_log_reintroduced`)** | **closes the record-ledger instance of path (a′); isolates the free-monoid kernel as inert; Crux 1 blocks "derive from A1"** |

**Structural distinction.** Prior notes attacked selectors (#2456), the selector
class (#2504), and the energy ledger (#2517). This note attacks the **record /
information ledger** — the framework's own "qubit→record" slogan — and finds
the additive recorded scalar is the `-log` of the multiplicative Born weight =
(Add) = P1, with the free-monoid concatenation length isolated and proven inert
(additive on words, but the `branch ↦ word` map is `-log p` or an A1-unpinned
quantized non-observable). Plus the independent Crux 1: A1 does not license
"observable = record."

## 6. Hypothesis set used (forbidden-imports check)

The note uses only:

- Elementary quantum kinematics: amplitude multiplicativity for independent
  tensor systems; Born `p = |psi|^2` multiplicative.
- The framework's Kraus-instrument record structure and Born-rule bridge
  (`PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md`,
  `BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md`) as **context**;
  their audit statuses are not consumed as load-bearing.
- Elementary algebra `t ↦ t^q` homomorphism (exponent-freedom) and `-log` as the
  additive coordinate of `(ℝ_+, ×)`.
- Free-monoid concatenation-length additivity and uniqueness (reproven; Lothaire
  1983 comparator).
- The Cauchy classifier (Cauchy 1821; Aczél 1966) and Shannon information /
  source-coding length (Shannon 1948), Boltzmann/Planck `S = k log W` — **all
  comparator only**.
- A1's content from `MINIMAL_AXIOMS_2026-05-20.md`.

No fitted parameters. No observed values. No PDG comparators. No new framework
axiom (per `feedback_no_new_axioms.md`). No new repo-wide vocabulary tag or class
name (per `feedback_no_new_repo_vocabulary.md`); only repo-canonical terms and
the existing #2456 / #2504 / structural-reframing vocabulary. No promotion of any
cited framework note's audit status.

## 7. Forbidden imports check

- No PDG observed values consumed.
- No literature numerical comparators consumed (Shannon / Boltzmann / Cauchy /
  free-monoid length are cited as comparators, not as derivation inputs; all
  load-bearing facts are reproven in the runner).
- No fitted selectors consumed.
- No admitted unit conventions load-bearing on the claim.
- No same-surface family arguments.
- No new repo vocabulary or class tags.

## 8. Reproduction

```bash
python3 scripts/audit_companion_observable_principle_p1_record_information_route_2026_06_03.py
```

Expected scorecard: `PASS=N, FAIL=0` at exact SymPy precision. A passing run
supports only the bounded finding above (verdict `circular_log_reintroduced`): A1
does not force observable=record; the framework's record quantifies branches by
the multiplicative Born weight, and the `-log` that makes the recorded scalar
additive is the same free choice as P1 (the (Add) face); the free-monoid
concatenation length, though genuinely additive and unique up to scale, does not
single out the additive quantification of a Born branch over the multiplicative
one without re-importing the `log`. It does **NOT** close P1, does **NOT** promote
any framework row, and consumes no fitted or observed numerical targets.

## 9. Validation

Primary runner:
[`scripts/audit_companion_observable_principle_p1_record_information_route_2026_06_03.py`](../scripts/audit_companion_observable_principle_p1_record_information_route_2026_06_03.py)
verifies at exact SymPy / Fraction precision:

- **T1** independent tensor branches → Born probability is multiplicative
  (`p_AB = p_A · p_B`); the v-chain modulus `r = |det(D+J)|` factorizes on
  block-diagonal `D` (the same multiplicative pre-record structure).
- **T2** information additivity `I = -log p` (`I_AB = I_A + I_B`); on
  `{Φ_q = p^q}` every member is multiplicative on independent sectors and no
  `q ≠ 0` power is additive — the additive representative is `q → 0` (`log`) =
  (Add).
- **T3** free-monoid concatenation length additivity `|w₁w₂| = |w₁| + |w₂|` and
  uniqueness up to scale (the equal-weight homomorphism is `c·|·|`).
- **T4** the `-log` identification is the bridge: `size(p) = c(-log p)` is
  additive over independent branches (the same Cauchy step), a non-`log` monotone
  size is not additive, and the bare integer mark-count cannot equal the
  continuous `log|det|` readout (`-log_2(1/3)` non-integer).
- **T5** the record's Born / normalized readout is exponent-blind
  (`(1/q) p^{-q} ∂(p^q)/∂θ = ∂(log p)/∂θ` for all `q`; the BLIND face); only the
  bare additive-size selector breaks the tie and it is (Add) = P1.
- **T6** A1 commits only the per-site qubit algebra + `Z^3`; records / Born are
  derivation lanes; the record quantifies branches by Born
  `p_r = Tr(K_r ρ K_r†)`, not a primitive mark-count.
- **T7** live-ledger context presence (no dependency status consumed).
- **T8** note honest-scope strings present; forbidden status-promotion / overclaim
  strings absent.
- **T9** source-note boundary declarations present.

## 10. Cross-references

Load-bearing (markdown-linked) authorities: **none** — the load-bearing content
is the elementary Cauchy / exponent-blindness / free-monoid SymPy algebra plus
A1's content; the framework rows below are target/context only and their audit
statuses are not consumed.

- `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`
  — parent broad row whose P1 admitted premise this no_go pins. Its audit status
  is unaffected by this row.
- `MINIMAL_AXIOMS_2026-05-20.md`
  — A1/A2 content (records/Born are derivation lanes, not axiom content; Crux 1).
- `PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md`
  — the framework's record object (Kraus instrument; branch weight
  `p_r = Tr(K_r ρ K_r†)`). Context only.
- `BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md`
  — the Born-rule bridge `p(E) = Tr(ρ E)`. Context only.
- `OBSERVABLE_PRINCIPLE_P1_EXPONENT_FIXING_IRREDUCIBILITY_NARROW_NOTE_2026-05-31.md`
  — #2456; supplies (Add)=P1 and the Born-BLIND fact reused here.
- `OBSERVABLE_PRINCIPLE_P1_BRIDGE_STRUCTURAL_REFRAMING_NARROW_NOTE_2026-05-21.md`
  — `retained_no_go`; the recorded-entropy / free-energy identification is (II.b)=P1.
- `OBSERVABLE_PRINCIPLE_P1_BRIDGE_ROUTE_D_SHARPENED_NO_GO_NOTE_2026-05-17.md`
  — Route D consolidated no-go that this note pins another candidate to.

Textual references (not markdown-linked, to avoid dangling citation edges to
branch-only notes):
`OBSERVABLE_PRINCIPLE_P1_EXPONENT_SELECTOR_DICHOTOMY_NARROW_NOTE_2026-06-02.md`
(#2504; BLIND-or-ADD dichotomy, class `𝒞`, path (a′)) and
`OBSERVABLE_PRINCIPLE_P1_SYMMETRY_TYPE_ENERGY_READOUT_NARROW_NOTE_2026-06-02.md`
(#2517; energy-ledger path-(a′) closure; `H = -log(T²)` one-level-up circularity).

External mathematics (cited inline as comparator, not as derivation input):
C. E. Shannon (1948) §6, §9; L. Boltzmann (1877) / M. Planck (1901) `S = k log W`;
J. von Neumann (1932) ch. V-VI; M. Lothaire (1983) ch. 1 (free-monoid length);
A.-L. Cauchy (1821) §V; J. Aczél (1966) §2.1 Thm 1; R. Landauer (1961);
C. H. Bennett (1982).

### Source-note boundary

**Hypothesis set used:** (1) amplitude/probability multiplicativity on
independent tensor systems (elementary); (2) the Kraus-instrument record weight
`p_r = Tr(K_r ρ K_r†)` (framework context, status not consumed); (3) `t ↦ t^q`
homomorphism and `-log` as the additive coordinate of `(ℝ_+, ×)` (elementary);
(4) free-monoid concatenation-length additivity + uniqueness (reproven;
comparator); (5) A1's content from `MINIMAL_AXIOMS_2026-05-20.md`. The physical
identification of the readout with `det(D+J)` is not assumed closed — it remains
gated by the staggered-Dirac realization gate, as in the parent note.

**Forbidden-imports check:** this note introduces **no** new framework axiom and
**no** new repo vocabulary or class tags. It uses only standard mathematical
terms and the repo-canonical "(Add)," "(Loc)," "(Pot)," "(BLIND)," "(ADD),"
"Pattern L," "F_p family," "independent subsystems," "block-diagonal." It does
**not** introduce a new ledger-class label or any parent-framing class.

**No-promotion statement:** this note does **not** promote, demote, or set the
audit status of `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`, the record / Born-rule
rows, #2456, #2504, #2517, the structural-reframing no-go, the Route D
consolidated no-go, the six `retained_no_go` rows, the staggered-Dirac
realization gate, or any other upstream row. The audit lane is the only status
authority.
