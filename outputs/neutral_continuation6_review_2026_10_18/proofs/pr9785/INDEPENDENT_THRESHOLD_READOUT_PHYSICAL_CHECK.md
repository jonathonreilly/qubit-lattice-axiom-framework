<!-- Original PR9785 source SHA256 a173a47f05663fff2c6660de0b28e77e483bee5eedc1c8cc20bcc10f9e3f325f. -->
**Source boundary:** Complete mathematical argument follows. Historical verdicts, execution narratives and provisional instructions are provenance only. Exact identities and conditional mathematical implications remain live; no audit status or additional physical premise is conferred. Earlier exploratory statements are read with their explicit later corrections.

# Independent check: actual-H transfer of the threshold readout measure

Checked the ACTUAL microscopic transfer section of `/tmp/neutral_threshold_readout_root.md`, using the previously established fixed-order local coefficient bound, ground-orbit construction, and low-energy source estimates. The threshold resolvent/limiting measure formula itself is outside this focused check and must pass its separate review.

## 1. Linear ray-moment growth is sufficient and valid

Let W be multiplication by ell+1 on the two rays and a constant on the transverse host. Native K4 has bounded hopping and bounded degree, and changes W by at most a fixed constant on each edge. Therefore [W,K4] extends to a bounded operator, uniformly in the coupling parameter near the declared threshold and in finite periodic-host/clamped-ray approximations. On the compact root source f,

    ||W exp(-is K4) f|| <= ||Wf|| + |s| ||[W,K4]|| ||f||.

One can prove this first with capped W and finite graphs, then pass to the limit; the commutator bounds are uniform. The uniform-in-time closed-ray moment lemma for a below-ray spectral projector is not needed here. The complete source includes energies for which such a spectral gap need not hold, so using linear moment growth instead is important.

The existing coefficient estimate ||(Dj-Evac,j)phi||<=Cj||Wphi|| applies to these vectors. It is independent of transverse separation because the vacuum-subtracted local terms have to intersect a down-spin neighborhood; the two-column interval has O(ell) sites, not a volume proportional to its transverse separation. Fixed-order support enlargement must remain included. The fixed finite sum j>=2 is consequently bounded by C J lambda²(1+|s|) along the K4 evolution. This step uses the established local-count lemma, not operator-norm smallness on the entire N4 sector.

## 2. Duhamel powers and source normalization

At physical time t=tau/(J lambda delta), coefficient time is s=tau/delta. Variation of constants gives, on the normalized root source embedding,

    evolution error <= C lambda (|tau|/delta + tau²/delta²)
                        + C lambda^28 |tau|/delta
                        + finite-size tails.

The second term is the global order-40 normal-form remainder and ground-energy-reference error. The powers and J cancellation are correct.

Write the transformed actual source vector as lambda T f+epsilon, with ||epsilon||<=C lambda² plus the smaller ground/normal-form errors. For bounded F, replacing the source vector changes its quadratic functional by O(lambda³), using the source norm O(lambda). Dividing by the proposed scale lambda² W0 delta log²(1/delta) gives O(lambda/[delta log²]), as stated. Centering and any residual elastic contribution are covered by this vector estimate; the leading ground source is the N4 root vector, not a freely selected mode.

For F in C_c^infinity, Fourier functional calculus and the finite weighted moments of its Schwartz transform turn the Duhamel estimate into coefficient-level quadratic-functional error O(lambda/delta²). Restoring the source factor lambda² and dividing by the measure scale gives

    O(lambda/[delta³ log²(1/delta)]).

This tends to zero for delta=lambda^alpha with 0<alpha<1/3. The strict range is sufficient; no endpoint improvement is needed for the claim. All centering oscillatory phases have modulus one and cause no additional norm loss. This calculation compares test-function integrals, not pointwise spectral densities or individual exact eigenvalues.

## 3. Explicit finite-volume and long-Fourier-time control

A concrete compatible cutoff is |tau|<=lambda^-1. The largest coefficient time is then O(lambda^(-1-alpha)), while the largest physical time is O(J^-1 lambda^(-2-alpha)). Both are much smaller than L~lambda^-4 for alpha<1/3, even using an ordinary finite-range microscopic/normal-form Lieb-Robinson speed rather than an improved lambda-sized speed.

On this time interval, periodic-host/clamped-ray versus infinite coefficient-fiber propagation from a root source has exponentially small wrap/cutoff error by finite-range propagation bounds. For ground-orbit independence, localize evolved local source terms to balls with radius less than a fixed fraction of L. Unions with the other finite local source support cannot cover an entire column, so different ground backgrounds have zero cross matrix elements, while plane symmetry equates diagonal ones. Polynomial factors from the normalized spatial Fourier sum are dominated by the exponentially small localization remainder. Fourier phases have unit modulus; allowed even COM mesh indices retain the previously fixed relative-coordinate boundary convention.

For |tau|>lambda^-1, use bounded unitarity and source norm, rather than extending Duhamel or ground-orbit locality to arbitrarily long times. After division by the measure scale, this tail is bounded by

    C/(delta log²) integral_(|tau|>lambda^-1) |Fhat(tau)| d tau.

Schwartz decay makes it smaller than any selected power of lambda by choosing a sufficiently high fixed tail bound. Thus the long-time integration does not require an infinite-time ground-orbit or finite-to-infinite propagation assertion.

The nearest allowed momentum must be handled as in the existing threshold-window argument: either tune the continuum parameter to the actual mesh point and define delta there, or retain the established mesh error O(lambda^4 log²) in the binding scale. Silently substituting a different finite-box binding energy would be unnecessary and potentially misleading.

## 4. Every-ground premise

The earlier actual-ground approximation and plane-orbit/locality argument are sufficient for this transfer if kept in their stated form. No assumption that an arbitrary actual ground vector is a translation eigenvector is needed. One must retain the earlier proof that the first source coefficient is lambda T f uniformly over the ground orbit; projector proximity alone would not establish that identity. Mixtures then follow by linearity with the same uniform constants.

## 5. Separate finite-M dynamical corollary

The proposed corollary to FIXED_OCCUPATION_LADDER_PROOF.md is valid. Exact spectral projection commutes with H, so normalizing the projected quasimode preserves its O_M(J lambda²) residual about the additive center. For W_M|m>=psi_m, the operator defect (H-Eg)W_M-W_M omega n has norm bounded by the square root of the sum of squared column residuals. Fixed M absorbs that factor. Hence

    ||exp[-it(H-Eg)]W_M-W_M exp(-it omega n)||
      <= C_M J lambda² |t|.

At the stated times this is O_(M,S)(lambda/delta). This strengthens prepared-span finite-time dynamics but does not make that span exactly invariant or close the full source algebra.

## Conclusion

The actual-H transfer powers, local moment control, and finite-volume/Fourier-tail steps are sound with the explicit cutoff above and the prior uniform ground/source lemmas. If the separate coefficient spectral-measure theorem is established, this supplies its actual-ground original-readout weak/test-function transfer for alpha<1/3. It does not transfer an isolated microscopic pole, a pointwise line shape, or an infinite-time scattering matrix.
