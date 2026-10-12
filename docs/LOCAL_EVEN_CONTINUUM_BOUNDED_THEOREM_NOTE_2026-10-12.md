---
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: partially_closes
conditional_surface_status: For the supplied one-dimensional massive free chain, chosen state and specified cell embeddings, fixed finite even polynomials have local norm, time-evolution and vacuum-correlation limits in an explicitly defined continuum even-CAR net.
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_id: local_even_continuum_bounded_theorem_note_2026-10-12
claim_type: bounded_theorem
claim_scope: For the supplied one-dimensional massive free chain, chosen state and specified cell embeddings, fixed finite even polynomials have local norm, time-evolution and vacuum-correlation limits in an explicitly defined continuum even-CAR net.
upstream_dependencies:
- concrete_gapped_chain_bounded_theorem_note_2026-10-12
runner: scripts/local_even_continuum_2026_10_12.py
artifact_role: theorem
claim_type_reason: Conditional supplied-model theorem with complete analytic argument and finite controls; source review does not confer retained status.
target_claim_id: mixed_local_poincare_correlations_bounded_theorem_note_2026-10-12
target_blocker_text: 'even local-observable norm

  and state limits'
source_of_blocker_text: handoff
next_trace_action: Use the explicit even-CAR comparison in the microscopic boost, mixed-word and section constructions at the same supplied-model premises.
---

**Type:** bounded_theorem


**Publication status:** The five exact source notes have completed separate-context source review and root integration for conditional composition. Original pending-review statements below describe the historical freeze and are superseded by this record. Mathematical arguments, failures and their original source identities are preserved. This is not an audit verdict or retained status.


# Local even spin observables have a causal massive continuum limit

**Author proof, 2026-10-12; fresh independent review pending.** Root proposed
the cell-average route and is a coauthor. The new result concerns explicit
uniformly bounded even spin observables in a supplied one-dimensional model.
It is conditional on the parent spin construction and the chosen scaling.
It does not select that model from framework axioms.

For every fixed `m,v>0`, the construction below gives a time-zero even CAR
net with propagation speed v and positive-energy quasifree vacuum. For
every finite family of compactly supported real smearings, its even words
are limits of actual local even spin observables. Their vacuum correlations
converge. Under specified, spacing-dependent isometric embeddings into a
common CAR algebra, the observables and their time evolutions converge in
C*-norm, uniformly on compact time intervals. This comparison implies
vanishing spin-norm commutators for the constructed observables at strictly
spacelike separations. It is not an intrinsic limit of every spin observable
or an exhaustion theorem for spin scaling nets.

## 1. Exact inputs and mathematical contract

Write S for this note's directory. The evidence directory is
`S/local_even_continuum/`. The supplied source identities are:

| Source | SHA-256 | Exact use |
|---|---|---|
| `ROOT_LOCAL_EVEN_CONTINUUM_LEAD.md` | `6ba018c16e86567a9e6d36921c384206f6f90ee886b1d9b30e206edc15d7be91` | Coauthor proposal, not evidence |
| `CONCRETE_GAPPED_CHAIN_PROBE.md` | `0aebc2ded245d9bc9ecae364db0d1a042f9642771ed788794dafd73fb7f621bd` | Full 930-line source read; even spin/CAR identification, actual spin energy flow, chosen state `omega_a=omega_0 o beta_a` |
| `CONCRETE_GAPPED_CHAIN_REVIEW.md` | `7c554adcf96ce281128c560af453234b346147f725879c25df17bbd9bcdb7d94` | Complete source review read; parent supported only at supplied-model scope |
| `Concrete_chain_root_review_coverage.json` | `1b462069c5800e767daa00e8d1718cf5eefefbe85bc7a00fbe78d290fea01909` | Root's source-bound acceptance and remaining limits |
| `GAPPED_CONTINUUM_LIMIT_PROBE.md` | `617b9a1cbb541d6f207de89c10f1fbb2005fbb27f68e818f0c14a3fe67bf802d` | Family-definition context, independently derived below; no boost result imported |

The exact parent hypotheses retained here are bilateral qubit spin algebras,
the Hamiltonian density

    h_(a,n) = -J_a X_n X_(n+1) - (g_a/2)(Z_n+Z_(n+1)),

and the parent's pure invariant state `omega_a=omega_0 o beta_a`, where
`omega_0` has every `Z_n=+1` and beta_a is its explicitly constructed
exponentially local spin automorphism. The parent proves its full spin-GNS
Hamiltonian has simple vacuum and gap `2(g_a-J_a)`. That construction is
used separately for each spacing. No uniform bound on beta_a's localization
as a tends to zero is assumed. No other algebraic ground-state selection
or uniqueness theorem is imported.

Choose, as model data rather than a derived physical law,

\[
 \sigma_a=\sqrt{m^2/4+v^2/a^2},\qquad
 g_a=\sigma_a/2+m/4,\qquad J_a=\sigma_a/2-m/4,\quad a>0.
 \tag{L1}
\]

Then `g_a>J_a>0`, `2(g_a-J_a)=m`, and `4g_a J_a=v^2/a^2`.
The current source authority is the supplied main revision
`a13caa4885f547c8d206265b031ba7649e539fd9`; planning is
`3a4b2c66a1ead7a1c48b4359627e968f681e3c39`; the assigned worktree was
`358fdf795a5504d4d7fd13344bbbd5df5504ebea`. Root refreshed ownership before
dispatch. No Git action is performed here. The current science workflow,
physics-loop/workhorse procedures, minimal axiom memo and primitive registry
were inspected. None supplies L1, this Hamiltonian, this state or this
observable identification. No new physical axiom or primitive is proposed.

The mathematical tools are the self-adjoint spectral theorem, Fourier
Plancherel, elementary Sobolev approximation, and finite-dimensional CAR/Fock
algebra followed by norm completion. Their required domains and estimates
are given below. No continuum boost theorem, scattering theorem, external
field-limit theorem or literature novelty claim is used.

## 2. Field conventions, the actual clock, and the chosen covariance

Let `K_a=ell^2(Z,C^2)`, with inner product conjugate-linear in its first
argument, and real subspace `K_(a,R)=ell^2(Z,R^2)`. Abstract Majoranas obey
`gamma_(n,1)=a_n`, `gamma_(n,2)=b_n` and
`{gamma_i,gamma_j}=2 delta_ij`. For real f define the bounded self-adjoint
field `c_a(f)=sum f_i gamma_i`; completion gives

\[
 \{c_a(f),c_a(g)\}=2(f,g)_R1,\qquad
 c_a(f)^2=\|f\|^2 1,\qquad \|c_a(f)\|=\|f\|.
 \tag{L2}
\]

Odd c_a symbols are auxiliary CAR fields, not asserted to be quasilocal
spin observables on the two-sided chain. Section 6 identifies their even
products with actual spin elements.

For a finite quadratic form `Q=(i/4) gamma^T A gamma`, with A real
antisymmetric, the CAR give `i[Q,gamma]=A gamma`. Coefficients in a real
smeared field therefore evolve by `exp(-tA)`, since the field column
evolves by `exp(tA)`. With `D_a=iA`, this is `U_a(t)=exp(+itD_a)`.
The actual Hamiltonian gives

\[
 (D_af)_{n,1}=2i(g_a f_{n,2}-J_a f_{n-1,2}),\qquad
 (D_af)_{n,2}=-2i(g_a f_{n,1}-J_a f_{n+1,1}).
 \tag{L3}
\]

It is bounded self-adjoint for each a, and position conjugation Gamma
satisfies `Gamma D_a Gamma=-D_a`. Thus `U_a(t)` preserves real vectors.
Finite spin cutoffs give this even-CAR dynamics first; finite-range matrix
cutoffs converge strongly and hence their groups do too, while L2 turns
field convergence into norm convergence. The parent's norm spin flow then
agrees on the completed even algebra. In particular its actual Heisenberg
flow on even words is the product of `c_a(U_a(t) f)` factors.

Use the unitary Fourier transform
`(F_a f)(q)=sqrt(a/(2pi)) sum_n exp(-ianq) f_n` onto
`L^2((-pi/a,pi/a),dq;C^2)`. L3 becomes

\[
 D_a(q)=\begin{pmatrix}0&2i(g_a-J_a e^{-iaq})\\
 -2i(g_a-J_a e^{iaq})&0\end{pmatrix},\qquad
 D_a(q)^2=E_a(q)^2 1,
\]
\[
 E_a(q)^2=m^2+{4v^2\over a^2}\sin^2(aq/2)\ge m^2,
 \qquad P_{a,+}={1\over2}(1+D_a/E_a).
 \tag{L4}
\]

Here and below the matrix square root is the positive one. This derives
both the uniform gap and the scaling algebra without the boost note.

The parent's chosen state restricts to precisely the quasifree covariance

\[
 \omega_a(c_a(f)c_a(g))=2\langle f,P_{a,+}g\rangle
 \quad(f,g\hbox{ real}).                                \tag{L5}
\]

To check that statement rather than choose a new state, set
`C=[[0,i],[-i,0]]=-sigma_y`, `r_a=J_a/g_a`, and
`theta_a(k)=Im log(1-r_a exp(-ik))`. Since `r_a<1`, the argument stays
in the right half-plane, where this logarithm is analytic. The parent's field-column action is
the real orthogonal operator whose Fourier matrix is
`R_a(k)=exp(i theta_a(k) sigma_z/2)`. Direct multiplication gives
`D_a=E_a R_a C R_a^*`. On coefficient smearings beta_a therefore acts by
`R_a^*`. The product spin state, in the parent's full product-Fock
representation, has covariance `2P_C=1+C`. Pulling it back gives
`2 R_a P_C R_a^*=2P_(a,+)`. Its finite even moments are quasifree because
the product vacuum is Fock vacuum and this is a real orthogonal CAR map.
Norm approximation passes that statement to all ell^2 smearings.

The one-site check fixes both possible sign errors: for `J=0`, the ground
state of `-gZ` is `Z=+1`, so `omega(XY)=i`. L5 gives
`2<e_1,P_+e_2>=i`. Direct Pauli commutation gives
`alpha_t(X)=cos(2gt)X+sin(2gt)Y`, exactly `c(exp(+itD)e_1)`.
The opposite projector or opposite clock fails one of these checks.

## 3. Position-local averaging and the limiting Dirac operator

Put `K=L^2(R,C^2)`, with real subspace `K_R=L^2(R,R^2)`. Define

\[
 (C_a f)_n=a^{-1/2}\int_{an}^{a(n+1)}f(x)\,dx,\qquad
 (C_a^*z)(x)=a^{-1/2}z_n\quad(an\le x<a(n+1)).
 \tag{L6}
\]

Cauchy-Schwarz on each cell proves `||C_a||<=1`;
`C_a C_a^*=1` and `C_a^*` is an isometry. Hence `Q_a=C_a^*C_a` is the
orthogonal projection onto these step functions. Both maps preserve
realness. If f is supported in a bounded interval I, `C_a f` has only
finitely many occupied cells; their union is contained in the closed
a-neighborhood of I, up to endpoints of measure zero.

For `f in H^1`, the fundamental theorem on each cell and Cauchy-Schwarz
give the sufficient estimate

\[
 \|(Q_a-1)f\|\le a\|f'\|.                               \tag{L7}
\]

For example, write `f(x)-a^-1 int_cell f(y)dy` as the averaged difference
`f(x)-f(y)`, apply Jensen, then bound each difference by
`|x-y| int_cell |f'|^2`; summing gives L7. Smooth compact functions are
dense in L2, and the projections have norm one, so `Q_a -> 1` strongly.

Define on `H^1(R,C^2)`

\[
 D=iv\sigma_x\partial_x-m\sigma_y,
 \qquad D(q)=-vq\sigma_x-m\sigma_y,
 \qquad E(q)=\sqrt{m^2+v^2q^2}.
 \tag{L8}
\]

The Fourier transform here is `(2pi)^(-1/2) int exp(-iqx)f(x)dx`.
Its Hermitian multiplier satisfies `D(q)^2=E(q)^2 1`. The maximal
self-adjoint multiplication domain pulls back to exactly H1, since
`||Df||^2=m^2||f||^2+v^2||f'||^2`. Cutoff and mollification in H1 prove
`C_c^infinity` is a core. This establishes the full generator, not just
a differential expression. Position conjugation reverses D, so
`U(t)=exp(+itD)` is real. Its unitary multiplier commutes with scalar
derivatives, and therefore preserves every Hs and each derivative norm.

To compare L3 and L8 set

\[
 c_a=2aJ_a=\sqrt{v^2+m^2a^2/4}-ma/2,\quad
 0<c_a\le v,\quad 0\le v-c_a\le ma/2.                   \tag{L9}
\]

Cell averaging commutes exactly with translations by a. Define
`d_a^-f=(f(x)-f(x-a))/a` and `d_a^+f=(f(x+a)-f(x))/a`.
In the first component the derivative is `i c_a d_a^- f_2`, and in
the second it is `i c_a d_a^+ f_1`; the mass terms are `im f_2,-im f_1`.
For either difference, the integral Taylor remainder gives
`||d_a^+f-f'||, ||d_a^-f-f'|| <= (a/2)||f''||`.
Applying the vector-valued triangle inequality before
C_a's contraction yields, for every `f in H^2`,

\[
 \begin{split}
 \|D_a C_a f-C_a Df\|
 &\le |c_a-v|\|f'\|+{c_a a\over2}\|f''\|\\
 &\le \delta_a(f):={a\over2}(m\|f'\|+v\|f''\|).
 \end{split}                                             \tag{L10}
\]

There is no extra sqrt(2): the two components' remainder norms are
combined in their Hilbert vector norm. The bound holds first for smooth
functions, then for H2 by density. It is a graph estimate, not an
operator-norm estimate on all of L2.

## 4. Quantitative dynamics and covariance convergence

For `f in H^2`, differentiating `U_a(t-s) C_a U(s)f` is legitimate in
ell^2: `D_a` is bounded for this a, `U(s)f` is in H2, and D is its
strong derivative generator. Integration and L10 give

\[
 \|U_a(t)C_a f-C_a U(t)f\|\le |t|\delta_a(f).
 \tag{L11}
\]

This uses preservation of the first and second derivative norms by U.
It holds for both signs of t. Combining it with L7 gives

\[
 \|C_a^*U_a(t)C_a f-U(t)f\|
 \le \epsilon_a(f,T):=a\|f'\|+T\delta_a(f),\quad |t|\le T.
 \tag{L12}
\]

Contraction and density extend convergence, uniformly for `|t|<=T`, to
every `f in K`. No operator-norm convergence on K is asserted.

The covariance admits a direct rate, stronger than a bare continuity
argument. Let `P_+=(1+sign D)/2`. For `s>0`, write
`R_a(z)=(D_a-z)^-1`, `R(z)=(D-z)^-1`. L4 and L8 imply

\[
 \|R_a(\pm is)\|,\|R(\pm is)\|
       \le(m^2+s^2)^{-1/2}.                              \tag{L13}
\]

For f in H2, R commutes with derivatives, so
`delta_a(R(+-is)f)<=delta_a(f)/sqrt(m^2+s^2)`. On that domain the
literal resolvent identity between the two Hilbert spaces is

\[
 R_a(z)C_a f-C_aR(z)f
 =-R_a(z)(D_aC_a-C_aD)R(z)f.
\]
\[
 \|R_a(\pm is)C_af-C_aR(\pm is)f\|
      \le {\delta_a(f)\over m^2+s^2}.                   \tag{L14}
\]

For any self-adjoint invertible A with gap m, the spectral theorem gives
the strongly convergent improper integral

\[
 \operatorname{sign}A={1\over\pi}\int_0^\infty
       [(A-is)^{-1}+(A+is)^{-1}]\,ds.                    \tag{L15}
\]

Indeed the scalar integral is
`(2/pi) int_0^infinity lambda/(lambda^2+s^2) ds=sign(lambda)`;
the truncated multipliers are bounded by one and converge pointwise,
which justifies strong convergence. The separate integral need not be
absolutely convergent in operator norm. The **difference** in L14 is
norm-integrable on each H2 vector, which is exactly what is needed.
Integrating L14 and using `int_0^infinity ds/(m^2+s^2)=pi/(2m)` proves

\[
 \boxed{\|P_{a,+}C_a f-C_aP_+f\|\le{\delta_a(f)\over2m}.}
 \tag{L16}
\]

Consequently

\[
 \|C_a^*P_{a,+}C_af-P_+f\|
 \le \eta_a(f):=a\|f'\|+{\delta_a(f)\over2m},\quad f\in H^2.
 \tag{L17}
\]

Here L7 applies to `P_+f`, and its derivative norm is at most `||f'||`.
The operators on both sides are contractions; H2 density extends strong
convergence to every f in K. The strictly positive fixed m is essential
to this bound; this note makes no massless-uniform assertion.

## 5. The continuum vacuum and all finite correlations

Let `K_+=P_+ K` and form fermionic Fock space `F_-(K_+)`. For real f put
`Vf=sqrt(2)P_+f` and

\[
 c(f)=a^*(Vf)+a(Vf),\qquad
 \omega(c(f)c(g))=2\langle f,P_+g\rangle.                \tag{L18}
\]

Creation is linear and annihilation antilinear in its vector argument.
Since `Gamma P_+ Gamma=1-P_+`, for real f,g one has
`2 Re <P_+f,P_+g>=(f,g)_R`. Thus L18 satisfies exactly L2 and
`||c(f)||=||f||`. The vacuum expectation is positive by this explicit
Fock construction. Its moments are quasifree: move annihilators to the
right using their CAR and use that they annihilate the vacuum. Odd
moments vanish. For an ordered list `f_1,...,f_(2r)`, make an
antisymmetric matrix W with `W_ij=2<f_i,P_+f_j>` for i<j and
`W_ji=-W_ij`, `W_ii=0`. Then

\[
 \omega(c(f_1)\cdots c(f_{2r}))=\operatorname{Pf}W,
 \quad \operatorname{Pf}W=\sum_{j=2}^{2r}(-1)^j
       W_{1j}\operatorname{Pf}W^{\widehat1\widehat j}.
 \tag{L19}
\]

In particular the four-field signs are `W12 W34-W13 W24+W14 W23`.
The upper-triangle prescription matters: the actual two-point form is
not itself antisymmetric when real smearings overlap. At one site
`omega(XYXY)=-1`, and the four-field formula gives
`i*i-1*1+i*(-i)=-1`. This also fixes the field normalization.

The positive Hamiltonian is the self-adjoint Fock sum
`H=dGamma(D|K_+)`, with its maximal direct-sum graph domain. It implements
`alpha_t(c(f))=c(U(t)f)` by `exp(+itH) A exp(-itH)`, fixes the vacuum,
and has one-particle energies E(q). An explicit optional scalar carrier
identification uses the unit vector

\[
 u_+(q)={1\over\sqrt2}
   \begin{pmatrix}(-vq+im)/E(q)\\1\end{pmatrix}.
 \tag{L20}
\]

Multiplication by u_+ maps `L^2(R,dq)` unitarily onto the positive
eigenline bundle of the Fourier-space D; direct multiplication gives
`D(q)u_+(q)=E(q)u_+(q)`. No boost covariance of a local net is inferred.

For real f,g, the actual lattice time-dependent two-point form is

\[
 2\langle U_a(t)C_af,P_{a,+}U_a(s)C_ag\rangle
 =2\langle C_af,P_{a,+}U_a(s-t)C_ag\rangle.              \tag{L21}
\]

For f,g in H2 and `|s-t|<=T`, L11 and L17 give the explicit error
relative to `2<f,P_+U(s-t)g>` at most

\[
 2\|f\|\,[T\delta_a(g)+\eta_a(g)].                     \tag{L22}
\]

No time derivative enters eta_a because U preserves derivative norms.
Density and boundedness yield uniform compact-time convergence for all
real L2 smearings. Alternatively strong convergence is uniform on the
compact vector orbit of g. Each fixed Pfaffian is a finite polynomial
in its two-point entries, so L19 proves convergence of every fixed finite
multitime vacuum correlation of even words. There is no claim uniform in
word degree, particle number, spatially growing test families or unbounded
time. The state in L21 is the actual chosen spin state through section 6.

## 6. Actual local spin observables and the explicit common embeddings

For a finite interval of lattice sites `[L,R]`, define

\[
 \gamma^{[L,R]}_{n,1}=\left(\prod_{j=L}^{n-1}Z_j\right)X_n,
 \quad
 \gamma^{[L,R]}_{n,2}=\left(\prod_{j=L}^{n-1}Z_j\right)Y_n.
 \tag{L23}
\]

These satisfy the finite CAR. They generate the full matrix algebra on the
`2^(R-L+1)`-dimensional spin space, since `Z_n=-i gamma_(n,1) gamma_(n,2)` and then X_n,Y_n
can be recovered. Finite CAR and spin algebras therefore have the same
faithful matrix realization. Their even subalgebras are isometrically
*-isomorphic.

When L is enlarged leftwards to L'<L, every gamma in `[L,R]` gains the
same factor `T=prod_(j=L')^(L-1) Z_j`. T commutes with the old interval.
In an even product there are 2r such factors, so they cancel as
`T^(2r)=1`. Right enlargement adds identity factors. This proves
compatibility of the finite isomorphisms; in particular an even product
with all occupied sites in an interval Lambda is a spin observable
supported in Lambda, independently of any exterior endpoint. The convex
hull of occupied cells suffices. Odd products acquire T and do not have
this endpoint independence. No bilateral odd-JW spin identification is used.

Completing the compatible finite even algebras gives an isometric
*-isomorphism `j_a` from the even CAR algebra over `K_(a,R)` to the even
quasilocal spin algebra. For compactly supported real `f_1,...,f_(2r)` set

\[
 A_a(f_1,\ldots,f_{2r})=
   j_a\big(c_a(C_af_1)\cdots c_a(C_af_{2r})\big),
 \qquad \|A_a\|\le\prod_j\|f_j\|.                       \tag{L24}
\]

It is an actual finite-support even spin element. Its physical support
lies in the convex hull of the occupied cells, hence in an a-enlargement
of any bounded interval containing the test supports. The test functions
are real so each individual auxiliary field is self-adjoint. Even words
need not be self-adjoint; their real and imaginary parts are observables
in the usual self-adjoint sense and obey the same convergence statements.

There is a useful **specified comparison**, not an intrinsic spin limit.
The real isometry `C_a^*:K_(a,R)->K_R` induces a CAR embedding
`iota_a(c_a(z))=c(C_a^*z)`. To see it is isometric without assuming a
universal-norm identification, restrict to finitely many orthonormal
vectors and complete them to an even-dimensional real subspace. Their
Clifford algebra has its faithful matrix representation by L23 (after
choosing an orthonormal basis); an orthogonal change of basis preserves
the CAR and its matrix norm. An isometry sends such an orthonormal set
to another. Its map is a faithful unital *-homomorphism on this full
finite matrix algebra and therefore isometric. Increasing finite
subspaces and norm completion give iota_a on the whole CAR algebra,
and its restriction to the even algebra remains isometric.

Define the spacing-dependent isometric even-spin embeddings

\[
 \Phi_a=\iota_a\circ j_a^{-1}.
 \tag{L25}
\]

Only the even spin algebra is in this domain. These embeddings are
explicit choices tied to the cells; no corresponding embedding of the
entire odd-inclusive spin algebra is claimed. For L24, the image is
the intended product `c(Q_af_1)...c(Q_af_(2r))`. For its actual spin
time evolution it is
`prod_j c(C_a^*U_a(t)C_af_j)`, by the energy identification in section 2.
L12 and a telescoping product estimate therefore imply

\[
 \sup_{|t|\le T}\left\|\Phi_a(\alpha_{a,t}(A_a))-
       \prod_j c(U(t)f_j)\right\|
 \le d_a(A,T):=\sum_j\epsilon_a(f_j,T)
                    \prod_{k\ne j}\|f_k\|              \tag{L26}
\]

for H2 smearings. Zero factors cause no difficulty in this product
form of the bound. For compactly supported L2 smearings there is norm
convergence without this rate, by L12's density extension. Finite linear
combinations of words inherit the statements. This is a C*-norm limit
of these elements in the common algebra chosen in L25; it is not
operator-norm convergence of the one-particle groups, nor a claim that
the lattice and continuum vacuum representations have been unitarily
identified. Their states are compared separately by L21-L22 and L19.

## 7. Finite propagation and causal even commutation

For a bounded interval I define `A(I)` to be the norm-closed algebra
generated by even words in `c(f)`, with real L2 f supported in I.
Set `A_t(I)=alpha_t(A(I))`. This is a precise time-zero net with time
evolution. Isotony follows from the support definition.

To prove its propagation property rather than read it off a dispersion,
write `u(t)=U(t)f`. For smooth compact f, the Fourier multiplier preserves
Schwartz functions at each bounded t, and its differential equation is

\[
 \partial_tu=-v\sigma_x\partial_xu-im\sigma_yu.
\]

The density `rho=u^*u` and flux `j=v u^* sigma_x u` satisfy

\[
 \partial_t\rho+\partial_xj=0,\qquad |j|\le v\rho.
 \tag{L27}
\]

The mass term cancels because `-im sigma_y` is anti-Hermitian. If f
vanishes to the right of R, the derivative for t>=0 of the exterior mass
`int_(R+vt)^infinity rho(t,x)dx` is
`j(t,R+vt)-v rho(t,R+vt)<=0`. It starts at zero and is nonnegative,
so stays zero. The left exterior is identical with the other sign.
For t<=0 apply the same argument to the reversed equation. Schwartz
decay justifies the integration; L2 approximation by smooth functions
supported in arbitrarily small enlargements of I extends the conclusion:

\[
 \operatorname{supp}U(t)f\subset I+[-v|t|,v|t|]
 \quad\hbox{if }\operatorname{supp}f\subset I.
 \tag{L28}
\]

For real f supported in I and g in J, unitarity and realness give

\[
 \{c(U(t)f),c(U(s)g)\}
 =2(f,U(s-t)g)_R1=0
 \quad\text{if }\operatorname{dist}(I,J)>v|s-t|.
 \tag{L29}
\]

Moving a word of even degree past another even word produces an even
number of CAR exchanges, so their sign is plus. Norm completion yields

\[
 [A_t(I),A_s(J)]=0\quad\text{when }
       \operatorname{dist}(I,J)>v|s-t|.                  \tag{L30}
\]

This is causal commutation for the defined net. The auxiliary odd fields
anticommute; they are not being called local spin fields.

There is also a statement in the actual microscopic spin norm. For A_a
and B_a from words supported in such I and J, let their degree bounds be
`M_A=prod||f_j||` and `M_B=prod||g_k||`. Isometry of Phi_a, L26 and L30
give, for H2 tests and `|t|,|s|<=T`,

\[
 \|[\alpha_{a,t}(A_a),\alpha_{a,s}(B_a)]\|
 \le 2M_B d_a(A,T)+2M_A d_a(B,T)\longrightarrow0.
 \tag{L31}
\]

The commutator is not asserted to vanish exactly at finite a. Strict
spacelike separation is the stated sufficient condition. The limit
also holds for compactly supported L2 tests without the displayed rate.

## 8. Parity and the exact reach of the construction

The real map V in L18 is onto the underlying real space of K_+:
for any `xi in K_+`, the real vector
`f=(xi+Gamma xi)/sqrt(2)` obeys `Vf=xi`. Its norm equality was already
proved. Choosing the analogous real g with `Vg=i xi` expresses a
creation operator as `[c(f)-i c(g)]/2`. Thus global even field products
on the vacuum span a dense subspace of the even Fock sector; compact
real test functions suffice by L2 approximation. Every even field word
preserves parity, so its cyclic vacuum representation is exactly that
sector, not the odd-inclusive Fock space.

The Hamiltonian restricted there is positive with simple vacuum and
nonvacuum energy at least 2m. The lower edge is 2m, by two orthogonal
one-particle packets in successively small neighborhoods of q=0, followed
by antisymmetrization. This differs from the parent's full spin-GNS
gap m. No even observable creates a one-particle state. The parent's
odd almost-local spin creators and its full spin representation are
different objects; no odd spin scaling limit is identified here.

The result is an explicit free massive causal CAR construction, with
its even observable net and a supplied-spin approximation. It does not
establish a full scaling-net exhaustion, local boost covariance, a
complete covariant spacetime-net identification, interacting or
three-dimensional physics, framework selection, or an empirical
prediction. These are outside the theorem rather than proved no-go
statements. The fixed model, state, real smearing convention, cell
embedding and fixed m,v are visible hypotheses throughout.

## 9. Frozen proof, author diagnostics, and handoff

The complete analytic candidate above and the focused control plan are
frozen before scientific execution under `local_even_continuum/frozen/`.
The diagnostic scripts test specified consequences and known-wrong
mutations using different arithmetic routes. They are author checks in
the same context, not a fresh independent review. The parent and root
lead exposed the proposed conventions; no blindness is claimed.

The frozen complete candidate has SHA-256
`dc6c87afb6157d84b032a095ae0a9be271330e85fd4685646b63f89945b56131`;
the plan has SHA-256
`31af24c9050df9bb862c36c754fc68ddb88c8d3a6dba9994a8de79893d153168`.
The mathematical arguments in sections 1-8 were not changed after that
freeze. Three wording corrections from the final source read are recorded
exactly in `local_even_continuum/POSTFREEZE_CHANGES.json`. The
execution manifest, sealed before scientific runs, has SHA-256
`ba58dff832791db97bce4780a52c3bc456ab70377bdbf982a7ca4459e46503f6`.

The four baseline controls completed without failed predicates. Their
complete rows and every changed mutant row were inspected; unchanged
mutant rows are named in `result_disposition.json` and remain in the
complete raw results. These observations support the explicitly named
finite fixtures, not the infinite-dimensional theorem by themselves.

| Control | Actual result | Limit of the evidence |
|---|---|---|
| Literal one- and five-site Pauli Hamiltonians, ground states, Heisenberg actions and four/six-field moments | Maximum norm residual `1.3868e-14` against the candidate generator, clock, covariance and Pfaffians; even endpoint/exterior/parity residuals exactly zero in these arrays | Open finite chains, not a proof of infinite-spin state existence |
| Odd left-endpoint witness | Degrees one and three each change by operator norm `2` | Demonstrates the claimed even restriction; no odd spin-field limit |
| Polynomial cell integration and actual nearest-neighbor action | All tested L10 ratios at a=`.4,.2,.1,.05,.025` are below `0.896`; exact antiderivative versus separate Gauss integration residual at most `6.27e-16` | Four fixed H2 spinors and floating arithmetic |
| Spectral dynamics, two Fourier resolutions | For field 0 at t=`.43`, embedded error falls from `.336392` at a=`.4` to `.0221649` at a=`.025`; respective L12 bounds are `1.42314` and `.0889462` | Periodic length-32 diagnostic with no wrap of the exact continuum support; finite spectral truncations remain |
| Periodic projector intertwining | For field 0, errors `.152728` and `.0107835` at the same endpoint spacings, versus L16 bounds `1.06240` and `.0664001` | This vector diagnostic is explicitly on the circle; it is not relabeled an infinite-line projector computation |
| Whole-line two-point integral versus infinite-lattice Brillouin quadrature | At relative time `.43`, errors `.0749149` and `.00452398` at the endpoint spacings, within L22 bounds `4.78725` and `.299203` | Adaptive and trapezoid quadratures are not interval-certified |

For the spectral probe, exact Fourier coefficients of the compact polynomial
initial data are computed from their spherical-Bessel formula. Truncated
continuum series are integrated over cells using the exact sinc factor;
this avoids approximating a discontinuous step function's L2 norm by
point sampling. The initial transforms are separately checked by direct
x-quadrature. The fine-grid exterior-cone norm is at most `4.18e-13`,
while reference-resolution cell averages differ by at most `8.30e-13`.
These are truncation diagnostics; exact finite propagation is L27-L28's
energy argument.

For the whole-line covariance, the tail beyond |q|=Q obeys
`2 Q^-4 ||f''||||g''||` by Plancherel and Cauchy-Schwarz. At Q=160 this
envelope is `1.05855e-7`; the adaptive error estimates are about `2.3e-12`.
Doubling Brillouin quadrature from 4096 to 8192 points changes the tested
values by at most `6.21e-17`. The estimates and this mesh difference are
reported separately; a small mesh difference is not a rigorous error
certificate. No numerical slope or monotonicity was an acceptance criterion.

Eight actual candidate-source mutations were executed against their
predeclared relevant controls. All eight were rejected by computed
mathematical residuals, rather than a hash gate:

| Mutation | Representative rejected consequence |
|---|---|
| Reverse Heisenberg coefficient clock | One-site matrix-flow residual `2.00408` |
| Use negative-energy projector | One-site ground-covariance residual `2.82843` |
| Divide cell integral by a | At a=`.025`, contraction and right-inverse identities fail; field-0 consistency residual `.571135` exceeds bound `.106240` |
| Reverse continuum mass sign | Same fixture gives `1.51610` versus `.106240` |
| Reverse continuum derivative sign | Same fixture gives `4.47949` versus `.106240` |
| Remove Jordan-Wigner tails | Five-site CAR residual `11.3137`, with further generator/state/moment failures |
| Remove alternating Pfaffian signs | One-site four-field residual `2` |
| Extend endpoint independence to odd words | The two actual odd witnesses each give residual `2` |

No mutant survives its complete targeted control. Individual predicates do
survive some mutations; the full records preserve those facts. For example,
the wrong continuum mass still meets the loose consistency bound on two
coarse fixtures, while finer spacings reject it. The standalone step-norm
identity also survives the wrong averaging normalization; the independent
contraction/right-inverse checks reject that mutant. The spectral and
correlation modules reuse the candidate sign conventions on both sides,
so their convergence alone would not choose the physical clock or vacuum;
that role belongs to the actual Pauli-state comparison and section 2's
analytic argument. No unrun broad mutation-coverage claim is made.

Separate source-copy, helper-copy and self-rebound-manifest corruptions
all fail the externally anchored input check before any science runs.
These are integrity checks, not mathematical evidence. All four baseline
and eight mutant scientific subprocesses have an actual 60-second timeout,
complete stdout/stderr, argv/cwd, before/after source hashes and timing
receipts; none timed out. The runtime is Python 3.13.5, NumPy 2.4.4 and
SciPy 1.17.1, with BLAS threads limited to one. Full reproduction commands
are in `local_even_continuum/README.md`.

The bounded source search at the pinned main revision is preserved under
`runs/source_statement_search/`. The closest inspected source was
`MICROCAUSALITY_FERMIONIC_EVEN_CAR_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md`:
its supplied finite-CAR walk bounds contain no state or continuum limit.
Its entire statement/proof was read for scope comparison; none of its
scientific conclusions is imported. The search was completed after this
candidate's analytic drafting and before computations. It is not an
exhaustive literature or open-PR novelty search, and no priority claim
follows. Root supplied the freshly checked ownership assignment.

The current checkpoint and final source/evidence manifest give recovery
paths and exact identities. Initial read-only calls lacked this durable
process recorder, and two broad combined outputs were truncated. Those
are disclosed in the checkpoint, not presented as completed verification.
Subsequent targeted reads covered the complete parent source and the
necessary arguments. No missing historical metadata was reconstructed.

The principal fresh-review targets are L5's actual state match, the
integrable resolvent comparison L14-L16, the norm-isometric even-spin
embedding L23-L26, and the passage from the flux estimate to L30-L31.
Within the stated supplied-model scope there is no intentionally assumed
new continuum lemma. These remain author proofs awaiting independent
review; no Lean certificate or audit ratification is claimed.

No editable prompt, platform instruction, axiom, canonical repository
runner or audit file is changed. No Git, publication, retained-status or
other-chat action is taken. Root owns integration and the fresh review
of this exact source before downstream scientific reuse.


## Publication evidence, imports and review record

**Author/checker pairing:** Same selected model family and reasoning effort; separate reviewer contexts with formula exposure, not blinded or diverse-family. Root supplied routes and is a coauthor; the section note is root-authored. Mechanical preparation and reproduction add no independent scientific review.

The comparison uses chosen spacing-dependent embeddings and the parent chosen ground state. Original position-kernel cutoff failures and fixed-threshold refinements remain. No intrinsic full-spin scaling net, odd local spin field, state-selection principle, interacting or higher-dimensional theorem is asserted.

The exact original note, source review, root coverage, all author/reviewer helper sources, complete results, rejected controls, survivors, timeouts and recording repairs are preserved through the [evidence map](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/a8ab3f49038327e3080d2f93afb7e34601459928/.claude/science/physics-loops/toe-local-continuum-20261012/EVIDENCE_MAP.json). Original source paths and SHA values identify frozen probes. The [literal publication map](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/a8ab3f49038327e3080d2f93afb7e34601459928/.claude/science/physics-loops/toe-local-continuum-20261012/PUBLICATION_EDITS.json) reconstructs the entire canonical note and runner without mathematical edits. Historical evidence is not relabeled as a new independent check.

Direct mathematical imports, each at the supplied scope stated in the original argument:

- [concrete gapped chain](CONCRETE_GAPPED_CHAIN_BOUNDED_THEOREM_NOTE_2026-10-12.md).

The chosen free one-dimensional dynamics, positive m and v, scaling, quasifree state, CAR machinery and cell comparison are stated hypotheses or constructions; the framework does not select these data. There is no empirical prediction, interacting or three-dimensional result. Broader spin-scaling classification remains a separate question.

All mathematical helper sources and imported finite refinement specimens are explicit primary inputs. No helper registry or dependency-policy edit is proposed. Canonical execution, vocabulary, graph comparison and focused compatibility are pending root execution; global combined pipeline and strict audit lint are independent landing gates.
