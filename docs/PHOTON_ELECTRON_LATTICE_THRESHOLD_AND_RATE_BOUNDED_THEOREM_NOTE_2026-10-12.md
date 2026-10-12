---
claim_id: photon_electron_lattice_threshold_and_rate_bounded_theorem_note_2026-10-12
claim_type: bounded_theorem
runner: scripts/photon_electron_threshold_and_rate_2026_10_12.py
upstream_dependencies: []
claim_scope: "Exact two-body threshold and leading pair-creation coefficient for supplied continuous-time Maxwell and massive sine-Dirac lattice symbols; conditional observation comparisons, with no empirical exclusion or native physical identification."
---

# Pair thresholds and rates for supplied photon and electron lattice laws

Status: proposed_retained

**Type:** bounded_theorem

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
conditional_surface_status: conditional-support
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "The mathematical conclusions retain explicitly supplied symbols, Hilbert space, vacuum, normalization and interaction; observational applicability remains open."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Test a species-resolved completion and control relative renormalized speeds before a detector-level joint inference."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Target, premises and result

**Exact target:** for the two supplied lattice dispersions below, compute the global two-particle energy threshold on the momentum torus and the leading, canonically normalized pair-creation rate at its onset.

This is conditional mathematics of a candidate effective law. Its strongest result is the exact one-dimensional variational formula (1), the angular envelope (4), and the positive onset coefficient (9). These results reduce an inverse problem's ambiguity; they do not select a microscopic theory from observations.

Use dimensionless crystal momenta in \(\mathbb T^3=(-\pi,\pi]^3\), continuous Hamiltonian time, additive energy and crystal momentum, and positive mass \(\mu\). Supply

\[
 \omega(k)=2\sqrt{\sum_i\sin^2(k_i/2)},\qquad
 \epsilon(p)=\sqrt{\mu^2+\sum_i\sin^2p_i}.
\]

Physical energies are \(\Lambda\omega,\Lambda\epsilon\); \(\mu=m/\Lambda\), with \(m=m_ec^2\) an external calibration. The effective length \(\ell=\hbar c/\Lambda\) is an unknown of this supplied completion, not a refit of the approved framework scale-reference primitive. Identifying the two lengths would be a further conditional specialization. Equal limiting speeds, an electron interpretation, and the continuous time symbol are supplied choices.

For the rate also supply four-component canonical fermions, a filled negative band, and the minimally coupled hopping Hamiltonian

\[
 H_f=\sum_x\mu\psi_x^\dagger\beta\psi_x+
 \frac1{2i}\sum_{x,i}
 [\psi_x^\dagger\alpha_i e^{ieA_{x,i}}\psi_{x+i}-\mathrm{h.c.}],
\]

where the \(\alpha_i,\beta\) obey the Dirac Clifford relations. Use the canonical transverse photon Hamiltonian \(H_\gamma=\frac12\sum(\Pi^2+\omega^2 A^2)\), \([A,\Pi]=i\), and single-photon link Fourier coefficient \(1/\sqrt{2\omega V}\). The calibrated coupling \(e\) refers to this normalized field. A frequency alone would not fix this coefficient: \(\frac12(Z\Pi^2+\omega^2 A^2/Z)\) has the same frequency and a different field matrix element.

Strictly positive rate requires \(e\ne0\). At zero interaction the same kinematic opening has zero pair-creation rate; equations (8)-(10) retain this factor explicitly.

The rate calculation also supplies the usual squared-amplitude transition rule and its infinite-volume, long-time golden-rule coefficient. Neither that probability rule nor a detector's event interpretation is derived from the registered realized-state primitive. This is an effective quantum calculation with those rules exposed as inputs.

The primitive registry and all source notes at revision `a13caa4885f547c8d206265b031ba7649e539fd9` were checked. The approved scale ruler, structural kinetic isotropy and realized-state slot retain their actual meanings. None is reclassified as an unapproved premise. The Hamiltonians, physical particle/vacuum identifications and observational response above are explicit conditional suppliers, not conclusions attributed to those primitives.

The finite comparison grammar was fixed before numerical threshold searches: relativistic dispersion, this sine-Dirac/Maxwell pair, and the same photon with a common-Laplacian electron \(\epsilon_L(p)=\sqrt{\mu^2+\omega(p)^2}\). Public headline data were already known. No blind validation is claimed.

## Exact global minimization

Put \(S=\sum_i\sin^2(k_i/2)\), \(G=4S\). The following first formula holds on the full torus, with \(\mu>0\):

\[
 E_{\min}(k,\mu)^2
 =\min_{0<z\le1}\frac{4\mu^2+2\sum_i[1-\sqrt{1-z\sin^2 k_i}]}z.
 \tag{1}
\]

To prove it, use \((A+B)^2=\min_{0<t<1}(A^2/t+B^2/(1-t))\) for positive \(A,B\). Minimize jointly over \(p,t\). Each coordinate of the sine-square expression is a constant minus a single sinusoid of \(2p_i\); its minimum is

\[
 \min_{p_i}\left(\frac{\sin^2p_i}{t}+\frac{\sin^2(k_i-p_i)}{1-t}\right)
 =\frac{1-\sqrt{1-4t(1-t)\sin^2k_i}}{2t(1-t)}.
\]

Set \(z=4t(1-t)\). The mass makes (1) diverge as \(z\downarrow0\), so the minimum is attained. This derivation includes noncollinear partitions and all reciprocal-lattice copies; no continuum collinearity theorem is imported.

For the rest of the threshold theorem fix nonzero \(k\) with every \(|k_i|<\pi/2\). Define

\[
 R(k)=\max_{0\le z\le1}R_z(k),\qquad
 R_z=zS-\frac12\sum_i[1-\sqrt{1-z\sin^2k_i}].
 \tag{2}
\]

Equation (1) gives \(E_{\min}<\omega\) exactly when \(\mu^2<R(k)\), with equality at \(\mu^2=R(k)\). This equivalence is about the supplied two-body spectrum, not photon survival in an instrument.

For an independent construction set \(p=k/2+q\), \(c_i=\cos k_i>0\), \(b_i=\sin k_i\),

\[
 T=\sum_i c_i\sin^2q_i,\quad
 C=\sum_i b_i\sin q_i\cos q_i,\quad
 X=\mu^2+S+T.
\]

The two squared energies are \(X+C,X-C\). Their product identity gives

\[
 [(\epsilon_p+\epsilon_q)^2-G][(\epsilon_p-\epsilon_q)^2-G]
 =4G[C^2/G-T-\mu^2].
 \tag{3}
\]

Here \(q\) on the energy subscripts denotes the other daughter. To fix the sign without a squaring ambiguity, reverse triangle on \((\mu,\sin p)\) and \((\mu,\sin(p-k))\) gives \(|\epsilon_p-\epsilon_q|<\omega\); positive mass makes equality impossible. Thus the second factor in (3) is negative.

Use \(C^2/G=\max_t(2tC-Gt^2)\) and maximize each \(q_i\) as a two-dimensional quadratic form. With \(u=4t^2\), the maximum is

\[
 F(u)=\frac12\sum_i[\sqrt{c_i^2+ub_i^2}-c_i]-Gu/4=R_{1-u}.
\]

It is strictly concave. Its derivative is positive at zero and negative at one: four times these derivatives are respectively \(\sum(1-c_i)^2/c_i\) and \(-\sum(1-c_i)^2\). The unique maximizer \(u_*\in(0,1)\) solves \(\sum b_i^2/\sqrt{c_i^2+u_*b_i^2}=G\). Threshold momenta are

\[
 p_*=k/2\pm q_*,\qquad
 (q_*)_i=\tfrac12\arctan(\sqrt{u_*}\tan k_i),
\]

together with independent \(\pi\) shifts. In general they are not collinear. Equal sharing instead gives \(2\sqrt{\mu^2+G/4}>\omega\) and misses the channel. For \(k=rn\), \(\sum n_i^2=1\), let \(A_4=\sum n_i^4\). Then \(R=r^4A_4/64+O(r^6)\), and the leading daughter fractions are \((1\pm1/\sqrt2)/2\).

The asymmetric leading threshold is known Lorentz-violation physics. Substitution of \(\xi=-A_4/12,\eta=-A_4/3\) into [Jacobson, Liberati and Mattingly, hep-ph/0209264v2](https://arxiv.org/abs/hep-ph/0209264v2), section III.C, equation (42), reproduces it. The contribution here is the finite-symbol reduction, explicit bounds and stated interaction checks; no priority claim is made.

## Error control, angular extrema and a comparator

For \(d_i(z)=\sqrt{1-zb_i^2}\), rationalize (2):

\[
 R_z=z(1-z)\sum_i
 \frac{(1-c_i)b_i^2}{2(d_i+c_i)(1+d_i)}.
\]

Since \(c_i\le d_i\le1\), evaluation at \(z=1/2\) for the lower bound and \(z(1-z)\le1/4\) for the upper give

\[
 \frac1{16}\sum_i(1-c_i)^2\le R(k)
 \le\frac1{16}\sum_i\frac{(1-c_i)^2}{c_i}.
\]

If \(\varepsilon=\max|k_i|<\pi/2\), Taylor inequalities yield the uniform directional estimate

\[
 \frac{\sum k_i^4}{64}(1-\varepsilon^2/12)^2
 \le R(k)\le\frac{\sum k_i^4}{64\cos\varepsilon}.
\]

For fixed photon energy parameter \(0<S<1/2\), write \(v_i=\sin^2(k_i/2)\). The function \(f_z(v)=1-\sqrt{1-4zv(1-v)}\) has
\(f_z''=4z(z-1)/[1-4zv(1-v)]^{3/2}\le0\). Concavity and \(f_z(0)=0\) give \(f_z(S)\le\sum f_z(v_i)\le3f_z(S/3)\). Hence equal components minimize (2), and an axis maximizes it. For \(d\) equal nonzero components direct maximization gives

\[
 R_d(S)=\frac{S^2}{4(d-S)},\qquad
 \frac{S^2}{4(3-S)}\le R(k)\le\frac{S^2}{4(1-S)}.
 \tag{4}
\]

For \(E=2\Lambda\sqrt S\) the equal-component threshold is

\[
 \Lambda_d(E)^2=\frac{E^2}{4d}+\frac{E^4}{64dm^2}.
 \tag{5}
\]

The common angular domain requires \(\Lambda>E/\sqrt2\). At (5) it requires \(E>4\sqrt{2d-1}\,m\); a single equal-component direction only requires \(E>4m\). Within the common domain, two-body kinematic stability in some orientation requires \(\Lambda\ge\Lambda_1/\sqrt3\), and \(\Lambda\ge\Lambda_1\) suffices for all orientations. No confidence level is attached to this mathematical envelope.

For the common-Laplacian comparator, let \(f_i(p)=e^{ip_i}-1\). The identity \(f(p+q)=f(p)+\mathrm{diag}(e^{ip_i})f(q)\) proves \(\omega(p+q)\le\omega(p)+\omega(q)\) on the full torus. A second triangle inequality on the two-vectors \((\mu,\omega(p))\), \((\mu,\omega(q))\) gives the exact positive gap

\[
 \epsilon_L(p)+\epsilon_L(k-p)\ge\sqrt{4\mu^2+\omega(k)^2}>\omega(k).
 \tag{6}
\]

This comparison concerns exactly this two-body dispersion family. It says nothing about other interactions, final states or other lattice completions. The relativistic null has the corresponding timelike triangle inequality. These comparators demonstrate that identical photon timing symbols can coexist with different pair thresholds.

## Interaction and normalization

The link midpoint convention gives the one-photon vertex, with \(e\) factored out,

\[
 V_\lambda=\sum_i\epsilon_{\lambda i}\alpha_i\cos(p_i-k_i/2),\quad
 \sum_i2\sin(k_i/2)\alpha_i\cos(p_i-k_i/2)=h(p)-h(p-k),
\]

where \(h(p)=\alpha\cdot\sin p+\mu\beta\), and \(\epsilon_\lambda\) is a real unit vector transverse to \(\hat k_i=2\sin(k_i/2)\). Put \(s=\sin p,t=\sin(k-p),a_i=\epsilon_{\lambda i}\cos(p_i-k_i/2)\). The rank-two projectors yield

\[
 \mathcal S_\lambda=\mathrm{tr}(P_+(p)V_\lambda P_-(p-k)V_\lambda)
 =|a|^2\left[1+\frac{\mu^2-s\cdot t}{\epsilon_p\epsilon_q}\right]
 +\frac{2(s\cdot a)(t\cdot a)}{\epsilon_p\epsilon_q}.
\]

This follows by expanding the projectors, using vanishing odd Clifford traces and \(\mathrm{tr}(\alpha_i\alpha_j\alpha_l\alpha_m)=4(\delta_{ij}\delta_{lm}-\delta_{il}\delta_{jm}+\delta_{im}\delta_{jl})\), with \(\beta\) anticommuting with each \(\alpha_i\). Reflect \(t\) perpendicular to \(a\): \(t'=t-2(\hat a\cdot t)\hat a\). Cauchy on \((\mu,s),(\mu,t')\) proves

\[
 \mathcal S_\lambda\ge\frac{2\mu^2|a|^2}{\epsilon_p\epsilon_q}>0
 \quad(\mu>0,\ a\ne0).
 \tag{7}
\]

Golden rule and the supplied \(1/\sqrt{2\omega V}\) matrix element give the width coefficient

\[
 \Gamma_\lambda=\frac{e^2}{8\pi^2\omega}
 \int_{\mathbb T^3}d^3p\,\mathcal S_\lambda
 \delta_D(\omega-\epsilon_p-\epsilon_q).
 \tag{8}
\]

Indeed \(2\pi(e^2/(2\omega V))\sum_p\) becomes \(e^2/(8\pi^2\omega)\int d^3p\). Final spin sums are already in the projectors; an unpolarized photon averages the two \(\lambda\) values. There is no further identical-particle factor for the electron and hole. Every independent \(\pi\) shift of \(p\) flips matching components of \(s,t,a\), preserving the entire integrand. Thus the full torus integral is eight times that over one cell of side \(\pi\). At small momentum these are **eight charged Dirac species**. Retaining only the central contribution is a partial width, not a physical removal of doublers.

## Exact threshold onset and a controlled order of limits

Fix nonzero \(k\) in the stated central cube, let \(\mu_*^2=R(k)\), and take \(\delta=R(k)-\mu^2\downarrow0\). Define \(D_i=\sqrt{c_i^2+u_*b_i^2}\), \(v_i=b_ic_i/D_i\), and

\[
 K=2\mathrm{diag}(D_i)-2vv^T/G.
\]

This is the negative Hessian of \(C^2/G-T\) at either threshold optimizer. Stationarity gives

\[
 G-\sum_i v_i^2/D_i=u_*\sum_i b_i^4/D_i^3>0,\qquad
 \det K=8\Bigl(\prod_iD_i\Bigr)\frac{u_*}{G}\sum_i b_i^4/D_i^3>0.
\]

The rank-one criterion proves positive definiteness, including zero components of \(k\). There are two exchanged minima per \(\pi\) cell and sixteen on the full torus. At threshold \(\epsilon_\pm=\sqrt S(1\pm\sqrt{u_*})\). Put \(A=1/[\sqrt S(1-u_*)]\). Identity (3) yields locally
\(\omega-\epsilon_p-\epsilon_q=A[\delta-y^TKy/2]+\) higher-order terms. The complement of these finitely many neighborhoods has a positive gap by compactness. A smooth change to quadratic coordinates therefore gives a coarea integral \(4\pi\mathcal S_*\sqrt{2\delta}/(A\sqrt{\det K})+o(\sqrt\delta)\) per minimum.

Since \(|(q_*)_i|<\pi/4\), no cosine weight vanishes, and (7) makes every real transverse polarization's coefficient positive. With \(\overline{\mathcal S}_*\) the polarization average at threshold, the central-cell result is

\[
 \Gamma_0=
 \frac{2\alpha(1-u_*)\overline{\mathcal S}_*\sqrt{2\delta}}
 {\sqrt{\det K}}+o(\sqrt\delta),\qquad
 \Gamma_{\mathbb T^3}=8\Gamma_0,
 \quad\alpha=e^2/(4\pi).
 \tag{9}
\]

For a single axis \(k=(\kappa,0,0)\), the coefficient of \(\sqrt\delta\) in \(\Gamma_0\) simplifies to \(\alpha\sqrt{2(1-\cos\kappa)/[(1+\cos\kappa)(1+3\cos\kappa)]}\). Equation (9) is at fixed nonzero momentum. Its remainder is not asserted uniform as \(k\to0\).

A separate scaling limit takes \(k=rn\), \(\mu=r^2\sqrt{A_4}/(8\sqrt\chi)\), and fixed finite \(\chi>1\), then \(r\to0\). With \(p=xk+l\), \(l\perp n\), \(l=O(r^2)\), \(w=x(1-x)\), the leading shell and spin average are

\[
 |l|^2=\mu^2[16\chi w(1-4w)-1],\qquad
 \overline{\mathcal S}=
 \frac{\mu^2+|l|^2(1-2w)}{2w^2r^2}+o(r^2).
\]

Integrating the transverse delta in (8) gives

\[
 \Gamma_0=\frac{\alpha\mu^2}{2r}I(\chi)+o(\mu^2/r),\quad
 I=16\chi\left[t^3/6+t^5/10+t/(8\chi)\right]_{t_-}^{t_+},\quad
 t_\pm^2=\frac{1\pm\sqrt{1-1/\chi}}2.
 \tag{10}
\]

To justify the shell, its allowed \(x\) set consists of two bounded open intervals. On compact interior subintervals the transverse radius and derivative are nonzero, so the implicit function theorem continues the exact shell. Endpoint contributions are integrable; for fixed \(\chi>1\) the roots are simple and separated, permitting the rescaled coarea limit. This establishes a positive coefficient without a claim about an arbitrary joint limit. Only after taking (10) may one write \(I\sim4\sqrt2\sqrt{\chi-1}\). No uniform interchange with \(\chi\downarrow1\), \(\chi\to\infty\), or finite coupling is asserted. The massless limit lies outside (9); it is not used to infer survival.

The primary rate literature [Rubtsov, Satunin and Sibiryakov, arXiv:1204.5782v1](https://arxiv.org/abs/1204.5782v1), section 3.1, equations (12)-(16), treats related continuum effective theories and distinguishes modified vertices from kinematics. It is a comparator; the lattice vertex and normalization above were derived explicitly.

## Observation map and candidate comparison

The [input record](../data/photon_electron_inverse_2026_10_12/observations.json) pins versions, downloaded-byte hashes, exact source items, units, roles and uncertainty meanings. The [runner](../scripts/photon_electron_threshold_and_rate_2026_10_12.py) writes [finite controls and conditional envelopes](../outputs/photon_electron_inverse_2026_10_12/results.json). No raw-count likelihood or detector response is reconstructed.

The same candidate photon law has \(v_i/c=\sin k_i/\omega\). With \(v_i^{(s)}=\sin^2(k_i/2)\) and \(S=\sum_i v_i^{(s)}\), direct differentiation gives
\[
 |v|^2/c^2=\frac{\sum_i4v_i^{(s)}(1-v_i^{(s)})}{4S}
 =1-\frac{\sum_i(v_i^{(s)})^2}{S}.
\]
For \(k=rn\), the ratio on the right is \(r^2A_4/4+O(r^4)\), while \(E/\Lambda=r+O(r^3)\). Taking the square root proves \(1-|v|/c=A_4E^2/(8\Lambda^2)+O((E/\Lambda)^4)\). Matching the timing convention \(1-v/c=3E^2/(2E_{\mathrm{QG},2}^2)\) gives \(E_{\mathrm{QG},2}=\sqrt{12}\Lambda/\sqrt{A_4}\). This short calculation makes the present argument self-contained; it repeats the established [repository timing result](PHOTON_DISPERSION_OBSERVATIONAL_CONSTRAINTS_AND_LIVE_FORMATION_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-24.md), which is contextual prior art, and is not a new contribution. The group-ray direction differs from crystal-momentum direction at higher order; angular envelope (4) does not require identifying them. FLRW transport, a lattice frame along the path and source timing remain supplied in a cosmological use.

The primary [LHAASO timing paper v3](https://arxiv.org/abs/2402.06009v3), revised 2026-02-13, Table 1 ML MINOS row gives the quadratic subluminal lower scale \(6.9\times10^{11}\) GeV. It agrees with the v2 value previously used in the repository. Alternative CCF and calibrated rows are not independent measurements. The bound depends on the paper's source, detector, EBL and cosmological model.

The primary [LHAASO survival paper v2](https://arxiv.org/abs/2106.12350v2), revised 2026-01-10, Table I reports 95% lower cutoff summaries \(1.14\pm0.06\) PeV for J2032+4102 and \(0.75\pm0.043\) PeV for Crab, where the quoted errors describe systematics of the bounds. They are not event-energy standard deviations. The paper fits reconstructed showers with source spectra and an assumed sharp cutoff. Its printed equation (2) has \(H(E-E_{\rm cut})\), apparently reversed relative to the text and infinite-cutoff null; this work transcribes the table and does not claim to reproduce that likelihood.

Using the current [NIST 2022 CODATA database](https://physics.nist.gov/cuu/Constants/Table/allascii.txt), \(m=0.00051099895069(16)\) GeV, the conditional arithmetic is:

| Published energy summary used as comparator | Axis \(\Lambda_1\) | Necessary \(\Lambda_1/\sqrt3\) for some orientation |
| --- | ---: | ---: |
| J2032, 1.14 PeV | \(3.1791\times10^{14}\) GeV | \(1.8354\times10^{14}\) GeV |
| Crab, 0.75 PeV | \(1.3760\times10^{14}\) GeV | \(7.9442\times10^{13}\) GeV |
| Timing scale conversion | \(1.9919\times10^{11}\) GeV | \(1.1500\times10^{11}\) GeV |

The first two rows are sensitivity envelopes under a supplied kinematic-stability premise, **not new 95% constraints**. At J2032's quoted systematic endpoints the necessary scale ranges from \(1.6473\) to \(2.0337\times10^{14}\) GeV. This is endpoint propagation, not a probability distribution. The mass uncertainty is negligible on that scale; correlations are not silently set to zero in a joint fit. With \(A=E^2/(4d),B=E^4/(64dm^2)\), the exact logarithmic sensitivities are \(\partial\log\Lambda/\partial\log E=(A+2B)/(A+B)\), \(\partial\log\Lambda/\partial\log m=-B/(A+B)\).

Under the tree matching, (10) converts to \(\Gamma_{0,E}=\alpha m^2I/(2E)\). At 1.14 PeV and \(\chi=1.05\), its central-species leading length is about 0.184 m; at \(\chi=1.5\), about 0.052 m. These are illustrative coefficients, not established exponential attenuation lengths of a physical photon. No near-threshold confidence margin is extracted from them.

The falsifiable correlation is explicit: at leading order, \(\chi=A_4E^4/(64m^2\Lambda^2)\), so a measured quadratic timing coefficient fixes the model's pair threshold once mass and direction are specified. For the same direction, kinematic stability at energy \(E_s\) implies \(1-v(E_t)/c\lesssim8m^2E_t^2/E_s^4\); unknown relative directions add at most the leading \(A_4\) ratio of three. This is a model consequence conditional on the bridge, not an independent prediction tested with already-used observations.

| Candidate | Shared photon timing | Pair-spectrum result | Present ranking |
| --- | --- | --- | --- |
| Relativistic null | Zero dispersion correction | Timelike positive gap | Preferred by parsimony among the tested descriptions; no fit improvement established for the alternatives |
| Sine-Dirac/Maxwell | One cutoff plus common orientation | (1)-(5), positive tree onset (9) | Conditional discriminator; eight charged species and speed matching unresolved |
| Common-Laplacian comparator | Same timing law | Positive gap (6) | Timing-degenerate with the preceding candidate; microscopic Dirac realization not supplied |

The extra cutoff and orientation are model choices; mass, charge, speed, species, vacuum and response are supplied. No BIC, Bayes factor or unique-law ranking is justified from one-sided published summaries. There are zero fitted datasets, zero blind validations and zero newly validated predictions.

## Exact remaining obligations and proof graph

The proof graph is: coordinate phasor minimization proves (1); strict concavity proves (2) and its unique threshold; the independent quadratic-form construction supplies the optimizer and Hessian; rationalization and concavity prove (4); Clifford traces and canonical oscillator normalization prove (7)-(8); the positive Hessian and local coarea argument prove (9); fixed-parameter rescaling proves (10). Each lemma is proved here. The finite runner checks these formulas through separate energy minimization, matrix projectors and exact-shell quadrature. No numerical search supplies the global quantifiers.

The strongest missing **physical** obligation is a renormalized, species-resolved realization whose photon/electron poles and detector response obey this same forward law across the measured energies. It is broader than the completed free-spectrum lemma; it has not been renamed as an almost-proved theorem. In particular:

- Gauge covariance alone does not enforce equal renormalized photon and electron speeds on this spatial lattice. Symmetry-allowed \(O(e^2r)\) self-energy terms can dominate the \(O(r^3)\) bare excess; their coefficient has not been computed here. Even matched speeds leave quartic corrections. [Collins et al., gr-qc/0403053v4](https://arxiv.org/abs/gr-qc/0403053v4) supplies a general warning, not a calculation of this Hamiltonian.
- Removing seven charged doublers requires changing the completion and recomputing its spectrum and vertex. A Wilson mass is an actionable alternative; this note does not rule it out.
- Atmospheric pair conversion, radiation and energy reconstruction can change under the same proposed law. The Coulomb-field calculation in arXiv:1204.5782v1, equations (31)-(40), uses additional sign and scale restrictions. Its photon-only suppression prescription cannot be copied into this two-sector model. A full source/propagation/detector likelihood is still needed.
- The finite-time kinetic approximation, source distance, possible cascades and orientation along the path remain inputs to attenuation. The present \(e^2\) coefficient does not establish a uniform interacting survival theorem.

Excluded mathematical endpoints are \(k=0\), the boundary \(|k_i|=\pi/2\) for the strict optimizer/Hessian result, and \(\mu=0\) for the onset statement. Formula (1) itself has the wider domain already stated. Equality has zero two-body phase space; finite rate margins must be handled separately.

## No-Go Discipline Gate

This packet addresses only the bounded two-body and tree-rate statements above. It makes no universal lattice, axiom-necessity or TOE impossibility claim. The checklist records actual attacks and leaves physical alternatives open. New proofs below are proposed evidence, not already ratified retained authority; no route is labeled `RULED OUT BY PRIOR`.

**N1 — Distinct attack routes.** The attack target is the composite conditional threshold/rate statement, not all microscopic laws.

| Family and marker | Concrete attack | Outcome and exact evidence |
| --- | --- | --- |
| Torus variational problem — ATTEMPTED | Noncollinear or reciprocal-lattice partitions might beat the threshold | Equation (1) minimizes every torus coordinate exactly; direct full-torus controls challenge the sign on both sides |
| Directional extremal problem — ATTEMPTED | A generic orientation might lie outside axis/body-diagonal extrema | Concavity of \(f_z\) proves (4) on the full fixed-S simplex |
| Finite-momentum remainder — ATTEMPTED | Higher sine terms might invalidate a leading-only boundary | Rationalized bounds and exact (5) retain the finite-symbol correction; the small-momentum coefficient is not used as an exact threshold |
| Spin selection and shell measure — ATTEMPTED | An energy channel might have a zero matrix element or zero-area shell | Reflection inequality (7), positive Hessian and coarea calculation prove a positive onset coefficient |
| Oscillator normalization and species counting — ATTEMPTED | Frequency-only normalization or omitted corners might change the rate | Canonical field matrix element is supplied explicitly; golden-rule factors and exact eightfold periodicity are checked separately from the spin inequality |
| Common-symbol countermodel — ATTEMPTED | The observed photon symbol alone might force the sine-Dirac pair result | Construction (6) is an explicit different completion with the same photon symbol; it defeats the broader uniqueness inference, which is not claimed |

The first five attack different mathematical obligations; the sixth is a surviving out-of-model alternative. It narrows physical interpretation rather than contradicting the stipulated-symbol theorem. This enumeration does not prove completeness of a physical search.

**N2 — Conditions and implications.** No count of independent physical walls is asserted. Treat source, propagation, detection and statistics together as the observational forward-model obligation, since a full inference must include them. For the remaining pairs, implication is unresolved rather than presumed absent:

| Pair | First closes second? | Second closes first? | Disposition |
| --- | --- | --- | --- |
| Native species realization / renormalized spectrum | unresolved | unresolved | keep named targets without an independence count |
| Native species realization / observational forward model | unresolved | unresolved | a field identification alone is not presented as a detector calculation |
| Renormalized spectrum / observational forward model | unresolved | unresolved | pole matching is not claimed to supply the observational likelihood |

**N3 — Hidden-condition scan.** “Canonical” names the explicitly supplied oscillator/fermion commutators and normalization; “vacuum” names the supplied filled band. “Physical,” “calibrated,” “FLRW” and “detector” identify explicit interpretation or extraction inputs. “Primitive” refers to the registry read, not a new supplier. No “standard QFT” shortcut supplies the spectrum, vertex or rate; those calculations are displayed. The continuum and weak-coupling orders of limits remain explicit.

**N4 — Residual matching.** No prior no-go is used as proof of this threshold. Jacobson equation (42) matches the leading quartic threshold only, not the exact torus result. Rubtsov section 3.1 concerns continuum rates, not this exact vertex; Collins concerns a generic radiative risk, not a computed coefficient here. The earlier repository timing note supplies provenance for timing, not a pair-survival theorem. None is counted as an exact negative witness against other completions.

**N5 — Resolution and rhetoric.** The negative boundary is limited to the specified two-body energies at a given mode, and the positive comparator gap is proved on the torus for that comparator. It is not a claim about every site process, every many-body block, or any interacting completion. Finite mode/projector/quadrature controls are executed; real-space source/detector and full interacting-lattice calculations are not. The primary runner prints these distinctions at all five required resolution classes.

**N6 — Partial closure and primitives.** The registered scale ruler, kinetic-form isotropy and realized-state slot were checked at the pinned source; they remain approved content. No new axiom is requested or declared necessary. Renormalization matching, a species-resolved completion or an explicit detector model could close parts of the physical target through ordinary mathematics and physics. A convention alone would not supply the missing calculation. The proposed identification is not silently ratified here.

**N7 — Steelman.** A hostile reviewer can keep the photon timing symbol while replacing the naive electron by a Wilson or other species-resolved action, changing the pair threshold and perhaps preserving PeV photons. They can also require a renormalized matching calculation before any free-shell rate is interpreted. The concrete next obligation is to derive that completion's full pair spectrum, interaction and detector-facing consequences. This is an open alternative to the broad inverse problem, so a universal exclusion is withdrawn. It is outside the fixed Hamiltonian of (1)-(10), not a refutation of that conditional calculation.

**N8 — Cross-cycle echo.** A scoped search of prior `NO_GO_LEDGER.md` files found the atomic massive-limit bridge's supplied mass/coupling distinction, the Born-scattering detector-centroid distinction, and the same-action Dirac-Kahler/OS distinction between transfer and central-time frequencies. These are not cited as current negative authorities or presumed still-audited grades. Their relevant repair mechanisms—explicit calibration, deriving the readout, and preserving the temporal symbol—are applied here as scope conditions. The current photon timing note already retains its physical transport suppliers. No similarly shaped prior wall is used to foreclose the present alternatives.

Packet disposition: scoped proposed mathematics with an open physical inverse problem; no five-route certificate of global physical impossibility is asserted. Independent milestone review must check the distinct-family and scope statements along with the proof.

## Review and reproducibility record

Author checks are distinct from independent checks. The initial threshold derivation was frozen at SHA-256 `e93937ca35136c42c7776ad8ca74abc5032249d2646c566d173967186349c12a`. A focused gpt-6-astra/max checker derived (1) by a different variational route before author exposure, then checked the supplement at `3ff2c897635b3be19672ece158d7054d915f031251f5d377bdf0abdf68aeecc8`. Its 30 pre-exposure and 9 post-exposure controls passed; the physical-domain qualification above incorporates its correction.

A separate focused gpt-6-astra/max checker derived the vertex, normalization and scaling integral before reading the rate draft at `e35807fa55d31c2a0db03b116c1b2db566a7c53d72a729b1963e4b8a882ac5d7`. It verified projectors against eigenspinors, all eight corners and finite position-space hopping. Its normalization and radiative cautions are incorporated. The further independent fixed-momentum onset check described below preceded extensive use of (9). These focused checks are neither ordinary milestone review nor formal audit.

The onset checker independently confirmed (9) against the draft at `f8520df52ab8efb66580415e1db1a02c7eef7c165c4eb311c8ea00ed21119164`. It caught an imprecise overlap statement: define \(\chi_{\rm exact}=R/\mu^2\) to obtain \(\delta=\mu^2(\chi_{\rm exact}-1)\) exactly. The leading \(\chi\) in (10) instead obeys \(\delta/\mu^2=\chi-1+O(r^2\chi)\); they cannot be substituted arbitrarily close to a finite-momentum threshold. The two limits above are kept separate. Its independent exact-shell checks covered oblique as well as axial momenta; these are checker evidence, distinct from this primary runner's axial rate controls.

Run `python3 scripts/photon_electron_threshold_and_rate_2026_10_12.py` for twelve threshold cases with direct torus minimization on both sides, fifty-six angular cases, fifty projector cases, eighteen exact-shell rate comparisons, a quadrature refinement and three hundred comparator samples. The analytic proofs carry the quantifiers. The author fixed-chi ratios converge toward one; the fixed-momentum threshold ratios are within about \(6.3\times10^{-5}\) of one at \(\delta/R=0.0003\). This is numerical convergence evidence, not an interval-arithmetic error certificate.

The six `--mutation` options independently alter threshold normalization, angular ordering, vertex phase, rate normalization, comparator mass or source energy units. Each was run and failed its actual mathematical/data assertion; no terminal forced-failure predicate substitutes for that check. Cache identity is managed through `scripts/runner_cache.py`, separately from those validity checks. No helper runner or dependency-policy edit is required. No formal audit, retention decision, observational fit or merge is part of this proposal.
