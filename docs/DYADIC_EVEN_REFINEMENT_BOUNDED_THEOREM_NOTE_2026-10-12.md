---
claim_id: dyadic_even_refinement_bounded_theorem_note_2026-10-12
claim_type: bounded_theorem
claim_type_reason: "Complete supplied-model conditional analytic proof; finite controls are supporting evidence, not framework selection."
claim_scope: "For the supplied one-dimensional massive free chain, explicit parity-even dyadic spin embeddings preserve physical interval support; their local inductive algebra equals the intrinsic norm-Cauchy quotient. Actual chosen states and fixed mixed flows extend using the pinned parent strong L2 limits."
upstream_dependencies:
  - concrete_gapped_chain_bounded_theorem_note_2026-10-12
  - local_even_continuum_bounded_theorem_note_2026-10-12
  - continuum_local_boost_bounded_theorem_note_2026-10-12
  - microscopic_local_boost_limit_bounded_theorem_note_2026-10-12
  - mixed_local_poincare_correlations_bounded_theorem_note_2026-10-12
runner: scripts/dyadic_even_refinement_2026_10_12.py
artifact_role: theorem
target_claim_id: null
target_blocker_text: "An intrinsic local even-spin refinement algebra and Cauchy sections for the supplied scaling family."
source_of_blocker_text: user_goal
next_trace_action: "Use the intrinsic algebra as support for a separately reviewed state-adapted locality and dynamics investigation; its terminal claims remain open."
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: partially_closes
conditional_surface_status: "Explicit dyadic even-spin inductive system and Cauchy sections; actual state and mixed-flow limits conditional on the pinned supplied massive chain theorems"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

**Publication chronology:** The complete source below is frozen at SHA-256 `646ad05eb2f3ba02b6410e4043a4f258ca84ea2c15b92a4ca7d0ab25e05ecc9c`. The later fresh source review and root source-bound verification accepted this bounded scope. Original pending-review sentences are historical, not the current review disposition. General operator-algebraic renormalization and inductive-limit machinery remain prior art.


# Dyadic refinement of the supplied chain's even spin algebra

**Author probe, 2026-10-12.** The maps below connect actual even spin
algebras at successive physical spacings, preserve physical interval
support, and identify their C*-inductive limit with the continuum even
CAR algebra. A sequence converges precisely when it satisfies the stated
intrinsic Cauchy condition under these maps. The actual chosen states and
fixed mixed time/translation/scaled-boost words pass to this limit.

The algebraic construction is proved here independently of the pending
local-UCP-section proposal. The state and mixed-flow conclusions use the
exact pinned supplied-model theorems listed below. They are conditional
mathematical conclusions, not framework selection or audit ratification.
The refinement does not make the actual finite-scale states or energy
flows exactly compatible; explicit counterexamples appear in section 8.

## 1. Contract, sources and prior art

Fix a_0,m,v>0 and a_n=a_0 2^{-n}, n in N_0. Every spin algebra is the
bilateral qubit quasilocal algebra; A_n denotes its parity-even part.
Parity changes X_j,Y_j to their negatives and fixes Z_j. Its local
algebra A_n(Lambda) is the even subalgebra of the finite spin algebra on
the finite interval Lambda. Only the even algebra enters the theorem.

Let E=`dyadic_even_refinement/`. Exact source copies, instruction revisions
and SHA-256 hashes are in E/source_inventory.json. The parent hashes are:

| Source | SHA-256 | Role |
|---|---|---|
| LOCAL_EVEN_CONTINUUM_PROBE.md | 7be1a72e2b59c5c61b68ead6d663e8d4e179b21e2497243a2859a4082ea7813b | Actual chosen state, even JW correspondence, uniform compact-time and covariance strong limits |
| CONTINUUM_LOCAL_BOOST_REVISED_PROBE.md | 59d34a51720446a554c41ec070c0b52b6dde67692c72b4c42a4937f7f4ca9d16 | Closed real Cauchy boost, continuum mixed words and specified spacetime net |
| MICROSCOPIC_LOCAL_BOOST_LIMIT_PROBE.md | 70118e0b1f7fd4fa9d041ce837f967abdd0e2f682a854d38885466fd6e4b125d | Actual scaled spin boost and its strong cell comparison |
| MIXED_LOCAL_POINCARE_CORRELATIONS_PROBE.md | 8c3a308b57a2e53d117a7c76046b4995c3a2ffc150e31cb142a90bd926796418 | Compact-parameter strong convergence of each fixed mixed word; restated in section 6 |
| CONCRETE_GAPPED_CHAIN_PROBE.md | 0aebc2ded245d9bc9ecae364db0d1a042f9642771ed788794dafd73fb7f621bd | Transitive supplied Hamiltonian, chosen ground state and actual spin-GNS flows |

LOCAL_EVEN_NET_SECTIONS_PROBE.md, hash
61d361d205fe2ecbc9e6ef0cab34fbdce5e14c9ffe8916ceaf44592c61e9a3de,
is preserved as context only. Its fresh review is open at dispatch, and
no theorem, UCP formula, or review conclusion from it is used here.
The four immediate mathematical parent arguments and their necessary
transitive arguments were read; the concrete parent was read at its
relevant sections, not given a new complete review. Historical author
status sentences inside the parents are not fresh review
receipts. Independent acceptance of this new argument remains open.

The worktree identity is 16a69597714f8c62387c2e9ee92c445c40f91410;
the main source read is a13caa4885f547c8d206265b031ba7649e539fd9 and
planning AGENTS.md is 3a4b2c66a1ead7a1c48b4359627e968f681e3c39.
Root owns the current ownership/prior-art sweep and all Git/publication
actions. Installed applicable skills match the captured main versions.
The realized-state primitive supplies no preferred ground state; the
Hamiltonian, its specific state and m,v are additional supplied model
data. No primitive or physical axiom is introduced.

Substantial prior art is explicit: Osborne and Stottmeister,
[Conformal Field Theory from Lattice Fermions](https://doi.org/10.1007/s00220-022-04521-8),
CMP 398 (2023), uses fermionic operator-algebraic renormalization,
wavelet maps and inductive limits. Its equation (91) already states the
abstract convergent-sequence criterion used here. The local CAR and
inductive-limit machinery is established mathematics, not a novelty
claim. This probe supplies the literal parity-sensitive spin maps, the
Haar-domain qualification, and reconciliation with this particular
massive state and actual mixed flows. Its proof is included rather than
importing unspecified wavelet regularity hypotheses.

## 2. A real dyadic isometry and its exact even-spin map

Set K_n=ell^2(Z;C^2), K_n,R=ell^2(Z;R^2), K=L^2(R;C^2),
K_R=L^2(R;R^2). Complex inner products are conjugate-linear in their
first entry. Majorana fields satisfy

    c_n(f)*=c_n(f), {c_n(f),c_n(g)}=2(f,g)_R 1,
    ||c_n(f)||=||f||,                           (D1)

for real vectors. Let jw_n be the finite-interval compatible isometric
map from even CAR(K_n,R) to A_n. In a finite interval starting at L,

    gamma_(j,1)=(product_(L<=k<j) Z_k) X_j,
    gamma_(j,2)=(product_(L<=k<j) Z_k) Y_j.        (D2)

The CAR hold, and these 2N Majoranas generate M_(2^N), since
Z_j=-i gamma_(j,1) gamma_(j,2), followed by recovery of X_j,Y_j.
Enlarging the left endpoint multiplies all old fields by the same
commuting exterior parity string. It cancels in an even product.
Thus these faithful finite identifications are compatible on the even
algebra and extend isometrically by norm completion. There is no
endpoint-independent odd bilateral spin identification in this proof.

Define the same real isometry at every scale by

    (R_n z)_(2j,r)=(R_n z)_(2j+1,r)=z_(j,r)/sqrt(2),
    r=1,2.                                      (D3)

Summing squares proves R_n*R_n=1. Its adjoint is
(R_n*w)_(j,r)=(w_(2j,r)+w_(2j+1,r))/sqrt(2). The CAR therefore give
a unital *-homomorphism c_n(z) -> c_(n+1)(R_n z). It is injective:
every finite real subspace can be enlarged to an even-dimensional one,
whose full Clifford algebra is a matrix algebra; the induced unital
map on that full matrix algebra is injective. Taking the dense union
and completing proves isometry before restricting to even elements.
Finite even Clifford algebras themselves need not be simple, and
simplicity of those algebras is not used.

Consequently

    rho_(n+1,n)=jw_(n+1) CAR(R_n) jw_n^-1          (D4)

is a unital injective isometric *-map A_n -> A_(n+1). For m>=n let
rho_(m,n) be its composition, with rho_(n,n)=id. If d=m-n, the
one-body composite is exactly

    (R_(m,n) z)_(2^d j+b,r)=2^(-d/2) z_(j,r),
    0<=b<2^d.                                   (D5)

Induction proves this formula including negative j and all d>=0.
It also proves rho_(l,m)rho_(m,n)=rho_(l,n).

For a finite coarse interval [L,R], all fine Majorana inputs lie in
[2L,2R+1]. Equation D2 shows their even products are ordinary spin
operators supported there. These children fill exactly the old physical
cell union [a_n L,a_n(R+1)); no physical interval enlargement occurs.

Here are explicit local generators. Write l=2j and omit tensor identities.
Direct multiplication of the literal Pauli matrices gives

    rho(Z_j)=(Z_l+Z_(l+1)-X_l X_(l+1)-Y_l Y_(l+1))/2, (D6)

    rho(X_j X_(j+1))=
      [X_l Z_(l+1) X_(l+2)
       +X_l Z_(l+1) Z_(l+2) X_(l+3)
       +X_(l+1) X_(l+2)
       +X_(l+1) Z_(l+2) X_(l+3)]/2.              (D7)

The onsite and nearest-neighbor even bilinears generate every local
even algebra: their Majorana edges form a connected path on the 2N
vertices, and commutators of adjacent bilinears generate every
bilinear, whose products span the even Clifford algebra. Thus D6-D7
plus D4 specify the full local map. The CAR proof, not separate guesses
for generators, guarantees all products and adjoints are respected.

An exact circuit decomposition clarifies a trap. Let sigma retain the
even-indexed fine fermion modes: gamma_(j,r) -> gamma_(2j,r). Let
O rotate each pair of site coordinates by pi/4, sending the even
Majorana to (gamma_(2j,r)+gamma_(2j+1,r))/sqrt(2) for both r.
The second column is the orthogonal difference with the sign needed
for a rotation. Its finite block action is implemented by an even
two-qubit unitary. Then rho=CAR(O) sigma on the even algebra.
However sigma(X_j X_(j+1))=X_(2j) Z_(2j+1) X_(2j+2), whereas
the ordinary tensor inclusion gives X_(2j) X_(2j+2).
Their difference has norm 2. Applying the same block unitaries preserves
that norm. Agreement on D6 cannot justify dropping the ancillary parity
strings between different coarse cells.

## 3. A UCP left inverse, derived without the pending section note

At one refinement split the real fine Hilbert space orthogonally into
the symmetric subspace R_n K_n,R and the antisymmetric subspace with
basis d_(j,r)=(e_(2j,r)-e_(2j+1,r))/sqrt(2). For a fixed orthonormal
basis of the latter, each individual sign flip d -> -d, fixing every
other basis vector, is a real orthogonal map and hence a CAR
automorphism. Average over all sign choices of the first N complement
basis vectors. Each average is unital completely positive, fixes the
symmetric CAR algebra pointwise and is bimodular over it.

On any polynomial in finitely many vectors from the combined basis,
the averages eventually kill precisely the monomials that contain a
nonempty set of complement basis fields, written in distinct-basis
normal form. These polynomials are norm dense. Contractivity therefore
gives a point-norm limit F_n. At every matrix level the same argument
preserves positivity, so F_n is UCP. Its range is the symmetric CAR
subalgebra, it is idempotent and bimodular, and it preserves the CAR
trace. This characterizes the trace-complement expectation; the
description is independent of the chosen complement basis.

For completeness, basis independence follows on finite exterior
Clifford monomials: the operation is orthogonal projection onto the
terms lying entirely in the retained subspace, with all complement
trace contractions performed. This finite operation is invariant
under complement orthogonal basis changes, and completion passes it
to the full algebra. Alternatively the trace-orthogonal projection
is uniquely specified on the dense polynomials. The CAR trace is
faithful, as its restriction to every finite full matrix algebra is
normalized matrix trace.

All sign-flip maps preserve total parity. Therefore F_n maps the even
algebra onto the retained even algebra. Inserting inverse CAR(R_n)
and the two JW maps gives a UCP contraction

    L_(n,n+1):A_(n+1)->A_n,
    L_(n,n+1) rho_(n+1,n)=id.                     (D8)

It is not claimed multiplicative on all fine elements. For distinct
complement unit vectors d_1,d_2, F_n(c(d_1)c(d_2))=0 but
F_n((c(d_1)c(d_2))^2)=-1. This is ordinary loss of complement data,
not a failure of D4's *-homomorphism.

## 4. The exact inductive limit and its interval algebras

Define the real cell isometry j_n and its adjoint C_n by

    (j_n z)(x)=a_n^(-1/2) z_j,  a_n j<=x<a_n(j+1),
    (C_n f)_j=a_n^(-1/2) int_[a_n j,a_n(j+1)] f(x) dx.
                                                    (D9)

C_n j_n=1, Q_n=j_n C_n is the cell projection and j_(n+1)R_n=j_n
exactly. Let H_n=j_n K_n,R. These spaces are nested. Their union is
dense in K_R: for f in H^1, Jensen and the fundamental theorem on
each cell give ||Q_n f-f||<=a_n||f'||; H^1 is dense in L^2 and all
Q_n are contractions. In particular Q_n ->1 strongly.

Put A=CAR(K_R)^even and

    Phi_n=CAR(j_n) jw_n^-1 : A_n -> A.
    Phi_m rho_(m,n)=Phi_n.                          (D10)

The images are nested isometric even subalgebras. They have dense
union: approximate the real inputs of each even field polynomial by
H_n vectors and use D1 and finite-product telescoping; parity averaging
shows that such polynomials are dense in A. Hence the C*-inductive
limit of (A_n,rho) is isometrically *-isomorphic to A, with its stated
canonical injections Phi_n. This assertion has both density and
injectivity, not merely a map from an abstract limit onto a subalgebra.

For a bounded open interval I let Lambda_n(I) consist of cells wholly
inside I, ignoring measure-zero endpoints. This is a finite interval
of sites, possibly empty, with the empty local algebra equal to C1.
Children of retained cells remain in Lambda_(n+1)(I), so D4 defines a
local inductive system. The corresponding H_n(I) are nested and
their union is dense in L^2(I;R^2): compact smooth functions in I
are approximated by cell projections for all sufficiently large n.
Repeating the previous argument gives

    lim_ind A_n(Lambda_n(I)) = CAR(L^2(I;R^2))^even. (D11)

Isotony follows from inclusion of intervals. This is an exhaustion
theorem for this specified dyadic even system and its inner-cell local
system. It is not an identification of every independently defined
spin scaling algebra or every bounded microscopic sequence.

## 5. Intrinsic Cauchy sections and the quotient

Let product_b A_n be bounded sequences x=(x_n), with the supremum norm.
Define Gamma_rho by the intrinsic condition

    lim_(N->infinity) sup_(m>=n>=N)
        ||x_m-rho_(m,n)x_n||=0.                     (D12)

Equivalently one can use the established double-limit form

    lim_(n->infinity) limsup_(m->infinity)
        ||x_m-rho_(m,n)x_n||=0.                     (D13)

To verify equivalence, D10 and isometry turn both expressions into
the ordinary corresponding conditions on y_n=Phi_n x_n in A. D12 is
the Cauchy criterion. If D13 holds, choose n_0 with limsup_m
||y_m-y_(n_0)||<epsilon/3; then both y_m and y_k lie within
epsilon/2 of y_(n_0) for all sufficiently large m,k, proving Cauchy.
The converse follows immediately. This also covers n=m and finite
initial exceptions. Boundedness is explicit in the section algebra;
the Cauchy property itself bounds the tail.

Gamma_rho is a unital C*-subalgebra: sums and adjoints preserve the
criterion; multiplication follows from

    ||x_m z_m-rho(x_n z_n)||
      <=||x_m|| ||z_m-rho z_n||
         +||x_m-rho x_n|| ||z_n||.

Uniform limits preserve D12 by the triangle inequality and the norm-one
maps rho. Therefore completeness and the C*-identity are inherited
from product_b A_n. Let Gamma_0={x:||x_n||->0}. It is an ideal in
Gamma_rho. The map

    ev_infinity(x)=lim_n Phi_n x_n                  (D14)

is a contractive *-homomorphism with kernel exactly Gamma_0.
It is onto: for any a in A, density of the nested images permits
y_n in Phi_n A_n with ||y_n-a||->0. For example approximate a first
by y^(k) in Phi_(N_k) A_(N_k), use that same element at every
N_k<=n<N_(k+1), and let k increase. Invert Phi_n to obtain x_n.
The sequence is bounded and obeys D12. Thus

    Gamma_rho/Gamma_0 is isometrically *-isomorphic to A,
    ||ev_infinity(x)||=lim_n||x_n||.                (D15)

The quotient norm equals the last limit: truncating finitely many
coordinates gives the upper bound limsup||x_n||, and adding any
c0 sequence leaves that limsup unchanged. This supplies a direct
norm check as well as the C*-isomorphism theorem.

The same proof for the local inner-cell system in D11 identifies its
Cauchy-section quotient with CAR(L^2(I;R^2))^even. No choice of the
pending UCP-section note is used in this intrinsic characterization.

There is also a constructive global lift of every limit element.
Repeat section 3 for K_R=H_n oplus H_n^perp to obtain E_n:A->Phi_n A_n.
The retained projection on one-body fields is Q_n. On every finite
field word, E_n(a)->a: approximate that word by fields in H_N; for
n>=N the approximation is fixed by E_n, giving error at most twice
the approximation error. Density gives point-norm convergence on A.
Then J_n=Phi_n^-1 E_n is UCP and (J_n a)_n is a Cauchy section with
limit a. This is a separately derived trace-complement lift. It has
not been identified with any formula or locality claim in the pending
section note.

## 6. Exact dynamical and state hypotheses from the chosen chain

The additional model data are

    sigma_a=sqrt(m^2/4+v^2/a^2),
    g_a=sigma_a/2+m/4, J_a=sigma_a/2-m/4,
    h_(a,j)=-J_a X_j X_(j+1)-(g_a/2)(Z_j+Z_(j+1)),
    omega_a=omega_0 o beta_a.                       (D16)

Here omega_0 is the all-Z-up product state and beta_a is the actual
spin automorphism constructed in the concrete parent. The even
restriction is quasifree with

    omega_a(c_a(f)c_a(g))=2<f,P_(a,+)g>,
    P_(a,+)=(1+sign D_a)/2,                         (D17)

where

    (D_a z)_(j,1)=2i(g_a z_(j,2)-J_a z_(j-1,2)),
    (D_a z)_(j,2)=-2i(g_a z_(j,1)-J_a z_(j+1,1)),
    D=i v sigma_x partial_x-m sigma_y,
    P_+=(1+sign D)/2.                               (D18)

The covariance sign follows from the chosen spin state, not a newly
selected continuum vacuum. At J=0, -gZ has Z=+1 ground state and
omega(XY)=i; D17 gives exactly i. The concrete beta_a rotates
the reference polarization by its real parallel band frame, giving
D17 on all real ell^2 inputs by norm continuity.

The local-even parent proves

    S_n=j_n P_(a_n,+) C_n -> P_+ strongly on K.       (D19)

It has the smooth-input estimate
||(S_n-P_+)f||<=a_n[||f'||+(m||f'||+v||f''||)/(4m)]
for f in H^2, then contraction/density gives D19 for all L^2.
S_n+Gamma S_n Gamma=Q_n, not 1 on K. We do not treat S_n alone
as a polarization of the entire common CAR algebra.

For the actual even spin actions, the pinned mixed theorem supplies:

    time:       V_n(t)=exp(+it D_(a_n)),
    space:      T_n(ell)z_j=z_(j-floor(ell/a_n)),
    boost:      Z_n(s)=exp(-is B_(a_n)),
    B_a={X_a,D_a}/2-aD_a/2,  (X_a z)_j=aj z_j.      (D20)

The boost is the actual spin action lambda^b_(-a_n s), equivalently
conjugation in its full spin-GNS representation by exp(-is a_n B_spin,a_n).
The closed lattice domain is the Fourier periodic H^1 domain, or
sum_j(1+j^2)||z_j||^2<infinity. The continuum boost is the closed
self-adjoint realization

    B=i v sigma_x(x partial_x+1/2)-mx sigma_y.        (D21)

Its domain is transported from the two scalar bands with
b=i(E partial_q+E'/2), E=sqrt(m^2+v^2q^2), and
Dom b={psi locally AC:psi, E psi'+E' psi/2 in L^2};
the full domain is J* (Dom b oplus Dom b). Compact smooth Cauchy
data are a core. These are imported closed-domain results, not domains
defined by the formal anticommutator alone.

Let w be any fixed finite word of the factor types in D20, including
the empty word, with parameters continuous in a compact parameter
space P. Write W_n(w,p) for its lattice one-body word and W(w,p)
for the corresponding real continuum unitary word. The parents give

    sup_(p in P)||j_n W_n(w,p) C_n f-W(w,p)f|| ->0
    for every f in K.                              (D22)

The continuum factors are exp(+itD), T(ell)f(x)=f(x-ell), and
exp(-isB). Their strong continuity makes continuum word orbits compact.
For completeness the composition step uses C_n j_n=1, so products
of embedded factors have no extra cell projections. Telescope a word
against its continuum word. Each suffix orbit is compact; convergence
on it follows from a finite epsilon-net and the common norm bound.
The elementary comparison is first proved on compact smooth inputs
and extended by density with uniform contraction error. This proves
D22 without applying a smooth estimate to a step function.

All W_n and W are real: their generators anticommute with position
conjugation and the group signs include conjugation of i. On even CAR,
the actual spin word alpha_n(w,p) sends each even product of fields
to the product with coefficients W_n(w,p)f. The continuum action
alpha(w,p) is the corresponding CAR automorphism. No rounded real
translation group law or finite-scale Lorentz relation is assumed.

## 7. Every Cauchy section has the actual state and mixed-flow limit

**Theorem.** Under D16-D22, for x in Gamma_rho with a=ev_infinity(x),
each fixed mixed word obeys

    sup_(p in P)||Phi_n alpha_n(w,p)x_n-alpha(w,p)a|| ->0. (D23)

Thus for each fixed p the transformed sequence is again in Gamma_rho.
Moreover, for any fixed finite collection x^1,...,x^r in Gamma_rho,
with limits a_1,...,a_r and words w_1,...,w_r,

    sup_(p in P) |omega_(a_n)(product_(k=1)^r
                  alpha_n(w_k,p)x_n^k)
             -omega(product_(k=1)^r alpha(w_k,p)a_k)| ->0. (D24)

Here omega is the even restriction of the real-CAR quasifree vacuum
with two-point form 2<f,P_+g>. The order of the product is kept.
In particular omega_(a_n)(x_n)->omega(a). The result is on all
intrinsically Cauchy sections, not just one preassigned smearing family.

**Proof of D23.** Extend the lattice word to a real unitary on K by

    W_hat_n(w,p)=j_n W_n(w,p) C_n+(1-Q_n).           (D25)

The two summands act on the orthogonal reducing subspaces H_n and
H_n^perp, so this really is unitary; it is not the nonunitary compression
alone. D22 and strong Q_n->1 imply W_hat_n->W strongly, uniformly
on P at each fixed vector. CAR field norm continuity and finite-product
telescoping then show CAR(W_hat_n)(b)->CAR(W)(b) uniformly on P
for every fixed b in A. Polynomial approximation extends this from
finite words because the automorphisms are isometries. Since

    Phi_n alpha_n(w,p)x_n=CAR(W_hat_n(w,p))(Phi_n x_n),

its difference from alpha(w,p)a is at most
||Phi_n x_n-a||+||CAR(W_hat_n(w,p))a-alpha(w,p)a||.
This proves D23. It also proves that the empty word causes no defect:
D25 is exactly the identity in that case.

**Proof of state convergence.** Fix b in Phi_N A_N. Approximate it in
norm by an even polynomial with real vectors in H_N. For n>=N these
vectors are exactly represented at scale n by D5/D10, and its actual
two-point entries are 2<f,S_n g>. D19 makes each entry converge to
2<f,P_+g>. Its ordered moment is the Pfaffian with entries
W_ij=2<f_i,P_+f_j> for i<j, W_ji=-W_ij, W_ii=0.
Even overlapping fields use this upper-triangle convention; the raw
two-point form is not antisymmetric. Each finite Pfaffian is a
polynomial in those entries. Thus

    omega_(a_n)(Phi_n^-1 b)->omega(b), n>=N.        (D26)

The polynomial approximation passes this to all b in Phi_N A_N
because states have norm one. For a general Cauchy section choose
b in the nested union with ||b-a||<epsilon. For n sufficiently large
and containing b, bound the discrepancy by

    ||Phi_n x_n-a||+2||a-b||
       +|omega_(a_n)(Phi_n^-1 b)-omega(b)|.

Then n->infinity and epsilon->0 give the stated actual-state limit.
No finite-scale state consistency or new extension state is needed.

**Uniform products.** By D23, the embedded product in D24 converges
uniformly to b(p)=product_k alpha(w_k,p)a_k, since all factor norms
are bounded independently of n,p. The map p->b(p) is norm continuous,
by strong one-body continuity, field continuity and polynomial
approximation; therefore b(P) is norm compact. Approximate it by a
finite epsilon-net from the nested union. All its points belong to
one Phi_N A_N. Apply D26 at those finitely many points and the norm-one
state bounds exactly as above. This proves D24 uniformly on P.

The limiting maps depend only on the continuum group element. In the
parent convention time t has coordinate translation tau=-t and boost
s has rapidity eta=vs. Hence words representing the same continuum
Poincare element induce the same action on Gamma_rho/Gamma_0, even
when they differ at every finite scale. For local sections with limit
in D11, the pinned time-slice and covariance theorem places the limit
in A(g D(I)). This is a statement about the specified continuum net;
it does not say finite-scale boosted support stays in a fixed set.

Haar inputs matter here. A nonzero fixed cell indicator has a jump
and is not in H^1, hence not in H^2 or generally in the continuum
generator domains. Its repeated-refinement section still satisfies
D23-D24 by the strong L^2 extension. No O(a_n) rate, differentiated
flow convergence, or generator-graph limit on such a section follows
from the smooth-input parent estimates. The proof does not require
any such assertion.

## 8. Two concrete failures of stronger finite-scale equations

These falsify the two stated equations for this fixed R and chosen
family. They do not exclude other renormalizations, states or dynamics.

**Chosen-state compatibility.** Put r_a=J_a/g_a in (0,1) and

    h_r(k)=(1-r cos k)/sqrt(1-2r cos k+r^2),
    mean F=(2pi)^-1 int_(-pi)^pi F(k) dk.

The actual polarization D17-D18 gives

    omega_a(Z_0)=mean h_(r_a),
    omega_(a/2)(rho Z_0)=mean (1+cos k) h_(r_(a/2)). (D27)

The second factor is |1+exp(-ik)|^2/2, from the two child amplitudes;
no Gaussian state on a finite open chain substitutes for this
infinite-chain covariance. The sine part integrates to zero.
Since sigma_a increases as a decreases, r_(a/2)>r_a>0.
Direct differentiation gives

    partial_r h_r(k)=-r sin^2 k/(1-2r cos k+r^2)^(3/2).

It is strictly negative almost everywhere. Also mean(cos k h_r(k))<0.
To prove the latter, pair c=cos k>0 with -c. Both h values are
positive, and

    h_r(c)^2=1-r^2(1-c^2)/(1-2rc+r^2)
              <1-r^2(1-c^2)/(1+2rc+r^2)=h_r(-c)^2

for 0<c<1. Multiplying the negative difference by c and integrating
with the symmetric cosine distribution proves the strict sign.
The weight 1+cos k is nonnegative and positive almost everywhere.
Consequently, for every a,m,v>0,

    omega_(a/2)(rho Z_0)
       < mean(1+cos k)h_(r_a)
       < omega_a(Z_0).                              (D28)

This is an exact scalar counterexample to omega_(a/2) rho=omega_a,
without any quadrature premise. The numeric control merely tests
these expressions for explicit parameters by two arithmetic routes.
It is compatible with D26: a fixed coarse element is tested in finer
and finer actual states until it converges, not assigned its original
coarse expectation forever. At v=0, outside the strict family,
r_a=0 and both expectations are 1; that degenerate survivor is explicit.

**Energy-flow compatibility.** Let delta_a(A)=i[H_a,A] on local
observables, with H_a's formal unweighted finite-range sum. The
finite commutator is well defined. Direct Pauli multiplication gives

    delta_a(Z_j)=-2J_a(X_(j-1)Y_j+Y_jX_(j+1)).       (D29)

Take j=1, so rho Z_1 is supported on fine sites 2,3. Then
delta_(a/2)(rho Z_1) is supported within sites 1 through 4.
In contrast rho(delta_a Z_1) has coefficient -J_a on the Pauli
word Y_3 Z_4 X_5. Indeed Y_1X_2=i gamma_(1,1)gamma_(2,1), and
its refined (3,5) term is Y_3 Z_4 X_5/2. The left coarse bond
does not contribute to that word. Therefore

    coefficient_(Y_3 Z_4 X_5)
       [delta_(a/2)(rho Z_1)-rho(delta_a Z_1)]=J_a>0. (D30)

The flows cannot intertwine for all t: both sides are differentiable
on this local input, and D30 contradicts equality of their derivatives
at zero. This test can be performed literally on three coarse and
six fine sites; no boundary term reaches the witness unexpectedly.
The same effect appears at one-body level: for z=e_(0,2),
(D_(a/2)Rz-RD_a z)_(3,1)=sqrt(2)i J_a. No unbounded operator
comparison or odd-spin identification is used to infer D30.

## 9. Scope stress test and remaining obligations

The strongest positive result is the complete specified dyadic system,
its local inductive limit, intrinsic sections and actual limits D23-D24.
The exact algebraic part uses real Hilbert/Clifford machinery only.
The dynamics and state retain the supplied chain and the pinned
closed-domain, covariance and actual-spin-implementation dependencies.
Fresh independent checking of the new proof is still required before
substantial downstream reuse. No full physical theory, framework-selected
Hamiltonian/state, odd spin limit or empirical prediction is established.

The negative statements are the explicit equation failures D28 and D30.
They are not a claim that all state-compatible refinements are impossible.
The No-Go Discipline skill is used to check that scope; this packet does
not claim a five-route exhaustive no-go or a mechanical no-go PASS.

* N1: the genuine routes examined are CAR isometric inclusion (survives),
  ordinary tensor insertion plus local block rotations (fails across
  blocks), exact chosen-polarization consistency (D28 fails), exact
  Hamiltonian intertwining (D30 fails), and asymptotic pullbacks along
  the nested system (D23-D26 survive). They are different mathematical
  questions, not five attacks exhausting every possible state-compatible
  refinement. The five-family no-go submission requirement is therefore
  not certified; this is a positive conditional probe with specified
  counterexamples, and any broader no-go packaging is held.
* N2: D28 and D30 are separate counterexamples to separate equations.
  Neither is presented as implying the other; their general logical
  independence is not proved. The algebra theorem has no dependency
  on the dynamical parents; the mixed theorem does. No wall count is used.
* N3: the model, chosen state, dyadic cells, real CAR, parent group
  domains, parity restriction and fixed compact parameter sets are
  explicit. The word "canonical" describes D10's injections only;
  it does not supply a physical choice. A final source scan is retained.
* N4: no historical no-go is a witness for D28 or D30. They use the
  displayed actual covariance and literal local commutator, respectively.
* N5: D28 is an onsite even-element witness; D30 spans three coarse
  cells. The equations therefore fail as algebra-wide identities.
  There is no claim that every element, mode or block fails. Constants
  and the algebraic CAR relations survive. Per-mode universal failure
  is not asserted or tested.
* N6: a trace-compatible reference state, the pullback of a chosen
  continuum state, or modified fine dynamics would change the question
  and can remove these particular compatibility demands. Such a change
  is not required for the proved actual asymptotic limits. No new
  physical axiom is needed or requested.
* N7: the strongest challenge is to replace Haar R by a filter adapted
  to the energy polarization and prove locality plus exact state or
  flow compatibility. That terminal obligation is unattempted here.
  It is outside the fixed-R equation falsified by D28/D30. The surviving
  asymptotic result already avoids demanding either exact identity.
* N8: the parent mixed theorem likewise retains finite-spacing
  Poincare and rounding defects while proving convergence. That
  mechanism applies here and is used in section 7. General OAR prior
  art likewise motivates renormalized limits, not raw cylindrical
  consistency. No historical closed-route label is imported.

## 10. Pre-execution controls and evidence boundary

This full analytic proposal, formulas and control expectations are
frozen before scientific execution in E/frozen. Controls will include
literal Pauli computations across two and three coarse cells, exact
CAR and two-step composition, left-inverse action, an ancillary-string
counterexample, actual-state quadratures and the literal D30 coefficient.
They will retain every failed predicate and every surviving mutation.

Exact arithmetic identities and floating state integrals are separately
labelled. Floating quadrature is a diagnostic, not proof of D28 or of
any infinite-dimensional convergence. Parent strong limits supply D19
and D22; this bounded probe does not repeat their whole-flow numerics.
Every scientific subprocess has a true timeout, complete INNER streams
and receipt, and an OUTER recorder before interpretation. Source and
helper bytes are sealed before the first scientific run. Subsequent
source changes, if any, will be explicit additions or preserved diffs.

No editable prompt file, platform instruction, axiom, audit file,
Git state or publication surface is modified by this worker.

## 11. Post-freeze root alternative, before scientific execution

After the analytic freeze, root suggested checking the exact state-adapted
map rather than leaving N7 as only a future filter proposal. This is
coauthor exposure, not an independent discovery or review certificate.
The conventions in the concrete parent do support the following
algebraic observation on the even algebras:

    rho^omega_(m,n)=beta_(a_m)^-1 rho_(m,n) beta_(a_n). (D31)

The all-up reference state's Majorana polarization is the constant
onsite C_0=-sigma_y. D3 acts on site coordinates identically in both
real components and hence intertwines C_0 exactly. Reference two-point
forms, then all ordered quasifree moments and norm density, give
omega_0 rho_(m,n)=omega_0. Since omega_a=omega_0 beta_a,

    omega_(a_m) rho^omega_(m,n)=omega_(a_n).          (D32)

The conjugations also telescope, so D31 is an injective inductive
system algebraically isomorphic to the original one. This observation
does not prove that D31 preserves finite interval support: the beta_a
are exponentially local quasilocal spin automorphisms, with extended
interaction strings, rather than the finite support map D3. Nor does
D32 prove actual energy-flow intertwining. These are separate
obligations. No uniform physical localization estimate for beta_a is
assumed here. D31-D32 are a concrete out-of-fixed-map escape and make
a general no-go interpretation of D28 especially inappropriate.

The only pre-execution wording correction to the frozen argument is
the source-read coverage sentence in section 1. Its exact diff and
this appended proposal are preserved in E/POSTFREEZE_PREEXEC.diff.
The original frozen proof and original protocol remain intact.

## 12. Actual controls, failures and final author handoff

The initial analytic freeze occurred at 2026-10-12T12:49:40.806575Z,
with SHA-256
7cd24efde9dea9c96d0529c6cdde8fa8f731191653771c24abf8f7ca12ec078e.
The original control protocol hash is
5511609d1961b7c2f4a463a2112a0343ba974e4e1065a028bce94f3657fc97fc.
Section 11 and the section 1 coverage correction were already present
when the execution manifest was sealed at 12:56:25.965503Z. Its note
hash is 983c435bbe33f954136cc5d506582f80fa38f9d722766ad854b2aafe49d4630d;
those exact executed argument bytes are now E/frozen/EXECUTED_ARGUMENT.md.
Thus the post-freeze alternative preceded every mathematical process,
including the invalid-provenance attempts described next. This section
reports later observations without rewriting the original argument.

The first two mathematical attempts started at 12:56:52.359895Z and
are **invalid as evidence records**. The invocation used record names
ending in `.inner` and `.outer`, while the recorder used Path.with_suffix;
the stream/receipt names collided. The six resulting files, hashes and
reason are preserved in E/INVALID_INITIAL_RECORDING.json. They are real
scientific attempts, not erased or relabeled as setup. Their mathematical
rows were not inspected or used for claims after the collision was found.
No missing stream or receipt was reconstructed.

The unchanged scientific scripts, candidate, fixtures and tolerances were
rerun using disjoint suffix-free `_inner` and `_outer` names. Valid
baseline OUTER runs started at 12:57:41.6998Z, and INNER jobs at
12:57:41.7713Z. All five valid scientific jobs have actual process-group
timeouts of 60 seconds at INNER and 70 seconds at OUTER, the extra ten
seconds allowing recorder overhead as clarified before any run in
E/PREEXEC_ADDENDUM.md. Every valid full stdout/stderr hash, before/after
source identity, return code and receipt was checked before interpreting
its rows. No valid job timed out; all stderr streams are empty. The
longest valid INNER job took 3.411 seconds.

| Author control | Observed result | Limit |
|---|---|---|
| Exact rational/complex Pauli algebra and literal Kronecker matrices | 168 predicates hold; D6-D7, all 64 two-coarse-site even basis multiplication pairs, rank-8 trace Gram matrix, two-step refinement to eight fine sites and complement expectation agree exactly | Finite algebra controls; the complete infinite construction is the proof |
| Ancillary parity | Ordinary tensor insertion differs from fermionic insertion by exact norm 2, including after the same correct block rotations | Onsite and parity checks alone survive and do not certify the cross-block map |
| Actual local Hamiltonian | Literal three-coarse/six-fine Pauli matrices give exactly coefficient +J_c in D30 | Local witness, not a numerical infinite-Hamiltonian construction |
| Actual infinite-state covariance | 38 predicates hold at a=2,1,.5,.25 for m=v=1; direct child covariance, literal D6 covariance and independent real quadrature agree within 4.47e-16 | Floating diagnostics; strict universal inequality is proved analytically in D28 |

For example, at m=v=a=1 the actual coarse Z expectation is
0.9624617081178061 and the actual refined expectation is
0.8678087500306405. The intermediate value in D28 is
0.955222601583984. At v=0, outside the strict assumptions, the
equality value 1 survives as planned. Two Brillouin grids and the
independent adaptive quadrature use the unchanged 2e-10 comparison
threshold; neither observed grid agreement nor the adaptive error
estimate is an interval-certified proof of an integral.

All three material source variants were run against their preregistered
targeted controls. The full rows, values and source diffs are retained.

| Source variation | Failed / executed predicates | Surviving checks |
|---|---:|---|
| Omit 1/sqrt(2) normalization | 20/47 | Off-diagonal CAR anticommutators, support and parity |
| Omit ancillary parity in the mode insertion | 1/6 | Block unitarity, onsite formula, onsite agreement and parity |
| Omit the child form factor 1+cos k | 14/38 | Positivity, grid convergence, the v=0 edge and most loose strict-margin fixtures |

In total the valid baselines contain 206 successful predicates, and
the 91 mutant predicates contain 35 failures and 56 survivors. Counts
inventory evidence; they do not prove the infinite theorem or supply
independent review. The positivity and grid tests surviving the missing
form factor are particularly relevant: internally stable state numbers
do not establish the intended refined observable.

E/row_inventory.json binds all 297 valid rows to their raw stream lines;
E/result_disposition.json records every failure and survivor, including
changed surviving rows. E/verified_execution_receipts.json and
E/summary.json give the checked execution inventory. The frozen source
is bound by execution-manifest hash
dfe56a005e018555d7d93b522d195042b94c74ff8aff67f53783d1cf7276a35f.
The final source merely appends this evidence account to the executed
argument. Reproduction uses the immutable executed argument via the
separately identified reproduction manifest; the historical manifest
and receipts remain untouched.

The runtime is Python 3.13.5, SymPy 1.14.0, NumPy 2.4.4 and SciPy 1.17.1.
All scientific processes limit BLAS/OMP threads to one. Exact symbolic
arithmetic, literal matrix arithmetic and the two numerical integration
routes are different calculations within this author context. They are
not separate-context independent reviews. No new whole-flow simulation
was run: D19/D22 remain explicit pinned parent inputs, and section 7 is
the new analytic extension from strong vector convergence to arbitrary
intrinsically Cauchy sections and compact-parameter joint moments.

The review targets are the trace-complement expectation, intrinsic
quotient identification, uniform compact-family state extension, and
the precise physical scope of the state-adapted alternative. Formal
retained status is unset; no Lean evidence is claimed. Root owns fresh
review, source integration and publication. No editable prompt changed.


## Publication evidence and review record

**Author/checker pairing:** Same selected model family and reasoning effort; separate formula-exposed reviewer context, not blinded or diverse-family. Root coauthored the state-adapted conjugacy addendum. Mechanical packaging and reproduction add no independent science review.

Only the supplied even algebra and chosen model data are covered. Fixed Haar maps have explicit state and energy-flow counterexamples. Elementary state-adapted conjugacy is proved, while its finite interval locality and actual dynamics remain open. No H2 rate is applied to Haar indicators; no state-selection, interacting or higher-dimensional theorem is asserted.

The accepted independent analytic review, exact and exterior-algebra controls, original author helpers, all raw output, and root verification are preserved through the [complete evidence map](../.claude/science/physics-loops/toe-dyadic-refinement-20261012/EVIDENCE_MAP.json). The original valid author jobs contain 206 passing baseline predicates and 91 mutant predicates (35 rejecting, 56 surviving). Two initial recorder filename collisions are preserved but are invalid provenance and excluded from those counts. The unchanged replacements and all failed and surviving subrows remain. The local-support predicate checks word length only; the trace predicate checks already-fixed images only. The analytic proof carries the corresponding general support and trace conclusions.

Direct proof inputs are [Concrete Gapped Chain](CONCRETE_GAPPED_CHAIN_BOUNDED_THEOREM_NOTE_2026-10-12.md), [Local Even Continuum](LOCAL_EVEN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-10-12.md), [Continuum Local Boost](CONTINUUM_LOCAL_BOOST_BOUNDED_THEOREM_NOTE_2026-10-12.md), [Microscopic Local Boost Limit](MICROSCOPIC_LOCAL_BOOST_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-12.md), [Mixed Local Poincare Correlations](MIXED_LOCAL_POINCARE_CORRELATIONS_BOUNDED_THEOREM_NOTE_2026-10-12.md). The local-even-net-sections result is adjacent context only and supplies no theorem premise. The new state-adapted followup is separate and is not an input.

The existing source N1–N8 discussion scopes fixed-map witnesses; it is not an exhaustive no-go or a claimed N-gate PASS. Section 11 proves elementary state-adapted conjugacy only. No new mathematical correction, control design, or Lean certificate is introduced by packaging. The [execution contract](../.claude/science/physics-loops/toe-dyadic-refinement-20261012/EXECUTION_CONTRACT.md) separates source preparation from root execution; original histories remain immutable. Global combined validation, strict audit lint, and independent audit ratification remain landing obligations. No audit verdict or retained promotion is applied.
