# The Bare One-Loop Velocity Anisotropy is Discretization-Artifact-Dominated — No Falsification from It; the Staggered (Taste-Protected) Computation is Decisive

**Date:** 2026-06-07
**Claim type:** bounded_theorem (a bare lattice quantity is shown to be discretization-dependent, hence not physical)
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_velocity_anisotropy_discretization_artifact_2026_06_07.py`](../scripts/frontier_velocity_anisotropy_discretization_artifact_2026_06_07.py)
**Cached runner output:**
[`logs/runner-cache/frontier_velocity_anisotropy_discretization_artifact_2026_06_07.txt`](../logs/runner-cache/frontier_velocity_anisotropy_discretization_artifact_2026_06_07.txt)

---

## Role

Follow-up sharpening of the doubler-artifact validation
(`VELOCITY_ANISOTROPY_DOUBLER_ARTIFACT_VALIDATION_NOTE_2026-06-07`, #3153). That note
showed the alarming `δv ≈ 0.31` was a naive-fermion **doubler** artifact, and that a
doubler-free Wilson fermion gave a finite `~0.058`. This note shows the **remaining**
bare off-shell `δv = B − A` is itself **strongly discretization-dependent** — so it
is *not* a physical continuum quantity, and **no falsification can be read off it**.
The framework's actual **staggered** fermion (taste-protected) is the decisive
computation. Runner **10 PASS / 0 FAIL**.

## The argument

### (A) Strong Wilson-parameter dependence
The Wilson `δv = B − A` varies by a factor of **~5.4** across the Wilson parameter
`r ∈ [0.3, 2.0]`:

```text
    r:     0.3      0.6      1.0      1.5      2.0
    B-A:  0.161    0.096    0.0597   0.0396   0.0297
```

A *physical* renormalization would be `r`-independent (the Wilson parameter is an
unphysical regulator knob). It is not. The earlier `~0.058` was just the `r = 1`
point.

### (B) Different regulator → different value
A scalar-mass regulator (chiral-breaking, no doubler removal) gives `δv` varying
with `m` (`0.232, 0.158, 0.084` for `m = 0.5, 1, 2`) — a *different* discretization
yields a *different* bare `δv`.

### (C) The bare `δv` is an additive lattice artifact
Across `{naive (doublers), Wilson(r), scalar-mass(m)}` the bare off-shell `δv` spans
**`~0.03` to `~0.31`** — dominated by the *fermion-action choice*, not by physics. By
standard lattice perturbation theory the bare self-energy carries additive
discretization artifacts that must be **matched/subtracted** (continuum-extrapolated)
to obtain the physical renormalization. The bare value is not that physical number.

### (D) The framework's staggered fermion is the decisive computation
The framework's actual fermion is **staggered**: 4 tastes (not naive's 16, not
Wilson's explicit chiral breaking), preserving a remnant chiral/taste `U(1)`. Crucially,
the **free staggered 2-point function has an exact tree-level SO(4)** (Euclidean
Lorentz) — the on-repo
[`LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md`](LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md)
result. The chiral-breaking that *sources* the Wilson/scalar-mass anisotropy is
**absent** in staggered.

> **Hypothesis (decisive, to be computed):** the staggered taste symmetry **protects**
> the velocity anisotropy, giving `δv ≪` the chiral-breaking Wilson/naive values
> (possibly `≈ 0`). If so, this is genuinely new: a *staggered* lattice gauge theory
> protects emergent Lorentz where generic lattice fermions do not.

## Verdict

- **No falsification** follows from the discretization-artifact-dominated bare `δv`
  (`0.03–0.31` by action). The framework is **not** falsified by these numbers.
- The physical `δv` is **uncomputed** — it requires continuum matching **and** the
  framework's staggered fermion.
- The **decisive remaining computation** is the staggered velocity renormalization
  (the taste-protection test). The exact tree-level SO(4) is a strong hint it is
  small/zero; that computation is the genuine pass/falsify, and the right next target.

This continues the de-bugging of route 1: naive `→ 0.31` (doublers, #3153); Wilson
`→ 0.03–0.16` (`r`-dependent chiral breaking, this note); physical `→` requires
staggered + matching. Each discretization probe further confirms the owner's
instinct — the alarming numbers are lattice artifacts, not the framework's prediction.

## What this note does NOT claim

- It does **not** claim `δv` is zero/small for staggered — that is the hypothesis to
  compute, not a result.
- It does **not** change the #3123 status (`δv` uncomputed at the physical level); it
  removes the temptation to read a falsification off the bare lattice value.
- **No** new axiom, primitive, repo vocabulary, or class tag; literature (Capitani
  lattice-PT; Groote–Shigemitsu) is comparator only. Sets **no** audit status.

## Reprove-and-cite ledger

- **Reproven here** (runner): the Wilson-parameter scan (`B − A` varies 5.4× across
  `r`); the scalar-mass scan; the `~0.03–0.31` span across discretizations; the
  framework's staggered-fermion / tree-SO(4) facts as the decisive route.
- **Cited** (comparator only): Capitani, *Phys. Rept.* 382 (2003) 113
  (hep-lat/0211036, lattice-PT additive renormalization); Groote–Shigemitsu,
  hep-lat/0001021; the on-repo free-staggered SO(4) two-point result.

## Audit dependency repair links

- [LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md](LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md)
- [LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md](LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md)
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)
- `VELOCITY_ANISOTROPY_DOUBLER_ARTIFACT_VALIDATION_NOTE_2026-06-07.md` (the parent #3153; not yet on main — backticked)

### Source-note boundary

**Hypothesis set:** (1) the one-loop fermion velocity self-energy on the spatial-lattice
+ continuous-time surface; (2) Wilson(`r`), scalar-mass(`m`), and naive fermion
discretizations; (3) the framework's staggered fermion + its tree-level SO(4) as the
decisive route. The result is a numerical demonstration that the bare off-shell `δv`
is discretization-dependent (an artifact).

**Forbidden-imports check:** no new axiom, primitive, repo vocabulary, or class tag;
only standard lattice-PT terms (Wilson parameter, additive renormalization, staggered
tastes, continuum matching). No fitted/PDG/`g_bare` value consumed; literature
comparator only.

**No-promotion statement:** this note does **not** promote, demote, or set the audit
status of #3153, #3123, or any upstream row. The audit lane is the only status
authority.
