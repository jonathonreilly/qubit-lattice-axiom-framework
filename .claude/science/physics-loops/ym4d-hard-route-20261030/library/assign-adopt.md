lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-03T15:00Z

# assign-adopt: the explicit erosion assignment as the localisation, and what its consumers read (queue row 110)

Provenance: Claude Opus 5.5, high effort, Mac mini worker, pinned at 84313ded3. Same-model and not gated. This is research-stage text: no status, no audit. Outline: Sussman-Alpoge `YM4_sketch_500.tex` at `31a47c543775`, fetched once by URL to a scratch folder and not copied here. Line numbers below are SA lines in that file.

Credit. The assignment adopted here is the visible repair in `gates/a3-close-meet-gate.md` Section H (Codex, row 106). Its first-rule twin and the joined-sequence lemma are `library/a3-close.md` Lemma J (Claude, row 103). The rules being instantiated are the outline's two erosion assignments (SA 5598-5610), and every consumer named below is theirs: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. Balaban (CMP 119 (1988) 243, Sections 1-3) is credited for the localised-background tests that the outline adopts.

Moves: the one premise that row 106 left on real-critical A3 and on 2.8, namely the identification of the erosion assignment (gate D1, Sections B, H, I).

## 0. Result

- **Adoption is admissible.** SA 5608-5609 allow "a particular assignment is supplied". Definition A below supplies both rules. Lemma A proves every requirement SA 5598-5610 places on an assignment, together with the properties the consumers read: cube unions, gaps, actual sets, one translation-compatible rule on all tori, commuting with common lifts of non-wrapping regions, plus an erosion-depth upper bound, monotonicity, locality and independence of the unit (Statement 3.8, SA 22044).
- **The joined sequence is then determined (Lemma JS).** Once Definition A is fixed, SA 9786's qualitative clauses (taken with the cut at depth j_a that its "levels q < j_a" clause forces) single out exactly the cut meet of Lemma J. So the gate's D1, "a compatible construction is not the source's", no longer applies on our chain. What remains is a definitional ruling, recorded as one: the outline's localisations are *defined* by Definition A.
- **Consumers (Section 4): no counterexample.** Every consumer of the localisations or towers that our chain reads uses only properties (A1)-(A9). Those consumers are Theorem 6(a), 6(b), 6(c), the four meets of 2.8 with (SEP) and (SEP-L), the cube-localised backgrounds of the tests (SA 17317-17380) as read by the floor-screening and support notes, the hereditary tower clauses (Lemma T = Theorem 5(a)), and statement 0 of 1c. No consumer reads a property that only a different assignment has. The one candidate, Theorem 5(b)'s requirement that the tower lie inside an ambient sequence, is a hypothesis checked where 5(b) is applied, and Definition A meets it there (4.7).
- **Label:** row 106's open identification is **discharged as a definition plus an implication**. The analytic results of rows 103 and 104 (Theorem 6(c) via Lemma 10.1, Theorem M, (SEP) and (SEP-L)) now hold for the outline's localisations as defined here. They still carry their own named premises: F0, the A1 port, P82°, GEO1-GEO6 and EXT (Proposition 2.3).

## 1. Definition A (the adopted assignments)

Conventions are those of SA 5585-5616 and of Lemma T. A level-p cubical subdomain Z is a union of cubes of the level-p localisation partition π_p (centred half-open M-cubes in level-p units). Work in level-p units, with tower scales ξ'_q = L^{q-p} for 0 ≤ q ≤ p. Distances d_∞ are periodic sup-distances between site sets on the torus. An *aligned* cube of side sξ'_q is a cube of the centred grid of that side; all grids are nested because L is odd and all sides are powers of L (SA 6029, 24060-24067). The torus side is a multiple of every grid side used (SA 24063). Fix the powers of L in the outline's order (SA 9916, 19469-19480), with

  𝔐 ≤ M_1' ,   L^2 M_2 ≤ M ,   M_1' < M_2 (so M_2 ≥ L M_1'),   ρ = R_1 𝔐 ≥ L 𝔐 .   (1.0)

**First rule.** T_0 = Z, and T_{q+1} is the union of the aligned cubes Q of side 𝔐ξ'_{q+1} with d_∞(Q, T_q^c) > ρξ'_q.

**Second rule.** T_0 = Z, and T_{q+1} is the union of the aligned cubes Q of side M_1'ξ'_{q+1} with d_∞(Q, T_q^c) ≥ M_1'ξ'_{q+1}.

**Cut at depth n** (0 ≤ n ≤ p): the sequence (T_0, ..., T_n), with T_{n+1} = ∅. Members may be empty.

**Localisation** (SA 9776 (a)): the cube-wise meet Ω'_q = Ω_q ∩ T_q of a separated sequence with the tower of a region. The **joined sequence of a μ-collared region** (SA 9786) is Ω'_q = Ω_q ∩ ⋂_b T^b_{min(q, j_b)}, where T^b is the tower of the part A_b under the rule named by the consumer. This is Lemma J's formula, and Lemma JS shows it is forced. In particular `meet-6c.md` Proposition 7.1's 𝓛_X Ω is the meet with the second-rule tower of X (μ = M_1'), and the cube-localised background U_{k,□} (SA 9789, "one part on one lattice, μ = M_1'") is the background of the second-rule tower of its part.

Units are lattice units throughout. No length in Definition A refers to a physical scale.
