# Direct action on the actual recovered forcing

Status: new conditional analytical refinement requiring a distinct check. The previously checked full-background inverse remains unchanged. By applying its exact decomposition to the actual recovered column rather than multiplying its norm by4e5, this note obtains

    ||R(E)F(E)||<2.66e17,
    sup ||L'(E)||<1.00068*(2.66e17+1.56e7/g)+3600.      (1)

For the fixed slow hopping g=1e-6 the latter is<2.67e17, improving the preceding4.7e18 ceiling by more than one order. This is an actual forced derivative certificate under the inherited exact source premises, not a new complete-state time or length theorem. No preferred1e17 target is imposed or reached.

## Scope and source exposure

Use exactly the uniform actual slow-output domain: .0027<j<.003, 0<g<=1e-6, 0<h<=4e-6 and d/g<=.024 with d=2j sin h. Both physical old-energy windows, both parities and record-X sectors, all eight internal forcing directions, and arbitrary passive references remain included. The emitter is removed. R is the inverse on235 finite background heads after eliminating only the actual infinite slow ray; F=R V_endpoint is its actual endpoint-forced column. L additionally recovers every slow closed tail, excluding only the nonsquare-summable propagating stationary ray.

The controlling previous source is slow_lead_forced_derivative_sharp/PROPOSAL.md662b64aa1d7714746abaa585f8e1af17ece308771b5c9de25f88fde03bb787c0, now distinctly checked by slow_lead_forced_derivative_sharp_check/REVIEW.md41f8ad9e18d7c1910f8a2c9b7cc70a2cb6b5a89ecbad47d52fd555b694718d4d. I authored the former and read the latter completely for this task. Root requested a direct RF estimate after the checked derivative became available. Its route, ancestry and expected usefulness are exposed; this is author refinement, not independent checking or original calibration. The full source and recovery readings from that coherent task are reused unchanged, with exact pins below.

No new Hamiltonian, preparation, scalar phase, coefficient correlation, energy interval or target waveform is introduced. Literal K stays inside the shared interacting source, and c_att remains the physical scalar. No scientific execution, matrix experiment, parameter sweep, delegation, W/Git/publication, checkpoint, prompt or model change occurred. The sole deliverable is this proposal; all frozen sources remain untouched.

## 1. Partition the actual F before applying any inverse

Partition the finite background into O, N and G:

- O:90 original arm heads plus82 old-buffer heads, total172.
- N:21 retained new input sites and18 cable sites, total39.
- G:24 gate sites.

The actual uniform recovery argument supplies original arms/buffers<240001, input sites<4670, attached upstream correction<2499, cable<7530 and gate-plus-closed-tail recovery<2060. The correction bound is for the entire193-head upstream range; applying it separately to either restriction is conservative. Therefore

    ||F_O||<240001+2499<243000,
    ||F_input||<4670+2499<7200,
    ||F_cable||<7530,
    ||F_N||<sqrt(7200^2+7530^2)<10500,
    ||F_U||<3e5, U=O union N,
    ||F_G||<2060.                                    (2)

The square sum for N is valid because the two finite coordinate ranges are orthogonal. It bounds an operator on the full forcing fiber: ||[A;B]||^2<=||A||^2+||B||^2. These are actual loaded amplitudes, not free incoming waves or old-device runtime estimates. The full closed outgoing amplitude near cable origin remains included in7530.

## 2. Apply the predeletion two-tail kernel to this actual vector

Temporarily extend F_U by zero at the deletion site b=21. Call this vector-valued operator f on the212-head predeletion space. This is a calculation of the action of an auxiliary kernel on a KNOWN forcing vector, not a claim that f solves the auxiliary physical dynamics.

The checked factorization is

    G2=diag(0,Dn)+J Gc J^T,
    J=[I;L_n], ||Gc||<3e10.                           (3)

Here Gc is the172-head kernel after both converters are loaded by free new-j rays; Dn is the direct sum of the free Dirichlet kernels on22 input and18 output sites. The lift from each old boundary to new coordinate m is (tau_c/j)Qn^(m+1). Its two physical boundary supports are orthogonal, so unlike the previous generic40-site bound,

    ||L_n||^2 <=9*max(22,18)=198,
    ||L_n||<14.1, ||J||=sqrt(1+||L_n||^2)<14.2.       (4)

This uses the actual block support, not an open-only restriction. Every channel has ||Qn||<=1 and tau_c/j<3. The transpose has the same Euclidean norm even though J is complex; J^T is not silently changed to J*. Each free Dirichlet block is<400, so the direct-sum norm is<22*400=8800.

The zero extension has the same N norm as F_N. Equations(2)–(4) give

    ||J^T f|| <=||F_O||+||L_n^T|| ||F_N||
                 <243000+14.1*10500=391050,
    ||G2 f||<8800*10500+14.2*(3e10)*391050
                <1.666e17.                          (5)

This keeps the actual amount of forcing in new coordinates. Replacing f by a unit vector and then multiplying the complete inverse norm by||F|| would lose the information in(2).

## 3. Pay input deletion with its actual row action

The complete physical deletion column has norm C_b<130000 and ||Z^-1||<24. Its old-coordinate restriction is<120001; its40-new-coordinate restriction is<3220, from the actual selected source recovery600, the decaying closed factorQn^21, and the full two-port kernel. Hence the same transpose row acting on f obeys

    ||G2(b,:)f||
      <120001*243000+3220*10500
      =29194053000<2.92e10.                          (6)

All these are full eight-coordinate norms, with the selected/closed decomposition performed in the checked port-column proof before taking the full norm. In particular no growing closed input power has been introduced.

Dirichlet deletion gives the exact retained action

    G_D F_U=(G2 f)_U-G2(U,b)Z^-1 G2(b,:)f.

Thus

    ||G_D F_U||<1.666e17+130000*24*(2.92e10)
                       <2.58e17.                    (7)

This is a row-action improvement, not a new bound on ||G_D||. The deleted site's forcing is zero, as required for this exact identity.

## 4. Pay the actual gate load and restore the gate range

Use the checked last-cable column C_a<220000, its diagonal<401, and the actual load Dg=-jQn-j^2Gg with ||Dg||<.117. The complete ordered boundary inverse has norm<4.1; its proof retains rho=Qn^2 r_gate at v17 and the full36-power return at v0. These objects already describe the actual slow output g and both record sectors.

The exact upstream loaded action is

    Ru F_U=G_D F_U
      -G_D(:,a)Dg[I+G_D(a,a)Dg]^-1 G_D(a,:)F_U.

Using the full row bound and ||F_U||<3e5 gives

    ||G_D(a,:)F_U||<220000*(3e5)=6.6e10,
    ||Ru F_U||<2.58e17+220000*.117*4.1*(6.6e10)
                   <2.65e17.                        (8)

This does not reorder the noncommuting source kernel and diagonal gate update. The same physical small port column controls the recovery and forcing sides.

The complete restored inverse has the previously checked blocks

    R_UU=Ru, ||R_UG||=||R_GU||<5e6, ||R_GG||<60000.

Consequently, on the ACTUAL F=(F_U,F_G),

    ||(RF)_U||<2.65e17+(5e6)*2060,
    ||(RF)_G||<(5e6)*(3e5)+60000*2060.

Adding the two range bounds, which is weaker than orthogonal square-sum aggregation but sufficient, yields

    ||RF||<2.65e17+1.03e10+1.5e12+1.236e8
              <2.66e17.                             (9)

Every235-head output coordinate has been restored. The result is a bound on the action on this forced column, not on arbitrary unit vectors, so it does not replace the preceding full inverse theorem.

## 5. Exact energy derivative and complete closed tails

The assembled matching equation is

    M(E)F(E)=V_endpoint,
    M(E)=E I-H_finite+j V_o Q_slow(E)V_o^T.

All finite physical matrices and coordinate inclusions are energy independent. Thus its exact derivative is

    F'=-R F-j R V_o Q_slow' V_o^T F.                  (10)

Equation(10) includes the derivatives of every buffer/cable propagation power and feedback denominator used to describe the same inverse. No value bound is promoted to a derivative bound; no factor Qn^m is differentiated as a constant. The assembled equation avoids having to estimate large product-rule terms before their exact cancellations.

The already checked actual output-port column obeys ||R V_o||<5e6. The slow-root derivative is<1/(1.99g) on the full channel space, and ||V_o^T F||<2060. Equations(9)–(10) therefore give

    ||F'||<2.66e17+(5e6)*[j/(1.99g)]*2060
                 <2.66e17+1.56e7/g.                  (11)

The derivative of the complete geometric closed-tail lift costs its checked multiplier1.00068 and additive3600, proving(1). The closed projectors are fixed B projectors on each physical window, so no projection derivative is missing. Boundary analyticity and the actual finite inverse justify all derivatives through the closed window endpoints for each fixed positive triple. The parameter g=0 is excluded and no uniform complex strip is asserted.

At g=1e-6, the exact ceiling in(1) is below2.67e17. Lower-lip fixed conjugation supplies the same estimate. Orthogonal parity and record sectors preserve the norm bound; the two physical windows remain distinct when this derivative is later integrated. Passive-reference tensoring leaves all operator norms unchanged.

## What this does and does not settle

The proof improves the direct finite-background term from4.68e18 to2.66e17 while retaining the separately bounded slow-surface derivative and every closed tail. It does not meet a preferred1e17 ceiling and does not claim that such a ceiling is false. The remaining large loss is already visible in(5)–(7): the original converter-loaded full kernel3e10 acts on the original source recovery, and the input-deletion row is estimated by norms rather than exploiting further correlation with F. Improving either action would need another exact identity or source calculation, not a derivative inferred from small scattering error.

A temporal consequence must insert this derivative into the independently checked onset integral with both hard-cutoff boundary terms, both lips, full emitter and background components, and the single omitted-state charge. Actual incoming/outgoing and normalization estimates remain separate. No incoming-late source is imported here, no time window or output length is selected, and no new actual success/runtime theorem is claimed. This coherent action estimate stops before those separate synthesis choices.

Distinct checking is required for the actual-coordinate bounds(2), disjoint-boundary lift norm(4), row-action use of the zero-extended F in(6)–(7), and restored full action(8)–(11). The previous inverse and derivative checks do not independently check this new composition of their inequalities. No publication, audit or retained status is asserted.

## Exact dependencies

- `slow_lead_forced_derivative_sharp/PROPOSAL.md`: `662b64aa1d7714746abaa585f8e1af17ece308771b5c9de25f88fde03bb787c0`.
- `slow_lead_forced_derivative_sharp_check/REVIEW.md`: `41f8ad9e18d7c1910f8a2c9b7cc70a2cb6b5a89ecbad47d52fd555b694718d4d`.
- `slow_lead_uniform_composition/PROPOSAL.md`: `8cd26edcb7941d8254494480455d17c137652ec779e37e78901de5a04e71ac9e`.
- `slow_lead_uniform_composition_check/REVIEW.md`: `b873ac37d8a327f27491f36e80dfe5e8aeef7eb0d7b405bba6b70a6ffb9e71a7`.
- `slow_lead_recovery/PROPOSAL.md`: `f0f39510b65133d8399720c53ce2822bfe60a378ab2e50e1773a3dc8d0fe880f`.
- `slow_lead_recovery_check/REVIEW.md`: `488d0a9e8871f77f40d44803ee9bfe7fda25388c66b367944eea3376f51f5195`.
- `record_attached_recovery_sharp/PROPOSAL.md`: `07320d9a2e7c4db6c7479be0c59064749dcd73209d0847db8327b1963465ef11`.
- `record_attached_recovery_sharp_check/REVIEW.md`: `cbd5dfd29fbe67ad36c3ffc97a896f55ea30b8a5af367930c48a080589523430`.
- `slow_lead_complete_onset_frontier/PROPOSAL.md`: `c590e093e7a4ca6abc1e147414f5ee5b08e725fa1a881b266fae7271b56e0d46`.
- `slow_lead_complete_onset_frontier_check/REVIEW.md`: `5f8b8a3b4aea4008c07d9d8e59b53a7c58bf4cb0deead4d7da66be84a2c4a32b`.

Original source/calibration and converter/gate pins are those explicitly preserved in the controlling sharp derivative source. They are reused within their checked scope, not newly re-audited. Hashes record source identity only.
