# Goal

Source/Eta Block 23 tests the shortest positive bridge left by Block22:

```text
strictly prior orthogonal Locked Record (front f, outcome b)
  -> QND control of a supplied fresh Blank star
  -> one geometry-selected successor live condition plus Ready word
  -> the Block22 writer
  -> an exact two-event Record prefix.
```

The target is a fixed proper-cubic six-ray successor star.  It is not a
selected successor site supplied from outside the Record.  The complete old
Locked packet, including both `f` and `b`, controls which ray is activated.
The second Ready word is produced by the same controlled preparation; it is
not supplied separately.

The fresh Blank star remains a declared finite low-entropy input.  Therefore
even a complete pass is a conditional two-event construction, not autonomous
recurrence, an unbounded history, or a derivation of blank capacity.

No Block23 target runner, cache, or target mutation may exist or execute
before this packet and the independent preregistration attack are committed.

## Imported Block22 atom

Let `D={+-e_1,+-e_2,+-e_3}` and let `B=D union {+-1}^3` be the fourteen
Block22 outcome labels.  Block22 supplies exact strictly positive effects
`E_b` on the six live qubits, with

```text
sum_b E_b = I_64,
Gamma_g E_b Gamma_g^dagger = E_(g b),
```

and a selected-anchor radial writer from a Ready word to a permanent Locked
packet.  The full primitive lattice uses the same onsite spin-one-half action
on every `M_2` site.

At anchor `x`, the Block22 relative support is

```text
L = {+-e_i},
F = {+-2e_i},
B_axis = {+-3e_i},
B_corner = {(2c_1,2c_2,2c_3): c_i in {+-1}},
H = {+-4e_i},
S = L union F union B_axis union B_corner union H.
```

It has six live and twenty-six pointer sites.  Write `C_(f,b)` for the
rank-one projector onto its orthogonal pointer word `Locked_(f,b)`.

## Fixed successor-star geometry

Freeze displacement `R=9`.  For every old front `f in D`, put

```text
y_f = x + 9 f,
S_f = y_f + S.
```

The runner must derive, rather than assume, that the old block `x+S` and all
six successor blocks `S_f` are pairwise disjoint.  The complete finite support
therefore has `32+6*32=224` primitive qubits and radius thirteen about `x`.
Proper cubic rotations permute the six successor blocks.

This is an atomic finite-range preparation on a selected star followed by six
parallel disjoint Block22 writer channels.  It is not a nearest-neighbor
compiler or a mixed-front arbitration law.

## Covariant Blank and Record-controlled target

For every nonzero relative site `r`, retain the Block22 radial projectors

```text
P_q(r) = (I + (-1)^q rhat dot sigma)/2.
```

Define `|Blank_y>` on all 32 sites of `y+S` as the product of logical radial
zero states relative to `y`.  Its six live sites are supplied pure live
conditions, not Records.  Its twenty-six pointer sites are all-zero and hence
orthogonal to every Ready word, which has exactly one live front bit.

The fresh input is the six-block product

```text
|BlankStar_x> = tensor_(d in D) |Blank_(y_d)>.
```

For an outcome `b`, define

```text
u_b = b / ||b||,
Q_b = u_b u_b^T - I_3/3,
v_n(b) = Q_b n / ||Q_b n||,       n in D,
rho_b = tensor_(n in D) (I + v_n(b) dot sigma)/2.
```

The displayed positive sign of `Q_b` is frozen and load-bearing.  Replacing
it by `-Q_b` is a different covariant preparation law with a different
transition kernel, not an allowed refit after execution.

The runner must prove `Q_b n` is nonzero, every factor is a pure state,
`Q_(-b)=Q_b`, and

```text
Q_(g b) = g Q_b g^T,
v_(g n)(g b) = g v_n(b)
```

for all twenty-four proper cubic rotations.  No fourteen-row state table is
allowed.

Let `|Target_(f,b)>` be the normalized star state in which:

- block `S_f` has live state `rho_b` and pointer word `Ready_f`;
- every block `S_d` with `d != f` remains `Blank_(y_d)`.

Thus the old Record's `f` selects the successor location and Ready
orientation, while its `b` selects the fresh live condition.

## Total controlled preparation channel

On the old pointer and six-block successor star, freeze the controlled Kraus
family

```text
A_(f,b) = C_(f,b) tensor |Target_(f,b)><BlankStar_x|,

P_valid = (sum_(f,b) C_(f,b)) tensor
          |BlankStar_x><BlankStar_x|,

K_STOP = I - P_valid.
```

Every operator acts as identity on the old six live qubits.  Orthogonality of
the `C_(f,b)` controls must imply

```text
sum_(f,b) A_(f,b)^dagger A_(f,b) = P_valid,
sum_(f,b) A_(f,b)^dagger A_(f,b)
  + K_STOP^dagger K_STOP = I.
```

The resulting channel is CPTP on the complete finite algebra and on inputs
entangled with arbitrary external references.  On every valid
`Locked_(f,b) tensor BlankStar` sector it prepares exactly
`Locked_(f,b) tensor Target_(f,b)`.  Reapplication is STOP because the target
star is no longer Blank: `Ready_f` differs from the all-zero Blank pointer at
its `2f` front slot.

The exact QND claim is confined to the commuting old Record algebra:

```text
Lambda_prep^dagger(C_(f,b) tensor I) = C_(f,b) tensor I.
```

The channel is not claimed to preserve the full noncommuting old pointer
algebra or the reduced density matrix of arbitrary coherent superpositions of
Record sectors.  The old physical Locked word is never overwritten.

The full branch channel must satisfy proper-cubic covariance under the one
common onsite spin action, with `x,f,b` carried to `g x,g f,g b`.  Physical
projectors and states must rotate; label permutation alone is insufficient.
Each `A_(f,b)` may acquire its own Kraus-gauge phase.  A coherent sum over all
`(f,b)` is forbidden: fixed-axis rotations give different phases to different
fixed Record sectors, so that summed operator does not transform by one global
Kraus phase and its cross-sector CP terms are not covariant.

## Exact two-event composition

Start the first Block22 writer at `x` with supplied initial front `f`, live
state `rho`, and its Ready pointer.  After first outcome `b_1`, apply the
controlled preparation above.  Then apply one copy of the Block22 writer to
each of the six pairwise-disjoint successor blocks in parallel.  On the
reachable target exactly one block is Ready and the other five are STOP.

The direct composite Kraus calculation must equal the reduced cylinder law

```text
p_f(b_1,b_2 | rho)
  = Tr(rho E_(b_1)) T(b_2 | b_1),

T(b' | b) = Tr(E_(b') rho_b).
```

It must hold with arbitrary reference entanglement on the initial live input.
The runner must prove nonnegativity, total normalization, first-prefix
marginal consistency, preservation and unique decoding of the first Locked
packet, formation of exactly one second Locked packet, and full proper-cubic
covariance.

The first eligible positive terminals are

```text
COVARIANT-LOCKED-RECORD-CONTROLLED-FRESH-BLANK-PREPARATION

EXACT-TWO-EVENT-RECORD-PREFIX-WITH-RECORD-SUFFICIENT-LIVE-CONDITION
```

Here “Record sufficient” means the complete anchored classical label `(f,b)`
on the declared fresh-Blank domain.  It does not mean that `b` alone chooses a
site, that arbitrary quantum Record coherences are unchanged, or that a
fresh substrate is generated.

## Frozen transition-kernel target

The runner must derive the complete fourteen-state kernel from `Q_b`, the
six product Bloch vectors, and the Block22 effect formula.  It may not insert
the expected entries as a table.

For an axis input ray `a`, the expected derived entries are

```text
T(+a|a) = T(-a|a) = 1/9,
T(other signed axis|a) = 5/72,
T(corner|a) = 1/16.
```

For a corner input ray `c`, they are

```text
T(signed axis|c) = 1/12,
T(c'|c) = 1/16 + 3/(64 sqrt(2))  if c'=+-c,
T(c'|c) = 1/16 - 1/(64 sqrt(2))  otherwise.
```

Because `rho_b=rho_(-b)` and `E_(+e_i)=E_(-e_i)`, the signed chain must lump
exactly to seven unoriented rays.  In the order three axis rays followed by
four corner rays, the quotient must be derived in block form:

```text
A_ii=2/9,  A_ij=5/36,
B_ik=1/8,
C_ki=1/6,
D_kk=1/8+3/(32 sqrt(2)),
D_kl=1/8-1/(32 sqrt(2)).
```

The runner must prove strict positivity, stochasticity, reversibility, and
the unique stationary weights

```text
pi(axis signed outcome)=1/12,
pi(corner signed outcome)=1/16,

pi(axis ray)=1/6,
pi(corner ray)=1/8.
```

It must derive the quotient spectrum by invariant subspaces, not by a dense
symbolic eigensolve:

```text
1,
sqrt(2)/16  with multiplicity 3,
1/12       with multiplicity 2,
0.
```

Strict positivity makes the finite quotient primitive.  This is a property
of the constructed candidate transition law, not a derivation of physical
event rates or frequencies from the axioms.

The primitivity and unique stationary distribution apply only to the internal
seven-outcome-ray kernel with a fixed inherited front.  Retaining the six
front labels gives six closed sectors, so the 42-state `(f,[b])` chain is not
irreducible and has nonunique mixtures across fronts.  Including the moving
anchor gives spatial drift, and permanent append history remains irreversible
even though the internal outcome kernel obeys detailed balance.

## Kill boundaries and exclusions

Failure of the controlled preparation is distinct from failure of the
already-passed Block22 writer and from the still-unexecuted mixed-front
problem.  A positive result is confined to the supplied one-use Blank star.

This block does not supply or claim:

- creation, replenishment, or conservation accounting of Blank capacity;
- a third event, arbitrary prefix, projective-limit history, liveness, rate,
  clock, cadence, or scheduler;
- overlapping-star compatibility or mixed-front arbitration;
- nearest-neighbor compilation or a fixed global tiling;
- a unique axiom-forced choice of `Q_b` or preparation channel;
- a Born-rule derivation beyond the explicit imported POVM law;
- Block19's six occurrence marks, factor two, beta, or a map from fourteen
  outcomes to those marks;
- action/source debit-credit continuity, stress tensor, Ward/Bianchi join,
  gravity coupling, axiom amendment, audit status, obligation retirement, or
  TOE percentage movement.

In particular, direct reuse of the same all-six-Blank-star eligibility at the
second anchor does not produce event three: its backward candidate is the
already-Locked first anchor.  That exact architecture-specific collision
motivates a predecessor-aware/mixed-front follow-up; it is not a general
history no-go.  The reversible seven-ray kernel is an internal reduced-kernel
property, not yet a realized stationary or reversible spatial Record process.
