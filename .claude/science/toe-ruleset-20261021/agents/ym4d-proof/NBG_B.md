# NBG_B.md — (N-bg) from BFT-5's side (target T55-E, lane B)

*Owner: worker T55-E, session 25. This file is written only by T55-E. A second worker (T55-D) attacks
(N-bg) from its own side in `NBG_A.md`; the two reads are deliberately independent and uncoordinated.*

---

## §1. PRE-STATED — statements only (FIRST EDIT of this file, 2026-10-28T21:07Z)

**This is the first edit made to this file.** It contains statements of intent only. It cites nothing
produced in this session, by me or by anyone else. Nothing below this section existed when this section
was written, and no derivation, arithmetic or check had been performed.

### §1.1 What I am asked to decide

The session-24 BFT_B record (§41.5 (iii), §43, and the [S24] consolidation) banks the claim:

> **(GAP-Z) is BFT-5's input (1), (G♯_0-field), moved off the trivial chain; so the nontrivial
> background and BFT-5 are ONE obstruction, not two, and PROOF must not count them twice.**

Lead decision **D5** rests on this, and RTARGET §54 pre-registers the failure mode **NBG-F1**:
*(N-bg) and BFT-5's (G♯_0-field) are not the same obstruction → the collapse is wrong and the
obstruction count goes back up.*

### §1.2 Pre-stated targets

- **NB1 (statement pinning).** Write **(G♯_0-field)** as one self-contained statement with its
  quantifiers in the order a consumer must read them: *what* object is bounded, *in which norm pair*,
  *uniformly in which parameters*, *given which hypotheses*, *at which background*. Record every place
  the lane states it and whether the statements agree. Expected outcome: a single statement, or a
  recorded disagreement.
- **NB2.** The same for **(GAP-Z)**.
- **NB3.** The same for **(N-bg)**, as its *consumers* quantify it (not as its name suggests).
- **NB4 (the collapse verdict).** For each ordered pair among {(N-bg), (GAP-Z), (G♯_0-field)}, decide
  whether a proof of the first *yields* the second **with the quantifiers the second's actual consumer
  needs**. Six implications, each decided separately and each labelled. Then give the count: one
  obstruction, two, or three. The test is explicitly *not* whether the prose matches.
- **NB5 (attack from BFT-5's side).** Decide whether
  (a) the session-24 composite contraction **A_soft = 1/3, uniform in k** (rebuilding the load-bearing
  step rather than citing it), plus
  (b) the Green's-function bound of GREENT.md (UNREVIEWED — re-derive whatever I lean on), plus
  (c) **A_c·γ_c** bounded constant-free, so that C_T is an actual number,
  suffice to reach **(G♯_0-field)**. If they do not, name exactly what is missing, and name it as a
  *statement*, not as a difficulty.
- **NB6 (the clause table).** Audit PROOF.md's BFT clause table (near l.6695) **clause by clause** for
  staleness beyond the three fixes session 24 already recorded ((CO-0) = Theorem W0; (CO-up) = Theorem
  GU; (SB) removed by Theorem CO-B). Give the corrected table as append-ready text in a
  `## FOR OTHER FILES (not edited)` section. I do not edit PROOF.md.
- **NB7 (the weight pair).** Decide whether **BFT-5** inherits NORMS.md's **weight-pair** requirement
  (curvature θ_w^c = 2, residual θ_w^r = d − 1 = 3), under which a single common θ_w has no solution in
  (0, 2] for any consumer. If it does, (G♯_0-field) as currently quoted — with one θ_w — is not the
  input BFT-5 consumes, and that is a defect in the *statement*, upstream of any proof.

### §1.3 My own named failure modes, pre-stated

Beyond RTARGET §54's NBG-F1:

- **NB-F2 (type mismatch).** (G♯_0-field) and (GAP-Z) are statements of **different type** — one a
  weighted Hölder/divergence-form (Schauder) pair bound, the other an ℓ²/symbol invertibility bound —
  in which case "the same obstruction" is a category error and the collapse must be restated as an
  implication chain with a named intermediate, or abandoned.
- **NB-F3 (one-way collapse).** The collapse holds in the direction strong ⟹ weak only, *and the ledger
  counts the weak one*. Then the tally is wrong in the unsafe direction: closing the counted item would
  not close the wall. This is the failure mode session 24's experience predicts.
- **NB-F4 (quantifier order).** The three statements differ not in content but in **where "uniformly in
  Z" sits relative to "there exists C"**; a proof of one in the order it is written does not supply the
  other in the order its consumer reads it.
- **NB-F5 (contraction ≠ gap).** The composite contraction A_soft bounds the *iteration map*, whereas
  (G♯_0-field) bounds the *inverse Hessian*. If the contraction's own construction consumes a
  coercivity/invertibility input of (G♯_0-field)'s type, then route NB5 is circular and cannot reach
  (G♯_0-field) at any price. I will check this against the anti-circularity clause (REVIEW_S22 l.430:
  no per-level C^{(j)} as Newton inverses; one contraction for 𝔉_k in 𝔐) before pricing anything.
- **NB-F6 (table not stale).** PROOF.md's clause table is stale in no further place, in which case NB6
  returns a confirmation and the corrected table equals the current one plus session 24's three fixes.
  A confirmation is a result and will be reported as one.

### §1.4 Statuses I will use

PROVEN (a complete proof written out here from stated hypotheses) / ARGUED (convincing, hole named) /
CONDITIONAL (proven given a named open input, named) / GAP / OPEN. A failed check is reported as a
FAIL with its output unaltered; any probe run after seeing a result is labelled post-hoc. If I get
nowhere on a target I will say so against that target's number.

### §1.5 Routes I will not re-walk

Per the session-24 dead list: per-level induction in any norm; both axial gauges; gluing via Theorem RW;
thin-cluster escape; finite funnel truncation; (NEUT-box); route (ii)/GT-ell; (CovLift) at θ > 0 for
every lift; and the gauge escape (Proposition TG-EXCL — a null operation).

---

## §2. Method, and the file:line discipline this scope forced

Systemic defect 1 of the session addendum (symbol collisions) turned out to be **the whole content of
target NB4**, so §2 records the discipline before the result. Every symbol below is quoted with the
file and line at which I read it, and I verified by `grep` that the name I was handed is the name the
consumer uses. The exercise found a sixth live family:

**The (G♯_0-\*) family has SIX distinct members**, by whole-lane count:

| name | occurrences | what it is | where |
|---|---|---|---|
| `(G♯_0-soft)` | 157 | the soft/residual half at U = 1 | RTARGET l.603; **PROVEN** (PROOF l.302) |
| `(G♯_0-fine)` | 124 | the fine-curvature Hölder half at U = 1 | RTARGET l.604 |
| `(G♯_0-plain)` | 104 | plain level-0 currents | PROOF l.3536 |
| `(G♯_0-fine-up)` | 104 | sources at levels ≥ 1 reaching the fine level | PROOF l.4800 |
| `(G♯_0-lev0)` | 48 | level-0 sources, **gauge-invariant outputs**, on lane A's pair | BFT_A l.555 |
| `(G♯_0-field)` | 161 | the **configuration** (gauge-variant) version in ‖·‖_{X_c} | RTARGET l.605 |

and a seventh name, **`(G♯_0-field^∇)`**, which BFT_A l.327 calls *"the ∇-version of (G♯_0-field)"* and
BFT_A l.559 defines as *"the gauge-variant components of 𝔐^∇"*. **These last two are the pair the
collapse question turns on, and they are not the same statement as each other.**

---

## §3. NB1 — (G♯_0-field), pinned. Status: PINNED; the item itself is OPEN ("not attempted")

The authoritative definition is RTARGET.md §33 (l.572-618), which is where PROOF l.3340 sends the
reader (*"(G♯) at U = 1 is (G♯_0-field) of §33"*). Assembled with its quantifiers in consumer order:

> **(G♯_0-field).** Let d = 4, L ≥ 3 odd, κ_− ≤ κ_i ≤ κ_+, and fix α ∈ (0,1), θ ∈ (0,1], 0 ≤ m < m_*'.
> **There exists** C < ∞ **depending only on** (L, κ_±, m, α) — *not* on k, T or X_0 — **such that for
> every** k ≥ 1, **every** coarse torus side T, **every** coarse basepoint X_0, **every** collection of
> co-closed zero-mean level-l sources j_l = d^*G_l (0 ≤ l ≤ k−1) and **every** level-k datum B_k,
> the critical configuration B of the **linearised abelian** chain
> E_j(B) = ½‖dB_0‖² + Σ_{i<k}(κ_i/2)‖QB_i − B_{i+1}‖² − Σ_l⟨j_l, B_l⟩ of Setting SC, **taken in the
> abelian per-level slice h^{(i)} = 0 with Feynman terms on the residual groups** (RTARGET l.599-600),
> satisfies
>   ‖B‖_{X_c} := max_i(‖B_i‖_{∞,m} + ‖dB_i‖_{∞,m}) ≤ C(‖G‖_{Y,α} + ‖B_k‖_{D,m}),
> with ‖G‖_Y := max_l ω_l‖G_l‖_{∞,m}, ω_0 = 1, ω_l = L^{θ(k−l)}, all values in coarse units and all
> weights w(z) = e^{m d(z,X_0)} in coarse ℓ¹ distance; the Hölder version adds [f_0]_{α,m}.

Five features of this statement are load-bearing for §6 and each is a quantifier, not a flourish:

1. **Background: trivial** (U = 1; the chain is the *linearised abelian* one, LINEAR_PACKAGE's title).
2. **Slice: the abelian PER-LEVEL covariant slice** h^{(i)} = 0 with Feynman terms (RTARGET l.600).
3. **Output: the CONFIGURATION**, i.e. the potentials B_i themselves — gauge-variant. This is why it is
   called the "field" member of the family and why PROOF l.3589 needs *"in addition, the abelian
   multi-level (per-level slice) physical gap"*: a bound on potentials needs a gap on the slice.
4. **Norm type: a weighted sup/Campanato (Schauder) PAIR**, Y_α → X_c, with exponential weights e^{md}.
5. **Uniformity: in k, T and X_0, at fixed (L, κ_±, m, α).**

**Status: OPEN, and specifically "not attempted".** RTARGET l.605 pre-stated it as attempted only if the
soft and fine halves were done; RTARGET l.654 records the outcome as *"(G♯_0-field) not attempted"*, and
PROOF l.3588-3590 as *"(G♯_0-field): not attempted. It needs, in addition, the abelian multi-level
(per-level slice) physical gap, which is not PG^{(k)}"*.

**What has changed under it since it was written, which the ledger has not propagated:**
- its sub-input (LED-src) is **closed at m = 0** — REVIEW_BFT_A_S6 l.22-23: *Lemma LE "is the genuinely
  new idea that closes PROOF's (LED-src) at m = 0"*;
- (G♯_0-lev0) at m = 0 for divergence-form + co-closed plain level-0 sources is **Theorem W0, CONFIRMED**
  (REVIEW_BFT_A_S6 l.24); (G♯-up) is **Theorem GU, CONFIRMED** (same line);
- but all of that is on **lane A's pair and lane A's slice**, for the **gauge-invariant** outputs
  (Corollary LIN0 is headed *"gauge-invariant (H-lin^∇)"*, BFT_A l.2242). None of it is the
  configuration statement, and none of it is on the per-level slice.

**And SF has already recorded that the slice cannot be traded.** SF l.890-892 [RSF2-fix GP-1/GP-2]:
G-pert *"bounds the Hessian … in the TRIVIAL slice at x^r, not the Hessian in 'a per-level covariant
slice through ψ^r' as (a5-G♯) is stated; **the two are different gauge-fixed operators** (re-centred
slice functional and Feynman term; moved residual groups)."* That is an independent, already-banked
record that "(G♯) at background B in slice S" does not transport to slice S′. **BFT-5 is stated on a
third slice, S_E, and nobody has reconciled it with either.**

---

## §4. NB2 — (GAP-Z), pinned. Status: PINNED; OPEN

Stated at BFT_B.md l.4334 and re-stated at l.4590:

> **(GAP-Z).** **There exists** M_Z < ∞, **uniform in** k, **in** T **and in** Z over the class
> considered, bounding the kernel of the **gauge-fixed COMPOSITE chain Hessian at Z** — equivalently a
> k-, T-uniform lower bound for 𝓛_Z on the slice — **with no decay claimed** (BFT_B l.4334). It is
> *"the background analogue of the package constant M of LINEAR_PACKAGE Theorem 4.2′"* (l.4334) and
> *"the M half, with no decay claimed. This is the genuinely new analytic input"* (l.4590).

Three features, to be read against §3's five:

1. **Background: general Z** (that is the whole point).
2. **Operator: the COMPOSITE gauge-fixed chain Hessian** 𝓛_Z, not the per-level-slice chain.
3. **Norm type: an ℓ²/symbol operator bound.** The file is explicit twice that **no decay** is claimed;
   the decay half is quarantined as the separate Combes-Thomas statement (BFT_B l.4591, ARGUED).

**Status: OPEN.** Its consumer is Theorem TRANSP (BFT_B l.4601): *(H-inv+)_Z for composite-co-closed
sources at Z holds, every constant of the trivial-background bundle ×(1 + Cf_k), uniformly in k and T,
GIVEN exactly (GAP-Z) and (N1-nd).*

**The one arithmetic fact that decides §6.** BFT_B l.4596 writes the trivial-background chain out:

> Theorem 4.2′'s `M` ⟹ Proposition W ⟹ Theorem Y, YH ⟹ W0, GU ⟹ Corollary LIN0 `=` `(H-inv)`.

So **(GAP-Z) sits at the BOTTOM of that chain and its Z = 1 restriction is Theorem 4.2′'s M, which is
PROVEN** (LINEAR_PACKAGE.md §4 l.219-237, FROZEN v1.1, with its explicit M(L, κ_±) and its strip
conditions verified in 30-digit arithmetic, independently recomputed by REVIEW_S15_CONVERGENCE).

---

## §5. NB3 — (N-bg), pinned. Status: PINNED; OPEN

Stated at NORMS.md l.629, as **its consumers** quantify it (NORMS l.624-628, Remark N6-5):

> **(N-bg).** **There exists** C < ∞, **uniform in** k, bounding **D³E_k^br(V) for every V in the
> small-field class** — i.e. the **Lipschitz constant of Hess E_k^br on the class**, which is what
> Lemma BR1 and δ_Sch actually consume (NORMS l.688-691), as opposed to Theorem N1-15's bound on
> **D³E_k^br(1)**, the cubic Taylor coefficient **at the trivial background**.

So (N-bg) is **not an invertibility statement at all**. It is a third-derivative/Lipschitz bound on the
*branch effective action*, and its two routes are given at NORMS l.630-637:

- **route (i), perturbative:** TOWER-VAR (a) + Lemma N1-2 at a general critical chain, *"the linear
  inputs (I3), (I4), (I5) must then be replaced by their background versions"*, plus **a composite LOC**;
- **route (ii), analytic:** BFT-4's Cauchy estimate on a k-uniform polydisc (BFT-2), **which does not
  pass through BFT-5 or (GAP-Z) at all**.

**One observation about route (i), recorded as a defect in NORMS.** NORMS l.631-634 names the objects to
be replaced as **(I3), (I4), (I5)** — which are, by NORMS' own l.116-122, *Theorem N2-lin* (LINEAR_PACKAGE
Thm 3.8), *Lemma J-str (b),(c)* (Lemma 3.1) and *Theorem N2-exp/N2-exp′* (Thms 4.2, 4.2′) — i.e. exactly
**the linear package, which is (GAP-Z)'s family** — and then in the same sentence calls that *"precisely
BFT-5 / the (G♯_0-field), (a5-G♯), (R♯_ω) family"*, which is a **different** family. **NORMS.md l.631-634
makes the same conflation as BFT_B §41.5, independently and earlier.** Two files making one error is a
pattern, not a coincidence, and it is the reason the collapse looked solid.

---

## §6. NB4 — THE COLLAPSE VERDICT. **THREE obstructions, not one.** Status: PROVEN (as stated below)

I checked all six ordered implications. **Pre-stated failure mode NBG-F1 OCCURS**, and so do my own
**NB-F2** (type mismatch) and **NB-F3** (one-way collapse, with the ledger counting the weak one).

### §6.1 The decisive argument, in three lines

1. (GAP-Z)'s own definition says it is *"the background analogue of the package constant M of
   LINEAR_PACKAGE Theorem 4.2′"* (BFT_B l.4334). Its **Z = 1 restriction is therefore M**.
2. **M is PROVEN** (LINEAR_PACKAGE FROZEN v1.1, Theorem 4.2′, l.219).
3. **(G♯_0-field) is "not attempted"** (RTARGET l.654; PROOF l.3588).

If (GAP-Z) *were* "(G♯_0-field) moved off the trivial chain", then restricting it to the trivial chain
would give (G♯_0-field), and (G♯_0-field) would be proven by step 2. It is not. **So the identification
is false, and it is false in exactly the direction the banked claim is used in.** ∎

### §6.2 Why it is false, structurally — four independent mismatches

Even setting the status arithmetic aside, (GAP-Z) ⇏ (G♯_0-field):

| | (G♯_0-field) [RTARGET §33] | (GAP-Z) [BFT_B §41] |
|---|---|---|
| background | **trivial**, U = 1, abelian linearised | **general Z** |
| slice | **abelian per-level**, h^{(i)} = 0 + Feynman | **composite** gauge-fixed (lane B's S_E) |
| norm | weighted sup/Campanato **Schauder pair**, with e^{md} decay | **ℓ²/symbol**, *"no decay claimed"* |
| output | **gauge-variant** configuration (potentials B_i) | operator invertibility ⟹ gauge-**invariant** outputs |
| extra input | the abelian **multi-level per-level-slice physical gap** | none named |

The norm row alone is fatal in that direction: **an operator bound with no decay cannot produce a
weighted sup bound with decay**, at any background. The slice row is fatal independently, and SF l.890-892
already says so for a different pair of slices.

### §6.3 The six implications, each decided

Write **(G♯f)** = (G♯_0-field), **(GZ)** = (GAP-Z), **(Nbg)** = (N-bg).

| # | implication | verdict | reason |
|---|---|---|---|
| 1 | **(GZ) ⟹ (G♯f)** | **FALSE** | §6.1 status argument + §6.2 four mismatches. (GZ) is the *input* of lane A's trivial-background chain; (G♯f) sits *above* that chain's output |
| 2 | **(G♯f) ⟹ (GZ)** | **FALSE** | (G♯f) is at Z = 1; moving to Z ≠ 1 is BFT5-red's steps 3-4 (G-pert + (G♯-patch^Ω)), and SF records (G♯-patch) as *"the B-NA wall itself, not a new sub-item of it"* (BFT_B l.3849). Different slice as well |
| 3 | **(GZ) ⟹ (Nbg)** | **FALSE as stated; TRUE only as one of ≥ 5 inputs** | (GZ) supplies the background version of **half of (I5)** (the M half). (Nbg) route (i) also needs (I3)_Z, (I4)_Z, the Combes-Thomas decay half [ARGUED, BFT_B l.4591], (N1-nd), a **composite LOC**, and (N-Q) + T-uniformity. And (Nbg) is a **third-derivative** bound; (GZ) is an inverse-Hessian bound |
| 4 | **(Nbg) ⟹ (GZ)** | **FALSE** | a Lipschitz bound on Hess E_k^br on the class says nothing about the invertibility of 𝓛_Z |
| 5 | **(G♯f) ⟹ (Nbg)** | **FALSE** | (G♯f) is at the trivial background; (Nbg) is precisely the gap from the trivial background to the class (NORMS Remark N6-5 exists only to name that gap) |
| 6 | **(Nbg) ⟹ (G♯f)** | **FALSE** | same reason as 4: wrong kind of object |

**Count: three obstructions.** No pair collapses in either direction. ARGUED-strength extra:
**(Nbg) can in principle be closed without either of the other two**, by NORMS route (ii) (BFT-4's
Cauchy estimate), which is by itself sufficient to refute "same obstruction".

### §6.4 What IS true, and what the ledger may keep

The salvageable content of [S24-note 2] is a **programme-level** statement, and it is correct:

> (GAP-Z) and the background version of the (G♯_0-field)/(a5-G♯) family would both be proven inside
> LINEAR_PACKAGE §10's single paper-scale item *"propagator bounds at a general background
> [cf. CMP 95, 96, 99]"*.

That is a statement about **which paper**, not about which theorem. The ledger consequence drawn from
it — *"ONE obstruction, not two, and this ledger must not count them twice"* (PROOF l.101-104) — **does
not follow**, because the two have different consumers, different residues and different statuses, and
because the "one" the ledger would keep is (GAP-Z), whose Z = 1 case is already proven.

### §6.5 Direction of the error, and what it costs

This is **NB-F3 exactly**: the collapse is defensible in the direction *strong ⟹ weak* (a full
general-background propagator theory would eventually yield both), and the ledger banked the *weak*
reading — that closing (GAP-Z) closes BFT-5's input. **Closing (GAP-Z) does not close BFT-5's input.**
Between them sit six theorems (W, Y, YH, W0, GU, LIN0), the gauge-variant half, and the multi-level
slice gap; the first six are **PROVEN at Z = 1** and the last two are not.

**Consequence for D5, stated plainly.** D5's premise — *"[S24] identifies it as the SAME obstruction as
BFT-5's (G♯_0-field) rather than two"* — is wrong. D5's **conclusion** — put this session's effort on the
nontrivial background — survives, because (N-bg), (GAP-Z) and BFT-5's residue all sit there. What changes
is the **count** (24 OPEN must not lose an entry here) and the **ordering** inside the background work:
(GAP-Z) is one paper-scale item; BFT-5's residue at the trivial background is a *different*, and by §9
much *smaller*, list than the ledger says.

---

## §7. NB5 — the attack from BFT-5's side. Verdict: **the three named ingredients cannot reach
## (G♯_0-field), and the obstruction is structural, not a price.** Status: PROVEN for (a) and (b);
## ARGUED for (c)

The scope prompt asked whether (a) the composite contraction **A_soft = 1/3**, (b) GREENT.md's
Green's-function bound, and (c) **A_cγ_c** bounded constant-free (so C_T is a number), together reach
(G♯_0-field) — *"and if not, exactly what is missing."* I attacked it, and the answer is that none of
the three is on the same branch of the DAG as (G♯_0-field). I state each refutation from the files, not
from the framing. **This contradicts the lead's framing in my scope prompt; per D6 I say so and why.**

### §7.1 (a) A_soft = 1/3 is NOT "one contraction for 𝔉_k in 𝔐", and it is the wrong direction

**Rebuilt rather than cited** (session-25 addendum, defect 4). Theorem N1-15 (NORMS l.507-520) states

  **N3(D³E_k^br(1)) ≤ 𝔚·L^{(d−4)k} + 𝔖·L^{d−1}/(L−1)**, with 𝔚, 𝔖 explicit,

and A_soft = 1/L is the **per-level ratio of the soft contributions**, L^{(d−1)−n} with n = k − j. Its
load-bearing step is TOWER-VAR (d) plus Lemma N1-1: D³E_k^br(1) = D³𝔉_k(1)[ζ^c·,ζ^c·,ζ^c·] is a **single
pullback** by the chain-minimiser map, so D³𝔉_k(1) is the level-0 Wilson vertex plus k soft vertices in
field-strength form, and the three exponents per soft level are (n + d − 1), −n, −n, summing to
(d−1) − n. I re-derived that arithmetic: at d = 4, L = 3 the soft sum is Σ_{n≥1} 3^{3−n} = 27/2 = **13.5**,
which is exactly the 13.5 printed at NORMS l.514, and the Wilson exponent is (d−4)k = 0 — marginal,
incurred once. The contraction is real and the count is right.

**But it is not the object the anti-circularity clause names.** REVIEW_S22 l.422-423 demands
*"one contraction for 𝔉_k in 𝔐 (COMP with (CL-0)-(CL-4) verified in 𝔐)"*. A_soft is not that:

1. **It is a bound on a trilinear form, not a contraction of a map.** N3(T) := max_x Σ_{y,z}|T(x,y,z)|
   (NORMS l.106) is an absolute row-sum norm on D³E_k^br; a contraction of 𝔉_k in 𝔐 is a Lipschitz
   constant < 1 for a fixed-point map in 𝔐. Different objects, different norms. **𝔐 does not appear in
   Theorem N1-15 at all.**
2. **The contraction PROOF.md actually names is GAP, not proven.** Proposition COMP, whose
   (CL-0)-(CL-4) *are* the one contraction in 𝔐, is recorded **GAP as written ((CL-4))** by [R22-fix]
   (PROOF l.135; re-pointed at l.6628). So the lane does not have that contraction, and A_soft is not a
   substitute for it.
3. **The direction is backwards.** Theorem N1-15's inputs are (I3), (I4), (I5) — *the frozen
   LINEAR_PACKAGE* (NORMS l.116-122) — plus (N-Q) and (N-loc)/T-uniformity. It **consumes** the linear
   package. (G♯_0-field) is a statement **above** that package's output: it is the configuration-level
   Schauder bound the package does not give. A consumer cannot produce its own supplier.
4. **It is at the trivial background** (NORMS l.624: *"Theorem N1-15 bounds D³E_k^br at the trivial
   background"*), i.e. on the near side of (N-bg), which is the wall D5 sends this session to.

**And the mechanism that makes A_soft work is the one that excludes it from (G♯_0-field).**
NORMS Remark N6-4 (l.613-619) is explicit: COMP-F1, *"SF S4-1's '(a5-G) is FALSE in ℓ^∞ → ℓ^∞'"*, and
LED-unif's Π_ex |x|^{−4} tail are statements about **extending** the response map to sources that are not
of divergence/exact form, and *"Theorem N1-15 never performs that extension: every response it uses is
the response to level-k data — i.e. to d_kX — which is exact, not merely closed."* **(G♯_0-field) is
exactly that extension**: its hypothesis is a collection of divergence-form sources G_l at every level
plus plain level-0 currents (RTARGET l.592-605). So A_soft's uniformity is bought by avoiding precisely
the sources (G♯_0-field) must accept. **Pre-stated failure mode NB-F5 OCCURS**, in the "wrong direction"
form rather than the circularity form: no circularity, but no reach either.

### §7.2 (b) GREENT bounds the FREE level-0 Laplacian, and a |x|^{−d} kernel is not an ℓ^∞ bound

GREENT's object is fixed at GREENT l.138-152: level 0, the **Hodge Laplacian Δ_0 on level-0 2-forms with
no gauge field**, acting componentwise as the scalar Laplacian, on Λ_0 = (Z/R_0)^d with R_0 = T·L^k. Its
theorems are (GT-1) |∇_μ G_R(x)| ≤ C_1|x|_2^{−(d−1)} and (GT-2) |∇_μ∇_λ G_R(x)| ≤ C_2|x|_2^{−d},
R-uniformly, C_1 = 54, C_2 = 1703 at d = 4.

Two reasons this cannot supply (G♯_0-field)'s fine half, the half whose named failure mode (G0-F2,
RTARGET l.613-614) is *"the fine-level Calderón–Zygmund singularity: no bound in sup norm alone for f_0"*:

1. **A |x|^{−d} kernel bound is not an ℓ^∞ → ℓ^∞ bound, because the lattice sum diverges.** This is the
   one arithmetic fact I leaned on, so I checked it rather than asserting it — **check nb1**, criteria
   `checks/nb1_criteria.md` (born 21:19Z, before `checks/nb1_logdiv.py`), output `checks/nb1_out.txt`:

   - **nb1-A: PASS.** Σ_{0<|x|_2≤R, x∈Z⁴}|x|_2^{−4} grows by **13.532, 13.545, 13.683** per octave
     (R: 3→6→12→24) against the predicted 2π² ln 2 = **13.682** — equal mass per octave, i.e. logarithmic
     divergence, agreeing with the continuum value to 0.01 % by the third octave.
   - **nb1-B: the DESIGNED-FAIL CONTROL WORKED.** The same criterion applied at exponent 5, where the sum
     must converge, **FAILS** it: increments 3.218, 1.622, 0.822 — halving per octave, far outside the
     band. So the criterion can discriminate; it is not a tautology.
   - **nb1-C: PASS.** N(24)/24⁴ = 4.9378 against π²/2 = 4.9348 (0.06 %), so the enumeration is right.

   Therefore (GT-2) gives a bound whose ℓ¹ kernel mass over a box of side R is ≍ 2π² ln R: it reproduces
   exactly the **log T** that GREENT §G3.2 already identifies as irreducible, and it does **not** close
   the sup-norm gap. The Hölder/Campanato route (LES-div) remains the only one, as PROOF l.308-311 says.
2. **It is at the trivial background and contains no gauge field**, so it is on the near side of both
   (N-bg) and (GAP-Z). GREENT's own §G5 says as much (l.611, l.671: *"(N-bg) and (H-C)'s C_♭ clause are
   untouched"*).

GREENT is a real result in the right technical family; it is simply the free-field input, which the
lane has had since LINEAR_PACKAGE. **It makes the T-price honest; it does not move (G♯_0-field).**

### §7.3 (c) A_cγ_c / C_T is on a different branch of the DAG

EPSSTAR Theorem ES-1 (A_cγ_c ≤ (1+√6)·C_S1(q,m)/m) prices the **Moser absorption constant of the energy
inequality** feeding **C_T**, whose consumer is the **(CLS-min) → RLARGE interface** on the **large-field**
branch (HANDOFF item 4; CONST_T.md). (G♯_0-field) is a **small-field, linearised, trivial-background**
Schauder estimate. There is no edge between them in either direction; making C_T an actual number does
not bear on BFT-5 at all. Status of this paragraph: **ARGUED** — I traced the consumers, I did not
re-derive ES-1.

### §7.4 What IS missing — named as statements, after [S24-fix 2]

This is the useful half of NB5. Once the slice is S_E (D1) and [S24-fix 2]'s three confirmations are
applied, BFT-5's residue **at the trivial background and m = 0** is much smaller than PROOF's table says,
and it is a *different* list:

| what BFT-5 needs at m = 0, trivial background | status now | source |
|---|---|---|
| invertibility + Schauder bound, gauge-**invariant** outputs, level-wise co-closed classes | **PROVEN as an implication**, every input CONFIRMED | [S24-fix 2]; Corollary LIN0 CONFIRMED in scope (REVIEW_BFT_A_S6 l.25-26) |
| the **gauge-variant / potential half**: potential component | **PROVEN-HERE** (Corollary FP), data + residual-type sources | BFT_A l.938-939, §13.13 l.1148-1149 |
| the **gauge-variant / gradient half** = LRL (b) | **PROVEN for the data map**, T ≥ 5, 0 ≤ m < m_*' | Corollary EP-LRL(b) + Theorem RH_m: BFT_B l.2661-2662, l.2819 |
| (G♯-rough)'s curvature half | **PROVEN-HERE** at m = 0, 0 < α < θ (Corollary G♯R) | BFT_A §23.10 l.2059, l.2148 |
| **composite-co-closed** source class (D1's restatement), curvature half | **CONDITIONAL on (CO-fun)** | BFT_B §31.2 l.3802; (NC-Γ)_cc |
| (R♯_ω) | *"a precise statement, not a proven one"* | PROOF l.3661; BFT_B §32.2 input 2 |
| (G♯-patch^Ω) | OPEN, but **narrowed**: CL-iv supplies the smallness, only the gluing remains | BFT_B §32.2 |
| (G♯-rough)/(G♯-up) at **α = θ** | OPEN, *"possibly false"* | BFT_A l.2359, l.2878 |

**The single smallest remaining missing input, named as a statement: (CO-fun).** BFT_B l.3802 states it
in full. It is the only item in that list that is (i) a single scalar estimate, (ii) already stated with
all its quantifiers, (iii) the sole thing standing between (NC-Γ)_cc's curvature half and BFT-5 clause
(b) **for the composite-co-closed class that lead decision D1 chose**, and (iv) equipped with two proven
structural facts to attack it with (Lemma FT (i): the funnel pieces are supported on block-interior links
of the blocks carrying the composite divergence; Lemma FT (ii): their coarse size is a geometric
convolution with **no power of L^{k−l}**). Everything else on the list is either proven, or paper-scale
((G♯-patch^Ω), (R♯_ω)), or possibly false ((G♯-rough) at α = θ).

*Not claimed:* that discharging (CO-fun) discharges BFT-5. It discharges one clause of one half at
m = 0 and the trivial background. **(GAP-Z) is still the paper-scale item behind the background move**,
and §6 says it is a different item from this one.

---

## §8. NB7 — the weight pair. **BFT-5 inherits it, and as written the target has NO admissible
## exponent.** Status: PROVEN as a statement about the target as written

BFT-5 is stated *"in the 𝔐-pair"* (REVIEW_S22 l.419). 𝔐 is defined at REVIEW_S22 l.392-396, and **one
symbol θ_w does three jobs there**:

1. the **displacement** weight: *"level-j curvature and soft-fluctuation components are weighted by
   L^{θ_w(k−j)}"* (l.393);
2. the **source** weight: *"nonlinear sources in a divergence-form norm Y (SF/RTARGET §33's pair with
   **ω_l = L^{θ_w(k−l)}**)"* (l.394);
3. BFT-1's **background-decay rate**: *"the own-units plaquette logs of U_j and the soft fluctuations
   ρ(U_j, U_{j+1}) are ≤ C_0L^{−θ_w(k−j)}ε"* (l.410);

and the Claim quantifies **one** of them: *"there exist … θ_w ∈ (0, 2]"* (l.399).

**The four live windows on that one symbol, by file:line:**

| window | value | where |
|---|---|---|
| lane A's proven pair (𝔐^∇, 𝒴^∇) | **α ≤ θ ≤ 1 − α, α ≤ ½** (worked at α = ¼, θ = ½) | BFT_A l.396-397, l.827, l.880 |
| SF's own consumer statement (a5-G♯) | **θ ∈ (0, 1]** | SF l.680 |
| RTARGET §33, where (G♯_0-field) lives | **θ ∈ (0, 1]** | RTARGET l.586 |
| the BFT target's existential | **θ_w ∈ (0, 2]** | REVIEW_S22 l.399 |
| **what the composite contraction REQUIRES** | **θ_w^c = 2, θ_w^r = 3, θ_A = 1** | NORMS §N7; [S24-fix 3], PROOF l.30-34 |

I verified the requirement rather than quoting it: with A = L^{d − θ_w^r − 2θ_A} and θ_A = min(1, θ_w^c − 1),
the canonical triple (2, 3, 1) at d = 4 gives **A = L^{4−3−2} = L^{−1} = 1/3 = A_soft** — i.e. **the
residual weight that A_soft = 1/3 is built on is exactly θ_w^r = 3.**

**Consequences, in order of how much they hurt:**

1. **θ_w^r = 3 is outside every one of the four windows above, including the target's own (0, 2].**
   [S24-fix 3] said BFT-1's existential "cannot support the composite route as written"; what it did
   **not** say is that **the one contraction the lane actually has (A_soft = 1/3) is itself at a weight
   BFT-1 as written forbids.** That is the same defect pointed the other way, and it is sharper.
2. **The ceiling is as binding as the floor, and nobody has recorded it.** Because 𝔐's source leg is
   lane A's ω_l, and lane A's estimates ((H-inv+), BL-7, GU, Corollary G♯R) are proven only for
   θ ≤ 1 − α ≤ ¾, **widening the existential to (0, 3] does not fix BFT**: the curvature leg wants 2,
   the residual leg wants 3, and the source leg is capped below 1. The repair is not a wider interval;
   it is **decoupling three (really four) exponents** — θ_w^c, θ_w^r, θ_A for the background decay and a
   separate θ_ω for the source weight — and restating 𝔐 and BFT-1/BFT-5 with all of them.
3. **So BFT-5 does inherit the weight-pair requirement**, through 𝔐, and inherits it in a form that
   makes the clause as written unsatisfiable. This is a **defect in the statement, upstream of any
   proof**: no amount of work on (G♯_0-field), (GAP-Z) or (CO-fun) can discharge a clause whose norm has
   no admissible parameter.

*Honest scope.* This is a statement about **the target as written**. If the intended reading is that
the three jobs were always meant to be different exponents and REVIEW_S22's prose merely reused the
letter, then BFT-5 does not inherit the pair directly — but then the target must be rewritten before it
can be proven or refuted, and the rewrite is the work. Either way the next edit to BFT is the same one.

---

## §9. NB6 — the BFT clause table, audited clause by clause. **Stale in EIGHT further places**,
## beyond [S24-fix 2]'s three. Status: PROVEN (each entry carries its file:line)

The table is at **PROOF.md l.6805-6813** (the scope prompt's "l.6695 area"; the heading is at l.6805 and
the four rows at l.6810-6813). Its own preamble says it is *"quoted, not re-judged"* from
REVIEW_BFT_B_S5/S4 — i.e. it was a transcription in session 23 and has not been re-judged since, while
sessions 9, 10, 11 and 24 moved eight of its entries. **Pre-stated failure mode NB-F6 does NOT occur.**

**A line-number warning for whoever edits it.** BFT_B §43's FOR OTHER FILES (l.4770) asks for the
BFT-0/1/2 edit *"at l.6731"*. PROOF.md has grown; the row is now at **l.6810**. BFT_B §32.2's citations
of *"PROOF l.3473, l.6698"* for (G♯_0-field) likewise no longer resolve (l.6698 is now inside [S23]'s
pointer list). **Edit by row content, not by the quoted line numbers.**

### §9.1 The three already recorded ([S24-fix 2]), for completeness
(CO-0) = lane A's **Theorem W0, CONFIRMED**; (CO-up) = **Theorem GU, CONFIRMED**; **(SB) is not an input
at all** (Theorem CO-B removes it).

### §9.2 The eight further stalenesses

**Row BFT-0/1/2**

- **S4. "(G♯-rough) curvature half" is PROVEN.** It is **Corollary G♯R**, PROVEN-HERE at m = 0, trivial
  background, all gauge-invariant outputs, 0 < α < θ (BFT_A §23.10 l.2059; table l.2148; scope restated
  l.2366). The residue is **α = θ only, OPEN and "possibly false"** (BFT_A l.2359, l.2878). The row
  lists the whole clause as an open input.
- **S5. "(Res-Hölder)" is PROVEN for the data map and closed for the composite-co-closed class.**
  Theorem RH / RHT at m = 0 and **Theorem RH_m** are PROVEN-HERE (BFT_B l.2816-2819; *"(Res-Hölder)_m
  for the data map PROVEN"*), and [S24-fix 2] itself records (Res-Hölder) = EP-F4 closed at m = 0 via
  Theorem RHT-cc. The genuine residue is **(Res-Hölder) for the non-co-closed remainder V_l**
  ([RBB6-fix RS6-1], BFT_B l.2631), which is outside Setting LIN. The row should name V_l.
- **S6. "LRL (b) ⇐ (Res-Hölder)_m (T ≥ 5)" has been discharged for the data map.** Corollary EP-LRL(b)
  with Theorem RH_m gives *"lane A's LRL (b) holds for T ≥ 5, 0 ≤ m < m′ < m_*′"* (BFT_B l.2661-2662).
  Since **the gradient half of (G♯_0-field^∇) needs LRL (b)** (BFT_A l.1660) and its **potential half is
  Corollary FP, PROVEN-HERE** (BFT_A l.938-939, l.1148-1149), the gauge-variant half of the
  trivial-background package is in hand for data and residual-type sources. The row still presents it as
  a live conditional.
- **S7. "background-covariant slice = (N1)" is superseded.** BFT_B §40-§41 split it:
  **(N1-a) PROVEN** (narrowed to the pinned class), **(N1-d) CONDITIONAL on the new named item (N1-nd)**,
  **(N1-c) PROVEN as an implication of Corollary CL-iv**, **(N1-b)/(N1-e) ARGUED**, with consumption
  fixed by **Proposition N1-CONS** (BFT_B l.4509, l.4728). Also **(N1-a) supplies (FP♯′) for S_E^Z**
  (BFT_B l.4502), which the row lists separately as open. **This edit was requested by BFT_B §43 in
  session 11 and has never been applied.**

**Row BFT-4**

- **S8. "(CovLift) [OPEN, nonabelian only]" understates it: one of its clauses is PROVEN FALSE.**
  **Proposition GZ-FALSE** (PROVEN, BFT_B §41): the non-residual g_Z clause **is false at every θ > 0,
  for every lift** — a currency mismatch, since BFT-1's **maximal** θ_w^c = 2 gives no coarse-curvature
  decay while the clause demands decay at rate θ, and θ > 0 is load-bearing because Theorem GU needs
  θ > α > 0 in the same slot. **Theorem Cg-nr** restates the (G)-slot representative, and the residue is
  the **new named OPEN item (CURV-dec)**, which the table does not carry. Recorded at [S24-note 3]
  (PROOF l.106-110) but **never propagated into the table**.
- **S9. "(W-lin-Π) ⟺ (H-inv+)" now resolves at m = 0.** [S24-fix 2] makes (H-inv+) at m = 0, trivial
  background, level-wise co-closed classes on 𝒞_glob **PROVEN as an implication with every input
  CONFIRMED**; so (W-lin-Π) holds in that scope. (It does **not** at m > 0.)

**Row BFT-5** — this row is stale in every clause it contains

- **S10. "no status recorded in any BFT review or lane file" is FALSE.** Lane B owns BFT-5 (lead
  decision D1) and **states it**: **(BFT-5_E)**, BFT_B §32.1, with clauses (a)-(d); **Proposition
  BFT5-red** gives the reduction (§32.2) and an explicit honest status; **clause (c) is PROVEN**
  (Proposition NCR, §31.1); clause (b)'s curvature half is **CONDITIONAL on (CO-fun)**; clause (d)'s
  weighted form additionally needs lane A's DX_m, DB_m.
- **S11. The open-input list is wrong in all three entries.**
  (i) **(G♯_0-field)** is RTARGET §33's statement on the **abelian per-level slice** (l.599-600) with the
  **per-level-slice** physical gap (PROOF l.3589) — a slice lead decisions D1/D2 have abandoned. On S_E
  the live name is **(G♯_0-field^∇)** (BFT_A l.266, l.327, l.559), and by S6 both of its halves are in
  hand at the trivial background for data and residual-type sources.
  (ii) **(G♯-patch)** is narrowed to **(G♯-patch^Ω)** by BFT_B §32.2 given Corollary CL-iv, which
  supplies the X_c-smallness on every frame, k- and T-uniformly, so only the gluing remains.
  (iii) **(CO-fun)** is missing from the row and is the live conditional on clause (b).
- **S12 (and this is the one with the largest ledger consequence). The row must NOT be merged with the
  nontrivial-background row.** [S24-note 2] (PROOF l.101-104) instructs the ledger not to count
  (GAP-Z) and (G♯_0-field) twice. **§6 of this file refutes that identification in both directions**:
  (GAP-Z)|_{Z=1} is Theorem 4.2′'s M, which is **PROVEN**, while (G♯_0-field) is **"not attempted"**;
  and they differ in background, slice, norm type and output class. **Pre-stated failure mode NBG-F1
  OCCURS, and the open count must not be reduced here.**

### §9.3 Two further defects of the table as an object, not of its rows

- **S13. There is no BFT-6 row**, although [S24-fix 4] (PROOF l.37-40) promotes **(BB-mix)** to BFT-6 and
  calls it *"the single gate on layer 2's expansion"*.
- **S14. The table has no note on 𝔐's exponent**, although §8 above shows that **as written the target
  has no admissible θ_w**, which makes every row's "in 𝔐" conditional on a restatement.

### §9.4 Append-ready replacement text

*For PROOF.md, to replace the heading and four rows at l.6805-6813. Written by T55-E; I have not edited
PROOF.md. Statuses are quoted with their sources; nothing here is a new judgement of a lane item except
§6's refutation, which is labelled as mine.*

```
*BFT clause status (re-audited in session 25 by NBG_B §9, clause by clause, against the lane files as
they now stand; the session-23 table was transcribed from REVIEW_BFT_B_S5/S4 and "quoted, not
re-judged", and sessions 9-11 and 24 have since moved eleven of its entries). Line numbers quoted by
BFT_B §43 (l.6731) and BFT_B §32.2 (l.3473, l.6698) have drifted; edit by row content.*

| clause | status | open inputs, as they now stand |
|---|---|---|
| BFT-0/1/2 | OPEN on 𝒞_glob. Lane claim (BFT_A l.306): "Theorem BA: BFT-0/1/2 on 𝒞_glob ⇐ (H-lin^∇) + (H-rem^∇) + (FP♯′), PROVEN as implication". The X_s halves (XR, XB, HX) and the data/residual sources (Theorem W) PROVEN; the slice is no longer open at the linear level (S_E). **(H-inv+) at m = 0, trivial background, level-wise co-closed classes on 𝒞_glob is PROVEN as an implication with every input CONFIRMED** ([S24-fix 2]) | at m = 0: **(Res-Hölder) for the non-co-closed remainder V_l only** ([RBB6-fix RS6-1], BFT_B l.2631); **(G♯-rough)/(G♯-up) at α = θ** (OPEN, "possibly false", BFT_A l.2359, l.2878). **LRL (b) is DISCHARGED for the data map** (Corollary EP-LRL(b) + Theorem RH_m, T ≥ 5, 0 ≤ m < m_*′, BFT_B l.2661). Background-covariant slice: **(N1-a) PROVEN** (pinned class; it also supplies **(FP♯′)** for S_E^Z, BFT_B l.4502), **(N1-d) CONDITIONAL on (N1-nd)**, **(N1-c) PROVEN as an implication of Corollary CL-iv**, (N1-b)/(N1-e) ARGUED; consumption fixed by **Proposition N1-CONS**. At m > 0: lane A's DX_m, DB_m, (G♯-res), (G♯_0-field^∇)_m, (G♯_0-fine-up), (H-rem^∇), (H-op). Off 𝒞_glob: (UHL), (SL-cov), Z^sm. PROOF side: BFT-0's identification clause = (CL-4) (Proposition COMP **GAP as written**, [R22-fix]) |
| BFT-3 | **k = 1 PROVEN** (lane B: Theorem BB-3_1); k ≥ 2 ⇐ weighted (H-inv+)_m, m > 0; gauge-invariant data part by Theorem W. **n ≤ 4 only** — all-order decay is BFT-6 | weighted (H-inv+)_m, i.e. lane A's m > 0 items above |
| BFT-4 | **k = 1 PROVEN** (gauge-invariant pieces); k ≥ 2 bounded polymers on 𝒞_glob ⇐ Theorem RW^∇_k-Π(E) [(W-Π) PROVEN; **(W-lin-Π) holds at m = 0, trivial background, level-wise co-closed classes**, by [S24-fix 2]] + (W-comm) [GAP 1 plain rows] + (W-loc) + (f) + (E3^∇) [ARGUED] + (I-id) | **(CovLift): its non-residual g_Z clause at θ > 0 is PROVEN FALSE for every lift** (Proposition GZ-FALSE, [S24-note 3]); restated by **Theorem Cg-nr**, leaving the new named item **(CURV-dec) [OPEN]**. (Mult-Y) [GAP-1 family], (Pair-loc) [ARGUED], (I-id)_Z [ARGUED]; the slice + Feynman mixed form OPEN; off 𝒞_glob GI-off ARGUED |
| BFT-5 | **OWNED BY LANE B (D1) AND STATED**: (BFT-5_E), BFT_B §32.1, clauses (a)-(d), with Proposition BFT5-red (§32.2) as the reduction. **Clause (c) PROVEN** (Proposition NCR, §31.1). Clause (b)'s residual half PROVEN (Theorem RHT-cc); its curvature half **CONDITIONAL on (CO-fun)**. Clause (d) (m > 0) additionally needs lane A's DX_m, DB_m. The session-23 entry "no status recorded in any BFT review or lane file" is superseded | **(CO-fun)** [OPEN, BFT_B §31.2 — the smallest remaining input]; **(R♯_ω)** ["a precise statement, not a proven one", PROOF l.3661]; **(G♯-patch^Ω)** [OPEN, narrowed by Corollary CL-iv, which supplies the smallness]; **(G♯-rough) at α = θ**. The trivial-background linear input is lane A's **(H-inv+)** on S_E (above), **not** RTARGET §33's (G♯_0-field), which is stated on the abandoned abelian per-level slice and carries that slice's physical gap |
| BFT-6 = (BB-mix) | **OPEN** ([S24-fix 4]); the single gate on layer 2's cluster expansion, and what (L-loc)_k is re-pointed to since BFT-3 stops at n ≤ 4 | (BB-mix) |

**Note on 𝔐 (binding on every row above).** REVIEW_S22 l.392-399 uses ONE symbol θ_w for three jobs —
𝔐's displacement weight (l.393), 𝔐's source weight ω_l (l.394) and BFT-1's background-decay rate
(l.410) — and quantifies it once, θ_w ∈ (0, 2]. The composite contraction A_soft = 1/L is built on
θ_w^r = d − 1 = 3 with θ_w^c = 2, θ_A = 1 ([S24-fix 3]; A = L^{d−θ_w^r−2θ_A} = L^{−1}), which is outside
(0, 2]; lane A's estimates on the same ω_l are proven only for α ≤ θ ≤ 1 − α ≤ ¾ (BFT_A l.396, l.827);
and SF's own consumer statement (a5-G♯) says θ ∈ (0, 1] (SF l.680). **Four incompatible windows on one
symbol: widening the interval does not repair it, and the repair is to decouple θ_w^c, θ_w^r, θ_A and
the source weight θ_ω and restate 𝔐, BFT-1 and BFT-5 with all four.** (NBG_B §8.)

**Note on the count.** [S24-note 2]'s instruction not to count (GAP-Z) and (G♯_0-field) as two items is
**withdrawn by NBG_B §6**: (GAP-Z)|_{Z=1} is LINEAR_PACKAGE Theorem 4.2′'s M, which is PROVEN, while
(G♯_0-field) is "not attempted" (RTARGET l.654), so they cannot be one statement; and they differ in
background, slice, norm type and output class. Failure mode NBG-F1 of RTARGET §54 OCCURS. The
programme-level reading — that both would be proven inside LINEAR_PACKAGE §10's single paper-scale item
"propagator bounds at a general background [cf. CMP 95, 96, 99]" — is correct and may be kept.
```

---

## §10. Check record (one check, with its designed-FAIL control)

**nb1.** Criteria `checks/nb1_criteria.md`, **born 2026-10-28T21:19Z, before `checks/nb1_logdiv.py`
existed**; no constant in the criteria is derived in this session (only d = 4, |S³| = 2π², π²/2, and
the exponents 4 and 5). No criterion was retuned, no re-run, no post-hoc probe.

**No numeric lock taken.** Plain Python 3, integers and floats, no numpy, no BLAS — DRIVE_BRIEF rule 6
exempts this. Environment: `nice -n 10`, `python3 -I`, `PYTHONDONTWRITEBYTECODE=1`,
OMP/OPENBLAS/MKL/VECLIB thread variables = 1. Runtime a few seconds, memory negligible.

| id | verdict | numbers |
|---|---|---|
| **nb1-A** (claim: Σ_{Z⁴}\|x\|^{−4} diverges logarithmically) | **PASS** | octave increments 13.532, 13.545, 13.683 vs 2π²ln2 = 13.682 |
| **nb1-B** (DESIGNED-FAIL CONTROL at exponent 5) | **CONTROL WORKED — it FAILS nb1-A's criterion**, as required | increments 3.218, 1.622, 0.822; band_ok=False, nondecay_ok=False |
| **nb1-C** (enumeration sanity) | **PASS** | N(24)/24⁴ = 4.9378 vs π²/2 = 4.9348, 0.06 % |

Output kept unaltered at `checks/nb1_out.txt` (stderr empty, `checks/nb1_err.txt`).
**What nb1 decides, and only that:** a kernel bound \|K(x)\| ≤ C\|x\|^{−d} on Z^d is not an ℓ^∞ → ℓ^∞
bound. It does **not** by itself decide anything about (G♯_0-field); §7.2's conclusion is nb1 plus the
reading of RTARGET's failure mode (G0-F2), which is argument.

---

## §11. Tally, scope and what I did not do

**PROVEN this session (in this file):**
- **§6, the collapse verdict.** (N-bg), (GAP-Z) and (G♯_0-field) are **three** obstructions; all six
  ordered implications fail with the quantifiers their consumers need. RTARGET §54's **NBG-F1 OCCURS**;
  my **NB-F2** (type mismatch) and **NB-F3** (one-way collapse, ledger counting the weak one) occur too.
- **§7.1**, that A_soft = 1/3 is not the contraction the anti-circularity clause names and cannot reach
  (G♯_0-field) — with the arithmetic rebuilt (Σ_{n≥1}L^{(d−1)−n} = L^{d−1}/(L−1) = 27/2 = 13.5 at
  d = 4, L = 3, matching NORMS l.511-516) and with **NORMS Remark N6-4 showing that the mechanism which
  makes A_soft uniform is exactly what excludes it from (G♯_0-field)'s source class**.
- **§7.2**, via check nb1, that (GT-2)'s \|x\|^{−d} bound is not an ℓ^∞ bound, so GREENT does not close
  the fine half.
- **§8**, that **BFT as written has no admissible θ_w** (four incompatible windows on one symbol).
- **§9**, that the BFT clause table is stale in **eight** further places (S4-S11) plus two defects of
  the table as an object (S13, S14). **NB-F6 does not occur.**

**ARGUED:** §7.3 (A_cγ_c/C_T is on the large-field branch, no edge to BFT-5 — consumers traced, ES-1 not
re-derived); §6.3's row 3 refinement (that (GAP-Z) is one of ≥ 5 inputs to (N-bg) route (i)); §6.4's
reading that (N-bg) route (ii) alone refutes "same obstruction".

**Nothing new is PROVEN about (G♯_0-field), (GAP-Z) or (N-bg) themselves.** The attack from BFT-5's
side produced a **negative** result and a corrected input list, not a step of the proof. I report that
as a fail against the optimistic reading of my own NB5.

**Robustness of §6 against the banked-review rule.** §6.1 leans on one banked PROVEN (Theorem 4.2′'s M)
and one banked negative ("not attempted"). I did **not** re-derive Theorem 4.2′. If it were later
downgraded, **§6.2's four structural mismatches (background, slice, norm type, output class) stand on
their own** and the verdict is unchanged; §6.1 is the short proof, §6.2 the robust one.

**Explicit scope limitations:**
1. I did not re-derive GREENT's C₁ = 54 or C₂ = 1703; §7.2's conclusion needs only the *shape*
   \|x\|^{−d} and the divergence of its lattice sum, both of which I checked.
2. **§9's entries S4, S5, S6, S9 rest on banked reviews and banked PROVEN-HEREs** (REVIEW_BFT_A_S6's
   confirmations; Corollary G♯R; Theorem RH_m; Corollary EP-LRL(b)) that I read but did not re-derive.
   Per the session rule, treat them as **evidence that the table is stale**, which is all §9 claims, and
   not as certificates that those items are closed.
3. I did not open (CO-fun), (R♯_ω) or (G♯-patch^Ω).
4. I did not coordinate with T55-D (NBG_A.md) and have not read it; the two reads are independent by
   design, and a disagreement between them is information, not an error.

**The single smallest remaining missing input in my scope: (CO-fun)** (BFT_B §31.2, l.3802) — stated in
full, one scalar estimate, the sole conditional on BFT-5 clause (b)'s curvature half for the
composite-co-closed class that lead decision D1 chose, and equipped with two proven structural handles
(Lemma FT (i) block-interior support; Lemma FT (ii) geometric convolution with **no power of L^{k−l}**).
Behind it, and genuinely paper-scale, **(GAP-Z)** — a *different* item.

---

## FOR OTHER FILES (not edited)

**PROOF.md (master ledger).**
1. **Replace the BFT clause table at l.6805-6813** with §9.4's append-ready text (five rows, two notes).
2. **Withdraw [S24-note 2]** (l.101-104). Its instruction *"the nontrivial background and BFT-5 are ONE
   obstruction, not two, and this ledger must not count them twice"* is refuted in both directions by
   §6. The open count must not be reduced on its account. Its salvageable form — that both items would
   be proven inside LINEAR_PACKAGE §10's one paper-scale *"propagator bounds at a general background"* —
   may be kept as a **programme** statement, explicitly not a ledger identification.
3. **Add a successor to [S24-fix 3]:** the ceiling, not only the floor. The same θ_w is 𝔐's source
   weight, which lane A's estimates cap at θ ≤ 1 − α ≤ ¾, so widening BFT-1's existential does not
   repair BFT. Four exponents must be decoupled (§8).
4. **Carry (CURV-dec)** as a named OPEN item in the BFT-4 row (it exists in [S24-note 3] but not in the
   table).

**RTARGET.md.** §54's failure mode **NBG-F1 OCCURS**; and §54 item (i) of the §53 list (RTARGET l.1042,
*"(GAP-Z) IS BFT-5's (G♯_0-field): the nontrivial background and BFT-5 are one obstruction"*) should be
marked REVERSED, against whoever banked it (BFT_B §41.5/§43, carried by the lead into [S24-note 2]).

**BFT_B.md (lane B, the owner of §41.5 and §43).** §41.5 (iii) and §43 item 4 identify (GAP-Z) with
(G♯_0-field). The identification is wrong as a statement identity (§6) although the Z = 1 → Z ≠ 1
*analogy* is right. The correct sentence is: **(GAP-Z) is the Z-analogue of LINEAR_PACKAGE Theorem 4.2′'s
M — i.e. of the INPUT of lane A's trivial-background chain — whereas (G♯_0-field) is a configuration-level
Schauder statement ABOVE that chain's OUTPUT, on a different slice.** §41.5's own l.4596 writes the chain
out and shows the distance. Also: §32.2's line-number citations for (G♯_0-field) (*PROOF l.3473, l.6698*)
no longer resolve, and §43's *"the BFT-0/1/2 row at l.6731"* is now l.6810.

**NORMS.md.** l.631-634 (route (i) of (N-bg)) names the objects to be replaced as **(I3), (I4), (I5)** —
the linear package, i.e. (GAP-Z)'s family — and in the same sentence calls them *"precisely BFT-5 / the
(G♯_0-field), (a5-G♯), (R♯_ω) family"*. Those are two different families (§5). This is the same
conflation as BFT_B §41.5, made independently and earlier, and is probably its source. Suggested
replacement: *"the background versions of (I3), (I4), (I5) — i.e. (GAP-Z) plus the Combes-Thomas decay
half plus the Tier-A/B/C transport of BFT_B §41 — together with a composite LOC; BFT-5's family
((G♯_0-field), (a5-G♯), (R♯_ω)) is then what converts those into the class statement, and is a separate
list."*

**BFT_A.md (lane A).** Two requests, both bookkeeping:
(i) the six-member (G♯_0-\*) family plus (G♯_0-field^∇) is a live collision (§2); a rename would help
most in PROOF's clause table, where "(G♯_0-field)" currently points at the abandoned per-level slice.
(ii) §9's S4/S6 read Corollary G♯R and LRL (b) as discharging their clauses at m = 0; if lane A disagrees
with that reading, say so, because §9.4's table encodes it.

**SF.md.** SF l.680's (a5-G♯) quantifies **θ ∈ (0, 1]**, while the composite contraction it ultimately
consumes needs θ_w^r = 3 (§8). SF is the consumer that would discover this last; flagging it now.

---

## §12. Addendum to §6 (appended after §11; §6 is unchanged): the obvious objection, answered

A reader defending the collapse will say: *"(GAP-Z) is a bound on the inverse of the gauge-fixed
**composite chain Hessian**; LINEAR_PACKAGE Theorem 4.2′ bounds **response-map symbols**. So
(GAP-Z)|_{Z=1} is strictly more than M, and §6.1's status argument does not apply."*

That objection is a **dilemma, and both horns give §6's verdict.**

- **Horn 1: (GAP-Z)|_{Z=1} *is* M.** This is what BFT_B asserts, twice and in its own words —
  *"the background analogue of the package constant M of LINEAR_PACKAGE Theorem 4.2′"* (l.4334),
  *"the M half, with no decay claimed"* (l.4590) — and it is what Theorem TRANSP needs, since TRANSP's
  conclusion is (H-inv+)_Z, the Z-analogue of Corollary LIN0, which at Z = 1 is derived **from** M
  through W, Y, YH, W0, GU (l.4596). Then §6.1 applies verbatim: M is PROVEN, (G♯_0-field) is "not
  attempted", so they are not one statement.
- **Horn 2: (GAP-Z)|_{Z=1} is strictly more than M.** Then (GAP-Z) is **not** "the background analogue
  of M", §41.5's own characterisation of it is wrong, and the sentence that carries the collapse
  (*"it is lane A's U = 1 package at Z ≠ 1"*, l.4594) is false on its face — because *"lane A's U = 1
  package"* is used in this lane for **two different things**: LINEAR_PACKAGE (PROVEN, frozen v1.1) and
  (G♯_0-field) (BFT_B §32.2 item 1: *"Status quoted: OPEN, lane A's U = 1 package"*). **The collapse is
  carried by that one ambiguous phrase.** On horn 2 the identification has no stated content at all, and
  §6.2's four structural mismatches (background, slice, norm type, output class) are the only thing left
  to judge it by. They refute it.

So the verdict does not depend on which horn is taken, and in particular does not depend on Theorem
4.2′'s banked PROVEN. **What the dilemma adds is the diagnosis:** this is systemic defect 1 of the
session addendum, operating on the phrase *"lane A's U = 1 package"* rather than on a single letter —
the same mechanism as the two η_1, and with a comparable consequence, since it is what persuaded the
ledger to merge two items of very different size.
