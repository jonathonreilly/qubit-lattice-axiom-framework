# Selective check: actual slow-output gate load

Disposition: conditional support for the stated real-band gate/load, forced-column, scattering, closed-tail and upstream feedback-interface estimates. I found no necessary mathematical correction. This does not establish a changed-device emitter denominator, spectral mass, complete output map, runtime or success theorem.

## Source, exposure and checking scope

Read the complete `../slow_lead_gate_load/PROPOSAL.md`, verified SHA256 c1e1fe95ca3c9d390df0fad468c80c93d4c1c2aa1e3fee4c93c4326f44b0e61d. The desired route and candidate constants were exposed. I did not author this proposal. I did author the attachment, passive-storage triage and slow-resource application, and previously checked the center inverse and attached endpoint. Thus this is independent of the present author, not blind, model-diverse, or an ancestral recertification.

The immediately preceding coherent task fully refreshed the attachment fbc1315e90a3980f71b1580de992b64602d5085f7a8aa1a50b90683da9ce9457, root interface a9795085bd36acbdaee9de8e46709f1a61c5065d5c6f0dadc37f8bb151f962e4 and its check ecec86951cdb2f36011e196fe8266bffec29f55a6d0ec8f67e4bfe5684a578fb. Here I reread the complete center-inverse source 3fb72f1629c0136531a41424683279a1b42f3a54bda4785359a367c018756c82 and attached endpoint source 2b2161aabb84d533ac884d4199a72d6c4ff6745cd00599a20abe547b9c9caea9, and refreshed the relevant local-gate 33u bound in source 93445d7d52e32859c980f0a0ebc6024238bedc7571d09e145ab1b128d8292f56. Previously checked exact center arithmetic and real-band domain/gap premises remain valid: center check cebb4153f1f1f75001614110ad7597fcf5b835ddad2ab15e0d57c1e089f0f67f; endpoint check 30bb3f38752c5d6fc2b036042315c7ccb82f2f932805e04476e9a886822b6fa3; wider-band source d79a1e9abbf0508a05169d4588539063854f0604ba8db933cf878496aa7328a2, with check 3f721b75911630e0aec48688893c6bae84a182cafaa1012c977e9e262d6e180d.

Applicable unchanged local instructions are reused. No numerical scientific execution, sweep, solver, delegation, model change, Git/publication, canonical-worktree or prompt edit occurred. Exact table data are reused from the prior checked computation; the new inequalities and scattering identities were reconstructed analytically. Only this review is written.

## 1. Physical modification, branches and inverse margins

The two origins o=(100,2,2) and first slow site (100,3,2) are distinct. The new connector tau_s=sqrt(jg), g=1e-6, differs from the original converter coefficient. The positive occupations restore the compressed gate diagonal and give every new site diagonal2j. They add no vacancy scalar. Thus the h_x in the gate Schur matrix really is unchanged; the change is in its outgoing selfenergy.

For the convention (z-H)^-1, the slow halfline surface function solves m=1/(delta-g^2 m). With physical decaying root delta=-g(v+v^-1), it is m=-v/g. Multiplication by tau_s^2=jg gives -jv, hence the PLUS jvP_o in D_new^R. The input outgoing load remains +jwP_p in D_new^2. There is no missing g/j factor.

On the selected channel, |v-w|<=|k-q|<.01201, so the whole-matrix Neumann denominator is >1-26*.01201=.68774. Since 38*.68774=26.13412>26, the inverse is <38/j. This is a real-band result only.

For closed channels the inherited TWO facts |w|<1/60 and |delta|>60j are retained (the former should not be rederived just from the latter using a rounded equality). With j>.0027, |delta|/g>162000, whereas 160000+1/160000<162000. The monotone small-root relation b+b^-1=|delta|/g proves b=|v|<1/160000 on either signed real branch. The centered h_x bound costs (2+sqrt2)j. In the two-output inverse, the orthogonal port projectors make the load norm max(j|w|,j|v|), not their sum. Therefore 60-(2+sqrt2)-1/60>56 proves both closed inverses <1/(56j).

In the selected open channel D_new^2 has imaginary part j sin(q)P_p+j sin(k)P_o. A kernel vector has both port coordinates zero. The invertible real mixer forces both arm ends zero, and the nonzero tridiagonal hoppings propagate zero throughout the arms. This proves actual invertibility, without using unitarity as a substitute for a pole check.

## 2. Sharper forced columns: the decisive center cancellation

The checked chain table gives physical p AND o port columns of R2 with squared norm <=25/(4j^2): the port rotation has equal-magnitude coefficients for both ports and orthogonal arm ranges. Transpose symmetry gives the corresponding row norms; Hermitian symmetry is neither true nor needed.

At center S_x=i x X, so R2=(I+S_x)/(2ij) on the port block. Explicitly R2,pp=R2,oo=-i/(2j), R2,op=x/(2j). Removing the input selfenergy has denominator1/2 and yields R0=R2+2ij R2p p^T R2. Direct substitution gives

    R0,pp=-i/j, R0,op=x/j, R0,oo=0,
    R0 p=2R2 p,
    R0 o=R2 o+i x R2 p.

Both column norms are at most5/j. The zero output diagonal is exact in either record sector, not an approximate real-part cancellation.

For Delta=D_old^R(q)-D_old^R(q0), ||Delta||<=3ju. The checked ||R0||<25/j gives column norm <=5/[j(1-75u)]. Applying R-R0=-R0 Delta R entrywise with the CENTER row bound5/j and this perturbed column bound gives |(R-R0)_ab|<=75u/[j(1-75u)] at both ports. This proves the stated h, |R_oo|<=h/j and |R_op|<=(1+h)/j.

The slow update is +eta P_o, eta=j(v-w), so its inverse column is R p-eta R o R_op/(1+eta R_oo). The sign and denominator are correct. At u<=4e-6, h<=.0003/.9997 and .01201h<.00000361. Consequently the denominator is >.99999639. For a transparent conservative arithmetic check, 5/(1-75u)<5.001501 and the correction bracket is <1.012014; their product is <5.062, hence safely <5.064. The inverse <38/j and column <5.064/j concern different quantities and are compatible.

The physical slow-tail equation gives psi_m=(tau_s/g)v^(m+1)psi_o. For a closed channel its l2 multiplier is sqrt(j/g)b/sqrt(1-b^2)<.00035. Since its forced gate norm is <1/56, combining the gate and its tail orthogonally gives <sqrt(1+.00035^2)/56<1/55. The selected channel contributes gate sites only; its stationary open ray is not l2. Orthogonal B-fiber ranges then make the full gate-plus-closed-tail norm the maximum, <5.064. There is no factor8 and no discarded closed tail.

## 3. Two-origin interface and repeated reflections

I reconstructed both directions from the endpoint equations. For incidence from the old side, tau_s t_L=j(w+r_L w^-1) and t_L=(tau_s/g)v(1+r_L), giving (7). For incidence from the slow side, tau_s t_R=g(v+r_R v^-1) and t_R=(tau_s/j)w(1+r_R), giving (8). They refer to the old site n=0 and distinct new site m=0.

Velocity normalization with V_j=2j sin q, V_g=2g sin k produces the same off-diagonal coefficient in both directions,

    t_f=exp[i(q+k)/2] sqrt(sin q sin k)/sin((q+k)/2).

The identity sin^2((q+k)/2)-sin^2((q-k)/2)=sin q sin k verifies current conservation and the stated moduli. At center t_f=i, not1; the physical coefficient is i sqrt(j/g).

At the shared old output origin o, the interface's reflected wave is the gate's incoming wave directly. No extra w^2 is allowed. Solving that scalar feedback gives all four expressions (11), including R_right=r_R+t_L r_o t_R/(1-r_o r_L). Since t_L t_R=t_f^2, its flux form follows. The real gate is reciprocal in the equal-velocity old-port convention, so t_rev=t.

With |r_o|,|r_p|<=33u and |r_L|<=1506u, d_min>1-.000132*.0061>.99999919. Then 33+1506/d_min<1540 proves the non-strict center-valid linear bound; 1540*(4e-6)=.00616<.0062. The center result is exactly zero, without a false strict zero inequality.

For the sector difference, t_+ approximates rho_R and t_- approximates -rho_R within33u. Thus |t_++t_-|<=66u and |t_+-t_-|<=2 by individual unitarity. Expanding the two fractions gives the stated terms132u|r_L|/d_min and66u|r_L|^2/d_min^2, plus66u from r_p. Their coefficient is <66+.806+.0025<68. This is a genuine cancellation of the common reflected interface contribution after two signed transmissions. It does not bound each individual reflection by68u.

For transmission, write t/d-x rho_R=(t-x rho_R)+t(1/d-1). Since |t|,|t_f|<=1, this costs at most33u+33u|r_L|/d_min<34u. Replacing t_f by its phase costs <=|r_L|^2<=1506^2*(4e-6)u=9.072144u, giving the safe44u. Both bounds cover the center non-strictly.

## 4. Closed feedback, cable phase and source-facing margin

For signed real decaying roots, the triangle bound on (w-v)/(v-w^-1) is a(a+b)/(1-ab). The original closed gate reflection bound applies at either port: its one-output inverse bound is obtained by the same centered row argument for either retained port. Multiplying gives the displayed function of a,b. A conservative check uses a+1/56<.034525, a+b<.016674 and (1-a/56)(1-ab)>.999702; its quotient is <.00058. The function increases in a,b on this domain. Thus the generalized closed feedback in (11) has margin>.99942; closed unitarity is not invoked.

The new load inverse independently gives |g_new|<1/(56j). Substitution into the exact input reflection formula pays the a^-1 factor before the a^36 cable factor: [a^36+a^35/56]/(1-a/56)<3*60^-36<1e-63. Both record sectors obey it; their difference costs at most twice this floor. No zero-energy closed cancellation follows.

The cable is still eighteen old-j edges. Its shift is diag(w^18,1) on BOTH sides of the generalized two-port matrix. Accordingly reflection gains w^36 and transmission gains w^18, with right reflection unchanged. The comparison -i x w^40 exp[i(q+k)/2] is correct at the specified planes. At center the gate-plus-interface transmission before cable is -x, while w^18=-1; the source-plane transmission is x. Omitting the connector's i or moving the slow origin onto o would give the wrong common phase.

The unchanged terminated source is defined BEFORE loading at v0, with ||S_CC||<2e8 and |S_PP|=1. With new closed return <1e-63, its closed Neumann product remains <2e-55. The ordered correction S_PC R_C(I-S_CC R_C)^-1 S_CP is <8e-47. Thus the effective selected reflection differs from the unloaded unit-modulus scalar by that amount, and the new selected loop denominator is >1-(1+8e-47)*.0062>.9937. This supports this background interface, not the original attached emitter constants: its open reflection has changed from33u to1540u.

## 5. Momentum conversion and limits

Differentiating equal energy gives dk/dq=V_j/V_g. A physical transmitted integral t_L F_q dq becomes t_L(dq/dk)F_q dk, equivalently t_f sqrt(dq/dk)F_q dk. Its squared coefficient norm is exactly integral|t_f F_q|^2dq. The first-site reference phase and actual gate return denominator must be included once. Retarded coefficients under k use i V_g A_slow/sqrt(2pi). The full eight-fiber lifting uses fixed spectral projections; later upstream products cannot be reordered by assuming those projections commute with the source.

These checks support the actual changed local load and real-axis margins, including both lips by conjugation of the real fixed-basis equations. They do not supply a quantitative complex strip. The actual emitter Green function, complete seed matrix mass/regularity, wrong-window inputs, slow outgoing/incoming profile and temporal behavior remain new obligations. Literal K/W, c_att, the supplied seed and passive references remain in the target. No inherited runtime, capture probability, resource advantage, finite-horizon success, permanent latch or native Record claim is certified.
