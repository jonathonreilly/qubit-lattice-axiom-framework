# Focused independent coherent two-leg response review

Reviewer `/root/localized_history_check`; root remains scientific author.
This immutable extension follows the completed one-way proper-count review.
It is not a formal audit, a landing verdict, an actual transponder calibration
or a claim about field dynamics. No author source, old report, state, lock,
branch or index was modified.

## Independent sequence and scope

Before reading any multi-leg author source, I derived the ideal station-to-
spacecraft-to-same-station phase composition and froze
COHERENT_TWO_LEG_PRECHECK_v1.md with closed numerical oracles. I executed the
independent protocol next: 150 controls passed in the final preserved result.
Only then did I read all 97 lines of COHERENT_MULTILEG_WORKING_v1.md, all
156 lines of coherent_count_controls_v1.py and all of COHERENT_COUNT_RESULTS_v1.json.
Their hashes match the supplied frozen identities. The two imported author
helpers had already been read completely in the separate one-way review and
remain unchanged. No author script or imported helper was executed by this reviewer.

The 150 controls are new and distinct from the 179 one-way controls. The source
reuses definitions from the frozen reviewer-owned one-way script, without
executing its test body. It implements two nested retarded null solves and a
shared station clock. These profiles are synthetic smooth metric/path fixtures;
they need not satisfy a free-field equation. They establish neither a KG energy
Gram nor a physical error budget. Any later stationary energy fixture is outside
this frozen comparison.

## Phase composition and checked factors

Let r be station reception, m the common spacecraft receive/re-emit event and e
station emission. For each null leg use its own emitter-to-receiver direction
and denominators. Write d=dm/dr=(1-n_d.v_G(r))/(1-n_d.v_S(m)) and
u=de/dm=(1-n_u.v_S(m))/(1-n_u.v_G(e)). With a fixed coherent phase multiplier k,

    Phi_received(r)=k nu_G tau_G(e)+constant,
    N=k nu_G [tau_G(e_b)-tau_G(e_a)],
    K_2=nu_received/(k nu_G)=f_G(e) u d/f_G(r).

The precheck uses u for the uplink time factor; it is not a velocity or source
frequency. The author's R_1,R_2 are u,d respectively. Its general backward
recurrence delta t_(j-1)=R_j delta t_j+B_j gives

    delta t_0=(product_j R_j) delta t_m
               +sum_j (product_(l<j) R_l) B_j.

Substitution/induction confirms this finite-chain formula and its product order.
The numerical controls here specialize to two legs; they do not claim an
independent numerical test of arbitrarily many legs. The author loop accumulates
the same preceding-leg product before attaching each geometric row. Its
controlled omission of the uplink factor is therefore a relevant discriminator.

At fixed receiving station proper labels,

    delta r=-chi_G(r)/f_G(r),
    delta m=d delta r+n_d.(xi_S(m)-xi_G(r))/D_dm,
    delta e=u delta m+n_u.(xi_G(e)-xi_S(m))/D_ue.

The emitted clock variation is chi_G(e)+f_G(e) delta e. Thus the position rows
are +f_G(e)n_u/D_ue at station emission,
f_G(e)[u n_d/D_dm-n_u/D_ue] at the spacecraft bounce, and
-f_G(e)u n_d/D_dm at station reception. The station clock rows are +1 and -K_2;
the spacecraft direct clock row is zero. These agree exactly with the author
note and endpoint_atoms implementation. The station state is shared at its two
different event times, rather than represented by independent endpoint clocks.
The author normalizes counts in units of nu_0 and divides by the fixed proper
span; the independent code retains k nu_G in absolute cycle counts. This
normalization difference is deliberate and consistent.

## Clock cancellation does not remove force response

The two proper-frequency factors contain f_G(e)/f_S(m) and f_S(m)/f_G(r).
Their spacecraft lapse cancels at the same event, even when it varies. Equivalently,
the exact coherent phase map never reads a spacecraft oscillator. A constant
proper spacecraft transmitter frequency would be a different model. Unknown
proper turnaround delay, time-dependent phase ratio, oscillator phase or hardware
response can restore clock terms and are not removed by this ideal argument.

The author's explicit clock-independent external dynamics make the spacecraft
clock a passive integral. No spacecraft clock atom then implies a zero spacecraft
clock adjoint, hence c_spacecraft=0. This conclusion would not follow merely
from zero endpoint clock rows if a controller or external force depended on that
proper clock. The note explicitly supplies the required clock independence.
The spacecraft position row generally remains nonzero, so its force-response
weight remains. In the static radial reference the row is -2 A_b along the range
direction, giving delta e=-2 xi_S(r-L). A constant range shift changes phase only;
a time-varying displacement changes finite counts.

The shared station clock offset gives
-k nu_G kappa_G (K_2,b-K_2,a). It need not cancel for changing Doppler, whereas the
spacecraft clock anchor is absent from this ideal phase map. Initial orbital
variations and the derived constant-background column must still be treated
using the actual operator. Coherence alone is not a generic constant-background
or initial-state selector.

## Independent numerical evidence

The static spatial conformal profile changes the spacecraft proper lapse but
leaves the coherent count exactly k nu_G Delta T. Its computed derivative is zero
for every tested step. The static temporal profile satisfies the exact
N_epsilon=k nu_G exp(-2 epsilon b L) Delta T relation. Its derivative is
-1.5247232000000013, with final central-difference error 7.40e-10.

For an inertially receding spacecraft and stationary station, the exact response
is (1-v)/(1+v), with no residual spacecraft gamma factor. Its velocity-variation
derivative is -0.41437500000000005 and final error 2.68e-11. A constant range
variation cancels from the count. The nonconstant spacecraft displacement oracle
xi_S(t)=0.03t^2 gives derivative -3.8464607999999996. It is nonzero despite zero
direct spacecraft clock response.

The changing three-dimensional geometry fixture gives derivative
0.11800822657662172, agreeing with direct clock inversion plus nested nonlinear
null intersections to 4.17e-11 at the final step. The independent suite separately
checks reception, bounce and emission event sensitivities, phase rows, ordering
of events, the exact cancellation in the product of proper-frequency ratios,
and the coordinate derivatives dm/dr and de/dr. First-order field, path and
clock pieces add correctly. Spacecraft clock-only changes leave nonlinear counts
unchanged; the shared-station clock derivative is 0.0038081676956233136 and equals
the boundary expression above. These are ordinary floating calculations, not
certified remainder or interval enclosures.

## Preserved finite-difference failure

The first coherent run failed the fixed 3e-7 derivative threshold for the
accelerating displacement at epsilon=0.00125: the error was
8.465219596409668e-7. Its source and stderr are preserved. In accordance with the
frozen decreasing-step protocol, immutable v2 adds epsilon=0.000625 and
0.0003125, retaining all previous steps, the same oracle and unchanged threshold.
The errors then become 2.1162502461535837e-7 and 5.290114613032415e-8. The sequence
shows the expected second-order truncation decrease. No parameter, formula or
tolerance was changed, and multi-leg author source had still not been opened.
The exact repair diff and both execution records are retained.

## Author source/results and regularity

The author preserves one shared fourteen-component two-body orbit/clock state.
Endpoint atoms have the checked geometric composition factors and no velocity
components. The code combines forward variational dynamics, an independently
propagated adjoint and the same declared nonlinear clock/orbit model used in the
one-way helper. Its stored 14 controls include a forward/adjoint count mismatch
3.76e-11, exactly zero spacecraft clock adjoint, nonzero spacecraft force
contribution 0.3794920260651277, and composed-factor omission error
0.03571857405757317. The nonlinear final count error is 1.73e-7, with successive
ratios about four. These are author records inspected for correspondence,
not 14 independent reviewer executions.

The phase endpoint rows touch only position and clock. The velocity adjoint
therefore has no atom jumps, and under the supplied bounded linear coefficients
it is continuous piecewise H1. Terminal zero and full initial-state contrast
provide zero outer traces. The clock weight may jump and remains L2. This
supports the note's reuse of the existing joint-operator regularity under its
stated hypotheses; it does not independently check the joint energy Gram itself.
The stored nullspace has six directions at the declared floating tolerance.
Its rank and annihilation are a synthetic controlled example, not an exact-rank
certificate or a guarantee of usable channels in actual measurements.

No additional mathematical discrepancy was found within this coherent phase/
endpoint/clock scope. Actual link calibration, media, finite delays, clock or
frequency hardware, external-force calibration, tensor/nonlinear corrections,
field dynamics and evidence-supported energy/error budgets remain open. No raw
observations, fitted parameters or new empirical test enter this report.

COHERENT_REVIEW_IDENTITY_v1.json binds all exact source/result identities, the
precheck, the preserved failed attempt, successful controls and this report.
