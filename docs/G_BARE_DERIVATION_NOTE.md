# G Bare Finite-Link/Wilson Beta=6 Bridge

**Date:** 2026-04-12. Parent repair: 2026-06-18.
**Historical branch label:** `claude/youthful-neumann`
**Lane:** DM relic mapping (Objection 1 from CODEX_DM_RESPONSE.md)
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_g_bare_derivation.py`

> **Parent dependency-chain gate:**
> This note is a source-side repair candidate only. It does not set, predict,
> or apply an audit verdict. The parent row must be independently re-audited
> before downstream rows may cite it as retained-grade closure.

The 2026-06-18 repair removes the circular-looking step in the older source
where the `beta = 2 N_c = 6` surface was effectively hard-coded and then used
to solve for `g_bare = 1`. The repaired parent now sources the two distinct
ingredients separately:

1. Finite-link canonical generator normalization supplies the scalar slot
   `g_link^2 = 1` inside the fixed `SU(3)` generator basis, from
   [`G_BARE_RIGIDITY_THEOREM_NOTE.md`](G_BARE_RIGIDITY_THEOREM_NOTE.md).
2. The standard Wilson small-`a` coefficient theorem supplies
   `beta g_bare^2 = 2 N_c`, from
   [`WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md`](WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md).
3. The scalar-slot compatibility is recorded and checked by
   [`G_BARE_PARENT_FINITE_LINK_WILSON_BETA6_BRIDGE_NOTE_2026-06-18.md`](G_BARE_PARENT_FINITE_LINK_WILSON_BETA6_BRIDGE_NOTE_2026-06-18.md).

Together these give `beta = 2 N_c = 6` for `N_c = 3` on the supplied
standard Wilson action surface, without using `beta = 6` as an input to
derive `g_bare = 1`.

---

## Status

**source-side repair candidate; parent re-audit required.** On the
finite-link canonical Wilson surface, the parent proof now composes a
canonical scalar-slot theorem with a Wilson coefficient theorem. The claim is
not a dynamical calculation, not a fit, not a running-coupling fixed point,
and not a derivation of the Wilson action form itself.

The canonical finite-link statement is bounded: it says that, once the
concrete `SU(3)` operator algebra and fixed trace form are in place, the
finite link is written in canonical generator coordinates with no additional
scalar multiplier. The Wilson theorem is also bounded: it gives the
coefficient relation inside the supplied standard Wilson plaquette action.

The parent claim after this repair is:

> On the supplied standard Wilson plaquette surface with the canonical
> finite-link `SU(3)` generator basis, the Wilson coefficient scalar is the
> same scalar slot eliminated by finite-link rigidity. Hence
> `g_bare^2 = 1`, and the Wilson small-`a` theorem gives
> `beta = 2 N_c / g_bare^2 = 6` for `N_c = 3`.

---

## Theorem / Claim

**Claim (finite-link Wilson coupling normalization):**

Assume:

1. The framework's finite-link `SU(3)` holonomies are expressed in the fixed
   canonical generator basis `T_a` with `Tr(T_a T_b) = delta_ab / 2`.
2. In that basis, the finite-link rigidity theorem removes any independent
   scalar-normalization multiplier: the canonical link coordinate is the
   `g_link^2 = 1` slot.
3. The supplied standard Wilson plaquette small-`a` theorem gives
   `beta g_bare^2 = 2 N_c`.
4. The Wilson theorem's `g_bare` is the scalar multiplying the same canonical
   `T_a` slot in the link/plaquette exponent.
5. `N_c = 3`, and the positive-coupling branch is used.

Then exact rational arithmetic gives

```text
g_bare^2 = g_link^2 = 1,
beta = 2 N_c / g_bare^2 = 2 * 3 / 1 = 6.
```

This is a finite-link/Wilson-surface theorem. It does not assert a continuum
running coupling, a global logarithm branch, Wilson action-surface selection,
or a phenomenological fitted value.

---

## Proof Sketch

- The finite-link rigidity theorem proves that scalar dilation of the fixed
  canonical `SU(3)` generator basis is not an allowed normalization ambiguity.
  In canonical finite-link coordinates, standard notation writes this as
  `g_link = 1`.
- The Wilson small-`a` theorem defines its `g_bare` as the scalar multiplying
  the canonical generators in the standard Wilson plaquette exponent and
  derives `beta g_bare^2 = 2 N_c`.
- The 2026-06-18 bridge note checks that these are the same scalar slot on
  the parent surface: a scalar multiplying the fixed `T_a` basis in the
  finite link/plaquette exponent.
- Therefore the Wilson scalar slot has `g_bare^2 = 1` on the canonical
  finite-link surface.
- Substituting `N_c = 3` into the Wilson coefficient identity gives
  `beta = 6`.

No step uses `beta = 6` as a premise for `g_bare = 1`.

---

## Inputs

1. **One-qubit operator algebra / finite-link operator surface:** the concrete
   canonical `SU(3)` generator basis and finite-link logarithm surface cited
   through
   [`G_BARE_RIGIDITY_THEOREM_NOTE.md`](G_BARE_RIGIDITY_THEOREM_NOTE.md).
2. **Wilson matching surface:** the coefficient theorem
   `beta g_bare^2 = 2 N_c` inside the supplied standard Wilson plaquette
   action, cited through
   [`WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md`](WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md).
3. **Scalar-slot compatibility:** the 2026-06-18 bridge note that identifies
   the Wilson scalar slot with the finite-link canonical scalar slot.
4. **Group rank:** `N_c = 3`.

These inputs are not new axioms. They are existing source surfaces plus the
new explicit compatibility bridge. Independent audit decides whether the
composition is sufficient for the parent row.

---

## What Is Actually Proved

**Exact finite-link/Wilson-surface result if the bridge is accepted:**

- The finite-link canonical scalar slot is `g_link^2 = 1`.
- The Wilson small-`a` coefficient identity gives
  `beta g_bare^2 = 2 N_c`.
- The bridge identifies `g_bare` and `g_link` as the same scalar slot on this
  supplied Wilson surface.
- Therefore `g_bare^2 = 1` and `beta = 6` for `N_c = 3`.

**Bounded results (supporting but not standalone derivations):**

- The old scalar generator-dilation objection is routed into a change of the
  fixed trace form, not a physical scalar freedom in the canonical basis.
- Wilson action-form selection remains outside this parent.
- Global logarithm branch selection and continuum gauge-field limits remain
  outside this parent.
- The mean-field, maximum-entropy, and lattice-beta-function routes still do
  not select `g = 1`.

**Numerical consequence (downstream only after independent re-audit):**

- At `g = 1`: `alpha_plaq = 0.0923`, and `R(DM) = 5.48` (0.25% from
  observed 5.47).
- Sensitivity: `g` in `[0.95, 1.05]` gives `R` in `[5.22, 5.78]`.

---

## What Remains Open

1. **Independent parent re-audit.** This source repair does not change the
   parent row's effective status. The audit lane owns that decision.

2. **Wilson action-surface selection.** The bridge is internal to the supplied
   standard Wilson plaquette action. It does not prove that no Symanzik,
   heat-kernel, Manton, tadpole-improved, fermion-induced, or other action
   surface can be selected by different premises.

3. **Continuum/global gauge-field interpretation.** The finite-link theorem
   is not a global logarithm-branch theorem and not a continuum gauge-field
   limit theorem.

4. **The other two DM imports still stand:**
   - `sigma_v = pi * alpha_s^2 / m^2` (perturbative QFT cross-section)
   - `V(r) = -C_F * alpha_s / r` (one-gluon exchange potential)

5. **Approaches that do not work:**
   - Strong-coupling fixed point: `SU(3)` has no nontrivial fixed point.
   - Maximum entropy: selects `g -> infinity`, not `g = 1`.
   - Mean-field iteration: diverges, does not converge to `g = 1`.
   - Plaquette self-consistency: not uniquely selecting.

---

## Paper-Safe Wording

After independent re-audit accepts this parent composition, safe wording is:

> On the supplied standard Wilson plaquette surface, the scalar multiplying
> the canonical finite-link `SU(3)` generator basis is the same scalar slot
> removed by finite-link gauge-normalization rigidity. Thus the canonical
> finite-link normalization gives `g_bare^2 = 1`, and the Wilson small-`a`
> coefficient theorem gives `beta = 2 N_c = 6` for `N_c = 3`.

What the paper should not say:

- "g = 1 is derived from a dynamical fixed-point condition."
- "g = 1 is the maximum-entropy coupling."
- "g = 1 is selected by the lattice beta function."
- "The Wilson action form is uniquely forced by this parent note."
- "The finite-link result is a continuum running-coupling theorem."

---

## Commands Run

```text
python3 scripts/g_bare_parent_finite_link_wilson_beta6_bridge_2026_06_18.py
python3 scripts/frontier_g_bare_derivation.py
```

Expected summaries:

```text
g_bare_parent_finite_link_wilson_beta6_bridge_2026_06_18.py
TOTAL: PASS=37 FAIL=0

frontier_g_bare_derivation.py
EXACT   : PASS = 51, FAIL = 0
BOUNDED : PASS = 12, FAIL = 0
TOTAL   : PASS = 63, FAIL = 0
```

These runners do not inspect or edit audit ledgers, audit queues,
publication matrices, or effective-status surfaces.

---

## Provenance Chain Update

| Input | Value | Source-side status before repair | Source-side status after repair |
|---|---:|---|---|
| finite-link canonical scalar slot | `g_link^2 = 1` | cited as context only | load-bearing via finite-link rigidity |
| Wilson coefficient identity | `beta g_bare^2 = 2 N_c` | cited but not composed with finite-link scalar slot | load-bearing via Wilson small-`a` theorem |
| beta surface | `beta = 6` at `N_c = 3` | effectively hard-coded in parent runner | exact consequence of the bridge composition |
| `sigma_v = pi*alpha^2/m^2` | -- | imported | imported, unchanged |
| `V(r) = -alpha/r` | -- | imported | imported, unchanged |

---

## Relationship to Other Approaches

| Approach | Result | Status |
|---|---|---|
| Unitarity bound | `g=1` makes `U` unitary, but so does any real `g` | Not selecting |
| Strong-coupling fixed point | `SU(3)` has no nontrivial fixed point | Does not work |
| Finite-link rigidity + Wilson small-`a` matching | `g_bare^2=1`, `beta=6` on supplied Wilson surface | Source-side repair candidate; re-audit required |
| Maximum entropy | Selects `g -> infinity` | Does not work |
| Staggered Dirac normalization | Consistent with `g = 1` | Supporting, not standalone |
