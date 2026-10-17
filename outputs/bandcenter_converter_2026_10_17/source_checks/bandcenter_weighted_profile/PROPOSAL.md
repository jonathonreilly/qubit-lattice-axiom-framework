# Pointwise converted profile and reference-weighted actual mass

Status: new analytical proposal, not independently checked. The existing derivative/central-value premises yield a pointwise complex profile ceiling, with all central and closed-feedback floors retained. Weighting its first moment by the exact reference measure removes the uniform .0008 profile-induced mass ceiling. Conditional on the checked in-band spectral identification, at kappa=1e-8 the actual total out-of-band mass is<4.43e-6, hence amplitude<.002105. No temporal escape, runtime, finite-window or common-j extension is asserted.

## Sources and exposure

Re-read the full relevant original source/filter/junction passages, lines163–319, of correlation_worktree/docs/REAL_ENDPOINT_AUTONOMOUS_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md at SHA256 71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff. This is a new current note identity; the mathematical passages below agree with the previously checked ancestry. The needed premises are the positive central calibration d0=1.76e-13, |r_bare'|<=700, unit-modulus r0=-exp(2ik), filter central reflection0 and transmission iz0, endpoint-reflection derivative<5, uniform closed-filter correction<1e-20, and fixed real source projections. No other changed note content is imported.

Reuse nominal converter proposal1cc6fec524a8184f844711a4fa6d72fcc7cd13a4c8b413cbc064cd4b2201df78 and its independent check f1653ba00c0f3d10d8846c1f010ad6dcddcd25535837dd87d17b9e655019a15c, including full seven-channel feedback<1e-86, exact mapped band and source recovery. Reuse endpoint proposal22e7b4a9363a0c010ebce59f3235891708fd40eb5a5fa18f91b1a8878fe99c5a and check200268709480f1533050f5d197a4bed7a2acaefa5f4a22a662938ddb504619c6, including full eight-coordinate Schur bounds, epsilon_G=1e-24, epsilon_L=1e-23, spectral-jump identification and absence of singular in-band mass under complete finite-core premises. Exact scalar reference density/normalization/tail is independently checked in1953d153c9ac8583202e7ca18bff62829bfbff2373691cc43a5ae152a2a6b0ae.

I have source/result exposure through my previous checks and root's hypothesis that first-moment weighting might help. This is a distinct proposed derivation, not an independent review of itself. No unfinished Herglotz-Poisson argument was read. No numerical/scientific execution, sweep, solver, delegation, Git/W/checkpoint/prompt/model change occurred. Only source text/hash reading and this deliverable were performed. Applicable unchanged workflow reused; all source/calibration/physical premises remain conditional.

## 1. Pointwise old source and filter estimates, derived rather than substituted

Write s=|k-k0|<=sigma=1e-6. From the exact central calibration and |r_bare'|<=700, while |r0'|=2 and zeta,omega have fixed unit modulus, the fundamental theorem of calculus gives

    |r_bare(k)-r0(k)zeta omega_p|<=d0+702s.           (1)

The filter parity endpoint reflections have derivative<5 on the full original band. Their half-sum a has a(k0)=0, so |a(k)|<=5s. Their half-difference b satisfies b(k0)=iz0 and |b'|<5. Since |b|<=1 on the real axis, |(b/z)'|<=6; hence |b/z-i|<=6s. These are derivative integrals on the already certified fixed interval, not substitution of s into a uniform error statement.

The exact scalar concatenation formula gives

    |r_scalar+r_bare|
      <=5s+17s/(1-5s)<=23s.

Indeed |(b/z)^2+1|<=12s by |b/z|<=1, while the round-trip denominator is>=1-5s. The final zero-floor scalar inequality is strict only for s>0; equality holds at s=0. The physical closed-filter correction is bounded uniformly by epsilon_cf=1e-20. There is NO reason to set it to zero at k0, and no closed-correction derivative is assumed. Thus

    |r_modified+r_bare|<23s+epsilon_cf.              (2)

After the exact real arm mixer and common port phase, R_old=(r_bare+r_modified)/2 and the transmission is r_bare minus half their sum, up to that known unit phase. Therefore

    |R_old|<5e-21+12s,
    |t_old-rho_g omega_p|<d0+5e-21+714s.             (3)

The second slope is conservatively rounded from702+23/2=713.5. The d0 floor is charged only where it actually enters; (2) cancels the same bare reflector in the reflection channel without assuming its calibration exact.

## 2. Pointwise nominal converter bounds

Put x=|q-pi/2|<=sigma. The exact nominal map gives |k-k0|<=.24x, using k'<.24 throughout the checked mapped band. The converter numerator vanishes exactly at its center and its derivative is<.029, while its denominator there is>.024. Thus

    |r_o|=|r_n|<=.029x/(.024-.029x)<=1.22x.

Using |sin k-S0|<=.24x, sin k>.4 and1-sin q<=x²/2, the checked transmission calculation localizes to |t_c-i|<=3x and |t_c²+1|<=6x. These follow from actual central equalities and uniform derivatives/elementary trig bounds, not from replacing sigma in a conclusion. The zero-floor bounds above may be strict for x>0, but at x=0 their two sides vanish. Closed full-fiber feedback remains only uniformly bounded: delta_c=1e-86, not zero at x=0.

The open multiple-return comparison therefore gives

    ||S_new+z^(2F)S_old||
      <=rho(x)+6x+rho(x)/(1-rho(x))+delta_c
      <9x+delta_c.                                 (4)

Combining (3),(4), including all seven closed channels through delta_c, yields convenient ordered pointwise bounds

    r(x)=1e-20+12x,
    t(x)=d0+1e-20+181x,
    |R_new(q)|<r(x),
    |t_new(q)-rho_n(q)omega_p|<t(x).                (5)

The slopes before final rounding are12*.24+9=11.88 and714*.24+9=180.36. Both constants absorb5e-21+delta_c without suppressing either. The common rho_n(q) includes the actual mapped k(q), old/filter/junction phase and equal old-buffer propagation; it is not refitted per column.

## 3. Full endpoint/emitter profile bound

Retain the checked endpoint's uniform full-coordinate epsilon_G=1e-24 and outgoing-row epsilon_L=1e-23; improving (5) does not change those proofs or bases. All seven emitter complements retain ||Dcc^-1||<6, and their Schur numerator term is kept. For0<kappa<=1e-8, the exact g formula gives the sharper relative denominator error

    |Dj-Dref|/Im Dref
      <=2r(x)/[(1-r(x))sin q]
           +j[epsilon_G+6kappa²epsilon_G²]/sin q
      <d(x):=2.0001r(x)+4e-27.                     (6)

Here r(x)<1.21e-5, sin q>=cos sigma, j<.003. In particular the coefficient2.0001 is valid uniformly; this is still a positive imaginary denominator comparison. It preserves all original full Schur invertibility and spectral regularity margins.

The exact profile ratio, including -kappa[L_j+kappa²L_C Dcc^-1 GCj]/Dj and the fixed common reference phase, obeys

    |F_j/Fref-omega_p|
      <=[t(x)+r(x)+d(x)+r(x)d(x)]/
             [(1-r(x))(1-d(x))]+tiny_row_term.      (7)

Since L0 has no complementary columns, ||L_C||<=epsilon_L. The extra numerator after division by the reference numerator has size at most j epsilon_L plus the negligible6j kappa²epsilon_L epsilon_G. The denominator conversion is near one. Together with the4e-27 in(6), a1e-25 numerator allowance suffices.

To make slack explicit, the denominator in(7) exceeds .99996, and its numerator including this allowance is at most

    t(x)+3.0002 r(x)+1e-25.

Its slope is at most217.0024 before dividing by .99996, hence below220 afterwards. Its constant after division is below1.8e-13, while retaining d0=1.76e-13. Therefore a uniform full complex profile bound is

    |F_j/Fref-omega_p|<a+b x,
    a=1.8e-13, b=220.                              (P)

This bounds phase and magnitude together, keeps all emitter/source complement coordinates, and has a strictly positive central floor. It does not assert exact center calibration or differentiate an uncontrolled closed correction.

## 4. Exact reference moments on the hard band

Let A0=2j-kappa²/j>0 and B0=kappa²/j. At q=pi/2+u the exact reference density reduces to

    dmu0/du=2kappa²/[pi(A0² tan²u+B0²)].

Its phase rho_n and w^(ell+1) has unit modulus and does not change this density. Let p0=mu0(|u|<=sigma), and M1,M2 be the unnormalized first absolute and second moments on that band. For u>=0, tan u>=u. Direct positive integrals give

    M1 <= [2kappa²/(pi A0²)]
                  log(1+(A0 sigma/B0)²),            (8)
    M2 <= 4kappa² sigma/(pi A0²).                   (9)

Both moments are with the ORIGINAL finite-band reference measure; no infinite Lorentzian extension or unnoticed normalization is used. Formula(8) exhibits the proposed kappa²/j² logarithmic scale. It is an upper bound, not an asserted exact asymptotic uniform in shrinking sigma. The central-floor contribution remains a p0 and cannot be removed by the small linewidth.

## 5. Actual full missing mass from a weighted lower density

The checked actual spectral jump identifies its in-band seed measure as |F_j|²dq with no singular component on the band, under the full finite-inverse premises. Since e(x)=a+b x<1, (P) gives

    p_actual>= integral_I (1-e(x))² dmu0
             >=p0-2a p0-2b M1.

The actual seed has total spectral mass one. Hence ALL actual outside-band mass, including point spectrum, obeys

    1-p_actual <= (1-p0)+2a+2b M1.                 (10)

This is the new bridge. It pays the exact reference tail separately and uses actual spectral identification to infer actual missing mass. It neither asserts global absolute continuity of the converted device nor substitutes reference mass for actual mass. Uniform profile error would instead charge about2*.0008; weighting avoids that unnecessary ceiling.

At the fixed value kappa=1e-8, use A0>.0053, A0<=2j, j<.003 and pi>3. Then A0 sigma/B0=A0 j sigma/kappa²<180000. The logarithm in(8) is<25: e>8/3, (8/3)^5>130 and130^5>32400000001 establish e^25>1+180000² without numerical logarithm evaluation. Thus

    M1< [2*10^-16/(3*.0053²)]*25 <6e-11.

The independently checked reference ceiling1-p0<4.4e-6 gives

    1-p_actual<4.4e-6+3.6e-13+440*(6e-11)
                <4.43e-6,
    ||outside-band seed||<.002105.                (11)

The latter follows because .002105²>4.43e-6. The previous uniform-profile mass amplitude about.041 is therefore not forced by these premises. This is still a nonzero mass error, dominated here by the reference hard cutoff. These numbers are for the fixed kappa=1e-8; one must use(8),(10), not hold the logarithm25 fixed, when changing kappa.

## 6. Optional initial packet comparison from the same data

No runtime inference is needed to compare initial spectral states. In the actual scattering representation, the in-band coefficient difference has norm at most

    ||(F_j-omega_p Fref)1_I||
        <=a sqrt(p0)+b sqrt(M2).

For kappa=1e-8, (9), pi>3 and A0>.0053 give M2<4.75e-18 and the preceding norm<4.8e-7. With f=Fref/sqrt(p0), the positive normalization cost is1-sqrt(p0)<=1-p0<4.4e-6. Combining with(11) gives the safe per-column initial comparison

    ||seed_j-normalized_actual_scattering_packet_j||
       <.002105+4.8e-7+4.4e-6<.002110.             (12)

The packet uses actual incoming reflection phase, full physical source/closed coordinates and common profile; it is not an output-only projected state. For arbitrary old/reference input, pay sqrt(2)<1.415 for possible overlap of the two old-energy ERROR columns in one parity, giving<.002986. Parities remain orthogonal. This comparison is not a claim that the packet is on physical output at any particular time. It does not meet a smaller tolerance merely because it improves the previous .041 bound, and it does not supersede the distinct small-coupling result without a chosen comparison objective.

## Scope and next check

The derivation uses only real-axis pointwise source/filter calculus, checked finite-fiber stationary composition/endpoint bounds and the exact reference measure. It does not require or supply new complex-disk regularity. Its decisive new steps are the explicit center-plus-derivative reconstruction(1)–(5), the ordered full profile estimate(P), and the actual lower-density integral(10). They require a separate independent check before use in a milestone. The unchanged source and full in-band finite-inverse premises remain conditional.

No common-j drift family, fixed-nominal waveform tolerance, endpoint derivative/contour estimate, temporal escape, finite output truncation, resource optimization, native supply or improved runtime is established. The scalar physical phase c_old+4gamma, old aging, both exterior ports before termination, and every internal/closed output remain as in the checked nominal architecture. A distinct unfinished Herglotz-Poisson route has neither been read nor used as support.
