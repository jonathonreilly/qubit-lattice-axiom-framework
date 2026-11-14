lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# CG16-K referee report (pass 3)

Written 2026-11-07 by a Claude Opus 5.5 headless lane on the Mac mini (model id `claude-opus-5-5`, max effort), as pass 3 (the referee) of part CG16-K under the method of open PR #10138: Claude drafts at length, Codex distils, a fresh session referees, then the owner freezes. This session wrote neither pass 1 (`CG16K_DRAFT.md`) nor pass 2 (`CG16K.md`). This is one check: one line-by-line read of `CG16K.md`. No review of this review was commissioned, and no other review was read.

**Text read.** `CG16K.md` as of commit `c82ee8663` (the last commit that touches it; branch `claude/toe-assembly` head). SHA-256 of the file read: `81d22728dc7645745b2efe99e613fd45f6ae4cd9490a572066f19593107da39b`. Line numbers below refer to that file.

**References consulted.** `CG16K_DRAFT.md` at `31ef08a1e` (SHA-256 `ada9d2dd...3545cb`); `prior/CG16K.md` at `15bc39079` (SHA-256 `ca1b0016...b69`); the other sources, with commits and lines, are in the section "Sources read" near the end. Other reviews of CG16K were not read.

**Method.** Every proof step was re-derived by hand. A `[check]` is a tiny scratch computation in `/tmp/toe-CG16Kref/` (under a minute, a few MB). It guides or refutes and never proves. Verdicts: CORRECT; ERROR (a false line, quoted, with a fix or counterexample); INCOMPLETE (a named missing step). A "referee closure" is a short complete argument for a missing step. Owner guidance applied: "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". Premises are read plainly. Nothing here adopts a law, a reading or a definition.

**Working-set entries used, by name.** PS-1c (`TOE_ASSEMBLY.md` line 180; `LW1_5.md` line 60). GA1-P-NN = NN-a, the owner text (`TOE_ASSEMBLY.md` line 235). PS-5, only as the comparison case. PS-6 and PS-6r (finite link registers), through the two five-mode laws `L5-U[m]` and `L5-O[S_+]` of `LW1_5.md`, both live by owner choice. ZM1-I1[a], only for one scope remark. No axiom or working-set entry is changed; `docs/MINIMAL_AXIOMS_2026-06-29.md` was not touched.

---

**Counts.** 55 items: 45 CORRECT, 4 ERROR, 6 INCOMPLETE. No ERROR or INCOMPLETE item changes the content of a theorem of `CG16K.md`. One referee closure (R1) turns the distiller's "does not follow" into a counterexample.

## 1. Verdict table

| # | Item (CG16K.md line) | Verdict | Note |
|---|---|---|---|
| 1 | §0 status (5) | CORRECT | |
| 2 | §0 "Proved here" list (7) | CORRECT | The `SO(10)`/`Spin(10)` sentence is right (R2). |
| 3 | §0 GAP paragraph (9) | ERROR | The `k_eff` GAP is real and the bound is false (R1). But "cites a generator-level result" misreads R; see item 23. |
| 4 | §0 open names (11) | CORRECT | Two unnamed opens should get names (§5). |
| 5 | §0 provenance (13) | CORRECT | Source `7086189d1` matches the note's branch head. |
| 6 | Def. 1, groups (17) | CORRECT | |
| 7 | Def. 2, modes and supports (18) | CORRECT | |
| 8 | Def. 3, neighbourhoods, canonical (19) | CORRECT | |
| 9 | Def. 4, frames, `SO(10)` (20) | CORRECT | R2. |
| 10 | Def. 5, fine block law, K-NN (21) | INCOMPLETE | "the stated fine cell lifts" are never stated. The draft's lifts (draft 3.5 item 3; Theorem 5.1(3)) are missing, and so is the cell group of the owner's NN-a text. Edit E3. |
| 11 | Def. 6, embedding `ι` (22) | CORRECT | |
| 12 | Def. 7, `T`, `k_eff` (23) | CORRECT | |
| 13 | Theorem 2.1 and proof (27-29) | CORRECT | |
| 14 | Full-`O` remark, LW1 A2 (31) | CORRECT | `LW1.md` line 209: "a site's stabilizer has three elements". |
| 15 | Lemma 2.2 (33-35) | CORRECT | |
| 16 | Theorem 2.3 and proof (37-40) | CORRECT | "fine-site orbits" means `T`-orbits; `k_eff ≥ 5` uses `5 = dim V_X ≤ |supp X|`. |
| 17 | GAP and correction (42) | CORRECT | Real. R1 refutes the draft's bound outright; R1' restores it under Theorem 3.2(i). The two-lattice sentence is draft Corollary 6.2, proof checked. |
| 18 | Lemma 2.4 (44-46) | CORRECT | For `SO(n)` the half-turn needs a third index, hence `n ≥ 3`. |
| 19 | #10014 paragraph (48) | INCOMPLETE | True as far as it goes. It drops the conditional counterexample (§2, G-E). Edit E5. |
| 20 | Theorem 3.1, statement and proof (52-56) | CORRECT | Prior work not credited: `LW1.md` "Dressed factorization" (196-205), `GA1_5_REFEREE.md` Lemma U and Proposition C. Edit E6. |
| 21 | Theorem 3.2, statement (58) | INCOMPLETE | Covariance depends on lifts with the coarse site signs `θ_g(X)` and coarse register lifts (draft Theorem 5.1(3)); not stated. Edit E3. |
| 22 | Theorem 3.2, proof (60-62) | CORRECT | Given item 21. R3 gives a shorter determinant argument. |
| 23 | Transfer and bounds paragraph (64) | ERROR | Quoted: "R is stated at generator level". `LW1_5.md` line 139 (R) reads: "for `S_+`, the generator-level site frame group is `SO(10)`, and the gate-wise group is that group outside the exceptional set." Fix: E1. |
| 24 | Turned lifts (66) | CORRECT | Flagged as unproved; correct. |
| 25 | Theorem 3.3, statement (68) | CORRECT | |
| 26 | Theorem 3.3, proof (70-72) | CORRECT | Checked: `T = Λ`, `q | 2`, the bounds 64 and 125, `p = 2`, `q = 1`, index-2 and index-3 cases. |
| 27 | Scope sentence (74) | CORRECT | |
| 28 | Example 4.1 (78) | CORRECT | Checked: rods `c' + tσ`, `t ∈ {1/2,…,9/2}`; `C_3` stabilizer; box containment; 40 + 960. |
| 29 | Example remarks, `1+1+3` (80) | CORRECT | |
| 30 | Lemma 5.1 (84-97) | CORRECT | `[check]` agrees. "face-axis `C2'`" means the axis along a face diagonal. |
| 31 | Prior records sentence (99) | ERROR | "corrected #9894" is wrong. The note's line 1134 corrects #9882's sentence and credits #9894 item 1 with `A1 + A2 + T1`. Edit E7. |
| 32 | Lemma 5.2 (101-103) | CORRECT | |
| 33 | Theorem 5.3, table and proof (105-116) | CORRECT | `O` dims: `[check]`; `O_h` splits checked by hand from the `σ_h`/`σ_d` stabilizers. |
| 34 | Script remark (118) | CORRECT | |
| 35 | Proposition 5.4 (120-122) | CORRECT | |
| 36 | Theorem 5.5, K-27 (124-126) | CORRECT | Given item 21's lifts. |
| 37 | Side-five and minimality remark (128) | CORRECT | |
| 38 | Lemma 6.1 (132-134) | CORRECT | Special case of `LW1_5.md` C2 (line 116); R2. |
| 39 | Protection paragraph (136) | CORRECT | `LW1_5.md` D (line 252): "the no-mass condition does not select five". |
| 40 | O-law centre paragraph (138) | ERROR | Maths correct (`LW1_5.md` line 169: "The site factors are respectively `−1` and `−iP_x`"). Attribution wrong: the digest never names the `SPIN10_MOTT_SITES_…` path, and "the digest's three escape routes" names nothing. Edit E8. |
| 41 | Sixteen-dial paragraph (140) | CORRECT | Stronger: the 11-mode bound is false in general and true under Theorem 3.2(i) (R1, R1'). |
| 42 | Zoom paragraph (142) | CORRECT | `ZM1.md` Z3 needs (G1); ZM1-I1[a] has "One coarse tick is `L` fine ticks". |
| 43 | Comparison paragraph (144) | CORRECT | |
| 44 | Four-test preamble (148) | CORRECT | |
| 45 | K-NN row (152) | INCOMPLETE | Test 2 should be C. The owner text fixes covariance "for `s∈𝒢=2Z³⋊O_{c₀}`" (`TOE_ASSEMBLY.md` line 235), and K-NN does not say how `𝒢` acts on one-mode sites. §2, G-K. |
| 46 | K-RUNG row (153) | CORRECT | Scope note: R1 makes "not established" into "false in general". |
| 47 | K-DIAL row (154) | CORRECT | Read with the wording GAP at line 159. |
| 48 | K-SEL row (155) | INCOMPLETE | Test 3 should be C, not P: §2, G-K. |
| 49 | K-CELL row (156) | CORRECT | |
| 50 | K-16 row (157) | CORRECT | |
| 51 | GAP in K-DIAL wording (159) | CORRECT | Real; dimensions 1, 2, 5, 8, 15 checked. Its last sentence can be strengthened to "not compatible" (R2). |
| 52 | CG16K-T and attacks A-C (161) | CORRECT | Open; three distinct attacks, each a failed construction; the C example checked. |
| 53 | Inherited opens (163) | CORRECT | |
| 54 | §8 prior work (167) | INCOMPLETE | Misses `GA1_5_REFEREE.md` Lemma U and Proposition C, `LW1.md` 196-205, `LW1_5.md` C2. Edit E6. |
| 55 | §8 literature (169) | CORRECT | Context only. |

## 2. The distiller's GAPs and the decisions asked for

**G-D (density; lines 9, 42). Real. Repaired: the bound is false in general and true for Theorem 3.2.** The draft's inference is false, not merely unproved: R1 gives `k_eff = (9/5)³` under Definitions 1, 2 and 7. Under Theorem 3.2(i), `k_eff ≥ 8` holds (R1'). The 5-, 7- and 16-site exclusions are correct as stated: an equal-size tiling has integer `k_eff`, which must then be an integer cube.

**G-R (upper bound for `L5-O`; lines 9, 64). Not real as worded.** R gives the gate-wise `SO(10)` bound outside the exceptional set, as M.1 does for `U(5)`. What is not established is the bound at exceptional angles, for both laws. That is the inherited LW1-5-X, not a new GAP. The draft's error was smaller than the distiller says: Theorem 5.1(5) omitted "outside the exceptional set" for `L5-O`.

**G-P (plaquette layer; lines 9, 64). Real; closed under stated hypotheses.** R4 (commuting sublayers, bounded gates, periodicity) with R3 (determinants). `LW1.md` E1 (line 401) already asks commuting sublayers of a supplied plaquette layer.

**G-T (broad transfer; line 9). Real.** For example, B1-U's "whose action is transitive on sites" transfers only to coarse sites; Theorem 3.3 shows the fine statement is false. The distilled restriction at line 64 is correct.

**G-W (K-DIAL wording; line 159). Real; the correction is right.**

**G-F (frame group).** The automorphism group on the dial algebra, and on the whole fine algebra, is `SO(10)`. Its implementers form a faithful `Spin(10)` on Fock space. Line 7 is correct (R2).

**G-E (#10014's "at most emergent").** #10014 (note lines 714-724) derives E from W5 and W6 and then says: "5 cannot be built from one-mode sites without smuggling … unless a coarse-rung rule makes a cluster the "site" and redefines "neighbour" at that rung. That rule would still have to pick a lopsided 5-tiling (at best 8/48) with no reason." Decision:
- Theorem 3.1 is correct. With Theorem 3.2 and Example 4.1 it gives a fine law with these properties: one mode per site; finitely many layers of even nearest-neighbour gates; finite registers; covariance under `10Z³ ⋊ O_{c'}` with all 24 rotations; and an exact frame action of `U(5)`, or of `SO(10)` implemented by `Spin(10)`, on five single sites spread along a rod.
- So E is false for laws admitted by NN-a *as read by K-NN*. These are laws whose gauge generators are block generators and whose cell group acts on fine sites through `π`. The owner's NN-a text names five-mode sites, so this is a conditional counterexample, not a refutation of an adopted statement.
- In #10014's own scope (per-term invariant nearest-neighbour bilinears), W5's "`N = 1`" step and W6 stand. The construction uses exactly the exception #10014 names, a coarse-rung rule (K-RUNG). What it refutes outright is the next sentence: once spectators are allowed, the rule need not pick a lopsided tiling. Example 4.1 keeps all 24 rotations. Without spectators, no cubic-covariant 5-tiling exists at all (Theorem 2.3).
- The construction pays for this. Fine-site transitivity fails (Theorem 3.3), and there is no fine-rung Gauss law.

**G-K (the readings and their four-tests).** Each reading is stated plainly and is not adopted. My assessments:
- **K-NN.** Tests 1 P, 3 C and 4 P agree with the draft. Test 2 is C, not P. The owner text quantifies covariance over `𝒢 = 2Z³ ⋊ O_{c₀}` acting on sites, and K-NN must also say that `𝒢` acts on one-mode sites through `π^{-1}`, a superlattice group. With that clause, test 2 passes. Without it, a law could choose its fine cell group freely.
- **K-RUNG.** P, F alone / C with a dial rule, P, C: agreed. It is the rule #10014 itself names as its exception.
- **K-DIAL.** C, P, P, C: agreed, with the spanned wording of line 159.
- **K-SEL.** Test 3 should be C. The rule takes `N` from #10014's selector, whose condition (b) is "an inserted identification, borderline" (note line 743, quoted at draft line 374). Line 136 of `CG16K.md` itself says that identification "is not a physical particle result". A dial count fixed through it settles part of the Weyl-species question for MT1-ii and CG1 by premise. Tests 1 and 4 C and test 2 P: agreed.
- **K-CELL.** P, P with K-RUNG, C, P: agreed. It lowers PS-1c's transitivity to the coarse rung. Theorem 3.3 shows that the laws of Theorem 3.2 meet PS-1c only under such a reading.
- **K-16.** Fails test 1: agreed.

**G-T3 (CG16K-T).** Attacks A (commuting gates), B (exponential of a covariant Hamiltonian) and C (layer orders fixed by the point group) are three distinct constructions. Each fails at a stated step. None is a no-go. CG16K-T stays open. Theorem 3.3 gives the necessary conditions: `k_eff = 8` and coarse translations `Z³` or `F`. Referee closure R5 adds one more. In every fine-transitive case the coarse stabilizer (all of `O`, or the tetrahedral group when `F` is paired with cube-centred rotations) fixes no five-dimensional dial space. So any realization needs the turned lifts of line 66 (CG16K-L). This is a necessary condition, not a no-go.

## 3. Referee closures

Each closure below is a complete argument, written for this report. None is adopted. Sections 1, 2, 4 and 5 cite them as R1-R5.

### R1. The density bound `k_eff ≥ 8` is false under Theorem 2.3's hypotheses (counterexample)

The distiller's GAP (line 9, line 42) says the draft's step "The smallest cube that is at least 5 is 8" (draft line 142) does not follow. It is in fact false in that generality.

**Claim R1.** There is a structure satisfying Definitions 1, 2 and 7 with `k_eff = (9/5)^3 = 729/125`. In it every coarse site except one orbit has a support of exactly five sites. So neither `k_eff ≥ 8` nor "every coarse site has at least `k_eff − 5 ≥ 3` non-dial fine modes" (draft Theorem 4.3, line 139) holds under those hypotheses.

*Construction.* Fine group `G = 9Z³ ⋊ O_0` (`c = 0`, a site). Coarse sites `X = Z³`, `κ = id`, and `π(λ, Q) = ((5/9)λ, Q)`. Scaling commutes with `Q`, so `π` is a homomorphism onto `5Z³ ⋊ O_0`, with linear parts `O`. Here `T = Λ = 9Z³` and `τ(t) = (5/9)t`, so `k_eff = 9³/5³`.

*Stabilizers.* For odd `m` and `x ∈ Z³`, let `St_m(x) = {Q ∈ O : Qx ≡ x mod m}`. Since 2 is invertible mod `m`, a rotation `Q ≠ 1` fixes `x` mod `m` exactly when `x` is congruent to a multiple of the axis vector of `Q` (check the five classes: `diag(1,−1,−1)` and the quarter-turns about `e_1` need `x_2 ≡ x_3 ≡ 0`; the 3-cycle needs `x_1 ≡ x_2 ≡ x_3`; the half-turn `(x,y,z) ↦ (y,x,−z)` needs `x ≡ y`, `z ≡ 0`). Hence `St_m(x)` is `O` at `0`, `C_4` on the axes, `C_3` on the body diagonals, `C_2` on the face diagonals, and trivial elsewhere. Counting points of `(Z/m)³`:
- `m = 5` (coarse): 1 point with `O`; 12 with `C_4` (two orbits of 6); 16 with `C_3` (two orbits of 8); 24 with `C_2` (two orbits of 12); 72 free (three orbits of 24).
- `m = 9` (fine): 1; 24 (four orbits of 6); 32 (four orbits of 8); 48 (four orbits of 12); 624 free (26 orbits of 24).

*Assignment lemma.* Let `y` be a coarse representative with stabilizer `H_y` in `G`, and let `s` be a fine site with `Stab_G(s) ⊆ H_y`. Put `S_{gy} ⊇ g H_y s` for `g ∈ G`. Then the sets `g H_y s` are well defined and partition the fine orbit `G s`. Proof: `g h s = g' h' s` gives `g^{-1} g' ∈ H_y Stab_G(s) H_y = H_y`. □ So if each fine `G`-orbit is used by at most one coarse orbit, all supports are disjoint and `G`-equivariant. For the representatives `y ∈ {0, e_1, 2e_1, (1,1,1), (2,2,2), (1,1,0), (2,2,0)}`, `Qy ≡ y` mod 5 forces `Qy = y`, so `H_y` acts linearly about the fine origin, and the seeds below are fixed exactly when they are fixed mod 9.

*Seeds.* `y = 0`: the octahedron `O·e_1` (6 sites; `V_X = E + T1`, Theorem 5.3). `y = e_1, 2e_1` (`C_4`): the fixed fine site `2e_1`, resp. `3e_1`, plus one free orbit (4 sites): 5 sites. `y = (1,1,1), (2,2,2)` (`C_3`): two fixed diagonal sites (`(1,1,1), (2,2,2)`, resp. `(3,3,3), (4,4,4)`) plus one free orbit (3 sites): 5. `y = (1,1,0), (2,2,0)` (`C_2`): one fixed site `(1,1,0)`, resp. `(2,2,0)`, plus two free orbits (2 + 2): 5. Each free coarse orbit: five free fine orbits: 5. Fine orbits used: axis 3 of 4, diagonal 4 of 4, face-diagonal 2 of 4, free `2 + 2 + 4 + 15 = 23` of 26. Where `|S_X| = 5`, take `V_X = ℓ²(S_X)`.

Per `9³` cell: 125 coarse sites, `6 + 5·124 = 626` support sites, 103 spectators. So `k_eff = 5.832`, and the average non-dial count is `104/125 < 1`. `[check]`: `check.py` in `/tmp/toe-CG16Kref/` rebuilds all 125 supports mod 9, confirms equivariance and pairwise disjointness, sizes `{5, 6}`, 626 sites, 23 of 26 free orbits used. □

The same scheme with fine `13Z³` and coarse `5Z³` gives sixteen-site supports with `k_eff = (13/5)^3 = 17.576 < 27` (`[check]`: 125 supports of 16, 80 of 85 free orbits). So the draft's "at least 11 non-dial modes per coarse site" for sixteen dials (draft line 386) is also false in this generality.

**What survives (repaired statement R1').** Under Theorem 3.2(i), `π(Λ) = 2Z³`, so `[Z³:Λ] = 8k_eff` is an integer. Then (proof of Theorem 3.3) `k_eff = p³` with `p ≥ 2`, or `k_eff = p³/8` with `p` odd and `p ≥ 5`. Hence `k_eff ≥ 8` holds for every block structure of Theorem 3.2. The average non-dial count per coarse site is then at least 3; for sixteen-dimensional `V_X` it is at least 11 (smallest admissible value 27, since `125/8 < 16 < 27 < 343/8`). "Every coarse site has" must read "on average per coarse site" even here: spectators belong to no coarse site.

### R2. The frame action of the O-law is `SO(10)`, implemented by a faithful `Spin(10)`

Let `γ_1, …, γ_10` be the dial Majoranas of `X` and `Spin(10)` the group generated by `exp(θ γ_aγ_b/2)`. At `θ = π` this is `−1`. So `−1 ∈ Spin(10)` acts on the Fock space as the scalar `−1`, and the representation `16 ⊕ 16bar` (tensored with the identity elsewhere) is faithful. Conjugation by a scalar is trivial, so the induced automorphism group of the fine algebra is `Spin(10)/{±1} = SO(10)`. `U(5)` acts faithfully on the algebra (`c ↦ e^{iθ}c` is nontrivial for `θ ∉ 2πZ`). The distiller's line 7 is therefore correct.

One sharpening, ported from `LW1_5.md` C2 (line 116: "The fixed site algebra of \(SO(10)\) is \(\operatorname{span}\{1,P\}\)"). Through `ι`, the `SO(10)`-fixed elements of `CAR(V_X)` are exactly `span{1, Γ_X}`, `Γ_X` the dial parity. (Rebuilt: the Fock representation restricts to `Spin(10)` as `16 ⊕ 16bar`, two inequivalent irreducibles, so the commutant is two-dimensional.) Lemma 6.1 is the quadratic case. It follows that a coupling `exp(iκ N_X ⊗ B)`, with `B` an even non-scalar element of `CAR(W)` and `κ ≠ 0` small, is *not* compatible with the `SO(10)` frame: register changes cannot act on matter, and `Ad_R(N_X) ≠ N_X` for `R ∉ U(5)`. Line 159's "not thereby proved compatible" can be strengthened to "not compatible".

### R3. Equal parity determinants hold for every embedded even gate

Let `S` be a compiled support with at least one fine mode orthogonal to every dial. Let `u` be an even unitary on the dial and register space. Write `D_±` for its parity sectors and `w_± = 2^{|W_S| − 1}` for the dimensions of the parity sectors of the non-dial modes in `S`. Then `ι(u)` has determinant `det(u|D_+)^{w_+} det(u|D_−)^{w_−}` on one total-parity sector and `det(u|D_+)^{w_−} det(u|D_−)^{w_+}` on the other. These are equal since `w_+ = w_−`. □ This covers matter, electric and register-only plaquette gates at once. K-27 has 22 non-dial modes per block and Example 4.1 has 960 spectators per box, so the hypothesis holds in both.

### R4. A plaquette layer compiles under stated hypotheses

Suppose a supplied plaquette layer is a fixed finite number of sublayers. Suppose each sublayer is a product of gauge-invariant even gates on pairwise disjoint sets of coarse link registers, each gate acts on at most `b` coarse links, and the sublayer is periodic under the coarse translations. Then the layer embeds as finitely many NN-a fine layers. Proof: as in Theorem 3.2(iii), give each gate a connected finite fine support containing the blocks at the ends of its links and their bridges (the blocks joined by fine paths through the bridges); it has at least three sites. R3 gives equal determinants; Theorem 3.1 compiles it. Gates in one sublayer commute, so they may be applied in any order. Supports have bounded size and finitely many shapes, so a periodic colouring with finitely many colours makes same-colour supports disjoint (the colouring step of `GA1_5_REFEREE.md` Proposition C(ii), line 190, ported). The product is `ι` of the sublayer in every order, so covariance and gauge invariance pass through `ι` as in Theorem 3.2. □ The extension is sound with these hypotheses written in. The working set leaves the plaquette class open as law data, so this is conditional.

### R5. A fine-transitive realization cannot keep fixed dial bases

**Claim R5.** Suppose the cell group `G = Λ ⋊ O_c` of a block structure (Definitions 1-2) acts transitively on fine sites. Then no coarse site's stabilizer fixes a five-dimensional subspace of `ℓ²(supp X)` pointwise. So Theorem 3.2's hypothesis (ii) fails, and any realization of CG16K-T needs the turned lifts of line 66 (CG16K-L).

*Proof.* Theorem 3.3 gives `T = Λ`, `k_eff = 8` and `π(Λ) ∈ {Z³, F}`. The linear parts of `π(O_c)`, a finite group, form `O`; a finite group of isometries fixes the centroid `c_0` of an orbit, and rotations about `c_0` preserve `Z³` only if `c_0` is a site or a cube centre. So `π(G) = π(Λ) ⋊ O_{c_0}`. Three cases.
- `π(Λ) = Z³`. For every `Q`, `Qc_0 − c_0 ∈ Z³`, so the rotations about each coarse site lie in `π(G)`: every stabilizer is all of `O`. There is one coarse site per cell and 8 fine sites, so `|supp X| ≤ 8`.
- `π(Λ) = F`, `c_0` a site. For every `Q`, `Qe_1 − e_1 ∈ F`, so both classes of coarse sites have stabilizer `O`. Two coarse sites and 16 fine sites per cell give `|supp X| ≤ 11`.
- `π(Λ) = F`, `c_0` a cube centre. The site stabilizer is `{Q : Qc_0 − c_0 ∈ F}`: the 12 rotations with an even permutation and an even number of sign changes, the tetrahedral group. A rotation outside it exchanges the two classes of `F`, so the action on coarse sites is transitive and `|supp X| ≤ 8`.
A vector fixed by a permutation group is constant on its orbits, so the fixed subspace has dimension equal to the number of stabilizer orbits on `supp X`. Five orbits of `O` about one centre need at least `1 + 6 + 6 + 6 + 6 = 25` sites (orbit sizes 1, 6, 8, 12, 24; only the centre is a singleton). Five orbits of the tetrahedral group need at least `1 + 4 + 4 + 4 + 4 = 17` (orbit sizes 1, 4, 6, 12). Both exceed the bounds above. □

This sharpens CG16K-T: the fixed-basis compilation of Theorem 3.2 cannot give fine transitivity. Turned lifts are needed. It is not a no-go for CG16K-T.

### Summary: where the closures leave the draft's claims

| Draft claim | Status after this report |
|---|---|
| "`k_eff ≥ 8`" and "at least `k_eff − 5 ≥ 3` non-dial fine modes" (draft Theorem 4.3) | False under its hypotheses (R1). True on average under Theorem 3.2(i) (R1'). |
| "at least 11 non-dial modes" for sixteen dials (draft 8.2) | False in general (R1). True on average under Theorem 3.2(i) (R1'). |
| `[Z³:Λ] = 8k_eff ≥ 64` for the laws of Theorem 3.2 (draft Proposition 5.8(a)) | True; `CG16K.md` Theorem 3.3 proves it without the false step. |
| Gate-wise `SO(10)` upper bound for `L5-O` (draft Theorem 5.1(5)) | True outside the exceptional set, by `LW1_5.md` R; open at exceptional angles (LW1-5-X). |
| "Every statement of `LW1_5.md` … holds" (draft Theorem 5.1(6)) | Too broad; holds for statements about the coarse algebra and tick only (G-T). |
| Remark 5.6's dial-number coupling "keeps the frames exact" | True for `U(5)`; false for the `SO(10)` frame (R2). |

## 4. Required edits to `CG16K.md`

Each edit is a wording or citation change. None changes the content of a theorem.

- **E1 (lines 9, 64; items 3, 23).** Replace "The draft's finite-gate upper bound for `L5-O` cites a generator-level result and is not established at arbitrary gate angles" and "but R is stated at generator level; that does not by itself classify all frames of an exponential at arbitrary angles" by: "`LW1_5.md` R gives the gate-wise `SO(10)` bound for `L5-O[S_+]` outside the exceptional set, as M.1 does for `U(5)`. The draft omitted that qualifier for `L5-O`. At exceptional angles both bounds are the inherited LW1-5-X."
- **E2 (lines 9, 42; items 3, 17).** After "Neither `k_eff ≥ 8` nor three extra modes per coarse site follows in general", add: "Both are false in general (referee R1: `k_eff = (9/5)³` with five-site supports). Under Theorem 3.2(i), `k_eff ≥ 8` holds, so the average number of non-dial modes per coarse site is at least 3, or at least 11 for sixteen-dimensional dial spaces (R1')." In line 140, replace "but does not prove the draft's general 11-non-dial lower bound" by "and the draft's 11-non-dial lower bound is false in general but true on average under Theorem 3.2(i) (R1, R1')".
- **E3 (lines 21, 58; items 10, 21).** Restore the draft's lift definition: "The fine lift `β_g` sends `c_x ↦ θ_g(X)c_{gx}` for `x ∈ supp X`, where `θ_g(X) = ±1` is the coarse site sign; it sends `c_x ↦ c_{gx}` on spectators; it acts on bridge registers by the coarse register lift (B1-U for `L5-U`, A2-5 for `L5-O`)." State in Definition 5 that the coarse group `𝒢 = 2Z³ ⋊ O_{c₀}` of the owner's NN-a text acts on fine sites through `π^{-1}`.
- **E4 (line 64).** Replace the plaquette sentence by R4's statement with its hypotheses (finitely many sublayers of commuting gauge-invariant gates on disjoint register sets, bounded size, periodic), citing R3 for determinants and `GA1_5_REFEREE.md` Proposition C(ii) for the colouring.
- **E5 (line 48; item 19).** Add: "Conditional counterexample. Under K-NN, Example 4.1 with Theorem 3.2 gives a fine NN-a law with an exact `U(5)` or `SO(10)` (implemented by `Spin(10)`) frame action on five single sites spread along a rod, with all 24 rotations. So #10014's E fails for laws admitted under K-NN. This uses #10014's own exception, a coarse-rung rule (K-RUNG). It refutes #10014's further sentence that such a rule 'would still have to pick a lopsided 5-tiling (at best 8/48)': with spectators, all 24 rotations are kept. #10014's derivation in its own scope (per-term invariant bilinears) stands. Fine-site transitivity fails (Theorem 3.3)."
- **E6 (lines 52-56, 167; items 20, 54).** Credit prior work: "`LW1.md` 'Dressed factorization' (lines 196-205) compiles each dressed cube gate of `L_cube` exactly, by the same inverse-function-theorem step. `GA1_5_REFEREE.md` Lemma U compiles every link-only unitary on five-mode sites, and Proposition C gives finite periodic depth. Theorem 3.1 extends these to all even unitaries with equal parity determinants, matter included, on one-mode sites." Cite `LW1_5.md` C2 at Lemma 6.1.
- **E7 (line 99; item 31).** Replace "and corrected #9894" by "and #9894 item 1, as recorded in the note's correction of #9882's 'no covariant 3 + 2 split' (note line 1134)".
- **E8 (line 138; item 40).** Replace "The digest `prior/CG16K.md` identifies the earlier centre obstruction in `docs/SPIN10_MOTT_SITES_…`" by "The digest identifies the earlier centre obstruction as #10027 (note lines 979, 989, 1024-1036); its note file is `docs/SPIN10_MOTT_SITES_…` (note line 1179)". Replace "the digest's three escape routes" by "#10027's listed routes (note line 981), two of them tested by #10038 and #10045".
- **E9 (table rows 152, 155; items 45, 48).** K-NN test 2: C, with the closing clause of E3. K-SEL test 3: C, for the reason in G-K.
- **E10 (line 159).** Replace "but not thereby proved compatible with the full O-law `SO(10)`" by "and is not compatible with the `SO(10)` frame (`LW1_5.md` C2; referee R2)".
- **E11 (line 11).** Give the two unnamed opens names (section 5) and drop the density GAP from the GAP list, since R1 and R1' decide it.

## 5. Open statements to carry by name

- **CG16K-T (open).** Find a coarse law with these properties: finite depth; faithful one-mode inflow on its hops (`LW1_5.md` M); an exact `U(5)`, or `SO(10)` implemented by `Spin(10)`, frame action at every angle; covariance under the 24 proper rotations and under coarse translations `Z³` or `F`. It must also come with a block structure (`k_eff = 8`, Theorem 3.3) whose dial lifts are consistent (CG16K-L), so that the fine cell group is transitive on fine sites. R5: such a structure cannot keep fixed dial bases, so turned lifts are necessary. Three attacks failed: A, commuting gates (faithful hops sharing a site need not commute); B, the exponential of a covariant gauge-invariant Hamiltonian (exact but not shown to be finite depth); C, layer orders fixed by the point group (a site-centred `C_4` maps `[0,1]³` to `[−1,0]×[0,1]×[0,1]`, a cube of neither tiling). No counterexample is known.
- **Labels proposed for two opens that `CG16K.md` leaves unnamed (labels only, not adopted).** **CG16K-16**: a coarse law whose exact frame group is `Spin(10)` acting on sixteen dials through the half-spin representation. Under Theorem 3.2(i) it costs at least 11 non-dial modes per coarse site on average (R1'). **CG16K-G**: a block route that also keeps a fine-rung Gauss law; `ZM1.md` Z3 then applies to linear transported dials.
- **CG16K-L (open; line 66).** Consistency of turned register lifts for dial bases that rotate by a cocycle `u(g, X)`: the group law and bridge orientation. It is not needed for K-27 or Example 4.1. It is needed for the `1 + 1 + 3` arrangement, the 7-star, and any full-`O` coarse site.
- **Inherited, unchanged.** LW1-5-T; LW1-5-X-B_m; LW1-5-X-O (this includes the gate-wise bounds at exceptional angles, E1); LW1-5-16 and R-CG1; GA1-P-5; VC1; CG1-i/P-HY; CG1-ii/P-COMP; MT1-ii; ZM1-I1[a] with `p = 2`; RCS-P; MT1-S[R-CS^str].
- **Owner questions (readings, none adopted).** K-NN with the cell-group clause of E3; K-RUNG; K-CELL; K-DIAL in its spanned wording, or K-SEL. K-16 fails test 1 and is not proposed.

## 6. Freeze recommendation

Freeze `CG16K.md` after edits E1-E11. No edit changes the content of a theorem. These results stand as proved: Theorems 2.1, 2.3, 3.1, 3.2 (with E3's lifts written in), 3.3 and 5.3; K-27 (Theorem 5.5); Lemmas 2.2, 2.4, 5.1, 5.2 and 6.1; Proposition 5.4; Example 4.1. If the closures R1-R5 are taken in, mark them as referee closures. R5 adds a necessary condition to CG16K-T (turned lifts); it does not decide it. This report is one check, and no one has checked it in turn. The `[check]` scripts guide and prove nothing; R1 is proved by the orbit count and the assignment lemma, not by the script.

## Prior work used

Each item was read at the commit listed under "Sources read". "Ported" means the argument is reused with credit, not re-derived as new.

| Prior result | Path | Use here |
|---|---|---|
| Digest of prior work on CG16K | `prior/CG16K.md` (all) | Map of #10014, #10027, LW1-5 F/K/SC, CH1, MT1, RCS1. |
| #10014, cluster obstruction: W5, W6, E and its exception clause | `docs/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md` lines 711-724, 743 (branch `docs/consolidate-gauge-matter-registers`) | Decision G-E; K-RUNG and K-SEL notes. |
| #10019, #10026, #10029 ledger rows; correction of #9882 crediting #9894 item 1; #10027 file link and routes | same note, lines 1197-1200, 1134, 1179, 981 | Items 31 and 40. |
| `LW1.md` Theorem A2 (site stabilizer of order three; sign gauge) | `LW1.md` line 209 | Item 14; lifts in E3. |
| `LW1.md` Dressed factorization (exact finite words by the inverse function theorem) | `LW1.md` lines 196-205 | Credited for Theorem 3.1 (E6). **Missed by the digest.** |
| `LW1.md` Theorem E1 (commuting plaquette sublayers) | `LW1.md` line 401 | G-P, R4. |
| `LW1_5.md` C2 (fixed algebra of `SO(10)` is `span{1, P}`) | `LW1_5.md` line 116 | Ported into R2; E10. **Missed by the digest and by `CG16K.md`.** |
| `LW1_5.md` M and M.1, R, U, Q and G, `z_x`, F and K, D, A2-5, B1-U, PS-1c | `LW1_5.md` lines 120, 139, 143, 130, 169, 171, 252, 262, 266, 60 | Items 23, 39, 40; E1; G-T. |
| `GA1_5_REFEREE.md` Lemma U (compiling link-only unitaries) and Proposition C (finite periodic depth) | `GA1_5_REFEREE.md` lines 154-190 | Credited for Theorem 3.1; colouring step ported into R4. **Missed by the digest.** |
| Owner NN-a text GA1-P-NN, its check and "What it changes" | `TOE_ASSEMBLY.md` lines 231-237 | Items 10 and 45; G-E; E3, E9. **Its cell-group clause and "Gauge-variant intermediate factors are allowed as compilation steps" are missed by the digest.** |
| Owner text ZM1-I1[a] | `TOE_ASSEMBLY.md` lines 239-244 | Item 42. |
| `ZM1.md` (G1) and Theorem Z3 | `ZM1.md` lines 71, 319 | Item 42. |
| `B5B.md` Theorems 3.1 and 3.3 | `B5B.md` lines 82, 103 | Item 54 (citation checked). |
| `RCS1.md` R-CS^str (proposed), RCS-P (open) | `RCS1.md` lines 18, 89 | Item 53 (citation checked). |
| Pass 1 | `CG16K_DRAFT.md` | Source of every item; draft Theorem 4.3, 5.1, Corollary 6.2, Proposition 5.8, section 9 checked against the distillation. |

## Sources read

| Source | Commit | Lines read |
|---|---|---|
| `CG16K.md` | `c82ee8663` | 1-169 (all) |
| `CG16K_DRAFT.md` | `31ef08a1e` | 26-41, 91-116, 137-290, 337-479; grep hits in 3-22, 42-87, 293-336 |
| `prior/CG16K.md` | `15bc39079` | 1-94 (all) |
| `LW1_REFEREE.md`, `Y2W_DRAFT.md` | branch head | 1-80; 1-30 (format only) |
| `TOE_ASSEMBLY.md` | `36d5dd136` | 231-245; grep hits 90, 126, 129, 180, 207-208, 214, 393, 578 |
| `LW1_5.md` | `727ad9884` | 57-62; grep hits in 106-186 (108-177) and 252-274 |
| `LW1.md` | `4b65c608f` | 190-205; grep hits 137, 209, 211, 215, 391, 393, 401 |
| `GA1_5_REFEREE.md` | `8d0d4b4db` | 154-190; grep hits 38, 63, 113, 152, 237, 301, 310 |
| `ZM1.md`, `B5B.md`, `RCS1.md` | `36d5dd136` (last commit touching them) | grep hits: `ZM1.md` 14-16, 61-71, 311, 319; `B5B.md` 9, 82-103; `RCS1.md` 9, 18, 89, 181, 207, 217 |
| `MT1.md`, `CH1.md` | branch head | grep hits only: `MT1.md` 25, 144, 150; `CH1.md` 24, 50, 54 |
| `origin/docs/consolidate-gauge-matter-registers`: `docs/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md` | `7086189d1` (after `git fetch -q`) | 700-726, 1197-1200; grep hits 21, 23, 37, 45, 57, 123, 246, 252, 269, 720, 743, 821, 981, 1134-1135, 1140, 1159, 1162, 1179 |

`[check]` script: `/tmp/toe-CG16Kref/check.py` (Python 3, under 2 s, a few MB, started with 55 percent memory free). It does three things. It rebuilds the R1 structures mod 9 and mod 13 and confirms their counts and disjointness. It recomputes the `O`-isotypic dimensions of the octahedron, the 7-star and the cubes of side 1 to 5 by character averages. Its output agrees with R1 and with Theorem 5.3. It proves nothing.

## FINISH

**Proved** (this report; one check, not itself checked).
1. Verdicts on all 55 items of `CG16K.md`: 45 CORRECT, 4 ERROR, 6 INCOMPLETE. No ERROR or INCOMPLETE item changes the content of a theorem.
2. R1. Draft Theorem 4.3's hypotheses admit `k_eff = (9/5)³ < 8` with five-site supports, by an orbit count and an assignment lemma. The sixteen-dial analogue has `k_eff = (13/5)³ < 27`.
3. R1'. Under Theorem 3.2(i), `k_eff` is `p³` (`p ≥ 2`) or `p³/8` (`p` odd, `p ≥ 5`). So `k_eff ≥ 8`, and `k_eff ≥ 27` for sixteen-dimensional dial spaces.
4. R2. The O-law dial frame acts on the fine algebra as `SO(10)`, implemented by a faithful `Spin(10)` on Fock space. With `LW1_5.md` C2 (ported), a dial-number coupling is not `SO(10)`-compatible.
5. R3. Every embedded even gate on a support with at least one non-dial mode has equal parity-sector determinants.
6. R4. A supplied plaquette layer compiles as finitely many NN-a fine layers under stated hypotheses. The colouring step is ported from `GA1_5_REFEREE.md` Proposition C(ii).
7. R5. If the fine cell group is transitive on fine sites, no coarse stabilizer fixes a five-dimensional dial space. So CG16K-T needs turned lifts (CG16K-L).
8. Decisions asked for:
   - K-27 and its exact block-scale frame action: CORRECT, once the lifts are written in (E3).
   - The group is `SO(10)` on the algebra, with a `Spin(10)` implementation: CORRECT.
   - Theorem 3.1: CORRECT (prior work to credit, E6).
   - The `k_eff ≥ 8` GAP: real, and the bound is false in general (R1).
   - The 5-, 7- and 16-site exclusions: CORRECT.
   - Theorem 3.3 and CG16K-T with attacks A-C: CORRECT, open.
   - K-RUNG, K-DIAL and K-CELL: four-tested correctly. K-NN test 2 and K-SEL test 3 should be C.

**Counterexamples.**
- R1, to draft Theorem 4.3's "`k_eff ≥ 8`" and "at least `k_eff − 5 ≥ 3` non-dial fine modes", and to draft 8.2's "at least 11 non-dial modes", each in its stated generality.
- To `CG16K.md` line 64's reading of `LW1_5.md` R: R's own text gives the gate-wise bound outside the exceptional set.
- Conditional on K-NN: to #10014's "So Spin(10) on a spread cluster can be at most emergent", read for NN-a laws, and to its "That rule would still have to pick a lopsided 5-tiling (at best 8/48)" once spectators are allowed. Example 4.1 with Theorems 3.1 and 3.2 is the witness. #10014's W5 and W6 stand in their own per-term scope.

**Open by name.** CG16K-T (attacks A, B and C failed; no counterexample); CG16K-L; CG16K-16 and CG16K-G (labels proposed for opens `CG16K.md` leaves unnamed); LW1-5-T; LW1-5-X-B_m; LW1-5-X-O; LW1-5-16 and R-CG1; GA1-P-5; VC1; CG1-i/P-HY; CG1-ii/P-COMP; MT1-ii; ZM1-I1[a]; RCS-P; MT1-S[R-CS^str]. Owner questions: K-NN, K-RUNG, K-CELL, K-DIAL or K-SEL.

**What changes downstream.**
- `CG16K.md`: edits E1-E11, then freeze (section 6).
- Owner questions: K-NN needs a clause saying how `𝒢` acts on one-mode sites (through `π^{-1}`). K-SEL's test 3 is conditional.
- Density: the "at least three non-dial modes per coarse site" claim holds only on average, and only under Theorem 3.2(i). A later part that drops (i) cannot use it.
- LW1-5-X: it carries the exceptional-angle frame bounds for both laws. There is no separate `L5-O` GAP.
- CG16K-T: any fine-transitive block route must use turned lifts (R5), so CG16K-L becomes a prerequisite.
- #10014's verdict: under K-NN and K-RUNG, five dials with exact frames and all 24 rotations exist (Example 4.1, K-27). Its tiling objection is answered by spectators or collective dials. Its per-term argument is unchanged.
- CG1, MT1-ii, CH1, FL1, EW1: unchanged. The 16 question stays where `LW1_5.md` left it.
