# FACEB.md — target T55-G: face (b)'s n², the escape or the no-go, and its price

*Owner: the T55-G worker (session 25). Writes only this file and `checks/fb1_*`. Append-only.*

## 1. PRE-STATED — statements only. THIS IS THE FIRST EDIT OF THIS FILE, written 2026-10-28T21:17:09Z,
## before any derivation, any script and any arithmetic of this session.

Nothing below is claimed. Every item is a target or a named way of failing. No constant appearing here
was produced in this session; each is quoted from a prior file with its file:line, and each such quote
is to be **re-derived** before it is used (HANDOFF's fourth systemic defect: a banked review is evidence,
not a certificate).

### 1.0 The objects, as cited (quoted inputs, not re-judged here)

- **(TENT-osc)** — TENTQ.md l.381, l.522, YSUP.md l.30: there is `C_osc < ∞` independent of `k, T, p` and
  of the coarse cell with `n²·osc_𝔅(Φ_k(Y^p_{*,0})) ≤ C_osc`. This is **face (b)** of Theorem NCE (ii)
  (TENTQ.md l.544).
- **The residue it bounds** — BFT_B.md l.3976, l.4114 (Proposition COF-res): the single term of `f_0` not
  covered by Theorem COF is `n²⟨D^root(S), h^{(0→k)}Y^p_{*,0}⟩ = n²Σ_X D(S)(c_X)·Φ_k(Y^p_{*,0})(c_X)`.
- **The explicit n²** — BFT_B.md l.4130 (Remark MASSLESS): `f_0 = n²dΔ_0^{-1}J_0`, `n = L^k`.
- **The estimate** — TENTQ.md l.277 (Corollary TQ-osc): `|𝒯_p(S)| ≤ 128·n²·osc_𝔅(Φ_k)·Σ_lπ_l(S_l)`,
  `128 = 2^d·2d` absolute.
- **The verdict session 24 left** — YSUP.md l.260-262 (Theorem YS-DEC (a)): (TENT-osc) is FALSE by exactly
  `n² = L^{2k}`, PROVEN as an implication, **CONDITIONAL on the profile input**; YSUP.md l.219-229
  (Theorem YS-CORE (ii)): the exact witness `u := ⅛d*δ_p` gives `Φ_k(u)(c_X) = −65/26244` for every
  `k ≥ 2`, the series terminating at `i = 2`.
- **The representative route, closed** — TGAUGE_PRICE.md l.230-258 (Theorem TG-PRICE, Corollary TG-NULL):
  `ρ = 1` exactly for every `μ ∈ Λ_0`; the gauge is a null operation; TGAUGE_PRICE.md l.573: face (b) has
  **no representative-theoretic escape at all**.
- **The consumer** — BFT_A.md l.2809 (Proposition SR) and l.2812 (Target (NC-E)).
- **A second quantity of the same size in the same response** — BFT_A.md l.3547-3552 (§38.6 *Reading*) and
  l.3597-3601 (§38.8 *Reading for (NC-Γ)*).
- **The reference ceiling for pricing** — `DX′ = 2.456·10⁻¹⁵²/C_Ω`, REVIEW_SF_S7.md l.203 (DX′-1 (iii));
  margin convention `margin = log₁₀(item ceiling) − log₁₀(DX′)`, ARS_FIX.md l.267-271.

### 1.1 Targets (written before any derivation)

- **FB1 (identify, by file:line, before anything else).** State (a) **what face (b) is**; (b) **which `n`**
  it carries (`n = L^k`? `n_i = L^i`? the torus `T`?) and **which quantity the square sits on**; (c) what
  the **consumer** needs in place of `n²` — `O(1)`, `O(log n)`, `O(n)`, or `n²` absorbable. Defect 1 of the
  session addendum applies in full: this lane has 4 `ε_*`, 2 `θ_0`, 5 `ε_1`, 3 `η_1`, and three multi-decade
  errors came from exactly this, so every symbol I compare is to be pinned to a file:line in my own text.
- **FB2 (sharpness).** Decide whether the `n²` is **attained** or is an artefact of the estimate. Either
  exhibit an instance achieving it up to constants, or show the estimate is lossy. An artefact is the single
  most valuable outcome available here.
- **FB3 (escapes that are NOT representative-theoretic).** The representation-theory route is closed
  (TGAUGE_PRICE) and is **not** re-walked. Try, in this order, and report each as tried-and-failed or
  tried-and-worked: (i) a cancellation from `d∘d = 0` (Bianchi) or from one-leg differentiation; (ii) a
  **divergence-form** rewriting; (iii) the **twisted-Koszul** complex; (iv) **summation by parts** on the
  lattice; (v) **`d = 4` marginality** — if the `n²` is an artefact of treating a marginal term as relevant,
  that is the answer.
- **FB4 (price, if it stands).** Give the decade cost against `DX′`, state whether it breaks a ceiling or
  eats margin, and **name the exchange rate used** (`η ↔ g_0²`? `η ↔ ε_1`?) rather than assume one.
- **FB5 (the no-go gets the same scrutiny as a theorem).** If the conclusion is that no escape exists,
  reframe it as a positive claim and test whether it survives. A no-go that only says "we could not find
  one" is to be reported as that and not as a no-go.
- **FB6 (check discipline).** Any gate run gets `checks/fb1_criteria.md` first, with pre-registered PASS/FAIL
  and no constant derived in this session, and a **designed-FAIL control** whose failure is reported.

### 1.2 PRE-REGISTERED VERDICTS (written before any script and before any derivation)

| verdict | the condition for it | what it means |
|---|---|---|
| **ARTEFACT** | some route listed in FB3 reduces the power of `n` in a **k-uniform** way, i.e. replaces `n²·osc_𝔅(Φ_k)` by a quantity that is `O(1)` (or `O(log n)`) on the same inputs | face (b) is not an obstruction; I report the route, the new statement, and its scope |
| **SHARP-AND-FATAL** | the `n²` is attained on an input the lane's own hypotheses admit, **and** the consumer needs `O(1)` with no mechanism to absorb a `k`-growing constant | face (b) stands; I price it and name what must change instead |
| **SHARP-AND-ABSORBABLE** | the `n²` is attained **but** the consumer's own budget tolerates it (a `k`-growing constant is admissible there, or the factor multiplying it is itself `O(n^{-2})` for a reason the lane already has) | the highest-value outcome short of ARTEFACT; I state the absorbing mechanism and its file:line |
| **MISIDENTIFIED** | the `n` carrying the square is not the one the files say, or the square is on a different quantity | a defect-1 finding; I stop and report it rather than price the wrong object |
| **NOT-DECIDED** | none of the above is reached | reported as that, with what was ruled out |

### 1.3 Pre-registered failure modes, with expectations

- **FB-F1** The `n²` is sharp and no listed escape touches it. *Expected to occur for the `Φ_k` leg.*
- **FB-F2** An escape works but only at a scope the obstruction does not live at (e.g. a nontrivial
  background, or `d ≠ 4`). *Expected for the twisted-Koszul route, which is trivial at the trivial
  background where the `n²` is measured.* Reported as a void escape, not a working one.
- **FB-F3** The lower bound is for the **witness** `u = ⅛d*δ_p`, not for the response `Y^p_{*,0}`, so a
  sharpness claim about `Y^p` is CONDITIONAL on the profile input. *Expected to occur.* If it does, the
  honest unconditional statement is about which **routes** are closed, not about the truth of (TENT-osc).
- **FB-F4** Face (b) is **not the binding item**: another quantity of the same size sits in the same
  response, so removing the `n²` changes nothing downstream. *If this occurs it reorders T55-G's value and
  must be said loudly.*
- **FB-F5** The price cannot be stated in decades at all, because the requirement is **uniformity in `k`**
  and the deficit is exponential in `k`, so there is no exchange rate to `DX′`. *If this occurs, any decade
  figure I give is a courtesy figure and must be labelled one.*
- **FB-F6** My own gate cannot decide — a tautology, a gate built from its object's own primitives, or a
  clause passing vacuously (defect 3). Controls are pre-registered in `checks/fb1_criteria.md` for exactly
  this.

### 1.4 Scope limits accepted in advance

`m = 0`, trivial background, `d = 4`, `L = 3`, abelian/linearised, the elliptic slice `S_E` (lead decision
D1). Nothing here will be claimed at `θ > 0`, at `m > 0`, at a nontrivial background, or about the factor
`k` of Theorem NCE (i), which is upstream (TENTQ.md l.579). No numeric job will be started under the
machine-wide lock; exact rational/integer arithmetic only.

### 1.5 Process commitments

PRE-STATED (this section) → `checks/fb1_criteria.md` → script → results → outcome, in that order, with the
times logged. Every failed check reported as a failure with the output kept. Every claim labelled
PROVEN / ARGUED / CONDITIONAL / GAP / OPEN. If I get nowhere I will say so.

---

## 2. Face (b), the `n`, and the quantity the square sits on (target FB1 (a),(b)).
## Appended after §1 (21:17:09Z) and after `checks/fb1_criteria.md` (21:20:47Z); written 21:24 UTC.

### 2.1 What face (b) is

Off the critical set of `𝔉_k`, Theorem NCE (ii) splits into two faces (TENTQ.md l.543-545): face (a) is
**(P0-sup)**, the Hölder half's need for a pointwise bound on `Γ_E^T D(S)`; **face (b) is (TENT-osc)**.

Face (b) is one scalar inequality, on the **response field alone** (TENTQ.md l.381-384):

> there is `C_osc < ∞`, independent of `k`, `T`, `p` and of the coarse cell `𝔅`, with
> **`n²·osc_𝔅(Φ_k(Y^p_{*,0})) ≤ C_osc`.**

It is what is left of **(TENT-Q)** after TENTQ eliminated the box charges (Theorem TQ-INT, TENTQ.md
l.253-259) and the oscillation (Lemma TENT-TV / Corollary TQ-osc, TENTQ.md l.276-294). The quantity it
controls is **Proposition COF-res's residue** (BFT_B.md l.4114-4116):

  **`𝒯_p(S) = n²⟨D^root(S), h^{(0→k)}Y^p_{*,0}⟩ = n²Σ_X D(S)(c_X)·Φ_k(Y^p_{*,0})(c_X)`** ,

the level-`k` root charges of the source paired against the **composite axial funnel of the response**,
`Φ_k = h^{(0→k)} = Σ_{i<k} ev^{(i+1→k)} h_i Q_str^{(0→i)}` (Proposition RF, quoted at BFT_B.md l.4118).
Corollary TQ-osc (TENTQ.md l.289-294) turns that into `|𝒯_p(S)| ≤ 128·n²·osc_𝔅(Φ_k)·Σ_lπ_l(S_l)` with
`128 = 2^d·2d` absolute.

### 2.2 Which `n`, and which quantity carries the square — pinned by file:line (defect 1)

This lane has four `ε_*`, two `θ_0`, five `ε_1` and three `η_1`, and three multi-decade errors came from
comparing the wrong one (session-25 addendum, defect 1). The same discipline applied here:

| symbol | which one, by file:line | value |
|---|---|---|
| **`n`** | `n = L^k`, the **total** fine-to-coarse scale ratio. BFT_B.md l.4130 (Remark MASSLESS) writes the object as `f_0 = n²dΔ_0^{-1}J_0` on "the level-0 torus of side `Tn`"; YSUP.md l.159-168 states the normalisation and says the only `L`-powers in the functional are "the explicit `n² = L^{2k}` of `𝒯_p` and the own→coarse conversion `‖v^c‖_∞ = n·sup_own|v|`" | `L^k`, `L = 3` |
| **not** `n_i = L^i` | the per-level block side, YSUP.md l.178-180. It appears inside `Φ_k`'s level-`i` term and is **summed over**, not squared | — |
| **not** `T` | the coarse torus side. `T` enters only through Remark MASSLESS's rejected route (BFT_B.md l.4130) and is absent from `𝒯_p` | — |
| **the squared quantity** | the square sits on **neither leg**: it is an **explicit prefactor** of the functional `f_0`, i.e. the fine→coarse **unit conversion** of a curvature (`n` per index of a 2-form). It is not an estimate and nothing in the derivation produced it | `n² = L^{2k}` |
| **the quantity that fails to supply `n^{-2}`** | `osc_𝔅(Φ_k(Y^p_{*,0}))`, the oscillation over one coarse cell of the composite funnel **of the response**, measured in **own** units (YSUP.md l.159-168: `Φ_k(v)/sup_own|v|` is dimensionless and carries no `k`) | wanted `O(n^{-2})`, is `Θ(1)` |

> **FB1 (b), stated: the `n²` is `L^{2k}` and it is an explicit prefactor, not a bound. What is being
> asked to decay is `Φ_k(Y^p_{*,0})` in own units, and in own units `Φ_k` is dimensionless and carries no
> `k` at all** (YSUP.md l.159-168, verified there by the exact outside identity
> `Φ_k(dδ_{c_X})(c_X) = L^{-dk} − 1`, ys1 A5). **So face (b) is the demand that a `k`-free dimensionless
> number be `≤ L^{-2k}`.** Pre-registered verdict **MISIDENTIFIED does not occur**: the files have the
> `n` and the quantity right.

That restatement is worth having, because it settles the shape of the question before any attack: the
`n²` cannot be reduced by sharpening an estimate — there is no estimate in it — and it cannot be reduced
by a change of units, because `Φ_k` is already unit-free. **Only a cancellation inside `Φ_k`, or a
compensating smallness in `D(S)`, can pay it.** §5 and §6 are those two leads.

---

## 3. What the consumer actually needs (target FB1 (c)). **It needs `O(1)`, and it needs it `k`-uniformly.**

The brief's own warning applies: *a proof that an `n²` is fatal is worth nothing if the consumer can
absorb `n²`*. So the consumer was looked up before anything was attacked.

### 3.1 The consumer, quoted

- **BFT_A.md l.2808-2811, Proposition SR:** *"For the rows `(R^B_0 + R^W_0, R^B_1, …, R^B_{k-1})` of a
  configuration with `‖x‖_𝔐 ≤ η ≤ η_0` (SPD's `η_0`), the Γ_E-response obeys **`‖f_0‖_∞ ≤ C_SR η²`,
  uniformly in `k, T`**."*
- **BFT_A.md l.2812, Target (NC-E):** *"(NC-Γ) for `Γ_E`, i.e. **`‖x(S^E_0(V))‖_inv ≤ Cη²` uniformly in
  `k, T`**."*
- **BFT_B.md l.3974, Theorem COF:** `‖f_0‖_∞ + [f_0]^∞_α ≤ C_fun(…)` with **"`C_fun` independent of
  `k, T`"**.

So the budget is a **`k`-uniform constant**, and the residue is one term of the same `‖f_0‖_∞`.

### 3.2 The three answers the brief asked me to distinguish

- **`O(1)`?** Yes. `O(n)` and `O(n log n)` are both outside the budget, because `n = L^k` and every
  statement above is quantified "uniformly in `k`". Even `O(log n) = O(k)` is outside **this** budget,
  although the lane separately carries a factor `k` upstream (TENTQ.md l.555-559, REVIEW_BFT_B_S9_S10's
  RS10-1) — which is a different, additive defect and is **not** a licence here.
- **Is `n²` absorbable?** **No, and for a reason sharper than "the constant must be `k`-uniform":**
  **both sides of `‖f_0‖_∞ ≤ C_SR η²` are homogeneous of degree 2 in `η`.** The residue's size is
  `≍ n²·L^{-3}·η²` (BFT_B.md l.4122; BFT_A.md l.3549-3552 independently). So **lowering `η` does not buy
  a single decade against this defect**: it scales both sides identically. This is the opposite of the
  situation in the ARS_FIX / EPS1_SWEEP lane, where margins move with `ε_1`.
- **Is there any mechanism that could absorb it?** Exactly one in the files, and it is not on the `Φ_k`
  leg: the residue is **linear in `D(S)`**, and **Lemma CD** (BFT_A.md l.2973-2979) identifies that leg
  exactly: `Ξ^T𝔑^0 = −K'^T_x∇(𝔉_k∘exp)`, so the root charge is **proportional to the gradient of the RG
  functional** and vanishes identically at critical points. §6 prices that route.

> **FB1 (c), stated.** The consumer needs the residue to be **`O(1)·η²` with a `k`-uniform constant**.
> It can absorb **nothing**: not `n²`, not `n`, not `log n`. And because the inequality is homogeneous of
> degree 2 in `η`, the deficit **cannot be bought with decades of `η`** — the only exchange rate into a
> smallness condition runs through the contraction's self-map condition, and §6 computes it.

### 3.3 >>> A finding that reorders the value of this target: **face (b) is not the binding item.**
### Pre-registered failure mode **FB-F4 OCCURS.**

The same `L^{2k-3}` appears **twice** in the same `Γ_E`-response, from **two different mechanisms**, and
face (b) is only one of them. BFT_A.md l.3597-3601 (§38.8, *Reading for (NC-Γ) and Proposition SR*):

> *"the `Γ_E`-response to a non-composite-co-closed row differs from a top-anchored response by
> `n²Σ_Z D(R)(Z)σ(Z)` **plus the tent term**."*

- **the tent term** is face (b): `D(S)` at the **level-`k`** roots against `Φ_k(Y^p_{*,0})`, reaching
  `≍ L^{2k-3}η²` (BFT_B.md l.4122);
- **`n²Σ_Z D(R)(Z)σ(Z)`** is the **slice-spike** term: `D(R)` at roots of **every** level `l(Z)` against
  `σ ≈ 0.003`, reaching `≍ L^{3l(Z)-k}η²`, i.e. **`L^{2k-3}η²` at `l(Z) = k−1`** (BFT_A.md l.3549-3552).
  **Lead decision D1 has already accepted these spikes as real.**

They are different objects at different roots, and **removing face (b)'s `n²` entirely would leave
`(NC-Γ)` for `Γ_E` failing by `L^{2k-3}` from the second term alone.** Checked for a defect-1 collision
and it is not one: the two live at different root levels (`k` vs `k−1`), are paired against different
functions (`Φ_k` vs `σ`), and are listed as separate summands in the same sentence of §38.8.

**But they share a leg.** Both are `n²⟨D(S), ·⟩`: **linear in the composite divergence `D(S)`, and both
vanish identically when `D(S) = 0`.** Hence:

> **Proposition FB-ONE-LEG (ARGUED; the inputs are quoted, not re-derived).** The two `L^{2k-3}` defects
> of the `Γ_E`-response off the critical set are **two functionals of one argument**, `D(S)`. No work on
> `Φ_k` can close `(NC-Γ)` for `Γ_E`, because the `σ`-spike term is untouched by it; and any mechanism
> that controls `D(S)` closes **both at once**. *Status ARGUED and not PROVEN: it rests on §38.6/§38.8,
> which are themselves ARGUED there, and I have not re-derived the `σ ≈ 0.003` measurement.*

This is the single most consequential thing in this file, and it is a **negative** about the value of
T55-G as scoped: **face (b) is necessary-but-not-sufficient, and it is not the cheapest of the two.**

---

## 4. Sharpness (target FB2). The `n²` is **not an artefact of the estimate**; and its sharpness
## **for the actual response is OPEN**, with the hole named and quantified.

Two different questions hide under "is the `n²` sharp", and session 24's files answer only the first.

### 4.1 There is no estimate to sharpen. **PROVEN-HERE (from quoted identities).**

The chain from `f_0` to face (b) contains exactly one inequality, and at the core it is an equality up to
a bounded factor:

1. `𝒯_p(S) = n²Σ_X D(S)(c_X)Φ_k(Y^p_{*,0})(c_X)` is an **identity** (Proposition COF-res, BFT_B.md
   l.4114-4120, PROVEN-HERE there; re-derived independently as `M = P + 𝒯` in TGAUGE_PRICE.md l.230-253
   and checked exactly in tg1b B1 (iii) by a disjoint code path).
2. `𝒯_p(S) = n²Σ_l⟨d(ev^{(0→l)}I_χΦ), S_l⟩` is an **identity** (Theorem TQ-INT, TENTQ.md l.263-274).
3. The only inequality is Lemma TENT-TV / Corollary TQ-osc (TENTQ.md l.276-294), and it is **attained**:
   TGAUGE_PRICE.md l.310 records that the quintic tent **attains** Lemma TENT-TV exactly (the lemma
   itself is TENTQ.md l.276-287), and Lemma TG-TV (TGAUGE_PRICE.md l.286-298) proves the matching lower bound
   `‖d(A^{(0→l)}μ)‖_1 ≥ (n/L^l)^{d−1}osc_1(Φ)` for **every** admissible `μ` — *"exactly Lemma TENT-TV's
   upper bound divided by `2d`"*.
4. For a source in one coarse cell only the `≤ 2^d` boxes of that cell carry charge, so the sum in (1) is
   finite and the worst box dominates: Theorem YS-CORE (iii) (YSUP.md l.234-236) gives
   `|Φ_k| ≤ C·C_0(1+R)^{-2}` with `R` the **fine** `ℓ^∞` distance, so one coarse step away `Φ_k` is
   already `O(C_0n^{-2})` and cannot cancel the `Θ(C_0)` at the box whose root is adjacent to `p`.

> **Corollary FB-NOEST (PROVEN-HERE as an implication of the four quoted items).** At the core cell,
> `|𝒯_p(S)| = n²·|Φ_k(Y^p_{*,0})(c_{X_p})|·|Q_{X_p}|·(1 + O(n^{-2}))`. **There is no slack in the
> estimate: at most the absolute factor `2d = 8` of Lemma TG-TV separates the bound from the object.**
> Pre-registered verdict **ARTEFACT is therefore unreachable through the estimator**, and the search must
> be for a cancellation inside `Φ_k` or a smallness in `D(S)`.

### 4.2 The witness, and what it does and does not establish

YSUP.md l.229-233 (Theorem YS-CORE (ii)) gives the exact instance: `u := ⅛d*δ_p` with `p` the
`(0,1)`-plaquette at `c_X + (1,0,0,0)` — **co-closed, admissible with `C_0 = 1` (equality at distance 1),
and the very field BFT_A §38.7 takes as `g_0`** — for which the funnel series **terminates**
(`φ_3 = φ_4 = φ_5 = 0` exactly) and

  **`Φ_k(u)(c_X) = −65/26244 = −2.4768·10⁻³` for EVERY `k ≥ 2`, exactly.**

Two structural facts about this witness, verified here rather than quoted (`checks/fb1_bianchi.py`,
clause A4, ALL PASS; see §7):

- `u` is **co-closed** (`δu = 0`) and `du ≠ 0`: it is **purely co-exact**, carrying only curvature;
- its support is exactly **4 links with coefficients `±1`** before the `1/8`, and `1/8 = 1/(2d)` at
  `d = 4` — consistent with the profile normalisation `(1+1)^{-3} = 1/8` that YSUP.md l.229 records.

> **Proposition FB-CLASS (PROVEN-HERE, and UNCONDITIONAL — this is the honest unconditional form of
> YSUP's verdict).** Let `𝒴` be the class of level-0 fields that the lane's own hypotheses on
> `Y^p_{*,0}` admit at the point where Corollary TQ-osc is applied: co-closed, with
> `|v(b)| ≤ C_0(1+|b−p|_∞)^{-3}` (BFT_A.md l.3556-3557, the `g_0` clause of Theorem PW-E). Then
> `u ∈ 𝒴` with `C_0 = 1`, and therefore
>
>   **`sup_{v∈𝒴} n²·osc_𝔅(Φ_k(v)) ≥ 2.4768·10⁻³·n²` for every `k ≥ 2`.**
>
> **Consequence: no proof of (TENT-osc) can run through the profile bound and co-closedness alone.** Any
> proof must use a property that distinguishes the actual `Y^p_{*,0}` **inside** `𝒴`. *This is
> unconditional — it needs no claim about `Y^p` at all — and it is strictly weaker than "(TENT-osc) is
> false", which is what YSUP states and which remains CONDITIONAL.*

### 4.3 >>> The sharpness for the **actual response** is OPEN, and the lane's own decomposition cannot
### close it. Pre-registered failure mode **FB-F3 OCCURS**, with a quantified reason.

YSUP.md l.252-254 reads its lower bound off as
`0.00248·C_0 ≤ max_X|Φ_k(Y^p_{*,0})(c_X)|` — substituting the response for the witness. The substitution
is where the conditionality lives, and the lane's only vehicle for it is BFT_A.md l.3556-3568 (Theorem
PW-E, Case A):

  **`Y^p ≡ g^♮ + Z'' + Σ_q G_e(q)Y^q`**, with `Σ_q|G_e(q)| ≤ ½` (U4′, BFT_A.md l.3568).

Write `A := |Φ_k(g^♮_0)|`, `B := sup|Φ_k(Z''_0)|`, `M := sup_p|Φ_k(Y^p_{*,0})|`. `Φ_k` is linear, so:

- **upper:** `M ≤ A + B + ½M`, hence **`M ≤ 2(A+B) = Θ(C_0)`** — a *proof* that `Φ_k(Y^p)` is `O(1)`,
  which is `n²` too big for face (b), so **the decomposition cannot prove (TENT-osc) either**;
- **lower:** `|Φ_k(Y^p)| ≥ A − B − ½M ≥ A − B − (A+B) = −2B`, i.e. **nothing**. The bootstrap coefficient
  bound `Σ_q|G_e(q)| ≤ ½` permits a cancellation of up to half the sup, and half the sup is, by the upper
  bound, as large as `A + B` — enough to cancel `A` entirely.

> **Proposition FB-BOOT (PROVEN-HERE, elementary).** From BFT_A §38.7's decomposition together with
> `Σ_q|G_e(q)| ≤ ½` **no lower bound on `|Φ_k(Y^p_{*,0})|` follows**, in either direction: the same two
> lines give `M ≤ 2(A+B)` and give no positive lower bound at all. **The sharpness of face (b)'s `n²` for
> the actual response is therefore OPEN**, and it is open for a reason that is not a technicality: the
> bootstrap is an absolute-value bound and the question is a **sign** question.
>
> **What would close it, named and cheap:** a **sign or positivity statement on the bootstrap kernel**
> `G_e(q)` — e.g. `G_e(q) ≥ 0`, or any statement forcing `Σ_q G_e(q)Φ_k(Y^q)` to carry the same sign as
> `Φ_k(g^♮)`. The funnel coefficients themselves are known to be sign-coherent (REVIEW_BFT_A_S8 S8-7:
> `φ_1 = −1/432`, `φ_2 = −17/104976`, ratio `17/243`, **same sign**, rebuilt as YSUP ys1 A1), so the
> missing half is only `G_e`. **This is exactly the `Z″₀`-cancellation attack point YSUP flagged to lane
> A (SESSION24_RESULTS.md l.1813-1816), now with the mechanism and the missing input named.**

*One consistency point checked and cleared, recorded because it is the kind of thing that hides.* The
named representative's level-0 field is `g^♮_0 = g_0 + dψ̃` with `ψ̃` **any** level-0 extension of
`ψ := h^{(0→k)}g_0` (BFT_A.md l.3558-3562), whereas YSUP evaluates `Φ_k` on `g_0`. By Proposition TGAUGE
(TENTQ.md l.321-331) `Φ_k(g^♮_0) = A^{(0→k)}ψ̃`, not `ψ`. The two agree for the natural (block-constant)
extension, and the difference between any two admissible extensions vanishes at the level-`k` roots,
i.e. lies in `Λ_*` — so it is **exactly** the freedom Theorem TG-PRICE prices as a null operation
(TGAUGE_PRICE.md l.230-253). **No defect; YSUP's number is the right number for the natural extension,
and the extension freedom is already spent.**

---

## 5. The escapes that are not representative-theoretic (target FB3). Five tried; **all five fail, and
## four of them fail by the SAME identity.** Written after `checks/fb1_bianchi.py` (ALL PASS, §7).

The representation-theory route is closed (TGAUGE_PRICE.md l.573) and is not re-walked here. The brief's
five alternatives were taken in order.

### 5.0 The unifying identity: `d∘d = 0`

Three of the five routes — Bianchi/one-leg differentiation, divergence-form rewriting, and summation by
parts — are the **same** lattice identity applied at different places, and the fourth (twisted Koszul) is
its homotopy. Stating that first saves re-deriving three failures:

> **Lemma FB-DD (PROVEN-HERE; `checks/fb1_bianchi.py` A1-A3, exact integer arithmetic on `Z_4^4`,
> ALL PASS, designed-FAIL control A6 FIRED).** On the level-`l` lattice, with `δ` the transpose of `d`:
> **(a)** `d∘d = 0` on 0-forms; **(b)** an **exact** 1-form and a **co-exact** 1-form are orthogonal:
> `⟨dφ, δW⟩ = ⟨ddφ, W⟩ = 0`; **(c)** a co-exact 1-form is co-closed: `δ(δW) = 0`.

### 5.1 Bianchi / one-leg differentiation. **FAILS — and the failure is exact, not a failed search.**

The hope (lead decision D3): the mechanism that takes `K_p` from 2.27 to `~0.12` on **closed** inputs —
the `d = 4` cubic vertex being marginal only after one leg is differentiated (PROOF.md l.6205-6240) —
should also deflate `𝒯_p`. Applied here it has two possible legs, and **both are already spent**:

- **The source leg.** `D(S)` is itself a divergence (`d*C(j) = D(S)`, Lemma DF-cc (i), quoted at
  TGAUGE_PRICE.md l.39 and l.252), so one-leg differentiation moves `d` onto the funnel. That move **is** Theorem
  TQ-INT (TENTQ.md l.263-274): `𝒯_p(S) = n²Σ_l⟨d(ev^{(0→l)}I_χΦ), S_l⟩`. It has already been made, and
  Lemma TG-TV (TGAUGE_PRICE.md l.286-298) proves the result **cannot be improved by more than `2d = 8`**.
  By Lemma FB-DD (b), any source slot that is itself in divergence form contributes **exactly zero** to
  `𝒯_p` — which is the correct and complete statement of the Bianchi cancellation on this leg, and it is
  equivalent to the already-known fact that `𝒯_p` depends on `S` only through `D(S)`. **No new gain.**
- **The response leg — and this is the sharp point.** Differentiating `Y^p_{*,0}` would reach `Φ_k`
  through `Φ_k∘d = A^{(0→k)} − ev` (Proposition TGAUGE, TENTQ.md l.321-331), i.e. it would only expose
  the **exact part** of the response. **But the witness that attains the `n²` has no exact part at all:**
  `u = ⅛d*δ_p` is purely co-exact (`δu = 0`, `du ≠ 0`, `⟨dμ, u⟩ = 0` for every `μ` — fb1 A3, A4, exact).
  So the Bianchi/derivative mechanism acts on a component of `Y^p_{*,0}` that carries **none** of the
  obstruction.

> **Proposition FB-BIANCHI (PROVEN-HERE).** One-leg differentiation annihilates exactly the exact part of
> the response leg and exactly the divergence-form part of the source leg. The `n²`-attaining witness is
> **orthogonal to the first** and `D(S)` is **entirely inside the second**. Therefore the Bianchi route
> **cannot** reduce the `n²`: it is already fully applied, and what it would remove is not what is there.
> *This is the same identity that makes Theorem TG-PRICE a null operation, and it explains **why** that
> theorem came out `ρ = 1` exactly rather than approximately.*

### 5.2 A divergence-form rewriting. **FAILS, because it is already performed on the only leg where it
### is available, and on the other leg it is literally the gauge.**

The `𝔐` norm's `Y` leg is in divergence form for exactly this reason, so the move was tried on both legs.

- **Source leg: already done.** `𝒯_p` depends on `S` only through `D(S) = Σ_l ev^{(0→l)T}d^*S_l` —
  a sum of divergences, by construction. Lemma FB-DD (b) says the divergence-form part of each slot is
  invisible. There is nothing further to rewrite.
- **Response leg: not available.** `Φ_k` is an **anti-derivative**, the Koszul primitive of the response:
  `Φ_k∘d = A^{(0→k)} − ev`. Putting `Φ_k(Y^p_{*,0})` into divergence form means writing it as (something)
  applied to `dY^p_{*,0}` or `δY^p_{*,0}` — i.e. choosing a **potential** for the response. That choice
  **is** the composite gauge `μ ∈ Λ_0` of Proposition TGAUGE, and Theorem TG-PRICE prices it at `ρ = 1`
  exactly, a null operation (TGAUGE_PRICE.md l.230-253). **So this route is the representative-theoretic
  route in different words, and it is closed by a theorem, not by a failed search.**

### 5.3 The twisted-Koszul complex. **VOID AT THIS SCOPE — pre-registered failure mode FB-F2 OCCURS.**

`h_i` **is** a Koszul homotopy: the axial line integral, satisfying `h_i(dν) = A_iν − ev^{(i+1)}ν`
(TENTQ.md l.334-335), which is the contracting-homotopy formula with the root evaluation as the residual
projector. The **twisted** complex is the one in which the line integral is parallel-transported along
the background connection. Two reasons it is not an escape here:

1. **The `n²` is measured at the trivial background** (`m = 0`, trivial background, abelian/linearised —
   TENTQ.md l.390, YSUP.md l.225-227, TGAUGE_PRICE.md l.447-452). **At the trivial background the twist
   is the identity**, so a twisted Koszul complex is the untwisted one and changes no number here.
2. A **different** homotopy (non-axial) would change `Φ_k`, but `Φ_k` is not an estimator — it is part of
   the definition of the composite blocking (`h_i` averages integrals along axial paths inside a
   level-`(i+1)` block, BFT_B §27.1, quoted at TENTQ.md l.306-309). Changing it changes the RG map, not
   the bound. That is a redesign of the scheme, not an escape from an estimate, and it is outside T55-G.

*Recorded as a void escape, not a working one, exactly as FB-F2 pre-registered.* The honest statement is
that the twisted complex belongs to **(N-bg)**, which is a different wall (lead decision D5).

### 5.4 Summation by parts on the lattice. **FAILS, with the remaining room PRICED at a factor 8.**

Summation by parts is what produces Theorem TQ-INT in the first place. What is left after it is the
freedom to choose the **level-0 extension** `Ψ` of the level-`k` root values of `Φ_k` — a discrete
least-gradient problem. It is settled, in both directions:

- **upper:** Lemma TENT-TV gives `‖d(ev^{(0→l)}Ψ)‖_1 ≤ 2d(n/L^l)^{d−1}Σ_X|Φ(c_X) − c|`, and the quintic
  tent **attains** it (TENTQ.md l.276-287, TGAUGE_PRICE.md l.310);
- **lower:** Lemma TG-TV gives `≥ (n/L^l)^{d−1}·osc_1(Φ)` for **every** admissible competitor, by a
  line-by-line flux argument (TGAUGE_PRICE.md l.286-294); Proposition TG-OPT computes the exact ratio
  `ρ_tv(l) = s(1 + L^{−l}n^{1−d}) → 1` — `657/656` and `1641/1640` at `d = 4, k = 2`, i.e. **0.15 %**.

> **The entire summation-by-parts route has at most the absolute factor `2d = 8` left in it, against a
> needed `L^{2k}`.** That is 0.90 decades against, at `k = 183`, 173.2 decades. **PRICED and CLOSED.**

### 5.5 `d = 4` marginality. **REAL, but it points the other way — and it cannot be the artefact.**

This was the most promising of the five, because `d = 4` marginality has surfaced in three unrelated
lanes (NORMS §N5's cubic vertex; PLD §19 route (ρ1); YSUP §2.2's line integral). It was tested and it
**does not** produce the `n²`.

1. **The marginality is real and is already correctly accounted.** YSUP.md l.186-215 (Theorem YS-AVG)
   does the count: an axial line integral averages `d−1 = 3` transverse directions and **sums** along the
   fourth, so its per-link weight is `n_i^{−(d−1)}` and its kernel `ℓ¹` mass is `n_i`, against a full
   block average's `n_i^{−d}` and `1`. Paired with the `|z|^{−3}` profile, `‖v‖_{ℓ¹(block)} ≍ 64n_i`,
   **linear and log-free because `d − 1 − 3 = 0` exactly at `d = 4`**. Result: `Θ(n_i^{−2})` per level,
   not `Θ(n_i^{−3})`.
2. **If a marginal term had been mis-treated as relevant, the signature would be a spurious `log`.**
   There is none: the count is **log-free** precisely because of the marginality, and YSUP's measured
   exponents converge to the marginal values (`−log_L(LImax_{i+1}/LImax_i) = 1.796, 1.901, 1.955 → 2`;
   `BA`: `2.728, 2.875, 2.945 → 3`, YSUP.md l.178-183). **Marginality is confirmed, not mis-treated.**
3. **>>> And the decisive point, which is where this route dies: the `n²` is not carried by any
   asymptotic level at all.** The funnel's value on the exact witness is dominated by its **`i = 0`**
   term — one block of side `L = 3`:

   `φ_1 = −1/54`, `φ_2 = −17/13122` (un-normalised), `φ_2/φ_1 = 17/243`, `φ_{i+1} = 0` for `i ≥ 2`
   exactly, so `Φ_k = φ_1 + φ_2 = −130/6561` with **`φ_1/Φ_k = 243/260 = 0.934615…` exactly**
   (YSUP.md l.229-233, l.211-213; the three fractions re-derived here post-hoc, §7.3).

   **93.46 % of the obstruction sits in a single `3⁴ = 81`-site block at the finest level, where no
   `d`-dimensional asymptotics operate.** A marginality argument is an argument about how a quantity
   scales as a block grows; the quantity here is a fixed rational number on a fixed 81-site block, the
   same for every `k ≥ 2`. **There is nothing for a marginality correction to act on.**

> **Proposition FB-LOCAL (PROVEN-HERE as an implication of the quoted exact rationals).** Face (b)'s `n²`
> is **not an accumulation over levels** and **not an asymptotic effect**: it is `L^{2k}` multiplying a
> `k`-independent rational that is 93.46 % determined by the `i = 0` term of the funnel, i.e. by the
> definition of `h_0` on one `3⁴` block. **Two consequences.** (i) It cannot be attacked level by level,
> and no per-level improvement — including a full extra power `n_i^{−3}` per level — changes it
> (YSUP.md l.277-281 reaches the same conclusion from the other side). (ii) Any fix must change `h_0`,
> which is part of the **definition of the composite blocking**, not part of an estimate. **The `n²` is
> in the scheme, not in the analysis.**

### 5.6 Summary of FB3

| escape | verdict | the reason, in one line |
|---|---|---|
| Bianchi / one-leg differentiation | **FAILS (PROVEN)** | fully applied on the source leg (= TQ-INT, optimal by TG-TV); on the response leg it removes only the exact part, and the witness is purely co-exact |
| divergence-form rewriting | **FAILS (PROVEN)** | already performed on the source leg; on the response leg it *is* the composite gauge, closed by TG-PRICE (`ρ = 1`) |
| twisted-Koszul complex | **VOID at this scope (FB-F2)** | the twist is the identity at the trivial background, where the `n²` is measured; a different homotopy redefines the RG map |
| summation by parts | **FAILS, PRICED** | the least-gradient extension problem is solved in both directions; at most `2d = 8` (0.90 decades) remains |
| `d = 4` marginality | **FAILS — real but inapplicable** | the marginality is confirmed and log-free; 93.46 % of the obstruction is a fixed rational on one `3⁴` block, where no asymptotics operate |

---

## 6. The price (target FB4). **Pre-registered failure mode FB-F5 OCCURS: there is no exchange rate.**
## Every decade figure below is a courtesy figure and is labelled one.

### 6.1 Why the honest answer is "this is not priceable in decades"

The consumer's inequality is `‖f_0‖_∞ ≤ C_SR η²` (BFT_A.md l.2809) and the residue is `≍ L^{2k-3}η²`
(BFT_B.md l.4122, BFT_A.md l.3551). **Both sides are homogeneous of degree 2 in `η`.** Lowering `η` —
the move that buys decades everywhere else in this lane — buys **exactly zero** here. The defect is a
`k`-dependence in a constant that is required to be `k`-uniform, and `L^{2k}` is exponential in `k`, so
**no fixed smallness condition repairs it for all `k`**.

> **It is therefore neither "breaking a ceiling" nor "eating margin".** It is a different kind of defect
> from the ones ARS_FIX and EPS1_SWEEP price, and reporting it in their currency without this paragraph
> would misrepresent it.

### 6.2 The one exchange rate that exists, and its assumption, stated before the numbers

The only route from a `k`-growing constant to a smallness condition is the contraction's **self-map**
condition: a map sending the ball `‖x‖_𝔐 ≤ η` into itself through a quadratic remainder bounded by `Cη²`
requires `Cη² ≤ η`, i.e. `η ≤ 1/C`. With `C = C_SR·L^{2k-3}` this gives

  **`η ≤ L^{3−2k}/C_SR`**, i.e. a cost of **`P(k) := (2k−3)·log₁₀L = (2k−3)·log₁₀3` decades of `η`**,

plus `log₁₀C_SR`, which is **not evaluated anywhere I have read** and is omitted below.

**TWO ASSUMPTIONS, both flagged, neither established in any file I read:**
- **(X1)** that the self-map reading above is the one this lane's contraction actually uses. BFT_A.md
  l.2812 states the target as `‖x(S^E_0(V))‖_inv ≤ Cη²` and does not write the self-map step.
- **(X2)** an identification of BFT's `η` (the `𝔐`-ball radius, BFT_A.md l.2809, `η_0` from Proposition
  SPD) with the quantity `DX′` and `ε_1` bound. **I found no file that states this identification.**
  Below, both candidate readings are reported and neither is adopted.

### 6.3 The courtesy figures (exact decimal, verified at 50 and 100 digits; fb1 A7 PASS, worst
### disagreement `2.08·10⁻⁴⁷`)

`P(k) = (2k−3)·log₁₀3`:

| `k` | `P(k)` (decades of `η`) |
|---|---|
| 10 | **8.111** |
| 42 | **38.647** |
| 160 | **151.247** |
| 183 | **173.195** |
| 183.4 | **173.577** |
| 355.6 | **337.897** |
| 356 | **338.279** |

Reference points, both quoted from prior files and not derived here:
- `DX′ = 2.456·10⁻¹⁵²/C_Ω` (REVIEW_SF_S7.md l.203, `C_Ω = 1`) → **151.610 decades**;
- `ε_1 = 6.7·10⁻⁴⁰` (RLARGE l.72, the headline value, quoted at ARS_FIX.md l.271) → **39.174 decades**.

Break-even level counts (the `k` at which the `n²` alone exhausts the whole budget):
- against `DX′`: **`k* = 160.380`**;
- against an `ε_1`-sized budget: **`k* = 42.552`**.

And the lane's own two quoted level counts, for comparison only (**the two are computed in different
bases in their source files — `log_3` for `n_♯`, `log_{81}` for `n_*` — which HANDOFF already flags as a
defect in RLARGE §5.4; they are listed here, not reconciled**):
- `≈ 183.4` (ARS_FIX's `n_♯` after the KN-step adoption; `355.6` before) → `P = 173.577`, i.e.
  **`+21.967` decades beyond `DX′`**;
- `≈ 42.0` (REVIEW_SF_S7's `n_*`) → `P = 38.647`, i.e. **`−0.527` decades**, just inside an `ε_1`-sized
  budget.

*The proximity of `k* = 42.552` to the quoted `42.0` is an arithmetic coincidence of two unrelated
quantities and is recorded as one. No mechanism connects them and none is claimed.*

**If `η` scales like `g_0` rather than `g_0²`, every figure in `g_0²` currency doubles** (`2P(k)`), and
the `DX′` break-even falls to `k* ≈ 81.7`. Both readings are reported because (X2) is open.

### 6.4 What the price actually buys, and what it does not

- **It does not buy a repair.** At any finite `k` the above says: pick `η` small enough and the self-map
  closes. At **every** `k` it says: `η` must shrink like `L^{−2k}`, which is not a smallness condition,
  it is the absence of one.
- **It does buy a statement about where the fixed point sits.** The residue is linear in `D(S)`, and
  Lemma CD (BFT_A.md l.2973-2979) gives `D(S) = −K'^T_x∇(𝔉_k∘exp)` with `K'_x = O(‖x‖)`. So:

> **Corollary FB-NBHD (ARGUED; CONDITIONAL on Lemma CD, which is PROVEN-HERE given (GI) at BFT_A.md
> l.2973, and on §38.6's charge sizing, which is ARGUED there).** `(NC-Γ)` for `Γ_E` holds, with its
> `k`-uniform constant, on the set
>
>   **`{ x : ‖x‖_𝔐 ≤ η and ‖∇(𝔉_k∘exp)(x)‖ ≲ C_SR L³ η n^{-2} }`** ,
>
> a neighbourhood of the critical set whose radius in the gradient is `n^{−2}` times the ball radius. The
> `n²` therefore costs **not decades of `η`, but `2k·log_L` of contraction**: it says the estimate is
> available only after the iteration has already reduced `‖∇(𝔉_k∘exp)‖` by `L^{2k}`. **This is circular
> as it stands** — the iteration needs the estimate to take the steps that produce the reduction — and
> that circularity, not the arithmetic, is the obstruction. It is exactly the route BFT_A.md l.3613 names
> and marks *"Not attempted"*: *"the contraction can be arranged so that its linear solve only meets
> composite-co-closed sources up to remainders multiplied by `∇(𝔉_k∘exp)`"*.

---

## 7. Check record, with a per-clause statement of discriminating power (written after §5-§6)

`checks/fb1_criteria.md` (21:20:47Z, no constant derived in this session) → `checks/fb1_bianchi.py` →
`checks/fb1_out.txt`, `checks/fb1_err.txt` (empty). Exact integer and exact `Decimal` arithmetic, plain
python, no numpy, no BLAS, **no machine-wide numeric lock taken** (session-25 brief rule 6). Runtime
under 2 s, memory a few MB. **No FAIL to report in this session**, and the designed-FAIL control fired.

| id | verdict | tested against | could it have failed? |
|---|---|---|---|
| **A1** `d(dφ) = 0` | **PASS** (0 nonzero components over 8 `φ`: 5 pseudo-random, 3 deltas) | nothing external — it is the complex's own identity | **MEDIUM-HIGH.** A wrong plaquette orientation, a wrong periodic wrap or a wrong `e_μ` offset each break it, and A6 shows a one-sign corruption does break it (6 nonzero). |
| **A2** `⟨dφ, δW⟩ = 0` | **PASS** (0 nonzero over 25 pairs) | a **different code path** from A1: `δ` is computed by transposing the *same* incidence lists, so a sign error in `d` cannot be cancelled by a matching one in `δ` | **MEDIUM-HIGH.** Broke in all 25 pairs under A6's corruption. |
| **A3** `⟨dμ, u⟩ = 0` on the **actual witness** `u = δ(1_p)` | **PASS** (0 nonzero over 10 `μ`) | YSUP.md l.229's witness, not a generic field | **MEDIUM.** Broke in 7 of 10 under A6. This is the clause that carries Proposition FB-BIANCHI. |
| **A4** non-vacuity of A3 | **PASS** — `u ≠ 0`; `δu = 0`; `du ≠ 0`; `|supp u| = 4` links with values `{−1, +1}` | defect 3's lens applied to my own gate: had `u` been `0`, A3 would pass vacuously and decide nothing | **HIGH as a guard.** It also **independently corroborates** YSUP.md l.229: 4 links of modulus 1, and the normalisation `1/8 = 1/(2d)` matches the profile value `(1+1)^{−3} = 1/8` at distance 1. |
| **A5** discriminating power of the pairing | **PASS** — `⟨dφ, j⟩ ≠ 0` in **5/5** pseudo-random pairs with a generic `j` | shows A2 is not a tautology about the inner product | **This clause exists only to show the gate can say "nonzero".** |
| **A6** **DESIGNED-FAIL CONTROL** | **CONTROL FIRED** — one incidence sign flipped (plaquette row 0, link 0, `+1 → −1`); **A1 fails (6 nonzero), A2 fails (25/25), A3 fails (7/10)** | — | **This is the control, and it is reported as having failed the clauses, as designed.** Without it A1-A3 would not be evidence. |
| **A7** price arithmetic | **PASS** — worst 50-vs-100-digit disagreement `2.081·10⁻⁴⁷` decades over 13 rows | two precisions of the same exact computation | **LOW as mathematics, MEDIUM as bookkeeping**: it guards a figure that will be quoted. |

### 7.1 What fb1 does NOT test, stated plainly

1. **No funnel is rebuilt.** `Φ_k`, `h_i`, `Q_str`, `φ_1`, `φ_2`, `ψ_u` are **quoted** from YSUP.md /
   TENTQ.md / REVIEW_BFT_A_S8 with file:line and **not** re-verified. Every claim of mine that uses a
   funnel value is CONDITIONAL on those files and is labelled so. Against the session's fourth systemic
   defect (*a banked review is evidence, not a certificate*), the load-bearing items I **did** re-derive
   are the ones my own propositions turn on — `d∘d = 0`, the orthogonality of the witness to exact forms,
   the witness's co-closedness and support — and the three funnel rationals' mutual consistency (§7.3).
2. **No response field is computed.** Nothing here is evidence about `Φ_k(Y^p_{*,0})`, which is exactly
   why §4.3 reports the sharpness for the response as OPEN rather than deciding it.
3. **Abelian, `m = 0`, trivial background, `d = 4`, `N = 4` periodic.** `Z_4^4` is large enough to
   separate the four directions and to wrap, and every clause is an identity that cannot depend on `N`;
   but it is a check on the cochain complex, not on the RG.
4. **Nothing here touches the factor `k`** of Theorem NCE (i) (TENTQ.md l.555-559), which is upstream.

### 7.2 One clause I considered and did NOT run, with the reason

A finite-torus solve for the lattice Green's function, to supply an unconditional `Θ(1)` lower bound on
the response's core independent of the profile input. **Not run**, for two reasons: it would need the
machine-wide lock for a rational linear solve, and — decisively — it would bound the **scalar**
Laplacian's Green function, whereas `Y^p_{*,0}` is the `1`-form response in the slice `S_E`, so the
result would not transfer. *Recorded because the gap it would have addressed is the one §4.3 leaves
open, and because an unconditional core lower bound remains the thing most worth having here.*
**Noted as an observation only, not a check:** for the scalar lattice Laplacian on `Z^d`,
`G(0) − G(e_μ) = 1/(2d)` exactly, by summing `ΔG = −δ_0` at the origin and using the `2d`-fold symmetry
— at `d = 4` that is `1/8`, the same `1/8` that normalises YSUP's witness. **This is a remark about a
different operator and is not evidence for the `1`-form problem.**

### 7.3 Post-hoc arithmetic (labelled post-hoc: run after seeing §5.5, not pre-registered)

Exact `Fraction` arithmetic, three lines: from `φ_1 = −1/54` and `φ_2 = −17/13122` (YSUP ys1 A1's listed
rationals), `φ_2/φ_1 = 17/243` ✓, `φ_1 + φ_2 = −130/6561`, `(φ_1+φ_2)/8 = −65/26244` ✓, `φ_1/8 = −1/432`
✓, `φ_2/8 = −17/104976` ✓, and `φ_1/Φ_k = 243/260 = 0.9346153846…` ✓, `|Φ_k|_unnormalised = 130/6561 =
0.019814052735863435` ✓ — reproducing YSUP.md l.284's `0.9346` and TENTQ.md l.365's calibration
`130/6561 = 0.019814` from the two `φ`'s alone. **Everything checks.**

**One normalisation inconsistency recorded, which changes no number.** YSUP.md l.249 lists "*all four of
`φ_1 = −1/54`, `φ_2 = −17/13122`, ratio `17/243`, `ψ_u = −65/26244` for the **unnormalised** `u`*". The
first two are indeed the un-normalised values; **`ψ_u = −65/26244` is the `⅛`-normalised one** (the
un-normalised total is `−130/6561 = 8 × 65/26244`). The list mixes the two normalisations. No downstream
figure is affected — YS-CORE (ii) states `−65/26244` for the normalised `u`, which is correct, and the
`0.019814` calibration is the un-normalised one, which is also correct — but a reader combining the four
as written gets `φ_1/ψ_u = 7.477 > 1`. *Erratum-level; flagged to YSUP's owner in §10.*

---

## 8. The no-go, reframed as a positive claim and tested (target FB5)

This repository's standing rule is that **a no-go gets the same scrutiny as a positive theorem**
(HANDOFF's process rules; `feedback_no_gos_need_same_scrutiny`). So the conclusion of §5 is restated
positively and attacked.

**Positive form.** *Every `k`-uniform bound on `𝒯_p` must come from the `D(S)` leg. On the `Φ_k` leg the
available freedom is exhausted: it consists of (i) the choice of level-0 extension, worth at most `2d =
8`; (ii) the choice of composite gauge, worth exactly `1`; (iii) one-leg differentiation, which
annihilates only components the obstruction does not occupy.*

**Attacks on the positive form, and what survives.**

1. *"(i)-(iii) is not an exhaustive list of the `Φ_k` leg's freedom."* **This attack lands, partially.**
   A fourth kind of freedom exists and is **not** closed: a property of the **actual** `Y^p_{*,0}` that
   distinguishes it inside the admissible class `𝒴` and makes its funnel small. Proposition FB-CLASS
   shows no such property is currently available (`u ∈ 𝒴` defeats everything derivable from the profile
   bound and co-closedness); it does **not** show none exists. **So the honest status of §5 is: a no-go
   about *available routes*, not an impossibility theorem.** Stated that way it survives; stated as
   "no escape exists" it does not, and I do not state it that way.
2. *"The estimator could still be lossy somewhere you did not look."* Corollary FB-NOEST answers this:
   the chain is three identities and one inequality, and the inequality is attained in both directions
   (Lemma TENT-TV attained, Lemma TG-TV the matching lower bound). **Attack repelled.**
3. *"`Φ_k` could be redefined."* True, and admitted in §5.3: `h_0` is part of the blocking's definition,
   so this is a redesign of the RG map. **The positive form is about the estimate, and it survives with
   that scope stated.** It is also the one place where the obstruction is genuinely movable, which is why
   Proposition FB-LOCAL says so explicitly rather than burying it.
4. *"The `n²` might be absorbable downstream."* §3 answers it and the answer is no, with the sharper
   reason that the consumer's inequality is homogeneous of degree 2 in `η`. **Attack repelled** — and
   note it was the attack most worth making, since it is the one that would have made this whole target
   moot in the favourable direction.
5. *"Face (b) might not matter."* §3.3 says it **does not matter on its own** — FB-F4 occurs, there is a
   second, independent `L^{2k−3}` in the same response. **This attack lands, and it is recorded as the
   most consequential finding here.**

---

## 9. Outcome (written after §8)

### 9.1 Outcome table

| object | status | content |
|---|---|---|
| **Face (b) identified, with the `n` and the squared quantity pinned** (§2) | **PROVEN-HERE** (reading of quoted statements) | `n = L^k`; the `n²` is an **explicit prefactor** (the fine→coarse curvature unit conversion of `f_0 = n²dΔ_0^{-1}J_0`, BFT_B.md l.4130), **not** an estimate; what must decay is `Φ_k(Y^p_{*,0})` in **own** units, which is dimensionless and carries no `k`. **Pre-registered verdict MISIDENTIFIED does NOT occur** |
| **What the consumer needs** (§3) | **PROVEN-HERE** (quotation + one line of algebra) | `O(1)` with a `k`-uniform constant (BFT_A.md l.2809, l.2812; BFT_B.md l.3974). **It can absorb nothing** — and because the inequality is homogeneous of degree 2 in `η`, the deficit **cannot be bought with decades of `η`** |
| **Corollary FB-NOEST** (§4.1) | **PROVEN-HERE** as an implication of four quoted items | there is **no estimate to sharpen**: three identities and one inequality attained in both directions; at most `2d = 8` separates bound from object. **Pre-registered verdict ARTEFACT is unreachable through the estimator** |
| **Proposition FB-CLASS** (§4.2) | **PROVEN-HERE, UNCONDITIONAL** | `sup_{v∈𝒴} n²·osc_𝔅(Φ_k(v)) ≥ 2.4768·10⁻³·n²`: **no proof of (TENT-osc) can run through the profile bound and co-closedness alone.** This is the unconditional core of YSUP's verdict, and it is strictly weaker than "(TENT-osc) is false" |
| **Proposition FB-BOOT** (§4.3) | **PROVEN-HERE, elementary** | from BFT_A §38.7's decomposition with `Σ_q|G_e(q)| ≤ ½`, **no lower bound on `|Φ_k(Y^p_{*,0})|` follows at all** — the two lines give `M ≤ 2(A+B)` and nothing below. **Sharpness for the actual response is OPEN**, and what is missing is a **sign statement on `G_e`**, not an estimate. **FB-F3 OCCURS** |
| **Proposition FB-BIANCHI** (§5.1) | **PROVEN-HERE** (fb1 A1-A4, control fired) | one-leg differentiation annihilates exactly the **exact** part of the response leg and the **divergence-form** part of the source leg; the `n²`-attaining witness `u = ⅛d*δ_p` is **purely co-exact**, and `D(S)` is entirely divergence-form. The Bianchi route is **already fully applied and removes nothing that is there** |
| **the divergence-form rewriting** (§5.2) | **CLOSED (PROVEN)** | already performed on the source leg; on the response leg it *is* the composite gauge, and Theorem TG-PRICE prices that at `ρ = 1` exactly |
| **the twisted-Koszul complex** (§5.3) | **VOID at this scope. FB-F2 OCCURS** | `h_i` **is** a Koszul homotopy; the twist is the identity at the trivial background, which is where the `n²` is measured. It belongs to **(N-bg)**, a different wall |
| **summation by parts** (§5.4) | **CLOSED and PRICED** | the least-gradient extension problem is settled in both directions (TENT-TV attained, TG-TV the matching lower bound, TG-OPT's ratio `→ 1`): **at most `2d = 8` = 0.90 decades remains, against 173.2 needed at `k = 183`** |
| **`d = 4` marginality** (§5.5) | **CONFIRMED as real; REFUTED as the explanation** | the count is marginal and **log-free** (`d − 1 − 3 = 0`) and YSUP's measured exponents converge to it, so nothing is mis-treated; and **93.46 % of the obstruction (`φ_1/Φ_k = 243/260` exactly) sits on a single `3⁴` block, where no asymptotics operate** |
| **Proposition FB-LOCAL** (§5.5) | **PROVEN-HERE** as an implication of the quoted exact rationals | the `n²` is **not** an accumulation over levels and **not** asymptotic: it is `L^{2k}` times a `k`-independent rational fixed by `h_0` on one `3⁴` block. **It is in the scheme's definition, not in the analysis** — which is both why no estimate-level escape exists and where the only real freedom is |
| **Proposition FB-ONE-LEG** (§3.3) | **ARGUED** (rests on BFT_A §38.6/§38.8, ARGUED there; the `σ ≈ 0.003` measurement not re-derived) | there are **two** independent `L^{2k−3}` defects in the `Γ_E`-response off the critical set — face (b)'s tent term at the **level-`k`** roots, and §38.6's `σ`-spike term at the **level-`(k−1)`** roots — and **both are `n²⟨D(S), ·⟩`**. Face (b) is **necessary but not sufficient**; the `D(S)` leg closes both at once. **FB-F4 OCCURS** |
| **the price** (§6) | **COMPUTED** (courtesy figures), **with FB-F5 OCCURRING** | there is **no exchange rate**: the requirement is `k`-uniformity and the deficit is exponential in `k`. Through the self-map reading (assumption **(X1)**) the cost is `P(k) = (2k−3)log₁₀3` decades of `η`: **8.11 at `k = 10`, 38.65 at 42, 173.58 at 183.4, 337.90 at 355.6**; break-even against `DX′ = 2.456e−152/C_Ω` at **`k* = 160.380`**, against an `ε_1`-sized budget at **`k* = 42.552`**. The identification of `η` with what `DX′`/`ε_1` bound is assumption **(X2)** and is **not established in any file I read** |
| **Corollary FB-NBHD** (§6.4) | **ARGUED, CONDITIONAL** on Lemma CD and on §38.6's charge sizing | `(NC-Γ)` for `Γ_E` holds `k`-uniformly on `{‖x‖_𝔐 ≤ η, ‖∇(𝔉_k∘exp)(x)‖ ≲ C_SR L³ηn^{−2}}`. The `n²` buys a **neighbourhood of the critical set**, not decades — and the use of that neighbourhood is **circular** as the contraction is currently written |
| **(TENT-osc) itself** | **unchanged from YSUP** | FALSE at `p`'s coarse cell by exactly `n²`, CONDITIONAL on the profile input; `k`-,`T`-uniform outside it with `R_c^{−3}` (ARGUED). **Nothing here changes either half.** §4.2-§4.3 **narrow** the conditionality to a single named missing input (a sign statement on `G_e`) and supply the unconditional class form |

**Pre-registered verdict, against §1.2's table: SHARP-AND-FATAL — with two qualifications that §1.2 did
not anticipate and that are more important than the verdict.** (1) "Sharp" holds **unconditionally only
as a statement about the admissible class** (FB-CLASS); for the actual response it is **OPEN** and cannot
be closed by the lane's own decomposition (FB-BOOT). (2) "Fatal" is **not the operative word**, because
face (b) is **not the binding item**: §3.3's second `L^{2k−3}` survives its removal.

### 9.2 Net on the open accounting

Nothing is added to or removed from the open set by this file. **(TENT-osc) stays as YSUP left it.** What
changes is its **rank**: it should be recorded as *one of two* `L^{2k−3}` defects sharing the leg
`D(S)`, not as the obstruction.

### 9.3 The single biggest remaining obstruction in this scope

**Not the `n²`.** It is the **circularity in Corollary FB-NBHD**: the only mechanism that can pay `L^{2k}`
is the smallness of `∇(𝔉_k∘exp)` along the contraction (Lemma CD, BFT_A.md l.2973-2979), the contraction
needs `(NC-Γ)` to take the steps that make `∇(𝔉_k∘exp)` small, and `(NC-Γ)` needs the smallness. Breaking
that circle — the route BFT_A.md l.3613 names and marks *"Not attempted"* — is what face (b) actually
costs, and it is a statement about the **architecture of the contraction**, not about `Φ_k`.

Below it, and much cheaper: a **sign statement on the bootstrap kernel `G_e`** (§4.3), which would turn
`(TENT-osc)`'s refutation from CONDITIONAL into unconditional and would settle the `Z″₀`-cancellation
attack point in one step.

---

## 10. FOR OTHER FILES (not edited)

**To the lead.**
1. **T55-G's target, as scoped, is worth less than it looks, and the reason is recorded in §3.3.** Face
   (b) is one of **two** `L^{2k−3}` defects in the `Γ_E`-response off the critical set; the other is
   BFT_A §38.6's `σ`-spike term at the level-`(k−1)` roots, which lead decision **D1 has already
   accepted as real**. Removing face (b)'s `n²` leaves `(NC-Γ)` for `Γ_E` failing by `L^{2k−3}`.
   **Both are `n²⟨D(S), ·⟩`**, so the leg to attack is `D(S)`, not `Φ_k`, and one mechanism closes both.
2. **The `n²` is not priceable in the ARS_FIX/EPS1_SWEEP currency, and quoting it there would
   misrepresent it** (§6.1): the consumer's inequality is homogeneous of degree 2 in `η`, so lowering
   `η` buys exactly zero. Courtesy figures are in §6.3 with their two assumptions named.
3. **I did not relitigate the representative route** (TGAUGE_PRICE's closure) and I confirm it from a
   second direction: §5.1 shows **why** `ρ = 1` came out exactly rather than approximately — the
   `n²`-attaining witness is purely co-exact, so there is nothing for a gauge to act on.
4. **Two assumptions of mine that a reviewer should break first:** **(X1)** the self-map reading of
   `C_SR` in §6.2, which BFT_A.md l.2812 does not write; and **(X2)** the identification of BFT's `η`
   with what `DX′` and `ε_1` bound, which **I found stated nowhere**. If (X2) is false, every decade
   figure in §6.3 is in the wrong currency — the structural conclusions (§2-§5, §9.3) do not depend on
   it.

**To YSUP.md's owner.**
- **§4.3 narrows your conditionality to one named input and shows it is not removable by §38.7's
  decomposition.** `Σ_q|G_e(q)| ≤ ½` (U4′) admits cancellation of up to half the sup, and the same two
  lines that give `M ≤ 2(A+B)` give **no** lower bound. **A sign/positivity statement on `G_e(q)` is
  exactly and only what is missing** — the funnel coefficients are already known to be sign-coherent
  (`φ_1`, `φ_2` same sign, ratio `17/243`). This is your flagged `Z″₀`-cancellation attack point with
  the mechanism identified.
- **One erratum, which changes no number** (§7.3): YSUP.md l.249's list of "all four … for the
  unnormalised `u`" mixes normalisations — `φ_1 = −1/54` and `φ_2 = −17/13122` are un-normalised,
  `ψ_u = −65/26244` is the `⅛`-normalised total (un-normalised: `−130/6561`). A reader combining the
  four as written gets `φ_1/ψ_u = 7.477 > 1`. Everything downstream is correct.

**To TENTQ.md's owner.** §2.2 here restates your `n²` in the form I think it should be carried: it is an
**explicit prefactor and a unit conversion**, and `Φ_k` is **unit-free and `k`-free**, so face (b) is the
demand that a `k`-free dimensionless rational be `≤ L^{−2k}`. Said that way, the impossibility of an
estimate-level escape is visible before any attack, and Corollary FB-NOEST makes it precise.

**To BFT_A.md's owner (lane A).** l.3613's parenthetical — *"the contraction can be arranged so that its
linear solve only meets composite-co-closed sources up to remainders multiplied by `∇(𝔉_k∘exp)` (Lemma
CD). Not attempted."* — is, by §3.3 and §6.4, **the only route that closes both `L^{2k−3}` defects at
once**, and §9.3 names the exact obstruction in it (circularity: the estimate is needed to take the
steps that would make it available). It should be promoted out of a parenthetical.

**To PROOF.md's owner.** Nothing in this file moves the tally. If face (b) is carried in the ledger it
should be carried **with its companion**: *"one of two `L^{2k−3}` defects of the `Γ_E`-response off the
critical set, both linear in `D(S)`; face (b) is necessary but not sufficient."*

---

## 11. Discipline, and one disclosure about this file's own edits

**Order and times.** §1 PRE-STATED (statements only, no constant from this session), **first edit of this
file, 2026-10-28T21:17:09Z** → `checks/fb1_criteria.md` **21:20:47Z**, with pre-registered PASS/FAIL,
designed-FAIL control and scope limitations, and **no constant derived in this session** →
`checks/fb1_bianchi.py` → `checks/fb1_out.txt` (ALL PASS; `fb1_err.txt` empty) → §2 onwards. Exact
integer and exact `Decimal`/`Fraction` arithmetic in plain python; **no numpy, no BLAS, no machine-wide
numeric lock taken**; runtime under 2 s.

**No FAIL to report**, and the **designed-FAIL control A6 FIRED** on all three clauses it targets (A1:
6 nonzero; A2: 25/25; A3: 7/10 under a single flipped incidence sign). One probe is labelled **post-hoc**
(§7.3, the three-fraction consistency arithmetic, run after §5.5 and not pre-registered).

**Disclosure about edits to this file.** After §10 was written I made one **citation-correction pass**
over §2-§10, replacing 39 `file:line` references with the lines I had re-verified by `grep`/`sed` against
the live files. **No statement, status, number or conclusion was changed** — only line numbers, and in
one place the wording of a citation that attributed "the tent attains Lemma TENT-TV" to TENTQ when the
sentence I meant is in TGAUGE_PRICE. This is recorded rather than left silent because this lane's defect
1 is precisely mis-cited symbols, and an uncorrected `file:line` is worse than none.

**What a hostile reviewer should attack first, in this order.**
1. **§3.3 / Proposition FB-ONE-LEG** — the claim that face (b) is not the binding item. It is **ARGUED**
   and rests on BFT_A §38.6/§38.8, which are ARGUED there, and I did not re-derive `σ ≈ 0.003`. If the
   `σ`-spike term is not of size `L^{2k−3}` in the `Γ_E` response, my central finding weakens to a
   remark.
2. **§6.2 assumptions (X1) and (X2)** — the self-map reading, and the identification of `η`. Neither is
   written in any file I read. If (X2) is false, the decade figures are in the wrong currency.
3. **§4.3 / Proposition FB-BOOT** — whether `Σ_q|G_e(q)| ≤ ½` is the right form of the bootstrap at the
   point of use, and whether some other statement in §38.7 already supplies the sign I say is missing.
4. **§5.5 / Proposition FB-LOCAL** — the `93.46 %` localisation. It is read off **quoted** rationals
   (`φ_1 = −1/54`, `φ_2 = −17/13122`), which I checked for mutual consistency but did **not** rebuild
   from the funnel.
