Original independent report SHA-256: 53bada1997eb42f3452f7b7aeb2274b565aa6660fa37615ae06e457da9794a22.

This display copy differs only by this prefix and removal of blank lines at EOF.
The exact reviewed bytes are recoverable from OPTICAL_IMMUTABLE_EOF_v1.json
at the campaign root; the original remains unchanged locally.

# Independent check of the nonconformal source/optics/radiation link

**Disposition: supported within the corrected formal point-action scope.** One material premise gap was found and corrected by the parent: constant self contributions alone do not eliminate a body-charge dipole. The main result now explicitly discards self terms and assumes zero residual body-dependent active/passive sensitivities. The new sensitivity diagnostic correctly displays the otherwise missing dipole channel. Two narrower reporting/scope clarifications were also completed. No material correction remains open for the claims actually made.

This was a focused independent proof/numerical check of parent-authored work. It was not a formal audit, empirical exclusion, retained-grade decision or authorization to land changes. I edited only this independent_review directory. The parent made the source corrections and authored the sensitivity extension. The fixed campaign deadline remains 2026-10-13T16:53Z.

## Scope and identities

I read the full original protocol, metric/radiation note, proof-details note, runner, freeze/results and both scope files, then the complete affected source changes, body-charge note/runner/results and correction receipts. All original result rows were consumed. The original, post-premise and final current source files are separately preserved in source_snapshot, source_snapshot_v2 and source_snapshot_final. No parent runner was imported or executed by the reviewer.

Final principal identities:

| File | SHA-256 |
|---|---|
| DIRECT_METRIC_RADIATION_LINK.md | 3a44d099c294d4dfdfaa5dffc93cc7753ad26207c7656889073bd3eaeef21864 |
| PROTOCOL.md | 76b02971daeafbf54a217117943cc13187b416ceb420851426412f81efef1ccb |
| check_metric_radiation_link.py | d0eff4bc05e94551edda0d705536a78f4ac9ea27128078200d9540a0346102bf |
| evidence_v1/RESULTS_v2.json | 17474478b7c9d75d28ab2f960b7f4660a29c0577b1d6932acf6fc425c4af9e54 |
| RESULTS_AND_PROOF_DETAILS.md | d5dfa01e238581f30dde151590b6063fb96a0c1435efdcf25760f66fd85e204d |
| BODY_CHARGE_SENSITIVITY.md | 5b288c1191760484c86f505359eab8495ace5f0dc470a99fef9a34cfc181e561 |
| check_body_charge.py | f7afdaa8df818a5a0ed10b66bc4e499b1a7632d0e0f3fa4b08c6b918389626b2 |

The original executed note was a0b03a06787b5179cd807e25ef416fe191d79750b279bd5f7fc73ee1cb8a363f, followed by the isolated accidental-plus-sign correction to c4b7fa0962eccb8023382350e13d2af174f34a3f49ab6685790b00d5e8d98db5. Both exact versions survive. The original runner was 2fc082abcbbf0004cfee2a6bfd6bfc212779a2d56f5f6a83bfef5c45b73cee2f. Its only later change is the returned scope string. Removing created_at, source_sha256 and scope from the old/new result objects leaves identical scientific content.

BODY_CHARGE_RESULTS.json binds the pre-reporting-clarification body note a4aa57fa77c4e274b56cdeff40714d18ef552aba2affc4afcec71248ab3ad742. That exact note is preserved; REPORTING_SCOPE_CORRECTION.json binds it to the final note above. No stale result identity was silently replaced. The originally frozen protocol is preserved as historical input rather than rewritten after evaluation. Complete identities, recovery paths and check dispositions are in REVIEW_RECEIPT.json.

## Findings and their disposition

**R1 — missing self-charge premise, resolved.** A constant extra source charge need not have a constant dipole. In the Newtonian inertial centre of mass, constant residual active charges q_a=m_a(1+eta_a) give

    D_self = m_red (eta1-eta2) r.

Unless the charge/mass contrast vanishes or has a sufficient order hierarchy, D_self'' radiates. “Weak self gravity” alone gives neither guarantee. The original wording therefore did not justify applying the no-dipole leading law to generic weak composite bodies. The parent now explicitly supplies the narrower self-term-discarded point action with zero residual active/passive body sensitivities at the retained order, removes the residual constant-self term from Q, and updates the claim and scope statements. This discharges R1 for that formal model; it does not prove an extended-body limit.

**R2 — error normalization, resolved.** The main runner's field named relative_error is |R_direct-R_formula|/max(1,|R_formula|). Its maximum 5.329070518200751e-15 is a scaled error, not a strict fractional error for R<1. The corresponding strict fractional maximum, computed as |difference|/|reference|, is 3.16092859346533e-14. The prose now defines the normalization and supplies a conservative 3.17e-14 fractional bound. No numerical gate or result changed.

**R3 — dipole channel versus total charged flux, clarified.** The new dipole is an additive odd-angular contribution. Nonzero residual charges can also change even multipoles, and a physical body theory can change the conservative orbit. The final body note explicitly prevents treating its R_dipole as the complete change in total flux. This preserves the useful sensitivity calculation without completing a body model that was not supplied.

## Exact matter, field and Maxwell variation

The N=D restriction is a consistent sector of the stated homogeneous vector action when e is fixed, u=e phi, and orthogonal free modes are set to zero. Factoring its normalization gives G_N=GN and c_s^-2=alpha N. This is a restriction, not a result about the earlier anisotropic q calibration.

For A=exp(psi), B=exp(-lambda psi), z=(B/A)^2 v²/c², the complete three-component variation gives

    p = m (B²/A) gamma_z v,
    H = sqrt(m²c⁴ A² + c²(A/B)² |p|²),
    -partial L/partial phi = m A gamma_z (1+lambda z).

The canonical identity partial H/partial phi at fixed p equals the same source. Hence the particle's explicit time-dependent Hamiltonian work cancels the field source work, with the usual boundary flux retained. H is nonnegative for positive m and timelike configurations. The field quadratic energy is positive in the stated sector. These are finite-energy algebraic properties, not a definition of singular point self energies or a proof of stable global evolution. The formal self-term removal used for the orbit must not be confused with such a regularization theorem.

At lambda=-1, the source reduces to mA/gamma_z and the metric reduces to the previously checked conformal limit. The sufficient positivity assertion for lambda>=0 is correct; the note does not incorrectly claim that this is the largest possible positivity range.

The metric determinant and inverse give

    L_em = (n E² - B_em²/n)/2,
    Pi = n E,
    H_em = (Pi²+B_em²)/(2n),
    n = B/A.

Both -partial L_em/partial phi at fixed E,B_em and partial H_em/partial phi at fixed Pi,B_em equal (1+lambda)H_em/c². This verifies the source/energy link and includes the conformal zero-source limit. H_em remains positive because n>0. The supplied gravitational field action has no corresponding metric dependence; adding a gravitational-field-energy source would change the model rather than repair an algebraic omission. That absence remains a physical limitation for strong-equivalence/general-covariance claims, which the note does not make. The orbital calculation explicitly has no electromagnetic field.

## Static optics checked by a different route

Fermat angular-momentum conservation for the static index exp(a/r), with the impact parameter defined at infinity, gives

    (du/dtheta)² = exp(2 epsilon u)-u²,
    epsilon=a/b, u=b/r.

Instead of the author's turning-point substitution, I differentiated this to an initial-value equation,

    u''+u = epsilon exp(2 epsilon u),
    u(0)=0, u'(0)=1.

Expand u=sin(theta)+epsilon u1+epsilon² u2. With zero higher-order initial data,

    u1=1-cos(theta),
    u2=sin(theta)-theta cos(theta).

The next outward zero is theta=pi+2epsilon+pi epsilon²+O(epsilon³). This independently proves the candidate coefficients 2 and pi in a/b, hence 2(1+lambda)m_g/b and pi(1+lambda)²m_g²/b².

For the separate Schwarzschild comparator in areal radius, the ray equation is u''+u=3 delta u². Its first correction is 3/2+cos(2theta)/2-2cos(theta), with value 4 at pi and zero derivative there. The second correction at pi is the elementary Green integral of 6 sin²(theta) times that first correction, equal to 15pi/4. Thus the comparison uses the same asymptotic b, without identifying the two closest-approach radii.

Independent initial-value integrations of these two ray equations reproduce all eight stored bending angles within **4.3021142204224816e-16 radians**. The largest drift of the corresponding first integral is **2.6645352591003757e-15**. No turning-point root or author quadrature was reused. These numerical controls are not interval certificates or new proofs of a finite-error cubic remainder. The parent correctly treats the reported cubic values as diagnostics.

The weak exterior metric has static PPN-shaped gamma=lambda and beta=1 with the usual positive U=-phi convention. This is not a full many-body PPN calculation. At lambda=1 the second bending coefficient is 4pi rather than the supplied Schwarzschild 15pi/4. The impact-parameter distinction and comparator coefficient also agree with the primary derivation in [Gibbons and Vyska, sections 2 and 2.3](https://arxiv.org/html/1110.6508v2). No solar second-order observation was fitted.

## Weak source ordering and radiation interference

I expanded the action before differentiating, independently of the author's direct exact-source series. Through the relevant weak order,

    L = -mc² + m v²/2 - m phi
        + m/c² [v⁴/8 -(lambda+1/2)phi v² -phi²/2] + ... .

Its variation yields m[1+phi/c²+(lambda+1/2)v²/c²]. After discarding self terms as the corrected premise requires, the Newtonian companion potentials satisfy sum m phi=2U. Therefore

    Q=M+[2U+(2lambda+1)T]/c²,
    Q_dot=(1-2lambda)U_dot/c².

The factor 2 multiplying U is required: each companion interaction appears in the source sum. It does not change the conservative Newtonian energy to T+2U. The field energy supplies the complementary contribution; the orbital energy at that order is T+U, whose conservation justifies the derivative relation. No missing factor of two remains.

Retarded multipole expansion of the scalar wave equation gives the radiation time-derivative amplitude

    Q_dot + n.D''/c_s + n_i n_j I_ij'''/(2c_s²) + ... .

The leading mass dipole has D''=0 in the Newtonian centre-of-mass calculation. Under the corrected zero-residual-sensitivity premise, its source/trajectory corrections are suppressed by additional slow-motion factors. The sphere average of the displayed monopole/quadrupole terms is

    P=(G_N/c_s){[Q_dot+Tr(I''')/(6c_s²)]²
                  + I_STF''':I_STF'''/(30c_s⁴)}.

The coefficient 1/30 follows from the fourth angular moment, and the source-monopole/trace cross term is essential. The independent controls retain it before squaring. For example, at e=.6, s=1, lambda=-1 the checked ratio is 0.26830073739092597; discarding this cross term gives 0.29688531978212396. At lambda=1 the interference has the opposite sign. A sum of separate monopole and trace powers is not the stated theory.

For the Newtonian pair, Tr(I'')=4T+2U and Tr(I''')=-2U_dot. Consequently

    K_dot=[(1-2lambda)/c²-1/(3c_s²)]U_dot,

as claimed.

The approximation is asymptotic at fixed finite lambda and positive s with v/c, v/c_s and external potential/c² small. It is not a uniform statement for arbitrary large lambda, arbitrary c_s or e approaching one at fixed orbital scale. The controls remain weak/slow through e=.8.

Within that formal sector, no additional term at the displayed leading radiative order was identified. Post-Newtonian orbit changes in I, higher-order corrections in Q, companion-potential retardation corrections, radiation reaction, and higher source multipoles enter at later weak/slow order. In particular the first near-zone retardation term from the conserved leading rest-mass charge is proportional to its vanishing time derivative; the next potential correction does not alter Q at the retained order. Corrections to the dipole are higher-order only after R1's body-charge premise is imposed. Arbitrary preferred-frame motion, body stresses/sensitivities and internal dynamics are not derived. A pulsar timing model or inference of masses would also require conservative relativistic dynamics; the same-orbit comparison does not supply those.

## Eccentric averages without importing the GR enhancement

I used true anomaly f and h²=k a(1-e²), with

    r=a(1-e²)/(1+e cos f),
    v_r=(k/h)e sin f,
    v_t=(k/h)(1+e cos f),
    dt/period = Omega r² df/(2pi h).

Differentiating the moment in the instantaneous radial/tangential frame gives

    I''' = (m_red k/r²)
           [-2 v_r e_r e_r^T
            -4 v_t(e_r e_t^T+e_t e_r^T)].

Its trace and trace-free norm independently yield the author's identities. The time averages then reduce to two elementary, uniform true-anomaly polynomial means:

    <sin² f(1+e cos f)²>_f = 1/2+e²/8,
    <(1+e cos f)²[e²sin² f+12(1+e cos f)²]>_f
      =12+73e²/2+37e⁴/8.

These give exactly the displayed U_dot² average and 32 m_red² a⁴ Omega⁶ f(e) for the trace-free third moment. The numerical enhancement is derived from the candidate's Kepler geometry; it is not assumed because it occurs in the GR comparator.

Dividing by the explicitly supplied same-orbit G_N/(5c⁵) comparison gives

    R=s^-5[1/6+(5/256)((1-2lambda)s²-1/3)²
                         e²(4+e²)/F],
    F=1+73e²/24+37e⁴/96.

Circular matching fixes s=6^(-1/5). At lambda=1, the square is (s²+1/3)² and cannot vanish for positive real s, so the ratio exceeds one for every 0<e<1 within the formal leading-order domain. Cancellation instead requires lambda=(1-1/(3s²))/2, or **0.1587212481534634** at the circular speed. The eccentric ratios at lambda=1 and the cancellation rows check. This is a conflict between two illustrative calibrations within the selected family, not a data exclusion.

For numerical independence I used a uniform 128-point true-anomaly rule, the radial-frame tensor above, and a 14-direction sphere rule: each of the six coordinate-axis directions has weight 1/15, each of the eight cube vertices has weight 3/40. This rule reproduces the quadratic and quartic sphere moments and is exact for the angular polynomial being squared. It differs from the author's eccentric-anomaly Gauss rule and latitude/azimuth quadrature.

All **36 frozen rows plus 8 calibration/cancellation rows** were checked. The maximum reviewer-versus-author scaled difference is **5.440092820663267e-15**; the strict fractional maximum is **3.181061896608522e-14**. Reviewer quadrature versus the closed formula has strict fractional maximum **8.881784197001252e-16**. Complete component powers, including interference, are preserved. No synthetic control was dropped.

## Body-charge extension and its boundary

For the supplied residual active charges, the odd angular amplitude n.D_self''/c_s has zero sphere cross term with the even monopole and quadrupole amplitudes. Its contribution is

    P_dipole=G_N |D_self''|²/(3c_s³).

The true-anomaly acceleration average gives

    <|r''|²>=a² Omega⁴ (1+e²/2)/(1-e²)^(5/2),

hence the parent's averaged dipole power and GR-normalized 5/96 coefficient follow. The circular ratio to the candidate's scalar quadrupole is (5/16)(delta_eta)²(c_s/v_orb)². The stated sufficient parametric hierarchy |delta_eta| much smaller than v_orb/c_s is therefore correct.

My independently evaluated dipole controls used delta_eta=1e-4 before the parent extension was read. Their exact quadratic rescaling to the parent's 1e-3 reproduces all four added rows within **7.78e-16 fractional power error**. The illustrative circular GR-normalized contribution is **0.15261229435330845**. This is not a measured sensitivity.

As now stated explicitly, this is only the odd-angular contribution on a supplied Kepler orbit. Nonzero eta also affects even source moments, and a consistent passive/body theory can alter the orbit. The diagnostic neither repairs the real-body gap nor supplies a complete charge-corrected total flux. The zero-sensitivity main law remains a useful explicit conditional construction.

## Evidence, failure history and remaining claims

The original numerical execution succeeded. Its note contained one accidental plus sign between prose lines; the exact executed bytes, source hash and isolated correction survive. The reviewer then identified R1 as a physical premise gap, not a failed numerical assertion. The parent preserved that original note, runner, scope certificate, result and proof-details note; narrowed the premise; and reran the scope-updated main runner. Its scientific result fields are unchanged. The new body diagnostic succeeded separately. The later error-label and dipole-scope edits changed no formula or runner and retain their exact predecessors and replacement receipts.

The reviewer primary execution and affected-source confirmation both exited successfully with empty stderr. No reviewer failed or discarded run occurred. Independent code, raw output, source snapshots, differences, normalization receipt and numerical evidence are retained here. The floating-point comparisons are not rigorous interval bounds.

The source and numerical claims are self-contained apart from declared standard numerical/symbolic libraries. The supplied field, particle and Maxwell actions are new candidate premises. The classic metric/optical geometry is not claimed as new physics. The prior exposed solar-bending context is development motivation; no data were fitted or held out and no GR posterior or uncertainty was transferred. That distinction remains consistent with the corrected VLBA-analysis context already checked in the [primary Fomalont et al. paper](https://arxiv.org/html/0904.3992v1).

The corrected conditional-support, frontier_discovery, partially_closes and proposal_allowed:false scope is appropriate. No full PPN theory, anisotropic-q inheritance, tensor radiation, compact-star prediction, body regularization, strong-field existence, actual timing likelihood or common empirical parameter fit has been established. The N1–N8 statement is a narrow algebraic obstruction within a defined family, not a framework route-exhaustion claim. These open sectors are not discharged by the successful synthetic controls.
