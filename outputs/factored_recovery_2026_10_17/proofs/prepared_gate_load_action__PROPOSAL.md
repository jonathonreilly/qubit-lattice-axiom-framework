# Gate load acting on the actual prepared boundary response

Status: new conditional author derivation requiring a distinct check. On the checked wide receiver domain, the actual endpoint-forced boundary vector y at a=v17 satisfies

    ||D_g y||<.357,                                  (1)

where D_g=-jQ-j²G_g is the difference between the auxiliary open-j surface and the actual gate load. This is an action bound for the actual response, not a uniformly small full load norm. It retains closed forcing and both record sectors. An optional consequence for the still-under-review full derivative096069 is stated separately; no operating point or temporal claim is made.

## 1. Why the gate preserves the B projections

The physical attached-kernel source specifies the24-head gate matrix h_x in each conserved record-X sector x=±1: ordinary head bonds, its real Hadamard junction, phase-cell bonds/occupations and terminal diagonal2j+jx. Before resolving record, the only record-dependent local terms are j n_T(I+X_R). They act trivially on the old/shared-source fiber. B acts on that old/source fiber and identically at every gate and slow-ray head. The kinetic bonds and compensation occupations likewise act as identity on that fiber. Therefore the gate-plus-slow-ray compression commutes with each spectral projector P_l of B. Its fixed sector inverse has the exact form

    R_g(E)=sum_l R_g,x(E-c_att-b_l) tensor P_l.

Record mixing in the computational basis does not change this fact: X_R acts on a different tensor factor and commutes with B. Resolve x first, or retain its orthogonal projectors (I+xX_R)/2. This local commutation does NOT imply that the upstream processor commutes with B or K. Its forcing can populate all channels, and no component of that forcing is removed.

In particular Q=Q_new(E-c_att-B), A=[j(Q-Q^-1)]^-1, G_g=e_p^T R_g e_p, D_g and the gate reflection commute channelwise within each x sector. This is established from the physical gate structure rather than assumed from an open scattering estimate.

## 2. Exact plane and load-action identity

At v0 let b be the actual outgoing cable coefficient and a_in its returned coefficient, acting on the FULL endpoint-forcing fiber. The physical gate/input separation is18 edges, so

    a_in=Q^36 r_gate b.

At a=v17, put b_a=Q^17 b. The actual total field there is

    y=Q^17 b+Q^-17 a_in=(I+rho)b_a,
    rho=Q² r_gate.                                 (2)

Thus the round trip at a is two steps; it is not r_gate alone. All closed growing powers were canceled before estimating any product. The exact auxiliary-to-gate load relation from the checked Schur formula is

    C_g=I+A D_g, rho=-A D_g C_g^-1,
    C_g^-1=I+rho.

Hence, without any condition on the upstream source,

    D_g y=D_g C_g^-1 b_a=-A^-1 rho b_a.              (3)

The ordering in this derivation already suffices; the local diagonal structure additionally justifies splitting and combining the explicit Q powers below. No inverse of I+rho is estimated to obtain(3), and the auxiliary load is not confused with the actual physical gate. The minus sign follows from the plus jQ auxiliary selfenergy in E-H and the negative j²G_g actual selfenergy.

## 3. Selected and closed action estimates

Retain the checked domain .0027<j<.003,0<g<=1e-6, |q-pi/2|<=h<=4e-6, d=2j sin h,d/g<=.5. On each selected channel |Q|=1, |r_gate|<.129 and |A^-1|=2j sin q<.006. The checked actual full-forcing feedback supplies ||P b||<460. Consequently

    ||P D_g y||<.006*.129*460=.35604.               (4)

This bounds the action on arbitrary endpoint forcing, not a scalar selected-input column. No factor ||y|| or inverse load denominator is needed.

For each signed closed root s, |s|<1/60, the checked gate bound is

    |r_gate,C| <=(1+1/(56|s|))/(1-|s|/56),
    ||C b||<1280.

The raw closed reflection is allowed to grow like1/|s|. In(3) its actual propagation gives

    |A^-1 rho Q^17|
      =j|s-s^-1| |s|^19 |r_gate,C|
      <=j(1+|s|²)(|s|^18+|s|^17/56)/(1-|s|/56).

This monotone positive envelope is bounded at1/60. With60^17>1.2e30 and j<.003, multiplication by1280 gives a full complementary action <1e-29. Both root signs and all seven closed channels are covered by the maximum of this diagonal bound, not by open flux unitarity. The fixed P/C output ranges are orthogonal; even a triangle sum of(4) and this bound proves(1).

The conserved record-X direct sum uses the maximum over x. Initial computational record0 is a normalized coherent inclusion into those sectors, not an extra multiplicity factor. All inequalities preserve passive references. Lower-lip fixed real conjugation preserves the exact load identity and every norm. The actual old/source mixing remains inside b, for which the quoted full-domain feedback bounds are explicitly needed.

Equation(1) says nothing about arbitrary y unrelated to this driven solution. For example the full load norm can remain near its checked .102 ceiling. Nor is (1) a derivative bound: small real action does not justify differentiating its upper bound.

## 4. Restricted consequence for the pending full derivative proposal

The source `prepared_full_recovery_factored_derivative/PROPOSAL.md`, SHA09606913b6bd71637b089ded04180b3afa6934ae39fa85926cb05d4e1f69423a, is STILL UNDER DISTINCT REVIEW at this writing. Its exact upstream formula is

    F_U=F_D-C_a D_g y.

In its partial derivative dot, only the slow boundary root is held fixed at its evaluation value; its physical correction is restored separately. The ordered product rule is

    dot F_U=F_D'-C_a' D_g y-C_a dot D_g y-C_a D_g dot y.

The new identity controls ONLY the second term by ||C_a'||*.357. It does not alter the other three bounds or assume a small derivative of D_g y. Conditional on that proposal's still-pending ceilings

    ||F_D'||<1.901e14, ||C_a'||<2.22e14, ||C_a||<8000,
    ||dot D_g||<1090, ||y||<521, ||D_g||<.102,
    ||dot y||<2e10, ||dot F_G||<1.3e11,

one obtains

    ||dot F||<1.901e14+(2.22e14)*.357
                   +8000*1090*521+8000*.102*2e10+1.3e11
              <2.9e14.                             (5)

The old .102*521=53.142 coefficient in that one term becomes .357. This is exact use of the physical load action, not a universal reduction of D_g or a global source commutation claim. The conservative remaining terms in(5) are intentionally unchanged.

If the complete096069 argument and this new action proof receive their distinct checks, its assembled identity

    F'=dot F-j R V_o Q_slow' V_o^T F

and restored output-column/closed-tail bounds would yield

    ||L'||<1.00068[2.9e14+1.28e6/g]+30.              (6)

At present(6) is explicitly conditional on that pending derivative review and checking the present proof. It is not an accepted replacement in a complete-device budget. No numerical parameter point, onset, receiver size, mass, performance or permanent-halt result follows here.

## Evidence, exposure and limits

I authored096069 and its derivative ancestors; root requested testing its dominant load-action product, without an assumed answer. The new physical B-block proof and reflection/load-action calculation are author work requiring distinct review. I read the complete wide-gate source and refreshed the attached-kernel physical gate matrix, full-B decomposition, load signs and reference-plane passages. Their unchanged scoped checks are reused. The earlier source/processor is not assumed to share the gate's B invariance. No recalibration or blanket ancestral recertification is claimed.

No scientific runner, inverse experiment, dynamics, numerical integration, sweep, operating-point selection, Git/canonical/publication/checkpoint/prompt/model change or delegation occurred. Only this proposal was created. Exact source identity is metadata, not proof.

- `slow_lead_wider_receiver_band/PROPOSAL.md`: `5b667173cd9ee3d8faa285e5856e8a89e8a83ae87f09207664cc5115e247ee57`.
- `slow_lead_wider_receiver_band_check/REVIEW.md`: `9c32a1c901300c32cb6d0630cfef19e9aa33b9438274b6ab8dc561ccc2a38b0d`.
- `record_attached_kernel/PROPOSAL.md`: `fbc1315e90a3980f71b1580de992b64602d5085f7a8aa1a50b90683da9ce9457`.
- `record_attached_kernel_check/REVIEW.md`: `7df395639ea91083d9321fd05f91ffbae94eb3ae87256beb09f7f4474fa2b005`.
- `slow_lead_wide_derivative/PROPOSAL.md`: `c2b9d6917db45faa1e9974cb69ef9bc683f45147bcb47b3588df36e94b630f2a`.
- `slow_lead_wide_derivative_check/REVIEW.md`: `c74a8118cccafe3e64dc6f4aa499fc7fa9abb194dae5cedbb2c253fb06054c79`.
- `prepared_full_recovery_factored_derivative/PROPOSAL.md`: `09606913b6bd71637b089ded04180b3afa6934ae39fa85926cb05d4e1f69423a`.
