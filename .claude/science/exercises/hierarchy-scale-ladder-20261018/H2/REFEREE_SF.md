**HIER-2 referee record. Same-family referee (Claude Opus 5.5, not independent), 2026-10-18.**

**VERDICT: NOT CONFIRMED as MASS-NO. The correct fixed reading is OPEN.** The L1 negative itself survives my checks, but as a numerical result on a comparator model, not as a proof.

**Findings**

1. **R1 claims more than it proves** (REPORT.md:21).
   - What is proved: in period-2 Bloch breaking, the ladder corrections (a/w)^p are O(q^p) and cannot gap the node.
   - Packets do not change this. An incommensurate spurion, Q = c + δ, enters through an axial offset |δ|/2 that sets a threshold, not a factor.
   - Counterexample to the general claim: a breaking placed once per rung cell of size L, on the staggered sublattice, has node-charge amplitude ε₀(a/L)³. That gaps the node at first order, with ε = ε₀(a/L)³, a ladder ratio. The report's own "(a/L)³" corollary is the single-defect limit of this case.
   - This case lies outside L1, and the rung assignment is supplied, so it falls in R3's free-integer bin. Correct form of R1: "for period-2 Bloch breaking, ε is the breaking amplitude."

2. **R4 is correct** (REPORT:35-42).
   - Lemmas (a)–(e) hold. (d) depends on the definition "fixed line = the whole fixed space of its stabiliser".
   - Wording fix: the 26 multi-charge hw1 directions are three-harmonic and sit inside L1. So "multi-harmonic" in the Open list (:83) is partly wrong.

3. **R5 reads singular values as masses, and that is wrong** (orders_group.py:339-342).
   - For a node pair (s, s+c), only one 2×2 direction gives a gap: P_c = 1, σx, σy or σz for c = 111, 100, 010, 001. It is the unique M with h_s M + M h_{s+c} = 0.
   - The rest of the block is a Lorentz-violating tensor term. A pure-tensor block has singular values (m, m) but leaves a gapless nodal ring.
   - Exact 4×4 pair-block check over the single-charge pairs (ref_checks2_A1-A1.out): 86 of 120 are certified gapless (half-gap about 1e-18 at a found q), 30 are gapped at order 1, and 4 at order 3.
   - Examples:
     - Every 111 T1 direction, counted as (1⁴), is gapless: Dirac part 0.000, tensor part about 0.40.
     - In 111 T2g dir0, counted as (1³, 3), the three doubler pairs are gapless; only the k* pair is gapped, at ε³.
   - So the pattern census at :48 and in parse_variants.out does not count masses. Where the tensor part is zero, the gap equals the singular value exactly.
   - True single-charge gap orders are still {1, 3}, with at most 2 per direction.
   - Multi-charge directions: the band-centre gap is certified zero in 14 of 26. The gapped cases are not certified: one apparent ε² gap turned out to be a missed zero (ref_check3.out vs ref_check4.out).

4. **The node representation does not contain PR #9702's projective symmetry group** (PREREG_FOLLOWUP:8, REPORT:60).
   - The τ twists (orders_group.py:91-112) are induced from class functions. They cancel on bilinears within an orbit, so all 8 variants are equivalent for charge 111.
   - In every variant, the charge-111 A2g and A2u spurions give no mass (orders_A*.out:22-23). The PR note says the opposite: I R I⁻¹ R⁻¹ = A2(R) (note :41), and its A2 staggered term gaps the quartet linearly (:43).
   - I built that representation, with the scalar cocycle A2(R), checked it is projective and that H0 is covariant under it (ref_check5.py). In it, A2 gaps all four pairs at order 1 and A1 gives nothing.
   - The results there are unchanged: singular-value orders {1, 3}, single-charge true gaps {1, 3}, at most 2 per direction.
   - So R7's mapping is wrong for the worker's own variants, but the conclusion survives.

5. **The span argument does not hold** (PREREG_FOLLOWUP:7, REPORT:49-51).
   - "V1 + V3 = Fix implies nothing new at order ≥ 5" is false in general. With M1 = E11 and M3 = E12 + E21, the span condition holds, yet a singular value appears at order ε⁵.
   - The {1, 3} claim therefore rests on the numerics, which include cross terms through order 7.
   - I closed the remaining gap, that an "∞" could hide an order ≥ 9: the generic rank of Fix equals the number of massive values in every direction (ref_checks_A1-A1.out, no mismatch).
   - Subgroup coverage: 150 random 3-generator subgroups per irrep gave no new fixed line.

6. **R2 holds for the exponents only** (REPORT:23-27).
   - In X2′, the lattice symmetries act identically on all 16 components (GEN1 a1 and a3(ii), chirality branch).
   - If colour is spread over cells (COL-1 class M, 35-site patterns), a ladder structure could separate quarks from leptons. Nothing on the ladder separates up from down, so the t:b failure stands.
   - "M_u ∝ M_d ∝ M_e and V_CKM = 1" needs identical coefficients as well. The ladder does not impose them; this is the minimal-SO(10), single-10_H case.

7. **The fixed reading is OPEN.**
   - TESTS.md:28 requires "a proof that the class cannot produce it", meaning HIER-2's class. HIER-1's wording ("within a stated class") is not available here.
   - By its own account R5 is "not a proof for higher-dimensional representations" (REPORT:44), and it runs on a comparator node representation.
   - So the record at TESTS.md:105 does not meet MASS-NO, even within L1.
   - R3 and R6 are sound in logic; I did not rerun them.

**Strongest correct statement.** OPEN.
- **Proved:**
  - R4(a)–(e); in particular, a one-dimensional spurion irrep gives a single finite order.
  - Exponents are sector-blind under both placements: generations as lattice labels, and X2′.
  - Free-integer exponent fits carry no evidence.
- **Checked numerically:** a naive-type comparator node space, with the worker's twists and with the PR's A2 cocycle.
  - One period-2 spurion in one irrep, along a symmetry-fixed line, gives chirality-odd terms only at orders 1 and 3.
  - Genuine Dirac gaps in single-charge directions occur only at orders {1, 3}, at most two per spurion. Often there is none, because the leading term is a Lorentz-violating tensor.
  - Two levels fit no sector within ×3.
- **Not excluded:**
  - dilute or longer-period breaking, where ε = ε₀(a/L)³ but the rung assignment is supplied;
  - two-amplitude classes;
  - interaction-driven masses.

Referee scripts and outputs are in `.../scratchpad/hier/ref_H2/`. Each ran alone; peak memory was 130 MB.