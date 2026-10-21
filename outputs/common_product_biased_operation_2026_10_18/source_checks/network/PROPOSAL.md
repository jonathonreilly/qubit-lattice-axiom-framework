# Stationary shared-record network with a positive record threshold

Provisional author derivation, conditional on the new biased-writer source dfe071 and requiring a separate composition check. A single positive record bias can be included in the actual one-control four-port network. The exact fixed-energy feedback problem remains invertible on an explicit two-open-channel domain. For record-blank incidence from I, its coherent comparator retains the common coefficient phase -i exp(57ik), while the outgoing record-1 spatial wave has a different momentum q. The full all-incidence comparator has ordered, channel-dependent phases; it is not the old scalar-phase matrix on the entire record fiber.

This is a stationary result only. No finite seed, normalized complete physical packet, finite observation window, faithful flag branch, preparation improvement or runtime is proved here.

## 1. Actual positive device and the single bias

Retain exactly the one-control core76b5, the two writers and two34-edge cables of c913, and the four infinite external radial leads. There is one physical program P at(21,1,0) and one physical record R at(0,0,0). In each program sector p the core has the four endpoint onsite occupations2j n_v and mediator coefficients D0 on the enabled matching and D1 on the disabled matching. Cross is enabled for p=0, straight for p=1. Its literal positive blocks are the eight Q_b bonds, eight separately listed b vacancies, four positive program-mediator blocks and four endpoint occupations. The exact all-head comparison with the old legal twelve-control sector is unchanged: the comparison isometry W acts only on program, so it also intertwines the additional record operator below. W is not physically implemented.

Both24-head writers, including their signed positive junction bonds, phase-cell repairs, four vacancies per writer and two contacts j n_T(I+X_R) per writer, are unchanged. All four terminal contacts use the SAME R. Add precisely ONE positive onsite block

    kappa n_R,  kappa>=0.                                  (1)

There is no separate bias for each writer, cable, lead, head or traversal. Head number and P remain conserved; X_R does not commute with(1). No X_R-sector diagonalization of the biased network is assumed.

The unchanged geometry is explicit: writer A has the two arms and ports of c913, with U_A=(0,8,0),F_A=(1,8,1); writer B is its image under(x,y,z)->(z,-y,x), with U_B=(0,-8,0),F_B=(1,-8,1). Their four distinct record-neighbor terminals are(+/-1,0,0),(0,0,+/-1). The core endpoints are I0=(20,0,0),O0=(22,0,0),I1=(22,2,0),O1=(20,2,0). The cables are

    O0 ->(22,-10,0)->(0,-10,0)->U_B,
    O1 ->(20,12,0)->(0,12,0)->U_A,

each34 edges with33 new interior heads. Set F0=F_B,F1=F_A. Final rays run in+x from their origins; I0 first steps to(19,0,0) then runs in+z, and I1 first steps to(23,2,0) then runs in+z. The checked disjointness and installed-neighbor inventory are unchanged by an onsite block at existing R. Unlisted couplings remain absent by supply.

The true common vacancy scalar remains

    c=8b+2c_R, c_R=4(sqrt(2)-1)j.                         (2)

The head-vacuum action is now c I+kappa n_R, not c I alone. In the one-head space write

    H=c I+K_0+kappa I_head tensor n_R.                     (3)

Restricting the last term to disjoint head-coordinate regions gives its internal/core/cable/external diagonal entries. These restrictions are a direct-sum partition of ONE operator, not several added physical biases. This explains why each regional stationary equation has the same record threshold even though only one onsite block is installed. If a uniform head penalty mu N is separately present, subtract the additional common one-head energy mu throughout; none of the stationary estimates changes. No such extra block is required here.

Before external-ray extensions the network has124 qubits (122 heads,P,R) and161 positive blocks: the160 from76b5 plus(1). These are finite internal-network counts, not finite-device resources. Head and program incident loads remain unchanged. The shared record load becomes8j+kappa. With D1=Lambda/8,D0=zeta D1,b=eta D0,j=b^2/D0, eta<=1/8,zeta<1/2, the inherited full-support loads are P:4(D1-2b)<Lambda/2, mediator:D1+2b<9Lambda/64, endpoint:6b+4j<13Lambda/256, other heads at most8j. For kappa/j<=.001, record load<8.001 Lambda/1024<Lambda. The bias introduces neither a new neighbor nor a negative compensator.

## 2. Common total energy and flux channel spaces

Let

    |k-pi/2|<=h<=10^-3, 0<=r=kappa/j<=10^-3,
    E=E_0(k)=2j(1-cos k),
    k_0=k, k_1=q=arccos(cos k+r/2).                       (4)

The physical stationary energy is c+E (or c+mu+E if the optional uniform penalty is present). Both channels are open and E=E_0(q)+kappa. The biased-writer source proves, directly from |cos q|<=.0015,

    |q-pi/2|<.002, sin k,sin q>.99, 0<=k-q<=r.            (5)

The last inequality is strict at its upper end when r>0; at r=0 both sides vanish. This endpoint qualification avoids the literal strict-inequality typo in the local source's displayed(2), without changing any of its non-strict norm ceilings.

In particular BOTH core momenta belong to[pi/3,2pi/3]. The core bound is valid on that larger band; the narrower .001 writer condition applies to the reference parameter k, not to an unsupported assertion that q also lies in the writer's original .001 band. The writer's full biased resolvent already treats q using its threshold perturbation proof.

At each external or cable reference plane use record channel vectors normalized by flux: a_a=sqrt(sin k_a) f_a, where f_a multiplies exp(-ik_a n). The common physical factor sqrt(2j) cancels in every scattering equation. All matrix norms below use this flux inner product, with the unchanged ordinary norm on path/program/passive references. Define

    Z=I_path,program tensor diag(exp(ik),exp(iq)),
    P_c=Z^34,  X=I_path,program tensor X_R,
    C=sum_p |p><p| tensor C_p tensor I_R,
    C_0=X_path, C_1=I_path,
    T=Z C=C Z, phi=-i exp(22ik), H_w=phi X.               (6)

P_c is the unitary one-way cable propagation in either direction. It follows from matching n and34-n exactly as in c913, independently for each channel. Its exponent is34, not33. Conversion to flux introduces no additional factor on a cable because a fixed record channel has the same velocity at its two ends.

The actual core scattering matrix, on I/O blocks and all program/record fibers, is the orthogonal sum of S_core,p(k) for R=0 and S_core,p(q) for R=1. It is unitary: the core conserves R, so its flux rescaling within each record block is scalar. With

    e=13eta^2+5zeta,

the checked core estimate gives

    ||S_c-[[0,T],[T,0]]||<=e.                            (7)

The two writers jointly have S_w=I_path tensor S_r(k) (and identity on program), with port ordering U,F. This is a direct sum over disjoint head paths carrying the ONE record fiber. It does not require conserved X_R. In the one-head coordinate equations, record contacts on the unoccupied other writer vanish, and the bias is the common threshold(3); no independent second record is introduced. Conditional on dfe071, S_w is unitary and

    ||S_w-[[0,H_w],[H_w,0]]||<=w,
    w=33h+480r.                                          (8)

The inverse estimate for the full48-dimensional single-writer matrix is at most10/(1-20r)<11. This is the explicit local internal solvability premise; scattering unitarity alone is not used to infer absence of an internal pole.

## 3. Exact full-fiber feedback and internal reconstruction

Partition S_c=[[A,B],[C_c,D]] and S_w=[[a,b_w],[c_w,d]]. Every exact block is a contraction. Equations(7)--(8) imply

    ||A||,||D||<=e; ||B-T||,||C_c-T||<=e;
    ||a||,||d||<=w; ||b_w-H_w||,||c_w-H_w||<=w.            (9)

For external incoming f_I,f_F, let v be the outgoing O coefficient and u the outgoing U coefficient. The exact equations, with noncommuting record order retained, are

    v=C_c f_I+D P_c u,
    u=a P_c v+b_w f_F.

If ew<1, define

    K=(I-a P_c D P_c)^-1, den=1-ew,
    ||K||<=den^-1, ||K-I||<=ew/den.                      (10)

This follows from a norm-convergent geometric series, with every actual reflection and threshold-changing writer passage included. Then

    S_IF = [[A+B P_c K a P_c C_c,       B P_c K b_w],
            [c_w P_c C_c+c_w P_c D P_c K a P_c C_c,
                                      d+c_w P_c D P_c K b_w]]. (11)

Its lower-left block also equals c_w P_c(I-D P_c a P_c)^-1 C_c. No commuting replacement of P_c with a writer block is made. These equations cover arbitrary incidence from I or F and coherent superpositions of both record channels at the same total energy, as well as arbitrary program/path/reference coherence.

Flux conservation in each unitary component cancels the internal cable currents because P_c is unitary. Hence(11) is an isometry on its finite external channel space, and therefore unitary. This is weighted-current unitarity, not unweighted spatial-coefficient unitarity. In particular the two writers' shared record does not invalidate the current cancellation: every term is already an operator on that same fiber.

All internal fields are retained by reconstruction, not declared vacant. Solve u=K(a P_c C_c f_I+b_w f_F), v=C_c f_I+D P_c u. At each cable site use the two counterpropagating channel waves. Core mediator coefficients are reconstructed separately in each record channel with denominator D_e-E_0(k_a); these are nonzero on the checked core band. Each writer's complete48-component vector is recovered by its full biased outgoing inverse acting on its two incoming port/record vectors. The writer inverse margin, core margin and(10) exclude an invisible homogeneous solution on this domain: homogeneous zero external data gives u=v=0, followed by zero component fields. This is a band-local stationary uniqueness statement only, not a claim excluding off-band/threshold point spectrum or estimating any seed overlap with it.

## 4. Correct ideal phase ordering and quantitative error

Setting the ideal reflection blocks to zero in(11) yields exactly the unitary comparator

    S_* = [[0, T P_c H_w], [H_w P_c T,0]]
        = phi [[0,Z^35 C X], [X Z^35 C,0]].               (12)

Each off-diagonal block is a product of unitaries. The two blocks have different orders of X and Z^35. At r=0 they coincide and reproduce c913. At r>0 they generally cannot both be written as the old scalar -i exp(57ik) times C X on the entire record fiber. Equation(12) is also consistent with reciprocal transposition: its two off-diagonal blocks are each other's transpose in the real program/path/record basis, since Z is diagonal and C is real symmetric. No conjugation of propagation phases is appropriate for that transpose relation.

For record-0 I incidence, the lower-left block gives

    S_* (f_I tensor|0>_R,0)
      = (0, -i exp(57ik) C f_I tensor|1>_R).              (13)

The common coefficient phase is independent of program and path, and the record is the same physical output R. The outgoing record-1 spatial wave uses exp(i q n). For record-1 I incidence its coefficient instead has phase phi exp(35iq), with record0 output. For F incidence with input record a, the upper-right phase is phi exp(35i k_(1-a)): the writer is crossed before the cable/core. Thus even F record0 incidence has the q cable/core phase. These distinctions are required by traversal order; they do not break the coherent R0 I-column target(13).

The same ordered telescoping argument as the original network remains valid because it uses only norms, not record commutation. Specifically,

    ||S_II||<=e+w/den, ||S_FF||<=w+e/den,
    ||S_IF,upper-T P_c H_w||<=e+w+ew/den,
    ||S_IF,lower-H_w P_c T||<=e+w+ew/den.

For example split B P_c K b_w-T P_c H_w into B P_c b_w-T P_c H_w and B P_c(K-I)b_w; the first term costs e+w and the second ew/den. Use the alternate inverse for the lower block. The symmetric matrix of these four norm ceilings bounds the full operator norm by its larger row sum. Multiplication by den shows that either row is at most[2(e+w)+ew]/den. Therefore

    ||S_IF-S_*|| <= Delta
      :=min{2,[2(e+w)+ew]/(1-ew)}.                        (14)

The cap2 uses unitarity of BOTH full matrices. No column normalization, postselection or lost internal probability is invoked. Equation(14), tensored with arbitrary passive reference, immediately bounds the R0 I column in(13). It also bounds all incoming columns against their actual ordered comparator(12), not against a silently fitted common scalar.

For completeness, replacing(12) by the old all-record scalar comparator costs at most35r, since ||Z^35-exp(35ik)I||<=35|q-k|<=35r. This optional larger-error comparison concerns coefficient spaces only. It never restores equal spatial wave numbers or dispersion, and it is not used in(13)--(14).

One explicit simultaneous smallness prescription is: for desired0<d<=1 choose positive eta,zeta,h and nonnegative r obeying

    eta^2<=min{1/64,d/156}, zeta<=d/60,
    h<=min{10^-3,d/396}, r<=min{10^-3,d/5760}.             (15)

Then e<=d/6,w<=d/6, ew<=d^2/36<1 and

    Delta<=[(2/3)d+d^2/36]/[1-d^2/36]<=5d/7<d.           (16)

The last inequality follows by taking d<=1 in the numerator after dividing by d and in the denominator. All local/core bands and load premises above hold at once. This is a sufficient stationary error family, not a time or resource scaling family. It allows a strictly positive r proportional to d if desired, but proves no finite-operation tolerance to that choice.

## 5. Spatial amplitude, energy and open operational obligations

For a unit ordinary-spatial incoming R0 I amplitude, flux conversion of(13) gives the ideal ordinary outgoing F amplitude

    sqrt(sin k/sin q) [-i exp(57ik)] C f_I tensor|1>_R,

with spatial factor exp(i q n). Its energy remains c+E_0(k)=c+kappa+E_0(q); replacing q by k would violate energy conservation. At this stationary level there is no normalized radial output state or empty-apparatus conclusion.

A future R0 incident spectral envelope g(k) with incoming launch phase included would naturally suggest the outgoing full-line scalar integral

    B_n(t)=1/sqrt(2pi) integral exp[i n q(k)-it E_0(k)]
                  sqrt(q'(k)) [-i exp(57ik)] g(k) dk,
    q'(k)=sin k/sin q.

Its full-integer-line L2 norm is ||g||_2 by changing variables p=q(k): the outgoing Fourier coefficient is [-i exp(57ik(p))]g(k(p))/sqrt(q'(k(p))). This elementary normalization follows from the explicit change of variables. It is NOT normalization of the complete physical network packet, whose incoming, outgoing and all internal pieces coexist and must solve the exact evolution together. A physical comparison restores exp(-ict), or exp[-it(c+mu)] for the separately specified uniform head penalty. There is no additional independent record phase to insert on top of E_0(k); alternatively separating exp(-it kappa) requires using E_0(q) consistently.

Open proof obligations are: construct the complete exact packet with its energy/channel measure and normalization for coherent incoming data; bound first and second k derivatives of q, every core/writer/feedback block and all internal maps; prove early and late separation with different group velocities; match an actual finite endpoint seed in full vector norm, paying all localized spectral components; control actual I/F cuts and returns with record-dependent channel energies; normalize the common finite F output and pay every internal/emitter/wrong-record residual. No old finite/flag proof is transported by analogy. The new bias has non-scalar head-vacuum action and breaks X_R conservation, so neither the old vacuum-preserving scalar perturbation class nor old sector packet constants automatically applies.

Record1 is still not an irreversible completion signal: a terminal contact can flip it inside a writer, and later returns can flip it again. This result supplies no physical measurement, capture, reset, blank preparation, autonomous loading, thermal improvement, native Record identification, old literal processor transfer, permanent halt or precision/manufacturing conclusion. Infinite rays are used only in the bounded one-head operator with finite program/record fibers, not as an unbounded infinite many-head sum.

## 6. Sources, exposure and verification boundary

All paths are relative to N=/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934. Fully read and SHA-256 refreshed unchanged for this derivation:

- common_product_biased_writer_scattering/PROPOSAL.md: dfe071282ac3d160073b85caa0bd11d4e1834e58278e1da8a3c354fec5440c18. PROVISIONAL dependency: its distinct check is pending at drafting, and its full48-dimensional inverse/flux bounds are adopted conditionally, not independently certified here.
- common_product_stage_record_core/PROPOSAL.md: c91300a5eb6db28e67e4b494398c57c3c53bc39d2da8c800a12c284cc5d6c729.
- common_product_single_control_router/PROPOSAL.md: 76b5fd9bdf7a1609dfbc981211a508991a6a24c53686e26f28907210007e1b01.

The complete checks common_product_stage_record_core_check/REVIEW.md (61de4ee29dd3838c4fc7c3bd19c49bf0cd4cb4bacf5ad3e8e10ca06c864e27c1) and common_product_single_control_router_check/REVIEW.md (549bf5e4862f9ad384fddaca6b6e73ae6c4da74c397b981c93a2d16473b418d0) were reread. Their checked core60bc91b6ad085a722b3805de1d1b0d93a9cabcf77b1c3f5a74e43045354c3182/check8fcee7e6ee6579196141e8e67d5adbf9887969cbbbd3de3c7d00c9caf8777e5d and actual writer93445d7d52e32859c980f0a0ebc6024238bedc7571d09e145ab1b128d8292f56/checkc5f3e1d7cef939e1bfa95df19f970e4da454cd12a74f068147b6cd50cdf51d5a are reused at the exact component scope recorded there. The writer inverse sharpening22bca57ebcbfb8cfabebbe044cd5302e784e585b503cee28d6172afc72e54cf0/checkd96ed6b26856490d802ceed2009f75aa9c0919eb8760bcfffe0389807965d1b5 enters through provisional dfe071. No old packet or finite-seed estimate is a premise of this proposal.

ROOT proposed composing the new threshold-aware local writer and explicitly warned about cable/writer ordering, shared bias and enlarged core bands. This author wrote c913 and76b5 and several earlier packet/finite interfaces. This is source/design-exposed same-model author continuation, not an independent or blind check. A distinct reviewer must check the regional interpretation of the single bias, shared-record direct sum without X conservation, flux conventions, all ordered feedback blocks, the all-incidence comparator versus its R0 I column, and the explicit simultaneous domain/error inequalities. Component support does not constitute support for this new composition.

Only this proposal was created. Verification consisted of author algebra, complete source reads and file/hash bookkeeping. No scientific executable, numerical sweep/simulation, W/Git/checkpoint/axiom/editable-prompt/model change, delegation or publication occurred. The source is provisional, with no retained status assigned.
