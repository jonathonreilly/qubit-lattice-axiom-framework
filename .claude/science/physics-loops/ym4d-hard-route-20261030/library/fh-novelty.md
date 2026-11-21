# Novelty check: the fine-mesh massive gauge and its Laplacian estimate (cp12 §4, Lemma 6 and Theorem 7)

Written 2026-11-05 by Claude (one session, one reading). Internal note for the owner. Nothing goes outward. Every claim about a source names the lines or the equation. "Read" means I read the passage. "Grep" means I only searched for words.

## Verdict

**KNOWN as a result. Only the proof route is new.**

The estimate in (BGH24) is Balaban's. A field with small curvature and small current has a local gauge on a cube with |A| ≤ Cα/ξ, |∇A| ≤ Cα/ξ² and |ΔA| ≤ Cα/ξ³, with constants that do not depend on the mesh. That is Balaban, CMP 99 (1985) 75–102, **Proposition 6, (1.134)–(1.136), pp. 98–99**. For the background minimiser, the same bounds plus the Hölder bound on ∇A are Balaban, CMP 102 (1985) 277–309, **Theorem 1, (9)–(10), p. 279**. Sussman and Alpoge's own outline states the same result as **Proposition 1a.3.8** (ym4.tex L7724–7730), credited to Balaban. Their complete account cites it, with its hypotheses written out, as **Proposition 4.9:prop-cube-gauge-regular** (CA-I L35202–35266).

So the sentence at SA L12773–12775 marks the scope of that subsection only. It does not mark a gap in their text: the supply of (BGH24) is their Proposition 1a.3.8.

Our Theorem 7 is also weaker than Proposition 6 as a statement. It assumes a C¹ gauge g₁ (cp12 (8); draft (F3)), and Proposition 6 constructs that gauge. What we have not found anywhere is our proof of the upgrade step. Our proof builds the gauge by a single-scale fixed point in a massive Landau gauge, div A₂ = −ξ⁻²Ψ₁(λ)λ, and gets mesh-uniformity from SA's explicit heat-kernel resolvent. It uses no averaging operators, no induction over scales, and no Balaban propagators.

## 1. Our result and the sentence in SA

- **cp12.md L174–343 (read).**
  - Hypothesis (8): |∂U−I| ≤ εη²ξ⁻², |J(U)| ≤ εξ⁻³, and a given real gauge g₁ with |A₁| ≤ aξ⁻¹ and |∇A₁| ≤ aξ⁻².
  - Lemma 5 is SA BGH2–BGH23, rebuilt.
  - Lemma 6 (L249–294) constructs λ by the fixed point (14), using R_μ with μ = ξ⁻¹. The result satisfies div A₂ = −ξ⁻²Ψ₁(λ)λ and |∇div A₂| ≤ Caξ⁻³.
  - Theorem 7 (L296–337) gets |Δ_ηA₂| from (16)–(18), using Δ = δd + ∇div, the current, and the plaquette logarithm. It then bootstraps ∇A₂ by (19) and applies (10).
  - L341–343: only the real clause of (H) is supplied. The complex part, the current supply and RCG4's F0 premise stay imports.
- **gates/cp12-gate.md (read).** Lemmas 5–6 and Theorem 7 are confirmed, with mesh-free constants and the real clause only. The check was done by one fresh Claude session.
- **cp12-draft.md L321 (read).** It claims: "§9.3 is new … the step SA 12774–12775 leaves open." **This claim is wrong as written** (see §2–§4 below) and should be narrowed.
- **The source of g₁ (read).** pr-lay.md L230–240 (Q, (18)) says it is "precisely ST1's RCG4 import, from a1-balaban §3.8, conditional on F0". a1-balaban.md L568–572 credits CMP 99 75–102, (1.128)–(1.138), which is Proposition 6. So our own C¹ input is the first-order part of the Proposition that already contains the second-order bound.
- **Our own port already says this.** a1-balaban.md L208–215 (read): G99.F, "Section F, in particular Proposition 6, the local gauges (1.135)–(1.136) … a regular field has a small local potential with first, Hölder, and second-difference bounds".
- **SA ym4.tex L12385–12800 (read).** BGH1–BGH23 are the scalar estimates. BGH24 (L12757–12762) is a hypothesis ("Suppose a local real gauge has supplied a potential …"). L12773–12775 is the sentence in question. BGH26–BGH30 (L12797–12858) use only a C¹ bound on the background potential A₀ for the response.

## 2. Sussman and Alpoge: the outline, the complete account and YM3

Searched with grep: Coulomb, Landau, H\"older, Schauder, Uhlenbeck, "massive gauge", BGH, mesh-uniform, "uniformly in the mesh", "fine mesh", "nonlinear Laplacian", \Delta_\eta A, divergence-free, div, "regular gauge", axial, B-CMP99a, Proposition~6.

- Counts in CA-I/II/III and YM3_I: **0** hits for Schauder, Uhlenbeck, "massive gauge", BGH, "mesh-uniform", "nonlinear Laplacian". CA-I has 1 hit for Coulomb (L45132, an unrelated re-blocking route). Neither the account nor YM3 contains our massive-gauge fixed point (grep).

**Outline (ym4.tex), read:**
- L7154: the class 𝔘_k(Ω_•,α) = {|∂U−1| < αη²ξ_j⁻², |J(U)| < αξ_j⁻³}. These are our first two hypotheses in (8).
- L7705–7720: Theorem 1a.3.6, the axial-to-Landau theorem (Balaban's Theorem 2 in "scheme c"). Its bounds are |A|_(−1), |∇A|_(−2), |D*DA|_(−3), |ΔA|_(−3) ≤ B₁(α₀+α₁), and the theorem "satisfies Hölder bounds on ∇A". Its hypotheses rest on Lemma 1a.3.2 "[to be proved; Package A]". For SA's own average M, L7720 states only the ‖A‖₁ and |D*DA|_(−3) bounds.
- L7722: Proposition 1a.3.7 (a priori bounds) is elliptic regularity through 𝖦_k(U₀). Its sketch is at L7904.
- **L7724–7730: Proposition 1a.3.8, "regular means small potential, locally".** For U ∈ 𝔘_k on a cube of side Mξ_j it gives ξ_j|A|, ξ_j²|∇A|, ξ_j³|D*D A|, ξ_j³|ΔA| ≤ CMα₀. This is (BGH24). The sketch at L7911 says: "Only propagators at **1** enter".
- L7763: Proposition 1a.3.12 flags that Balaban's Theorem 8 asserts the second-order and Hölder bounds without proof when RD*A = f, f ≠ 0.
- L3815–3824: the open obligation SA name is the background orbit "behind the local assertions numbered 1a.3.6, 1a.3.8". It is not the gauge estimate.

**CA-I, read:**
- **L35202–35266:** Proposition "Balaban's cube gauge for regular fields [CMP99a, Prop. 6, (1.135)–(1.136)]". The hypotheses are the curvature bound and the current bound |D*_{U₀}∂U₀| < α₀η²(L^jη)⁻³. The conclusion bounds L^jη|A|, (L^jη)²|∇A|, (L^jη)³|∂*∂A| and (L^jη)³|Δ^ηA|, each by less than 7dL²B₁M*α₀, with ordinary finite differences. The text then sketches Balaban's proof (Theorem 4 applied to the pair 1, U₀″). The account cites the result; it does not reprove it.
- **L11690–11718:** the same Proposition quoted verbatim. It notes that (1.9) is "the second-order condition", which a first-order factor need not satisfy.
- L12739–12756: the norm N_β(A) includes the Hölder seminorm of ∇_U A, via CMP 99b (3.40).
- L13596–13616 and L13840–13870: the Hölder members come from CMP 99b (3.42)–(3.47), Theorem 3.3.
- L14711–14760: Lemma "Linear bounds on the background potential": N_β(𝓗^J(B)) ≤ C|B|, from CMP 102b (133)–(136).
- L13342–13355: the background's Hölder norm on the window is Balaban CMP 109 (3.27).
- L157462–157469: Balaban's Theorem 2 with (1.36)–(1.39) and B₂(β₀).

**CA-II, read:**
- **L18877–18927:** Remark "No Hölder bound off the regular region". Balaban's Hölder bound is CMP 109 (4.18)/(3.32), obtained from (3.27) for the minimiser. None of the regularity conditions CMP 109 (1.11)–(1.16), CMP 119 (2.34)–(2.39) or CMP 122a (1.64)–(1.69) "contains a Hölder clause". Our theorem does not touch this: raw configurations have no small current.

**CA-III, read:**
- L35166–35336: Lemma 9.3:lem-gauge-fixing. This is CMP 99a Theorem 4 with (1.9) replaced by a divergence-form current bound. It gives first-order bounds only (eq. 9.3:eq-gauge-fixing-1).
- L35325–35333: it records Balaban's unproved Hölder-regularity generalisation (CMP 99a (1.147)).

**YM3_I, read:**
- **L20755–20790:** Theorem I-28-75 (3D). Curvature and current bounds |∂U−1| < αη² and |D_U^T∂U| < αη² give a real gauge with |A₀|, |∇^ηA₀| and |D₁^TD₁A₀| < B_*lα. The gauge is built by smoothing a comb section. It is SA's own averaging-free construction. It bounds curl-transpose-curl, not ΔA₀, and it gives no Hölder bound in that theorem (L20831–21184 scanned: no Hölder or Laplacian conclusion on A₀).
- I found no 4D analogue of this construction in ym4.tex or CA-I/II/III (grep "comb section", "smoothed section": 0 hits).
- L10428 ff.: interior scalar estimates in 3D, the analogue of BGH.

## 3. Balaban (OCR text; formulas garbled in places; check against the PDF before quoting outward)

- **CMP 99a (75–102), read L1–160, L395–790, L1240–1380, L1428–1490.**
  - The class U_k is defined by (1.7)–(1.9). In the OCR the formula of (1.9) is lost. The surrounding text says it is gauge invariant through D*_U ∂U (L139–143). CA-I L35212–35216 gives it as |D*_{U₀}∂U₀| < α₀η²(L^jη)⁻³, the current. L1466–1468 calls (1.9) "a strong assumption … satisfied by solutions of the variational problem".
  - **Theorem 2 (L452–458)** gives conditions (1.36)–(1.39). (1.36) carries constants B₁ and B₂(β₀); B₂(β₀) is the Hölder constant (Proposition 3, L691–696: "B₂(β₀) = 5dLB₀(β₀) … the corresponding norms of G(U₀), H(U₀)"). (1.39) is |D*DA|, |ΔA| ≤ B₁(α₀+α₁)(L^jη)⁻³ (L446–447, garbled).
  - The gauge is Landau with averaging constraint: R(U₀)D*A = 0, Q_j(U₀,ηA) = B (L437–440).
  - The mechanism matches ours (L470–696). The "basic estimate" (1.54) writes D*∂U₁U₀ = D*∂U₀ + iη²D*DA + O(…). Hence J = D*DA is small in |·|_(−3) (1.55). Then A = G(U₀)J + G(U₀)ΣQ*… B₁ (1.58), and the bounds follow from the propagator bounds of CMP 99b Theorem 3.3 (1.59)–(1.62).
  - Proposition 3 (L691) needs only a sup bound |A| < α₂(L^jη)⁻¹ in the slice.
  - **Proposition 6 (L1340–1372, (1.134)–(1.138), pp. 98–99):** on a cube □ of side ML^jη inside a regular region there is a gauge u on □̃ with L^jη|A|, (L^jη)²|∇^ηA|, (L^jη)³|∂^{η*}∂^ηA|, (L^jη)³|Δ^ηA| < 7dL²B₁Mα₀, and Rd^{η*}A = 0. Derivatives are taken "without any external gauge field configuration" (L1370–1372). The proof applies Theorem 4 to the pair (1, U₀″) (L1346–1349). So only flat propagators with averaging enter.
  - The constants depend on d and L only (L455–458). They do not depend on η or k, so the result is mesh-uniform.
- **CMP 102 (277–309), read L60–110 and L1095–1126.** **Theorem 1, (9)–(10), p. 279:** for minimal configurations, on each cube of the class there is a gauge with |A| < B₃Mε₁(L^jη)⁻¹, |∇A| < B₃Mε₁(L^jη)⁻², ‖A‖_{1,β} < B₄(β₀)Mε₁(L^jη)⁻²⁻β for 0 ≤ β < β₀ = 1, and |∂*∂A|, |ΔA| < B₃Mε₁(L^jη)⁻³. Proposition 8 and (167)–(169) (pp. 304–305) prove it.
- **CMP 99b (389–434), read L425–600.**
  - The regularity class (3.35)–(3.36) asks for local gauges with |A| ≤ O(1)Mα₀(L^jη)⁻¹ and |∇A| ≤ O(1)Mα₀(L^jη)⁻², and |d*dA| ≤ O(1)Mα₀(L^jη)⁻³.
  - Theorem 3.1 (3.42)–(3.47) has Hölder bounds (3.43) ‖ζ∇G′λ‖_β with B₀(β), β < 1. Theorem 3.3 gives the same for G(U). These are the mesh-uniform propagator Hölder bounds behind (1.36).
  - L465–469: "We will prove in another paper" that (3.37)–(3.38) imply (3.35)–(3.36). That is CMP 99a §F.
- **CMP 89, 95, 96, 98, 109, 119:** I did not read them for this question. CMP 109 (3.26)–(3.32), (4.17)–(4.18) carry the background Hölder norms; I know this through CA-I L13342–13355 and CA-II L18889 (read).
- **Gauge, smallness and mesh.** Balaban's gauge is a generalised Landau gauge with averaging constraint, reached from an axial gauge. The smallness is α₀ (curvature and current) with 7dL²Mα₀ ≤ c₁. The bounds are uniform in η = L⁻ᵏ.

## 4. Published literature (web search; abstracts and listings only)

- Balaban CMP 99 (1985) 75–102 and CMP 102 (1985) 277–309: closest, and contain the result (§3).
- I. Chevyrev, "Yang–Mills measure on the two-dimensional torus as a random distribution", CMP 372 (2019), arXiv:1808.09196. It uses a Landau-type gauge on lattice approximations with Hölder-type bounds in 2D. Probabilistic setting, not our estimate. The listing says extension to d = 3 is open.
- I. Chevyrev, H. Shen, "Invariant measure and universality of the 2D Yang–Mills Langevin dynamic", arXiv:2302.12160. It uses lattice gauge fixing in 2D. The abstract has no Landau/Coulomb Hölder estimate.
- A. Chandra, I. Chevyrev, "Gauge field marginal of an Abelian Higgs model", arXiv:2207.05443. It gives Hölder–Besov moments uniform in the spacing, in 2D, abelian, in a fixed gauge.
- J. Dimock, "The renormalization group according to Balaban" I–III (arXiv:1108.1335, 1212.5562, 1304.0705). These are scalar expositions. Dimock's QED papers (math-ph/0210020, arXiv:1512.04373) are abelian. I did not check their gauge lemmas.
- No paper found that proves a deterministic lattice Coulomb or Landau gauge with Schauder/Hölder estimates uniform in the mesh for non-abelian fields in 4D, other than Balaban. The search was a few standard queries, so this is weaker than a read.

## 5. What would be new relative to SA's text

**In one sentence.** A short, single-scale, averaging-free proof: under small curvature, small current and a given C¹ gauge on a cube, a massive Landau gauge correction gives a mesh-uniform bound on Δ_ηA and hence on [∇A]_α. It uses only SA's flat heat-kernel resolvent (BGH2–BGH23), instead of Balaban's averaged Landau slice, his induction over scales and his propagators G(1) with averaging (CMP 95/96/99b).

**Limits:**
- The statement is weaker than Balaban's Proposition 6. It needs g₁ as input, and in our chain g₁ is RCG4, which is Proposition 6's first-order part and stays conditional on F0 (pr-lay L240).
- Real clause only. The complex clause of (H) is not touched (cp12 L343).
- The current bound |J| ≤ εξ⁻³ is an import (cp12 L343). It is also the open item SA name at L3815–3824 (the background orbit).
- It gives nothing off the regular region. CA-II L18877–18927 stands.
- The gain inside our own chain is real but small: the second-order and Hölder clauses no longer depend on F0 or on CMP 99b (3.43). The first-order clause still does.

## 6. What a contribution would need before it is worth sending

1. **Remove the g₁ import.** A 4D, averaging-free construction of the C¹ gauge from curvature and current alone would make the whole local statement an elementary, self-contained proof of Balaban's Proposition 6 (real clause). SA's YM3 Theorem I-28-75 (YM3_I L20766–20790, comb-section smoothing in 3D) is the model to port. With that, the full statement "regular field ⇒ C^{1,α} local gauge, mesh-uniform" would not use F0, which SA's outline also takes from Balaban. That would be worth offering, credited to Balaban for the statement.
2. **State it at Balaban's strength.** Use one cube with the hypotheses of SA's 𝔘_k (L7154), no g₁, and the conclusion of their Proposition 1a.3.8 (L7724–7730) plus [∇A]_α. Compare it line by line with CA-I L35202–35266.
3. **The complex clause.** That is a holomorphic version for complex U = e^{iηA′}U with small A′, as SA need in 1a.3.8's second half (L7730).
4. **Check the OCR.** Read (1.9), (1.36) and (1.136) of CMP 99a and (9)–(10) of CMP 102 in the PDF before quoting them to anyone.
5. **Correct cp12-draft L321.** "§9.3 is new … the step SA leaves open" should read: "a new proof of the second-order and Hölder clauses of Balaban CMP 99a Prop. 6 / SA Prop. 1a.3.8, given a C¹ gauge".
