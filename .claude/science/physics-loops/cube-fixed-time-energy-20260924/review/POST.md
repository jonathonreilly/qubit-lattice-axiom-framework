# Released-author comparison: fixed-time actual birth energy

2026-09-24. No material mathematical error or missing model hypothesis was found
in the released argument at SHA-256
`083a916c73714a687d1cee0ec93c91594e6aa8e7a135ec12b50a60c238b9bb35`.
Its three stated, birth-scaled limits agree with the independently sealed PRE.
No correction to the theorem argument is requested. This conclusion is
conditional on the stated prior supplied-model results; it is not a formal
audit, retained-status application, unscaled energy limit, or publication-source
confirmation for bytes that have not yet been released.

The sealed PRE was preserved exactly:

    PRE.md
      1681b7333d6244bcad00b8b287b6fd0e621c466a0d1b61d0c53295edd1576e58
    PRE_SEAL.json
      ab8add60721daeb55da75a082dd6c94e958ab9747c8543f9f7cd40a9be19b288

The new author text was first read only after that seal and the parent's
explicit release. No further delegation was used. The author controls' reused
builder is acknowledged below and is not described as independent reconstruction.

## What was compared

The complete released `FIXED_TIME_ACTUAL_BIRTH_ENERGY.md` was read, including
its exact no-event representation, projector inequality, low-band density
argument, moment assembly and stated exclusions. The relevant prior sources
were already read and bound to exact hashes in the PRE; their unchanged
mathematical content was reused rather than re-audited.

The full frozen `control_attempt01/fixed_time_controls.py`, full reused
`cube_control.py`, complete first-run stdout/stderr and aggregate result JSON
were also read. The three separate epsilon result files were parsed and checked
for exact equality with their aggregate rows. The unsealed live revision of
`fixed_time_controls.py` and its pending new normalization family were not read
or treated as final evidence. No expensive numerical run was repeated.

## 1. Exact projector contraction is valid

The argument at author lines 44-86 uses the no-event Riesz projectors E_r,
not the Hermitian projectors P_r, in its monotonicity statement. Since E_r
commutes with the exact no-event semigroup K_e, for t>=s,

    E_r v(t)=K_e(t-s) E_r v(s).

Contractivity of K_e on every vector immediately implies

    ||E_r v(t)|| <= ||E_r v(s)||.

Orthogonality and positivity of E_r are unnecessary. This is slightly cleaner
than the PRE's equivalent exact-similarity construction, which bounds each
coordinate-block propagator by 1+O(epsilon^3). Neither proof assumes that
||P_r v(t)|| is monotone. The author also does not infer such monotonicity
from an approximate projector.

The O(epsilon^3) comparison E_r-P_r is correctly uniform in S. The common
integer W gaps and uniformly bounded T,C_S,Gamma give a common convergent
contour expansion. At order epsilon^2 the only difference is the insertion
of Gamma, which commutes with W. Its contour integrals have double poles and
vanish. This leaves a uniform O(epsilon^3) remainder.

The high initial component is O(epsilon), and the second high component is
O(epsilon^2). Therefore the projector replacement changes
epsilon^(-2)||E_1 v(t)||^2 by O(epsilon^2), uniformly at all later times;
this is the cross term epsilon^(-2) O(epsilon) O(epsilon^3). The author
explicitly invokes the needed initial bound before making this estimate.

For every fixed tau the prior compact-fast-time expansion supplies the
grade-one norm limit f_i(tau). The author then uses exact contraction from
s=epsilon^2 tau to every t>=t0, takes a joint limsup, and only afterwards
takes tau to infinity. This yields the displayed bound (B) from rotor strong
decay on the fixed actual input. It neither substitutes a growing tau into
a compact-time estimate nor assumes an operator-norm rotor decay rate.

## 2. The density-based low-block argument preserves its hypotheses

This is the main difference from the PRE. The PRE derived strong convergence
of the low no-event propagator directly, using its generator
-iKD plus a bounded perturbation. The author instead uses the already supplied
full-density limit, but applies it only to the uniformly bounded Q_S.
That route is valid here, for the following explicit reasons.

1. beta_i is a fixed, normalized, finite-support W=0 vector in N=6. The
   canonical actual first output satisfies ||phi_i-beta_i||=O(epsilon),
   uniformly in S. This is an allowed initialization for the bounded
   compensation target theorem, which covers any P-supported density and
   does not require N=4 initialization.
2. Trace-norm contraction of the microscopic GKLS semigroup transfers that
   O(epsilon) initial difference. The uniformly-in-S target theorem and the
   compensated common-rotor density limit then prove the author's (C) for
   this N=6 initialization, under the same positive fixed parameters and
   joint scaling used in the claim. There is no switch to an uncompensated
   model or another lambda.
3. Projection onto the N=6 corner is a trace-norm contraction. Because the
   Hamiltonian preserves N, births only increase N, and the initial state
   has N=6, that corner is exactly |v(t)><v(t)|. The second-birth N=8 part
   is included in the full density and does not contaminate this identity.
4. Q_S is extended by zero, is uniformly bounded and converges strongly
   to zero on the common physical word space. For a trace-class operator
   A, finite-rank approximation gives Tr(Q_S A)->0. A finite net on the
   norm-compact continuous trace-class orbit makes the convergence uniform
   on [0,T]. The trace-norm error in (C) then gives the author's (D).
5. With the finite-spin canonical unitary U, the expectation change from
   v to U* v is bounded by

       ||U Q_S U*-Q_S|| <= 2||Q_S|| ||U-I||=O(epsilon).

   Since Q_S has only its Pi_0 block, this gives the low-coordinate energy
   expectation that is actually needed. No operator-norm convergence
   Q_S->0 is asserted or required.

Thus the density argument at author lines 88-119 controls precisely the
bounded scaled low-band observable. It does not apply density convergence
to H or H^2, and it does not silently assume an unbounded field-energy moment.

## 3. Moment normalization and scope

The exact terminal identity at author lines 27-42 is correct for both
original instruments at lambda=0: after the remaining birth all eight sites
are occupied and the Hamiltonian is zero. Consequently the unnormalized
no-event vector computes the full-ensemble first and second energy moments.
Survival probability must not be divided out; the author does not do so.

With H=delta epsilon^(-4)h, both scaled expressions in the assembly are

    epsilon^2 <H>/delta       = epsilon^(-2)<v,hv>,
    epsilon^6 <H^2>/delta^2   = epsilon^(-2)||hv||^2.

The Hermitian high-band contributions vanish by (B). In the low band,
h_low=epsilon^2 Q_S+O(epsilon^4), so the mean uses (D), while
||epsilon^(-2) h_low^2||=O(epsilon^2) needs only the uniform Q_S bound.
For the full trace-one density, 0<=Var(H)<=Tr(H^2 rho) is valid even though
H need not be positive. The author's final variance step is therefore valid
and simpler than retaining the squared-mean correction explicitly.

The exclusion of time zero is necessary: the actual birth coefficients are
ell_i=2,1,3/2. The exclusions concerning moving high-field input families,
changing lambda or graph, unscaled moments, quantitative rates and reservoir
interpretation are correctly maintained. No material scope expansion was
found. The PRE's moving lower endpoint and all-future second-moment/variance
refinements also follow from the same uniform inequalities, but the released
author file does not yet state them. Any publication wording must preserve
their distinct scopes, particularly the finite upper endpoint for the mean.

## 4. Frozen finite controls: actual findings and limits

The first attempt's source computes the correct full-H moments from normalized
actual first-mark outputs. It constructs the canonical preparation through
the complete selected low eigenspace and its positive-overlap Gram inverse
square root. The reused spin-one builder enumerates all 3^12 field words,
imposes Gauss, and builds the complete N=4,6,8 spaces of dimensions
3197,5604,672. At spin one all nonzero normalized shift amplitudes are one;
the builder correctly blocks forbidden shifts and uses the corresponding
loss 2-E_e^2 on an empty edge. The compensation and zero N=8 Hamiltonian
match the theorem's model.

The recorded run completed its assertions. Its stderr contains only two
SciPy integer-to-float FutureWarnings. The complete output reports contour
16-to-32 differences about 8.5e-8 to 8.8e-8, and projector comparison norms
divided by epsilon^3 of approximately 2.250,2.326,2.381. These are floating
consistency observations, not interval bounds or a joint S/epsilon limit.
The small nonorthogonal example has a self-adjoint-projector high weight
that rises from approximately zero to 5.17e-6 while the oblique component
decreases; it exercises the precise distinction needed for inequality (A).

A deterministic check of every saved moment row gave:

- Each separate epsilon JSON exactly matches its aggregate row.
- Each saved variance equals saved second moment minus epsilon^2 times the
  saved mean squared, with zero computed residual.
- The largest initial survival normalization error is 6.22e-15.
- The recorded oblique squared norms decrease at every sampled step.

Two evidence-boundary observations remain important and do not invalidate
the analytic theorem:

- In the large control, the commutation residual alone cannot certify a
  correct grade-one Riesz projector: any rational function of h_eff formed
  from resolvents commutes with its exponential. Similarly, propagation by
  the original contraction decreases the norm of any supplied component.
  These gates are consistency diagnostics, not independent identification
  of the spectral band. The added normalization/discriminating family and
  its results were still unsealed and are outside this POST's coverage.
- `control_attempt01` is a historical snapshot, not a standalone runnable
  directory: its script imports and hash-checks `cube_control.py` beside
  itself, while the supplied builder is in the parent author directory.
  Reproduction should explicitly stage the frozen script and exact-hash
  builder together. This does not undermine the recorded original run,
  whose stderr identifies execution from the parent author directory.

No new expensive computation is needed to settle the released mathematical
argument. A final source-bound check of any revised runner is still separate
from this comparison. No claim of independent runner reproduction is made.

## Reviewed source identities

Author root:

    /Users/jonreilly/Documents/Codex/physics-sync-2026-09-24-fifth/campaign-working/.claude/science/physics-loops/mobile-record-next-gaps-20260924/fixed_time_energy_author

Exact relative paths and SHA-256:

    FIXED_TIME_ACTUAL_BIRTH_ENERGY.md
      083a916c73714a687d1cee0ec93c91594e6aa8e7a135ec12b50a60c238b9bb35
    cube_control.py
      cf51bc234d72cb26667b740dddf9f29b27b3c43826dac74df941401a113df125
    control_attempt01/fixed_time_controls.py
      abd7a07671cb482547a3e0d172c244331c1ca9ed55e767fac20e6c2176b6599b
    control_attempt01/FIXED_TIME_CONTROL_RESULTS.json
      fed0d1015a74d6c9292359b861736fb661175f22113899a815558e2f9a94f7bf
    control_attempt01/CONTROL.stdout
      4098d28d68eca33bb83ac347369bc78022cec0228fe1e8fc39e41b27c1ae8050
    control_attempt01/CONTROL.stderr
      26795562885d164bc471d4962d6ff38ea439b39ba1f625199c1a33d63da3263c
    control_attempt01/CUBE_CONTROL_epsilon_0.1.json
      b69b94689c4c78fc5c97d1134cf2b2c6ad2f8cd2d95278ef3d4e2735f6f7da88
    control_attempt01/CUBE_CONTROL_epsilon_0.075.json
      17efeec10160a02434a73c9e3b6b175e3fd7b863ff28370a26f915672c1b98d5
    control_attempt01/CUBE_CONTROL_epsilon_0.05.json
      454d4bc58dbfa1ac4b0a6d69729dc3fb6fc96a9f4b9807ca7749af6b9e9e50d7

The original base commit and prior-source hashes remain those in PRE_SEAL.json.
Only POST.md and POST_SEAL.json were added during this comparison. PRE, prior
evidence, author source, live runner and audit state were not modified.
