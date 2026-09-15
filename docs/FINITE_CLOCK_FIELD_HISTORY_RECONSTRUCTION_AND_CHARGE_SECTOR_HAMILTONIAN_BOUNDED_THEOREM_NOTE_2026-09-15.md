---
claim_id: finite_clock_field_history_reconstruction_and_charge_sector_hamiltonian_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "For the supplied finite-clock Villain law at fixed finite N and beta>0, all finite field histories reconstruct a local clock field algebra and an injective positive transfer operator in the matched free state. Finite temporal fillings identify each reconstructed charge-sector Hamiltonian bottom with the static threshold. A conditional temporal averaging estimate also gives a strictly positive energy floor for each nonzero external charge profile. Native-law selection, continuum scaling and mobile matter are separate targets."
upstream_dependencies:
  - finite_clock_static_charge_transfer_hamiltonian_and_path_comparison_bounded_theorem_note_2026-09-15
  - finite_clock_ginibre_free_state_and_static_charge_bound_bounded_theorem_note_2026-09-15
runner: scripts/finite_clock_field_history_reconstruction_and_charge_sector_hamiltonian_2026_09_15.py
---

# Finite-clock field histories and the charge-sector Hamiltonian

**Date:** 2026-09-15
**Type:** bounded_theorem
**Status:** proposed_retained

For the supplied finite-clock Villain law, all finite sequences of field
insertions and transfer steps determine a common history representation.
The local clock field operators are bounded unitaries, the transfer operator
is injective, and its logarithm is a nonnegative Hamiltonian. A temporal
surface comparison proves that its charge-sector bottom is the static
threshold. Conditional averaging at charged vertices additionally gives a
strictly positive lower bound on each nonzero external charge sector. These
are author proof proposals awaiting independent review.

## Exact inputs and target

The [static transfer source](FINITE_CLOCK_STATIC_CHARGE_TRANSFER_HAMILTONIAN_AND_PATH_COMPARISON_BOUNDED_THEOREM_NOTE_2026-09-15.md)
is pinned to PR8144 at691f96525772ec0e7d06a528d14ad17324400f22.
The [matched free-state source](FINITE_CLOCK_GINIBRE_FREE_STATE_AND_STATIC_CHARGE_BOUND_BOUNDED_THEOREM_NOTE_2026-09-15.md)
is pinned to PR8140 at8a71d7fa8a87a451e5c49df31d18986574d73610, with its
provisional PR8133 inputs. The complete interacting source unit requires
independent review or prior landing of those bases. The present delta alone
cannot ratify its premises.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: finite_clock_static_charge_transfer_hamiltonian_and_path_comparison_bounded_theorem_note_2026-09-15
target_blocker_text: "Extend static insertion moments to the local field history algebra and identify the bottom of its full reconstructed charge sector."
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Independently review the history reconstruction and matched state passage; pursue fixed-clock continuum scaling and dynamical matter."
conditional_surface_status: "Supplied finite-clock Villain law, beta>0, fixed finite N and the matched free-boundary state. The quantitative energy upper bound additionally uses the source curvature assumptions."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Actual finite history Gram limits, bounded prefix operators, local inverse comparison and a positive temporal-surface coefficient bijection."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

| Input or obligation | Source and disposition |
|---|---|
| Clock Villain law, finite N>=1,beta>0 | Explicit supplied model; no native selection |
| Limits of all finite closed currents; matched temporal transfer | Provisional free-state source, reviewed as part of the full unit |
| Positive inverse comparison and static threshold | Provisional static transfer source |
| All-history Gram space, bounded field operators and injectivity | Part I below |
| Full history-sector bottom | Part II below; constructive temporal filling |
| Strict lower bound for nonzero external charge | Part III below; finite conditional averaging |
| Coulomb-form quantitative upper bound | Source large-beta curvature plus the identified sector bottom |
| Physical clock, continuum field, moving charged matter | Separate targets; no impossibility result or axiom-update claim |

All limits here are those of the same cofinal free-boundary state. Statements
about the reconstructed space do not identify every possible infinite-volume
representation or every Gibbs state. No all-state uniqueness is assumed.
Time is in the selected lattice units. Individual edge fields are kinematic
operators; gauge-invariant spatial loops belong to the observable subalgebra.

## Part I. Reconstructing finite histories

## 1. Enlarge the generator set honestly

On every finite spatial free box let tau_L=T_L/lambda_L, and let U_j multiply
by the clock character for finite integer spatial current j. A history word is

 w_L=U_(j0) tau_L^(n1) U_(j1) ... tau_L^(nr) U_(jr) Omega_L,
 n1,...,nr>=1.                                                     (1)

Adjacent zero-time characters are combined. The case r=0 is included, as is
j0=0. Every word has norm at most1 and total charge profile
rho=d0*(j0+...+jr), interpreted mod N. There are countably many words.

Two words with different charge profiles mod N are orthogonal by local gauge
invariance. For words with the same profile, their finite scalar product is a
sequence of spatial character insertions in a common temporal transfer
correlation. Between insertions, include temporal currents given by the
cumulative charge profile. At an insertion the change of this profile is
exactly its spatial divergence, so the resulting four-dimensional current is
conserved. The two distant ends carry vacuum charge0. This makes the scalar
product an actual finite closed-current expectation in the temporal limit.
Its cofinal spatial limit exists by the exact same free-state monotonicity
and exhaustion argument as in the source: first take the outer vacuum-time
limit at fixed spatial box, then the spatial limit; the supremum over those
finite prisms equals the cofinal free-box net for this fixed closed current.
This uses monotonicity of the character expectation, not a thin-prism
curvature estimate. No positivity of an arbitrary
complex linear combination is inferred from cosine positivity: that positivity
comes from the finite-volume vector norms before taking limits.

Write K(v,w)=lim_L<v_L,w_L>. Finite sums have positive Gram forms, so quotient
null combinations and complete to H_history. This is a larger space than the static-only construction; equality of their
charge-sector bottoms requires the additional comparison in Part II.

## 2. Bounded field and transfer operators

On formal history symbols, prefixing a character defines U_l[w]=[U_l w]. At every finite L,
<U_l v,U_l w>=<v,w>, U_l U_k=U_(l+k), U_l*=U_(-l), U_(N l)=I.
These equalities pass to the Gram limit. Thus each U_l extends to a unitary;
they give a bounded representation of the commuting local clock configuration
algebra, the inductive union/closure of finite cylinder algebras, not a selected physical
measurement rule. Prefixing tau defines S w=tau w. Finite identities give
0<=S<=I and ||Sx||<=||x|| for every finite sum, so S extends to a positive
self-adjoint contraction. The unit vacuum obeys S Omega=Omega.

Gauge transformations with finite spatial support act diagonally by each word's charge character.
This action is unitary, commutes with S, and sends U_j to its usual gauge
character times U_j. The Hilbert space is a direct sum of the finite-charge
profiles represented by the words. Gauge-invariant closed spatial-loop
operators preserve these profiles; individual edge fields transform between
them. Calling the latter kinematic field operators does not make them
physical gauge-invariant observables.

All charge-balanced finite multitime matrix elements generated by S and the
U_j reproduce the corresponding matched free-state closed-current correlations
by their definition and the prefix relations. Charge-unbalanced elements vanish
by the exact gauge selection rule. This is more than a separate cyclic
spectral representation for each static path.

## 3. No zero transfer subspace on the enlarged history space

The finite comparison U_j* tau_L^(-1) U_j<=K(j) tau_L^(-1) is the one from
the static transfer source. If a word has a nonempty next time interval, write
w_L=U_(j0) tau_L^n phi_L, n>=1, ||phi_L||<=1. Then

 <w_L,tau_L^(-1)w_L>
 <=K(j0)<phi_L,tau_L^(2n-1)phi_L><=K(j0).              (2)

For a one-character word the same bound follows from tau_L Omega_L=Omega_L.
This bound depends on the final spatial insertion, not the length of the
preceding finite history. It is not a uniform bound over arbitrary spatial
insertions. The proof also covers j0=0 with K(0)=1.

Each word's finite spectral measure has mass at most1 and moments converging
to those of S, hence converges weakly on[0,1]. Apply the continuous cutoffs
min(m,1/lambda), with value m at0, and then monotone convergence as in the static transfer source.
The limiting measure has inverse moment at most K(j0) and no atom at0.
The zero spectral projection of S kills every word, a dense generating set.
Thus S is injective on ALL of H_history, and H=-log S is a nonnegative
self-adjoint operator with a strongly continuous semigroup. Every word has
finite exponential energy moment bounded by K(j0). No physical continuous-time
calibration is introduced.

## 4. Embed the static space without assuming exhaustion

The closure of S-polynomials applied to single-character vectors U_j Omega
of charge rho embeds isometrically as the earlier static space, because all
its Gram moments agree. It is invariant under bounded self-adjoint S and is
therefore reducing. Its bottom is the earlier static E_rho. The full history
sector can contain an additional reducing subspace; inclusion alone gives
only an upper bound on its bottom. Part II proves equality by comparing every
history generator, without assuming time-zero cyclicity or identifying the
two spaces. Local gauge charge profiles are preserved by S.

## Part II. Finite temporal fillings identify the full bottom

## 1. The elementary positive current comparison

On any finite free clock cell complex, expand every plaquette Villain weight
in its discrete Fourier series with coefficients c_k>0. Integration/summation
over the link clocks gives

 W(J)=Z_J/Z_0,
 Z_J=sum_(d1* s=J modN) product_p c_(s_p).              (1)

Orientation may replace J with -J and leaves W unchanged. All summands are
nonnegative. If J-K=d1*S for a finite integer plaquette chain S, shift the
summation variable s by S. With

 R(S)=product_p max_k c_k/c_(k+S_p),

strict positivity and coefficient evenness give

 R(S)^(-1) W(K)<=W(J)<=R(S) W(K).                      (2)

The fiber bijection also covers absent fibers: both sums then vanish. For a
nonempty contractible free cube and a finite conserved current, a finite
integer filling makes its fiber nonempty. The constants only use plaquettes
in S and are independent of the surrounding box. Infinite matched free-state
limits therefore preserve(2). This is a positive expansion of the original
clock weight, not a positive expansion of its logarithm or square root.

## 2. A history differs from a static reference only at its two ends

Use a word from Part I in chronological order, with spatial insertions
j_1,...,j_m at integer times0<=t_1<=...<=t_m<=L. Put j_total=sum_i j_i
and rho=d0*j_total. Here L is the duration of this fixed history, not the
spatial volume. Its diagonal transfer moment

 F_w(n)=<w,S^n w>, n>=0,

is the closed-current expectation on a temporal interval of length2L+n:
one insertion history near the left end, its reflection/conjugate near the
right end, and the fixed temporal charge rho between them. The reference
W_(j_total)(2L+n) places the total spatial current at each outer end.

Move each left spatial insertion j_i from time0 to t_i. The required filling
is the temporal strip j_i times the interval[0,t_i], with orientation fixed by
the boundary formula for a product chain. Its side boundary is exactly the
change of cumulative temporal charge. Summing these strips gives an explicit
finite integer temporal-plaquette chain S_w whose boundary is the difference
of the left endpoint currents. Reflect it for the other end. No existence-only
homology argument, spatial filling or large-beta source estimate is needed.
Overlapping strips are added algebraically. Even if the two reflected fillings
touch, the local ratio bound for their sum is bounded by the product of their
separate ratio bounds, by applying the shift twice.

Consequently

 R(S_w)^(-2) W_(j_total)(2L+n)
 <=F_w(n)<=R(S_w)^2 W_(j_total)(2L+n).                  (3)

The constant is finite for each fixed history, independent of n and spatial
volume. One convenient upper bound on R(S_w) is the product over each unit
time interval of K(j_total-j_past), where j_past is the sum of insertions
already made by that interval. This is the final-current strip filling, not
a claim that histories with the same final charge have equal finite-time
amplitudes. If no time interval is present, it reduces to the static insertion.

## 3. Equality on the full history sector

The static reference is strictly positive and has finite rate E_rho by
the static transfer source. Its fixed shift in time2L does not change this rate. The fixed
multiplicative comparison(3) therefore gives

 -lim_(n to infinity) log F_w(n)/n=E_rho

for EVERY history word of charge rho. In particular every such word has
nonzero norm. Each word's spectral measure for the history Hamiltonian has
bottom E_rho. The spectral projection below E_rho kills all generating words
of that charge, hence their dense span. Since each word has spectral support
arbitrarily close to E_rho, the full charge-sector spectral bottom is E_rho.

This establishes the larger-space bottom in its
specified history reconstruction. It does not prove time-zero cyclicity and
does not identify arbitrary other infinite-volume representations. The earlier
Coulomb-form upper bound consequently holds in this full history sector under
the source's stated large-beta curvature assumptions. The local gauge charge
profile is still preserved by the transfer operator; mobile matter is not
created by this reconstruction.

## Part III. A local lower bound for nonzero external charge

The following bound uses N>=2; N=1 has no nontrivial charge profile.

Let w(k)>0 be the one-link temporal Villain weight on Z_N, m=min w,M=max w,
and set delta=(m/M)^6, r=1-delta. Positive Fourier coefficients imply that w
is nonconstant at finite beta and N>=2, hence0<delta<1 and0<r<1. The exponent6
is the maximum spatial vertex degree in the cubic spatial lattice.

## 1. Conditional averaging at charged vertices

For finite spatial configurations a,b, the kernel of the charge-projected
convolution is, up to its common normalization,

 C_rho(a,b)=average_eta exp[-2pi i<rho,eta>/N]
                       product_e w(a_e-b_e+(d0 eta)_e).             (1)

Let v have rho_v nonzero mod N. Condition on all eta except eta_v. Its
conditional probability has N positive weights, each a product of d_v<=6
terms between m and M. Consequently each probability is at least
(m/M)^(d_v)/N>=delta/N. Write this conditional distribution as delta times
the uniform law plus(1-delta) times another probability law. The nontrivial
charge character averages to0 under the uniform component, so its conditional
absolute expectation is at most r. This is a strict finite-clock mixing
estimate, not a Gaussian approximation.

For a set A of charged vertices with no adjacent pair, their conditional
eta variables are independent after all other eta are fixed: no edge joins
two variables in A. The same estimate multiplies. Integrating the remaining
variables and dropping their phases in absolute value gives pointwise

 |C_rho(a,b)|<=r^|A| C_0(a,b).                          (2)

This does not say C_rho itself has nonnegative entries. It is an absolute
kernel bound against the neutral projected kernel.

## 2. Transfer operator and infinite reconstructed sector

Spatial V commutes with local gauge transformations. Put
T_rho=V^(1/2) C_rho V^(1/2)=P_rho T, where P_rho is the orthogonal gauge-charge
projection and T commutes with it. The neutral projected T_0 has an entrywise
positive kernel and its norm is the full Perron eigenvalue lambda0: the unique
positive Perron vector is gauge invariant. Equation(2) therefore implies

 ||T_rho||<=r^|A| lambda0.                              (3)

Indeed |T_rho x|<=r^|A| T_0|x|, and the L2 norm gives(3). On the rho sector,
T_rho agrees with T. Thus0<=tau|rho<=r^|A|I. This form bound passes through
all finite history Gram limits, yielding the full history-sector estimate

 H|rho>=|A|[-log(1-(m/M)^6)] I.                         (4)

Only the finite history representation reconstructed earlier is identified;
other infinite-volume representations are not covered. The estimate does
not depend on the spatial box. Boundary degrees below6 only improve delta.

For s charged vertices, the bipartition supplies an independent subset of
size at least ceil(s/2). A separated nonadjacent test-charge pair has an
independent subset of size2; an adjacent pair is covered by size1. Charge
aliases rho=0 mod N are excluded from the charged count and retain the neutral
vacuum at energy0. N=1 has no nontrivial charge sector and needs no bound.

## 3. Physical scope and compatibility

Combining with the static/full-history threshold equality gives a strictly
positive lower bound for each nonzero external charge profile. Under the
additional source curvature assumptions, the existing Coulomb-form upper
bound remains valid. This brackets an external-charge energy; it gives neither
an exact interaction force nor a propagating charged-particle mass.

The lower bound can be extremely small at weak lattice coupling and tends to0
in parameter limits; no continuum-uniform mass claim is made. It applies to
nonzero local Gauss charge. Neutral transverse field excitations belong to the
rho=0 sector, where this bound is0, so it does not assert a neutral photon gap.
The model still conserves each external charge profile and supplies no matter
hopping term. No axiom change, general no-go or physical-law selection follows.


## No-Go Discipline Gate

This is an affirmative reconstruction and comparison. It submits no global
no-go, exhaustive route search, independent wall count or axiom requirement.
No negative packet PASS is claimed.

**N1.** The actual mechanisms are the free-state history Gram limit, bounded
operator prefixing, inverse spectral cutoffs, positive temporal fillings and
conditional temporal averaging at charged vertices.
Finite controls challenge charge projection, inverse normalization, strip
orientation and the reference-time shift. These are not five exhausted
research alternatives, and the negative route quota is not claimed as met.

**N2.** The field algebra depends on mixed-history limits; injectivity adds
the inverse bound; the full bottom adds temporal fillings and the static
threshold. The quantitative upper bound additionally depends on the prior
curvature estimate; the lower bound uses strictly positive finite clock weights
and an independent subset of charged vertices. These are connected proof inputs, not independent walls.

**N3.** The law, state, beta>0, finite N, charge labels and time units are
explicit. Dense generation is by the stated history space, not every physical
representation. No positive Fourier expansion of sqrt(V) or log(V), no
continuum limit and no time-zero cyclicity is assumed.

**N4.** The linked static source supplies only its minimal static space and
local inverse comparison. All-history operator reconstruction and the temporal
endpoint comparison are proved here. No negative prior finding is used as an
impossibility witness.

**N5.** The primary executes local coefficients, actual temporal-link sums,
finite history Gram/operator forms, integer strip boundaries and whole-cube
clock versus Fourier-current sums. Infinite cofinal limits and spectral dense
span arguments are written proofs, explicitly unexecuted in its cache lines.

**N6.** Extending from static correlations to the history field algebra is a
constructive partial closure under a supplied model. It does not settle model
selection, continuum scaling or moving matter, and does not declare any of
those targets impossible or require a new axiom.

**N7.** The strongest challenge is that a larger history sector may have lower
states than all static insertions detect. Part II addresses this by an actual
finite endpoint filling for every generating word and a volume/time-independent
coefficient ratio. A reviewer should check that the closed currents match the
same free state and that the2L time shift and both endpoint constants are kept.

**N8.** The preceding source left full field reconstruction open. The first
private history construction explicitly left its larger-sector bottom open.
The temporal filling provides a concrete mechanism to address that question;
it supplies no claim about unrelated infinite-volume representations.

## Author evidence, reproduction and limits

The self-contained primary has three finite families. Three square systems with
N=2,3,4 compare27history words against explicit charge-projected temporal
links, their Gram forms, field-prefix unitarity and inverse moments. Another
108history comparisons check temporal fillings and the full reference-time
shift. Two complete cubes compare direct link-clock enumeration with positive
plaquette-current fibers (4096and531441link assignments). These use different
calculation paths, all personally executed; they are not independent review.
A third family checks twelve charged/alias cases using explicit gauge sums and
independent Fourier charge blocks, and29single-vertex conditional distributions.
It tests both separated charge vertices and the excluded trivial harmonic.

The runner reads only its own source for integrity and declares a300-second
cache timeout. All scientific fixtures and actual controls are internal.
Floating checks cannot certify cofinal limits, operator-domain completion or
the infinite spectral theorem. Exact private proof/check provenance is at
campaign commit6a88f7785585a27a4c121537ab3b2d2b4ac52476; the public author packet records final source hashes,
actual mutations and mechanical validation. Full source review remains pending.
No audit verdict, main science, axiom, primitive or editable prompt is changed.
