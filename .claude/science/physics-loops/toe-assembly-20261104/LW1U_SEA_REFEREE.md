lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# LW1-U_sea referee report (pass 3)

Written 2026-11-06 (UTC) by a Claude Opus 5.5 headless lane on the Mac mini, as pass 3 (the referee) under PR #10138's method: Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen. Lane: referee of `LW1U_SEA.md` (part LW1, item LW1-U_sea).

**Referee.** Claude Opus 5.5 (model id `claude-opus-5-5`), max effort, headless on the Mac mini; session clock 2026-11-05 21:29 EST. This session wrote neither pass 1 (`LW1U_SEA_DRAFT.md`, with its source `LW1U_DRAFT.md`) nor pass 2 (`LW1U_SEA.md`). This is one check: one line-by-line read of `LW1U_SEA.md`, compared with its pass-1 sources where it cites them. No other review was read for content; `LW1_REFEREE.md` was read for its format only. No review of this review was commissioned. No subagent was used.

**What this file is.** A referee report. It grants no status, adopts no law, reading or definition, and changes no axiom or working-set entry. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. A "referee closure" is a short complete argument, written here, for a step the text leaves out. "[check]" marks a tiny floating-point scratch computation: `check_sea_ref.py` and `check_cube_ref.py` in `/tmp/toe-usearef/`, about one second and 260 MB in all, largest space an `8^3` torus of 512 sites, started with 60 percent of memory free. A check guides or refutes. It never proves. Every verdict rests on a hand derivation meant to be Lean-formalizable.

**Text read.** `LW1U_SEA.md` as added in commit `c96e71cdf` (unchanged at branch head `c96e71cdf`). SHA-256 of the file read: `b866e215a14fa014cb18a5b5f63548f7587c3bba6926d8266af06ae6fcd2d5db`. Line numbers below refer to that file.

**Source revisions read.**

| Ref | Commit |
|---|---|
| branch `claude/toe-assembly`, local checkout (HEAD) | `c96e71cdf` |

Files read at that commit, by line, with the commit that last changed each. All are in `.claude/science/physics-loops/toe-assembly-20261104/` unless a path is given.
- `LW1U_SEA.md` (`c96e71cdf`): lines 1-123, all of it.
- `LW1U_SEA_DRAFT.md` (`2d0adc0c0`): lines 1-403, all of it. Its SHA-256 equals the hash `LW1U_SEA.md` line 5 records (`ed0746a646a505736bbb3301608035637153b111c75fbea59c17eeac5c49e7bc`).
- `LW1U_DRAFT.md` (`73d98e1a8`): lines 1-386, all of it. Its SHA-256 equals the hash `LW1U_SEA.md` line 5 records.
- `LW1.md` (`5ff19240c`): lines 1-508, all of it. Its SHA-256 equals the hash `LW1U_SEA.md` line 5 records.
- `TOE_ASSEMBLY.md` (`7d2b20d29`): lines 95-219 (sections 3.1-3.5). Its SHA-256 equals the hash `LW1U_SEA.md` line 5 records.
- `LW1_5_DRAFT.md` (`e648fa3e0`): lines 296-330 (sections 8.1-8.3) and 370-410 (carry-over rows, A2-5, B8-5).
- `LW1_REFEREE.md` (`5a2a0affe`): lines 1-100 and 226-238, for the format only. `Y2W_DRAFT.md` (`92e03055c`): lines 1-40, for the head format only. `AGENTS.md` (`91ccfa0ca`), for the rules.

Between the distiller's base `5ff19240c` and `c96e71cdf` none of the four hashed sources changed (`git diff --stat` is empty). No other branch was read. No existing file was edited.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The premises of `LW1U_SEA.md` are read plainly: PS-3h, PS-7r, the joint Born identification, and PS-3h5 where Theorem 12 assumes it. This report proposes no reading, specification or definition, so no four-test smuggle check is run here.

**Working set used, by name.** These are the entries the checked text uses; the referee used no others. PS-1 read by PS-1c, only through the free tick of `L_cube` (`LW1.md` section 1). PS-3 read by PS-3h (support and transport). PS-7 read by PS-7r (the sea). PS-3c, only through `LW1.md` B8a in line 121. PS-5, and the proposed reading PS-3h5 of `LW1_5_DRAFT.md` section 8.2 (not adopted), only for Theorem 12.

**Inputs from outside the working set.** The joint Born identification (`LW1.md` inferred definition 26), which the checked text takes as a premise. Standard mathematics, re-derived where a verdict uses it: Wick's determinant rule; the Slater formula for matrix elements of a Fock lift; the continuous functional calculus with Stone-Weierstrass; Riesz projections and their first-order expansion; the identity theorem for real-analytic functions; Bloch decomposition over a cell lattice; Shannon entropy subadditivity and its equality case. No literature is used here.

**Method.** Every statement and proof step was re-derived by hand. The arithmetic was then compared with a [check]. Verdicts: CORRECT; ERROR (a false or misleading line, quoted, with its fix); INCOMPLETE (a named missing step, with a referee closure). Each citation of another file was compared with that file.

**Counts.** 101 items: 85 CORRECT, 7 ERROR, 9 INCOMPLETE. The ERRORs are three symbol clashes, one wrong description of a face, one sentence that says "admissible" where it means "selected", one use of the reserved word "proposed", and one citation. The INCOMPLETE items are one-line steps, each closed in section 2.2. No ERROR or INCOMPLETE item changes the content of a theorem. The distiller's one GAP is real (section 3).

---

## 1. Verdict table

| # | Item (`LW1U_SEA.md` line) | Verdict | Note |
|---|---|---|---|
| 1 | Title; status, sentence 1 (1, 3) | CORRECT | "the Born law" is the free sea's; say so. |
| 2 | Status: the sea's transport is the diagonal singleton at `h = 0` in the window and at `h = 1` off `Σπ` (3) | CORRECT | This is Theorem 4. |
| 3 | Status: positive cost on `Σπ`; LW1-U_hop, its five-flavour form and LW1-U_f open; no counterexample (3) | CORRECT | "Positive cost" uses item 53's closure. |
| 4 | Status: the GAP sentence (3) | CORRECT | The gap is real (section 3). |
| 5 | Status: last sentence (3) | CORRECT | |
| 6 | Provenance (5) | CORRECT | All four recorded hashes verified. Effort is stated twice ("high", "not visible"); merge. |
| 7 | Definition 1: cubes and hop operators (9) | ERROR | Gives `η_i` a factor `1/√3`, a second meaning. |
| 8 | Definition 2: angles (10) | ERROR | `b` also names the cell index. The bounds are correct. |
| 9 | Definition 3: sea, covariance, half-step rule (11) | CORRECT | |
| 10 | Definition 4: support, `C_h`, `d̄`, `O_h`, diagonal coupling (12) | CORRECT | These are defined in `LW1.md` section 1 ("Transport"); E6 proves the entropy limit. |
| 11 | Definition 5: `Σπ` parameter, product point, classes, finer field (13) | CORRECT | |
| 12 | Definition 6: (CL) and (CL′) (14) | CORRECT | Matches `LW1U_DRAFT.md` line 306 and `LW1U_SEA_DRAFT.md` line 279. |
| 13 | Definition 6: "(CL) implies (CL′)" (14) | INCOMPLETE | The `ν_2` half, with the same `λ`, needs Theorem 7 and E4. |
| 14 | Definition 7: premises; PS-3m report (15) | CORRECT | The report matches `LW1U_DRAFT.md` section 8. Wording note in 2.3. |
| 15 | Theorem 1: principal minors fix the law (19) | CORRECT | |
| 16 | Theorem 1: Fock-lift matrix elements (19) | CORRECT | |
| 17 | Theorem 1: layer rule `G ↦ WGW*` (19) | CORRECT | |
| 18 | Theorem 1: proof (21) | CORRECT | |
| 19 | Theorem 2: statement (23) | CORRECT | Name the initial state `ω_0 = ω_G`. |
| 20 | Theorem 2 proof: symmetric half-steps, `V_e V V_e* = V^T` (25) | CORRECT | |
| 21 | Theorem 2 proof: `f(V^T) = f(V)^T` (25) | CORRECT | `σ(V^T) = σ(V)` follows from the conjugation. |
| 22 | Theorem 2 proof: covariances `G, Ḡ, G, …` (25) | CORRECT | [check] |
| 23 | Theorem 2 proof: equal principal minors give equal laws (25) | CORRECT | |
| 24 | Theorem 2 proof: `μ > 0`, the upper projection is continuous in `V` (27) | CORRECT | |
| 25 | Theorem 2 proof: `μ = 0` by fibres (27) | CORRECT | "almost everywhere" should read "on every fibre `K ≠ 0`". |
| 26 | Pass-1 check report (29) | CORRECT | Matches `LW1U_SEA_DRAFT.md` line 153. |
| 27 | Theorem 3: statement (31) | CORRECT | "contains exactly the diagonal coupling" should read "is the diagonal singleton". |
| 28 | Theorem 3 proof: the diagonal amplitude is nonzero (33) | CORRECT | |
| 29 | Theorem 3 proof: diagonal admissible, zero cost, the only zero-cost coupling (33) | CORRECT | |
| 30 | Theorem 3 proof: `cos θ = 0` (33) | CORRECT | |
| 31 | Theorem 4: statement (35) | CORRECT | |
| 32 | Theorem 4: proof (37) | INCOMPLETE | Uses that `ω_1` is cell-invariant; not shown. |
| 33 | Theorem 4: history clause (35, 37) | CORRECT | Say "with each step selected from `O_h`". |
| 34 | Theorem 5: statement (39) | CORRECT | |
| 35 | Theorem 5: proof (41) | INCOMPLETE | Uses that the torus spectrum lies in `σ(V)`; not shown. |
| 36 | The entropy stage is idle (43) | CORRECT | |
| 37 | Theorem 6: statement (47-48) | CORRECT | |
| 38 | Theorem 6 proof: corner probability `m/8` (50) | INCOMPLETE | Uses invariance of `ν_P` under the 24 rotations; not stated. |
| 39 | Theorem 6 proof: independence, homogeneity, Wick (50) | CORRECT | |
| 40 | Theorem 6 proof: boundary witness `1/12` and `0` (52) | CORRECT | [check] |
| 41 | Theorem 6 proof: analyticity on `Ω`, identity theorem (52) | CORRECT | |
| 42 | Remark on (CL) (54) | CORRECT | The sufficiency is `LW1U_DRAFT.md` Theorem 10.2 (pass 1); cited, not load-bearing. |
| 43 | Theorem 7: the odd gate is `iR_o` (58) | CORRECT | |
| 44 | Theorem 7: support criterion (58, 60) | CORRECT | |
| 45 | Theorem 7: the support is symmetric (58, 60) | CORRECT | |
| 46 | Theorem 7: odd number forces two changes (60) | CORRECT | |
| 47 | Theorem 7: fibre identity `V + V* = 2 sin(a) χ(K) I` (62) | CORRECT | |
| 48 | Theorem 7: trace formula (63-64) | CORRECT | [check] |
| 49 | Theorem 7: `P(K)` is not constant, so `P` joins distinct odd cubes (64) | CORRECT | |
| 50 | Theorem 7: the compression `G_D` is not a projection (64) | CORRECT | |
| 51 | Theorem 7: parity determinant, `ν_P(N_D odd) > 0` (65-66) | CORRECT | [check] |
| 52 | Theorem 7: bound on changes per odd cube (58, 66) | CORRECT | |
| 53 | Theorem 7: "the asserted positive cost" (66) | INCOMPLETE | The step from changes per odd cube to `d̄` is missing (one line). |
| 54 | Theorem 8: definitions of `Z`, `D`, `Y` (68) | ERROR | `D` also names odd cubes. |
| 55 | Theorem 8: `ZPZ = I − P` (68, 70) | CORRECT | [check] |
| 56 | Theorem 8: `P̄ = YPY` (68, 70) | CORRECT | [check] |
| 57 | Theorem 8: `Y` constant on each odd cube, value `s_b` (68, 70) | CORRECT | [check] |
| 58 | Theorem 8: invariance under `R_o^s` (68, 70) | CORRECT | [check] |
| 59 | Theorem 8: `iR_o = (iY) R_o^s` (70) | CORRECT | |
| 60 | Theorem 8: a swap-invariant optimizer exists (68, 70) | CORRECT | |
| 61 | Open: LW1-U_hop (72) | CORRECT (open) | |
| 62 | The selection is discontinuous at `Σπ` (72) | CORRECT | |
| 63 | Theorem 9: points, cubes, classes (76) | CORRECT | |
| 64 | Theorem 9: the two expansions (77) | CORRECT | [check] |
| 65 | Theorem 9: consequence (78) | CORRECT | |
| 66 | Theorem 9 proof: twelve rotations, class-flat moduli (80) | INCOMPLETE | Uses invariance of `ν_1` under the twelve and their action on cubes and classes; not stated. |
| 67 | Theorem 9 proof: `P_0`, `Q_0`, `V(a)` (82) | CORRECT | |
| 68 | Theorem 9 proof: first-order Riesz formula (83) | CORRECT | |
| 69 | Theorem 9 proof: the entries (84) | ERROR | "the common face": the two cubes share no face. The numbers are correct. |
| 70 | Theorem 9 proof: conjugation and `a²/36` (84) | CORRECT | |
| 71 | Theorem 9 proof: analyticity, isolated zeros (84) | CORRECT | |
| 72 | GAP in pass 1, §5.5 (86) | CORRECT | The gap is real. The missing condition is locality, not homogeneity (section 3). |
| 73 | Theorem 10: definitions (88) | ERROR | "proposed" is a reserved word here; the form is a candidate. |
| 74 | Theorem 10: consistent and cell-invariant (88, 90) | INCOMPLETE | Cell invariance is asserted, not argued. |
| 75 | Theorem 10: marginals (88, 90) | CORRECT | |
| 76 | Theorem 10: support (88, 90) | CORRECT | |
| 77 | Theorem 10: `q(A,B) = det(P_0)_{AB} det(R_D)_{AB}` (92) | CORRECT | |
| 78 | Theorem 10: the two matrices and their determinants (93-95) | CORRECT | [check] |
| 79 | Theorem 10: the sign persists for small `a > 0` (95) | CORRECT | |
| 80 | Pass-1 one-cube report (97) | CORRECT | Matches `LW1U_SEA_DRAFT.md` line 338; the [check] reproduces it. |
| 81 | Theorem 11: statement (99) | CORRECT | |
| 82 | Theorem 11 proof: both laws are `⊗_D p` (101) | CORRECT | |
| 83 | Theorem 11 proof: cost and entropy counted on odd cubes (101) | INCOMPLETE | `d̄` and `s` are defined on even cells; the conversion is missing. |
| 84 | Theorem 11 proof: strict deficit by tiling (101) | CORRECT | |
| 85 | Theorem 11 proof: not diagonal, `1/16` (101) | CORRECT | Uses `N_D = 4` almost surely; say so. |
| 86 | Continuation attack: its three reasons (103) | CORRECT | |
| 87 | Continuation attack: citation of `LW1U_DRAFT.md` Theorem 4.3 (103) | ERROR | That theorem is stated at `δ = 1/32`; the family is pass 1's reading of its proof. |
| 88 | Theorem 12: hypotheses (107) | CORRECT | Conditional on PS-3h5, a proposed reading. |
| 89 | Theorem 12: the laws are unchanged (107, 109) | CORRECT | |
| 90 | Theorem 12: "the admissible transport is uniquely diagonal" (107) | ERROR | Means `O_h`; says `C_h`. |
| 91 | Theorem 12 proof: the coarse diagonal pair is supported; zero cost (109) | INCOMPLETE | Uses that the five-mode `ω_1` is cell-invariant; not shown. |
| 92 | Theorem 12 proof: on `Σπ` an odd total forces a change (111) | CORRECT | |
| 93 | Theorem 12 proof: probability `(1 − E[(−1)^{N_D^{(1)}}]^5)/2 > 0` (111) | CORRECT | |
| 94 | Theorem 13: statement (113) | CORRECT | Its hypothesis holds; closure in 2.3. |
| 95 | Theorem 13: proof (115) | CORRECT | |
| 96 | Theorem 13: the electric layer (115) | CORRECT | |
| 97 | Section 7: LW1-U_hop (119) | CORRECT | |
| 98 | Section 7: LW1-U_f (120) | CORRECT | |
| 99 | Section 7: VC1 and TM1 (121) | CORRECT | |
| 100 | Section 7: proposed readings (122) | CORRECT | |
| 101 | Section 7: pass-1 checks (123) | CORRECT | Matches `LW1U_SEA_DRAFT.md` lines 240, 259 and 303. |

---

## 2. Details of the non-CORRECT items

### 2.1 ERRORS

**Item 7 (line 9, notation).** `LW1U_SEA.md`: "Their edges carry `η_i(x)=(-1)^{Σ_{j<i}x_j}/√3`." In `LW1.md` section 1 the sign is "\(\eta_i(x)=(-1)^{\sum_{j<i}x_j}\)", with no `1/√3`. The line gives the symbol a second meaning. No later line uses `η_i`, so no proof is affected. Fix: "The edge `(x, x+e_i)` carries the weight `η_i(x)/√3`, with `η_i(x) = (-1)^{Σ_{j<i} x_j}` as in `LW1.md` section 1."

**Item 8 (line 10, notation).** `LW1U_SEA.md`: "`a = ε − μ/2`, `b = ε + μ/2`". Line 9 uses `b ∈ Z³` for the cell index, and Theorem 8 (line 68) uses `D_b` and `s_b` in that sense. Fix: use the names of `LW1.md` section 1, "\(a_e=\varepsilon-\mu/2\), and \(a_o=\varepsilon+\mu/2\)": "`V_e = exp(−i a_e R_e)`, `V_o = exp(i a_o R_o)`, `V = V_o V_e`. In the window, `0 < a_e < π/2` and `0 < a_o < π`." Keep `a = a_e = π/2 − μ` on `Σπ`, as line 13 does. The bounds themselves are right: `a_e > 0` because `μ < 2ε`; `a_e < ε < π/2`; `a_o < 2ε < π`.

**Item 54 (lines 68 and 70, notation).** `LW1U_SEA.md`: "`D_x=(-1)^{Σ_i x_i}`, and `Y=DZ`" and "`D\bar P D=I−P`". In the same theorem `D_b` is an odd cube, and elsewhere `R_D` and `N_D` index a cube by `D`. Fix: write `D_s`, as `LW1.md` section 1 does ("Put \(D_s|x\rangle=(-1)^{x_1+x_2+x_3}|x\rangle\)"), so `Y = D_s Z` and `D_s P̄ D_s = I − P`.

**Item 69 (line 84, a wrong description).** `LW1U_SEA.md`: "Across the common face, the two odd-edge entries relevant to `x,y` are `+1/√3` and `−1/√3`, while the even edge has weight `1/√3`." The cubes `D_0 = {1,2}³` and `D_{e_1} = {3,4} × {1,2}²` are disjoint and share no face. The two first-order paths from `x` to `y` run around the unit face with corners `(2,1,2), (2,2,2), (3,2,2), (3,1,2)`. That face has one odd edge in each cube and two even edges joining the cubes. Fix: "Around the unit face with corners (2,1,2), (2,2,2), (3,2,2), (3,1,2), which joins the two cubes, the odd edge in `D_0` has entry `+1/√3`, the odd edge in `D_{e_1}` has entry `−1/√3`, and both even edges have entry `1/√3`." The coefficient `1/(6i)` is correct (section 4.E).

**Item 73 (line 88, a reserved word).** `LW1U_SEA.md`: "**Theorem 10 (the proposed Margenau–Hill candidate fails positivity).** … define the proposed signed cylinder form". In this assembly "proposed" names a reading or specification put to the owner, which then needs the four-test check. Line 122 says "no new proposal is made here". The form is a candidate coupling inside an attack. Fix: replace both words "proposed" by "candidate". Also write `γ_+ = ∏_D Ad Γ(R_D)`: it is a product of commuting automorphisms, not a tensor product.

**Item 87 (line 103, citation).** `LW1U_SEA.md`: "`LW1U_DRAFT.md` Theorem 4.3 reports a non-factor family with singleton optimizer at its product endpoint and a nontrivial optimizer segment for small positive parameter." `LW1U_DRAFT.md` Theorem 4.3 concerns one state. Its parameter is fixed at line 103: "`delta = 1/32`". It names no family and no endpoint. The family is pass 1's reading of that proof, `LW1U_SEA_DRAFT.md` line 353: "`LW1U_DRAFT.md` Theorem 4.3 gives a family of invariant states, affine in a parameter `delta`, with `O_h` a non-degenerate segment for each `delta ∈ (0, 1/16)` (its proof uses `delta` only in Lemma 4.0(i), which needs `delta < 1/16`, and Lemma 4.0(iii), which needs `delta ≠ 0`)". That reading is right (section 4.E). Fix: "`LW1U_SEA_DRAFT.md` §5.7 observes that the proof of `LW1U_DRAFT.md` Theorem 4.3, stated at `δ = 1/32`, runs for every `δ ∈ (0, 1/16)`. At `δ = 0` the state is a product of equal cube states, the two Born laws are equal, and `O_h` is the diagonal singleton (Theorem 3)."

**Item 90 (line 107, a word with two meanings).** `LW1U_SEA.md`: "For either actual configuration, the admissible transport is uniquely diagonal off `Σπ`, so its history is constant." The file uses "admissible" for the elements of `C_h`: line 12 ("The admissible set `C_h`"), line 58, and the last sentence of the same statement ("every admissible odd-step transport moves"). Read so, the sentence says that `C_h` has one element. The proof shows that `O_h` has one element. Fix: "For either actual configuration, `O_h` is the diagonal singleton off `Σπ`, so the history is constant."

### 2.2 INCOMPLETE, with referee closures

**Item 13 (line 14).** `LW1U_SEA.md`: "(CL) implies (CL′), since the finer counts are cube-local functions." (CL′) uses one law `λ` for both `ν_1` and `ν_2`. The stated reason gives the `ν_1` half only. *Closure.* Given the number field `n`, the cubes are independent under (CL). Conditioning on the cube-local events `{m_D = v_D}` keeps them independent, with laws `α_{|v_D|}(· | m_D = v_D)` that depend on `v_D` only. This gives the `ν_1` half with `λ` the law of `m` under `ν_1`. For the `ν_2` half, E4 supplies some `π ∈ C_1`. By Theorem 7, `π`-almost surely `(N_O(c′_D), N_E(c′_D)) = (N_E(c_D), N_O(c_D))` for every odd cube `D`. So the swapped field of `c′` has law `λ` under `ν_2`, and the same conditioning gives the `ν_2` half. Theorem 9 uses only the `ν_1` half.

**Item 32 (line 37).** Theorem 3 needs a cell-invariant state: `LW1.md` line 95 defines `C_h` "For cell-invariant \(\omega_h\)". The proof does not show that `ω_1` is cell-invariant. *Closure.* `ω_1` is quasi-free with covariance `P̄` (Theorem 2). Each cell translation `T_{2b}` is a real permutation matrix. It commutes with `R_e` and `R_o` (`LW1.md` A2: "Even translations preserve its phases exactly"), so with `V` and its spectral projection `P`, and, being real, with `P̄`. Hence `ω_1` is cell-invariant. (`LW1U_SEA_DRAFT.md` line 179 gives the same fact through A2.)

**Item 35 (line 41).** The proof needs the torus sea to exist and be gapped. *Closure.* For even `L`, the cell-momentum fibres of the torus tick `V_L` are the fibres `V(K)` at the torus momenta `K ∈ (4π/L) Z³`. So `σ(V_L) ⊂ σ(V)`, which avoids `±1` when `μ > 0`. Thus `π` lies in a gap of `V_L`, the PS-7r torus sea is `P_L = f_P(V_L)`, and `P(K)` is continuous in `K` (a Riesz integral over a fixed contour), which the Riemann-sum step uses.

**Item 38 (line 50).** `LW1U_SEA.md`: "Rotations about `C_0` preserve its number and act transitively on its corners. Hence each corner has conditional occupation probability `m/8`". The step also needs: the rotations preserve `ν_P` and map even cubes to even cubes. *Closure.* The 24 rotations about `c_0` form `O_{c_0} ⊂ 𝒢`. Their lifts `D_d P_Q` fix `R_e` and `R_o` (`LW1.md` A2: "The signed permutation \(D_dP_Q\) consequently fixes both \(R_e,R_o\)"), so they commute with `V` and `P`, and `ω_P` is invariant (B10(3)). A diagonal sign changes no occupation, so `ν_P` is invariant under the site permutation. A2's proof sends even cube centres to even cube centres. So each rotation fixes `C_0` and the event `{N_{C_0} = m}`, and `α_m` is invariant.

**Item 53 (line 66).** `LW1U_SEA.md`: "The support bound yields the asserted positive cost." The bound concerns changes per odd cube. The cost `d̄` of `LW1.md` line 97 counts changes on `C_0 = {0,1}³`. *Closure.* `D_0 = {1,2}³` and `C_0` each contain exactly one site of each class of `Z³` modulo `2Z³`. For a cell-invariant `π`, each site's change probability depends only on its class. So `E_π Σ_{x∈D_0} 1[ξ_x ≠ ζ_x] = E_π Σ_{x∈C_0} 1[ξ_x ≠ ζ_x] = 8 d̄(π)`, and `d̄(π) ≥ ν_P(N_D odd)/4 > 0` for every `π ∈ C_1`.

**Item 66 (line 80).** `LW1U_SEA.md`: "the twelve parity-preserving cube rotations would make each corner's conditional occupation probability `m_E/4` or `m_O/4`". The step also needs: the twelve preserve `ν_1`, map odd cubes to odd cubes, fix `D_0` and keep the two corner classes. *Closure.* A rotation about the centre of `D_0` is a rotation about `c_0` followed by an even translation (`LW1.md` A2: "Rotations about other even or odd cube centres differ from these by even translations"), so it lies in `𝒢`. Its lift commutes with `R_e` and `R_o`, so with `V_e` and `P`, so with `P̄ = V_e P V_e*`; hence `ν_1` is invariant. A2's proof sends odd cube centres to odd cube centres, and the rotation fixes `D_0`. Write it as `x ↦ Q(x − c) + c` with `2c = (3,3,3)`, where `Q` permutes coordinates by `κ` and flips the signs on a set `F`. Then `Σ_i x_i` changes by `3|F| − 2Σ_{i∈F} x_{κ(i)}`, which is even exactly when `|F|` is even. With `det Q = 1` this means `κ` is even. There are `3 · 4 = 12` such `Q`: the rotations of the tetrahedron `E_{D_0}`, transitive on `E_{D_0}` and on `O_{D_0}` [check: 12 rotations; the orbit of `(1,1,2)` is `E_{D_0}`]. So each rotation maps the field `m` to a permuted field with `m_{D_0}` fixed, and `α_v` is invariant. The word "Homogeneity" in line 80 can go: the twelve rotations about the centre of `D_k` give the one-point function in `D_k` directly.

**Item 74 (lines 88 and 90).** `LW1U_SEA.md`: "It is consistent and cell-invariant". The proof argues additivity only. *Closure.* Even translations preserve every `η_i` (`LW1.md` A2: "Even translations preserve its phases exactly"). So `T_{2b} R_D T_{2b}* = R_{D+2b}`, and the translation automorphism commutes with `γ_+`. With `ω_1` cell-invariant (item 32), `q(τ_b E × τ_b E′) = q(E × E′)`.

**Item 83 (line 101).** The cost `d̄` and the specific entropy `s` of `LW1.md` lines 97-101 are defined on even cells: "\(Q_m=\{0,\ldots,2^m-1\}^3\) is a box of cells". The proof counts cost per odd cube and applies subadditivity over odd cubes. *Closure.* For the cost, see item 53. For the entropy, let `B_m` be the site set of `Q_m` and `B′_m = B_m + (1,1,1)`, the site set of the odd cubes `D_b`, `b ∈ Q_m`. With `n = 2^{m+1}`, `|B_m \ B′_m| = |B′_m \ B_m| = n³ − (n−1)³ ≤ 3n²`. Each site carries a pair `(ξ_x, ζ_x)` with four values. So `H_{B_m} ≤ H_{B_m ∪ B′_m} ≤ H_{B′_m} + 3n² log 4`, and the same with the boxes exchanged. Divide by `|Q_m| = n³/8`: the difference tends to zero, so the limit over boxes of odd cubes is `s`.

**Item 91 (line 109).** The PS-3 sets of the five-mode law need a cell-invariant `ω_1`. *Closure.* `W_{x+2b} = i^{Σ_i x_i + 2Σ_i b_i} = (−1)^{Σ_i b_i} W_x`, so `(W P̄ W*) ⊗ I_5` is cell-invariant when `P̄` is (item 32).

### 2.3 Notes on CORRECT items that bear on the freeze

- **Item 1.** "the Born law is unchanged" should read "the free sea's Born law is unchanged".
- **Item 6.** Line 5 states the effort twice: "reasoning effort high" (set by the lead from the run log) and "effort: not visible" (the distiller). Keep one sentence that gives both sources.
- **Item 10.** `C_h`, `d̄`, `s` and `O_h` are defined in `LW1.md` section 1 ("Transport", lines 95-101); E6 proves the limit defining `s`. Cite so.
- **Item 14.** The selection by fewest changes, then greatest entropy, is PS-3's own text (`TOE_ASSEMBLY.md` line 114: "It moves by the support-respecting transport that changes the fewest modes, and among those has maximal entropy"); PS-3h says when it acts. `LW1.md` calls the joint Born identification a premise (inferred definition 26). So "supplied readings" should read "premises: PS-3 read by PS-3h, and the joint Born identification".
- **Item 19.** State the initial state: "Start from `ω_0 = ω_G`."
- **Item 21.** `f(V^T)` is defined because `V^T = V_e V V_e*` has the spectrum of `V`.
- **Item 25.** "hence `V_e P V_e*=P^T` almost everywhere" should read "the fibre identity holds for every `K ≠ 0`, so `V_e P V_e* = P^T` as operators".
- **Item 27.** "contains exactly the diagonal coupling" should read "is the diagonal singleton".
- **Item 33.** "a history built using LW1 E5" should read "a history built by LW1 E5 with each step selected from `O_h`" (E5's last sentence).
- **Item 42.** The sufficiency of (CL) is `LW1U_DRAFT.md` Theorem 10.2, a pass-1 result. It is cited and not rebuilt here; no result of `LW1U_SEA.md` rests on it.
- **Item 64.** [check: on the `8^3` torus, `|P̄_{x′y}|/a²` is below `10^{-15}` at `a = 0.3` and `a = 1.0`.] This suggests that `P̄_{x′y}` vanishes on the whole line `a_o = π/2`. It is not proved and not needed.
- **Item 85.** "The all-E four-particle pattern has probability `det(I_4/2)=1/16`" uses `N_D = 4` almost surely (`P_0` restricted to `D` is a rank-four projection), so the probability that all E-corners are occupied equals the probability of the pattern.
- **Item 88.** PS-3h5 is a proposed reading (`LW1_5_DRAFT.md` section 8.2, "Proposed readings needed by the law (adopt nothing)"). Theorem 12 holds under it and says so ("Assume").
- **Item 94, referee closure.** Line 113 assumes that the dressed generators "are real symmetric in the occupation/link basis". This holds. In the basis of occupation states (modes in one fixed order) times link states `|m⟩`, each `c_y^† c_x` with `x ≠ y` has entries in `{0, ±1}` (Jordan-Wigner signs), and `J_ℓ` has real nonnegative entries (`LW1.md` section 1). So each term `η_i(x)(c_y^† J_ℓ c_x + c_x^† J_ℓ^† c_y)/√3` is real and Hermitian, hence real symmetric, and so is `H_C`. Theorem 13 therefore holds without the "suppose", for `τ_E = 0` on a finite even torus. `LW1U_SEA_DRAFT.md` line 374 stated this fact without the sign detail.

---

## 3. The distiller's GAP (line 86)

**The GAP is real.** Pass 1, `LW1U_SEA_DRAFT.md` line 305: "**Where Attack 1 fails, exactly.** The pair of cubes `(D_0, D_{e_1})` is not conditionally independent given the shared field. The dependence appears at first order in `a`, through a face with phase `-1` that straddles the even edge between the cubes." Proposition 5.6 of pass 1 (Theorem 9 here) does not prove the first sentence.

**What the contradiction uses.** It refutes a representation `ν_1 = ∫ ⊗_D α_{m_D} dλ(m)`. Such a representation has three properties:
- (a) given the full field `m`, the odd cubes are independent;
- (b) given `m`, the law of `c_D` depends on `m_D` only (locality);
- (c) one law `α_v` serves every cube (homogeneity).

Property (c) is not needed. The twelve rotations about the centre of `D_k` give the one-point function `v_E/4` or `v_O/4` in `D_k` directly (item 66). Under (b), (c) also follows from cell invariance, because conditional laws are unique up to null sets and a cell translation carries the conditional law at `D` to the one at its translate.

Property (b) is where line 305 overreaches. Without (b), `E[c_x | m]` may depend on the counts of other cubes and, inside one class, on `x`. Then (a) gives only `E[c_x c_y] = E[E[c_x | m] E[c_y | m]]`. The rotations about the centre of `D_0` move `D_{e_1}`. They relate this pair of cubes to other pairs, and they constrain nothing inside one pair. So the proof does not reach the claim. The line-86 phrase "the homogeneous local-law condition could fail separately" is right in substance; the condition that matters is the local-law part (b).

**The order in `a`.** The entry `P̄_xy = ia/6 + O(a²)` is first order. The occupation covariance is `Cov(c_x, c_y) = −|P̄_xy|² = −a²/36 + O(a³)`, which is second order. The distiller's sentence "The first-order expansion is for a covariance entry, not a proved first-order conditional dependence" is right.

**Repaired statement.** Theorem 9 as written, with "(CL′) fails" read as: *`ν_1` has no version in which, given the full shared field `m`, the odd cubes are independent and each cube's conditional law depends only on its own count pair `m_D`.* Pass 1's line 305 becomes: "Attack 1 fails at its hypothesis. (CL′) is false near the product point and off a discrete subset of `Σπ` (Theorem 9). The witness is the two-point function: `|P̄_xy|² − |P̄_{x′y}|² = a²/36 + O(a³)`."

**Carry the stronger claim?** No. No statement of `LW1U_SEA.md` uses it. The attack fails without it: the route of `LW1U_DRAFT.md` Theorem 10.2 needs (a) and (b) together, because its per-cube target `λ*_{n_k}` depends on the cube's own count ("given `n_Lambda` the configuration of cube `k` has law `alpha_{n_k}`", line 314). Theorem 9 shows that (a) and (b) do not both hold. Line 86's last clause "the stronger dependence claim remains open" should read "the stronger dependence claim is not used and is dropped". It is not an open statement of this part.

---

## 4. Checks behind the verdicts, section by section

### 4.A Head and section 1 (items 1-14)

The SHA-256 of each file read equals the hash `LW1U_SEA.md` line 5 records. `5ff19240cf33824df71619ddac9ce2f943db6247` is the full hash of `5ff19240c`. The window bounds of item 8 are re-derived in 2.1. `Σπ` lies in the window: if `2ε + μ = π` and `0 < μ < π/2`, then `2ε = π − μ ∈ (π/2, π)`, so `μ < π/2 < 2ε < π`. Conversely, inside the window `2ε + μ = π` forces `μ < 2ε = π − μ`, so `μ < π/2`. On `Σπ`, `a = a_e = π/2 − μ ∈ (0, π/2)`. Items 12 and 14 were compared with `LW1U_DRAFT.md` lines 306 and 224-241. Its smuggle check reads "Pass", "Pass", "Pass, with that note", "Pass", and its limit (a) covers the case "If the factor components are invariant under no finite-index lattice of cell translations". `LW1.md` Amendment 1 records "Non-factor states: no rule is adopted." The report in line 15 is accurate.

### 4.B Section 2 (items 15-36)

*Theorem 1.* `∏_{x∈A} n_x = c†_{x_1}⋯c†_{x_k} c_{x_k}⋯c_{x_1}`, and Wick's rule gives `det[ω(c†_{x_i} c_{x_j})] = det[G_{x_j x_i}] = det G_AA`. Inclusion-exclusion gives every cylinder probability; cylinder events form a π-system that generates the product σ-field. For the Fock lift, `⟨0| c_{a′_n}⋯c_{a′_1} c†(f_1)⋯c†(f_n) |0⟩ = det[⟨e_{a′_i}, f_j⟩]`, with `f_j = u e_{a_j}`. For a layer, `Γ(W)* c_x Γ(W) = Σ_z W_{xz} c_z`, so `ω_G(β(c†_y c_x)) = Σ_{z,z′} conj(W_{yz}) W_{xz′} G_{z′z} = (WGW*)_{xy}`.

*Theorem 2.* Let `J` be complex conjugation in the site basis; then `X^T = J X* J`. Transposition is linear, isometric, reverses products and commutes with adjoints. `R_e` and `R_o` are real symmetric, so `V_e^T = V_e`, `V_o^T = V_o`, and `V^T = V_e V_o = V_e V V_e*`. For a polynomial `p` in `z` and `z̄`, `p(V, V*)^T = p(V^T, V^{T*})`, because `V^T` is normal. Polynomials in `z, z̄` are dense in `C(σ(V))` (Stone-Weierstrass), the functional calculus is isometric, and `σ(V^T) = σ(V)`. So `f(V)^T = f(V^T) = V_e f(V) V_e*`. Since `f` is real, `G^T = Ḡ`. Then `V_o Ḡ V_o* = V G V* = G`, and `det Ḡ_AA = conj(det G_AA) = det G_AA`. [check: on the `8^3` torus at pass 1's four points, `|V_e P V_e* − P̄| ≤ 1.5e-15` and `|V_o P̄ V_o* − P| ≤ 1.6e-15`, while `max|P − P^T| = 0.071, 0.142, 0.298, 0.325`.] For `μ > 0`: B10's proof gives `Re λ = cos a_e cos a_o + sin a_e sin a_o χ(K) ∈ [cos 2ε, cos μ] ⊂ (−1, 1)`; the spectrum on `ℓ²` is the closure of the union of the fibre spectra; so `σ(V)` is two closed arcs, one in each open half-plane, and `f_P` is continuous on it. For `μ = 0`: from `X_{(b,r),(b′,r′)} = (2π)^{−3} ∫ e^{iK·(b−b′)} X(K)_{rr′} dK` one gets `(X^T)(K) = X(−K)^T`. Here `Re λ = cos²ε + sin²ε χ(K)`, which equals `1` only at `K = 0` and exceeds `−1` everywhere. For a normal matrix `M`, `1_{Im>0}(M^T) = 1_{Im>0}(M)^T`. So `V_e P(K) V_e* = P(−K)^T = (P^T)(K)` for every `K ≠ 0`, and the fibre `K = 0` is null (B10).

*Theorem 3.* `det(cos θ I ± i sin θ R_AA) = ∏_j (cos θ ± i sin θ r_j)`, and each factor has real part `cos θ`. Zero cost forces `ξ = ζ` on `C_0`, then on each translate, then everywhere (a countable union of null sets). For `A = {x}` and `cos θ = 0` the amplitude is `± i R_xx = 0`.

*Theorem 4.* `cos a_e > 0` in the window. `cos a_o = 0` exactly when `a_o = π/2`, that is `2ε + μ = π`. By Theorem 2 and Theorem 1, `ω_{2n} = ω_P` and `ω_{2n+1} = ω_1`. For the history, disintegrating `π_diag` gives `K_h(ξ, ·) = δ_ξ` for `ν_h`-almost every `ξ`; Ionescu-Tulcea gives `ℚ(ξ_{h+1} = ξ_h) = 1` for each `h`; intersect over `h`. At `μ = 0`, `a_e = a_o = ε ∈ (0, π/2)`.

*Theorem 5.* The transpose and amplitude identities hold verbatim in finite dimension. B7's unique coupling then has zero cost, so it is the identity coupling. `(P_L)_{xy}` is a Riemann sum of the continuous Bloch integrand of `P_xy` (with item 35's closure), so it converges to `P_xy`. Principal minors converge, and so do the cylinder probabilities of `(c, c)`.

### 4.C Section 3 (items 37-42)

Under (CL) at `h = 0`, with item 38's closure, each corner of each even cube has conditional probability `n_k/8`. So `E[c_x c_y | n] = (n_0/8)(n_k/8)` for `x ∈ C_0`, `y ∈ C_k`, and Wick's rule gives `E[c_x c_y] = 1/4 − |P_xy|²` (`P_xx = 1/2`, B10(2)). At `a_e = 0`, `V = e^{i a_o R_o}` with upper eigenvalue `e^{i a_o}` on `R_o = 1`, so `P = (I + R_o)/2`. The edge `(1,0,0)–(2,0,0)` is odd (its first coordinate `1` is odd), lies in the odd cube `{1,2} × {−1,0}²`, and has sign `η_1 = 1`; so `|P|² = 1/12`. The sites `(0,0,0) ∈ {−1,0}³` and `(3,1,1) ∈ {3,4} × {1,2}²` lie in different odd cubes, and `R_o` acts inside odd cubes; so that entry is `0`. [check: `0.0833333`; `F = 0.0789` at `(a_e, a_o) = (0.2, 0.9)`.] `Ω = {0 < 2ε < π, 0 < μ < π}` is open and convex. It contains the window and the line `μ = 2ε`. On `Ω` the real parts lie between `cos μ` and `cos 2ε` in either order (`a_e < 0` is allowed there), and both lie in `(−1, 1)`. So a fixed contour works locally, `V` is entire in `(a_e, a_o)`, each `P_xy` extends holomorphically, and `F` is real-analytic on `Ω`. `F = 1/12` on the line, so its zero set has empty interior (identity theorem).

### 4.D Section 4 (items 43-62)

*Theorem 7.* `V_o = cos(π/2) + i sin(π/2) R_o = iR_o`, and `⟨A′|Γ(iR_D)|A⟩ = i^n det R_{A′A}`. With E-corners first, `R_{A′A} = [[0, X], [Y, 0]]`, `X = R_{A′_E A_O}`, `Y = R_{A′_O A_E}`. If `|A′_E| > |A_O|`, then `|A′_O| < |A_E|` and the rank is at most `|A_O| + |A′_O| < n`; the other case is symmetric. So invertibility forces square blocks, and then `det R_{A′A} = ± det X det Y`. Symmetry: `det R_{AA′} = det (R_{A′A})^T`. For odd `N`, `|N_E − N_O| ≥ 1`, and each class changes in at least that many sites. On `Σπ`, `V = i cos a R_o + sin a R_o R_e`, so `V + V* = sin a {R_o, R_e} = (sin a/3) Σ_i (T_{2e_i} + T_{−2e_i})` (B10), whose odd-cell fibre is `2 sin a χ(K) I`. With `c = sin a χ(K)` and `s = (1 − c²)^{1/2}`, the eigenvalues are `c ± is`, and `P(K) = (1/2)[I + (V(K) − V(K)*)/(2is)]`. Here `V − V* = 2i cos a R_o + sin a [R_o, R_e]`, `tr R_D = 0`, `tr R_D² = 8`, and `tr(R_D [R_D, R_e(K)]) = tr R_e(K) − tr R_e(K) = 0`. So `tr(R_D P(K)) = 16 i cos a/(4 i s) = 4 cos a/s`. [check: the torus average of `4 cos a/s` equals `tr(R_{D_0} P_{D_0 D_0})` to ten digits, `3.8500070731` at `a = 0.3` and `2.3453186121` at `a = 1.0`.] A cell-invariant operator acts inside cells exactly when its fibre is constant (uniqueness of Fourier coefficients). For a projection `G`, `Σ_z |G_xz|² = G_xx`, while `(G_D²)_xx = Σ_{z∈D} |G_xz|²`. With `det(I + tM) = Σ_B t^{|B|} det M_BB` at `t = −2`, `E[(−1)^{N_D}] = det(I − 2G_D)`. [check: `ν(N_{D_0} odd) = 0.00017, 0.132, 0.493` at `a = 0.01, 0.3, 1.0`.]

*Theorem 8.* An even edge has `⌊x_i/2⌋ = ⌊(x_i+1)/2⌋`; across an odd edge the cell index steps by one. So `Z R_e Z = R_e`, `Z R_o Z = −R_o`, and `Z V_o Z = cos a_o − i sin a_o R_o = −V_o` at `a_o = π/2`. Since `1_{Im>0}(−V) = I − P`, `ZPZ = I − P`. B10(2) reads `Θ P Θ^{−1} = D_s P̄ D_s = I − P`. For `x = 2b + 1 + r`, `⌊x_i/2⌋ = b_i + r_i`, so `Z_x = (−1)^{Σb + Σr}`, `D_s(x) = −(−1)^{Σr}`, and `Y_x = −(−1)^{Σb}`. Stationarity gives `P = V_o P̄ V_o* = R_o P̄ R_o`. `Y R_o = R_o Y` because `Y` is constant on odd cubes, and `(R_o^s)² = I`. [check: `|ZPZ − (I − P)| ≤ 2.7e-15`, `|P̄ − YPY| ≤ 9.5e-16`, `|[P̄, R_o^s]| ≤ 1.3e-15` at `a = 0.001, 0.01, 0.3, 1.0`; `Y = −(−1)^{Σb}` on every `D_b` tested.] The time swap keeps the marginals (`ν_1 = ν_2`), the support (Theorem 7), the cost, invariance, and every box entropy (it is a bijection of each cell's pair alphabet). `O_1` is convex (E6), so the average of an optimizer and its swap is a swap-invariant optimizer.

*Line 72.* `P` is analytic in `(ε, μ)` on `Ω`. So the diagonal couplings off `Σπ` converge locally to the diagonal coupling at a point of `Σπ`. That coupling is not in `C_1` (Theorem 7). So no element of `O_1` there is their local limit.

### 4.E Section 5 (items 63-87)

*Theorem 9.* The coordinate sums of `x, x′, y` are `5, 3, 7`. Take `Γ = {|z − i| = 1}`. For small `|a|`, `σ(V(a))` lies within `‖V(a) − iR_o‖ = O(a)` of `{i, −i}`. With `R_0(z) = P_0/(z − i) + Q_0/(z + i)`, the residues inside `Γ` are `0` for `(z − i)^{−2}`, none for `(z + i)^{−2}`, and `1/(2i)` for `((z − i)(z + i))^{−1}`. So `P_1 = (P_0 V_1 Q_0 + Q_0 V_1 P_0)/(2i)` with `V_1 = R_o R_e`, and `P_0 R_o = P_0`, `Q_0 R_o = −Q_0` give `P_1 = (P_0 R_e Q_0 − Q_0 R_e P_0)/(2i)`. `R_e` joins `D_0` and `D_{e_1}` only by the four even edges `z ↔ z + e_1`, `z ∈ F_0 = {(2, s, t) : s, t ∈ {1, 2}}`, each with entry `1/√3`. With `(P_0)_{uv} = (δ_{uv} + r_{uv})/2` and `(Q_0)_{uv} = (δ_{uv} − r_{uv})/2`, one gets `(P_0)_{uz}(Q_0)_{z′w} − (Q_0)_{uz}(P_0)_{z′w} = (r_{uz} δ_{z′w} − δ_{uz} r_{z′w})/2`. Hence `(P_1)_{uw} = (4i√3)^{−1}[r_{u, w−e_1} 1(w − e_1 ∈ F_0) − r_{u+e_1, w} 1(u ∈ F_0)]`. For `(x, y)`: `r_{(2,1,2),(2,2,2)} = η_2(2,1,2)/√3 = (−1)²/√3` and `r_{(3,1,2),(3,2,2)} = (−1)³/√3`. So `(P_1)_{xy} = (4i√3)^{−1}(2/√3) = 1/(6i)`. `P_0`, `Q_0` and `R_e` are real, so `P̄(a) = P_0 − a P_1 + O(a²)` and `P̄_xy = −a/(6i) + O(a²) = ia/6 + O(a²)`. For `x′ = (1,1,1)`: `x′ ∉ F_0`, and `r_{(1,1,1),(2,2,2)} = 0` (opposite corners). [check: `P̄_xy/a = 0.16667i, 0.16666i, 0.16499i, 0.14682i` at `a = 0.001, 0.01, 0.3, 1.0`.] On the line `a_o = π/2`, `μ = π/2 − a` and `2ε = π/2 + a` lie in `(0, π)` for `|a| < π/2`, so the line lies in `Ω`.

*Theorem 10.* `Γ(−R_D) = (−1)^{N_D} Γ(R_D)`, and both commute with `N_D`. So `Ad Γ(−R_D)` and `Ad Γ(R_D)` agree on every element that commutes with `(−1)^{N_D}`, in particular on occupation projectors; this gives the second marginal through Theorem 8. At `a = 0`, `ψ = c†(φ_1)⋯c†(φ_4)|0⟩`, where `Φ = [φ_1 ⋯ φ_4]` is a real orthonormal basis of `{R_D = 1}`. Then `ψ_A = det Φ_{A,:}`, `ψ_A ψ_B = det(Φ_A Φ_B^T) = det(P_0)_{AB}`, and `Γ(R_D)ψ = det(Φ^T R_D Φ) ψ = ψ`. Each entry of `√3 R_AB` was re-derived from its edge, direction and sign `η_i`; the matrix of line 93 is right. In `√3 R_AB`, adding row 1 to row 3 leaves the permutation matrix of `(12)(34)`, of determinant `+1`; so `det R_AB = 1/9`. In `2(P_0)_AB`, expanding along column 3 (one entry `t`, in row 4, sign `−1`) and then along the remaining column 3 (one entry `t`) gives `−t · t · (1 − t²) = −2/9`; so `det(P_0)_AB = −1/72`. `A` and `B` each have two E-corners and two O-corners, as the swap requires. [check: `det R_AB = 0.111111`, `det(P_0)_AB = −0.0138889`, `q = −0.00154321`; over the `70²` four-particle pairs, 528 negative entries, minimum `−1/144`, negative mass `1.07407`, signed cost 8; both marginals of the one-cube form equal `ψ_S²` to `4e-17`.]

*Theorem 11.* `R_D² = I` and `tr R_D = 0`, so `R_D` has four eigenvalues `+1` and `P_0|_D` has rank four. `Γ(iR_D)ψ_D = i⁴ ψ_D = ψ_D`, so both laws are `⊗_D p`. `λ*` is B7's unique maximizer on the least-cost face of one cube. Equality in subadditivity holds only for independence, which gives the deficit `g/|B|` after tiling. `(P_0)_{EE} = I_4/2` because `R_D` vanishes on E-E pairs. The swap sends `E_D` only to `O_D`, and that pair is supported: `R_D² = I` gives `R_{EO} R_{OE} = I_4`, so `R_{OE}` is invertible. [check: `p(all-E) = 0.0625`.]

*Line 103.* Pass 1's reading of `LW1U_DRAFT.md` Theorem 4.3 holds. Lemma 4.0(i) needs `ρ_{ab} ≥ (1/8 − 2δ) I > 0`, that is `δ < 1/16`. Lemma 4.0(iii) gives `P_0 ≠ P_1` and `Q_0 ≠ Q_1` exactly when `δ sin 2α ≠ 0`. Lemma 4.2 and Steps 1-6 use `δ` only through these facts. At `δ = 0`, `ρ_{ab} = I/8` and `u (I/8) u* = I/8`, so the two Born laws are the same product, and `O_h` is the diagonal singleton (Theorem 3, `cos α ≠ 0`). Only the attribution in line 103 is wrong (item 87).

### 4.F Section 6 (items 88-96)

*Theorem 12.* `LW1_5_DRAFT.md` line 313 gives the tick ("Its one-body tick is `(W V W^*) ⊗ 1_5`"), and A2-5's proof gives the half-steps ("the free cube generators are `WR_TW^* ⊗ 1_5` for both tilings"). A block-diagonal covariance factorizes every Wick moment over flavours (`LW1_5_DRAFT.md` line 402). The principal minors of `WGW*` equal those of `G`, because `W` is diagonal and unitary. For the coarse support, `⟨σ| P_ξ Γ P_ξ |σ⟩ = ⟨σ|Γ|σ⟩ = ∏_j det u_{A_j A_j} ≠ 0`. On `Σπ` each flavour swaps its counts, so `N_E^{tot}(σ′) = N_O^{tot}(σ)`. Keeping the site-number pattern forces `N_E^{tot} = N_O^{tot}`; keeping the parity pattern forces `N_E^{tot} ≡ N_O^{tot}` modulo 2; either makes the total even. By flavour independence `E[(−1)^{N_D}] = E[(−1)^{N_D^{(1)}}]^5`, and Theorem 7's proof gives `|E[(−1)^{N_D^{(1)}}]| < 1`.

*Theorem 13.* With item 94's closure, `M_e` and `M_o` are products of commuting symmetric factors, hence symmetric. `U_0^T = M_e M_o = M_e U_0 M_e*`. For `ρ = f(U_0)` with `f` real, `M_e ρ M_e* = f(U_0^T) = ρ^T = ρ̄`, which has the same diagonal as `ρ`; and `M_o ρ̄ M_o* = U_0 ρ U_0* = ρ`. With `τ_E ≠ 0`, `M_e U_0 M_e* = M_e W_E M_o` and `U_0^T = M_e M_o W_E`, as line 115 says.

### 4.G Section 7 (items 97-101)

Each bullet restates a theorem above or reports a pass-1 check. The reports match `LW1U_SEA_DRAFT.md` lines 240, 259 and 303. The owner question cited in line 120 is `LW1U_DRAFT.md` line 361: "The owner decides whether the Qualification applies at every state or at the states the law reaches from its `omega_0`." Line 121's use of B8a matches `LW1.md` line 291: "Under the free tick and PS-3c, starting from the free sea, no record forms."

---

## 5. Required edits

These must change before the freeze. Each is one sentence or less; the replacement text is in section 2.
1. Line 9 (item 7): "The edge `(x, x+e_i)` carries the weight `η_i(x)/√3`, with `η_i(x) = (-1)^{Σ_{j<i} x_j}` as in `LW1.md` section 1."
2. Line 10 (item 8): name the angles `a_e = ε − μ/2` and `a_o = ε + μ/2`; keep `a = a_e` on `Σπ`.
3. Lines 68 and 70 (item 54): write `D_s` for the staggered sign, so `Y = D_s Z` and `D_s P̄ D_s = I − P`.
4. Line 84 (item 69): replace "Across the common face …" by the description of the unit face with corners `(2,1,2), (2,2,2), (3,2,2), (3,1,2)`.
5. Line 88 (item 73): "proposed" becomes "candidate" (twice); `⊗_D Ad Γ(R_D)` becomes `∏_D Ad Γ(R_D)`.
6. Line 103 (item 87): attribute the `δ`-family to `LW1U_SEA_DRAFT.md` §5.7's reading of the proof of `LW1U_DRAFT.md` Theorem 4.3, which is stated at `δ = 1/32`.
7. Line 107 (item 90): "`O_h` is the diagonal singleton off `Σπ`" in place of "the admissible transport is uniquely diagonal off `Σπ`".
8. Line 14 (item 13): add that the swapped field of `c′` has law `λ` under `ν_2`, by E4 and Theorem 7.
9. Line 37 (item 32): add that `ω_1` is cell-invariant, because cell translations are real and commute with `P`.
10. Line 41 (item 35): add that the torus spectrum lies in `σ(V)`, so the torus sea is defined and gapped.
11. Line 50 (item 38): add that the 24 rotations preserve `ν_P` and map even cubes to even cubes (A2, B10(3)).
12. Line 66 (item 53): add that `D_0` and `C_0` are fundamental domains of `2Z³`, so `d̄(π) ≥ ν_P(N_D odd)/4`.
13. Line 80 (item 66): add that the twelve rotations lie in `𝒢`, preserve `ν_1`, fix `D_0` and keep both classes; drop "Homogeneity and".
14. Lines 88-90 (item 74): add that `γ_+` commutes with cell translations and `ω_1` is cell-invariant.
15. Line 101 (item 83): add the conversion of `d̄` and `s` to odd cubes, and say that `N_D = 4` almost surely.
16. Line 109 (item 91): add `W_{x+2b} = (−1)^{Σ_i b_i} W_x`, so the five-mode `ω_1` is cell-invariant.
17. Lines 3 and 86 (the GAP): say "local-law condition (each cube's conditional law depends only on its own count pair)" in place of "homogeneous local-law condition", and replace "the stronger dependence claim remains open" by "the stronger dependence claim is not used and is dropped" (section 3).

Recommended, not required: the wording notes of section 2.3 for items 1, 6, 10, 14, 19, 21, 25, 27, 33, 42 and 85; and, for item 94, replacing "suppose the dressed half-step generators of LW1 are real symmetric" by the one-line fact that they are, which makes Theorem 13 unconditional for `τ_E = 0`.

## 6. Open statements to carry, by name

- **LW1-U_hop** (line 72). *For `(ε, μ) ∈ Σπ = {2ε + μ = π, 0 < μ < π/2}`, the set `O_1` at the odd half-tick (the pure hop `Γ(iR_o)` acting on `ω_P ∘ β_e`) has exactly one element.* Three distinct attacks failed, each at a named step. (1) Conditional representation given the finer shared field: (CL′) is false near the product point and off a discrete subset of `Σπ` (Theorem 9). (2) A coupling built from the state's cube-local symmetry: the Margenau-Hill form is not positive near the product point (Theorem 10). (3) Continuation from the solved product point: specific entropy is affine, odd sectors enter for every `a > 0`, and no uniform entropy deficit or contraction is available (Theorem 11, line 103). Known on `Σπ`: every admissible coupling moves the configuration (Theorem 7), and a swap-invariant optimizer exists (Theorem 8).
- **LW1-U_hop, five-mode form** (lines 107 and 119). The same question for the free sea of `L5-O` (site parities) and `L5-U` (site numbers), under PS-3h5. Known: every admissible odd-step coupling moves (Theorem 12). No attack on its uniqueness has been run.
- **LW1-U_f** (line 120). Uniqueness, with the torus clause, for invariant factor states other than the free sea. This file does not treat it. Its attacks are in `LW1U_DRAFT.md` section 10, which this report does not referee.

Not carried: the conditional dependence of `(D_0, D_{e_1})` given the shared field (section 3). Nothing uses it.

## 7. Freeze recommendation

`LW1U_SEA.md` can be frozen with its open statements named, after required edits 1-17. Every result it marks as proved was re-derived and holds. The seven ERRORs are three symbol clashes (lines 9, 10 and 68), one wrong description of a face (line 84), one word with two meanings (line 107), one reserved word (line 88) and one citation (line 103). The nine INCOMPLETE items are one-line steps, each closed in section 2.2. None of them changes a theorem. The distiller's GAP is real, and its repair is one sentence (section 3). After the edits, the frozen file proves LW1-U_sea at the even half-tick on the whole window `0 < μ < 2ε < π` and at the odd half-tick off `Σπ`. There the sea's selected transport is the diagonal coupling. The file also proves the torus clause for the torus seas. It names LW1-U_hop as the open remainder of LW1-U_sea.

---

## FINISH

**Proved here (referee closures; no new result of the part).**
- Closures of the nine INCOMPLETE items (section 2.2): `(CL) ⇒ (CL′)` in full on `Σπ`; cell invariance of `ω_1`, of the five-mode `ω_1` and of the form `q`; the torus spectrum lies in `σ(V)`; invariance of `ν_P` under the 24 rotations about `c_0` and of `ν_1` under the twelve parity-keeping rotations about the centre of `D_0`, with their count; `d̄` and `s` may be computed on odd cubes.
- Theorem 13 holds without its "suppose", for `τ_E = 0` on a finite even torus: the dressed generators are real symmetric in the occupation-link basis (section 2.3, item 94).
- The exact content of the GAP: Theorem 9 refutes "independence given the full shared field together with locality of each cube's conditional law"; homogeneity follows from locality and cell invariance and is not used (section 3).
- Re-derived and confirmed: Theorems 1-13 of `LW1U_SEA.md`, with the fixes of section 5.

**Counterexamples.** None to any statement of `LW1U_SEA.md`. Pass 1's sentence "The pair of cubes `(D_0, D_{e_1})` is not conditionally independent given the shared field" (`LW1U_SEA_DRAFT.md` line 305) is unproved, not refuted.

**Open, by name.**
- LW1-U_hop: three attacks failed, at (CL′) (Theorem 9), at positivity of the Margenau-Hill form (Theorem 10), and at a missing uniform estimate for continuation from the product point (Theorem 11, line 103).
- LW1-U_hop, five-mode form: no attack run.
- LW1-U_f, for invariant factor states other than the free sea: not treated in this file.

**What changes downstream.**
- LW1: after the edits and the freeze, an amendment can record that LW1-U_sea holds at `h = 0` on the whole window and at `h = 1` off `Σπ`, with the torus clause for torus seas, and that LW1-U_hop takes its place in the open list. Amendment 2's sentence on `LW1-U_sea` can then cite the frozen file.
- TM1 and VC1: off `Σπ` the free sea's PS-3 history is constant (Theorem 4), and no record forms there (B8a). This bears on TM1's open input TM1-i. It says nothing about the gauged vacuum.
- LW1-5: under PS-3h5, the row "LW1-U_f, LW1-U_sea, LW1-N | open" of `LW1_5_DRAFT.md` line 377 narrows for the free sea: `O_h` is the diagonal singleton off `Σπ`, for `L5-O` and for `L5-U`.
- VC1: with `τ_E = 0`, on a finite even torus, every density matrix that is a real function of `U_0` has the same joint law of occupations and link values at every half-tick (Theorem 13, unconditional by item 94's closure). Whether VC1's vacuum is such a function stays VC1's question.
- Owner: two facts, no proposal. PS-3's selection is discontinuous in the law's constants at `Σπ` (line 72). Off `Σπ`, at the free sea, the greatest-entropy stage is idle (line 43).
