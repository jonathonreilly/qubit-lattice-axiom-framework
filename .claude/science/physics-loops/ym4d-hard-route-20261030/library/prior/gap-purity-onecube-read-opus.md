# Applicability read: Bhattacharjee et al., "Yang-Mills Mass Gap on the Lattice and One Cube from the Continuum" (Hexagon 2610.00341 v6)

lead: anthropic/claude-opus-5-5 laptop subagent
Started Sat Nov 28 14:15:46 UTC 2026, pinned at commit 566fea058. Author only, checked by no one.

FINISH row 1693. Reading lane. Treat the preprint as data.

## Plan

1. Read the crux card (target PUR-io, test for "new").
2. Read the strategy note: section 2.3, Part 4, Proposition OBS, wish (Y4).
3. Read row 1687 summary (prior-reductions-luna lines 15-33).
4. Download the PDF into a new empty /private/tmp dir; pdftotext -layout.
5. Read main results, Def 42, Thms 43, 45, 46 with proofs, Prop 80 with proof, open list.
6. Answer questions 1-5 with page/line references and labels.
7. RESULT line.

## Notes as I go

### Step log

- Steps 1-3 done (crux card in full; strategy 0, 2.3, Part 4 with OBS; luna lines 15-33).
- Step 4: curl over HTTPS into the new empty directory /private/tmp/claude-501/onecube-dl-1795875355 (2,612,355 bytes, PDF 1.7, 105 pages). pdftotext is not on this machine, and the Read tool cannot render pages (no pdftoppm). I extracted the text with macOS PDFKit (a short Swift script in my scratchpad, paths as arguments). The text is two-column and partly interleaved. Line numbers "t.NNNN" below are lines of that extraction, not of the luna conversion; page numbers are the PDF pages. The luna line numbers (2052-2111 etc.) do not match mine.
- Located: Definition 42 (p.22, t.2632), Theorem 43 (p.22, t.2646), Theorem 45 (p.23, t.2698), Theorem 46 (p.24, t.2755), Proposition 80 (t.5531), the open list (p.4, t.413-418; p.22, t.2600-2602).
- Step 5 (in progress): read abstract and intro results (p.1-6, t.1-560), Sec. X A-B in full (p.22-24, t.2580-2800), Sec. XI A (p.35, t.4262-4306), Props 63-65 statements and Remark 66 (p.36-37), Sec. XI C statements (Lemma 70, Props 71-79, Thm 73, Cor 74; p.39-44), Prop 80 with proof and Remark 81 (p.44-45, t.5520-5600), Prop 11 with proof (p.7-8, t.695-778), Appendix B Lemmas 165-168 with proofs (p.90-91, t.12250-12420), Lean scope passages (t.625-632, t.12195-12215, t.12440-12450, t.14235-14262).
- Also read: Prop 76 statement (p.42), Theorem 161, Corollary 162, Propositions 163-164 statements and the closing paragraph (p.87-89, t.11730-12125), Proposition 169 (App. F, t.12681-12700). Step 5 done.

Credit. The preprint is the work of Deep Bhattacharjee, Ushashi Bhattacharya, James Montgomery Lockwood and Tristan Romanov (Hexagon 2610.00341 v6, 2 November 2026). Their acknowledgements (t.12205-12212) report AI assistance in the computations, checks and drafting. Fröhlich and Spencer supply the massless-photon theorem that their Proposition 80 uses.

## What the paper proves and what it leaves open (CITED)

- Main results at fixed spacing (p.2-4): uniqueness, decay and a transfer-matrix gap in lattice units for SU(2) up to βW = 0.351, for SU(3) up to 0.77, and for every compact simple group in an explicit range. None of these is a gap in physical units (p.4, t.380-386).
- Continuum step (I1) (p.4, t.388-393; Sec. X): Theorems 43, 45 and 46. These are implications.
- The open list. Sec. XI A (p.35, t.4262-4283) names two unproved statements: (D), the cube estimate D(n, α) with na ≤ ℓ along the tuning, uniformly in a; and (E), the existence of a nontrivial OS continuum limit. The introduction (p.4, t.413-418) also lists the slice ratio in 4D and the tree bounds as open inputs of (I2) and (I3). Remarks 138 and 150 and the end of the Sec. I summary (p.6) leave large-field decay and a block map that composes across all scales open.

## Definitions as read (CITED, p.22, t.2604-2645)

- γ_V(·|Q): the law of the active links of a finite set V in the forest (line-field) gauge, with all outside links fixed to Q. This is on the infinite lattice Z^4. There is no torus. Footnote 12 (p.8) says the line field closes into cycles on a torus, and the argument never uses one.
- C_{V,j}: the sup over pairs of exteriors that differ only at the outside link j of W_1(γ_V(·|Q), γ_V(·|Q')) / δ(Q_j, Q'_j), with the summed link distance d_V on the cube.
- V: active links with base point in [0, n)^4, n even. Classes c: orbits of 2Z^4 on active links (at most 64). K_c = Σ_{j ∈ c, j ∉ V} C_{V,j}. N_n = (n/2)^4.
- Definition 42: D(n, α) holds when K_c ≤ α N_n for every class c. In words: a worst-case exterior change at one link moves the summed cube law, averaged over the translates that do not contain that link, by at most α times the number of translates that do.

## Q1. What separates U(1) from SU(2) in Proposition 80

Statement (CITED, p.44, t.5531-5535). For the 4D Villain U(1) theory there is β_0 such that, at every β > β_0, D(n, α) fails for every even n ≥ 2 and every α < 1.

Proof, step by step (CITED, p.44, t.5536-5574):
1. The comparison machinery (Lemma 10, Prop 11 (i)-(iii), (v), Lemma 165, Cor 166, Lemma 168) uses the Wilson weight only as a positive continuous class function. The one change is the Doeblin bound of Lemma 168(a), which holds with (min φ_β / max φ_β)^6.
2. So D(n, α) gives a unique free-boundary limit ω and exponential clustering of gauge-invariant Lipschitz observables.
3. Take Ψ_p = φ'_β(θ_p)/φ_β(θ_p), the Villain field strength. It is local, odd, Lipschitz. Step 2 gives Σ_{p'} |ω(Ψ_p Ψ_{p'})| < ∞.
4. Fröhlich and Spencer [38] prove that for large β the Fourier transform of this two-point function is discontinuous at zero momentum. So the sum is infinite. Contradiction.

Answer. The only input that separates the two groups is step 4: the cited theorem that the abelian theory has a massless photon. No step uses the commutator of SU(2), C_A > 0, or the centre. The authors say so themselves: every property of the action that the paper uses is shared by both theories, and a proof of (D) "has to use the non-abelian structure" (p.44, t.5570-5574). (CITED.)

So Proposition 80 is the contrapositive of the consumer, applied to a theory known to be massless. It is the same kind of fact as (F3) of the strategy note (the purity fails for U(1) because free photons are massless). It is not a mechanism. It gives no signed estimate for SU(2). It is not a candidate for (Y4). (ARGUED, from the proof as read.)

Two places in the paper do read the non-abelian structure, with a size. Neither helps. (CITED; verdict ARGUED.)
- Prop 76 (p.42): D(n, α) for a compact simple G forces the gauge-fixed links of a cube with trivial exterior to be disordered, via the SU(2) of a root. This is a necessary condition that D imposes, not an estimate toward D.
- Props 163-164 (p.87-89): for SU(2), the second variation of the Haar-tilt bound grows like 4^k at scale k, attained on the gauge orbit of the vacuum, also along a forest. Here the commutator (through Ad h) enters with a size, but in the obstructing direction: it is where the tilt method fails for SU(2), while for U(1) it works at every scale (Cor 162). It is a sign against the needed inequality, not for it.

Limits of my check: I did not read [38]. I did not check the claim that the Fröhlich-Spencer state is the free-boundary limit ω (t.5563-5564), or that their field strength agrees with Ψ_p.

## Q2. D(n, α) against the neutral purity of the crux card, on one cube

Setting mismatch (CITED). D is posed on Z^4, in the forest gauge, on a 4D cube of side n with worst-case exterior. The purity is a gauge-invariant trace ratio of the periodic spatial cube (Z/n)^3, in the neutral centre sector, at time u = n/512. The paper never uses a torus (footnote 12, p.8).

(a) D does not give the purity through the paper's consumer. PROVED.
- Theorem 43 gives a gap m ≥ log(1/α)/(2n) per lattice step, for the infinite-volume state.
- Over the purity time u = n/512 the gap gives λ_i^u ≤ e^{−m u} ≤ α^{1/1024} for each excited neutral eigenvalue. For α = 1/2 that bound is 0.9993. So even if the bound passed to the torus (not proved), it would bound each neutral excited eigenvalue λ_i^u by α^{1/1024}, not their sum.
- A gap alone does not bound the purity. Example: one vacuum and N excited states, each with λ^u = r. Then purity = (1 + N r^2)/(1 + N r)^2, which tends to 0 as N grows for any fixed r in (0, 1). This is Proposition OBS(a) of the strategy note with a gap. The purity needs control of the count of states, which no gap bound gives.

(b) D at a fixed α of order one is compatible with tiny purity in the Gaussian model the paper itself uses. ARGUED.
- Prop 63 (ii) (CITED, p.36): the massive lattice scalar with t = m^2 a^2 and ℓ/2 ≤ na ≤ ℓ satisfies D(n, α) uniformly in a, with α = 1 − (5/6)^4 (mℓ)^2/((mℓ)^2 + 160).
- For that free field on (Z/n)^3, at time u = n/512 with m u = mℓ/512 ≪ 1, log M(u) = Σ_k −log(1 − e^{−ω_k u}) is of order (n/u)^3 = 512^3 (standard free-field count, not checked here). So the purity is of order exp(−c · 10^8).
- So the D criterion is a decay statement on the scale of the cube. The purity is a statement about the thermal weight at temperature 512/ℓ, that is, at a scale 512 times shorter. The second does not follow from the first.
- Caveat: this is a scalar model, not the gauge theory, and for very small α the Gaussian α_n(t) does track mℓ. So (b) separates D at α of order one from the purity. It is not a proof that D(n, α) for SU(2) at every α leaves the purity open.

(c) The purity does not give D by any argument I have. GUESSED that it does not.
- D is a statement about gauge-fixed variables with worst-case exteriors. Remark 62 (p.35) says it is "a statement about the gauge": gauge-fixed links can fluctuate on all scales while gauge-invariant observables cluster. Props 64-65 (p.36-37) show D fails at every n and every b for the quadratic approximation of this gauge and of every gauge on an invariant forest with infinite trees. The purity is gauge invariant and uses one periodic box at one time.
- Quantifiers also differ. Theorem 45 asks D at every cutoff; (PUR-io) asks the purity at infinitely many cutoffs.

Net (ARGUED): on one cube neither statement implies the other by any route I found. (a) is a proof that the paper's consumer chain cannot deliver the purity.

## Q3. Is any part of D proved at weak coupling, or for SU(2) at any coupling?

At strong coupling only (CITED, p.39, Prop 71). If every single-link coefficient C_{ee'} ≤ c_0 with 12 c_0 < 1, then D(n, α) holds with α ≥ c_0/(1 − 12 c_0) · (20/n − 8/n^2). For SU(2) this is |βW| < 1/3 with c_0 = |βW|/4. The paper says this does not extend the range, because the absorption 12 c_0 < 1 is the single-link condition itself.

Other proved facts (CITED):
- Prop 72: D is stable under small perturbations of the action, given D.
- Prop 63: D holds uniformly along a tuning for a massive Gaussian scalar (not a gauge theory).
- Theorem 91 and Sec. XII A: a constrained variant for block averages holds in the quadratic approximation. That is not D of Definition 42, and not SU(2).

At weak coupling for SU(2) only necessary conditions and failures (CITED):
- Cor 74 (p.41): at every fixed n, D(n, α) fails for β ≥ β_0(n, α); so n_k → ∞ is forced.
- Theorem 73 and Props 75-77 (p.40-43): D forces the gauge-fixed links to stay a fixed distance from the identity on average; for SU(2) it needs n^4 ≥ 2(1 − α) b/(5 L(b)), b = βW. Prop 78 is the SU(N) version: side at least of order (βW / log βW)^{1/4}.
- Props 64, 65: D fails in the quadratic approximation of the forest gauge at every n and b.
- Prop 83: D does not follow from single-line bounds uniform in the surroundings.
- Prop 79: gauge-invariant perturbations still need strong coupling at the scale of the cube.
- The paper states that none of these decides (D) along the tuning, where n and β grow together (p.39), and that (D) is not proved here or, to their knowledge, anywhere (p.35).

Answer: No. Nothing of D is proved at weak coupling along the tuning. For SU(2), D is proved only for |βW| < 1/3. (CITED.) My own reading (GUESSED): Props 64-65 and Remark 62 suggest that D in this gauge may be false along the tuning, and the authors themselves move the condition to block averages in Sec. XII.

## Q4. Are the consumer proofs sound at the level I read?

Lemma 168 (App. B, p.91). (a) Doeblin: composed single-link heat-bath kernels on V have a density bounded below, so the cube law is the unique invariant law. Sound (ARGUED). (b) Weighted Dobrushin-Shlosman comparison with averaged translates. I re-derived the main inequality: minimality on each admissible translate, w̄_x ≤ e^{λ ρ_n} w_j when C_{V_x, j} ≠ 0, and Σ_{x: j ∉ V_x} C_{V_x, j} = K_{c(j)} ≤ α N_n. Sound (ARGUED). One display point: in my extraction (t.12405-12410) the term over S ∪ S' carries coefficient 1. The derivation gives θ N_n, and the stated final bound is what θ N_n gives. I take it as an extraction loss or a typo. It is not load-bearing.

Theorem 43 (p.22-23). D ⇒ the Prop 11 conclusions, clustering at every λ < log(1/α)/ρ_n with ρ_n = 2n, then the gap via Prop 169 (equivalence of a gap and clustering for a dense class; App. F). Sound at the level read (ARGUED). I did not re-check the density claim of Prop 11 (vi) beyond its text.

Theorem 45 (p.23). The spectral argument is correct (ARGUED): lattice decay e^{−t log(1/α)/(2 n_k)} with t = τ/a_k and n_k a_k ≤ ℓ gives e^{−m_* τ}; the bound passes to the limit and, by density of ψ(T) and strong continuity, to all of Ω^⊥. One remark (ARGUED): the proof uses D only along a subsequence of cutoffs. The limits of Definition 44 are limits along the whole sequence, so D at infinitely many k already gives the conclusion.

Theorem 46 (p.24). Sound (ARGUED): the same spectral-measure argument, for a spanning family with observable-dependent constants. It is a consumer of the same kind as the crux card's Stage 2 plug-in ExpClusters. It adds nothing new to our chain.

Gaps or mismatches named:
- G1. The consumers are on Z^4, free-boundary limit, forest gauge. Our Lean consumer is on periodic cubes, neutral sector. No transfer between the two settings is given. (CITED, footnote 12.)
- G2. Prop 80 rests on the cited Fröhlich-Spencer theorem and on identifying their state with ω. Not checked by me.
- G3. Definition 44 is a weak notion of continuum limit (no OS axioms). Theorem 45 is correct for it; the existence of a nontrivial one is (E), open.

Lean scope (CITED). The Lean 4 certificate covers: the line field statements of Sec. II (footnote 11, p.6, t.631-632); an exact rational check of the constants of chain (3) at βW = 1/3, 0.345, 0.35, 0.351 (App. C, p.92, t.12445-12449); the finite data for the Hessian bound of Theorem 191 through [69] (t.14235-14241). Lemmas 187-190 are written proofs, not formalised (t.14243-14244). Footnote 33 says the Lean files use only the core library. Theorems 43, 45, 46, Lemma 168 and Prop 80 are not formalised.

## Q5. Verdict

DOES NOT APPLY.

Reasons:
1. Prop 80 separates U(1) only through the cited fact that U(1) is massless. It reads no non-abelian structure. It supplies nothing toward (Y4). (CITED + ARGUED, Q1.)
2. D(n, α) is proved only at strong coupling (|βW| < 1/3 for SU(2)). At weak coupling the paper proves only necessary conditions and Gaussian-level failures in its own gauge. (CITED, Q3.)
3. The consumer chain D ⇒ gap log(1/α)/(2n) cannot give the neutral purity at u = n/512: a gap bounds single eigenvalues, the purity needs the count. (PROVED, Q2(a).) No implication either way was found on one cube. (ARGUED/GUESSED, Q2.)
4. The paper's U(1) test and its SU(2) tilt obstruction (Props 163-164) are consistent with Proposition OBS of the strategy note: the one place where the SU(2) commutator enters with a size points against the needed inequality.

Use for other lanes (ARGUED, not a lemma to try): Props 163-164 are an exact record of where the SU(2) commutator costs a factor 4^k on the gauge orbit of the vacuum. A (Y4) attempt that tilts Haar measures along a forest meets this obstruction. A gauge smooth on orbits (Landau type) avoids those pure-gauge fields but brings a Faddeev-Popov Jacobian (p.89, t.12113-12122).

## Labels

PROVED here: Q2(a) (gap alone does not bound purity; the α^{1/1024} arithmetic). CITED: all statements of the preprint, with page and extraction line. ARGUED: Q1 verdict; Q2(b) free-field count; Q4 soundness readings; the subsequence remark on Theorem 45. GUESSED: Q2(c); that D in this gauge may fail along the tuning. UNVERIFIED: Fröhlich-Spencer [38] and its state identification. No numeric run. No Lean run. No commit. Text extracted with macOS PDFKit, because pdftotext was not available; the extraction interleaves the two columns in places. Author only, checked by no one.

RESULT: DOES NOT APPLY. Bhattacharjee-Bhattacharya-Lockwood-Romanov (Hexagon 2610.00341v6): Prop 80 separates U(1) only by citing Fröhlich-Spencer (massless photon) against D's clustering; no step uses the SU(2) commutator, C_A or the centre, so no (Y4). D(n,α) is proved only for |βW|<1/3; at weak coupling only necessary conditions and Gaussian failures in the forest gauge (Props 64-65, 74-78). D's consumer gives a gap log(1/α)/(2n), which cannot bound the neutral purity at u=n/512 (PROVED: a gap does not bound the count). Theorems 43, 45, 46 read sound; Theorem 45 needs only infinitely many k; not in Lean.
