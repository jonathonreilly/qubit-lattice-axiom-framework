lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# CN1RG: exact errors sufficient for convergence of the speed flow, pass 1

Written 2026-11-08 by a Claude Opus 5.5 headless lane on the Mac mini, as pass 1 of leaf RG (wall W3, rank 1) of `CN1_TREE.md`, under the method of open PR #10138: Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen.

**What this file is.** An author-side long draft. It grants no status, adopts no law, adopts no reading and changes no axiom or working-set entry. "Proved here" means: the argument is written out in full below and has not yet been distilled or refereed. "[check]" marks a tiny scratch computation in `/tmp/toe-CN1RG/`. A check guides and never proves. Nothing here is a verdict.

**Source revisions read.**

| Ref | Commit |
|---|---|
| local branch `claude/toe-assembly` (this checkout) | `b5bf445d7` |
| `origin/main` (read with `git show` only, after `git fetch -q origin main`) | `43a1fcc37` |

Files read at those commits, by line. This folder: `prior/CN1RG.md` lines 1-85 (all); `CN1_TREE.md` lines 1-300 (root, R1, RG, LIMIT, OBS), 560-700 (P1-P6, N1), 820-968 (N8, N9, candidates, literature L1-L10, ranking, lane briefs); `CN1.md` lines 1-199 (all); `CN1MOD.md` lines 1-184 (all); `CN1MOD_REFEREE.md` lines 110-125 (G1-G8); `CN1_OUTLINE.md` lines 42-73 (literature) and 289-302 (R1-MOD attacks); `TOE_ASSEMBLY.md` lines 201-270 (sections 3.4-3.11) and 743-775 (section 11); `LZ1.md` lines 1-12; `ZM1INV.md` lines 1-14; `Y2W_DRAFT.md` lines 1-40 (format only). `origin/main`: `docs/WILSON_STAGGERED_RETAINED_GRASSMANN_TWO_LAYER_KP_POLYMER_NORM_BOUNDED_THEOREM_NOTE_2026-07-12.md` lines 1-95 and 368-378; `docs/SPATIAL_LATTICE_GAUGE_FERMION_LOGARITHMS_AND_METRIC_ATTRACTION_LIMITS_BOUNDED_THEOREM_NOTE_2026-09-14.md` lines 1-60; `docs/SUPPLIED_QUARTET_LINEAR_METRIC_FLOW_BOUNDED_THEOREM_NOTE_2026-09-15.md` lines 160-170; `docs/GAUGED_LOG_TRANSFER_QUASILOCALITY_COMBES_THOMAS_NARROW_THEOREM_NOTE_2026-06-13.md` lines 1-45 (last changed `22e798257`).

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". This file works on the supplied model M″ only. No axiom, reading or law text is touched.

**Working set used, by name.** None as a premise. The object is the supplied model M″ of `CN1MOD.md` §1, which that frozen file calls "a proposed supplied model for rung 1, not a realization of a live law" (`CN1MOD.md` line 171). Results used by name: `CN1MOD.md` §1 (the action of M″, its gauge-sign repair, the referee closures G2 and G6); the node RG of `CN1_TREE.md` with its estimate (W) and Lane brief 1, as the target; `CN1.md` (OL) and Theorem 3 with its integrable-forcing closure, only as the reason why (W) is the gate.

**Inputs from outside the working set.** Standard mathematics, rebuilt in the text: finite-dimensional linear algebra (singular values, adjoints, Schur complements, Hadamard's inequality), Fourier analysis on the lattice, a discrete Poincaré inequality, the IMS localization identity, the Combes-Thomas conjugation, lattice Stokes for axial gauges. Literature is in §0.2. No citation is load-bearing.

**Check.** Two scratch computations in `/tmp/toe-CN1RG/scripts/`: `check_gw.py` (2D toy, dense matrices up to 512 x 512, 10 s, 627 MB peak, started at 51 percent free memory) and `check_flux.py` (2D toy, dense matrices up to 2048 x 2048, 25 s, 627 MB peak, started at 52 percent free memory). They are guidance only and are reported where used (§4, §5).

---

## 0. Sources, prior work used, literature

### 0.1 Prior work used

Each item names the prior result and what this file does with it.

| Prior result | Path | Use here |
|---|---|---|
| Model M″: Wilson action with `w_{a0}=1`, `w_{aj}=v_a`, `U_{aμ}=e^{ieq_aA_μ}`, Gaussian photon `δ_{μν}/(\hat k^2+m^2)`, gauge sign `A_μ(x)↦A_μ(x)+χ(x)−χ(x+μ̂)` | `CN1MOD.md` §1 | The model of this file, unchanged. |
| Free zero-mode closure: `D^†D=m(p)^2+Σ_μw_μ^2\sin^2p_μ`, invertible with antiperiodic time | `CN1MOD_REFEREE.md` G2 | Extended: Lemma 3.2 gives the lower bound `D^†D ≥ (w_{min}^2/2)(−Δ)` used in Theorem 1. |
| Hodge decoupling: the exact photon component decouples from invariant fermionic observables; the remaining invariant mass term is "nonlocal in the curvature" | `CN1MOD_REFEREE.md` G6 | Used in Lemma 6.1 (census): the massive photon adds no local coordinate in a covariant scheme. |
| Open items B1 and B2 ("B1 (open)", "B2 (open)") and C1 | `CN1MOD.md` §5 | B1 is proved here for real and complex small-field backgrounds (Theorem 1, Corollary 4.3). The bounded half of B2 is proved for every real background (Theorem 2). The locality half of B2 is the stopping lemma LF (§7). |
| Node RG, estimate (W), "The action norm must control every other marginal coordinate that can feed the velocity equations" | `CN1_TREE.md` lines 190-232 | Target. The census is Lemma 6.1. |
| Lane brief 1 and its three named attacks | `CN1_TREE.md` lines 943-949 | §7 records the three attacks on the stopping lemma. |
| (OL), Theorem 3 and the integrable-forcing closure | `CN1.md` §§4-5 | Context only: they convert (W) into convergence. Not re-proved, not extended. |
| Attacks 1-4 on R1-MOD (all-orders sum, massless kernel, symmetry, large N) | `CN1_OUTLINE.md` §5.6, `CN1.md` §7 | Not repeated. |
| One-step high-mass polymer bound with retained `det D_{II}`; "does not prove an invariant RG neighborhood" | `docs/WILSON_STAGGERED_RETAINED_GRASSMANN_TWO_LAYER_KP_POLYMER_NORM_BOUNDED_THEOREM_NOTE_2026-07-12.md` lines 11-13, 85-88 (main, unaudited) | Not used: it needs `m>4`, and M″ is massless. Recorded because the digest names it. |
| Node contrasts: "Inter-node contrasts decay more slowly than the mean matter/photon mismatch" | `docs/SUPPLIED_QUARTET_LINEAR_METRIC_FLOW_BOUNDED_THEOREM_NOTE_2026-09-15.md` lines 165-167 (main, unaudited) | Lemma 6.1(iv): Wilson species in M″ have one light node each, so M″ has no node contrasts. |
| Fixed-background Combes-Thomas with "a spectral gap that is uniform over all gauge backgrounds" | `docs/GAUGED_LOG_TRANSFER_QUASILOCALITY_COMBES_THOMAS_NARROW_THEOREM_NOTE_2026-06-13.md` lines 30-36 (main, unaudited) | **Missed by the digest.** Same technique, different operator: it has a mass gap; M″ is massless, so here the gap comes from the block term. The argument is rebuilt in Lemma 3.7, not imported. |

### 0.2 Literature (searched and fetched 2026-11-08)

Searches: Balaban–O'Carroll–Schor fermion block RG; Dimock QED d=3 papers (arXiv author query); Brydges–Dimock–Hurd; Bauerschmidt–Brydges–Slade 1211.2477; constructive infrared QED4 (Mastropietro; Falconi–Giuliani–Mastropietro, arXiv author and title queries); Ginsparg–Wilson; Chadha–Nielsen. "Fetched" means the text was read; quotes are exact.

- **[D17]** J. Dimock, "Multiscale block averaging for QED in d=3", arXiv:1712.10029 (v3, 2020-03-03). Full text fetched and read. Eq. (2): "DA = γ · ∇A −1/2 ǫ∆A ... is the Dirac operator on the lattice with Wilson correction." Eq. (20): `S_k(A) = (D_A + m̄_k + b_kP_k(A))^{-1}`, `P_k(A) = Q_k^T(−A)Q_k(A)`. Eq. (22): `D_k(A) = b_k − b_k^2 Q_k(A)S_k(A)Q_k^T(−A)`. Eq. (23): `Γ_k(A) = (D_k(A) + bL^{-1}P(A))^{-1}`. Lemma 5, eqs. (94)-(95), credited there to Balaban–O'Carroll–Schor: "Let M be sufficiently large (depending on L), and ek sufficiently small (depending on L, M), and let A ∈ G̃k,Ω. Then there is a random walk expansion". Lemma 6, eqs. (98)-(99): local inverses on cubes. Proof of Lemma 6, eq. (115): "In [24] it is shown by some Fourier analysis and taking advantage of the Wilson form of the free fermion action that ∥Γk,□(0)f∥2 ≤ C∥f∥2". Part IV: "Lemma 6 for A ∈ G̃k,Ω can be obtained using gauge transformations and expansions around A = 0. See [24] for details." The dimension is three. **Check of the tree's L3 locator:** Lemmas 5-6 and Eqs. (94)-(95) are as the tree says; the paper's Theorem 1 is the gauge-field minimizer regularity theorem, not a fermion bound.
- **[D22]** J. Dimock, "Stability for QED in d=3: an overview", arXiv:2204.07201. Full text fetched. Section 3: "the fermion field is effectively already bounded". Eq. (19) and the sentence after it: "e−1/4 p(e0)2 = O(L−nN/2en) beats |T0N|M = L3NM−3." and "They do not require renormalization and can be bounded without further processing." Section 5: "These operators also embody coupling between large and small field regions, which is abundant and needs to be controlled."
- **[D15]**, **[D20]** J. Dimock, arXiv:1512.04373 ("Ultraviolet regularity for QED in d=3") and arXiv:2009.01156 ("Ultraviolet Stability for QED in d=3"). Abstract pages only.
- **[BOS89]** T. Balaban, M. O'Carroll, R. Schor, "Block renormalization group for Euclidean fermions", Commun. Math. Phys. 122 (1989) 233-247. Title and record only. **NOT VERIFIED.**
- **[BOS91]** T. Balaban, M. O'Carroll, R. Schor, "Properties of block renormalization group operators for Euclidean fermions in an external gauge field", J. Math. Phys. 32 (1991) 3199-3208, DOI 10.1063/1.529479. Search-engine summary of the abstract only (d = 2, 3). **NOT VERIFIED.** Used only through [D17]'s quoted statements.
- **[GW82]** P. H. Ginsparg, K. G. Wilson, "A remnant of chiral symmetry on the lattice", Phys. Rev. D 25 (1982) 2649, DOI 10.1103/PhysRevD.25.2649. INSPIRE abstract fetched: "A new criterion for chiral symmetry in lattice theories of fermions is derived within a block-spin formalism." Credit for the block-spin origin of identities of the type of Theorem 2; the identity of Theorem 2 is proved here and is not claimed to appear in [GW82].
- **[CN83]** S. Chadha, H. B. Nielsen, "Lorentz invariance as a low-energy phenomenon", Nucl. Phys. B 217 (1983) 125-144, DOI 10.1016/0550-3213(83)90081-0. INSPIRE abstract (summary) only. **Text NOT VERIFIED.**
- **[FGM22]** M. Falconi, A. Giuliani, V. Mastropietro, talk "Renormalization at all orders for lattice infrared QED4 with massless electron" (A. Giuliani, AQFP seminar, 2022-03-24). Talk page fetched. Its abstract states, as paraphrased by the fetch tool, a construction at all orders with only the electron-mass counterterm, and non-perturbative well-definedness with an infrared cutoff on the photon propagator for small charge, "a priori non-uniformly in the IR cutoff". No paper found in arXiv author or title queries. **Paper NOT VERIFIED.**
- **[M07]** V. Mastropietro, "Renormalization group and Ward identities for infrared QED4", J. Math. Phys. 48 (2007) 102303, DOI 10.1063/1.2800156. Repository pages returned HTTP 403; search-engine summary only. **NOT VERIFIED.**
- **[BBS15]** R. Bauerschmidt, D. Brydges, G. Slade, "Structural stability of a dynamical system near a non-hyperbolic fixed point", arXiv:1211.2477, Ann. Henri Poincaré (2015). Search result only; the tree's locator "Theorem 1.4 and Corollary 1.8" is **NOT VERIFIED**. Not used.
- **[BDH98]** D. Brydges, J. Dimock, T. R. Hurd, "Estimates on renormalization group transformations", Can. J. Math. 50 (1998) 756. Record only, **NOT VERIFIED**, not used. The searches found no Brydges–Dimock–Hurd paper on random-walk expansions; the gauge-covariant random-walk expansion in the literature read here is Balaban's, as used in [D17] Lemma 5.
- Combes–Thomas (Commun. Math. Phys. 34 (1973) 251) and the IMS localization formula (Ismagilov, Morgan, Simon, Sigal): credit only, **NOT VERIFIED** (the page fetched empty). Both are rebuilt in §3.

**What the literature gives this lane.** In d = 3, Balaban–O'Carroll–Schor and Dimock control the background-field fermion propagators on small fields, by Fourier analysis at zero field plus local gauges and expansions ([D17] Lemmas 5-6). Large-field regions are bounded globally in a unit volume, where "tiny factors ... beat" the number of cubes ([D22] eq. (19)). For lattice QED4 with massless electrons, the talk [FGM22] reports non-perturbative control with a photon infrared cutoff, not uniform in the cutoff. The lane found no construction of the massless or uniformly massive infrared flow of four-dimensional lattice QED with Wilson fermions. That is a search result, not a claim about the whole literature.

## 1. The question, quoted, and the outcome

### 1.1 The question

`CN1_TREE.md` line 945, Lane brief 1: "Take M″ with two unit-charge Wilson species and unequal positive speeds. Keep the photon. Target one exact blocking step and a real invariant domain supporting estimate (W). Begin with a uniform inverse and decay bound for \(D_v(A)+aQ_A^*Q_A\). Include compatible gauge transitions. Track every marginal coordinate that can source speed differences."

`CN1_TREE.md` lines 202-216, the estimate:
\[
x_{k+1}=x_k+hG_k\mathcal F(x_k)+r_{k,N},\qquad b_-\le G_{k+1}^{-1}-G_k^{-1}\le b_+,\qquad
\|r_{k,N}\|_\infty\le C\bigl(G_k^2+G_ke^{-\beta k}+G_ke^{-\beta(N-k)}\bigr), \tag{W}
\]
with \(x_k=(v_{1,k},v_{2,k},c_k)\), \(h=\log L\), "All constants are independent of \(N\) and volume. The action norm must control every other marginal coordinate that can feed the velocity equations." Line 218: "Estimate (W) is a proposed sufficient gate. It does not replace UB″."

`CN1MOD.md` line 163: "**B1 (open):** prove the needed 3+1-dimensional analytic, exponentially decaying background-field block operators uniformly through N scales on the required complex small-field domain. A local axial-gauge Neumann expansion does not by itself control the transition functions between blocks. **B2 (open):** decouple the fermion integral across large-field regions."

### 1.2 The question made exact

The lane has three parts. Each is stated here as a closed mathematical statement about M″ (§2 fixes all symbols).

- **(T1) Block operator.** For the rescaled multiscale operator \(X_k(U)=D_{w,U}+\bar m+a_kP_k(U)\) on the lattice of spacing \(\eta=L^{-k}\), prove \(\|X_k(U)^{-1}\|\le C\) and \(\|1_\Delta X_k(U)^{-1}1_{\Delta'}\|\le Ce^{-\gamma\,d(\Delta,\Delta')}\) for unit cubes \(\Delta,\Delta'\), with \(C,\gamma\) independent of \(k\), the volume, the background in a stated complex small-field domain, and the speeds in a compact positive set. "Compatible gauge transitions" means: the domain is invariant under real gauge transformations, and the proof needs no transition functions between local gauges.
- **(T2) Census.** List every local coordinate of dimension at most four, in the scale-\(k\) effective action of a gauge-covariant block scheme for M″, that can enter the speed equations; identify the exchange-odd ones.
- **(T3) One exact step and a real invariant domain supporting (W).** Define the exact blocking step for M″, a domain \(\mathfrak D_k\) of scale-\(k\) densities, and prove that the step maps \(\mathfrak D_k\) into \(\mathfrak D_{k+1}\) with (W), uniformly in \(N\) and volume.

### 1.3 Outcome in one paragraph

**(T1) is proved (Theorem 1), in four dimensions, for real and complex small-field backgrounds, uniformly in all scales.** The proof is not the local axial-gauge resolvent expansion. It combines three facts: the Wilson term makes the Hermitian part of \(D_U\) nonnegative in every real background (Lemma 3.1); an IMS localization moves the free lower bound \(D^*D\ge\tfrac12w_{\min}^2(-\Delta)\) into any small-field background through local gauges, inside gauge-invariant quadratic forms, so no transition function ever appears (Lemma 3.5); and a two-case estimate splits a unit vector into its block-average part and the rest (Lemma 3.6). Combes-Thomas conjugation gives the decay (Lemma 3.7). **A new exact identity (Theorem 2)** holds for the blocked operator \(D_k=a_k-a_k^2Q_kS_kQ_k^*\) in every real background: \(\operatorname{Re}D_k=a_k^{-1}D_k^*D_k+H_k^*(\operatorname{Re}D_U+\bar m)H_k\). It gives \(\|D_k(U)\|\le a_k\) and a uniform single-step determinant bound for **every** real background, with no small-field condition; this is the bounded half of B2. On small fields it gives a strictly positive Hermitian part on the unit lattice, so every compression is invertible with uniform bounds: these are the local inverses that Balaban's random-walk expansion needs ([D17] eq. (115) in d = 3), now in d = 4 with a background field and without Fourier analysis (Corollary 4.3). **(T2) is proved (Lemma 6.1):** in the covariant scheme the marginal coordinates are \(z_{a,0},z_{a,s}\) (\(a=1,2\)) and the two photon coefficients; the only exchange-odd marginal coordinate, after the field normalization, is \(\Delta=v_1-v_2\); the only exchange-odd relevant one is \(\bar m_1-\bar m_2\). **(T3) is not proved.** The run stops at **Lemma LF** (§7): locality, uniform in the scale, of the change of \(D_k(U)\) and of the single-step fermion determinant when the background is changed on a large-field region. Three named attacks fail on it, each at a stated step: the local axial-gauge resolvent expansion (no small-link gauge on a large-field cube; the finite-volume bound of [D22] eq. (19) cannot beat the infrared volume), the covariant random-walk expansion (uniform local inverses on large-field cubes are equivalent to the absence of coarse near-zero modes with vanishing block averages, which no available estimate excludes), and finite-range polymer localization (the only background-uniform bound on the minimizer is an energy bound that loses \(\eta^{-1/2}\) when turned into an \(L^2\) bound). No counterexample to (W) was found. UB″ stays open as the stronger alternative.

## 2. Setting: M″ in rescaled units and the exact fermion step

### 2.1 Lattices, fields, links

Fix \(d=4\), an integer \(L\ge2\), a scale \(k\ge1\), and \(\eta=L^{-k}\). Lengths are in units of \(L^k\) original lattice spacings ("rescaled units"). The fine lattice is \(\Lambda_\eta=(\eta\mathbb Z/T\mathbb Z)^4\) and the unit lattice is \(\Lambda_1=(\mathbb Z/T\mathbb Z)^4\), with an integer side \(T\) (the original torus has side \(TL^k\)). The unit cube of \(y\in\Lambda_1\) is \(B_y=y+\eta\{0,\dots,L^k-1\}^4\). Fermion fields are \(f:\Lambda_\eta\to\mathbb C^4\) with \(\langle f,g\rangle=\eta^4\sum_xf(x)^*g(x)\); unit-lattice fields \(\phi:\Lambda_1\to\mathbb C^4\) have \(\langle\phi,\chi\rangle=\sum_y\phi(y)^*\chi(y)\). The \(\gamma_\mu\) are Hermitian with \(\{\gamma_\mu,\gamma_\nu\}=2\delta_{\mu\nu}\); so \(\tfrac12(1\pm\gamma_\mu)\) are orthogonal projections.

A **background** is a family of link variables \(U_\mu(x)=e^{i\theta_\mu(x)}\), \(\theta_\mu(x)\in\mathbb C\), on the fine links \((x,x+\eta e_\mu)\). It is **real** when every \(\theta_\mu(x)\) is real. Antiperiodic time is built in: the links \((x,x+\eta e_0)\) with \(x_0=T-\eta\) carry an extra factor \(-1\) inside \(U_0(x)\). In M″, \(U_\mu(x)=e^{ieqA_\mu(x)}\) on the original lattice, so \(\theta=eqA\).

The **rescaled Wilson operator** with weights \(w=(1,v,v,v)\), \(v>0\), is
\[
(D_Uf)(x)=\frac1\eta\sum_\mu w_\mu\Bigl[f(x)-\tfrac12(1-\gamma_\mu)U_\mu(x)f(x+\eta e_\mu)-\tfrac12(1+\gamma_\mu)U_\mu(x-\eta e_\mu)^{-1}f(x-\eta e_\mu)\Bigr].
\]
With \(\psi_\eta(x)=\eta^{-3/2}\psi(x/\eta)\) and \(\bar m=\mu/\eta=L^k\mu\), the M″ action \(\sum_x\bar\psi(\mu+D)\psi\) of `CN1MOD.md` §1 equals \(\langle\bar\psi_\eta,(D_U+\bar m)\psi_\eta\rangle\) (Grassmann pairing with the measure \(\eta^4\)). For real \(U\), \(U^{-1}=\bar U\), and \(D_U\) is the operator of `CN1MOD.md` §1. Write \(w_{\min}=\min(1,v)\), \(w_{\max}=\max(1,v)\). Fix once and for all a compact speed interval \(v\in[v_-,v_+]\subset(0,\infty)\); all constants below depend on \(v_\pm\) only through \(w_{\min}\) and \(w_{\max}\).

### 2.2 Gauge-covariant averaging

A **single averaging step** from a lattice of spacing \(\lambda\) to spacing \(L\lambda\) averages over \(B^\lambda(u)=u+\lambda\{0,\dots,L-1\}^4\). The transport from \(x\in B^\lambda(u)\) to \(u\) runs along the **monotone path** that goes from \(u\) by fine links first in direction 1, then 2, 3, 4, and \(V(u,x)\) is the product of the \(U_\mu(z)\) along it, in path order from \(u\). (Each \(U_\mu(z)\) transports from \(z+\eta e_\mu\) to \(z\).) The **k-step averaging** \(Q_k\) is the composition of the steps from spacing \(\eta\) to spacing 1. Its transport \(V_k(y,x)\), \(x\in B_y\), is the product along the concatenated path, which is monotone in every coordinate, stays in \(B_y\), and has length \(|x-y|_1\le4\). Set
\[
(Q_kf)(y)=\eta^4\!\!\sum_{x\in B_y}\!V_k(y,x)f(x),\qquad (\tilde Q_k\phi)(x)=V_k(y,x)^{-1}\phi(y)\ (x\in B_y),\qquad P_k=\tilde Q_kQ_k .
\]
On the unit lattice, \(Q\) is one averaging step from spacing 1 to spacing \(L\), with its transports also along fine links, and \(P=\tilde QQ\). Then \(Q_{k+1}:=QQ_k\) is the \((k+1)\)-step averaging viewed at scale \(k\).

**Lemma 2.1 (averaging).** (i) \(Q_k\tilde Q_k=1\), \(P_k^2=P_k\), and the same for \(Q,P\). (ii) If \(U\) is real, \(\tilde Q_k=Q_k^*\), \(\tilde Q=Q^*\), and \(P_k,P\) are orthogonal projections. (iii) For \(g:\Lambda_\eta\to U(1)\) put \(U^g_\mu(x)=g(x)U_\mu(x)g(x+\eta e_\mu)^{-1}\), let \(G\) multiply fine fields by \(g\) and \(G_1\) multiply unit-lattice fields by \(g|_{\Lambda_1}\). Then \(D_{U^g}=GD_UG^{-1}\), \(Q_k(U^g)=G_1Q_k(U)G^{-1}\), \(\tilde Q_k(U^g)=G\tilde Q_k(U)G_1^{-1}\), \(P_k(U^g)=GP_k(U)G^{-1}\).

*Proof.* (i) \((Q_k\tilde Q_k\phi)(y)=\eta^4\sum_{x\in B_y}V_kV_k^{-1}\phi(y)=\eta^4L^{4k}\phi(y)=\phi(y)\). Then \(P_k^2=\tilde Q_k(Q_k\tilde Q_k)Q_k=P_k\). (ii) For \(|V_k|=1\), \(\langle\phi,Q_kf\rangle=\eta^4\sum_y\sum_{x\in B_y}\phi(y)^*V_kf(x)=\langle\tilde Q_k\phi,f\rangle\). An idempotent equal to its adjoint is an orthogonal projection. (iii) Each hop picks up \(g(x)\cdot g(x+\eta e_\mu)^{-1}\) and a path product telescopes to \(g(y)V_kg(x)^{-1}\). □

### 2.3 The operators of one exact step

Fix \(a>0\) and \(a_k=a(1-L^{-1})/(1-L^{-k})\in[a(1-L^{-1}),a]\). (This is the parameter that the composition of single Gaussian steps of strength \(a\) produces, as Lemma 2.3 shows; it is Dimock's \(b_k\) of [D17] eq. (18).) Put
\[
X_k=D_U+\bar m+a_kP_k,\qquad S_k=X_k^{-1},\qquad H_k=a_kS_k\tilde Q_k,\qquad D_k=a_k-a_k^2Q_kS_k\tilde Q_k,\qquad \Gamma_k=\Bigl(D_k+\frac aLP\Bigr)^{-1},
\]
whenever the inverses exist. \(D_k\) and \(\Gamma_k\) act on unit-lattice fields; \(H_k\) maps them to fine fields. By Lemma 2.1(iii), \(X_k(U^g)=GX_k(U)G^{-1}\) and \(D_k(U^g)=G_1D_k(U)G_1^{-1}\).

**Lemma 2.2 (exact fermion step at a fixed background).** Let \(X_k\) be invertible. For Grassmann fields \(\psi,\bar\psi\) on \(\Lambda_\eta\) and \(\Psi,\bar\Psi\) on \(\Lambda_1\),
\[
\int\exp\Bigl(-\langle\bar\psi,(D_U+\bar m)\psi\rangle-a_k\bigl\langle\bar\Psi-\bar\psi\tilde Q_k,\ \Psi-Q_k\psi\bigr\rangle\Bigr)D\bar\psi D\psi=\det X_k\cdot\exp\bigl(-\langle\bar\Psi,D_k\Psi\rangle\bigr),
\]
where \(\bar\psi\tilde Q_k\) denotes the unit-lattice row field \(y\mapsto\eta^4\sum_{x\in B_y}\bar\psi(x)V_k(y,x)^{-1}\).

*Proof.* The exponent is \(-\langle\bar\psi,X_k\psi\rangle+a_k\langle\bar\Psi,Q_k\psi\rangle+a_k\langle\bar\psi,\tilde Q_k\Psi\rangle-a_k\langle\bar\Psi,\Psi\rangle\). Translate \(\psi=W+H_k\Psi\), \(\bar\psi=\bar W+a_k\bar\Psi Q_kS_k\); Berezin integration is translation invariant. Since \(X_kH_k=a_k\tilde Q_k\) and \(a_kQ_kS_kX_k=a_kQ_k\), the cross terms cancel and the exponent becomes \(-\langle\bar W,X_kW\rangle-\langle\bar\Psi,(a_k-a_k^2Q_kS_k\tilde Q_k)\Psi\rangle\). Finally \(\int e^{-\langle\bar W,X_kW\rangle}=\det X_k\) in the normalization of the Berezin measure that absorbs \(\eta^4\). □

**Lemma 2.3 (composition).** Let \(R=(a_k+\tfrac aLP)^{-1}=a_k^{-1}(1-P)+(a_k+\tfrac aL)^{-1}P\), \(a'=a_k\frac aL/(a_k+\frac aL)\), and \(X'=D_U+\bar m+a'\tilde Q_kPQ_k\) (the \((k+1)\)-step operator at scale \(k\)). If \(X_k\) and \(X'\) are invertible, then \(D_k+\frac aLP\) is invertible and
\[
\Gamma_k=R+R\,a_kQ_k\,X'^{-1}\tilde Q_k\,a_k R,\tag{2.1}
\]
\[
\det X_k\cdot\det\Bigl(D_k+\frac aLP\Bigr)=\det\Bigl(a_k+\frac aLP\Bigr)\det X',\tag{2.2}
\]
\[
\frac aL-\Bigl(\frac aL\Bigr)^2Q\,\Gamma_k\,\tilde Q=a'-a'^2\,Q_{k+1}X'^{-1}\tilde Q_{k+1},\qquad \tilde Q_{k+1}:=\tilde Q_k\tilde Q.\tag{2.3}
\]
After rescaling by \(L\), \(X'\) is \(L^{-1}\) times the operator \(X_{k+1}\) at spacing \(\eta/L\) with parameter \(La'=a_{k+1}\), and (2.3) is \(D_{k+1}\). So one exact step maps \((\det X_k,D_k)\) to \((\det X_{k+1},D_{k+1})\) up to the explicit constant \(\det(a_k+\frac aLP)\) and the rescaling.

*Proof.* Consider the block operator on (fine field, unit-lattice field)
\[
M=\begin{pmatrix}X_k&-a_k\tilde Q_k\\-a_kQ_k&a_k+\frac aLP\end{pmatrix}.
\]
Its Schur complement with respect to the first block is \(a_k+\frac aLP-a_k^2Q_kS_k\tilde Q_k=D_k+\frac aLP\). With respect to the second block it is \(X_k-a_k^2\tilde Q_kRQ_k=D_U+\bar m+\tilde Q_k(a_k-a_k^2R)Q_k\). Since \(P^2=P\), \(a_k-a_k^2R=a'P\), so this complement is \(X'\). Both complements are invertible, so \(M\) is, and the lower-right block of \(M^{-1}\) equals both \((D_k+\frac aLP)^{-1}\) and the right side of (2.1). The two Schur factorizations of \(\det M\) give (2.2). For (2.3), the Gaussian integral over (fine, unit-lattice) fields with the next step's term \(\frac aL\langle\bar\Psi'-\bar\Psi\tilde Q,\Psi'-Q\Psi\rangle\) gives the kernel \(\frac aL-(\frac aL)^2Q(M^{-1})_{22}\tilde Q\) for \(\Psi'\). Insert (2.1): \(QP=Q\) and \(Q(1-P)=0\) give \(QR=(a_k+\frac aL)^{-1}Q\), and the scalars combine to \(a'\) and \(a'^2\). The rescaling statement is the substitution \(x\mapsto x/L\), under which \(D_U\) gains a factor \(L\) and \(1/a_{k+1}=1/(La_k)+1/a\) holds for \(a_{k+1}=La'\). □

Lemmas 2.2 and 2.3 are the fermionic half of one exact blocking step: at every fixed background, the step is a Gaussian Grassmann integral with explicit kernel and determinant. They hold for any background for which the inverses exist. The bounds are §§3-5.

## 3. Theorem 1: uniform inverse and decay on small fields

### 3.1 Domain and statement

For a background \(U=e^{i\theta}\) write \(\theta=\theta_R+i\theta_I\) and \(U_R=e^{i\theta_R}\). For a plaquette \(p\), \(\varphi_p\in(-\pi,\pi]\) is the oriented sum of \(\theta_R\) around \(p\), reduced mod \(2\pi\). (The antiperiodic signs enter a plaquette twice with opposite orientation, so they cancel.) The **small-field domain** is
\[
\mathcal U_k(\varepsilon,\delta)=\bigl\{U:\ |\varphi_p|\le\varepsilon\eta^2\ \text{for every plaquette},\ \ |\theta_I|\le\delta\eta\ \text{on every link}\bigr\}.
\]
In M″ terms (\(\theta=eqA\), rescaled field strength \(F=dA/\eta^2\), rescaled \(A/\eta\)): \(|eqF|\le\varepsilon\) and \(|eq\operatorname{Im}A|\le\delta\) in rescaled units. **The domain is invariant under real gauge transformations** \(\theta_\mu(x)\mapsto\theta_\mu(x)+\chi(x)-\chi(x+\eta e_\mu)\): plaquette sums and \(\theta_I\) do not change. This is the form of "compatible gauge transitions" used here: the domain is defined gauge-invariantly, and the proof below only evaluates gauge-invariant quadratic forms in local gauges. No transition function between local gauges ever enters.

**Theorem 1 (uniform inverse and decay).** Fix \(a>0\), \([v_-,v_+]\subset(0,\infty)\), and set \(\kappa=w_{\min}/4\), \(a_-=a/2\), \(a_+=a\), \(s_1=\min(a_-/4,\ \kappa^2/(16a_+),\ 0.3\kappa)\), \(s_0=s_1/2\). There are an explicit integer \(M\ge2\) and explicit \(\varepsilon_0,\delta_0,\mu_0,\alpha_0>0\), depending only on \(a,w_{\min},w_{\max}\), such that for every \(L\ge2\), every \(k\ge1\), every torus side \(T\ge6M\) that is a multiple of \(M\), every \(U\in\mathcal U_k(\varepsilon_0,\delta_0)\) and every \(\bar m\ge-\mu_0\):

1. \(X_k(U)\) is invertible and \(\|X_k(U)f\|\ge\tfrac{s_0}2\|f\|\), \(\|X_k(U)^*f\|\ge\tfrac{s_0}2\|f\|\); for real \(U\) the constant is \(s_0\).
2. For all sets \(\Delta,\Delta'\subset\Lambda_\eta\), \(\|1_\Delta X_k(U)^{-1}1_{\Delta'}\|\le\frac4{s_0}e^{-\alpha_0\operatorname{dist}_\infty(\Delta,\Delta')}\).
3. \(\theta\mapsto X_k(e^{i\theta})^{-1}\) is holomorphic on the interior of the domain, and \(X_k(U^g)^{-1}=GX_k(U)^{-1}G^{-1}\) for real gauge transformations.

All constants are independent of \(k\), \(L\), \(T\), \(v\in[v_-,v_+]\) and \(U\). The proof is Lemmas 3.1-3.8.

### 3.2 The lemmas

**Lemma 3.1 (the Wilson term).** For real \(U\), with \((\delta^U_\mu f)(x)=\eta^{-1}(f(x)-U_\mu(x)f(x+\eta e_\mu))\) and \(\|\nabla_Uf\|^2=\sum_\mu\|\delta^U_\mu f\|^2\),
\[
\operatorname{Re}D_U:=\tfrac12(D_U+D_U^*)=\tfrac\eta2\sum_\mu w_\mu(\delta^U_\mu)^*\delta^U_\mu\ \ge0 .
\]
*Proof.* Let \((T_\mu f)(x)=U_\mu(x)f(x+\eta e_\mu)\); it is unitary and \(T_\mu^*f(x)=U_\mu(x-\eta e_\mu)^{-1}f(x-\eta e_\mu)\). So \(D_U=\eta^{-1}\sum_\mu w_\mu[1-\tfrac12(T_\mu+T_\mu^*)+\tfrac12\gamma_\mu(T_\mu-T_\mu^*)]\). \(\gamma_\mu\) commutes with \(T_\mu\), so the last term is anti-Hermitian. Finally \(\eta^2(\delta^U_\mu)^*\delta^U_\mu=(1-T_\mu)^*(1-T_\mu)=2-T_\mu-T_\mu^*\). □

**Lemma 3.2 (free lower bound).** On \(\ell^2(\eta\mathbb Z^4;\mathbb C^4)\) with \(U\equiv1\), \(\|D_1h\|^2\ge\frac{w_{\min}^2}2\|\nabla_1h\|^2\).

*Proof.* The symbol of \(D_1\) is \(\eta^{-1}(m(p)+i\sum_\mu w_\mu\gamma_\mu\sin\eta p_\mu)\) with \(m(p)=\sum_\mu w_\mu s_\mu\), \(s_\mu=1-\cos\eta p_\mu\in[0,2]\). By the anticommutation relations its modulus squared is \(\eta^{-2}(m^2+\sum_\mu w_\mu^2\sin^2\eta p_\mu)\). The symbol of \((\delta_\mu)^*\delta_\mu\) is \(2\eta^{-2}s_\mu\). If every \(s_\mu\le1\), \(\sum w_\mu^2s_\mu(2-s_\mu)\ge w_{\min}^2\sum s_\mu\). If some \(s_\nu>1\), then \(\sum s_\mu>1\) and \(m^2\ge w_{\min}^2(\sum s_\mu)^2\ge w_{\min}^2\sum s_\mu\). In both cases the symbol of \(D_1^*D_1\) is at least \(\frac{w_{\min}^2}2\cdot2\eta^{-2}\sum s_\mu\). Plancherel. □

**Lemma 3.3 (Poincaré on a unit cube).** For \(g:B_y\to\mathbb C^4\) with mean \(\bar g=\eta^4\sum_{B_y}g\), \(\ \eta^4\sum_{B_y}|g-\bar g|^2\le4\,\eta^4\sum_{\ell\subset B_y}\eta^{-2}|g(x_\ell)-g(x_\ell+\eta e_{\mu_\ell})|^2\).

*Proof.* Let \(n=L^k=1/\eta\). By Jensen, \(|g(x)-\bar g|^2\le n^{-4}\sum_{x'}|g(x)-g(x')|^2\). Join \(x\) to \(x'\) by the rectilinear path that changes coordinate 1 first, then 2, 3, 4; it has at most \(4n\) links, so Cauchy-Schwarz gives \(|g(x)-g(x')|^2\le4n\sum_{\ell\in\text{path}}|\delta_\ell g|^2\). A link in direction \(\mu\) lies on the paths of at most \(n^{\mu-1}\cdot n^{4-\mu}\cdot n^2=n^5\) ordered pairs (free: \(x_1..x_{\mu-1}\), \(x'_{\mu+1}..x'_4\), and the pair \(x_\mu,x'_\mu\)). So \(\sum_x|g-\bar g|^2\le4n^2\sum_\ell|\delta_\ell g|^2\). Multiply by \(\eta^4=n^{-4}\). □

**Lemma 3.4 (axial gauge on a cube).** Let \(C\) be a lattice cube of side \(s\le T/2\) and \(U\) real with \(|\varphi_p|\le\varepsilon\eta^2\) on the plaquettes of \(C\), and \(3s\varepsilon\eta<\pi\). There is \(g:C\to U(1)\) with \(U^g_\mu(x)=e^{i\theta'_\mu(x)}\), \(|\theta'_\mu(x)|\le3s\varepsilon\eta\), on every link of \(C\). So the transport of \(U^g\) along any path of \(n\) links in \(C\) has angle at most \(3s\varepsilon\eta\,n\).

*Proof.* Root \(c\) at a corner. The axial tree is the set of \(\mu\)-links \((x,x+\eta e_\mu)\) with \(x_\nu=c_\nu\) for all \(\nu>\mu\); its path from \(c\) to \(x\) moves in direction 1, then 2, 3, 4. Choose \(g\) so that \(U^g=1\) on tree links. For a non-tree \(\mu\)-link at \(x\), \(U^g\) equals the holonomy of the loop: tree path to \(x\), the link, tree path back from \(x+\eta e_\mu\). The two tree paths share their legs in directions below \(\mu\), and their legs in directions above \(\mu\) are translates by \(\eta e_\mu\). So the loop bounds a ribbon of at most \(3s/\eta\) plaquettes. Lattice Stokes for an abelian field: the holonomy is the product of the plaquette variables of the ribbon. Take \(\theta'\) to be the sum of the \(\varphi_p\). □

**Lemma 3.5 (IMS localization with local gauges).** Let \(U\) be real with \(|\varphi_p|\le\varepsilon\eta^2\) everywhere, \(M\ge2\) dividing \(T\), \(T\ge6M\), and \(9M\varepsilon\le1\). Then for every \(f\)
\[
\|D_Uf\|^2\ge\frac{w_{\min}^2}4\|\nabla_Uf\|^2-E\|f\|^2,\qquad E=\frac{K_{I}}{M^2}+7225\,w_{\max}^2M^2\varepsilon^2,\quad K_I=3301\pi^2w_{\max}^2 .
\]
*Proof.* *Partition.* In one dimension let \(\phi_j(t)=\sin(\pi(t-(j-1)M)/2M)\) on \([(j-1)M,jM]\), \(\cos(\pi(t-jM)/2M)\) on \([jM,(j+1)M]\), zero elsewhere; then \(\sum_j\phi_j^2=1\) and \(|\phi_j(t)-\phi_j(t')|\le\frac\pi{2M}|t-t'|\). Put \(\chi_J(x)=\prod_\mu\phi_{J_\mu}(x_\mu)\). So \(\sum_J\chi_J^2=1\), \(\operatorname{supp}\chi_J\subset C_J\) (a cube of side \(2M\)), \(|\chi_J(x)-\chi_J(x')|\le\frac\pi{2M}|x-x'|_1\), and every point lies in at most \(3^4=81\) of the cubes enlarged by \(3\eta\).

*IMS identity.* For any operator \(Z\), \(\sum_J[\chi_J,[\chi_J,Z^*Z]]=2Z^*Z-2\sum_J\chi_JZ^*Z\chi_J\), so \(\sum_J\|Z\chi_Jf\|^2=\langle f,Z^*Zf\rangle-\frac12\sum_J\langle f,[\chi_J,[\chi_J,Z^*Z]]f\rangle\). Also \([\chi,Z^*]=-[\chi,Z]^*\) gives \(\langle f,[\chi,[\chi,Z^*Z]]f\rangle=2\operatorname{Re}\langle[\chi,[\chi,Z]]f,Zf\rangle-2\|[\chi,Z]f\|^2\).

*Commutator sizes.* \(\|D_U\|\le12w_{\max}/\eta\). A hop \(T\) has \(\|[\chi_J,T]\|\le\frac{\pi\eta}{2M}\) and \(\|[\chi_J,[\chi_J,T]]\|\le(\frac{\pi\eta}{2M})^2\). Hence \(\|[\chi_J,D_U]\|\le\frac{4\pi w_{\max}}M\) and \(\|[\chi_J,[\chi_J,D_U]]\|\le\frac{2\pi^2w_{\max}\eta}{M^2}\). These commutators act only within the \(\eta\)-neighbourhood of \(C_J\). With the overlap count 81,
\(\frac12\sum_J|\langle f,[\chi_J,[\chi_J,D_U^*D_U]]f\rangle|\le81(24\pi^2+16\pi^2)\frac{w_{\max}^2}{M^2}\|f\|^2\). The same computation for \(\delta^U_\mu\) (\(\|\delta_\mu\|\le2/\eta\)) gives \(\frac12\sum_J|\langle f,[\chi_J,[\chi_J,\nabla_U^*\nabla_U]]f\rangle|\le\frac{243\pi^2}{M^2}\|f\|^2\).

*Local step.* Let \(g_J\) be the axial gauge of Lemma 3.4 on the cube \(C_J^+\) (the \(\eta\)-neighbourhood of \(C_J\), side \(s\le3M\)), extended by 1. Put \(h=g_J\chi_Jf\), supported in \(C_J\). \(D_U\chi_Jf\) uses only links of \(C_J^+\), on which \(|U^{g_J}-1|\le9M\varepsilon\eta\). So, with Lemma 2.1(iii), \(\|D_U\chi_Jf\|=\|D_{U^{g_J}}h\|\ge\|D_1h\|-72w_{\max}M\varepsilon\|h\|\), and \(\|\nabla_1h\|\ge\|\nabla_{U^{g_J}}h\|-18M\varepsilon\|h\|=\|\nabla_U\chi_Jf\|-18M\varepsilon\|h\|\). Lemma 3.2 (with \(h\) extended by zero to \(\eta\mathbb Z^4\)) then gives \(\|D_U\chi_Jf\|\ge\frac{w_{\min}}{\sqrt2}\|\nabla_U\chi_Jf\|-85w_{\max}M\varepsilon\|\chi_Jf\|\). Use \((\alpha-\beta)_+^2\ge\alpha^2/2-\beta^2\): \(\|D_U\chi_Jf\|^2\ge\frac{w_{\min}^2}4\|\nabla_U\chi_Jf\|^2-7225w_{\max}^2M^2\varepsilon^2\|\chi_Jf\|^2\).

*Sum.* Sum over \(J\), use \(\sum_J\|\chi_Jf\|^2=\|f\|^2\), and the IMS identity for \(Z=D_U\) and for \(Z=\delta^U_\mu\). The two error terms give \(K_I\le(3240+61)\pi^2w_{\max}^2\). □

The local gauges \(g_J\) of different cubes are never compared. Each enters one gauge-invariant number, \(\|D_U\chi_Jf\|\) or \(\|\nabla_U\chi_Jf\|\).

**Lemma 3.6 (two-case coercivity, real backgrounds).** Under the hypotheses of Lemma 3.5 and \(144\varepsilon\le1\), for real \(U\), \(\bar m\ge-\mu_0\), and \(\|f\|=1\),
\[
\|X_kf\|\ge s_1-\mu_0-E_0,\qquad E_0=37\kappa\varepsilon+\sqrt E .
\]
*Proof.* Let \(p=\|P_kf\|\), \(q=\|(1-P_k)f\|\), \(p^2+q^2=1\) (Lemma 2.1(ii)).

*Step 1 (Hermitian part).* By Lemma 3.1, \(\|X_kf\|\ge\operatorname{Re}\langle f,X_kf\rangle\ge\bar m+a_kp^2\).

*Step 2 (Poincaré through the averaging).* On each unit cube \(B_y\) take the axial gauge of Lemma 3.4 rooted at \(y\) (side 1): links have \(|\theta'|\le3\varepsilon\eta\), and the averaging transports (monotone paths, at most \(4/\eta\) links) have \(|V_k'-1|\le12\varepsilon\). With \(f'=g_yf\) on \(B_y\) and \(\bar f'\) its mean: \(\|g_yP_kf-\bar f'\|_{B_y}\le12\varepsilon(2+12\varepsilon)\|f\|_{B_y}\le25\varepsilon\|f\|_{B_y}\) (pointwise bound, using \(|V_k'|=1\) and Cauchy-Schwarz); and by Lemma 3.3 and Lemma 3.4, \(\|f'-\bar f'\|_{B_y}\le2\|\nabla_Uf\|_{B_y}+12\varepsilon\|f\|_{B_y}\), where \(\|\nabla_Uf\|_{B_y}\) keeps the links inside \(B_y\). Minkowski in \(\ell^2\) over the cubes: \(q\le2\|\nabla_Uf\|+37\varepsilon\).

*Step 3.* Lemma 3.5 and Step 2: \(\|D_Uf\|\ge\frac{w_{\min}}2\|\nabla_Uf\|-\sqrt E\ge\kappa q-37\kappa\varepsilon-\sqrt E\). So \(\|X_kf\|\ge\kappa q-a_kp-|\bar m|-E_0\).

*Cases.* Let \(p_0=\min(\frac12,\frac\kappa{4a_k})\). If \(p\ge p_0\), Step 1 gives \(\|X_kf\|\ge a_kp_0^2-\mu_0\). If \(p<p_0\) and \(\bar m\ge0.3\kappa\), Step 1 gives \(\|X_kf\|\ge0.3\kappa\). If \(p<p_0\) and \(\bar m<0.3\kappa\), then \(q\ge\sqrt3/2\), \(a_kp\le\kappa/4\), \(|\bar m|\le\max(0.3\kappa,\mu_0)\), and Step 3 gives \(\|X_kf\|\ge(0.866-0.25-0.3)\kappa-\mu_0-E_0\). Finally \(a_kp_0^2=\min(a_k/4,\kappa^2/(16a_k))\ge s_1\) because \(a_k\in[a/2,a]\). □

**Lemma 3.7 (complex backgrounds).** If \(U\in\mathcal U_k(\varepsilon,\delta)\) and \(\delta\le1/8\), then \(\|X_k(U)-X_k(U_R)\|\le K_5\delta\) with \(K_5=16w_{\max}+24a_+\).

*Proof.* \(|e^{i\theta}-e^{i\theta_R}|=|e^{-\theta_I}-1|\le2\delta\eta\), and the same for the inverses; the hopping coefficients are at most \(w_\mu/\eta\) in norm, four directions, two hops: \(\|D_U-D_{U_R}\|\le16w_{\max}\delta\). A transport is a product over at most \(4/\eta\) links, so \(|V_k(U)/V_k(U_R)-1|\le e^{4\delta}-1\le8\delta\) and \(|V_k(U)^{\pm1}|\le2\). Cauchy-Schwarz on each cube (\(\eta^4|B_y|=1\)) gives \(\|Q_k(U)-Q_k(U_R)\|,\|\tilde Q_k(U)-\tilde Q_k(U_R)\|\le8\delta\) and \(\|Q_k(U)\|\le2\). So \(\|P_k(U)-P_k(U_R)\|\le24\delta\). □

**Lemma 3.8 (Combes-Thomas conjugation).** Let \(\rho:\Lambda_\eta\to\mathbb R\) satisfy \(|\rho(x)-\rho(x')|\le|x-x'|_\infty\) (torus distance), \(0\le\alpha\le1\), and \(X_\alpha=e^{\alpha\rho}X_ke^{-\alpha\rho}\). For \(U\in\mathcal U_k(\varepsilon,\delta)\) with \(\delta\le1/8\): \(\|X_\alpha-X_k\|\le K_6\alpha\), \(K_6=32w_{\max}+8a_+\).

*Proof.* \((X_\alpha-X_k)(x,x')=X_k(x,x')(e^{\alpha(\rho(x)-\rho(x'))}-1)\). Hops join points at distance \(\eta\), so the hopping part changes by at most \(\eta^{-1}\cdot4w_{\max}\cdot2\cdot2\cdot2\alpha\eta\). \(P_k(x,x')=\eta^4V_k(y,x)^{-1}V_k(y,x')\) joins points of one unit cube (\(\ell^\infty\)-diameter below 1); the Schur test bounds its change by \(4(e^\alpha-1)\le8\alpha\). □

### 3.3 Proof of Theorem 1

Choose an integer \(M\ge2\) with \(M^2\ge128K_I/s_1^2\) (the torus side is then required to be a multiple of \(M\); for the tower of scales take the original side \(ML^{N'}\)); then \(\varepsilon_0\le\min\bigl(s_1/(85\sqrt{128}\,w_{\max}M),\ s_1/(296\kappa),\ 1/(12M)\bigr)\), so that \(\sqrt E\le s_1/8\) and \(37\kappa\varepsilon_0\le s_1/8\); and \(\mu_0=s_1/4\). Lemma 3.6 gives \(\|X_k(U_R)f\|\ge s_1/2=s_0\) for real backgrounds. \(X_k^*\) is the same kind of operator with \(\gamma_\mu\mapsto-\gamma_\mu\) and the same \(P_k\), so the same bound holds for it. Take \(\delta_0=\min(1/8,s_0/(2K_5))\); Lemma 3.7 gives item 1 for complex \(U\). In finite dimension an injective operator is invertible, so \(\|X_k^{-1}\|\le2/s_0\). Take \(\alpha_0=\min(1,s_0/(4K_6))\); Lemma 3.8 gives \(\|X_\alpha f\|\ge\frac{s_0}4\|f\|\), so \(\|X_\alpha^{-1}\|\le4/s_0\). With \(\rho=\operatorname{dist}_\infty(\cdot,\Delta')\), \(1_\Delta X_k^{-1}1_{\Delta'}=1_\Delta e^{-\alpha_0\rho}X_{\alpha_0}^{-1}1_{\Delta'}\), which is item 2. Item 3: the entries of \(X_k\) are polynomials in \(e^{\pm i\theta}\), and on the open set where item 1 holds the inverse is holomorphic by Cramer's rule; covariance is Lemma 2.1(iii). □

**Remarks.** (i) Nothing in the proof uses \(d=4\) except the constants 4, 81, \(3^d\); the same proof works in every dimension. (ii) The tree (`CN1_TREE.md` L3) asked to "Port from three Euclidean dimensions to four" the construction of [D17] Lemmas 5-6. Theorem 1 is not that port; it reaches the same global bound by a route without local inverses on the fine lattice. Proposition 5.2 shows why local inverses on the fine lattice are not available from accretivity, and Corollary 4.3 supplies them on the unit lattice.

## 4. Theorem 2: an exact identity for the blocked operator, and its consequences

**Theorem 2 (blocked Hermitian part).** Let \(U\) be real, \(\bar m\in\mathbb R\), and \(X_k(U)\) invertible. Then
\[
\operatorname{Re}D_k=\frac1{a_k}D_k^*D_k+H_k^*\bigl(\operatorname{Re}D_U+\bar m\bigr)H_k .\tag{4.1}
\]
*Proof.* For real \(U\), \(\tilde Q_k=Q_k^*\) (Lemma 2.1(ii)), so \(H_k=a_kS_kQ_k^*\) and \(D_k=a_k-a_k^2Q_kS_kQ_k^*\). Hence \(\operatorname{Re}D_k=a_k-a_k^2Q_k(\operatorname{Re}S_k)Q_k^*\). From \(X_kS_k=1\), \(\operatorname{Re}S_k=S_k^*(\operatorname{Re}X_k)S_k\), and \(\operatorname{Re}X_k=\operatorname{Re}D_U+\bar m+a_kP_k\). So
\[
a_k^2Q_k(\operatorname{Re}S_k)Q_k^*=H_k^*(\operatorname{Re}D_U+\bar m)H_k+a_k(Q_kH_k)^*(Q_kH_k),
\]
using \(a_kS_kQ_k^*=H_k\) and \(P_k=Q_k^*Q_k\). Since \(Q_kH_k=1-D_k/a_k\), the last term is \(a_k-D_k-D_k^*+a_k^{-1}D_k^*D_k\). Therefore \(\operatorname{Re}D_k=D_k+D_k^*-a_k^{-1}D_k^*D_k-H_k^*(\operatorname{Re}D_U+\bar m)H_k\). Subtract \(\operatorname{Re}D_k\) from both sides. □

[check] `check_gw.py`: a 2D analogue (two-component spinors, \(L^k\in\{2,4,8\}\), a \(4\times4\) unit lattice, random real links with angle spread from 0 to 1.5, \(\bar m=0\), \(a=1\)). The residual of (4.1) was at most \(1.4\times10^{-15}\), and \(\|D_k\|\le0.94\le a\) in every case. Guidance only.

Block-spin transformations of fermions are the setting in which Ginsparg and Wilson derived their relation ([GW82]); (4.1) is a relation of the same origin for the Hermitian part, with the Wilson term as the inhomogeneous piece. It is proved here and not attributed to [GW82].

**Corollary 4.1 (every real background).** Let \(U\) be real and \(\bar m\ge0\). Then:

1. \(X_k(U)\) is invertible, and so are \(X'\) and \(D_k+\frac aLP\) (notation of Lemma 2.3).
2. \(\|D_k(U)\|\le a_k\), and \(\operatorname{Re}D_k(U)\ge a_k^{-1}D_k(U)^*D_k(U)\ge0\).
3. \(\|Q_kH_k(U)\|\le1\) and \(\frac\eta2\sum_\mu w_\mu\|\delta^U_\mu H_k(U)\phi\|^2\le a_k\|\phi\|^2\).
4. \(\|D_k+\frac aLP\|\le a_k+\frac aL\), so \(|\det(D_k+\frac aLP)|\le(a_k+\frac aL)^{4|\Lambda_1|}\), and \(D_{k+1}\) of (2.3) again obeys item 2.

No small-field condition and no bound on the field strength enters. Items 2 and 4 are the bounded half of B2 of `CN1MOD.md` §5: in every real background, the blocked kernel and the single-step fermion determinant are bounded uniformly in \(k\), \(L\), the volume and the speeds.

*Proof.* 1. By Lemma 3.1 \(\operatorname{Re}X_k\ge a_kP_k\ge0\). If \(\langle f,\operatorname{Re}X_kf\rangle=0\), then \(\delta^U_\mu f=0\) on every link and \(P_kf=0\). The first condition makes \(f\) covariantly constant: \(f(z)=U_\mu(z)f(z+\eta e_\mu)\) on every link. Telescoping along the averaging path gives \(V_k(y,x)f(x)=f(y)\), so \((Q_kf)(y)=f(y)\). Then \(P_kf=0\) forces \(f=0\). So \(\operatorname{Re}X_k\) is positive definite and \(X_k\) is injective, hence invertible. The same argument applies to \(X'\) (it has the same form). Lemma 2.3 then gives \(D_k+\frac aLP\) invertible.
2. By (4.1) and \(\operatorname{Re}D_U+\bar m\ge0\), \(\|D_kF\|^2\le a_k\operatorname{Re}\langle F,D_kF\rangle\le a_k\|F\|\|D_kF\|\).
3. With \(N=D_k/a_k\): \(\|N\|\le1\) and \(\operatorname{Re}N\ge N^*N\), so \((1-N)^*(1-N)=1-2\operatorname{Re}N+N^*N\le1-N^*N\le1\). And (4.1) gives \(H_k^*(\operatorname{Re}D_U)H_k\le\operatorname{Re}D_k\le a_k\); use Lemma 3.1.
4. \(\|P\|=1\) for real \(U\) (orthogonal projection). Hadamard's inequality \(|\det A|\le\prod_i\|Ae_i\|\le\|A\|^{n}\) on the \(4|\Lambda_1|\)-dimensional space. The last claim is (2.3) and item 2 at the next scale (after rescaling). □

**Corollary 4.2 (small fields: unit-lattice kernels).** Let \(\mathcal U_k^\sharp=\mathcal U_k(\varepsilon_0/L^2,\delta_0/L)\), \(\bar m\ge-\mu_0/L\), \(T\ge6ML\), with the constants of Theorem 1. (Field strength has dimension two, so this is the domain on which Theorem 1 also applies to \(X'\) after rescaling by \(L\).) Then for \(U\in\mathcal U_k^\sharp\):

1. \(|D_k(y,y')|\le a_k\delta_{yy'}+\frac{16a_k^2}{s_0}e^{-\alpha_0(|y-y'|_\infty-1)_+}\) (matrix norm on \(\mathbb C^4\)).
2. \(\|\Gamma_k\|\le\frac1{a_k}+\frac{8L}{s_0}\) for real \(U\) (for complex \(U\), \(\|R\|\le5/a_k\) and \(\|P\|\le4\) give \(\|\Gamma_k\|\le\frac5{a_k}+\frac{200L}{s_0}\)), and \(|\Gamma_k(y,y')|\le C(L)\,e^{-\frac{\alpha_0}L(|y-y'|_\infty-2L)_+}\).
3. \(D_k\), \(\Gamma_k\) and \(\det X_k\) are holomorphic in \(\theta\) on the interior of the domain, and covariant under real gauge transformations.

*Proof.* 1. \((Q_kS_k\tilde Q_k)(y,y')=Q_k1_{B_y}S_k1_{B_{y'}}\tilde Q_k\); the factors have norms at most 2, \(\frac4{s_0}e^{-\alpha_0\operatorname{dist}_\infty(B_y,B_{y'})}\), 2 (Theorem 1 item 2 and Lemma 3.7), and \(\operatorname{dist}_\infty(B_y,B_{y'})\ge|y-y'|_\infty-1\). 2. Use (2.1). \(R\) acts inside single \(L\)-blocks of \(\Lambda_1\). \(X'=L^{-1}\times\)(the operator of Theorem 1 at spacing \(\eta/L\)), so \(\|X'^{-1}\|\le2L/s_0\) and its block kernel decays at rate \(\alpha_0\) per scale-\((k+1)\) unit, that is \(\alpha_0/L\) per unit at scale \(k\). 3. Theorem 1 item 3 and Cramer's rule. □

**Corollary 4.3 (unit-lattice accretivity; local inverses on every subset).** Let \(U\in\mathcal U_k^\sharp\) be real, \(\bar m\ge0\), \(M_k=D_k+\frac aLP\), and \(\sigma=(\frac1{a_k}+\frac{8L}{s_0})^{-1}\). Then
\[
\operatorname{Re}M_k\ge c_N:=\frac{\sigma^2}{2a}.
\]
Consequently, for **every** subset \(Y\subset\Lambda_1\), the compression \(M_{k,Y}=1_YM_k1_Y\) on \(\ell^2(Y)\) is invertible with \(\|M_{k,Y}^{-1}\|\le1/c_N\), and \(|M_{k,Y}^{-1}(y,y')|\le\frac2{c_N}e^{-\alpha_1|y-y'|_\infty}\) for an explicit \(\alpha_1>0\) depending on \(a,w_{\min},w_{\max},L\). For complex \(U\in\mathcal U_k(\varepsilon_0/L^2,\delta_1/L)\) with \(\delta_1\) small enough, the same holds with \(c_N/2\).

*Proof.* By (4.1), \(\operatorname{Re}M_k\ge a_k^{-1}D_k^*D_k+\frac aLP\). Corollary 4.2 gives \(\|M_kF\|\ge\sigma\|F\|\). And \(\|M_kF\|^2\le2\|D_kF\|^2+2(\frac aL)^2\|PF\|^2\le2a\bigl(a_k^{-1}\|D_kF\|^2+\frac aL\|PF\|^2\bigr)\) since \(a_k\le a\). So \(\operatorname{Re}\langle F,M_kF\rangle\ge\frac{\sigma^2}{2a}\|F\|^2\). A lower bound on the Hermitian part passes to every compression: \(\operatorname{Re}\langle F,M_{k,Y}F\rangle=\operatorname{Re}\langle F,M_kF\rangle\) for \(F\) supported in \(Y\); then \(\|M_{k,Y}F\|\ge c_N\|F\|\). Decay: Combes-Thomas as in Lemma 3.8, using the kernel bound of Corollary 4.2 item 1; the change of \(M_{k,Y}\) under conjugation by \(e^{\alpha\rho}\) is at most \(\sum_{z}\sup|M_k(y,y+z)|(e^{\alpha|z|_\infty}-1)\), which is \(O(\alpha)\) for \(\alpha\le\alpha_0/2\). Complex \(U\): the resolvent identity and Theorem 1 give \(\|D_k(U)-D_k(U_R)\|=O(\delta)\). □

Corollary 4.3 supplies, in four dimensions and with a background field, the local inverses that the covariant random-walk expansion needs. In d = 3 at zero field, [D17] eq. (115) obtains them "by some Fourier analysis and taking advantage of the Wilson form of the free fermion action"; here the Wilson form enters through (4.1) and no Fourier analysis at the unit-lattice level is used.

**Corollary 4.4 (accretivity survives decoupling).** Partition \(\Lambda_1\) into cubes \(\{Y\}\). Let \(S=(s_{YY'})\) be a real positive semidefinite matrix with \(s_{YY}=1\), and let \(M_k\circ S\) have blocks \(s_{YY'}(M_k)_{YY'}\). Under the hypotheses of Corollary 4.3, \(\operatorname{Re}(M_k\circ S)\ge c_N\), so \(M_k\circ S\) is invertible with \(\|(M_k\circ S)^{-1}\|\le1/c_N\), uniformly in \(S\).

*Proof.* Write \(S=\sum_ru_ru_r^{\top}\) and \(D_r=\bigoplus_Yu_{r,Y}1_Y\). Then \(A\circ S=\sum_rD_rAD_r\) for every block operator \(A\), so \(A\ge0\) implies \(A\circ S\ge0\). Apply this to \(A=\operatorname{Re}M_k-c_N\): \(\operatorname{Re}(M_k\circ S)-c_N(1\circ S)\ge0\), and \(1\circ S=1\) because \(s_{YY}=1\). □

Interpolation matrices of the Brydges-Kennedy type, \(s_{YY'}=\min\) of the forest parameters on the path from \(Y\) to \(Y'\), are positive semidefinite with unit diagonal; so cluster expansions of \(\log\det M_k\) and of \(\Gamma_k\) with such parameters keep the bound of Corollary 4.3 at every interpolation point. (Positive semidefiniteness of these matrices is a standard fact; it is not used elsewhere in this file, and the corollary is stated for any such \(S\).)

## 5. Large fields and the fine lattice: three exact facts

These facts locate the obstacle of §7. They are proved; the [check] at the end is guidance.

**Proposition 5.1 (zero modes pass to the blocked operator exactly).** Let \(U\) be real, \(\bar m\ge0\) (so \(X_k\) is invertible, Corollary 4.1). Then \(Q_k\) is injective on \(\ker(D_U+\bar m)\) and
\[
\ker D_k(U)=Q_k\,\ker(D_U+\bar m).
\]
*Proof.* If \((D_U+\bar m)\psi_0=0\), then \(X_k\psi_0=a_k\tilde Q_kQ_k\psi_0\), so \(\psi_0=H_k\Phi\) with \(\Phi=Q_k\psi_0\). Then \(Q_kH_k\Phi=\Phi\) and \(D_k\Phi=a_k(1-Q_kH_k)\Phi=0\). If moreover \(\Phi=0\), then \(X_k\psi_0=0\), so \(\psi_0=0\): injectivity. Conversely, if \(D_k\Phi=0\), put \(\psi=H_k\Phi\); then \(Q_k\psi=\Phi\) and \((D_U+\bar m)\psi=X_k\psi-a_kP_k\psi=a_k\tilde Q_k(\Phi-Q_k\psi)=0\). □

So the blocked operator inherits every exact zero mode of the fine operator, with the same multiplicity. For U(1) backgrounds on \(T^4\) with constant \(F_{12},F_{34}\) and flux quanta \(n_{12},n_{34}\), the continuum Dirac operator has index \(n_{12}n_{34}\) (standard; not used as a proof step). The Wilson term lifts these modes. Proposition 5.1 says that whatever survives near zero in \(D_U+\bar m\) also appears in \(D_k\); a uniform lower bound for \(D_k+\frac aLP\) on a large-field region therefore needs the block averages to separate those modes.

**Proposition 5.2 (accretivity on the fine lattice is only of order \(\eta\)).** Let \(U\equiv1\) (with the antiperiodic signs) and \(\bar m=0\). There is \(f\) with \(\|f\|=1\) and
\[
\operatorname{Re}\langle f,X_kf\rangle\le2\pi^2w_{\max}\,\eta .
\]
*Proof.* Take \(f(x)=c\cos(2\pi x_1)e\) for a fixed unit spinor \(e\), with \(c>0\) chosen so that \(\|f\|=1\). Each unit cube contains a full period of \(n=L^k\ge2\) equally spaced points in \(x_1\), and \(\sum_{j<n}\cos(2\pi j/n)=0\), so every block average vanishes and \(P_kf=0\) (the transports are 1 inside cubes, which do not cross the time boundary). On the lattice \(\|\delta_1f\|^2=4\eta^{-2}\sin^2(\pi\eta)\|f\|^2\) (for \(n\ge3\) the two exponentials of the cosine are orthogonal; for \(n=2\) they coincide). By Lemma 3.1, \(\operatorname{Re}\langle f,X_kf\rangle=\frac\eta2w_1\|\delta_1f\|^2\le2\pi^2w_1\eta\). □

Consequence. A compression \(1_\Delta X_k1_\Delta\) to a fine-lattice cube \(\Delta\) of side larger than one cannot be inverted uniformly in \(k\) by a numerical-range argument: its numerical range comes within \(O(\eta)\) of zero (take \(f\) above times a cutoff; the cutoff costs \(O(\eta)\) as well). This does not show that such compressions are not uniformly invertible; it shows that any proof must use more than the Hermitian part. Theorem 1 uses the singular values of the global operator; Corollary 4.3 moves to the unit lattice, where (4.1) makes the Hermitian part strictly positive.

**Proposition 5.3 (no small-link gauge on a large-field cube).** Let a cube contain a square loop \(\gamma\) of rescaled side \(\ell\) in a coordinate plane, with holonomy angle \(\Theta\in(-\pi,\pi]\). Then for every real gauge transformation \(g\) some link of \(\gamma\) has \(|\theta^g_\mu(x)|\ge|\Theta|\eta/(4\ell)\) (representatives in \((-\pi,\pi]\)), and so \(\eta^{-1}|U^g_\mu(x)-1|\ge|\Theta|/(2\pi\ell)\).

*Proof.* \(\gamma\) has \(4\ell/\eta\) links, and the signed sum of the representatives is \(\equiv\Theta\) mod \(2\pi\). If every representative had modulus below \(|\Theta|\eta/(4\ell)\), the sum would have modulus below \(|\Theta|\le\pi\), hence would equal \(\Theta\), a contradiction. Finally \(|e^{i\theta}-1|\ge\frac2\pi|\theta|\) for \(|\theta|\le\pi\). □

For a uniform rescaled field \(F\) in the plane of \(\gamma\), \(\Theta=F\ell^2\) when \(F\ell^2\le\pi\). Taking \(\ell=\min(1,\sqrt{\pi/F})\): in every gauge, some hopping coefficient of \(D_{U^g}-D_1\) on the cube is at least \(\min(F/2\pi,\ 1/2)\). Once \(F\ge2\pi s_0\), this is at least the coercivity constant \(s_0\) of Theorem 1. So on a cube whose field strength is of order one in rescaled units, the step "Neumann series around the free operator in a local gauge" is not available in any gauge.

[check] `check_flux.py`: the 2D analogue with uniform flux \(N_\Phi\) quanta on a \(4\times4\) unit lattice, \(a=1\), \(\bar m=0\), \(L=2\) for the unit-lattice step. At rescaled field strength \(F\approx6.3\): \(\sigma_{\min}(X_k)=0.675\) at \(\eta=1/4\) and \(0.365\) at \(\eta=1/8\) (zero field: \(1.28\), \(1.26\)). The ratio \(\sigma_{\min}/(\eta F)\) is 0.43 and 0.46, as expected if would-be zero modes are lifted by the Wilson term at a rate of order \(\eta F\). On the same toy, \(\sigma_{\min}(D_k+\frac aLP)\) stayed between 0.22 and 0.83 and \(\lambda_{\min}(\operatorname{Re}(D_k+\frac aLP))\) stayed positive (at least 0.22). The toy is too coarse to have more flux quanta than unit cubes at small \(\eta F\), which is the regime where Proposition 5.1 predicts near-zero modes of \(D_k+\frac aLP\). Guidance only: this suggests that Theorem 1's constant cannot be made uniform in \(k\) on large fields, and it neither proves nor refutes a uniform bound for \(D_k+\frac aLP\).

## 6. The marginal coordinates

**Scheme for the census.** Take the background-field scheme of §2 with two changes that restore the lattice symmetries. Blocks are centered (odd \(L\)), and each transport is the average of the phases along all \(4!\) rectilinear orderings, as [D17] eq. (11) does in d = 3. Theorem 1, Corollaries 4.1-4.4 and Propositions 5.1-5.2 hold verbatim for this choice: their proofs use only \(Q_k\tilde Q_k=1\), unimodular transports for real \(U\), and \(|V_k'-1|\le12\varepsilon\) in the axial gauge of a cube (an average of phases each at most \(12\varepsilon\)). The photon is blocked by a gauge-covariant linear averaging, so the scale-\(k\) effective action is a gauge-invariant functional of the coarse photon and covariant in the coarse fermions. "Local coordinate" means a coefficient of a local monomial in the localized part of that action.

**Lemma 6.1 (census).** In this scheme, for M″ with \(q_1=q_2=1\):

1. *Symmetries.* The exact step commutes with: lattice gauge transformations (Lemma 2.1(iii)); the species phases \(\psi_a\mapsto e^{i\alpha_a}\psi_a\) (\(a=1,2\)); translations by the block lattice; the spatial cubic group with its spinor action; spatial inversion; Euclidean time reflection; charge conjugation; and the species exchange \(\sigma\), which maps the data \((v_1,v_2,\bar m_1,\bar m_2)\) to \((v_2,v_1,\bar m_2,\bar m_1)\).
2. *Fermions.* The local fermion monomials of dimension at most 4 allowed by item 1 are, for each species, \(\bar\psi_a\psi_a\) (dimension 3), \(\bar\psi_a\gamma_0\nabla_0\psi_a\) and \(\sum_j\bar\psi_a\gamma_j\nabla_j\psi_a\) (dimension 4). No monomial mixes the species. Coefficients: \(\bar m_a\) (relevant), \(z_{a,0}\), \(z_{a,s}\) (marginal); \(v_a=z_{a,s}/z_{a,0}\).
3. *Photon.* The local gauge-invariant photon monomials of dimension at most 4 are the constant and \(\sum_jF_{0j}^2\), \(\sum_{j<l}F_{jl}^2\). Coefficients \(z_E,z_B\) (marginal); \(c^2=z_B/z_E\) and \(G=e^2/z_E\). No photon mass is generated: \(\det X_k(U^g)=\det X_k(U)\) and \(D_k(U^g)=G_1D_k(U)G_1^{-1}\). The census is taken for the model in which the exact photon component is removed; by the Hodge decoupling of `CN1MOD_REFEREE.md` G6 it has the same gauge-invariant observables as M″. There the supplied mass stays in the Gaussian orbit weight \(\tfrac12m^2|A_{\rm coex}|^2\), which is quadratic and integrated exactly; it adds no local coordinate. (Averaging over the exact component instead would conjugate the charged kernel by random gauge transformations; that is the gauge-fixed object of `CN1.md` GAP 6.2, and it is not used here.) The charge is not a separate coordinate: the fermion action stays covariant with the same \(e\). All these coefficients are scheme coordinates, "gauge- and scheme-dependent until an observable bridge is supplied" (`CN1MOD.md` §1, definition 2).
4. *Exchange-odd data.* The exchange-odd local coordinates of dimension at most 4 are \(\bar m_1-\bar m_2\) (relevant) and \(z_{1,0}-z_{2,0}\), \(z_{1,s}-z_{2,s}\) (marginal). If each step rescales \(\psi_a\) so that \(z_{a,0}=1\) (a choice in the definition of the step), the only exchange-odd marginal coordinate is \(\Delta=v_1-v_2\).
5. *Nodes.* Each Wilson species has exactly one light node: the free symbol vanishes only at \(p=0\), because \(m(p)\ge2w_{\min}/\eta\) whenever some \(\eta p_\mu=\pi\) (and \(\sin\eta p_\mu=0\) for all \(\mu\) forces each \(\eta p_\mu\in\{0,\pi\}\)). So M″ has no inter-node contrasts; the slow node-contrast modes of the quartet note (§0.1) do not arise.
6. *Non-covariant schemes.* If the fermion propagator is split without gauge covariance (finite-range decomposition of the free covariance), gauge invariance no longer constrains the local photon terms. The lattice symmetries then allow, in addition, the masses \(A_0^2\) and \(\sum_jA_j^2\) (relevant), two-derivative quadratic terms that gauge invariance would tie together (marginal), and four quartics \(A_0^4\), \(A_0^2\sum_jA_j^2\), \((\sum_jA_j^2)^2\), \(\sum_jA_j^4\) (marginal). All of them are exchange-even.

*Proof.* Item 1: each statement is a direct check on the Wilson action, on the Gaussian blocking term and on the averaging (centered blocks and averaged orderings are invariant under the cubic group and the reflections; charge conjugation maps transports to their inverses together with \(A\mapsto-A\)). Item 2: a fermion bilinear \(\bar\psi_a\Gamma\psi_b\) or \(\bar\psi_a\Gamma\nabla_\mu\psi_b\) with \(a\ne b\) changes under \(e^{i(\alpha_b-\alpha_a)}\). Without derivative, \(\Gamma\in\{\gamma_5,\gamma_\mu\gamma_5,\sigma_{\mu\nu}\}\) is excluded by inversion or time reflection, and \(\Gamma=\gamma_\mu\) by charge conjugation. With one derivative: \(\Gamma=1\) gives, up to a total difference, the charge-odd antisymmetric combination; \(\gamma_5\) and \(\gamma_\mu\gamma_5\) are excluded by inversion; \(\gamma_\nu\nabla_\mu\) with \(\nu\ne\mu\) needs an invariant pairing of a spatial vector with a scalar, which the cubic group does not have; \(\sigma_{0j}\nabla_j\) is odd under time reflection (\(\gamma_5\gamma_0\sigma_{0j}\gamma_0\gamma_5=-\sigma_{0j}\)); \(\epsilon_{jlm}\sigma_{jl}\nabla_m\) is odd under inversion. What remains is item 2. Item 3: a gauge-invariant local functional of dimension at most 4 is a function of \(F\); the quadratic forms on the electric triplet and on the magnetic triplet invariant under the cubic group are multiples of \(\sum_jF_{0j}^2\) and \(\sum_{j<l}F_{jl}^2\) (each triplet is an irreducible representation); \(\sum_jF_{0j}\epsilon_{jlm}F_{lm}\) is odd under inversion. Gauge invariance of \(\det X_k\) is Lemma 2.1(iii). Item 4: \(\sigma\) swaps the per-species coefficients and fixes the photon ones. Item 5: \(m(p)=\eta^{-1}\sum_\mu w_\mu(1-\cos\eta p_\mu)\). Item 6: the monomials of degree 2 and 4 in \(A\) invariant under the cubic group, inversion, time reflection (\(A_0\mapsto-A_0\)) and \(A\mapsto-A\); a cubic-invariant symmetric 3-tensor would be needed for \(A_0\,(\cdot)^3\) terms and none is inversion-even. □

**What item 4 does for UB″.** In `CN1MOD.md`, \(E\) collects "all other exchange-odd components", and U0 and U3 control it. In the covariant scheme with the normalization of item 4, \(E\) contains no marginal coordinate; it contains only irrelevant exchange-odd parts of the polymer remainder, and the relevant difference \(\bar m_1-\bar m_2\) is fixed by the choice of the two critical counterterms. This narrows U0 and U3; it does not prove them.

## 7. The stopping lemma LF and the three attacks

### 7.1 Why (T3) needs a local large-field step

A real invariant domain must bound the photon fluctuation integral for every photon configuration. In Balaban's scheme the configurations are split cube by cube into small and large fields, and large-field cubes carry a small factor. In d = 3, in a unit volume, Dimock bounds the large-field contributions globally: "e−1/4 p(e0)2 = O(L−nN/2en) beats |T0N|M = L3NM−3" ([D22], after eq. (19)), with \(p(e_0)=(-\log e_0)^p\) and \(e_0=L^{-N/2}e\), so \(e^{-p(e_0)^2/4}=e^{-cN^{2p}}\). In M″'s infrared problem this global bound fails. At scale \(k\) the coupling is \(G_k\ge G_0/(1+b_+G_0k)\) (the lower half of (W)'s coupling condition), so a factor \(e^{-c(-\log G_k)^{2p}}\) is \(e^{-c(\log k+O(1))^{2p}}\). The rescaled torus at scale \(k\) has at least \(L^{4(N-k)}\) unit cubes when the original side is at least \(L^N\). For \(k\le N/2\) and \(N\) large, \(L^{4(N-k)}e^{-c(\log k)^{2p}}\to\infty\). So the large-field contributions must be bounded **locally**: a large-field region \(R\) may cost at most \(e^{C|R|}\) relative to a small-field reference, with \(C\) uniform in \(k\), \(N\) and the volume. For the fermions this is a statement about how \(D_k(U)\) and \(\det(D_k+\frac aLP)\) change when \(U\) changes on \(R\). Corollary 4.1 bounds both in every background. It does not localize the change. That is Lemma LF.

### 7.2 The lemma

Let \(\mathcal U_k^\sharp\) be as in Corollary 4.2. Let \(R\subset\Lambda_1\) be a union of unit cubes, \(U'\in\mathcal U_k^\sharp\) real, and \(U\) real with \(U=U'\) on every link outside \(R\). Let \(\Phi_R=\eta^{-2}\max_{p\subset R}|\varphi_p(U)|\), the largest rescaled field strength of \(U\) in \(R\).

**Lemma LF (open).** There are \(C,\gamma,p_*>0\), independent of \(k\), the volume, \(U\), \(U'\) and \(R\), such that for all \(y,y'\in\Lambda_1\)
\[
\bigl|D_k(U)(y,y')-D_k(U')(y,y')\bigr|\le C(1+\Phi_R)^{p_*}\,e^{-\gamma(\operatorname{dist}(y,R)+|y-y'|_\infty)} .
\]

**Consequence (proved from LF).** \(\log|\det M_k(U)|-\log|\det M_k(U')|\le C'(1+\Phi_R)^{p_*}|R|\), where \(M_k=D_k+\frac aLP\). *Proof.* \(M_k(U)M_k(U')^{-1}=1+A\) with \(A=(\Delta+\frac aL(P(U)-P(U')))\Gamma_k(U')\) and \(\Delta=D_k(U)-D_k(U')\). \(|\det(1+A)|\le\prod_i(1+\sigma_i(A))\le e^{\|A\|_1}\). The trace norm of \(\Delta\) is at most \(4\sum_{y,y'}\|\Delta(y,y')\|\le C''(1+\Phi_R)^{p_*}|R|\) by LF; \(P(U)-P(U')\) is supported on the \(L\)-blocks that meet \(R\), with norm at most 2, so its trace norm is at most \(8L^4|R|\); and \(\|\Gamma_k(U')\|\) is bounded by Corollary 4.2. □

LF is the locality half of B2. It is the precise point where the block-operator work of this file meets the large-field step of (T3). When \(U\) is itself small-field, LF holds with \(\Phi_R\) small, by Theorem 1 and the resolvent identity; the content of LF is the large-field case.

### 7.3 Two exact lemmas toward LF

**Lemma 7.1 (near-null vectors have small block averages).** For real \(U\), \(\bar m\ge0\) and every \(\psi\), \(\ \|Q_k\psi\|^2=\|P_k\psi\|^2\le a_k^{-1}\|\psi\|\,\|X_k\psi\|\).

*Proof.* Lemma 3.1: \(a_k\|P_k\psi\|^2\le\operatorname{Re}\langle\psi,X_k\psi\rangle\le\|\psi\|\|X_k\psi\|\). □

This is the cancellation behind Corollary 4.1: if \(X_k\psi_0=\sigma\tilde\psi_0\) with \(\sigma\) small, the term \(\sigma^{-1}\psi_0\tilde\psi_0^{*}\) of \(S_k\) enters \(D_k=a_k-a_k^2Q_kS_k\tilde Q_k\) only through \(Q_k\psi_0=O(\sigma^{1/2})\) and \(\tilde Q_k^*\tilde\psi_0=O(\sigma^{1/2})\), so it contributes \(O(1)\).

**Lemma 7.2 (geometric resolvent reduction).** Let \(\chi:\Lambda_\eta\to[0,1]\) equal 1 at distance at least 3 from \(R\) and 0 within distance 2, with \(|\chi(x)-\chi(x')|\le|x-x'|_\infty\). Let \(\Lambda_\chi\) be the union of the unit cubes that meet the \(\eta\)-neighbourhood of \(\{0<\chi<1\}\), and \(\mathcal C=[X_k(U'),\chi]\). (Every nonzero entry \(\mathcal C(x,x')\) has \(\chi(x)\ne\chi(x')\) with \(x,x'\) neighbours or in one unit cube; since \(|\chi(x)-\chi(x')|<1\) there, one of the two values lies in \((0,1)\), so \(\mathcal C=1_{\Lambda_\chi}\mathcal C1_{\Lambda_\chi}\).) Then \(\|\mathcal C\|\le16w_{\max}+4a_+\le K_6\) and, for unit cubes \(B_y,B_{y'}\subset\{\chi=1\}\),
\[
\Delta(y,y')=a_k^2\,Q_k1_{B_y}\Bigl[S'\chi\,\mathcal C\,S'+S'\,\mathcal C\,\bigl(1_{\Lambda_\chi}S_k(U)1_{\Lambda_\chi}\bigr)\,\mathcal C\,S'\Bigr]1_{B_{y'}}\tilde Q_k,\qquad S'=S_k(U').
\]
*Proof.* \(X_k(U)\) and \(X_k(U')\) agree on functions supported where \(\chi\ne0\) (hops have length \(\eta\), averaging acts inside unit cubes, and \(R\) is a union of unit cubes). So for \(g=\chi g\): \(X_k(U)(\chi S'g)=g+\mathcal CS'g\), that is, \(S_k(U)g=\chi S'g-S_k(U)\mathcal CS'g\). The adjoint statement gives \(1_{B_y}S_k(U)=1_{B_y}S'\chi+1_{B_y}S'\mathcal CS_k(U)\). \(\mathcal C\) is supported in \(\Lambda_\chi\). Combine, use \((1-\chi)1_{B_y}=0\), and \(\Delta=-a_k^2Q_k(S_k(U)-S')\tilde Q_k\) between \(B_y\) and \(B_{y'}\) (the averaging on these cubes does not see \(R\)). The bound on \(\mathcal C\) is the computation of Lemma 3.8 with \(\alpha\rho\) replaced by \(\chi\). □

By Theorem 1 for \(U'\), every factor except \(1_{\Lambda_\chi}S_k(U)1_{\Lambda_\chi}\) is bounded and decays exponentially away from \(R\). So LF follows from a bound on the large-field block \(1_{\Lambda_\chi}S_k(U)1_{\Lambda_\chi}\) that is polynomial in \(\Phi_R\) and decays along \(\Lambda_\chi\), uniformly in \(k\). It also follows from any argument that keeps the cancellation of Lemma 7.1.

### 7.4 The three named attacks

**Attack 1: local axial-gauge resolvent expansion.** *Plan.* As in [D17] Lemma 6, part IV: "Lemma 6 for A ∈ G̃k,Ω can be obtained using gauge transformations and expansions around A = 0." Build local inverses on cubes meeting \(R\) by choosing a local axial gauge and expanding around the free operator; patch them as in Lemma 5. *Fails at:* the expansion around \(A=0\) on cubes meeting \(R\). By Proposition 5.3, once the field strength on a cube reaches \(2\pi s_0\), every gauge leaves a hopping perturbation of size at least \(s_0\) on that cube. That is the size of the coercivity constant, so the Neumann series has no convergence criterion there. Proposition 5.1 adds a structural reason: the large-field operator carries the would-be zero modes of \(D_U\), which no series around the free operator reproduces. The finite-volume global substitute of [D22] eq. (19) fails in the infrared by §7.1.

**Attack 2: covariant random-walk expansion.** *Plan.* Use Corollary 4.3's local inverses on the small-field part, and the geometric resolvent identity (Lemma 7.2) to cross into \(R\); bound every term by products of local norms, as a random-walk expansion does. *Fails at:* the bound on the large-field block \(1_{\Lambda_\chi}S_k(U)1_{\Lambda_\chi}\). A random-walk bound uses only norms of local resolvents. Inside a large-field region those norms are at least \(1/\sigma_{\min}(X_k(U)|_{\rm loc})\). The [check] of §5 shows \(\sigma_{\min}(X_k)\) falling in proportion to \(\eta F\) at fixed rescaled field strength (0.675 at \(\eta=1/4\), 0.365 at \(\eta=1/8\), \(F\approx6.3\)), as expected from Proposition 5.1 and the Wilson lifting of zero modes. If that scaling holds, the norm bound grows like \(1/(\eta F)=L^k/F\), which is not uniform in \(k\). The true \(D_k(U)\) stays bounded (Corollary 4.1) because of the cancellation of Lemma 7.1, which passes through the global block averages; a product of local norms does not see it. The scaling is a [check], not a theorem; but no available estimate bounds the large-field block uniformly in \(k\), so the step is not supplied.

**Attack 3: finite-range polymer localization.** *Plan.* Use only the background-uniform bounds of Corollary 4.1 (\(\|D_k(U)\|\le a_k\), \(\|Q_kH_k\|\le1\), the energy bound on \(H_k\)). Localize \(D_k(U)\) by a Combes-Thomas conjugation or a finite-range decomposition of \(S_k(U)\), and extract polymer activities supported near \(R\). *Fails at:* a background-uniform decay estimate. (i) Conjugation by \(e^{\alpha\rho}\) is not unitary, so \(e^{\alpha\rho}D_ke^{-\alpha\rho}\) does not satisfy (4.1); the size of the conjugation error is controlled by the kernel decay of \(D_k(U)\), which is what LF asserts. The argument is circular. (ii) Localizing through \(H_k\) instead: Corollary 4.1 item 3 gives only \(\|\nabla_UH_k\phi\|^2\le\frac{2a_k}{\eta w_{\min}}\|\phi\|^2\); turning this energy bound into an \(L^2\) bound on \(R\) loses \(\eta^{-1/2}=L^{k/2}\). (iii) A finite-range decomposition of \(S_k(U)\) needs a positive operator to decompose; \(S_k(U)S_k(U)^*\) is positive, but its norm is \(\sigma_{\min}(X_k(U))^{-2}\), the quantity that Attack 2 could not bound.

**Status.** LF is open after these three attacks. The step that each lacks is different: a convergent local expansion (1), a uniform large-field block bound (2), a background-uniform decay estimate (3). **The route that the analysis points to** keeps Lemma 7.1's cancellation inside Lemma 7.2: split \(1_{\Lambda_\chi}S_k(U)1_{\Lambda_\chi}\) into its near-null part, which enters \(\Delta\) only through block averages of size \(O(\sigma^{1/2})\), and a remainder bounded by the next singular value. That needs a gap between the near-null singular values of \(X_k(U)\) and the rest, uniform in \(k\), which is not known. It is recorded as a route, not as a fourth attack.

### 7.5 What (T3) needs besides LF

With LF, the route still needs two steps. They were not attempted, because the run stopped at LF.

- **S-small.** On small fields, integrate the scale-\(k\) photon fluctuation by a cumulant (cluster) expansion. Theorem 1 gives analyticity of \(\det X_k\) and \(D_k\) on a complex polydisc of radius of order \(\delta_0\) in \(eA\), that is of order \(\delta_0G_k^{-1/2}\) in the normalized fluctuation; Corollary 4.4 keeps the fermionic bounds under decoupling. The second cumulant is the one-loop step; the higher cumulants should be \(O(G_k^2)\).
- **M1 (one-loop matching).** The per-step one-loop speed increment of the block scheme equals \(hG_k\mathcal F(x_k)\) up to \(O(G_ke^{-\beta k}+G_ke^{-\beta(N-k)})\). Its leading term should follow from the scale invariance of the free fixed point and the universality of the logarithm; the lattice and mass corrections from the approach of the rescaled free operators to that fixed point.

**No counterexample to (W) was found.** `CN1.md` Proposition 4 defeats (W)-type convergence with a persistent \(O(G)\) source that does not vanish at consensus. By Lemma 6.1(4), in the covariant scheme no marginal coordinate other than \(\Delta\) can carry such a source. A persistent source would have to come from the relevant difference \(\bar m_1-\bar m_2\) (fixed by the critical counterterms) or from irrelevant terms, which are expected to decay like \(L^{-k}\). This supports (W); it does not prove it.

## 8. Readings and specifications

This file proposes no reading, no law text and no change to any axiom or working-set entry. It works on the supplied model M″, which `CN1MOD.md` calls "a proposed supplied model for rung 1, not a realization of a live law".

Three definitions are used as hypotheses of theorems about M″. They are four-tested here for completeness (1: states or fixes a part's target; 2: open-ended; 3: settles a downstream physics question by premise; 4: adds structure or constants its reasons do not need). P = pass, C = conditional, F = fail. None is adopted.

| Definition | 1 | 2 | 3 | 4 | Note |
|---|---|---|---|---|---|
| (T1)-(T3) of §1.2, the lane's target made exact | P | P | P | P | They restate this lane's own target from `CN1_TREE.md` lines 202-216 and 945; they fix no other part's target. |
| Small-field domain \(\mathcal U_k(\varepsilon,\delta)\) (§3.1) | P | P | P | P | A hypothesis of Theorem 1; gauge invariant; its two constants are the ones the proof needs. |
| Census scheme (centered blocks, averaged orderings, covariant photon averaging, \(z_{a,0}=1\); §6) | P | P | C | P | A choice of RG scheme for M″. Test 3 is C: the speeds it defines are scheme coordinates; their identification with invariant thresholds is OBS's question, not settled here. |

## FINISH

**Proved here (pass 1, not distilled or refereed).**
- Lemmas 2.1-2.3: the fermionic half of one exact blocking step of M″ at a fixed background is a Gaussian Grassmann integral with kernel \(D_k\) and determinant \(\det X_k\); the composition law (2.1)-(2.3) links scale \(k\) to \(k+1\) exactly.
- **Theorem 1 (B1 of `CN1MOD.md`).** For \(X_k(U)=D_{w,U}+\bar m+a_kP_k(U)\) in four dimensions: \(\|X_k^{-1}\|\le2/s_0\) and \(\|1_\Delta X_k^{-1}1_{\Delta'}\|\le\frac4{s_0}e^{-\alpha_0\operatorname{dist}(\Delta,\Delta')}\), holomorphic and gauge covariant, on the complex small-field domain \(\mathcal U_k(\varepsilon_0,\delta_0)\), for \(\bar m\ge-\mu_0\), with explicit constants independent of \(k\), \(L\), the volume, the background and \(v\in[v_-,v_+]\). The domain is invariant under real gauge transformations, and the proof (IMS localization in local axial gauges, Lemmas 3.1-3.8) never compares two local gauges.
- **Theorem 2.** The exact identity \(\operatorname{Re}D_k=a_k^{-1}D_k^*D_k+H_k^*(\operatorname{Re}D_U+\bar m)H_k\) for every real background.
- Corollary 4.1 (every real background, \(\bar m\ge0\), no small-field condition): \(\|D_k(U)\|\le a_k\), \(\operatorname{Re}D_k\ge a_k^{-1}D_k^*D_k\), \(\|Q_kH_k\|\le1\), an energy bound on \(H_k\), and \(|\det(D_k+\frac aLP)|\le(a_k+\frac aL)^{4|\Lambda_1|}\). This is the bounded half of B2.
- Corollary 4.2 (unit-lattice kernel bounds on small fields); Corollary 4.3 (\(\operatorname{Re}(D_k+\frac aLP)\ge c_N\), hence uniformly bounded, decaying inverses of every compression: the local inverses of Balaban's random-walk expansion in d = 4 with a background field); Corollary 4.4 (the bound survives decoupling by positive semidefinite interpolation matrices).
- Proposition 5.1 (\(\ker D_k=Q_k\ker(D_U+\bar m)\), injectively); Proposition 5.2 (the fine-lattice numerical range of \(X_k\) comes within \(2\pi^2w_{\max}\eta\) of zero); Proposition 5.3 (no small-link gauge around a loop of large holonomy).
- Lemma 6.1 (census): in the covariant scheme the marginal coordinates are \(z_{a,0},z_{a,s}\) (\(a=1,2\)), \(z_E,z_B\); the relevant ones \(\bar m_1,\bar m_2\) and the constant; the only exchange-odd marginal coordinate after normalization is \(\Delta=v_1-v_2\); each Wilson species has one light node; the extra photon coordinates of non-covariant schemes are exchange-even.
- §7: the infrared failure of the finite-volume global large-field bound (§7.1); LF implies the one-sided determinant bound; Lemma 7.1 (near-null vectors have block averages \(O(\sigma^{1/2})\)); Lemma 7.2 (exact geometric-resolvent reduction of LF to the large-field block).

**Counterexamples.** None to a stated claim. No counterexample to (W) was found (§7.5).

**Open, by name.**
- **LF** (§7.2): open after three named attacks. The local axial-gauge resolvent expansion fails at "expansion around \(A=0\) on large-field cubes" (Propositions 5.1, 5.3; and §7.1 for the global substitute). The covariant random-walk expansion fails at "a uniform bound on the large-field block \(1_{\Lambda_\chi}S_k(U)1_{\Lambda_\chi}\)" (local norms miss the cancellation of Lemma 7.1; [check] suggests \(\sigma_{\min}(X_k)\propto\eta F\) on large fields). Finite-range polymer localization fails at "a background-uniform decay estimate for \(D_k(U)\) or \(H_k(U)\)" (conjugation breaks (4.1); the energy bound loses \(\eta^{-1/2}\)).
- **(T3)**, the lane's target "one exact blocking step and a real invariant domain supporting estimate (W)": open. On this file's route it needs LF, then **S-small** and **M1** (§7.5), which were not attempted because the run stopped at LF.
- **UB″**: open, kept as the stronger alternative; Lemma 6.1(4) narrows U0 and U3 to irrelevant exchange-odd data and the tuned difference \(\bar m_1-\bar m_2\).
- Inherited, unchanged: R1″-MOD[d], R1″-MOD, R1-MOD, LIMIT, OBS, C1, and the framework bridges listed in `CN1MOD.md` §5.

**What changes downstream.**
1. `CN1_TREE.md` node RG: its first hard step, "B1 with complex backgrounds on compatible local gauges", is supplied by Theorem 1 (with Corollaries 4.2-4.3 for the unit-lattice operators). The next step on the background-field route is LF, then S-small and M1.
2. `CN1MOD.md` B2 splits into a proved bounded half (Corollary 4.1) and the open locality half LF.
3. `CN1MOD.md` C1 (generated photon quartic and regulator) concerns non-covariant schemes only: in the covariant scheme no photon mass or quartic coordinate exists (Lemma 6.1(3), (6)).
4. The speeds defined here are scheme coordinates; OBS and LIMIT are not affected.
5. Citations: the tree's L3 locator is right for [D17] Lemmas 5-6 and Eqs. (94)-(95); [D17]'s Theorem 1 is the gauge-field minimizer regularity theorem, not a fermion bound. The L4 locator of [BBS15] stays unverified. The digest missed one repository note on the same technique (`docs/GAUGED_LOG_TRANSFER_QUASILOCALITY_COMBES_THOMAS_NARROW_THEOREM_NOTE_2026-06-13.md`, §0.1).
6. No owner question arises; nothing is proposed for adoption; `docs/MINIMAL_AXIOMS_2026-06-29.md` and the working set are unchanged.
