lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-16T07:56Z

# gap-compact-rigidity-max: the compactness-and-rigidity architecture for the short step

Queue row 1017 of `FINISH.md`, read at commit 2cdb35e78. Worker: Claude Fable 5.2, max effort, Mac mini worker 2. Started 2026-11-15T19:56Z (`date -u`). No file is edited except this one (and any new lemma file under `library/` named below). No commit, no push: a relay copies this file.

This is research-stage working state. It grants no status. Marks used: PROVED (every step written here, by hand), ARGUED (argument given, one named step not written out), OPEN, FAILS (explicit counterexample or failing step).

## Plan (at most eight steps; one step per response; each step is appended before the next starts)

1. **Read and pin.** FINISH rules; `parts/gap.md` (Corollary Z4, Theorem ZD-c, the test table); rows 1002, 1011, 1013 and their notes; grep the lane for earlier compactness, limit-point and rigidity attempts ((N) of row 978, limit points of effective actions, `library/gap-ladder-max.md`, `library/gap-crux-fp.md`). Duplicate-attack check against `library/open-core.md` and the FINISH rows. Output: the exact statements this note reads, with file and line.
2. **Exercise skill and literature lens.** Fetch the exercise skill at main commit 8b11ae2bb9 into a new folder under /tmp, follow it. Literature: Kenig-Merle concentration-compactness and rigidity; limits of lattice gauge measures; generalized symmetries; what is published and what each source proves.
3. **Task (1), the compactness step.** State it exactly: topology, what is kept, what can be lost. Test it against the no-rigidity models first (Lemma PT, Proposition NP, the five-dimensional test of `library/gap-crux-fp.md`, a product with a massless factor).
4. **Task (2), the rigidity statement.** State it exactly. Test it against compact U(1) (it must fail there), frozen Q_8 and 2T.
5. **Task (3), first surviving piece.** Prove it by hand, or build the counterexample.
6. **Task (3) continued** if step 5 grows long, or the second surviving piece.
7. **Task (4), the consumer.** Which form of (W) or of the seed the contradiction yields; what it changes in `parts/gap.md`.
8. **Verdict table and RESULT line.**

## Step log

(Each step below is appended when it is finished. A step that stops early says where it stopped.)

## 1. Step 1 result: what was read, what is pinned, what was found again

### 1.1 The statements this note reads (file and line at commit 2cdb35e78)

- **Objects (DEF).** `library/gap-crux-restate.md` L29-45. Wilson SU(2), torus n = (n_1, ..., n_4), sides at least 3, Z(n), F = log Z, f = inf F(n)/abs(n), Delta(n) = F(n) - f abs(n) >= 0. Box B, transfer operator T_B, eigenvalues lambda_0 > lambda_1 >= ..., m(B) = log(lambda_0/lambda_1), S(k; B) = sum over i >= 1 of (lambda_i/lambda_0)^k. D(a) = Delta(a, a, a, a) (`library/gap-phys-seed.md` L247).
- **Engine.** Theorem S, `gap-crux-restate.md` L192-203; Corollary S3', L217-219. Lemma A, Lemma K, Lemma X, Lemma E (L37, L178-190). Checked in rows 698, 699.
- **Theorem ZD** (`gap-phys-seed.md` L296-304): at one coupling, (A) seed, (B) D(a) <= 6.1 x 10^(-4) for one a, (C) b m(b^3) >= 256 D(b/4) + 29.64 for one b, (D) "D bounded and sup of b m(b^3) infinite" are equivalent.
- **Theorem ZD-c** (L311-320): along a trajectory (a_j, beta_j) with the sizes P = {2^i l_1}, D^+(L) = limsup_j D_j(L/a_j), z^-(L) = liminf_j (L/a_j) m_j((L/a_j)^3): (PHYS-SEED) iff (BDD-Delta) and (Z-UNB).
- **Corollary Z4** (L322-323): if D(a) <= D_0 for a >= a_0, then either b m(b^3) < 256 D_0 + 29.64 for every multiple b >= 4 a_0 of 4 (**branch G, the gapless branch**), or there are N, c > 0 with m(L^3) >= c/N for all L >= 2N.
- **The wall (W)** (`parts/gap.md` L18-20): along the account's trajectory there is a physical size L in P with z^-(L) > 256 D_0 + 30, D_0 a bound of D^+ on the sizes from L/4 on.
- **Test table** (`parts/gap.md` L193-207) and its five points (L211-223). Point 5: no model of the SU(2) class with first-passage data and no gap is on record.
- **Lemma PT, Corollary PT1** (`library/gap-crux-exercise3-max.md` L690-720): products; a product with compact U(1) in its massless phase has no seed. **Proposition NP**: `library/gap-crux-exercise4-max.md` 5.1 (read in Step 3). **Five-dimensional test**: `library/gap-crux-fp.md` F15 (L50), L76, L88 (GUIDE grade).
- **Row 1002** (`library/prior/gap-kflow-read-opus.md` L95-102, L299, L324): every published monotone is blind; for SU(2) a_UV = 3 a_V, so an end with one or two free photons is allowed by the a-theorem.
- **Row 1011** (`library/gap-pinned-cell-gauge-max.md`): Proposition W (L184-199), the exact second-order Ward identity with its bracket term; Lemma CEN and Corollary CEN2 (L263-286): a link twist that is an exact symmetry is central, so it has no bracket. In its own reading (L290-292): "the symmetric link twists are the one-form symmetry, and a one-form symmetry is abelian."
- **Row 1013** (`library/gap-invent-selective-max.md` L250-252, L275-277): the 2D engine in 4D works only while a colour frame exists; the missing object is a short step at order-one response. Reopen conditions (i), (ii).

### 1.2 Earlier compactness, limit-point and rigidity attempts in the lane (found again; none is a Kenig-Merle architecture)

Grep of `library/gap-*.md`, `library/prior/gap-*.md`, `parts/*.md` for: Kenig, concentration compactness, critical element, profile decomposition (no hit outside this file); rigidity; limit point, limit object, subsequence, tightness, scale-invariant limit, massless limit; one-form, generalized symmetry, emergent.

| Earlier item | Where | What it holds | Relation to this row |
|---|---|---|---|
| Crux lemma (N) of A1, row 978 | `library/gap-ladder-max.md` L67 | "a seed with margin for every limit point of the reference-scale effective actions, in a topology in which the seed functional is continuous"; first doubt: closeness of order 1/volume in the local sup norm is needed | This is the compactness step in its direct form. It was named, not attacked. Step 3 below states it exactly and tests it. |
| A6, continuum value, row 978 | same file L77 | "(C + N): the limit exists, and it is below 1/5041 at one ell_*"; doubt: the thermal sum is a trace over all states of a large box | Same object: a limit of ratios of torus partition functions. |
| Limit states of a seeded sequence | `library/gap-seed-limit.md` L140-172, L258-282 | Tychonoff compactness for states on local functions of the lattice at one coupling; every limit state clusters, GIVEN the gap hypothesis (G) | Compactness of the gapped branch, on the lattice at fixed coupling. Not a limit along the trajectory, and not the gapless branch. |
| Item 29 of the second brainstorm | `library/gap-brainstorm2-max.md` L179, L239, L318 | "either (Z-UNB) holds, or the limit theory contains a massless singlet vector state, that is, an emergent conserved two-form current. Then exclude the second branch for SU(2) (no continuous one-form symmetry survives non-abelian fusion)"; verdict there: "needs a monotone parameter ... equals Theorem R" | The rigidity seed of this row, in one sentence, dropped without a statement. This row states it and tests it (Step 4). |
| Row 745 literature | `library/prior/gap-lit-rigid.md` | Nguyen, Tanizaki and Unsal 2023 (arXiv:2306.02485): for a gapped 4D theory with Z_N one-form symmetry, the pattern of light flux sectors, under a 0/1 assumption on sector ratios | Rigidity inside the gapped branch (Theorem R of row 742). Not the gapless branch. |
| Soft exclusion of branch G | row 988 Route 3 (`parts/gap.md` L61-62, L65-66) | set aside; re-judged "too strong" by row 998 6d | The only earlier attempt on branch G by soft means. Its verdict binds Step 4: a class-wide soft statement with no ultraviolet hypothesis is refuted by w_p (Proposition V) and by U(1). |
| "Rigidity" elsewhere in the lane | `gap-means-max.md` (duality rigidity, Theorem R); `gap-seeddec-max.md` (rigidity of minimal fillings) | other meanings of the word | none |

### 1.3 Duplicate-attack check (rule 0a)

`library/open-core.md`: no line on compactness, rigidity, a critical element, a limit object, branch G, or a one-form symmetry (grep, zero hits). FINISH rows naming these words: 745 (literature on flux-sector rigidity) and 1017 (this row). Row 1016 (`gap-global-reform-max`, running now on worker 1) takes reopen condition (i) of row 1013: an exact reformulation with a global non-abelian symmetry. It is not this architecture. I do not attack its candidates. I do not attack (CAS), (HC-phys), (MONO-Delta), (TUBE'), (NOCRIT) or any statement that an earlier row holds; where a step below reduces to one of them, I name the match and stop there.

### 1.4 Not read in Step 1

The bodies of rows 1003, 1004, 988, 982; the account's TeX; every primary paper. Each is read at the step that needs it.

