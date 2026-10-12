---
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: Fixed finite words of actual time, rounded spatial translation and scaled boost actions have compact-parameter norm limits on constructed even spin polynomials, and the chosen-state ordered joint moments converge with the stated fixed-data estimates.
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_id: mixed_local_poincare_correlations_bounded_theorem_note_2026-10-12
claim_type: bounded_theorem
claim_scope: Fixed finite words of actual time, rounded spatial translation and scaled boost actions have compact-parameter norm limits on constructed even spin polynomials, and the chosen-state ordered joint moments converge with the stated fixed-data estimates.
upstream_dependencies:
- concrete_gapped_chain_bounded_theorem_note_2026-10-12
- local_even_continuum_bounded_theorem_note_2026-10-12
- microscopic_local_boost_limit_bounded_theorem_note_2026-10-12
- continuum_local_boost_bounded_theorem_note_2026-10-12
runner: scripts/mixed_local_poincare_correlations_2026_10_12.py
artifact_role: theorem
claim_type_reason: Conditional supplied-model theorem with complete analytic argument and finite controls; source review does not confer retained status.
target_claim_id: null
target_blocker_text: 'handles

  fixed mixed words and their ordered correlations'
source_of_blocker_text: handoff
next_trace_action: Use the fixed-word norm and state estimates to extend the explicitly constructed comparison sections by density; do not assume arbitrary scaling-family control.
---

**Publication status:** The five exact source notes have completed separate-context source review and root integration for conditional composition. Original pending-review statements below describe the historical freeze and are superseded by this record. Mathematical arguments, failures and their original source identities are preserved. This is not an audit verdict or retained status.


# Mixed local Poincare words and chosen-state spin correlations

**Author candidate, 2026-10-12.** For the supplied massive free spin-chain
family, each fixed finite word of actual time, integer translation and
scaled boost actions has a compact-parameter continuum limit on constructed
even spin polynomials. The comparison is in norm under explicitly specified
spacing-dependent CAR embeddings. Chosen-state joint moments converge by
their ordered Pfaffians. All these comparisons are O(a) for fixed compact
smooth input data, with constants written below. Continuum Poincare
relations therefore give vanishing defects on those observables, while
the microscopic relations need not hold at any nonzero spacing.

The actual microscopic boost theorem remains a provisional dependency.
The argument is conditional on that exact theorem and the other pinned
supplied-model premises, not an independent re-proof of their existence
results. No full spin scaling net, uniform operator-unit-ball limit, odd
spin-field limit, interacting theory, higher-dimensional realization,
empirical prediction or framework selection is asserted.

## 1. Exact premises and status

S is this note's directory; E is `mixed_local_poincare_correlations/`.
The complete root route was read as a proposal, not as evidence. Its SHA is
`027269df4b50ca3e35db7a19d005c4a5114d18a30f24abb7f77421a618e1a255`.

| Source | SHA-256 | Imported scope |
|---|---|---|
| `LOCAL_EVEN_CONTINUUM_PROBE.md` | `7be1a72e2b59c5c61b68ead6d663e8d4e179b21e2497243a2859a4082ea7813b` | Actual chosen covariance, even spin/CAR isomorphism, isometric cell embedding, time and projector estimates; independently reviewed and root-accepted |
| `MICROSCOPIC_LOCAL_BOOST_LIMIT_PROBE.md` | `70118e0b1f7fd4fa9d041ce837f967abdd0e2f682a854d38885466fd6e4b125d` | Actual GNS boost identity, closed lattice generator and quantitative cell comparison; **fresh independent review still open** |
| `CONTINUUM_LOCAL_BOOST_REVISED_PROBE.md` | `59d34a51720446a554c41ec070c0b52b6dde67692c72b4c42a4937f7f4ca9d16` | Real Cauchy Poincare representation, compact smooth orbits, vacuum and specified local net; revised smooth-gauge statement independently reviewed and root-accepted |
| `CONCRETE_GAPPED_CHAIN_PROBE.md` | `0aebc2ded245d9bc9ecae364db0d1a042f9642771ed788794dafd73fb7f621bd` | Supplied symmetric spin density and actual full-GNS state/flows underlying the preceding bridges |

The revised continuum source's complete diff and review were read. The
review SHA is `3abe5da0ba5e4917b8a22275a37efa2318a5a59e4d5798a940b86ec86966c644`;
root coverage is `dd76e7dc61c6179b2c729a1d3b181c8acd7c58ba567c346f7bce11421076687c`.
Its correction restricts differential gauge formulas to smooth phases;
the chosen parallel frame used here is unchanged. No rough-gauge
differential identity is needed. Root's complete microscopic author read,
SHA `2cf21a009d975cf3c217d9be614ea217ce6d856c61f0858de9740fcd3a2effb9`,
does not replace that theorem's pending independent review.

The fixed main/planning/worktree source identities and reused instruction
hashes are inventoried in E. The selected model/effort remains unchanged,
no subdelegation occurs, and root owns publication, Git and audit decisions.
Every scientific diagnostic follows a frozen complete proof and protocol.

## 2. Actual elementary actions and one common Hilbert space

Fix m,v>0 and 0<a≤a_0, with `2(g_a-J_a)=m`, `4g_aJ_a=v²/a²`,
g_a>J_a>0. The supplied density is
`h_n=-J_a X_nX_(n+1)-(g_a/2)(Z_n+Z_(n+1))` and the chosen state is
`omega_a=omega_0 o beta_a`, as constructed in the concrete parent.
Set K=L²(R;C²), K_a=ell²(Z;C²), with real parts K_R,K_a,R.
Inner products are conjugate-linear in the first entry. Position
conjugation is denoted Gamma; Fourier conjugation includes q reflection.

The actual coefficient generators are

    (D_a z)_(1,n)=2i(g_a z_(2,n)-J_a z_(2,n-1)),
    (D_a z)_(2,n)=-2i(g_a z_(1,n)-J_a z_(1,n+1)),
    B_a={X_a,D_a}/2-aD_a/2,  X_a z_n=an z_n.          (Q1)

D_a is bounded self-adjoint at fixed a. B_a has the self-adjoint closure
and periodic Fourier H¹ domain proved in the microscopic parent; finite
position sequences are a core. Its actual full-spin implementer is
`exp(-is a B_spin,a)` and acts on even coefficient words by exp(-isB_a).
The corresponding spin automorphism is `lambda^b_(-as)`.

The continuum generators are
`D=i v sigma_x partial_x-m sigma_y` and
`B=i v sigma_x(x partial_x+1/2)-mx sigma_y`, with the full domains and
compact smooth core supplied by the parents. Define elementary factors

    time:        V_a(t)=exp(+itD_a), V(t)=exp(+itD);
    boost:       Z_a(s)=exp(-isB_a), Z(s)=exp(-isB)=V_cont,(vs);
    translation: T_a(ell)z_n=z_(n-N_a(ell)),
                 T(ell)f(x)=f(x-ell),
    N_a(ell)=floor(ell/a),  |aN_a(ell)-ell|≤a.        (Q2)

The underlying spin translations send site n to n+N_a(ell). The even-JW
identification intertwines them with T_a: the exterior parity strings
cancel for every even finite product, and norm completion gives equality
on the even algebra. This does not identify odd bilateral spin fields.
Any other predetermined integer rounding satisfying the displayed bound
has the same theorem; the diagnostics use the specified floor convention.

Floor rounding is not a real-translation group homomorphism. In particular
`N_a(ell)+N_a(-ell)=-1` away from integer multiples of a, so the two
rounded factors can compose to a one-cell shift. No finite-a continuity
in ell or exact real-translation group law is asserted. Time and boost
are the actual point-norm continuous spin flows at each fixed a.

Define the physical cell maps

    (C_a f)_n=a^(-1/2) int_[an,a(n+1)] f(x)dx,
    (j_a z)(x)=a^(-1/2)z_n on [an,a(n+1)),
    C_a j_a=1, Q_a=j_a C_a, ||j_a z||=||z||,
    ||(Q_a-1)f||≤a||f'||.                            (Q3)

These are real contractions/isometries, Q_a is an orthogonal projection,
and Q_a→1 strongly. For any lattice unitary Y_a write
`A_a(Y_a)=j_a Y_a C_a`. All these operators on K are contractions, and
for r≥1 their product is exactly

    A_a(Y_(a,1)) ... A_a(Y_(a,r))
       =j_a Y_(a,1)...Y_(a,r) C_a.                   (Q4)

This follows by inserting C_a j_a=1 between successive factors. No new
cell projection is inserted per multiplication. The empty embedded word
is Q_a, not the identity on all K.

## 3. Quantitative elementary estimates

The parents supply the following estimates, restated with a-independent
upper constants for 0<a≤a_0. For compact smooth h define

    d(h)=(m||h'||+v||h''||)/2,
    R_0(h)=(m/2)||xh'||+(v/2)||xh''||+2v||h'||
              +(7m/4)||h||+(v a_0/6)||h''||.

The weighted domain additionally requires xh∈L²; compact smooth data
meet it. The microscopic parent's appended adjoint-domain argument
identifies its differential expression with the closed B on that class.
The single-factor bounds are

    ||j_a V_a(t) C_a h-V(t)h||≤a L_time(t,h),
    L_time(t,h)=||h'||+|t|d(h),

    ||j_a Z_a(s) C_a h-Z(s)h||≤a L_boost(s,h),
    L_boost(s,h)=||(Z(s)h)'||
                +int_0^|s| R_0(Z(sign(s)u)h)du.       (Q5)

At s=0 the integral is zero. Both estimates hold for either parameter sign.
For translations, exact cell equivariance gives
`T_a(ell) C_a=C_a T(aN_a(ell))`. Therefore

    ||j_a T_a(ell) C_a h-T(ell)h||
     ≤||(Q_a-1)T(aN_a(ell))h||
          +||T(aN_a(ell))h-T(ell)h||
     ≤2a||h'||=:a L_space(ell,h).                    (Q6)

The second inequality is the H¹ fundamental theorem for translations.
It is uniform in ell. Density and contraction give strong convergence
of each elementary comparison, locally uniformly in its physical
parameter, for every vector of K; the parents prove the time/boost
extension, and the same argument proves it for translations.

## 4. Fixed words, compact parameter sets, and an explicit rate

A word w consists of finitely many chosen factor types in Q2, in the
displayed left-to-right operator order. Allow their real parameters to
be continuous functions of p in a fixed compact parameter set P.
The lattice factor uses those parameters and the prescribed rounding;
its continuum factor Y_j(p) is strongly continuous. Put

    Y_a(w,p)=Y_(a,1)(p)...Y_(a,r)(p),
    Y(w,p)=Y_1(p)...Y_r(p),
    E_a(w,p)=j_a Y_a(w,p) C_a.                        (Q7)

The empty word has Y_a=1,Y=1,E_a=Q_a. For a nonempty word, Q4 and the
noncommutative telescoping identity give

    E_a(w,p)-Y(w,p)
      =sum_(j=1)^r A_(a,1)...A_(a,j-1)
         (A_(a,j)-Y_j)Y_(j+1)...Y_r.                 (Q8)

For fixed f, the continuum suffix vectors
`h_j(p)=Y_(j+1)(p)...Y_r(p)f` form compact subsets of K. Indeed finite
products of strongly continuous unitaries are jointly strongly continuous
by telescoping on a fixed vector; the continuous image of compact P is
compact. Contractions converging strongly, uniformly in their own compact
parameters at each fixed vector, also converge uniformly on a compact
set of vectors: choose a finite epsilon-net and use the difference norm
bound 2 for its approximation error. Applying this to each summand of
Q8 proves

    sup_(p in P)||E_a(w,p)f-Y(w,p)f|| -> 0, f∈K.     (Q9)

For real compact smooth f every h_j(p) is compact smooth with a common
compact support over P, and the needed derivatives are jointly continuous
in the parameters and position. For time this is finite propagation and
the smooth Dirac solution; for translations it is ordinary translation;
for boosts it is the parent's compact tilted-Cauchy orbit theorem.
Induct over the finitely many suffixes. Thus the following constants are
finite, and Q8 gives an explicit bound:

    k_w(f,p)=sum_(j=1)^r L_type(j)(parameter_j(p),h_j(p)),
    K_w(f;P)=sup_(p in P)k_w(f,p),
    ||E_a(w,p)f-Y(w,p)f||≤a k_w(f,p)≤a K_w(f;P).     (Q10)

For the empty word set k_empty(f,p)=||f'||, by Q3. Smoothness of the
parameter functions is not required for the supremum argument;
continuity and compactness suffice. The constants depend on the input,
word length/types, parameter set, m,v,a_0. No uniform estimate on all
unit vectors, growing word lengths, growing rapidities or vanishing m
is asserted. Complex data follow by complex linearity/density; the field
and spin statements below use real data.

## 5. Actual even-spin polynomials and limiting regions

Let `jw_a:CAR(K_a,R)^even -> spin^even` be the parent's compatible
isometric finite Jordan–Wigner map. The real isometry j_a induces the
isometric CAR embedding `iota_a(c_a(z))=c(j_a z)`. Its isometry follows
on every even-dimensional full finite Clifford matrix algebra and then
by completion, before restricting to the even part. Write
`Phi_a=iota_a o jw_a^(-1)`; no full odd spin map is being asserted.

For real compact smooth f_1,...,f_(2r) supported in an interval I, define

    A_a=jw_a(product_j c_a(C_a f_j)),
    A=product_j c(f_j),  M_j=||f_j||.                (Q11)

A_a is finite spin-local in the a-cell enlargement of I. It is an even
polynomial, not necessarily self-adjoint; its real and imaginary parts
obey the same statements. Let alpha_a(w,p) be the composition of the
**actual** spin time, integer-translation and scaled-boost automorphisms
in Q2. Their established even-CAR actions compose, so

    Phi_a(alpha_a(w,p)A_a)
        =product_j c(E_a(w,p)f_j).                   (Q12)

Since ||c(f)||=||f|| for real f, finite-product telescoping gives

    ||Phi_a(alpha_a(w,p)A_a)-alpha_(g(w,p))(A)||
      ≤sum_j epsilon_j(a,p) product_(k!=j) M_k,
    epsilon_j=||E_a(w,p)f_j-Y(w,p)f_j||.             (Q13)

Equations Q9–Q10 give uniform convergence and the explicit O(a) bound
obtained by replacing epsilon_j with a K_w(f_j;P). Finite polynomial
sums obey the corresponding sum of bounds with absolute coefficients.
More generally, a product of fields with different words assigned to
different coefficients is an actual even spin element after jw_a and
has the same bound. It is not described as an actual spin action on each
odd field. For actual transformed observables, all fields of each even
monomial share its word; joint products of such observables naturally
give the different-word assignment needed below.

The revised continuum parent identifies Y(w,p) with the Cauchy action
of the product g(w,p) in the proper orthochronous 1+1 Poincare group.
An elementary physical time t corresponds to coordinate translation
`(tau,ell)=(-t,0)`; spatial ell corresponds to `(0,ell)`; boost s has
eta=vs. These signs are fixed throughout. Its net satisfies
`A(D(I))=CAR(L²(I;R²))^even` and exact region covariance. Consequently
the limit in Q13 belongs to `A(g(w,p)D(I))`. This identifies a region
for these specified limiting observables, not a scaling-net exhaustion.

## 6. Approximate Poincare relations on the constructed observables

If two fixed words w,w' represent the same continuum group element for
each p∈P, then Q10 and the triangle inequality prove

    ||E_a(w,p)f-E_a(w',p)f||
       ≤a[K_w(f;P)+K_w'(f;P)].                      (Q14)

For general fixed L² data the same difference converges to zero by Q9.
Combining Q14 with Q13 proves the corresponding norm defect tends to
zero for each specified even polynomial; Phi_a is isometric, so this
is also the actual spin norm of the difference of its two transformed
observables. The constants are uniform on the stated compact parameter
set, including continuous correlated parameters in the comparison word.

Two useful exact continuum identities, with eta=vs, are

    Z(s)V(t)Z(-s)=T(-v t sinh eta)V(t cosh eta),      (Q15)
    Z(s)T(ell)Z(-s)=T(ell cosh eta)V(-(ell/v)sinh eta). (Q16)

They follow by transforming the coordinate translation vector (tau,ell)
with Lambda_eta, using tau=-t. Independently on the positive band,
`W(s)psi(q)=sqrt(E(F_s(q))/E(q))psi(F_s(q))`,
`F_s(q)=q cosh eta+(E(q)/v)sinh eta`, and
`E(F_s(q))=E(q)cosh eta+vq sinh eta`. Conjugation therefore sends E
and q to the displayed combinations. With time multiplier exp(+itE)
and translation exp(-iell q), it gives exactly Q15–Q16. The negative
band follows from reality, not from an unrelated sign convention.

These continuum relations are used as targets for Q14; they are not
inserted into the finite-a proof. The parent's lattice stress retains
its cos(aq) factor, and rounded translations have the additional defect
described after Q2. Finite-a norms and invariant-state checks can remain
correct even when a continuum relation or its physical parameter sign
is wrong. Those weak-control survivors must be retained in diagnostics.

## 7. The actual chosen-state covariance and all finite joint moments

Let `P_(a,+)=(1+sign D_a)/2`, `P_+=(1+sign D)/2`, and set
`S_a=j_a P_(a,+) C_a`. On all K this is an orthogonal projection:
`S_a²=S_a=S_a*`. It vanishes on Q_a-perp. Its real-complement identity
is precisely

    S_a+Gamma S_a Gamma=Q_a,                         (Q17)

because the lattice polarization complements to one and the cell maps
are real. It is not the identity on all K. Thus 2S_a is not being
declared the covariance of a vacuum on the full common CAR algebra.
Only the embedded cell-subspace moments are compared; no extension of
omega_a to every common-algebra element is chosen or required.

The parent's resolvent proof gives, for h∈H²,

    ||(S_a-P_+)h||≤a p(h),
    p(h)=||h'||+(m||h'||+v||h''||)/(4m).             (Q18)

Both operators are contractions, so density gives strong convergence
on K, uniform on compact vector sets by the finite-net argument. This
estimate requires fixed strictly positive m; no massless-uniform bound
is claimed.

Consider a finite collection of actual transformed even polynomials and
expand their ordered joint product. One resulting monomial has 2n real
fields with original inputs f_j and their block's assigned word w_j.
Put `z_(j,a)=Y_a(w_j,p)C_a f_j`,
`y_(j,a)=j_a z_(j,a)`, and `x_j=Y(w_j,p)f_j`.
Let epsilon_j=||y_(j,a)-x_j|| and M_j=||f_j||. The parent's actual
chosen state is quasifree on even CAR with positive covariance, so its
ordered pair entry is exactly

    G_(a,ij)=2<z_(i,a),P_(a,+)z_(j,a)>
             =2<y_(i,a),S_a y_(j,a)>,
    G_ij=2<x_i,P_+x_j>.                              (Q19)

These are complex sesquilinear pairings, not their real parts. Although
the covariance of overlapping fields is not antisymmetric, the ordered
Wick matrix is defined by W_ij=G_ij and W_ji=-G_ij for each i<j, with
zero diagonal. This construction keeps the
order of the original fields; it does not reorder noncommuting fields.

Expanding the difference of the two Q19 pairings in its first vector,
second vector and projection yields

    |G_(a,ij)-G_ij|
      ≤2[epsilon_i M_j+M_i epsilon_j
                    +M_i||(S_a-P_+)x_j||].          (Q20)

Here ||y_(j,a)||≤M_j and ||x_j||=M_j; the same bound holds for every
parameter value. Compact continuum word orbits and Q18 show uniform
entry convergence. For compact smooth inputs it is quantitatively O(a),
with coefficient
`2[K_(w_i)(f_i;P) M_j+M_i K_(w_j)(f_j;P)
  +M_i sup_(p∈P)p(x_j(p))]`.
Every required derivative seminorm on that orbit is finite by §4.

The ordered 2n-field expectation is the Pfaffian of that Wick matrix.
For four fields it is `G12 G34-G13 G24+G14 G23`. For n≥1 let
delta be the largest pair-entry error and
`C=2 max_j M_j²`, so both lattice and continuum entries have modulus
at most C. Expanding over the (2n-1)!! perfect matchings and telescoping
each product of n entries proves

    |omega_a(product_j c_a(z_(j,a)))
            -omega(product_j c(x_j))|
      ≤(2n-1)!! n delta C^(n-1).                    (Q21)

For n=0 the common moment is one and the error zero. If all inputs
vanish the assertion is immediate. Otherwise C>0. This proves uniform
convergence of every fixed finite joint moment, and O(a) for compact
smooth inputs. Polynomial expansion extends it to finite linear
combinations with explicit sums of absolute coefficient bounds. It is
not uniform in the degree, number of factors, or polynomial coefficients.

Each elementary lattice factor preserves P_(a,+): time and translation
commute with its Fourier multiplier, and the actual boost preserves its
positive band by the microscopic parent. Thus every common lattice word
leaves all these chosen-state moments exactly invariant, even though the
lattice words need not obey Poincare relations. Equivalently the actual
spin state is invariant under each of these actual automorphisms.
The continuum factors preserve P_+ and give the corresponding vacuum
invariance. Independently transforming different observables does not
in general preserve their joint correlation. Q14 and Q21 also control
replacement of a word by a continuum-equivalent word in any such fixed
joint moment; no exact finite-a relation is assumed.

## 8. Interpretation, parity, and frozen checks

The supplied full-spin GNS space is full Fock. The cyclic space of its
global even vacuum algebra is even Fock, and all constructed observables
and actions preserve that sector. No one-particle state is created from
the vacuum by an even polynomial. Writing odd auxiliary fields inside
Q19–Q21 does not produce an odd local spin-field scaling theorem.

The result is the convergence of specified actual observables and their
chosen-state correlations to the specified free local net, uniformly
for fixed compact parameter families. It gives approximate relations
on those sequences and exact covariance only in the continuum. It is
not a change of vacuum, a full scaling-net identification, a uniform
spin Lieb–Robinson estimate, or a statement about interactions, scattering
completeness or connected non-Gaussian fermionic correlations.

The entire proof and `CONTROL_PROTOCOL.md` are frozen before scientific
execution. A few distinct controls target composition and correlations:
literal finite spin words and ground-state joint products; independent
continuum semidirect-coordinate composition versus scalar pullback;
finite-box microscopic words and Brillouin covariance versus continuum
word vectors and Pfaffians. Finite boundaries and Fourier quadrature
are numerical limitations, not hidden proofs. Wrong time/displacement,
complex covariance and Wick-order variants test specific weaknesses;
weak survivors and finite-spacing defects are retained. All scientific
subprocesses have actual60s limits and complete pre-inspection streams.
Fresh independent review of this theorem remains required after handoff.

## 9. Source-bound author checks and handoff, 2026-10-12

Sections 1–8 above are preserved byte for byte from the pre-execution
410-line analytic freeze, SHA
`e6abc7aa1c3d8162654a12b784d3ba38d0b630f285f05be1fdb2b00ba6f62a2d`.
The frozen control protocol is
`9dda4a2e2c344aa764f82260d74b7e71df9a0e53c84aca1f4287594b9ef535ea`;
analytic-freeze metadata is
`14ac4be8df451e4fabefeab335043cd15e4c753e2778793fcf354a9372230c91`.
The external execution-pins anchor is
`ef3179b070ac93286a78b5c3f6c2eaab452fc02b0a9aa5d0dc77914c79d08665`.
It binds all scientific modules, variants, exact source copies, proof,
protocol and unchanged instructions before scientific imports.

No analytic correction, scientific code correction, failed baseline or
failed numerical refinement occurred in this packet. Root's complete
coauthor read of the frozen proof and plan reported no correction; that
read is not independent review. The microscopic boost parent remains a
provisional source dependency at this author handoff. Its separate review
receipt can be integrated by root later without changing this historical
freeze. Fresh independent review of this mixed theorem remains open.

The twelve scientific subprocesses contain 1006 diagnostic rows: 444
baseline/refinement rows all pass, and 102 of the 562 source-mutant rows
fail. All runs had actual subprocess timeout60s, complete stdout/stderr,
source-before/after identities and version records before inspection.
No scientific run timed out; the longest elapsed time was 1.194 seconds.
These counts inventory checks rather than supply proof or review grades.

| Distinct arithmetic route | Observed comparison |
|---|---|
| Literal six-site Pauli H/Q, actual spin permutation and mixed even conjugations | Largest even-matrix Frobenius residual `6.73e-15`; largest ordered 2/4/6-field ground-state moment residual `1.56e-15`, tolerance `5e-10` |
| Sequential scalar pullbacks versus independent spacetime semidirect-coordinate product | Largest complex-vector residual `2.89e-16`; Q15/Q16 residuals at most `1.13e-16`, tolerance `2e-11` |
| Sparse physical-cell lattice words, padded Brillouin polarization and continuum Fourier cell integrals | Q20/Q21 arithmetic bounds hold at the sampled spacings; all full numeric entries and nonzero relation defects retained |
| Coarse/fine box, line-quadrature, packet-quadrature and projector-grid comparison | Largest comparable change `1.04e-8`, below the fixed `8e-7` threshold; the predeclared higher refinement was therefore unused |

The fine-resolution spacing study gives the following retained values.
They are finite diagnostics; the analytic argument, not a fitted slope,
establishes Q9–Q21 and the rate. The Q20/Q21 bounds are conservative and
are tested using measured vector/pair errors, so they are not independent
numerical derivations of an O(a) rate.

| a | Maximum common-space vector error | Maximum complex pair error | Maximum 2/4/6 moment error | Maximum Q15/Q16 coefficient defect |
|---|---:|---:|---:|---:|
| .4 | .938344 | .277194 | .164797 | .770142 |
| .2 | .546430 | .175154 | .075064 | .379329 |
| .1 | .210834 | .081115 | .035922 | .104601 |
| .05 | .142922 | .054523 | .025850 | .099495 |

The error/a values for those vectors range from 2.108 to 2.858; no
monotonicity in a is assumed. In fact both tested Q16 defects rise slightly
from a=.1 to a=.05, as retained in `spacing_table.json`. Rounded inverse
translations agree exactly with a one-cell shift in all four rows, while
their distances from the identity are .843189, .514025, .270577 and
.137088 respectively. No finite-a real-translation group law is inferred.
The common-word chosen-state covariance residual is below `8e-16`; the
different-word correlations change. Invariance does not diagnose the
Lorentz relation defect. Main mixed-word outgoing translation amplitudes
were zero for these initially interior packets. The proof does not import
that finite-box fact as a microscopic locality estimate.

The five pinned wrong-source variants produced the following selective
failures. Every failed row and every survivor is retained.

| Source mutation | Targeted failures | Weak survivors |
|---|---|---|
| Physical time sign reversed | 12/106 literal-spin rows and 14/46 continuum rows | All coefficient and continuum norm checks; unaffected generators/covariance |
| Spatial translation direction reversed | 10/106 literal-spin rows and 14/46 continuum rows | All norm checks; zero-displacement even-word blocks |
| Q15 transformed displacement sign reversed | 4/46 continuum rows, specifically the four nonzero s,t Q15 rows | All nine Q15 norm checks, zero-parameter Q15 rows, all Q16 rows |
| Imaginary covariance discarded | 44/106 literal-spin rows, including all six ordered moments | All actual even-word matrix and norm checks |
| Pfaffian alternating sign removed | 4/106 literal-spin rows, the four degree4/6 joint moments | Both degree2 moments, all pair covariances, actual even matrices and norms |

Thus a norm-only suite would miss every mutation tested here. The literal
spin calculation supplies a separate complex-moment reference for the
covariance and Wick-sign variants. A lattice/continuum comparison that
shared a wrongly modified Wick formula would not by itself supply that
reference; this packet does not mislabel such a shared path independent.

All three deliberate integrity copies reject before scientific execution:
one changes candidate source, one changes the pinned proof, and one also
rewrites a source hash inside its manifest while retaining the original
external manifest digest. The last case rejects at that external anchor.
The original scientific files, frozen proof and all prior packets remain
unchanged. `evidence_inventory.json` covers complete row groups and raw
receipt hashes; `result_disposition.json` records every executed scientific
run; `summary.json` identifies the two unused optional refinement jobs.

The finite-spin reference state is a finite-chain ground-state oracle,
not the infinite chosen omega_a. The mixed study uses the supplied
infinite polarization approximated on a padded periodic grid. Finite
boxes and quadrature have an observed refinement check, not rigorous
numerical tail certificates. C5 compact polynomial fixtures exercise H²
arithmetic, while the quantitative theorem is stated for C-infinity
compact data. Checks cover finitely many parameters, not every point of
the compact parameter sets in the proof. Arithmetic routes are distinct
within one author context; they are not fresh independent reviewers.

`mixed_local_poincare_correlations/manifest.json` and `receipt.json` seal
the final note, every source, raw run, failure and survivor, with the
recursive seal boundary stated explicitly. Original dependency and
instruction hashes are refreshed at sealing. No editable prompt files,
axioms, audit verdicts, Git state, publication surfaces or prior sealed
packets were changed. No model/effort override or delegation occurred.


## Publication evidence, imports and review record

**Author/checker pairing:** Same selected model family and reasoning effort; separate reviewer contexts with formula exposure, not blinded or diverse-family. Root supplied routes and is a coauthor; the section note is root-authored. Mechanical preparation and reproduction add no independent scientific review.

Norm-only and zero-parameter wrong-sign survivors remain, together with all nonzero finite-spacing relation defects and mixed-state correlation changes. The independent false half-density expectation, low-cutoff failures, refinements and administrative recording correction remain. Floor translations are not a real group at positive spacing. No growing-word or operator-unit-ball uniformity is asserted.

The exact original note, source review, root coverage, all author/reviewer helper sources, complete results, rejected controls, survivors, timeouts and recording repairs are preserved through the [evidence map](../.claude/science/physics-loops/toe-local-continuum-20261012/EVIDENCE_MAP.json). Original source paths and SHA values identify frozen probes. The [literal publication map](../.claude/science/physics-loops/toe-local-continuum-20261012/PUBLICATION_EDITS.json) reconstructs the entire canonical note and runner without mathematical edits. Historical evidence is not relabeled as a new independent check.

Direct mathematical imports, each at the supplied scope stated in the original argument:

- [concrete gapped chain](CONCRETE_GAPPED_CHAIN_BOUNDED_THEOREM_NOTE_2026-10-12.md).
- [local even continuum](LOCAL_EVEN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-10-12.md).
- [microscopic local boost limit](MICROSCOPIC_LOCAL_BOOST_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-12.md).
- [continuum local boost](CONTINUUM_LOCAL_BOOST_BOUNDED_THEOREM_NOTE_2026-10-12.md).

The chosen free one-dimensional dynamics, positive m and v, scaling, quasifree state, CAR machinery and cell comparison are stated hypotheses or constructions; the framework does not select these data. There is no empirical prediction, interacting or three-dimensional result. Broader spin-scaling classification remains a separate question.

All mathematical helper sources and imported finite refinement specimens are explicit primary inputs. No helper registry or dependency-policy edit is proposed. Canonical execution, vocabulary, graph comparison and focused compatibility are pending root execution; global combined pipeline and strict audit lint are independent landing gates.
