---
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: For the supplied massive free continuum representation, the real Cauchy boost agrees with the specified scalar boost including full domains and acts covariantly on a defined spacetime even-CAR vacuum net.
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: Explicit Cauchy-data/domain/local-algebra bridge for the already supplied scalar continuum representation; no microscopic localization convergence is assumed
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_id: continuum_local_boost_bounded_theorem_note_2026-10-12
claim_type: bounded_theorem
claim_scope: For the supplied massive free continuum representation, the real Cauchy boost agrees with the specified scalar boost including full domains and acts covariantly on a defined spacetime even-CAR vacuum net.
upstream_dependencies:
- concrete_gapped_chain_bounded_theorem_note_2026-10-12
- gapped_continuum_limit_bounded_theorem_note_2026-10-12
runner: scripts/continuum_local_boost_2026_10_12.py
artifact_role: theorem
target_claim_id: null
target_blocker_text: 'identifies the continuum boost with its local Lorentz

  action'
source_of_blocker_text: handoff
next_trace_action: Use the accepted smooth parallel-frame Cauchy/domain theorem in the actual microscopic boost and mixed even-observable constructions.
---

**Publication status:** The five exact source notes have completed separate-context source review and root integration for conditional composition. Original pending-review statements below describe the historical freeze and are superseded by this record. Mathematical arguments, failures and their original source identities are preserved. This is not an audit verdict or retained status.


# Local boosts for the supplied continuum Majorana algebra

**Author candidate, 2026-10-12.** This note constructs a real unitary
Cauchy-data boost, identifies its full self-adjoint generator with the
previous scalar continuum boost in the actual limiting parent frame, and
proves covariance and spacelike locality of a specified spacetime even-CAR
net. The argument is frozen before the author controls. A separate fresh
review is required; this note sets no audit verdict.

The result is conditional on the supplied free continuum carrier and CAR.
It does not prove convergence of boosted microscopic spin localizations, a
spin scaling net, interacting dynamics, 3+1 dimensions, parameter selection,
or a physical identification of this model. The given m,v are positive
mathematical parameters, not values derived from framework axioms. The
unfinished separate local-even draft is not an input.

## 1. Inputs and exact target

The source-bound inputs are:

* [Concrete supplied chain](CONCRETE_GAPPED_CHAIN_BOUNDED_THEOREM_NOTE_2026-10-12.md), SHA-256
  `0aebc2ded245d9bc9ecae364db0d1a042f9642771ed788794dafd73fb7f621bd`:
  equations C15–C16 fix its two-band kernel and smooth real frame;
  C20 fixes `c=(a+i b)/2`; C21–C24 identify its supplied full-spin GNS
  representation and literal boost.
* [Continuum group theorem](GAPPED_CONTINUUM_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-12.md), SHA-256
  `617b9a1cbb541d6f207de89c10f1fbb2005fbb27f68e818f0c14a3fe67bf802d`:
  the chosen g_a,J_a family, scalar boost b and its full domain, strong group
  limits, and maximal Fock sector sums, at the supplied representation scope.
* [Focused continuum review](../.claude/science/physics-loops/toe-local-continuum-20261012/EVIDENCE_MAP.json), SHA-256
  `254d2ccae248a52af4207041196f7b4565deccc720981d09e336ad4935adcd76`:
  supports reuse of that exact conditional theorem, not retained status.

Only the parent frame identification and the scalar/Fock comparison use these
inputs. The Cauchy, CAR and local-net argument below is supplied explicitly.
General free-Dirac covariance is established mathematical machinery; no
novelty for that general result is claimed. The new bridge being tested is
its convention- and domain-complete identification with this chain's chosen
continuum representation. Prior main notes and their scope comparison are
recorded in the evidence inventory, not imported as proof premises.

Set K_R=L²(R,dx;R²), K=L²(R,dx;C²), and let C denote position-space complex
conjugation. The complex inner product is linear in its second entry.
Use the usual Pauli matrices, Fourier transform

    fhat(q)=(2π)^(-1/2) ∫ e^(-iqx) f(x) dx,

and Xf(x)=xf(x). The supplied Dirac operator and dispersion are

\[
 D=i v\sigma_x\partial_x-m\sigma_y,\qquad
 D(q)=-vq\sigma_x-m\sigma_y,\qquad
 E(q)=\sqrt{m^2+v^2q^2},\quad m,v>0.                 \tag{L1}
\]

The Fourier multiplier D(q) is Hermitian and D(q)²=E(q)²1. Its self-adjoint
domain is H¹(R;C²): `||Df||²=m²||f||²+v²||f'||²`. Smooth compact data
are a core, by H¹ cutoff and mollification. In position space `CDC=-D`,
so `O_t=e^{itD}` commutes with C and is real orthogonal on K_R.
For compact smooth initial data let `φ_f(t,x)=(O_t f)(x)`. It solves

\[
 (\partial_t+v\sigma_x\partial_x+i m\sigma_y)\phi=0.
                                                               \tag{L2}
\]

Define the spacetime boost and its spin matrix by

\[
 \Lambda_\eta(t,x)=
 \left(t\cosh\eta+{x\over v}\sinh\eta,
       x\cosh\eta+vt\sinh\eta\right),\qquad
 S_\eta=e^{-\eta\sigma_x/2}.                           \tag{L3}
\]

There are two inverse conventions that must remain distinct:

\[
 U_\eta f(x)=S_\eta\phi_f(\Lambda_\eta(0,x)),\qquad
 V_\eta=U_{-\eta}.                                    \tag{L4}
\]

The raw solution pullback is U. The group that pushes the local algebra to
`Λ_eta O` is V. The previously reviewed scalar group
`W(s)=e^{-is b}` identifies with `V_{vs}`, not `U_{vs}`.

## 2. Classical solutions, support and conserved flux

Fourier multiplication by `e^{itD(q)}` preserves Schwartz space, uniformly
in its seminorms on compact time intervals. This follows either by
differentiating `cos(tE)1+i sin(tE)D/E`, whose derivatives have polynomial
bounds, or directly by its smooth spectral multipliers. Thus smooth compact
initial data give smooth rapidly decreasing solutions and allow the following
energy argument without an uncontrolled boundary term.

For complex as well as real solutions set

\[
 \rho=\phi^*\phi,\qquad j=v\phi^*\sigma_x\phi.
 \quad \partial_t\rho+\partial_xj=0,\quad |j|\le v\rho.
                                                               \tag{L5}
\]

The mass term cancels since `i m σ_y` is anti-Hermitian. If initial support
is in [l,r], then for t≥0
`d/dt ∫_(r+vt)^∞ ρ = j(r+vt)-vρ(r+vt)≤0`; the analogous left-hand
integral has the same sign. Applying the argument backwards in time gives

\[
 \operatorname{supp}O_t f\subset[l-v|t|,r+v|t|].        \tag{L6}
\]

Zero exterior L² norm and smoothness give pointwise vanishing there. This
also proves finite propagation for arbitrary compact intervals by density
when only L² data are needed. Fourier evolution gives uniqueness; equivalently
the conserved norm forces a solution with zero Cauchy data to vanish.

The transformed solution `S_eta φ(Λ_eta z)` again obeys L2. Indeed, the
transformed derivative part is

    S_eta e^(eta sigma_x) (partial_t' + v sigma_x partial_x') φ,

while `σ_y S_eta=S_eta^(-1)σ_y` and
`S_eta e^(eta σ_x)=S_eta^(-1)`. These identities use the
anticommutation of σ_x and σ_y; they fix the sign in S_eta.

The point-dependent time in L4 is therefore legitimate on smooth compact
data. If `supp f⊂[-R,R]`, its transformed support at t=0 satisfies
`|x| cosh η≤R+|x| |sinh η|`, hence

\[
 \operatorname{supp}U_\eta f\subset
 [-R e^{|\eta|},R e^{|\eta|}].                         \tag{L7}
\]

This is only a compactness estimate, not a claim that a boosted spacetime
region is its equal-time interval squeeze.

To prove the norm identity, use the spacelike line in primed coordinates
`t'=(tanh η/v)x'`. Conserved flux through it is

\[
 \int_{\mathbb R}\left(\rho-{	anh\eta\over v}j\right)dx'
 =\int_{\mathbb R}
   \phi^*(\Lambda_\eta(0,x))
       (\cosh\eta-\sigma_x\sinh\eta)
   \phi(\Lambda_\eta(0,x))\,dx
 =\|U_\eta f\|^2.                                    \tag{L8}
\]

Here `x'=x cosh η`, and `S_eta^*S_eta=e^{-ησ_x}`. Apply the divergence
theorem separately on the two regions between t'=0 and this line, cut off
at x'=±L. If `L>R/(1-|tanh η|)`, L6 makes every joining vertical segment
zero: along it `|t'|≤|tanh η|L/v`, while the support is bounded by
`R+|tanh η|L<L`. Thus no contribution at infinity is presumed. Oriented
flux conservation gives L8 equal to `||f||²` for both signs of η.

The real matrix S_eta and real evolution show that U_eta is real. Solution
uniqueness and the exact matrix/coordinate group laws give
`U_eta U_zeta=U_(eta+zeta)` on compact smooth data, with inverse U_-eta.
L7 and smooth parameter dependence give strong continuity there by dominated
convergence on a common compact set. Norm preservation then extends this to
a strongly continuous real unitary group on all K. This proves existence,
surjectivity and continuity before extending the variable-time formula to
general data; no pointwise formula is asserted for an arbitrary L² vector.

## 3. The full boost domain and a compact Cauchy-data core

Differentiating L4 at η=0 on C_c^∞ gives

\[
 {d\over d\eta}U_\eta f\big|_0={i\over v}B_D f,
 \quad B_D={XD+DX\over2}
 =i v\sigma_x(x\partial_x+1/2)-mx\sigma_y.             \tag{L9}
\]

The anticommutator is initially a formula on that core. It is not a
definition of the final domain by `Dom(XD)∩Dom(DX)`.

Here is an explicit complete self-adjoint realization. Put

\[
 C_0=-\sigma_y,\quad \theta(q)=\arctan(vq/m),\quad
 R(q)=e^{i\theta(q)\sigma_z/2},\quad D(q)=E(q)R(q)C_0R(q)^*,
                                                               \tag{L10}
\]
\[
 e_+={1\over\sqrt2}(1,-i)^T,\quad e_- =\overline{e_+},\quad
 u_\pm(q)=R(q)e_\pm,\quad
 (Jf)_\pm(q)=u_\pm(q)^*\widehat f(q).                  \tag{L11}
\]

J is unitary from K to `L²(dq)⊕L²(dq)`. Its columns satisfy

\[
 u_\pm^*u_\pm'=0,\qquad
 u_-(q)=\overline{u_+(-q)},\qquad
 (JCf)_\pm(q)=\overline{(Jf)_\mp(-q)}.                 \tag{L12}
\]

The first identity follows from `e_±^*σ_z e_±=0`; the second uses oddness
of θ. Thus the frame is simultaneously parallel and compatible with the
actual position-space real structure, whose Fourier action includes q→−q.

In Fourier space L9 is `iD(q)∂_q+iD'(q)/2`. Conjugating first by R gives
`C_0 b`, since the extra term is `(iE/2){C_0,R^*R'}` and
`R^*R'=iθ'σ_z/2` anticommutes with C_0. Therefore

\[
 J B_D J^*=b\oplus(-b),\qquad
 b=i(E\partial_q+E'/2).                               \tag{L13}
\]

For clarity, the scalar domain is reproduced rather than left implicit.
Set `r(q)=v^{-1}arsinh(vq/m)` and `q(r)=(m/v)sinh(vr)`. The unitary
`(Tψ)(r)=sqrt(E(q(r))) ψ(q(r))` sends b to i∂_r. Since r ranges over
the entire real line, the derivative has its usual full H¹(R) domain,
and C_c^∞ is a core. Pulling this back yields

\[
 \mathcal D_b=
 \{\psi\in L^2(dq):\psi\text{ locally absolutely continuous},
       \ E\psi'+(E'/2)\psi\in L^2(dq)\},\qquad
 \operatorname{Dom}B_D=J^*(\mathcal D_b\oplus\mathcal D_b).
                                                               \tag{L14}
\]

One may equivalently require Eψ'∈L² because |E'|≤v. This is a maximal
domain statement. There is no endpoint trace or boundary extension on R.
Smooth compact momentum functions in each band are a core. Their inverse
images under J are Schwartz functions: R and all its derivatives are smooth
bounded multipliers of Schwartz space. Thus Schwartz space is a core for
B_D. It can in turn be approximated by compact smooth Cauchy data. For a
fixed smooth cutoff χ equal to one near zero, let χ_L(x)=χ(x/L). Then

    B_D(χ_L f)=χ_L B_D f+i v σ_x xχ_L' f.

The last term tends to zero in L² since xχ_L' is uniformly bounded and
supported in the escaping tail. This proves graph convergence for every
Schwartz f. Consequently the literal operator L9 on C_c^∞(R;C²) is
essentially self-adjoint, with the domain L14. Since the Stone generator
of U extends L9/v on this core, essential self-adjointness gives

\[
 U_\eta=e^{i\eta B_D/v},\qquad V_\eta=e^{-i\eta B_D/v}.
                                                               \tag{L15}
\]

This also checks `CB_DC=-B_D`, which is consistent with the reality of
U and V because C conjugates i as well as B_D.

## 4. Positive-energy transport and the Berry term

Let `P_+=(1+D/E)/2`, understood as a Fourier multiplier; then
`CP_+C=1-P_+`. Equations L13–L15 show that U and V preserve both energy
bands. On the positive band the identification
`I_+ψ=F^(-1)(u_+ψ)` gives

\[
 I_+^*U_\eta I_+=e^{i\eta b/v}=W(-\eta/v),\qquad
 I_+^*V_\eta I_+=W(\eta/v).                            \tag{L16}
\]

One can check L16 without assuming a boost from its commutators. Define

\[
 F_s(q)=q\cosh(vs)+{E(q)\over v}\sinh(vs),\qquad
 (W(s)\psi)(q)=\sqrt{{E(F_s(q))\over E(q)}}\psi(F_s(q)).
                                                               \tag{L17}
\]

For an initial positive-energy plane wave with momentum k, the raw pullback
in L4 gives new momentum
`q=k cosh η+(E(k)/v)sinh η` and energy
`E_q=E(k)cosh η+vk sinh η>0`. Direct matrix multiplication gives

\[
 (D(q)-E_q)S_\eta=S_\eta^{-1}(D(k)-E(k)).              \tag{L18}
\]

Thus `S_eta u_+(k)=a(k,eta)u_+(q)`. The coefficient is positive real:
differentiate this identity, project onto u_+(q), and use L12 and
`u_+^*σ_xu_+=-vq/E(q)`. It gives
`a'/a=vq/(2E(q))`, `a(k,0)=1`, hence
`a=sqrt(E(q)/E(k))`. Also `dq/dk=E(q)/E(k)>0`. Changing the Fourier
integration variable from k to q therefore gives
`sqrt(E(k)/E(q)) ψ(k)`, with `k=F_(-eta/v)(q)`, precisely L16.
There is no unrecorded momentum-dependent phase.

For any smooth real phase χ and normalized positive eigenvector
`u=e^{iχ}u_+`, the actual scalar generator is

\[
 b_\chi=i(E\partial_q+E'/2)+iE u^*u'
       =b-E\chi',\qquad
 W_\chi(s)=M_\chi^*W(s)M_\chi,\quad M_\chi=e^{i\chi}.
                                                               \tag{L19}
\]

For this smooth phase the differential identity holds in the distributional
sense on the unitarily transported domain `M_chi^* D_b`. If Eχ' is bounded,
this domain also equals D_b as a set, by bounded perturbation. The
off-band derivative terms cancel exactly: differentiating `D u=E u` gives
`u_-^*D'u=2E u_-^*u'`, canceling the two terms from L13.

For an arbitrary measurable phase β with |β|=1 almost everywhere, the
valid statement is instead the unitary conjugation
`b_beta=M_beta^* b M_beta`, with domain `M_beta^* D_b`, and
`W_beta(s)=M_beta^* W(s) M_beta`. No derivative of β is asserted. For
example β(q)=sgn(q) and a smooth compactly supported φ with φ(0)≠0 give
`ψ=M_beta^* φ` in the transported domain, although ψ has a jump and is
not in D_b. Its distributional derivative has a delta contribution;
discarding it by setting a jump phase's derivative to zero almost
everywhere cannot justify the differential formula on the usual weak
derivative domain. This counterexample limits the unrestricted gauge
wording, while all actual parallel, rational and constant frames used
below are smooth.

The tempting rational eigenvector
`u_rat=((-vq+i m)/E,1)^T/sqrt(2)` has
`χ=π/2+θ/2`, so its Berry term is

\[
 iE u_{\rm rat}^*u_{\rm rat}'=-{mv\over2E(q)}.          \tag{L20}
\]

Dropping it would identify a different group in that frame. Its correct
transport includes `exp(i[χ(F_s(q))-χ(q)])`. To preserve the real
structure after any positive-band gauge change, the negative frame must
be changed to `u_-^chi(q)=overline(u_+^chi(-q))`; choosing two unrelated
band phases silently changes the real-data identification.

## 5. Relation to the actual supplied chain frame

For the continuum family in the input theorem,
`g_a-J_a=m/2`, `4g_aJ_a=v²/a²`, and

\[
 K_a(q)=\begin{pmatrix}
 0&2i(g_a-J_a e^{-iaq})\\
 -2i(g_a-J_a e^{iaq})&0
 \end{pmatrix},\qquad
 R_a(q)=e^{i\theta_a(q)\sigma_z/2},\quad
 \theta_a(q)=\arg(g_a-J_a e^{-iaq}).                    \tag{L21}
\]

The real part of the argument is strictly positive, so this is the same
single-valued odd smooth periodic frame as C16 after k=aq. Directly,

    2(g_a-J_a e^(-iaq))
       =m+2J_a(1-cos(aq))+2iJ_a sin(aq) → m+i v q.

Since `2aJ_a→v`, this convergence holds with every fixed number of
q derivatives on each compact set. The argument stays away from zero
there, so `R_a→R` in that same local smooth sense, `K_a→D`, and
`u_(a,+)=R_a e_+→u_+`. The finite-a frame is parallel for the same
`e_+^*σ_z e_+=0` reason. Its differentiated anticommutator therefore
vanishes exactly before taking a limit.

In the parent's all-up reference vacuum, `c=(a+i b)/2` annihilates and
`c^*=(a-i b)/2` creates. The positive reference vector e_+ in L11 fixes
this phase, since `sqrt(2)e_+^* (f_a,f_b)^T=f_a+i f_b`. Thus L11 is
the actual parent parallel-frame limit, with this explicit constant
creation convention. A different constant reference phase conjugates the
one-particle identification by that constant; no variable phase is erased.

The parent normalization is `dk/(2π)`. The scalar scaling map is exactly
`ψ(k)↦sqrt(a/(2π))ψ(aq)` into Lebesgue dq. Its literal scaled boost is
`b_a^0=i(E_a∂_q+E_a'/2)-aE_a/2`, and its centered boost removes the last
term. Both tend to the b of L13 in the reviewed strong comparison sense.
The origin term came from the parent's actual first moment; it is not
the Berry term in L20. Consequently L16 identifies the already-reviewed
full scalar boost limit with a geometrically defined continuum Cauchy group.

This paragraph establishes a frame/group identification. It does not assert
that the microscopic spin-to-CAR map, its localization lengths, or boosted
microscopic local algebras have a uniform scaling limit.

## 6. CAR vacuum with the stated covariance convention

Let h=P_+K and let F=F_-(h) be its fermionic Fock space, with vacuum Ω.
Use annihilation a(h), antilinear in h, and creation a^*(h), linear in h,
with `{a(h),a^*(k)}=<h,k>`. Define for real f∈K_R

\[
 c(f)=a^*(\sqrt2P_+f)+a(\sqrt2P_+f).                  \tag{L22}
\]

This is real-linear and self-adjoint. Since `CP_+C=1-P_+`, real f,g obey
`2 Re<P_+f,P_+g>=(f,g)_R`; hence

\[
 \{c(f),c(g)\}=2(f,g)_R1,\quad
 \|c(f)\|=\|f\|,\quad
 \langle\Omega,c(f)c(g)\Omega\rangle
       =2\langle f,P_+g\rangle.                        \tag{L23}
\]

The covariance sign and factor in L23 follow from the actual annihilation
of Ω; they are not imported from a state in the unfinished local-even draft.
The field algebra here is the concrete C*-algebra generated by all c(f).
It is the usual Majorana CAR representation on this real one-particle space;
the elementary relations above suffice for the net assertions below.

The vacuum is cyclic on F. Indeed for every h∈P_+K, the vector
`f=(h+Ch)/sqrt(2)` is real and has `sqrt(2)P_+f=h`. Products of fields
applied to Ω give all finite wedge products after subtracting their lower
particle contractions. These are dense. The odd/even decomposition is the
Fock particle parity, and c(f) is odd. The vacuum cyclic subspace of the
global even algebra is exactly

\[
 F_{\rm even}=\bigoplus_{n\ge0}\wedge^{2n}h.           \tag{L24}
\]

Containment follows from parity, and the reverse containment follows by
the same finite-wedge induction with even products. Thus the even vacuum
GNS sector must not be replaced silently by full F, which also has odd
particles. The parent full-spin GNS space was full F; that fact does not
turn odd Jordan-Wigner fields into elements of a local even algebra.

Any real unitary A commuting with P_+ has the vacuum-preserving implementer
`Γ(A|h)`, since second quantization sends L22 to c(Af) and fixes Ω.
In particular O_t, spatial translations and U_eta,V_eta meet the hypotheses.
Vacuum invariance is therefore proved from positive-band preservation.
Equivalently L23 and all its Wick products are invariant. Under I_+, the
boost implementer is exactly

\[
 \mathcal V_\eta=\Gamma(W(\eta/v)),\qquad
 \mathcal U_\eta=\Gamma(W(-\eta/v)).                   \tag{L25}
\]

The generator of `mathcal V_(vs)` is the reviewed maximal Fock sector sum
`dΓ(b)`. Its domain is the direct sum of the maximal closed sector sums,
with square-summable sector-generator norms; an intersection of individual
particle domains is only a core construction. Restriction to F_even keeps
only even sectors of this same self-adjoint operator. The corresponding
positive Hamiltonian is dΓ(E). The prior group theorem's full-Fock strong
convergence therefore identifies this implementer, while still saying
nothing about convergence of local algebras.

## 7. A precise spacetime net and its locality

For a real test source `H∈C_c^∞(R^(1+1);R²)` define its Cauchy vector by
the Bochner integral

\[
 kH=\int_{\mathbb R}O_{-t}H(t,\cdot)\,dt\in K_R,
 \qquad \Phi(H)=c(kH).                                 \tag{L26}
\]

It is smooth compact Cauchy data by L6 and differentiability of the compact
time integral. Its norm is at most `∫||H_t||dt`. Most useful is the exact
duality, for any smooth solution with real initial f,

\[
 (f,kH)_R=\int\phi_f(t,x)^T H(t,x)\,dt\,dx.            \tag{L27}
\]

For every open spacetime region O, define F(O) as the unital C*-algebra
generated by Φ(H) for such H with support in O. Let

\[
 A(O)=F(O)^{\rm even}
 =\overline{\operatorname{span}}
 \{1,\Phi(H_1)\cdots\Phi(H_{2n}):\operatorname{supp}H_j\subset O\}.
                                                               \tag{L28}
\]

The equality follows by approximating with field polynomials and averaging
over parity. This is a definition of a specified continuum local algebra,
not a claim that every physical observable has been identified with it.
Isotony follows immediately from test-function inclusion.

If O_1 and O_2 are spacelike separated in the precise sense that
`|x-y|>v|t-u|` for every pair of their points, L6 gives

\[
 (kH,kG)_R=\int dt\,du\,
      (H_t,O_{t-u}G_u)_R=0
 \quad (\operatorname{supp}H\subset O_1,
        \operatorname{supp}G\subset O_2).              \tag{L29}
\]

All integrals are absolutely controlled by compact time support and
unitarity. For compact test supports the spacelike margin is positive;
finite propagation makes the spatial inner product zero pointwise in
(t,u). The CAR now give graded locality of the field polynomials and,
by norm closure,

\[
 [A(O_1),F(O_2)]=0,
 \qquad [A(O_1),A(O_2)]=0.                             \tag{L30}
\]

This proves locality for the specified net on all such open regions, without
confusing disjoint equal-time supports with arbitrary spacetime separation.

For completeness, the net has the expected time-slice identification on
double cones. For a bounded interval I=(l,r), put

    D(I)={(t,x): l+v|t|<x<r-v|t|}.

If H is compactly supported in D(I), finite propagation gives
`kH∈C_c^∞(I;R²)`. Compactness supplies a uniform margin to the boundary,
so the support cannot accumulate at l or r. Conversely, for any compact
smooth f in I with distance δ>0 to its boundary, choose a real smooth χ
of integral one supported in `|t|<δ/(2v)`, and set
`H(t,x)=χ(t)(O_t f)(x)`. Its support lies in D(I), by L6, and kH=f.
Consequently

\[
 F(D(I))=C^*\{c(f):f\in L^2(I;\mathbb R^2)\},\qquad
 A(D(I))=F(D(I))^{\rm even}.                           \tag{L31}
\]

The passage from smooth compact data to L² uses the exact norm identity
in L23. Translated or boosted double cones inherit the corresponding
Cauchy-surface statement from the covariance proved next. No maximality,
Haag duality, split property or local cyclicity theorem is being claimed.

## 8. Geometric covariance, vacuum sector and group conventions

The spacetime source transformation for the physical boost is

\[
 H_\eta(z)=S_\eta H(\Lambda_{-\eta}z),\qquad
 kH_\eta=V_\eta kH.                                   \tag{L32}
\]

To prove this, take the inner product with a real initial f. The adjoint
of V_eta is U_eta; substitute its solution formula in L27 and then change
variables `w=Λ_eta z`. The spacetime Jacobian is one and S_eta is real
symmetric. The resulting integral is exactly L27 with H_eta. This argument
also fixes the spin matrix for smeared fields; it is not guessed from the
matrix acting on solutions.

The source transformation is a smooth compact test-function bijection from
O to Λ_eta O. With the implementer L25 this proves exact equality

\[
 \mathcal V_\eta F(O)\mathcal V_\eta^*=F(\Lambda_\eta O),\qquad
 \mathcal V_\eta A(O)\mathcal V_\eta^*=A(\Lambda_\eta O).
                                                               \tag{L33}
\]

Both containments use the inverse transformation; a one-way support bound
alone would not have proved equality. On even vacuum GNS space set
`A_vac(O)=A(O)|F_even` and restrict mathcal V_eta to F_even. Since parity
commutes with the implementer, L33 remains true there and Ω is fixed.
The global net is vacuum cyclic on F_even: L31 over growing intervals,
continuity in f, and the argument for L24 give a dense set of even wedges.

One can include translations with all signs explicit. For
`g z=Λ_eta z+a`, define its Cauchy map V_g by the solution formula

\[
 \phi_{V_gf}(z)=S_{-\eta}\phi_f(g^{-1}z).              \tag{L34}
\]

For a pure translation a=(τ,ell),
`V_a=T_ell O_-tau`, where `(T_ell f)(x)=f(x-ell)`.
These maps preserve P_+, are real unitary, and form a strongly continuous
representation of the proper orthochronous 1+1 dimensional Poincare group:
coordinate pullbacks compose in the inverse order while the displayed
operator action gives `V_g V_h=V_(gh)`. Existence follows from the already
proved solution maps and uniqueness; continuity follows from continuity of
translations, O and U. Their positive-band pure-translation action is
`exp[-i(τE(q)+ell q)]`; the time generator E is positive with this
explicit `e^{-iτH}` convention.

The general source transform is `H_g(z)=S_eta H(g^{-1}z)`. The same
duality proof as L32 gives `kH_g=V_g kH`, and hence exact region covariance
for `Γ(V_g|h)` on F and its restriction to F_even. These implementers fix
Ω and implement the vacuum GNS automorphisms uniquely on their respective
cyclic spaces. Their action on the C*-algebra is point-norm continuous:
`||c(V_gf)-c(f)||=||V_gf-f||`, followed by polynomial approximation.

In the parameter used by the supplied chain theorem, this reads

\[
 e^{-is\,d\Gamma(b)} A(O) e^{is\,d\Gamma(b)}
       =A(\Lambda_{vs}O).                              \tag{L35}
\]

L35 is the promised continuum local-covariance bridge. It is an equality
inside a specifically constructed free continuum net. The earlier scalar
group limit supplies the limiting unitary representation; it does not by
itself supply any convergence of the microscopic localized spin algebras.

## 9. Scope, status and remaining obligations

The stated conditional mathematical target is covered by L1–L35: full
Cauchy and boost domains, a genuine compact smooth core, real structure,
the actual parent parallel frame including its constant phase, positive
band and vacuum preservation, spacetime locality, double-cone time-slice
identification, and exact geometric covariance of the even vacuum net.
No missing lemma is hidden in an appeal to a numerical control. The next
internal gate is a separate fresh review of this complete source and its
evidence; author checks are not that review.

The explicit supplied inputs remain the 1+1 free Dirac dynamics, m,v>0,
Majorana CAR, P_+ vacuum, and the chosen microscopic family for the parent
identification. Alternatives such as a different dispersion, interaction,
statistics or polarization require a new theorem; they have not been ruled
out. General algebraic-net structure and the finite spin-to-CAR localization
bridge are separate tasks. No full spin scaling net, convergence of boosted
microscopic localization, physical state selection, framework primitive,
parameter value or empirical prediction is obtained by defining A(O).

The author controls will test the finite matrix, phase, flux and support
identities by genuinely different calculations and preserve failures and
survivors. Ordinary floating calculations cannot certify L14, L24 or the
infinite-dimensional net. No Lean execution or retained status is predeclared.

## 10. Author evidence and convention handoff

This section was appended after the controls. The complete preceding 616
lines, including L1–L35, are unchanged from the analytic freeze at
`2026-10-12T10:11:02.670951+00:00`, SHA-256
`9fc9cf7f203855faef12e63a9de355cdea525ad007c8ae27ada8c06509d62055`.
The immutable copy is
[the frozen argument](../.claude/science/physics-loops/toe-local-continuum-20261012/EVIDENCE_MAP.json).
The pre-execution
[control protocol](../.claude/science/physics-loops/toe-local-continuum-20261012/EVIDENCE_MAP.json), SHA-256
`053738bb5f213f8d4392673db6311747114edae8909969b02b7d99a8d95fc773`,
predates the scientific helper sources and fixes the diagnostic tolerances.
No analytic formula or scientific helper was changed during these runs.

The exact SymPy baseline reconstructs the spin, Lorentz, frame and finite
Jordan–Wigner matrices from their entries. Its algebraic predicates hold,
including the mass-term intertwiner, conserved-flux matrix, Berry term,
real-structure reflection, vacuum covariance `2<f,P_+g>` and the distinction
between the even vacuum sector and full Fock space. These checks are finite
algebra, not a proof of the domain/core or infinite-dimensional net results.

The initial numerical run is a preserved failure. At 180 Gauss nodes, the
two tilted-Cauchy full-wave relative errors are `.655238507697483` and
`.43600655052828025`; their norm errors are `.4293541291033513` and
`.19010196272268617`. The independently evaluated source identities and
realness checks survive. In the same run, both 360-node full-wave checks
pass, with errors below `1.71e-15`. The predeclared refinement to 360 and
720 nodes passes without changing a formula, fixture, helper, gate or
tolerance: the largest full-wave error is below `1.87e-15`, and the largest
norm/flux residual is below `6.24e-14`. This is evidence of quadrature
resolution for this fixture; it does not certify convergence, compact
support, a self-adjoint domain or a local algebra.

The following intentionally wrong variants are actual failed processes.
Numerical values below are at 720 nodes and rapidities `.47` and `-.38`.
Every failed and surviving predicate is preserved in
[the lossless results](../.claude/science/physics-loops/toe-local-continuum-20261012/EVIDENCE_MAP.json) and complete
raw streams under [runs](../.claude/science/physics-loops/toe-local-continuum-20261012/EVIDENCE_MAP.json).

| Alteration | Decisive observed failure | Weaker conditions that survive |
| --- | --- | --- |
| Wrong spin exponent, exact matrices | PDE time, space and mass intertwiners; flux; plane-wave intertwiner | Determinant, frame, real-pairing and finite-CAR checks |
| Opposite vacuum polarization | Exact vacuum covariance sign, with off-diagonal residuals of magnitude 2 | Projection and real-complement identities; even-sector dimension |
| Wrong spin exponent, numerical waves | Full-wave errors `.54172`, `.36592` | Realness, scalar norm and independently evaluated source identity |
| Reversed scalar rapidity | Full-wave errors `.81201`, `.69370`; source errors `.83453`, `.71418` | Norm, flux and realness |
| Rational frame without its Berry phase | Full-wave errors `.14191`, `.11174`; source errors `.15261`, `.12670` | Direct Cauchy norm/flux and all realness checks |
| Wrong source-spin exponent | Source errors `.55359`, `.35736` | All Cauchy-wave, norm, flux and realness checks |

The missing-Berry variant also has a roughly `1e-7` discrepancy in its
finite spatial-window norm. That discrepancy is not evidence that its exact
global transformation fails to be unitary: changing the momentum frame can
alter the tails outside this window. The full-vector mismatch is the
decisive diagnostic. The reversed-rapidity variant explicitly illustrates
why correct norm and realness alone do not establish the intended group.

Two equivalent-frame variants survive as intended: the rational frame with
its correct transport phase, and a constant positive-band phase `.37`
together with the conjugate negative-band phase. Their full-wave errors
remain below `1.89e-15`. Passing or rejected variant counts carry no proof
weight, and the exact/numerical wrong-spin runs are two calculations of
the same alteration, not two independent mathematical error families.

Every scientific process passed an external manifest-digest and input-hash
gate before execution. The manifest SHA-256 is
`b49d7e361b755ad071d76d8e57d608c83118293be1c13cacd80e10531432364d`.
Separate altered-target, altered-helper and altered-manifest controls all
exit 2 before the sentinel command executes. All scientific and rejection
runs have actual 60-second subprocess timeouts, exact argv, start/end
times, unchanged source snapshots, raw stdout/stderr and recorded exit
codes. No process timed out. The final [receipt](../.claude/science/physics-loops/toe-local-continuum-20261012/EVIDENCE_MAP.json)
binds the artifact inventory. None of this provenance certifies the theorem.

For composition, retain both sign conventions: `U_eta|h=W(-eta/v)` and
`V_eta|h=W(eta/v)`. In L34, coordinate-time pushforward is
`Γ(exp(-i tau E))`; the parent's Heisenberg `Γ(exp(+i t E))` therefore
corresponds to `tau=-t` in this source-net labeling. The local covariance
claim L35 uses V and the parent's W parameter exactly as written. No time
orientation is silently relabeled during a later microscopic comparison.

Two prior main notes were read completely as context. Their exact paths,
hashes and scopes are recorded in
[the source inventory](../.claude/science/physics-loops/toe-local-continuum-20261012/EVIDENCE_MAP.json):
`docs/FREE_DIRAC_POINCARE_REPRESENTATION_BOUNDED_NOTE_2026-05-30.md`
(`b976f0efbab87757795891b268b9c06d1d1cd2125b4698cba72fe8665fcfe3c4`)
provides textbook carrier/algebra support and explicitly excludes full
domains and microcausality;
`docs/FREE_DIRAC_WIGNER_ACTION_STRONG_CONTINUITY_BRIDGE_NOTE_2026-06-07.md`
(`d4e4234e1c87e3c4c3531f5b6663c8d3d7d2e9b1813d125c354e1bad07187e4e`)
proves supplied 3+1 dimensional mass-shell Wigner continuity, without the
present parent-frame/real-Cauchy/even-net identification. No general
free-Dirac novelty or exhaustive literature coverage is claimed.

Author evidence is complete at this bounded scope. A separate fresh
adversarial review is still required. The earlier focused continuum review
does not review this new local-algebra theorem, and the root coauthor's
source read does not replace that independent review.

## Focused gauge-regularity revision

This separate revised candidate restricts the differential identity L19
to smooth phases, and states measurable phase changes only by unitary
conjugation with their transported domains. It retains the jump-phase
counterexample to unrestricted differential wording. The original
713-line author note, frozen argument, controls, receipts and manifests
remain unchanged in the original author packet. Their runs concern the
smooth frames already specified there and have not been rerun for this
restriction. The rest of the argument and its numerical claims are
byte-for-byte unchanged. The revision is requested by the fresh focused
review, which must bind this separate source before composition; it is
not an applied audit verdict. The original note's statements about
pending review describe its own historical state.


## Publication evidence, imports and review record

**Author/checker pairing:** Same selected model family and reasoning effort; separate reviewer contexts with formula exposure, not blinded or diverse-family. Root supplied routes and is a coauthor; the section note is root-authored. Mechanical preparation and reproduction add no independent scientific review.

The original unrestricted measurable-gauge differential statement is preserved as an error. The revised statement requires smooth phases for the differential identity; a merely measurable phase gives unitary conjugation with its transported domain. The jump-domain witness, low-quadrature failure, constant/rational-gauge controls and consistent rapidity-reversal survivor remain. This theorem alone does not prove microscopic localization convergence.

The exact original note, source review, root coverage, all author/reviewer helper sources, complete results, rejected controls, survivors, timeouts and recording repairs are preserved through the [evidence map](../.claude/science/physics-loops/toe-local-continuum-20261012/EVIDENCE_MAP.json). Original source paths and SHA values identify frozen probes. The [literal publication map](../.claude/science/physics-loops/toe-local-continuum-20261012/PUBLICATION_EDITS.json) reconstructs the entire canonical note and runner without mathematical edits. Historical evidence is not relabeled as a new independent check.

Direct mathematical imports, each at the supplied scope stated in the original argument:

- [concrete gapped chain](CONCRETE_GAPPED_CHAIN_BOUNDED_THEOREM_NOTE_2026-10-12.md).
- [gapped continuum limit](GAPPED_CONTINUUM_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-12.md).

The chosen free one-dimensional dynamics, positive m and v, scaling, quasifree state, CAR machinery and cell comparison are stated hypotheses or constructions; the framework does not select these data. There is no empirical prediction, interacting or three-dimensional result. Broader spin-scaling classification remains a separate question.

All mathematical helper sources and imported finite refinement specimens are explicit primary inputs. No helper registry or dependency-policy edit is proposed. Canonical execution, vocabulary, graph comparison and focused compatibility are pending root execution; global combined pipeline and strict audit lint are independent landing gates.
