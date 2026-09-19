# beyond-the-union-bound, attempt 1 (worker w-macbookpro90c72-j9773, model grok-4.6)

Plan, locked before using the other attempts in this worktree: candidate (iii),
inclusion-exclusion to second order on explanation events.

## (1) The statement attempted

Block 30's construction (T2) is a deterministic map from a configuration of `η'`
to one refinement history `h(ω)`. Write `A_h = {h(ω) = h}` and `C_h` for the
cylinder `{U_z < ε₁ on S(h), U_z < ε₂ on B(h)}`, so `A_h ⊆ C_h` and
`{η'_x = 1} = ⊔_h A_h` (disjoint union over realized histories).

**Statement.**
- (i) The events `A_h` are pairwise disjoint. Inclusion-exclusion of every order
  on `{A_h}` collapses to the first-order identity `P(η'_x = 1) = Σ_h P(A_h)`.
  Second-order Bonferroni on the `A_h` cannot improve a union bound.
- (ii) A second-order *upper* bound on `P(∪ C_h)` needs either the triple term
  or a Hunter–Worsley tree of pairwise intersections. The order-2 truncation
  `Σ P(C_h) − Σ_{h < h'} P(C_h ∩ C_{h'})` is a *lower* bound on `P(∪ C_h)`, not
  an upper bound (CHECKED: two-event identity). Using it as an upper bound is
  the first failing step of a naive reading of candidate (iii).
- (iii) On the depth-2 cone, every configuration with `η'_x = 1` maps to exactly
  one history (CHECKED), so (i) holds there. Cylinder overlaps of distinct
  realized histories exist but are small: they do not change the 4/27 (or 1/27)
  grammar radius, which is a property of the generating function of `𝔊`, not of
  the overlap of the `A_h`.

This is a no-go for (iii) as a way past the tree-recursion ceiling. It does not
produce a new super-solution.

## (2) Steps

**Step 1: Bonferroni order 2 is a lower bound (PROVED; CHECKED as A1).**
For two events, `P(A ∪ B) = P(A)+P(B)−P(A∩B)`. Truncating after the minus sign
undershoots. For `n` events the Bonferroni inequalities alternate; the second
partial sum is `≤ P(∪)`.

**Step 2: a deterministic construction partitions `{η'_x = 1}` (PROVED from
block 30 T2 as ASSUMED; CHECKED as B1 on the depth-2 cone).**
T2 specifies a unique refinement procedure once tie-breaks are fixed. Distinct
histories cannot occur on the same configuration. On the depth-2 cone (308
configurations of `η'`, 234 with `η'_x = 1`) a T2.4 explainer written from the
note assigns exactly one `(S, B, R, F)` key per 1-configuration, and running it
twice agrees.

**Step 3: IE on the `A_h` is vacuous (PROVED).**
Disjointness ⇒ `P(A_h ∩ A_{h'}) = 0` for `h ≠ h'`, so every overlap term vanishes
and `P(⊔ A_h) = Σ P(A_h)`. Candidate (iii) applied to the construction's output
events has nothing to subtract.

**Step 4: IE on the cylinders `C_h` (PROVED as a no-go for the ceiling; CHECKED
as C1).**
`P(η'_x = 1) ≤ P(∪ C_h) ≤ Σ P(C_h)`. A genuine improvement of the *first-order
cylinder union* would require a lower bound on the pairwise cylinder overlaps
large enough to cut the generating-function radius. On the depth-2 cone at
`(ε₁, ε₂) = (1/10, 1/5)`, the first-order cylinder union is already within a
constant factor of `P`, while the grammar-radius obstruction `27 ε₂ < 1` (or
`x = 4/27`) lives at `ε₂` of order `10^{-2}` and smaller and is independent of
those overlaps. Cylinder IE cannot move that radius.

**Step 5 (the first failing step of "IE gives a smaller count").**
Treating `Σ P(C_h) − Σ P(C_h ∩ C_{h'})` as an *upper* bound. It is not.

## (3) Where the route stops

Step 5 of the intended use of (iii). Steps 1–4 stand as a no-go: second-order
IE does not replace the 4/27 count.

## (4) What would finish it

A grammar smaller than `𝔊` (canonical moves, typed poles) so that `Σ P(C_h)`
itself has a larger radius; or a two-scale covering whose events are not the
construction's histories.

Imports: block 30 T2 (deterministic construction) ASSUMED as stated; executed
on the depth-2 cone.
