# Goal

Source/Eta Block 22 tests the shortest positive quantum-to-Record bridge left
after Blocks 09--21, while resolving two preregistration-fatal type errors
before any target runner exists:

1. Block09's fourteen probabilities may be an exact six-qubit POVM, but a
   Lueders implementation disturbs its six inputs.  Those inputs cannot at the
   same time be arbitrary unknown permanent quantum Records whose complete
   `M_2` contents remain QND.
2. A live Bloch-vector qubit and a computational scalar pointer bit do not
   transform under one common onsite cubic action.  Assigning different
   internal actions by block role is hidden typing.

The corrected campaign has three explicitly separated targets:

- prove the exact full-Hilbert Block09 POVM lift;
- construct a primitive-`M_2`, common-action, cubic-covariant **radial**
  Record packet and use it to write the POVM result from a consumable live
  six-qubit input;
- prove the narrow QND boundary that prevents relabeling that live instrument
  as a nondisturbing read of arbitrary noncommuting permanent Record inputs.

This block does not compose translated writers, arbitrate mixed fronts, relay
the post-measurement live state, or generate an infinite history.  Those are
gated follow-ups only after the isolated common-action writer passes.

No Block22 target runner, cache, or target mutation may exist or execute
before this packet and its independent preregistration attack are committed.

## Stage A: exact Block09 six-qubit POVM

Let `D={+-e_1,+-e_2,+-e_3}` and let
`sigma_k^(epsilon e_j)` act on the live qubit at signed-neighbor factor
`epsilon e_j`.  Freeze `tau=1/24`.

For either output sign `delta=+-1`, define

```text
E_(delta e_i)
  = I_64/12
    + (tau/4) sum_(j,epsilon)
        epsilon (delta_(i,j)-1/3) sigma_j^(epsilon e_j).
```

The effect is independent of `delta`: the two axis signs are distinct equal
branches, so their sign is ancillary branch randomness rather than additional
information extracted from the input.

For `c in {+-1}^3`, define

```text
E_c
  = I_64/16
    + (3 tau/32) sum_(j,epsilon) epsilon
        sum_(k != j) c_j c_k sigma_k^(epsilon e_j).
```

The runner must derive, not insert, the exact spectra

```text
spectrum(E_axis)  subset [1/18, 1/9],
spectrum(E_corner) subset
  [(8-3 sqrt(2))/128, (8+3 sqrt(2))/128],
```

strict positivity, `sum_b E_b=I_64`, and equality with Block09 equations
(2)--(4) on every product six-tuple.  Product density matrices span the full
operator algebra, so this is also the unique linear locally tomographic Born
extension of that product law.

For every proper cubic rotation `g`, let `u_g` be one spin-one-half lift and
let `Gamma_g` both permute the six tensor factors and apply `u_g` at every
factor.  The required covariance identity is

```text
Gamma_g E_b Gamma_g^dagger = E_(g b).
```

No abstract Stinespring placeholder is accepted.  Since different-site Pauli
terms commute, construct the positive square root explicitly as

```text
sqrt(E_b) = sum_(z in {+-1}^6) sqrt(lambda_b(z))
              product_n P_(b,n,z_n),
lambda_b(z) = a_b + sum_n z_n ||w_(b,n)||,
P_(b,n,z) = (I + z hat(w_(b,n)) dot sigma^(n))/2.
```

The first eligible positive terminal is

```text
EXACT-BLOCK09-SIX-QUBIT-POVM-LIFT
```

It is an operator theorem.  By itself it does not decide which physical
degrees of freedom supply the six inputs.

## One common primitive cubic action

The full primitive lattice uses one action only:

```text
Gamma_g:
  site z -> g z,
  every onsite M_2 factor -> u_g M_2 u_g^dagger.
```

There is no scalar-pointer site type.  Every Record-code qubit transforms by
the same spin action as every live qubit.  The pointer is made covariant by
soldering each local orthogonal readout basis to its nonzero relative lattice
direction.

## Exact radial pointer basis

For any nonzero integer vector `r`, put `n_r=r/||r||` and define the two
orthogonal one-qubit projectors

```text
P_0(r) = (I + n_r dot sigma)/2,
P_1(r) = (I - n_r dot sigma)/2.
```

Choose normalized eigenvectors `|q_r>` of these projectors.  Their phases are
Kraus gauge.  Under the common onsite action,

```text
u_g P_q(r) u_g^dagger = P_q(g r),
u_g |q_r> = exp(i phi_(g,q,r)) |q_(g r)>.
```

Thus a complete branch map may transform exactly even when one rank-one Kraus
representative transforms by an irrelevant phase.  Covariance must be checked
at the CP-map/Choi level; merely permuting labels is insufficient.

## Stage B: covariant primitive live-to-Record writer

At selected anchor `x`, use the disjoint relative-site sets

```text
L = {+-e_i}                                      six live qubits
F = {+-2 e_i}                                    six front slots
B_axis = {+-3 e_i}                               six axis-outcome slots
B_corner = {(2c_1,2c_2,2c_3): c_i in {+-1}}     eight corner slots
H = {+-4 e_i}                                    six status slots
P = F union B_axis union B_corner union H         26 pointer sites
S = L union P                                     32 primitive qubits
```

The support is sparse, proper-cubic invariant, and contained in radius four.

For `f in D`, define `|Ready_f>` on the pointer sites by:

- every status slot `r in H` has logical value zero, state `|0_r>`;
- front slot `2f` has logical value one and the other five front slots zero;
- all fourteen outcome slots have logical value zero.

For outcome `b`, define `|Locked_(f,b)>` by:

- all six status slots have logical value one;
- the front word is unchanged;
- exactly the geometric axis or corner outcome slot for `b` has logical value
  one.

Ready is a supplied pre-Record pointer condition.  Locked is one compound
26-site Record packet: status, front, and outcome sites are all declared
permanent local Records after the atomic formation event.  The six live sites
are not part of that packet.

The bit value is not a scalar property of one primitive density matrix:
`P_0(r)=P_1(-r)`.  It is decoded from the whole anchored packet.  The set of
26 recorded pointer positions has centroid `x`, which recovers the anchor;
then `r=y-x` fixes every site's radial basis.  The runner must prove that this
centroid/template decoder is unique on the isolated registered packet.  No
single-site scalar-bit claim is eligible.

The six Ready and 84 Locked words must be mutually orthogonal, geometrically
decodable, and proper-cubic covariant.  The locked words split into
simultaneous `(f,b)` pair orbits of sizes

```text
6, 6, 24, 24, 24.
```

The 84 words must be generated from geometry and labels; an 84-row code table
is forbidden.

Let `W_(f,b)=|Locked_(f,b)><Ready_f|` on the pointer block.  On the full
32-qubit algebra, freeze

```text
K_(f,b) = sqrt(E_b)_live tensor W_(f,b),

P_ready = sum_f |Ready_f><Ready_f|,
K_STOP = I_live tensor (I_pointer-P_ready).
```

The runner must prove

```text
sum_(f,b) K_(f,b)^dagger K_(f,b)
  + K_STOP^dagger K_STOP = I,
```

full-Hilbert CP/TP including arbitrary external references, exact conditional
branch probability `Tr(rho E_b)` for a supplied Ready front, and the Lueders
poststate `sqrt(E_b) rho sqrt(E_b)/Tr(rho E_b)`.

The complete common-action covariance kill test is the branch-superoperator
identity

```text
Ad(Gamma_g) o Phi_(x,f,b) o Ad(Gamma_g)^(-1)
  = Phi_(g x,g f,g b)
```

for every proper cubic rotation, with the same onsite spin lift acting on all
32 primitive qubits.  Equivalently, Kraus representatives may differ only by
one branch phase.

Locked words lie outside `P_ready`; every later application of this isolated
instrument therefore acts as exact identity on the complete locked pointer
and post-measurement live state.  The permanent object is the orthogonal
radial Record packet.  The consumed/disturbed live shell is explicitly not an
earlier permanent Record.

The second eligible positive terminal is

```text
COVARIANT-PRIMITIVE-M2-RADIAL-POINTER-LUDERS-WRITER-FROM-LIVE-INPUT
```

It means an isolated, selected, radius-four atomic 32-qubit instrument.  It
does not mean nearest-neighbor dynamics, overlapping-anchor compatibility,
Ready preparation, a translation-invariant virgin product state, or a
generated history.  In particular, incompatible radial bases prevent one
primitive site from simultaneously serving arbitrary overlapping Ready
templates.

## Stage C: permanent-Record QND boundary

Let `{Phi_b}` be CP branch maps on the six input qubits.  If their
nonselective channel fixes every arbitrary unknown six-qubit state,

```text
sum_b Phi_b = identity_channel,
```

then the identity channel's rank-one Choi matrix forces every positive branch
Choi matrix to be proportional to it.  Every branch effect is therefore
`q_b I`.  The nonconstant effects in Stage A cannot occur.

The same conclusion applies to the open Block10 family under complete old
six-qubit prefix preservation because its tangents generate `M_64`, as
established by Block11.  This is a narrow information-without-disturbance
boundary, not a no-go for Record-conditioned dynamics.

The eligible scoped boundary terminal is

```text
INFORMATIVE-BLOCK09-POVM-INCOMPATIBLE-WITH-COMPLETE-M2-RECORD-QND
```

It does not cover an orthogonal classical Record sufficient statistic,
consumable pre-Record conditions, a redundant environment fragment, an
approximate read, a supplied external live program, or an ontic Record layer
outside standard quantum-channel identity semantics.

## Exhaustive target

The primary runner must derive and test at least:

- all Stage-A effects, exact spectra, completeness, product-law equality,
  uniqueness, square roots, and 24-frame covariance;
- arbitrary correlated live inputs and arbitrary reference extensions;
- all 24 rotations of `L,F,B_axis,B_corner,H`, radial-basis projector
  orthogonality/covariance, and the complete 32-site geometry;
- six Ready and 84 Locked product words, mutual orthogonality, status
  separation, local decode, and five pair orbits;
- complete Kraus CP/TP, branch probabilities, Lueders poststates, locked
  identity, and the full common-action CP-map covariance kill test;
- the rank-one-Choi QND boundary and a commuting orthogonal-label control;
- H1, H2, all rotated frames, actual reverse, and Block09 symbolic open-family
  probabilities as downstream algebraic controls only;
- source/AST scans rejecting a supplied outcome, H1/H2 lookup, role-dependent
  onsite action, computational scalar pointer, 84-row code table, copied or
  restored live state, hidden Record-input identity, host winner, global
  scheduler, fixed tiling, physical rate/clock, Block19 beta/factor two,
  action/source/gravity identification, axiom edit, audit verdict, obligation
  retirement, or TOE movement.

The independent checker must not import the primary runner.  It must rebuild
the POVM and radial code through different representations and extend at least
one domain axis.

## Prospective adjudication

The result may contain all compatible staged terminals.  The preferred
complete mixed terminal is

```text
POVM-AND-COVARIANT-LIVE-TO-RECORD-WRITER;
RECORD-TO-RECORD-CAUSAL-BRIDGE-OPEN
```

Failure terminals are restricted to their exact stages:

- `NONPOSITIVE-OR-INCOMPLETE-SIX-QUBIT-POVM`;
- `NONORTHOGONAL-OR-NONCOVARIANT-RADIAL-RECORD-CODE`;
- `NO-COMMON-CUBIC-M2-LIVE-TO-RECORD-WRITER`;
- `NO-MEMBER-IN-FROZEN-ISOLATED-INSTRUMENT-FAMILY`.

Any negative must pass the post-execution N1--N8 packet.  No stage may turn a
failure into a claim against all Record formation, all quantum measurement,
gravity, or the minimal axioms.

## Explicit imports and nonclaims

Imported: one selected anchor, a supplied Ready radial pointer word, a
consumable six-qubit live state, the Lueders instrument choice, an atomic
radius-four higher-body interaction, a compound 26-site formation event, and
a STOP channel.

Not claimed: the six live inputs are Block09's permanent neighboring Records;
production of Ready/live states; overlapping-anchor arbitration; mixed-front
liveness; consumable relay; causal-prefix history; exact Block10 action
evolution; nearest-neighbor compilation; autonomous bath; local-infinite
process; physical time/rate/cadence; Block19 typing/factor two/beta;
action-to-intensity selection; conserved source; gravity; axiom amendment;
audit retention; obligation retirement; or TOE percentage movement.
