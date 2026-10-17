# Proposed finite-precision real preparation contract

Corrected V2 of the root-authored analytical proposal. A separate same-model,
source-exposed reviewer reconstructed the load-bearing estimates and identified
two narrow proof corrections, both included below. Root source qualification
is recorded in ../bounded_followup_root_review/ACCEPTANCE.json. This refines the
qualified real local preparation, without changing its runtime apparatus or
importing a new thermal device. No scientific program or parameter search ran.
It is not published or retained; the frozen original proposal is preserved.

## Exact contract and controlling sources

Use exactly the realifier c1cf729c2639d682a66df72b880c529dbabfc1768935ae62d170538973ce2018
and preparation57e1cebcee12bf6499564051f91f981fe11814d73d45b9e1168c045e65ab9b8c,
qualified together by root acceptance98315ba16275ceb44dd3fcf32d655d1e92d42da7c7678600327be89d9d1ba852.
The same literal HR,M, exact static coefficients, kappa in[1e-12,1e-8],
M=ceil(50/kappa^2), T=kappa^-2, old K and W are retained. The fourteen
positive preparation terms act on the same eight sites and no old/source
qubits. All statements below use the same fixed apparatus before and after
setup. Time t denotes time after the five-unit setup.

Write the nominal added control as

    A(s)=u(s) sum_{a=1}^9 R_a
       +w1(s)[Q_e0,m(+1)+n_e1]
       +w2(s)[Q_m,e1(-1)+n_e0] +w3(s)n_e1.

These are fourteen separately counted term channels; the last n_e1 channel
has a different time window from the first pulse spectator. The fixed R_a
are the eight positive edge complements and the positive pin from the
parent. Their norm sum is

    Aiso=4J+4kappa(1+c+s)+E0-kappa < 1/7.

The parent supplies nonnegative C1 profiles on[0,5], all zero at endpoints,
with integral u=4, integral w1=pi/4, integral w2=integral w3=pi/2. The full
Q(+1) and Q(-1) norms are2, and each occupation norm is1.

For each of the fourteen channels independently, multiply its entire fixed
positive local block by a constant 1+xi_a with |xi_a|<=eta<1. Keep its nominal
profile, support and internal coefficient ratios. This is a box of static
amplitude calibrations of the preparation channels. It is not a box of
independent Pauli coefficients or arbitrary errors in the runtime Hamiltonian.
In particular an entire Q/complement scales together, preserving positivity.

## 1. Uniform control-error budget

Let A_xi be this perturbed control and U_xi the actual five-unit evolution
under HR,M+A_xi. With U_0 the nominal preparation, full-space unitary
Duhamel and the triangle inequality give

    ||U_xi-U_0|| <= integral_0^5 ||A_xi(s)-A(s)|| ds
       <= eta [4Aiso+3pi/4+3pi/2+pi/2]
       = eta [4Aiso+11pi/4] <= 10 eta.            (1)

The coefficient3 counts a two-site block of norm2 and its spectator of norm1.
Using pi<22/7, the bracket is less than129/14<10. This estimate is on the
full finite qubit space, independent of M, and remains valid after tensoring
any passive reference. It does not assume that the actual perturbed state
stays in the ideal isolated core. Global scalar errors from the local
complements are included in the full operator difference.

Combining (1) with the nominal supported preparation estimate gives

    ||U_xi E_e0 - exp(-iPhi) E_chi exp(-5iK)||
       <= sqrt(2)kappa + eta[4Aiso+11pi/4].       (2)

Phi=5cseed+4r+3pi/4 is the nominal comparison phase. This is a bound to
that specified phase, not an assertion that the perturbed evolution has
exactly the same scalar action or exactly the same prepared head state.

Propagate the entire difference under the unchanged HR,M runtime and use
the qualified complete resonance interface. Uniformly for t in[T,2T],

    ||exp(-itHR,M) U_xi E_e0
      -zeta exp[-i(Phi+cR*t)] B_t^R exp[-i(t+5)K]W||
       < .00483202 + 10 eta.                    (3)

Every old/reference/source/emitter/rail output, the actual common waveform,
fixed central residual and old aging remain in the same comparator. The
nominal finite window and enormous apparatus size are unchanged. There is
no setup-time factor multiplying the later huge runtime t in (1): the
new perturbation vanishes after setup. Static runtime calibration errors,
if present, would require a different analysis and are not included here.

For eta=10^-5 the complete finite operator bound is <.00493202. Thus the
unhalved trace distance for the stipulated pure seed and every old/reference
input is <.00986404, using the two-isometry expansion. On the infinite
apparatus the same addition applies to the .00383202 bound for all t>=T;
this does not create an all-future finite-device theorem.

## 2. Supplied imperfect seed with arbitrary old/reference correlations

For 0<=epsilon<=1, suppose the actual joint input omega_DRA has actual
old/reference marginal rho_DR and apparatus seed probability at least1-epsilon:

    Tr[(I_DR tensor |e0><e0|)omega_DRA] >= 1-epsilon.

Here |e0> denotes the entire required auxiliary product seed: both sources
and clocks blank, e0 occupied, e1 blank. Use the already-qualified general
rank-one marginal bound from the earlier product-preparation source,
without importing that source's single-rail Gibbs apparatus:

    ||omega_DRA-rho_DR tensor |e0><e0|||_1
      <= g(epsilon)
      := epsilon+sqrt[epsilon(4-3epsilon)] <=3sqrt(epsilon). (4)

Let d=1-Tr[(I_DR tensor |e0><e0|)omega_DRA] be the actual deficiency,
so 0<=d<=epsilon. Projecting onto the seed gives a subnormalized state whose
trace distance from omega is at most sqrt[d(4-3d)]. To see this, purify omega
and split the purification into its orthogonal seed and complement parts.
The difference from its projected rank-one operator has eigenvalues
(d+sqrt[d(4-3d)])/2 and (d-sqrt[d(4-3d)])/2. Partial trace is contractive.
Replacing the projected old/reference marginal by rho_DR costs d, because
the residual marginal is positive with trace d. Thus the triangle bound
is g(d), followed by g(d)<=g(epsilon). The complete function g is monotone
on[0,1]: its derivative is 1+(2-3x)/sqrt[x(4-3x)] on(0,1); this is
nonnegative below2/3, and above2/3 follows from
x(4-3x)-(3x-2)^2=4(1-x)(3x-1)>=0. Continuity includes the endpoints.
The simpler projection term alone is not monotone on all[0,1]; d=2/3 and
epsilon=1 give2/sqrt(3)>1, so its isolated replacement by epsilon would be
false. No such replacement is used here. The final estimate g(epsilon)
<=3sqrt(epsilon) follows from epsilon<=sqrt(epsilon) and 4-3epsilon<=4.
This is an input-quality implication, not a cooling theorem. Its exact
antecedent is reused from the qualified product-preparation lemma.

Both the perturbed setup and later runtime are the same actual unitary for
the two initial states, so their trace distance is preserved. Combining(3)
and(4), the complete finite output trace error is strictly below

    g(epsilon) + .00966404 + 20 eta.             (5)

The explicit box eta<=10^-5 and epsilon<=10^-9 gives

    g(epsilon)+.00986404
      <=3sqrt(10^-9)+.00986404 < .00996404 < .01.

The inequality3sqrt(10^-9)<10^-4 follows by squaring positive quantities.
No independence between old/reference and auxiliary input is required.
No measurement or postselection is performed; all initial bad-sector weight
and preparation leakage remain in the full trace bound. The pure-input
operator estimate(3) is not extended as an isometry statement to mixed inputs.

## 3. Full positivity, support, slew and modeled work

All factors1+xi_a are positive constants, so the changed controls remain
real PSD local blocks with the same ordinary-neighbor supports. They remain
C1, zero at both endpoints, and identically absent after time5. There are
still fourteen channels on eight sites and no new qubits or old/source
controls. The old added incident cap two, old edge norm3 and source loads
are unchanged. There is no all-site cap-two claim.

Full positive-block norm sums and incident derivative norm sums increase by
at most1+eta. Thus for eta<=10^-5, valid rounded bounds are

    added control norm sum <9.001,
    maximum incident control slew <20.001,
    absolute modeled setup work <33.001.

For work, use the actual state and Hamiltonian identity
Wsetup=Tr[HR,M rho(5)]-Tr[HR,M rho(0)], since A_xi vanishes at endpoints.
Integrating the sum of absolute coefficient variations times full block
norms gives at most(1+eta)[2Aiso+165pi/16] <33(1+eta)<33.001.
No ideal-core zero-work shortcut is applied to leaked or imperfect inputs.
The work is modeled Hamiltonian work only, with no microscopic controller
heat, fabrication, reset cost or physical energy identification supplied.

The same operator bound(1) would hold for bounded time-dependent relative
errors, but the displayed C1/slew/work bounds do not follow from a mere
amplitude bound in that wider class. The present result deliberately uses
constant calibration errors. Timing shifts, pulse-overlap errors, altered
static hoppings, density/complement imbalance and changing supports are
separate models and are not included by relabeling them as xi_a.

## 4. Readiness and energy limits

The theorem weakens exact pulse-area and exact pure-seed requirements to
explicit supplied amplitude and joint seed-probability contracts. It supplies
neither their native calibration nor their physical manufacture. The old
single-rail Gibbs construction is not transported to this doubled apparatus.

The channel/readiness bound alone does not extend the parent's preparation
energy-moment guarantees uniformly over growing M. For example, a mixture
of the desired seed and probability epsilon of the all-occupied auxiliary
configuration meets the seed-probability premise while the latter component
has a clock energy growing with M. Its initial energy contribution is of
order epsilon M. A useful energy or variance claim for imperfect delivery
needs a weighted moment/tail contract as well. The bounded actual control
work above is a different statement and remains valid for every finite input.

Native control/thermal suppliers, autonomous preparation, joint static
runtime calibration, noise through the long runtime, complete capture/reset/
reuse, practical resources and physical Hamiltonian/energy/Record identification
remain open. Only the five-unit control calibration box and the stated
correlated input-quality implication are qualified for provisional composition
after the preserved selective analytical check and these two corrections.
Publication, transport checks and independent retained audit are separate.
