# Physical final-tag syndrome orthogonality — Cycle 521 (2026-07-21)

Authority: none.  Audit: unset.  Constitutional effect: none.

## Result

Cycle 521 separates three questions that were conflated by the original
seven-M2 tag relation:

1. can final native matter support a Hermitian operator whose eigenvalue is
   the logical center-number parity;
2. can final native matter plus the appended tag support a perfect syndrome
   that accepts every correct tag and rejects every flipped tag; and
3. if neither is available, what exact final-code constraint or protected
   information-retention architecture remains constructive?

For the existing Cycle-311/315/515/516 native representation, the first two
questions have a bounded negative answer.  The reason is stronger than the
Cycle-520 Pauli-span failure: opposite-parity native code vectors have exact
nonzero overlap.  No Hermitian operator can assign opposite eigenvalues to
nonorthogonal vectors, and no projector can put them into orthogonal
accept/reject sectors.

The fixed-order overlap is exactly (1/400) in magnitude.  The result holds
at train L=5 and held L=6.

This does not invalidate the tagged encoding.  The independently appended
tag makes the code isometric precisely because it retains information that
the final native row has lost.  It means that this tag is not a redundant
syndrome bit derivable from the final native shell.

Two constructive routes remain:

- the canonical dense non-Pauli projector
  (P_\tau=E_\tau E_\tau^\dagger), with involution
  (J_\tau=2P_\tau-I); and
- a protected shadow written coherently before overlapping factors erase the
  final native parity decoder.

The dense projector is exact and bounded on the three-star patch, but its
coefficients and primitive realization are supplied.  One protected parity
shadow per tagged center gives a genuinely local two-M2 equality constraint,
but does not independently tie the equal pair back to final native matter.
The six-occupation shadow is the larger direct-update comparator.

No broad no-go, minimum-content theorem, shared substrate obstruction, or
axiom pressure follows.

## Hermitian parity lemma

Let (E_i) and (E_j) be final native encoded logical columns and let
(p_i,p_j\in\{0,1\}) be their center-number parities.  Suppose a Hermitian
operator (Q=Q^\dagger) on the native shell satisfied

\[
Q E_k=(-1)^{p_k}E_k
\]

for every logical column.  Hermiticity gives

\[
(-1)^{p_i}\langle E_j,E_i\rangle
=\langle E_j,QE_i\rangle
=\langle QE_j,E_i\rangle
=(-1)^{p_j}\langle E_j,E_i\rangle.
\]

Therefore an opposite-parity pair must be orthogonal.  Cycle 518 supplies 24
opposite-left-parity native pairs whose overlap magnitude is exactly
(1/400).  The assumed (Q) cannot exist.

This lemma quantifies over every Hermitian operator on this final native
patch.  It is not limited to Pauli operators, stabilizer spans, diagonal
operators, or nearest-neighbor support.  It is also not a result about changed
representatives or a pre-overlap protected register.

## Perfect-syndrome lemma

Append one tag with the correct value (p_i).  Suppose a projector (P)
accepted every correct state and rejected every flipped-tag state:

\[
P(E_j\otimes|p_j\rangle)=E_j\otimes|p_j\rangle,
\qquad
P(E_i\otimes|1-p_i\rangle)=0.
\]

Choose a native overlap pair with (p_j=1-p_i).  The correct second state and
the wrong-tag first state carry the same tag, so

\[
\langle E_j,p_j|E_i,1-p_i\rangle
=\langle E_j|E_i\rangle
=\pm 1/400
\]

up to its exact Gaussian phase.  But the range and kernel of an orthogonal
projector are orthogonal.  This is a contradiction.  The same argument
applies to a Hermitian involution that assigns the two sets eigenvalues
(+1) and (-1).

Consequently the Cycle-519 one-tag code admits no perfect final
native-data-plus-tag syndrome for every tag flip.  For each of the 48
affected logical columns, the canonical code projector accepts a flipped-tag
component with squared norm exactly (1/160000).  The other 2,581 columns
have no such native collision in the tested code.

This is an error-detection statement, not a failure of tagged isometry.

## Exact two-star and three-star spectra

The companion runner recomputes the fixed physical overlap, rather than
inferring it from quotient coincidence alone.

### Two adjacent centers

At L5 and held L6:

| item | exact result |
|---|---:|
| native overlap pairs | 24 |
| affected logical columns | 48 |
| maximum collision degree | 1 |
| left-tag xor | 1 for all 24 |
| overlap magnitude | (1/400) |
| overlap magnitude squared | (1/160000) |

### Bent three-center overlap

The Cycle-520 geometry has three bent-path centers, sixteen cells, 96 logical
modes, and global total number at most two.  The exact native doubleton
spectrum at both sizes is:

| three-tag xor | pairs | affected columns | (P_\tau X^sP_\tau) rank | operator norm |
|---:|---:|---:|---:|---:|
| `001` | 0 | 0 | 0 | 0 |
| `010` | 0 | 0 | 0 | 0 |
| `011` | 18 | 36 | 36 | (1/400) |
| `100` | 0 | 0 | 0 | 0 |
| `101` | 0 | 0 | 0 | 0 |
| `110` | 18 | 36 | 36 | (1/400) |
| `111` | 6 | 12 | 12 | (1/400) |

Each set is a disjoint union of two-column blocks; the maximum collision
degree is one.  Center parities differ across respectively 24, 42, and 24 of
the 42 native pairs.  Thus no native-only Hermitian parity operator exists
for any of the three named centers.

The joint three-tag code has a useful stronger property.  Because no native
overlap carries xor `001`, `010`, or `100`, its canonical projector rejects
every single-tag flip exactly.  It also rejects `101`.  It cannot perfectly
reject correlated tag flips `011`, `110`, or `111`; those errors retain code
overlap (1/400) on the affected columns.

This is a bounded error-word spectrum, not a coding-distance theorem for a
recurrent or full-number volume.

## Dense non-Pauli final-code constraint

Cycle 520 proves that the independently tagged three-center encoder is an
isometry on 4,657 logical columns.  Therefore

\[
P_\tau=E_\tau E_\tau^\dagger,
\qquad
J_\tau=2P_\tau-I
\]

are an exact projector and Hermitian involution.  They satisfy

\[
P_\tau E_\tau=E_\tau,
\qquad
J_\tau E_\tau=E_\tau.
\]

For a logical unitary (U), the explicit off-code completion

\[
\widehat U_\tau
=E_\tau U E_\tau^\dagger+I-P_\tau
\]

is unitary, obeys

\[
\widehat U_\tau E_\tau=E_\tau U,
\qquad
[\widehat U_\tau,J_\tau]=0,
\]

and acts as identity on the orthogonal complement.  It therefore supports the
already tested tagged seam update, onsite contact, and one-particle mass
fixture exactly at the code-space level.

Proper-cubic covariance follows functorially.  If
(R_fE_\tau=E_{\tau,f}U_f), then

\[
R_fP_\tau R_f^\dagger=P_{\tau,f}.
\]

Cycle 520 checks all 24 frame transports and all 576 frame products for the
underlying tagged construction at L5 and held L6.  The tag is a scalar and
the projector introduces no direction order.

The resource boundary is severe and explicit:

| object | two-star tag | three-star tags |
|---|---:|---:|
| logical/code rank | 2,629 | 4,657 |
| observed native branch-shell M2 union | 419 | 545 |
| union including tags | 420 | 548 |
| compressed projector matrix units | 23,767,921 | 43,210,561 |
| literal expanded projector matrix units | 24,947,401,424,896 | 11,607,754,707,828,736 |

The M2 figures are support upper bounds obtained from the union of every
selected branch representative, not lower bounds or a proof that every site
is necessary.  The compressed matrix-unit count is

\[
1+96(10^2)+240(2^2)+4320(100^2)=43,210,561.
\]

The literal count expands the independent vacuum-role branches.  The runner
does not materialize either dense projector.  The formula proves existence
on the bounded shell; it does not synthesize its coefficients from one- or
two-M2 primitive gates, a nearest-neighbor admissibility rule, or an
autonomous sparse law.

## One protected parity shadow

Let (\sigma_A) be one dedicated protected M2 written coherently alongside
the independently appended tag before neighboring factors overlap:

\[
\tau_A=\sigma_A=N_A\bmod2.
\]

The local constraint

\[
C_A=Z_{\tau_A}Z_{\sigma_A}=+1
\]

has support two M2.  The three center constraints are disjoint and commute.
Their common tag-shadow subspace has dimension 8 inside the 64-dimensional
six-M2 tag-shadow shell.  Deleting one equality constraint raises that factor
to dimension 16.

For a seam carrying endpoint occupations (n_a,n_b), flip both the tag and
shadow of each incident tagged center by (n_a\mathbin\oplus n_b).  The
runner exhausts all 4,657 Cycle-520 logical configurations on all sixteen
seams:

- 74,512 single-seam correct-code checks have zero failures;
- 4,657 complete-schedule checks have zero failures;
- there are eighteen center-seam incidences; and
- deleting either the tag update or matching shadow update gives exactly 190
  equality-syndrome failures at every incidence.

The inherited fermionic phase remains (±1).  Coin and onsite contact
preserve local number parity, so they leave both copies fixed.  The Cycle-520
mass and contact fixtures are therefore unchanged.  Both bits transform as
proper-cubic scalars.

This is information retention, not recovery from the final native matter.
The equality constraint detects a single tag flip or a single shadow flip,
but not the correlated operation (X_\tau X_\sigma).  It also admits an
equal but incorrectly initialized pair.  Coherent pre-overlap initialization,
placement, and the physical decorated seam gate remain supplied.

No host inspection is required by the mathematical encoder: it is a coherent
isometry on logical occupation basis states.  Primitive preparation of that
isometry is not proved.

## Six-occupation shadow comparator

The larger comparator retains six private occupation M2s per coarse cell.
On the sixteen-cell patch this is 96 shadow M2s.  At the three tagged centers,
eighteen CNOTs compute the three parity tags:

\[
W=\prod_{A=1}^3\prod_{d=1}^6
\operatorname{CNOT}(q_{A,d}\rightarrow\tau_A).
\]

Compute/use/uncompute conjugation gives an exact intertwiner algebraically,
and deleting any one of the eighteen parity CNOTs produces 96 valid-
configuration errors in the Cycle-520 control.

This route exposes the individual occupation controls needed by the seam
update.  It is not yet the physical compiler: synchronization with the
Cycle-515/516 native shell and a bare one-/two-M2 decomposition of the
Cycle-219 six-mode coin are both unproved.  The private register is therefore
a comparator, not an imported solution.

## Held-size, covariance, deletion, and lawful domain

The exact overlap spectrum, native-shell support count, and Gaussian overlap
magnitudes agree at L5 and held L6.  The bent three-center union contains
sixteen distinct cells and 22 induced edges in all 24 frames at both sizes.
The straight three-center L5 geometry remains rejected because it has one
extra periodic wrap edge per frame.

The runner reuses the complete Cycle-520 controls:

- 35,328 local-term frame tests per size with zero lookup, auxiliary,
  reference, or amplitude failures;
- 24 proper-cubic frames and 576 frame products;
- 16 disjoint logical stream seams;
- 4,470,720 pairwise seam-order checks over all eight tag words with zero
  failure;
- one-particle mass equal to the Cycle-219 fixture within the existing
  tolerance; and
- contact deletion residual `0.36789306705608243` on 240 active same-cell
  two-particle configurations.

The lawful domain is the bent three-center, sixteen-cell global-
(N\leq2) code at L5 and L6.  Full number, other overlaps, boundaries,
arbitrary volumes, and the thermodynamic limit are not covered.

## Supplied inventory and remaining walls

| supplied item | role here | not derived here |
|---|---|---|
| Cycle-311/315/515/516 branch shell | final native representatives, order/gauge grammar | primitive sparse synthesis |
| Cycle-518 fixed overlap | two-star cross-parity residual | result for changed representatives |
| Cycle-519/520 tags | independently retained center parities | final native decoder or initialization law |
| Cycle-520 bent patch | three-center geometry, logical seam update, frames | recurrent volume |
| (P_\tau,J_\tau) formulas | exact dense final-code constraint | matrix-unit generation and nearest-neighbor enforcement |
| identity off-code completion | exact bounded unitary extension | selected physical off-code law |
| protected parity shadows | redundant pre-overlap information | primitive placement/preparation |
| six-occupation shadows | exposed occupation controls | physical six-mode coin and shell synchronization |
| Cycle-219 coin | mass fixture | generated species spectrum |
| Cycle-230 contact | local number-preserving phase | primitive interaction and physical rate |

The runner hash-binds the packaged Cycle-520 runner and note and separately
checks the corrected Cycle-519 semantic boundary.  It therefore cannot pass
against a silently changed upstream overlap certificate.

The collapsed open walls are:

- `W_sparse_constraint`: replace or synthesize the dense (P_\tau) using
  bounded primitive operations;
- `W_prepare`: coherently prepare tags or protected shadows without assuming
  the logical encoder as a host service;
- `W_update`: synthesize the decorated tag/shadow seam action inside the
  native physical shell;
- `W_shadow_sync`: keep a six-occupation shadow synchronized with the native
  Wilson/order shell;
- `W_recur`: extend the bounded three-center construction to recurrent
  overlaps and a volume collision policy; and
- `W_prediction`: connect the compiler to source/response, Record/time, and
  Born/probability bridges.

## N1–N8 no-go discipline

Gate status for a broad compiler impossibility, minimum-content, shared-
substrate obstruction, or axiom-pressure claim: **FAIL / DO NOT SHIP**.

### N1 — alternative-route map

1. **Factor-local seven-port relation — ATTEMPTED.**  It succeeds on every
   isolated M64 factor but fails on 142,668 three-star seeds after overlap.
2. **Complete retained Pauli/reference span — ATTEMPTED.**  Cycle 520 finds
   rank 147 versus augmented rank 148 for every center.
3. **Arbitrary native-only Hermitian parity operator — ATTEMPTED.**  The
   exact (1/400) opposite-parity overlaps falsify its defining eigenvalue
   equation on this representation.
4. **Perfect native-plus-one-tag syndrome — ATTEMPTED.**  Correct and flipped
   states have exact nonzero cross overlap, contradicting accept/reject
   orthogonality.
5. **Canonical dense code projector — ATTEMPTED.**  It exists exactly,
   rejects every single tag flip on the three-tag patch, and supports an
   identity off-code update completion; primitive sparsification is open.
6. **One protected parity shadow — ATTEMPTED.**  It gives three commuting
   two-M2 equality checks and exact logical seam preservation, with
   initialization and decorated physical update open.
7. **Six-occupation shadow — ATTEMPTED.**  Compute/use/uncompute is exact and
   every CNOT deletion is detected; physical coin synthesis and shell
   synchronization remain open.
8. **Opposite-carrier/changed representative — LIVE.**  The zero-new-M2
   comparator must re-earn the local column, dense-star, update, and mass
   fixtures.
9. **Joint role, flux, or nonregular auxiliary — UNTESTED / LIVE.**  A
   different bounded representation can remove the cross-parity native
   overlap rather than diagnose it.

The constructive projector and shadow routes prevent a route-independent
negative.

### N2 — wall-independence audit

| pair | same failed object? | does either automatically close the other? |
|---|---:|---:|
| sparse constraint / preparation | no | no |
| sparse constraint / physical update | no | no |
| sparse constraint / shadow synchronization | no | no |
| sparse constraint / recurrence | no | no |
| preparation / physical update | no | no |
| preparation / shadow synchronization | no | no |
| preparation / recurrence | no | no |
| physical update / shadow synchronization | no | no |
| physical update / recurrence | no | no |
| shadow synchronization / recurrence | no | no |
| any compiler wall / prediction | no | no |

The Hermitian-parity and perfect-syndrome statements are two formulations of
one final-information wall, not two independent impossibilities.

### N3 — hidden-wall scan

The packet exposes the native representative grammar, factor order, number
cutoff, independently appended tag, dense projector coefficients, identity
off-code choice, shadow placement, coherent initialization, CNOT network,
seam controls, coin, contact, coupling, sizes, geometry, frame action, and
tolerances.  “Constraint” is divided into exact dense code projection,
two-M2 shadow equality, and primitive nearest-neighbor enforcement.  No
schedule layer is called time and no host query is hidden as a physical law.

### N4 — residual matching

Cycle 518 supplies the two-star (1/400) Gram residual.  Cycle 520 supplies
the tagged three-star isometry, factor-local failure, Pauli-span rank defect,
logical seam update, mass/contact, and frame transport.  Cycle 521 separately
recomputes all 42 three-star fixed overlaps at L5 and L6 and obtains the same
(1/400) magnitude with xor counts `011:18`, `110:18`, `111:6`.  No time,
source, Record, Born, or probability residual is used to close a compiler
wall.

### N5 — rhetoric audit

“No Hermitian parity operator” means no Hermitian operator satisfying the
displayed eigenvalue equation on every column of this exact final native
representation.  “No perfect syndrome” means no projector/involution with
the displayed accept/reject action for the specified tag errors.  It does not
mean no non-Pauli constraint of any weaker kind: (P_\tau) is an explicit
positive example.  “Bounded” means the 16-cell, 548-M2 observed union, not
nearest-neighbor primitive synthesis or recurrent volume locality.

### N6 — partial-closure path

The dense (P_\tau/J_\tau) construction closes exact final-code projection
and single-tag leakage on the bounded three-star shell.  One parity shadow
reduces the check itself to two M2 by retaining one new bit before overlap.
The next partial closure is to synthesize the decorated seam gate on this
shadow code or to find a changed representative with vanishing cross-parity
native Gram.  No premise edit is needed.

### N7 — hostile steelman

A hostile reviewer should reject (P_\tau) as a primitive physical law: its
43,210,561 compressed matrix units merely repackage the full encoder and its
identity completion is chosen, not derived.  The one-shadow constraint can
keep two wrong bits equal, and the six-shadow route may duplicate the entire
logical occupation register without solving the native-shell synchronization
or coin problem.  Conversely, a changed representative can eliminate the
nonorthogonality and thereby evade both negative lemmas.  These objections
keep every physical wall explicit without undoing the exact overlap theorem.

### N8 — cross-cycle echo

Cycles 311, 315, 319, 324, 327, 330, 515, and 516 repeatedly repaired apparent
local obstructions by retaining role/order information or serializing it.
Cycles 518–520 show the same lesson at adjacent-star scale: once native
information is erased, postprocessing cannot recreate it, but an independent
tag restores isometry.  Cycle 521 adds the precise error-correction boundary:
the retained tag is logical information unless a second protected carrier or
changed representation makes it redundant.  This echo favors construction,
not axiom pressure.

## TOE dependency ledger and next experiment

| wall | Cycle-521 movement | exact remaining obligation |
|---|---|---|
| (C_{\rm ref}) | unchanged; dense projector uses the retained native shell | derive reference/role preparation or change representation |
| (C_{\rm num}) | clarifies that final native matter does not carry a Hermitian center-parity decoder; shadows retain it explicitly | full number and autonomous initialization |
| (C_{\rm wrap}) | unchanged; L5 straight-path wrap remains rejected | volume/boundary and physical time bridges |
| (C_{\rm int}) | dense and shadow completions preserve the exact logical seam/contact action | primitive decorated seam and coin synthesis |
| (C_{\rm local}) | exact dense final-code projector and single-tag syndrome on three centers | sparse nearest-neighbor constraint, recurrence, off-code law selection |
| (C_{\rm source}) | unchanged | autonomous response/source bridge and prediction |

The optimal next experiment is not another final-port parity search.  Run a
two-route primitive tournament:

1. place one protected parity shadow per center, construct an actual bounded
   physical decorated seam gate, and test three-star update, constraint
   preservation, leakage, frames, held size, contact, and mass; and
2. make the zero-new-M2 opposite-carrier representative re-earn its first
   local column and one physical seam update, measuring whether its final
   native cross-parity Gram vanishes.

Only if the first route requires individual mode controls should it widen to
the six-occupation shadow.  The dense projector remains the exact comparator,
not the default physical engine.

## Verification

```text
python3 scripts/physical_final_tag_syndrome_orthogonality_cycle521_2026_07_21.py --mode dry-contract
python3 scripts/physical_final_tag_syndrome_orthogonality_cycle521_2026_07_21.py --mode syndrome-certificate
```
