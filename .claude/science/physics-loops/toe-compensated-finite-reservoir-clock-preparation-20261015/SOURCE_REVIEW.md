# Source-exposed check of compensated finite-reservoir preparation

Status: substantive mathematical check complete. The reviewed implication is supported under its
explicit expanded-control and pure-memory premises. No material source repair
has been identified. This is a source-exposed check, not an audit or an
independent model-family result.

Target: the exact candidate `DERIVATION.md`, SHA256
`e3f8baf1f1c1d674a8ef22668356f245fc19716d5a4cf53279cd8f994ad02273`,
36516 bytes, and its frozen finite-reservoir/boundary premises. Candidate freeze
SHA256 `653fbbff11aa1ace2118e71d40c82599724b35446a0e91ce9e71ee55994798d5`.
Both supplied identities were verified on 2026-10-15 before argument checking.

The assigned questions are admissibility of positive nearest-neighbour
compensators, the full retained-output target at actual elapsed time, scalar
and original-generator accounting, smooth ramps, resource/calibration charges,
and the sufficient global-peak exponent. The checker separately rederived
the central estimate and scaling. No numerical scientific computation
has been predeclared or run. Metadata operations are not scientific evidence.

Source exposure: the candidate, its conclusion and its resource table were
available before checking. The checker inherits the supervising model/effort;
no blind or model-diverse independence is claimed. No other candidate or
independent-check report is being used.

Instructions read: checkout AGENTS pointer; freshly fetched `ai/execution`
AGENTS; checkout science workflow; physics-claim-reviewer skill; skill freshness
and proof-search governance. The applicable workflow, skill and references
match local `origin/main` bbada1fe09b2d10d610560864d86b68c24a59713. The only Git
operation changing metadata was the AGENTS pointer's fetch of `ai/execution`;
no scientific file, checkout/index content, local branch, PR or audit status was edited.
The first aggregated candidate display was truncated; it is not counted as
complete reading and was replaced by explicit line-complete reads.

The complete candidate (703 lines), complete finite-reservoir raw argument
(541 lines), complete boundary raw argument (182 lines), and 19-line reservoir
root disposition were read. The latter supplies status context only. The first
truncated aggregate display was repaired with nontruncated explicit intervals:
candidate 1–230, 231–490, 491–703; reservoir 1–280, 281–541; boundary 1–182.
The exact canonical files are preserved for byte-binding only; their unrelated
wrapper arguments and other window bodies were not independently reviewed.

## Result and exact scope

Candidate lines 98–152, 239–328, 399–464 and 466–540 establish a coherent
conditional construction. On the literal finite boundary apparatus, given the
fresh isolated pure reservoir and the newly supplied positive generators
`C_j = c_j I - h_j`, a finite smooth schedule prepares the specified entry while
transferring all former clock information into the retained reservoir. The
nominal density-operator target retains the complete reservoir/reference state
and advances the original old generator K for the actual entire preparation
time. Its reference-uniform trace error is at most

    min(2, B r_on + G_e r_off),

and joint readiness error plus full-space implementation error contribute

    eta_ready + 2 integral ||E_impl(t)|| dt.

The displayed balanced schedule really has sufficient peak global added-control
norm `O(e_err^-7)`, versus the parent's particular `O(e_err^-10)` schedule, for
the same specified nondegenerate parameter family. This is a comparison of
two sufficient certificates with different control alphabets. It is neither
an optimum nor an improvement available to the parent's SWAP/X-only supplier.

No missing mathematical premise was found inside that stated implication.
The new generators are a supplied conditional engineering interface within
the existing construction, not an adopted physical axiom or a native supplier.
Its physical supply assumptions remain substantial and explicit: signed
interaction matching inside positive compensators, complex phase/orientation
control, old-Pauli-dependent detunings, common-envelope calibration, eligible
vacancies, independent pure memory, engineered reservoir degeneracy/isolation,
finite timing/precision and an external drive. Their realization is not proved.
The result gives no retained audit status, native dynamics, autonomous driver,
permanent classical record, restoration of consumed memory, arbitrary occupied
geometry or identification of the engineered generator with measured energy.

## Separate central derivation: projective path speed

This check uses normalized pure-state path length and energy variance, with
exact plateau factorization, rather than estimating the candidate's single
full-interval Duhamel integral. It shares the candidate's exact source and
finite-dimensional unitary premises. It is a different analytic route, not a
blind or model-diverse replication. No numerical computation is required.

Write `v(t)=1-u(t)`. On either ramp the actual generator is
`K+u(t) C0 I+v(t) H_app`; the ideal ramp generator is `K+u(t) C0 I`.
For a normalized input purification psi and ramp duration r, let U and U_c be
these propagators and consider the normalized comparison curve

    chi(s) = U(r,s) U_c(s,0) psi,       0 <= s <= r.

Its endpoints are the actual and comparator output. Direct differentiation
gives `dot chi = i v(s) U(r,s) H_app U_c(s,0) psi`. Consequently its projective
speed is

    sqrt(||dot chi||^2 - |<chi,dot chi>|^2)
       = v(s) Delta_(U_c(s)psi)(H_app).

For normalized rays, the angle between endpoints is at most integrated
projective speed; the trace distance of the two pure density operators is
twice the sine of that angle. To see the path-length inequality, remove the
instantaneous common phase so the tangent is orthogonal to the ray. For
`f(s)=|<chi(0),chi(s)>|`, Cauchy–Schwarz then gives
`|f'(s)| <= sqrt(1-f(s)^2) ||dot chi_perp(s)||` wherever differentiable.
Integration of the arccosine derivative, extended by continuity at its
endpoints, bounds the endpoint angle by the integrated speed. Thus no
expansion in r or assumption about actual sector occupation is being made.

On turn-on, every input is allowed, but `0 <= H_app <= B I`. Since
`H_app^2 <= B H_app`, writing its mean as m gives
`Var(H_app) <= B m - m^2 <= B^2/4`. The turn-on curve therefore has length at
most `B r_on/4`, using `integral v = r_on/2`. Its full-output trace distance
is at most `2 sin(min(pi/2,B r_on/4))`, hence at most `B r_on/2`.

On the plateau the actual generator is exactly `K+C0 I+G(t)`. K acts on D,
whereas both pulses act on C/E; they commute. The disjoint full SWAP pulses and
the entry pulse have area pi/2 and endpoint unitaries exactly `product S_u`
and `X_v0`, including their phases. Thus this whole plateau is exact on every
input. It maps ideal turn-on output to the bare entry C factor and transfers
the whole old C register, with all correlations, into E. Applying the actual
plateau and off-ramp to the earlier error cannot increase its trace norm.

For the remaining comparison, the off-ramp starts on the ideal entry factor
with arbitrary D/E/R purification. At every comparator time the source
compression identities give

    <H_app> = alpha0,      <H_app^2> = alpha0^2+q,
    Delta(H_app) = sqrt(q).

The old K evolution changes neither identity: they are scalar compressions on
the entire D domain. The off-ramp projective length is at most
`sqrt(q) r_off/2`, and its full-reference trace error at most
`sqrt(q) r_off`. Combining the two stages proves the slightly tighter bound

    ||rho_actual-rho_target||_1
       <= min(2, B r_on/2 + sqrt(q) r_off)
       <= min(2, B r_on + G_e r_off).

Purification and contraction establish this uniformly for mixed inputs and
arbitrary passive references, with E retained. The tighter bound is an
optional strengthening, not a necessary repair. It does not improve the
resource exponents here because `sqrt(q)` and `G_e` have the same nonzero
asymptotic order in the specified family.

The phase-sensitive isometry statement cannot simply substitute variance for
the full norm. Retaining `||dot chi||` instead of its projective component gives
`B r_on/2` and `G_e r_off/2` in Hilbert norm. Telescope the exact plateau and
two unitary ramps to recover precisely the candidate's isometry estimate
`||UJ-V_T|| <= (B r_on+G_e r_off)/2`. This also checks the common phase
`exp(-i C0 A_u)` and the unchanged old phase `exp(-iTK)`. The channel's freedom
to ignore a common phase does not authorize removal of a generator scalar or
its energy/work charge.

The readiness/error extension follows separately from contraction of the
initial trace error and the full-space perturbation estimate for two finite
unitary propagators. Sector-breaking perturbations are covered only when
their full-space norm integral is supplied. Nothing here certifies that
physical calibration.

## Literal compensators, geometry and imported hypotheses

The term spectra in candidate lines 109–123 are correct. Occupations have
eigenvalues 0 and their coefficient; signed P n terms have spectrum
`{-d,0,d}`; real or complex exchange has one-excitation eigenvalues `+/-d`
and zero on the empty/full pair. Thus `c_j=lambda_max(h_j)` makes each C_j
positive on its whole local qubit space, with no one-excitation restriction.
All supports are the original onsite or nearest-neighbour one-/two-qubit
supports. Positive scalar padding alone does not supply the signed `-h_j`
interaction, and the candidate correctly treats that as new control access.

Summing the literal terms gives exactly

    number of compensator terms = 2L+23,
    D_c = 2 Lambda + 2 sqrt(Lambda) sum_(j=0,1)(g_j+|z_j|)
                         + sum_(j=2)^(L-1) J_j,
    C0 = B + D_c,       S_C = B + 2D_c,
    C = C0 I-H_app,     D_c I <= C <= C0 I.

The vacuum attains C0. S_C is the sum of local term norms and is correctly
kept distinct from the global norm C0. The four detunings supply total
compensator norm `2 Lambda` at q0; mediator and head loads in (7) follow by
adding their incident table entries. Installed-plus-control loads in lines
205–211 likewise retain the original terms even where the net operator
cancels. A finite cap needs an actual positive margin; vacancies provide none.

The coordinates prove disjoint matching for all L>=8: reservoir tail sites
have `(x,z)=(1,-1), y<=-1`, the remaining site in that class has y=0, and the
other finite rows are separated by coordinates. Every matched pair differs
by exactly one unit. The resulting `2(L+9)` new qubits and `2L+23` selected
edges agree with the parent. The equal numerical term count is a different
inventory. Other occupied factors must avoid these sites, and unlisted
couplings to nearby old sites remain excluded or paid.

I checked the needed parent algebra directly against its literal coefficients,
not merely its accepted label. For each cell and Pauli eigenvalue p=+/-1 the
mediator arm is

    [[1,-1/4],[-1/4,1+p/4]],

with the other arm obtained by p -> -p. Both are bounded below by 1/2. Their
inverses give left self-energy `448 kappa/209`, right self-energy
`480 |z|^2/209`, and upper-right response
`-kappa exp(i phi P)`, hence the stated lower-left response. The first cell's
reversed orientation and phi0=-pi/4 produce the required first logical edge.
The head Schur complement is `cI+G`, unitarily gauged to the scalar path with
extreme eigenvalues `c +/- Omega L`; its minimum is Omega. Factoring the
positive old-operator-valued site matrix is legitimate on all hard-core
sectors because its old operators commute with every new annihilator.

There is also a separate check of the full-space upper norm, avoiding a
one-particle trace argument. Let X_C flip all C qubits, let P_arm swap a with
a' and b with b' in each cell, let Z_alt be the product of Z over either
lattice parity class of C, and let Y_q act on the addressed old datum. The
unitary `Z_alt P_arm X_C Y_q` conjugates the literal apparatus to `B I-H_app`:
occupations become their complements; the three sign reversals on the paired
detunings give their negatives; particle-hole conjugation and arm swapping
restore the complex port orientation; Z_alt negates every C–C exchange.
Therefore positivity of H_app also implies `H_app <= B I`. The all-C-full
state gives eigenvalue B and the vacuum gives zero. This verifies the exact
full-sector norm used on turn-on without assuming simultaneous old-Pauli
diagonalization.

Finally, the actual entry v0 is the right port. Its two outgoing mediator
amplitudes have squared norm `2 Lambda |z0|^2=q`, while its diagonal is alpha0.
These images are orthogonal to the entry and to each other, so
`J_e* H_app J_e=alpha0 I` and `J_e* H_app^2 J_e=(alpha0^2+q)I`.
This independently verifies G_e and the variance input of the projective
check. It also confirms that replacing z0 by g0 would price the wrong port.

The subsequent word's order remains `exp(-itK) W exp(-iTK)`, with its full
moving clock output. Rearranging this to `exp(-i(t+T)K) W` would be invalid for
general K. The boundary proof's gauge/prefix comparison and explicit finite
parameter choices were read; no additional result from its other canonical
window bodies is being imported.

## Smooth schedule and resource derivation

The bump profile is smooth and flat at its endpoints. On [1/3,2/3],
`b>=exp(-9/2)`, so `I_b>=exp(-9/2)/3` and `m0<=3 sqrt(e)`.
Writing `y=1/[x(1-x)]>=4` gives `|b'|<=y^2 exp(-y)<=16 exp(-4)`, hence
`m1<=48 sqrt(e)`. Symmetry and unimodality give `integral F=1/2` and
`integral |w'|=2m0`. These facts prove the displayed finite areas, peak slopes
and variations; there are no switching impulses. An exact normalized waveform
is a supplied idealization and its implementation error is charged explicitly.

The fixed-width, fixed-K, positive-prefix family has specified lower choices
`L=Theta(e_err^-2)`. From `kappa_j=Omega sqrt((j+1)(L-j))` at j=0,1,
`g_j,|z_j|,f=Theta(L^1/4)`, while `b=Theta(L)`. The mediator numerator in
the boundary's finite bound is dominated by `b r=Theta(L^5/4)`; squaring its
division by e_err yields

    Lambda = Theta(L^(5/2) e_err^-2) = Theta(e_err^-7).

This uses the nonzero fixed constants explicitly assumed by the candidate.
The scalar head sum is `Theta(L^2)`, the direct-tail coefficient sum is
`Theta(L^2)`, and the port magnitudes are `Theta(e_err^-4)`. Thus the Lambda
terms dominate B, D_c, C0, S_C and d_max, all of order `e_err^-7`.
Furthermore `alpha0=Theta(e_err^-2)`, `q=Theta(e_err^-8)` and
`G_e=Theta(e_err^-4)`. These two-sided orders justify the reciprocals; arbitrary
larger Lambda or a degenerate prefix is outside this particular power table.

With switching allowances proportional to e_err and
`t_s=t_p=n pi m0/C0`, it follows that

    r_on = Theta(e_err^8),       r_off = Theta(e_err^5),
    t_s=t_p = Theta(e_err^5),    T = Theta(e_err^5).

The parallel SWAP norm is `2n gamma`, because all n pairs can be antisymmetric
simultaneously. Its peak is therefore exactly C0 on this schedule; the entry
peak is C0/n. On pulse intervals the installed-plus-compensator apparatus is
the scalar C0 I, so its full norm including the active positive pulse is at
most 2C0. The added controls alone have norm at most C0 plus the active pulse;
equality for the noncommuting sum C+G is not needed or claimed.

The compensation turn-on derivative is `Theta(C0/r_on)=Theta(e_err^-15)`.
The off-ramp and SWAP derivative are order `e_err^-12`, and the entry
derivative is order `e_err^-10`. Their derivative supports do not overlap.
The integrated global control norm is bounded by

    C0 [2n pi m0/C0 + (r_on+r_off)/2] + n pi + pi,

which is `O(e_err^-2)`, including turn-off. Total control variation is
`(4+2/n) C0=O(e_err^-7)`. Per-site added load is `O(e_err^-7)` and the
complete duration is `O(e_err^5)`.

For comparison, the parent's chosen SWAP duration is order `e_err/B=e_err^8`.
Its peak global norm `2n pi/t_s` is order `e_err^-10`, derivative
`2n pi^2/t_s^2` is order `e_err^-18`, and variation is order `e_err^-10`.
Its entry duration is order e_err^5, so both schedules have the stated total
duration order and action order. This independently reconstructs every power
in the candidate's comparison table, rather than inferring them from its
headline. Both rows are sufficient constructions; neither is a lower bound
over all controls.

At a fixed positive plateau duration, compensation action is instead order
e_err^-7. The calibration estimates correctly distinguish the cases:
`2 eta_C S_C A_u` permits a sufficiently small `eta_C=O(e_err^3)` on the
balanced family and `eta_C=O(e_err^8)` at fixed duration. These are demanded
certificates, not achieved calibrations. Independent envelope errors, shared
envelope errors, waveform shifts, cross terms between coefficient/envelope
faults and all n pulse errors are separately accounted for. A change in
elapsed endpoint time requires a retimed target or an additional evolution
bound; it is not just an L1 waveform translation.

## Scalars, moments, work and discriminating failure witness

The apparatus's Pauli scalar is B/2. Paired old-only detuning strings cancel;
each onsite occupation contributes half its coefficient, and exchanges have
no scalar. Compensators therefore contribute `u(C0-B/2)`. The SWAP and entry
scalars are `n gamma/2` and omega. The `3L+41` nonidentity-string count follows
from L+9 onsite strings, four detuning strings, 8 internal-exchange strings,
8 left-port strings, 16 complex right-port strings and `2(L-2)` tail strings.
None of these scalar or local-load charges disappears when the plateau's
effective dynamics cancels H_app.

Endpoint moments use the same installed `H0=K+H_app`, because every added
control vanishes at both endpoints. The initial K/H_app covariance is kept.
At the ideal output, scalar entry compressions and free-K aging give mean
`Tr(K sigma_D)+alpha0` and variance `Var_(sigma_D)(K)+q`, regardless of the
retained E correlations. With `beta=h+B`, trace duality gives the stated mean
and centered second-moment errors; the squared centered means add at most
`2 beta^2 eps_total`, so the variance error is at most `3 beta^2 eps_total`.
The reference-valued linear-moment estimates follow by duality against any
record operator of norm <=1. They are not conditional variances or an energy
measurement. The note correctly demands tighter trace error for fixed moment
tolerances when B grows.

For the finite closed driven system,
`d Tr(H_act rho)/dt = Tr(dot G_tot rho)` is exact. With equal endpoint
generators, integrating it gives the candidate's work identity. Integrating
the three actual derivative norms yields its bound and `(4+2/n)C0` on the
balanced schedule. Since `D_c I<=C<=C0 I` and each ramp is monotone, the on
work lies in [D_c,C0] and the off work in [-C0,-D_c]. This is an upper variation
allowance; it is not a minimum net work, cooling law or microscopic account
of the controller and its energy store.

The retained-output counterexample is valid and sharply scoped. Start with
any fixed old vector and `(vac_C 0_R + full_C 1_R)/sqrt(2)`. Turn-on gives
the exact relative phase `theta=B r_on/2`, because H_app has eigenvalues 0
and B on those rays for every old state. The exact plateau transfers the phase
into E/R. Subsequent off-ramp dynamics acts only on D/C, so the E/R marginal
retains trace distance `2|sin(B r_on/4)|` from its target. Partial-trace
contraction makes this a lower bound on this schedule's final full-output
error. At `r_on=1/B`, it stays `2 sin(1/4)` while `G_e r_on -> 0` in the
specified family. Thus replacing the arbitrary-sector turn-on charge by an
entry-only G_e charge is false. This is not a lower bound for every control
design; special phases and further correction operations are not excluded.

The witness also explains why discarding E would hide a relevant error. Dirty
memory, an excitation-exchange substitute for full SWAP, or a requirement that
E return to the same pure state would change/fail the stated target; the
candidate preserves those limitations. No universal no-go is proposed here.

## Verification limits and source freeze

No numerical scientific program, parent runner, physical device or formal proof
checker was run. The one allowed optional computation was not needed. This
report supplies analytic finite-dimensional checks, not a simulation of the
many-body dynamics or evidence of practical control supply. The projective
derivation and literal-spectrum checks are distinct calculations but share
the candidate's inputs and model family. More source copies or zero-exit
metadata receipts do not strengthen that independence.

After the substantive derivation, resource checks and the report above had
already been written, the supervising agent reported that its own candidate
read found no repair. That observation arrived before final freeze, but no
other review body, derivation or computation was supplied or used. This late
conclusion exposure further precludes a claim of blind checking. The stronger
channel bound above belongs only to this report; the immutable candidate was
not edited or silently strengthened.

The only persistent outputs are this assigned report directory and its source
and bookkeeping artifacts. Editable prompts changed: none. Scientific
checkout files, PRs, locks, campaign checkpoints and audit records changed:
none. The initial AGENTS-directed fetch updated Git fetch metadata only; it
was not a checkout, science edit or status application. No other chat was
messaged; the supervising agent receives progress/final notices through the
delegation channel.

Source capture, closure and the final freeze refresh are the actual metadata
child executions in `runs/capture/`, `runs/closure/` and `runs/final/`, with
launch sources, complete stdout/stderr and receipts. The last refresh only
checks for concurrent source drift before freezing. The initial tool-mediated identity probes are documented in
`TOOL_READ_RECORD.md`; those were not scientific programs or previously sealed
runs. Source identities are in `SOURCE_MANIFEST.json`, and final freshness,
canonical extraction and candidate-freeze checks are in `FINAL_CHECK.json`.
`FINAL_FREEZE.json` pins the completed report and all deliverable members,
excluding only its own circular hash. These are identity/bookkeeping records,
not additional mathematical proof. No scientific conclusion is deferred
behind a future numerical experiment.
