# NBG_A.md — (N-bg): the nontrivial background, attacked directly (target T55-D)

## §A0 PRE-STATED (FIRST EDIT of this file, 2026-10-28 21:13:54 UTC; STATEMENTS ONLY; cites nothing produced in this session)

This section is written before any derivation. It names what I intend to do, the outcomes I will accept as
success or failure, and the failure modes I will record as failures if they occur. Every item below is a
statement of intent or a pre-registered verdict, not a result.

### A0.1 Scope and ownership
- I may WRITE only this file and `checks/na1_*`. I may READ anything. No git, ever.
- Target **T55-D** (RTARGET §54): attack **(N-bg)** directly — first by stating it precisely with its
  quantifiers, then by trying to prove it, then, failing that, by reducing it to the smallest missing input.
- The statement of record I am starting from is **NORMS.md l.629**: "**(N-bg) [OPEN].** D³E_k^br(V) for V in
  the small-field class, with a constant uniform in k", with its two routes (i) perturbative / BFT-5 and
  (ii) analytic / BFT-4 Cauchy.

### A0.2 Pre-stated targets
- **TA. The statement.** Write (N-bg) as a self-contained mathematical statement: *what* object, in *which*
  norm, uniform in *what*, over *which* class of backgrounds, given *what*. Quantifiers in the order the
  consumer imposes them, with every symbol pinned by file:line (lane defect 1 — symbol collisions).
- **TB. The three quantifier questions**, answered against the CONSUMER, not against the statement:
  (a) is k-uniformity what the consumer needs, or something weaker;
  (b) is the class of backgrounds the full small-field class, or a smaller set the consumer actually feeds;
  (c) does (N-bg) inherit NORMS §N7's weight PAIR (θ_w^c, θ_w^r) = (2, d−1), or a different condition.
- **TC. The identity at a nontrivial background.** Decide whether Lemma E3 / TOWER-VAR (d) —
  `D³E_k^br(1) = D³𝔉_k(1)[ζ^c·,ζ^c·,ζ^c·]` — holds verbatim at a nontrivial critical chain, or acquires
  extra terms. If it holds, say exactly which hypotheses it needs.
- **TD. The vertex at a nontrivial configuration.** Decide whether Lemma N1-1's structural statement — the
  composite cubic vertex carries *exactly one differentiated (or residual) leg per term* — survives at a
  nontrivial critical configuration. If it does not, identify the new terms, count their scaling exponents
  by the method of NORMS §N6/§N7, and say whether they are subcritical, marginal or divergent at d = 4.
- **TE. The reduction.** Reduce (N-bg) to the smallest list of inputs not already proven, and decide
  RTARGET §54's **NBG-F1**: whether (N-bg) and BFT-5's (G♯_0-field)/(GAP-Z) are or are not the same
  obstruction.
- **TF. d = 4 marginality.** For every exponent condition I derive, record the dimension at which it fails.
  If a route needs d < 4 anywhere, name that as the obstruction rather than hiding it in a constant.

### A0.3 Pre-registered outcomes (one of these will be recorded as the outcome of TD/TE)
- **O1.** The background vertex is subcritical: (N-bg) imposes no exponent condition beyond the one
  Theorem N1-15 already imposes, and the whole of (N-bg) reduces to background versions of the LINEAR
  inputs. Then (N-bg) collapses onto (GAP-Z)/(G♯_0-field) and NBG-F1 does NOT occur.
- **O2.** The background vertex is marginal: a new term sits exactly at the d = 4 borderline, so (N-bg)
  needs a strictly stronger weight pair than BFT-1 supplies. Then (N-bg) is a genuinely separate wall and
  NBG-F1 OCCURS.
- **O3.** The background vertex is divergent: a new term grows with k at any admissible weight pair, so
  (N-bg) is FALSE as stated and must be restated (e.g. with a k-dependent threshold). Recorded as a no-go,
  and then subjected to the repository's no-go standard (reframe as a positive claim and re-test).
- **O4.** No decision: I cannot settle TD. Recorded as a failure of this session, with the specific step
  that defeated me named.

### A0.4 Pre-stated failure modes (if one occurs, it is reported as having occurred)
- **NBGA-F1.** The identity of TC acquires extra terms at a nontrivial background (i.e. TOWER-VAR (d) is
  special to the trivial point). Then route (i) of NORMS Remark N6-5 is harder than that remark says.
- **NBGA-F2.** The consumer's class is NOT the small-field class, in the direction that makes the theorem
  HARDER (a larger class), not easier. In particular: PROOF.md's "another route to (H-G)" remark requires
  D³E on interpolated fields that leave the small-field class.
- **NBGA-F3.** The norm in which (N-bg) must hold is not the one Theorem N1-15 delivers (N3 / row norm),
  so a background N1-15 would not discharge the consumer's clause even if proven.
- **NBGA-F4.** I find a defect in NORMS.md's own definitions while reading them. Then I report it in
  "FOR OTHER FILES" and do NOT silently build on the repaired version.
- **NBGA-F5.** My exponent count reproduces someone else's by construction (a gate built from its object's
  own primitives), so it could not have come out otherwise. Then it is not evidence and I say so.
- **NBGA-F6.** (N-bg) turns out not to be consumed by the route the lane has adopted (D1/D2: the composite
  route), so D5's "the wall" is mis-targeted. If so, I say it loudly, per D6.

### A0.5 Method and discipline
- Rule 2: any numeric check gets `checks/na1_<id>_criteria.md` with PASS/FAIL pre-registered BEFORE the
  script, containing no constant derived in this session. Rule 6: I will prefer not to run numerics at all;
  exact integer/rational arithmetic in plain python if any.
- Any check I run gets a **designed-FAIL control** and I report that the control failed (lane defect 3).
- Rule 4 (banked results): where my argument leans on a banked PROVEN, I re-derive the load-bearing step in
  this file rather than cite it.
- Statuses PROVEN / ARGUED / CONDITIONAL / GAP / OPEN, used strictly. A failed attempt is reported as failed.
- **Append-only.** Nothing already in this file is rewritten after it is written.

### A0.6 What I will NOT re-walk (dead routes, per the brief and SESSION24_RESULTS.md)
Per-level induction in any norm as a route to level-uniformity; global axial gauge; within-cell axial gauge;
gluing via Theorem RW; thin-cluster escape; finite funnel truncation; (NEUT-box); route (ii)/GT-ell;
(CovLift) non-residual at θ > 0; the gauge escape (Proposition TG-EXCL).

---

## §A1 The statement of (N-bg), with its quantifiers in the consumer's order (TA, TB)

Written 2026-10-28, after §A0. Everything in this section is an exegesis of existing files; the only claim
is about which statement is which, pinned by file:line.

### A1.0 Three distinct objects wear the symbol C_♭ (lane defect 1: verify before combining)

| tag | definition | file:line | what it is |
|---|---|---|---|
| **(C♭-I)** | `C_♭ := 4S_♭n_1/r_♭`, bounding the N_0-Lipschitz constant of Hess f, of the joint (A,B)-Hessian and of the level-1 slice/fixing operators | PROOF.md l.5829-5840 (Lemma N5-an♭) | an **analyticity** constant of an **explicit local** functional. Exists, not evaluated ((C_♭-eval), OPEN). Level-independent. |
| **(C♭-II)** | "E_i^br is holomorphic on the complex neighbourhood, and **the N_0-Lipschitz constant of its Hessian in the chart at the lift is ≤ C_♭^{(i)}**" | PROOF.md l.6045 ((I_i) (c) of Proposition NAH-ind); same words in **(BG-unif) (iv)**, PROOF.md l.6098 | the Lipschitz constant of Hess E_i^br **on the chart-ball at the lift**. This is what BR1-at-level-i and NAH-unif consume. |
| **(C♭-III)** | "C_♭^{(k)} as its consumers use it is the Lipschitz constant of Hess E_k^br **on the small-field class**" | NORMS.md l.625-626, and (N-bg) at NORMS.md l.629 | the Lipschitz constant **on the whole class**. This is what (N-bg) is stated to deliver. |

Also in the family, and not the same: `C_♭(F_i)` at PROOF.md l.6284 ("the N_0-Lipschitz constant (**in the
sup norm of the field**) of Hess E_i^br") — E3's recursion variable, which omits "at the lift"; and `C_soft`,
the same constant for the soft term, PROOF.md l.6284-6285.

**Consequence, and it is the first result of this file.** **(C♭-III) ⊋ (C♭-II)**: (N-bg) is stated at a
strictly larger class than its live consumers impose. Two corollaries:

1. **SF's ε_1 chain does NOT consume (N-bg).** SF.md l.2192, l.2497, l.2790 use `ε_br ∋ 1/(24𝔠_∞²C_♭)` and
   read `ε_1 ≤ 5.95·10⁻⁷⁷/C_♭` (session 6) / `4.26·10⁻⁷/C_♭` (session 7). That `C_♭` is **(C♭-I)**, the
   level-0 N5-an♭ constant of the *explicit* functional, and SF names its open input as **(C_♭-eval)**
   (SF.md l.2798-2800, PROOF.md l.5850), not as (N-bg). So **(N-bg) does not drive ε_1**, and the ε_1
   sweep and (N-bg) are disjoint problems. *(This is a reading of other lanes' files, offered to them in
   §A6, not an edit.)*
2. **NORMS §N8's first two consumer rows are mis-attributed at level 0.** The rows "Lemma BR1 … ‖R_2‖_∞ ≤
   ½C_♭r² … Needs **(N-bg)**: R_2 is at the branch, not at 1" and "Lemma CURV1 step (6) … needs (N-bg)"
   (NORMS.md l.688-689) are **false at level 0 and true at level i ≥ 1**. At level 0, `f_V(A) :=
   F(e^AU^{(0)}(V), V)` is an explicit local function of the links and the Lipschitz step is discharged by
   N5-an♭ = (C♭-I) at every V of the class with no background statement whatever (that is exactly what
   BR1's own proof does, PROOF.md l.5870-5872). At level i ≥ 1 the same step needs (C♭-II) for E_i^br, and
   there (N-bg) is the right pointer. The table does not distinguish the two, and the symbol C_♭ in those
   rows changes meaning between BR1's proof and BR1-at-level-i.

### A1.1 (N-bg), stated self-containedly

Notation of PROOF [S20]-[S22] and NORMS §N1. `𝔉_k(U_0,…,U_{k-1}; V_k) := S_W(U_0) + Σ_{j=0}^{k-1}κ_jΣ_c
φ̂_c(M̄^{(j)}_c(U_j); U_{j+1})` (PROOF.md l.6580, Lemma TOWER-VAR); `E_k^br(V_k) = 𝔉_k(tower; V_k)`
(TOWER-VAR (a)); `N_0(M) := max row ℓ¹ sum`, and for a symmetric trilinear form
`N3(T) := max_xΣ_{y,z}|T(x,y,z)| = sup{|T(δ_x,Y,W)| : x, |Y|_∞ ≤ 1, |W|_∞ ≤ 1}` (NORMS.md l.105-107, from
PROOF.md l.6289's `N_0(D³E_i[w]) ≤ C_♭^{(i)}|w|_∞`).

> **(N-bg), consumer form — the statement this file adopts.**
> *There exist `ε_0 > 0`, `r_0 > 0` and `C_♭^∞ < ∞`, **depending only on `(N, L, κ_±)`** — in particular
> independent of `k`, of the torus side `T`, and of the field — such that:*
> *for **every** `k ≥ 1`;*
> *for **every** torus with level-k side `T ≥ T_0`;*
> *for **every** level-k field `V` with own-units plaquette logs `max_P|log V_P| ≤ ε ≤ ε_0`, for which the
> critical chain `Z(V)` exists;*
> *for **every** `A` on level-k links with `|A|_∞ ≤ r_0` (the chart at the lift `A ↦ e^AU^{(k)}(V)` of
> PROOF.md l.6045);*
> *one has* **`N3(D³E_k^br(e^AU^{(k)}(V))) ≤ C_♭^∞`.**

Four remarks, each of which is a quantifier that the statement at NORMS.md l.629 does not carry:

- **(q1) "uniform in k" is uniform in the LEVEL INDEX i = k of `E_i^br`**, which is simultaneously the number
  of integrated levels. Both readings coincide here; no ambiguity, but it should be said once.
- **(q2) The norm is `N3` — a row norm with a DELTA in the differentiated slot — not NORMS §N2's `𝔑`.**
  See §A1.3: `𝔑` as defined is `+∞` for every nonabelian consumer, so a background Theorem N1-15 stated in
  `𝔑` would discharge nothing. Pre-stated failure mode **NBGA-F3 is therefore live and is avoided only by
  using N3**, which is what Theorem N1-15 in fact does (NORMS.md l.510).
- **(q3) The class is the LIFT-TUBE, not the class.** The `∀A` quantifier is over a sup-ball of radius
  `r_0` in the chart at the lift; `r^{(i)} = 12𝔠_∞^{(i)}ε` in BR1, or HG-ind's corrected
  `r^{(i)} := 2𝔠_∞^{(i+1)}κ_i(N_0(|𝒦_ρ^{(i)}|) + 1)ε` (PROOF.md l.6477, [R22-fix S22-4]). **Honest
  limitation of this remark:** `E_k^br` is gauge invariant (BR1 (iv)), `N3` is a block norm, so only the
  gauge class of the background matters; and on a block, curvature-smallness buys axial connection-smallness
  (Lemma AX / Lemma N1-5), so the lift-tube is *within constants of* the small-field class modulo gauge. I do
  **not** claim the lift-tube is strictly smaller in a way that is exploitable. What I do claim is that
  (C♭-II) is the clause to prove and (C♭-III) is strictly more than anyone has asked for.
- **(q4) The direction in which the class is too SMALL.** Pre-stated **NBGA-F2 OCCURS**: PROOF.md
  l.6508-6511's "another route to (H-G)" needs, besides (C♭-II), the localisation of `∇E_i^br`, and its own
  text says "the interpolation that replaces far links **leaves the small-field class**". So the one route
  that converts (N-bg) into level-uniform (H-G) without BFT-4 needs `D³E` on a class **larger** than the
  small-field class. That is a second, opposite, class question, and it is not part of (N-bg) as stated.

### A1.2 Is k-uniformity what the consumer needs? (TB (a))

The consumer chain is `(N-bg) ⟹ (H-C)'s C_♭ clause ⟹ Proposition NAH-unif/NAH-unif′ ⟹ ε_unif > 0 ⟹
(N5-unif) ⟹ SF Corollary SF-thr-k` (PROOF.md l.6299-6302; SF.md l.957, l.986). Two findings:

**(k1) The consumer is already capped at `ε_unif = O(1/k)` by a DIFFERENT mechanism, so full k-uniformity of
C_♭ is not the binding quantifier for it.** Failure mode CURV-F2″ (PROOF.md l.6500-6507) states, in the
ledger's own words, "`ε_unif = O(1/k)` **even if every `𝔠_∞^{(i)}`, `κ_i` and `C_♭^{(i)}` were
level-uniform**". Since `ε_unif := inf_i min{…, ε_br^{(i)}, …}` and `ε_br^{(i)} ∋ 1/(24(𝔠_∞^{(i)})²C_♭^{(i)})`
(PROOF.md l.5843), a growth `C_♭^{(i)} = O(i)` contributes `Ω(1/k)` to the same infimum and therefore does
**not** worsen the route's output. **So for the per-level route as it stands, `C_♭^{(k)} = O(k)` is as good
as `O(1)`.** NORMS [N1-corr 1] (NORMS.md l.600-602) priced the polynomial case as "still not (H-C)"; against
the *consumer* rather than against (H-C), `O(k)` is enough and `O(k²)` costs one power.
**(k2) But the weakening is not free, and I say so.** If level-uniform (H-G) is obtained non-recursively
(BFT-4, or PROOF.md l.6508-6511's remark route), CURV-F2″ is removed and the cap `O(1/k)` lifts — and then
`C_♭^{(k)}` is again binding at `O(1)`. So the honest answer to TB (a) is:
> **(N-bg) is needed k-uniformly only in the architecture in which CURV-F2″ has already been removed; in
> every architecture now written down, `C_♭^{(k)} = O(k)` suffices.** Whether `ε_unif = O(1/k)` is itself
> acceptable is a FLOW/SF question (the level-k curvature of an asymptotically free flow is itself `O(1/k)`,
> so the comparison is of constants, not of rates). I do **not** settle it; it is item 2 of §A6.

### A1.3 A defect in NORMS §N2's vertex norm `𝔑` (pre-stated NBGA-F4 OCCURS)

**Claim (PROVEN-HERE).** Let `T := D³E_k^br(V)` for any `V` at which `E_k^br` is gauge invariant and whose
Hessian does not annihilate all commutators `[Y, λ]`. Then NORMS Definition N^F-2's vertex norm
`𝔑_{l,m}(T) := sup{|T(X,Y,W)| : ‖X‖^{(1)}_{l,m} ≤ 1, ‖Y‖^{(∞)}_{l,m} ≤ 1, ‖W‖^{(∞)}_{l,m} ≤ 1}`
(NORMS.md l.169-171) is `+∞`.

*Proof.* `‖X‖^{(1)}_{l,m}` depends on `X` only through `d_lX` and `r_l(X)` (NORMS.md l.157-161). Take
`X = t·d_lλ̂_l` for a nested pure gauge of Lemma N1-6. Then `d_lX = 0`, and `r_l(d_lλ̂) = Q d_lλ̂_l −
d_{l+1}λ̂_{l+1} = 0` because `Q_str d_iμ = d_{i+1}(μ|centres)` and the family is nested (NORMS.md l.420-421,
l.306-310). So `‖X‖^{(1)}_{l,m} = 0` for every `t`. But by the Ward identity the file itself states —
`T(d_lλ, Y, W) = −H([Y, λ], W) − H(Y, [W, λ])`, NORMS.md l.179-181 — `|T(X,Y,W)| = |t|·|Ward term|`, which is
unbounded in `t` as soon as the Ward term is non-zero. ∎

*Scope and repair.* The Ward term vanishes identically in the abelian/linearised setting (commutators are
zero), so `𝔑` is finite exactly where NQ-1 lives and infinite exactly where (N-bg) lives — which is the
worst possible place for this defect to sit. **The repair is one line and costs nothing**: the BFT norm `𝔐`
is defined *on composite displacements `X ∈ S_k`*, a slice (REVIEW_S22 l.389-392, l.432), and a slice
excludes nested pure gauges; Definition N^F-2 drops the words "`X ∈ S_k`". **Nothing in NORMS.md depends on
the defect**: Theorem N1-15 is stated and proved in `N3` (NORMS.md l.510, l.531), not in `𝔑`, and §N7's
exponent table is a statement about the same row-norm counting. I report it because a reviewer comparing a
future background N1-15 against `𝔑` would be comparing against an empty gate (lane defect 3: a gate nothing
can pass is not a gate). Requested in §A6 as item 1.

---

## §A2 The identity at a nontrivial background: PROVEN-HERE, and it costs nothing (TC)

### Lemma NB-1 (background TOWER-VAR (d)): PROVEN-HERE

*Statement.* Let `F(A, B)` be `C³` near `(a_0, B_0)`, and let `B ↦ a(B)` be a twice-differentiable family
with `F_A(a(B), B) = 0` for all `B` near `B_0`, `a(B_0) = a_0`. Put `E(B) := F(a(B), B)` and
`ζ := (a'(B_0), 1)`. Then, **at `B_0`, with no hypothesis that `B_0` is a distinguished point**,
  **`D³E(B_0)[δ_1, δ_2, δ_3] = D³F(a_0, B_0)[ζδ_1, ζδ_2, ζδ_3]`  exactly.**

*Proof.* Write `z(B) := (a(B), B)`, so `z' = ζ`, `z'' = (a'', 0)`, `z''' = (a''', 0)`. By the chain rule for
the third derivative of a composition,
`D³E = D³F[z'·, z'·, z'·] + Σ_{3 pairings} D²F[z''(δ_i,δ_j), z'δ_l] + DF[z'''(δ_1,δ_2,δ_3)]`.
The last term is `F_A[a'''] = 0` by criticality. Each middle term is
`D²F[(a''(δ_i,δ_j), 0), (a'δ_l, δ_l)] = F_AA[a''(δ_i,δ_j), a'δ_l] + F_AB[a''(δ_i,δ_j), δ_l]
 = (F_AAa' + F_AB)[a''(δ_i,δ_j), δ_l] = 0`,
because differentiating `F_A(a(B),B) = 0` once gives `F_AAa' + F_AB = 0` **at every `B`**, not only at a
distinguished one. ∎

*Independent re-derivation (second route, because this step is load-bearing).* Expanding directly,
`D³E = F_BAA[δ_1,a'δ_2,a'δ_3] + F_BAB[δ_1,a'δ_2,δ_3] + F_BBA[δ_1,δ_2,a'δ_3] + F_BBB + F_BA[δ_1,a''(δ_2,δ_3)]`,
while `D³F[ζ,ζ,ζ]` is those first four terms plus `D³F[(a'δ_1,0), ζδ_2, ζδ_3]`. Differentiating
`F_AA[v,a'δ] + F_AB[v,δ] = 0` once more in `δ_3` and setting `v = a'δ_1` gives
`D³F[(a'δ_1,0),ζδ_2,ζδ_3] = −F_AA[a'δ_1, a''(δ_2,δ_3)]`, and the same relation with `v = a''(δ_2,δ_3)`,
`δ = δ_1` gives `F_AA[a''(δ_2,δ_3), a'δ_1] = −F_BA[δ_1, a''(δ_2,δ_3)]`. The two expressions coincide. ∎

### Corollary NB-2 (the composite identity at a nontrivial critical chain): PROVEN-HERE given (CL-4)-type differentiability

*Statement.* Let `V` be a level-k field for which the tower `Z(V) = (U_0(V), …, U_{k-1}(V))` exists and is
twice differentiable in `V`. Then
  **`D³E_k^br(V) = D³𝔉_k(Z(V); V)[ζ^c(V)·, ζ^c(V)·, ζ^c(V)·]`,  `ζ^c(V) := (a'(V), 1)`,**
with `a'(V) = −(Hess_{AA}𝔉_k(Z(V);V))^{-1}Hess_{AB}𝔉_k(Z(V);V)` on the slice (any admissible representative,
Lemma N1-2).
*Proof.* TOWER-VAR (a) (PROOF.md l.6583-6586) gives `F_A = ∇_{(U_0,…,U_{k-1})}𝔉_k = 0` along the tower and
`E_k^br(V) = 𝔉_k(Z(V); V)`, at every `V` of the class — the identity is not special to `V = 1`. Apply
Lemma NB-1 with `A := (U_0,…,U_{k-1})`, `B := V`. Gauge: `a'` is determined modulo fluctuation-gauge
directions, and Lemma N1-2 (NORMS.md l.228-250) licenses any admissible representative; its proof uses only
that `a_Λ` is a differentiable critical family and that `F_AA` annihilates gauge directions **at a critical
point** (Lemma NA-inv) — both true at every critical point, not only the trivial one. ∎

### Reading: pre-stated failure mode NBGA-F1 does NOT occur, and TOWER-VAR (d)'s stated reason is narrower than its true reason

PROOF.md l.6591-6594 justifies TOWER-VAR (d) by "the second-derivative term `D²𝔉[D²Z, DZ]` pairs a direction
with **the linear branch, which is critical for the quadratic part** in every direction (as in Lemma E3)" —
a trivial-background argument. The true reason, above, is `F_AAa' + F_AB = 0`, the first derivative of
criticality, which holds at every background. **So TOWER-VAR (d) generalises verbatim and route (i) of
NORMS Remark N6-5 (NORMS.md l.630-634) pays nothing for the identity.** Note also that **Lemma E3 itself is
already stated at an arbitrary background** — PROOF.md l.6276-6277 reads "any level: `F(A,B)` smooth,
`U(e^BV) = e^{a(B)}U(V)` a real-analytic family of critical points of `F(·, e^BV)`" — so the single-level
background identity is banked; what Corollary NB-2 adds is the **composite** version, which is what the
composite route needs and which TOWER-VAR (d) states only at `1`.

**Whole content of (N-bg) after NB-2.** Two factors, and nothing else:
- **(BG-V) the vertex** `D³𝔉_k` evaluated at the configuration `Z(V)` — an *explicit, finite-range, local*
  functional at a configuration with small own-units curvature and small soft fluctuations;
- **(BG-ζ) the background chain-minimiser map** `ζ^c(V)` — the background versions of (I3), (I4), (I5),
  Lemma N1-4, Lemma N1-11, (N-Q), (N-loc).

§A3 prices (BG-V). §A4 identifies (BG-ζ).

---

## §A3 The background vertex: PROVEN-HERE subcritical (TD). Pre-registered outcome **O1**.

### A3.1 Lemma NB-3 (the three vertex families at a nontrivial configuration): PROVEN-HERE

*Statement.* Let `Z = (U_0,…,U_{k-1})` be any configuration with level-0 plaquette logs `X_p := log U_{0,∂p}`
and soft fluctuations `ρ^{(0)}_c := ρ_c(U_j, U_{j+1})`, all inside the BCH ball. Then
  **`D³𝔉_k(Z)[A,A,A] = Σ_p{ W'''(X_p)[Y'_p,Y'_p,Y'_p] + 3W''(X_p)[Y''_p, Y'_p] + W'(X_p)[Y'''_p] }`**
  **` + Σ_jκ_jΣ_c{ φ̂'''(ρ^{(0)}_c)[ρ_1,ρ_1,ρ_1] + 3φ̂''(ρ^{(0)}_c)[ρ_2, ρ_1] + φ̂'(ρ^{(0)}_c)[ρ_3] }`**
where, with `Y_p(A) := log(the p-holonomy of e^AZ)`:
`Y'_p = (d^ZA)_p`, the **background-covariant coboundary** `Σ_bσ_bAd(h_b)A_b` (`h_b` the partial background
product round `p`); `Y''_p = 2Q^Z_2(A)_p` and `Y'''_p = 6C^Z_p(A)` the covariant quadratic and cubic BCH
terms, with ℓ¹ coefficient masses `M_W(1+O(ε))` and `M_C(L,d,N) < ∞`, **neither of which contains a
coboundary**; and `ρ_1 = r_j(A)` (the residual), `ρ_2, ρ_3` its quadratic and cubic parts. The scalar
coefficients obey
  **`W'(X) = X + O(|X|³),  W''(X) = 1 + O(|X|²),  W'''(X) = O(|X|)`,**
  **`φ̂'(ρ) = ρ + O(|ρ|³),  φ̂''(ρ) = 1 + O(|ρ|²),  φ̂'''(ρ) = O(|ρ|)`.**

*Proof.* `D³[W∘Y](0)[A,A,A] = W'''(Y(0))[Y',Y',Y'] + 3W''(Y(0))[Y'',Y'] + W'(Y(0))[Y''']` is the chain rule
for a scalar function of a map with `Y(0) = X_p`. For the coefficients: for `Y ∈ su(N)`, `tr Y = 0` and
`Re tr Y³ = 0` (`(Y³)^† = −Y³`, so `tr Y³` is purely imaginary), hence
`W(Y) := Re tr(1 − e^Y) = ½|Y|²_HS − (1/24)tr Y⁴ + O(Y⁵)` — **this is Lemma N1-1 (a)'s computation
(NORMS.md l.198-205), re-derived here at `Y ≠ 0`** — and the three displayed coefficient statements follow
by differentiating. The same for `φ̂ = ½|ρ|² + O(ρ⁴)` (TOWER-VAR (c), PROOF.md l.6589-6590). That
`Y'_p = (d^ZA)_p`: the linear part of the ordered product `∏(e^{σ_bA_b}Z_b)` round `p` is the `Ad`-twisted
signed sum of the legs, which is the covariant coboundary by definition. ∎

*What changes relative to Lemma N1-1, said plainly.* At `Z = 1` the coefficients `W'(0)` and `W'''(0)`
**vanish**, and only the middle family survives — that is NORMS Lemma N1-1's "exactly one differentiated (or
residual) leg per term" (NORMS.md l.191-226). At `Z ≠ 1` the two outer families switch on, with coefficients
of size `|X_p|` and `|ρ^{(0)}_c|`. **So Lemma N1-1's structural statement is FALSE at a nontrivial
background, and the whole new content of (N-bg)'s vertex is the two families it loses.** The dangerous one
is the last: `W'(X_p)[Y'''_p]` and `φ̂'(ρ)[ρ_3]` carry **no** differentiated leg at all.

### A3.2 Theorem NB-4 (the background vertex adds no exponent condition): PROVEN-HERE given (H1)-(H3)

*Hypotheses.*
- **(H1)** the tower `Z(V)` exists at `V` and is twice differentiable in `V` (Corollary NB-2's hypothesis;
  the identification "tower = composite critical point" is PROOF's **(CL-4)**).
- **(H2)** *BFT-1 at the critical chain, at the weight PAIR* `(θ_w^c, θ_w^r) = (2, d−1)`: own-units level-j
  plaquette logs of `Z(V)` `≤ C_0L^{−2(k−j)}ε` and own-units soft fluctuations `≤ C_0L^{−(d−1)(k−1−j)}ε`.
- **(H3)** *the background linear package*: the background chain-minimiser map `ζ^c(V)` obeys the background
  versions of (I3), (I4), (I5) — equivalently of Lemma N1-4, Lemma N1-7, Lemma N1-11 with (N-Q) and
  (N-loc) — with constants `C_f, C_R, M, m′, 𝔠_P, c_m` depending only on `(N, L, κ_±)`, not on `k`, `T` or `V`.

*Conclusion.* With the bookkeeping of Theorem N1-15 (NORMS.md l.507-556), at `d = 4`, `L = 3`,
  **`N3(D³E_k^br(V)) ≤ (1 + C′ε)·[𝔚 + 13.5·𝔖] + C″·ε`, uniformly in `k`, `T` and `V` in the class,**
where the new `O(ε)` term is the sum of four geometric series whose L-exponents per level are
**−1, −4, −8 and −2** (check na1-C), explicitly
`L^{−k}` (0-derivative Wilson) `+ L^{−4k}` (3-derivative Wilson) `+ Σ_{n≥1}L^{−2n+3} = 27/8`
(0-derivative soft) `+ Σ_{n≥1}L^{−8n+12} = 81·6561/6560` (3-derivative soft), each times an absolute
constant built from `M_W, M_C, 𝔠_P, c_m, C_f, C_R, κ̂, C_0`.

*Proof.* (1) Corollary NB-2 reduces `D³E_k^br(V)` to `D³𝔉_k(Z(V))[ζ^c·,ζ^c·,ζ^c·]`. (2) `𝔉_k` is a sum of
one Wilson term and `k` soft terms, so `D³𝔉_k` is the sum of Lemma NB-3's six families. (3) The
**1-derivative** families are Theorem N1-15's own terms: the maps `d, Q_2, r_j` are replaced by `d^Z, Q^Z_2,
r^Z_j`, whose ℓ¹ masses change by `(1 + O(ε))` and whose responses are supplied by (H3); the scalar
coefficients are `1 + O(ε²)`. Their exponents are therefore unchanged — `(d − θ_w^c − 2θ_A)k` for Wilson and
`(d − θ_w^r − 2θ_A)n + θ_w^r` for soft, **verified symbolically against NORMS §N7 by check na1-A (PASS, and
it is the control that makes the rest non-tautological)**. (4) The **3-derivative** and **0-derivative**
families are new. Each is bounded by (coefficient) × (one ℓ¹ leg) × (two sup legs) exactly as in N1-15's
steps (1)-(4), with the coefficient bounded by (H2) and the legs by (H3). Their exponents, computed from the
same five primitive ingredients plus (H2)'s two, are
  3-deriv Wilson `d − 4θ_w^c`; **0-deriv Wilson `d − θ_w^c − 3θ_A`**;
  3-deriv soft `(d − 4θ_w^r)n + 4θ_w^r`; **0-deriv soft `(d − θ_w^r − 3θ_A)n + θ_w^r`**
(check na1-B/C). At `(d, θ_w^c, θ_w^r, θ_A) = (4, 2, 3, 1)` these are `−4, −1, −8, −2`: all strictly
negative, so all four sum to a constant. (5) Summation as in N1-15 step (5). ∎

### A3.3 The three readings that matter

**(R1) `d = 4` marginality is NOT in the background terms.** Check na1-D: the four new families are
subcritical for `d < 8`, `d < 5`, `d < 12`, `d < 6` respectively. The **only** marginal family at `d = 4` is
the one Theorem N1-15 already carries — the 1-derivative Wilson vertex, critical dimension exactly `4`
(NORMS.md l.658-661: "the Wilson term is therefore exactly marginal, which is harmless only because it
occurs once"). The 1-derivative soft family is subcritical for `d < 5`, margin one power, as NORMS records.
**So (N-bg) does not introduce a `d = 4` marginality, and no route here needs `d < 4`.** This answers TF.

**(R2) (N-bg) inherits BFT-1's weight pair and asks LESS of it.** Substituting
`θ_A = min(1, θ_w^c − 1)` (NORMS.md l.656-657) into the two 0-derivative conditions gives (**post-hoc**,
derived after na1 ran): the 0-derivative Wilson family needs `θ_w^c > 7/4` and the 0-derivative soft family
needs `θ_w^r > 1`, against Theorem N1-15's `θ_w^c ≥ 2` and `θ_w^r > 2` (NORMS.md l.658-663). **At the
delivered pair `(2, d−1) = (2, 3)` the new families have margins `1` and `2` powers of `L`, against the
existing `0` and `1`.** So the answer to TB (c) is: (N-bg) needs **the same weight pair and no more**;
NORMS §N8's "must be stated as the pair" (NORMS.md l.697) is the whole requirement, at the background too.

**(R3) The background vertex costs a factor `(1 + Cε)`, and that is the same currency as lane B's
Theorem BGD.** BFT_B.md l.4529 ("the whole deviation of a background problem from the trivial one is
governed by the background **curvature**") and l.4552 (`e_l ≤ Cρ_{l+1}²f_k = CL^{−2(k−l−1)}f_k`, "no weight
penalty, no factor `k`") reach the same conclusion for the *algebraic* defects of the chain operators. §A3
reaches it independently for the *vertex*, from the Taylor expansion rather than from the operator algebra.
**Two independent routes to "the background is a relative `O(ε)`", on two different objects.**

### A3.4 What a hostile reviewer should attack first (and the one place the sign of my error is not safe)

1. **`Q^Z_2` must still carry no coboundary, and `Y'` must still be one.** If at a background the
   *quadratic* part `Y''_p` acquired a piece containing a covariant coboundary the estimate would only
   improve; but if the *linear* part `Y'_p` were NOT a covariant coboundary — i.e. if the response to
   level-k data entered `Y'` otherwise than through `d^Z` — the 1-derivative family would split off a
   0-derivative piece **with coefficient `W''(X) = 1 + O(ε²)`, not `O(ε)`**, whose exponent is
   `d − 3θ_A = 1` at `(4,1)`: **divergent, with no `ε` to suppress it.** This is the single assumption whose
   failure kills Theorem NB-4, and it is an identity about the ordered product round a plaquette, not an
   estimate. I have checked it by direct expansion (Lemma NB-3's proof) and no further.
2. **(H2) is BFT-1 at the maximal curvature weight.** Check na1-F corrupts exactly this ingredient and the
   gate then FAILS. If BFT-1 is only available at `θ_w^c = 0` — the weightless form Proposition COMP
   actually delivers via **(CL-3)** (PROOF.md l.6608-6610: own-units plaquette logs `≤ C_3(ε + η)` **at every
   level**, no scale weight) — then **check na1-E shows every new family goes positive and Theorem NB-4 is
   false.** So the theorem is not robust to weakening BFT-1; it is exactly as strong as BFT-1's weight pair.
3. **(H1)/(CL-4).** Corollary NB-2 needs the tower, not merely a composite critical point. PROOF.md
   l.6619-6625 names (CL-4) for exactly this.

*Anti-circularity, checked.* `ζ^c(V)` is the **composite** chain-minimiser map, not a product of per-level
Newton inverses, so BFT-0's anti-circularity clause (REVIEW_S22 l.432) is satisfied by construction, as it
is for Theorem N1-15 (NORMS.md l.502-506). The induction is well-founded: `C_♭^{(k)}` is produced from
objects available at step `k` of NAH-ind, not from itself.

---

## §A4 The reduction, and the verdict on NBG-F1 (TE)

### A4.1 (N-bg) reduced

Collecting §A2 and §A3:

> **Theorem NB-5 (reduction of (N-bg)): PROVEN-HERE as an implication.**
> **(N-bg) in its consumer form (§A1.1) follows from (H1) + (H2) + (H3) alone.** The vertex contributes
> nothing beyond a factor `(1 + Cε)` and an additive `C″ε`. In particular **(N-bg) imposes no exponent
> condition, no weight-pair condition, and no dimensional condition beyond those Theorem N1-15 already
> imposes at the trivial background.**

| input | what it is | status, by file:line |
|---|---|---|
| **(H1)** | the tower exists at `V` and is twice differentiable; "tower = composite critical point" | **OPEN**, named **(CL-4)**, PROOF.md l.6619-6625 |
| **(H2) curvature** | own-units level-j curvature of the chain `≤ C_0L^{−2(k−j)}ε` (BFT-1, `θ_w^c = 2`) | **PROVEN** for the linear chain (NORMS Lemma N1-4, l.267-280); **PROVEN-HERE** for the R^ax chain (BFT_B Theorem N2, l.3041-3060, l.3228: `f_j ≤ 2Λ_2f_k`, k-, T-, j-uniform, curvature-only, no global gauge); **OPEN** for the nonlinear critical chain (= BFT-1) |
| **(H2) soft** | own-units soft fluctuations `≤ C_0L^{−(d−1)(k−1−j)}ε` (`θ_w^r = d − 1`) | = **(C_g-θ) at θ = 1**, BFT_B l.2876-2879: **PROVEN-HERE** for the linear lift at every `0 ≤ θ ≤ 1` (Prop Cg-lin); first-order **PROVEN**, BCH remainder **ARGUED**, nonlinearly (Prop Cg-NL) |
| **(H3) M half** | `sup|f_0^Z| ≤ C_f sup|d^Z_kB_k|`, `sup|r^Z_{k−1}| ≤ C_R sup|d^Z_kB_k|` and the inter-level residual decay, k-, T-uniformly | = **(GAP-Z)**, BFT_B §41.5 (ii), l.4592: "a `k`-, `T`-uniform bound on the kernel of the gauge-fixed composite chain Hessian at `Z` — the `M` half … the genuinely new analytic input". **OPEN** |
| **(H3) locality, invariant half** | exponential locality of the background symbols `B_k ↦ f_0^Z`, `B_k ↦ r^Z_j` | **ARGUED** (Combes-Thomas with a scalar weight, BFT_B §41.5 (ii): "the scalar-weight computation is standard … **Not PROVEN, and explicitly not CONDITIONAL**") |
| **(H3) locality, variant half** | **(N-loc)** at the background: locality of the gauge-VARIANT representative of `ζ^c` | **OPEN**; = (CL-1)'s open half, the multi-scale axial gauge (NORMS.md l.426-435) |

### A4.2 NBG-F1: does NOT occur — and the confirmation is independent of lane B's route

RTARGET §54's **NBG-F1** asks whether (N-bg) and BFT-5's (G♯_0-field) are **not** the same obstruction.
**They are the same obstruction.** Theorem NB-5 reaches that conclusion **from the (N-bg) side**: after the
identity (§A2) and the vertex count (§A3), everything that is left in (N-bg) is a statement about the
**linear** response at the background, which is exactly `(GAP-Z) = (G♯_0-field)` moved off the trivial chain
(BFT_B l.4594, l.4737). Lane B reached the same identification **from the BFT-5 side**, by a different
argument (the algebraic-defect pricing of Theorem BGD plus the observation that (C-I) does not transport by
conjugation). **Two independent derivations of the same collapse**, so [S24-flag]'s collapse stands and the
obstruction count does not go back up.

*What §A3 adds that the lane-B route did not have:* lane B priced the transport of the **operator**
algebra; nobody had priced the transport of the **vertex**. A reviewer could have objected that the cubic
vertex, whose marginality at `d = 4` is the whole reason the trivial-background estimate is delicate, might
degrade at a background and introduce a second, independent `d = 4` obstruction. **Check na1-D answers that
objection with a margin: the new vertex families are subcritical through `d = 7`, `d = 4`, `d = 11` and
`d = 5` respectively** — i.e. the nearest of them (the 0-derivative Wilson family) is still subcritical at
`d = 4` with one power of `L` to spare.

### A4.3 The smallest remaining missing input, and a route to it that nobody has walked

The reduction leaves **(GAP-Z)** as the single genuinely new analytic input (everything else is either
already OPEN at the trivial background, or PROVEN for a sibling chain). Lane B prices (GAP-Z) as
**paper-scale** — LINEAR_PACKAGE §10's "propagator bounds at a general background [cf. CMP 95, 96, 99]".
Reading it against §A3, a cheaper route is visible and is **not** among the dead routes:

> **(HESS-rel) [named here; GAP].** There is `C < ∞` depending only on `(N, L, κ_±)` such that for every
> `k`, every torus and every `V` of the class, the difference of the composite chain Hessians
> `Hess𝔉_k(Z(V)) − Hess𝔉_k(1)` admits the **slot-wise** decomposition of BFT_B §41.2 (c) — `E = Σ_l e_l·𝒪_l`
> with `𝒪_l` the operator already present in that slot and `e_l ≤ CL^{−2(k−l−1)}f_k` — so that
> `‖E‖_{𝔐→Y} ≤ C f_k ‖Hess𝔉_k(1)‖_{𝔐→Y}` with **no weight penalty and no factor k**.

**Given (HESS-rel), (GAP-Z) follows from the FLAT `(G♯_0-field)` by a Neumann series**, since the weighted
pair `𝔐 → Y` is precisely the pair in which the flat chain Hessian is supposed to have an `O(1)` condition
number; the amplification that kills a naive perturbation argument (the chain Hessian's spectrum spans all
scales, so `‖𝓛‖·‖𝓛^{-1}‖ ≍ L^{2k}` in unweighted norms) is exactly what the weights remove. Then
**(N-bg) adds no paper to the programme: the paper is the flat `(G♯_0-field)`, which is already OPEN and
owned by lane A, and (N-bg)'s own residue is (HESS-rel), a session-scale item.**

*Status, honestly: this is a NAMED REDUCTION, not a proof, and it is the weakest thing in this file.*
Three reasons not to bank it:
1. BFT_B §41.2 (c) proves the slot-wise form for **two** defects (B1 exactness, B2 root covariance), not for
   the whole Hessian difference. The remaining pieces look benign — `W''(X_p) − 1 = O(ε²)` and
   `φ̂''(ρ) − 1 = O(ρ²)` are relative `O(ε²)` **slot-wise by inspection**, and the rest is the replacement of
   `d, Q` by `d^Z, Q^Z`, which is what B1/B2 price — but **I have not enumerated the difference term by
   term**, and that enumeration is the work.
2. BFT_B §41.5 (i) **PROVES** that the symbol route (analytic continuation of the momentum-space symbol,
   LINEAR_PACKAGE Theorem 4.2/4.2′) does **not** transport by conjugation. A Neumann series is a different
   device and is not refuted by that result — but lane B, which knows this material best, did not take it,
   and I do not know whether it declined it for a reason I have not seen.
3. (HESS-rel) needs the flat bound in the **weighted** pair, i.e. `(G♯_0-field)` itself, which is OPEN. So
   the reduction moves work rather than finishing it.

### A4.4 Outcome recorded against §A0.3

**Pre-registered outcome O1 occurs.** O2 (a new marginal term) and O3 (a divergent term) do **not** occur
at the delivered weight pair, and O3 **does** occur at `θ_w^c = 0` (check na1-E), which is why §A3.4 item 2
says the theorem is exactly as strong as BFT-1's weight pair and no stronger.

Pre-stated failure modes: **NBGA-F1 does NOT occur** (§A2). **NBGA-F2 OCCURS** (§A1.1 (q4): PROOF.md
l.6508-6511's localisation route needs `D³E` on a class LARGER than the small-field class). **NBGA-F3 is
live and is avoided only by using `N3`** (§A1.1 (q2), §A1.3). **NBGA-F4 OCCURS** (§A1.3: `𝔑` is `+∞`).
**NBGA-F5 is addressed by check na1-A**, the control that forces my ingredient table to reproduce NORMS §N7
before any new exponent is believed. **NBGA-F6 does NOT occur**, but see §A6 item 3: the consumer of
(N-bg) is the per-level route, and the composite route's own contraction condition **(CL-2)** needs the
Lipschitz constant of `Hess𝔉_k` — an explicit local functional — not of `Hess E_k^br`. So **D5's "(N-bg) is
the wall" is right about the obstruction and should be read as being about BFT-5/(GAP-Z), which is what it
collapses to.**

---

## §A5 Check record

**na1 (exponent bookkeeping).** Criteria `checks/na1_criteria.md` written **before** `checks/na1_exp.py`;
exact integer/`Fraction` arithmetic in plain python (`python3 -I`), no numpy, no sympy, no BLAS, no numeric
lock (brief rule 6). Script, criteria and output kept unaltered; output `checks/na1_out.txt`.

| clause | verdict |
|---|---|
| **na1-A** (CONTROL: the 1-derivative families must reproduce NORMS §N7 l.650-651 symbolically) | **PASS** |
| **na1-B** (the four new leading coefficients match the pre-registered expressions) | **FAIL** — see below |
| **na1-C** (at `(4,2,3,1)`: all four new coefficients `≤ −1`, 1-derivative Wilson `= 0`) | **PASS** (`−4, −1, −8, −2`; Wilson `0`) |
| **na1-D** (critical dimension of each new family `> 4`) | **PASS** (`8, 5, 12, 6`) |
| **na1-E** (DESIGNED-FAIL control at `θ_w^c = 0`) | **control PASSED**: na1-C reports FAIL there |
| **na1-F** (DESIGNED-FAIL control, P6 corrupted) | **control PASSED**: na1-C reports FAIL there |

**na1-B FAILED as pre-registered, and the fail is mine.** `na1_criteria.md` pre-registered the
3-derivative **soft** family's leading coefficient as `d − θ_w^r − 2θ_w^c − θ_A`. The computed value is
`d − 4θ_w^r`. The pre-registration was a transcription error: that family has **three residual legs**
(`φ̂'''(ρ)[ρ_1,ρ_1,ρ_1]`, all three legs entering through `r_j`), so it carries `θ_w^r` four times — once
from the coefficient and three times from the legs — and no `θ_w^c` at all. The other three
pre-registrations match exactly. **The criteria file is NOT edited** (brief rule 3); the error is recorded
here. It does not affect na1-C or na1-D, which test the *value* of the leading coefficient
(`−8`, subcritical through `d = 11`), not my prediction of its symbolic form; and it does not affect
Theorem NB-4, whose proof uses the computed form.

**What na1 can and cannot decide.** It decides exponents and nothing else. It cannot decide whether `ζ^c(V)`
obeys (H3) — that is (GAP-Z) — nor whether the critical chain obeys (H2), nor any constant. Its power
comes from two places: na1-A, which makes the ingredient table answerable to a previous session's published
table rather than to itself, and na1-E/na1-F, which show the gate is not vacuous: perturbing either the
weight or the background-curvature ingredient makes it fail.

---

## §A6 Tally

| item | status |
|---|---|
| **§A1.0** C_♭ is **three** distinct objects (C♭-I / C♭-II / C♭-III), pinned by file:line | **PROVEN-HERE** (a reading of existing files) |
| **§A1.0 (1)** SF's `ε_1` chain consumes (C♭-I) = N5-an♭'s constant, so **(N-bg) does not drive `ε_1`** | **ARGUED** (reading of SF.md l.2192-2195, l.2497-2499, l.2790-2800; for SF to confirm) |
| **§A1.0 (2)** NORMS §N8's BR1 and CURV1 rows are **false at level 0**, right at level `i ≥ 1` | **PROVEN-HERE** |
| **§A1.1** (N-bg) in consumer form: `N3`, chart at the lift, `∀k ∀T ∀V ∀A` | **statement** (adopted) |
| **§A1.2 (k1)** `C_♭^{(k)} = O(k)` suffices for the only live consumer (CURV-F2″ caps it at `O(1/k)` anyway) | **ARGUED** |
| **§A1.2 (k2)** full k-uniformity is binding only once CURV-F2″ is removed, which needs BFT-4 or the (H-G) remark route | **ARGUED** |
| **§A1.3** NORMS Definition N^F-2's vertex norm `𝔑` is **`+∞`** for every nonabelian consumer | **PROVEN-HERE**; one-line repair (`X ∈ S_k`); nothing in NORMS depends on it |
| **§A2 Lemma NB-1** the branch third-derivative identity at an arbitrary background | **PROVEN-HERE** (two independent derivations) |
| **§A2 Corollary NB-2** composite TOWER-VAR (d) at a nontrivial critical chain | **PROVEN-HERE** given (H1)/(CL-4) |
| **§A2** TOWER-VAR (d)'s stated reason is narrower than its true reason; the identity costs nothing at a background | **PROVEN-HERE** |
| **§A3.1 Lemma NB-3** the six vertex families; Lemma N1-1's "one derivative per term" is **FALSE** at a background | **PROVEN-HERE** |
| **§A3.2 Theorem NB-4** the background vertex is subcritical; `N3(D³E_k^br(V)) ≤ C_♭^∞` | **CONDITIONAL** on (H1), (H2), (H3) |
| **§A3.3 (R1)** `d = 4` marginality is **not** in the background terms (critical dims 8, 5, 12, 6) | **PROVEN-HERE** (check na1-D) |
| **§A3.3 (R2)** (N-bg) needs `θ_w^c > 7/4`, `θ_w^r > 1` — **weaker** than N1-15's `θ_w^c ≥ 2`, `θ_w^r > 2` | **PROVEN-HERE**, labelled **post-hoc** (derived after na1 ran) |
| **§A4.1 Theorem NB-5** (N-bg) ⟸ (H1) + (H2) + (H3), with no new exponent/weight/dimension condition | **PROVEN-HERE as an implication** |
| **§A4.2** **NBG-F1 does NOT occur**: (N-bg) and (G♯_0-field)/(GAP-Z) are one obstruction, confirmed from the (N-bg) side | **ARGUED**, independently of lane B's route |
| **§A4.3 (HESS-rel)** a named, session-scale route from the flat `(G♯_0-field)` to `(GAP-Z)` by a Neumann series | **GAP** — named, not proven; the weakest item in this file |
| **check na1** | A **PASS**, B **FAIL** (my pre-registration error), C **PASS**, D **PASS**, E and F **controls PASSED** |

**Unchanged OPEN after this file:** (CL-4); BFT-1 at the critical chain; (GAP-Z)/(G♯_0-field); (N-loc) and
its background version; (C_♭-eval); every clause of (H-C) other than C_♭. **Nothing in PROOF.md's tally
moves on this file**, and nothing here is a discharge: Theorem NB-4 is CONDITIONAL and Theorem NB-5 is an
implication.

---

## FOR OTHER FILES (not edited)

1. **NORMS.md — Definition N^F-2 (l.169-171), binding.** The vertex norm `𝔑_{l,m}` is `+∞` for every
   nonabelian `T = D³E_k^br`, by the file's own Ward identity at l.179-181 applied to a nested pure gauge
   (`‖d_lλ̂‖^{(1)} = 0` while `T(d_lλ̂, Y, W) ≠ 0`). **Repair: add "`X` in the composite slice `S_k`"**, as
   the BFT norm `𝔐` has it (REVIEW_S22 l.389-392, l.432). Theorem N1-15 is unaffected (it is stated and
   proved in `N3`). Reported because a reviewer comparing a future background N1-15 against `𝔑` would be
   comparing against a gate nothing can pass.
2. **NORMS.md — §N8's consumer table (l.688-689).** The Lemma BR1 and Lemma CURV1 rows should read "needs
   (N-bg) **at level `i ≥ 1`**". At level 0 the Lipschitz step is discharged by Lemma N5-an♭ alone (that is
   what BR1's own proof does, PROOF.md l.5870-5872) and the symbol `C_♭` in those rows is **(C♭-I)**, not
   the `C_♭^{(i)}` of (N-bg).
3. **NORMS.md — (N-bg)'s statement (l.629).** Restate at the strength the consumers impose: **"the
   `N_0`-Lipschitz constant of `Hess E_k^br` in the chart at the lift"** (PROOF.md l.6045, (I_i) (c); same
   words in (BG-unif) (iv), PROOF.md l.6098), not "on the small-field class". The two differ, and the
   second is strictly more than anyone has asked for. Add that the norm is **`N3`**, not `𝔑`.
4. **PROOF.md — Lemma TOWER-VAR (d) (l.6591-6594).** Its justification ("the linear branch, which is
   critical for the quadratic part") is the trivial-background special case of `F_AAa' + F_AB = 0`, the
   first derivative of criticality, which holds at **every** critical chain. **So TOWER-VAR (d) extends to
   a nontrivial background verbatim** (Corollary NB-2 here), and NORMS Remark N6-5's route (i)
   (NORMS.md l.630-634) pays nothing for the identity. Worth a one-line note, since the identity is the
   part of route (i) everyone expected to be hard.
5. **PROOF.md — NORM-F2's location (NORMS.md l.263-265).** Lemma N1-3's consequence says the Bianchi
   defect, the `Zd_2F` term and the Z-tails "return ONLY in the background extension (N-bg) … and that is
   where it must be re-examined". Sharpening: they return **inside (H3), i.e. inside (GAP-Z)**, and **not
   in the vertex**. Theorem N1-15's composite proof never uses `K_p(Z)` (its inputs are (I3), (I4), (I5),
   Lemma N1-7, Lemma N1-11), and neither does §A3's background version. So NORM-F2 is a question about the
   background *propagator*, not about the closed-input restriction on the vertex.
6. **BFT_B / lane B — offered, not claimed.** **(HESS-rel)** (§A4.3) would give `(GAP-Z)` from the flat
   `(G♯_0-field)` by a Neumann series in the weighted pair, making (N-bg)'s own residue session-scale
   rather than paper-scale. BFT_B §41.2 (c) already proves the required slot-wise, weight-free,
   factor-k-free form for the two algebraic defects (B1, B2); what is missing is the same statement for the
   **whole** Hessian difference. Two questions for lane B, which knows this material best:
   (a) is the remaining difference (`W''(X_p) − 1`, `φ̂''(ρ) − 1`, and the `d → d^Z`, `Q → Q^Z` replacement
   beyond B1/B2) slot-wise in the same sense? (b) **was a Neumann series considered and declined?**
   §41.5 (i)'s no-go is about conjugation and the symbol method, which a Neumann series does not use, but
   the absence of the attempt may mean there is an obstruction I have not seen.
7. **SF.md — for the T55-C symbol audit.** The `C_♭` in SF's `ε_1` chain (SF.md l.2192-2195, l.2497-2499,
   l.2790-2800) is **(C♭-I)**, Lemma N5-an♭'s analyticity constant of the *explicit* level-0 functional,
   whose open input SF itself names as **(C_♭-eval)**. It is **not** the `C_♭^{(i)}` of (N-bg)/(H-C). So
   **(N-bg) does not drive `ε_1`**, and the `ε_1` sweep (T55-B) and (N-bg) (T55-D) are disjoint. Three
   symbols share the name `C_♭`; the audit should split them (C♭-I / C♭-II / C♭-III, §A1.0).
8. **FLOW / SF — a question I could not settle, and it changes what (N-bg) is worth.** Failure mode
   CURV-F2″ caps `ε_unif` at `O(1/k)` *independently of* `C_♭` (PROOF.md l.6500-6507), so for the per-level
   route `C_♭^{(k)} = O(k)` is as good as `O(1)`. **Is `ε_unif = O(1/k)` acceptable to the flow?** The
   level-k curvature of an asymptotically free flow is itself `O(1/k)`, so the comparison is of constants,
   not of rates. If `O(1/k)` suffices, the per-level route's k-uniformity problem is a constant problem; if
   it does not, (N-bg) is only useful alongside a non-recursive (H-G).
9. **PROOF.md l.6508-6511 — the (H-G) remark route needs a LARGER class.** It needs, besides (C♭-II), the
   localisation of `∇E_i^br`, and its own text says "the interpolation that replaces far links **leaves the
   small-field class**". So the one route that turns (N-bg) into level-uniform (H-G) without BFT-4 needs
   `D³E` on a class **larger** than the small-field class — the opposite direction from §A1.1 (q3). That
   second class question is not part of (N-bg) as stated and should be named if the route is taken.
