# Actual record gate with a same-center slow output load

Status: new authored conditional real-band interface, requiring independent checking. Replace only the outgoing lead of the frozen record gate by g=10^-6, connector tau_s=sqrt(jg), and positive occupations preserving diagonal 2j. On the unchanged selected physical energy bands, the actual new one-output gate inverse is <38/j. The source-facing OPEN reflection is <.0062 and satisfies a zero-floor bound <=1540u, u=|q-pi/2|<=4e-6. Its record-sector difference is smaller, <=68u. The full closed return at v0 remains <3*60^-36 per channel. Exact scattering, recovery and momentum conversion are given below. No emitter, seed-mass, runtime, output-error or finite-success theorem is transferred to this changed Hamiltonian.

## Sources and exposure

Read COMPLETE root-authored `../same_carrier_slow_lead/PROPOSAL.md`, SHA256 `a9795085bd36acbdaee9de8e46709f1a61c5065d5c6f0dadc37f8bb151f962e4`, and its distinct check `../same_carrier_slow_lead_check/REVIEW.md`, SHA256 `ecec86951cdb2f36011e196fe8266bffec29f55a6d0ec8f67e4bfe5684a578fb`. The new lead, g and suggested rank-one perturbation were exposed by root, not discovered independently here.

Reuse complete unchanged attachment `../record_attached_kernel/PROPOSAL.md` fbc1315e90a3980f71b1580de992b64602d5085f7a8aa1a50b90683da9ce9457 and my check7df395639ea91083d9321fd05f91ffbae94eb3ae87256beb09f7f4474fa2b005; local gate source93445d7d52e32859c980f0a0ebc6024238bedc7571d09e145ab1b128d8292f56/checkc5f3e1d7cef939e1bfa95df19f970e4da454cd12a74f068147b6cd50cdf51d5a; gate inverse3fb72f1629c0136531a41424683279a1b42f3a54bda4785359a367c018756c82/checkcebb4153f1f1f75001614110ad7597fcf5b835ddad2ab15e0d57c1e089f0f67f. The fixed wider-band source d79a1e9abbf0508a05169d4588539063854f0604ba8db933cf878496aa7328a2 supplies the inherited real kinetic gap. The terminated upstream source matrices are unchanged and may be reused from attached endpoint2b2161aa/check30bb3f38 only BEFORE imposing the changed gate load.

I authored earlier attachment/recovery checks and the all-time/publication synthesis, but neither this scalar slow interface nor the local gate. This is source-exposed author derivation, not an independent check. Original calibration and all supplied coefficient premises remain conditional. No scientific execution, sweep, solver, delegation, Git/W/publication/model/prompt/checkpoint edit occurred. This is the sole deliverable.

## 1. Coordinates, diagonals and branches

Keep input p=(100,1,1), output o=(100,2,2), the entire 24-site gate h_x in record-X sector x=+1 or -1, and the eighteen-edge cable from v0=(82,1,1) to p. The old output port o is NOT the first slow site. The latter is m=0 at (100,3,2); slow site m is (100,3+m,2). Its connector to o is -tau_s, where tau_s differs from the original old-J/new-j converter hopping. All slow diagonals are 2j and their shared B is unchanged.

The port occupation (j-tau_s)n_o, first slow occupation (2j-tau_s-g)n_0 and later occupations 2(j-g)n_m are nonnegative. Together with their exchange blocks they preserve every stated diagonal. They introduce no vacancy scalar, so c_att is unchanged. This is an actual Hamiltonian modification, not a change in comparison convention.

For each B eigenvalue b_l and scalar-subtracted physical energy lambda, set z_l=lambda-b_l and delta_l=z_l-2j. Define retarded roots by

    delta_l=-j(w_l+w_l^-1)=-g(v_l+v_l^-1),
    |w_l|,|v_l|<1 for Im lambda>0.

On the selected open channel w=exp(iq), v=exp(ik), q,k in (0,pi). On the real band |delta|<2.4e-8 and g=1e-6, both are open; |q-k|<.01201 and |v-w|<.01201. In each of the other seven channels the unchanged old gap gives |delta_l|>60j>.162 and |w_l|<1/60. Since |delta_l|/g>162000>160000+1/160000, the signed slow decaying root obeys

    |v_l|<1/160000.                                (1)

Thus there is still one open and seven closed directions per parity/record sector on these chosen windows. This identifies channel types on a specified energy set, not actual spectral concentration of the modified device.

## 2. Actual finite inverse and full recovery

The free slow surface resolvent at its FIRST site is -v_l/g. Its contribution at the old port is tau_s^2(-v_l/g)=-jv_l. Consequently

    D_x,new^R(z_l)=z_l I_24-h_x+j v_l P_o,
    D_x,new^2(z_l)=z_l I_24-h_x+j w_l P_p+j v_l P_o. (2)

The first eliminates only the slow ray; the second also imposes an outgoing old-j input lead. Neither changes h_x or the port compression diagonal. In the selected open channel,

    D_x,new^R-D_x,old^R=j(v-w)P_o.

Using the checked ||(D_x,old^R)^-1||<26/j, Neumann inversion gives

    ||(D_x,new^R)^-1||
       <26/[j(1-26*.01201)]<38/j.                  (3)

Indeed 26*.01201=.31226 and 38*.68774>26. This is a genuine complete 24-site inverse margin on the real band, not a scalar boundary estimate.

For closed channels the centered row bound ||h_x-2jI||<=(2+sqrt(2))j gives

    ||(D_x,new^R)^-1||,
    ||(D_x,new^2)^-1|| <1/(56j),                    (4)

because the selfenergy norm costs at most j/60 for the two orthogonal ports, and |delta_l|>60j. This covers signed roots below and above the lead bands without importing scalar-subtracted positivity of the attached source. On the open band D_x,new^2 is invertible as well: its imaginary part is positive on both ports, with coefficients j sin q and j sin k. A kernel vector has zero ports, then zero arm ends by invertibility of U, then zero arms by their nonzero hoppings. This is an existence proof; (3) is the needed quantitative one-output inverse.

Let g_x,new(z_l)=e_p*(D_x,new^R)^-1e_p. On the full eight-dimensional fiber

    G_x,load(lambda)=sum_l g_x,new(z_l)P_l,
    Sigma_x(lambda)=j^2 G_x,load(lambda).            (5)

The cable boundary a=v17 remains joined to p by -j. Its gate response is

    psi_gate,l=-j(D_x,new^R(z_l))^-1e_p P_l psi(a).

The forced column admits a substantially sharper estimate than (3). At q0=pi/2 the old equal-lead gate has S_x=i x X_ports, and its port Green matrix is (I+S_x)/(2ij). Thus R2,pp=R2,oo=-i/(2j) and R2,op=x/(2j). The checked rotated-chain column norms give BOTH physical port columns norm <=5/(2j): each physical port is an equal signed superposition of the same two orthogonal arm ports. Removing the input selfenergy gives

    R0=R2+2ij R2 e_p e_p^T R2,
    R0,pp=-i/j, R0,op=x/j, R0,oo=0,
    ||R0 e_p||, ||R0 e_o||<=5/j.

For the output column, specifically R0 e_o=R2 e_o+i x R2 e_p; for the input column it is 2 R2 e_p. These signs use transpose symmetry and the actual center scattering phase. Put h=75u/(1-75u). The real-band perturbation of norm <=3ju, with ||R0||<25/j, implies for R=(D_x,old^R)^-1

    ||R e_p||,||R e_o|| <=5/[j(1-75u)],
    |R_oo|<=h/j, |R_op|<=(1+h)/j.

The entry changes are bounded by (5/j)(3ju)(5/[j(1-75u)]), using the resolvent identity and the center ROW norm 5/j. With eta=j(v-w), exact Sherman--Morrison now gives

    (D_x,new^R)^-1 e_p
      =R e_p - eta R e_o R_op/(1+eta R_oo).

Consequently the actual forced-column recovery satisfies

    j ||(D_x,new^R)^-1 e_p||
      <= 5/(1-75u) [1+.01201(1+h)/(1-.01201h)]
      <5.064,                                      (3a)

since u<=4e-6, h<=.0003/.9997 and the denominator exceeds .99999639. The full inverse bound (3) remains useful for regularity; (3a) is the sharper boundary-forcing estimate. This derivation was prompted by root's exposed center-column calculation and is not independent of that suggestion.

Hence the full eight-fiber gate recovery has norm <5.064, by an orthogonal direct sum, not eight times a scalar bound. The slow tail is exactly

    psi_slow,l(m)=sqrt(j/g) v_l^(m+1) psi_gate,l(o),
    m=0,1,... .                                    (6)

The selected open stationary tail is not l2 and is treated through flux/Fourier coefficients below. For a closed channel its complete tail factor is sqrt(j/g)|v_l|/sqrt(1-|v_l|^2)<.00035, using sqrt(j/g)<55 and (1). Its gate factor is <1/56, so its gate-plus-tail recovery is <sqrt(1+.00035^2)/56<1/55. The selected block recovers only gate sites with norm <5.064. Thus the combined map into all gate sites AND all seven slow closed tails has full-fiber norm <5.064. It does not include the open stationary ray or any new bound on the upstream emitter inverse.

## 3. The interface coefficients at the correct two origins

At the interface, old port o has index n=0 on its virtual old-j side, whereas first slow site has m=0. For old incidence psi_n=w^n+r_L w^-n at n<=0 and slow outgoing t_L v^m, exact matching gives

    r_L=(w-v)/(v-w^-1),
    t_L=sqrt(j/g) v(1+r_L).                         (7)

For incidence from the slow side, write v^-m+r_R v^m there and t_R w^-n on the old side. The two boundary equations instead give

    r_R=(v-w)/(w-v^-1),
    t_R=sqrt(g/j) w(1+r_R).                         (8)

These formulas hold as generalized coefficients on closed branches too, without assigning them flux unitarity. On the real open band, define velocities V_j=2j sin q and V_g=2g sin k. The two flux-normalized transmissions agree:

    t_f=sqrt(V_g/V_j)t_L=sqrt(V_j/V_g)t_R
       =exp[i(q+k)/2] sqrt(sin q sin k)/sin((q+k)/2). (9)

Their positive amplitude satisfies |t_f|^2=1-|r_L|^2=1-|r_R|^2. At center r_L=r_R=0 and t_f=i, whereas the physical t_L=i sqrt(j/g). In particular the connector contributes a nontrivial phase even when perfectly matched. From the checked scalar interface

    |r_L|<=.251|delta|/g<=1506u,
    |r_L|=|r_R|<.0061.                             (10)

The non-strict linear inequality covers u=0. No false strict zero-floor bound is asserted.

## 4. Exact gate-plus-interface scattering

Let the ORIGINAL two-j-lead gate scattering at p,o be

    S_gate,x=[[r_p,x,t_rev,x],[t_x,r_o,x]].

It acts diagonally in B and is complex symmetric in these equal-velocity port conventions, so t_rev,x=t_x. On the selected channel it is unitary and the checked gate estimate gives |r_p,x|,|r_o,x|<=33u, |t_x|<=1 and |t_x-x rho_R|<=33u with rho_R=-i w^22.

The interface relation at the shared old output plane o is EXACTLY incoming_to_gate=r_L outgoing_from_gate. There is NO additional w^2 here: r_L is already referred to o, not to its former next site. Summing the actual repeated reflections gives, with d_x=1-r_o,x r_L,

    R_left,x=r_p,x+t_rev,x r_L d_x^-1 t_x,
    T_left,phys,x=t_L d_x^-1 t_x,
    T_right,phys,x=t_rev,x d_x^-1 t_R,
    R_right,x=r_R+t_L r_o,x d_x^-1 t_R.             (11)

For open channels the off-diagonals in the flux-normalized full matrix are both t_f t_x/d_x, and R_right=r_R+t_f^2 r_o,x/d_x. This matrix is unitary by the actual real matching/current conservation. Closed-channel formulas (11) use physical generalized coefficients instead of flux factors.

The source-facing open reflection has the strong bound

    |R_left,x|<=33u+|r_L|/(1-33u|r_L|)
               <=1540u <.0062.                    (12)

The denominator is >1-(.000132)(.0061)>.99999919. This estimate is obtained from repeated scattering, not from squaring the coarse inverse norm 38/j.

There is also a useful sector-difference improvement. Since t_++t_- has norm <=66u while |t_+-t_-|<=2, one has |t_+^2-t_-^2|<=132u. Taking the difference of the two fractions in (11) gives

    |R_left,+-R_left,-|
      <=66u+132u |r_L|/d_min
                      +66u |r_L|^2/d_min^2 <=68u.   (13)

This reflects the cancellation of the leading common slow-interface reflection under two signed gate transmissions. It is not a claim that the actual individual reflection is as small as the sector difference.

For transmission, a derived local comparison is

    |T_left,flux,x-x rho_R t_f|
       <=33u+33u |r_L|/d_min <=34u.                 (14)

Since |t_f-exp[i(q+k)/2]|=1-sqrt(1-|r_L|^2)<=|r_L|^2, an optional unit-modulus phase comparison is

    |T_left,flux,x-x rho_R exp[i(q+k)/2]|
       <=34u+|r_L|^2 <=44u.                        (15)

Here |r_L|^2<=1506^2 u^2<=9.072144u on the specified band. These constants are newly derived local scattering ceilings, not a requested or inherited complete-device target error.

## 5. Closed scattering and the eighteen-edge source plane

The denominator in (11) also has a direct closed-channel margin. Put a=|w_l|<1/60 and b=|v_l|<1/160000. Equations (7) and the original closed gate inverse imply

    |r_L|<=a(a+b)/(1-ab),
    |r_o,x|<=(1+1/(56a))/(1-a/56).

Their product is bounded by

    [(a+1/56)(a+b)]/[(1-a/56)(1-ab)]<.00058,

using the upper limits for a,b; the expression increases with both. Thus every closed d_x is nonzero with |d_x|>.99942. This independently validates the formal composition (11) on the actual signed branches, without a closed-channel unitarity assumption.

Alternatively the new actual load (5) directly gives the total input reflection

    R_left,x=(-1-j w_l^-1 g_x,new)/(1+j w_l g_x,new).

By (4), its cable-shifted reflection obeys exactly the old safe form

    |w_l^36 R_left,x|<3*60^-36<1e-63.              (16)

The 1/a factor is paid before multiplying by a^36. The new slow branch does not change the cable's old-j roots or its length. Its closed sector difference can be bounded by twice (16); no exact closed-center cancellation is assumed.

At reference planes (v0, first_slow_site), move only the INPUT plane by eighteen edges. With D18=diag(w_l^18,1), the generalized two-port matrix changes to D18 S_new,x D18. Thus left reflection acquires w_l^36, each transmission acquires w_l^18, and right reflection is unchanged. For the selected channel the flux transmission comparator in (15) becomes

    x w^18 rho_R exp[i(q+k)/2]
       =-i x w^40 exp[i(q+k)/2],                   (17)

equal to x at the common center. The gate-port transmission alone is -x there; the cable factor i^18=-1 accounts for the difference. A later source/output packet must retain this new k-dependent phase and the source's unchanged q-dependent phases.

All formulas lift to the full eight-coordinate fiber by summing their B-channel blocks against the fixed orthogonal P_l and then retaining both record sectors. The upstream source need not commute with these projectors. If its unchanged input-terminated matrix is S^D, the actual new feedback is b=(I-S^D R_new,x)^-1 B_e f at v0, with R_new,x diagonal in B. Closed elimination still has ||S_CC R_C||<2e-55 from (16). The selected effective source reflection differs from its unit-modulus unloaded value by <8e-47, exactly as before. Equation (12) therefore supplies a real selected feedback denominator >1-(1+8e-47)*.0062>.9937. This is a useful modified-load regularity input; it does not import any old endpoint, emitter or density error constant. Their actual Green matrices change and require fresh quantitative comparisons.

## 6. Slow momentum and the remaining physical interface

Energy conservation gives

    dk/dq=V_j/V_g,   dq/dk=V_g/V_j.                (18)

Suppose a particular actual outgoing integral before this connector is written with q-normalized coefficient F_q. On moving to the slow first-site origin, physical transmission and change of variable give

    F_slow(k)=t_L(q(k)) (dq/dk) F_q(q(k))
             =t_f(q(k)) sqrt(dq/dk) F_q(q(k)),       (19)

with the gate return denominator and any cable phase included in the ACTUAL F_q, or multiplied explicitly by (11), but never omitted. Consequently its squared k norm is integral |t_f F_q|^2 dq. Equivalently a retarded slow coefficient A_slow uses i V_g A_slow/sqrt(2pi), not the old i V_j normalization. Closed tails use the geometric norm (6), not an open momentum Jacobian.

These identities do not say that F_q remains the former attached reference profile: the slow load changes source feedback and the emitter selfenergy. Even perfect center matching is not equality of the spectral measure on a nonzero band. A new full-input endpoint comparison, actual seed mass, common slow outgoing/incoming profile, spectral synthesis, and temporal estimate are still needed. The literal K/W and c_att, all wrong-window prepared inputs, supplied initialization and record measurement remain owed. No unchanged runtime, finite success probability, new resource advantage or permanent-record claim follows from this local calculation.
