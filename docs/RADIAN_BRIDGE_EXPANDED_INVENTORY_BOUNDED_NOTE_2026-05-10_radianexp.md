# Supplied rational catalogue and finite angle-target search

**Date:** 2026-05-10 (scope corrected 2026-10-25)
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status authority:** independent audit lane; this source does not assign an audit outcome.
**Primary runner:** [`scripts/cl3_radian_bridge_expanded_inventory_2026_05_10_radianexp.py`](../scripts/cl3_radian_bridge_expanded_inventory_2026_05_10_radianexp.py)
**Cached output:** [`logs/runner-cache/cl3_radian_bridge_expanded_inventory_2026_05_10_radianexp.txt`](../logs/runner-cache/cl3_radian_bridge_expanded_inventory_2026_05_10_radianexp.txt)

## Restricted positive arithmetic

The runner's Fraction catalogue is supplied data, not verified retained
physical provenance. If x,y are rational, then x+y, xy and x/y (y nonzero)
are rational: write x=a/b,y=c/d with integer a,b,c,d and bd nonzero,
and use `(ad+bc)/(bd)`, `ac/(bd)`, `ad/(bc)`. Induction proves closure
for finite arithmetic expressions with nonzero denominators. Algebraic
closure is algebraic, not necessarily rational: the positive fourth root
of 2 is an elementary counterexample. Adding rational entries does not
enlarge Q's dimension over Q. None of these statements constrains arbitrary
free dimensionless parameters or the full numerical catalogue below.

For supplied `a=1/(4pi)`, `u>0` and `l=a/u`, all denominators are positive
and substitution gives `1/a=1/(l*u)=4pi`, whereas `u/l=4pi*u²`.
The historical candidate `u_0/alpha_LM` keeps its actual value and now bears
the latter label. Inserting pi into a definition does not independently
predict pi. No equivalence with a physical QED normalization, phase-space
measure, or a physical radian-bridge premise is established here.

## Exact scope of supplied data and computation

The 28 Fraction atoms are
`1/3,2/3,2/9,8/9,1/9,1/2,1/4,1/5,7/8,7/9,7/18,4/3,13/3,37/2,
3071/36,20873/48,5/9,47/486,16891/43740,41/10,-19/6,-7,16,18,2,3,7,26`.
“APBC fourth-power factor” is a historical catalogue label for the supplied
`Fraction(7, 8)` value, not proof of its physical origin.
`P_VEV_NUM=0.5934` remains the original binary float promoted to mpmath;
50-digit computation does not recover missing input precision. Its fourth
root u0 is not certified rational. Catalogue flags distinguish expressions
with and without explicit pi, not rational versus irrational numbers.
The remaining atoms are P,u0,a,l,a/u0² under the supplied definitions.

The search uses mpmath at 50 decimal digits: singles, ordered pair products
and ratios, and ordered pair linear combinations with coefficients
`[-3,-2,-1,1,2,3,4,6,8,9]`. Pair sums of absolute size at most 1e-3 are
excluded as in the original. Targets are `2pi,pi,pi/2,pi/3,pi/9,4pi,
1/(2pi),(2/9)*2pi`. Relative thresholds remain 1e-3 (near) and 1e-30
(strict numerical threshold); stored reported errors retain the original
conversion to float. “Strict” does not mean a symbolic equality proof.
The filtered rational-atom result checks only this implemented search.
There is no triple or general-power search or probability model for an
expected coincidence count. Historical example values await actual output
verification; this source-only revision does not report fresh findings.

## Finite expression displays

At s=1/8 the runner evaluates the supplied heat expression
`1-exp(-(4/3)*s)`. Its comparisons do not establish an e/pi independence
theorem or universal exclusion. The Wilson display is the finite polynomial
`(4/3)s-(1/9)s²-(13/81)s³-(37/162)s⁴-(3071/8748)s⁵-(20873/34992)s⁶`.
The discrepancy display at s=1/8 and 1/2 is
`(7/9)s²-(5/9)s³-(47/486)s⁴-(16891/43740)s⁵-(308999/524880)s⁶`.
Their rational-input evaluations are rational by the finite arithmetic
proof; no convergence or infinity limit is proved. In particular
`q_n=floor(10^n*2pi)/10^n` is rational and
`0<=2pi-q_n<10^(-n)`, so rational sequences can converge to 2pi.
The eight power displays use exactly exponents `[1,2,4,8,16,18,32,36]`,
not every exponent through 36. Printed values are unscored observations.

## Rounded cosine comparison

The hardcoded rounded vector `(-0.67857,-0.29683,0.97540)` is a supplied
comparator. Fourteen fixtures are `1,2pi,4pi,pi,u0/l,4/3,7/8,7/9,16,18,26,
l,l²,P`. Each yields sorted `cos((2/9)*alpha+2pi*k/3)`, k=0,1,2, compared
with the sorted rounded vector by maximum absolute deviation. The old
best-match and alpha=1 assertions used literal True: they remain unscored,
not fresh numerical tests. This comparison neither derives masses nor
selects a physical phase. Alpha=1+9pi*k for integer k has the same cosines
as alpha=1, which disproves global uniqueness from these fixtures.

## Historical withdrawals and current evidence boundary

The old whole-framework obstruction, six independent no-go tally, terminal
admission ledger, retained provenance, e/pi theorem attribution, Wilson
infinity assertion and physical normalization identification are withdrawn.
Exact old source and cache are preserved in recovery. Literal True claims
are printed only as HISTORICAL_UNSCORED, including old labels; these are
not current assertions. Genuine finite predicates and thresholds are
preserved in the external predicate map. The runner has no imported physics
helper or source-note proof premise; its actual input is this note and its
explicit embedded data. No downstream theorem or status is approved.
The existing cache is historical pending separately authorized execution.
