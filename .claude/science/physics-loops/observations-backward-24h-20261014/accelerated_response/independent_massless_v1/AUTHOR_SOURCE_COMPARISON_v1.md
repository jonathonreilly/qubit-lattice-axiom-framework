# Focused author-source comparison after independent massless freeze

Reviewer `/root/inertial_response_check`. Root remains scientific author.
This supplement follows the independently frozen derivations, 18 pure-force
controls and 27 joint field/force controls. `INDEPENDENT_REVIEW_v1.md` and
`INDEPENDENT_IDENTITY_v1.json` were written before reading the new author
notes/code and remain unchanged. The source comparison is not a formal audit,
canonical delivery review, physical data test or full count-model validation.

I read both complete author notes and the complete new Gram program at these
identities, then rechecked the identities after the narrow code checks:

| Author artifact | SHA-256 |
| --- | --- |
| `JOINT_CLOCK_FORCE_WORKING_v2.md` | `7ac81b681804460dfb277b4e2fa369b69ed138b68f833d103a9e547f81de7f7c` |
| `ACCELERATED_RESPONSE_WORKING_v1.md` | `80d40337d01210ff51847fd56b32fb4b6332e286ac1461a1c10f9e16d0e3ed04` |
| `joint_gram_controls_v2.py` | `4bd9f3ba99369437ceefedb803bc6aae5d4d552c06b5d7e7a00b2501ab62a975` |
| `JOINT_GRAM_RESULTS_v2.json` | `48ecd654fe086c5307bc7f6c967c9915dd309596d2c231274db2c255d01a60bd` |

No unresolved scoped mathematical or implementation discrepancy was found in
the massless joint Gram. The independently identified constant-background
qualification is now explicit in the author's v2 proof. The original independent
prechecks and the earlier author failure remain preserved; neither is relabeled
as if it had always contained the later repair.

## Proof, factors and domains

The author's phase variable `phi_n=s-n.x` and vector `b_n` coincide with my
frozen `tau_n` and `B_n`. The author uses a positive exponential convention;
its plane-wave force coefficient is therefore `+ik A(n-u)`, whereas my negative
exponential convention gives `-ik A(n-u)`. Both correctly give the same real
arrival amplitude `C-partial_tau H` after integration by parts. The stated
`1/(8pi^2)` angular/time Gram is consistent with the real Hilbert norm `2E`.
The pure-force expression and the single-path joint expression exactly match
the independent derivations; no factor two, force sign or laboratory/rest-energy
substitution is missing.

The C2 path with a uniform subluminal margin, bounded acceleration, compact H1
force weight with zero traces and compact L2 direct weight gives the required
H1/L2 arrival functions. No jerk or derivative of the direct coefficient is
required. The formulas define the extension from initially smooth energy data;
they do not presume arbitrary finite-energy point traces. Multiple paths are
summed in one common arrival coordinate before the Gram is formed. Their cross
terms cannot generally be evaluated at equal coordinate time or replaced by
independent field-energy budgets.

The author's sharper bound on b is valid. The exact algebraic identity

    (1-n.u)^2-(1-|u|^2)|n-u|^2=(n.u-|u|^2)^2

implies `|b|<=sqrt(1-|u|^2)<=1`. In differentiating b, the three terms are bounded
respectively by `2 beta a/(1-beta^2)`, `(1+beta)a` and `a/(1-beta)`. Their sum
is exactly the author's `D_beta a`. Minkowski and `d>=1-beta` give its sufficient
single-path envelope, including the direct coefficient. Squaring the sum of
individual norm bounds is a valid, generally nonsharp multipath envelope with
one common field-energy budget. This is stronger than the loose coefficient
bound in my initial independent precheck; the exact norm itself is identical.

The anchored homogeneous-H1 Sobolev representative in L6 fixes the constant
background. The author correctly retains the alternative requirement
`sum integral c_A ds=0` if arbitrary added constants are admitted. That
qualification is an explicit premise or an observable cancellation to prove,
not a derived state selector. The source makes no claim that actual radio
contrasts automatically satisfy it. Its explicit restriction to a massless free
field is appropriate; the inertial all-mass enclosure has not been carried over
to accelerated paths.

## Interaction with the supplied one-way and adjoint model

I also checked the displayed first-order kinematic algebra, without taking over
authorship or asserting a numerical validation of the full physical model.
Linearizing the null relation gives
`D_r delta s-D_e delta t=n.(xi_r-xi_e)`. Fixing receiver proper time gives
`delta s=-eta_r/ell_r`, and the source phase shift
`eta_e+ell_e delta t` produces the displayed chi, including both proper-clock
terms and the position signs. Dividing the chi difference by the fixed receiver
proper interval is consistent with the stated normalized count definition.
This depends on the supplied conformal flat null model, constant proper emitter
frequency and absence of the additional link phases explicitly excluded there.

The augmented state's proper-clock row follows by differentiating
`A_b sqrt(1-|u|^2)` with fixed background: its velocity term is
`-A_b gamma u.delta u` and its field term is `ell alpha h`. The adjoint identity
then gives `W=alpha lambda_v`, `c=alpha ell lambda_eta`, the initial-state row and
the endpoint jumps with the stated signs. The initial epoch is strictly before
the endpoints; an endpoint at the initial epoch is separately assigned its
initial-state coefficient.

The regularity argument is a valid sufficient route to the massless theorem:
position/clock endpoint rows have no velocity component, so lambda_v has no
jump; lambda_eta may have jumps, which leave c in L2. Bounded piecewise
coefficients give continuous piecewise H1 lambda_v. The final velocity-adjoint
trace is zero. An actual contrast annihilating the full initial-state row also
makes its initial velocity-adjoint trace zero, allowing compact H1 extension.
This requires the stated full initial-state cancellation and an actual rank
calculation; merely canceling constant velocity is insufficient. Velocity
endpoint atoms could violate the condition and are correctly left outside it.

The result still supplies a conditional sensitivity operator for a chosen
reference model. Actual Cassini two-way/transponder response, external scalar
couplings, media/electronics, calibrated worldlines/clocks, error bounds and an
energy supplier are open. No empirical or nonlinear error certificate follows
from this algebra check. Root's later full augmented count-adjoint work is not
part of the four-source unit checked here.

## Complete program reading and narrow execution

The program's rest, inertial and curved paths have consistent derivatives. Its
curved fixture is uniformly subluminal even by the conservative global component
bound `sqrt(.16^2+.20^2+.21^2)<.34`. Both vector windows and their derivatives
are consistent, compact and smooth at the endpoints. The density routine
implements `c-partial_s(b.W)`, including b's acceleration derivative. The
original-wave routine instead integrates the unsimplified clock and force
coefficients against the laboratory phase. This is a useful separate
representation of the same mathematics. Its positive-exponential signs and
radial/angular normalization agree with the independent Fourier derivation.

The multipath routine partitions the common arrival interval at every shifted
support endpoint, independently inverts the monotone phase for each path and
zeroes inactive intervals before summing. The stationary-location shifts in its
spectral version have the corresponding phase sign. The intentionally wrong
independent-path and equal-coordinate versions are discriminating fixtures,
not alternative valid formulas. Finite quadrature comparisons are accurately
labeled diagnostics rather than certified truncation enclosures.

After freezing independent evidence, I extracted only the author's elementary
fixture/density functions and ran 38 narrow comparisons. Five-point numerical
derivatives independently checked x', u', W' and `partial_s(b.W)` at additional
points and directions. Phase-equation residuals checked the nine-step inverse
on additional multipath quadrature nodes, where strict monotonicity guarantees
uniqueness. All 38 comparisons passed; the largest equality discrepancy was
`2.880806704297356e-12`. These are author-code implementation checks and remain
separate from the 45 pre-author-access independent controls. The complete author
suite was not rerun.

The recorded v2 result contains 15 author checks, all consistent with their
stored predicates/tolerances. Its source hash matches, stdout is byte-identical
to the result JSON and stderr is empty. The previous v1 stopped at the separated
path refinement check: `1.5583164980625952e-8` exceeded the original `3e-10`
tolerance. I read and bound that original stderr and the saved angular
diagnostic. The exact source diff changes only the base/refined angular
resolutions and output version. It does not relax the tolerance or change a
formula. The v2 refinement discrepancy is `1.6177466310995925e-10`, below the
same tolerance. The initial failure therefore remains visible as a quadrature
resolution failure, not a rejected physical candidate or a retrospectively
successful run.

Exact identities, recorded author outputs, preserved failure hashes and the 38
new narrow comparisons are in `AUTHOR_SOURCE_COMPARISON_RESULTS_v1.json` and its
separate identity record. All writes by this reviewer are confined to this
independent directory. No author source, index, branch, campaign state, lock,
publication, raw observation or audit surface was changed.
