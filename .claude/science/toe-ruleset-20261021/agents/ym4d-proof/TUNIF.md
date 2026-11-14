# TUNIF.md — T-uniformity (target T55-F)

Owner: the T-uniformity worker, session 25. This file is append-only. It may be read by anyone; nobody else
writes it. Requests for other files are collected in the final section "FOR OTHER FILES (not edited)".

---

## §U0 PRE-STATED (first edit of this file, 2026-10-28T21:27:45Z; statements only; cites nothing produced in this session)

This is the first edit of this file. Nothing below §U0 existed when §U0 was written. §U0 fixes the targets, the
admissible outcomes and the failure modes so that the rest of the file can be read against them.

**Disclosure, in the manner of EXISTENCE §21.0.** Exploratory reading preceded this text and was not written
down: HANDOFF.md, NLOC.md (all), NORMS.md §N2-§N8, GREENT.md §G0, SESSION24_RESULTS.md (the NLOC/GREENT/TGAUGE
entries), RTARGET.md §54, LINEAR_PACKAGE.md §3-§4, PROOF.md l.5835-5858 and l.6110-6135, EXISTENCE.md §21.3, and
greps of the lane for "T-uniform". That reading included the observation that the obstruction NLOC §L7 names is a
twisted-complex division problem and the plan to attack it by the two σ-telescoping identities; it produced no
written derivation and no number. Every number quoted in §U0 is read off a file that existed before this edit.

**On the no-constant rule.** No constant in §U0, and none in any `checks/tu1_*_criteria.md`, is derived by me.
Thresholds are either structural 0/1 verdicts or numbers already in NLOC.md / LINEAR_PACKAGE.md / NORMS.md.

### Scope

This file attacks **T-uniformity** and nothing else. T is the **coarse (level-k) torus side**; the level-j side is
T_j = T·L^{k−j} and the fine side is T·L^k (LINEAR_PACKAGE §1.1 convention, as used by NORMS.md and NLOC.md).
I write **no** other lane file. I do not touch the axioms.

### Targets

- **T-U0 (the statement, with its quantifiers).** Write out what "T-uniformity" means in this lane, with every
  quantifier shown: which object, which norm, over which range of T, jointly with k or separately, and for which
  consumer. The lane uses the phrase for at least two different things (NLOC's (N-loc♯)/Theorem N1-15 constant,
  and BFT_B's "k-, T-uniform" labels); say which is open. **A sharp statement is itself a deliverable.** If a
  quantifier in the recorded statement is weaker or stronger than the consumer needs, say so and give the repaired
  statement.
- **T-U1 (the consumer).** Determine, from the consumers themselves (PROOF.md's Lemma BR1, Theorem NAH1 (b)/δ_Sch,
  Proposition NAH-unif / (H-C); EXISTENCE.md §21.3), whether T-uniformity is needed over all T ≥ T_0, over a
  bounded range, or not at all; and at which exponential weight m the consumer's norm is taken. Report what is
  demanded by a named consumer and what is only asserted.
- **T-U2 (the open half).** NLOC.md §L7 names **(N-loc-cell)** as what is left of (N-loc-b), and says the missing
  step is "the twisted analogue of Lemma NL-10 (b) … one lemma, not a programme". **Attempt that lemma.** If it is
  proven, carry it through to (N-loc♯) and to Theorem N1-15 and state exactly which constants are T-free. If it is
  not, say which step fails.
- **T-U3 (the price without it).** State the T-dependence of Theorem N1-15 that is actually proven today, from
  the files as they stand, and re-derive any step of it I lean on. GREENT.md and NLOC.md are UNREVIEWED; nothing
  from them is to be cited as settled.
- **T-U4 (the (GT-sup) reduction).** REVIEW_BFT_B_S9_S10 marks the reduction of (GT-sup) to (Y-sup^loc)
  NOT-VERIFIED; BFT_B's Proposition GT-loc claims it with an absolute constant 20 and Lemma ΓT-op (d) carries an
  absolute constant. **Check the reduction myself** and give a verdict, inheriting neither.
- **T-U5 (uniformity in L, k, j, N).** State for every item proven here whether the constant depends on j, k, T,
  or on the torus at all, and say where it would fail if it did.

### Admissible outcomes, pre-registered

- **(U-O1)** T-uniformity PROVEN for Theorem N1-15 at its scope (d = 4, trivial background, abelian/linearised),
  with every constant exhibited and T-free, and the consumer clause checked.
- **(U-O2)** A weaker statement proven and checked to suffice for the consumer that actually exists; the stronger
  one withdrawn as unnecessary.
- **(U-O3)** CONDITIONAL on one named new input, named explicitly with its own status.
- **(U-O4)** T-uniformity, or one of its recorded statements, **FALSE as stated**, with the obstruction exhibited
  and the repaired statement given. To be reported as a refutation, not dressed as progress. A no-go must be
  tested by reframing it as a positive claim.
- **(U-O5)** No progress. To be reported plainly.

### Pre-registered failure modes for this session's own work

- **(U-F1) The hidden T.** A constant called absolute that contains the torus side through a cell count, a volume,
  a line length, a smallest nonzero momentum 2π/T, or a periodisation count. Every sum over the torus must be
  exhibited and its T-dependence named.
- **(U-F2) The L^k leak.** A construction that gains the required L^k once but pays it twice (e.g. two nested
  within-cell line integrations), giving L^{2k} or L^{3k} where the budget is L^k. The budget is
  |b|_∞ ≲ L^k|d_0B_0|_∞; any assembly must be counted, not asserted.
- **(U-F3) The wrong leg.** Proving the sup (ℓ^∞) half and calling it the ℓ¹ half. NLOC [NL-corr 1] already has
  the sup half T-free; the open half is the column ℓ¹ mass.
- **(U-F4) Two representatives.** Taking the sup bound from one admissible representative and the ℓ¹ bound from
  another. NORMS Theorem N1-15 needs both from the **same** admissible family (NLOC §L2 (A3), Proposition NL-9).
- **(U-F5) Admissibility dropped.** A gauge that is not in Lemma N1-2's admissible class (nested, trivial at the
  level-k roots). Without it Theorem N1-15's identity is not available and the result is void.
- **(U-F6) Analyticity assumed where only a discrete torus exists.** On the coarse torus the momenta are the
  discrete set (2π/T)Z^d; a division by ν_μ = e^{ip_μ} − 1 at the smallest nonzero momentum costs T unless the
  numerator's vanishing at p_μ = 0 is used together with an analyticity (strip) bound. If I divide, I must say
  which strip and which theorem supplies it.
- **(U-F7) The zero mode swept into a seam.** The chain's constant (harmonic) mode cannot be removed by any gauge.
  It must be exhibited and counted, not absorbed.
- **(U-F8) Quoting an unreviewed file as settled.** GREENT.md, NLOC.md, NORMS.md, NQ_CHECK.md, CONST_T.md,
  STAR_CONST.md are all unreviewed. Any load-bearing step taken from them is to be re-derived here.
- **(U-F9) A gate that cannot decide.** Any check must be able to fail, must have a designed-FAIL control, and the
  control's failure must be reported.

### Not success

Numerics in place of a proof. A statement at fixed T called T-uniform. A log called a constant. A bound whose
constant is not exhibited as a function of (N, L, d, κ_±, m). Declaring (H-C)'s C_♭ clause discharged: Theorem
N1-15 bounds D³E_k^br(**1**), and **(N-bg) is untouched and is the larger wall** (NORMS Remark N6-5, NLOC §L8).
Declaring anything about the nontrivial background.

---

## §U1 Scope, inputs, conventions

**Conventions.** NORMS.md's and LINEAR_PACKAGE.md's. Levels j = 0, …, k; n := k − j; **T is the coarse
(level-k) side**, T_j = T·L^{k−j}, fine side TL^k. ℓ := L^k is the side of one level-k **cell** in fine units.
d = 4 is the case of interest (general d displayed where it is free); L ≥ 3 odd. d_j, d_j^*, Q, r_j, ev as in
NORMS §N1. Everything below is **abelian / linearised, trivial background** (Setting SC), as NORMS §N6 and
NLOC §L8 are. **Nothing here bears on (N-bg), and (N-bg) is the larger wall.**

**Imported inputs, with the exact statement used, and their provenance.**

- **(I-A) LINEAR_PACKAGE Theorem 4.2′ (N2-exp′), frozen v1.1, PROVEN, reviewed (REVIEW_S15_CONVERGENCE,
  REVIEW_S16_S17).** *Uniformly in k ≥ 1, T and the fine offset u:* the B_k-symbols of r_{k−1} and of f_0
  extend analytically to the strip S := {|Im p_α| < m_*′} and are bounded there by M = M(L, κ_±); and
  **every entry of the infinite-lattice kernels obeys |K(X)| ≤ Me^{−m′|X|_1} for every m′ < m_*′, X a COARSE
  displacement; torus kernels are the periodisations** (LINEAR_PACKAGE l.211-224). Notation as in Lemma 4.4
  there: f̂_0(n· + u)_{ρσ} = Σ_v 𝔅^v_{ρσ}(p; u)·b̂_v(p), |𝔅| ≤ M on S. Proven value at κ = 1, L = 3:
  **m_*′ = 0.0384**; the located (not proven) rate is ≈ 1.036.
  *This is the one load-bearing import of §U4 and it is the frozen package's, not a session-24 file's.*
- **(I-B) f_0 = L^{2k}d_0B_0** (NORMS (I3) / LINEAR_PACKAGE Thm 3.8), and **sup|f_0| ≤ C_f sup|d_kB_k|**
  uniformly in k, T.
- **(I-C) Theorem NQ-1** (NQ_CHECK.md): ‖Q^j‖_{∞→∞} ≤ 𝔮_0L^j uniformly in j, 𝔮_0 = 1 + d(L+1)/(2L).
  *Status as recorded there: PROVEN; the file is session-24 and carries REVIEW_NQ_S1.* Used only in §U4.6
  (levels j ≥ 1), exactly as NORMS Lemma N1-11 step (4) uses it. **Everything in §U4.1-§U4.5 is free of it.**
- **(I-D) Lemma N1-2** (NORMS): admissible reparametrisations — nested, trivial at the level-k roots — leave
  TOWER-VAR (d)'s identity intact. **Lemma N1-6** (NORMS): a coarse pure gauge of own size 1 is realised at
  level j with own size L^{−(k−j)}.
- **(I-E) Lemma N1-7** (NORMS): ℓ¹ mass from a sup bound plus coarse exponential locality, with
  c_m := coth(m′/2)^d and n_link(j) = dL^{d(k−j)}, n_plaq(0) = (d(d−1)/2)L^{dk}. *Re-derived in §U4.6 (it is
  two lines: group the level-j objects by the level-k cell containing them and sum the geometric series).*

**What is NOT imported.** No statement of NLOC.md or GREENT.md is used as an input. Where §U2-§U3 agree with
NLOC's §L3 or §L7 I say so and give my own derivation; where §U4 supersedes NLOC §L7's open item I say that
too. GREENT.md's constants (C₁ = 54, C₂ = 1703, 𝒮_T = 2.51·10⁸) are quoted **only** in the comparison table of
§U4.7, labelled as that file's unreviewed numbers, and nothing here depends on them.

---

## §U2 T-uniformity restated, with its quantifiers (T-U0)

### U2.1 The phrase names two different things, and only one of them is open

A grep of the lane for "T-uniform" returns two disjoint families.

**(a) The BFT_B family — mostly CLOSED.** BFT_B labels a long list of its own results "k- and T-uniform":
Theorem EP-bd (l.2062), Corollary CL-iv (l.3546), Proposition COF-size (l.4251), Lemma ΓT-op's clauses, the
threshold ε_gi (l.1668), Theorem YH's C_YN (REVIEW_BFT_A_S8 l.174-175). In every one of these the T-uniformity
is **proven and is not the difficulty**: the constants are built from L, d, N, κ_±, m′ and from geometric sums
of e^{−m′d}, with no torus sum anywhere. The open items in that family — (GT-sup), (Y-sup^loc), (TENT-Q),
(NEUT-box) — are open for reasons that have **nothing to do with T**; they are n = L^k counting questions.
(§U6 checks the (GT-sup) reduction, which is the one the brief flags.)

**(b) The NORMS/NLOC family — this is the open one.** Theorem N1-15 (NORMS §N6) bounds N3(D³E_k^br(1))
"for every k ≥ 1 and every torus large enough at level k". Its constant is claimed uniform in k. **Uniformity
in T is not claimed and does not hold on the route as written**, because two of the theorem's four steps bound
a sum over the whole torus by a sup times the number of level-k cells, T^d.

### U2.2 The statement, with every quantifier shown

**Definition (the object).** N3 is NORMS Definition N^F-2's vertex norm 𝔑_{k,m} at **m = 0**, i.e., for the
symmetric trilinear form T := D³E_k^br(1) on level-k data,
  **N3(T) = sup{ |T(δ_x, Y, W)| : x a level-k link, |Y|_∞ ≤ 1, |W|_∞ ≤ 1 }**, symmetrised over which argument
carries the δ (Remark N^F-3 (iii) fixes the normalisation up to 2(d−1)). *This is exactly the N_0 (sup
row/column-sum) object the consumers use: Σ_{b′}|M_{bb′}| = sup over sign patterns Y of |T(δ_b, Y, ·)|, so the
extremal Y is a **global sign pattern** and the m = 0 reading is forced by the consumer, not chosen.*

**(T-UNIF) [the statement].** *There are 𝔚, 𝔖 < ∞ depending only on (N, L, d, κ_±, m′) — in particular
independent of k, of the level index j, of the level-k link x, and of the coarse side T — such that*
  **N3(D³E_k^br(1)) ≤ 𝔚·L^{(d−4)k} + 𝔖·L^{d−1}/(L − 1)  for every k ≥ 1 and every T ≥ T_0.**
*Scope: d = 4, trivial background, abelian / linearised.*

Three quantifier readings have to be fixed, and the lane has not fixed them in one place:
- **(Q1) The range of T.** "For every T ≥ T_0" with T_0 = 1.2932·10⁷ (N5-sf0). T is **not** bounded above by
  anything in layer 1: every layer-1 consumer imposes only a lower bound (§U3). So T-uniformity is a statement
  about T → ∞ at fixed k, and it is **not** needed for the UV limit, which is k → ∞ at fixed T.
- **(Q2) Jointly with k, or separately?** Jointly — but note that **"uniform in k at fixed T" is already
  uniform over an unbounded family of volumes**, since the fine side is TL^k → ∞. The two limits are not
  interchangeable statements about one parameter: k → ∞ at fixed T is the UV limit at fixed physical volume;
  T → ∞ at fixed k is the thermodynamic limit at fixed lattice spacing. **Corollary NL-4 delivers the first.
  (T-UNIF) is the second, and the two are logically independent.** This is the quantifier the lane's "not
  uniform in T, which layer 2 needs" sentence elides.
- **(Q3) Which norm, and at which exponential weight.** 𝔐's exponential weights are m ≥ 0 and NORMS
  Definition N^F-2 puts **e^{−m d_k(z,x)} on the divergence-form (ℓ¹) leg and e^{+m d_k(b,x)} on the two
  configuration (ℓ^∞) legs**, both anchored at the level-k link x. At m > 0 the configuration legs are
  therefore required to **decay** from x. **At any m > 0 the T-dependence of the route disappears for free**
  (§U2.3) — but the m > 0 norm is **weaker** than the m = 0 norm on exactly the leg the consumer uses, and the
  consumer's extremal Y is a global sign pattern, so the m > 0 statement does **not** serve Lemma BR1. The
  open statement is the m = 0 one. *(Recorded because the first thing one wants to try here is "use the
  weights"; it is a real theorem and it is the wrong one. Failure mode U-F3 in its subtlest form.)*
- **(Q4) The weight pair.** NORMS §N7 needs **(θ_w^c, θ_w^r) = (2, d−1)**, not a single θ_w. T-uniformity is
  **orthogonal to that**: the scale weights L^{θ(k−j)} multiply level-j objects and cancel against L^{−θ(k−j)};
  no torus sum passes through them. **T-uniformity does not inherit the weight-pair obstruction**, and
  conversely fixing the pair does nothing for T. Checked by substituting θ_w^c, θ_w^r, θ_A into §N6's four
  exponent counts: T enters only through the cell count in the two ℓ¹-of-the-potential-response steps.

### U2.3 Where the T is, exactly — one line, re-derived

I traced NORMS §N6's proof independently of NLOC §L3 and reach its conclusion, which I therefore confirm:
**(N-loc) is used exactly twice**, in steps (2) and (4), and only to bound **|ζ^c_jδ_x|_{ℓ¹}** through Lemma
N1-7. Steps (1) and (3) use |d_0ζ^c_0δ_x|_{ℓ¹} and |r_j(δ_x)|_{ℓ¹}, which are **gauge-invariant** responses
whose coarse kernels are exponentially local by (I-A); the Y, W legs use only sup bounds. Hence the whole
T-dependence of Theorem N1-15 is the single quantity

  **(N-loc♯)  𝔏_j := sup_x Σ_{b ∈ links(level j)} |(ζ^c_{sm,j}δ_x)(b)| ≤ 𝔠_L·L^{(d−1)(k−j)},  𝔠_L free of j, k, x, T.**

Without any decay the sum runs over the T^d level-k cells and gives 𝔠_L = d𝔠_P·T^d. With decay at rate m′ it
gives 𝔠_L = d𝔠_P·c_{m′}. **The budget L^{(d−1)n} is exactly one level-k cell's worth** (dL^{dn} level-j links
per cell × the sup L^{−n}); (N-loc♯) says the response's ℓ¹ mass behaves as if confined to O(1) cells.

At m > 0 the two configuration legs supply e^{−2m d_k(p,x)} at the vertex location p against the ℓ¹ leg's
permitted e^{+m d_k}, leaving a **spare** e^{−m d_k(p,x)} which sums to c_m over the torus; that is the whole
content of the (Q3) remark, and it needs nothing but the T-free sup bound. At m = 0 there is no spare factor
and (N-loc♯) is the open statement.

---

## §U3 Who actually needs it (T-U1)

**Layer 1: nobody needs T → ∞.** Every consumer of C_♭ in PROOF.md is at a fixed torus with a **lower** bound
only: Lemma BR1 opens "Let T ≥ T_0" (PROOF l.5842); Lemma N5-an♭'s C_♭ := 4S_♭n_1/r_♭ with n_1 = 4(3L)⁴ is a
Cauchy estimate on a polydisc in **finitely many, T-free** variables (l.5835-5840); Theorem NAH1 (b)/δ_Sch use
C_♭α′ at a background, α′ being the AX-gauge field size; Proposition NAH-unif's ε_unif is an infimum over
**levels** at a fixed torus. **So Corollary NL-4's fixed-T statement meets every layer-1 consumer as recorded,
and T-uniformity is not a layer-1 requirement.**

**Layer 2: needed, but not demanded by a named row.** EXISTENCE §21.3's consumer list is the integration
interface, and every row that consumes the (H-C)/BFT family — (BG-unif), (N5-unif) ⇐ (H-K) + (H-C⁺) + (H-ℂ),
(SF^J)_k, (L-loc)_k — asks for **level-uniform** thresholds, not volume-uniform ones. "Volume-uniform" occurs
162 times in EXISTENCE.md but attached to that lane's **own** hypotheses (H-Bal-3G, H-Bal-1's M-uniformity),
to its **conclusions** ("not Haar, uniformly in the volume"), and to ASSEMBLY (III); it is never attached to
C_♭^{(k)} or to Theorem N1-15's constant.
**Verdict (honest, and it is a correction to the lane's record):** the sentence "layer 2 needs T-uniform
constants" (NLOC §L5 Remark NL-5, repeated in HANDOFF item 1) is **not traced to a consumer anywhere in the
repository**. It is nevertheless **very likely right**, for a reason that should be written down rather than
assumed: X-IV takes limit points of finite-volume states, and the cluster/polymer activities that control
them inherit C_♭^{(k)} through (N5-unif); an activity bound that degrades in the volume does not survive that
limit. **Status of the demand: ARGUED, not demanded by a named row.** It is recorded here as item 1 of FOR
OTHER FILES, addressed to the existence lane, because it is their quantifier to fix, not this lane's.

**Consequence for how to read §U4.** A proof of (T-UNIF) is worth having; a proof of it that is *also* the
cheapest route to the fixed-T statement is worth more. §U4 is both: it replaces T^d ≈ 2.8·10²⁸ (and GREENT's
log-growing 𝒮_T) by a T-free constant, and it discharges a named OPEN input rather than pricing it.

---

## §U4 The twisted division theorem: (N-loc-cell) discharged, and (N-loc♯) T-free

NLOC §L7 reduced the open half of (N-loc) to one named lemma: *"what is missing is the **twisted** analogue of
Lemma NL-10 (b): that a transversally closed V with values in V(𝒞) is ν_β times something analytic. That is one
lemma, not a programme."* This section proves that lemma, in the form the application needs, and carries it
through. **I do not use NLOC's §L7 as an input: §U4.1 sets the complex up from scratch.**

### U4.1 The twisted cell complex (set-up; PROVEN-HERE as a definition plus two identities)

The map B_k ↦ B_0 is covariant under **level-k** translations only, so the level-0 fields carry a **coarse**
Fourier transform with a matrix index running over the fine offsets inside one cell. Write a level-0 site as
(X, u) with X ∈ Z^d the cell and u ∈ 𝒞 := (Z/ℓ)^d, ℓ = L^k, the offset, and decompose
ψ(X, u) = ∫ e^{ip·X}ψ̂(u; p) dp. A fine unit shift in direction μ sends u ↦ u + e_μ inside the cell and, at
u_μ = ℓ − 1, sends u ↦ 0 with X ↦ X + e_μ. Hence on the Fourier side it is the **twisted shift**, and the fine
exterior derivative becomes
  **(D_μψ̂)(u) := f_μ(u)ψ̂(u + e_μ mod ℓ) − ψ̂(u),  f_μ(u) := z_μ := e^{ip_μ} if u_μ = ℓ − 1, else 1.**
D_μD_ν = D_νD_μ, and a 1-form b̂ = (b̂_1, …, b̂_d) on 𝒞 has (D ∧ b̂)_{μν} = D_μb̂_ν − D_νb̂_μ. Put
**ν_μ := z_μ − 1**. Two operators on functions on 𝒞, for each direction μ:
  **σ_μ(g)(u) := Σ_{i∈Z/ℓ} g(u with u_μ ↦ i)** (the line sum; independent of u_μ),
  **Θ_μ(g)(u) := Σ_{0≤i<u_μ} g(u with u_μ ↦ i)** (the telescoping partial sum; zero at u_μ = 0).

**Lemma TU-0 (the three identities): PROVEN-HERE.** For every g on 𝒞 and every μ ≠ γ:
 (i) **σ_μ(D_μ g) = ν_μ·g|_{u_μ=0}**; in particular σ_μ(D_μg) = 0 at p_μ = 0.
 (ii) **σ_μ(D_γ g) = D_γ σ_μ(g)** and Θ_μ(D_γg) = D_γΘ_μ(g).
 (iii) The **line solve**: 𝔖_μ(g) := Θ_μ(g) + σ_μ(g)/ν_μ satisfies **D_μ𝔖_μ(g) = g**, and for ν_μ ≠ 0 it is
   the unique solution; ker D_μ = 0 for ν_μ ≠ 0. Moreover **|Θ_μ(g)|_∞ ≤ (ℓ−1)|g|_∞** and
   **|σ_μ(g)|_∞ ≤ ℓ|g|_∞**.
*Proof.* (i) Σ_{u_μ=0}^{ℓ−1}[f_μ g(u+e_μ) − g(u)] = [Σ_{i=1}^{ℓ−1}g(i) + z_μ g(0)] − Σ_{i=0}^{ℓ−1}g(i)
= (z_μ − 1)g(0). (ii) D_γ acts in a different coordinate and the μ-seam factor does not depend on u_γ.
(iii) ψ := 𝔖_μ(g) has ψ|_{u_μ=0} = σ_μ(g)/ν_μ, and for u_μ < ℓ−1, D_μψ = g by telescoping; at u_μ = ℓ−1,
D_μψ = z_μσ_μ(g)/ν_μ − [σ_μ(g)/ν_μ + σ_μ(g) − g(ℓ−1)] = σ_μ(g) − σ_μ(g) + g(ℓ−1) = g(ℓ−1). If D_μψ = 0 then ψ
is constant along μ-lines and the seam gives ν_μψ = 0, so ψ = 0 when ν_μ ≠ 0. The two size bounds are the
number of terms. ∎
**This is the whole source of the L^k gain and the only place it is taken: Θ_μ integrates over ℓ = L^k fine
steps inside ONE cell. Everything else in §U4 is bounded by an absolute constant.** (Failure mode U-F2 is the
risk that this is paid twice; §U4.5 counts it and it is paid once.)

### U4.2 The division bound (rebuilt, not cited): PROVEN-HERE

**Lemma TU-1.** Let 0 < η′ < η ≤ 0.1 and let g be analytic and 2π-periodic in p_μ on S_η := {|Im p_α| < η},
with |g| ≤ G there, and suppose **g|_{p_μ=0} = 0**. Then g/ν_μ is analytic on S_η and
  **sup_{|Im p|≤η′}|g/ν_μ| ≤ κ(η, η′)·G,  κ(η, η′) := max(2, (π/2)e^{η′}/(η − η′)).**
*Proof.* ν_μ(p_μ) = e^{ip_μ} − 1 has simple zeros exactly at p_μ ∈ 2πZ, where g vanishes by hypothesis and
periodicity, so the quotient is analytic and periodic. On |Im p_μ| ≤ η′: if |Re p_μ| ∈ [π/2, π] then
Re e^{ip_μ} ≤ 0, so |ν_μ| ≥ 1 and the quotient is ≤ 2G. If |Re p_μ| ≤ π/2, write w := p_μ; g(w) = w∫_0^1g′(tw)dt
with |g′| ≤ G/(η − η′) by Cauchy on the disc of radius η − η′ about w (which stays in S_η), and
|ν_μ(w)| = |w|·|∫_0^1e^{itw}dt| ≥ (2/π)e^{−η′}|w|. ∎
*(This is LINEAR_PACKAGE Lemma 4.4 step (1) rebuilt, as the standing rule requires; it is also NLOC's
Lemma NL-10 (a). I have written out the proof rather than cite either.)*

### U4.3 The second obstruction vanishes identically: PROVEN-HERE, d ≥ 3

**Lemma TU-2.** Let F̂ be a 2-form on 𝒞, analytic in p on S_η, and **closed**: D_αF̂_{βγ} − D_βF̂_{αγ} +
D_γF̂_{αβ} = 0 for all α, β, γ. Put **Ω_β := σ_1(F̂_{1β})|_{p_1=0}** (β ≥ 2) and **Φ := σ_2(Ω_2)|_{p_2=0}**.
Then, for d ≥ 3:
 (i) **D_βΩ_γ = D_γΩ_β** for all β, γ ≥ 2 (Ω is a closed 1-form of the transverse twisted complex);
 (ii) **Φ ≡ 0.**
*Proof.* (i) Apply σ_1 to the (1, β, γ) closedness relation at p_1 = 0. By Lemma TU-0 (i) the first term
σ_1(D_1F̂_{βγ}) = ν_1·(…) vanishes at p_1 = 0; by TU-0 (ii) the other two are D_βσ_1(F̂_{1γ}) and
D_γσ_1(F̂_{1β}). So −D_βΩ_γ + D_γΩ_β = 0.
(ii) Take β = 2 and any γ ≥ 3 in (i) and apply σ_2 at p_2 = 0: σ_2(D_2Ω_γ) = 0 by TU-0 (i), and
σ_2(D_γΩ_2) = D_γσ_2(Ω_2) = D_γΦ by TU-0 (ii). Hence **D_γΦ = 0 for every γ ≥ 3**, i.e. Φ is constant along
every γ-line of the cell; its seam condition then forces **ν_γΦ = 0**. For d ≥ 3 such a γ exists, and ν_γ is
not a zero divisor in the ring of functions analytic on the connected strip S_η (it vanishes only on
{p_γ ∈ 2πZ}), so Φ ≡ 0. ∎
*Two remarks.* (a) The hypothesis is **closedness only** — no size, no decay, no exactness, nothing about the
chain. (b) d ≥ 3 is load-bearing exactly as in NLOC's Lemma NL-11 step (0); at d = 2 there is no γ and Φ need
not vanish. For the application F̂ is **exact** (F = d_0B_0), and then Φ = 0 also follows directly from TU-0 (i)
twice, in any d — so the application never touches the d ≥ 3 clause. *(This is why check tu1-B, which runs on
exact inputs, tests the σ-identities and not the d ≥ 3 step; disclosed in the criteria.)*

### U4.4 The twisted degree-2 division: PROVEN-HERE, d ≥ 3

**Theorem TU-3 (a closed 2-form of the twisted cell complex is an analytic coboundary, with one factor of ℓ).**
Let d ≥ 3, 0 < η′ < η ≤ 0.1, and let F̂ be closed as in Lemma TU-2, analytic on S_η with
|F̂|_{S_η} := sup_{S_η}max_{u,α<β}|F̂_{αβ}(u; p)| =: G < ∞. Define, with κ := κ(η, η′) from Lemma TU-1,
  **μ := Θ_2(Ω_2) + σ_2(Ω_2)/ν_2**  (on {p_1 = 0}; analytic there by Lemma TU-2 (ii) and Lemma TU-1),
  **b̂_1 := −μ/ℓ**  (independent of u_1 — the **spread** transverse gauge function),
  **G_β := F̂_{1β} + D_βb̂_1,  b̂_β := Θ_1(G_β) + σ_1(G_β)/ν_1  (β ≥ 2).**
Then b̂ is analytic on S_{η′} and
  **(D ∧ b̂)_{αβ} = F̂_{αβ} for all α < β,  and  |b̂|_{S_{η′}} ≤ 2(1 + κ)·ℓ·G.**
*Proof.* **(1) μ is well defined and D_βμ = Ω_β for every β ≥ 2.** |Ω_2| ≤ ℓG by TU-0 (iii), σ_2(Ω_2) vanishes
at p_2 = 0 by Lemma TU-2 (ii), so Lemma TU-1 applies and μ is analytic with
|μ| ≤ (ℓ−1)·ℓG + κ·ℓ·ℓG ≤ (1 + κ)ℓ²G. D_2μ = Ω_2 by TU-0 (iii). For γ ≥ 3,
D_2(D_γμ − Ω_γ) = D_γ(D_2μ) − D_2Ω_γ = D_γΩ_2 − D_2Ω_γ = 0 by Lemma TU-2 (i), and ker D_2 = 0 wherever
ν_2 ≠ 0, so D_γμ = Ω_γ there and hence everywhere by analyticity.
**(2) The pole of b̂_β cancels.** σ_1(b̂_1) = ℓ·(−μ/ℓ) = −μ, so by TU-0 (ii)
σ_1(G_β) = σ_1(F̂_{1β}) + D_βσ_1(b̂_1) = σ_1(F̂_{1β}) − D_βμ = σ_1(F̂_{1β}) − Ω_β, which **vanishes at p_1 = 0 by
the definition of Ω_β**. So σ_1(G_β) = (1 − E_1)σ_1(F̂_{1β}), Lemma TU-1 applies, and b̂_β = 𝔖_1(G_β) is
analytic on S_{η′}.
**(3) The equations.** For β ≥ 2: D_1b̂_β − D_βb̂_1 = G_β − D_βb̂_1 = F̂_{1β} by TU-0 (iii). For 2 ≤ β < γ:
D_1(D_βb̂_γ − D_γb̂_β − F̂_{βγ}) = D_β(D_1b̂_γ) − D_γ(D_1b̂_β) − D_1F̂_{βγ}
= D_β(F̂_{1γ} + D_γb̂_1) − D_γ(F̂_{1β} + D_βb̂_1) − D_1F̂_{βγ} = 0 by closedness, the two b̂_1 terms cancelling;
ker D_1 = 0 for ν_1 ≠ 0 gives the equation there, and analyticity gives it everywhere.
**(4) The sizes.** |b̂_1| = |μ|/ℓ ≤ (1 + κ)ℓG. |D_βb̂_1| = |Ω_β|/ℓ ≤ G, so |G_β| ≤ 2G and
|b̂_β| ≤ (ℓ−1)·2G + κ·ℓ·2G ≤ 2(1 + κ)ℓG. ∎

**Why the spread choice is the whole point (failure mode U-F2).** Any b̂_1 with σ_1(b̂_1) = −μ removes the
pole; the obvious one, b̂_1 := −μ·δ_{u_1,0}, has |b̂_1| = |μ| ≍ ℓ²G and the construction then costs **L^{2k}**,
which is a factor L^k over budget and would be worthless. **Spreading μ uniformly over the ℓ steps of the cell
costs nothing and is exactly Lemma N1-6's mechanism one level down.** The two line integrations are therefore
paid **once** between them: Θ_2 buys ℓ for μ and the spreading gives it straight back.

### U4.5 What Theorem TU-3 is

It is the **multi-scale axial gauge**, in the only form in which it can exist: a telescoping (axial) integration
**inside** one level-k cell, which is where the L^k must come from, combined with an analytic division **in the
coarse momentum**, which is where the exponential coarse locality comes from. NLOC §L7's two objections are met
rather than evaded: a fine-local division is impossible (an O(1) right inverse of d_0 would contradict
|B|_∞ ≳ R|dB|_∞), and the coarse division is twisted — Theorem TU-3 is the twisted division. The obstruction
NLOC names, **(N-loc-cell)**, turns out not to be a condition to verify on the symbol at all: its first
functional Ω is absorbed by the gauge function b̂_1 (this is the Fourier form of NLOC Proposition NL-7's
identity Φ = d_⊥g, "the Dirac string of the axial gauge is a transverse pure gauge"), and its second functional
Φ **vanishes identically for every closed F̂** (Lemma TU-2). **(N-loc-cell) is discharged.**

### U4.6 Carrying it to (N-loc♯) and to Theorem N1-15

**Corollary TU-4 ((N-loc-b′) at level 0): PROVEN-HERE given (I-A).** *Let x be a level-k link and let B_0 be
the level-0 component of Setting SC's chain minimiser for the datum δ_x. There is a level-0 1-form b with
d_0b = d_0B_0 — hence b = B_0 − d_0λ for a fine gauge function λ, modulo the constant mode — whose coarse
kernel obeys*
  **|K(X; u)| ≤ 𝔠_0·L^{−k}·e^{−η′|X|_1},  𝔠_0 := 2(1 + κ(m_*′, η′))·M·2(d−1),**
*for every η′ < m_*′, uniformly in k, T and u.*
*Proof.* By (I-A), F̂ := (d_0B_0)^ = L^{−2k}f̂_0 has entries analytic on S_{m_*′} with |F̂| ≤ 2(d−1)ML^{−2k}
(the 2(d−1) is |d_kδ_x|, supported on the 2(d−1) coarse plaquettes containing x; translate x to the origin so
that the datum's symbol is 1, which is legitimate by coarse translation covariance). F̂ is closed (d_0d_0 = 0).
Apply Theorem TU-3 with η = m_*′, G = 2(d−1)ML^{−2k}, ℓ = L^k: |b̂| ≤ 2(1+κ)·L^k·2(d−1)ML^{−2k} = 𝔠_0L^{−k} on
S_{η′}, and Paley-Wiener (contour shift) gives the kernel bound. **Torus:** by (I-A) the torus kernels are the
periodisations of the infinite-lattice ones, and periodisation commutes with d_0, so the periodised b is a
representative of the torus B_0 and its torus ℓ¹ mass is ≤ the Z^d one. **Zero mode:** at p = 0 the
construction is not used and is not needed — 𝔅^v(0) = 0 (LINEAR_PACKAGE Lemma 4.4 step (2):
𝔅^v = Σ_μν_μh_{μv}), i.e. **the response to a coarse-constant datum is flat**, so F̂(·; 0) = 0. ∎

**Corollary TU-5 ((N-loc♯), T-free): PROVEN-HERE given (I-A), (I-C).**
  **𝔏_j ≤ 𝔠_L·L^{(d−1)(k−j)} for every 0 ≤ j ≤ k, with 𝔠_L := d·c_{η′}·(𝔮_0𝔠_0 + 𝔮_0·8dκ̂C_RL²/(L²−1) + 1 + c_{η′})
  independent of j, k, x and T**, c_{η′} := coth(η′/2)^d.
*Proof.* **Level 0.** Group the level-0 links by the level-k cell containing them: there are dL^{dk} per cell
and T^d cells, and Corollary TU-4 gives Σ_X Σ_{u,μ} |K| ≤ dL^{dk}·𝔠_0L^{−k}·Σ_{X∈Z^d}e^{−η′|X|_1}
= d𝔠_0c_{η′}L^{(d−1)k}. (This is Lemma N1-7's grouping, re-derived: Σ_{X∈Z^d}e^{−η′|X|_1} = coth(η′/2)^d.)
**Levels j ≥ 1.** By the chain relation B_j = Q^jB_0 − Σ_{i<j}Q^{j−1−i}r_i — which is forced, since a
representative is fixed by the level-0 gauge alone (the minimiser set of the chain energy is affine over its
null space, whose elements are δB_0 = d_0λ and δB_j = d_j(ev^jλ) by root covariance Q∘d_j = d_{j+1}∘ev) —
apply (I-C) ‖Q^j‖_{∞→∞} ≤ 𝔮_0L^j and (I-A)'s exponentially local r_i kernels exactly as NORMS Lemma N1-11
step (4) does. Q^j averages over fine paths inside one level-j block, which lies inside one level-k cell, so it
moves no coarse mass and does not degrade the rate η′. **Constant mode.** No gauge changes the torus mean of a
1-form, and the chain's mean is exactly c_j = L^{−(k−j)}c_k with c_k = mean(δ_x), |c_k| = T^{−d} (the constant
and mean-zero sectors are orthogonal for the chain form, and Q(const c) = Lc); its ℓ¹ mass is
dT^dL^{dn}·L^{−n}T^{−d} = dL^{(d−1)n}, **exactly one unit of the budget and free of T**. Likewise the mean of
the constructed b is ≤ 𝔠_0L^{−k}c_{η′}T^{−d}, contributing another dc_{η′}L^{(d−1)n}. ∎

**Theorem TU-6 ((T-UNIF)): PROVEN-HERE given (I-A)-(I-E).** *Theorem N1-15's conclusion holds with 𝔚, 𝔖 as
stated there, with 𝔠_P replaced by 𝔠_0c_{η′}-type constants and **c_m ↦ c_{η′}** in the two potential-slot ℓ¹
masses: for every k ≥ 1 and **every T ≥ T_0**,*
  **N3(D³E_k^br(1)) ≤ 𝔚 + 13.5·𝔖 at d = 4, uniformly in k and in T, with A_soft = 1/L unchanged.**
*Proof.* Steps (1) and (3) of N1-15's proof are untouched (gauge-invariant ℓ¹ masses, (I-A)). Steps (2) and (4)
use |ζ^c_jδ_x|_{ℓ¹}, for which Corollary TU-5 supplies 𝔏_j ≤ 𝔠_LL^{(d−1)n} with 𝔠_L free of T. The sup legs
use the same representative (Corollary TU-4's row ℓ¹ mass, ≤ 𝔠_0c_{η′}L^{−k}: **one representative carries
both legs**, which is what NORMS §N6 and NLOC §L2 (A3) require — failure mode U-F4 does not occur). The
admissibility correction is NORMS Lemma N1-6's nested interpolant applied to d_kμ := δ_x − (level-k component
of the constructed chain), a difference of exponentially localised objects, so it respects (I-D)'s class and
adds a term of the same form (failure mode U-F5 does not occur). The four exponent counts and the summation
are unchanged, so A_soft = 1/L and the series still sums to L^{d−1}/(L−1) = 13.5. ∎

### U4.7 The constant, scored honestly against both comparators

The T-free price is **2(1 + κ(m_*′, η′))·c_{η′}** in place of NLOC's T^d and in place of the ideal c_{m′}.
Optimising η′ at the proven rate m_*′ = 0.0384 (κ = 1, L = 3, d = 4):

| η′ | κ(m_*′, η′) | c_{η′} = coth(η′/2)⁴ | 2(1+κ)c_{η′} |
|---|---|---|---|
| m_*′/2 = 0.01920 | 83.4 | 1.178·10⁸ | 1.99·10¹⁰ |
| 0.75m_*′ = 0.02880 | 168.4 | 2.33·10⁷ | **7.88·10⁹** |
| 0.90m_*′ = 0.03456 | 423.4 | 1.12·10⁷ | 9.53·10⁹ |

| comparator | value | this route |
|---|---|---|
| NLOC Corollary NL-4's cell count T^d at T = T_0 | 2.80·10²⁸ | **7.9·10⁹, and T-free** |
| GREENT's 𝒮_T at T = T_0 (that file is UNREVIEWED; grows like log T) | 2.51·10⁸ | ×31 worse at T_0, but **bounded as T → ∞** |
| the ideal (N-loc) at the same proven rate, c_{m_*′} ≈ 7.36·10⁶ | 7.36·10⁶ | ×1.07·10³ |
| the same at the **located** (not proven) rate 1.036 | — | 2(1+κ)c = **2.96·10³** |

So: **the factor 10³ over the ideal is κ and the half-strip loss, and it is the usual rate-quality gap of this
lane, not a structural one.** Scored against GREENT at a fixed T = T_0 this route is 31× more expensive; scored
at any T above ≈ 10⁹ it is cheaper, and it is the only one of the three that does not grow.

---

## §U5 What is NOT proven, and the three places a hostile reviewer should attack

1. **(N-bg) is untouched.** Theorem TU-6 bounds **D³E_k^br(1)** — one Taylor coefficient at the trivial
   background. (H-C)'s C_♭ clause, as Lemma BR1 and δ_Sch consume it, is the **Lipschitz constant of
   Hess E_k^br on the small-field class**. These are different statements (NORMS Remark N6-5). **Nothing here
   discharges (H-C), and (N-bg) remains the larger wall.** What is discharged is one named input of one
   trivial-background theorem, and the T-quantifier on it.
2. **(N-Q) is still an input.** Theorem N1-15 was CONDITIONAL on **(N-Q) and (N-loc)**. §U4 removes the
   second. It does **not** remove the first: Corollary TU-5's levels j ≥ 1 use ‖Q^j‖ ≤ 𝔮_0L^j. Honest new
   status of Theorem N1-15: **CONDITIONAL on (N-Q) alone, and now uniform in T as well as in k.**
3. **(N-loc-b) as literally stated is not what is proven, and the gap is a mean.** NLOC §L2's (N-loc-b)
   asserts |(ζ^c_{sm,j}δ_x)(b)| ≤ 𝔠_PL^{−(k−j)}e^{−m d_k(b,x)} pointwise. The chain's constant mode is exactly
   c_j = L^{−(k−j)}c_k with |c_k| = T^{−d}, and **no gauge transformation changes the torus mean of a 1-form**,
   so the representative built in §U4 equals (an exponentially decaying field) + (that constant), and at coarse
   distances D ≳ (d log T + log 𝔠_0)/η′ the constant dominates the stated bound. What §U4 proves is
   **(N-loc-b′) = exponential decay + the explicit constant mode**, and that is strictly what (N-loc♯), hence
   Theorem N1-15, consumes (the constant mode's ℓ¹ mass is exactly one unit of the budget, §U4.6). *Whether
   some other representative satisfies the literal (N-loc-b) is left open and is irrelevant: the mean alone
   does not refute it, since an exponentially localised field of height L^{−k} has mean ≍ L^{−k}c_m T^{−d}.*
   **Pre-registered failure mode U-F7 occurred and is reported, not absorbed.**

**The three attack points, named for the reviewer.**
- **(A1) The import.** Everything rests on LINEAR_PACKAGE Theorem 4.2′ (i) in the precise form "analytic on
  {|Im p_α| < m_*′} and bounded by M, **uniformly in k, T and the fine offset u**", plus (ii)'s "torus kernels
  are the periodisations". If the uniformity in u is weaker than stated — e.g. if M degrades with the offset's
  distance from the cell centre — then |F̂|_{S} is not ℓ-free and §U4.4's budget changes. *I did not re-prove
  Theorem 4.2′; it is frozen, PROVEN and twice reviewed, and re-proving it is a paper-scale task. This is the
  one import I take on its ledger status, and I name it as such.*
- **(A2) The periodisation.** Corollary TU-4 builds b on the infinite coarse lattice and periodises. The step
  "the torus chain minimiser's kernel is the periodisation of the Z^d one" is (I-A) (ii)'s, not mine. If the
  torus object differed from the periodisation by a boundary term, the T-free ℓ¹ bound would need redoing (the
  inequality Σ_{torus}|periodisation| ≤ Σ_{Z^d}|·| is the only property I use, and it is one line).
- **(A3) The admissibility correction.** The constructed b fixes the level-0 gauge; Lemma N1-2's class
  requires a nested family trivial at the level-k roots, restored by Lemma N1-6's multilinear interpolant of
  d_kμ := δ_x − (level-k component of the constructed chain). I claim that correction is exponentially
  localised because d_kμ is a difference of exponentially localised objects and multilinear interpolation is
  cell-local (a level-j value depends on the 2^d surrounding level-k values). That is a one-line argument and
  it should be checked; if it failed, the ℓ¹ bound would pick up the interpolant's mass, not a T.

---

## §U6 The (GT-sup) reduction, checked here (T-U4)

The brief records this as a loose end: a review marked the reduction NOT-VERIFIED although Lemma ΓT-op (d)'s
absolute constant appeared to settle it. **I checked it and there is no disagreement to resolve — two
different propositions are being given one name.**

**(i) The implication is correct. Re-derived here.** Proposition GT-loc (BFT_B §36.2, l.4158-4166) says
sup{|λ^{Γ_E}_*(p)(z)| : z ∈ Z} ≤ 2M_n·max{max_{Ñ_X}|Y^p_{*,0}|}, M_n = 2(4n+1). Its two steps are:
Λ(x)(z) = Σ_Xχ^5_X(z)λ^E_X(x)(z) with χ^5 ≥ 0 and Σ_Xχ^5_X = 1, so Λ(x)(z) is a **convex combination** over
the ≤ 2^d boxes with |z − c_X|_∞ < 1; and Lemma ΓT-op (d), a pure duality bound on **any** level-0 1-form,
|λ^E_X(x)(z)| = |⟨(λ^E_X)^Tδ_z, x_0⟩| ≤ ‖(λ^E_X)^T(δ_z − δ_{c_X})‖_1·max_{Ñ_X}|x_0| ≤ 2M_n max_{Ñ_X}|x_0|,
the subtraction of δ_{c_X} being licensed by the pointwise pin λ^E_X(x)(c_X) = 0 (§16.1 (c)) and the
localisation to Ñ_X by ΓT-op (b). Converting to coarse units divides by n: **2M_n/n = 4(4n+1)/n = 16 + 4/n
≤ 20 for every n ≥ 1** (16.44 at n = 9). Y^p_{*,0} is in ΓT-op (d)'s hypothesis class, which is "level-0
1-form" with no co-closedness or decay requirement. **So "(GT-sup) ⟸ (Y-sup^loc), with the absolute constant
20, k- and T-uniformly" is CORRECT.** My verdict agrees with the review's own ("Proposition GT-loc as an
inequality: CONFIRMED; constant 20: verified, and absolute", REVIEW_BFT_B_S9_S10 S10-14 and the CONFIRMED
table at l.996).

**(ii) What the review marked NOT-VERIFIED is a different sentence.** S10-14's NOT-VERIFIED is against the
**headline** "(GT-sup) is not a question about where the spikes of λ^{Γ_E}_* sit" and against [S10-fix 2]'s
"expected TRUE" — i.e. against the *conclusion drawn from* the implication, on the ground that the antecedent
(Y-sup^loc) is probably false at the core. **The reduction and the headline are not the same claim, and the
lane's record ("the (GT-sup) reduction was marked NOT-VERIFIED") conflates them.** Corrected reading: the
reduction is CONFIRMED; the headline is NOT-VERIFIED; (GT-sup) is CONDITIONAL on (Y-sup^loc), which is
unproven and ARGUED-false.

**(iii) One point neither side states, and it is mine.** The remainder ⟨D(S), λ^Γ_*(p)⟩ is
**representative-free** (BFT_B l.3819: changing Y^p_* changes ⟨S, Y^p_*⟩ and ⟨D(S), λ⟩ by opposite amounts),
so (Y-sup^loc) only has to hold for **some** admissible representative. The review's refutation is a count for
the **𝒩-minimising** one: a |z|^{−3} dipole profile has Σ_{r≤n}r³r^{−3} = n ✓ and an O(1) own-unit peak, hence
coarse sup ≍ n, against the ≲ 1 that (Y-sup^loc) demands. But 𝒩 ≍ n is also consistent with a **spread**
field: n of ℓ¹ mass over ≍ n^d links averages n^{1−d} ≪ 1/n. **So the free-field count refutes (Y-sup^loc)
only under the extra premise that no admissible representative is spread near p** — plausible for a
point-source response, not proven, and not stated as a premise in S10-14. Recorded as a narrowing of the
review's finding, not a reversal of it.

**(iv) The loss is the lane's standard defect, one level down.** Both routes to (GT-sup) — GT-loc (ℓ¹ × sup)
and GT-ell (ℓ^∞ × ℓ¹) — are Hölder steps that discard cancellation in the dipole kernel. bb8t T1's
‖(λ^E_X)^Tδ_z‖_1 ≈ 10.6n against lane A's measured λ ≈ 0.003 at the roots next to p is a measured factor ≈ n
of loss. **That is exactly lead decision D3's diagnosis** — an absolute-value row/column sum applied where the
object is in divergence form and the operator is a conjugate of dC⁰d^* — now visible in the slice rather than
in the third derivative. If D3's cure (NORMS Remark N8-2) works, it should be tried on ΓT-op (d) too.

**(v) T plays no role in any of this.** Every constant in (i) is built from M_n = 2(4n+1), χ^5 and 2^d; n is
L^k, not the torus side. **(GT-sup) is a k-counting question, not a T-question**, and it is not part of
target T55-F's open item. Recorded so that the next reader does not look for T-uniformity here.

---

## §U7 Checks tu1 and tu1b — one pre-registered FAIL, reported

**tu1** (criteria `checks/tu1_criteria.md`, written 21:33Z **before** the script; script
`checks/tu1_twisted.py`; output `checks/tu1_out.txt`; stderr `checks/tu1_err.txt`). Exact rational arithmetic
(`fractions` only, no BLAS), 2 s wall, 63 MB peak, nice 10 — **no numeric lock taken or needed** (Rule 6).
Instances: d = 4 at ℓ = 3 and ℓ = 9, d = 3 at ℓ = 5, with generic twists and with z_1, z_2 within 10⁻⁶ and
10⁻⁴ of 1.

- **tu1-A PASS.** D ∧ b = F with **zero** discrepancies in exact arithmetic, every component, every site,
  all eight instances. The diagnostic max|D_βμ − Ω_β| is also exactly 0 everywhere (Theorem TU-3 step (1)).
- **tu1-B PASS.** Φ = 0 exactly in every instance. *Disclosed in the criteria in advance:* on exact inputs
  this also follows by telescoping alone, so tu1-B tests the σ-identities and the indexing, not Lemma TU-2's
  d ≥ 3 clause.
- **tu1-E PASS.** max|b| / (ℓ·max|F|) = 0.271 (ℓ = 3, d = 4), **0.0873 (ℓ = 9, d = 4)**, 0.173 (ℓ = 5, d = 3),
  against the pre-registered bracket 100. The ratio **falls** as ℓ grows, which is the signature of **one**
  factor of ℓ, not two: failure mode **U-F2 does not occur**, and this is the clause that would have caught it.
- **tu1-C: the designed-FAIL control FAILED AS DESIGNED.** A single-entry perturbation breaking closedness
  gives 12 (d = 4) and 10 (d = 3) nonzero discrepancies, worst 4.2 and 3.0, and Φ = 1 ≠ 0. **So tu1-A and
  tu1-B are gates that can fail** (defect 3's requirement).
- **tu1-D FAIL** — and the criterion, not the mathematics, is what failed. With b_1 omitted the uncorrected
  max|b| ran 171.4 → 1633 → 16252 → 162438 over ε = 10⁻¹…10⁻⁴, a growth of **947.6** against the
  pre-registered "≥ 10³". **Four values span three decades, so a true 1/ε pole can give at most ≈ 10³ and the
  first step is below 10 because the pole is not yet dominant at ε = 0.1: the criterion was unsatisfiable by
  the truth** — GREENT's gt1-D defect (a gate that cannot PASS), met a second time. Script, criteria and
  output are kept **unaltered** and the FAIL stands.
- **tu1b-D PASS** (repair run; `checks/tu1b_criteria.md` written after reading tu1_out.txt and **repairing
  only the tu1-D criterion**, `checks/tu1b_pole.py` importing the unaltered `tu1_twisted.py`, output
  `checks/tu1b_out.txt`). Over six decades the uncorrected successive ratios are
  **9.5275, 9.9504, 9.9950, 9.9995, 10.0000** — a clean simple pole in 1/ν_1 — while the corrected max|b| is
  **exactly constant (10.5333) over all six**, variation 1.000. **So the b_1 correction of Theorem TU-3 is
  load-bearing and it removes the pole completely.**

What the checks do and do not establish: they verify the algebra and the indexing of §U4's construction on
instances, and they verify that the spread b_1 is necessary and sufficient to remove the pole. **They are not
the proof**; Theorem TU-3 is written out in §U4.4 and does not depend on them.

---

## §U8 Tally

**PROVEN-HERE (complete proofs written out above, from stated hypotheses; abelian/linearised, trivial
background, d = 4 unless said otherwise)**
1. **Lemma TU-0** — the twisted cell complex's three identities: σ_μ(D_μg) = ν_μ·g|_{u_μ=0}; σ_μ, Θ_μ commute
   with D_γ for γ ≠ μ; the line solve 𝔖_μ with D_μ𝔖_μ = 1, ker D_μ = 0 for ν_μ ≠ 0, and the two size bounds.
   **This is where, and the only place where, the factor L^k is bought.**
2. **Lemma TU-1** — the one-variable division bound with κ(η, η′) = max(2, (π/2)e^{η′}/(η − η′)), rebuilt from
   scratch (not cited from LINEAR_PACKAGE Lemma 4.4 or NLOC Lemma NL-10 (a)).
3. **Lemma TU-2** — for every **closed** 2-form of the twisted cell complex, analytic in p: the transverse
   obstruction Ω is closed, and the second obstruction **Φ ≡ 0** for d ≥ 3, by ν_γ not being a zero divisor.
   *Hypothesis: closedness only.*
4. **Theorem TU-3** — **the twisted degree-2 division**: a closed, analytic 2-form of the twisted cell complex
   is D ∧ b̂ with b̂ analytic on the shrunken strip and **|b̂| ≤ 2(1 + κ)·ℓ·|F̂|**, ℓ = L^k. The transverse
   obstruction is absorbed by the **spread** gauge function b̂_1 = −μ/ℓ; the concentrated choice costs L^{2k}
   and is the trap. **This is the lemma NLOC §L7 named as missing ("one lemma, not a programme").**
   **(N-loc-cell) is discharged** — not by verifying its conditions but by showing closedness implies them.
5. **Corollary TU-4** — **(N-loc-b′)**: an exponentially coarse-local level-0 gauge representative of the
   chain minimiser's response to δ_x, rate any η′ < m_*′, constant 𝔠_0 = 4(d−1)(1 + κ)M, **uniform in j, k, T
   and the fine offset**; plus the explicit constant mode. Given (I-A).
6. **Corollary TU-5** — **(N-loc♯) with 𝔠_L independent of j, k, x and T.** Given (I-A), (I-C).
7. **Theorem TU-6** — **(T-UNIF): Theorem N1-15 holds uniformly in k AND in T**, A_soft = 1/L and every
   exponent count untouched, with c_m ↦ c_{η′} and 𝔠_P ↦ 𝔠_0c_{η′}. Given (I-A)-(I-E); **CONDITIONAL on
   (N-Q) and on nothing else.** T-free price 2(1+κ)c_{η′} = **7.9·10⁹** at the proven rate (2.96·10³ at the
   located rate), against T^d = 2.8·10²⁸ and the ideal c_{m_*′} = 7.4·10⁶.
8. **§U2.2-§U2.3** — the statement of T-uniformity with its four quantifiers (Q1)-(Q4), and the independent
   re-derivation that the T enters Theorem N1-15 in exactly two of its four steps and only through
   |ζ^c_jδ_x|_{ℓ¹}. Confirms NLOC §L3's reading, reached from NORMS §N6's proof.
9. **§U2.2 (Q3)** — at any **m > 0** the T-dependence of the route vanishes for free, from the sup bound
   alone; and this is the **wrong theorem**, because the consumer's extremal configuration leg is a global
   sign pattern, so the consumer's norm is the m = 0 one. Recorded to close the obvious false route.
10. **§U6 (i)** — Proposition GT-loc's implication re-derived: **(GT-sup) ⟸ (Y-sup^loc) with the absolute
    constant 16 + 4/n ≤ 20, k- and T-uniform. CORRECT.**

**ARGUED**
11. **§U3** — that layer 2 does need T-uniformity, through the cluster/polymer activities that inherit
    C_♭^{(k)} via (N5-unif) into X-IV's limit points. **Not demanded by any named row of EXISTENCE §21.3**,
    every one of which asks for level-uniformity instead.
12. **§U6 (iii)** — the review's refutation of (Y-sup^loc) needs the unstated premise that no admissible
    representative is spread near p; the remainder is representative-free, and 𝒩 ≍ n is consistent with a
    spread field. A narrowing, not a reversal.

**CORRECTIONS TO THE LANE'S RECORD**
- **[TU-corr 1]** NLOC §L8's verdict table row *"same, uniform in T | **CONDITIONAL on (N-loc-b)**, reduced to
  (N-loc-cell) | (N-loc-cell) [OPEN]"* and §L9 item 15 are **superseded**: (N-loc-cell) is discharged by
  Theorem TU-3 and the row becomes "unconditional at the stated scope, CONDITIONAL on (N-Q)". NLOC's own
  reduction is what made this possible and the credit is its; what was missing was one lemma and it is §U4.4.
- **[TU-corr 2]** HANDOFF.md's critical-path item 1 ("what is actually open is uniformity in T") and
  SESSION24_RESULTS §5 ("T-uniformity: NO") are superseded for the **(N-loc)** route. GREENT's log T is a
  property of the **Coulomb** representative, which is not the one to use; the exponentially local
  representative exists (Theorem TU-3) and has no log.
- **[TU-corr 3]** "The (GT-sup) reduction was marked NOT-VERIFIED" conflates two propositions: the
  **implication** is CONFIRMED by both the review and me; the **headline** is what is NOT-VERIFIED. §U6.
- **[TU-corr 4]** (N-loc-b) as literally stated in NLOC §L2 is **not** what any route can deliver for the
  representative built here: the chain's constant mode is ineliminable by gauge. **(N-loc-b′)** is the
  statement, and it is what (N-loc♯) needs. §U5 item 3.

**OPEN / untouched**
13. **(N-Q)** — unchanged; Theorem N1-15's remaining input.
14. **(N-bg)** and **(H-C)'s C_♭ clause on the class** — untouched, and the larger wall.
15. **(GT-sup)**, **(Y-sup^loc)**, **(NEUT-box)**, **(TENT-Q)** — untouched; and §U6 (v) records that none of
    them is a T-question.

---

## FOR OTHER FILES (not edited)

1. **To the existence lane (EXISTENCE.md).** §21.3's consumer list demands **level**-uniformity from every row
   that consumes the (H-C)/BFT family and never demands volume-uniformity of C_♭^{(k)}. Layer-1 files
   (NLOC §L5, HANDOFF item 1) nevertheless assert "layer 2 needs T-uniform constants". **One of the two
   records is wrong.** Please state, in §21.3's own form, which layer-1 constants X-IV needs uniform in the
   volume. §U4 now supplies T-uniformity for Theorem N1-15, so the question is no longer blocking — but the
   quantifier should be written down once rather than assumed in two directions.
2. **To NLOC.md's owner.** §L8's verdict table and §L9 item 15 need the [TU-corr 1] row. §L7's framing —
   "(N-loc-cell) is a finite list of cell-flux divisibility conditions on an already-PROVEN symbol" — was the
   right reduction and is what made §U4 a half-page: the conditions turn out to be implied by closedness
   (Lemma TU-2), and the first one is absorbed rather than verified.
3. **To GREENT.md's owner.** Nothing in GREENT is refuted. Its Green's-function bounds stand on their own; but
   its consumer (the ℓ¹ mass of the **Coulomb** representative) is no longer the cheapest route, and
   Proposition NL-8's |x|^{−d} tail is a property of that representative, not of the response. The honest
   comparison is in §U4.7: GREENT is 31× cheaper at T = T_0 and grows like log T; §U4 is T-free.
4. **To PROOF.md's owner.** Theorem N1-15's ledger row should read **CONDITIONAL on (N-Q)** (not on (N-Q) and
   (N-loc)), **uniform in k and T**, at d = 4, trivial background, abelian/linearised; and (N-loc),
   (N-loc-b), (N-loc-cell) should be closed with a pointer to §U4, with [TU-corr 4]'s repair of the statement.
   **(H-C)'s C_♭ clause is NOT discharged** and (N-bg) is unchanged; nothing here may be read as touching them.
5. **To BFT_B.md's owner / the next reviewer.** §36.2's headline sentence should be narrowed to what §U6 (i)
   establishes, and §U6 (iii)'s premise (that no admissible representative is spread near p) should be stated
   explicitly wherever (Y-sup^loc) is called false. §U6 (iv): ΓT-op (d)'s ℓ¹ × sup step is lead decision D3's
   defect one level down and is a candidate for Remark N8-2's cure.
6. **To whoever writes the next criteria file.** tu1-D is the second instance in two sessions of a gate that
   **cannot pass**: a pre-registered total that the true behaviour cannot reach (four sample points span three
   decades). Pre-registration should test satisfiability-by-the-truth as well as falsifiability.

---

## §U9 Two precisions, appended after §U8 (append-only; §U1-§U8 stand as written)

**[TU-prec 1] Corollary TU-5, levels j ≥ 1, one word sharpened.** §U4.6 says Q^j "moves no coarse mass". A
level-j block has side L^j ≤ L^k and may straddle a coarse-cell boundary, so Q^j moves coarse mass by **at
most one cell in each direction**. The correct statement is therefore: Q^j preserves the rate η′ and costs a
factor at most **e^{dη′} ≤ e^{d·m_*′} ≤ e^{0.154} < 1.17** at d = 4. This changes 𝔠_L by less than 17% and
nothing else. The same applies to the Q_str-transports of the r_i.

**[TU-prec 2] The normalisation 2(d−1) in Corollary TU-4 is conservative.** (I-A) bounds the symbol of the map
**B_k ↦ f_0** directly, so for the datum δ_x the symbol is 𝔅^{v_x} itself and |F̂| ≤ ML^{−2k}; the factor
2(d−1), which belongs to Lemma N1-7's |d_kδ_x|, is carried in 𝔠_0 out of caution and may be dropped if the
reviewer confirms the map is read as B_k ↦ f_0 rather than d_kB_k ↦ f_0. It does not affect any exponent.

**Record (process).** PRE-STATED section §U0: **7 254 bytes**, written 2026-10-28T21:27:45Z, before any
derivation in this file. Checks tu1 (21:31:33-21:31:35Z) and tu1b (21:32:18Z), exact rational arithmetic, no
numeric lock taken (Rule 6: plain-python exact arithmetic), nice 10, 63 MB peak. One pre-registered FAIL
(tu1-D), reported in §U7 with its diagnosis and its repair run. *This file cannot write a `*_LOG.md`; the
byte size is logged here instead, and item 7 of FOR OTHER FILES asks the lead to carry it across.*

**FOR OTHER FILES, item 7 (added).** **To the lead.** §U0's byte size (7 254) needs to go into the session
log; this worker's scope is `TUNIF.md` and `checks/tu1_*` only. And the single sentence worth propagating is
**[TU-corr 2]**: the critical-path item "T-UNIFORMITY, not (N-loc)" is closed at its stated scope, and the
remaining input of Theorem N1-15 is **(N-Q)**, which NORMS §N4 itself calls "a question about a DEFINITION,
not a theorem" — if Setting SC's Q is the straight average, 𝔮_0 = 1 and Theorem N1-15 is **unconditional** at
d = 4, trivial background, abelian/linearised, uniformly in k and T.
