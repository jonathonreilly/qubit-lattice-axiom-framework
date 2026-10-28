# GESIGN.md — target T55-O: the sign structure of the bootstrap kernel `G_e`, and the
# circularity in Corollary FB-NBHD

Worker file. Owned: this file and `checks/gs1_*`. No other file is edited. No git command is run.

---

## 1. PRE-STATED — statements only. THIS IS THE FIRST EDIT OF THIS FILE, written
## 2026-10-28T21:46:35Z, before any derivation, any script and any arithmetic of this session.

### 1.0 Inputs, named (not re-judged here)

- **`FACEB.md`** (T55-G, UNREVIEWED, written ~21:17-21:40Z today). My scope is set by its
  Proposition **FB-BOOT** (§4.3), its Corollary **FB-NBHD** (§6.4), its Proposition **FB-ONE-LEG**
  (§3.3) and its §9.3. FACEB is my *input*, not my authority: every load-bearing step I take from it
  is re-derived here from the primary files, per the session-25 rule that a banked PROVEN is evidence
  and not a certificate.
- The primary files: **`BFT_A.md`** (§21-§23, §26-§28, §31, §33, §38), **`BFT_B.md`** (§35),
  **`YSUP.md`**, **`TENTQ.md`**.

### 1.1 Disclosure of reading order, and what it costs in pre-registration weight

Before writing this section I read, in this order: the session-25 drive brief; `HANDOFF.md`;
`SESSION25_RESULTS.md`'s T55-G entry; `FACEB.md` §3.3, §4, §6.4, §9, §10, §11; `BFT_A.md`
l.1680-1760 (§21.0-§21.3), l.1860-1935 (§23.1-§23.4), l.2320-2400 (§27 U4-U4'), l.2579-2600 (§28.12),
l.2755-2835 (§31.1), l.2973-3010 (§33.3-§33.5), l.3030-3050 (§33.7), l.3385-3400 ([RBA7-fix] P7-3),
l.3530-3625 (§38.6-§38.9); `BFT_B.md` l.4105-4135 (§35.6-§35.8).

**My reasoning during that reading went beyond reading.** In unrecorded form I formed, before writing
this section, (a) a suspicion about the status of the constant `½` in `Σ_q|G_e(q)| ≤ ½`, (b) a
suspicion about the `r = ∞` branch of Lemma LD, and (c) a suspicion about the base point of the
iteration `Φ_E`. Targets and failure modes below that bear on those three **carry no pre-registration
weight** and are marked **(c)**, following this lane's own convention (BFT_A §21.3). Everything else
is pre-registered in the ordinary sense. I record this rather than pretend to a blank slate, because
pretending would be the more serious breach.

### 1.2 Targets (written before any derivation of this session)

**GS1 — what `G_e` is.** State the construction of the bootstrap kernel `G_e` from the primary file,
by file:line, with the operator that produces it and the current it is applied to, and with every
symbol disambiguated against SYMBOLS.md's defect-1 list.

**GS2 — the sign structure of `G_e(q)`, computed, not estimated.** Decide, from the construction:
(i) whether the `G_e(q)` are of one sign; (ii) what `Σ_q G_e(q)` is as a **signed** quantity;
(iii) whether that signed quantity is an invariant of the current or an artefact of the particular
primitive chosen; (iv) whether the lead of FACEB §4.3 — *"the funnel coefficients are already
sign-coherent"* — transfers to `G_e`, which is a different object.

**GS3 — what the sign statement buys.** Decide, and say in which direction: does a sign statement on
`G_e` give the matching **lower** bound that makes face (b)'s `n²` sharp for the actual response, or
does it expose a **cancellation** that makes it not sharp? **(c)** If a cancellation is available,
quantify it as a fraction of `A := |Φ_k(g^♮_0)|`. No preference is formed before computing; both
outcomes are reported with the same weight.

**GS4 — Corollary FB-NBHD promoted out of a parenthetical.** State the circularity of BFT_A l.3613 as
a **named clause with full quantifiers**: the three arrows, each with its quantifier over
configurations, over iteration step, over `k` and `T`, and with the norm in which each smallness is
asserted.

**GS5 — try to break the circle.** Test, in this order: (i) does the circle actually close, or is one
of the three arrows weaker than its statement? **(c)** (ii) a bootstrap / continuous induction along a
connected contraction parameter; (iii) a weaker smallness that suffices for `(NC-Γ)` and is available
unconditionally; (iv) a different quantity the contraction produces earlier; (v) an a-priori bound
supplying the first step. Report which arrow is weakest and whether the circle closes.

**GS6 — verify FB-ONE-LEG.** Decide whether the two `L^{2k−3}` defects of the `Γ_E` response off the
critical set are two functionals of one argument `D(S)`. If they are, say whether items GS2-GS3 and
GS4-GS5 and the `Γ_E` defect are one problem.

### 1.3 PRE-REGISTERED VERDICTS (written before any script and before any derivation)

For GS2, exactly one of:
- **SIGN-COHERENT** — the `G_e(q)` are provably of one sign, or `Σ_q G_e(q)` is provably bounded away
  from `−½` by a computed margin.
- **SIGN-MIXED** — the `G_e(q)` provably take both signs, with the mechanism named.
- **SIGN-MOOT** — the question is ill-posed or vacuous at the point of use, because the kernel's size
  or existence is not what the bootstrap display asserts. **(c)**
- **SIGN-OPEN** — none of the above is decidable from the construction.

For GS3, exactly one of: **SHARP** (the lower bound follows), **CANCELS** (a cancellation of a named
fraction of `A` is available), **NEITHER** (the question is replaced by a different one, named).

For GS5, exactly one of: **CIRCLE-CLOSES** (all three arrows hold as stated and no route out was
found), **CIRCLE-BREAKS** (a named arrow is weaker than stated, or a named route out works),
**CIRCLE-PARTIAL** (the circle becomes an induction with a named residual gap).

For GS6, exactly one of: **ONE-LEG-HOLDS**, **ONE-LEG-FAILS**, **ONE-LEG-OPEN**.

### 1.4 Pre-registered failure modes, with expectations

- **GS-F1** `G_e` is not a single object: the symbol collides across `§21.1`, `§23.3`, `§27` and
  `§38.7`. *Expected: does not occur (one construction, several bounds).*
- **GS-F2** the `½` of BFT_A l.3568 is a **threshold fixed for a different consumer** and not the
  size the lemma proves. **(c)** *Expected: occurs.*
- **GS-F3** the sign question has no answer because the kernel's sign depends on the free parameter
  of the construction. *Expected: occurs in a strong form.* **(c)**
- **GS-F4** FACEB's identification of YSUP's witness `u = ⅛d*δ_p` with §38.7's `g_0` is wrong, and
  `A` is therefore not YSUP's number. *Expected: occurs; expected to change no conclusion.*
- **GS-F5** one of FB-NBHD's three arrows is not a dependency of its consumer but of a stronger
  statement nobody needs. **(c)** *Expected: occurs on arrow (γ).*
- **GS-F6** FB-ONE-LEG is false because the two defects are the same term double-counted, not two
  terms. *Expected: does not occur, but if it does it strengthens FB-ONE-LEG rather than refuting it.*
- **GS-F7** my own gate cannot fail: any numeric check I write is a test of my own implementation of
  Lemma PC rather than of the lane's claim. *Mitigation pre-committed: a designed-FAIL control whose
  input is known to violate the clause, reported as having fired.*

### 1.5 Scope limits accepted in advance

1. I do **not** re-derive Theorem Y, Theorem COF, Proposition SR, Proposition TE or Lemma RC. I quote
   them and re-derive only the steps my conclusions rest on.
2. I do **not** compute `Φ_k` of anything. YSUP owns that number; I treat `A` and `B` as symbols.
3. I do **not** attempt `(TENT-Q)`, `(NEUT-box)` or `(PW-ℓ¹)`.
4. Any statement about the *size* of `C_j`, `C_Z(c)`, `C_β` or `C_SR` is quoted, never produced here.
5. Nothing in this file moves the PROOF.md tally, and nothing here is an audit judgement.

### 1.6 Process commitments

PRE-STATED first (this section). Criteria file `checks/gs1_criteria.md` before any script, containing
no constant derived in this session. Exact integer / `Fraction` arithmetic in plain python; no numpy,
no BLAS, no machine-wide numeric lock. Statuses strictly PROVEN-HERE / ARGUED / CONDITIONAL / GAP /
OPEN. Any probe run after seeing a result is labelled post-hoc. A designed-FAIL control for every
gate, reported as having fired or not fired. Line numbers: located by string, never by offset
(SYMBOLS.md §13); every `file:line` below was re-checked by `grep`/`sed` against the live file at the
time of writing.
