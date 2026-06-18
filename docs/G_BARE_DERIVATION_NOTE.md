# g_bare Conditional beta=6 Corollary

**Date:** 2026-04-12
**Branch:** `claude/youthful-neumann`
**Lane:** DM relic mapping (Objection 1 from CODEX_DM_RESPONSE.md)
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_g_bare_derivation.py`

> **2026-06-18 source repair boundary:**
> This parent row is no longer a positive theorem deriving `g_bare = 1` or
> `beta = 6` from canonical Cl(3) normalization. It is only the bounded
> conditional algebraic corollary
>
> ```text
> CN + WM + supplied beta=6 + N_c=3  =>  g_bare^2 = 1
> ```
>
> where CN is canonical trace normalization and WM is Wilson small-`a`
> matching. The local `beta = 6` Wilson coefficient surface is an explicit
> scoped input here, not a result of this parent note.

---

## Status

**bounded conditional algebra / parent source repair.** The strongest honest
current-surface claim is that the exact algebra closes after the local
`beta = 6` Wilson coefficient surface is supplied. This edit is not a retained
status promotion, not a positive theorem, does not apply an audit verdict, and
does not add an axiom. The claim is not a dynamical calculation, not a fit, not
a fixed-point condition, and not a derivation of the Wilson action coefficient.

The canonical normalization itself remains the admitted upstream convention
layer; this note does not derive that convention from `A1 + A2` alone. The
local `beta = 6` surface also remains open unless a separate retained theorem
derives it.

This note is the **older bounded normalization route**. For the sharper
operator-algebra response to the old rescaling objection, see
[G_BARE_RIGIDITY_THEOREM_NOTE.md](/Users/jonBridger/Toy%20Physics-dm/docs/G_BARE_RIGIDITY_THEOREM_NOTE.md:1).
That newer note does not claim a dynamical fixed-point selection of `g = 1`;
it argues instead that, once the concrete `su(3)` operator algebra is fixed,
there is no independent bare coupling parameter left.

The repaired parent claim is:

> Given canonical trace normalization, Wilson matching
> `beta = 2 N_c / g_bare^2`, supplied `beta = 6`, and `N_c = 3`, exact
> arithmetic gives `g_bare^2 = 1`; on the positive branch, `g_bare = 1`.

---

## Theorem / Claim

**Claim (conditional beta=6 algebra):**

Given:

1. The Cl(3) algebra generators satisfy {G_mu, G_nu} = 2 delta_{mu,nu}
2. The canonical Cl(3) connection normalization
   `Tr(T_a T_b) = delta_ab / 2`
3. The accepted Wilson plaquette small-a matching
   `beta = 2 N_c / g_bare^2`
4. The scoped Wilson coefficient input `beta = 6`
5. `N_c = 3`

Then exact arithmetic gives `g_bare^2 = 2 N_c / beta = 1`. On the positive
branch, `g_bare = 1`.

**Proof sketch:**

- The canonical Cl(3) generator normalization fixes the finite carrier Gram
  surface used for the Wilson connection.
- The rescaling repair now proves only a Gram-scaling lemma: a nontrivial
  `T_a -> c T_a` changes the canonical trace surface by `c^2`. It does not
  derive beta routing.
- The constraint-vs-convention repair now proves only the conditional algebra
  corollary. It explicitly treats `beta = 6` as supplied.
- With `N_c = 3`, Wilson matching gives
  `g_bare^2 = 2 N_c / beta = 6 / 6 = 1` only after the scoped `beta = 6`
  surface is supplied.

**Consequence:** supplied `beta = 6` implies `g_bare = 1` on the positive
branch. This note does not prove `beta = 6`.

---

## Inputs

1. **Cl(3) algebra:** `{G_mu, G_nu} = 2 delta_{mu,nu}`.
2. **Canonical connection normalization:**
   `Tr(T_a T_b) = delta_ab / 2`.
3. **Wilson matching surface:** `beta = 2 N_c / g_bare^2`.
4. **Scoped beta surface:** `beta = 6` is supplied to this parent row.
5. **Color rank:** `N_c = 3`.

The first input is the local algebraic starting point. The second is the
admitted canonical normalization surface. The third is the Wilson matching
surface. The fourth is an explicit scoped input, not a new axiom and not a
result of this note.

---

## What Is Actually Proved

**Exact conditional result:**

- `CN + WM + beta=6 + N_c=3 => g_bare^2 = 1`.
- On the positive-coupling branch, this gives `g_bare = 1`.
- The Gram-scaling dependency only says nontrivial scalar carrier rescaling
  changes the canonical trace surface; beta-routing remains separate.
- The convention layer is explicitly at canonical normalization and at the
  supplied beta surface, not at a hidden separate `g_bare` choice.

**Bounded results (supporting but not standalone derivations):**

- The mean-field self-consistency ratio alpha_V/alpha_bare = 1.35 at g=1
  (moderate, not uniquely selecting)
- The mean-field iteration does NOT converge to g = 1 (it diverges)
- Maximum entropy does NOT select g = 1 (it selects g -> infinity)
- The SU(3) lattice beta function has NO nontrivial fixed point

**Numerical consequence:**

- At g = 1: alpha_plaq = 0.0923, and R(DM) = 5.48 (0.25% from observed 5.47)
- Sensitivity: g in [0.95, 1.05] gives R in [5.22, 5.78]

---

## What Remains Open

1. **Direct derivation of the local beta=6 surface.**
   This parent row does not derive the local Wilson coefficient surface
   `beta = 6`. A future theorem-grade supply of that surface would be needed
   before this can become an unconditional parent closure.

2. **Absolute derivation of canonical normalization remains open.**
   The canonical normalization is the admitted upstream convention layer.
   This note does not prove that the normalization itself follows from
   `A1 + A2` alone.

3. **The other two DM imports still stand:**
   - sigma_v = pi * alpha_s^2 / m^2 (perturbative QFT cross-section)
   - V(r) = -C_F * alpha_s / r (one-gluon exchange potential)

4. **Approaches that do NOT work:**
   - Strong-coupling fixed point: SU(3) has no nontrivial fixed point
   - Maximum entropy: selects g -> infinity, not g = 1
   - Mean-field iteration: diverges, does not converge to g = 1
   - Plaquette self-consistency: not uniquely selecting

---

## How This Changes The Paper

**Before:** g_bare = 1 was ASSUMED (Objection 1 in CODEX_DM_RESPONSE.md).
The DM provenance was: 7 NATIVE, 5 DERIVED, 1 ASSUMED, 2 IMPORTED.

**After this repair:** `g_bare = 1` is not a retained zero-input structural
constraint from this parent row. It is conditional algebra after supplying
`beta = 6`. The DM provenance remains blocked on a retained beta-surface
derivation before `g_bare` can move from supplied/conditional support to
derived.

**Paper-safe wording:**

> Relative to canonical trace normalization and the Wilson matching relation
> `beta = 2 N_c / g_bare^2`, a supplied local `beta=6` surface at `N_c=3`
> implies `g_bare=1` on the positive branch. The `beta=6` surface is a
> separate open input unless independently derived.

**What the paper should NOT say:**

- "g = 1 is derived from a dynamical fixed-point condition"
- "g = 1 is the maximum-entropy coupling"
- "g = 1 is selected by the lattice beta function"
- "canonical Cl(3) normalization alone derives beta = 6"
- "this parent row removes all continuum rescaling freedom"

These are false or stronger than this source surface. The repaired statement
is conditional algebra over the supplied beta surface, not a dynamical or
unconditional framework derivation.

---

## Commands Run

The original 2026-04-12 note recorded an older diagnostic runner with one
expected bounded failure from the mean-field fixed-point route. That historical
diagnostic is not the parent re-audit surface.

**2026-05-03 parent re-audit runner:**

```
python3 scripts/frontier_g_bare_derivation.py
```

Expected summary on the repaired parent source surface:

```
EXACT   : PASS = 73, FAIL = 0
BOUNDED : PASS = 0, FAIL = 0
TOTAL   : PASS = 73, FAIL = 0
```

---

## Provenance Chain Update

| Input | Value | Status (before) | Status (after) |
|-------|-------|-----------------|----------------|
| g_bare | 1.0 | stale bounded-normalization claim | conditional algebra from supplied beta=6 |
| sigma_v = pi*alpha^2/m^2 | -- | IMPORTED | IMPORTED (unchanged) |
| V(r) = -alpha/r | -- | IMPORTED | IMPORTED (unchanged) |

---

## Relationship to Other Approaches (from task specification)

| Approach | Result | Status |
|----------|--------|--------|
| (1) Unitarity bound | g=1 makes U unitary but so does any g | Not selecting |
| (2) Strong-coupling fixed point | SU(3) has no nontrivial fixed point | Does not work |
| (3) Canonical Cl(3) normalization + Wilson matching + supplied beta=6 | **g = 1 conditional corollary** | **bounded conditional algebra; beta=6 remains open** |
| (4) Maximum entropy | Selects g -> infinity | Does not work |
| (5) Staggered Dirac normalization | Consistent with g = 1 | Supporting, not standalone |
