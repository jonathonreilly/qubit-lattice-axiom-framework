# Literature notes: Balaban's method in open sources (session 5, 2026-10-26)

**Provenance.** arXiv identifiers, titles and dates were checked against the arXiv API (export.arxiv.org). The PDFs were
fetched from arxiv.org/pdf/<id> into the session scratchpad, and their text was extracted with pypdf, with page markers.
Statements below are transcribed from that text; "p." is the PDF page, which matches the printed page number in every
paper read.

**Tags.**
- **[read]**: I read the passage myself in the extracted text.
- **[read-skim]**: the section was located and its statement read, but not the proof.
- **[not-read]**: only the bibliographic entry is known. Journal data come from Dimock's reference lists, which are
  [read].

Formulas are transcribed with light normalisation of the PDF extraction (sub/superscripts flattened). Nothing here is
paraphrased from memory.

**Correction to the session brief.** Dimock's "The renormalization group according to Balaban" I-III treats the
**scalar φ⁴ model in d = 3**, not scalar QED. The abstracts say "the scalar phi^4 model on a toroidal lattice in dimension
d=3" [read]. Dimock I p.1 calls it "a special case of the scalar QED model treated by Balaban" [read]. QED in d = 3 is a
separate series: 1512.04373, 1712.10029, 2009.01156, and the overview 2204.07201.

---

## 1. J. Dimock, "The Renormalization Group According to Balaban - I. Small fields", arXiv:1108.1335 (v2; 52 pp.) [read-skim; sections 1, 3.1-3.2, 4.1 and App. B read]
Journal: Rev. Math. Phys. 25 (2013) 1330010 (from the reference list of 2204.07201, p.16 [read]).

- **Model (p.2, eqs. 1-7).**
  - Torus T^{-N}_M = (L^{-N}Z / L^M Z)^3.
  - Density ρ_N(φ) = exp(-½⟨φ, (-Δ + μ̄)φ⟩ + V_N(φ)), with V_N = ε_N Vol + ½ μ_N ∫φ² + ¼ λ ∫φ⁴.
- **Stability theorem, Theorem 1 (p.2, eq. 7).** "For any λ, μ̄ > 0 there is a choice of renormalization counterterms
  ... and a constant c such that exp(-c Vol(T_M)) ≤ Z_{M,N}/Z_{M,N}(0) ≤ exp(c Vol(T_M)) for all M, N."
  - The volume parameter M is arbitrary, with bulk dependence. (The proof is in part III.)
- **Small-field sets.**
  - Definition 1 (p.14, eq. 110). S_k is the set of Φ_k with |Φ_k - Q_k φ_k| ≤ p_k, |∂φ_k| ≤ p_k and
    |φ_k| ≤ λ_k^{-1/4} p_k, where φ_k = a_k G_k Q_k^T Φ_k is the minimiser.
  - The threshold is p_k = (-log λ_k)^p (eq. 109). The fields are dimensionless, so the bounds are per scale.
  - Definition 2 (p.15, eq. 111) gives the complex analyticity domain R_k.
- **Polymer norm (p.16, eqs. 118-120).**
  - ||E(X)||_k = sup_{φ∈R_k} |E(X, φ)|, and ||E||_{k,κ} = sup_X ||E(X)||_k e^{κ d_M(X)}.
  - M d_M(X) is the length of the shortest tree joining the M-cubes of X.
  - Inequality (122): d_M(X) ≤ |X|_M ≤ 3^d(1 + d_M(X)).
- **Normalisation (p.18, eq. 135).** E(X,0) = 0, E_2(X,0;1,1) = 0 and E_2(X,0;1,x_μ) = 0 for small polymers.
  Lemma 11 (eq. 138): ||(BE)_{L^{-1}}||_{k+1,κ} ≤ O(1) L^{-ε} ||E||_{k,κ}. This is the contraction of irrelevant terms.
- **Small-field effective-action theorem, Theorem 14 (p.23, eqs. 176-182).**
  - Hypothesis: ρ_k(Φ_k) = Z_k exp(-S_k(Φ_k, φ_k) - V_k(φ_k) + E_k(φ_k)) on S_k, with E_k = Σ_X E_k(X), normalised, and
    |μ_k| ≤ λ_k^{1/2}, ||E_k||_{k,κ} ≤ 1 (eq. 179).
  - Conclusion: ρ_{k+1} has the same form on S_{k+1}, with the flow (180):
    - ε_{k+1} = L³ε_k + L_1 E_k + ε*_k;
    - μ_{k+1} = L²μ_k + L_2 E_k + μ*_k;
    - λ_{k+1} = Lλ_k;
    - E_{k+1} = L_3 E_k + E*_k.
  - Bounds (181)-(182): ||L_3 E_k|| ≤ O(1) L^{-ε} ||E_k||, and |ε*_k|, ||E*_k|| ≤ O(1) L³ λ_k^{1/4-10ε}.
- **Cluster expansion.**
  - Lemma 21 (p.30, eqs. 236-237): Ξ'_k(φ) = exp(Σ_Y E#_k(Y, φ)), with
    |E#_k(Y)| ≤ O(1) L³ λ_k^{1/4-10ε} e^{-L(κ-5κ_0-5) d_{LM}(Y)}.
  - Theorem 27 (App. B, p.39, eqs. 297-299): if |H(X,Φ)| ≤ H_0 e^{-κ d_M(X)}, with κ > 3κ_0 + 3 and H_0 ≤ c_0, then
    ∫ exp(Σ_X H(X)) dμ = exp(Σ_Y H#(Y)), with |H#(Y)| ≤ O(1) H_0 e^{-(κ-3κ_0-3) d_M(Y)}, for an ultralocal
    probability measure μ.
- **Flow solution, Theorem 24 (p.36, eqs. 283-284).** For λ_K = L^{-Δ}λ small there is a unique sequence (ε_k, μ_k, E_k)
  with |μ_k| ≤ λ_k^{1/2+β}, ||E_k||_{k,κ} ≤ λ_k^β and |ε_k| ≤ O(1) λ_k^β.
- **Not present.** No marginal coupling: λ_k = L^k λ_0 just scales (eq. 106), because the model is super-renormalizable.
  No gauge field.

## 2. J. Dimock, "... II. Large fields", arXiv:1212.5562 (v2; 94 pp.) [read-skim; section 1, section 3.1 and Theorem 3.1 read]
Journal: J. Math. Phys. 54 (2013) 092301 [2204.07201 p.16, read].

- **Large/small split (p.2-3, eqs. 9-12).**
  - Insert 1 = Σ_{Ω_1} ζ(Ω_1^c, Φ_0) χ(Ω_1, Φ_0), with conditions (10): |Φ_1 - QΦ_0| ≤ p_0, |∂Φ_0| ≤ p_0 and
    |Φ_0| ≤ λ_0^{-1/4} p_0.
  - "In a cube □ ⊂ Ω_1^c at least one of exp(-a/2L²||Φ_1 - QΦ_0||²_□) or exp(-S_0(□,Φ_0)) or exp(-V_0(□,Φ_0)) is bounded
    by e^{-O(1)p_0²}", which gives e^{-O(1)p_0²|Ω_1^c|_M} (p.3).
  - At step k the thresholds are p_k = (-log λ_k)^p, and the regions are nested: Ω_1 ⊃ Ω_2 ⊃ ... ⊃ Ω_k.
- **Region separation (p.20, eqs. 147-148).** Pairs Π_j = (Ω_j, Λ_j), decreasing as in (145), with
  d((Λ̄_{j-1})^c, Ω_j) ≥ 5[r_j] L^{-(k-j)}M and r_k = (-log λ_k)^r.
- **Main representation, Theorem 3.1 (p.29-31, eqs. 201-222).** ρ_k is a sum over histories Π of integrals over the
  large-field variables. Each term contains:
  - the bare action S⁺_k(Λ_k) on the current small-field region;
  - E_k(Λ_k) = Σ_{X⊂Λ_k} E_k(X), with |E_k(X)| ≤ λ_k^β e^{-κ d_M(X)} (212), "identical with the global small field
    functions of part I";
  - a tiny remainder R_{k,Π}, with |R(X)| ≤ λ_k^{n_0} e^{-κ d_M(X)} (214);
  - active boundary terms B, with |B(X)| ≤ B_0 λ_k^β e^{-κ d_M(X, mod Ω_k^c)} (217);
  - inactive boundary terms B̃ ≤ B_0 |Λ_{k-1} - Λ_k| (218);
  - unrenormalised actions S^{+,u} on δΛ_{k-1} (220);
  - characteristic functions C_{k,Π} and χ_k(Λ_k) (206-208).
- **Remark 3 (p.31), load-bearing for L5.** "in Balaban's models these R_k terms get additional contributions from a
  recycling operation that converts some large field contributions back to small field contributions (the 'R -
  operation'). This difficult step is not necessary for this model." **So the R-operation is NOT treated in Dimock
  I-III.**

## 3. J. Dimock, "... III. Convergence", arXiv:1304.0705 (v1; 37 pp.) [read-skim; Theorem 1, section 4 Lemmas 11-13, Theorem 2, Corollary 1 and Lemma 20 read]
Journal: Ann. Henri Poincaré 15 (2014) 2133-2175 [2204.07201 p.16, read].

- **Theorem 1 (p.3-4, eqs. 14-27).** Restates II's representation, with |E_k(X)| ≤ λ_k^β e^{-κ d_M(X)} for
  β < 1/4 - 10ε (20).
- **Large-field small factors.**
  - **Lemma 11 (p.23, eq. 155):**
    exp(-¼ a L^{-(N-j-1)} |Φ_{j+1} - QΦ_j|²_{P_{j+1}}) ζ^q(P_{j+1}) ≤ exp(-¼ a L p_j² M^{-3} |P_{j+1}|).
    Proof (eqs. 156-158): ζ forces one point per LM-cube with |Φ_{j+1} - QΦ_j| ≥ p_j.
  - **Lemma 12 (p.23-24, eq. 160):** the same for the fluctuation fields W_j, with p_{0,j}.
  - **Lemma 13 (p.24, eq. 166):**
    exp(-S^{+,u}_j(Λ_{j-1} - Λ_j)) ζ_j(Q_j) ≤ exp(C λ_j^β |δΛ_{j-1}| - c_2 p_j² M^{-3} |Q_j|).
    Here the large-field factor is extracted from that level's own effective action.
  - Proof of Lemma 13 (p.25): if |∂Φ_j| ≤ c_1 p_j and |Φ_j| ≤ c_1 α_j^{-1} p_j on □^{∼R_1}, then the smeared-field
    bounds (174) hold and ζ_j(□) = 0. Otherwise Lemma 20 converts the action into a lower bound on the fundamental
    fields.
- **Lemma 20 (p.35, eq. 246; attributed to Balaban [4] = CMP 89, 571-597).** With Neumann boundary conditions on a union
  X of unit blocks:
  ½||Φ - Q_k φ||²_X + ½||∂φ||²_X + ½μ||φ||²_X ≥ c_0 (||∂Φ||²_X + μ||Φ||²_X), with c_0 = O(1).
  This is the fine-action ≥ coarse-action inequality.
- **Theorem 2 (p.33, eqs. 221-222).** Z_{M,N} = Z_{M,N}(0) exp(Σ_X H(X)), with |H(X)| ≤ O(1) λ^{β/2} e^{-κ_0 d_M(X)}.
- **Corollary 1, stability (p.33, eq. 225).** exp(-λ^η Vol(T_M)) ≤ Z_{M,N}/Z_{M,N}(0) ≤ exp(λ^η Vol(T_M)), with η
  independent of M and N.
- **Correlation functions: not proven.** "The analysis can be adapted to treat correlation functions as well" (p.33).

## 4. J. Dimock, "Ultraviolet Stability for QED in d=3", arXiv:2009.01156 (v2, 27 Jul 2021; 78 pp.) [read-skim; sections 1-2, section 4.2.2 Lemma 23 and Lemma 19 read]
Journal: none listed on arXiv; "to appear in Annales Henri Poincaré" per 2204.07201 p.16.

- **Model (p.1, eq. 1).**
  - The torus T^{-N}_0 = (L^{-N}Z/Z)³ has **unit volume**, and the main result is "in a fixed finite volume" (abstract).
  - Abelian gauge field A on bonds, Wilson fermions. Coupling e_k = L^{-(N-k)/2} e, so it grows exponentially
    (super-renormalizable).
- **RG step (p.2, eq. 4).** δ(A_{k+1} - QA_k) δ(τA_k): **axial gauge fixing in each L-block**, with Landau-gauge
  minimisers used for the estimates.
- **Flow, Proposition 1 (p.6, eqs. 29-30).** Unique solution of the flow with ε_K = m_K = 0 and E_0 = 0, satisfying
  |ε_k| ≤ 2e_k^{1/4-7ε}, |m_k| ≤ e_k^{3/4-8ε} and ||E_k(X,A)||_{h_k} ≤ e_k^{1/4-7ε} e^{-κ d_M(X)}.
- **Theorem 1 (p.7-8, eqs. 37-40).** The density after k steps has the history-sum form (6), with gauge-invariant,
  analytic polymers E_k (38) and boundary terms (40).
- **Dimensionless small-field conditions (p.8, eq. 41).** |dA_{j'}| ≤ L^{(3/2)(k-j')} p_{j'}: in fine units the allowed
  field strength grows like L^{(3/2)(k-j')}. That is the d = 3 gauge scaling; in d = 4 it would be L^{2(k-j)}
  [inference, not read].
- **Theorem 2, stability (p.8, eq. 42).** "Let the coupling constant e be sufficiently small. Then for all N:
  1/2 ≤ |Z(N,e)/Z(N,0)| ≤ 3/2."
- **Gauge large-field factors, Lemma 23 (p.64, eq. 471).**
  - ζ⁰_{k+1}(P_{k+1}) ≤ exp(-p_{k+1}(Mr_{k+1})^{-3}|P| + CM² p_{k+1}^{-1} ||dA_k||²_{(Λ_k - Ω_{k+1})^{2♮}}), and three
    similar bounds.
  - Mechanism (p.64-65, eqs. 473-479):
    - one-step regularity, |dA⁰_{k+1}| ≤ CM ||dA_k||_{∞, □^{∼3}} (478), comes from Theorem 1 of 1712.10029;
    - so ζ⁰ = 1 forces |dA_k| ≥ (CM)^{-1} p_{k+1} somewhere nearby;
    - the cost is charged to that level's action ½||dA_k||², via ζ ≤ exp(-p + (CM)² p^{-1} ||dA_k||²) (479).
  - **The sup bound is used across ONE step only (constant CM). It is never iterated over levels; each level re-seeds
    from its own action.**
- **No R-operation.** The only "recycles" occurrences (p.53, after eq. 404) refer to the flow equations.

## 5. J. Dimock, "Multiscale block averaging for QED in d=3", arXiv:1712.10029 (v3; 53 pp.) [read-skim; section 3.9 Theorem 1 read]
Journal: J. Math. Phys. 61 (2020) 032302 [2009.01156 ref. 31, read].

- **Theorem 1, regularity (p.43, eq. 327).** For a restricted orbit minimising ||dA||² with multiscale averages fixed,
  on an L^{-(k-j)}M cube in δΩ_j any A in the orbit is gauge equivalent to an A' with
  L^{-(k-j)/2}|A'|, L^{-3(k-j)/2}|∂A'|, ... ≤ C_0 M p_j sup_{j'} L^{-3(k-j')/2} p_{j'}^{-1} sup_p |dA_{j'}(p)|.
- Dimock states (p.43): "We more or less follow an intricate strategy developed by Balaban in [8], [11]. The following are
  abelian versions of non-abelian results in these references." Here [8] = CMP 99 (1985) 75-102 and [11] = CMP 102
  (1985) 277-309.

## 6. J. Dimock, "Ultraviolet regularity for QED in d=3", arXiv:1512.04373 (v3; 89 pp.) [read-skim; Lemmas 6, 9, 11 read]
Journal: J. Math. Phys. 59 (2018) 012301 [2009.01156 ref. 30, read].

- **Lemma 6 (p.24, eqs. 194-195), Landau-gauge Green's function G_k.** It has a random-walk expansion on M-blocks,
  |G_k f|, |∂G_k f|, ||δ_α ∂G_k f||_∞ ≤ C||f||_∞, and local decay Ce^{-γ d(y,y')}. "We sketch the proof." Sources:
  CMP 95, 96, 99 (389-434).
- **Lemma 9 (p.29, eqs. 237-238), minimiser H_k.** The same bounds. Sources: CMP 95, 96, 99.
- **Lemma 11 (p.31, eqs. 249-250), fluctuation covariance C_k and C_k^{1/2}.** |C_k(Υ,Υ')| ≤ Ce^{-γ d}. Sources: CMP 96,
  99, 116.
- **These propagator bounds are themselves imported from Balaban in Dimock's abelian work.**

## 7. J. Dimock, "Stability for QED in d=3: an overview", arXiv:2204.07201 (16 pp.) [read in full]
Expanded ICMP 2021 talk.

- **Theorem 1 (p.2).** K₋ ≤ Z_N(e)/Z_N(0) ≤ K₊.
  - "The method works equally well for any finite volume, not just unit volume. But the infinite volume limit would pose
    new difficulties" (p.2-3).
- **Large-field mechanism in its simplest form (p.4-5, eqs. 14-19).**
  - χ_0(□) = χ(sup_{p∈□}|dA_0(p)| ≤ p(e_0)), with p(e_0) = (-log e_0)^p.
  - ζ_0(□) e^{-¼||dA_0||²_□} ≤ e^{-¼ p(e_0)²} (17).
  - Σ_Ω e^{-¼p²|Ω^c|_M} ≤ exp(e^{-¼p²}|T|_M) (19).
- **Free-gauge splitting (p.6, eqs. 22-23).** ½||dA_0||² = ½||dA^{min}_0||² + ½||dZ_0||². The Gaussian dμ_{C_0} sits on
  {QZ_0 = 0, Z_0 axial}, where ||dZ_0||² ≥ const ||Z_0||².
- **Cluster expansion with ultralocal measures (p.9, eqs. 42-44).** Random-walk expansions restore locality.
- **Theorem 2 (p.14, eq. 73).** Flow solution with |ε_k| ≤ e_k^{1/4}, |m_k| ≤ e_k^{3/4} and
  ||E_k(X)||_{h_k} ≤ e_k^{1/4} e^{-κ d_M(X)}.
- **Journal data for Dimock I-III (p.16)**, used above.
- **Balaban's Yang-Mills series, as cited (p.15-16):** CMP 95:17-40; 96:223-250; 98:17-51; 99:389-434; 102:255-275 (3D
  pure gauge UV stability); 102:277-309; 109:249-301; 116:1-22; 119:243-285.
  - The large-field papers CMP 122:175-202 and 122:355-392 are listed in Dimock I (p.51, refs. 15-16), as are CMP
    99:75-102 (1712.10029 ref. 8) and CMP 89:571-597.

## 8. Not read
- **Balaban's CMP papers: every body [not-read].** The 4D YM statements remain [unverified-exact-statement]. Title note:
  Dimock cites CMP 98 as "Averaging operators for lattice gauge field theories"; PROOF.md had "operations". Unresolved.
- **J. Imbrie, "Renormalization group methods in gauge field theories"** (Les Houches 1984 proceedings, North-Holland
  1986) [not-read]. It is a likely open-ish exposition, but no free copy was found.
- **S. Chatterjee, "Yang-Mills for probabilists", arXiv:1803.01950:** abstract only [read via the arXiv API]. A survey,
  not used.
- **A web search (2026-10-26) found no modern open exposition of Balaban's 4D YM proof.** A search-engine summary claimed
  Dimock's papers express doubt about the 4D completeness. I did NOT find such a sentence in the text I read, so the
  claim is unverified and must not be cited.

---

# Session 6 (2026-10-27): Balaban CMP 109 read; open-source search for the large-field results

## 9. T. Balaban, "Renormalization group approach to lattice gauge field theories I. Generation of effective actions in a small field approximation and a coupling constant renormalization in four dimensions", Commun. Math. Phys. 109 (1987) 249-301 [read: the whole paper, pp. 249-301]
Source: owner-supplied PDF `balaban_cmp109_249-301_1987.pdf` (scanned) and its text extraction `balaban_cmp109_text.txt`.
The text extraction garbles many displayed formulas. Equations (0.1), (0.4)-(0.19), (0.27)-(0.31), (1.1)-(1.4) and
(2.4)-(2.9) were read from page images (PDF pages 3, 5, 6, 7, 10, 11, 12, 18, extracted with pypdf+Pillow into the
scratchpad). Other equations are transcribed from the text extraction and are marked [txt] where a symbol could be
misread. "p." = printed page. Received 23 Sept 1985, revised 31 Mar 1986; communicated by A. Jaffe (p.301).

### 9.1 Scope, in Balaban's words
- Abstract (p.249): "The analysis is restricted to small field approximation." Effective actions are built "by cluster
  expansions in one step renormalization transformations", with β-functions and "a coupling constant renormalization
  by a recursive system of renormalization group equations".
- p.250: "We study the renormalization transformations under the simplifying assumption that integrals are restricted
  to small fields." **CMP 109 contains no large-field estimate.**
- p.250: the technical core is taken from the earlier series [7-16]; their results "are valid in four-dimensional
  theories (in fact they are dimension-independent)".
- p.251: "The analysis of the Callan-Symanzik equations, based on perturbative calculations, will be discussed in
  another paper."
- G is any compact semisimple Lie group with G ⊂ U(N), and the trace is normalised, tr 1 = 1 (p.251-252). d = 4 is
  the main case, and the proof "also covers the dimension d = 3" (p.259).

### 9.2 Geometry and the averaging (pp. 251-254)
- (0.1), p.251: T_ε = {x ∈ εZ^d + Σ_μ ½ε e_μ : -L_μ < x_μ < L_μ}, with ε = L^{-K}, L_μ = L^m, and **"L is an odd,
  positive integer > 11"** (page image). The coarse tori T^{(k)}_{L^kε} are the same with ε → L^kε. The action is
  (0.2) A^ε(U) = Σ_p ε^{d-4}[1 - Re tr U(∂p)].
- Contours (p.252): G(y,x) is the family of shortest axial contours from the block centre y to x ∈ B(y). There is one
  contour for each permutation of the coordinate directions in which x - y is nonzero, with |n_μ| ≤ (L-1)/2. [x,x'] is
  the parallel transport of the coarse bond c to x.
- **Link average (0.4), p.253 (page image):**
  Ū(c) = M(U,c) = exp[ i Σ_{x∈B(c_-)} L^{-d} Σ_{Γ∈G(c_-,x)} |G(c_-,x)|^{-1} Σ_{Γ'∈G(c_+,x')} |G(c_+,x')|^{-1}
  (1/i) log U(Γ ∪ [x,x'] ∪ (-Γ') ∪ (-c)) ] U(c).
- Group averages, axioms (0.5)-(0.9), p.253: M({U_j^{-1}}) = M({U_j})^{-1}; M({uU_jv}) = uM({U_j})v; M is permutation
  invariant; (1/i) log M({exp iA_j}) = n^{-1}Σ A_j + (higher order); M maps G to G. Federbush's definition is the
  solution U of (0.10), Σ_j (1/i) log(U_j U^{-1}) = 0, "as it was proved by Federbush in [35 (II)]". The averaged
  contour variable is (0.11) U(y,x) = M({U(Γ)}_{Γ∈G(y,x)}).
- Second average (0.12), p.254: Ū(c) = exp[i Σ_{x∈B(c_-)} L^{-d} (1/i) log U(c_-,x) U([x,x']) U(x',c_+) U(-c)] U(c).
  "all results of the paper [12] are valid for it ... both definitions are equally good for our purposes, in fact we may
  use many other definitions" (p.254). There is no axiomatisation of link averages ("not interesting enough", p.254).
- **Comparison with our S4' (check c17(B)).** In (0.4) the two contour families are averaged *independently*; S4'
  uses the same coordinate order at both ends. With the same pairing, (0.4) equals S4' exactly, because
  exp(avg log(T S^{-1})) S = S exp(avg log(S^{-1}T)) (conjugation by S; c17(B): error 4e-16 in d = 3 and 6e-16 in d = 4).
  With independent pairing the two maps agree at linear order and differ at second order (c17(B): the difference
  scales by 3.96 when the amplitude is doubled).

### 9.3 The renormalisation transformation and the gauge fixing (pp. 254-256)
- (0.13): (Tρ)(V) = ∫ dU t(V,U) ρ(U).
- Small-field restriction (p.254): ρ and the integral are restricted to "regular configurations U, i.e. configurations
  satisfying bounds |U(∂p) - 1| < ε_0, p ∈ T, with ε_0 positive and sufficiently small".
- Exponential gauge fixing (0.14), p.254: exp[-(1/2α)|U(y,x) - 1|²] = exp[-(1/α)[1 - Re tr U(y,x)]]. This is
  Euclidean-invariant, unlike the δ-function axial gauge of [9,16]. It is introduced via the Faddeev-Popov identity
  (0.15)-(0.16), together with χ({|U(y,x) - 1| < ε_0}).
- **(0.17), p.255 (page image):**
  A_1(V) = (T_0 A)(V) = log N_0^{-1} ∫ dU Π_{c∈T^{(1)}} δ(Ū(c)V^{-1}(c)) χ_0
  exp[-(1/g_0²) Σ_{y∈T^{(1)}} Σ_{x∈B(y),x≠y} [1 - Re tr U(y,x)] - (1/g_0²) A(U)].
  So α = g_0², and the block constraint is a **δ-function**, not a heat kernel.
- (0.19): the same at step k, with g_k and A_k(g_k, U).
- **Coupling recursion (0.18), (0.20), p.255-256:** 1/g_0² = 1/g_1² + β_1(g_0), and 1/g_k² = 1/g_{k+1}² + β_{k+1}(g_k).
  Here k counts coarse-graining steps from the finest lattice. "(d/ds)(1/g²) = -β(g)" (p.255). With β > 0 the coupling
  grows toward the infrared. This confirms the sign convention of PROOF.md L4c [R1-fix], with resolution j = K - k.

### 9.4 Background fields and the effective-action form (pp. 256-264)
- Background (0.21), p.256: U_k(V) minimises U → A^η(U) on {U : Ū^k = M^k(U) = V}. "In [15] it was proved that in a
  space of regular orbits there exists exactly one critical orbit, which is a set of minima".
- (0.22): A_k(g_k,V) = A_k(g_k,U_k(V)) = -(1/g_k²) A^η(U_k(V)) + E_k(U_k(V)).
- (0.23): E_k = Σ_{j=1}^k [-β_j(g_{j-1}) A^η(U_k) + E^{(j)}(U_k)].
- Localisation assumption (0.24)-(0.25), p.257: E^{(j)}(U) = Σ_{X∈D_j} E^{(j)}(X,U), with the terms analytic and gauge
  invariant, depending on U|_X, and |E^{(j)}(X,U)| ≤ E_0 exp(-κ d_j(X)). Here D_j is the class of connected unions of
  M-cubes (M = L^m) at scale j, and d_j(X) is the shortest-tree length divided by M.
- **Renormalised form (0.28)-(0.29), p.258 (page image):**
  -β_j(g_{j-1}) A^η(U_k) + E^{(j)}(U_k) = Σ_{X∈D_j} V^{(j)}(X,U_k), with
  |V^{(j)}(X,U_k)| ≤ O(1)(L^jη)^{4+α} exp(-κ d_j(X)), α > 0.
  (0.30) then gives |E_k(U_k)| ≤ O(1)(1 - L^{-α})^{-1} M^{-4} |T_1^{(k)}|, i.e. bulk dependence only, uniformly in k.
  "This is the essence of the ultraviolet stability concept" (p.259).
- The mechanism (p.258): if X is not inside one cube, (0.25) gives exp(-κ(L^jη)^{-1}). Otherwise use local coordinates
  U_k = exp iηH (Sect. F [15]), expand E^{(j)}(X, exp iηH) to fifth order in H, bound the fifth-order term by
  E_0 O((L^jη)^5) e^{-κd_j}, and use the Ward-Takahashi identities to extract β A^η from the lower orders.
- **Small-field domains (p.259, page image):** "For the k-th action such a domain is determined by the condition
  |∂U_k(V) - 1| < ε_0η² on T_η, for ε_0 sufficiently small. Another possible definition, technically less convenient, is
  given by the condition |∂V - 1| < ε_0 on T_1^{(k)}." Here η = L^{-k} is the fine spacing in units of the current
  coarse lattice.
- **Theorem 1 (p.259, page image):** "If the sequence of the effective coupling constants is contained in an interval
  ]0,γ] with a sufficiently small positive γ, then the effective actions for small fields are given by the formulas
  (0.22)-(0.24), with terms satisfying (0.29)." No asymptotic freedom is assumed.
- **Theorem 2 (p.259, page image):** d = 4 and G = SU(2). For γ small and g small "there exists a bare coupling constant
  g_0 = g_0(ε,g) such that the sequence of the effective coupling constants g_k is contained in the interval ]0,γ],
  and g_K = g." There are constants 0 < β ≤ β' with
  (0.31) 1/g² + β log(L^kε)^{-1} ≤ 1/g_k² ≤ 1/g² + β' log(L^kε)^{-1}.
  **"A proof of this theorem, based on perturbative calculations, will be given in a separate paper"** (p.259-260).
  The SU(2) restriction "is superficial" (p.260). Note that log(L^kε)^{-1} = (K - k) log L.
- **Section 1 (p.260, page image).** Background regularity: |V(∂p') - 1| < ε_0' on T_1^{(k)} gives exactly one regular
  critical orbit (Theorem 1 [15]). U_k(ε_0) is (1.2):
  |U(∂p) - 1| < ε_0η², η = L^{-k}, and |J| < ε_0 with J = D*_U η^{-2} π Im ∂U.
  "By Proposition 2 [12] this condition implies that |V(∂p') - 1| < 2ε_0 for p' ∈ T_1^{(k)}, and is implied by the
  condition on V, with 2ε_0 replaced by B_3^{-1}ε_0, see Theorem 1 [15]."
- (1.3): A_k(U_k) = -(1/g_k²)A(U_k) + Σ_{j=0}^{k-1} {-β_{j+1}(g_j)A(U_k) + [log Z^{(j)}(U_k) - log Z^{(j)}(1)]
  + [E^{(j+1)}(g_j,U_k) - E^{(j+1)}(g_j,1)]}.
  (1.4): Z^{(j)}(U_k) = ∫ dB δ(Q̃B) exp[-½⟨B, Δ^{(j)}(U_k)B⟩]. The operators H_{1,j}, Δ_1 are "defined in Sect. D
  [13]".
- (1.7)-(1.9) [txt]: E^{(j)} = Σ_{X∈D_j} E^{(j)}(X), extended to analytic functions E^{(j)}(X, g_{j-1}, U, J) of two
  variables. U obeys first-order regularity; J replaces the second-order quantity (1.8), D*η^{-2}π Im ∂U.
- **Spaces U^c_j(X, α_0, α_1, γ_0) (p.262).** Unions of orbits of complexified gauge transformations (1.10) of pairs
  (U,J) with:
  - (i) U = U'U_r, U_r ∈ G, |∂U_r - 1| < α_0ξ² on X (1.11), and on each O(1)LM-cube a G-gauge in which
    U_r = exp iξA with |A|, |∇_ξA| < O(1)LMB α_0 (1.12);
  - (ii) U' = exp iξA', |A'|, |∇_ξA'| < α_1 (1.13);
  - (iii) |∂U - 1| < α_0ξ², |J| < γ_0 (1.14);
  - (iv) the multiscale backgrounds U_n(M'(U)) built on the maximal sequences {Ω_n} of [14] (conditions (1.3)-(1.6)
    [14]) obey (1.16) on X^{-2}.
  Minimal configurations with |∂U_j - 1| < ε_0ξ², ε_0 small, lie in these spaces (p.263, via Proposition 9 [15]).
- Inductive bound (1.18), p.263: |E^{(j)}(X, g_{j-1}, U, J)| ≤ E_0 exp(-κ d_j(X)) "for M ≥ M(κ), γ sufficiently small",
  for all (U,J) ∈ U^c_j(X, α_0, α_1). There is **no positive power of the coupling** in (1.18).
- Symmetry: gauge invariance (1.19) and lattice Euclidean invariance (p.263).
- **β-function (1.20)-(1.22), p.264 [txt].** Π_{j+1,μν} is the second derivative of E^{(j+1)}(g_j, U_{j+1}(exp iB)) at
  B = 0. It is δ_ab times a real function by G-invariance (1.21), and Euclidean covariant. After the limit
  T^{(j+1)} → Z^d, β_{j+1}(g_j) = -(∂²/∂p_μ∂p_ν)Π̂_{j+1,μν}(g_j,0) = Σ_x Π_{j+1,μν}(g_j,x) x_μ x_ν, for μ ≠ ν (1.22).
  It is "smooth ... uniformly bounded on this interval together with all derivatives. We will investigate other
  properties in a separate paper."
- **Theorem 3 (p.264)**, the precise form of Theorem 1: "There exist positive constants κ_0, M(κ), γ, ε_0, ε_1, α_0,
  α_1 such, that if κ ≥ κ_0, M ≥ M(κ), 0 < g_k ≤ γ for k = 0,1,...,K, then the sequence of actions A_k, defined
  inductively by the small field renormalization transformations (0.17)-(0.20), satisfy all the inductive assumptions
  described between (1.1)-(1.22)."

### 9.5 One RG step: the fluctuation integral (Sects. 2-3, pp. 265-281)
- (2.1)-(2.3): the critical point of V → G(V) + A(U_k(V)) on {V̄ = W} is V^{(k)} = U^{k}_{k+1}, in the axial gauge
  G(V) = 0. The fluctuation is V = V'V^{(k)}, B' = (1/i) log V'.
- Axial → Landau: the gauge transformation u_k "constructed in [14]" gives U_k u_k^{-1} = exp iηH_k(B'), analytic in B'
  for |H_k| < α_1 (p.265-266; formula (106) [12]).
- (2.5): G(B') = Σ ½|B̃'(y,x)|² + G_3(B'). (2.6)-(2.8) is the expansion of the action, using (41), (174), (171) [15]:
  A(U_k(V'V^{(k)})) = A(U_{k+1}) + ⟨H_1B', J⟩ + ½⟨H_1B', Δ_1H_1B'⟩ + V(H_1B').
- **Fluctuation small-field restriction (2.9), p.266 (page image):** χ_k = Π_{b∈T^{(k)}\{b_0(c)}} χ({|B'(b)| < ε_1}).
  "Another possibility is to take g_k/γ_k ε_1 instead of ε_1, where γ_k = C log(L^kε)^{-1} with C sufficiently large."
  After the scaling B' = g_kB (p.267), the fixed-ε_1 choice allows Gaussian-normalised fluctuations up to ε_1/g_k.
- The δ(Q̃B') constraint is linearised by B' = B - hD(B) (p.267). Then (2.12)-(2.13):
  E^{(k+1)}(g_k, U_{k+1}) = log ∫ dμ_{C^{(k)}}(B) χ_k exp[P^{(k)} + {...}], with C^{(k)} = (C*Δ^{(k)}C)^{-1} (p.268).
  (2.15) is the coupling renormalisation.
- Sect. 3: analytic extensions (3.1)-(3.17), Lemma 4 (3.53), p.280, and the fifth-order Taylor remainder bound
  (3.34)-(3.35). These use the exponential decay of δH/δB (rate δ_0, "Proposition 9, (190) [15]"), the formulas
  (1.43)-(1.54) [14], and (97), (77), (106) [12].

### 9.6 Ward-Takahashi identities and the β-function (Sects. 4-5, pp. 281-298)
- (4.9): the Ward identity from gauge invariance, as in (2.23)-(2.28) [7]. Consequences: (4.14) (δ/δB)E(1) = 0 (G
  semisimple), and the hierarchy (4.15).
- (4.17)-(4.18): bounds on derivatives of the localised field B, |∂B| < α_1(L^jη)², from Proposition 5 [7].
- (4.34): reduction of the renormalisation-relevant part to E^{(2)}, which is resummed into the vacuum polarisation
  tensor Π (4.37).
- (4.40)-(4.45): the counterterm β_j(g_{j-1})(A(U_j exp iB^{(k)}) - A(U_k(V^{(k)}))) produces the same local terms with
  Δ_j from (1.66) [10]. They cancel against the Π terms once β_j is defined as the coefficient in (5.37).
- **Sect. 5.** Π is translation invariant, permutation and reflection covariant (5.6)-(5.8), transverse (5.9),
  exponentially decaying (5.10), hence analytic in a strip (p.293). Laurent decomposition (5.17)-(5.36), then
  (5.37): Π̂_μν(p) = β(δ_μν Δ(p) - d̄_μ(p)d_ν(p)) + Π'_μν(p), with Π' a third-order polynomial in d, d̄ with analytic
  coefficients (5.38). β is fixed by (5.41)-(5.42) [txt], "the fundamental equality defining the β-function".
  **Re-derived independently in PROOF.md, Lemma L4a-Π, check c17(A).**
- **Deferral of the localisation (p.298):** "the terms of the transformed action ... are still nonlocal in the
  fluctuation and the background field ... In the next paper we will construct such localizations and prove the bounds.
  They are used to construct a cluster expansion of the integral in (2.13), and to finish the proof of the inductive
  assumptions for the term E^{(k+1)} defined by (2.13)." **So CMP 109 does not complete the proof of Theorem 3.** By
  Crossref metadata (2026-10-27) the next paper is CMP 116 (1988) 1-22, subtitle "II. Cluster expansions" [v-crossref;
  body not-read].

### 9.7 Every place CMP 109 defers to another paper, and what it says each supplies
Reference numbers are CMP 109's own; journal data are from its list (pp. 298-301).
- **[12] = CMP 98 (1985) 17-51, "Averaging operations for lattice gauge theories"** (this is the printed title in
  CMP 109's list; Dimock prints "operators"):
  - the earlier, non-Euclidean-symmetric average (p.252);
  - "all results of the paper [12] are valid" for (0.4) and (0.12) (p.254);
  - **Proposition 2**: (1.2) ⇒ |V(∂p') - 1| < 2ε_0 (p.260, 265);
  - (106) the Landau-gauge transformation (p.265); (97) (p.270, 278); (77) contour variables (p.275); (32)-(41) gauge
    expansions (p.283).
- **[13] = CMP 99 (1985) 389-434, "Propagators for lattice gauge theories in a background field":**
  - Sect. D, the operators H_{1,j} and Δ_1 (p.261);
  - (3.35)-(3.38), regular complex configurations, analyticity of the explicit terms (p.261);
  - (3.127)-(3.128) and (3.156), the quadratic form Δ^{(k)} (p.266-267).
- **[14] = CMP 99 (1985) 75-102, "Spaces of regular gauge field configurations on a lattice and gauge fixing
  conditions":**
  - the spaces U_k(ε_0) (with [15], p.260);
  - (1.3)-(1.6), the maximal sequences {Ω_n}, and (1.5), M^p (p.262);
  - (1.7)-(1.10), the regularity conditions (p.261);
  - the axial → Landau gauge transformation u_k (p.265); Sect. E (p.267); (1.43)-(1.54) expansions (p.272, 279);
    (1.9) (p.272).
- **[15] = CMP 102 (1985) 277-309, "The variational problem and background fields in renormalization group method for
  lattice gauge theories":**
  - Theorem 1, existence and uniqueness of the regular minimal orbit (p.256, 260);
  - Sect. F, local coordinates U_k = exp iηH (p.258, 275); Sect. G, the multiscale minimisers (p.265, 270, 282);
  - Proposition 9 and (190), exponential decay of δH/δB with rate δ_0, and the bounds on U_n(M'(U)) (p.263, 271);
  - (41), (171), (174), (179), (180), (2): the action expansion and the Landau-gauge representation (pp. 266-277);
  - Sect. C (p.267).
- **[16] = CMP 102 (1985) 255-275, 3D UV stability:** the representation (41), (47); the background fields "are the
  same as in [16]"; the expansion of log Z^{(j)} (p.256, 260, 261).
- **[10] = CMP 95 (1984) 17-40:** the formula (1.66) for Δ_j and the momentum notation (1.29)-(1.37) (p.291).
- **[11] = CMP 96 (1984) 223-250:** cited only within the ranges [4-16] and [7-16] (p.249-250). No specific use.
- **[7] = CMP 89 (1983) 411-445, (Higgs)_{2,3} III:** the method of Sects. 3-5, namely the Ward identities (2.23)-(2.28),
  (3.25)-(3.32), the lattice Taylor formula (3.10), and **Proposition 5** on functional derivatives of averaging
  operations (pp. 250, 258, 283, 285-288).
- **[8] = CMP 89 (1983) 571-597** (regularity and decay of lattice Green's functions): listed only. No specific use.
- **[35] Federbush,** "A phase cell approach to Yang-Mills theory I, II" (University of Michigan preprints): the group
  average (0.10) and its properties (p.253).
- **[43] Gawędzki-Kupiainen CMP 99 (1985) 197-252:** the Laurent-series device of Sect. 5 (p.294).
- **Forward deferrals:**
  - the localisation and cluster expansion of (2.13) go to "the next paper" (p.298);
  - Theorem 2 and the perturbative analysis of the Callan-Symanzik equations go to "a separate paper" (p.251, 259-260);
  - further properties of β_j go to "a separate paper" (p.264).
- **CMP 116, 119 and 122 are not cited** (they appeared later). CMP 109 never mentions large-field regions beyond the
  restriction itself.

### 9.8 What CMP 109 establishes, and what it does not
- **Establishes, with proofs in the paper:**
  - the Euclidean-invariant averaging and gauge fixing;
  - the exact inductive form of the small-field effective actions;
  - the reduction of one RG step to the fluctuation integral (2.13);
  - the analytic extensions and the fifth-order remainder bounds (Lemma 4);
  - the Ward-identity reduction of the marginal part to the polarisation tensor;
  - the symmetry analysis defining β_j.
- **Does not establish:**
  - the localisation and bounds of (2.13), i.e. the inductive step of Theorem 3 (deferred to CMP 116);
  - the coupling flow, Theorem 2 / (0.31) (deferred). In particular, **no statement β_j → 2b_0 log L appears in CMP
    109**;
  - any large-field estimate;
  - anything about the earlier papers' results, which are cited, not reproved.

## 10. Open-access search for the large-field / R-operation results (2026-10-27)
- **Balaban CMP 122 (1989) 175-202 and 355-392.**
  - Crossref [v-crossref]: titles "Large field renormalization. I. The basic step of the R operation" and "... II.
    Localization, exponentiation, and bounds for the R operation", issues 2 and 3.
  - OSTI ETDEWEB abstracts [read-abs]:
    - Part I (osti.gov/etdeweb/biblio/6142166): "We construct the renormalization operation of the expressions
      connected with the large field regions." The rest of the record (paraphrased): the operation R removes the main
      obstacle to proving UV stability of four-dimensional gauge theories, and the proof is completed in Part II.
    - Part II (osti.gov/etdeweb/biblio/6481841): "In this paper we conclude the discussion of the basic properties and
      bounds for the R operation", completing "the proof of the ultraviolet stability of four-dimensional pure gauge
      field theories" (the record adds "as formulated in Theorem 1"; which paper's Theorem 1 is not stated).
    - The OSTI record for Part II gives the citation as "120:4, 575-612". Crossref and Springer give 122:355-392. This
      is treated as an OSTI metadata error [unresolved].
  - Bodies [not-read]. Project Euclid served an Incapsula bot-detection page again (2026-10-27); not bypassed.
- **Balaban CMP 116 (1988) 1-22:** Crossref subtitle "II. Cluster expansions" [v-crossref]. Body [not-read].
- **Balaban, Feldman, Knörrer, Trubowitz, "Complex bosonic many-body models: overview of the small field parabolic
  flow", arXiv:1609.00968** [read: pp. 1-4].
  - p.4: "If the actions in our functional integrals were sums of positive terms (as in a Euclidean O(n) model) it
    would be routine to extract an exponentially small factor per point of a large field region."
  - Their models are not positive, and they have no per-point large-field result. This is general context, not a YM
    statement.
- **Dimock, "Lectures on the ultraviolet problem for QED in d=3", Roma Tre 2022**
  (www.nsm.buffalo.edu/~dimock/Rome.final.pdf) [read-skim: pp. 3-4, 38-39, 57-59].
  - p.39, eqs. (224)-(228): ζ_0(□)e^{-¼||dA_0||²_□} ≤ e^{-¼p(e_0)²}, hence e^{-¼p(e_k)²} ≤ c_{n_0} e_k^{n_0}. The sum
    over all levels of the large-field counting terms, Σ_k c_{n_0} e_k^{n_0} |T^0_{N-k}|_M ≤ c M^{-3} Σ_k
    (L^{-(N-k)/2}e)^{n_0} L^{3(N-k)}, "is bounded uniformly in N for n_0 ≥ 7". **The geometric decay of the
    super-renormalisable coupling e_k is what makes the crude count converge.** This is the template whose 4D failure
    is Proposition LF-count in PROOF.md.
  - p.57: restoring the locality of the characteristic functions "is a difficult technical problem", with "no
    analyticity" available.
  - p.59: Theorem 3, 1/2 ≤ |Z(N,e)/Z(N,0)| ≤ 3/2, in unit volume.
  - No R-operation.
- **Jaffe-Witten, Clay problem description** (claymath.org yangmills.pdf) [read: p.11-13]. Balaban's 4D extension
  "includes an analysis of asymptotic freedom to control the renormalization group flow as well as obtaining
  quantitative estimates on effects arising from large values of the gauge field". The citation given is CMP 109
  alone. No statement of the large-field theorem.
- **arXiv API searches** (au:Balaban; abs:"large field" AND Balaban; au:Trubowitz AND au:Knorrer) and web searches:
  - no open exposition of the 4D YM large-field bound or of the R-operation was found;
  - Dimock II p.31 Remark 3 [read, S5] remains the only open description of what the R-operation does;
  - Balaban's later "The large field renormalization operation for classical N-vector models", CMP 198 (1998) 493-534
    [v-crossref; body not-read; not open] is the closest later treatment of the same operation, in a simpler model;
  - Balaban, "Constructive gauge theory" I and II (Plenum proceedings 1986, pp. 207-263, and 1990, pp. 55-68)
    [v-crossref; not-read; not open].

## 11. Session 7 search: 2D testbed for the one-cube R-operation (2026-10-27)
- **Balaban, "The large field renormalization operation for classical N-vector models", CMP 198 (1998) 493-534**
  [read-abs: Rutgers scholarship record]. Abstract: a renormalization operation of the large-field densities is
  constructed, which improves their bounds, proves all inductive hypotheses and "completes the construction and
  analysis of the full renormalization group flow for these models". By the series it belongs to (CMP 167 (1995)
  103-154, "A low temperature expansion for classical N-vector models. I. A renormalization group flow"; II, CMP 182
  (1996); III, CMP 196 (1998)) [search snippets / catalogue entries only], this is the LOW-TEMPERATURE (spin-wave,
  d ≥ 3) problem, an infrared analysis. It is **not** a 2D asymptotically free UV construction. The record does not
  state d; the d ≥ 3 attribution comes from the companion correlation-function paper's catalogue abstract
  ("in d ≥ 3 dimensions, N ≥ 2") [search snippet]. Body [not-read; paywalled].
- **Kopper, "Mass generation in the large N nonlinear σ-model", CMP 202 (1999) 89-126, arXiv:math-ph/9902020**
  [read-skim: abstract and introduction via arXiv HTML]. The introduction says the hard part of the UV analysis of the
  2D model has "so far only [been] performed in the hierarchical case for N>2 and as long as the effective coupling
  stays small" (attributed to Gawędzki-Kupiainen and Pordt-Reiss). The large fields appear only via "a finer splitting
  of the large field configurations before cluster expanding" in his own IR analysis.
- Giuliani-Ott, arXiv:2302.07299 [read-abs]: d ≥ 3 low-temperature O(N), no Balaban large-field content.
- No open-access statement of a 2D large-field R-operation was found. No paywall, sign-in or bot check was crossed.
