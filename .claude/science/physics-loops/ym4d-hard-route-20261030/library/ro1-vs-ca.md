# RO1 versus the complete account: does RO1 give O(4) without (IR-fl)?

Provenance: Claude Opus 5.5 (subagent of the lead), 2026-11-05. Research text, not an audit; grants no status. One reading. Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the complete account (CA) and the outline (SA).

Sources read (bounded ranges, never whole for CA/SA):
- `library/ro1.md` whole (L1–703); `gates/ro1-gate.md` whole; `library/lg1.md` L1–8, L313–330, L365–384, L425–485; `library/cl1.md` L57–170, L275–326, L362–486, L536; `library/sr1.md` L542–568; `library/ph1.md` L579–606; `library/assembly-status.md` rows L28–35.
- CA = `scratchpad/sa/ca_{I,II,III}.tex` (CA-I sha256 `4cb5cb5e…6e93`, equal to RO1's record L675). CA-I L2590–2830, L3020–3160. CA-II L2791–2985. CA-III L75922–76030, L79925–80010, L101415–101440, L108520–108580, L109225–109365, L110784–111060, L111167–111260.
- SA = `scratchpad/sa/ym4.tex` (sha256 `d7f77d4d…4b6f`, equal to RO1 L674). L24478–24492, L31799–31835.

Notation: "CA proves in full" would mean a CA statement with status "proved". CA itself says no clause of Theorem 0 has that status (CA-III L110865: "No clause of Theorem~\ref{3.1:thm-main} is proved outright."). Below, "CA standing" means "proved as an implication" in CA's own sense.

## 1. What RO1 proves, and its inputs

**Statement.** RO1 Theorem 9 (ro1.md L630–641). Conclusion (9.1), L636–641:
"the hierarchy is O(4)-invariant on separated compact \(C^1\) tuples and on its diagonal-flat extension: \(S_n(Rf_1,\ldots,Rf_n)=S_n(f_1,\ldots,f_n)\), \(\Sigma_n(R\phi)=\Sigma_n(\phi)\), \(R\in\mathrm O(4)\)."

**Domain.**
- Limits. "Let \(S\) be a volume-first limit through periodic Gibbs states, or a canonical component of PH1 with its all-state realization" (L630). Volume-first is defined at L18–23: periodic infinite-volume Wilson DLR states \(\rho_j,\nu_j\) "at the same first-passage data, with \(a_j\to0\)", and "The volume limit is already taken at each spacing. This part assumes the realization" (L23). CL1 Lemma 1 (cl1.md L99–113) builds such states as torus-limit points at each fixed cutoff.
- Observables. The plaquette action density \(\mathcal O_a(f)=\sum_pf(x(p))a_p\), \(a_p=1-\tfrac12\operatorname{ReTr}U_p\), SU(2), centered by \(\nu\) (L11–13). This is CA's observable: CA-III L75950–75952 has \(a_p=1-\operatorname{Re}\operatorname{tr}U(\partial p)\) with \(\operatorname{tr}\mathbf 1=1\).
- Points. Separated tuples only: "compact \(C^1\) entries with pairwise disjoint supports" (L16). All orders \(n\). The diagonal-flat extension \(\Sigma_n\) is a second conclusion and needs H-S (L630, L628). No coincident points.

CA clause (vi) asks for the same test class: "all real \(f_i\in C^1_c(\mathbb{R}^4)\) with pairwise disjoint supports" (CA-I L3078–3082), on "every limit \(S^T_{n;\infty}\) of (ii-\(\mathbb{R}^4\))" (L3078–3079).

**Inputs** (ro1.md L52–80; Theorem 9 L630).
- H-U, UV1 full rooted D1 (L54–62): torus source representation, with \(|Z_\ell(W)|/Z_\ell(0)\le\exp\{\Re U_\ell+\Re\sum_{s,X}e_{s,X}+C_{\rm st}\ell^4\}\), domain terms \(|e_{s,X}|\le Ae^{-\kappa m(X)}\), locality in \(X^+\), representation independence, mirror-periodized sources, decay above the rooted entropy rate. L62: "**Outstanding — imported UV1:** this manuscript does not prove this actual source representation". Used only in Lemma 2 (UI), L161–197.
- H-L, LG1 (L64): translation and signed-permutation invariance; RP at coordinate site, coordinate bond and diagonal mirrors, for every periodic state.
- H-C, CL1(2)–(4) (L66): limit symmetries; position-uniform local \(C^1\) bounds; distributions \(T_n\); coordinate and diagonal RP of the limit; coordinate Hilbert spaces; the cube cone \(E\ge0,|q_r|\le E\) (L31: "the round cone is not assumed").
- H-T, TP1(4) / TU10, state-uniform (L68–76): \(0\le S_2^T(f,h)\le u(d)\|f\|_\infty\|h\|_\infty\) on the class \(\mathfrak T(d;\vartheta_*)\), \(\vartheta_*=1/12000\), \(u(d)\to0\). L76: "**Outstanding — imported TU10**". Used in Lemma 5 (L463–475) and through it in Theorem 6.
- H-S, SR1(4) (L78): only for \(\Sigma_n\) (L586: "H-S is needed only in the last paragraph").
- H-P, PH1 (L80): only for components.
- IN1's order of constants (L86–90), as an imported condition.

RO1's own Result (L680): "Neither D1 nor TU10 nor existence of the realizations is discharged here." Status line (L702): "frozen, as a conditional implication". The gate (ro1-gate.md L1, L98–100) found no failing step.

## 2. Each input against the complete account

### 2.0 The domain bridge
CL1 Theorem 9(1) (cl1.md L459): "Every volume-first limit of the connected functions is a limit of SA 0(a)(iii) type." Its proof (L469–485) chooses, at each \(j\), a torus of side \(\ell_j\ge j\) whose cumulants are within \(1/j\) of the torus-limit state \(\rho_j\) (eq. (29)). So each RO1 limit is also a joint-diagonal limit along \((K_j,\ell_j)\). CA (ii-\(\mathbb R^4\)) (CA-I L2690–2704) is stated for such sequences "along one joint diagonal subsequence". Thus RO1's limits are a **subclass** of CA's (ii-\(\mathbb R^4\)) limits: those where the volume grows fast enough at each spacing. CL1 L485 limits this: "It neither identifies an arbitrary periodic DLR state as a torus limit point nor claims the converse for arbitrary growing-torus sequences." SA says the same (ym4.tex L24480–24487): "A direct limit on growing tori ... is a different construction until a separate recognition theorem identifies it with this class. In particular this section does not assign diagonal reflection positivity to an arbitrary growing cubic-torus limit."

Consequence: RO1 cannot give clause (vi) on **every** (ii-\(\mathbb R^4\)) limit. At best it gives it on the volume-first ones.

### 2.1 H-U (UV1, rooted D1)
- CA has no statement in this form. I read the correlation theorem (CA-II L2791–2966, "PROVED" in the index heading scan). It gives the ingredients:
  - (iii), L2919–2936: the sourced densities have "the induction format with sources"; "its terms are analytic in \(w\), a term localised in a domain \(X\) depends on \(w\) only through its restriction to \(X^+\)" (L2925–2926); bounds "of Ba{\l}aban's construction with the enlarged activity constants".
  - (iv), L2937–2957: the torus bound on derivatives of \(\log Z\) at \(z=0\), with volume factor \(\mathsf Q=e^{(E_+^\sharp+C_{\rm low})N^4}\) (L2945).
- It does not state RO1's consumer form: a bound on \(|Z_\ell(W)|/Z_\ell(0)\) for a large (mirror-periodized, whole-torus) complex source, summed over all scales, with rooted-entropy margin and representation independence. Deriving that form is our UV1/D1 task. Our status: `assembly-status.md` L28, UV1 "not started (skeleton: criteria [C]; D1 [O])".
- The correlation theorem itself is conditional. Its own hypotheses include "the statement on the window data of the blocks at the preparatory site, on which the relative bound for the boundary-type terms depends and whose proof is outstanding" (CA-II L2810–2812). Its standing: CA-III L110880–110893, "proved as an implication, by a complete deduction, from Ba{\l}aban's statements as cited ... and from statements of status ``stated; proof incomplete''".
- **Verdict for H-U: open.** Not a CA statement. Not a frozen text of ours. Its raw material is in CA's correlation theorem at CA standing.

### 2.2 H-L (LG1)
- Supplied by our frozen LG1, not by CA. LG1 Theorem 10 (lg1.md L365): "Every periodic Wilson DLR state at \(\beta>0\) is invariant and reflection positive at every admissible mirror (3)". Theorem 13(5) (L431) lists "diagonal lattice mirrors". LG1 Result (L475): "No mathematical step of this assembled fixed-lattice argument is left **Outstanding**." Status L485: "frozen". Its only imports are foundational tools (L462). LG1 L448: "No CA input is needed for LG1."
- CA is consistent with it. CA-III L108556–108557: "The Wilson weight has that positivity on \(\mathbb{Z}^4\)". CA-III L79973–79974: "Diagonal reflection positivity holds for the Wilson weight on \(\mathbb{Z}^4\) and fails on every straight torus". CA does not use it: "This positivity is therefore not asserted for the limits of Theorem~0 and is not used in this book" (L108561–108562).
- CA proves only coordinate RP: lattice RP lemma 6.1:lem-reflection-positivity (CA-II L60440); "reflection positivity of the lattice measure, which is proved (Chapter~\ref{ch:6})" (CA-III L110903–110904).
- **Verdict for H-L: closed, by LG1** (one Claude gate; not supplied by CA).

### 2.3 H-C (CL1(2)–(4))
Split into pieces.
- Compactness and position-uniform bounds. CL1 imports them from SR1 (I3, cl1.md L63–73), which needs D1 (SR1 status L568: "Import UV1 ... remains open"). CA (iii-b) gives a replacement: "independent of \(K\), \(g_0\), \(m\) and the position and non-increasing in \(\mathsf{d}\) (no decay in \(\mathsf{d}\) is asserted)" (CA-I L2610–2625). It holds on tori with \(L^m\ge\ell(n,R,g)\), so it passes to torus-limit states at fixed cutoff. CL1 Lemmas 2, 3, 5 use only a position-independent bound \(M_n(d,R)\) at fixed \((d,R)\) (cl1.md L117–119, L297–299). (iii-b) supplies that. Standing of (iii-b): CA-III L110896–110899, proved as an implication; "the uniformity of the last-scale constants in the torus exponent. The last of these is of status ``stated; proof incomplete''."
- Coordinate RP, \(W_4\), OS Hilbert space, \(H\ge0\), \(\mathbb R^3\) translations. CA (ii-\(\mathbb R^4\)) asserts these (CA-I L2694–2704), for joint-diagonal limits, hence (by 2.0) for RO1's limits. Standing CA-III L110905–110908: "proved as an implication from the per-ball volume-free bound, reflection positivity of the lattice measure and (0)".
- Diagonal RP of the limit. Not in CA. CL1 Lemma 3 (cl1.md L142–170) passes LG1's diagonal positivity to the limit, eq. (8), using only convergence on separated tuples.
- The cube cone \(E\ge\|p\|_\infty\). Not in CA. CA-I L2706–2708 lists as "Not asserted": "the spectrum condition (joint energy--momentum spectrum in the closed forward cone) beyond \(H\ge0\)". CL1 Lemma 8 (cl1.md L416–453) proves the cube cone from the coordinate and the diagonal reflection (Lemma 7, L362–414). It uses "the two-continuum-reflection proof, with no lattice plateau or phase input" (L420).
- **Verdict for H-C:** the CA part is at CA standing; the diagonal and cone parts are from frozen LG1 + CL1 Lemmas 3, 7, 8. CL1 is frozen against SR1's I3, not against CA (iii-b). Re-reading CL1 Lemmas 1–3, 5, 7, 8 with (iii-b) in place of I3 is needed. I checked Lemmas 2, 3, 5 use only fixed-\((d,R)\) position-uniform bounds; I did not re-check CL1 Lemmas 4 and 6 (needed only for \(\Sigma_n\)).

### 2.4 H-T (TU10, state-uniform)
- CA clause (iv) is TU10 on tori. Same test class: "\(\mathfrak{T}(\mathsf{d};\vartheta)\) is the set of pairs of non-negative Lipschitz functions ... \(\int f_i\ge\vartheta\|f_i\|_\infty\mathsf{d}^4\), \(\operatorname{Lip}f_i\le\|f_i\|_\infty/(\vartheta\mathsf{d})\), and \(\mathsf{d}\le\operatorname{dist}(\operatorname{supp}f_1,\operatorname{supp}f_2)\le6\mathsf{d}\)" (CA-I L2758–2763). Same upper bound with vanishing \(u\): "uniformly in \(K\), \(g_0\), \(m\) and the position" (L2782), \(S^T_{2;K,m}\le\tfrac83b_0C_{\mathcal K}\|f_1\|_\infty\|f_2\|_\infty(g^{-2}+\lambda_\sharp s-c_5)^{-2}\) (L2788–2789), with \(s(\mathsf d)\to\infty\) as \(\mathsf d\downarrow0\) (L2745–2746). Lower bound positive (L2786–2787), so \(S_2^T\ge0\). Every \(\vartheta\in(0,1]\) is allowed (L2720), so \(\vartheta_*=1/12000\) is admitted, at the ceiling \(\gamma_W^{\mathbb T}(\vartheta_*)\). Valid for "every \(m\ge m_{\mathbb{T}}(g_-(g))\) (hypothesis (H5), and nothing more on \(m\))" (L2766), at depths with \(K-s(\mathsf d)\ge k_W\) (eq. 3.1:eq-main-2), which holds for fixed \(\mathsf d\) once \(K\) is large.
- Uniform in \(m\) means it passes to torus-limit DLR states at fixed cutoff, hence to RO1's volume-first realization. It does **not** pass to arbitrary periodic states. So it does not supply H-T for PH1 components, whose realizing states need not be torus limits.
- Standing (CA-III L110909–110969): proved as an implication. Beneath it: "the source lemma and the flat shell bound, both stated in Chapter~\ref{ch:8} with their proofs outstanding, and the continuum kernel, whose statement and proof are not written out there" (L110952–110955); "one part of the small-piece statement beneath the localisation of the sourced step is of status ``stated; proof incomplete''" (L110943). The ch13 list confirms: "Lemma~\ref{8.21:lem-source} \(\cdot\) the source lemma \(\cdot\) ... proof outstanding" and "Lemma~\ref{8.21:lem-continuum-kernel} ... proof outstanding" (CA-III L111245–111247).
- Note: CA (iv) does not use volume-uniform rarity of never-healed regions (CA-III L110939–110941, L110964). Our TP1 route to TU10 goes through AG-rarity (assembly-status L136). CA's route avoids that open item.
- **Verdict for H-T: supplied by CA (iv) at CA standing**, for torus-limit realizations only.

### 2.5 H-S (SR1) and H-P (PH1)
- H-S: CA (ii-\(\mathbb R^4\)) gives "distributions of locally finite order on \((\mathbb{R}^4)^n_{\neq}\)" (CA-I L2695) and lists "coinciding points" and "temperedness" as not asserted (L2705–2706). It gives no diagonal-flat extension. SR1 is frozen as an implication from UV1 (sr1.md L544, L568). Not needed for O(4) on separated tuples.
- H-P: CA lists "uniqueness of \(\Omega\) and clustering" as not asserted (CA-I L2708). No component theory in CA. PH1 is frozen as an implication from LG1, SR1, CL1 (ph1.md L581, L606). Not needed for the torus-limit case.

## 3. Does RO1 use (IR-fl), or an equivalent, in disguise?

**What (IR-fl) is.** CA-I L3029–3048: the connected correlation of the shell-averaged flux \(\mathfrak B^{\rm sh}_{\chi_{\mathcal R}}\) of the lattice rotation current with \(\mathcal O(f_1),\ldots,\mathcal O(f_n)\) has \(\liminf_{\mathcal R\to\infty}\limsup_j|\cdot|=0\). Sufficient: stress-tensor insertion decay \(o(\mathcal R^{-4})\), uniformly in the cutoff (L3050–3076). It is an infrared statement: a correlation at distance \(\mathcal R\to\infty\).

**RO1 uses no such object.** A text search of ro1.md for "stress", "Ward", "flux", "cluster", "infrared" finds nothing. No current, no Ward identity, no far sphere. I then checked each step for any large-distance input.

- Lemma 1 (L94–119). Fixed cutoff. The only volume limit is (1.3): the DLR/torus oscillation cost \(72\beta l^4a^{-3}\ell^{-1}\to0\) as \(\ell\to\infty\) at fixed \(a\) (L114). No correlation decay.
- Lemma 2 (L121–215). Uses H-U as a per-cell upper bound. The coarse scales enter through "\(C_1(l/a_s)^4\)" per cell (L179), summed geometrically in (2.6) (L183–184); the infrared remainder enters only as the extensive constant \(C_{\rm st}\ell^4\) (L57), i.e. \(C_{\rm st}\) per unit volume. This is a stability (free-energy) bound, not a decay of correlations. The domain decay \(e^{-\kappa m(X)}\) is polymer locality at each RG scale \(a_s\le1\), counted in units of \(a_s\).
- Lemma 3 (L217–288). Spectral calculus on the cube cone at a fixed small time margin. Local.
- Lemma 4 (L292–401). Kernels are bounded by \(\delta^{-5n}\) with \(\delta=\min(1,\min_ir(v_i))\) (L325–328). Large separations cost nothing because \(\|T(v)\|\le1\) (L308). The finite band (L366–370) comes from growth \(e^{5n|\Im z|}\): imaginary rotation shrinks the light margins like \(e^{-|\Im z|}\) (L366). That is a short-distance (light-cone) input.
- Lemma 5 (L405–481). Only \(t\to0\): "\(t^8\Gamma(t)\longrightarrow0\)" (L411), from \(m_\mu(Q)=o(Q^8)\) at high energy (L473). Vacuum subtraction "needs no unique vacuum" (L420).
- Theorem 6 (L483–554). The critical modes die by "\(0\le g_r(is)\le\Gamma(re^{-|s|})=o(e^{8|s|})\)" (L494): again \(\Gamma\) near zero. The \(|m|=1\) step is a positivity identity at each finite \(s\): "\(c_0+2c_1\cosh4s\ge0\)", "\(c_0-2c_1\cosh4s\ge0\)" (L547–548). The limit \(s\to\infty\) is a boost, not a distance. No rate at large distance.
- Lemma 7 (L558–582). Rotation phases, Cauchy–Schwarz (4.10), real analyticity on connected configuration spaces, integer convexity. No decay.
- Lemma 8 (L584–628). Holomorphy of translations from the cube cone, (8.2) (L599–604). Local.
- Theorem 9 (L645). Coordinate-plane rotations generate SO(4).

**Where the infinite volume enters.** Only in two places. (i) The order of limits: volume first at each spacing (L18–23). (ii) LG1 Theorem 10 (lg1.md L365): diagonal RP of every periodic DLR state, proved at fixed cutoff via Lemma 9's comparison with tilted-period states (lg1.md L313–330). Both are proved lattice facts or construction choices. Neither is a decay hypothesis. The cube cone (CL1 Lemma 8) follows from two reflections, with no decay.

**Conclusion for Q3.** RO1 does not use (IR-fl) or a stress-tensor decay, openly or in disguise. Its replacements are ultraviolet (H-U, H-T) plus diagonal RP of the volume-first limit. The IR content that CA's Ward-identity route needs at \(\mathcal R\to\infty\) does not arise, because RO1 never integrates a local identity over space.

**Consistency with CA's counter-models.**
- Anisotropic free fields (CA-III L108524–108549): RP at axis hyperplanes, \(W_4\), mass gap, not O(4). "The model also fails reflection positivity at the twelve diagonal mirrors" (L108554–108555). It violates H-L/H-C. Excluded by RO1's hypotheses.
- Threshold model, \(\mathcal O^\lambda(f)={:}\sum_I(\psi_I+\lambda H_I)^2{:}\) (CA-III L109238–109311, "Proof outstanding", L109314). It is RP "at every hyperplane normal to any of the sixteen mirror normals of \(W_4\)" (L109265–109266) and not O(4). Its observable is \({:}(\partial^4\phi)^2{:}\), of dimension 10. So \(S_2\sim|x|^{-20}\), and for tests of size \(d\), \(S_2^T(f,h)\sim d^{8}\cdot d^{-20}\|f\|_\infty\|h\|_\infty\to\infty\). It violates H-T (which needs \(u(d)\to0\)). In RO1's terms \(\Gamma(t)\sim t^{-20}\), so \(g_r(is)\) may grow like \(e^{20|s|}\) and the step at L494 fails. Excluded by RO1's hypotheses. (This is my scaling computation, not a CA statement.)
- CA's own lesson: "By Proposition~\ref{10.8:prop-threshold-sharpness}, even reflection positivity at all sixteen mirrors of \(W_4\) does not suffice without an infrared or growth input of its own" (CA-III L108564–108565). RO1's H-T is exactly a growth input (ultraviolet). CA's stronger sentence, "No argument that uses only reflection positivity, \(\mathbb{R}^4\rtimes W_4\)-invariance and position-uniform bounds can prove \((\mathrm{IR\text{-}fl})_{\omega_0}\)" (L109310–109311), is about proving (IR-fl). RO1 does not prove (IR-fl), and uses more than those three inputs.
- "Without any hypothesis, no bounded, non-constant, continuous, translation-invariant two-point kernel \(T\) on \(\mathbb{R}^4\setminus\{0\}\) is reflection positive ... at all sixteen mirrors" (CA-III L79983–79989). RO1's connected kernel is not bounded near zero (\(\Gamma(t)\) is finite only for \(t>0\), ro1.md L408–410). No conflict.

## 4. Does CA's O(4) chapter consider and reject an RP route like RO1's?

Yes, in one remark, and partly. CA-III Remark 10.1:rem-diagonal-positivity (L79931–79990), "Two-point rotation invariance under diagonal reflection positivity".

**What it says.**
- Scope: "This remark concerns the two-point function only. It is an implication from a hypothesis that Theorem~0 does not assume and that is not proved" (L79933–79935).
- Hypotheses (L79947–79957): (a) coordinate RP on one-field vectors and \(\mathbb R^4\rtimes W_4\); (b) clause (iii-b); (c) "The upper member of clause~(iv) of Theorem~0, with its logarithmic factor"; (d) diagonal RP of \(S_2[\sigma]\) on one-field vectors at \(v_{01}^\perp\).
- Conclusion: two-point O(4) (L79959–79961). The proof is referred to "the theorem deducing two-point \(O(4)\) invariance on \(\mathbb{R}^4\) from (a)--(d); it is not reproduced here" (L79964–79966). I searched the theorem/lemma/proposition headings of CA-I/II/III for that theorem, for "the lemma on diagonal reflection positivity of the Wilson weight" (L79974) and for "the theorem on hyperoctahedrally reflection-positive translation-invariant kernels" (L79988–79989). I found no numbered statement for any of them. Only the remark's own cross-references matched. (Not found, which is weaker than read.)

**Why CA rejects it for Theorem 0.** Two reasons.
1. (d) is not available for CA's limits. "Diagonal reflection positivity holds for the Wilson weight on \(\mathbb{Z}^4\) and fails on every straight torus ... For the periodic family of tori, hypothesis~(d) would amount to independence of the limit from the shape of the box. It is not proved, and it is not assumed by Theorem~0" (L79973–79977). Also L108556–108562: "A diagonal hyperplane, however, does not separate the periodic torus on which the lattice measures of Theorem~0 live. This positivity is therefore not asserted for the limits of Theorem~0 and is not used in this book."
2. Higher points. "The statement is restricted to two points. For \(n\ge 3\) the item that is missing is positivity for configurations rotated by an element of \(O(4)\setminus W_4\), and that positivity is itself the conclusion sought" (L79979–79981).

CA's (ii-\(\mathbb R^4\)) also omits the spectral cone: "Not asserted ... the spectrum condition (joint energy--momentum spectrum in the closed forward cone) beyond \(H\ge0\)" (CA-I L2705–2708). CA-III L101429–101432 says the spectrum condition "would follow only from (M1) and (M2)", neither supplied.

**Does RO1 escape?**
1. Diagonal RP: **yes, on its own domain only.** RO1 does not use torus measures at the diagonal mirror. It uses volume-first limits of DLR states on \(\mathbb Z^4\), where LG1 Theorem 10 proves diagonal RP at fixed cutoff (lg1.md L365), and CL1 Lemma 3 passes it to the limit (cl1.md L160–166). This matches CA's own sentence that the Wilson weight has diagonal positivity on \(\mathbb Z^4\). It is not box-shape independence; it is the choice to remove the volume first. LG1 Lemma 12 (lg1.md L417) agrees with CA that no single torus is adapted to both a coordinate and a diagonal normal. The price: RO1 covers the volume-first subclass of CA's (ii-\(\mathbb R^4\)) limits (§2.0), not all of them.
   The load-bearing claim is LG1 Theorem 10: **every** periodic DLR state is diagonally RP. CA does not state or refute this. A referee should read LG1 Lemmas 5, 8, 9 and Theorem 10 hardest; LG1 has had one Claude gate (lg1.md change log L477–483).
2. Higher points: **yes.** RO1 never needs positivity of a rotated configuration of the full kernel. Lemma 4 gets boost positivity from the Gram identity (4.7) along imaginary rotations (ro1.md L354–364: "This is a vector Gram identity, not continuation of a scalar inequality"). It then isolates the **top** harmonic coefficient \(H=c^{(2k)}_{-M(2k)}\). That single coefficient obeys the covariance (4.1), so its positivity across a line with any normal \(R_\nu e_0\) is the time-reflection positivity times the phase \(e^{4iM(2k)\nu}\) (L393–397). Lemma 7 (L558–582) uses only this top-coefficient positivity, plus polygon rotation and convexity, to force \(M(2k)=kM(2)\). Theorem 6 gives \(M(2)=0\). So the "missing item" of L79979–79981 is replaced by positivity of one harmonic, which is covariant by construction. This is SA's angular chain (ym4.tex L31826–31835).
3. Spectral cone: **yes.** RO1 needs only the cube cone (ro1.md L31), which CL1 Lemma 8 derives from one coordinate and one diagonal reflection (cl1.md L416–453), not the forward cone.

**Comparison of hypotheses at two points.** CA's (a)–(d) contain no insertion bound like H-U. RO1 reaches Theorem 6 through plates (Lemma 3–5, which use Lemma 2, hence H-U). For \(n=2\) alone, H-U may be avoidable: the band at L494 uses only \(\Gamma\), and \(\Gamma\) comes from TU10. But RO1's \(\mu\) is built from plate vectors \(\zeta_{\varphi,a}=(1-P_\Omega)B_{\varphi;a}\Omega\) (L416). Whether a plate-free two-point version holds on CA standing plus LG1/CL1 is **not checked** here. For \(n\ge3\), Lemmas 4 and 7 need the plates, hence H-U.

## 5. Verdict

**(b), with a precise form.** RO1 gives O(4) without (IR-fl). It does not secretly need (IR-fl) (§3). But it does not run on CA's clauses alone. One input is not a CA statement at all, and the others are at CA standing, which CA itself calls "proved as an implication", never "proved" (CA-III L110865).

Input table, for RO1 on a volume-first limit through torus-limit DLR states (not PH1 components):

| RO1 input | Supplied by | Standing |
|---|---|---|
| H-U (UV1 rooted D1) | Nothing in CA in this form. Ingredients: CA-II correlation theorem 5.1, (iii) L2919–2936 and (iv) L2937–2957 | **Open.** Ours: UV1 "not started", D1 [O] (assembly-status L28). CA's theorem has an outstanding hypothesis (CA-II L2810–2812) |
| H-L (LG1, all mirrors incl. diagonal) | Our LG1 Theorems 10, 13 | Closed in LG1 (lg1.md L475, L485); one Claude gate. Not in CA (CA-III L108561–108562) |
| H-C bounds, coordinate RP, OS space | CA (iii-b) CA-I L2610–2625; CA (ii-\(\mathbb R^4\)) L2690–2704, via CL1 Thm 9(1) recognition | CA standing (CA-III L110896–110908); (iii-b) rests on a "stated; proof incomplete" item (L110899) |
| H-C diagonal RP of the limit, cube cone | CL1 Lemmas 3, 7, 8 from LG1 | Proved in CL1 (frozen) given convergence and bounds; needs re-reading with (iii-b) in place of SR1 |
| H-T (TU10) | CA clause (iv), CA-I L2715–2790 | CA standing (CA-III L110909–110969); beneath it the source lemma and flat shell bound, "proofs outstanding" (L110952–110955; ch13 L111245–111247) |
| H-S (for \(\Sigma_n\) only) | Not in CA; our SR1 | Conditional on UV1 (sr1.md L568) |
| H-P (components only) | Not in CA; our PH1 | Conditional on SR1, CL1 (ph1.md L606); CA (iv) is torus-only, so state-uniform H-T for components is not supplied |

**Precise statement of what is available now.** Assume H-U on CA's first-passage data. Then RO1 Theorem 9 gives, for every volume-first limit \(S\) through torus-limit DLR states at CA's first-passage data, with \(g\le\min(\gamma_J,\gamma_W^{\mathbb T}(1/12000))\) and IN1's/CA's constant order: \(S_n(Rf_1,\ldots,Rf_n)=S_n(f_1,\ldots,f_n)\) for all \(n\ge2\), \(R\in\mathrm O(4)\), real compact \(C^1\) \(f_i\) with pairwise disjoint supports. This is CA clause (vi)'s conclusion (CA-I L3078–3082) on the volume-first subclass of (ii-\(\mathbb R^4\)) limits, with (IR-fl) replaced by H-U. Its standing is CA's (iii)/(iv) standing plus H-U plus LG1/CL1.

**What changes relative to CA.** CA has clause (vi) "Not proved" (CA-III L111006), resting on (IR-fl), "a hypothesis of clause~(vi) and is derived nowhere in this book" (L110834–110835). RO1 moves O(4) from an infrared hypothesis that CA's programme does not touch to ultraviolet statements that CA's programme is built to prove (its correlation theorem and clause (iv)). This is a real difference in kind. It is not yet a proof at any higher standing than CA's other clauses.

**What would have to be done to make (a) complete.**
1. **Write UV1 on CA's inputs.** Derive RO1's H-U (ro1.md L54–60) from CA's correlation theorem (CA-II L2791–2966) and clause (i). Needed: the sourced torus bound on \(|Z_\ell(W)|/Z_\ell(0)\) for whole-torus mirror-periodized complex sources of small \(\|\cdot\|_\sharp\); summation of all scales' localized terms; decay rate \(\kappa\) above the rooted entropy \(22\log2\) plus type entropy (ro1.md L166); representation independence; the extensive last-lattice constant. Check that CA's source classes \(\mathcal W_k\) contain these sources. This is the one genuinely open input.
2. **Record H-T from CA (iv).** Pass CA (iv) to torus-limit DLR states at fixed cutoff (uniform in \(m\), CA-I L2766, L2782), then to the limit. Fix \(\vartheta_*=1/12000\) and the ceiling \(\gamma_W^{\mathbb T}(\vartheta_*)\) inside RO1's constant order (ro1.md L88). Short; no new estimate.
3. **Re-run CL1 on CA (iii-b).** Replace I3 (SR1) by (iii-b) in CL1 Lemmas 1–3, 5, 7, 8, with \(\rho_j=\nu_j\) torus-limit states. Check first-passage data are CA's, not IN1's, throughout RO1.
4. **Referee LG1 Theorem 10 hard.** It is the one place where RO1 claims something CA says it cannot get for its limits. The claim is about DLR states on \(\mathbb Z^4\), so it does not contradict CA, but it carries the escape.
5. **Optional, to match CA's full domain.** Either a recognition theorem identifying arbitrary joint-diagonal (ii-\(\mathbb R^4\)) limits with volume-first ones (SA L24480–24487 names this gap), or accept the volume-first subclass as the stated domain.
6. **Optional, two points first.** Check whether Theorem 6 runs without plates (no H-U), from CA (ii-\(\mathbb R^4\)), CA (iv), LG1 and CL1 alone. If so, two-point O(4) of volume-first limits is available at CA standing now, without (IR-fl) and without D1. This matches the shape of CA's own Remark 10.1 hypotheses (a)–(d), with (d) supplied by LG1 + CL1.

Even after 1–4, the result stands no better than CA's correlation theorem and clause (iv), since CA proves no clause outright (CA-III L110865, L111046–111047: "none can stand better than the correlation theorem and the ultraviolet steps on which that theorem rests").
