# Independent review of the separate physical mass-gap target

**Disposition: the spectral lemma and scope controls are confirmed. The lattice limit criterion is confirmed after a narrow onset-time clarification, checked in this same reviewer context. No physical infrared estimate, existence theorem or mass-gap theorem is proved by this unit. MG0–MG5 remain open.**

The complete original target, `MASS_GAP_TARGET.md` at `9761471ab46e659ce856e2b9c7c10fef2b06cf5c`, has 130 lines/7323 bytes and SHA256 `d721bd77d36e6f96a1ce408c57d333776e17058a453b8c887ec0daf9f067cedf`. The coordinator's narrowly corrected frozen target has 133 lines/7507 bytes and SHA256 `105440c10b9a2fc91b2be366f439053de05fd3d3497596f8f28993b0fe42de7b`. The complete original was read, then the complete original-to-corrected diff was checked and all other bytes compared unchanged. The corrected source was read with an explicit hash assertion. This report certifies those bytes, not subsequent changes to a working path.

[Pre-stated criteria](checks/review_massgap_target_criteria.md), [complete correction diff](checks/review_massgap_target_fix.diff), [source manifest](checks/review_massgap_target_source_manifest.json) and [freeze receipt](checks/review_massgap_target_receipt.json) bind the scope and evidence. Current-main methodology remains `ca2bc7ddf64790da96cd43d42017d000fbfe4808`, previously read in this same context. Astra/max was requested in the coordinator dispatch; visible model identity is GPT-6, with no separate configuration introspection. This is same-family scoped review, not cross-family, whole-PR or audit certification. Prior determinant and lattice-bridge reports are unchanged. No shared source, git/PR or audit mutation was performed by this reviewer.

## 1. Independent spectral proof

Let H be self-adjoint and nonnegative, with H Omega=0 and ||Omega||=1. The orthogonal complement K=Omega-perp is reducing for H, because Omega is an eigenvector. The bounded operator exp(-tH) is defined on every Hilbert-space vector; the vectors need not lie in the unbounded generator's operator domain. Their spectral measures are finite positive measures.

For fixed F and 0<=b<m_*, positivity of that measure gives

    exp(-bt) ||E_H([0,b]) v_F||^2
      <= <v_F,exp(-tH)v_F>
      <= A_F exp(-m_* t),             t>=t_F.

Thus ||E_H([0,b])v_F||^2<=A_F exp(-(m_*-b)t), and sending t to infinity annihilates the projection. This uses only finite A_F,t_F for that F. They need not be uniformly bounded over the observable family. The exponential rate, however, must be a single positive m_* shared by the family.

A bounded projection that kills each v_F kills their finite linear span and its closure. The assumed dense span is K, so E_H([0,b]) vanishes on K. Taking an increasing countable sequence b<m_* with b tending to m_* gives E_H([0,m_*))|_K=0 by strong monotone convergence of spectral projections. Hence the restricted spectrum lies in [m_*,infinity), and ker H is exactly span{Omega}. An eigenvalue at m_* is permitted; the proof does not assert a strict inequality above the threshold.

This also explains why diagonal reflected correlations suffice. No uniform estimate for every finite linear combination or additional polarization bound is necessary for this projection argument: linearity is used after each vector has already been annihilated. Density of the physical family is essential. A cyclic vector for a selected scalar subalgebra does not imply density in the Hilbert space of the requested complete gauge-invariant local theory.

If K is nonzero, choose nonzero v in K. Since E_H([0,R]) tends strongly to the identity as finite R tends to infinity, some such R has E_H([0,R])v nonzero. The excited spectrum therefore has finite infimum, as well as the positive lower bound. This argument does not construct a one-particle eigenstate or an isolated mass shell. If K were zero, the decay criterion would be vacuous and the excited threshold would not be the required finite one; the separate MG4 obligation correctly excludes that case.

The identification of the Hilbert correlation with centered reflected Euclidean observables, their products and their renormalized domains remains an assumption to be proved by MG0/MG2. Nothing in the abstract spectral argument constructs a Yang–Mills hierarchy or an OS reconstruction.

## 2. Finding and same-context fix: uniform onset and an admissible time window

The original section 3 explicitly made m_* and A_F uniform in ultraviolet cutoff and volume, but did not explicitly do so for the onset t_F. Its proposed proof passes the bound at each fixed physical t to the limiting hierarchy. That proof needs the bound to apply at that t eventually. A cutoff-dependent onset can lose that condition; in the extreme example T_safe(T)=T and t_F(T)=2T, the interval on which decay is required is empty at every cutoff/volume. The constant function C_T(t)=1 would then satisfy the windowed assertion vacuously, and its fixed-time limit has no positive decay rate.

The requested smallest correction was to choose, for each physical F, finite A_F and t_F independent of cutoff/volume, with a common positive physical m_*, and to require the inequality on t_F<=t<=T_safe(volume), with T_safe tending to infinity along the same hierarchy. The coordinator made exactly this change and updated MG3. The saved complete diff shows no unrelated change. I confirmed the corrected hash above in this same context. This closes the quantifier ambiguity; it does not supply the estimate.

With the correction, fix t>=t_F. Eventually t is in the safe range. Assuming the actual renormalized centered reflected correlations converge to the same hierarchy used for reconstruction, their upper bound passes to the limit at that t. If lattice time is discrete, the corresponding convergent admissible approximants to t and the required continuity belong to that same matching obligation. The resulting bound holds for all physical t>=t_F. Only then is t sent to infinity in the spectral proof. No interchange of an uncontrolled large-time limit with cutoff removal has been used.

The constants and time variable must use fixed physical units. A dimensionless lattice spectral gap requires the correct conversion by the time step before it becomes a candidate m_*. The phrase “equivalent physical transfer-operator gap” likewise requires the specified hierarchy, normalization, vacuum centering and continuum matching; positivity of a finite transfer matrix alone supplies none of this uniform quantitative control.

## 3. Counterexamples and controls

The stated two-field quadratic matrix has determinant mu k^2, and eliminating its positive b-block mu gives exactly k^2. At k=0 the full matrix has a zero eigenvalue. Thus an auxiliary or internal massive block is compatible with a remaining massless mode. It cannot prove a physical gap of the reconstructed interacting theory.

A family of positive physical cutoff masses a tending to zero has correlations exp(-at) tending to 1 at each fixed t. Positivity of each cutoff mass alone cannot yield a positive limiting threshold. This is not a statement about an unconverted dimensionless lattice number.

For H=0 on C Omega, H=1 on C v, and H acting by multiplication by x on L2((0,1)), the kernel is precisely C Omega, while the continuous excited spectrum reaches zero. The selected v correlation is exp(-t). For the unit constant function f in the hidden L2 component, the correlation is (1-exp(-t))/t and ||E_H([0,b])f||^2=b for 0<b<1. Its positive low spectral weight prevents every positive exponential rate. This verifies the source's failure of a selected-observable test even with a unique zero-energy eigenvector.

A further common-rate control uses H e_j=(1/j)e_j on ell2(N), in addition to the vacuum. Finite-support vectors have dense span and each has some positive exponential rate, but these rates have no common positive lower bound and the excited spectrum accumulates at zero. Thus replacing a common m_* by m_F would invalidate the lemma.

The [first exact-control script](checks/review_massgap_target_01.py) and [unaltered stdout](checks/review_massgap_target_01_out.json) record **15/16**, with [empty stderr](checks/review_massgap_target_01_err.txt). The one failure was a reviewer implementation error: SymPy structural equality compared an expanded positive polynomial with an unexpanded equivalent expression. It was not suppressed or changed to an all-pass report. The separately pre-stated [diagnostic](checks/review_massgap_target_02.py), [complete output](checks/review_massgap_target_02_out.json) and [stderr](checks/review_massgap_target_02_err.txt) give **4/4**, proving the intended polynomial identity by a zero exact residual and positive remainder coefficients, and reproducing the original structural inequality. These elementary controls are support for the explicit examples; the spectral lemma is established by the argument above. They are not a computation of Yang–Mills correlations.

## 4. Primary-source scope and final boundary

The official [Jaffe–Witten statement](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf), sections 3–4, was read directly. It specifies a quantum theory with local gauge-invariant fields, the relevant axiomatic and short-distance properties, a finite positive mass threshold, and the quantifier over compact simple gauge groups. The target correctly distinguishes its present SU(N) family from that whole group range. These are target specifications, not analytic inputs.

The dated [OpenAI announcement](https://openai.com/index/building-scientific-understanding-with-academic-communities/) was also read directly. It announces Yang–Mills existence and a Lean formalization, and describes deferring release of the physics artifacts to the external collaboration. It does not announce a physical mass-gap theorem. The source's comparison is appropriately restricted to announced scope; no unreleased proof was inspected or used. The external-source access record distinguishes actual reading from separately attempted raw-object hashing, including the preserved initial TLS-certificate failure.

| Claim/interface | Final disposition |
| --- | --- |
| Spectral projection lemma, dense-span extension and unique kernel | Confirmed as a sufficient conditional theorem. |
| Finite excited infimum | Confirmed under nonzero Omega-perp; no particle-state existence inferred. |
| Fixed-time lattice passage | Confirmed after the explicit uniform onset/safe-window correction. |
| Three source counterexamples and common-rate control | Confirmed. |
| Primary-source comparison and SU(N) scope boundary | Confirmed as statements of scope, not proof validation. |
| MG0: complete existence/reconstruction | Open. |
| MG1: actual uniform infrared decay/physical gap producer | Not constructed. |
| MG2–MG3: source transport and cutoff/volume passage | Open; the criterion specifies necessary work for this route. |
| MG4–MG5: surviving excited sector and complete theorem identification | Open. |

No auxiliary gap, determinant cancellation, one-loop coefficient or conditional application of MG1 is counted as completion of the user's existence-and-mass-gap goal. A genuine infrared producer and the complete existence inputs still require construction and independent checking.
