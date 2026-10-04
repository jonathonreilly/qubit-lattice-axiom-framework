# PMNS TM2 Magic Residual is a Native Dynamical Unitary — Narrow Bridge Theorem

**Date:** 2026-06-05
**Claim type:** positive_theorem (narrow algebraic bridge + obstruction reframing)
**Status:** unaudited candidate. Graph-visible only so the independent audit
lane can decide whether the candidate is retained.
**Primary runner:** [`scripts/pmns_tm2_magic_residual_dynamical_generator_runner.py`](../scripts/pmns_tm2_magic_residual_dynamical_generator_runner.py)
**Cached output:** [`logs/runner-cache/pmns_tm2_magic_residual_dynamical_generator_runner.txt`](../logs/runner-cache/pmns_tm2_magic_residual_dynamical_generator_runner.txt)

## Corrigendum (2026-09-30)

Source-scope correction. Status fields above are unchanged; effective status
stays with the independent audit lane. Checks are same-family (Claude Sonnet
5.5), not an independent referee.

**What was wrong.** Theorem item 4 says a `V_4`-invariant `M_nu` keeps
`theta_13` free because "the `C_3`-doublet block is unconstrained", and the
Honest auditor read repeats it. That is false. `[M_nu, S] = 0` makes `M_nu`
block-diagonal in `span{W}` plus the doublet; `[M_nu, P_23] = 0` then forces
the doublet block to be diagonal in the two `P_23` eigenvectors
`xi = (2,-1,-1)/sqrt6` (even) and `eta = (0,1,-1)/sqrt2` (odd). The Hermitian
commutant of `V_4` is 3-dimensional, spanned by `|W><W|`, `|xi><xi|`,
`|eta><eta|`. Every `V_4`-invariant `M_nu` with a non-degenerate spectrum has
eigenvectors `W, xi, eta`, electron row `|U_ej|^2 = {1/3, 2/3, 0}`, and, with
`W` as the second column, `s13^2 = 0`, `s12^2 = 1/3`, `s23^2 = 1/2`
(tribimaximal), not `s13^2 ~ 0.022`. If two eigenvalues are equal (for
example a degenerate doublet block), `M_nu` still commutes with `V_4`, but its
eigenvectors are then not determined by `M_nu`, so it fixes no mixing angle
either. The runner's part (D) checks the trimaximal
column and equal `mu`, `tau` rows (both true) and never evaluates `|U_e3|^2`;
"`theta_13` FREE" in its docstring and in item 4 was a label, not a check.
Adding the record dephasing of the sibling note to the third flip `S.P_23`
gives the same `V_4` and the same `theta_13 = 0`.

**Item 5 and runner part (E).** The runner's "`sin^2 theta_13` proxy" is the
minimum over all nine `|U|^2` entries. In its witness that minimum, 0.0213,
sits in the `tau` row; the electron row is (0.388, 1/3, 0.279), so `|U_e3|^2`
is not in 0.015-0.030, and the witness commutes with `S` only (its `mu` and
`tau` rows differ). The statement in item 5, that an `S`-commuting `M_nu` can
reach the observed `s13^2`, is true (an `S`-only operator has
`s13^2 = (2/3) sin^2(phi)` for doublet rotation angle `phi`), but the witness
does not show it and carries no `mu`-`tau` residual.

**Corrected statement.** Items 1-3 (`S` not in `S_3`; `exp(i pi/3 H_dem)` is a
phase times `S`; `<S, P_23> = V_4`) stand. Item 4 reads: `[M_nu, V_4] = 0`
gives the trimaximal column, the `mu`-`tau` modulus residual, maximal
atmospheric mixing, **and `theta_13 = 0`**. A `mu`-`tau` residual compatible
with `theta_13 != 0` needs a different condition, for example the
antiunitary reflection `P_23 M_nu^* P_23 = M_nu` together with
`[M_nu, S] = 0`; the graph-first residual the repository supplies is the
unitary invariance `P_23 H P_23 = H`, so the reflection is not supplied here.
With it the check below finds `s23^2 = 1/2`, `|sin delta| = 1`, `theta_13`
free, and still `s12^2 = 1/(3 c13^2)`.

**Data scope.** With the trimaximal column as the second PMNS column and
`U_e = I`, `s12^2 = 1/(3 c13^2) >= 1/3` for every `s13^2`; it is 0.3409 at
`s13^2 = 0.0222` and 0.3404-0.3416 across the quoted `s13^2` range. The
NuFIT-6.1 3-sigma range for `s12^2` the repository already quotes
(`PMNS_DCP_FORECAST_STANDING_DEGRADES_UNDER_NUFIT6_BOUNDED_NOTE_2026-06-08.md`,
line 28) is [0.2893, 0.3295]. The TM2 form is outside it, and a trimaximal
electron-row entry `1/3` is outside the rectangle's image at every mass
position. arXiv:2512.03809 (Ding, Li, Lu, Petcov; the statement is in the body
text, not the abstract) reports the TM2-type patterns disagree with the first
JUNO `sin^2 theta_12` measurement at the 3.6 sigma level. The April sum-rule
note that the 2026-08-05 historic intake wraps
(`docs/historic_intake/HISTORIC_KOIDE_PMNS_SUM_RULES_NOTE_2026_04_21_INTAKE_NOTE_2026-08-05.md`,
audit unset) already lists TM2 as not fitting (0.294 against 1/3).

**TM1.** The same paper finds a different literature pattern, TM1 (first
column `xi`), inside the JUNO 3-sigma range. This repository does not supply
it: the record dephasing fixes `W` as a column, not `xi`, and with the flip
`S.P_23` it gives the `V_4` result above. The historic intake cited above
lists TM1 as not fitting its NuFIT-based comparator (0.684 against 2/3); that
note does not use the JUNO measurement. Nothing here adopts TM1 as a framework
result.

**Evidence.** `scripts/pmns_tm2_scope_check_solar_angle_outside_nufit61_and_v4_commutant_forces_theta13_zero_2026_09_30.py`
(26 PASS, 0 FAIL): commutant dimensions, the runner's own seed-7 `M_nu`
(electron row 0, 1/3, 2/3), the part (E) witness, the reflection family.

## Audit context

The conditional TM2 lemmas
[`PMNS_TM2_RESIDUAL_CONSEQUENCE_BOUNDED_NOTE_2026-05-26.md`](PMNS_TM2_RESIDUAL_CONSEQUENCE_BOUNDED_NOTE_2026-05-26.md)
and
[`PMNS_TM2_MAGNITUDES_CONDITIONAL_BOUNDED_NOTE_2026-05-26.md`](PMNS_TM2_MAGNITUDES_CONDITIONAL_BOUNDED_NOTE_2026-05-26.md)
(both `retained_bounded`) derive the TM2 sum rule and maximal atmospheric
mixing from **two assumed** PMNS residuals: a trimaximal second column
`|U_x2|^2 = 1/3` and a mu-tau modulus residual `|U_mu i|^2 = |U_tau i|^2`.
They explicitly do not derive those residuals from the framework.

The graph-first route
[`PMNS_GRAPH_FIRST_AXIS_ALIGNMENT_NOTE.md`](PMNS_GRAPH_FIRST_AXIS_ALIGNMENT_NOTE.md)
(`retained_bounded`) supplies the residual `Z_2` swap `P_23` as a symmetry of
the active mass operator on the `hw=1` triplet, and
[`PMNS_GRAPH_FIRST_RESIDUAL_ANTIUNITARY_NARROW_THEOREM_NOTE_2026-05-16.md`](PMNS_GRAPH_FIRST_RESIDUAL_ANTIUNITARY_NARROW_THEOREM_NOTE_2026-05-16.md)
(`retained`) its antiunitary upgrade. `P_23` is the source of the **mu-tau
modulus** half of TM2. It is **not** the source of the **trimaximal column**
half: the trimaximal column requires the neutrino mass operator to keep the
democratic vector `W` as an eigenvector, i.e. to commute with the **magic
reflection** `S = 2|W><W| - I`, which is an *independent* condition from
`P_23`-invariance.

The apparent obstruction is group-theoretic: the framework's static
generation symmetry on the `hw=1` triplet is `S_3 = <C_3, P_23>` (the cube's
coordinate-cycle and the graph-first axis swap), and the magic generator `S`
is **not** in `S_3`. By Lagrange `S_3` has no Klein four-group `V_4`, and `S`
is non-monomial (it lives in the group algebra `R[S_3]`, not in the realized
permutation group). Read statically, the magic residual TM2 needs looks
unreachable without enlarging the flavor group to `A_4`/`S_4`, which the
framework does not realize.

This note removes that static reading. It proves the magic `S` is the **native
time-`pi/3` evolution of the democratic `C_3`-symmetric coupling**, hence the
`V_4` Klein residual TM2 needs is generated by native operations after all,
and the open problem reduces from "the flavor group is too small" to the
sharper residual-symmetry question "does the neutrino mass operator commute
with the magic `S` (preserve `W`)."

## Safe statement

Work on the `hw=1` generation triplet `V_1 = span{|100>, |010>, |001>}` with
the democratic / `C_3`-singlet vector `W = (1,1,1)/sqrt(3)`. Let

```text
S      = 2 |W><W| - I          (magic reflection; eig {+1,-1,-1}, S W = W)
C      = cyclic shift (1 2 3) on the three corners
H_dem  = C + C^dagger = J - I   (native double-shift corner coupling; J = all-ones)
P_23   = the graph-first axis swap [[1,0,0],[0,0,1],[0,1,0]]
```

Here the three generations are the `hw=1` Brillouin-zone corners of the
`(Z_2)^3` unit cube (`THREE_GENERATION_STRUCTURE_NOTE`, `retained_bounded`), and
`C` is the order-3 relabeling of those three corner patterns supplied by the
Lattice axiom (not a hop along a 6-NN bond). The democratic coupling
`H_dem = C + C^dagger = C + C^2 = J - I` is the **native second-order
double-shift** corner coupling `P(sum_{a<b} S_a S_b)P^T = J - I`
([`FLAVOR_NATIVE_DOUBLE_SHIFT_CORNER_COUPLING_NOTE_2026-05-30.md`](FLAVOR_NATIVE_DOUBLE_SHIFT_CORNER_COUPLING_NOTE_2026-05-30.md),
`retained_bounded`): a single first-order shift annihilates the triplet
(`P S_mu P^T = 0`), so the democratic coupling is genuinely the two-step object,
not an imported Hamiltonian and not a (non-existent) diagonal lattice edge.

**Theorem.**

1. **(Static non-membership.)** `S` is not a static `S_3` generation symmetry:
   `S` equals no permutation matrix, is non-monomial, and `S_3 = <C, P_23>`
   has no `V_4` subgroup (`|S_3| = 6`, `4` does not divide `6`).

2. **(Dynamical realization.)** `H_dem = C + C^dagger` has spectrum
   `{+2 (on W), -1, -1}` — `W` non-degenerate, its orthogonal complement
   (the `C_3`-doublet) degenerate. Consequently

   ```text
   exp( i (pi/3) H_dem ) = exp(2 i pi/3) * S
   ```

   exactly: the magic reflection is the time-`pi/3` evolution of the native
   democratic coupling, up to a global phase. (Proof: a relative phase of
   `pi` between the non-degenerate `W` mode and the degenerate complement
   is a reflection through `W`, i.e. `S`.)

3. **(Klein generation.)** `<S, P_23>` is the Klein four-group `V_4`. Both
   generators are native: `P_23` is the graph-first axis swap; `S` is the
   dynamical unitary of (2).

4. **(Conditional TM2 consequence.)** If a neutrino mass operator `M_nu`
   commutes with `V_4 = <S, P_23>` and the charged-lepton sector is diagonal
   in the corner basis (`U_e = I`), then the PMNS matrix `U = U_e^dag U_nu`
   has an **exact trimaximal column** (from `[M_nu, S] = 0`, i.e. `W` is an
   eigenvector), a **mu-tau modulus residual** (from `[M_nu, P_23] = 0`), and
   **maximal atmospheric mixing**, with `theta_13` **free** — `M_nu` is not
   forced circulant, so the `C_3`-doublet block is unconstrained and there is
   **no TM3 overshoot**.

5. **(Reframing of the "must break the democratic structure" reading.)** A
   `W`-preserving (`S`-commuting) `M_nu` realizes `sin^2 theta_13` in the
   observed band `0.015–0.030` while keeping the exact trimaximal column. The
   reading that "the neutrino sector must break the democratic structure to
   fit `theta_13`" tests only the **full** `C_3`-circulant operator, which
   forces all columns trimaximal (`sin^2 theta_13 = 1/3`, the TM3 overshoot).
   It does **not** test the intermediate `S`-preserving (`TM2`) operator, which
   keeps `W` while splitting the doublet. So `W`-preservation is not excluded
   by `theta_13`.

## Proof

**(1)** Direct: `S` has entries `(1/3)[[-1,2,2],[2,-1,2],[2,2,-1]]`, not a
`0/1` permutation matrix, and has two nonzero entries per row/column (non-
monomial). The subgroups of `S_3` have orders `1,2,3,6` (Lagrange forbids
order `4`), so `S_3` contains no `V_4`. `S` is the order-2 element acting as
`+1` on the trivial rep (`W`) and `-1` on the 2-dim standard rep; the latter
is `-I_2`, which is not in the image of `S_3`'s standard rep (a dihedral
group `D_3` of rotations by `0, +-120 deg` and three reflections — `180 deg`
rotation is absent).

**(2)** `H_dem = C + C^dagger = C + C^2 = J - I` is the real circulant with
first row `(0,1,1)` (since `I + C + C^2 = J`); its eigenvalues are
`2 Re(omega^k)` for `omega = e^{2 pi i/3}`, i.e.
`{2, -1, -1}`, with the `+2` eigenvector `W`. By the spectral mapping,
`exp(i t H_dem) = e^{2 i t} P_W + e^{-i t}(I - P_W)`. At `t = pi/3`:
`e^{2 i pi/3} P_W + e^{-i pi/3}(I - P_W)`. Since `e^{-i pi/3} = -e^{2 i pi/3}`,
this equals `e^{2 i pi/3}(P_W - (I - P_W)) = e^{2 i pi/3}(2 P_W - I) =
e^{2 i pi/3} S`. The runner confirms `|tr(U^dag S)|/3 = 1` and
`U = e^{2 i pi/3} S` to `1e-12`.

**(3)** `S^2 = P_23^2 = I`, and `S, P_23` commute (both are block operators
respecting the `W` / doublet split; `P_23` acts within each block, `S` is
`+1`/`-1` on the blocks), so `<S, P_23> = {I, S, P_23, S P_23}` is abelian
with every element an involution: the Klein four-group. The runner enumerates
the closure and checks order `4`, abelian, all involutions.

**(4)** `[M_nu, S] = 0` forces `M_nu` block-diagonal in `span{W} ⊕ doublet`,
so `W` is an eigenvector; with `U_e = I`, the corresponding PMNS column is
`W = (1,1,1)/sqrt(3)`, magnitudes `1/3` (trimaximal). `[M_nu, P_23] = 0`
gives the mu-tau modulus residual, hence (by the cited TM2 lemmas) maximal
atmospheric mixing. The doublet `2x2` block of `M_nu` is unconstrained by
`V_4`, so its eigenvectors carry a free `theta_13`. The runner constructs a
`V_4`-symmetrized `M_nu`, checks it commutes with `S` and `P_23`, is **not**
circulant, and reads off the exact trimaximal column + equal mu-tau rows.

**(5)** The runner scans `W`-preserving operators `a |W><W| + B_doublet` and
exhibits one with an exact trimaximal column and `sin^2 theta_13` proxy
`= 0.0213`; the full-circulant control returns all magnitudes `= 1/3`.

## Boundary

This note does **not**:

- **Derive that `M_nu` commutes with `V_4`.** This is the open gap. The
  current DM-neutrino source operator
  ([`PMNS_FROM_DM_NEUTRINO_SOURCE_H_DIAGONALIZATION_CLOSURE_THEOREM_NOTE_2026-04-17.md`](PMNS_FROM_DM_NEUTRINO_SOURCE_H_DIAGONALIZATION_CLOSURE_THEOREM_NOTE_2026-04-17.md),
  `unaudited`) has **non-zero** frozen singlet-doublet slots and therefore
  **breaks** `W` (does not commute with `S`). So `V_4`-invariance of `M_nu`
  is currently **contested**, not assumed. What this note shows is that the
  obstruction is a residual-symmetry-selection question, not a flavor-group-
  size impossibility, and that `theta_13` does not exclude the `W`-preserving
  branch.
- **Audit the charged-diagonal premise `U_e = I`.** The eigenvalue-only Koide
  content is retained and is basis-free, and the framework's stated readout is
  axis-diagonal, but the `U_e = I` readout itself is `unaudited` (separate
  authority).
- **Select the evolution time `t = pi/3`.** The coupling itself is native:
  `H_dem = C + C^dagger = J - I` is the retained_bounded double-shift corner
  coupling (not an imported Hamiltonian, not a diagonal edge — see Safe
  statement). What is *not* selected here is the specific evolution time
  `t = pi/3` that maps it to the magic reflection; item 2 is an existence
  statement ("`S` lies in the native double-shift coupling's time-evolution
  closure"). See the Forbidden imports check.

## No-Go Discipline Gate

**Status:** PASS for the narrow static-non-membership lemma (Theorem item 1)
only. The negative content is the single statement "the magic `S` is not a
static `S_3` generation symmetry." The note's thrust is positive: that same
`S` is reachable dynamically, so item 1 is *bypassed*, not promoted to an
impossibility.

### N1 — Alternative route enumeration

| route | attempt | status |
|---|---|---|
| Static `S_3` permutation | realize `S` as a corner permutation | fails: `S` non-monomial (item 1) |
| Static `S_3` + single-qubit phases | realize `S` as a monomial op | fails: `S` non-monomial |
| Enlarge flavor group to `A_4`/`S_4` | host `V_4` statically | not realized by framework; left OPEN as a positive route |
| **Dynamical evolution of native `C_3`-coupling** | `exp(i pi/3 (C+C^dag))` | **SUCCEEDS** (item 2) — this is the route taken |

### N2 — Wall-independence audit

The single static wall (`S not in S_3`) is independent of the dynamical
realization: enlarging or not enlarging the static flavor group does not
change the spectral identity `exp(i pi/3 H_dem) = phase * S`.

### N3 — Hidden-wall scan

Load-bearing inputs are explicit and finite-dimensional: the magic matrix
`S`, the cyclic shift `C`, `P_23`, the spectral mapping theorem, and
Lagrange's theorem. "Native", "framework", and "democratic" are not used as
hidden retained inputs for the negative lemma.

### N4 — Residual matching

| witness | residual | here | match? |
|---|---|---|---|
| `PMNS_GRAPH_FIRST_AXIS_ALIGNMENT_NOTE` | `P_23` mass-operator symmetry | the mu-tau half of `V_4` | yes |
| `PMNS_TM2_*_2026-05-26` | assumed trimaximal column + mu-tau residual | the consequences this note feeds | yes |
| `NEWPHYSICS_NP_NEUTRINO_PMNS_NOTE_2026-05-10_npNu` | full-circulant => TM3 overshoot | the negative control this note reframes (tests only full circulant) | yes (as reframed) |

### N5 — Rhetoric audit

"Not in `S_3`" is scoped to the static permutation group. The note does not
claim the magic `S` is unrealizable, nor that TM2 is impossible — the opposite
is shown. No "only/last/closes/exhausted" framing is used.

### N6 — Partial-closure path scan

Open positive paths left explicitly open: (a) derive `M_nu`'s `V_4`-invariance
(`W`-preservation) natively; (b) select the democratic coupling and the time
`t = pi/3` from the dynamics; (c) audit `U_e = I`. None is called a new axiom.

### N7 — Steelman

Strongest objection: a "residual symmetry" is conventionally a static element
of the flavor group, and `S` is not such an element, so calling it a residual
is non-standard. Response: TM2 requires only that `M_nu` *commute with the
matrix* `S` (a static condition on `M_nu`); item 2 shows that matrix is a
native dynamical unitary, which is what makes requiring `[M_nu, S]=0` an
import-free condition rather than a foreign-symmetry import. The steelman
blocks the stronger claim "`S` is a static flavor-group residual"; it does not
block "`S` is a native operation and `[M_nu,S]=0` is an admissible condition."

### N8 — Cross-cycle echo

Prior repo overclaims declared a lane closed after testing one representative
operator. The `npNu` "must break the democratic structure" reading is exactly
such an echo (it tested only the full circulant). This note avoids the echo by
exhibiting the untested intermediate (`W`-preserving) operator and confirming
it fits `theta_13`.

## Forbidden imports check

No new axiom or imported structure is asserted. `C`, `P_23`, `S`, and `H_dem`
are finite matrices on the existing `hw=1` carrier. `H_dem = C + C^dagger = J - I`
is **not** an imported Hamiltonian: it is the retained_bounded native
second-order double-shift corner coupling
(`FLAVOR_NATIVE_DOUBLE_SHIFT_CORNER_COUPLING_NOTE_2026-05-30`,
`P(sum_{a<b} S_a S_b)P^T = J - I`), and the framework's lattice has **no**
diagonal edges (6-NN cubic adjacency; a first-order single shift `P S_mu P^T = 0`
annihilates the triplet), so `H_dem` is the genuine two-step object rather than
a non-existent diagonal bond. The note does **not** import a specific neutrino
dynamics — item 2 is an existence statement ("`S` is in the time-evolution
closure of the native double-shift coupling"; only the time `t = pi/3` is not
selected), and item 4 is conditional on an explicitly-undischarged `M_nu`
residual. The charged-diagonal premise is flagged as a separate unaudited
authority.

## Runner check breakdown

The paired runner exercises class A finite-dimensional algebra only: magic-`S`
spectrum/involution/`W`-fix, non-membership in `S_3` (permutation + monomial
+ Lagrange), the spectral identity `exp(i pi/3 H_dem) = exp(2 i pi/3) S`, the
`<S,P_23> = V_4` closure, the `V_4`-invariant-`M_nu` => TM2 (trimaximal column
+ mu-tau modulus + maximal atmospheric, non-circulant) consequence, the
`W`-preserving `theta_13`-in-band exhibit, and two negative controls
(full-circulant => TM3; charged-circulant rotation destroys the trimaximal
column). Expected `runner_check_breakdown = {A: N, B: 0, C: 0, D: 0,
total_pass: N}` where `N` is the printed `PASS` count in the cache.

## Honest auditor read

The runner performs explicit class A matrix algebra; every load-bearing
equality is checked to `1e-12`. The positive content (items 1–3, 5 and the
conditional item 4) is exact and self-contained. The physics value is the
**reframing**: an apparent flavor-group-size no-go for the TM2 trimaximal
column is dissolved into a residual-symmetry question with a native generator,
and the `theta_13` "must break `W`" reading is shown to test only the full
circulant. The note does not close TM2: the neutrino `V_4`-invariance
(`W`-preservation) is open and currently contested by the unaudited
DM-neutrino source operator, and the charged-diagonal readout is a separate
unaudited authority. Effective status remains `unaudited` until the
independent audit lane assigns one.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/pmns_tm2_magic_residual_dynamical_generator_runner.py
```
