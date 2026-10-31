# KN_ADOPT — H1 (the S4′ weights) and the RLARGE §6 adoption patch

Owner of this file: the T55-A worker, session 25 (ym4d-proof lane).
Writable by me: **this file** and new files under `checks/` prefixed `kn1_`. Nothing else, anywhere.
**No git command will be run by me.**

---

## §0. PRE-STATED (first edit of this file)

**This is the first edit made to this file. UTC time of this edit: 2026-10-28T21:04Z.**

Statements only. This section cites **nothing produced in session 25** — not the lead's session-25 brief,
not RTARGET §54, not any session-25 worker file. The figures named below as *under test* are transcribed
from **ARS_FIX.md (session 24)** and are flagged as objects of audit, **never as inputs**: per the lane's
standing rule, a banked PROVEN is evidence and not a certificate, and anything load-bearing is re-derived
here rather than cited. Written **before** reading RLARGE.md §2 / §6, PROOF.md's S4′ definition,
EXISTENCE.md's Lemma KN, or any of the arithmetic below.

### §0.1 The question I was given, restated in my own words

ARS_FIX.md §3.2-§3.3 rebuilds **Lemma KN′** and **Corollary KN-step′** on our structures and proves them
from seven hypotheses H1-H7. Its §3.3 finds **H1** — that the averaged transporter M̄_c is a mixture
Σ_i w_i T_i with **w_i ≥ 0 and Σ_i w_i = 1** — to be the **only** hypothesis RLARGE.md does not state;
RLARGE l.996 says only that *"M̄_c is a mean of the T^σ_y"*. ARS_FIX therefore labels the whole 82-decade
adoption **CONDITIONAL on one word** and routes the repair to RLARGE as conditional (its §8.1 item 4,
§8.6 item 3).

**My target T55-A is to settle H1 from the DEFINITION of the S4′ average, not from the word "mean".**

### §0.2 Pre-registered outcomes — exactly three, and I must pick one and prove it

- **H1 PROVEN.** The S4′ average that defines M̄_c is, by its own definition, a convex combination of the
  T^σ_y: a finite (or finitely-supported) index set with nonnegative weights summing to 1, or a normalised
  positive measure. Then Lemma KN′ / Corollary KN-step′ hold **unconditionally** in RLARGE's setting on
  this account, and the adoption lands.
- **H1-F1.** H1 is **false**, or true only for a **sub-family** of S4′ contours. Then KN-step′ stays
  CONDITIONAL, nothing lands, and I must say **exactly which contours break it**.
- **H1-F2.** H1 holds for *an* S4′ average, but **not for the object RLARGE §6 (R1) actually uses** in the
  lasso/ribbon argument. Specifically: (R1)'s proof invokes S4′ **pairing** ("the same σ at both ends")
  and **translation covariance of P^σ**; I must verify that the object those two properties are asserted
  of is the **same** M̄_c whose convexity KN′ needs. If they are different objects, the patch is addressed
  to the wrong one.

I pre-register that **a uniform average over a finite index set is trivially convex**, and that this is the
*expected* answer — and therefore that the live hazards are the ones that do **not** look like that: a
signed average, an unnormalised sum, a reweighting by a σ-dependent factor, a quotient of two averages, a
limit/continuum average whose measure is not positive, an average over a set that depends on the field, or
**two different averages sharing the symbol M̄_c**. I will look for each specifically.

### §0.3 Pre-registered failure modes of my own work

- **(K1) Reading-only verdict.** A convexity claim settled by one quoted sentence is the same error as
  settling it by the word "mean". A PROVEN verdict here requires the **constructive definition** of the
  S4′ average — index set, weights, normalisation — traced to the file that defines it, plus the
  **inheritance chain** from that definition to M̄_c at RLARGE §6's point of use. Anything less is ARGUED.
- **(K2) Symbol collision on M̄_c, T^σ_y, S4′ or P^σ.** This lane holds 5 ε_1, 4 ε_*, 3 η_1 and 2 θ_0, and
  three multi-decade errors trace to collisions. Before I combine any two statements about M̄_c I verify by
  **file:line** that they are the same object. A collision here is exactly outcome **H1-F2**.
- **(K3) The gate cannot fail.** Convexity is a property an average "obviously" has; a check that assumes
  a weight list and then verifies it sums to 1 is a tautology. Any numeric or symbolic check I run gets a
  **designed-FAIL control** — a signed/unnormalised weight family on which KN′'s convexity step must be
  shown to break — and I report that the control failed.
- **(K4) ARITH-F1: wrong ε_1.** The two decade figures must each be stated **with the ε_1 it is evaluated
  at, by file:line**. This lane has five distinct ε_1 and the recorded 92-vs-82 slip is exactly a
  difference attributed to the wrong one. I will quote the file:line of each ε_1 I use.
- **(K5) Patch beyond scope.** The adoption patch must change **only** (R3)/(R4) and what they force. If
  writing it requires moving any other RLARGE constant, that is a finding (ARS_FIX claims the kernel-branch
  constant is invariant; I re-derive rather than assume it).
- **(K6) Over-claiming the landing.** Even with H1 PROVEN, a_RS's **status** is a separate question from
  its **size**. I pre-register that I must state plainly what the adoption does not buy.

### §0.4 Pre-registered deliverables, in order

1. **T55-A1.** The S4′ average's definition located by file:line, and H1's verdict (PROVEN / H1-F1 /
   H1-F2) with a written proof from that definition.
2. **T55-A2** — *only if H1 is PROVEN*. The literal append-ready adoption patch for RLARGE §6, in a
   `## FOR OTHER FILES (not edited)` section, carrying: (a) η_1 := c_1ε_1 with c_1 = 1/(2(L² + 5.5·A_d(L)))
   and its d = 4, L = 3 value; (b) the re-centred dichotomy **(R3′)** and the re-centred kernel branch
   **(R4′)** in full, with the kernel exponent; (c) the **reversals** the adoption forces, re-verified by
   me and not copied; (d) the two **decade gains**, re-derived from a_RS ∝ η_1² and the ε_1 values in
   force, each labelled with the ε_1 (file:line) it is evaluated at; (e) what the adoption does **not**
   buy.
3. **T55-A3.** Confirm or refute the claim that a_RS is CONDITIONAL on (PLD)_k before **and** after the
   adoption, i.e. that no choice of η_1 relative to τ_bg restores in-step derivation.

### §0.5 Pre-registered arithmetic method

Exact `fractions.Fraction` in plain `python3 -I`, single thread, **no numpy / BLAS / SciPy**; `Decimal` at
two precisions for log10 display only, and a disagreement between the two precisions is a **FAIL of the
arithmetic**, not of the claim. No numeric lock taken or needed (exact rational arithmetic). Every decade
figure is formed as an exact rational ratio and logged once. Criteria file
`checks/kn1_criteria.md` is written **before** any script and contains **no constant derived in session
25**.

### §0.6 Pre-registered statuses

**PROVEN** (a complete argument written out in this file from stated hypotheses) / **COMPUTED** (exact) /
**ARGUED** (convincing with an identified hole) / **CONDITIONAL** (naming the open input) / **GAP** /
**OPEN**. A failed check is reported as a **FAIL** with script and output kept **byte-unaltered**; a re-run
takes a **new id** with the criteria untouched; any probe run **after** seeing a result is labelled
**POST-HOC** and carries no pre-registered verdict. I will not inflate: a wrong PROVEN is worse than an
honest OPEN, and if H1 fails I say so loudly and land nothing.

*(End of §0, the pre-stated section. Everything below this line was written after it.)*

---

## §1. T55-A1 — H1: **PROVEN**, and it was never a hypothesis RLARGE was missing

> ### **H1 is PROVEN from the definition. The S4′ average is a UNIFORM average over a finite index set of size d!·L^d, with constant weights (d!L^d)^{-1} — and RLARGE's Lemma RS (R1) ALREADY USES that convexity, in the very clause the patch amends.**

Status: **PROVEN** (complete argument below, from PROOF.md's own definition). Checks `kn1-1` (CONVEX, with
a designed-FAIL control that HAS-POWER) and `kn1-4` (IDENTITIES-HOLD).

### §1.1 Where the S4′ average is actually defined — the handle ARS_FIX did not follow

ARS_FIX §3.3 looked for H1 in **RLARGE** and found only the word "mean" (RLARGE.md **l.992**, not l.996 as
the brief has it — see §1.7 correction 1). RLARGE never defines M̄_c; it is defined once, in the master
ledger, as part of decision 4:

> **PROOF.md l.1754-1755**: *"**Decision 4: the RG kernel.** For a coarse link c = (X, X + e_μ), let
> **M̄_c(U) := (d!L^d)^{-1} Σ_σ Σ_{y∈B(X)} T^σ_y(U)** be the mean of the S4′ contour transporters (S4′
> pairing: the same order σ at both ends). **‖M̄_c‖_op ≤ 1.**"*

and the index-wise transporters are defined at **PROOF.md l.711-713**:

> *"For each of the **d! coordinate orders σ**, let P^σ be the complete-axial transporter … and
> **T^σ_y = P^σ(c_X → y)·S_y·P^σ(c_Y → y + L e_μ)^dag**"*, with y ranging over **B(X)**, the fine block of
> side L, i.e. **L^d sites**.

The same kernel is carried verbatim in the frozen package, **LINEAR_PACKAGE.md l.81-82** (*"With M̄_c(U)
the mean of the S4′ contour transporters…"*) — an independent, frozen record of the same object.

### §1.2 The proof of H1

**Claim (H1).** M̄_c = Σ_{i∈I} w_i T_i with w_i ≥ 0 and Σ_{i∈I} w_i = 1.

*Proof.* Take I := S_d × B(X), the index set of PROOF.md l.1754's double sum: σ ranges over the d!
coordinate orders (PROOF.md l.711) and y over the L^d sites of the block B(X) (PROOF.md l.702, blocks of
side L). Hence **|I| = d!·L^d**, a finite set fixed by (d, L) alone. PROOF.md l.1754 writes
M̄_c = (d!L^d)^{-1} Σ_{(σ,y)∈I} T^σ_y, i.e. w_{σ,y} = (d!L^d)^{-1} for every index. These weights are
**constants of the geometry**: they do not depend on U, on the coarse link c, on the level, on the
background, or on the field at all. Each is **strictly positive**, and
Σ_{(σ,y)∈I} w_{σ,y} = |I|·(d!L^d)^{-1} = (d!L^d)·(d!L^d)^{-1} = **1**. ∎

Verified as exact rationals at (d,L) ∈ {(2,3), (3,3), (4,3), (5,3), (4,5)} — so the property is not an
accident of d = 4, L = 3 — in `checks/kn1_h1_out.txt`. At d = 4, L = 3 the index set has
**24 × 81 = 1944** elements and every weight is exactly **1/1944**.

**This is the strongest of the three pre-registered outcomes.** The weights are not merely nonnegative
and normalised: they are **uniform and field-independent**, which is more than Lemma KN′ asks for.

### §1.3 H1-F2 is RULED OUT: the pairing and the covariance are properties of the summands

The brief's specific hazard was that RLARGE §6 (R1)'s two invoked properties — *"S4′ pairing (the same σ
at both ends)"* and *"translation covariance of P^σ"* (**RLARGE.md l.986**) — might be asserted of a
different object from the M̄_c whose convexity KN′ needs. They are not. The chain, link by link:

| step | statement | file:line |
|---|---|---|
| 1 | T^σ_y := P^σ(c_X → y)·S_y·P^σ(c_Y → y + Le_μ)^† — **the same σ appears in both legs of the formula** | PROOF.md l.712 |
| 2 | so "S4′ pairing" is a property of **each individual T^σ_y**, built into its definition, not of the averaging | PROOF.md l.712, l.1755 (the parenthesis repeats it) |
| 3 | M̄_c is the uniform mean of **exactly those** T^σ_y | PROOF.md l.1754 |
| 4 | RLARGE's Lemma RS Setting fixes δ_c := max_{σ,y}‖T^σ_y − S_c‖_op *"over the S4′ contours of c"* — **the same index set (σ, y)** | RLARGE.md l.970 |
| 5 | (R1)'s proof uses the pairing and the translation covariance on **T^σ_y S_c^{-1}**, one index at a time, to bound δ_c | RLARGE.md l.984-992 |
| 6 | (R4) consumes M̄ through D4-norm (2), whose M **is** M̄_c(U) | RLARGE.md l.996; PROOF.md l.1756-1757 |

So the pairing/covariance properties are used **index-wise**, to control each summand, and the averaging
is applied to the same index set afterwards. **One object throughout. H1-F2 does not occur.**

**Collision sweep (failure mode K2).** Every lane-wide occurrence of M̄ (grep over ym4d-proof/*.md and
EXISTENCE.md, snapshots excluded) resolves to this one object: BFT_A.md l.21, BFT_B.md l.465,
FLOW.md l.115/134/314/1076/1447/1456, LINEAR_PACKAGE.md l.81-82. **M̄_c is one symbol, defined once.**
The only near-miss is **PROOF.md l.2281's polar(M̄_c)** — the unitary polar factor, a *different* object;
RLARGE §6 uses M̄_c itself (‖M̄_c − S_c‖ at l.973, Re tr(V^{-1}M̄) at l.995-997), not its polar part.
Unlike ε_1 (five) and η_1 (three), **M̄_c carries no symbol split.**

### §1.4 **The finding that reframes the conditionality: (R1) already uses H1**

RLARGE l.973's Lemma RS (R1) has two clauses: *"δ_c ≤ A_d(L)η … **hence ‖M̄_c − S_c‖ ≤ A_d(L)η**."* The
word "hence" is doing exactly one piece of work:

  ‖M̄_c − S_c‖ = ‖Σ_i w_i(T_i − S_c)‖ ≤ Σ_i w_i‖T_i − S_c‖ ≤ (Σ_i w_i)·max_i‖T_i − S_c‖ = **δ_c**,

and both inequalities need **w_i ≥ 0 and Σ_i w_i = 1**. With signed weights the first step still holds
with Σ|w_i| in front, and the second fails outright. The same is true of PROOF.md l.1755's
**‖M̄_c‖_op ≤ 1**, which for a mean of unitaries holds *iff* the weights are a probability vector.

> ### **So H1 is not an extra hypothesis the adoption imports into RLARGE §6. It is a hypothesis RLARGE §6 is ALREADY USING, in (R1)'s second clause and in the kernel's normalisation. If H1 failed, RLARGE (R1) would be false as written today.** The adoption therefore takes **no new risk at all** on this account, and ARS_FIX §6.2's *"CONDITIONAL on exactly one stated input"* is, on the mathematics, **discharged** — what remains is a one-sentence documentation request, not a condition.

### §1.5 By-product (PROVEN): **W′_c is the S4′ coarse link itself**, not a new object

Lemma KN′ re-centres at W′ := S e^{X̄}, X̄ := Σ_i w_i X_i, X_i := log(S_c^{-1}T_i). With the uniform
weights of §1.2 this is

  X̄ = (d!L^d)^{-1} Σ_σ Σ_{y∈B(X)} log(S_{c_X}^{-1} T^σ_y),  **W′_c = S_{c_X} exp(X̄)**,

which is, character for character, **PROOF.md l.714's definition of the S4′ coarse link**
U′(X, X + e_μ) = S_{c_X} exp( (1/d!) Σ_σ L^{-d} Σ_{y∈B(X)} log(S_{c_X}^{-1} T^σ_y) ), since
(1/d!)·L^{-d} = (d!L^d)^{-1}. So, on the domain D′ of PROOF.md l.715:

> **W′_c = U′(c) = the S4′ averaged coarse link.** The re-centring point of Lemma KN′ is the lane's own
> averaging map, evaluated at the same configuration.

Three consequences, all free:
1. **Nothing new is defined in RLARGE §6.** (R3′)/(R4′) below re-centre at an object PROOF already
   defines, iterates and has checked.
2. **W′_c inherits the S4′ covariances already proven**: gauge covariance (PROOF.md l.724-725, L1a/L1b),
   **axis-permutation covariance** (PROOF.md l.734-736, *"New: axis permutations … This repairs L8b"*),
   reflection covariance (L9a′), and B_4-symmetry of the family (RLARGE.md l.956). A re-centred (R3′)
   therefore does not disturb the B_4 symmetry that R4D-iso needs (RLARGE.md l.956, PROOF.md l.1762).
3. It explains **PROOF.md l.2281**'s *"polar(M̄_c) differs from S4′(V)_c by exp(O(C(L)ε_2³))"*: KN′'s
   ‖W′^{-1}M̄ − 1‖ ≤ 3δ² is the same comparison with an explicit constant. **I do not reconcile the
   exponents (3δ² against O(ε_2³)); they are stated in different variables and I have not checked that
   they agree. Flagged for PROOF's owner, not claimed.** [ARGUED at best; see §8.4.]

### §1.6 The degeneracy refinement (reportable outcome DEGENERATE-BUT-CONVEX), and why it is harmless

Distinct indices can give the **same** transporter: if y agrees with c_X in some coordinates, every order
σ that differs only by permuting those coinciding coordinates traces the **same** complete-axial path. So
the weights induced on the set of *distinct* transporters are **not uniform**. Enumerated exactly at
d = 4, L = 3 (`kn1_h1_out.txt`): 1944 index pairs collapse to **633** distinct (path, y) pairs, with
induced weights in **{1/1944, 1/486, 1/162, 1/81}** — all strictly positive, summing to exactly **1**.

**This does not touch H1.** Merging equal terms replaces (w_i, w_j) by (w_i + w_j) and preserves both
nonnegativity and the normalisation; Lemma KN′ never requires uniformity, only a probability vector. The
refinement is recorded because a hostile reviewer will raise it, and because it means **the honest
statement of H1 is "a probability vector", not "a uniform average"** — the uniformity is a property of
the *index* family, not of the transporter family.

### §1.7 Three corrections to citations in my own brief and in ARS_FIX [reading]

1. **The quoted sentence is at RLARGE.md l.992, not l.996.** l.996 is the D4-norm (2) step of (R4). The
   quote *"So δ_c ≤ A_d(L)η, and M̄_c is a mean of the T^σ_y"* is **l.992**. ARS_FIX §3.3 has it right;
   the session-25 brief has l.996.
2. **ARS_FIX §8.3 item 2 is partly moot.** It asks EXISTENCE to make the probability-weight hypothesis
   explicit in Lemma KN. **EXISTENCE.md l.1756 already states it**: *"Let M̄ = Σ_iw_iT_i **(probability
   weights)**"*. The hypothesis was never implicit in the existence lane; what was missing was the
   *verification on the consuming lane's object*, which is §1.2 above.
3. **The quadratic (R3) threshold is "v2-E9"** (RLARGE.md l.64 carries the tag `[v2-E9]`), so the
   threshold now being reopened is itself the output of an earlier E-item — HANDOFF's closing pattern,
   *"check what someone fixed once and nobody revisited"*, one layer deeper than ARS_FIX read it.

---

## §2. T55-A2(d) — the two decade gains, RE-DERIVED (not quoted)

Status: **COMPUTED (exact)**. `checks/kn1_gain.py` → `kn1_gain_out.txt`, criteria `kn1_criteria.md`.

### §2.1 The derivation, in closed form

a_RS := min{a_η, κε_1²/(256N)} (**RLARGE.md l.1020**), a_η := η_1²/(2N) (**RLARGE.md l.1026**), κ = 1.
The a_η entry is the active one at every live ε_1 (verdict **EXP-4** on all four rows of `kn1-2`), so
**a_RS ∝ η_1²** and the gain is convention-free:

  **GAIN = log₁₀(a_RS^lin / a_RS^quad) = 2·log₁₀(η_1^lin / η_1^quad) = 2·log₁₀( 512·N·A_d·c_1 / ε_1 )
        = 2·log₁₀( 4608N / (117 ε_1) )**  at d = 4, L = 3.

The /10², the /(c_RS·10²) and DX′ all cancel in the difference, so the gain does **not** depend on which
ceiling convention is taken. It **does** depend on N, because c_1 = 1/117 is N-free while the quadratic
entry ε_1²/(4608N) is not — a dependence ARS_FIX's headline does not carry.

### §2.2 The two figures, each with the ε_1 it is evaluated at, by file:line

| | ε_1, **by file:line** | N | a_RS quadratic | a_RS linear | **GAIN** |
|---|---|---|---|---|---|
| today | **6.7·10⁻⁴⁰ — RLARGE.md l.72** (*"So ε_1 ≲ 6.7·10⁻⁴⁰"*; also RLARGE.md l.612's v3 table row) | 2 | 5.931360·10⁻¹⁶⁶ | 8.198188·10⁻⁸⁴ | **+82.1406** |
| today | same | 3 | 1.757440·10⁻¹⁶⁶ | 5.465459·10⁻⁸⁴ | **+82.4927** |
| proposed | **9.38495112638·10⁻⁴⁵ — EPS1_SWEEP.md l.455** (= √(η_♭/4); **owner-gated and undecided**) | 2 | 2.283406·10⁻¹⁸⁵ | 1.608542·10⁻⁹³ | **+91.8478** |
| proposed | same | 3 | 6.765647·10⁻¹⁸⁶ | 1.072361·10⁻⁹³ | **+92.2000** |

**kn1-2 verdict: GAIN-REPRODUCES at N = 2.** ARS_FIX l.455's 82.141 / 91.848 are the **N = 2** figures and
they reproduce to 10⁻⁴ decade. **I did not take them as inputs**; they are recovered from RLARGE l.1020 +
l.1026 + l.64, EXISTENCE l.1771 and the two ε_1 above.

> ### **[kn1-A] A fourth wrong pairing of the "92", and it is the one the ledger quotes.** The ledger's **92** is reproducible in *three* different ways — 91.848 at (proposed ε_1, N = 2), **92.200 at (proposed ε_1, N = 3)**, and nowhere at today's ε_1 under either N. ARS_FIX corrected "92 at today's ε_1" to 82.141; the residual hazard is that **92.2 at N = 3** will now be mistaken for a confirmation of the ledger's 92. **The figure a reader wants is 82.141 at (today's ε_1 = 6.7·10⁻⁴⁰, RLARGE l.72, N = 2)**, and every quotation should carry both labels. This is defect 1 and defect 2 of the session brief, arriving together.

### §2.3 The margins against DX′, both conventions, both N

DX′ = **2.456·10⁻¹⁵²/C_Ω** (**REVIEW_SF_S7.md l.203**), evaluated at C_Ω = 1; every row is linear in C_Ω.
Convention g_K² ≲ a/10² is **RLARGE.md l.616-617**; the c_RS = 625 column is the honest per-cube
convention of **RLARGE.md l.1021/l.1023/l.1024**.

| ε_1 | N | quad, /10² | lin, /10² | quad, /(c_RS·10²) | lin, /(c_RS·10²) |
|---|---|---|---|---|---|
| today (RLARGE l.72) | 2 | **−15.617** | **+66.523** | −18.413 | +63.728 |
| today (RLARGE l.72) | 3 | −16.145 | +66.347 | −18.941 | +63.552 |
| proposed (EPS1_SWEEP l.455) | 2 | **−35.032** | **+56.816** | −37.828 | +54.020 |
| proposed (EPS1_SWEEP l.455) | 3 | −35.560 | +56.640 | −38.356 | +53.844 |

All four quadratic rows **BIND**; all four linear rows are **NOT-BINDING**. The sign is robust across N,
across both conventions and across both ε_1.

---

## §3. T55-A2(c) — the reversals, each re-verified from the owning file

### §3.1 Reversal 1: **RLARGE.md l.65's η_1 ≤ η_q dies, and REVIEW_RLARGE_V2 §2.3's "CORRECT" with it**

**RLARGE.md l.65**: *"For ε_1 ≤ 2, **η_1 ≤ η_q** unless δ_0/A_d binds (**"CORRECT", REVIEW_RLARGE_V2
§2.3**)."* The endorsement reads, in full: *"§0 η_1 ≤ η_q (l.66-67): for ε_1 ≤ 2,
ε_1²/(512NA_d) ≤ ε_1/(256NA_d). **CORRECT.**"*

I re-derive it rather than cite it. With η_q := min{ε_1/(2L²), ε_1/(256NA_d), δ_0/A_d} (RLARGE l.64; the
δ_0 entry omitted, which can only **lower** η_q and **enlarge** any reversal — a stated one-sided
reading), at d = 4, L = 3 and N = 2, 3 the second entry binds, so η_q = ε_1/(2304N), and

  **quadratic:** η_1/η_q = [ε_1²/(4608N)]·[2304N/ε_1] = **ε_1/2** → ≤ 1 **iff ε_1 ≤ 2**. The endorsement
  is exactly right, and `kn1-3(a)` returns the value **1.000000 at ε_1 = 2** — the boundary — which is an
  independent reconstruction of a verdict written by another author for another purpose.

  **linear:** η_1/η_q = [c_1ε_1]·[2304N/ε_1] = **2304N·c_1 = 2304N/117**, an **exactly ε_1-free constant**:
  **512/13 = 39.3846 (N = 2)** and **768/13 = 59.0769 (N = 3)**, identical at both live ε_1 (exact Fraction
  equality, `kn1_gain_out.txt`).

> **ORDER-REVERSED, by a factor 39.3846 (N = 2) / 59.0769 (N = 3), at every ε_1.** RLARGE l.65's sentence
> becomes **false**, and REVIEW_RLARGE_V2 §2.3's "CORRECT" is an endorsement of the quadratic form only.
> **That banked endorsement dies with the adoption.** (ARS_FIX l.526's two figures reproduce exactly.)

### §3.2 Reversal 2: HIST.md l.186's route comparison — **and ARS_FIX's 1551× is the wrong quantity**

**HIST.md l.186-187**: *"The binding exponent of the joint route is the plaquette branch **a_η/81** (h4);
most of h4's 80-fold reduction of n_♯ comes from **c_RS = 81 against 5⁴ = 625**, and the rest from
**η_q² against η_1²**."* So HIST names **two** factors, and the route comparison is the ratio of **binding
exponents**:

  RS/joint = [a_η(η_1)/c_RS] / [a_η(η_q)/81] = (81/625)·(η_1/η_q)²,  c_RS = 625 (**RLARGE.md l.1021**).

| form | η-factor (η_1/η_q)² | **route = (81/625)·that** | verdict |
|---|---|---|---|
| quadratic, today's ε_1, N = 2 | 1.12225·10⁻⁷⁹ | 1.45444·10⁻⁸⁰ | **RS-WORSE** (the joint route is better — HIST's recorded position) |
| **linear, N = 2 (any ε_1)** | **1551.148** | **201.029** | **RS-BETTER** |
| **linear, N = 3 (any ε_1)** | **3490.083** | **452.315** | **RS-BETTER** |

> ### **[kn1-B] SOURCE-DISAGREES with ARS_FIX l.536-537 and with the session-25 brief. The RS route becomes 201.0× better than the joint route at N = 2, not 1551×.**
> **1551.148 = (η_1/η_q)² is the η-factor alone.** HIST l.186-187 names the cube factor **in the same
> sentence**, and the joint route keeps its 81 against RS's 625; dividing by that **625/81 = 7.7160**
> gives **201.029**. ARS_FIX l.536-537 calls 1551 *"the RS route's exponent … better than the joint
> route's"*, which is a comparison of **binding** exponents and therefore must carry both factors.
> Direction: **unfavourable to the headline by a factor 7.716**; **the sign does not change** and the
> reversal stands. At N = 3 the route figure is **452.315×**.
> *Why it matters beyond bookkeeping:* 201× is the size of the case for re-ordering HIST's two routes.
> 1551× would make the RS route better than the joint route by more than the joint route's entire
> cube-counting advantage; 201× says the RS route wins **in spite of** that advantage, by a factor that a
> single further improvement to either c could still overturn.

**HIST.md l.181's constant, verified.** *"for ε_1 → 0, **η_q/η_1 = 2/ε_1**"* — exact at both live ε_1
under the quadratic form (`kn1-3(c)`, exact Fraction equality). Under the adoption it becomes the
**ε_1-free constant η_q/η_1 = 117/4608 = 13/512 = 0.0253906**, identical at both ε_1. **Confirmed; the
brief's 0.0254 is right.**

**HIST.md l.151** (*"PM is what makes the threshold linear (Lemma RS-lin)"*) stops being the only
mechanism, as ARS_FIX §8.4 item 2 says. I confirm the reading and add nothing.

---

## §4. **A consumer of a_RS that the banked sweep missed, and its resolution** [new; POST-HOC]

Status: the arithmetic is **PROVEN** from the stated (F_R) hypothesis; the item is **POST-HOC** (not
pre-registered in `kn1_criteria.md`).

ARS_FIX §5.1's consumer sweep enumerated occurrences of **η_1**. a_RS has consumers that do not name η_1,
and one of them carries a_RS with the **opposite sign**:

> **RLARGE.md l.830**: *"**§6 Lemma RS:** "1/g_i² ≥ 1/g_{i+1}² under (F)" is not implied by (F_R):
> **factor e^{a_RS R}** (§0, F-mono)."*

Every other consumer wants a_RS **large** (it sits in e^{−a_RS/g²}). This one has a_RS in a **positive**
exponent, so raising a_RS by 82.141 decades makes **this** correction worse. At the extreme of the
admissible range — R = 1/(2g_K²) with g_K² = 2.456·10⁻¹⁵² — one has a_RS^lin·R = **1.67·10⁶⁸** against
a_RS^quad·R = 1.21·10⁻¹⁴, which taken naively looks catastrophic. **It is not, and the reason must be
stated in the patch rather than left to be rediscovered:**

*Resolution.* The factor enters as C → C·e^{a_RS R} inside the base (Ce^{−a_RS/g²})^{n/c_RS}
(RLARGE.md l.1023; FLOW.md l.909 *"absorbed in C"*; REVIEW_FLOW_S1_S2 l.342 *"the repair factor
(e^{a_RS R})^{n/c_RS} is right"*). The ceiling condition is therefore
**a_RS·(1/g² − R) ≥ log C_ℓ**, not a_RS/g² ≥ log C_ℓ. Under the **standing** (F_R) hypothesis
**g_K² ≤ 1/(2R)** (**RLARGE.md l.113**; carried into HW's net at **RLARGE.md l.413**) one has
1/g² − R ≥ 1/(2g²), so a sufficient condition is **g² ≤ a_RS/(2·10²)**.

> **So the F-mono repair costs exactly a factor 2 — 0.30103 decades — on the ceiling, before and after the
> adoption. Both margins of §2.3 shift down by 0.301 and the GAIN is exactly unchanged.** Corrected
> headline margins at today's ε_1, N = 2: **−15.918 (quadratic) and +66.222 (linear)**; with c_RS,
> **−18.714 and +63.427**.
>
> **But the protection is a hypothesis, not an identity.** Without g_K² ≤ 1/(2R) the correction e^{a_RS R}
> is unbounded and **grows with a_RS**, so the adoption consumes 82.141 decades of whatever headroom that
> hypothesis leaves. The patch below carries this as named side condition **(S4)**. ARS_FIX §6.2's
> *"nothing else moves"* is **true, but for a reason it did not give**, and its §4.2 table has no row for
> l.830.

---

## §5. T55-A3 — what the adoption does NOT buy: **CONFIRMED**

Status: **CONFIRMED** (reading + exact arithmetic, `kn1_sides_out.txt` (C), POST-HOC).

ARS_FIX §3.4 / §8.6 item 6 says a_RS is CONDITIONAL on **(PLD)_k (i)** (RLARGE.md l.1020 *"a_η from
(PLD)_k (i)"*) before and after, because **REVIEW_PLD_S3 l.309** holds: *"**Choosing η_1 relative to τ_bg
cannot restore in-step derivation.**"* I tested whether the adoption's particular η_1 escapes it. It does
not, and it makes the shortfall **larger**:

| threshold, as a multiple of ε_1 | value | ÷ (2τ_bg = 2ε_1/L²) | reaches the in-step range? |
|---|---|---|---|
| RLARGE (R3) quadratic entry ε_1²/(4608N) | ~10⁻⁴¹ | ~10⁻⁴⁰ | **NO** |
| RLARGE (R3) linear entry ε_1/(2L²) = ε_1/18 | 0.055556 | 0.250000 | **NO** |
| **RS-compatibility ceiling** ε_1/(1.001L²) (REVIEW_PLD_S3 l.305) | 0.111000 | 0.499500 | **NO** |
| **KN-step′ c_1ε_1 = ε_1/117** | 0.008547 | 0.038462 | **NO** |

The decisive row is the third: **even the RS-compatibility ceiling itself falls short of 2τ_bg by ×2.002**
and of the refined range (1+δ)τ_bg for every δ > 1/1000. The obstruction is therefore **structural in the
RS-compatibility cap** (REVIEW_PLD_S3 l.304-305: every RS-compatible threshold is ≤ ε_1/L²(1+o(1)), while
τ_bg ≥ ε_1/L²(1−o(1))) and is **independent of c_1**. The adoption's c_1ε_1 sits **×26.0 below** 2τ_bg,
i.e. **further** from the in-step range than RLARGE's own linear entry ε_1/18.

> ### **CONFIRMED, with one sharpening ARS_FIX does not state: the adoption does not merely leave the obstruction untouched — it moves the threshold ×6.5 FURTHER from the in-step range than RLARGE's (R3) first entry (ε_1/18) would, and ×12.99 further than the RS-compatibility ceiling itself. The honest label is exactly ARS_FIX's: a_RS becomes 82.141 decades larger and stays CONDITIONAL on (PLD)_k (i).** REVIEW_PLD_S3 l.356 records that (PLD)_k at η_1 is *"very plausibly TRUE with uniform constants"* and that *"what fails is only the in-step proof"* — so this is a proof gap, not a suspected falsehood, before and after.

**RS-compatibility of the new threshold, checked** (the hazard in the other direction): c_1ε_1 = ε_1/117
against the cap ε_1/(1.001·9) leaves **×12.99** of room, so (R3′) **is** RS-compatible and
**Proposition INH holds a fortiori** (REVIEW_PLD_S3 l.300-302). Independent arrival at ARS_FIX §5.2's
×12.99.

---

## §6. Verdicts and status summary

| item | status |
|---|---|
| **H1 (the S4′ weights are a probability vector)** | **PROVEN** from PROOF.md l.1754 + l.711-713 |
| H1-F2 (wrong object) | **RULED OUT** — PROVEN (reading, chain of six cited steps, §1.3) |
| H1-F1 (a sub-family of contours breaks it) | **RULED OUT** — the weights are field-independent constants on the full index set S_d × B(X); **no contour breaks it** |
| M̄_c symbol collision | **NONE** (lane-wide sweep, §1.3) |
| (R1)'s second clause already uses H1 | **PROVEN** (§1.4) — so the adoption takes no new risk |
| W′_c = the S4′ coarse link U′(c) | **PROVEN** on D′ (§1.5) |
| degeneracy of the index→transporter map | **COMPUTED** (633 distinct of 1944 at d=4,L=3); **harmless** |
| Lemma KN′ / Corollary KN-step′ in RLARGE's setting | **PROVEN unconditional** (H1 here; H2-H7 by ARS_FIX §3.3, which I did not re-derive) |
| **The adoption** | **LANDS.** No remaining hypothesis gap on H1 |
| GAIN 82.1406 at ε_1 = 6.7·10⁻⁴⁰ (RLARGE l.72), N = 2 | **COMPUTED (exact)** |
| GAIN 91.8478 at ε_1 = 9.38495112638·10⁻⁴⁵ (EPS1_SWEEP l.455), N = 2 | **COMPUTED (exact)**; that ε_1 is **owner-gated and undecided** |
| the gain is N-dependent (82.4927 / 92.2000 at N = 3) | **COMPUTED**; not recorded anywhere else |
| RLARGE l.65 "η_1 ≤ η_q" and REVIEW_RLARGE_V2 §2.3's "CORRECT" | **FALSE after the adoption** (×39.3846 / ×59.0769) |
| HIST l.186 route comparison | **REVERSES to RS-BETTER by 201.029× (N = 2)**, not 1551× — **SOURCE-DISAGREES with ARS_FIX l.536-537** |
| HIST l.181 η_q/η_1 → 117/4608 = 13/512 | **COMPUTED (exact)**, ε_1-free |
| RLARGE l.830's e^{a_RS R} (F-mono) consumer | **new row**; costs 0.30103 decades on each margin, **0 on the gain**, under the standing g_K² ≤ 1/(2R); **side condition (S4)** |
| a_RS's STATUS | **unchanged: CONDITIONAL on (PLD)_k (i)**, before and after — **CONFIRMED**, §5 |
| the patch's identities (c_1 = 1/117, (L²+5.5A_d)c_1 = ½, t/2+4(t/8)=t, (t/8)²/4N = t²/256N) | **IDENTITIES-HOLD** (exact) |
| **what I did NOT re-derive** | H2-H7 of ARS_FIX §3.3; the internal inequalities of Lemma KN′'s proof beyond the convexity step; DX′; C_Ω; a_η's PLD-side constant; τ_bg's o(1)'s |

---

## §7. Checks, controls, power and provenance

| id | pre-registered verdict | result |
|---|---|---|
| **kn1-1** | CONVEX / NOT-CONVEX / DEGENERATE-BUT-CONVEX | **CONVEX**, at all five (d,L); refinement **DEGENERATE-BUT-CONVEX** (633 of 1944 distinct, weights {1/1944, 1/486, 1/162, 1/81}, sum exactly 1) |
| **kn1-1 control** | must fail (c-i) **and** (c-ii), else NO POWER | **HAS-POWER.** Signed family w = (4, −3) on T_{1,2} = e^{±X}, θ = ¼: rejected by (i); **‖R‖ = 1.369394 against 3δ² = 0.1875, exceeded ×7.303**; and **‖M̄‖_op = 1.984444 > 1**, violating PROOF.md l.1755. Convexity is load-bearing |
| **kn1-2** | GAIN-REPRODUCES / SOURCE-DISAGREES | **GAIN-REPRODUCES** at N = 2 (82.1406 / 91.8478); branch **EXP-4** on all four rows |
| **kn1-2 control (ARITH-F1)** | must separate the two ε_1 by ≥ 1 decade | **HAS-POWER**: 9.7073 decades apart |
| **kn1-2 power leg** | gain must move with c_1 | **HAS-POWER**: c_1 = 1/18 moves it by exactly 1.6258 = 2log₁₀(117/18) |
| **kn1-3(a)** | ORDER-PRESERVED / ORDER-REVERSED | **ORDER-PRESERVED** (quadratic, including exactly 1.000000 at ε_1 = 2) / **ORDER-REVERSED** (linear, 512/13 and 768/13, ε_1-free by exact Fraction equality) |
| **kn1-3(b)** | ROUTE-FIGURE-REPRODUCES / SOURCE-DISAGREES | **SOURCE-DISAGREES**: route = 201.029× (N = 2), 452.315× (N = 3); 1551.148 is the η-factor |
| **kn1-3(c)** | quadratic must return ε_1-DEPENDENT (own control) | **ε_1-DEPENDENT** (control fires correctly); linear returns 13/512 at both ε_1 |
| **kn1-4** | IDENTITIES-HOLD / FAIL | **IDENTITIES-HOLD** |
| **kn1-4 control** | 5.5 → 5 must break (ii) | **HAS-POWER**: (L²+5A_d)/117 = 6/13 ≠ ½ |
| **kn1-5** | PASS / FAIL (two precisions) | **PASS** — worst 50-vs-100-digit disagreement **4.841·10⁻⁴⁹** decades |
| **kn1-6** | — | **POST-HOC**, no pre-registered verdict: side conditions (S1)/(S2), the rebuilt 106 → 105.275780 (ratio 1.006879) and 5.5 → 4.758892, and the (PLD)_k shortfall table |

**No FAIL to report.** `kn1-3(b)` is a SOURCE-DISAGREES against a banked figure, which is a pre-registered
outcome of that check, not a failure of the check.

**Power grading, honestly.**
- **kn1-1's control is STRONG.** It does not test my weights; it tests whether the *conclusion* of
  Lemma KN′ survives signed weights, and it shows the conclusion breaking by ×7.3 and PROOF.md l.1755's
  own ‖M̄_c‖ ≤ 1 breaking by ×1.98. A gate that could not fail here would have made H1 decorative.
- **kn1-3(a) is STRONG.** It reproduces **REVIEW_RLARGE_V2 §2.3's** verdict, written by another author
  before this proposal, including the boundary value 1.000000 at ε_1 = 2. Had I mis-read l.64 it would
  have disagreed there.
- **kn1-3(b) is STRONG.** It returns a disagreement against a figure banked in ARS_FIX **and** repeated in
  the session-25 brief and in PROOF.md l.84, using HIST's own two named factors.
- **kn1-2 is MEDIUM-STRONG**: it reproduces another worker's figures, which is weak on its own, but its
  ARITH-F1 control and its c_1 power leg both fire, and the N = 3 row is new.
- **kn1-4 and kn1-5 are WEAK by construction** (exact identities; my arithmetic against itself).
- **§1.2's proof has no numerical power at all.** It is a reading of one definition. Its force is that the
  definition is *constructive* — index set, weights, normalisation, all written out at PROOF.md l.1754 —
  so the verdict does not rest on the word "mean" anywhere.

**What these checks cannot catch.** They cannot validate PROOF.md l.1754's definition itself (if decision
4's kernel is ever restated with a reweighted average, H1 must be re-checked — see §8.4); they cannot
validate DX′, C_Ω, a_η's PLD-side constant, τ_bg's o(1)'s, or R; they cannot settle ARS_FIX §2.3's reading
question about l.830 vs l.832; and they say nothing about H2-H7, which I took from ARS_FIX §3.3 and did
**not** re-derive.

**Provenance.** UTC file order (host clock UTC−4), scratch originals:
**KN_ADOPT.md §0 at 21:04Z** (`date -u` read immediately before writing) → `kn1_criteria.md` **21:12:22Z**
→ `kn1_h1.py` **21:13:30Z** → `kn1_h1_out.txt` **21:13:36Z** → `kn1_gain.py` **21:14:53Z** →
`kn1_gain_out.txt` **21:15:00Z** → `kn1_sides_posthoc.py` **21:15:56Z** → `kn1_sides_out.txt` **21:16:02Z**
→ §1-§8 of this file. **The pre-stated section precedes the criteria by 8 minutes and the criteria precede
the first script by 68 seconds.** As this file has been appended to, its own mtime is that of the last
append; the criteria file contains **no constant derived in session 25** and precedes every script.
§0's byte size as it now stands (lines 1-100, through its end-marker): **7 577 bytes**;
`kn1_criteria.md`: **8 330 bytes**.

Exact `fractions.Fraction` throughout; `Decimal` for log10 display only, at **50 and 100** digits.
Plain `python3 -I`, single thread (OMP/OPENBLAS/MKL = 1), `nice 10`, **no numpy, no BLAS, no SciPy**;
each script under 1 s. **No numeric lock taken and none needed** (exact rational arithmetic, brief rule 6);
machine load 3.89 at the start, 1.76 at the end. **No git command was run by me.**
*Disclosed:* the designed-FAIL control's (c-ii) and ‖M̄‖ legs use double-precision complex arithmetic
(margins 1.369 vs 0.1875 and 1.984 vs 1 — ~15 orders above double error, so no verdict turns on it); π and
e in `kn1_sides_posthoc.py` are `math`-module doubles, used only for POST-HOC figures with ~40 decades of
slack. One cosmetic defect in `kn1_sides_out.txt` line (S2) — the label text reads
`3/(4*A_d*c_1^-1^-1 ...)` where the formula is 351/(36π); **the printed value 3.103521 is correct and the
output is kept byte-unaltered.**

Files written by me: **KN_ADOPT.md**, `checks/kn1_criteria.md`, `checks/kn1_h1.py`,
`checks/kn1_h1_out.txt`, `checks/kn1_h1_err.txt`, `checks/kn1_gain.py`, `checks/kn1_gain_out.txt`,
`checks/kn1_gain_err.txt`, `checks/kn1_sides_posthoc.py`, `checks/kn1_sides_out.txt`,
`checks/kn1_sides_err.txt`. **Nothing else, anywhere.**

---

## §8. FOR OTHER FILES (not edited)

I wrote only `KN_ADOPT.md` and `checks/kn1_*`. The following are requests on their owners. §8.1 is the
adoption patch itself, written append-ready in RLARGE's own notation.

### §8.1 For RLARGE's owner — **the adoption patch for §6, literal and append-ready**

**Preamble for the owner, not part of the patch.** ARS_FIX §6.2 labelled this adoption *CONDITIONAL on
one word* — that RLARGE state the S4′ weights to be nonnegative and normalised. **That condition is
discharged.** The weights are defined, constructively and uniformly, at **PROOF.md l.1754**
(M̄_c(U) := (d!L^d)^{-1}Σ_σΣ_{y∈B(X)}T^σ_y(U)) over the index set of **PROOF.md l.711-713** (d! orders ×
L^d block sites), so they are the constants (d!L^d)^{-1} > 0 summing to 1 — **1/1944 each at d = 4,
L = 3**. Moreover **your own (R1) second clause already uses this**: *"hence ‖M̄_c − S_c‖ ≤ A_d(L)η"*
(l.973) is the convexity step ‖Σw(T − S)‖ ≤ Σw‖T − S‖ ≤ max‖T − S‖ = δ_c, which is false for signed
weights — as is **PROOF.md l.1755's ‖M̄_c‖_op ≤ 1**. **The adoption therefore imports no hypothesis your
file does not already rely on.** Everything below is unconditional on that account. (It remains
CONDITIONAL on (PLD)_k (i) exactly as before — see item 7.)

---
#### PATCH TEXT BEGINS (replaces §6 Lemma RS's (R3) and (R4); (R1), (R2), (R5) keep their statements)

**Threshold (replaces l.64's η_1 and §6 (R3)/(R4); E9 FIRST horn, REVIEW_PLD_S3 l.462).**

  **η_1 := c_1·ε_1,  c_1 := 1/(2(L² + 5.5·A_d(L)))  (= 1/117 at d = 4, L = 3).**

The identity **(L² + 5.5A_d(L))·c_1 = ½** is exact by construction and is what the dichotomy below uses.
Source of the form: EXISTENCE.md l.1771, l.1774-1775 (Lemma KN, Corollary KN-step), rebuilt on our
structures in ARS_FIX §3.2 and KN_ADOPT §1.

**Re-centring (new object, but not a new definition).** For each coarse link c = (X, X + e_μ) put

  X^{σ,y}_c := log(S_c^{-1}T^σ_y),   X̄_c := (d!L^d)^{-1} Σ_σ Σ_{y∈B(X)} X^{σ,y}_c,   **W′_c := S_c·exp(X̄_c)**,

with the principal log. **W′_c is exactly the S4′ averaged coarse link U′(X, X + e_μ) of PROOF.md l.714**,
so it carries S4′'s gauge covariance (PROOF L1a/L1b), axis-permutation covariance (PROOF.md l.734-736) and
reflection covariance (L9a′) with no new verification, and the B_4-symmetry that R4D-iso needs (l.956) is
untouched. M̄_c is the decision-4 mean of PROOF.md l.1754.

**Side conditions (all four are side conditions on ε_1 and on the flow, and all four hold at the current
constants by ~40 decades; verified in KN_ADOPT `checks/kn1_sides_out.txt`).**
- **(S1)** ε_1 ≤ 1/(106·√N·A_d(L)²·c_1²) = **169/(106√N)** = **1.127368** (N = 2), **0.920492** (N = 3).
- **(S2)** (π/3)·A_d(L)·c_1·ε_1 ≤ 1/4  ⟺  ε_1 ≤ 351/(36π) = **3.103521**.
- **(S3)** the traceless log exists on the chart: N·(π/3)·A_d·c_1·ε_1 < 2π ⟺ **ε_1 < 78/N** at d = 4,
  L = 3. (This is PROOF's own D′_N condition, l.715, in ε_1 units. It binds only for N ≳ 39 at ε_1 ≈ 2.)
- **(S4)** the standing (F_R) condition **g_K² ≤ 1/(2R)** (your l.113, your l.413) — see item 5 below; it
  is what keeps l.830's e^{a_RS R} repair at a factor 2 once a_RS rises.

**(R3′) Re-centred dichotomy.** Under (S1)-(S3), if ‖1 − V_P‖ ≥ ε_1 then **either** η ≥ η_1 = c_1ε_1,
**or** some c ∈ ∂P has **‖V_c − W′_c‖_op ≥ ε_1/8**.

*Proof.* ‖1 − V_P‖ ≤ ‖1 − W′_P‖ + Σ_{c∈∂P}‖V_c − W′_c‖ (telescoping unitaries, as in (R2), but against
W′ rather than S), and ‖1 − W′_P‖ ≤ ‖1 − S_P‖ + Σ_c‖W′_c − S_c‖ ≤ L²η + 4(e^δ − 1) by (R2) and
δ ≤ (π/3)A_d(L)η, which is (R1) together with |θ| ≤ (π/3)‖e^{iθ} − 1‖ for ‖·‖ ≤ 1. Under (S2), δ ≤ ¼ and
4(e^δ − 1) ≤ 4·((e^{1/4} − 1)/(1/4))·(π/3)·A_dη = **4.758892·A_dη ≤ 5.5·A_dη**. Hence on {η < c_1ε_1},

  ‖1 − W′_P‖ ≤ (L² + 5.5A_d)η < (L² + 5.5A_d)c_1ε_1 = **ε_1/2 exactly**,

and if in addition all four ‖V_c − W′_c‖ < ε_1/8 then ‖1 − V_P‖ < ε_1/2 + 4·(ε_1/8) = ε_1. The dichotomy
is therefore **exhaustive by construction**. ∎

**(R4′) Re-centred kernel branch, unconditional.** For every U with δ_c(U) ≤ A_d(L)η_1 and g² ≤ κ, under
(S1)-(S3),

  ∫_{‖V_c − W′_c‖_HS ≥ ε_1/8} k_c(V_c, U) dV_c ≤ e·c_N^{-1}(κ/g²)^{N²−1}·**e^{−κε_1²/(256Ng²)}**,

and for distinct coarse links the bound multiplies (k = Π_c k_c is a product of conditional densities, as
in (R4)).

*Proof.* By **PROOF.md l.1754**, M̄_c = Σ_{(σ,y)} w_{σ,y}T^σ_y with **w_{σ,y} = (d!L^d)^{-1} > 0** and
**Σ w_{σ,y} = 1**; write T^σ_y = S_c e^{X^{σ,y}_c} with X^{σ,y}_c ∈ su(N) (the traceless log exists by
(S3)), and δ := max_{σ,y}‖X^{σ,y}_c‖_op ≤ (π/3)A_dη_1 ≤ ¼ by (S2). With X̄_c and W′_c as above, and using
Σ w X = X̄,

  R := W′_c^{-1}M̄_c − 1 = Σ w[(e^{−X̄} − 1)(e^{X} − 1)] + (e^{−X̄} − 1 + X̄) + Σ w(e^{X} − 1 − X),

so **‖R‖ ≤ (e^δ − 1)² + δ²e^δ ≤ δ²(e^{2δ} + e^δ) ≤ 3δ²** for δ ≤ ¼. *(Both displayed steps use the
convexity: Σ w X = X̄ needs Σw = 1, and the term-by-term bound needs w ≥ 0.)* Put Z := W′_c^{-1}V_c and
x := ‖V_c − W′_c‖_HS = ‖1 − Z‖_HS. For unitary Z, ‖1 − Z‖²_HS = 2 Re tr(1 − Z^{-1}) exactly, so with
|tr(AB)| ≤ ‖A‖_HS‖B‖_HS,

  Re tr((W′_c^{-1} − V_c^{-1})M̄_c) = Re tr((1 − Z^{-1})(1 + R)) ≥ ½x² − √N‖R‖_op·x ≥ ½x² − 3√Nδ²x ≥ **¼x²**

for x ≥ 12√Nδ² — a threshold that is *equivalent* to the inequality, not an estimate of it. (S1) is
exactly the statement that ε_1/8 ≥ 12√Nδ² at δ = (π/3)A_dc_1ε_1: the sharp coefficient is
8·12·(π/3)² = **105.275780**, and 106 is its safe rounding. D4-norm (2) gives
𝒩(M̄_c) ≥ e^{−(κ/g²)(1 − N^{-1}Re tr V_0^{-1}M̄_c)}·e^{−1}c_N(g²/κ)^{N²−1} with V_0 the SU(N)-maximiser,
and Re tr(V_0^{-1}M̄_c) ≥ Re tr(W′_c^{-1}M̄_c) since W′_c is a candidate. Hence
k_c ≤ e·c_N^{-1}(κ/g²)^{N²−1}·e^{−κx²/(4Ng²)}, which at x = ε_1/8 is the stated
**κε_1²/(256Ng²)**. Haar mass ≤ 1. ∎

**(R5) is unchanged in form**: on {η ≥ η_1} some plaquette of U_4 has s(U_p) ≥ η_1²/(2N) = **c_1²ε_1²/(2N)**
(inequality (B)).

**Consequential constants.** a_η = η_1²/(2N) = c_1²ε_1²/(2N) (l.1026 unchanged in form);
**a_RS = min{a_η, κε_1²/(256N)}** (l.1020 unchanged in form), and the a_η entry is still the active one
(it would take ε_1 > 814.587 for the other branch, N = 2).
**The kernel branch constant κε_1²/(256N) is IDENTICAL before and after** — (R4) reached it by halving
ε_1²/(128N) to absorb 2δ_c, (R4′) reaches it from ¼·(ε_1/8)² — so the adoption changes **exactly one
entry** of the min and no other constant in §6 moves.

**RS-compatibility.** c_1ε_1 = ε_1/117 ≤ ε_1/(1.001L²), the cap of REVIEW_PLD_S3 l.305, with **×12.99** to
spare; so (R3′) is RS-compatible and Proposition INH holds a fortiori (REVIEW_PLD_S3 l.300-302).

#### PATCH TEXT ENDS
---

**The consequential edits elsewhere in your file, with the numbers re-derived in KN_ADOPT §2-§4:**

1. **l.830-831 is the decision that has to be rewritten, and it is not only wording.** Today it reads
   *"**§6 Lemma RS:** … **η_1 is v2/v3's η_1 (E9).**"* — i.e. v3 answered REVIEW_PLD_S3 l.462's either/or
   by taking the **second** horn. This patch takes the **first**. The note must become, at minimum:
   *"§6 Lemma RS: η_1 is KN-step′'s c_1ε_1 (**E9, first horn**); (R3) and (R4) are replaced by (R3′) and
   (R4′), which re-centre at the S4′ averaged link W′_c. The kernel-branch constant is unchanged."*
   Two further clauses of the same note need attention: the **e^{a_RS R}** clause (item 5) and the
   fact that **l.830's one-clause answer records no price** — the price was first computed in ARS_FIX and
   is 82.141 decades.
2. **l.64's η_1 definition is replaced** (the quadratic entry disappears; it is tagged `[v2-E9]`, so this
   supersedes a v2 decision, not a v3 one).
3. **l.65 becomes FALSE and must be deleted or reversed.** *"For ε_1 ≤ 2, η_1 ≤ η_q unless δ_0/A_d binds
   ("CORRECT", REVIEW_RLARGE_V2 §2.3)."* Under the adoption **η_1/η_q = 2304N·c_1 = 512/13 = 39.3846
   (N = 2), 768/13 = 59.0769 (N = 3)**, an **ε_1-free** constant, so the ordering reverses at **every**
   ε_1. **REVIEW_RLARGE_V2 §2.3's "CORRECT" endorsement is of the quadratic form only and dies with it.**
   I re-derived both the endorsement (η_1/η_q = ε_1/2, equal to 1 exactly at ε_1 = 2) and the reversal;
   see KN_ADOPT §3.1. Suggested replacement: *"η_1 > η_q by the ε_1-free factor 2304N·c_1 (39.38 at
   N = 2, 59.08 at N = 3); the v2 ordering η_1 ≤ η_q was a property of the quadratic (R3) threshold."*
4. **l.618 must be edited regardless** (ARS_FIX §8.1 item 1 — I confirm the arithmetic independently):
   a_RS's ceiling sits **−15.617** decades below DX′ at ε_1 = 6.7·10⁻⁴⁰ (l.72), N = 2, and **−18.413**
   under the c_RS = 625 convention, before the adoption; **+66.523 / +63.728** after it.
5. **l.830's e^{a_RS R} repair is the one consumer of a_RS whose direction is OPPOSITE, and it needs the
   standing hypothesis spelled out.** Raising a_RS by 82.141 decades raises e^{a_RS R}. Because the factor
   enters as C → C·e^{a_RS R} inside (Ce^{−a_RS/g²})^{n/c_RS} (l.1023; FLOW.md l.909), the true ceiling
   condition is **a_RS(1/g² − R) ≥ log C_ℓ**; under your standing **g_K² ≤ 1/(2R)** (l.113, l.413) this is
   implied by **g² ≤ a_RS/(2·10²)**, i.e. the repair costs exactly **a factor 2 = 0.30103 decades**,
   before and after, and **the 82.141-decade gain is unaffected**. **Without g_K² ≤ 1/(2R) the correction
   is unbounded and grows with a_RS**, so please carry it as side condition (S4) rather than leave it
   implicit. Corrected headline margins: **−15.918 / +66.222** (and −18.714 / +63.427 with c_RS).
   *ARS_FIX's consumer sweep enumerated η_1 occurrences and has no row for this one.*
6. **l.1024's n_♯ and §5.4's table**: as ARS_FIX §8.1 item 8, unchanged by me; and l.832 vs l.830 still
   needs the ruling ARS_FIX §8.1 item 7 asks for. I add nothing there.
7. **Status, unchanged by the patch.** a_RS remains **CONDITIONAL on (PLD)_k (i)** (your l.1020). I tested
   whether the new threshold escapes REVIEW_PLD_S3 l.309's *"choosing η_1 relative to τ_bg cannot restore
   in-step derivation"* and it does **not**: even the RS-compatibility ceiling ε_1/(1.001L²) falls short
   of 2τ_bg by ×2.002, and c_1ε_1 falls short by **×26.0** — further than your own ε_1/(2L²) entry would.
   **The honest ledger line is "82.141 decades larger and still conditional".** KN_ADOPT §5.

### §8.2 For HIST's owner — **one figure in the request you are about to receive is wrong**

1. **l.186-187's route comparison reverses, but by 201.0×, not 1551×.** Your sentence names **two**
   factors — *"c_RS = 81 against 5⁴ = 625, and the rest from η_q² against η_1²"* — so the comparison of
   **binding** exponents is (81/625)·(η_1/η_q)². Under the adoption (η_1/η_q)² = **1551.148** (N = 2), and
   the route ratio is **(81/625)·1551.148 = 201.029×** in the RS route's favour (**452.315×** at N = 3).
   **ARS_FIX §8.4 item 1 and PROOF.md l.84 quote 1551×, which is the η-factor alone and omits your own
   cube factor 625/81 = 7.7160.** The sign and the conclusion are unchanged; the size is not.
2. **l.181's "for ε_1 → 0, η_q/η_1 = 2/ε_1" becomes the ε_1-free constant 117/4608 = 13/512 = 0.0253906.**
   Verified exactly at both live ε_1. I also reproduce your 2/ε_1 exactly under the current threshold.
3. **l.151's "PM is what makes the threshold linear"** stops being the only mechanism (ARS_FIX §8.4
   item 2); I confirm the reading and add nothing.
4. **l.1377-1379's chain-energy floor η_1²/(2NC_cone) gains 82.141 decades** at ε_1 = 6.7·10⁻⁴⁰, N = 2
   (**82.4927 at N = 3**). ARS_FIX §8.4 item 3 quotes the N = 2 figure without the label.

### §8.3 For the existence lane's owner (EXISTENCE.md)

1. **Your Lemma KN already states H1 and did not need the repair ARS_FIX §8.3 item 2 requested.**
   **l.1756** reads *"Let M̄ = Σ_iw_iT_i **(probability weights)**"*. The hypothesis is explicit. What was
   missing was its **verification on the consuming lane's object**, and that is now done: PROOF.md l.1754
   gives constant weights (d!L^d)^{-1}. No edit needed; recorded so the request is not actioned twice.
2. **Your re-centring point has a name in the other lane.** W′ = S e^{X̄} with the S4′ weights **is** the
   S4′ averaged coarse link U′ of PROOF.md l.714 (KN_ADOPT §1.5). Worth one line in your §13.6: it makes
   the re-centring canonical rather than auxiliary, and it carries S4′'s gauge/permutation/reflection
   covariances for free.
3. **Your two constants rebuild**: l.1775's **106** as 8·12·(π/3)² = **105.275780** (ratio 1.006879) and
   l.1771's **5.5** as 4·((e^{1/4}−1)/(1/4))·(π/3) = **4.758892**. Independent of ARS_FIX §8.3 item 1.
4. **The N-dependent chart condition** (ARS_FIX §8.3 item 3) is confirmed as **ε_1 < 78/N** at d = 4,
   L = 3, and it is exactly PROOF's own D′_N domain condition (PROOF.md l.715) written in ε_1 units.

### §8.4 For PROOF's owner (the decision-4 kernel and the ledger)

1. **PROOF.md l.1754 is now load-bearing for another lane's lemma.** The uniform weights (d!L^d)^{-1} are
   what makes Lemma KN′ applicable in RLARGE §6, and they are also what makes **your own l.1755's
   ‖M̄_c‖_op ≤ 1** and **RLARGE's (R1) second clause** true. **If decision 4's kernel is ever restated
   with a reweighted, signed or field-dependent average, three statements break at once.** Worth one line
   at l.1754 recording that the probability-weight property is consumed downstream.
2. **A reconciliation I could not do.** **l.2281** states *"polar(M̄_c) differs from S4′(V)_c by
   exp(O(C(L)ε_2³))"*. Lemma KN′ gives the sharper-looking ‖W′_c^{-1}M̄_c − 1‖ ≤ 3δ² with
   **W′_c = S4′(U)_c** (KN_ADOPT §1.5) — a **δ²** where l.2281 has **ε_2³**, in different variables.
   **I did not reconcile the two and do not claim they agree.** If they are the same comparison, one of
   the two exponents is improvable; if not, polar(M̄_c) and S_c e^{X̄} differ in a way worth naming.
3. **Ledger corrections**, both to **PROOF.md l.84**: (i) the route figure is **201.029×**, not 1551×
   (§8.2 item 1); (ii) **l.63-66's "92 decades"** was already corrected to 82.141 by ARS_FIX — note that
   **92.200 is reproducible at (the proposed ε_1, N = 3)**, so a bare "92" now has *two* wrong readings
   available. Quote **82.141 at ε_1 = 6.7·10⁻⁴⁰ (RLARGE l.72), N = 2**, with both labels.
4. **[S24-flag 6] can be closed on the H1 account.** The repair's only named condition is discharged; what
   remains is RLARGE's decision (l.830's horn) and a_RS's unchanged dependence on (PLD)_k (i).

### §8.5 For the lead

1. **H1 is PROVEN, from PROOF.md l.1754, and it was never a real condition** — RLARGE's own (R1) uses it
   already. **The adoption lands.** Do not carry "CONDITIONAL on one word" forward.
2. **Two banked figures reverse and one banked figure is wrong.** Reversing: RLARGE l.65's η_1 ≤ η_q (with
   REVIEW_RLARGE_V2 §2.3's "CORRECT"), and HIST l.186's route ordering. Wrong: the **1551×**, which is
   **201.029×** once HIST's own cube factor is carried (§8.2 item 1) — it is quoted in ARS_FIX §5.1/§8.4,
   in PROOF.md l.84 and in the session-25 brief.
3. **The gain is N-dependent and nobody has labelled it**: 82.1406 (N = 2) / 82.4927 (N = 3) at today's
   ε_1; 91.8478 / **92.2000** at the proposed one. The ledger's "92" is now reproducible at two wrong
   pairings.
4. **One new consumer, found by sweeping a_RS instead of η_1**: RLARGE l.830's e^{a_RS R}, the only place
   a_RS appears with the **opposite** sign. It costs 0.30103 decades on each margin and **nothing** on the
   gain, *provided* the standing g_K² ≤ 1/(2R) holds. The method generalises: **ARS_FIX swept the symbol
   that changed (η_1) rather than the quantity whose size changed (a_RS)**, and the two sweeps are not the
   same set.
5. **D4 holds on this leg.** H1 → KN-step′ → (C2) discharged is intact: H1 is PROVEN and nothing in the
   chain broke. I did not test the rest of D4's chain, which is EPS1_SWEEP's (C2) bookkeeping, not mine.
6. **a_RS is 82.141 decades larger and still CONDITIONAL on (PLD)_k (i).** Confirmed, and sharpened: the
   adoption moves the threshold ×26.0 below 2τ_bg, **further** from the in-step range than RLARGE's own
   ε_1/(2L²) entry. §5.

*(End of KN_ADOPT.md. Files written by this worker: this file, `checks/kn1_criteria.md`,
`checks/kn1_h1.py`, `checks/kn1_h1_out.txt`, `checks/kn1_h1_err.txt`, `checks/kn1_gain.py`,
`checks/kn1_gain_out.txt`, `checks/kn1_gain_err.txt`, `checks/kn1_sides_posthoc.py`,
`checks/kn1_sides_out.txt`, `checks/kn1_sides_err.txt`. Nothing else, anywhere. No git command was run by
me.)*

---

## §9. Errata on this file, recorded rather than hidden

Two self-corrections were made to §1 and §5 **after** they were first written and **before** this file was
handed over. Both are recorded here because the lane's convention is that nothing is silently rewritten.

1. **§5, a wrong ratio of my own.** I first wrote that c_1ε_1 sits *"×13.0 further from the in-step range
   than RLARGE's (R3) first entry"*. The correct factor against **ε_1/(2L²) = ε_1/18** is
   **117/18 = 6.5**; **12.99 = 117/9.009** is the factor against the **RS-compatibility ceiling**
   ε_1/(1.001L²), a different comparator. Corrected in place, both figures now stated with their
   comparators. The ×26.0 shortfall against 2τ_bg is unaffected, and no verdict changes.
   *Cause: the same defect this session is about — a ratio quoted against the wrong one of two
   denominators that differ by a factor 2.*
2. **§1.2, a citation off by one line.** The block-side statement is **PROOF.md l.702**, not l.703.

No numeric verdict, no status and no line of the §8.1 patch is affected by either.
