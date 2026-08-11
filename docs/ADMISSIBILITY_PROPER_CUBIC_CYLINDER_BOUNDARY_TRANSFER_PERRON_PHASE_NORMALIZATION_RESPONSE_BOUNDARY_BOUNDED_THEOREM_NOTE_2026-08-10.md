---
claim_id: admissibility_proper_cubic_cylinder_boundary_transfer_perron_phase_normalization_response_boundary_bounded_theorem_note_2026-08-10
claim_type: bounded_theorem
claim_scope: "On the finite-width quotient C3 x C3 x Z of the proper-cubic lattice, two supplied positive occupancy-mediated sixteen-Record-state nearest-neighbour factor laws reduce exactly from 16^9 full label states to 512 occupancy states per transverse slice. Each positive integer slice transfer has a unique normalized left/right Perron boundary pair. Those messages define normalized laws on every finite longitudinal interval, with exact endpoint-deletion projectivity and compatible overlap marginals by the Perron eigenvector identities. The stationary occupancy law lifts to fifteen positive actual-edge source expectations and positive semidefinite Euclidean metric stress. The two supplied transfers have distinct fixed points and stationary laws. Multiplying either whole-sector transfer by an arbitrary positive scalar leaves its boundary messages, Doob transition, stationary law, and every normalized interval law unchanged while rescaling its Perron eigenvalue; independent positive sector multipliers likewise change geometry odds without changing either conditional cylinder family. Both the inherited compact metric-reaction branch and a distinct full-rank metric-response control solve the Perron-selected stationary sources. Thus a unique boundary fixed point closes finite-width overlap gluing conditional on a supplied transfer but does not select the extensional rule, absolute cross-sector normalization, geometry-phase odds, curvature coefficient, or response branch. This is a finite-width transfer/gluing and normalization-response boundary theorem, not a full-Z3 thermodynamic-limit or Gibbs-phase theorem, physical law selector, complete stationary Ward theorem, Lorentzian dynamics theorem, axiom necessity result, or axiom adoption."
upstream_dependencies:
  - minimal_axioms
  - admissibility_interacting_record_spatial_gluing_phase_response_selection_boundary_bounded_theorem_note_2026-08-10
runner: scripts/admissibility_proper_cubic_cylinder_boundary_transfer_perron_phase_normalization_response_boundary_2026_08_10.py
---

# Proper-Cubic Cylinder Boundary Transfer / Perron Phase-Normalization Boundary

**Date:** 2026-08-10
**Type:** `bounded_theorem`
**Role:** exact finite-width proper-cubic quotient gluing, unique positive
Perron boundary messages, arbitrary-interval overlap projectivity,
sixteen-state actual-edge source lift, absolute normalization gauge,
geometry-prior nonselection, response-branch discrimination, and narrowed
law/axiom delta
**Scope:** the quotient `C3 x C3 x Z`, nine sites and 512 occupancy states per
transverse slice, one null plus fifteen actual-edge Record labels per site,
two positive integer factor laws, interval lengths zero through eight as
numerical controls for an analytic all-length identity, all 24 proper cubic
rotations at factor level, all 24 four-axis Record-label relabellings, five
inherited curvature coefficients, three source units, and three supplied
metric-response stiffnesses.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.

**Primary runner:**
[admissibility_proper_cubic_cylinder_boundary_transfer_perron_phase_normalization_response_boundary_2026_08_10.py](../scripts/admissibility_proper_cubic_cylinder_boundary_transfer_perron_phase_normalization_response_boundary_2026_08_10.py)

## Result Up Front

Block 32 supplied a genuine interacting four-site parent and proved that
marginal projectivity is not the same thing as deletion-stable local factors.
It left a boundary-message transfer fixed point as the next constructive
target. This block supplies such a fixed point on a finite-width quotient of
the cubic lattice and then asks what it actually selects.

Let the transverse slice be `C3 x C3`. Retaining the edge incidences inherited
from `Z^3`, each slice site has four transverse neighbours and two longitudinal
neighbours. The global cylinder is not the full lattice, but its local factor
uses all six nearest-neighbour incidences and is invariant under the proper
cubic permutation of those directions.

Each site has states

    s in {0,...,15},                                      (1)

where zero is null and one through fifteen are the actual-edge labels from
Block 31. Define occupancy

    o(s) = 0 if s=0, and 1 otherwise.                    (2)

For sector `g`, the local weights `a_g(s)` are the positive integer class
weights used in Block 32, and every nearest-neighbour pair contributes

    rho_g^[o(s_i)=o(s_j)],       rho_0=2, rho_1=3.        (3)

This is a genuine six-neighbour interaction. The conditional weight of a
candidate state is

    a_g(s) rho_g^N_i(o(s)),                              (4)

where `N_i` counts the six neighbour occupancies matching the candidate.
Adjacent occupancy cross-ratios are four and nine.

Because the interaction depends only on occupancy, summing the fifteen actual
labels is exact. The two aggregate local-weight pairs are

    A_0 = (5,62),             A_1 = (7,77).              (5)

A transverse slice therefore reduces from `16^9 = 68,719,476,736` full label
states to `2^9 = 512` occupancy states without discarding the conditional
actual-edge label distribution.

For slice occupancies `x,y`, let `M_perp(y)` count matched transverse edge
occupancies and `M_z(x,y)` count matched longitudinal occupancies. Define

    q_g(y) = prod_i A_g(y_i) rho_g^M_perp(y),             (6)

    K_g(x,y) = q_g(y) rho_g^M_z(x,y).                    (7)

Every entry of `K_g` is a positive integer. Hence the normalized positive
transfer map has unique right and left Perron boundary messages,

    K_g r_g = lambda_g r_g,
    l_g^T K_g = lambda_g l_g^T.                           (8)

They define the interval law

    mu_g^L(x_0,...,x_L)
      = l_g(x_0) [prod_(t=0)^(L-1) K_g(x_t,x_(t+1))]
        r_g(x_L) / [lambda_g^L <l_g,r_g>].               (9)

Equation (8) makes (9) normalized and exactly projective under deletion of
either endpoint. Every pair of overlapping longitudinal intervals therefore
has the same marginal on the overlap. This is the boundary-message gluing
object that Block 32 lacked.

The decisive result is what this fixed point does **not** select. For any
positive scalar `c_g`, replacing

    K_g -> c_g K_g,       lambda_g -> c_g lambda_g        (10)

leaves both messages, the normalized interval family, its stationary slice
law, and its Doob transition unchanged. The raw eigenvalue changes. Therefore
an eigenvalue comparison cannot supply physical geometry odds until absolute
cross-sector normalization and its action unit are fixed independently.

Likewise, arbitrary positive weights on the two already-normalized cylinder
families change the geometry odds from one to seven without changing either
conditional family. Unique within-sector gluing is not cross-sector phase
selection.

The stationary occupancy law lifts to fifteen positive actual-edge source
expectations. Their Euclidean metric stresses remain positive semidefinite.
Both the inherited compact rank-25 reaction system and a distinct rank-15
metric-response control solve those now-fixed stationary sources. Boundary
gluing therefore does not choose the physical gravity response either.

This closes a real part of the gravity path: on the supplied positive
finite-width transfer, no arbitrary iterative boundary choice remains. It
also moves the missing object one level upstream. The remaining law must be an
absolutely normalized geometry-bearing specification on the full `Z^3`
lattice, with its phase and response derived from the same action and followed
by the complete stationary Ward connection and Lorentzian update.

This is **not a full `Z^3` phase theorem**. No canonical axiom is edited. Fixed
TOE percentages remain unchanged.

## Inputs And Non-Imports

| Input | Used here | Not imported |
|---|---|---|
| [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) | cubic nearest-neighbour carrier, proper cubic rotations, one fixed varying local distribution rule, and permanent Records | no extensional probability values, transfer operator, boundary condition, action unit, geometry odds, response law, or dynamics |
| [Block 32 interacting gluing boundary](ADMISSIBILITY_INTERACTING_RECORD_SPATIAL_GLUING_PHASE_RESPONSE_SELECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md) | actual-edge labels, positive sector weights, interaction controls, source/stress compiler, compact reaction, metric-response control, and the induced-boundary-message target | no full-lattice transfer, absolute sector normalization, phase selector, complete Ward connection, or Lorentzian update |

## 1. Finite-Width Proper-Cubic Quotient

Quotient `Z^3` by translations of three sites in the first two axes and leave
the third axis infinite. A transverse slice is the simple torus `C3 x C3`:
nine sites, eighteen distinct transverse edges, and degree four at every
slice site. The previous and next longitudinal sites restore degree six.

The quotient singles out the longitudinal axis globally. Consequently the
result is finite-width proper-cubic quotient support, not a theorem on the
full cubic lattice. At the local-factor level, every one of the six edge
incidences uses the same equality factor. Proper cubic rotations merely
permute those incidences, so the local rule is covariant under all 24 proper
cubic rotations.

The actual-edge label weights depend only on their four-axis Hamming class.
They commute with all 24 permutations of the four label axes. Spatial
covariance and internal label covariance are checked separately; neither is
used to identify the label with physical matter without the inherited
conditional bridge.

## 2. Exact Sixteen-State Occupancy Lift

For fixed neighbour occupancies, all fifteen actual candidates acquire the
same interaction power. Summing their conditional numerators gives

    [sum_(e=1)^15 a_g(e)] rho_g^N_i(1),                  (11)

while the null numerator is

    a_g(0) rho_g^N_i(0).                                 (12)

The sums in (5) follow exactly from the supplied integer weights. Conversely,
conditional on occupancy one, the actual label distribution is

    P_g(e | o=1) = a_g(e) / sum_(f=1)^15 a_g(f).         (13)

Thus the 512-state transfer is not a replacement ontology. It is the exact
occupancy marginal of the positive sixteen-state factor law, and (13) lifts
it back to every actual-edge label.

The interaction is occupancy-mediated rather than full-label equality as in
Block 32. This alternate positive law is intentional: it keeps the full source
carrier while making a nontrivial nine-site transverse fixed point exactly
computable. It is supplied law content, not an axiom consequence.

## 3. Perron Boundary Fixed Point

Normalize the positive cone by total mass. The map

    F(r) = K_g r / ||K_g r||_1                           (14)

is continuous and maps the closed simplex into its strict interior. A fixed
point exists. Strict positivity makes it unique. If positive eigenvectors
`r,s` were not proportional, set `a=min_i r_i/s_i` and
`b=max_i r_i/s_i`. For every row, the ratio
`(K_g r)_i/(K_g s)_i` is a strict positive-weight average of the component
ratios and lies strictly between `a` and `b`. At an index attaining `a`, the
two eigenvalue equations would require `lambda_r/lambda_s>1`; at an index
attaining `b`, they would require the same ratio to be less than one. This is
impossible. The same argument applies to the transpose and the left message.

This is the finite positive-matrix Perron argument specialized to the exact
transfer (7). The transfer entries are integer-defined; the messages and
eigenvalues are generally algebraic rather than rational. The runner computes
them in double precision, verifies normalized residuals below the stated
tolerances, and obtains the same right message from uniform, delta, and ramp
initializations.

The executed eigenvalues are approximately

    lambda_0 = 1.83786726555e24,
    lambda_1 = 7.26405737255e29.                          (15)

Their absolute values have no physical cross-sector meaning here because of
the normalization gauge (10).

## 4. Exact Interval Normalization And Overlap

Summing (9) over every slice gives

    <l_g, K_g^L r_g> / [lambda_g^L <l_g,r_g>] = 1.       (16)

Deleting the left endpoint replaces `l_g^T K_g` by `lambda_g l_g^T`.
Deleting the right endpoint replaces `K_g r_g` by `lambda_g r_g`. In either
case the factor of `lambda_g` cancels and leaves the shorter member of the
same family.

Every overlap of two longitudinal intervals is obtained by repeated endpoint
deletion, so the overlap marginal is independent of which larger interval was
used. This is exact projectivity for every finite longitudinal interval,
conditional on the fixed transverse width and supplied transfer.

Equivalently, define

    P_g(y|x) = K_g(x,y) r_g(y) / [lambda_g r_g(x)],       (17)

    pi_g(x) proportional to l_g(x) r_g(x).               (18)

Then (17) is stochastic and (18) is stationary. The runner verifies row and
stationarity residuals directly for both 512-state sectors.

## 5. Absolute Normalization Gauge And Phase Odds

Substitution of (10) into (9) cancels `c_g^L` between numerator and
denominator. It also cancels exactly in (17). The left and right eigenvectors
do not change. Thus every within-sector probability is blind to the positive
whole-transfer scale.

The runner uses a scale factor seven and verifies the normalized transition
is unchanged while the relevant eigenvalue ratio changes by exactly seven.
This forbids treating the raw Perron eigenvalue ratio as geometry odds without
first supplying a common physical action normalization.

Even after a normalization convention is chosen separately in each sector,
one may form

    P(g, interval) proportional to d_g mu_g^L(interval)  (19)

for arbitrary positive `d_g`. The conditional interval laws are unchanged,
while `P(g=1)/P(g=0)=d_1/d_0`. The executed odds one and seven are two
explicit completions.

The two walls are distinct:

- `c_g` is a normalization gauge invisible to each normalized transfer law;
- `d_g` is the unselected mixture weight between already-normalized sectors.

A physical geometry action could relate them, but no such relation follows
from positivity or the Perron fixed point alone.

## 6. Stationary Source Lift And Gravity Response

Let `pi_g` fix the expected occupied sites in one transverse slice. Equation
(13) then gives the fifteen expected actual-edge counts

    s_g(e) = E_pi[N_actual] a_g(e) / A_g(1).              (20)

Every component is positive and their sum is the expected occupied-site
count. Pullback through the Block-31 constant-metric map is a positive sum of
rank-one tensors, hence positive semidefinite.

This source is more selected than the arbitrary Block-32 count census: it is
the expectation of one unique stationary boundary law conditional on `K_g`.
Nevertheless it admits both inherited response completions:

1. the rank-25 compact KKT system cancels the metric component by reaction;
2. the rank-15 operator with supplied positive metric stiffness responds along
   the metric directions without that reaction.

Both solve at every executed `alpha`, source-unit, and metric-stiffness
control. Therefore boundary-message uniqueness does not imply gravity-phase
or coefficient selection.

## 7. What Is Closed And What Is Not

Closed on the supplied cylinder:

- a positive neighbour-dependent sixteen-state factor law;
- exact reduction to a tractable occupancy transfer;
- unique normalized Perron boundary messages;
- normalized interval laws at every longitudinal length;
- exact endpoint projectivity and overlap compatibility;
- stationary actual-edge source expectations and positive metric stress.

Not closed:

- selection of the extensional local weights or `rho` from the axiom memo;
- an infinite-transverse or full `Z^3` global specification and phase;
- absolute cross-sector normalization and a physical action unit;
- geometry-sector odds;
- the curvature coefficient or compact-versus-metric response;
- the complete stationary Ward connection;
- a causal Lorentzian update.

The Perron iteration itself is no longer the wall. The missing object is one
absolutely normalized geometry-bearing specification whose full-lattice phase,
source, and response arise from the same action.

## 8. Law And Axiom Boundary

Admissibility asserts that there is one fixed neighbour-dependent rule. The
Perron construction shows how any supplied positive rule of the displayed
form yields a unique finite-width boundary message. It does not recover the
rule's numerical values from the structural axiom wording.

Record permanence can carry the boundary message across an overlap. It does
not set the message before the extensional transfer is known, relate transfer
normalizations across geometry sectors, or provide a geometry update.

A sufficient downstream law interface would supply:

1. one extensional proper-cubic conditional specification on arbitrary finite
   regions or a selected full-lattice global law;
2. one common physical action unit and absolute normalization across geometry
   sectors;
3. geometry dependence whose differentiated transfer produces both the source
   and complete stationary Ward response; and
4. the autonomous Lorentzian Record/geometry update.

If those data cannot be derived from the existing structures, a narrow
Admissibility amendment could register the normalized specification and its
geometry coupling. This block does not establish that such an amendment is
minimal or necessary. All four items can remain downstream law content if
derived. No fifth ontology axiom is proven necessary.

## 9. N1--N8 Status

This note makes bounded nonselection statements, so the no-go discipline is
applied before any negative wording is shipped.

### N1: Alternative-route enumeration

Live routes include a different positive transfer; a nonpositive or
deterministic boundary realization; increasing transverse width; a full
`Z^3` DLR or other global specification; boundary-condition phase selection;
geometry-dependent interaction; an absolute action normalization; curved/open
geometry; boundary flux; nonlinear response; a complete same-action Ward
identity; and a causal Lorentzian update.

### N2: Wall-independence audit

Three walls remain independent. Finite-width versus full-lattice selection is
a thermodynamic/spatial question. Absolute normalization versus mixture odds
is a cross-sector action question. Compact reaction versus metric response is
a geometry-dynamics question. Solving any one does not algebraically solve the
other two.

### N3: Hidden-wall scan

The result depends on the supplied width-three quotient, occupancy coarse
variable, occupancy-mediated equality interaction, integer local weights,
strict positivity, two sectors, inherited actual-edge identification, flat
compact Hessian, curvature-square lift, and linear response controls. None is
hidden as current-axiom content.

### N4: Residual matching

The exact residuals are the extensional transfer values, infinite-transverse
and full-lattice phase, common action unit, absolute cross-sector
normalization, geometry odds, response branch, complete stationary Ward
connection, and Lorentzian nonlinear update.

### N5: Partial-closure scan

Positive content is retained explicitly: genuine six-neighbour interaction,
an exact sixteen-to-two-state occupancy lift, unique Perron boundary messages,
all-length interval normalization, exact endpoint projectivity, compatible
overlaps, stationary source/stress lift, and two complete response controls.

### N6: Steelman

The strongest continuation is a single absolutely normalized
geometry-dependent transfer/action on increasing cubic regions whose selected
full-lattice phase differentiates to the source, contact, multiplier, and
connection terms. That object could remove the scale gauge and select the
response without new ontology.

### N7: Cross-cycle echo

Blocks 26 through 32 repeatedly separated conditional normalization from
physical action units and joint geometry odds. This block closes the boundary
fixed point on a nontrivial cylinder and shows that the same distinction
survives unique overlap gluing.

### N8: Rhetoric audit

Authorized wording is limited to this finite-width positive transfer family
and the named response controls. It is not a full-lattice phase
classification, universal transfer no-go, gravity no-go, axiom-minimality
proof, complete Ward theorem, or dynamical theorem.

**N1--N8 status:** `PASS` for the bounded wording above. All named routes and
walls remain explicit.

## 10. Reproduction

Run:

```bash
python3 scripts/admissibility_proper_cubic_cylinder_boundary_transfer_perron_phase_normalization_response_boundary_2026_08_10.py
```

Expected final line:

```text
TOTAL: PASS=22 FAIL=0
```

The transfer entries and occupancy reduction are integer-defined. The Perron
messages and response solves use double precision with named residual
tolerances. The all-length overlap statement is the exact algebraic
consequence (16) of the verified eigenvector equations, not an extrapolation
from the nine executed interval lengths.

## 11. Exact Next Target

Promote the transfer to an absolutely normalized geometry-bearing
specification on increasing proper-cubic regions. Test whether one selected
full-`Z^3` phase exists and whether differentiating its normalized leading
functional supplies the expected source together with every connected,
contact, mixed/source, multiplier, and generator-connection term in the
complete stationary Ward identity. If the scale gauge persists, isolate the
narrow sufficient law or Admissibility amendment before attempting the
Lorentzian update.
