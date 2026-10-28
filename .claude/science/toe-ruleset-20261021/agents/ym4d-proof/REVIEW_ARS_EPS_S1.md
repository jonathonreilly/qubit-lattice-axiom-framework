# REVIEW_ARS_EPS_S1 — hostile review of ARS_FIX.md and EPS1_SWEEP.md

Target T55-H. Reviewer: a worker that did not write either file. Scope: WRITE only this file and
`checks/ra1_*`. Read-only everywhere else.

---

## 0. PRE-STATED (first edit of this file; statements only)

**Written 2026-10-28T21:08Z UTC, BEFORE any derivation, any arithmetic and any read of the two
target files beyond their existence.** This section cites nothing produced in this session: the
items below are the assignment as handed to me, plus the two target files' own headline numbers as
quoted to me in my scope. No constant below is derived by me; every one is a *claim of the files
under review* that I am undertaking to re-derive independently.

I am spec'd to **refute**, not to confirm. A review that confirms everything has told the lane
nothing. Accordingly I pre-commit to the following: if I finish with no REFUTED and no
NOT-VERIFIED finding, I will say explicitly in my summary that I failed to break anything and that
this is weak evidence rather than a certificate.

### 0.1 What I will test, and what would count as a refutation

**A. Decade arithmetic (assigned failure mode ARITH-F1).**

- **A1.** ARS_FIX claims the KN-step adoption is worth **82.141 decades at today's ε_1** and
  **91.85 decades at the proposed ε_1**. *Refutation* = I re-derive from a_RS ∝ η_1² and obtain a
  value differing from either by ≥ 0.01 decades, **or** I find that the two figures are not
  evaluated at two different ε_1 (i.e. that the same ε_1 is used twice, or that one of them is
  evaluated at an ε_1 that is no longer an input).
- **A2.** ARS_FIX claims the honest margin is **−15.62 to −18.41 decades**, not −15.62, *because
  a_RS is priced per cube as a_RS/c_RS with c_RS = 625*. *Refutation* = the stated interval
  endpoints do not follow from the stated mechanism; in particular if log10(625) = 2.7959 does not
  reconcile −15.62 with −18.41 to within 0.01, the pair is inconsistent and at least one endpoint
  is wrong.
- **A3.** The **1551×** route reversal at **N = 2**. *Refutation* = the factor at N = 2 is not
  1551 to within rounding, or the reversal is not at N = 2 (i.e. the crossing N is different, or
  there is no crossing).
- **A4.** The constant **117/4608 = 0.0254**. *Refutation* = 117/4608 ≠ 0.0254 to the stated
  precision, or 117 and 4608 are not the quantities the file says they are (a symbol collision
  would show here).
- **A5.** **c_1 = 1/117** at d = 4, L = 3. *Refutation* = c_1 derived from the file's own stated
  construction is not 1/117; or 117 is assembled from factors that do not multiply to 117.
- **A6.** The **39.3846 / 59.0769** order-reversal figures. *Refutation* = either number is not
  reproducible from the file's stated inputs, or their difference/ratio is inconsistent with the
  mechanism named for the reversal.
- **A7.** Independent of all the above: for EVERY decade figure I touch I will state **by
  file:line** which of the FIVE ε_1 in this lane it is evaluated at. A figure whose ε_1 I cannot
  pin by file:line is recorded **NOT-VERIFIED**, not CONFIRMED. The three known multi-decade errors
  in this lane trace to exactly this, so "the number reproduces" is not sufficient; the number must
  reproduce *at a named ε_1 that is still an input*.

**B. Does ARS_FIX's rebuild of Lemma KN' prove what it claims?** It is labelled PROVEN from
hypotheses H1-H7 and claims to be *rebuilt rather than cited*.

- **B1.** *Refutation* = the proof as written has a step that does not follow, or silently uses a
  hypothesis not in H1-H7, or is in fact a citation with the load-bearing step left to the cited
  source.
- **B2.** Corollary KN-step''s dichotomy is asserted **exhaustive by construction**, with the t/8
  doing that work. *Refutation* = I exhibit an admissible configuration in neither horn, or show
  the two horns overlap in a way that makes the "either/or" uninformative, or show the t/8 is a
  free parameter chosen after the fact rather than forced.
- **B3.** ARS_FIX asserts **H1 is the only hypothesis RLARGE does not state**. *Refutation* = at
  least one of H2-H7 is also unsupplied by RLARGE. I will check H2-H7 against RLARGE **one at a
  time** and record a verdict per hypothesis, not a single aggregate verdict.

**C. EPS1_SWEEP's verdict structure (assigned failure mode C2-F1).** It returns SAFE WITH NAMED
CONDITIONS and says **(C2) is "the binding condition; everything else is bookkeeping"**.

- **C1'.** *Refutation of the "bookkeeping" claim* = any one of (C1), (C3)-(C7) requires new
  mathematics, or is not discharged, or is itself conditional on something open. "Bookkeeping"
  means: mechanical, no new mathematics, and certain to succeed. I will hold it to that.
- **C2'.** **(C6)** says to *re-evaluate the ε_1 number first — four live values are in force*. I
  pre-state the test: **if the ε_1 number is not determinate, lowering it is not bookkeeping**, it
  is undefined, and (C6) is a blocker rather than a clause. *Refutation* = the four values are not
  reconciled anywhere in the lane and the sweep's own arithmetic picks one without saying which.
- **C3'.** **(C7)** makes the verdict conditional on two **uncertified hand constants**
  (c_+·C_Ω ≲ 1.5e46, and DX' remaining the binding ceiling). I pre-state: **a verdict resting on
  uncertified constants is CONDITIONAL, not SAFE.** *Refutation* = the file's own headline status
  word is stronger than (C7) permits.

**D. The "could this check have failed?" lens**, applied to every gate in both files, and to the
check files `checks/ar1_criteria.md`, `ar1_margins.py`, `ar1b_power.py`,
`ar1c_knrebuild_posthoc.py` and the `es1_*` / `e1*` files. For each gate I will name an input that
would have made it fail. *Refutation* = a gate for which no such input exists: a tautology, a gate
built from its object's own primitives, a verdict that is the transpose of its own definition, a
clause that passes vacuously, or a gate unsatisfiable by construction. I note in advance that
`ar1c` is labelled **post-hoc by its own author**; I will test separately whether its conclusion is
**load-bearing** anywhere despite that label, since a post-hoc probe may be honestly labelled and
still be improperly consumed.

**E. The stale-minimum lens, applied to ARS_FIX itself.** ARS_FIX's own closing lesson is *"before
attacking an estimate, check what someone fixed once and nobody revisited."* *Refutation* = ARS_FIX
or EPS1_SWEEP reasons about a threshold that another file later made an **output**, so that the
inequality is correct at the value it was written for and wrong now. This is the shape of the
52-decade error of session 24 and I expect to find at least one instance.

### 0.2 Process commitments

- Statuses used strictly: **CONFIRMED / NOT-VERIFIED / REFUTED** for findings;
  PROVEN / ARGUED / CONDITIONAL / GAP / OPEN where I characterise a lane claim.
- **NOT-VERIFIED is not a soft CONFIRMED.** I will use it when I could not pin the claim, and say
  what would pin it.
- Exact rational arithmetic in plain python only (no lock needed, rule 6). If I write a check it
  gets `checks/ra1_criteria.md` with pre-registered PASS/FAIL **before** the script, and a
  **designed-FAIL control**; a gate with no control is not evidence.
- Anything I find that changes what the two parallel workers (KN-step adoption patch; ε_1
  execution) should do goes in **## FOR OTHER FILES (not edited)** and leads my reply.
- Append-only below this line.

---

## 1. HEADLINE — read this before the KN-adoption patch or the ε_1 move lands

> ### **The two files' arithmetic is right and their framing is not.** I could not break a single
> number in ARS_FIX's margin chain — all of **−15.617 / −18.413 / +66.523 / +56.816 / +82.141 /
> +91.848**, **c_1 = 1/117**, **39.3846 / 59.0769**, **117/4608**, **H5's 1.12737 / 0.920492** and the
> rebuilt **105.276** and **4.75889** reproduce exactly from the owning files' definitions. What breaks
> is **what the numbers are a gain over, and whether the thing they repair is consumed.**

**Three findings, in the order that matters.**

1. **[RA-F1, REFUTED] The question ARS_FIX §2.3 says "has to be SAID" is said, 400 lines earlier in the
   same file, the other way.** ARS_FIX l.304: *"If v3 intends a_RS to enter no smallness condition at
   all, that has to be SAID — l.832 retires the symbols a_♯/n_♯, not the exponent."* **RLARGE §3.5,
   l.433-439** — the section l.832 points to, which ARS_FIX cites only through that pointer and never
   reads — says: *"the greedy disjointness factors 7⁴, 81, 5⁴, RS-joint's c_RS = 81 ⇐ (PLD-q)_k, and the
   a_♯ := min{…}/greedy formula are **not consumed**"*, *"The exponent of unreturned defects is
   a = min{θa_bad, a_A}"*, and *"v2's remark **'No counted item depends on a_♯ or n_♯' stands**."*
   **a_RS reaches a coupling ceiling only through a_♯ (RLARGE l.1024).** Neither file cites §3.5, l.435,
   l.438 or l.835 anywhere (grep: zero hits in both).
2. **[RA-F2, REFUTED] The adoption is worth 2.303 decades over the lane's own best proven route, not 82.141.**
   ARS_FIX l.537 prices the route reversal at **1551×** by comparing bare exponents `(η_1/η_q)²`, while the
   sentence it is correcting — **HIST l.185-186** — states the compared quantity as *"the binding exponent
   of the joint route is the plaquette branch **a_η/81**"* against the RS route's **a_RS/625**. With both
   routes' own c_RS the ratio is **201.029**, i.e. **2.303 decades** (N = 2; **452.3** / 2.655 at N = 3).
   ARS_FIX applies c_RS = 625 where it deepens the breach (its own §2.2 Correction 1) and drops the
   625-vs-81 asymmetry where it would shrink the gain. Designed-FAIL control confirms the disagreement is
   caused by the asymmetry and not by my bookkeeping (`checks/ra1_out.txt`, RA1-6 control F-d returns 1551
   when the asymmetry is removed).
3. **[RA-F3, REFUTED] EPS1_SWEEP §5 (C2)'s "the binding condition; everything else is bookkeeping" does
   not survive.** (C2) (l.481-484) is itself an **either/or** whose second horn is *"or scope RLARGE
   l.618"* — writing a sentence. **(C6)** (l.492-493) is strictly prior to (C2) and is not bookkeeping,
   and **(C7)** (l.494-496) is not a condition at all but a statement that the verdict is CONDITIONAL. See
   §4 below. **D4's chain "discharge H1 → adopt KN-step' → (C2) discharged → the rest is bookkeeping" is
   therefore wrong in its ordering**, independently of whether H1 holds.

---

## 2. The decade arithmetic (ARITH-F1), re-derived independently

Criteria `checks/ra1_criteria.md` (written before any script, no constant of mine in it) →
`checks/ra1_margins.py` → `checks/ra1_out.txt`; corrected-summary re-run under a new id
`checks/ra1b_margins.py` → `checks/ra1b_out.txt` (see §2.7). Exact `fractions.Fraction`, `Decimal` at 60
digits for log10 display only, `python3 -I`, single thread, no numpy/BLAS, **no numeric lock taken and
none needed** (brief rule 6). Chain used: `A_d = (d−1)L(L−1)/2 = 9` (**RLARGE l.973**) →
`η_1 = min{ε_1/18, ε_1²/(4608N)}` (**RLARGE l.64, l.976, l.1009**) → `a_η = η_1²/(2N)` (**RLARGE l.981,
l.1026**) → `a_RS = min{a_η, κε_1²/(256N)}` (**RLARGE l.1020**) → ceiling `a/10²` (**RLARGE l.616-617**)
→ `DX′ = 2.456·10⁻¹⁵²/C_Ω` (**REVIEW_SF_S7 l.203**).

### 2.1 [RA-1] The four headline figures — **CONFIRMED** (ARS_FIX l.272, l.455)

| ε_1, with its owning file | margin /10² | margin /(625·10²) | gain (lin − quad) |
|---|---|---|---|
| 1.27e-39 (SF l.2837) | −14.506 | −17.302 | **81.585** |
| 9.52e-40 (RLARGE l.71) | −15.007 | −17.803 | **81.835** |
| 8.95e-40 (RLARGE l.611) | −15.114 | −17.910 | **81.889** |
| **6.7e-40 (RLARGE l.72)** | **−15.617** | **−18.413** | **82.141** |
| proposed 9.38495112638e-45 (EPS1_SWEEP l.455) | −35.032 | −37.828 | **91.848** |

Every one of ARS_FIX's figures lands to the last digit it prints. The gain is
`2·log10(512·N·A_d·c_1/ε_1)` = `2·log10(78.7692/ε_1)` at N = 2 — closed form, so the structural claim at
ARS_FIX l.466-467 that the 92-vs-82 discrepancy is *"exactly 2 × 4.854 = 9.707"* is right as well.
**Which ε_1 each is at: the 82.141 is at RLARGE l.72's 6.7e-40 and the 91.848 at EPS1_SWEEP l.455's
9.38495112638e-45. ARS_FIX l.445-446 names both correctly in its own table header.**

### 2.2 [RA-2] "−15.62 to −18.41 because a_RS is priced per cube as a_RS/c_RS, c_RS = 625" — **CONFIRMED**

`−15.6171 − log10(625) = −18.4130` ✓ (RECONCILES, to 10⁻⁴ decade). The mechanism at **ARS_FIX l.283-289**
produces exactly the stated interval. *Designed-FAIL control:* the same reconciliation with c_RS = 81
returns **−17.5256**, DOES-NOT-RECONCILE — so the gate has power and the interval is genuinely a 625
statement. The underlying textual claim is also right: **RLARGE l.1023** prices n cubes as
`(Ce^{−a_RS/g²})^{n/c_RS}` and **l.1024** forms `a_♯ := min{a″, a_♭, a_RS/c_RS}`.

### 2.3 [RA-3] **NOT-VERIFIED** — "the gain at today's ε_1" is a figure at one of four, and it is the most favourable one

Across the **four live ε_1** the gain runs **81.585 → 82.141**, a spread of **0.555 decades**, and
**82.141 is the maximum**, because the gain grows as ε_1 falls and 6.7e-40 is the smallest of the four.
ARS_FIX's §4.1 table header does name the value; **the texts that will be copied do not** — **ARS_FIX
l.462** (*"The gain at TODAY's ε_1 is 82.141 decades"*), **l.582**, **l.771** and **l.875** all say
"today's ε_1" with no value attached, to RLARGE's owner and to the lead. Honest form: **81.59-82.14
decades, 82.141 at RLARGE l.72's 6.7·10⁻⁴⁰.** The same remark applies to the margin: the honest
statement is **−14.51 to −15.62** (bare) / **−17.30 to −18.41** (per cube), and ARS_FIX l.288-289 quotes
only the second pair of endpoints as if the four values collapsed.

A second, worse point about those four. **Two of them are not live.** 8.95e-40 and 1.27e-39 come from
**RLARGE l.611**, a table row whose own status column reads *"v1's n_* formula, not n_H"* — a superseded
row. EPS1_SWEEP l.167 calls all four *"all presented as current"*; RLARGE l.611 does not present its two
as current. This does not change any sign (every row is negative) but it inflates the apparent
disagreement that (C6) is about. **Verdict on "four live values": NOT-VERIFIED — at most two of the four
(9.52e-40 at RLARGE l.71 and the 6.7e-40 headline at l.72) are presented by their owning file as in
force, and those two are the same min read at two points.**

### 2.4 [RA-4] c_1 = 1/117 — **CONFIRMED**, and the identity cited as evidence for it **cannot fail**

`1/(2(L² + 5.5A_d)) = 1/(2(9 + 49.5)) = 1/117` exactly ✓ (**EXISTENCE l.1771**, **ARS_FIX l.365**).

But **ARS_FIX l.592 and l.828 cite *"the identity (L² + 5.5A_d)c_1 = ½ verified exactly"* as evidence for
the rebuild, and relay it to EXISTENCE's owner as an independent recovery.** It is not evidence: `c_1` is
**defined** as `1/(2(L² + 5.5A_d))`, so the identity is `X·1/(2X) = 1/2`. In
`checks/ar1_margins.py` **l.24** `c_1 = F(1,2)/(L2 + F(11,2)*A_d)` and at **l.244-245** the script tests
`(L2 + KN_55*A_d)*c_1 == F(1,2)`. **The pre-registered verdict pair "IDENTITY-HOLDS / IDENTITY-FAILS"
(ARS_FIX §7.1, ar1-3 (c)) has an unreachable branch.** This is session 24's named defect *"a gate built
from its object's own primitives"*, in the **pre-registered** script, not only in the post-hoc one.
*The version with power, which I ran:* substituting the dichotomy's own sharper coefficient 4.75889 for
the 5.5 inside c_1 gives **0.442992 ≠ ½** — so the comparison can fail, and it establishes the genuine
content, that the 5.5 in c_1 and the 5.5 in the dichotomy's first part are the **same** constant.
*By-product:* building c_1 on the sharp 4.75889 would give c_1 = 1/103.66 and **0.105 decades more** of
a_η, forgone at no cost. Not material; recorded because nobody has looked.

### 2.5 [RA-5] 117/4608, 39.3846, 59.0769 — **CONFIRMED**, with a latent collision

`4608/117 = 512/13 = 39.3846…`, `6912/117 = 768/13 = 59.0769…`, `117/4608 = 13/512 = 0.025390625`
exactly. **But the two integers "4608" in this lane are different quantities**: in `η_1 = ε_1²/(4608N)`
it is `512·A_d`, with N carried separately; in `η_q = ε_1/4608` it is `256·N·A_d` **evaluated at N = 2**.
They coincide **only at N = 2** (at N = 3 they are 13824 and 6912). ARS_FIX l.538 writes *"η_q/η_1 =
117/4608 = 0.0254, a constant"* one paragraph away from a file that writes `ε_1²/(4608N)`. It is
ε_1-independent as claimed, but it is **N-dependent** and the two 4608s are not the same 4608. Flagged
under defect 1, not as an error.

### 2.6 [RA-9] H5's 1.12737 / 0.920492 — **CONFIRMED** (ARS_FIX l.408)

1.127368 and 0.920492; relative differences 1.5e-6 and 4.5e-7. I had this wrong by hand on first pass;
the file is right. The rebuild of EXISTENCE's **106** as `8·12·(π/3)² = 105.2758`, ratio **1.006879**, and
of the **5.5** as `4·((e^{1/4}−1)/(1/4))·(π/3) = 4.75890 ≤ 5.5`, both reproduce (ARS_FIX l.377, l.385).

### 2.7 Disclosure on my own run

`ra1_margins.py`'s summary line *"spread of the GAIN across the four live eps_1"* computed the spread over
**five** rows, including the proposed ε_1, and printed **10.263** where the four-value spread is
**0.555**. The table above it was correct throughout. **`ra1_margins.py` and `ra1_out.txt` are kept
byte-unaltered**; the fix is a re-run under a new id, `ra1b_margins.py` → `ra1b_out.txt`, with one line
changed and the criteria untouched. Reported as my own slip, not the file's.

---

## 3. Does ARS_FIX's rebuild of Lemma KN′ prove what it claims?

### 3.1 [RA-6] Lemma KN′ (ARS_FIX l.337-360) — **CONFIRMED, PROVEN as labelled**

I rebuilt every step by hand rather than re-reading it. All of it holds.

- The decomposition at l.345 is **exact**, not an estimate: with `A := e^{−X̄} − 1`, `B_i := e^{X_i} − 1`,
  `W′^{-1}M̄ − 1 = AΣw_iB_i + (A + X̄) + Σw_i(B_i − X_i)`, which is what is written, and the middle term
  needs `Σw_iX_i = X̄` — i.e. **H1**, exactly where ARS_FIX says the load is.
- `‖A‖, ‖B_i‖ ≤ e^δ − 1` needs `‖X̄‖ ≤ Σw_i‖X_i‖ ≤ δ`, which again needs `w_i ≥ 0, Σw_i = 1`. ✓
- `‖R‖ ≤ (e^δ−1)² + δ²e^δ ≤ δ²(e^{2δ}+e^δ) ≤ 3δ²` at δ ≤ ¼: `e^{1/2}+e^{1/4} = 2.93275 ≤ 3` ✓ and the
  sharper ratio 2.57475 ✓.
- `‖1−Z‖²_HS = tr(2 − Z − Z^†) = 2 Re tr(1 − Z^{-1})` for unitary Z ✓ **exact**.
- `(W′^{-1} − V^{-1})M̄ = (1 − Z^{-1})(1 + R)` ✓ exact; `‖1 − Z^{-1}‖_HS = x`, `‖R‖_HS ≤ √N‖R‖_op` ✓;
  `½x² − 3√Nδ²x ≥ ¼x² ⟺ x ≥ 12√Nδ²` ✓ **an equivalence, so the 12 is forced, as l.355 claims**.
- The maximiser step `Re tr(V_0^{-1}M̄) ≥ Re tr(W′^{-1}M̄)` needs only `W′ ∈ SU(N)`, which needs X̄
  traceless, which needs H3. ✓
- **Norm bookkeeping checked for a direction error and there is none:** KN′ thresholds in **HS**,
  KN-step′'s second horn is in **op**, and `‖·‖_op ≤ ‖·‖_HS`, so `{op ≥ t/8} ⊆ {HS ≥ t/8}` — the inclusion
  runs the right way.

### 3.2 [RA-7] Corollary KN-step′'s dichotomy is **genuinely exhaustive by construction** — **CONFIRMED**

Negating both horns gives `η < c_1t` and all four `‖V_c − W′_c‖ < t/8`, hence
`‖1−V_P‖ ≤ L²η + 4(e^δ−1) + Σ‖V_c−W′_c‖ < (L² + 5.5A_d)c_1t + 4·(t/8) = t/2 + t/2 = t`, contradicting
`‖1−V_P‖ ≥ t`. **No admissible configuration escapes both horns, and the two horns are allowed to
overlap without weakening anything** (the price is a sum over branches, not a partition). The **t/8 is
not a free parameter**: given that c_1 is defined to make the first part exactly t/2, the remaining
budget t/2 over four coarse links forces t/8. ARS_FIX l.383's *"the t/8 is what makes it so"* is
therefore half the story — **c_1's definition and the t/8 are one choice, made once**; they are not two
independent confirmations, and §7.1's ar1-3 (c) counting the identity as a separate check double-counts
it (see RA-4).

### 3.3 [RA-8] H2-H7 against RLARGE, one at a time — **CONFIRMED that H1 is the only one RLARGE does not state**, with two qualifications

| | my verdict | note |
|---|---|---|
| **H2** common S with T_i = Se^{X_i} | **AVAILABLE** | RLARGE l.969-970 defines a single straight transporter S_c per coarse link and l.973 bounds every T^σ_y against it. The *bound* is all H2 needs; the *chart* is H3, and ARS_FIX splits them correctly. |
| **H3** traceless log, ‖X‖ ≤ (π/3)‖·‖ | **AVAILABLE, and the π/3 is correctly restricted** | `|θ| ≤ (π/3)|e^{iθ}−1|` fails for ‖·‖ ≳ 1.002 (at θ = π it reads π ≤ 2.094, false). ARS_FIX l.376 states the restriction *"for ‖·‖ ≤ 1"* and H4 (δ ≤ ¼ ⇒ A_dη ≤ 3/(4π) = 0.2387) enforces it with room. The traceless-sum argument and `ε_1 < 78/N` both reproduce. **Qualification:** H3 is a hypothesis RLARGE also does not state — it states only the (R1) *bound* (l.973). It is *derivable* from what RLARGE states, which H1 is not; that is the honest distinction, and ARS_FIX l.413's flat *"H1 is the only hypothesis RLARGE does not state"* elides it. |
| **H4** δ ≤ ¼ | **AVAILABLE** | ε_1 ≤ 39/(4π) = 3.10352 ✓ |
| **H5** t ≤ 1/(106√N A_d²c_1²) | **AVAILABLE** | 1.127368 / 0.920492 ✓ (RA-9) |
| **H6** g² ≤ κ and D4-norm (2) | **AVAILABLE, no new import** | **RLARGE l.978** states `g² ≤ κ` inside (R4) and **l.996** uses D4-norm (2) in the same proof. Confirmed verbatim. |
| **H7** conditional independence of the four kernels | **AVAILABLE, and stronger than needed** | **RLARGE l.980**: *"for distinct coarse links the bound multiplies (k = Π_ck_c is a product of conditional densities)"* ✓. **Qualification:** KN-step′ as stated needs only a **union** bound over the four links, not independence; listing H7 as a hypothesis overstates what the corollary consumes. Harmless, but it makes the hypothesis list look one item more demanding than it is. |
| **H1** nonnegative normalised weights | **the real gap, correctly identified** | **RLARGE l.992** ends *"and M̄_c is a mean of the T^σ_y"* — I read it in situ and that is the whole of it. ARS_FIX's CONDITIONAL label is the right one. |

**One hypothesis is used and listed nowhere**, though it is harmless: KN′'s conclusion is a bound on
`∫k(V,M̄)dV` and therefore inherits whatever normalisation convention `k` carries; ARS_FIX folds this into
H6 ("D4-norm (2)"), which is the same convention RLARGE l.996 uses, so there is no gap — but the H-table
should say "H6 also fixes the normalisation of k", since that is what makes the e·c_N^{-1}(κ/g²)^{N²−1}
prefactor the same prefactor on both sides.

**Verdict on §3.2-§3.3 as a whole: the rebuild is a rebuild, not a citation, and it is correct.** This is
the strongest part of ARS_FIX and I could not dent it.

### 3.4 [RA-10] The check files, under the "could this check have failed?" lens — **REFUTED for five gates**

| gate | could it have failed? |
|---|---|
| `ar1_margins.py` ar1-1, ar1-2 | **YES.** My own controls F-a (η_1 := ε_1 → NOT-BINDING, +68.553) and F-b (η_1 := ε_1³/(512NA_d) → BINDS, −93.965) both move the verdict. Genuinely strong. |
| `ar1_margins.py` ar1-3 **(c)** l.243-245 | **NO.** Tautology in c_1's own definition (RA-4). |
| `ar1_margins.py` ar1-3 **(f)** l.269-271 | **NO.** The verdict string `"SAME-CONSTANT"` is a **literal in the format argument**, not a computed comparison. Reported as a result in ARS_FIX §7.1. |
| `ar1_margins.py` ar1-3 (a)/(b) at the live ε_1 | holds by ~40 decades; **ARS_FIX l.695 already grades these WEAK and says so.** Honest. |
| `ar1_margins.py` ar1-3 (d), (e); ar1-4 (b), (c), (d) | **YES**, all five are real comparisons with real counterfactuals. ar1-4 (c)/(d) reproducing seven of REVIEW_PLD_S3's independently scanned integers is the file's best evidence. |
| `ar1c_knrebuild_posthoc.py` **[2], [3], [7]** | **NO — they contain no computation at all**, only `print` statements asserting algebra. "STEP-2-IDENTITY", "STEP-3-IDENTITY", "SAME-CONSTANT" are prose. |
| `ar1c` **[4]** | **split.** The `4(e^{1/4}−1)/(1/4)·(π/3) ≤ 5.5` comparison can fail ✓; the `EXACT-HALF` line and the `DICHOTOMY-EXHAUSTIVE` line cannot. |
| `ar1c` **[5]** | **NO.** `"(REPRODUCES)"` is hard-coded in the format string at l.77-78, not conditioned on the ratio. |
| `ar1c` **[6]** | **NO.** `"CHART-AVAILABLE at every N"` is a bare print; the bound is never compared to a live ε_1 in code. |
| `ar1c` **[1]** | **YES** (weakly) — a real numeric comparison against 3, with monotonicity asserted in prose but visible in the printed values. |

**Is `ar1c`'s conclusion load-bearing despite its POST-HOC label?** *Partly, and it should not be.*
`ar1c` is correctly labelled POST-HOC and carries no pre-registered verdict, and the **PROVEN** status of
§3.2 rests on the hand proof, which is sound (RA-6) — so nothing collapses. **But its outputs are
relayed as verification to a lane that cannot see the label:** **ARS_FIX l.825-829** tells EXISTENCE's
owner *"your two constants are recovered independently … `ar1c_out.txt`"*, and the two items it leads
with are the one computation in [4] that has power and the **identity that cannot fail**. And
**ARS_FIX l.592** carries the same tautology into §6.2's evidence list for the PROVEN. **Recommendation:
strike the identity from both, keep the 105.276 and 4.75889, which are real reproductions.**

---

## 4. EPS1_SWEEP's verdict structure (C2-F1)

### 4.1 [RA-11] **REFUTED — (C2) is not "the binding condition", and it is not the one everything else reduces to**

Four separate reasons, any one of which is sufficient.

**(i) (C2)'s own second horn is bookkeeping.** EPS1_SWEEP l.481: *"**(C2) Adopt KN-step's linear η_1
first, or scope RLARGE l.618.**"* The second horn (l.482-484) is *"**or** record that the RS/joint route's
ceiling already sits 15.62 decades below DX′ and will sit 35.03 below after the move"* — i.e. write a
sentence. So **either** the second horn is acceptable, in which case (C2) is discharged by bookkeeping
and is not the binding condition, **or** it is not acceptable, in which case the verdict at l.468
(**"SAFE WITH NAMED CONDITIONS"**) is wrong and should read *UNSAFE until an unlanded repair lands*. The
file cannot have it both ways, and D4's chain takes the first reading while the lead's urgency takes the
second.

**(ii) (C6) is strictly prior to (C2) and is not bookkeeping.** EPS1_SWEEP l.492-493:
*"**(C6) Re-evaluate the ε_1 number first.** Four live values are in force (§1.1); NORMS.md's
k-independence argument is written at 1.27·10⁻³⁹. **Fix the number before lowering it.**"* Two things
follow. First, **every number in (C2) is a number at one of those values** — −15.62, −35.03, +66.52,
+56.82, and ARS_FIX's 82.141 and 91.848 — so (C2)'s content is not determinate until (C6) is. A condition
whose premise is indeterminate cannot be the one that binds. Second, (C6) is **not bookkeeping by its own
words**: it says an argument in **another file** (NORMS.md's k-independence) is written at a value that
is one evaluation stale. Re-establishing a k-independence argument at a different constant is
mathematics. **The brief's test — "if the number is not determinate, lowering it is not bookkeeping" —
is met.** (See RA-3: my own reading is that the indeterminacy is smaller than §1.1 implies, because two
of the four values come from a superseded table row; but *smaller* is not *settled*, and nobody has
settled it.)

**(iii) (C7) is not a condition; it is the verdict's hypothesis.** EPS1_SWEEP l.494-496: *"**(C7) The
whole verdict is CONDITIONAL on c_+·C_Ω ≲ 1.5·10⁴⁶ … and on DX′ remaining the binding programme
ceiling.** Both are uncertified hand constants."* A clause that begins *"the whole verdict is
CONDITIONAL on"* cannot be an item in a list of which "everything else is bookkeeping". **The honest
status word for §5 is CONDITIONAL, not SAFE WITH NAMED CONDITIONS** — and under the lane's own
definitions (brief rule 3: *CONDITIONAL = proven given a named open input*), (C7) names two.

**(iv) (C3) is a status change in two other lanes, not bookkeeping.** EPS1_SWEEP l.485-488 asks EXISTENCE
and PLD to *"record that the floor is ε_1 ≫ g, not 'none'"*, against **EXISTENCE l.3112**, **l.4191** and
**PLD l.995**, and notes PLD's ℓ¹ absorption margin **loses 4.854 decades**. The sweep's own §2.2 found
this floor and says TAUFLAT did not have it and that **REVIEW_SF_S5 l.332**'s "no lane requires ε_1 ≥
constant" was *"not shaped to catch"* it. Writing a newly-discovered floor into two files, and
re-checking the clauses that live on it at a margin that has just shrunk by 4.854 of 36.63 decades, is
not bookkeeping either.

> **Consequence for the session's ordering, which is what the lead asked for.** The chain is not
> H1 → KN-step′ → (C2) → bookkeeping. It is: **(C6) must be settled first** (which ε_1, and is NORMS's
> argument stale?); **(C7) must be converted from a hypothesis into a bound** or the verdict relabelled
> CONDITIONAL; **(C3) is a two-lane edit with a shrinking margin**; and **(C2) is, on the evidence of
> §1 of this review, a repair to a quantity RLARGE §3.5 says is not consumed.**

### 4.2 [RA-12] **REFUTED — (C7)'s condition is written with the wrong operator, and the direction of the risk is backwards**

EPS1_SWEEP l.441-444 and l.494 state the condition as **`c_+·C_Ω ≲ 1.5·10⁴⁶`** and give four exhaustion
figures: *"8.31·10⁵³ (RLARGE's ceiling) or 1.54·10⁴⁶ (g²_CRC ×82) at the proposed ε_1, against 4.24·10⁶³
and 7.87·10⁵⁵ today."* Recomputing them from the file's own inputs (`checks/ra1_out.txt`, RA1-7):

| row | my margin | the figure is the exhaustion value of |
|---|---|---|
| RLARGE a/10², today | +63.627 | **1/C_Ω = 4.236e63** — **c_+ does not appear in this ceiling at all** |
| RLARGE a/10², proposed | +53.920 | **1/C_Ω = 8.312e53** |
| g²_CRC ×82, today | +55.879 (file: 55.90) | **c_+/C_Ω = 7.87e55** |
| g²_CRC ×82, proposed | +46.189 | **c_+/C_Ω = 1.545e46** |

All four numbers reproduce. **The label on them does not.** Since `DX′ ∝ 1/C_Ω` (**RLARGE l.618**,
**REVIEW_SF_S7 l.203**) and `g²_CRC ∝ 1/c_+`, every margin is `∝ C_Ω/c_+`, so the binding condition is
**`c_+/C_Ω ≲ 1.5·10⁴⁶`**, and for the two RLARGE rows it is **`1/C_Ω ≲ 8.3·10⁵³`** with no c_+ in it.
**As written, (C7) says a large C_Ω endangers the verdict. In the file's own arithmetic a large C_Ω
protects it, and a SMALL C_Ω (below ~1.2e-54) is what exhausts the margin.** ARS_FIX has the same
quantity the right way round (l.275, l.706: *"every row is linear in C_Ω"*), so **the two files under
review denominate the same hand constant in opposite directions** — HANDOFF's closing paragraph names
exactly this pattern (*"an allowance currency that two lanes had each denominated differently"*).

### 4.3 [RA-13] **NOT-VERIFIED — the C_Ω at which ARS_FIX's headline reverses is computable and is stated nowhere**

Both files say every margin is linear in C_Ω and then evaluate at C_Ω = 1 without asking where the sign
changes. It changes at:

| claim | reverses once |
|---|---|
| a_RS binds today, bare /10² (ARS_FIX l.272) | **C_Ω > 10^15.617 = 4.14·10¹⁵** |
| a_RS binds today, per cube /(625·10²) | **C_Ω > 10^18.413 = 2.59·10¹⁸** |
| a_RS binds at the proposed ε_1 | **C_Ω > 1.08·10³⁵** (bare) / **6.72·10³⁷** (per cube) |

**That threshold sits 30.4 decades inside (C7)'s own admissible window for the hand constants.** So
EPS1_SWEEP's (C7) licenses a range of C_Ω over most of which **(C2)'s premise is false**. Neither file
notices, because (C7) is in one file and the C_Ω-linearity in the other.

*In fairness, and this is the honest reading:* **SF l.2073** defines `C_Ω := C + 3(N²−1)/2`, and
**REVIEW_SF_S7 l.338** says *"C_Δ, C_♭, C_Ω are analytic and hand constants. **Only C_Δ can bind**"*. So
C_Ω is expected to be modest — on that reading C_Ω ≥ 4.5 at N = 2, which makes every margin **0.65
decades better** than printed and leaves a_RS still binding at −14.96. **Verdict NOT-VERIFIED rather than
REFUTED:** the headline is probably safe on C_Ω, but *"RLARGE l.618 has a false sentence today"*
(**ARS_FIX l.871**, stated flatly) and *"l.618 is false as written and must be edited regardless of what
else is decided"* (**ARS_FIX l.763**) are **unconditional statements of a C_Ω-conditional fact**, and
ARS_FIX l.609 labels the same fact CONDITIONAL two pages earlier. The ledger will copy the unconditional
form.

### 4.4 [RA-14] **NOT-VERIFIED — κ is never cited, and (G4) was tested only against ε_1**

Every a_RS row is evaluated at `κ = 1`; neither file cites a line fixing κ. The min changes branch at
**κ = 128c_1² = 128/13689 = 9.35·10⁻³**: below it the kernel entry `κε_1²/(256N)` becomes the active one
under the **linear** η_1 and the gain is capped at **84.170 + log10 κ** decades (80.17 at κ = 1e-4,
76.17 at κ = 1e-8). ARS_FIX pre-registered this as failure mode **(G4) "the min's other branch"**
(l.128-130) and then tested the branch condition only in ε_1 (l.255-257, *"it would need ε_1 > 814"*).
**(G4) is therefore pre-registered and not discharged.** It does not threaten the conclusion — killing
82 decades needs κ ≲ 10⁻⁸² — but a pre-registered failure mode reported as not-triggered on the strength
of a different variable is not a discharge.

---

## 5. The stale-minimum lens, applied to ARS_FIX itself

ARS_FIX l.893-896 closes with *"Before attacking an estimate, check what someone fixed once and nobody
revisited."* Applied to ARS_FIX:

### 5.1 [RA-15] **REFUTED — RLARGE §3.5 answers the question §2.3 leaves open, and answers it against a_RS**

ARS_FIX §2.3 (l.291-307) is the pivot of the whole file: it asks whether l.616-617's g-ceiling convention
applies to a_RS at all, notes that **l.832** retires `a_♯, c_RS = 5⁴, n_♯` as *"superseded by §3.5 and
§5.2 (a = min{θa_bad, a_A})"*, and then declines to follow the pointer, concluding *"if v3 intends a_RS
to enter no smallness condition at all, that has to be SAID"* (l.304) and asking RLARGE's owner to *"say
which"* (l.788-791). **§3.5 is at RLARGE l.433-439 and says it.** Quoting it in full matters:

- l.434-437: *"For unreturned defects the case split … the greedy disjointness factors 7⁴, 81, 5⁴,
  RS-joint's c_RS = 81 ⇐ (PLD-q)_k, and the **a_♯ := min{…}/greedy formula are not consumed** (HW §5.3
  (5): 'Not consumed by Theorem HW: RS-joint, (PLD-q)_k, (SG^fl)_k, PLD-desc, (BG)_k, the case split of
  RLARGE §3.4 …')."*
- l.438: *"**The exponent of unreturned defects is a = min{θa_bad, a_A}** (§0)."* — neither entry contains
  a_RS, and both are ∝ ε_1², not ε_1⁴.
- l.438-439: *"v2's remark **'No counted item depends on a_♯ or n_♯' stands** for the frozen lemmas."*

**a_RS reaches a coupling ceiling only through a_♯ (RLARGE l.1024).** So on RLARGE's own text the
ε_1⁴ exponent is not consumed by any counted item.

ARS_FIX gives two reasons for keeping a_RS live anyway (l.296-300) and **neither supports the conclusion**:

1. *"l.830 keeps a_RS live: '§6 Lemma RS: … is not implied by (F_R): **factor e^{a_RS R}**'."* That
   factor has a_RS in the **favourable** direction — a smaller a_RS makes `e^{a_RS R}` closer to 1. At
   a_RS ≈ 10⁻¹⁶⁶ it is 1 to within 10⁻¹⁶⁶ for any R this lane could write down. **The one live appearance
   of a_RS that ARS_FIX itself cites argues against its own conclusion.**
2. *"Lemma RS … its output is a weight with a_RS in the exponent."* **Lemma RS's stated output contains
   no a_RS.** (R4) (l.979) gives `e^{−κε_1²/(256Ng²)}` — the **ε_1²** kernel branch, whose ceiling clears
   DX′ by **+68.55 decades**; (R5) (l.981) gives an **action** lower bound `s(U_p) ≥ η_1²/(2N)`, not a
   weight. `a_RS := min{a_η, κε_1²/(256N)}` is introduced at **l.1020** under the heading *"Definitions
   for the induction"*, i.e. inside §7.1 — the bookkeeping l.832 supersedes. The one place η_1²/(2N)
   becomes a cost, **(TS-c) at l.1183-1186**, is in **§7.3 Theorem TS**, which **l.835** declares
   *"frozen-background shadow; **not used by RLF-step v3**"* — a line neither file cites.

> **Verdict RA-15: REFUTED.** *"a_RS's ceiling BINDS TODAY"* (ARS_FIX l.277) and *"RLARGE l.618's
> unscoped sentence is FALSE"* (l.280, l.610, l.871) are **correct about the arithmetic of a_RS and
> not established about the programme.** The honest status is: **a_RS's ceiling, computed as l.616-617
> would compute it, sits 15.62-18.41 decades below DX′; RLARGE §3.5 and l.835 say the quantity that
> carries it into a smallness condition is not consumed.** ARS_FIX's own (G6) ("the /10² convention")
> was the right failure mode and it fired; the file recorded it as a scope caveat instead of as the
> answer.

### 5.2 [RA-16] **REFUTED — the 1551× route reversal is 201×, and the number that matters is 2.303 decades**

**ARS_FIX l.537**: *"the RS route's exponent becomes (η_1/η_q)² = **1551× BETTER** than the joint
route's (N = 2)"*, repeated to HIST's owner at **l.847**. The sentence being corrected is **HIST
l.185-186**, which states the compared quantity explicitly: *"**The binding exponent of the joint route
is the plaquette branch a_η/81** (h4); most of h4's 80-fold reduction of n_♯ comes from **c_RS = 81
against 5⁴ = 625**, and the rest from η_q² against η_1²."* The comparison therefore carries each route's
own c_RS, and ARS_FIX keeps only the η² half:

| | N = 2 | N = 3 |
|---|---|---|
| bare `(η_1^lin/η_q)²` (what ARS_FIX reports) | 1551.148 | 3490.083 |
| **per cube, `[a_η(η_1^lin)/625]/[a_η(η_q)/81]`** | **201.029** | **452.315** |
| in decades | **2.3033** | **2.6554** |

*Designed-FAIL control (F-d):* removing the 625/81 asymmetry returns **1551.148** exactly — so the
disagreement is caused by the asymmetry and is not a slip of mine. **This is the same c_RS that ARS_FIX
§2.2 Correction 1 insists on when it deepens the breach by 2.80 decades** (l.283-289). Applying it on one
side only is a currency inconsistency inside a single file.

### 5.3 [RA-17] **REFUTED — "82.141 decades" is the gain over RLARGE's own RS route, not over the lane's best proven route, which is 79.84 decades better today**

**HIST's Lemma RS-lin is listed PROVEN-HERE at RLARGE l.628**, it is *"the setting of Lemma RS (RLARGE
§6), step i → i + 1"* (HIST l.168-169), and it already delivers a **linear** threshold η_q by
**re-centring on the maximiser** (HIST l.150-151: *"RLARGE's Lemma RS compared V with S directly, which
costs a LINEAR δ … PM is what makes the threshold linear"*) — **the same mechanism KN-step′ uses**.
Computing its per-cube exponent at today's ε_1, N = 2 (`checks/ra1_out.txt` RA1-8):

| | per-cube exponent | margin vs DX′ |
|---|---|---|
| RS route, quadratic η_1 (today) | 9.49018e-169 | **−18.413** |
| **joint route, a_η(η_q)/81 (today)** | **6.52499e-89** | **+61.424** |
| RS route after the adoption, /625 | 1.31171e-86 | +63.728 |

**The joint route beats today's RS route by 79.837 decades and clears DX′ by +61.42 decades already.**
The adoption's **net** gain over it is **+2.303 decades** (the 201× of RA-16; +2.655 at N = 3), and
**+2.303 at the proposed ε_1 too** — the net value is ε_1-independent, because both routes are ∝ ε_1².

**Caveat, stated so this is not over-read.** RLARGE l.437 records **RS-joint as CONDITIONAL ⇐ (PLD-q)_k**
on the plain measure, and a_RS's a_η is CONDITIONAL on **(PLD)_k (i)** (ARS_FIX §3.4, RLARGE l.1020). So
the two routes are conditional on sibling PLD hypotheses, neither discharged — **the joint route is not
free, but it is not more conditional than the thing the adoption repairs.** Either way, the figure that
should go to RLARGE's owner is not "82 decades of repair"; it is **"2.3 decades over the route HIST
already proved, and 82 decades over the route RLARGE §3.5 says is not consumed."**

### 5.4 [RA-18] Minor, recorded without a verdict

- **EPS1_SWEEP l.270**: *"η_q/η_1 = 2/ε_1 … grows **×71398**"*. From the file's own two ε_1 the factor is
  **71391.9**; 10^4.854 is 71450. Immaterial (1 part in 10⁴); noted because the file's arithmetic is
  otherwise exact.
- **ARS_FIX l.487-494** (the n_♯ level-count "second defect in RLARGE §5.4's table") and **l.482** (the
  l.1184 per-plaquette cost) both describe quantities inside the sections RLARGE l.832 and **l.835**
  supersede. ARS_FIX caveats the first (l.493-494) and not the second.
- **ARS_FIX l.538** states `η_q/η_1 = 117/4608 = 0.0254` as *"a constant"*. It is ε_1-independent but
  **N-dependent** (117/6912 = 0.01693 at N = 3); and see RA-5 on the two 4608s.
- **EPS1_SWEEP §4.5 / (C4)** — the proposed value quoted **1.000000946×** above its own bound —
  reproduces exactly (9.38496/9.38495112638 = 1.00000094549). **CONFIRMED**, and it is a good catch.
- ARS_FIX's §1/§1.1 finding — that **E9 was an either/or and RLARGE v3 chose the other horn at l.830** —
  **CONFIRMED** by reading l.830 in situ. It is the single most useful reading result in either file.

---

## 6. SUMMARY TABLE

| # | claim tested | where it lives | verdict | the corrected number |
|---|---|---|---|---|
| RA-1 | −15.617 / −18.413 / +66.523 / +56.816 / +82.141 / +91.848 | ARS_FIX l.272, l.455 | **CONFIRMED** | — (exact to the last printed digit) |
| RA-2 | honest margin −15.62 to −18.41 *because* a_RS/c_RS, c_RS = 625 | ARS_FIX l.283-289 | **CONFIRMED** | — (control with 81 gives −17.53, fails) |
| RA-3 | "the gain at today's ε_1 is 82.141" | ARS_FIX l.462, l.582, l.771, l.875 | **NOT-VERIFIED** | **81.59-82.14**; 82.141 is at 6.7e-40, the most favourable of the four |
| RA-4 | c_1 = 1/117; "identity (L²+5.5A_d)c_1 = ½ verified" | ARS_FIX l.365, l.592, l.828 | **CONFIRMED** / gate **REFUTED** | c_1 ✓; the identity is a tautology in c_1's definition |
| RA-5 | 117/4608 = 0.0254; 39.3846; 59.0769 | ARS_FIX l.526, l.538 | **CONFIRMED** | exact as 13/512, 512/13, 768/13; two different 4608s |
| RA-6 | Lemma KN′ PROVEN from H1-H7 | ARS_FIX l.337-360 | **CONFIRMED** | every step rebuilt by hand; holds |
| RA-7 | the dichotomy is exhaustive by construction | ARS_FIX l.365-387 | **CONFIRMED** | t/8 is forced, not free; c_1 and t/8 are one choice |
| RA-8 | "H1 is the only hypothesis RLARGE does not state" | ARS_FIX l.413 | **CONFIRMED with qualification** | H3 is also unstated (but derivable); H7 is stronger than consumed |
| RA-9 | H5 = 1.12737 / 0.920492; 106→105.276; 5.5→4.75889 | ARS_FIX l.408, l.377, l.385 | **CONFIRMED** | 1.127368 / 0.920492; ratio 1.006879 |
| RA-10 | the check gates can decide | ar1_margins.py l.244, l.270; ar1c [2][3][5][6][7] | **REFUTED (5 gates)** | 2 unfalsifiable in the *pre-registered* script; 5 in ar1c |
| RA-11 | "(C2) is the binding condition; everything else is bookkeeping" | EPS1_SWEEP l.484 | **REFUTED** | (C6) is prior; (C7) is a hypothesis; (C3) is a 2-lane edit; (C2)'s 2nd horn is bookkeeping |
| RA-12 | "CONDITIONAL on c_+·C_Ω ≲ 1.5e46" | EPS1_SWEEP l.443-444, l.494 | **REFUTED** | **c_+/C_Ω ≲ 1.5e46**; and **1/C_Ω ≲ 8.3e53** for the two RLARGE rows |
| RA-13 | the headline's C_Ω-dependence | ARS_FIX l.275, l.706, l.763, l.871 | **NOT-VERIFIED** | reverses at **C_Ω > 4.14e15** (bare) / **2.59e18** (per cube) |
| RA-14 | (G4) "the min's other branch" discharged | ARS_FIX l.128-130, l.255-257 | **NOT-VERIFIED** | branch flips at **κ = 128/13689 = 9.35e-3**; gain = 84.170 + log₁₀κ below it |
| RA-15 | "a_RS binds today"; "RLARGE l.618 is FALSE" | ARS_FIX l.277, l.280, l.610, l.871 | **REFUTED as unconditional** | **RLARGE §3.5 l.433-439**: a_♯ *"not consumed"*, *"No counted item depends on a_♯ or n_♯"*; **l.835**: §7.3 *"not used by RLF-step v3"* |
| RA-16 | the 1551× route reversal | ARS_FIX l.537, l.847 | **REFUTED** | **201.029× = 2.303 decades** (N=2); **452.3× = 2.655** (N=3) |
| RA-17 | "the adoption is worth 82.141 decades" | ARS_FIX l.455, l.771; EPS1_SWEEP l.434 | **REFUTED as a programme figure** | **+2.303 decades** over HIST's Lemma RS-lin (PROVEN-HERE, RLARGE l.628), which already clears DX′ by **+61.42** |
| RA-18 | ×71398; the N-dependence of 117/4608; §4.5's 9.46e-7 | EPS1_SWEEP l.270, l.458; ARS_FIX l.538 | minor / **CONFIRMED** | 71391.9; N=3 gives 0.01693; 1.00000094549 ✓ |

**Net:** 8 CONFIRMED, 4 NOT-VERIFIED, 6 REFUTED. **I did not break the mathematics; I broke the
accounting and the framing.** Lemma KN′ and Corollary KN-step′ are correct and are genuinely rebuilt —
that part of ARS_FIX is the best work in either file and should be kept verbatim.

---

## 7. FOR OTHER FILES (not edited)

### 7.1 For the two workers acting on these files RIGHT NOW — act on these before you land

1. **To the KN-step adoption worker (T55-A).** The **mathematics you are adopting is sound** (RA-6,
   RA-7, RA-8) — adopt it. But **do not land the sentence "worth 82.141 decades"**. Land
   **"+2.303 decades (×201) over HIST's Lemma RS-lin, and +82.141 over RLARGE's own RS route"**, and
   note that **RLARGE §3.5 l.433-439 says the formula that carries a_RS into a ceiling is not
   consumed**. Also: **strike `(L² + 5.5A_d)c_1 = ½` from the evidence list** — it is a tautology in
   c_1's definition (RA-4) — and keep the 105.276 and 4.75889, which are real.
2. **To the ε_1-move worker (T55-B).** **(C2) is not the only binding condition (RA-11).** **(C6) is
   prior to everything you are doing**: the ε_1 in force is not settled, and EPS1_SWEEP l.493 says
   **NORMS.md's k-independence argument is written at 1.27e-39**. Settle that first or state plainly
   that you have not. And **(C7)'s condition is mis-stated**: it is **c_+/C_Ω ≲ 1.5e46**, not
   `c_+·C_Ω` (RA-12) — if you propagate the product form you will carry a sign error on a hand constant
   into the ledger.
3. **Both.** Every margin either of you quotes is **∝ C_Ω** and reverses at **C_Ω > 4.14e15** (RA-13).
   Quote the threshold or quote the margin as CONDITIONAL.

### 7.2 For RLARGE's owner

1. **§8.1 item 7 of ARS_FIX asks you to "say which" between l.830 and l.832. Your file already says it,
   at §3.5 (l.433-439) and l.835.** Before answering, confirm whether §3.5's *"not consumed"* and *"No
   counted item depends on a_♯ or n_♯"* are still your intent. If they are, **l.618 is not false** and
   ARS_FIX §8.1 item 1 should be withdrawn. If they are not, §3.5 needs the edit, not l.618.
2. **l.1020's a_RS is defined under the heading "Definitions for the induction" inside §7.1**, which
   l.832 supersedes; the only place η_1²/(2N) becomes a *cost* is **(TS-c) at l.1183-1186, in §7.3**,
   which **l.835** says is *"not used by RLF-step v3"*. If a_RS is live anywhere else, that place should
   be named.
3. **l.65's η_1 ≤ η_q does reverse under the adoption** (RA-5): to **39.3846×** (N = 2) / **59.0769×**
   (N = 3). ARS_FIX is right about this.

### 7.3 For HIST's owner

**ARS_FIX §8.4 item 1 will arrive with the figure 1551×. The figure your own l.185-186 defines is
201.029× (N = 2) / 452.315× (N = 3)**, because your sentence prices the joint route at **a_η/81** against
the RS route's **a_RS/625** and ARS_FIX keeps only the η² half. Your l.181's `η_q/η_1 = 2/ε_1` becoming a
constant is right, but the constant is **117/(256·N·A_d)** — 0.025390625 at N = 2, **0.016927** at N = 3.

### 7.4 For the lead

1. **Lead with RA-15, RA-16 and RA-17 when you brief the next wave.** The arithmetic of both files is
   clean; the framing is not, and three of the four figures that would have gone into PROOF.md's ledger
   (82 decades of value; 1551× route reversal; "RLARGE l.618 is FALSE") need restating.
2. **D4's chain is wrong in its ordering (RA-11), and the reason is not H1.** Even if H1 is discharged
   today and KN-step′ lands, (C6) and (C7) are undischarged and (C3) is a two-lane edit.
3. **EPS1_SWEEP's §5 status word should be CONDITIONAL, not "SAFE WITH NAMED CONDITIONS"** — its own
   (C7) says so in the first six words.
4. **Two unfalsifiable gates are in a *pre-registered* script, not only a post-hoc one** (RA-10):
   `ar1_margins.py` l.244-245 and l.269-271. §53's defect 3 is still live in session 24's own output.
5. **This review is itself evidence, not a certificate.** The thing I am least sure of is RA-15: it
   turns on whether RLARGE §3.5's *"not consumed"* is current, and only RLARGE's owner can say. If it is
   not current, RA-15 falls and ARS_FIX's headline stands as written — **but RA-16 and RA-17 survive
   either way**, because they are about which route the 82 decades is measured against, not about
   whether a_RS is consumed.

*(End of REVIEW_ARS_EPS_S1.md. Files written by me: this file, `checks/ra1_criteria.md`,
`checks/ra1_margins.py`, `checks/ra1_out.txt`, `checks/ra1_err.txt`, `checks/ra1b_margins.py`,
`checks/ra1b_out.txt`, `checks/ra1b_err.txt`. Nothing else, anywhere. No git command was run by me.
No numeric lock was taken and none was needed — exact rational arithmetic, brief rule 6; 0.3 s real.)*
