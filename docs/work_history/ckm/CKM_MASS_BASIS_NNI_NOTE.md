# CKM Mass-Basis NNI Reparameterization Boundary

**Date:** 2026-07-12
**Type:** no_go
**Claim type:** no_go
**Status:** source-side exact negative boundary; independent audit is required
before any effective-status change.
**Claim scope:** if the displayed coefficient map
`p_ij = g_ij sqrt(mu_i/mu_j)` is used as a reparameterization of the same
Hermitian texture, it cannot suppress a CKM entry. The historical `1.14 x`
output inserts `p_13` into the geometric reconstruction law and therefore
computes a different texture. Whether that operation is intended as a
physical deformation is a separate open interpretation and derivation route.
**Script:**
[`scripts/frontier_ckm_mass_basis_nni_reparameterization_no_go.py`](../../../scripts/frontier_ckm_mass_basis_nni_reparameterization_no_go.py)
**Cached output:**
[`logs/runner-cache/frontier_ckm_mass_basis_nni_reparameterization_no_go.txt`](../../../logs/runner-cache/frontier_ckm_mass_basis_nni_reparameterization_no_go.txt)

The previous numerical runner is preserved at
`scripts/frontier_ckm_mass_basis_nni.py` as historical instrumentation. Its
PDG masses, fitted coefficients, and PDG CKM entries remain observational and
fitted inputs. They are not used by the theorem or its primary runner.

## Exact result

Let `0 < mu_1 < mu_2 < mu_3` and let a Hermitian texture be parameterized in
the geometric convention by

```text
M_ij = g_ij sqrt(mu_i mu_j),                 i < j,
M_ji = conjugate(M_ij).
```

Define the displayed coefficient map

```text
p_ij = Phi_ij(g_ij) = g_ij sqrt(mu_i/mu_j), i < j.
```

Solving for `g_ij` and substituting into the same matrix entry gives the
unique consistent reconstruction law

```text
g_ij = p_ij sqrt(mu_j/mu_i),
M_ij = p_ij mu_j.                            (1)
```

Therefore

```text
R_phys(Phi(g))_ij
  = p_ij mu_j
  = g_ij sqrt(mu_i/mu_j) mu_j
  = g_ij sqrt(mu_i mu_j)
  = R_geom(g)_ij.                            (2)
```

Equation (2) is entrywise equality of the matrices. Consequently their
spectra and diagonalizer sets agree. For nondegenerate spectra, matched mass
ordering and phase conventions give the same CKM moduli. With degeneracies,
the set of possible CKM moduli is the same, and an identical basis choice
inside each common degenerate eigenspace gives identical moduli. A consistent
same-texture application of `Phi` cannot suppress or enhance `|V_ub|`; it
changes coefficient coordinates, not the matrices.

## What the historical runner actually computes

The historical runner forms

```text
p_13 = g_13 sqrt(mu_1/mu_3)
```

and then inserts `p_13` into the *geometric* reconstruction law. That gives

```text
M_13^legacy
  = p_13 sqrt(mu_1 mu_3)
  = g_13 mu_1,                               (3)
```

whereas the original entry is

```text
M_13^geom = g_13 sqrt(mu_1 mu_3).            (4)
```

Thus

```text
M_13^legacy / M_13^geom = sqrt(mu_1/mu_3).   (5)
```

For `g_13 != 0` and `mu_1 < mu_3`, equations (3) and (4) are unequal. The
factor advertised as “mass-basis suppression” is exactly the factor by which
the runner changes the matrix entry after mixing the two reconstruction
conventions.

This is not a merely verbal distinction. Holding every other entry fixed,
the Hermitian Frobenius invariant changes by

```text
tr[(M^legacy)^2] - tr[(M^geom)^2]
  = 2 |g_13|^2 mu_1 (mu_1 - mu_3) < 0.       (6)
```

So the legacy insertion is a genuine texture deformation. It may change a
numerically diagonalized CKM matrix, but that change is not produced by a
same-texture coordinate transformation. Calling the deformation a physical
normalization would require a separate semantic and dynamical authority; this
note neither assumes nor rules out that interpretation.

## Independent obstruction to the “mass-eigenvalue” wording

The historical construction also uses `mu_i` as diagonal entries while
calling them mass eigenvalues. For a Hermitian instance with any nonzero
off-diagonal coefficient,

```text
tr(M^2) - sum_i mu_i^2
  = 2 sum_{i<j} |g_ij|^2 mu_i mu_j > 0.       (7)
```

If the eigenvalue multiset of `M` were `{mu_1,mu_2,mu_3}`, the left-hand side
would be zero. Hence the displayed non-diagonal matrix cannot simultaneously
have the `mu_i` as its diagonal entries and as its eigenvalues. A different
inverse-eigenvalue construction could adjust the diagonal entries, but the
historical runner does not perform one.

Equation (7) is a second exact obstruction. It is not needed for the
reparameterization no-go in equations (1)-(6), but it prevents the current
matrix builder from supplying the missing eigenvalue-to-texture bridge by
terminology alone.

## Schur-chain identity retained at its safe boundary

If `g_13 = g_12 g_23`, then the coefficient map still obeys the exact chain

```text
p_13 = p_12 p_23,
```

because the square-root ratios multiply. This is a coefficient identity. It
does not identify `p_13` with `V_ub`, and it does not override the
reconstruction identity `M_13 = p_13 mu_3`.

The standalone structural note
`docs/CKM_MASS_BASIS_NNI_STRUCTURAL_IDENTITIES_NARROW_THEOREM_NOTE_2026-06-17.md`
is context only and is not a load-bearing dependency of the present proof;
the primary runner reconstructs all algebra used here.

## Consequence for the former `1.14 x` statement

The old claim that the displayed map, *as a same-texture normalization*,
suppresses the geometric `|V_ub|` overshoot to approximately `1.14` times a
quoted PDG value does not survive this exact check. The numerical statement
has three separate layers:

1. imported PDG quark masses;
2. fitted geometric coefficients and an imported PDG CKM comparator;
3. a texture deformation obtained by using `p_13` with the geometric rather
   than the converted reconstruction law.

Deriving the masses or coefficients would retire the first two imports, but
it would not turn layer 3 into a same-texture reparameterization. A
reparameterization of an unchanged matrix remains observable-invariant. To
retain a positive numerical route, a future source could interpret and derive
the *deformed texture itself* and a physical texture-to-CKM bridge, then
compare its independently derived output with observation. That separate
physical-deformation route remains open.

The current quark-mass authority independently confirms that five non-top
quark masses remain open rather than framework-derived; see the
non-load-bearing route context
`docs/lanes/open_science/03_QUARK_MASS_RETENTION_OPEN_LANE_2026-04-26.md`.
No quark mass or CKM observation is needed for the exact negative boundary.

## No-go discipline gate

### N1 — Alternative routes

| Attack route | Attempt and result | Marker |
|---|---|---|
| Consistent coefficient reparameterization | Reconstruct with `M_ij=p_ij mu_j`; equation (2) returns the original matrix entrywise, so no CKM observable changes. | `ATTEMPTED` — symbolic proof and exact controls in the primary runner |
| Active unitary basis change | A common weak-basis change acts on the matrices and their diagonalizers covariantly; it cannot turn equation (2) into the changed entry (3). The runner’s operation is not such a transformation. | `ATTEMPTED` — matrix-equality and CKM-invariance controls |
| Interpret the legacy insertion as a new texture | This does change CKM numerically, but equations (5)-(6) show why: it changes a matrix invariant. It escapes only by abandoning the normalization claim. | `ATTEMPTED` — exact invariant and synthetic two-sector controls |
| Derive the quark mass hierarchy first | Framework-derived `mu_i` would remove an input import but equation (2) holds for every positive triple, so it cannot make a reparameterization suppress `V_ub`. | `ATTEMPTED` — universal symbolic variables; current mass lane checked as route context |
| Derive the geometric coefficients first | Framework-derived `g_ij` would remove fitted inputs but equations (2), (5), and (6) hold for every nonzero coefficient, so it cannot repair the reconstruction mismatch. | `ATTEMPTED` — universal symbolic coefficients |
| Import the separate CKM atlas prediction | The atlas can supply an independent `V_ub` formula, but substituting that target into this texture would be a readout assumption or fit and would not turn the legacy deformation into normalization. | `ATTEMPTED` — dependency and circularity audit |

These routes close only the narrow proposition “the displayed normalization
itself produces the suppression.” They do not claim that no framework texture
can ever predict `V_ub`.

### N2 — Wall independence

The exact no-go has one algebraic wall, not an inflated list of independent
walls: consistent reconstruction returns the same matrix. Missing mass
derivations, coefficient derivations, and physical readout theorems are walls
for a *new positive texture prediction*, but none is a premise of equations
(1)-(6), and closing any of them does not alter the reparameterization
identity.

### N3 — Hidden-wall scan

The matrix-equality proof assumes only positive ordered scale labels and a
Hermitian texture with the displayed reconstruction laws; coefficients may be complex. “Mass
eigenvalue,” “NNI,” “Schur complement,” PDG data, fitted coefficients,
framework operators, and the minimal axioms are not hidden proof inputs. The
strict inequality in (6) additionally requires `g_13 != 0` and
`mu_1 < mu_3`; the matrix-equality result (2) does not. A unique CKM-modulus
representative additionally requires nondegenerate spectra or a common basis
prescription inside degenerate eigenspaces. Without that choice, equality
holds for the full set of allowed representatives rather than one unique
matrix of moduli.

### N4 — Residual matching

| Prior finding | Residual it attacked | Residual closed here | Match? |
|---|---|---|---|
| `docs/audit/data/audit_ledger.json:993647-993700` (2026-04-30 judicial history) | asserted identification of normalized coefficients with CKM observables | a same-texture coefficient reparameterization does not change the matrix or CKM moduli | yes, for the same-texture reading |
| `docs/audit/data/audit_ledger.json:993739` (2026-05-05 numerical-match history) | imported masses, fitted coefficients, and an asserted normalization bridge | the same-texture reading is invariant before numerical imports are evaluated | yes for that bridge reading; a physical-deformation reading remains open |
| `docs/QUARK_LANE3_BOUNDED_COMPANION_RETENTION_FIREWALL_NOTE_2026-04-27.md:32` | CKM closure is a mixing theorem, not a five-mass theorem | whether framework masses can rescue this same-texture map | no; retained only as route context, not a witness |

The audit histories are residual provenance, not premises of the theorem.

### N5 — Rhetoric audit

- Per-entry: equations (1)-(5) are exact for each upper-triangular entry.
- Whole single matrix: entrywise equality in (2) fixes the complete matrix.
- Two-sector CKM readout: identical up/down matrix pairs have the same
  diagonalizer sets. For nondegenerate spectra their CKM moduli agree after
  matched ordering and phases; for degenerate spectra the sets of possible
  CKM moduli agree, or a common basis prescription gives identical
  representatives. The runner verifies one nondegenerate synthetic control.
- Framework- or lattice-wide: not claimed. The theorem does not forbid a
  separately derived texture deformation or another flavor mechanism.

Accordingly, “cannot suppress” always means “cannot suppress by the displayed
map while representing the same matrix.”

### N6 — Partial-closure paths

There is a legitimate positive continuation: explicitly rename the legacy
operation a texture deformation, derive that deformation from retained
framework dynamics, derive its quark-mass and coefficient inputs, and prove a
texture-to-CKM observable bridge. No new axiom is automatically required;
ordinary retained theorems could in principle close those steps. The approved
scale-reference, kinetic-isotropy, and realized-state primitives supply no
mass ratio, coefficient, mixing angle, or flavor readout and are irrelevant
to the exact algebraic no-go.

### N7 — Steelman

The strongest objection is that the historical author may have intended
`p_13` not as a coordinate for the same matrix but as a physically distinct
mass-suppressed coupling prescription. Under that interpretation the changed
matrix is intentional, and the numerical scan is a valid exploration of a
new texture. This objection is correct but does not defeat the narrow no-go:
it concedes that the result is a deformation requiring its own dynamical and
observable derivation. The note therefore preserves the old runner as
historical instrumentation and rejects only the normalization-based closure.

### N8 — Cross-cycle echo

The required repo and no-go-ledger search found these similar wall shapes:

| Prior wall | Current/retired state | Retirement mechanism | Could it apply here? |
|---|---|---|---|
| Overall hypercharge-coordinate selection, `docs/audit/data/premise_decision_history.json:13-15` | reclassified as a vacuous normalization convention; the current source row is awaiting re-audit | convention reframe under reciprocal charge/coupling scaling | yes in method: distinguish coordinate reparameterization from physical content. Applied here by leaving the deformation interpretation open. |
| Bare-coupling coordinate selection, `docs/audit/data/premise_decision_history.json:16-21` | reclassified as a rescaling convention; the current source row is awaiting re-audit | reciprocal coupling/action normalization reframe | yes in method, but it cannot make two unequal matrices equal. |
| Endpoint-blind Route-2 renormalization, `docs/QUARK_ROUTE2_ENDPOINT_BLIND_RENORMALIZATION_NO_GO_NOTE_2026-06-21.md:24-54` | not retired; current row is unaudited | none; nonseparable physical readout remains the named escape | yes: a transformation that changes the invariant is new readout/texture content, not an endpoint-blind reparameterization. Used only as a similar-shape search result, not authority. |
| CKM-to-five-mass promotion, `.claude/science/physics-loops/lane3-quark-mass-retention-20260428/NO_GO_LEDGER.md:5-7` | not retired; five non-top masses remain open | no current retirement mechanism | no direct retirement of this algebraic result; it only confirms that deriving masses is a separate program. |

The earlier judicial history for this row identified a symbol-to-observable
renaming. The present proof resolves only the same-texture coordinate reading.
The convention-reframe examples prevent the stronger claim that all physical
meanings of the historical word “normalization” are impossible.

**No-go discipline disposition:** `PASS` for the narrow
reparameterization-only claim. The broader problems of deriving a physical
quark texture, five non-top masses, and a texture-to-CKM bridge remain open.

## Falsifiers and scope boundaries

The exact negative claim is falsified by either of the following:

- an algebraic counterexample to `p_ij mu_j = g_ij sqrt(mu_i mu_j)` under the
  displayed definition of `p_ij`;
- a nondegenerate pair of identical up/down matrices whose CKM moduli differ
  after matched eigenstate ordering and phase conventions solely because one
  pair is written with `g` and the other with `p`; or, in a degenerate case,
  unequal sets of possible CKM moduli for the two parameterizations.

The source-attribution claim that the historical runner computes a deformation
would separately be falsified if its source reconstructed the converted entry
as `p_13 mu_3`; it currently reconstructs with
`p_13 sqrt(mu_1 mu_3)`.

Not claimed:

- a first-principles value of any quark mass, NNI coefficient, CKM entry, or
  Jarlskog invariant;
- a global no-go against all NNI or other flavor textures;
- a no-go against a dynamically derived mass-suppressed texture;
- any audit verdict or publication promotion.

## Verification

```bash
python3 scripts/frontier_ckm_mass_basis_nni_reparameterization_no_go.py
```

The runner uses positive symbolic variables, exact rational matrices, and a
synthetic two-sector diagonalization control. It contains no PDG mass, CKM
entry, fitted flavor coefficient, observed target, or framework-derived
numeric value.
