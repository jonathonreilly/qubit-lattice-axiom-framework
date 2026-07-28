# A2's Two-Sided-Inverse Proviso Fails on Every Finite Translation-Covariant Lattice, the Repo's Own Periodic Convention Makes It Unsatisfiable, and Covariance Repairs It Without New Input (Bounded Theorem)

**Date:** 2026-07-26
**Type:** bounded_theorem
**Claim type:** bounded_theorem (exact rational linear algebra on explicit
finite matrices; a well-posedness result about a stated proviso, plus a repair
already available in the framework).
**Status authority:** none. Audit: unset. Constitutional effect: none. This
note edits no axiom, foundation, Qualification, primitive, registry, policy,
queue, audit-status, or PR-control surface. **It does not derive A2 and does
not change the status of `gravity_full_self_consistency_note`.**
**Primary runner:**
[`scripts/physical_a2_two_sided_inverse_wellposedness_cycle708_2026_07_26.py`](../scripts/physical_a2_two_sided_inverse_wellposedness_cycle708_2026_07_26.py)
(7 PASS / 0 FAIL, exit 0).

## The proviso

The ledger row for `gravity_full_self_consistency_note` (`criticality:
critical`) records:

> "The scoped implication is mathematically valid **provided the stated
> two-sided inverses exist**: substituting `L^{-1} = G_0 = H^{-1}` and
> inverting gives `L = H`."

The proviso is stated and, so far as the prior-art sweep found, never checked.
This note checks it.

## Answer

**W1 — the kernel.** On the periodic `L^3` torus, `H = -Delta_lat` annihilates
the constants, and its kernel is *exactly* the constants: one dimension, at
`L = 2` and `L = 3` (row Z1, exact null space).

**W2 — the proviso fails.** A singular operator has no two-sided inverse.
`H` has rank 26 of 27 at `L = 3`, and maps the zero vector and the all-ones
vector to the same image. So on **any** finite translation-covariant lattice,
`G_0 = H^{-1}` does not exist and A2's antecedent cannot be satisfied as
written (row Z2).

**W3 — the repo's own periodic convention makes it unsatisfiable, not merely
undefined.** [`BELL_INEQUALITY_DERIVED_NOTE`](BELL_INEQUALITY_DERIVED_NOTE.md)
builds the periodic Poisson Green's function as the *"graph Laplacian
pseudoinverse … excluding the zero mode"*. The runner constructs that
pseudoinverse explicitly and verifies `H·H⁺ = I - J/n` exactly. `H⁺` shares
`H`'s kernel, so it is singular too — and `L^{-1}` is invertible by
definition, its inverse being `L`. A singular `G_0` therefore admits **no**
`L` at all on the full space (row Z3).

So two lanes use different objects for `G_0` on a periodic lattice, and under
the one the repo actually implements, A2 has no solution rather than an
unproven one.

**W4 — what does survive.** Restricted to the zero-mean sector, `H` is
invertible (rank 7 of 7 at `L = 2`), and A2 determines `L` there (row Z4).
The whole of the ambiguity is the single constant mode.

**W5 — covariance repairs it, with no new input.** The landed range-1
covariant classification gives `L = A·I + B·Delta`. Requiring `L = H` on every
*nonzero* mode gives `A + B·D̂(k) = -D̂(k)`. With six distinct nonzero `D̂`
values on the `L = 4` torus this is over-determined, and its unique solution is

```text
A = 0,   B = -1,
```

consistent on all six (row Z5). The constant mode is never used. So the gap
left by W3/W4 closes using covariance — which Admissibility already supplies —
rather than by adding anything to A2.

**W6, W7 — the two repairs that cost something.** A mass term restores
invertibility but shifts the diagonal, so `L != -Delta_lat` and the conclusion
becomes screened rather than Poisson (row Z6). A Dirichlet box restores
invertibility but is **not** translation-invariant: its row sum is 3 at a
corner and 0 at the centre, so it annihilates no constant (row Z7). That
matters because the parent note lists translation invariance as a *consequence*
of `L = H` given A2 — and its CHECK 3 tests the stencil at "interior sites"
only, which is exactly where a box repair hides.

## Claim ledger

Per the inference audit (physics-loop step 11). One row per claim; a
restatement gets its own row.

| ID | Claim | Support | Hypotheses | Shown vs claimed | Falsifier |
|---|---|---|---|---|---|
| W1 | ker(-Delta_lat) on the periodic torus is exactly the constants, dim 1 | row Z1, exact null space at L=2,3 | [satisfied] periodic boundary conditions; finite lattice | shown: dim 1 and the basis vector is constant, at L=2 and L=3; claimed: the same, for these L | a null vector that is not constant, or dim != 1 |
| W2 | on any finite translation-covariant lattice `G_0 = H^{-1}` does not exist, so A2's antecedent cannot be satisfied as written | W1 plus rank deficiency, row Z2 | [satisfied] the lattice is finite and periodic (translation-covariant) | shown: H is singular at L=3, and W1 supplies the constant as a kernel vector at any L, so no two-sided inverse exists there; claimed: the antecedent cannot be satisfied on such lattices — **not** that it fails on infinite Z^3, where the kernel exists but is unbounded (see Scope) | a finite periodic lattice on which -Delta_lat is nonsingular, i.e. carries no constant kernel vector |
| W3 | under the pseudoinverse convention, `L^{-1} = G_0` has no full-space solution | row Z3: H+ built explicitly, `H·H+ = I - J/n` verified exactly, rank(H+) < n | **[supplied]** G_0 is read as the Moore-Penrose pseudoinverse, per the Bell note -- that convention is not repo-wide authority for this lane | shown: H+ is singular, and an invertible `L^{-1}` cannot equal a singular operator; claimed: the same | a nonsingular pseudoinverse, or an L with L^{-1} singular |
| W4 | on the zero-mean sector H is invertible and A2 determines L there | row Z4, exact rank on the sector basis | [satisfied] H preserves the sector (symmetric, kills constants), verified in-row | shown: sector rank is full at L=2; claimed: the same | a zero-mean vector annihilated by H |
| W5 | **thesis** covariance forces A = 0, B = -1 uniquely, using only nonzero modes | row Z5, exact solve on two modes then checked on all six | **[supplied]** L lies in the landed range-1 covariant family (that classification states these operator hypotheses are supplied, not derived); [satisfied] at least two distinct nonzero D-hat | shown: the 2x2 solve gives (0,-1) and it satisfies all six nonzero modes; claimed: the same. **Not** claimed: that covariance derives A2 | a nonzero-mode set admitting a second solution, or the solution failing one mode |
| W6 | the mass repair changes the operator | row Z6 | [satisfied] m^2 != 0 | shown: rank becomes full and the diagonal shifts; claimed: the same | a mass term leaving the diagonal unchanged |
| W7 | the Dirichlet repair breaks translation invariance | row Z7 | [satisfied] open boundary, L >= 3 so an interior site exists | shown: row sums differ between corner and centre; claimed: the box operator is not TI — **not** that the note is wrong to want TI | equal row sums across all sites of a Dirichlet box |

## Scope

- **This does not derive A2.** The gap named in the ledger row —
  `missing_bridge_theorem: supply a retained derivation of L^{-1} = G_0` —
  is untouched. What changes is that the derivation must now also say which
  `G_0` it means and on what space.
- **Infinite `Z^3` is a different case and is not covered by W2.** In `d = 3`
  the lattice Green's function exists as a kernel decaying like `1/(4π|x-y|)`
  (the Maradudin result the lane already cites), because the constant is not
  in `l^2`. What fails there is *boundedness*: `0` sits at the bottom of the
  spectrum, so the inverse is unbounded and the class-A inversion step needs
  domain care rather than being algebraic. W2 is scoped to finite covariant
  lattices, where the failure is outright.
- W1 is verified at `L = 2, 3` and W4 at `L = 2`; the constant is in the
  kernel at every `L` by direct computation, but the runner does not sweep all
  `L`.
- W5 assumes `L` lies in the landed range-1 covariant family. Outside that
  family the constant-mode action of `L` is genuinely unconstrained by A2.
- No claim is made about which repair the framework should adopt, and none is
  adopted here.
- No lane, row, or obligation status is changed, and no N1–N8 verdict is
  awarded.

## Controls

Rows Z6 and Z7 are the controls: each exhibits a repair that *works* for
invertibility and prices what it costs, so W2 is not read as "the lane is
broken". Z3 constructs the pseudoinverse rather than asserting its properties —
an earlier draft set `pinv_annihilates_const = True` with the comment "by
definition", a row that could not fail; it is replaced by an explicit
construction checked against `H·H⁺ = I - J/n`. Z5 solves on two modes and then
verifies the solution against all six, so the uniqueness claim is not read off
the two modes that produced it.

## Dependency citations

The runner imports nothing from the repository. The proviso is quoted from
`docs/audit/data/ledger/gr/gravity_full_self_consistency_note.json`
(`verdict_rationale`). The parent claim, its A1/A2 split, the derived
translation-invariance property, and CHECK 3 are from
[`GRAVITY_FULL_SELF_CONSISTENCY_NOTE`](GRAVITY_FULL_SELF_CONSISTENCY_NOTE.md).
The periodic pseudoinverse convention is from
[`BELL_INEQUALITY_DERIVED_NOTE`](BELL_INEQUALITY_DERIVED_NOTE.md). The range-1
covariant classification is
[`PROPER_CUBIC_FINITE_SUPPORT_LINEAR_KERNEL_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-25`](PROPER_CUBIC_FINITE_SUPPORT_LINEAR_KERNEL_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-25.md).
The infinite-volume Green's-function asymptotic is the Maradudin et al. (1971)
result already cited by the lane, used here only to scope W2.
