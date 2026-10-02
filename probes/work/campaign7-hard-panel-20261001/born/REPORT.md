The harness refused to let me write `c7/hard/born/REPORT.md`; it returned "Subagents should return findings as text". The full report is below, so please save it there verbatim. I ran no code. EXACT means a pen-and-paper proof or exact hand arithmetic; ARGUED means reasoning I have not checked.

**Summary (10 lines)**
1. [EXACT] Every antipodal weight law f(t) is the Born-type, affine law of some convex hull of the same pure states. The cubic witness is the Born rule for conv{q⊗q⊗q}. Affinity holds exactly when a site's law-level state space is the Bloch ball of M_2(C).
2. [EXACT] Obstruction: a neighbour ensemble that is antipodal, or centrally symmetric, cannot tell any odd h from Born. Uniform cube-orbit ensembles cannot see the l = 3, 5, 7 sectors. Under the soldered reading, finitely many tests can never force affinity.
3. [EXACT] Criterion: barycenter coherence over a rotation-closed ensemble family forces affinity if and only if it separates every odd l ≥ 3 sector. One trine is enough. A tetrahedron misses l = 5, and the explicit monotone rogue (9/10)t + (1/10)P_5 survives it.
4. [EXACT] Top route: supply a two-site tensor composite and a compression lock. Then no-signalling of record formation, with each site's weights taken from the same law, forces F(s;p) = (1 + s·p)/2 on pure and mixed states, or the constant coin. This holds for every bounded law, with no affinity clause, no repeat certainty, no Born weights, and no regularity assumption.
5. [EXACT] Repeat certainty comes out as a result rather than an input. The cubic witness fails at r = c = 3/5: the two conditions demand 4401/5425 and 7641/15625. The power-law family passes one probe family and fails the other unless γ = 1.
6. [ARGUED] This settles the "nonlinear-law classification" item that the landed recorded-randomizer note and the dynamics-clause synthesis leave deferred, in their own supplied setting.
7. [ARGUED] Sentence audit:
   - Axiom text: the same law at both sites, normalisation, and "varies with".
   - Readings: "a site's law reads its M_2(C) element" and pick coherence.
   - Not in the text: the tensor composite and the compression lock.
8. [ARGUED] Under this route the Born form needs a composition law plus a compression lock, which ties Root A to NEXT item 4. The landed price (affinity plus repeat certainty) is traded for these, not removed.
9. [ARGUED] This is consistent with Galley–Masanes 2018. I could not verify how it relates to Han–Choi.
10. The follow-up is an exact-rational runner (at most 4×4 matrices, under 1 s), specified in §5.

---

# Lane A (born): Root A, readout and the Born form

## 1. Problem in framework terms

Take a site with one recorded neighbour q and a binary menu {p, −p}. Possibility covariance and normalisation give w(p|q) = f(p·q), with h := 2f − 1 odd and |h| ≤ 1 (landed menu block, Theorem 3). Born is h(t) = t. The landed witnesses h = t³ and h = t + t(1 − t²)/4 pass every listed sentence. The question is which sentence forces h(t) = t, and whether that sentence is in the axiom text.

**Reformulation [EXACT].** Write h = Σ_{l odd} h_l P_l. The addition theorem gives h(p·q) = ⟨Φ(p), JΦ(q)⟩, where Φ(q) is the list of Y_lm(q) for odd l with h_l ≠ 0, each scaled by √(4π|h_l|/(2l+1)), and J = diag(sgn h_l). Under any neighbour ensemble μ, the site's law is (1 + ⟨Φ(p), J∫Φ dμ⟩)/2. That is affine in the generalised Bloch vector ∫Φ dμ.

So every antipodal law is a Born-type law for some convex hull of the same pure states. The cubic witness is Born for conv{q⊗q⊗q}, because (p·q)³ = ⟨p^{⊗3}, q^{⊗3}⟩. That hull is 10-dimensional (the l = 1 sector plus the l = 3 sector). Affinity in the M_2(C) Bloch vector holds exactly when h lives in the l = 1 sector alone, which is exactly when the law-level state space is the Bloch ball.

The Born-form question therefore becomes: is a site's law-level state space the state space of M_2(C), or a larger hull of the same pure states?

## 2. Obstructions, with exact scope

- **O1. Antipodal blindness [EXACT].** For μ = aδ_q + (1−a)δ_{−q}, the barycenter is r = (2a−1)q and the averaged law is 1/2 + |r| h(r̂·p)/2 (1/2 when r = 0). That is a function of r for every odd h. Any centrally symmetric ensemble gives 1/2 for every odd h. This is the two-dimensional Gleason gap, transposed to the preparation side.
- **O2. Cube orbits are blind below l = 9 [EXACT].** A uniform ensemble on a proper-cubic orbit (6, 8, 12 or 24 points) has nonzero l-moment only if H_l contains an O-invariant. The count (1/24)[χ_l(0) + 8χ_l(2π/3) + 6χ_l(π/2) + 9χ_l(π)] is 0 for l = 1, 3, 5, 7 and 1 for l = 9. Both witnesses live in l ≤ 3, so uniform soldered cube-orbit ensembles never see them.
- **O3. Criterion [EXACT, by Funk–Hecke].** Suppose a site's averaged law depends on a neighbour ensemble through its barycenter alone, over a rotation-closed family 𝒦 ("barycenter coherence"). Then h is forced affine if and only if, for every odd l ≥ 3, 𝒦 contains two ensembles with equal barycenter and different l-moments. If some l is missed, h = (1−ε)t + εP_l passes; it satisfies |h| ≤ 1 and h(1) = 1, and is monotone for small ε.
- **O4. Records-only conditions cannot carry coherence (landed).** If conditions are formed neighbour records, order-blind positive unsoldered rules are constant (`ORDER_BLIND_NEAREST_NEIGHBOUR_..._2026-09-22`, `HOLES_AS_UNRECORDED_SITES_..._2026-09-22`). Coherence therefore needs a law-level neighbour state, which the axioms do not supply.
- **O5. The lock plus no-signalling passes every law (landed).** This is the replacement-rule countermodel in `DYNAMICS_CLAUSE_A_DISTANT_RECORD_IS_A_RECORDED_RANDOMIZER_..._2026-09-24`.
- **O6. Soldered reading [EXACT count].** Finitely many orientations and probe directions give finitely many linear conditions on infinitely many h_l. Without a finite-degree ansatz they never force affinity.

## 3. Routes, ranked

**R1 (top): pick coherence on a composite.**
- Supplied:
  - C1: an ordinary, ungraded tensor composite C²⊗C² of two neighbours, carrying entangled law-level pure states.
  - C2: the lock acts on the composite by compression. B's record m sends the joint vector to the normalised ⟨m|_Bψ⟩ ⊗ |m⟩.
- Reading-level:
  - C3: a site's law reads the restriction of the law-level state to its own M_2(C). That restriction is the reduced state; it is an algebraic restriction and uses no probabilities.
  - C4: pick coherence. A's law-level odds equal the average of A's post-pick odds over B's pick, with B's odds taken from the same law, for every menu of B.
- What it shows (Theorem 1, §4): Born on pure and mixed states, or the constant coin. This uses no affinity clause, no repeat-certainty clause, no Born ensemble weights, and no regularity assumption.
- It answers the deferred "nonlinear-law classification" item on main (`DYNAMICS_CLAUSE_CAMPAIGN_SYNTHESIS_...`, line 176).
- Cheapest decisive test: §5.

**R2: barycenter coherence at a single site.**
- Supplied:
  - P1: pick coherence for a law-level neighbour.
  - P2: the same as C3, applied at one site.
  - P3: one realised trine-type ensemble.
- What it shows (Theorem 2): affinity. Then f(1) = 1 sets c = 1.
- P3 is a menu-abundance choice made by the law, not axiom content.

**R3: effect-side frame function** (landed F_4/F_A, Born-price note of 2026-09-05).
- Its trine row with homogeneous grading, (2/3)Σ_k f(t_k·q) = 1, is the same identity Σ_k h(t_k·q) = 0 as in R2 [EXACT].
- It adds indexing and homogeneity sentences and gains nothing over R2.

**R4: envariance.**
- The native version is the landed stabiliser fair coin. Inside R1 it supplies the step H(r, 0) = 0.
- Zurek-style fine-graining needs C1, so it reduces to R1.

**Route (c), record additivity.** Additivity within one menu is already reading note 3. Across menus at one condition it is vacuous (menu-independence note, 2026-09-03). Across conditions it is R3's fibred clause.

**Sentence audit.**

| Sentence | In the axiom text? |
|---|---|
| Same law at both sites | Yes (translation covariance) |
| Unsoldered SU(2) covariance | Reading of "No possibility is privileged" (the landed soldering fork) |
| Antipodal normalisation | Yes (reading note 3) |
| Constant law excluded | Yes ("varies with") |
| C3/P2: the law reads the site's M_2(C) element | ARGUED: a defensible reading of "the full one-site possibility domain has algebraic presentation M_2(C)" at law level; reading note 3 ("a probability measure on" the domain) leans against it |
| C4/P1: pick coherence | ARGUED: reading note 1 ("the law supplies the odds; the realized state supplies the pick") plus nearest-neighbour determination, since B's menu is distance-2 data; unsatisfiable with records-only conditions (O4) |
| C1: tensor composite with entangled law-level states | No (the composition law is open; NEXT item 4) |
| C2: compression lock | No (the replacement rule also obeys the lock; O5) |
| P3: a trine ensemble | No (a choice made by the law) |

**Steelman of the witnesses.**
- Each witness is the Born rule for a larger hull of the same pure states (§1).
- Under R2 they survive exactly when 𝒦 misses their sectors. A coin plus a trine, or a coin plus a tetrahedron, catches both because both live in l = 3.
- Under R1 they survive if C2 is dropped. That fits Galley–Masanes (Quantum 2, 104, 2018): modifications of Born can keep no-signalling, but they violate purification and local tomography. [ARGUED; literature is context here, not a premise.]

## 4. Derivation for R1 (Theorem 1)

**Setting** (supplied: C1, C2). |ψ_r⟩ = √a|00⟩ + √(1−a)|11⟩, with a = (1+r)/2 and 0 < r < 1. Both reduced Bloch vectors are r·e_z.

**Step 0** [EXACT; uses C3, covariance, normalisation]. A binary law on {p, −p} at reduced Bloch vector s has the form F(s; p) = (1 + H(|s|, ŝ·p))/2, with H odd in its second argument and H(1, t) = h(t). In particular H(r, 0) = 0.

**Step 1** [EXACT; uses C2]. Let B record m = (θ, φ), with c = cos θ. Then ⟨m|_Bψ⟩ = √a cos(θ/2)|0⟩ + √(1−a) e^{−iφ} sin(θ/2)|1⟩. A's conditional states n_± (for outcomes ±m) are:
- z-components u_+ = (c + r)/(1 + rc) and u_− = (r − c)/(1 − rc);
- transverse lengths s_± = √(1−r²)√(1−c²)/(1 ± rc);
- azimuths −φ and −φ + π.

B's weights, from the same law and C3, are w_± = (1 ± H(r, c))/2.

**Step 2** [uses C4]. For every m and every probe p: Σ_± w_± h(n_±·p) = H(r, p_z).

**Step 3** [EXACT]. Take the probe p = e_x. Then n_±·p = ±s_± y, with y = cos φ free in [−1, 1], and the right-hand side is H(r, 0) = 0. Because h is odd:

  (A)  w_+ h(s_+ y) = w_− h(s_− y) for all y.

Choose r = c = √ρ, with 0 < ρ < 1. Then s_+ = 1/λ and s_− = 1, where λ = (1+ρ)/(1−ρ). So h(λz) = κ h(z) on [0, 1/λ], with κ = w_+/w_−.
- (i) If h ≡ 0 on some interval (0, δ), then (A) over all λ > 1 spreads the zero to (0, 1]: the law is the constant coin. Otherwise κ depends on λ alone, and κ(λμ) = κ(λ)κ(μ).
- (ii) h(1) = κ(λ) h(1/λ), together with |h| ≤ 1, gives h(1) ≠ 0 and κ ≥ |h(1)| > 0. The function x ↦ log κ(e^x) is additive and bounded below, hence linear. So κ(λ) = λ^γ with γ ≥ 0. Boundedness of probabilities is the only regularity used.
- (iii) Hence h(t) = h(1) t^γ on (0, 1]. Applying (A) again at any (r, c) gives (1 + H)/(1 − H) = λ^γ, that is, H(r, c) = tanh(γ artanh(rc)) for |c| < 1.

**Step 4** [EXACT]. Let B measure m = e_x (c = 0). By Step 0, w_± = 1/2. Write r = cos β, so n_± = (±sin β, 0, cos β). For the probe p = (sin α, 0, cos α), n_±·p = cos(β ∓ α). Step 2 gives:

  (B)  H(cos β, cos α) = [h(cos(β − α)) + h(cos(β + α))]/2.

**Step 5** [EXACT]. Set α = π/2 − ε and let ε → 0⁺.
- From (B) with (iii): dH/dε at 0 equals γ h(1) cos β (sin β)^{γ−1}.
- From (iii) directly: dH/dε at 0 equals γ cos β.
- If γ > 0, then h(1)(sin β)^{γ−1} = 1 for every β in (0, π/2). That forces γ = 1 and h(1) = 1.
- If γ = 0 (a step law), (iii) gives H = 0 for |c| < 1, while (B) with α + β < π/2 gives H = h(1). So h(1) = 0, the constant law.

**Conclusion** [EXACT under C1–C4 and the axiom-level sentences].
- h(t) = t and H(r, c) = rc, so F(s; p) = (1 + s·p)/2 on pure and mixed states. The other solution is the constant coin, and "varies with" removes it.
- f(1) = 1 (repeat certainty) is an output, not an input.
- Ordinary quantum mechanics satisfies every instance of Step 2, so the solution set is exactly {Born, coin}.
- [ARGUED] Read together with the landed compression note (Born plus joint effects give compression), compression and Born force each other under marginal no-signalling.

**Witness accounting** [EXACT, hand arithmetic].
- The power-law family h = t^γ with H = tanh(γ artanh(rc)) satisfies all of (A). It fails (B) unless γ = 1.
- Cubic witness (γ = 3) at r = c = 3/5: (A) demands H = (3x + x³)/(1 + 3x²) at x = 9/25, which is 4401/5425. (B) demands [1 + (−7/25)³]/2 = 7641/15625. No mixed-state extension satisfies both. Born gives 9/25 for both.
- Monotone witness: h(λz)/h(z) = λ(5 − λ²z²)/(5 − z²) depends on z, so (A) fails for every extension.
- Anti-Born: h(1) = −1 contradicts Step 5.

**Theorem 2 (R2)** [EXACT]. Let h be odd and bounded, and suppose Σ_{k=1}^{3} h(t_k·p) = 0 for almost every p in S², where {t_k} is a trine.
- By Funk–Hecke, the l-component of p ↦ Σ_k h(t_k·p) is λ_l Σ_m Y_lm(p) Σ_k Y_lm(t_k)*, with λ_l proportional to ∫h P_l.
- Place the trine on the equator at azimuths 0, 2π/3, 4π/3. Then Σ_k Y_lm(t_k) = 3 N_lm P_l^m(0) when m ≡ 0 (mod 3), and 0 otherwise.
- For odd l ≥ 3, take m = 3: l + m is even, so P_l^3(0) ≠ 0, which forces λ_l = 0. Hence h = ct.
- Coin-versus-trine coherence produces exactly this identity: the coin gives 1/2 for any law, and the trine gives 1/2 + (1/6)Σ_k h(t_k·p).

Exact witness values:
- Uniform trine neighbour, probe p = t_1: cubic 5/8, monotone 15/32.
- Uniform tetrahedron neighbour, probe p = v_1: cubic 11/18, monotone 17/36.
- H_5 contains no T-invariant; the character count is (11 − 8 − 3)/12 = 0. So the rogue h = (9/10)t + (1/10)P_5 passes coin-versus-tetrahedron in every orientation (check: 1 + 3P_5(−1/3) = 0). It fails the trine, giving 263/512 at p = t_1.

## 5. Cheapest decisive computation (specification; not run)

An exact-rational runner. Matrices are at most 4×4; it should run in under 1 s.

**Inputs.**
- Pythagorean Schmidt data (r, √(1−r²)) ∈ {(3/5, 4/5), (5/13, 12/13), (7/25, 24/25)}.
- Rational m and p built from Pythagorean triples.
- Laws: Born, coin, anti-Born, cubic, monotone, power laws with γ = 2 and γ = 3, and the l = 5 rogue.

**Checks.**
1. Step 1's steering formulas against an explicit 4×4 compression.
2. Residuals of (A) and (B) are zero for Born and for the coin at every sampled point.
3. γ = 3 with H = T_3: (A) residual zero; (B) residual nonzero, with the values 4401/5425 versus 7641/15625 at r = c = 3/5.
4. Monotone witness and the l = 5 rogue: the (A) ratio depends on z, shown at two rational z.
5. Single site:
   - the values 5/8, 15/32, 11/18, 17/36 and 263/512;
   - the tetrahedral P_5 sum vanishes identically as a polynomial in p;
   - the character counts for O and T.
6. Mutations:
   - flip the signs of u_±;
   - drop the √(1−c²) factor;
   - replace compression with the replacement rule. For this last one, expect every law to pass, reproducing O5.

**What each outcome means.**
- Everything as stated: the program can record "Born follows from C1 + C2 + C3 + C4" as a decision point next to "affinity + repeat certainty".
- Any law that is neither Born nor constant and has zero residual in both (A) and (B) at every sampled point: Step 3 or Step 5 is wrong. Stop and redo the derivation.
- Under the replacement-rule mutation, some law fails: the O5 accounting is wrong.

**Open science items.**
- The soldered (cubic-anisotropic) version of Theorem 1.
- Whether the dynamics-clause Heisenberg bond produces the Schmidt family natively; the landed note uses a supplied partial swap.
- Han–Choi (arXiv:1307.2026). Its abstract describes a causality condition "stronger than no-signaling" for binary devices. I could not read the full text, so how it relates to Theorem 1 is unverified.

Sources:
- [Han & Choi, arXiv:1307.2026](https://arxiv.org/abs/1307.2026)
- [Galley & Masanes, Quantum 1, 15 (2017)](http://quantum-journal.org/papers/q-2017-07-14-15/)
- [Galley & Masanes, Quantum 2, 104 (2018)](https://quantum-journal.org/papers/q-2018-11-06-104/)
- [Masanes, Galley & Müller, Nat. Commun. (2019)](https://www.nature.com/articles/s41467-019-09348-x)