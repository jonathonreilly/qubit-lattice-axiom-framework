# Perturbed three-site attachment: distinct analytical check

**Conditional support; no necessary correction found.** The stated six-block realization, complementary reference margin, ordered full-fiber inverse criterion, exact detuned installed sixth moment and all-input concentration bound are valid within the supplied domains and unchanged background premises. This check does not establish an actual outgoing-wave tolerance, local escape, finite-time complete-output accuracy or useful perturbed operating point.

Checked complete source: `three_site_perturbed_attachment/PROPOSAL.md`, SHA256 `f32b28aba669d09933c9c22052b2abce4d68339f43faa5beac8f3dc4d8ee978d`. The source remains unchanged. The controlling sufficient conditions are chi<1 for the reference and Theta_eps<1 for the loaded inverse. Failure of the latter inequality would be a failure of this sufficient estimate, not a demonstrated physical resonance or no-go.

## Exposure and selected scope

I did not author this perturbed attachment or its new scalar-robustness source. I authored the prepared-core dwell/recovery proposal and the subsequent nominal three-site complete-output composition, and have authored or reviewed related source/interface ancestry. Root exposed this target and the requested inverse/positivity/moment scope. This is a distinct, source-exposed same-model analytical check, not blind or model-diverse independence and not a new validation of the original calibration.

I read the complete target, the complete scalar-robustness source `32456b0b...`, and its complete root review `ba06cef2...`. Their exact identities are listed below. The nominal installation, full-fiber inverse conventions, scalar moment and unchanged wide-background arguments were already read completely in the preceding coherent tasks and are reused only at their verified identities. The new closed-channel bounds, multiplication order and every third-power component are reconstructed here rather than inferred from status labels. Scalar packet stability is not imported as an installed-apparatus performance result.

## Positive installation and unchanged background

Since q=1-3eta lies in (0,1] and B_eps>=20epsilon, the strict assumption B_eps/q<1 implies epsilon<1/20. The parameter domain therefore gives positive nonzero couplings and, even using the larger scalar domain eta<=1/16,

    kappa/j<=sqrt(3eta(1+epsilon))<1/2,
    a2/j<.13, |d_i|/j<1/320,
    (a1+a2)/j<3eta sqrt(1+epsilon)<.193.

The structured port block has the full-space eigenvalues 0, j-kappa, j+kappa and 2j, so it is PSD. The two Q_a blocks are PSD. The least occupation margin at s2 is greater than j(1-.13-1/320)>0; at s1 it is greater than j(2-.193-1/320)>0; and the s0 coefficient is also strictly positive. Negative detunings cause no positivity failure in this specified domain.

Summing the one-head diagonals gives

    s2: j+a2+(j+d2-a2)=2j+d2,
    s1: a1+a2+(2j+d1-a1-a2)=2j+d1,
    s0: a1+(2j+d0-a1)=2j+d0.

The port retains its existing j plus the j from the structured port block, hence 2j. Principal compression away from all three source heads leaves exactly j n_p, independent of kappa, and no contribution from the other five listed blocks. Thus the original emitter-free H_bg and full8 kernel G are unchanged. This is the fact that licenses reuse of the background comparison; no nominal-emitter inverse is transferred.

All detunings multiply the full internal identity. They cannot secretly change with old energy, parity, record or source excitation. The source occupations vanish on blank heads and introduce no new vacuum scalar. Shared B is still counted once. The d_i are retained in the local source operator, while c_att and the original energy centers remain fixed. They are not removable input-dependent phases. The nominal geometry, selective installation assumptions and unmerged block counts are unchanged.

## Reference determinant: selected and complementary inputs

The scalar-reference matrix is a functional-calculus function of self-adjoint D. On the selected channel the scalar robustness proof gives

    |q_ref,eps(delta)|>=m_eps(delta^2+lambda^2)^(3/2),
    m_eps=(1-3eta)-B_eps>0.

That proof's nominal margin 1-3eta is weaker than the nominal square-root margin, but valid. It retains the physical m_j rather than replacing the load by an imaginary constant. The selected numerator estimate is also valid:

    |delta-d_i|<=|delta|+epsilon lambda
                <=(1+epsilon)sqrt(delta^2+lambda^2),
    |P_eps(delta)|
       <=[(1+epsilon)^2+(1+epsilon)/3](delta^2+lambda^2).

This selected estimate alone would not control the full internal inverse. The target supplies the missing complementary estimate separately, and I checked it directly.

For a complementary eigenvalue |x|>=.185, the physical reference is outside [-2j,2j]. Its real root satisfies |m_j(x)|<=1/j on BOTH exterior components. Put t=lambda/|x|<6e-8. Reverse triangle inequalities give

    |P_eps(x)|/|x|^2
      >=(1-epsilon t)^2-(1+epsilon)t^2/3,
    |x-d2-kappa^2m_j(x)|/|x|
      >=1-(3+4epsilon)t.

The first lower factor is greater than 1-6e-9-1.3e-15 and the second greater than 1-1.92e-7. Both are positive. The subtracted term a2^2(x-d0), divided by |x|^3, has magnitude at most

    (8/3)(1+epsilon)t^2(1+epsilon t)<1.1e-14.

Therefore the product of those two lower factors minus this last allowance is greater than .9999997, and in particular greater than .99. This argument uses absolute values separately on both energy signs. It does not assume the perturbed determinant is odd; general detunings destroy that symmetry.

An upper triangle inequality gives |P_eps(x)|<1.000001|x|^2. Hence

    |1/q_ref,eps(x)|<1/(.99*.185^3)<170,
    |P_eps(x)/q_ref,eps(x)|<1.000001/(.99*.185)<6.

These are uniform bounds for the full complementary subspace by the spectral functional calculus. No channel-count factor is required. They include the wrong-window prepared vacuum direction and all excited directions. Both reference lips have the same real complementary roots.

The selected inverse envelope dominates 170 throughout the retained interval: m_eps<=1, |delta|<=2.4e-8 and lambda<=1e-8 imply

    m_eps(delta^2+lambda^2)^(3/2)
       <=(2.6e-8)^3=1.7576e-23.

It is consequently safe to use that selected envelope as a norm ceiling for the entire reference inverse, while retaining the much sharper 170 when applying it to complementary INPUTS. This does not assert that the actual loaded inverse is diagonal.

## Exact ordered elimination and loaded conditioning

Write A=A2-kappa^2G, with A_i=D-d_i I. Substituting the target's three columns gives the following row identities, with Q_eps^{-1}f on the right:

    row 3: -a1 a2 A + A a1 a2 = 0,
    row 2: a1(A1 A-a2^2 I)-a1 A1 A+a1 a2^2 I = 0,
    row 1: A0(A1 A-a2^2 I)-a1^2 A
            =(A0 A1-a1^2 I)A-a2^2 A0=Q_eps.

Thus the first row equals f and the other two vanish. No G factor is commuted through A0 or A1. The scalar couplings are the only factors reordered in these substitutions. Conversely homogeneous row 3 solves for psi1 from psi2 because a2>0, row 2 solves for psi0 because a1>0, and row 1 gives Q_eps psi2=0. Invertible Q_eps therefore implies invertible S_eps without inverting a possibly resonant A_i or A.

Subtracting the reference leaves exactly

    Q_eps=Q_ref,eps-kappa^2 P_eps(G-m_j(D))
          =Q_ref,eps[I-kappa^2 Q_ref,eps^{-1}P_eps
                                                  (G-m_j(D))].

The actual deviation stays on the RIGHT. Only the reference quantities are functions of D. Applying the selected and complementary estimates above to Q_ref,eps^{-1}P_eps gives the target energy-resolved majorant. Its uniform bound follows from

    1/sqrt(delta^2+lambda^2)<=1/lambda,
    |delta|/sqrt(delta^2+lambda^2)<=1,
    |delta|<=d.

This proves precisely

    Theta_eps=kappa^2[(A_eps/m_eps)(a0/lambda+b0)
                                          +6(a0+b0d)].

Under Theta_eps<1, Neumann inversion gives Q_eps^{-1}=(I-K_eps)^{-1}Q_ref,eps^{-1}. Applying the reference inverse first to P or C proves all three bounds in (8). In particular the complementary input bound is 170/(1-Theta_eps) for its FULL output vector, including load-induced mixing into the selected output. It is not a selected-row truncation.

At epsilon=0 this sufficient criterion is looser than the sharper nominal Theta3; the target explicitly acknowledges that. This is not an inconsistency or an implicit claim of necessity. As m_eps approaches zero the displayed estimates deteriorate, and no fixed useful tolerance is supplied.

The same reasoning must be repeated on the actual lower lip. Q_lower is generally not Q_upper-adjoint because of the noncommuting factor order. The target correctly avoids that false identity. With the unchanged complete background matching, physical-root separation and strictly positive margins on the compact windows, local root continuation and continuity of the finite inverses give regular seed boundary values. These physical premises support the stated absence of hidden singular seed mass inside the windows. The algebraic scalar margin alone would not establish that spectral conclusion. No conclusion about outside spectral types follows from this regularity argument.

## All four detuned third-power components

Fix the ORIGINAL center E_e=c_att+2j+e on a prepared K-energy range, and suppress its common vacuum internal vector. The detunings act as scalars there because B iota=iota K and the source heads have no other head-dependent contact. Direct multiplication gives

    H_e |s0>=d0|s0>-a1|s1>,
    H_e^2 |s0>=(d0^2+a1^2)|s0>
                    -a1(d0+d1)|s1>+a1 a2|s2>.

Applying H_e once more yields:

| Head | Coefficient of H_e^3 | Origin of the terms |
|---|---|---|
| s0 | d0^3+a1^2(2d0+d1) | Seed diagonal plus the return from s1 |
| s1 | -a1(d0^2+d0d1+d1^2+a1^2+a2^2) | Terms from all three source heads |
| s2 | a1a2(d0+d1+d2) | The detuned two-hop component and its next diagonal |
| p | -a1a2 kappa | First arrival at the background port |

The new s0 and s2 components vanish in the nominal undetuned case but cannot be dropped here. The mixed d0d1 term in s1 and all three detunings in s2 have the stated signs. The third application has just reached p; neither its diagonal nor downstream interactions have yet acted on that component. Shared internal/contact structure beyond p therefore does not enter this sixth moment, though it still governs later dynamics.

The four head supports are orthogonal, with the same prepared internal norm. All coefficients are real. Squaring their norms proves the exact mu6_eps in (10), including the port term. In the bounded one-head operator this is an ordinary compressed sixth-power identity. For an unbounded generalization it is correctly interpreted as the third-power quadratic form with the required prepared-vector domain. A formal path expansion would not waive that domain condition.

For the uniform envelope, the respective absolute coefficients are bounded by

    lambda^3[epsilon^3+epsilon(1+epsilon)],
    3a1 lambda^2(1+epsilon+epsilon^2),
    3epsilon lambda a1a2,
    a1a2 kappa.

Use a1^2<=lambda^2(1+epsilon)/3 and a1^2a2^2<=8lambda^4(1+epsilon)^2/9. Their four squared bounds are exactly

    lambda^6[epsilon^3+epsilon(1+epsilon)]^2,
    3lambda^6(1+epsilon)(1+epsilon+epsilon^2)^2,
    8epsilon^2lambda^6(1+epsilon)^2,
    (8/3)jlambda^5(1+epsilon)^3.

Their sum reproduces (11). In particular the port-reaching contribution is of order jlambda^5 and has not been replaced by a lambda^6-only estimate. At epsilon=0 the exact and upper-envelope expressions both recover 3lambda^6+(8/3)jlambda^5. The original centers are used throughout; no favorable resonance shift or discarded detuning phase was introduced.

## Actual concentration, references and limits

For each prepared old-energy range, the spectral theorem applied to the exact sixth moment gives sqrt(mu6_eps)/d^3 as the outside-width-d STATE norm. The common-union complement I^c is contained in either respective outside interval. For an arbitrary input split into its two orthogonal input-energy components, triangle inequality followed by Cauchy--Schwarz gives the stated sqrt(2mu6_eps)/d^3. This does not assume their omitted output images are orthogonal or that actual H commutes with K. Squaring the norm bound gives the positive-operator statement in (12).

The initial record0 remains coherent. Passive-reference tensoring preserves the operator norm and the positive-operator inequality. Every outside spectral type and every output coordinate is covered, not only seed return or the scalar reference density. This moment statement needs the actual local prefix and domain assumptions, but does not need the loaded inverse condition or successful emission. It remains valid with a compatible finite downstream cap. The infinite-ray boundary inverse/regularity claim is not thereby transferred to a finite spectrum.

For a later complete-output composition this actual omitted-state allowance must be charged once globally. The scalar robustness result does not supply perturbed actual source/core escape, both physical traveling terms, a fixed common output with literal W/K/c_att, or a useful finite cut. The present source correctly leaves those obligations open. No nominal .0006 complete-output ceiling, tolerance independent of all other device errors, native precision supply or permanent storage result follows from the present review.

## Exact source identities and work performed

| Source relative to the renewal directory | SHA256 |
|---|---|
| three_site_perturbed_attachment/PROPOSAL.md | f32b28aba669d09933c9c22052b2abce4d68339f43faa5beac8f3dc4d8ee978d |
| three_site_source_robustness/PROPOSAL.md | 32456b0b5c99ad1acfcdc9a770d022ffcc14069dee157981c715177cfa6a7eb6 |
| three_site_source_robustness_check/REVIEW.md | ba06cef2ddf0aae45eeaf5f5c8740258babe21d2a8206fbf6c1eb7b3b33f97ad |
| three_site_actual_attachment/PROPOSAL.md | 4278633f3436008a770088331a2424d3f42dda06d08853dfe18d9b8a6554f006 |
| three_site_actual_attachment_check/REVIEW.md | ede902f9c1bebc768147e459894f98610689f33655f87d01d91d07531cbd157d |
| three_site_loaded_inverse/PROPOSAL.md | 7a154f66dd52ce70745e010641eaa98cffab8ededbeb9972139c3cbd10135672 |
| three_site_loaded_inverse_check/REVIEW.md | 8ddded69f6c5758650c166c8adbc3c05346478e81d4636b8bc5e226f365c9ca2 |
| three_site_product_source/PROPOSAL.md | a89025dafcb588459e88c14fa802e9e9ce2e5184aa42d9d22f6521a1dadb4823 |
| three_site_product_source_check/REVIEW.md | c161daea2f3a126ad84baaa63d975b5d80fd3243f11ca3b1075673f62530245b |
| slow_lead_wide_endpoint/PROPOSAL.md | c4c99408686166ba4d80bc973f5c22afdd1185bbf38e4539512dc26afd5cd5e3 |
| slow_lead_wide_endpoint_check/REVIEW.md | c6cc2ed747956e70bba1a7af3a5d65d3d36a7f708367727cb6f5e8a74386feb5 |

The original canonical source/calibration/B identity remains `71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff`; it is inherited within the stated scope, not rederived or recalibrated here. Nominal source evidence and its historical qualifications remain unchanged.

This review used analytical reconstruction and deterministic file/hash inspection only. No scientific program, numerical inverse, spectrum, parameter sweep, dynamics or tolerance optimization was executed. No original source, W, Git, PR, checkpoint, editable prompt, axiom, model or publication state was changed. Only this review was created. Its conditional support is a selective scientific check, not an independent retained audit verdict or authorization to claim full-device robustness.
