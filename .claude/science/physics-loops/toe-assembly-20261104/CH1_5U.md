# CH1-5U-i. The twisted family and its mirror

## 0. Status

**Proved in this item, subject to the stated standard representation theory:** the covering description of the family; vanishing linear and cubic traces; the SU(2) index and Z4 character calculations; the restricted absence of a new-SU(2) embedding; the mirror quartic phase calculation; and the one-site commutant. The named anomaly interpretations additionally use the cited anomaly formulas. These results are not yet refereed.

**GAP:** the draft's claim that all global U(5) anomalies vanish uses an unverified bordism computation and an anomaly-theory input. Its sketch does not establish the required localization equivalences. Its alternative Spin(10) route also needs a verified precise anomaly theorem. Absence of the named anomaly tests is not a proof of absence of every anomaly. Spacetime-symmetry anomalies are not analyzed. The draft's claimed implication CH1-5U-i ⇒ CH1-5U-q needs an extra local-operator and correlation hypothesis. The purported failures of the existence attacks have the narrower scope stated below.

**Open by name:** CH1-5U-i; CH1-5U-q; CH1-i; GA2 bridge Y2; AM-5; CH1-ii; CH1-5O-i; reflection positivity; CG1K-H; LW1-5-X; VC1-5U-odd. The full global-anomaly calculation remains open here. No law or reading is adopted.

**Provenance.** Pass 2 run (set by the lead from the run log): Codex `gpt-6.1-terra`, reasoning effort high, codex-cli 0.165.0, session `01a1aed1-ebe2-7c72-9dc6-1679cbf694ce`. Pass 2 distillation of `CH1_5U_DRAFT.md`, SHA-256 `91430000d948742a9e833b1855ca02634fdcb7722dc9ae49df3c039a30bc07ae`. Context: `TOE_ASSEMBLY.md`, `LW1.md`, `CH1.md`, `LIT_SMG.md`; checkout HEAD `bf403a16a2bbb3bc0315a71f6cf1d791445cbb7f`. Pass 1 reports source revision `2d0adc0c0`; its other cited draft lemmas are inputs, not independently verified here. Distilled by Codex, requested model `gpt-6.1-terra`; actual model and reasoning effort are not exposed in this session. Session `01a1aed1-ebe2-7c72-9dc6-1679cbf694ce`. No referee status is claimed.

## 1. Definitions inferred by the distiller

1. The center `U(1)_N` acts by `e^{iθ}1_5`; a field of charge `q` transforms by `e^{iqθ}`. A bar denotes the complex-conjugate representation. Write `10=Λ²C⁵`, `5bar=(C⁵)*`.
2. Let `u` be odd and `u≡2 mod 5`, `k=(u−2)/5` and `k'=−3k−1`. Thus `k` is odd, `k'` even and `|u|≥3`. Define
   \[R_u=(\Lambda^2\mathbb C^5\otimes\det^k)\oplus((\mathbb C^5)^*\otimes\det^{k'})\oplus\det^u=10_u\oplus\overline5_{-3u}\oplus1_{5u}.\]
   The flipped assignment `B_k` has the same U(5) representation; its Standard Model embedding differs. The left-handed description of the mirror is `R_u*`.
3. Put `Ũ(5)={(g,z)∈U(5)×U(1):z²=det g}`, `−1̃=(1_5,−1)`, and `S=(Λ⁰⊕Λ²⊕Λ⁴)C⁵` with action `(g,z)↦z⁻¹Γ(g)`. The standard identification of this pair with the U(5) preimage and a restricted half-spin 16 of Spin(10) is nomenclature, not an input to the representation proofs.
4. The proposed fermionic structure is `K_d=(Spin(d)×U(5))/⟨(−1,−1_5)⟩`. The draft cites Lemma Z-U for the identification of `−1_5` with fermion parity on local operators. That algebraic identification alone does not prove the continuum theory is defined on every K-manifold. Both K and ordinary `Spin×U(5)` backgrounds are considered conditionally.
5. The perturbative test is `Tr_R X³=Tr_R X=0` for all `X∈u(5)`. A named global-anomaly test is a pullback of the anomaly along the specified structure map. This use of “type” does not classify all possible anomalies. In all pullback statements, connections are pulled back or induced compatibly, and the spinor representations descend.
6. `L5-U`, `G_U`, the hypothesis IR, and PS-8 mean the items in pass 1's quoted sources. CH1-5U-i asks for an `L5-U` tick with finitely many gauge-invariant site or cell gate layers, and an invariant stationary state, realizing precisely the light family `R_u`, or the flipped `B_k` assignment, with U(5) unbroken and all other fermion-odd excitations gapped. This is a proposed dynamical realization, not an established construction.

## 2. Representation and elementary charges

**Theorem 2.1 (Ũ and Φ).** `Ũ(5)` is connected. The map `σ(A,w)=(w²A,w⁵)` from `SU(5)×U(1)` is onto, with kernel `{(w⁻²1_5,w):w⁵=1}`. Its scalar circle `C={(w²1_5,w⁵)}` is isomorphic to U(1).

Every continuous homomorphism `ψ:U(5)→Ũ(5)` satisfying `ψ(A)=(A,1)` for `A∈SU(5)` is
\[\psi_{a,b}(g)=(g\det(g)^a,\det(g)^b),\quad 2b=1+5a.\]
Here `a` is odd, `b≡3 mod 5`; the map is onto, with kernel `μ_|b|` of scalar matrices, and
\[\psi_{a,b}^*S\cong10_{-b}\oplus\overline5_{3b}\oplus1_{-5b},\qquad \psi_{a,b}(-1_5)=(1_5,(-1)^b).\]
Thus for `b=−u`, `a=−(2u+1)/5`, `φ_u=ψ_{a,b}` has `φ_u* S≅R_u`, kernel `μ_|u|`, and sends `−1_5` to `−1̃`. The parity-preserving maps of this specified form give exactly the line of `R_u`. None is an isomorphism because `b≡3 mod 5` excludes `b=±1`; in particular `u=1` cannot arise from such an isomorphism. Scalars with `λ^u=1` act trivially on `R_u`.

*Proof.* Given `(g,z)`, choose `λ⁵=det g`, then `w²=λ` and change `w` to `−w` if necessary to obtain `w⁵=z`. Set `A=λ⁻¹g`. This proves surjectivity of σ, and its kernel and connectedness follow. The circle is injectively parametrized because `w²=w⁵=1` implies `w=1`.

For the converse, Schur's lemma puts the image of scalars in `C`, so `ψ(λ1)=(λ^{2b}1,λ^{5b})` for integer `b`. Restriction to `μ_5⊂SU(5)` gives `2b≡1 mod 5`. With `a=(2b−1)/5`, decomposition `g=λA` yields the displayed formula. Conversely it defines a homomorphism. Its kernel satisfies `λ^{2b}=λ^{5b}=1`; hence it is `μ_|b|`. Its differential is an isomorphism between 25-dimensional groups. Its compact image is open and closed in connected Ũ(5), hence onto.

On `Λ^r`, `r=0,2,4`, the pullback has weight `1_T+(ar−b)(1,1,1,1,1)`. The charges are `−5b,−b,3b`; `Λ⁴≅5bar⊗det` gives the indicated types. The parity formula follows by substitution. For odd `b`, `u=−b` is odd and `2 mod 5`, and the converse follows from the same equations. □

Complex conjugation produces the conjugate representation and conjugate embedding. It does not identify `R_u*` with the same unbarred `R_{−u}` convention.

**Theorem 2.2 (Q1 and Q1′, restricted).** Family and mirror charges lie in `{±u,±3u,±5u}` and have modulus at least 3. In a number-conserving quasi-free description, elementary one-particle and one-hole modes have charges `+1` and `−1`; none is a family member.

*Proof.* The first assertion follows from the displayed representation. The one-body space is spanned by creators of charge 1; holes have opposite charge. □

**GAP Q1′:** this does not show that every low-energy *composite* operator or multiparticle excitation in every quasi-free system has charge ±1, nor that no weakly coupled composite family can ever arise in an interacting law. The one-body conclusion is sufficient to identify the proposed elementary starting point as unavailable.

## 3. Anomaly calculations

**Theorem 3.1 (N, naturality).** For a structure homomorphism `f:K'→K` over `SO(d)` and a compatible representation `R`, induced associated bundles obey `P'×_{K'} f*R ≅ (P'×_f K)×_K R`. With compatible connections the associated Dirac operators and their indices and η-invariants agree. A vanishing anomaly therefore pulls back to a vanishing anomaly. In particular, `F_u:K_d→Spin(d)×_{Z₂}Ũ(5)`, `[s,g]↦[s,φ_u(g)]`, is well defined and pulls the anomaly of S back to that of `R_u`.

*Proof.* Both bundles are the quotient of `P'×R` by the same equivalence relation. The induced connection and Clifford action agree under this identification. Theorem 2.1 gives `φ_u(−1_5)=−1̃` and `φ_u*S=R_u`, which establish the special map and pullback. □

**Theorem 3.2 (A1, perturbative traces).** For every `X∈u(5)`, `Tr_{R_u}X=Tr_{R_u}X³=0`. The same holds for `R_u*`. Under the standard four-dimensional Weyl anomaly polynomial, all perturbative gauge and mixed gauge-gravitational anomalies vanish.

*Proof.* Diagonalize `dφ_u(X)`. On `S`, its 16 weights have the form `(1/2)∑ ε_i x_i` with an even number of plus signs. For any linear or cubic monomial, some variable has odd exponent and at least one of the five variables is absent. Flip both corresponding signs. This preserves the parity of plus signs and cancels the coefficient. The trace identities follow on S and hence on `R_u`. Conjugation reverses odd traces. Expanding in the central and traceless parts gives the `SU(5)^3`, `U(1)SU(5)^2`, `U(1)^2SU(5)`, `U(1)^3` and mixed gravitational terms. □

The draft's second derivation uses the cited `SU(5)^3` indices `A(10)=1`, `A(5bar)=−1`, the line `u(1,−3,5)`, and vanishing traces of traceless generators. It agrees with the proof above but is not an independent verification of those cited indices here.

**Theorem 3.3 (A2).** For every continuous `σ:SU(2)→U(5)`, with `n(W)=2Tr_W J_3²`,
\[n(\sigma^*R_u)=4n(\sigma^*5)\in4\mathbb Z.\]
Under the standard instanton-index and Witten-anomaly formulas, its Witten-type anomaly and that of the mirror vanish for these maps.

*Proof.* `det∘σ` is trivial because `su(2)` is perfect and SU(2) connected. If the eigenvalues of `J_3` on 5 are `y_i` with sum zero, then `∑_{i<j}(y_i+y_j)²=3∑y_i²`. The dual adds `∑y_i²` and the singlet adds zero. The SU(2) representation on 5 decomposes into spins of dimensions at most 5, whose indices are integers. The map `(s,h)↦[s,σ(h)]` gives the stated pullback. □

**Theorem 3.4 (A3).** If `g∈U(5)` and `g²=−1_5`, let `ν(g)` be the number of `+i` eigenvalues minus the number of `−i` eigenvalues on `R_u`. Then `ν∈{16,0,−16}`. At `g=i1_5`, it is `±16`; without the singlet it is `±15`. Under the cited mod-16 formula these tests vanish for the full family and mirror, and not for the 15 alone.

*Proof.* Conjugate `g` to `i diag(s_i)` with `r` negative signs. All three charges are `u mod 4`. Put `t=5−2r` and `ε=i^{u−1}=±1`. Then `ν=ε χ_{R_u}(diag(s_i))`, and, since `k,u` are odd and `k'` even,
\[\chi=(-1)^r\frac{t^2-3}{2}+t=(16,0,0,0,0,-16)_{r=0}^5.\]
Conjugation reverses ν. The center acts uniformly by `i^u`; removing the singlet removes one equal eigenvalue. □

**Theorem 3.5 (A4 and A5(i)).** No `σ:SU(2)→U(5)` satisfies `σ(−1)=−1_5`; consequently no structure map of the special form `[s,h]↦[s,σ(h)]` exists from `Spin×_{Z₂}SU(2)` to K. Also
\[K_d\cong(Spin^c(d)\times SU(5))/\mu_5,\]
where `ζ∈μ_5` acts by `(ζ⁻¹,ζ1_5)` on the central U(1) and SU(5).

*Proof.* Every σ has determinant 1, whereas `det(−1_5)=−1`. For the second statement, write `U(5)=(SU(5)×U(1))/μ_5` via `(A,λ)↦λA`. First divide `Spin×SU(5)×U(1)` by `(-1,1,-1)` and then by `(1,ζ1,ζ⁻¹)`. □

**GAP A4:** the proof excludes maps of the stated form, not every conceivable structure map involving a nontrivial spin component or every realization of the new-SU(2) anomaly.

**Conditional proposition 3.6 (A5(ii–iv)).** If `Ω₅^{Spin×_{Z₂}U(5)}=0` and, after local anomaly cancellation, the anomaly defines a homomorphism from this bordism group to U(1), then the full global anomaly of `R_u` and its mirror vanishes on K backgrounds and hence on ordinary spin U(5) backgrounds.

*Proof.* Theorem 3.2 gives the stipulated local cancellation. A homomorphism from the zero group is trivial; apply Theorem 3.1. □

**GAP A5:** neither hypothesis is established by the draft. The proposed AHSS sketch asserts, without proving the maps of Thom spectra, that quotienting by `μ_5` has the required 2-local effect and that odd-local K-bordism is oriented bordism of `BU(5)`. The displayed zero E² terms would suffice only after these identifications are justified. The alternative pullback from the Spin(10) 16 requires a precise checked theorem on its anomaly on `Spin×_{Z₂}Spin(10)`, not a list of reported anomaly types. The draft's unconditional verdict “all anomalies absent” is therefore not proved. A nonzero perturbative anomaly off the line follows only within the cited one-family classification, whose hypotheses are not re-proved here.

## 4. Mirror interactions and attempted routes

**Theorem 4.1 (K).** Let left-handed Weyl fields `A_{jk}=−A_{kj}`, `B^j`, `C` transform in `10bar_{−u}`, `5_{3u}`, `1_{−5u}`. Write `(χη)=ε^{αβ}χ_αη_β`. The unitary linear transformations commuting with U(5) are `U(1)^3`. The nonzero Lorentz- and U(5)-invariant quartics
\[O_2=\sum_{j,k}(A_{jk}B^k)(B^jC),\quad O_3=\sum\epsilon^{ijklm}(A_{jk}A_{lm})(\bar B_i\bar C)\]
are fixed exactly by the image of the gauged center: phases `(e^{iα},e^{-3iα},e^{5iα})`.

*Proof.* The three irreducible SU(5) types are distinct, so Schur's lemma gives the phase group. Both contractions are SU(5)-invariant and their U(1) charges are `−u+3u+3u−5u=0` and `−2u−3u+5u=0`. In `O_3`, for `i=1` the eight orderings of index pairs `(23),(45)` give the same nonzero contribution. In `O_2` the monomial `A_{12;1}B^2_{;2}B^1_{;1}C_{;2}` has nonzero coefficient; the reversed index term has different spinor components. Fixing the quartics imposes `α+2β+γ=0` and `2α−β−γ=0` modulo `2π`. These give `β=−3α`, `γ=5α`, including finite components. The gauged center supplies the full circle because `u≠0`. □

This excludes additional commuting **linear unitary flavor phases** common to these two interactions. It does not classify antiunitary, spacetime, nonlinear, higher-form, or microscopic symmetries, nor prove the interactions are realizable with the needed independent composite lattice fields. The draft's stronger “no surviving symmetry has an anomaly” is a GAP.

**Attack 1**, free; **Attack 2**, PS-8 on elementary content; and **Attack 3**, one-site composites: pass 1 reports failures at Lemma V, K1-5/K2-5 with AM-5, and U-A(iii), respectively. These source-dependent findings are not re-established here.

**Attack 4**, import a Spin(10) mirror-gapping flow: Theorem 2.1 pulls back any invariant interaction of S to an invariant interaction of `R_u`. The elementary quasi-free starting point does not have the required charge sectors (Theorem 2.2). This does not rule out another interacting starting point. The proposed gapping flow and a lattice realization of its continuum composite operators remain unproved. A proposed additional strongly coupled gauge group changes the stipulated law; it is not adopted.

**Attack 5**, overlap pullback: assuming pass 1's cited W2, `(U^{jk})²=0`, any state multiplicative on these operators gives `ω(U^{jk})²=0`, so its matrix of values is zero and not unitary. Thus this specific evaluation cannot supply the c-number unitary links used in the proposed overlap construction. This does not exclude operator-valued, coarse-grained, or approximate alternatives. A Euclidean overlap kernel also needs a separate derivation of the requested tick; the cited one-site composite CAR obstruction is not checked here. Replacing the finite registers with c-number links changes the law and is not adopted.

**Attack 6**, protected mirror flavor symmetry or elementary propagator: Theorem 4.1 defeats a universal obstruction based solely on a commuting linear unitary flavor phase that must survive *both* quartics, subject to their microscopic admissibility. The elementary charged field lies in a different global-charge sector from the family (Theorem 2.2), so an elementary one-particle pole theorem alone does not establish a constraint on the composite family. For a gauge-dressed correlator, endpoints, the Wilson line, Gauss constraints, and the definition of global charge must be specified before the draft's intermediate-state selection rule can be applied. Neither observation proves a general no-go theorem inapplicable.

## 5. Open subproblem and proposed readings

**CH1-5U-q (open, as proposed).** There exist an `L5-U` update and a stationary `G_U`- and gauge-invariant state, plus a quasi-local fermion-odd operator of `U(1)_N` charge `|q|≥3`, whose large-separation correlations agree with those of a free Weyl field.

**GAP in the claimed implication.** CH1-5U-i requires a light `10_u`, so its spectrum has charge `|u|≥3`. It implies CH1-5U-q only if hypothesis IR also supplies a quasi-local charged operator with the specified free-Weyl correlations. Frozen `CH1.md` defines IR using quasi-local odd operators with large-separation Weyl correlations, which supports the intended implication. It also requires a gauge-covariant dressing or charge-sector prescription; pass 1 does not specify that charged component and prescription in CH1-5U-q. With it, `¬CH1-5U-q` refutes CH1-5U-i. The family also has charge magnitudes at least 9 and 15 in its other sectors. A theorem excluding all light charged excitations of modulus at least 3 would refute the target directly. The question is dynamical and is not settled by local carrier representations.

**Theorem 5.1 (Q3).** An operator on one site's `Λ(C⁵)` commutes with every `Γ(g)`, `g∈U(5)`, exactly when it is a function of the site number `N_x`.

*Proof.* The `Λ^k C⁵`, `0≤k≤5`, are irreducible and pairwise inequivalent: the center acts with distinct charges k. Schur's lemma makes the commutant the span of their projectors, which are polynomials in `N_x`. □

For a proposed on-site interaction `V(N_x)`, changing occupation from `n` to `n+q` changes that term's energy by `V(n+q)−V(n)`. The proposed 1+1-dimensional five-mode chain test was not run. The draft's assertion that it would merely print its input, or that four sites cannot distinguish a light composite from a finite-size level, is not established: hopping, gauge dynamics and finite-size scaling affect the spectrum. Such a test would be a guide, not a proof of 3+1-dimensional CH1-5U-q.

**Proposed four-test readings, with pass-1 results.** No item is adopted. (a) K as continuum structure: pass 1 says pass on tests 1–4 and calls it forced; the microscopic parity identity supports compatibility but does not itself establish all K backgrounds. (b) “global-anomaly type” as pullback: pass 1 says pass on all four; it is a definition, and completeness remains open. (c) an added strongly coupled gauge group: pass 1 records fail, fail unless specified, fail, fail; the claimed automatic settlement of CH1-i by adding it is not proved, though it changes the law. (d) c-number links replacing registers: pass 1 records fail, pass, fail, fail; the replacement changes PS-6r, while the claimed automatic settlement of bridge Y2 is not proved. (e) CH1-5U-q: pass 1 says pass on all four as an open question; its claimed implication from CH1-5U-i is conditional as above. The tests concern target fit, openness, whether a downstream question is settled by premise, and unneeded added structure, respectively.

## 6. Check record and limits

Pass 1 reports scratch checks, not proofs: (1) matching 16 weights for eight line values `|u|≤40`; (2) linear and cubic traces at 30 random integer points for each; (3) characters `16,0,0,0,0,−16` for `u=−33,−23,−13`; (4),(8) the quadratic index identity at random traceless points and the seven SU(2) partitions of 5, with index set `{20,10,5,4,2,1,0}`; and (6) phase solutions modulo `n=2,…,30`. The scratch code and output are not included in the supplied source and were not rerun here. The general proofs above do not rely on those checks.

The anomaly interpretations rely on standard results attributed in the draft to Atiyah–Singer, Witten, Tachikawa–Yonekura, García-Etxebarria–Montero, Hsieh, and the η-invariant anomaly framework. The exact outside hypotheses were not independently verified in this pass. A targeted literature lookup found [Davighi and Lohitsiri, Anomaly interplay in U(2) gauge theories](https://www.repository.cam.ac.uk/items/330c9a0f-f3c6-4e9d-9c33-efa03b0f8eb0), which concerns a different group and does not establish A5, and [Debray et al., What Bordism-Theoretic Anomaly Cancellation Can Do for U](https://doi.org/10.1007/s00220-024-04937-4), which illustrates the bordism/anomaly distinction but does not verify the claimed K computation. The independent referee must check these inputs, the unverified source dependencies and all GAPs before any amendment.
