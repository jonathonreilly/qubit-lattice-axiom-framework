---
claim_id: "gapped_chain_scattering_bounded_theorem_note_2026-10-12"
claim_type: bounded_theorem
claim_scope: "Actual odd almost-local spin creators, compact positive transfer, fixed-finite-particle incoming/outgoing limits and onto symmetric-to-antisymmetric Fock maps in the chosen supplied-chain full-spin GNS. Both noninjective velocity branches remain. No arbitrary interacting model, other state or relativistic carrier premise."
upstream_dependencies:
  - concrete_gapped_chain_bounded_theorem_note_2026-10-12
runner: scripts/gapped_chain_scattering_2026_10_12.py
artifact_role: theorem
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: "Actual almost-local spin creators and complete scattering in the supplied one-dimensional gapped chain's chosen full-spin GNS representation"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
target_claim_id: null
target_blocker_text: "For the specified one-dimensional chain with `g>J>0`, can the explicit\nspin Bogoliubov automorphism supply nonzero almost-local one-particle\ncreators, a dense target family, and complete scattering in the *chosen\nground-state GNS representation*?"
source_of_blocker_text: "user_goal"
next_trace_action: "Record actual creator density and completeness only in the chosen full-spin GNS; keep the separate continuum/local-net and framework-selection questions open."
claim_type_reason: "Conditional theorem for the explicitly supplied one-dimensional model and stated hypotheses; finite controls supplement the full argument and confer no retained or framework-realization status."
---

**Type:** bounded_theorem


**Publication status:** Completed source review and root integration found no required mathematical correction at the frozen original identity. Author-era pending-review statements below are preserved historical chronology and are superseded by this status. The complete argument remains unchanged.



# Actual spin creators and complete scattering in the chosen gapped-chain GNS

**Author conditional proof, 2026-10-12; independent review pending.**
For the supplied chain with g>J>0 and the full-spin state constructed in
the concrete-chain parent, there are nonzero odd, almost-local spin
creators with exact one-particle vacuum columns. They can also be chosen
smooth under the energy flow with compact strictly positive
energy-momentum transfer. Their separated-velocity products have strong
incoming and outgoing vector limits at every finite particle number.
Those limits define onto unitary maps from symmetric Fock space to the
entire chosen spin GNS Hilbert space. In the conventions fixed below,
\[
 W_{\rm out,n}=M_{\epsilon_v},\qquad
 W_{\rm in,n}=(-1)^{n(n-1)/2}M_{\epsilon_v},\qquad
 S_n=(-1)^{n(n-1)/2}I.                                  \tag{S1}
\]
The target coordinates are antisymmetric Fock coordinates; the source
coordinates in S1 are symmetric. Their distinction is essential.

This is a supplied, integrable one-dimensional model and one specified
GNS representation. It establishes no framework-selected dynamics,
physical particle identification, scattering theorem for arbitrary
interactions, other ground-state representations, continuum or
three-dimensional theory, or exact lattice Lorentz symmetry. The
parent's exact scalar-boost-closure failure remains intact. Root supplied
the unverified route and is a contributor, not an independent reviewer.

## 1. Exact dependencies and conventions

The complete parent `CONCRETE_GAPPED_CHAIN_PROBE.md`, SHA-256
`0aebc2ded245d9bc9ecae364db0d1a042f9642771ed788794dafd73fb7f621bd`,
was read, including the full even-to-odd spin lift, state construction,
domains and scope boundaries. Its fresh source review at SHA-256
`7c554adcf96ce281128c560af453234b346147f725879c25df17bbd9bcdb7d94`
and full `ANALYTIC_RECONSTRUCTION.md` at SHA-256
`f2a8b1d666dad49539614df01543119498710d754d154560b11aa75d3ca4fbf8`
were also read. Root subsequently accepted their conditional source
reuse, with no mathematical correction, in
`Concrete_chain_root_review_coverage.json`, SHA-256
`1b462069c5800e767daa00e8d1718cf5eefefbe85bc7a00fbe78d290fea01909`.
That is explicit checked-parent dependence, not retained status or a
new independent audit here. Parent controls are not rerun or recast as
our evidence. Their two disclosed numerical blind spots remain covered
only by the review's separate witnesses and analytic proof.

Write gamma for the parent's spin automorphism beta, to avoid confusing
it with any scalar Lorentz parameter. The actual model, state and
representation being reused are
\[
 h_x=-JX_xX_{x+1}-{g\over2}(Z_x+Z_{x+1}),\quad g>J>0,
 \qquad \omega=\omega_0\circ\gamma,\quad
 \pi=\pi_0\circ\gamma.                                \tag{S2}
\]
Here omega0 is the product state Z_x=+1, and gamma is the unit-time
**spin** dynamics of the exponentially summable spin-string interaction
in the parent's C17. It is onto, translation covariant and parity
preserving. The actual energy flow alpha and lattice translations tau
commute, leave omega invariant, and on this full cyclic representation
have canonical implementations
\[
 H=d\Gamma_-(E),\quad T_a=\Gamma_-(e^{-iak}),\quad
 E(k)=2\sqrt{g^2+J^2-2gJ\cos k},\quad a\in\mathbb Z.
                                                               \tag{S3}
\]
The Fourier transform is \(\widehat u(k)=\sum_xe^{-ikx}u_x\),
with \(d\mu(k)=dk/(2\pi)\) on the circle. In particular
\(|x\rangle\mapsto e^{-ikx}\). Let
\(\mathfrak h=L^2(\mathbb T,d\mu)\). The physical Hilbert space here is
the **full** \(\mathcal F_-(\mathfrak h)\), including odd sectors, with
vacuum Omega and its grading projections Pi_n. Each Pi_n reduces H and
T; it need not be a joint spectral function of H,T when bands overlap.
No spectral separation of the one-particle band from every multiparticle
band is assumed. The mass gap is \(m=2(g-J)>0\).

The ordered finite-spin configuration \(|x_1<\cdots<x_n\rangle\)
is identified with
\(a^*(e_{x_1})\cdots a^*(e_{x_n})\Omega\). This fixes the full
Jordan–Wigner order. The creation operators are linear in their arguments.
In normalized product measure, set
\[
 \begin{split}
 f_1\wedge\cdots\wedge f_n
   &=\sqrt{n!}\,P_-(f_1\otimes\cdots\otimes f_n),\\
 f_1\vee\cdots\vee f_n
   &=\sqrt{n!}\,P_+(f_1\otimes\cdots\otimes f_n).
 \end{split}                                            \tag{S4}
\]
Thus their wavefunctions are respectively \(1/\sqrt{n!}\) times
the determinant and permanent of the matrix \(f_i(k_j)\). This is the
Fock creation-product convention; the wedge of orthonormal functions
has norm one. No extra n! is inserted into the sector measures.

All self-adjoint second-quantized sums in this note mean the closures on
their maximal sector-sum and Hilbert direct-sum domains. The new proof
uses their bounded unitary groups; it never replaces a maximal sum
domain by an intersection of individual domains.

## 2. Actual odd spin creators and exact vacuum columns

Set
\[
 S_x^-={X_x-iY_x\over2},\quad A_x=\gamma^{-1}(S_x^-),
 \qquad A_x=\tau_x(A_0).                               \tag{S5}
\]
These are bounded **spin-algebra** elements. They are odd under spin
parity; no bilateral odd-CAR field is being declared quasilocal.
The exact representation identities give
\[
 \pi(A_x)=\pi_0(S_x^-),\quad
 \pi(A_x)\Omega=|x\rangle,\quad
 \pi(A_x^*)\Omega=0.                                  \tag{S6}
\]
In particular A_x is nonzero and has norm one.

Here is the needed localization bound from the actual spin interaction.
For \(r=J/g<1\), its interval term has norm at most
\(r^n/(4n)\); at most n+1 intervals of length n contain a given pair
of sites. Consequently, for \(0<\mu<-\log r\), it has finite norm
for \(F_\mu(d)=e^{-\mu d}(1+d)^{-3}\), exactly the parent's C18.
The circle-independent spin factors are finite dimensional, the terms
are bounded Hermitian and autonomous, and the lattice is the countable
metric space Z. These match the hypotheses of the actual
[NSY arXiv:1810.02428v2, Theorem 3.1](https://arxiv.org/abs/1810.02428v2).
The F-function definitions, interaction norm and full theorem statement
were freshly read in the copied original TeX, lines 1094–1360; the
thermodynamic flow existence and norm limits are checked parent inputs.
The resulting finite-volume commutator estimate, followed by that norm
limit, gives at times +1 and -1
\[
 \|[\gamma^{\pm1}(S_x^-),U_Y]\|
       \le C\sum_{y\in Y}F_\mu(|x-y|)                 \tag{S7}
\]
for every norm-one unitary on a finite Y disjoint from x. Constants
depend on g,J,mu and the unit time, but not on x or Y.

Average S7 over the finite complement unitaries defining the normalized
trace expectation onto \(B_R(x)\), then exhaust the complement.
The expectations converge in norm on the quasilocal algebra, by local
approximation. The summable exterior tail proves
\[
 \|A_x-\mathbb E_{B_R(x)}A_x\|\le C_\mu e^{-\mu R}.
                                                               \tag{S8}
\]
This argument applies equally to the inverse automorphism, so its odd
spin locality is proved rather than borrowed from an even-CAR formula.

For \(f\in C^\infty(\mathbb T)\), put
\[
 c_x(f)=\int e^{ikx}f(k)d\mu(k),\qquad
 A(f)=\sum_{x\in\mathbb Z}c_x(f)A_x.                  \tag{S9}
\]
The coefficients are Schwartz on Z by periodic integration by parts,
so the sum converges absolutely in the algebra norm, with
\(\|A(f)\|\le\sum_x|c_x(f)|\). Equations S6 and Fourier inversion give
\[
 \pi(A(f))\Omega=f\in\mathfrak h,\qquad
 \pi(A(f)^*)\Omega=0,\qquad
 (1-\Pi_1)\pi(A(f))\Omega=0.                           \tag{S10}
\]
Finite translates already span the trigonometric polynomials, dense in
the one-particle sector. This is actual creator density, not density of
unrelated abstract test vectors.

For almost locality, truncate the sum to \(|x|\le R/2\), and replace
each retained A_x by its expectation onto \(B_{R/2}(x)\). This is
supported in \(B_R(0)\), up to harmless integer floors, and its error is
bounded by
\[
 C e^{-\mu R/2}\sum_x|c_x(f)|
       +\sum_{|x|>R/2}|c_x(f)|.                        \tag{S11}
\]
It is O(R^-N) for every N. Constants are allowed to depend on f.
The unsmeared A_x are exponentially local; the smooth packets A(f)
and the filtered creators below are rapid almost-local. These different
decay claims are not interchanged.

## 3. Optional transfer filters, proved on the actual spin algebra

The direct product limit below first uses A(f) and needs no abstract
Haag–Ruelle theorem. For applications requiring compact transfer we
construct such creators and then prove that their limits agree.
Use the actual action \(\beta_{s,x}=\alpha_s\tau_x\) of
\(\mathbb R\times\mathbb Z\); its implemented character on a
one-particle vector is \(e^{isE(k)-ixk}\).

Given \(F\in C_c^\infty(\mathbb R\times\mathbb T)\), define
\[
 \begin{split}
 w_F(s,x)&={1\over2\pi}\int_{\mathbb R}de
      \int_{\mathbb T}d\mu(k)\,F(e,k)e^{-ise+ixk},\\
 B_F&=\sum_x\int_{\mathbb R}w_F(s,x)\beta_{s,x}(A_0)\,ds.
 \end{split}                                            \tag{S12}
\]
The kernel is Schwartz in s and rapid on Z, jointly with all time
derivatives; this follows by integration by parts in e and k, with
compact energy support. Thus S12 converges absolutely in norm, and
\[
 F(e,k)=\sum_x\int w_F(s,x)e^{ise-ixk}ds.               \tag{S13}
\]

For completeness, almost locality of S12 follows from actual LR bounds.
The original h interaction is finite range with bounded terms; it has
finite F_mu norm for every fixed mu>0. The same NSY bound and exterior
unitary averaging give, for a local C supported in \(B_L(0)\),
\[
 \|(1-\mathbb E_{B_R(0)})\alpha_s\tau_x(C)\|
 \le C_1(2L+1)\|C\|
       e^{-\mu_1(R-|x|-L-v_{\rm LR}|s|)}               \tag{S14}
\]
when the displayed distance is positive. Constants are independent of
L,R,x,s; an upper bound by 2||C|| is always available. Take
\(L=\lfloor R/4\rfloor\), approximate A0 by S8, and on
\(|x|+v_{\rm LR}|s|\le R/2\) use S14. The resulting error is
exponential times a polynomial in R. The complementary portion of S12
is O(R^-N) in norm for every N because w_F is jointly Schwartz and
\(|x|+v_{\rm LR}|s|>R/2\) implies \(|x|+|s|>cR\).
A positive enlarged LR speed can always be used. This proves rapid
almost locality of B_F. Parity is odd because the energy and spatial
flows preserve parity. Integration by parts also proves all norm
energy derivatives:
\(\delta_h^q B_F=\sum_x\int(-\partial_s)^q w_F(s,x)
\beta_{s,x}(A_0)ds\). No norm derivative of A0 is assumed here.

We use the following explicit Arveson support convention. For any
continuous linear functional on the algebra, take the group Fourier
support of its orbit distribution, with characters \(e^{ise-ixk}\);
the element's transfer support is the union of these supports, closed.
For kernels set \(\widehat g(e,k)=\sum_x\int g(s,x)e^{ise-ixk}ds\).
Smearing an orbit by w_F shifts its argument by +(s,x), so its Fourier
distribution is multiplied by F, by S13. This assertion can be checked
without a spectral-transfer theorem: a second Schwartz smearing g
obeys \(\beta_g(B_F)=\beta_{g*w_F}(A_0)\), by norm Fubini, and the
transform of its convolution is \(\widehat g F\). If the support of
\(\widehat g\) misses supp F, that product and hence the convolution
are zero by Fourier inversion. Such test functions characterize
distributional support. Therefore
\[
 \operatorname{Sp}_\beta(B_F)\subset\operatorname{supp}F,
 \qquad \operatorname{Sp}_\beta(B_F^*)\subset-\operatorname{supp}F.
                                                               \tag{S15}
\]
The second inclusion uses complex conjugation of the kernel, whose
transform is \(\overline{F(-e,-k)}\). Momentum differences are taken
on the circle. No continuous geometric spatial flow has been introduced.

The vacuum formula is an ordinary bounded joint spectral multiplier,
with no double-operator-integral assumption:
\[
 \pi(B_F)\Omega=F(E(k),k),\qquad
 \pi(B_F^*)\Omega=0.                                  \tag{S16}
\]
Indeed A0 Omega is the constant one-particle wavefunction, and the
vacuum is fixed by every beta implementer. The adjoint formula follows
already from A0* Omega=0 under each smearing.
Set \(B_F(f)=\sum_xc_x(f)\tau_x(B_F)\). If
\[
 F(E(k),k)=1\quad\hbox{on supp }f,                    \tag{S17}
\]
then B_F(f) has exactly the column and zero adjoint column in S10.
Its transfer remains inside supp F, because translations and their norm
sums do not enlarge S15. Its almost locality follows from the same
spatial summation argument as S11, now with arbitrary polynomial tails.

Such filters exist with strictly positive compact energy support: choose
a real smooth energy function equal to one on
\([2(g-J),2(g+J)]\) and supported in a compact subset of (0,infinity),
and take F independent of k. For individual packets an additional smooth
momentum cutoff equal to one on supp f is permitted. More general
filters satisfying S17 are allowed. Positivity, transfer smoothness and
odd-spin algebra membership have thus been checked for actual creators.
No isolation of Pi1 by a function of H,T is used.

## 4. Uniform lattice tails outside velocity cones

Let \(v=E'\), let f be smooth, and choose a bounded open interval I
with \(v(\operatorname{supp}f)\Subset I\). For either sign of t set
\[
 f_t=e^{-itE}f,\quad u_t(x)=c_x(f_t),\quad
 C_t(I)=\{x\in\mathbb Z:x/t\in I\},\quad |t|\ge1.
                                                               \tag{S18}
\]
For x outside this cone, the derivative of the oscillatory phase is
\(x-tv(k)\). There is c>0 such that, on a neighborhood of supp f,
\[
 |x-tv(k)|\ge c(|x|+|t|).                              \tag{S19}
\]
For \(|x|\le(2\|v\|_\infty+1)|t|\), use the positive gap between
the velocity support and the complement of I. For larger |x| use
\(|x|-|t|\|v\|_\infty\). This proves S19 also in the far spatial
tail, not just on a compact range of x/t.

Put \(\lambda=|x|+|t|\) and divide the phase by lambda. Its first
derivative is uniformly bounded away from zero on that neighborhood,
and every higher derivative is uniformly bounded, because
\(|t|/\lambda\le1\). Repeated integration by parts with
\((i(x-tv))^{-1}\partial_k\), using a smooth cutoff equal to one on
supp f, gives for every integer N
\[
 |u_t(x)|\le C_N(1+|x|+|t|)^{-N}\qquad(x\notin C_t(I)).
                                                               \tag{S20}
\]
This may be done in finitely many circle charts; alternatively periodic
integration has no boundary term since x is an integer. Only the first
phase derivative is inverted. No nondegeneracy of E'' is needed.
Summing S20 over the full integer lattice gives, for every L>0,
\[
 \|\mathbf1_{C_t(I)^c}u_t\|_1+
 \|\mathbf1_{C_t(I)^c}u_t\|_2\le C_L(1+|t|)^{-L}.       \tag{S21}
\]
For example the two sums before relabeling exponents are bounded by
constants times \(|t|^{1-N}\) and \(|t|^{1/2-N}\), respectively.
The cone has at most \(C_I(1+|t|)\) sites. Parseval, Cauchy–Schwarz
on the cone and S21 outside it give the essential spectator bound
\[
 \|u_t\|_1\le C_f(1+|t|)^{1/2},\qquad
 \|u_t\|_2=\|f\|_2.                                  \tag{S22}
\]
Constants need not be uniform over all packet families or particle numbers.

## 5. Exact spin-to-CAR product comparison and both limits

First take smooth packets whose compact velocity supports can be
enclosed in disjoint bounded open intervals I_i.
For the displayed signs order these intervals as
\(I_1<\cdots<I_n\). The theorem initially concerns this interval
ordering; the general symmetric map will remove the ordering convention.
Define the actual spin vectors
\[
 \Psi_t^A(f_1,\ldots,f_n)
 =e^{itH}\pi\bigl(A(f_{1,t})\cdots A(f_{n,t})\bigr)\Omega.
                                                               \tag{S23}
\]
This equals the product of equally timed Heisenberg packet operators on
the invariant vacuum. It is a vector limit, not a bounded-operator
strong limit on the whole Hilbert space.

Under the actual representation S6,
\(\pi(A(f_{i,t}))=\sum_xu_{i,t}(x)S_x^-\). Replace each coefficient
by its restriction to \(C_t(I_i)\). A telescoping product estimate,
\(\|\sum_xu(x)S_x^-\|\le\|u\|_1\), S21 and S22 show that the
resulting vector error is O(|t|^-L) for every L, for each fixed n.
Specifically a replaced factor has an arbitrarily rapid l1 tail and
the n-1 spectators grow at most \((1+|t|)^{(n-1)/2}\).

For the truncated factors all cones are finite and disjoint. On an
increasing configuration \(x_1<\cdots<x_n\), the spin product
coefficient is the permanent of \(u_{i,t}(x_j)\): distinct spin flips
commute and repeated flips vanish. The CAR creation product coefficient
is its determinant in the ordered basis fixed before S4. Only one
permutation can survive the cone restrictions. At positive t it is
the identity; at negative t it is the reversal. Thus the **exact finite
cone identity** is
\[
 \prod_{i=1}^n\Bigl(\sum_{x\in C_t(I_i)}u_{i,t}(x)S_x^-\Bigr)\Omega
 =\begin{cases}
 \prod_i a^*(u_{i,t}^{\rm cone})\Omega,&t>0,\\
 (-1)^{n(n-1)/2}\prod_i a^*(u_{i,t}^{\rm cone})\Omega,&t<0.
 \end{cases}                                            \tag{S24}
\]
The half-line CAR sign on a finite configuration counts occupied sites
strictly to the left; applying an increasing ordered creation word from
right to left gives the positive ordered basis. This checks S24's sign
directly, including odd particle numbers.

On CAR Fock space \(\|a^*(u)\|=\|u\|_2\). Therefore replacing the
truncated CAR packets by their full packets costs an arbitrarily rapid
l2 tail by S21 and a product of fixed l2 norms. Finally
\(e^{itH}a^*(f_{1,t})\cdots a^*(f_{n,t})\Omega
=f_1\wedge\cdots\wedge f_n\), by the actual S3 energy group.
Combining all three comparisons proves
\[
 \lim_{t\to+\infty}\Psi_t^A=f_1\wedge\cdots\wedge f_n,
 \qquad
 \lim_{t\to-\infty}\Psi_t^A
       =(-1)^{n(n-1)/2}f_1\wedge\cdots\wedge f_n.       \tag{S25}
\]
For each fixed smooth interval-separated family the vector convergence
is faster than any inverse power of |t|. The proof is for every finite
n, not extrapolated from a two-particle calculation.

If compact velocity supports are pairwise disjoint but interlace so that
single ordered intervals cannot contain them, partition the compact
velocity range into finitely many small intervals. A smooth partition
in v splits each packet into finitely many smooth pieces; the positive
distance between different packets' velocity supports permits every
nonzero selected combination to have separated containing intervals.
Multilinearity applies S25 to each combination. In that situation the
answer need not be one fixed sign times the original wedge; the general
multiplier in §7 is the precise statement.

## 6. The filtered actual creators have exactly the same limits

Let \(B_i=B_{F_i}\) with S17 for f_i, and write
\(D_i=B_i-A_0\). Use translated packet sums
\(B_i(f_{i,t})=\sum_xu_{i,t}(x)\tau_x(B_i)\), and similarly for D_i.
Equations S10 and S16–S17 imply the exact identity
\[
 \pi(D_i(f_{i,t}))\Omega=0\quad\hbox{for every }t.       \tag{S26}
\]
No claim that D_i itself annihilates the vacuum is needed when F_i has
a momentum cutoff. The packet identity is what the proof uses.

Two rapid almost-local centered elements C,D obey
\[
 \|[\tau_x(C),\tau_y(D)]\|
      \le C_N(1+|x-y|)^{-N}                            \tag{S27}
\]
for all N: replace them by local approximants of radius less than
|x-y|/3, which commute, and bound each approximation error. Small
separations are absorbed in the constant. On two disjoint velocity
cones the site distance is at least \(\delta|t|\). Summing S27 with
the packet coefficients and using S22 gives a bound of the form
\(C_N(1+|t|)^{1-N}\). The off-cone terms have arbitrary decay by
S21. Consequently
\[
 \|[D_i(f_{i,t}),A(f_{j,t})]\|=O(|t|^{-L})
       \quad(i\ne j)                                 \tag{S28}
\]
for every L; the same is true for any pair of the fixed almost-local
seeds. The coefficient l1 growth of each uncommuted factor is at most
O(|t|^1/2).

Telescope the product of B_i packet sums against the product of A
packet sums. In each term commute its D_i factor through all factors
to its right. The final term vanishes on Omega by S26. Every commutator
term has arbitrary decay by S28, which dominates all its finitely many
spectators. Applying the norm-one \(e^{itH}\) proves
\[
 e^{itH}\pi\bigl(\prod_i B_i(f_{i,t})-\prod_i A(f_{i,t})\bigr)\Omega
       \longrightarrow0                              \tag{S29}
\]
with arbitrary inverse-power speed. Thus S25 and the general multiplier
limits below hold for the actual compact-positive-transfer creators too.
The same argument proves independence under any fixed almost-local seed
replacement with the same packet vacuum columns, under the explicitly
used translation covariance and locality bounds. It does not assert
uniformity in time-dependent choices of the filters.

## 7. Velocity coincidences, density and the exact multiplier

The function
\[
 v(k)=\frac{4gJ\sin k}{E(k)}                            \tag{S30}
\]
is real analytic on the circle because g>J>0 keeps E positive. It is
nonconstant: v(0)=0 while v(pi/2)>0. For each real c, v-c is a
nonzero real-analytic function on a compact circle, so its zeros are
isolated and finite. Hence each velocity level has Lebesgue measure
zero. For every n, Fubini and a finite union give
\[
 \mu^n\{(k_1,\ldots,k_n):v(k_i)=v(k_j)
                   \text{ for some }i\ne j\}=0.        \tag{S31}
\]
This is not injectivity of v. For example the positive branch has its
maximum at cos k=J/g and generally has two momenta per submaximal positive
velocity. Both branches remain in the one-particle space and the proof.

Away from S31 define
\[
 \epsilon_v(k_1,\ldots,k_n)
       =\prod_{i<j}\operatorname{sgn}(v(k_j)-v(k_i)).   \tag{S32}
\]
Choose any value on the null set. Reordering a tuple of distinct real
velocities by a transposition reverses the sorting parity; equivalently
the Vandermonde sign in S32 is alternating. Its modulus is one almost
everywhere. Multiplication by epsilon_v therefore is a unitary
\[
 M_{\epsilon_v}:P_+L^2(\mathbb T^n,\mu^n)
                    \longrightarrow P_-L^2(\mathbb T^n,\mu^n),
 \qquad M_{\epsilon_v}^{-1}=M_{\epsilon_v}.             \tag{S33}
\]
On a tensor family with \(I_1<\cdots<I_n\), at a tuple with
\(k_j\in\operatorname{supp}f_j\) epsilon_v is +1. At a permuted
tuple it is the permutation sign. Expanding S4, and using the disjoint
velocity supports, proves the correctly normalized pointwise identity
\[
 M_{\epsilon_v}(f_1\vee\cdots\vee f_n)
                    =f_1\wedge\cdots\wedge f_n.       \tag{S34}
\]
For other interval orders the sorting sign appears on the right. For
interlacing supports apply S34 to the interval-ordered pieces from the
finite splitting after S25 and sum those identities. No single fixed
sign times the original unsplit wedge is asserted in that case. Thus
the spin product limits agree with S1 on all such symmetric tensors.

Here is density on the whole n-particle sector, not just a chosen
monotone branch of v. For delta>0 choose a finite nonnegative smooth
partition \(\sum_j\chi_j=1\) on the compact velocity range, with
\(\chi_j\in C_c^\infty(I_j)\) and each interval I_j of length at
most 3delta.
For any symmetric L2 function G, expand G by
\(\prod_i\sum_j\chi_j(v(k_i))=1\). Retain only terms whose
containing intervals have pairwise disjoint closures. The discarded
multiplier has absolute value at most one and is supported where some
velocity pair has distance at most 6delta. By S31 and dominated
convergence, the retained symmetric function tends to G in L2 as
delta tends to zero. The selection rule is invariant under coordinate
permutations, so symmetry is preserved.

For any retained finite tuple of intervals, approximate G in the product
L2 space by a finite linear combination of smooth simple tensors.
Multiplication by the bounded smooth factors \(\chi_j(v(k_i))\)
preserves the approximation and puts each tensor factor in
\(C^\infty(\mathbb T)\) with velocity support compactly inside its
specified I_j. Then symmetrize; P+ has norm one. There are only finitely
many retained interval tuples at fixed delta. This proves density of
finite linear combinations of separated-velocity smooth symmetric
tensors. Preimages of I_j may have several momentum components; the
argument keeps all of them and imposes no injectivity restriction.

## 8. Complete wave operators in this chosen representation

Define the asymptotic Hilbert space to be \(\mathcal F_+(\mathfrak h)\)
with the convention S4. On its dense finite-particle span just proved,
define outgoing and incoming wave operators by the actual vector limits
S23 using either the A creators or the filtered creators. Equations
S25 and S34 identify these maps exactly with S1. This proves linear
consistency and every cross-family inner product: both maps are
restrictions of the explicit isometries S33, not merely norm matches
within individual disjoint packet families.

For n=0 both maps fix Omega; for n=1 both are the identity. For each
n≥2 S33 is onto the entire antisymmetric sector, so the extensions
\[
 W_{\rm out}=\bigoplus_{n\ge0}M_{\epsilon_v},\qquad
 W_{\rm in}=\bigoplus_{n\ge0}(-1)^{n(n-1)/2}M_{\epsilon_v}
                                                               \tag{S35}
\]
are onto unitaries from symmetric Fock space to the **entire chosen
full-spin GNS Hilbert space** of S2. Infinite-sector vectors are reached
by Hilbert completion and finite-sector truncation. No uniform-in-n
large-time estimate or single infinite product of operators is claimed.
This proves completeness in the stated representation and supplies all
particle-number sectors, not just one-particle density.

Both epsilon_v and the scalar incoming sign commute with multiplication
by the total energy and geometric momentum characters. Thus W_in/out
intertwine the actual energy groups and all integer translations:
\[
 e^{isH}W_{\rm in/out}=W_{\rm in/out}\Gamma_+(e^{isE}),
 \quad T_aW_{\rm in/out}=W_{\rm in/out}\Gamma_+(e^{-iak}).
                                                               \tag{S36}
\]
Stone's theorem also gives equality of the full energy domains under
these unitaries. The scattering operator with convention
\(S=W_{\rm out}^*W_{\rm in}\) is
\[
 S=\bigoplus_{n\ge0}(-1)^{n(n-1)/2}I
       =\exp\!\left({i\pi\over2}N(N-1)\right).        \tag{S37}
\]
The final expression is bounded spectral calculus of particle number;
its definition requires no vector to lie in Dom N squared.

The incoming/outgoing source statistics are symmetric because these are
asymptotic products of spin-local commuting creators. Their targets are
fermionic coordinates of the diagonal representation, related by the
velocity sorting sign. Declaring those two Fock spaces identical would
erase the step that produces S37. Other coordinate conventions can
rephase the displayed maps; this note fixes the ordered configuration,
Fourier, time and Fock conventions in S3–S4 and derives the signs from
actual configurations. No general local-net spin-statistics theorem is
being asserted.

## 9. Exact scope and remaining boundaries

The exact columns S10/S16 eliminate every off-one-particle remainder for
these selected creators. This is an actual operator construction with
dense target columns; it is stronger than an imposed regularity bound
for abstract vectors. It says nothing similar about arbitrary local
operators, and Pi1 has not been replaced by an isolated joint H,T band.
The present direct proof uses the periodic dispersion E and actual
geometric translations; it does not invoke the earlier relativistic
centre/boost carrier bridge or identify current momentum with k.

The following distinctions are essential to the theorem. A bare even-CAR
diagonalization would not provide S5; the checked full spin automorphism
does. A one-particle density statement alone would not imply S35; the
all-n product comparison, null coincidence set and sectorwise unitary
argument do. A pointwise stationary-phase slogan would not supply S21;
the uniform far-lattice bound S19–S20 and summation do. Arbitrary
measurable momentum packets are not asserted to give the same literal
time-dependent operator formula; the maps on all L2 sectors are the
isometric extensions of the dense smooth domain.

At g=J the positive gap and the parent's spin automorphism hypotheses
change; at J=0 the velocity is constant and S31 fails. Neither edge is
included. Velocity coincidences at distinct momenta exist but have zero
product measure, and are not discarded by deleting a whole momentum
branch. At finite times overlapping spin flips obey hard-core exclusion;
they are not globally equal to CAR creators or ordinary bosonic creators.
Only the spatially ordered cone identity S24 is exact in that form.

The supplied density retains the parent's exact non-Lorentz stress
\(4JgE(k)\cos k\); no scalar-beta closure or higher-dimensional
symmetry follows from the scattering result. No state beyond the
explicit omega in S2, no physical asymptotic space outside its GNS, and
no selection of this Hamiltonian by the framework has been established.
Independent review of this new proof remains necessary before extensive
reuse; no audit or retained status is assigned here.

## 10. Frozen proof, discriminating evidence and honest limits

Sections 1–9 above were frozen before creation or execution of the new
scientific controls, at 2026-10-12T08:48:25Z. The immutable
`gapped_chain_scattering/ANALYTIC_BEFORE_CONTROLS.md` is 611 lines,
29,828 bytes, SHA-256
`801a25591d53a2e9b22c3bac35e92d7e6ee58a0f319baba44dc3bdbc25f00f1b`.
This final note preserves that entire byte prefix; its only subsequent
addition is this evidence section. Root read all 611 lines and reported
no immediate defect as coauthor. A fresh independent review is still
required. The root lead is snapshotted at SHA-256
`10807d86cc0fd199aca71a6ca449a1b373474b73cc585374d141543e43e41344`;
it was a proposed route, not evidence for the conclusion.

`candidate.py` contains finite representatives of the displayed
formulas. `controls.py` supplies separate Pauli tensor, determinant,
occupation-basis, quadrature and cumulative-sum calculations. The
baseline's 95 recorded finite rows meet their stated numerical
tolerances. They are discriminating witnesses, not proofs by enumeration.

| Formula under check | Different calculation and finite scope |
| --- | --- |
| Actual spin product | Dense tensor products of the literal 2 by 2 lowering matrix, n=1 through 4 on six sites; overlapping packets included |
| Frozen CAR order | Determinant minors compared with occupied-left CAR action; complex coefficients |
| Cone reversal sign | Exact disjoint two-site cones for n=1 through 7 in both directions, plus permutation inversion counts |
| S4 normalization | Symmetric wavefunction norm versus bosonic occupation creators with square-root occupation factors; antisymmetric norm versus Gram determinant, n=2,3,4 |
| Velocity and both branches | Five-point derivative of the independent hypot expression for E; both roots of the quadratic relation between cos k and a prescribed speed |
| S34 sorting map | Derivative-determined velocity ordering and determinant amplitudes for every permutation of three finite families |
| Packet Fourier/time clocks | FFT coefficients versus Gauss–Legendre integration on actual compact packet supports, in both time directions |
| Finite-time pair comparison | Permanent/determinant array difference versus strict-right cumulative probability sums; independently recorded captured packet norms |
| Transfer clock | Direct continuous-time quadrature and literal integer translation characters versus the transfer multiplier |

For g=2.3, J=0.7, the last pair fixture has finite-window spin/CAR
vector difference about 1.76433e-4 at both t=+128 and t=-128.
The largest packet norm-squared deficit in those windows is about
4.39e-8. These are finite-window values; they are not certified errors
for the infinite-lattice vector. Grid doubling changes the sampled
coefficients by less than 4e-16, and the independent packet quadrature
discrepancy is below 5e-15 on its selected sites. The transfer-clock
fixture uses a Gaussian Schwartz kernel solely to test S12–S16 signs;
it is not offered as evidence of compact positive transfer. Compact
support, almost locality and all norm derivatives are proved in §3.

Nine exact whole-source mutants and their literal diffs are retained in
`mutants/`. Every one is rejected by the unchanged complete suite.
The complete result files retain all rows, including every survivor;
`MUTANT_RESULTS.json` records both changed and exactly unchanged
row data comparisons against the baseline.

| Exact mutation | Discriminating failure and preserved blind spot |
| --- | --- |
| Erase incoming phase | Negative-time n=2,3,6,7 cones and the incoming pair fixture fail; n=1,4,5 retain even reversal parity |
| Count CAR occupancy on the right | Determinants and odd reversal-parity cone cases fail; n=4 remains insensitive to the resulting global even sign |
| Permit a second spin flip at one site | Dense Pauli products and the same-site zero-vector test fail; every already separated cone remains insensitive |
| Divide by n! instead of sqrt(n!) | Independent occupation/Gram norms and determinant amplitudes fail; equal wrong source/target norms still pass a norm-ratio comparison |
| Sort momentum instead of velocity | The n=3 amplitude fixture fails; n=2 has the same order and the chosen n=4 tuple has two compensating inversions, so both survive |
| Delete the second velocity branch | Three actual one-particle branch vectors and all selected map norms/amplitudes fail |
| Reverse packet energy time | Direct quadrature and both large-time pair fixtures fail; grid refinement and packet norms survive |
| Reverse spatial Fourier character | Direct quadrature and both large-time pair fixtures fail; grid refinement and packet norms survive |
| Reverse transfer energy | All four direct actual-character filter comparisons fail |

The momentum-order survivor is particularly instructive: a norm check
cannot distinguish different unit-modulus sorting signs, and a selected
tuple can have equal sorting parity by accident. The amplitude witness
rejects that exact wrong rule, while the all-momenta result remains the
analytic alternating-sign identity of §7. Likewise, the pair-error
identity alone passes under a wrong incoming sign because its reference
is the error for the supplied sign; the independently fixed reversal
and actual Fourier controls are needed to discriminate that change.

The first baseline execution passed without a numerical repair. All
nonzero scientific-control exits are the retained intentional mutants.
A separate real 0.08-second timeout witness exits 124 and preserves its
partial output. Pre-freeze patch context mismatch and a later read-only
lookup using nonexistent inventory names are disclosed in
`OPERATIONAL_HISTORY.md`; neither changed the analytic argument or hid a
scientific failure. The originally truncated baseline display was
recovered by reading every complete result row, and every changed mutant
row was then read in full. No parent control was rerun.

The source-bound command receipts record exact argument vectors, source
hashes, wall times, bounded subprocess timeouts, complete stdout/stderr
and exit codes. `SOURCE_PINS.initial.json` preserves the earlier pending
parent-acceptance state; `ANALYTIC_FREEZE.json` and
`SOURCE_PINS.final.json` record the subsequently accepted exact parent.
The checked external theorem is NSY Theorem 3.1 as matched in §2.
`external_raw/` inventories its original source archive, TeX and prior
fetch receipt. Those bytes, and the literal source-read stdout, remain
outside the publication set. No unrelated mathematical theorem or
abstract scattering theorem is silently imported.

The scope stress check distinguishes eight issues: alternative direct
and filtered creator routes; independence of the parent identification
from the new all-n argument; explicit locality, ordering and full-domain
hypotheses; no residual claim outside the chosen GNS; bounded theorem
wording; the actual density and filter closure achieved here; the
momentum-order and branch-deletion counterexamples; and preservation of
the parent's non-Lorentz result and numerical blind spots. These are
scope checks for this positive conditional theorem. They are not a
universal no-go packet, five substitute proof routes, or an audit verdict.
The remaining action is independent review of this new note and its
evidence, followed by root's separate publication decision. No editable
prompt, axiom, audit status, Git state or repository execution surface
was changed by this author task.


## Publication evidence and limits

**Author/checker pairing:** Same selected model family and reasoning effort, separate author/reviewer contexts with candidate formulas exposed; not blinded or diverse-family. Root supplied routes and is a coauthor. Mechanical packaging adds no independent scientific review.

The n=8-only incoming-phase mutation survives all 95 author rows; the independent literal 256-by-256 integer matrix gives squared error four versus zero. Occupation insertion overlaps the author mechanism; compact-filter and n=8 matrices are distinct calculations. Cutoffs T=20,40,80,160 failed the unchanged 1e-6 filter gate; T=320 refinement passes. All finite-window, clock and sorting subcase survivors remain. No finite suite proves all-n or infinite-volume completeness.

Hashes quoted in the original argument identify frozen probe inputs, not the administratively renamed canonical notes; the publication map records that lineage. The complete original note, separate source review, root coverage, all author/reviewer sources, raw results, failed attempts and refinement history are reconstructable from the [evidence map](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/62d316633190ad2198fdfa91fc52192551990034/.claude/science/physics-loops/toe-supplied-chain-20261012/EVIDENCE_MAP.json). Raw external papers remain outside the packet, with [version/source identities](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/62d316633190ad2198fdfa91fc52192551990034/.claude/science/physics-loops/toe-supplied-chain-20261012/EXTERNAL_SOURCE_INVENTORY.json). Canonical execution and whole-source replay outcomes are not predeclared; the root execution receipt records their actual outcomes.

This three-note milestone selects one integrable one-dimensional model and scaling family. It imports no massive-carrier theorem or pending local-algebra route. Exact finite-spacing Lie closure still fails. No interacting, local-net, 3D, physical-selector, interval or new Lean certificate is supplied. Global combined validation and strict audit lint remain separate independent landing gates; no audit verdict or retained promotion is applied.

Direct proof input: [the supplied concrete chain](CONCRETE_GAPPED_CHAIN_BOUNDED_THEOREM_NOTE_2026-10-12.md), at its full-spin construction and actual-generator scope.
