# Explicit attached record geometry and full-fiber load interface

Status: source-exposed authored construction and exact algebra, requiring a different selective checker. This freezes one attachment and supplies finite-matrix scattering, closed-load and core-resolvent formulas. It does not inherit the unattached device's actual mass, runtime or output-error theorem. The local stationary gate is a checked dependency, not an all-time completion certificate.

## Sources and exposure

Use autonomous_record_route/PROPOSAL.md SHA256 93445d7d52e32859c980f0a0ebc6024238bedc7571d09e145ab1b128d8292f56 and its check c5f3e1d7cef939e1bfa95df19f970e4da454cd12a74f068147b6cd50cdf51d5a. I authored that check and the converter publication review; this new attachment/interface is author work, not an independent check of itself. Root supplied the candidate rigid lattice map below. I checked its actual site and phase consequences rather than assuming them.

The physical resource source is bandcenter_resources/PROPOSAL.md, verified 96d6fdfa01631c17bd43c62c3a11f8754d2b31836740cc11f5a663172e3b37e7, with prior check 01b87c7557a3d7c6c34f6a2cb1b6d7bfb61416cf3ca1d982e6aa704280352efd. The completely read current converter note is W/docs/NOMINAL_BANDCENTER_CONVERTER_COMPLETE_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md, verified f8480df631730d3e4e9fadb07b73486a1e02aec650511f7eae859ae2dabbe311; its author draft is converter_publication/NOTE.md a4b0fecba52f13078d01fbbe93f156212a506da0f68bbf1b17962adacf6b4d48. Necessary unchanged geometry/coefficient premises are reused from those complete readings. No original calibration is revalidated. PR9674 is root-supplied provenance, not remotely verified here.

No scientific/numerical execution, solver, parameter search, delegation, W/Git/model/prompt/checkpoint edit or publication occurred. Only source inspection, hash bookkeeping and this sole deliverable were performed. Applicable unchanged instructions/workflow are reused.

## 1. Frozen geometry and physical Hamiltonian

Retain the entire nominal converted apparatus except its straight infinite output beyond new index 17. Its original output origin is v0=(82,1,1). Retain the eighteen cable vertices

    v_n=(82+n,1,1), 0<=n<=17.

The old output converter still joins (81,1,1) to v0. Install ordinary -j bonds along this cable and from v17=(99,1,1) to the gate input port p=(100,1,1). No cap is installed at v17 in the actual attached device.

Map every local gate vertex from the checked proposal by

    F(x,y,z)=(108-y,1+x,1+z).

This is an integer orthogonal coordinate transformation followed by translation, hence preserves all nearest-neighbor edges. In particular

    R=(108,1,1), T0=(108,2,1), T1=(108,0,1),
    A0=(100,2,1), A1=(100,1,2),
    p=P_in=(100,1,1), o=P_out=(100,2,2).

Use exactly the transformed two arm paths and phase-cell bonds of the checked gate. The new final output is

    o_r=(100,2+r,2), r=0,1,..., with o_0=o.

It continues with -j bonds. For a finite version, M now counts these FINAL output vertices r=0,...,M-1, and a cap j n_(o_(M-1)) replaces the deleted outgoing bond. This M is not the old straight-output count.

Collision check: every new gate vertex has first coordinate between100 and108; all prior retained converter-device head vertices have first coordinate <=99, and the only prior ones above81 are the cable on y=1,z=1. The cable ends adjacent to p, without sharing a vertex. Within the transformed gate, distinctness follows from the injective rigid map and the checked local paths. The final output has x=100,z=2,y>=2; the only gate points at x=100,z=2 are A1 with y=1 and o with y=2. Thus the output extension meets the gate only at o. The record is distinct from every head site. All old/source qubits lie far outside the new region. Additional geometric adjacency, including around the arms, remains uninstalled under the same selective-coupling premise.

Keep the exact source B once, both original converters, input ell=20, emitter kappa=1e-8, and all old/source/contact coefficients. Add the gate's 24 head bonds, four phase-cell occupations, four junction vacancies and two contacts j n_T(I+X_R). All these blocks are static real PSD and at most two-qubit. The record has no free Hamiltonian and is supplied initially in |0>. This is a supplied preparation, not native Record identification.

The only added common scalar is c_R=4(sqrt(2)-1)j. Thus the complete physical scalar is c_att=c_total+c_R. This scalar is global, including while the head remains in the old apparatus; it cannot be charged only after gate arrival. Literal K and its target aging remain unchanged.

## 2. Counts and compression convention

The original nonoutput apparatus contains194 heads; the eighteen retained cable heads give a core C of212 heads. The gate has24 heads including both p and o. The final output contributes M-1 additional heads. Therefore finite head count is M+235, and adding the four old/source qubits and ONE record gives M+240 physical qubits.

There are194 edges within the original nonoutput head graph. Add one original output converter edge, seventeen internal cable edges, one cable-to-p edge,24 gate edges and M-1 final-output edges. Total head edges are M+236. The edge count exceeds the head count by one because the connected graph now has two independent cycles. The previous source B and source hopping are not counted as head edges.

Relative to the original M+223 block inventory, head-bond count increases by42. Four phase occupations, four gate vacancies and two record contacts add ten further blocks. The finite cap remains one block at its new location. Thus the stated decomposition has M+275 positive blocks. These are exact bookkeeping counts, not minima or feasible allocations. The record incident-block norm sum is4j; original source loads persist.

For later finite transfer, the new cap again makes the finite one-head operator the exact compression of this NEW infinite graph, with one cut -j. No old onset/window or old M is selected here. In the core-versus-gate algebra below, C is instead a temporary compression at v17: H_C includes the retained j n_(v17) contribution of its deleted -j bond. This is an algebraic compression diagonal, not an extra installed block in the actual attached Hamiltonian.

## 3. Conserved sectors and the exact 24-site matrix

X_R commutes with the entire attached Hamiltonian. Let x=+1,-1 denote its eigenvalue. In a fixed old parity sector retain the FULL eight-dimensional shared old/source fiber, with real spectral projections P_l of B and eigenvalues b_l. No old/source eigenvector or complementary direction is deleted. For a physical spectral parameter z_phys define lambda=z_phys-c_att and kinetic parameter z_l=lambda-b_l. The two x sectors each contain this full eight-dimensional fiber. The initially supplied |0>_R=(|+>+|->)/sqrt(2) requires coherent recombination afterwards.

Define the real symmetric 24 by24 gate matrix h_x on its two eleven-site arms and two ports. Its diagonal is2j at all sites except terminal diagonal2j+jx and the four phase-cell endpoint diagonals3j. Its off-diagonals are exactly the arm bonds -j, the two phase bonds -sqrt(2)j, and the square block -jU in the checked arm/port ordering. The port diagonals2j include the retained diagonal contribution of their external -j bonds. This is the compressed kinetic matrix after removing c_R; it does not remove B or K from physical evolution.

Let e_p,e_o be the gate port vectors and E=(e_p,e_o). For Im z>0 select s(z) solving

    z=2j-j(s+s^-1), |s|<1,

by continuation of the resolvent branch. At an open real energy z=2j(1-cos q), 0<q<pi, its upper boundary is s=e^(iq). At real closed energies the chosen s is the signed real decaying root. The free semi-infinite j lead's surface resolvent for convention (z-H)^-1 is m_free(z)=-s(z)/j. This sign follows also from m=1/(z-2j-j squared m).

Define the outgoing two-lead matrix

    D_x(z)=z I_24-h_x+j s(z)(e_p e_p*+e_o e_o*).

Each lead self-energy is j squared m_free=-j s, hence its subtraction gives the PLUS sign in D_x. For Im z>0 this is the Schur complement of a self-adjoint graph resolvent and is invertible. Its boundary continuation may require explicit pole checks at real energies; a formula written with an inverse does not silently exclude a real pole or a removable singularity.

## 4. Exact generalized scattering and reference planes

At either exterior lead let r>=0 count distance OUTWARD from its gate port, and prescribe

    psi(r)=s^-r a+s^r b, psi(0)=a+b.

The two-port vectors a,b are not flux-normalized across different closed channels. All open ports in one l channel have the same velocity, so their physical open normalization agrees. Substituting psi(1)=s psi(0)+(s^-1-s)a in the port equations gives

    psi_gate=D_x(z)^-1 E j(s-s^-1)a,
    S_x(z)=j(s-s^-1) E*D_x(z)^-1 E-I_2,
    b=S_x(z)a.                                      (A)

This derives the sign and source normalization, not merely an analytic continuation of a guessed unitary matrix. For closed s the same formula describes formal growing incoming and decaying outgoing coefficients; it is not a unitary closed-channel scattering assertion. Recover every finite gate amplitude by the first line of(A), and the entire lead tail by the stated root powers.

On the full eight-coordinate fiber, set S_x(lambda)=sum_l S_x(z_l) tensor P_l, with analogous diagonal root functions. Record recombination is the direct sum over x with projectors (I+x X_R)/2. The gadget alone is diagonal in B; the preceding old source need not be, so its later composition must keep the matrix order.

On the selected real band, the checked local gate gives S_x(pi/2)=i x X_port, and ||S_x(q)-rho_R(q)x X_port||<=33|q-pi/2| with rho_R=-i exp(22iq). This is a statement at gate port origins. Moving only the input reference plane back to v0 shifts it by18 edges. With D18=diag(s^18,1), the isolated-gadget scattering at planes(v0,o) is

    S_x^(v0,o)=D18 S_x D18.                          (B)

Consequently input reflection acquires s^36 and transmission s^18. The nominal transmitted common factor is s^18 rho_R=-i s^40, equal to -i at q=pi/2, multiplying x. This cable phase is not zero and must enter any later target. Formula(B) is a reference-plane identity; v0 is physically attached to the original converter, not an additional free semi-infinite lead in the complete device. Closed factors and input amplitudes must retain this convention when composing with that converter.

## 5. Exact outgoing load and core resolvent, without two-sided scattering poles

For emitter estimates it is simpler to eliminate the gadget and downstream lead together, leaving its INPUT PORT as part of the load. Define

    D_x^R(z)=z I_24-h_x+j s(z)e_o e_o*,
    g_x(z)=e_p* [D_x^R(z)]^-1 e_p.                  (C)

Only the downstream output lead is eliminated in(C); no input-lead self-energy belongs here. g_x is the boundary resolvent of the whole gate-plus-downstream-ray compression. It includes both terminated arms and all their returns. On the old/source fiber define G_x^load(lambda)=sum_l g_x(lambda-b_l)P_l. The exact core self-energy at a=v17 is

    Sigma_x(lambda)=j squared G_x^load(lambda),
    R_C,x(lambda)=[lambda-H_C-|a><a| tensor Sigma_x(lambda)]^-1. (D)

H_C includes full B, source contacts, converters, emitter and cable, after subtracting c_total; removing c_att from the total leaves the same core relative operator. In particular no extra c_R remains in H_C. Equations(C)--(D) are ordinary ordered block Schur complements. For a core forcing f, core response is R_C,x f and gate response in each B component is

    psi_gate,l=-j [D_x^R(z_l)]^-1 e_p P_l psi_core(a). (E)

The downstream tail is s_l^r psi_gate,l(o) for r>=0. The minus sign in(E) comes from the physical joining hopping -j. These formulas keep finite gate sites and all closed tails, not just the transmitted wave.

For comparison with the UNATTACHED infinite converter, its corresponding core self-energy at a is Sigma_free=-j sum_l s_l P_l. Thus

    DeltaSigma_x=j squared G_x^load+j sum_l s_l P_l,
    R_C,x=R_C,free+R_C,free E_a DeltaSigma_x E_a* R_C,x. (F)

All products in(F) retain their indicated order. This is a resolvent identity, not a small-perturbation claim. Small real OPEN reflection does not by itself bound the selected load, its poles, or its complex continuation sufficiently to import the original emitter theorem.

## 6. Closed-channel bound on the known REAL band

There is one useful direct finite-matrix estimate independent of open reflection. The centered gate matrix obeys

    ||h_x-2j I|| <=(2+sqrt(2))j.

Indeed its largest absolute centered row sum is a phase-cell row: j diagonal shift plus j+sqrt(2)j hoppings. Terminal rows have sum2j, square rows (1+sqrt(2))j, and remaining rows at most2j. Symmetry supplies the column bound. Adding either one or both outgoing lead self-energies costs at most j|s|, since the port projectors are orthogonal.

For each inherited real CLOSED channel on the wider selected band, |s_l|<1/60 and |z_l-2j|=j(|s_l|+|s_l|^-1)>60j. Therefore both matrices(C) and D_x are invertible there, with

    ||[D_x^R(z_l)]^-1||, ||D_x(z_l)^-1||
       <=1/[|z_l-2j|-(2+sqrt(2))j-j|s_l|]
       <1/(56j).                                   (G)

The last relaxation follows from 60-(2+sqrt(2))-1/60>56. In particular |g_x(z_l)|<1/(56j) and ||Sigma_x P_closed||<j/56, in each x sector. This is an absolute CLOSED-load bound, not a relative small error versus the free load or a bound on the selected open response. It rules out real closed-load poles on this particular inherited gap domain. It does not yet certify the complex disks needed by a new temporal argument. The source/channel gaps themselves remain inherited premises, not newly numerically checked values.

## 7. Same-port cancellation and the eighteen-edge closed return

Let r_x(z)=[S_x(z)]_pp in the GATE input reference plane. Sherman--Morrison applied to D_x=D_x^R+js e_p e_p* gives the exact meromorphic identities

    r_x=(-1-j s^-1 g_x)/(1+j s g_x),
    g_x=-(s/j)(1+r_x)/(1+r_x s squared),
    Sigma_x-Sigma_free=-j s r_x(1-s squared)/(1+r_x s squared). (H)

They are initially valid where their denominators are nonzero and then as meromorphic identities; cancellations do not establish separate inverse bounds. In particular the two record-sector load difference is exactly

    g_+-g_-=-(s/j)(1-s squared)(r_+-r_-)
                     /[(1+r_+ s squared)(1+r_- s squared)]. (I)

On the selected real open band the target gate is purely off-diagonal. Thus r_+(q0)=r_-(q0)=0, |r_x(q)|<=33u and |r_+-r_-|<=66u, where u=|q-pi/2|. Equations(H)--(I) exhibit linear suppression of the OPEN load correction and record-sector difference, with denominator at least1-33u in each factor. They do not turn all eight channels into open channels or suppress the closed corrections by u. This observation was suggested by root after the initial interface derivation; these identities are an exposed follow-up derivation, not independent origin.

Move the load reference plane back to v0, retaining the eighteen-edge free cable. Its reflection is R_x=s^36 r_x. Equivalently its surface resolvent is the eighteenth iterate of f_z(g)=1/(z-2j-j squared g), starting from g_x at p. Hence

    g_x^(v0)=-(s/j)(1+s^36 r_x)/(1+s^38 r_x).       (J)

This alternative partition excludes the cable from the original core; do not use it on top of(D), which already includes the cable. At the old output converter the hopping into v0 is -tau, so eliminating this alternative load contributes tau squared times g_x^(v0), not j squared times it. The scalar and full B decomposition remain unchanged.

For each real closed channel let a=|s|<1/60. From(G), |jsg_x|<a/56, so the first denominator in(H) is bounded away from zero and

    |r_x| <=(1+1/(56a))/(1-a/56),
    |R_x|=|s^36 r_x|<3*60^-36,
    |1+s^38 r_x|>1-3*60^-38.                       (K)

The apparently large 1/a factor has been paid before applying the cable suppression. The bound follows from a^36+a^35/56 at a<=1/60, not from incorrectly imposing open unitarity on closed r_x. Consequently(J) has no closed real pole on this specified gap interval, and its correction to -s/j is bounded by

    (a/j) |R_x|(1+a squared)/(1-a squared |R_x|).

This is a positive closed-return floor, not exact center cancellation. At a generalized source interface with output incoming closed coefficient a_C=R_C b_C, closed elimination has the ordered denominator I-S_CC R_C and correction S_PC R_C(I-S_CC R_C)^-1 S_CP. Here R_C is the diagonal load with entries R_x on that output port (and any other loads must be included explicitly). The relevant source S blocks must be evaluated at the SAME v0 plane and for the actual chosen core; this proposal does not substitute an old reference-plane S_CC ceiling without checking it. Equations(K) give the small load factor, but the full source denominator and open-feedback resolvent still require their own norm bounds. An endpoint DeltaG linear-open-plus-closed-floor estimate is therefore a concrete next goal, not a theorem already supplied by(H)--(K).

## 8. Outstanding decisive interfaces

The next checker should verify the orientation/signs in(A)--(F), the18-edge reference-plane shift, matrix diagonals, and the row bound(G). These exact formulas are intended to make subsequent estimates reproducible with a finite matrix rather than conceal a load behind a reflection ceiling.

For the SELECTED open channel, establish appropriate nonzero denominators or directly controlled full inverses for(C), then for(D), on the desired real interval and complex contours. A possible pole of the auxiliary load need not be a pole of the complete coupled system; cancellations must be handled in the full block matrix rather than by asserting separate bounded inverses where they fail. Conversely no absence of bound states follows from the band-center transmission. Both record sectors and their coherent seed weights must be retained in the actual spectral jump, mass and target comparison. Recover every gate/core/closed-tail component through(E), not just the outgoing open row.

Only after that work can one define and check a new common outgoing packet (including -i exp(40iq), source phase, c_att and literal exp(-itK)W), actual residual spectral mass, complete temporal escape and a finite-device window. The established unattached .001514/.001515 errors, T=1e17 and previous M are not transferred. No all-time herald correctness follows: terminal record rotation can occur before exit and returns can toggle it. The geometry and load formulas supply a concrete interface for further analysis, not native preparation/readout or a permanent completion latch.
