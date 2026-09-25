---
claim_id: formation_rate_functions_the_axiom_text_admits_record_determined_clocks_reduce_to_the_constant_clock_between_neighbour_records_and_state_reading_clocks_split_by_menu_dephasing_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: Conditional hazard identities, fixed-menu dephasing factorization and finite clock diagnostics. No
  axiom admissibility classification or selected formation rule.
upstream_dependencies:
- minimal_axioms
- record_formation_clock_in_the_clause_the_field_aligned_menu_s_odds_do_not_depend_on_when_records_form_bounded_theorem_note_2026-09-24
runner: scripts/formation_rate_functions_record_determined_clocks_reduce_to_constant_and_state_reading_clocks_split_by_menu_dephasing_2026_09_24.py
---

# Conditional formation clocks: finite windows and a fixed-menu criterion

**Type:** bounded_theorem

## Supplied setting

Supply qubit reconstruction, Born outcome probabilities, selective projector
updates, a menu, a trajectory and a nonnegative measurable conditional hazard
f(t). The survival is S(t)=exp(-integral_0^t f), and formation density
w(t)=f(t)S(t). When 1-S(T)>0, condition on formation before T to obtain
p_T(q)=integral_0^T w(t) Tr(P_q rho(t)) dt / (1-S(T)).
A zero hazard or other zero formation probability has no such conditional law.
The clock's flow parameter and rate units are supplied even for a constant
clock. An axiom not supplying a rate does not prove that every proposed
rate is compatible with every other axiom; no admission classification is
claimed. The classes below are overlapping example constructions.

## Frozen records and covariance

If f=F(R) with R frozen between neighbor-record events, with no other time,
age, history or state arguments, it is constant on each such interval.
A functional of a separately supplied law p(.|R) is a special case. Before
the next neighbor event, conditional survival over elapsed time s is
exp(-f s). This does not make the full lifetime exponential when future
neighbor events change the rate, nor its mean automatically 1/f.

Entropy, support size and inverse maximum probability are invariant under
permuting a distribution's labels. The runner checks a supplied field-law
example under 24 proper cubic rotations; a fixed lab-axis component changes.
This is a property of that law and group action, not a universal
classification of rates. On an unordered binary menu a scalar rate must
also be invariant under n->-n. Thus (1+r dot n)/2 requires an oriented
menu; it is not an unordered-menu invariant. Alignment 2(r dot n)^2,
purity and coherence examples are even. Covariance alone does not distinguish
those that depend on off-diagonal reconstruction data.

## Fixed-menu factorization

For fixed external records, time, parameters and menu, let
Delta(rho)=sum_q P_q rho P_q. Since Delta is idempotent, f depends on rho
only through Delta(rho) iff f=f composed with Delta. Restricting f to the
image proves the converse. For a qubit Delta retains r dot n and removes
the perpendicular component; |rho_+-|^2=(|r|^2-(r dot n)^2)/4.
The constant and menu-odds functions pass this criterion. Purity and
coherence do not, as explicit states show. Calling this 'registered-only'
is a supplied interpretation: a probability diagonal or conditional quantum
state is not the realized record configuration. No extension of Record's
readout rule to clock dynamics is adopted.

## Constant-clock integration and the order of limits

For fixed nonzero h, omega=|h|, H=h dot sigma/2, precession gives
r(t)=r_parallel+cos(omega t) r_perp+sin(omega t) hhat cross r_perp.
At constant f>0, the exact finite-window average is
r_f,T=r_parallel+Re(z) r_perp+Im(z) hhat cross r_perp, where
z=f[1-exp(-(f-i omega)T)]/[(f-i omega)(1-exp(-fT))].
This follows by integrating exp(-(f-i omega)t) and normalizing the
formation density. Its infinite-window limit is
z_infinity=f^2/(f^2+omega^2)+i f omega/(f^2+omega^2).
The difference of Bloch averages has norm at most 2 exp(-fT), by separating
the omitted tail of a normalized probability mixture. Numerical quadrature
has additional discretization error.

Taking T to infinity first, then f to zero, gives the field-dephased
average. At fixed T, f to zero instead gives the uniform time average with
z=(exp(i omega T)-1)/(i omega T), generally nonzero. Thus replacing a finite window by the infinite-window
formula before taking the slow-rate limit is unjustified. Both iterated
limits eventually give the field-dephased average if T also tends to infinity.
Taking f to infinity at fixed T>0 gives the initial state.
The field-menu probability is constant throughout, so every normalized
positive-mass time weighting agrees there. For h=0 the trajectory is
constant on every menu and hhat is unnecessary.

## Witness and finite diagnostics

For p perpendicular to hhat, write r=c hhat+a p+b(hhat cross p).
The p-menu odds depend on a cos(omega t)-b sin(omega t), independently
of c, whereas the coherence magnitude depends on c^2. Two states with
the same a,b therefore have identical odds trajectories. A common hazard
functional of that trajectory and the same external inputs gives the same
formation-weighted odds. Allowing differing records, parameters or other
arguments would defeat that conclusion. Purity |r|^2=a^2+b^2+c^2 and
the coherence hazard provide explicit unequal-window examples. On the
field menu, varying only the transverse magnitude leaves the odds fixed
while the purity clock's conditional mean time changes; for constant f it
is 1/f-T/(exp(fT)-1).

The runner retains isolated-site and interacting two-qubit trajectories,
three constant law functionals at supplied p_plus=.75, odds/purity/coherence
examples, and a linear hazard beta t. For beta=pi/2, survival is
exp(-pi t^2/4), with infinite-window mean integral_0^infinity S(t)dt=1
in the supplied units. These calculations do not select a physical clock.

The tilted menu is normalized hhat+.9 e, where e is normalized
cross(hax,xaxis), not hax itself and not perpendicular to hhat. Its cosines
are approximately e dot hhat=.424 and p dot hhat=.861. The companion
geometry repair preserves all earlier review corrections.

Seven original check families remain, plus controls for menu relabeling
and the finite-window slow-rate limit. Trapezoid agreement for a selected
constant-clock grid is not a uniform error bound for every hazard or
trajectory. All reported integrals are finite numerical diagnostics unless
an analytic identity above explicitly supplies their limit. A many-site
hazard law, autonomous preparation and which suppliers meet the complete
axiom set remain open. No interpretation or primitive is adopted.

## Dependencies

[Current axiom authority](MINIMAL_AXIOMS_2026-06-29.md).
[Supplied formation-clock model](RECORD_FORMATION_CLOCK_IN_THE_CLAUSE_THE_FIELD_ALIGNED_MENU_S_ODDS_DO_NOT_DEPEND_ON_WHEN_RECORDS_FORM_BOUNDED_THEOREM_NOTE_2026-09-24.md).

## Evidence limits and No-Go Discipline Gate

- **N1 — Domain:** the explicit supplied supports, representations, trajectories and finite experiments above.
- **N2 — Independence:** fresh primary execution is distinct from the independent controls recorded with this review.
- **N3 — Imports:** Hilbert kinematics, models, patterns, clocks and sectors remain supplied rather than framework admissions.
- **N4 — Dependencies:** linked current scoped parents govern; historical titles do not strengthen these claims.
- **N5 — Resolution:** numerical spectra, quadrature, sampled fits and Berry sums are not certified global enclosures.
- **N6 — Residuals:** physical realization, complete classification and larger-system inference require separate evidence.
- **N7 — Counterroutes:** alternative representations, sectors, nonlinear laws and different orders of limits remain available where stated.
- **N8 — Boundary:** this is source review, not an audit verdict or a retained-grade promotion.

## Recovery and falsifiers

An example satisfying a theorem's exact hypotheses but violating its conclusion
refutes that theorem. A failed finite check requires investigation; it is not
silently converted into a different physical interpretation. The original
branch preserves wider proposed claims and all original calculations for
explicit recovery. This source's scope controls its historical identifier.

Original PR #9164, frozen head `949725492ef91dcead40a6144355cec643ed3d60`.
