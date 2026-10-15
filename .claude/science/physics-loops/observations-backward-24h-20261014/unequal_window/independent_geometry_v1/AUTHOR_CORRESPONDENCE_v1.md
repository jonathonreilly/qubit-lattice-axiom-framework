# Focused post-exposure unequal-window correspondence

The normalized necessary constraint and the explicit angular-null annihilator agree with my previously frozen independent geometry. The added quotient resolves the preserved monopole counterexample on the author's narrower chart. The Gaussian random-wave construction supplies the claimed nonzero kinematic sensitivity witness. No substantive mathematical discrepancy was found in this assigned scope. This is a separately labeled post-exposure correspondence, not another blind derivation, a formal audit or an empirical validation. Root remains author.

The independent report and its 27 controls remain unchanged. I froze copies of, then read the complete WORKING_v3.md, geometry_check_v1.py and geometry_check_v3.py. I read the complete saved v1 geometry result. The v3 result was copied after my separate controls finished; its 43 saved true flags and exact source identity were checked, without executing author code. The working note's weak/pullback/sampling sections were read for context only; their proof and implementation remain the separately assigned reviewer's responsibility.

## Normalized projection and necessity

In my original notation b1=(A-B mu)/r, b2=(B-A mu)/r, p=b1 b2 and ell=-(mu+p)/r. The author's p1=-b1, p2=b2, so p1 p2=-p. Its normalized quantities are therefore

    P=partial_r+gamma,  gamma=ell/p,
    G=(d1 d2 C_uu)/p,
    J=d2 C_Su/b2,
    U=partial_A gamma=(p ell_A-p_A ell)/p^2.

The author's restriction p1 p2!=0 is stronger than the b2!=0 chart of my unnormalized derivation. It is explicit and sufficient for these normalizations. It excludes both radial cross-projection zeros; no implicit division by a zero principal coefficient remains. The fixed-r, fixed-N2 time slot and gamma's A derivative are consistent. Differentiating G includes the time-dependent velocity normalization and geometry.

With R=C_VV,r, T=y partial_1+c0, D=partial_1-a0, and b=y A_1, the two supplied relations are PR=G and TR=DJ. Hence

    F=T G-P D J=[T,P]R=b U R.

Since b depends only on times and L=U P-U_r,

    L(b U R)=b U^2 P R=b U^2 G.

Thus H=L(TG-PDJ)-bU^2G=0 is necessary without dividing by b or U. In the regular bU!=0 chart it is the spatial compatibility condition for R*=F/(bU). My second temporal compatibility condition is deliberately not claimed here; this single necessary implication need not supply it. In particular I do not treat missing reconstruction sufficiency, parameter rank or a positive/full-history converse as a defect in this stated target.

The interior zero of U is exactly the geometric determinant zero found independently. Keeping H without division avoids excluding it from necessity, although information can degenerate. The normalized chart still excludes p1p2=0. Low-mode cancellation does not restore these excluded points, establish uniform sensitivity, or remove conditioning near them.

## Independent rational-degree certificate

The missing shear ell=0,1 change C_Su by arbitrary time functions times 1 and mu. After normalization by alpha2 p2 this is span{r,r/(r^2-delta)}, delta=A^2-B^2. A fixed-r leg-one derivative adds r/(r^2-delta)^2, including derivatives of arbitrary time coefficients; D introduces no further radial basis. No coefficient of those missing modes is specified or fitted. Since G is unchanged by missing S modes, their effect on H is in minus LP of this three-dimensional radial span.

I recomputed the rational reduction in the different variable t=r^2. Define

    h(t)=[t^2-2(A^2+B^2)t+delta^2]/[t^2-delta^2],
    h_A=partial_A h,      gamma=h/r,      U=h_A/r.

For an odd input r f(t), its P image is

    g(t)=(1+h)f+2t f_t.

The next operator has the independent t representation

    L g=2 h_A g_t+[(h+1)h_A/t-2(h_A)_t]g.

Taking f_j=(t-delta)^(-j), j=0,1,2, also gives the simple formula

    g_j=2t[(1-j)t-(A^2+B^2)-j delta]
         /[(t-delta)^(j+1)(t+delta)].

Direct rational reduction in this representation gives the following exact certificate. The numerator degrees are in t and each numerator contains t^2; complete coefficient lists are retained in POSTEXPOSURE_RESULTS_v1.json.

| j | Denominator of LP[r/(r^2-delta)^j] | Numerator degree | Degree after W |
|---|---|---:|---:|
| 0 | (t-delta)^4(t+delta)^4 | 6 | 6 |
| 1 | (t-delta)^5(t+delta)^4 | 4 | 3 |
| 2 | (t-delta)^6(t+delta)^4 | 5 | 3 |

Thus W=(t-delta)^6(t+delta)^4/t^2 cancels every denominator and t^2 factor. Every WLP nuisance is a polynomial of degree at most six in t. This exactly agrees with the author's raw r-degree bounds 12,8,10 and weighted r degrees 12,6,6. All three independently computed polynomials equal the saved author polynomials coefficient-for-coefficient.

Since K=r partial_r=2t partial_t, the product over j=0,...,6 of (K-2j) annihilates every such polynomial. Multiplication by W must occur first, as specified. At fixed time all nuisance coefficients are constants under these radial operators. The cancellation therefore holds for arbitrary time-dependent missing-mode coefficients; it does not assume or calibrate them. This establishes the stated quotient invariance of ZH on the chart. It removes genuine signal as well as nuisance and does not cover arbitrary angular masks.

My preserved unit-monopole fixture still gives a nonzero unquotiented result. In the author's normalization, with A'=−1 and a0=0, its nuisance derivative is -4AB r/q_-^2. Therefore the change in raw H is 4AB LP(r/q_-^2). At A=2,B=3,r=2 it equals 606208/19683, yet the stated Z annihilates it exactly. This explicitly resolves, rather than discards, the earlier counterexample: the original raw test was not invariant, while the added operator is. The old nonzero residuals remain valid evidence for the earlier raw relation.

## Gaussian covariance sensitivity

The random field g(x)=sqrt(2) cos(k dot x+theta), with theta uniform independently of k~N(0,2 lambda I), is bounded, mean zero, homogeneous and isotropic. Averaging over theta gives cos(k dot(x1-x2)); the Gaussian characteristic function then gives C(r)=exp(-lambda r^2). This supplies a genuine positive covariance, not merely an arbitrary radial argument. Gaussian wave-vector moments also justify the finite derivative moments used here. It is an existence witness, not selection of the actual cosmic covariance.

For V=f(N)g and S=s(N)g, the supplied local law holds exactly when

    s'-a0 s=y f'+c0 f.

No gravitational background equations follow from this scalar ordinary differential condition. A concrete unit-amplitude choice is f=1, a0=0, c0=1, s=N, with y supplied. Altering only the tested c0 by delta_c changes H by delta_c LP R, and changes ZH by delta_c f(N1)f(N2) ZLP C_r. The coefficient below concerns ZLP C_r; general amplitudes and delta_c multiply it.

I independently conjugated the t-coordinate operators by exp(-lambda t). Start with C_r=r(-2lambda)exp(-lambda t). Its first P image, after removal of the exponential, is g=(1+h-2lambda t)(-2lambda). Then

    exp(lambda t) L P C_r
      =2h_A(g_t-lambda g)+[(h+1)h_A/t-2(h_A)_t]g.

After multiplication by W this is a polynomial of degree eight in t, with leading coefficient 32 A lambda^3. Each conjugated Euler factor is 2t partial_t-2lambda t-2j and raises the leading degree by one with multiplier -2lambda. After seven factors the degree is fifteen in t (thirty in r) and the leading coefficient is exactly

    -4096 A lambda^10.

Restoring the exponential gives the claimed -4096 A lambda^10 r^30 exp(-lambda r^2) leading term. Since A,lambda>0, the polynomial is not identically zero; analytic nonvanishing therefore holds at some points of every nonempty open regular radial chart. An explicit interior check at A=2,B=3,r=5/2,lambda=1/2 gives the nonzero polynomial value 10740842923919677734375/134217728 before restoring exp(-25/8). The author's v3 conjugated r-operator implements the same formula and normalization. The old r^19 fixture remains only a smooth-function nonvacuity example; the Gaussian extension is the separate positive-covariance witness.

This proves some kinematic sensitivity survives the angular quotient. It does not demonstrate full-gravity solution membership, parameter uniqueness, observed signal significance or a stable finite-data inverse. Those limits are stated in the source and remain necessary.

## Exact scope and identities

The original independent 27 controls are unchanged. The separate post-exposure program has 33 passing exact/correspondence controls and no failure. It does not invoke the author's program. It uses the independent unnormalized dictionary and a t-coordinate operator construction, checks the exact nuisance degrees/polynomials and the preserved monopole, derives the Gaussian leading coefficient, and binds the saved v1 results. Saved author totals are 38 for v1 and 43 for v3; those are not new independent runs.

Source snapshots read in full:

- WORKING_v3.md: 90695ccbf7eacf97ee80b0594c17d1be30ded864d30b0729aff5aaf798282ce8.
- geometry_check_v1.py: eb82aa52be8a755af78e7427deec8b3859349200ab5e318fc9bfe69eee0d6fc2.
- GEOMETRY_RESULT_v1.json: 734da887f5d6c56b6ef3a8d99324c6b86e53c388ff0ea2ca2238d61779d23724.
- geometry_check_v3.py: 0d2d7fd18e386fa41e93ccdc4d8b6d3c7e3ee8d0e8c2b89a0bab0eaf307ac73c.

Saved v3 result 0bb9f1f979ce02f870b0330645a5fea2affbba01d7ef118481a05b6492bc64ec binds that same v3 source; only its source identity, saved flags and relevant witness fields were used. The complete exposure manifest and independent source/result hashes accompany this report.

No new physical assumptions were silently retired. The field law, calibrated geometry, smooth homogeneous/isotropic scalar-flow covariance, shear interpretation, observational signal/noise and survey conditions remain conditional. This report does not independently certify the weak adjoint, lensing pullback, finite-catalogue expectation construction, numerical stability or any empirical claim. No canonical files, branch, index, campaign state or ownership were changed.
