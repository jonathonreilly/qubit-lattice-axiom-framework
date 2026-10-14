---
claim_id: near_ground_spatial_correlation_bounded_theorem_note_2026-10-12
claim_type: bounded_theorem
actual_current_surface_status: conditional-support
assembly_status: publication_candidate_exact_root_review_pending
scientific_execution: none_in_this_assembly
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: theorem
conditional_surface_status: bounded consequences of the explicitly supplied model and representation
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: conditional spatial estimates with literal hypotheses and controls
audit_required_before_effective_retained: true
bare_retained_allowed: false
next_trace_action: preserve conditional spatial control for later model-selection research; no existing blocker is closed
runner: scripts/near_ground_spatial_correlation_identity_2026_10_12.py
upstream_dependencies:
  - concrete_gapped_chain_bounded_theorem_note_2026-10-12
  - current_preserving_refinement_bounded_theorem_note_2026-10-12
  - local_even_continuum_bounded_theorem_note_2026-10-12
  - bounded_interaction_ground_bounded_theorem_note_2026-10-12
  - continuum_local_ground_spatial_bounded_theorem_note_2026-10-12
  - adiabatic_ground_preparation_bounded_theorem_note_2026-10-12
  - excitation_pulse_response_bounded_theorem_note_2026-10-12
---

# Near-ground spatial correlation control

**Type:** bounded_theorem

The complete frozen argument below controls connected correlations by actual
excess form energy above the selected gapped ground. It includes the explicit
coherent four-particle free-continuum family that prevents the stated uniform
improvement beyond square-root dependence, the linear alternative under ground-block diagonality,
and clustering for each fixed normal free state with fixed translated probes.
These are different quantifiers, retained without alteration.

The exact [Concrete](CONCRETE_GAPPED_CHAIN_BOUNDED_THEOREM_NOTE_2026-10-12.md),
[Current](CURRENT_PRESERVING_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md),
[Local](LOCAL_EVEN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-10-12.md)
and [bounded-ground](BOUNDED_INTERACTION_GROUND_BOUNDED_THEOREM_NOTE_2026-10-12.md)
parents retain their supplied model and representation status; Current is
still an open_gate. The [continuum spatial companion](CONTINUUM_LOCAL_GROUND_SPATIAL_BOUNDED_THEOREM_NOTE_2026-10-12.md)
contains the exact ground-clustering input. The archived comparison's
specified protocol substitutions have the separately conditional
[preparation](ADIABATIC_GROUND_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-12.md)
and [response/pulse](EXCITATION_PULSE_RESPONSE_BOUNDED_THEOREM_NOTE_2026-10-12.md)
parents. Those protocol inputs are not required for the general state-energy
inequality or its coherent state-family counterexample.

Even support of a density, parity invariance and evenness of a probe are
distinct conditions. The stronger even gap in the state error requires
even-sector support. Arbitrary autonomous holds preserve the actual excess;
this does not supply an unrestricted long-time continuum operator comparison.
The following entire body retains its original hypotheses and exposure record.

<!-- BEGIN LITERAL SOURCE: NEAR_GROUND_CLUSTERING_INDEPENDENT.md -->

# Near-ground spatial correlations: an energy bound and its uniform scope

Status: proposed ordinary conditional analytic theorem in the supplied
full-Fock continuum model, with an actual finite-spacing comparison.
This core was derived before exposure to the root near-ground candidate.
Its ground, locality and current-carrier premises are shared checked sources;
that dependence and the same-model limitation remain explicit. This is not
an audit, formal verification, physical state selector or new axiom.

For a simple gapped ground, small actual excess energy controls the
connected correlation of bounded probes by the ground correlation plus a
constant times the square root of that excess. In the supplied massive
free continuum model this square-root dependence cannot be replaced
uniformly by a smaller-order function over all admissible normal states
and arbitrarily distant norm-one compact even probes. The witness below
uses smooth compact coefficient fields, finite-energy even pure states,
and the actual positive-polarization dispersion. Each fixed witness state
nevertheless clusters when one fixed probe is translated to infinity.

## 1. Precise hypotheses and supplied spatial ground bound

Fix m,v>0. The target one-particle operator, energy and polarization are

\[
 D(p)=-vp\sigma_x-m\sigma_y,\qquad
 E(p)=\sqrt{m^2+v^2p^2},\qquad P_+(p)=\tfrac12(I+D(p)/E(p)).
 \tag{N1}
\]

Use the full fermionic Fock space over
\(\mathfrak h=P_+L^2(\mathbb R;\mathbb C^2)\), with
\(H=d\Gamma(E)\) and vacuum \(\Omega\). Inner products are conjugate-linear
in the first variable. The unitary Fourier transform has factor
\((2\pi)^{-1/2}\) and phase \(e^{-ipx}\).
For real coefficient fields f, the selfadjoint Majorana is

\[
 \gamma(f)=a^*(h_f)+a(h_f),\qquad
 h_f=\sqrt2P_+\widehat f,\qquad
 \{\gamma(f),\gamma(g)\}=2(f,g)_{\mathbb R}I,\quad
 \|\gamma(f)\|=\|f\|_2.
 \tag{N2}
\]

The annihilator is conjugate-linear in its argument. In particular the
real coefficient map in (N2) is an isometry onto the underlying real
space of \(\mathfrak h\), as supplied by Local section 8.
The local algebra \(\mathcal A(X)\) is the norm-closed even CAR algebra
generated by real compact L2 coefficients supported in a bounded interval X.
Local section 7 proves finite propagation of the actual signed Dirac
coefficient flow and commutation of even algebras in its causal window.
These are statements about the coefficient supports; \(P_+\) itself is
not a local position-space projection.

Assume a bounded total potential

\[
 V=V^*\in\mathcal A(W),\qquad \|V\|\le K<m/2,
 \tag{N3}
\]

where W is one fixed bounded interval. It can be internally nonlocal
within W; it is not an extensive sum of local interaction densities.
The checked ground synthesis supplies \(G=H+V\), selfadjoint on D(H),
its simple even ground \(\Omega_g\), energy \(E_g\in[-K,K]\), and

\[
 L=G-E_g\ge0,\quad P=|\Omega_g\rangle\langle\Omega_g|,\quad Q=I-P,
 \qquad
 L\ge\delta Q,\quad \delta=m-2K>0.
 \tag{N4}
\]

The ground-orthogonal even sector has the larger gap
\(\gamma=2m-2K\). No such larger full-Fock gap is asserted.
All energy expectations below are nonnegative quadratic-form
expectations of L, not formal matrix elements of an unbounded operator
on unspecified vectors.

For \(A\in\mathcal A(X)\), \(B\in\mathcal A(Y)\), put

\[
 d_W(X,Y)=\min\{\operatorname{dist}(X,Y),
                  \operatorname{dist}(X,W)+\operatorname{dist}(Y,W)\}.
 \tag{N5}
\]

The complete newly read spatial parent and its comparison prove

\[
 |C_g(A,B)|
 :=|\langle AB\rangle_g-\langle A\rangle_g\langle B\rangle_g|
 \le 2\|A\|\|B\|e^{-(m-K)d_W(X,Y)/v}.
 \tag{N6}
\]

This applies to arbitrary bounded elements of those even algebras,
including nonselfadjoint elements and rough L2 polynomials.
No assertion that \(A\Omega_g\) has finite energy is needed.
For clarity, the parent proves the exact zero commutator window
\([A,e^{itG}Be^{-itG}]=0\) when \(v|t|<d_W\), using the ordered bounded
Dyson series. Its Gaussian positive-frequency filter, with a spectral
gap q and zero window T, gives

\[
 |C_g(A,B)|\le\|A\|\|B\|
 \min\{1,[1+2/(\pi qT)]e^{-qT/2}\}
 \le2\|A\|\|B\|e^{-qT/2}.
 \tag{N7}
\]

Finite complex spectral measures, rather than their energy moments,
justify this filter. Here its four spectral vectors are even, so
q=\(\gamma\) and T=\(d_W/v\), proving (N6).
The displayed middle expression in (N7) is used only for T>0;
when T=0 the trivial covariance bound gives (N6) directly.
The full proof of this supplied step is the pinned spatial source,
sections 2–4; the new state and sharpness proofs start below.

If \(\ell=\operatorname{diam}(W)\), then
\(d_W\ge[\operatorname{dist}(X,Y)-\ell]_+\).
Thus a fixed defect permits an ordinary-distance exponential bound
with a fixed diameter penalty. An unchanged Euclidean light cone does
not follow for an arbitrary V in (N3), as the parent's bilocal
counterexample shows. In the free case V=0, use the direct free window
and obtain (N6) with K=0 and \(d_W=\operatorname{dist}(X,Y)\),
without any fictitious defect.

## 2. Finite form energy controls state distance

Let \(\rho\) be a normal density on this representation, and define

\[
 \epsilon=\mathcal E_L(\rho)
 :=\sup_{n\ge1}\operatorname{Tr}\rho\,\min(L,n)<\infty,
 \qquad q=\operatorname{Tr}\rho Q.
 \tag{N8}
\]

The spectral inequality (N4) gives

\[
 q\le\min(1,\epsilon/\delta).
 \tag{N9}
\]

If \(\rho\) is supported in the even sector, the same proof uses
\(\gamma\) instead of \(\delta\).
Write g for the applicable one of these two gap constants.
Parity invariance, \([\rho,(-1)^N]=0\), by itself does not imply even
sector support and does not license the replacement \(g=\gamma\).

Here is the complete trace-distance step. Write a spectral decomposition
\(\rho=\sum_j\lambda_j|\psi_j\rangle\langle\psi_j|\).
On the span of two unit vectors, diagonalizing the difference of their
rank-one densities gives

\[
 \big\||\psi_j\rangle\langle\psi_j|-P\big\|_1
 =2\sqrt{1-|\langle\Omega_g,\psi_j\rangle|^2}.
 \tag{N10}
\]

Trace-norm convergence of the density sum, convexity, and
Cauchy–Schwarz with the weights \(\lambda_j\) yield

\[
 \|\rho-P\|_1
 \le2\sum_j\lambda_j\sqrt{\langle\psi_j,Q\psi_j\rangle}
 \le2\sqrt q
 \le2\min(1,\sqrt{\epsilon/g}).
 \tag{N11}
\]

This proof uses bounded Q and density operators. It does not require
the individual \(\psi_j\) to belong to D(G). Finite (N8) suffices;
the energy inequality is a spectral/form statement and is passed to
the trace by monotone convergence.

## 3. Connected-correlation estimate and a positive linear alternative

For a density \(\sigma\), define
\(C_\sigma(A,B)=\operatorname{Tr}\sigma AB-
(\operatorname{Tr}\sigma A)(\operatorname{Tr}\sigma B)\).
No commutation of \(\rho\) with G is assumed.
For arbitrary bounded A,B and densities \(\rho,\sigma\), put
\(D=\|\rho-\sigma\|_1\). Hölder's trace inequality gives

\[
 |\operatorname{Tr}(\rho-\sigma)AB|\le D\|A\|\|B\|,
\]
\[
 |(\operatorname{Tr}\rho A)(\operatorname{Tr}\rho B)
   -(\operatorname{Tr}\sigma A)(\operatorname{Tr}\sigma B)|
 \le2D\|A\|\|B\|.
\]

Consequently

\[
 |C_\rho(A,B)-C_\sigma(A,B)|\le3D\|A\|\|B\|.
 \tag{N12}
\]

The product of means was split into two terms; no cancellation or
assumed vanishing one-point function enters this estimate.
Combining (N6), (N11) and (N12) proves the promised bound

\[
 \boxed{\quad
 |C_\rho(A,B)|
 \le 2\|A\|\|B\|e^{-(m-K)d_W(X,Y)/v}
       +6\|A\|\|B\|\min(1,\sqrt{\epsilon/g}).
 \quad}
 \tag{N13}
\]

The right side can also be capped by \(\|A\|\|B\|\).
Indeed the Hilbert–Schmidt Cauchy–Schwarz inequality on the two centered
vectors \((A^*-\overline{\langle A\rangle_\rho})\rho^{1/2}\) and
\((B-\langle B\rangle_\rho)\rho^{1/2}\) gives this elementary covariance
bound. The constants in (N12)–(N13) are sufficient, not optimized.

There is a meaningful extra premise that improves the power. If
\([\rho,P]=0\), then
\(\rho=(1-q)P+Q\rho Q\), and the two terms in \(\rho-P\) have
orthogonal supports. Hence \(\|\rho-P\|_1=2q\), and

\[
 |C_\rho(A,B)-C_g(A,B)|
 \le6\|A\|\|B\|\min(1,\epsilon/g).
 \tag{N14}
\]

For example, a density stationary under every \(e^{-itG}\) commutes
with the spectral projection P and satisfies this additional premise.
This is a condition eliminating ground-to-excited coherence.
It is not a consequence of parity invariance: coherent superpositions
of the even vacuum and an even excitation preserve parity. The
counterexample in section 6 uses precisely such coherence.

## 4. Observation times, preparation hypotheses and actual spacings

Under an arbitrary autonomous hold,
\(\rho(t)=e^{-itG}\rho e^{itG}\), spectral calculus gives
\(\mathcal E_L(\rho(t))=\epsilon\), \(q(t)=q\), and
\(\|\rho(t)-P\|_1=\|\rho-P\|_1\). Even sector support is also preserved.
Thus (N13) is uniform in all real hold times for the equal-time
expectation of the fixed local probes A,B in the evolved state.
This all-hold-time statement follows from closeness to a stationary
ground; it is not an operator-norm continuum comparison of arbitrary
long-time evolved observables.

In particular, for an actual prepared state with a separately supplied,
proved estimate

\[
 \epsilon_{\rm prep}(\tau)\le C_{\rm prep}/\tau^2,
 \tag{N15}
\]

(N13) gives an additive correlation error at most
\(6\|A\|\|B\|\sqrt{C_{\rm prep}/g}/\tau\), uniformly during any subsequent
autonomous hold. A supplied vanishing-excess preparation without a rate
still gives a vanishing error. Equation (N15) is an explicit input to
this substitution, not a preparation theorem derived from the gap
alone. For an exact even vacuum preparation evolved with an even
Hamiltonian, the resulting state is supported in the even sector, so
g=\(\gamma\) is appropriate. No assertion is made that every density
used in section 6 is generated by a particular ramp, pulse or local
preparation protocol, or that the substituted \(1/\tau\) estimate is
optimal for such a restricted protocol.

Here is the actual finite-spacing version, using only the static
comparison already checked in the ground and spatial parents.
Let \(H_c\) be the actual positive two-band Hamiltonian, with

\[
 e_{c,L}(p)^2=m^2+\frac{2v^2p^2}{1+\sqrt{1-c^2p^2}},\quad
 e_{c,H}(p)^2=m^2+\frac{2v^2}{c^2}(1+\sqrt{1-c^2p^2}),
 \quad |p|<1/c.
 \tag{N16}
\]

Use \(G_c=H_c+V_c\) on the physical Fock space, with V_c bounded,
selfadjoint and even, and its in-band extension reducing that space. Suppose
\(\|V_c\|,\|V\|\le K<m/2\) in the spacings under consideration, the
in-band unital CAR potentials obey
\(\nu_c=\|\widehat V_c-V\otimes I_H\|\to0\), and the separately even
ordinary-cell probes obey

\[
 a_c=\|\widehat A_c-A\otimes I_H\|,\quad
 b_c=\|\widehat B_c-B\otimes I_H\|,\quad
 \|A_c\|,\|A\|\le M_A,\quad \|B_c\|,\|B\|\le M_B.
 \tag{N17}
\]

Current C21 supplies \(a_c,b_c\to0\) for fixed ordinary compact L2
polynomials. The target V must also satisfy the spatial premise (N3)
to use (N6). For fixed \(\mu>K\), set

\[
 r_c=\frac{\mu^2c/v+\nu_c}{(\mu-K)^2},\qquad
 d_\mu=\frac{m-2K}{(\mu+K)(\mu+m-K)},\qquad
 \theta_c=2\min(1,r_c/d_\mu).
 \tag{N18}
\]

The parent's compressed-resolvent argument proves that the isometrically
embedded actual rank-one ground density differs from the target ground
density, tensored with the high vacuum, by at most \(\theta_c\) in trace
norm. In (N17) observables have unital CAR extensions; states have
isometric density embeddings. Outside-band zero modes of an auxiliary
generator are not part of the actual gap argument. The high-vacuum
projection, physical Fock-band projection and interacting ground
projection are different projections.

For any actual normal density \(\rho_c\) of actual excess
\(\epsilon_c=\mathcal E_{G_c-E_{g,c}}(\rho_c)\), (N11)–(N12),
the ground trace bound, and product telescoping give

\[
 \begin{split}
 |C_{\rho_c}(A_c,B_c)|
 \le{}&2M_AM_Be^{-(m-K)d_W(X,Y)/v}
       +6M_AM_B\min(1,\sqrt{\epsilon_c/g})\\
     &+3\theta_cM_AM_B+2(M_Ba_c+M_Ab_c).
 \end{split}
 \tag{N19}
\]

Here g=\(\delta\) for general actual states and g=\(\gamma\) for states
supported in the actual even sector. The observable comparison terms
follow by one telescoping of the product and one of the two means;
each observable error appears twice. In fact
\(\lvert C_{\rho_c}(A_c,B_c)-C_g(A,B)\rvert\) is bounded by the last
three error terms on the right of (N19), without its exponential term.
This is an estimate on actual
finite-c correlations, not just a statement about a limiting density.
It holds uniformly under arbitrary autonomous holds of \(\rho_c\):
the first state comparison is always with its own stationary actual
ground, and the remaining comparisons are all at time zero.

For fixed profiles, \(\epsilon_c\to0\) gives the ground continuum limit
throughout all sufficiently small spacings, with no subsequence selector.
If an actual even preparation supplies
\(\epsilon_c\le C_{\rm prep}/\tau(c)^2\) uniformly and
\(\tau(c)\to\infty\), the same conclusion and the stated \(1/\tau(c)\)
error hold. No relation between c and \(\tau(c)\) is required by (N19).
This assertion is conditional on that actual preparation bound, not
on a free-energy ceiling alone.

The spatial limit can be taken after the fixed-profile continuum
limit. A joint unbounded translation \(R=R(c)\) additionally requires
(N17) for those moving profiles. Uniformity on bounded translation
sets follows from compactness of fixed L2 translation orbits and
strong convergence of the uniformly bounded cell comparison maps.
Pointwise C21 is not sufficient for arbitrary growing translations;
the spatial parent gives an explicit current-coordinate phase
counterexample to that stronger coefficient-norm premise.
No optional native-lattice clustering theorem is used here. Similarly,
these equal-time estimates do not assert an unrestricted growing
relative-time continuum comparison.

## 5. A concrete pair of local probes in the free continuum

We now test uniform improvement of the excess-energy power using
V=0 in the actual model (N1)–(N2). This subclass already satisfies every
bounded-defect hypothesis. Fix a real nonzero smooth compact scalar
function \(\phi\), normalized by \(\|\phi\|_2=1\), supported in an interval
I of length \(\ell\). Put

\[
 f_1=(\phi,0),\quad f_2=(0,\phi),\quad
 h_j=\sqrt2P_+\widehat f_j,\qquad
 A=i\gamma(f_1)\gamma(f_2).
 \tag{N20}
\]

The real fields \(f_1,f_2\) are orthonormal. Thus A is selfadjoint,
\(A^2=I\), \(\|A\|=1\), and \(A\in\mathcal A(I)\).
For \(R>\ell\), let \(T_Rh(p)=e^{-ipR}h(p)\), translate both real
profiles by R, and denote the resulting observable by \(B_R\).
Then \(\|B_R\|=1\), \(B_R\in\mathcal A(I+R)\), and A commutes with
\(B_R\). Their distance is \(R-\ell\). They are fixed-degree,
fixed-shape smooth local probes; no norm or word degree grows with R.

Since the diagonal entries of D vanish, \(\|h_j\|=1\).
The off-diagonal entry of \(D/E\) is \((-vp+im)/E\), and the Fourier
modulus of the real \(\phi\) is even. Therefore

\[
 \langle h_1,h_2\rangle=i\kappa,\qquad
 \kappa=m\int_{\mathbb R}\frac{|\widehat\phi(p)|^2}{E(p)}\,dp,
 \qquad 0<\kappa<1,\quad d=1-\kappa^2>0.
 \tag{N21}
\]

Strictness uses \(E(p)>m\) except on the null set \(\{0\}\);
a nonzero L2 function cannot be supported on that set.
In particular \(h_1,h_2\) are complex-linearly independent, a fact
which would not follow merely by treating two real modes as two
independent positive-energy modes without checking their Gram matrix.

Let \(\Pi_4\) be the four-particle projection. With the creation-wedge
convention fixed by \(a^*(u_1)\cdots a^*(u_n)\Omega
=u_1\wedge\cdots\wedge u_n\), set

\[
 w_R=h_1\wedge h_2\wedge T_Rh_1\wedge T_Rh_2,\quad
 u_R=\Pi_4 AB_R\Omega=-w_R,\quad n_R=\|w_R\|.
 \tag{N22}
\]

The sign comes from the two factors i in A and \(B_R\).
All other terms of \(AB_R\Omega\) have particle number at most two.
Every cross-Gram entry
\(\langle h_i,T_Rh_j\rangle\) tends to zero as \(R\to\infty\):
its Fourier integrand is L1 by Cauchy–Schwarz, and its oscillatory
integral tends to zero. One elementary justification is approximation
of that L1 integrand by smooth compact functions, integration by parts
there, and the uniform L1 error bound. The determinant formula for
fermionic wedges now gives

\[
 n_R^2
 =\det\operatorname{Gram}(h_1,h_2,T_Rh_1,T_Rh_2)
 \longrightarrow d^2.
 \tag{N23}
\]

Thus some finite \(R_0>\ell\) has \(n_R\ge d/2\) for every \(R\ge R_0\).
No exponential overlap rate or momentum cutoff was assumed.

All four one-particle vectors are in D(E), because \(\phi\) is smooth.
In fact the same diagonal calculation yields

\[
 \|Eh_j\|=\|ET_Rh_j\|=e_\phi,\qquad
 e_\phi=(m^2+v^2\|\phi'\|_2^2)^{1/2}.
 \tag{N24}
\]

On their wedge the actual Fock Hamiltonian acts as the sum of the
four one-particle energies. This formula and membership in D(H)
follow first for spectrally bounded vectors and then by simultaneous
E-graph convergence of all four vectors, continuity of the wedge,
and closedness of H. The wedge norm is at most the product of the
one-particle norms. Hence

\[
 \|Hw_R\|\le4e_\phi.
 \tag{N25}
\]

Define the normalized four-particle vector
\(\chi_R=u_R/n_R\). It belongs to D(H), is even, and its actual energy
\(\mathcal E_R=\langle\chi_R,H\chi_R\rangle\) satisfies

\[
 4m\le\mathcal E_R
 =\frac{\langle w_R,Hw_R\rangle}{n_R^2}
 \le\frac{4e_\phi}{n_R}
 \le E_*:=\frac{8e_\phi}{d},
 \qquad R\ge R_0.
 \tag{N26}
\]

The upper bound is uniform in separation and uses the actual unbounded
dispersion. It is not inferred from boundedness of A or from a transition
probability. It also does not replace the full continuum Hamiltonian
by a finite-mode surrogate.

## 6. Exact-energy even states giving a square-root lower bound

For a prescribed \(0<\epsilon\le m\) and \(R\ge R_0\), set

\[
 \eta_R=\epsilon/\mathcal E_R,\qquad
 \psi_{\epsilon,R}
   =\sqrt{1-\eta_R}\,\Omega+\sqrt{\eta_R}\,\chi_R,\qquad
 \rho_{\epsilon,R}=|\psi_{\epsilon,R}\rangle
                    \langle\psi_{\epsilon,R}|.
 \tag{N27}
\]

These are normalized even pure states in D(H), with
\(\eta_R\le1/4\) and exactly

\[
 \mathcal E_H(\rho_{\epsilon,R})=\epsilon.
 \tag{N28}
\]

The energy cross term vanishes because H preserves particle number
and \(H\Omega=0\). Both ground and excitation components are even:
the states are supported in the even sector and are parity invariant,
not just mixtures permitting an odd sector.

Since A and \(B_R\) are quadratic, their application to the vacuum has
particle number zero or two. Thus
\(\langle\Omega,A\chi_R\rangle=
\langle\Omega,B_R\chi_R\rangle=0\), with the adjoint matrix elements
also zero. On the other hand \(AB_R\) is selfadjoint, and (N22) gives

\[
 \langle\Omega,AB_R\chi_R\rangle
 =\langle AB_R\Omega,\chi_R\rangle=n_R>0.
 \tag{N29}
\]

Consequently the product expectation has the positive cross term
\(2n_R\sqrt{\eta_R(1-\eta_R)}\), while the two means have no
square-root cross term. More explicitly, with
\(a=\langle A\rangle_\Omega\), \(b=\langle B_R\rangle_\Omega\),
\(a_\chi=\langle A\rangle_{\chi_R}\),
\(b_\chi=\langle B_R\rangle_{\chi_R}\), the two state means are
\((1-\eta_R)a+\eta_Ra_\chi\) and
\((1-\eta_R)b+\eta_Rb_\chi\).
Each mean differs from its vacuum value by at most \(2\eta_R\).
The two products of means therefore differ by at most \(4\eta_R\).
The diagonal part of the AB expectation differs from its vacuum value
by at most \(2\eta_R\). All these scalars are real. This proves

\[
 \left|C_{\rho_{\epsilon,R}}(A,B_R)
      -C_\Omega(A,B_R)
      -2n_R\sqrt{\eta_R(1-\eta_R)}\right|\le6\eta_R.
 \tag{N30}
\]

Let

\[
 c_0=\frac{d}{\sqrt{2E_*}},\qquad
 \epsilon_0=\min\{m,c_0^2m^2/36\}.
 \tag{N31}
\]

For \(0<\epsilon\le\epsilon_0\), (N23),(N26) and
\(\eta_R\le1/2\) imply
\[
 2n_R\sqrt{\eta_R(1-\eta_R)}\ge c_0\sqrt\epsilon,\qquad
 6\eta_R\le\frac{3\epsilon}{2m}\le\frac{c_0}{4}\sqrt\epsilon.
 \tag{N32}
\]

The free ground bound is
\(|C_\Omega(A,B_R)|\le2e^{-m(R-\ell)/v}\).
Choose any R large enough that \(R\ge R_0\) and
\[
 R-\ell\ge\frac vm\max\{0,\log(8/(c_0\sqrt\epsilon))\}.
 \tag{N33}
\]
Then the vacuum term is at most \(c_0\sqrt\epsilon/4\).
Equations (N30)–(N33) establish the explicit lower bound

\[
 \boxed{\qquad
 C_{\rho_{\epsilon,R}}(A,B_R)
 \ge \frac{c_0}{2}\sqrt\epsilon>0.
 \qquad}
 \tag{N34}
\]

There is no upper bound on R in this construction. All constants
\(d,e_\phi,E_*,c_0,\epsilon_0\) depend only on the fixed m,v and the
fixed compact smooth profile, not on \(\epsilon\) or the separation.
The threshold \(R_0\) is fixed by that profile's Gram limit.
The energy is exact, not merely bounded by an unspecified multiple of
\(\epsilon\).

It follows precisely that no function \(f(\epsilon)=o(\sqrt\epsilon)\)
can replace the excess term uniformly in a bound
\[
 |C_\rho(A_x,B_y)|\le F(\operatorname{dist}(X+x,Y+y))
                       +C f(\epsilon),
 \tag{N35}
\]
where C is finite and independent of the energy, admissible state and
translation, and F is one fixed function, independent of that energy
and state, with \(F(r)\to0\) as \(r\to\infty\), even for the norm-one profiles
(N20) and \(V=0\). For each sufficiently small \(\epsilon\), take R
arbitrarily large, so that F is smaller than any chosen fraction of
\(\sqrt\epsilon\), while (N34) still holds. Letting \(\epsilon\to0\)
contradicts (N35). In particular a uniform \(O(\epsilon^\alpha)\)
replacement with \(\alpha>1/2\), including a linear term, fails in
this stated class.

This is a uniform-family sharpness result for the excess power,
not a claim that the numerical constant in (N13) or its spatial
exponent is optimal. The family is indexed by both energy and
separation; it is not a single state with persistent correlations
at all separations. No claim about every interacting potential or
about a restricted preparation protocol follows from this example.

## 7. Each fixed normal free state still clusters for fixed translated probes

For completeness, the absence of a uniform state-family improvement is
compatible with a strong positive fixed-state statement. In the free
Fock representation, if B is any fixed bounded even local observable
and \(B_R\) its geometric translate, then

\[
 B_R\ \longrightarrow\ \langle B\rangle_\Omega I
 \quad\text{in the weak operator topology as }|R|\to\infty.
 \tag{N36}
\]

To prove this, first let B be a finite even polynomial in compact real
Majoranas. Take vectors \(C\Omega,D\Omega\) for finite field polynomials
C,D. These vectors form a dense subspace of the full Fock space:
the real coefficient map in (N2) is onto, so creations are complex
linear combinations of such fields, and compact real coefficients
are dense by L2 approximation.
Compute \(\langle C\Omega,B_RD\Omega\rangle\) by successively
anticommuting annihilators to the vacuum, equivalently by the finite
vacuum pairing expansion. Every pairing between a translated B
coefficient and a fixed C or D coefficient tends to zero by the L1
oscillatory argument used for (N23). Pairings entirely inside the
translated block do not change with R. In terms with no linking
pairing, moving the even-length translated block past a fixed block
has sign plus; the surviving sum is exactly
\(\langle B\rangle_\Omega\langle C\Omega,D\Omega\rangle\).
This proves (N36) on the dense vector set.

The uniform bound \(\|B_R\|=\|B\|\) extends the limit to all vector
matrix elements. Norm approximation of a general even local B by
finite even polynomials, with the same norm error for every R,
proves (N36) in its stated norm-closed local algebra. No energy
moment of C,D or B, and no compactness of H's resolvent, is needed.

Pairing a uniformly bounded weak-operator convergent family with a
trace-class operator passes to the limit, by finite-rank approximation
of that operator. Hence for any fixed normal density \(\rho\) and
any fixed bounded A,

\[
 \operatorname{Tr}\rho B_R\to\langle B\rangle_\Omega,\qquad
 \operatorname{Tr}\rho AB_R\to
       (\operatorname{Tr}\rho A)\langle B\rangle_\Omega,\qquad
 C_\rho(A,B_R)\to0.
 \tag{N37}
\]

This applies in particular to every fixed state (N27), when its
parameters are fixed and the second probe is subsequently translated
further away. Its convergence rate is not uniform over the varying
states used in (N34). The assertion in (N37) keeps A fixed and
translates a fixed B; it is not an additional rate for arbitrary
varying observables, supports, particle contents or representations.
It is a free-representation result, not a classification of normal
states for arbitrary interacting dynamics.

## 8. Domain, representation and scientific boundaries

The upper bounds require only a normal density with finite actual
excess form energy and bounded probes. Rough local probes need not
map the ground into the energy form domain. The witness uses smooth
compact profiles to prove its stronger D(H) membership and uniform
actual energy directly; it does not repair the separate rough-domain
counterexamples in the ground parent.

The ground gap is a premise in the supplied full Fock representation.
Even sector support of a state, parity invariance of a density, and
evenness of an observable are three distinct conditions. The larger
gap in (N6) uses the parity of four vectors created from the even
ground. Its use for the state-distance term separately requires
even sector support. The witness meets that stronger condition.
No general assertion about preservation of a particle-parity sector
under arbitrary CAR subsequential limits is used.

Smallness of the total potential norm supplies the ground and gap;
spatial locality in fixed W supplies the ground spatial decay.
Neither premise selects a physically realized interaction or state.
A positive fixed free-energy ceiling does not imply vanishing actual
interacting excess. Conversely, near-ground actual states do obey
the parent's free-energy cap \(\mathcal E_H(\rho)\le2K+\epsilon\);
that auxiliary fact is not a substitute for (N8).

Only equal-time two-block connected correlations are estimated here.
There is no higher-cumulant, extensive-interaction, optimal
correlation-length, universal relativistic-net or empirical claim.
The literal counterexample (N34) refutes the particular uniform
excess-power improvement (N35). It does not exhaust possible
additional hypotheses or prove a global no-go. The block-diagonal
positive alternative (N14), fixed-state result (N37), and explicit
preparation hypotheses are retained.

## 9. Exact inputs, exposure and independent-core scope

The neutral plan was written before new spatial proof-body exposure
at 2026-10-12T21:01:56.126117+00:00, with SHA256
63f23b76814e6faada8506d42407d2b8be1ed027230959e624213b32c86e675b.
The task used these exact sources:

| Source | SHA256 | Coverage and use |
| --- | --- | --- |
| BOUNDED_INTERACTION_GROUND_SYNTHESIS.md | b8bcba769100bf819885937d850a7bff8543e4233c1df3cf65f68372552160e9 | Prior complete author read reused; definitions and sections 7–9 refreshed for actual gaps, resolvents and excess |
| BOUNDED_INTERACTION_GROUND_SYNTHESIS_REVIEW.md | af0cf7d6e9ea98fc92ac86df651c136cb2766f40571b814b69f3850304ebfe53 | Prior complete read reused at unchanged identity |
| GAPPED_LOCAL_CORRELATION_INDEPENDENT.md | 22b57614cc79fe7db0fec7d5861363da64b1bda205a93f153acf274c28c5910e | Newly read all 566 lines before deriving; supplied spatial bound and static comparison |
| GAPPED_LOCAL_CORRELATION_CROSSCHECK.md | 79f2c951b7c9319865e09a10950c73e235cbefa08de73791595f5ac940568378 | Newly read all 325 lines; complete source-exposed comparison, not another independent premise |
| Canonical Current note | 763082a6faa8bea3f6be74ddc7ee81bf288c00740085804e62f701a1576283ff | Earlier complete read reused; actual sign and Fourier definitions refreshed |
| Canonical Local note | b5a8394a9d8c17bb9559597a68b061ad3872201ebf9793bd5c9f10b15ac2c6aa | Earlier complete read reused; finite propagation and full/even representation distinction refreshed |

The new exposure record honestly brackets first spatial-source exposure
between the plan and its completed-read record, rather than inventing a
precise unrecorded first-read clock. Exact input copies, byte counts,
coverage and final identities are in near_ground_clustering_independent.
Unchanged governing instruction coverage is reused at the identities
recorded in the neutral plan.

No root near-ground probe or seal, latest campaign checkpoint, other new
root candidate, or optional native-clustering proof was read before this
independent core was frozen. Earlier preparation work remains shared
context; (N15) is stated as an explicit conditional input rather than
a new independent proof or a hidden imported protocol constant.
The author knew the assigned question and the existence of a separate
root candidate, not its construction or result.

This is a same-model independent derivation of the spatial-excess
composition and actual-model uniformity test from the stated shared
premises. The ground trace-distance step was already present in the
shared ground synthesis and is explicitly reproduced here.
Source identities establish provenance only. No numerical or formal
proof execution, external theorem search, repository/Git operation,
publication, audit verdict, canonical edit, campaign checkpoint,
editable prompt or physical axiom change was performed.
The frozen core and seal precede outcome reporting and any comparison
with the root near-ground candidate.

<!-- END LITERAL SOURCE: NEAR_GROUND_CLUSTERING_INDEPENDENT.md -->

## Assembly relationship and exact review scope

The literal core has SHA-256
3ccc98a7a03d1617476bd14d25e3a64f20b33c12c0ffd16e9aec06fe0e88a76b.
Its complete [source-exposed comparison](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/4ff0ff1d7868b24d7854428110512daed13530f9/.claude/science/physics-loops/toe-spatial-control-20261012/objects/b316b084ec3a9c106af5026d53783dabf401d23a33cb634f090a67d37143d225.gz)
has SHA-256
b316b084ec3a9c106af5026d53783dabf401d23a33cb634f090a67d37143d225
and records no required repair. It preserves the independent profile choice,
stronger D(H) witness, all normalization constants, fixed-state positive result
and pre-exposure provenance. The root alternative and its original seal are
carried separately; no alternative-source independence is invented here.

The square-root control is sharp in the stated uniform family of admissible
free-continuum states and distant fixed-profile probes. It is not a claim that
a chosen ramp or pulse realizes those states, nor a rate-optimality theorem for
that restricted protocol. Each fixed normal free state still has the precise
fixed-probe clustering conclusion proved in N36-N37.

The comparison's native preparation consequence uses the earlier finite
polynomial-resource theorem, with its defect geometry and temporal resources.
It remains valid at that scope. This assembly does not replace that premise
with the later whole-unit-ball theorem or assert a new protocol composition.
In particular no newer BV/prepared-pulse, propagation-limit, graph-energy or
spatial-escape result is incorporated. The named preparation and pulse
parents are provenance for the already checked conditional substitutions only.

Actual finite-spacing bounds use the stated unital observable convergence
and isometric ground-density embedding. Full-Fock, even-ground and high-band
projections remain distinct. Fixed-profile/compact-parameter convergence does
not imply arbitrary moving-profile or growing relative-time convergence.
The bound uses actual interacting excess, not a free-energy ceiling alone.

All source reviews are ordinary same-family checks on shared exact premises.
N1/N5 remain pending; the literal uniform-family obstruction is not an
exhaustive no-go claim. No analytic Lean certificate, audit verdict, retained
promotion, new state selector or new physical axiom is supplied. Root accepted the exact
source assembly for publication preparation only. The publication wrapper
requires separate exact root review.

## Publication evidence and review record

The [source map](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/4ff0ff1d7868b24d7854428110512daed13530f9/.claude/science/physics-loops/toe-spatial-control-20261012/EVIDENCE_MAP.json) preserves exact
proofs, completed comparisons, original exposure records and finite Ring
source/log/receipt. Its compressed objects decode to their named original
bytes. The [transformation map](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/4ff0ff1d7868b24d7854428110512daed13530f9/.claude/science/physics-loops/toe-spatial-control-20261012/PUBLICATION_EDITS.json)
records every wrapper change and all literal body boundaries.
The registered primary tool checks source identity and reconstruction only;
it executes zero mathematical predicates and supplies no proof or audit.
The [N-gate record](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/4ff0ff1d7868b24d7854428110512daed13530f9/.claude/science/physics-loops/toe-spatial-control-20261012/NO_GO_DISCIPLINE_CHECKLIST.md)
retains N1/N5 pending. No new mathematical body edit or status promotion
is introduced by publication preparation.


Review-loop integration note: dependencies are integrated through main d5c0ccd2e578839f19362c9705986e1e585496e5 and the accompanying reviewed spatial/energy batch. Original analytic bodies and historical evidence remain preserved. Live canonical parent hashes are refreshed with original bindings retained; earlier pending/main labels describe publication-time provenance and confer no audit authority.
