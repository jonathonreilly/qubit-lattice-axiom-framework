# Distinct check: limiting mass-tuned mediator family

## Required correction and disposition

The reviewed original `mediated_mass_tuned_family/PROPOSAL.md`, SHA256 `37736cb921b2f0e3e3c6fef9042225a0b44770bd8c58dba78807b04658bef288`, has one incorrect first derivative: V'(0) must be sqrt(2C), not sqrt(8C). The displayed preceding equation 2sqrt(8)V'(0)-8sqrt(C)=0 itself is correct. W'(0)=C/2 is correct. This factor-two error does not enter the implicit-function existence proof or any finite-length estimate. All other stated mathematical conclusions receive conditional support at their expressly local, selected-channel linear-model scope. Root preserved that revision as ORIGINAL_37736cb9.md and corrected exactly the displayed V derivative. I inspected the complete one-line diff and verified both hashes. Final corrected source `d01ed6b60f3bacf2b7557687995902f8c3e172eafecd7a1547cb3bc458451883` receives conditional support without remaining required correction. The original hash remains `37736cb921b2f0e3e3c6fef9042225a0b44770bd8c58dba78807b04658bef288`.

## Reconstructed equations and local solution

The exact mediator Taylor derivative gives c_l=gamma_l^2 d_n and positive linear mass factors because E-H subtracts the self-energy. In the length limit these are Z0=1+u, Z1=1+u+v, Z2=1+v+w. Source-only constant congruence divides the first two hopping magnitudes by sqrt(Z0 Z1) and sqrt(Z1 Z2), and the port hopping by sqrt(Z2). The port and all background coordinates are left fixed. These are algebraic coefficients, not physical state normalization factors.

Substituting the stated hopping magnitudes into A2^2=8 A1^2 cancels the common length exponent and gives v^2(1+u)=8u^2(1+v+w). Substitution into K^2=3sqrt(3)j A1 cancels r^(2m-2) and gives w^2 sqrt(Z0 Z1)=3sqrt(3)j J_m d_infty u Z2. Thus C and both equations (1), including their powers and positive square roots, are correct. This replaces the earlier bare-gamma correlations; imposing both sets simultaneously is not part of the construction.

After u=epsilon^2,v=epsilon^2 V,w=epsilon W, dividing the two equations by epsilon^4 and epsilon^2 respectively gives exactly F1,F2. The resulting functions extend real analytically across epsilon=0 near the positive base point. At zero the derivatives with respect to V,W form diag(2sqrt(8),2sqrt(C)), so the analytic implicit-function theorem applies for each fixed C>0. Local uniqueness concerns only the branch near that base point. Continuity keeps V,W positive for sufficiently small epsilon. For physical coefficients only epsilon>0 is used; gamma3 is of order sqrt(epsilon), and is not claimed analytic through epsilon=0.

Differentiating along the solution branch at zero gives

    2sqrt(8)V'(0)=8sqrt(C),
    2sqrt(C)W'(0)=C sqrt(C).

Therefore V'(0)=sqrt(2C) and W'(0)=C/2. Both corrections have positive direction. No derivative value is needed to invoke the theorem or to prove the later finite-length bounds.

All three gamma_l tend to zero, while J_m+q<2j implies the positive fixed margin 2j-J_m>0. Hence sufficiently small positive epsilon satisfies every listed installation inequality, as well as the optional gamma_l <= (J_m-q)/4. This is an existence statement with exact supplied correlations. It does not provide a numerical allowable epsilon, global uniqueness, a native implementation or a tolerance guarantee. Fixed coefficients do not depend on m.

## Exact finite-length comparison

The finite geometric sum gives d_n=d_infty(1-r^(2n)). For n1=n2=2m-1,n3=m, the three finite masses in the target follow exactly. Since 0<r<1 and 4m-2>=2m for all integers m>=1 (equality at m=1), every difference Zi-Zim is nonnegative and no larger than delta_m=(u+v+w)r^(2m). All masses are at least one. Integrating the derivative 1/x of log on the interval between Zi and Zim therefore proves |log(Zim/Zi)|<=delta_m, without a small-delta assumption.

The actual finite linear-model first ratio is (v/u)^2 Z0m/Z2m; its limiting value is eight. Its log discrepancy is exactly log(Z0m/Z0)-log(Z2m/Z2), bounded by 2delta_m. The second normalized ratio has log discrepancy one half log(Z0m/Z0) plus one half log(Z1m/Z1) minus log(Z2m/Z2), again bounded by 2delta_m. Exponentiating an absolute log bound gives the claimed absolute relative error exp(2delta_m)-1 on either side of one. It does not give exact tuning at finite m.

With lambda_m=Lambda r^(2m-2), the identity delta_m=(u+v+w)r^2 lambda_m/Lambda is exact. For fixed supplied coefficients the relative discrepancies are consequently O(lambda_m) as m grows. The constant can be large and depends on epsilon,J_m,q,j; this is not a uniform bound over all suppliers or continuous lambda tuning. It corrects the limiting ratio defect of the earlier bare-ratio family only at this specified linear-model level.

## Physical and verification limits

The port retains c3 z and its full nonlinear self-energy; source-only congruence does not remove it. Normalizing the port would alter all attached contacts. Higher hopping terms have the length-dependent relative expansion n_l z^2/(J_m-q)^2 and the diagonal Taylor remainder remains cubic with the displayed resolvent envelope. A shrinking-energy-region and tail argument is still required for a physical pulse; a fixed-band approximation is not supplied by the m limit. No complementary-channel or ordered loaded-background inverse follows from the selected scalar calculation.

The corrected stationary installation `d2b7b435f6813847a0b293d5584a3aa5af844a02be09a95b768adc4ea4f963e3` replaces, rather than adds to, the existing j n_p cap. The completed scoped installation recheck, `2cea5e9a3cd59b63d09bf21c1ddb929fff2251f9044ed3bd7189b3df10062ff8`, was read in full and supports that replacement without changing the mediator formulas. The target’s pending label records its authorship chronology; that specific dependency is now discharged within the stationary scope. This review does not certify the formerly doubled cap. J_m denotes the new supplied mediator bond, not the calibrated processor J. The endpoint sign gauge and seed-to-port phase (-1)^m remain physical comparison obligations.

I refreshed the complete local product-seed witness check, SHA256 `aac24f84f9373a5e59511195e717780d24ecffc41c1e4cb878bcf262a4085630`, concerning witness source `57892f7690a5f634c44c2fe0752c5cfb682d3fbfbda1aa4c1ca4edd45bb0fdee`. Its local residual construction does not require the old bare-ratio gamma identities. Its fixed-coefficient preparation allowance is bounded by gamma1 sqrt(d_infty), and does not vanish with m alone. That allowance is an upper certificate, not a leakage lower bound or a no-go. I reuse that distinct check only to qualify the target's discussion, not to claim a loaded output theorem or recertify the witness.

Root authored this new candidate and the prior linear-mass diagnostic. I authored the isolated and stationary mediator ancestors and checked the diagnostic, so there is substantial shared source exposure. The new IFT, coefficients and finite-length inequalities were reconstructed here as a distinct check of root's work. The earlier diagnostic review is `4195db1eb9b15ed68397350433981ffd0ba9d31815161927beb0a57eb02c05e1`, for source `51b3461c0ed92f304a34cc97f017e1cda53876ec5904b0868682dfe09dffc44d`. This is not blind independent calibration, a complete performance point or retained audit status.

Only this review was written. No source edits, numerical root solving, scientific execution, parameter sweep, Git/canonical/PR/checkpoint/prompt/model changes or delegation occurred.
