# Compact connected response of the two-plaquette SU(2) marginal

Status: proposed_retained

This note bounds the full compact connected two-source/two-boundary response
of the actual seven-edge marginal, including the normalizer subtraction in
the two-plaquette conditional at identity. It composes the existing compact
and regional/chart suppliers with a new exact marginal insertion identity
and a checked generic density-forest theorem. This is a finite two-step
result for the supplied SU(2) family; it is not a physical mass-gap theorem.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "compact connected response of the actual seven-edge marginal and its conditional-normalizer subtraction"
source_of_blocker_text: user_goal
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Specify and prove the compact nonidentity background and conditional geometry class needed for the next exact transition."
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Analytic connected estimates for the supplied finite two-step SU(2) family, above a fixed coupling threshold, at zero sources and identity terminal exterior."
audit_required_before_effective_retained: true
bare_retained_allowed: false
full_existence_established: false
physical_continuum_mass_gap_established: false
```

## Exact law and source class

Fix odd L>=3, kappa>0, m>=3, fine torus side L^2 m, Wilson beta=u and
both normalized kernel strengths kappa u. J is the seven distinct terminal
edges of two elementary plaquettes sharing exactly one edge, and O=E2\J.
At zero sources and V_O=I the hidden probability law is exactly

    rho_J(dU0 dU1)=Q_J(0)^(-1) q_u(U0) K0(U1|U0)
                                  product_(e in O) k1,e(I|U1) dU0 dU1.

Every K0 factor and surviving input-dependent radial normalizer remains.
There is one original fine Wilson action. The entire normalized terminal
kernel disappears on J after integrating its output. The terminal-root
fine forest has arbitrary permitted internal trees and retains all non-tree
fine links and all intermediate links. Its quotient measure is nu_J; the
independent root-fixed gauge orbit is probability Haar at zero source.

Let F,G be real local C2 quotient functions invariant under simultaneous
conjugation, with fixed norm, reader-cardinality and reader-diameter bounds.
For distinct c,d in O and fixed tangent vectors v_c,v_d at identity put

    A_e=kappa u <i v_e dot sigma_Pauli,M1,e>.

All reader sets include complete syntactic retained-coordinate supports.
Let tau_4 be the least number of periodic axial nearest-neighbor cell edges
in a connected graph meeting S_F,S_G,S_c,S_d. Empty-support constants have
zero cumulants and are treated separately. Global conjugation invariance
of an original source does not by itself make it a quotient function.

## Full compact response and connected expansion

There are u_0,C<infinity and mu>0, depending only on L,kappa and the fixed
source class, such that for all finite volumes and u>=u_0,

    |kappa4_(nu_J)(F,G,A_c,A_d)|
       <= C |v_c||v_d| u^-1 exp(-mu tau_4).                    (1)

For unit tangent vectors and every 0<=eta<mu,

    sum_(c,d in O,c!=d) exp(eta tau_4)|kappa4_(nu_J)(F,G,A_c,A_d)|
       <=C_eta u^-1 exp[-b_eta d_1(S_F,S_G)].                   (2)

The constants are uniform in pair placement/orientation and allowed trees.
They are existence constants; no useful numerical onset u_0 is claimed.
These statements concern the full compact law, not a chart-conditioned law.

The [complete composition proof](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/marginal-connected-density-expansion.md)
also supplies the stronger intermediate bookkeeping result. With
p=log(2+u)^A, A>5/2, and normalized bounded insertions X_i/ell_i on a fixed
complex source polydisc, the compact/chart log ratio has an absolutely
convergent connected expansion with a fixed spatial weight beta_f>0
(distinct from the Wilson beta=u)

    log(Z_compact/Z_chart)=sum_Y Psi_Y,
    sup_x sum_(Y contains x) exp(beta_f |Y|/2) sup|Psi_Y|
                                             <=C exp(-c p^2). (3)

Every term contains a compact insertion, and every differentiated source
brings its entire reader set into Y. This gives a compact/chart fourth-
cumulant difference bounded by
C ell_F ell_G kappa^2 u^2 |v_c||v_d| exp(-c p^2) exp(-beta_f tau_4/2).
For this correction F,G may be bounded measurable quotient functions.
The C2 singlet assumptions are needed for the chart u^-1 gain in (1).

The [source-marked compact proof](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/marginal-source-marked-compact-decomposition.md)
rebuilds first-successful shells with c_J and actual surviving factor counts.
Whole source factors remain inside both regional numerator and denominator;
the latter is not frozen at zero sources. A common phase wedge justifies
division and analytic source differentiation. Simultaneous resummation
removes all selected dummy regions from every good annulus.

The [actual frozen Gaussian proof](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/marginal-frozen-gaussian-producers.md)
uses the complete normalized marginal Hessian, without translation symmetry.
It retains the Gaussian determinant and all physical prefactors, chooses
symmetric covariance paths and activates whole owner cells. The composition
then bounds the compact activity count and verifies every hypothesis of the
existing [density-forest theorem](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/zero-shift-marked-density-forest.md).
Normalized Gaussian density derivatives allow nonsmooth insertions. The
source-dependent chart law remains; only identically indexed no-compact
terms cancel in the ratio. The actual marginal chart covariance, local
moments, and both 1|3 and 2|2 cumulant cancellations complete (1).

## Original sources and the conditional density

For original local C2 singlet sources F(a,h),G(a,h), retain the joint orbit
factor E_h exp(sF+tG). With f=E_h F, g=E_h G and
C_FG=E_h(FG)-fg, the exact identity is

    kappa4_(rho_J)(F,G,A_c,A_d)
      =kappa4_(nu_J)(f,g,A_c,A_d)+kappa3_(nu_J)(C_FG,A_c,A_d). (4)

The second term has an O(1) tree bound, not an asserted O(u^-1) bound.
It vanishes when the source orbit-reader sets H_F,H_G are disjoint, or
either source is orbit invariant. Otherwise include endpoint owner cells
in bounded source regions T_F,T_G. The resulting full bound is

    C |v_c||v_d|[u^-1+1_(H_F intersects H_G)]
                              exp[-mu' tau_4(T_F,T_G,S_c,S_d)], (5)

with the corresponding weighted boundary-pair sum. No conditional orbit
covariance or source-only normalization is removed by separate projection.

For the actual conditional density p_J=N_V/Q_J of the seven terminal links,
the exact distinct-link identity at V=I,s=t=0 is

    D_c D_d partial_s partial_t log p_J
      =kappa4_(pi_I)(F,G,A_c,A_d)
                 -1_(c,d in O) kappa4_(rho_J)(F,G,A_c,A_d).    (6)

Restoring the seven positive leading kernel energies preserves c_J. The
composition proof repeats the same finite-template match for that fully
pinned companion, explicitly covering arbitrary permitted internal trees.
Combining its bound with (1) bounds (6) by the same C/u tree form for
quotient singlets, uniformly for all distinct
terminal c,d. Original sources obey (5), and weighted pair sums follow.
For c,d both in O the second term is controlled, not dropped. If either
is in J it is zero because Q_J is independent of that terminal output.
The exact partial-terminal derivation retains all 15 total-cumulance terms;
the direct marginal argument bounds their combined value without assuming
that thirteen of them vanish.

## Evidence and remaining boundary

The dependency closure is included in this same PR; no provisional result
below is represented as an audit-ratified authority.

| Obligation | Included source and status |
|---|---|
| Exact quotient, original orbit factor and conditional normalization | [Forest exchange](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/compact-forest-exchange.md) and [partial-terminal identities](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/partial-terminal-normalization.md), previously checked at unchanged bytes. |
| Seven-edge compact c_J and normalized precision | [Compact marginal theorem](SU2_TWO_PLAQUETTE_MARGINAL_COERCIVITY_BOUNDED_THEOREM_NOTE_2026-11-09.md), previously checked supplied lemmas. |
| Whole-factor regional bounds and actual cube covariance | [Regional/chart theorem](SU2_MARGINAL_REGIONAL_AND_CHART_ESTIMATES_BOUNDED_THEOREM_NOTE_2026-11-09.md), previously checked supplied lemmas, with their stated domains. |
| Exact source-marked compact representation | New compact proof linked above, proved for this marginal. |
| Actual frozen Gaussian and whole-cell base budget | New Gaussian proof linked above, proved for this marginal. |
| Normalized-density forest and scalar combinatorics | Generic forest linked above and [scalar-leg count](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/scalar-leg-forest-count.md), previously checked; all actual-law hypotheses matched in the new composition. |
| Compact primitive budget, connected response and conditional subtraction | New composition linked above, including the restored-kernel arbitrary-tree companion; independent check recorded below. |

The [Luna repo and primary-literature check](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/sources/marginal-connected-expansion-prior-art-20261109.md)
preceded the new proofs. It identifies the closest repo methods and the
unmatched hypotheses in the published Gaussian/cluster comparators. Exact
source identities, approach advice and mathematical check coverage are
indexed in the working pack's
[review history](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/REVIEW_HISTORY.md).
Research checks do not confer formal retained status; independent audit
remains required. Earlier notes' open-next-step statements are historical
milestones; this note supplies the stated identity-exterior continuation.

The next obligation is compact control of the nonidentity backgrounds and
larger conditional geometries actually needed by another exact transition,
with all inherited normalizers and readers retained. Repeated-link jets,
arbitrary deletion geometry, closure under repeated blocking, physical-scale
cutoff control, continuum construction and a physical spectral gap remain
open. Neither the pinned Hessian nor the decay exponent above is identified
with a Yang-Mills mass. The same PR contains the full current proof tree.
