# C6 independent review

**Reviewer:** Claude Opus 5.5 (claude-opus-5-5), a subagent. I re-derived the proofs by hand and wrote my own code (`review_scripts/`), which imports neither `c6_lib.py` nor the author's runners. I did not commit anything. Everything ran on one core.
**Provenance caveat:** the same model family as the author. This is not an independent human check.
**Network:** I could not fetch arXiv or ar5iv (DNS blocked). Web search gave only abstract-level text and secondary paraphrases of BHM. Every BHM detail below is marked as recalled or as confirmed by snippet.

## Independent evidence (own code, own conventions)

My conventions all differ from the author's: qubit indexing, direction labels, the on-site Jordan–Wigner map (reversed qubit order, a permuted direction-to-Majorana map), plaquette product order, the corner vertex ordering (seeded random and translation-invariant), and one tube per lattice edge instead of two. So I compare only quantities that do not depend on convention.

| log | content | result |
|---|---|---|
| `review_scripts/rv_main.log` | k(L) for F1 (2 orderings), F3, toric at L = 2..7, F4 at L = 2..5, F5 at L = 2..4; commutation and Hermiticity; frustration-freeness (FF) from an explicit left-kernel relation basis with exact phases (8 sectors, L = 2..6); TQO-1 on the torus by explicit centralizer-in-cube basis vs. the stabilizer span (not the cleaning formula), 10 (family, L) cases including corner L = 2, 3; Levin–Wen T-junction with ℓ = 1, 2, 3 and a toric control; corner T-junction with length-2 legs, 240 cases | `TOTAL: PASS=9 FAIL=0` |
| `review_scripts/rv_local.log` | (T1)/(T2) for my own corner 2-complex, cube sides 1–4; Lemma 1 in local stabilizer form by explicit centralizer: F1 r ≤ 3 (W = 3), F3 r ≤ 3, F4 r = 1, F5 r = 1, 2 (W = 2); negative control (remove one B_v, defect 1 detected) | `TOTAL: PASS=3 FAIL=0` |
| `review_scripts/rv_ff_relations.log` | proved relation-module basis, checked by dimension at L = 3..6; FF signs of the basis relations up to L = 12 (F1 two orderings to L = 12 / 10, F3 to L = 12), all 8 sectors | `TOTAL: PASS=4 FAIL=0` |

Key numbers:
- **k:** k = 3 for F1, toric and F5 at every L tested. F3/F4 have k = 3 at even L and **k = 2 at odd L** (L = 3, 5, 7).
- **TQO-1:** the logical counts in cubes of side r = 1..L are [0, …, 0, 2k] in all cases (e.g. corner L = 3: [0, 0, 6]).
- **Frustration at odd L:** 7 of 8 sectors are frustrated, and only flux 0 is FF. This matches the author's log.
- **Exchange sign:** −1 in every twisted case (F1, F3, F5) and +1 for the toric control.

## Per-claim verdicts

| # | verdict | severity | notes / fix |
|---|---|---|---|
| R1 Lemma 1 | **correct** | — (wording: minor) | See §1. I re-derived every step for the edge, repetition and Majorana cases and for the corner (T1)/(T2). The runner's cell families are the same as the §2.3 complex. One difference: the runner builds each tube twice (once from each end site), which is harmless; my build uses one tube per edge and gets the same homology. Fix: state the duplicate in §2.3. Also W counts the lattice sites a generator spans, so say so explicitly. |
| R2 TQO-1 | **correct** | — | Independently reproduced: no logical in any cube of side ≤ L−1, for 10 cases. The proof route (side ≤ L−2W−1) is valid. |
| R3 GSD | **correct** | minor | k ≤ 3 by the injection into H_1 ⊕ H^1 is valid. The odd-L argument in §3 (H^1 parity, plus Σ_v B_v ∝ Σ_e A_e at odd L) is a proof of k ≤ 2, not only a post-hoc story; with the certificates, k = 2. Relabel it "POST-HOC discovery; upper bound proved". Remark to add: GSD depending on the parity of L for F3/F4 is a translation-symmetry ("weak") enrichment effect. "GSD 8 on T^3" is therefore not an L-independent invariant of the T^3 topology for these encodings, and R8 should say so. |
| R4 FF | **correct as a certificate**; the general-L proof is still open but much reduced | moderate | See §3. I proved that the GF(2) relation space is {cube relations} (dim L³−1) ⊕ 3 plane relations ⊕ an all-B relation (F1 always; F3 iff L even), confirmed by dimension at L = 3..6. Because the sign is a homomorphism on this space, FF is equivalent to +1 signs on about 5 basis relations. The cube sign is local, so it does not depend on L once L ≥ 3. Certified to L = 12. What remains is a closed-form plane / all-B sign. Suggest adding this reduction to §3. |
| R5 logicals / distance | **unverified** (not re-run) | minor, not load-bearing | The argument is plausible. BHM needs only R1/R2, not d. |
| R6 fermion statistics | **correct** | — | Confirmed with my own T-junction, e^{iθ} = t3 t2⁻¹ t1 t3⁻¹ t2 t1⁻¹. The legs were checked to anticommute only with B at their two ends and to commute with every plaquette or loop. Result: −1 for F1 (2 orderings and a flux sector), F3, and my own corner build (240 of 240); +1 for the toric control. Mechanism, which explains why the sign does not depend on ordering: hops sharing a vertex always anticommute. For F1/F5 this comes from the ordering tails; for F3/F4, on-site Majoranas anticommute while Majoranas on different sites commute. With three such pairs the formula gives (−1)³. |
| R7 BHM stability | **correct with fix** | moderate (citation precision) | See §2. Fixes: (a) "R1 is exactly the stabilizer form of TQO-2" should read "R1 implies TQO-2". (b) For exponentially decaying V, do not claim poly(L)·e^{−cL} unless it is checked against the paper; write "superpolynomially / exponentially small as in [BHM Thm]". (c) In the R7 row, "uniformly in L" should read "uniformly over the L-sequence on which FF holds (all even L; all L for flux 0)". |
| R8 persistence | **correct with fix** | minor | Hastings–Wen and BMNS supply the locality-preserving unitary. They do not themselves prove that 3D point-particle exchange statistics are invariant. Cite a statement that does, or mark this step as standard but not proved here. Add the remark on GSD and parity of L (see R3). |
| R9 scoped no-go | **correct with fix** | minor | See §4. N1–N8 hold. Make the scope explicit: periodic tori (bulk only); qubit-local perturbations; J0 unquantified and possibly tiny. |

## 1. Lemma 1 (re-derivation)

**Edge codes (F1).** ω(x, B_v) = |a ∩ star v| forces ∂a = 0, so by (T1) a = ∂c. Multiplying by ∏_{f∈c} S_f cancels the X-part, because S_f has X exactly on ∂f; the Z-tails are irrelevant to that cancellation. Commuting with S_f then gives δb = 0 on every face, so by (T2) b = δφ and Z(b) = ∏B^φ.

**Repetition halves (F2, F5).** Commuting with R forces equal X on both halves. On a link the closed cochain is b_{h1} + b_{h2}. After dividing by ∏B^φ, what is left is a product of R's. Correct. This also holds for F5, where B_q acts on the on-site edges and the half at q.

**Majorana codes (F3, F4).** I checked ω(x, y) = Σ_v(|x_v||y_v| + x_v·y_v): Majoranas on different sites commute under on-site Jordan–Wigner. Then:
- ω(·, B_v) = |x_v|;
- for site-even x, ω(·, A_e) = y_e;
- y = δφ, then x = Σ z_e A_e with ∂z = 0, then z = ∂c.

For F4, P_up and P_dn pair the matter bits, and D_v ≡ B_v modulo the P's. Correct.

**Corner complex (T1), tube sliding.** A tube is an annulus of 4 rectangles. Each rectangle has boundary link + on-site + link + on-site, so adding rectangles moves links within a tube at the cost of on-site edges only. At a site, the boundary summed over its 12 corners counts only link endpoints, because on-site edges contribute twice. So the tube parities n_e form a cubic 1-cycle. A 4-link plaquette cell meets each of its 4 tubes in exactly one link, so subtracting ∂c clears the parities. The leftover is a 1-cycle on each cuboctahedron. All 14 faces are filled and χ = 12 − 24 + 14 = 2, so it is a sphere and the cycle bounds.

**Corner complex (T2).** b is closed on all cells and vanishes outside B. On Z³ the complex has H¹ = 0, which follows from (T1) applied to any finite cycle. So b = δφ, and φ is constant on the connected complement, which can be taken as 0. Correct.

**Runner versus proof.** `cycles()` in `c6_lib.corner_code` and in the repo runner contains exactly squares (6), triangles (8), tubes (4 per (v, d) over all 6 d, so each tube appears twice), and 4-link plaquettes (3). This is the complex of §2.3. My own cell list, with one tube per edge, gives the same homology and the same TQO counts.

## 2. Bravyi–Hastings–Michalakis

**What I know reliably** (recalled; the shape is confirmed by search snippets of the abstract and of secondary sources):
- BHM, J. Math. Phys. 51, 093512 (2010), arXiv:1001.0344.
- H0 = Σ Q_A is a sum of geometrically local, pairwise commuting projectors on a D-dimensional periodic lattice, with ground space P = ∩ ker Q_A. This is frustration-free with gap ≥ 1 by construction.
- TQO-1: P O_A P = c(O_A) P for O_A on cubes of side ≤ L*, with L* growing as a power of L.
- TQO-2: the local ground projector P_B of a slightly enlarged cube and the global P have reduced states on A with the same kernel. Secondary sources state it as ker Tr_{Ā} P = ker Tr_{Ā} P_B. It is required only for topologically trivial regions.
- Conclusion for J ≤ J0 (constants independent of L): the spectral bands that come from the low levels of H0 stay separated by an O(1) gap, and the lowest band (2^k levels) has width exponentially small in L (in L* for strictly short-range V).
- Citations that look right: Bravyi–Hastings CMP 307, 609 (2011); Michalakis–Zwolak CMP 322, 277 (2013), which generalises to frustration-free Hamiltonians with a local gap and LTQO and drops commutativity; Hastings–Wen PRB 72, 045141; BMNS CMP 309, 835.

**What I could not verify** (paper text unreachable):
- the exact decay class allowed for V, and the precise width bound for exponentially decaying V (possibly a stretched exponential or a power of L*);
- the exact gap constant (1/2 is a choice of J0, and harmless);
- the exact enlargement used in TQO-2.

**Does the note's use match?**

*Stabilizer reduction.* For stabilizer codes, Tr_{Ā}P ∝ the projector onto the code of S ∩ P_A, and the same holds for P_B with S_B ∩ P_A. TQO-2 therefore holds iff every element of S supported in A is generated by generators inside B. Lemma 1 (C(S_B)|_A ⊆ ⟨S_B⟩) implies this, and also implies TQO-1 when nothing wraps. So the hypotheses are verified. The relationship is "implies", not "is exactly".

*Uniform gap, splitting, and no symmetry requirement.* These are consistent with BHM for finite-range V and L* = Θ(L). For exponentially decaying V, the bound should be quoted from the paper.

*Odd-L frustration.* This is legitimate as stated. BHM is a statement for each L with constants that do not depend on L, so any infinite sequence of L, such as even L or flux 0 at all L, gives a thermodynamic statement. Flux 0 is FF at all L tested, so it supplies the full sequence. At odd L a π-flux sector is a boundary-condition artefact: an odd number of plaquettes with flux −1 in a plane forces a defect. Flipping one plaquette sign per plane, a non-local twist of the boundary condition, restores FF without changing the bulk terms. Infinite-volume bulk properties are unaffected.

The literal finite-volume claim "uniform in all L" fails for the frustrated sectors at odd L, because the ground band there contains forced excitations. The R7 row must say "along FF sequences", as the conditional in §4 already does.

## 3. FF beyond the author's certificate (reviewer's addition)

For F3, a relation Σφ_v B_v + Σc_p S_p = 0 forces z = ∂c to satisfy z_e = φ_v = φ_{v+a} on every edge. Hence:
- φ is constant;
- φ = 0 gives c ∈ Z_2, which is the span of the cubes plus 3 planes;
- φ = 1 needs ∂c = (all edges), which is solvable iff L is even.

For F1, the X-parts force c ∈ Z_2, and there is in addition the identically trivial all-B relation.

The dimensions match the left kernel at L = 3..6. Generators commute and are Hermitian, so the relation sign is a GF(2) homomorphism, and FF ⇔ the signs of {one cube, 3 planes, all-B} are all +. The results:
- even L = 4..12: all signs are + in all 8 sectors;
- odd L: the plane-c sign is (−1)^{f_c} and the cube sign is +.

Closing R4 for all L now needs only a closed-form evaluation of the plane and all-B signs.

## 4. Scoped no-go (N1–N8)

The discipline holds: the wall is J ≤ J0; FF is listed as a premise; the steelman (spin-ice photon) is conceded outside the domain; resolution is lattice-wide and per_mode is not run; no prior wall is contradicted. Points to state explicitly, since they are currently implicit:
1. **Periodic tori only.** BHM says nothing about open boundaries or defects, where gapless boundary or defect modes are not excluded by this argument. "No gapless excitation" is a bulk statement.
2. **J0 is unquantified.** The O(1) hoppings in the corner Dirac-pair notes are not shown to be inside or outside the stable region. The note already says this; keep it next to R9.
3. **The no-go covers qubit-local perturbations.** For F3/F4, Majoranas on different sites commute (on-site Jordan–Wigner), so these are not physical lattice fermions. This should be said if the corollary is ever read as a statement about a fermionic UV.
4. **N1 route 5** (no U(1) enlargement) follows from the gap R7 alone. It need not lean on R8, which is cited.

"No massless fermion" is correct in the many-body spectral sense inside the region.

## Reproduce

```bash
cd .claude/science/physics-loops/toe-scale-ladder-20261018/blocks/C6/review_scripts
python3 rv_main.py           # ~2 min, TOTAL: PASS=9 FAIL=0
python3 rv_local.py          # ~40 s, TOTAL: PASS=3 FAIL=0
python3 rv_ff_relations.py   # ~1 min, TOTAL: PASS=4 FAIL=0
```

Combined: **TOTAL: PASS=16 FAIL=0**.

---

## Correction confirmation (2026-10-18, same reviewer)

I read the whole revised NOTE.md and `scripts/c6_ff_general_L.py`, and its log (`TOTAL: PASS=6 FAIL=0`).

### (1) Earlier findings

| finding | status |
|---|---|
| R1 (duplicate tubes, W in sites, "implies") | resolved |
| R3 (k ≤ 2 proved at odd L; weak-enrichment remark) | resolved |
| R5 marked UNVERIFIED | resolved |
| R7 (a) "implies" | resolved |
| R7 (c) "along FF sequences" | resolved in the R7 row; see N-2 for F5 |
| R8 statistics invariance marked "not proved here" | resolved |
| R9 / N1 scope (tori, bulk, qubit-local, J0, route 5) | resolved |
| R7 (b) bound for exponentially decaying V | **partly**; see N-1 |

### (2) The new FF theorem for F1–F4 (FF ⇔ L even or f = 0): checked and correct

**Relation basis, all L.** I re-derived it.
- F1/F2: vec(∏_c S) = Σ_e (∂c)_e vec(A_e) by (H4). Hence ∂c = 0 forces the S-product to the zero vector, which in turn forces φ = const (star map kernel = constants).
- F3/F4: φ_v = (∂c)_e at both ends of every edge.

Both arguments hold for all L, so the dimension checks are only confirmations.

**Periodicity step.** I re-derived it.
- The product over Z_m^D of translates of a fixed motif, in lex order, has phase m^D·p + 2 Σ_δ w(δ) · m^{D−1} · cnt(δ_first, m), where cnt = m − d for d > 0 and |d| for d < 0.
- The overlap offsets satisfy |δ_i| ≤ s − 1. They do not alias once m ≥ 2s − 1, and the motif does not self-wrap.
- The phase is an integer polynomial in m mod 4, so it is periodic with a period dividing 4.
- The author's ranges cover everything below the threshold plus one full period: F1/F2 planes L = 2..12 against threshold 9 (true s = 3, so the threshold is conservative); all-B over m = 1..8.

**Sector factors.** I checked the sector factors (−1)^{f_c L²} for planes, + for the cube, and (−1)^{Σ f_c L³/2} = + for all-B at even L.

**My own code.** `review_scripts/rv_periodicity.py` uses my builders and my conventions, including 3 orderings. It builds the closed form Q(m) from the motif-overlap table, matches it to the direct product at m = 5..10, and gives sign + for every m up to 60 (log `TOTAL: PASS=3 FAIL=0`). Earlier, `rv_ff_relations.log` gave the full pattern directly for L = 3..12 in all 8 sectors.

**Verdict: correct.**

### (3) New or remaining defects

- **N-2 (moderate): F5 has no infinite FF sequence.** BHM needs FF for infinitely many L, and the corner code is certified only for L ≤ 6. Yet §4's Conclusion says "Every listed code has a uniform-in-L gap", and the R7 row says "F5: the certified L". Fix: state that F5 stability is CONDITIONAL on FF(L) along an infinite sequence, which is open. Otherwise prove it with the same relation-basis-plus-periodicity method on the corner complex.
- **N-1 (minor): leftover wording in §4.**
  - The Conclusion paragraph still says "splitting of at most poly(L)·e^{−cL}".
  - The cited-theorem block is still phrased for ‖V‖ ≤ J e^{−μr}.
  - N1 route 3 still says "Excluded by the cited theorem's decay class".

  Make all three conditional on checking the paper, to match the R7 row.

No other new defects.

### Final verdict

**READY for the F1–F4 scope**, once the two wording fixes above (N-1 and N-2) are applied. They are edits to the text and need no new computation. The F5 stability claim stays CONDITIONAL until FF is shown at general L.

Reviewer logs: `rv_main.log` 9/0, `rv_local.log` 3/0, `rv_ff_relations.log` 4/0, `rv_periodicity.log` 3/0. Total **TOTAL: PASS=19 FAIL=0**.
