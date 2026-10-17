# A physical pulse bridge for the mass-tuned mediated source

Status: bounded author proposal with partial analytical lemmas, not a completed pulse or output theorem. At assignment the loaded-inverse argument was provisional. Its subsequent distinct review `f6303bb3`, read in full here, conditionally supports `5f909e1e` at stationary scope without a required correction. That review does not certify the new arguments below. The mass-tuned coefficients and product witness retain their separate checked scopes.

The proposed next theorem should compare the actual apparatus to the EXACT scalar mediated chain, using its physical bare seed and its exact outgoing phase. It should not identify the actual packet with the ordinary critical three-site packet from a small center discrepancy. The latter remains useful as a weighted local resolvent comparator, with the physical mass factors retained.

Three concrete advances below are available for distinct checking: an exactly normalized scalar comparison measure; an energy-resolved boundary-integral estimate which removes the spurious calibration-floor logarithm; and a joint recovery estimate for every mediator coordinate. Wrong-window outgoing rows, actual Stone identification and a quantitative escape/arrival time remain load-bearing work.

## 1. Exact candidate theorem and reference

Retain every hypothesis and finite inverse gate of the checked loaded interface: corrected cap replacement, shared B/c_att, the fixed mass-tuned gamma_l, n1=n2=2m-1,n3=m, fixed port gauge, actual full G/G0 on both physical windows, rho<=min(d_bg,a/2), eta<1, k_C>0 and zeta<1. All notation below has the meaning in that source; in particular a=J_m-q, lambda=lambda_m and Z_i are the fixed limiting source masses. Passive reference systems are allowed by operator norm throughout.

Define a genuine scalar Hamiltonian h_m by retaining the SAME three source sites and all three mediator paths, with their physical negative real hoppings. At p replace the processor background by a uniform negative-j half-line. Subtract only the common 2j carrier, leaving zero head diagonal everywhere. This is a mathematical comparison operator; no prepared incoming packet is supplied. Its input is the physical endpoint vector |s0>.

The target theorem is a represented-outgoing comparison

    actual outgoing component from the product input
      ≈ one normalized scalar packet from h_m
           tensor [literal iota exp(-itK) W and record1],

with the original c_att/carrier, fixed source-to-port phase and physical slow-coordinate reference plane. The error must be stated as an operator norm on the complete prepared old input, with a separately paid wrong-window contribution. Identification of the entire actual state additionally requires incoming, local/source/mediator/background, closed-tail, one actual outside-window, physical-halfline normalization and finite-cut terms. No old time bound is a premise of this theorem.

## 2. Physical scalar normalization without removing the mass factors

The supplied occupation inequalities imply that every absolute hopping row sum of h_m is <=2j: interior rows use J_m+q, mediator-end rows J_m+gamma_l, source rows gamma1, gamma1+gamma2 or gamma2+gamma3, and the port row j+gamma3. Hence ||h_m||<=2j by the Schur test. All bonds are nonzero and only finitely many differ from the uniform tail.

An l2 eigenvector at any energy in [-2j,2j] would have an oscillatory, or threshold affine, uniform-tail solution. It must therefore vanish on that tail; the nonzero bonds propagate the zero backward to the seed. Exterior eigenvalues are excluded by the norm bound. The seed Weyl function is a finite continued fraction in m_j(z). On the band interior the tail has strictly negative imaginary part; each recursion 1/(delta-bond^2 m) retains that sign and a nonzero denominator. Its interior boundary values are therefore analytic on local physical root branches. Any remaining singular measure is supported at the two thresholds, which have no atoms by the tail recurrence and cannot support singular continuous measure. Thus the physical scalar seed measure is purely absolutely continuous and has total mass ONE. This is a new argument for this mediated chain, not reuse of the ordinary three-site density.

Let S_sc(delta) be the exact PHYSICAL three-source Schur matrix obtained from the mediator functions and G0=m_j(delta), including the port diagonal s3(delta). Put

    r20,sc=(S_sc^(-1))_20,
    B_sc(delta)=t3(delta) r20,sc(delta)
                         /[1-s3(delta)m_j(delta+i0)].      (1)

On |delta|<=rho, all mediator eliminations are nonsingular. The exact scalar seed density is

    rho_sc(delta)=-Im(S_sc^(-1))_00/pi
                 =sin(q)/(pi j) |B_sc(delta)|^2,
    delta=-2j cos q.                                      (2)

Indeed the only imaginary source load is t3^2 m_j/(1-s3 m_j), and -Im[m_j/(1-s3 m_j)]=(-Im m_j)/|1-s3 m_j|^2. The inverse imaginary-part identity then gives (2). At internal mediator poles outside this region, use the original scalar Jacobi operator or its continued fraction; a pole of a Schur representation is not automatically a physical pole.

In the limiting mass coordinates, (1) contains exactly

    B_sc=(-1)^(m-1) c(delta)b1(delta)b2(delta)
       /[sqrt(Z0) q_sc(delta)(1-s3(delta)m_j(delta+i0))],    (3)

where b1,b2 are the positive mass-congruent source hoppings, c=|t3|/sqrt(Z2), and q_sc is their exact scalar three-source determinant. Thus the physical 1/sqrt(Z0) and the fixed sign remain. Neither can be removed by declaring a normalized effective source. The full scalar second moment is gamma1^2, its actual first-hop squared, rather than lambda^2/3. Energy-dependent masses and the other spectral weight are present in this normalized physical model.

Reuse only the unchanged background phase/flux interface of the checked outgoing source. Write

    ell_x(delta)=-x omega rho_att w^21/j,
    w=exp(iq), rho_att=-i w^40 zeta_phase exp[i172 k_old(q)],
    A_sc=-rho_att w^21 B_sc/j,
    F_sc(q)=i E'_q A_sc/sqrt(2pi), E'_q=2j sin q.

These definitions are needed only on the retained central interval, where the old calibration phases are physical real phases. Equation (2) gives exactly |F_sc(q)|^2 dq=rho_sc(delta)d delta. With the unchanged physical converter,

    F_s(k)=t_f sqrt(dq/dk) F_sc(q(k)),
    p_m=integral_Irho |t_f|^2 rho_sc(delta)d delta,
    F_hat=F_s/sqrt(p_m).                                  (4)

Positive nonzero Jacobi bonds give nonzero scalar density on an open central set, so p_m>0; flux contraction gives p_m<=1. Normalize the comparator once, paying 1-sqrt(p_m). This does not renormalize any actual output or postselected branch. Unit full Fourier norm is not unit norm on the physical half-line at a chosen time.

There is an explicit conservative normalization allowance. Apply the checked local witness to the scalar chain, where there is only ONE input energy. With c1=u(1-r^(4m-2)),

    delta_p=sqrt(2[1-1/sqrt(1+c1)]),
    B_sc,out=delta_p+sqrt(Z0 Z1/3)lambda
                                      /[rho sqrt(1+c1)],
    1-p_m <= Xi_m := B_sc,out^2+(rho/g)^2.                 (5)

The first term is the scalar outside-window probability bound; the second uses the actual converter bound |r_L|<=|delta|/g. When Xi_m<1, the normalization cost is at most Xi_m/[1+sqrt(1-Xi_m)]. Otherwise retain exact p_m. The actual installed product input still needs its DIFFERENT two-energy witness bound, with sqrt(2) on the residual term. The fixed preparation allowance does not vanish with m, and is only an upper certificate.

## 3. Verified energy-resolved local-column bound: no a0 logarithm

This section verifies root's proposed refinement algebraically. It is new author work needing a distinct check. Put R=sqrt(delta^2+lambda^2), s=sqrt(1-3lambda/j), F=S_crit+DeltaF as in the loaded source, and retain its uniform zeta<1. Resolvent subtraction gives, on either lip,

    ||F^(-1)-S_crit^(-1)||
       <=36 ||DeltaF(delta)||/[s^2(1-zeta)R^2].            (6)

The order is -F^(-1)DeltaF S_crit^(-1); no actual factors commute. Replacing ||DeltaF|| by chi R too early produces chi log(rho/lambda), which need not vanish because chi retains a0. That is an avoidable loss for (6), not an obstruction.

Here is an explicit integrated envelope. Define

    A_err=1/[(1-eta0)(1-eta)], B_err=A_err^2 tau^2/k_C,
    nu=gamma3^2/[a(a-rho)], e(delta)=a0+b0|delta|,
    D3=Gamma2/[a^3(a-rho)], Gamma2=sum_l gamma_l^2,
    theta12=(1-rho^2/a^2)^(-(2m-1))-1,
    theta3=(1-rho^2/a^2)^(-m)-1,
    H12=(2m-1)/a^2 * (1-rho^2/a^2)^(-2m),
    H3=m/a^2 * (1-rho^2/a^2)^(-m-1),
    H_hop=sqrt(3)H12+3(2+theta3)H3,
    Jfac=3j(1+theta3)^2,

    C0=A_err a0+B_err a0^2,
    C1=nu/[j^2(1-nu rho/j)]+A_err b0+2B_err a0 b0,
    C2=B_err b0^2.

The exact port/complement proof, with its error evaluated at the actual delta, gives

    ||G_eff-m_j(delta)|| <= C0+C1|delta|+C2 delta^2.

For the hopping functions, the mean-value bound

    (1-delta^2/a^2)^(-n)-1
       <=n delta^2/a^2 * (1-rho^2/a^2)^(-n-1)

retains their quadratic zero. The finite masses and diagonal Taylor term likewise retain their actual |delta| and |delta|^3 factors. Consequently

    ||DeltaF(delta)|| <=delta_m |delta|+D3|delta|^3
                +lambda H_hop delta^2
                +lambda Jfac(C0+C1|delta|+C2 delta^2).     (7)

All quantities in (7) use the physical ordered loaded kernel. The closed feedback term is included in B_err e(delta)^2.

Let L=log(1+rho^2/lambda^2), Atn=atan(rho/lambda), and Q2=2(rho-lambda Atn). Direct integration gives

    integral_-rho^rho ||DeltaF(delta)||/R^2 d delta
      <= J_int := delta_m L+D3(rho^2-lambda^2 L)
          +lambda H_hop Q2
          +Jfac[2C0 Atn+lambda C1 L+lambda C2 Q2].         (8)

Every term in this upper expression is nonnegative. In particular the calibration term is <=pi Jfac C0, not C0 log(rho/lambda). The mass discrepancy and loaded slope genuinely retain their logarithms, with prefactors delta_m=O(lambda) and lambda C1.

For rho=min(d_bg,a/2,sqrt(a lambda)) at fixed supplied coefficients and fixed g,h, all terms in (8) except the inherited C0 contribution tend to zero: delta_m L and lambda C1 L are O(lambda log(1/lambda)); the Taylor term is O(rho^2); the hopping term is O(lambda m rho) with fixed gap-dependent constants; and lambda C2 Q2=O(lambda rho). The remaining upper allowance is O(j a0), with the smaller quadratic a0 term retained. It does NOT vanish by increasing m.

For a unit selected bare-seed column, the corresponding selected three-source BOUNDARY-INTEGRAL difference, after the actual physical congruence, is at most

    36 J_int/[pi sqrt(Z0) s^2(1-zeta)]                     (9)

uniformly in time. The 1/pi accounts for both lips in Stone's 1/(2pi i) formula; the output mass congruence has norm at most one, while the input factor is exactly 1/sqrt(Z0). Equation (9) compares the cutoff physical column to U T_P S_crit^(-1) T_P U, not to an unscaled unit-normalized three-site source. Identification of this boundary integral with the actual spectral evolution requires the assembled physical boundary/Stone argument below. Equation (9) alone proves neither a mediator norm bound nor a complete pulse theorem.

## 4. All mediator heads: stationary dressing plus a controlled variation

Let X(E) be the vector of physical endpoint columns at s0,s1,s2,p. The exact mediator recovery is

    K_l(E)X=-gamma_l(D tensor I+A_l)^(-1)
                                      (C_L X_left+C_R X_right).

The three internal paths are disjoint. For real E in the window, this recovery is the same on both lips because the mediator blocks are in their local gaps. On a mediator's own two-endpoint scalar selected domain its Gram contribution is exactly

    K_l(E)^*K_l(E)=-Sigma_l'(delta).                       (10)

Thus the physical endpoint-plus-mediator Gram matrix is I minus the assembled self-energy derivative. At the center it contains the finite source masses Z_im AND port mass 1+w_m; away from the center it also contains off-diagonal derivative terms. This identity cannot be replaced by a free rescaling of the seed or port. It is a stationary Gram identity, not permission to ignore cross-energy terms in a time-domain norm.

A useful finite-interval recovery reduction follows from the resolvent identity, without counting mediator heads one by one. Set E0 to the center of the particular physical window. On the selected channel,

    ||K_l(E)-K_l(E0)||<=gamma_l |delta|/[a(a-rho)].

On the complement the product of the two physical resolvent bounds costs at most gamma_l |delta|/b^2, which is smaller on this domain. K(E0) there uses the physical D_C(E0)+A_l, not A_l alone. Combining all three disjoint paths therefore gives

    ||K(E)-K(E0)||<=sqrt(Gamma2)|delta|/[a(a-rho)].         (11)

No factor proportional to the 10m-4 internal heads is needed: (11) is an operator norm into their joint Hilbert space.

For completeness, the checked full inverse supplies a uniform endpoint-column bound. With b_mix from that source, define

    Rmax=sqrt(rho^2+lambda^2),
    A_src=6(1+b_mix/k_C)^2/[s(1-zeta)]+Rmax/k_C,
    T3max=max(sqrt(Z2)kappa(1+theta3),tau),
    C_end=A_src sqrt(1+(B_tilde T3max)^2).

Then ||X_+(E)||,||X_-(E)||<=C_end/R for any unit source-site forcing on the full fiber. The extra endpoint p follows from the exact physical relation psi_p=G_tilde t3(D)psi_s2. This bound retains complementary source coordinates.

Write X_I(t) for its two-lip endpoint boundary integral on this ONE window, and M_I(t) for the corresponding all-mediator integral. Equations (11) and the two-lip norm bound imply

    ||M_I(t)-K(E0)X_I(t)||
      <=2sqrt(Gamma2) C_end [Rmax-lambda]
                              /[pi a(a-rho)]
      <=2sqrt(Gamma2) C_end rho/[pi a(a-rho)].             (12)

The elementary integral is integral |delta|/R d delta=2(Rmax-lambda). This error tends to zero with rho at fixed coefficients and the checked eventual margins. Equation (12) is a separate, unchecked ancillary author reduction, not part of the previously checked loaded-inverse contract. The nonzero K(E0)X_I(t) term remains: mediator vacancy follows only after the corresponding endpoint response is shown small. In particular the static third-path PORT term remains. The coarse C_end/R bound by itself has a logarithmic integral and does not prove that port term decays. For two windows use their own physical centers and recovery maps and justify input aggregation; they are not one unexamined common dressing map. Actual outside-window state is still charged separately by the product witness. The reference dressed witness is not substituted for the input.

## 5. Outgoing handoff: exact identity, estimates still open

The background outgoing row remains the old emitter-free row L_x because the corrected compression restores the same H_bg. The NEW source-dependent row is exactly

    A_med,x=L_x (I-s3(D)G_x)^(-1)
                            t3(D)(S_x^(-1))_20.           (13)

This follows from the background equation with its added port diagonal. The inverse sits to the left of t3(D); neither is commuted through G_x. With the physical scalar reference, the ideal selected row is x omega A_sc P from section 2. This retains the exact complex source denominator, converter phase and source-to-port sign.

The outgoing coefficient requires a different weighted estimate from the local-source Stone integral. The physical port factor and the last-source column must be retained before integrating. A direct 1/R envelope or the local estimate (9) is not an outgoing L2 theorem. The exact selected scalar last-source entry is b1 b2/q_sc; its comparison to the full selected column must retain complementary feedback and the physical 1/sqrt(Z0) factor. An explicitly bounded scalar determinant or an energy-resolved absolute column estimate is a viable next interface; neither is declared complete here.

Only after proving that source-to-port estimate should one apply the checked full row ceiling ||L_x||<461 and reference-row error j||L_x-ell_x P||<=2.1e-13+304|q-pi/2|+.302|delta|/g, together with the actual flux/Jacobian. A separate wrong-window estimate must start with complementary PREPARED forcing in (25) of the loaded source; deleting it because the scalar reference has only one open input is invalid. Root is separately deriving this raw traveling-coefficient interface. That work is not a premise of this proposal, and this note supplies no duplicate outgoing error or complete theorem.

## 6. What remains before a claimed dynamical theorem

The immediate checkable contributions here are physical scalar normalization (2)--(5) and the source/mediator boundary-integral comparisons (9),(12). The next theorem must combine them with a separately proved complete-input outgoing L2 comparison based on (13), preserving literal phase and an explicit p_m normalization cost. The new partial lemmas in this note need distinct checks; the outgoing column estimates are still a specified obligation.

The actual assembled Stone identification must be written from the physical off-real resolvent and the inherited finite background matching, using the new mediator and source inverse margins. Continuous pointwise formal boundary expressions alone are not a statement about every possible spectral component. Establish uniform local boundary reconstruction of the prepared finite-coordinate columns and exclude any hidden in-window singular seed mass under those premises. Outside the common window union, use the one actual product-witness bound; no global spectral gap is assumed.

A quantitative useful-time claim then needs endpoint/port escape and physical outgoing arrival. Equation (12) reduces mediator escape to the endpoint columns plus a controlled energy-variation error; it does not set a time. The exact scalar h_m has qualitative local escape for each fixed m by its absolutely continuous finite-coordinate spectral measures, but that supplies no rate uniform in m. Its exact phase in (1)--(4), the original dispersion, the incoming component and every old finite-background/closed-tail output must be analyzed at the new parameters. A new finite receiver cut must be paid afterward. No old three-site pulse, sixth moment, runtime or apparatus count is inherited.

The two fixed allowances are kept distinct: a0 is an inherited background calibration upper allowance, while delta_p is the bare-product preparation certificate. Neither is a demonstrated lower error. The mass congruence, the normalized comparator and the mediator recovery map cannot turn either into an actual state preparation. This is a route to a conditional dynamical result, not a full result already obtained.

## 7. Exact exposure and limits

Paths are relative to `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934`.

| Source | SHA256 |
| --- | --- |
| `mediated_loaded_inverse_interface/PROPOSAL.md` | `5f909e1ea897e9aaef31dd362e42fc60d5ba0b5f595d28bd12f1d000d8552a22` |
| `mediated_loaded_inverse_interface_check/REVIEW.md` | `f6303bb308a56b0db39cf66b673e40174be775e7a32a71f28a6e489beb3990c3` |
| `mediated_mass_tuned_family/PROPOSAL.md` | `d01ed6b60f3bacf2b7557687995902f8c3e172eafecd7a1547cb3bc458451883` |
| `mediated_mass_tuned_family_check/REVIEW.md` | `6a7a9f0dcb6ea04e5bde943e99a9ab7e04755ab0cfb26a07e6d1a4fd4e174b2e` |
| `mediated_product_seed_witness/PROPOSAL.md` | `57892f7690a5f634c44c2fe0752c5cfb682d3fbfbda1aa4c1ca4edd45bb0fdee` |
| `mediated_product_seed_witness_check/REVIEW.md` | `aac24f84f9373a5e59511195e717780d24ecffc41c1e4cb878bcf262a4085630` |
| `three_site_outgoing/PROPOSAL.md` | `af580b44fc2ebfc35eb014ffc63b8bae17464150677ede4a8b8315886f6f36ac` |
| `three_site_outgoing_check/REVIEW.md` | `721a183db3e42527d7cb5bdda697e6c6d81312a94cf047dd7ea15897cb4c2f02` |

The mass/witness sources and checks were fully read in the preceding coherent task; their identities are unchanged. The loaded review and outgoing source/check were fully refreshed here. The old scalar source `a89025dafcb588459e88c14fa802e9e9ce2e5184aa42d9d22f6521a1dadb4823` was also read as context, not imported as a mediated-source theorem. The exact corrected installation and its review chain remain pinned through the loaded source.

I authored the loaded proposal and earlier core work and share substantial exposure to this lane. Root suggested the energy-resolved refinement in section 3 while this task was underway; its subtraction and integrals were reconstructed here, not presumed. The other reductions are new author work, not independent certification. No scientific execution, spectrum, quadrature, time evolution, parameter point or sweep occurred. Only this proposal was written. No W/Git/PR/publication/checkpoint/prompt/axiom/model changes or delegation occurred.
