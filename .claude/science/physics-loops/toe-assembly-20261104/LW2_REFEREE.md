lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# LW2 referee report (pass 3)

Written 2026-11-08 by a Claude Opus 5.5 headless lane on the Mac mini (model id `claude-opus-5-5`, max effort) as pass 3, the fresh-session referee, under PR #10138's method. This session wrote neither pass 1 (`LW2_DRAFT.md`, Claude) nor pass 2 (`LW2.md`, Codex `gpt-6.1-terra`). It is one check: one line-by-line read of `LW2.md`. It reviews no other review. It adopts no law, reading or axiom, and changes no working-set entry. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged.

**Text read.** `LW2.md` at commit `ecdf9708b` (the commit that last changed it; branch `claude/toe-assembly`, HEAD `ecdf9708b`). SHA-256 of the file read: `0720c03e368180e083425fc87407b463056e1a97d693cf0471b0056f7f60fed0`. Line numbers below are lines of that file. Its pass-1 source `LW2_DRAFT.md` has SHA-256 `72a6a98816c0df6e799bf3e655eb50ba1e774f9f955af1132093ff7f8a7ac8e8`, the hash `LW2.md` line 13 records.

**Sources read.** All at HEAD `ecdf9708b`, in this folder unless marked. The table of files, commits and line ranges is in section 9.

**Method.** Every proof was re-derived by hand. Each quotation that a step relies on was compared with its source by `grep -n` and a direct read. Verdicts: CORRECT; ERROR (a false or misquoted line, quoted, with a fix); INCOMPLETE (a named missing step). A "referee closure" is a short complete argument that supplies a missing step; it is new proof text and needs the lead's check like any other. A `[check]` is a tiny scratch computation in `/tmp/toe-LW2ref/`; it guides and never proves. No `[check]` was run for this report; every step below is by hand.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The laws and readings are read plainly. No hostile meaning is read into PS-5, PS-6, PS-6r, NN-a or ZM1-INV.

**Working-set entries used, by name.** PS-1 read by PS-1c (cell covariance), PS-5 (five modes per site), PS-6 and PS-6r (finite link registers with a frame group), NN-a (nearest-neighbour compilation), ZM1-INV (the invariant-only zoom), the four tests of `TOE_ASSEMBLY.md` section 3.2, and the two live laws `L5-U[m]` and `L5-O[S_+]` as candidates. The GB1 readings R-SUM and R-IA are used only as `GB1E.md` defines them.

---

## 1. Verdict table, part A (LW2 sections 0 to 4)

RC-x names a referee closure. RC-4.2, RC-7.1 and RC-I1g are in section 2; RC-T3b and RC-G3b in section 3; RC-G3c in section 4.

| # | Item (LW2 line) | Verdict | Note |
|---|---|---|---|
| 1 | §0 status paragraph (5) | CORRECT | |
| 2 | §0 "Proved subject to" list (7) | CORRECT | Each listed proof is written out below. |
| 3 | §0 GAP list (9) | CORRECT | Each GAP is ruled on in section 2: all four are real; each has a repair. |
| 4 | §0 Open by name (11) | CORRECT | RC-G3b, RC-G3c and RC-I1g would remove three names (section 7). |
| 5 | §0 provenance (13) | CORRECT | The recorded draft hash matches `LW2_DRAFT.md`. |
| 6 | §1 scope and prior work (17) | CORRECT | Every cited theorem exists with the stated content. |
| 7 | §1 digest paragraph (19) | CORRECT | |
| 8 | Definitions inferred by the distiller (23) | CORRECT | `ρ` is `KINV.md` line 31. |
| 9 | §2 tools paragraph (27) | CORRECT | |
| 10 | Setting S (29) | CORRECT | For `L5-U` the rishon link is "an ordinary tensor factor" because every register operator conserves rishon number and so is even. One sentence should say so. |
| 11 | Lemma T0 (31) | CORRECT | Density: `GB1Z2L5.md` line 33. |
| 12 | Lemma T1 (33-40) | CORRECT | Each `ψ_x` spans a graded line (even unitaries preserve parity), so it is homogeneous and the product state is well defined on the CAR algebra. |
| 13 | Cor T1.1(a) (43) | CORRECT | Same witness as `GB1Z2L5.md` lines 39-40 and `ZM1INV.md` R1 (line 58). The tilt replaces the directed-cycle step. |
| 14 | Cor T1.1(b) (44) | CORRECT | Agrees with `GB1Z2L5.md` line 49. |
| 15 | Cor T1.1(c) (45) | CORRECT | |
| 16 | Cor T1.1(d) (46) | INCOMPLETE | No functional is given. Fix: `λ_x = −1 + ε_R h(x)` on the U(1) weight. Matter weight `n ≥ 0` gives the maximizer `n = 0`; a positive link `(x,y)` carries end weights `∓E`, so `λ_x(−E) + λ_y(E) = ε_R E` has the unique maximizer `E = S`. This is the witness of `GB1Z2L5.md` line 87. |
| 17 | Lemma T2(a)-(c) (48-50) | CORRECT | |
| 18 | Cor T2.1 (52) | CORRECT | `XZ = −ZX` checked by hand. |
| 19 | Lemma T3(a) (54, 56) | CORRECT | Holds in every link-algebra convention that contains `U` and `e^{iθE}`. |
| 20 | Lemma T3(b) (54, 56) | INCOMPLETE | `b` multiplies by a discontinuous function of four links. It lies in `B(⊗_ℓ H_ℓ)`. Setting S builds region algebras from link algebras, and the C*-tensor product of the `B(H_ℓ)` is strictly smaller than `B(⊗H_ℓ)`; membership of `b` is not shown. RC-T3b proves the conclusion with polynomial multipliers only, in every convention. |
| 21 | Lemma T3(c) (54, 56) | CORRECT | |
| 22 | Remark T3.1 (58) | CORRECT | Add: under `K+C1` the dynamics still acts, by automorphisms (`Ad u` preserves `K+C1`), though `U_ℓ` and `e^{iθE}` are not elements. |
| 23 | Lemma T4 and its instances (60-62) | CORRECT | (CP) gives each property `LZ1.md` line 40 lists; D1 invariance follows from gauge invariance (`LZ1.md` line 42). For `L5-O` the implementer has site factor `−iP_x` and end factors whose product is `−1` on `S_+` (`GB1Z2L5.md` line 77). |
| 24 | §4.0 reading of the table (68) | CORRECT | |
| 25 | Table row 1 (72) | CORRECT | |
| 26 | Table row 2 (73) | CORRECT | V2b needs RC-T3b for SU(2). |
| 27 | Table row 3 (74) | CORRECT | |
| 28 | Table row 4 (75) | CORRECT | V4c says GAP 4.2; RC-4.2 now proves it for generic angles. |
| 29 | Table row 5 (76) | CORRECT | RC-G3b and RC-G3c extend the V5b outcome. |
| 30 | Table row 6 (77) | CORRECT | |
| 31 | Table row 7 (78) | ERROR | "V7a: (CP) fails" holds for the reading `K_z = SU(5)` at every `κ`. The table should add that the gate breaks U(1) only when `sin(120κ) ≠ 0` (GAP 7.1, RC-7.1). |
| 32 | Table row 8 (79) | CORRECT | |
| 33 | §4.1 "What the proof uses" (83) | CORRECT | Quotes match `ZM1I1A.md` lines 25, 32, 38, 48, 50. |
| 34 | Prop 1.1 (85-87) | CORRECT | For U(1), each eigenvalue of `E` has multiplicity one; the essential-spectrum count is still right (rational case: infinite multiplicity of `e^{iθn}`; irrational: the whole circle). |
| 35 | Prop 1.2 (89-91) | CORRECT | With coarse `L5-U[m₁]` the contradiction holds even at `L = 1`, as the text says. |
| 36 | §4.2 "What the proof uses" (95) | CORRECT | Quotes match `GB1Z2L5.md` lines 43, 47, 61. |
| 37 | Prop 2.1 (97-99) | CORRECT | `GB1QL.md` lines 89, 91. |
| 38 | Prop 2.2 (101) | CORRECT | For SU(2), given RC-T3b. |
| 39 | Prop 2.3 (103-105) | CORRECT | "Three of the four cases" matches `GB1Z2L5.md` line 95. At `m = 5` the pairs `(∅, full)` and `(full, ∅)` share a `T′`-weight, but their value `0` lies below the maximum `2c_1 + 2c_2 + c_3 > 0`. The last sentence can be shortened: the `T′`-fixed algebra has a character, and a smaller algebra inherits it by restriction. |
| 40 | §4.3 "What the proof uses" (109) | CORRECT | `KINV.md` lines 29-39. |
| 41 | Prop 3.2 (111-113) | ERROR | The mathematics is right. The text says the `KINV.md` line 49 sentence is "quoted in section 1"; LW2 section 1 does not quote it (the draft did, `LW2_DRAFT.md` line 83). Fix: quote it here: "Theorem 2 also supplies no odd-fine-`m` result: the same end exchange precludes a reversal-invariant character there." |
| 42 | Prop 3.3 (115-117) | CORRECT | `V L_h V^{-1} = R_h` checked. |
| 43 | Prop 3.4 (119) | CORRECT | |
| 44 | Prop 3.5 (121) | CORRECT | |
| 45 | §4.4 "What the proof uses" (125) | CORRECT | `GB1ISO.md` lines 38-40, 72, 74. |
| 46 | Def 4.1 (127) | INCOMPLETE | The gate is not specified on pairs of unequal isotypic types `λ ≠ λ′` of the two stars. `GA1_5.md` line 172: "act as identity on unequal types or unmatched sectors". Add that clause (here and in text C1′). |
| 47 | Def 4.1 properties (i)-(iv) (129) | CORRECT | With item 46's clause. (ii): the block projections commute and the two gates act on different end factors of a shared link. |
| 48 | Prop 4.1 (131-133) | CORRECT | Here `𝒞` is the cubes with equal-parity base (`GB1ISO.md` line 30); each site is a corner of one even and one odd cube. |
| 49 | Remark after Prop 4.1 (135) | CORRECT | |
| 50 | GAP 4.2 (137-139) | CORRECT | The gap is real. RC-4.2 repairs it (section 2). |
| 51 | §4.5 "What the proofs use" (143) | CORRECT | `GB1E.md` lines 103-105, 186, 192, 196; `GB1QL.md` line 310; `GA2_Y2.md` line 43. |
| 52 | Prop 5.1 (145) | CORRECT | |
| 53 | §4.5 closing paragraph (147) | CORRECT | `GA2_Y2.md` line 49. |
| 54 | §4.6 "What the proofs use" (151) | CORRECT | `RCSPC.md` line 168; `RCSPO.md` line 62. |
| 55 | Prop 6.1 (153) | CORRECT | |
| 56 | Prop 6.2 (155) | CORRECT | The hypothesis `ω(B*B) > 0` is not used. |
| 57 | §4.7 "What the proof uses" (159) | CORRECT | `LZ1.md` line 62. |
| 58 | Prop 7.1 (161-163) | CORRECT | (a) is a statement about `D_ℓ` and holds. (b) and (c) hold for the reading `K_z = SU(5)`. The added GAP 7.1 is real; see section 2. |
| 59 | §4.7 paragraph (165) | CORRECT | |
| 60 | Prop 7.2 (167-169) | CORRECT | "Spectators do not hop" (`GB1QL.md` line 92); no other gate acts on them. |
| 61 | §4.8 "What the proofs use" (173) | ERROR | The #10027 quotation is at `TOE_ASSEMBLY.md` line 129, not line 132 (line 132 is the PS-6 heading). The other quotations match `LW1_5.md` line 11, `CG16D.md` line 7, `CG16S.md` line 7, `RCSP16.md` line 7, `CG16B.md` line 39. |
| 62 | Prop 8.1 (175) | CORRECT | Class 𝓛 asks only for "a finite Hilbert space" per link (`CG16B.md` line 23); `RCSPO.md` line 38 says "For any finite Spin(20) link representations". |
| 63 | §4.9 parity of `m` (179) | CORRECT | |
| 64 | Prop 4.9 (181) | CORRECT | `N + 6(min(m,N) − max(0,m−N))` gives `ZM1I1A.md`'s `11` at `N = 5`, `m ∈ {1, 9}` (line 46). The closing remarks match `ZM1I1A.md` line 56 and `CG16K.md` line 39. |

## 1. Verdict table, part B (LW2 sections 5 to 8)

| # | Item (LW2 line) | Verdict | Note |
|---|---|---|---|
| 65 | Def 5.1 (187) | CORRECT | Matches `GB1QL.md` lines 88-93. The matter angles are `a_e = ε − μ/2`, `a_o = ε + μ/2`, `0 ≤ μ < 2ε < π` (line 92). |
| 66 | "What `L[s]` meets" (189) | CORRECT | `GB1QL.md` line 299 (a), (c). |
| 67 | Def 5.2 (193) | CORRECT | |
| 68 | Def 5.2 checks (195) | CORRECT | |
| 69 | Theorem G2 (197-199) | CORRECT | Greedy filling of the per-colour totals is unique because the `c_j` strictly decrease; at the maximum every colour is full or empty at each end, so each weight space is one Slater vector. |
| 70 | §5.2 closing paragraph (201) | CORRECT | |
| 71 | (P1) (205) | INCOMPLETE | The content is right, but the quotation "uniform in ambient volume and `n≤T`" comes from the digest (`prior/LW2.md` line 33), not from `GB1QL.md`. Quote the source: `GB1QL.md` line 299, "So Theorem 4.8 and Corollaries 4.9-4.10 hold for `L5[SU(2), s]` on states with empty matter", and the rate `ε_n` of line 231. |
| 72 | G3 preamble and (a) statement (207-208) | CORRECT | |
| 73 | G3(b) statement (209) | CORRECT | It is a statement about the compressed transfer. The distiller's caveat is right; RC-G3b proves the same conclusion for R-IA itself. |
| 74 | G3(c) statement (210) | CORRECT (superseded) | "Not decided" was accurate for pass 1. RC-G3c proves (c), box-independently. |
| 75 | Proof of G3(a) (212) | CORRECT | Strict positivity `m_t > 0` is `GB1ISO.md` Theorem 2.2 (line 50). `GB1E.md` Theorem 2.2 gives only "nonnegative ... positive near the identity" (line 52). Cite the first only. |
| 76 | Lemma G3.1 (214) | CORRECT | `1 + Σc(k_i) ≥ (1+|k⃗|)²/(4n)` checked; the sum is finite for `r > 3n/4`. |
| 77 | Proof of G3(b) (216) | CORRECT | `κ_min` agrees with `GB1ISO.md` line 60. |
| 78 | G3(c), attacks A1-A3 (218) | CORRECT | Each attack fails at the stated step, and the three are distinct. None of them uses the cube factorization of `T_ex` (`GB1ISO.md` line 41) or a flux-graded estimate; RC-G3c does. |
| 79 | Theorem G4 (220-222) | CORRECT | With item 46's clause. `(U*AU − 𝕍*A𝕍)P_0 = 0` checked: the matter gates fix empty matter and `𝕍*A𝕍` commutes with `P_0`. Spectator excitations make `H_phys` larger than the link span, but G4 does not claim the span. |
| 80 | Theorem G5 (224-226) | CORRECT | `SGAP.md` line 64. The SGAP model has no link term at `t = 0` (`SGAP0.md` item 1: "electric coupling zero"); charge and light number act on matter. |
| 81 | Theorem G1 (230-232) | CORRECT | The neighbour covariance is positive here (negative for U); the adjacency step needs only "nonzero versus zero", and disjoint representatives exclude equality. `(1 + cos(θ/2))/2` and `f_1(θ) = cos(θ/2)` checked. |
| 82 | §5.4 summary (234-240) | ERROR | Line 235, "it fails only at `s = ∞`", is false as a general statement: Prop 1.2's finite variant `L5-U[•]` already loses the adjacency step. Fix: "for these two families it fails only at `s = ∞`". Line 239, "Theorem 8.1's negativity ... fails at large `s`": Theorem 8.1's step threshold depends on `s`, so it does not reach a fixed step (as §8 line 297 says). Reword, and add RC-G3b, RC-G3c to row 5. |
| 83 | §6.1 three readings (246) | CORRECT | |
| 84 | Theorem I1 preamble and GAP I1(g) (250) | CORRECT | The gap is real. RC-I1g repairs it (section 2). (CP) itself needs no caveat: chain gates are gauge invariant, so they commute with each `c_z`. |
| 85 | I1(a) (251) | CORRECT | |
| 86 | I1(b) (252) | CORRECT | Needs `0 < m < 10s`, which Def 5.2 gives. |
| 87 | I1(c) (253) | CORRECT | The `2s | m` witness is the analogue of a locked witness (`KINV.md` line 20); `KINV.md` Theorem 2 uses it only through lift invariance. |
| 88 | I1(d) (254) | CORRECT | |
| 89 | I1(e) (255) | CORRECT | |
| 90 | I1(f) (256) | CORRECT | |
| 91 | I1(g) (257) | INCOMPLETE | True without chain moves (Theorem I2). With chain moves it is RC-I1g, with a changed generator `a`. |
| 92 | Proof of I1 (259) | CORRECT | The end-flavour sharpening `χ(p_{ℓ,X}) ∈ sZ` checked. |
| 93 | Theorem I2 (261-263) | CORRECT | Matches the four steps of Proposition S-odd (`GA1_5_REFEREE.md` lines 236-249). `dim Λ^p(C⁵⊗C^s) = C(5s,p) ≥ 5`. |
| 94 | §6.3 (267) | ERROR | "and only when `s ∤ m`" is wrong for row 3. By I1(c), the fine-character step of K-INV has no instance whenever `2s ∤ m`, which includes `s | m` with `m/s` odd (for example `s = 2`, `m = 2`). Fix: "row 2 when `s ∤ m`; row 3's first step when `2s ∤ m`". |
| 95 | §6.4 (271-272) | CORRECT | The q-deformation citation is context only; LW2 line 13 records that it was not fetched. |
| 96 | §7 four-test preamble (276) | CORRECT | Quotes match `TOE_ASSEMBLY.md` lines 173-176; test 2 is cut before "to get a result". |
| 97 | C1 (278) | CORRECT | Grades match `GB1QL.md` line 353. |
| 98 | C1′ (280) | INCOMPLETE | The text inherits item 46's missing clause. Grades: agreed (section 5). |
| 99 | C2 (282) | CORRECT | Grades agreed. |
| 100 | C3 (284) | INCOMPLETE | A candidate text should not point to a GAP. Replace the last sentence by "with a free real constant `κ`, `sin(120κ) ≠ 0`" (RC-7.1). Grades agreed. |
| 101 | C4 (286) | CORRECT (grade change advised) | Given RC-G3b, test 4 should read F; see section 5. |
| 102 | C5 (288) | CORRECT | Grades agreed. Given RC-T3b, the C5a claim for SU(2) holds in every convention that contains the link multipliers. |
| 103 | C6 (290) | CORRECT | Grades agreed. |
| 104 | "What the grades say" (292) | CORRECT | |
| 105 | §8 (297) | CORRECT | |

**Counts.** 105 items: 93 CORRECT (item 74 is superseded by RC-G3c; item 101 carries an advised grade change), 5 ERROR (items 31, 41, 61, 82, 94) and 7 INCOMPLETE (items 16, 20, 46, 71, 91, 98, 100). The four distiller GAPs are recorded correctly (items 50, 58, 73, 84) and are ruled on in section 2. No ERROR changes the content of a theorem. Item 20 (Lemma T3(b)) is the only proof step whose argument does not go through as written; RC-T3b replaces it.

---

## 2. The distiller's four GAPs: rulings and repairs

**GAP 4.2 (generic support spreading with matter). Real.** The pass-1 proof treats the hop's link matrices as commuting numbers. In the Heisenberg picture `e^{iaH_C}d^†e^{−iaH_C}` is not a one-body combination of the `d^†`: its second-order term contains `[H_C, U_ℓ]`, and the entries of `U_s` do not commute. The step "the next layer spreads the operator into a second cube" is also not proved. The repair below works with vectors, where the one-particle sector is exact.

**RC-4.2 (referee closure).** Take `L[s]` with any `s ≥ 1`, `θ`, `τ_E`. Fix a site `x`. Along `e_1` the cubes `C_o(x)` and `C_e(x)` extend in opposite directions. Let `y₀ = x + δe_1 ∈ C_o(x)` and `z₀ = x − δe_1 ∈ C_e(x)`, `δ = ±1`. There are a countable set `Z_o` and, for each `a_o ∉ Z_o`, a countable set `Z(a_o)`, such that for `a_o ∉ Z_o` and `a_e ∉ Z(a_o)` the operator `X = U^*d^†_{x,4}U` lies in the algebra of no unit cube (its matter and links). In particular no single cube of either tiling supports it.

*Proof.* (1) *Test vector.* Let `φ` be a product link vector with the links of `(x,y₀)` and `(x,z₀)` in `H_0`, and `Φ = |vac⟩⊗φ`. If `X` lies in the algebra of a unit cube `C`, then `XΦ ∈ span{c^†_{w,j}|vac⟩ : w ∈ C}⊗(links)`: `X` is a sum of monomials in the modes of `C` times link operators, and a monomial with an annihilator kills `|vac⟩`.
(2) *Computing `XΦ`.* Each matter gate fixes empty matter (`GB1QL.md` line 301, proof of (d)). So `UΦ = |vac⟩⊗W_BW_Eφ` and `XΦ = M_e^*M_o^*(c^†_{x,4}|vac⟩⊗φ)`. The tick conserves matter number, and spectators never move (`GB1QL.md` line 92). On the one-particle sector a cube gate acts exactly as `e^{iah_C}`, `h_C = 3^{−1/2}Σ_{ℓ⊂C}η(|y⟩⟨x|⊗U_ℓ + h.c.)`, an operator on `C⁸⊗C²⊗(links)` whose entries are link operators. The eight corners of `C_o(x)` lie in eight distinct even cubes, so `C_e(w)` meets `C_o(x)` only in `w`. Writing `XΦ = Σ_w|w⟩⊗ψ_w` and `φ_4 = u_4⊗φ`:
`ψ_{y₀} = [e^{ia_eh_{C_e(y₀)}}]_{y₀y₀}[e^{ia_oh_{C_o(x)}}]_{y₀x}φ_4`, `ψ_{z₀} = [e^{ia_eh_{C_e(x)}}]_{z₀x}[e^{ia_oh_{C_o(x)}}]_{xx}φ_4`.
Both are entire in `(a_e, a_o)`.
(3) *Nonvanishing.* At `a_e = 0`, `ψ_{y₀} = [e^{ia_oh}]_{y₀x}φ_4`. Its `a_o`-derivative at `0` is `±i3^{−1/2}` times a column of `U_s` or `U_s^*` applied to `φ`; it is nonzero, because on `H_0` one has `P_μ = x^+_μY_s` with `y_0 = 1`, which sends the constant to `x_μ` (`GB1QL.md` lines 55-57). A nonzero vector-valued entire function of one variable has countably many zeros. So `ψ_{y₀}(0,a_o) ≠ 0` for `a_o` off a countable set `Z′`, and for such `a_o` the map `a_e ↦ ψ_{y₀}(a_e,a_o)` vanishes on a countable set. The `a_e`-derivative of `ψ_{z₀}` at `a_e = 0` is `i[h_{C_e(x)}]_{z₀x}[e^{ia_oh}]_{xx}φ_4`; at `a_o = 0` it is again a nonzero column applied to `φ`. So it is nonzero for `a_o` off a countable set `Z″`, and then `a_e ↦ ψ_{z₀}` vanishes on a countable set. Put `Z_o = Z′ ∪ Z″`.
(4) No unit cube contains both `y₀` and `z₀`; they differ by `2e_1`. By (1), `X` lies in no cube algebra. □

In the parameters `a_e = ε − μ/2`, `a_o = ε + μ/2` the exceptional set is Lebesgue-null in the allowed region. As LW2 says, this is a remark about the state class: `GB1ISO.md` states its results for empty matter.

**GAP 7.1 (determinant coupling and exceptional angles). Real.** On `Λ⁵(C⁵_x⊕C⁵_y)`, `D_ℓ = 120ε|f_x⟩⟨f_y|`, with `f_y` the state with all five rishons at `y`, `f_x` the state with all five at `x`, and `|ε| = 1`. So `D_ℓ + D_ℓ^*` has eigenvalues `±120` on `span{f_x, f_y}` and `0` elsewhere, and, with `P` the projection onto that span,
`e^{−iκ(D_ℓ+D_ℓ^*)} = 1 + (cos(120κ) − 1)P − i sin(120κ)(D_ℓ + D_ℓ^*)/120`.
At `κ = π/120` this is `1 − 2P`, which commutes with the end numbers, as the distiller says.

**RC-7.1 (referee closure).** Let `g ∈ U(5)` act at one site `x` only, with `det g = e^{iα}`. Conjugation multiplies `D_ℓ` by `e^{±iα}` (Prop 7.1(a), proof) and fixes `P`. So the gate commutes with `g` if and only if `sin(120κ)(e^{iα} − 1) = 0`. Hence, if `sin(120κ) ≠ 0`, the elements of `U(5)_x` that commute with every gate of `L5-U^{det}` are exactly those of `SU(5)_x`; if `sin(120κ) = 0`, `W_D` commutes with all of `U(5)`. Prop 7.1(b) and (c) are statements about the reading `K_z = SU(5)` and hold for every `κ`. Whether some unitary outside the `U(5)` action commutes with every gate is not needed for (b)-(c) and is not decided here. *Repaired statement:* in Prop 7.1, table row 7 and text C3, replace "`κ ∈ R∖{0}`" by "`κ ∈ R` with `sin(120κ) ≠ 0`".

**GAP I1(g) (the band with chain moves). Real.** Theorem I2's proof transports `A_v = 1⊗a` through the swap layer only. A chain layer acts on the multiplicity spaces of each star and can change `a`.

**RC-I1g (referee closure).** Let the chain-augmented law add one layer `W_ch = ∏_{(ℓ,z)}V_{ℓ,z}` over link ends. Each `V_{ℓ,z}` acts on the end factor at `(ℓ,z)`, commutes with the colour `U(5)` there and with the end number, and is the same operator at every end (as cell covariance requires); `exp(−iγΣ_jΣ_a(r^†_{j,a}r_{j,a+1} + h.c.))` is one such. Then Theorem I2 holds for the augmented tick, with the same state and the same fibre `e^{−iK·(1,1,1)}`. The generators are `A_v(a)`, where `a` is traceless on `M_{λ₀}`, `tr a^*a = d`, and `a` commutes with the operator `c` by which `W_ch` acts on `M_{λ₀}`.

*Proof.* (1) On `star(v)` the layer acts as `⊗_{ends}V`, which commutes with the diagonal `U(5)_v`; by Schur's lemma it is `⊕_λ 1_{V_λ}⊗c_λ`. Put `c = c_{λ₀}`. It preserves `σ^→`. (2) Such an `a` exists. If `c` is scalar, any traceless `a` serves. Otherwise take the spectral projections `P_1, P_2` of `c` for two distinct eigenvalues and scale `P_1/tr P_1 − P_2/tr P_2`. (3) The state of Theorem I2 is, on each star, the normalized projection onto the `λ₀` summand; `1⊗c` fixes it. The layer is link-only, so `GA1_5.md` Theorem 6.1's reduction (line 158) holds with `𝕍` the product of the link layers in tick order. (4) `Ad W_ch` sends `A_v(a)` to `A_v(c^*ac) = A_v(a)`; its factors at other stars act on other end factors and preserve the sector, so they commute with `A_v(a)`. The identification `τ_t` maps the ends of `star(v)` to those of `star(a(v))` with orientation kept, so it intertwines the layer on the two stars, and the swap carries `A_v(a)` to `A_{v′}(a)` with the same `a`. (5) The rest of Theorem I2's proof is unchanged: the `u_b = π(A_{2b}(a))Ω` are orthonormal and `Ũu_b = u_{b−(1,1,1)}`. □ Each chain gate acts on one link end, so its NN-a compilation is immediate.

**GAP G3(b) (compressed transfer versus R-IA). Real, as an identification.** The plain finite-register reading of R-IA continues the symmetric layers of the quantum-link tick `U_(s)` (`GB1E.md` line 97 and Theorem 4.1, line 86; `GB1QL.md` line 70). It gives `T^{IA}_s = ⊗_C e^{βB^s_C/4}e^{−tA_C}e^{βB^s_C/4}`, where `B^s_C` is built from the so(5) link `U_s` (`GB1QL.md` line 58). G3(b)'s `Π T_{loc,C} Π` is a different operator. Even at `s = 1`, where `ιU_1ι^* = ΠUΠ` on each link (`GB1QL.md` Remark 4.4), the two differ at second order in `β` by terms such as `Π B_C Q B_C Π`, with `Q` the projection onto flux above `s`; this is nonzero because `B_C` maps flux `s` to flux `s+1`. For `s ≥ 2` the coefficients `y_k ≠ 1` (line 56) also enter. So G3(b) is a statement about a new construction, as the distiller says.

**RC-G3b (referee closure; proof in section 3).** For every `t > 0` and `β ∈ R` there is `s₀(t,β)`, independent of the box, such that for `s ≥ s₀` the embedded kernel of `T^{IA}_s` is, cube by cube, at least `(1/2)e^{−12|β|}m_t^{12} > 0`. The kernels converge uniformly to those of `⊗_C T_{loc,C}`. So the lifts are gauge-invariant probability measures and converge in total variation to `μ_loc[β,t]`. The conclusion of G3(b) therefore holds for R-IA itself.

---

## 3. Referee closures RC-T3b and RC-G3b

These are new proof text by this referee. Each needs the lead's check like any other step. No `[check]` was run for them.

**RC-T3b (Lemma T3(b) in every convention).** Let each link of `Z³` carry `L²(SU(2))` with the gauge action `U ↦ h_yUh_x^{-1}`, with any matter. Suppose each link algebra contains the multiplication operators by the matrix entries of `U_ℓ` and the parity `a_ℓ = (−1)^{k_ℓ}`, `(a_ℓf)(U) = f(U with U_ℓ ↦ −U_ℓ)`. Then `𝔄^G` has no character.

*Proof.* Let `ℓ₀ = (x₀, x₀+e_1)` and let `p_1,…,p_4` be the four plaquettes that contain `ℓ₀`. Let `X_i` be the holonomy of `p_i` based at `x₀`. Distinct `p_i` share only `ℓ₀`, so there is a link `ℓ_i ∈ p_i` in no other `p_j`. Identify `SU(2)` with the unit quaternions in `R⁴`; then `(1/2)tr(XY^{-1}) = ⟨X,Y⟩`. Put `v_0 = 1`, `v_i = X_i`, and `g_{ab} = ⟨v_a,v_b⟩`. Each `g_{ab}` is a polynomial in the link entries (on `SU(2)`, `conj U_{11} = U_{22}` and `conj U_{12} = −U_{21}`). So its multiplication operator lies in the algebraic tensor product of the link algebras. It is gauge invariant, because a gauge transformation conjugates every `X_i` by the same `h_{x₀}`. Five vectors in `R⁴` are linearly dependent, so `det[g_{ab}]_{a,b=0}^{4} = 0` as a function and hence as an operator. Each `a_ℓ` is gauge invariant, because `−1` is central. Conjugation by `a_{ℓ_i}` replaces `X_i` by `−X_i` and fixes the other `X_j`. So it negates `g_{0i}` and every `g_{ij}` with `j ≠ i`. Let `χ` be a character. Then `χ(a_{ℓ_i})² = 1`, so `χ(g_{0i}) = −χ(g_{0i}) = 0` and `χ(g_{ij}) = 0` for `i ≠ j`, while `χ(g_{aa}) = 1`. Multiplicativity gives `0 = χ(det[g]) = det[χ(g_{ab})] = det I_5 = 1`, a contradiction. □

The proof uses only polynomial multipliers and single-link operators. So it holds whether a region algebra is the C*-tensor product of its link algebras or the full `B(⊗H_ℓ)`. The `K + C1` convention of Remark T3.1 contains neither the multipliers nor `a_ℓ`, as LW2 already says.

### 3.1 One-cube facts used by RC-G3b and RC-G3c

Both transfers factor over the cubes of the tiling. For the infinite register this is `GB1ISO.md` Theorem 2.1, line 41: "`T_ex=⊗_C e^{−a₀(τ_EA_C+θB_C)}`". For the quantum-link register the same holds, because each `B^s_C` acts on the twelve links of `C` and terms of different cubes commute. So we work on one cube, with `𝒦 = L²(SU(2))^{⊗12}`.

- (F1) *Flux.* `𝒦 = ⊕_{k⃗}⊗_ℓH_{k_ℓ}`, `k⃗ ∈ N^{12}`, with projections `Π_{k⃗}`. Put `P_{≤L} = Σ_{max k⃗ ≤ L}Π_{k⃗}`, `Q_L = 1 − P_{≤L−1}`, and `Π = P_{≤s}`, so `R := R_s^{⊗12} = ran Π`. `A = Σ_ℓE²_ℓ` equals `Σ_ℓc(k_ℓ)`, `c(k) = k(k+2)/4`, on `ran Π_{k⃗}`; on `ran Q_L`, `A ≥ c(L)`.
- (F2) *Two potentials.* `B = B_C` is multiplication by a real function with `|B| ≤ 24` (`GB1ISO.md` line 60). `B̃ = ιB^s_Cι^*` satisfies `B̃ = ΠB̃Π` and `‖B̃‖ ≤ 24`, by `‖U_s‖ ≤ 1` (`GB1QL.md` Proposition 4.2(d), line 147). Both change each link's flux by at most one, since `x_μ = x^+_μ + x^-_μ` and `P_μ = x^+_μY_s + Y_sx^-_μ` shift the degree by `±1` (`GB1QL.md` lines 55-57) and a plaquette uses each of its links once. Hence `P_{≤L−1}X = P_{≤L−1}XP_{≤L}` and `Q_{L+1}X = Q_{L+1}XQ_L` for `X ∈ {B, B̃}`.
- (F3) *Low-flux comparison* (`GB1QL.md` Lemma 4.7, line 219). For `v ∈ ran P_{≤M}` with `M ≤ s`, `‖(B̃ − B)v‖ ≤ 96δ_s(M)‖v‖`, `δ_s(M) = 2M(M+3)/(s(s+3))`.
- (F4) *Weighted norm.* Put `w(k⃗) = ∏_ℓ(k_ℓ+1)` and `|||y||| = Σ_{k⃗}w(k⃗)‖Π_{k⃗}y‖`. LW2's Lemma G3.1 gives `‖Π_{k⃗}y‖_∞ ≤ w(k⃗)‖Π_{k⃗}y‖`; so `|||y||| < ∞` gives a continuous representative with `‖y‖_∞ ≤ |||y|||`. By Cauchy–Schwarz, `|||P_{≤L}y||| ≤ d_L^6‖y‖` with `d_L = Σ_{k≤L}(k+1)²`. Heat factors contract `|||·|||`. For `X ∈ {B, B̃}`, `|||Xy||| ≤ c|||y|||` with `c = 24·6^{12}`: each `k⃗` has at most `3^{12}` neighbours `k⃗′`, and `w(k⃗) ≤ 2^{12}w(k⃗′)`.
- (F5) *Smoothing.* `|||e^{−uτA}y||| ≤ k_{2uτ}(e)^6‖y‖`, since `Σ_k(k+1)²e^{−2uτc(k)} = k_{2uτ}(e)` (`z_k(e) = (k+1)²`, `GB1E.md` line 54). Also `k_t(e) ≤ C₀(1 + t^{−3/2})` for an absolute `C₀`.
- (F6) *Reproducing vectors.* For `U ∈ SU(2)^{12}`, `e_U(W) = ∏_ℓΣ_{k≤s}z_k(W_ℓU_ℓ^{-1})` lies in `R`, `⟨e_U, f⟩ = f(U)` for `f ∈ R`, and `‖P_{≤L}e_U‖ = d_L^6` for `L ≤ s`. The embedded kernel of an operator `Y` on `R` is `⟨e_U, Ye_V⟩` (`GB1E.md` line 54: `Z_k` is the kernel of `Π_k`).
- (F7) *Targets.* `κ ≥ e^{−12|β|}m_t^{12}` and the exact R-SUM cube kernel is at least `e^{−24a₀|θ|}m_{a₀τ_E}^{12}` (`GB1ISO.md` line 60), with `m_t > 0` (`GB1ISO.md` Theorem 2.2).

### 3.2 Proof of RC-G3b (R-IA)

Let `S = e^{βB̃/4}` on `R` and `b = 6|β|`. The R-IA cube kernel is `K^{IA}_s(U,V) = ⟨e_U, Se^{−tA}Se_V⟩ = ⟨e^{−tA/2}Se_U, e^{−tA/2}Se_V⟩`.

1. *Telescoping.* With `w_U = (B̃ − B(U))e_U`, `(B̃^n − B(U)^n)e_U = Σ_{i=1}^{n}B(U)^{n−i}B̃^{i−1}w_U`, because `B(U)` is a scalar.
2. *Low flux.* For `1 ≤ M ≤ s`, `P_{≤M−1}(B − B(U))e_U = 0`. Indeed, for `f ∈ ran P_{≤M−1}`, (F2) puts `(B − B(U))f` in `ran P_{≤M} ⊆ R`, so `⟨f,(B − B(U))e_U⟩ = conj(((B − B(U))f)(U)) = 0` by (F6). Hence `P_{≤M−1}w_U = P_{≤M−1}(B̃ − B)P_{≤M}e_U`, and (F3), (F6) give `‖P_{≤M−1}w_U‖ ≤ 96δ_s(M)d_M^6`. Also `‖w_U‖ ≤ 48d_s^6`.
3. *High flux.* `(1 − P_{≤M−1})w_U ∈ ran Q_M`, and `B̃^{i−1}` maps `ran Q_M` into `ran Q_{M−i+1}` (F2). So for `i ≤ M`, `‖e^{−tA/2}B̃^{i−1}(1 − P_{≤M−1})w_U‖ ≤ e^{−(t/2)c(M−i+1)}24^{i−1}·48d_s^6`.
4. *Sum.* Let `r_U = e^{−tA/2}(S − e^{βB(U)/4})e_U = Σ_{n≥1}((β/4)^n/n!)e^{−tA/2}(B̃^n − B(U)^n)e_U`. Steps 1-3, with `i ≤ M/2` and `i > M/2` treated apart, give
 `‖r_U‖ ≤ (be^b/24)[96δ_s(M)d_M^6 + 48d_s^6e^{−(t/2)c(M/2)}] + 2d_s^6Σ_{n>M/2}nb^n/n!`.
 Take `M = ⌊s^{1/20}⌋`. Then `δ_s(M)d_M^6 ≤ 2(M+3)²(M+1)^{18}/s² → 0`; `d_s^6 ≤ (s+1)^{18}` while `c(M/2) ≥ M²/16`, so the second term tends to `0`; and `(M/2)!` outgrows every power of `s`, so the third does too. Hence `sup_U‖r_U‖ → 0`.
5. *Kernel.* Put `a_U = e^{βB(U)/4}e^{−tA/2}e_U`. Then `K^{IA}_s(U,V) = ⟨a_U + r_U, a_V + r_V⟩`, `‖a_U‖ ≤ e^{6|β|}k_t(e)^6`, and `⟨a_U, a_V⟩ = e^{β(B(U)+B(V))/4}∏_ℓK^{(t)}_s(U_ℓV_ℓ^{-1})` with `K^{(t)}_s = Σ_{k≤s}e^{−tc(k)}z_k`. G3(a)'s proof gives `sup|K^{(t)}_s − k_t| ≤ r_s(t) → 0`. So `sup_{U,V}|K^{IA}_s − κ| → 0`, and by (F7) `K^{IA}_s ≥ (1/2)e^{−12|β|}m_t^{12}` for `s ≥ s₀(t,β)`. Every bound is per cube, so `s₀` does not depend on the box. `T^{IA}_s` is positive definite and gauge invariant; the lift statements follow as in G3(a). □

## 4. Referee closure RC-G3c: G3(c) holds (R-SUM, `θ ≠ 0`)

**RC-G3c.** Fix `a₀ > 0`, `τ = τ_E > 0` and `θ ∈ R`. There is `s₀(a₀,τ,θ)`, independent of the box, such that for `s ≥ s₀` the embedded kernel of the R-SUM finite-register transfer `e^{−a₀H_s}` is strictly positive. Cube by cube it converges uniformly to the kernel of `e^{−a₀H}`. So the lifts are gauge-invariant probability measures and converge in total variation to the exact lift.

*Setting.* One cube, with the facts (F1)-(F7) of section 3.1. Put `H = τA + θB` on `𝒦`, `H_s = τA + θB̃` on `R`, and `Ĥ = τA + θB̃` on `𝒦`. Since `B̃ = ΠB̃Π`, `Ĥ = H_s ⊕ τA` on `R ⊕ R^⊥`. So the kernel of `e^{−a₀Ĥ}` is `K_s + h_s`, where `K_s` is the kernel of `e^{−a₀H_s}` and `h_s` is the kernel of `e^{−a₀τA}(1 − Π)`. Telescoping the twelve link factors gives `sup|h_s| ≤ 12r_s(a₀τ)k_{a₀τ}(e)^{11} → 0`, with `r_s` as in G3(a). Let `K` be the kernel of `e^{−a₀H}`.

*Step 1 (Dyson bounds).* Let `X ∈ {B, B̃}` and `G = τA + θX`. The Dyson series `e^{−wG} = Σ_n(−θ)^n∫_{Δ_n(w)}e^{−u_0τA}Xe^{−u_1τA}⋯Xe^{−u_nτA}du` converges in norm; `Δ_n(w)` has volume `w^n/n!`. Three bounds follow, for `0 < w ≤ a₀`, with constants independent of `s`.
- (a) `|||e^{−wG}y||| ≤ e^{c|θ|w}|||y|||`, by (F4) term by term.
- (b) *Smoothing.* `|||e^{−wG}f||| ≤ S(w)‖f‖` with `S(w) = Σ_n((c|θ|w)^n/n!)C₀^6(1 + ((n+1)/(τw))^{3/2})^6 < ∞`. On the part of `Δ_n(w)` where `u_i` is the largest coordinate, `u_i ≥ w/(n+1)`. Bound the factors left of `e^{−u_iτA}` in `|||·|||`, that factor by (F5) with half its time, and the factors to its right in `L²`.
- (c) *Damping.* For `L ≥ 2`, `|||Q_Le^{−wG}f||| ≤ η_w(L)‖f‖` with `η_w(L) = e^{−(τw/2)c(L/2)}S(w) + Σ_{n≥L/2}((c|θ|w)^n/n!)C₀^6(1 + ((n+1)/(τw))^{3/2})^6`. By (F2), `Q_L` passes through the term as `e^{−u_0τA}Q_LXQ_{L−1}e^{−u_1τA}Q_{L−1}X⋯`, so for `n < L/2` every heat factor acts on `ran Q_{L/2}` and damps by `e^{−u_jτc(L/2)}`. Half of the largest factor smooths and the rest damps, which gives the first term. For `n ≥ L/2` use (b). `η_w(L) → 0` as `L → ∞`, uniformly for `w ∈ [a₀/4, a₀/2]`.

*Step 2 (kernel vectors).* By (b) and (F4), `f ↦ (e^{−wG}f)(U)` is a bounded functional of norm at most `S(w)`. Let `F_w(U)` (for `G = Ĥ`) and `G_w(U)` (for `G = H`) be its Riesz vectors, so `(e^{−wĤ}f)(U) = ⟨F_w(U), f⟩`. Then `F_w(U) = e^{−(w/2)Ĥ}F_{w/2}(U)`, `‖F_w(U)‖ ≤ S(w)`, and the kernel of `e^{−wĤ}` is `⟨F_{w/2}(U), F_{w/2}(V)⟩`. By (a) and (F4), `‖P_{≤L}F_w(U)‖ = sup{|(e^{−wĤ}f)(U)| : f ∈ ran P_{≤L}, ‖f‖ = 1} ≤ e^{c|θ|w}d_L^6`. By (c), `|||Q_LF_w(U)||| ≤ η_{w/2}(L)S(w/2)`. The same holds for `G_w`.

*Step 3 (Duhamel).* `e^{−a₀Ĥ} − e^{−a₀H} = θ∫_0^{a₀}e^{−(a₀−u)Ĥ}(B̃ − B)e^{−uH}du`. Applied to `f ∈ 𝒦`, the integrand has finite sup norm, integrable in `u`: on `[0,a₀/2]` use (b) for `e^{−(a₀−u)Ĥ}`; on `[a₀/2,a₀]` use (a) for `e^{−(a₀−u)Ĥ}` and (b) for `e^{−uH}`. Test the operator identity against trigonometric polynomials `f, g`. The kernel of `e^{−(a₀−u)Ĥ}(B̃ − B)e^{−uH}` is `⟨F_{a₀−u}(U),(B̃ − B)G_u(V)⟩`, which Step 4 bounds uniformly in `u, U, V` for each `s`, so Fubini applies. Both sides are continuous kernels, so they agree everywhere, and the kernel difference is
`D(U,V) = θ∫_0^{a₀}⟨F_{a₀−u}(U), (B̃ − B)G_u(V)⟩du`.

*Step 4 (estimate).* Fix `1 ≤ M ≤ s` and split `G_u(V) = P_{≤M}G_u(V) + Q_{M+1}G_u(V)`.
- (i) Low flux. By (F2), `|⟨F_{a₀−u}(U),(B̃ − B)P_{≤M}G_u(V)⟩| = |⟨P_{≤M+1}F_{a₀−u}(U),(B̃ − B)P_{≤M}G_u(V)⟩|`, and by (F3) and Step 2 this is at most `96δ_s(M)e^{2c|θ|a₀}d_{M+1}^{12}`.
- (ii) High flux, `u ≥ a₀/2`. The term is `(e^{−(a₀−u)Ĥ}y)(U)` with `y = (B̃ − B)Q_{M+1}G_u(V)`. By (a), (F4) and Step 2 it is at most `2ce^{c|θ|a₀}η_{u/2}(M+1)S(u/2)`.
- (iii) High flux, `u < a₀/2`. Since `B̃ − B` is self-adjoint, (F2) rewrites the term as `⟨Q_{M+1}(B̃ − B)Q_MF_{a₀−u}(U), G_u(V)⟩`, the conjugate of `(e^{−uH}y′)(V)` with `y′ = Q_{M+1}(B̃ − B)Q_MF_{a₀−u}(U)`. It is at most `2ce^{c|θ|a₀}η_{(a₀−u)/2}(M)S((a₀−u)/2)`.
In (ii) and (iii) the time arguments lie in `[a₀/4, a₀/2]`. So
`sup_{U,V}|D| ≤ |θ|a₀[96δ_s(M)e^{2c|θ|a₀}d_{M+1}^{12} + 2ce^{c|θ|a₀}sup_{w∈[a₀/4,a₀/2]}η_w(M)S(w)]`.
Take `M = ⌊s^{1/40}⌋`. Then `δ_s(M)d_{M+1}^{12} ≤ 2(M+3)²(M+2)^{36}/s² → 0`, and the second term tends to `0` by Step 1(c).

*Step 5 (conclusion).* `K_s = K + D − h_s → K` uniformly. By (F7), `K ≥ e^{−24a₀|θ|}m_{a₀τ}^{12} > 0`, so `K_s ≥ (1/2)e^{−24a₀|θ|}m_{a₀τ}^{12}` for `s ≥ s₀(a₀,τ,θ)`. The full kernel is a product of cube kernels, and gauge projection averages positive kernels, so positivity and `s₀` do not depend on the box. The lift statements follow as in G3(a). □

**How RC-G3c relates to A1-A3.** The three attacks fail as LW2 states them. RC-G3c uses two steps that none of them uses. (1) The R-SUM transfer factors over cubes (`GB1ISO.md` line 41), so the problem is one fixed cube and box-independence is automatic. (2) The finite-register potential is compared with the multiplication operator only at low flux (F3), where they agree up to `δ_s(M)`. High flux is damped by the heat factor and measured in the weighted norm `|||·|||`, which controls sup norms. This answers A2's obstacle: no sup bound on the kernel of `B̃` is needed. It does not contradict `GB1E.md` Theorem 8.1: `s₀` grows without bound as `a₀ → 0`. It also does not contradict `GB1E.md` line 206 ("It does not prove that the fixed-register kernels are probability measures"); that line describes Theorem 8.3, and RC-G3c is a separate argument.

---

## 5. Decisions on the questions named in the brief

**The extremal-witness criterion T0-T1.** Correct (items 11-15). The criterion needs only a torus, real functionals with unique maximizers, and one-dimensional maximal weight spaces; Lemma T0 makes every local invariant commute with the tilted functional, so it fixes the witness line. T1.1(a)-(c) are correct; T1.1(d) lacks its functional (item 16, repaired there).

**The three exclusions.** (1) *Two gauge-singlet modes* (T2.1): correct; two singlet CAR modes give an anticommuting pair of invariant symmetries. (2) *Flavour algebras with `s ∤ n`* (T2(c), G2): correct; the commutator forces equal integer values on the `F_{aa}`, so `s` divides `n`. (3) *Kogut–Susskind links* (T3): (a) U(1) is correct in every convention containing `U` and `e^{iθE}`; (b) SU(2) is correct in conclusion, but its proof uses a discontinuous multiplier that the region algebras of Setting S need not contain; RC-T3b proves it with polynomial multipliers in every convention; (c) is correct.

**T4, the centre-parity hypothesis.** Correct. (CP) supplies exactly the properties `LZ1.md` §1 uses (line 40): pairwise commuting involutive adjoint actions, translation covariance, commutation with every gauge-invariant gate, and products equal to matter parity on local operators. A D1 state is invariant because local gauge invariance implies it (line 42). The `L5-O` instance uses the torus rotation by `π`, not `−1`; `GB1Z2L5.md` line 77 gives its site factor `−iP_x` and the scalar `−1` on `S_+`.

**The feature table, row by row.** Each variant breaks the named step, except where the table says the negative persists.
- Row 1: V1a breaks trace transfer (no tracial state on `B(H)`); V1c breaks the adjacency step (zero covariances); growth keeps it (G1). Correct.
- Row 2: V2a, V2b, V2c remove the character, so Theorem 4's proof has no input; V2d keeps it (Prop 2.3); growth with a full-rank torus keeps it. Correct; V2b for SU(2) rests on RC-T3b.
- Row 3: V3a removes the `ρ`-fixed fine character; V3b removes the fixed end sum; V3c removes the fine character. Correct. K-INV itself is not decided in any variant, as LW2 says.
- Row 4: V4d breaks factorization at every `θ` and the support statement at `θ = 0`. Correct. V4c is GAP 4.2; RC-4.2 proves that one tick spreads `d^†` beyond any cube for generic matter angles. V4a belongs to LW2M.
- Row 5: V5b: G3(a), G3(b), and with RC-G3b and RC-G3c also R-IA and R-SUM at every `θ`; V5c breaks Theorem 5.1's infinite-rank step; V5d is ported; V5e changes the law with `s`. Correct.
- Row 6: V6b breaks Lemma 5's emptied level; rishon-type growth keeps it. Correct.
- Row 7: V7a breaks (CP) for the reading `K_z = SU(5)`; the gate breaks U(1) only when `sin(120κ) ≠ 0` (item 31, RC-7.1). V7b ported; V7c and growth keep (CP). Correct with that condition.
- Row 8: ported; growth changes no hypothesis. Correct.

**G1.** Correct at every finite `s, s₁` (item 81). **G2.** Correct, including the sharpening `χ(p_{ℓ,X}) ∈ sZ` (items 69, 92). **G3.** (a) correct, box-independent; (b) correct for the compressed transfer; RC-G3b gives the same for R-IA itself; (c) the three attacks fail as stated and are distinct, and RC-G3c proves (c), box-independently. **G4.** Correct for every `s` once Definition 4.1 has its unequal-type clause. **G5.** Correct; the SGAP0 gap is the same for every finite register with a two-valued `X_ℓ`.

**I1 and I2.** Correct, with three repairs: I1(g) with chain moves needs RC-I1g; §6.3's "only when `s ∤ m`" must read "`2s ∤ m`" for row 3 (item 94); I1(d) needs no caveat.

**The four distiller GAPs.** All four are real. 4.2: repaired (RC-4.2). 7.1: repaired by the condition `sin(120κ) ≠ 0` (RC-7.1). I1(g): repaired (RC-I1g). G3(b): the identification is false in general, and RC-G3b proves the conclusion for R-IA directly.

**Four-test grades of the six texts.** I agree with every grade except one.
- C1 (`L[s]`): 1 C, 2 P, 3 P, 4 C. Agree.
- C1′ (swap variant): 1 P, 2 P, 3 C, 4 C. Agree, once the text has the unequal-type clause.
- C2 (`LU[s,m]`): 1 C, 2 P, 3 C, 4 C. Agree.
- C3 (`L5-U^{det}`): 1 P, 2 P, 3 C, 4 C. Agree, once the text states `sin(120κ) ≠ 0` instead of pointing to a GAP.
- C4 (compressed reading): 1 C, 2 P, 3 P, 4 C as written. If RC-G3b is accepted, test 4 should be F: the text's own reason, a positive finite-register Euclidean transfer, is met by R-IA itself, so the compression is structure that reason does not need.
- C5 (infinite register): 1 F, 2 P, 3 F, 4 C. Agree.
- C6 (`L5-U[•]`): 1 P, 2 P, 3 C, 4 C. Agree.

**Four-test note on this report.** This report proposes no new law, reading or definition. RC-G3b uses R-IA exactly as `GB1E.md` line 97 states it, applied to the quantum-link tick of `GB1QL.md` line 70; R-IA keeps its recorded grades (P C C C). The chain-layer conditions in RC-I1g are hypotheses of a closure, not a proposed law text.

---

## 6. Required edits to `LW2.md`

Each edit names the table item it repairs. E1-E17 are text repairs. E18-E21 import referee closures; the lead decides whether to accept each closure before importing it.

- **E1** (item 10). Setting S: add "For `L5-U` and `LU[s,m]` the rishon register is an ordinary tensor factor because every register operator conserves rishon number and is even."
- **E2** (item 16). T1.1(d): give the functional `λ_x = −1 + ε_R h(x)` and the maximizers `n = 0`, `E_ℓ = S` on positive links.
- **E3** (item 20). Lemma T3(b): replace the proof by RC-T3b, or state that region algebras are `B(⊗_{ℓ∈R}H_ℓ)` and keep the given proof under that convention. Prop 2.2, row 2 and C5 then cite RC-T3b.
- **E4** (item 22). Remark T3.1: add that under `K + C1` the dynamics acts by automorphisms although `U_ℓ`, `e^{iθE}` are not elements.
- **E5** (items 31, 58, 100). Prop 7.1, table row 7 and text C3: replace "`κ ∈ R∖{0}`" by "`κ ∈ R` with `sin(120κ) ≠ 0`". Replace GAP 7.1 by RC-7.1, keeping its last sentence that (b) and (c) hold for the reading `K_z = SU(5)` at every `κ`.
- **E6** (item 41). Prop 3.2: quote `KINV.md` line 49 in place, since section 1 does not quote it.
- **E7** (items 46, 98). Definition 4.1 and text C1′: add "and acts as the identity on pairs of unequal isotypic types" (as `GA1_5.md` line 172).
- **E8** (items 28, 50). Replace GAP 4.2 by RC-4.2. Row 4, V4c: "one tick carries `d^†` off every single cube for generic matter angles (RC-4.2)".
- **E9** (item 61). §4.8: "`TOE_ASSEMBLY.md` line 132" becomes "line 129".
- **E10** (item 71). (P1): quote `GB1QL.md` line 299 (Prop 4.11(d)) and the rate of line 231, not the digest.
- **E11** (item 75). Proof of G3(a): cite `GB1ISO.md` Theorem 2.2 alone for `m_t > 0`.
- **E12** (item 82). §5.4: line 235 becomes "for these two families it fails only at `s = ∞`"; line 239 becomes "`GB1E.md` Theorem 8.1's threshold depends on `s`, so its negativity does not reach a fixed step at large `s`".
- **E13** (item 94). §6.3: "only when `s ∤ m`" becomes "row 2 when `s ∤ m`, and row 3's first step when `2s ∤ m`".
- **E14** (item 84). Theorem I1 preamble: drop the parity caveat; chain gates are gauge invariant, so (CP) holds with them.
- **E15** (item 101). C4: if E19 is accepted, grade test 4 F, with the reason given in section 5.
- **E16** (items 3, 4). §0: update the GAP and Open lists to match E5, E8, E17-E21.
- **E17** (item 39, optional). Prop 2.3: end the proof with "A closed subgroup containing `T′` has a smaller fixed algebra, which inherits the character by restriction."
- **E18** (items 84, 91). Replace GAP I1(g) by RC-I1g; I1(g) then reads "holds for every `s` and `m`, with or without chain moves of the stated kind; with chain moves the generator `a` must commute with the chain unitary on `M_{λ₀}`".
- **E19** (items 73, 101). Keep G3(b) as a statement about the compressed transfer. Add RC-G3b as G3(b′), the same conclusion for R-IA itself. Replace the GAP G3(b) caveat by the ruling of section 2.
- **E20** (items 74, 78). Replace G3(c) "Not decided" by RC-G3c. Keep A1-A3 as a record of failed steps, with the note of section 4 on what RC-G3c adds.
- **E21** (items 29, 82). Table row 5 and §5.4: V5b becomes "positive kernels at fixed step for `s ≥ s₀`, box-independent, for R-SUM at every `θ` and for R-IA (G3, RC-G3b, RC-G3c)".

---

## 7. Open statements to carry by name

These stay open after the edits of section 6. "Open" means not decided by `LW2.md` or this report; it is not a claim either way.

1. **LW2-ODD-DET.** Does `L5-U^{det}` with `sin(120κ) ≠ 0` have a propagating odd band in some D1 state?
2. **LW2-DET-MAX** (named here). Does any unitary outside the `U(5)` action commute with every gate of `L5-U^{det}`? Prop 7.1(b)-(c) do not need the answer.
3. **LW2-QDEF.** q-deformed registers; they need a new reading of PS-6.
4. **D-theory proper** (reading (iii) of §6.1).
5. **K-INV-E and the row-3 map questions.** Existence of the K-INV map in variants V3a-V3c, with coarse `R_{s₁}`-type or `L5-U[•]` registers, and with fine `LU[s,m]`, `2s ∤ m`.
6. **GB1-Z2 readouts for characterless variants.** For `L[s]`, the Standard-Model `SU(2)` readings, `LU[s,m]` with `s ∤ m`, and Kogut–Susskind links, the conclusion of `GB1Z2L5.md` Theorem 4 is not decided by characters.
7. **LW2-TR•** (named here). With fine and coarse `L5-U[•]`, does any argument other than adjacency exclude `L ≥ 2` (Prop 1.2, first case)?
8. **LW2-CL-KS** (named here). Does the U(1) Kogut–Susskind variant of row 6 have a Clifford node (Prop 6.1)?
9. **ISO-FP, GB1-CF, LW2-M**, and the isotropy of `L^{sw}[s]` at `θ ≠ 0` (LW2 line 135).
10. **GB1E-RP[s]** (named here). Reflection positivity of the finite-register lifts of G3(a), G3(b), RC-G3b and RC-G3c. None of them is checked for it; `T0-start` needs it.
11. **Volume-uniform finite-register estimates.** G3, RC-G3b and RC-G3c are fixed box, fixed `N_t`, then `s → ∞`; only `s₀` is box-independent. This is part of T0-rate.
12. **The `GB1QL.md` list, unchanged:** GB1-QL[matter], GB1-QL[`L5-O`], GB1-QL[U(2)], E-1, E-2, E-3, GB1-SC, VC1, T0-start[SU(2)], T0-rate, T0-QLR[SU(2)], Y2-W.

**Names that leave the list if the lead accepts the closures.** GB1E-POS[θ≠0] (RC-G3c). The chain-augmented neutral band (RC-I1g). The finite-register R-IA identification: the identification is false in general (section 2), and its purpose is met by RC-G3b.

## 8. Prior work used

Each item was read at the commit listed in section 9.

- `prior/LW2.md` (digest), lines 1-104: the map of on-file results and failed routes.
- `GB1Z2L5.md`: Theorem 1 (line 33), Theorem 2 and its witnesses (37-49), Theorem 4 (59-61), Theorem 6 and its `L5-O` implementer (75-77), Theorem 7 (85-87), the open cases (95).
- `ZM1INV.md`: Theorem 2.1 (44), R1 (58-66).
- `KINV.md`: definition 4 (20), Theorems 1-2 (29-39), line 49.
- `ZM1I1A.md`: Theorems 1-3 and the load statement (25-50); Theorem 4's arithmetic (52-58).
- `LZ1.md`: §1 centre implementers, D1 states and bands (36-44); Theorems 2.1-2.2 (52-66).
- `GA1_5.md`: Theorems 6.1-6.3 and the odd-`m` remark (150-182); `GA1_5_REFEREE.md` Proposition S-odd (232-249).
- `GB1QL.md`: §1.2 the register and `U_s` (50-60); §1.3 the ticks (70); §1.5 the test law (84-93); Proposition 4.2(d) (147); Lemma 4.3 (161-165); Lemma 4.7 (211-219); Theorem 4.8 (229-233); Proposition 4.11 (299-301); R-QL5 (353).
- `GB1E.md`: §1 kernels (31); Theorem 2.2 (52-54); Theorem 4.1 (86-88); readings R-SUM and R-IA (96-97); Theorems 5.1 (103-105), 8.1 (186-188), 8.2 (192), 8.3 and scope (198-206).
- `GB1ISO.md`: tiling (30); Theorems 2.1 (38-41), 2.2 (50-56), 2.3 (58-60), 3.1 (72-74).
- `SGAP.md` Theorem 4 (64-70); `SGAP0.md` items 1-5 (11-15) and Theorem 9 (150-156).
- `RCSPC.md` Lemma 5 (168); `RCSPO.md` Theorems 1 (38) and 3.2 (62).
- `CG16B.md` class 𝓛 (23) and Theorem 2.2 (39); `CG16D.md` (7) and Lemma N (71); `CG16S.md` (7); `RCSP16.md` (7); `CG16K.md` Theorem 2.3 (39).
- `LW1_5.md` (11, 102); `LIT_QLM.md` (23, 45, 117); `GA2_Y2.md` (43, 49); `TOE_ASSEMBLY.md` (129, 171-178, 310-323).

**Prior work the digest missed or did not connect.** (1) `GB1QL.md` Lemma 4.7's plaquette comparison, `‖(B̃_C − B_C)v‖ ≤ 96δ_s(M)‖v‖` at flux `M ≤ s`; it is load-bearing for RC-G3b and RC-G3c. (2) `GB1ISO.md` Theorem 2.1's factorization of the exact R-SUM transfer (line 41); the digest records the factorization (its line 39) but not that it makes G3(c) a one-cube problem. (3) `GB1ISO.md` Theorem 2.3's two-sided kernel bounds (line 60). (4) `GB1Z2L5.md` line 77, the `L5-O` centre implementer used by Lemma T4. (5) `GA1_5.md` line 172, the unequal-type clause that Definition 4.1 omits.

## 9. Sources read

Checkout `/Users/jonBridger/toe-worker/repo`, branch `claude/toe-assembly`, HEAD `ecdf9708b`. No other branch was needed. Files in this folder, with the commit that last changed each:

| File | Last changed | Lines read |
|---|---|---|
| `LW2.md` | `ecdf9708b` | 1-297 (all) |
| `LW2_DRAFT.md` | `a6291aad1` | 1-40, 83, and grep hits (202, 297, 305-307, 344-387) |
| `prior/LW2.md` | `0ec9a2b33` | 1-104 (all) |
| `LW1_REFEREE.md` | `5a2a0affe` | 1-80 (format) |
| `Y2W_DRAFT.md` | `92e03055c` | 1-16 (head format) |
| `TOE_ASSEMBLY.md` | `15d00adcf` | 129-132, 171-178, 207, 310-323 |
| `GB1Z2L5.md` | `3de4558ac` | 33-95 |
| `ZM1INV.md` | `fb9508e83` | 44, 58, 66, 84, 88-102 (grep hits) |
| `KINV.md` | `fb9508e83` | 20, 29-53 |
| `ZM1I1A.md` | `59cdde899` | 21-60 |
| `LZ1.md` | `5e228c059` | 14-68 |
| `GA1_5.md` | `913ef70a5` | 150-182, grep hits |
| `GA1_5_REFEREE.md` | `8d0d4b4db` | 232-249 |
| `GB1QL.md` | `03b159959` | 50-60, 70, 84-93, 147, 161-165, 211-233, 299-301, 310, 353 |
| `GB1E.md` | `4f59990a4` | 31, 52-54, 86-97, 103-107, 186-206 |
| `GB1ISO.md` | `f6412654f` | 30, 38-41, 50-60, 72-74, grep hits |
| `SGAP.md`, `SGAP0.md` | `fb9508e83`, `fb9508e83` | `SGAP.md` 19-21 and 64-70 (definitions, Theorem 4), with grep hits; `SGAP0.md` 11-15, 26, 102, 108, 150-156 |
| `RCSPC.md`, `RCSPO.md` | `e06ecdf43`, `f36736dae` | `RCSPC.md` 168; `RCSPO.md` 38, 62 |
| `CG16B.md`, `CG16D.md`, `CG16S.md`, `CG16K.md`, `RCSP16.md` | `8a2bedb83`, `662bf5107`, `ea997b5c8`, `4d1379fd8`, `3631210a2` | the quoted lines (7, 23, 39, 71) |
| `LW1_5.md`, `LIT_QLM.md`, `GA2_Y2.md` | `4d1379fd8`, `5d1409d92`, `2ca9262f0` | the quoted lines (11, 102; 23, 45, 117; 43, 49) |

---

## 10. Freeze recommendation

Freeze `LW2.md` after the text edits E1-E17 are applied. They change no theorem's content. Import E18-E21 only after the lead checks RC-I1g, RC-G3b and RC-G3c; check RC-T3b, RC-4.2 and RC-7.1 before E3, E5 and E8 use them. If the lead does not accept RC-G3b or RC-G3c, keep G3(b) and G3(c) as `LW2.md` states them, with A1-A3, and keep GB1E-POS[θ≠0] and the finite-register R-IA question open; the rest of the freeze is unaffected. Nothing in `LW2.md` adopts a law, a reading or an axiom, and this report adopts nothing.

---

## FINISH

**Proved** (in `LW2.md`, checked here). Lemmas T0, T1, T2, T3(a), T3(c), T4; Corollaries T1.1(a)-(c) and T2.1; Propositions 1.1, 1.2, 2.1, 2.3, 3.2-3.5, 4.1, 4.9, 5.1, 6.1, 6.2, 7.1 (U(1) breaking of the gate needs `sin(120κ) ≠ 0`), 7.2, 8.1; Theorems G1, G2, G3(a), G3(b) for the compressed transfer, G4 (with Definition 4.1's unequal-type clause), G5, I1(a)-(f), I1(g) without chain moves, I2.

**Proved here as referee closures** (new text; each needs the lead's check).
- RC-T3b: with `L²(SU(2))` links, `𝔄^G` has no character in every region-algebra convention that contains the link multipliers and `(−1)^{k_ℓ}`.
- RC-4.2: in `L[s]`, for `a_o` off a countable set and then `a_e` off a countable set, one tick carries `d^†_{x,4}` to an operator in no unit cube's algebra.
- RC-7.1: the elements of `U(5)_x` commuting with the determinant gate are exactly `SU(5)_x` when `sin(120κ) ≠ 0`, and all of `U(5)_x` when `sin(120κ) = 0`.
- RC-I1g: GA1-5's neutral band survives chain moves of the stated kind, with a generator commuting with the chain unitary.
- RC-G3b: the finite-register R-IA transfer of the cube-face SU(2) family has a strictly positive kernel for `s ≥ s₀(t,β)`, box-independent, converging uniformly to the infinite-register local kernel.
- RC-G3c: the same for the R-SUM transfer at every `θ`, `s ≥ s₀(a₀,τ_E,θ)`; this proves G3(c).

**Counterexamples.** `s = 2`, `m = 2` refutes §6.3's "only when `s ∤ m`" for row 3. `L5-U[•]` refutes line 235's unrestricted "fails only at `s = ∞`". `κ = π/120` makes the determinant gate U(1)-symmetric (the distiller's example, confirmed). The identification of G3(b)'s compressed transfer with finite-register R-IA is false in general (section 2).

**Open by name.** LW2-ODD-DET; LW2-DET-MAX; LW2-QDEF; D-theory proper; K-INV-E and the row-3 map questions; GB1-Z2 readouts for characterless variants; LW2-TR•; LW2-CL-KS; ISO-FP, GB1-CF and LW2-M, with the isotropy of `L^{sw}[s]` at `θ ≠ 0`; GB1E-RP[s]; volume-uniform finite-register estimates; and the `GB1QL.md` list (GB1-QL[matter], GB1-QL[`L5-O`], GB1-QL[U(2)], E-1, E-2, E-3, GB1-SC, VC1, T0-start[SU(2)], T0-rate, T0-QLR[SU(2)], Y2-W). If RC-G3c, RC-G3b and RC-I1g are accepted, GB1E-POS[θ≠0], the finite-register R-IA identification and the chain-augmented band leave the list.

**What changes downstream.**
- W1, GB1 and the YM T0 interface: if RC-G3b and RC-G3c are accepted, both finite-register Euclidean transfers of the cube-face SU(2) family, R-SUM at every `θ` and R-IA, are gauge-invariant probability kernels at fixed step for `s ≥ s₀`, with `s₀` independent of the box. Row 5's negative is then a small-step effect only (`GB1E.md` Theorem 8.1). Reflection positivity (GB1E-RP[s]) and volume-uniform estimates remain open.
- GB1-Z2 and ZM1-INV readouts: the character obstruction is escaped only by gauge-singlet spectators, the Standard-Model SU(2) readings, Kogut–Susskind links (any convention, RC-T3b), or flavour registers with `s ∤ m`; K-INV's fine-character step fails when `2s ∤ m`.
- GB1ISO's empty-matter factorization does not extend to the matter sector at generic angles (RC-4.2).
- LZ1 and CG16: the determinant variant escapes (CP) for the reading `K_z = SU(5)` at every `κ`; its gate breaks U(1) only when `sin(120κ) ≠ 0`.
- Text C4 should be withdrawn or graded F on test 4 if RC-G3b is accepted.
