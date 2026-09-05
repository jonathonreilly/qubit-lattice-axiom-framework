# CHECKER — block 213, the weighted-kernel dispersion (independent refuting checker)

**VERDICT: FIX FIRST.** No blocker. Every load-bearing computation reproduces
exactly under disjoint machinery built from scratch in
`/private/tmp/claude-502/b213check/` (own hand-built bench kernels, own
supercell Fourier reduction, own operator dictionary, own Gröbner census, own
series expansion in `eps`). Two **material** findings: (CK-01) the graded-cone
theorem is false at positive-definite points of Block 211's own compatible
variety that the note's `claim_scope`, headline and `N5` `per_mode` do not
exclude — the restriction to the degree-diagonal representative is load-bearing
and is missing from those three surfaces; (CK-02) one displayed exact value in
`N4b` is wrong by a factor of five. Seven minor findings. **The locus theorem
survives in full, and the sign of the det-B lemma survives at the runner's own
corner ordering** (but see CK-03: the sign is not order-independent).

## Framework refresher (read in full before any of the below)

`docs/MINIMAL_AXIOMS_2026-06-29.md` complete (233 lines: Lattice / Qubit /
Admissibility / Record; the Qualification, Audit-Pipeline, Dynamics,
Observable-Principle-parent, 2026-06-05, Open-Gates and Historical sections);
`docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` complete (six rules,
three approved primitives: `scale_reference_primitive`,
`kinetic_isotropy_primitive`, `realized_state_primitive`);
`docs/audit/data/axiom_premise_nodes.json` complete (four canonical ids).
**No axiom or registered primitive is used as content by this block, and none is
needed for anything it claims.** The block introduces no primitive and asks for
no registration; `registered: 0`, `adopted: 0`, `axiom_movement: none` are
correct as written.

## What I rebuilt independently (disjoint machinery, never importing the primary runner)

- The `η`-staggered lane kernel written out by hand as a site-indexed matrix on
  `(4,4)`, `(4,2,2)` and `(4,4,4)`: **equals** `b201.lane_kernel` entry for
  entry (64 nnz, antisymmetric); the graded raising part equals
  `b201.raising_part` on `(8,4)`; `K = d − dᵀ` and `d² = 0` on all three
  benches; the 3D links match Block 209's `omega`-conjugated generators at all
  48 links, 0 bad, 32 nnz on `(4,2,2)`.
- A **second, disjoint** route: my own period-2 operator dictionary, verified to
  reproduce the hand-built bench matrices exactly on all three benches.
- The period-2 reduction rebuilt as an honest **supercell Fourier transform** of
  the direct `64 × 64` bench matrix on `(4,4,4)` at the `W1` cell: every coarse
  momentum's `8 × 8` block equals `Z (H_B d_B − d_Bᵀ H_B) Z⁻¹`, and the product
  of the eight block charpolys equals the direct `64 × 64` charpoly.
- The principal part taken by **explicit series in `eps`** at
  `z = exp(i eps kappa)` (not by a hand-written first-order formula).
- Block 211's cell form rebuilt from its landed degree-block formulas and
  checked against `b211.face_system` + `b211.solve_pinned` at all four chart
  representatives and at `W1, W2, W3, honest_face, L+−, L−+`.

## FINDINGS

### CK-01 — MATERIAL. The graded-cone theorem needs the degree-diagonal representative, and `claim_scope`, the headline and the `N5` `per_mode` fence do not say so — with a positive-definite counterexample on Block 211's own variety.

**Attacked sentence** (`N5` `per_mode`, byte-identical in the note and the
runner's `N5_FENCE`):

> "both assemblies preserve grade parity, `M = [[0, B], [B^T, 0]]` with
> `B = H_e D_eo + D_oe^T H_o`, the characteristic cone `{det B = 0}` is
> reading-independent"

and the `RESULT` line / one-sentence summary / title: "ITS CHARACTERISTIC CONE
IS, UNDER THE GRADED ASSEMBLY, THE UNION OF THE TWO HODGE READINGS' CONES ...
AND NOWHERE ELSE OFF FLAT", and `claim_scope`: "completed by Block 211's
per-offset-isotropic cell form under Block 105's two landed assemblies".

**Independent evidence.** Block 211's landed result is that solvability at every
compatible moduli point leaves **exactly four free duality parameters**
`D07, D16, D25, D34`, absent from every degree block, with an *open bounded
four-dimensional* PD region (`D07² < v0/v1`, `D16², D25², D34² < v1/v0`). All
four are **grade-parity crossing** entries: `(0,7)` couples grade 0 to grade 3,
and `(1,6)`, `(2,5)`, `(3,4)` each couple grade 1 to grade 2. Taking `W1`
(`v0 = 15/16, g0 = 1/4, v1 = 1, g1 = 1/4`, all-plus) and switching on one
parameter at `1/4` — inside Block 211's own bound `16/15` — I verified by
substitution into all 96 of `b211.face_system`'s equations that the cell is
still **on the six-face-compatible variety**, and by leading minors that it is
still **positive definite**; then measured `H0` and `M = H0 D + Dᵀ H0` from my
own series expansion:

| duality parameter on | on Block 211 variety | PD | `H0` preserves grade parity | `det M` factors (total degree, multiplicity) | cone = union of the two Hodge cones |
| --- | :---: | :---: | :---: | --- | :---: |
| none (degree-diagonal) | yes | yes | **yes** | `(2,2), (2,2)` | **yes** |
| `D07 = 1/4` | yes | yes | no | `(2,2), (2,2)` | yes |
| `D16 = 1/4` | yes | yes | no | **`(4,2)`** | **no** |
| `D25 = 1/4` | yes | yes | no | **`(4,2)`** | **no** |
| `D34 = 1/4` | yes | yes | no | **`(4,2)`** | **no** |

At `D16 = 1/4` the cone is a single **irreducible quartic**
`96kt⁴ − 112kt³kx + 16kt³ky + 224kt²kx² − 112kt²kxky + 154kt²ky² − 112ktkx³ + 80ktkx²ky − 109ktkxky² + 16ktky³ + 96kx⁴ − 112kx³ky + 218kx²ky² − 112kxky³ + 96ky⁴`
(squared), which is neither one Hodge reading's cone nor the union of the two.
So the note's four-way dichotomy — union off the locus, one quadric on it,
non-Hodge pair under overlap — **does not exhaust Block 211's compatible
positive-definite variety**; it exhausts the measure-zero degree-diagonal slice
of it. The `N5` `per_block` fence *is* correctly scoped ("Graded assembly, **any
block-diagonal cell form**"), and `INSTANCE_SCOPE[1]` and the
narrowest-true-statement *do* say "at the degree-diagonal representative". The
defect is that the three surfaces that a consumer reads first — `claim_scope`,
the one-sentence summary/title, and the `per_mode` parity sentence — do not.

**Narrowest fix.** (i) Append "at its degree-diagonal representative
(`D07 = D16 = D25 = D34 = 0`)" to `claim_scope` after "per-offset-isotropic cell
form"; (ii) add the same five words to the one-sentence summary and to the
`per_mode` grade-parity clause (the `N5` fence is byte-gated at `I-1`, so the
runner's `N5_FENCE` constant must change with it); (iii) add one line to `N6
REOPEN`: switching on any of `D16, D25, D34` breaks grade parity and replaces
the cone by an irreducible quartic, with the PD witness `W1 + D16 = 1/4`. No
number in the note changes.

### CK-02 — MATERIAL. The displayed transverse-split value at `honest_face` is wrong by a factor of five.

**Attacked sentence** (`N4`, line 332-334):

> "**splits** at exactly one — `honest_face` ... — into `5 (kt² + kx² + ky²)`
> and `(25/13)(5kt² − 8kt kx − 8kt ky + 5kx² + 8kx ky + 5ky²)`."

**Independent evidence.** My own computation of the four graded H-pencil
branches at `honest_face` gives
`5(kt²+kx²+ky²)`, `(5/9)Q`, `(5/13)Q`, `(9/25)(kt²+kx²+ky²)` with
`Q = 5kt² − 8ktkx − 8ktky + 5kx² + 8kxky + 5ky²`; the middle two are `kᵀG1k` and
`kᵀG2k`, so the transverse pair is `{5(kt²+kx²+ky²), (5/13)Q}`. The runner's own
receipt agrees (`logs/runner-cache/...txt` line 268:
`25*kt**2/13 - 40*kt*kx/13 - ... = (5/13) Q`). The note printed `(25/13) Q`,
five times the measured value. `RESULTS_block213.md` defect 7 states it
**correctly** as "`(25/13) kᵀ M1 k`" — and `kᵀ M1 k = Q/5` at
`g0 = 4/5`, so `(25/13) kᵀ M1 k = (5/13) Q`. The error is the substitution of
the expanded `Q` for `kᵀ M1 k` without dividing by five. No gate catches it:
`TRANSVERSE_SPLIT_RATIONAL_WITNESSES` records the witness **name** only.

**Narrowest fix.** `(25/13)` → `(5/13)` in that sentence (or write it as
`(25/13) kᵀ M1 k`).

### CK-03 — minor. "THE SIGN IS `+D3`" is a statement about the corner ordering, not about the object.

**Attacked sentence** (`N2`): "**The sign is `+D3`**: the first draft declared
`−D3`, and its gate would have failed had its baseline ever finished."
Also claim register 19, the narrowest-true-statement, and `N5` `per_block`.

**Independent evidence.** I reproduced `det B = +D3 (kᵀD1k)(kᵀ E adj(D2) E k)`
exactly at 17 symbols under the runner's ordering (even
`[(0,0,0),(0,1,1),(1,0,1),(1,1,0)]`, odd `[(0,0,1),(0,1,0),(1,0,0),(1,1,1)]`, both
in Block 209's `CORNERS` order). `B` maps the odd sector to the even sector, so
`det B` has a sign only relative to a chosen ordering of each: I re-ran the same
computation with one transposition of the even basis and got
`det B = −D3 (kᵀD1k)(kᵀ E adj(D2) E k)` for the identical object. The invariant
statements are `det(B Bᵀ) = (det B)²` and the cone `{det B = 0}` — both of which
the note also makes.

**Narrowest fix.** In `N2`, after "The sign is `+D3`", add "in the even/odd
corner order `[(0,0,0),(0,1,1),(1,0,1),(1,1,0)] | [(0,0,1),(0,1,0),(1,0,0),(1,1,1)]`;
the cone, not the sign, is order-independent."

### CK-04 — minor. `S0`/`S1` are stated without the index order that decides which cells are rule A.

`N4b` writes "With `M1 = I − g0 S0`, `M2 = I − g1 S1` the signed triangles" and
then `S1 = −E S0 E`, without saying that `S0, S1` are read in the `(t, x, y)`
direction order — which for degree 1 is the **reverse** of Block 209's own
`DEGREE_INDICES[1] = (1, 2, 4) = (y, x, t)`, the order in which Block 211's
landed block formula `M1 = [[1, −c_xy0, −c_ty0], [−c_xy0, 1, −c_tx0], [−c_ty0,
−c_tx0, 1]]` is stated. I hit this directly: reading `S0` in Block 211's own
order makes `flipped(("xy",0),("xy",1))` — Block 211's class-`(−1,−1)`
representative, and `W2`/`W3`'s sign cell — a **rule-B** cell, which would
contradict the chart result `{t(u²+1), u(u²+1)}`. In the correct `(t, x, y)`
order all four representatives are flat-only, the chart and the census agree,
and I verified the runner's convention against `b211.solve_pinned` at all four
chart representatives and at `W1, W2, W3, honest_face, L+−, L−+`. The runner is
self-consistent; the note is under-specified.

**Narrowest fix.** One clause in `N4b`: "`S0` and `S1` read in the `(t, x, y)`
direction order, i.e. `S0 = [[0, s_tx0, s_ty0], [s_tx0, 0, s_xy0], [s_ty0,
s_xy0, 0]]`" — after which `S1 = −E S0 E` reads `s_tx1 = s_tx0`,
`s_ty1 = −s_ty0`, `s_xy1 = s_xy0`.

### CK-05 — minor. `E d E ≠ d` is true but is not the operative reason the four representatives cannot decide the coincidence question.

I verified `E d E ≠ d` for three independent nontrivial corner-sign gauges (only
`E = ±I` can fix `d`, since adjacent corners must carry equal signs). But the
coincidence test `G1 ∝ G2` contains no kernel at all. Under `D → E D E` the two
readings transform as `G1 → Σ1 G1 Σ1` and `G2 → Σ2 G2 Σ2` with
`Σ1 = diag(ε_{e_μ})` on the unit corners and `Σ2 = diag(ε_{1−e_μ})` on the
complementary corners; the proportionality question is invariant only when
`Σ1 = ±Σ2`, which is why representatives are points. `E d E ≠ d` is the reason
the **cone** moves. Both are true; the note gives only the second as the reason
for the first.

### CK-06 — minor. Rule B's "no positive point" is a statement on the family's magnitude domain.

`LOCUS_RULE_B` (declared literal, quoted in `F-7`'s statement and in `N4b`)
reads "`g0 = -g1/(1 - pi0 g1) < 0`: no positive point". As a blanket inequality
this is false: at `π0 = +1` and `g1 > 1` the same curve gives
`g0 = g1/(g1 − 1) > 0`. It is true on the family, where the tie `g1² = 1 − v0v1`
with `v0, v1 > 0` forces `|g1| < 1`. Fix: append "on the family's magnitude
domain `|g1| < 1`".

### CK-07 — minor. `N4g` over-claims the seventeen-symbol scope of the principal-part lemma.

> "**The principal-part lemma is symbolic in seventeen variables and
> fraction-free** — every identity is a polynomial identity, so there is nothing
> left to sample."

The transverse-product half is not taken at 17 symbols. `N2` scopes it correctly
("the product taken on the symbolic Block 211 family") and
`RESULTS_block213.md`'s could-not list says so explicitly ("not expanded as a
seventeen-symbol polynomial identity (cost)"). The `N4g` sentence does not carry
the exception. Fix: "…in seventeen variables and fraction-free, the transverse
product excepted (taken on the symbolic four-parameter family)".

### CK-08 — minor. The `Imports` bullet says Block 107's completion is "used unchanged" while substituting a different operator.

> "its completion pattern `Q = m H + H d − dᵀ H` (Block 107's, used unchanged)"

Block 107/201's completion is `Q = m H + H D_s − D_sᵀ H` with `D_s = A_s − Ps A_s Ps`
the **seam glue** (`scripts/admissibility_dirac_kahler_covariant_rule_identification_2026_08_26.py`
lines 360, 892), not the graded raising part `d_K`. The substitution (and the
periodic-for-seam change) is declared in the `N5` `per_element` fence, in
`IMPOSED_OBJECTS[0]` and in the modelling-choices paragraph; only this bullet
reads as if the operator were the same. Fix: "…the completion **pattern**
`Q = m H + H X − Xᵀ H` (Block 107's, with `X = d` here in place of Block 201's
seam glue `D_s`)".

### CK-09 — minor. The `F-8` locus measurement is not fail-closed with a family attribution.

`measure_principal` builds the locus branch constants with
`locus_constants.append(tuple(sorted(constants)))`. If a defect makes a
branch/cone ratio `k`-dependent, `sorted` raises
`TypeError: cannot determine truth value of Relational` inside `measure()` —
before any gate is evaluated. Observed on two of my three mutation probes (see
table). The runner's top-level handler does print `[FAIL] INTERNAL-EXCEPTION`
and `TOTAL: PASS=0 FAIL=1` and exits nonzero, so nothing is silently passed and
no certified baseline can hide such a defect; but the headline gate for the
locus theorem cannot report a `FAIL` for the perturbation it exists to detect.
Fix: test `k`-freeness of each ratio first and set the flag `False` rather than
sorting.

### CK-10 — minor (pack hygiene). `CLAIM_STATUS_CERTIFICATE.md` contradicts the landed note's front matter.

The pack file still carries `actual_current_surface_status: open` and
`claim_type_reason: pending (…)` against the note's `conditional-support` and
its full `claim_type_reason`. It is marked "to be completed at block close"; it
was not. All other machine-status fields in the note use values in current use
across `.claude/science/physics-loops/` (`trace_class: upstream_support`,
`reachability_to_target: supports`, `artifact_role: theorem`,
`actual_current_surface_status: conditional-support`), and the note's
`target_blocker_text` matches `TRACE_GATE.md` and the `GOAL` verbatim.

## Mutation-probe table

Copies of the runner in `/private/tmp/claude-502/b213check/mut/`, `ROOT`
repointed at the worktree and nothing else changed (the git authority pins all
resolve; gate `A` passed in every run, so every gate was exercisable).

| # | planted defect | caught? | how | exit |
| --- | --- | :---: | --- | :---: |
| M1 | `eta()` returns `−(−1)^Σ` for direction 2 only — the `η_y` staggering phase sign-flipped in the y direction alone | **yes** | not by a family: `TypeError` inside `measure()` (the `F-8` `sorted(constants)` of CK-09); prints `[FAIL] INTERNAL-EXCEPTION`, `TOTAL: PASS=0 FAIL=1` | 1 |
| M2 | det-B lemma comparison put back to `−D3`: `sp.expand(objects["detB"] + D3*q1*q2_adj) == 0` | **yes, cleanly** | `GATES … F=FAIL …`, `[FAIL] F-1` (`det B = +D3 … (False)`), all other families PASS, `TOTAL: PASS=35 FAIL=1` | 1 |
| M3 | `L+−` moved off the coincidence curve but kept **on the family and PD**: `(v0, g0, v1, g1) = (3√5/8, 1/4, 2√5/5, 1/2)` | **yes** | not by a family: same `TypeError` (the branch/cone ratios stop being `k`-free exactly because the point is off the locus); `TOTAL: PASS=0 FAIL=1` | 1 |

Two of three planted defects are detected only as a crash. Both crash *before*
the gates run, so neither could ever be certified — but the family attribution
is lost, which is CK-09.

## Attacks that FAILED (the block survived these)

1. **The det-B lemma, sign included.** `det B = +D3 (kᵀD1k)(kᵀ E adj(D2) E k)`
   and `D0` absent, reproduced exactly at 17 symbols by my own series expansion
   and my own Berkowitz determinant. 2D: `det B = −D2 (kᵀD1k)`, reproduced.
2. **The expansion, measured not assumed.** Zeroth order `K_H,B(1) = 0`; the
   first-order coefficient equals `H0 D + Dᵀ H0`; `M` symmetric; `H0`
   grade-parity preserving; `M_ee = M_oo = 0`; `M_eo = H_e D_eo + D_oeᵀ H_o` —
   all four under **both** assemblies at the fully symbolic block-diagonal cell
   form. `det(B Bᵀ) = (det B)²`, so the cone is reading-independent.
3. **The Bloch reduction itself.** Verified against an honest supercell Fourier
   transform of the direct `64 × 64` bench matrix on `(4,4,4)`, block by block
   and by the product of charpolys.
4. **The 64-cell census.** My own Gröbner run: `(g0, g1)` in **48** cells;
   `(g0g1+g0−g1)` 4 cells class `(1,−1)`; `(g0g1−g0+g1)` 4 cells class `(−1,1)`;
   `(g0g1−g0−g1)` 4 cells class `(1,1)`; `(g0g1+g0+g1)` 4 cells class `(−1,−1)`.
   Rule-A 8, rule-B 8, union = the 16 curve cells, closed forms for
   `P = M1 E M2 E` verified in every one, `S² = 2I + πS` verified in every one,
   both curves degree one in `g0` with the root verified by substitution.
   `48 + 16 = 64`.
5. **The chart.** `{t(u²+1), u(u²+1)}` in all four classes, real zero `(0,0)`
   only — and all four class representatives are flat-only cells in my census,
   so chart and census agree on the 16 cells the four charts cover.
6. **Missed locus points: none found.** The Gröbner ideal in each of the 16
   curve cells is **principal**, so the proportionality variety has no extra
   component; in the other 48 it is the reduced point `(g0, g1)`. The census is
   computed from the minors of `(G1, G2)` directly, not from the closed form, so
   a point with `G1 ∝ G2` but `P` not of the displayed form would still appear —
   none does. `G1 ∝ G2 ⟺ M1 E M2 E ∝ I` re-derived by hand from
   `G1 = (v1/v0) M1`, `G2 = (v0/v1) E M2⁻¹ E`.
7. **"Never scalar", including at the boundary of positivity.**
   `μ − 1 = π0 g1³(2 + π0 g1)/((1−π0g1)(1+π0g1)³)` re-derived by hand and
   symbolically; its only roots are `g1 = 0` (flat) and `π0 g1 = −2`, off the
   family (`|g1| < 1` is forced by `g1² = 1 − v0v1`). At the PD boundary of the
   `π0 = +1` branch `μ → ∞`; of the `π0 = −1` branch `μ → 0`. Never `1` off flat.
   The second reason survives too: `1/(1 − g1²) = 1` only at `g1 = 0`.
8. **PD-solvability along the whole curve, and it is Block 211's notion.**
   `π0 = +1`: `g0 = g1/(1+g1) < 1/2 ⟺ g1 < 1` and `π1 = −1` allows any `g1 < 1`.
   `π0 = −1`: `g0 = g1/(1−g1) < 1 ⟺ g1 < 1/2` and `π1 = +1` requires `g1 < 1/2`.
   Both are exactly Block 211's PD-solvability criterion; the two witnesses are
   PD outright at the degree-diagonal representative, which is strictly stronger.
9. **The two `QQ(√6)` witnesses.** Both on the family (both ties exact), both in
   rule-A cells, both on the curve, both PD; `G2 = μ G1` exactly with
   `μ = 32/27` and `27/32`; graded `det B` one quadric squared; branch constants
   `(1, 32/27, 4/3, 4/3)` and `(1, 27/32, 9/8, 9/8)` with no leftover factor
   (the transverse pair splits); overlap cone a pair proportional to neither
   reading. Re-derived the volumes by hand: `v0² = 2/3`, `v1² = 27/32` and
   `32/27`.
10. **The overlap cone and its sign.** `det B = +Q+ Q−` exactly at symbolic
    couplings (`−Q+Q−` refuted); the folded `H0 = h0 I + 2h_f` with the declared
    `h0` and `h_f` verified entry by entry on the symbolic family.
11. **Hunting an overlap cone that IS a Hodge cone: none exists.** I extended
    the note's "at every point measured" to **all 64 sign cells at symbolic
    `(v0, v1, g0, g1)`**: zero cells in which an overlap cone factor is
    identically `kᵀG1k` or `kᵀG2k`. The note's claim is weaker than the truth.
12. **The `N4` witness table**, reproduced value for value: the graded cone
    factors and overlap cone factors at `W1, W2, W3, mixed, near_boundary,
    honest_face, boundary` (including `mixed`'s six-digit overlap coefficients
    and `boundary`'s `(kt−kx+ky)²` at Hessian rank 0 with the rank-2 companion);
    the transverse pair splits at `honest_face` and only there among the six
    curved rational witnesses.
13. **The 2D formulas.** Graded branches `(kt²−2c kt kx+kx²)/(1−c²)` and
    `/v²` with `g = [[1,c],[c,1]] = (D1/D0)⁻¹`; not scalar generically; scalar
    exactly on `v² = 1−c²`; overlap pencil scalar; `c_K = 2cv²/(3v²+1−c²(v²+1))`
    and `c_K − c = −c(1−c²)(v²+1)/(3v²+1−c²(v²+1))`, nonzero for `c ≠ 0`. The
    displayed exact `0-form`/`2-form`/`W1-overlap` symbols match the receipt.
14. **Shear/volume registration, sharper than claimed.** From the lemma,
    `det B = q(M1) · q(E adj(M2) E) / v0²` exactly: `v1` is **absent** from
    `det B` and `v0` enters only as an overall scale. Verified symbolically
    (`det B / det B|_{v=1} = v0⁻²`). The shears move both cones; the sign class
    moves the overlap cone.
15. **"Dead end five" strengthened.** Brute force over `g1 = p/q`,
    `gcd(p,q)=1`, `p, q ≤ 200` (the note claims height 120) on both positive
    rule-A curves: **no** point with both tied volumes rational.
16. **Authority and provenance.** All five pins verify live:
    `origin/main = e249016f…`, axiom blob `bc23300b…` on `origin/main` and in
    the worktree, registry blob `b93959cc…` on `origin/main` vs `f01d3be8…` in
    the worktree (the inherited Block 212 divergence, disclosed), parent
    `4e9931a9…` resolving `PARENT_REF` with both Block 212 blobs
    (`58e98794…`, `eddb3f69…`) identical at the parent and in the worktree, and
    the stale pin `7a98db1d…` a real ancestor of `HEAD` carrying neither. The
    receipt's `runner_sha256 07ee1235…` equals `shasum -a 256` of the committed
    runner. Baseline re-run by me: `PASS=36 FAIL=0`, exit 0, all nine gates PASS.
17. **Quote fidelity.** The `R5` block quote matches `GOAL.md` lines 11-14
    verbatim (and the note says so — "in its own words as quoted by this block's
    GOAL"). Block 201's rule `A = sx, B = −sz` (note line 48), `FORK_SHEAR = 5/13`,
    `FORK_MASS = 9/20` all check. Block 211's degree-block formulas
    (`deg-1 = v1 M1` on corners `(1,2,4)`, `deg-2 = (1/v0) M2` on `(3,5,6)`), its
    ties, its PD criterion and its witnesses match the note's `W1` section
    verbatim. The scout-grade fence is verbatim against **Block 211's title**
    (its one-sentence body variant reads "about … and not a gravity"; nothing
    turns on this, and Block 213 carries "NO GRAVITY IS SUPPLIED" separately).
    Residual quotes for Blocks 201/211/212 in the `N4` citation table all match
    their sources. **PR #7970** verified read-only: its title, `κ(m,U) = 0`
    identically, the `6³/8³/12³` sizes, "the generated mass does respond to the
    diagonal metric", and its own boundary "nothing derived from the axioms" —
    the note quotes it at exactly its own conditional scope and does not
    contradict it.
18. **No unlanded note is linked in a way that misstates its status.** The three
    links (Blocks 201, 211, 212) resolve in the worktree and in `HEAD` and not on
    `origin/main`; `N7` discloses precisely this and gate `A-2` binds it.
19. **`N1`–`N8` carry no hidden necessity claim.** The only occurrence of the
    word is "Each is non-supply within this formalism, never necessity"; the
    cycle-913 caution is carried verbatim in `N0` and in the `N5` `RESULT` line.
20. **Nothing landed is touched by correction 113.** Block 211 makes no claim
    about `G1 ∝ G2`; the two readings `G1 = D1/D0` and `G2 = D3 E D2⁻¹ E` are
    Block 213's own declared candidates built on Block 209's honest-lift pattern.
    Block 212 is a stack parent only. The predecessor draft was never landed.
21. **No "cone" → "metric" slide of substance.** `CONE` and `METRIC` are both
    fenced in `N0` and `N4g`, and "one metric's cone" always resolves to "one of
    the two declared rational readings". The one place with a bare definite
    article is `N3`'s "the cone **is** the cell metric's cone" in two directions,
    where only one reading exists; harmless, but a "`G1 = D1/D0`" would remove it.
22. **The F2 leak is not material to anything I checked.** I did not open
    `F2_blind_metric_prediction.md` and cannot verify its contents by
    construction. It does not matter for this check: I re-derived `N4b`'s
    coincidence theorem, the det-B lemma, the 2D formulas and the locus
    witnesses end to end with disjoint machinery, so their correctness does not
    depend on the seal; route `F2` (Schur/metric identification of the principal
    part) is a **selection** route that the note explicitly does not execute and
    whose conclusion no line of the note asserts; and a leaked prediction could
    not manufacture a non-selection claim (`H-3`). The supervisor's comparison
    stands unaffected.

## Verdict

**FIX FIRST** — CK-01 (three surfaces to qualify, no number changes) and CK-02
(one coefficient, `25/13 → 5/13`). Everything else is minor. **The locus theorem
survives every attack I could mount**, including a from-scratch census, a
from-scratch closed form, the boundary of positivity, and a search for missed
components; **the sign of the det-B lemma survives** at the runner's declared
corner ordering, with the caveat of CK-03 that the sign is ordering-relative
while the cone is not.

*Checker machinery: `/private/tmp/claude-502/b213check/` (`ck_core.py`,
`ck_a1_bloch.py`, `ck_b_principal.py`, `ck_c_census.py`, `ck_c2_chart_conflict.py`,
`ck_d_locus_overlap.py`, `ck_e_witnesses.py`, `mut/m1..m3.py`). Block 201, 211
and 105 runners imported read-only for comparison only; the primary runner never
imported. Two bugs in my own first-pass machinery (a mis-extracted `B` block and
a wrong degree-1 index order) were found and fixed by disagreement with the
primary and are recorded here as such — in both cases the primary was right.*
