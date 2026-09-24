---
claim_id: charged_record_exchange_band_field_response_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Conditional mathematics of the explicitly supplied finite model and stated ordered limits; historical numerical tables are author observations, with fresh controls separately identified below."
upstream_dependencies:
  - minimal_axioms
  - homogeneous_mobile_charged_records_and_field_dynamics_bounded_theorem_note_2026-09-24
runner: scripts/charged_record_exchange_band_field_response_2026_09_24.py
---

**Type:** bounded_theorem
**Status:** conditional mathematical construction; unaudited.

The complete source argument below is preserved from the frozen submission. Its dated author-status statements and historical execution tables describe that submission, not an independent audit verdict. Quantum laws, enlarged site/link memories, Hamiltonians, instruments, backgrounds and preparations are supplied mathematical model assumptions. They are not new repository axioms or framework primitives. Fresh execution of the canonical runner checks the stated finite controls; finite tests alone do not establish the general proofs or limits.

# The charged-record exchange band's restoring field response

2026-09-22. Author proof and exact finite controls; independent reconstruction
pending. This note analyzes the specific interacting rotor target proposed in
HOMOGENEOUS_MOBILE_CHARGED_RECORDS_AND_FIELD_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md. Its microscopic
derivation is a separate, currently provisional dependency. The present
potential-band calculation can instead be read directly as a theorem about
the explicitly supplied target below.

**Finding.** The lowest matter-potential band at zero angle has positive
curvature in every physical gauge-field direction, including uniform flat
connections. There is a volume-independent lower curvature bound. A separate
fixed-box cutoff-packet argument gives massive harmonic oscillations in this
band's ordered weak-kinetic limit. This does not prove the phase diagram or
a gap of the complete quantum many-body Hamiltonian uniformly in volume.
It does rule out simply transferring the neutral model's soft-photon packet
argument to this particular charged band's minimum.

## 1. The precise target and its finite matter matrix

Use the same d>=2 cubic even torus, all periods >=6. Put n=V/2, which is even.
The A sites are occupied by permanent records of charges q_a=+1 or -1 with
sum q_a=0; B sites are empty. Integer rotor links obey div E=q. The proposed
target is

\[
 H=K\sum_e E_e^2-J\sum_p(R_p+R_p^\dagger),\qquad K,J>0. \tag{1}
\]

For a cyclic plaquette a,b,c,d, a,c in A, R_p exchanges the A records by
a->b->c and c->d->a, with their actual charges shifting the links. Nothing
in this calculation changes a record's content. In angle coordinates A_e,
write the directed path integrals

\[
 X_p=A_{ab}+A_{bc},\quad Y_p=A_{cd}+A_{da},\quad
 \phi_p=X_p+Y_p,\quad \theta_p=(X_p-Y_p)/2.              \tag{2}
\]

Thus phi=C A is the ordinary curl and theta=Theta A is the average of the
two a-to-c paths. If a stored edge orientation disagrees with a path, use
its negative angle. The two A endpoints determine an oriented diagonal
graph edge with incidence (D f)_p=f_c-f_a. A full vertex gradient Gf obeys

\[
 C G=0,\qquad \Theta Gf=D(f|_A).                        \tag{3}
\]

At fixed link angles the magnetic term is a finite Hermitian matrix
V_J(A) in the zero-total-charge record space. In the pair basis its exact
plaquette expression is

\[
 V_{J,p}(A)=-J\left[
    (1+q_aq_c)\cos\phi_p+
    2\{\tau_a^-\tau_c^+e^{-2i\theta_p}
        +\tau_a^+\tau_c^-e^{2i\theta_p}\}\right].
                                                               \tag{4}
\]

Here tau^+ takes - to + at a fixed location. In (4) it always appears with
tau^- at the other location: the combined term exchanges the two permanent
records. It does not describe a charge-flipping event for one record.

The equal-charge sectors have phases e^(+-i phi). For opposite charges the
two directed routes lead to the same joint final state, so their amplitudes
add to the factor two in (4). At A=0,

\[
 V_J(0)=-2J\sum_p {\sf Swap}_{a(p),c(p)}.                \tag{5}
\]

The diagonal A graph is connected: its lattice translations e_i+-e_j generate
the even-sum sublattice, including 2e_i, and the periods are even. On a connected
graph adjacent transpositions generate all permutations. Each swap has norm
one; a normalized vector reaches the lower energy -2J P, P the plaquette
count, exactly when it is fixed by every swap. In the fixed charge-count
sector that common space is one-dimensional, the uniform Dicke vector u over
all n/2-plus words. The remaining finite matrix spectrum is separated by a
strictly positive gap. No bound on that full matter gap uniform in volume is
needed or asserted.

Consequently the lowest eigenvalue lambda_J(A) and its eigenvector are
analytic near zero on every fixed box. Complex conjugation sends A to -A,
so lambda_J is even there. Denote the Hessian by M_J.

## 2. Exact Hessian, including matter relaxation

For an arbitrary real angle direction a, put phi=C a and theta=Theta a.
Let L_A=D^T D and P_cyc=I-D L_A^+ D^T. Then

\[
 a^T M_J a
 = J\frac{n-2}{n-1}\|C a\|^2
   +4J\frac{n}{n-1}\|P_{\rm cyc}\Theta a\|^2.           \tag{6}
\]

In particular, freezing the record vector and evaluating only its direct
second derivative would overestimate the answer by omitting relaxation.
The projection in (6) is that relaxation exactly, rather than a heuristic
choice of a record phase.

To derive it, all expectations in this paragraph are in u. The fixed-count
two-site correlations are

\[
 \langle q_aq_c\rangle=-1/(n-1)\quad(a\ne c),\qquad
 \langle\tau_a^-\tau_c^++\tau_a^+\tau_c^-\rangle
       =n/[2(n-1)].                                   \tag{7}
\]

Both follow by counting the uniform words; diag <q_a^2>=1.
Writing V' and V'' for derivatives along a, (4) gives

\[
 V'u=2iJ\sum_a(D^T\theta)_a q_a u,\qquad
 \langle V''\rangle
  =J\frac{n-2}{n-1}\|\phi\|^2
       +4J\frac{n}{n-1}\|\theta\|^2.                    \tag{8}
\]

The space of vectors q[f]u=sum_a f_a q_a u is invariant under V(0).
It has inner product n/(n-1) f^*P_0 g, where P_0 removes constants.
The permutation action gives the exact identity

\[
 [V_J(0)+2JP]q[f]u=2Jq[L_A f]u.                       \tag{9}
\]

Since D^T theta has zero sum, the reduced inverse needed for V'u is
(2J L_A)^+ on precisely this subspace. The simple-eigenvalue derivative
identity is obtained by differentiating (V-lambda)u=0 twice with normalized
u and <u,u'>=0:

\[
 \lambda''=\langle V''\rangle
       -2\langle V'u,[V(0)-\lambda(0)]_\perp^{-1}V'u\rangle.
\]

Equations (7)-(9) turn the second term into
4Jn/(n-1) theta^T D L_A^+D^T theta. Subtraction proves (6).
This derivation needs no claim about the rest of the ferromagnet spectrum.

## 3. A uniform geometric curvature bound

Let P_T be the orthogonal projection onto the full transverse link space
T=(range G)^\perp. This includes d harmonic constant directions; they are
physical, not vertex gauges. Define

\[
 F(a)=\|Ca\|^2+4\|P_{\rm cyc}\Theta a\|^2
     =\min_{f_A}\{\|Ca\|^2+4\|\Theta a-Df_A\|^2\}.       \tag{10}
\]

The exact local-star bound is

\[
 4(d-1)\|P_Ta\|^2\ \le F(a)\le 4d\|P_Ta\|^2.           \tag{11}
\]

Here is a proof valid for every allowed box. For each plaquette, the expression
inside (10) is

\[
 (X+Y)^2+(X-Y-2Df_A)^2
      =2[(X-Df_A)^2+(Y+Df_A)^2].
\]

The two squares are the two two-link paths connecting its A vertices through
its B corners. At a fixed B vertex b, its 2d A neighbors form a graph with all
pairs except opposite-direction pairs: the complete multipartite graph
K_(2,2,...,2). For an A neighbor a define
u_a=a_(a->b)+f_A(a). A two-link path a->b->c has adjusted angle u_a-u_c.
Thus

\[
 F(a)=2\min_{f_A}\sum_{b\in B}u_b^T L_{\rm star}u_b.     \tag{12}
\]

The star Laplacian has eigenvalues 0, z-2 and z: constant vectors have zero,
antisymmetric vectors within the d opposite pairs have z-2, and pair-constant
vectors whose pair values sum to zero have z. Therefore

\[
 (z-2)\min_s\sum_a(u_a-s)^2
 \le u^T L_{\rm star}u
 \le z\min_s\sum_a(u_a-s)^2.
\]

After minimizing over f_A and the independent constants s=f_B(b), the sum
of squared differences is exactly min_f ||a-Gf||^2=||P_Ta||^2.
The lower bound follows by minimizing both sides. For the upper bound use
the f_A,f_B that minimize this full least-squares problem before applying
the upper inequality in (12). Multiplying by two proves (11).

Since (n-2)/(n-1) <= n/(n-1), (6) and (11) give

\[
 4J(d-1)\frac{n-2}{n-1} P_T
 \ \le M_J\le\
 4Jd\frac{n}{n-1} P_T                               \tag{13}
\]

as quadratic forms; both sides vanish on vertex gradients. This controls
every physical direction, not merely one special plane wave. For all
allowed boxes n>=18, so the lower bound remains separated from zero
uniformly in volume. It is a bound on a potential-band Hessian, not on the
spectrum of the full kinetic Hamiltonian.

For a constant link connection a_(x,i)=v_i, C a=0. The opposite diagonal
orientations cancel in D^T Theta a, and summing the two diagonal choices
of each coordinate pair yields

\[
 \|\Theta a\|^2=(d-1)\|a\|^2,\qquad
 M_J a=4J\frac n{n-1}(d-1)a.                           \tag{14}
\]

Thus even uniform flat connections have positive curvature. The extra
term in (6) cannot be absorbed into a curl-square coefficient.

## 4. A fixed-box physical packet statement

This section addresses what the potential result does and does not imply
for the full quantum dynamics. It supplies one ordered finite-box packet
limit, with constants permitted to depend on the box. It does not interchange
a thermodynamic limit with weak coupling.

Fix a box and put

\[
 K=\omega_0 h,\quad J=\omega_0/h,\quad
 h=\sqrt{K/J}\longrightarrow0,\quad \omega_0>0.         \tag{15}
\]

Let M=M_J/J from (6), independent of J. On the gauge quotient T, define the
strictly positive oscillator

\[
 H_{\rm osc}=\omega_0[-\Delta_x+\tfrac12 x^T Mx].
                                                               \tag{16}
\]

The frequencies are omega_l=omega_0 sqrt(2 mu_l), where mu_l are the
eigenvalues of M restricted to T. Equation (13) gives

\[
 \omega_l\ge\omega_0
   \sqrt{8(d-1)(n-2)/(n-1)}.                           \tag{17}
\]

There are (d-1)V+1 physical coordinates, including the harmonic ones.

To construct a legitimate Gauss state, first work in a small injective
chart of the full compact vertex-gauge quotient, not the smaller neutral
quotient that removed global electric flux. Its real tangent space is T
and its lattice is 2pi P_T Z^M; its discreteness follows from the rational
matrix of the finite integer gradient projection. For every charge word q
choose any integer link flow e_0(q) with div e_0=q. Such a flow exists because
the total integer charge is zero on a connected graph. Split it as

\[
 e_0(q)=E_L(q)+\alpha(q),\qquad
 E_L(q)=B^T(BB^T)^+q,\qquad \alpha(q)\in T.
\]

The electric spectrum in that component is e_0(q)+Lambda_T with
Lambda_T=ker B intersect Z^M. On the quotient this is a flat, possibly twisted
line bundle. In a local parallel frame its kinetic operator is exactly

\[
 -K\Delta_T+K q^T(BB^T)^+q.                             \tag{18}
\]

The twist only specifies how the local section is extended between charts.
The Coulomb term in (18) is a finite diagonal matter matrix for this fixed
box. The magnetic matrix in this parallel frame is (4), because it shifts
the electric field by the actual path current. Gauge covariance gives the
same statement directly by restricting the original angle wavefunction
to T. No external continuous charge source is substituted for the records.

Let u(A) be the normalized analytic eigenvector of V_1(A), chosen by
normalizing its Riesz projection applied to the real Dicke vector u(0);
its overlap with u(0) is positive near zero. All of its derivatives needed
below are bounded on a sufficiently small fixed chart. The simple band and
reality symmetry give

\[
 \lambda_1(A)=-2P+\tfrac12 A^T M A+O_V(|A|^4).
                                                               \tag{19}
\]

Choose a smooth cutoff chi supported in that chart and equal to one near
zero. For a normalized finite Hermite combination psi of (16), prepare
the actual compact bundle section

\[
 I_h\psi(A)=h^{-r/4}\chi(A)u(A)\psi(A/\sqrt h),
 \qquad r=(d-1)V+1,                                    \tag{20}
\]

and extend it by the bundle identifications. It vanishes near the chart
boundary, so it is unambiguously defined and smooth on the compact
configuration space. Its norm is 1 plus an exponentially small correction.
Its lift satisfies Gauss exactly. It does not assume a product state
between matter and field.

Subtract the scalar -2JP from (1). Under A=sqrt(h)x the kinetic action on
(20) gives the intended -omega_0 Delta_x psi plus

\[
 -2\omega_0\sqrt h\,(\nabla_Au)\cdot\nabla_x\psi
       -\omega_0 h\,(\Delta_Au)\psi,                    \tag{21}
\]

with chi inserted. Terms differentiating chi are exponentially small,
since the evolving finite Hermite packet has Gaussian tails uniformly
on fixed times. Equation (19) gives potential residual
O_V(omega_0 h)|||x|^4 psi||. The Coulomb matrix (18) contributes
O_V(omega_0 h)||psi||. Derivatives of u in (21) are bounded on the chart,
so the leading residual is O_{V,psi,T}(sqrt h). Outside the chart the
cutoff is zero. No assumption of an exact adiabatic following law is used.

Each fixed-h full compact Hamiltonian is self-adjoint: its component
twisted Laplacians have the usual domains, (18) has finite matter norm,
and (4) is bounded. The oscillator has its standard Hermite core.
Differentiating the Duhamel intertwiner and normalizing (20) therefore gives

\[
 \sup_{0\le t\le T}
 \|e^{-it(H+2JP)}I_h\psi/\|I_h\psi\|
      -I_h e^{-itH_{\rm osc}}\psi/
               \|I_h e^{-itH_{\rm osc}}\psi\|\|
 \le C_{V,\psi,T,\omega_0}\sqrt h.                      \tag{22}
\]

This suffices for bounded physical readouts. The initial state is a
specifically prepared band packet. Constants include derivatives of u,
which depend on the finite matter gap; no volume-uniform estimate is
claimed in (22). Improving the power by adding excited-band corrections
is possible in principle but is not needed or asserted here.

At fixed box and h, (20) has finite electric moments of all orders.
Projection to spin intervals preserves Gauss and charge counts and converges.
Thus the preceding microscopic charged-record theorem, if independently
confirmed, can be composed first at S->infinity for fixed h and box.
Only then take h->0 in (22). Positive microscopic birth rates in that
first limit follow its declining beta schedule, not a new finite-density
production theorem.

Equation (17) describes massive harmonic response in this particular
prepared-band limit. At the neutral model's continuum normalization
omega_0=c/(2a), its lower frequency grows at least as a positive multiple
of c/a. The neutral packet argument, which instead produces omega~c|k|,
therefore cannot be copied into this charged band. This observation says
nothing about all possible initial bands, other coupling paths, or
intermediate-coupling phases of (1).

## 5. Controls and limits of independent evidence

charged_record_potential_hessian_check.py builds (4) directly from record
permutations, without importing the microscopic runner. In fixed-zero-charge
sectors of four and six sites (dimensions 6 and 20), it computes the complete
H0,H1,H2 matrices with exact arithmetic, their reduced inverse and the
independent graph expression (6). All entries and the resulting directional
curvatures agree. The two nontrivial rational curvatures are 982/3675 and
14124/6125; two pure gradient controls have exactly zero curvature.
Separate finite-angle diagonalization at three step sizes converges to them.

The runner independently assembles full cubic incidence, curl, diagonal graph
and average-path matrices on 4^2,6^2,8^2,4^3 and 6^3 tori. It checks the
integer identities (3), the gauge kernel and the uniform-connection formula.
The smallest positive Hessian eigenvalues at J=1 are approximately
3.428571,3.764706,3.870968,7.741935,7.925234, respectively. They meet the
lower expression in (13) in those controls. On 6^3 the uniform curvature
is 8.07476635514. The finite floating spectra corroborate the algebra and
are not interval enclosures.

Two-mode Fourier Ritz probes are explicitly marked as probes. In d=3 the
chosen two-dimensional subspaces have nonzero leakage (about .41416 at
side six), so their displayed Ritz values are **not** asserted to be
dispersion eigenvalues. The all-direction analytic bound (13) avoids
that insufficient ansatz. No result is inferred from suppressing this
leakage. The runner passed on its first execution, with complete source,
results, stdout, empty stderr and receipt retained.

The packet argument (18)-(22) has not received an independent reconstruction
or a full microscopic dynamics simulation. It is an additional author
proof, not a numerical consequence of the finite Hessian matrices.

charged_band_packet_check.py separately evolves a compact one-coordinate,
six-component matrix model with four fixed-count records on a cycle. Only
one exchange edge carries theta; phi is zero. This auxiliary model has
exact band Hessian 4/3, ||u'(0)||^2=5/12 and oscillator frequency sqrt(8/3).
Its cutoff packet has a nonzero band derivative, so it tests the
sqrt(h) residual in (21), not just a scalar cosine approximation.
For h=1/32 down to 1/256 the time-one state error decreases from .0113375
to .00142288 and satisfies the direct finite-matrix Duhamel bound.
The two residuals divided by sqrt(h) approach .824872 and 1.428720,
as predicted by the exact band derivative and oscillator derivative norms.

The first packet execution missed its declared 1e-9 cutoff-refinement target:
cutoffs 91/111 at h=1/128 differed by 1.27048e-9. A separate dense Hermitian
spectral propagator reproduced the discrepancy, while cutoffs 151/211
reduced it to 1.68e-12. The repaired runner increases the base cutoff
from ceil(8/sqrt(h)) to ceil(12/sqrt(h)) and the refinement from +20 to +60;
it keeps the original 1e-9 assertion and all scientific coefficients.
The new grid/cutoff difference is below 6.6e-13. Original source, failure,
receipts and all diagnostics remain under charged_band_source_history.
This is a numerical precision repair, not a changed theorem.
The auxiliary matrix model does not simulate the full cubic Gauss system.

charged_band_geometry_check.py additionally checks the exact local-star
eigenvalues in dimensions 2 through 6 and the periodic sign transformation
described below, including wrapping faces and both charge signs.

## 6. Scope stress test and next design decisions

The following checks apply the selected no-go discipline to the *bounded
negative inference* about this branch, without claiming a general no-go.

- **N1, alternative routes.** The neutral-background construction already has
  a positive photon-packet result. Within a charged model, a gapped uncondensed
  matter sector, dilute mobile charges, another statistics choice, bound
  neutral composites, another band or another coupling regime are materially
  different routes. They are not excluded by (6) or (22).
- **N2, wall independence.** The exact Hessian relies on fixed A occupancy,
  hard-core bosonic charge exchange, zero total charge, the negative swap
  sign, its lowest finite-volume band and the uniform coefficient in (1).
  The microscopic normal-form proof and decreasing birth rate are not
  premises of the direct target Hessian calculation.
- **N3, hidden conditions.** Matter relaxation is included through the
  reduced resolvent, vertex gauge directions are removed, physical harmonic
  directions are retained, and the packet proof keeps its volume-dependent
  matter gap and prescribed initial preparation explicit.
- **N4, residual matching.** Positive potential curvature alone is not used
  as a theorem about the full interacting spectrum. The separately displayed
  compact physical-state residual establishes only the ordered fixed-box
  prepared-packet limit. No thermal or infinite-time statement is inferred.
- **N5, rhetoric.** The conclusion is that one direct weak-band transfer of
  the neutral photon construction fails. It is not that charged records,
  homogeneous laws, electromagnetism or the TOE are impossible.
- **N6, partial closure.** The microscopic route still supplies a useful
  interacting matter-field construction and a calculable response. An
  additional matter interaction could change that response, but must be
  supplied and analyzed rather than advertised as an automatic repair.
- **N7, strongest contrary case.** Intermediate-coupling quantum fluctuations
  can invalidate this weak-band description; an alternative deconfined phase
  is an open possibility. Equations (13) and (22) do not classify it.
- **N8, cross-cycle consistency.** The earlier pure-gauge photon packet and
  static external-source Coulomb calculation concern different sectors or
  targets. The new result changes no premise or coefficient in those frozen
  proofs. Its role is to prevent an unjustified merger of their conclusions
  with dense mobile charged matter.

Independent reconstruction remains the next gate for this unit. It is not
published as a retained scientific verdict or a complete phase theorem.


## 7. An overall ring-sign reversal alone is equivalent

One possible change of effective statistics would be only to replace
-J sum(R+R^\dagger) by +J sum(R+R^\dagger), keeping every other term and
the same charge Hilbert space. That particular change is exactly unitarily
equivalent on the even boxes used here.

Set nu_(x,i)=(sum_(j<i) x_j) mod 2 and
T_pi=exp(i pi sum_e nu_e E_e). Every plaquette has odd oriented nu sum:
increments through a periodic boundary are still odd because the side
length is even. T_pi commutes with Gauss, record charges and sum E^2.
Every transported charge is an odd integer, +1 or -1. The phase gained
by a four-link record exchange therefore equals the ordinary pi-flux
plaquette phase, independently of the two record contents:

\[
T_\pi R_pT_\pi^\dagger=-R_p,\qquad
T_\pi H_-T_\pi^\dagger=H_+,\qquad
H_\pm=K\sum E^2\pm J\sum_p(R_p+R_p^\dagger).
\]

The transformation moves the minimum
from zero angle to a periodic pi-flux connection; it does not remove
the corresponding band response or change the full target spectrum.

This does not derive a fermionic microscopic record theory, nor exclude
statistics changes that introduce further interactions, Hilbert-space
constraints or signs. It only removes a sign-only repair as a distinct
target within the present even-torus model. The exact geometry control
checks 8,688 charge-dependent exchange signs on four square/cubic boxes,
including all wrapping faces. The displayed parity argument supplies
the all-size proof.


## Landing scope and No-Go Discipline Gate

- **N1 — Domain:** only the model, graph, sector, preparation, observables and order of limits explicitly specified above.
- **N2 — Alternatives:** other instruments, Hamiltonians, states and scaling paths are not excluded.
- **N3 — Imports:** supplied quantum and probabilistic structures are model assumptions; the native axioms do not select them.
- **N4 — Dependencies:** named companion arguments are used within their stated scope; no audit grade is inherited.
- **N5 — Evidence:** exact finite algebra and numerical stability controls corroborate the displayed proofs. Floating spectra and propagations are not interval enclosures. Historical tables are not independently certified by their presence here.
- **N6 — Resolution:** fixed-volume, uniform-volume and ordered-limit statements keep their distinct hypotheses; no exchange of limits is inferred.
- **N7 — Remaining work:** native selection, physical implementation, energy supply, preparation and empirical identification remain separate obligations except for explicitly proved model-specific results.
- **N8 — Authority:** this source applies no audit verdict, retained grade or assembly decision.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository premise boundary only; it does not derive the supplied model.
- [homogeneous_mobile_charged_records_and_field_dynamics_bounded_theorem_note_2026-09-24](HOMOGENEOUS_MOBILE_CHARGED_RECORDS_AND_FIELD_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md): conditional argument only within its explicit hypotheses.

Finite-dimensional linear algebra, operator calculus and the explicit inequalities above are mathematical tools. Referenced literature is attribution or context unless its actual assumptions and use are stated in the argument.

## Source and verification

Source PR #8661, frozen head `a5e06800ed56708c370ebaa4830bf203c96c9656`. The primary review session uses no subagents; no separate fix reviewer or formal audit is claimed. Original auxiliary packets, failed attempts and historical seals remain recoverable on the original PR branch. The combined receipt records each original path disposition.

```bash
python3 scripts/charged_record_exchange_band_field_response_2026_09_24.py
```

The canonical wrapper executes the selected scientific controls in a fresh temporary directory, retains their generated result JSON in its stdout, and ends with TOTAL. It does not execute historical sealing or approval instructions.
