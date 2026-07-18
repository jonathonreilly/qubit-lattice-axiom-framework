# Off-code local-auxiliary completion of the square-pyramid even algebra — Cycle 246

Date: 2026-07-17
Status: bounded constructive/discriminating probe; no physical compiler closure
Authority: none
Audit: unset

## Question and disposition

This cycle asks whether bounded M2 auxiliaries can remove the closed-torus
identity in the Cycle-235 square-pyramid face-Pauli realization,

\[
\prod_t W_t=I,
\]

while retaining the local even-CAR generator relations, locally enforcing the
auxiliary code, carrying both total-parity sectors at every held size, and
remaining covariant under all 24 proper-cubic frames.

The strongest exact construction is an **off-code completion**.  Add one port
qubit to every pyramid/mode and set

\[
\widehat B_t = W_t Z_t,\qquad \widehat A_e=A_e.
\]

In the runner's plain-text contract this is `Bhat_t = W_t Z_t`.

The \(\widehat B_t\) are independent, their product is the nontrivial auxiliary
parity \(\prod_t Z_t\), and \(X_t\) is a weight-one operator anticommuting with
only \(\widehat B_t\).  All endpoint \(A\)-\(B\) relations, hopping-hopping
relations, and modified-Gauss loop relations remain exact.  This is a useful
local algebra completion.

It is not yet a CAR compiler.  Before auxiliary constraints, the Wilson-fixed
code exponent is \(12N-1\), rather than the six-mode Fock exponent \(6N\).
The extra tensor factors are unconstrained.  The tested bounded covariant
constraints that remove this multiplicity either return to the total-even
representation or leave a global repetition conjugate.  A selected-port
defect can recover the target exponent and both parities, but it fails 20 of
24 proper frames, fails every nonzero unit translation, and turns remote odd
fields into paths from the defect.

This is therefore a partial constructive result plus a candidate-family
discriminator.  It is not an impossibility theorem and creates **no axiom
pressure**.

## Starting map and supplied structure

For \(N=L^3\) coarse cells, the retained square-pyramid cellulation supplies:

- six pyramid 3-cells, identified with the six Cycle-230 direction modes, per
  coarse cell;
- 15 face qubits per coarse cell;
- the bounded face-flux operators \(W_t\) and framed face hopping operators
  \(A_e\);
- modified-Gauss loops of local rank \(9N-2\), plus three supplied torus
  Wilson constraints, for rank \(9N+1\);
- a supplied local incident-face ordering and its known bounded cubic framing
  gauge;
- periodic sizes \(L=3,4,5\), with \(L=6\) held out here;
- one auxiliary M2 port per pyramid for the main completion candidate.

Those ingredients are not derived in this cycle.  The torus, the choice to fix
three Wilson labels, the square-pyramid incidence structure, the six-mode
identification, and the local Pauli framing remain supplied structure.  The
period-16 marker regression is also inherited from Cycle 237; it is a local
sector-label construction, not an autonomous preparation result.

Directly relevant bounded prior art is Wei et al., [*High-Distance
Error-Correcting Codes for Fermion-to-Qubit Mappings in 2D and 3D*
(2025)](https://arxiv.org/abs/2509.00147).  Their 3D base uses the
Chen--Kapustin physical-fermion-to-qubit map, retains constant-weight local
stabilizers/operators, and carries nontrivial membrane-sector structure before
concatenation with fermionic color-code blocks.  In the periodic construction,
odd total emergent-fermion number is not supplied by a single block; multiple
logical blocks are kept total-even.  That is useful confirmation of the
even-algebra/sector boundary, but the paper is not treated here as a bounded
odd-sector state-preparation map or as a compiler for the Cycle-230 update.

## Exact free completion

Let the auxiliary port qubits transform under rotations exactly as their
pyramids.  Then

\[
\widehat B_t=W_tZ_t
\]

has weight six: five incident face \(Z\)'s and one port \(Z\).  Since each
auxiliary column occurs in exactly one row,

\[
\operatorname{rank}\{\widehat B_t\}=6N,
\qquad
\prod_t\widehat B_t=\prod_t Z_t\ne I
\]

on the full physical Hilbert space.  Moreover, \(X_t\) has the exact singleton
syndrome

\[
X_t\widehat B_s=(-1)^{\delta_{ts}}\widehat B_sX_t.
\]

No endpoint auxiliary dressing is needed for the even algebra.  The original
face operator \(A_{uv}\) anticommutes with \(W_u,W_v\), commutes with all other
\(W_t\), and commutes with every auxiliary \(Z_t\).  It therefore has exactly
the desired relation to \(\widehat B\).  The complete L=3 hopping-pair
commutation graph is unchanged, as are all primal-edge loop products.

This completion is proper-cubic at the level of the unconstrained operator
family: frames permute the six port qubits together with their pyramid labels.
It uses bounded support and constant overhead.  Its failure is code content:

| Candidate | Physical qubits | Added auxiliary rank | Code exponent | Parity content |
|---|---:|---:|---:|---|
| free ports | \(21N\) | 0 | \(12N-1\) | full relation, but \(2^{6N-1}\) excess multiplicity |
| onsite \(Z_t=+1\) | \(21N\) | \(6N\) | \(6N-1\) | one total-even copy |
| connected \(Z_uZ_v=+1\) | \(21N\) | \(6N-1\) | \(6N\) | two total-even copies |
| one omitted onsite check | \(21N\) | \(6N-1\) | \(6N\) | both parities, but one marked port |

The first row is specifically a **trivial tensor-qubit completion**, not a
locality-preserving state isometry and not a compiled physical update.

## Local constraint tournament

### Onsite freezing

The constraints \(Z_t=+1\) are radius-zero, mutually commuting, and covariant
as a family.  They commute with every \(\widehat B_t\), every bare \(A_e\), and
therefore every even update synthesized from those generators.  On their code,
however,

\[
\widehat B_t=W_t,\qquad \prod_t\widehat B_t=I.
\]

The singleton \(X_t\) anticommutes with its onsite constraint and leaks from
the lawful code.  This is an exact return to the Cycle-235 total-even sector.

### Edge/ferromagnetic constraints

Impose \(Z_uZ_v=+1\) on every edge of the connected pyramid adjacency graph.
The family is bounded, proper-cubic, and has rank \(6N-1\).  It leaves one
repetition bit \(b\), with \(Z_t=b\) throughout the graph.  This gives the
target dimension, but

\[
\prod_t\widehat B_t=b^{6N}=+1
\]

because there are six modes per cell.  Both values of \(b\) are total-even;
the code is two copies of the even representation, not the two parity irreps
of the full six-mode Fock space.

A local \(X_t\) creates defects on its five incident auxiliary checks.  The
constraint-preserving conjugate is \(\prod_tX_t\), of weight \(6N\).  Thus the
local off-code flipper has become a global on-code resource.  Preparing a
coherent arbitrary repetition bit is correspondingly a cat-state preparation
problem; selecting one classical \(b\) sector does not encode a parity
superposition.

Changing the edge-check eigenvalue signs does not solve this.  Any consistent
signed connected pattern has \(Z_t=s_tb\), and hence

\[
\prod_t Z_t=\left(\prod_t s_t\right)b^{6N}=\prod_ts_t.
\]

It can select one fixed even or odd sector, but cannot supply both.  A sign
pattern with odd \(\prod_ts_t\) marks ports/cells and is not the homogeneous
proper-cubic family.

## Selected-port, parity-exponent, and deletion controls

Leaving one auxiliary check unconstrained at a single port is a sharp deletion
control.  It raises the onsite-code exponent from \(6N-1\) to \(6N\), and on
that defect code

\[
\prod_t\widehat B_t=Z_{t_0}.
\]

Both parity sectors are present and the local algebra remains exact.  This
shows that the missing sector is not a failure of the face-Pauli algebra.  The
cost is an anchored parity service: choosing \(t_0=(0,+x)\) is preserved by
only 4 of 24 frames and by no nonzero unit translation.  Odd operators at
remote modes require an even path back to the anchor.

A translation-periodic variant uses one scalar auxiliary per cell, dresses
exactly one of the six ports in that cell, and imposes scalar ferromagnetic
constraints.  It has the target exponent \(6N\), but its total parity is
\(b^N\).  It gives one even and one odd copy when \(N\) is odd, while at
even-volume \(N\) it gives two even copies and no odd copy.  It also selects a
port direction and again fails 20/24 frames.  Dressing all six ports restores
cubic symmetry but cancels as \(b^{6N}=1\).

The runner exhausts the strict diagonal Pauli alternative made from one
proper-cubic scalar orbit and the three unoriented-axis auxiliary orbit.  The
six-direction by three-axis incidence pairs have two frame orbits, yielding
four invariant binary matrices.  In every one, each axis auxiliary occurs an
even number of times in the six-port product.  The invariant scalar assignment
is likewise either zero occurrences or six.  Thus this bounded diagonal
ansatz cannot expose an odd auxiliary exponent.  This enumeration does not
cover port-sized codes, non-Pauli reflections, twisted frame actions, or gauge
QCAs.

## Endpoint dressings and common Wilson coupling

For

\[
\widehat A_{uv}=A_{uv}X_u^pX_v^q,
\]

the endpoint anticommutation syndromes are

| \((p,q)\) | at \(u\) | at \(v\) |
|---|---|---|
| (0,0) | anticommute | anticommute |
| (1,0) | commute | anticommute |
| (0,1) | anticommute | commute |
| (1,1) | commute | commute |

Hence endpoint X dressing cancels, rather than repairs, the required relation.
Symmetric endpoint-Z dressing \(A_{uv}Z_uZ_v\) retains all relations; the
auxiliary Z factors occur twice around every loop and cancel.  It therefore
does not change the parity product.

The three Wilson labels remain a tempting proper-cubic global resource.  The
equal-Wilson family leaves a common bit, but directly identifying a defect
parity with it uses a constraint of weight \(3L+1\); the two equal-Wilson
relations have weight \(6L\).  These weights were checked at L=3,4,5 and held
L=6.  No bounded common-Wilson coupling is constructed here.  Cycle 241's
fixed-orbit chain search also found no nonzero all-size Wilson selector, but
that prior finite Pauli template search is not elevated to a theorem about
general gauge or non-Pauli couplings.

## Covariance, leakage, marker preparation, and fixtures

The free-port, onsite, and full-edge ferromagnetic families transform by
permutation under all 24 proper frames.  Their bounded even generators commute
with the applicable Z-type constraints, so the even update does not leak from
those codes.  The operator that supplies the missing local conjugacy does leak
for onsite constraints and creates local defects for ferromagnetic constraints.

The inherited radius-two marker still has 4096 distinct phase templates, zero
ambiguities, zero rotation mismatches, and unique positive-axis successors.
This confirms a local covariant code-family label.  It does not prepare the
ferromagnetic repetition cat state, choose its logical bit, or turn the marked
defect into a homogeneous compiler.  Marker preparation and auxiliary state
preparation remain separate imports.

There is no actual bounded covariant odd-sector isometry \(E\) in this cycle.
Accordingly, the one-particle mass fixture, local contact, and Cycle-230 seam
block are not reported as preserved or reproduced.  The bare \(A,\widehat B\)
relations are sufficient to carry even algebraic formulas off code, but that
is weaker than satisfying

\[
E G_{\rm coarse}=G_{\rm physical}E
\]

on the declared full code space.  This is the fixture firewall.

## Exact runner and residual ledger

Run:

```bash
python3 scripts/off_code_local_auxiliary_completion_cycle246_2026_07_17.py
```

The runner checks L=3,4,5 and held-out L=6 where size dependence matters.

| Residual | Cycle-246 status |
|---|---|
| local even-algebra operator map | exact for free \(\widehat B=WZ\), bare \(A\) |
| full-algebra parity relation off code | exact; \(\prod\widehat B=\prod Z_{aux}\) |
| auxiliary multiplicity removal | not closed without sector/covariance loss |
| lawful local singleton flipper | absent in tested constrained codes |
| full-Fock exponent | achieved by ferromagnet/defect, but wrong sector content or symmetry |
| odd sector at all held sizes | not achieved covariantly |
| all 24 proper frames | free/onsite/edge families yes; selected port 4/24 |
| bounded common-Wilson coupling | not built; direct weight grows as \(3L+1\) |
| bounded state isometry/preparation | not built |
| one-particle mass/contact/seam | firewalled, not claimed |

For the six-wall campaign ledger this moves \(C_{local}\) constructively at the
off-code algebra level and sharpens its on-code residual.  It does not move
\(C_{int}\), because no actual full-code contact/seam intertwiner exists.  It
does not change \(C_{ref}\), \(C_{num}\), \(C_{wrap}\), or \(C_{source}\).

## N1–N8 no-go-discipline record

### N1 — Alternative-route enumeration

The probe tests free port auxiliaries, onsite freezing, connected
ferromagnetic and signed-edge constraints, one deleted onsite check, one
selected scalar port per cell, cubic-symmetric all-port scalar dressing,
exhaustive scalar/axis diagonal Pauli incidence matrices, endpoint X and Z
dressings, and direct common-Wilson coupling.  Still-live alternatives include
bounded non-Pauli commuting reflections, a genuine local gauge code with a
topological parity bit, a twisted proper-cubic frame action, measurement and
feedforward preparation, open-boundary encoders, and non-Clifford QCAs.

### N2 — Wall-independence audit

The free construction closes the local operator-relation wall while leaving
dimension and state encoding open.  Onsite constraints close local lawful
enforcement but lose odd parity.  Ferromagnetic constraints close the exponent
count but leave two even copies and a global conjugate.  The defect closes the
finite parity count but independently fails covariance and locality of remote
odd fields.  These conditions are not treated as one obstruction.

### N3 — Hidden-wall scan

The audit separately checks algebra rank, stabilizer rank, code exponent,
parity multiplicities, even/odd volume behavior, constraint leakage,
conjugate weight, proper-cubic covariance, unit translation, Wilson support,
marker selection, state preparation, and fixture availability.  It also flags
the supplied Wilson sector, ordering/framing gauge, periodic topology, and
mode-to-pyramid identification.

### N4 — Residual matching

Every negative statement is scoped to its evidence: Z-type onsite/edge
constraints, strict scalar/axis diagonal Pauli dressings, endpoint Pauli
dressings, or direct Wilson constraints.  The evidence does not establish a
route-independent obstruction to all local auxiliaries, all non-Pauli maps,
or all locality-preserving isometries.

### N5 — Rhetoric audit

The result is called an off-code algebra completion and a constrained-candidate
failure.  It is not called a physical-site compiler, an impossibility theorem,
a minimum-content theorem, or constitutional evidence.  No wrapped phase is
called physical energy, no generator element is called a rate, and no pointer
copy is called a Record.

### N6 — Partial-closure path scan

The free completion, exact-dimensional ferromagnetic code, one-defect full
parity code, and odd-volume selected-port code are retained as partial
closures.  The highest-value continuation is to replace the repetition/defect
parity service with a bounded cubic gauge code whose local constraints leave a
common logical bit and admit a bounded state isometry, or to construct an
explicit non-Pauli port code that evades the even-orbit cancellation.

### N7 — Steelman

The strongest contrary case is that a local auxiliary gauge field can spread
the common Wilson bit through bounded Gauss constraints, so that no port is
distinguished and a finite-depth or measurement-assisted isometry prepares the
lawful sector.  Another live possibility is a bounded non-Pauli representation
of six commuting involutions with a twisted cubic action whose product is the
logical parity.  Neither is ruled out by the binary Pauli searches here.

### N8 — Cross-cycle echo

Cycle 235 supplied the exact local even-algebra map and exposed the closed
flux identity.  Cycle 237 separated a covariant marker family from its sector
preparation.  Cycle 241 found the local-rank deficit for a product-ancilla
Clifford QCA and the absence of a fixed all-size Pauli Wilson selector, while
leaving non-Clifford and subalgebra maps open.  Cycles 238 and 240 likewise
separated sector preparation/decoding resources from a bounded unitary
compiler; Cycle 239 showed that a distinguishable-walker update can be local
without supplying fermionic antisymmetry.  The present result is consistent
with those distinctions but is not promoted by repetition into a shared
substrate no-go.

## Conclusion

The equation \(\widehat B_t=W_tZ_t\) is the cleanest local repair yet of the
square-pyramid full-algebra relation: bounded, cubic, exact, and equipped with
a weight-one off-code conjugate.  The tested local constraints reveal the
remaining problem precisely.  Removing the auxiliary multiplicity turns the
local conjugate into leakage or a global repetition operator, while the only
explicit both-parity deletion marks a port and loses covariance.  This is a
sharper target for the next constructive gauge/non-Pauli search, not axiom
pressure.

Time firewall: completed within the Cycle-246 campaign window.  No axioms,
foundation text, Qualification, primitives, registries, policies, queues, or
audit status were edited.
