# CKM compound magnitudes and circumradius: conditional bridge

**Type:** bounded_theorem
**Review scope:** conditional supplied algebra and the specifically reviewed comparisons;
physical interpretation, inherited authority checks, and audit status are not certified.

Date: 2026-04-25; source correction reviewed 2026-10-21.
This note gives exact algebra for supplied model formulas. It does not confer
retained status or establish a physical CKM prediction. The earlier companion
classified `proposed_retained` by the substring `retained`; that authority
inference is withdrawn. No ledger or audit verdict is modified.

Primary companion: `scripts/frontier_ckm_compound_magnitudes_circumradius_bridge.py`.

## Supplied premises and scope

For positive a=alpha_s, supply N_pair=2,N_color=3,N_quark=6 and

    lambda²=a/2, A²=2/3, rho=1/6, eta=sqrt(5)/6,
    rho_bar=(4-a)/24, eta_bar=sqrt(5)(4-a)/24,
    R_bar²=(80+a²)/320,
    U=|V_us|²=a/2, C=|V_cb|²=a²/6,
    B=|V_ub|²=A²lambda^6(rho²+eta²)=a³/72,
    T=|V_td|²=A²lambda^6[(1-rho_bar)²+eta_bar²]
      =a³(80+a²)/1152.

For the nondegenerate upper-half-plane triangle interpretation use 0<a<4;
the algebraic identities below extend to positive a with these definitions.
The magnitude prescription is hybrid: Vub uses unbarred leading inputs while
Vtd uses the barred apex. Exact equality of these supplied formulas is not an
exact all-orders CKM parameterization or a proof that the approximations share
a controlled truncation error. Their physical realization and coupling-scheme
matching remain separate obligations.

The radius formula follows for the supplied triangle(0,0),(1,0),(rho_bar,eta_bar)
by R²=b²c²/(4 eta_bar²), away from a=4, where b²=rho_bar²+eta_bar²,
c²=(1-rho_bar)²+eta_bar². At a=4 the triangle degenerates; the displayed
radius expression is a limiting continuation, not a circumcircle of three
distinct noncollinear vertices.

## Exact conditional identities

C1 follows directly:

    T/(UC) = (80+a²)/96 = (10/3)R_bar²,
    3T = 10 UC R_bar².

The factors 3 and 10 equal N_color and N_pair(N_quark-1). The old extra
headline rewrite with N_pair²N_color(N_quark-1)/N_pair was incorrect and is
removed; it gave 30, not 10.

For C2,

    T/B = (80+a²)/16 = 20 R_bar²,
    U/C = 3/a,
    TU/(CB) = 60 R_bar²/a = 30 R_bar²/U.

Equivalently TU²/(CB)=30R_bar². This corrects the earlier malformed
fourth-power expression. The factors 60 and 30 equal N_pair²N_color(N_quark-1)
and N_pairN_color(N_quark-1) at the supplied counts. Varying arbitrary inputs
need not break both equations; no universal rigidity or count selector follows.

## Historical numerical diagnostics

The companion uses a=.103 (rounded, not an imported canonical module) and
historical central magnitudes U^.5=.2243,C^.5=.0410,B^.5=.00382,T^.5=.00861.
It separately computes the C1 model identity to absolute 1e-10. That is a
numerical algebra check, not a relative-error experimental test.

For the C1 comparison the right side mixes historical magnitudes with the
model radius. For C2 it compares a model compound ratio to the historical
compound ratio. Both central residuals are printed. No errors, correlations,
extraction model, or theory truncation covariance are supplied; the old 5%
cutoffs are not a combined PDG uncertainty and are removed as validation
criteria. The historical inputs are not presented as a current PDG fit.

## Evidence and dependencies

The companion retains the C1/C2 symbolic predicates and numerical identity
threshold. Documentary source-presence/count-pattern checks are explicitly
separate; numerical inputs are supplied in code, not proved by text extraction.
An empty or proposed Status label cannot establish retained authority.
The original failed authority checks remain in the review packet; the current
helper no longer makes those invalid authority claims.

The following references supply model context, not retention certificates:

- [NLO barred apex](CKM_NLO_BARRED_TRIANGLE_PROTECTED_GAMMA_THEOREM_NOTE_2026-04-25.md).
- [Structural counts](CKM_MAGNITUDES_STRUCTURAL_COUNTS_THEOREM_NOTE_2026-04-25.md).
- [CP-phase inputs](CKM_CP_PHASE_STRUCTURAL_IDENTITY_THEOREM_NOTE_2026-04-24.md).
- [Circumradius formula](CKM_BARRED_CIRCUMRADIUS_EXACT_CLOSED_FORM_THEOREM_NOTE_2026-04-25.md).
- [Wolfenstein inputs](WOLFENSTEIN_LAMBDA_A_STRUCTURAL_IDENTITIES_THEOREM_NOTE_2026-04-24.md).

Run `python3 scripts/frontier_ckm_compound_magnitudes_circumradius_bridge.py`.
A green result checks the bounded supplied algebra and documentary presence;
it does not change these dependencies' scientific or audit status.
