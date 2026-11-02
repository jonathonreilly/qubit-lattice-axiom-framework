# TENTQ: the compensation charge (TENT-Q) / (NEUT-box) — session 25 (2026-10-28 UTC)

Scope of the whole file, stated once and binding on every claim in it: **m = 0, trivial background, 4D,
L = 3, θ > 0 as in the (Pl-c) class, the elliptic slice S_E (lead decision D1)**. Every status is one of
PROVEN-HERE / PROVEN as an implication / ARGUED / COMPUTED / CONDITIONAL (input named) / OPEN.

## 1. PRE-STATED (session 25) — statements only; the FIRST edit of this file, written 2026-10-28 14:01 UTC

This section is the first edit of TENTQ.md. It contains **statements only**. It cites nothing produced in
this session. Exploratory *reading* preceded it (DRIVE_BRIEF; HANDOFF; BFT_B §16.1-16.2, §24.0-24.1, §25.1,
§27.1-27.4, §31, §35, §36, §37-header; BFT_A §31.1, §36.0-36.1, §38.3-38.7; REVIEW_BFT_A_S8 Parts 4-6 and
its closing sections; SESSION24_RESULTS entries for REVIEW_BFT_A_S8, BFT_B s9, BFT_B s10; the scratch
scripts revA8/rev8_exact.py and revA8/rev8_psi.py) with exploratory reasoning that is not recorded; the only
claim §1 makes is file order. All inputs below enter as **named hypotheses**, quoted and not re-judged.

### 1.0 The object

For a chain source S with composite divergence D(S) := Ξ^TS (BFT_B §27.1), for every level-k site X:

    **Q_X(S) := ⟨χ^5_X D(S)⟩ = Σ_w χ^5_X(w) D(S)(w).**

Theorem NCE (ii) (BFT_B §36.5) says the whole of (NC-Γ) for Γ_E off the critical set reduces to this one
scalar per level-k box, appearing twice: (a) as the (P0)-slot size of the slice correction Γ_E^TD(S) via
Lemma ΓT-op (e), and (b) as the root charge of Proposition COF-res paired against the response's level-k
funnel Φ_k(Y^p_{*,0})(c_X) = Proposition TE's tent coefficient. The two faces are named **(NEUT-box)** and
**(TENT-Q)**.

### 1.1 Targets of this session (written before any derivation)

- **T1 (global neutrality).** Decide whether Σ_X Q_X(S) = 0 identically, for every chain source S, with no
  hypothesis on S beyond being a chain source. Expected: **TRUE** (the two inputs are Σ_X χ^5_X = 1, BFT_B
  §16.1 (b), and Σ_z D(S)(z) = 0, BFT_B §36.1 / Lemma DF (iii)). If true, state it as a proposition and say
  exactly what it buys: Σ_X Q_X δ_{c_X} is a **neutral** charge distribution on the level-k root lattice.
- **T2 (boundary-term form).** Decide whether each individual Q_X(S) is a boundary term, i.e. whether it can
  be written as a pairing in which every term carries at least one difference of χ^5 and is therefore
  supported only on the collar where χ^5_X is not locally constant. Targets, in order:
  (a) the exact summation-by-parts identity for Q_X in terms of the *slots* of S (level-l 1-forms), not of
      D(S);
  (b) from (a), whether Q_X vanishes identically (expected: **NO**, lane B's §25.1 (e) bb8t C1 records the
      term as "real and grows like n^d", and §25.1 (f) gives a nonzero exact total variation);
  (c) if it does not vanish, whether its support is the collar and what the exact collar weight is.
- **T3 (the price, done explicitly).** With T1 and T2, price the (TENT-Q) functional
      𝒯_p(S) := n² Σ_X Q_X(S) · Φ_k(Y^p_{*,0})(c_X)
  explicitly, in two steps: (i) replace the naive bound n²·Σ_X|Q_X|·max|Φ_k| by the **neutral** bound
  obtained from T1 (a level-k discrete integration by parts against a flux potential for Q), so that only
  **differences of Φ_k between neighbouring level-k boxes** enter; (ii) evaluate the resulting factor on the
  exact tent data of REVIEW_BFT_A_S8 S8-7 (φ_1 = -1/432, φ_2 = -17/104976, ratio 17/243, ψ_u = -65/26244 at
  k = 2), **re-derived in this session with the rev8 machinery and not merely quoted**, and state whether the
  product is k-uniform or whether, and by exactly which power of L, it is not.
- **T4 (the pin).** Read Lemma ΓT-op (e) (BFT_B §24.1, §25.1 (e)) and decide whether the appearance of the
  compensation charge at the **pinned** site c_X is forced by the slice S_E or is a normalisation choice in
  the box potential. Specifically: decide whether the pin λ^E_X(c_X) = 0 of BFT_B §16.1 (c) can be replaced
  by a different normalisation of the same minimiser (e.g. ⟨λ^E_X⟩ = 0 on Ñ_X, or a χ^5-weighted mean) without
  changing Γ_E, Π_E, S_E or any gauge-invariant output; and, if it can, what the second term of Lemma ΓT-op
  (e) becomes. Record which of Γ_E's *proven* properties (16.1 (c) ev^{(k)}Λ = 0, 16.1 (d) Π_E idempotent,
  16.1 (e) Ker, Proposition GT-split's pointwise form) depend on the pin.
- **T5 (status).** State what is left of (TENT-Q) and of (NC-Γ) for Γ_E off the critical set after T1-T4,
  with an honest status, and say plainly if a target was not reached.

### 1.2 Pre-registered failure modes

- **TQ-F1.** Σ_X Q_X(S) ≠ 0 for some chain source S (T1 fails). Expected: **does not occur**.
- **TQ-F2.** Q_X(S) = 0 for every X and every chain source S, i.e. the obstruction is empty. Expected:
  **does not occur** (if it did occur, (TENT-Q) and (NEUT-box) would both be vacuous and Theorem NCE (ii)
  would close off the critical set; this is the one outcome that would be a proof rather than a reduction).
- **TQ-F3.** The boundary-term form of T2 exists but the collar weight carries a **positive** power of n, so
  that the summation-by-parts gains nothing against the naive bound. Expected: **OCCURS in ℓ^∞ against the
  current's sup** (the total variation of a partition of unity over a box of ≍ n^d sites is an n^{d-1} count,
  which is exactly the n^{d-1} = n³ that (NEUT-box) as derived in BFT_B §36.4 asks to be beaten), and
  **does not occur** against the current's own ℓ¹ norm. If both halves of this expectation hold, the honest
  conclusion is that (NEUT-box) is a statement about which **currency** the source is measured in, not about
  cancellation — and that is a result, not a failure.
- **TQ-F4.** The neutral bound of T3 (i) is unavailable because no level-k flux potential for Q with a
  controlled ℓ¹ norm exists on the torus (the level-k lattice is 4-dimensional, so a neutral charge has a
  potential, but its ℓ¹ norm may grow with the torus side T). Expected: **OCCURS for a generic neutral Q**,
  and the useful statement is therefore local: a bound in terms of Σ_X|Q_X| times the **oscillation** of Φ_k
  over the support of Q, or a bound in terms of a potential supported where Q is. State which.
- **TQ-F5.** The pin of T4 is forced, i.e. some proven property of Γ_E breaks under every other
  normalisation. Expected: **partially occurs** — the pin is what makes Λ(x)(c_Y) = 0 and hence
  Proposition GT-split pointwise, so moving it cannot be free; the question is whether the cost is a
  different term of the same size or a smaller one.
- **TQ-F6.** (TENT-Q) and (NEUT-box) are *not* the same scalar after all (Theorem NCE (ii)'s identification
  is wrong), e.g. because the (P0)-slot face uses max_X|Q_X| while the tent face uses the signed sum
  Σ_X Q_X Φ_k(c_X), and the second can vanish while the first does not. Expected: **OCCURS as a
  distinction** — the two faces are the same *scalar family* {Q_X} but not the same *functional of it*, and
  T1 makes the difference sharp, because T1 kills the signed sum's constant mode and not the max. If so,
  say so, because it changes what has to be proven.

### 1.3 Pre-registered process commitments

- Any numeric check gets `checks/tq1_criteria.md` written **before** its script, containing no constant
  derived in this session. All arithmetic is exact (`fractions.Fraction`), plain python, single thread, no
  BLAS, no numeric lock.
- A FAIL is reported as a FAIL, script and output kept unaltered; a re-run uses a new id with the criteria
  untouched; anything run after seeing a result is labelled **post-hoc**.
- Load-bearing cited mathematics is **rebuilt** here, not cited: in particular the funnel weights h_i, the
  straight average Q_str, Φ_k and the exact tent values of REVIEW_BFT_A_S8 S8-7 are recomputed in this
  session's own script before being used in any estimate.
- This file is append-only. No other lane file is edited; requests go in a final
  "## FOR OTHER FILES (not edited)" section.

## 2. Proofs (appended after §1 (14:02:12 UTC), after `checks/tq1_criteria.md` (14:12:45 UTC) and after `checks/tq1_charge.py` (14:14:28 UTC) ran to completion (output 14:25:02 UTC, ALL PASS))

Notation, fixed as in the criteria file: n = L^k, d = 4, L = 3; level-l roots at off(l) + L^lZ^d,
off(l) = (L^l − 1)/2; σ_5, χ^5_X as in BFT_B §16.1 (b), §24.0; (d*v)(z) = Σ_μ[v(z − e_μ, μ) − v(z, μ)], so
⟨d*v, f⟩ = ⟨v, df⟩ (BFT_A §23.1); D(S) = Σ_{0≤l≤k−1} ev^{(0→l)T}d*S_l (BFT_B §27.1, with ev^{(0→0)} = id);
π_l(S_l) = L^{3(k−l)}sup_own|S_l| (BFT_B §27.1); Q_X(S) = ⟨χ^5_X, D(S)⟩ (BFT_B §36.5 (ii)).

### 2.0 Scope note on the gauge fibre, and why an abelian model is COMPLETE here (not vacuous)

Every operator appearing in §2 — multiplication by χ^5_X, d, d*, ev^{(0→l)} and its transpose, the funnel
weights h_i, the straight average Q_str, λ^E_X and Λ — acts **componentwise on su(N) in an orthonormal
basis** at the trivial background: BFT_B §24.0 ("All maps act componentwise on su(N) (orthonormal basis)")
and §16.1 (f) ("Π_E acts identically and linearly on each su(N) component … and a constant Ad is a constant
orthogonal matrix on these components, so they commute"). Every statement of §2 is **linear with scalar
coefficients in the fibre**. Therefore a scalar (abelian) exact model is a **complete** test of these
identities, not a vacuous one, and the nonabelian content of the problem sits entirely in (i) the structure
of the source, D(S) = −K′^T_x∇(𝔉_k∘exp)(x; B) (BFT_A Lemma CD), which is taken as a named input and never
unpacked here, and (ii) the background, which §2.9 (c) addresses separately.

**Where this stops, stated plainly.** At a **nontrivial** background the analogous statements are *not*
fibre-componentwise and an abelian model would be vacuous for them: see §2.9 (c), where Proposition QN is
shown to be a **trivial-background statement** that fails at a background by exactly a holonomy defect.
(BFT_B session 11 §43.1 records that the abelian model of bb9b/bb10 is vacuous for every one of its §41
statements; that warning applies to background statements, and §2 makes none.)

### 2.1 Proposition QN (global neutrality of the box charges): PROVEN-HERE

*Statement.* For **every** chain source S (no hypothesis: not composite-co-closed, not (CC-0), not of any
source class), **Σ_X Q_X(S) = 0**, the sum over all level-k sites X of the torus.

*Proof.* Σ_X Q_X(S) = ⟨Σ_X χ^5_X, D(S)⟩ = ⟨1, D(S)⟩ by the partition of unity Σ_X χ^5_X = 1
(BFT_B §16.1 (b), re-verified exactly as tq1 A4). For each slot, ⟨1, ev^{(0→l)T}d*S_l⟩ = ⟨1, d*S_l⟩ because
ev^{(0→l)T} places a level-l function on **distinct** level-0 sites (BFT_B §29.1 (a)); and
⟨1, d*S_l⟩ = ⟨d1, S_l⟩ = 0 on the torus. Summing over l gives 0. ∎

*What it buys, and what it does not.* The level-k root-charge field Σ_X Q_X δ_{c_X} — which by Theorem NCE
(ii) is exactly D(S^E_0(S)) = I_χ^TD(S) — is **neutral**. Hence in the (TENT-Q) functional
n²Σ_X Q_X Φ_k(Y^p_{*,0})(c_X) the tent coefficient may be replaced by Φ_k − c for **any** constant c: the
constant mode of the tent coefficient is annihilated identically. §2.5 decides what that is worth.
It does **not** make the individual Q_X vanish (§2.2), and it is not new mathematics: it is
Σ_X χ^5_X = 1 combined with the ΣD(S) = 0 that BFT_B §36.1 already uses. It is stated here because §36.5's
display of (TENT-Q) and §36.4's display of (NEUT-box) both quantify over max_X|Q_X| and over the **signed**
sum without recording that the signed sum has a null direction. **TQ-F1 does not occur** (tq1 A1, exact, two
models).

### 2.2 Proposition QSBP (the summation-by-parts form of the box charge): PROVEN-HERE

*Statement.* For every chain source S and every level-k site X,

  **Q_X(S) = Σ_{l=0}^{k−1} ⟨ d(ev^{(0→l)}χ^5_X) , S_l ⟩**   (★)

— the box charge is **not** an average of D(S) over the box; it is the pairing of each source slot with the
**level-l differential of the restricted tent**, i.e. a weighted boundary flux of the source itself.

*Proof.* Q_X(S) = Σ_l ⟨χ^5_X, ev^{(0→l)T}d*S_l⟩ = Σ_l ⟨ev^{(0→l)}χ^5_X, d*S_l⟩ (adjointness of the
placement, BFT_B §29.1 (a)) = Σ_l ⟨d(ev^{(0→l)}χ^5_X), S_l⟩ (d^T = d*, BFT_A §23.1). ∎
(tq1 A2: exact for **every** X, in d = 2 and d = 4, k = 2.)

This is BFT_B §25.1 (f)'s identity Q_X(D(j)) = ⟨d ev χ^5_X, j⟩ extended from a single-level source to the
full composite divergence; the extension is the two lines above.

**(a) Q_X does not vanish: TQ-F2 does NOT occur, with an exact configuration.** Take the single-slot source
S_l := c·sign(d(ev^{(0→l)}χ^5_X)). Then by (★) and the exact total variation of BFT_B §25.1 (f)
(re-verified independently here as tq1 A3, at l = 0, 1, 2 and in d = 2 and d = 4),

  **Q_X(S) = c·‖d(ev^{(0→l)}χ^5_X)‖_1 = c·2d(n/L^l)^{d−1} = 8c·L^{3(k−l)}  (d = 4),**

which is nonzero for every k and every l. So neither route 1 of the brief's hoped-for outcomes holds:
**Q_X is not identically zero and does not reduce to a vanishing boundary term.** It *is* a boundary term —
every term of (★) carries one difference of χ^5 — but the boundary term does not vanish; it is a flux
through the tent's collar with the explicit weight |dχ^5_X| ≤ (15/8)/n per direction (|σ_5′| ≤ 15/8,
BFT_B §16.1 (b)).

**(b) The exact k- and T-uniform bound, with an absolute constant.** From (★), the total variation of
§25.1 (f), and π_l(S_l) = L^{3(k−l)}sup_own|S_l|:

  |Q_X(S)| ≤ Σ_l ‖d(ev^{(0→l)}χ^5_X)‖_1·sup_own|S_l| = Σ_l 2d·L^{3(k−l)}·L^{−3(k−l)}π_l(S_l)
  **= 2d Σ_{l=0}^{k−1} π_l(S_l) = 8 Σ_l π_l(S_l)**,

and in the (P0) + (Pl-c) classes **|Q_X(S)| ≤ 8[‖S^c_0‖_∞ + (1 − L^{−θ})^{−1}‖S‖_{Pc}]**, uniformly in k, T
and X, with the **absolute** constant 8 = 2d. By (a) the inequality is **attained**, so no better bound in
these norms exists.

*The mechanism, in one line.* The L^{3(k−l)} of the tent's total variation cancels **exactly** against the
own-unit-to-coarse-unit conversion L^{−3(k−l)} of the plain slot. That cancellation is why the charge is
O(1): it is a currency identity, not a cancellation in the data.

### 2.3 Proposition QFALSE: (NEUT-box), as stated in BFT_B §36.4, is FALSE — by exactly L^{2k}. PROVEN-HERE

*(NEUT-box) as derived in §36.4:* max_X|⟨χ^5_X D^⊥(S)⟩| ≤ C·n·‖D^⊥(S)‖_∞.

*Statement.* There is no such C, uniform in k: for every k there is a Setting-LIN source in the (P0) class
for which the ratio is ≥ n² = L^{2k}.

*Proof.* Take the level-0-only source j_0 := c·sign(dχ^5_{X_0}) of §2.2 (a) (zero where dχ^5_{X_0} = 0, hence
supported in N_{X_0}). By §2.2 (a), Q_{X_0}(j_0) = 8c·n³ exactly. On the other side, D = d*j_0 and a
divergence of a 1-form with sup c obeys ‖D‖_∞ ≤ 2d·c = 8c. The level-k-root part changes nothing:
Q_{X_0}(D^⊥) = Q_{X_0}(D) − D(c_{X_0}) ≥ 8cn³ − 8c. Hence

  max_X|⟨χ^5_X D^⊥⟩| / (n‖D^⊥‖_∞) ≥ (8cn³ − 8c)/(8c·n) = n² − 1 = **L^{2k} − 1**. ∎

*Reading, and it is the session's first finding.* The obstruction §36.4 isolates is a **currency mismatch,
not a cancellation failure** — exactly the session-24 pattern the handoff names. (NEUT-box) asks the box
charge to be smaller than ‖D‖_∞ by n^{d−1} = n³; the charge is in fact bounded by the **coarse plain norms
of the source slots** with constant 8 (§2.2 (b)), and ‖D‖_∞ is a **different** currency: for a level-0-slot
source, ‖D‖_∞ ≍ n^{−3}π_0(S_0) while |Q_X| ≍ π_0(S_0). The two differ by n³, of which (NEUT-box) grants one
power. **Nothing can repair (NEUT-box) as written**, because §2.2 (b)'s bound is attained; what has to
change is the route, not the constant.

### 2.4 Proposition PINC (the pinned compensation charge cancels identically in the pairing): PROVEN-HERE given Lemma ΓT-op (a)

*Statement.* Let φ be any level-0 function and x any chain. With the B/P split of BFT_B §25.1 (f),
Γ_E^Tφ = B + P, B := −Σ_X Σ_w χ^5_X(w)φ(w)A^X_w, P := Σ_X Q_X(φ)A^X_{c_X}, one has, writing
γ_X := ⟨A^X_{c_X}, x_0⟩:

  **⟨P, x_0⟩ = Σ_X Q_X(φ)·γ_X   and   ⟨B, x_0⟩ = −Σ_X Q_X(φ)·γ_X + ⟨φ, Λ(x)⟩,**

so **the whole contribution of the pinned compensation charge to the pairing ⟨Γ_E^Tφ, x_0⟩ = ⟨φ, Λ(x)⟩
cancels identically against the corresponding piece of the bulk term.** Equivalently, Γ_E^Tφ is, in one
piece and with no pinned term at all,

  **Γ_E^Tφ = −Σ_X Σ_w χ^5_X(w)φ(w)·(A^X_w − A^X_{c_X}),**  a sum of box **dipole** fields.

*Proof.* Lemma ΓT-op (a) (BFT_B §25.1 (a), PROVEN-HERE there) with ψ = δ_w gives
(λ^E_X)^Tδ_w = −A^X_w + A^X_{c_X}, hence λ^E_X(x)(w) = ⟨(λ^E_X)^Tδ_w, x_0⟩ = γ_X − ⟨A^X_w, x_0⟩, i.e.
⟨A^X_w, x_0⟩ = γ_X − λ^E_X(x)(w). Substituting into B,
⟨B, x_0⟩ = −Σ_XΣ_wχ^5_X(w)φ(w)[γ_X − λ^E_X(x)(w)] = −Σ_X Q_X(φ)γ_X + ⟨φ, Σ_Xχ^5_Xλ^E_X(x)⟩, and
Σ_Xχ^5_Xλ^E_X(x) = Λ(x) = Γ_E x by definition (BFT_B §24.0). Adding ⟨P, x_0⟩ = Σ_XQ_X(φ)γ_X gives
⟨Γ_E^Tφ, x_0⟩ = ⟨φ, Λ(x)⟩, which is Lemma DF (i). The one-piece form is the same substitution read
backwards, using Σ_wχ^5_X(w)φ(w) = Q_X(φ). ∎

*Answer to the question "can the pin be moved", in two halves.*
**(i) The pin itself is FORCED — TQ-F5 occurs.** λ^E_X is the minimiser of ‖x_0 + d_Xλ‖² on Ñ_X, unique
**modulo constants** (BFT_B §16.1 (a)); the normalisation λ^E_X(c_X) = 0 is what gives Λ(c_Y) = 0 for every
Y, hence ev^{(k)}Λ = 0, hence **Π_E x − x = DΛ ∈ 𝒢_0** — the statement that Π_E moves x along the composite
gauge orbit **without touching the data** (BFT_B §16.1 (c)). Replacing the pin by any other normalisation
(⟨λ^E_X⟩_{Ñ_X} = 0, a χ^5-weighted mean, …) shifts Λ by Σ_Xχ^5_Xa_X(x) with a_Y(x) ≠ 0 at the roots, so
ev^{(k)} of the shifted Λ is nonzero and the shifted Π_E is not a projection along 𝒢_0 at all: S_E would no
longer be a slice of the composite gauge orbit. It also destroys Proposition GT-split's pointwise form,
which is exactly Λ(x)(c_Y) = 0 (BFT_B §36.1). **So the pin is not an incidentally-fixed parameter; it is
constitutive of S_E.**
**(ii) It does not matter, because the pinned charge is not an obstruction.** By the statement above, the
pinned term's entire effect on every pairing is nil. Lemma ΓT-op (e)'s second term — "the only one that is
not O(n‖φ‖_∞)" — is a property of the **ℓ^∞ norm** of Γ_E^Tφ, which is genuinely of order n^d: bb8t C1
attains (2n + 1)^4·0.125 at φ = 1_{N_X}, and that φ has Q_X = ⟨χ^5_X⟩ = n^d (tq1 A4, exact), so the
measurement and the bound agree and the ℓ^∞ norm really is that large. The pairing it is used to bound is
not. **Hölder is being applied at the wrong place.**

*Consequence for route (ii) of §36.4 (Proposition GT-ell): it is dead as a route, independently of
(NEUT-box).* Even granting (NEUT-box), GT-ell's **first** term is already 2.5·5^dC_YN·n⁴‖D^⊥(S)‖_∞, and for
a level-0-slot source in the (P0) class n⁴‖D‖_∞ ≍ 8n·π_0(S_0) — one power of n above the class norm. So the
ℓ^∞×ℓ¹ route loses a power of n in its *leading* term whatever the box charges do. Combined with §2.3
((NEUT-box) false by L^{2k}) and with the identical cancellation above, the honest conclusion is:

> **(NEUT-box) should be WITHDRAWN as an open item, not attempted.** It is false as stated (§2.3), it is
> not necessary (the pinned charge cancels in every pairing, so the quantity it bounds is an artefact of
> taking ‖Γ_E^Tφ‖_∞ before pairing), and it is not sufficient (GT-ell's first term already loses n). The
> ℓ^∞×ℓ¹ route is **not a second route**: it is route (R2)/Proposition NCR with a lossy intermediate step.

### 2.5 Theorem TQ-INT (the tent-interpolation reduction of (TENT-Q)) and Corollary TQ-osc: PROVEN-HERE

*Statement (TQ-INT).* Let Φ be **any** level-k function and 𝒯_p(S) := n²Σ_X Q_X(S)·Φ(c_X). Put
Ψ := I_χΦ = Σ_X Φ(c_X)χ^5_X, the quintic-tent interpolation of Φ (BFT_B §16.14's I_χ). Then

  **𝒯_p(S) = n² Σ_{l=0}^{k−1} ⟨ d(ev^{(0→l)}Ψ) , S_l ⟩.**

*Proof.* Multiply (★) by Φ(c_X), sum over X, and use linearity of ev^{(0→l)} and d. ∎
(tq1 A5: exact in d = 2 and d = 4, with **pseudo-random** Φ, so nothing is tuned.)

With Φ := Φ_k(Y^p_{*,0}) this is Proposition COF-res's residue (BFT_B §35.7). **So (TENT-Q) is not a sum of
box charges against tent coefficients at all: it is a single pairing of each source slot against the
gradient of one scalar field — the tent interpolation of the tent coefficient.** The box charges, and with
them the whole "one scalar per level-k box" formulation, are **eliminated**.

*Lemma TENT-TV (the tent's total variation with the constant mode removed): PROVEN-HERE.* For every level-k
function Φ, every 0 ≤ l ≤ k and every constant c,
  **‖d(ev^{(0→l)}Ψ)‖_1 ≤ 2d(n/L^l)^{d−1}·Σ_X|Φ(c_X) − c|,**
and, per direction and pointwise, writing z for the level-0 avatar of a level-l site,
  d(ev^{(0→l)}Ψ)(z, μ) = Σ_τ w_τ(z)·δ_μ(z)·[Φ(c_{X^+_μ,τ}) − Φ(c_{X^-_μ,τ})],  w_τ ≥ 0, Σ_τ w_τ = 1,
  |δ_μ(z)| ≤ 15/(8n),
where τ runs over the transverse root choices and X^±_μ,τ are the two μ-adjacent level-k roots.
*Proof.* Ψ − c = Σ_X(Φ(c_X) − c)χ^5_X by Σ_Xχ^5_X = 1, and d(ev^{(0→l)}(Ψ − c)) = d(ev^{(0→l)}Ψ); apply the
triangle inequality with §25.1 (f)'s exact total variation per box. For the pointwise form, factorise
χ^5_X = Π_νσ^{(ν)}_5: in direction μ only the μ-factor differs, the transverse factors are ≥ 0 and sum to 1
over τ, and for each fixed τ the two μ-adjacent roots have **exactly opposite** μ-differences because
σ_5(t) + σ_5(1 − t) = 1 (BFT_B §16.1 (b)); |σ_5′| ≤ 15/8 and the coarse step is 1/n. ∎

*Corollary TQ-osc.* If supp S lies in one coarse cell, so that the level-k boxes seeing it are the ≤ 2^d
boxes 𝔅 of that cell, then with c the mean of Φ over 𝔅,

  **|𝒯_p(S)| ≤ 2^d·2d·n²·osc_𝔅(Φ_k(Y^p_{*,0}))·Σ_{l}π_l(S_l) = 128·n²·osc_𝔅(Φ_k)·Σ_lπ_l(S_l)** (d = 4),

and for a general source one sums over coarse cells. Hence

> **(TENT-Q) ⟸ (TENT-osc): n²·osc_𝔅(Φ_k(Y^p_{*,0})) ≤ C, uniformly in k, T, p and 𝔅** — one scalar
> inequality on the **response field alone**, with no source, no charge and no support question in it.

### 2.6 Proposition TQ-NOGAIN: the gain from neutrality is a constant, not a power of L. PROVEN-HERE + COMPUTED

*Statement.* The only effect of Proposition QN on (TENT-Q) is to replace max_X|Φ_k| by
osc_𝔅(Φ_k) (Corollary TQ-osc). For the Φ_k that occurs this is a bounded factor, not a power of L:
**if Φ_k(v) vanishes at some level-k root of 𝔅 — which it does whenever v is supported in a proper subset
of the blocks that 𝔅 covers — then osc_𝔅(Φ_k(v)) = max_𝔅|Φ_k(v)| exactly.**

*Proof.* osc over a set containing a zero of Φ_k equals max|Φ_k| on that set. Φ_k(v)(c_X) =
Σ_{i<k}ev^{(i+1→k)}h_i(Q_str^{(0→i)}v)(X) reads v only on the level-k block of X (h_i averages integrals
along axial paths **inside** a level-(i+1) block, BFT_B §27.1; Q_str averages inside blocks), so
Φ_k(v)(c_X) = 0 for every X whose level-k block misses supp v. ∎

*COMPUTED confirmation, and it is a negative for this session's own preferred route.* tq1 A8 (exact, d = 4,
k = 2, u = ⅛d*δ_p the admissible source of REVIEW_BFT_A_S8 S8-7 placed at c_X + (1,0,0,0)):
Φ_2(u)(c_X) = −65/26244 and Φ_2(u) = **0 exactly at all eight one-coarse-step neighbours**, so
max one-step difference / max = **1 exactly**. The funnel of a compactly supported field lives in one box.

> **Route 1 of the brief is therefore settled negatively, and sharply.** Q_X is globally neutral (§2.1), it
> is exactly a boundary term (§2.2), and neither fact reduces (TENT-Q) by any power of L. Global neutrality
> buys the constant mode and nothing more. **(NEUT-box) is not the statement "that boundary term vanishes"**
> — the boundary term is nonzero, bounded by 8Σ_lπ_l(S_l) and attained.

### 2.7 Proposition TGAUGE (the tent coefficient is not intrinsic — and its removal is free of charge only in bookkeeping): PROVEN-HERE

*Statement.* For every level-0 function μ and every level-k site X,
  **Φ_k(x_0 + dμ)(X) − Φ_k(x_0)(X) = A^{(0→k)}μ(X) − μ(c_X),**
where A^{(0→k)}μ(X) = L^{−dk}Σ_{s∈[0,L^k)^d}μ(L^kX + s) is the average of μ over the level-k block of X.
In particular, for μ ∈ Λ_* (μ = 0 at the level-k roots, so that Ξμ ∈ 𝒢_0) the change is exactly the block
average A^{(0→k)}μ, which can be prescribed arbitrarily. **Hence one can choose a representative within the
composite gauge orbit for which Φ_k(Y^p_{*,0}) ≡ 0, or ≡ any constant; with Proposition QN the second choice
makes Proposition COF-res's residue vanish identically.**

*Proof.* Q_str∘d = d∘A one step: for v = dμ, (Q_str dμ)(Y, m) = L^{−d}Σ_{r∈[0,L)^d}[μ(LY + r + Le_m) −
μ(LY + r)] = A μ(Y + e_m) − Aμ(Y), because the telescoping of the straight line of L links leaves only its
two ends and Σ_rμ(L(Y + e_m) + r) = L^dAμ(Y + e_m). Iterating, Q_str^{(0→i)}dμ = d(A^{(0→i)}μ). Next,
h_i(dν) = A_iν − ev^{(i+1)}ν (the block mean minus the root value) — the identity
h_0(dλ) = (mean of λ over the L^d offsets) − λ(root), which REVIEW_BFT_A_S8 verified exactly and which is
re-verified here, at every level, through A6. Therefore
Φ_k(dμ)(X) = Σ_{i<k}ev^{(i+1→k)}[A^{(0→i+1)}μ − ev^{(i+1)}A^{(0→i)}μ](X) = Σ_{i<k}[Ā_{i+1}(X) − Ā_i(X)],
Ā_j(X) := the average of μ over the level-j block centred at c_X, Ā_0(X) = μ(c_X). The sum telescopes to
Ā_k(X) − μ(c_X). ∎ (tq1 **A6**: exact, d = 4, k = 2, pseudo-random μ and pseudo-random x_0, value
−17600766949/4728643920 on both sides; linearity also checked.)

*What this does and does not buy. ARGUED for the second half.* It buys the structural fact that the tent
coefficient is a **representative artefact**, not an invariant: Proposition COF-res's residue is not a term
of f_0 but a term of one particular bookkeeping of f_0. It does **not** buy a smaller bound. Changing
Y^p_{*,0} by dμ changes the main pairing of Theorem COF step (c) by ⟨Σ_l(Q_str^{(0→l)})^Tĵ_l, dμ⟩ =
Σ_l⟨ĵ_l, d(ev^{(0→l)}μ)⟩ (using d*(Q_str^{(0→l)})^T = ev^{(0→l)T}d*, BL-2 (c) transposed), and a μ with
A^{(0→k)}μ = −Φ_k has own sup ≍ max|Φ_k| and may be taken smooth on the coarse scale, so
‖d(ev^{(0→l)}μ)‖_1 ≍ L^{3(k−l)}max|Φ_k| — the **same** L-power as Lemma TENT-TV, hence the same bound
n²·max|Φ_k|·Σ_lπ_l(S_l). This is as it must be: f_0 is gauge-invariant, so no representative choice changes
the true size. *ARGUED*, because the cost estimate uses a smoothness choice for μ that is natural but not
forced, and no μ is constructed explicitly here.

### 2.8 Theorem TQ (what (TENT-Q) is, after §2.1-§2.7): assembled

**(i) PROVEN-HERE.** For every chain source S, every level-k function Φ and every representative:
  𝒯_p(S) = n²Σ_l⟨d(ev^{(0→l)}I_χΦ), S_l⟩, with |𝒯_p(S)| ≤ 128·n²·osc_𝔅(Φ)·Σ_lπ_l(S_l) per coarse cell
(Theorem TQ-INT, Lemma TENT-TV, Corollary TQ-osc). The constant 128 = 2^d·2d is absolute; nothing in it
depends on k, T, p or N.

**(ii) PROVEN-HERE.** Σ_X Q_X(S) = 0; Q_X(S) = Σ_l⟨d(ev^{(0→l)}χ^5_X), S_l⟩; |Q_X(S)| ≤ 8Σ_lπ_l(S_l),
attained. So the charge itself is **O(1) in the source's own currency, k- and T-uniformly**.

**(iii) The deficit, COMPUTED and named.** With the **own-unit funnel gain** of the exact computation
rebuilt here (tq1 A7: φ_1 = −1/432, φ_2 = −17/104976, ratio 17/243, ψ_u = −65/26244 for u = ⅛d*δ_p with
sup_own|u| = 1/8, so |Φ_k(u)|/sup_own|u| = 8·65/26244 = **130/6561 = 0.019814**, k-independent), and with
sup_own = n^{−1}·‖·‖^c_∞,

  **n²·osc_𝔅(Φ_k(Y^p_{*,0})) ≍ 0.0198·n²·sup_own|Y^p_{*,0}| = 0.0198·n·‖(Y^p_*)^c_0‖_{∞,loc}.**

So **(TENT-Q) is short of k-uniformity by exactly one power of n = L^k, times the same unknown
‖(Y^p_*)^c_0‖_{∞,loc} that (GT-sup) needs**. Two readings of this, both recorded:
- it **reproduces** §35.7's figure: with the core value ‖(Y^p)^c_0‖_∞ ≍ n (i.e. sup_own|Y^p_0| ≍ 1, the own
  size of a fine dipole field at distance 1 from p) the bound is 0.0198·n² ≈ 0.53·L^{2k−3}, which is
  §35.7's and Lemma RC's *Reading*'s ≍ L^{2k−3}. So the two accounts agree, and §2 does not contradict them;
- it **sharpens** them: the L^{2k−3} is not an irreducible fact about the tent. It is
  n²·(0.0198·sup_own|Y^p_{*,0}|), i.e. **n·(Y-sup^loc)**, and 0.0198 is an absolute constant. Every power of
  L in it is a unit conversion on the response field.

**(iv) Status. (TENT-Q): OPEN, reduced to (TENT-osc), CONDITIONAL deficit n·(Y-sup^loc).** Named item:

> **(TENT-osc), named and stated.** There is C_osc < ∞, independent of k, T, p and of the coarse cell, such
> that for a named representative Y^p_*, n²·osc_𝔅(Φ_k(Y^p_{*,0})) ≤ C_osc for every level-k cell-corner set
> 𝔅. **OPEN.** By §2.6 it is **not** weaker than n²·max_𝔅|Φ_k(Y^p_{*,0})| ≤ C_osc whenever Φ_k has a zero in
> 𝔅, which is generic. By (iii) it holds iff ‖(Y^p_*)^c_0‖_{∞,loc} ≲ n^{−1} on the boxes 𝔅 see — i.e. it is
> (Y-sup^loc) **with one extra power of n**, and it is therefore strictly stronger than (GT-sup)'s input.

**(v) What is NOT reached, plainly.** Nothing here computes Φ_k on a response field: tq1 evaluates Φ_k only
on an explicit compactly supported **source** (criteria scope limitation 3). So (iii)'s own-unit gain
0.019814 is **exact for that source** and is used for the response only as a dimensionless calibration,
labelled ARGUED where it is. No claim is made at m > 0, at θ > 0, at a nontrivial background, or about the
factor k in (NC-Γ) and (PW-ii) (REVIEW_BFT_A_S8 S8-12, S8-13 stand untouched).

### 2.9 The three face identifications asked for

**(a) (TENT-Q) and (NEUT-box) are NOT the same question — TQ-F6 OCCURS as pre-stated.** They are two
functionals of the same scalar family {Q_X}, and §2 separates them completely:
- (NEUT-box) is max_X|Q_X| measured against ‖D^⊥(S)‖_∞ — **FALSE by L^{2k}** (§2.3), and **withdrawn**,
  because the quantity it is used to bound cancels in the pairing (§2.4);
- (TENT-Q) is the **signed** sum Σ_X Q_XΦ_k(c_X), whose constant mode Proposition QN annihilates
  identically — **OPEN**, reduced to (TENT-osc) (§2.8).
Theorem NCE (ii)'s sentence "(TENT-Q) and (NEUT-box), two faces of the same quantity" is right about the
quantity and wrong about the item: one of the two faces is a false inequality in a mis-chosen currency, and
the other is a live statement about the response field. **They must not be carried as one item, and
(NEUT-box) must not be carried at all.**

**(b) (NEUT-box) against session 11's (CURV-dec) and lane A's Proposition OB: the same SHAPE, and the
difference is the one that matters. ARGUED.** The lead asks whether these are one object. They are not, and
§2 says why in one word: **smoothness of the cut-off.**
- (CURV-dec)'s residue (BFT_B §42.3 (iii)) is Σ_z(d_Z^*(F_l − 𝒫^{blk}_l))(z) = 0 **on a block** — a
  **sharp** (hard-indicator) neutrality condition, required to invoke Lemma BOG's no-wrap clause on a cube
  of side q, on the background's own Yang-Mills current.
- Proposition OB (BFT_A §26.2) is a **per-piece** total of β_m = κ_m[r_m(c), x_{m+1}(c)] — again a hard
  decomposition, and genuinely nonabelian (a commutator).
- (NEUT-box) is a **smooth**-weight condition: χ^5 is a C^{2,1} partition of unity, and §2.2 shows the
  consequence — the hard neutrality requirement becomes a **boundary flux with the explicit weight
  |dχ^5| ≤ (15/8)/n and exact total variation 2d(n/L^l)^{d−1}**. That is precisely why (NEUT-box) is not an
  obstruction and (CURV-dec)'s residue may be: a smooth cut-off converts "the total must vanish" into "the
  total is a collar flux of size O(1) in the right currency", and a hard cut-off does not.
**So: three conditions of one shape, three different objects, and one of them (mine) is already defused by
the smoothness of its own cut-off.** BFT_B §42.4's "three per-block neutrality conditions on three
different divergences is a pattern, not an identification" is confirmed, and this session adds the reason
the pattern does not close: the three differ in the regularity of the cut-off, which is exactly the
variable that decides whether neutrality is needed.
*A transferable proposal, offered and not claimed (see §4 FOR OTHER FILES).* The device that defuses
(NEUT-box) is a three-step one that S_E already implements: (1) replace the hard block indicator by the
quintic tent χ^5; (2) absorb the residual per-box total by a **pinned** point charge at the block root (the
ρ = ψ − ⟨ψ⟩δ_{c_X} of Lemma ΓT-op (a)); (3) observe that the pinned charge's contribution cancels
identically in the pairing (§2.4). If (CURV-dec)'s per-block solve is run against a tent partition instead
of a block indicator, step (1) replaces its no-wrap condition by a collar flux and steps (2)-(3) dispose of
the remainder. Whether Lemma BOG's constant 4q survives the smoothing is **not** decided here.

**(c) Lemma CONJ and the background: the scope boundary of §2, stated exactly.** Proposition QSBP (★) is
pure adjointness and transports to a background verbatim with d → d_Z, d* → d_Z^*. **Proposition QN does
not.** ⟨1, d_Z^*S_l⟩ = ⟨d_Z1, S_l⟩ and d_Z of a constant su(N) element ξ is Ad_{Z_b}ξ − ξ, which vanishes
only where the holonomy commutes with ξ. So at a nontrivial background **Σ_X Q_X^Z(S) ≠ 0**, and the defect
is a holonomy defect. By session 11's **Lemma CONJ** (flat background: Ad_G intertwines everything exactly
and pointwise) that defect is governed by the background **curvature**, not by ‖log Z‖ — so the right
statement to attempt at a background is "Σ_X Q_X^Z(S) is bounded by f_k times the class norms", and the
flat case is exactly the case where it is 0. This session makes **no** background claim; the above fixes
what would have to be proved. Note also that Lemma CONJ does **not** give Q_X^Z(Ad_G S) = Ad_{G(c_X)}Q_X(S):
the box sum does not commute with a varying Ad_G, and the defect is again the variation of G over Ñ_X,
i.e. curvature. **This is the one place where an abelian model would be vacuous, and §2 makes no claim
there.**

### 2.10 The residual obstruction that §2 exposes, named: (P0-sup)

Face (a) of Theorem NCE (ii) is the (P0)-slot size of the slice correction Γ_E^TD(S), used by route (R1) to
feed S^E_0(S) into Theorem COF. §2.4 disposes of it **wherever the correction is paired**. It does not
dispose of it in one place: **Theorem COF step (d), the Hölder half**, feeds LES-div a *pointwise* bound on
the level-0 current (BFT_B §35.5 (d): "sup|J_0[S^j]| ≤ n^{−3}(π_0(C(j)) + κ_+‖r^c_{k−1}‖_∞)"), and there the
correction enters by its sup, which bb8t C1 shows is genuinely ≍ n^d‖D‖_∞. Hence:

> **(P0-sup), named and stated.** Theorem COF's Hölder half, applied to the corrected source
> S^E_0(S) = S + Γ_E^TD(S), requires a **pointwise** bound on the level-0 current, and ‖Γ_E^TD(S)‖_∞ is
> genuinely of order n^d‖D(S)‖_∞ (not an artefact: Lemma ΓT-op (e) + bb8t C1 + tq1 A4's ⟨χ^5_X⟩ = n^d).
> **No neutrality statement about Q_X can repair this**, because §2.2 (b)'s bound on the charge is attained.
> **OPEN.** *The repair direction, proposed and not claimed:* obtain [f_0]^∞_α from Proposition NCR itself
> rather than from LES-div on the corrected source — f_0^{Γ_E}(S)(p) − f_0^{Γ_E}(S)(p′) =
> ⟨S, Y^p_* − Y^{p′}_*⟩ + ⟨D(S), λ^{Γ_E}_*(p) − λ^{Γ_E}_*(p′)⟩, so the Hölder half is a **difference of
> gauge transport functions** and never needs the sup of Γ_E^TD(S) at all. That turns the Hölder half into
> a Hölder version of (GT-sup)/(Y-sup^loc), i.e. into the same lane-A linear-package object.

## 3. Check record for tq1, with a per-check statement of discriminating power (written after §2)

Files: `checks/tq1_criteria.md` (14:12:45 UTC, **before** the script), `checks/tq1_charge.py` (14:14:28 UTC),
`checks/tq1_out.txt`, `checks/tq1_err.txt` (empty). Exact `fractions.Fraction`, plain python 3 `-I`, single
thread, `OMP/OPENBLAS/MKL_NUM_THREADS=1`, `nice -n 10`, no numpy/BLAS, **no numeric lock taken** (DRIVE_BRIEF
rule 6: exact rational arithmetic needs none). One run, no re-runs, no criterion amended. Load at start 1.95.

**Verdicts: ALL PASS (A1-A7 over both models; A8 informational).** No FAIL to report in this session.

| id | verdict | what it is tested **against** | could it have failed? |
|---|---|---|---|
| A1 Σ_X Q_X = 0 | PASS (exact, d = 2 and d = 4) | nothing independent — it is Σ_Xχ^5_X = 1 composed with ΣD(S) = 0, both prior PROVEN | **LOW.** Only on a convention error in D or in the root spacing. Given A4 it is close to forced, and I say so. |
| A2 identity (★) | PASS (exact, **every** X, both models) | two **disjoint** code paths: `composite_divergence` (d* + placement) then an explicit box sum, against `ev_pull`→`d_of`→pairing. Neither calls the other and neither is the transpose of the other | **MEDIUM.** A sign error in d*, a wrong `avatar`, or a wrong adjoint for the placement would fail it. |
| A3 total variation = 2d(n/L^l)^{d−1} | PASS (exact, l = 0, 1, 2; d = 2 and d = 4) | a **prior lane's closed form** (BFT_B §25.1 (f), post-proof correction (1)) against a brute-force total variation computed here from σ_5 | **MEDIUM-HIGH.** Wrong tent width, wrong off(l), or a wrong σ_5 would fail it. One of only two checks here against a number this lane did not produce. |
| A4 Σχ^5 = 1, ⟨χ^5_X⟩ = n^d | PASS (exact) | the identity σ_5(t) + σ_5(1 − t) = 1 (BFT_B §16.1 (b)) | **LOW** for the first clause; **MEDIUM** for ⟨χ^5_X⟩ = n^d, which fixes the n^d that bb8t C1 measures. |
| A5 tent-interpolation (TQ-INT) | PASS (exact, both models, **pseudo-random** Φ) | two disjoint paths: box-charge sum × Φ, against the global interpolation I_χΦ paired slot-wise | **MEDIUM.** Nothing is tuned; Φ is pseudo-random, so a wrong I_χ or a missing constant-mode term would fail. |
| A6 **tent-gauge identity** | PASS (exact; both sides −17600766949/4728643920) | a **new** identity with no prior value to match: the HT/`qstr` funnel pipeline against a plain block average, on pseudo-random μ **and** pseudo-random x_0 | **HIGH — this is the check of this session most able to fail.** A telescoping error, a wrong block convention, a wrong off(l) or a wrong Q_str∘d = d∘A would all fail it, and nothing in the file predicted the value. |
| A7 rebuild of S8-7's rationals | PASS (all four exact) | **an independent prior computation**: REVIEW_BFT_A_S8's φ_1 = −1/432, φ_2 = −17/104976, ratio 17/243, ψ_u = −65/26244, rebuilt here from the axial 24-order construction and the straight average | **HIGHEST against an outside number.** Any error in HT, `qstr`, the plaquette convention or the normalisation would fail it. |
| A8 ∇^{(k)}Φ_k / max Φ_k | informational; **ratio = 1 exactly** | — | n/a, but note it came out **against** this session's preferred route (§2.6): it is the number that kills route 1's hoped-for gain. |

**What tq1 does NOT test, stated plainly (and the lead asked for exactly this).**
1. **No check here reaches nonabelian content.** Every tq1 statement is fibre-componentwise at the trivial
   background and §2.0 proves, by citation to BFT_B §24.0 and §16.1 (f), that a scalar model is therefore a
   **complete** test of it rather than a vacuous one. The one statement in §2 where the fibre matters —
   Proposition QN at a nontrivial background — is **explicitly not claimed** (§2.9 (c)), precisely because an
   abelian model would be vacuous for it.
2. **(CC-0) at critical points rests entirely on BFT_A Lemma CD (i), a nonabelian identity that no lane-B
   check touches** (the reviewer of sessions 9-10 records this, and REVIEW_BFT_B_S9_S10 S10-* notes that
   everything downstream of it rests on a quoted lemma). §2 takes it as a **named input** and asserts nothing
   about it. No result of this session would change if Lemma CD (i) were narrowed: §2 is about the residue
   that appears **when** D(S) ≠ 0, which is the complement of Lemma CD (i)'s scope.
3. **No response field is computed anywhere** (criteria scope limitation 3). Φ_k is evaluated only on an
   explicit compactly supported *source*. Every statement about Y^p_{*,0} in §2.8 (iii) is a calibration,
   labelled ARGUED there.
4. **No check reaches Corollary COF-crit (§35.6)** — the step REVIEW_BFT_B_S9_S10 Part J refutes. Nothing in
   §2 depends on §35.6: §2 prices the residue and the charge, and §35.6 is the substitution of row sizes into
   Theorem COF's class norm, which is upstream and outside this scope. See §4.3.
5. **k = 2 only**, and d = 2 for the generic-dimension identities (A1, A2, A4, A5 are also run at d = 4).
   A level count cannot be measured at k = 2; nothing here is evidence about k-uniformity, and §4.3 does not
   use tq1 for that.

## 4. Outcome (written after §3)

### 4.1 Outcome table

| object | status | content |
|---|---|---|
| **Proposition QN** (Σ_X Q_X(S) = 0) | **PROVEN-HERE** | for every chain source, no hypothesis. The level-k root-charge field I_χ^TD(S) is **neutral**, so the tent coefficient's constant mode is annihilated. **TQ-F1 does not occur.** tq1 A1 |
| **Proposition QSBP** (★) | **PROVEN-HERE** | Q_X(S) = Σ_l⟨d(ev^{(0→l)}χ^5_X), S_l⟩ — the charge is a **collar flux of the source**, not a box average of D(S). Extends BFT_B §25.1 (f) from one slot to the composite. tq1 A2 |
| **Q_X ≠ 0** | **PROVEN-HERE** | exact configuration S_l = c·sign(d(ev^{(0→l)}χ^5_X)) gives Q_X = 8c·L^{3(k−l)}. **TQ-F2 does not occur**; (NEUT-box) is **not** the statement that a boundary term vanishes |
| **|Q_X(S)| ≤ 2d Σ_lπ_l(S_l) = 8Σ_lπ_l(S_l)** | **PROVEN-HERE, and attained** | k-, T-, X-uniform, **absolute** constant. The L^{3(k−l)} of the tent's total variation cancels exactly against the own→coarse conversion |
| **Proposition QFALSE** | **PROVEN-HERE** | **(NEUT-box) as stated in BFT_B §36.4 is FALSE, by exactly L^{2k} − 1.** A currency mismatch, not a cancellation failure. Not repairable: the §2.2 (b) bound is attained |
| **Proposition PINC** | **PROVEN-HERE** given Lemma ΓT-op (a) | the pinned compensation charge's entire contribution to every pairing **cancels identically**; Γ_E^Tφ = −Σ_XΣ_wχ^5_X(w)φ(w)(A^X_w − A^X_{c_X}), one piece, no pinned term. **The pin is FORCED (TQ-F5 occurs) and irrelevant** |
| **route (ii) / Proposition GT-ell** | **dead as a route** (PROVEN-HERE for both halves) | its ℓ^∞ step splits an exactly-cancelling pair; and its *leading* term n⁴‖D‖_∞ already loses one power of n in the (P0) class, (NEUT-box) or no (NEUT-box) |
| **(NEUT-box)** | **WITHDRAWN, not OPEN** | false as stated, not necessary (PINC), not sufficient (GT-ell's first term) |
| **Theorem TQ-INT** | **PROVEN-HERE** | 𝒯_p(S) = n²Σ_l⟨d(ev^{(0→l)}I_χΦ), S_l⟩: the box charges are **eliminated**; (TENT-Q) is one pairing against the gradient of the tent-interpolated tent coefficient. tq1 A5 |
| **Lemma TENT-TV** + **Corollary TQ-osc** | **PROVEN-HERE** | ‖d(ev^{(0→l)}I_χΦ)‖_1 ≤ 2d(n/L^l)^{d−1}Σ_X|Φ(c_X) − c|; hence |𝒯_p(S)| ≤ 128·n²·osc_𝔅(Φ_k)·Σ_lπ_l(S_l) per coarse cell |
| **Proposition TQ-NOGAIN** | **PROVEN-HERE** + **COMPUTED** | neutrality buys max → osc and **nothing more**: Φ_k(v) vanishes at every level-k root whose block misses supp v, so osc = max exactly. tq1 A8: ratio **1 exactly** |
| **Proposition TGAUGE** | **PROVEN-HERE** (identity); **ARGUED** (the price) | Φ_k(x_0 + dμ)(X) − Φ_k(x_0)(X) = A^{(0→k)}μ(X) − μ(c_X). The tent coefficient is a **representative artefact**; it can be gauged to a constant and the residue then vanishes by QN — at an equal cost in the main pairing. tq1 **A6** |
| **(TENT-Q)** | **OPEN, reduced to (TENT-osc)**; deficit **n·(Y-sup^loc)**, COMPUTED calibration 0.0198 | one scalar inequality **on the response field alone**: n²·osc_𝔅(Φ_k(Y^p_{*,0})) ≤ C_osc |
| **(P0-sup)** (new named item) | **OPEN**, stated precisely (§2.10) | Theorem COF's **Hölder** half needs the level-0 current in **sup**, and ‖Γ_E^TD(S)‖_∞ ≍ n^d‖D‖_∞ genuinely. No neutrality statement repairs it. Proposed repair: take [f_0]_α from Proposition NCR's **difference** form |
| **TQ-F3, TQ-F4** | neither needed | the collar weight question (F3) is settled exactly by §2.2 (b) — the n-power cancels, so F3 **does not occur** in the coarse currency and **does occur** against ‖D‖_∞, as pre-stated; F4's flux-potential route was **not used** (Lemma TENT-TV replaced it, with an explicit constant), so F4 is moot |

### 4.2 The five questions in the brief, answered

1. **Does Q_X vanish, cancel, or is it obstructed?** It **does not vanish** and it **does not cancel**
   (exact configuration, §2.2 (a)). It is, however, **bounded k- and T-uniformly with an absolute
   constant 8** in the source's own coarse currency (§2.2 (b), attained). So it is neither zero nor an
   obstruction *as a charge*; what it is paired against decides.
2. **Is (NEUT-box) a boundary-term statement?** It is **exactly** a boundary-term statement — (★) writes
   Q_X as a collar flux with weight ≤ (15/8)/n and exact total variation 2d(n/L^l)^{d−1} — and **that
   boundary term does not vanish**. The brief's conjecture "(NEUT-box) is exactly the statement that that
   boundary term vanishes" is therefore **false in both directions**: the term is a boundary term, and
   (NEUT-box) is not its vanishing but an inequality against the wrong norm, which is **FALSE by L^{2k}**.
3. **Can the pinned compensation charge be moved?** **No — and it does not need to be.** The pin is
   constitutive of S_E (it is what makes ev^{(k)}Λ = 0, hence Π_E a projection along 𝒢_0): TQ-F5 occurs.
   But the pinned charge's whole contribution to every pairing **cancels identically** (Proposition PINC),
   so Lemma ΓT-op (e)'s second term is a property of the ℓ^∞ norm and not of the slice. **Route (ii) is
   dead and (NEUT-box) is withdrawn.**
4. **Status of (NC-Γ) for Γ_E off the critical set.** Off the critical set the two faces **separate**
   (TQ-F6 occurs): face (a) is no longer (NEUT-box) but the new named item **(P0-sup)** — the Hölder half's
   need for a pointwise bound on Γ_E^TD(S) — and face (b) is **(TENT-osc)**. Both are now statements about
   **Y^p_* and the estimate route**, not about the box charges. **And see §4.3: the factor k sits upstream of
   all of this.**
5. **What is left of (TENT-Q)?** One inequality, **(TENT-osc)**, with the source eliminated, the charge
   eliminated, the constant absolute (128 = 2^d·2d), the exact calibration 0.019814 rebuilt, and a named
   deficit of **exactly one power of n = L^k relative to (Y-sup^loc)** — i.e. (TENT-Q) is strictly stronger
   than (GT-sup)'s input, by L^k, and the two are no longer independent items.

### 4.3 >>> The factor k is UPSTREAM of everything in §2, and this session's own currency confirms it

REVIEW_BFT_B_S9_S10 Part J (S10-6, binding fix RS10-1) refutes **Corollary COF-crit (§35.6)**: Theorem COF's
right-hand side carries ‖j‖_Pc = max_l L^{θ(k−l)}π_l(j_l), §35.6 substitutes the **per-level** row bound
π_l(V_l) ≤ Cη² for it, and the two differ by L^{θ(k−1)}; the in-proof route gives (k − 1) and optimising θ
gives ≈ 25(k − 1). **Therefore Theorem NCE (i) is not k-uniform, and the factor k is upstream of
(TENT-Q), (NEUT-box) and (Y-sup^loc) alike.** This session **accepts that finding and does not claim
otherwise.**

**I reproduce it independently, in this session's own currency, and the sharp form is cheaper than ≈25(k−1).**
Every bound of §2 is stated against **Σ_{l=0}^{k−1}π_l(S_l)**, not against ‖S‖_Pc. In the (P0) + (Pl-c)
class that sum is geometric and k-uniform: Σ_{l≥1}π_l(S_l) ≤ (1 − L^{−θ})^{−1}‖S‖_{Pc}. But for the BCH₂
**rows**, Corollary NC gives π_l(V_l) ≤ 2C_NCC_bchκ_+L²η² **per level with no level decay**, and then

  **Σ_{l=0}^{k−1}π_l(V_l) ≤ k·2C_NCC_bchκ_+L²η² — a bare level count k, with no power of L and no θ to
  optimise.**

So the reviewer's diagnosis is exactly right ("(Pl-c) does not contain the rows"), and the sharp statement
of the loss is **k**, not L^{θ(k−1)} and not 25(k − 1): routing through ‖·‖_Pc is what forces the θ
optimisation, and Σ_lπ_l avoids it. **Offered to lane B as a currency improvement on RS10-1 (see §5).**

**What may and may not be claimed as a result, therefore:**
- **MAY:** the box charge is O(1) with an absolute constant per level (§2.2 (b)); the residue is one pairing
  (§2.5); (NEUT-box) is false and withdrawn (§2.3, §2.4); (TENT-Q) reduces to (TENT-osc) with deficit
  n·(Y-sup^loc) (§2.8). All of these are **per-level** statements and are **k-uniform in their own right**:
  no constant in §2 contains k.
- **MAY NOT, and is not claimed anywhere above:** that closing (TENT-Q) completes (NC-Γ) for Γ_E uniformly
  in k. It does not. Even with (TENT-osc), (Y-sup^loc) and (P0-sup) all granted, the level sum over slots
  contributes **k** (or ≈25(k − 1) through ‖·‖_Pc), and removing it needs lane A's **(SPD)/(W2)**, OPEN.
  The honest form of every §2 statement is therefore **"at fixed k"**, or **"with the level count displayed
  as Σ_lπ_l(S_l)"**, which is how §2 writes them.

### 4.4 >>> (GT-sup) is reopened, and this session's numbers independently support the reopening

REVIEW_BFT_B_S9_S10 S10-14 marks §36.2's headline conclusion **NOT-VERIFIED**: ΓT-op (d)'s constant 20 is
right and does apply to Y^p_{*,0}, but the reduction lands on **(Y-sup^loc)**, which demands
max_own|Y^p_0| ≲ 1/n near p, and the |z|^{−3} profile behind 𝒩(Y^p) ≍ n contradicts it. **§2.8 (iii) reaches
the same place from the other side, without having read that review when §2 was written:** the own size of a
fine dipole field at distance 1 from p is ≍ 1, not ≍ 1/n, and with that value the (TENT-Q) bound is
0.0198·n² ≈ 0.53·L^{2k−3} — which is exactly Lemma RC's *Reading* and §35.7's figure. So:

- **(Y-sup^loc) is expected FALSE at the core of the response**, and §36.2's own caveat said so
  ("a global (Y-sup^loc) is a statement about the core of the response, not about its tail");
- consequently **(TENT-osc) is expected FALSE at the core too**, by L^{2k}, and (TENT-Q) is **not** merely
  OPEN but **expected FALSE for a representative whose level-0 field is of fine-dipole size near p**;
- **the one thing that could save it is a currency that the funnel actually uses.** Φ_k is a *block-averaged
  axial line integral*, not a sup: h_i(w)(X) is the average over the L^d block offsets of the integral of w
  along an axial path. The core of a |z|^{−3} field is a vanishing fraction of a block. So the right norm for
  (TENT-osc) is an **averaged** one, and the exact calibration 0.019814 of tq1 A7 is measured on a field
  concentrated at a single plaquette — i.e. on the worst-localised admissible field. **Whether the averaging
  beats the core is the live question, and it is not decided here.** Named in §5 as a request.
- **Scope honesty on the calibration.** The k-independence of the own-unit funnel gain rests on
  REVIEW_BFT_A_S8 S8-5's convergence of Φ_l, which is **exact at i = 1** (ratio 17/243, rebuilt here as
  tq1 A7) and **ARGUED for i ≥ 2**. Without it the crude sup bound on Φ_k is ≍ n·sup_own|v| (each Q_str step
  can multiply the own sup by L), which would be a further power of n. So §2.8 (iii)'s figure is
  **CONDITIONAL on (Φ-conv)**, the convergence of Σ_iφ_{i+1}, which is ARGUED in lane A and is not proven
  anywhere.

### 4.5 The single biggest remaining obstruction in this scope

Not (TENT-Q)'s algebra — that is now closed in exact form, with absolute constants, and the box charges are
gone. It is the **own-unit size of the response's level-0 field in the norm the funnel uses**: one object,
(Y-sup^loc) for the gauge-transport face and (TENT-osc) = n·(Y-sup^loc) for the tent face, both expected
false in the sup norm at the core of Y^p and both undecided in the block-averaged norm that Φ_k and λ^E
actually read. **It is a lane-A linear-package question about Y^p, and it is now the only thing between
Theorem NCE (ii) and a statement — at fixed k.**

## 5. FOR OTHER FILES (not edited)

**To BFT_B.md's owner (lane B), five items.**
1. **(NEUT-box) should be struck from the open set, not attempted.** §2.3: it is FALSE as stated in §36.4, by
   exactly L^{2k} − 1, with an exact (P0)-class configuration. §2.4: the quantity it bounds cancels
   identically in every pairing, so it is an artefact of taking ‖Γ_E^Tφ‖_∞ before pairing. §2.4's last
   paragraph: even granting it, Proposition GT-ell's **first** term loses a power of n. Suggested wording:
   *"(NEUT-box) withdrawn (TENTQ §2.3, §2.4): false as stated, not necessary, not sufficient; route (ii) is
   route (R2) with a lossy intermediate step."*
2. **Theorem NCE (ii)'s "two faces of the same quantity" needs splitting.** §2.9 (a): the two faces are
   different functionals of {Q_X} and only one of them survives. Off the critical set the residual pair is
   **(TENT-osc)** (face b) and the **new** item **(P0-sup)** (face a, §2.10) — the Hölder half's need for a
   pointwise bound on Γ_E^TD(S). (P0-sup) is not about Q_X at all.
3. **A currency improvement on RS10-1.** §4.3: stating Theorem COF against **Σ_{l}π_l(S_l)** instead of
   ‖j‖_Pc makes the row loss exactly the level count **k**, with no power of L and no θ to optimise, instead
   of L^{θ(k−1)} optimised to ≈25(k − 1). The reviewer's refutation stands either way; this is a cheaper
   bookkeeping of the same fact, and it is the form in which every §2 bound is stated.
4. **The same summation-by-parts applies to the (GT-sup) face, and §31.3 (R2)'s two factors are not both
   class-bounded.** ⟨D(S), λ⟩ = Σ_l⟨d(ev^{(0→l)}λ), S_l⟩ by (★) with χ^5_X replaced by λ. Unlike I_χΦ, λ
   has **no scale-n smoothness**, so its level-l differences are of order sup|λ| and the l = 0 slot costs a
   power of n that ‖D(S)‖_1·sup|λ| hides in the ℓ¹ factor. **Request:** re-price §31.3 (R2) against
   Σ_lπ_l(S_l) and the level-l differences of λ, and say which weighted ℓ¹ of D(S) the class actually
   supplies. *Not decided here — flagged, not claimed.*
5. **Proposition PINC is available as a lemma** (§2.4): Γ_E^Tφ = −Σ_XΣ_wχ^5_X(w)φ(w)(A^X_w − A^X_{c_X}), one
   piece of box **dipole** fields, which is the pin-free form of Lemma ΓT-op (a) and makes the cancellation
   visible. It is three lines from §25.1 (a) and may be entered as an erratum-free addition if wanted.

**To whoever owns (CURV-dec) (BFT_B §42.3) — a transferable device, offered and not claimed.** §2.9 (b):
(NEUT-box), (CURV-dec)'s residue and lane A's Proposition OB are **three different objects of one shape**,
and the variable that distinguishes them is the **regularity of the cut-off**. (NEUT-box) is defused because
χ^5 is smooth: the hard condition "the block total must vanish" becomes a collar flux with weight
≤ (15/8)/n and exact total variation 2d(n/L^l)^{d−1}. The three-step device S_E already implements is
(1) smooth partition instead of block indicator, (2) absorb the residual per-box total by a **pinned** point
charge at the root (ρ = ψ − ⟨ψ⟩δ_{c_X}, Lemma ΓT-op (a)), (3) the pinned charge cancels in the pairing
(Proposition PINC). **Proposal: run (CURV-dec)'s per-block solve against a quintic-tent partition rather
than a block indicator**; step (1) then replaces Lemma BOG's no-wrap condition by a collar flux. **Whether
Lemma BOG's constant 4q survives the smoothing is not decided here**, and that is the one thing to check
before believing this.

**To BFT_A.md's owner (lane A), two requests.**
1. **(TENT-osc), and the norm it should be stated in.** §4.4: the funnel Φ_k is a **block-averaged axial
   line integral** of Y^p_{*,0}, not a sup. The sup form of the question, (Y-sup^loc) and its n-fold
   strengthening (TENT-osc), is expected FALSE at the core of Y^p (|z|^{−3} profile vs 𝒩(Y^p) ≍ n). The
   request is the **averaged** bound the funnel actually consumes: a k-, T-, p-uniform bound on
   max_X|(h^{(0→k)}Y^p_{*,0})(c_X)| and on its one-coarse-step difference, for the 𝒩-minimising
   representative. This is the single object left between Theorem NCE (ii) and a statement at fixed k.
2. **(Φ-conv) should be named and given a status.** §4.4's last bullet: the k-independence of the own-unit
   funnel gain 130/6561 = 0.019814 (rebuilt exactly here, tq1 A7) rests on the convergence of
   Φ_l = Σ_{i<l}φ_{i+1}, which is **exact at i = 1** (ratio 17/243) and **ARGUED for i ≥ 2**
   (REVIEW_BFT_A_S8 S8-5, S8-7's "routine estimate (ii)"). Without it the crude bound is Φ_k ≍ n·sup_own|v|,
   a further power of n. Every quantitative statement about the tent in this project is CONDITIONAL on it,
   including §2.8 (iii) and §35.7's L^{2k−3}. It is cheap (an operator ratio at i = 2, exact, no solve) and
   it is load-bearing in three files.

**To PROOF.md's owner.** If (NEUT-box) appears in the ledger, it should move to **withdrawn/refuted** with
the reason "false by L^{2k} as stated; the bounded quantity cancels in the pairing (TENTQ §2.3, §2.4)", and
**(P0-sup)** and **(TENT-osc)** should be entered in its place. Net open-item count in this scope:
−1 ((NEUT-box)), +2 ((P0-sup), (TENT-osc)), with (TENT-Q) **re-stated** rather than closed and with the
upstream factor k (RS10-1) recorded as binding on it.

## 6. POST-HOC probe tq1b (run after tq1 and after §2-§5 were written; labelled post-hoc)

`checks/tq1b_qfalse_posthoc.py`, `checks/tq1b_out.txt` (14:35:12-14:35:15 UTC, exact, 3 s, no lock).
**This is a post-hoc probe. It has no PASS/FAIL of its own, `checks/tq1_criteria.md` was not touched, and
no verdict in §2-§5 was changed by it.** Its only purpose is to exhibit Proposition QFALSE's configuration
explicitly rather than by inequality.

For d = 4, j_0 := sign(dχ^5_{X_0}) (own sup 1), D := d*j_0:

| k | n | ‖dχ^5_{X_0}‖_1 | box sum ⟨χ^5_{X_0}D⟩ | ‖D‖_∞ | ⟨χ^5_{X_0}D⟩/(n‖D‖_∞) |
|---|---|---|---|---|---|
| 1 | 3 | 216 = 2d·n³ | **216** | **8 = 2d** | **9 = n²** |
| 2 | 9 | 5832 = 2d·n³ | **5832** | **8 = 2d** | **81 = n²** |

Three things it adds, all post-hoc:
1. The two independent computations of Q_{X_0} — the box sum Σ_wχ^5_{X_0}(w)D(w) and the collar flux
   ‖dχ^5_{X_0}‖_1 of (★) — agree **exactly**, at both k. (A third confirmation of Proposition QSBP, now on
   the extremal configuration rather than on pseudo-random data.)
2. ‖D‖_∞ = 2d **exactly** (not merely ≤ 2d), attained at c_{X_0} where all d sign hyperplanes meet.
3. The ratio in Proposition QFALSE is therefore **exactly n² = L^{2k}**, not merely ≥ n² − 1. **(NEUT-box)
   as stated in BFT_B §36.4 fails by exactly L^{2k}**, and §2.3's "≥ L^{2k} − 1" may be read as "= L^{2k}"
   for this configuration. The statement in §2.3 stands unaltered as the record.
