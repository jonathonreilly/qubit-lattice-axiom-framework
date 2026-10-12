---
claim_id: bounded_interaction_ground_bounded_theorem_note_2026-10-12
claim_type: bounded_theorem
claim_scope: "Bounded total even perturbations, energy-controlled subsequences, and small-interaction unique ground selection in the supplied actual two-branch model."
upstream_dependencies:
  - energy_transfer_correlation_bounded_theorem_note_2026-10-12
  - current_preserving_refinement_bounded_theorem_note_2026-10-12
  - concrete_gapped_chain_bounded_theorem_note_2026-10-12
  - local_even_continuum_bounded_theorem_note_2026-10-12
runner: scripts/bounded_interaction_ground_identity_2026_10_12.py
artifact_role: theorem
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: partially_closes
target_claim_id: null
target_blocker_text: "Extend supplied free dynamics to bounded interactions and isolate conditions that select a continuum ground density."
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

Primary runner: [source identity and reconstruction only](../scripts/bounded_interaction_ground_identity_2026_10_12.py).
It executes zero mathematical predicates, scientific mutations or Lean checks.
Archive hashes and reconstruction are not mathematical evidence.

**Publication provenance and review.** The following 1057-line frozen assembly
has SHA-256 `b8bcba769100bf819885937d850a7bff8543e4233c1df3cf65f68372552160e9`.
Its complete 307-line source-exposed review has SHA-256
`af0cf7d6e9ea98fc92ac86df651c136cb2766f40571b814b69f3850304ebfe53`.
Root read the complete assembly and review. The bounded-interaction and ground
cores were independently derived before comparison within the same model
family and shared premises; the assembly and its review are source exposed.
No theorem-invalidating finding was reported. Their actual exposure records,
counterexamples, numerical precision clarifications and original pending
statuses are preserved in the reconstructable archive.

All mathematics below is unchanged. Four Markdown targets in the source's
dependency record are relocated to their canonical publication notes, preserving
the labels. Exact old/new targets and a link-only diff are recorded. Later completed formal-scope
evidence is described after it, without rewriting its historical status.
Final publication wrapper/program review and root execution acceptance remain
pending in this source preparation. This is one part of a two-note milestone,
not a new independent proof or retained-status decision.


# Bounded even interactions and conditional ground-state selection

Status: proposed conditional theorem for the supplied one-dimensional chain.
This is a source-exposed coauthor synthesis of the frozen derivations and
ordinary checks listed in section 12, with shared premises and the same-model
limits recorded there. The assembled source has not yet received its own exact
review. It is not a retained claim, an audit verdict, a new physical axiom, or
an analytic Lean theorem.

There are two different state conclusions. A uniformly bounded **total** even
interaction and a uniform mean interacting-energy bound give subsequential
normal-state limits and compact-time ordinary-cell correlations. The additional
smallness bound \(K<m/2\), together with vanishing **actual excess energy above
the finite-spacing ground**, gives a unique ground state in the supplied
representation and convergence without a subsequence. The latter preparation
hypothesis is not implied by a fixed mean-energy ceiling or by a realized-state
primitive. Neither theorem selects the interaction or its coupling physically.

## 1. Supplied model, spaces, and complete hypotheses

Fix \(m,v>0\). The load-bearing parent sources are Current C2, C9, C14, C21,
C25 and its corrected physical-time convention; Concrete section 6 (the full
spin GNS representation, its positive Fock Hamiltonian and gap); and Local L10
and its ordinary-cell/even-spin identification. Their exact source identities
at main `516cb69d8487ff04f8a48e065d3dcbe71d7dd237` are in section 12 and the
input manifest. They are supplied conditional model premises, not conclusions
derived here from a more primitive framework.

Write \(\mathfrak h_L=P_+L^2(\mathbb R;\mathbb C^2)\) for the target positive
polarization, where in Fourier coordinates

\[
D(p)=-vp\sigma_x-m\sigma_y,\qquad
E(p)=\sqrt{m^2+v^2p^2},\qquad P_+(p)=\tfrac12(I+D(p)/E(p)).                 \tag{1}
\]

The high positive-polarization copy is \(\mathfrak h_H\). The common full
carrier, with the low factor ordered first in the graded tensor identification,
is

\[
\mathcal F_* = \mathcal F_-(\mathfrak h_L\oplus\mathfrak h_H)
       \simeq \mathcal F_L\otimes\mathcal F_H,\qquad H_0=d\Gamma(E)
       \text{ on }\mathcal F_L.                                             \tag{2}
\]

The low CAR algebra acts as its usual full-Fock representation tensor \(I_H\).
Odd Majoranas used in formulas are auxiliary coordinates; the observable blocks
and perturbations below are separately even and have the physical even-spin
interpretation supplied by the parents. No restriction to the even-vacuum Fock
sector is made in (2).

For spacing \(c>0\), put \(I_c=(-1/c,1/c)\), \(w_c(p)=\sqrt{1-c^2p^2}\) on
\(I_c\). The actual positive one-particle dispersions after the current carrier
map are

\[
 e_{c,L}(p)^2=m^2+\frac{2v^2p^2}{1+w_c(p)},\qquad
 e_{c,H}(p)^2=m^2+\frac{2v^2}{c^2}(1+w_c(p)).                                \tag{3}
\]

The null endpoints of \(I_c\) do not affect the multiplication operators.
Let \(\iota_c\) be the second-quantized actual positive-energy isometry from
Current. Distinguish the following projections throughout:

\[
\begin{aligned}
\Pi_c&=\iota_c\iota_c^*
       &&\text{(vacuum outside both actual momentum bands)},\\
q_c&=\Gamma(\mathbf1_{I_c})\text{ on }\mathcal F_L
       &&\text{(the full low Fock-band projection, including its vacuum)},\\
P&=I_L\otimes|\Omega_H\rangle\langle\Omega_H|,\quad Q=I-P
       &&\text{(high vacuum and its complement)},\\
P_{g,c},P_{g,0}&&&\text{(rank-one interacting ground projections, when proved).}
\end{aligned}                                                             \tag{4}
\]

Thus \(\Pi_c\) is a Fock projection, not a one-particle cutoff, and
\(P\Pi_c=q_c\otimes|\Omega_H\rangle\langle\Omega_H|\). The symbols in (4)
must not be interchanged. In particular, the ground projections generally do
not equal the free high-vacuum projection or commute with it.

The actual \(H_c\), represented on \(\Pi_c\mathcal F_*\), is the positive
second quantization of (3), with no vacuum energy offset. Its maximal operator
domain is \(\mathcal D(N)\) at each fixed \(c\), since its one-particle energy is
bounded above and bounded below by \(m\). The target \(H_0\) has its maximal
weighted Fock multiplication domain; this is generally smaller than
\(\mathcal D(N)\). Both free operators have a simple vacuum eigenvalue zero and
spectrum in \(\{0\}\cup[m,\infty)\). The even sector has threshold \(2m\) away
from its vacuum. Directly from (3), on the actual physical range,

\[
 E\le e_{c,L}\le\sqrt2 E,\quad
 \Lambda_c=\sqrt{m^2+2v^2/c^2},\quad
 H_c\ge H_0\otimes I_H,\quad H_c\ge\Lambda_c N_H\ge\Lambda_c Q.              \tag{5}
\]

The first many-body inequality uses the low band restriction of \(H_0\);
outside-band modes are in their vacuum on the actual range. It is a quadratic
form assertion there, not a claim about an unspecified extension of \(H_c\).

Here are the interaction and observable hypotheses. They hold for
\(0<c<c_0\), with a fixed finite \(K\ge0\):

1. \(\widehat V_c\) is a bounded, selfadjoint, even, in-band CAR element on the
   common carrier, in its **unital** CAR extension; it reduces \(\Pi_c\).
   Its actual restriction is \(V_c\). The target is selfadjoint even
   \(V_0\in\operatorname{CAR}(\mathfrak h_L)\), with
   \(\widehat V_0=V_0\otimes I_H\), and
   \(\|\widehat V_c\|,\|V_0\|\le K\).
2. For each finite \(T\), the free orbits obey

   \[
   \nu_{V,c}(T)=\sup_{|t|\le T}
       \|\alpha_{c,t}(\widehat V_c)-\alpha_{0,t}(V_0)\otimes I_H\|
       \longrightarrow0.                                                   \tag{6}
   \]

3. For a specified finite word, its separately even blocks
   \(\widehat A_{j,c},A_{j,0}\) have the same in-band/low CAR placement, norm
   bounds \(L_j\) for both, and free-orbit errors

   \[
   \nu_{j,c}(T)=\sup_{|t|\le T}
       \|\alpha_{c,t}(\widehat A_{j,c})-
             \alpha_{0,t}(A_{j,0})\otimes I_H\|\longrightarrow0.              \tag{7}
   \]

The common \(\alpha_c\) may be defined by any fixed block-diagonal
selfadjoint one-particle extension outside the band, for example zero there.
It agrees with the physical dynamics on in-band CAR and preserves the
outside-band vacuum subspace. Its second quantization implements a point-norm
continuous CAR flow. Only (6)-(7) are used to compare it with the target flow;
no comparison on arbitrary high or outside-band observables is presumed.
The extended generator can have extra zero modes and must **not** be used in
place of the actual \(H_c\) for the gap argument below.

The common extensions of \(\widehat V_c\), \(\widehat A_{j,c}\) and the identity
are unital CAR operators: they act on the remaining modes, including the high
factor for a low target, by the appropriate CAR extension. By contrast, the
resolvents in section 7 are zero outside their physical subspaces. A zero
extension of an identity or observable would give a different norm comparison.

For ground convergence alone, section 8 uses the weaker time-zero premise
\(\nu_c=\|\widehat V_c-\widehat V_0\|\to0\), plus \(K<m/2\); it does not need
(6), (7), or the normal-state compactness lemma. For arbitrary varying
potentials, time-zero norm convergence does not replace the explicitly assumed
orbit comparison (6) in the dynamical theorem.

## 2. A concrete ordinary-cell class satisfying the hypotheses

For a real \(L^2\) coefficient field \(f\) supported in a fixed compact physical
interval, use the actual ordinary cell average

\[
 (C_cf)_j=c^{-1/2}\int_{cj}^{c(j+1)}f(x)\,dx,\qquad
 \|C_cf\|\le\|f\|.                                                         \tag{8}
\]

Current C21 and C25 give, in the same real coefficient carrier,

\[
 J_cC_cf\longrightarrow(f,0),\qquad
 \sup_{|t|\le T}\|J_ce^{itD_c}C_cf-(e^{itD}f,0)\|\longrightarrow0             \tag{9}
\]

for every \(L^2\) input, not only for smooth inputs. The CAR field norm is the
real coefficient norm. Product telescoping therefore promotes (9) to (6)-(7)
for every fixed finite even *-polynomial in these fields, with its corresponding
target polynomial. Choose a selfadjoint polynomial for a potential, or replace
\(B\) by \((B+B^*)/2\); evenness by itself does not imply selfadjointness.

Explicitly, for a monomial of degree \(r\), coefficient errors \(d_{k,c}(T)\)
and bounds \(b_k\) for both coefficients give the orbit error at most
\(\sum_{k=1}^r d_{k,c}(T)\prod_{\ell\ne k}b_\ell\). Add these bounds with the
absolute polynomial coefficients. They tend to zero and supply fixed norm
bounds, including a finite \(K\) for the single total potential. The same proof
allows cell inputs tending to fixed inputs in \(L^2\) and finitely many scalar
coefficients tending to fixed values. This slightly enlarged class includes the
normalized cell example in section 6; normalization is not literally a fixed
finite-spacing polynomial coefficient.

Local L10 supplies the physical even-spin representatives. At spacing \(c\)
they lie in the finite cell hull of the fixed compact supports, with at most
one-cell endpoint enlargement on either side. The number of cells can grow
as \(c\downarrow0\). Their images under \(J_c\) are band limited and need not be
exactly supported in the same continuum interval; (9), rather than an exact
support identification, is the comparison used here. No additional spectral
transfer bound, commutator bound, or energy-form mapping property is required
for this fixed ordinary \(L^2\)-cell class.

This is a uniformly bounded **total** perturbation confined to a fixed region.
It does not cover an extensive sum whose total operator norm grows with volume
or cell count. A bound on each summand alone would not supply \(K\).

## 3. Domains, interacting dynamics, and the word comparison

Define the actual and target Hamiltonians

\[
 G_c=H_c+V_c,\quad\mathcal D(G_c)=\mathcal D(H_c),\qquad
 G_0=H_0+V_0,\quad\mathcal D(G_0)=\mathcal D(H_0).                            \tag{10}
\]

They are selfadjoint and bounded below by \(-K\). One direct proof is to take
\(\eta>K\): \(I+V(H\mp i\eta)^{-1}\) has its Neumann inverse, so the closed
symmetric operator \(H+V\) has surjective \(G\mp i\eta\) and is selfadjoint.
The form \(q_G=q_H+\langle\cdot,V\cdot\rangle\) is closed and semibounded on
\(\mathcal D(H^{1/2})\); its shifted form norm is equivalent to the free form
norm. Thus the form domains also agree. There is no premise or conclusion
that \(V\) preserves either the free operator domain or its form domain.

For a normal density \(\rho\), define the semibounded expectation by

\[
 \mathcal E_G(\rho)=\operatorname{Tr}\rho(G+K)-K.                             \tag{11}
\]

Here the trace of a positive unbounded operator is its nonnegative quadratic
form expectation, equivalently its spectral-truncation limit. Whenever finite,
\(\mathcal E_G(\rho)=\mathcal E_H(\rho)+\operatorname{Tr}\rho V\). This avoids
an unjustified trace of a product of unbounded operators.

For the common-carrier comparison, name the chosen free extension
\(\widehat H_c\), and put
\(\widehat G_c=\widehat H_c+\widehat V_c\) on
\(\mathcal D(\widehat H_c)=\mathcal D(\widehat G_c)\). Set

\[
 Z_c(t)=e^{it\widehat G_c}e^{-it\widehat H_c},\qquad
 B_c(t)=\alpha_{c,t}(\widehat V_c).
\]

The restrictions of these exponentials to the physical range are exactly the
actual \(e^{itG_c}\) and \(e^{-itH_c}\). Differentiate the implementing product
strongly on \(\mathcal D(\widehat H_c)=\mathcal D(\widehat G_c)\) to obtain

\[
 Z_c'(t)=iZ_c(t)B_c(t),\qquad Z_c(0)=I.                                      \tag{12}
\]

The two unbounded terms combine into
\(i e^{it\widehat G_c}\widehat V_c e^{-it\widehat H_c}\);
no differentiation of \(\widehat V_c\) on that domain is
needed. Independently, the bounded norm-continuous coefficient \(B_c(t)\) gives
a unique norm-differentiable solution of the integral equation (12), by its
convergent iterated integrals on bounded time intervals. Selfadjointness of
\(B_c(t)\) makes the solution unitary. Strong uniqueness on the dense domain
identifies it with the implementing product. Its integrals lie in the unital
even CAR algebra. Consequently

\[
 \beta_{c,t}(A)=e^{it\widehat G_c}Ae^{-it\widehat G_c}
              =Z_c(t)\alpha_{c,t}(A)Z_c(t)^*                               \tag{13}
\]

is a grading-preserving, point-norm continuous CAR flow. The target satisfies
the same statements in low CAR. Write its cocycle tensored with \(I_H\) as
\(Z_0\). The useful right-generator identity has the sign and order

\[
 (Z_cZ_0^*)'(t)=iZ_c(t)(B_c(t)-B_0(t))Z_0(t)^*.
\]

Integrating forwards or backwards and using unitarity yields, without an
exponential factor,

\[
 \|Z_c(t)-Z_0(t)\|
 \le\int_{\min(0,t)}^{\max(0,t)}\|B_c(s)-B_0(s)\|\,ds
 \le |t|\nu_{V,c}(T)\quad (|t|\le T).                                      \tag{14}
\]

First split the free-observable difference in (13), then the difference of
the two unitary conjugations. This proves

\[
 \sup_{|t|\le T}\|\beta_{c,t}(\widehat A_{j,c})-
                     \beta_{0,t}(A_{j,0})\otimes I_H\|
 \le \nu_{j,c}(T)+2T\|A_{j,0}\|\nu_{V,c}(T).                                \tag{15}
\]

For a fixed word in the displayed product order, with no assumption that its
times are chronologically ordered, put

\[
 W_c(\mathbf t)=\prod_{j=1}^n\beta_{c,t_j}(\widehat A_{j,c}),\quad
 W_0(\mathbf t)=\prod_{j=1}^n\beta_{0,t_j}(A_{j,0}),\quad L=\prod_j L_j.
\]

A telescoping expansion gives the explicit finite-word constant

\[
 \sup_{\mathbf t\in[-T,T]^n}\|W_c(\mathbf t)-W_0(\mathbf t)\otimes I_H\|
 \le \zeta_c(T):=
 \sum_{j=1}^n\bigl[\nu_{j,c}(T)+2T\|A_{j,0}\|\nu_{V,c}(T)\bigr]
                  \prod_{k\ne j}L_k\longrightarrow0.                       \tag{16}
\]

This compares the complete products as unital operators. It does not replace
the compression of a product by a product of compressions and needs no energy
control after individual observable insertions.

## 4. The arbitrary bounded-interaction subsequence theorem

Assume (1)-(7), with any finite \(K\), and actual normal densities \(\rho_c\)
satisfying

\[
 \mathcal E_{G_c}(\rho_c)\le M<\infty.                                      \tag{17}
\]

The class is nonempty only if \(M+K\ge0\). Embed the density by
\(\widehat\rho_c=\iota_c\rho_c\iota_c^*\), and use the full high partial trace
\(\tau_c=\operatorname{Tr}_H\widehat\rho_c\), not a normalized high-vacuum
compression. Then

\[
 \operatorname{Tr}\tau_c=1,\qquad
 \mathcal E_{H_0}(\tau_c)\le\mathcal E_{H_c}(\rho_c)\le M+K.                 \tag{18}
\]

We explicitly invoke the normal-CAR compactness lemma proved in section 11
of the frozen `ENERGY_TRANSFER_CORRELATION_SYNTHESIS.md`, SHA-256
`d63214a0d6365e1ae339f63caad67526bdd942130f76b064b13c2b7b2365b49c`.
It says: on separable full fermionic Fock space, a uniform mean
\(d\Gamma(e)\) bound with \(e\ge mI>0\) gives, from every sequence of normal
densities, a subsequence converging on the entire CAR algebra to a state
represented by a full-Fock normal density of no larger free energy. The normal
extension of that full CAR state is unique. This is an explicit proof dependency,
not a new proof of the normality lemma here. Its separate exact-source review
is recorded in section 12. Its proposal/publication provenance does not give it
main, retained, or audit authority.

Apply the lemma to (18). From every sequence \(c_n\downarrow0\) (or any positive
sequence tending to zero) one can choose a single subsequence on which

\[
 \operatorname{Tr}\tau_c A\longrightarrow\operatorname{Tr}\tau A
       \quad\text{for every }A\in\operatorname{CAR}(\mathfrak h_L),\qquad
 \mathcal E_{H_0}(\tau)\le M+K.                                             \tag{19}
\]

The same subsequence serves all fixed tests. It is not a trace-norm compactness
statement or a statement of convergence on all \(B(\mathcal F_L)\).

The interacting energy has the sharper inherited bound

\[
 \mathcal E_{G_0}(\tau)
 \le\liminf_{\text{chosen subsequence}}\mathcal E_{G_c}(\rho_c)\le M.         \tag{20}
\]

Here is the full passage for (20). For any positive finite-rank one-particle
operator \(b\le E\) in form order, \(d\Gamma(b)\) is a bounded positive CAR
observable: its norm is at most \(\operatorname{Tr}b\). Equations (5) and
\(\nu_c\le\nu_{V,c}(T)\to0\) give

\[
 \operatorname{Tr}\tau_c d\Gamma(b)+\operatorname{Tr}\tau_c V_0
 \le\mathcal E_{G_c}(\rho_c)+\nu_c.                                        \tag{21}
\]

The test \(b\) need not preserve the band; its form domination by \(E\) suffices
on the actual state. Both terms on the left converge by (19), including the
indefinite potential term because \(V_0\in\operatorname{CAR}\). To recover the
entire free energy, take \(E_R=\min(E,R)\), finite-rank projections
\(p_\ell\uparrow I\) strongly, and
\(b_{R,\ell}=E_R^{1/2}p_\ell E_R^{1/2}\le E\). For each fixed \(R\), these
increase in \(\ell\) strongly to \(E_R\). The one-particle density of \(\tau\)
is trace class since \(\operatorname{Tr}\tau N\le(M+K)/m\). Monotone convergence
of its trace pairing first in \(\ell\), then in \(R\), gives

\[
 \sup_{R,\ell}\operatorname{Tr}\tau d\Gamma(b_{R,\ell})
       =\mathcal E_{H_0}(\tau).
\]

No monotonicity in \(R\) at fixed noncommuting \(p_\ell\) is asserted. Take the
liminf in (21) for each test and then this supremum to obtain (20). In
particular the valid free-energy estimate is
\(\mathcal E_{H_0}(\tau)\le M-\operatorname{Tr}\tau V_0\le M-\inf\sigma(V_0)\),
not in general \(M\).

For the words in (16), along the same subsequence,

\[
 \sup_{\mathbf t\in[-T,T]^n}
 \left|\operatorname{Tr}\rho_c W_c^{\rm actual}(\mathbf t)
             -\operatorname{Tr}\tau W_0(\mathbf t)\right|\longrightarrow0.   \tag{22}
\]

Indeed, the difference from \(\operatorname{Tr}\tau_cW_0(\mathbf t)\) is at
most \(\zeta_c(T)\), by (16) and the definition of partial trace. The map
\(\mathbf t\mapsto W_0(\mathbf t)\) is norm continuous from the compact time
cube into low CAR. Its image is norm compact. Pointwise convergence of norm-one
states on CAR is uniform on this image: use a finite norm-\(\varepsilon\) net,
convergence on its finitely many centers, and a \(2\varepsilon\) bound for the
two state errors between each test and its center. This proves (22), without
a rate for the state part or a further subsequence for each observable.

If the input states are parity invariant, so are their partial traces and the
limit in (19). Definite support in the even global Fock sector is a stronger
condition and need not pass to a CAR limit; section 10 gives the escape example.
The theorem therefore uses full-Fock normality, including possible odd-sector
weight. It does not infer a unique \(\tau\) across different subsequences,
stationarity, or a preferred realized state.

## 5. High occupation and its precise role

From (5) and (18),

\[
 \operatorname{Tr}\widehat\rho_c N_H\le\frac{M+K}{\Lambda_c},\qquad
 \operatorname{Tr}\widehat\rho_c Q\le\frac{M+K}{\Lambda_c}.                  \tag{23}
\]

These inequalities hold at every real time for the density evolved by \(G_c\),
because its \(G_c\)-energy is conserved and
\(\mathcal E_{H_c}\le\mathcal E_{G_c}+K\) still holds. This argument does not
claim that \(Q\), \(N_H\), or the free energy commutes with \(G_c\).

The direct proof of (22) uses the trace-one \(\tau_c\) and the full operator
comparison (16), so it incurs neither a high-vacuum normalization error nor a
separate high-occupation error. Equation (23) remains a useful state estimate;
it cannot replace (6)-(7) for arbitrary spacing-dependent observables. No
multitime assertion is inferred by multiplying single-factor compressions.

## 6. Nonquadratic local interaction and a rough-domain example

### 6.1 Normalized and unnormalized quartics are different formulas

Choose six normalized real \(C_c^\infty\) coefficient fields \(f_1,\ldots,f_6\)
with pairwise disjoint spatial supports separated by positive distances inside
a fixed compact interval. Set
\[
 \Gamma_{j,c}=\gamma(C_cf_j),\qquad n_{j,c}=\|C_cf_j\|\longrightarrow1.
\]
For all sufficiently small \(c\), the cell supports are disjoint,
\(n_{j,c}>0\), and
\(\Gamma_{j,c}^2=n_{j,c}^2I\),
\(\Gamma_{j,c}\Gamma_{k,c}=-\Gamma_{k,c}\Gamma_{j,c}\) for \(j\ne k\).
Here \(\gamma\) denotes the selfadjoint Majorana field of a real coefficient.

The normalized \(C_{j,c}=\Gamma_{j,c}/n_{j,c}\), and their target
\(C_{j,0}=\gamma(f_j)\), satisfy \(C_j^2=I\) and pairwise anticommutation.
For real \(\lambda\ne0\), define
\[
 V_c^{N}=\lambda C_{1,c}C_{2,c}C_{3,c}C_{4,c},\qquad
 A_c^{N}=iC_{1,c}C_{5,c}.                                                    \tag{24}
\]
Both are even and selfadjoint. Reversing four factors has sign
\((-1)^6=1\), and the fourfold product squares to \(I\); hence
\(\|V_c^{N}\|=|\lambda|\). The same is true at the target. Their finite-spacing
physical spin representatives are supported in the cell hull described in
section 2. The normalization coefficients converge to one and are bounded
eventually, so this is in the enlarged convergent-coefficient class of that
section. It is not literally a polynomial with spacing-independent
coefficients in the unnormalized \(C_cf_j\).

The multiplication, including its sign, is
\[
 V_c^{N}A_c^{N}=-i\lambda C_{2,c}C_{3,c}C_{4,c}C_{5,c},\quad
 A_c^{N}V_c^{N}=+i\lambda C_{2,c}C_{3,c}C_{4,c}C_{5,c},
\]
and therefore
\[
 i[V_c^{N},A_c^{N}]=2\lambda C_{2,c}C_{3,c}C_{4,c}C_{5,c}.                   \tag{25}
\]

A strict fixed-polynomial alternative, selfadjoint at every spacing, is
\[
 V_c^{F}=\frac{\lambda}{2}
  (\Gamma_{1,c}\Gamma_{2,c}\Gamma_{3,c}\Gamma_{4,c}
   +\Gamma_{4,c}\Gamma_{3,c}\Gamma_{2,c}\Gamma_{1,c}).                         \tag{26}
\]
It has the same normalized-input target and
\(\|V_c^{F}\|\le|\lambda|\prod_{j=1}^4\|f_j\|=|\lambda|\).
At sufficiently small \(c\), (26) equals the forward product. With
\(A_c^{F}=i\Gamma_{1,c}\Gamma_{5,c}\) there, the correct identity is
\[
 i[V_c^{F},A_c^{F}]
       =2\lambda n_{1,c}^{\,2}
               \Gamma_{2,c}\Gamma_{3,c}\Gamma_{4,c}\Gamma_{5,c}.              \tag{27}
\]
For all spacings the selfadjoint observable can instead be written
\(i[\Gamma_{1,c},\Gamma_{5,c}]/2\), which agrees with this \(A_c^F\) in the
disjoint-support regime. The factor \(n_{1,c}^{\,2}\) in (27) cannot be dropped.
For nonnormalized input functions the bound in (26) is
\(|\lambda|\prod_{j=1}^4\|f_j\|\), so the sufficient ground-smallness test is
that product \(<m/2\); \(|\lambda|<m/2\) alone is sufficient here only with the
stated unit norms or with the explicitly normalized construction (24).

These are genuinely nonquadratic effects. The six orthonormal real Majoranas
generate a faithful complex Clifford algebra \({\rm Cl}_6\simeq M_8(\mathbb C)\).
Distinct monomials are orthogonal for its normalized matrix trace. Thus the
nonzero grade-four term in (25) is linearly independent of scalar and
grade-two terms. The fifth generator gives a nontrivial even observable to
commute with the first four; the sixth supplies the convenient even-dimensional
simple Clifford algebra. The smooth chosen inputs are in the one-particle
generator domain, so the free CAR derivation of \(iC_1C_5\) is a sum of
bilinears. A quadratic/quasifree derivation on any larger coefficient space
also sends a bilinear to scalar-plus-bilinear expressions. The canonical
tracial conditional expectation onto these six real modes sends those
expressions into the scalar/grade-two subspace of \(M_8\), while fixing the
grade-four term. It therefore cannot absorb (25) into a quadratic generator.
This is a bounded local interacting witness, not just a changed one-particle
dispersion. The faithful representation, grading, and analytic domain facts
in this paragraph are handwritten arguments, outside the formal identity
reported in section 11.

### 6.2 Bounded local potentials need not preserve the free form domain

Take \(f=\mathbf1_{[0,1]}e_1\) and nonzero real smooth \(g=g_1e_1\) supported
inside \((2,3)\). The real coefficient supports are disjoint, so
\[
 V_0=i\gamma(f)\gamma(g)
\]
is bounded, selfadjoint, even, and local. A strict all-spacing selfadjoint
approximant is \(V_c=i[\gamma(C_cf),\gamma(C_cg)]/2\); section 2 applies.
This example does not require any new quantitative convergence rate.

Let \(u=\sqrt2P_+\widehat f\), \(z=\sqrt2P_+\widehat g\) in the positive
one-particle space. Since \(P_{+,11}=1/2\), the unitary Fourier convention gives
\[
 \|u(p)\|^2=\frac{1-\cos p}{\pi p^2},\qquad
 \int_{\mathbb R}E(p)\|u(p)\|^2\,dp=\infty.                                  \tag{28}
\]
For example, integrating over intervals of fixed width on which
\(1-\cos p\) is bounded below gives a divergent harmonic series, since
\(E(p)\ge v|p|\). In contrast \(z\ne0\) belongs to \(\mathcal D(E^{1/2})\)
because \(g\) is smooth with compact support. Real orthogonality of \(f,g\)
does not require complex orthogonality of \(u,z\). Subtract the \(z\) component:
\[
 u'=u-\frac{\langle z,u\rangle}{\|z\|^2}z.
\]
Then \(u'\perp z\), \(u'\notin\mathcal D(E^{1/2})\), and
\(u\wedge z=u'\wedge z\). For \(E_R=\min(E,R)\), the two-particle form is
\[
 \langle u'\wedge z,d\Gamma(E_R)(u'\wedge z)\rangle
   =\|z\|^2\langle u',E_Ru'\rangle
       +\|u'\|^2\langle z,E_Rz\rangle\longrightarrow\infty.                  \tag{29}
\]
The cross terms vanish by \(u'\perp z\). Acting on the vacuum,
\(V_0\Omega_L\) has this nonzero two-particle component, up to a phase, and
possibly a vacuum component. Hence
\[
 \Omega_L\in\mathcal D(H_0),\qquad
 V_0\Omega_L\notin\mathcal D(H_0^{1/2}).                                      \tag{30}
\]
There is no conflict with (10): bounded selfadjoint perturbations have the same
operator and form domains as the free Hamiltonian without mapping those
domains into themselves. Their unitary groups preserve their own operator
and form domains, but a bounded observable insertion need not do so.
At fixed \(c\) the one-particle dispersion is bounded; this does not give a
uniform continuum commutator or form bound for the rough example.

## 7. Actual free and perturbed compressed resolvents

The following estimates do not use the normality lemma, the cocycle theorem,
or smooth cell coefficients. Assume (1)-(5), bounded selfadjoint in-band
\(\widehat V_c\) reducing \(\Pi_c\), low \(\widehat V_0=V_0\otimes I_H\),
the bound \(K\), and only
\(\nu_c=\|\widehat V_c-\widehat V_0\|\to0\).
Choose any fixed \(\mu>K\). Define bounded positive operators on the entire
common carrier by
\[
 R_c=\iota_c(H_c+\mu)^{-1}\iota_c^*,\qquad
 R_0=(H_0+\mu)^{-1}\otimes|\Omega_H\rangle\langle\Omega_H|.                    \tag{31}
\]
These are **compressed, zero-extended resolvents**. They are not the resolvents
of ordinary densely defined operators on all of \(\mathcal F_*\): each has
an outside-physical kernel. In particular \(R_0\) is not
\((H_0\otimes I_H+\mu)^{-1}\).

### 7.1 Uniform free estimate over every particle sector

On \(I_c\), \(1-w_c(p)\le c|p|\). Rationalization of (3) gives
\[
 e_{c,L}-E
  =\frac{v^2p^2(1-w_c)}{(1+w_c)(e_{c,L}+E)}
  \le\frac{cv}{2}p^2\le\frac{c}{2v}E^2.                                    \tag{32}
\]
For \(p\ne0\), use \(e_{c,L}+E\ge2v|p|\); at \(p=0\) the difference is zero.
On any finite-particle low-band configuration put
\(x=\sum_i E(p_i)\), \(y=\sum_i e_{c,L}(p_i)\). Thus
\[
 0\le y-x\le\frac{c}{2v}\sum_i E(p_i)^2\le\frac{c}{2v}x^2,\quad
 \left|\frac1{y+\mu}-\frac1{x+\mu}\right|
   =\frac{y-x}{(y+\mu)(x+\mu)}\le\frac{c}{2v}.                               \tag{33}
\]
On the vacuum the difference is zero. This multiplication bound is uniform
over all particle numbers, so it bounds the entire low-band Fock block.

For precision, the root derivation also proved the smaller low-block constant
\[
 \frac{c}{v}\sqrt{\frac{\sqrt2-1}{2}}\ \simeq\ 0.455\,\frac c v.              \tag{34}
\]
Indeed \(y-x\le ax\) with \(a=\sqrt2-1\). Also
\(1-w_c=c^2p^2/(1+w_c)\), so
\[
 e_{c,L}-E
 =\frac{v^2c^2p^4}{(1+w_c)^2(e_{c,L}+E)}
 \le\frac{c^2}{2v^2}E^3.
\]
Summing and using \(\sum_i E(p_i)^3\le x^3\) gives
\(y-x\le bc^2x^3\), \(b=1/(2v^2)\). For \(x>0\) the resolvent difference is
at most \(\min(a/x,bc^2x)\le c\sqrt{ab}\). Equation (33), the independently
reconstructed \(0.5\,c/v\) bound, is simpler but not smaller than (34).
Both yield the same global bound below.

The four commuting free reducing subspaces are \(P\Pi_c\),
\(P(I-\Pi_c)\), \(Q\Pi_c\), and \(Q(I-\Pi_c)\).
On \(P(I-\Pi_c)\) the target has at least one low particle outside \(I_c\),
so \(H_0\ge E_{\mathrm{edge},c}=\sqrt{m^2+v^2/c^2}\), while \(R_c=0\).
On \(Q\Pi_c\), \(R_0=0\) and \(H_c\ge\Lambda_c\).
Both resolvents vanish on \(Q(I-\Pi_c)\). Taking the maximum of the block
bounds, rather than a sum, proves
\[
 \|R_c-R_0\|
 \le\max\left\{\frac c{2v},
       \frac1{E_{\mathrm{edge},c}+\mu},
       \frac1{\Lambda_c+\mu}\right\}\le\frac c v.                            \tag{35}
\]
One may replace the first entry by (34). This is a norm estimate for the
specified compressed resolvents, not uniform convergence of propagators on
the full high branch or disappearance of its equal-time CAR algebra.

### 7.2 A bounded-potential identity without inverting a compression

Similarly put
\[
 S_c=\iota_c(G_c+\mu)^{-1}\iota_c^*,\qquad
 S_0=(G_0+\mu)^{-1}\otimes|\Omega_H\rangle\langle\Omega_H|.                    \tag{36}
\]
Since \(\|R_c\|,\|R_0\|\le1/\mu\), Neumann series on the full carrier give
\[
 S_c=(I+R_c\widehat V_c)^{-1}R_c
     =R_c(I+\widehat V_cR_c)^{-1},\qquad
 \|(I+R_c\widehat V_c)^{-1}\|,\|(I+\widehat V_cR_c)^{-1}\|
       \le\frac{\mu}{\mu-K},                                                \tag{37}
\]
with the identical target formulas. On the physical range the series is the
ordinary bounded-perturbation resolvent identity. On the complement it gives
zero, because \(R_c=0\) and \(\widehat V_c\) reduces that range. At the target
use \([\widehat V_0,P]=0\). No inverse of \(R_c\) or \(R_0\) on the full carrier
has been taken.

Multiplication on the left by \(I+R_c\widehat V_c\) and on the right by
\(I+\widehat V_0R_0\) proves the exact noncommutative identity
\[
 S_c-S_0=(I+R_c\widehat V_c)^{-1}
   [\,R_c-R_0+R_c(\widehat V_0-\widehat V_c)R_0\,]
          (I+\widehat V_0R_0)^{-1}.                                        \tag{38}
\]
It requires no commutation of \(\widehat V_c\) with \(P\), and no commutation
between the two potentials. The target identity
\([\widehat V_0,P]=0\) was already used above. From (35)-(38),
\[
 \|S_c-S_0\|\le\varepsilon_c,\qquad
 \varepsilon_c=\frac{\mu^2c/v+\nu_c}{(\mu-K)^2}\longrightarrow0.              \tag{39}
\]
For rough ordinary \(L^2\) cells, \(\nu_c\to0\) has no universal rate in this
argument. The displayed \(O(c)+O(\nu_c)\) comparison must not be relabeled an
overall \(O(c)\) convergence theorem.

## 8. Small interactions: simple ground state, gap, and its limit

Now additionally assume
\[
 \|\widehat V_c\|,\|V_0\|\le K<m/2.                                         \tag{40}
\]
Existence and the gap conclusions in this section apply only to spacings
where (40) holds. If it is assumed for \(0<c<c_0\), that is the range of the
conclusion; a family which is small only eventually is not assigned a ground
gap at all other spacings. The all-spacing limit below means convergence as
\(c\to0\) throughout this range, without choosing a subsequence.

### 8.1 The gap is proved from the actual free spectrum

Consider either actual \(H_c\) on its physical space or target \(H_0\), writing
it as \(H\), and interpolate \(H+sV\), \(0\le s\le1\). By the free vacuum
premise its spectrum is contained in \(\{0\}\cup[m,\infty)\), with a simple
zero. The circle \(|z|=m/2\) has distance at least \(m/2\) from that spectrum.
Since \(\|sV(H-z)^{-1}\|<1\), the entire circle stays in the resolvent set of
\(H+sV\), with a uniformly convergent Neumann series. Its Riesz projection is
norm continuous in \(s\) and starts with rank one.

For orthogonal projections \(E,F\) with \(\|E-F\|<1\), the map
\(F:\operatorname{ran}E\to\operatorname{ran}F\) is injective, and the reverse
map is also injective: a vector in the first kernel would have
\(\|(E-F)x\|=\|x\|\). Starting with finite rank, the dimensions therefore agree.
A finite subdivision of \([0,1]\) preserves the rank-one Riesz projection.

The same resolvent Neumann test at real points outside the \(sK\)-neighborhood
of the free spectrum gives
\[
 \sigma(H+sV)\subset[-sK,sK]\ \cup\ [m-sK,\infty).                            \tag{41}
\]
The rank-one projection selects precisely the first cluster. At \(s=1\) it
is a simple eigenvalue \(E_g\in[-K,K]\), with the rest of the spectrum at least
\(m-K>K\). Thus actual and target operators have unique ground lines in these
representations, with uniform gap
\[
 \gamma=m-2K>0.                                                            \tag{42}
\]
No compact-resolvent hypothesis or finite-volume spectral discreteness is
used; the excited spectrum can be continuous.

Evenness preserves parity. The odd free sector is bounded below by \(m\),
so its perturbed energy is at least \(m-K>K\ge E_g\); the ground line is even.
On the even sector the free excited threshold is \(2m\). Applying the same
argument within that sector gives the larger lower gap \(2m-2K\) there.
That larger constant can be used only for states supported in the even
sector, not for every state merely because the ground vector is even.

For the physical spin-cell class, Concrete supplies an irreducible full-spin
GNS representation. In the product spin representation's finite-flip basis,
the local diagonal spin operators force a commuting operator to be diagonal,
and the local flip operators force all its diagonal entries to coincide.
Composition with Concrete's onto spin automorphism preserves that
irreducibility. A nonzero vector is cyclic in an
irreducible representation, since its closed cyclic subspace is reducing.
The actual ground vector therefore defines a pure state in that same spin
representation. Its canonical positive implementing Hamiltonian is
\(G_c-E_{g,c}\), with vacuum energy zero. This is uniqueness of the ground
line **within the supplied representation**. It is not a classification or
uniqueness theorem for all algebraic ground states in inequivalent
representations.

### 8.2 Ground projections and energies from the compressed resolvents

Regard the rank-one actual ground density \(P_{g,c}\) on \(\mathcal F_*\) by
\(\iota_c\), and the target density by tensoring its vector with \(\Omega_H\).
Keep the name \(P_{g,0}\) for this rank-one extension, not for \(P\).
The positive bounded \(S_c,S_0\) have their respective ground vectors as
unique top eigenvectors, with eigenvalues
\[
 \lambda_c=(\mu+E_{g,c})^{-1},\qquad
 \lambda_0=(\mu+E_{g,0})^{-1}.
\]
Define
\[
 a_\mu=\frac1{\mu+K},\quad b_\mu=\frac1{\mu+m-K},\quad
 d_\mu=a_\mu-b_\mu
      =\frac{m-2K}{(\mu+K)(\mu+m-K)}>0.                                     \tag{43}
\]
The top eigenvalues are at least \(a_\mu\); all complementary spectral values
are at most \(b_\mu\), including the outside-physical zero eigenvalues.

Let \(\psi_c\) be a normalized actual ground vector in the common space and
\(Q_{g,0}=I-P_{g,0}\). The bounded equation
\[
 Q_{g,0}(S_0-\lambda_c)\psi_c
       =Q_{g,0}(S_0-S_c)\psi_c
\]
has on \(Q_{g,0}\mathcal F_*\) an inverse with norm at most \(1/d_\mu\), since
\(\lambda_c\ge a_\mu>b_\mu\). Thus
\(\|Q_{g,0}\psi_c\|\le\varepsilon_c/d_\mu\).
For two rank-one projections, the operator norm of their difference is the
sine of their vector angle, and its trace norm is twice that sine. This follows
by diagonalizing their difference on the span of their two unit vectors.
Consequently
\[
 \|P_{g,c}-P_{g,0}\|\le\min(1,\varepsilon_c/d_\mu),\qquad
 \|P_{g,c}-P_{g,0}\|_1\le2\min(1,\varepsilon_c/d_\mu).                        \tag{44}
\]
No assertion that \(\psi_c\in\mathcal D(H_0\otimes I_H)\) is needed for this
bounded resolvent argument.

The top eigenvalue of a positive operator is its norm, so
\(|\lambda_c-\lambda_0|\le\|S_c-S_0\|\). Taking reciprocals with
\(\lambda_c,\lambda_0\ge1/(\mu+K)\) gives
\[
 |E_{g,c}-E_{g,0}|\le(\mu+K)^2\varepsilon_c.                                 \tag{45}
\]
Equations (44)-(45) hold throughout the sufficiently small spacing range.
They use time-zero potential convergence and smallness, not a state
compactness extraction or a uniqueness premise for the possible limits in (19).

## 9. Vanishing actual excess energy selects the ground at all small spacings

Let \(\rho_c\) be arbitrary actual normal densities, with nonnegative form
expectations
\[
 \eta_c=\mathcal E_{G_c-E_{g,c}}(\rho_c)\longrightarrow0.                     \tag{46}
\]
This is an additional preparation/selection hypothesis. It refers to the
actual interacting finite-spacing \(G_c\) and its actual ground energy.
A fixed ceiling in (17) is not a substitute.

The spectral gap gives
\[
 1-\operatorname{Tr}\rho_cP_{g,c}\le\min(1,\eta_c/\gamma).
\]
To see the trace-distance consequence directly, write the density as a
countable mixture of unit vector states. Each vector has distance
\(2\sqrt{1-|\langle\psi_{g,c},\phi\rangle|^2}\) from the pure ground density.
Convexity of trace norm and Cauchy-Schwarz for the mixture give
\(\|\rho_c-P_{g,c}\|_1\le2\sqrt{1-\operatorname{Tr}\rho_cP_{g,c}}\).
This proof needs only the finite form expectation in (46), not that every
vector lies in the operator domain. Combining it with (44) yields
\[
 \|\widehat\rho_c-P_{g,0}\|_1
 \le 2\min(1,\sqrt{\eta_c/\gamma})
      +2\min(1,\varepsilon_c/d_\mu)\longrightarrow0.                        \tag{47}
\]
The whole right side can also be capped by the general trace distance \(2\).
If every \(\rho_c\) is supported in the even sector, \(\gamma\) in the first
term can be replaced by \(2m-2K\); no such replacement follows just from
parity invariance of the density. The state family in (46) automatically has
\[
 \mathcal E_{H_c}(\rho_c)
     \le E_{g,c}+\eta_c+K\le2K+\eta_c,                                       \tag{48}
\]
but the converse implication from a bounded free energy to (46) is false.

For the dynamical observable class also satisfying (6)-(7), (16) and (47)
give the complete all-spacing finite-word bound
\[
\begin{split}
 \sup_{\mathbf t\in[-T,T]^n}
 \left|\operatorname{Tr}\rho_cW_c^{\rm actual}(\mathbf t)
       -\operatorname{Tr}P_{g,0}(W_0(\mathbf t)\otimes I_H)\right|
 \le\zeta_c(T)+2L\left[
       \min(1,\sqrt{\eta_c/\gamma})
           +\min(1,\varepsilon_c/d_\mu)\right]\longrightarrow0.             \tag{49}
\end{split}
\]
Trace-norm convergence in (47) also gives convergence for every fixed bounded
common-carrier operator, a conclusion stronger than (19). Equation (49)
still needs the stated norm comparison for the moving observables. Its time
range is each fixed compact cube. There is no assertion of uniform convergence
on an unbounded time interval.

## 10. Counterexamples and boundaries preserved by the two theorems

### 10.1 Any positive fixed energy cap can leave distinct actual even limits

Take \(V_c=V_0=0\), so the ground is the vacuum even in the small-interaction
regime. Choose orthonormal positive-polarization low vectors \(u,w\) with
momentum support in \(|p|<L_*\), and let \(\phi=u\wedge w\). For
\(c<1/L_*\), \(\phi\) is in the actual low band, with
\[
 2m\le\langle\phi,H_c\phi\rangle
       \le B:=2\sqrt{m^2+2v^2L_*^2}.                                       \tag{50}
\]
Given any ceiling \(C>0\), choose
\(\theta=\min(1/2,C/(2B))>0\). The common embedded vectors
\[
 \psi_c=\sqrt{1-\theta}\,\Omega+\sqrt{\theta}\,\phi
\]
are actual normalized even states, independent of \(c\) in the common carrier.
Their actual free energy is at most \(\theta B\le C\), whereas their excess
above the vacuum is at least \(2m\theta>0\). They do not converge to the
ground. Alternating the vacuum and this vector according, for example, to the
parity of \(\lfloor1/(cL_*)\rfloor\) gives two different subsequential limits
while keeping the same actual energy ceiling.

The difference is visible by an ordinary compact even observable, not just
by a nonlocal bounded-operator projection. First the CAR number projection
\(N_u=a^*(u)a(u)\) has expectations \(\theta\) and \(0\). The real coefficient
map \(f\mapsto\sqrt2P_+\widehat f\) is onto \(\mathfrak h_L\) as a real Hilbert space.
Choose real preimages \(f_u,g_u\) of \(u,iu\). Then
\(\gamma(f_u)=a^*(u)+a(u)\), \(\gamma(g_u)=ia^*(u)-ia(u)\), and
\[
 N_u=\tfrac12(I+i\gamma(f_u)\gamma(g_u)).
\]
Approximate these real coefficients in \(L^2\) by compactly supported real
ones. CAR norm continuity and the selfadjoint expression
\(\tfrac12I+\tfrac i4[\gamma(f),\gamma(g)]\) give a compact even \(A\) with
\(\|A-N_u\|<\theta/4\). Its expectations in the two states differ by more than
\(\theta/2\). The actual ordinary-cell \(A_c\) tends to \(A\) in the current
carrier by C21. Thus (17) alone does not select a unique limit even in the
concrete physical observable class covered by (22).

### 10.2 Other scope tests

* **The interacting and free energy budgets differ.** A scalar local even
  potential \(V=-aI\), \(a>0\), allows a state with positive free energy at
  most \(a\) to have interacting energy at most zero. Therefore a ceiling
  \(M=0\) does not imply free energy at most \(M\). The exact valid conclusions
  are (18) and (20).

* **Mean energy is not trace-norm compactness.** Take orthonormal low packets
  \(u_j\) in one fixed bounded momentum interval. Their one-particle densities
  have uniformly bounded energy, are pairwise at trace distance \(2\), and
  converge on CAR to the vacuum because \(u_j\rightharpoonup0\).
  CAR convergence here follows first for finite polynomials from their
  creation/annihilation matrix elements, then for all CAR by norm density.
  It is not convergence of these densities in trace norm. Nor is an arbitrary
  \(B(\mathcal F_L)\) weak-* cluster functional forced to be that normal vacuum
  state: the one-particle sector projection has expectation \(1\) throughout
  and expectation \(0\) in the vacuum. Since a normal extension of the full CAR
  limit is unique, such a full bounded-operator cluster functional is not
  normal.

* **Even-sector support can escape.** Choose a fixed \(u\) and an orthonormal
  sequence \(w_j\perp u\) in a bounded momentum interval. The even two-particle
  states \(u\wedge w_j\) have bounded actual energy for all sufficiently small
  spacings and converge on CAR to the odd one-particle state \(u\). Polynomial
  matrix elements again give this by \(w_j\rightharpoonup0\).
  The limit is parity invariant but is not supported in the even Fock sector.
  This is why (19) targets full Fock. Uniqueness of a normal extension of a
  full CAR state is not an assertion that even physical tests alone determine
  an unrestricted parity-coherent full-CAR state.

* **An energy-zero initial ground state does not control arbitrary moving
  high observables.** At \(V=0\), take two orthonormal high-band packets with
  fixed bounded current momentum support. Their energies are
  \(2v/c+O(c)\) uniformly on that support. A bounded even pair-creation plus
  pair-annihilation observable has a vacuum two-time correlation with phase
  frequency \(4v/c+O(c)\). At a fixed nonzero time, suitable spacing subsequences
  therefore give different phases. The initial state is the exact
  energy-zero vacuum. This family fails the low ordinary-cell comparison
  (7); it is not a counterexample to (22) or (49). It is a counterexample to
  dropping their observable hypothesis.

* **The high CAR norm persists.** For any normalized actual high packet,
  \(a^*(h)a(h)\) is a projection of operator norm \(1\) at every spacing.
  The small high occupation in (23) and compressed-resolvent convergence in
  (35) do not shrink that equal-time algebra in \(C^*\) norm.

* **The mass-gap hypothesis has content.** In the separate abstract example
  with one-particle orthonormal modes of energies \(e_j=2^{-j}\), the Fock state
  filling the first \(n\) modes has mean energy \(<1\). Its CAR limit fills
  every mode and is not normal in vacuum Fock: the finite products of the first
  \(k\) occupation projections converge strongly to zero in that Fock space,
  while the limiting state assigns each product value \(1\). This shows why
  a lower particle-energy bound is used in the pinned normality lemma. It is
  not a classification of all gapless systems.

The endpoint \(K=m/2\) and larger interactions lie outside the sufficient
smallness proof (40)-(42), not in a proved impossibility region. A larger
potential with a separately established isolated simple ground may permit a
different argument. Rough-cell domain failure (30) is a concrete failure of
domain preservation for that example, not a failure of bounded-perturbation
dynamics or of the ordinary-cell convergence theorem.

Nothing here establishes an extensive interacting bulk limit, interacting
three-dimensional field theory, scattering, current conservation, boost or
Lorentz covariance of the perturbation, uniqueness of all algebraic ground
states, a universal rate for arbitrary \(L^2\) cells, or a physical rule choosing
the state, coupling, or potential. These are positive conditional results with
specified boundaries, not an exhaustive negative route classification. No
N1-N8 packet completion, five-route exhaustion, or global no-go claim is made.

## 11. Exact finite-algebra formal scope

The full `BOUNDED_INTERACTION_FORMAL_SCOPE_REVIEW.md` was read before this
assembly. It reports a successful Lean compilation of the supplied normalized
finite-algebra identity and substantive wrong-sign and missing-factor negative
controls; it also preserves an earlier import failure. This synthesis has not
rerun that compiler or inspected it as an analytic proof pipeline. The raw
identity source reported there is `CliffordInteraction.lean`, SHA-256
`beff44ab9f6bb88fcc0acf38a36be508bfbf03bd8790a005b91ae9135d4e1a54`.

The reported theorem has a unital complex-algebra type, normalized assumption
\(x^2=1\), and relations
\[
 yx=-xy,\quad zx=-xz,\quad tx=-xt,\quad ux=-xu,\quad
 uy=-yu,\quad uz=-zu,\quad ut=-tu.
\]
With \(P_4=xyzt\), \(Q_2=xu\), \(T_4=yztu\), these give
\[
 P_4Q_2=-T_4,\qquad Q_2P_4=T_4,\qquad
 i[(\lambda P_4)(iQ_2)-(iQ_2)(\lambda P_4)]=2\lambda T_4.                    \tag{51}
\]
The algebraic parameter can be complex; the selfadjoint physical witness in
(24) uses real \(\lambda\). The normalized hand computation (25) is an
application of these relations.

No star operation, norm, positivity, grading, faithfulness, nonzero witness,
locality, Fock construction, unbounded domain, semigroup, resolvent, or limiting
operation appears in that generic formal claim. Indeed \(y=z=t=u=0\) satisfies
the displayed relations and makes \(T_4=0\), so the identity by itself does not
prove a nonzero nonquadratic interaction. Those hypotheses and conclusions
come from the separate Clifford/Fock arguments in section 6.1.

In particular \(x=\Gamma_{1,c}\) in the unnormalized cell construction has
\(x^2=n_{1,c}^2I\), not \(I\). The reported normalized theorem cannot be applied
to it without rescaling or a different lemma. Its correct unnormalized
hand-derived expression is (27), including \(n_{1,c}^2\). No analytic result in
sections 3-10 is claimed as Lean verified, and no formal scope is promoted by
the number of source checks.

## 12. Exact sources, composition, and remaining review

The exact frozen source inputs are below. Full SHA-256 values, original paths,
byte counts, snapshots, read coverage, and exposure order are also recorded in
`bounded_interaction_ground_synthesis/INPUT_MANIFEST.json`. Every input body
is preserved unchanged.

| Source | SHA-256 | Role in this assembly |
|---|---|---|
| `BOUNDED_LOCAL_INTERACTION_ROOT_PROBE.md` | `7d9509a4d2c4b3fb956fd8e0379c39c3b24b245c271b239bed3ea49e1f50a22c` | Cocycle, exact energy passage, local witness |
| `BOUNDED_LOCAL_INTERACTION_INDEPENDENT.md` | `66356c203e8df633f303c2dfa552e6390aabbe1a1b9decdf00d00853259470f6` | Independent-before-comparison reconstruction, rough-domain example, scope tests |
| `BOUNDED_LOCAL_INTERACTION_CROSSCHECK.md` | `fd7869b5a41da4dadfc1bdd025e2f5d0c83d2ede2f6bd17264af57ef1854148c` | Source-exposed comparison and normalization/domain precision |
| `BOUNDED_INTERACTION_FORMAL_SCOPE_REVIEW.md` | `5cb275ecd82ea246a18af156e8192baa65dc54d2909aa69c6a79eeee28a11937` | Exact finite-algebra formal boundary |
| `GAPPED_GROUND_SELECTION_ROOT_PROBE.md` | `9716960392a6fa3b9465c2600bb8bb4a722fcbb8d1b1e7603bb8c8e35c28574f` | Compressed resolvents, gap, ground and excess-energy bounds |
| `GAPPED_GROUND_SELECTION_INDEPENDENT.md` | `47995ff099e6985fa0f73fa4cccf46faa99779aaec1bae9b226dc7b546d8226e` | Independent-before-comparison reconstruction, simpler low-block bound, fixed-cap example |
| `GAPPED_GROUND_SELECTION_CROSSCHECK.md` | `5f6589a2712e6cc06ed380ee4cc3db64152814abe06ece9eb258d1981d9b9b73` | Actual-spacing, projection, normalization, and constant precision |
| `ENERGY_TRANSFER_CORRELATION_SYNTHESIS.md` | `d63214a0d6365e1ae339f63caad67526bdd942130f76b064b13c2b7b2365b49c` | Explicit provisional dependency for full normal-CAR compactness |

The canonical parent identities are:

* [Current: actual current carrier, dispersions, and ordinary-cell limits](CURRENT_PRESERVING_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md),
  repository `docs/CURRENT_PRESERVING_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md`,
  SHA-256 `763082a6faa8bea3f6be74ddc7ee81bf288c00740085804e62f701a1576283ff`.
* [Concrete: full-spin Fock realization, irreducibility, and vacuum gap](CONCRETE_GAPPED_CHAIN_BOUNDED_THEOREM_NOTE_2026-10-12.md),
  repository `docs/CONCRETE_GAPPED_CHAIN_BOUNDED_THEOREM_NOTE_2026-10-12.md`,
  SHA-256 `2311c445bffc809d3387089c0feb48892f15f535d889121664dabe49fa146b05`.
* [Local: real fields, ordinary compact cells, and physical even-spin words](LOCAL_EVEN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-10-12.md),
  repository `docs/LOCAL_EVEN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-10-12.md`,
  SHA-256 `b5a8394a9d8c17bb9559597a68b061ad3872201ebf9793bd5c9f10b15ac2c6aa`.

The load-bearing [normality dependency](ENERGY_TRANSFER_CORRELATION_BOUNDED_THEOREM_NOTE_2026-10-12.md)
is a frozen proposed conditional source, not a required live file on main.
Its completed exact-source review, `ENERGY_TRANSFER_CORRELATION_SYNTHESIS_REVIEW.md`,
has SHA-256 `009043c543e809e4a19483bdc3d2932e61ff92170f1f76428cf8e851e3c48e57`;
the root acceptance record `SYNTHESIS_FINAL_REVIEW_ROOT_ACCEPTANCE.json`
has SHA-256 `f322d9262724208ce26eea6f181e81eefef73cbbf162fdf3eb1af278ec71895b`.
Those records concern that exact earlier source, not the present assembly.
The completed review artifact and receipt were recovered after stream failures;
its completion is established by those saved exact files, not inferred from a
missing final message. The finite-energy PR9499 proposal is provenance of the
earlier lane only, not an additional mathematical authority required here.
The current parent's `open_gate` disposition is not closed by this source.

Exposure chronology is explicit. This author had already authored/read the
frozen correlation synthesis and its exact-source review. For this task the
complete bounded-interaction root and independent cores, their crosscheck,
the formal-scope review, and both complete ground cores were read before
assembly. The necessary Concrete representation/gap passage was refreshed at
the unchanged parent bytes. Once root supplied the sealed ground-crosscheck
identity, that complete comparison was read before the final source was
written and frozen. The actual-spacing smallness, quartic norm factors, three
projection roles, and \(0.455\) versus \(0.5\) low-block distinction above
incorporate its precision items. Neither comparison reported a
theorem-invalidating finding in its stated scope.

The two independently written cores in each pair preceded their mutual
comparison as documented in their own records. They nevertheless share the
supplied model, parent arguments and selected model family. The current
assembly is explicitly source exposed and is not another independent check.
The normality dependency remains visible; the ground proof is separate from
it. The bounded interaction, energy budget and vanishing-excess preparation
are new conditional hypotheses, not new framework axioms or consequences of
the realized-state primitive.

The final source and an exact input/exposure manifest are the deliverable.
The assembled proof still requires its own exact-source review and root
acceptance before any publication packaging. This task changes no original
proof, editable prompt, campaign checkpoint, repository source, audit file,
Git state, or frozen correlation publication package. Deterministic hashes
and source inventories establish identity only; there is no new mathematical
runner, compiler execution, retained-status claim, or audit verdict.


## Publication dependencies, representation and scope

The direct parents are the [correlation theorem](ENERGY_TRANSFER_CORRELATION_BOUNDED_THEOREM_NOTE_2026-10-12.md),
[Current](CURRENT_PRESERVING_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md),
[Concrete](CONCRETE_GAPPED_CHAIN_BOUNDED_THEOREM_NOTE_2026-10-12.md), and
[Local Even](LOCAL_EVEN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-10-12.md).
Correlation supplies the full-CAR normal finite-energy subsequence lemma;
Current supplies the actual two branches, chosen carrier and C21/C25;
Concrete supplies the positive full spin-GNS Fock dynamics and vacuum; Local
supplies CAR normalization and the ordinary-cell/even-spin interpretation.

The correlation note is the OPEN proposal PR9500 at the stacked base
3679df3c7901b4660f5d9e9d69023e2e82772a83, not main authority. Its exact canonical
bytes and original synthesis/review are archived here. The other three parent
bodies match main 516cb69d8487ff04f8a48e065d3dcbe71d7dd237. Current remains
open_gate. Root must review the cumulative stack before any later main landing.

The cited canonical correlation note has wrapper hash
`60be3444c7e9e60090617944733f6c84dbd9184e3ca043d90bc71203ac2e1843`
and contains the exact frozen mathematical core from original source
`d63214a0d6365e1ae339f63caad67526bdd942130f76b064b13c2b7b2365b49c`.
Relocating its original source link does not enlarge the original review scope.

The two analytic regimes remain separate. Arbitrary uniformly bounded total
selfadjoint even interactions allow a bounded cocycle and actual-energy-controlled
subsequences under the stated comparison assumptions. They do not supply unique
state selection. The small-total-norm regime K<m/2 gives the stated isolated
ground and all-spacing limit only for spacings satisfying the theorem's
smallness premise, together with actual excess energy tending to zero.
A fixed positive energy cap is insufficient for that selector. No extensive
interaction or autonomous relaxation conclusion is supplied.

Full unital observable/potential extensions, Fock-band projections,
high-vacuum embeddings, rank-one ground projections, and zero-extended compressed
resolvents have their separate meanings in the body. The kernels of compressed
resolvents are not physical zero-energy sectors. Parity invariance is distinct
from fixed even-particle-sector support. The low-block constants c/(2v) and
sqrt((sqrt(2)-1)/2)c/v are distinct valid estimates; the former is simpler,
not stronger. The global c/v bound is the same.

The rough ordinary-cell example keeps the missing operator/form-domain
regularity visible; no potential domain-invariance premise has been inserted.
The normalized finite Clifford identity is distinct from the unnormalized
cell factor n_1,c squared. The nonquadratic witness requires the concrete
faithful finite CAR representation and its stated normalization, beyond the
abstract ring identity.

## Later completed finite formal-scope record

Two different historical Lean artifacts are carried with their complete source,
available inner/outer execution records, exact compiler/mathlib identities,
and scope reviews. Neither was executed during this package preparation.

The Clifford source proves the finite normalized algebraic commutator under its
displayed square and anticommutation relations. The earlier missing-import
failure and its narrow import-path repair remain archived. Its two altered
proof attempts failed; they are not proved negations or literal counterexamples.
No analytic norm, faithfulness, domain, continuum or ground theorem follows
from that abstract identity alone.

The separately completed compressed-resolvent review, SHA-256
`5ba536c715eb6c3069c4e2937f288eee2ce0cbbce87621065055804318cb65cb`,
and root acceptance support only the saved noncommutative ring identity with
one stated left-inverse and one stated right-inverse premise. The two rational
counterexamples are actual proved conjunctions refuting the reversed sign
and omitted term. They do not test all possible factor-order changes.
The original interrupted review stub is retained as an incomplete attempt;
the later complete review is separately identified. Historical seals marked
pending are not silently rewritten.

Existence of bounded inverses, Neumann estimates, compressed physical subspaces,
gap projections and all unbounded analytic conclusions remain ordinary
mathematical arguments in this note. No analytic Lean or retained certificate
is claimed. Reconstruction tools merely identify these saved records.

## Publication and narrowing boundary

Publication metadata and this wrapper are added around the original source.
Only four authorized Markdown targets are relocated inside the body; labels
and all mathematics are preserved. The exact original and
publication diff are reconstructable. The [No-Go Discipline Gate](../.claude/science/physics-loops/toe-bounded-interactions-20261012/NO_GO_DISCIPLINE_CHECKLIST.md)
records N1/N5 as pending. The literal counterexamples constrain precise
implications; they do not establish five-route exhaustion or a global
obstruction. There is no new axiom, empirical prediction, audit verdict,
retained promotion or proof supplied by the identity runner.
