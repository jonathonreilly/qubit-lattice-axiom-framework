# Selective local check: fixed-spectrum orientation scope

Verdict: the rotation, derivative bounds, detuning correlation and supplier interpretation are correct on the intended nonnegative-coupling branch, with one substantive wording correction about a sufficient angular tolerance and two domain/sign clarifications below. This is a narrow source-exposed algebra check, not independent discovery, a full-device review, or acceptance of any simultaneous perturbation/runtime composition.

## Source identities and exposure

Read completely:

- Root's assessment in this directory, SHA256 `25221ebc70b09702b38aa626410f7760c57968d732b2c0b620c46fda548afaa3`.
- `../endpoint_precision_root_notes/FIXED_EIGENVALUE_INTERFACE.md`, SHA256 `548c8579d603200db45c7c7f4fdd3f2cef08aee53846efe524ef94591b692057`.
- `../endpoint_fixed_spectrum_interface_check/REVIEW.md`, SHA256 `d370f70e5232904389368434a18a88407d30474b98b030a03c96e4d2e24fc7ce`.

The cited fixed-spectrum review pins its nominal canonical body to `bc75051b87d62e65ea7953f11c2fcd320f1a9ab853c7a346f32e9314859cb1a5` at the earlier milestone. That is the provenance of its full-space convention; I did not silently replace it with a later append. The exact q0,J,kappa0 data needed here are explicitly supplied in the assessed source. I authored related structural/precision proposals and have prior source exposure; this is selective reconstruction after reading the root's claim, not a blind independent origin. Previously read unchanged local workflow is reused. No scientific execution, diagonalization, computation sweep, delegation, W/Git/checkpoint/prompt edit or model/effort change occurred. Only source reads/hashes and this report write were performed. The assessed source was not edited.

## 1. Rotation and branch

For U(theta)=[[cos theta,-sin theta],[sin theta,cos theta]],

    U diag(lambda_minus,lambda_plus) U^T
      =[[lambda_minus+R sin²theta,-R sin theta cos theta],
        [-R sin theta cos theta,lambda_plus-R sin²theta]].

Thus the stated sign corresponds to this real rotation convention. With g=J-E0>0, R=sqrt(g²+4kappa0²), theta0=atan(2kappa0/g)/2 in(0,pi/4), one has R cos2theta0=g and R sin2theta0=2kappa0. Substitution gives exactly the nominal diagonal entries E0,J and offdiagonal -kappa0.

On 0<=theta_a<=theta0, kappa_a=R sin2theta_a/2 is monotone, lies in[0,kappa0], and Delta=R(sin²theta_a-sin²theta0)<=0. Equal trace and determinant give

    g Delta-Delta²=kappa_a²-kappa0²,
    Delta=2(kappa_a²-kappa0²)/
             [g+sqrt(g²-4(kappa_a²-kappa0²))],
    |Delta|<=(1-r²)kappa0²/g.

These formulas recover the cited branch exactly. Vacuum0 and double occupation E0+J agree with the full-qubit convention in the cited review; positivity follows from keeping the positive nominal eigenvalues and those outer sectors fixed. This is a static block parameterization, not a preparation gate. The background endpoint displacement -Delta remains a real physical change, not a supplied theorem margin.

## 2. Angular derivatives and the tolerance-direction correction

Write s0=sin2theta0=2kappa0/R. For 0<=r<=1,

    theta(r)=asin(r s0)/2,
    theta'(r)=s0/[2 sqrt(1-r²s0²)],
    kappa0/R <= theta'(r) <= kappa0/g.

Integrating from r to1 gives exactly

    (1-r)kappa0/R <= theta0-theta(r)
                         <=(1-r)kappa0/g.              (1)

The source's eta>=0 formulation should either require 0<=eta<=1 or explicitly intersect its stated interval with 0<=r<=1. Otherwise eta>1 allows negative r, contrary to the declared nonnegative-angle branch. The intended eta=1e-6 case is unaffected.

For fixed eta in[0,1], the EXACT one-sided angular interval corresponding to r in[1-eta,1] is

    0<=delta_theta<=w_eta,
    w_eta=[asin(s0)-asin((1-eta)s0)]/2,
    eta*kappa0/R <= w_eta <= eta*kappa0/g.             (2)

The source correctly bounds the interval width ABOVE, but its immediately following phrase "This is a sufficient tolerance" is unsafe if interpreted as certifying every angular error below the displayed upper bound. An upper bound on w_eta is an envelope, not a guaranteed allowable radius. Specifically, the source does not establish that delta_theta<4.167e-13 implies r>=1-1e-6. The implication needed for a sufficient angle-only contract uses the LOWER bound:

    0<=delta_theta<=eta*kappa0/R
       implies delta_theta<=w_eta and hence r>=1-eta.  (3)

This remains one-sided; angle increases above theta0 would increase r above1 and leave the stated contract.

Suggested replacement: "The exact one-sided allowed angular width is w_eta in(2), and w_eta<4.167e-13 for eta=1e-6. This upper estimate describes its size; a sufficient allowed angular-error radius is eta*kappa0/R (or the exact w_eta). Neither is a necessary fabrication lower bound." This preserves the valid scale interpretation without reversing the inequality's role.

## 3. Conservative nominal gap without floating diagonalization

For exact q0=4.510351185997098,

    cos k0=(q0²-1)/(q0²+1),
    g=J(2 cos k0-1)=J(q0²-3)/(q0²+1).

Since q0>9/2 and J>3/100, monotonicity of (x-3)/(x+1) gives

    g>(3/100)*(69/85)=207/8500>.024.

This is a direct rational proof with ample slack. At eta=1e-6 and kappa0=1e-8, the upper-width estimate is therefore

    w_eta<=eta*kappa0/g <10^-14/.024
         <4.167*10^-13.

For completeness, a simple explicitly sufficient numerical radius can be given without evaluating R. Since g<J<.031 and 4kappa0²=4e-16, R<.032. Hence eta*kappa0/R>3.125e-13 at eta=1e-6, so every one-sided angular reduction at most3.125e-13 is sufficient for this local r interval. This loose radius is optional; it is not a fabrication lower bound or a device-level certified tolerance. Together the lower and upper width estimates justify the stated order4e-13 scale as a description of the nominal parameter interval.

## 4. Eigenvalue errors and supplied precision

At fixed theta_a, perturbing the two eigenvalues by epsilon_minus,epsilon_plus gives exactly

    delta a=epsilon_minus cos²theta_a+epsilon_plus sin²theta_a,
    delta b=epsilon_minus sin²theta_a+epsilon_plus cos²theta_a,
    delta kappa=(epsilon_plus-epsilon_minus)
                       sin theta_a cos theta_a.

The source's hopping-error formula is correct for the positive coupling parameter kappa, whose matrix entry is -kappa. If "hopping" means the signed offdiagonal entry, its change has the OPPOSITE sign. Naming delta_kappa explicitly removes that ambiguity.

For epsilon_minus=epsilon_plus=epsilon, both one-excitation diagonals change by epsilon and the offdiagonal does not. With vacuum fixed at0 this is not a whole-space global shift. Even if the double-occupation value were adjusted consistently with new eigenvalue sum, the unchanged vacuum and unaffected lead still prevent treating it as a removable global phase of the entire device. Generic independent eigenvalue errors therefore do not follow the orientation-only detuning correlation. Their magnitudes, positivity constraints and spectral effects would need separate assumptions and estimates.

The source correctly describes an explicit structured supplier: exact eigenvalues plus a restricted eigenvector orientation, with a product basis seed retained. Encoding correlated coefficients in one positive block can be a meaningful architectural choice without constituting a native mechanism to supply that spectrum or orientation. The source does not establish a universal obstruction or a necessary precision floor. Nor do the local formulas imply complete spectral mass, source/closed-output bounds or comparison to a fixed nominal waveform. Those remain separate composition obligations, which this review neither assumes nor endorses.

## Disposition

Accept the local algebra and scoped supplier interpretation after distinguishing the upper bound on angular width from a sufficient allowed angular radius, making the nonnegative-r domain explicit, and identifying the eigenvalue-error formula as delta_kappa. No further local mathematical defect was found within the reviewed scope. Full-device claims remain outside this verdict.

## Qualified revision checked before finalizing this review

After the above findings were communicated, root preserved the original and supplied `QUALIFIED.md`, SHA256 `d9b13303f9a2f0aa21ce1991748d66787f3e71b35919f845ac0765ad1be60462`. I read that complete short revision. It correctly distinguishes the upper-width envelope from the sufficient lower-bound radius, restricts eta to[0,1], explicitly names positive kappa versus the signed offdiagonal entry, and supplies the valid exact rational lower bound on g. Those corrections resolve the local issues identified here. The qualified revision is accepted within this selective local-algebra/supplier-interpretation scope; it does not gain a full-device or implementation qualification from this verdict.
