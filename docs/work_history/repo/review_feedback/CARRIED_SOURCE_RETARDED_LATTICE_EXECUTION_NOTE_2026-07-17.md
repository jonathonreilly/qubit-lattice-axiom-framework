# Carried-source delayed-recontact lattice execution — 2026-07-17

**Type:** bounded constructive joint-history extension

**Status:** six-tick local/global charge ledger with delayed colocated recontact

**Authority:** none

**Audit:** unset

**Constitutional effect:** none. This note does not edit or propose an axiom,
foundation clause, Qualification rule, primitive, registry, policy, queue, or
audit status.

Companion runner:

```text
scripts/carried_source_retarded_lattice_execution_2026_07_17.py
```

## Result

The carried internal-species code now has an explicitly instrumented joint
six-tick lattice history. One moving matter carrier receives the common
Cycle-219 matter coin and matter stream. Its local internal excitation
exchanges reversibly with a colocated scalar field excitation; the field then
receives its own six-direction coin and field stream. No host schedules
the local exchange direction.

The declared sparse sector is

```text
Q=N_e+N_f=1,
```

with the direct sum

```text
excited matter e_d with field vacuum
  direct-sum
ground matter g_d with one field direction f_b.
```

The local exchange, both streams, and both coins preserve that sector. The
six-tick history preserves norm, local/global Q, the matter edge ledger, and
the carried-charge edge ledger with maximum residual

```text
7.66053886991358e-14.
```

This is an internal-excitation/field-number ledger, not energy, work, stress,
a clock rate, or a gravitational source.

## Law and schedule

The inherited local exchange is

```text
T = sum_d (|g,d><e,d| tensor b_s^dagger
         + |e,d><g,d| tensor b_s),

V(theta)=exp(+i theta T),
theta=0.8 m=0.3627245233399082.
```

One tick is

```text
common e/g matter coin + field coin
  -> local e <-> g+field exchange
  -> common e/g matter stream
  -> field stream.
```

No contact layer is applied in this runner. A Cycle-230-shaped phase formula is
checked separately outside the executed one-matter update; no contact collision
or contact-bearing schedule is claimed.

## Exact local and edge ledger

At each exchange cell define

```text
j_x = Delta <N_f(x)>_vertex = -Delta <N_e(x)>_vertex.
```

The local exchange therefore preserves

```text
q_x=<N_e(x)+N_f(x)>
```

before streaming. Excited charge follows the matter-direction edge current;
field charge follows the field-direction edge current. Their incoming sums
reconstruct the next-tick `q_x` exactly on the declared direct carried
hard-core code. Matter number has its separate source-free edge identity.

No sparse amplitude threshold is used. The state is represented by complete
six-component excited amplitudes and complete `6 x 6` ground/field amplitudes
for every reached pair of matter and field cells.

## Six-tick squared-norm sector weights

Starting from scalar excited matter at the origin and field vacuum gives:

| tick | excited-sector squared norm | field-sector squared norm | global `sum_x j_x` | cells with negative `j_x` |
|---:|---:|---:|---:|---:|
| 1 | `0.8741007838712875` | `0.12589921612871396` | `0.12589921612871394` | 0 |
| 2 | `0.727809607323819` | `0.27219039267618256` | `0.14629117654746848` | 0 |
| 3 | `0.6549150856918392` | `0.34508491430816285` | `0.07289452163198028` | 1 |
| 4 | `0.5283141424283513` | `0.47168585757165143` | `0.12660094326348825` | 0 |
| 5 | `0.4425583519333496` | `0.5574416480666536` | `0.08575579049500195` | 1 |
| 6 | `0.37252929258063144` | `0.6274707074193724` | `0.07002905935271839` | 0 |

The matter and field support remain inside their six-edge causal cones.

## Delayed colocated recontact and coherent local depletion

Here “retarded” means only that a local effect occurs after intervening
coin/stream ticks in the autonomous update. The state carries no path-history
or provenance tag, so it does not prove that a specific emitted amplitude
traveled outward and returned.

The initial exchange has no colocated scalar field weight. Delayed colocated
recontact becomes nonzero at tick 2; this can include co-moving and recombined
amplitudes and is not path-resolved return. At tick 3, after two completed
stream steps, the origin has

```text
colocated scalar squared norm        0.014459389884125264
local Delta N_f                     -0.0067710042558824495
diagonal emission term              +0.04004264620072222
diagonal field-depletion term       -0.0018204258521108238
coherent interference term          -0.04499322460449384
component-sum residual              < 6e-11.
```

The origin again has negative local current at tick 5,

```text
j_origin = -0.006169212654162532.
```

The exact decomposition used at every exchange cell is

```text
Delta N_f
 = sin^2(theta)(||e||^2-||f_s||^2)
   +2 sin(theta)cos(theta) Im<e,f_s>.
```

A 48-case randomized relative-phase test compares the direct matrix
`Delta N_f` with this formula and also checks `Delta N_e+Delta N_f=0`.
The direct/formula and charge residuals are below the declared tolerance.

Thus the autonomous history contains delayed local recontact and negative
field-number transfer back into the carried excitation. This is a coherent
local depletion/re-excitation current. It is not an incoherent absorption
sector weight and not path-proven return: the negative sign at tick 3 is dominated
by interference between excited and colocated-field amplitudes.

Nor is it global net field depletion. Every displayed global `sum_x j_x`
remains positive through tick 6, and the field-sector squared norm rises from
`0.12589921612871396` to `0.6274707074193724`. The route demonstrates delayed
colocated recontact and local coherent depletion, not a bound eigenmode,
stationary dressing, recurrence law, decay law, or global radiation balance.

## Covariance and held sizes

The dynamic covariance test starts from an anisotropic superposition containing
both a separated ground/field branch and a colocated branch. Each of tick 1 and
tick 2 is recorded and asserted under all 24 proper-cubic frames; the maximum
state residual across both ticks is

```text
2.2486540596359683e-16.
```

Periodic held domains reproduce the complete six-tick infinite sparse state:

| held size | state residual | global-Q residual |
|---:|---:|---:|
| `L=13` | `0.0` | `6.439293542825908e-15` |
| `L=15` | `0.0` | `6.439293542825908e-15` |

The support has not reached a periodic image at this resolution, so these are
no-wrap controls rather than finite-volume response claims.

## Mass, deletion, and separate contact-formula check

Both `e` and `g` use the same common matter coin. The inherited bare fixture is
the Cycle-219 one-particle mass fixture:

```text
analytic mass    0.4534056541748852
dispersion mass  0.4534056690336209
rest mass        0.4534056541748851.
```

Setting `theta=0` returns the four-tick bare excited-matter walk with state
residual `0.0` and exact field vacuum. This is source-coupling deletion; it
does not determine the dressed mass of the nonzero-coupling history.

A separate formula evaluates to one at matter number zero and one and to
`exp(i0.37)` at matter number two. This is an out-of-domain algebra check only:
no contact matrix or contact layer is applied to the six-tick history.

## Direct-code and physical-matrix boundary

The inherited direct physical allocation is

```text
12 matter M2/cell + 6 field M2/cell = 18 M2/cell.
```

The active local `Q=1` exchange block has dimension 42. This runner rechecks
that the inherited direct-code labels map to 42 distinct 18-M2 computational
basis indices. It does not assemble the complete `2^18` onsite matrix or a
global physical tensor matrix. The six-tick sparse history executes the
declared direct carried hard-core code, not a newly instantiated full physical
compiler.

This is **not the Cycle-269 code**, not a physical CAR splice, and no full-Fock
or two-matter compiler is inferred. Ordinary SWAP transport is exact in the
executed one-matter sector; its known double-occupancy difference from FSWAP
remains outside this route.

## Supplied structure

The load-bearing supplied structure is:

1. the direct 12-matter-M2 plus six-field-M2 allocation and identity-completed
   local code;
2. the one-matter `Q=1` preparation sector and scalar excited initial packet;
3. the interpretation of `e` as charged source capacity and `g` as discharged;
4. the local exchange operator, coupling `theta=0.8m`, sign, and schedule;
5. identical Cycle-219 matter coins/streams for `e` and `g`;
6. the Cycle-214/215 field coin and ordinary field stream;
7. the separate, unexecuted algebraic `g=0.37` contact formula;
8. infinite sparse geometry and periodic held `L=13,15` boundaries.

No full-Fock preparation, Cycle-269 intertwiner, two-matter contact update,
dressed mass, stationary source equation, static action, physical energy or
stress, clock calibration, metric response, occurrence, Record, Born law, or
empirical calibration is supplied or derived.

## Disposition

```text
joint multi-tick lattice execution: PASS through six ticks
local/global Q conservation:        PASS
delayed colocated recontact:          PASS at tick 2; no path provenance
local coherent field depletion:      PASS, negative origin Delta N_f at ticks 3 and 5
global net field depletion:           NOT OBSERVED through tick 6
mass/deletion/held-size controls:     PASS
full-Fock or Cycle-269 splice:        NOT EXECUTED
shared obstruction or axiom pressure:NONE
```

This is a bounded constructive route with named open work and **no no-go
claim**.
The next useful test is whether delayed coherent recontact produces a stable
dressed one-particle eigenmode or bounded recurrence on held sizes without importing a
clock, source action, or full-Fock CAR transport.

## Verification

```text
python3 -m py_compile \
  scripts/carried_source_retarded_lattice_execution_2026_07_17.py

PYTHONPATH=scripts python3 \
  scripts/carried_source_retarded_lattice_execution_2026_07_17.py
```
