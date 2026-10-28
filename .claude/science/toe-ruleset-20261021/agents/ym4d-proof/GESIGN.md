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
operator applied to one explicit current, both produced inside **Lemma LD** (BFT_A.md l.1713-1718,
proof §23.3 at l.1897-1917):

> *"With `J := 𝔽^{(0→k)}d*G'` and `e := d*G' − (Q_str^{(0→k)})^TJ`, one has `Z = Z' + Σ_qG_e(q)Y^q`,
> where `G_e := 𝒫e` (Lemma PC), and `Z'` minimises `E_src` with data `β` and the residual-type
> sources `s_i := (Q^{(i+1→k)})^TJ`."* (BFT_A.md l.1716-1718)

The three ingredients, each pinned:

1. **`𝒫`, the operator** — Lemma PC, BFT_A.md l.1708-1711, proof at l.1873-1892. It is a **signed
   one-sided cumulative sum along the first axis**, iterated down in dimension:
   `G_{aν} := −S_ν + 1[z_a ≥ b]W_ν` with `S_ν(z) := Σ_{t≤z_a}e_ν(t, z')` and
   `W_ν(z') := Σ_t e_ν(t, z')` (l.1879), plus a transverse `(d−1)`-dimensional copy of itself on the
   single slice `z_a = b` (l.1882). It satisfies `d*G = e` exactly and `Σ|G| ≤ 3qΣ|e|` on a cube of
   side `q`.
2. **`e`, the current** — `e := d*G' − (Q_str^{(0→k)})^TJ`, co-closed (BFT_A.md l.1911-1913) and
   supported in a cube of side `q ≤ 2.05r` about `p` (BFT_A.md l.2345, l.2601).
3. **`G'`, the source of `e`** — `G' := χh_p − [Δ_0, χ]ω^p` with `χ := Φ_{r,p}` a product cutoff at
   radius `r`, `ω^p := Δ_0^{-1}(δ_p − h_p)`, and `h_p` the **constant** 2-form of `p`'s orientation
   with total sum 1 (BFT_A.md l.1694-1695, l.1713-1714).

### 2.2 The free parameter, which is the whole story (defect 2: *"check what someone fixed once"*)

Lemma LD is stated for **every** `χ = Φ_{r,p}` with `1 ≤ r ≤ M/4`, **and for `χ :≡ 1`** ("`r = ∞`"):
BFT_A.md l.1713, *"Let `χ := Φ_{r,p}` with `1 ≤ r ≤ M/4`, or `χ :≡ 1` ("`r = ∞`")"*. So `G_e` is not
one object but a **one-parameter family** `G_e^{(r)}`, while the object it decomposes, `Y^p`, does
not depend on `r` at all (`Y^p` is defined at BFT_A.md l.1691-1693 as a minimiser of `E_src` with the
single source `δ_q`, with no `r` in sight).

Theorem Y picks `r := L^{k+c}` when `T ≥ 8L^c` and `r := ∞` otherwise (BFT_A.md l.1868-1869,
dated precision 2), and `c` is then fixed by **`L^c ≥ max(260, 3476C_j)`** ([RBA5-fix] U4′,
BFT_A.md l.2344-2346). **That choice is made for Theorem Y's constants, not for the bootstrap**, and
nothing downstream of §38.7 re-examines it.

**GS-F1 does not occur:** one construction (`𝒫e`), several bounds on it. No symbol collision: the
`G_e` of l.1716, l.1915, l.2345, l.2601, l.3093 and l.3568 are the same object, and `G'`, `G_e` and
`𝒫` are distinct symbols throughout.

**One correction to FACEB, which changes none of its conclusions.** FACEB §4.2 calls YSUP's witness
`u = ⅛d*δ_p` *"the very field BFT_A §38.7 takes as `g_0`"*. It is not. §38.7's `g_0` is
`d*(χω^p)` in Case A (BFT_A.md l.3557) and `y^p = d*ω^p` in Case B (BFT_A.md l.3576) — a lattice
**Green's-function dipole**, not a four-link field; `g_0 = Δ_0^{-1}(d*δ_p) = 8Δ_0^{-1}u` at `r = ∞`,
since `d*h_p = 0`. Both fields lie in FACEB's class `𝒴` (co-closed, profile `(1+|z−p|)^{-3}`;
`|g_0| ≤ C_0'(1+|z−p|)^{-3}` at BFT_A.md l.3557, `|y^p| ≤ C_K(…)^{-3}` at l.3576), so **Proposition
FB-CLASS is unaffected**. What is affected is the identification of `A := |Φ_k(g^♮_0)|` with YSUP's
`2.4768·10⁻³`: BFT_A itself marks that identification **ARGUED** and supports it by a *measurement*,
`a = −0.0022` at `k = 2, T = 2` (BFT_A.md l.3588-3590), against the witness's exact `−0.0024768`.
**GS-F4 occurs, as expected, and changes no conclusion** — but `A` must be carried as a symbol with
an ARGUED numerical value, not as YSUP's exact rational. I carry it as a symbol (scope limit §1.5.2).

---

## 3. The sign structure of `G_e`, computed (target GS2)

### 3.1 First: the kernel can be taken **identically zero**. **PROVEN-HERE.**

> **Proposition GS-ZERO (PROVEN-HERE, from Lemma LD's own hypotheses).** Take `χ ≡ 1` (`r = ∞`) in
> Lemma LD, which Lemma LD admits for every `k ≥ 1` and every `T ≥ 1` (BFT_A.md l.1713). Then
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
`G'` through `−⟨G', dZ_0⟩` (BFT_A.md l.1906), which equals `−⟨d*G', Z_0⟩ = 0`. ∎

This is **not new mathematics**: it is BFT_A's own Case B, which states the same collapse in the same
words — *"`Y^p ≡ g + Z` with `g_0 = y^p` … **No bootstrap.**"* (BFT_A.md l.3576-3579). What is new is
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
> *Proof.* `d*G' = d*δ_p − d*dg_0 = d*δ_p − Δg_0` (BFT_A.md l.1901-1903, `g_0` co-closed). `g_0` has
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
`C_K` and `C_φ`, both uncomputed — BFT_A.md l.2328-2330. Per §1.5.4 I quote it and do not size it, so
the second and third columns are conditional on `C_j`, and the `r = ∞` row is not.)*

### 4.3 What the question becomes. **Verdict NEITHER, pointing toward SHARP.**

At `r = ∞` the inequality is `|Φ_k(Y^p_{*,0})| ≥ A − B` with

- `A = |Φ_k(g^♮_0)|`, `g_0 = y^p = d*ω^p` — the lattice Green's-function dipole;
- `B = sup|Φ_k(Z″_0)|`, `Z″` the **source-free** minimiser with data `β_str = −Q_str^{(0→k)}y^p`.

So the missing input is **not a sign statement and not about `G_e`**: it is the two-sided comparison
`B < A`, i.e. *does the terminal-data response `Z″` beat the explicit dipole at the level-`k` roots?*
Two named pieces, both outside my scope but both well-posed:

> **(GS-A) `A` is `k`-free and positive.** BFT_A measures `a = −0.0022` at `k = 2, T = 2`, offset
> `(1,0,0,0)` and marks the identification **ARGUED** (BFT_A.md l.3588-3590); YSUP proves the exact
> `k`-free `−65/26244 = −2.4768·10⁻³` for the four-link witness `u`, which is a **different field**
> (§2.2). **OPEN for `g_0`; ARGUED-and-measured.**
>
> **(GS-B) `B = O(n^{-2})`.** BFT_A's own Case B bound is
> `‖Z_str‖_{inv,m'} ≤ G_D(m')‖β_str‖_{D,m'}` with `‖β_str‖_{D,m'} ≤ C_βe^{128m'L^c}n^{-2}`
> (BFT_A.md l.3577-3578) — i.e. `Z″` is small **by `n^{-2}`**. What is missing is one line: that `Φ_k`
> is a bounded functional on the `inv`-ball with a `k`-uniform constant. BFT_A's own scaling supports
> it — `φ_{i+1}(x_0) ≍ L²·(level-i gradient) ≍ L^{2(i+1)}η/n²`, so `Φ_k(x_0) ≍ L^{2k}η/n² = η ≍
> ‖∇^cx^c_0‖_∞` (BFT_A.md l.3615-3617) — but it is **not written**. **CONDITIONAL on that line.**

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
  `Φ_k(Y^p_{*,0})` at the level-`k` roots (Proposition COF-res, BFT_B.md l.4110-4116). See §7.
- `𝔅_η := {x : ‖x‖_𝔐 ≤ η}`; `η_0` is SPD's radius (BFT_A.md l.2807).
- `C_SR` — Proposition SR's constant (BFT_A.md l.2806-2810), `k`-, `T`-uniform.

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
