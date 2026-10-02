**Golterman–Shamir against Variant T: the theorem does not kill it, Variant T does not evade it, and the result turns on one open question**

Golterman–Shamir (GS) do not kill Variant T. Variant T also does not evade them: it satisfies every GS hypothesis it controls. Its fate rests on GS's one conjectural hypothesis, whether the gapped corners' propagator zeros are "kinematical" (removable by adding composite fields). Nothing was run or written. Labels are EXACT (proof here), CHECKED (finite hand check), ARGUED (reasoning) and LIT (fetched text, never a premise).

**Sources fetched.** Full text of the GS proceedings (arXiv:2603.15985). Sections I, III, IV and Appendix B.2 of their predecessor paper (arXiv:2505.20436 v3, PRD 113, 014503). Abstracts of the GS PRL (arXiv:2311.12790), Zeng–Xu–Lu–You (arXiv:2405.05339) and Flores-Calderón–Hooley (arXiv:2410.22173). I read everything in c7/hard as instructed. The copyright rule allows one quotation in this whole report, so it is used once, in §1.

## 1. The GS theorem (LIT)

**The constructed Hamiltonian.**
- Take a set of interpolating fields Ψ_a: elementary fields plus local composites.
- Form the retarded anticommutator R_ab(x,t) = iθ(t)⟨0|{Ψ_a(x,t), Ψ_b†(0,0)}|0⟩ and Fourier transform it.
- Set 𝓡(p) to its value at ω = iε as ε → 0, and define H_eff(p) = 𝓡(p)⁻¹.
- For a free Hamiltonian this reproduces the Bloch Hamiltonian, provided every field in H is in the set.

**Singularities of 𝓡.**
- A *primary singularity* is where 𝓡 → ∞. It needs a massless single-particle state, and there H_eff has a zero eigenvalue.
- A *secondary singularity* is non-analytic but finite. It comes from intermediate states with three or more massless particles.

**Complete set.** In a given charge sector:
- the massless asymptotic states correspond one-to-one with the primary singularities; and
- 𝓡 has no zeros.

**Zero types.** GS contrast "kinematical" with "genuine"; "dynamical" is not their term.
- *Kinematical:* a zero of 𝓡 that appears because just one chirality of a massive Dirac fermion is interpolated. Adding a composite for the other chirality removes it. Their natural candidate is B_i ∝ ∂H_int/∂χ_i†.
- *Genuine:* a zero that survives every choice of fields. H_eff then has a pole, which GS read as ghost states and lost unitarity. They argue it is unlikely when H is local, but this is not proved.

**Theorem (2505.20436, §III).** Start from a regular spatial lattice with a compact global symmetry G, not spontaneously broken, whose generators have discrete eigenvalues. Assume:
1. H has finite range and contains fermion fields alone.
2. The continuum limit is free, relativistic massless fermions, with no massless bosons.
3. Every charge sector holding a massless fermion admits a complete set with no zeros in 𝓡.

Then H_eff satisfies the Nielsen–Ninomiya (N-N) hypotheses:
- it lives on the Brillouin zone;
- it is Hermitian (their App. B.1);
- it is analytic away from degeneracy points (B.3, via edge-of-the-wedge, using B.2 locality: the density is a finite sum of finite products of fields with bounded support);
- it is C¹, in fact C², at primary singularities (EFT argument: the least-irrelevant operator has dimension n ≥ d+2).

So the massless spectrum is vector-like, charge sector by charge sector.

**Two further GS results.**
- *Section IV:* under a uniform strong-coupling limit, a canonical subset ξ of fields absent from H_int decouples and is vector-like.
- *Proceedings:* GS note that in this analysis "anomalies appear to play no role".
- *PRL abstract:* once gauged, zeros act as coupled ghosts, generate the same anomaly as poles, and unitarity is lost.

## 2. Applying it to Variant T

### 2a. Hypothesis audit

| GS hypothesis | Variant T | Label |
|---|---|---|
| Regular lattice, translations | full Z³ | EXACT by construction |
| Compact unbroken G with discrete charges | on-site Spin(10). The 16 is complex, so the weight sectors μ ∈ wt(16) contain no 16̄ | EXACT; "unbroken" is the SMG premise |
| (1) Finite range, fermions alone | 27-site composites with Ω + λC₂; meets App. B.2 locality | EXACT |
| (2) Free relativistic continuum | every light leg carries I(q) = O(q^{2R}), so interactions are irrelevant | EXACT diagrammatically, if Σ̃ is bounded |
| C¹ at light corners | corner lemma plus Σ = O(q^{4R}) | EXACT, if Σ̃ is bounded |
| (3) Complete set (kinematical zeros) | not determined | open |

The corner zero-mode lemma and the factorised self-energy place Variant T inside GS's class; they do not reach hypothesis (3). H_eff is translation-invariant by construction. It is analytic away from degeneracy points by GS's locality appendix, and C¹ at the light corners. Taking ψ alone, H_eff has poles at the gapped corners, so N-N cannot be applied to ψ by itself. Whether it can be applied to the full H_eff is exactly hypothesis (3).

### 2b. Structural facts

**F1 (EXACT): the equation of motion contains the GS bound-state field.**
- From D3: [H, ψ_k] = H₀(k)ψ_k + Σ_n I_n(k) B^[n]_k, where B^[n] = ∂H_int/∂Φ^[n]†.
- This B^[n] is exactly GS's candidate partner field, and it enters with weight I_n(πn) = 1 at its own corner.
- So Variant T contains nothing that blocks the kinematical mechanism.

**F2 (EXACT): the light corners decouple exactly.**
- Set E_c = 0. Then ψ_{πe_a}(t) = ψ_{πe_a} for all t.
- ψ_{πe_a} anticommutes with every Φ and Φ†. So for any odd operator O built from Φ and Φ†, {ψ_{πe_a}, O†} = 0, and the retarded function R_{ψO}(πe_a; t) vanishes identically.
- For a general O, R_{ψO}(πe_a) is a pure pole with a static residue.
- The light-corner mode is therefore an exact free particle with residue 1, at every coupling, on every even torus.

**F3 (EXACT, if 𝓡_ψψ is continuous and invertible off isolated singular sets): the gapped zeros carry the cancelling winding.**
- 𝓡_ψψ(k) is Hermitian. On slices k₃ = const that avoid singular points, its negative-eigenvalue bundle has a Chern number, which is 2π-periodic in k₃.
- So poles and zeros together carry total winding zero in each Spin(10) weight sector. This is the Volovik/Gurarie count, and 𝓡_ψψ⁻¹ is the Wang–Zhang topological Hamiltonian.
- The light poles carry −3 per weight, so the zeros of the gapped set must carry +3.
- Each zero inherits its corner's chirality: near a Dirac-paired corner, 𝓡_ψψ ≈ χ_n σ·q/m², which points the same way as the free pole χ_n σ·q/q².
- Check: (+1) + (−1) + 3·(+1) = +3. CHECKED.
- This matches Flores-Calderón–Hooley's statement that an isolated zero inherits the pole's topological charge (LIT). Their example uses a k-local, real-space-nonlocal interaction.

**F4 (EXACT): the GS partner must sit at the light corners (O-parity lemma).**
- An orbit of the proper octahedral group O on T³ has size 24/|Stab|. It is odd exactly when |Stab| is 8 or 24.
- Such a stabilizer contains a C₄ and a perpendicular C₂, which forces k ∈ {0, π}³. So every non-corner orbit has even size.
- Proper rotations preserve Weyl charge.
- Now assume hypotheses (1)–(3) with the five gapped corners 𝒢 really gapped, so 𝒢 has no primary singularities. N-N gives 3w₁ + (even) = 0, so w₁ is even.
- ψ contributes −1 at each light corner. Hence each light corner also hosts an odd net number of massless opposite-chirality composites, which by Spin(10) form at least one full 16 per corner.
- By F2, ψ is exactly massless at q = 0, so the partner and ψ form a massless Dirac pair. Their mixing is O(q^{2R}), which is irrelevant.
- So Variant T cannot fail in the Golterman–Petcher–Rivas way (a light Dirac mass). If it fails, it fails through massless partners. One example interpolator is the composite {ē_b, ē_c, 111}, whose momenta sum to πe_a (CHECKED).

### 2c. Are Variant T's zeros kinematical?

This cannot be decided on paper. It is a two-way fork.

**Branch K (kinematical, GS's conjecture).**
- F4 applies: the result is three massless Dirac 16s, so the spectrum is vector-like and Variant T fails.
- It requires exactly massless three-fermion bound states of gapped constituents. Nothing protects them except H_eff topology; anomaly does not, since the light set is anomaly-free.

**Branch G (genuine).**
- The mirror-triplet zeros, net +3 per weight, cannot be removed by any finite set of local composites. Hypothesis (3) fails and the 2505 theorem does not apply.
- The cost is the PRL claim that such zeros act as ghosts once gauged.
- ARGUED: a unitary lattice Hamiltonian with on-site gauging has no negative-norm states, so "ghost" must describe the effective theory.
- Zeng–Xu–Lu–You find no sub-gap optical conductivity in SMG insulators (LIT). GS cite this as support for kinematical zeros, but it fits non-removable, non-ghostly zeros equally well. The literature has not settled this.

**On the index question.** F3 is the forced count. It shows chirality is not a topological property of ψ's two-point function. Whether that makes the chirality "illusory" as a physical statement is exactly the K-versus-G fork, because zeros are not states.

**GS §IV strong-coupling decoupling does not apply (EXACT).** No canonical field subset is absent from H_int. The modes absent are the 3×32 corner-momentum modes, which do not form a lattice field.
- ARGUED: the free light window is roughly q* ~ (v/Δ)^{1/(4R−1)} (from mean-field P = Δq^{4R} against v|q|), and it shrinks as g grows. So Variant T must live at intermediate coupling.

## 3. Anomaly matching

**The UV anomaly is zero (EXACT).**
- The Fock vacuum is a symmetric product state for Spin(10) × (Z³ ⋊ O*), including the Z₄ centre.
- So every UV 't Hooft anomaly vanishes, including translation-twisted ones, and the IR content must be anomaly-free.

**The light triplet 3 × 16_L passes every check.**

| Anomaly | Value for 3 × 16_L | Label |
|---|---|---|
| Spin(10)³ | 0; so(10) has no cubic invariant. Each Cartan U(1) has Σq = Σq³ = 0, since for each coordinate the weights ±½ occur 8 times each | EXACT |
| Spin(10)–gravity² | 0; no abelian factor | EXACT |
| Z₄-centre ν | 48 ≡ 0 mod 16 | EXACT arithmetic |
| Translation-twisted ν | ±16 or ±48, all ≡ 0 mod 16 (REPORT_v2 table) | EXACT arithmetic |
| Z₂(translation)–Spin(10)² | 4 instanton zero modes per 16 (Dynkin index T(16) = 2), even | EXACT |
| Global (Dai–Freed / new SU(2)) | anomaly-free per Wang–Wen–Witten and García-Etxebarria–Montero | LIT |

If U(1)_F were kept, Σq³ = 48 ≠ 0 would fail. So breaking it to Z₄ is required, consistent with obstruction O-E.

**Verdict on Q3.** Anomaly matching permits the chiral light triplet but does not protect it. The light set and the gapped set are each anomaly-free, so a chiral, a vector-like and a fully gapped IR all match. This agrees with GS's remark that anomalies do not enter.

The chirality is protected perturbatively, not topologically:
- Spin(10) forbids pairing.
- Translations forbid inter-corner bilinears.
- Interactions are irrelevant and suppressed by the form factors.
- One relevant tuning, E_c, remains.

## 4. Verdict and cheapest decisive check

**Verdict (ARGUED).**
- **Open.** GS does not kill Variant T, because hypothesis (3) is a conjecture. Variant T does not evade GS through any hypothesis it controls: locality, translation invariance, on-site G and a free continuum all hold.
- **Survival condition.** Variant T survives only on branch G: the mirror-triplet zeros, net winding +3 (EXACT), must be irremovable.
- **Failure signature.** Branch K has a definite, measurable outcome: a massless opposite-chirality composite 16 at each light corner (F4).
- **Where the views point.** GS's combined view (2505.20436 plus the PRL) predicts failure. The SMG literature's view predicts branch G.

**Cheapest decisive check (spec only, not run).** A 1+1D Variant-T analogue. It is a clean test of GS because the form factors make induced light four-fermion vertices O(q^{8R}), which are irrelevant (EXACT diagrammatically). That removes GS's 2D objection about marginal operators, which applies to the Zeng–Zhu–Wang–You (ZZWY) 3450 model.

*Inputs*
- Lane C's 3450 ring: four complex species with charges (3, 4, 5, 0), light at k = 0, mirror at π, and no quadratic staggered term.
- Composites Φ_j = ½ψ_j − ¼(ψ_{j+1} + ψ_{j−1}), form factor sin²(k/2) (R = 1), and its square (R = 2).
- Gapping vectors ℓ₁, ℓ₂ applied to the Φ's, with coupling U swept.
- DMRG with local dimension 16, L = 48–96, bond dimension 400–800, under 2 GB, one worker, BLAS threads = 1.

*Measurements*
- **M1:** central charge c.
- **M2:** gaps at k ≈ 0 and k ≈ π.
- **M3:** in each charge sector, the 2×2 ω = 0 retarded matrix over {ψ_i, B_i = ∂H_int/∂Φ_i†} near π, using correction vectors (static susceptibilities). Check whether det 𝓡 is nonzero and finite.
- **M4:** whether 𝓡_BB diverges near k = 0 with the opposite chirality sign.
- **M5:** Luttinger parameter K = 1, to confirm the continuum is free.

*Outcomes*

| Outcome | Meaning |
|---|---|
| c = 2, symmetric, K = 1, det 𝓡_{ψB}(π) → 0 for every composite tried | GS hypothesis (3) fails in a model that satisfies (1) and (2). Branch G is live; move to 3+1D |
| c = 4 with M4 divergent | Branch K is realised; the mechanism gives vector-like content |
| c = 2 but det 𝓡 ≠ 0 and no partner | Contradicts the theorem; audit for secondary singularities or a numerical error |
| c < 2, or symmetry breaking | Golterman–Petcher–Rivas or symmetry-breaking failure |

*Limits.* This decides the GS fork for the form-factor mechanism, not whether a 3+1D SMG phase exists.

*3+1D follow-up (not cheap).* Count massless Spin(10)-charged states through the coefficient of the Cartan-current vacuum polarisation, or through the low-temperature specific heat:
- 3 16s means chiral;
- 6 means branch K;
- 0 means the PRL ghost reading.

The QMC sign problem for this model is unknown.

Sources:
- [arXiv:2603.15985](https://arxiv.org/abs/2603.15985)
- [arXiv:2505.20436](https://arxiv.org/abs/2505.20436)
- [arXiv:2311.12790](https://arxiv.org/abs/2311.12790)
- [arXiv:2405.05339](https://arxiv.org/abs/2405.05339)
- [arXiv:2410.22173](https://arxiv.org/abs/2410.22173)
- [arXiv:2607.09935](https://arxiv.org/abs/2607.09935)