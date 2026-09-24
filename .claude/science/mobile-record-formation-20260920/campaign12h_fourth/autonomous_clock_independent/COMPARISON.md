# Comparison of the finite traveling clock with the sealed spin-clock PRE

**Finding:** no mathematical correction to the released traveling-clock theorem
is required at its stated finite-horizon, one-time reduced-channel scope. The
velocity endpoint term, physical-time clipping, finite-chain tail, system-only
counterphase, all-reference mixture estimate and positive clock/program energy
are supported by independent derivations below. The initial-derivative and
power limitation is made explicit; the theorem must not be read as asserting
that stronger convergence.

The independent spin-clock PRE remains a distinct construction. Its seal is
`d015c9245087ce39c102c61d859171c58ccd5b4a2ea4d25ea2b9bc37a61493ad`.
All 38 PRE bindings, including 17 source snapshots, remain unchanged. Neither
construction is an audit verdict, native-law selection, or publication/landing
approval.

## Sources, provenance and independent scope

The released principal note is
[AUTONOMOUS_FINITE_CLOCK_FOR_THE_ORIGINAL_REDUCED_DYNAMICS.md](comparison_sources/autonomous_clock_author/AUTONOMOUS_FINITE_CLOCK_FOR_THE_ORIGINAL_REDUCED_DYNAMICS.md),
SHA256 `bf11561362dfd8d4f0298be946efa9ec8c8e198a0f3b2b01e4b811537120ff5f`.
Its complete author seal has SHA256
`dcff32f98d26b2cddfdcfa8feeb4dc8907b9174f54f0b51f3ec0cda0a9fa6c4e`.
The full note, both current scientific scripts, retained earlier clock script,
planning/development records, receipt, and necessary released dependency
arguments were read. All 30 comparison sources are authenticated in
[COMPARISON_SOURCE_BINDINGS.json](COMPARISON_SOURCE_BINDINGS.json).

The previously sealed battery/collision theorem remains a supplied premise,
with its separate independent comparison bound by the author seal. The present
new calculations do not import any root clock or model implementation. The
original-star computation uses this worker's earlier source-blind, sealed
local operator matrices and a new spectral clock propagator. Root replay is
separate consistency evidence and is not labeled independent.

## 1. The velocity variance comes from the zero-extension endpoints

Use the root's orientation `T|x>=|x+1>`,
`K=2JI-J(T+T†)`, and `V=iJ(T-T†)` on the integer line. Write

```
a_j=sqrt(2/(w+1)) sin(j theta),  j=1,...,w,
theta=pi/(w+1),
chi_x=i^x a_(x+w+1),           x=-w,...,-1,
```

and zero-extend a and chi. The sine recurrence implies that
`(V-2J cos(theta))chi` vanishes on the packet itself. Its only nonzero
components are

```
x=-w-1: J i^(-w-1) a_1,
x=0:    J a_w.
```

They are orthogonal to chi. Therefore the mean and variance are exactly

```
<V>=2J cos(theta),
Var(V)=J²(a_1²+a_w²)=4J² sin²(theta)/(w+1).                (C1)
```

This is a direct operator-action reconstruction of the load-bearing endpoint
term. It does not treat the finite sine envelope as a bilateral velocity
eigenstate. Dropping those two components would give the wrong zero variance.

The second-neighbor identity also follows without importing a stored value:

```
S_2=sum_j a_j a_(j+2)
   =2cos(theta)sum_j a_j a_(j+1)-sum_(j=1)^(w-1) a_j²
   =2cos²(theta)-1+a_w²
   =cos(2theta)+2sin²(theta)/(w+1).                         (C2)
```

The symmetric envelope has `<X>=-(w+1)/2`. Its support has diameter w-1, so
`sd(X)<=(w-1)/2`. The new exact control verifies (C1)-(C2), including their
nonzero endpoint residuals, for five widths with exact arithmetic.

On the integer line, `i[K,X]=V` and `[K,V]=0`. The shifts preserve the
finite-support core, their commutators with X are bounded, and the resulting
unitary preserves the finite-position-moment domain. Thus
`X(t)=X+tV` on the packet's domain is legitimate. On a finite path, however,

```
[K_M,V_M]=2iJ²(P_right-P_left),                             (C3)
```

which is not zero. The root proof correctly applies the linear Heisenberg
identity only to the infinite comparison problem, and treats the finite path
separately. The independent exact control retains (C3), so the finite and
infinite statements are not conflated.

## 2. Physical-time clipping and finite-chain error

With `2J cos(theta)=1/tau`, the infinite packet's mean is
`-(w+1)/2+t/tau`. No assumption of independent position and velocity is
needed: the Hilbert-space triangle inequality on centered vectors gives

```
sd(X+tV)<=sd(X)+t sd(V).
```

Adding the fixed initial mean lag yields

```
tau E|X(t)-t/tau|
 <=tau[(w+1)/2+(w-1)/2]+t tau sd(V)
 =tau w+t tan(theta)/sqrt(w+1).                            (C4)
```

For 0<=t<=T=n tau, the target coordinate t/tau belongs to [0,n]. Projection
onto that interval cannot increase its distance. Hence the root's clipped
physical-time estimate follows, including both endpoints. At t=0 the actual
clipped error is zero; the positive right side is only a conservative bound.

For the finite path `[-w-R,n+R]`, use integer R and zero embedding in the
line. Every adjacency walk of length less than R starting in the packet is
unchanged. In fact the first possible outgoing path on the left has length
R+1, so the root's stated threshold is conservative. The new exact power
control checks equality through R and a nonzero discrepancy at R+1.

Remove the irrelevant scalar clock phases before comparing propagators.
Both adjacency norms are at most two. Uniformly for t<=T, a=2JT gives

```
||chi_M(t)-chi_infinity(t)|| <= 2 sum_(m>=R) a^m/m!
                            <= 2 exp(a) a^R/R!.            (C5)
```

The second inequality uses `R!/(R+k)!<=1/k!`. Pure-state trace distance is
at most twice the aligned vector distance. The same controlled prefix
unitary acts on both comparison states and does not depend on the system
input. It preserves the vector estimate even after adjoining a reference.
Partial trace then gives exactly

```
b_R=min(2,4 exp(a) a^R/R!).                                 (C6)
```

This is an all-input isometry estimate, not a probability tail inferred from
a single state. The infinite clock is only a comparison device.

For R>=8a, the factorial lower bound gives

```
log[exp(a) a^R/R!] <= a+R log(ea/R)
                  <= (9-8log 8)a < -7a.
```

Thus the root's `b_R<=4exp(-7a)` is valid. Because
`a=n/cos(theta)<=2n` for w>=2, choosing R=ceil(8a) leaves
`M=n+w+2R+1=O(n+w)` genuinely finite. The new control also compares finite
propagation with the independent infinite-chain Bessel kernel. Those samples
corroborate the analysis; floating-point samples are not claimed to verify
errors of order 10^-900 or smaller.

## 3. The two counterphase conventions are both valid

Let `Q=H+H_R`, `B_k=V_k...V_1`. The root uses

```
W_k=exp(+ik tau H)V_k exp[-i(k-1)tau H],
G_k=exp(+ik tau H)B_k.                                    (C7)
```

The intermediate exponentials cancel exactly in the product. This does not
require `[H,V_k]=0`; each factor only needs to commute with Q, which it does.
The root also correctly notes that W_k need not itself obey the lift's
identity rule on inaccessible incomplete battery blocks. Full unitarity and
energy conservation are enough for the history Hamiltonian; the original
battery approximation is applied to B_k.

Tracing the clock and then the battery produces

```
Omega_aut(t)=exp(tA) sum_x p_t(x) exp[-k(x)tau A] Phi_k(x)^B.
```

This is the original physical H evolution, with the programmed collision H
counted once. Programming B_k directly would leave an extra free rotation.
The same error was independently retained in the spin-clock PRE.

For a common clock and time grid, the PRE's full-Q convention would use
`P_k=exp(+ik tau Q)B_k`. The exact relationship is

```
P_k=exp(+ik tau H_R)G_k.                                  (C8)
```

The two global Hamiltonians are related by the clock-controlled battery
unitary with blocks `exp(+ik(x)tau H_R)`. It acts identically on the initial
packet's k=0 support. Their full output states can therefore differ, but after
tracing clock and battery their system/reference one-time channels agree.
There is no counterphase discrepancy to repair. The independent
4800-dimensional control verifies this with the non-H-covariant jump
`sqrt(gamma)|+><0|`, rather than relying on an energy-eigenoperator example.

## 4. The reference-uniform mixture bound and resource powers

The interaction-picture target satisfies

```
Psi_I'(t)=exp(-tA)D exp[t(A+D)],
||Psi_I(t)-Psi_I(s)||_diamond<=2g|t-s|.                     (C9)
```

Thus the timing term contains 2g, not 2(h+g). The supplied correlated-battery
prefix error eta_L and collision error `T tau(7g²+4hg)` remain valid after
unitary conjugation. Applying them inside the exact mixture, using (C4),
then restoring the finite clock by (C6), proves the root's bound

```
sup_(0<=t<=T)||Omega_aut(t)-exp[t(A+D)]||_diamond
 <=min(2, eta_L+T tau(7g²+4hg)
          +2g[tau w+T tan(theta)/sqrt(w+1)]+b_R).           (C10)
```

The same prepared environment and Hamiltonian appear at every t. Complete
contractions, isometry bounds and convexity make this uniform over arbitrary
untouched references. Neither a Markovian clock nor a repeatedly reset
battery is assumed. The original resolved/coherent marks enter the collision
isometry unchanged and determine the full original reduced generator.

For the supplied star, `h=O(C²)`, `g=O(C)`, with `C=S(S+1)`. The stated
choices `L,w=O(C²)`, `n=O(C^5)`, and R=ceil(8n/cos(theta)) give

```
eta_L=O(C^-2),
T tau(7g²+4hg)=O(C^-2),
g tau w=O(C^-2),
g tan(theta)/sqrt(w+1)=O(C^-2).
```

The boundary error is exponentially small in C^5. Prefactors must also enforce
`tau g<=1/2` for the finite models being used; this is automatic eventually
in the asymptotic sequence and can be imposed on the finite remainder.
Multiplying the error by h gives O(1) absolute energy error and o(C) error.
The leading star energy limit then uses the separately attributed uniform
microscopic Duhamel result, not qualitative density convergence alone.
The spectral battery and program depend on the supplied Hamiltonian; a common
resource upper estimate does not select one fixed physical bath for all lambda.

## 5. Positive clock/program energy and interaction accounting

The finite path eigenvalues are
`2J[1-cos(l pi/(M+1))]`, l=1,...,M. Subtracting the actual lowest eigenvalue
e_0 makes the bare clock `H_C=K_M-e_0 I` nonnegative. Gauge conjugation
preserves its spectrum, so the programmed term and total Hamiltonian are
nonnegative. Its exact norm and prepared mean are

```
||H_hist||=4J cos(pi/(M+1)),
<chi,H_C chi>=<H_hist>_initial=2J cos(pi/(M+1)).              (C11)
```

The real nearest-neighbor overlap of chi is zero because of its i^x phase.
This verifies the root's ground-referenced cost, rather than treating an
arbitrary positive scalar as supplied energy.

An explicit optional split, useful for comparison with PRE, is
`H_hist=H_C+H_int`. From `||T_M+T_M†||=2cos(pi/(M+1))`,

```
||H_int||<=4J cos(pi/(M+1)).                               (C12)
```

The packet and its nearest neighbors all have k(x)=0, so H_int actually
annihilates the specified initial product subspace. Its initial mean is zero.
The new independent moment calculation also gives

```
Var_initial(H_C)=4J² w sin²(theta)/(w+1).                  (C13)
```

These additional split/variance identities are derived here; they are not
retroactively attributed to the frozen root note. Bare H_C and H_int need not
be separately conserved. Their sum H_hist is positive and conserved, as is Q.
Consequently the battery's energy change exactly balances the system's energy
change. The clock/program cost is neither omitted nor relabeled as a free
external schedule.

The root's sufficient clock dimension, prepared clock/program energy and
hopping scale are O(C^5); (C12) gives the same order for the interaction norm.
The prepared battery energy is O(C^4). The n fresh pure flags have dimensions
7 or 4 per flag for resolved or coherent marks and exponential combined
Hilbert dimension. Memory purity, battery coherence, clock coherence and
programmed spectral couplings remain supplied resources. No resetting,
thermodynamic lifecycle, locality, optimality or bounded-strength limit is
established.

## 6. The distinct PRE construction and the derivative/power boundary

| Feature | Sealed independent PRE | Released root construction |
| --- | --- | --- |
| Clock | Finite spin-N/2, exact binomial law | Finite open path, traveling sine packet |
| Program times | Inverse arcsine grid | Uniform k tau grid |
| Physical-time control | Exact finite law, `E|t_J-t|<=T/sqrt(2N)` | Initial lag/velocity estimate plus finite-chain tail |
| Counterphase | Full Q in the program | System H in the program; equally valid by (C8) |
| Terminal behavior at T | Exactly the final prefix | A mixture of clipped prefixes, with the reduced-channel bound (C10) |
| Loose star clock cost for O(C^-2) channel accuracy | O(C^10) | O(C^5) |

The PRE's exact terminal-prefix instrument statement must not be silently
transferred to the traveling packet. Conversely, the root's better sufficient
resource estimate is its own new result; it does not rewrite the PRE's proof.
Both constructions preserve their failed naive timing and double-counting
routes. Neither sufficient cost is an optimum.

There is a precise additional limitation that should remain explicit wherever
this result is used:

> For each fixed finite clock and the specified product preparation, the
> initial reduced generator is A, not A+D. In particular the autonomous initial
> system-energy derivative is zero. Uniform one-time channel approximation and
> uniform energy error on a finite interval do not imply convergence of the
> initial dissipative power. The required clock limit can contain a shrinking
> small-time boundary layer.

For the traveling packet this follows from H_int annihilating the initial
product subspace. The new full-matrix control checks the derivative on all
input matrix units. In its non-H-covariant example, autonomous initial power
is zero while the GKLS initial power from the ground state is
`omega gamma/2=0.28284271247461906`. For the supplied dressed star input, the
separately checked GKLS initial derivative is

```
kappa [18delta/epsilon²+12K lambda]/(1+3epsilon²),
```

whereas the finite autonomous initial derivative is still zero. No claim in
(C10) or the root's energy-error inequality contradicts this; those are
function-value estimates, not derivative estimates. Calling this an exact
initial-power realization would be incorrect.

The one-time mixture also does not establish arbitrary-intervention process
tensors, exact unbinned event times, uniformly normalized rare records, or
permanent irreversible memory. Measuring clock or flags during the run can
change the subsequent evolution. Finite recurrence is compatible with both
finite-horizon theorems. The star remains a one-birth example; additional graph
dynamics are not reconstructed by this clock comparison.

## 7. Executed evidence, reporting correction and disposition

The new independent controls are
[traveling_packet_identity_control.py](traveling_packet_identity_control.py)
and [traveling_program_and_star_control.py](traveling_program_and_star_control.py).
They reconstruct (C1)-(C3), exact walk-power matching, Bessel propagation,
finite spectral resources, the counterphase comparison, and a full
non-H-covariant 4800-dimensional autonomous Hamiltonian. The largest full-H
versus separately propagated-clock isometry error is below 1.8e-15; the two
counterphase conventions' reduced Choi entries differ by less than 7e-16.

The original-star control reconstructs all 20 released rows using this worker's
frozen primitive local matrices. It uses a new discrete-sine spectral clock
propagator and constructs the finite battery overlap matrix from explicitly
translated sine vectors. The maximum difference across the compared state,
energy, resource and bound fields is `1.5000461810188437e-12`, well below the
stated 2e-8 comparison threshold. This numerical calculation has the original
lambda=0 stationary dressed input and both instruments. Its whole-prefix
battery reduction depends on that initial stationarity; it is not a reset
model or an arbitrary-input shortcut. General input/reference scope comes
from the analytic isometry/mixture proof.

Both frozen author controls were separately replayed from exact copied sources,
with temporary imports confined to the owned runtime directory. Their result
JSON and stdout reproduced byte for byte. This is consistency evidence only.
Full outputs, hashes and exit codes are saved in
[COMPARISON_EXECUTION_RECEIPT.json](COMPARISON_EXECUTION_RECEIPT.json).

The historical reporting defect is preserved. Thirty displayed boundary-tail
fields had underflowed to floating zero; the final helper reports a positive
conservative normal-float floor instead. The source change only alters that
reporting expression and its comments, and every other recorded scientific
value remains equal. [REPORTING_CORRECTION_CHECK.json](REPORTING_CORRECTION_CHECK.json)
and [author_underflow_reporting_fix.diff](author_underflow_reporting_fix.diff)
record the comparison. The independent high-precision control retains the
actual positive bounds as decimal strings; for w=16,n=1024 the bound is about
`4.769342735236000696253361e-3457`. Neither a displayed zero nor the later float
floor replaces the exact asymptotic bound in the theorem.

No unresolved execution failure or scientific discrepancy was found.
Required mathematical corrections to the frozen clock theorem: **none**.
Preserve the derivative/power limitation, distinguish the two clocks and their
terminal statements, and retain the premise/attribution boundaries. Private
provenance and public omission policy are recorded separately in
[PUBLICATION_PROVENANCE.md](PUBLICATION_PROVENANCE.md). This comparison makes
no root-source edit, publication change, audit verdict or merge decision.
