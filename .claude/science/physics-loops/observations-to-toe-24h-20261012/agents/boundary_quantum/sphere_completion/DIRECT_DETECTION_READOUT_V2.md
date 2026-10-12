# Including missed detections in the proposed correlation test

Direct parent derivation, October 12, 2026. This is a declared measurement
model and prospective design constraint, not measured detector efficiency or
an exclusion using experimental data. It extends the checked reflection
statistic and the separately proposed angular-error calculation.

## All heralded trials remain in the statistic

The source herald and decision to include the trial occur before the fresh
sampling branch and joint setting choice. For each such herald and chosen
local setting, each arm returns
a binary value. If there is no detection, assign an independent fair local
bit. The trial is still included. Both sampling branches use the same local
assignment map. Under the quantum comparison, this is a local binary POVM,
so the reflection bound remains |B|<=1 for arbitrary setting-dependent
efficiency. Fresh-setting independence, a branch-independent common local
map and the definition of the source herald remain required. No coincidence
postselection is used.

For the **candidate prediction**, additionally stipulate independent loss
on the two arms, independent of settings, ideal outcomes and the source's
hidden details, with efficiencies eta_A, eta_B. Assume the fair assignment
bits are independent of those variables and each other. Then

    C_readout(a,b) = eta_A eta_B C_actual(a,b),
    B_readout = eta_A eta_B B_actual.

These formulas do not require ideal fair marginals because any single fair
assignment bit removes its cross term. General setting-dependent or
outcome-dependent loss lacks this simple factorization, even though the
all-trial quantum bound still holds. In a sequential experiment the loss
premises and efficiency lower bounds must hold conditionally on the past;
an unconditional efficiency average is insufficient for the sample guarantee.

If the pre-loss candidate statistic has conditional mean at least 1+Delta,
and eta_A eta_B has a conditional lower bound q, then

    Delta_readout = q(1+Delta)-1.

Positive gap requires q>1/(1+Delta); for equal efficiencies it requires
eta>1/sqrt(1+Delta). With positive certified readout gap, the same bounded
Z in [-111/20,111/20] and threshold 1+Delta_readout/2 give sufficient
N=ceil[40(111/20)^2/Delta_readout^2] for each error at most .01.
No finite sample claim is made when the certified gap is nonpositive.

## Deterministic no-click assignment is a different model

If both arms always assign +1 to a missed event, and the candidate has
fair ideal local marginals as well as the same independent loss assumptions,

    C_plus = eta_A eta_B C_actual + (1-eta_A)(1-eta_B).

A constant correlation c0 contributes -c0 to B, since P3 is orthogonal to
constants and the diagonal has coefficient -1. Therefore

    B_plus = eta_A eta_B B_actual - (1-eta_A)(1-eta_B).

For equal eta and pre-loss lower value 1+Delta, positivity is equivalent
to Delta eta^2+2eta-2>0, or eta>2/[1+sqrt(1+2Delta)]. This is slightly
more demanding than fair randomized assignment under these candidate
assumptions. Either local assignment preserves the quantum bound; their
candidate predictions differ. Discarding missed trials is a third protocol
and is not justified by either equation.

## Frozen diagnostic table

Before calculation, fix equal efficiencies
{1,199/200,99/100,197/200,49/50,39/40,97/100}. Evaluate both assignment
models using (i) the exact ideal visibility-.95 gap and (ii) the separately
frozen bound with per-side angular error 1/1000 radians and additional
candidate correlation error 1/1000. The second model retains fair candidate
marginals for the deterministic-assignment formula; the bounded correlation
error alone would not guarantee fairness. If fairness is unavailable, only
the randomized assignment formula is claimed without further marginal terms.

The comparison uses exact Fraction arithmetic and square-root brackets for
displayed efficiency thresholds. These efficiency values are hypothetical
diagnostics, not engineering requirements derived from actual calibration.
This block selects no optimal inequality or apparatus. A successful real
test still requires a complete source, timing, settings and detection map.

## Source continuity

Version 2 states the timing of heralding and inclusion explicitly. The
original note, frozen table and computation remain preserved; no efficiency,
expectation or sample count changed.
