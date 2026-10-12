---
claim_id: adiabatic_ground_preparation_bounded_theorem_note_2026-10-12
claim_type: bounded_theorem
claim_scope: "Linear vacuum preparation with uniform amplitude and actual quadratic excess-energy bounds, joint ground limit, arbitrary autonomous hold and compact relative-time correlations; later broad-class rate witness."
upstream_dependencies:
  - bounded_interaction_ground_bounded_theorem_note_2026-10-12
runner: scripts/adiabatic_ground_preparation_identity_2026_10_12.py
artifact_role: theorem
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: partially_closes
target_claim_id: null
target_blocker_text: "Construct a supplied protocol whose actual excess energy vanishes and quantify its controlled observation window."
source_of_blocker_text: frontier_question
next_trace_action: "Review and integrate this exact assembly; preserve supplied dynamics, state and protocol premises."
conditional_surface_status: "Supplied massive chain and full Fock representation; Current is open_gate and correlation PR9500 is provisional."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Conditional ordinary analytic theorems with explicit premises; finite algebra Lean scope is separate."
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

**Type:** bounded_theorem

Status: conditional-support

Primary runner: [source identity and reconstruction only](../scripts/adiabatic_ground_preparation_identity_2026_10_12.py).
It executes zero mathematical predicates, scientific mutations or Lean checks.

**Publication provenance and review.** The frozen 888-line preparation assembly
has SHA-256 `6d82cfece7f56a333c3583fa7e97b1b2e38edd5c414893ba128e70a74c60ba7c`.
Its complete 285-line source-exposed review, SHA-256
`fe3aa3cde43c557609b66b589ac49d16c3f9f8207f0d75ff0ff3a1cf3d692245`,
found no theorem-invalidating error. Root read the whole assembly and review
and accepted two precise citation corrections in the later publication copy.
The complete review and root acceptance, SHA-256
`fe3862a6f975ea2e0a5bb4852c620bd6a066002a51b04fb62cf4fdcb25138ac1`,
are archived. The frozen original remains unchanged.

Exactly two citation passages below now attribute ordinary-cell support to
Local sections 3 and 6, especially L23-L24, instead of L10. No mathematical
statement or other body byte was edited. Both exact old/new strings and a
separate citation-only diff are preserved. The original pending-review and
no-optimality language records the original assembly's scope and chronology.

A separately completed 427-line sharpness proof is appended after the original
body and publication dependency record. It was independently sealed before
source comparison; the complete 259-line comparison and root read record are
archived. It gives a fixed finite two-mode witness for the broad linear-ramp
class. It does not retroactively turn the original assembly into an optimality
proof or establish sharpness for the supplied chain interaction.

All stages retain same-family/shared-premise limits. Publication wrapper/program
review and root execution acceptance remain pending here. This source assembly
and its archive reconstruction are not a fresh independent check or audit.


# Slow preparation of the conditional interacting ground state

Status: proposed conditional analytic theorem; source-exposed companion
assembly. This source combines the exact preparation and quadratic-energy
proofs with their completed ordinary comparisons and the frozen
bounded-interaction/ground theorem listed in section 12. It has not yet
received its own exact-source focused review. It confers no retained or audit
status and contains no analytic Lean claim.

A supplied external linear switch, starting in the exact free vacuum, prepares
the instantaneous ground line with amplitude error `O(1/tau)` and actual
unbounded excess energy `O(1/tau^2)`. The constants are uniform in the
allowed lattice spacing. The actual free mean energy never exceeds `2K`.
Static ground convergence then gives the continuum interacting ground density
for every joint limit `c -> 0, tau(c) -> infinity`, including an arbitrary
final autonomous waiting time. Correlation convergence needs the separately
stated norm comparison of observable and interaction orbits on each fixed
relative time window.

The chain, vacuum representation, interaction, exact initial state, controllable
schedule and small total interaction bound are supplied hypotheses. This is one
conditional unitary preparation protocol, not autonomous relaxation or a
framework-derived state-selection law.

## 1. Hypotheses, actual spaces, and three distinct conclusions

The analytic preparation theorem first concerns one Hilbert space
\(\mathcal H\), a selfadjoint \(H\ge0\) on the dense domain
\(\mathcal D=\mathcal D(H)\), and a normalized vector \(\Omega\) such that
\[
 H\Omega=0,\qquad
 H\ge m(I-|\Omega\rangle\langle\Omega|),\qquad m>0.                         \tag{P1}
\]
The zero eigenvalue is simple. Let \(V=V^*\) be bounded with
\[
 \|V\|\le K<m/2,\qquad \delta=m-2K>0.                                      \tag{P2}
\]
The bound is on the **total** operator. With \(\hbar=1\), prescribe
\[
 H^{\rm ramp}(t)=H+(t/\tau)V,\quad 0\le t\le\tau,\qquad
 \Psi_\tau(0)=\Omega,\qquad \tau>0.                                        \tag{P3}
\]
In slow time \(s=t/\tau\), write
\[
 H_s=H+sV,\quad
 \partial_sU_\tau(s,r)=-i\tau H_sU_\tau(s,r),\quad
 \psi_\tau(s)=U_\tau(s,0)\Omega,\quad
 \rho_\tau(s)=|\psi_\tau(s)\rangle\langle\psi_\tau(s)|.                      \tag{P4}
\]
After \(s=1\) hold \(G=H+V\) fixed. Evenness of \(V\), when imposed for the
physical spin application, preserves parity. The full-space analytic estimates
below need no parity restriction, compact resolvent, particle cutoff, bounded
\(H\), bound on \([H,V]\), or invariance \(V\mathcal D\subset\mathcal D\).

For the actual chain, use the supplied Current, Concrete and Local parents at
main `516cb69d8487ff04f8a48e065d3dcbe71d7dd237`, with the exact identities
in section 12. In their positive-energy carrier let
\[
 E(p)=\sqrt{m^2+v^2p^2},\quad
 \mathcal F_*=\mathcal F_-(\mathfrak h_L\oplus\mathfrak h_H)
              \simeq\mathcal F_L\otimes\mathcal F_H,\quad
 H_0=d\Gamma(E)\text{ on }\mathcal F_L.                                    \tag{P5}
\]
Here \(v>0\), \(\mathfrak h_L=P_+L^2(\mathbb R;\mathbb C^2)\),
\(P_+(p)=\frac12(I+[-vp\sigma_x-m\sigma_y]/E(p))\), and
\(\mathfrak h_H\) is the high positive-polarization copy. The low factor
comes first in the graded tensor identification. Low even operators act
as their full-Fock representatives tensor \(I_H\).

For \(I_c=(-1/c,1/c)\), \(w_c(p)=\sqrt{1-c^2p^2}\) on that interval, the actual
branches are
\[
 e_{c,L}^2=m^2+\frac{2v^2p^2}{1+w_c},\qquad
 e_{c,H}^2=m^2+\frac{2v^2}{c^2}(1+w_c).                                    \tag{P6}
\]
Let \(\iota_c\) be the actual positive-energy Fock isometry and
\(\Pi_c=\iota_c\iota_c^*\) its range projection: vacuum outside both momentum
bands. It is a Fock-space projection, not a one-particle projection. Also put
\[
 q_c=\Gamma(\mathbf1_{I_c})\text{ on }\mathcal F_L,\quad
 P_H=I_L\otimes|\Omega_H\rangle\langle\Omega_H|,\quad Q_H=I-P_H.
\]
The ground projections \(P_s\), or \(P_{g,c}\) at the final coupling, are
different objects from \(\Pi_c,q_c,P_H\). They need not commute with \(P_H\).

The actual \(H_c\) acts on its physical Fock space, identified with
\(\Pi_c\mathcal F_*\); its domain at each fixed \(c\) is \(\mathcal D(N)\).
Its one-particle bandwidth is finite at fixed \(c\) but not uniformly bounded
as \(c\to0\). The target domain is the maximal weighted domain of \(d\Gamma(E)\).
Both actual and target free Hamiltonians satisfy (P1). On the actual range,
as form inequalities,
\[
 E\le e_{c,L}\le\sqrt2E,\qquad
 H_c\ge H_0\otimes I_H,\qquad
 H_c\ge\Lambda_cN_H\ge\Lambda_cQ_H,\quad
 \Lambda_c=\sqrt{m^2+2v^2/c^2}.                                           \tag{P7}
\]
Outside-band modes are absent from that physical range.

For \(0<c<c_0\), let \(\widehat V_c\) be a bounded selfadjoint even in-band CAR
element in its **unital** common-carrier extension, reducing \(\Pi_c\).
Its actual restriction is \(V_c\). Let \(V_0\) be a selfadjoint even low-CAR
element, \(\widehat V_0=V_0\otimes I_H\), with both norms at most the same
\(K<m/2\). The three conclusions require different premises:

1. The preparation estimates apply separately at each allowed \(c\), or to the
   target, using only (P1)-(P3). No inter-spacing convergence is needed.
2. The joint state limit additionally assumes the time-zero comparison
   \(\nu_c=\|\widehat V_c-\widehat V_0\|\to0\), with the actual embeddings and
   branches above.
3. Correlations additionally require the compact free-orbit norm comparisons
   (P39) below for the specified even observable blocks and the potential.

Only spacings satisfying the uniform smallness hypothesis are covered.
A family that is small only eventually is not assigned a gap at earlier
spacings. No normal-state subsequence lemma is needed by this ground route.

## 2. A self-contained common-domain propagator construction

We prove the domain fact needed for both the actual and auxiliary evolution.
Let \(B(s)=B(s)^*\) be bounded and norm \(C^1\) on a compact interval,
\(H_s=H+B(s)\), and \(a>0\). Bounded perturbation gives selfadjointness on
the common domain \(\mathcal D\): for \(\eta>\sup\|B(s)\|\), the Neumann
inverse of \(I+B(s)(H\mp i\eta)^{-1}\) makes \(H_s\mp i\eta\) surjective.
The shifted closed forms have the same form domain as \(H\), although \(B(s)\)
need not map either domain into itself.

First construct the Hilbert-space propagator without claiming domain
invariance. The interaction-picture generator
\(a e^{iasH}B(s)e^{-iasH}\) is bounded, selfadjoint and strongly continuous.
Its iterated strong integrals converge on every vector, uniformly on compact
intervals, by the exponential-series bound. The bounded equation and its
backward equation give a unitary two-parameter propagator. Returning to the
free picture gives \(U(s,r)\), strongly jointly continuous, with the composition
law and the free Duhamel identity. For each fixed \(\eta\in\mathcal D\), that
identity, differentiating the free unitary on the test vector, gives
\[
 \frac d{ds}\langle\eta,U(s,r)x\rangle
      =-ia\langle H_s\eta,U(s,r)x\rangle                                 \tag{P8}
\]
for every \(x\in\mathcal H\). Inner products are antilinear in the first entry.
This is a weak equation; it does not assert \(U(s,r)x\in\mathcal D\).

Choose \(L>\sup_s\|B(s)\|\), and define
\[
 Y_s=H_s+L,\quad J_s=Y_s^{-1},\quad C_s=B'(s)J_s.
\]
The bounded resolvent identity proves
\[
 J_s'=-J_sB'(s)J_s,\qquad
 HJ_s=I-(B(s)+L)J_s.                                                       \tag{P9}
\]
Both right sides are norm continuous and the second identity is norm \(C^1\).
Difference quotients and closedness of \(H\) therefore show that \(J_s\) is
\(C^1\) as a bounded map \(\mathcal H\to\mathcal D\) with its fixed graph norm.

For any \(z_r\in\mathcal H\), solve the bounded Volterra equation
\[
 z(s)=U(s,r)z_r+\int_r^s U(s,u)C_u z(u)\,du.                               \tag{P10}
\]
Picard iteration with the same exponential majorant gives a unique continuous
solution. No domain property of \(z\) is used. Applying (P8), with Fubini for
bounded continuous weak integrands, yields
\[
 \frac d{ds}\langle\eta,z(s)\rangle
   =-ia\langle H_s\eta,z(s)\rangle+\langle\eta,C_sz(s)\rangle,\quad
 \eta\in\mathcal D.                                                       \tag{P11}
\]
The integrated identity also holds for graph-\(C^1\) test paths, with the
additional derivative of the test. This follows by finite-difference sums:
use (P11) for the fixed test at each subdivision endpoint and pass to the
graph-norm limit. The estimates use continuity of \(z\), boundedness of \(C\),
and graph continuity of the tests, so do not assume differentiability of \(z\).

Set \(u(s)=J_sz(s)\), and use the graph-\(C^1\) test \(J_s\eta\) for any
\(\eta\in\mathcal H\). Since \(H_sJ_s=I-LJ_s\) is bounded selfadjoint, the
product rule in integrated weak form is legitimate and gives
\[
 \frac d{ds}\langle\eta,u(s)\rangle
 =\langle\eta,[J_s'+J_sC_s]z(s)-iaH_sJ_sz(s)\rangle
 =\langle\eta,-iaH_sJ_sz(s)\rangle.                                       \tag{P12}
\]
The first two terms cancel by (P9). The last vector is norm continuous.
Testing its vector integral against all \(\eta\) proves that \(u\) is strongly
\(C^1\), belongs to \(\mathcal D\), and solves \(u'=-iaH_su\).
Moreover \(Y_su(s)=z(s)\) is continuous, so \(u\) is graph continuous.

For \(u_r\in\mathcal D\) choose \(z_r=Y_ru_r\). This strong solution equals
the originally constructed \(U(s,r)u_r\): transforming this already regular
solution to the interaction picture gives the bounded equation with its
unique solution. This step does not assume domain invariance of the original
Dyson evolution. Reversing the construction in time proves onto-\(\mathcal D\)
propagation. It also gives \(\partial_rU(s,r)x=iaU(s,r)H_rx\) for \(x\in\mathcal D\),
using the composition law and the strong equation.

Unitarity, (P10) and Gronwall yield
\[
 \|Y_sU(s,r)Y_r^{-1}\|
 \le \exp\!\left(\int_{\min(r,s)}^{\max(r,s)}
                  \|B'(u)Y_u^{-1}\|\,du\right).                          \tag{P13}
\]
For reversed time the signed integral equation gives the same bound.
The graph transform is also jointly strongly continuous: its Volterra
equation is (P10) with initial datum a fixed Hilbert vector. Each iterated
kernel is strongly jointly continuous, and the norm majorant makes the series
uniform on compact parameter sets. These facts justify graph-continuous
integrands later, not merely bounded graph norms.

For the actual ramp take \(a=\tau\), \(B(s)=sV\), \(L=m\), and write
\[
 Y_s=H_s+m\ge(m-K)I,\quad
 \kappa=\frac K{m-K},\quad \mathfrak g=e^\kappa,\quad
 \|Y_sU_\tau(s,r)Y_r^{-1}\|\le e^{\kappa|s-r|}.                            \tag{P14}
\]
This estimate is independent of \(\tau,c\). The vacuum belongs to \(\mathcal D\),
so its entire ramp path is in that domain, is Hilbert \(C^1\), and is graph
continuous. Nothing here applies \(H\) to an arbitrary interaction-picture
Dyson vector or assumes \(V\mathcal D\subset\mathcal D\).

## 3. Ground branch, reduced resolvent, and graph derivatives

For the actual \(H\), the circle \(|z|=m/2\) lies in the resolvent of every
\(H_s\), since its free distance is at least \(m/2\) and \(sK<m/2\).
The Neumann series gives a norm-continuous Riesz projection starting with
rank one. Two orthogonal projections at distance less than one have the same
finite rank: their restrictions to one another's ranges are injective.
A finite subdivision of \([0,1]\) therefore preserves rank one.
The same Neumann test off the \(sK\)-neighborhood of the free spectrum gives
\[
 \sigma(H_s)\subset[-sK,sK]\cup[m-sK,\infty).
\]
The first cluster is a simple ground energy \(E_s\in[-sK,sK]\); the rest is
separated from it by at least \(\delta=m-2K\). This uses the actual spectrum,
not a full-carrier extension with artificial zero modes.
In the supplied Fock application the free vacuum is even. For even \(V\),
the odd spectrum is at least \(m-sK>sK\ge E_s\), so the ground line is even.
The actual ramp preserves parity by uniqueness of its evolution.

The fixed contour is norm smooth under bounded \(V\). Multiplying its
resolvent by \(H\) shows graph smoothness as well:
\(H(H_s-z)^{-1}=I+(z-sV)(H_s-z)^{-1}\).
A local normalized graph-smooth ground section gives Hellmann-Feynman,
\[
 E_s'=\operatorname{Tr}(P_sV),\qquad |E_s'|\le K.                          \tag{P15}
\]
Put \(Q_s=I-P_s\), and let \(R_s\) be the inverse of \(H_s-E_s\) on \(Q_s\),
extended by zero on \(P_s\). Thus
\[
 \|R_s\|\le\delta^{-1},\quad
 (H_s-E_s)R_s=Q_s,\quad H_sR_s=Q_s+E_sR_s.
\]
It maps \(\mathcal H\) into \(\mathcal D\). It is not an inverse on the ground
line. Differentiating the eigenprojection and inverse relations gives
\[
 P_s'=-R_sVP_s-P_sVR_s,\qquad
 R_s'=-R_s(V-E_s')R_s-P_s'R_s-R_sP_s'.                                    \tag{P16}
\]
For a direct inverse differentiation one may use
\((H_s-E_s+\delta P_s)^{-1}=R_s+\delta^{-1}P_s\) on the common domain;
this avoids an inverse on a kernel. The first identity also follows by
multiplying the derivative of \((H_s-E_s)P_s=0\) by \(R_s\).
The off-diagonal selfadjoint block norm and (P16) give
\[
 \|P_s'\|\le K/\delta,\qquad
 \|R_s'\|\le4K/\delta^2,\qquad
 \|P_s''\|\le10K^2/\delta^2.                                               \tag{P17}
\]
For the last constant, differentiating \(P_s'\) gives two \(R_s'\) terms
costing \(8K^2/\delta^2\), and two \(P_s'\) terms costing \(2K^2/\delta^2\).

Define the anti-selfadjoint \(A_s\) and selfadjoint \(X_s\) by
\[
 A_s=[P_s',P_s],\qquad X_s=R_sP_s'P_s+P_sP_s'R_s.
\]
Then
\[
 \|A_s\|\le K/\delta,\quad \|X_s\|\le K/\delta^2,\quad
 \|X_s'\|\le30K^2/\delta^3,\quad [A_s,P_s]=P_s'.                           \tag{P18}
\]
The \(X_s\) estimate uses its off-diagonal block norm. Its six derivative
terms cost \(8+20+2=30\). The crucial product identities are
\[
 H_sX_s=P_s'P_s+E_sX_s\text{ on }\mathcal H,\qquad
 X_sH_s=P_sP_s'+E_sX_s\text{ on }\mathcal D,\qquad
 [H_s,X_s]=A_s\text{ on }\mathcal D.                                      \tag{P19}
\]
Both products have bounded extensions, and \(X_s\mathcal H\subset\mathcal D\).

We also need the genuine graph derivative, beyond the bounded Hilbert
derivative. Put \(Z_s=P_s'P_s+(E_s+m)X_s\). It is norm \(C^1\) using only
the already established norm derivatives. Since \(X_s=Y_s^{-1}Z_s\) and
\(Y_s^{-1}\) is graph \(C^1\) by (P9), \(X_s\) is graph \(C^1\).
Equivalently, at fixed \(s\), differentiate
\(H_sX_r=H_rX_r-(r-s)VX_r\) by closed-operator difference quotients.
Both arguments give
\[
 X_s'\mathcal H\subset\mathcal D,\qquad
 Y_sX_s'=P_s''P_s+(P_s')^2+(E_s'-V)X_s+(E_s+m)X_s'.                        \tag{P20}
\]
All right sides are norm continuous. The factor \(VX_s\) is bounded;
there is no hidden assumption that \(V\) maps an energy domain into itself.

## 4. Explicit adiabatic integration

Let \(U_A(s,0)\) solve
\[
 U_A'=(-i\tau H_s+A_s)U_A,\qquad U_A(0,0)=I.
\]
The domain lemma applies with bounded norm-\(C^1\) perturbation
\(sV+iA_s/\tau\). It is selfadjoint after multiplication by \(\tau\),
so \(U_A\) is unitary and preserves \(\mathcal D\).
Its graph constant may depend on fixed \(\tau\); no such constant is used
in the estimates. Differentiating on \(\mathcal D\) and extending by boundedness,
\[
 (U_A^*P_sU_A)'=0,\qquad P_sU_A(s,0)=U_A(s,0)P_0.
\]
Consequently \(\phi_s=U_A(s,0)\Omega\) is a unit vector in the exact
instantaneous ground line. This is an auxiliary comparison evolution;
the actual protocol contains no \(A_s\) term.

For \(W=U_\tau(s,0)^*U_A(s,0)\) and
\(F=U_\tau(s,0)^*X_sU_A(s,0)\), the product rules and (P19) give
\[
 W'=U_\tau^*A_sU_A,\qquad
 F'=i\tau U_\tau^*A_sU_A+
       U_\tau^*(X_s'+X_sA_s)U_A.                                         \tag{P21}
\]
These identities first hold on \(\mathcal D\). The graph regularity in
(P20) and the common-domain evolution justify the products. Their right
sides have bounded strong integrals, so density extends the integrated
identities to every vector. No operator-norm derivative of an unbounded
free unitary is asserted.

Eliminating \(A_s\), integrating and using unitarity gives
\[
 \|U_\tau(s,0)-U_A(s,0)\|\le C_{\rm ad}/\tau,\qquad
 C_{\rm ad}=\frac{2K}{\delta^2}+\frac{31K^2}{\delta^3},\qquad
 e_\tau=\min(1,C_{\rm ad}/\tau),\quad 0\le s\le1.                          \tag{P22}
\]
There are two endpoint terms \(2K/\delta^2\); the integral costs at most
\((30+1)K^2/\delta^3\). A linear switch is not flat at its endpoints,
and neither endpoint term has been dropped.

The exact pure-state distance formula, obtained on the span of two unit
vectors, now gives
\[
 \|(I-P_s)\psi_\tau(s)\|\le e_\tau,\qquad
 \|\rho_\tau(s)-P_s\|_1
   =2\|(I-P_s)\psi_\tau(s)\|\le2e_\tau.                                   \tag{P23}
\]
The transition probability is at most \(e_\tau^2\). This alone is not an
estimate of an unbounded energy observable; that needs the following arguments.

## 5. Actual work, the free-energy cap, and form transport

Let \(q_\tau(s)=\langle\psi_\tau(s),H_s\psi_\tau(s)\rangle\).
The domain lemma gives a Hilbert-\(C^1\), graph-continuous path, sufficient
for the true work identity. To check it without \(\mathcal D(H^2)\), write
\(\Delta\psi=\psi_\tau(s+h)-\psi_\tau(s)\) and separate
\(H_{s+h}-H_s=hV\). The remaining difference of quadratic forms is
\[
 \langle\Delta\psi,H_s\psi_\tau(s+h)\rangle
       +\langle H_s\psi_\tau(s),\Delta\psi\rangle.
\]
After division by \(h\), Hilbert differentiability and graph continuity give
\(2\operatorname{Re}\langle\psi_\tau'(s),H_s\psi_\tau(s)\rangle=0\).
Thus
\[
 q_\tau'(s)=\langle\psi_\tau(s),V\psi_\tau(s)\rangle,\qquad
 q_\tau(s)\le sK,\qquad
 0\le\langle\psi_\tau(s),H\psi_\tau(s)\rangle\le2sK.                        \tag{P24}
\]
There is no derivative of \(H_s\psi_\tau\) in this calculation.

The actual excess \(d_\tau(s)=q_\tau(s)-E_s\) is nonnegative by the ground
property. By (P15), (P23) and \(d_\tau(0)=0\),
\[
 d_\tau(s)=\int_0^s\operatorname{Tr}[(\rho_\tau(r)-P_r)V]\,dr,\qquad
 0\le d_\tau(s)\le2Ks\,e_\tau.                                           \tag{P25}
\]
The integrand need not be nonnegative. Trace distance is used only against
bounded \(V\), and (P25) concerns the actual unbounded \(H_s\).
The free bound \(2sK\) is stronger than the valid but unnecessary
\(2K+d_\tau(1)\) estimate in the initial root source.

A second use of the same work identity gives form transport. For any
\(u\in\mathcal D\), the norm of \(U_\tau(s,r)u\) is \(\|u\|\), and
\[
 \begin{split}
 \|Y_s^{1/2}U_\tau(s,r)u\|^2
 &\le\|Y_r^{1/2}u\|^2+K|s-r|\|u\|^2\\
 &\le\left(1+\frac{K|s-r|}{m-K}\right)\|Y_r^{1/2}u\|^2 .
 \end{split}                                                            \tag{P26}
\]
Both time orders follow by integrating the absolute work bound. There is
no factor \(\tau\) in this work term: the \(\tau H_s\) contributions cancel.

Extend (P26) to the form domain by spectral truncation of \(Y_r\).
These approximants lie in \(\mathcal D(Y_r)=\mathcal D\), converge in form
norm, and their evolved pairwise differences obey (P26).
The evolved sequence is Cauchy in the final form norm. Unitarity identifies
its Hilbert limit, and closedness of \(Y_s^{1/2}\) gives the desired form
limit. Reverse time gives onto-form-domain propagation. Consequently
\[
 \|Y_s^{1/2}U_\tau(s,r)Y_r^{-1/2}\|\le M,\qquad
 M=\sqrt{\frac m{m-K}}<\sqrt2,\qquad 0\le r,s\le1.                         \tag{P27}
\]
No form-domain invariance of \(V\) was assumed or inferred.

## 6. Quadratic actual excess energy, with the form integral justified

From (P19)-(P20), uniformly in \(s\),
\[
 \begin{split}
 \|Y_sX_s\|&\le u:=\frac{K(2m-K)}{\delta^2},\\
 \|Y_sX_s'\|&\le v_*:=\frac{K^2(43m+4K)}{\delta^3}.
 \end{split}                                                            \tag{P28}
\]
For the second line, the five terms in (P20) cost
\(13K^2/\delta^2+30(m+K)K^2/\delta^3\).
Here \(13=10+1+1+1\), and \(13\delta+30(m+K)=43m+4K\).
The first line uses \(K/\delta+(m+K)K/\delta^2=K(2m-K)/\delta^2\).

For a bounded \(Z\) with bounded \(Y_sZ\) and range in \(\mathcal D\),
pairing \(Zx\) with \(Y_sZx\) gives
\(\|Y_s^{1/2}Z\|^2\le\|Z\|\|Y_sZ\|\).
Use this on \(X_s\) and \(X_s'\), and put \(T_s=X_s'+X_sA_s\).
Equations (P18), (P28) imply
\[
 \begin{split}
 a_*&=\frac{K\sqrt{2m-K}}{\delta^2},\\
 b_*&=\frac{K^2}{\delta^3}
          \left[\sqrt{30(43m+4K)}+\sqrt{2m-K}\right],\\
 \|Y_s^{1/2}X_s\|&\le a_*,\qquad
 \|Y_s^{1/2}T_s\|\le b_* .
 \end{split}                                                            \tag{P29}
\]
The last summand in \(b_*\) is \(a_*\|A_s\|\le a_*K/\delta\).
These constants do not use a commutator with \(V\).

The exact variation formula is
\(\psi_\tau(s)-\phi_s=-\int_0^sU_\tau(s,r)A_r\phi_r\,dr\).
Differentiation of \(U_\tau(s,r)X_r\phi_r\) gives
\(i\tau U_\tau(s,r)A_r\phi_r+U_\tau(s,r)T_r\phi_r\).
The positive sign uses the derivative in the initial time of the propagator.
Integration therefore gives
\[
 \xi_s:=\psi_\tau(s)-\phi_s
 =\frac1{i\tau}\left[
 U_\tau(s,0)X_0\Omega-X_s\phi_s+
         \int_0^sU_\tau(s,r)T_r\phi_r\,dr\right].                          \tag{P30}
\]
All signs and both endpoint terms are retained.

For completeness, the last integral exists in the fixed final form space,
not merely as a Hilbert integral with a pointwise bound. Set \(f_r=T_r\phi_r\).
By (P20), \(T_r\) is norm continuous into the common graph space; since
\(\phi_r\) is Hilbert continuous, \(f_r\) is graph continuous.
For fixed \(r_0\), the common-domain lemma makes
\(U_\tau(r,r_0)f_{r_0}\) graph continuous. Hence
\(w_r=f_r-U_\tau(r,r_0)f_{r_0}\) tends to zero in the graph norm of \(Y_r\).
The interpolation inequality
\(\|Y_r^{1/2}w_r\|^2\le\|w_r\|\|Y_rw_r\|\) tends to zero.
The composition law and (P27) then give
\[
 \|Y_s^{1/2}[U_\tau(s,r)f_r-U_\tau(s,r_0)f_{r_0}]\|
       \le M\|Y_r^{1/2}w_r\|\longrightarrow0.
\]
Thus the integrand is continuous in the fixed final form norm.
Riemann sums converge in that complete space; because \(Y_s\ge(m-K)I\),
their Hilbert limit is the integral in (P30). This proves the required
integration/closure step without assuming that a mere form bound implies
form continuity.

Now (P27), (P29), \(s\le1\), and (P30) show
\[
 \|Y_s^{1/2}\xi_s\|\le D_*/\tau,\qquad
 D_*=(1+M)a_*+Mb_*.
\]
The auxiliary ground vector is annihilated by \((H_s-E_s)^{1/2}\), and
\(0\le H_s-E_s\le Y_s\) as forms since \(m+E_s\ge m-K>0\).
Consequently the promised actual energy bound is
\[
 0\le d_\tau(s)
   =\|(H_s-E_s)^{1/2}\psi_\tau(s)\|^2
   =\|(H_s-E_s)^{1/2}\xi_s\|^2
   \le\frac{D_*^2}{\tau^2},\qquad 0\le s\le1.                             \tag{P31}
\]
The actual vector lies in \(\mathcal D(H_s)\), so this form expression
equals its unbounded operator expectation. Combining (P25) and (P31)
permits the smaller bound \(\min(2Ks\,e_\tau,D_*^2/\tau^2)\).
No transition-probability argument has been substituted for energy control.
No optimality of the coefficient or of the power is claimed.

## 7. The independent graph coefficient as a recorded check

The separately frozen rate derivation estimates the same identity (P30) in
the operator graph norm. From (P28),
\(\|Y_sT_s\|\le v_*+(K/\delta)u\). The joint strong graph continuity proved
after (P13) makes the integrand graph continuous, so graph-space Riemann
sums justify applying \(Y_s\) under its integral. Thus
\[
 \|Y_s\xi_s\|\le C_{\rm gr}/\tau,\quad
 C_{\rm gr}=(1+\mathfrak g)u+\mathfrak g[v_*+(K/\delta)u],\quad
 C_{\rm en}=C_{\rm ad}C_{\rm gr}.                                         \tag{P32}
\]
Using (P22), the exact ground equation and \(m+E_s>0\) gives
\(d_\tau(s)=\langle\xi_s,Y_s\xi_s\rangle-(m+E_s)\|\xi_s\|^2
\le C_{\rm en}/\tau^2\).

The completed source comparison also establishes \(D_*^2\le C_{\rm en}\).
Indeed put \(x=K/\delta^2\), \(y=30K^2/\delta^3\), \(z=K/\delta\). Then
\(C_{\rm ad}=2x+y+xz\) and
\[
 D_*=\sqrt{xu}+M\sqrt{xu}+M\sqrt{yv_*}+Mz\sqrt{xu}.
\]
Since \(M^2=1+\kappa\le e^\kappa=\mathfrak g\), the four terms are bounded by
\(\sqrt{xu},\sqrt{x\mathfrak gu},\sqrt{y\mathfrak gv_*},
\sqrt{(xz)(\mathfrak guz)}\), respectively.
Four-term Cauchy-Schwarz gives
\[
 D_*^2\le(2x+y+xz)
       [u+\mathfrak gu+\mathfrak gv_*+\mathfrak guz]
       =C_{\rm en}.                                                     \tag{P33}
\]
This compares the recorded sufficient constants. It is not an optimality
theorem or new independent evidence supplied by this assembly.

## 8. Arbitrary final autonomous hold and actual high occupation

After preparation define, for every waiting time \(w\ge0\),
\[
 \rho_{\tau}^{\rm hold}(w)
 =e^{-iwG}\rho_\tau(1)e^{iwG},\qquad G=H+V,\quad P_g=P_1.
\]
The final spectral evolution preserves \(\mathcal D(G)=\mathcal D(H)\);
it commutes with \(P_g\) and with \(G-E_1\). Therefore
\[
 \begin{split}
 \|\rho_{\tau}^{\rm hold}(w)-P_g\|_1&\le2e_\tau,\\
 \operatorname{Tr}\rho_{\tau}^{\rm hold}(w)(G-E_1)
    &=d_\tau(1)\le\min(2Ke_\tau,D_*^2/\tau^2),\\
 0\le\operatorname{Tr}\rho_{\tau}^{\rm hold}(w)H&\le2K .
 \end{split}                                                            \tag{P34}
\]
The last line uses conservation of
\(\operatorname{Tr}\rho_{\tau}^{\rm hold}(w)G=q_\tau(1)\le K\), and
\(|\operatorname{Tr}\rho_{\tau}^{\rm hold}(w)V|\le K\).
These facts hold for arbitrarily large \(w\), with no comparison of
finite-spacing and target propagators at that large time.

For the actual bands, (P7) gives at every \(\tau>0,w\ge0\)
\[
 \operatorname{Tr}\widehat\rho_{c,\tau}^{\rm hold}(w)N_H
 \le\frac{2K}{\Lambda_c},\qquad
 \operatorname{Tr}\widehat\rho_{c,\tau}^{\rm hold}(w)Q_H
 \le\frac{2K}{\Lambda_c}.                                                 \tag{P35}
\]
Here \(\widehat\rho=\iota_c\rho\iota_c^*\).
No conservation of high number under the interaction was assumed.
Both actual branches remain present at every finite spacing.
The high bound is a consequence of actual free-energy control; it does not
replace the ground-distance or vanishing-excess hypothesis.

## 9. Joint continuum and slow-preparation ground limit

Use the static comparison hypotheses of section 1. We recall the exact
bounded ground theorem needed here, with its compression conventions.
Choose any fixed \(\mu>K\), and put on the common carrier
\[
 \begin{aligned}
 \mathsf R_c&=\iota_c(H_c+\mu)^{-1}\iota_c^*,&
 \mathsf R_0&=(H_0+\mu)^{-1}\otimes|\Omega_H\rangle\langle\Omega_H|,\\
 \mathsf S_c&=\iota_c(H_c+V_c+\mu)^{-1}\iota_c^*,&
 \mathsf S_0&=(H_0+V_0+\mu)^{-1}\otimes|\Omega_H\rangle\langle\Omega_H|.
 \end{aligned}
\]
These are zero-extended **compressed resolvents**, with kernels off their
physical ranges. They are not full-carrier Hamiltonian resolvents obtained
by assigning zero physical energy to missing modes.

For reference, the actual free comparison is
\(\|\mathsf R_c-\mathsf R_0\|\le c/v\).
Its low-band proof follows directly from (P6):
on \(I_c\), \(1-w_c\le c|p|\) and \(e_{c,L}+E\ge2v|p|\), so
\[
 e_{c,L}-E
 =\frac{v^2p^2(1-w_c)}{(1+w_c)(e_{c,L}+E)}
 \le\frac{cv}{2}p^2\le\frac{c}{2v}E^2.
\]
At \(p=0\) the difference is zero.
For a finite low configuration, \(x=\sum E_i\), \(y=\sum e_{c,L,i}\) obey
\(0\le y-x\le cx^2/(2v)\), and its resolvent difference is at most \(c/(2v)\).
The bound is uniform in particle number and is zero on the vacuum.
On \(P_H(I-\Pi_c)\), target energy is at least
\(\sqrt{m^2+v^2/c^2}\); on \(Q_H\Pi_c\), actual energy is at least
\(\Lambda_c\); on \(Q_H(I-\Pi_c)\), both compressions vanish.
Taking the maximum of these reducing-block bounds gives \(c/v\).
The ground source also records a smaller low-block coefficient; the global
bound used here is the same.

Neumann series with \(\|\mathsf R_c\|,\|\mathsf R_0\|\le1/\mu\) and the
in-band reduction hypotheses give the exact identity
\[
 \mathsf S_c-\mathsf S_0
 =(I+\mathsf R_c\widehat V_c)^{-1}
 [\mathsf R_c-\mathsf R_0+
       \mathsf R_c(\widehat V_0-\widehat V_c)\mathsf R_0]
 (I+\widehat V_0\mathsf R_0)^{-1}.
\]
On the complements it follows by zero extension; no inverse of a compression
on its kernel is taken. It requires no commutation of \(\widehat V_c\) with
\(P_H\). Hence the checked constants are
\[
 \|\mathsf S_c-\mathsf S_0\|\le\varepsilon_c,\qquad
 \varepsilon_c=\frac{\mu^2c/v+\nu_c}{(\mu-K)^2},\quad
 d_\mu=\frac{\delta}{(\mu+K)(\mu+m-K)},\quad
 b_c=\min(1,\varepsilon_c/d_\mu).                                         \tag{P36}
\]
Both top ground eigenvalues are at least \(1/(\mu+K)\); the entire
complementary spectrum of \(\mathsf S_0\), including its zero kernel, is at
most \(1/(\mu+m-K)\). Applying its inverse separation to the component of an
actual ground vector orthogonal to the target ground gives norm at most
\(\varepsilon_c/d_\mu\). The rank-one trace formula therefore yields
\[
 \|\widehat P_{g,c}-\widehat P_{g,0}\|_1\le2b_c.                            \tag{P37}
\]
Here \(\widehat P_{g,0}\) is the rank-one density of the target interacting
ground vector tensored with the **high vacuum**, not \(P_{g,0}\otimes I_H\).
The potential and observable embeddings, in contrast, are unital.

Combining (P23), (P34), and (P37) gives the central preparation consequence
\[
 \sup_{w\ge0}
 \|\widehat\rho_{c,\tau}^{\rm hold}(w)-\widehat P_{g,0}\|_1
 \le 2e_\tau+2b_c.                                                       \tag{P38}
\]
The right side can also be capped by \(2\). It tends to zero for every
\(\tau=\tau(c)\to\infty\), through every allowed \(c\to0\), with no
subsequence and no required relation between the two scales.
The actual excess at that spacing is at most \(D_*^2/\tau(c)^2\);
a continuum energy has not been substituted in that statement.
Every spacing-dependent waiting time \(w(c)\ge0\) is allowed.

The argument compares preparation with its own instantaneous ground uniformly
in \(c\), and only then compares static ground densities. It never applies a
fixed-time free comparison to the diverging physical duration \(\tau(c)\).
It asserts convergence of densities, not of vector phases or of complete
propagator groups uniformly for all times. It uses the ground theorem in the
supplied representation and does not classify inequivalent ground-state
representations.

## 10. Compact relative-time correlations under norm-orbit hypotheses

For the specified separately even in-band observable blocks
\(\widehat A_{j,c}\) and low target blocks \(A_{j,0}\), suppose their norms
are at most \(L_j\), and let \(\alpha_c,\alpha_0\) be the free CAR flows.
For every fixed \(T<\infty\), require
\[
 \begin{split}
 \nu_{V,c}(T)&=\sup_{|t|\le T}
  \|\alpha_{c,t}(\widehat V_c)-\alpha_{0,t}(V_0)\otimes I_H\|\longrightarrow0,\\
 \nu_{j,c}(T)&=\sup_{|t|\le T}
  \|\alpha_{c,t}(\widehat A_{j,c})-\alpha_{0,t}(A_{j,0})\otimes I_H\|
       \longrightarrow0 .
 \end{split}                                                            \tag{P39}
\]
These are additional dynamical comparison premises. Time-zero potential
convergence is sufficient for section 9 but is not used as a substitute for
(P39) in an arbitrary varying-potential class.

For example choose a block-diagonal one-particle free extension off the actual
band, zero there if desired, and let \(\widehat H_c\) implement its flow on the
common carrier. Its restriction to \(\Pi_c\mathcal F_*\) is the actual
\(H_c\). Put \(\widehat G_c=\widehat H_c+\widehat V_c\).
The possible artificial zero modes of this extension play no role in the
actual preparation or gap proof. At the target use \(H_0\otimes I_H\) and
\((H_0+V_0)\otimes I_H\) for these **unital observable** comparisons.

The bounded cocycle
\(Z_c(t)=e^{it\widehat G_c}e^{-it\widehat H_c}\) satisfies
\[
 Z_c'=iZ_cB_c(t),\quad B_c(t)=\alpha_{c,t}(\widehat V_c),\quad Z_c(0)=I.
\]
To justify this identity, differentiate on the common operator domain of
\(\widehat H_c,\widehat G_c\); the unbounded terms combine to
\(i e^{it\widehat G_c}\widehat V_c e^{-it\widehat H_c}\).
This does not apply \(\widehat H_c\) to \(\widehat V_c x\).
The point-norm continuous CAR coefficient gives a unique norm-continuous
bounded integral equation and unitary solution in even CAR. Strong uniqueness
on the dense domain identifies it with the implementing product. Thus
\(\beta_{c,t}(A)=Z_c(t)\alpha_{c,t}(A)Z_c(t)^*\) is the interacting CAR flow.

With the target cocycle tensored with \(I_H\), the right-generator order gives
\((Z_cZ_0^*)'=iZ_c(B_c-B_0)Z_0^*\). Unitarity and integration in either time
direction prove
\[
 \|Z_c(t)-Z_0(t)\|\le |t|\nu_{V,c}(T),\qquad
 \sup_{|t|\le T}\|\beta_{c,t}(\widehat A_{j,c})
                 -\beta_{0,t}(A_{j,0})\otimes I_H\|
 \le\nu_{j,c}(T)+2T\|A_{j,0}\|\nu_{V,c}(T).                              \tag{P40}
\]
There is no exponential factor. For the entire finite ordered word, put
\[
 W_c(\mathbf u)=\prod_{j=1}^n\beta_{c,u_j}(\widehat A_{j,c}),\quad
 W_0(\mathbf u)=\prod_{j=1}^n\beta_{0,u_j}(A_{j,0}),\quad L=\prod_j L_j .
\]
A product telescoping expansion gives
\[
 \sup_{\mathbf u\in[-T,T]^n}
 \|W_c(\mathbf u)-W_0(\mathbf u)\otimes I_H\|
 \le\zeta_c(T):=\sum_{j=1}^n
       [\nu_{j,c}(T)+2T\|A_{j,0}\|\nu_{V,c}(T)]
                    \prod_{k\ne j}L_k\longrightarrow0.                 \tag{P41}
\]
The empty omitted-factor product equals one. This bound compares complete
unital products. It neither replaces a compression of a product by products
of compressions nor assumes energy bounds after observable insertions.

Using (P38), the actual restrictions \(W_c^{\rm actual}\), and (P41),
\[
 \begin{split}
 &\sup_{\substack{w\ge0\\\mathbf u\in[0,T]^n}}
 \big|\,\operatorname{Tr}\rho_{c,\tau}^{\rm hold}(w)
                      W_c^{\rm actual}(\mathbf u)
       -\operatorname{Tr}\widehat P_{g,0}
                       (W_0(\mathbf u)\otimes I_H)\,\big|\\
 &\qquad\le \zeta_c(T)+2L(e_\tau+b_c).
 \end{split}                                                            \tag{P42}
\]
These observation times in the actual protocol are
\(t_j=\tau+w+u_j\). The waiting time may diverge with spacing because the
holding state remains equally close to its stationary ground. The relative
window \(T\) is fixed. The product order need not be chronological.
The mathematical operator bound (P41) also holds on the symmetric cube;
a physical protocol interpretation of negative relative times additionally
requires \(w+u_j\ge0\), so that observations occur after switching.

For every \(\tau(c)\to\infty\), (P42) tends to zero uniformly in \(w\ge0\)
on each fixed relative window. No comparison on the interval of length
\(\tau(c)+w(c)\) has been asserted. A growing relative window would require
a separate bound making \(\zeta_c(T(c))\to0\).

The actual ordinary-cell class supplied by Local sections 3 and 6 and
Current C21/C25 satisfies (P39). For a real compactly supported \(L^2\) coefficient field \(f\),
the physical cell average is
\[
 (C_cf)_j=c^{-1/2}\int_{cj}^{c(j+1)}f(x)\,dx,\qquad
 \|C_cf\|\le\|f\|,\qquad
 \sup_{|t|\le T}\|J_ce^{itD_c}C_cf-(e^{itD}f,0)\|\to0.                    \tag{P43}
\]
The time-zero statement is included. \(J_c\) is the parent's real coefficient
carrier map; the Fock isometry \(\iota_c\) used for densities is a distinct map.
The CAR field norm is its real coefficient norm. For a degree-\(r\) monomial
with coefficient errors \(d_{k,c}(T)\) and bounds \(b_k\), telescoping gives
error at most \(\sum_k d_{k,c}(T)\prod_{\ell\ne k}b_\ell\).
Finite sums with their scalar coefficients therefore give (P39) and fixed
operator norm bounds for fixed finite even *-polynomials.
A potential must additionally be selfadjoint; evenness alone is insufficient.
Symmetrizing by \((B+B^*)/2\) is one way to ensure this.

Converging \(L^2\) inputs and finitely many converging scalar coefficients are
also allowed with the same bounded-polynomial argument. Local section 6, especially L23-L24, supplies the even-spin representative
in the finite physical cell hull of the compact supports; the cell averaging
in section 3 gives at most one-cell endpoint enlargement. The number of cells can
grow as \(c\to0\); the bound \(K\) must still bound the total polynomial.
The band-limited carrier images are not claimed to retain exact continuum
support. No smoothness, bounded \([H,V]\), or additional energy-transfer
hypothesis is needed for this ordinary \(L^2\)-cell class. No universal
convergence rate in \(c\) is inferred from its \(L^2\) convergence.

## 11. Scope, counterexamples, and formalization limits

All preparation bounds hold for every \(\tau>0\), every \(0\le s\le1\),
and every allowed spacing with the same \(m,K\). At \(K=0\) the preparation
error constants \(C_{\rm ad},D_*\) vanish. The graph factor satisfies
\(\mathfrak g<e\) and the form
factor \(M<\sqrt2\); neither grows with duration or bandwidth.
As \(\delta\downarrow0\) the displayed constants can diverge. The argument
does not cover \(m=0\), \(K=m/2\), unbounded \(V\), or an extensive interaction
without a uniform total norm bound. A per-cell interaction bound alone does
not supply (P2). The switch and exact initial vacuum remain external inputs;
arbitrary initial states are not covered by (P23) or (P31).

The fixed-cap counterexample in the exact ground synthesis remains valid:
already for \(V=0\), a small fixed mixture of vacuum and an actual even
two-particle low-band state has a positive uniformly bounded free energy,
and can stay distinguishable from vacuum by an ordinary even local test.
Thus a positive fixed cap, including \(2K\) when \(K>0\), does not by itself
select the ground. This protocol supplies
vanishing actual excess through (P31), as well as the stronger direct
trace-distance estimate. It does not derive the protocol from a state
primitive or prove autonomous relaxation, thermalization, typicality, or
control availability.

The same ground source gives an even bounded rough-cell interaction whose
action on the free vacuum lies outside the free form domain. That example is
consistent with this proof: bounded perturbation preserves the operator and
form domains **as domains of the Hamiltonians**, without requiring \(V\) to
preserve those domains on arbitrary vectors. The common-domain propagator
lemma and the \(X_s'\) graph proof are therefore essential; smooth-cell domain
assumptions have not been silently inserted.

The even physical ramp starting from vacuum remains in the even sector.
The theorem nevertheless uses the full-Fock gap \(\delta=m-2K\).
It does not transfer an even-sector gap to arbitrary states or assert that
support in a fixed parity sector passes under arbitrary CAR limits.
Here trace convergence to the specific even interacting ground follows from
the stronger preparation-and-gap argument. General energy-controlled CAR
subsequences, their possible parity-sector escape, and their normality proof
are separate statements, not ingredients of (P38).

The parent interaction note's saved finite Clifford identity concerns
normalized algebraic generators. It does not establish a propagator,
selfadjointness, a spectral gap, energy-domain regularity, or any adiabatic
bound. Its unnormalized cell identity retains the factor \(n_{1,c}^2\)
described there. This companion makes no extension of that finite Lean
scope and claims no Lean or numerical execution. The arguments here are
ordinary conditional analysis. No formal audit, retained classification,
novel adiabatic mechanism, rate optimality, smooth-cell rate, response result,
or newly selected physical axiom is claimed.

## 12. Exact sources, comparison exposure, and review boundary

The primary assembly inputs below are copied byte-for-byte under
`adiabatic_preparation_synthesis/inputs`. The complete initial preparation
root source, its comparison, and the ground assembly review were newly read
without truncation during this assembly. Complete prior reads of the other
five inputs were reused at verified unchanged identities; necessary domain,
static-ground and correlation passages were also refreshed directly.
The author wrote the independent rate core and its subsequent source-exposed
comparison, as well as the prior ground synthesis. This assembly is therefore
a source-exposed coauthor operation, not an independent check of those works.

| Exact input | SHA-256 |
|---|---|
| `ADIABATIC_PREPARATION_ROOT_PROBE.md` | `47e7c1babb9b51c4772813cb83f34c088f8df950a3d5fac678d8781f6e01e695` |
| `ADIABATIC_PREPARATION_INDEPENDENT.md` | `3ac5a798d0c48822eb2495deed89bfd4bcf5aef4ffa60019dded169aee230eec` |
| `ADIABATIC_PREPARATION_CROSSCHECK.md` | `e66e7741331052b3b9d3bcbb04f4a0c03a594e36fff3e2d6339c4257c4b7d465` |
| `ADIABATIC_ENERGY_RATE_ROOT_ADDENDUM.md` | `5c05a9a8bc926c9a59f4098f009476fc259d55e90eb9b596f34dcdce4ceb69f6` |
| `ADIABATIC_ENERGY_RATE_INDEPENDENT.md` | `9f5339805d51c6a06f755c7cfcf39be21b39e30ae07c9cceb01d94652d164b20` |
| `ADIABATIC_ENERGY_RATE_CROSSCHECK.md` | `3248093cfe4ea554ada8dbc83f719a603eada1d0a353a7742713cc534f87d5d6` |
| `BOUNDED_INTERACTION_GROUND_SYNTHESIS.md` | `b8bcba769100bf819885937d850a7bff8543e4233c1df3cf65f68372552160e9` |
| `BOUNDED_INTERACTION_GROUND_SYNTHESIS_REVIEW.md` | `af0cf7d6e9ea98fc92ac86df651c136cb2766f40571b814b69f3850304ebfe53` |

The ground synthesis pins and supplies the necessary canonical model
premises; their prior complete/necessary semantic coverage is reused here,
rather than represented as a new transitive audit:

| Parent at the selected main revision | SHA-256 | Used premises |
|---|---|---|
| `CURRENT_PRESERVING_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md` | `763082a6faa8bea3f6be74ddc7ee81bf288c00740085804e62f701a1576283ff` | Actual positive-energy isometry, both branches, C21/C25, physical-time convention |
| `CONCRETE_GAPPED_CHAIN_BOUNDED_THEOREM_NOTE_2026-10-12.md` | `2311c445bffc809d3387089c0feb48892f15f535d889121664dabe49fa146b05` | Actual full-spin Fock representation, simple free vacuum, gap and domains |
| `LOCAL_EVEN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-10-12.md` | `b5a8394a9d8c17bb9559597a68b061ad3872201ebf9793bd5c9f10b15ac2c6aa` | Ordinary real fields, compact physical cells and even-spin interpretation |

Their conditional/open dependencies retain that status. The frozen ground
assembly and its ordinary review are provisional source dependencies here,
not authority inherited from a main-branch landing or a retained audit.
The earlier finite-energy and correlation publication history does not
upgrade this companion's status. The full normality lemma is not needed.

The initial preparation comparison records its independent core freeze at
`2026-10-12T18:56:47.519322+00:00`, before its root-proof exposure.
The root quadratic-energy addendum was reported sealed at
`2026-10-12 18:59:28 UTC`. The independent rate source was frozen at
`2026-10-12T19:12:37.439715+00:00` before its root-addendum exposure at
`2026-10-12T19:13:52.835881+00:00`. Those rate proofs share the allowed
preparation core; the derivative and representation premises are shared.
Separate before-comparison drafting within the selected model family does
not remove shared-premise or shared-model error risks. The historical source
comparisons report no theorem-invalidating finding in their scopes; their
outcomes are not substituted for the arguments written above.

The exact new body-return boundaries, reused read coverage, neutral plan,
immutable input copies, complete author-read record and final identity
inventory are in the accompanying evidence directory. Body-return timestamps
record tool exposure boundaries, not exact cognitive timing.
All eight original sources and their prior manifests remain unchanged.
Only this assembly and its assigned evidence directory were written.
No repository or canonical package, Git state, PR, audit, campaign checkpoint,
editable prompt, installation, or scientific runner was changed or executed.

This complete assembled source still requires root acceptance and its own
focused exact-source review. That review has not been predicted by the
ordinary comparisons of its inputs.





## Publication dependency, protocol and joint-limit record

The direct mathematical parent is the [bounded-interaction/ground theorem](BOUNDED_INTERACTION_GROUND_BOUNDED_THEOREM_NOTE_2026-10-12.md).
That note carries the exact Current, Concrete, Local Even and provisional
correlation dependencies. This single direct edge keeps the protocol theorem
and its ground selector in one coherent milestone. The ground/preparation
route does not need the arbitrary-state normal-subsequence lemma to establish
its rank-one ground-density conclusion.

The supplied inputs remain the exact vacuum, massive full-Fock Hamiltonian,
selfadjoint bounded total even interaction, uniform K<m/2, positive gap, and
controlled linear H+sV switch. Common operator domain, graph continuity,
form transport and the actual work estimate are proved in the body without
assuming [H,V] bounded or V D(H) contained in D(H). The O(tau^-2) bound is for
the true unbounded excess energy. It is not inferred from transition
probability alone. The sharper form coefficient and the optional graph
coefficient remain separately identified with their checked comparison.

For any joint c tending to zero and tau(c) tending to infinity under the stated
spacing premises, the prepared density tends to the selected continuum ground.
The result permits an arbitrary subsequent autonomous hold. Fixed relative-time
correlation windows additionally use the explicit norm-orbit comparison premise;
the ordinary finite compact L2 even-polynomial class satisfies it through
Current C21/C25 and the corrected Local support attribution. A diverging ramp
or hold duration is not a global propagator convergence theorem. A growing
relative observation window requires its own vanishing comparison modulus.

## Later companion appendix: scoped quadratic-energy rate witness

The following complete proof was frozen separately at SHA-256
`36b88a3704e2bd4d0063257a2a04160cb1d6ea846ac2af0ee4d893d9f6075e06`.
Its source comparison has SHA-256
`a323115d3f638c0b0010715afbea153b980426e685cdf4f111f3a1ea1d5606e7`.
Root read both in full. The proof below is byte-exact, including its historical
exposure statement. The root comparison core is also archived.

**Scope of this later result.** For one fixed nonzero two-mode even interaction
with norm below m/2, the actual linear-ramp excess has positive liminf after
multiplication by tau squared. This establishes the broad-class exponent
obstruction to a uniform faster power. The leading coefficient oscillates;
no general prefactor or fixed supplied-chain sharpness is claimed. K=0 and
commuting interactions can have zero excess. The finite example's endpoint-flat
protocol comparison is confined to its own proved setting, not promoted to a
general unbounded-energy theorem or a protocol-independent obstruction.

The even transition gap and the full Fock spectral gap are distinct in this
example. The complete remainder estimate, bootstrap threshold and exact
actual-energy calculation are retained. The sign-changing derivative in its
second integration by parts is controlled by absolute bounds. No numerical
runner, formal proof or new scientific computation is supplied here.

### Begin unchanged separately frozen proof


# Independent sharpness of the linear-ramp actual excess-energy rate

Status: ordinary analytic counterexample and conditional quantitative theorem,
independent of any new root sharpness argument. The two assigned independent
preparation/rate notes are shared premises and have been read completely.
No numerical experiment, formal verification, source-comparison verdict,
retained audit, or novelty claim is made.

**Result.** For every fixed `m > 0` and `0 < K < m/2`, the broad class in the
question contains one fixed, even, two-mode fermionic example whose actual
final excess energy is bounded above and below by positive multiples of
`tau^(-2)` for all sufficiently large real `tau`. In fact the scaled energy
has explicit positive liminf and limsup. Thus the supplied uniform
`O(tau^(-2))` guarantee cannot generally be replaced by `o(tau^(-2))`, even
with a constant or little-o assertion tailored to each fixed member of this
class. This does not establish a lower bound for the specified infinite
chain, every allowed potential, or a changed switching protocol.

## 1. Actual protocol and exact finite Fock witness

Use the physical convention of the assigned notes:

\[
 H^{\rm ramp}(t)=H+(t/\tau)V,\quad 0\le t\le\tau,
 \qquad \psi_\tau'(s)=-i\tau(H+sV)\psi_\tau(s),\quad s=t/\tau.       \tag{S1}
\]

The initial state is the exact free vacuum, and the measured excess is
above the exact ground energy of `H+V`. No time renormalization, bounded
energy proxy, or replacement of that final Hamiltonian is used.

Fix any `0 < k <= K`. On `F_-(C^2)` let `a_1,a_2` be the usual CAR
annihilators, `Omega` the vacuum, and

\[
 n_j=a_j^*a_j,\qquad H=m(n_1+n_2),\qquad
 V=k(a_1^*a_2^*+a_2a_1).                                        \tag{S2}
\]

Take the ordered even basis `Omega, eta`, where `eta=a_1^*a_2^* Omega`.
The pair annihilator has the order `a_2 a_1`, so it sends `eta` to `Omega`
with positive sign. The potential vanishes on the two odd one-particle
basis vectors. It is selfadjoint and even, and

\[
 H\ge m(I-|\Omega\rangle\langle\Omega|),\quad \ker H=\mathbb C\Omega,
 \qquad \|V\|=k\le K<m/2.                                        \tag{S3}
\]

The full space has dimension four; the odd sector has free energy `m`.
The exact vacuum is even, and the actual evolution stays in the two-dimensional
even subspace. On that subspace and the odd subspace, respectively,

\[
 (H+sV)_{\rm even}=\begin{pmatrix}0&ks\\ks&2m\end{pmatrix},
 \qquad (H+sV)_{\rm odd}=mI.                                     \tag{S4}
\]

This is a fixed potential, independent of `tau`, not a duration-dependent
adversarial family. It is a local two-mode CAR polynomial (even quadratic);
no spatial identification with an ordinary-cell potential of the supplied
infinite chain is being asserted.

## 2. Instantaneous spectral data, signs and exact amplitudes

For `0 <= s <= 1`, define

\[
 E(s)=\sqrt{m^2+k^2s^2},\qquad
 \alpha(s)=\tfrac12\arctan(ks/m),\qquad
 f(s)=\alpha'(s)=\frac{km}{2E(s)^2}.                              \tag{S5}
\]

Real normalized eigenvectors in the ordered even basis are

\[
 g(s)=\binom{\cos\alpha(s)}{-\sin\alpha(s)},\qquad
 e(s)=\binom{\sin\alpha(s)}{\cos\alpha(s)},
 \qquad \lambda_g(s)=m-E(s),\quad\lambda_e(s)=m+E(s).              \tag{S6}
\]

Multiplication by (S4) verifies both signs. Their derivatives are
`g'=-f e` and `e'=f g`. The full-space ground is the simple line `g(s)`:
the two odd energies lie at `m`, and their distance from the ground is
`E(s) >= m`. The excited even energy is separated by

\[
 \Delta(s)=\lambda_e(s)-\lambda_g(s)=2E(s).                       \tag{S7}
\]

Thus all the abstract gap assumptions hold, even with a stronger gap than
required by `m-2K`. No odd state is populated in this example.

Write the actual solution, including its dynamical phases, as

\[
 \psi_\tau(s)=a(s)e^{-i\tau\int_0^s\lambda_g(u)du}g(s)
             +b(s)e^{-i\tau\int_0^s\lambda_e(u)du}e(s),
 \qquad a(0)=1,\quad b(0)=0.                                    \tag{S8}
\]

Let `Phi(s)=int_0^s Delta(u)du`. Substitution into (S1), with the derivatives
of the real eigenvectors, gives the exact equations

\[
 a'=-fb\,e^{-i\tau\Phi},\qquad b'=fa\,e^{i\tau\Phi},
 \qquad |a|^2+|b|^2=1.                                          \tag{S9}
\]

The coefficients depend on `tau`; the notation suppresses that argument.
The norm identity follows either from the unitary evolution or directly
by differentiating it in (S9). All functions here are smooth finite-dimensional
functions; every integration and derivative below is on the compact interval
`[0,1]`, with `Delta >= 2m`. There is no unbounded-domain step in this witness.

The actual excess at the final time is exactly

\[
 d_\tau=\langle\psi_\tau(1),
       (H+V-\lambda_g(1))\psi_\tau(1)\rangle
       =2E(1)|b(1)|^2.                                         \tag{S10}
\]

Cross terms vanish by the exact eigenbasis. This equality, not a norm
estimate paired with an unbounded operator, identifies the physical energy.

## 3. Uniform amplitude control before extracting endpoint terms

Put

\[
 F(s)=\frac{f(s)}{\Delta(s)}=\frac{km}{4E(s)^3},\qquad
 F_0=\frac{k}{4m^2},\quad F_1=\frac{km}{4(m^2+k^2)^{3/2}}.          \tag{S11}
\]

For `k > 0`, `F` is positive and decreasing, and `F_0 > F_1 > 0`.
Integrating `b'=fa exp(i tau Phi)` by parts, and using the equation for
`a'` without dropping its feedback, gives the exact identity

\[
 b(s)=\frac1{i\tau}\left[
 F(s)a(s)e^{i\tau\Phi(s)}-F_0
 -\int_0^s F'(u)a(u)e^{i\tau\Phi(u)}du
 +\int_0^s F(u)f(u)b(u)du\right].                               \tag{S12}
\]

The sign of the last term comes from the minus sign in `a'`.
Let `B=sup_[0,1] |b|` and

\[
 L=\int_0^1 f(s)ds=\alpha(1)\le\frac{k}{2m},\qquad
 J=\int_0^1 F(s)f(s)ds\le F_0L.                                \tag{S13}
\]

Using `|a| <= 1` and the monotonicity of `F`, the first three contributions
in the bracket in (S12) have total absolute bound

\[
 F(s)+F_0+\int_0^s|F'(u)|du=2F_0.
\]

Hence `B <= 2F_0/tau + JB/tau`. Set

\[
 \tau_0=\frac{k^2}{4m^3}\ge2J.
\]

For every `tau >= tau_0`, it follows that

\[
 B\le\frac{4F_0}{\tau},\qquad
 \sup_{0\le s\le1}|a(s)-1|\le LB\le\frac{4F_0L}{\tau}.            \tag{S14}
\]

The second bound integrates the exact `a'` equation. In particular the
phase correction hidden in `a(s)` is controlled; it is not silently set to
one over an interval whose physical length is `tau`.

## 4. Explicit second-order remainder in the amplitude

Define

\[
 G(s)=\frac{F'(s)}{\Delta(s)}
     =-\frac{3k^3ms}{8E(s)^6},\qquad
 G'(s)=-\frac{3k^3m(m^2-5k^2s^2)}{8E(s)^8}.                       \tag{S15}
\]

One further integration by parts yields, for all `s` in `[0,1]`,

\[
 \left|\int_0^sF'(u)a(u)e^{i\tau\Phi(u)}du\right|
 \le\frac1\tau\left[
 |G(s)|+|G(0)|+\int_0^s|G'(u)|du+\int_0^s|G(u)|f(u)du\right].     \tag{S16}
\]

This uses only `|a| <= 1` and `|a'|=f|b| <= f`. Thus it remains valid
independently of the sharper (S14). The necessary explicit bounds are

\[
 \begin{split}
 G(0)&=0,\qquad \|G\|_\infty\le\frac{3k^3}{8m^5},\\
 \int_0^1|G'|&\le\frac{3k^3}{8m^5}+\frac{5k^5}{8m^7},\\
 \int_0^1|G|f&\le\frac{3k^4}{16m^6}.
 \end{split}                                                    \tag{S17}
\]

For the middle bound, use `E >= m` and
`|m^2-5k^2s^2| <= m^2+5k^2s^2`, then integrate `s^2`. In particular no
incorrect claim that `G'` keeps one sign for all `k < m/2` is needed.

Subtract the proposed endpoint term from (S12). The remaining endpoint
has size at most `F_0 |a(s)-1|`; the last integral has size at most `JB`.
Equations (S13)-(S17) therefore give the fully explicit estimate

\[
 \boxed{\displaystyle
 b(s)=\frac{F(s)e^{i\tau\Phi(s)}-F_0}{i\tau}+r_\tau(s),\qquad
 \sup_s|r_\tau(s)|\le\frac{C}{\tau^2},\quad \tau\ge\tau_0,}
                                                                    \tag{S18}
\]

where the nonoptimal, finite constant is

\[
 C=\frac{k^3}{m^5}+\frac{3k^4}{16m^6}+\frac{5k^5}{8m^7}.           \tag{S19}
\]

Indeed, the two terms controlled by (S14) contribute at most
`8 F_0^2 L <= k^3/(4m^5)` to this constant; the two `G,G'` cubic terms
contribute `3k^3/(4m^5)`. The other two terms are as displayed in (S17).
This is an analytic remainder bound uniform on the whole slow interval,
not an asymptotic assertion inferred from sampled ramp durations.

## 5. Positive all-duration asymptotic lower bound and sharp order

Write `E_1=sqrt(m^2+k^2)`, `D=F_0-F_1 > 0`, `S=F_0+F_1`, and

\[
 \Phi_1=\Phi(1)=E_1+\frac{m^2}{k}\operatorname{arsinh}(k/m)>0.
\]

Equation (S18) and the exact energy formula (S10) give

\[
 \left|\tau^2d_\tau-
 2E_1\left(F_0^2+F_1^2-2F_0F_1\cos(\tau\Phi_1)\right)\right|
 \le2E_1\left(\frac{2SC}{\tau}+\frac{C^2}{\tau^2}\right).          \tag{S20}
\]

Thus interference has not been replaced by a phase average. In particular,

\[
 \begin{split}
 \liminf_{\tau\to\infty}\tau^2d_\tau&=2E_1(F_0-F_1)^2>0,\\
 \limsup_{\tau\to\infty}\tau^2d_\tau&=2E_1(F_0+F_1)^2.
 \end{split}                                                    \tag{S21}
\]

For equality in these liminf/limsup claims take, respectively,
`tau_n=2 pi n/Phi_1` and `tau'_n=(2n+1) pi/Phi_1`. They tend to infinity
and the error in (S20) tends to zero. The uniform bounds on the cosine
give the opposite inequalities. No convergence of the scaled energy itself
is claimed; its leading coefficient oscillates.

More explicitly, for

\[
 \tau\ge\tau_*:=\max\{\tau_0,2C/D\},
 \qquad
 \frac{E_1D^2}{2\tau^2}\le d_\tau
 \le\frac{2E_1(S+C/\tau)^2}{\tau^2}.                            \tag{S22}
\]

The lower bound follows from
`|F_1 exp(i tau Phi_1)-F_0| >= D` and `|tau r_tau(1)| <= C/tau`.
The endpoint magnitudes are strictly unequal, so no large-duration
interference can remove this lower bound. It holds for one fixed `H,V`,
not just a sequence of Hamiltonians chosen as a function of duration.

Taking `k=K` proves broad-class sharpness for every fixed allowed `m,K`
with `K>0`: a universal guarantee `d_tau=o(tau^(-2))`, or an upper bound
`C'(m,K) tau^(-p)` for any `p>2`, is false on this class. Even permitting
`C'` to depend on this particular `H,V` does not overcome (S22).
The supplied parent's `O(tau^(-2))` upper theorem is therefore optimal in
order under these abstract assumptions. Its explicit prefactor is not
shown optimal by this example.

The special class `K=0` has `V=0` and zero excess exactly. It is explicitly
excluded from the positive lower-bound statement and is not an exception
hidden in a division by `k`.

## 6. Infinite-mode extension and limits of the witness

The same obstruction can, if desired, be placed in an unbounded infinite-mode
Fock problem without changing any computation. Let the one-particle space be
`C^2 direct-sum ell^2`, with free one-particle energy `mI`, so the full
Hamiltonian is `mN`. It is unbounded, has a unique vacuum and gap `m`.
Let the even `V` in (S2) act on the first two modes and trivially on the
spectator factor. In the graded Fock tensor decomposition, its evenness makes
this precisely `V_pair tensor I`. Starting from the full vacuum, the spectator
vacuum remains fixed and the exact evolution factors through (S4). The vector
always has at most two particles, lies in the operator domain, and its actual
unbounded excess is exactly (S10). Thus unboundedness alone does not evade
the broad-class lower bound.

Neither realization is the supplied fixed dispersive infinite chain. The
extension uses isolated chosen modes and a flat free dispersion. It proves
no locality statement for ordinary physical-cell potentials of that chain,
and no matching `tau^(-2)` lower bound for its particular nonquadratic local
interactions. Establishing a chain-specific lower bound would require a
separate excitation/endpoint analysis in that model. Nothing here imports
such a premise or labels that narrower question closed.

Nor does sharpness of the class mean every allowed potential has this rate.
For the same finite Fock space, the nonzero even potential `V=k n_1` commutes
with `H`, annihilates `Omega`, and leaves `Omega` as the exact ground of
`H+sV`. Its actual excess is zero for every duration. This is an explicit
counterexample to a universal positive lower bound over all potentials.

## 7. A smoother protocol changes the endpoint problem

The linear ramp is part of the statement. The result does not exclude faster
preparation when that protocol is changed. Here is a direct check in the same
finite example, without importing a general higher-order adiabatic theorem.

Replace `s` in (S4) by a real `q(s)` in `C^3[0,1]`, with `q(0)=0`, `q(1)=1`.
Set `E=sqrt(m^2+k^2 q^2)`, `Delta=2E`,
`f=km q'/(2E^2)`, `F=f/Delta`, and `G=F'/Delta`.
The same amplitude equations and exact identity (S12) hold. Define finite
constants

\[
 \begin{split}
 B_0&=\sup_{0\le s\le1}
      \left(|F(s)|+|F(0)|+\int_0^s|F'(u)|du\right),\\
 L_q&=\int_0^1|f|,\qquad J_q=\int_0^1|Ff|,\\
 C_q&=2B_0(\|F\|_\infty L_q+J_q)
       +\|G\|_\infty+|G(0)|+\int_0^1|G'|+\int_0^1|Gf|.
 \end{split}                                                    \tag{S23}
\]

For `tau >= 2 J_q` and `tau>0`, the argument yielding (S14) now gives
`sup |b| <= 2B_0/tau` and `sup |a-1| <= 2B_0 L_q/tau`.
The second integration by parts is valid since `F` is `C^2` and `Delta>0`.
It proves

\[
 \left|b(1)-\frac{F(1)e^{i\tau\Phi(1)}-F(0)}{i\tau}\right|
       \le\frac{C_q}{\tau^2}.                                  \tag{S24}
\]

If `q'(0)=q'(1)=0`, both endpoint terms vanish, and therefore this same
finite example has `d_tau <= 2E_1 C_q^2/tau^4` for that changed protocol.
For instance `q(s)=3s^2-2s^3` has all the stated properties. The constants
in (S23) are explicit integrals of displayed smooth functions on a compact
interval; they are finite without any additional domain assumption here.

This finite-example statement demonstrates why the linear-ramp lower bound
cannot be transferred to smoother switching. It does not assert a uniform
`O(tau^(-4))` unbounded-energy theorem for every abstract `H,V` under a changed
protocol; that would require its own graph/domain analysis. No optimization
over preparation protocols has been proved.

## 8. Rejected shortcuts, preserved limits and provenance

The following potential shortcuts are not used:

- An `O(tau^(-1))` upper bound on leakage does not imply a lower bound or
  sharpness, and by itself does not identify actual energy. Equations
  (S18) and (S10) provide those missing pieces in this example.
- Expanding only to first order in the fixed coupling `k` at a fixed physical
  time would not control a time interval growing with `tau`. No small-`k*tau`
  expansion is used. The instantaneous eigenbasis is exact at every fixed
  allowed `k`, and the remainder is controlled as `tau` tends to infinity.
- Averaging the cosine in (S20) would discard possible endpoint interference.
  The strict inequality `F_0>F_1` is the reason the all-large-duration lower
  bound survives here. No dephasing or averaged-time premise is supplied.
- `G'` need not have a fixed sign throughout the allowed interval of `k/m`;
  (S17) uses an absolute bound and retains this possibility.
- The zero-excess commuting example and the smoother-profile improvement
  remain explicit. The witness is not promoted to a statement about every
  potential, all protocols, or a fixed infinite-chain interaction.

These are analytically excluded shortcuts, not claimed failed numerical
runs. No numerical or formal run was performed. The exact finite-dimensional
calculation is sufficient to test the stated broad-class guarantee; the
provided unbounded upper theorem supplies the complementary general order.
No new continuum, extensive-interaction, unique-state-selector, or physical
axiom conclusion follows.

## 9. Exact inputs and exposure/freeze record

The neutral plan was frozen at **2026-10-12T19:31:23.649705+00:00**, before
reading the two new inputs. Its SHA256 is
`6099b53dc0fed4a8d9457b7d48e14254c4fc56130bebcac36c46a69a74c0b96d`.
The only new scientific files read were:

| Input | SHA256 | Complete coverage |
| --- | --- | --- |
| `ADIABATIC_PREPARATION_INDEPENDENT.md` | `3ac5a798d0c48822eb2495deed89bfd4bcf5aef4ffa60019dded169aee230eec` | 492 lines, 23060 bytes |
| `ADIABATIC_ENERGY_RATE_INDEPENDENT.md` | `9f5339805d51c6a06f755c7cfcf39be21b39e30ae07c9cceb01d94652d164b20` | 369 lines, 15845 bytes |

Their first-read receipts are saved in the assigned evidence directory.
The batched return was truncated in the preparation note's final scope
section; lines 426–492 were then read separately without truncation, completing
that exposure. The energy-rate note was returned in full. The notes are used
for the exact protocol, hypotheses, target energy and existing upper bound;
no claim is made to have independently audited every earlier parent proof.

Previously known context includes the massive free Fock chain, ordinary even
cell perturbations, normality and bounded-interaction work, corrected-cell
comparisons, and completed Lean statement-scope reviews. Those shared premises
are disclosed, not represented as blind independence. Governing procedures
are reused from the unchanged instruction coverage already read in this
campaign; this task performed no new main-branch check.

No new root sharpness proof, root sharpness seal, checkpoint, new synthesis,
or other worker argument was read before this core was frozen. Independence
is limited to this separate same-model analytic reconstruction from the two
allowed notes and the disclosed prior context. It is not model-family
independence, formal proof, or audit independence.

The exact core copy, source-input manifest, and freeze time/hash are in
`adiabatic_energy_sharpness_independent/`. Only this note and that assigned
directory were written. No original note, repo source, Git state, publication
package, checkpoint, editable prompt, physical axiom or audit status changed.


### End unchanged separately frozen proof

The original preparation assembly's no-optimality statement remains its
historical scope. Only this explicitly later appendix supplies the broad-class
linear-ramp witness. The original, both publication citation replacements,
complete appended source and exact wrapper transformation reconstruct from the
content-deduplicated archive.

The [No-Go Discipline Gate](../.claude/science/physics-loops/toe-bounded-interactions-20261012/NO_GO_DISCIPLINE_CHECKLIST.md)
keeps N1/N5 pending. Explicit scoped counterexamples and this witness do not
complete an exhaustive no-go packet. Final wrapper/program acceptance and
root execution remain separate. There is no analytic Lean certificate,
retained-status claim, empirical prediction or autonomous state selector.
