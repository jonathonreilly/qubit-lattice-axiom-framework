# Worker report: the `audited_failed` Cl(3) complexification root

Investigation only. No repo file was edited, no commit/push/PR, no audit pipeline run,
no verdict set or predicted. All content read from `origin/main` at
`e6d1070adf5691fa030bef6e008cd9081487e9f1` (fetched at session start).

Node under investigation: `cl3_complexification_split_narrow_theorem_note_2026-05-10`
- shard: `/Users/jonBridger/Toy Physics/.claude/worktrees/quirky-wiles-92e3b4/docs/audit/data/ledger/cl/cl3_complexification_split_narrow_theorem_note_2026-05-10.json`
- note: `/Users/jonBridger/Toy Physics/.claude/worktrees/quirky-wiles-92e3b4/docs/CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md`
- primary runner: `/Users/jonBridger/Toy Physics/.claude/worktrees/quirky-wiles-92e3b4/scripts/cl3_complexification_exclusion_stress_2026_07_13.py`
- helper runner: `/Users/jonBridger/Toy Physics/.claude/worktrees/quirky-wiles-92e3b4/scripts/cl3_pauli_irrep_faithful_direct_sum_n7_independent_2026_07_17.py`
- companion runner: `/Users/jonBridger/Toy Physics/.claude/worktrees/quirky-wiles-92e3b4/scripts/audit_companion_cl3_complexification_split_exact_2026_05_10.py`
- recorded stdout: `/Users/jonBridger/Toy Physics/.claude/worktrees/quirky-wiles-92e3b4/logs/runner-cache/cl3_complexification_exclusion_stress_2026_07_13.txt`

**Hash state (checked, not assumed).** The note and primary-runner hashes on
`origin/main` are byte-identical to those recorded in the shard, so the failing
auditor read exactly the text quoted below and nothing has drifted since:

```
sha256(docs/CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md)
  = 0853bab805b1e879d90c170e7ce51722950df42c18cdc8903af1a07e09868e1e
shard "note_hash" (line 97)
  = 0853bab805b1e879d90c170e7ce51722950df42c18cdc8903af1a07e09868e1e
sha256(scripts/cl3_complexification_exclusion_stress_2026_07_13.py)
  = 2c480ed92e1dd9dcd929cf0650143a6e527160c946b2148e2a9627522ec39221
shard audit_state_snapshot "runner_hash" (line 51)
  = 2c480ed92e1dd9dcd929cf0650143a6e527160c946b2148e2a9627522ec39221
```

---

## 1. Full audit history from the ledger shard

Current row state (`docs/audit/data/ledger/cl/cl3_complexification_split_narrow_theorem_note_2026-05-10.json`):

- line 60 `"audit_status": "audited_failed"`
- line 76 `"criticality": "critical"`
- line 79 `"deps": []`
- line 80 `"direct_in_degree": 29`
- line 81 `"effective_status": "audited_failed"`
- line 87 `"intrinsic_status": "audited_failed"`
- line 88 `"load_bearing_score": 25.288`
- line 93-95 `"negative_assertion_classes": ["derived_no_go_boundary"]`
- line 4649 `"transitive_descendants": 1767`

There are **11 audit rounds** on record: one first-audit stub carried inside a
cross-confirmation block, ten entries in `previous_audits`, and the live row
(which is a duplicate of `previous_audits[9]`). In date order:

### Round 1 — 2026-05-11 — `audited_clean` (gpt-5.5, xhigh)

Recorded only as the `first_audit` half of the round-2 cross-confirmation
(shard `previous_audits[0].cross_confirmation.first_audit`):

> "claim_scope": "Pure algebraic audit of Cl(3,0): omega^2 = -1 and centrality, real-algebra isomorphism Cl(3,0) ~= M_2(C), complexified split into two M_2(C) summands, and two-dimensional complex irreducible readout, with no physical lattice or Hilbert-space bridge claimed."
> "verdict": "audited_clean"

### Round 2 — 2026-05-21 — `audited_clean` (gpt-5.5, xhigh), cross-confirmation `confirmed`

`previous_audits[0]`, verbatim:

> `"verdict_rationale": "The load-bearing content is a standard class-(A) algebraic closure: centrality and square of the pseudoscalar, the real-algebra isomorphism Cl(3,0) ≅ M_2(C), the complexified idempotent split, and the 2-dimensional simple-module readout. The runner source genuinely performs exact symbolic Pauli-matrix and abstract idempotent checks rather than importing external constants or fitted premises. The proof stays within the stated abstract algebra scope and explicitly excludes the open physical per-site Hilbert-space bridge."`

> `"notes_for_re_audit_if_any": "A second auditor should re-check the wording around 'faithful irreducible complex representation of Cl(3,0)' versus non-faithfulness as a representation of the full complexified direct-sum algebra; within the note's real-algebra scope this is not a blocker."`

Runner breakdown `{"A": 38, "B": 0, "C": 0, "D": 0, "total_pass": 38}`.
Later invalidated procedurally: `"invalidation_reason": "no_go_discipline_packet_missing"`, archived 2026-07-11.

**This is where the representation-boundary question first enters the record** —
as an explicit non-blocking flag, not as a defect.

### Round 3 — 2026-07-11 — `audited_clean` (gpt-5.6-sol, xhigh)

`previous_audits[1]`:

> `"verdict_rationale": "The load-bearing content is a genuine class-(A) algebraic closure with no fitted value, physical readout, external comparator, or open dependency. The runner performs exact Pauli-matrix, real-linear-independence, central-idempotent, and commutant checks, and its 38 reported checks agree with the proof. The K4d runner flag is initialized rather than solved computationally, but the accompanying scalar-anticommutation proof independently establishes that subclaim, so this implementation weakness does not break the theorem."`

Its N7 steelman block already names the exact issue and resolves it:

> `"argument": "Because every irreducible representation of the split complexification annihilates one M_2(C) summand, K4 may appear internally inconsistent in calling the resulting two-dimensional representation faithful."`
> `"resolution": "The faithfulness claim is for the original real algebra Cl(3,0) ≅ M_2(C), on which either Pauli chirality is injective. Only the complex-linear extension to Cl(3,0) tensor_R C has a summand kernel, exactly as the source's factor-through wording states."`
> `"resolved": true`

Invalidated `"no_go_discipline_packet_invalid"`, archived 2026-07-12.

### Round 4 — 2026-07-13 06:42 — `audited_conditional` (five-judge judicial panel, 4/5)

`previous_audits[2]`. This is the round that **reclassified the row as carrying a
derived no-go boundary**, which is what put it under the N1-N8 packet regime:

> `"The algebraic classification is correct, but the source explicitly asserts both that every faithful irreducible complex representation has dimension 2 and that no faithful one-dimensional representation exists. Those are in-scope derived exclusion claims, not merely disclaimers about unaudited physical content. The rubric makes negative-assertion classification a semantic judgment independent of the false mechanical source-shape trigger, and an audited-clean verdict with this derived no-go boundary requires a complete passing N1-N8 packet, which the supplied evidence does not provide."`

Judge 3 dissented (`"first", "audited_clean"`), holding the exclusions are
consequences inside a positive theorem, not a no-go.

### Rounds 5-10 — 2026-07-13 07:44 to 11:18 — six consecutive `audited_conditional`

All six are packet/stdout-artifact failures, **never mathematical objections**.
Verbatim, in order:

- `previous_audits[3]` (07:44, batch A, 52 passes):
  > `"N5 nevertheless fails because the live runner output supplies none of the required exact per_element, per_site, per_mode, per_block, and lattice_wide resolution lines."`
- `previous_audits[4]` (07:44, batch B, 52 passes):
  > `"N5 fails procedurally because the supplied live stdout contains no exact per_element, per_site, per_mode, per_block, and lattice_wide resolution lines for each authenticated negative statement"`
- `previous_audits[5]` (09:18, 54 passes):
  > `"Issue: the live N5 resolution sweep covers only two canonical scientific negatives, while the authenticated manifest contains seven N5 phrase-occurrence groups... Why this blocks: the packet explicitly makes any untested rhetoric resolution force a No-Go Discipline FAIL, so a clean verdict cannot be applied even though the exact Cl(3,0) algebra checks themselves pass 54/54."`
- `previous_audits[6]` (10:23, batch A, 54 passes) — shard line 4428:
  > `"N5 nevertheless fails because both exclusion sweeps mark lattice_wide [NOT EXECUTED]"`
- `previous_audits[7]` (10:23, batch B, 54 passes) — shard line 4480:
  > `"The source proof and 54 exact class-A runner checks substantively establish (K1)-(K4), including the faithful-real versus non-faithful-complexification distinction. No-go discipline judgments are N1 FAIL because fewer than five distinct attack-mechanism classes are evidenced..."`
- `previous_audits[8]` (11:18, 62 passes) — shard line 4532:
  > `"The note's algebraic chain is correct on the restricted packet: the primary runner genuinely constructs the Clifford algebra and reports 62 exact algebraic checks with no failures... N7 nevertheless has no independent resolution surface distinct from the runner used for its steelman, so the mandatory clean-verdict gate cannot pass from this packet."`

Note that round 10's complaint (no independent N7 surface) is exactly what the
helper runner `cl3_pauli_irrep_faithful_direct_sum_n7_independent_2026_07_17.py`
was written for four days later.

### Round 11 — 2026-07-21 15:56 — `audited_failed` (codex-audit-batch-B-20260721-5f30bd34, gpt-5.6-sol, xhigh, confidence high)

**This is the flip to `audited_failed`.** Shard line 4626 / line 4650 (live row),
verbatim and complete:

> `"Issue: the K3 idempotence display contains the malformed expression `(1 - 2 i ω + 1)/(2² · )`, although the following equality and runner use the correct denominator 4. Why this blocks: a clean math audit must certify every displayed formula; the negative-assertion judgment otherwise passes N1-N8, with five distinct live routes closing the single faithfulness boundary, no hidden import or prior-witness mismatch, all five resolution classes executed, the faithful-direct-sum steelman resolved by reducibility, and no applicable supplied partial-closure or cross-cycle candidate. Repair target: replace the malformed denominator with `4` and independently rerun the K1-K4 formula audit and 62 exact assertions. Claim boundary until fixed: the abstract split and dimension conclusions remain runner-supported, but the source note is not clean as written."`

Shard line 68 (`chain_closure_explanation`):

> `"The intended theorem is independently supported, but the displayed K3 computation of e_+² contains the undefined denominator `(2² · )`. Consequently, not every quantitative identity in the source closes as written."`

Shard line 99 (`notes_for_re_audit_if_any`) — the repair instruction quoted in the task:

> `"Correct the displayed K3 e_+² denominator to 4, then re-audit the refreshed source and independently recheck the faithful-real/nonfaithful-complex representation boundary."`

Runner breakdown at that round: `{"A": 62, "B": 0, "C": 0, "D": 0, "total_pass": 62}`; `"blocker": null`.

### Answer to "when and on what stated grounds"

It flipped to `audited_failed` on **2026-07-21T15:56:39Z**, in a single round, on
**one stated ground only**: a malformed denominator token in one displayed
intermediate step of the (K3) idempotence computation. The same auditor
explicitly certifies everything else — N1 through N8 all pass, all 62 exact
runner checks pass, and the faithful-direct-sum steelman is resolved. The
verdict rests on the rule that "a clean math audit must certify every displayed
formula", not on any claimed error in the theorem.

One procedural note: the row also carries
`restoration_history[0]` with `"restoration_policy": "restore_overaggressive_invalidation.v2"`,
`"restored_at": "2026-07-22T17:21:20.733053+00:00"` — the failed verdict was
archived by the invalidation sweep on 2026-07-21T15:58 and then restored on
2026-07-22, which is why `previous_audits[9]` and the live row are identical.

---

## 2. The K3 display, and the algebra done independently

### 2a. Locating the display

`docs/CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md:143-150`, verbatim:

```text
e_+ + e_-   = ((1 - i ω) + (1 + i ω))/2 = 1,
e_+ · e_-   = ((1 - i ω)(1 + i ω))/4    = (1 - (i ω)²)/4
            = (1 - i² ω²)/4              = (1 - (-1)(-1))/4 = 0,
e_+²        = ((1 - i ω)/2)²             = (1 - 2 i ω + (i ω)²)/4
            = (1 - 2 i ω + 1)/(2² ·  )    = (2 - 2 i ω)/4 = e_+,
e_-²        = e_-  (analogous).
```

Line 148 as raw text (Python `repr`, to show the exact byte content of the
malformed token — note the *two* spaces between `·` and `)`):

```
'            = (1 - 2 i ω + 1)/(2² ·  )    = (2 - 2 i ω)/4 = e_+,'
```

So the auditor's quotation is accurate. `(2² ·  )` is a dangling product: a
multiplication sign with no right operand. As written it denotes nothing; the
step `(1 - 2iω + 1)/(2² · ) = (2 - 2iω)/4` is not a well-formed equality.

**Provenance.** The token is old. Tracing every commit that touched the file
(`git log --follow`), the malformed line is present unchanged in every version
back to the earliest reachable commit `62a903eb0e` (2026-05-16). It was *not*
introduced by the 2026-07-12 display-repair commit `a87ae28a3f`
("science-fix(cl3): complexification-split displays corrected + K4d computed"),
which repaired the K2 Pauli-product display and the K3 quotient-map display but
left line 148 untouched. It therefore survived two `audited_clean`
cross-confirmed rounds and six `audited_conditional` rounds before being caught.

### 2b. The algebra, done from the idempotent relations

The generic fact first. Let `c` be a central element of an algebra over a field
of characteristic ≠ 2 with `c² = 1`, and set `e = (1 + c)/2`. Then

```
e²  = ((1 + c)/2)·((1 + c)/2)
    = (1 + c)(1 + c) / (2·2)
    = (1 + c + c + c²) / 4
    = (1 + 2c + c²) / 4
    = (1 + 2c + 1) / 4          [using c² = 1]
    = (2 + 2c) / 4
    = (1 + c) / 2
    = e.
```

The denominator at the step where `c²` is replaced by `1` is `2² = 4`, and it is
forced: if the display reads `(1 + 2c + 1)/D`, then requiring `(2 + 2c)/D =
(1 + c)/2` gives `D = 4` uniquely (`D` cannot be cancelled away because
`2 + 2c ≠ 0` in this algebra). I confirmed this symbolically:
`solve(Eq((2 - 2*w)/D, (1 - w)/2), D)` returns `[4]`.

Now specialize to the note's convention. **The relevant element is not `ω`
itself.** In `Cl(3,0)` the pseudoscalar squares to `-1`, not `+1`:

```
ω² = γ_1 γ_2 γ_3 γ_1 γ_2 γ_3
   = γ_1 γ_2 (γ_3 γ_1) γ_2 γ_3        [regroup]
   = γ_1 γ_2 (-γ_1 γ_3) γ_2 γ_3       [γ_3 γ_1 = -γ_1 γ_3]
   = -γ_1 (γ_2 γ_1) γ_3 γ_2 γ_3       [regroup]
   = -γ_1 (-γ_1 γ_2) γ_3 γ_2 γ_3      [γ_2 γ_1 = -γ_1 γ_2]
   = γ_1² γ_2 γ_3 γ_2 γ_3
   = γ_2 (γ_3 γ_2) γ_3                [γ_1² = 1]
   = γ_2 (-γ_2 γ_3) γ_3               [γ_3 γ_2 = -γ_2 γ_3]
   = -γ_2² γ_3²
   = -1.
```

So the involution is `c := -i ω` (for `e_+`), with

```
c² = (-i ω)(-i ω) = (-i)² ω² = (-1)·(-1) = +1.
```

and `e_+ = (1 - i ω)/2 = (1 + c)/2`. Substituting `c = -iω` into the generic
chain above gives exactly the note's line and fixes its denominator:

```
e_+²  = ((1 - i ω)/2)²
      = (1 - i ω)(1 - i ω) / (2·2)
      = (1 - 2 i ω + (i ω)²) / 4
      = (1 - 2 i ω + 1) / 4            [(i ω)² = i² ω² = (-1)(-1) = +1]
      = (2 - 2 i ω) / 4
      = (1 - i ω) / 2
      = e_+.
```

**What the display SHOULD read.** Line 148 should read

```text
            = (1 - 2 i ω + 1)/4          = (2 - 2 i ω)/4 = e_+,
```

(equivalently `/(2²)` or `/(2 · 2)`; all denote 4). The auditor's instruction
"correct the displayed K3 e_+² denominator to 4" is **correct**, and 4 is the
unique correct value.

A sanity control that the `i` is load-bearing (the naive `(1 + ω)/2` would be
*wrong* here): with `ω² = -1`,

```
((1 + ω)/2)² = (1 + 2ω + ω²)/4 = (1 + 2ω - 1)/4 = 2ω/4 = ω/2  ≠  (1 + ω)/2.
```

I verified this by exact computation in the 8-dimensional blade algebra built
from the Clifford relations alone (structure constants derived from
`{γ_i,γ_j} = 2δ_ij`, no Pauli input): `((1+ω)/2)²` returns the coefficient
vector `[0,0,0,0,0,0,0,1/2]`, i.e. `ω/2`. So the task prompt's parenthetical
form `e_+ = (1 + ω)/2` is *not* the right normalization in `Cl(3,0)`; the note's
`e_± = (1 ∓ iω)/2` is. In the same computation `e_+ + e_- = 1`, `e_+ e_- = 0`,
`e_±² = e_±` all return exact `True`, and `ω` commutes with all 8 basis blades.

### 2c. Is it a display defect only?

**Yes — display only. It does not propagate to the runner or the theorem.**

- **Same line, correct value.** The very next equality on line 148,
  `(2 - 2 i ω)/4 = e_+`, is correct, and the *preceding* line 147 already
  carries the correct denominator `4`. So the malformed token sits between two
  correct expressions; nothing downstream in the note consumes it.
- **Runner uses the correct normalization.** In
  `scripts/cl3_complexification_exclusion_stress_2026_07_13.py:239-247`:
  ```python
  e_plus = Rational(1, 2) * (one - I * omega)
  e_minus = Rational(1, 2) * (one + I * omega)
  idempotent_results = [
      vector_equal(e_plus + e_minus, one),
      vector_equal(algebra_product(e_plus, e_minus), zero),
      vector_equal(algebra_product(e_minus, e_plus), zero),
      vector_equal(algebra_product(e_plus, e_plus), e_plus),
  ```
  The `1/2` prefactor is exact `Rational`, and idempotency is *computed*, not
  displayed. There is no `2² · ` anywhere in the runner.
- **I re-ran both runners today** (they perform no file writes; `git status`
  confirms no repo file changed):
  - `scripts/cl3_complexification_exclusion_stress_2026_07_13.py` →
    `TOTAL: PASS=62 FAIL=0`, `FLAGS: none`, matching both the recorded stdout
    `logs/runner-cache/cl3_complexification_exclusion_stress_2026_07_13.txt`
    and the shard's `runner_check_breakdown` of 62.
  - `scripts/cl3_pauli_irrep_faithful_direct_sum_n7_independent_2026_07_17.py` →
    all `N7_INDEPENDENT_CHECK ... status=PASS`.
- **Theorem statement untouched.** (K3) as stated at note lines 28-33 asserts
  `e_± := (1 ∓ i·ω)/2` are complete central orthogonal idempotents. That
  statement is true and independently verified above.

I also re-derived every other display in the note (K1's `ω²` chain at lines
100-106, the centrality chain at 115-118, the K2 real-basis count at 124-135,
the `ω·e_+ = i·e_+` chain at 154, the `e_+ e_- = 0` chain at 145-146, the
`ω = iI ⇒ e_+ = (1+1)/2 · I = I` reduction at 243-245) and found **no second
defect**. The `(2² ·  )` token is the sole malformed display in the note.

---

## 3. The faithful-real / nonfaithful-complex representation boundary

### 3a. The precise question

The ambiguity is in the phrase "complex representation of `Cl(3,0)`". Two
distinct objects are in play:

- **(a)** an `R`-algebra homomorphism `ρ : Cl(3,0) → End_C(V)` — a representation
  of the *real* algebra on a complex vector space;
- **(b)** a `C`-algebra homomorphism `ρ^C : A_C → End_C(V)` where
  `A_C := Cl(3,0) ⊗_R C` — a representation of the *complexification*.

Every `ρ` of type (a) extends uniquely to a `ρ^C` of type (b) by
`ρ^C(a ⊗ z) = z·ρ(a)`, and the two have *different* kernels. The exact question
the repair instruction asks to recheck is: **for which of (a) and (b) is the
word "faithful" being used in K4, and is the resulting statement true?**

Formally, the three propositions to separate are:

- **(P1)** Every irreducible finite-dimensional complex representation of the
  *real* algebra `Cl(3,0)` has `dim_C V = 2`, and is automatically faithful.
- **(P2)** Each such representation, extended to `A_C`, is *non*-faithful, with
  kernel exactly the opposite central summand (`dim_C ker = 4`).
- **(P3)** `A_C` does admit faithful representations, but the smallest is
  `C² ⊕ C² = C⁴` and it is **reducible** — so faithfulness on `A_C` cannot be
  had together with irreducibility.

### 3b. Working it out

**Center and simplicity.** `Z(Cl(3,0)) = R·1 ⊕ R·ω` with `ω² = -1`, so the
center is `R`-isomorphic to `C`. `Cl(3,0)` is *simple as a real algebra*: under
the Pauli isomorphism `Cl(3,0) ≅ M_2(C)` (K2), a two-sided real ideal `J` is
stable under multiplication by the central element `ω ↦ iI`, hence is a complex
subspace, hence a two-sided complex ideal of `M_2(C)`, hence `{0}` or everything.
Consequently **every nonzero algebra homomorphism out of `Cl(3,0)` is injective**.

**(P1).** Let `ρ : Cl(3,0) → End_C(V)` be irreducible, `V` finite-dimensional
over `C`. Since `ω` is central, `ρ(ω)` commutes with `ρ(Cl(3,0))`; `ρ(ω)` is
`C`-linear, so it lies in the commutant, which by Schur's lemma (over `C`,
finite dimension) is `C·id`. Write `ρ(ω) = λ·id`. Then
`λ²·id = ρ(ω²) = ρ(-1) = -id`, so `λ = ±i`. Take `λ = +i` (the other case is the
parity conjugate). Extend to `ρ^C` on `A_C`. With `e_± = (1 ∓ iω)/2`:

```
ρ^C(e_+) = (id - i·ρ(ω))/2 = (id - i·(i·id))/2 = (id + id)/2 = id,
ρ^C(e_-) = (id + i·ρ(ω))/2 = (id + i·(i·id))/2 = (id - id)/2 = 0.
```

So `ρ^C` kills `e_-A_C` and factors through `e_+A_C ≅ M_2(C)`. By
Artin-Wedderburn, `M_2(C)` has a single isomorphism class of irreducible left
module, the natural `C²`. Hence `dim_C V = 2`. Faithfulness of `ρ` on the real
algebra then follows *for free* from real simplicity — it is not an extra
hypothesis.

**(P2).** Continuing: `ker ρ^C ⊇ e_-A_C` (complex dimension 4), and `ρ^C`
restricted to the simple algebra `e_+A_C` is nonzero hence injective, so
`ker ρ^C = e_-A_C` exactly. Symmetrically `ker ρ_-^C = e_+A_C`.

**(P3).** `ρ_+ ⊕ ρ_-` on `C⁴` has `ker = e_-A_C ∩ e_+A_C = {0}`, so it is
faithful on `A_C`; but `P = diag(I₂, 0)` is a nontrivial idempotent commuting
with the whole image, so it is reducible with invariant summands of dimensions
2 and 2.

**No 1-dimensional representation at all.** For `ρ : Cl(3,0) → C`, one needs
`c_i² = 1` and `c_ic_j + c_jc_i = 0 (i≠j)`, i.e. `2c_ic_j = 0` while every
`c_i ≠ 0` — contradiction. The ideal generated by
`{c_i² - 1, 2c_ic_j}` has Gröbner basis `[1]` (unit ideal), so the system is
empty over `C`. Note this holds for *all* one-dimensional representations, not
just faithful ones.

**Exact verification (my own, built from the Clifford relations):**

```
rho_+(omega) = i·I,   rho_-(omega) = -i·I
rho_+ : real rank of Cl(3,0) -> M_2(C) = 8  (dim_R = 8)  -> faithful on real algebra: True
rho_- : real rank of Cl(3,0) -> M_2(C) = 8  (dim_R = 8)  -> faithful on real algebra: True
rho_+^C : complex rank on A_C = 4 (dim_C A_C = 8), kernel dim_C = 4 -> faithful on A_C: False
rho_-^C : complex rank on A_C = 4 (dim_C A_C = 8), kernel dim_C = 4 -> faithful on A_C: False
ker rho_+^C dim = 4 | rank(e_- A_C) = 4 | rank[ker | e_- A_C] = 4 -> ker rho_+^C == e_- A_C : True
rho_+ (+) rho_- on C^4: complex rank on A_C = 8 -> faithful on A_C: True
P = diag(I2,0) commutes with every image: True -> that faithful rep is REDUCIBLE
1-dim complex system solutions: []      Groebner basis: [1]
```

The repo's own helper runner reaches the identical conclusion independently:

> `N7_STEELMAN_RESOLUTION wall=irreducible complexified A-module faithfulness boundary; steelman=rho_plus_direct_sum_rho_minus; individual_kernel_dim_complex=4; combined_complex_rank=8; faithful=true; reducible=true; invariant_summand_dims_complex=2,2; conclusion=faithfulness_does_not_recover_irreducibility`

### 3c. Verdict on the note's treatment

The note's K4 (`docs/CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md:174-184`):

> "Each simple summand `M_2(C)` admits, by Artin-Wedderburn, a unique
> isomorphism class of irreducible left module — the natural action on
> `C²`, of complex dimension `dim_C V = 2`. Hence every faithful
> irreducible finite-dim complex representation of `Cl(3,0)` factors
> through exactly one of the two simple summands `e_±`, and has complex
> dimension `2`. Here `faithful` refers to the representation of the real
> algebra `Cl(3,0)`. The corresponding complex-linear representations of
> the full complexification are individually non-faithful:
> `ker ρ_+^C = e_- · (Cl(3,0) ⊗_R C)` and
> `ker ρ_-^C = e_+ · (Cl(3,0) ⊗_R C)`. Their restrictions to the real
> algebra `Cl(3,0)` are faithful real-algebra maps. ∎"

**Correct, and understated — not incorrect.** Every clause matches what I
derived: the disambiguating sentence ("Here `faithful` refers to the
representation of the real algebra `Cl(3,0)`") is present and does exactly the
work the 2026-05-21 auditor asked for; both kernels are named correctly; the
restriction claim is right.

Two honest understatements, both of which weaken the note rather than overclaim:

1. **"faithful" is redundant.** By real simplicity, *every* nonzero irreducible
   finite-dimensional complex representation of `Cl(3,0)` is faithful and has
   dimension 2. The note proves the stronger statement but states the weaker,
   qualified one. Keeping "faithful" is what creates the parse ambiguity that
   three separate auditors (2026-05-21 `notes_for_re_audit_if_any`, the
   2026-07-11 N7 steelman, the 2026-07-21 "faithful-direct-sum steelman") each
   had to resolve from scratch. Dropping the qualifier, or adding one clause
   noting that faithfulness is automatic, would retire that recurring N7 route
   permanently.
2. **(P3) is not stated in the note prose.** The note says the complexified
   representations are "individually non-faithful" but never states the sharper
   fact that no *irreducible* `A_C`-module is faithful and that the minimal
   faithful `A_C`-module `C⁴` is reducible. That fact lives only in the helper
   runner's `N7_STEELMAN_RESOLUTION` line, which the note does not link.

**Timing check (relevant to whether the boundary is a live defect).** The
clarifying sentence "Here `faithful` refers to the representation of the real
algebra `Cl(3,0)`" was added on 2026-07-13 in commit `b415237bf3`, i.e. it *was*
in the text the 2026-07-21 auditor read. That auditor's own rationale records
the boundary as passing: `"the faithful-direct-sum steelman resolved by
reducibility"`. So the second half of the repair instruction is a
**re-verification request, not an allegation of error**.

---

## 4. Decisive question: is a source-only repair sufficient?

**Recommendation: YES — a minimal, source-only repair is sufficient to make the
node re-auditable. There is no mathematical error in the theorem. Confidence:
high (≈0.9) on the mathematics; moderate (≈0.6) that the very next audit round
returns clean.**

Basis for the high-confidence half:

- The failing auditor's own words scope the defect to a display token and
  explicitly certify everything else: `"the negative-assertion judgment
  otherwise passes N1-N8"`, `"the abstract split and dimension conclusions
  remain runner-supported"`, `"blocker": null`.
- I independently reproduced K1-K4 from the Clifford relations with exact
  arithmetic and found the theorem statements true, the forced denominator to be
  4, and the representation boundary correct as written.
- The defect is provably non-propagating: the runner's normalization is exact
  `Rational(1,2)` and its idempotency check is computed, 62/62 passing on a
  fresh run today.
- The row has `deps: []`, so no upstream repair is needed and no upstream can
  re-break it.

The minimal repair is a **single-line edit** to
`docs/CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md:148`,
replacing `(2² ·  )` with `4`. That alone changes the note hash, which is the
required requeue mechanism (see §5).

Why the second half of my confidence is only moderate — three things the
supervisor should weigh, all procedural rather than mathematical:

1. **The row is under the N1-N8 packet regime** (`negative_assertion_classes:
   ["derived_no_go_boundary"]`, set by the 2026-07-13 judicial panel). Eight of
   the eleven rounds died on packet/stdout completeness, not on content. A
   display fix does nothing about packet completeness; it only removes the one
   *content* objection. The 2026-07-21 round did pass N1-N8, so the packet is in
   good shape *provided the next auditor receives the same evidence*.
2. **The helper runner has no recorded stdout.** The shard's
   `audit_state_snapshot.runner_cache_state` (lines 46-52) records
   `scripts/cl3_pauli_irrep_faithful_direct_sum_n7_independent_2026_07_17.py`
   with `"cache_freshness": "missing"`, `"cache_status": null`,
   `"cache_runner_sha256": null`, and there is no
   `logs/runner-cache/cl3_pauli_irrep_faithful_direct_sum_n7_independent_2026_07_17.txt`
   on `origin/main`. The N7 independent-resolution surface therefore exists only
   as source; round 10 (`previous_audits[8]`) failed on exactly
   `"N7 ... has no independent resolution surface distinct from the runner used
   for its steelman"`. Recording that stdout alongside the display fix is the
   single highest-value add-on. `cache_freshness: "missing"` is an accepted
   enum value (`docs/audit/scripts/compute_audit_queue.py:411-414`), so it is not
   a hard gate — but it is the historically most common way this row has failed.
   Uncertainty flagged: I did not run the pipeline (out of scope), so I cannot
   confirm that adding a cache file leaves the fingerprint untouched.
3. **The note does not link the helper runner.** It is registered only via
   `docs/audit/data/audit_dispatch_queue.json:1389`. Adding it to the note's
   Validation runner list would make the N7 surface visible to a source-reading
   auditor. That is a source edit, not audit data.

**Optional, low-risk hardening I would fold into the same edit** (supervisor's
call — each is a narrowing/clarification, not a strengthening, and none adds
vocabulary):
- one clause in K4 noting that faithfulness on the real algebra is automatic by
  real simplicity (retires the recurring "faithful" ambiguity at its root);
- one sentence recording (P3): no irreducible `A_C`-module is faithful, and the
  minimal faithful `A_C`-module `C²⊕C²` is reducible (moves the N7 resolution
  from runner-only into the source).

**What I would NOT do:** rework the theorem. Nothing in eleven rounds of audit
history, and nothing in my own re-derivation, identifies a mathematical error in
K1-K4. Reworking would be spending capacity to fix a problem that does not exist.

---

## 5. Risk: how much churn does editing this note cause?

I read the guard verbatim at
`docs/ai_methodology/skills/review-loop/SKILL.md:809-820`:

> "**Audit-hash churn guard.** Non-semantic hygiene sweeps on audited source notes
> can be scientifically harmless while still invalidating large parts of the
> audit ledger, because note hashes are source-content hashes. Before landing any
> branch that touches many existing claim-note files for formatting, link-target,
> path, vocabulary, or other non-science cleanup, run the pipeline in validation
> mode and inspect the `seed_audit_ledger.py` / `invalidate_stale_audits.py`
> counts. If the change would reset or requeue already-audited rows solely due to
> non-semantic churn, do not land the broad source sweep. ..."

and the companion gate at `SKILL.md:893-903`:

> "**Stuck-row repair requeue gate.** Terminal non-clean rows
> (`audited_conditional` / `audited_renaming` / `audited_failed` /
> `audited_numerical_match`) re-enter the audit queue only through their own
> note or paired-runner hash drift, an upstream `deps_changed` invalidation, or
> a dispatcher-sidecar re-audit target. Dependent-side edits never reschedule
> the stuck row."

### Measured blast radius

I rebuilt the dependency graph from all 3,857 ledger shards on `origin/main`
(every shard carries a `claim_id`; none was skipped) and took the transitive
closure of `deps`-reversed edges from the target:

| quantity | value |
|---|---|
| total ledger rows | 3,857 |
| direct dependents (in-degree) | 29 |
| **transitive dependents** | **1,731** (1,732 including the node itself) |
| share of ledger | **44.9 %** |
| hop histogram | 1:29, 2:92, 3:202, 4:342, 5:309, 6:299, 7:170, 8:111, 9:62, 10:63, 11:38, 12:10, 13:4 |

That reproduces the task's "~1,732". *Discrepancy flagged:* the shard's own
`"transitive_descendants": 1767` (line 4649) is 36 higher; it was stamped at
audit time on 2026-07-21 and I did not reconcile the difference. It does not
change any conclusion below.

### The number that actually matters

Of those 1,731 downstream rows, the current status distribution is:

| downstream `effective_status` | count |
|---|---|
| `unaudited` | 1,608 |
| `meta` | 119 |
| `audited_conditional` | 3 |
| `audited_renaming` | 1 |

**Only 4 downstream rows currently hold any verdict at all.** 1,727 of 1,731 are
already `unaudited` or `meta`. (844 of them carry non-empty `previous_audits`,
i.e. they were audited once and have already been invalidated by earlier waves —
that cost is sunk, not incurred by this repair.) The four are:

- `ai_methodology.raw.canonical_framing_paragraph` — `audited_renaming`
- `gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_3plus1_full_packet_no_go_theorem_note_2026-04-20` — `audited_conditional`
- `sigma_hier_uniqueness_theorem_note_2026-04-19` — `audited_conditional`
- `universal_qg_canonical_refinement_net_note` — `audited_conditional`

None of them lists the target among its own `deps`; all four sit many hops away.

### Whether the edit propagates at all

I read the invalidation logic rather than assuming it
(`docs/audit/scripts/invalidate_stale_audits.py`, `detect_invalidation`, lines
283-386 and 500-587). The dependent-side triggers are, exhaustively:
`deps_changed` (a dep added/removed), `dep_weakened` (a dep's
`effective_status` **rank drops**), `dep_claim_type_changed`,
`dep_claim_scope_changed`, `axiom_premise_changed` (note-hash drift of an
*axiom-premise* dep only), and `criticality_increased`.

Three facts follow:

1. **There is no generic "upstream note-hash changed" trigger.** Note-hash drift
   invalidates only *the row whose own note changed*
   (`seed_audit_ledger.py:611-613`: `elif prior.get("note_hash") != node["note_hash"]: row = archive_prior_audit(row)`).
2. **The target is not an axiom premise.** `docs/audit/data/axiom_premise_nodes.json`
   lists exactly four canonical ids — `minimal_axioms`,
   `scale_reference_primitive`, `kinetic_isotropy_primitive`,
   `realized_state_primitive` — and the target is not among them. So the
   `axiom_premise_changed` path cannot fire from this edit.
3. **`dep_weakened` cannot fire either, because the status would go UP.** The
   rank table at `invalidate_stale_audits.py:155-169` has
   `"audited_failed": 0` — the lowest rank in the table — and
   `"unaudited": 30`. The target is currently `audited_failed`; after a note
   edit it becomes `unaudited` pending re-audit. `status_rank(after) <
   status_rank(before)` is `30 < 0`, which is false. No weakening.

Additionally, `compute_effective_status.py:177-178` returns
`("unaudited", "awaiting_audit")` for any unaudited row *without consulting its
deps*, so the 1,727 already-unaudited descendants are indifferent to the
target's status either way.

### Verdict on the churn guard

**The guard does not bite here, and the repair is cheap.** Concretely:

- Rows requeued by the edit: **1** (the target itself). That requeue is not a
  cost — it is the *only* permitted mechanism to un-stick a terminal
  `audited_failed` row, per the stuck-row repair requeue gate quoted above.
- Downstream verdicts at risk: **0** by the mechanical triggers I traced; the
  four verdict-holding descendants are not reachable by any dependent-side
  trigger from an upstream note-hash change that *raises* the upstream rank.
- The guard's own trigger condition — "touches **many** existing claim-note files
  for formatting ... cleanup" — is not met: this is one file, one line, and it
  is a *science* correction (a malformed formula), not cosmetic churn.

**Is it worth the audit capacity?** Yes, decisively. The cost is one audit
round on one row. The benefit is that a `critical`-criticality,
`load_bearing_score` 25.288 root with 29 direct citers and 44.9 % of the ledger
downstream stops carrying rank-0 `audited_failed`. Every one of those 1,608
unaudited descendants that later reaches `audited_clean` will have its chain
evaluated by `clean_status` (`compute_effective_status.py:118-124`), which
returns `retained_pending_chain` with `chain_waiting_on:<dep>` for any dep that
is not chain-satisfying. Leaving this root failed means the whole Cl(3) →
staggered-Dirac → per-site-Hilbert cone can never rise above
`retained_pending_chain`, no matter how many descendants get audited. One line
of repair buys back the ceiling on 45 % of the ledger.

**Caveat I am flagging rather than smoothing:** I did *not* run the pipeline in
validation mode (explicitly out of scope for this worker). The counts above are
derived from reading the invalidation/seed/effective-status sources and from a
graph rebuild, not from a `seed_audit_ledger.py` / `invalidate_stale_audits.py`
dry run. The guard's text says to run that dry run before landing. My analysis
predicts it will report 1 requeued row and 0 invalidations, but that prediction
should be confirmed by the actual pipeline before landing.

---

## 6. The three sibling Clifford roots — same kind of defect?

**Short answer: NO. All three currently sit at `audited_conditional` for
packet/live-stdout-evidence reasons, not for a displayed-formula error. Their
defect class is "runner artifact", not "source math typo". One of them
(`clifford_volume_chirality_even_dimension`) previously had a genuine
mathematical defect, which has already been repaired.**

### 6a. `cl3_pauli_irrep_uniqueness_narrow_theorem_note_2026-05-10`

`docs/CL3_PAULI_IRREP_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md`;
`effective_status: audited_conditional` (2026-07-19), `criticality: critical`,
`load_bearing_score: 17.78`, `direct_in_degree: 14`,
`transitive_descendants: 1757`, `deps: []`, 51 class-A passes, 9 prior rounds
(1 clean → 8 conditional).

> `"verdict_rationale": "The class-A derivation supports the stated decomposition, module classification, faithfulness distinction, and conditional unitary refinement, and no mathematical contradiction was found. ... N1 cannot pass from the rendered packet because only faithful-direct-sum-carrier and gram-normalization appear as complete live route records; complex-kernel-solve and central-character-separation are absent, while finite-simple-counterexamples is clipped. This is a runner-evidence defect rather than evidence against the theorem."`

> `"notes_for_re_audit_if_any": "runner_artifact_issue: provide unclipped current-cycle stdout or a cached live certificate containing complete N1 records for complex-kernel-solve, central-character-separation, and finite-simple-counterexamples, then rerun the clean gate."`

Different kind: **clipped/absent live stdout**, explicitly labelled
`runner_artifact_issue`, with "no mathematical contradiction was found" stated
outright. Repair is an evidence-capture fix (record complete stdout), not a
source edit. Note this row shares the same helper runner
(`cl3_pauli_irrep_faithful_direct_sum_n7_independent_2026_07_17.py`) whose
stdout is uncached — the same gap as in §4 item 2, so one cache-capture fix
would serve both rows.

### 6b. `clifford_volume_chirality_even_dimension_narrow_theorem_note_2026-05-10`

`effective_status: audited_conditional` (2026-07-21), `criticality: critical`,
`load_bearing_score: 13.934`, `direct_in_degree: 7`,
`transitive_descendants: 1382`, `deps: []`, 79 class-A passes, 8 prior rounds.

Current verdict — same artifact class as 6a:

> `"verdict_rationale": "The source gives a sound algebraic proof from the Clifford relations, covering the even construction, the odd internal-kernel exclusion, and the d_s=3 parity consequence. ... N1 clean certification nevertheless fails because the rendered current-cycle stdout contains only three complete route records; the first two are absent or truncated, and runner source cannot substitute for live ATTEMPTED-route evidence."`

**But its history is the one genuinely different case, and worth the
supervisor's attention as precedent.** It carried **four consecutive
`audited_failed` rounds** (2026-07-13 ×2, 07-15, 07-17) on a real logical gap:

> `previous_audits[3]`: `"The unrestricted assertion is false because the zero element anticommutes with every generator. Moreover, checking that each basis monomial individually fails does not by itself exclude cancellation in an arbitrary linear combination; neither the proof nor runner establishes the required simultaneous-kernel or coefficientwise-independence argument."`

> `previous_audits[5]`: `"The theorem's odd-n conclusion may be correct, but the presented inference is invalid: a linear constraint kernel can contain combinations even when it contains no individual basis vector."`

That is a *substantive* defect — a monomial-by-monomial scan illegitimately
generalized to arbitrary linear combinations. It was repaired: the current note
now carries a coefficient-level proof at
`docs/CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md:141-175`
("This proves that the simultaneous anticommutator kernel is exactly `{0}`" /
"Here is the same result at coefficient level, making cancellation between ...")
and the runner now "constructs the full simultaneous coefficient matrix"
(note line 299). The row moved `audited_failed → audited_conditional` on
2026-07-21.

**Contrast with the target node:** that row's four failures named a broken
inference and demanded new mathematics; the target node's single failure names a
missing character in a denominator and explicitly certifies the mathematics.
These are opposite ends of the severity scale, and the target is the cheap end.

### 6c. `clifford_chirality_dimension_narrow_theorem_note_2026-05-10`

`effective_status: audited_conditional` (2026-07-21), `criticality: critical`,
`load_bearing_score: 10.51`, `direct_in_degree: 2`,
`transitive_descendants: 728`, **`deps: ["minimal_axioms"]`** (the only sibling
with a dependency), 25 class-A passes, 12 prior rounds.

> `"verdict_rationale": "The Clifford-basis parity proof correctly establishes the volume-element identity, even-dimensional chirality involution, and conditional d_s=3 parity consequence. The note also asserts a substantive odd-dimensional no-go result, while the supplied runner lacks the mandatory five-resolution rhetoric probes and sufficient independently evidenced attack-route coverage for a clean verdict. ... N5 lacks the prescribed resolution lines, N6 exposes no relevant indexed closure candidate, N7 lacks an independent resolution surface naming the boundary ..."`

> `"notes_for_re_audit_if_any": "runner_artifact_issue: add a current-cycle audit block containing five distinct N1 attack-route probes, the five required N5 resolution-class lines for every authenticated negative-phrase group, and an independent N7 resolution surface, then re-run this row."`

Same artifact class. This row has an *additional*, separate churn source: six of
its twelve prior rounds were invalidated by
`axiom_premise_changed:minimal_axioms:<hash>-><hash>`, i.e. it re-queues every
time the `minimal_axioms` note text moves. That is the one place in this group
where the axiom-premise hash trigger is live — and it is a standing tax on this
row independent of any repair.

### 6d. Summary comparison

| row | status | defect class | repair surface |
|---|---|---|---|
| `cl3_complexification_split` | `audited_failed` | **displayed-formula typo** (`(2² ·  )`), math certified | **1 line of the note** |
| `cl3_pauli_irrep_uniqueness` | `audited_conditional` | runner artifact — clipped/absent N1 stdout | evidence capture (stdout) |
| `clifford_volume_chirality_even_dimension` | `audited_conditional` | runner artifact — truncated N1 route records (a *prior* real math gap was already repaired) | evidence capture (stdout) |
| `clifford_chirality_dimension` | `audited_conditional` | runner artifact — missing N1/N5/N7 blocks; plus recurring `minimal_axioms` hash churn | runner audit block + N7 surface |

None of the three siblings is blocked by a source-math error today. The target
node is the only one of the four whose repair is a source edit, and it is the
smallest repair of the four.

---

## Open uncertainties (flagged, not smoothed)

1. I did **not** run the audit pipeline in validation mode. The requeue/churn
   counts in §5 are derived from reading
   `docs/audit/scripts/invalidate_stale_audits.py`,
   `docs/audit/scripts/seed_audit_ledger.py` and
   `docs/audit/scripts/compute_effective_status.py` plus a graph rebuild. They
   are predictions to be confirmed, not measurements of a dry run.
2. The shard's `transitive_descendants: 1767` vs my computed 1,731. Unreconciled.
3. I did not verify whether adding a `logs/runner-cache/` stdout file for the
   helper runner is fingerprint-neutral. `helper_runner_hashes` tracks the
   *script* hash (`invalidate_stale_audits.py:487-499`), which would not change,
   but `runner_cache_state` is part of the v1 snapshot and I did not trace
   whether re-stamping it constitutes drift.
4. Whether the next auditor returns clean depends on packet completeness, which
   is outside anything a source edit controls. Eight of eleven rounds died there.
   I set no verdict and predict none; §4's "moderate" figure is my own
   uncertainty estimate about process, not a status claim.
5. Scratchpad verification script (not a repo artifact, written outside the repo):
   `/private/tmp/claude-502/-Users-jonBridger-Toy-Physics--claude-worktrees-quirky-wiles-92e3b4/66008b76-8d97-42b5-b1e1-4e60c09bb2e9/scratchpad/cl3_indep_verify_20260724.py`
