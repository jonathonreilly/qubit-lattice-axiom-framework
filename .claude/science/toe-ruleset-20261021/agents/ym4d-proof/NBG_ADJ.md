# NBG_ADJ.md — adjudication of the (N-bg) / (G♯_0-field) / (GAP-Z) obstruction count

Worker: T55-K (adjudicator). Lane: ym4d-proof. Session 25.

---

## §0. PRE-STATED — statements only

**This is the first edit to this file. UTC 2026-10-28T21:33:53Z.**

This section cites nothing produced in session 25 except the names of the two files placed under
adjudication: `NBG_A.md` and `NBG_B.md`. It contains no derivation, no constant, and no verdict.
Everything below it was written after it.

### §0.1 What this file is for

Two workers attacked the same question in parallel without reading each other. One reports that
(N-bg), (G♯_0-field) and (GAP-Z) are **one** obstruction; the other reports **three**. This file rules
on the count and on the dependency structure behind it. It does not prefer a status label: a PROVEN
outranks an ARGUED only if its proof survives reading.

### §0.2 Targets, stated before any work

- **(T-K1)** Decide whether **(GAP-Z)|_{Z=1} = M** of LINEAR_PACKAGE Theorem 4.2′, by reading
  (GAP-Z)'s own definition in BFT_B.md and Theorem 4.2′ in LINEAR_PACKAGE.md. The step that can fail
  is **admissibility of Z = 1 inside (GAP-Z)'s own quantifier**; (T-K1) is decided only if that step
  is checked explicitly and separately.
- **(T-K2)** Decide whether **(N-bg) ⟵ (GAP-Z)** (the reduction claimed on the (N-bg) side) survives,
  by reading the three hypotheses of the theorem that carries it and checking whether the hypothesis
  the reduction's author could not prove is doing the work. A reduction whose unproven hypothesis
  already entails the conclusion is **circular** and does not reduce anything; a reduction whose
  unproven hypothesis is strictly weaker than the conclusion is a genuine reduction.
- **(T-K3)** Evaluate **all six ordered implications** among the three items, in both directions, each
  one against the quantifiers its *consumer* needs rather than the quantifiers the source statement
  asserts. A single surviving implication changes the count.
- **(T-K4)** State the **count** and the **dependency graph**: which item implies which, under what
  named hypotheses, and how many genuinely independent items remain.
- **(T-K5)** Attribute. For each worker, state which specific claim survives and which does not, and
  say explicitly where an argument is right while the count built on it is wrong.
- **(T-K6)** Rule on whether PROOF.md's [S25-fix 2] stands or must be reversed, and if it must be
  reversed, supply append-ready replacement text in a `## FOR OTHER FILES (not edited)` section,
  since PROOF.md is the lead's to edit.

### §0.3 Named failure modes for this adjudication, stated in advance

- **ADJ-F1 (too convenient).** The hypothesis that "both are right, the answer is two" is attractive
  because it costs neither worker an argument. It fails if the reduction of (T-K2) and the
  non-identity of (T-K1) cannot both be true of the *same* (GAP-Z) — i.e. if the (GAP-Z) that (N-bg)
  reduces to is not the (GAP-Z) whose restriction to Z = 1 is M. If the lane carries two (GAP-Z)s,
  the count is not two and the convenient answer is wrong.
- **ADJ-F2 (label deference).** Ruling for the PROVEN over the ARGUED without re-deriving the PROVEN.
  Controlled by requiring that (T-K1) be settled from the primary definitions, not from either
  worker's quotation of them.
- **ADJ-F3 (line-number drift).** Every cite verified by **string**, never by line number. A cite that
  no longer says what the citing file claims is reported as a defect of the citing file.
- **ADJ-F4 (phrase collision inherited).** Both workers may share one ambiguous phrase, in which case
  the disagreement is verbal and the count question is ill-posed until the phrase is split. If this
  occurs, the ruling must split the phrase and then count.
- **ADJ-F5 (counting units).** "Obstruction" is itself undefined. The count depends on whether one
  counts *statements*, *unproven inputs*, or *paper-scale tasks*. If the two workers are counting in
  different units, that must be said and the count given in all units used.

### §0.4 Admissible outcomes, enumerated before looking

Exactly one of: **ONE** (all three collapse), **TWO** (reduction holds, identity fails), **THREE**
(no implication survives), or **ILL-POSED-THEN-N** (the question is verbal, resolved by splitting a
phrase, after which the count is N). Any other outcome is a failure of this adjudication to decide
and must be reported as such.

### §0.5 Scope and process

Writes only `NBG_ADJ.md` and `checks/ad1_*`. Reads anything. No git. Appends only. If a numeric or
symbolic check is run, criteria are pre-registered in `checks/ad1_*_criteria.md` before the script is
written, and every gate carries a designed-FAIL control whose firing is reported.

---

## §1. Method, and the citation audit the scope forced

Everything below is located **by string**. T55-C (`SYMBOLS.md` §13) records that PROOF.md's line numbers
moved **+79** since the session-24 files cited them and **+25 again** during that audit, non-uniformly.
I re-resolved every cite that either worker leans on. Result:

| cite, as the citing file writes it | resolves? | note |
|---|---|---|
| BFT_B l.4334 — the (GAP-Z) definition | **YES**, exact | in §38.1, the definitions block |
| BFT_B l.4590 — *"the `M` half, with no decay claimed"* | **YES**, exact | in §41.5 (ii) |
| BFT_B l.4594 — *"it is lane A's `U = 1` package at `Z ≠ 1`"* | **YES**, exact | §41.5 (iii) |
| BFT_B l.4737 — the (GAP-Z) table row | **YES**, exact | §41.7 table |
| BFT_B l.3840 — *"Status quoted: OPEN, lane A's U = 1 package"* | **YES**, exact | §32.2 item 1 |
| RTARGET l.654 — *"(G♯_0-field) not attempted"* | **YES**, exact | §37 |
| NORMS l.629 — (N-bg) | **YES**, exact | Remark N6-5 |
| NORMS l.631-634 — the (I3)(I4)(I5) ↔ BFT-5 sentence | **YES**, exact | route (i) |
| NORMS l.656-657, l.658-663 — θ_A, the N1-15 windows | **YES** | used by check ad1 |
| **PROOF l.3588** — *"(G♯_0-field): not attempted"* | **NO — the string is at l.3614** | **drift +26.** Cited this way by NBG_B §6.1, by the T55-E ledger entry, **and by PROOF.md's own [S25-fix 2]**, which therefore contains a cite into itself that is 26 lines off |

**Finding A1 (PROVEN, a reading).** The one drifted cite in the disputed material is **PROOF l.3588 →
l.3614**. The quoted words are unchanged, so no claim depends on it; it is a defect of the pointer, and
it is now inside PROOF.md itself. Correction supplied in §7.

**Finding A2 (PROVEN, a reading).** The phrase *"lane A's `U = 1` package"* occurs at **three** sites in
BFT_B.md with **two** meanings: l.3840 (= **(G♯_0-field)**, OPEN), l.4334 and l.4594 (= **LINEAR_PACKAGE**,
PROVEN/frozen). The l.4594 occurrence is backticked (`` `U = 1` ``), so a plain-text grep for the phrase
misses it — which is how a phrase collision survives a symbol audit. **NBG_B §12's diagnosis is confirmed
from the primary source, and the site count is three, not two.**

---

## §2. (T-K1) Is (GAP-Z)|_{Z=1} really M? — ruling

### §2.1 The step the lead flagged does NOT fail: Z = 1 is admissible

The scope prompt named this as the step that could break the refutation. It does not break.

- (GAP-Z)'s quantifier is *"uniform in k, T and in Z **over the class considered**"* (BFT_B l.4334).
- The class is **𝒦(ε) := {V : f_k(V) ≤ ε}** (BFT_B l.2865), and Theorem TRANSP is stated *"On the class
  `𝒦(ε)` with `ε ≤ ε_1`"* (BFT_B l.4600-4601). The trivial field has f_k = 0 ≤ ε, so **V = 1 ∈ 𝒦(ε)** for
  every ε ≥ 0; it is the interior point of a smallness class, not an excluded boundary case.
- BFT_B §38.1 supplies the specialisation explicitly: *"At Z = trivial these are §15.0's λ_X^E, a_X, Λ,
  Π_E, S_E"* — the covariant slice objects are **defined** so that Z = trivial returns the flat ones.
- §41.5 (ii) frames (GAP-Z) as one of the two halves into which *"Theorem 4.2′'s two conclusions
  separate"* at a background, i.e. as the Z-deformation of a statement that exists at Z = 1.

**Ruling (PROVEN): restricting (GAP-Z) to Z = 1 is legitimate.** The quantifier admits it, the
definitions specialise to it, and the surrounding text treats Z = 1 as the base case. **NBG_B's step 1
survives the attack the lead aimed at it.**

### §2.2 But (GAP-Z) is not one statement — it is three

The refutation's step 1 reads (GAP-Z)'s *gloss*. Its defining sentence contains two characterisations
joined by *"equivalently"*, and they are not equivalent; a third reading is in circulation in NBG_A.

| reading | text | what it says at Z = 1 | status at Z = 1 |
|---|---|---|---|
| **(α)** operative clause, BFT_B l.4334 | *"a bound … on the kernel of the gauge-fixed composite chain Hessian at Z — **equivalently** a k-, T-uniform lower bound for 𝓛_Z on the slice"* | a k-, T-uniform **coercivity of 𝓛_1 on S_E** — a multi-level composite-slice physical gap, controlling the **configuration** | **not located as proven.** Proposition PG^{(k)} (PROOF l.3137) is PROVEN but is *"a one-step composite"* (PROOF l.3615), not the multi-level statement |
| **(β)** §41.5 (ii), BFT_B l.4590 | *"the **`M` half**, with no decay claimed"*, after *"Theorem 4.2′'s two conclusions separate"* | Theorem 4.2′ (i) minus the strip: the B_k-symbols of r_{k−1} and f_0 bounded by M | **PROVEN** (LINEAR_PACKAGE Thm 4.2′, frozen v1.1) |
| **(γ)** NBG_A §A4.1's *"(H3) M half"* | `sup|f_0^Z| ≤ C_f sup|d^Z_kB_k|`, `sup|r^Z_{k−1}| ≤ C_R sup|d^Z_kB_k|` | the **(I3)** sup bounds — NORMS l.116-118 = LINEAR_PACKAGE **Theorem 3.8**, an ℓ^∞→ℓ^∞ statement | **PROVEN** (Thm 3.8) |

**Finding A3 (PROVEN, a reading).** (α) and (β) are different statements. (β) bounds the symbols of two
**gauge-invariant outputs** (r_{k−1}, f_0); (α) is a coercivity of the gauge-fixed operator on the slice
and so controls the **configuration**. The word *"equivalently"* at BFT_B l.4334 asserts an equivalence
that is not available: a bound on two response symbols does not give a lower bound for 𝓛_Z on the slice,
and a slice gap is not a bound on those two symbols. **(γ) is a third object:** an ℓ^∞→ℓ^∞ bound (hence
an ℓ¹ statement about the kernel) against (β)'s ℓ² symbol bound. **So the lane carries three
inequivalent objects under the one name (GAP-Z)** — systemic defect 1 again, now inside a single
defining sentence. (This is also the weak form of my pre-stated **ADJ-F1**, and it OCCURS: the (GAP-Z)
that T55-D reduces (N-bg) to is (γ), while the (GAP-Z) whose Z = 1 restriction T55-E tests is (β)/(α).)

### §2.3 Ruling on T-K1

**The non-identity (GAP-Z) ≠ (G♯_0-field) is upheld, and it is robust across all three readings.**

- Under **(β)** — which is BFT_B §41.5 (ii)'s own framing, and the dominant intent, since that section
  exists to *split* Theorem 4.2′ — NBG_B's three-line argument is **sound as written**: Z = 1 is
  admissible (§2.1), (GAP-Z)|_{Z=1} is M, M is PROVEN, (G♯_0-field) is not attempted, so they are not one
  statement. **PROVEN.**
- Under **(γ)** the same argument runs with Theorem 3.8 in place of 4.2′. **PROVEN.**
- Under **(α)** the status argument **fails** — (α)|_{Z=1} is not located as proven anywhere — and the
  conclusion must be carried by structure instead. It is, decisively, by §2.4.

### §2.4 A refutation that needs neither the "M" gloss nor any banked PROVEN

This is the argument I would put in the ledger, because it survives reading (α), survives a downgrade of
Theorem 4.2′, and is checkable in two lines from PROOF.md alone:

> **(G♯_0-field) is strictly more than a gap.** PROOF l.3614-3615: *"**(G♯_0-field): not attempted.** It
> needs, **in addition**, the abelian multi-level (per-level slice) physical gap, which is not PG^{(k)}"*
> — and PROOF l.3613: *"**(G♯_0-fine) is also needed for (G♯_0-field)**"*. PROOF l.5069 states the same
> decomposition as an order of work: *"(G♯_0-field): the abelian multi-level per-level-slice gap (PG at
> every level with the effective energies E_i, via E-low), **then the Hölder field bound**."*
>
> So **(G♯_0-field) = [multi-level per-level-slice gap] + [(G♯_0-fine), a Campanato/Hölder bound]**.
> (GAP-Z) is at most the first, and on a different slice (composite S_E against the per-level h^{(i)} = 0
> with Feynman terms, RTARGET l.599-600); it explicitly disclaims the second (*"with **no decay**
> claimed"*, twice, l.4334 and l.4590). And (G♯_0-fine) is OPEN for a reason that has nothing to do with
> any gap: PROOF l.3612, *"the source-to-f_0 symbol with K ≠ 0 aliases has not been shown analytic in a
> strip"*. **Therefore (GAP-Z)|_{Z=1} ⇏ (G♯_0-field), at any reading of (GAP-Z).** ∎

**Status: PROVEN.** It names the missing sub-item — **(G♯_0-fine)** — which neither worker did.

### §2.5 Where NBG_B's §6.2 table overreaches

Two of its five rows are reading-dependent and should not be quoted as unconditional:

- **"output class: gauge-variant configuration vs gauge-**invariant** outputs".** True under (β). **False
  under (α)**, where a slice coercivity controls the configuration. The row mixes horns.
- **"extra input: … vs *none named*".** False under (α), where (GAP-Z) **is** a gap statement.

The three rows that survive every reading are **slice**, **norm type / decay**, and — the one that should
be added — **the missing (G♯_0-fine) half**. The **background** row is not a mismatch at all once one
restricts to Z = 1, which is the only way the two can be compared. **NBG_B's §12 dilemma is therefore not
airtight as written** (horn 2 keeps only three of its four mismatches); the conclusion is unaffected,
because three suffice and §2.4 is independent of both horns.

---

## §3. (T-K2) Theorem NB-5's reduction: non-circular, real — and not a reduction to (GAP-Z)

### §3.1 Is (H3) doing the work?

The scope prompt asked whether (H3), the hypothesis T55-D could not prove, makes the reduction trivial or
circular. **It does not.**

- **Not circular.** (N-bg) bounds **D³**E_k^br(V) — a third derivative. (H3) bounds **first**-order
  response maps (ζ^c(V), f_0^Z, r^Z_j). A first-order hypothesis cannot contain a third-order conclusion,
  and the induction is well-founded (NBG_A §A3.4: C_♭^{(k)} is built from objects available at step k of
  NAH-ind, not from itself). The anti-circularity clause of REVIEW_S22 l.432 — do not use per-level
  covariances as Newton inverses — is satisfied, because ζ^c is the **composite** chain-minimiser map.
- **Not trivial.** NB-5 is the exact background analogue of Theorem N1-15, which consumes (I3)(I4)(I5) at
  the trivial background to bound D³E_k^br(1) (NORMS l.112-124, l.507-556). The new content is Lemma NB-3
  (at Z ≠ 1 the vertex has **six** families, not one — Lemma N1-1's "exactly one differentiated leg per
  term" is FALSE at a background) and the count that the four new families are subcritical.

**Ruling (PROVEN as a reading of the two files, with the quantitative step re-derived in check ad1): the
reduction is legitimate.** I re-derived the load-bearing arithmetic independently — see §8; my
leg-counting rule was first forced to reproduce NORMS' two pre-session exponents (reproduction control
ad1-A PASS) and then returned **−4, −1, −8, −2** with critical dimensions **8, 5, 12, 6**, matching
NBG_A §A3.2 although those numbers were deliberately **not** pre-registered as targets.

### §3.2 But the reduction is not to (GAP-Z) — NBG_A's own table says so

NBG_A §A4.1's table lists NB-5's hypotheses with their statuses. Read as a list of open inputs it gives:

| input | what it is | status in NBG_A's own table |
|---|---|---|
| (H1) | tower existence + differentiability = **(CL-4)** | **OPEN** |
| (H2) curvature | BFT-1 at θ_w^c = 2, **at the nonlinear critical chain** | **OPEN** (PROVEN only for the linear and R^ax *sibling* chains) |
| (H2) soft | (C_g-θ) at θ = 1 nonlinearly | first order PROVEN, **BCH remainder ARGUED** |
| (H3) M half | = **(GAP-Z)** (reading (γ)) | **OPEN** |
| (H3) locality, invariant half | Combes-Thomas at the background | **ARGUED** |
| (H3) locality, variant half | **(N-loc)** at the background | **OPEN** |

**Finding A4 (PROVEN, a reading of NBG_A against itself).** The headline *"(N-bg) collapses to (GAP-Z);
the smallest missing input is (GAP-Z)"* is produced by §A4.3's extra move — *"everything else is either
already OPEN at the trivial background, or PROVEN for a sibling chain"* — and that move does not hold
for **(H2) curvature**. BFT-1 at the critical chain is **not** "already OPEN at the trivial background":
at the trivial background there is no curvature to decay, so BFT-1 is an irreducibly
background-specific open input. *"PROVEN for a sibling chain"* is not proven. And NBG_A's own §A3.4
item 2 makes (H2) load-bearing: at θ_w^c = 0 *"every new family goes positive and Theorem NB-4 is
false"* — which my designed-FAIL control **ad1-C** independently reproduces (exponents +4, +7, −8, +4).
**So BFT-1 at the weight pair is a second background-specific input to (N-bg), not implied by (GAP-Z).**

**Ruling: the reduction survives; the "single input" headline does not.** The honest form of NB-5 is
**(N-bg) ⟸ (CL-4) + BFT-1 + (GAP-Z) + (N-loc)^Z + [Combes-Thomas, ARGUED]**, which is exactly NBG_B's
§6.3 row 3 (*"TRUE only as one of ≥ 5 inputs"*), reached from the opposite side. **On the one row where
the two workers' reasoning actually meets, they agree.**

### §3.3 The independence claim fails

NBG_A §A4.2 says the collapse is *"confirmed from the (N-bg) side, by a route independent of lane B's"*,
and claims **"Two independent derivations of the same collapse."** It is not two.

The collapse has two legs. Leg 1, **(N-bg) ⟶ background linear response**, is NBG_A's own and is sound.
Leg 2, **background linear response = (GAP-Z) = (G♯_0-field)**, is *cited*: NBG_A's own sentence reads
*"…which is exactly `(GAP-Z) = (G♯_0-field)` moved off the trivial chain **(BFT_B l.4594, l.4737)**"*.
Those two lines are §41.5 (iii) and its table row — **the very claim NBG_B refutes**.

**Finding A5 (PROVEN, a reading).** T55-D's second leg is lane B's claim, imported verbatim. The two
reads are independent in *authorship* but not in *evidence*: there is one derivation of leg 1 and one
(refuted) derivation of leg 2. **The "two independent derivations" sentence must be withdrawn.** This is
the single error that turned a correct reduction into a wrong count.

---

## §4. (T-K3) The six ordered implications, re-decided — with the consumers' quantifiers

Write **(G♯f)** = (G♯_0-field), **(GZ)** = (GAP-Z), **(Nbg)** = (N-bg). "Consumer quantifiers" means:
for (Nbg), what PROOF l.6045 (I_i)(c) and CURV-F2″ actually demand; for (GZ), what Theorem TRANSP demands
(BFT_B l.4600-4601: on 𝒦(ε), m = 0, composite-co-closed sources at Z = Z^off(V)); for (G♯f), what
B-NA-red demands (RTARGET §33's X_c pair with its Hölder version).

| # | implication | unconditional verdict | conditional form that **does** hold | my reason |
|---|---|---|---|---|
| 1 | **(GZ) ⟹ (G♯f)** | **FALSE** | none found | §2.4: (G♯f) additionally requires **(G♯_0-fine)** (PROOF l.3613), which (GZ) disclaims (*"no decay claimed"*), and sits on the per-level slice, not S_E |
| 2 | **(G♯f) ⟹ (GZ)** | **FALSE** | **(GZ)\|_{Z=1} + (HESS-rel) ⟹ (GZ)** — *not* (G♯f) + (HESS-rel); see §4.1 | (G♯f) is a Z = 1 statement with no mechanism to move off Z = 1; NBG_B's reason (needs G-pert + (G♯-patch^Ω), different slice) stands |
| 3 | **(GZ) ⟹ (Nbg)** | **FALSE as stated** | **(GZ) + (CL-4) + BFT-1 + (N-loc)^Z + CT ⟹ (Nbg)** (Theorem NB-5, PROVEN-HERE as an implication by T55-D; its quantitative step re-derived here as ad1) | (GZ) is one of ≥ 5 inputs. **Both workers reach this independently** |
| 4 | **(Nbg) ⟹ (GZ)** | **FALSE** | none found | a third-derivative/Lipschitz bound on Hess E_k^br carries no information about the invertibility of 𝓛_Z |
| 5 | **(G♯f) ⟹ (Nbg)** | **FALSE** | none found | (G♯f) is at the trivial background; (Nbg) is *defined* as the gap from the trivial background to the class (NORMS Remark N6-5 exists only to name that gap) |
| 6 | **(Nbg) ⟹ (G♯f)** | **FALSE** | none found | as 4: wrong order of derivative, wrong object |

**All six unconditional implications fail. NBG_B's §6.3 verdict is UPHELD**, row by row, including with
the consumers' quantifiers rather than the statements' own. I found **no** surviving unconditional
implication in either direction.

### §4.1 One conditional implication survives, and NBG_A mis-states its own input

NBG_A §A4.3's **(HESS-rel)** (status GAP) is a real and un-walked route, and it is not touched by
BFT_B §41.5 (i)'s no-go (which is about *conjugation* and the symbol method; a Neumann series is neither).
But **the flat input it names is the wrong one.** A Neumann series
`‖(A + E)^{-1}‖ ≤ ‖A^{-1}‖/(1 − ‖A^{-1}E‖)` needs the flat inverse **in the same pair as the perturbation
estimate**, and (HESS-rel) is stated in lane B's **𝔐 → Y** pair. (G♯_0-field) is not in that pair: BFT_B
l.3840 states it *"in the §33 pair"*, on the per-level slice. So the correct reading of NBG_A's own route
is

> **(GZ)|_{Z=1} in the 𝔐 → Y pair + (HESS-rel) ⟹ (GZ).**

**Finding A6 (ARGUED — I read lane B's pair conventions from citations and did not re-derive 𝔐).** The
flat input this route needs is a **fourth object**: the Z = 1 composite-slice chain-Hessian inverse bound
in lane B's own 𝔐 → Y pair. It is not (G♯_0-field) (wrong pair, wrong slice), not Theorem 4.2′'s M (wrong
currency: ℓ²/symbol, and only two gauge-invariant outputs), and not Corollary LIN0 (gauge-invariant
outputs only). **Its status is unrecorded anywhere I could find.** Naming it is cheap and is the
precondition for the cheapest route to (GAP-Z) anyone has proposed. I refer to it below as the **flat
𝔐-pair composite-slice bound**; lane B should name it properly or say why it already has it.

### §4.2 A consumer-quantifier observation neither worker drew

NBG_A §A1.2 (k1) establishes that **(N-bg)'s only live consumer needs C_♭^{(k)} = O(k), not O(1)**,
because CURV-F2″ caps ε_unif at O(1/k) independently of C_♭ (PROOF l.6500-6507). Combining that with
NB-5: **the (GAP-Z) that (N-bg) needs inside (H3) need only be O(k)-uniform, not k-uniform.** Since the
whole difficulty of (GAP-Z) is k-uniformity, this is a materially weaker input for the (N-bg) branch —
though **not** for Theorem TRANSP, whose statement is k-uniform. Status **ARGUED**, and conditional on
CURV-F2″ remaining in force (NBG_A §A1.2 (k2): full k-uniformity binds again once CURV-F2″ is removed).
Recorded because the lead asked for the consumers' quantifiers and this is one of them.

---

## §5. (T-K4) The ruling: the count, and the dependency graph

### §5.1 The count depends on the unit, and the two workers used different units

My pre-stated **ADJ-F5 OCCURS.** T55-E counts **distinct statements**; T55-D counts **new analytic
inputs not already open elsewhere**. Both counts are internally defensible and neither is the ledger's
unit, which is **open work items at this wall**. The count must be given in all three.

| unit | count | contents |
|---|---|---|
| **distinct statements**, no pairwise implication | **THREE** | (N-bg), (GAP-Z), (G♯_0-field). **T55-E is right in this unit.** |
| **independent obstructions** (items not implied by other named items) | **TWO paper-scale** | **(GAP-Z)** and **(G♯_0-field)**. **(N-bg) is NOT one**: NB-5 derives it from items already named. **T55-D is right that (N-bg) adds nothing — and wrong about which item it collapses to.** |
| **open work items on the (N-bg) branch** | **SIX** | (CL-4), BFT-1 at the weight pair, (GAP-Z), (N-loc)^Z, Combes-Thomas-at-Z [ARGUED], + the (C_g-θ) BCH remainder [ARGUED]. **Neither worker's count is this.** |

**The lead's working hypothesis — "both can hold, giving two" — is UPHELD in the unit the ledger uses,
and I could not break it.** I tried three ways: ADJ-F1 (do the two (GAP-Z)s coincide? — **they do not**,
§2.2, but all readings are OPEN at Z ≠ 1 and all are distinct from (G♯_0-field), so the answer survives);
ADJ-F2 (does the PROVEN beat the ARGUED only by its label? — **no**, §2.4 gives a proof that needs no
banked PROVEN at all); ADJ-F4 (is the disagreement merely verbal? — **partly**: the sharpest conflict is
not between the two files but **inside NBG_A**, whose §A6 tally already lists (CL-4), BFT-1,
(GAP-Z)/(G♯_0-field) and (N-loc)^Z as *separate* unchanged OPEN items, contradicting its own §A4.2
headline).

**Where the hypothesis needs correcting:** it says *"both workers' counts are wrong and both their
arguments may be right."* The first half is right. The second is not quite — **T55-E's headline argument
(the three lines) is unsound under one of the three readings of (GAP-Z) and is not the reason its
conclusion holds**, and **T55-D's independence claim is false**, not merely imprecise.

### §5.2 The dependency graph

Nodes: the three disputed items, plus every named input that appears in an edge. `⟸` = "follows from".
Status in brackets is the *edge's* status, i.e. how well the implication itself is established.

```
                    (G♯_0-field)   [OPEN, "not attempted"; RTARGET l.654, PROOF l.3614]
                          ⇑
            ┌─────────────┴──────────────┐
   multi-level per-level-slice      (G♯_0-fine)
   physical gap  [OPEN;             [OPEN; PROOF l.3612: the K ≠ 0 alias
   NOT PG^{(k)}, PROOF l.3615]      symbol not shown analytic in a strip]
            (no edge to anything below — different slice, different pair)

                       (GAP-Z)      [OPEN; three inequivalent readings, §2.2]
                          ⇑
         ┌────────────────┴─────────────────┐
  flat 𝔐-pair composite-slice bound    (HESS-rel)
  [status UNRECORDED — §4.1]           [GAP; proven by BFT_B §41.2(c) for
                                        two defects B1/B2 only]
                      ⇑  edge status: ARGUED (§4.1; NBG_A named
                         (G♯_0-field) here, which is the wrong input)

                        (N-bg)       [OPEN]
                          ⇑  edge status: PROVEN-HERE as an implication
                             (Theorem NB-5; quantitative step re-derived, check ad1)
   ┌──────────┬──────────┴──────┬──────────────┬──────────────────┐
 (CL-4)    BFT-1 at        (GAP-Z)        (N-loc)^Z      Combes-Thomas at Z
 [OPEN]   (θ_w^c,θ_w^r)    [OPEN]          [OPEN]           [ARGUED]
          = (2,3) [OPEN]
                                    — and, by §4.2, (GAP-Z) is needed here
                                      only at O(k), not k-uniformly [ARGUED]

  alternative, bypassing the whole lower block:
                        (N-bg)  ⟸  BFT-4's Cauchy estimate on a k-uniform
                                    polydisc (BFT-2)        [route (ii), NORMS l.635-637;
                                    needs the trivial-background Taylor bound at EVERY
                                    order, so not obviously cheaper — but it touches
                                    neither (GAP-Z) nor (G♯_0-field)]
```

**Read off the graph:**
1. **The (G♯_0-field) subtree and the (GAP-Z) subtree share no node.** That is the non-identity, in
   picture form, and it is why the ledger must not merge them.
2. **(N-bg) has no outgoing edge** — nothing depends on it that does not already depend on its inputs —
   and two incoming routes. It is a **consequence**, not an obstruction.
3. **The only edge that would join the two subtrees is the one NBG_A mis-stated** (§4.1). Repaired, it
   does not join them: it joins (GAP-Z) to a flat statement in lane B's own pair.

### §5.3 The single item that, if proven, collapses the most

**(GAP-Z).** Proven, it discharges (C-I), hence Theorem TRANSP's entire (H-inv+)_Z bundle and all of lane
B's Tier-C at the background (BFT_B l.4601, l.4606), **and** it supplies (H3)'s M half for Theorem NB-5,
so it closes the BFT background branch and the (N-bg) branch together. It does **not** close
(G♯_0-field) — that is the whole content of this ruling.

**Highest leverage per unit of work, which is a different question: (HESS-rel).** It is session-scale
(BFT_B §41.2 (c) already proves the required slot-wise, weight-free, factor-k-free form for two defects),
and it converts the paper-scale (GAP-Z) into a flat statement. **Before anyone walks it, the flat input
must be renamed** per §4.1, or the route will be walked toward an object that cannot serve it.

---

## §6. (T-K5) Who was wrong about what

Both workers did good work and both reported honestly. The point here is an accurate record.

### T55-E (`NBG_B.md`) — the conclusion survives; the headline proof is weaker than advertised

| claim | ruling |
|---|---|
| **(GAP-Z) ≠ (G♯_0-field)** | **SURVIVES — upheld, PROVEN.** This is the load-bearing claim and it is right |
| the three-line argument of §6.1 | **SOUND under readings (β) and (γ); UNSOUND under (α)**, where (GAP-Z)\|_{Z=1} is a slice coercivity that is *not* located as proven. It is not the reason the conclusion holds. §2.4 supplies a proof that holds under all three readings and names the missing half, **(G♯_0-fine)**, which §6 does not |
| Z = 1 is an admissible restriction | **SURVIVES** — verified independently against 𝒦(ε) and §38.1 (§2.1). The attack the lead aimed at this step misses |
| all six ordered implications fail | **SURVIVES**, row by row, including under the consumers' quantifiers (§4). But §6.3 **missed one surviving *conditional*** implication, row 2 — which it could not have seen, since it did not read NBG_A |
| §6.2's four structural mismatches | **PARTLY SURVIVES.** **Slice** and **norm type** survive every reading. **Output class** and **extra input** are reading-dependent and fail under (α). **Background** is not a mismatch at all once one restricts to Z = 1. Three mismatches, not four — enough, but the table should not be quoted as it stands |
| §12's diagnosis: the collapse rides on the phrase *"lane A's U = 1 package"* | **SURVIVES, and is sharpened: three sites, two meanings** (BFT_B l.3840 vs l.4334, l.4594), one of them backticked so that a plain grep misses it (§1, Finding A2). This is the most valuable single finding in either file |
| NORMS l.631-634 is the probable source | **SURVIVES** — verified by string; (I3)(I4)(I5) are LINEAR_PACKAGE Thms 3.8, 3.1, 4.2/4.2′ (NORMS l.116-124), not the (G♯_0-field) family |
| **the count: THREE obstructions** | **WRONG in the ledger's unit.** Three distinct *statements*, yes. But (N-bg) is **not** an independent obstruction: it is implied by items already named (§3). The correct ledger count at this wall is **two paper-scale items** |

**In one line: T55-E's argument is right where it matters and its count is wrong — it counted statements
where the ledger counts obstructions, and it could not see that (N-bg) is downstream because it did not
have T55-D's reduction.**

### T55-D (`NBG_A.md`) — the mathematics survives; the verdict does not

| claim | ruling |
|---|---|
| **Lemma NB-1 / Corollary NB-2**: the branch third-derivative identity extends to any background; TOWER-VAR (d)'s stated reason is the trivial-background special case | **SURVIVES** (the vanishing term is the first derivative of criticality — the envelope argument — which holds at every critical chain). Not independently re-derived here beyond that reading |
| **Lemma NB-3**: six vertex families at Z ≠ 1; **Lemma N1-1's "exactly one differentiated leg per term" is FALSE at a background** | **SURVIVES.** This is the real discovery in the file and it is a correction to NORMS |
| **Theorem NB-4**: the four new families are subcritical; (N-bg) adds no exponent, weight-pair or dimensional condition | **SURVIVES — independently re-derived here** (check ad1: −4, −1, −8, −2; critical dimensions 8, 5, 12, 6), with a reproduction control calibrated on NORMS' pre-session exponents and a designed-FAIL control that fires |
| the vertex transports at relative cost (1 + Cε), closing the "second d = 4 obstruction" objection | **SURVIVES.** The only marginal family at d = 4 is the one N1-15 already carries; the nearest new one is subcritical by one power of L |
| **Theorem NB-5**: (N-bg) ⟸ (H1) + (H2) + (H3) | **SURVIVES**, non-circular (first-order hypotheses, third-order conclusion) and non-trivial (§3.1) |
| **"(N-bg) collapses to (GAP-Z); the smallest missing input is (GAP-Z)"** | **WRONG.** NBG_A's own §A4.1 table and §A6 tally list **(CL-4), BFT-1 at the critical chain, (N-loc)^Z** as further open inputs, and BFT-1 is irreducibly background-specific — *"PROVEN for a sibling chain"* is not proven, and §A3.4 item 2 makes it load-bearing (my ad1-C reproduces the failure at θ_w^c = 0) |
| **"NBG-F1 does not occur; (N-bg) and (G♯_0-field)/(GAP-Z) are one obstruction"** | **WRONG**, and wrong for a specific reason: the second leg, *"(GAP-Z) = (G♯_0-field)"*, is **cited from BFT_B l.4594, l.4737** — it is lane B's claim, not a finding of this file |
| **"confirmed … by a route independent of lane B's" / "two independent derivations of the same collapse"** | **FALSE — must be withdrawn** (§3.3). Independent in authorship, not in evidence. One derivation of leg 1 (T55-D's own, sound), one of leg 2 (lane B's, refuted) |
| **§A4.3 (HESS-rel)**, labelled GAP and *"the weakest item in this file"* | **SURVIVES as a route and is the most valuable un-walked item named this session** — but its stated flat input is wrong (§4.1). The worker's own caveats 1-3 were well placed; the defect is in the input, not in the caveats |
| §A1.0 (three C_♭ objects), §A1.3 (𝔑 = +∞), §A1.2 (C_♭^{(k)} = O(k) suffices) | **Outside the disputed question; not adjudicated here.** §A1.2 is used in §4.2 as a consumer-quantifier observation and is labelled ARGUED there |
| **the count: ONE** | **WRONG**, for two independent reasons: the imported leg 2 is false, and even leg 1 does not reduce (N-bg) to a single input |

**In one line: T55-D's argument is right about (N-bg) and wrong about what (N-bg) reduces to — its
reduction is sound and its count fails because it imported, without checking, exactly the claim its
counterpart was refuting.**

### The symmetry worth recording

**On the one row where the two files' reasoning actually meets — "(GAP-Z) is one of ≥ 5 inputs to
(N-bg)" — they agree** (NBG_B §6.3 row 3; NBG_A §A4.1's table). Each then wrote a headline that its own
body contradicts: NBG_B counted (N-bg) as an independent obstruction although its row 3 says it is
downstream; NBG_A counted one obstruction although its table lists six open inputs. **The disagreement
between the two files is smaller than the disagreement inside each of them.** My pre-stated **ADJ-F4
partly OCCURS**: the dispute is substantially verbal (counting units, §5.1) plus one genuine false claim
on each side (T55-E's "three obstructions"; T55-D's "independent confirmation").

---

## §7. (T-K6) PROOF.md's [S25-fix 2]: STANDS, with a mandatory amendment

**Ruling: [S25-fix 2] is NOT reversed.** Its operative instruction — that [S24-note 2]'s *"ONE
obstruction, not two, and this ledger must not count them twice"* is wrong, and the open count must not
be reduced on its account — is **correct**. I ruled for T55-E on the identity question, so the lead's
correction stands and nothing has to be un-done.

**But three of its sentences are wrong and must be amended**, and the amendment is not cosmetic: as it
stands, [S25-fix 2] tells a future reader that (N-bg) is an independent obstruction, which is the thing
T55-D disproved, and it carries a proof that fails under one of the three readings of (GAP-Z).

1. *"They are THREE obstructions, not one"* → three distinct **statements**; **two** independent
   obstructions. (N-bg) is downstream.
2. the three-line refutation → replace with §2.4's, which needs no banked PROVEN and names (G♯_0-fine).
3. *"four independent mismatches"* → three survive every reading (§2.5).
4. the cite **"PROOF l.3588"** → **l.3614** (§1, Finding A1).

Append-ready replacement text is in the FOR OTHER FILES section below. **PROOF.md is the lead's to edit
and I have not touched it.**

---

## §8. Check record — ad1

Criteria `checks/ad1_criteria.md`, **written before `checks/ad1_exp.py` existed**. No constant in the
criteria is derived in session 25: the criteria pre-register only d = 4, L = 3, the weight pair (2, d−1)
from HANDOFF, θ_A = min(1, θ_w^c − 1) from **NORMS l.656-657**, and the two exponents NORMS l.658-663
already carries. **NBG_A's numbers −4, −1, −8, −2 and 8, 5, 12, 6 were deliberately NOT pre-registered as
targets**, so reproducing them is evidence rather than circularity. No criterion retuned, no re-run, no
post-hoc probe. Plain python3 `-I`, exact `Fraction`/integer arithmetic, no numpy, no sympy, no BLAS, no
numeric lock (brief rule 6). `nice -n 10`, thread vars = 1, runtime < 1 s, memory negligible. Output kept
unaltered at `checks/ad1_out.txt`; `checks/ad1_err.txt` empty.

| id | verdict | numbers |
|---|---|---|
| **ad1-A** reproduction control (the rule must first return NORMS' own two exponents, or the gate is void) | **PASS** | 1-deriv Wilson at d = 4: **0** (NORMS: "exactly marginal"); 1-deriv soft slope at d = 4: **−1**, at d = 5: **0** (NORMS: subcritical for d < 5) |
| **ad1-B** THE GATE: are the four new families strictly subcritical at (4, 2, 3, 1)? | **PASS** | **−4, −1, −8, −2**; critical dimensions **8, 5, 12, 6** |
| **ad1-C** DESIGNED-FAIL CONTROL at θ_w^c = 0 (hence θ_A = −1) | **CONTROL FIRED** — ad1-B's criterion **FAILS** here, as required | **+4, +7, −8, +4**: three of four families go positive. Independently reproduces NBG_A's na1-E |
| **ad1-D** SECOND DESIGNED-FAIL CONTROL: formula sensitivity | **CONTROL FIRED** | leg-counting 3-deriv soft slope **−8** vs the alternative form d − θ_w^r − 2θ_w^c − θ_A = **−4**. The gate is formula-sensitive, so it is not a tautology |

**Separate robustness line, not a pass (ad1-D).** Both forms are negative, so ad1-B's verdict does not
depend on which is used. **This is the resolution of T55-D's disclosed FAIL na1-B**: the worker
pre-registered d − θ_w^r − 2θ_w^c − θ_A for the 3-derivative soft family and computed d − 4θ_w^r. The
leg count makes the computed form the right one (coefficient φ̂‴(ρ) = O(|ρ|) carries θ_w^r, plus three
ρ_1 legs at θ_w^r each), and **both are negative, so the FAIL is a pre-registration error with no
consequence for the result.** The worker's self-assessment is confirmed; the disclosure was correct and
the conclusion is undamaged.

**What ad1 decides, and only that.** It decides the subcriticality of four exponents under a stated
leg-counting rule calibrated on NORMS. It decides **nothing** about (GAP-Z), (G♯_0-field), the slice
question, the identity question, or any status. The adjudication in §2-§7 is a reading of statements and
no script could have produced it.

---

## §9. Tally, and what I did not do

**PROVEN (in this file).**
- **§2.1** Z = 1 is an admissible value of Z in (GAP-Z)'s own quantifier (𝒦(ε) = {f_k ≤ ε}, BFT_B l.2865;
  §38.1's Z = trivial specialisation). The step the lead flagged does not fail.
- **§2.2 / Finding A3** (GAP-Z) names **three inequivalent objects**; BFT_B l.4334's *"equivalently"* is
  not an equivalence.
- **§2.4** (GAP-Z)|_{Z=1} ⇏ (G♯_0-field), **at every reading**, because (G♯_0-field) also requires
  **(G♯_0-fine)** (PROOF l.3613) and the per-level-slice gap that is explicitly *not* PG^{(k)}
  (PROOF l.3615). Needs no banked PROVEN.
- **§3.1** Theorem NB-5's reduction is non-circular and non-trivial.
- **§3.2 / Finding A4** NB-5's hypothesis set contains a second background-specific open input, **BFT-1
  at the weight pair**, so (N-bg) does not reduce to (GAP-Z) alone.
- **§3.3 / Finding A5** T55-D's second leg is cited from BFT_B l.4594/l.4737; the independence claim is
  false.
- **§4** all six unconditional implications fail, including under the consumers' quantifiers.
- **§1 / Findings A1, A2** the citation audit: one drifted cite (PROOF l.3588 → l.3614, now inside
  PROOF.md's own [S25-fix 2]); the phrase *"lane A's U = 1 package"* at three sites with two meanings,
  one backticked.

**ARGUED.** §4.1 / Finding A6 (the flat 𝔐-pair composite-slice bound is a fourth, unrecorded object —
I read lane B's pair conventions from citations and did not re-derive 𝔐); §4.2 (the (N-bg) branch needs
(GAP-Z) only at O(k), conditional on CURV-F2″ remaining in force); §5.3's leverage judgement.

**Nothing new is proven about (N-bg), (GAP-Z) or (G♯_0-field) themselves.** This file moves no item in
PROOF.md's tally. It settles a dispute and corrects a ledger entry; it is not a step of the proof, and
I report that plainly.

**Explicit scope limits.**
1. I did **not** re-derive LINEAR_PACKAGE Theorem 4.2′ or Theorem 3.8. §2.4 is written precisely so that
   the ruling does not need them; §2.3's readings (β)/(γ) do, and are labelled accordingly.
2. I did **not** re-derive Lemma NB-1's two derivations, Lemma NB-3's expansion, or Corollary NB-2
   beyond reading them and checking the envelope argument. I re-derived only NB-4's exponent count.
3. I did **not** open (CO-fun), (R♯_ω), (G♯-patch^Ω), (N1-nd) or (CURV-dec).
4. I did **not** search for a proof of the **flat 𝔐-pair composite-slice bound**; I searched for a
   *record* of one and found none. Absence of a record is not absence of a proof — lane B should say.
5. I read **both** files under adjudication in full, plus BFT_B §38.1 and §41.5-§41.7, LINEAR_PACKAGE §3-§4,
   NORMS Remark N6-5 and §N7, RTARGET §33 and §37, and PROOF.md §§ located by string. I did not read
   REVIEW_BFT_B_S9_S10 or SF.md beyond the lines quoted by NBG_B.

**Biggest obstruction in my scope, having ruled: the flat 𝔐-pair composite-slice bound of §4.1.** It is
the input to the only cheap route to (GAP-Z) that anyone has named, it is named wrongly in the file that
proposed the route, and its status appears nowhere. One lane-B sentence would settle whether the route
is open or already blocked.

---

## FOR OTHER FILES (not edited)

### PROOF.md (the lead's; [S25-fix 2] is the lead's edit and mine is a ruling on it)

**1. [S25-fix 2] STANDS — do not reverse it.** Amend it. Replace the block that currently begins
`**>>> [S25-fix 2] THIS IS REFUTED (NBG_B §6, session 25). They are THREE obstructions, not one,` and
runs to `...NORMS l.631-634 makes the same conflation independently and earlier and is probably its
source.` with:

```
  **>>> [S25-fix 2] THIS IS REFUTED (NBG_B §6, session 25; adjudicated and amended by NBG_ADJ §2, §5,
  session 25). (GAP-Z) and (G♯_0-field) are NOT one item, so the "must not count them twice"
  instruction above is WRONG — banked by the lead and used to set session 25's priority ordering
  before it was checked. The open count must not be reduced on its account.
  **The count, in the unit this ledger uses: TWO independent obstructions, not one and not three.**
  (GAP-Z) and (G♯_0-field) are two paper-scale items with no shared node. (N-bg) is a THIRD DISTINCT
  STATEMENT but is NOT an independent obstruction: NBG_A's Theorem NB-5 derives it from (CL-4) + BFT-1
  at the weight pair + (GAP-Z) + (N-loc)^Z + a Combes-Thomas step [ARGUED], all already named, and its
  own residue — the background cubic vertex — is PROVEN-HERE subcritical (NBG_A §A3; re-derived
  independently in NBG_ADJ check ad1: exponents −4, −1, −8, −2, critical dimensions 8, 5, 12, 6, with
  a reproduction control on NORMS' own exponents and a designed-FAIL control that fires at θ_w^c = 0).
  **The refutation, in the form that needs no banked PROVEN** (NBG_ADJ §2.4): PROOF l.3614-3615 states
  that (G♯_0-field) *"needs, in addition, the abelian multi-level (per-level slice) physical gap, which
  is not PG^{(k)}"*, and PROOF l.3613 that *"(G♯_0-fine) is also needed for (G♯_0-field)"* — so
  (G♯_0-field) = [multi-level per-level-slice gap] + [(G♯_0-fine), a Campanato/Hölder bound that is
  OPEN for an unrelated reason: PROOF l.3612, the K ≠ 0 alias symbol is not shown analytic in a strip].
  (GAP-Z) is at most the first, on a DIFFERENT slice (composite S_E vs the per-level h^(i) = 0 with
  Feynman terms, RTARGET l.599-600), and explicitly disclaims the second (*"with no decay claimed"*,
  BFT_B l.4334 and l.4590). Hence (GAP-Z)|_{Z=1} ⇏ (G♯_0-field) at ANY reading of (GAP-Z).
  **Z = 1 IS an admissible restriction** (𝒦(ε) := {V : f_k(V) ≤ ε}, BFT_B l.2865; BFT_B §38.1 gives the
  Z = trivial specialisation explicitly), so the short status argument is available too: under BFT_B
  §41.5 (ii)'s own reading — (GAP-Z) is *"the M half"* of Theorem 4.2′ — (GAP-Z)|_{Z=1} is M, PROVEN,
  while (G♯_0-field) is "not attempted" (RTARGET l.654; **PROOF l.3614**, not l.3588 — the pointer in
  the earlier version of this note had drifted 26 lines).
  **All six ordered implications fail unconditionally** (NBG_B §6.3, re-decided in NBG_ADJ §4 against
  the consumers' quantifiers). **THREE structural mismatches survive every reading: slice, norm
  type/decay, and the missing (G♯_0-fine) half.** The earlier "four mismatches" over-counted: "output
  class" and "extra input" hold only under the reading in which (GAP-Z) is a symbol bound, and
  "background" is not a mismatch once one restricts to Z = 1.
  **Diagnosis:** the collapse rides on the phrase *"lane A's `U = 1` package"*, used at THREE sites in
  BFT_B.md with TWO meanings — l.3840 (= (G♯_0-field), OPEN) against l.4334 and l.4594
  (= LINEAR_PACKAGE, PROVEN) — the l.4594 occurrence backticked, so a plain grep for the phrase misses
  it. Systemic defect 1 operating on a phrase. NORMS l.631-634 makes the same conflation independently
  and earlier and is probably its source. **A further defect of (GAP-Z) itself:** BFT_B l.4334 defines
  it twice in one sentence, joined by *"equivalently"* — a bound on the kernel of the gauge-fixed
  composite chain Hessian, AND a k-, T-uniform lower bound for 𝓛_Z on the slice — and these are not
  equivalent (the first, as §41.5 (ii) reads it, bounds two gauge-invariant response symbols; the
  second controls the configuration). NBG_A §A4.1 uses a third reading (the background (I3) sup
  bounds). **(GAP-Z) must be restated before it is used.**
```

**2. Second [S25-fix 2] site.** Replace the parenthetical
`(notably **(GAP-Z) IS BFT-5's (G♯_0-field)** — **REFUTED in session 25, see [S25-fix 2]: they are three
obstructions, not one**)` with:

```
(notably **(GAP-Z) IS BFT-5's (G♯_0-field)** — **REFUTED in session 25, see [S25-fix 2]: they are TWO
independent obstructions, not one; (N-bg) is a third distinct statement but is downstream of items
already named, by NBG_A's Theorem NB-5, and is not an independent obstruction**)
```

**3. New note to carry, [S25-note]:** *the flat 𝔐-pair composite-slice bound* — the Z = 1 composite-slice
chain-Hessian inverse bound in lane B's 𝔐 → Y pair — **has no status recorded anywhere**. It is the
input that NBG_A §A4.3's (HESS-rel) route actually needs (NBG_A names (G♯_0-field), which is in the §33
pair on the per-level slice and cannot serve; NBG_ADJ §4.1). It is neither Theorem 4.2′'s M (wrong
currency) nor Corollary LIN0 (gauge-invariant outputs only). **Lane B to name it or to say it already
has it.**

### RTARGET.md

**§54's failure mode NBG-F1:** record **OCCURS**, with the amendment that the count is **two**
independent obstructions and that **(N-bg) is not one of them**. **RTARGET l.1042** (*"(GAP-Z) IS
BFT-5's (G♯_0-field): the nontrivial background and BFT-5 are one obstruction"*) → mark **REVERSED**,
against BFT_B §41.5 (iii)/§43, carried by the lead into [S24-note 2]. NBG_B's request to mark it
reversed is upheld.

### BFT_B.md (lane B)

1. **§38.1's (GAP-Z) definition (l.4334) is internally ambiguous** and should be split. The sentence
   joins two non-equivalent characterisations with *"equivalently"*. Lane B should state which it means
   — the **M half of Theorem 4.2′ at Z** (§41.5 (ii)'s framing) or a **coercivity of 𝓛_Z on S_E** — and,
   if both are wanted, name them separately. NBG_A §A4.1 is already using a third reading (background
   (I3) sup bounds), which is how the same name came to carry three objects.
2. **§41.5 (iii) and §43 item 4 are REVERSED** as statement identities. The correct sentence: *(GAP-Z)
   is the Z-analogue of the input of lane A's trivial-background chain, whereas (G♯_0-field) is a
   configuration-level Schauder statement on a different slice that additionally requires (G♯_0-fine)
   and the multi-level per-level-slice gap.* The Z = 1 → Z ≠ 1 **analogy** is right; the identity is
   not. (This upholds NBG_B's request, with the reason strengthened.)
3. **The phrase *"lane A's `U = 1` package"* must be retired** from BFT_B.md. Three sites, two meanings
   (l.3840 vs l.4334, l.4594), one backticked. Suggested: *"LINEAR_PACKAGE v1.1"* at l.4334 and l.4594,
   *"(G♯_0-field), lane A's OPEN trivial-chain configuration bound"* at l.3840.
4. **Two questions from NBG_A §A4.3 that this adjudication endorses and sharpens.** (a) Is the whole
   Hessian difference slot-wise in §41.2 (c)'s sense, beyond the two defects B1/B2? (b) **Was a Neumann
   series considered and declined?** §41.5 (i)'s no-go is about conjugation and the symbol method and
   does not touch it. **Sharpened:** the flat input such a series needs is the Z = 1 bound **in your own
   𝔐 → Y pair**, not (G♯_0-field). Does lane B have it?

### NBG_A.md (T55-D) — two corrections, neither touching its mathematics

1. **§A4.2's sentence *"Two independent derivations of the same collapse"* must be withdrawn.** The
   second leg, *"(GAP-Z) = (G♯_0-field)"*, is cited from BFT_B l.4594, l.4737 — it is lane B's claim,
   not a finding of NBG_A, and it is refuted. The independence is of authorship, not of evidence.
   Everything upstream of that sentence — NB-1, NB-2, NB-3, NB-4, NB-5 — stands.
2. **§A4.3's (HESS-rel) names the wrong flat input.** Replace *"(GAP-Z) follows from the FLAT
   (G♯_0-field) by a Neumann series"* with *"…from the flat (Z = 1) composite-slice chain-Hessian
   inverse bound **in the 𝔐 → Y pair** by a Neumann series"*. (G♯_0-field) is stated in the §33 pair on
   the per-level slice (BFT_B l.3840) and cannot close a Neumann series run in 𝔐 → Y. With that
   repair the route survives and is the most valuable un-walked item named this session; without it,
   anyone walking it walks toward an object that cannot serve.
3. *(Not a correction.)* §A4.1's *"(H3) M half"* is written as the background **(I3)** sup bounds
   (NORMS l.116-118 = LINEAR_PACKAGE Thm 3.8), while BFT_B's (GAP-Z) is the background **(I5)** symbol
   bound minus decay. They are different statements, both OPEN at Z ≠ 1. Worth a line, since the table
   equates them.

### NBG_B.md (T55-E) — one correction, not to the verdict

**§6.2's mismatch table should be cut from five rows to three.** "Output class" and "extra input" hold
only under the reading in which (GAP-Z) is a symbol bound on gauge-invariant outputs; under BFT_B
l.4334's *"lower bound for 𝓛_Z on the slice"* reading, (GAP-Z) **is** configuration-level and **is** a
gap statement, and both rows collapse. "Background" is not a mismatch once one restricts to Z = 1, which
is the only way the two can be compared at all. **Slice** and **norm type/decay** survive every reading,
and the row that should be added is **the missing (G♯_0-fine) half** (PROOF l.3613) — which is the
strongest row available and is not in the table. The §6 verdict is unaffected and is upheld.

### NORMS.md

Upholds NBG_B's request at l.631-634 and adds the reason. Route (i) of (N-bg) names the objects to be
replaced as **(I3), (I4), (I5)** — by NORMS' own l.116-124 these are LINEAR_PACKAGE Thm 3.8, Lemma 3.1
and Thms 4.2/4.2′, the **linear package** — and then calls them *"precisely BFT-5 / the (G♯_0-field),
(a5-G♯), (R♯_ω) family"*, which is a different family. Suggested replacement, merging NBG_B's text with
this ruling:

```
the background versions of (I3), (I4), (I5) — i.e. (GAP-Z) plus the Combes-Thomas decay half plus the
Tier-A/B/C transport of BFT_B §41 — together with (CL-4), BFT-1 at the weight pair, (N-loc) at the
background, and a composite LOC. BFT-5's family ((G♯_0-field), (a5-G♯), (R♯_ω)) is a SEPARATE list with
no shared node: (G♯_0-field) additionally requires (G♯_0-fine) and the multi-level per-level-slice gap
(PROOF l.3613, l.3615), neither of which (GAP-Z) supplies. See NBG_ADJ §2.4, §5.2.
```

Also worth adding to Remark N6-5: **Lemma N1-1's "exactly one differentiated (or residual) leg per
term" is FALSE at a nontrivial background** (NBG_A §A3.1, Lemma NB-3) — two further families switch on
with coefficients O(|X_p|) and O(|ρ|) — **and the new families are subcritical** (critical dimensions
8, 5, 12, 6 against d = 4; NBG_A §A3.2, re-derived in NBG_ADJ check ad1).

---

## §10. Outcome recorded against the PRE-STATED section (§0.3, §0.4)

**Outcome against §0.4's enumeration: ILL-POSED-THEN-TWO.** The question "how many obstructions" was
ill-posed as asked, because the two workers counted in different units (§5.1) and because the name
(GAP-Z) carries three inequivalent objects (§2.2). Resolved: **three distinct statements; TWO
independent obstructions** in the unit the ledger uses; **six** open work items on the (N-bg) branch.
The phrase that had to be split before the count could be taken is *"lane A's `U = 1` package"*
(three sites, two meanings), exactly as §0.3's ADJ-F4 anticipated.

**Pre-stated failure modes.**
- **ADJ-F1 (too convenient): OCCURS, in the weak form.** The (GAP-Z) that T55-D reduces (N-bg) to is the
  background **(I3)** sup bound; the (GAP-Z) whose Z = 1 restriction T55-E tests is the **M half** of
  Theorem 4.2′; BFT_B l.4334's operative clause is a third thing. The convenient answer survives only
  because all three readings are OPEN at Z ≠ 1 and all three are distinct from (G♯_0-field) (§2.3,
  §2.4). **It survives, but not for the reason the lead gave, and (GAP-Z) must be restated.**
- **ADJ-F2 (label deference): does NOT occur.** The ruling for T55-E rests on §2.4, which uses no banked
  PROVEN; T55-E's own PROVEN-labelled three-line argument is reported as unsound under one of the three
  readings (§2.3).
- **ADJ-F3 (line-number drift): OCCURS.** One drifted cite, PROOF l.3588 → l.3614, now carried inside
  PROOF.md's own [S25-fix 2] (§1, Finding A1). Every other cite in the disputed material resolves.
- **ADJ-F4 (shared ambiguous phrase): PARTLY OCCURS.** The phrase collision is real and is the cause
  (§1 Finding A2, §2.2), but the dispute is not purely verbal: T55-E's "three obstructions" and T55-D's
  "independent confirmation" are each a genuine false claim.
- **ADJ-F5 (counting units): OCCURS.** It is the main reason the two reports looked incompatible. The
  count is given in all three units in §5.1.

**Against the lead (D6).** The lead's working hypothesis — reduction plus non-identity gives two — is
**upheld in the ledger's unit, and I could not break it**; §5.1 records the three attempts. Two
amendments to it. (i) *"both their arguments may be right"* is too generous: T55-D's independence claim
is **false**, not imprecise, and T55-E's headline proof is **not the reason its conclusion holds**.
(ii) The lead's instruction to check *"that Z = 1 is an admissible value of Z in (GAP-Z)'s own
quantifier, which is the step that could fail"* pointed at the wrong step: **that step is sound**
(§2.1). The step that actually fails is the one before it — reading *"the background analogue of the
package constant M"* as a definition when the same sentence gives a different operative clause.
