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

> **2026-07-16 dependency correction.** The stable-path matrix theorem cited
> below now proves only a defined trace-Taylor coefficient equivalence. It does
> **not** supply a Wilson action or a physical matching dictionary. Every
> Wilson reading in this note is therefore conditional on the separately
> named input `W-PHYS`: identify the theorem's defined `beta D(gx)` coefficient
> with the Wilson action coefficient and its defined `1/2` coefficient with
> the target kinetic coefficient. A second, logically independent condition,
> `SLOT-ID`, identifies the resulting Wilson label `g_bare` with the
> finite-link canonical slot `s`. This note derives neither `W-PHYS` nor
> `SLOT-ID`; neither condition chain-satisfies a dependency.

The 2026-06-18 repair removes the circular-looking step in the older source
where the `beta = 2 N_c = 6` surface was effectively hard-coded and then used
to solve for `g_bare = 1`. The repaired parent now sources the two distinct
ingredients separately:

1. Finite-link canonical generator normalization supplies the scalar slot
   `g_link^2 = 1` inside the fixed `SU(3)` generator basis, from
   [`G_BARE_RIGIDITY_THEOREM_NOTE.md`](G_BARE_RIGIDITY_THEOREM_NOTE.md).
2. The defined matrix-trace coefficient theorem supplies the formal identity
   `beta g^2 = 2 n` after equality of its two internally defined
   coefficients, from
   [`WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md`](WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md).
3. The bridge theorem locates exactly when the two scalar slots coincide but
   does not choose their identification:
   [`G_BARE_PARENT_FINITE_LINK_WILSON_BETA6_BRIDGE_NOTE_2026-06-18.md`](G_BARE_PARENT_FINITE_LINK_WILSON_BETA6_BRIDGE_NOTE_2026-06-18.md).

Together with the explicit non-satisfying conditions `W-PHYS` and `SLOT-ID`,
these give the conditional
readout `beta = 2 N_c = 6` for `N_c = 3`. Without `W-PHYS`, they give only
the formal coefficient identity. Without `SLOT-ID`, finite-link rigidity does
not set `g_bare`. No physical Wilson conclusion follows from the cited
theorems alone.

---

## Status

**source-side repair candidate; parent re-audit required.** On the
finite-link canonical surface and conditional on `W-PHYS` and `SLOT-ID`, the parent proof
composes a canonical scalar-slot theorem with a formal coefficient theorem.
The claim is
not a dynamical calculation, not a fit, not a running-coupling fixed point,
and not a derivation of the Wilson action form itself.

The canonical finite-link statement is bounded: it says that, once the
concrete `SU(3)` operator algebra and fixed trace form are in place, the
finite link is written in canonical generator coordinates with no additional
scalar multiplier. The matrix theorem is dependency-free but formal: it gives
a coefficient relation only between expressions defined inside its packet.

The parent claim after this repair is:

> Conditional on `W-PHYS` and `SLOT-ID`, on the explicit standard Wilson plaquette surface with the canonical
> finite-link `SU(3)` generator basis, the Wilson coefficient scalar is the
> same scalar slot eliminated by finite-link rigidity. Hence
> `g_bare^2 = 1`, and `W-PHYS` maps the formal matrix identity to
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
3. The defined matrix-trace theorem gives `beta g^2 = 2n` only as a formal
   coefficient equality.
4. `W-PHYS` identifies `(n,g)` with `(N_c,g_bare)` and identifies the two
   formal coefficients with the Wilson and target kinetic coefficients.
5. `SLOT-ID` identifies that Wilson label `g_bare` with the finite-link
   canonical scalar slot `s=1`. This is a separate condition, not a theorem
   output of the bridge row.
6. `N_c = 3`, and the positive-coupling branch is used.

Then exact rational arithmetic gives

```text
g_bare^2 = g_link^2 = 1,
beta = 2 N_c / g_bare^2 = 2 * 3 / 1 = 6.
```

This is a conditional finite-link/Wilson-surface implication. It does not
derive `W-PHYS` or `SLOT-ID` and does not assert a continuum
running coupling, a global logarithm branch, Wilson action-surface selection,
or a phenomenological fitted value.

---

## Proof Sketch

- The finite-link rigidity theorem proves that scalar dilation of the fixed
  canonical `SU(3)` generator basis is not an allowed normalization ambiguity.
  In canonical finite-link coordinates, standard notation writes this as
  `g_link = 1`.
- The matrix-trace theorem derives only its formal coefficient equivalence.
  `W-PHYS`, not that theorem, performs the Wilson/gauge-field dictionary.
- The 2026-06-18 bridge note proves the exact split redundancy and locates the
  equality point of the two slots; it explicitly does not choose the
  same-slot identification.
- Conditional on `SLOT-ID`, the Wilson label has `g_bare^2=s^2=1` on the
  canonical finite-link surface.
- Conditional on `W-PHYS`, substituting `N_c = 3` into that Wilson reading gives
  `beta = 6`.

No step uses `beta = 6` as a premise for `g_bare = 1`.

---

## Inputs

1. **One-qubit operator algebra / finite-link operator surface:** the concrete
   canonical `SU(3)` generator basis and finite-link logarithm surface cited
   through
   [`G_BARE_RIGIDITY_THEOREM_NOTE.md`](G_BARE_RIGIDITY_THEOREM_NOTE.md).
2. **Formal coefficient surface:** the defined theorem
   `beta g^2 = 2 n`, cited through
   [`WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md`](WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md).
3. **Physical dictionary `W-PHYS`:** the explicit, not-derived,
   non-chain-satisfying identification of those formal coefficients and
   symbols with the Wilson matching surface.
4. **Same-slot condition `SLOT-ID`:** the explicit, not-derived,
   non-chain-satisfying identification `g_bare=s`.
5. **Pin-equivalence bridge:** the 2026-06-18 theorem that locates when the
   two slots agree without choosing their identification.
6. **Group rank:** `N_c = 3`.

These conditions are not new axioms or approved primitives. They do not
chain-satisfy dependencies. Independent audit decides the bounded scope of
the conditional composition.

---

## What Is Actually Proved

**Exact conditional result if the bridge, `W-PHYS`, and `SLOT-ID` are all
explicitly imposed:**

- The finite-link canonical scalar slot is `g_link^2 = 1`.
- The formal matrix coefficient identity becomes
  `beta g_bare^2 = 2 N_c` only through `W-PHYS`.
- `SLOT-ID`, not the bridge, identifies `g_bare` and `g_link` as the same
  scalar slot on this explicit Wilson surface.
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

If `W-PHYS` and `SLOT-ID` are explicitly imposed and independent re-audit accepts the conditional
composition, safe wording is:

> On the supplied standard Wilson plaquette surface, the scalar multiplying
> the canonical finite-link `SU(3)` generator basis is the same scalar slot
> removed by finite-link gauge-normalization rigidity. Thus the canonical
> finite-link normalization gives `g_bare^2 = 1`; conditional on the supplied
> Wilson coefficient dictionary, the formal matrix theorem then gives
> `beta = 2 N_c = 6` for `N_c = 3`.

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
TOTAL: PASS=103 FAIL=0

frontier_g_bare_derivation.py
EXACT   : PASS = 51, FAIL = 0
BOUNDED : PASS = 16, FAIL = 0
TOTAL   : PASS = 67, FAIL = 0
```

These runners do not inspect or edit audit ledgers, audit queues,
publication matrices, or effective-status surfaces.

---

## Provenance Chain Update

| Input | Value | Source-side status before repair | Source-side status after repair |
|---|---:|---|---|
| finite-link canonical scalar slot | `g_link^2 = 1` | cited as context only | load-bearing via finite-link rigidity |
| formal coefficient identity | `beta g^2 = 2 n` | cited but not composed with finite-link scalar slot | load-bearing as formal algebra only; Wilson use additionally requires `W-PHYS` |
| beta surface | `beta = 6` at `N_c = 3` | effectively hard-coded in parent runner | exact consequence only under `W-PHYS` and `SLOT-ID` |
| `sigma_v = pi*alpha^2/m^2` | -- | imported | imported, unchanged |
| `V(r) = -alpha/r` | -- | imported | imported, unchanged |

---

## Relationship to Other Approaches

| Approach | Result | Status |
|---|---|---|
| Unitarity bound | `g=1` makes `U` unitary, but so does any real `g` | Not selecting |
| Strong-coupling fixed point | `SU(3)` has no nontrivial fixed point | Does not work |
| Finite-link rigidity + formal coefficient identity + `W-PHYS` + `SLOT-ID` | conditional `g_bare^2=1`, `beta=6` on explicit Wilson surface | Source-side conditional candidate; re-audit required |
| Maximum entropy | Selects `g -> infinity` | Does not work |
| Staggered Dirac normalization | Consistent with `g = 1` | Supporting, not standalone |
