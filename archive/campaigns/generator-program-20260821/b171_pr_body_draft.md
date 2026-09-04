## Block 171 — The Generator Trilemma Kernel (the trilemma has a solution; the census finds collisions; the null fixture is corrected)

Stacked on Block 170 (the closure audit II). With the OS route closed and quadruple-audited, panel 6 redefined B1 as **the trilemma**: does any weight built from the full quotient `Q` simultaneously satisfy (i) probability well-formedness, (ii) trail/record sensitivity, and (iii) the anti-shim transport standard? It does — and four bounded negatives come with it.

### THE TRILEMMA THEOREM — the winning set is an exact set

Over a **ten-member battery** at the record-slice scope on the bench 12x4, the winning set is **exactly `{W6, W7, W9, W10}`** (same at 8x4) and the deep-memory subset — the weights a record at the *farthest* free level still moves — is **exactly `{W9, W10}`**. Both are asserted as set equalities, not memberships. **The candidate is `W9 = herm(Q^{-1})`**, on full memory depth, on being the Hermitian part of the covariance the committed Gaussian measure actually supplies, and on its twin.

### Leg (i) is a CONGRUENCE THEOREM, not a census

`herm(Q^{-1}) = Q^{-1} herm(Q) Q^{-dagger}` — checker-confirmed **true as printed**, verified on a generic symbolic complex `2x2` and then entry for entry at both extents. So `herm(Q^{-1})` is literally a congruence `X herm(Q) X^dagger`, **Sylvester** carries positive definiteness across it, and **nonsingularity is not an extra hypothesis** because `herm(Q) > 0` forces it. Measured `(24,0,0)` / `(16,0,0)` `(n+,n-,n0)[b165]` for `herm(Q)`, `herm(Q^{-1})` and `Q^dagger herm(Q)^{-1} Q`, with the record-slice blocks `(4,0,0)`. The hypothesis is labelled a **census** in `m` and the moduli, not a theorem in them.

**And the anti-shim separation sits inside one formula.** `W9` moves under both holonomy dials at `T_phys = 6`; its twin `herm(Q)^{-1}` — the same two operations in the other order — is still. The checker's form is stronger and is carried: **`herm(Q)` is matrix-invariant under the full complex holonomy dial**, so the separation is against that entire invariant subalgebra. Disclosed: two of the four leg-(iii) dials leave the positive region; leg (i) survives at all four and the verdict rests on the three that do not.

### S1/S2 — slice-compressed weights are record-blind BY THEOREM

At `s_t = 0` slice `c` is a **direct summand** of `Q` (and with `s_t` free that fails, so it is an `s_t = 0` fact) and `Q[c,c]` carries no free-shear symbol. Hence `f(Q)_cc = f(Q_cc)` for the whole closure, and **every slice-compressed weight is record-blind by theorem** — 7 of 7, with **no normalization leak** because every gram in the battery is itself block-diagonal there. The escape is not a different functional but the **record-slice scope**.

### The K-identities, with the checker's reshaping carried verbatim

**K1** is a theorem for the site class map **and content-free** — it says the diagonal sums to the trace and holds for any matrix, stated honestly rather than billed as work; it **fails** for the sigma-value alphabet by an exact nonzero defect. **K2's order-dependence belongs to the chain-rule construction, not to the weight**: the one-shot Gibbs joint is exactly order-independent (defect exactly zero). The solve's original witness is **quoted then corrected** — both records sat at the read slice, where the two class events are orthogonal projectors, and it mixed wirings; the checker's distinct-time-level chain is the valid demonstration. **K3** holds. Ionescu-Tulcea builds the half-infinite process forward from K1+K3 at a fixed slot order — **no completed future** — and **ergodicity is named openly as the unsupplied residue**.

**The design fork goes to the owner's bar undecided**: chain-rule form (order-dependent for same-slice records, but the forward construction the directive forces) against the one-shot joint (order-free, no per-slot factorization, killed at the value alphabet by K1).

### The pre-census — collisions exist, and the branch is unreachable

At the site alphabet, whose size is `L_x (T_phys - 2)` = 16 and 8 (the solve's `2 L_x (T_phys - 2)` was an **arithmetic error**, disclosed): **16 of 16** distinct weight profiles, **10 of 16** distinct frequency profiles, **6 doubled**. **Collisions exist**, checker-confirmed twice (22 of 32 rows independently rebuilt, zero mismatches). B2's zero-collision branch is **unreachable** at this scope, the frequency map **underdetermines** the weights, and the **Gleason-shaped** refinement census is the remaining theorem-capable instrument.

### LEMMA L2 — the "second null fixture" is REFUTED as stated

Credited to the disjoint checker: carrier `x`-homogeneity buys **`x`-period-2**, not uniformity — the chart lattice is translation by 2. `W5`, `W6` and `W7` are **non-uniform** on both claimed null carriers at record-slice scope (flat, `W6`, 12x4: `123983/487832` against `119933/487832`), and `W6`/`W7` are half the winning set. `W9` itself **is** null on both, which is exactly why its bench must be the disclosed **`x`-inhomogeneous** probe carrier, measured in-region. The shipped `NULL_FIXTURES` table is corrected in this PR — B2 reads it, and the correct null hypothesis there is 2-periodicity, not uniformity.

### Verification and independence disclosure

- Runner: `scripts/admissibility_dirac_kahler_generator_trilemma_kernel_2026_08_21.py` — baseline **8/8 PASS** exit 0 (~63 s against a 150 s budget), `--deep` clean at 70 s (run by the draft worker, not deferred), N5 fence byte-identical, mutation battery **15/15 one-gate clean**. **Disclosed, not smoothed:** at draft time the baseline was **7/8**, gate H failing on the single landing-time condition that the note is not yet at its final path — the case the standing sweep's own docstring names. The twelve gate-A-through-G mutations were verified **exclusive** at draft time (each flips its own gate and no other); the three gate-H mutations only become non-degenerate once the note lands, exactly as Block 170 disclosed for its gate-A pair, and the supervisor re-runs the full sweep after landing. No floats over 614 reported numerals, gated twice: the landed exactness predicate over every numeral, and an **AST scan of the runner's own source** returning zero float literals. No `nsimplify`.
- **Machinery, disclosed and gated where it bites:** dialled inverses use `DomainMatrix` over `QQ_I`, gated entry for entry against the landed LU route **where LU terminates**, and by an exactly vanishing `Q Q^{-1} - 1` residual on the dialled actions — where the landed `sp.inv(method="LU")` **did not terminate** at 8x4 after 7.5 minutes. The checker's **independent route** (real `2N x 2N` embedding over `QQ`) agrees entry for entry there.
- **Worker profile:** Opus solve (50/50 checks, 55.3 s); disjoint maximum-scrutiny Opus checker, which read the solve as text only and rebuilt every 171-specific object by an independent route — **three reshaping corrections** (the K2 premise and its mis-wired witness; K1 disclosed content-free; the machinery gate re-placed) and **two discovered lemmas**, both absorbed and credited (**L1** matrix-invariance of `herm(Q)` under the full complex dial; **L2** the period-2 null control), plus a five-item quantifier-hygiene sweep; Opus draft worker; supervisor review. **Cross-context**, same model family.

### Status discipline

Nothing registered, adopted or proposed. Nine objects are **imposed** by this block — the record-slice scope, the `x`-inhomogeneous probe carrier, `W9`, `W10`, both generator wirings, both class maps and the declared slot order — each measured and never registered; the slot-order fork and any alphabet choice are **measured design inputs for the owner's bar**. Scope is two extents, the site alphabet and the committed action class and no wider — not a continuum statement, not an OS no-go. CYCLE913 carried verbatim (non-supply within this formalism, never metaphysical necessity), with its positive counterpart stated too: **candidacy within this formalism, never a claim about nature**. Zero axiom retirement, zero obligation retirement, no TOE percentage moves, retained-positive end-to-end theory count remains zero. No priority or originality claim is made.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
