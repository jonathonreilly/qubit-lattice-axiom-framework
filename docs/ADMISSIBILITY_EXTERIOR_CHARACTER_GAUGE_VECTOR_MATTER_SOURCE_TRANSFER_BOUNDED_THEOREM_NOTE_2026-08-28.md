---
claim_id: admissibility_exterior_character_gauge_vector_matter_source_transfer_bounded_theorem_note_2026-08-28
final_path: docs/ADMISSIBILITY_EXTERIOR_CHARACTER_GAUGE_VECTOR_MATTER_SOURCE_TRANSFER_BOUNDED_THEOREM_NOTE_2026-08-28.md
claim_type: bounded_theorem
claim_scope: "For a supplied finite reflected cubical slab, the supplied compact common-chart metric/scalar seam, a supplied compact commuting internal O(3)-vector matter carrier with full-support measure, supplied diagonal coframe coefficient maps, a supplied covariant hopping and onsite scalar coupling, and explicit nonnegative temporal gauge/matter signs, one shared-link action has an exact matter current in the connection equation, a constrained matter equation, nonzero reciprocal slice-action coframe/scalar response contributions, and a joint gauge-metric-scalar-matter reflected Gram. Strict disclosed signs give an injective temporal-gauge transfer on the metric quotient and injectivity after Haar projection only on the gauge-invariant Hilbert space. Exact negative-sign, zero-hopping, source-reflection, determinant-sector, and noncontractible-topology witnesses retain the boundaries. The carrier, action, coefficients, mass/source reading, measure, temporal extension, gauge identification, metric quotient, and physical matter/stress/Hamiltonian interpretation are explicit inputs rather than framework-selected consequences."
runner: scripts/admissibility_exterior_character_gauge_vector_matter_source_transfer_2026_08_28.py
independent_checker: scripts/admissibility_exterior_character_gauge_vector_matter_source_transfer_independent_2026_08_28.py
status: proposed_retained
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: admissibility_exterior_character_metric_source_polarized_seam_bounded_theorem_note_2026-08-28
target_blocker_text: "Test a supplied gauge-vector matter hopping term on the resulting positive metric/source seam, including the complete gauge-matter projector, strict transfer support, and spectral response; do not identify the scalar source with a Record or physical stress without a separate supplier."
source_of_blocker_text: handoff
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Test whether the finite mathematical transfer has any uniformly controlled matter spectral gap or continuum scaling on a disclosed family; do not identify it as physical time, Standard Model matter, or gravity without separate suppliers."
conditional_surface_status: "exact supplied shared-link compact gauge-vector matter model with reciprocal response, full finite OS transfer, strict-support qualifications, and determinant/topology/sign falsifiers; no framework-selected carrier, action, matter source, metric dynamics, continuum law, or physical identification"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the shared-link field equations, diagonal coframe/source responses, tensor-feature Gram, strict compact support, and counterexamples are exact finite mathematical theorems for a fully disclosed supplied action, while every physical supplier remains open"
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Shared-link gauge-vector matter transfer on the exterior-character seam

**Date:** 2026-08-28

**Type:** `bounded_theorem`

**Status:** `proposed_retained` — a review proposal, not an audit verdict.

## Result up front

The [metric/source polarized seam](ADMISSIBILITY_EXTERIOR_CHARACTER_METRIC_SOURCE_POLARIZED_SEAM_BOUNDED_THEOREM_NOTE_2026-08-28.md)
provides a compact dynamic feature `X=(G,r)` and an exterior-character
connection kernel with joint reflection positivity.  It contains no matter.
The [exterior-character action theorem](ADMISSIBILITY_DIRAC_KAHLER_EXTERIOR_CHARACTER_ACTION_TRANSFER_BOUNDED_THEOREM_NOTE_2026-08-28.md)
provides the ordered plaquette force but keeps any source or matter extension
open.

This note supplies a real commuting internal vector `phi_x in B^3` and uses
the same orthogonal link in the plaquette word and the covariant hopping term.
On a reflected slab, the complete one-step action is

```text
S_step
 = sum_cross S_MS(X_+,U_+;X_-,U_-)
   + sum_x tau_x ||phi_(x,+)-h_x phi_(x,-)||^2/2
   + [S_slice(X_+,R_+,phi_+)+S_slice(X_-,R_-,phi_-)]/2.       (1)
```

`S_MS` is the supplied polarized metric/scalar/connection seam.  The same
temporal vertex link `h_x` acts on the matter vector and the crossing
plaquette words, so Haar integration is one simultaneous gauge projection,
not two unrelated positive factors.

The spatial slice action has exterior-character plaquettes, gauge-vector
hopping, and an onsite scalar coupling.  Define the parent endpoint force by
`delta_(R_(e,+)) S_MS=<F_(e,+)^MS,X>`.  The exact full positive-endpoint link
equation is

```text
F_(e,+)^MS + 4 G_(e,+)
 + lambda_e d_e skw(R_e phi_s phi_t^T)=0.                    (2)
```

The last two terms are the exact half-slice contribution; for the standalone
slice equation their common factor is restored and they again sum to zero.
Here `G_e` is the ordered, cyclically rebased spatial-plaquette force.  The
slice term in the same one-step action gives a compact-ball matter equation,
nonzero diagonal coframe and scalar response contributions, and commuting
mixed variations.  A full one-step derivative also includes the already
supplied parent-seam derivative unless the matched-flat control below is used.

For nonnegative crossing character and hopping coefficients, the shared-link
kernel has a tensor-product representation Gram before the common Haar
projection.  Strict signs give injectivity in temporal gauge and, after
projection, only on the gauge-invariant Hilbert space.  Negative gauge or
matter signs give exact `[[1,2],[2,1]]` Grams.  An unmatched source profile
gives a non-Hermitian kernel.  In the explicit one-plaquette witness below,
the incident plaquette word stays in the improper component and therefore has
zero exterior-character tangent force while matter produces a nonzero
continuous current on its shared link.  This does not select the determinant
sector or remove a noncontractible improper flat holonomy.  A
determinant-minus-one link alone does not imply that every incident plaquette
word is improper.

This is a supplied internal Euclidean vector model.  It is not a Standard
Model field, a Record source, a physical stress tensor, an Einstein equation,
Lorentz covariance, a continuum theory, a physical clock, or a physical
Hamiltonian theorem.

## Imports and open boundaries

| Input | Role | Provenance | Open boundary |
|---|---|---|---|
| compact dynamic `X=(G,r)` seam, positive relative scalar normalization `alpha`, metric quotient, and seam action | metric/scalar/connection crossing kernel | linked polarized-seam parent | no framework-selected metric, scalar source, measure, or action |
| exterior-character `Q,f_n`, ordered force, Haar temporal links, and group support | gauge carrier and crossing representation | linked exterior-character parent | no physical selection of the orthogonal connection or action member |
| finite four-dimensional reflected cubical slab with open time boundary and separately supplied spatial boundary condition | locality, OS reflection, and topology domain | supplied combinatorial extension; the global counterexample below uses a periodic spatial torus | no continuum, causal, or clock interpretation |
| per-site dynamic positive spatial diagonal coordinates `a_(x,1),a_(x,2),a_(x,3)` with `G_x=diag(a_(x,i)^2)`, external reflection-even `a_(x,0)`, and coefficient maps `V_x,c_p,d_e` | weights the slice gauge, hopping, and potential terms | supplied common-chart specialization and incidence maps below | no independent-local-frame or diffeomorphism covariance; only each spatial triple is integrated |
| normalized full-support relative Lebesgue measure on every compact diagonal `G_x` domain, scalar interval, and their finite product | replaces the full-dimensional parent measure after diagonal pullback | supplied measure on the relative diagonal coordinates | no metric-dependent or framework-derived path measure |
| commuting internal matter `phi_x in B^3` | compact `O(3)` gauge-vector carrier | supplied mathematical target | no fermion, spin-statistics, flavor, Standard Model, or physical matter identification |
| normalized invariant Lebesgue measure on `B^3` | matter Hilbert measure and polynomial density | supplied full-support probability measure | no path measure derived from the axioms |
| `lambda_e`, independent temporal-extension coefficient `tau_x`, mass parameter, quartic parameter, scalar coupling, and their signs | spatial hopping, temporal support, and onsite action | supplied coefficients | `tau_x` is not derived from `lambda_0 d_0`; no coefficient, scale, or physical sign selection |
| the same `R_e,h_x` acting on exterior-character and matter factors | shared-link gauge identification | supplied identification tested here | no derivation that the tangent connection is a physical matter gauge field |
| real reflection-matched gauge-invariant slice action | positive bounded transfer multiplier with `[M,P]=0` | supplied OS extension | unmatched sources require a fresh test and fail below |
| one-to-one site-separating association `x -> (X_x,U_x)` and reflection-compatible anchor maps `b_P(p),b_E(e)` from spatial plaquettes/edges to site items | types `r_x,V_x,c_p,d_e` and the strict-support product without an aggregated pullback | supplied finite incidence data | other averaging or shared-feature maps preserve positivity only after a fresh kernel audit and require a fresh injectivity proof |
| physical source, coframe stress, time, and Hamiltonian readings | none | absent | displayed derivatives and transfer logarithms stay mathematical |

The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) supply neither the matter
carrier nor this action, measure, coefficient map, temporal extension, or
physical interpretation.

## Supplied slice action

For every site-separating parent item `x`, take positive diagonal Euclidean
coframe scales

```text
g_(x,mu nu)=delta_(mu nu) a_(x,mu)^-2,      a_(x,mu)>0,
V_x=1/(a_(x,0) a_(x,1) a_(x,2) a_(x,3)),
c_(x,mu nu)=V_x a_(x,mu)^2 a_(x,nu)^2,
d_(x,mu)=V_x a_(x,mu)^2.                               (3)
```

On the compact diagonal subdomain of the parent metric feature,

```text
G_x=diag(a_(x,1)^2,a_(x,2)^2,a_(x,3)^2).                (4)
```

with each spatial triple the positive coordinates of the dynamic parent `G_x`
and each `a_(x,0)` a supplied positive reflection-even external scale.
Equation (4) is a common-chart specialization, not a local-coordinate theorem.
Use normalized Lebesgue measure in the relative diagonal entries and scalar
coordinate, with full support on the compact relative domain; this is a new
supplied measure, not the measure-zero restriction of full-dimensional
Lebesgue measure on `Sym(3)`.  One common domain for every displayed control
has `epsilon<=1`, `M>=49`, and source radius `R>=1`.

Supply reflection-compatible anchor maps `b_P(p)` and `b_E(e)` from each
spatial plaquette and edge to a site-separating parent item.  For
`p || i j` and `e || i`, abbreviate

```text
c_p=c_(b_P(p),i j),       d_e=d_(b_E(e),i).             (4a)
```

The rational local control assigns its plaquette, edge, and onsite term to one
common item.  Other averaging prescriptions are different supplied actions.

Let `R_e in O(3)` on stored spatial links and `phi_x in B^3`.  Under a local
internal gauge transformation,

```text
R_(x->y) -> q_y R_(x->y) q_x^-1,
phi_x -> q_x phi_x.                                     (5)
```

For fixed `n>=1`, define

```text
S_slice
 = sum_(spatial p) kappa_p c_p f_n(Q(W_p))
   + (1/2) sum_(spatial e) lambda_e d_e
       ||phi_t-R_e phi_s||^2
   + sum_x V_x U_x(phi_x;r_x),                          (6)

U_x(phi;r)
 = [(m_x^2-zeta_x r)/2] ||phi||^2
   + (gamma_x/4)||phi||^4.                              (7)
```

Here `r_x` is the scalar coordinate of the parent item assigned one-to-one to
site `x` in the displayed site-separating model; `zeta_x` is a supplied scalar-to-matter
normalization.  It is not identified as Record content, mass density, or
energy.  The compact domains make (6) finite for every finite real
`m_x^2,gamma_x,zeta_x,r_x`.  Nonnegative `gamma` is convenient but not needed
for finite-volume boundedness on `B^3`.

Equations (4a)–(7) are exactly gauge invariant because the anchors and metric
weights are gauge singlets, `Q` is a class function,
the hopping norm is covariant, and the potential depends only on `||phi||`.
The scalar, relative-diagonal metric, and matter measures are independent
supplied full-support product measures.

## Exact shared-link equations

For each occurrence of an unfrozen stored link in a plaquette, retain the
ordered cyclic re-basing `U_(p,e)`, orientation sign `epsilon_(p,e)`, and
proper-component indicator `eta_p` from the exterior-character parent.  Put

```text
G_e = sum_(p,e occurrences)
  eta_p epsilon_(p,e) kappa_p c_p
  f_n'(Q_p) skw U_(p,e).                                (8)
```

Under `R_e(t)=exp(tX)R_e`, `X in so(3)`, the plaquette derivative is
`8<G_e,X>` in the parent's inner product.  For `e:s->t`, the hopping derivative
is

```text
-lambda_e d_e phi_t^T X R_e phi_s
 = 2 lambda_e d_e
   <skw(R_e phi_s phi_t^T),X>.                          (9)
```

For the standalone `S_slice`, their sum gives
`4G_e+lambda_e d_e skw(R_e phi_s phi_t^T)=0` after division by the
common factor two.  In `S_step`, the half-slice variation is exactly
`<4G_e+lambda_e d_e skw(R_e phi_s phi_t^T),X>`; adding the parent endpoint
force gives (2).  The matter current is therefore in the same link equation,
not a separately postulated source.  It does not alter the need to cyclically
rebase every plaquette word.

The matter recoil is reciprocal at the action level.  For a target variation
`delta phi_t` and link tangent `X`, either differentiation order gives

```text
D_(phi_t) delta_R S_hop[delta phi_t,X]
 = delta_R D_(phi_t) S_hop[delta phi_t,X]
 = -lambda_e d_e delta phi_t^T X R_e phi_s.             (9a)
```

In the rational control below, take `delta phi_t=e_1` and the planar
generator; both orders equal `6/175`.  This is ordinary Hessian symmetry of
the supplied hopping action, not a derived conservation law.

For an interior matter value `||phi_x||<1`, the standalone slice variation is

```text
0 = sum_(e:x=s(e)) lambda_e d_e
      (phi_x-R_e^T phi_t)
    + sum_(e:x=t(e)) lambda_e d_e
      (phi_x-R_e phi_s)
    + V_x [m_x^2-zeta_x r_x+gamma_x||phi_x||^2] phi_x.  (10)
```

For the positive endpoint of `S_step`, write the left side of (10) as
`E_(x,+)^slice`.  The exact full equation is
`0 in tau_x(phi_(x,+)-h_x phi_(x,-))+E_(x,+)^slice/2+N_(B^3)(phi_(x,+))`;
the negative endpoint has the reflected formula.  Thus the independent
temporal coefficient is not silently added to the standalone equation with a
wrong factor.  At `||phi_x||=1`, equation (10) is replaced by the corresponding normal-cone
variational inequality.  For an exact boundary control, keep only
`U(phi)=-||phi||^2/2` on `B^3` and take `phi=e_1`; then
`grad U=-e_1` and `-grad U=e_1 in N_(B^3)(e_1)`.  No unconstrained equation is
claimed on the compact boundary.

## Coframe, scalar, and mixed response

Let `D_(x,l)=a_(x,l) partial_(a_(x,l))`.  Directly from (3)–(4a),

```text
D_(x,l) V_x=-V_x,
D_(x,l)c_p
 = 1_(b_P(p)=x)[2(delta_(l i)+delta_(l j))-1]c_p,
D_(x,l)d_e
 = 1_(b_E(e)=x)(2 delta_(l i)-1)d_e.                 (11)
```

Therefore the exact diagonal coframe derivative contributed by the spatial
slice action (6) is

```text
T_(x,l) := D_(x,l) S_slice
 = sum_(spatial p || i j, b_P(p)=x)
     [2(delta_(l i)+delta_(l j))-1]
     kappa_p c_p f_n(Q_p)
   + (1/2) sum_(spatial e || i, b_E(e)=x)
     (2 delta_(l i)-1) lambda_e d_e
     ||phi_t-R_e phi_s||^2
   - V_x U_x(phi_x;r_x).                              (12)
```

The scalar response and two mixed derivatives contributed by `S_slice` are

```text
partial_(r_x) S_slice = -zeta_x V_x ||phi_x||^2/2,
D_(x,l) partial_(r_x)S = partial_(r_x)D_(x,l)S
                    = zeta_x V_x ||phi_x||^2/2,
partial_(r_x) grad_(phi_x)S
 = grad_(phi_x) partial_(r_x)S = -zeta_x V_x phi_x.  (13)
```

For `l=1,2,3`, one endpoint of the full `S_step` has the relevant dynamic-parent
`S_MS` derivative plus one half of (12); its `r_x` response similarly has the
parent derivative plus one half of (13).  The external `a_(x,0)` is not a
Hilbert-space endpoint coordinate: a reflection-matched common variation acts
on both half-actions and gives `(T_(x,0,+)+T_(x,0,-))/2`, with no parent
`G` derivative.  Under a simultaneous matched variation of both dynamic
endpoints, the two half-slice contributions add to (12)–(13).  At matched
endpoints, flat relative holonomy, and zero metric/scalar mismatch, both
parent first derivatives vanish, so the rational values below equal the full
simultaneous matched response as well as the standalone slice response.  Likewise
`D_(x,l) delta_R S=delta_R D_(x,l) S` term by term.  These are ordinary
mixed-partial identities of the supplied action, not a Ward identity or a
physical stress theorem.  If `R` is later made metric-dependent, its chain
rule must be added.

For the conditional finite matter/slice partition function
`Z_matter(r | fixed parent seam data and geometry)`, with `r` held as an
external profile rather than integrated,

```text
partial_(r_x) log Z
 = zeta_x V_x <||phi_x||^2>/2,                        (14)
```

and the Hessian in those fixed source-profile variables is the
positive-semidefinite covariance of `zeta_x V_x||phi_x||^2/2`.  At one decoupled
site with `m^2-zeta r=gamma=0`, normalized Lebesgue measure on `B^3` gives
`E||phi||^2=3/5`, `E||phi||^4=3/7`, and the exact strict witness
`partial_r^2 log Z_matter=3 zeta^2 V_x^2/175` for `zeta!=0`.  This is a
mathematical susceptibility, not a statement about the full transfer
partition that integrates dynamic `r`; that object also contains the parent
`S_MS` derivatives.

## Exact rational response witness

Choose

```text
(a_0,a_1,a_2,a_3)=(2,3,5,7),
V_x=1/210,       c_p=c_12=15/14,      d_e=d_1=3/70.  (15)
```

Use `n=1`, unit plaquette/hopping coefficients, the rational rotation with
`cos(theta)=3/5,sin(theta)=4/5`, and

```text
phi_s=e_1,       phi_t=e_2,
R e_1=(3/5)e_1+(4/5)e_2.                             (16)
```

Then

```text
Q=16/5,
S_gauge=24/7,
||phi_t-R phi_s||^2=2/5,
S_hop=3/350.                                         (17)
```

At one site take `||phi||=1,m^2=1,r=1/2,zeta=1,gamma=0`.  The site term is
`1/840`, so the local spatial action is `2063/600=14441/4200`.  Take the
parent crossing data matched and flat, as described above.  Equations
(11)–(13) then give

```text
(T_0,T_1,T_2,T_3)
 = (-14441/4200, 14431/4200, 14359/4200, -14441/4200),
partial_r S=-1/420,
D_(x,l) partial_r S=1/420.                           (18)
```

Every value in (15)–(18) is derived by exact rational arithmetic.
For the same stored spatial link and the planar generator
`X=[[0,-1,0],[1,0,0],[0,0,0]]`, direct differentiation gives
`delta S_gauge=48/7` and `delta S_hop=-9/350`.  The force form of (8)–(9)
gives the same two values, hence the exact combined derivative is
`2391/350`.  This checks the relative normalization in (2), not only a
zero-gauge-force special case.

## Improper component and topology

For a one-plaquette control, let its word and shared link both be
`F=diag(-1,1,1)`, with all other ordered factors equal to the identity, and
take `phi_s=e_1`, `phi_t=e_2`.  Every continuous tangent variation of this
incident plaquette word stays within the improper component and leaves the
exterior character constant, so its plaquette term has zero tangent force.
The matter current on the shared link is

```text
skw(F e_1 e_2^T)
 = (1/2) [[0,-1,0],[1,0,0],[0,0,0]] != 0.            (19)
```

Matter can therefore exert a continuous current on this link while the
incident improper plaquette word supplies no exterior-character tangent
force.  This is a one-plaquette comparison, not a claim that the determinant
of one link fixes the components of all incident plaquettes.  It does not
select the determinant component.  Let

```text
P=diag(-1,-1,1) in SO(3),
F=diag(-1,1,1) in O(3)\SO(3).                        (20)
```

Both have `Q=16`.  With `phi_s=phi_t=e_3`, both hopping terms vanish, so the
complete local action has an exact proper/improper collision.

There is also a global collision.  On the periodic flat-seam witness, place
`F` on the stored x-edges crossing one noncontractible x-seam and identity on
all other links.  Every plaquette has `Q=0`.  Set `phi_x=e_3` at every site.
Every identity and `F` fixes `e_3`, so every hopping term vanishes and the
onsite terms equal those of the trivial connection.  The coupled action does
not lift the noncontractible improper flat sector.

## Shared-link reflected Gram

Use the newly supplied normalized full-support relative measure on each
compact diagonal `X_x` domain, normalized Haar measure for every orthogonal
link, and

```text
d nu(phi)=3/(4 pi) 1_(||phi||<=1) d^3 phi.           (21)
```

For every temporal matter edge define `tau_x>=0`.  Its crossing factor is

```text
exp[-tau ||psi-h phi||^2/2]
 = exp[-tau||psi||^2/2] exp[-tau||phi||^2/2]
   sum_(k>=0) tau^k/k!
   <psi^(tensor k),h^(tensor k)phi^(tensor k)>.      (22)
```

Every coefficient is nonnegative.  Multiply (22) by the parent dynamic
metric/scalar/exterior-character feature expansion.  Because the same `h`
occurs in both factors, each term is a matrix coefficient of the tensor
product of the exterior representation and the vector tensor power.  Haar
integration is the orthogonal projector onto their simultaneous invariant
subspace.  Thus the complete shared-link crossing kernel is a sum of squares;
this is not an inference from pointwise-positive Boltzmann weights.

Here is the full reflected form.  Write a positive-half history as
`z_+=(X_+,U_+,phi_+)`, including the site metric/scalar pairs, every oriented
spatial link, and every matter vector.  Geometric time reflection sends sites
and ordered edge endpoints to their reflected sites and endpoints.  Define
`theta z_-` by pullback to the positive half:

```text
(theta G)_x=G_(theta x),   (theta r)_x=r_(theta x),
(theta phi)_x=phi_(theta x),
(theta U)_(x->y)=U_(theta x->theta y),
U_(y->x)=U_(x->y)^(-1).                              (23a)
```

The last convention automatically inverts any canonically reoriented
temporal edge.  Thus `G` and the dynamic `r` reflect as site fields, `phi`
reflects as an internal Euclidean vector, and link orientation is explicit.
For a bounded positive-half observable `F`, the antilinear reflection is

```text
(Theta F)(z_-)=overline(F(theta z_-)).
```

In temporal gauge, the product of the parent feature expansion and (22) has
one joint feature index `A` and the explicit form

```text
K_cross(z_-,z_+)
 = sum_A c_A overline(Phi_A(theta z_-)) Phi_A(z_+),
c_A >= 0.                                             (23b)
```

Let `W_+(z_+)>0` contain every plus-half multiplier, including
`exp[-S_slice(z_+)/2]` and the one-sided factors extracted from the parent
seam.  Reflection matching means `W_-(z_-)=W_+(theta z_-)`; the finite product
measure has the same property.  Consequently

```text
Z^(-1) int (Theta F) F exp(-S_step) dmu_- dmu_+
 = Z^(-1) sum_A c_A
   |int_+ F(z_+) W_+(z_+) Phi_A(z_+) dmu_+|^2 >= 0.   (23c)
```

This is the antilinear reflected Gram for the full supplied
metric/scalar/gauge/matter carrier.  Restoring the temporal links and
integrating their normalized Haar measures applies the same simultaneous
gauge projector `P` to the joint features; it does not create independent
gauge and matter projectors.

All spatial plaquettes, spatial hopping, onsite potentials, and scalar-source
terms are real, gauge invariant, and reflection matched.  They enter through
a bounded strictly positive multiplier `M` on the compact domain.  With `C`
the temporal-gauge crossing operator and `P` the simultaneous gauge projector,

```text
T = M P C M = M C P M >=0,       [M,P]=[C,P]=0.      (23)
```

The source is therefore inside the complete transfer multiplier rather than
deleted from the OS test.  In particular the dynamic coordinate `r` in
(23a) reflects as a scalar.  The unmatched-source control (26) instead freezes
a deliberately non-reflection-matched external profile
`r_-(x) != r_+(theta x)` and therefore changes the reflection data; it is not
a counterexample to the matched dynamic-source kernel.

## Strict support and transfer logarithm

For every strict `tau_x>0`, the temporal-gauge matter kernel
`exp(tau psi dot phi)` is injective on `L^2(B^3,nu)`.  If its quadratic form
vanishes, (22) makes every tensor moment of the input vanish.  Polynomial
density on the compact ball then forces the input to vanish.  No analytic
continuation or literature theorem is needed.

For strict parent crossing couplings and `alpha>0`, the parent
metric/scalar/connection operator is injective on its metric quotient.  Its
tensor product with the strict matter operator is therefore injective in
temporal gauge.  The positive compact multiplier `M` preserves injectivity.
After Haar integration, `ker P` remains an exact nullspace on the full
kinematic carrier; injectivity holds only on `P H`.

Restricting the parent metric to the compact diagonal domain does not borrow a
density conclusion for free.  Ordinary polynomials in the three positive
diagonal entries and `r` are dense on that compact relative domain, while
`ell(G)=Tr G` has a strict positive lower bound.  Multiplying an approximant
to `f/ell^N` back by `ell^N` reproduces the parent's homogeneous tail argument
on the diagonal coordinates.  Hence the strict parent support proof survives
this explicit restriction.

At `tau=0`, the matter kernel is constant and rank one.  A nontrivial matter
domain therefore makes the transfer noninjective even if every gauge coupling
is strict.  Zero parent coupling, zero parent scalar normalization, raw
coframe gauge copies, or aggregated shared features retain the parent null
qualifications.

This strict statement uses the supplied one-to-one site-separating parent
items.  Identifying several sites with one `X` is a pullback that preserves
the Gram proof but can destroy feature separation, so aggregated features are
not covered by the injectivity claim.

On the injective positive carrier, normalize by the top eigenvalue and define
the densely defined self-adjoint logarithm by spectral calculus.  On a carrier
with any of the displayed nullspaces, restrict to the support or OS null
quotient first.  This is a finite mathematical generator, not a physical
Hamiltonian or clock.

## Exact Gram and reflection controls

For an action-derived exact control take matched parent data
`X=(I,r=1)`, `alpha=1`, and `n=1`, so `b(X,X)=2`.  Choose two histories
`U_0=I,U_1=diag(-1,-1,1)` with relative `Q=16` and set the parent crossing
coefficient to `log(2)/32`; its off-diagonal is `1/2`.  Take matter histories
`phi_0=0,phi_1=e_1` and `tau=2 log 2`, so their matter off-diagonal is `1/2`.
Finally set `m^2=gamma=0` and `zeta=4 log(2)/V_x` in the matched `r=1` onsite
term, with all other spatial half-action terms zero in this control.  The two
half-action multipliers are then exactly `1,2`.  The complete
Gram derived from these histories and the disclosed action is

```text
G_+ = [[1,1/2],[1/2,4]],       det G_+=15/4.         (24)
```

For a negative gauge crossing coefficient, keep the matter histories equal
and take effective coefficient `-log(2)/16` at `Q=16`.  For a negative matter
coefficient, keep the gauge histories equal, use antipodal matter values, and
take `tau=-log(2)/2`.  These action-derived dyadic choices give in either case

```text
G_- = [[1,2],[2,1]],           det G_-=-3.           (25)
```

Positive diagonal half-action multipliers cannot repair this inertia.

Reflection matching of the scalar source is independently load-bearing.  Set
the crossing coefficients to zero.  Keep the preceding `m^2=gamma=0` and
`zeta=4 log(2)/V_x`; take `r_+=1` and `r_-=0`.  The action therefore derives
positive-side half multipliers `(1,2)` and negative-side half multipliers
`(1,1)`, with rows indexed by positive histories.  The kernel is

```text
K = [[1,1],[2,2]] != K^T,
(1,-i) K (1,i)^T = 3-i,
(3,-2) K (3,-2)^T = -1.                              (26)
```

Thus an unmatched source profile does not define a reflection-positive form.

## Nonselection and strongest missing lemma

Every parent member `f_n` admits the construction, because its positive
character expansion and ordered force are the only member-specific inputs.
The metric weights, hopping, source response, and OS test therefore do not
select `n=1`.  Nor do positivity and covariance select the matter carrier,
mass, quartic term, source normalization, or coefficients.

The strongest missing lemma is a framework-native supplier that identifies a
realized matter carrier and source observable, derives their shared orthogonal
transport, action, measure, and coefficients, and physically identifies the
coframe/source derivatives and transfer generator.  Without it, this exact
model is a conditional discriminator rather than near closure of matter,
gravity, or time.

## Proof-obligation graph

| Obligation | Status |
|---|---|
| compact gauge-vector carrier and invariant measure | supplied and explicitly defined |
| shared-link gauge covariance | proved by (5)–(7) |
| ordered link equation with matter current | proved by (8)–(9) |
| constrained matter equation | proved by (10) |
| coframe/scalar responses and reciprocity | proved by (11)–(14) |
| nonzero exact witness | proved by (15)–(18) |
| improper local current and determinant collision | proved by (19)–(20) |
| noncontractible coupled flat-sector witness | proved after (20) |
| full shared-link reflected Gram | proved by (21)–(23) |
| strict matter support and qualified injectivity | proved by tensor moments and compact polynomial density |
| sign and source-reflection falsifiers | proved by (24)–(26) |
| physical matter/source/stress/action selection | open; strongest missing lemma above |
| continuum, Lorentz, Einstein, physical Hamiltonian, or clock law | open and not inferred |

The graph is acyclic.  The target-equivalent physical supplier is not used to
prove the finite theorem.

## No-Go Discipline Gate

The note contains bounded negative statements, so N1–N8 are recorded even
though the claim type is not `no_go`.

### N1 — failed attack routes

| Route | Attempt and exact failure | Authority | Marker |
|---|---|---|---|
| matter independent of the shared link | Replace `R_e phi_s` by `phi_s`; the hopping link derivative is identically zero, so no matter current enters (2) | compare (6) and (9) | `ATTEMPTED` |
| covariant hopping without a gauge action | Keep hopping but delete the plaquette term; covariance survives but neither `G_e` nor a curvature action is supplied | (2), (6), and current-main local-form precedent below | `ATTEMPTED` |
| internal scalar matter | Use a trivial one-dimensional `O(3)` representation; hopping can be positive but its link current is zero | (9), which vanishes for the trivial representation | `ATTEMPTED` |
| negative temporal hopping | Set `tau<0`; the antipodal two-history Gram (25) has determinant `-3` | (22), (25) | `ATTEMPTED` |
| zero temporal hopping | Set `tau=0`; the compact matter kernel is constant and rank one | strict-support section | `ATTEMPTED` |
| restrict by hand to `SO(3)` | The improper collision is removed only by changing the supplied domain; the action itself does not select that sector | (19)–(20) and torus witness | `ATTEMPTED` |

The successful shared-link compact vector construction is not counted as a
failed attack.  Fermionic matter, other compact representations, heat-kernel
actions, local trivializations, and native Record/source suppliers remain live.

### N2 — wall independence

The feature domain and its measure are kept separate because a carrier does
not select a probability law.  The crossing seam and spatial slice action are
separate independently closable units.  Physical meanings are not collapsed.

| Wall | Independently closable content |
|---|---|
| parent-seam | metric/scalar/exterior-character crossing kernel and signs |
| matter-carrier | `B^3`, internal `O(3)` action, and bosonic reading |
| matter-measure | normalized full-support invariant measure |
| slice-action | coframe weights, plaquettes, hopping, potential, and coefficients |
| source-reading | physical meaning of the scalar coordinate and `zeta` |
| stress-reading | physical meaning of (12)–(13) |
| reflection | plane, boundary, half-actions, and source matching |
| gauge-space | temporal links, simultaneous projector, quotient, and physical subspace |
| topology | spatial boundary conditions and global holonomy sector |
| continuum-Lorentz | refinement and Lorentzian continuation |
| Hamiltonian-clock | physical generator and time observable |

`I` means closing one wall does not close the other; `--` is the diagonal.

| | seam | carrier | measure | action | source | stress | reflection | gauge | topology | continuum | Hamiltonian |
|---|---|---|---|---|---|---|---|---|---|---|---|
| seam | -- | I | I | I | I | I | I | I | I | I | I |
| carrier | I | -- | I | I | I | I | I | I | I | I | I |
| measure | I | I | -- | I | I | I | I | I | I | I | I |
| action | I | I | I | -- | I | I | I | I | I | I | I |
| source | I | I | I | I | -- | I | I | I | I | I | I |
| stress | I | I | I | I | I | -- | I | I | I | I | I |
| reflection | I | I | I | I | I | I | -- | I | I | I | I |
| gauge | I | I | I | I | I | I | I | -- | I | I | I |
| topology | I | I | I | I | I | I | I | I | -- | I | I |
| continuum | I | I | I | I | I | I | I | I | I | -- | I |
| Hamiltonian | I | I | I | I | I | I | I | I | I | I | -- |

Exact separators cover the closest pairs.  The scalar and vector carriers
admit many measures.  The negative-sign and zero-coupling models use the same
carrier but change the action.  Equation (6) is defined before a reflection
plane or projector is chosen.  The unmatched-source witness keeps the action
formula but changes reflection data.  Open versus periodic topology does not
change the local current.  A source reading does not identify a metric
derivative as physical stress.  The finite Gram can be supplied without a
continuum, Lorentzian continuation, physical Hamiltonian, or clock, and any of
those interpretations can be stipulated without proving the Gram.

### N3 — hidden-wall scan

The complete literal scan used `assume`, `assuming`, `suppose`, `choose`,
`supplied`, `canonical`, `background`, `by construction`, `registered`, and
the required close variants.

| Hit family | Disposition |
|---|---|
| `supplied` | every scientific occurrence maps to the Imports table: slab, feature, carrier, measure, action, coefficients, reflection, gauge space, or physical boundary |
| `choose` | exact witness data and negative controls only; no selected physical value |
| `positive` | distinguishes metric positivity, Gram positivity, sign hypotheses, or positive multipliers; never means empirically correct |
| `matter` | always the supplied internal commuting vector until a physical supplier exists |
| `source` and `stress` | mathematical scalar and derivatives (12)–(14); no Record, energy, or gravity meaning |
| `canonical` | no scientific hit claims a canonical carrier, action, source, or Hamiltonian; cache mechanics only |
| `background` | each spatial diagonal triple coordinates the dynamic supplied parent `G_x`; only `a_(x,0)` and the rational evaluation point are fixed inputs, and neither is a derived spacetime background |
| `assume`, `assuming`, `suppose`, `by construction`, `registered`, `as is standard`, `framework provides`, `bridge context`, `naturally`, `obviously`, `standard QFT` | no hidden premise; hypotheses use definitions and Imports |

No literature value, float reconstruction, fitted coefficient, Grassmann
measure, fermionic sign, or local-coordinate trivialization is hidden.

### N4 — residual matching

| Source and literal location | Residual | Use here | Match |
|---|---|---|---:|
| metric/scalar seam, `docs/ADMISSIBILITY_EXTERIOR_CHARACTER_METRIC_SOURCE_POLARIZED_SEAM_BOUNDED_THEOREM_NOTE_2026-08-28.md:88-105`, `:107-195`, `:310-413` | supplied compact feature, positive crossing Gram, quotient, and physical selection open | supplies only `S_MS`, feature/measure, and strict parent kernel | yes |
| exterior-character action, `docs/ADMISSIBILITY_DIRAC_KAHLER_EXTERIOR_CHARACTER_ACTION_TRANSFER_BOUNDED_THEOREM_NOTE_2026-08-28.md:57-102`, `:145-184`, `:286-370`, `:388-468` | ordered force and gauge transfer; matter/source extension open | supplies `Q,f_n,G_e`, group support, and gauge projector boundary | yes |
| minimal axioms, `docs/MINIMAL_AXIOMS_2026-06-29.md:114-130`, `:173-190`, `:205-213` | no matter carrier, source/action, measure, or dynamics | premise boundary only | yes |

The other surfaces below are non-linking prior art and carry no premise or
grade authority.

### N5 — rhetoric and resolution audit

`T/H` means tested here and holds; `U/N` means untested and no claim.

| Negative phrase | per-element | per-site | per-mode | per-block | lattice-wide |
|---|---|---|---|---|---|
| independent matter factor does not give the shared link current | `T/H`: derivative is zero if `R` is absent | `T/H`: one exact oriented link | `T/H`: vector versus trivial representation | `U/N`: no census of all matter actions | `U/N`: no global matter no-go |
| negative hopping does not give RP | `T/H`: entries `1,2` exact | `T/H`: two matter histories | `T/H`: negative sign has determinant `-3` | `U/N`: projection may remove modes on degenerate quotients | `U/N`: no thermodynamic sign theorem |
| zero hopping is not matter-injective | `T/H`: constant kernel | `T/H`: nontrivial compact ball | `T/H`: rank-one zero mode | `T/H`: a tensor product inherits the matter null | `U/N`: no infinite-volume gap claim |
| unmatched source is not reflection positive | `T/H`: asymmetric entries | `T/H`: two source histories | `T/H`: quadratic form `3-i` | `U/N`: no classification of all source profiles | `U/N`: no continuum source theorem |
| the action does not select the determinant sector | `T/H`: proper/improper `Q=16` collision | `T/H`: hopping vanishes on `e_3` | `T/H`: local and noncontractible witnesses | `T/H`: periodic flat seam survives | `U/N`: no classification of all topologies |
| coframe/source derivatives are not physical stress or gravity | `T/H`: exact rational derivatives | `T/H`: one supplied site/link/plaquette | `T/H`: proper and improper modes | `U/N`: no Ward/conservation theorem | `U/N`: no Einstein/Lorentz claim |

The runner classifies all five resolutions: it executes the per-element,
per-site, and per-mode controls and explicitly records the per-block and
lattice-wide entries as checked but not executed.
No bounded falsifier is broadened into a universal matter, action, source, or
gravity no-go.

### N6 — partial closure and primitive scan

| Path scanned | Exact result | Disposition |
|---|---|---|
| convention/reframe | simultaneous internal `O(3)` changes preserve (5)–(7); independent coordinate changes of the metric weights are not licensed | internal covariance kept; local-coordinate covariance open |
| interpretation/meta/vocabulary | `docs/repo/CONTROLLED_VOCABULARY.md` provides no rule identifying the vector with physical matter or (12) with stress | no labeling closure or vocabulary edit |
| approved premise registry | `docs/audit/data/axiom_premise_nodes.json` contains no matter action, measure, source, or OS seam supplier | no axiom/primitive/registry edit |
| current-main local action class | `docs/DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md:27-31,59-97,146-171` supplies a Wilson/hopping/mass form class but leaves coefficients, nontriviality, and physical action open | closest form precedent; no source/coframe/shared-transfer theorem imported |
| current-main coupled OS precedents | `docs/RP_COUPLED_MULTISLICE_HALFSPACE_GAUGE_STAGGERED_OS_GRAM_NARROW_THEOREM_NOTE_2026-07-11.md:11-28,55-97,155-183,323-335` and `docs/COUPLED_PERIODIC_TWO_SEAM_SU3_WILSON_STAGGERED_REFLECTED_GRAM_BOUNDED_THEOREM_NOTE_2026-07-12.md:9-47,51-99,143-180,350-440` prove supplied `SU(3)` staggered-fermion Grams | distinct carrier/measure; no claim of first gauge-matter RP theorem |
| transfer precedents | `docs/MESON_GAUGE_INVARIANT_OS_TRANSFER_REPRESENTATION_BOUNDED_NOTE_2026-05-30.md:16-71,83-108,142-178` and `docs/INTERACTING_TRANSFER_MATTER_GAP_AND_GAUGE_REDUCTION_BOUNDED_NOTE_2026-05-30.md:13-46,55-110,117-144` leave full coupled transfer/gap conditional | method comparison only |
| in-flight first-order matter/geometry action | branch-local `docs/ADMISSIBILITY_INCIDENCE_SCALAR_GRAPH_MATTER_FIRST_ORDER_TOTAL_WARD_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md:28-60` has an unretained Lorentzian scalar candidate and no joint compact `O(3)` OS theorem | non-authoritative branch-local near hit |
| external theorem | no precise literature theorem is needed for finite derivatives, tensor Grams, or compact polynomial density | no literature imported |

The explicit finite route closes conditionally.  Carrier/action selection,
physical source/stress, local coordinates, spectral gap, and continuum routes
remain open.

### N7 — steelman

A physical matter law could use fermions, another compact representation, a
heat-kernel gauge action, local tetrads, a metric-dependent measure, or a
Record-derived source.  It could be reflection positive by a mechanism not
present in (22), select `SO(3)` through matter representation data, or have a
continuum limit even if this finite model does not.  Conversely, a physical
theory could keep the metric external and require no dynamic metric transfer.
These live possibilities defeat any broad matter/action/gravity no-go, so none
is claimed.

### N8 — cross-cycle echo

| Earlier surface | Pinned status | Retirement/mechanism | Applicability |
|---|---|---|---|
| `docs/DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md:27-31,59-97,146-171` | `bounded_theorem`, audit/effective `unaudited` | not retired; supplied Wilson, hopping, mass form class leaves coefficients/action open | closest current-main action-form echo; no metric/source transfer theorem |
| `docs/MATTER_GAUGE_MINIMAL_COUPLING_FIBER_FRAME_FORCES_CONNECTION_NARROW_THEOREM_NOTE_2026-06-08.md:14-24,93-152,168-205` | `bounded_theorem`, audit/effective `unaudited` | not retired; transporter covariance is kinematic and gauge dynamics stay separate | shared-link covariance precedent only |
| `docs/RP_COUPLED_MULTISLICE_HALFSPACE_GAUGE_STAGGERED_OS_GRAM_NARROW_THEOREM_NOTE_2026-07-11.md:11-28,55-97,155-183,323-335` | `positive_theorem`, audit/effective `unaudited` | not retired; supplied `SU(3)` Wilson/staggered-fermion full-halfspace Gram | blocks a novelty claim for generic gauge-matter RP; carrier and result differ |
| `docs/COUPLED_PERIODIC_TWO_SEAM_SU3_WILSON_STAGGERED_REFLECTED_GRAM_BOUNDED_THEOREM_NOTE_2026-07-12.md:9-47,51-99,143-180,350-440` | `bounded_theorem`, audit/effective `unaudited` | not retired; supplied periodic coupled Gram, explicitly no transfer/Hamiltonian result | method echo only |
| branch-local incidence-scalar note at `08357978...` | source status `unretained`, absent current source, no current audit authority | not retired into authority; one Lorentzian candidate has geometry source and recoil | distinct in-flight near hit; no premise imported |

No echo is used as authority for a stronger statement.

```yaml
no_go_discipline:
  status: PASS
  negative_assertion_classes:
    - derived_no_go_boundary
    - bounded_with_named_walls
  demotion: null
```

## Prior-art sweep, review boundary, and reproduction

The mandatory sweep refreshed the pinned current-source tree and searched both
noun orders for gauge-vector matter actions, covariant hopping, shared-link
currents, coframe/source response, coupled reflection positivity, transfer,
injectivity, and spectral gaps.  It found the current-main Wilson/hopping form
class, kinematic minimal coupling, several `SU(3)` staggered-fermion OS
theorems, and conditional meson/gap transfer results.  A separate in-flight
scan found the branch-local incidence-scalar matter/geometry candidate.  None
has this compact commuting `O(3)` carrier, dynamic metric/scalar seam,
same-action exact current/coframe/source witness, strict matter support, and
determinant/topology/sign/source falsifier packet.  Classification: open after
matched-hit review.  No literature was needed.

Run:

```bash
python3 scripts/admissibility_exterior_character_gauge_vector_matter_source_transfer_2026_08_28.py
python3 scripts/admissibility_exterior_character_gauge_vector_matter_source_transfer_2026_08_28.py --mode independent
python3 scripts/admissibility_exterior_character_gauge_vector_matter_source_transfer_independent_2026_08_28.py
```

The primary runner declares sixteen hostile mutations covering metric weights,
matter current/equation, coframe/source and matter-link reciprocity, orientation, improper and
determinant boundaries, gauge/matter signs, source reflection, zero hopping,
strict support, and physical overread.  Every mutation must exit nonzero with
exactly one intended failure.  Independent audit remains required before any
effective retained-grade status can be assigned.
