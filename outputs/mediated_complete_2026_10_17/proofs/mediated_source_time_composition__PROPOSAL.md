# Full represented source-time bound for the mass-tuned mediated apparatus

Status: new conditional author composition, requiring a distinct check. The result is a time bound for the THREE physical source endpoint heads, with every internal source-fiber component and both prepared old-energy inputs retained. It is not a bound for the mediator heads, processor background, incoming/outgoing rays, or the actual omitted spectral vector. Those are separate pieces of a complete-output argument.

The checked one-window selected-output comparison is sufficient once the full complementary blocks are paid. The resulting bound has the requested form

    A_s(t) <= min{1, C_s exp(-lambda t/2) + S_s},
    C_s = 9/sqrt(Z0),                                      (1)

with an explicit finite-m S_s below. A sharper polynomial-times-exponential allowance is also given. This compares the actual represented source to a mass-contracted critical reference; it does not substitute the exact mediated scalar waveform, normalize an effective seed, or assign the ordinary source's sixth moment to the physical mediated seed.

## 1. Physical domain and meaning of A_s

Retain the corrected installation, fixed mass-tuned coefficient family and ALL hypotheses of the checked loaded inverse `5f909e1e`/`f6303bb3`. In particular the old calibrated emitter-free background is unchanged, the shared B and physical c_att occur once, cap replacement is literal replacement, and all supplied positive blocks, roles, preparation and calibration hypotheses remain. This proof uses the original centered physical operator. A separately supplied scalar shift would require its known full phase and shifted window centers; no such alteration is needed here.

Use the notation of that source: .0027<j<.003, a=J_m-q>0, r=q/J_m in (0,1), n1=n2=2m-1, n3=m, and fixed supplied gamma_l<=a/4 satisfying its exact mass equations. Put

    u=gamma1^2/(J_m^2-q^2),
    v=gamma2^2/(J_m^2-q^2), w=gamma3^2/(J_m^2-q^2),
    Z0=1+u, Z1=1+u+v, Z2=1+v+w,
    lambda=lambda_m=Lambda r^(2m-2),
    Lambda=sqrt(3)gamma1^2/[J_m sqrt(Z0 Z1)],
    kappa=sqrt(3j lambda), delta_m=(u+v+w)r^(2m).

The three Z_i are the fixed limiting masses, not a new physical preparation. For a finite m the finite-m mass discrepancy remains in delta_m. Require 0<lambda<=1e-8 and

    0<rho<=min(d_bg,a/2), d_bg=2j sin h,
    0<h<=4e-6, 0<g<=1e-6, d_bg/g<=.5,
    eta<1, k_C>0, zeta<1.                               (2)

Here eta,k_C,zeta are the explicit ordered-port, complementary and selected inverse gates of the loaded source. No full spectral gap is assumed. All their finite-m definitions and strict inequalities are premises, not replaced by the asymptotic discussion below.

Let V be the actual bare product preparation, including initial record0, and let Pi_1,Pi_3 be the old K energy projections. Its internal preparation iota_0 obeys B iota_0=iota_0 K, including the unchanged source vacuum and record convention. For b=1,3 define

    E_b=c_att+2j+b, I_b=[E_b-rho,E_b+rho], I=I_1 union I_3.

Let Q_s project onto s0,s1,s2, tensored with the ENTIRE internal fiber. The quantity proved here is exactly

    A_s(t)=||Q_s exp(-itH) E_H(I) V||, t>=0.             (3)

H is the actual assembled infinite-lead operator covered by the stationary and seed-regularity premises. Formula (3) includes source components outside the selected internal energy and preserves arbitrary coherent old inputs and passive references. It excludes the actual vector E_H(I^c)V. No actual outside allowance is added anywhere in this proposal.

The regularity source `f8153ddb` and check `9d837417` supply the missing actual Stone identification: the finite-coordinate seed measures are absolutely continuous on neighborhoods of both closed windows, and their densities are the physical lower-minus-upper resolvent column jumps divided by 2pi i. This uses full inherited analytic matching and the strict new inverse gates, not a small value bound on G alone. It requires neither a parameter-uniform continuation strip nor a temporal estimate. Both lips and the window endpoints are covered for each fixed finite m.

## 2. Selected and complementary physical columns

On one window let P be the selected B spectral projection and C=I-P, and use P_src=I_3 tensor P, C_src=I_3 tensor C on the source coordinates. Subsequent block subscripts P,C mean these source projections; C_s in (1) remains the time-bound constant. The other prepared old-energy input lies in C on this window. It is not removed from the proof.

Write

    T_P=diag(Z0^(-1/2),Z1^(-1/2),Z2^(-1/2)) tensor P,
    T=T_P direct-sum I_C,
    U=diag((-1)^m,(-1)^(m+1),(-1)^m) tensor I_fiber.

The exact physical inverse is S^(-1)=U T S_hat^(-1) T U. With the loaded source's actual ordered Schur blocks it is

    S_hat^(-1) =
      [[F^(-1), -F^(-1) X K_C^(-1)],
       [-K_C^(-1) Y F^(-1),
        K_C^(-1)+K_C^(-1)Y F^(-1)X K_C^(-1)]].          (4)

No relation X=Y* on a fixed lip is used. Define the uniform nonnegative bounds

    s=sqrt(1-3lambda/j), R(delta)=sqrt(delta^2+lambda^2),
    C_F=6/[s(1-zeta)],
    e_rho=a0+b0 rho, a0=8e-18, b0=46000/.0053+290/g,
    e_tilde=e_rho/[(1-eta0)(1-eta)],
    theta3=(1-rho^2/a^2)^(-m)-1,
    tau=gamma3^2/b_gap, b_gap=.185-(J_m+q),
    b_mix=kappa(1+theta3)e_tilde tau, beta_mix=b_mix/k_C.

Here eta0 is the unperturbed ordered-port bound from the loaded source; it is less than one under its contract. The inequalities underlying (4) are

    ||F^(-1)||<=C_F/R,
    ||K_C^(-1)||<=1/k_C, ||X||,||Y||<=b_mix.             (5)

Consequently a unit selected bare-seed input has complementary SOURCE output at most

    ||C_src S^(-1) e_s0 P||
       <= C_F beta_mix/[sqrt(Z0) R].                    (6)

The right T gives exactly 1/sqrt(Z0); the left T is the identity on C and the fixed gauges have norm one. This is the output that is absent from the checked selected-output lemma.

For a unit complementary bare-seed input, the two physical output blocks satisfy

    ||P_src S^(-1) e_s0 C|| <= C_F beta_mix/R,
    ||C_src S^(-1) e_s0 C|| <= 1/k_C+C_F beta_mix^2/R.   (7)

The left selected T is a contraction, while the input T equals the identity on C. The sum of (7) bounds the norm of the whole three-source column. This is deliberately conservative; no orthogonality of the upper- and lower-lip columns is assumed.

In particular the first term in (7) for the complementary output block is retained in full. Although the constant closed scalar reference has a zero jump on the wrong window, the ACTUAL K_C contains loaded feedback. This proof never claims its jump is zero or that it is a real matrix on the physical lip.

## 3. One-window integrated errors

Every following error is uniform in t. For a physical column majorant B(delta) that applies on both lips, the absolute Stone bound is integral B(delta) d delta/pi. It follows from triangle inequality on the lower-minus-upper jump; an entrywise imaginary part of a rectangular column would be incorrect.

### Selected source output

Reuse precisely the checked energy-resolved estimate in section 3 of `mediated_pulse_bridge_plan`. For selected input and selected three-source output the physical comparison is

    U T_P S_crit(delta)^(-1) T_P U,

where

    S_crit=[[delta,lambda/sqrt(3),0],
            [lambda/sqrt(3),delta,lambda sqrt(8/3)],
            [0,lambda sqrt(8/3),delta-3jlambda m_j(delta)]].

This is the exact finite-band critical scalar comparison, including its physical Weyl function m_j. The checked L1 lemma gives

    D_sel=36 J_int/[pi sqrt(Z0) s^2(1-zeta)].             (8)

For an explicit usable definition, introduce only the inherited bounds

    A_err=1/[(1-eta0)(1-eta)], B_err=A_err^2 tau^2/k_C,
    nu=gamma3^2/[a(a-rho)], Gamma2=sum_l gamma_l^2,
    D_3=Gamma2/[a^3(a-rho)],
    theta12=(1-rho^2/a^2)^(-(2m-1))-1,
    H12=(2m-1)/a^2 * (1-rho^2/a^2)^(-2m),
    H3=m/a^2 * (1-rho^2/a^2)^(-m-1),
    H_hop=sqrt(3)H12+3(2+theta3)H3,
    Jfac=3j(1+theta3)^2,
    C0=A_err a0+B_err a0^2,
    C1=nu/[j^2(1-nu rho/j)]+A_err b0+2B_err a0 b0,
    C2=B_err b0^2,
    L_log=log(1+rho^2/lambda^2), Atn=atan(rho/lambda),
    Q2=2(rho-lambda Atn).

Then

    J_int=delta_m L_log+D_3(rho^2-lambda^2 L_log)
          +lambda H_hop Q2
          +Jfac[2C0 Atn+lambda C1 L_log+lambda C2 Q2].   (9)

The finite-m gates ensure the displayed denominators are positive. Formula (9) retains the closed feedback, selected port correction, finite mass discrepancy and energy dependence of every effective hopping. It follows by integrating the checked ordered subtraction

    ||F^(-1)-S_crit^(-1)||
       <=36 ||DeltaF(delta)||/[s^2(1-zeta)R(delta)^2],

with the energy-dependent numerator BEFORE dividing by R. Thus the a0 allowance in C0 is integrated against lambda/R^2. It is not multiplied by log(rho/lambda).

### Complementary output from selected input

Define L_R=2 asinh(rho/lambda)=integral_-rho^rho d delta/R(delta). Integrating (6) with both lips gives

    D_out=C_F beta_mix L_R/[pi sqrt(Z0)].                (10)

The critical comparison has no such complementary source output. Therefore the actual complete three-source response to the selected input on this one window differs from its critical physical comparison by at most D_sel+D_out. This triangle bound is valid even without exploiting the orthogonality of the two source-fiber output blocks.

### Wrong-window input, all outputs

Integrating the sum in (7) on the actual finite interval gives

    D_wrong=[2rho/k_C+C_F L_R(beta_mix+beta_mix^2)]/pi.   (11)

Equation (11) bounds the ACTUAL represented wrong-window source response itself. There is no ideal wrong-window source term to add: the critical reference of a prepared energy b has its scalar band at E_b, while the other window is separated by almost 2 and the scalar bandwidth is 4j<.012. Thus its jump on the other window is zero. This observation is about the critical reference, not the loaded complement. Keeping the 2rho/k_C term avoids an unsupported cancellation in the latter.

## 4. Physical critical reference, phases and truncation

Let h_crit be the carrier-subtracted isolated scalar three-site source with negative hoppings lambda/sqrt(3), lambda sqrt(8/3), sqrt(3jlambda), followed by the uniform negative-j ray. Its exact finite-band unitary source column is

    phi(t)=Q_3 exp(-it h_crit)|0>,

where Q_3 retains all three source heads. Define T_src=diag(Z0^(-1/2),Z1^(-1/2),Z2^(-1/2)) and g0=(-1)^m. The untruncated physical COMPARISON column, embedded in the actual source fiber, is

    C(t) f = exp[-it(c_att+2j)]
       [g0 U T_src phi(t)/sqrt(Z0)]
          tensor [iota_0 exp(-itK) f].                    (12)

This expression keeps both old energies coherently, the actual common scalar and every fixed source gauge. It is a comparison map, not an assertion that a mass-rescaled vector was prepared. For example its s0 component at t=0 is 1/Z0, not one. The input 1/sqrt(Z0) and the separate output masses cannot be removed by normalization.

Let C_I(t) be the same map with the direct-sum critical reference spectral projector onto the PHYSICAL union I inserted before Q_3. Its one-window source kernels are exactly those used in (8). Since the reference commutes with K and has the same scalar source for both prepared energies, the untruncated sum (12) has no sqrt(2) penalty in its norm. This orthogonality is used only for the known reference, not the actual error columns.

Here are the complete checked critical pulse bounds, reproduced to specify the time dependence. Put r_c=lambda/j, q_c=1-3r_c, C_c=6r_c+9r_c^2. The finite-band reference amplitudes differ coordinatewise from

    phi_0,M=e^(-x)(1+x+x^2/3),
    phi_1,M=i e^(-x)(x+x^2)/sqrt(3),
    phi_2,M=-e^(-x)sqrt(2)x^2/3, x=lambda t,

by at most

    E0=(C_c+r_c^2/12)/q_c^2+r_c^5/(30pi),
    E1=[4sqrt(3)C_c/(3pi)+sqrt(3)r_c^2/(3pi)]/q_c^2
                                      +sqrt(3)r_c^4/(12pi),
    E2=[C_c/sqrt(2)+5r_c^2/(12sqrt(2))]/q_c^2
                  +r_c^3/(3pi sqrt(2))+r_c^5/(60pi sqrt(2)).

These are controlled finite-band-to-rational comparison errors of the ISOLATED critical reference. The rational cubic pulse is not declared to be an exact evolution of the mediated apparatus. Weighted by the actual source mass factors, define

    F_Z(x)=e^(-x)/sqrt(Z0)
       *sqrt[(1+x+x^2/3)^2/Z0
                    +(x+x^2)^2/(3Z1)+2x^4/(9Z2)],
    E_Z=sqrt(E0^2/Z0+E1^2/Z1+E2^2/Z2)/sqrt(Z0).          (13)

Then ||C(t)||<=F_Z(lambda t)+E_Z. In particular, with E_vec=sqrt(E0^2+E1^2+E2^2) and the checked unweighted F,

    F_Z(x)<=F(x)/sqrt(Z0)<=9exp(-x/2)/sqrt(Z0),
    E_Z<=E_vec/sqrt(Z0).                                 (14)

For reference truncation ONLY, the critical scalar seed has the exact moment

    mu6,ref=3lambda^6+(8/3)jlambda^5,
    eta_ref=min{1,sqrt(2mu6,ref)/rho^3}.                  (15)

Use the conservative checked two-input common-union estimate in (15). Contracting its omitted reference vector by Q_3, the output T_src and the input mass gives

    ||C(t)-C_I(t)||<=eta_ref/sqrt(Z0).                    (16)

The source projection and T_src are applied AFTER the reference spectral evolution; they need not commute with h_crit for this contraction bound. All reference carriers and old-energy phases are included. No bound on E_H(I^c)V follows from (15). The physical mediated seed's first coupling is gamma1 and its second central moment is gamma1^2, already incompatible with assigning it the critical scalar moment by notation. Any actual outside estimate must use its separate valid physical witness or another actual calculation.

## 5. Coherent two-window composition and explicit time criterion

For each b, the selected input V Pi_b on I_b differs from its corresponding C_I column by at most D_sel+D_out. For an arbitrary old vector f, the sum of these two errors has norm at most

    (D_sel+D_out)(||Pi_1 f||+||Pi_3 f||)
       <=sqrt(2)(D_sel+D_out)||f||.                     (17)

This uses input orthogonality and triangle inequality, not orthogonality of actual error outputs. The remaining terms are exactly the two wrong-window responses E_H(I_b)V Pi_(other). Each costs at most D_wrong, so their operator sum costs at most 2 D_wrong. A sharper sqrt(2) bound is possible by the same input argument, but is not needed here. Distinct parity/record-X blocks combine by maximum because the model is block diagonal there; the initial record0 superposition is retained coherently. Equivalently the bounds can be used directly as full-fiber operator bounds. Tensoring with an arbitrary passive reference does not change any norm.

Combining (8)--(17) gives the full physical represented source bound

    A_s(t) <= min{1, F_Z(lambda t)+S_s},                 (18)
    S_s=E_Z+eta_ref/sqrt(Z0)
                    +sqrt(2)(D_sel+D_out)+2D_wrong.

The cap by one is valid because Q_s, E_H(I) and the actual V are contractions and exp(-itH) is unitary. Equations (14) and (18) prove (1), with NO source derivative or assumed decay of an actual resolvent boundary. The decay comes from the checked critical reference after the actual full-column comparison has been paid.

For a chosen finite m satisfying every gate, this also supplies an elementary sufficient local time criterion. If epsilon>S_s, it is enough to take

    t >= (2/lambda) max{0, log[9/(sqrt(Z0)(epsilon-S_s))]}. (19)

Then A_s(t)<=epsilon. This is an estimate for the represented three-head source norm only. It is not an apparatus runtime, a receiver arrival time, or a necessary time bound. If epsilon<=S_s, this comparison does not certify it; it does not prove impossibility or an actual persistent source residue.

## 6. Shrinking-window limit and the calibration allowance

Fix one supplied mass-tuned coefficient solution and fixed background g,h. Take

    rho_m=min(d_bg,a/2,sqrt(a lambda_m)).                  (20)

For all sufficiently large m, rho=sqrt(a lambda), rho/lambda tends to infinity, m rho^2/a^2 tends to zero, and the checked finite inverse gates hold. This is the fixed-coefficient asymptotic proved by the loaded source, not permission to assume those gates for an untested finite m.

The new terms are controlled explicitly. With fixed positive limiting k_C and bounded inverse margins,

    beta_mix=O(sqrt(lambda)(a0+b0 rho)),
    L_R=O(log(rho/lambda)),
    D_out=O(sqrt(lambda)(a0+b0 rho)log(rho/lambda)),
    D_wrong=O(rho)
       +O([sqrt(lambda)(a0+b0 rho)
                      +lambda(a0+b0 rho)^2]log(rho/lambda)). (21)

All terms in (21) vanish. This pays complementary output and wrong-window input without assuming that their pointwise inverse columns vanish: those columns can grow like lambda^(-1/2) near resonance. Their finite-interval L1 bounds nevertheless decrease.

Furthermore E_Z=O(lambda/j), and the reference truncation has

    eta_ref <=sqrt[6lambda^6+(16/3)jlambda^5]
                                         /(a lambda)^(3/2)
             =O(lambda)                                (22)

for fixed a,j. Equation (22) is still a reference-only statement. It says nothing about a physical sixth moment or the actual product preparation allowance.

For D_sel, all terms of (9) vanish except its calibration contribution. To make that statement exact, let the subscript infinity denote the limits of the explicit coefficient bounds along (20). Those limits exist: eta0 tends to tau/[.185-2j], eta tends to eta0+tau a0, k_C has a positive limit, and theta3 tends to zero. Define

    C0,infty=A_err,infty a0
                      +A_err,infty^2 tau^2 a0^2/k_C,infty.

Then J_int tends to 3pi j C0,infty and zeta tends to

    zeta_infty=18j C0,infty<1e-18,                       (23)

using precisely the limiting gate bounds in the checked loaded source. The finite-m masses contribute delta_m log(1+rho^2/lambda^2)=O(lambda log(1/lambda)); the diagonal term is O(rho^2); the hopping term is O(lambda m rho) with fixed gap constants; and the slope term is O(lambda log(1/lambda)). None supplies a nonvanishing logarithm multiplying a0.

Thus the particular explicit upper allowance in (18) has limit

    S_s,infty=sqrt(2) * 108j C0,infty
                            /[sqrt(Z0)(1-zeta_infty)].   (24)

This is a nonvanishing CALIBRATION CERTIFICATE when a0 is retained. It is not a lower bound on actual error or source occupancy. Increasing m alone does not make this certificate arbitrarily small. At fixed scaled time x=lambda_m t_m, the proven bound tends to F_Z(x)+S_s,infty; if x tends to infinity, its decaying term vanishes and the allowance (24) remains. At a fixed physical time t, lambda_m t tends to zero, so source narrowing alone does not furnish a shorter-time conclusion.

The available local interface is therefore concrete: the checked finite gates determine every term of S_s, and (19) determines a sufficient represented-source time whenever the desired tolerance exceeds that allowance. A tiny mediator gap or a large fixed background slope can make the first useful m or time impractical. No coefficient selection, numerical operating point or optimization is asserted.

## 7. Remaining scope, exact exposure and source identities

The new conclusion is (18), or the exponential interface (1), for the actual represented SOURCE endpoints. Mediator dressing cannot be folded into Z_i and discarded: those are additional physical output coordinates, requiring their separately checked recovery theorem and its own error terms. The processor background, closed tails, both traveling directions, actual common-waveform normalization and finite cut likewise require their own bounds. Only a later complete-output composition should add the actual omitted spectral vector, once across all physical outputs. No actual outside error is hidden inside S_s.

The old scalar reference's exact three-source amplitudes and its sixth moment are imported only as reference statements. Neither the exact scalar mediated packet nor a hypothetical Markov physical bath is used. The actual common scalar c_att, old aging, fixed gauges, passive references and preparation are maintained. This is not a derivation of microscopic laws, a prepared mediator state, native coefficient supply, a permanent halt or a full device-performance result.

Paths below are relative to `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934`.

| Source | SHA256 |
| --- | --- |
| `mediated_pulse_bridge_plan/PROPOSAL.md` | `2ad7f5936ab6044d180fe16ddf96f954a077f81f9d3e760df64ee373689b9e36` |
| `mediated_pulse_bridge_plan_check/REVIEW.md` | `b7b8697bbda3746ba98373562cbb9648bb8bc65d378887bcd4b56fe16d4f13cc` |
| `mediated_loaded_inverse_interface/PROPOSAL.md` | `5f909e1ea897e9aaef31dd362e42fc60d5ba0b5f595d28bd12f1d000d8552a22` |
| `mediated_loaded_inverse_interface_check/REVIEW.md` | `f6303bb308a56b0db39cf66b673e40174be775e7a32a71f28a6e489beb3990c3` |
| `mediated_seed_regularity/PROPOSAL.md` | `f8153ddb6a86a58e04e9d69a1ef98d13feefe8f0171ba3cbb3e98cf35ae4522b` |
| `mediated_seed_regularity_check/REVIEW.md` | `9d837417cc295e6d96fcaf1c8db5aad508d618f90cd57bcb9d560bb70640ea6d` |
| `three_site_local_escape/PROPOSAL.md` | `0340895610d3a5ef709dd8a03c1bc5872c8f34cf00f21053c00adcc3d706468d` |
| `three_site_local_escape_check/REVIEW.md` | `e19767c8092fb856a3c24cb279f621deea38d69d65c41bef4a1aea44bad23074` |
| `three_site_product_source/PROPOSAL.md` | `a89025dafcb588459e88c14fa802e9e9ce2e5184aa42d9d22f6521a1dadb4823` |
| `three_site_product_source_check/REVIEW.md` | `c161daea2f3a126ad84baaa63d975b5d80fd3243f11ca3b1075673f62530245b` |
| `mediated_mass_tuned_family/PROPOSAL.md` | `d01ed6b60f3bacf2b7557687995902f8c3e172eafecd7a1547cb3bc458451883` |
| `mediated_mass_tuned_family_check/REVIEW.md` | `6a7a9f0dcb6ea04e5bde943e99a9ab7e04755ab0cfb26a07e6d1a4fd4e174b2e` |

I authored the loaded interface and pulse-bridge proposal and earlier core work. Their distinct checks are reused at the exact scopes above, not treated as a check of this new composition. The pulse-bridge check, regularity source/check, nominal local source/check and critical scalar source/check were read in full for this task; the unchanged fixed-mass and loaded ancestry was read in full in the preceding coherent work and the required ordered blocks were refreshed here. All listed identities were checked. Root supplied the present composition question and requested explicit complementary-output, wrong-input and physical-mass accounting. The calculations in (6)--(24) are this new author composition and still need a distinct check.

The pending complete-output draft mentioned during this task was not read or used as evidence. No scientific execution, dynamics, quadrature, parameter sweep, new numeric point or delegated work occurred. Deterministic text reads and hashes were used for source identity only. Only this proposal was written; no W/Git/PR/publication/checkpoint/prompt/axiom/model changes occurred.
