# Nominal converted-lead endpoint and emitter: stationary and mass interface

Status: proposed analytical extension, not independently checked. Closing the new input and attaching the equal-diagonal emitter is stationary-feasible with all eight internal coordinates retained. The slower new lead worsens the spectral-mass scale. The potential benefit is a structured emitter/lead resonance relation, not an established improvement in nominal runtime or resources. No old escape time or finite-window theorem is transferred.

## Sources and exposure

I authored and reuse `../bandcenter_converter_composition/PROPOSAL.md`, SHA256 `1cc6fec524a8184f844711a4fa6d72fcc7cd13a4c8b413cbc064cd4b2201df78`. Read completely the selective independent check `../bandcenter_converter_composition_check/REVIEW.md`, SHA256 `f1653ba00c0f3d10d8846c1f010ad6dcddcd25535837dd87d17b9e655019a15c`. This extension is exposed to that review and to root's direction; it is not an independent discovery or another check of its own predecessor. After the reference integral below had been drafted, root supplied the same exact cotangent substitution and normalization formula; this is additional source exposure, not an independent check of the extension.

The predecessor records canonical mathematical source ancestry d17d5e32f3f44f162aff15ced734238ba1543212525d618d36dc95511095c4be, followed by read snapshots 9d493f2c67525f89fc32cc1201888a8729b64a2ce5522a7ad46dc9d473b2aae3 and 99a16de7d111bc0d3ab87ecb566db80b3a678c534cecc86ae7fe2d4dd9625639. The checker separately read the necessary original passages in snapshot 2ec466a624705dbd707c0c855df2d1dd93068df11e6f28b633eb8e4d3462a7cb. I do not claim to have read that entire later snapshot. Here the frozen proposal and check supply the exact original matching/kernel premises; the endpoint Dirichlet and spectral-jump arguments are reproduced below. No unrelated current W change is endorsed.

Previously read applicable instructions/workflow are reused at the identities recorded in the predecessor. No scientific execution, numerical experiment, parameter optimization, delegation, model override, or W/Git/checkpoint/prompt edit occurred. This file is the sole deliverable. All quantities below are nominal; no common-j error family or fixed-nominal-waveform robustness statement is assumed.

## 1. Fixed construction and new-port kernel

Use the checked TWO external converters, old buffers F=40, original source/filter/junction, and q in I=pi/2+[-sigma,sigma], sigma=1e-6. The new lead has .0027<j<.003, E(q)=2j(1-cos q), and

    v_new=E'(q)=2j sin q>.0053.

Write w=exp(iq), Qn=wP+Qn,c, ||Qn,c||<1/60. The old energy map k(q) and literal K/W are unchanged. Define the known common phase

    rho_n(q)=-exp(2iF k(q)) rho_g(k(q)).

The checked new open two-port matrix has diagonal reflection R and transmission t, uniformly in each of the four old/parity columns, with

    |R|<eta=21e-6,
    |t-rho_n omega_p|<delta=d0+723e-6,
    d0=1.76e-13.

These follow by adding the <9sigma converter matrix error to the separate original reflection and transmission bounds, not by using the looser combined column norm as a reflection bound.

The complete new-port retarded kernel at first-new-site origins m=n=0 is

    Gn_ab(m,n)=delta_ab An Qn^|m-n|+Qn^m Tn_ab Qn^n,
    An=[j(Qn-Qn^-1)]^-1,
    ||An||<200, ||An^-1||<21.

The open An entry is 1/(i v_new). Its closed entries have magnitude <1/[.0027(60-1/60)]<6.18. The inverse bound follows from the inherited B<20 and the displayed channel energies; no whole-space resolvent norm is used.

For completeness a useful full coefficient bound is ||Tn||<600 on both ports combined. Here is a derivation, including closed incidence used only as finite matching data. At one converter write old incident/outgoing amplitudes at its boundary as A,B and new incoming/outgoing coefficients as alpha,beta. For a closed mode with old root a and new root s,

    H=epsilon-J-j+Ja+(tau^2/j)s,
    A=R_o B+u alpha, beta=R_n alpha+v B,
    u=-tau(1-s^2)/H,
    v=(tau/j)s(1+R_o),
    R_n=-s^2+(tau/j)s u.

The checked |H|>5.99J, |R_o|<.2 give |u|<.04, |v|<.048 and |R_n|<.002. These formulas retain the sign of each real closed root. In the open channel, u=t_c chi, v=t_c/chi, chi=sqrt(v_new/v_old), so |u|<.49 and |v|<2.5; |R_n|<1.22e-6. These open bounds also follow directly from the physical amplitude formulas, without applying flux normalization to closed channels.

Let U,V,R_o,R_n denote these fixed-B diagonal channel matrices on both ports. With So=Told Aold^-1, the exact full generalized coefficient is

    Sn=R_n+V Qo^F So (I-R_o Qo^(2F) So)^-1 Qo^F U.

The checked ||So||<1+2(5.2e-12)+5.2e-32, return norm <1.22e-6 on open modes and <2e-65 on closed modes, give inverse norm <1.000002. Therefore ||Sn||<1.3 and ||Tn||=||Sn An||<260<600. This establishes a full internal bound rather than inferring closed rows from the open scattering error. The retarded kernel is complex symmetric in the fixed real basis, and Tn,PP=An,open S_new.

## 2. Close the new input after ell=20

Keep input-tail sites 0,...,ell with ell=20 and delete b=ell+1 and the outer tail. The comparison background keeps kinetic endpoint diagonal 2j. Put

    X=Qn^ell Tn_aa Qn^ell,
    X0=An,open R w^(2ell) P,
    Z=An+Qn X Qn.

The PP entries of X and X0 coincide exactly. The three remaining block terms give

    ||X-X0||<3*600*60^-20<1e-32.

Use 60^10>6e17 to verify the last deliberately loose bound. The original tiny PC/CP coefficient is not needed here; all seven closed coordinates gain the new-stub decay. Since ||X0||<200 eta=.0042 and ||An^-1||<21, ||Z^-1||<24.

Dirichlet deletion gives the FULL endpoint Green matrix

    G=An+X-(An+X)Qn Z^-1 Qn(An+X).

At X0 it is block diagonal, with

    g=-(w/j)(1+R w^(2ell))/(1+R w^(2ell+2)),
    G0,CC=-Qn,c/j.

The denominators have modulus at least 1-eta. On the tiny X-neighborhood, ||An+X||<201 and ||Z^-1||<24. Differencing the displayed expression costs at most

    1+2*201*24+201^2*24^2 <3e7

times ||X-X0||. Consequently

    ||G-G0||<epsilon_G=1e-24,
    ||G||<400, ||G_PC||,||G_CP||<epsilon_G.

This controls the full endpoint matrix, not only its vacuum diagonal.

For the outgoing output-open row set

    Y=P Tn_ba Qn^ell,
    L=Y[I-Qn Z^-1 Qn(An+X)].

Its scalar approximation is

    L0=-(t/j) w^(ell+1)/(1+R w^(2ell+2)) P.

Indeed ||Y-Y0||<600*60^-20<2e-33 and ||Y0||<200. The variation of the bracket costs [24+24^2*201]||X-X0||; its norm is <1+24*201. Thus

    ||L-L0||<epsilon_L=1e-23.

The constants have ample slack. No closed source amplitude is erased in this comparison.

## 3. Equal-diagonal emitter and its seven-coordinate complement

Attach an emitter with one positive two-qubit block

    j(n_e+n_end)-kappa(a_e^* a_end+a_end^* a_e),

and the positive onsite j n_e. For 0<kappa<=1e-8<j its one-excitation eigenvalues are j+/-kappa, vacuum value 0 and double-occupation value 2j. The retained ordinary new-j bond contributes j to the endpoint, hence the physical endpoint and emitter diagonals are both 2j. This directly realizes the background diagonal used above after coupling; there is no unaccounted kappa-dependent compensation. The seed is the emitter-occupied product state with the original source vacuum and arbitrary old/reference state.

At lambda=b+E(q), after removal of all common scalars, the emitter Schur matrix is

    De=(lambda-2j)I-B-kappa^2 G.

On Pc the bare distance is >.186-.006 sigma>.185 for the six excited channels and is nearly 2 for the other vacuum. The perturbation norm is <400kappa^2. Therefore the complementary block Dcc is invertible with ||Dcc^-1||<6, uniformly for the stated coupling interval. Its off-diagonal coupling to P has norm <kappa^2 epsilon_G. Define the exact resonant scalar

    Dj=E-2j-kappa^2 Gjj-kappa^4 GjC Dcc^-1 GCj,
    Dref=E-2j+(kappa^2/j)w.

The exact scalar endpoint difference gives

    |g+w/j|<2eta/[j(1-eta)].

Consequently, comparing directly with Im Dref=(kappa^2/j)sin q,

    |Dj-Dref| < epsilon_D Im Dref <=epsilon_D |Dref|,
    epsilon_D=5e-5,
    Im Dj>(1-epsilon_D) Im Dref>329kappa^2.

The main ratio is 2eta/[(1-eta)sin q]<.000043; epsilon_G and 6kappa^2 epsilon_G^2 fit far inside the chosen margin. In particular this proves a positive imaginary part; a relative modulus comparison alone would not suffice. Block inversion also yields ||De^-1||<1/(300kappa^2), including all complementary coordinates. The finite matching constructions exclude an in-band normal eigenvector. Out-of-band point spectrum is not excluded or discarded.

The exact outgoing seed amplitude is -kappa L De^-1 u_j, where u_j is the real vacuum vector. The minus sign comes from inversion of the positive off-diagonal kappa in lambda-H when the physical hopping is -kappa. Equivalently its numerator after emitter Schur reduction is

    -kappa [L_j+kappa^2 L_C Dcc^-1 GCj]/Dj.

The sign is plus because the complementary-to-vacuum block of De is -kappa^2 GCj. This term is retained even though its bound is negligible.

## 4. Common complex profile and precise mass limitation

Stone's formula with R+=(lambda+i0-H)^-1 gives the outgoing coefficient F_j=i E' Aout,j/sqrt(2pi). Define one common nominal reference profile

    Fref(q)= i kappa E'(q) w^(ell+1) rho_n(q)
                  /[sqrt(2pi) j Dref(q)].

It includes both converter and old-source propagation phases. The preceding estimates give uniformly

    |F_j/Fref-omega_p|<epsilon_F=.0008.

For example the leading ratio error is bounded by

    [delta+eta+epsilon_D+eta epsilon_D]/[(1-eta)(1-epsilon_D)]
        <.000795,

and the explicit epsilon_L, epsilon_G corrections are far smaller than the remaining margin. This is a complex profile bound, not just probability agreement. No old/parity-dependent carrier or phase is fitted.

The scalar half-line reference with endpoint/emitter diagonal 2j and coupling kappa has the exact density

    |Fref(q)|^2=2kappa^2 sin^2(q)/(pi |Dref(q)|^2).

Writing A0=2j-kappa^2/j>0, B0=kappa^2/j and u=cot q, its integral outside I is exactly

    1-p0=(4kappa^2/pi) integral_(tan sigma)^infinity
              du/[(A0^2 u^2+B0^2)(1+u^2)],

and is bounded above by 4kappa^2/[pi A0^2 tan sigma]. The full density integral on (0,pi) is exactly 2kappa^2/[B0(A0+B0)]=1. This can be obtained by elementary partial fractions; it establishes the scalar reference's normalization without assuming a Lorentzian or extrapolating an approximate line shape. Multiplication by rho_n changes only its phase. For kappa<=1e-8 the loose numerical consequence is 1-p0<4.4e-6 (and at kappa=1e-12, <4.4e-14).

The reference missing-mass scale is therefore kappa^2/(j^2 sigma), worse at smaller j. A reference bound is NOT an actual-seed mass bound. The latter needs a separate argument.

One argument available immediately, although crude, is exact spectral variance. In a selected column the actual seed has mean b+2j+c_total and variance kappa^2, since only the endpoint hopping acts off that product vector. The physical interval is centered EXACTLY at this mean, with half-width

    d=2j sin sigma>.0053 sigma.

Thus the norm of ALL actual out-of-band spectral mass, including point spectrum, is at most min(1,kappa/d). No interval recentering or residual deletion is made. The in-band rank-one jump, supplied by the finite matching inverse and the single asymptotic output-open channel, identifies the actual in-band measure with |F_j|^2 dq. This identity also gives the separate weaker bound

    1-p_actual <=1-(1-epsilon_F)^2 p0.

At kappa=1e-8 the variance amplitude bound is uninformative, and the profile-based mass bound only gives amplitude about .041, not a small-error preparation theorem. It must not be replaced by the reference amplitude about .0021. Deriving a useful actual mass estimate at that coupling requires a new quantitative local spectral-measure/self-energy regularity argument on the SAME band, with all complementary coordinates and point mass accounted for. Its inputs have not been supplied by the stationary norm bounds alone.

As a feasibility illustration, not an optimization or runtime claim, take the already familiar small value kappa=1e-12. Then actual out-of-band amplitude <.000189. With f=Fref/sqrt(p0), positive normalization, replacing the seed by the normalized exact scattering packet having outgoing coefficient omega_p f costs at most

    kappa/d + epsilon_F sqrt(p0) + (1-sqrt(p0)) <.000989

per column. This follows by spectral orthogonal decomposition plus the in-band complex profile bound. The actual scattering incoming coefficient includes its actual reflection phase; it is not silently replaced by a different incoming packet. At this coupling 1-sqrt(p0)<4.4e-14. For arbitrary old/reference inputs, possible overlap between the two old-energy error vectors in one parity costs sqrt(2)<1.415, giving <.0014; the two parities are orthogonal. This is solely an initial complete spectral-comparison interface, with no assertion that the packet has already escaped at any stated time.

## 5. Preserved physical output and remaining obligations

The two converters contribute scalar 4gamma in addition to the old physical scalars. The emitter block above contributes no vacancy scalar. The final comparator must retain exp[-it(c_old+4gamma)] exp(-itK)W and the common q-dependent profile phase rho_n(q), with its actual E(q). Closing a tail removes no source qubits or old coordinates. Both converter neighborhoods, both old buffers, the shared source, all emitter coordinates and every closed tail remain recoverable through the full kernel and Schur formulas; their norm or derivative is not set to zero.

This proposal does not prove temporal escape, a new localized-column derivative estimate, contour regularity, finite M comparison, a complete geometry/resource count, or permanent halting. The new group velocity is smaller, so existing time/window values cannot be reused. A useful larger-kappa actual-mass bound is an explicit open interface, not a failed universal possibility. No coupling optimization was performed.

The structural point survives: in the stipulated supplier block, emitter and new lead share diagonal 2j independently of kappa, while the old source remains at the energy where it was calibrated. However the nominal relation 2j=E0, converter parameters, and exact equal-diagonal supply are still specified physical data. Common-j drift, independent diagonal errors, converter mismatch and comparison to a FIXED nominal waveform require a separate robustness contract. The current result establishes stationary feasibility and a conservative small-coupling spectral interface; it does not establish better nominal resources or precision-free fabrication.
