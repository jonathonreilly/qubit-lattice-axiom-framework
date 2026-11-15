# YSUP: does the funnel's averaging beat the core of Y^p? — session 25 (2026-10-28 UTC)

Scope of the whole file, stated once and binding on every claim in it: **m = 0, trivial background, d = 4,
L = 3, the elliptic slice S_E (lead decision D1), linearised**. Every status is one of PROVEN-HERE /
PROVEN as an implication / ARGUED / COMPUTED (exact) / CONDITIONAL (input named) / OPEN.

## 1. PRE-STATED (session 25) — statements only; the FIRST edit of this file, written 2026-10-28 14:47 UTC

This section is the first edit of YSUP.md. It contains **statements only**. It cites nothing produced in this
session. Exploratory *reading* preceded it (DRIVE_BRIEF; HANDOFF; TENTQ.md in full, especially §2.5-§2.10,
§4.4, §4.5, §5; REVIEW_BFT_A_S8 Parts 4-5; REVIEW_BFT_B_S9_S10 Part L (S10-13 to S10-16); BFT_A §38.3-§38.7;
BFT_B §29.2 Lemma FT (i), §34.3, §36.1-§36.3, §31.3; the scratch scripts revA8/rev8_exact.py and
revA8/rev8_psi.py) with exploratory reasoning that is not recorded; the only claim §1 makes is file order.
All inputs below enter as **named hypotheses**, quoted and not re-judged.

### 1.0 The object, as cited

For a level-0 chain field v and a level-k site X with root (block centre) c_X, the funnel is

    **Φ_k(v)(X) = Σ_{i=0}^{k-1} ev^{(i+1→k)} h_i ( Q_str^{(0→i)} v ) (X)**    (BFT_A §38.3 / BL-2 (b)),

with (BFT_B §29.2 Lemma FT (i)) **h_i(w)(Y) = avg_{y∈B(Y)} ∫_{a(c_Y→y)} w**, a(c_Y→y) the axial path in a
fixed coordinate order, all such paths staying **inside** B(Y); and (BFT_B §27.1)
**(Q_str v)(Y,m) = L^{-d} Σ_{r∈[0,L)^d} Σ_{j<L} v_m(LY + r + j e_m)**.

The two consumers, as cited:
- **(Y-sup^loc)** (BFT_B §36.2, Proposition GT-loc): a bound on max_X‖(Y^p_*)^c_0‖_{∞,Ñ_X} in **coarse**
  units, i.e. on n·max_own|Y^p_{*,0}|; it delivers **(GT-sup)** = sup_p sup{|λ^{Γ_E}_*(p)(z)| : z ∈ supp D(S)}
  bounded uniformly in k, T (BFT_B §27.4), with the absolute constant 20.
- **(TENT-osc)** (TENTQ §2.8 (iv)): n²·osc_𝔅(Φ_k(Y^p_{*,0})) ≤ C_osc uniformly in k, T, p, 𝔅.

The profile input, as cited: Y^p's free part g_0 obeys **|g_0(b)| ≤ C_0(1 + |b − p|_∞)^{−3}**, co-closed,
and ψ := h^{(0→k)}g_0 is the tent that Theorem PW-E's data split forces out (BFT_A §38.7); the same
|z|^{−3} profile is the only one consistent with Theorem YH's 𝒩(Y^p) ≤ C_YN·n (REVIEW_BFT_B_S9_S10 S10-14).

### 1.1 Targets of this session (written before any derivation)

- **Y1 (the exact form and normalisation).** Write Φ_k down as the block-averaged axial line integral it is,
  as an explicit kernel on fine links: Φ_k(v)(c_X) = Σ_{i<k}⟨K_i, v⟩ with K_i := (Q_str^{(0→i)})^T h_i^T δ_X.
  State (a) supp K_i exactly, (b) sup|K_i|, (c) ‖K_i‖_1, each with its power of L, and (d) the unit
  convention in which the output is compared with sup_own|v|, so that no spurious power of n enters.
- **Y2 (the exact block average of the |z|^{−3} profile).** Compute the level-i gain exactly: the size of
  (Q_str^{(0→i)}v) and of the i-th funnel term φ_{i+1} := h_i(Q_str^{(0→i)}v)(X) for an admissible profile
  field, as a power of the **block side** n_i := L^i, with an explicit constant. Decide between the two
  candidate powers n_i^{−2} and n_i^{−3} and say which mechanism fixes it.
- **Y3 (the comparison with the two thresholds).** (Y-sup^loc) needs ≲ 1/n; (TENT-osc) needs ≲ 1/n² after
  the n² (and by TENTQ's Proposition TQ-NOGAIN osc may not be traded for less than max). State, for each,
  whether the averaged currency clears the threshold, clears it with room, or fails, **and by what power of
  n**.
- **Y4 (the axial dimension count, explicitly).** State the dimension count for an axial line integral in
  d = 4: how many directions are averaged, how many are summed, and what that costs relative to a full
  block average. Then state which level of the sum over i is binding.
- **Y5 (the verdict and, if negative, the fallback).** If the averaging beats the core, state the bound with
  its constant and which of (Y-sup^loc) and (TENT-osc) it delivers, at what scope. If it does not, say so
  plainly, and assess TENTQ §2.10's fallback — taking [f_0]_α from Proposition NCR's **difference** form, so
  that the Hölder half becomes a Hölder (GT-sup) and never needs the sup of Γ_E^TD(S).

### 1.2 Pre-registered failure modes, with expectations

- **YS-F1.** The level-i block average of the |z|^{−3} profile is O(n_i^{−3}) or smaller (the brief's
  candidate), so that each level clears 1/n with room. Expected: **DOES NOT OCCUR as stated**; expected
  instead O(n_i^{−2}), because an axial line integral averages over d − 1 = 3 transverse directions and
  **sums** along the fourth, so it loses exactly one power of n_i against a full block average.
- **YS-F2.** The i = 0 term of Φ_k carries the same n-gain as the top level. Expected: **DOES NOT OCCUR.**
  Expected: ev^{(1→k)}h_0 reads v only inside the **level-1** block of c_X (fine side L = 3), so its gain is
  L^0 = 1 and it is the binding term. If this expectation holds, the brief's framing — "the core of a
  |z|^{−3} field is a vanishing fraction of a block" — is answered by saying that the block in question is
  the level-(i+1) block, not the level-k block, and at i = 0 the core is **not** a vanishing fraction of it.
- **YS-F3.** φ_1 vanishes, or the higher terms cancel it, so that Φ_k(v)(c_X) is o(1) in k although every
  individual term is O(1). Expected: **DOES NOT OCCUR** for at least one admissible placement of p;
  expected instead that Σ_{i≥1}|φ_{i+1}| < |φ_1| for a compactly supported admissible field, provably, so
  that |Φ_k| is bounded **below** uniformly in k. Note: for *some* placements φ_1 = 0 by symmetry, and the
  statements (Y-sup^loc)/(TENT-osc) are universally quantified over p and 𝔅, so one placement suffices to
  refute and no placement suffices to prove.
- **YS-F4.** The funnel's far-field decay is too slow for the failure to be confined to the core, so that
  (TENT-osc) fails even at coarse distance 1 from p and the "core" diagnosis is wrong. Expected:
  **DOES NOT OCCUR**; expected |Φ_k(v)(c_X)| ≲ C_0(1 + |c_X − p|_∞)^{−2}, the line-integral profile of a
  |z|^{−3} field, so that the failure is strictly a core phenomenon and §36.2's own caveat is confirmed.
- **YS-F5.** The two faces share their averaging, so that a verdict on Φ_k settles both. Expected:
  **DOES NOT OCCUR — the two faces consume different averaging operators.** Φ_k's kernel is a local O(1)
  weight on the level-1 block; λ^E's kernel is the box-dipole A^X_z − A^X_{c_X} of Lemma ΓT-op (a), a
  **difference of two box-Coulomb gradients**, whose pairing with a second |z|^{−3} field is a convolution.
  Expected consequence, to be decided: the λ^E face is O(1) by its own averaging and the Φ_k face is not
  rescued by its own. If this occurs, the correct repair for face (a) is not (Y-sup^loc) at all but the
  replacement of Proposition GT-loc's ℓ¹ × sup Hölder step by the exact dipole pairing.
- **YS-F6.** The conclusion is conditional on (Φ-conv) (the convergence of Σ_iφ_{i+1}, exact at i = 1 and
  ARGUED above, TENTQ §4.4). Expected: **DOES NOT OCCUR for this profile class** — expected that the
  level-i bound of Y2 *proves* geometric convergence with ratio L^{2−d} = L^{−2} for every field obeying the
  (1 + |z|_∞)^{−3} profile, so that the result of this file is unconditional on (Φ-conv) within its scope.
  If that expectation fails, every statement here is CONDITIONAL on (Φ-conv) and will say so.

### 1.3 Pre-registered process commitments

- Any numeric check gets `checks/ys1_criteria.md` written **before** its script, containing no constant
  derived in this session. All arithmetic exact (`fractions.Fraction` / Python ints), plain `python3 -I`,
  single thread, no numpy/BLAS, **no numeric lock** (DRIVE_BRIEF rule 6).
- At least one check must be **capable of failing against an independently produced number**, and at least
  one must be a **designed-FAIL control** demonstrating that the pipeline detects a deliberate error. Each
  check is graded for discriminating power, and a gate that cannot fail is labelled as such.
- A FAIL is reported as a FAIL, script and output kept unaltered; a re-run uses a new id with the criteria
  untouched; anything run after seeing a result is labelled **post-hoc**.
- Load-bearing cited mathematics is **rebuilt** here, not cited: the axial weights of h_i, Q_str, the root
  offsets, and REVIEW_BFT_A_S8 S8-7's exact rationals are recomputed in this session's own script before
  being used in any estimate.
- This file is append-only. **No other lane file is edited** (in particular not TENTQ.md, BFT_A.md,
  BFT_B.md, NLOC.md or any REVIEW_* file); requests go in a final "## FOR OTHER FILES (not edited)".

## 2. Proofs and computations (appended after §1 (14:47 UTC), after `checks/ys1_criteria.md` (14:54 UTC), `checks/ys1_funnel.py` (ran 14:57, 0.99 s, 101 MB, 2 FAILs), `checks/ys1b_criteria.md` (15:06 UTC), `checks/ys1b_power.py` (ran 15:01, 1.48 s, aborted at clause B5) and `checks/ys1b2_control.py` (ran 15:02))

Notation. n = L^k, n_i = L^i, d = D = 4, L = 3. off(l) = (L^l − 1)/2; the level-i avatar of the level-k
root c_X is Y_i = (off(k) − off(i))/L^i, and L·Y_{i+1} + (L−1)/2 = Y_i. v is a level-0 1-form in **own**
units; C_0 := the profile constant of |v(b)| ≤ C_0(1 + |b − p|_∞)^{−3}; R := |c_X − p|_∞ in fine units.

### 2.0 Scope note: why a scalar model is COMPLETE here, and where that stops

h_i, Q_str, ev, d and d* act **componentwise on su(N) in an orthonormal basis** at the trivial background
(BFT_B §24.0; §16.1 (f)). Every statement of §2 is linear with scalar coefficients in the fibre, so an exact
scalar model is a **complete** test of it, not a vacuous one. **Where this stops:** at a nontrivial
background the axial transports do not commute with the fibre and a scalar model is vacuous; §2 makes **no**
background claim and none of its statements is offered at m > 0 or at a background. The nonabelian content
of the problem sits in the source (BFT_A Lemma CD) and in the background, both taken as named inputs.

### 2.1 Proposition YS-K (Φ_k's exact form, support and norms, in the normalisation Theorem TQ-INT uses): PROVEN-HERE

*Statement.* For every level-0 field v and every level-k site X,

  **Φ_k(v)(c_X) = Σ_{i=0}^{k−1} ⟨K_i, v⟩,   K_i := (Q_str^{(0→i)})^T h_i^T δ_{Y_{i+1}},**

and the kernels K_i, which are level-0 1-forms, satisfy, with B the level-(i+1) block of c_X:

  **(a) supp K_i = exactly the set of level-0 links both of whose endpoints lie in B** (fine side L^{i+1}),
      and **both ends of that range are attained**;
  **(b) sup_b|K_i(b)| ≤ L^{i(1−d)} = n_i^{−3}** (exact value (10/81)·n_i^{−3}, COMPUTED);
  **(c) ‖K_i‖_1 ≤ L^i·L^{−d}Σ_{y∈B(X)}|y − c_X|_1 = (8/3)·n_i** (exact asymptote 2·n_i, COMPUTED);
  **(d) K_i(z, m) depends on z only through (⌊z_ν/n_i⌋)_{ν≠m} and z_m**, so it is constant on each of the
      n_i^{d−1} transverse fine translates inside a block.

*Proof.* The form is the transpose of the definition of §1.0, slot by slot, using that
ev^{(i+1→k)T}δ_X = δ_{Y_{i+1}} (the level-k roots are level-(i+1) roots, off(k) ≡ off(i+1) mod L^{i+1}).
(a) Lemma FT (i) (BFT_B §29.2, PROVEN there): the axial paths of a block stay inside it, so h_i^Tδ_{Y_{i+1}}
is carried by level-i links (Y_i + z, c) with z_c ∈ {−1, 0} and z_ν ∈ [−1, 1] for ν ≠ c — the *longitudinal*
index of the h-kernel is restricted to two values. One transpose step is
(Q_str^Tψ)(z, m) = L^{−d}Σ_{j<L}ψ(Y(z, m, j), m) with Y_ν = ⌊z_ν/L⌋ (ν ≠ m) and Y_m = ⌊(z_m − j)/L⌋, so the
composite longitudinal stencil of (Q_str^{(0→i)})^T overhangs a level-i block by n_i − 1. The two effects
cancel **exactly**: the longitudinal fine range is
[off(k) − off(i) − n_i, off(k) − off(i) + 2n_i − 2], whose ends are off(k) ∓ (3n_i − 1)/2 = off(k) ∓ (L^{i+1}−1)/2
— precisely the level-(i+1) block, with equality at both ends.
(b) sup|Q_str^Tψ| ≤ L^{−d}·L·sup|ψ| = L^{1−d}sup|ψ|, iterated i times from |h_i^Tδ| ≤ 1 (Lemma FT (i)'s
|c(X, b)| ≤ 1). (c) ‖Q_str^Tψ‖_1 ≤ L‖ψ‖_1 (each fine link receives from ≤ L level-i links at weight L^{−d},
and each level-i link reaches L^{d+1} fine links), iterated from ‖h_i^Tδ‖_1 = L^{−d}Σ_y|y − c_X|_1 = 8/3
(no cancellation: a μ-link on the + side of c_X is traversed only forward, one on the − side only backward).
(d) is the coordinatewise form of the transpose chain in the proof of (a). ∎
*Checked:* ys1 A2 (a),(b) PASS at i = 0, 1 (brute transpose dict, 216 and 23328 links); ys1 A3 PASS (the
transpose path reproduces the forward pipeline exactly); ys1b B1 PASS for (b),(c) at i = 0,…,4.
**(c) as an EQUALITY is FALSE and was pre-registered as one: ys1 A2 clause (c) is a disclosed FAIL** —
‖K_1‖_1 = 56/9 < 8, and the exact values 8/3, 56/9, 488/27, 4376/81, 39368/243 give ‖K_i‖_1/n_i → 2, not 8/3.
The inequality is what is derivable and what every bound below uses. See §3.

*Normalisation, stated so that no spurious power of n can enter.* Q_str^{(0→i)} maps own level-0 1-forms to
own level-i 1-forms and multiplies **constants by L^i** (it is a line integral over n_i fine links, averaged
over transverse translates), so it carries no hidden L-power; h_i has dimensionless kernel mass 8/3 (the mean
axial path length in level-i steps); hence Φ_k(v) is in the units of a **gauge function**, the same units as
μ in Proposition TGAUGE, and **Φ_k(v)/sup_own|v| is dimensionless and carries no k**. The only L-powers in
the (TENT-Q) functional are therefore the explicit n² = L^{2k} of 𝒯_p and the own→coarse conversion
‖v^c‖_∞ = n·sup_own|v| — exactly as TENTQ §2.8 (iii) records, and §35.7's L^{2k−3} = n²/27.
**This normalisation is verified exactly, with no free parameter: ys1 A5 PASS** —
Φ_k(dδ_{c_X})(c_X) = L^{−dk} − 1 exactly at k = 1 (−80/81) and k = 2 (−6560/6561), which is Proposition
TGAUGE (TENTQ §2.7) evaluated on a δ, an **outside formula** that a wrong root offset, a wrong level count or
a telescoping error would each break.

### 2.2 Theorem YS-AVG (the exact block average of the |z|^{−3} profile, and its power of n): PROVEN-HERE + COMPUTED

*Statement (the power).* Let v be the admissible profile (1 + |b − p|_∞)^{−3} of BFT_A §38.7 (C_0 = 1,
d = 4). Then, with n_i = L^i the block side:

  **(i) PROVEN. LImax_i := max{|Q_str^{(0→i)}v|(ℓ) : ℓ a level-i link of the level-(i+1) block of c_X}
      ≤ 64·n_i^{−2} + 12·n_i^{−3},  and  |φ_{i+1}(v)| := |⟨K_i, v⟩| ≤ 96·n_i^{−2} + 12·n_i^{−3}.**
  **(ii) COMPUTED (exact, i ≤ 6). LImax_i·n_i² = 11.411, 14.285, 15.918, 16.722 at i = 3, 4, 5, 6,
      monotone and convergent; −log_L(LImax_{i+1}/LImax_i) = 1.796, 1.901, 1.955 → 2.**
  **(iii) COMPUTED (exact, i ≤ 6). The FULL normalised block average BA_i := n_i^{−d}Σ_{|z−p|_∞≤(n_i−1)/2}v(z)
      obeys BA_i·n_i³ = 18.686, 25.183, 28.886, 30.676 at i = 3, 4, 5, 6, and
      −log_L(BA_{i+1}/BA_i) = 2.728, 2.875, 2.945 → 3.**

**So the block-averaged axial line integral of a |z|^{−3} field over a block of side n_i is Θ(n_i^{−2}),
while a full block average of the same field over the same block is Θ(n_i^{−3}). The line integral loses
exactly one power of n_i.** Pre-registered failure mode **YS-F1 does not occur** (ys1b B2: LI and LImax land
in band **(V-2)**, BA in band **(V-3)**, the two bands disjoint by construction; ys1b B3: the scaled
constants LImax_i·n_i² and BA_i·n_i³ are each monotone and change by 5.1% and 6.2% from i = 5 to i = 6,
inside the pre-registered 15%).

*Proof of (i), and the dimension count asked for (target Y4), stated explicitly.*
The kernel of Q_str^{(0→i)} at one level-i link has sup L^{−di}·max_w mult_i(w) ≤ L^{−di}·n_i = n_i^{1−d},
and its stencil lies in a fine box of side ≤ 2n_i. By §2.1 (b) the same sup bound holds for K_i, whose
support is the level-(i+1) block, a fine box of side L·n_i. Hence
|⟨K_i, v⟩| ≤ sup|K_i|·‖v‖_{ℓ¹(supp K_i)} ≤ n_i^{−3}·C_0·T(S), S := (L^{i+1} − 1)/2 ≤ (3/2)n_i, where
T(S) := Σ_{s=0}^{S}N(s)(1+s)^{−3} with the ℓ^∞ shell count N(0) = 1, N(s) = (2s+1)^4 − (2s−1)^4 = 64s³ + 16s.
Since 64s³/(1+s)³ < 64 and Σ_{s≥1}16s/(1+s)³ ≤ 16(π²/6 − 1) = 10.32, **T(S) ≤ 64S + 11.32 ≤ 96n_i + 12**,
giving (i). The same with S ≤ n_i gives the LImax clause. ∎

**The dimension count, in one paragraph — this is the crux the brief flagged.** In d dimensions, with block
side n_i:

| object | per-link kernel weight | kernel ℓ¹ mass | directions averaged |
|---|---|---|---|
| full normalised block average | n_i^{−d} | 1 | **d** |
| block-averaged axial line integral (h_i∘Q_str^{(0→i)}) | n_i^{−(d−1)} | n_i | **d − 1** |

An axial line integral **averages over the n_i^{d−1} transverse translates of the line inside the block and
SUMS along the remaining direction.** That is one averaging fewer than a block average, and it shows up
twice — one power of n_i in the per-link weight and one in the ℓ¹ mass. Paired against the profile it gives
n_i^{−(d−1)}·‖v‖_{ℓ¹(block)}, and in **d = 4 with exponent 3** the marginal count is
‖v‖_{ℓ¹(block)} = Σ_{s≤n_i}N(s)(1+s)^{−3} ≍ 2d·2^{d−1}·n_i = 64n_i — **linear in n_i, with no logarithm**,
because d − 1 − 3 = 0 exactly. Hence n_i^{−3}·64n_i = 64n_i^{−2}, and a full block average would have given
n_i^{−4}·64n_i = 64n_i^{−3}, which is the figure the brief conjectured. The brief's O(n^{−3}) is the right
answer **for the wrong operator**; the right operator gives O(n^{−2}). The marginality is worth recording:
at profile exponent 4 the ℓ¹ mass would be O(1) and the line integral would give n_i^{−3}; at exponent 2 it
would be n_i² and the line integral would give n_i^{−1}. The exponent 3 is exactly the one Theorem YH's
𝒩(Y^p) ≤ C_YN·n forces (REVIEW_BFT_B_S9_S10 S10-14), so the answer is pinned by that input and by nothing
else.

### 2.3 Theorem YS-CORE (Φ_k at the core of a |z|^{−3} field is Θ(1), k- and T-uniformly, bounded both ways): PROVEN-HERE (upper) + COMPUTED exact (lower)

*Statement.* For the admissible profile class |v(b)| ≤ C_0(1 + |b − p|_∞)^{−3} at m = 0, trivial background,
d = 4, L = 3, uniformly in k ≥ 2, in the torus side T, in X and in p:

  **(i) PROVEN (upper). |Φ_k(v)(c_X)| ≤ [8/3 + Σ_{i≥1}(96L^{−2i} + 12L^{−3i})]·C_0 = 15.13·C_0.**
      Sharpened with §2.2 (ii)'s exact values for i ≤ 6 and the proven tail for i ≥ 7:
      **|Φ_k(v)(c_X)| ≤ 3.89·C_0** (COMPUTED + PROVEN tail).
  **(ii) COMPUTED, exact (lower). For u := ⅛d*δ_p with p the (0,1)-plaquette at c_X + (1,0,0,0) — co-closed,
      admissible with C_0 = 1 (|u(b)| ≤ (1 + |b − z_0|_∞)^{−3}, equality at distance 1), and the very field
      BFT_A §38.7 takes as g_0 — the funnel series TERMINATES:
      φ_1 = −1/432, φ_2 = −17/104976, and φ_3 = φ_4 = φ_5 = 0 EXACTLY, so
      Φ_k(u)(c_X) = −65/26244 = −2.4768e−3 for EVERY k ≥ 2, exactly.**
  **(iii) PROVEN (far field). |Φ_k(v)(c_X)| ≤ C·C_0·(1 + R)^{−2}, R = |c_X − p|_∞**, with C ≈ 1.0e3 from the
      crude constants of §2.2 (i) and ≈ 20 from §2.2 (ii)'s measured ones. The funnel of a |z|^{−3} field has
      a **line-integral profile |·|^{−2}**, not a |·|^{−3} one.

*Proof of (i).* Sum §2.2 (i) over i, improving the i = 0 term by
|⟨K_0, v⟩| ≤ ‖K_0‖_1·sup|v| = (8/3)C_0 (§2.1 (c)). Σ_{i≥1}96L^{−2i} = 12 and Σ_{i≥1}12L^{−3i} = 6/13. ∎
*Proof of (iii).* Split at L^{i+1} ≤ R. For those levels supp K_i lies in a ball of radius < R/2 about c_X,
so sup_{supp}|v| ≤ 8C_0R^{−3} and |φ_{i+1}| ≤ ‖K_i‖_1·8C_0R^{−3} ≤ (64/3)C_0n_iR^{−3}; Σn_i ≤ R/2 over
those i, giving ≤ (32/3)C_0R^{−2}. For the remaining levels n_i > R/L, so n_i^{−2} < L²R^{−2}, and
§2.2 (i) summed geometrically gives ≤ (96·9·9/8)C_0R^{−2} + O(C_0R^{−3}). ∎
*On (ii).* φ_{i+1}(u) = 0 for i ≥ 2 because Q_str^{(0→i)}u = 0 on the level-i links h_i reads once both
links of u in each direction are interior to one straight-average block: the two same-direction entries of
d*δ_p sit at transversely adjacent sites and cancel under the transverse average, and only a block boundary
separating them can prevent it, which happens at i = 1 and i = 2 for this placement and never again. The
exact values are a **rebuild** of REVIEW_BFT_A_S8 S8-7's independently produced rationals (ys1 A1 PASS: all
four of φ_1 = −1/54, φ_2 = −17/13122, ratio 17/243, ψ_u = −65/26244 for the unnormalised u), extended to
k = 5 here (ys1b B4 PASS, including the covariance clause).

*Reading, and it is the answer to the question.* **0.00248·C_0 ≤ max_X|Φ_k(Y^p_{*,0})(c_X)| ≤ 3.89·C_0, both
bounds uniform in k and T.** The funnel of a field with a |z|^{−3} core is Θ(C_0): the averaging neither
grows nor decays with k. It is the **same order as the sup** of the field, which is Θ(C_0) — so in the
block-averaged norm the funnel actually uses, there is **no gain in any power of n over the sup norm at the
core.**

### 2.4 Theorem YS-DEC (the decision asked for): the averaging does NOT beat the core

**(a) (TENT-osc) is FALSE, by exactly n² = L^{2k}. PROVEN as an implication; CONDITIONAL on the profile input.**
(TENT-osc) (TENTQ §2.8 (iv)) asks n²·osc_𝔅(Φ_k(Y^p_{*,0})) ≤ C_osc uniformly in k, T, p, 𝔅, i.e.
max_𝔅|Φ_k| ≲ n^{−2} once Proposition TQ-NOGAIN's osc = max is granted. At the coarse cell containing p,
§2.3 (ii) gives ≥ 2.4768e−3·C_0 and §2.3 (i) gives ≤ 3.89·C_0, both k-independent, so
n²·osc_𝔅(Φ_k) ≥ 2.4e−3·C_0·n² and the inequality fails **by exactly the full n² = L^{2k}**, with nothing
gained from the averaging. The pre-registered failure modes **YS-F2 and YS-F3 do not occur.**
*And osc does not help at the core, independently of TQ-NOGAIN's hypothesis:* by §2.3 (iii) Φ_k falls from
Θ(C_0) at R = O(1) to O(C_0n^{−2}) one coarse step away, so osc_𝔅 ≍ max_𝔅 at p's cell whether or not Φ_k has
a zero there. (In the **far** field, where Φ_k has no zero and TQ-NOGAIN's hypothesis fails, osc does buy one
extra power of the coarse distance — see (c) — so TQ-NOGAIN is confirmed exactly where it is stated and
sharpened exactly where it is not.)

**(b) Why, structurally — and this is the point the brief named.** The brief's framing is that "the core of a
|z|^{−3} field is a vanishing fraction of a block". **The block in Φ_k is the level-(i+1) block, not the
level-k block.** By §2.1 (a), the i-th term of Φ_k reads v **only** inside the level-(i+1) block of c_X,
of fine side L^{i+1}. At **i = 0** that block has side L = 3 and n_0 = 1: the core of the field is not a
vanishing fraction of a 3^4 block, it is the whole of it, and the gain is n_0^{−2} = 1. Consequently:

> **The power of the averaging is not what decides the question. The presence of the i = 0 level is.** Even
> if the per-level gain had been the brief's hoped-for n_i^{−3}, Φ_k = Σ_{i<k}Θ(n_i^{−3}) = Θ(1) still, with
> the i = 0 term dominating. Only a funnel whose *smallest* block grew with k could beat the core, and Φ_k's
> smallest block has side L for every k.

The quantitative confirmation is that the i = 0 term carries 93% of Φ_k on the exact witness
(φ_1/Φ_k = (−1/432)/(−65/26244) = 0.9346) and that the higher terms are **exactly zero** from i = 2 on.

**(c) What IS delivered, and it is not nothing: (TENT-Q) is k-uniform away from p's coarse cell.**
Combining §2.3 (iii) with Corollary TQ-osc (TENTQ §2.5): for a chain source S supported in a coarse cell at
coarse distance R_c ≥ 1 from p's cell,
  **|𝒯_p(S)| ≤ 128·n²·osc_𝔅(Φ_k)·Σ_lπ_l(S_l) ≤ 128·C·C_0·R_c^{−3}·Σ_lπ_l(S_l),**
using osc_𝔅 ≍ C_0·n^{−2}R_c^{−3} across one coarse step of the R^{−2} profile (one power of R_c better than
the max). This is **k- and T-uniform, with an absolute constant**. So (TENT-Q) is not globally false: it is
false **only** for sources meeting p's own coarse cell, and there by exactly n². *Status: ARGUED* — §2.3 (iii)
is PROVEN but the one-coarse-step oscillation of the R^{−2} profile is estimated, not computed.

> **(TENT-osc) should therefore be restated, not carried as written:** the correct open item is the **core
> contribution alone**, n²·osc over the single coarse cell containing p, and it is **FALSE** there for any
> representative whose level-0 field has the |z|^{−3} core. Everything outside that cell is settled with an
> explicit R_c^{−3} decay.

**(d) (Y-sup^loc): the block average does not clear it either — it fails by exactly n.** (Y-sup^loc) demands
n·max_own|Y^p_{*,0}| ≲ C, i.e. max_own ≲ C/n. The own sup is Θ(C_0) (the profile's value at the links next
to p), so it fails by n — which REVIEW_BFT_B_S9_S10 S10-14 and TENTQ §2.8 (iii) already say. The question
asked here is whether the **averaged** currency rescues it, and the answer is **no**: §2.3 shows the funnel's
own block-averaged reading of the same field is also Θ(C_0), the same power, so substituting the averaged
norm for the sup gains **nothing** and the shortfall is still exactly n = L^k. **YS-F1's expectation holds
and the rescue fails at the threshold 1/n by one full power.**

### 2.5 Proposition YS-PHI ((Φ-conv) is PROVEN for the |z|^{−3} profile class): PROVEN-HERE

*Statement.* For every v with |v(b)| ≤ C_0(1 + |b − p|_∞)^{−3}, the funnel series Φ_l = Σ_{i<l}φ_{i+1}
converges geometrically with ratio L^{2−d} = L^{−2} = 1/9:
  **|φ_{i+1}(v)| ≤ C_0(96L^{−2i} + 12L^{−3i}),  so  Σ_{i≥0}|φ_{i+1}(v)| ≤ 15.13·C_0 < ∞,**
uniformly in k and T. *Proof:* §2.2 (i). ∎
*Consequence, and it discharges a named conditionality.* TENTQ §4.4's last bullet and its lane-A request 2
record that **every quantitative tent statement in this project, including §35.7's L^{2k−3}, is CONDITIONAL
on (Φ-conv)**, which is exact at i = 1 (ratio 17/243) and ARGUED above. **Within the (1 + |z|_∞)^{−3}
profile class at d = 4 this file removes that conditionality**: the ratio is bounded by L^{−2} = 0.1111 by a
proof, and the prior exact value 17/243 = 0.0700 sits under it (ys1 A1, rebuilt). The measured asymptotic
ratio of the *averaging itself* is L^{−2} to three figures (ys1b B2: ρ → 1.796, 1.901, 1.955). **So every
statement in §2 is unconditional on (Φ-conv)**, and that is the one input the brief asked to be checked for.
*What is NOT discharged:* (Φ-conv) for fields **outside** this profile class, which is what §35.7's general
L^{2k−3} needs. Outside the class the crude bound (each Q_str step multiplies the own sup by L) stands, and
nothing here improves it.

### 2.6 Proposition YS-GT (the λ^E face is NOT rescued by averaging either — it is rescued by its THRESHOLD): ARGUED

*Statement.* Pre-registered failure mode **YS-F5 occurs, but not for the reason pre-stated.** The two faces
do consume different averaging operators — Φ_k's kernel is an O(1)-weight local sum on the level-1 block
(§2.1), λ^E's is the box dipole A^X_{c_X} − A^X_z of Lemma ΓT-op (a) — but **both objects are Θ(C_0)**. The
asymmetry is in the thresholds, not in the averaging:
- **(GT-sup)** (BFT_B §27.4) asks sup|λ^{Γ_E}_*(p)| = **O(1)**;
- **(TENT-osc)** asks max|Φ_k| = **O(n^{−2})**, because 𝒯_p carries an explicit n².
*The estimate.* λ^E_X(x)(z) = ⟨A^X_{c_X} − A^X_z, x_0⟩ with A^X_w = d G_X(·, w), G_X the Neumann Green's
function of Ñ_X. In d = 4, |A^X_w(b)| ≍ |b − w|^{−3} away from ∂Ñ_X, so pairing against a second |·|^{−3}
field is the **same marginal convolution** as §2.2: Σ_b|b − w|^{−3}|b − p|^{−3} ≍ |w − p|^{−2} for
|w − p| ≥ 1. Hence
  **|λ^E_X(Y^p)(z)| ≲ C_0[(1 + |c_X − p|_∞)^{−2} + (1 + |z − p|_∞)^{−2}] = O(C_0), k- and T-uniformly,**
which **is** (GT-sup) — delivered **without** (Y-sup^loc), which is false. The factor n that Proposition
GT-loc loses is exactly the ℓ¹ × sup step discarding this convolution: ‖(λ^E_X)^Tδ_z‖_1 ≈ 10.6n (bb8t T1)
times sup_own|Y^p_0| ≈ C_0 gives O(nC_0) where the pairing gives O(C_0).
*Status: ARGUED, with the hole named.* It needs the box Green's-function gradient profile
|A^X_w(b)| ≲ |b − w|^{−3} on Ñ_X with Neumann boundary conditions — a classical lattice estimate, **not
proven here and not checked here** (ys1b criteria scope limitation 4). Independent corroboration, quoted and
not produced here: lane A measures σ ≈ 0.003 at the roots next to p, k-independent at k = 2 and 3 (ba8), and
REVIEW_BFT_B_S9_S10 S10-14 records GT-loc as "off by about a factor n relative to the measured object" —
which is exactly the factor this estimate recovers.

### 2.7 Assessment of TENTQ §2.10's Hölder fallback: the right move for face (a), and no help at all for face (b). ARGUED

TENTQ §2.10 proposes taking [f_0]^∞_α from Proposition NCR's **difference** form,
f_0^{Γ_E}(S)(p) − f_0^{Γ_E}(S)(p′) = ⟨S, Y^p_* − Y^{p′}_*⟩ + ⟨D(S), λ^{Γ_E}_*(p) − λ^{Γ_E}_*(p′)⟩,
so that the Hölder half never needs ‖Γ_E^TD(S)‖_∞ and (P0-sup) disappears. Assessment, in three parts:
1. **It removes (P0-sup) completely, and that is correct.** No sup of the slice correction appears in the
   difference form; the quantity that TENTQ §2.10 shows to be genuinely ≍ n^d‖D‖_∞ never enters. This is a
   strict improvement over routing the Hölder half through LES-div on the corrected source.
2. **It lands on an object this file controls, with one power of decay to spare.** The second term needs
   sup|λ^{Γ_E}_*(p) − λ^{Γ_E}_*(p′)| on supp D(S). By §2.6's convolution the p-difference at separation
   ρ = |p − p′| carries one more derivative of the |·|^{−3} kernel, giving
   |λ_*(p)(z) − λ_*(p′)(z)| ≲ C_0ρ(1 + |z − p|_∞)^{−3} for ρ ≤ |z − p|, i.e. a **local Lipschitz** bound and
   hence [·]_α for every α ≤ 1 with the same O(C_0) size. So the Hölder half becomes a Hölder (GT-sup) of
   the same strength as (GT-sup) itself, not a stronger statement — the fallback does **not** trade one open
   item for a harder one. *ARGUED, and it inherits §2.6's named hole (the box Green's-function profile).*
3. **It does nothing for (TENT-osc).** §2.10's proposal is explicitly about face (a), the Hölder half. Face
   (b) is the curvature-half residue D^root paired with the funnel (BFT_B §36.1's table), it carries the
   explicit n² of 𝒯_p, and no Hölder reformulation removes that n². **The fallback is a repair for (P0-sup)
   and (GT-sup) and leaves (TENT-osc) exactly where §2.4 leaves it.**

*What else could repair face (b), in decreasing order of credibility (statements only, none claimed here).*
(α) **Restrict the claim to its true domain** — §2.4 (c): (TENT-Q) is k-uniform for sources outside p's
coarse cell with an explicit R_c^{−3}, and the open item is the single core cell. This is a restatement, not
a repair, but it is PROVEN-grade and it shrinks the item by a factor T^d.
(β) **Use the representative freedom.** Proposition TGAUGE (TENTQ §2.7) makes Φ_k a representative artefact:
there is μ ∈ Λ_* with A^{(0→k)}μ = −Φ_k, for which the residue vanishes identically. TENTQ §2.7 prices this
as an **equal** cost in the main pairing, *ARGUED* — the single most valuable thing to settle, because if the
price is strictly smaller the tent face is free. It is a question about one explicit μ and it is cheap.
(γ) **Pair D^root against the funnel exactly rather than through Hölder.** D^root and Φ_k are both
root-supported objects with computable profiles (§2.3 (iii) gives Φ_k's); the n² may be absorbed by the
own-unit size of D^root at high-level roots, which GT-attr (BFT_B §36.3) already identifies as the
k-growing factor. Not attempted here.
(δ) A larger-than-n^{−2} threshold, i.e. a restatement of (TENT-Q) that does not carry n². Not available
from anything read here.

### 2.8 What is NOT reached, plainly

1. **No response field is computed anywhere.** Every statement about Y^p_{*,0} is a statement about the
   **profile class** |v| ≤ C_0(1 + |z − p|_∞)^{−3}, which is a **named input** (BFT_A §38.7's g_0 bound;
   Theorem YH's 𝒩 ≤ C_YNn via REVIEW_BFT_B_S9_S10 S10-14). Whether the actual Y^p_{*,0} = g^♮ + Z''_0 +
   Σ_qG_e(q)Y^q_0 has a core of that size, and whether Z''_0's funnel could cancel g_0's, is **not decided
   here**. The lower bound §2.3 (ii) is exact for the single field u = ⅛d*δ_p, which BFT_A §38.7 and
   REVIEW_BFT_A_S8 S8-7 treat as a legitimate g_0; it is not a statement about the assembled response.
2. **Nothing at m > 0, θ > 0, a nontrivial background, or about N.** §2.0.
3. **The upstream factor k is untouched.** REVIEW_BFT_B_S9_S10 Part J (binding fix RS10-1) refutes Corollary
   COF-crit and leaves the level count k (or ≈ 25(k − 1) through ‖·‖_Pc) **upstream** of (TENT-Q),
   (Y-sup^loc) and everything in §2. **This file accepts that finding and claims no k-uniformity for
   (NC-Γ).** Every statement above is k-uniform **in its own right** — no constant in §2 contains k — which
   is a different and weaker thing, and §2 says so wherever it matters. In particular nothing here is
   evidence about k-uniformity: k ≤ 5 throughout.
4. **λ^E is never computed.** §2.6 and §2.7 are analytic and rest on an unproven lattice Green's-function
   profile.
5. **k ≤ 6 for the averaging, k ≤ 5 for the funnel.** The powers in §2.2 are asymptotic reads of four and
   three ratios respectively, with the convergence disclosed (5.1% and 6.2% at the last step) and the
   analytic bound (i) covering all i.

## 3. Check record, with a per-check statement of discriminating power (written after §2)

Files, all in `checks/`: `ys1_criteria.md` (14:54 UTC, **before** the script), `ys1_funnel.py` (ran 14:57,
0.99 s real, 101 MB peak), `ys1_out.txt`, `ys1_err.txt`; `ys1b_criteria.md` (15:06 UTC, written before its
script, declaring the two repairs **before** any new number was produced), `ys1b_power.py` (ran 15:01,
1.48 s, 22 MB, **aborted at clause B5**), `ys1b_out.txt`, `ys1b_err.txt`; `ys1b2_control.py` (clause B5
alone, ran 15:02), `ys1b2_out.txt`, `ys1b2_err.txt` (empty). Exact `fractions.Fraction` / Python ints,
plain `python3 -I`, `nice -n 10`, all thread variables = 1, no numpy, no BLAS, single thread, **no numeric
lock taken** (DRIVE_BRIEF rule 6 exempts exact rational arithmetic). Load at start 1.63 and 1.45.

**Two FAILs are reported, both disclosed and neither repaired in place.** `ys1_criteria.md` was **not
touched**; `ys1_funnel.py`, `ys1_out.txt` and `ys1_err.txt` are kept unaltered with their FAILs; the repairs
were pre-registered in a **new** criteria file under a **new id** before the re-run.

| id | verdict | what it is tested **against** | could it have failed? |
|---|---|---|---|
| **ys1 A1** rebuild of S8-7's four rationals | **PASS** (exact, all four) | an **independent prior computation in another file and another session** (REVIEW_BFT_A_S8 S8-7: −1/54, −17/13122, 17/243, −65/26244), rebuilt here from the axial 24-order construction and Q_str | **HIGHEST against an outside number.** Any error in the axial weights, the root offsets, Q_str, the plaquette convention or the normalisation fails it. **A7 proves it can fail** (see below) |
| **ys1 A2 (a)** supp K_i ⊆ level-(i+1) block | **PASS** (i = 0, 1, both link endpoints) | Lemma FT (i) (BFT_B §29.2), a closed statement from another file | **MEDIUM-HIGH.** The fit is **exact and non-obvious**: the h-kernel's longitudinal range {−1,0} and the Q_str^T overhang n_i − 1 cancel to the block edge with **equality at both ends**, so a one-site error in either would fail it |
| **ys1 A2 (b)** sup\|K_i\| ≤ L^{i(1−d)} | **PASS** (i = 0, 1; **ys1b B1** at i ≤ 4) | the one-step ℓ^∞ gain derived in §2.1 | **MEDIUM.** It is the clause every bound of §2.2 rests on; a wrong Q_str^T would fail it. Measured exact value (10/81)L^{−3i}, a factor 8.1 under the bound |
| **ys1 A2 (c)** ‖K_i‖_1 **=** L^i·(8/3) | **FAIL** — ‖K_1‖_1 = 56/9, not 8 | the same closed form, asserted as an **equality** | it **did** fail. The criterion was wrong: only "≤" is derivable, because the Q_str^T stencils of oppositely-signed level-i links overlap. **No statement in §2 uses the equality**; §2.1 (c) states "≤" and ys1b B1 confirms it at i ≤ 4, with the exact asymptote ‖K_i‖_1/n_i → 2 |
| **ys1 A3** forward pipeline = transpose kernel | **PASS** (exact, both i) | **two disjoint code paths**: `phi_terms`→`qstr`→`hfun` against `hT`→`qstrT`→pairing. Neither calls the other and neither is the other's transpose by construction | **MEDIUM-HIGH.** A sign error in either transpose, or a wrong avatar, fails it |
| **ys1 A5** Φ_k(dδ_{c_X}) = L^{−dk} − 1 | **PASS** (exact, k = 1 and 2) | **an outside formula with no free parameter**: Proposition TGAUGE (TENTQ §2.7), proven in another file this session did not write | **HIGH.** It pins the whole normalisation at once: a wrong root offset, a wrong level count, a wrong block convention or a telescoping error each break it. It is the check that forecloses a spurious power of n |
| **ys1 A6** k-uniform lower bound at k = 3 | **PASS** | (a) level/translation covariance against A1's k = 2 values; (b) the head against the proven geometric tail bound (ratio 93.9) | **HIGH for (a)** — a wrong off(3) fails it; **MEDIUM-HIGH for (b)** |
| **ys1 A7** DESIGNED-FAIL CONTROL (off(l) := 0) | **PASS of the control** — it returned 0, **not** −1/54 | itself | **this is the power measurement.** It establishes that A1 and A3 are capable of failing, which four findings in session 24 were not |
| **ys1 A4** band test on the staircase field, i ≤ 3 | **FAIL (V-other)** | BA_i computed from the same data by a different operator | it **did** fail. Two named causes, both real: the L-adic staircase understates the profile non-uniformly, and i ≤ 3 with the i = 0 → 1 ratio included is not asymptotic. Repaired under a new id |
| **ys1 A8** bands distinguish LI from BA | **FAIL** (consequence of A4) | — | consequential only |
| **ys1b B1** repaired A2 (c): the inequality | **PASS** (i ≤ 4, both clauses) | the two closed forms of §2.1, as inequalities | **MEDIUM.** A violation would refute the one-step gains §2.2 rests on |
| **ys1b B2** THE DISCRIMINATING CHECK | **PASS, (V-2) for LI and LImax, (V-3) for BA** | **BA_i, an independent operator on the same data, landing in the other band** — so the instrument demonstrably reads both answers | **HIGH, and the session's conclusion turns on it.** Pre-registered to be able to reverse the verdict: LI in (V-3) would have meant the averaging beats the core. It did not. ρ^{LI} = 1.796, 1.901, 1.955 against ρ^{BA} = 2.728, 2.875, 2.945 |
| **ys1b B3** scaled constants converge | **PASS** | a stricter read of the same data than the band test: a wrong power drifts by L per level and 15% cannot absorb it | **HIGH.** LImax·n² = 11.41→16.72 (Δ 5.1% at the last step), BA·n³ = 18.69→30.68 (Δ 6.2%) |
| **ys1b B4** φ_i of u at k = 5 | **PASS** (covariance clause) | A1's k = 2 values | **MEDIUM-HIGH for the gate.** The **values** φ_3 = φ_4 = φ_5 = 0 exactly are COMPUTED measurements with no PASS/FAIL attached, as the criteria said in advance |
| **ys1b B5** DESIGNED-FAIL CONTROL (flat multiplicity) | **PASS of the control** (run as `ys1b2`) | itself | **this is the power measurement for the new pipeline.** It confirms the pipeline is sensitive to the one feature the whole argument turns on — that an axial line integral **sums** rather than averages along its direction. `ys1b_power.py` **aborted** at this clause when its internal mass check (Σ_s c_s = L^{i(d+1)}) caught the corruption (135 against 243); that abort is kept in `ys1b_err.txt` unaltered, and `ys1b2_control.py` re-runs the clause alone with the mass check reported rather than raised. B1–B4 had already printed and are unaffected |

**What these checks do NOT test, stated plainly.**
1. **Nothing nonabelian.** §2.0 argues from BFT_B §24.0 and §16.1 (f) that a scalar model is *complete* for
   every identity in §2; it would be **vacuous** for a background statement, and §2 makes none.
2. **No response field.** v and u are stand-ins for the **profile class**; the class membership of
   Y^p_{*,0} is a named input (§2.8 (1)).
3. **No λ^E.** §2.6 and §2.7 are unchecked analysis and are labelled ARGUED.
4. **No level count.** k ≤ 6; a factor k cannot be measured there and none is claimed.
5. **The positive profile v is a bad lower-bound witness and was not used as one.** For a field positive and
   near-symmetric about c_X, h_0's signed weights cancel and φ_1 can vanish; v measures only the **power**
   of the averaging (the upper-bound/scaling question of Y2). The lower bound uses the co-closed u, where
   the exact value is nonzero. This separation was pre-registered in `ys1_criteria.md`'s scope limitation.

## 4. Outcome (written after §3)

### 4.1 Outcome table

| object | status | content |
|---|---|---|
| **Proposition YS-K** (Φ_k's exact kernel form) | **PROVEN-HERE** | Φ_k(v)(c_X) = Σ_{i<k}⟨K_i, v⟩, K_i = (Q_str^{(0→i)})^T h_i^Tδ_{Y_{i+1}}; supp K_i = **exactly** the level-(i+1) block (both ends attained); sup\|K_i\| ≤ n_i^{−3} (exact (10/81)n_i^{−3}); ‖K_i‖_1 ≤ (8/3)n_i (exact asymptote 2n_i). Normalisation pinned by ys1 A5 against TGAUGE |
| **Theorem YS-AVG** (the block average, with its power) | **PROVEN-HERE** (bound) + **COMPUTED** (power, exact, i ≤ 6) | the block-averaged axial line integral of a \|z\|^{−3} field over a block of side n_i is **Θ(n_i^{−2})** — measured constant 16.72 → ≈ 17.5 at C_0 = 1 — while a **full** block average of the same field over the same block is **Θ(n_i^{−3})** — measured 30.68 → ≈ 32. The line integral loses **exactly one power of n_i**, because it averages d − 1 = 3 directions and sums along the fourth. **YS-F1 does not occur** |
| **the dimension count** | **PROVEN-HERE** | n_i^{−(d−1)}·‖v‖_{ℓ¹(block)} against n_i^{−d}·‖v‖_{ℓ¹(block)}, with ‖v‖_{ℓ¹(block)} ≍ 64n_i **linear and log-free** because d − 1 − 3 = 0 exactly at d = 4. The profile exponent 3 is marginal and is the one Theorem YH forces |
| **Theorem YS-CORE** | **PROVEN-HERE** (upper) + **COMPUTED exact** (lower) | **0.0024768·C_0 ≤ max_X\|Φ_k(v)(c_X)\| ≤ 3.89·C_0** (crude proven form 15.13·C_0), uniform in k, T, p. For u = ⅛d*δ_p the series **terminates**: φ_3 = φ_4 = φ_5 = 0 exactly and Φ_k(u) = −65/26244 for **every** k ≥ 2 |
| **far-field profile** | **PROVEN-HERE** | \|Φ_k(v)(c_X)\| ≤ C·C_0(1 + \|c_X − p\|_∞)^{−2}: the funnel of a \|z\|^{−3} field has a **line-integral \|·\|^{−2} profile**, not a \|·\|^{−3} one |
| **>>> THE DECISION: does the averaging beat the core?** | **NO. DECIDED.** | **PROVEN as an implication from the profile input.** The averaging gains n_i^{−2} at level i, which is real; but Φ_k is a **sum over levels starting at i = 0**, whose block has fine side L = 3 and whose gain is therefore L^0 = 1. The i = 0 term carries 93% of Φ_k on the exact witness. **The power of the averaging is not what decides it; the presence of the i = 0 level is** — even a per-level gain of n_i^{−3} would leave Φ_k = Θ(1) |
| **(TENT-osc)** | **FALSE, by exactly n² = L^{2k}** | CONDITIONAL on the profile input (BFT_A §38.7 / Theorem YH). Not OPEN any more at the core: n²·osc_𝔅 ≥ 2.4e−3·C_0·n² at p's coarse cell, and osc ≍ max there independently of TQ-NOGAIN's hypothesis. **YS-F2, YS-F3 do not occur** |
| **(TENT-Q) away from p's cell** | **ARGUED, k- and T-uniform** | \|𝒯_p(S)\| ≤ 128·C·C_0·R_c^{−3}·Σ_lπ_l(S_l) for S in a coarse cell at coarse distance R_c ≥ 1. So (TENT-Q) is **not globally false**; the open item shrinks to the **single coarse cell containing p**, by a factor T^d |
| **(Y-sup^loc)** | **FALSE by exactly n; and the averaged currency does not rescue it** | the own sup is Θ(C_0), the threshold C/n; the funnel's block-averaged reading of the same field is **also** Θ(C_0), the **same power**, so substituting the averaged norm gains nothing. **This answers the brief's question 3 for face (a) too: it fails, by one full power of n** |
| **Proposition YS-PHI ((Φ-conv))** | **PROVEN-HERE for the (1+\|z\|_∞)^{−3} class** | geometric with ratio L^{2−d} = L^{−2} = 1/9; the prior exact i = 1 ratio 17/243 = 0.0700 sits under it, and the measured asymptotic ratio is L^{−2} to three figures. **Every statement in this file is therefore UNCONDITIONAL on (Φ-conv).** Not discharged outside the class, which is what §35.7's general L^{2k−3} needs |
| **Proposition YS-GT** (the λ^E face) | **ARGUED** (hole named: the box Neumann Green's-function gradient profile) | both faces' objects are Θ(C_0); the asymmetry is in the **thresholds** ((GT-sup) wants O(1), (TENT-osc) wants O(n^{−2}) because 𝒯_p carries n²). The exact dipole pairing gives \|λ^{Γ_E}_*\| = O(C_0) **without (Y-sup^loc)**, recovering exactly the factor n that REVIEW_BFT_B_S9_S10 S10-14 measures GT-loc to lose. **YS-F5 occurs, for a different reason than pre-stated** |
| **TENTQ §2.10's Hölder fallback** | **ARGUED assessment: sound for face (a), no help for face (b)** | it removes (P0-sup) entirely; it lands on the same object §2.6 controls, with one extra power of decay from the p-difference, so it is **not** a harder statement than (GT-sup); and it does **nothing** for (TENT-osc), which carries the n² of 𝒯_p and is not a Hölder statement |
| **YS-F4** | **does not occur** | the far field is \|·\|^{−2}, so the failure is strictly a core phenomenon and BFT_B §36.2's own caveat is confirmed |
| **the upstream factor k** | **accepted, not claimed against** | RS10-1 stands. No k-uniformity for (NC-Γ) is claimed anywhere above |

### 4.2 The brief's five questions, answered

1. **Φ_k's exact form and normalisation.** §2.1: Φ_k(v)(c_X) = Σ_{i<k}⟨K_i, v⟩, K_i = (Q_str^{(0→i)})^T h_i^Tδ,
   supported **exactly** on the level-(i+1) block with sup ≤ n_i^{−3} and ℓ¹ ≤ (8/3)n_i. The normalisation is
   fixed and verified against an outside formula (TGAUGE; ys1 A5 exact at k = 1, 2): Φ_k(v)/sup_own|v| is
   dimensionless and k-free, and the only L-powers in the functional are the explicit n² = L^{2k} and the
   own→coarse conversion. **No spurious power of n**; §35.7's L^{2k−3} = n²/27 is reproduced.
2. **The exact block average, with its power of n.** §2.2: **Θ(n_i^{−2})**, measured 16.72·C_0·n_i^{−2} at
   i = 6 and still rising to ≈ 17.5, with −log_L of the ratio = 1.796, 1.901, 1.955 → 2. The brief's
   candidate n^{−3} is the answer for a **full block average** (measured 30.68·C_0·n_i^{−3}, ρ → 3) — the
   right number for the wrong operator.
3. **Does the averaging beat the core?** **NO, and by a margin that no constant can close.** (TENT-osc)
   needs ≲ n^{−2} and gets Θ(1): it **fails by exactly n² = L^{2k}**. (Y-sup^loc) needs ≲ 1/n and the
   averaged currency also gives Θ(1): it **fails by exactly n = L^k**. The averaging gains two powers of the
   **block side** at each level, which is real and is what makes the far field |·|^{−2} and the series
   convergent — but the block side at the binding level i = 0 is L, not n.
4. **The axial dimension count.** §2.2's table: the line integral averages d − 1 = 3 transverse directions
   and **sums** along the fourth, costing one power of n_i in the per-link weight (n_i^{−3} not n_i^{−4})
   and one in the kernel's ℓ¹ mass (n_i not 1). Against a profile whose block-ℓ¹ mass is **marginally**
   linear in n_i (d − 1 − 3 = 0 at d = 4, log-free), that is n_i^{−2} against n_i^{−3}. **And the binding
   level is i = 0, where there is no averaging at all** — which is the crux, and it makes the verdict
   independent of which of the two powers is right.
5. **If it fails, what else could.** §2.7: the Hölder fallback is **correct for face (a)** — it removes
   (P0-sup), and the object it lands on is O(C_0) by §2.6, one power of decay better than (GT-sup) needs —
   and **irrelevant to face (b)**. For face (b) the ranked options are (α) restrict the claim to its true
   domain (PROVEN-grade: everything outside p's coarse cell is k-uniform with an R_c^{−3} decay, shrinking
   the item by T^d), (β) **price Proposition TGAUGE's representative shift exactly** — currently ARGUED as
   an equal cost, and if it is strictly smaller the tent face is free; this is the cheapest high-value item
   left — (γ) pair D^root against the funnel exactly rather than through Hölder, using §2.3 (iii)'s profile.

### 4.3 The single biggest remaining obstruction in this scope

Not the averaging — that is now decided, with exact constants both ways and the mechanism named. It is
**Proposition TGAUGE's price**: Φ_k is a representative artefact that can be gauged to zero (TENTQ §2.7,
PROVEN identity), and the whole of (TENT-osc) would evaporate if the cost of that gauge in Theorem COF's
main pairing were strictly smaller than the tent it removes. TENTQ prices it as **equal**, *ARGUED*, from a
smoothness choice for μ that is "natural but not forced", with **no μ constructed**. That is one explicit
construction and one exact pairing — cheap, local, and it decides whether face (b) is an obstruction at all.
Everything else in this scope is either settled above or sits behind the upstream factor k (RS10-1).

## 5. FOR OTHER FILES (not edited)

**To TENTQ.md's owner — four items, all of them changes to live statements.**
1. **(TENT-osc) is no longer OPEN; it is FALSE at the core, by exactly n², for the profile class, and TRUE
   with an explicit decay elsewhere.** §2.4. Suggested restatement of §2.8 (iv)'s named item: *"(TENT-osc)
   holds for sources outside p's coarse cell, with |𝒯_p(S)| ≤ 128·C·C_0·R_c^{−3}Σ_lπ_l(S_l) at coarse
   distance R_c ≥ 1 (YSUP §2.4 (c), ARGUED); at p's own coarse cell it is FALSE by exactly L^{2k} (YSUP
   §2.3, §2.4 (a)), and the open item is the core cell alone."* This **shrinks** the item by T^d rather than
   closing it, and it removes the word "undecided" from §4.4's third bullet.
2. **§4.4's "whether the averaging beats the core is the live question, and it is not decided here" is now
   decided: it does not.** §2.2 and §2.4. The reason is structural and is worth carrying in one line: Φ_k's
   level-i term reads the **level-(i+1)** block, not the level-k block, so the i = 0 term's block has side
   L = 3 and no averaging occurs there. The brief's framing — that the core is a vanishing fraction of a
   block — is true of the level-k block and false of the one Φ_k actually uses.
3. **(Φ-conv) is PROVEN for the (1 + |z|_∞)^{−3} profile class** (YSUP §2.5), with geometric ratio
   L^{2−d} = L^{−2} = 1/9, so §2.8 (iii)'s figure and §4.4's last bullet may drop the conditionality **within
   that class**. It is **not** proven outside it, and §35.7's general L^{2k−3} still needs the general
   statement, so the lane-A request 2 of §5 should stay — narrowed.
4. **Proposition TQ-NOGAIN is confirmed where it is stated and sharpened where it is not.** Its hypothesis
   ("Φ_k(v) vanishes at some level-k root of 𝔅") holds for compactly supported v and **fails** for a field
   with the |z|^{−3} tail, where Φ_k is nowhere zero. At p's own cell nothing changes (Φ_k falls by a
   factor ≈ 4 across one coarse step, so osc ≍ max anyway); in the far field osc buys one extra power of the
   coarse distance (R_c^{−3} rather than R_c^{−2}), which is what makes item 1 work. No correction is
   needed; an added clause would be.
5. **§4.5 may be narrowed.** "Both undecided in the block-averaged norm that Φ_k and λ^E actually read" is
   now: Φ_k's block-averaged norm is **decided** (Θ(C_0), no gain — YSUP §2.3); λ^E's is **ARGUED** O(C_0)
   by the dipole convolution (YSUP §2.6), which would deliver (GT-sup) without (Y-sup^loc).

**To BFT_A.md's owner (lane A) — the answer to TENTQ §5's request 1, and one new request.**
1. **The averaged bound the funnel consumes, as asked.** TENTQ's lane-A request 1 asks for a k-, T-,
   p-uniform bound on max_X|(h^{(0→k)}Y^p_{*,0})(c_X)| and on its one-coarse-step difference. For the
   profile class of §38.7 (|g_0| ≤ C_0(1 + |z − p|_∞)^{−3}, co-closed) the answer is
   **|Φ_k(v)(c_X)| ≤ 3.89·C_0 (PROVEN; crude form 15.13·C_0), with the profile
   |Φ_k(v)(c_X)| ≤ C·C_0(1 + |c_X − p|_∞)^{−2}, and a matching exact lower bound 2.4768e−3·C_0 attained at
   u = ⅛d*δ_p for every k ≥ 2.** It is k- and T-uniform and it is **Θ(1)**, not O(1/n²), so it does not
   deliver (TENT-osc). The one-coarse-step difference is Θ(C_0) at p's cell and O(C_0n^{−2}R_c^{−3}) beyond.
2. **A new exact fact about §38.7's own witness, offered as an erratum-free addition.** For u = ⅛d*δ_p at
   offset (1,0,0,0), the funnel series **terminates**: φ_3 = φ_4 = φ_5 = 0 **exactly** (ys1b B4, exact at
   k = 5), so ψ_u = Φ_k(u) = −65/26244 is exact for **every** k ≥ 2, not merely at k = 2. S8-7's "routine
   estimate (ii)" (that the φ_{i+1} for i ≥ 2 do not reverse φ_1 + φ_2) is therefore **not needed for this
   witness**: they are zero. The mechanism is that the two same-direction entries of d*δ_p sit at
   transversely adjacent sites and cancel under the straight average once no block boundary separates them.
3. **Request: is Y^p_{*,0}'s core really the |z|^{−3} profile, or could Z''_0 cancel g_0's funnel?**
   Everything above is CONDITIONAL on the class membership of the **assembled** representative
   Y^p ≡ g^♮ + Z'' + Σ_qG_e(q)Y^q (§38.7). §2.3's lower bound is exact for g_0 = u alone. If Z''_0's funnel
   cancelled g_0's to O(n^{−2}) the verdict would reverse — I do not believe it does (Theorem YH's
   𝒩 ≍ n pins the ℓ¹ mass and §38.7's data split is what **forces** ψ out), but it is not proven here and it
   is the one place the negative verdict could be attacked.
4. **Request, and it is the highest-value item left in this scope: price Proposition TGAUGE's μ exactly.**
   §4.3. Construct one explicit μ ∈ Λ_* with A^{(0→k)}μ = −Φ_k(Y^p_{*,0}) and compute both sides —
   the tent it removes and the Σ_l⟨ĵ_l, d(ev^{(0→l)}μ)⟩ it adds. TENTQ §2.7 argues they are equal from a
   smoothness choice that is "natural but not forced". With §2.3 (iii)'s |·|^{−2} profile for Φ_k the
   natural μ is now explicit, so this is a finite exact computation, and it decides whether face (b) is an
   obstruction at all.

**To BFT_B.md's owner (lane B) — one correction and one proposed replacement.**
1. **Proposition GT-loc's headline survives, but by a route it does not state.** §36.2 reduces (GT-sup) to
   (Y-sup^loc), which is false (own sup Θ(C_0), threshold C/n). **(GT-sup) itself may nevertheless be true**:
   λ^E_X(x)(z) = ⟨A^X_{c_X} − A^X_z, x_0⟩ is a **convolution of two |·|^{−3} kernels in d = 4**, which is
   marginal and gives O(C_0), not O(nC_0) — recovering exactly the factor n that REVIEW_BFT_B_S9_S10 S10-14
   measures GT-loc to lose against lane A's σ ≈ 0.003. **Proposal: replace Proposition GT-loc's ℓ¹ × sup
   Hölder step by the exact dipole pairing**, and state (GT-sup)'s sufficient condition as the
   Green's-function profile |A^X_w(b)| ≲ |b − w|^{−3} on Ñ_X (Neumann), a classical lattice estimate, in
   place of (Y-sup^loc), which is false. *ARGUED here, not claimed: the Green's-function profile is neither
   proven nor checked in this file, and that is the whole of the hole.*
2. **(P0-sup) and the Hölder fallback.** TENTQ §2.10's proposal is sound and should be adopted: the
   difference form of Proposition NCR removes (P0-sup) completely, and by item 1 the object it lands on
   carries one **extra** power of decay from the p-difference, so the Hölder half is not a harder statement
   than (GT-sup). It does **nothing** for (TENT-Q), which carries the explicit n² of 𝒯_p (YSUP §2.7).

**To PROOF.md's owner.** If **(TENT-osc)** is entered in the ledger it should be entered **FALSE at the
core, by L^{2k}, for the |z|^{−3} profile class (CONDITIONAL on that profile input)**, with the surviving
positive statement "(TENT-Q) is k- and T-uniform for sources outside p's coarse cell, with an R_c^{−3}
decay" recorded alongside it. **(Y-sup^loc)** should be marked **FALSE by L^k in both the sup and the
block-averaged currency** — not merely doubtful — while **(GT-sup)** stays OPEN with a *new* sufficient
condition (the box Green's-function profile) replacing the false one. **(Φ-conv)**, if it is carried, is
**PROVEN for the (1 + |z|_∞)^{−3} profile class at d = 4** and OPEN outside it. Net in this scope: one item
refuted, one item narrowed to a single coarse cell, one conditionality discharged within a class, and the
upstream factor k (RS10-1) untouched and still binding on all of it.
