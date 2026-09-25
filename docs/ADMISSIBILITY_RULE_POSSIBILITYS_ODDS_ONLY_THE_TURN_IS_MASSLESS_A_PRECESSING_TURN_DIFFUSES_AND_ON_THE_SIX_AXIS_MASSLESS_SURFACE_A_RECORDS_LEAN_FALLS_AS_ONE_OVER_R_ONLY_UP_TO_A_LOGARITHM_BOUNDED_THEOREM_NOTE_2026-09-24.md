---
claim_id: admissibility_rule_possibilitys_odds_only_the_turn_is_massless_a_precessing_turn_diffuses_and_on_the_six_axis_massless_surface_a_records_lean_falls_as_one_over_r_only_up_to_a_logarithm_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: Conditional nonzero-azimuth spectral comparison for an existing smooth monotone leaning fixed point;
  Gaussian ansatz identities without a large-beta limit theorem; exact spectra of separately supplied linear turn
  equations; formal six-axis cubic coefficients; conditional radial centre-branch logarithm for u>0. No order-zero
  gap, global ordered branch, nonlinear-precession derivation or lattice far-field theorem.
upstream_dependencies:
- admissibility_rule_interaction_through_the_odds_of_unformed_sites_field_equation_massless_surface_content_charge_no_first_order_mass_channel_at_neutral_scale_bounded_theorem_note_2026-09-20
- admissibility_rule_possibilitys_odds_carry_content_not_record_count_at_long_range_a_massless_turn_channel_in_the_ordered_sea_bounded_theorem_note_2026-09-23
- minimal_axioms
runner: scripts/admissibility_rule_possibilitys_odds_only_the_turn_is_massless_a_precessing_turn_diffuses_a_records_lean_runs_logarithmically_2026_09_24.py
---

# Supplied odds models: conditional turn spectrum, cubic coefficients and radial logarithm

**Type:** bounded_theorem
**Status:** bounded-support; supplied mathematical models, unaudited.

This note studies supplied odds maps, a separately supplied linear turn dynamics, and a formal scalar gradient approximation. It does not establish a nonlinear lattice far field, a global ordered branch or a physical dynamics; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Premises and declared objects

Use the current sphere parent: beta>0, uniform probability measure sigma on S^2, Kf(s)=integral exp(beta s.b)f(b)d sigma(b)/Z, Z=sinh(beta)/beta. Supply an existing smooth positive nonconstant fixed point F(t)=(KF)^6/<(KF)^6>, t=s.n, with F non-decreasing. Existence for every beta above the uniform linear threshold is not proved by that parent and is not claimed here. Put g=KF and A eta=K(F eta)/g. The density and relative-density operators are similar by multiplication by F. The rotational tangent has eigenvalue1/6.

For the six-axis map supply positive p,q,r, T=p+q+4r, l1=(p-q)/T, l2=(p+q-2r)/T. Axial probability laws are pi(s)=[1+3v s1+D(3s1^2-1)]/6. Use the normalized product of the six neighbor factors. Expansions below assign v order t and D order t^2; denominators are nonzero near the uniform law. Slaving additionally requires l1!=0 and 1-6l2!=0.

Mathematical imports: compact positive-kernel simplicity and strict spectral dominance (Jentzsch); the modified Bessel order inequality I_m(x)<I_1(x) for integer m>=2,x>0 (Soni); Gaussian integration and Hermite polynomial identities. The radial asymptotic is conditional on the stated smooth invariant centre branch; its existence is a centre-manifold theorem import, not a conclusion of a finite polynomial check.

## Theorem T1 — conditional nonzero-azimuth comparison and a separate Gaussian ansatz

For an existing F as above, the azimuthal kernels are proportional to exp(beta t t') I_m(beta sqrt(1-t^2)sqrt(1-t'^2)) times the positive F/g factors. In order one, the rotational tangent is nonnegative and nonzero. Positivity of the interior kernel and the eigen-equation make its interior profile strictly positive. Compact positive-kernel simplicity identifies eigenvalue1/6 as the simple spectral radius; all other order-one eigenvalues have smaller modulus. For each fixed integer |m|>=2 the positive kernel is strictly smaller in the interior, so the strict comparison theorem gives spectral radius below1/6. Endpoint zeros have measure zero; equivalently factor out the known endpoint profile in the weighted space. These conclusions use the stated compactness/positivity imports, not just the runner's three sample comparisons. They do not address m=0 or a gap uniform in beta and all m.

Separately, inserting a tangent-plane Gaussian ansatz exp(-a|x|^2) into the Gaussian neighbor model gives curvature a beta/(2a+beta). The nonzero fixed point after the sixth power is a=5beta/2. Its conditional Gaussian chain has mean x/6, variance1/(6beta) and polynomial eigenvalues6^-n. The algebraic masses for n=1,2,3 are0,30,210. This is an exact Gaussian-model calculation, not proof that the original sphere fixed points or spectra approach it as beta grows. No executed order-zero sphere-spectrum evidence is supplied by this runner.

## Theorem T2 — a supplied linear dynamics

Supply the ordered turn equation tau_dot=-(Gamma I+Omega J)(tau-neighbor_mean), J=[[0,-1],[1,0]], Gamma>=0, Omega real. With gamma(k)=sum cos(kj)/3 and E(k)=6(1-gamma), its frequencies under exp(-i omega t) are (+/-Omega-i Gamma)E/6. For Gamma>0 these are damped quadratic long-wave modes; at Gamma=0 they are undamped quadratic modes, not diffusion.

Supply also the two-sublattice circular-sector matrix [[-(Gamma+iOmega),(Gamma+iOmega)gamma],[(Gamma-iOmega)gamma,-(Gamma-iOmega)]]. Its characteristic polynomial is lambda^2+2Gamma lambda+(Gamma^2+Omega^2)(1-gamma^2). At Gamma=0 its frequencies are +/-Omega sqrt(1-gamma^2), with magnitude |Omega||k|/sqrt3 at leading small k. For fixed Gamma>0 the slow root is -(Gamma^2+Omega^2)(1-gamma^2)/(2Gamma)+higher orders. Omega=0 is degenerate.

These two matrices are supplied tangent models. The original nonlinear precession about the raw lean of Phi is not derived here: its magnitude and tangent projection must be included before identifying Omega with a bare nonlinear coefficient. No existence of an alternating nonlinear fixed point for every negative beta follows from the matrix calculation.

## Theorem T3 — exact local expansion and formal scalar approximation

Write S1=sum v_y. Direct expansion of the normalized product gives

    v' = l1 S1 + 3 l1^3(sum v_y^3 - S1 sum v_y^2)
         - 2 l1 l2(sum v_y D_y - S1 sum D_y) + O(t^5),
    D' = l2 sum D_y + (3/2)l1^2(S1^2-sum v_y^2) + O(t^4).

One general proof uses uniform six-axis moments: <s1>=0, <s1^2>=<s1^4>=1/3, <Q>=0, <s1^2 Q>=2/3 for Q=3s1^2-1. Expand product_y(1+3l1 v_y s1+l2 D_y Q) and divide its first and quadrupole moments by its zeroth moment. The elementary identities for sums over distinct pairs and triples give the displayed coefficients for arbitrary six neighbor values; the runner additionally checks six exact fixtures.

Ignoring higher gradients and higher amplitudes in a separately assumed slow-field approximation gives D=45 l1^2 v^2/(1-6l2). The formal equation is -Delta v+m^2 v+u v^3=source, with m^2=(1-6l1)/l1 and u=90 l1^2(1-36l2)/(1-6l2). Mixed nonlinear gradients and the approximation error are not bounded here. On5p=7q+4r, l1=1/6 and, for r!=q, u=(5/2)(4r-7q)/(r-q), equal to5/2 at(3,1,2). For r>q, u>0 exactly when4r>7q. At r=q the slaving denominator vanishes. The effective radial result below requires u>0, not every point of the massless surface.

## Theorem T4 — conditional nonzero centre-branch asymptotic

In the separately supplied three-dimensional continuum scalar equation -Delta v+u v^3=0 away from a source, put v=A(r)/r and tau=log r. Then A_tau_tau-A_tau=u A^3. Let u>0 and restrict to a nonzero branch tending to zero on a smooth local invariant graph A_tau=h(A), whose existence is the explicit centre-manifold import. Its invariance equation h'h-h=u A^3 gives

    h(A)=-u A^3+3u^2 A^5-24u^3 A^7+O(A^9).

For B=A^-2 this yields B'=2u-6u^2/B+O(B^-2). First B/tau tends to2u; integration then gives B=2u tau+O(log tau). Substituting this bound back shows the derivative of B-2u tau+3u log tau is O(log tau/tau^2), integrable at infinity. Thus B=2u tau-3u log tau+C+o(1). This argument excludes the zero solution, requires u>0 and concerns the selected continuum centre branch. It is not an existence or matching theorem for a held-record source on the lattice. The scale exp(1/(2u A0^2)) is a leading-balance estimate, not a proved crossover radius.

## No-Go Discipline Gate

### N1 — Exceptions
No order-zero gap, all-beta ordered branch, Gaussian limit, lattice far field or dynamics selection is established. The half-power logarithm requires the stated nonzero radial branch and u>0.
### N2 — Wall independence
No repository no-go wall is used.
### N3 — Supplied assumptions
The fixed point, positive kernel imports, linear dynamics, gradient approximation and centre-branch import are explicit.
### N4 — Dependencies
Only the current two parent scopes and the minimal axioms are used. Historical probe verdicts confer no authority.
### N5 — Resolution
Exact finite checks cover kernel series and three comparison points, Gaussian polynomial modes through degree3, two supplied matrices, six local expansion fixtures and radial coefficients through degree8. General statements require the arguments and imports above. No order-zero sphere scan was executed here.
### N6 — Primitive boundary
No primitive or physical dynamics is adopted.
### N7 — Strongest objection
Finite coefficients do not prove an original nonlinear sphere limit or a nonlinear lattice response. Those conclusions remain deferred.
### N8 — Historical scope
The original PR preserves all stronger prose, campaign claims and auxiliary provenance. The present scoped statements control.

## Falsifiers

A coefficient failure in the stated local product model, a failure of either supplied matrix characteristic polynomial, or a nonzero radial centre branch violating the displayed asymptotic under its hypotheses refutes the corresponding result.

## Review record — historical author provenance

Original PR9156 harvests three author-reported probes attempts and referees. These reports are historical provenance, not fresh independent evidence. Original materials remain preserved; no audit verdict is applied.

## Imports and canonical dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [admissibility_rule_possibilitys_odds_carry_content_not_record_count_at_long_range_a_massless_turn_channel_in_the_ordered_sea_bounded_theorem_note_2026-09-23](ADMISSIBILITY_RULE_POSSIBILITYS_ODDS_CARRY_CONTENT_NOT_RECORD_COUNT_AT_LONG_RANGE_A_MASSLESS_TURN_CHANNEL_IN_THE_ORDERED_SEA_BOUNDED_THEOREM_NOTE_2026-09-23.md): current supplied parent only.
- [admissibility_rule_interaction_through_the_odds_of_unformed_sites_field_equation_massless_surface_content_charge_no_first_order_mass_channel_at_neutral_scale_bounded_theorem_note_2026-09-20](ADMISSIBILITY_RULE_INTERACTION_THROUGH_THE_ODDS_OF_UNFORMED_SITES_FIELD_EQUATION_MASSLESS_SURFACE_CONTENT_CHARGE_NO_FIRST_ORDER_MASS_CHANNEL_AT_NEUTRAL_SCALE_BOUNDED_THEOREM_NOTE_2026-09-20.md): current supplied parent only.

## Verification

Run `python3 scripts/admissibility_rule_possibilitys_odds_only_the_turn_is_massless_a_precessing_turn_diffuses_a_records_lean_runs_logarithmically_2026_09_24.py`. Expected TOTAL: PASS=12 FAIL=0. Metadata checks are distinct from mathematical families.
