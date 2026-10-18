# Independent two-rung original-source algebra check

Read `/tmp/neutral_two_rung_root.md`. The original-source ladder calculation is consistent under the separately required two-feature residual/N8 projection and low-energy-source estimates. The vacuum extension Fdagger is not assumed equal to the actual source on excited states.

## Exact mixed host identity

Let Phi be the normalized symmetric host pair matrix, Xi the symmetric matrix of Fdagger, and a_h=Tr(Phi dagger Xi). Polarizing the exact quartic spin norm in its ket coefficients, then dividing by two because differentiation of Bdagger squared gives 2Fdagger Bdagger, yields exactly

<B_Hdagger^2 vac,Fdagger B_Hdagger vac>
=2a_h+4Tr(Phi dagger Phi Phi dagger Xi)
 -16sum_i rho_ii (Xi Phi dagger)_ii
 +4sum_(i<j)|f_ij|^2 f_ij* xi_ij.

An independent direct four-site-amplitude enumeration with random complex seven-site pair coefficients agrees to1.15e-16; `/private/tmp/neutral_mixed_pair_control.py`. The complex conjugations and factors are correct.

The trace correction is bounded by ||rho||op ||Phi||HS ||Xi||HS. Translation uniformity gives rho_ii=1/V, so the third term is -16a_h/V. The final term is O(1/V), since max|f_ij|^2<=max_i sum_j|f_ij|^2=2/V and Cauchy-Schwarz bounds sum|f_ij xi_ij|. Hence the mixed deviation is O(1/(Vdelta)) for the specified native host profile and bounded F norm.

For unnormalized host B_H=sqrt(w) B_hatH, a=<chi,Fvac>=sqrt(w)a_h because rays have more than two spin flips. The leading mixed term is 2w a, not 2sqrt(w)a. This is precisely the scaling used in the draft.

## Ray selection and errors

B_H squared has four spin flips, while F B_R has at least six, so their overlap vanishes. B_H B_R has at least six and B_R squared at least eight, so neither overlaps F B_H, which has four. These statements concern flip number, not wall number; they hold before any N8 projection.

The remaining mixed terms are bounded using the previously verified factorization counts. In particular ||B_H B_R vac||=O(eta), ||F B_R vac||=O(eta), and ||B_R squared vac||=O(eta^2). The mixed product is therefore O(eta^2), with still smaller ray-ray versus F-ray contributions. The replacement 2w a by 2a costs 2eta^2 a, also within this bound. Thus

<Bdagger^2 vac,Fdagger Bdagger vac>
=2a+O(eta^2)+O(1/(Vdelta)).

This is sharper than the O(eta) norm comparison because the missing first-order ray cross terms are exactly forbidden by spin-flip count. That selection rule is essential to the fading-source relative estimate.

## Physical source versus its vacuum extension

The N-grade+4 part of the first dressed coefficient is a normalized sum of fixed-support local operators. Its action on a region with the all-up local configuration agrees with the all-lowering pair vacuum extension. The difference can act only within a fixed neighborhood of existing down spins or incident walls. The support must include incident vertical neighbors; otherwise an endpoint extension from an up spin could be misclassified as a vacuum action.

For a compact feature of interval length ell, at most C(ell+1) translated local terms contribute to this difference. Each has coefficient O(1/sqrt(V)), bounded local output multiplicity, and bounded spin-change range. A weighted row/column estimate therefore bounds its action by C/sqrt(V) times a fixed length moment. The uniform ray moments and host ell=1 imply an O(V^-1/2) vector bound on chi, independent of transverse separation. This supplies the claimed extension error rather than assuming the two operators coincide globally. Between N4 and N8 only the grade+4 component contributes.

The stated N8 projection loss of Bdagger squared contributes O(V^-1/2) to the mixed matrix element if its separate contact estimate is valid, because ||Fdagger chi|| is uniformly bounded by the same host/ray product controls. I did not reprove the entire dynamical intertwining/contact-residual lemma in this source check.

Higher fixed-order dressed source coefficients acting on chi have uniform vector bounds by finite-pattern translation counting: far from the existing feature they create the finite vacuum pattern, with a bounded normalized Gram sum; close terms have the local weighted bound just described. Equivalently, union-factorization multiplicities grow only polynomially in ell at each fixed source order. The uniform length moments absorb that polynomial. The translation-independent scalar part cancels for the allowed nonzero Q. Thus their lambda^2-prefactored contribution is O(lambda^2), provided the stated local source expansion and its remainder are retained.

## Relative errors and interpretation

Here a asymptotically sqrt(W0delta)log(1/delta) is nonzero. Then eta^2/a=O(sqrt(delta)log(1/delta))->0. On V~lambda^-12, delta=lambda^alpha with alpha<2/3, both 1/(Vdelta a) and 1/(sqrt(V)a) vanish. An O(lambda^2) higher-source matrix element is negligible relative to lambda a since lambda/[sqrt(delta)log(1/delta)]->0. Dividing the unnormalized mixed overlap by ||P8 Bdagger squared vac||->sqrt(2) yields the coefficient sqrt(2)a[1+o(1)]. The vacuum source extension's norm need not equal one for this identity; its actual bounded normalization is already carried by a and Xi.

The original bare source preserves N, so its matrix element between exact N4 and N8 coefficient vectors is zero. This does not mean it is zero on each sector, nor does it replace the separate source-norm estimate needed after exact microscopic spectral projection. The draft's final projection argument must continue to use its independent low-energy-source lemma; global ||C_Q|| bounds alone would be inadequate.

Momentum is consistent: Bdagger carries Q and its square carries2Q, while C_Q supplies the additional Q in the ladder transition. The accepted even COM mesh convention avoids midpoint twists. The conclusion is a pair of window-vector matrix elements once the dynamical prerequisites are established, not an eigenstate ladder, a canonical commutation relation, or a unique field operator off vacuum.
