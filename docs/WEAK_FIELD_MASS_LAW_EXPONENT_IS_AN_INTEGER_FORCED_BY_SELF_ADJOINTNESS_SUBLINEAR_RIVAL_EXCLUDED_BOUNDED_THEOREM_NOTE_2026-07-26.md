# The Weak-Field Mass-Law Exponent Is an Integer Forced by Self-Adjointness: the Sublinear Rival to Valley-Linear Is Excluded, Admission (c) Collapses into the A2 Coupling, and the P4 Rival Formula Is Misstated (Bounded Theorem)

**Date:** 2026-07-26
**Type:** bounded_theorem
**Claim type:** bounded_theorem (exact rational resolvent arithmetic and
closed-form perturbation coefficients; one unconditional exclusion, one
conditional reduction, one correction to a landed support note).
**Status authority:** none. Audit: unset. Constitutional effect: none. This
note edits no axiom, foundation, Qualification, primitive, registry, policy,
queue, audit-status, or PR-control surface. **It introduces no axiom and no
primitive, does not derive A2, and does not close admission (c).**
**Primary runner:**
[`scripts/physical_weak_field_exponent_from_self_adjointness_cycle707_2026_07_26.py`](../scripts/physical_weak_field_exponent_from_self_adjointness_cycle707_2026_07_26.py)
(8 PASS / 0 FAIL, exit 0).

## The gap this addresses

Probe P4 sharpened the `G_Newton` lane to three named admissions and recorded
this about the third:

> "(c) `S = L (1 - φ)` — weak-field test-mass response."
> "At least three weak-field action forms have been tested … valley-linear
> `S = L(1 - φ)` gives `F~M = 1.00` (Newtonian), spent-delay `S = L√(1 - φ)`
> gives `F~√M = 0.50` (NOT Newtonian) … **The selection of valley-linear is by
> EMPIRICAL match to `F~M = 1`, not by retained derivation. The audit ledger
> contains no retained 'weak-field-action derivation theorem'.**"
> — [`G_NEWTON_SELF_CONSISTENCY_BOUNDED_SHARPENING_NOTE_2026-05-10_planckP4`](G_NEWTON_SELF_CONSISTENCY_BOUNDED_SHARPENING_NOTE_2026-05-10_planckP4.md)

So a load-bearing input to a lane whose parent row carries 773 transitive
descendants is currently fixed by matching the known Newtonian answer.

The landed [`ACTION_UNIQUENESS_NOTE`](ACTION_UNIQUENESS_NOTE.md) observes, on
one fixed ordered-lattice family, that the mass-law exponent equals the
weak-field power `p` of the field in the action, and explicitly declines to
promote it: *"not promoted to a closed formula or a universal theorem"*. This
note does **not** re-observe that. It supplies a mechanism, and finds that the
stated discriminator is wrong.

## Answer

**Theorem 1 (the rival formula is misstated — correction).** P4 names the
rival as `S = L√(1 - φ)` and assigns it `F~M = 0.50`, in three separate places.
The **source code settles what was actually measured**. In
[`scripts/action_universality_probe.py`](../scripts/action_universality_probe.py),
`action_value()` defines the sqrt mode as

```python
if action_mode == "valley_sqrt":
    return L * (1.0 - np.sqrt(f))
```

that is `S = L(1 - √f)` — the square root is on the **field**, not on `1 - f`,
and the mode is named `valley_sqrt`, not "spent-delay". P4's expression is a
different function:

```text
1 - sqrt(1 - f) = f/2 + f^2/8 + ...
```

so `L√(1 - φ)` is weak-field **linear** — leading power exactly 1, coefficient
1/2 — placing it in the *Newtonian* class alongside `L(1-f)`, `L exp(-f)` and
`L/(1+f)`. Row B verifies both powers and the convergence `depth/f → 1/2`.

**The measured number is right; the formula and the label attached to it are
not.** Row I shows why the number survives: the genuinely geometric
spent-delay of
[`ACTION_CROSSOVER_NOTE`](ACTION_CROSSOVER_NOTE.md), `S = dl - √(dl² - L²)`,
expands with `dl = L(1+ε)` as

```text
S = L[(1+eps) - sqrt(2 eps + eps^2)]  ->  L[1 - sqrt(2 eps)],
```

so it is *also* sublinear with leading power 1/2 and coefficient `√2`. Three
expressions carry the "spent-delay/sqrt" name across the repo; two of them
(`L(1-√f)` and the geometric one) share the `p = 1/2` class and match the
measurement, and **P4's `L√(1-φ)` is the sole outlier**.

Consequence: **admission (c)'s stated discriminator, as written, does not
discriminate** — it compares valley-linear against another member of the
Newtonian class. The real rival is the sublinear class, which Theorem 2
excludes on different grounds, so the exclusion below is aimed at the genuine
alternative and not at a strawman.

**Theorem 2 (self-adjointness forces integer powers — unconditional).** Let
the field enter as a perturbation `H(λ) = H + λV` with `H` self-adjoint and
`V` self-adjoint and bounded. By Rellich/Kato, a self-adjoint family depending
analytically on `λ` has eigenvalues and spectral projections analytic in `λ`.
Hence every response has a leading power that is a **positive integer**:

| leading power | condition | row |
|---|---|---|
| `p = 1` | `⟨ψ|V|ψ⟩ ≠ 0` (Hellmann–Feynman) | C, D |
| `p = 2` | first-order term vanishes | E |
| `p = 1/2` | **unreachable** | F |

The half-power requires a branch point, which a self-adjoint analytic family
cannot have. Row F exhibits the branch point explicitly — `H(λ) = [[0,1],[λ,0]]`
has eigenvalues `±√λ` exactly — and confirms it is **not** self-adjoint, while
twelve self-adjoint samples all return powers 1 or 2 under a convergence test.

`H` is self-adjoint in this lane by the parent note's own CHECK 3. **So the
sublinear class is excluded by framework content, not by preference.**

**Theorem 3 (the propagator responds linearly — exact).** The connection to
the lane's own object needs no eikonal action and no eigenvalue. The resolvent
identity gives exactly

```text
G(λV) - G_0 = -λ · G_0 V G_0 + O(λ^2),
```

so the propagator's leading response power is 1 whenever `G_0 V G_0 ≠ 0`. Row H
verifies this in exact rational arithmetic on a `27×27` open-box Laplacian:
the residual of `(G(λ) - G_0)/λ` against `-G_0 V G_0` shrinks proportionally to
`λ` when `λ` is halved.

**Theorem 4 (what admission (c) reduces to).** Combining: if the field couples
additively to the propagator, the weak-field response is linear unless the
first-order matrix element vanishes. So admission (c) is not "select the
function `1 - φ` from an infinite menu". It is:

> **phase valley** (`g'(0) < 0`, row G — the landed sign requirement) **plus a
> nonvanishing first-order matrix element** (`⟨ψ|V|ψ⟩ ≠ 0`).

Both are genericity/sign conditions rather than a choice of functional form,
and every function satisfying them gives `F ∝ M` — the landed universality
class, now with a reason.

## Scope — what is conditional and on what

This is the load-bearing limitation and it is stated first rather than buried.

**The additive coupling is not derived.** Theorems 3 and 4 assume the field
enters as `H(φ) = H + φ`. That is the lane's own coupling, but the note it
comes from labels those bullets explicitly:

> "Heuristic motivation (not a proof, recorded for context only) … These four
> bullets are **physical-modelling motivation**, not a class-A or class-B
> proof."
> — [`GRAVITY_FULL_SELF_CONSISTENCY_NOTE`](GRAVITY_FULL_SELF_CONSISTENCY_NOTE.md)

So this note does **not** derive admission (c) from the axioms. What it does is
**collapse admission (c) into the same unforced premise the A2 heuristic
already uses**: previously (a) and (c) were two independent unforced inputs;
after this note, granting the additive coupling delivers both. That is a
reduction in the number of independent gaps, not a closure of any of them.

**What is unconditional:** Theorem 1 (the correction) and Theorem 2 (the
`p = 1/2` exclusion, which needs only self-adjointness).

**Other scope limits.**

- Theorem 2 is proved for bounded self-adjoint `V` on finite lattices. The
  infinite-volume statement needs Kato–Rellich hypotheses not checked here.
- The identification "valley depth ↔ propagator response" is made through
  Theorem 3 for the propagator. The further step to the *path action* `S` used
  by the landed harness is **not** established here and is flagged as the
  remaining seam.
- `f ∝ M` is the landed family's construction (field `s/r`, `s ∝ M`), not a
  result of this note.
- **`G_0 = H^{-1}` does not exist translation-invariantly.** The periodic
  Laplacian annihilates constants, so `H` is singular on the torus and the
  lane's `G_0` needs an open boundary (as the parent note's CHECK 3 quietly
  indicates by testing "interior sites") or a mass. Row H therefore uses an
  open box. This note records the issue and does **not** resolve it; it is a
  separate obstruction to A2 that appears not to be written down anywhere.
- No formation rule, no dynamics, no action is supplied. No lane, row or
  obligation status is changed, and no N1–N8 verdict is awarded.

## Controls and honesty record

- **Row A** cross-checks every closed-form valley depth against `1 - g(f)` at
  moderate `f`. Three drafting errors were caught by the runner and are
  recorded rather than silently fixed: evaluating `1 - g(f)` at `f = 1e-9`
  underflowed to exactly zero for `g = 1 - f²`; rows E and F subtracted
  nearly-equal eigenvalues and lost the entire second-order signal, reporting
  `p = 1.997` and then dividing by a response that had underflowed; and row F's
  detail string asserted "all integer" independently of the boolean it was
  reporting. All three are fixed, and the rationalized forms that fix them are
  documented in the runner.
- **Row F** uses a convergence test, not a fixed tolerance: the deviation from
  the nearest integer must both be small and shrink as `λ` shrinks. The earlier
  fixed 1e-9 tolerance failed on genuine `O(λ)` contamination, which is physics
  rather than float error.
- **Row G** reproduces the landed phase-valley sign requirement as a
  consistency check against `ACTION_UNIQUENESS_NOTE`.
- **Row E** checks the second-order coefficient against the closed-form
  prediction `b²/(a₀-c₀)`, so the `p=2` row is anchored to perturbation theory
  and not merely to a slope.

## Dependency citations

The runner imports nothing from the repository. The gap statement and the
three admissions are from
[`G_NEWTON_SELF_CONSISTENCY_BOUNDED_SHARPENING_NOTE_2026-05-10_planckP4`](G_NEWTON_SELF_CONSISTENCY_BOUNDED_SHARPENING_NOTE_2026-05-10_planckP4.md).
The universality classes, the tested action forms, and the phase-valley sign
requirement are landed in [`ACTION_UNIQUENESS_NOTE`](ACTION_UNIQUENESS_NOTE.md)
and are cited, not re-derived. The additive coupling, the self-adjointness of
`H`, and A2 are from
[`GRAVITY_FULL_SELF_CONSISTENCY_NOTE`](GRAVITY_FULL_SELF_CONSISTENCY_NOTE.md).
The narrowing of admission (a) is
[`G_NEWTON_SKELETON_SELECTION_BOUNDED_NOTE_2026-05-10_gnewtonG1`](G_NEWTON_SKELETON_SELECTION_BOUNDED_NOTE_2026-05-10_gnewtonG1.md).
Rellich/Kato analyticity of self-adjoint families is standard external
mathematics, used as a proof skeleton and re-earned on finite matrices by the
runner rather than imported as authority.
