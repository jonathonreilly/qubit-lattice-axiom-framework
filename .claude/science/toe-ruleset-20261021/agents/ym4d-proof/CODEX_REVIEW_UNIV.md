# PRE-STATED

This contract was written before reading the target or the earlier P4 review in this session. The user's prompt disclosed the eight claims to attack; that prior exposure is explicit. This is an independent mathematical review, not an audit-status update or an existence proof for Yang–Mills theory.

- Scope: `UNIV55.md` and the necessary local support, especially `CODEX_REVIEW_P4.md`. No git operations. The only written file is this report.
- Frozen target SHA-256: `62033ebd7f6928261b8262616c9437bb22c4bca5179d645ed2b5119268ca8609`.
- Earlier P4 review SHA-256: `12d59c044e86af2fe66806332aed9a2e98181409e075151a983c4b4eeb7d1b34`.
- Verdicts: **CONFIRMED** requires an actual proof with the claimed quantifiers; **REFUTED** requires a concrete contradiction or counterexample to those quantifiers; **NOT-VERIFIED** means an unresolved hypothesis, missing estimate, ambiguous statement, or unsupported argument. A conditional implication and satisfaction of its hypotheses receive separate verdicts.
- Proposition T: independently reconstruct the disintegration, reference measure, normalization, observable norm, exact-equality case and approximate bound. Test whether coarse-law independence is uniformity in that law or literal disappearance of the law.
- IR claim: separate fixed physical volume, continuum limit, thermodynamic limit and volume-uniform comparison. Test the two-phase example exactly; it must establish only its actual obstruction, not necessity of a particular decay hypothesis for every route.
- UV claims: check all cutoff/volume dependence in the soft-kernel lower bound; distinguish unsuppressed coarse fields from failed comparison; track the marginal direction and common-space construction without accepting power counting as a uniform theorem.
- Geometry/topology: prove the dense-subgroup statement exactly; distinguish interpolating edge holonomies from extending plaquette logarithms, transition data or a prescribed topological sector. Treat semiclassical instanton weights separately from rigorous probability estimates.
- Sphere/Ward route: write the finite-regulator identity, including measure/Jacobian, gauge, contact and defect contributions. Distinguish absence of a geometric boundary from vanishing regulator or seam insertions, and fixed-radius estimates from uniform decompactification.
- Seam and Theorem U: check factorization variables, hypotheses, limiting order, joint subsequences and continuity needed to extend dense symmetry to full OS1. Do not infer OS0, OS2, OS3 or non-freeness from an OS1 argument.
- Arithmetic is exact or symbolic only; no floating-point evidence. Literature recollections are marked `[m]`; checked external sources are identified explicitly and cannot replace a missing local argument.
- The report will end with the precise bankable statements and a judgment on whether the sphere route makes OS1 purely ultraviolet.

## Review boundary and principal finding

Read [UNIV55.md](UNIV55.md) completely, including all corrections and E1–E6, and [CODEX_REVIEW_P4.md](CODEX_REVIEW_P4.md) completely. Superseded formulations in E1–E3 are not treated as the author's final position. Relevant original passages of [PROOF.md](PROOF.md), [REVIEW_S22.md](REVIEW_S22.md), and [ROTDEF.md](ROTDEF.md) were inspected; these larger files were not reviewed in full. This is an independent source review, not a branch review or an audit. No exact runtime model identifier is inferred from the requested model label.

**CONFIRMED: the fixed-volume comparison implication. NOT-VERIFIED: its Yang–Mills hypotheses and an unconditional “OS1 is purely UV” conclusion.** Source: UNIV55.md, locating strings “Proposition T (fixed volume: the coarse integral drops out)”, “Theorem U (CONDITIONAL)”, and “Closing statement”.

The probability lemma survives. The Ward alternative is a coherent conditional route that avoids comparing two coarse spaces. Neither supplies the missing all-background estimates. Corrections are needed to the alleged necessity of decay, the SU(N)/U(1)/SO(3) distinction, the inference from geometric errors to small marginal coefficients, and the interpretation of the instanton power. The corrected RG induction works once a quantitative AF envelope is an actual hypothesis.

## 1. Proposition T and “the coarse law never appears”

**CONFIRMED.** Source: UNIV55.md, locating strings “Proposition T”, “(U-cond)”, “(U-dens)”, and “E5 (addendum to §2.1”.

Use one reference measure \(dV\), positive conditional partition functions \(Z_G(V)\), and conditional observables \(h_G(V)\). Put

\[
 Q_G=\int Z_G(V)\,dV,\qquad \rho_G=Z_G/Q_G,\qquad
 \omega_G(F)=\int h_G\rho_G\,dV.
\]

If

\[
 \sup_V|h_1-h_R|\leq\delta_c,\qquad
 \sup_V|\log Z_1-\log Z_R-c'|\leq\delta_d,
\]

then \(Q_1/Q_R\in[e^{c'-\delta_d},e^{c'+\delta_d}]\), and hence

\[
 e^{-2\delta_d}\leq\rho_1/\rho_R\leq e^{2\delta_d}.
\]

For \(\|F\|_\infty\leq M\),

\[
 \omega_1(F)-\omega_R(F)
 =\int(h_1-h_R)\rho_1\,dV+\int h_R(\rho_1-\rho_R)\,dV
\]

gives exactly

\[
 |\omega_1(F)-\omega_R(F)|
 \leq\delta_c+M(e^{2\delta_d}-1).
\]

In the normalized formulation \(|c|\leq\delta_d\), as claimed. If \(\delta_c=\delta_d=0\), the normalized coarse laws coincide and the expectations agree. Complex bounded observables obey the same estimate. Unbounded observables require additional integrability.

The polymer implication is also correct, provided its norm dominates the stated real-field suprema:

\[
 \sup_V\left|\sum_X\delta P_X(V)\right|
 \leq\sum_b\sum_{X\ni b}\sup_V|\delta P_X(V)|
 \leq N_b\eta.
\]

Field-independent vacuum constants enter \(c'\). Fixed \(N_b\) and \(\eta\to0\) suffice regardless of strong coupling, phase coexistence, or susceptibilities in the remaining coarse integral.

**CONFIRMED as “no separate coarse-correlation estimate is used”; NOT-VERIFIED as automatic elimination of all long modes.** Source: UNIV55.md, locating strings “Nothing about ν^G enters”, “both hypotheses of Proposition T”, and “UV by construction” in §6.

E5 is algebraically exact. It does not erase the coarse-law comparison: relative conditional partition functions determine that law. Nor does normalization of a Markov kernel establish that its conditional fluctuations live only below \(\ell_0\). For example, with the normalized positive kernel \(k(V\mid U)=1\), the coarse density is identically one but \(h_G(V)=\omega_G(F)\). The observable hypothesis is then the desired conclusion itself. This tests the inference from disintegration alone; it is not a counterexample to the lane's specified contour kernel.

For that kernel, conditional locality/coercivity uniform in the pinned field would justify the intended scale interpretation. It is a substantive analytic obligation outside the small-field region. Proposition T supplies a sufficient mechanism, not evidence that its hypotheses are weaker or easier than universality. It does settle the narrower issue: a **proved** all-configuration relative-weight comparison at fixed volume cannot be defeated by an uncontrolled coarse susceptibility.

## 2. IR and the exact content of the two-phase example

**CONFIRMED: the finite-volume response identity and example.** Source: UNIV55.md, locating strings “The exact point where infrared information enters”, “d/ds E_{ρ_s}[h]”, and “E_{ν_η}[σ_0] = tanh(η|Λ_n|)”.

For \(D=\sum_X\delta P_X\) and \(d\nu_s=e^{sD}d\nu_0/\nu_0(e^{sD})\),

\[
 \frac{d}{ds}\nu_s(h)=\operatorname{Cov}_{\nu_s}(h,D).
\]

On \(M\) sites in the two-phase law the perturbed weights are exactly

\[
 p_\pm=\frac{e^{\pm\eta M}}{e^{\eta M}+e^{-\eta M}},
 \qquad \nu_\eta(\sigma_0)=\tanh(\eta M).
\]

Thus \(\eta\to0\) at fixed \(M\) gives zero, while \(M\to\infty\) at fixed \(\eta>0\) gives one. The joint sequence \(\eta_M=1/M\) gives the nonzero constant \(\tanh1\). These symbolic calculations refute a volume-independent vanishing estimate based on per-site smallness alone over this class of laws.

**REFUTED as a necessity claim.** Source: UNIV55.md, locating strings “a bound uniform in n needs”, “the passage from Version Ω to R^4 is exactly the summability condition”, and “The two-phase example shows it cannot be removed without decay”.

Absolute covariance summability is sufficient for the displayed triangle-inequality method. It is not necessary for every uniform comparison. On \(2m\) sites in the same two-phase law, take

\[
 \delta P_{2j-1}=\eta\sigma_{2j-1},\qquad
 \delta P_{2j}=-\eta\sigma_{2j}.
\]

Their total is zero on both configurations. Thus \(\nu_s=\nu_0\) and all expectations agree at every volume. Nevertheless, for \(h=\sigma_1\), each absolute covariance equals \(\eta\), so their sum is \(2m\eta\). No correlation decay occurs. Cancellations, symmetries, or a restricted perturbation class can remove an extensive response without the asserted absolute summability. This example does not claim such a cancellation in Yang–Mills.

“IR enters only when removing \(N_b\)” is valid as a description of this **particular sufficient bound after its uniform conditional inputs have been supplied**. It is not a theorem locating every possible IR dependence of a proof. Conditional mixing, nonuniform source bounds, exterior-law comparison, or the later \(R\to\infty\) limit can introduce other long-distance obligations. Failure of this absolute-summability method is not a no-go for a selected symmetric limit.

The correct conclusion is: fixed-volume uniform density comparison needs no IR decay; the two-phase example blocks its extension to arbitrary infinite-volume laws from per-block smallness alone.

## 3. Soft-kernel minorization and large coarse fields

**CONFIRMED, with fixed or uniformly bounded final kernel strength.** Source: UNIV55.md, locating strings “Well-posedness of sup_V (soft kernel)”, “The comparison must hold ON large fields”, and “probability → 1 as R grows”; original source: PROOF.md, “Decision 4: the RG kernel”.

Write \(b=\kappa_0/g_*^2\), where \(g_*\) is the final kernel coupling, not the fine bare coupling. The contour matrices are unitary and their averaging weights are nonnegative and normalized. Hence

\[
 \|\overline M_c\|_{\rm op}\leq1,\qquad
 0\leq1-N^{-1}\Re\operatorname{tr}(V_c^{-1}\overline M_c)\leq2.
\]

Haar probability gives \(e^{-2b}\leq\mathcal N(\overline M_c)\leq1\), so \(k_c\geq e^{-2b}\). Conditioning on the **penultimate** field and then integrating it gives

\[
 \rho(V)\geq e^{-2b|E_0|},\qquad
 \nu(A)\geq e^{-2b|E_0|}\operatorname{Haar}(A).
\]

This is independent of the fine cutoff when \(b\) and the fixed-volume coarse graph are fixed. Positivity defines the ratio version of the conditional expectation at every \(V\). If \(b=b(a)\to\infty\), this does not supply a cutoff-independent positive lower bound.

For the growing-volume claim select \(m\) plaquettes with disjoint links. Given the penultimate field, their events are independent because the last kernel factorizes over output links. Each large-angle event has probability at least

\[
 q=e^{-8b}\operatorname{Haar}\{W:\|\log W\|\geq\varepsilon_0\}>0
\]

when the displayed Haar set has positive measure: four independent Haar links have Haar plaquette product. Thus \(\nu(\text{none})\leq(1-q)^m\to0\) as \(m\to\infty\), at fixed \(b\). Conditioning only on the original fine field need not make a multistep composite kernel factorize; the correct conditioning is on the last input.

**CONFIRMED as a limitation of a small-field-only proof; NOT-VERIFIED as a necessity of using a supremum method.** Source: UNIV55.md, “does not reach it” and “so the sup must cover it”; original source: REVIEW_S22.md, “Statement (BFT)” and “max_P|log V^r_{k,P}| ≤ ε ≤ ε_0”.

A positive-Haar-measure coarse large-field set cannot be discarded because its probability allegedly vanishes with \(a\). BFT's stated domain excludes it. But nonvanishing probability does not force pointwise uniform comparison; a weighted bound, coupling, or cancellation might suffice. The conclusion is specific to the proposed supremum route. The fine-field assertion retains the threshold and AF-rate conditions in PROOF.md, “Corollary (AF window)”; it is not banked as an unconditional all-\(N\), all-threshold theorem.

## 4. Marginal coupling and the misaligned blocking step

### 4.1 Fixed-ratio scheme difference

**CONFIRMED: E7 as cited does not control an untuned marginal difference. NOT-VERIFIED: a nonzero \(O(1)\) difference for this particular pair of blocking maps.** Source: UNIV55.md, “The marginal direction — the step P4's sketch omits” and “scheme constant c”; original source: PROOF.md, “E7.2 (contraction)” and “The marginal direction is fixed by RC”.

Contraction on irrelevant coordinates cannot bound a remaining marginal coordinate. But the manuscript supplies no matching integral or nonperturbative calculation of \(c_1-c_R\) for these contour families. Different schemes can have different finite coupling coordinates; that fact does not prove a nonzero difference for this pair. A field redefinition transforms observables and irrelevant coordinates too. Its isolated scheme coefficient is not a physical obstruction to universality. The proposed redundancy cancellation remains unproved; fixed-ratio blocking has not been excluded.

The formal propagation calculation for an already small scalar inverse-coupling difference is sound under a beta-function expansion with a derivative-controlled remainder. For \(u=g^{-2}\),

\[
 \frac{du}{d\log\mu}=2\beta_0+2\beta_1/u+O(u^{-2})
\]

has linearized derivative \(O(u^{-2})=O(g^4)\) if the displayed remainder has derivative \(O(u^{-3})\). A controlled AF envelope makes its integral finite. Mere differentiability of an \(O(u^{-2})\) remainder would not imply that derivative bound. This conditional ODE calculation does not verify the nonperturbative envelope or first-step matching.

### 4.2 Diverging ratio

**CONFIRMED: the scalar scale conditions are compatible. NOT-VERIFIED: they imply N2's effective-action estimate.** Source: UNIV55.md, “One misaligned step with a slowly diverging ratio r(a)” and “every component of the first-step difference”.

For example \(r=1/g\to\infty\) gives \(g^2r=g\to0\). An explicitly commensurate choice is \(r_k=5k\), \(a_k=\ell_0/(5kL^{k^2})\), and first common scale \(s_k=\ell_0/L^{k^2}\), followed by \(k^2\) aligned steps. When \(\ell/\ell_0\) is an integer, these are allowed torus spacings, and the stated AF asymptotics give \(g(a_k)^2r_k\to0\). The staircase length factor is exactly \(3/5+4/5=7/5\). These facts alone control neither conditional partition functions nor an absolute difference in \(g^{-2}\).

A simple exact control exposes the missing normalization argument. For a Gaussian variable with density proportional to \(e^{-A^2/(2g^2)}\), replace the coarse variable by \(V=(1+1/r)A\). The relative change tends to zero, but its inverse variance changes by

\[
 \delta u=g^{-2}\big[(1+1/r)^{-2}-1\big].
\]

At \(g=1/n,\ r=n\), both proposed small parameters are \(1/n\), while

\[
 \delta u=-\frac{n^2(2n+1)}{(n+1)^2}\leq-n\quad(n\geq2).
\]

This is not a Yang–Mills counterexample. It refutes the inference from small geometric/transport errors alone to small **absolute marginal coefficients**. N2 must prove matching of the leading continuum normalization, including \(g^{-2}\) amplification and every marginal tensor component allowed by the reduced common symmetry. A scalar \(m_j\) suffices only if that marginal sector closes, or if it denotes a norm of the whole sector.

Polynomial growth of constants in \(r\) also needs its actual exponents: \(g^p r^q\to0\) does not follow from \(g^2r\to0\) for arbitrary \(p,q>0\). A slower \(r=\log(1/g)\) beats any fixed polynomial multiplied by a positive power of \(g\), but cannot repair a term \(r^q/r\). Quantitative estimates must say which terms carry which powers.

**NOT-VERIFIED as a theorem: the rejection of a one-step block to physical scale \(\ell_0\).** Source: UNIV55.md, “One step straight from scale a to a fixed fraction of ℓ_0” and “the mean is shrunk”. The Wilson-line self-energy argument is explicitly [m]. Even mean shrinkage requires a concentration estimate for the averaged transporter and analysis of the normalized kernel before it implies loss of useful information. No universal exclusion of that option is banked.

**REFUTED if interpreted as a lower bound on the actual error; CONFIRMED as optimization of the proposed envelope.** Source: UNIV55.md, “The rate”, specifically “O(1/r + g(a)^2 r) ≥ 2g(a)·O(1)”.

\[
 \frac1r+g^2r-2g=\frac{(1-gr)^2}{r}\geq0.
\]

But an \(O(1/r+g^2r)\) upper bound supplies no lower bound on the error, which could vanish or have cancellations. Optimizing this envelope gives \(O(g)\) if N2 is proved with the asserted constants. No power-law rate has been established, and none has been excluded.

## 5. The rational rotation and the dense subgroup

**CONFIRMED, without importing Niven's theorem.** Source: UNIV55.md, locating strings “One rotation suffices” and “Group lemma, now re-derived”.

Let \(z=(3+4i)/5=e^{i\theta}\). If \(\theta/\pi\in\mathbb Q\), then \(z\) is a root of unity. Thus \(z+z^{-1}=6/5\) is an algebraic integer. A rational algebraic integer is an integer: inserting a reduced fraction \(p/q\) into a monic integral polynomial forces \(q\mid p^n\), hence \(q=1\). The contradiction proves \(\theta/\pi\notin\mathbb Q\).

The closure of the powers of this rotation is all of \(SO(2)_{12}\). Conjugating by signed coordinate permutations gives every \(SO(2)_{\mu\nu}\). Coordinate-plane rotations generate \(SO(4)\), for example by eliminating matrix entries with successive Givens rotations. A coordinate reflection supplies the other component, proving

\[
 \overline{\langle H_4,R_\theta\rangle}=O(4).
\]

The periodicity assertion is also exact: at \(a=\ell/(5n)\), \((\ell/a)R^{-1}e_i=5nR^{-1}e_i\in\mathbb Z^4\).

**REFUTED if interpreted as a full rotation action on the same standard torus.** Source: UNIV55.md, “rotation acts by” in §1.2, and “Not available for UNIV-T” in §3.4.

This \(R\) does not preserve \(\ell\mathbb Z^4\). A once-winding \(e_1\) loop has a rotated lift with endpoint displacement \(\ell R e_1\notin\ell\mathbb Z^4\), so it is not a loop on the same quotient. Rational periodic grids do not make \(R\) a torus isometry. UNIV-T's comparison of the **same** torus observable on two grids remains meaningful. The dense-group argument belongs on an eventual common Euclidean algebra, not as an \(O(4)\) action on this torus. Continuity of the limiting action is still required.

## 6. Topology, smooth interpolation, and instantons

### 6.1 Edge holonomies versus prescribed branch/transition data

**CONFIRMED for existential interpolation of edge holonomies on a regular coarse grid. REFUTED: its alleged failure for U(1) and SO(3) under that same meaning.** Source: UNIV55.md, locating strings “every coarse configuration admits an interpolating connection”, “For U(1)”, and “For SO(3)”.

There is a direct construction. Choose one orientation for each edge \(e\), of length \(\ell_0\). For \(G=SU(N),U(1),SO(3)\), choose \(X_e\in\mathfrak g\) with \(e^{X_e}=V_e\) and \(\|X_e\|\leq D_G\), independent of the link assignment. For SU(N), diagonalize \(V_e\), choose eigenphases in \((-\pi,\pi]\), and add/subtract \(2\pi\) to enough eigenphases to make their sum zero. This gives a traceless logarithm of norm at most \(3\pi\). U(1) and the axis-angle form of SO(3) also have uniformly bounded logarithms.

Around the middle third of each edge choose a thin tube of transverse radius a fixed small multiple of \(\ell_0\). Tubes can be disjoint and avoid every other edge. In longitudinal/transverse coordinates \((s,y)\), take fixed smooth bumps \(f,\chi\), with \(f\) supported in that middle third, \(\int f=1\), and \(\chi(0)=1\). Define

\[
 A_e=X_e\ell_0^{-1}f(s/\ell_0)\chi(y/\ell_0)\,ds,
 \qquad A=\sum_e A_e .
\]

Adjust the sign to the holonomy convention. Along \(e\), the integral is \(X_e\) and the matrices commute, giving holonomy \(V_e\). The connection vanishes near the vertices. Within each tube \(A_e\wedge A_e=0\), and different tubes do not overlap. Consequently

\[
 F_A=dA,\qquad \|F_A\|_\infty\leq CD_G\ell_0^{-2}.
\]

This is a smooth connection with a constant independent of the number of regularly spaced cells. It works on a periodic grid as well as a box. In particular, U(1) and SO(3) edge data have this interpolation.

The U(1) monopole argument adds an unstated restriction: real face fluxes must equal the **principal** plaquette angles. A smooth interpolation need only have

\[
 \int_pF=\theta_p+2\pi n_p .
\]

If principal outward angles sum to \(2\pi\), branch integers can make the actual outward flux sum zero, as \(dF=0\) requires. Fluxes of order \(2\pi\) through coarse faces still require only curvature of order \(\ell_0^{-2}\). Bare link holonomies do not force that principal-branch monopole. Prescribed SO(3) lifts or transition data likewise add information.

**REFUTED: the stated obstruction-theory proof step. NOT-VERIFIED: a continuous, gauge-covariant, branch-controlled interpolation suitable for the RG argument.** Source: UNIV55.md, “a 4-cell is unobstructed” and “finitely many closures suffice”.

Extending a map \(S^3\to G\) over \(B^4\) is not the same problem as triviality of a principal \(G\)-bundle over \(S^3\). Already \(SU(2)\simeq S^3\) has the degree-one identity map, which cannot extend over \(B^4\), since an extension would give a null homotopy. The cited \(\pi_2\) fact does not discharge a prescribed four-cell transition-map extension. Conversely, the tube construction does not prescribe such a map.

Also, a principal logarithm of an SU(N) matrix need not be in \(\mathfrak{su}(N)\): for \(e^{2\pi i/3}I_3\in SU(3)\), it has trace \(2\pi i\). The principal eigenphase norm bound is true, but does not define a global smooth Lie-algebra chart. Compactness and finitely many branch closures do not give derivatives across branch changes.

The constructed interpolator need not depend continuously on \(V\), minimize the constrained action, coincide with the background selected by the soft kernel, or preserve a separately prescribed bundle sector. Its curvature bound proves no conditional quantum partition-function, Hessian, or renormalized-insertion estimate. This distinction, rather than a group-specific obstruction to edge interpolation, is the load-bearing issue.

### 6.2 The small-instanton power

**CONFIRMED: arithmetic in the stated one-loop model. NOT-VERIFIED: a lattice-scale probability estimate uniform in coarse fields.** Source: UNIV55.md, “The most dangerous large coarse fields are UV-safe”, “11N/3 − 4 > 0”, and erratum “E3 (§2.4(C))”.

\[
 16\pi^2\frac{11N}{48\pi^2}=\frac{11N}{3},\qquad
 \alpha:=\frac{11N}{3}-4\geq\frac{10}{3}>0\quad(N\geq2).
\]

If the normalized size law is **assumed** proportional to \(\rho^{\alpha-1}\) on \([a,\ell_0]\), then, for \(2a\leq\ell_0\),

\[
 P(a\leq\rho\leq2a)
 =\frac{(2^\alpha-1)a^\alpha}{\ell_0^\alpha-a^\alpha}\longrightarrow0.
\]

This proves the power within that model. The source's semiclassical input is marked [m]; integrating it does not convert it into a rigorous lattice probability. The usual determinant prefactors and higher running corrections add logarithms [m: recalled semiclassical structure, not derived here]. The continuum instanton approximation is not uniformly justified at \(\rho/a=O(1)\), and lattice dislocations need not have the continuum instanton action.

A checked primary discussion distinguishes the dilute size power from cutoff dislocations and describes shrinking under the Wilson plaquette action: [de Forcrand–García Pérez–Hetrick–Stamatescu, equation (3) and §2](https://arxiv.org/pdf/hep-lat/9802017). That source supports the distinction, not a rigorous bound replacing the missing estimate.

E3 correctly withdraws the claim that fractional boundary charge simply shrinks as an integer instanton. But coarse **link data** do not by themselves specify a smooth boundary connection or its Chern–Simons invariant. Even given such a connection, the relative background correction and lattice fugacity need estimates. There is no proved all-\(V\) suppression bound, no proof that every topological large field is harmless, and no derived ceiling on the universality rate exponent from this semiclassical power.

## 7. The global-Killing-field Ward route W0–W3

### 7.1 Exact identity and two meanings of boundary

**CONFIRMED.** Source: UNIV55.md, locating strings “Ward identity on S^4_R”, “Identity (PROVEN, one line)”, and “needs NO common”; supporting source: ROTDEF.md, “Proposition 3.2 (Ward identity)”.

On \(\mathcal C=SU(N)^E\), for smooth \(S,F,\Xi\), with divergence relative to product Haar measure,

\[
 0=\int_{\mathcal C}\operatorname{div}(F\Xi e^{-S})\,dU,\qquad
 \omega(\Xi F)=\omega\big(F(\Xi S-\operatorname{div}\Xi)\big).
\]

Taking \(F=1\) gives \(\omega(\mathfrak W)=0\), so the right side is the claimed covariance. This includes the measure/Jacobian term. Gauge fixing is unnecessary; a gauge-fixed implementation must also transform its measure and constraints.

Compact **configuration space** makes this integration by parts boundary-free on a finite torus too. ROTDEF's physical shell flux instead arises from a spatial cutoff multiplying the rotation field. A global smooth Killing field on the closed sphere needs no such cutoff, so that shell-at-infinity term is absent. In a covariant continuum description \(\nabla_{(\mu}v_{\nu)}=0\) annihilates the contraction with a symmetric stress tensor.

**CONFIRMED for absence of the radial shell; NOT-VERIFIED if the phrase also discards interface defects.** Source: UNIV55.md, “its IR term TQ_ν — does not exist” and “(W2) Seam transparency in Ward form”.

The regulator has a seam. Separate chart integrations can have interface terms; a physical seam defect can have a displacement/stress insertion when the seam moves. These cancel or vanish only after matching. W2 acknowledges this. The defensible claim removes the radial shell, not every interface insertion.

This architecture needs no common coarse space between \(\mathcal K\) and \(g\mathcal K\): differentiate observables in one fixed measure and use transport at the endpoint. Conditioning to establish W1 uses that one measure's coarse space. This observation does not construct the lattice vector field at the seam or prove its continuum action on observables.

### 7.2 What W0–W3 must establish

**NOT-VERIFIED for the sphere regulator.** Source: UNIV55.md, “(W0) A selection-rule analysis”, “(W1) Source-inserted local bounds”, “(W2)”, “(W3)”, and “Correction to the last sentence”.

For the homogeneous flat-chart rotation component, an exact independent check supports the restricted selection rule. Let \(A=\Lambda^2\mathbb R^4\). Gauge-invariant dimension-four pure-gauge bilinears lie in \(\operatorname{Sym}^2 A\). Enumerating all \(2^4\,4!=384\) signed permutation matrices, independently of the target's runner, gives

\[
 \langle\chi_A,\chi_{\operatorname{Sym}^2A}\rangle_{H_4}=0,\qquad
 \langle1,\chi_{\operatorname{Sym}^2A}\rangle_{H_4}=1,\qquad
 \langle\det,\chi_{\operatorname{Sym}^2A}\rangle_{H_4}=1.
\]

The exact formulas used were

\[
 \chi_A(h)=\frac{(\operatorname{tr}h)^2-\operatorname{tr}(h^2)}2,\qquad
 \chi_{\operatorname{Sym}^2A}(h)=\frac{\chi_A(h)^2+\chi_A(h^2)}2 .
\]

Inversion also excludes an odd-dimensional local monomial in this rotation representation under these symmetry assumptions. This verifies the algebraic rule, not the full renormalized operator expansion on a sphere.

A varying coupling, chart/curvature data, and the seam supply extra coefficients and reduce the regulator's exact symmetries. In stereographic coordinates,

\[
 \nabla_g\cdot v=0,\qquad \partial_\mu v^\mu=-4v(\log\Omega).
\]

Thus the chart dilation term uses coordinate divergence, not the vanishing metric divergence. Its trace-anomaly contribution must be combined with variation of the coupling profile and insertion renormalization. The two-loop local scale rule is not a nonperturbative proof that the residual coefficient is \(c_4=O(g_{\rm bare}^2)\). That is a Λ-matching/source-renormalization obligation. Pure background constants disappear in covariances; operator-valued residuals do not.

The corrected total-covariance argument for W1 is sound. Let \(J_{d,a}(x)\) be a specified renormalized insertion of dimension \(d=4,6\), and \(O_s\) an observable along the rotation path. Sufficient bounds are

\[
 \sup_{a,x,V}|E[J_{d,a}(x)\mid V]|\leq A_{d,R},\qquad
 \sup_{a,x,V,s}|\operatorname{Cov}(O_s,J_{d,a}(x)\mid V)|
 \leq B_{d,R,O}.
\]

Then, exactly,

\[
 |\operatorname{Cov}(O_s,J_{d,a}(x))|
 \leq B_{d,R,O}+2\|O\|_\infty A_{d,R}.
\]

No coarse-law decay appears. At fixed \(R\), the counting argument needs only a uniform conditional covariance bound; conditional decay is one possible way of proving it. A bounded-curvature interpolator does not establish these conditional **quantum insertion** bounds. BFT-3 concerns derivatives of a small-field critical background, not this full quantum covariance. Large fields and renormalized contact terms remain. Positive flow time helps observable regularity but is not a theorem bounding every mixed insertion.

W2 must give a **vanishing total seam contribution**, or a bounded renormalized seam insertion multiplied by a vanishing coefficient. Boundedness alone produces an area-sized error, not \(o(1)\). W3 needs an expectation estimate uniform along the group path, including flow normalization, rotated-loop discretization, and source/contact mixing. Smooth-background Taylor consistency alone does not suffice.

### 7.3 Precise conditional Ward implication

**CONFIRMED conditionally.** Source: UNIV55.md, “Normalization (precision on the fixed-R bound)” and “What it avoids”.

Assume the finite-cutoff vector field is constructed, endpoint transport holds, and its action on \(O_s\) agrees with the group derivative up to an expectation error \(\varepsilon_{a,R,O}\to0\), with a consistent sign convention. Suppose the expansion of \(\mathfrak W\) uses physical quadrature weights of bounded total volume, has

\[
 a^2\|c_{6,a}\|_\infty\to0,\qquad \|c_{4,a}\|_\infty\to0,
\]

satisfies the preceding conditional insertion bounds, and has total seam/remainder covariance \(s_{a,R,O}\to0\). Writing \(C_{d,R,O}=B_{d,R,O}+2\|O\|_\infty A_{d,R}\), integration along a fixed finite group path yields

\[
 |\omega_{\mathcal K}(O)-\omega_{g\mathcal K}(O)|
 \leq \varepsilon_{a,R,O}+s_{a,R,O}
 +C_R\operatorname{Vol}(S_R^4)
 \left[a^2\|c_{6,a}\|_\infty C_{6,R,O}
       +\|c_{4,a}\|_\infty C_{4,R,O}\right]\to0 .
\]

The estimates must hold uniformly along the path. Constants may depend on fixed \(R\). This proves the intended implication without a coarse-decay estimate or a common grid. W0–W3 are not established, and the geometry supplies neither the small coefficients nor the insertion bounds. The fixed torus lacks this global rotation Killing field; that does not prove that every possible proof of UNIV-T must use a common grid.

## 8. Zero seam, transparency, and non-freeness

**CONFIRMED: exact factorization and the need for an additional matching condition.** Source: UNIV55.md, locating strings “V12”, “β_p = 0 every crossing plaquette”, and “an additional UV input, N5”; original witness: CODEX_REVIEW_P4.md, “RP does not establish a transparent seam”.

With zero crossing weights and no other crossing interactions,

\[
 e^{-S}=e^{-S_-}e^{-S_+},\qquad
 d\mu=d\mu_-\,d\mu_+\,dH_{\rm crossing}.
\]

The unused Haar variables integrate to one. Gauge-invariant observables supported in opposite interiors are independent at every cutoff, consistently with reflection positivity. If a hemisphere/bulk limit has a nonzero connected correlation between separated supports that a rotation moves to opposite sides, that correlation witnesses seam visibility. Nonnegative crossing weights and bulk operator counting do not prove transparency.

The interface can carry two independent boundary connections and a matching transporter \(h\mapsto u_-hu_+^{-1}\). With \(D_i h=\partial_i h+A_i^-h-hA_i^+\), the expression \(\operatorname{tr}((D_i h)^\dagger D_i h)\) is gauge invariant and reflection even. Counting only bulk operators of an already continuous connection misses it. An appropriately chosen positive seam may still work. N5 is a reasonable UV target if it means a local matching estimate uniform in the conditional background; that estimate is additional work.

**REFUTED as a general implication: “non-free” forces a nonzero separated correlation.** Source: UNIV55.md, “Proviso to V12” and “any limit that is not ultralocal”.

Non-Gaussian ultralocal laws exist. On the compact sphere take a Poisson random measure with independent equally likely marks \(\pm1\) and intensity \(\lambda\,d\mathrm{vol}\). Its exact characteristic functional is

\[
 E e^{i\Phi(f)}
 =\exp\left\{\lambda\int(\cos f(x)-1)\,d\mathrm{vol}(x)\right\}.
\]

Disjoint regions are independent, but \(\kappa_4(\Phi(f))=\lambda\int f^4\ne0\) for nonzero real \(f\). The law is non-Gaussian and isometry invariant. Independence of reflected halves gives the RP form \(|EF|^2\geq0\). This is not a Yang–Mills model; it shows that the seam witness needs a nonzero **separated** correlation, not merely non-freeness. The earlier P4 review already used the correct qualification.

## 9. Theorem U: conditional proof and missing quantifiers

**CONFIRMED with corrected \(p>2\), a quantitative AF envelope, a closed marginal/irrelevant norm decomposition, and the observable/seam hypotheses. NOT-VERIFIED as a construction satisfying them.** Source: UNIV55.md, locating strings “Theorem U (CONDITIONAL)”, “Correction to the proof in 3.1”, and “So (N1) must be stated with p > 2”.

A weighted norm gives a simpler proof than the loop-gain absorption. Write \(0<\lambda=L^{-\kappa_E}<1\) and suppose the nonnegative norms satisfy

\[
 d_{j+1}\leq\lambda d_j+Cg_j^p m_j,\qquad
 m_{j+1}\leq(1+Cg_j^4)m_j+Cd_j .
\]

Set \(A=C/(1-\lambda)\) and \(z_j=m_j+A d_j\). Since \(C+A\lambda=A\),

\[
 z_{j+1}\leq(1+Cg_j^4+ACg_j^p)z_j,
 \qquad
 z_n\leq z_0\exp\left(C\sum_jg_j^4+
                  \frac{C^2}{1-\lambda}\sum_jg_j^p\right).
\]

Uniform boundedness of the two sums propagates \(m_0+d_0=o(1)\) over the growing number of levels. The abstract recurrence needs no loop-gain assumption \(G<1\), nor absorption of unspecified “early levels”.

For example, the explicit envelope

\[
 g_j^2\leq(g_*^{-2}+B(n-j))^{-1},\qquad B>0,
\]

implies for \(q>2\)

\[
 \sum_{j=0}^{n}g_j^q
 \leq g_*^q+\frac{2g_*^{q-2}}{B(q-2)}.
\]

This follows by comparing the decreasing function \((g_*^{-2}+Bx)^{-q/2}\) with its integral. With \(B=2\beta_0\log L\), it reproduces the manuscript's constants for \(q=p,4\).

The literal L1-FLOW entry, “the effective coupling stays ≤ γ at every scale”, is weaker than this envelope. A small upper bound alone permits arbitrarily long nearly constant-coupling segments, so the product need not be bounded uniformly in \(n\). The correction's AF asymptotics must be supplied as a uniform inequality, not a formal \(\approx\). Reading the correction as adding this hypothesis makes the intended implication valid.

The \(p>2\) correction is substantive. For \(p=2\), \(\lambda=1/2\), \(C=1\), \(A_0\) a positive integer, and \(g_j^2=(A_0+n-j)^{-1}\), take equality in the recurrence, \(d_0=0\), and \(n=2m\). Positivity yields

\[
 m_{j+2}\geq(1+g_j^2)m_j,\qquad
 m_{2m}\geq m_0\prod_{k=1}^{m}
                  \left(1+\frac1{A_0+2k}\right).
\]

The product diverges by the harmonic-series comparison for its logarithm. Choosing \(m_0\) as its reciprocal gives initial error tending to zero but \(m_{2m}\geq1\). This refutes the uncorrected abstract uniform-propagation argument. It does not prove failure of every \(p\leq2\) Yang–Mills comparison: faster initial decay, cancellations, or a different norm could change the conclusion.

The remaining conditional steps are valid: the common-scale norm must dominate the logarithmic density difference per block on real fields, with every marginal component included; N3 extends that control to all coarse configurations; N4 gives conditional observable comparison; fixed \(N_b\) and Proposition T give UNIV-T. The sphere version also needs the curved/profile variants and a specified N5 seam.

These assumptions contain the main unproved two-theory comparison. They are not consequences of BFT, the one-theory RLF target, or E7 as quoted. No OS0, OS2, OS3, determining-algebra theorem, or non-free witness follows from this induction alone.

## 10. Evidence and scope of the negative findings

One review pass incorporated all target errata. The only artifact written was this report. No git command, source fix, audit-status operation, or second output file was used.

Decisive checks were the displayed proofs and counterexamples. In-memory Python with integers and fractions.Fraction checked all 384 hypercubic character values, exact orthogonality of the \(3/5,4/5\) rotation, the exponent \(10/3\), and the Gaussian-rescaling identity at integer controls \(n=2,\ldots,19\). General claims rest on the analytic proofs, not those finite controls. No floating-point computation, Yang–Mills simulation, RG runner, or formal proof checker was used.

Source identities at the post-read check:

| Source | SHA-256 |
|---|---|
| UNIV55.md | 62033ebd7f6928261b8262616c9437bb22c4bca5179d645ed2b5119268ca8609 |
| CODEX_REVIEW_P4.md | 12d59c044e86af2fe66806332aed9a2e98181409e075151a983c4b4eeb7d1b34 |
| PROOF.md | f8337f4a90d24bbc74e1e300dbaf2c4ac59596c4e8506d2dd986d7ea6f8b587c |
| REVIEW_S22.md | e7df10f9dc13220399896e320ece04de19b3f9d6b9865062d1723ab5cc20341f |
| ROTDEF.md | 413261674aaafa7c68793e9f10ebc1421fdf92871bd583f7c654981511104bf2 |

The target and P4 hashes match the pre-stated identities. Findings use only the inspected supporting passages, not complete verification of the larger supporting files. The workflow, mathematical-review, proof-obligation, and negative-claim scope rules were read. No repo-wide framework primitive is used to establish a Yang–Mills estimate.

The incidental Gantumur publication metadata was checked against the primary [arXiv v2 page](https://arxiv.org/abs/2512.22072v2) and [v3 page](https://arxiv.org/abs/2512.22072v3), which lists JHEP 07 (2026) 036. The paper's full arguments and the target's extended regulator assessment are outside the eight requested attacks and are not certified here. No remembered literature assertion is an unmarked proof premise. The target's unverified Wilson-line self-energy and semiclassical inputs retain their [m] qualification.

The negative-claim discipline is restricted to the actual witnesses:

| Check | Scope retained |
|---|---|
| Alternatives | Fixed-ratio common-grid blocking, diverging-ratio blocking, a weighted-law comparison, a sphere Ward proof, and tuned seam matching remain possible. No general no-go or five-route exclusion is claimed. |
| Dependence | Seam matching and source estimates enter both architectures; their independence is not asserted. |
| Hidden hypotheses | Conditional locality, marginal-coordinate normalization, the AF envelope, branch/sector data, and separated-correlation witnesses are explicit. |
| Matching | Two-phase and Gaussian examples test abstract implications. The zero seam belongs to the admitted regulator class. None is a counterexample to Yang–Mills existence. |
| Resolution | Fixed cutoff, fixed volume, arbitrary coarse background, and decompactification are distinct. |
| Partial closure | Repairs are mathematical estimates or sharper statements, not demands for new physical axioms. |
| Surviving route | The conditional Ward estimate and weighted RG induction are concrete sufficient mechanisms. |
| Prior review | P4 already supplied the uniform-density mechanism and correctly qualified seam witness. Its missing quantum comparison is not closed by geometric interpolation. |

This is not a formal no-go packet and assigns no claim-audit status.

## 11. Exactly what may be banked; judgment on the sphere route

The bankable results are:

1. **Proposition T and its fixed-volume polymer consequence**, including the unnormalized-partition-function formulation. Source: UNIV55.md, “Proposition T” and “E5”.
2. **The final soft-kernel lower bound, positive probability of positive-Haar-measure coarse large-field sets, and the disjoint-plaquette growing-volume bound**, with fixed final strength. Source: UNIV55.md, “Well-posedness of sup_V” and “probability → 1 as R grows”.
3. **The response identity and the two-phase obstruction to arbitrary uniform bounds from per-block smallness alone**, without the alleged necessity of decay. Source: UNIV55.md, “The exact point where infrared information enters”.
4. **Rational-grid periodicity and the dense \(O(4)\) subgroup lemma**, with a continuous action required on the eventual state space. Source: UNIV55.md, “Group lemma, now re-derived”.
5. **Bounded-curvature interpolation of coarse edge holonomies on a regular grid**, by the tube construction, also for U(1) and SO(3). This gives no RG background or partition-function estimate. Source under review: UNIV55.md, “every coarse configuration admits an interpolating connection”.
6. **The instanton exponent's arithmetic and its integral under the assumed size model**, without a lattice probability bound. Source: UNIV55.md, “11N/3 − 4 > 0”.
7. **The finite-lattice Ward identity, absence of the radial-cutoff shell on a closed sphere, and the conditional fixed-radius Ward implication**, retaining seam and observable defects. Source: UNIV55.md, “Ward identity on S^4_R” and “Normalization (precision on the fixed-R bound)”.
8. **Zero-seam factorization and the need for additional matching**, with a separated-correlation witness required to demonstrate nontransparency in a limit. Source: UNIV55.md, “V12”.
9. **Theorem U's abstract induction with summable AF coefficients and complete norm/observable hypotheses**, proved above by a weighted norm. Source: UNIV55.md, “Correction to the proof in 3.1”.

**Judgment: the sphere route can conditionally make fixed-radius symmetry restoration a UV comparison problem; UNIV55 has not established that OS1 on \(\mathbb R^4\) is now a purely ultraviolet question.** Source: UNIV55.md, “Its UV status is settled as a reduction”, “W0-W3”, and “S5's radius-uniform local bounds”. Absence of angular-momentum flux at infinity is a real geometric advantage. A proof still needs all-background conditional/source control, nonperturbative local Λ-matching, and a transparent seam, followed by a common determining local algebra and radius-uniform bounds permitting decompactification and symmetry transport. No coarse correlation-decay theorem is logically forced by the two sufficient mechanisms proved here; neither has been implemented for this Yang–Mills regulator. OS0–OS3 and non-freeness remain unproved. This is a viable conditional route, not a completed ultraviolet resolution of OS1.

