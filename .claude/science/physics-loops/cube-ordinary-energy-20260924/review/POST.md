# POST comparison: ordinary mean and mesoscopic energy layer

This POST follows the immutable independent PRE, SHA-256
`1f6e944205553c4941ba851c6dde270b06b444606ae15d51e66324ea99512cb1`,
sealed before root disclosure. No PRE file has been changed. The root inputs
were frozen in `POST_sources/`; exact identities and revalidation are in
`POST_SOURCE_PINS.json` and `POST_SOURCE_VALIDATION.log`.

## Source-bound disposition

No consequential mathematical defect was found in the following complete
released arguments, under their declared conditional imports:

- `UNSCALED_MEAN_PERSONAL_DERIVATION.md`, SHA-256
  `d03bf3b34e120d7c85dd7636de9317c2c44b59a2da70aa43d4499c2b698d92ae`.
- `MESOSCOPIC_ENERGY_LAYER_PERSONAL.md`, SHA-256
  `27d130bb494f1a7dde240c88e00f669961a07539b59890274655afda38e096d7`.

I confirm the conditional ordinary full-ensemble mean convergence, including
the stronger lower endpoint condition `a_e/epsilon^(6/5)->infinity`, and the
relative variance statement only in the specified mesoscopic window
`tau_e->infinity`, `epsilon tau_e->0`. No repair of a scientific formula or
hypothesis is requested. No fixed-positive-time variance conclusion follows.
This is selective scientific checking; it grants no retained audit status or
physical selection of the Hamiltonian, compensation, preparation or instrument.

The first candidate's central proof was already independently reconstructed in
PRE. The mesoscopic supplement was first read after PRE was sealed: the
verification below is a new POST derivation from the previously established
bounds and the conditional actual-input lower tail, not a claim that those
stronger statements had been sealed independently in PRE.

## Complete candidate comparison

The phase H^2 estimate agrees with PRE section 1. In particular, the proof
needs and checks all of the following: at an exceptional phase the zero modes
are dark; the kernel is reducing and semisimple; the complementary block has
strictly negative spectral real parts; the analytic slow cluster derivative
vanishes after compression because the entire dark-dark block is zero; and
that slow block inherits the uniform Gaussian-type semigroup bound. These
facts work at multiplicities two and four. Duhamel phase differentiation uses
products at the same phase whose time parameters sum to tau, so no lost
exponential factor is hidden. The order-two L2 norm is O(tau^(-1/4)) in the
five physical Gauss coordinates. A fixed measure-zero fiber is never used as
a physical input.

The growing-time comparison is an actual Duhamel estimate. Spin-box exclusion
is included in the weighted O(C^(-1)) error; the scalar high-band phase is
removed only after exact block separation. The exact block semigroup has a
common all-time norm bound because the physical no-event propagator is a
contraction and its similarities are uniformly conditioned. Thus no finite-spin
spectral gap or invalid substitution into a compact-time limit is required.

The root proves a stronger initial second-band bound than PRE needed:
`||E_2 phi||=O(epsilon^4)`, rather than the sufficient O(epsilon^3). I checked
its proof directly. The grade-two row of the exact Riesz projector has leading
blocks `epsilon^2 F^2/2`, `-epsilon F`, and identity. These have respectively
parity even, odd, and even. The diagonal epsilon-squared imaginary loss cannot
alter these minimal-order coefficients. Applying that row to the actual
unnormalized birth gives precisely

    epsilon^3 [j F^3/6 - F j F^2/2 + F^2 j F/2] Omega.

The local nilpotence and remote-commutation identities cancel it, as my PRE
primitive-word implementation independently checked on all 36 marks. The
remaining projected numerator is odd by W parity and is O(epsilon^5).
Since the exact E_2 range is a graph over Pi2 with uniformly bounded graph
constant, bounding its Pi2 component bounds the entire vector. Division by
the actual nonzero O(epsilon) birth norm proves the claimed O(epsilon^4).
This also explains why taking the old O(epsilon^2) normalized bound at face
value would have left an order-one energy obstruction.

The polynomial-weight low-domain argument is sufficient. My PRE used the
stronger exponential weight, but that is unnecessary for the stated mean.
The root's `w=1+sum E_e^2` algebra controls both the local operators and their
adjoints, so the polar factors and exact-cluster remainders are controlled in
that weighted algebra. KD commutes with w. The common interaction-picture
Dyson series therefore propagates D-domain bounds and gives strong convergence
uniformly on bounded time intervals. The expectation estimate in equation (22)
is valid by self-adjointness on the common D domain; it is not an assumption
that norm convergence alone controls an unbounded observable.

Finally the ordinary-coordinate replacement has the correct epsilon power:
`||y_0-a_0||=O(epsilon^3)` and `||H_low||=O(epsilon^(-2))` give an O(epsilon)
expectation error. This uses the finite-spin global norm solely for that small
coordinate mismatch. It does not demand a weighted estimate for the whole
fast microscopic vector. Hermitian spectral separation removes energy cross
terms, and the terminal N=8 energy is zero, so full-ensemble accounting is
maintained.

## New POST derivation of the relative window

Let `f_i(tau)=||exp(tau L)r_i||^2`. The conditional sharp-tail lower and upper
bounds are `c(1+tau)^(-5/2)<=f_i<=C(1+tau)^(-5/2)` for the three actual inputs.
The absolute bound already derived in PRE/root is

    ||a_1(epsilon^2 tau)/epsilon - exp(tau L)r_i||
       <= C epsilon^2[1+(1+tau)^(3/4)],

after removing the common scalar phase. Dividing by the lower bound for the
rotor norm gives a relative vector error at most
`C epsilon^2(1+tau)^2`. Therefore it is o(1) along every growing sequence
with `epsilon tau->0`. The Hermitian-coordinate error, divided by the same
leading amplitude, is at most `C epsilon^2(1+tau)^(5/4)` and also vanishes.
The first Hermitian band is `delta epsilon^(-4)[I+O(epsilon^2)]`, so

    E_1(epsilon^2 tau_e)
        = delta epsilon^(-2) f_i(tau_e) [1+o(1)],
    M2_1(epsilon^2 tau_e)
        = delta^2 epsilon^(-6) f_i(tau_e) [1+o(1)].

These are relative first-band statements. Their uniform version follows
whenever the maximal `epsilon(1+tau)` in the considered family tends to zero.
No total-mean relative statement is needed or valid when the total crosses zero.

For the second band, exact contraction plus the projector comparison give
Hermitian amplitude O(epsilon^3) at all times, hence mean O(epsilon^2) and
second moment O(epsilon^(-2)). The low coordinate has bounded `||D a_0||` and
bounded H4, so `||H_low a_0||=O(1)` on [0,T]. Replacement by y_0 costs
`O(epsilon^(-2))O(epsilon^3)=O(epsilon)` in this energy-vector norm. Therefore
the low second moment is O(1). This is stronger than, and must not be replaced
by, a direct operator-norm comparison of H_low squared expectations.

The ratios of the other contributions to the leading first-band second moment
are bounded by constants times

    epsilon^4/f_i(tau_e),       epsilon^6/f_i(tau_e).

Both vanish when `tau_e=o(epsilon^(-1))`, by the lower tail. The squared total
mean has ratio at most

    C[epsilon^2 f_i(tau_e)+epsilon^6/f_i(tau_e)] ->0.

Thus the full variance has the same relative asymptotic as M2_1 in this window.
The time itself tends to zero: `t_e=epsilon^2 tau_e=o(epsilon)`. A fixed positive
physical time instead has `tau=t/epsilon^2`, for which `epsilon tau=t/epsilon`
diverges and the relative error estimate does not vanish. The fixed-time
variance remains open.

## New POST derivation of the epsilon^(6/5) layer

The first-band mean is of order `epsilon^(-2) tau^(-5/2)`. Equating its scale
to one gives `tau` of order `epsilon^(-4/5)` and physical time of order
`epsilon^(6/5)`. This is a two-sided order statement, with no asymptotic
prefactor imported beyond the available rotor tail.

If `t_e/epsilon^2->infinity` and `t_e/epsilon^(6/5)->0`, the relative window
holds automatically and the positive first-band mean diverges. The low mean
is bounded and the second-high mean vanishes, so the ordinary full mean
consequently tends to positive infinity.

At `t_e=x epsilon^(6/5)`, fixed x>0, the high mean stays between positive
constant multiples of `x^(-5/2)`. The variance is of order
`epsilon^(-4)x^(-5/2)`, with fixed positive parameter-dependent constants.
This does not assert that the total mean is positive: its bounded low part
can have either sign.

For the stronger uniform late-layer conclusion, put
`L_e=a_e/epsilon^(6/5)->infinity` and choose the comparison fast time

    tau_e=epsilon^(-4/5) min(sqrt(L_e),epsilon^(-1/10)).

Then `tau_e->infinity`, `tau_e epsilon^(4/5)->infinity`,
`epsilon tau_e<=epsilon^(1/10)->0`, and `epsilon^2 tau_e<=a_e` eventually.
Thus the first-high energy tends to zero there by the relative result.
Its exact Riesz-component norm cannot increase at later physical times.
The Hermitian component satisfies

    ||P_1 v||^2 <= 2||E_1 v||^2+O(epsilon^6),

so the extra term contributes O(epsilon^2) after multiplication by
`epsilon^(-4)`. This explicit inequality also accounts for the otherwise
implicit projector-comparison cross term. Uniform low convergence on [0,T]
and uniformly vanishing second-high mean complete the stated convergence on
`[a_e,T]`. This construction never applies the relative expansion at a fixed
positive physical time.

## Evidence coverage and limits

I read both complete root arguments, both seals, the finite-S control source,
its JSON, stdout and stderr. Every member of the author/supplement seals was
hash-verified. The abandoned route record was hash-verified only; its contents
were unnecessary and were not used. The reused previous matrix-builder hash
was checked, but its implementation was not re-reviewed here. The root
explicitly calls that control reused author evidence; I do not promote it to
independent evidence. The two SciPy FutureWarnings in stderr do not indicate
a failed computation or a mismatch of the displayed numerical results.

The PRE contains an independently written primitive physical-word computation
and the load-bearing analytic derivation. Additional POST symbolic controls
check the generic Riesz-row denominators and parity, their independence from
the leading diagonal loss, and the layer/variance exponent arithmetic. These
are narrow checks, not a numerical certification of the continuum theorem.
All outputs and verification limitations remain in the packet. The primary
self-contained publication control, any repository checks, final publication
source review, and formal audit are outside this dispatch and are not claimed
complete here.
