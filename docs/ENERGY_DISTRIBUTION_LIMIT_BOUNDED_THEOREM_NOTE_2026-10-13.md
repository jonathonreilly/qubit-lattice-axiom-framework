---
claim_id: energy_distribution_limit_bounded_theorem_note_2026-10-13
claim_type: bounded_theorem
claim_scope: "Conditional one-time free-energy distribution bounds on the supplied actual Fock carriers, with separate moment, protocol, normalization and target-tail hypotheses for the stated endpoints."
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
artifact_role: theorem
assembly_status: accepted_source_with_reviewable_publication_wrapper
runner: scripts/energy_distribution_limit_identity_2026_10_13.py
scientific_execution: none_in_this_assembly
trace_class: upstream_support
reachability_to_target: supports
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
conditional_surface_status: supplied-model conditional arguments with explicit provisional dependencies
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: complete conditional proof body preserved with one accepted tail-hypothesis wording precision
audit_required_before_effective_retained: true
bare_retained_allowed: false
next_trace_action: root publication review and integration; current-main landing checks and independent retained audit remain separate
upstream_dependencies:
  - bv_graph_energy_protocol_bounded_theorem_note_2026-10-13
  - prepared_driven_state_bounded_theorem_note_2026-10-13
  - current_preserving_refinement_bounded_theorem_note_2026-10-12
  - local_even_continuum_bounded_theorem_note_2026-10-12
  - bounded_interaction_ground_bounded_theorem_note_2026-10-12
  - adiabatic_ground_preparation_bounded_theorem_note_2026-10-12
  - time_averaged_energy_transfer_bounded_theorem_note_2026-10-12
---

# Energy-distribution limits with explicit endpoint resources

**Type:** bounded_theorem

This publication candidate carries the root-accepted conditional source assembly.
Its mathematical body is
the complete 944-line independent derivation, originally frozen with SHA-256
`4ab02757ff0be403b15d41779a04ca596436bc62240dbc027c01ac6d0fb78abc`.
One accepted wording precision qualifies the moving-target tail hypothesis;
all formulas and equation labels are preserved. The wrapper adds chronology,
scope and source bindings, not a new theorem or another scientific check.

The body concerns one-time spectral laws of the actual nonnegative free
Hamiltonians. Its subquadratic transport estimates use the actual commuting
energy bridge, trace comparison and second-moment bounds. Its quadratic
transport endpoints use the additional moment or graph-vector, preparation,
bounded-work, commutator, probability and target-tail resources stated at
each application. A second-moment cap alone does not establish the endpoint.
The compact-BV protocol and gap assumptions belong to those applications;
they are not universal assumptions of every abstract density estimate.

The uniform or varying-target tail hypothesis is sufficient for the displayed
clipping argument, not necessary for every comparison of moving laws. An
arbitrary noncontractive insertion yields a nonnegative weight; a probability
interpretation requires the contraction or common fixed rescaling already
specified in the body. Positive normalization and its actual denominators
remain required. The all-hold, vanishing-budget target is the interacting
ground's free-energy law, which need not be a point mass at zero.

## Chronology and notation of the preserved body

The independent proof froze on 2026-10-13 at 00:05:53 UTC, before its new root
comparison. The complete 514-line source-exposed comparison froze at 00:21:23
UTC with SHA-256
`92a80fb57297812f544adef693caa19a8c28c3d6e008b7093af82526301cba86`.
Root's 00:28:59 acceptance record and the accepted postcomparison precision
record preserve conditional acceptance and distinguish the original proof's
endpoint results from the root's sharper first-transport/CDF constants.
Those sharper formulas are comparison evidence, not silently substituted
into this body. Root accepted the exact source assembly at 02:27:42 UTC,
reusing complete body coverage and reading the new wrappers and three wording
changes. The new publication wrappers remain subject to exact root review.

The original title, local notation, equation labels, source names, exposure
statements and then-outstanding review statements below are historical text.
They describe the original freeze, not the exposure or review status of this
later assembly. The exact original and comparison remain unchanged in the
content-addressed source archive. Same-family separate-context derivation
and later source exposure do not establish model diversity, formal analytic
verification, transitive audit or retained status. Current remains open_gate.

## Preserved distribution derivation

# Distributions of measured actual free energy

Status: independent conditional consequence from the exact allowed parents.
The new energy-distribution root and its seals remain unread before freeze.
This is a same-family derivation with shared sources, not a formal,
model-diverse or transitive audit. No scientific program is used.

There are two different levels of conclusion. Uniform second moments and a
full density comparison give quantitative Wasserstein convergence of every
order below two. The specified vacuum-ramp/BV-pulse protocol has additional
graph information: on controlled finite time windows it also gives convergence
of the second moment and Wasserstein distance of order two. Uniform moment
bounds alone do not provide that endpoint. Regular insertions preserve the
first conclusion at positive limiting outcome probability and uniform
regularity. An additional graph comparison, supplied by fixed BV averages
with the stated ordinary orbit comparisons, gives the endpoint. All
probabilities and extra premises are explicit.

## 1. Objects, exact parent inputs and metric

Let \(H_c\) be the actual nonnegative free Hamiltonian on the physical
in-band Fock space, \(\widehat\rho_c=\iota_c\rho_c\iota_c^*\) its density
placement on \(\mathcal F_L\otimes\mathcal F_H\), and
\(\widehat\rho_0=\rho_0\otimes|\Omega_H\rangle\langle\Omega_H|\).
The target free Hamiltonian is \(H_0=d\Gamma(E)\),
\(E(p)=\sqrt{m^2+v^2p^2}\), with \(m,v>0\) and refinement \(c>0\).
Bounded operator comparisons use unital
placements, distinct from these density placements. No outside-band zero
mode is assigned physical energy.

For a normal state the measured free-energy law is the probability measure
\[
 \mu_c(B)=\operatorname{Tr}\rho_c\mathbf1_B(H_c),\qquad
 \mu_0(B)=\operatorname{Tr}\rho_0\mathbf1_B(H_0),\quad B\subset[0,\infty).
                                                                    \tag{E1}
\]
This is a one-time spectral measurement distribution. It is not a work
distribution defined by two measurements, nor a distribution of the signed
bounded work operator. The given state and measurement prescription are
inputs, not a derived microscopic selection rule.

For probability measures with finite \(r\)-th moment, \(r\ge1\), define
\[
 W_r(\mu,\nu)=\inf_{\pi\in\operatorname{Cpl}(\mu,\nu)}
                  \left(\int|x-y|^r\,d\pi(x,y)\right)^{1/r}.         \tag{E2}
\]
The couplings below prove the bounds directly. Total variation means
\(\sup_B|\mu(B)-\nu(B)|\), one half of the signed-measure variation norm.

The graph parents prove for the actual branches, in their commuting free
occupation representation,
\[
 H_c\ge L:=H_0\otimes I_H,\quad H_c\ge\Lambda_cN_H,\quad
 \Lambda_c=\sqrt{m^2+2v^2/c^2},\quad
 0\le H_c-L\le k_cH_c^2,
 \qquad k_c=\frac{c}{2v}+\frac1{\Lambda_c}.                          \tag{E3}
\]
The last inequality is a joint spectral/form statement on the actual range.
For each low particle \(e_{c,L}-E\le cE^2/(2v)\); summing uses
\(\sum E_i^2\le(\sum E_i)^2\). The high part is bounded by
\(H_cQ_H\le H_c^2/\Lambda_c\). This proves E3 without squaring a
noncommuting interacting form inequality.

Write
\[
 S_c^2=\operatorname{Tr}\rho_cH_c^2,
 \qquad S_0^2=\operatorname{Tr}\rho_0H_0^2,
 \qquad \alpha_c=\|\widehat\rho_c-\widehat\rho_0\|_1.               \tag{E4}
\]
Second moments mean spectral moments:
\(S_c=\|H_c\rho_c^{1/2}\|_{\rm HS}\). Finite second moment puts every
positive-weight ensemble vector in \(D(H_c)\); it does not require
\(D(H_c^2)\), trace-class \(H_c^2\rho_c\), or unbounded cyclic trace
manipulations. Let \(\lambda_c=\operatorname{Tr}_H\widehat\rho_c\).
The parents give \(\operatorname{Tr}\lambda_cH_0^2\le S_c^2\) and
\(\|\lambda_c-\rho_0\|_1\le\alpha_c\). For a fixed target, a uniform
\(S_c\) and this trace limit also supply its finite second moment by bounded
spectral cutoffs and lower semicontinuity. For a varying target family its
moment bound is a separate stated resource.

Write \(G_c=H_c+V_c\) and \(G_0=H_0+V_0\), with bounded selfadjoint even
potentials as in the exact parents. Their actual simple ground
energies and projectors are \(E_{g,c},P_c\) and \(E_{g,0},P_0\), with
\(|E_{g,c}|,|E_{g,0}|\le K\). The automorphisms \(\alpha_t\) and
\(\beta_t\) are respectively free and interacting Heisenberg evolution,
\(\operatorname{Ad}(e^{itH})\) and \(\operatorname{Ad}(e^{itG})\).

The supplied linear ramp from the exact free vacuum, finite compact BV
pulse, and autonomous holds obey
\[
 S_c,S_0\le S:=2K+b,\qquad
 b=|\epsilon|a\operatorname{TV}(j),\quad
 \|V_c\|,\|V_0\|\le K<m/2.                                        \tag{E5}
\]
Here \(a\) bounds the selfadjoint even pulse observable, \(j\) is its real,
zero-extended whole-line BV profile supported in \([0,T]\), and endpoint
atoms count. The pulse Hamiltonian is \(G-\epsilon j(t)A\).
The bound is independent
of ramp speed and both holds. A finite list of BV controls replaces \(b\)
by the sum of their budgets. For general normal input of initial free
root-second-moment \(S_{\rm in}\), the corresponding bound is
\(S_{\rm in}+2K+b\), not the vacuum value E5.

The graph-only corrections are applied: the ground-preserving zero-absorption
control assumes an exact interacting initial ground; older amplitude and
graph/gap estimates are combined by taking their minimum, without a claimed
uniform ordering. A larger parity gap is used only on even-sector support,
not merely a parity-invariant density. The full gap \(g=m-2K\) is safe below.

Here are explicit choices for the parent error resources used below. Put
\(\nu_c^V=\|\widehat V_c-\widehat V_0\|\). For any fixed \(\mu>K\),
\[
 r_c^{\rm res}=\frac{\mu^2c/v+\nu_c^V}{(\mu-K)^2},\quad
 d_\mu=\frac{g}{(\mu+K)(\mu+m-K)},\quad
 b_c=\min(1,r_c^{\rm res}/d_\mu),\quad
 e_c^{\rm gs}=(\mu+K)^2r_c^{\rm res}.                              \tag{E5a}
\]
Thus \(\|\widehat P_c-\widehat P_0\|_1\le2b_c\) and
\(|E_{g,c}-E_{g,0}|\le e_c^{\rm gs}\). The ramp coefficient is
\(e_\tau=\min(1,C_{\rm ad}/\tau)\),
\(C_{\rm ad}=2K/g^2+31K^2/g^3\).
For ordinary bounded inputs the interacting orbit error satisfies
\[
 d_{A,c}(L):=\sup_{|s|\le L}
     \|\beta_{c,s}(\widehat A_c)-\widehat{\beta_{0,s}(A_0)}\|
 \le\min\{2a,\nu_{A,c}(L)+2La\nu_{V,c}(L)\},                     \tag{E5b}
\]
where \(\nu_{X,c}(L)\) is the corresponding free CAR orbit norm error.
These tend to zero for every fixed \(L\) for the supplied ordinary compact
real \(L^2\) inputs and finite even polynomials. There is no universal
rate in \(c\), or an implicit estimate on arbitrary growing windows.

## 2. Distribution comparison from second-moment bounds alone

Let \(\nu_c\) be the \(H_0\)-law of \(\lambda_c\). The strongly commuting
pair \((H_c,L)\) has a joint probability law in \(\rho_c\), whether or not
the state commutes with either operator. It couples \(\mu_c\) with \(\nu_c\).
Occupation-wise, put \(d=h-\ell\). Then \(0\le d\le h\) and
\(d\le k_ch^2\). For \(1\le r\le2\),
\[
 d^r=d^{2-r}d^{2r-2}\le(k_ch^2)^{2-r}h^{2r-2}
                       =k_c^{2-r}h^2,
 \qquad W_r(\mu_c,\nu_c)^r\le k_c^{2-r}S_c^2.                     \tag{E6}
\]

For any two nonnegative-energy laws \(\nu,\mu\), their common measure can
be coupled diagonally. The two residual measures have equal mass
\(t=\operatorname{TV}(\nu,\mu)\). Couple those arbitrarily; since
\(|x-y|^r\le x^r+y^r\) for \(x,y\ge0\), Hölder on each residual gives
\[
 W_r(\nu,\mu)^r
   \le(S_\nu^r+S_\mu^r)t^{1-r/2},\qquad1\le r<2.                   \tag{E7}
\]
Indeed \(\int x^r d\nu_{\rm res}\le
(\int x^2d\nu_{\rm res})^{r/2}t^{1-r/2}\le S_\nu^rt^{1-r/2}\).
For \(t=0\) the laws coincide. A spectral measurement contracts trace norm,
so \(\operatorname{TV}(\nu_c,\mu_0)\le\min(1,\alpha_c/2)\).
The triangle inequality now proves the explicit bound
\[
 \boxed{\ W_r(\mu_c,\mu_0)
 \le k_c^{(2-r)/r}S_c^{2/r}
 +(S_c^r+S_0^r)^{1/r}
           \min(1,\alpha_c/2)^{1/r-1/2},\qquad1\le r<2.\ }         \tag{E8}
\]
The second term may use the smaller low-partial-state trace error. In
particular
\[
 W_1(\mu_c,\mu_0)\le k_cS_c^2
                 +(S_c+S_0)\sqrt{\min(1,\alpha_c/2)}.              \tag{E9}
\]
Thus uniform second moments and the supplied full density limit imply laws
converge in every \(W_r\), \(1\le r<2\). This is stronger than convergence
of the first mean. For any Lipschitz readout \(f\), coupling gives the error
bound \(\operatorname{Lip}(f)W_1\). At a threshold \(x\), any coupling with
\(r\)-cost \(D^r\) gives, for \(s>0\),
\[
 F_0(x-s)-D^r/s^r\le F_c(x)\le F_0(x+s)+D^r/s^r.                  \tag{E10}
\]
Consequently threshold probabilities converge at continuity points of the
target distribution. No uniform claim about a discontinuity is hidden in
this statement.

For the checked finite-pulse family, insert its full-density bound into E8:
\(\alpha_c\le2e_\tau+2b_c+2|\epsilon|Jd_{A,c}(T+w)\), capped at two.
Here \(b_c\) is the parent's ground trace coefficient, distinct from the
control budget \(b\), and \(J(s)=\int_0^s|j(u)|du\), \(J=J(T)\).
Fixed final windows and any
pre-pulse waits therefore give these distribution limits as
\(c\to0,\tau(c)\to\infty\). Growing windows need their actual state/orbit
modulus. Uniform second moments do not remove that requirement.

## 3. A proved endpoint criterion for \(W_2\)

E8 does not itself tend to zero at \(r=2\). Here is a useful explicit
criterion that will be verified for the specified protocol. Suppose
\(d_1\) bounds \(W_1(\mu_c,\mu_0)\), and
\(\Delta_2\) bounds the difference of their second moments. Define the
target tail resource
\[
 A_0(R)=\int(x^2-R^2)_+\,d\mu_0(x),\qquad R>0.                     \tag{E11}
\]
Clipping energy at \(R\) costs in squared transport at most
\(\int(x^2-R^2)_+d\mu\), since \((x-R)_+^2\le(x^2-R^2)_+\).
The clipped laws lie in \([0,R]\), so their squared transport is at most
\(R\) times their first transport, at most \(Rd_1\). The function
\(\min(x^2,R^2)\) is \(2R\)-Lipschitz. Therefore the actual tail is bounded
by \(\Delta_2+2Rd_1+A_0(R)\), and the triangle inequality proves
\[
 \boxed{\ W_2(\mu_c,\mu_0)
 \le\sqrt{\Delta_2+2Rd_1+A_0(R)}
            +\sqrt{Rd_1}+\sqrt{A_0(R)}.\ }                         \tag{E12}
\]
For a fixed finite-second-moment target, \(A_0(R)\to0\). Taking first
\(c\to0\) at fixed \(R\), then \(R\to\infty\), proves \(W_2\to0\)
when \(d_1,\Delta_2\to0\). For varying targets the same proof requires
uniform integrability of their squared energy, explicitly
\(\sup A_0(R)\to0\) over the compared target family. A uniform numerical
second-moment cap alone is not that condition.

This criterion is proved here by couplings and truncation; no inference
from trace distance to an unbounded expectation is made. It also states
which target-tail information an effective \(W_2\) rate needs. Without a
higher moment or another tail estimate, no universal power rate for that
tail is supplied by the parents.

## 4. The supplied protocol has graph convergence on fixed windows

This uses information stronger than E4-E5. The graph parents prove, for the
pure ramp output after any pre-pulse hold,
\[
 \|F_c\psi_c\|\le t_\tau:=\min(2K,D_{\rm gr}/\tau),\quad
 D_{\rm gr}=2K/g+9K^2/g^2+9K^3/g^3,\quad F_c=G_c-E_{g,c}.            \tag{E13}
\]
They also prove the cyclic operator-domain identity
\(G_cU_c=U_c(G_c+\mathcal T_c)\),
\(\|\mathcal T_c\|\le b\), on \(D(G_c)=D(H_c)\). Holds commute with
\(G_c\). The pure preparation and pure target ground are important to the
following convenient vector formulation; section 6 states the more general
insertion requirements. Arbitrary normal inputs with only E4 are not given
E13 by this argument.

Choose ground phases so
\(\|\widehat\Omega_c-\widehat\Omega_0\|\le\sqrt2 b_c\). Choose the ramp
phase relative to its own ground so
\(\|\psi_c-\Omega_c\|\le\sqrt2 e_\tau\). These follow from the respective
rank-one trace bounds. At output remove the harmless ground phase over
\(L=T+w\). The driven-ground vector is \(B_c(w)\Omega_c\), with
\(B_c(w)=\beta_{c,-L}(S_c(T))\) and
\(S_c(t)=e^{itG_c}U_c(t)\). Let \(d_c=d_{A,c}(L)\), and put
\[
 u_c=\sqrt2e_\tau+\sqrt2b_c+|\epsilon|Jd_c,\qquad
 z_c=[|\epsilon|V_j+2\epsilon^2aB_j]d_c,
 \quad V_j=|Dj|(\mathbb R),\quad B_j=\int J(s)|Dj|(ds).             \tag{E14}
\]
The exact bounded work integrand is
\(\mathcal T_c=-\epsilon\int S_c(s)^*\beta_{c,s}(A_c)S_c(s)Dj(ds)\).
After shifting its entire integrand by \(-L\), define
\(Z_c(w)=\beta_{c,-L}(\mathcal T_c)\). Partial shifted cocycles differ
by at most \(|\epsilon|J(s)d_c\). Each shifted work integrand consequently
differs by at most \(d_c+2a|\epsilon|J(s)d_c\), giving
\[
 \|\widehat Z_c(w)-\widehat Z_0(w)\|\le z_c,
 \qquad \|Z_c(w)\|\le b.                                           \tag{E15}
\]
All are unital bounded CAR integral constructions with the correct actual
restrictions; none is a zero extension of a unitary. The BV derivative
atoms and singular part are included in E15.

The graph identity gives the following actual free-energy vector on the
driven ground:
\[
 H_c B_c(w)\Omega_c
       =[(E_{g,c}-V_c)B_c(w)+B_c(w)Z_c(w)]\Omega_c.                  \tag{E16}
\]
The bounded operator in brackets has norm at most \(2K+b\). Its actual and
target versions differ in norm by at most
\(e_c^{\rm gs}+\nu_c^V+(2K+b)|\epsilon|Jd_c+z_c\), where
\(\nu_c^V=\|\widehat V_c-\widehat V_0\|\) and
\(e_c^{\rm gs}\) bounds \(|E_{g,c}-E_{g,0}|\). For the preparation error,
the same graph identity and final subtraction of bounded \(V_c\) give
\[
 \|H_cU_{c,\rm total}(\psi_c-\Omega_c)\|
       \le t_\tau+(2K+b)\sqrt2e_\tau.                              \tag{E17}
\]
Combining E14-E17, the suitably phased actual output vector \(x_c\) and
the target driven-ground vector \(x_0\) obey on the common carrier
\[
 \|\widehat x_c-\widehat x_0\|\le u_c,\qquad
 \|\iota_cH_cx_c-(H_0x_0)\otimes\Omega_H\|
 \le v_c:=t_\tau+e_c^{\rm gs}+\nu_c^V+(2K+b)u_c+z_c.               \tag{E18}
\]
In particular their **actual second moments converge**, with the explicit
bound
\[
 \Delta_2\le(S_c+S_0)v_c\le2(2K+b)v_c.                            \tag{E19}
\]
This conclusion uses graph work, ground stationarity and the bounded work
operator comparison. It is not a consequence of uniform second moments or
trace convergence alone.

There is a useful normal-state extension with an explicit extra hypothesis.
Suppose the pre-pulse state has
\(t_c^2=\operatorname{Tr}\rho_cF_c^2\to0\), instead of assuming a pure
ramp output. With \(Y_c\) the pulse and final hold, the graph identity is
\(H_cY_c=Y_c(F_c+D_c)\), where
\(D_c=E_{g,c}+\mathcal T_c-Y_c^*V_cY_c\) is bounded by \(S=2K+b\).
The full gap gives excited probability at most \(\min(1,t_c^2/g^2)\).
For a spectral ensemble, the pure-state trace formula and Cauchy--Schwarz
bound the trace distance to a rank-one ground by twice the square root of
the ensemble excited probability. Thus
\(\|\rho_c-P_c\|_1\le2\min(1,t_c/g)\), without a diagonal-state
assumption. The final root second moment is at most \(t_c+S\).
Expanding Hilbert--Schmidt squared norms, not unbounded traces, bounds the difference
between the two final free second moments for inputs \(\rho_c\) and
\(P_c\) by
\[
 t_c^2+2S t_c+2S^2\min(1,t_c/g).                                  \tag{E19a}
\]
The density difference is unchanged by \(Y_c\). Combining E19a with the
driven-ground comparison E16 therefore proves the same fixed-window
\(W_2\) limit for coherent or mixed normal inputs with this vanishing
excitation second moment. Small first excess energy alone is weaker and
does not grant E19a with \(t_c\to0\).

On every bounded final-hold window, \(u_c,v_c\to0\) as
\(c\to0,\tau(c)\to\infty\), with arbitrary pre-pulse holds. There is no
relative preparation/spacing rate. E9 and E19 inserted in E12 prove
\(W_2(\mu_c,\mu_0)\to0\). The convergence is uniform on such windows:
\(w\mapsto H_0x_0(w)\) is Hilbert continuous, since
\(H_0=G_0-V_0\), the held vector lies in \(D(G_0)\), and \(V_0\) is
bounded. Its image over a compact window is compact. Bounded spectral tail
projections tend strongly to zero, hence uniformly on that compact image,
which supplies the uniform target tail in E11. The same argument permits
strengths in a fixed compact set using the norm-continuous bounded formulas
for \(B_0,Z_0\).

There is also a finite-protocol \(W_2\) limit without sending the ramp
time to infinity. In this paragraph the target is the continuum output
of the **same finite ramp**, rather than the driven exact ground. Write
\(t_p=\tau+w_{\rm pre}\),
\(L=\tau+w_{\rm pre}+T+w_{\rm post}\), and
\(g_\tau(s)=\min(s/\tau,1)\). The full bounded perturbation of the free
Hamiltonian is
\(B(s)=g_\tau(s)V-\epsilon j(s-t_p)A\).
The previously checked free-cocycle argument supplies
\[
 q_c^{\rm prot}=(L-\tau/2)\nu_{V,c}(L)
                    +|\epsilon|J\nu_{A,c}(L),\qquad
 \alpha_c\le\min(2,2q_c^{\rm prot}).                              \tag{E19b}
\]
Its graph version can be proved directly. Let
\(C_c=\alpha_{c,-L}(S_c^{\rm free}(L))\), where
\(S_c^{\rm free}(s)=e^{isH_c}U_{c,\rm full}(s)\), and shift the
noncyclic graph-work operator
\(W_c=\int U_{c,\rm full}(s)^*\,dB_c(s)\,U_{c,\rm full}(s)\)
by the same free automorphism to obtain \(Z_c^{\rm free}\).
The work measure has total norm variation at most \(K+b\). Since the
initial vacuum has zero free energy, the graph identity gives
\[
 x_c=C_c\Omega,\qquad
 \iota_cH_cx_c=
  [\widehat C_c\widehat Z_c^{\rm free}-\widehat V_c\widehat C_c]
       \Omega.                                                    \tag{E19c}
\]
For every partial cocycle shifted by \(-L\), the norm difference is at
most \(q_c^{\rm prot}\). Subtraction of the ramp and pulse work
integrands then bounds the two \(Z^{\rm free}\)'s by
\(\nu_{V,c}(L)+|\epsilon|V_j\nu_{A,c}(L)
       +2(K+b)q_c^{\rm prot}\).
Therefore the energy-vector difference in E19c is at most
\[
 v_c^{\rm prot}=(4K+3b)q_c^{\rm prot}
        +\nu_{V,c}(L)+\nu_c^V+|\epsilon|V_j\nu_{A,c}(L),
 \qquad \Delta_2\le2(2K+b)v_c^{\rm prot}.                         \tag{E19d}
\]
The measure \(dB\) includes the pulse endpoint atoms; its ramp piece is
\(V\,ds/\tau\). This explains every term in the displayed estimate.
For fixed positive \(\tau\) and fixed finite holds, E19b-E19d tend to
zero, and E9/E12 prove the claimed same-protocol \(W_2\) limit. Growing
total durations require these actual weighted moduli to vanish and the
target-tail condition of E12. The earlier stationary-ground route instead
allows arbitrary pre-holds without comparing an orbit over that duration.

For growing final holds E18 remains explicit with its growing orbit window.
Its errors must vanish; using E12 uniformly also requires the displayed
target squared-energy tail control. Neither condition is silently furnished
by a uniform graph bound. The previously frozen actual \(t/c^2\) density
counterexample does not disprove energy-law convergence: its \(V=0\) free
energy law is invariant under either hold.

## 5. Vanishing pulse budget gives an all-hold endpoint limit

There is a stronger conclusion in the absolute weak-source limit. It uses
the ramp's excitation graph estimate, not just a small first excess energy.
For any finite pulse sequence with total graph-work budget \(b_c\!{}^{\rm p}\),
set \(r_c=t_{\tau(c)}+b_c\!{}^{\rm p}\). The graph identity gives
\(\|F_c x_c\|\le r_c\), independently of all autonomous holds and their
lengths. The full gap gives excited probability at most
\(\min(1,r_c^2/g^2)\). Choosing a phase relative to the actual ground,
\[
 \|x_c-\Omega_c\|\le\sqrt2\min(1,r_c/g).
\]
Since \(H_c=F_c+E_{g,c}-V_c\), define
\[
 U_c=\sqrt2\min(1,r_c/g)+\sqrt2 b_c,\qquad
 V_c^{\rm err}=r_c+e_c^{\rm gs}+\nu_c^V+2K U_c .                  \tag{E20}
\]
Here the unadorned \(b_c\) again means the static ground coefficient.
Direct subtraction of the two ground energy vectors proves
\[
 \|\widehat x_c-\widehat\Omega_0\|\le U_c,\qquad
 \|\iota_cH_cx_c-(H_0\Omega_0)\otimes\Omega_H\|
       \le V_c^{\rm err}.                                         \tag{E21}
\]
For example, the actual within-model difference is bounded by
\(r_c+2K\sqrt2\min(1,r_c/g)\); the two ground energy vectors differ by
at most \(e_c^{\rm gs}+\nu_c^V+2K\sqrt2 b_c\). This proves E21 without
any orbit estimate over a growing time window.

Consequently \(c\to0\), \(\tau(c)\to\infty\), and
\(b_c\!{}^{\rm p}\to0\) imply convergence in \(W_2\) to the target
interacting ground's **free-energy measurement law**, uniformly over all
pre-holds and post-holds. Its law need not be a point mass at zero: the
interacting ground need not be a free-energy eigenvector. Use E9 with
\(\alpha_c\le2U_c\), second-moment error at most
\((S_c+\|H_0\Omega_0\|)V_c^{\rm err}\), and the fixed target tail in
E12. These are uniform resources because the target is now fixed.

For a fixed BV profile, \(\epsilon(c)\to0\) suffices for the budget
condition. No relative \(\tau\epsilon\) rate is needed for this absolute
distribution limit. It is not a statement about a distribution rescaled by
\(\epsilon^2\), nor does it replace the separate preparation conditions
for a quadratic work coefficient. A merely small mean excess energy and a
bounded second moment do not imply E20: section 8 gives an actual control.

The all-hold conclusion also extends to normal states whose pre-pulse
excitation root-second-moment tends to zero. After the pulse it is at most
that root moment plus the budget, by the graph identity and the
Hilbert--Schmidt triangle inequality. Call the resulting bound \(r_c\).
With \(C_c=E_{g,c}-V_c\), expansion of
\(\|(F_c+C_c)\rho_c^{1/2}\|_{\rm HS}^2\) bounds its difference from
the actual ground free second moment by
\(r_c^2+4Kr_c+8K^2\min(1,r_c/g)\).
The trace distance is at most \(2\min(1,r_c/g)\). Together with the
static ground comparison, these give E12 uniformly in all holds. There is
no assumption of a diagonal state or an energy eigenvector ensemble.

## 6. Normal inputs and regular outcome insertions

First consider one specified outcome represented by a bounded contraction
\(M_c\), with target \(M_0\), on the respective actual carriers. A finite
word \(M_c=A_{n,c}\cdots A_{1,c}\) of outcome contractions is included.
Its probability is the joint probability of that outcome string. Known
autonomous dynamics between insertions may be moved into the insertions by
Heisenberg conjugation, provided their shifted orbit and graph comparisons
are checked over the resulting time window. This statement is not a norm
comparison of the unbounded Hamiltonians' full unitary groups.

Assume the following explicit bounds, with corresponding unital placements
when a common-carrier norm is used:
\[
 \|M_c\|,\|M_0\|\le a\le1,\quad
 \|\widehat M_c-\widehat M_0\|\le\beta_c,\quad
 M_cD(H_c)\subset D(H_c),\quad
 \|[H_c,M_c]\|\le d_c^{\rm M},                                    \tag{E22}
\]
and the same domain assertion for the target with commutator bound
\(d_0^{\rm M}\). The commutators are bounded extensions of their
operator-domain values. The graph parents supply these hypotheses for
their regular insertion class. If a bounded observable is not a
contraction, it can be divided by a known common norm bound to specify a
physical outcome operator. The normalized output is unchanged, but the
probability must include that division; \(\operatorname{Tr}M\rho M^*\)
greater than one is not called a probability.

Let
\[
 \sigma_c=M_c\rho_cM_c^*,\quad p_c=\operatorname{Tr}\sigma_c,\qquad
 \sigma_0=M_0\rho_0M_0^*,\quad p_0=\operatorname{Tr}\sigma_0 .       \tag{E23}
\]
Adding and subtracting \(\widehat M_c\widehat\rho_0\widehat M_c^*\)
gives, without unbounded operators,
\[
 \|\widehat\sigma_c-\widehat\sigma_0\|_1\le
       \delta_c:=a^2\alpha_c+2a\beta_c,
 \qquad |p_c-p_0|\le\delta_c.                                     \tag{E24}
\]
Thus positive fixed target probability also guarantees positive actual
probability for sufficiently small errors. When both are positive, the
normalized output states \(\rho_c^{\rm M}=\sigma_c/p_c\) obey
\[
 \|\widehat\rho_c^{\rm M}-\widehat\rho_0^{\rm M}\|_1
 \le\min\left(2,\frac{2\delta_c}{\max(p_c,p_0)}\right).            \tag{E25}
\]
To check the sometimes useful maximum denominator, expansion with the
first normalization gives \((\delta_c+|p_c-p_0|)/p_c\); expansion with
the second gives the same numerator divided by \(p_0\). Both hold, so
their minimum is legitimate.

There is also a domain-valid moment bound. For a spectral ensemble of a
normal input with finite second moment, E22 holds on each positive-weight
vector. Summing the squared norms is equivalently the Hilbert--Schmidt
identity
\[
 H_cM_c\rho_c^{1/2}
    =M_cH_c\rho_c^{1/2}+[H_c,M_c]\rho_c^{1/2},\qquad
 \|H_cM_c\rho_c^{1/2}\|_{\rm HS}
       \le Q_c:=aS_c+d_c^{\rm M}.                                \tag{E26}
\]
Finite-rank spectral sums converge in both Hilbert--Schmidt norms, which
justifies this identity without any trace cycling. The conditional root
second moment is at most \(Q_c/\sqrt{p_c}\). Define
\(Q_0=aS_0+d_0^{\rm M}\). Applying E8 to the conditional states proves
\[
\begin{split}
 W_r(\mu_c^{\rm M},\mu_0^{\rm M})
 &\le k_c^{(2-r)/r}\left(\frac{Q_c^2}{p_c}\right)^{1/r}\\
 &\quad+\left(\frac{Q_c^r}{p_c^{r/2}}
                   +\frac{Q_0^r}{p_0^{r/2}}\right)^{1/r}
 \min\left(1,\frac{\delta_c}{\max(p_c,p_0)}\right)^{1/r-1/2},
 \qquad1\le r<2 .
\end{split}                                                       \tag{E27}
\]
This is a statement about the actual free Hamiltonian after the outcome,
not only the compressed low energy. With probabilities bounded below,
uniform \(Q_c,Q_0\), and \(\delta_c\to0\), every such \(W_r\) tends
to zero.

For rare but nonzero outcomes set \(p_* =\min(p_c,p_0)\). If the two
\(Q\)'s are bounded by \(Q\), sufficient explicit conditions are
\[
 \frac{k_c^{2-r}Q^2}{p_*}\longrightarrow0,
 \qquad\frac{Q^r\delta_c^{1-r/2}}{p_*}\longrightarrow0 .           \tag{E28}
\]
For example E27 gives
\(W_1\le k_cQ^2/p_*+2Q\sqrt{\delta_c}/p_*\).
These are sufficient resource conditions, not necessary rates. If
\(p_0=0\), there is no target conditional state to compare. Convergence of
unnormalized outcomes and their probabilities still makes sense; dividing
by the vanishing probability has no automatic distribution limit.

For a word with \(\|A_i\|\le a_i\), individual domain invariance and
bounded commutators \(d_i\), the Leibniz rule on \(D(H)\) gives
\[
 a=\prod_i a_i,\qquad
 d^{\rm M}\le\sum_i d_i\prod_{j\ne i}a_j.                         \tag{E29}
\]
Every term is bounded and every intermediate vector stays in \(D(H)\).
The finite word therefore satisfies E26. A common uniform bound can be
used if some individual factors have different actual and target norms.

## 7. The insertion endpoint: an extra graph comparison and its source

Uniform bounded commutators alone do not upgrade E27 to \(W_2\). For the
pure protocol vectors in E18, a sufficient additional premise is a norm
comparison of the bounded commutators themselves. Write
\[
 C_c=[H_c,M_c],\quad C_0=[H_0,M_0],\qquad
 \|\widehat C_c-\widehat C_0\|\le\zeta_c,\quad
 \|C_c\|,\|C_0\|\le d.                                           \tag{E30}
\]
Their unital bounded placements must restrict to the actual commutators.
This premise is not inferred from E22 or from trace convergence.
The same argument applies to the finite-protocol vectors E19b-E19d with
\(u_c=q_c^{\rm prot}\) and \(v_c=v_c^{\rm prot}\).
For the unnormalized vectors \(y_c=M_cx_c\), \(y_0=M_0x_0\), E18 and
the domain identity prove
\[
 \|\widehat y_c-\widehat y_0\|\le u_c^{\rm M}:=a u_c+\beta_c,
 \quad
 \|\iota_cH_cy_c-(H_0y_0)\otimes\Omega_H\|
 \le v_c^{\rm M}:=a v_c+\beta_c S_0+d u_c+\zeta_c .                \tag{E31}
\]
Indeed subtract \(M_cH_cx_c+C_cx_c\) and
\(M_0H_0x_0+C_0x_0\); all four error terms in E31 follow by a bounded
operator norm. Also \(|p_c-p_0|\le2a u_c^{\rm M}\), or the smaller
available E24 probability bound may be used. Actual conditional second
moments have difference at most
\[
 \Delta_2^{\rm M}
 \le\frac{(Q_c+Q_0)v_c^{\rm M}}{p_c}
       +\frac{Q_0^2|p_c-p_0|}{p_cp_0}.                            \tag{E32}
\]
The first term compares the unnormalized squared energy norms; the second
compares their normalizations. This asymmetric form is valid, and its
version with indices interchanged can also be used.

For a fixed target outcome with \(p_0>0\), \(u_c,v_c,\beta_c,\zeta_c\to0\)
and uniformly bounded resources imply \(\Delta_2^{\rm M}\to0\).
Use E27 at \(r=1\) and E12 with the conditional target law to conclude
\(W_2(\mu_c^{\rm M},\mu_0^{\rm M})\to0\). The uniform or varying-target endpoint
statements proved here assume uniform integrability of the conditional
target's squared energy. On fixed compact time windows a continuous family
of target graph vectors and a probability lower bound supply this. Rare
outcomes require the actual denominators in E27 and E32 to be controlled.
For arbitrary mixed inputs one could instead assume convergence of a
common purification and its energy columns in Hilbert--Schmidt norm;
neither that assumption nor E31 is supplied by trace convergence alone.

The normal near-ground extension after E19 has a more concrete endpoint
version. For \(t_c^2=\operatorname{Tr}\rho_cF_c^2\to0\), the same
operator-domain identities give
\(H_cM_cY_c=M_cY_cF_c+R_c\), with \(\|R_c\|\le Q=aS+d\).
The actual unnormalized energy norm is at most \(a t_c+Q\).
Thus the unnormalized free second-moment difference between this outcome
from \(\rho_c\) and from its actual ground input is bounded by
\[
 a^2t_c^2+2aQt_c+2Q^2\min(1,t_c/g).                               \tag{E32a}
\]
This follows by the same Hilbert--Schmidt expansion as E19a. Their outcome
probabilities differ by at most \(2a^2\min(1,t_c/g)\). Combine these
bounds with the pure driven-ground comparison E31, then normalize as in
E32. At a positive target outcome probability this proves the conditional
\(W_2\) limit for these normal inputs as well. It does not extend that
endpoint to arbitrary normal inputs with only uniform second moments.

There is a concrete regular class for which E30 follows from the existing
ordinary bounded-orbit comparison. Let
\[
 M_c=\int k(s)\,\beta_{c,t+s}(B_c)\,ds,\qquad
 \alpha_k=\|k\|_1,\quad q_k=|Dk|(\mathbb R),\quad \|B_c\|\le a_B,
                                                                    \tag{E33}
\]
where \(k\) is a fixed compact BV kernel, possibly complex, and both
endpoints and all singular derivative pieces count. Use a fixed common
rescaling if \(a_B\alpha_k>1\). The graph parents prove the actual
domain invariance and
\[
 [H_c,M_c]
   =i\int\beta_{c,t+s}(B_c)Dk(ds)-[V_c,M_c],\qquad
 \|[H_c,M_c]\|\le a_B(q_k+2K\alpha_k).                             \tag{E34}
\]
The sign follows from
\(\partial_s\beta_s(B)=i[G,\beta_s(B)]\) and BV integration by parts.
Only the resulting bounded commutator is used on the operator domain;
no unsmeared \([H_c,B_c]\) is presumed.

If \(d_{B,c}(L)\) bounds the ordinary orbit difference on a window
containing \(t+\operatorname{supp} k\), norm integration gives
\[
 \beta_c\le\alpha_k d_{B,c}(L),\qquad
 \zeta_c\le(q_k+2K\alpha_k)d_{B,c}(L)
                     +2a_B\alpha_k\nu_c^V .                      \tag{E35}
\]
The last term comes from subtracting the two bounded \([V,M]\)'s;
thus E35 does not commute an unbounded free Hamiltonian through a norm
limit. Fixed kernels and bounded centers have \(\beta_c,\zeta_c\to0\)
and uniform E34 bounds. This supplies the claimed conditional \(W_2\)
limit for fixed finite words of these insertions at positive target
probability, following the supplied protocol on fixed windows.

For completeness, with individual norm errors \(\beta_i\), commutator
errors \(\zeta_i\), and common bounds \(a_i,d_i\), telescoping E29 gives
a word commutator error bounded by
\[
 \sum_i\zeta_i\prod_{j\ne i}a_j
  +\sum_i d_i\sum_{j\ne i}\beta_j\prod_{\ell\ne i,j}a_\ell,        \tag{E36}
\]
with empty products equal to one. Thus no zero norm factor is divided
out. Norm errors telescope in the usual sum
\(\sum_i\beta_i\prod_{j\ne i}a_j\).

Shrinking averaging width is a separate joint limit. For
\(k_\sigma(s)=\sigma^{-1}k(s/\sigma)\), replace \(q_k\) by
\(q_k/\sigma\) in E34-E35. One must check those weighted errors, the
\(d u_c\) term of E31, probabilities, and target tail resources. The
parents' sufficient sector-word condition \(c/\sigma\to0\), by itself,
does not check any of these distribution requirements. Their rough-field
control can even have a point-window limit outside the free form domain.
No universal shrinking-window energy-distribution rate is established.

## 8. Controls and the exact limits they establish

### 8.1 An actual near-ground family defeats the moment-only endpoint

Set \(V=0\). Choose two orthonormal actual high-band one-particle modes
and let \(\chi_c\) be their normalized two-particle wedge. The parent
branch bounds give, on its spectral support,
\[
 2\Lambda_c\le H_c\le2\sqrt2\Lambda_c,
 \qquad L_c:=\|H_c\chi_c\|\in[2\Lambda_c,2\sqrt2\Lambda_c].
\]
Fix \(s>0\) and, for small \(c\), put
\[
 p_c=s^2/L_c^2,\qquad
 \rho_c=(1-p_c)|\Omega\rangle\langle\Omega|
                     +p_c|\chi_c\rangle\langle\chi_c|.             \tag{E37}
\]
These are actual even normal states. Their second free moment is exactly
\(s^2\), their full trace distance to the common vacuum is \(2p_c\to0\),
and their low partial state is exactly the vacuum. Their first excess
energy tends to zero because
\(p_c\langle\chi_c,H_c\chi_c\rangle=O(\Lambda_c^{-1})\).
Nevertheless
\[
 W_2(\mu_c,\delta_0)^2=s^2,\qquad
 W_r(\mu_c,\delta_0)^r
     =p_c\langle\chi_c,H_c^r\chi_c\rangle
     \asymp s^2\Lambda_c^{r-2},\quad1\le r<2.                     \tag{E38}
\]
The constants in the last comparison depend only on \(r\), by the stated
spectral interval. Thus the power of the branch term in E8 has the correct
order on the actual carrier, even with zero low-partial-state error.
This is an allowed near-ground state family, not the output of the
specified \(V=0\) vacuum ramp, which stays exactly vacuum. Its initial
excitation second moment is \(s^2\), so it does not satisfy the extra
vanishing graph hypothesis in E19a or E20. No contradiction with the
protocol endpoint is present.

The trace-error exponent is also the natural uniform exponent with only
a second-moment cap. For a common nonnegative Hamiltonian, a probability
\(p=s^2/E^2\) near energy \(E\) against vacuum has
\(W_r^r\) of order \(s^r p^{1-r/2}\). This is realizable at a fixed
actual \(c\) by even finite-particle wedges of increasing particle number
in a fixed nonempty momentum interval: their total energies lie between
two fixed positive multiples of that particle number. This auxiliary
state-class control is not a claim about a fixed finite preparation.

### 8.2 Actual regular CAR insertions need not preserve the endpoint

The extra commutator comparison E30 cannot be dropped even for an outcome
whose probability tends to one. The following example is on the actual
CAR carrier, with exact vacuum input, \(V=0\), and no pulse. Choose the
two orthonormal high modes \(u_c,z_c\) from 8.1, and let
\[
 \gamma(u)=a^*(u)+a(u),\qquad
 B_c=i\gamma(u_c)\gamma(z_c),\qquad \chi_c=B_c\Omega .              \tag{E39}
\]
The CAR imply that \(B_c\) is even, selfadjoint and unitary, with
\(\langle\Omega,B_c\Omega\rangle=0\). Its vacuum image is the
normalized two-high wedge up to a phase. These modes lie in the actual
one-particle energy domain. On the finite-particle core,
\([H_c,\gamma(u)]=a^*(e_cu)-a(e_cu)\), whose norm is \(\|e_cu\|\).
The product rule therefore gives
\[
 \|[H_c,B_c]\|\le\|e_{c,H}u_c\|+\|e_{c,H}z_c\|
                         \le2\sqrt2\Lambda_c.                    \tag{E40}
\]
To verify domain invariance, approximate any \(D(H_c)\) vector by this
core in graph norm. The identity
\(H_cB_c\phi_n=B_cH_c\phi_n+[H_c,B_c]\phi_n\) has convergent right
side. Closedness of \(H_c\) proves \(B_c\phi\in D(H_c)\) and the
same identity on that domain. This supplies all the regularity used here.

Fix an energy scale \(d_*>0\), take \(t_c=d_*/L_c\), and define
\[
 M_c=\frac{I+t_cB_c}{1+t_c},\qquad M_0=I.                          \tag{E41}
\]
For small \(c\), these are contractions, and
\(\|\widehat M_c-I\|\le2t_c\to0\). Their actual commutator norms
are uniformly bounded by \(\sqrt2 d_*\), using E40 and
\(L_c\ge2\Lambda_c\). The norm difference from the identity is also
small at every autonomous time. Yet their outcome probability and
normalized post-outcome vector on vacuum are exactly
\[
 p_c=\frac{1+t_c^2}{(1+t_c)^2}\longrightarrow1,\qquad
 y_c^{\rm norm}=\frac{\Omega+t_c\chi_c}{\sqrt{1+t_c^2}},
 \qquad
 W_2(\mu_c^{\rm M},\delta_0)
       =\frac{d_*}{\sqrt{1+t_c^2}}\longrightarrow d_* .            \tag{E42}
\]
The last equality is the actual root-second-moment identity for transport
to a point mass. All \(W_r\), \(r<2\), do converge to zero. E30 fails:
\(\|[H_c,M_c]\Omega\|=d_* /(1+t_c)\) stays nonzero, whereas the target
commutator is zero. This isolates the missing graph comparison, despite
norm-convergent insertions, uniform regularity, a perfect initial state,
and nonvanishing outcome probability.

This family depends on high-band modes as \(c\) varies. It is an actual
bounded even CAR construction, but it is not asserted to be a fixed
ordinary compact-smearing prescription or a fixed local finite-hull
insertion. The fixed BV-average theorem in section 7 has those stronger
comparison resources and is unaffected.

### 8.3 A vanishing outcome can select the high-energy component

On the same input take instead \(K_c=t_cB_c\), with target \(K_0=0\).
The operator norm tends to zero and its commutator norm stays uniformly
bounded. The actual outcome probability is \(t_c^2\to0\), but its
conditional state is exactly \(\chi_c\), with energies at least
\(2\Lambda_c\to\infty\). The unnormalized outcome tends to zero in
trace norm. There is no target conditional state because \(p_0=0\).
Thus E24 remains correct while unconditional division by a vanishing
probability would be false. The probability costs in E27-E32 cannot be
discarded as bookkeeping.

### 8.4 A higher transport order needs a higher moment premise

The authorized graph independent parent, section 8.2, gives a fully
bounded-control abstract example that is useful here. On
\(\mathbb C\Omega\oplus\ell^2(\{2,3,\ldots\})\), let
\(H\Omega=0\), \(He_n=mn e_n\),
\(f_n=C/(\sqrt n\log n)\) normalized in \(\ell^2\), and
\(A=|f\rangle\langle\Omega|+|\Omega\rangle\langle f|\).
Then \(\|A\|=1\), \(V=0\), and the ramp is exactly vacuum. For a
nonzero rectangular pulse, \(\psi(T)=e^{-iT(H-\epsilon A)}\Omega\)
has finite second energy moment by graph work. Writing its vacuum
component as \(u_0\), scalar integration by parts gives
\[
 u_n(T)=\frac{\epsilon f_n}{mn}
 \left[u_0(T)-e^{-imnT}
       -\int_0^T e^{-imn(T-s)}u_0'(s)\,ds\right].                 \tag{E43}
\]
The vacuum lies in \(D(H-\epsilon A)\), so \(u_0'\) is continuous.
For sufficiently small positive \(T\), the nonzero initial excited
derivative \(i\epsilon f\) ensures \(|u_0(T)|<1\). Approximation of
\(u_0'\) in \(L^1\) by step functions proves that the integral in E43
tends to zero as \(n\to\infty\). The bracket is then bounded below in
modulus by \((1-|u_0(T)|)/2\) for every sufficiently large \(n\).
Consequently every \(2+\eta\) moment diverges, since
\(\sum n^\eta|f_n|^2=\infty\) for all \(\eta>0\).

Thus the abstract bounded BV hypotheses do not even ensure finiteness of
\(W_{2+\eta}(\mu,\delta_0)\). This is an abstract spectral model, not
an asserted realization by the supplied ordinary continuum CAR source.
Higher regularity of that narrower source class remains a possible extra
route, and is not excluded by this control. The proved endpoint \(W_2\)
does not carry an unproved higher-order extension.

### 8.5 Transport convergence does not assert total variation convergence

Even a fixed finite-dimensional diagnostic separates the metrics: a common
excited state for Hamiltonians with respective energies \(\omega+\delta_c\)
and \(\omega\), \(\delta_c\to0\), gives point masses at different
locations. All transport distances tend to zero while total variation is
one. This example is abstract, not a model-specific fixed-protocol claim.

There is also an actual-carrier control on uniform statements over moving
target states. Fix distinct positive momenta \(p_1,p_2\). Choose two
normalized low wave packets supported in intervals of width \(c^4\)
about them and let both compared densities be their common two-particle
wedge on the embedded low carrier. Thus the full density error is zero
and the second moments are uniformly bounded. The target total energy is
supported in an interval of width \(O(c^4)\) about
\(E(p_1)+E(p_2)\). The actual total energy interval has width
\(O(c^4)\) about \(e_{c,L}(p_1)+e_{c,L}(p_2)\). The checked dispersion
expansion is
\[
 e_{c,L}(p)-E(p)=c^2\frac{v^2p^4}{8E(p)}+O(c^4)
\]
uniformly near these fixed momenta. The two intervals are disjoint for
small \(c\); their laws have total variation one, while \(W_2=O(c^2)\).
This is a varying target state family, not the fixed ramp/pulse family.
It excludes a uniform total variation conclusion based only on the
displayed trace and moment resources. It does not disprove possible total
variation convergence for the fixed actual protocol under additional
spectral analysis. No such stronger metric is established here.

### 8.6 What the time controls do and do not say

For finite nonzero strength the proof gives fixed-window limits and the
explicit sufficient growing-window conditions in sections 2-4 and 7. It
does not supply a universal growing-time rate for ordinary \(L^2\) inputs.
For the exact preparation and a vanishing control budget, section 5 gives
an absolute all-hold \(W_2\) ground-law limit. The earlier actual
\(t/c^2\) example separates full densities at nonzero strength while
preserving the free-energy distribution when \(V=0\). It must not be
relabelled as a counterexample to the energy-law limit. This note does not
construct a fixed ordinary interacting protocol whose energy distributions
fail at growing hold times; that separate question remains open here.

## 9. Claim scope, dependencies and remaining work

The new conclusions are conditional mathematical consequences of the exact
allowed carrier, gap, preparation, graph-work and orbit premises. The
following distinctions are essential to their scope.

| Inputs actually used | Conclusion established here |
| --- | --- |
| Normal states, actual second-moment caps, common-carrier trace limit | E8: all \(W_r\), \(1\le r<2\), with explicit constants |
| Exact vacuum followed by the same fixed finite ramp, pulse and holds in both models | E19b-E19d and E12: same-protocol second-moment and \(W_2\) convergence |
| Supplied exact vacuum ramp and fixed finite BV pulse, controlled finite final window | E18-E19 and E12: second-moment and \(W_2\) convergence, arbitrary pre-holds |
| Normal input with excitation second moment tending to zero | E19a supplies the same endpoint on fixed windows |
| Vanishing excitation graph bound and vanishing total pulse budget | E20-E21 and section 5: absolute \(W_2\) ground-law convergence for all holds |
| Bounded regular outcome word, norm comparison, positive limiting probabilities | E27: conditional \(W_r\), \(r<2\); E28 gives sufficient rare-outcome scaling |
| In addition, commutator comparison and protocol graph comparison | E31-E32: conditional \(W_2\), with target-tail and probability requirements |
| Fixed BV averages of inputs with the supplied ordinary orbit comparison | E34-E36 verify the extra insertion graph comparison on fixed windows |

The actual controls 8.1-8.3 preserve positivity, normalization, parity,
actual in-band support and all stated graph domains. They concern the
larger classes explicitly indicated, not a necessity theorem for a
specific ramp or fixed local prescription. The higher-moment example is
abstract. The total variation controls distinguish an abstract fixed state
from an actual moving-state family. None is an unqualified no-go for the
physical continuum model.

A scoped negative-claim stress check has been applied. Alternative routes
include excitation graph convergence, fixed BV insertion regularization,
higher moments, better growing-time orbit control and target tail control;
the first two are used positively here. The controls test different
missing premises rather than repeat the same state-selection failure.
Their residual effects are quantified in E38, E42 and the outcome
probabilities. Extra locality or spectral assumptions remain live routes.
No actual fixed-protocol obstruction is inferred from an abstract or
moving-input example. Prior graph and driven-state results are dependencies,
not independent corroborations of this new consequence.

Open obligations are a source-exposed check of this complete new argument,
any desired explicit fixed-target tail rate, additional growing-time target
tail/orbit estimates, rare-outcome resources for a particular instrument,
and any stronger fixed-protocol total variation or higher-moment claim.
No new physical parameter selection, initial state law, work measurement
scheme, or formal retained/audited status follows from these bounds.

## 10. Exact source and exposure record

The neutral plan and input identities were sealed before reading the newly
authorized graph content. The evidence directory
`energy_distribution_limit_independent` records exact coverage, retained
snapshots and final hashes. Newly read sources are:

* `GRAPH_ENERGY_INDEPENDENT.md`, SHA-256
  `5c147e2f079f12eb6a4d2f75264ffa51757729c8d444634b203542706fb53967`,
  all 887 lines.
* `GRAPH_ENERGY_CROSSCHECK.md`, SHA-256
  `2b4c75a30b0f70b63eba8912e34804b15bb35d980551467b27ecde970c070ac4`,
  all 578 lines.
* `GRAPH_NATIVE_POSTCOMPARISON_CORRECTIONS.md`, whole-file SHA-256
  `11d55133cd32a47d2bc79151a12f3fb2512bd79ea5144fa40eb747b221e9076f`,
  graph-only lines 8-27. The native body was not read or imported.

The unchanged already-read sources reused are the BV work independent and
crosscheck (`0af3a48b...`, `741b3d4a...`), preparation synthesis and review
(`6d82cfec...`, `fe3aa3cd...`), prepared-pulse independent and crosscheck
(`0096ba16...`, `3fe0db39...`), and driven-state independent and crosscheck
(`e542889e...`, `f050d2c5...`). Their full hashes and the earlier scoped
named-parent/instruction coverage are in the source manifest. Previously
exposed old prepared-pulse and driven-state roots remain declared prior
exposure; they are not newly independent evidence. Their originals and
all prior freezes remain unchanged.

The graph crosscheck reproduces comparisons to its own earlier root source;
that reproduced material is within the newly authorized complete crosscheck.
No underlying new root original was opened. The new energy-distribution
root/seals, all other new root candidates, low-block and Lean sources,
phase-space material, publication package, checkpoint/HANDOFF/queue and
outcomes remained unexposed through this note's freeze. No other source
was required to establish the displayed conditional consequences.

Verification is symbolic derivation and complete author reading with
explicit source identities. Standard-library filesystem hashing, copying,
counting and JSON bookkeeping are not scientific computation. No scientific
runner, formal checker, installation, Git action, repository mutation,
other-chat message, audit action or delegation occurred for this task.

## Assembly source and dependency crosswalk

The complete source body above comes from
ENERGY_DISTRIBUTION_LIMIT_INDEPENDENT.md. Its one accepted wording change is
the sufficient-tail qualification authorized by
ENERGY_DISTRIBUTION_POSTCOMPARISON_PRECISIONS.md
(`54d600e491a46d3c84d9d4b3ae849d4d3019f18f5aa6e0736f3f1b606c9fdd62`).
Exact old/new text, body and full-assembly diffs, and byte/line maps accompany
this source packet. No displayed formula or counterexample is repaired away.

The named canonical parents have distinct roles:

| Parent | Used role and limit |
|---|---|
| [BV and graph energy protocol](BV_GRAPH_ENERGY_PROTOCOL_BOUNDED_THEOREM_NOTE_2026-10-13.md) | Actual commuting energy bridge, graph preparation/work resources and regular insertion hypotheses/constructions. Its BV and Graph bodies retain their separate premises. |
| [Prepared and driven state](PREPARED_DRIVEN_STATE_BOUNDED_THEOREM_NOTE_2026-10-13.md) | Prepared-pulse and driven-state trace comparison for the stated protocol targets and windows. It does not give arbitrary growing-time control. |
| [Current refinement](CURRENT_PRESERVING_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md) | Actual branch dispersion, placement and normalization conventions; its claim remains open_gate. |
| [Local even continuum](LOCAL_EVEN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-10-12.md) | Supplied continuum CAR/Fock carrier and bounded even observable conventions. |
| [Bounded-interaction ground](BOUNDED_INTERACTION_GROUND_BOUNDED_THEOREM_NOTE_2026-10-12.md) | Supplied ground/gap and static comparison resources used in the protocol specialization. |
| [Adiabatic preparation](ADIABATIC_GROUND_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-12.md) | The specified ramp resource; no unsupported parity-sector enlargement is imported. |
| [Time-averaged energy transfer](TIME_AVERAGED_ENERGY_TRANSFER_BOUNDED_THEOREM_NOTE_2026-10-12.md) | Named regularization input inherited through the graph source; abstract insertion results still require their explicit domain and commutator hypotheses. |

Canonical hashes, the exact BV/Graph and Prepared/Driven body placements,
transitive inherited roles and actual reading coverage are bound in the
packet's ACCEPTED_PARENT_SOURCE_BINDINGS.json and ACCEPTED_DEPENDENCY_MAP.json. Their byte
checks are bookkeeping. They are not a fresh proof of every upstream claim.
The already supplied model, state, measurement and protocol choices remain
inputs. No physical detector selection, microscopic derivation of these
choices, total-variation endpoint, general rare-outcome limit, or automatic
growing-time theorem is added by this assembly.

The negative controls keep their literal state/protocol classes. Existing
scoped stress checks are preserved; N1/N5 global-packet obligations remain
pending, and no completed no-go packet or packet PASS is assigned.

The evidence archive retains the independent freeze, full comparison,
read-coverage records and root acceptance chronology. No scientific/formal
runner, publication driver or audit was executed in assembling this note.
The source assembly has root acceptance with honest limits on fresh reading.
New publication integration and registration require the separately reviewed
root procedure and its actual execution receipts.

The [publication packet](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/8c88ed444f104bfd482c5886d28d7b09f68c6c1b/.claude/science/physics-loops/toe-energy-observables-20261013/README.md) binds exact archives,
complete publication diffs, parent identities, review chronology and pending
obligations. The [identity-only runner](../scripts/energy_distribution_limit_identity_2026_10_13.py) verifies bytes and
reconstruction only; it supplies no mathematical proof, independent audit or
retained status. Original pending/exposure statements within the body remain
historical. The exact source acceptance retains its false fresh-full-note and
fresh-full-context-diff read fields.


Review-loop integration note: dependencies are integrated through main 160abf2a01435d2afcc3561d25a592da0c0eb4a2 and this reviewed energy/dynamics batch. Original analytic arguments and historical evidence remain preserved. Live canonical parent hashes are refreshed with original bindings retained; earlier pending/main labels describe publication-time provenance and confer no audit authority. Any formatting-only transformations are explicitly recorded in the publication map.
