# Physical Cycle-269 coherent proper-cubic pair orbit

Date: 2026-07-17
Authority: none
Audit: unset

## Question

Can the fixed-Wilson reference-relative localized pair lifts be assembled into
one linear encoder for genuine coherent superpositions over a nontrivial
proper-cubic orbit, with the same physical stream/catch-up and Cycle-230
contact products acting on the entire common code space?

## Constructive result

Yes, on one bounded identical-pair orbit relative to the supplied reference
vacuum.

At a supplied coarse-cell anchor `x`, take the twelve unordered perpendicular
pairs of the six half-edge modes.  They are one transitive proper-cubic orbit.
For every address `a`, the reviewed localized lift supplies an intracell state
`P_(x,a,0)|Omega_+++>` and its streamed/caught-up state
`P_(x,a,1)|Omega_+++>`.  The common twenty-four-dimensional encoder is

    E_x = sum_(a=0)^11 sum_(t=0)^1
          P_(x,a,t)|Omega_+++><x,a,t|.

This is one linear E_x, not a separately selected encoder for each basis ray.
The auxiliary tag strings of its 24 columns are distinct, so the exact Gram
matrix is `E_x^dagger E_x=I_24`.  Consequently it maps arbitrary coherent
superpositions of the twelve-address basis and both stream slices isometrically.
This is a matrix-free definition of one linear isometry. It is not a circuit
that prepares the columns or their amplitudes.

The construction has the exact restricted intertwiners

    E_x S_coarse = S_physical E_x,
    E_x C_coarse = C_physical E_x,

where `S_coarse=I_12 tensor X_2`, `S_physical` is the one complete outer-edge
FSWAP layer followed by the simultaneous collision-safe auxiliary catch-up,
and

    C_coarse = I_12 tensor diag(exp(i g),1),  g=0.37.

`C_physical` is the same complete product of the Cycle-230 local contact
projectors used by every address.  The actual Cycle-230 order is stream then
contact, because `G_g=W_g Gamma(SC)`.  The common code satisfies both

    E_x (C_coarse S_coarse)
      = (C_physical S_physical) E_x,

and the reverse-order comparator

    E_x (S_coarse C_coarse)
      = (S_physical C_physical) E_x.

The reported 24-by-24 physical matrices are restricted physical matrices:
they are the actions of the common global products on `im(E_x)`, not
full-Hilbert-space matrices. The contact restriction is evaluated from the
literal `B`-projector eigenvalues of each physical representative, not merely
from a decoded occupation label. Equality on all 24 basis columns proves the
intertwiners for every coefficient vector by linearity; the three coherent
vectors below are additional numerical probes, not the basis of that claim.

These schedules are compiler compositions, not physical time. Contact and
stream cannot silently be exchanged: their operator-norm commutator on this code is
`0.36789306705608243`.

## Support and constraints

The inherited physical allocation is 15 face M2 plus six auxiliary port M2
per coarse cell, or 21 M2 per cell.  A single column has relative Pauli/tag
support from 3 through 19 M2.  The relative-state union of the 24
representatives is 42, 46, 50, or 54 M2 depending on the translated anchor
convention, hence at most fifty-four-M2 and independent of `L`.

That 42--54 count is not operator support. The complete stream/catch-up layer
is an extensive product whose union is all `21 L^3` face-plus-port M2, while
the complete contact product has union `15 L^3` face M2. Their locality is in
their bounded factors: an outer stream/catch-up factor uses 11 M2 and a full
cell contact block uses 18 face M2. No 54-M2 implementation of the global
operators or of an `E_x` preparation circuit is inferred.

Every column commutes with every local face-code check and all three fixed
Wilsons.  Each also has eigenvalue `+1` under every local
`B_v Z_port(v)` constraint.  These are linear constraints, so their zero
constraint leakage extends immediately to arbitrary coherent address
superpositions.

The support statement is reference-relative.  It does not turn preparation of
the spatially extended fixed +++ Wilson reference vacuum into a bounded
operation.

## Proper-cubic covariance and phases

The address basis is the antisymmetric wedge basis for two identical CAR
modes.  A proper frame therefore acts by a signed permutation `W_R`, not by an
unsigned permutation of unordered labels.  This is physical exchange sign,
not a separately fitted ray phase.  Crucially, the same sign is common on both
stream slices:

    U_R E_x = E_(R x) (W_R tensor I_2)

up to the one address-independent global ray phase of the supplied reference
vacuum.  The Pauli representatives themselves had zero residual phase after
the declared wedge sign was included.

The sign is independently fixed before inspecting the transformed Pauli
phase: it is `+1` when the mapped ordered mode pair agrees with the declared
target wedge order and `-1` when it is reversed. The runner then compares both
physical stream slices to that expected sign. It also verifies that reversing
source/carrier roles at fixed address multiplies both encoded columns by the
same minus sign and leaves their tags unchanged. Thus source and carrier are
ordered wedge slots for one identical pair, not independent species labels.

The runner checked:

- all 24 proper-cubic frames at every one of the 27 `L=3` anchors, or 15,552
  encoded-column tests;
- all 576 signed-wedge group products, with maximum group-law residual zero;
- transitive coverage of all 12 pair addresses;
- zero common-slice phase failures;
- invariance of the fixed reference tableau;
- commutation of the induced frame action with both stream and contact;
- all 27 `L=3` translations at all 27 source anchors, or 17,496
  encoded-column tests, with zero failure; and
- all 729 translation-group products, with maximum residual zero.

Thus the signs form one lawful proper-cubic representation on the whole
coherent code, rather than twelve independent phase conventions.

## Held size, coherence, and exact residuals

The complete anchor family was tested at training sizes `L=3,4,5` and held
size `L=6`:

In compact contract language: held L=6 passed.

| L | anchors `E_x` | encoded columns | held | Gram/action/constraint failures |
|---:|---:|---:|:---:|---:|
| 3 | 27 | 648 | no | 0 |
| 4 | 64 | 1,536 | no | 0 |
| 5 | 125 | 3,000 | no | 0 |
| 6 | 216 | 5,184 | yes | 0 |

For every anchor the runner established the full 24-column Gram, stream,
contact, inverse, Cycle-230 stream-then-contact, and reverse-order matrix equalities. It additionally
tested a uniform coherent state, a Fourier-phase state, and a fixed-seed
generic complex state. The matrix residuals were zero, and the largest
floating normalization/superposition residual was
`2.220446049250313e-16`.

## Deletion and lawful-domain controls

The following deletions all leave the declared common code or change its
action detectably:

- deleting catch-up after stream leaves zero resulting rays in the code, even
  after irrelevant Pauli representative phase is removed;
- retaining only one of the two required stream factors leaves zero resulting
  states in the code and violates the port constraint;
- the literal projector spectrum identifies exactly one active physical
  contact factor, the addressed source/carrier pair; deleting it changes the
  input column by residual `|exp(i g)-1|=0.36789306705608243`, while all other
  pair projectors are inactive;
- deleting one stream-slice column gives stream-closure residual one; and
- deleting one full pair address gives signed-frame covariance leakage one.

The lawful domain checks reject coefficient vectors of dimensions 23 or 25,
nonfinite coefficients, out-of-range anchors, `L=2`, and an opposite rather
than perpendicular local pair.  These tests distinguish the declared code
space from arbitrary even physical states.

## Supplied-structure inventory

The construction creates no dynamic address service; it instead imports:

1. one global fixed +++ Wilson, all-`B=+1` face-code reference vacuum;
2. one supplied cell address `x` and the six direction labels at that cell;
3. the antisymmetric CAR wedge address convention and graph-edge orientation;
4. six auxiliary port M2 per cell initialized to zero;
5. the Cycle-269 `A/B/FSWAP` dictionary and collision-safe catch-up product;
6. the Cycle-230 finite real contact coupling `g=0.37`; and
7. the Cycle-230 stream-then-contact order and the reverse-order comparator.

In particular, address preparation is not derived.  The result proves the
linear action after arbitrary address amplitudes are supplied; it does not
construct a bounded circuit that prepares those amplitudes from the reference
vacuum or an autonomous physical address decoder.

## Exact boundary

This closes the earlier restriction to one separately selected localized ray:
one common physical code now carries coherent superpositions over all twelve
proper-cubic pair directions and both slices, and the same stream/catch-up and
contact operators act exactly on it.

It remains reference-relative and fixed-anchor. It is not independent species,
not a coin router, and not a full-Fock compiler. It is not a construction of
position coherence over a volume-growing set of cell anchors. It does not
encode odd states, larger even sectors, the six-mode coin, the local joint
coin/port-routing update, or a full-Fock compiler. It makes no physical-energy,
rate, physical-time, gravity/source, Record, or Born claim.

This is a constructive partial compiler seam.  There is no no-go claim and no
axiom pressure.

## Dependency-ledger effect

- `C_local`: materially narrowed from separately selected localized rays to
  one bounded 12-address coherent proper-cubic orbit; global position
  coherence and preparation remain open.
- `C_int`: the Cycle-230 contact, its actual stream-then-contact composition,
  and the reverse-order control now act exactly on that common coherent
  subspace.
- `C_wrap`: unchanged; the fixed +++ Wilson reference-vacuum import remains.
- `C_ref`: unchanged by this probe.
- `C_num`: unchanged by this probe.
- `C_source`: unchanged by this probe.

The next useful seam is an autonomous bounded encoder/preparer or a coherent
extension across multiple cell anchors, followed separately by the joint
matter-coin/port-routing problem.  Failure of any such extension would remain
route-specific evidence unless independently established across the other
compiler routes.
