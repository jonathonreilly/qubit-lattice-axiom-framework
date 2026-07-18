# Rough-terminal subsystem/auxiliary-CAR factorization — Cycle 251

Date: 2026-07-17
Status: constructive local-commutant closure; bounded full-Fock encoder remains open
Authority: none
Audit: unset
Constitutional effect: none

Companion runner:

```text
scripts/rough_terminal_subsystem_gauge_factorization_cycle251_2026_07_17.py
```

## Result up front

Cycle 247's \(N-1\) rough-terminal multiplicity is not an arbitrary pile of
onsite gauge qubits.  It is an exact second **auxiliary even-CAR** algebra on
the \(N=L^3\) coarse cells, parity-locked to the six-mode matter CAR algebra.
The runner constructs bounded auxiliary parity and hop operators of physical
weights 6 and at most 18.  They commute with every mapped matter \(B\) and
\(A\), with every local code constraint, and have the exact auxiliary CAR
incidence signs through L=3,4,5 and held-out L=6.

This bounded family exhausts the full Pauli commutant of the mapped matter
algebra modulo stabilizers.  Its only radical is total auxiliary parity, and
that operator equals total matter parity exactly on the physical code.  After
fixing either common parity, the code therefore admits the exact sectorwise
factorization

\[
  \mathcal H_{\rm code}^{\pm}
  \cong
  \mathcal H_{\rm matter}^{\pm}\otimes
  \mathcal H_{\rm aux}^{\pm},
  \qquad
  \dim\mathcal H_{\rm aux}^{\pm}=2^{N-1},
\]

and the mapped matter even algebra acts on the first factor only.  In
particular, the fixed free-plus-contact Cycle-230 word is independent of the
auxiliary state in each common-parity sector.  The one-particle mass fixture,
the local contact and seam block, and the L=3 sea rank are reproduced.

That is a genuine correction to the Cycle-247 interpretation, but it is not a
complete physical compiler.  The two auxiliary parity sectors are correlated
with the two matter sectors.  A root/spanning-tree proof exposes a full matrix
factor after parity fixing, but its canonical Pauli coordinates acquire
extensive support under the tested symplectic reduction.  No bounded
parity-sector identification and no bounded state-preparation circuit \(E\)
has been constructed.  The auxiliary system is therefore **not a canonical
onsite gauge** that can simply be discarded.  The retained result is a local
operator/subsystem representation and sectorwise algebraic intertwiner, not a
bounded full-Fock tensor encoder.  There is no axiom pressure.

## Exact local commutant construction

Let \(s_x\) be the puncture sink in coarse cell \(x\), let \(u_x\) and
\(v_y\) be the two matter modes joined by a coarse stream edge \(e=(x,y)\),
and let \(h_x\) be the rough terminal.  Cycle 247 supplies the mapped matter
stream

\[
  \widehat A_e=A(u_x,v_y)X_{h_x}X_{h_y}.
\]

Define the auxiliary cell parity and hop by

\[
 \widetilde B_x=\prod_{a=0}^{5} Z_{(s_x,u_{x,a})},
 \qquad
 \widetilde A_e=A(s_x,u_x)\widehat A_e A(v_y,s_y).
\]

The support of \(\widetilde B_x\) is six puncture spokes.  The support of
\(\widetilde A_e\) lies in the two endpoint puncture cells and their shared
stream neighborhood; its maximum tested Pauli weight is 18.  No global
Jordan--Wigner order or parity service appears in these definitions.

The runner verifies the auxiliary even-CAR presentation exactly:

- \(\widetilde A_{xy}\) anticommutes with precisely
  \(\widetilde B_x\) and \(\widetilde B_y\);
- two distinct auxiliary hops anticommute precisely when their coarse edges
  share one endpoint;
- all auxiliary generators commute with the full mapped matter family and
  the stabilizer group; and
- every generator is Hermitian.

Thus the apparent boundary multiplicity is a parity-locked auxiliary
fermionic system, not a collection of independently identifiable onsite
qubits.

## Normalizer and commutant census

Write \(S\) for the Cycle-247 stabilizer space and \(M\) for the span of
\(S\) with all mapped matter \(B\)'s and \(A\)'s.  The physical code has
\(q=22N\) M2 factors and

\[
 \operatorname{rank}S=15N+1,
 \qquad
 \log_2\dim\mathcal H_{\rm code}=q-\operatorname{rank}S=7N-1.
\]

The exact quotient census is

| quotient | vector dimension | symplectic rank | radical |
|---|---:|---:|---|
| mapped matter \(M/S\) | \(12N-1\) | \(12N-2\) | \(P_m\) |
| matter commutant \(C(M)/S\) | \(2N-1\) | \(2N-2\) | \(P_g\) |
| explicit \(\widetilde B,\widetilde A\) span | \(2N-1\) | \(2N-2\) | \(P_g\) |

The theoretical centralizer quotient dimension follows from the nondegenerate
physical Pauli symplectic space:

\[
 \dim C(M)/S=2q-\operatorname{rank}M-\operatorname{rank}S=2N-1.
\]

Because the explicit bounded auxiliary family lies in the centralizer and
has that same quotient dimension, it exhausts the Pauli commutant.  The
matter/commutant intersection is one-dimensional, with the exact operator
identity

\[
 P_g=\prod_x\widetilde B_x
 =\prod_{x,a}B_{x,a}=P_m.
\]

The results at L=3,4,5,6 are respectively:

| L | N | code exponent | matter dimension/rank | commutant dimension/rank |
|---:|---:|---:|---:|---:|
| 3 | 27 | 188 | 323 / 322 | 53 / 52 |
| 4 | 64 | 447 | 767 / 766 | 127 / 126 |
| 5 | 125 | 874 | 1499 / 1498 | 249 / 248 |
| 6 held out | 216 | 1511 | 2591 / 2590 | 431 / 430 |

Since a Pauli-generated matrix algebra has a commutant spanned by the Pauli
operators that commute with its generators, this also gives the full matrix
commutant for the declared stabilizer representation.  It does not give an
encoder preparation circuit.

## Sectorwise factorization and its precise limit

Choose one marked root cell and a spanning tree of the coarse cubic graph.
The \(N-1\) nonroot \(\widetilde B_x\)'s together with the \(N-1\)
tree-edge \(\widetilde A_e\)'s have quotient dimension and symplectic rank
\(2N-2\).  Every starting generator still has weight at most 18.  Hence, in a
fixed common-parity sector, they generate the full auxiliary matrix algebra
on \(N-1\) logical qubits.  Dimension counting closes exactly:

\[
 (6N-1)_{\rm matter\ sector}+(N-1)_{\rm auxiliary\ sector}=7N-2,
\]

the exponent of either fixed-parity physical-code sector.

This root/tree construction is an algebraic coordinate proof, not a local
choice available to a homogeneous rule.  The root and tree are global
conventions.  Moreover, deterministic symplectic Gram--Schmidt on this
bounded generating family produces maximum physical Pauli weights

\[
 162,\ 385,\ 750,\ 1296
\]

at L=3,4,5,6.  This growth falsifies that particular attempt to obtain
bounded canonical tensor coordinates.  It is not a lower bound against every
Clifford, non-Clifford, measurement-assisted, or subsystem preparation.

The honest representation is therefore

\[
 \mathcal H_{\rm code}
 \cong
 (\mathcal H_m^+\otimes\mathcal H_g^+)
 \oplus
 (\mathcal H_m^-\otimes\mathcal H_g^-),
\]

not a demonstrated bounded local isomorphism
\(\mathcal H_m\otimes\mathcal H_{g,\rm fixed}\).  Abstractly identifying
\(\mathcal H_g^+\) and \(\mathcal H_g^-\) by dimension would hide the exact
parity lock and supplies no bounded implementation.

## Two local commuting selector attempts

Two selector families reduce the physical code exponent from \(7N-1\) to
\(6N\) without leakage, but neither satisfies the complete compiler contract.

1. **Marked-root selector.** Impose \(\widetilde B_x=+1\) at all cells except
   one root.  The \(N-1\) bounded commuting rows are independent, retain both
   matter parities, and a root at the origin is stable under the 24 proper
   rotations.  Omitting one distinguished cell is a global supplied role and
   breaks every nonzero coarse translation.
2. **Covariant equality selector.** Impose
   \(\widetilde B_x\widetilde B_y=+1\) on every coarse nearest-neighbor edge.
   This local family has rank \(N-1\) and is covariant under all coarse-cell
   unit translations and 24 frames.  It leaves one common auxiliary bit
   \(b\).  Since \(P_m=P_g=b^N\), odd N gives one copy of each matter parity,
   whereas even N fixes \(P_m=+1\) and gives two copies of the even sector.
   L=4 and held-out L=6 therefore fail the both-parity/held-size contract.

The second result is an exact volume-parity residual, not evidence that every
local commuting selector fails.  Mixed \(X/Z\), non-Pauli, measurement, and
dynamical selector routes remain untested.

## Covariance scope and supplied role marker

The complete redundant auxiliary family—not the marked tree coordinates—is
tested under all 24 proper-cubic frames.  The inherited bounded incident-order
gauge sends every \(\widetilde B_x\) and oriented \(\widetilde A_e\) to its
framed counterpart exactly.  Periodic-wrap translations can also change the
numeric incident-edge order and edge orientation; after the same bounded
ordering-gauge and orientation-sign repair, coarse-cell unit translations
send every generator to its translated counterpart exactly.

This means translations of the supplied puncture/macro-cell roles.  It is not
homogeneous one-site translation on undifferentiated physical M2 factors.
The inherited Cycle-237 period-16 physical role marker remains supplied, as
do its sector preparation and selection.  Cycle 251 neither generates that
marker nor removes its reference dependence.

## Fixed update and fixture reopening

Fix, rather than fit, the Cycle-230 order

\[
 G_{\rm coarse}=W_{0.37}\,\Gamma(SC_{\beta=-0.3}),
\]

with the onsite exterior coin followed by the stream and then the onsite
contact.  Replace its even-CAR generators by the Cycle-247 mapped generators
to define \(G_{\rm physical}\) on the declared code.  Every mapped matter
generator commutes with the complete auxiliary algebra.  Therefore, for each
fixed common parity, an algebraic sector intertwiner \(E_\pm\) satisfies

\[
 E_\pm G_{\rm coarse}^{\pm}
 =G_{\rm physical}^{\pm}E_\pm,
\]

with identity action on \(\mathcal H_g^\pm\).  The runner tests an explicit
spectator tensor residual of zero at machine precision.  It does not assemble
a bounded full-space \(E\) joining the two parity sectors.

The fixed fixtures are reproduced without retuning:

- analytic mass \(0.4534056541748852\), rest mass
  \(0.4534056541748851\), dispersion mass
  \(0.4534056690336209\), and forced mass
  \(0.45444242813733504\);
- local exterior dimension 64, exact local unitarity, and contact identity on
  zero- and one-particle states;
- L=3 supplied principal-cut sea rank 73; and
- the L=416 seam wrapped phase \(-0.004514002770486904\), with singular values
  \(1,0.99988849,0.99988849,0.99988849\).

This reopens the mass/contact/seam firewall only at the local operator and
sectorwise algebraic level.  It does not rename wrapped phase as physical
energy, a generator element as a rate, or the coarse CAR cell as a completed
physical-site compiler.

## Deletion and lawful-domain controls

At L=3:

- deleting one member of the independent root/tree auxiliary factor lowers
  its quotient dimension from 52 to 51;
- deleting the two rough-terminal \(X\)'s from one mapped stream creates
  exactly two local \(C_x\) violations, while the dressed stream has zero;
  and
- deleting one independent local code constraint lowers stabilizer rank from
  406 to 405 and adds one physical logical direction.

These distinguish algebraic multiplicity, update leakage, and code-rank
deletion.

## Supplied-structure inventory

Nothing in this cycle is law-selected.  The construction uses:

1. the Cycle-230 six-mode M64 coarse cell and intrinsic CAR presentation;
2. \(\beta=-0.3\), contact coupling \(g=0.37\), and the fixed update order;
3. the Cycle-229 exterior-algebra convention and occupation basis;
4. the Cycle-219 common-coin relation and mass interpretation;
5. the principal wrapped-phase branch, sea cut, seam target \(-1\), and
   finite-volume sequence;
6. the Cycle-235 square-pyramid cellulation, three Wilson rows, face-M2
   convention, and incident-edge order;
7. the Cycle-247 puncture sink, one rough terminal per cell, local cell
   constraints, and terminal stream dressing;
8. the bounded ordering-gauge covariance repair;
9. the auxiliary \(\widetilde B,\widetilde A\) definitions introduced here;
10. periodic L=3,4,5 domains and held-out L=6;
11. the supplied puncture macro-cell partition and coarse translations;
12. the inherited period-16 physical role marker and its selected sector;
13. the marked root/tree only as a factorization proof convention; and
14. ordinary complex quantum mechanics and the stabilizer/Pauli code space.

No axiom, foundation, Qualification, primitive, registry, policy, queue, or
audit-status surface is edited.

## Dependency ledger

| wall | Cycle-251 disposition |
|---|---|
| \(C_{ref}\) | auxiliary parity sector, puncture macro-role, and period-16 marker remain supplied |
| \(C_{num}\) | both matter parities exist in the full code; covariant equality fixing fails on even volumes |
| \(C_{wrap}\) | unchanged; branch/sea/seam references remain supplied and are not time or energy |
| \(C_{int}\) | fixed contact and seam now intertwine sectorwise; bounded full-space \(E\) remains open |
| \(C_{local}\) | materially advances: bounded local matter and auxiliary even-CAR algebras with exact full commutant; bounded preparation/tensor identification remains open |
| \(C_{source}\) | unchanged; no source/resource/gravity law is generated here |

This is not a shared substrate obstruction.  It is a sharpened local-encoder
residual inside the priority gauge/auxiliary route.

## N1–N8 no-go-discipline gate

### N1 — Alternative-route enumeration

At least the following routes remain distinct and live:

1. keep the auxiliary even-CAR sector as an explicit encoded input and demand
   only gauge-independent even dynamics;
2. construct bounded local canonical pairs with a radius-one or radius-two
   Clifford cage, rather than the tested tree reduction;
3. use a non-Pauli subsystem algebra or non-Clifford local isometry;
4. use measurement/reset plus local syndrome processing to select or identify
   auxiliary parity sectors;
5. use a staggered/time-multiplexed parity shuttle with an explicit covariant
   schedule;
6. search mixed \(X/Z\) commuting selectors instead of diagonal parity
   equalities;
7. use an open rough boundary or marked charge sink as a target-changing
   control; and
8. relax full-Fock \(E\) to a declared fixed-parity operational sector if the
   physical question never uses odd observables.

Only the two diagonal selectors and one tree canonicalization are tested
here.  No route-independent impossibility is claimed.

### N2 — Wall-independence audit

- The marked-root selector closes rank and both parities but fails coarse
  translation; its wall is reference/role selection.
- The covariant equality selector closes rank, locality, and frames but fails
  both parities at even N; its wall is parity arithmetic.
- The unfixed auxiliary subsystem closes local algebra, covariance, held size,
  mass, contact, seam, and gauge-independent even dynamics; its wall is a
  bounded full-Fock sector identification/preparation.
- The tree proof closes sectorwise matrix factorization but introduces a
  global coordinate convention and extensive canonical representatives.
- The open boundary closes odd termination but changes overhead and
  homogeneity.

These walls are not one shared premise, and failure of one route does not
transfer to the others.

### N3 — Hidden-wall scan

The result still supplies the coarse-cell decomposition, punctures, terminal
roles, incident order, Wilson sector, marker phase, update schedule, coupling,
coin parameter, branch cut, sea, and seam.  The factorization proof adds a
marked root and tree but does not feed them into the physical update.  It
would be a hidden global service to use that proof convention as a local
encoder, so no such claim is made.  Ordinary complex amplitudes and tensor
composition also remain framework imports.

### N4 — Residual matching

The exact unresolved line is:

> Construct a bounded, proper-cubic and coarse-translation-covariant
> full-Fock encoding \(E\) that locally identifies the parity-locked auxiliary
> sectors, or prove by a route-independent argument that no such encoding is
> required for the operational even algebra.

Measured residuals are: auxiliary quotient \(2N-1\), one shared parity
radical, tree-canonical maximum weights 162/385/750/1296, and the even-volume
equality-selector loss of the odd matter sector.  These are implementation
residuals, not a constitutional deficit.

### N5 — Rhetoric audit

Forbidden conclusions are not shipped.  The note does not call the
multiplicity harmless gauge, does not call the tree proof a bounded encoder,
does not call a sectorwise intertwiner the requested full \(E\), and does not
promote two selector failures to a local-selector no-go.  “Exhausts the
commutant” is restricted to the declared stabilizer/Pauli representation and
is supported by exact dimension equality.

### N6 — Partial-closure path scan

The construction already supports useful partial closure: any supplied even
matter update has an exact local physical representative and is independent
of the auxiliary state within each parity sector.  The mass, contact, and seam
fixtures can therefore be exercised without selecting \(N-1\) auxiliary
qubits.  A future encoder can target only sector identification/preparation;
it need not rediscover the local operator map or the update fixtures.

### N7 — Steelman

> The result may already be the physically appropriate fermionic subsystem
> compiler.  Observable dynamics in Cycle 230 is even and preserves total
> parity.  The physical code realizes the matter even algebra with its exact
> commutant, and every auxiliary state gives identical matter predictions in
> a fixed sector.  Requiring canonical onsite gauge qubits or a full-Fock
> tensor product may impose an unnecessary bosonic encoding convention on a
> naturally parity-superselected system.  Conversely, if coherent comparison
> of matter parity sectors is operationally required, a bounded odd
> intertwiner—not a selector for every auxiliary qubit—is the precise missing
> object.  Neither possibility needs a new axiom before the operational
> requirement is settled.

The steelman survives.  It supports retaining the sectorwise compiler while
keeping the full-Fock preparation claim open.

### N8 — Cross-cycle echo

- Cycle 235 exposed the periodic total-even face-code sector.
- Cycle 237 separated covariant marker families from selected marker states.
- Cycle 245 constructed exact sector gauging with a boundary/charge sink.
- Cycle 246 localized an off-code parity conjugate but did not close a code
  image.
- Cycle 247 built exact lawful rough-terminal matter operators and identified
  the \(N-1\) multiplicity.
- Cycle 248 tested parity-doubling spectators, while Cycle 249 tested coherent
  gauge-frame preparation.

Cycle 251 does not repeat those negatives.  It identifies the full local
commutant and shows that the multiplicity has auxiliary fermionic structure.
The repeating wall is now narrower: covariant preparation or identification
of parity-correlated sectors.  Because previous cycles repeatedly retired
apparent rank walls by changing representation, this remaining wall cannot
support an impossibility or axiom-pressure claim.

## Time firewall

- campaign elapsed time: inherited 12-hour goal, still active;
- Cycle-251 runner scope: bounded exact Pauli/stabilizer arithmetic through
  held-out L=6 plus fixed numerical fixtures;
- authority: none;
- audit: unset;
- constitutional edits: forbidden and not made;
- next retask: bounded odd-intertwiner/canonical-pair search or an explicit
  operational superselection decision, not axiom drafting.
