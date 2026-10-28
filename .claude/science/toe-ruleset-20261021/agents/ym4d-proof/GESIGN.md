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

---

## 2. What `G_e` is (target GS1). Appended after §1 (21:46:35Z) and after
## `checks/gs1_criteria.md` (21:52Z) and after `checks/gs1_pc.py` and its output; written
## 21:53 UTC.

### 2.1 The construction, by file:line

`G_e` is **not** a kernel given by a formula at the point of use. It is the output of one explicit
operator applied to one explicit current, both produced inside **Lemma LD** (BFT_A.md l.1711-1718,
proof §23.3 at l.1900-1917):

> *"With `J := 𝔽^{(0→k)}d*G'` and `e := d*G' − (Q_str^{(0→k)})^TJ`, one has `Z = Z' + Σ_qG_e(q)Y^q`,
> where `G_e := 𝒫e` (Lemma PC), and `Z'` minimises `E_src` with data `β` and the residual-type
> sources `s_i := (Q^{(i+1→k)})^TJ`."* (BFT_A.md l.1716-1718)

The three ingredients, each pinned:

1. **`𝒫`, the operator** — Lemma PC, BFT_A.md l.1705-1708, proof §23.1 at l.1874-1892. It is a **signed
   one-sided cumulative sum along the first axis**, iterated down in dimension:
   `G_{aν} := −S_ν + 1[z_a ≥ b]W_ν` with `S_ν(z) := Σ_{t≤z_a}e_ν(t, z')` and
   `W_ν(z') := Σ_t e_ν(t, z')` (l.1879-1880), plus a transverse `(d−1)`-dimensional copy of itself on
   the single slice `z_a = b` (l.1883). It satisfies `d*G = e` exactly and `Σ|G| ≤ 3qΣ|e|` on a cube of
   side `q`.
2. **`e`, the current** — `e := d*G' − (Q_str^{(0→k)})^TJ`, co-closed (BFT_A.md l.1911-1912) and
   supported in a cube of side `q ≤ 2.05r` about `p` (BFT_A.md l.2345, l.2601).
3. **`G'`, the source of `e`** — `G' := χh_p − [Δ_0, χ]ω^p` with `χ := Φ_{r,p}` a product cutoff at
   radius `r`, `ω^p := Δ_0^{-1}(δ_p − h_p)`, and `h_p` the **constant** 2-form of `p`'s orientation
   with total sum 1 (BFT_A.md l.1693-1694, l.1711-1712).

### 2.2 The free parameter, which is the whole story (defect 2: *"check what someone fixed once"*)

Lemma LD is stated for **every** `χ = Φ_{r,p}` with `1 ≤ r ≤ M/4`, **and for `χ :≡ 1`** ("`r = ∞`"):
BFT_A.md l.1711, *"Let `χ := Φ_{r,p}` with `1 ≤ r ≤ M/4`, or `χ :≡ 1` ("`r = ∞`")"*. So `G_e` is not
one object but a **one-parameter family** `G_e^{(r)}`, while the object it decomposes, `Y^p`, does
not depend on `r` at all (`Y^p` is defined at BFT_A.md l.1691-1693 as a minimiser of `E_src` with the
single source `δ_q`, with no `r` in sight).

Theorem Y picks `r := L^{k+c}` when `T ≥ 8L^c` and `r := ∞` otherwise (BFT_A.md l.1869,
dated precision 2), and `c` is then fixed by **`L^c ≥ max(260, 3476C_j)`** ([RBA5-fix] U4′,
BFT_A.md l.2344-2346). **That choice is made for Theorem Y's constants, not for the bootstrap**, and
nothing downstream of §38.7 re-examines it.

**GS-F1 does not occur:** one construction (`𝒫e`), several bounds on it. No symbol collision: the
`G_e` of l.1716, l.1915, l.2345, l.2601, l.3093 and l.3568 are the same object, and `G'`, `G_e` and
`𝒫` are distinct symbols throughout.

**One correction, and it belongs to YSUP rather than to FACEB.** The sentence *"the very field
BFT_A §38.7 takes as `g_0`"*, which FACEB §4.2 repeats, is **YSUP's own**, at YSUP.md l.229-230
(Theorem YS-CORE (ii)). It is not right. §38.7's `g_0` is
`d*(χω^p)` in Case A (BFT_A.md l.3557) and `y^p = d*ω^p` in Case B (BFT_A.md l.3570) — a lattice
**Green's-function dipole**, not a four-link field; `g_0 = Δ_0^{-1}(d*δ_p) = 8Δ_0^{-1}u` at `r = ∞`,
since `d*h_p = 0`. Both fields lie in FACEB's class `𝒴` (co-closed, profile `(1+|z−p|)^{-3}`;
`|g_0| ≤ C_0'(1+|z−p|)^{-3}` at BFT_A.md l.3557, `|y^p| ≤ C_K(…)^{-3}` at l.3570), so **Proposition
FB-CLASS is unaffected**. What is affected is the identification of `A := |Φ_k(g^♮_0)|` with YSUP's
`2.4768·10⁻³`: BFT_A itself marks that identification **ARGUED** and supports it by a *measurement*,
`a = −0.0022` at `k = 2, T = 2` (BFT_A.md l.3583), against the witness's exact `−0.0024768`.
**GS-F4 occurs, as expected, and changes no conclusion** — but `A` must be carried as a symbol with
an ARGUED numerical value, not as YSUP's exact rational. I carry it as a symbol (scope limit §1.5.2).

---

## 3. The sign structure of `G_e`, computed (target GS2)

### 3.1 First: the kernel can be taken **identically zero**. **PROVEN-HERE.**

> **Proposition GS-ZERO (PROVEN-HERE, from Lemma LD's own hypotheses).** Take `χ ≡ 1` (`r = ∞`) in
> Lemma LD, which Lemma LD admits for every `k ≥ 1` and every `T ≥ 1` (BFT_A.md l.1711). Then
> `G' = h_p` is a **constant** 2-form, so
>
>   `(d*G')_ν(z) = Σ_μ[G'_{μν}(z − e_μ) − G'_{μν}(z)] = 0` identically,
>
> hence `J = 𝔽^{(0→k)}d*G' = 0`, hence `e = d*G' − (Q_str^{(0→k)})^TJ = 0`, hence
> **`G_e = 𝒫e ≡ 0`** and the residual sources `s_i = (Q^{(i+1→k)})^TJ` vanish too. The decomposition
> of BFT_A.md l.3560 collapses to
>
>   **`Y^p ≡ g^♮ + Z″` exactly, with `g_0 = y^p = d*ω^p` and `Z″` the SOURCE-FREE minimiser with
>   data `β_str = −Q_str^{(0→k)}y^p`.**

*Proof of the only non-quotation step.* `d*` of a constant 2-form is zero by the convention fixed at
BFT_A.md l.1872 (each term of `Σ_μ[G_{μν}(z−e_μ) − G_{μν}(z)]` cancels). The energy only ever sees
`G'` through `−⟨G', dZ_0⟩` (BFT_A.md l.1909), which equals `−⟨d*G', Z_0⟩ = 0`. ∎

*One textual discrepancy, flagged because a reviewer will meet it.* Lemma LD's statement says
*"(and `G' = 0` for `r = ∞`)"* (BFT_A.md l.1713) and §23.3 step 1 repeats it (l.1904). Taken
literally that is **false**: at `χ ≡ 1`, `G' = χh_p = h_p ≠ 0`. What is true, and what every use of
`G'` needs, is **`d*G' = 0`** and `⟨G', dZ_0⟩ = 0`. The conclusion is unchanged and in fact
strengthened — `e = 0` follows from `d*G' = 0` alone — but the sentence should be corrected, because
a reader checking `G' = 0` against `G' := χh_p − [Δ_0, χ]ω^p` will conclude the lemma is wrong.

This is **not new mathematics**: it is BFT_A's own Case B, which states the same collapse in the same
words — *"`Y^p ≡ g + Z` with `g_0 = y^p` … **No bootstrap.**"* (BFT_A.md l.3570-3573). What is new is
the observation that **the case split is a choice about Theorem Y's constants, not a constraint on
the decomposition**: `r = ∞` is available at every `T`, and the only thing it costs is that Lemma
EX's shell count becomes `J + 2` with `L^J ≤ M/4 = Tn/4`, i.e. `≈ k + log_L T` instead of `k + c`
(BFT_A.md l.1928-1930) — a `T`-uniformity loss **in Lemma EX's depth factor**, which is a statement
about the *upper* bound on `Φ_k(g^♮)`, not about the lower bound at issue in FB-BOOT.

> **Consequence for FACEB §4.3 / §9.3 / §10.** The missing input FACEB names — *"a sign or positivity
> statement on the bootstrap kernel `G_e(q)`"* — **is not missing.** It is available in the strongest
> form a sign statement can take, `G_e ≡ 0`, by a parameter choice already inside the lane's Lemma LD,
> and BFT_A already writes the resulting decomposition. **Pre-registered verdict SIGN-MOOT.**
> **GS-F3 occurs in its strong form:** the sign of `G_e` depends on the free parameter `r`, and at one
> admissible value of `r` there is no `G_e`.

### 3.2 Second: where the kernel is not zero, the `½` is a **threshold, not a size**. **PROVEN-HERE
### as a reading of two quoted lines.**

BFT_A.md l.3568 states `Σ_q|G_e(q)| ≤ ½ (U4′)`. U4′ itself (BFT_A.md l.2344-2346) proves

  **`Σ|G_e| ≤ 1738C_jL^{-c}`**, *"and the contraction `Σ|G_e| ≤ ½` holds for `L^c ≥ max(260, 3476C_j)`"*.

So `½` is the value of a bound that is `O(L^{-c})` **evaluated at the smallest `c` Theorem Y needs**.
It is a sufficient threshold for the contraction, chosen in §27 for a different consumer, and `c` is
free upward (subject only to Case A's `T ≥ 8L^c`). **GS-F2 occurs, as expected.** This is defect 2 of
the session-25 brief in its exact form: an inequality correct at the constant it was written for, in
a file that later reads that constant as the quantity's size.

### 3.3 Third: the honest sign facts about `G_e` where it is nonzero. **PROVEN-HERE** (three
### elementary lemmas), with `gs1` as the control.

These matter because a future worker may want the finite-`r` branch.

> **Lemma GS-ZS (zero component sums). PROVEN-HERE.** Let `e` be a co-closed 1-form with compact
> support in a lift (no wrap). Then `Σ_z e_ν(z) = 0` for **every** component `ν`.
>
> *Proof.* Pair `d*e = 0` with the coordinate function `z_ν`:
> `0 = Σ_z z_ν(d*e)(z) = Σ_μ Σ_z z_ν[e_μ(z − e_μ) − e_μ(z)]`. For `μ ≠ ν` the shift does not move
> `z_ν` and the two terms cancel. For `μ = ν`, reindexing the first term gives
> `Σ_z (z_ν + 1)e_ν(z) − Σ_z z_νe_ν(z) = Σ_z e_ν(z)`. ∎ (`gs1` A2 PASS, 12/12; control A6a FIRED.)

**Consequence: `e` is provably NOT sign-coherent in any component that does not vanish.** FACEB's
lead — *"the funnel coefficients are already sign-coherent"* — is about `φ_1 = −1/432`,
`φ_2 = −17/104976` (REVIEW_BFT_A_S8 S8-7, quoted at FACEB §4.3), a **different object**: the funnel
coefficients of `Φ_k`, not the bootstrap kernel. **The lead does not transfer, and on the current `e`
it is provably false.** (Target GS2 (iv) answered.)

> **Lemma GS-FM (the signed total of a primitive is a first moment, and is primitive-independent).
> PROVEN-HERE.** Let `e` be co-closed with compact support in a lift and let `G` be **any** 2-form
> with `d*G = e` and compact support. Then for all `μ, ν`
>
>   **`Σ_z G_{μν}(z) = Σ_z z_μ e_ν(z) =: M_{μν}(e)`,  and `M(e)` is antisymmetric.**
>
> *Proof.* `Σ_z z_μ e_ν(z) = Σ_λ Σ_z z_μ[G_{λν}(z − e_λ) − G_{λν}(z)]`; the `λ ≠ μ` terms cancel and
> the `λ = μ` term telescopes to `Σ_z G_{μν}(z)`. Antisymmetry: pair `d*e = 0` with `z_μz_ν` to get
> `M_{νμ} + M_{μν} + δ_{μν}Σ_z e_μ = 0`, and use Lemma GS-ZS. ∎ (`gs1` A3, A4 PASS, 12/12; A4 is
> non-vacuous — the reversed-axis primitive differs pointwise; controls A6b, A6c FIRED.)

**Consequence: `Σ_q G_e(q)` — the signed total the FB-BOOT question is about — is an invariant of
`e`, not an artefact of Lemma PC's axial gauge.** (Target GS2 (iii) answered: it is an invariant.)

> **Lemma GS-MOM (the first moment of the inner current, exactly). PROVEN-HERE.** For every cutoff
> `χ` (every `r`, finite or infinite), with `p` of orientation `(α, β)`:
>
>   **`M(d*G') = M(d*δ_p)` = the unit antisymmetric matrix in the `(α, β)` plane, exactly.**
>
> *Proof.* `d*G' = d*δ_p − d*dg_0 = d*δ_p − Δg_0` (BFT_A.md l.1903, `g_0` co-closed). `g_0` has
> compact support in the lift, and `Δ z_μ = 0` for the lattice Laplacian, so
> `M_{μν}(Δg_0) = Σ_z z_μ(Δg_0)_ν = Σ_z (Δz_μ)(g_0)_ν = 0`. For `d*δ_p`, Lemma GS-FM with the
> primitive `δ_p` gives `M_{μν} = Σ_z (δ_p)_{μν}(z) = 1` at `(μν) = (αβ)` and 0 otherwise. ∎

So the whole signed total of `G_e` comes from the level-`k` subtraction:
`M(e) = 1_{αβ} − M((Q_str^{(0→k)})^TJ)`. **I did not compute the second term** — it needs `Q_str` and
`𝔽` in explicit form, which §1.5.1 puts out of scope. **Flagged as the one piece of GS2 (ii) left
OPEN**, and it is only needed if someone insists on the finite-`r` branch.

> **Remark GS-CUM (why sign coherence of `G_e` is the wrong thing to ask for).** `𝒫` is a **signed
> one-sided cumulative sum**: `G_{aν}(z) = −Σ_{t≤z_a}e_ν(t, z')` for `z_a < b` and `0` for `z_a ≥ b`
> (BFT_A.md l.1879, l.1888). So `G_e` is sign-coherent in its `(a, ν)` components exactly when the
> **partial sums** of `e_ν` are one-signed along every axial line — which is neither implied by nor
> implies anything about the signs of `e` itself, and which depends on the axis order. `gs1` A5
> measures both ends of this: **0 of 12** generic co-closed currents give a sign-coherent `𝒫e`
> (**SIGN-MIXED**), while the single-plaquette current `e = d*δ_q` gives `𝒫e = δ_q` exactly
> (one value, `+1`) — **sign-coherent**. So there is **no general no-go** and **no general theorem**:
> the sign of `G_e` is a property of the particular `e` and of the axis order, and it is not a thing
> the lane can prove in general. This is the second reason the route of §3.1 is the right one.

### 3.4 GS2 verdict

**Primary: SIGN-MOOT** (Proposition GS-ZERO: the kernel can be taken `≡ 0`; and where it is not, its
size is `1738C_jL^{-c}` with `c` free, not `½`).
**Subsidiary, for the finite-`r` branch: SIGN-MIXED** for the current `e` (Lemma GS-ZS, PROVEN) and
for generic `𝒫e` (`gs1` A5, 0/12), with the actual `𝒫e`'s coherence **OPEN** and axis-order-dependent.

---

## 4. What the sign statement buys, and in which direction (target GS3). Written 21:54 UTC.

### 4.1 The FB-BOOT algebra with the coefficient kept as a symbol. **PROVEN-HERE, elementary.**

FACEB §4.3 runs the bootstrap at `ε := Σ_q|G_e(q)| = ½`. Keep `ε` free. With
`A := |Φ_k(g^♮_0)|`, `B := sup|Φ_k(Z″_0)|`, `M := sup_p|Φ_k(Y^p_{*,0})|`, and `Φ_k` linear:

- `M ≤ A + B + εM`, so **`M ≤ (A + B)/(1 − ε)`**;
- `|Φ_k(Y^p)| ≥ A − B − εM ≥ A − B − ε(A + B)/(1 − ε)` = **`[A(1 − 2ε) − B]/(1 − ε)`**.

> **Proposition GS-WINDOW (PROVEN-HERE).** The lower bound is positive **iff `B < A(1 − 2ε)`**. The
> cancellation the bootstrap admits is exactly **`2ε` as a fraction of `A`** — not `A`.

At `ε = ½` the right side is `0` and nothing follows: **that, and only that, is FB-BOOT's
"no lower bound at all".** It is the value of a one-parameter family at the single point where the
family is degenerate. (Exact check, labelled **post-hoc** — it is arithmetic on quoted constants, run
after `gs1`: at `ε = ½, ¼, 1/100, 0` the bound at `B = 0` is `0, 2/3, 98/99, 1` in units of `A`.)

### 4.2 The cancellation, quantified (target GS3's explicit demand)

With U4′'s `ε ≤ 1738C_jL^{-c}` (BFT_A.md l.2345), the cancellable fraction of `A` is
`2ε ≤ 3476C_jL^{-c}`:

| cancellable fraction of `A` | needs | Case A also needs |
|---|---|---|
| 100 % (the `½` of l.3568) | `L^c ≥ 3476C_j` | `T ≥ 27808C_j` |
| 50 % (the `¼` form of §26.3) | `L^c ≥ 6952C_j` | `T ≥ 55616C_j` |
| 1 % | `L^c ≥ 347600C_j` | `T ≥ 2.7808·10⁶C_j` |
| **0 %** | **`r = ∞` (Proposition GS-ZERO)** | **nothing** |

Going from 100 % to 1 % costs **5 extra powers of `L` at `L = 3`** (`log_3 100 = 4.1918`). Going to
0 % costs nothing at all and is the `r = ∞` branch BFT_A already writes. *(`C_j = 12C_G`, built from
`C_K` and `C_φ`, both uncomputed — BFT_A.md l.2331. Per §1.5.4 I quote it and do not size it, so
the second and third columns are conditional on `C_j`, and the `r = ∞` row is not.)*

### 4.3 What the question becomes. **Verdict NEITHER, pointing toward SHARP.**

At `r = ∞` the inequality is `|Φ_k(Y^p_{*,0})| ≥ A − B` with

- `A = |Φ_k(g^♮_0)|`, `g_0 = y^p = d*ω^p` — the lattice Green's-function dipole;
- `B = sup|Φ_k(Z″_0)|`, `Z″` the **source-free** minimiser with data `β_str = −Q_str^{(0→k)}y^p`.

So the missing input is **not a sign statement and not about `G_e`**: it is the two-sided comparison
`B < A`, i.e. *does the terminal-data response `Z″` beat the explicit dipole at the level-`k` roots?*
Two named pieces, both outside my scope but both well-posed:

> **(GS-A) `A` is `k`-free and positive.** BFT_A measures `a = −0.0022` at `k = 2, T = 2`, offset
> `(1,0,0,0)` and marks the identification **ARGUED** (BFT_A.md l.3583); YSUP proves the exact
> `k`-free `−65/26244 = −2.4768·10⁻³` for the four-link witness `u`, which is a **different field**
> (§2.2). **OPEN for `g_0`; ARGUED-and-measured.**
>
> **(GS-B) `B = O(n^{-2})`.** BFT_A's own Case B bound is
> `‖Z_str‖_{inv,m'} ≤ G_D(m')‖β_str‖_{D,m'}` with `‖β_str‖_{D,m'} ≤ C_βe^{128m'L^c}n^{-2}`
> (BFT_A.md l.3571-3572) — i.e. `Z″` is small **by `n^{-2}`**. What is missing is one line: that `Φ_k`
> is a bounded functional on the `inv`-ball with a `k`-uniform constant. BFT_A's own scaling supports
> it — `φ_{i+1}(x_0) ≍ L²·(level-i gradient) ≍ L^{2(i+1)}η/n²`, so `Φ_k(x_0) ≍ L^{2k}η/n² = η ≍
> ‖∇^cx^c_0‖_∞` (BFT_A.md l.3607-3608) — but it is **not written**. **CONDITIONAL on that line.**

> **Corollary GS-SHARP (CONDITIONAL on (GS-A) and (GS-B)).** At `r = ∞`, for every `k` with
> `L^{2k} > C·C_Z/A`, `|Φ_k(Y^p_{*,0})| ≥ A − B ≥ A/2 > 0`, `k`-freely. **Face (b)'s `n²` is then
> SHARP for the actual response**, and the pre-registered outcome **CANCELS does not occur**: the
> cancellation FB-BOOT reports is an artefact of `ε = ½` and is zero at `r = ∞`.
>
> *Honest caveat, which I will not paper over:* the `k`-threshold `k_0 := ⌈log_L(C·C_Z/A)/2⌉` is set
> by `C_Z` / `C_β e^{128m'L^c}`, constants §1.5.4 forbids me to size. **So this is an asymptotic
> sharpness statement with an unsized threshold, not a finite-`k` one.**

**GS3 verdict: NEITHER** — the question is replaced by a different, named one (`B < A`, i.e.
(GS-A) + (GS-B)) — **and the direction it points is SHARP, not CANCELS.** I record that I had formed
no preference before computing: failure mode GS-F3 was pre-registered as *expected to occur*, and it
did, but in the direction that removes the cancellation rather than the one that supplies it.

---

## 5. Corollary FB-NBHD promoted out of a parenthetical (target GS4). Written 21:54 UTC.

BFT_A.md l.3612-3613 carries the whole item as a two-sentence parenthetical at the end of §38.8:

> *"Alternatively the contraction can be arranged so that its linear solve only meets
> composite-co-closed sources up to remainders multiplied by `∇(𝔉_k∘exp)` (Lemma CD). **Not
> attempted.**"*

and BFT_A.md l.2595-2598 (§28.12 Remark 2) carries **the same proposal in different words**:

> *"A formulation that iterates only the composite-co-closed projection of the equation, and recovers
> full criticality from (FP♯′) for the projecting gauge, would remove `V` altogether. **Not
> written.**"*

**These two parentheticals are one item and should be merged.** Here it is, named and quantified.

### 5.1 Setting and symbols, each pinned (defect 1)

Setting LIN at the **trivial** background, `m = 0`, `d = 4`, `L ≥ 3` odd. `k ≥ 1`, `T ≥ 1`,
`n := L^k`. Data `B_k`. Gauge fixing `Γ_E` (lane B's slice `S_E`, LEAD DECISION of §31).

- `H` — the quadratic form of the chain energy; `Ξ` — the composite-gauge generator;
  `Λ_*` — gauge functions vanishing at the level-`k` roots.
- `𝓛_E := H + Γ_E^TΓ_E` (read off BFT_A.md l.2980).
- `𝔑^0(x; B)` — the nonlinear remainder, defined by
  `∇(𝔉_k∘exp)(x; B) = Hx − N_B − 𝔑^0(x; B)` (BFT_A.md l.2976). Write `∇𝔉(x)` for the left side.
- `Φ_E(x) := 𝓛_E^{-1}(N_B + 𝔑^0(x; B))` (BFT_A.md l.2791).
- `K_x` — `(K_xξ)_j(b) := d/dt|_0 log(e^{tξ_j(b^-)}e^{x_j(b)}e^{-tξ_j(b^+)})` (BFT_A.md l.2760);
  **`K_0 = −Ξ`** and **`K'_x := K_x − K_0`** (BFT_A.md l.2761).
- `D(S) := Ξ^TS` — the composite divergence of a source `S`.
- `Ψ^p` — the root function `σ(Π_EY^p)` at non-level-`k` roots (Lemma RC, BFT_A.md l.3545-3547) and
  `Φ_k(Y^p_{*,0})` at the level-`k` roots (Proposition COF-res, BFT_B.md l.4113-4116). See §7.
- `𝔅_η := {x : ‖x‖_𝔐 ≤ η}`; `η_0` is SPD's radius (BFT_A.md l.2809).
- `C_SR` — Proposition SR's constant (BFT_A.md l.2808-2811), `k`-, `T`-uniform.

### 5.2 The clause

> ### **Clause (FB-CIRC)** — the circularity of Corollary FB-NBHD, stated with quantifiers.
>
> **(α) Response ⟸ gradient smallness.** *For every `L, k, T`, every `η ≤ η_0` and every
> `x ∈ 𝔅_η`:* the `Γ_E`-response to the rows `V(x)` of `x` obeys
> `‖f_0[V(x)]‖_∞ ≤ C_SRη² + n²|⟨D(V(x)), Ψ^p⟩|`, and `D(V(x)) = −K'^T_x∇𝔉(x)` (Lemma CD,
> BFT_A.md l.2789-2792, PROVEN-HERE given (GI) at l.2973-2982). *Hence there is `c_1 = c_1(L)` such
> that if*
>   **`‖K'_x‖·‖∇𝔉(x)‖_† ≤ c_1η²n^{-2}`**  *(`‖·‖_†` the norm dual to `sup|Ψ^p|`),*
> *then `(NC-Γ)` holds at `x` with its `k`-, `T`-uniform constant.* Using the ARGUED
> `|K'_xξ| ≤ C|x||ξ|` (BFT_A.md l.2984), a sufficient form is **`‖∇𝔉(x)‖_† ≤ c_2ηn^{-2}`** — which
> is FACEB's FB-NBHD set `{‖x‖_𝔐 ≤ η, ‖∇(𝔉_k∘exp)(x)‖ ≲ C_SRL³ηn^{-2}}`.
>
> **(β) Gradient smallness ⟸ the contraction's steps.** *For every `x_0 ∈ 𝔅_η` and the orbit
> `x_{j+1} := Φ_E(x_j)`:* if the orbit converges to a fixed point `x_*` then `∇𝔉(x_*) = 0`
> (Lemma CD (ii), BFT_A.md l.2791-2792 with [RBA7-fix] P7-3, l.3392-3395), so `‖∇𝔉(x_j)‖ → 0`;
> *there is `J = J(η, k, L)` such that `‖∇𝔉(x_j)‖_† ≤ c_2ηn^{-2}` for all `j ≥ J`.*
>
> **(γ) The steps ⟸ the response.** *For every `k, T` and every `η ≤ η_0`:* `Φ_E` is a self-map of
> `𝔅_η` and a contraction there **only if** `(NC-Γ)` — the conclusion of (α) — holds **at every
> `x ∈ 𝔅_η`**; i.e. `‖x(S^E_0(V(x)))‖_inv ≤ Cη²` uniformly in `k, T` (Target (NC-E),
> BFT_A.md l.2812).
>
> **The circle.** (α) needs (β)'s smallness; (β) needs the orbit, which needs (γ)'s self-map; (γ)
> needs (α)'s conclusion on the whole ball.

**Quantifier audit, which is where the break is.** (α) quantifies over **points** of `𝔅_η`;
(β) over **orbit indices** `j`; (γ) over **points of `𝔅_η`** again. The mismatch is between (β),
which delivers smallness only along one orbit, and (γ), which demands the estimate at every point.
Nothing in the consumer needs the estimate at a point the iteration never visits.

---

## 6. Breaking the circle (target GS5). **The circle does not close. Arrow (γ) is the weakest and
## is false as stated; the base step is free; what is left is an `O(k)`-step transient.**
## Written 21:56 UTC.

### 6.1 The base step is free. **PROVEN-HERE from a DEFINITION, not from an estimate.**

> **Proposition GS-BASE (PROVEN-HERE given (GI); independent of the ARGUED bound
> `|K'_xξ| ≤ C|x||ξ|`).** At `x = 0`,
>
>   **`K'_0 = K_0 − K_0 = 0` exactly** (BFT_A.md l.2761 **defines** `K'_x := K_x − K_0`),
>
> so Lemma CD gives `D(𝔑^0(0; B)) = Ξ^T𝔑^0(0; B) = −K'^T_0∇𝔉(0; B) = 0`, **for every `B`, every `k`,
> every `T`**. Since `Ξ^TN_B = 0` identically (BFT_A.md l.2977-2978, a consequence of
> `r_{k-1}(Ξξ) = 0`, and it does not use (GI)), the **whole source the linear solve meets at the
> first step**, `N_B + 𝔑^0(0; B)`, is **composite-co-closed**: `(CC-0)` holds exactly.
>
> **Hence `(NC-Γ)` is NOT needed to take the first step.** What is needed there is Theorem COF under
> `(CC-0)`, which is **PROVEN**: `‖f_0‖_∞ + [f_0]^∞_α ≤ C_funC'η²`, `k`-, `T`- **and
> `Γ`-uniformly** (BFT_B.md l.4108-4110, Corollary COF-crit; and BFT_B.md l.4122:
> *"(CO-fun) is true under (CC-0) and false without it"*).

This is the brief's **"a-priori bound that supplies the first step for free"**, and it is exact
rather than approximate: the vanishing is a definition (`K'_0 = 0`), not a smallness.

### 6.2 Arrow (β) is not an asymptotic statement. It is an **exact per-step identity**.
### **PROVEN-HERE from two quoted definitions.**

> **Lemma GS-STEP (PROVEN-HERE).** Let `x_{j+1} := Φ_E(x_j) = 𝓛_E^{-1}(N_B + 𝔑^0(x_j; B))` with
> `𝓛_E = H + Γ_E^TΓ_E`. Then **for every `j`, with no convergence assumption**,
>
>   **`∇𝔉(x_{j+1}) = 𝔑^0(x_j; B) − 𝔑^0(x_{j+1}; B) − Γ_E^TΓ_Ex_{j+1}`.**
>
> *Proof.* `Hx_{j+1} + Γ_E^TΓ_Ex_{j+1} = N_B + 𝔑^0(x_j)` by definition of `x_{j+1}`. Substitute into
> `∇𝔉(x_{j+1}) = Hx_{j+1} − N_B − 𝔑^0(x_{j+1})`. ∎
> *(Consistency: at a fixed point `x_j = x_{j+1} = x`, this is `∇𝔉(x) = −Γ_E^TΓ_Ex`, which is exactly
> the first line of BFT_A's §33.3 (ii), l.2980. So Lemma GS-STEP is the one-step form of a line the
> lane already has.)*

So the quantity arrow (α) wants is, **at every step and not only in the limit**, a **step difference
plus the gauge violation**:

  `‖∇𝔉(x_{j+1})‖ ≤ Lip(𝔑^0; 𝔅_η)·‖x_{j+1} − x_j‖ + ‖Γ_E^TΓ_Ex_{j+1}‖`,

with `Lip(𝔑^0; 𝔅_η) ≤ C_Nη` because `𝔑^0` is the quadratic-and-higher part. **Arrow (β) is therefore
much STRONGER than Clause (FB-CIRC) states**, and it is the brief's *"a different quantity that the
contraction produces earlier than the smallness"*: the step difference is produced at step `j+1`
itself.

### 6.3 Arrow (γ) is false as stated. **The weakest arrow, and the one that breaks.**

(γ) asserts that the contraction needs `(NC-Γ)` **at every point of `𝔅_η`**. Its consumer — a Banach
iteration started at `x_0` — needs the estimate only **at the iterates it visits**. With §6.1 the
orbit may be started at `x_0 = 0`, where the hypothesis is free, and with §6.2 the requirement at
step `j+1` is readable from step `j`. The dependency is therefore

  `x_0 (free) → x_1 → x_2 → ⋯`

— **an induction on `j`, not a cycle.** **GS-F5 occurs, on arrow (γ), as pre-registered.**

> **Proposition GS-NOCIRC (PROVEN-HERE as an implication of GS-BASE + GS-STEP + Lemma CD).** Clause
> (FB-CIRC) is **not circular**. (α) at `x_{j+1}` depends on `∇𝔉(x_{j+1})`, which by Lemma GS-STEP
> depends on `x_j, x_{j+1}` and the gauge violation, and the induction is anchored at `x_0 = 0`,
> where `D = 0` exactly and Theorem COF applies unconditionally. **No step of the argument requires
> its own conclusion.**

### 6.4 What is actually left: an `O(k)`-step transient, priced. **ARGUED.**

Running the induction, at step `j ≥ 1`:

  `‖D(V(x_j))‖ = ‖K'^T_{x_j}∇𝔉(x_j)‖ ≤ C_Kη·[C_Nη·‖x_j − x_{j-1}‖ + ‖Γ_E^TΓ_Ex_j‖]`,

while (α) needs `≤ c_1η²n^{-2}`. With a contraction factor `θ < 1` and `‖x_j − x_{j-1}‖ ≤ θ^{j-1}‖x_1‖`:

  the first term meets the requirement **iff `θ^{j-1}‖x_1‖ ≲ n^{-2}`, i.e. iff
  `j ≳ 1 + (2k·log L + log‖x_1‖)/log(1/θ)`.**

> **Proposition GS-TRANSIENT (ARGUED; it uses `Lip(𝔑^0) ≤ C_Nη` and `‖K'_x‖ ≤ C_K‖x‖_𝔐`, the second
> of which BFT_A marks ARGUED at l.2984).** The residual gap in (FB-CIRC) is **not a circularity and
> not an `L^{2k}` of contraction**: it is the **first `J ≈ 2k·log L / log(1/θ)` steps**, i.e.
> `O(k)` steps of a geometric iteration, during which `(NC-Γ)` is available only with the extra
> factor `n²θ^{j-1}‖x_1‖`. **FACEB §6.4's "`2k·log_L` of contraction" is the right count of steps and
> the wrong reading of its cost**: a Banach iteration runs to convergence; `O(k)` steps is not a
> price, it is a loop bound. The price is only that the **self-map property** must survive those
> `O(k)` steps.

### 6.5 Three routes out of the transient, with honest verdicts

**(R1) Iterate inside the slice.** Replace `Φ_E` by a solve that preserves `S_E = Ker Γ_E`. Then
`Γ_E^TΓ_Ex_j ≡ 0` and Lemma GS-STEP reduces to `∇𝔉(x_{j+1}) = 𝔑^0(x_j) − 𝔑^0(x_{j+1})` exactly,
removing one of the two terms outright. **Cheap and PROVEN to remove that term** (it is Lemma
GS-STEP with the second summand zero); it does **not** remove the step-difference term.
*Status: PROVEN as a reduction; does not close the transient alone.*

**(R2) Iterate the composite-co-closed projection** — BFT_A.md l.2595-2598 and l.3612-3613, the two
parentheticals, merged. Project the source onto `{D = 0}` at every step. Then `D ≡ 0` at every step,
`(CC-0)` holds throughout, and Theorem COF gives the `k`-, `T`-, `Γ`-uniform `Cη²` at **every** step,
not only the first. **The entire transient disappears.** The cost moves to one statement:
*does the projected iteration still converge to a critical point of `𝔉_k`?* By Lemma CD (ii) a fixed
point of the **unprojected** map is critical; for the projected map the analogous statement is
BFT_A's unwritten `(FP♯′)`. **This is the route, and it is a finite-dimensional question:** what the
projection discards is the level-`k` root charges `Q_X = D(S)(c_X)`, **one scalar per level-`k` box**,
with `Σ_X Q_X = 0` already (BFT_B.md l.4114). *Status: the reduction is PROVEN-HERE given Theorem COF;
`(FP♯′)` is OPEN and is the real content of l.3613.*

**(R3) A graded ball** `η_j := η·min(1, n²θ^{j})` — the brief's open-closed / continuous-induction
shape. **It works formally and buys nothing.** The enlarged radius must stay inside SPD's `η_0`, so
`ηn² ≤ η_0`, i.e. **`η ≤ η_0L^{-2k}`** — exactly the `L^{-2k}` FACEB §6.4 already priced and
correctly called *"not a smallness condition, it is the absence of one"*. **Reported as a FAILED
route**, and reported because a reader would otherwise try it: the open-closed argument is available
and the connected parameter exists (`j`, or a continuous interpolation of the data), but the set
where the smallness holds is open-and-closed only in a ball whose radius already carries the `n^{-2}`.

**(R4) A weaker smallness that suffices — and this one is available.** (α)'s sufficient condition is
a **norm** bound on `∇𝔉`. The consumer does not need a norm bound. By Proposition COF-res the defect
is `n²Σ_X D(c_X)Φ_k(Y^p_0)(c_X)` with **`Σ_X D(c_X) = 0`** (BFT_B.md l.4114, *"supported on the
level-`k` roots, total 0"*), and `|Φ_k| ≤ CC_0(1 + R)^{-2}` decays in the fine distance `R`
(YSUP.md l.232-234, Theorem YS-CORE (iii)). **So what is needed is a dipole-level
neutrality of the root charges against a `(1+R)^{-2}` profile — not smallness of `∇𝔉` in any norm.**
That is strictly weaker, it is finite-dimensional, and it is exactly the lane's named
`(TENT-Q)` / `(NEUT-box)` (BFT_B.md l.4124-4125; HANDOFF.md priority 5). *Status: PROVEN-HERE that
(R4)'s condition suffices in place of (α)'s; `(TENT-Q)` itself remains OPEN.*

### 6.6 GS5 verdict

**CIRCLE-PARTIAL.** Both pre-registered clauses fit — arrow (γ) **is** weaker than stated
(CIRCLE-BREAKS's clause) **and** the circle becomes an induction with a named residual gap
(CIRCLE-PARTIAL's). I record the **less flattering** of the two, CIRCLE-PARTIAL, because the residual
gap is real: the self-map property over the first `O(k)` steps is not established, (R3) does not
supply it, and (R2) replaces it by `(FP♯′)`, which is OPEN.

**Weakest arrow: (γ).** It is the only one of the three that is false as written, and it is false for
a quantifier reason (ball vs orbit), not a quantitative one. **(β) is the strongest** — it is an
identity, not an asymptotic. **(α) is sound but over-strong**: (R4) shows its sufficient condition is
not the consumer's necessary one.

---

## 7. FB-ONE-LEG, verified (target GS6). **ONE-LEG-HOLDS, and for a sharper reason than FACEB gives.**
## Written 21:56 UTC.

FACEB §3.3 states FB-ONE-LEG as *"two functionals of one argument `D(S)`"*, **ARGUED**, resting on
BFT_A §38.6/§38.8 and on an un-re-derived `σ ≈ 0.003`. Re-deriving the structural half from the two
primary identities gives something stronger.

- **Lemma RC's identity** (BFT_A.md l.3545-3547, **PROVEN-HERE** there):
  `f^♯_0[S](p) − f^E_0[S](p) = n²⟨D(S), σ(Π_EY^p)⟩`.
  Its first line (BFT_A.md l.3538) records **`σ(y) vanishes at the level-k roots`**, so this pairing
  **sees only the non-level-`k` roots**.
- **Proposition COF-res** (BFT_B.md l.4113-4116, **PROVEN-HERE** there): the extra term is
  `n²⟨D^root(S), h^{(0→k)}Y^p_{*,0}⟩ = n²Σ_X D(S)(c_X)Φ_k(Y^p_{*,0})(c_X)`, with `D(S) = D^root(S)`
  **supported on the level-`k` roots**.

> **Proposition GS-ONELEG (PROVEN-HERE as an implication of the two quoted identities; the SIZES
> remain ARGUED in their files).** The two `L^{2k−3}` defects are not two mechanisms sharing a leg.
> They are **one pairing `n²⟨D(S), Ψ^p⟩` split by root level**, with
>
>   `Ψ^p(Z) := σ(Π_EY^p)(Z)` at non-level-`k` roots, `Ψ^p(c_X) := Φ_k(Y^p_{*,0})(c_X)` at level-`k`
>   roots,
>
> the split being **forced**, not chosen: `σ ∈ Λ_*` vanishes at the level-`k` roots by construction
> (BFT_A.md l.3538), so the two supports are complementary and the decomposition is exhaustive. In
> particular **both vanish identically when `D(S) = 0`**, both are linear in `D(S)`, and both carry
> the same `n²`.

**FB-ONE-LEG HOLDS**, upgraded from ARGUED to PROVEN **for its structural claim**; the *sizes*
(`σ ≈ 0.003` measured; `≍ L^{2k−3}` reach) stay ARGUED exactly where BFT_A and BFT_B leave them, and
I did not re-derive them (§1.5.1). **GS-F6 does not occur** in its refuting form; it occurs in the
strengthening form the failure mode anticipated — BFT_B itself already says the two reach
`L^{2k−3}` *"by the same mechanism"* (BFT_B.md l.4122).

**One class mismatch, flagged (it is not a symbol collision, but it is adjacent to defect 1).**
BFT_B §35.7 quantifies over **Setting LIN^cc** sources, for which `D(S) = D^root(S)` lives **only**
at the level-`k` roots (BFT_B.md l.4114) — for that class the `σ`-term is identically zero and there
is literally **one** term. BFT_A §38.6's *Reading* quantifies over a general non-composite-co-closed
row `R`, for which `D(R)(Z)` is carried at roots of **every** level (BFT_A.md l.3549-3552). **The two
files are describing the same pairing over two different source classes.** A reader combining them
without noticing will double-count. *Recorded for BFT_A's and BFT_B's owners in §9.*

> **Consequence, and it is the reason this target should not have been split.** Items GS2-GS3 (the
> sign/`G_e` question), GS4-GS5 (the `(NC-Γ)` circularity) and the `Γ_E` defect are **one problem**,
> and the single object is `D(S)`:
> - `D(S) = −K'^T_x∇(𝔉_k∘exp)(x)` (Lemma CD) — `D` is the whole defect;
> - `D(S) ≡ 0` at `x = 0` by definition of `K'` (Proposition GS-BASE) — the induction has a base;
> - `D(S) ≡ 0` at every step under (R2)'s projection — the induction has a route;
> - and `G_e` never enters any of it, because at `r = ∞` there is no `G_e` (Proposition GS-ZERO).
>
> **The `D(S)` leg is the target; `Φ_k` and `G_e` are not.** That agrees with FACEB's own §10 item 1
> and strengthens it.

---

## 8. Check record `gs1`, with a per-clause statement of discriminating power. Written 21:58 UTC.

Script `checks/gs1_pc.py`, output `checks/gs1_out.txt`, stderr `checks/gs1_err.txt` (empty).
Exact integer arithmetic, plain python, no numpy, no BLAS, **no machine-wide numeric lock taken**;
runtime under 2 s; `seed = 20261028`, `N = 7`, `d = 4`, 12 trials.

| clause | result | what it could have shown instead |
|---|---|---|
| **A1** `d*(𝒫e) = e` exactly, `supp 𝒫e` inside the cube | **PASS** 12/12 | that my implementation of Lemma PC is not Lemma PC, or that Lemma PC's support claim fails in `d = 4`. A6a shows the clause can fail. |
| **A2** every component of a co-closed compactly supported `e` sums to 0 (Lemma GS-ZS) | **PASS** 12/12 | a nonzero component sum, refuting GS-ZS. A6a produced component sums `[1,0,0,0]`, so the clause discriminates. |
| **A3** `Σ_z G_{μν} = Σ_z z_μe_ν` and `M` antisymmetric (Lemma GS-FM) | **PASS** 12/12 | a mismatch, refuting GS-FM. A6b and A6c both produced mismatches. |
| **A4** the signed totals are the same for two different primitives | **PASS** 12/12, **non-vacuous** (the reversed-axis primitive differs pointwise) | equality holding only because the two primitives coincided — the clause reports VACUOUS in that case, and it did not. |
| **A5** sign coherence of `𝒫e` | **0 / 12 coherent → SIGN-MIXED**; and `e = d*δ_q` gives `𝒫e = δ_q`, a single `+1`, **coherent** | the opposite: 12/12 coherent would have recorded SIGN-COHERENT-GENERIC. One counterexample settles it, and there were twelve. |
| **A6 designed-FAIL control** | **FIRED on all three clauses** — A6a (non-co-closed input: exactness FALSE, sums `[1,0,0,0]`), A6b (wrong primitive: totals ≠ moments), A6c (`M̃` not antisymmetric) | had any of the three passed, `gs1` would carry **no control** and A1-A3 would not be evidence. |

**What `gs1` does NOT test, stated plainly.** It does not touch `Q_str^{(0→k)}`, `𝔽^{(0→k)}`, `ω^p`,
`χ`, `Φ_k`, `Y^p`, `Z″`, the contraction, or the actual current `e = d*G' − (Q_str^{(0→k)})^TJ`.
Every claim in §3.1, §3.2, §4, §5, §6 and §7 is a **derivation from quoted statements**, not a
numeric result. `gs1` supports exactly three of them — Lemma GS-ZS, Lemma GS-FM, and Remark
GS-CUM's two-sided sign finding — and nothing else. A reader must not read its PASSes any wider.

**Post-hoc arithmetic, labelled.** §4.1's table of `[A(1−2ε) − B]/(1−ε)` at `ε = ½, ¼, 1/100, 0` and
§4.2's three thresholds were computed in exact `Fraction` arithmetic **after** `gs1` ran and were
**not** pre-registered. They are arithmetic on quoted constants (`1738C_j`, `3476C_j`, `6952C_j` from
BFT_A.md l.2344-2346) and on §4.1's two-line algebra; they are not a gate and carry no control.

**No FAIL to report in `gs1`.** One route is reported as FAILED in the mathematics: **(R3), the
graded ball** (§6.5), which reproduces the `η ≤ η_0L^{-2k}` it was meant to avoid.

---

## 9. Outcome

### 9.1 Outcome table

| object | status | content |
|---|---|---|
| **`G_e` identified, with its free parameter** (§2) | **PROVEN-HERE** (reading of quoted statements) | `G_e = 𝒫e`, `e = d*G' − (Q_str^{(0→k)})^TJ`, `G' = χh_p − [Δ_0,χ]ω^p`; `𝒫` is a signed one-sided cumulative sum (BFT_A.md l.1879). It is a **one-parameter family in `r`**, while `Y^p` does not depend on `r`. **GS-F1 does not occur** |
| **Proposition GS-ZERO** (§3.1) | **PROVEN-HERE** | at `χ ≡ 1` (`r = ∞`, admitted by Lemma LD at every `k, T`), `d*G' = 0`, so `J = 0`, `e = 0`, **`G_e ≡ 0`** and the residual sources vanish: `Y^p ≡ g^♮ + Z″` exactly. **The sign statement FACEB names as missing is available in the strongest form there is.** BFT_A writes the same collapse at l.3570-3573 (*"No bootstrap"*) |
| **The `½` is a threshold, not a size** (§3.2) | **PROVEN-HERE** as a reading of BFT_A.md l.2344-2346 vs l.3568 | `Σ|G_e| ≤ 1738C_jL^{-c}`, `c` free. **GS-F2 occurs** — defect 2 of the session-25 brief, exactly |
| **Lemma GS-ZS** (§3.3) | **PROVEN-HERE**; `gs1` A2 PASS, control fired | each component of a compactly supported co-closed 1-form sums to zero, so **`e` is provably sign-incoherent**. FACEB's lead (*"the funnel coefficients are already sign-coherent"*) is about a different object and **does not transfer** |
| **Lemma GS-FM** (§3.3) | **PROVEN-HERE**; `gs1` A3, A4 PASS (A4 non-vacuous), controls fired | `Σ_z G_{μν} = Σ_z z_μe_ν`, antisymmetric: **the signed total `Σ_q G_e(q)` is an invariant of `e`, not an artefact of Lemma PC's axial gauge** |
| **Lemma GS-MOM** (§3.3) | **PROVEN-HERE** | `M(d*G') = M(d*δ_p)` = the unit in `p`'s plane, exactly, for every `χ`. The second term `M((Q_str^{(0→k)})^TJ)` is **not computed** (out of scope) — the one piece of GS2 (ii) left OPEN |
| **Remark GS-CUM** (§3.3) | **PROVEN-HERE** (construction) + `gs1` A5 | sign coherence of `𝒫e` ⟺ the partial sums of `e` are one-signed along each axial line, and it is axis-order dependent. `gs1`: **0/12** generic, but `e = d*δ_q` **is** coherent — so **no general no-go and no general theorem**. **GS-F3 occurs in its strong form** |
| **GS2 verdict** | **SIGN-MOOT** primary; **SIGN-MIXED** subsidiary | the kernel can be taken `≡ 0`; where it is not, `e` is sign-mixed and `𝒫e`'s coherence is `e`- and axis-dependent |
| **Proposition GS-WINDOW** (§4.1) | **PROVEN-HERE, elementary** | `|Φ_k(Y^p)| ≥ [A(1−2ε) − B]/(1−ε)`: the bootstrap admits a cancellation of **`2ε` as a fraction of `A`**, not of `A`. FB-BOOT's *"no lower bound at all"* is the value of this at the single degenerate point `ε = ½` |
| **the cancellation, quantified** (§4.2) | **COMPUTED** (exact; post-hoc, on quoted constants) | ≤ `3476C_jL^{-c}` of `A`; 100 % at `L^c = 3476C_j`, 50 % at `6952C_j`, 1 % at `347600C_j` (**5 extra powers of `L` at `L = 3`**, and `T ≥ 2.78·10⁶C_j`), **0 % at `r = ∞`, free** |
| **Corollary GS-SHARP** (§4.3) | **CONDITIONAL** on **(GS-A)** (`A` is `k`-free; ARGUED-and-measured in BFT_A, l.3583) and **(GS-B)** (`Φ_k` bounded on the `inv`-ball; supported by BFT_A.md l.3607-3608, **not written**) | at `r = ∞`, `|Φ_k(Y^p_{*,0})| ≥ A − B ≥ A/2` for `k ≥ k_0`. **Face (b)'s `n²` is SHARP for the actual response**, with an **unsized** `k`-threshold. **GS3 verdict NEITHER, pointing SHARP** |
| **Clause (FB-CIRC)** (§5.2) | **STATED** with full quantifiers, merging BFT_A.md l.2595-2598 and l.3612-3613 | three arrows (α) response ⟸ gradient, (β) gradient ⟸ steps, (γ) steps ⟸ response, each quantified over configurations, orbit index, `k` and `T` |
| **Proposition GS-BASE** (§6.1) | **PROVEN-HERE given (GI)**; independent of the ARGUED `|K'_xξ| ≤ C|x||ξ|` | `K'_0 = 0` **by definition** (BFT_A.md l.2761), so `D(N_B + 𝔑^0(0;B)) = 0` exactly: the first step's source is composite-co-closed and Theorem COF applies **unconditionally**. **The base step is free** |
| **Lemma GS-STEP** (§6.2) | **PROVEN-HERE** | `∇𝔉(x_{j+1}) = 𝔑^0(x_j) − 𝔑^0(x_{j+1}) − Γ_E^TΓ_Ex_{j+1}`, exactly, at every step. **Arrow (β) is an identity, not an asymptotic** |
| **Proposition GS-NOCIRC** (§6.3) | **PROVEN-HERE** as an implication | Clause (FB-CIRC) is **not circular**: arrow (γ) quantifies over the ball where its consumer needs only the orbit, and the orbit is anchored where the hypothesis is free. **GS-F5 occurs on arrow (γ)** |
| **Proposition GS-TRANSIENT** (§6.4) | **ARGUED** (uses `‖K'_x‖ ≤ C‖x‖_𝔐`, ARGUED at BFT_A.md l.2984) | what is left is the **first `J ≈ 2k·log L/log(1/θ)` steps** — `O(k)` steps of a geometric iteration, not `L^{2k}` of contraction. FACEB's step count is right; its reading of the cost is not |
| **(R1) slice-preserving solve** (§6.5) | **PROVEN** as a reduction | removes `Γ_E^TΓ_Ex_j` from Lemma GS-STEP identically; does not close the transient alone |
| **(R2) iterate the composite-co-closed projection** (§6.5) | reduction **PROVEN-HERE given Theorem COF**; `(FP♯′)` **OPEN** | kills `D` at **every** step, so Theorem COF's `k`-, `T`-, `Γ`-uniform `Cη²` holds throughout and the transient disappears. The cost is one finite-dimensional statement: **one scalar per level-`k` box**, with `Σ_X Q_X = 0` already. **This is l.3613's real content** |
| **(R3) graded ball** (§6.5) | **FAILED, reported** | reproduces `η ≤ η_0L^{-2k}`. The open-closed shape is available and buys nothing |
| **(R4) a weaker smallness that suffices** (§6.5) | sufficiency **PROVEN-HERE**; `(TENT-Q)` **OPEN** | the consumer needs **dipole neutrality of the level-`k` root charges against a `(1+R)^{-2}` profile**, not a norm bound on `∇𝔉`. Strictly weaker, finite-dimensional, and already named as `(TENT-Q)`/`(NEUT-box)` |
| **GS5 verdict** | **CIRCLE-PARTIAL** | the circle does **not** close; arrow **(γ)** is the weakest and is false as stated; the residual gap is the self-map property over `O(k)` steps |
| **Proposition GS-ONELEG** (§7) | **PROVEN-HERE** for the structural claim (sizes stay ARGUED in their files) | the two `L^{2k−3}` defects are **one pairing `n²⟨D(S), Ψ^p⟩` split by root level**, the split forced by `σ ∈ Λ_*` vanishing at the level-`k` roots. **ONE-LEG-HOLDS**, upgraded from FACEB's ARGUED. **GS-F6 does not occur** |
| **the `g_0` / `u` correction** (§2.2) | **PROVEN-HERE** | §38.7's `g_0` is `d*(χω^p)` / `y^p`, **not** YSUP's `⅛d*δ_p` (the claim is YSUP.md l.229-230's own, repeated by FACEB §4.2); `g_0 = 8Δ_0^{-1}u` at `r = ∞`. FB-CLASS unaffected; `A` must be carried as a symbol. **GS-F4 occurs, as expected, changing no conclusion** |

### 9.2 Net on the open accounting

**Nothing is added to or removed from the open set.** `(TENT-osc)`, `(TENT-Q)`, `(NC-Γ)` and
`(PW-ℓ¹)` all stay exactly as their files leave them. What changes is **which object the lane should
be attacking**, and the removal of one named missing input that was never missing.

### 9.3 The single biggest thing this changes

**The item FACEB flags as *"below it, and much cheaper"* — a sign statement on `G_e` — is not an open
item.** It is discharged by Proposition GS-ZERO at a parameter value BFT_A already uses, and the
inequality it was supposed to rescue (`|Φ_k(Y^p)| ≥ A − B`) follows with no cancellation at all. The
sharpness of face (b)'s `n²` for the actual response therefore reduces to **(GS-A) + (GS-B)**, two
one-line statements about `Φ_k(y^p)` and `Φ_k` on the `inv`-ball, neither of which is about the
bootstrap.

**And the item FACEB flags as the real obstruction is not circular.** Arrow (γ) is false as stated,
the base step is free by a definition, and the remaining content of BFT_A.md l.3613 is **(R2)**: a
projected iteration plus `(FP♯′)`, whose cost is one scalar per level-`k` box. That is the same
finite-dimensional object as `(TENT-Q)`/`(NEUT-box)`, which HANDOFF.md already carries at priority 5.
**So face (b), the `Γ_E` defect, l.3613's parenthetical and `(TENT-Q)` are one item, and the single
leg is `D(S)`.**

---

## 10. FOR OTHER FILES (not edited)

**To the lead.**
1. **T55-O's cheap half is discharged, and it was never a sign question.** Proposition GS-ZERO: take
   `χ ≡ 1` in Lemma LD and `G_e ≡ 0`. The `½` at BFT_A.md l.3568 is U4′'s threshold, not U4′'s size
   (`1738C_jL^{-c}`, l.2345) — **defect 2 of the session-25 brief, in a file written today**.
2. **T55-O's structural half is not a circularity.** `K'_0 = 0` **by definition** (BFT_A.md l.2761),
   so the contraction's first step meets a composite-co-closed source and Theorem COF applies with
   no `(NC-Γ)`. Clause (FB-CIRC) §5.2 and Proposition GS-NOCIRC §6.3. What is left is an `O(k)`-step
   transient and `(FP♯′)`.
3. **BFT_A.md l.2595-2598 and l.3612-3613 are the same proposal** in two parentheticals, one in
   §28.12 and one in §38.8. They should be merged into one named target when l.3613 is promoted.
4. **One thing I did against the brief's steer, per D6.** The brief framed item 1 as *"establish the
   sign structure of `G_e(q)`"* and said the funnel coefficients' sign coherence is *"a lead worth
   following"*. I followed it far enough to **refute** it (Lemma GS-ZS: `e` is provably
   sign-incoherent; and the funnel coefficients are a different object), and then stopped computing
   signs, because the parameter that makes `G_e` zero is already in the lemma. I report this rather
   than deliver a sign table nobody needs.
5. **Two assumptions of mine a reviewer should break first.** (i) That Lemma EX's degradation at
   `r = ∞` (shell count `≈ k + log_L T`, BFT_A.md l.1928-1930) affects only the *upper* bound on
   `Φ_k(g^♮)` and not the lower bound FB-BOOT wants — §3.1. If that is wrong, Proposition GS-ZERO
   still holds but §4.3 loses its `T`-uniformity. (ii) `Lip(𝔑^0; 𝔅_η) ≤ C_Nη` in §6.4, which I did
   not verify; it is the ordinary statement that `𝔑^0` is the quadratic-and-higher part, but it is
   not written as a lemma anywhere I looked.

**To BFT_A.md's owner (lane A).**
- **l.3568 should read `Σ_q|G_e(q)| ≤ 1738C_jL^{-c} ≤ ½` and name `c`**, or §38.7's reader will take
  `½` for the kernel's size, as FACEB did. The same applies to l.2272 and l.3094.
- **Case A / Case B is a choice about Theorem Y's constants, not about the decomposition.** l.3573's
  *"No bootstrap"* holds at `r = ∞` for **every** `T`, and l.3613's consumer does not need Theorem
  Y's constants. Worth one sentence at l.3556.
- **l.1713 and l.1904's *"`G' = 0` for `r = ∞`"* is literally false** — at `χ ≡ 1`,
  `G' = χh_p = h_p ≠ 0`. What holds is `d*G' = 0` (and `⟨G', dZ_0⟩ = 0`), which is all any use needs
  and is what makes `e = 0`. One-word fix, but a reader who checks it will think Lemma LD is wrong.
- **l.2761's `K_0 = −Ξ`, `K'_x := K_x − K_0` is load-bearing** far beyond its remark: it gives
  `K'_0 = 0` exactly and with Lemma CD makes the contraction's first source composite-co-closed. It
  deserves to be stated as a corollary of Lemma CD rather than left in a definition.
- **§38.6's *Reading* and BFT_B §35.7 quantify over different source classes** (general
  non-composite-co-closed rows, `D` at all root levels, vs Setting LIN^cc, `D` at level-`k` roots
  only). A reader combining them will double-count. §7 here.

**To BFT_B.md's owner (lane B).**
- §35.7's Proposition COF-res and BFT_A's Lemma RC are **one pairing split by root level**, the split
  forced by `σ ∈ Λ_*`. Your l.4122 already says *"by the same mechanism"*; §7 here proves the
  structural half. If you carry it, carry it as `n²⟨D(S), Ψ^p⟩` with `Ψ^p` defined piecewise.

**To FACEB.md's owner (T55-G).**
- **§4.3, §9.3 and §10's second bullet to YSUP should be withdrawn or restated.** *"A sign or
  positivity statement on `G_e(q)` is exactly and only what is missing"* is not right: at `r = ∞`
  there is no `G_e`, and at finite `r` the admissible cancellation is `2ε ≤ 3476C_jL^{-c}` of `A`,
  not `A`. Proposition FB-BOOT's algebra is correct; it is evaluated at `ε = ½`, which is U4′'s
  threshold and not U4′'s bound.
- **§4.2's *"the very field BFT_A §38.7 takes as `g_0`"* is wrong** (§2.2 here) — though the
  sentence is YSUP.md l.229-230's, not yours. FB-CLASS is
  unaffected; the identification of `A` with `2.4768·10⁻³` is not.
- **§6.4's reading of the cost is too pessimistic.** *"`2k·log_L` of contraction"* is a count of
  **steps** of a geometric iteration, which a Banach argument supplies for free; the cost is the
  self-map property over those steps, which is a different and smaller thing.
- **§3.3's FB-ONE-LEG is right, and provable** — see §7.

**To YSUP.md's owner.**
- The `Z″₀`-cancellation attack point is **not** a sign question. At `r = ∞` the decomposition is
  `Y^p ≡ g^♮ + Z″` with no bootstrap term, and what is needed is `B < A`, i.e. (GS-A) + (GS-B) of
  §4.3. (GS-B) is one line from BFT_A.md l.3571-3572 plus l.3607-3608 and is worth writing.
- **l.229-230's *"the very field BFT_A §38.7 takes as `g_0`"* is an erratum** — §38.7's `g_0` is
  `d*(χω^p)` (l.3557) or `y^p` (l.3570), and `g_0 = 8Δ_0^{-1}u` at `r = ∞`. Theorem YS-CORE (ii)'s
  exact `−65/26244` is unaffected; what is affected is the step that reads it off as a bound for the
  **response**, which is the step FACEB §4.3 found conditional.
- Note that **`Φ_k` is being evaluated on two different fields** in the two files: `⅛d*δ_p` (yours,
  exact, `−65/26244`) and `d*(χω^p)` / `y^p` (BFT_A's, measured, `−0.0022`). They differ by
  `8Δ_0^{-1}`.

**To PROOF.md's owner.** Nothing here moves the tally. If `(TENT-Q)` is carried, it should be
carried **with** l.3613's `(FP♯′)` and `(NEUT-box)`: §7 and §6.5 (R2)/(R4) say they are one
finite-dimensional item — one scalar per level-`k` box, already of total zero.

---

## 11. Discipline

**Order and times.** §1 PRE-STATED (statements only; no constant from this session), **first edit of
this file, 2026-10-28T21:46:35Z** → `checks/gs1_criteria.md` **21:52Z**, with pre-registered PASS/FAIL
verdicts, a designed-FAIL control and an explicit statement of what the check cannot test, and **no
constant derived in this session** → `checks/gs1_pc.py` → `checks/gs1_out.txt` (ALL PASS;
`gs1_err.txt` empty) → §2 onwards, 21:53-21:58Z. Exact integer / `Fraction` arithmetic in plain
python; **no numpy, no BLAS, no machine-wide numeric lock taken**; runtime under 2 s. **No git
command was run.**

**Disclosure, made in §1.1 before any derivation.** I read BFT_A §21-§23, §27, §28.12, §31.1,
§33.3-§33.5, §38.6-§38.9 and BFT_B §35.6-§35.8 **before** writing the PRE-STATED section, and formed
three suspicions during that reading. Every target and failure mode bearing on them is marked
**(c)** and carries **no pre-registration weight** (GS-F2, GS-F3, GS-F5, and parts of GS3 and GS5).
This is the lane's own convention (BFT_A §21.3).

**Statuses.** No claim in this file is marked PROVEN-HERE unless its proof is written out above from
hypotheses that are quoted with a `file:line`. **CONDITIONAL claims name their input**: Corollary
GS-SHARP names (GS-A) and (GS-B); Proposition GS-TRANSIENT is ARGUED and names the ARGUED input it
uses. **One route is reported FAILED** ((R3), §6.5). The designed-FAIL control **FIRED on all three
clauses**. Two pieces are reported **OPEN and not attempted**: `M((Q_str^{(0→k)})^TJ)` (§3.3) and
`(FP♯′)` (§6.5).

**Re-derivation rather than citation, per the session-25 rule.** The load-bearing steps I take from
FACEB are *not* taken from FACEB: Proposition FB-BOOT's algebra is rebuilt in §4.1 with the
coefficient free; FB-ONE-LEG is rebuilt in §7 from Lemma RC and Proposition COF-res directly; and
FB-NBHD's circularity is rebuilt in §5.2 from Lemma CD, `Φ_E`'s definition and `𝓛_E` directly. Three
of FACEB's statements are corrected here (§2.2, §4.1-§4.3, §6.4) and one is confirmed and
strengthened (§7).

**What a hostile reviewer should attack first, in this order.**
1. **§3.1 / Proposition GS-ZERO** — whether `r = ∞` is genuinely admissible *at the point of use*
   in §38.7, as opposed to admissible in Lemma LD. I claim it is, because `Y^p` does not depend on
   `r` and FB-BOOT is a statement about `Y^p`; if §38.7's consumer secretly needs Theorem Y's
   `r = L^{k+c}` constants in the same breath, my §4.3 weakens (but Proposition GS-ZERO survives).
2. **§6.1 / Proposition GS-BASE** — whether the contraction may be started at `x_0 = 0`. If the lane
   starts it elsewhere (at the free solution, say), the base step is free only if `K'` is small
   there, which is a bound and not a definition.
3. **§6.4 / Proposition GS-TRANSIENT** — the `Lip(𝔑^0) ≤ C_Nη` input, and whether `θ` is bounded
   away from 1 uniformly in `k`. If `θ → 1` with `k`, the step count `J` is not `O(k)`.
4. **§7 / Proposition GS-ONELEG** — whether `σ(Π_EY^p)` and `Φ_k(Y^p_{*,0})` really are the
   restrictions of one function, or whether the two files' `D(S)` differ by more than their source
   class.
