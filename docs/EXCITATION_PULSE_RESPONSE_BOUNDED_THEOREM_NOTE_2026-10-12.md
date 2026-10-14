---
claim_id: excitation_pulse_response_bounded_theorem_note_2026-10-12
claim_type: bounded_theorem
claim_scope: "Conditional gapped ground excitation response and actual finite-pulse energy, domains and fixed-window limits for the supplied two-band model."
upstream_dependencies:
  - bounded_interaction_ground_bounded_theorem_note_2026-10-12
  - adiabatic_ground_preparation_bounded_theorem_note_2026-10-12
  - current_preserving_refinement_bounded_theorem_note_2026-10-12
  - local_even_continuum_bounded_theorem_note_2026-10-12
runner: scripts/excitation_pulse_response_identity_2026_10_12.py
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

Primary runner: [source identity and reconstruction only](../scripts/excitation_pulse_response_identity_2026_10_12.py).
It executes zero mathematical predicates, scientific mutations or formal checks.
Source identities and reconstruction do not establish mathematical truth.

**Publication chronology.** The complete frozen 1247-line assembly below is
`694e3962b6513089f7422e4c7f7f0a886488b2f2af81f2d8e04be9fea31247ce`.
Its later complete 491-line exact-source review is
`c50b1ac2b3c49fdf951c5729da1a17dbbda4c991cdb35342bd8d1a6a0882f16b`.
Root's complete-read/source-scope receipt is
`5ce736eaca68385d6c78e05d08d6869b064f1917fe05c5ff221b95095e932c2f`.
The review identified no required repair at the source's stated conditional
scope. The source's earlier pending labels remain literal historical records.
All mathematical body bytes, including its title and source ledger, are unchanged.
No Markdown-target relocation was necessary.

The response and pulse cores were independently derived before comparison
within the same model family and shared premises. The synthesis and its later
review were source exposed; the reviewer authored those earlier independent
cores and comparisons. This is corroborating ordinary analytic work, not a
new blind derivation, model-diverse verification, analytic formal proof or audit.
The exact exposure histories and complete originals are reconstructable from
the content-deduplicated evidence packet.

This wrapper adds publication metadata and dependency links only. Final review
and root acceptance of the wrapper, program and packet remain pending in this
source preparation. Source-scope acceptance does not authorize execution.

# Conditional excitation response and actual finite-pulse energy

Status: source-exposed conditional analytic synthesis, 2026-10-12.
The excitation-response and finite-pulse cores were separately reconstructed
before their respective comparisons. This note assembles those checked
arguments; it is not another independent proof, an audit, retained status,
an analytic Lean theorem, or a new physical axiom. Its own exact-source review
remains pending. Exact inputs and exposure coverage are recorded in section 12.

For the supplied massive full-Fock model with a small bounded total even
interaction, a bounded even observable has a positive finite connected
excitation measure. Static compressed-resolvent convergence gives narrow
measure convergence and compact-time connected correlations. Inverse moments
give static susceptibility and equilibrium ground curvature. Positive energy
moments require additional domains; a checked H1 coefficient class supplies
the first two, while a strict rough compact-cell example has infinite limiting
first moment.

A prescribed finite pulse can nevertheless have finite actual energy for
that rough observable. Absolutely continuous profiles, and profiles with
finitely many absolutely continuous pieces and jumps, give domain-preserving
propagation and an exact bounded-work identity. This proves finite-strength
energy bounds and continuum convergence, as well as a positive quadratic
absorption coefficient with an explicit remainder. A separate joint
lattice/impulse example shows why the pulse resources cannot be discarded.

The Hamiltonian, representation, physical clock, total potential, exact
initial ground, observable, source sign, amplitude and time profile are
supplied inputs. The note does not select them physically.

## 1. Actual model, comparison premises and notation

Fix m,v>0. The supplied actual finite-spacing free Hamiltonian is
\[
 H_c=d\Gamma(e_{c,L}\oplus e_{c,H}),\quad I_c=(-1/c,1/c),\quad
 w_c(p)=\sqrt{1-c^2p^2},
\]
\[
 e_{c,L}(p)^2=m^2+\frac{2v^2p^2}{1+w_c(p)},\qquad
 e_{c,H}(p)^2=m^2+\frac{2v^2}{c^2}(1+w_c(p)).             \tag{1}
\]
It acts on its actual full fermionic Fock space, with vacuum energy zero.
The target low space has
\[
 H_0=d\Gamma(E),\qquad E(p)=\sqrt{m^2+v^2p^2}.
\]
The coefficient convention is the unitary Fourier transform
\(\widehat f(p)=(2\pi)^{-1/2}\int e^{-ipx}f(x)\,dx\), with
\[
 D(p)=-vp\sigma_x-m\sigma_y,\qquad P_+(p)=\tfrac12(I+D(p)/E(p)).
\]
For real coefficient fields the Majorana convention is
\(\gamma(f)^*=\gamma(f)\),
\(\{\gamma(f),\gamma(g)\}=2(f,g)_{\mathbb R}I\), and
\(\|\gamma(f)\|=\|f\|\). In the target, acting on the free vacuum its
creation amplitude is \(\sqrt2P_+\widehat f\). These conventions fix the cell and wedge
normalizations used below; the underlying full-Fock realization is a
supplied parent premise.
The common carrier is the full doubled Fock space
\(\mathcal F_*=\mathcal F_L\otimes\mathcal F_H\), with the low factor ordered
first in the graded identification. The supplied vacuum-preserving
isometry \(\iota_c\) has range projection \(\Pi_c\). The target is embedded
with the high factor in its vacuum.

The actual form inequalities are
\[
 H_c\ge \Lambda_c N_{H,c}\ge\Lambda_c(I-P_{\mathrm{hv},c}),
 \qquad \Lambda_c=\sqrt{m^2+2v^2/c^2},                   \tag{2}
\]
and, on the embedded actual range,
\[
 H_c\ge H_0\otimes I_H.                               \tag{3}
\]
The low comparison in (3) follows from \(e_{c,L}\ge E\); outside-band
particles are absent. At fixed c the one-particle ceiling is
\(\sqrt{m^2+4v^2/c^2}\), but the full many-body Hamiltonian is unbounded.
Its domain is D(N) at fixed c. The target has the maximal dGamma(E) domain.

Let
\[
 G_c=H_c+V_c,\quad V_c=V_c^*,\quad \|V_c\|\le K<m/2,
 \qquad \delta=m-2K>0.                               \tag{4}
\]
The bound is on the total even potential. The supplied ground theorem
gives a simple even ground line with normalized vector \(\Omega_c\), energy
\(E_c\in[-K,K]\), projection \(P_{g,c}\), and
\[
 L_c=G_c-E_c\ge\delta(I-P_{g,c}).
\]
Write \(Q_{g,c}=I-P_{g,c}\) and
\(\omega_c(B)=\langle\Omega_c,B\Omega_c\rangle\).
Use analogous symbols at c=0. Bounded perturbation gives
D(G_c)=D(H_c) and equality of their shifted form domains. It does not imply
that V_c preserves either domain. Evenness is a restriction on these
experiments in full Fock, not a replacement by an even-only representation.

The free even sector has its next threshold at 2m. Any two-dimensional
strict spectral cutoff below 2m-K for the perturbed even operator would
contain a vector orthogonal to the free vacuum. Its Rayleigh quotient is
at least 2m-K, a contradiction. Taking increasing strict cutoffs shows
there is at most one even spectral direction below that threshold.
The even ground lies there since \(E_c\le K<2m-K\). Subtracting its
energy therefore gives the stronger even excitation threshold
\[
 \Delta=2m-2K.                                       \tag{5}
\]
The full-space ground and resolvent comparisons continue to use delta.
All conclusions concern allowed spacings satisfying the stated uniform
hypotheses, with limits through those spacings tending to zero.

Bounded observables and potentials use their common unital CAR extensions
\(\widehat A_c,\widehat V_c\); the target extension is tensor \(I_H\).
They preserve the physical ranges. Densities, vectors and actual resolvents
use isometric conjugation, extended by zero. In particular \(P_{g,c}\),
\(\Pi_c\) and \(P_{\mathrm{hv},c}\) are different projections. No actual
generator is replaced by a full-carrier Hamiltonian with additional
zero-energy modes.

Take \(A_c=A_c^*\) even with \(\|A_c\|,\|A_0\|\le a\), and assume
\[
 \alpha_c=\|\widehat A_c-A_0\otimes I_H\|\longrightarrow0,\qquad
 \nu_c=\|\widehat V_c-V_0\otimes I_H\|\longrightarrow0. \tag{6}
\]
A concrete sufficient class consists of fixed finite even polynomials in
ordinary cells
\[
 (C_cf)_r=c^{-1/2}\int_{cr}^{c(r+1)}f(x)\,dx
\]
of real compactly supported L2 coefficients. Potentials are separately
selfadjoint and obey (4). Current C21/C25 and Local sections 3 and 6,
especially L23-L24, supply the common limits and finite-cell even-spin
representatives. This citation makes no new propagation or local-ground
claim. More general in-band bounded even CAR potentials are allowed when
their comparison assumptions are stated explicitly.

Fix a reference \(s_*>K\). The pinned static ground theorem supplies
\[
 S_c=\iota_c(G_c+s_*)^{-1}\iota_c^*,\quad
 S_0=(G_0+s_*)^{-1}\otimes|\Omega_H\rangle\langle\Omega_H|,
\]
\[
 \epsilon_c^R=\frac{s_*^2c/v+\nu_c}{(s_*-K)^2},\quad
 \|S_c-S_0\|\le\epsilon_c^R,\quad \|S_c\|\le(s_*-K)^{-1},
\]
\[
 d_*=\frac{\delta}{(s_*+K)(s_*+m-K)},\quad
 p_c=\min(1,\epsilon_c^R/d_*),\quad
 \|\widehat P_{g,c}-\widehat P_{g,0}\|\le p_c,\quad
 \|\widehat P_{g,c}-\widehat P_{g,0}\|_1\le2p_c,
\]
\[
 |E_c-E_0|\le e_c:=(s_*+K)^2\epsilon_c^R.             \tag{7}
\]
These are zero-extended compressed resolvents; S_0 is not extended by the
identity on high Fock. No compact-resolvent hypothesis is present.

For explicit dynamical comparison, assume separately, on every fixed
\(|t|\le T\), the free-orbit moduli \(\nu_{A,c}(T),\nu_{V,c}(T)\to0\).
Here \(\alpha_{c,t}(B)=e^{itH_c}Be^{-itH_c}\), and, on the common unital
comparison algebra, these moduli mean
\[
 \nu_{A,c}(T)=\sup_{|t|\le T}
 \|\widehat\alpha_{c,t}(A_c)-\alpha_{0,t}(A_0)\otimes I_H\|,\qquad
 \nu_{V,c}(T)=\sup_{|t|\le T}
 \|\widehat\alpha_{c,t}(V_c)-\alpha_{0,t}(V_0)\otimes I_H\|.
\]
Any exterior free extension used to define those common orbits is confined
to bounded comparison; it is not substituted into (1)-(3) or actual energy.
The bounded interaction cocycle then gives
\[
 d_{A,c}(T):=\nu_{A,c}(T)+2Ta\,\nu_{V,c}(T)
 \ \ge\sup_{|t|\le T}
 \|\widehat\beta_{c,t}(A_c)-\beta_{0,t}(A_0)\otimes I_H\|,\qquad
 \beta_{c,t}(A)=e^{itG_c}Ae^{-itG_c}.                 \tag{8}
\]
Indeed \(Z_c=e^{itG_c}e^{-itH_c}\) has right generator
\(Z_c'=iZ_c\alpha_{c,t}(V_c)\). Differentiation first on D(H_c) cancels
the unbounded terms; uniqueness identifies the norm integral solution.
The identity
\((Z_cZ_0^*)'=iZ_c(\alpha_c(V_c)-\alpha_0(V_0))Z_0^*\)
gives \(\|Z_c-Z_0\|\le T\nu_{V,c}(T)\); two conjugating unitaries give (8).
Ordinary fixed-cell polynomials supply these moduli. A general in-band
potential must have this additional premise when (8) is used.
Time-zero norm convergence is not renamed an operator-norm orbit estimate.

## 2. Connected spectral measures and static narrow convergence

Let \(a_{0,c}=\langle\Omega_c,A_c\Omega_c\rangle\), and set
\[
 \xi_c=(A_c-a_{0,c})\Omega_c,\qquad
 \mathsf M_c(B)=\langle\xi_c,\mathbf1_B(L_c)\xi_c\rangle.
                                                               \tag{9}
\]
The spectral theorem gives a positive finite Borel measure with
\[
 M_c:=\mathsf M_c(\mathbb R)=\|\xi_c\|^2
      =\omega_c(A_c^2)-\omega_c(A_c)^2\le a^2,\qquad
 \operatorname{supp}\mathsf M_c\subset[\Delta,\infty). \tag{10}
\]
Centering removes precisely the elastic ground atom
\(a_{0,c}^2\delta_0\). The support improvement uses evenness; without it
delta is the safe threshold. No energy domain for \(A_c\Omega_c\) is needed.

Choose ground phases with nonnegative common overlap. The rank-one angle
identity gives
\[
 \|\widehat\Omega_c-\widehat\Omega_0\|\le\sqrt2p_c,\qquad
 \|\widehat\xi_c-\widehat\xi_0\|\le
 q_c:=\alpha_c+(1+\sqrt2)a p_c,\qquad
 |M_c-M_0|\le2a q_c.                                 \tag{11}
\]
This follows by telescoping \((I-\widehat P_g)\widehat A\widehat\Omega\).
The connected correlation in the stated product order is
\[
 C_c(t)=\omega_c(\beta_{c,t}(A_c)A_c)-a_{0,c}^2
       =\langle\xi_c,e^{-itL_c}\xi_c\rangle
       =\int e^{-it\omega}\,d\mathsf M_c(\omega).       \tag{12}
\]
It is continuous, bounded by M_c, and \(C_c(-t)=\overline{C_c(t)}\).

Static comparisons (6)-(7) suffice for narrow finite-measure convergence.
For \(f\in C_0(\mathbb R)\), define on a common compact spectral interval
containing the spectra of S_c
\[
 g_{c,f}(s)=f(s^{-1}-s_*-E_c)\quad(s>0),\qquad g_{c,f}(0)=0.
                                                               \tag{13}
\]
It is continuous at zero because f vanishes at infinity. Uniform continuity
of f gives \(g_{c,f}\to g_{0,f}\) uniformly. Polynomial approximation gives
norm continuity of continuous functional calculus for S_c, hence
\(g_{c,f}(S_c)\to g_{0,f}(S_0)\) in norm. These are precisely the
zero-extended compressions of f(L_c), not f applied to exterior zero modes.
Taking expectations in the convergent xi vectors proves
\(\int f\,d\mathsf M_c\to\int f\,d\mathsf M_0\).

Mass convergence in (11) prevents escape to infinite frequency. A compact
continuous cutoff equal to one on [0,R], followed by R tending to infinity,
makes the eventual mass outside that cutoff as small as the target tail.
This is tightness near c=0. Cutting off a bounded continuous test now proves
\[
 \int f\,d\mathsf M_c\longrightarrow\int f\,d\mathsf M_0
 \qquad\text{for every bounded continuous }f.         \tag{14}
\]
No subsequence, arbitrary-state compactness or compact resolvent is used.
If M_0>0, the normalized probability measures converge as well. If M_0=0,
only vanishing unnormalized mass is concluded.

Tightness and
\(|e^{-it\omega}-e^{-is\omega}|\le R|t-s|\) on [0,R]
give equicontinuity on compact time intervals; a finite time net therefore
upgrades (14) to compact-time uniform convergence of (12), already under
the static hypotheses.

For a quantitative route under (8), direct telescoping gives
\[
 \sup_{|t|\le T}|C_c(t)-C_0(t)|
 \le d_{C,c}(T):=a\,d_{A,c}(T)+3a\alpha_c+6a^2p_c.    \tag{15}
\]
The uncentered word costs \(a d_A+a\alpha_c+2a^2p_c\);
the mean-square correction costs \(2a\alpha_c+4a^2p_c\).
The independent alternative
\(2a\nu_{A,c}(T)+4Ta^2\nu_{V,c}(T)+6a^2p_c+2a\alpha_c\)
is also a sufficient modulus. Either may be capped by \(2a^2\).

The root's alternative Fourier route is consistent: for h>0,
\[
 M_c-\frac1{2h}\int_{-h}^h\operatorname{Re}C_c(t)\,dt
 =\int\left[1-\frac{\sin(h\omega)}{h\omega}\right]d\mathsf M_c.
                                                               \tag{16}
\]
The bracket is nonnegative and at least 1/2 for \(|\omega|\ge2/h\).
Compact-time convergence and target dominated convergence as h decreases
give tightness. Fourier inversion for smooth compact tests, then cutoff
approximation, give (14). This route requires a correlation comparison;
(13) establishes the same result from weaker static premises.

## 3. Finite resolution and the specified causal response

For \(\operatorname{Im}z>0\), define
\[
 F_c(z)=\int\frac{d\mathsf M_c(\omega)}{\omega-z},\qquad
 s_{c,\eta}(x)=\frac1\pi\operatorname{Im}F_c(x+i\eta).
                                                               \tag{17}
\]
F_c is Herglotz, \(|F_c(z)|\le a^2/\operatorname{Im}z\), and
\[
 s_{c,\eta}(x)=\int\frac{\eta\,d\mathsf M_c(\omega)}
                           {\pi((\omega-x)^2+\eta^2)}\ge0,\qquad
 \int_{\mathbb R}s_{c,\eta}(x)\,dx=M_c.
\]
Broadened tails below Delta do not change the measure's exact support.
Fubini gives \(F_c(z)=i\int_0^\infty e^{izt}C_c(t)\,dt\).
For eta,T>0 put
\[
 \mathcal J_c(\eta,T)=
 \frac{d_{C,c}(T)(1-e^{-\eta T})+2a^2e^{-\eta T}}{\eta}.
                                                               \tag{18}
\]
Splitting the time integral at T proves, uniformly in real x,
\[
 |F_c(x+i\eta)-F_0(x+i\eta)|\le\mathcal J_c(\eta,T),\qquad
 |s_{c,\eta}(x)-s_{0,\eta}(x)|\le\mathcal J_c(\eta,T)/\pi.
                                                               \tag{19}
\]
At fixed eta choose T then c. A shrinking eta(c) or growing T(c) requires
the displayed error actually to vanish; no universal rough-cell rate follows.
Qualitative compact-time convergence can replace (15) for qualitative limits.

Introduce the externally prescribed source
\[
 G_{c,\varepsilon}(t)=G_c-\varepsilon j(t)A_c,\quad
 \varepsilon\in\mathbb R,\qquad \hbar=1.               \tag{20}
\]
For real integrable j on [0,T], the interaction-picture integral equation
\[
 U_{I,c}'(t)=i\varepsilon j(t)\beta_{c,t}(A_c)U_{I,c}(t),
 \qquad U_{I,c}(0)=I                                \tag{21}
\]
has a unitary bounded Dyson solution. It gives bounded readouts without
assuming observable-domain invariance. Energy propagation for this protocol
will require the extra temporal hypotheses of section 7.

Starting in the exact ground, differentiating the bounded Dyson series at
zero source strength gives
\[
 r_{c,j}(t)=\int_0^t j(s)\chi_c(t-s)\,ds,\qquad
 \chi_c(t)=i\mathbf1_{t\ge0}\omega_c([\beta_{c,t}(A_c),A_c])
         =2\mathbf1_{t\ge0}\int\sin(\omega t)\,d\mathsf M_c.
                                                               \tag{22}
\]
The minus sign in (20), the order in (12), and the physical clock fix this
positive sine sign. Opposite source sign reverses the linear response.
If \(J(t)=\int_0^t|j(s)|ds\), the n-th nested commutator is bounded by
\(a(2|\varepsilon|aJ(t))^n/n!\). Therefore
\[
 |\langle A_c\rangle_\varepsilon(t)-a_{0,c}
                         -\varepsilon r_{c,j}(t)|
 \le a[e^{2|\varepsilon|aJ(t)}-1-2|\varepsilon|aJ(t)]
 \le2\varepsilon^2a^3J(t)^2e^{2|\varepsilon|aJ(t)}.     \tag{23}
\]
This is a uniform bounded-readout remainder, not an unbounded energy estimate.
Equation (15) gives \(\sup_{0\le t\le T}|\chi_c-\chi_0|\le2d_{C,c}(T)\)
and \(\sup|r_{c,j}-r_{0,j}|\le2J(T)d_{C,c}(T)\).

The causal Fourier-Laplace transform is
\[
 \chi_c(z)=\int_0^\infty e^{izt}\chi_c(t)\,dt
 =\int\left[\frac1{\omega-z}+\frac1{\omega+z}\right]d\mathsf M_c
 =2\int\frac{\omega}{\omega^2-z^2}\,d\mathsf M_c.       \tag{24}
\]
It is analytic, bounded by \(2a^2/\operatorname{Im}z\), and its difference
is at most \(2\mathcal J_c(\eta,T)\) at \(z=x+i\eta\).
For x>0,eta>0,
\[
 \operatorname{Im}\chi_c(x+i\eta)
 =\int\eta\left[\frac1{(\omega-x)^2+\eta^2}
               -\frac1{(\omega+x)^2+\eta^2}\right]d\mathsf M_c\ge0.
\]
The sign reverses at x<0; chi is not Herglotz on the whole upper half-plane.
Positive-frequency boundary absorption is the measure \(\pi\mathsf M_c\),
obtained distributionally by the Poisson kernels on compact tests inside
(0,infinity); no ordinary spectral density is assumed. For real |x|<Delta
there is no absorption and
\[
 0\le\chi_c(x)\le \frac{2a^2\Delta}{\Delta^2-x^2}.      \tag{25}
\]
These are response statements for the supplied observable and source.

## 4. Static susceptibility, reduced resolvents and ground curvature

Let \(R_c=Q_{g,c}L_c^{-1}Q_{g,c}\) denote the reduced inverse on the actual
space, zero on the ground. It is bounded by \(1/\delta\) on full Fock,
by \(1/\Delta\) on even vectors, and maps into D(G_c). Define
\[
 \chi_c^{\rm stat}=2\langle\xi_c,R_c\xi_c\rangle
     =2\int\omega^{-1}\,d\mathsf M_c,\qquad
 0\le\chi_c^{\rm stat}\le2M_c/\Delta\le2a^2/\Delta.     \tag{26}
\]
No positive energy moment is required. It is positive exactly when xi_c is
nonzero. The static frequency value differs from the time-kernel value
\(\chi_c(t=0)=0\).

Here is a static quantitative comparison which does not require orbit
moduli. On the common carrier put
\[
 B_c=-(s_*+E_c)I+\delta\widehat P_{g,c},\quad
 Y_c=I+S_cB_c,\quad T_c=Y_c^{-1}S_c,\quad
 \widehat R_c=T_c-\delta^{-1}\widehat P_{g,c},\quad
 M_*=1+(s_*+K)/\delta.                               \tag{27}
\]
On the ground Y_c has eigenvalue \(\delta/(s_*+E_c)\); on an excitation
ell>=delta it is \(\ell/(\ell+s_*+E_c)\); off the physical range it is one.
Thus \(\|Y_c^{-1}\|\le M_*\). T_c is the zero-extended compressed inverse
of \(L_c+\delta P_{g,c}\); no inverse of S_c on its kernel is used.

Multiplication on both sides verifies the ordered bounded identity
\[
 T_c-T_0=(I+S_cB_c)^{-1}
 [S_c-S_0+S_c(B_0-B_c)S_0](I+B_0S_0)^{-1}.           \tag{28}
\]
Only each own spectral pair commutes; there is no cross-pair commutation.
Consequently
\[
 \|\widehat R_c-\widehat R_0\|\le
 r_c:=M_*^2\left[\epsilon_c^R+
          \frac{e_c+\delta p_c}{(s_*-K)^2}\right]+\frac{p_c}{\delta},
\]
\[
 |\chi_c^{\rm stat}-\chi_0^{\rm stat}|
       \le4a q_c/\Delta+2a^2r_c.                    \tag{29}
\]
The vector difference is even, permitting Delta in that term. The full
resolvent bound r_c continues to use delta.

For a separately supplied static source \(G_c-hA_c\), the uniform sufficient
condition \(|h|a<\delta/2\) isolates its simple ground by a contour of radius
delta/2 about E_c. The bounded resolvent Neumann series gives an analytic
rank-one ground projection. For
\(R_h(z)=(G_c-hA_c-z)^{-1}\),
\[
 G_cR_h(z)=I+(z+hA_c)R_h(z).
\]
The projection is therefore analytic into the fixed graph space. A local
normalized ground section may be differentiated in that graph norm.
At h=0 choose parallel gauge. Differentiating the eigenvalue equation gives
\[
 E_c'(0)=-a_{0,c},\quad
 \Omega_c'(0)=R_c\xi_c,\quad
 \frac{d}{dh}\langle A_c\rangle_{\rm ground}\big|_0=\chi_c^{\rm stat},
 \qquad E_c''(0)=-\chi_c^{\rm stat}.                 \tag{30}
\]
The inverse maps the bounded source vector into the domain, even if
\(A_c\Omega_c\) itself is outside the form domain.

The same static value is the zero-frequency Abel limit of (24), with
\[
 0\le\chi_c^{\rm stat}-\chi_c(i\eta)
 \le\frac{2\eta^2a^2}{\Delta(\Delta^2+\eta^2)}.
\]
Combining both endpoint errors and (18) gives the alternative bound
\[
 |\chi_c^{\rm stat}-\chi_0^{\rm stat}|
 \le2\mathcal J_c(\eta,T)
       +\frac{4\eta^2a^2}{\Delta(\Delta^2+\eta^2)}.     \tag{31}
\]
Neither (26) nor (31) asserts an absolutely convergent undamped time integral.

A sudden unit step has linear coefficient
\[
 r_c(t)=2\int\frac{1-\cos(\omega t)}{\omega}\,d\mathsf M_c. \tag{32}
\]
A nonzero positive-frequency atom prevents its ordinary long-time limit.
Indeed the cosine transform of the finite measure
\(\omega^{-1}d\mathsf M_c\) has zero Cesaro mean by the gap, but Cesaro
pairing with the cosine at that atom's frequency isolates half its positive
weight. A transform tending to a constant would give zero such pairing.
The Abel mean of (32) is chi_c(i eta), tending to (26). A source
\(e^{\eta t}\) applied from the remote past has the same linear coefficient
at t=0. These operations differentiate in source strength first at fixed
eta; (23) supplies no uniform finite-strength limit as the switching
interval diverges. Static equilibrium and Abel response imply no relaxation.

## 5. Positive moments, the H1 class and a rough compact-cell witness

For r>=0 the exact spectral domain statement is
\[
 m_{r,c}:=\int\omega^r\,d\mathsf M_c
          =\|L_c^{r/2}\xi_c\|^2,                    \tag{33}
\]
with value infinity outside the power domain. For positive powers the
ground component may be added or removed. The first moment is the excitation
form energy when \(A_c\Omega_c\in D(L_c^{1/2})\). If it lies in D(G_c),
\[
 m_{2,c}=\|[G_c,A_c]\Omega_c\|^2.                    \tag{34}
\]
If also \(A_c^2\Omega_c\in D(G_c)\), expansion on the ground gives the
literal double-commutator rule
\[
 \omega_c([A_c,[G_c,A_c]])=2m_{1,c}.                 \tag{35}
\]
Under form hypotheses alone the corresponding quadratic-form expression
equals \(2m_{1,c}\); it must not be called an already defined operator
commutator. Boundedness of A alone supplies none of these positive moments.

Writing positive-frequency absorption as
\(\chi_c''(d\omega)=\pi\,d\mathsf M_c(\omega)\), the exact rules are
\[
 \chi_c^{\rm stat}=\frac2\pi\int\omega^{-1}\chi_c''(d\omega),\quad
 M_c=\frac1\pi\int\chi_c''(d\omega),\quad
 m_{1,c}=\frac1\pi\int\omega\,\chi_c''(d\omega),
\]
\[
 \lim_{\eta\to\infty}\eta^2\chi_c(i\eta)=2m_{1,c}.     \tag{36}
\]
The last statement includes infinity by monotone convergence. Without a
first moment only \(\chi_c(i\eta)\le M_c/\eta\) is automatic. Finite moments
justify, for example, \(C_c'(0)=-im_{1,c}\) and \(C_c''(0)=-m_{2,c}\).
If M_c>0 and m_1,c is finite, Cauchy-Schwarz gives
\[
 2M_c^2/m_{1,c}\le\chi_c^{\rm stat}\le2M_c/\Delta.     \tag{37}
\]
Narrow convergence gives only
\(m_{r,0}\le\liminf m_{r,c}\). Uniform integrability of the omega^r tails
implies convergence; a uniform (r+epsilon)-moment bound is sufficient,
with tail bounded by a constant times R^(-epsilon).

A checked sufficient coefficient class is a fixed finite polynomial of real
compact H1 fields. The actual signed one-particle symbol obeys
\[
 D_c(q)^2=\left[m^2+(v^2/c^2)|e^{icq}-1|^2\right]I,\quad
 D=iv\sigma_x\partial_x-m\sigma_y,\quad
 \|Df\|^2=m^2\|f\|^2+v^2\|f'\|^2.
\]
Cells commute with lattice translations and are contractive. Hence
\[
 \|D_cC_cf\|^2
   =m^2\|C_cf\|^2+v^2\|C_cd_c^+f\|^2
   \le m^2\|f\|^2+v^2\|f'\|^2.                       \tag{38}
\]
Here \(d_c^+f=c^{-1}(f(\,\cdot+c)-f)\), an average of f', proving the bound.
Local L10 gives for H2 coefficients
\[
 \|D_cC_cf-C_cDf\|\le(c/2)(m\|f'\|+v\|f''\|).
\]
Approximate a real compact H1 coefficient by real compact H2 coefficients
in H1. The uniform bound (38), this H2 estimate and Current C21 give
\[
 J_c(iD_cC_cf)\longrightarrow(iDf,0).                \tag{39}
\]
For real f, iDf and iD_cC_cf are in the real coefficient spaces. The
Majorana derivative is \(\gamma(iDf)\), not \(i\gamma(Df)\).

For \(A=\sum_k a_k\prod_j\gamma(f_{kj})\), free differentiation replaces
one factor at a time by gamma(iDf). A uniform commutator bound is
\[
 C_A=\sum_k|a_k|\sum_j\|Df_{kj}\|
                   \prod_{\ell\ne j}\|f_{k\ell}\|,\qquad
 C_*=C_A+2Ka.                                      \tag{40}
\]
Equation (39) and telescoping give norm convergence of the common free
derivatives. Time-zero convergence of V and A gives norm convergence of
the interacting commutators, bounded by C_*.
To prove domain preservation, for x in D(H) differentiate
\(e^{itH}Ax=\alpha_t(A)e^{itH}x\). Norm differentiability of the bounded
orbit gives a Hilbert derivative, so the generator criterion puts Ax in
D(H). Then D(G)=D(H) and the bounded [V,A] term prove the interacting
domain assertion. Products give the same for A squared. V need not
preserve either domain.

Consequently (34)-(35) hold in this H1 class, and
\[
 m_{2,c}\le C_*^2,\quad m_{1,c}\le a C_*,\qquad
 m_{1,c}\to m_{1,0},\quad m_{2,c}\to m_{2,0}.         \tag{41}
\]
The first-moment tail is at most \(C_*^2/R\). The second-moment limit uses
the norm-convergent commutator vectors and ground vectors, not that tail
bound alone. Higher moments need additional power-domain or iterated
commutator control; rough V is not regularized by smooth A.

For the explicit failure with bare compact L2 data, take V=0,
\[
 f=\mathbf1_{[0,1]}e_1,\quad
 g=g_1e_1\ne0\text{ smooth real with support in }(2,3),\quad
 A_c=\tfrac i2[\gamma(C_cf),\gamma(C_cg)],\quad
 A_0=i\gamma(f)\gamma(g).
\]
The cells are disjoint for small c. If
\(u=\sqrt2P_+\widehat f,\ z=\sqrt2P_+\widehat g\), the positive polarization
has diagonal entries 1/2, so
\[
 \|u(p)\|^2=\frac{1-\cos p}{\pi p^2},\qquad
 \int E(p)\|u(p)\|^2dp=\infty,\qquad z\in D(E^{1/2}),\ z\ne0. \tag{42}
\]
Intervals where 1-cos p is bounded below give the divergent harmonic tail.
Subtract the z component to get \(u'\perp z\) still outside D(E^(1/2)).
For \(E_R=\min(E,R)\), the two-particle wedge satisfies
\[
 \langle u'\wedge z,d\Gamma(E_R)(u'\wedge z)\rangle
 =\|z\|^2\langle u',E_Ru'\rangle+
       \|u'\|^2\langle z,E_Rz\rangle\longrightarrow\infty. \tag{43}
\]
Orthogonality kills the cross terms. This wedge is the nonzero two-particle
part of A_0 Omega, up to a phase; centering cannot remove it. Thus
\(m_{1,0}=\infty\). At each fixed c only zero/two-particle sectors occur
and the one-particle band is bounded, so all positive moments are finite.
Lower semicontinuity gives \(m_{1,c}\to\infty\). Finite spectral mass,
narrow convergence, finite resolution and finite static susceptibility
all persist for this strict ordinary compact-cell example.

## 6. Spectral topology controls and their different potential classes

Weak convergence does not generally strengthen to total variation. As an
abstract control, \(G_c=\operatorname{diag}(0,\omega_0+c)\),
\(G_0=\operatorname{diag}(0,\omega_0)\), \(A=\sigma_x\), with omega_0>Delta,
have convergent generators, resolvents and identical grounds. Their
excitation measures are \(\delta_{\omega_0+c}\) and \(\delta_{\omega_0}\),
whose total-variation norm difference is two. This is an abstract
two-level implication test, not the supplied chain.

There is also an actual-band example in the general bounded in-band CAR
potential class. It has a fixed ordinary compact-cell observable, but its
potential is not a strict compact-spatial-cell polynomial. Its momentum
packets have noncompact spatial tails; that restriction must remain explicit.

Trivialize the one-dimensional positive-polarization fiber measurably and
choose a bandwidth b>0 and orthonormal scalar packets
\[
 u_+(p)=b^{-1/2}\mathbf1_{(0,b)}(p),\qquad
 u_-(p)=b^{-1/2}\mathbf1_{(-b,0)}(p).
\]
For c<1/b they lie in the actual low band. Choose \(0<\lambda<m/4\) and
\[
 \widehat V_c=V_0\otimes I_H
       =-\lambda[n(u_+)+n(u_-)],\qquad K=2\lambda<m/2. \tag{44}
\]
The number projections commute and the total norm is 2lambda. The physical
Hamiltonian is exactly the second quantization of
\(e_{c,L}-\lambda(P_{u_+}+P_{u_-})\), with the unchanged high branch.
The one-particle lower bound is m-lambda>0, so the free vacuum remains the
unique full-Fock ground, with E_c=0. On the packets' fixed compact momentum
support, \(e_{c,L}\to E\) uniformly. CAR norm continuity therefore gives
compact-time comparison of the potential's free orbit. This example
satisfies both static and dynamic general-potential hypotheses.

Each momentum half-interval reduces the one-particle operator. Its unique
subthreshold bound energy b_c<m solves
\[
 1=\frac{\lambda}{b}\int_0^b
                   \frac{dp}{e_{c,L}(p)-b_c}.        \tag{45}
\]
The eigenvector is a normalized multiple of
\((e_{c,L}-b_c)^{-1}u_+\), with a reflected negative packet. The right side
is strictly increasing in the candidate energy, tends to zero at minus
infinity, and diverges at m because the dispersion rises quadratically from
m. The lower operator bound gives \(b_c\in[m-\lambda,m)\). The rank-one
resolvent formula is invertible below m away from that single scalar zero,
excluding further subthreshold spectrum.

Let b_0 be the target root. For 0<|p|<1/c the actual formula (1) gives
\(e_{c,L}(p)>E(p)\). At candidate b_0 the finite-c integral in (45) is
strictly smaller than one. Hence
\[
 b_c>b_0,\qquad b_c\longrightarrow b_0.              \tag{46}
\]
For convergence, uniform dispersion convergence and two fixed candidates
on opposite sides of b_0 trap the monotone roots. Their denominators remain
separated from zero, so the normalized bound vectors \(v_{c,+},v_{c,-}\)
converge in norm as well.

The even pair \(\Phi_c=v_{c,+}\wedge v_{c,-}\) is the lowest nonvacuum even
excitation, with energy 2b_c, isolated below b_c+m. There are only two
subthreshold one-particle modes, all other one-particle energies are at
least m, and higher even particle sectors cannot lower this threshold.
This is an even-sector statement, not an exclusion of odd spectrum.

A selfadjoint pair-creation plus pair-annihilation operator for the target
bound modes has a nonzero matrix element to Phi_0. Express it using the four
real Majorana preimages of those two modes, approximate those coefficients
by compact real L2 fields, and symmetrize. Operator-norm approximation
preserves a nonzero matrix element. This constructs a fixed compact
degree-two even polynomial A_0 with
\[
 w=|\langle\Phi_0,A_0\Omega\rangle|^2>0.
\]
Its ordinary-cell representatives satisfy (6) and (8). The resulting
excitation measures have
\[
 \mathsf M_0(\{2b_0\})=w,\qquad
 \mathsf M_c(\{2b_0\})=0\quad\text{for all small positive }c. \tag{47}
\]
The atom at 2b_c has weight w_c->w; the target even spectrum has no value
there once \(2b_c<b_0+m\). Testing the signed measure on these two atoms
gives total-variation norm at least \(w_c+w\to2w\). Thus even convergence
on every fixed Borel set fails, while (14) holds. Atoms also invalidate
any blanket replacement by ordinary spectral densities or uniform
cumulative-mass convergence at jumps.

Equation (47) is not a counterexample under the further restriction that
the potential itself use strictly compact ordinary spatial coefficients.
Weak and finite-resolution convergence hold in that subclass, but neither
a total-variation theorem nor a counterexample for that narrower class
is supplied here. This is a named stronger-topology obligation.

## 7. Finite pulses: common-domain propagation from AC coefficients

For the principal pulse theorem take real
\[
 j\in W^{1,1}([0,T]),\qquad j(0)=j(T)=0              \tag{48}
\]
in its absolutely continuous representative, extended by zero outside the
interval. Define
\[
 J(t)=\int_0^t|j(s)|ds,\quad J=J(T),\quad
 V_j(t)=\int_0^t|j'(s)|ds,\quad V_j=V_j(T),
\]
\[
 B_j=\int_0^T J(t)|j'(t)|dt\le JV_j,\qquad
 C_j=\int_0^T J(t)^2|j'(t)|dt\le J^2V_j.            \tag{49}
\]
There is no smallness requirement on \(|\varepsilon|a\|j\|_\infty\).
The pulse may close an instantaneous gap. The work and domain arguments
need only a nonnegative excitation operator and its initial zero-energy
ground; the gap is used for the model's selection/comparison and separate
gap-dependent estimates.

The following construction proves the required domain assertions. Let F>=0
be selfadjoint on a fixed D, and let B(t)=B(t)* have the norm-Bochner
representation
\[
 B(t)=B(0)+\int_0^t B'(s)ds,\qquad \int_0^T\|B'(s)\|ds<\infty. \tag{50}
\]
This explicit AC hypothesis holds for \(-\varepsilon j(t)A\). It does not
appeal to a general differentiability theorem for arbitrary Banach-valued
AC maps. Each F+B(t) is selfadjoint on D by bounded perturbation.

First construct U(t,r) on the Hilbert space using the bounded strong
interaction-picture Dyson integrals for
\(e^{itF}B(t)e^{-itF}\). Their simplex norm majorants give convergence and
unitarity. For a fixed eta in D, differentiating the freely moved test
vector gives the weak equation
\[
 \partial_t\langle\eta,U(t,r)x\rangle
       =-i\langle(F+B(t))\eta,U(t,r)x\rangle.          \tag{51}
\]
Inner products are antilinear in their first entry. This construction
requires no domain invariance of U or B.

Choose b>sup||B(t)|| and put
\[
 Y_t=F+B(t)+b>0,\qquad R_t=Y_t^{-1},\qquad D_t=B'(t)R_t.
\]
The bounded resolvent identity gives almost everywhere
\[
 R_t'=-R_tB'(t)R_t,\qquad
 FR_t=I-(B(t)+b)R_t.                                \tag{52}
\]
Both R_t and FR_t are norm AC with norm-integrable derivatives. Their
integral pairs lie in the closed graph of F, so R_t is AC as a map into
the fixed graph space D.

For arbitrary z_r solve the Volterra equation
\[
 z(t)=U(t,r)z_r+\int_r^t U(t,s)D_s z(s)ds.             \tag{53}
\]
The integrable norm of D and the factorial majorant give a unique continuous
z. Its fixed-D-test equation is
\[
 \partial_t\langle\eta,z\rangle
 =-i\langle(F+B(t))\eta,z\rangle+\langle\eta,D_tz\rangle
\]
almost everywhere. The product rule also holds for graph-AC test paths:
approximate them by graph-piecewise-linear paths, uniformly in graph norm
with derivatives converging in L1 graph norm. Boundedness of z, the uniform
D-to-H bound of F+B(t), and integrability of D_t pass all scalar integral
identities to the limit. This assumes no strong derivative or domain
membership of z.

Apply that rule to \(R_t\eta\), for any Hilbert vector eta, and put u=R_tz.
The terms \(R_t'+R_tD_t\) cancel. Since
\((F+B(t))R_t=I-bR_t\) is bounded, selfadjoint and norm continuous, the
remaining equation is
\[
 u(t)=u(r)-i\int_r^t(I-bR_s)z(s)\,ds.                \tag{54}
\]
Thus u is Hilbert C1, belongs to D at every time, solves the actual
Schrodinger equation, and is graph continuous because \(Y_tu(t)=z(t)\).
For u_r in D choose z_r=Y_ru_r. Transform this now regular solution into
the interaction picture and use bounded-equation uniqueness to identify it
with U(t,r)u_r. Reverse time proves onto-D propagation. Domain invariance
has been proved after construction, not assumed to identify the solution.

Gronwall in (53) gives in both directions
\[
 \|Y_tU(t,r)Y_r^{-1}\|
 \le\exp\!\left(\int_{\min(r,t)}^{\max(r,t)}
                         \|B'(s)Y_s^{-1}\|ds\right). \tag{55}
\]
For F=L_c and B=-epsilon j A_c, choose
\(b=\rho+|\varepsilon|a\|j\|_\infty\), rho>0. Then \(Y_t\ge\rho\), and
the right side is at most
\(\exp(|\varepsilon|aV_j/\rho)\), uniformly in c. The initial ground is
in D(L_c). Consequently the entire actual pulse path is in D(G_c),
Hilbert C1 and graph continuous. No bounded commutator [G_c,A_c],
observable-domain invariance, or uniform one-particle ceiling is needed.

## 8. Exact work, finite-strength caps and finite jumps

Write \(\psi_{c,\varepsilon}(t)\) for the actual solution of (20) from
\(\Omega_c\), and
\[
 a_{\varepsilon,c}(t)=\langle\psi_{c,\varepsilon}(t),
                              A_c\psi_{c,\varepsilon}(t)\rangle,\qquad
 q_c(t)=\langle\psi_{c,\varepsilon}(t),
                    (L_c-\varepsilon j(t)A_c)\psi_{c,\varepsilon}(t)\rangle.
\]
For a Hilbert-C1, graph-continuous path, the difference of the fixed-L_c
quadratic form is the sum pairing the vector difference with L_c psi
at the two nearby times. Its derivative is \(2\operatorname{Re}
\langle\psi',L_c\psi\rangle\). The bounded term involving j is AC.
The two Schrodinger terms cancel, leaving
\[
 q_c'(t)=-\varepsilon j'(t)a_{\varepsilon,c}(t)
 \quad\text{almost everywhere}.                     \tag{56}
\]
This also proves absolute continuity through its integrated identity.
No L_c A_c, D(L_c squared), or derivative of L_c psi is used.

The cyclic endpoints and initial ground give the actual final excess
\[
 \mathcal D_c(\varepsilon,j)
 =\langle\psi_{c,\varepsilon}(T),L_c\psi_{c,\varepsilon}(T)\rangle
 =-\varepsilon\int_0^T j'(t)a_{\varepsilon,c}(t)\,dt\ge0. \tag{57}
\]
Nonnegativity is the final ground property, not a pointwise sign of work.
Since \(\int j'=0\), the same integral may use
\(a_{\varepsilon,c}(t)-a_{0,c}\).
Equation (21) and unitarity give
\[
 \|U_{I,c}(t)-I\|\le|\varepsilon|aJ(t),\qquad
 |a_{\varepsilon,c}(t)-a_{0,c}|
                          \le2|\varepsilon|a^2J(t).
\]
Therefore, at every finite real amplitude,
\[
 0\le\mathcal D_c(\varepsilon,j)
 \le\min\bigl(|\varepsilon|aV_j,\ 2\varepsilon^2a^2B_j\bigr)
 \le\min\bigl(|\varepsilon|aV_j,\ 2\varepsilon^2a^2JV_j\bigr).
                                                               \tag{58}
\]
The energy is not asserted to be exactly quadratic. Its existence and
finiteness were proved before any bounded-state comparison.

Returning to the actual free operator, \(G_c=H_c+V_c\), \(E_c\le K\)
and (2) imply
\[
 \langle H_c\rangle_{\rm final}\le2K+\mathcal D_c,\qquad
 \langle N_{H,c}\rangle_{\rm final}
                     \le(2K+\mathcal D_c)/\Lambda_c. \tag{59}
\]
During the pulse the same work identity gives
\[
 \langle H_c\rangle_t
 \le2K+|\varepsilon|a\,[V_j(t)+|j(t)|].              \tag{60}
\]
After the source vanishes, autonomous G_c evolution preserves the actual
excess for every waiting time and hence preserves (59). It need not
preserve H_c or N_H separately. These caps alone do not compare
nonequilibrium states uniformly over diverging waiting times.
If epsilon tends to zero at a fixed pulse, the state stays even and
its weight outside the ground is at most \(\mathcal D_c/\Delta\).
A fixed finite energy cap alone is not a vanishing-excess condition.

The sufficient temporal class includes finitely many AC pieces and finitely
many jumps, with source zero before and after the interval. Let dj be the
distributional derivative including both endpoint jumps, and use
\[
 V_j=|dj|([0,T]),\quad
 B_j=\int_{[0,T]}J(t)|dj|(dt),\quad
 C_j=\int_{[0,T]}J(t)^2|dj|(dt).                     \tag{61}
\]
On each continuous piece section 7 applies. At a jump the state is
continuous and in the same D(G_c) on both sides; the instantaneous
Hamiltonian energy changes by
\(-\varepsilon\Delta j\,a_{\varepsilon,c}(t)\).
Summing the finite pieces and jumps proves
\[
 \mathcal D_c(\varepsilon,j)
       =-\varepsilon\int_{[0,T]}a_{\varepsilon,c}(t)\,dj(t). \tag{62}
\]
The integrand is continuous even at a jump, so no left/right state
convention is hidden. The total derivative mass is zero. Bounds (58)
remain valid with (61); (60) uses the accumulated variation including
jumps up to the chosen side of t. Piecewise domain propagation, not a
distributional Hamiltonian kick, underlies this statement.

For example j=h on (0,T), zero outside, has endpoint masses h and -h:
\[
 \mathcal D_c=\varepsilon h[a_{\varepsilon,c}(T)-a_{0,c}],
 \qquad 0\le\mathcal D_c\le2|\varepsilon h|a.          \tag{63}
\]
Finite evolution under \(G_c-\varepsilon hA_c\) preserves the common
domain. A finite rectangular pulse is not an instantaneous exponential
of A_c. General BV profiles with infinitely many jumps or singular
continuous derivative are outside this propagation proof.

## 9. Positive absorption coefficient without an unfiltered first moment

Insert the bounded readout expansion (23) into the exact work identity.
For either (48) or the finite-jump class,
\[
 \mathcal D_c(\varepsilon,j)
          =\varepsilon^2\mathcal Q_c(j)+\mathcal R_c(\varepsilon,j),
\]
\[
 |\mathcal R_c(\varepsilon,j)|
 \le2|\varepsilon|^3a^3e^{2|\varepsilon|aJ}C_j
 \le2|\varepsilon|^3a^3V_jJ^2e^{2|\varepsilon|aJ}.    \tag{64}
\]
This is a uniform O(|epsilon| cubed) bound at a fixed pulse. It derives
from bounded work rather than differentiating an uncontrolled energy
expectation. The coefficient is
\[
 \widehat j(\omega)=\int_0^Tj(t)e^{i\omega t}dt,\qquad
 \mathcal Q_c(j)=\int\omega|\widehat j(\omega)|^2
                                      d\mathsf M_c(\omega)\ge0. \tag{65}
\]

To prove (65) before assuming any first moment, use (22) in
\(-\int r_{c,j}(t)\,dj(t)\). Fubini is justified by finite spectral
mass and the bound \(V_jJ\). For fixed omega put
\[
 F_\omega(t)=\int_0^t j(s)\sin(\omega(t-s))ds.
\]
It is C1 with derivative
\(\omega\int_0^t j(s)\cos(\omega(t-s))ds\), including for a piecewise
source. Stieltjes integration by parts, retaining endpoint terms, gives
\[
 -2\int F_\omega(t)\,dj(t)
 =2\omega\int_{s<t}j(t)j(s)\cos(\omega(t-s))\,ds\,dt
 =\omega|\widehat j(\omega)|^2.                     \tag{66}
\]
The last equality is symmetry of the square integral; its diagonal has
Lebesgue measure zero. No derivative of C_c or positive energy moment
was imported into the frequency interchange.

Integration by parts also gives for omega>0
\[
 |\widehat j(\omega)|\le\min(J,V_j/\omega),\qquad
 0\le\omega|\widehat j(\omega)|^2
       \le\min(\omega J^2,V_j^2/\omega)\le JV_j.
\]
The weight is continuous and vanishes at zero and infinite positive
frequency; its zero extension to negative frequencies is in C_0(R).
Thus
\[
 0\le\mathcal Q_c(j)\le
             a^2\min(JV_j,V_j^2/\Delta),\qquad
 \mathcal Q_c(j)\longrightarrow\mathcal Q_0(j).      \tag{67}
\]
The coefficient limit uses only the static spectral convergence (14).
It holds even when \(m_{1,0}=\infty\). Under an explicit correlation modulus,
(66) also gives
\[
 |\mathcal Q_c(j)-\mathcal Q_0(j)|
                       \le2V_jJ\,d_{C,c}(T).       \tag{68}
\]
For a rectangle, (65) reduces to
\[
 \mathcal Q_c(j)=2h^2\int
                  \frac{1-\cos(\omega T)}{\omega}\,d\mathsf M_c.
                                                               \tag{69}
\]

For a general integrable source, the bounded first Dyson term gives the
derivative of the excited final state at epsilon=0:
\[
 i e^{-iE_cT}e^{-iTL_c}\widehat j(L_c)\xi_c.          \tag{70}
\]
Its squared L_c form norm is exactly (65), possibly infinite. This is a
precise linear spectral criterion. For an L1-only profile it is not a
nonlinear domain-preserving propagation or finite-energy theorem. Nor
does temporal regularity make the unsmeared vector A_c Omega_c acquire
the missing positive moments.

## 10. Exact finite-strength continuum energy through bounded work

For this conclusion retain the compact orbit comparison (8), the embedded
ground trace bound \(2p_c\), and the same fixed pulse and source strength
at every spacing. Let \(B_c(t)=\widehat\beta_{c,t}(A_c)\) and compare the
common source unitaries, with the target unitary extended tensor I_H.
Their left-generator difference gives
\[
 \partial_t(U_{I,0}^*U_{I,c})
       =i\varepsilon j(t)U_{I,0}^*(B_c-B_0)U_{I,c},
\]
\[
 \|U_{I,c}(t)-U_{I,0}(t)\|
                  \le|\varepsilon|J(t)d_{A,c}(T).   \tag{71}
\]
Both source flows preserve their actual ranges. Their common bounded
comparison agrees with the actual protocol on those ranges. Unitarity
eliminates an exponential stability loss.

Directly telescoping the readout and ground density gives
\[
 |a_{\varepsilon,c}(t)-a_{\varepsilon,0}(t)|
       \le2a p_c+(1+2|\varepsilon|aJ)d_{A,c}(T).
\]
Using the two exact work identities proves
\[
 |\mathcal D_c-\mathcal D_0|
 \le|\varepsilon|V_j[2a p_c+(1+2|\varepsilon|aJ)d_{A,c}(T)]. \tag{72}
\]
An earlier independent improvement retains the quadratic amplitude factor.
Set
\[
 T_c^A(t)=U_{I,c}(t)^*B_c(t)U_{I,c}(t)-B_c(t),\qquad
 \|T_c^A(t)\|\le2|\varepsilon|a^2J(t).
\]
Its difference splits exactly as
\[
 T_c^A-T_0^A=
 U_{I,c}^*(B_c-B_0)U_{I,c}-(B_c-B_0)
 +U_{I,c}^*B_0U_{I,c}-U_{I,0}^*B_0U_{I,0}.
\]
The first pair costs \(2\|U_{I,c}-I\|d_A\), the second
\(2a\|U_{I,c}-U_{I,0}\|\). Thus its norm is at most
\(4|\varepsilon|aJ(t)d_A\). The initial ground-density error is at most
\(4|\varepsilon|a^2J(t)p_c\). Ground stationarity permits (57) or (62)
to use the expectation of T_c^A after subtracting the baseline. Consequently
\[
 |\mathcal D_c(\varepsilon,j)-\mathcal D_0(\varepsilon,j)|
 \le4\varepsilon^2aB_j[d_{A,c}(T)+a p_c].            \tag{73}
\]
This holds at every fixed finite amplitude, including strong pulses, and
tends to zero through all allowed spacings. The actual final mean of G_c
also converges, since E_c converges separately. No trace-norm error or
weak-measure limit was paired with an unbounded Hamiltonian: energy passage
uses the exact bounded-work identities.

There is a distinct joint weak-source consequence requiring only the static
spectral hypotheses. For a fixed pulse and any nonzero epsilon(c)->0,
(64) and (67) give
\[
 \frac{\mathcal D_c(\varepsilon(c),j)}{\varepsilon(c)^2}
                    \longrightarrow\mathcal Q_0(j). \tag{74}
\]
The remainder divided by epsilon squared is bounded by a constant times
|epsilon| at this fixed pulse. Finite-strength convergence (73) uses the
orbit premise; coefficient convergence (74) does not.

For j or T depending on c, their actual displayed resources and moduli
must make the chosen estimate vanish. In particular (73) would require
its \( \varepsilon(c)^2 B_{j_c}
[d_{A,c}(T(c))+a p_c]\) factor to tend to zero. This is a sufficient
certificate, not a necessary characterization. Arbitrary autonomous final
waiting times leave the excess and (72)-(74) unchanged. They do not give
uniform convergence of the resulting nonequilibrium states or of readouts
on unrestricted growing time windows.

## 11. Actual rough impulse controls, including the joint limit

Use the free example of section 5 and normalize g so \(\|f\|=\|g\|=1\).
For all sufficiently small c its disjoint cell supports give
\[
 A_c=i\gamma(C_cf)\gamma(C_cg),\quad \|A_c\|\le1,\quad
 A_c^2=n_c^2I,\quad
 n_c=\|C_cf\|\,\|C_cg\|\longrightarrow1,\qquad A_0^2=I. \tag{75}
\]
Here n_c is a coefficient norm product, not a particle-number observable.
We have \(A_0\Omega\notin D(H_0^{1/2})\),
\(m_{1,c}<\infty\) at fixed c, and \(m_{1,c}\to\infty\).

An ideal distributional source \(-\theta\delta(t)A\) prescribes the distinct
kick \(e^{i\theta A}\). In the target,
\[
 e^{i\theta A_0}\Omega
      =\cos\theta\,\Omega+i\sin\theta\,A_0\Omega.      \tag{76}
\]
For \(\theta\notin\pi\mathbb Z\) this vector lies outside the free form
domain: otherwise subtracting its vacuum part and dividing by the nonzero
coefficient would put A_0 Omega in that linear domain. At theta in pi Z
the target ideal kick is a scalar vacuum. At every small fixed c the kick
has only zero/two-particle components and finite actual energy,
\[
 \mathcal D_c^{\rm kick}(\theta)
       =\frac{\sin^2(\theta n_c)}{n_c^2}\,m_{1,c}.    \tag{77}
\]
Thus for fixed nonexceptional theta it diverges as c decreases. These
statements concern energy domains, not existence of the bounded unitary.
No conclusion at exceptional amplitudes is extrapolated to other limits.

Approximate the impulse by real smooth finite pulses: choose
\(k\in C_c^1((0,1))\) with \(\int k=1\), and put
\[
 j_\sigma(t)=\sigma^{-1}k(t/\sigma),\quad 0\le t\le\sigma,
 \qquad\varepsilon=\theta.                           \tag{78}
\]
Each finite sigma pulse has finite actual energy, uniformly in c at that
fixed sigma. However
\[
 J=\|k\|_1,\qquad V_{j_\sigma}=\|k'\|_1/\sigma.
\]
The fixed-pulse energy and remainder constants need not stay bounded.
For the target quadratic coefficient,
\[
 \mathcal Q_0(j_\sigma)=
 \int\omega|\widehat k(\sigma\omega)|^2\,d\mathsf M_0
                        \longrightarrow\infty.      \tag{79}
\]
Pointwise \(\widehat k(\sigma\omega)\to1\); Fatou and \(m_{1,0}=\infty\)
prove this without monotonicity or a divergence rate. It does not prove
fixed-strength energy divergence by itself, since (64) is not uniform in
sigma.

For exact target energy, rescale the bounded interaction equation to u=t/sigma.
Its generator is \(i\theta k(u)\beta_{\sigma u}(A_0)\). The rough finite
CAR polynomial has a point-norm continuous free orbit, since its L2
coefficient orbits are strongly continuous. The unitary stability estimate
therefore gives \(U_I(\sigma)\to e^{i\theta A_0}\) in norm. Free strong
continuity on the fixed kick vector gives convergence of the physical final
vectors to (76). Every finite-sigma vector belongs to D(H_0). At each fixed
R the bounded positive cutoff \(\min(H_0,R)\) has convergent expectations.
Actual energies dominate them, and the limiting cutoff expectations grow
without bound. Hence, for theta not in pi Z,
\[
 \mathcal D_0(\theta,j_\sigma)\longrightarrow\infty.  \tag{80}
\]
This uses the exact finite-strength state, not an extrapolated response
coefficient or a trace-distance energy bound.

There is also a direct actual joint limit. On the common carrier define
\[
 W_{c,\sigma}=\widehat\beta_{c,-\sigma}(U_{I,c}(\sigma)).
\]
The physical final vector is \(W_{c,\sigma}\Omega\), up to its ground phase;
in this free example the common vacuum and its zero energy agree at every c.
The rescaled left generator of W at intermediate u is
\(i\theta k(u)\widehat\beta_{c,\sigma(u-1)}(A_c)\). For sigma<=1,
\[
 \|W_{c,\sigma}-e^{i\theta A_0}\otimes I_H\|
 \le|\theta|\|k\|_1\left[
 d_{A,c}(1)+
 \sup_{|t|\le\sigma}\|\beta_{0,t}(A_0)-A_0\|\right]\longrightarrow0.
                                                               \tag{81}
\]
This uses a fixed compact orbit window, including negative times; it
does not multiply that error by \(V_{j_\sigma}\).
On the actual ranges, (3) implies that each actual energy dominates the
expectation of every bounded cutoff
\(\min(H_0\otimes I_H,R)\). Norm convergence from (81) passes each cutoff
expectation to the high-vacuum embedding of (76). Then R tending to
infinity proves
\[
 \mathcal D_c(\theta,j_\sigma)\longrightarrow\infty
 \quad\text{along every joint }c\to0,\ \sigma\to0,\quad
 \theta\notin\pi\mathbb Z,                           \tag{82}
\]
for this strict rough ordinary-cell example. All finite-c, finite-sigma
energies are finite. This proves no divergence rate, no assertion at
exceptional amplitudes, and no obstruction for smoother observables.
It uses both actual bands and the actual form lower bound, not an
interchange of two unbounded energy limits.

The exact zero-absorption control is
\[
 A_c\Omega_c=a_{0,c}\Omega_c.                        \tag{83}
\]
The source then changes only the ground phase:
\(\psi(t)=e^{-iE_ct+i\varepsilon a_{0,c}\int_0^t j}
\Omega_c\). Thus the excitation measure, pulse coefficient and exact final
excess all vanish. A=I is one example. This explicit eigenvector condition
replaces ambiguous wording about commuting on a rough ground vector;
no automatically defined unbounded commutator is inferred.

## 12. Scope, open obligations and exact-source provenance

The static results use the supplied actual model, small total K, static
resolvent/ground comparison and time-zero observable/potential convergence.
The explicit orbit-resolution and exact finite-strength inter-spacing
bounds additionally use (8). Positive moments have the domains in (33)-(35),
with H1 a sufficient concrete class. Pulse domain propagation and work use
(48) or the finite-jump extension, and an exact initial ground. Bounded
L1-only readout dynamics is a weaker assertion.

The earlier preparation theorem provides a controlled approximate ground
protocol, with its own actual excess bounds. It does not give the exact
ground at a finite ramp time. This note uses its common-domain machinery
and the specified exact-ground pulse initial condition; it makes no new
finite-ramp-error composition claim. A quantitative pulse theorem for such
approximate initial states would require its own explicitly stated error
and energy argument.

Other named limits of coverage are: stronger spectral topology for strictly
compact-spatial potentials; nonlinear energy propagation for general L1-only
or arbitrary infinite-jump/singular-continuous BV profiles; unrestricted
joint zero frequency resolution or growing time windows; higher moments
with rough interactions; and optimal temporal regularity or impulse rates.
The narrow counterexamples above are literal examples with their stated
classes, not exhaustive route elimination or global no-go results.

Nothing here derives a physical source, coupling, scalar mediator, new
particle identity, Lorentz mass, empirical force law, extensive interaction,
autonomous relaxation or three-dimensional microscopic theory. The current
conditional model retains its open parent dependencies. Time-average
observable constructions and spatial/local-ground research are not part of
this synthesis.

All newly exposed argument bodies were read completely before drafting.
The following originals are unchanged and copied into
excitation_response_pulse_synthesis/inputs:

| Source | SHA-256 | Scope |
|---|---|---|
| GROUND_SPECTRAL_RESPONSE_INDEPENDENT.md | e4a0f999ffc4cffd6ca53476a047acfd08de284444f02de8698f754cfa8a4d8d | 717-line independent-before-comparison core: static spectral route, even gap, H1 class, actual moving atom |
| GROUND_SPECTRAL_RESPONSE_ROOT_PROBE.md | d51bb0961d55e5b336570784f4f2d19964bd9ff1cc07439146f31b24c3fbdcdf | 271-line root core: response conventions, static bound, Fourier route, abstract topology control |
| GROUND_STATIC_RESPONSE_ROOT_ADDENDUM.md | 19d1c72220146f2e271465083260f97f4d363fcf7fc5f6bf6be12115554a761a | 51-line static curvature argument |
| GROUND_SPECTRAL_RESPONSE_CROSSCHECK.md | 10c2bdb8e6e2ee65c0f85184cabc01f101f77b5b8ad1dcd3825e212fa9a9b185 | 433-line source-exposed comparison; no theorem-invalidating finding; preserves scope differences |
| SMOOTH_PULSE_ENERGY_INDEPENDENT.md | 3be0730d252ce52280e50fb629e369b062b10a5b77cc036eac1bba9b65e001e6 | 580-line independent-before-comparison core: AC/finite-jump proof, refined constants, actual joint impulse limit |
| SMOOTH_PULSE_ENERGY_ROOT_PROBE.md | 60684f3d3986a70314b34245f30ed5ee0c32d8f1cb67aa3e25c9df666afd53e8 | 291-line root core: C1 pulse/work theorem, coefficient modulus, during-pulse and high-band caps |
| SMOOTH_PULSE_ENERGY_CROSSCHECK.md | ce644c7d6f8e71aa07821e41d2a076599015c62ee6c5e172e62be0fcdb8abcf4 | 480-line source-exposed comparison; no required theorem repair; exact domain and control qualifications |
| SMOOTH_PULSE_CONTROL_WORDING_ADDENDUM.md | d6107c80c7f4c40a1f95b73a403d78050ecd5e23753cee0076a935b457ba3e54 | Explicit A Omega=a0 Omega control used in (83) |

The spectral independent freeze preceded its root-body exposure, and the
pulse independent freeze preceded its root-pulse exposure, as recorded in
their completed comparisons. Those are ordinary separate derivations with
shared model-family and premise limits. This author read both sides and
their comparisons for the present assembly; no new independence claim
arises from combining them. Historical pending-status sentences in the
original cores remain preserved as historical source text.

The reusable parents are pinned at their unchanged identities:

| Parent | SHA-256 | Reused coverage |
|---|---|---|
| BOUNDED_INTERACTION_GROUND_SYNTHESIS.md | b8bcba769100bf819885937d850a7bff8543e4233c1df3cf65f68372552160e9 | Complete prior read: actual bands, static ground/resolvent and orbit premises, rough-domain construction |
| ADIABATIC_PREPARATION_SYNTHESIS.md | 6d82cfece7f56a333c3583fa7e97b1b2e38edd5c414893ba128e70a74c60ba7c | Complete prior read; common-domain weak-to-strong construction, used within section 7's reproduced AC argument |
| ADIABATIC_PREPARATION_SYNTHESIS_REVIEW.md | fe3aa3cde43c557609b66b589ac49d16c3f9f8207f0d75ff0ff3a1cf3d692245 | Complete prior read; analytic scope and later citation corrections |
| CURRENT_PRESERVING_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md | 763082a6faa8bea3f6be74ddc7ee81bf288c00740085804e62f701a1576283ff | Complete prior read; actual symbol refreshed, C14/C21/C25 reused; open_gate |
| LOCAL_EVEN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-10-12.md | b5a8394a9d8c17bb9559597a68b061ad3872201ebf9793bd5c9f10b15ac2c6aa | Complete prior read; cell contraction and graph passage refreshed; L23-L24 identification reused |

Root supplied the PR9502 publication context. The current canonical
conditional-support ground note has SHA-256
8454f1c88d5d6c05910b5d7fd1ec34d454118c4b41ad3d930a339c77c97c45b2;
the preparation note has
dd2862222f8501620d97adbac6ff2c2f38751a24043e09c34acc8bc6c162dfca.
Their publication headers were inspected and full copies are pinned as
provenance only. The mathematical dependencies above remain the named
frozen original assemblies. Historical wrapper/pending language does not
constitute a new status determination. Their identity/reconstruction tools
execute zero mathematical predicates; none was run for this task.

Equation (28) is checked analytically by multiplication here. Prior formal
records distinguish a finite Clifford identity from a finite compressed-
resolvent algebra identity. Neither is an analytic formalization of the
spectral, unbounded-domain, positivity, convergence or pulse theorems.
No formal artifact or compilation is used as a load-bearing premise of
this note, and no new numerical, symbolic or formal execution occurred.

The evidence directory contains the early neutral plan, exact input copies,
complete new-read and reused-coverage record, the final author self-check,
an immutable output copy and the source/hash seal. Hashes identify the
argument versions; they are not mathematical evidence. The selected
inherited model and effort were unchanged. No original core, canonical
source, publication package, repository, Git/PR/audit state, editable prompt,
physical axiom or campaign checkpoint was changed, and no delegation or
other-chat messaging occurred.

## Publication dependencies and limits

The four direct parents are the [bounded-interaction and ground theorem](BOUNDED_INTERACTION_GROUND_BOUNDED_THEOREM_NOTE_2026-10-12.md),
the [adiabatic preparation theorem](ADIABATIC_GROUND_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-12.md),
[Current](CURRENT_PRESERVING_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md), and
[Local Even](LOCAL_EVEN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-10-12.md).
The first supplies the actual bands, bounded-interaction ground comparison and
full-Fock representation. The second supplies the common-domain construction
used in the pulse proof; it does not replace this note's exact initial ground
by a finitely prepared approximate ground. Current supplies the actual free
symbol and C21/C25 comparison, and Local supplies the ordinary physical-cell
and even-spin interpretation and graph-consistency premises.

The first two canonical parents are conditional proposals in OPEN PR9502 at
the stacked base `ba3ea535fa5ce80a3ad81b384a2063185da42756`; their inherited
correlation parent is also provisional. They are not main or retained authority.
Current remains open_gate. Main premise bytes are those of
`516cb69d8487ff04f8a48e065d3dcbe71d7dd237`. The exact canonical parent bytes and
the underlying frozen source assemblies are archived. Their later finite
formal/ramp appendices are not additional analytic premises of this note.

The theorem retains the supplied Hamiltonians and identifications, small total
bounded interaction, exact initial ground, bounded even observable and stated
real source convention. Static spectral convergence and quantitative orbit
comparison have distinct hypotheses. Full-space and even-excitation gaps,
unital observable extensions, physical-range projections, high-vacuum
projections, ground projections and zero-extended compressed resolvents remain
distinct. No compression kernel is assigned a physical zero-energy sector.

The H1 ordinary-cell moment result has its graph argument. Rough compact L2
cells can have infinite target energy moments despite finite actual-spacing
moments. The moving-atom obstruction to stronger spectral topology uses the
stated general in-band potential with noncompact spatial tails; it does not
settle that topology for strictly compact-spatial interactions.

Actual work and free/high-band caps apply to the specified norm-AC controls
and finitely many AC pieces and jumps, including endpoint jumps. General BV
source propagation is not added. Exact finite-strength work bounds, weak-source
filtered coefficients and the joint impulsive counterexample have their own
quantifiers. The zero-control condition is the explicit bounded eigenvector
condition A Omega = a0 Omega. A distributional kick is not substituted for
finite-duration evolution. Autonomous hold energy control does not supply
unrestricted long-time continuum readouts; fixed compact observation windows
and all stated orbit resources remain in force.

The [No-Go Discipline Gate](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/f055a7bee614bd614cf3d387ec60804eb9f7597b/.claude/science/physics-loops/toe-response-transfer-20261012/NO_GO_DISCIPLINE_CHECKLIST.md)
keeps N1 and N5 pending. Literal counterexamples refute only the named stronger
implications. No five-route exhaustion, global obstruction, new physical axiom,
empirical prediction, audit verdict or retained promotion is claimed. No
finite algebra identity is treated as formalization of the analytic proofs.


Review-loop integration note: PR9500 and PR9502 are now landed on main through 9a96afddaf66d0921dc0e2656460025498d312bc. Their analytic proofs remain unchanged; publication links, two Local support citations and integration provenance were corrected. Live parent pins are refreshed in PARENT_BINDINGS.json with the original pins retained. Earlier OPEN/main statements above are publication-time history, not current status or audit authority.
