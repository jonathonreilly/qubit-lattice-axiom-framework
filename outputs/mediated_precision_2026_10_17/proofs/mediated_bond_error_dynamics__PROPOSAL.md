# Scalar mediator-bond errors: a complete uniform-time spectral interface

Status: new author derivation requiring a distinct check. A conditional full-output error interface is proved below without a time-times-Hamiltonian-error estimate. It compares an erroneous positive-block apparatus to the SAME prescribed nominal critical packet, with the actual global scalar phase. The explicit coarse constants are finite for a fixed admissible nominal apparatus but may grow badly as its linewidth shrinks. An O(m epsilon) complete tolerance theorem has NOT been established. The stationary product sensitivity alone does not establish that sharper conclusion.

## 1. Error model and fixed target

Fix one admissible nominal finite m of the checked mass-tuned construction, with infinite slow receiver and nominal tuple w0. Retain its background, geometry, physical input V, bandwidth rho, lambda, Z0, critical reference packet and full literal old K/W. Change only the positive scalar coefficient of each new mediator-path block P_w=w(I-X), with

    w_e=w_e0(1+e_e), |e_e|<=epsilon<1.

All new occupations remain exactly 2j; the old capped processor is unchanged. No independent occupation, block-shape or unintended-contact error is allowed. Write C(w)=sum_e w_e and H(w)=H_P(w)-C(w)I. The checked full-space identity gives

    H(w)=H_base+sum_new 2j n_v-sum_newedges w_e X_e.       (1)

Thus centered onsite coefficients and all background energy windows are unchanged. The physical answer always includes exp(-it C(w)). Relative positive errors do not change the endpoint sign gauge (-1)^m. We do not retune lambda, fit a packet to the actual device or impose the nominal critical correlations on the erroneous tuple.

Use the nominal target T0(t) of complete6ed86, including (-1)^m, c_att+2j, the exact nominal critical denominator/phase, its one physical-halfline normalization, exp(-itK)W, record1 and all nonreceiver vacua. The erroneous positive-block target is exp(-it C(w))T0(t). This is a prescribed centered nominal packet with one explicitly supplied actual scalar phase. Using the nominal scalar instead costs an additional 2|sin(t(C(w)-C(w0))/2)|; that term is not removed by the result below.

## 2. Exact finite elimination retaining every new head

Let N contain ALL 10m-1 new heads (three source endpoints and every internal mediator), excluding the retained port p. Its finite fiber includes the full inherited internal space; no selected-channel truncation is made. Work in the one-head sector and fixed real physical coordinates, uniformly in the inherited record/parity blocks. This restriction suffices for the prepared input and is invariant. Passive references are tensored by identity.

Let A_i be the compression of centered H(w_i) to N, i=0,1, retaining the shared internal operator and every negative hopping within N. Let J inject the full port fiber into the terminal new vertex adjacent to p; ||J||=1. Let w_pi be the physical bond from that vertex to p. The remaining infinite background H_bg is IDENTICAL for both tuples. Put G^lip(E)=<p|(E-H_bg)^-1|p> in the exact boundary-value sense. Since the physical cross hopping is -w_pi, the E-H block pencil is

    [[E-A_i, +w_pi J <p|],
     [+w_pi |p> J*, E-H_bg]].

Its full new-head Schur matrix and seed column are

    S_i^lip=E-A_i-w_pi^2 J G^lip J*,
    K_i^lip=(S_i^lip)^-1, u_i^lip=K_i^lip V_N,
    z_i^lip=-w_pi J* u_i^lip.                         (2)

Here V_N is the actual unit product-seed embedding, not a mass-congruent seed. The full background column is (E-H_bg)^-1|p> z_i. In particular the minus sign in z is fixed by the physical hopping convention. Equation (2) preserves the order of every full-fiber factor; G need not commute with the mediator or source matrices.

This finite elimination is equivalent to eliminating the gapped mediator interiors and then using the checked ordered source/port Schur system, but does not presuppose symmetric endpoint slopes or identical actual cells. Its advantage for a general error box is that every wrong-window forcing and every mediator output is already present.

All subsequent integrals run over the SAME two centered physical windows I_b=c_att+2j+b+[-rho,rho], b=1,3, on both lips. Take uniform bounds over both windows, lips and conserved sectors. Nominal strict loaded gates and mediator gaps imply that S_0 is invertible continuously on these compact windows. This is a finite outgoing Schur inverse, not a bounded whole-Hilbert-space resolvent on the continuum. Define finite, explicitly specified quantities

    k(E)>=||K_0^lip(E)||, u(E)>=||K_0^lip(E)V_N||,
    G_*=1/j+a0+b0 rho,
    d(E)>=||S_1^lip(E)-S_0^lip(E)||.

These can be bounded by exact finite matrix expressions or by the checked nominal elimination/reconstruction. No numerical inverse estimate is asserted here. A universal algebraic error-box choice is

    d_* = 2 epsilon w_max
                    +(2epsilon+epsilon^2) w_p0^2 G_*,             (3)

where w_max is the largest nominal new bond. Indeed the path has degree at most two, so ||A_1-A_0||<=2epsilon w_max; this bound acts as identity on the full internal fiber. The port term contributes |w_p1^2-w_p0^2|G_*. Formula (3) does not count C(w) in A_1-A_0.

Require the finite robust gate

    theta(E)=k(E)d(E)<1 uniformly.                    (4)

Then exact inverse subtraction, in the proper order, gives

    u_1-u_0=-K_1(S_1-S_0)u_0,
    ||K_1||<=k/(1-theta),
    e_N(E)=k d u/(1-theta) >=||u_1-u_0||,
    e_z(E)=w_p1 e_N+|w_p1-w_p0|u >=||z_1-z_0||.       (5)

The estimates are for the full prepared-input operator, including complementary outputs and wrong-window inputs. A maximum over lips bounds each lip; no rectangular spectral jump is replaced by entrywise imaginary part.

For uniform certification of an entire error box it suffices to set k_*=sup k, u_*=sup u, theta_*=k_*d_*<1, and use

    e_N*=k_* d_* u_* /(1-theta_*),
    e_z*=(1+epsilon)w_p0 e_N*+epsilon w_p0 u_*.        (6)

These are explicit finite sufficient conditions. They guarantee a nonzero allowed epsilon at each fixed strictly admissible nominal finite tuple. They do not guarantee a useful epsilon or a margin uniform in m.

## 3. Regularity and full physical spectral synthesis

Retain the background's complete analytic matching premise, not merely its real-axis envelope. Under (4), actual finite Schur inverses continue on local complex neighborhoods of the compact windows: use the actual nonzero real boundary determinants, continuity and a finite cover. This repeats the checked finite-m regularity argument with a different finite matrix. The actual seed measure is absolutely continuous on the windows and their endpoints; finite rectangular jumps and the background ray synthesis therefore represent the retained actual evolution. No outside spectral type is excluded.

Let L^lip be the unchanged background recovery from port forcing to its 235 finite heads and ALL closed slow tails, excluding propagating rays. Its checked full-forcing bound is L0=14000. Equation (2) gives the background difference L^lip(z_1-z_0). The two-lip jump and triangle over both physical windows give a uniform-in-time bound for every new head plus the nontraveling background:

    B_local=(2/pi) int_(-rho)^rho [e_N(delta)+L0 e_z(delta)] ddelta. (7)

The factor 2/pi accounts for two lips and two windows. Window-dependent closed/output decompositions are embedded in the fixed physical Hilbert space before triangle; they are not assumed mutually orthogonal.

The unchanged physical outgoing row has norm at most 461 before flux conversion. The checked exact conversion for port forcing is

    ||F_A||_L2(k)^2 <= (j/pi) int ||A(delta)||^2 ddelta.

It contains the true connector transmission and Jacobian; no extra inverse slow velocity is inserted. Applying it to z_1-z_0, and adding both windows by triangle, bounds ONE full outgoing discrepancy by

    B_ray=2*461 sqrt(j/pi) [int e_z(delta)^2 ddelta]^(1/2).        (8)

This deliberately conservative factor two covers full input on each window, rather than invoking selected-input orthogonality. The actual real structure gives the same incoming bound at the SAME positive physical time. Equivalently apply the same estimate to the conjugate lower-lip coefficients with their fixed physical order. It does not assert a scalar density for an operator column. Halfline restriction is a contraction for each traveling term, and both discrepancies must be charged.

Combining all spatial pieces proves, for every real t,

    ||e^(-itH(w)) E_w(I)V - e^(-itH(w0)) E_0(I)V||
       <= B_ret := B_local+2B_ray.                    (9)

Thus (9) covers all apparatus outputs and arbitrary references without a time factor. A directly evaluable coarse version is

    B_ret <= (4rho/pi)(e_N*+14000 e_z*)
                         +4*461 sqrt(2j rho/pi) e_z*. (10)

For fixed m and fixed strict nominal margins it is O(epsilon) as epsilon tends to zero. Its constant is not claimed O(m). This is a retained-window difference estimate, not yet the difference of the two full unitaries.

## 4. Actual omitted state and complete prescribed-packet bound

The nonuniform first cell still has an exact product witness. With its internal positive adjacency A_cell, endpoint bonds gamma_L,gamma_R, put

    c_L=gamma_L^2 ||A_cell^-1 C_L||^2,
    t_1=(-1)^(n1-1)gamma_L gamma_R product(q_i)/product(J_i).

The gapped bipartite identity gives Y=V-gamma_L A_cell^-1 C_L iota and (H-E_b)Y=t_1 s1 iota, up to the immaterial fixed sign. Its Gram is (1+c_L)I. The corrected cap/unchanged downstream compression is still required; no isolated preparation theorem is imported. The same two-window full-input witness yields

    o(w)=min{1, sqrt(2[1-1/sqrt(1+c_L)])
                         +sqrt(2)|t_1|/[rho sqrt(1+c_L)]}
          >=||E_w(I^c)V||.                            (11)

One must retain an actual gap for A_cell. For the error box a sufficient condition is (1-epsilon)J_m-(1+epsilon)q>0 (and the n=1 interpretation without weak bonds). The exact unequal slope sums from the precision source supply positive bounds c_min<=c_L<=c_max. Its logarithmic product bound supplies |t_1|<=|t_10|exp(tau_1), tau_1=(2n1+1)[-log(1-epsilon)]. Therefore a uniform alternative is

    o_box=min{1, sqrt(2[1-1/sqrt(1+c_max)])
                    +sqrt(2)|t_10|exp(tau_1)/[rho sqrt(1+c_min)]}. (12)

At epsilon=0 this recovers the nominal witness ceiling exactly. Do not use the old gamma_L=gamma_R slope after asymmetric errors.

Let b_0(t) denote the NOMINAL retained-window-to-target allowance in complete6ed86: its displayed complete bound with the actual nominal eps_out term removed. It includes nominal source decay/recovery, both raw errors, ideal incoming decay and the raw-to-unit mass deficit. It is nonnegative and valid wherever the nominal scalar normalization condition is certified. Keep its original lambda, Z0, phase and prescribed packet, rather than substituting actual stationary ratios.

Triangle with (9) and the single actual outside state proves

    ||e^(-it H_P(w))V-e^(-it C(w))T0(t)||
                    <= o(w)+B_ret+b_0(t),             (13)

or uniformly over the error box, replace o(w) by o_box. This is a COMPLETE time-uniform additive tolerance interface relative to the existing time-dependent nominal certificate. No extra nominal outside state is charged: the retained nominal comparison b_0 already comes from its explicit synthesis. No actual bound mass is discarded, and no claim that outside mass decays is needed. For example, if b_0(t)<=b_late for every t>=T0 by the nominal certificate, the erroneous apparatus has error<=o_box+B_ret+b_late for every such t, on the infinite receiver.

Equation (13) is not a proof of uniform small difference between full actual and nominal evolutions with an O(epsilon) ceiling tending to zero: outside spectral vectors have not been compared. It is a continuous perturbation of the existing complete OUTPUT CERTIFICATE with its explicit outside allowance. Possible outside atoms and their phases remain paid by (11). It supplies neither an early-time relative herald guarantee nor a finite all-future receiver theorem. A finite read window can separately use the unchanged slow-lead cut, with actual C on both sides, but no size or window is chosen here.

## 5. What the stationary O(m epsilon) data do and do not close

The exact product laws give |log(t_l/t_l0)|<=(2n_l+1)ell with ell=-log(1-epsilon); fixed-gap unequal slope sums give length-uniform slope perturbation bounds. These are the right variables for sharper dynamics, but are not enough to replace (10) by O(m epsilon) with uniform linewidth constants.

An exact nonuniform three-source elimination uses s_lL(D),s_lR(D),t_l(D), with source diagonal entries

    D-s_1L,
    D-s_1R-s_2L,
    D-s_2R-s_3L,

and port load s_3R(D). The loaded term is -t_3(D) G_tilde t_3(D), G_tilde=G(I-s_3R G)^-1. Only after this ordered full-fiber reduction may one take selected/complementary Schur blocks. The nominal symmetric s_lI+t_lX formula cannot be reused under arbitrary independent errors. The mass congruence used for comparison should remain the NOMINAL one if the nominal packet is fixed; actual masses then enter its error matrix and seed factors rather than silently changing the target.

The checked energy-resolved raw lemma shows a promising precise gain: an additional selected matrix numerator bounded by alpha lambda+beta|delta|, after port/complement control, contributes to its raw L2 ceiling in proportion to

    sqrt(lambda)[alpha lambda sqrt(pi/(2lambda^3))
                         +beta sqrt(pi/(2lambda))]
                =sqrt(pi/2)(alpha+beta).              (14)

Thus alpha,beta=O(m ell) would produce a selected traveling O(m ell) allowance without a time or inverse-linewidth penalty. This calculation does not prove the needed nonuniform numerator, third-hop relative action, complementary-column differences or all-head local estimate. Calibration constants, mass changes and higher-energy terms must be kept separately. The actual reference column v20=lambda^2*(2sqrt(2)/3)/qcrit is essential in the sharper loading proof.

The full source/local Stone problem is different. Applying only absolute norms to a beta|delta| numerator over R^2 produces beta log(1+rho^2/lambda^2), not automatically O(beta). To remove it requires a proved two-lip/static-mass cancellation or a controlled pulse comparison for the nonuniform energy-dependent pencil. Bounds on real stationary values or zero-energy slopes do not prove that cancellation. Every mediator recovery map also changes, including its endpoint injections and unequal slopes; one must bound that change on physical columns and retain the third-cell port and all closed-channel products. The direct finite-head theorem above avoids omitting these terms, at the cost of coarse inverse constants.

Accordingly the sharp O(m epsilon) complete scaling question remains open in this proposal. The proved result is (13) with explicit finite Schur/regularity gates and (10), not a tolerance target, a uniform-in-m performance theorem or evidence that those sharp estimates are impossible. No pole splitting or multiple-pole continuity is assumed.

## 6. Exposure and evidence

I authored the prior recovery, cut/layout and energy-resolved raw refinement and checked several loaded/pulse/complete interfaces. Root proposed this precision question. This new finite-Schur perturbation and complete composition is author work, not an independent recertification of those premises, and needs a distinct check.

Exact refreshed source identities:

- positive implementation: 8cadb35ee3c41e02b984906030297c2e1a5d5daf5a576ef0e2dfb4531f3da616; check65719cf16109c9cc397890ebcffbf592979a09299a872f9c26ed213b7fad23e0.
- stationary precision: ec94570c294d760dadda17370fb8e65634880aa346709bc2d28fc6f3245f0084; check2c6f4d9d74dc4fd348da7c743260caa5f32394a91db96ae458c50d5def6fef34.
- loaded full inverse:5f909e1ea897e9aaef31dd362e42fc60d5ba0b5f595d28bd12f1d000d8552a22; previously checkedf6303bb3.
- source time:73116231ff9d68e030b86def616eb69c088d72647005049279d82b5d0ab4137e; check496164c0.
- raw traveling:263929233b06c4466535452e95f3a05ecfd6ab1a1046938bbac57322c2870f97; check111aaeff.
- energy-resolved raw:7b74e1850a59a4d809edf0a049aa1fb5e773ddb5fdfb88aea563b2ba6db6fa44; newly read checkbe74e1e896b508bcfa2e50d65ae2ff87663eefeecd785e3a5819fa87e821a1cc.
- recovery:83530c67a650ae309fa920c0d149388080bb47178fd2b9f2a4cba88512be6333, especially its definition of the full port-forcing L0 map; check6f1b0755.
- final complete composition:6ed86c33b624ffc8f672e0f2380194fb624c9678b6f477ccab6f5cb59eef57f7; scoped checke9d6b346.

The positive-block and precision arguments were read fully in the immediately preceding coherent integration work and refreshed here; energy-resolved source and its new distinct check were read fully. The other unchanged full arguments and their exact physical scope were read during the preceding source/composition tasks, with identities refreshed rather than recursively audited. A truncated combined read was followed by separate complete reads of the new energy-resolved material. No new source-time or nonuniform-output theorem is imported by file label.

Only this proposal was written. No numerical integration, solver, dynamics, parameter sweep, operating point, canonical/Git/PR/checkpoint/prompt/axiom/model changes or delegation occurred. Native P-block and diagonal supply, initialization, independent onsite/block-shape errors, arbitrary downstream perturbations and physical implementation remain separate obligations.
