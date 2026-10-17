# Direct prepared-core differentiation: a physical contact/filter interface

Status: bounded author derivation requiring a distinct check. The original unconverted prepared physical core has an explicit derivative estimate obtained from its 16-contact matching system and two-site filter, without using the arbitrary loaded inverse 3e10. The extension to the converter-loaded Phi_old is given as an exact differentiated interface with remaining coefficient obligations. No improved full assembled L' constant, temporal theorem or device operating point is claimed.

## Scope and conventions

Reuse the original calibrated .03<J<.031, original interval |k-k0|<=1e-6, E(k)=2J(1-cos k), E'(k)>.025, and the actual eight-dimensional B fiber in each parity sector. All derivatives until explicitly divided by E' are with respect to OLD k, not the new lead q. The projectors of B are fixed. The core O comprises 90 original arm heads plus 82 old buffer heads, with the outer planes at m=40. The real junction transformation U is constant and unitary. Both physical old-energy windows and both lips retain the same interpretation.

Let Psi_B(k) denote the original 172-coordinate physical recovery from unit TWO-port OPEN incidence at these outer old-J planes, with decaying rather than growing closed tails. The checked dwell identity gives ||Psi_B||<30. This is used only as a value estimate in a differentiated finite equation. No derivative is inferred from that value or from the first derivative of scattering alone.

The target Phi_old(E)P in prepared_core_recovery §4 is a DIFFERENT map: the two converters have already changed its incidence and closed return. A derivative estimate for Psi_B alone is not a bound for Phi_old P. Sections 3–4 specify that distinction and the outstanding terms.

## 1. Exact finite physical equations and direct differentiation

Before the filter, the physical contact matching matrix is

    M16=[[lambda-2J-B-VA, JI8],
                          [JI8, lambda-2J-B+JQ-VB]],

using -JQ^-1=lambda-2J-B+JQ. For a fixed open incoming vector its RHS is (0,iE'/z times that vector), z=exp(ik). The exact supplied real inverse is <166. The canonical proof establishes on its actual complex disks of radius1e-12, not from off-real unitarity,

    ||M16^-1||<167, ||M16'||<.1,
    ||RHS||<.063, ||RHS'||<.125.

Consequently the bare contact solution b satisfies

    ||b||<11,
    ||b'|| <=167²*.1*.063+167*.125<205.                 (1)

On free arm sites, the open solution is the incoming wave plus r_g times the outgoing wave; the closed solution is a decaying Q_C power applied to the contact coefficient. The canonical exact matching gives |r_g|=1 on the real band and |r_g'|<1000 in either stated equivalent origin convention. On the same disks |Q_C|<.15, |Q_C'|<.125, |z|,|z'|<1.001. Derivative powers are expanded as sums before norms; no Q_C^-n is introduced.

Let y(k) be the bare incoming solution restricted to the finite arm-and-buffer range and y_f its two filter coordinates. Let C(k)=G_bare(O,f) and G_f=G_bare(f,f), with f=(F,F+1), F=20. The constant filter matrix V has norm<.05. Exact resolvent recovery is

    x=(I-G_f V)^-1 y_f,
    Psi=y+C V x,
    x'=(I-G_f V)^-1[y_f'+G_f' V x],
    Psi'=y'+C' V x+C V x'.                            (2)

These are physical-coordinate columns. They retain all closed directions and the complex retarded order. In particular V is to the RIGHT of G_f; no transpose is replaced by an adjoint. The same formulas on the lower lip follow by fixed real conjugation.

The inherited filter inverse and derivative bounds are

    ||(I-G_f V)^-1||<2000, ||G_f'||<3e4.               (3)

Equation (3) comes from differentiating the actual free/image kernel and the small matching system, not from differentiating a small reflection coefficient. The dwell result supplies ||x||<30 for a unit physical open incident vector, since x is a restriction of its actual filtered recovery. Changing between the original arm origin and outer port planes multiplies the incident coefficient by unit-modulus open phases on the real band; it does not alter this value bound.

## 2. An explicit conservative derivative for the original core

For clarity a safe finite-coordinate envelope can be obtained directly, before converters. In each arm the physical interval up to the outer plane contains 86 head positions (45 arm positions and 41 buffer positions). Unfold the fixed junction U into two such arms; U and the reordering are energy independent. There is no count factor from the eight-dimensional fiber.

From (1), the open plane waves and their derivatives, and the closed decaying powers, the bare recovery obeys conservative bounds

    ||y'||<20000, ||y_f'||<4000.                       (4)

Here a per-site derivative ceiling 2000 suffices: the open contribution is bounded by 2*86+1000, and the closed part by 205+11*86*.125 on the real band. A contact coordinate uses (1) directly. Stacking at most86 sites gives <20000, and stacking the two filter sites gives <4000. This deliberately overcounts closed power derivatives by replacing their nonnegative decaying powers by one. It never estimates a formal growing incoming closed wave. The two-arm direct sum has the maximum of the arm operator norms, not their sum.

For n,m>=2 the exact bare kernel is

    G_bare(n,m)=A Q^|n-m|+Q^(n-1)T_g Q^(m-1),
    ||A||<41, ||A'||<110, ||T_g||<208, ||T_g'||<3000.

For n<=86 and m=20 or21, each physical block has norm<300 and derivative<30000. Indeed the free derivative is bounded by 110+86*1.001*41; the image derivative by 105*1.001*208+3000, giving a total below30000 at the real point. Powers are at most one there. Contact-to-filter rows are obtained from the M16 inverse block followed by Q^(m-2); their value is <167 and derivative <167²*.1+19*167*1.001<7000. Thus those rows also fit the same envelopes. The equivalent contact-coordinate indexing changes no bound.

Stacking the86-by2 blocks by a safe square-sum norm gives

    ||C||<sqrt(172)*300<4000,
    ||C'||<sqrt(172)*30000<400000.                     (5)

Together (2)–(5) give

    ||x'||<2000[4000+30000*.05*30]=9.8e7,
    ||Psi'||<20000+400000*.05*30+4000*.05*(9.8e7)
              <2e10.                                (6)

The value norm remains <30. Translating to the actual outer incoming planes differentiates the finite open incident phases. The original origin-to-outer-plane shift is at most86 steps in each arm; even paying this separately adds at most86*30<3000. The constant real U does not differentiate. Therefore safely

    ||d Psi_B/dk||<2.1e10,
    ||d Psi_B/dE||<8.4e11<1e12.                       (7)

This is a coarse derivative certificate for the original prepared finite physical map, derived without the 3e10 arbitrary inverse and without Cauchy division of a value bound by1e-12. It is not an optimal estimate. It does not include the derivative of the entire infinite closed-tail recovery, though those tails were legitimate positive contributions in the value/dwell bound. If that larger output is needed, its decaying-power derivative must be included separately.

The contact/kernel identities, coordinate count and source bounds in (1)–(7) are the explicit load-bearing obligations for distinct checking. The calculation does not certify a numerical inverse or recalibrate M16. It uses the original supplied analytic inequalities as conditional premises.

## 3. Exact converter-loaded derivative interface

Use the SAME outer old port planes. Let u(E)=a_old,P(E) be the two open incoming coefficients generated by a unit selected new-port input, and v(E)=a_old,C(E) its complementary incoming coefficient at that outer plane. These are matrices on the selected new-port input domain, not constants. With

    H_C(E)=G_old(O,B;E) A_old(E)^-1 C,

the exact physical decomposition is

    Phi_old(E)P = Psi_B(E)u(E)+H_C(E)v(E).             (8)

The already checked converter value bounds give

    ||u||<.5, ||v||<1e-44, ||H_C||<160.               (9)

They give no derivative for u or v by themselves. Differentiating (8), retaining every term, yields

    ||(Phi_old P)'||
      <= .5*1e12+30||u'||+1e-44||H_C'||+160||v'||.   (10)

Primes in (8)–(10) are PHYSICAL E derivatives. The closed term cannot simply be dropped. It is small only after the relevant differentiated physical maps have been bounded, or the complete product is bounded directly.

An implementation of the remaining calculation should use the exact converter return with its powers already combined,

    v=R_c Q_old,C^40 b_old,C,
    v'=R_c' Q_C^40 b_C
          +R_c (Q_C^40)' b_C+R_c Q_C^40 b_C'.         (11)

Since Q_C is a fixed-projector spectral function,

    (Q_C^40)'=40 Q_C^39 Q_C'.

The old source coefficient b_C itself includes the converter feedback. Differentiating it requires its exact linear matching equation and the inverse of that feedback, not merely the real small bound on b_C. No free growing closed input is estimated by its value at the wrong reference plane. Likewise H_C' must differentiate its physical G_old column and the exact A_old^-1, or (11) must be multiplied through that recovery before taking norms.

The existing converter Woodbury identity provides another equivalent starting point. If D_c is its diagonal load update, C_c=I+A_old D_c and r_c=-A_old D_c C_c^-1, then

    I+G_old(B,B)D_c
      =[I-Q_old^40 S_old Q_old^40 r_c] C_c.           (12)

Every factor in (12) has a fixed physical meaning. Its derivative includes the old scattering derivative, both40-power derivatives, r_c' and C_c'. The order in (12) cannot be changed across S_old. New-root derivatives use d/dE, with dq/dE=(2j sin q)^-1; old-root derivatives use dk/dE=(2J sin k)^-1. These chain rules are different. A bound on the derivative of an approximate open reflection alone would not establish (10) or (12).

This proposal does not assign numerical bounds to u', v' or H_C'. Their exact canceled-product evaluation, with both physical converter transmission factors, remains the precise missing step to turn (7) into an improved bound for the requested ACTUAL Phi_old P. Equations (8)–(12) expose a smaller finite matching route; they do not assert that (10) is already numerically better than the old assembled derivative.

## 4. What this changes, and what it does not

The original contact/filter portion admits direct differentiation with the supplied small inverses; it need not use the arbitrary converter-loaded inverse3e10. Equation (7) is a partial structural improvement. The requested converter-loaded prepared recovery derivative is reduced to the explicit remaining coefficient/product derivatives in (10)–(12), not closed by a value or first-scattering-derivative argument.

Even a completed Phi_old P estimate would still need the input-cap and actual wide-gate coefficient derivatives before becoming a full L' bound. In the assembled equation F'=-RF-jRV_o Q_slow'V_o^T F, the forcing RF contains all restored coordinates and wrong-window columns. Replacing it wholesale by the derivative of one prepared incoming column would be invalid. The full-fiber and closed-tail terms must remain covered.

The separate three-source D3 obligation in prepared_core_recovery §8 is also unchanged. D3 differentiates the ACTUAL resonant ordered Q3 inverse on the prepared input and is not bounded by (7), by the first derivative of scattering, or by small real source return. No source escape, IBP budget, runtime, receiver length or complete-output claim follows here. Failure to finish (10) in this bounded task is not evidence of impossibility or a lower bound on recovery derivatives.

## Exact evidence, exposure and limitations

- prepared_core_recovery/PROPOSAL.md: cce29994b7141df161ca12f377765fdaf760f7e64fc56043bbf370e2cd437ea9; complete argument read. Its checked dwell/value scope is reused through prepared_core_dwell_check/REVIEW.md, 88274b8b49e583bdb9b5f933f7406b1a96a6ca79049e57b83e8030c834d16819, and prepared_core_composition_check/REVIEW.md, 52edba6061be49eef40b5c06754a7425b5f7f62671f175cc72a093d4a60de65c, previously fully read at these identities.
- Canonical REAL_ENDPOINT_AUTONOMOUS_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md: 71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff; necessary physical matching/filter passages175–319 and analytic derivative passages1386–1518 refreshed in full. The unrelated full theorem is not independently recertified.
- slow_lead_forced_derivative_sharp/PROPOSAL.md: 662b64aa1d7714746abaa585f8e1af17ece308771b5c9de25f88fde03bb787c0; full argument refreshed for physical columns, converter order and differentiation conventions. Its previously checked scope is reused, not its narrower gate constants for a new wider-band conclusion.

I previously checked the dwell argument and several derivative/recovery ancestors and authored other scalar/source interfaces. Root requested this structural route and exposed the remaining arbitrary-inverse loss. The new direct derivative argument is author work, not an independent review of my own ancestors. The inherited M16/calibration hypotheses are supplied. No unsupported complex-domain bound is posited; the complex estimates invoked are the explicit canonical ones, and (2) is directly differentiated on the real interval.

Only this proposal was written. No numerical inverse, sweep, dynamics, solver, scientific runner, W/Git/PR/checkpoint/prompt/model change or delegation occurred. No performance point or native realization claim is selected. Distinct checking is required before (7) or this interface is used downstream.
