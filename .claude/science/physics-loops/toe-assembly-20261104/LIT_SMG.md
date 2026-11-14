# Symmetric mass generation for the five-mode mirror sector

The twisted family `R_u = 10_u + 5bar_{-3u} + 1_{5u}`, with `u` odd and `u = 2 mod 5`, has vanishing perturbative anomalies and passes the global anomaly tests described below. Its mirror passes the same tests separately. A useful native bridge exists: `R_u` is the pullback of a Spin(10) spinor along a nonfaithful homomorphism `U(5) -> Spin(10)`. This transfers invariant interaction formulas and supplies a route to a complete continuum anomaly proof. It does not supply a lattice mirror gap. Wang–Wen assume the general gapped-boundary existence step. The confinement constructions require additional dynamics. The lattice papers give exact small-block results, conditional obstructions, or numerical evidence, with different symmetries. No fetched work establishes CH1-5U-i or CH1-5O-i for the repo's finite-depth update and composite carriers. On `L5-O`, the absence of local spinor operators still prevents a direct Spin(10)-16 construction; breaking to a specified residual group remains necessary.

## 1. García-Etxebarria and Montero: ordinary and discrete global anomalies

**Source.** Iñaki García-Etxebarria and Miguel Montero, *Dai-Freed anomalies in particle physics*. First submitted 2018; checked [arXiv:1808.00009v3](https://arxiv.org/abs/1808.00009v3), revised 2020; published 2019. Read §§3.3–3.4, 3.6.3 and 4.3. Exact anchors: Eqs. **(3.19), (3.24), (3.25), (3.70), (4.14)–(4.16)**. Quote from (3.25): “\(\Omega^{\mathrm{Spin}}_5(BSU(n))=0,\ \text{for }n>2\).”

**What it proves and assumes.** These are mathematical bordism computations and index-theoretic anomaly arguments. They separate local anomaly cancellation from the remaining exponentiated eta invariant. Ordinary Spin manifolds have no remaining degree-five bordism obstruction for `SU(5)` or `Spin(10)`. This does not remove the local `SU(5)^3` anomaly for arbitrary matter. A different tangential structure, `Spin ×_{Z2} Z4`, gives the mod-16 test through its Smith map to Pin-plus bordism. Their hypercharge conventions in (4.13) differ from CH1's; the abstract symmetry action must be translated.

**Native ordinary-Spin claim.** For every allowed integer `u`, both a left-handed `R_u` and its right-handed mirror have zero invertible gauge/gravitational anomaly on Spin four-manifolds with arbitrary principal `U(5)` bundles. Use the actual group `U(5) = (SU(5) × U(1))/Z5`, including bundles that do not split into an `SU(5)` bundle and a line bundle. With `T(5)=1/2`, the four local coefficients are

\[
 A_{SU(5)^3}=1-1=0,\qquad
 A_{SU(5)^2N}=\tfrac32u+\tfrac12(-3u)=0,
\]
\[
 A_{N\text{-grav}}=10u-15u+5u=0,\qquad
 A_{N^3}=10u^3-135u^3+125u^3=0.
\]

There is no independent `SU(5) U(1)^2` coefficient because every `SU(5)` generator is traceless. A right-handed mirror in `R_u`, equivalently a left-handed field in `R_u*`, reverses the anomaly functional. Zero remains zero. Cancellation between the family and its mirror is not the argument.

**A short native extension of their method.** Rebuild `Omega_5^Spin(BU(5))=0` directly. The only potentially nonzero term of total degree five in the low-degree Atiyah–Hirzebruch spectral sequence is `H_4(BU(5);Z2)`, dual to `c1^2,c2`. The outgoing `d2` removes the first component because `Sq^2(c1)=c1^2`. The incoming `d2` removes the remaining component because `Sq^2(c2)=c1 c2+c3`, while `Sq^2(c1^2)=0`. Integral cohomology is torsion-free and polynomial in the Chern classes; no other total-degree-five term survives. This checks arbitrary `U(5)` bundles without pretending that the group is a direct product.

**Mapping and rebuild.** This closes the ordinary continuum anomaly sub-obligation in CH1 §5.1, once the index/eta framework and spectral-sequence inputs are rebuilt. It does not prove AM-5 for interacting Floquet updates. Estimated proof: **4–6 pages** for the representation traces and `BU(5)` computation, plus a separately proved index/eta and bordism library. Section 2 below treats the parity quotient, which the ordinary-Spin computation alone does not cover.

**Source checkpoint.** Read CH1 §5 and Theorem U-A, and CG1K's summary and §5. Actual branch was `toe-assembly-local`, HEAD `2d0adc0c022753469151385e1789a4f444585ca6`; no branch change was made. SHA-256: `CH1_5_DRAFT.md` = `879002bdde3b9ddb0a4d4ae39ed2e35ecb5c44f973f6e67ef66d0a8192f1bf2d`; `CG1_KILL_DRAFT.md` = `46ce7c0695ef74aae258bf6e2e39aed6d5c5f31a11e8caaf6e68d987f11ec58d`. Live searches on 2026-11-05 covered every requested author group, exact `U(5)` global anomalies, rigorous lattice SMG and recent mirror-decoupling constraints. Every work cited here had its versioned arXiv abstract and PDF fetched. Numbering follows those PDFs. Cached primary texts and their hash manifest are in `/private/tmp/smg-lit-20261105/`. Reading verifies attribution; it does not confer repository proof or independent review.

## 2. Wang and Wen: Spin(10), its remaining Z2 class, and the twisted-family bridge

**Source.** Juven Wang and Xiao-Gang Wen, *A Non-Perturbative Definition of the Standard Models*. First submitted 2018; checked [arXiv:1809.11171v3](https://arxiv.org/abs/1809.11171v3), 2020. Exact anchors: **Propositions 1 and 2**, Eqs. **(9), (13)–(16)**. Quote from Proposition 1: “the mirror sector can be chosen to be a fully gapped boundary.”

**What it establishes and assumes.** The anomaly analysis distinguishes `Spin × Spin(10)` from `(Spin × Spin(10))/Z2^F`. The latter permits a `Z2` class represented by `exp(i pi integral w2 w3)`. Equation (14) tests old and new `SU(2)` anomalies. Equations (15)–(16) restrict a chiral 16 to **eight** isospin-1/2 doublets of the specified `Spin(3)` subgroup; there are no isospin-3/2 representations there. Thus the 16 has zero coefficient. The cobordism calculation is mathematical. The deduction of an available lattice gapped boundary uses Proposition 2, explicitly introduced as an assumption and described as believed true. It supplies no explicit, volume-uniform mirror-gap bound for these laws.

**Native bridge, derived here; not attributed to the paper.** Let `E` denote the defining five-dimensional `U(5)` representation. Set

\[
 k=(u-2)/5,\qquad k'=(1-3u)/5,\qquad r=(-2u-1)/5,
 \qquad W_u=E\otimes(\det E)^r.
\]

All exponents are integers. The twisted family is

\[
 R_u=(\Lambda^2E)(\det E)^k
       \oplus E^*(\det E)^{k'}\oplus(\det E)^u.
\]

The complex five-vector `W_u` defines an oriented real ten-vector with

\[
 \det W_u=(\det E)^{1+5r}=(\det E)^{-2u}.
\]

Its determinant winding is even. Its map to `SO(10)` therefore lifts to a homomorphism `f_u: U(5) -> Spin(10)`. The exterior-algebra spinor construction gives, up to naming the two spinor chiralities,

\[
 f_u^*S^+=\Lambda^{\mathrm{even}}W_u\otimes(\det E)^u=R_u.
\]

Indeed, degrees `0,2,4` give exponents `u`, `2r+u=k`, and `1+4r+u=k'`. Computing the spinor's torus weights gives central charges `5u,u,-3u` as a second normalization check. Exact rational arithmetic checked these affine identities and the local anomaly sums; this author check is not independent review. Because `u` and `r` are odd, `W_u(-I_5)=I_{10}` while `R_u(-I_5)=-I_{16}`. Hence `f_u(-I_5)=-1` in Spin(10). The map has finite kernel `Z_|u|`; it is **not** an embedding of the exact gauge group. We pull back representations, bundles and interactions. We do not replace `U(5)` by its image or discard its bundle sectors.

**Precise parity-quotient claim to rebuild.** Write

\[
 \mathcal G_u(d)=(\mathrm{Spin}(d)\times U(5))
                  /\langle(-1,-I_5)\rangle.
\]

For every allowed `u`, a Weyl `R_u` and its mirror each have trivial invertible anomaly on all admissible `G_u` backgrounds. This is a literature-supported native theorem target, not retained status. The lift above induces a map from `G_u` to `Spin ×_{Z2} Spin(10)`. Naturality of the fermion anomaly transfers the zero anomaly of the 16. There is also a check specific to this restriction: `[s,g] -> [s,det g]` maps `G_u` to `Spin^c`, since the rank is odd. Thus `w2(T)` has an integral lift and `w3(T)=0`; the possible `w2 w3` class restricts to zero. An anomaly group admitting a nonzero class does not mean this representation carries it.

This quotient is motivated by CH1's exact relation `(-1)^F=(-1)^N`. The repo still must establish which continuum background structures its microscopic law realizes. The two claims above cover ordinary Spin bundles and this parity-identified extension explicitly. They do not address extra crystalline, time-reversal, higher-form or Floquet symmetries unless those are specified.

**Interactions that can be rebuilt now.** Let `A=10_u`, `B=5bar_{-3u}`, `C=1_{5u}`, and let `Phi` transform as `W_u=5_{-2u}`. Pulling back the spinor-vector Yukawa invariant gives channels

\[
 \epsilon_{ijklm}A^{ij}A^{kl}\Phi^m,\qquad
 A^{ij}B_i\Phi_j^*,\qquad B_i C\Phi^i,
\]

with Weyl spinor contractions and relative Clebsch coefficients to be written explicitly. Their charge sums are `0,0,0`. Eliminating a massive Gaussian auxiliary field produces gauge-invariant quartics, including channels with content `A^3 B` and `A B^2 C`. These preserve `U(1)_N` while breaking an unwanted common fermion-number rotation to a subgroup. `Phi` can be a Hubbard–Stratonovich variable; giving it independent physical dynamics would require a separate realization in the law. A mass at fixed nonzero `Phi` does not prove a gap after its orientation fluctuates.

No pair from the charges `u,-3u,5u` sums to zero for `u != 0`. Thus an isolated same-chirality family admits no gauge-invariant quadratic Weyl mass. The anomaly-free target needs interactions to acquire a symmetric gap.

**Mapping and rebuild size.** On `L5-U`, this gives anomaly bookkeeping and interaction tensors for the actual twists, including negative `u`. It does not turn their composite operators into independent canonical modes. On `L5-O`, it does not create a forbidden local 16 of the original Spin(10). After symmetry breaking, it can apply to a residual `U(5)` family if that family is realized. Estimated proof: **3–5 pages** for the lift, kernel and tensors; **8–15 pages** for the quotient anomaly calculation and its naturality, assuming the needed mathematical infrastructure. A gap theorem on the specified cube update remains an open research problem; no honest finite proof-size estimate follows from this paper.

## 3. Wan and Wang: mod-16 is not the whole anomaly ledger

**Source.** Zheyan Wan and Juven Wang, *Beyond Standard Models and Grand Unifications: Anomalies, Topological Terms, and Dynamical Constraints via Cobordisms*. First submitted 2019; checked [arXiv:1910.14668v4](https://arxiv.org/abs/1910.14668v4), 2020. Exact anchors: Eqs. **(3.1), (5.14)–(5.16), (6.1)–(6.2)**; Tables **9–10, 25–28**. Quote from (3.1): “\(\Omega^{\mathrm{Pin}^{+}}_4=\mathbb Z_{16}\).”

**What it proves and assumes.** These are mathematical bordism and invertible-phase classifications for specified tangential groups. Table 25 gives `Z2`, detected by `w2 w3`, for `Spin ×_{Z2} Spin(10)`. Table 27 gives zero degree-five Spin bordism for `SU(5)`, while Table 28 retains its perturbative cubic anomaly class. Adding `Z4^F` changes the answer. For the product SM internal group, Table 9 has torsion `Z2 × Z4 × Z4 × Z16`. Its representatives include `a c2(SU(3))`, `c2(SU(2)) eta'`, `c1(U(1))^2 eta'`, and `eta(PD(a))`. Here `eta'` is the one-dimensional `Z4`-valued invariant. Other SM central quotients require their own tables. None of these computations proves a mirror gap.

**Native discrete ledger.** In exact `U(5)`, choose `z=i I_5`. Its square is the parity element. Every component of `R_u` has charge `u mod 4`, because `-3u` and `5u` equal `u mod 4`. With the convention that a left-handed charge-1 Weyl field contributes `+1`,

\[
 \nu_{16}(R_u)=
 \begin{cases}16,&u=1\pmod4,\\-16,&u=3\pmod4\end{cases}
 =0\pmod{16}.
\]

The mirror contributes the negative and also vanishes. The `SU(5)^2-Z4` instanton test gives `3u-3u=0`; using residues gives `4u=0 mod 4`. The full pullback anomaly argument in §2, rather than this one instanton test, covers all mixed invariants of any subgroup that actually maps into the stated `U(5)`. Thus the family carries zero coefficients also on the appropriate mixed `Z4` and `Z2` tests after restriction. Do not transplant Table 9's group to a different global form of the SM group.

Removing `C` leaves `nu16 = ±15`, which is nonzero if this `Z4^F` is preserved. By contrast, `10+5bar` with **only** ordinary `SU(5)` symmetry is anomaly-free: there is no automatically imposed mod-16 rule for every SU(5) theory. With continuous `U(5)` preserved, removing `C` already fails the local gravitational and cubic tests.

**Mapping and rebuild.** For CH1-5O-i, compute the residual group and parity structure first. The standard family under `H` has the ordinary anomaly-free restriction of `10+5bar+1`; its four weak doublets also pass the old Witten test. This says nothing about gapping the other components of the repo's `10,120,252` parents. Nor does the conventional spinorial parity quotient describe those tensor-class local operators automatically. Estimated proof: **3–5 pages** for this family's discrete restrictions; **10–20 pages** for the needed low-degree quotient-bordism calculation. Extra residual symmetries need a new ledger.

## 4. Razamat and Tong: confinement can gap chiral matter, with qualifications

**Source.** Shlomo S. Razamat and David Tong, *Gapped Chiral Fermions*. First submitted 2020; checked [arXiv:2009.05037v3](https://arxiv.org/abs/2009.05037v3), 2021. Exact anchors: Eqs. **(2.1), (2.4), (3.1)** and §2.1. Quote from (3.1): “\(\nu_4=n_+-n_-\ \mathrm{mod}\ 16\).”

**What it establishes and assumes.** This is continuum physics using supersymmetric s-confinement, with an explicitly conjectural nonsupersymmetric warm-up. Equation (2.1) couples conjugate singlets to confined composites. Equation (2.4) implements the odd-`N` antisymmetric SU(N) example. The auxiliary sector includes gauge fields, scalars and additional fermions. The warm-up gauges the `SU(5)` acting on `10+5bar`, assumes its proposed confining spectrum, and preserves an external `U(1)`. It does **not** preserve that SU(5) as an independently massless target gauge sector. The odd-`N` supersymmetric construction also needs extra matter to avoid an auxiliary Witten anomaly. Full continuous-charge assignments must include all auxiliary fields.

**Mapping and rebuild.** The warm-up is not a solution with exact, unbroken target `U(5)`. The symmetry-preserving construction is more useful after separating target and auxiliary groups. Rebuild the complete UV charge table, every local and global anomaly, the composite representations, and the infrared mass matrix. Then ask whether the repo supplies the auxiliary dynamics without changing its law. Do not infer a nonsupersymmetric lattice theorem from holomorphy. Estimated proof: **5–8 pages** for algebraic matching and mass matrices; a native confinement and gap proof is a separate, unresolved obligation.

## 5. Tong: a review of the dynamical routes and their assumptions

**Source.** David Tong, *Comments on Symmetric Mass Generation in 2d and 4d*. First submitted 2021; checked [arXiv:2104.03997v3](https://arxiv.org/abs/2104.03997v3), 2022. Exact anchors: Eqs. **(2.7), (2.8), (2.10), (2.14)** and §§2.2–2.3. Quote adjoining (2.8): “For N odd, one must work a little harder”.

**What it establishes and assumes.** This continuum analysis compares supersymmetric confinement, conjectural nonsupersymmetric confinement, and Higgs descriptions with symmetry locking. Equation (2.7) is the antisymmetric plus `N-4` antifundamentals; `N=5` is relevant here. The text explicitly says the initial auxiliary group is insufficient at `N=5`. Additional vectorlike matter and a larger auxiliary group enter. Section 2.3 treats SM fermions. Its surviving group in (2.14) includes `B-L`; it is not an explicit realization of the repo's exact `U(5)` update.

**Mapping and rebuild.** Use this paper to compare the auxiliary-sector routes, and to distinguish a preserved diagonal symmetry from breaking the target gauge field. Rebuild the Higgs stabilizer, anomaly matching and full mass matrices for one chosen construction. Credit Tong's mechanism, but retain its strong-dynamics premises until proved. Estimated proof: **4–7 pages** for those algebraic steps. Proving confinement, a thermodynamic gap and its implementation by the permitted gates is not bounded by that estimate. The two-dimensional mechanisms do not establish four-dimensional mirror decoupling.

## 6. Wang and You: SMG definitions and a solvable finite block

**Source.** Juven Wang and Yi-Zhuang You, *Symmetric Mass Generation*, 2022; checked [arXiv:2204.14271v1](https://arxiv.org/abs/2204.14271v1). Exact anchors: Eqs. **(1)–(3)** and §II.E. Quote from the discussion of (1): “is the unique ground state of HFK”.

**What it establishes and assumes.** This is a review and construction framework. Its eight-Majorana quantum-mechanical interaction has an exactly checkable unique symmetric ground state and finite gap. The symmetry is a specified antiunitary symmetry and fermion parity. Section II.E states anomaly cancellation and absence of a bilinear mass as SMG criteria, then asserts phase existence. That assertion is not a constructive uniform-gap theorem for a specified microscopic law. An anomalous sector may instead require topological order; such a gapped sector need not be removable as a trivial mirror regulator.

**Mapping and rebuild.** Rebuild the finite-block spectrum as an exact CAR calculation and use it as a benchmark for a symmetry-preserving interaction. Neither the count of Majoranas nor its antiunitary symmetry identifies the block with `R_u`. A whole-system product gap also does not isolate a desired chiral sector. Estimated proof: **2–3 pages** for the block, followed by a new representation and locality bridge for any use here.

## 7. Kikukawa: an explicit overlap measure with an open locality problem

**Source.** Yoshio Kikukawa, *On the gauge invariant path-integral measure for the overlap Weyl fermions in 16 of SO(10)*. First submitted 2017; checked [arXiv:1710.11618v5](https://arxiv.org/abs/1710.11618v5), 2018; published 2019. Exact anchors: Eqs. **(3.2)–(3.7), (3.25), (3.68), (7.1)**. Quote from §7 concerning (7.1): “There remains the issue of smoothness/locality”.

**What it establishes and assumes.** Exact algebra constructs invariant right-handed 't Hooft vertices and a saturated-measure proposal. The paper proves symmetry identities, including CP invariance. Its gauge-field dependence uses overlap/Ginsparg–Wilson projectors and admissibility. The conclusion explicitly leaves smoothness/locality of the measure term (7.1) for future work. Nonvanishing auxiliary integrals and unbroken symmetry are argued and tested in selected backgrounds. These are not an established local, reflection-positive mirror regulator for arbitrary gauge backgrounds.

**Mapping and rebuild.** Pull the invariant tensors back through `f_u`, preserving their exact `U(5)` charges. Rebuild the vertex identities and saturation calculation for the repo's composite carriers before considering a measure. Overlap projectors are not finite-depth gates. The extra uniform locality, gap, and reflection-positivity steps remain. On unbroken `L5-O`, the initial spinor field is absent. Estimated proof: **4–8 pages** for tensor and finite-Grassmann identities. A proof of (7.1)'s required locality, plus translation to the law, remains unbounded and open.

## 8. Golterman and Shamir: a conditional interacting doubling theorem

**Source.** Maarten Golterman and Yigal Shamir, *Constraints on the symmetric mass generation paradigm for lattice chiral gauge theories*. First submitted 2025; checked [arXiv:2505.20436v3](https://arxiv.org/abs/2505.20436v3), 2026. Exact anchors: Eq. **(1.1)**, Eqs. **(3.1)–(3.7)**, and the **unnumbered theorem in §III, PDF pp. 15–16**. Quote from that theorem: “the massless fermion spectrum in this charge sector is vector-like.”

**What it proves and assumes.** The conditional theorem concerns a translation-invariant regular spatial lattice Hamiltonian with finite-range fermionic terms, unbroken compact symmetry, a continuum limit of free relativistic massless fermions without massless bosons, and a complete set of interpolating fields whose zero-frequency retarded matrix has no zeros. Its inverse defines the effective one-particle Hamiltonian. Under the stated regularity conditions, the doubling conclusion follows. That propagator zeros can always be removed by including composite partners is a conjectural physical step, not an unconditional theorem about every SMG model.

**Mapping and rebuild.** This is a decisive stress test for a proposed mirror interaction. Include composites in the propagator matrix; a vanishing elementary propagator alone proves neither a gap nor successful chirality. The repo has Floquet updates and gauge registers, so the paper's Hamiltonian hypotheses need an explicit bridge. Do not declare either law excluded by this conditional result. Estimated proof: **6–10 pages** for the conditional correlator/regularity argument and torus chirality count, plus a new Floquet adaptation if possible.

## 9. Golterman and Shamir: the 2026 follow-up

**Source.** Maarten Golterman and Yigal Shamir, *Symmetric mass generation and the Nielsen-Ninomiya theorem*, 2026; checked [arXiv:2603.15985v1](https://arxiv.org/abs/2603.15985v1), Lattice 2025 proceedings. Exact anchors: Eqs. **(5)–(9)** and §3. Quote adjoining (6): “The interpolating fields for the putative bound-state partners”.

**What it adds.** This physics-level summary proposes composite interpolators schematically obtained by differentiating the mirror interaction with respect to a mirror field. It recaps the conditional theorem. Existence of an operator with the right charge does not establish a particle pole, residue or mass. The paper explicitly uses putative bound states.

**Mapping and rebuild.** For the quartics in §2, derive these composite channels and include them in a complete correlator matrix. This directly addresses the repo's emphasis on composite light fields. Check whether a claimed mirror gap instead hides another light charged state. Estimated proof: **2–4 pages** for operator transformations and correlator definitions. Bound-state dynamics remain open. This proceedings paper is not an independent confirmation of the main paper's hypotheses.

## 10. You, He, Xu and Vishwanath: a 2+1D mechanism with a different charge symmetry

**Source.** Yi-Zhuang You, Yin-Chen He, Cenke Xu and Ashvin Vishwanath, *Symmetric Fermion Mass Generation as Deconfined Quantum Criticality*. First submitted 2017; checked [arXiv:1705.09313v2](https://arxiv.org/abs/1705.09313v2), 2017; published 2018. Exact anchors: Eqs. **(1)–(3)**. Quote from the paragraph after (2): “The charge U(1) symmetry is explicitly broken”.

**What it establishes and assumes.** The lattice model has four complex flavors on each honeycomb site, an SU(4)-invariant quartic, and eight low-energy Dirac fermions in 2+1D. At zero hopping its local quartet interaction has a unique symmetric ground state; the product state is explicit in (3). The deconfined critical description uses partons and emergent gauge fields. The direct continuous transition is a physics proposal supported by the numerical literature, not a theorem established by this calculation.

**Mapping and rebuild.** It supplies an exact small-block comparison and a parton route. Its charge-four creation term violates ordinary number conservation, so one cannot use it unchanged in exact `U(5)`. The charge-balanced quartics in §2 are a possible replacement to investigate, not an established extension of this result. It is also one spatial dimension short. Estimated proof: **2–4 pages** for the local spectrum and symmetry calculation. A 3+1D, mirror-selective, volume-uniform gap requires new work.

## 11. Zeng and collaborators: numerical mirror decoupling in 1+1D

**Source.** Meng Zeng, Zheng Zhu, Juven Wang and Yi-Zhuang You, *Symmetric Mass Generation in the 1+1 Dimensional Chiral Fermion 3-4-5-0 Model*, 2022; checked [arXiv:2202.12355v2](https://arxiv.org/abs/2202.12355v2). Exact anchors: Eqs. **(1)–(3)** and the DMRG results. Quote from the paragraph after (3): “Our central goal is to numerically verify”.

**What it establishes and assumes.** A thin Chern-insulator strip separates light and mirror modes. Two selected six-fermion interactions act on the mirror boundary. The model cancels the 1+1D gauge anomaly `3^2+4^2-5^2-0^2`. DMRG supplies evidence for a mirror gap and a surviving light sector. Bosonization motivates compatible gapping interactions. Finite-size data and extracted critical behavior do not prove a thermodynamic gap.

**Mapping and rebuild.** Use its separation of sectors and choice of compatible interactions to design CH1 §5.1's proposed small-chain test. Rebuild the integer charge constraints and continuum null-vector conditions before simulation. Neither these charges nor the two-dimensional anomaly polynomial extends to U(5) Weyl fermions in 3+1D. Estimated proof: **3–5 pages** for the 1+1D continuum gapping algebra, with a separate lattice-to-continuum argument. This work supplies no proof-size estimate for the four-dimensional problem.

## 12. Butt, Catterall, Pradhan and Toga: a different gravitational anomaly

**Source.** Nouman Butt, Simon Catterall, Arnab Pradhan and Goksu Can Toga, *Anomalies and symmetric mass generation for Kaehler-Dirac fermions*. First submitted 2021; checked [arXiv:2101.01026v4](https://arxiv.org/abs/2101.01026v4), 2022. Exact anchors: Eqs. **(29), (30), (34)–(37)**. Quote from (29): “\(Z\to e^{-2i\alpha\chi}Z\).”

**What it proves and assumes.** The Kähler–Dirac measure has an Euler-characteristic anomaly for its form-degree U(1). The index equals the Euler characteristic. A spectral-flow/Pfaffian sign argument gives further restrictions for reduced fields. These are analytic anomaly calculations for Kähler–Dirac fields. The claimed SMG applications are proposed interactions and consistency conditions. Equality to collections of ordinary Dirac fields in flat space does not identify their gravitational couplings on curved backgrounds.

**Mapping and rebuild.** This prevents a counting error: a staggered or Kähler–Dirac `Z4` is not automatically the exact central `i I_5` action on `R_u`. Rebuild its Euler-index calculation only if a Kähler–Dirac discretization is actually introduced. It does not alter the U(5) ledger above. Estimated proof: **4–6 pages** for the finite-cochain version and Pfaffian sign argument; a relation to these laws would be an additional obligation.

## 13. Butt, Catterall and Toga: four-dimensional gauge-driven numerical SMG

**Source.** Nouman Butt, Simon Catterall and Goksu Can Toga, *Symmetric Mass Generation in Lattice Gauge Theory*, 2021; checked [arXiv:2111.01001v1](https://arxiv.org/abs/2111.01001v1). Exact anchors: Eqs. **(7), (10), (19)** and the numerical results. Quote introducing those results: “provide evidence that a four fermion condensate appears”.

**What it establishes and assumes.** The four-dimensional Euclidean model uses reduced staggered bifundamentals of `SU(2) × SU(2)`. A symmetric quartic is allowed; its Yukawa representation reduces a staggered U(1) to Z4. Simulations give evidence for a four-fermion condensate and the proposed symmetric massive regime. This is numerical evidence with analytic symmetry checks. A condensate by itself is not a spectral-gap theorem.

**Mapping and rebuild.** It confirms that dimensionality alone does not rule out numerical SMG studies. It does not realize a chiral U(5) family or isolate its mirrors. Rebuild the allowed-interaction and forbidden-bilinear tests, then apply those tests to the charge-balanced operators in §2. Estimated proof: **2–4 pages** for algebraic tests. Thermodynamic gap, residual light spectrum, and a map to the permitted unitary gates are additional open tasks.

## 14. Guo and You: an explicit higher-dimensional Hamiltonian is not yet this gap theorem

**Source.** Yuxuan Guo and Yi-Zhuang You, *Symmetric Mass Generation of Kähler-Dirac Fermions from the Perspective of Symmetry-Protected Topological Phases*. First submitted and published 2023; checked [arXiv:2306.17420v6](https://arxiv.org/abs/2306.17420v6), 2024. Exact anchors: Eqs. **(25)–(28)** and Figure 2. Quote after (26): “the model possesses a unique and symmetric ground state.”

**What it establishes and assumes.** The paper gives a two-copy Kähler–Dirac interaction and an inversion-protected SPT interpretation across dimensions. Its strong-coupling argument reduces the interaction to independent quantum-mechanical cells, starts from a two-state degeneracy, and proposes the singlet (28). Figure 2 checks a 256-dimensional single-cell spectrum in 1+1D numerically. The text labels the extension away from the perturbative ratio as numerical. That figure is not a rigorous all-dimension, finite-hopping, thermodynamic gap bound. The general-dimensional perturbative splitting also needs an explicit order-by-order calculation.

**Mapping and rebuild.** This is a concrete Hamiltonian worth testing, not evidence that the exact target group or mirror sector has been solved. Rebuild each relevant cell spectrum symbolically, check its true symmetry, and prove stability under hopping with volume-independent bounds. Its Kähler–Dirac and inversion setting differs from both laws. Estimated proof: **4–8 pages** for one fixed cell and its perturbation series; the lattice stability and U(5) representation bridges remain open.

## 15. Fidkowski and Kitaev: a rigorous local gapping result to use as a benchmark

**Source.** Lukasz Fidkowski and Alexei Kitaev, *The effects of interactions on the topological classification of free fermion systems*. First submitted 2009; checked [arXiv:0904.2197v3](https://arxiv.org/abs/0904.2197v3), 2009; published 2010. Exact anchors: Eqs. **(8), (11)** and §II.A. Quote from its proof: “it is already a unique ground state of W1.”

**What it proves and assumes.** Eight Majoranas carry a quartic interaction with an exactly characterized unique ground state. The proof reduces the fourteen-term interaction to four compatible quartic constraints. It is a finite-dimensional spectral argument, not simulation evidence. Independent copies on disjoint cells give an exactly gapped product Hamiltonian in any spatial dimension at zero intercell coupling. This elementary extension says nothing about a chiral light sector. The paper's broader interpolation and one-dimensional phase analysis should not be confused with this specific exact block result.

**Mapping and rebuild.** Rebuild the Clifford identities, uniqueness, exact first excited energy and antiunitary action. Use this as a standard for what a rigorous SMG block proof should look like. The block does not carry `10_u+5bar_{-3u}+1_{5u}`, and its symmetry is not exact U(5). Estimated proof: **2–4 pages**. A weak-hopping stability theorem and a mechanism preserving only the desired light chirality would require additional proofs. A rigorous lattice mirror-decoupling result for the exact CH1 targets is **NOT VERIFIED**: none was located in this search. This is a search limit, not an impossibility claim.

## Rebuild candidates

Ordered by movement on the open items, not by ease. Page counts cover the stated mathematical unit; they exclude undeveloped index/bordism infrastructure and unresolved strong dynamics.

| Rank | Native unit, with credit | Effect on the open item | Estimated proof size / remaining wall |
|---|---|---|---|
| 1 | Twisted `U(5)` pullback, invariant Yukawas and quartics; build on Wang–Wen and Kikukawa | Gives an exact-group interaction target for every allowed `u`; eliminates the normalization mismatch | 3–5 pages; composite CAR, mirror selectivity and uniform gap remain |
| 2 | Full family-and-mirror anomaly theorem on Spin and parity-quotient backgrounds; García-Etxebarria–Montero, Wang–Wen, Wan–Wang | Resolves CH1-5U-i's missing continuum global-anomaly ledger, including mixed discrete tests | 8–15 pages plus foundational library; does not prove interacting AM-5 |
| 3 | Complete elementary-plus-composite correlator test; Golterman–Shamir | Could expose a hidden light partner or identify the precise escape from conditional doubling | 6–10 pages for conditional theorem; new Floquet bridge required |
| 4 | Residual-group anomaly and representation ledger after `Spin(10) -> G_infty`; Wan–Wang | Makes CH1-5O-i's target precise once CG1K-H selects the group | 3–6 pages per specified group; no breaking mechanism supplied |
| 5 | Odd-`N` confinement construction with all auxiliary charges; Razamat–Tong and Tong | Provides a possible SU(5)/SM gapping route if its extra dynamics can be realized | 5–8 pages of algebra; confinement and embedding into the law unresolved |
| 6 | Exact block spectra and bounded hopping perturbations; Fidkowski–Kitaev, You–He–Xu–Vishwanath, Guo–You | Builds rigorous local benchmarks for candidate gates | 2–8 pages per block; no demonstrated twisted-U(5) mirror block |
| 7 | Compatible interactions and diagnostics for a small-chain probe; Zeng et al. and Catterall collaborations | Improves the proposed lower-dimensional experiment and identifies competing order | 3–5 pages of symmetry/gapping algebra; numerics cannot close either 3+1D item |
