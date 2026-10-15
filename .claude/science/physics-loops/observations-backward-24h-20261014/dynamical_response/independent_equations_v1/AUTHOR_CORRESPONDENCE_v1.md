# M14 focused equation correspondence after independent freeze

This is a source comparison of the two complete working arguments, not a formal audit, canonical-source review, numerical-forward validation or publication approval. Root remains scientific author. The independent derivation and controls were frozen before either new M14 author note was opened. No root production code, forward trajectory, new observation, survey likelihood or empirical error budget was read or run in this check.

The complete independently frozen derivation is `INDEPENDENT_EQUATIONS_v1.md` (SHA256 `bd47f06d14a097d4efcc1ee16342337bd62f0da73088391b626588c0c8fcd863`). Its 30 exact controls passed. Those controls include independently derived wave-operator metric slots, background and constraint propagation, conformal maps, momentum inversion, turning/rank counterexamples and radial kinetic normalization. Deliberately dropping either the number-contrast b-squared mass or the matter-dependent lapse source gives a nonzero constraint-propagation residual. These are independent controls, not author aggregate counts.

## Read scope and exact sources

After that freeze I copied and completely read:

- `dynamical_response/WORKING_v1.md`, 5,859 bytes, SHA256 `637fdbfbead8d4566bf0e99e046a26cae28123b73f88f60d4e768ee5584cdff1`.
- `dynamical_response/EXTENSION_v1.md`, 5,877 bytes, SHA256 `1e1dadc5a38f5b6ac0a2e2fd778d360d1246f49c668cd054c88ca53705a3dc57`.
- The complete prior `docs/EXPONENTIAL_SCALAR_FINITE_MODE_INVERSE_BOUNDED_THEOREM_NOTE_2026-10-14.md`, 8,764 bytes, SHA256 `d816996a38b6ca65feef503578372058d6d67561fd4c36318f476ca6ba22ee64`, specifically to resolve the potential-label question without presuming a metric convention.

The M12 supplied action was previously reviewed in full and was separately copied before the new M14 exposure. Its current action, kinetic metric and transverse-equation sections were reread here: SHA256 `dde833e8bcb69f4ab5e03eb911aa534dbf23647d5fb03cd1be469bac2e977122`. This is a supplied candidate, not a newly derived action. Immutable snapshots and individual identities are in this directory. This report does not claim a check of source versions written after these snapshots.

## 1. Full equations and constraint propagation

Use b=d ln A/dchi, Einstein proper time, canonical background velocity s, canonical perturbation X and its derivative Z. My independent pi,sigma,p are the author's s,X,Z. The author's n is necessarily the contrast of the Einstein proper rest-frame number density: delta rho/rho=n+bX. A coordinate-volume number contrast would instead be n-3phi and would obey a different continuity/source representation.

With that dictionary every displayed background and five-component perturbation equation matches the independent derivation. In particular:

    2Q(phi_dot+Hphi)=sX-rho v;
    n_dot=p_wave^2 v+3phi_dot;
    v_dot=-phi-bX-bs v.

The scalar source is equivalent to

    Z_dot=-3HZ-[p_wave^2+V_chichi+rho(b_chi+b^2)]X
          +4s phi_dot-2(V_chi+b rho)phi-b rho n.

The b-squared term and the -2b rho phi source are both present in the author form. Their signs follow from the explicitly supplied action and number-density convention. The matter stress trace does not acquire an extra lapse perturbation. The lapse term arises from delta(box chi) and the rolling background scalar equation.

The undivided 00 residual C agrees exactly. Independently differentiating it using these evolution equations yields C_dot=-3H C, with no quasistatic approximation. The spatial trace equation follows identically from the momentum evolution, background equations and Euler equation. Thus the initial gravitational constraint is propagated rather than being repeatedly imposed to remove a scalar degree of freedom. X and Z remain independently free, with n available to solve the initial constraint when rho>0. The unsafe divisor 2Q p_wave^2-s^2 is not required.

The working note describes propagation as a check but does not yet print C_dot=-3HC; my independent proof supplies that identity for later exposition. I have not rerun the author's reported forward controls or direct Christoffel calculation, and do not use their reported counts as independent evidence.

## 2. Physical frame and normalized momentum inverse

The map Psi_J=phi+bX, Phi_J=phi-bX is correct for the explicit time and spatial metric slots. v_J=A v, delta_J=n-3bX, dt_J=A dt, rho_J=rho/A^4 and H_J=(H+bs)/A give

    v_J,tJ=-Psi_J,
    delta_J'=K^2 v_J/H_J+3Phi_J'.

Differentiating W=K^2 v_J/H_J at fixed comoving wave number gives W'+(2+h)W=-K^2 Psi_J/H_J^2. The expansion chart H_J>0, k_com>0 and A>0 are substantive domains. The normalized quantities additionally require nonzero W and S=Phi_J+Psi_J when r or S'/S is used. At their zeros the unnormalized metric/velocity equations remain the appropriate objects; finite ratios cannot be invented.

Let x=F'/F and y=x/q, with q=2Qb^2>0. My independently derived relation in Jordan time was

    phi_tJ+H_J phi=lambda phi+(lambda/q)(Psi_J-phi)-Gamma v_J,
    lambda=(ln A)_tJ, Gamma=rho_J/(2F).

Using lambda=-H_J x/2 and S=2phi gives exactly the author's displayed momentum equation. The identity P W=-a_J^3 K^2 S/(3H0^2) then yields M=P'+P P3=P(1+S'/S), and hence

    R=M+P x/2+P r y/2,
    R=rho_J a_J^3/(3H0^2 F).

The velocity-column sign and factors of two agree. This replacement of a quasistatic input relation retains arbitrary coupled-scalar waves in the readouts. It neither predicts their state nor establishes a calibrated survey map.

The three-row inverse solves the same finite-dimensional problem as my [phi,bX,-v_J] inverse after nonsingular row/column rescalings. For real mode components, rank three determines R,x,y, and nonzero y with positive x/y identifies q. A fourth equation is a necessary no-refit consistency test, not a proof of all field equations or an independent empirical test when generated synthetically.

A small domain clarification was sent to root: write explicitly that the rows are calibrated real mode components, or require a common real recovered coefficient vector when using complex Fourier coefficients. The algebra extends to complex rows, but physical positive R and q require that reality condition. Unknown constant common amplitude for each mode cancels from the normalized readouts; independent channel gains and time-dependent normalizations do not.

## 3. Rank availability and exact degeneracies

The extension's factor c is correct:

    c=2 A a_E^3(H+bs)/(3H0^2),
    P=-c phi/v, P r=-c bX/v.

Consequently det L=c^2 b det[v,phi,X]/(4 v1 v2 v3). Under b!=0, each v_i!=0 and the stated regular expanding chart, rank three is available in the conditional solution space. Pick three small independent rows, choose Z freely, and solve the initial 00 equation for n because rho>0. The full smooth linear initial-value equations then give local solutions. A common scaling keeps perturbations small over a fixed regular finite interval. This establishes existence, not a realistic or observed mode preparation, and does not assert a uniform lower bound on conditioning.

The counterexamples in the extension are necessary and correctly scoped. Proportional rows fail. Three different wave numbers need not supply three different transfer shapes. At b=0, q=0 and division by b is unavailable, even if the canonical scalar rolls and carries momentum. At s=0 with b!=0, x=y=0 and momentum fixes no instantaneous q even if the readout matrix is invertible. A nearby limiting inference would use additional time information, not the instantaneous ratio. Small y or nearly singular L makes the inference fragile. Turning points do not make the original canonical equations singular, although a reconstructed F-coordinate chart may fail there.

## 4. Conditional finite-error envelope

The product-error inequality for P r is valid:

    |Pr-Phat*rhat| <= |Phat| e_r+|rhat| e_P+e_P e_r.

Thus the proposed d bounds the induced infinity norm of L-Lhat. For eta=||Lhat^-1|| d<1, the inverse perturbation bound applies to the true L. The exact error equation is

    L(z-zhat)=(M-Mhat)-(L-Lhat)zhat.

It gives the stated epsilon. If |yhat|>epsilon, expanding x/y-xhat/yhat gives the displayed ratio error epsilon(1+|qhat|)/(|yhat|-epsilon). The positivity certificates are sufficient when the true and fitted physical coefficients are real. Failed sufficient conditions remain inconclusive.

No probability coverage follows without statistical assumptions, and no absolute envelopes are supplied by this derivation. Calibration, derivatives, shared clocks, windows and numerical errors must be included in any actual envelope. The extension states those limits. A rational fixture in my post-exposure controls checks the error orientation and both matrix and ratio enclosures; it is not an empirical uncertainty model.

## 5. Background and adopted-family reconstruction

R'/R=-x is equivalent to the independent Gamma consistency equation Gamma_tJ/Gamma=2lambda-3H_J. Thus the inferred coefficients supply relative F, conditional on conserved Jordan dust. They do not fix F separately from the unknown dust normalization.

Transforming the independent potential-free background equation

    H_J,tJ-lambda_tJ+lambda H_J+Gamma+lambda^2(1/q-1)=0

to N gives equation (3) in the extension with omega=(1/q-3)/2. Transforming the canonical Friedmann equation gives equation (4), including its sign and factor of one-half in the kinetic term. These identities are necessary background checks; observing an instantaneous momentum inverse does not guarantee them.

For the adopted radial candidate the relation q/beta+R(1-3q)kappa=1 is algebraically equivalent to q=beta(F-Fc)/(F-3beta Fc). Its two-row determinant is exactly (q1-q2)/kappa. Therefore varying q identifies the two constants within this assumed chart, with the stated positive and interval gates. Constant q leaves an underdetermined pair. Sampled membership checks do not prove an interval identity.

The displayed branch inversion k=[1-2sqrt(1-3beta)]/3, exponential-u formula and potential normalization all agree with the supplied M12 family. In particular V_J/(F H0^2)=2(Hv/H0)^2 U/C, so equation (5) follows. The second linear solve requires independent U0,U1 rows, gamma>0 and nu>0. The small-u ill-conditioning warning is substantive; no chosen high precision can become observed precision. This is reconstruction and testing within an adopted family, not a selector for the action or an explanation of scales.

## 6. Transverse modes and prior labels

For the supplied radial background, K_uu is independent of x,y, K has no cross terms, A depends only on u and U_x=U_y=0 at x=y=0. Arbitrary transverse linear perturbations therefore produce no first-order scalar energy/momentum, matter coupling or radial source. This is genuine linear decoupling, not a zero-amplitude rule. Their own linear equations retain free initial data. Quadratic backreaction, nonradial backgrounds and nonsymmetric extensions remain outside the one-field block. No stability theorem follows solely from positive transverse potential curvature after a time-dependent canonical rescaling.

I read the complete earlier finite-mode note rather than inferring its convention from familiar symbols. It writes Phi_J=Phi(1+k y), Psi_J=Phi(1-k y) and their ratio, but nowhere assigns those labels to g00 and gij. Those displayed formulas are compatible with Phi_J naming the time slot and Psi_J the spatial slot. Therefore the symbol difference does not prove a physical sign error. No older source was modified, and no earlier inverse calculation was independently rerun here. The present explicit metric-slot dictionary removes the ambiguity for this new result.

## 7. Controls, failures and conclusion within scope

The independent pre-exposure script has 30 passing exact checks. A separate post-exposure script has 14 passing controls for the normalized momentum relation, determinant factor, frame/background conversion, candidate identities and rational error enclosure. Those 14 are source-correspondence checks and must not be described as independent of exposure to the author argument.

The first post-exposure run failed while counting SymPy BooleanAtom values, before writing a result. Its immutable source and a precise setup-failure record are preserved. Version 2 converts each pass flag to a Python bool before counting/serialization; no mathematical expression, fixture or threshold was changed. Version 2 exits zero, 14/14 passing. This is a checker setup failure, not a failed scalar candidate.

No substantive equation, sign, factor, rank or finite-error defect was found in the frozen two-note scope. The two prose/domain clarifications above were sent to root. Canonical source, implementation correspondence, numerical integration, calibration, current cache and publication bindings remain separate work. No formal verdict or universal no-go is asserted.
