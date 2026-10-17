# Distinct check of the prepared converter derivative

**Conditional support for the stated finite-output, selected-input bound.** I read the complete proposal at SHA256 `a444e105c88fcfad8fcae59b7f72d9dd9247e2b83ada73edeb7b97a849b33653` and reconstructed its converter equations, complex finite-coordinate ceilings, product rules and numerical margins. The bound

    ||d(Phi_old P_new)/dE|| < 5.1e11

follows from the exact inherited premises and the newly checked original-core derivative. No change to that final constant is needed. One intermediate margin should be made explicit: the claimed `||b_C||<3e-12` does NOT follow using only the displayed coarse `||N||<2` and `||u||<.5`. The actual Neumann margin and the stronger velocity-based value do prove it; section 4 below supplies the short missing estimate. I also spell out why `||eta_base||<.5` is justified, rather than inferring it from a loose unrelated collection of scalar bounds.

The original-core source remains unchanged, including its historical pending-check labels. Its subsequent distinct root review `75563597ec6edd1b688bfd81b51b4dc5b1adab7033d9f78a860f759cf5e70729` now supports `||Psi_B'||<1e12` for the original unconverted **finite** 172-head recovery. This review uses exactly that scope. It does not obtain an arbitrary-forcing derivative, infinite-tail derivative, source escape estimate or new runtime theorem.

## 1. Domain, physical derivative and exact feedback order

The nominal map is unchanged:

    E=2j(1-cos q)=2J(1-cos k),
    |q-pi/2|<=h<=4e-6,
    |k-k0|<.96e-6,
    E_k'>.025, E_q'>.0053.

The bandwidth source first places the new interval inside the ORIGINAL old interval by its energy margins. Thus the bounds `|dk/dE|<40` and `|dq/dE|<189` are available before any derivative is taken. Fixed old energy/parity and fixed real B spectral projections mean that no derivative of a moving channel basis is omitted. The old J, new j, converter supplier, scalar offsets and physical energy windows are not retuned.

At the original port origins write the finite-buffer field as `Q^-m a+Q^m b`. The generalized scattering relation is `b=T A^-1 a`, with the inverse on the RIGHT. The canonical Green kernel gives an incoming source coefficient `A Q^n` and outgoing coefficient `T Q^n`; eliminating that source coefficient proves this order without commuting T through A.

The signed closed converter return is diagonal in the fixed B projections. At F=40 the exact boundary equation gives

    a_C=E_c b_C, E_c=R_c Q_C^80,
    b_C=(I-S_CC E_c)^-1 S_CP a_P,
    S_tilde=S+S_PC E_c(I-S_CC E_c)^-1 S_CP.

These equations retain both port converters, all seven complementary directions per port and their noncommuting source blocks. There is no replacement of a mixed source by independent scalar sources.

For OPEN incidence at the outer old planes, `u=z^-40 a_P`. Substituting the exact converter relation gives

    u=(I-r_o S_tilde,B)^-1 eta_c alpha,
    S_tilde,B=z^80 S_tilde,
    eta_c=t_c sqrt(v_new/v_old).

The common factor `z^40` disappears only from the conversion between origin and outer incoming coefficients; the round-trip `z^80` remains. The original open scattering matrix already has its 90-step phase. The separately checked bound `||(S_B)_k'||<894` pays all 170 steps and gives `||S_B'||<35760<36000`. The new first-site phase `exp(iq)` in t_c is also retained below.

## 2. The coarse Cauchy bounds have an actual finite analytic domain

I refreshed the canonical matching/filter and complex-disk passages, rather than extrapolating a real small reflection or dwell norm. At every real old k under consideration, the supplied disk of radius `rho=1e-12` has the analytic fixed-projector root continuation and explicit ceilings

    ||M16^-1||<167, ||A||<41, ||A^-1||<22,
    ||T_g||<208, ||Q_C||<.15,
    ||(I-G_filter V)^-1||<2100, ||V||<.05,
    ||Ttilde||<2e7.

In particular, the inverse-root recurrence is used in M16 before estimating its variation. The real inverse/calibration inequalities are conditional source premises; neither this review nor the converter proposal recalculates them. The continuation of the free inverse A uses its explicit open and closed spectral formulas, as in the canonical disk argument. It does not depend on unitarity away from the real axis.

For S_gen, the filtered arm image coefficient propagates 24 steps to each original port origin. Its two-sided open factor is at most `exp(48rho)<1.001`; closed powers are decaying. The fixed real junction mixing is unitary. Even the proposal's extra factor two gives

    ||T||<4.1e7,
    ||T A^-1||<4.1e7*22<1e9.

The unfiltered arm is covered by the same envelope. Applying scalar Cauchy to fixed input/output unit vectors and then taking the operator supremum yields `||(S_gen)_k'||<1e21`, with no dimension factor. The physical chain rule gives

    ||S_gen'||<4e22.                                      (1)

This bound applies to all its blocks. The open first derivative uses its much sharper scattering estimate instead; replacing that derivative by (1) would destroy the useful open-incidence estimate.

For the complementary recovery `H_C=G_old(O,B) A^-1 C`, O is the full finite old region and B the two outer old sites. Unfolding the constant junction gives two 86-position arms: 45 original arm positions plus 41 old buffer positions each. The two-arm transformation and coordinate rearrangement are energy independent. Physical blocks have eight-dimensional fibers; those are covered by block operator norms, not multiplied as extra scalar coordinate counts.

On each finite arm, the bare free/image block is bounded by

    41 exp(86rho)+208 exp(170rho)<300.

This safely covers all coordinate differences and sums in the finite range. Contact-to-free blocks follow from the M16 inverse block times a nonnegative outward Q power and also fit 300. No incoming growing closed coefficient is introduced by this kernel formula. A row restricted to the two filter sites has norm below `sqrt(2)*300<500`. The Woodbury update therefore gives the per-site-block ceiling

    300+500^2*.05*2100=26,250,300<2.7e7.

Allowing another factor two for physical mixing still leaves every relevant block below `1e8`. A safe block square-sum estimate on the 172-by-2 boundary column then gives

    ||G_old(O,B)||<sqrt(344)*1e8<2e9,
    ||H_C||<2e9*22<5e10

on the actual analytic disk. Cauchy and `|dk/dE|<40` establish

    ||H_C'||<2e24.                                       (2)

This argument concerns finitely many actual coordinates. It does not estimate an off-real scattering wave over an infinite lead, invoke a whole-space real resolvent norm, or differentiate the sharper real value `||H_C||<160` as though it were an analytic-disk bound. That real 160 is reused only where the product rule requires a value.

## 3. Closed converter derivatives and the 80-power feedback

For each signed closed root pair a,w, the exact reflection ratio is

    R_c=-N_c/D_c,
    N_c=J-j-Ja+J S0 w,
    D_c=epsilon-J-j+J S0 w+Ja.

The second expression for D_c is the one to differentiate: `epsilon'=1`. It is algebraically identical to `J-j-J/a+J S0 w` by the old root equation, but avoids separately bounding a derivative of a large inverse root.

The real bounds `|a|<=1/7`, `|w|<1/60`, `|a'|<5`, and

    |w'|=|w|^2/[j(1-|w|^2)]<.104

hold for either sign of each closed root. With `.03<J<.031` and `S0<.5`,

    |N_c'|<.031*5+.031*.5*.104<.157,
    |D_c'|<1+.031*5+.031*.5*.104<1.157.

Using `|D_c|>.1797` and `|N_c|<.0358`, quotient differentiation gives less than 2.16, hence the stated loose `||R_c'||<3`. The inherited value `||R_c||<.2` remains separate.

Because all closed projectors are fixed, the power derivatives are exact scalar derivatives within each block. Since `7^40>1e32`,

    ||E_c||<.2*7^-80<2e-65,
    ||E_c'||<(3+560)*7^-80<6e-62.

For `N=(I-S_CC E_c)^-1`, the order in

    N'=N(S_CC' E_c+S_CC E_c')N

is correct. Using `||N||<2` here is harmless and gives `||N'||<4e-42`. Differentiating all four factors of `S_PC E_c N S_CP`, the two terms containing a differentiated source cross block are each below `9.6e-54`. The E_c' term is below `4.32e-84`, and the N' term below `2.88e-129`. Thus the proposal's derivative ceiling `1e-51` is safe, as is its real correction ceiling `1e-86`.

Moving this correction to the outer open planes adds at most `80*40*1e-86`. Therefore `||S_tilde,B'||<36001` follows. Its real norm is one by exact flux conservation for the real finite source with decaying closed loads; no flux is assigned to closed modes. The source's alternative `1+1e-86` norm bound would leave the subsequent margins intact.

## 4. Open coefficient derivative, and the needed b_C value margin

Reciprocity identifies the two flux-normalized transmissions. It does not equate unnormalized old and new site amplitudes. Substituting the physical transmission formula yields exactly

    eta_c=eta_base(1+r_o),
    eta_base=exp(iq) sqrt(j S0/J) sin(q)/sin(k).

In particular, eta_base includes the first-new-site phase. Its magnitude bound below .5 can be justified without guessing: it is the product of `chi=sqrt(v_new/v_old)<.49` and the source's transmission square-root factor `sqrt(S0 sin(q)/sin(k))<1.000003`. Thus `||eta_base||<.490002<.5`.

Both converter numerator and denominator have q derivatives below .029. On the enlarged interval their denominator is greater than `.024-.029h>.0239998`. Consequently

    |r_o'|<(.029*189/.0239998)(1+4.88e-6)<230.

The logarithmic derivative of eta_base is

    i q'+cot(q) q'-cot(k) k'.

The respective magnitudes are bounded by 189, .000945 and 100. Therefore `||eta_base'||<145` and

    ||eta_c'||<145(1+4.88e-6)+.5*230<300.

For unit fixed alpha, exact flux conservation gives `||eta_c||<.49`, and the open return inverse is below `1.000005`. This supplies the sharper value

    ||u||=||a_P||<.49*1.000005<.490003,                  (3)

as well as the rounded .5 used in derivative estimates. Differentiating the ordered open equation with alpha fixed gives

    u'=(I-r_o S_tilde,B)^-1
        [eta_c' alpha+(r_o' S_tilde,B+r_o S_tilde,B')u].

The proposal's bound is therefore justified:

    ||u'||<1.000005[300+(230+4.88e-6*36001)*.5]<500.

For the original coefficient `a_P=z^40 u`, its additional physical phase derivative is at most `40*40*.5`; hence `||a_P'||<1300`. There is no cancellation of this derivative in the origin closed-feedback equation.

Here is the explicit completion of the `b_C<3e-12` margin. The actual closed feedback satisfies

    ||S_CC E_c||<(6e-32)(2e-65)=1.2e-96,
    ||N||<1/(1-1.2e-96)<1.000001.

Combining this with (3) and the stated cross bound gives

    ||b_C||<1.000001*(6e-12)*.490003
             <2.941e-12<3e-12.                         (4)

Thus the number used in the source is valid. The proof should retain this sharper value step, or cite the older already-composed `b_C<6e-12||a_P||` estimate, rather than relying on its coarse N<2 display. This is a local proof clarification, not a changed device, added assumption or relaxation of the final constant.

For the derivative, the coarse N<2 DOES suffice:

    ||b_C'||
      <=||N'|| ||S_CP|| ||a_P||
         +||N|| ||S_CP'|| ||a_P||
         +||N|| ||S_CP|| ||a_P'||
      <4.1e22.

The dominant contribution is bounded by `2*(4e22)*.5=4e22`; the other terms leave ample margin.

## 5. Actual closed incidence and the finite-output product rule

At the outer old plane the incoming complementary coefficient is

    v=R_c Q_C^40 b_C.

This is obtained from the origin coefficient `R_c Q_C^80 b_C` by evaluating its growing incoming wave at m=40. Exactly forty powers cancel BEFORE taking any norm. Treating the origin return and a separately unbounded inverse-root factor would be the wrong estimate for this physical coefficient.

Fixed projectors give `||(Q_C^40)'||<=200*7^-39=1400*7^-40`. Using (4), the source's three product-rule terms yield

    ||v||<.2*7^-40*3e-12<1e-44,
    ||v'||<3*7^-40*3e-12
             +.2*1400*7^-40*3e-12
             +.2*7^-40*4.1e22<8.3e-11.

The first two derivative contributions are below `9e-44` and `8.4e-42`; the third is below `8.2e-11`. Both signs of all complementary roots are retained. There is no small-value-to-small-derivative inference for b_C or v.

The exact physical decomposition at the same planes is

    Phi_old P_new=Psi_B u+H_C v.

The Green column with its source at B supplies the prescribed incoming field everywhere in O, which ends at B. The supplementary exterior incoming-minus-outgoing wave used in the original Green derivation is outside those planes; it does not add an omitted term inside O. This is why using the full finite physical Green column in section 2 is consistent with the incoming convention.

From (2), the actual real `||H_C||<160`, and the v estimates,

    ||(H_C v)'||<(2e24)(1e-44)+160*(8.3e-11)
                  <1.4e-8.

The original-core review supplies `||Psi_B'||<1e12` for this original finite map, while the distinct dwell check supplies `||Psi_B||<30`. All four product-rule terms are therefore paid:

    ||(Phi_old P_new)'||
      <(1e12)*.5+30*500+1.4e-8
      <5.1e11.

The result includes the full old finite output, its internal source excitations and wrong-window/complementary OUTPUT coordinates. It is a selected two-new-port OPEN-input bound separately on each physical old-energy window and parity. Fixed real conjugation supplies the other lip; tensoring a passive reference does not change an operator norm. Input vectors are held fixed in this derivative.

## 6. Limits and source exposure

This check does not extend the result to arbitrary complementary NEW-port incidence, new converter sites/tails beyond O, the complete infinite closed-tail derivative, input termination, wide-gate feedback or the resonant three-source derivative. A later full endpoint-forcing calculation must still charge the actual complementary coefficient and its derivative against an appropriate complete complementary recovery. Likewise, a full L' needs its cap/gate coefficient derivatives. No runtime improvement, finite receiver count, permanent record, native supplier or microscopic Hamiltonian conclusion follows from this bound alone.

I authored `prepared_core_recovery/PROPOSAL.md` and the large three-site composition, and previously read the shared original kernel and converter ancestry. I did not author this converter derivative proposal or the direct-core derivative proposal. Root exposed the target, the original-core review and the potentially insufficient coarse N margin. This is a source-exposed distinct calculation with shared premises, not a blind or model-independent review, and not a new audit of the canonical calibration or the whole endpoint theorem.

The complete changed converter argument, direct-core source and new root check were read. The complete converter composition, its check and enlarged-band argument were refreshed; the canonical physical/matching/filter passages 145--319 and analytic-disk passages 1386--1518 were read. The exact previously checked dwell/value results were reused within their scope, with the relevant physical-plane and boundary-column passages reread. Every source identity in the table below was verified from actual bytes. No changed source or calibration is silently substituted for an older snapshot.

| Source relative to the renewal directory, except the last row | SHA256 |
|---|---|
| prepared_converter_direct_derivative/PROPOSAL.md | a444e105c88fcfad8fcae59b7f72d9dd9247e2b83ada73edeb7b97a849b33653 |
| prepared_core_direct_derivative/PROPOSAL.md | cfca9422163b4f4694a2efddbbff6779bd3c354bbd505e90af4d16189d1e40be |
| prepared_core_direct_derivative_check/REVIEW.md | 75563597ec6edd1b688bfd81b51b4dc5b1adab7033d9f78a860f759cf5e70729 |
| prepared_core_recovery/PROPOSAL.md | cce29994b7141df161ca12f377765fdaf760f7e64fc56043bbf370e2cd437ea9 |
| prepared_core_dwell_check/REVIEW.md | 88274b8b49e583bdb9b5f933f7406b1a96a6ca79049e57b83e8030c834d16819 |
| prepared_core_composition_check/REVIEW.md | 52edba6061be49eef40b5c06754a7425b5f7f62671f175cc72a093d4a60de65c |
| bandcenter_converter_composition/PROPOSAL.md | 1cc6fec524a8184f844711a4fa6d72fcc7cd13a4c8b413cbc064cd4b2201df78 |
| bandcenter_converter_composition_check/REVIEW.md | f1653ba00c0f3d10d8846c1f010ad6dcddcd25535837dd87d17b9e655019a15c |
| bandcenter_bandwidth_extension/PROPOSAL.md | d79a1e9abbf0508a05169d4588539063854f0604ba8db933cf878496aa7328a2 |
| correlation_worktree/docs/REAL_ENDPOINT_AUTONOMOUS_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md | 71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff |

Only this review was created. All calculations above are analytical reconstructions; no scientific source was imported or executed, and no numerical inverse, dynamics, sweep or new calibration was run. Deterministic source/hash reads are metadata evidence only. No original proposal, W, Git, PR, checkpoint, editable prompt, axiom or model setting changed; no delegation or audit action occurred.
