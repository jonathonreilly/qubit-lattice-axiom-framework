# Observable-specific Wilson blindness and readout — Cycle 274

Date: 2026-07-17

Branch: `codex/bare-metal-mvp-probes-20260713`

PR: existing draft PR #5389 only

Authority: none

Audit: unset

## Decision

Cycle 271 gave a conservative, full-support-cone certificate: before the
backward gate cone contains a noncontractible cycle, the flat Wilson seam can
be moved outside it and every local process block is identical in all eight
characters.  It did not say that a support-cone wrap automatically makes a
particular observable sensitive.

Cycle 274 performs the missing observable calculation with the actual
Cycle-230 free-plus-contact update.  On the declared low-particle sectors, the
tested onsite and contact density algebras are numerically Wilson-blind to the
stated floating tolerance before their full-cell first wrap.  Onsite density,
the scalar mass-mode projector, and contact density become sensitive at that
wrap and remain sensitive one compiler iteration later.  The narrower probes
expose real observable-specific cancellations: the directed-mode density at
even \(L=4\), and again at held-out \(L=6\), is still exactly blind at the
full-cell first wrap and responds only one step later; bond probes have a wider
initial support and can respond one step earlier.  Several characters
orthogonal to the selected bond or mode also cancel while other characters
respond.  Thus a support-cone wrap is not automatic sensitivity, and the
Cycle-271 bound is sharp only for specified observable families.

That is a bounded positive readout result, not a no-go theorem.  Conserved
global number is an immediate counterexample to any claim that every even
observable must read a Wilson character.  Other local algebras, preparations,
codes, and gauge quotients remain open.  There is no route-independent
obstruction and no axiom pressure.

## Actual update used

The one-particle rule is the supplied Cycle-230 rule

\[
 U_w=S_w C_{\beta=-0.3},\qquad S=B A,
\]

where the free stream is the depth-two fermionic-swap construction and the
Wilson character inserts a sign on a flat periodic stream seam.  The runner
checks directly at \(L=3\) that its sparse \(U_w^\dagger\) at \(w=000\)
equals the dense Cycle-230 `spatial_layers` matrix and that the actual stream
retains the \(S=B A\) factorization.

On the two-particle sector the update is

\[
 G_w=W_g\,\Gamma_2(U_w),\qquad
 W_g=\prod_x\exp\!\left[i g {N_x\choose2}\right],\qquad g=0.37.
\]

The Heisenberg columns for a rank-\(r\) projector \(P=E E^\dagger\) are

\[
 Y_w(t)=G_w^{-t}E,\qquad P_w(t)=Y_w(t)Y_w(t)^\dagger.
\]

For the one-particle probes, \(G_w\) reduces exactly to \(U_w\).  For contact
density, the runner evolves all fifteen onsite two-mode wedges and applies the
actual contact phase before each inverse free step.  This is a genuine
two-particle contact calculation, not a one-particle proxy.

For two projector columns \(Y_0,Y_w\), with
\(M=Y_0^\dagger Y_w\), the reported operator residual is

\[
 \|P_0-P_w\|_2=\sqrt{1-\sigma_{\min}(M)^2}.
\]

For bond kernel \(H\), the finite Frobenius residual is evaluated from

\[
 \|Y_0 H Y_0^\dagger-Y_w H Y_w^\dagger\|_F^2
 =2\operatorname{tr}(H^2)-2\Re\operatorname{tr}(H M H M^\dagger).
\]

No complete Fock matrix is materialized.  The calculation is nevertheless an
exact restriction of the declared finite CAR update to the \(N=1\) and
\(N=2\) sectors, up to ordinary complex floating arithmetic and an explicit
\(2\times10^{-14}\) sparse-pruning threshold.  Gram leakage is reported.

## Gauge placement and covariance

A fixed seam placed next to a translated probe creates immediate raw-matrix
differences that are only a choice of representative.  Cycle 274 avoids that
artifact.  For a probe at cell \(x\), each flat seam is placed on a farthest
periodic plane,

\[
 q_a=x_a+\lfloor(L-1)/2\rfloor\pmod L.
\]

When the probe is translated, its seam representative is translated with it.
When a proper-cubic frame reverses an axis, the unoriented seam edge
\(\{q,q+1\}\) is transformed as an edge and the Wilson bits are permuted with
the axes.  This is the finite gauge-aligned comparison appropriate to the
Cycle-271 quotient; it does not hide a noncontractible holonomy.

The runner audits the complete sparse one-step rule, not just selected output
numbers, under all 24 proper-cubic frames and the full 27-element translation
group at \(L=3\).  Same-cell pair incidence, hence the contact density and
contact phase, is invariant under those maps.  Covariance of the one-step
rule implies covariance of every reported Heisenberg iterate.

## Observable set

The physically relevant even probes are:

1. **Onsite density:** the rank-six projector onto all directional modes in
   one cell, restricted to \(N=1\).
2. **Scalar mass probe:** the rank-one projector onto the proper-cubic scalar
   direction \(6^{-1/2}(1,1,1,1,1,1)\), restricted to \(N=1\).
3. **Directed-mode density:** a rank-one onsite mode projector, restricted to
   \(N=1\).
4. **Bond kinetic:** \(a_u^\dagger a_v+a_v^\dagger a_u\) on a nearest-neighbor
   outer bond, restricted to \(N=1\).
5. **Bond current:** \(i(a_u^\dagger a_v-a_v^\dagger a_u)\) on the same bond,
   restricted to \(N=1\).
6. **Contact density:** the rank-fifteen projector onto two distinct modes of
   one cell, restricted to \(N=2\).

The runner separately checks the Cycle-219/Cycle-230 one-particle mass fixture

\[
 m_{\rm rest}=m_{\rm analytic}=0.453405654174885\ldots .
\]

The local scalar projector is an observable probe related to that fixture; it
is not itself a claim that a local projector measures physical energy.

## Finite census

Training sizes are \(L=3,4,5\).  The held-out L=6 fixture is never used to
select a threshold or onset.  All eight Wilson sectors are evaluated.  The
exact onset of onsite-density sensitivity is

| \(L\) | Cycle-271 first wrap | first nonzero onsite-density residual |
|---:|---:|---:|
| 3 | 2 | 2 |
| 4 | 2 | 2 |
| 5 | 3 | 3 |
| 6 held out | 3 | 3 |

Onsite density, scalar mass-mode, directed-mode, and contact-density residuals
cancel below \(2\times10^{-10}\) at all iterations strictly before that row's
full-cell first wrap.  The two-cell bond starts with broader support and its
own cone can wrap one step earlier.  At full-cell wrap and wrap plus one, the
runner prints the seven nontrivial sector residuals for every observable.  It
also prints the corresponding seven contact-density residuals.  The exact
numbers in runner output, rather than a support-cone assertion, are the result
surface.  In particular, the all-zero \(L=4\) directed-mode row at \(t=2\),
followed by a nonzero \(t=3\) row, is an exact observable-specific cancellation;
the held-out \(L=6\) row independently repeats it at \(t=3\) then \(t=4\).

The important interpretation is narrow:

- a noncontractible path has become available at first wrap;
- actual Cycle-230 coin mixing makes alternatives with distinct holonomy
  interfere;
- these particular low-rank even operators distinguish at least some Wilson
  blocks;
- the result establishes operator separation, hence existence of a witness
  state, but does not supply or select that state;
- it does not show that a local laboratory can prepare coherent Wilson-sector
  superpositions under the physical M2 constraints.

## Controls

### Leakage and particle-sector closure

The one-particle rule preserves \(N=1\).  Exterior-square evolution plus the
diagonal contact phase preserves \(N=2\).  Antisymmetric collisions are
deleted exactly by the wedge sign.  The runner checks every evolved column
Gram matrix against identity and reports the maximum leakage across training
and held-out sizes, all sectors, and both wrap times.

### Deletions

- **Wilson deletion:** comparing a block with itself returns exactly zero for
  every declared residual.
- **Coin-mixing deletion:** replacing the Cycle-219 coin by identity leaves
  the full onsite-density projector Wilson-blind even after wrap.  Seam signs
  then decorate separate permutation columns but cannot rotate their span.
- **Contact deletion in \(N=1\):** exactly no effect, as required by
  \({N_x\choose2}=0\).
- **Contact deletion in \(N=2\):** at one iteration the onsite contact
  projector receives only a common phase and is unchanged; after free mixing,
  deleting \(g\) changes its evolved projector.  This distinguishes a real
  contact effect from merely relabeling the free sector.

### Lawful domain

The runner rejects \(L<3\), a character outside \(0,\ldots,7\), negative
compiler iterations, and a nonunitary or wrongly shaped onsite coin.  The
finite claims are not extrapolated to an infinite lattice or an undeclared
Fock sector.

## Supplied-structure ledger

| supplied item | role in this cycle | status after the cycle |
|---|---|---|
| six intrinsic CAR modes per coarse M64 cell | observable algebra and Fock sectors | supplied; still not a physical M2-site compiler |
| Cycle-219 coin family | onsite mixing and proper-cubic scalar mode | supplied candidate family |
| \(\beta=-0.3\) | mass fixture member | supplied numerical choice |
| Cycle-230 \(S=B A\) FSWAP stream | nearest-neighbor free transport | supplied compiler update |
| onsite \(g=0.37\) contact | two-particle interaction | supplied numerical coupling |
| periodic cubic torus and \(L=3,4,5,6\) | finite test geometry | supplied regulator and size split |
| three Wilson bits | twisted boundary character | retained superselection/block label |
| farthest flat seam representative | gauge-aligned numerical presentation | supplied test convention; residual is holonomy-dependent after wrap |
| probe cell, bond, and low-particle sector | observable test family | supplied, explicit scope |
| compiler iteration count | composition depth | supplied test index |
| pruning and comparison tolerances | numerical decision surface | supplied and reported |

Not supplied or selected here: a physical M2 encoding, local gauge-check
Hamiltonian, initial state or sea, sector-selection mechanism, probability
law, physical energy, clock calibration, causal-time interpretation, Record
formation, source/resource law, gravity equation, or axiom content.

## TOE dependency ledger

| wall | Cycle-274 evidence | disposition |
|---|---|---|
| \(C_{\rm ref}\) | no new reference-system or physical-clock derivation | unchanged |
| \(C_{\rm num}\) | the calculation preserves the declared `N=1` and `N=2` sectors but introduces no physical number reference or parity join | unchanged; a common both-parity physical encoding and number-reference selection remain open |
| \(C_{\rm wrap}\) | exact prewrap cancellation and postwrap readout locate the topological onset for six observable families | sharpened, not closed |
| \(C_{\rm int}\) | genuine \(N=2\) contact projector includes the actual supplied phase and deletion control | strengthened boundedly; coupling remains supplied |
| \(C_{\rm local}\) | observable algebra is local on the coarse CAR cell, but no bounded physical-M2 encoding is produced | coarse locality sharpened; physical compiler wall remains open |
| \(C_{\rm source}\) | no state preparation, source law, or gravity/resource response is derived | unchanged |

This cycle primarily resolves a diagnostic ambiguity inside
\(C_{\rm wrap}\): first support wrap is not treated as automatic observable
sensitivity; sensitivity is calculated.  It does not close the campaign's
physical-site compiler question.

## Fresh N1–N8 discipline

The following stress test applies to the bounded residual claim and to any
temptation to turn it into an impossibility or minimum-content statement.

### N1 — Alternative-route enumeration

Routes still open include: a different local even observable algebra; a
stabilizer-dressed observable; explicit local gauge auxiliaries; fixed-sector
encoding; open or contractible boundary conditions; local seam-coboundary
transport; state restrictions that never witness the operator residual;
error-detecting subsystem codes; staggered/time-multiplexed scheduling; and a
direct physical-M2 realization in which Wilson labels are redundancy rather
than observables.  Global number is already an exact all-time blind
observable.  The tested readout is therefore not universal.

### N2 — Condition-independence audit

Post-wrap readout jointly uses periodic topology, nonzero Wilson character,
the selected seam-equivalence class, actual dense onsite coin mixing, a
declared observable, a sufficiently large iteration count, and the specified
particle sector.  Contact-specific conclusions additionally use the supplied
nonzero \(g\).  Removing coin mixing deletes onsite-density readout; removing
contact has no effect in \(N=1\).  These conditions are not independent walls
and are not counted as such.

### N3 — Hidden-condition scan

Hidden assumptions made explicit are: finite periodic regulator, flat seam
representative, translated/rotated gauge alignment, complex-double
arithmetic, sparse threshold, fixed proper-cubic origin convention, a chosen
bond orientation, restriction to \(N=1,2\), access to the entire low-rank
operator rather than a supplied laboratory protocol, and comparison of
Wilson blocks without a sector-preparation law.  None is promoted to
substrate content.

### N4 — Residual matching

Below wrap, numerical zeros match the Cycle-271 coboundary certificate.  At
wrap, the surviving residual matches noncontractible path interference and
changes with the Wilson character.  The coin-deletion result matches loss of
path mixing.  The contact-deletion result matches the fact that an initial
projector-global phase becomes observable only after free spreading and a
later contact action.  No residual points to a missing axiom.

### N5 — Resolution and rhetoric audit

The warranted language is “these declared observables distinguish twisted
blocks at and after the tested first wrap.”  It is not “topology is locally
observable in all states,” “wrap forces every observable to respond,” “a
Wilson bit is a measured record,” or “the compiler generates physical time.”
The output is a finite operator residual, not physical energy, probability,
rate, or occurrence.

### N6 — Partial-closure path scan

A useful partial closure is available without constitutional change: keep
all Wilson blocks, use Cycle-271's local quotient before wrap, and attach this
Cycle-274 residual census whenever an observable cone wraps.  A future local
gauge compiler can also dress operators or restrict its code subspace so the
relevant residual vanishes.  Those are constructive next probes.

### N7 — Steelman

The strongest opposing interpretation is that Wilson dependence is entirely
a boundary-condition artifact and no lawful local preparation can compare
the blocks.  Cycle 274 concedes the preparation point: operator separation
does not supply a coherent sector witness.  What the exact finite calculation
does rule out is the stronger algebraic claim that these evolved low-rank
operators remain identical across blocks after wrap.  Conversely, global
number and the identity-coin onsite projector steelman persistent blindness.

### N8 — Cross-cycle echo

Cycle 269 retained all eight Wilson characters rather than silently fixing a
sector.  Cycle 271 proved complete local-process equivalence before the cone
wrap and exhibited a Wilson-word residual at first wrap.  Cycle 274 agrees
with both: exact observable cancellation holds in the contractible regime,
and actual selected observables acquire character-dependent residuals once
the noncontractible alternatives enter.  This is a consistency echo, not a
new constitutional obstruction.

## Bounded conclusion and next probe

The strongest retained result is an exact low-particle Heisenberg census for
the actual Cycle-230 coin/contact/\(S=B A\) update: full onsite and contact
density algebras are Wilson-blind before their first wrap and distinguish at
least some of all eight blocks at and one step beyond it for training
\(L=3,4,5\) and held-out \(L=6\).  Narrower directed-mode and bond probes show
the promised cancellations and shifted onset rather than inheriting the upper
cone automatically.  Full proper-cubic and translation covariance, leakage,
deletion, and lawful-domain controls are green when the runner is green.

The optimal next step is constructive: carry these observables through the
priority local-gauge/auxiliary physical-M2 route and test whether their
dressed representatives intertwine the Cycle-230 update on the declared code
space.  If a fixed Wilson sector or dressed algebra is used, its preparation,
local constraints, and supplied structure must remain explicit.

Compiler iteration is not physical time.  A Wilson character is not a Record.
The wrapped contact phase is not physical energy, and no matrix element in
this note is a transition rate.
