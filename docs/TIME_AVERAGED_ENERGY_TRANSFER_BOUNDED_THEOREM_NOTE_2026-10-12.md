---
claim_id: time_averaged_energy_transfer_bounded_theorem_note_2026-10-12
claim_type: bounded_theorem
claim_scope: "Conditional BV time-kernel two-sided actual free-energy form transfer, finite-word high-vacuum compression and scoped continuum limits under bounded autonomous interactions."
upstream_dependencies:
  - energy_transfer_correlation_bounded_theorem_note_2026-10-12
  - bounded_interaction_ground_bounded_theorem_note_2026-10-12
  - current_preserving_refinement_bounded_theorem_note_2026-10-12
  - local_even_continuum_bounded_theorem_note_2026-10-12
runner: scripts/time_averaged_energy_transfer_identity_2026_10_12.py
artifact_role: theorem
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: partially_closes
target_claim_id: null
target_blocker_text: "Physical inputs, provisional parent claims and stated operator-domain and convergence hypotheses remain supplied premises."
source_of_blocker_text: frontier_question
next_trace_action: "Root review of this exact publication assembly, bounded source integration, cumulative stack review and later applicable independent audit."
conditional_surface_status: "Supplied two-band chain and identifications; Current open_gate; stacked PR9502 and inherited PR9500 provisional."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Ordinary conditional analytic theorem with same-family source checks and literal counterexamples; identity tools execute no mathematics."
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

**Type:** bounded_theorem

Status: conditional-support

Primary runner: [source identity and reconstruction only](../scripts/time_averaged_energy_transfer_identity_2026_10_12.py).
It executes zero mathematical predicates, scientific mutations or formal checks.
Source identities and reconstruction do not establish mathematical truth.

**Publication chronology.** The complete independent 696-line source below is
`04eef4960b18d6b0e4a7f81852ddceea7fc081c855360bf613aaf9124e141984`.
It was frozen before exposure to the separately sealed root time-smearing
candidate. The later complete 410-line source-exposed comparison is
`46533eb1f57e866f4b3d7db23c1e41d69eac566ce16cf0eaaa489f58fccfc905`.
Root read both complete sources and their comparison. The comparison identifies
no required mathematical repair at their stated scope and distinguishes the
independent extensions from the root candidate. Both original cores and their
exposure records remain archived unchanged. The source's earlier pending labels
are preserved as historical chronology, not rewritten as current uncertainty
about whether that comparison was completed.

The derivations share the same model family and allowed premises. The comparison
is ordinary source-exposed analytic corroboration, not model-diverse, formal or
retained verification. No result from another later candidate is incorporated.
Every byte of the frozen source below is preserved. No Markdown-target
relocation was necessary. This wrapper adds metadata and dependency links only.

Final publication wrapper/program/packet review and root execution acceptance
remain pending in this source preparation. The two-note publication package
does not make the response theorem a premise of this averaging theorem.

# Finite temporal averaging and actual free-energy transfer

Status: independently derived conditional mathematical core, 2026-10-12.
This is an ordinary argument with shared premises and the inherited model
family, not an audit, formal verification, retained claim or new physical axiom.
The separate root time-smearing candidate and its outcome have not been read.

A compactly supported bounded-variation time kernel is sufficient. In particular,
a finite rectangular average works, provided its endpoint jumps are retained.
Averaging a bounded observable under an autonomous Hamiltonian \(H+V\), with
\(H\ge0\) selfadjoint and bounded selfadjoint \(V\), gives both adjoint
free-energy form estimates with explicit constants. No spatial smoothness,
bounded \([H,V]\), or domain invariance of \(V\) or of the original observable
is required. Applied to the supplied actual high gap, this gives an \(O(c)\)
scalar high-vacuum compression estimate at every fixed nonzero averaging width.
The sector estimate is uniform in all observation centers. Continuum comparison
has its own compact-window and state-convergence premises.

The fixed-width qualifier matters. A fixed rough ordinary-cell target prevents
uniform fixed-reference-energy form constants in a point-window limit.
There is nevertheless a sufficient joint shrinking regime, including
\(c/\varepsilon(c)\to0\) for a fixed finite word with a common scaled kernel.
Neither that condition's necessity for fixed ordinary inputs nor a universal
point-observation obstruction is asserted.

## 1. Allowed premises, carrier and meaning of the claim

The shared mathematical sources are exactly:

- `ENERGY_TRANSFER_CORRELATION_SYNTHESIS.md`, SHA-256
  `d63214a0d6365e1ae339f63caad67526bdd942130f76b064b13c2b7b2365b49c`,
  especially its actual-gap, two-sided form and bounded-commutator arguments.
- `BOUNDED_INTERACTION_GROUND_SYNTHESIS.md`, SHA-256
  `b8bcba769100bf819885937d850a7bff8543e4233c1df3cf65f68372552160e9`,
  especially its bounded cocycle, common domains, ordinary-cell comparison
  and rough-domain example.
- The unchanged canonical Current and Local sources, with respective hashes
  `763082a6faa8bea3f6be74ddc7ee81bf288c00740085804e62f701a1576283ff` and
  `b5a8394a9d8c17bb9559597a68b061ad3872201ebf9793bd5c9f10b15ac2c6aa`.
  Current C21/C24/C25 and Local sections 3 and 6 are the specific local premises.
  Local L10 is a generator estimate; the even-spin identification is L23-L24.

These remain supplied conditional constructions. Current is open_gate.
The correlation and interaction syntheses are proposed source dependencies;
their existence is not main or audit authority. The present work derives the
time-averaging step and its consequences, not the chosen dynamics, vacuum,
physical time convention or observation rule.

Fix \(m,v>0\). On the actual physical finite-spacing Fock space \(\mathcal F_c\),
the transported positive free Hamiltonian, with no vacuum subtraction, is
\[
 H_c=d\Gamma(e_{c,L}\oplus e_{c,H}),\quad I_c=(-1/c,1/c),\quad
 w_c(p)=\sqrt{1-c^2p^2},
\]
\[
 e_{c,L}(p)^2=m^2+\frac{2v^2p^2}{1+w_c(p)},\qquad
 e_{c,H}(p)^2=m^2+\frac{2v^2}{c^2}(1+w_c(p)).
 \tag{T1}
\]
Let \(P\) be the no-high-particle projection on that space and \(Q=1-P\).
The actual form inequality and commutation are
\[
 H_c\ge\Lambda_c N_H\ge\Lambda_c Q,\quad
 \Lambda_c=\sqrt{m^2+2v^2/c^2},\quad [H_c,P]=0.                 \tag{T2}
\]
At fixed \(c\), the one-particle energies are bounded by
\(\mathcal E_c=\sqrt{m^2+4v^2/c^2}\); the many-body Hamiltonian is still
unbounded. On the full target low Fock space,
\(H_0=d\Gamma(E)\), \(E(p)=\sqrt{m^2+v^2p^2}\).

The interaction is autonomous:
\[
 L_c=H_c+V_c,\qquad V_c=V_c^*,\quad \|V_c\|\le K<\infty.       \tag{T3}
\]
For physical observations and continuum comparison, \(V_c\) and the observable
blocks are even CAR elements with the in-band unital placement of the shared
source. The abstract domain estimate itself holds for every bounded block
on the actual Hilbert space. No smallness \(K<m/2\) is needed here.

The following distinctions are retained. \(P\) is not an interacting ground
projection and need not commute with \(L_c\). The common Fock-band projection
\(\Pi_c\), the low-band Fock projection \(q_c\), and \(P\) are distinct.
The gap in T2 is used only for the actual \(H_c\) on \(\mathcal F_c\), never
for a common extension with zero-energy outside-band modes.
Unital CAR extensions are used for operator-norm comparison; densities and
physical corners can be extended by zero. Their identities are different.

## 2. Kernels and the averaged operators

Let \(k\in L^1(\mathbb R)\) be compactly supported and of bounded variation
on the whole real line. This means its distributional derivative \(Dk\)
is a finite complex Borel measure. Write
\[
 a_k=\|k\|_1,\qquad q_k=|Dk|(\mathbb R).
 \tag{T4}
\]
The total variation is that of the zero-extended kernel: endpoint jumps count.
A sufficient special case is \(k\in W^{1,1}(\mathbb R)\) of compact support,
where \(q_k=\|k'\|_1\). For a piecewise \(W^{1,1}\) kernel on an interval,
the interior derivative and all jumps, including the endpoints, must be
included in \(q_k\).

For a selfadjoint generator \(L\) and \(B\in\mathcal B(\mathcal H)\), put
\[
 \beta_t(B)=e^{itL}Be^{-itL},\qquad
 A_k(t)=\int_{\mathbb R} k(s)\beta_{t+s}(B)\,ds,\qquad
 \|B\|\le b.                                                \tag{T5}
\]
For a general bounded \(B\), the integral is a strong vector integral:
for each \(x\), \(s\mapsto\beta_s(B)x\) is continuous and bounded, and its
Bochner integral defines a bounded linear operator of norm at most \(ba_k\).
This does not assume norm continuity of the original \(B\)-orbit.
Its adjoint is the strong integral with \(\bar k\) and \(B^*\).

In the physical CAR class the interacting flow is point-norm continuous,
so T5 is also a norm Bochner integral in the even CAR algebra. This follows
from the bounded cocycle recalled in section 7. If \(B=B^*\) and \(k\) is
real, \(A_k(t)=A_k(t)^*\). A nonnegative kernel of integral one is a
contractive temporal average; complex kernels and nonsymmetric words are
also allowed in the estimates.

The integrand uses actual physical time \(t+s\). No high-frequency phase
subtraction or time rescaling of the supplied dynamics has been made.
Although the initial ordinary-cell observable has finite spatial support,
its time average is only asserted to be an even CAR/quasilocal observable.
No exact fixed spatial support or new propagation-speed bound is asserted.

## 3. A domain-valid bounded commutator from a BV kernel

Here \(\langle u,v\rangle\) is linear in the second variable. For \(u,x\in
\mathcal D(L)\), the scalar function
\[
 F_{u,x}(s)=\langle e^{-isL}u,B e^{-isL}x\rangle
          =\langle u,\beta_s(B)x\rangle
\]
is continuously differentiable, even though \(Bx\) need not lie in
\(\mathcal D(L)\). Differentiation acts only on the two domain vectors:
\[
 F_{u,x}'(s)=i\{\langle Lu,\beta_s(B)x\rangle
                        -\langle u,\beta_s(B)Lx\rangle\}.     \tag{T6}
\]
Its derivative is bounded by
\(b(\|Lu\|\|x\|+\|u\|\|Lx\|)\). BV integration by parts, using a compact
cutoff equal to one on the kernel support, gives
\(\int kF'=-\int F\,d(Dk)\).
This identity for compactly supported \(C^1\) tests follows from the
distributional identity by uniform \(C^1\) approximation on the compact support.

Define a second bounded strong integral
\[
 C_k=i\int_{\mathbb R}\beta_s(B)\,d(Dk)(s),\qquad
 \|C_k\|\le bq_k.                                           \tag{T7}
\]
A finite complex measure is handled by its polar density with respect to
its total variation; vector continuity and boundedness ensure integrability.
Equations T6-T7 imply, for every \(u\in\mathcal D(L)\),
\[
 \langle Lu,A_k(0)x\rangle
       =\langle u,A_k(0)Lx+C_kx\rangle.                       \tag{T8}
\]
The adjoint-domain characterization of the selfadjoint \(L\) now proves
\[
 A_k(0)\mathcal D(L)\subset\mathcal D(L),\qquad
 [L,A_k(0)]x=C_kx\quad(x\in\mathcal D(L)).                     \tag{T9}
\]
Thus the operator-domain conclusion is obtained from a weak identity;
it is not inserted as a differentiability premise.

Apply the same argument to \(B^*,\bar k\). It proves the domain assertion
for \(A_k(0)^*\), with commutator \(-C_k^*\) and the same bound.
Since the unitary group preserves \(\mathcal D(L)\), conjugating T9 gives
\[
 A_k(t),A_k(t)^*:\mathcal D(L)\longrightarrow\mathcal D(L),
 \qquad \|[L,A_k(t)]\|,\ \|[L,A_k(t)^*]\|\le bq_k              \tag{T10}
\]
for all real \(t\).

For clarity, \(W^{1,1}\) supplies a further norm-differentiability proof even
for arbitrary bounded \(B\):
\[
 \beta_h(A_k(0))
  =\int k(s-h)\beta_s(B)\,ds,\qquad
 \frac{\beta_h(A_k(0))-A_k(0)}h
       \longrightarrow-\int k'(s)\beta_s(B)\,ds
\]
in norm, because difference quotients converge in \(L^1\).
For a general BV kernel, T8-T10 do not rely on this \(L^1\)-derivative
assertion, which would fail for a jump. In the point-norm continuous CAR
class, the measure integral of the norm-continuous orbit also gives a
norm-continuous commutator orbit and hence norm differentiability of the
averaged orbit: on the dense domain, differentiate the conjugation using T9
and integrate \(i\beta_s(C_k)\); density identifies that integral on all vectors,
and its norm continuity gives the norm derivative. The weak-domain proof
covers both cases.

For the normalized rectangular average
\[
 k_\varepsilon(s)=\frac1{2\varepsilon}
                    \mathbf1_{[-\varepsilon,\varepsilon]}(s),
 \quad a_k=1,\quad q_k=\varepsilon^{-1},
\]
the exact commutator is
\[
 [L,A_{k_\varepsilon}(t)]
   =\frac{i}{2\varepsilon}
           \{\beta_{t-\varepsilon}(B)-\beta_{t+\varepsilon}(B)\}. \tag{T11}
\]
Treating the interior derivative as zero and dropping these endpoints
would give an incorrect conclusion.

## 4. Return to the actual free operator and its form domain

Let \(H\ge0\) be selfadjoint and \(V=V^*\) bounded, \(\|V\|\le K\).
The operator \(L=H+V\) on \(\mathcal D(H)\) is selfadjoint. For completeness,
bounded perturbation preserves closedness and symmetry; for \(\eta>K\),
\[
 L\mp i\eta=\{I+V(H\mp i\eta)^{-1}\}(H\mp i\eta)
\]
has surjective range by the convergent Neumann inverse. The two range
conditions establish selfadjointness. Therefore
\(\mathcal D(L)=\mathcal D(H)\).

The closed form of \(L+K+\mu\), \(\mu>0\), has domain
\(\mathcal D(H^{1/2})\) and satisfies
\[
 H+\mu\ \le L+K+\mu\ \le H+\mu+2K
                 \le(1+2K/\mu)(H+\mu)                       \tag{T12}
\]
as forms. This follows by adding the bounded \(V\)-form to the closed free
form; the displayed equivalent norms prove closedness, and its associated
operator agrees with the selfadjoint \(L+K+\mu\).
Neither this argument nor equality of domains asserts that \(V\) maps either
domain into itself.

By T10, \(A=A_k(t)\) and \(A^*\) preserve \(\mathcal D(H)\). On that domain,
\[
 [H,A]=[L,A]-[V,A],\qquad
 \|[H,A]\|,\ \|[H,A^*]\|
       \le d_k:=b(q_k+2Ka_k),\qquad \|A\|\le a:=ba_k.         \tag{T13}
\]
All terms involving \(V\) here are bounded products. This requires no action
of \(H\) on \(Vx\).

Here is the form step, including its closure justification. Put \(F=H+\mu\)
and let \(C=[H,A]\) be the bounded extension. For \(R_s=(F+s)^{-1}\),
domain preservation and multiplication of the resolvent equation give
\[
 [R_s,A]=-R_sCR_s.
\]
For \(x\in\mathcal D(F)\), the spectral integral
\[
 F^{1/2}x=\frac1\pi\int_0^\infty s^{-1/2}F(F+s)^{-1}x\,ds
\]
converges strongly: use \(s^{-1/2}\|x\|\) near zero and
\(s^{-3/2}\|Fx\|\) at infinity. Subtract \(A\) times the formula for \(x\)
from the formula for \(Ax\), using \(F R_s=I-sR_s\), to obtain
\[
 [F^{1/2},A]
  =\frac1\pi\int_0^\infty s^{1/2}R_sCR_s\,ds,\qquad
 \|[F^{1/2},A]\|\le\frac{\|C\|}{2\sqrt\mu}.                  \tag{T14}
\]
The integral converges in operator norm since
\(\pi^{-1}\int_0^\infty s^{1/2}(\mu+s)^{-2}ds=(2\sqrt\mu)^{-1}\).
The scalar integral follows by \(s=\mu u^2\) and then \(u=\tan\theta\).

For \(x\in\mathcal D(F^{1/2})\), take spectral cutoffs \(x_N\in\mathcal D(F)\)
converging in the form norm. In
\[
 F^{1/2}Ax_N=A F^{1/2}x_N+[F^{1/2},A]x_N
\]
the right side converges and \(Ax_N\to Ax\). Closedness of \(F^{1/2}\)
proves that \(Ax\) lies in its domain and extends T14. Repeat for \(A^*\).
The resulting two-sided actual free-energy estimate is
\[
 \boxed{\ 
 \|F^{1/2}A_k(t)F^{-1/2}\|,\quad
 \|F^{1/2}A_k(t)^*F^{-1/2}\|
 \le \kappa_k(\mu):=
 b\left[\left(1+\frac K\mu\right)a_k+\frac{q_k}{2\mu}\right].\ } \tag{T15}
\]
Each expression denotes its bounded extension with the just-proved
form-domain inclusion. The bound is independent of the time center \(t\),
the free spectral upper bound, and spacing. It therefore applies uniformly
to the actual \(H_c\), despite its diverging one-particle ceiling as \(c\to0\).
The identical statement holds for \(H_0,V_0\).

## 5. Finite words and quantitative high-vacuum compression

Fix \(n\ge1\), \(\|B_{j,c}\|\le b_j\), compact BV kernels \(k_j\), and
\(A_j=A_{k_j,c}(t_j)\) formed using \(L_c\). Write
\[
 a_j=b_j a_{k_j},\quad a=\prod_j a_j,\quad
 W_c=\prod_{j=1}^n A_j,\qquad
 C_c=P A_1 P A_2 P\cdots P A_n P.
\]
Times can be arbitrary real numbers in arbitrary product order.
Let \(\rho_c\) be a normal density with actual free form energy
\(\operatorname{Tr}\rho_c H_c\le M\). Set
\[
 \delta_c=\operatorname{Tr}\rho_c Q\le M/\Lambda_c,\quad
 \tau_c=P\rho_cP,\quad p_c=1-\delta_c,\quad
 \sigma_c=\tau_c/p_c\ \text{if }p_c>0.                       \tag{T16}
\]
These are high-vacuum compressions, not low partial traces.

For general forward/adjoint form constants \(\kappa_j^+,\kappa_j^-\),
the exact \(n+1\)-slot insertion identity is
\[
 W_c-C_c=\sum_{j=0}^n L_j Q R_j,\quad
 L_0=I,\quad L_j=P A_1P\cdots P A_j\ (j\ge1),\quad
 R_j=A_{j+1}\cdots A_n,\ R_n=I.                             \tag{T17}
\]
Here \(R_0=W_c\). \(P\) commutes with \(F_c=H_c+\mu\), so it contracts
the form norm, and
\(\|QF_c^{-1/2}\|\le(\Lambda_c+\mu)^{-1/2}\).

To justify the trace estimate for a merely finite-form-energy density,
diagonalize \(\rho_c=\sum_r\lambda_r|\psi_r\rangle\langle\psi_r|\).
Every positive-weight \(\psi_r\) has finite form energy and
\(\sum_r\lambda_r\|F_c^{1/2}\psi_r\|^2\le M+\mu\).
For each slot,
\[
 |\langle\psi_r,L_jQR_j\psi_r\rangle|
 =|\langle QL_j^*\psi_r,QR_j\psi_r\rangle|
 \le\frac{\|F_c^{1/2}\psi_r\|^2}{\Lambda_c+\mu}
       \prod_{i\le j}\kappa_i^-\prod_{i>j}\kappa_i^+ .
\]
Summing positive weights and the finite slots is legitimate; all original
trace products contain only bounded operators. It proves
\[
 \left|\operatorname{Tr}\rho_cW_c-
        \operatorname{Tr}\tau_c(C_c|_{P\mathcal F_c})\right|
 \le S_c(\mu):=\frac{M+\mu}{\Lambda_c+\mu}
       \sum_{j=0}^n\prod_{i\le j}\kappa_i^-\prod_{i>j}\kappa_i^+ .
 \tag{T18}
\]
Both adjoints are essential in the prefix estimate. With T15 this becomes
\[
 S_c(\mu)\le
 \frac{(n+1)(M+\mu)}{\Lambda_c+\mu}
       \prod_{j=1}^n b_j\left[\left(1+\frac K\mu\right)a_{k_j}
                                      +\frac{q_{k_j}}{2\mu}\right]. \tag{T19}
\]
For the normalized state,
\[
 \left|\operatorname{Tr}\rho_cW_c-
        \operatorname{Tr}\sigma_c(C_c|_{P\mathcal F_c})\right|
       \le S_c(\mu)+a\,M/\Lambda_c.                         \tag{T20}
\]
The extra term is just \(a|1-p_c|\). A sufficient condition for \(p_c>0\)
is \(M<\Lambda_c\), automatically true at small spacing for fixed \(M\).

Fixed kernels, \(n,K,M,\mu,b_j\) give \(S_c=O(c)\), uniformly for all centers.
This is a scalar correlation/compression result, not smallness of the full
high CAR algebra in operator norm. Crucially, \(C_c\) contains compressions
of the actual interacting observables. Since \(P\) need not reduce \(L_c\),
it is not identified with an isolated low Hamiltonian evolution of
\(PB_{j,c}P\). Nor is \(PW_cP\) identified with \(C_c\).

If the density itself is shifted by an arbitrary interacting waiting time,
start with free cap \(M\). Conservation of the semibounded \(L_c\)-energy and
\(|\operatorname{Tr}\rho V_c|\le K\) give
\[
 \operatorname{Tr}\rho_c(w)H_c\le M+2K\qquad(w\in\mathbb R).   \tag{T21}
\]
This uses T12 and the spectral definition of the conserved form expectation;
it is not conservation of \(H_c,Q\) or \(N_H\). Thus T18-T20 also hold
uniformly in such a waiting time after replacing \(M\) by \(M+2K\).

## 6. Scaled windows and a useful choice of reference energy

For fixed nonzero compact BV \(\varphi_j\), define
\[
 k_{j,\varepsilon_j}(s)=\varepsilon_j^{-1}
                         \varphi_j(s/\varepsilon_j),\qquad
 a_{k_j}=\alpha_j:=\|\varphi_j\|_1,\quad
 q_{k_j}=q_j/\varepsilon_j,\quad q_j=|D\varphi_j|(\mathbb R).
 \tag{T22}
\]
The form constants at a fixed \(\mu\) need not remain bounded as
\(\varepsilon_j\downarrow0\). Nevertheless T18 is valid at any positive
reference energy, which can be chosen separately at each spacing.

If a factor is zero the word comparison is trivial. Otherwise \(\alpha_j>0\),
and a nonzero compactly supported BV \(L^1\) function has \(q_j>0\).
Set
\[
 D_{\boldsymbol\varepsilon}
       =K+\max_j\frac{q_j}{2\alpha_j\varepsilon_j}>0,\qquad
 \mu=D_{\boldsymbol\varepsilon}.
\]
Then T15 gives \(\kappa_j\le2b_j\alpha_j=2a_j\), and
\[
 \boxed{\quad
 S_c\le (n+1)2^n a\,
     \frac{M+D_{\boldsymbol\varepsilon}}
          {\Lambda_c+D_{\boldsymbol\varepsilon}}.\quad}      \tag{T23}
\]
T20 adds \(aM/\Lambda_c\) if normalization is used.
For fixed finite \(n,b_j,\varphi_j,K,M\), a sufficient joint condition is
\[
 c\max_j\varepsilon_j(c)^{-1}\longrightarrow0.               \tag{T24}
\]
For a common width this is \(c/\varepsilon(c)\to0\), even if the width
tends to zero. A simple bound follows from \(\Lambda_c\ge\sqrt2v/c\):
the right side of T23 is at most
\((n+1)2^n a\,c(M+D_{\boldsymbol\varepsilon})/(\sqrt2v)\).
The optimized-reference step avoids asserting that an artificially fixed
\(\mu\) is necessary for a joint estimate. It does not prove an optimal
constant, necessary window scale, or a rate for the complete continuum limit.

For the rectangular kernel in T11,
\(D_\varepsilon=K+1/(2\varepsilon)\). All expressions stay meaningful at
\(K=0\) and \(M=0\); averaging can transfer energy after an insertion even
when the initial state is the free vacuum.

## 7. Ordinary rough cells and compact-window continuum comparison

For the continuum statement use the unital common CAR carrier and precisely
the bounded-interaction source's hypotheses. Let \(\widehat V_c,V_0\) be
selfadjoint even in-band/low potentials, bounded by \(K\), and let
\(\widehat B_{j,c},B_{j,0}\) be separately even blocks, bounded by \(b_j\).
The low target acts tensor \(I_H\). Assume, for each finite \(R\),
\[
 \nu_{V,c}(R)=\sup_{|s|\le R}
       \|\alpha_{c,s}(\widehat V_c)-\alpha_{0,s}(V_0)\otimes I_H\|\to0,
\]
\[
 \nu_{j,c}(R)=\sup_{|s|\le R}
       \|\alpha_{c,s}(\widehat B_{j,c})-\alpha_{0,s}(B_{j,0})\otimes I_H\|\to0.
 \tag{T25}
\]
Only on this common comparison carrier may a block-diagonal free extension
outside the physical band be chosen. It is not used for T2 or T18.

Here is the relevant bounded comparison argument. The cocycle
\(Z_c(s)=e^{is\widehat L_c}e^{-is\widehat H_c}\) satisfies
\(Z_c'=iZ_c\alpha_{c,s}(\widehat V_c)\). The common-domain product
differentiation is first valid on \(\mathcal D(\widehat H_c)\);
its two unbounded terms cancel, leaving the bounded perturbation.
The norm integral equation has its unique unitary solution by convergent
iterated bounded integrals. Strong uniqueness identifies the two solutions,
and the integral solution lies in even CAR. Thus
\(\beta_{c,s}(B)=Z_c(s)\alpha_{c,s}(B)Z_c(s)^*\).
The right-generator difference identity gives
\[
 (Z_cZ_0^*)'=iZ_c(\alpha_c(V_c)-\alpha_0(V_0))Z_0^*,
 \qquad \|Z_c(s)-Z_0(s)\|\le |s|\nu_{V,c}(R)\quad(|s|\le R).
\]
Consequently
\[
 \eta_{j,c}(R):=\nu_{j,c}(R)+2R b_j\nu_{V,c}(R)
 \quad\text{bounds}\quad
 \sup_{|s|\le R}\|\beta_{c,s}(\widehat B_{j,c})
                   -\beta_{0,s}(B_{j,0})\otimes I_H\|.       \tag{T26}
\]
No exponential factor or free-energy regularity of \(V_c\) is used.

If \(\operatorname{supp}k_j\subset[-S_j,S_j]\), \(|t_j|\le T\), and
\(R=T+\max_j S_j\), integration and product telescoping give
\[
 \|\widehat A_{j,c}(t)-A_{j,0}(t)\otimes I_H\|
            \le a_{k_j}\eta_{j,c}(R),
\]
\[
 \sup_{\mathbf t\in[-T,T]^n}
 \left\|\prod_j\widehat A_{j,c}(t_j)
             -\prod_j A_{j,0}(t_j)\otimes I_H\right\|
 \le Z_c(T):=\sum_j a_{k_j}\eta_{j,c}(R)\prod_{\ell\ne j}a_\ell\to0.
 \tag{T27}
\]
The same constants bound the low high-vacuum conditional expectations,
because that expectation is contractive. It is not multiplicative;
one applies it separately to each factor, as in T18.

A concrete class satisfying T25 is fixed finite even *-polynomials in ordinary
cells of real compactly supported \(L^2\) fields:
\[
 (C_cf)_r=c^{-1/2}\int_{cr}^{c(r+1)}f(x)\,dx,\qquad \|C_cf\|\le\|f\|.
\]
Current C21/C25 give the coefficient convergence in norm uniformly on compact
times, without spatial differentiability of \(f\). The CAR field norm and
product telescoping promote it to T25. Potentials are separately chosen
selfadjoint; their bound is on the total polynomial, not per cell.
Local sections 3 and 6, L23-L24, give the finite-cell-hull even-spin
representatives and at most one-cell endpoint enlargement of the initial
supports. Norm limits and finitely many converging scalar coefficients are
also allowed. None of these ordinary-cell facts alone asserts a free-energy
form bound for the unsmeared block; T15 supplies it for the average.

## 8. States, compression versus partial trace, and time-window scope

Let \(\widehat\rho_c\) be the actual density embedded by zero in the common
full Fock space. The trace-one low partial trace
\(\lambda_c=\operatorname{Tr}_H\widehat\rho_c\) is different from T16's
unnormalized high-vacuum compression. For the low target word
\(W_0(\mathbf t)=\prod_j A_{j,0}(t_j)\), T27 gives the direct estimate
\[
 \left|\operatorname{Tr}\widehat\rho_c\widehat W_c(\mathbf t)
       -\operatorname{Tr}\rho_0 W_0(\mathbf t)\right|
 \le Z_c(T)+
   \sup_{\mathbf s\in[-T,T]^n}
       |\operatorname{Tr}(\lambda_c-\rho_0)W_0(\mathbf s)|.
 \tag{T28}
\]
This requires an explicit state-convergence premise. Trace-norm convergence
suffices with last term at most \(a\|\lambda_c-\rho_0\|_1\).
CAR state convergence also suffices for these fixed CAR words: point-norm
continuity makes the image of the fixed compact time cube norm compact,
and a finite norm net turns pointwise state convergence into uniform
convergence on it.

If instead the normalized T16 state, embedded in full low Fock, converges
to \(\rho_0\), the high-vacuum route gives
\[
 |\operatorname{Tr}\rho_c W_c-\operatorname{Tr}\rho_0W_0|
 \le S_c+aM/\Lambda_c+Z_c(T)+
   \sup_{\mathbf s\in[-T,T]^n}
        |\operatorname{Tr}(\sigma_c-\rho_0)W_0(\mathbf s)|.
 \tag{T29}
\]
For T29, compress each in-band unital factor by the high vacuum and identify
it with its unital low CAR conditional expectation. Its actual physical
restriction is the corresponding \(q_c\) corner. Since all finite-c factors
remain in-band, the corner expectation in \(\sigma_c\) equals the product
of those low factors. T27 bounds each difference from its target. No
replacement of a product's compression by the product of its compressions
is hidden in this step: that error is exactly T18.

For the ordinary-cell class T28 already proves qualitative convergence
without the new transfer estimate. T29 adds a separate quantitative
high-vacuum compression statement; it need not give a better total error.

If desired, the full-CAR normal-subsequence lemma in the pinned correlation
synthesis is an explicit provisional dependency: T2 and
\(H_c\ge H_0\otimes I_H\) give
\(\operatorname{Tr}\lambda_c H_0\le M\). That lemma supplies subsequences
converging on all low CAR to a normal full-Fock finite-energy density.
It supplies no trace-norm compactness or unique/all-sequence selector.
The normalized high-vacuum states have the same CAR subsequential limit:
purifying the compression gives
\(\|\widehat\rho_c-\widehat\sigma_c\|_1\le2\sqrt{\delta_c}\to0\);
apply this to bounded low tests. Parity invariance can pass, whereas fixed
even-particle-sector support need not. The target is full Fock.

The uniform-in-center sector estimate T19 is not an unlimited-time continuum
theorem. For centers or supports growing with \(c\), one needs explicitly
\(Z_c(T(c))\to0\) with the enlarged \(R(c)\), and convergence of the state
functionals on the resulting moving target words. Pointwise CAR convergence
alone supplies no such uniformity for a noncompact family.

For normalized scaled kernels with uniformly bounded \(L^1\) norms and
\(\varepsilon_j(c)\to0\), fixed ordinary inputs still have a qualitative
point-window limit. For fixed \(T\), T26 holds on a fixed slightly larger
interval, while uniform norm continuity of the target orbit gives
\[
 \sup_{|t|\le T}
 \left\|\int\varphi_j(u)\beta_{0,t+\varepsilon_j u}(B_{j,0})\,du
                         -\beta_{0,t}(B_{j,0})\right\|\to0.  \tag{T30}
\]
Here \(\int\varphi_j=1\); the integral of the absolute difference is bounded
by its compact-time continuity modulus times \(\|\varphi_j\|_1\).
T27 followed by T30 and the fixed instantaneous target word gives the
state/correlation conclusion on compact centers. No rate follows from C25
for arbitrary rough \(L^2\) data. In particular, an \(O(c)\) sector estimate
at fixed width is not an \(O(c)\) complete continuum correlation rate.

## 9. What cannot be uniform when the width tends to zero

### 9.1 A fixed rough ordinary input defeats uniform form constants

Use the permitted rough-cell example explicitly. Take
\(f=\mathbf1_{[0,1]}e_1\) and a nonzero smooth real \(g=g_1e_1\) supported
inside \((2,3)\). The target
\(B_0=i\gamma(f)\gamma(g)\) is bounded, selfadjoint and even. If
\(u=\sqrt2P_+\widehat f\), \(z=\sqrt2P_+\widehat g\), then
\[
 \|u(p)\|^2=\frac{1-\cos p}{\pi p^2},\quad
 \int E(p)\|u(p)\|^2dp=\infty,\quad z\ne0,\ z\in\mathcal D(E^{1/2}).
 \tag{T31}
\]
The divergence follows by fixed-width intervals where \(1-\cos p\) is
bounded below and \(E(p)\ge v|p|\). Subtracting the \(z\)-component from
\(u\) gives \(u'\perp z\) with \(u'\notin\mathcal D(E^{1/2})\).
For \(E_R=\min(E,R)\),
\[
 \langle u'\wedge z,d\Gamma(E_R)(u'\wedge z)\rangle
 =\|z\|^2\langle u',E_Ru'\rangle+
       \|u'\|^2\langle z,E_Rz\rangle\longrightarrow\infty.
\]
The wedge identity is obtained by expanding its antisymmetrized tensor;
the cross terms contain \(\langle u',z\rangle=0\).
Thus \(B_0\Omega\notin\mathcal D(H_0^{1/2})\), although
\(\Omega\in\mathcal D(H_0)\).

Let \(\varphi\) be a compact BV kernel with integral one, and choose any
fixed bounded selfadjoint even \(V_0\) in the supplied CAR class.
Norm continuity of the CAR orbit gives
\(A_{\varepsilon,0}(0)\to B_0\) in norm. If the actual operator norms on
the left of T15 remained bounded at one fixed \(\mu>0\), then
\(\|(H_0+\mu)^{1/2}A_{\varepsilon,0}\Omega\|\) would be bounded.
The lower semicontinuity of the closed positive form would put
\(B_0\Omega\) in its domain, a contradiction. One direct justification is
to bound every bounded spectral truncation on the norm-convergent vectors
and take its monotone limit. Hence the fixed-\(\mu\) form constants cannot
stay uniformly bounded as the temporal width shrinks.

This also applies to joint ordinary-cell approximants \(B_c\).
For example the selfadjoint \(i[\gamma(C_cf),\gamma(C_cg)]/2\) has the
required target, with eventual disjoint supports. T25-T30 imply
\(\widehat A_{\varepsilon(c),c}(0)\to B_0\otimes I_H\) whenever
\(\varepsilon(c)\to0\). If uniform actual fixed-\(\mu\) form constants
existed, apply them to the common vacuum. Since
\(H_c\ge H_0\otimes I_H\) on the actual range, bounded target spectral
truncations would again force finite target form energy of \(B_0\Omega\).
No divergence rate is proved by this contradiction. It is compatible
with T23 using a growing \(\mu(c)\), and with the qualitative point-window
correlation limit in T30.

### 9.2 A locally oscillatory family shows a genuine short-window failure

The following is outside the fixed ordinary-input C25 class; it uses the
allowed alternating-cell C24 family. It demonstrates why T24 cannot simply
be discarded for a theorem uniform over all bounded local cell families.

Choose normalized real compactly supported \(f=f_1e_1,g=g_1e_1\) with disjoint
supports. For sufficiently small \(c\), their occupied cell sets are disjoint.
Normalize their nonzero cell vectors and alternate them:
\[
 z_c=M_cC_cf/\|C_cf\|,\quad w_c=M_cC_cg/\|C_cg\|,\quad
 (M_cx)_r=(-1)^r x_r,\qquad B_c=i\gamma(z_c)\gamma(w_c).
 \tag{T32}
\]
They are real orthonormal coefficient vectors. Finite CAR therefore gives
\(B_c=B_c^*\), \(B_c^2=I\), \(\|B_c\|=1\); Local section 6 makes this a
finite-support even spin observable in a fixed interval containing the
supports and their small-cell endpoint enlargements.

Current C24 and \(\|C_cf\|,\|C_cg\|\to1\) give norm convergence of the
unital CAR images to a pure high-factor block
\(B_H=i\gamma_H(Rf)\gamma_H(Rg)\), where \(R\) is the fixed reflection.
The high polarization is constant in position/momentum. Its two-point
function vanishes for the disjoint supports, so
\(\langle\Omega_H,B_H\Omega_H\rangle=0\), while \(B_H^2=I\).
Consequently \(P\widehat B_cP\to0\) in norm.

Take the allowed interaction \(V_c=0\). On the actual one-particle
coefficient space the free generator norm is at most \(\mathcal E_c\).
CAR field continuity and two-factor telescoping give
\[
 \|\beta_{c,s}(B_c)-B_c\|\le2|s|\mathcal E_c .
\]
For a fixed real compact BV kernel \(\varphi\) of integral one and
\(m_1=\int|u\varphi(u)|du<\infty\),
\[
 \|A_{\varepsilon,c}(0)-B_c\|\le2\varepsilon\mathcal E_c m_1\to0
                 \quad\text{if }\varepsilon(c)/c\to0.       \tag{T33}
\]
Let the initial state be the exact actual free vacuum, of energy zero.
For the two identical averaged factors, selfadjointness and the preceding
norm limits imply
\[
 \langle\Omega,A_{\varepsilon,c}^2\Omega\rangle\to1,\qquad
 \langle\Omega,P A_{\varepsilon,c}P A_{\varepsilon,c}P\Omega\rangle
                =\|P A_{\varepsilon,c}\Omega\|^2\to0.        \tag{T34}
\]
Thus finite initial energy alone cannot make this short-window product
compression vanish uniformly over such varying bounded local families.
The example does not contradict fixed ordinary-input low convergence,
does not cover every intermediate window scale, and is not a global no-go.

## 10. Final scope and independent-derivation boundary

This note supplies a concrete sufficient regularity condition, not its necessity:
compact BV on the whole line, including jumps, suffices; \(W^{1,1}\) is a
convenient smaller class. Merely writing an interior derivative or a formal
commutator is not the domain proof. All operator and form inclusions actually
used above were obtained by weak adjoint-domain identities, resolvents and
closedness. The actual free gap, bounded total \(K\), and the actual initial
free-energy cap are the quantities entering the compression estimate.

The autonomous bounded interaction can be rough. No domain invariance of
\(V_c\), ground preparation, small coupling, gap of \(H_c+V_c\), or control of
unbounded energy by trace distance is assumed. Time-dependent ramps and
extensive interactions require separate arguments. Kernel choice remains a
supplied finite-resolution observable prescription, not a derived physical
measurement law.

The spatially rough example and locally oscillatory counterexample delimit
specific uniformity claims. They do not invalidate the positive fixed-width
theorem, the joint sufficient regime, or the ordinary-cell qualitative
point-window limit. No numerical, symbolic or formal runner was executed.
The original allowed sources, publication packages, repository, Git/PR/audit
state, prompts and campaign checkpoints remain unchanged. No outcome from
the separate root candidate was received before this core's seal.


## Publication dependencies and limits

The four direct parents are the [energy-transfer correlation theorem](ENERGY_TRANSFER_CORRELATION_BOUNDED_THEOREM_NOTE_2026-10-12.md),
the [bounded-interaction and ground theorem](BOUNDED_INTERACTION_GROUND_BOUNDED_THEOREM_NOTE_2026-10-12.md),
[Current](CURRENT_PRESERVING_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md), and
[Local Even](LOCAL_EVEN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-10-12.md).
Correlation supplies the two-sided finite-word trace estimate, actual high-band
gap and explicitly scoped state-limit alternatives. Bounded interaction
supplies the autonomous cocycle and actual free-energy control. Current supplies
the actual branches, common carrier and C21/C24/C25. Local supplies the ordinary
cell normalization and even-spin interpretation. The response theorem is not
a direct or mathematical premise here.

The canonical correlation note has exact hash
`60be3444c7e9e60090617944733f6c84dbd9184e3ca043d90bc71203ac2e1843`
and contains the unchanged frozen correlation core
`d63214a0d6365e1ae339f63caad67526bdd942130f76b064b13c2b7b2365b49c`.
Correlation in OPEN PR9500 and bounded interaction in OPEN PR9502 remain
provisional dependencies at the stacked base
`ba3ea535fa5ce80a3ad81b384a2063185da42756`. Current remains open_gate.
Main premise bytes are those of `516cb69d8487ff04f8a48e065d3dcbe71d7dd237`.
Exact canonical parent bytes and needed underlying assemblies are archived;
publication references do not enlarge their original review scopes.

The averaging theorem uses a nonnegative free operator, a bounded autonomous
selfadjoint interaction of arbitrary stated total norm, and a bounded observable.
It does not require the small-interaction ground-selection regime. Whole-line
compact BV kernel variation includes endpoint jumps. The weak domain argument
and square-root closure establish both adjoint sides of the actual free-energy
form bound; boundedness alone is not substituted for them. The high-vacuum
projection is distinct from a ground or Fock-band projection, and a product of
compressed factors is distinct from compressing the entire product.

Fixed kernels give the stated finite-word compression estimate under actual
finite-energy states, uniformly in center time at the bound level. Continuum
correlations still require the specified state convergence and compact enlarged
time-window norm-orbit premises. Partial-trace and normalized high-vacuum state
routes have distinct errors. Full-Fock normal subsequences do not imply trace-norm
compactness, unique state selection or preservation of a fixed particle sector.

Shrinking windows have explicit sufficient resources, including the varying
reference-energy improvement; neither necessity nor optimality is claimed.
The fixed rough-cell failure of a uniform point-window form constant coexists
with qualitative ordinary-cell correlation convergence under its premises.
The alternating C24 family is a separate varying-family obstruction. The note
does not turn these controls into a global no-go or a claim about arbitrary
unbounded observation times.

The [No-Go Discipline Gate](../.claude/science/physics-loops/toe-response-transfer-20261012/NO_GO_DISCIPLINE_CHECKLIST.md)
keeps N1 and N5 pending. No route-exhaustion certificate, new physical axiom,
empirical prediction, analytic formal verification, audit verdict or retained
promotion is supplied by this publication or its identity-only runner.
