# Local Physical-M2 Mass--Scalar Deformation Response — Route B

Date: 2026-07-17

Authority: none

Audit: unset

Constitutional effect: none
Scientific type: bounded constructive deformation response with explicit imports

Coverage: all 24 proper-cubic frames and 648 frame-translation tests.  Scope:
this is not physical energy and not a selected gravitational source.  No axiom
pressure is claimed.

## Question

Can the current connected physical-M2 matter/contact fixture and the finite
six-direction scalar coin support a new exact local relative update whose
response is bounded, Hermitian, additive, translation/proper-cubic covariant,
and aligned with the existing scalar response fixtures?

The target here is deliberately narrower than a gravity/source law.  A positive
answer must not rename a wrapped phase physical energy, a gate generator a
rate, or a supplied deformation response a selected gravitational source.

## Construction

For the Cycle-219 species at `beta=-0.3`, let

\[
    m=-3\tan(\beta/2),\qquad
    M_x=mN_x.
\]

On the Cycle-269 connected physical matter code, the six local occupation
parities are represented by the gauge-compatible physical Pauli operators
`B_(x,d)`.  Thus

\[
    N_x={1\over2}\sum_{d=1}^{6}(I-B_{x,d}).
\]

Add six physical field M2 sites per coarse cell and declare the local field
code to be vacuum plus the six one-excitation directional states.  Define

\[
 X_{s,x}={1\over\sqrt6}\sum_{d=1}^{6}
 X_{x,d}\prod_{e\ne d}{I+Z_{x,e}\over2}.
\]

This Hermitian operator maps vacuum to the uniform scalar direction
`|s>=(1,1,1,1,1,1)/sqrt(6)`, maps `|s>` back to vacuum, annihilates the five
transverse one-excitation directions, and preserves the declared seven-state
code exactly.

Supply the bilinear local deformation layer

\[
 V_x(\epsilon)=\exp[-i\epsilon M_x\otimes X_{s,x}],
 \qquad V(\epsilon)=\prod_x V_x(\epsilon).
\]

If `G_0` is the existing matter onsite coin/contact layer together with the
finite field coin, and `G_epsilon=V(epsilon)G_0`, then the exact finite relative
update is

\[
R_\epsilon=G_\epsilon G_0^\dagger=V(\epsilon).
\]

The displayed cancellation and its numerical matrix check are performed on
the `M64 matter x 7 field-code` logical block.  The operator `V(epsilon)` is
explicitly represented on physical M2 below, but this route inherits rather
than freshly reruns the entire baseline coin/contact/field update
intertwiner.  It is therefore a physical local deformation layer, not a new
proof of the full combined `E G = G_physical E` compiler.

No logarithm of the full walk is used.  At the declared parameterization its
Hermitian tangent is

\[
 H_{\rm def}=i\left.\partial_\epsilon R_\epsilon\right|_0
            =\sum_x M_x\otimes X_{s,x}.
\]

The scientific name earned here is **deformation response**.

## Physical support and covariance

The local physical matter support union of the six `B_(x,d)` operators is 18
M2 sites for every tested `L=3,4,5,6`.  Adding the six field M2 sites gives a
24-M2 local deformation block.  Each expanded `B X_s` Pauli term has weight at
most 11: maximum matter `B` weight 5 plus six field sites.

All matter terms commute with every local code check and all three Wilson
operators.  Leakage is zero through held-out `L=6`.  Adjacent matter support
unions overlap on one M2, but their `B` generators commute; distinct local field blocks
also commute.  Parallel deformation layers therefore compose exactly.

The physical field transition is invariant under all direction permutations
induced by the 24 proper-cubic frames.  The connected-code matter operator
passes all `24 x 27 = 648` proper-frame and `L=3` translation tests, including
the bounded framing-gauge repair already required by the physical matter code.

## Exact controls

| Control | Result |
|---|---:|
| Field encoding intertwining | `0.0` |
| Field-code leakage | `0.0` |
| `X_s` Hermiticity residual | `0.0` |
| Maximum field-frame covariance residual | `0.0` |
| Joint local code dimension | `448` |
| `G_epsilon G_0^dagger - V(epsilon)` | `2.349129874285814e-14` |
| Relative-update unitarity residual | `4.271724330598608e-15` |
| `H_def` Hermiticity residual | `0.0` |
| `||H_def||` at `beta=-0.3` | `2.7204339250493117` |
| Common-rephase relative-update residual | `2.3236354937316816e-14` |
| Disjoint parallel commutator | `0.0` |
| Parallel finite-composition residual | `1.4721413199329615e-15` |
| Local-check/Wilson leakage, `L=3,4,5,6` | `0` |
| Frame-translation failures in 648 tests | `0` |
| Contact-response commutator | `0.0` |
| Onsite-coin-response commutator | `0.0` |
| Bilinear source-leg residual | `3.1125870256501347e-15` |
| Bilinear response-leg residual | `0.0` |
| Free Cycle-213 projection residual | `5.584220101197091e-17` |
| Uniform scalar-port derivative residual | `1.3597399555105182e-16` |

Coupling deletion `epsilon=0` returns the exact matter-contact plus finite-coin
baseline.  Charge deletion removes the deformation while retaining the bodies,
their onsite coin, and the ordinary contact law.

## Mass and contact fixture

The actual contact

\[
 W_g=\exp\left[i g {N_x(N_x-1)\over2}\right],\qquad g=0.37,
\]

is identity for `N<=1` and commutes with `M_x`.  The deformation therefore
retains the literal ordinary contact factor, and deletion retains the prior
one-particle mass tests.

At `beta=-0.3` the relevant numbers are

| Quantity | Value |
|---|---:|
| raw vacuum-relative scalar rest phase | `0.15113521805829502` |
| supplied `c^2` | `1/3` |
| analytic/inertial mass `m` | `0.4534056541748852` |
| dispersion mass | `0.4534056690336209` |
| force-response mass | `0.45444242813733504` |

Thus the raw phase is `c^2 m`, not `m`.  Choosing `M_x=mN_x` imports the
Cycle-219 common-cone conversion `m=(raw rest phase)/c^2`.  The mass charge is
not selected by the raw phase alone.  This is a load-bearing normalization
input, not a numerical residual to hide.

## Rephase and reparameterization audit

A common constant rephase of both `G_epsilon` and `G_0` cancels from the exact
finite relative update.  This is stronger than choosing a global logarithm.

A deformation-dependent rephase does not cancel:

\[
 G_\epsilon\mapsto e^{-ia\epsilon}G_\epsilon
 \quad\Longrightarrow\quad
 H_{\rm def}\mapsto H_{\rm def}+aI.
\]

For `a=0.31`, the finite-difference residual against the exact shifted response
is `6.345970398111437e-12`, and the identity shift per dimension is exactly
`0.31`.

Likewise, `epsilon=s lambda` leaves matched finite endpoints unchanged but
rescales the tangent by `s`.  At `s=1.7`, the matched-endpoint residual is
`0.0`, while the tangent scale changes by `1.7`.

Therefore the new construction earns a well-defined finite relative update
for declared endpoints.  It does not earn a deformation-independent zero or
normalization for the tangent response.  An operational calibration—such as a
physical clock or an independently specified interaction standard—would still
be required.

## Bilinear reciprocity boundary

Both legs come from the same Hermitian bilinear operator:

\[
 (I\otimes\langle s|)H_{\rm def}(I\otimes|0\rangle)=M,
 \qquad
 \langle n|H_{\rm def}|n\rangle=m n X_s.
\]

The tested residuals are `3.1125870256501347e-15` and `0.0`.  This earns
algebraic source/response reciprocity of the supplied vertex.  It does **not**
earn matter recoil, a combined continuity equation, reciprocal geometry,
universal clock response, or metric dynamics.

## Cycle-213 and Cycle-216 reductions

The undeformed finite-coin scalar sector reproduces the free Cycle-213 centered
wave equation at `dt^2=1/3`, with residual
`5.584220101197091e-17`.

The deformation derivative maps the field vacuum to the same uniform scalar
direction used by the finite-coin source port, with one-particle coefficient
`m` and residual `1.3597399555105182e-16`.

However, the literal one-field port has the Cycle-215 two-tap forced equation.
For the selected externally supplied constant point injection its scalar
forcing is

\[
 \gamma\rho-\rho=-L\rho/6,
\]

not the direct Cycle-213 term `rho/3`.  The two-tap identity residual is `0.0`;
the finite port-level direct-source mismatch is `0.6322439777544321`.  This
number is not a self-consistent matter-field history or a same-source static
comparison.  Thus this route reproduces the **free** Cycle-213 scalar law but
does not reproduce Cycle 213's direct source insertion under that selected
port/order.

If the Cycle-216 static stiffness action

\[
 K=2I-U-U^\dagger

\]

and zero-mean periodic elimination are separately supplied, the deformation's
scalar source leg is exactly the source direction used there.  The static
projection then reproduces `3 L^+`:

| L | Stiffness residual | `scalar - 3 Green` residual |
|---:|---:|---:|
| 3 | `4.3065361921872157e-16` | `4.906385601649283e-16` |
| 5 | `4.1016060314694323e-16` | `4.087282864087263e-16` |
| 7 held out | `4.552521930955827e-16` | `1.2151562181052388e-15` |

This is a conditional static-action match.  The finite relative update alone
does not derive the `K` action, its pseudoinverse, or the zero-mean boundary
selection.

## Supplied structure

- `beta=-0.3` and the Cycle-219 common-family coin;
- the mass map `m=-3 tan(beta/2)` and the `c^-2=3` phase-to-mass conversion;
- the Cycle-230 ordinary contact `g=0.37` and insertion order;
- the Cycle-269 connected physical-M2 matter code and its local `B` operators;
- six additional field M2 sites per coarse cell;
- the vacuum-plus-one-excitation field code restriction;
- the uniform vacuum/scalar transition `X_s`;
- the bilinear `M_x tensor X_s` vertex;
- the deformation parameter, sign, zero, and normalization;
- the finite acoustic coin;
- the Cycle-216 `K` stiffness when the static comparison is made;
- periodic zero-mean boundary/source data for the static solve.

## Derived versus not earned

Derived on the declared code and fixtures:

- an exact finite relative update;
- a bounded Hermitian physical-M2 deformation response;
- constant 24-M2 local support and maximum expanded term weight 11;
- zero code/Wilson leakage through held-out `L=6`;
- all-24-frame and translation covariance;
- exact parallel additivity/composition;
- common-rephase cancellation;
- preservation of the baseline mass/contact fixture under deletion;
- algebraic reciprocity of the supplied bilinear vertex;
- the free Cycle-213 and conditional static Cycle-216 scalar reductions.

Not earned:

- a deformation-independent response zero;
- a selected deformation normalization;
- the direct Cycle-213 source law;
- exact combined matter-field continuity;
- self-consistent matter recoil;
- universal passive/clock coupling;
- tensor or nonlinear metric response;
- physical energy, stress, or a selected gravitational source.

## Prior-art and novelty boundary

The matter code, contact, mass fixture, finite acoustic coin, free scalar-wave
projection, and static `3L^+` identity are reused repo results.  The new result
is their explicit joining by a bounded physical-M2 vacuum/scalar relative
deformation layer, together with endpoint/rephase/reparameterization controls
and the exact identification of the Cycle-213 source-port mismatch.

No external engine is used or extended.  No uniqueness, broad no-go, minimum
content, axiom pressure, or constitutional conclusion is claimed.
