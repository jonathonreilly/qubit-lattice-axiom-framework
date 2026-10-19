# Geometric source profile: distinct analytical check

Disposition: SUPPORT at the stated free-profile and standalone lead-term scope. No source correction is required. The physical upper-semicircle spectrum is compared to a separately normalized single-pole profile with its omitted domain paid. The partial fractions, 29rho/8 ceiling, phases, cutoff normalization, integer translation and dispersion/tail estimates are consistent. No finite-router, complete launch-time or resource theorem follows from this check.

## Exact evidence, reads and exposure

The complete changed source was read and its SHA256 verified:

- `common_product_geometric_source_profile/PROPOSAL.md`: `be2ab9da4b62ca7f595c17fea5ec6e62849cdada2c34416154996ad15180538e`.

Paths are under N=`/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934`. Necessary source arguments were completely reread, with identities refreshed:

- `common_product_endpoint_launch/PROPOSAL.md`: `fb72f4ed4af9d6f00d6430ec4997fab3f8fbb978b140692b083ddda5e324e9e4`.
- `common_product_launch_derivative_bounds/PROPOSAL.md`: `378086fdc6b217f9a2eb9d85fdb1ca862a54905be048d298465e0b123722fec8`.
- `common_product_resonance_tail/PROPOSAL.md`: `306174fb0a884c62d5c6de401492a742a3d8a55670ef273f9d376258e531c002`.

I also completely reread `bandcenter_reference_measure_check/REVIEW.md`, the measure check pinned by the launch source as `1953d153c9ac8583202e7ca18bff62829bfbff2373691cc43a5ae152a2a6b0ae`, to inspect its actual mass-one normalization and hard-band domain. Its scalar measure is reused at the stated standalone operator scope; this is not a fresh audit of arbitrary attached apparatus. The resonance survival estimate is not needed for the new free-profile proof and is not independently certified here merely by reading it.

ROOT suggested the single-pole route and supplied this check scope. The author has network/packet ancestry; I authored or checked other launch/component interfaces and read the proposed formulas before reconstructing them. This is a source-exposed, same-model distinct analytical check of the NEW calculations, not blind replication, model diversity or blanket independence for reused premises. No scientific executable, numerical integration, solver, sweep or delegation was used.

## 1. Exact rational identity and physical domain

From cot k=i(z^2+1)/(z^2-1), the denominator in the physical F is

    (2-rho^2)cot k-i rho^2
       =2i[1+(1-rho^2)z^2]/(z^2-1).

Thus F_rat=-d rho z(z^2-1)/(1+a^2 z^2), with d=1/sqrt(2pi), a=sqrt(1-rho^2), including the negative sign. This agrees with the phase-preserving launcher column, not just its modulus. Its rational coefficients are real, so reflection k->2pi-k conjugates it and preserves its modulus. The physical upper-half norm is one by the exact source measure. The full rational continuation therefore has squared norm TWO. Treating it as the original normalized spectrum on the whole circle would be false; the source explicitly retains this failed shortcut.

Direct subtraction of the two resolvents gives

    U_+-U_-=2d rho a z/(1+a^2 z^2).

Multiplying by (1+a^2)/(2a^3) and subtracting d rho z/a^2 yields exactly F_rat. This independently checks the sign, a powers and coefficient b_a. U_+ is resonant at z=i and U_- at z=-i; their roles have not been interchanged.

On the nonresonant half-circle each denominator squared is at least1+a^2. Its interval length pi and d^2=1/(2pi) give exactly L_rho=rho/sqrt(2(1+a^2)). The polynomial contribution on the upper half has norm rho/(sqrt(2)a^2). On the upper half the difference is (b_a-1)U_+-b_a U_--d rho z/a^2; on the lower half it is -U_+. Summing their norm ceilings, rather than incorrectly inserting the lower physical spectrum, gives the stated B_rho.

For x=rho^2, differentiating b_a=(2-x)/(2(1-x)^(3/2)) yields (1-x/4)/(1-x)^(5/2). This is positive and at most (4/3)^(5/2)<9/4 for x<=1/4. Hence b_a-1<=9rho^2/4<=9rho/8. Also b_a<=7/(3sqrt(3))<3/2, L_rho<=sqrt(2/7)rho<3rho/5 and the polynomial norm is below rho. Their sum is at most (9/8+3/2+1)rho=29rho/8. Both compared vectors are normalized, justifying the separate norm-distance cap2. No small-rho asymptotic is used to cover the endpoint rho=1/2.

## 2. Fourier support, normalization and exact free evolution

Since 0<a<1, the expansion of (1+iaz)^-1 converges absolutely and uniformly. With the stated inverse kernel exp(+ink), a term exp(imk) contributes only at n=-m. Thus

    u_(-m)=i rho(-ia)^m for m>=0, u_n=0 for n>0.

The support direction and factor i are correct. The geometric squared norm is rho^2/(1-a^2)=1, with no residual Fourier factor. Consequently U_+ is normalized in unweighted dk. The comparison is not a normalized version of F_rat.

Multiplication by exp(-itE(k)) is unitary on the whole circle for all real t, and inverse Fourier transform is unitary onto the full integer line. The free hopping generator has symbol 2j-2j cos k under this convention. Therefore the free evolved norm difference is exactly its initial spectral difference at every t. Half-line and arbitrary coordinate restrictions contract it, but do not preserve normalization of the individual restricted terms. The exact physical launch decomposition still includes the emitter amplitude AND the conjugate incoming term; those were not removed by this calculation.

The two-path/reference extension is the scalar comparison tensored with identities on orthogonal path/fiber factors. Its operator norm has no additional path count. None of this requires closing a time-dependent contour. The essential singularity at z=0 and the physical upper-half integration domain remain real reasons the earlier residue shortcut is unavailable as stated.

## 3. Real cutoff and actual positive normalization

For g=chi F_up/sqrt(p), both vectors have norm one. Their inner product is (integral chi|F|^2)/sqrt(p), real and at least sqrt(p), because 0<=chi<=1 implies chi>=chi^2. Hence the exact distance formula gives the source's square-root ceiling sqrt(2(1-sqrt(p))). This is a distance between normalized vectors, not merely discarded mass.

When the inherited hard-band estimate is used, its domain is 0<sigma<pi/2, and its useful nontrivial case is P_sigma<1. Then p>=1-P_sigma gives the stated bound, and 1-sqrt(1-P)<=P establishes the further sqrt(2P) ceiling. These are precisely the checked source-measure hypotheses, retained by the phrase “checked hard-band source bound.” Unitary multiplication and spatial restriction give (13), including the cap2. The cutoff need not be analytic, and shrinking sigma must retain the displayed mass cost.

## 4. Dispersion and integer translation

At k=pi/2+s, U_+=i rho/[sqrt(2pi)(1-a exp(is))], so its squared modulus has denominator (1-a)^2+4a sin^2(s/2). For |s|<=pi, sin(|s|/2)>=|s|/pi gives the majorant pi rho^2/(8a s^2). This bound deliberately retains the broad spectral tails; using a narrow linewidth in its place without a paid error would not justify the calculation.

Let m=floor(2jt+1/2). The inverse Fourier transform of exp(-imk)U_+ is u_(n-m). The prefactor exp(-i2jt)exp(im pi/2) therefore makes the comparison multiplier exp(-i2jt)exp(-ims), exactly the linearized multiplier with an INTEGER translation. The residual is 2jt sin s-ms=(2jt-m)s+2jt(sin s-s). The sign and rounding phase are fixed, including at negative times. Integer m makes the comparison multiplier periodic; the intermediate s-based factorization only needs a measurable branch almost everywhere.

Integrating the s^-2 bound after multiplication by s^2 gives integral s^2|U_+|^2<=pi^2 rho^2/(4a). Thus the rounding norm is at most pi rho|2jt-m|/(2sqrt(a))<=2rho|2jt-m|<=rho. The bound covers ties in the rounding rule because their distance is exactly1/2.

For the nonlinear term, Taylor's remainder bound |sin s-s|<=|s|^3/6 gives phase magnitude at most T_d|s|^3 with T_d=j|t|/3. After squaring the minimum of this and2 and using evenness, the required positive integral is

    2C rho^2 integral_0^infinity min(4,T_d^2 s^6)/s^2 ds,
    C=pi/(8a).

Splitting at s0=(2/T_d)^(1/3) gives T_d^2 s0^5/5+4/s0=(6/5)2^(5/3)T_d^(1/3). This yields exactly the proposed squared coefficient 3pi*2^(5/3)/(10a*3^(1/3)), and hence norm growth rho(j|t|)^(1/6). The listed elementary numerical bounds indeed put this coefficient's square below4 uniformly. At t=0 the dispersion term is zero directly, so no division by T_d is used there. Triangle inequality and normalization justify D_rho(t) with its cap2. The same argument works for negative times through |t|.

Combining with the paid initial comparison proves (18). Substituting j|t| of order rho^-2 times a positive logarithmic factor yields the stated sufficient rho^(2/3) times logarithm^(1/6) behavior plus O(rho). This is only a specified free-profile norm bound. It is not an occupied-source estimate or a finite-device operating time.

## 5. Spatial tails and the incoming lead term

For L<=m the exact squared geometric tail sum is

    rho^2 sum_(n<=L) a^(2(m-n))=a^(2(m-L)).

This confirms (19), including L=m where the norm is one. At t>=0, m>=0; choosing L=-1 gives the left-tail term a^(m+1). The comparison has no support at n>m, giving the right-tail statement directly by projection contraction. Each physical free sequence has norm one, so the optional cap1 is valid.

Conjugating f_n(-t) gives exactly integral exp(-ink-itE(k))conjugate(F(k))/sqrt(2pi) on the physical upper half, which is the pinned incoming coefficient. For t>1/(4j), m(-t)=floor(-2jt+1/2)<=-1; G(-t) is then zero on every physical n>=0. This establishes (21). The strict time condition matters: at t=1/(4j), the selected m(-t) is0, so one cannot claim that vanishing at the endpoint. The source correctly excludes that case.

The incoming bound need not improve indefinitely because the dispersion allowance grows. The emitter residual remains a separate term. No outgoing-only free profile is mistaken for the complete normalized seeded state.

## Conclusion and verification limits

All changed load-bearing estimates are supported under the stated rho, source and Fourier conventions. The strongest legitimate new result is a normalized, phase-fixed geometric comparison with paid upper/lower-domain error, exact all-time free evolution of that comparison, and a separate time-dependent integer-translation envelope. Its free spatial tails and conjugate incoming consequence follow without extra physical assumptions.

The result does not establish complete finite launching, finite-router cut errors, source reabsorption control, record thresholds, runtime/resource exponents, preparation, capture/reset, native realization or permanent halt. The rational full-circle norm-two shortcut remains false and explicitly preserved as such. Only this review was written; no source, W, Git, checkpoint, editable prompt, model setting or publication surface was changed.
