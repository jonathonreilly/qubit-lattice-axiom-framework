---
claim_id: "concrete_gapped_chain_bounded_theorem_note_2026-10-12"
claim_type: bounded_theorem
claim_scope: "Chosen one-dimensional g>J>0 symmetric spin chain and its explicitly constructed full-spin GNS: conserved canonical current, actual weighted generator, gap and controlled packet residual. Exact finite-spacing scalar Lie closure fails; no framework-selected dynamics or physical identification."
upstream_dependencies:
  - weighted_current_closure_bounded_theorem_note_2026-10-12
  - gapped_boost_invariance_bounded_theorem_note_2026-10-12
  - microscopic_boost_flow_bounded_theorem_note_2026-10-12
runner: scripts/concrete_gapped_chain_2026_10_12.py
artifact_role: theorem
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: partially_closes
conditional_surface_status: "Specified one-dimensional transverse-Ising diagnostic; mathematical realization and infrared operator bounds, with no framework or physical identification"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
target_claim_id: "gapped_chain_scattering_bounded_theorem_note_2026-10-12"
target_blocker_text: "existence of a common concrete representation"
source_of_blocker_text: "handoff"
next_trace_action: "Use the supplied full-spin model only at its stated hypotheses in the paired Scattering and Continuum notes; retain the finite-spacing Lie failure and all broader framework obligations."
claim_type_reason: "Conditional theorem for the explicitly supplied one-dimensional model and stated hypotheses; finite controls supplement the full argument and confer no retained or framework-realization status."
---

**Type:** bounded_theorem


**Publication status:** Completed source review and root integration found no required mathematical correction at the frozen original identity. Author-era pending-review statements below are preserved historical chronology and are superseded by this status. The complete argument remains unchanged.



# A concrete gapped spin chain: conserved current, actual boost, and a controlled residual

**Author construction, 2026-10-12; independent review pending.** Root supplied
the unverified candidate and exploratory coefficients and is a contributor.
The construction below is a mathematical test of one specified one-dimensional
spin model. Its dynamics, couplings and state are not derived from the
framework axioms. No three-dimensional model, exact Lorentz representation,
TOE, physical-particle identification or empirical claim follows.

For every real `g>J>0`, the symmetric density has an exactly conserved
canonical current. The weighted current–boost bracket is a distinct local
stress derivation, and fails equality to any scalar multiple of the energy
derivation. An explicit exponentially localized spin automorphism constructs
a pure translation-invariant state whose **full spin** GNS Hamiltonian is
positive, has a simple vacuum, and has gap `2(g−J)`. The same construction
identifies the canonical boost and current on that entire representation.
On the actual one-particle sector the residual is multiplication by
`i E(k)(cos(k)−1)` after the stated normalization. Sections 8–9 bound its
action and integrated covariance on momentum-supported packets, including
the restriction on how long the packet remains in the patch.

These are author proofs with different-method author calculations. Neither
the computational checks nor the previously reviewed conditional lemmas
constitute an independent review of this new spin-to-Fock construction.

## 1. Contract, inputs and provenance

Write S for this note's directory. Evidence is under
`S/concrete_gapped_chain/`. The target is the density

\[
 h_x=-JX_xX_{x+1}-{g\over2}(Z_x+Z_{x+1}),\qquad g>J>0,
 \quad x\in\mathbb Z.                                      \tag{C1}
\]

The site algebra is `M_2(C)`, the algebra is its quasilocal tensor product,
and translations send site x to site x+a. Units set the lattice spacing and
the coefficient in the Schrödinger generator to one. These are explicit
model choices, not primitive-registry consequences. The minimal axiom memo
and registry were read; none of the registered scale, kinetic-isotropy or
realized-state primitives is used to supply C1 or its state.

The complete following frozen arguments and reviews were read before reuse:

| Source | SHA-256 | Use |
|---|---|---|
| [Weighted-current criterion](WEIGHTED_CURRENT_CLOSURE_BOUNDED_THEOREM_NOTE_2026-10-12.md) | `561cc0109580b74c42b19af27ab35801deea61a9c304dc2f43da772e042448f7` | Finite orbit-moment reduction; also directly evaluated below |
| [Gapped-vacuum invariance](GAPPED_BOOST_INVARIANCE_BOUNDED_THEOREM_NOTE_2026-10-12.md) | `94d1f879927135d378dcafb6e9b603465155906a71fed5ca301b4354566cea14` | Separately matched cross-check on boost-state invariance |
| [Weighted boost flow](MICROSCOPIC_BOOST_FLOW_BOUNDED_THEOREM_NOTE_2026-10-12.md) | `7ec1d7eecb4eba020548eba8b56dff66712f52b4eba634ba276dd67440d28de7` | Actual finite-range spin boost flow and its local cyclic action |

Their review identities, instruction snapshots, initial source identities and
installed/repository skill comparisons are in `sources/manifest.initial.json`.
The root lead was read as a proposal at SHA-256
`4fff67ff5b15e5a1b750d7a9b6d475e2eb96e7cd89a07f1ae0b6be5e2c510b6d`.
Its root helper/results were not imported by either new computation. The lead
discloses a correction to its exploratory path metadata; no mathematical
conclusion here depends on those fixtures or their metadata.
Root also supplied a supplemental suggestion to construct the full spin
automorphism and test cancellation of the boost connection. That coauthor
lead is captured in `sources/root_supplemental_route.txt`; this is not a
blinded or independent construction relative to root.

The pending integrated-covariance note is not a premise and was not read.
The main/planning/check-out revisions are the parent-specified
`a13caa4885f547c8d206265b031ba7649e539fd9`,
`3a4b2c66a1ead7a1c48b4359627e968f681e3c39`, and
`dc7f415f73df3754653f4985382ca0fb96f07cda`. No Git action was performed.
The scoped source search found an existing transverse-Ising strip diagnostic,
not this weighted operator construction. Literature already contains the
Ising dispersion and conserved energy current: no novelty claim is made for
those facts. The contribution tested here is the matched density, full-spin
realization, actual weighted generator, and operator residual with its domains.

## 2. Exact local current and conservation

For local A define finite sums

\[
 \delta_hA=i\sum_x[h_x,A],\quad
 \delta_bA=i\sum_xx[h_x,A],\quad
 p_x={i\over2}\sum_r r[h_x,h_{x+r}],\quad
 \delta_pA=i\sum_x[p_x,A].                                \tag{C2}
\]

Only r=±1 contributes. Using `[X,Z]=−2iY`,

\[
 [h_0,h_1]=iJg(Y_1X_2-X_0Y_1),\qquad
 [h_0,h_{-1}]=iJg(X_{-1}Y_0-Y_0X_1),
\]
\[
 p_0={Jg\over2}(X_{-1}Y_0+X_0Y_1-Y_0X_1-Y_1X_2).
                                                               \tag{C3}
\]

This is the literal canonical density. Finite relabeling on each local
observable gives the equivalent unweighted representative

\[
 p'_x=Jg(X_xY_{x+1}-Y_xX_{x+1}),\qquad \delta_{p'}=\delta_p.
                                                               \tag{C4}
\]

Do not identify C3 and C4 as literal local operators. Padding a finite
Hamiltonian and first moment around supp A, finite Jacobi and pair
symmetrization give `[δ_h,δ_b]=δ_p`, with exactly the half in C2.

Put `f_x=X_xX_(x+1)+Y_xY_(x+1)` and `u_x=X_xZ_(x+1)X_(x+2)`.
A direct multiplication using C4 gives

\[
 r:=\delta_p(h_0)
 =Jg^2(f_{-1}-f_1)+2J^2g(u_0-u_{-1}+Z_0-Z_1).              \tag{C5}
\]

For transparency the separate contributions are

| Energy term | Its δ_p action |
|---|---|
| `−J X0 X1` | `2J²g(u0−u−1+Z0−Z1)` |
| `−(g/2) Z0` | `Jg²(f−1−f0)` |
| `−(g/2) Z1` | `Jg²(f0−f1)` |

Every nonidentity translation orbit in C5 has coefficient sum zero. Thus
`δ_r=0`: in its action on a local observable the translated differences
cancel by a finite change of index. Finite Jacobi gives
`δ_r=[δ_p,δ_h]`, so

\[
 [\delta_h,\delta_p]A=0\quad\text{for every local }A.        \tag{C6}
\]

This is exact operator conservation for arbitrary real J,g, not merely a
ground-state expectation, a finite-volume spectral coincidence, or samples
of parameters. Positivity/gap will require the stricter C1 regime later.

## 3. The actual weighted stress and exact scalar-closure failure

On local inputs the ordered bracket is
`[δ_p,δ_b]A=i sum_x x[τ_x(r),A]`. For any finite difference,

\[
 i\sum_xx[\tau_x(q-\tau_1q),A]=\delta_qA.                 \tag{C7}
\]

All nonzero summands on the given local input form a finite set. No
unbounded operator sum or discarded infinite boundary is used. An explicit
primitive for C5 is

\[
 a=Jg^2(f_{-1}+f_0)+2J^2g(-u_{-1}+Z_0),\qquad r=a-\tau_1a.
\]

Consequently the unweighted stress representative can be chosen as

\[
 \boxed{t_0=2Jg^2(X_0X_1+Y_0Y_1)
              +2J^2g(Z_0-X_0Z_1X_2),\quad
        [\delta_p,\delta_b]=\delta_t.}                    \tag{C8}
\]

Its four coefficients are also the negatives of the first translation
moments of the four orbits in C5. For any real scalar β,

\[
 t-\beta h\ \sim\ (2Jg^2+\beta J)X_0X_1+2Jg^2Y_0Y_1
 +(2J^2g+\beta g)Z_0-2J^2gX_0Z_1X_2,                    \tag{C9}
\]

where `~` means equality of unweighted derivations. A nonzero finite Pauli
orbit sum cannot have zero derivation: collect translates with a
nonidentity factor at site zero, commute with the full one-site matrix
factor, and use its zero partial trace to force the collected operator to
vanish; finite tensor-word independence then forces the orbit coefficient
to vanish. The YY coefficient `2Jg²` in C9 therefore rules out
`δ_t=βδ_h` for every β when Jg≠0. The independent XZX orbit is another
witness. This exact conclusion quantifies only over β at this fixed density.

At J=0 or g=0, all h_x commute, p=t=0, and a nonzero energy derivation
would require β=0 for scalar closure. Those edges do not supply the
positive-β diagnostic. At g=J>0 the algebra remains valid but the gap and
the analytic construction below cease to meet their hypotheses.

## 4. Density improvements are consequential

Let

\[
 h_x^{\eta}=h_x-\eta g(Z_x-Z_{x+1}),\qquad \eta\in\mathbb R.
                                                               \tag{C10}
\]

The energy derivation is unchanged, while `δ_b^η=δ_b−ηg δ_Z`.
Recomputing the current gives the representative

\[
 p_x^{\eta}=Jg\big[(1+2\eta)X_xY_{x+1}
                         +(-1+2\eta)Y_xX_{x+1}\big].     \tag{C11}
\]

The unweighted density for `[δ_h,δ_p^η]` has orbit representative

\[
 8J\eta g^2(-X_0X_1+Y_0Y_1)
       +8J^2\eta g(Z_0+X_0Z_1X_2).                       \tag{C12}
\]

It is nonzero for Jgη≠0. In particular the asymmetric onsite convention
`η=1/2`, namely `−JXX−gZ_x`, does not retain this conservation identity.
The energy dynamics and its state/gap survive; its chosen first moment and
current change. This prevents transferring the result by identifying energy
derivations alone. Adding a constant multiple of H by shifting the origin
of B does preserve the commutators, and is a different operation from C10.

## 5. The spin/CAR distinction and an explicit spin automorphism

Let Θ be the spin parity automorphism, sending X,Y to −X,−Y and fixing Z.
Only the even spin and even CAR algebras are identified intrinsically here.
On each finite interval the Jordan–Wigner expressions

\[
 a_x=\Bigl(\prod_{y<x}Z_y\Bigr)X_x,\qquad
 b_x=\Bigl(\prod_{y<x}Z_y\Bigr)Y_x                         \tag{C13}
\]

use the **finite interval's** left endpoint. Even products are independent
of that endpoint upon enlarging the interval. They therefore define a
compatible isometric *-isomorphism between the two even quasilocal
algebras. The odd expressions in C13 are not asserted to be elements of
the bilateral spin quasilocal algebra.

The finite identities needed are

\[
 Z_x=-ia_xb_x,\quad X_xX_{x+1}=-ib_xa_{x+1},\quad
 Y_xY_{x+1}=ia_xb_{x+1},\quad X_xZ_{x+1}X_{x+2}=-ib_xa_{x+2}.
                                                               \tag{C14}
\]

Write a quadratic form as `(i/4) γ^T A γ` with A real antisymmetric.
Then `i[Q,γ]=Aγ` by the CAR, and its Hermitian one-body matrix is `K=iA`.
Use `(Ff)(k)=sum_x exp(−ikx) f_x`, with normalized measure `dk/(2π)`;
`Xf_x=x f_x` becomes `i∂_k`. For C1 the matrix, eigenvalues, and a
constant reference matrix are

\[
 K(k)=\begin{pmatrix}0&2i(g-Je^{-ik})\\-2i(g-Je^{ik})&0\end{pmatrix},
 \quad E(k)=2\sqrt{g^2+J^2-2gJ\cos k},\quad
 C=\begin{pmatrix}0&i\\-i&0\end{pmatrix}.                   \tag{C15}
\]

Thus `K²=E²1`; this identity alone is not yet a spin-GNS theorem.
Set `r=J/g∈(0,1)` and define periodic real functions and matrices

\[
 \theta(k)=\operatorname{Im}\log(1-re^{-ik})
          =\sum_{n\ge1}{r^n\over n}\sin(nk),\qquad
 D(k)=e^{i\theta(k)\sigma_z/2},\qquad K=E D C D^* .         \tag{C16}
\]

The series and all derivatives converge uniformly. Its oddness gives
`D(−k)=overline(D(k))`, the reality needed for a Majorana orthogonal map.
There is no winding or antiperiodic eigenframe: `Re(1−re^(−ik))>0`.
This check is specific to r<1.

The map is implemented on the **full spin algebra** by a different,
ordinary spin interaction. Its terms on `[x,x+n]`, n≥1, are

\[
 Q_{x,n}={r^n\over8n}
   \left(Y_xZ_{x+1}\cdots Z_{x+n-1}X_{x+n}
        +X_xZ_{x+1}\cdots Z_{x+n-1}Y_{x+n}\right).          \tag{C17}
\]

An empty interior product is one. In even CAR notation these are
`i r^n(a_xa_(x+n)−b_xb_(x+n))/(8n)`. The generator matrix is
`L(k)=i θ(k)σ_z/2`, so its unit-time Majorana action is precisely D.
The factor 1/8 follows from the 1/4 quadratic-form convention and the two
orientations; at first order, `i[Q,−g sum Z]=(J/2)sum(XX−YY)`, which
removes the pairing part of `−J sum XX` with the displayed sign.

Here is the checked existence input. [Nachtergaele–Sims–Young,
arXiv:1810.02428v2](https://arxiv.org/abs/1810.02428v2), Theorem 3.5,
constructs the norm thermodynamic dynamics for interactions of finite
F-norm. Its definitions, Theorems 3.1, 3.4–3.5 and their required setting
were read in the acquired original TeX. We use finite-dimensional spins,
zero separate onsite Hamiltonians, autonomous bounded Hermitian terms,
`Z` with its usual metric, and exhaustive intervals. These meet its
algebraic and continuity hypotheses.

To check the summability hypothesis, choose `0<μ<−log r` and
`F_μ(d)=exp(−μd)/(1+d)^3`. Splitting the convolution at half the separation
shows a finite convolution constant bounded by
`16 sum_z(1+|z|)^(−3)`. At distance d, at most n+1 intervals of length n
contain a given pair, and `||Q_(x,n)||≤r^n/(4n)`. Hence

\[
 \sum_{Z\ni u,v}\|\Phi_Q(Z)\|
 \le {1\over2}\sum_{n\ge\max(1,|u-v|)}r^n,
 \qquad \|\Phi_Q\|_{F_\mu}<\infty.                       \tag{C18}
\]

This proves existence of a spin automorphism β, the unit-time Q flow,
without assuming an interacting vacuum, a gap, or implementability of D
in the original product-state Fock representation. On the even algebra it
has the action D: finite-interval CAR identities give it before the limit;
the bounded, exponentially summable matrix L has strongly convergent
finite cutoffs, and CAR smeared fields are norm-continuous in their
`ℓ²` arguments. This passes the equality to every even finite product.
Translation invariance and Θ-invariance of Q, preserved under its limits,
make β commute with translations and Θ.

We will use the following elementary lift lemma, rather than identifying
odd spin and odd CAR algebras.

**Even-algebra lift lemma.** An automorphism ρ of the infinite spin algebra
that fixes its even algebra pointwise is either the identity or Θ. A
point-norm continuous path of such automorphisms starting at the identity
is the identity throughout.

Proof: the relative commutant of the even spin algebra in the spin
quasilocal algebra is scalar. Indeed, for a commuting C take a norm-close
local conditional expectation `C_Λ`. Commutation with the finite even
algebra forces `C_Λ=aI+b prod_(x∈Λ) Z_x`. Commuting with `X_xX_y`, with
x∈Λ and y outside, gives `|b|≤||C−C_Λ||`. Let Λ exhaust the chain.
Now `U=X_0ρ(X_0)` commutes with the entire even algebra, since
`ρ(X_0) A ρ(X_0)=ρ(X_0AX_0)=X_0AX_0` for even A. Thus
`ρ(X_0)=λX_0`, with λ=±1. Every odd A equals `(AX_0)X_0`, with even
first factor, so ρ is as claimed. The two values are separated by norm
two on X_0, proving the path assertion. This also explains why a putative
continuous, freely adjustable odd-sector phase is not an allowed spin
automorphism fixing the even algebra.

## 6. Constructing the full spin GNS state and its simple gap

Let `e_n=(2π)^(−1)∫ E(k) exp(−ink) dk`, so `e_(−n)=e_n∈R`.
For `0<ρ<−log r`, the factorization

\[
 E(k)=2g\sqrt{1-re^{ik}}\sqrt{1-re^{-ik}}
\]

is analytic in `|Im k|<−log r`. Contour shifting gives the explicit bound

\[
 |e_n|\le C_\rho e^{-\rho|n|},\qquad
 C_\rho=2g(1+r e^\rho).                                  \tag{C19}
\]

On the even algebra C16 conjugates the energy dynamics to the
number-conserving dynamics with formal quadratic form
`sum_(x,y) e_(y−x)c_x^*c_y`, where `c_x=(a_x+i b_x)/2`.
Define this **as a spin interaction** by the local even expressions

\[
 q_x^E=e_0 n_x+\sum_{n\ge1}e_n F_{x,n},\quad
 n_x=(1-Z_x)/2,\quad
 F_{x,n}=c_x^*c_{x+n}+c_{x+n}^*c_x
 ={X_xZ_{x+1}\cdots Z_{x+n-1}X_{x+n}
   +Y_xZ_{x+1}\cdots Z_{x+n-1}Y_{x+n}\over2}.              \tag{C20}
\]

The sums per center converge in norm. C19 gives finite F_μ-norm by the
same interval count as C18, taking μ<ρ. Its spin dynamics α^E therefore
exists. On the even spin algebra `β α^h_t β^(−1)=α^E_t` by C16 and
finite quadratic evolution. The two sides are point-norm continuous
automorphism families; their relative automorphism fixes the even algebra.
The lift lemma gives equality on **every spin observable**.

Let ω_0 be the product state with Z_x=+1 at every site. Its spin GNS space
has orthonormal basis indexed by all finite subsets of Z of flipped spins.
This identifies it with the full fermionic Fock space
`F_−(ℓ²(Z))=direct_sum_(n≥0) wedge^n ℓ²(Z)`, without a parity restriction.
In this representation, the half-line parity used in C13 is well defined
on each finite-subset basis vector and extends to a bounded unitary. It
defines CAR operators on this Hilbert space, not new quasilocal spin
elements. The product spin representation is irreducible: an operator
commuting with every local Z is diagonal in this basis, and commuting with
the local X operators makes all its diagonal entries equal.

Every term of C20 annihilates the product vacuum Ω. Finite spin cutoffs
therefore preserve ω_0, and their norm limit α^E does too. On the n-particle
sector the generator is `sum_(j=1)^n E_j`; the finite hopping matrices
converge strongly to the bounded one-body E. Their second quantizations
converge strongly on each fixed particle sector and then on Fock space by
finite-sector approximation. Thus the canonical product-GNS energy is
exactly `dΓ(E)`, with no scalar vacuum energy left.

Now set

\[
 \omega=\omega_0\circ\beta,\qquad \pi=\pi_0\circ\beta.
                                                               \tag{C21}
\]

Because β is onto, `(π,F_−(ℓ²(Z)),Ω)` is the full cyclic GNS representation
of ω. Its state is pure and translation invariant. The exact conjugacy above
identifies the canonical energy generator and spectrum:

\[
 H=d\Gamma(E),\quad m:=2(g-J)>0,\quad
 m\le E(k)\le2(g+J),\quad
 \ker H=\mathbb C\Omega,\quad
 \operatorname{spec}H\subset\{0\}\cup[m,\infty).           \tag{C22}
\]

The one-particle subspace is all `L²(T,dk/(2π))`. Packets supported in
arbitrarily small neighborhoods of k=0 have energies approaching m, so
the infimum of the nonzero spectrum is exactly m. This is a full spin-GNS
gap, not the larger even-Fock threshold 2m, and not an inference from finite
periodic boundary sectors. Since E is bounded above and below by positive
constants, `Dom H=Dom N` as sets, with equivalent graph norms.

No claim about uniqueness among every possible algebraic ground state is
needed. This constructs one pure state and its actual simple gapped GNS
Hamiltonian for every g>J>0. It also verifies all hypotheses G1–G6 of the
frozen gapped-invariance theorem: finite range/norm (`R=1`, `||h||≤J+g`),
the actual invariant energy flow, C22, and the operator conservation C6.
That theorem independently supplies the local state identities for the
same current and first moment. It is not used circularly to construct ω.

## 7. Identifying the actual weighted boost and its full domains

The spatial first moment in C2 has onsite coefficient `g(x−1/2)` and
nearest-neighbor Majorana bond coefficient `Jx`. Thus its Hermitian
one-body operator is, on smooth periodic two-component functions,

\[
 L_B={1\over2}\{X-1/2,K\}
     =iK\partial_k+{i\over2}K'-{1\over2}K.                 \tag{C23}
\]

This calculation uses the same bond density C1: the average of `x−1/2`
and `(x+1)−1/2` is x. It is not a boost guessed from the dispersion.
Conjugating C23 by D, with `D^*D'=iθ'σ_z/2`, gives

\[
 D^* L_B D=C b,\qquad
 b=i\left(E\partial_k+{E'\over2}\right)-{E\over2}.         \tag{C24}
\]

The extra matrix term is `(iE/2){C,D^*D'}` and vanishes because
`{C,σ_z}=0`. In particular the derivative of the eigenframe cancels the
off-band part; ignoring it would invalidate the identification. The term
`−E/2` is the retained origin convention, not an omitted Berry term.

Here is a domain proof. Since E is positive, smooth and periodic, the
coordinate `q(k)=∫_0^k du/E(u)` identifies the k-circle with a circle of
length `L=∫_(−π)^π dk/E(k)`. The unitary coordinate change multiplies a
wavefunction by `sqrt(E)` and sends b to
`i∂_q−E(k(q))/2`. The derivative with periodic H¹ domain is self-adjoint
by its Fourier basis; the real bounded multiplication perturbation
preserves self-adjointness on that domain. Pulling back yields

\[
 \operatorname{Dom}b=H^1_{\rm per}(\mathbb T),
 \qquad C^\infty_{\rm per}(\mathbb T)\text{ and trigonometric
 polynomials are cores.}                                  \tag{C25}
\]

Smooth multiplication and the smooth coordinate change preserve H¹ and
give equivalent graph norms. This also proves essential self-adjointness
of C23: D is a smooth periodic unitary, and Cb is the direct sum of b and
−b in a constant frame. Its unitary flow preserves smooth periodic
functions, hence Schwartz sequences on Z, with bounded Schwartz seminorms
on each compact time interval. One can see this directly from the complete
smooth vector field E and its smooth Jacobian/phase.

To make C24 an identity of **actual spin flows**, define another spin
zero-chain, using the number-conserving strings C20:

\[
 b_x^E=(x-1/2)e_0n_x
       +\sum_{n\ge1}\left(x+{n-1\over2}\right)e_nF_{x,n}.
                                                               \tag{C26}
\]

Its one-body matrix is `{X−1/2,E}/2`, exactly b. For each `0<μ<ρ`, C19
implies `||b_x^E||_(G,x)≤C(1+|x|)` for `G(R)=exp(−μR)`;
indeed the norm/tail sums are bounded by
`C_ρ sum_(n≥0)(1+|x|)(n+1)exp(−ρn)`, with the tail starting at n>R.
For each local spin A, distant centers contribute an absolutely summable
`(1+|x|)exp(−μ dist(x,supp A))` commutator bound.

We apply [Teufel–Wesle–Wessel, arXiv:2511.02941v2](https://arxiv.org/abs/2511.02941v2),
Theorem 8, to C26. Its growth, locality and unconditional-generator
hypotheses have just been checked. For clarity its required **bounded**
zero-chain LR hypothesis holds for the selected G as follows. Telescope a
bounded G-local zero-chain of norm M into ball shells; the radius-n shell
has norm at most `(1+exp μ)M exp(−μn)`. On Z a pair lies in at most 2n+1
such balls. With

\[
 D_\mu=1+(1+e^\mu)\sum_{n\ge1}(2n+1)(1+2n)^3e^{-\mu n/2}<\infty,
 \quad C_*=16\sum_z(1+|z|)^{-3},
\]

the resulting interaction has norm at most `C_*D_μ M` for the normalized
kernel `C_*^(−1)exp(−μd/4)/(1+d)^3`, whose convolution constant is at most
one. NSY's Theorem 3.1 gives the required LR bound with
`F(R)=exp(−μR/4)`, prefactor 2, and speed constant `8 C_*D_μ/μ`.
Explicitly the sum of this normalized kernel over y at distance at least
R from a fixed x is at most `exp(−μR/4)`, since
`C_*^(−1) sum_z(1+|z|)^(−3)=1/16≤1`. Absorbing the temporal factor
`exp(2 C_*D_μ M|t|)` into R gives that speed; inside the resulting cone
the trivial commutator bound supplies prefactor 2.
Both decay exponents in TWW are infinite; the lattice volume bound has
D=1. Spin conditional expectations are contractive and nested and disjoint
spin factors commute, precisely the properties used by that theorem's
proof. Thus its spin application supplies an actual point-norm group
`λ_s^E`, with rapid almost-local preservation, for C26.

The original TWW definitions, Theorems 7–8, their proofs and relevant
appendix were read in the ancestor's raw original TeX. The cutoff-radius
typo and the enlarged local norm constant disclosed in the frozen
weighted-flow source are handled here with radius k/2 and a factor at most
`3(1+L)^ν`, respectively. For C26 the corrected generator tail is
`O(k² exp(−μk/2))` plus an exponentially small outer-center sum. No faulty
radius estimate or unproved arbitrary-decay version is used.

Every term in C26, including each TWW cutoff, annihilates Ω in the product
GNS representation. Hence ω_0 is λ^E-invariant. Its canonical implementer
is exactly `dΓ(b)`: on finite-particle finite-position vectors the absolute
matrix sums give that action; these vectors are a core. For the latter
claim, finite-position vectors are trigonometric polynomials under Fourier
transform and hence a core for b by C25; their finite antisymmetric tensor
products are a core for each finite sum `sum_j b_j`, by spectral/tensor
approximation, and finite-sector truncations are a core for the Hilbert
direct sum. There is no freely chosen odd-sector additive constant.
For the stated cutoff this vacuum claim can be checked term by term:
the center x is retained, so its onsite n_x is retained; a hopping string
is either wholly inside `B_(k/2)(x)` or has an exterior traceless endpoint
and its conditional expectation is zero. No nonzero constant vacuum
term is introduced by the conditional expectations.

The finite-cutoff identification on the even algebra is also controlled
for the unbounded first moment. Its matrices converge on every Schwartz
sequence to C23/C26, uniformly when that sequence ranges over a compact
time orbit of the limiting smooth flow. A direct bound splits indices at
k/4: outer indices have arbitrarily small polynomial tails, and long
matrix bonds have exponential tails C19, even after their linear spatial
weights. Duhamel's formula consequently gives, for such f,

\[
 \|(e^{isL_k}-e^{isL})f\|
 \le\int_0^{|s|}\|(L_k-L)e^{\pm iuL}f\|\,du\longrightarrow0.
                                                               \tag{C27}
\]

The sign is the orientation of s. Density and unitarity extend convergence
to all one-body vectors. Finite CAR bilinears then converge in norm.
Here is a more explicit tail justification for C27. In a cutoff of radius
M, separate f into `|x|≤M/4` and its complement. On the complement,
`||L_M||≤C(1+M)` and
`||Lf||≤C||(1+|X|)f||`, so every desired inverse power of M follows
from a higher weighted ℓ² seminorm of f. For the inner part, an omitted
matrix entry must have a bond of length at least M/4. Its coefficient is
bounded by `C(1+|x|+|y|)exp(−ρ|x−y|)` by C19. Summing these tails in
both row and column indices and applying the Schur bound gives at most
`C(1+M)²exp(−ρM/8)||f||`. Combining the two pieces yields, for every
integer N≥1 and all sufficiently large M,

`||(L_M−L)f|| ≤ C_N(1+M)^(−N)||(1+|X|)^(N+2)f||`
`+ C(1+M)²exp(−ρM/8)||f||`.

The same argument is simpler for the finite-range original matrix.
The limiting flows preserve the required weighted seminorms uniformly
on compact time intervals by C25, so this bound justifies the uniform
dominated integral in C27. Endpoint floors only enlarge the constants.
Combining this with the norm spin-cutoff limits shows that
`β λ_s^b β^(−1)` and `λ_s^E` agree on the even spin algebra. The lift
lemma makes them equal on the full spin algebra. This proves exact
first-moment conjugacy, beyond a formal positive-band calculation.

Therefore in the state C21 the canonical GNS generators are

\[
 \boxed{H=d\Gamma(E),\qquad B=d\Gamma(b),\qquad
 P=d\Gamma(p),\quad p(k)=E(k)E'(k)=4Jg\sin k,\qquad
 T=d\Gamma(t),\quad t(k)=4Jg E(k)\cos k.}                 \tag{C28}
\]

For P and T, C14 gives respectively the one-body matrices `p(k)1` and
`4Jg cos(k)K(k)` directly from C4/C8. Conjugating by D makes them
number-conserving; their exponentially summable spin flows and canonical
product-state implementations follow as for C20. The same even lift
identifies the full spin flows, including their odd actions. Thus there
is no inference from even-sector equality to an assumed full lift.

Each dΓ operator has its usual self-adjoint Hilbert direct-sum domain:
the sector vector is in the domain of the sum of its one-body operators
and the squared norms of all sector images sum to a finite number.
The finite-particle smooth domain is a common invariant core. Separately,
the actual local cyclic domain `π(A_loc)Ω` is invariant under H,B,P,T
because their original local derivations are local and the canonical GNS
actions are `iG π(A)Ω=π(δ_G A)Ω`. The frozen weighted-flow and gap
theorems now apply with all their stated model hypotheses established.

On the actual one-particle sector H,P,T are bounded multiplication
operators, while B has exactly the periodic H¹ domain C25. On this domain,

\[
 [B,H]=iP,\qquad [B,P]=iT,
 \quad [H,P]=0.                                           \tag{C29}
\]

The same identities hold on the finite-particle smooth common core and
the invariant local cyclic domain just described. No separate core claim
for that local cyclic domain is needed here. These identities are
not declarations about every maximal product domain or a scalar-beta
Lorentz algebra. In particular T differs from every scalar multiple of H
as an operator on this one-particle sector too.

## 8. An operator residual bound and the geometric translation check

This section restricts to the actual one-particle reducing subspace of
C28. Put

\[
 c=\sqrt{4Jg},\qquad \mathcal B=B/c,\qquad Q=P/c=c\sin k,
 \qquad K_{\rm cur}=P/c^2=\sin k.
                                                               \tag{C30}
\]

Here c is a normalization determined by the specified couplings; it is
not an identified physical light speed. The exact one-particle dispersion
can also be written `E(k)=sqrt(m²+4c² sin²(k/2))`. From the **actual**
operator C24, not from that dispersion alone,

\[
 [\mathcal B,H]=iQ,\qquad
 [\mathcal B,Q]-iH=iE(k)(\cos k-1).                       \tag{C31}
\]

Let `0<κ<π`, and let χ_κ be the momentum projection on `|k|≤κ`, using
the representative k∈[−π,π]. Initially take ψ∈H¹ with this support.
The commutator defect in C31 is a bounded multiplication operator, so
its action extends uniquely to every ψ in χ_κL². Since E and `1−cos k`
increase with |k| on this patch,

\[
 \begin{split}
 \|([\mathcal B,Q]-iH)\chi_\kappa\|
   &=R_\kappa:=E(\kappa)(1-\cos\kappa),\\
 \|([\mathcal B,Q]-iH)\psi\|
   &\le (1-\cos\kappa)\|H\psi\|
    \le {\kappa^2\over2}\|H\psi\|.                      \tag{C32}
 \end{split}
\]

The operator-norm equality follows by packets concentrated arbitrarily
near a patch endpoint. This is a uniform bound on the relevant operator
action for every supported packet; it is not a fitted dispersion curve
or merely a small expectation value. Equivalently,
`([B,P]−ic²H)χ_κ=ic²E(cos k−1)χ_κ`.

The original spin translations also have an actual implementer here.
Since β commutes with translations and fixes their invariant-state
construction, the canonical spin translation by an integer a acts on
the finite-flip basis as `|x₁,…,x_n⟩↦|x₁+a,…,x_n+a⟩`. Its one-particle
Fourier action is

\[
 U_a\psi(k)=e^{-iak}\psi(k),\qquad a\in\mathbb Z.
\]

Consequently the current clock, with its orientation explicitly chosen,
obeys

\[
 \|(e^{-iaK_{\rm cur}}-U_a)\chi_\kappa\|
 \le |a|\sup_{|k|\le\kappa}|\sin k-k|
 \le {|a|\kappa^3\over6}.                               \tag{C33}
\]

The first inequality uses `|exp(iu)−exp(iv)|≤|u−v|`; the second follows
by integrating `1−cos u≤u²/2`. Thus the geometric/current comparison
is checked on this representation and sector. It does not identify the
current clock exactly with geometric translations, nor construct a
canonical continuous geometric translation of the spin algebra. Taking
the principal branch k as a bounded logarithm of U_1 would make a branch
choice; noninteger multipliers from it need not preserve periodic H¹.

On any fixed n-particle patch where every momentum lies in [−κ,κ], the
sum of the absolute residual multipliers is at most
`(1−cos κ) sum_j E(k_j)`. Hence the relative bound in C32 also holds
on the finite-particle smooth core there, with H the full sum. This does
not supply a particle-number-independent absolute norm bound on Fock
space. No restriction to an even parity sector is made anywhere.

## 9. Integrated control under the actual boost flow

The infinitesimal estimate is accompanied by a controlled finite-parameter
statement. Let `V_ρ=exp(−iρ\mathcal B)` on one-particle space. The smooth
complete characteristic F_ρ on the circle solves

\[
 {d\over d\rho}F_\rho(k)={E(F_\rho(k))\over c},
 \qquad F_0(k)=k,
 \qquad F_\rho'(k)={E(F_\rho(k))\over E(k)}.               \tag{C34}
\]

In a lift to the real line, `F_ρ(k+2π)=F_ρ(k)+2π`. Direct differentiation
on the smooth core, including the zeroth-order origin term in C24, gives
the **unitary** flow

\[
 (V_\rho\psi)(k)=
 \sqrt{{E(F_\rho(k))\over E(k)}}\,
 \exp\!\left({i\over2}(F_\rho(k)-k)\right)\psi(F_\rho(k)).
                                                               \tag{C35}
\]

The square root is the half-density Jacobian; deleting it loses
unitarity. The phase is periodic as written and retains the bond-origin
convention. The substitution u=F_ρ(k) proves norm preservation. Its
group property and strong continuity then give the same generator and
domain as C25, so this is the flow of the canonical boost already
identified in C28. For every bounded multiplier f,
`V_ρ M_f V_ρ*=M_(f∘F_ρ)`.

Define the actual conjugated operators

\[
 H_\rho=V_\rho H V_\rho^*=E(F_\rho(k)),\qquad
 Q_\rho=V_\rho Q V_\rho^*=c\sin(F_\rho(k)).
\]

They solve the exact multiplication-operator equations

\[
 \partial_\rho H_\rho=Q_\rho,\qquad
 \partial_\rho Q_\rho=H_\rho+R_\rho,
 \quad R_\rho=E(F_\rho)(\cos F_\rho-1).                  \tag{C36}
\]

Let ψ have support in `|k|≤κ₀`, where `0≤κ₀<κ<π`. Suppose every
characteristic starting in this patch stays in `|F_u(k)|≤κ` for
`|u|≤|ρ|`. Then `||R_u ψ||≤R_κ||ψ||`. Variation of constants in the
two-component equation C36 gives, for either sign of ρ,

\[
 \begin{split}
 \|(H_\rho-H\cosh\rho-Q\sinh\rho)\psi\|
     &\le R_\kappa(\cosh|\rho|-1)\|\psi\|,\\
 \|(Q_\rho-Q\cosh\rho-H\sinh\rho)\psi\|
     &\le R_\kappa\sinh|\rho|\,\|\psi\|.                 \tag{C37}
 \end{split}
\]

Indeed the error integrals have kernels `sinh(ρ−u)` and `cosh(ρ−u)`,
respectively; integration of their absolute values gives the displayed
constants. The multipliers are bounded, so the proof holds first on the
smooth core and then for all such L² packets by density. It requires no
unjustified interchange of unbounded operator products. The same formulas
describe the action on the transported packet `V_ρ*ψ`; its support is
F_ρ(supp ψ). The support of V_ρψ has the opposite orientation, F_(−ρ).

There is an explicit sufficient condition for the support hypothesis.
As long as the characteristic remains in the chosen coordinate patch,

\[
 {E(k)\over c}\le\sqrt{(m/c)^2+k^2},\qquad
 |F_u(k)|\le
 \kappa_0\cosh|u|+
 \sqrt{\kappa_0^2+(m/c)^2}\sinh|u|.                      \tag{C38}
\]

The first inequality is `2|sin(k/2)|≤|k|`. Compare the derivative of
|F_u| with `sqrt((m/c)²+|F_u|²)` in either time direction; solving this
scalar differential inequality gives the second. A first-exit argument
therefore proves the required support property whenever the right-hand
side of C38 at |ρ| is strictly less than κ. This is an a priori
condition, not a posteriori visual inspection of a numerical orbit.

For fixed positive m/c, shrinking κ to zero cannot keep a nonzero fixed
ρ within such a patch: even the characteristic starting at zero moves
with initial speed m/c. Thus C37 is a finite-patch, finite-parameter
estimate with stated support control. It does not assert uniform Lorentz
covariance at fixed nonzero rapidity on arbitrarily narrow patches of a
fixed massive lattice model. One can make all terms small in a family
with m/c small and κ₀ proportional to κ while preserving g>J for each
member; that family is an additional chosen scaling, not a deduction of
a continuum quantum field theory.

## 10. Reproducible evidence, source imports, and failed alternatives

The evidence is author-produced and imports no campaign helper. Its
reproduction commands and the complete logs are under
`concrete_gapped_chain/README.md` and `concrete_gapped_chain/logs/`.
Every runner was bounded by a 60-second subprocess timeout; no run timed
out. Receipts record exact commands, code hashes, software versions,
elapsed time, exit status and complete stdout/stderr. The initial symbolic
runner is preserved under `controls/revisions/`; its later extension added
checks of displayed intermediate formulas without changing the method or
results. Nothing was repaired by suppressing a failed baseline assertion.

| Control | What it independently calculates within this author work | Limits |
|---|---|---|
| `controls/local_symbolic.py` | Exact SymPy polynomials in J,g,η,β using its own sparse Pauli products; actual support-overlap sums; C3–C12 and all three one-site generator actions | Finite algebra only; proves no infinite-chain domains |
| `controls/kernel_and_matrix.py`, Laurent part | Derives current and stress from differential-operator commutators of the generic 2×2 kernel; checks the connection cancellation with arbitrary symbolic E and θ | Shares the author-specified mathematical conventions; not a blinded independent review |
| The same runner, tensor part | Separate seven-site Kronecker matrices with Gaussian-integer arithmetic at `(J,g)=(1,2),(2,3),(3,7),(0,2),(2,0)`; direct center commutators; separate three-site JW identities | Finite fixtures, not thermodynamic convergence |
| `controls/packet_flow.py` | Actual characteristic ODE, packet norms, and an independent quadrature-coordinate inversion using 45-decimal arithmetic | Illustrations, not interval arithmetic or a replacement for C32–C38 |

The integer tensor computation guards every arithmetic operation by an
upper bound below `2^60`; the largest encountered bound was 5,419,008.
Its central commutators match the infinite local formulas. It deliberately
retains the **nonzero open-boundary** commutators: for the three nondegenerate
fixtures, `maxabs([H₂,P₄])`, with `H₂=2H` and the finite canonical
`P₄=i[H₂,B₂]`, is 96, 432 and 3,528. Their commutators with central
X,Y,Z vanish. Thus no global
finite-open conservation identity was substituted for C6, and a boundary
discrepancy was not discarded as numerical error.

Known-wrong mutations were executed and retained with exit status one:
removing the current's half, reversing the orbit moment, pretending the
improvement leaves the current unchanged, reversing the CAR current,
deleting the range-two stress term, changing the connection coefficient,
using a constant characteristic speed, deleting the half-density, and
reversing the clock. The corresponding targeted controls reject each
mutation. These show sensitivity to specific mistakes; neither their
number nor successful baseline assertions establish the analytic theorem.
All failed rows and their unchanged full outputs are preserved.

For the numerical illustration, the normalized packet is proportional to
`(1−(k/κ₀)²)²` on [−κ₀,κ₀], and zero elsewhere. It belongs to the
one-particle H¹ domain. The table gives L² errors in C37, followed in
parentheses by its proved upper bound. Normalizing with dk rather than
dk/(2π) in the runner changes both packet normalizations by the same
constant and leaves these reported normalized norms unchanged.

| `(J,g; κ₀,κ,ρ)` | C38 support bound | Energy error (bound) | Current error (bound) |
|---|---:|---:|---:|
| `(1,1.05; .03,.09,.5)` | .06367691 < .09 | `1.9864e−6` (`1.0835e−4`) | `1.2523e−5` (`4.4238e−4`) |
| `(1,2; .025,.2,.1)` | .09599795 < .2 | `4.8250e−6` (`2.0730e−4`) | `1.8162e−4` (`4.1495e−3`) |

The independent implicit equation `∫_k^(Fρ(k)) c/E(u) du=ρ` agrees
with the ODE endpoint to below `3e−15` at the recorded sample points.
That observed agreement is not a rigorous global numerical error bound.

The external mathematical imports are narrowly specified:

| Primary source and inspected material | Matched hypotheses and role |
|---|---|
| [Nachtergaele–Sims–Young, arXiv:1810.02428v2](https://arxiv.org/abs/1810.02428v2), source lines 1094–1360 and 1662–1790 | The F-function definitions and Theorem 3.1 statement; Theorems 3.4–3.5 and the relevant proofs. Finite spin factors on countable metric Z, bounded autonomous Hermitian terms, finite F-norm checked in C18–C20; yields the Q and diagonal spin flows and the LR input in §7. This is an external theorem, not a new derivation of thermodynamic dynamics. |
| [Teufel–Wesle–Wessel, arXiv:2511.02941v2](https://arxiv.org/abs/2511.02941v2), source lines 151–458 and 508–959 | Complete relevant definitions, Theorems 7–8, their proofs and appendix. Even local terms, conditional expectations, unconditional generator, linear growth, exponential decay and bounded-chain LR input are checked in §7. The spin extension follows the same conditional-expectation/local-commutation proof, with the disclosed typo corrections. |
| [De Luca–Viti–Bernard–Doyon, arXiv:1305.4984v2](https://arxiv.org/abs/1305.4984v2), Sections II and IV | Context for the known Ising dispersion and heat current. Its Hamiltonian parameters map by `J_D=2J`, `h_D=g/J`. It is not used to establish any GNS, weighted domain, current normalization or theorem here. |
| [Antal–Rácz–Sasvári, cond-mat/9612047v1](https://arxiv.org/abs/cond-mat/9612047v1), model/current discussion on pages 1–2 | Context for known current conservation. Its spin normalization was not fully reconciled, so no coefficient or proof is imported. |

The NSY source section containing Theorem 3.9 was also inspected but that
theorem is not needed for this note. Searches found Araki's two-sided XY
paper and Araki–Matsui ground-state work, but full theorem hypotheses were
not obtained or imported. A Project Euclid retrieval failed; the proposed
route using those papers was therefore not treated as evidence. The full
spin state and gap above instead have the explicit author construction.

All acquired raw external sources are inventoried in
`concrete_gapped_chain/literature/inventory.json` and are **excluded from
the publication packet**. Context papers read through the web are listed
as web-only reads, without implying a local complete copy or complete
paper review. The final evidence manifest refreshes the antecedent and
instruction identities; the source search is bounded and does not assert
an exhaustive literature or open-PR novelty search.

The following scoped stress test records the negative routes without
turning them into a universal no-go:

| No-go-discipline item | Result for the actual quantifiers of this note |
|---|---|
| N1: alternative routes | Fixed scalar β fails by C9. The explicit η improvement family loses current conservation by C12. An origin shift `B↦B+aH` leaves `[B,P]` unchanged since `[H,P]=0`. Replacing the current by the branch momentum k can give the desired second commutator on an interior patch, but leaves `[B,H]=iP` with `P=c² sin k` and introduces the global domain issue described after C33. Restriction to controlled low momentum does work approximately by C32–C38. These are real alternatives examined; no claim that they exhaust all densities or interactions is made. |
| N2: wall independence | C9 and the multiplier `c²E cos k` are two calculations of the same obstruction, not independent physical walls. Density improvement dependence is a separate failed inference. No conjunction of supposed independent obstructions is used to rule out models. |
| N3: hidden assumptions | The chain dimension, C1, g>J, the state C21, normalization c, support patch and finite boost range are explicit choices. No framework primitive, unique algebraic ground-state theorem, parity-sector assumption, invisible odd lift, or implementability of β in the original vacuum is imported. |
| N4: residual match | C31 is computed for the actual canonical operator on its H¹ domain; C32 is its sharp patch norm, C33 checks the actual geometric translation, and C37 includes the transported support condition. Dispersion alone would not establish these conclusions. |
| N5: rhetoric | The failure is exact scalar closure for this density, and loss of this conserved current under C10. It is not a no-go for emergent covariance, other boosts, other spin models, higher-dimensional theories or the framework. |
| N6: partial closure | The positive partial result is the explicit full-spin gapped GNS realization and its actual one-particle boost, followed by controlled approximate covariance. These author proofs still require independent review. |
| N7: strongest counter-route | Other improved densities or different interactions could obey other algebraic relations; none is excluded. The small m/c family mentioned after C38 can enlarge the controlled finite-parameter regime, but requires an additional scaling choice and further continuum work. |
| N8: cross-cycle echo | The antecedent weighted-current note proved a conditional finite-orbit criterion. This note adds a candidate evaluated at generic parameters and a state/domain construction. Repeating the antecedent's result alone would not establish any of §§5–9. |

The hard failures retained are therefore C9, C12, global finite-open
conservation, a dispersion-only boost inference, a bilateral odd-JW
quasilocal identification, and uniform fixed-rapidity control in shrinking
patches at fixed m/c. The last three are invalid shortcuts avoided by
the construction and explicit bounds, not numerical counterexamples to
unrelated theories. Tool-level read/search issues are separately recorded
in `logs/operational_notes.json`; they are not presented as scientific
failures.

## 11. Claim ledger and review handoff

| Claim | Present status | What remains outside the claim |
|---|---|---|
| Exact current, conservation, stress and η dependence | Author algebraic theorem, exact symbolic and disjoint tensor/kernel controls | Independent review of this source revision |
| Actual full spin state, simple gap, weighted GNS operators and domains | Author construction using the checked NSY/TWW imports and the proved even-algebra lift | Independent analytic review; no assertion about every algebraic ground state |
| Low-momentum residual, geometric comparison and integrated packet control | Author operator theorem with explicit support hypotheses; numerical illustrations only | Removal of those support/time restrictions or a continuum field theory |
| Framework realization, three-dimensional dynamics, physical particles, exact Lorentz symmetry, scattering and empirical predictions | Not established or inferred here | Separate constructive work and independently checked premises |

The load-bearing review targets are the full-spin even-algebra lift,
the cutoff comparison C27, and the identification of the canonical
unbounded boost with dΓ(b). Finite calculations cannot replace those
checks. The packet estimates then follow from the explicit self-adjoint
one-particle operator and elementary ODE inequalities.

No Lean execution is claimed. If a formalization is desired, a useful
bounded obligation is the finitely supported translation-orbit lemma C7
together with the generic Pauli coefficient identities C5/C8/C12. It
would certify the signs and density dependence, while making no claim to
formalize the thermodynamic spin flow, the even lift or the GNS domain
argument. A line count or theorem count would not be evidence for those
analytic steps.

The frozen source identity, evidence identities, antecedent refresh and
run classifications are recorded in `concrete_gapped_chain/manifest.json`
and `concrete_gapped_chain/receipt.json`. This handoff has no Git action,
repository write, canonical execution, checkpoint, publication action,
audit verdict or retained-status change. No editable prompt or axiom file
was changed. The selected model and reasoning effort were preserved, and
no work was subdelegated.



## Publication evidence and limits

**Author/checker pairing:** Same selected model family and reasoning effort, separate author/reviewer contexts with candidate formulas exposed; not blinded or diverse-family. Root supplied routes and is a coauthor. Mechanical packaging adds no independent scientific review.

The raw-origin and reciprocal-Jacobian whole-source variants survive the author predicates. Independent literal-moment and complete transported-norm witnesses reject them. The original half-density row is an algebraic identity, not independent unitarity verification. The M=128 cutoff failed the unchanged 1e-10 gate; M=192 refinement and all original failures remain. Self-adjoint sector sums use maximal total-generator closures, permitting cancellations; they are not intersections of individual domains.

Hashes quoted in the original argument identify frozen probe inputs, not the administratively renamed canonical notes; the publication map records that lineage. The complete original note, separate source review, root coverage, all author/reviewer sources, raw results, failed attempts and refinement history are reconstructable from the [evidence map](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/62d316633190ad2198fdfa91fc52192551990034/.claude/science/physics-loops/toe-supplied-chain-20261012/EVIDENCE_MAP.json). Raw external papers remain outside the packet, with [version/source identities](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/62d316633190ad2198fdfa91fc52192551990034/.claude/science/physics-loops/toe-supplied-chain-20261012/EXTERNAL_SOURCE_INVENTORY.json). Canonical execution and whole-source replay outcomes are not predeclared; the root execution receipt records their actual outcomes.

This three-note milestone selects one integrable one-dimensional model and scaling family. It imports no massive-carrier theorem or pending local-algebra route. Exact finite-spacing Lie closure still fails. No interacting, local-net, 3D, physical-selector, interval or new Lean certificate is supplied. Global combined validation and strict audit lint remain separate independent landing gates; no audit verdict or retained promotion is applied.
