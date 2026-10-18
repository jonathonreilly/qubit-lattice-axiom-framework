# C6: the emergent-fermion Z2 codes satisfy the BHM hypotheses; stability, topological data, and a scoped no-photon corollary

**Date:** 2026-10-18 · **Block:** C6 of `toe-scale-ladder-20261018` · **Status:** worker output, unaudited, no independent check yet.
**Claim types used below:** `EXACT-PROOF` (a proof valid for all L), `EXACT-CERT` (exact finite GF(2)/Pauli-phase computation at the stated L), `CITED` (a published theorem that is applied, not re-proved here), `CONDITIONAL` (a proved implication from named premises), `POST-HOC` (seen in output first, explained afterwards).
**Novelty:** low. The BHM stability theorem is textbook, and the stabilizer-code TQO conditions are standard. What this block adds is a check of the hypotheses for these specific supplied codes: one homological lemma that covers all five families for every L, exact certificates, and a scoped corollary.

## 0. Supplied codes (named premises; nothing is adopted)

Definitions come from the 2026-10-17 notes and runners. `c6_lib.py` transcribes them, and the corner builder copies the repo runner's code line by line.

| tag | source note (docs/) | qubits/site | generators |
|---|---|---|---|
| F1 | `BKSF_CUBIC_FERMION_CODES_ARE_NOT_ROTATION_INVARIANT_…` and `…BARE_PERMUTATION…` | 3 (edges) | B_v = Z on the 6 edges at v; S_p = ±A A A A, where A_(v,a) = X_e · Z(edges at v ordered before +a) · Z(edges at v+e_a ordered before −a); 720 orderings and 8 sign sectors |
| F2 | `BKSF_CUBIC_FERMION_CODES_SITE_LOCAL_REALIZATION_…` | 6 (half-edges) | B_v, R_(v,a) = Z Z, and S_p with A = X X · Z-tails |
| F3 | `MAJORANA_PER_DIRECTION_…` | 3 (6 Majoranas γ_{v,d}) | B_v = (−i)^3 γ_0…γ_5; S_p = ± ∏ of A_(v,a) = γ_{v,+a} γ_{v+e_a,−a}; 8 sign sectors |
| F4 | `SPINFUL_MAJORANA_PER_DIRECTION_…` | 5 (6 link + 4 matter Majoranas) | D_v (total parity), P_up, P_dn, and W_p = ± ∏ u_e |
| F5 | `CORNER_FERMION_QUBIT_CODE_GENUINE_CUBE_ROTATION_ACTION_…` | 48 | B_q, R = ZZ, and loops i^n F ∏A on squares, triangles, tubes and plaquettes; 16 uniform flux patterns |

Conventions: the on-site Jordan–Wigner choice (F3, F4) and the sign labels of the 8 sectors may differ from the repo runners by an on-site Clifford or a relabeling. Those changes preserve supports, so they do not affect TQO, k or statistics. Hamiltonian: H0 = Σ_g (1 − g)/2 over the listed generators. It is a sum of commuting projectors with gap 1.

## 1. Results

| # | statement | type |
|---|---|---|
| R1 | **Lemma 1 (homological TQO).** For every family, every cube B whose W-enlargement does not wrap the torus, and every L: a Pauli operator supported in B that commutes with all generators is, up to phase, a product of generators supported in B+W. W = 2 for F3–F5 and W = 3 for F1–F2, measured in sites. | EXACT-PROOF (§2); EXACT-CERT for cube sides 1–4 (1–3 for corner), 23 cases |
| R2 | **TQO-1 on the torus.** No nontrivial logical operator is supported in any cube of side ≤ L−1. The full torus carries all 2k independent logicals. | EXACT-CERT, L = 2..6, all five families, 30 cases (cleaning-lemma count); EXACT-PROOF via R1 for side ≤ L − 2W − 1 |
| R3 | **GSD(L).** k = log2 GSD = 3 for F1, F2 and F5 at every L tested, and for F3 and F4 at even L. F3 and F4 have k = 2 at odd L. **The GSD does not grow with L, so there is no fracton behaviour.** | EXACT-PROOF for k ≤ dim H_1 = 3 (§3); EXACT-CERT for 422 (code, L) cases, L = 2..8 (corner 2..6); the odd-L value 2 is POST-HOC (§3) |
| R4 | **Frustration-freeness** (−I ∉ S, phase-tracked). It holds for every sign sector of F1–F4 and every corner flux pattern at all even L tested. The flux-0 sectors of F1–F4 are frustration-free at all L tested. At odd L the π-flux sectors are frustrated (−I ∈ S). For the corner code, only the patterns with square = plaquette flux are consistent at L = 3. | EXACT-CERT, L = 2..8 (F1 for 2 orderings at L = 7, 8; F1 for all 720 orderings at L = 4); **not proved for general L** |
| R5 | **Logical algebra (even L).** Three straight strings (products of A along noncontractible lines) and three membranes commute with S, are independent, and pair as the identity matrix. Translates of each are equivalent mod S. **Distance d ≥ L** for F1–F4 at even L ≥ 4; d ≤ (minimal string weight). | EXACT-CERT at L = 4, 6; d ≥ L is CONDITIONAL on R5 holding for that L (§3) |
| R6 | **Point-charge self-statistics.** For F1, F2, F3 and F4, the Kitaev hopping test (single hops) and the straight-leg Levin–Wen T-junction (legs of length 3) give exchange sign −1 for all 20 direction triples. All 720 F1 orderings give −1. The corner code gives −1 in all 240 (corner, triple) cases. The sign is unchanged under random stabilizer dressing of the legs. The untwisted toric-code control gives +1. **The charge is a fermion.** | EXACT-CERT |
| R7 | **BHM stability** (§4). Under any finite-range (or exponentially decaying) perturbation V of strength J ≤ J0, where J0 does not depend on L, the spectral gap stays ≥ 1/2 uniformly in L. The 2^k ground states split by at most poly(L)·exp(−cL). No cubic covariance is needed. | CITED theorem + R1–R4 → CONDITIONAL on FF(L) along the chosen sequence of L |
| R8 | **Persistence of topological data.** Inside the stable region the phase is a 3D Z2 gauge theory with an emergent fermionic point charge, a Z2 flux loop, mutual braiding −1, and GSD 8 on T^3 (even L). | CITED (quasi-adiabatic continuation; invariance of statistics under locality-preserving unitaries) applied to R5–R6; not re-proved |
| R9 | **Corollary (scoped no-go).** For J ≤ J0, H0 + V has no gapless excitation. In particular it has no emergent photon and no massless fermion. | CONDITIONAL on R7 (§5, No-Go Discipline Gate) |

Certificates: `logs/c6_tqo_runner_full.log` (`TOTAL: PASS=18 FAIL=0`), `logs/c6_complex_homology_check.log` (`TOTAL: PASS=3 FAIL=0`), and the combined `logs/C6_SUMMARY.log`.

## 2. Lemma 1 and its proof (valid for every L and every cube size)

Notation: a Pauli is identified, up to phase, with its GF(2) vector; ω is the symplectic form. For a cell complex X with vertices V, edges E and 2-cells F, ∂ and δ are the boundary and coboundary maps over GF(2).

**Topological input (T).** For X the cubic complex of Z^3, or the corner complex (§2.3), and any cube B:
- (T1) every 1-cycle supported in B is ∂ of a 2-chain supported in B+1;
- (T2) every 1-cochain supported in B that is closed (vanishes on every ∂f) equals δφ for a vertex function φ supported in B+1.

The same holds on the torus whenever B+1 does not wrap.

### 2.1 Edge-type codes (F1; F2 and F5 with repetition halves)

Hypotheses, which hold by construction (see the builder code):
- (H1) one qubit per edge;
- (H2) B_v = Z on the edges at v;
- (H3) A_e = X_e · Z(t_e), with any Z-tail t_e;
- (H4) each loop stabilizer has GF(2) vector Σ_{e∈∂f} vec(A_e).

Let x be supported in B and commute with all generators.
1. Write x = A(a)·Z(b′), where a is the X-part of x. This is possible because A_e carries X exactly on e.
2. ω(x, B_v) = |a ∩ star(v)|, so ∂a = 0. By (T1), a = ∂c with c in B+1.
3. Then x′ = x · ∏_{f∈c} S_f is a pure Z(b) supported in B+1, with tails at most one site out.
4. ω(Z(b), S_f) = Σ_{e∈∂f} b_e, so b is closed. By (T2), b = δφ.
5. Then Z(b) = ∏_v B_v^{φ_v}, with φ supported in B+2.

So x ∈ ⟨generators in B+W⟩. Every step is linear and local; no ordering or twist was used. The twist only fixes signs and statistics.

**Repetition halves (F2, F5).** R_e = Z_{h1} Z_{h2}, and A_e has X on both halves. Commuting with R forces equal X on both halves, so the X-part is again some A(a). In step 4, the closed cochain is b_e = b_{h1} + b_{h2}. After dividing by ∏B^φ, what remains has b_{h1} = b_{h2} on links and b = 0 on single-qubit edges, so it is a product of R's.

### 2.2 Majorana-type codes (F3, F4)

Per site, 3 qubits ≅ 6 Majoranas. The Pauli group mod phase is F2^{6/site}, with ω(x, y) = Σ_v (|x_v||y_v| + x_v·y_v). Then:
- ω(x, B_v) = |x_v| (because 6 is even), so every site of x is even;
- for site-even x, ω(x, A_(v,a)) = x_{v,+a} + x_{v+a,−a} =: y_e.

Proof:
1. Commuting with every S_p means δy = 0. By (T2), y = δφ.
2. x + Σ φ_v B_v has y = 0, so it equals Σ z_e A_e. Site-evenness gives ∂z = 0.
3. By (T1), z = ∂c, so x ∈ span{B, S} inside B+1.

**F4.** Commuting with P_up and P_dn forces matter bits to come in pairs. Dividing by P's removes the matter content, and D_v plays the role of B_v. The argument then reduces to F3.

### 2.3 Topological input (T) for the corner complex (proof for all sizes)

The complex: each site carries a cuboctahedron (12 corners, 24 edges, all 14 faces filled: 6 squares and 8 triangles). Each lattice edge carries a "tube" of 4 rectangles, each made of 2 links and 2 on-site edges. Each lattice plaquette carries a 4-link cell.

**(T1).** Let z be a cycle in B.
1. Using the tube rectangles, slide all links on a tube onto one representative link. The coefficient left on that link is the tube's link parity n_e.
2. n is a cubic 1-cycle, since the link endpoints must close up at each site. So n = ∂c in the cubic complex.
3. Subtract the corner plaquette cells of c. Each covers its 4 tubes once. Re-slide; now every tube carries an even number of links, and these cancel.
4. What remains lies on single sites. It is a cycle on the cuboctahedron, i.e. on a 2-sphere with all faces filled, so it is a boundary.

All moves stay inside B+1.

**(T2).** By (T1), b sums to zero around every closed loop in a contractible neighbourhood U ⊇ B+1. So φ(q) = Σ b along any path from a base point outside B is well-defined, and φ is constant (choose 0) on the connected set U∖(B+1).

The repo runner reproduces both properties by direct GF(2) homology (cubic sides 1–5, corner sides 1–4). This is a different computation from the Pauli-rank counting (`c6_complex_homology_check.py`).

## 3. Consequences on the torus T^3_L

- **TQO-1.** A cube of side r with r + 2W + 1 ≤ L sits in a non-wrapping neighbourhood, so R1 makes every commuting Pauli on it a stabilizer. This holds for all L: TQO-1 with L* = L − 2W − 1 = Θ(L). The exact count (cleaning lemma: dim logicals in M = 2|M| − dim S|_M − dim S + dim S|_{M^c}) is sharper, giving L* = L − 1 for every case with L ≤ 6.
- **Bound on k.** Running the proof globally, x ↦ ([z], [y]) ∈ H_1(T^3) ⊕ H^1(T^3) is injective on C(S)/S, and the B-shift ambiguity is accounted for below. So k ≤ 3 for every L. Strings realize all of H_1 and membranes all of H^1 at even L, which gives k = 3 there. The certificates confirm this.
- **Odd L for F3/F4 (POST-HOC).** The output k = 2 was seen first. Explanation: Σ_e y_e = Σ_v |x_v| = 0 for site-even x, and the parity of y is a class invariant (each vertex has degree 6). So only even-parity H^1 classes are realized; at odd L the plane-dual class has parity L^2 ≡ 1. Dually, Σ_v B_v = Σ_e A_e makes s_x s_y s_z trivial. This leaves a 2+2-dimensional logical group, so k = 2. **The GSD is bounded in L in every case (8 or 4); none of these codes is fracton-like.**
- **Distance (even L).** Every nontrivial logical anticommutes with some string or membrane, because the pairing is the identity. Then it anticommutes with all translates, which are equivalent mod S. For F1–F4, membranes in different planes have disjoint supports, which gives L of them. Strings ≥ 2 apart transversely are disjoint, which gives ⌊L/2⌋² ≥ L. Hence d ≥ L. The equivalence of translates is certified at L = 4, 6. For general even L it follows from injectivity of the class map, because a translation preserves homology classes; this step is argued, not machine-checked. The corner code's distance is not bounded separately; R2 is what BHM needs.
- **R4 caveat.** Frustration-freeness is certified only at L ≤ 8 (corner ≤ 6). The pattern (π-flux sectors frustrated exactly at odd L) fits a sign (−1)^{flux·L²} on the global plane relations. A proof would have to show that the relation module is generated by local cube relations, whose sign does not depend on L, plus the plane relations. This is not done.

## 4. Applying Bravyi–Hastings–Michalakis

**Cited theorem.** Bravyi, Hastings and Michalakis, J. Math. Phys. 51, 093512 (2010); with Bravyi–Hastings, CMP 307, 609 (2011); and Michalakis–Zwolak, CMP 322, 277 (2013) for the frustration-free / local-gap generalization. The theorem is stated here from memory, because there was no network access in this session; its exact constants were not re-read. Setting:
- H0 = Σ Q_A, a sum of commuting projectors of bounded range on a D-dimensional torus, frustration-free with gap 1;
- H0 satisfies TQO-1 (P O_A P = c(O_A) P for O_A on cubes of side ≤ L* with L* ≥ L^α) and TQO-2 (the same statement with the local ground projector of A's enlargement).

Conclusion: there exist J0 > 0 and c > 0, depending on D, range, α and the decay rate but not on L, such that for any V = Σ V_{x,r} with ‖V_{x,r}‖ ≤ J e^{−μ r} and J ≤ J0:
- the spectrum of H0 + V splits into a band of 2^k levels of width ≤ poly(L)·e^{−c L*};
- the rest of the spectrum lies a gap ≥ 1/2 above that band.

**Checked hypotheses.**

| hypothesis | where it is checked |
|---|---|
| commuting projectors, bounded range | §0; R4 commutation check over all generator pairs sharing a qubit |
| frustration-free | R4, for the stated (sector, L) |
| TQO-1 | R1/R2, with L* = Θ(L) (α = 1) |
| TQO-2 | R1 is exactly the stabilizer form: P_{B+W} O_B P_{B+W} ∝ P_{B+W} |

BHM's unit enlargement is reached by coarse-graining into blocks of W sites, which is standard.

**Conclusion (CONDITIONAL on FF(L) along the sequence of L used, e.g. even L for every sector).** Every listed code has a uniform-in-L gap and a ground-space splitting of at most poly(L)·e^{−cL} under every sufficiently small finite-range qubit perturbation. The perturbation may break cubic, translation and fermion-parity symmetry. J0 is not computed; BHM's constants are not explicit enough to quote.

**Topological data that persist** (R8; CITED, conditional). Hastings–Wen quasi-adiabatic continuation (PRB 72, 045141 (2005)) and Bachmann–Michalakis–Nachtergaele–Sims (CMP 309, 835 (2012)) give a locality-preserving unitary from the unperturbed to the perturbed ground band. Such a map preserves superselection sectors, fusion, the exchange statistics of point particles, and charge–loop braiding. So the persisting data are those of R5/R6:
- a Z2 point charge with θ = π (a fermion);
- a Z2 flux loop;
- mutual braiding −1;
- GSD 8 on T^3 at even L (4 for F3/F4 at odd L).

This is the 3D Z2 gauge theory with a fermionic charge, distinct from the bosonic 3D toric code. The statement that the perturbed charge stays a fermion uses the cited invariance; it is not re-proved here.

## 5. Corollary and No-Go Discipline Gate

**Corollary (CONDITIONAL on R7).** Fix any code in §0 and any (sector, L-sequence) where FF holds. For every Hermitian perturbation V of range ≤ r0 and strength J ≤ J0(code, r0), uniform in L, the spectrum of H0 + V above the 2^k-level ground band has a gap ≥ 1/2. Hence there is no gapless excitation in this region: no emergent U(1) photon, no massless (Dirac or Weyl) fermion, and no gapless gauge mode.

**Route pruned.** The route is: "start from one of these Z2-fermion codes, add small local terms, and obtain QED (photon plus massless charged fermion) in the same phase". It is closed for the family {H0 + V : ‖V‖_local ≤ J0}. Any route to QED from these codes must cross a phase boundary, where the gap closes (in the thermodynamic limit, for some J > J0), or change the premises (§N7).

**Remark on the corner Dirac-pair notes (interpretation).** `CORNER_FERMION_MASSLESS_DIRAC_PAIR_…` and `CORNER_FERMION_LONG_WAVELENGTH_…` study one-fermion band structures with hopping t ~ 1. A linear crossing in a one-particle band is not a gapless many-body excitation, as long as the charge creation cost exceeds the band's depth below its own zero. Inside the BHM region the emergent fermion is massive in the many-body sense. A massless Dirac excitation of the many-body system requires leaving that region. It is not computed here whether the notes' parameters lie inside J0; they are O(1) and not small.

### No-Go Discipline Gate (N1–N8)

- **N1 — routes to QED that this corollary addresses or excludes:**
  1. Small local perturbation of H0. ATTEMPTED: excluded by R7.
  2. Small perturbation that breaks every symmetry (cubic, translation, fermion parity). ATTEMPTED: excluded, since BHM needs no symmetry.
  3. Exponentially decaying rather than finite-range terms. Excluded by the cited theorem's decay class.
  4. Driving the fermion band to a node at zero energy by hopping. Not in the small-J region unless the hopping is below J0, in which case the gap stays. Outside J0: not covered.
  5. Emergent U(1) from Z2 by enlarging the gauge group at small J. Excluded: the flux loop stays gapped and the topological data are Z2 (R8).

  These are five normalized families with distinct mechanisms. Routes **not** excluded:
  - large J or a phase transition;
  - perturbations whose strength grows with L, or which are non-local;
  - adding degrees of freedom (an enlarged Hilbert space, e.g. rotor/U(1) link variables);
  - changing H0 itself (another supplied code);
  - Floquet/QCA dynamics, which are not of the form H0 + V.
- **N2 — walls.** One wall: J ≤ J0. FF(L) is a hypothesis on the L-sequence, not an independent wall on the conclusion. The two are independent: neither implies the other.
- **N3 — hidden conditions.** "As is standard": the coarse-graining in TQO-2 is non-load-bearing, since BHM allow any fixed range. The BHM constants were cited from memory, which is flagged in §4. "By construction" (H1–H4) is checked in code.
- **N4 — residual matching.** BHM's residual is the stability of a gap for commuting TQO Hamiltonians. The residual claimed here is the absence of gapless modes in H0 + small V. They match. Quasi-adiabatic invariance is used only for R8, not for R9.
- **N5 — resolution.** "No gapless excitation" is a statement about the spectrum of the many-body Hamiltonian (lattice-wide). It is not a statement about one-particle bands (per-mode), which the runner does not compute. Runner certificate lines: per_element/per_site/per_block/lattice_wide are given; per_mode is "checked and not executed".
- **N6 — reframes.** None. No new axiom; the codes stay supplied premises.
- **N7 — steelman.** "Emergent photons do exist in 3D lattice models, e.g. quantum spin ice (Hermele–Fisher–Balents 2004), and Z2-to-U(1) transitions are known. A Hamiltonian near the transition might give QED." Correct, but that point is outside the J ≤ J0 domain; the corollary explicitly concedes it. A second objection: "J0 may be so small that the region is physically irrelevant." Also concedes nothing within scope: J0 is not quantified.
- **N8 — earlier claims.** Consistent with the 2026-10-17 notes, which list "gap stability" as not claimed. This block now supplies it, conditionally. No prior wall is contradicted.

Gate status: PASS for the scoped corollary as stated (domain: J ≤ J0, FF along the sequence of L). There are no failure conditions within that domain.

## 6. What needs independent checking (load-bearing)

1. **Lemma 1 / topological input (T) for the corner complex (§2.3).** This is the only step that gives TQO for all L and all cube sizes. The certificates test cube sides up to 4. A reviewer should re-derive the tube-sliding argument and check that the runner's cycle list (cell families) matches §2.3.
2. **The BHM statement (§4), cited from memory.** It needs checking against the paper, including whether TQO-2 is required in the "local ground projector" form verified here.
3. **R4.** Frustration-freeness for general L is unproved.

## Reproduce

```bash
cd .claude/science/physics-loops/toe-scale-ladder-20261018/blocks/C6
python3 scripts/c6_tqo_runner.py           # about 80 s; TOTAL: PASS=18 FAIL=0
python3 scripts/c6_complex_homology_check.py  # about 4 s; TOTAL: PASS=3 FAIL=0
```
