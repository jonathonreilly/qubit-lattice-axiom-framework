# Canonical force/energy source confirmation

Reviewer: `/root/force_energy_bridge_check`. This supplements the full working
report `REVIEW_FORCE_ENERGY_BRIDGE_v1.md`; it is not a formal audit verdict.

## Exact canonical identities

- Note: `docs/SCALAR_FINITE_WINDOW_INITIAL_HISTORY_BOUNDED_THEOREM_NOTE_2026-10-15.md`
  SHA-256 `6b961015a75b9655623ddffd2c43d1ead6100d61c506208d772fe7cde58509dd`.
- Force helper: `scripts/scalar_force_energy_controls.py`
  SHA-256 `f178ee6df06f7d391e5b9eae26cb4c665afcde458b9afb1fc9f8abe3683a2353`.

I read the full canonical note for context, and checked the complete force,
force-energy, normalization, candidate coupling and gravity-substitution
sections against the independently derived working result. I then inspected
the affected final changes adding angular closed forms. The earlier temporal
and moving-path proofs have separate reviewer scopes; this confirmation does
not replace those reviews or review the entire publication/primary wrapper.

## Confirmed correspondence

The exact conformal action force and its explicit leading free-field use are
preserved. P/R coefficient budgets, Fourier half-wave signs, Cjet coefficient,
joint mode budget, Q factor and constant-background frame scaling remain as
independently checked. The candidate formulas now restated in the note give
partial_u log A=sqrt(a)/F and q=a/J. With 0<k<1/3,
1/3-a=(1-3k)^2/12>0, 1-3a=(1-3k)^2/4>0, sigma Z>0 and J>1,
so the stated 0<q<1/3 follows. This is a consequence of supplied K and A;
it does not select the action, masses or realized background.

The six targeted symbolic confirmations in `CANONICAL_ALGEBRA_CONTROLS_v1.json`
all passed. They directly differentiate the newly restated A, contract K,
check both positivity identities, and establish that the author's new
constant-speed closed forms agree with my independent angular primitives.
The formulas extend to negative nonzero u by their even overall parity;
their u=0 limits agree with the exact stationary norm.

The helper's scientific computations initially matched the working runner;
only its callable/output wrapper differed. Its final additions are:

1. Eight nonzero-speed comparisons between the numerical angular integrals
   and their independently established closed forms. The formulas and units
   agree with equation (5), with T=1 in these helper controls. These comparisons
   meaningfully test the z-u sign rather than just testing a coarse ceiling.
2. A shared `mode_energy_bound(alpha, energies)` computes
   sqrt(2*(alpha.alpha)*sum(energies)) for both random inequalities and the
   aligned attainment fixture. This preserves the bound while ensuring the
   exact fixture exercises the same function. The analytic attainment witness
   has energies proportional to alpha_j² and signed values sqrt(2E_j), so a
   missing factor two is detectable there. The prior random-only sensitivity
   failure is reported by the author and retained separately; I do not relabel
   it as an initially successful mutation test.
3. Output is returned to the primary wrapper; no working source/result file
   is modified by this adaptation.

The numerical calculations remain synthetic. I did not rerun the unchanged
253 independent controls or the canonical helper. The author is responsible
for its changed helper/cache execution and final mutation record. This
confirmation binds mathematical/source correspondence, not an uninspected
cache result or mutation outcome.

## Scope and disposition

No remaining mathematical discrepancy is identified in this force/energy
scope. The canonical units qualification now explicitly requires conversion
of every natural-unit quantity on the right side; the optional SI expression
in my working review is not asserted by the canonical note. That resolves the
presentation clarification without adding an unnecessary unit claim.

The physical energy remains the positive quadratic energy of the stipulated
stable local free operator matching the supplied action. The actual mass
spectrum, approximation error, trajectory/clock/ray calibration, energy budget,
same-background identification and laboratory response are surviving premises.
The note states these limits and does not turn the bound into an empirical fit
or derive a selected state. No raw observations were accessed.

The two referenced supplied-action notes were also byte-compared with their
stated pinned main commit 92574ffe95192cc0724a27e1acad28e42d325115; both match.
Hashes and exact confirmation time are in the accompanying identity JSON.
