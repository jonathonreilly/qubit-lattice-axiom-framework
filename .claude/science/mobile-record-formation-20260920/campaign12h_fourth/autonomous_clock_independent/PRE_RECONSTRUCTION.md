# PRE: a genuinely finite clock for the supplied finite-horizon channel

Independent reconstruction, before access to `autonomous_clock_author`.

**Conditional result.** The supplied finite battery and marked collision
premise admits an explicit finite autonomous extension. For each fixed finite
system, horizon T>0 and desired accuracy, one time-independent, finite,
nonnegative total Hamiltonian gives a uniformly accurate reduced channel on
0<=t<=T for all inputs, including arbitrary untouched references. It exactly
preserves the given system-plus-battery free energy. The clock, pure flags,
coherent preparations and an interaction norm that grows with accuracy are
explicit resources. The result concerns one-time channels; it supplies neither
an exact unbinned event-time instrument nor a multitime intervention process.

The clock's natural progress is nonlinear. An inverse program grid and an
explicit correction for the added physical free evolution are essential to
this construction. Both corresponding failed routes are retained below.

## Supplied premise, identities and scope

The mathematical premise is the complete sealed packet
`full_instrument_energy_supply_author`, principal note
`FINITE_ENERGY_SUPPLY_FOR_MARKED_COLLISION_DYNAMICS.md`, SHA256
`6b9c4ae27ee49754e905f0d990b766be94f2c9ee8a624da01208a6da14b20288`,
author seal SHA256
`469d1f35340e2615d7c7e9d4bbad4a18a111fc04bdb49105fb9120cdb0c7ee83`.
`SOURCE_BINDINGS.json` binds local snapshots and the previously verified
instructions. Its battery/collision results are admitted conditional premises
here, not relabeled as independently certified by this new clock calculation.
The premise's scientific scripts were inspected but no campaign builder is
imported into any new control. No new clock-author source, current CHECKPOINT,
or external personal calculation was accessed.

Use units with hbar=1. Fix the actual finite-dimensional system Hamiltonian H
and actual jumps L_mu of either stipulated instrument. A fixed scalar shift
puts the ground energy of H at zero without changing its commutator or any
energy difference. The original positive microscopic star already permits this
choice. Set

```
A(rho) = -i[H,rho],
D(rho) = sum_mu L_mu rho L_mu† - {Gamma,rho}/2,
Gamma = sum_mu L_mu† L_mu,
g = ||Gamma||, h = ||H||, c = 7g²+4hg,
L_GKLS = A+D.
```

Let the battery width be the positive integer b. The supplied construction
has r distinct positive system gaps E_a, r positive finite ladders,

```
H_B = sum_(a=1)^r E_a N_a >=0,
D_B=(b+2)^r,
beta_b = product of the buffered sine profiles on 1,...,b,
<B>_energy = (b+1)/2 sum_a E_a.
```

The r=0 scalar-energy case needs no battery. Every flag has f=1+(number of
actual marks) orthogonal states and zero free Hamiltonian. Blank flags are pure
additional resources. On system, battery and all flags write
`Q=H+H_B`. The premise provides a full finite unitary V(U) for every flag
unitary U, with `[V(U),Q]=0`, no cyclic battery wrap, and, for any sequence
using distinct flags and the same initial beta_b, a prefix channel error

```
eta_b = min(2,8 sin(pi/[2(b+1)])) <= min(2,4pi/(b+1)).       (1)
```

The norm is diamond norm with trace norm, not half trace norm. Thus arbitrary
reference-entangled inputs are covered. The error does not accumulate once
per gate, because the complete conserved-label blocks give an exact
representation of the product unitary. The actual battery can become
correlated; no reset or catalyst-return assumption is made.

For any dt with g dt<=1/2, the supplied collision uses exactly

```
K_0=sqrt(I-dt Gamma),   K_mu=sqrt(dt) L_mu,
```

followed by `exp(-i dt H)` and a unitary completion on its new flag. Denote this
unitary U(dt) and its reduced channel E_dt. The admitted bound is

```
||E_dt-exp(dt L_GKLS)||_diamond <= c dt².                   (2)
```

No energy filtering, altered actual mark, incoherent resolution of a coherent
mark, or changed microscopic jump scale is introduced.

## Inverse clock grid and programmed conserving gates

Choose an integer N>=1 large enough that `gT/sqrt(N)<=1/2`. Set

```
nu = pi/T,
t_j = (2T/pi) arcsin sqrt(j/N),       j=0,...,N,
dt_j = t_j-t_(j-1),                  j=1,...,N.             (3)
```

The largest step is an endpoint step,

```
dt_max = (2T/pi) arcsin(1/sqrt(N)) <= T/sqrt(N).            (4)
```

Indeed, the derivative of `arcsin sqrt(u)` decreases up to u=1/2 and increases
thereafter, with reflection symmetry about the midpoint. Equal-u increments
are largest at the endpoints. The final inequality follows from the convex
function arcsin lying below its endpoint chord on [0,1]. Thus every collision
satisfies the required small-step condition.

Use N blank flags. Let U_j=U(dt_j), V_j=V(U_j), and let
`B_j=V_j ... V_1`, `B_0=I`, on the common finite work space consisting of
system, battery and flags. In particular `[B_j,Q]=0` on the whole space.
The program prefixes and their increments are

```
P_j = exp(+i t_j Q) B_j,      P_0=I,
W_j = P_j P_(j-1)† = exp(+i dt_j Q) V_j.                   (5)
```

All P_j and W_j are unitaries commuting with Q. Equation (5) is a deliberate
free-evolution correction. The collision gates already include the physical
system evolution for their scheduled duration. Adding Q as a term of the
autonomous Hamiltonian requires removing that duplicate evolution from the
program. The battery factor in the correction is also explicit; it is not
silently omitted because beta_b is coherent in battery energy.

## One positive finite clock and one time-independent Hamiltonian

The clock has exactly N+1 orthogonal positions |j>, j=0,...,N. Its bare
Hamiltonian is

```
H_C = nu N/2 I
      +(nu/2) sum_(j=1)^N sqrt(j(N+1-j))
                         (|j><j-1|+|j-1><j|).             (6)
```

This is `nu(J_x+N/2 I)` in the symmetric spin-N/2 representation. Its spectrum
is `0,nu,...,nu N`, so it is finite and nonnegative. Prepare the pure position
state |0>. There is no momentum line, negative unbounded clock spectrum,
truncated nonunitary shift, or periodic boundary wrap.

Define the clock-controlled unitary and programmed Hamiltonian

```
C_P = sum_j |j><j| tensor P_j,
H_prog = C_P (H_C tensor I) C_P†,
H_int = H_prog-H_C tensor I,
H_tot = I_C tensor Q + H_C tensor I + H_int
      = I_C tensor Q + H_prog.                            (7)
```

Equivalently, every forward off-diagonal clock link in (6) is multiplied by
W_j, and every reverse link by W_j†; the diagonal is unchanged. This is a
single fixed finite matrix. The values t_j and gates are stored in its
couplings, not applied by an external switching schedule during the run.
It need not be spatially local or simple to build.

The exact full-space identities are

```
[H_prog,I_C tensor Q]=0,
[H_tot,I_C tensor Q]=0,
H_prog>=0,   H_tot>=0.                                    (8)
```

The positivity follows by conjugation and Q>=0. Since C_P commutes with Q,
H_tot is also unitarily equivalent to `Q+H_C`. Thus preservation of system plus
battery free energy holds for every input, at every physical time, on the
entire finite Hilbert space, not merely on the buffered initial subspace.
Bare H_C need not be conserved separately: it can exchange energy with H_int.
Its energy and the interaction are both counted below. The positive conserved
program term is `H_C+H_int=H_prog`.

## Exact one-time reduced channel

Use the fixed initial environment
`|0>_C tensor beta_b tensor |0>_F1 ... |0>_FN`, independent of the system
input. The following identities also hold tensored with an arbitrary untouched
reference. From (7)-(8) and P_0=I,

```
exp(-it H_tot)(|0> tensor psi)
  = sum_j a_j(t)|j> tensor exp(-it Q)P_j psi,              (9)
```

where a_j(t) is the bare-clock amplitude. An elementary N-spin derivation of
(6) gives

```
a_j(t) = exp(-i nu Nt/2) sqrt(binomial(N,j))
         [cos(nu t/2)]^(N-j) [-i sin(nu t/2)]^j.
```

Therefore on 0<=t<=T the exact clock-position law is

```
p_j(t) = Binomial(N,p(t))[j],   p(t)=sin²(pi t/[2T]).       (10)
```

The work input can be arbitrary and entangled: because each P_j is unitary,
this position law is independent of that input. Tracing the clock removes
cross terms between j. Let Phi_j^B be the reduced system channel obtained from
B_j with the fixed initial battery and all flags blank. Since

```
exp(-itQ)P_j = exp[-i(t-t_j)Q] B_j,
```

and a final battery-only unitary disappears under partial trace, the actual
autonomous reduced channel is exactly

```
Phi_aut(t) = sum_j p_j(t) exp[(t-t_j)A] Phi_j^B
           = exp(tA) sum_j p_j(t) Psi_j^B,
Psi_j^B = exp(-t_j A) Phi_j^B.                            (11)
```

The unitary channel `exp[(t-t_j)A]` is meaningful even when t_j>t. Those
branches do not constitute classical events in the future: j is a quantum
clock position in (9), and (11) describes an unconditioned one-time channel.

At t=T the clock is exactly at j=N, up to an irrelevant global phase, and
(11) gives Phi_aut(T)=Phi_N^B. There is no leftover physical free evolution
at that endpoint. The same cancellation holds before discarding flags, so the
complete discrete marked collision history at T inherits the premise's
eta_b bound. This endpoint observation alone would not prove the uniform-time
claim that follows.

## Uniform physical-time and reference-stable estimate

Let `Psi(t)=exp(-tA)exp[t(A+D)]`, an interaction-picture CPTP channel. The
exact derivative is

```
Psi'(t) = exp(-tA) D exp[t(A+D)].
```

Unitary channels are complete trace-norm isometries, and the GKLS semigroup is
completely trace-norm contractive. With `||D||_diamond<=2g`,

```
||Psi(s)-Psi(t)||_diamond <= 2g |s-t|   (s,t>=0).           (12)
```

There is no extra h in this clock-timing term. This cancellation is another
reason to keep the added free evolution explicit.

Telescoping the variable collision steps using (2), and then using the common
battery bound (1), gives every prefix

```
||Phi_j^B-exp(t_j L_GKLS)||_diamond
 <= eta_b+c sum_(k<=j) dt_k²
 <= eta_b+c T dt_max.                                     (13)
```

Conjugation by `exp(-t_j A)` leaves this error unchanged. No accumulating
independence assumption about the battery or flags enters (13).

It remains to control the random inverse clock time uniformly, including
0 and T. Put q=J/N where J has (10), and theta(p)=arcsin sqrt(p). For
0<p<1, the squared chord between the unit vectors
`(sqrt(1-q),sqrt(q))` and `(sqrt(1-p),sqrt(p))` obeys

```
E[(sqrt(q)-sqrt(p))²] <= Var(q)/p = (1-p)/N,
E[(sqrt(1-q)-sqrt(1-p))²] <= Var(q)/(1-p) = p/N.
```

Thus its expected squared length is at most 1/N. The angle difference d is
in [0,pi/2], and its chord is `2sin(d/2)>=2sqrt(2)d/pi`, by concavity of sin
on [0,pi/4]. Applying Cauchy-Schwarz and (3),

```
E|t_J-t| <= T/sqrt(2N).                                   (14)
```

At p=0 or 1 the random position is deterministic and this difference is zero,
so the same bound covers the endpoints without a singular division. This is
an analytic bound for all t; a mesh of numerical times is not its proof.

Combining (11)-(14) gives the promised single-environment family:

```
sup_(0<=t<=T) ||Phi_aut(t)-exp(t L_GKLS)||_diamond
 <= min(2, eta_b+c T dt_max+sqrt(2)gT/sqrt(N))
 <= min(2, eta_b+[T²(7g²+4hg)+sqrt(2)gT]/sqrt(N)).           (15)
```

The very same H_tot and initial environment work for every physical time in
this interval and every input/reference state. For a desired tolerance z>0,
one sufficient finite choice is eta_b<=z/2 and

```
N >= max(1,4g²T²,4[T²(7g²+4hg)+sqrt(2)gT]²/z²),            (16)
```

rounded upward. For example `b+1>=8pi/z` suffices for the first condition.
These are loose sufficient resources, not lower bounds or an efficient design.
The g=0 purely unitary case of course does not need this machinery.

## Energy, coherence, purity and interaction resources

The explicit resources of this construction are:

| Resource | Sufficient supplied value |
| --- | --- |
| Clock Hilbert dimension | N+1 |
| Clock free spectrum | `0,nu,...,nu N`, with nu=pi/T |
| Initial clock mean energy above its ground | `nu N/2=pi N/(2T)` |
| Initial clock energy variance | `nu²N/4` |
| Battery dimension | `(b+2)^r` |
| Prepared battery mean energy | `(b+1)sum_a E_a/2` |
| Battery maximum free energy | `(b+1)sum_a E_a` |
| Blank pure flags | N flags, each dimension f and zero assigned free Hamiltonian; joint dimension f^N |
| Total Hilbert dimension | `d_S (b+2)^r (N+1) f^N` |
| Programmed clock term norm | `||H_prog||=nu N` |
| Interaction norm | `||H_int||<=nu N` |
| Initial interaction mean | Exactly zero for every system input |

For the interaction bound, subtract the scalar `nu N/2` before taking the
difference in (7): `H_int=C_P(nu J_x)C_P†-nu J_x`, so its norm is at most
`2nu||J_x||=nu N`. This does not claim a strength bound independent of
accuracy. The total norm is at most `h+(b+1)sum E_a+nu N`.

The bare clock state |0> is coherent in the H_C energy basis, with binomial
energy probabilities `binomial(N,k)/2^N`; it is not a stationary clock-energy
mixture. The sine-profile battery also contains energy coherence. These pure
preparations and the precisely supplied spectral couplings are not derived
from thermal equilibrium or a native dynamics. A zero flag Hamiltonian does
not make preparing and resetting pure flags thermodynamically free. No reset,
replenishment, or physical lifecycle cost is claimed.

Because the interaction has no diagonal clock block, its initial mean is
zero. The expectation of `H_C+H_int` remains `nu N/2`, while its two terms
can change separately. The clock term is positive; the bounded interaction
can have either sign. Exact conservation of Q separately implies

```
<H>_t-<H>_0 = <H_B>_0-<H_B>_t.                            (17)
```

Thus the finite battery, not an uncounted clock-energy decrease, supplies the
system energy in this model. The construction does not declare that increase
to be heat. At fixed finite H, (15) also gives the uniform moment bound

```
|<H>_aut(t)-<H>_GKLS(t)| <= h times the right side of (15). (18)
```

For a varying microscopic model, h can diverge, so channel accuracy must be
chosen to control this moment. For example, the supplied star premise gives
`h=O(C²)`, `g=O(C)`, `C=S(S+1)`, uniformly in the electric parameter. A loose
sufficient choice for error O(C^-2) is b=O(C²), N=O(C^10), at fixed T. It
has battery prepared energy O(C^4), clock mean energy and interaction bound
O(C^10), and O(C^10) pure flags. Equation (18) then has error O(1), which is
o(C). This illustrates how expensive the sufficient autonomous account can
be; it is not an optimal scaling or a lower bound. Programs and spectral
batteries are rebuilt for their supplied model; a uniform upper estimate does
not mean one unchanged Hamiltonian implements every electric parameter.

## Preserved failed routes and nonclaims

**Uniform gate durations on the uncorrected nonlinear time grid.** Perfect
endpoint transfer is insufficient. If the clock (6) is assigned equal
collision steps T/N, its typical completed duration is
`T sin²(pi t/[2T])`, rather than t. With the pump
`L=sqrt(gamma)|1><0|`, the exact ground-state survival for the naive binomial
mixture is `(1-p(t)gamma T/N)^N`, tending to
`exp[-gamma T p(t)]`. At t=T/4, p(t)=(2-sqrt(2))/4, which differs from 1/4.
This gives a nonzero limiting trace-distance error even though both endpoints
are correct. Equation (3), not merely increasing N, corrects this route.

**Omitting the free-evolution correction.** If the program uses V_j in place
of W_j, the endpoint reduced channel is
`exp(TA) Phi_N^B`. It contains an extra physical free evolution. In the
phase-covariant pump example the phase is doubled; in a general noncommuting
model one should not replace the result by a guessed generator `2A+D`.
The controls retain a nonzero endpoint reference-state error for the omitted
correction as N grows. Equations (5) and (11) resolve this failure explicitly.

**Uniform channels do not imply uniform generators at t=0.** At fixed finite
N, the initial mean interaction operator is zero, so the autonomous initial
reduced derivative is A, without D. The first clock transition probability is
of order t². The GKLS derivative is A+D. This is compatible with (15): the
small-time boundary layer shrinks as N and the interaction norm grow. No
convergence of derivatives, initial dissipative power, or conditional rare
outputs follows from this uniform one-time channel estimate.

**Finite horizon and recurrence.** At time 2T the bare clock propagator is the
identity because its energies are integer multiples of pi/T. Accordingly the
program propagator is also the identity and `exp(-i2T H_tot)=exp(-i2T Q)`
on the work space. Previously created flags are coherently undone if nothing
intervenes. The same finite model is therefore not a permanent irreversible
reservoir or an all-time GKLS dilation. The theorem covers the specified
horizon only.

**Flags, event times and interventions.** The final discrete marked collision
history is meaningful and has the premise's approximation bound. It is not
an exact continuum record with unbinned jump times. At intermediate physical
times the clock is in a coherent superposition of prefixes; reading it or
old flags can change subsequent dynamics. Uniform diamond convergence of
one-time reduced maps does not establish convergence under arbitrary
interventions, a quantum process tensor, conditional future histories, or
uniform normalized rare-event states. These require separate estimates.

This is an engineered finite-horizon dilation of a supplied law. It adds no
framework axiom, selects no electric completion or physical Hamiltonian, and
establishes no native reservoir, empirical particle law, locality theorem,
infinite-volume limit, or universal physical selection result. It is a
checked constructive route within its assumptions, not evidence that its
large resources occur naturally.

## Independent controls, failures and recovery

`exact_clock_control.py` constructs, without a campaign import, a complete
96-dimensional finite clock/work space with a two-level system, finite positive
battery and two pure flags. The jump is `sqrt(gamma)|+><0|`, which is not an
energy eigenoperator. Exact symbolic identities check every gate's full-space
unitarity and energy conservation, the full programmed conjugation, positivity
via the exact clock spectrum, initial clock resources, and the physical
free-evolution cancellation. The omitted correction is detected exactly.

`finite_clock_dynamics_control.py` constructs one sparse time-independent full
Hamiltonian in each of three larger finite cases, then directly exponentiates
it on all input columns. A separately reduced history expression is compared
to the full channel, including a maximally entangled reference test. At the
largest case, dimension 17024, the maximum full-H/history matrix-entry
residual is below 4e-15. Both separate free-energy conservation and the
clock-plus-interaction account are checked at every sampled time. These are
finite corroborations of the analytic all-input theorem, not a sampled proof
of uniformity.

`clock_uniformity_control.py` independently uses exact binomial and pump-channel
formulas through N=16384. It checks the inverse-grid and Hellinger estimates,
complete channel matrices, and both persistent wrong routes. In its fixed
example the corrected maximum sampled reference-input error decreases from
about 0.04051 at N=16 to 0.001323 at N=16384. The naive equal-step error at
T/4 tends to about 0.14733 on a ground-state input; the omitted-counterphase
endpoint reference error tends to about 0.62770. These failures are preserved
as mathematical counterexamples to those routes.

Complete result tables, stdout, stderr and a source-bound execution receipt
are saved. No unresolved control execution failure occurred. The author clock
comparison remains open until this PRE packet is sealed. No commits, PRs,
audit decisions, publication changes or axiom adoption are part of this work.
