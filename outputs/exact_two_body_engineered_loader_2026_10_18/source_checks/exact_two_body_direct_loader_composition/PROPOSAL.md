# Exact two-body direct-loader composition on four rails

New author derivation requiring a distinct composition check. The accepted exact diamond7fa888 is a premise. The corrected matched-extension source a1157 has now received distinct check36a1, read completely before this freeze; its local matching is adopted at that checked scope, not as evidence of the present global composition. The original75a0 is preserved but is not the operative phase convention. The new contribution is an explicit ordered global conjugacy on the full shared Q/P/R fiber, with every physical arm retained, rather than an approximate gate or a transfer of an earlier finite theorem.

There is an exact 26-layer construction retaining the original direct-loader function U_f=I_a tensor[X_R C_P^(b) SWAP_QP]. Its physical right-side gate is -U_f. The minus is fixed and included in the scalar output profile. On the one-head sector the infinite device is unitarily equivalent to four uniform scalar chains. A finite symmetric input/output extension has the corresponding exact scalar reduction, but no high-success time window or resource-versus-error policy is proved here. All signed positive blocks, exact matching, selective finite-range installation, input and blank apparatus remain supplied.

## 1. Local supplied blocks and corrected matching convention

There are four head rails labeled (a,b) in {0,1}^2 and three ordinary shared data qubits Q,P,R. Rail labels are head-position labels, not additional physical qubits. No free data or active reference Hamiltonian is present. Every occurrence of Q, P or R below uses the same qubit.

For head qubits i,j use the positive block

    Q_s(i,j;w)=w[n_i+n_j-s(sigma_i^+sigma_j^-+sigma_i^-sigma_j^+)],
    s=+1 or -1, w>0.                                    (1)

Its full-support norm is2w, with spectrum0,0,2w,2w. Let J>0, a_d=J/sqrt(2), g=J and mu=(sqrt(2)-1)J. A gated diamond has physical heads L,u,v,R_d and blocks

    Q_+(L,u;a_d), Q_+(L,v;a_d),
    Q_+(u,R_d;a_d), Q_-(v,R_d;a_d),
    J n_u(I+X), J n_v(I-X),                             (2)

where X=X_D or Z_D on its single ordinary data target. The head terminal R_d is distinct from the data qubit R. Each contact has full norm2J. The identity diamond instead uses X=I, installs only2J n_u and omits the zero v contact; it has five nonzero blocks instead of six and no data qubit support.

The physical arm transform B=(u+v)/sqrt(2), C=(u-v)/sqrt(2) converts (2) to links -J,+JX,-J on L,B,C,R_d. With one ordinary Q_+(J) continuation at each endpoint, every resulting one-head diagonal is2J+mu. No mu term is added to these four diamond heads. Gauging the right side by -X makes the middle link -J, so the scalar comparator is h_0+mu I, where h_0 has diagonal2J and every hopping -J. Its evolution is exp(-i mu t)exp(-it h_0), or directly exp[-it(h_0+mu I)], NEVER both a full shifted evolution and an extra mu phase.

A two-rail Hadamard mixer has heads L0,L1,R0,R1, four Q_s bonds of weight J/sqrt(2) with hopping matrix -J H, H=2^-1/2[[1,1],[1,-1]], and one ordinary exterior bond at every port. Its diagonal is likewise2J+mu without extra onsite terms. A four-rail Hadamard layer consists of two such disjoint mixers, on the chosen path label. A four-rail permutation layer instead has four ordinary Q_+(J) bonds realizing the permutation and mu n on each of its eight port heads. Its diagonal after the exterior bond is also2J+mu. None of these basis changes is an installed instantaneous unitary; they are analytical representations of a static Hamiltonian.

Every block is real, positive, head-number preserving and at most two-body on full qubit support. Every block annihilates the all-head vacuum on arbitrary data. The vacuum scalar is ZERO. The mu shift belongs to the one-head scalar reduction, not to the full Hilbert-space vacuum and not to a freely chosen subtraction on the data.

## 2. Gate layers and exact chronological word

Define CZ_(a,D)=|0><0|_a tensor I_D+|1><1|_a tensor Z_D. A physical four-diamond layer implements -CZ_(a,D) between its left and right ports: two identity diamonds on a=0 and two Z_D diamonds on a=1, duplicated over b. All four scalar chains are identical. Similarly a layer with two X_T diamonds on a=1 and two identity diamonds on a=0 has gate -CX_(a,T), where CX flips ordinary target T when a=1.

The ordered three-layer sequence

    H_a, CZ_(a,D), H_a                                  (3)

has logical word N_(D,a)=H_a CZ_(a,D) H_a, which flips a if and only if D=1. In the PHYSICAL gauge its word is -N_(D,a), because there is one diamond layer. This is a data-to-head-path CNOT derived by rail interference with a two-body Z contact, not an assumed data-controlled head-head hopping.

For distinct ordinary D,T, concatenate chronologically

    H_a, CZ_(a,D), H_a, CX_(a,T), H_a, CZ_(a,D), H_a.      (4)

Ignoring only its explicitly tracked common sign, this is

    F_(D,T)=N_(D,a) CX_(a,T) N_(D,a).

On basis bits it restores a and sends T to T xor a xor D, leaving D unchanged. This calculation holds for BOTH a values. The physical seven-layer word is -F_(D,T), with three diamond signs. Apply three such sequences with (D,T)=(Q,P),(P,Q),(Q,P). Writing the initial bits as a,q,p,

    p1=p xor a xor q,
    q2=q xor a xor p1=p,
    p3=p1 xor a xor q2=q.                               (5)

Thus the 21-layer word is exactly -I_a tensor SWAP_QP, including coherent auxiliary, data and reference states. Intermediate Q/P gates have NOT been commuted or evaluated in global fixed-control sectors.

Append four layers, chronologically,

    H_b, CZ_(b,P), H_b, X_b.                             (6)

Here the controlled-Z layer is identity on b=0 and Z_P on b=1, duplicated over a; X_b is the four-bond permutation layer. The first three logical factors give N_(P,b), the positive-control bit flip. Since X_b N_(P,b) flips b precisely when P=0, define

    C_P^(b)=|0><0|_P tensor X_b+|1><1|_P tensor I_b.

The physical word of(6) is -C_P^(b). Multiplication with the previous minus yields the prefix

    G_pre=I_a tensor[C_P^(b) SWAP_QP].                   (7)

Finally append four gated X_R diamonds, one per rail. Their physical layer gate is -X_R. The complete right-side gauge is therefore

    G_out=-U_f,
    U_f=I_a tensor[X_R C_P^(b) SWAP_QP].                 (8)

There are 26 layers: fourteen four-rail Hadamard layers, ten controlled diamond layers from(4),(6), one four-bond permutation layer and one final all-X_R diamond layer. Equivalently there are eleven diamond layers in total. No adjacent Hadamard cancellation is used to shorten the physical graph. Their identical scalar delays remain installed and counted.

For supplied a=1 and R=0 the basis action is exactly the original direct-loader action

    (b,q,p,0_R) -> (b xor(1-q),p_Q,q_P,1_R),              (9)

with a restored. The scalar minus in(8) is not a changed logical function or a fitted input-dependent phase. Old P and its passive environment remain on Q/environment. The reverse spatial transfer has gate G_out*=-U_f*, generally NOT -U_f.

## 3. Exact global gauge with all physical arms

Connect consecutive layers by four ordinary Q_+(J) bonds, pairing equal physical rail labels. Each cable is ONE graph edge, with no interior head. It supplies the one exterior bond required at both of its module endpoints. The first and final ports attach to ordinary scalar rays. No bypasses, additional data dynamics or undeclared bonds are present.

Apply the head-only arm rotation of section1 independently to all44 physical diamonds. These are rotations in mutually orthogonal one-head coordinate subspaces, even though their ordinary targets are shared. Call the resulting head-basis unitary A. It is not an all-head local physical circuit. Mixer bases are not separately rotated here; they remain explicit unitary-valued hoppings between four-coordinate slices.

There is now a linear sequence of74 virtual positions x=0,...,73, each carrying the four-rail and shared-data fiber. A diamond layer occupies four consecutive slices, a mixer/permutation layer two. Consecutive modules have distinct endpoints, joined by one cable link. The counts are

    11*4+14*2+1*2=74 slices,
    11*3+14*1+1*1+25=73 links.                           (10)

Every diagonal is(2J+mu)I on the full fiber. The forward block from x to x+1 is -J V_x, with V_x equal to I on ordinary/cable/outer diamond links, H_a or H_b on a Hadamard link, X_b on the permutation link, and -X_layer on a diamond B-C link. Here X_layer is a rail-controlled real Hermitian involution, such as CZ_(a,D), CX_(a,T), or the uniform X_R. These layers have the claimed block-diagonal physical realization; writing X_layer is only a representation of the one-head matrix and does not install a three-body block.

Define ordered cumulative unitary gauges

    W_0=I, W_(x+1)=V_x W_x,
    W=direct-sum_x W_x.                                 (11)

Extend W by I on the left rays and by G_out on the right rays. Since

    W_(x+1)* (-J V_x) W_x=-J I,

and every diagonal is scalar, the EXACT identity is

    (A W)* H_one (A W)=(h_0+mu I) tensor I_(rails,QPR),   (12)

with the convention that A maps virtual arm coordinates back to physical heads. The formula fixes the order in every product, including repeated noncommuting Q/P actions. Reverse links are adjoints automatically. At each cable both endpoint gauges agree, so scalar matching requires no gate to commute through a cable. No loops remain in the rotated virtual coordinates; all74 slices and296 physical heads are accounted for.

For a diamond whose prefix is W_pre, its four gauges are

    W_L=W_B=W_pre,
    W_C=W_Rd=-X_layer W_pre.                            (13)

For a scalar profile f_x(t), the PHYSICAL arm vectors are therefore

    psi_u=(f_B W_pre-f_C X_layer W_pre)xi/sqrt(2),
    psi_v=(f_B W_pre+f_C X_layer W_pre)xi/sqrt(2).         (14)

These formulas retain partial gate action on arms, including interference between two different prefix words. It would be false to assert that every internal physical head carries a single completed unitary word. Equation(12), not such an assertion, is the full apparatus identity.

On infinite rays h_0 is the ordinary uniform-chain one-head operator with diagonal2J and hopping -J. It is bounded. The transformation is unitary on this one-head space tensor the finite data fiber and arbitrary passive identities. It makes no boundedness claim for an unrestricted infinite many-head sum. All heads initially blank is still a supplied preparation premise, not a consequence of this one-head identity.

## 4. Exact all-port scattering and spatial events

Use radial n>=0 from each exterior origin. Left origin is virtual x=0, right origin x=73. The full scalar energy is

    E(k)=mu+2J(1-cos k), 0<k<pi.

A left incoming wave has phase exp(ikx); at right radius n it is exp(ik(73+n)). Consequently the exact eight-port scattering matrix is

    S(k)=exp(73ik) [[0,G_out*],[G_out,0]]
        =-exp(73ik) [[0,U_f*],[U_f,0]].                  (15)

The zero diagonal blocks state no reflection on the matched infinite device. Left and right transmission are reciprocal ordered words; the common delay is73 graph edges, not spatial Manhattan length. There is no perturbative eta/zeta or narrow central-band error. The threshold mu and minus in(15) are both retained. At band edges the usual zero-velocity scattering parametrization is not asserted; the exact operator identity(12) still holds.

For a head initially on any left extension coordinate and arbitrary rail/data/reference state xi, let f(t)=exp(-it h_0)|source>. The full state is exactly

    exp(-i mu t) A sum_x f_x(t)|x> tensor W_x xi.         (16)

For any chosen set of right-extension coordinates, including or excluding the right origin as specified, its projection factors as the common restricted scalar profile times -U_f xi. Conditional on nonzero probability, the normalized complete spatial-event channel is exact, including the retained head profile, data and references. Its probability is independent of xi. At zero probability the normalized conditional channel is undefined. No estimate of that probability or useful time window follows merely from its factorization.

Likewise the left-extension event carries I. Intermediate events generally have the physical mixtures(14), not U_f. A spatial right event is therefore a precise all-time gate certificate under the supplied Hamiltonian and initial left state, whereas the record event must be analyzed separately.

## 5. What the actual record-one event does and does not certify

Only the FINAL four diamonds touch data R. Assume R starts0, as in(9). Before this last layer every W_x commutes with R and leaves it0. The last layer occupies virtual slices70,71,72,73 with labels L,B,C,R_d. The prefix is exactly G_pre of(7), with positive common sign because ten diamond layers have preceded it. Therefore

    W_70=W_71=G_pre,
    W_72=W_73=-X_R G_pre=-U_f.                          (17)

On physical final arms, (14) gives a coherent R0 piece from f_71 and an R1 piece from f_72. Direct projection, not an inference from right-side transmission, gives

    P_R1 psi_u=-exp(-i mu t) f_72 U_f xi/sqrt(2),
    P_R1 psi_v=+exp(-i mu t) f_72 U_f xi/sqrt(2),          (18)

where xi has blank R. On every final R_d and right-extension coordinate x>=73 the R1 vector is -exp(-i mu t)f_x U_f xi. On all preceding coordinates and final L the R1 vector is zero. The component of physical arms from virtual B is eliminated because it has R0; it is not presumed to have the completed gate.

Let J_rec embed a virtual scalar coordinate72 as (|u>-|v>)/sqrt(2) in the corresponding final physical diamond, and each x>=73 as its physical head coordinate, retaining the output rail label. Then the exact full branch identity is

    P_R1 exp(-itH_one)E_left,R0
      =-exp(-i mu t) J_rec[(f_72|72>+sum_(x>=73)f_x|x>)
                                           tensor U_f]. (19)

The branch profile is unnormalized. Its probability is

    p_rec(t)=|f_72(t)|^2+sum_(x>=73)|f_x(t)|^2,            (20)

independent of the supplied logical/data/reference state. If positive, its normalized logical operation is EXACT U_f, including old-state/reference retention. This special conclusion is proved by(17)--(18) and requires blank R and the absence of every earlier R contact/free term. It is not a general property of placing a record diamond after an arbitrary network.

Crucial distinction: R=1 does NOT imply that the head has reached an external output ray or that all internal heads are vacant. It may occupy the antisymmetric final-arm combination in(18), and the final origin R_d is also internal. The external-only event is x>=74, with probability sum_(x>=74)|f_x|^2; it has its own exact factorized output profile. Equation(19) is not an assertion that this latter profile equals the record profile. Both can have arbitrarily small probability. Returns can unset the record as the scalar amplitude moves back to earlier slices; no irreversible latch or permanent completion signal is proved. If R is not initially blank, (19) is not the asserted branch contract.

## 6. Actual blocks, shared-data loads and a supplied finite geometry

All counts refer to nonzero installed positive blocks. There are44 diamonds. Of these24 are gated and20 are identity: the ten controlled layers each have two of each kind, and the final layer has four gated. Thus diamond heads=176 and diamond blocks=24*6+20*5=244. Fourteen Hadamard layers each have two mixers, totaling112 heads and112 blocks. The permutation layer has8 heads,4 Q_J bonds and8 mu onsite blocks. Twenty-five interlayer gaps each have four cable bonds, adding100 blocks and no heads. In total, before exterior rays,

    heads=296, ordinary data=3, total qubits=299,
    positive blocks=244+112+12+100=468.                 (21)

More explicitly there are392 head-head blocks,48 head-data contacts,20 identity-diamond onsite blocks and8 permutation mu onsite blocks. No zero contact is counted. All port exterior bonds are provided either by the100 cable bonds or the eight exterior attachments; they are not included twice in the module count.

The ordinary-data incident loads count every repeated target. Q participates in four CZ_(a,Q) layers and one CX_(a,Q) layer: ten gated diamonds, hence20 norm-2J contacts and total40J. P participates in two CZ_(a,P) layers, two CX_(a,P) layers and the final CZ_(b,P) layer: likewise40J. R participates only in four final diamonds, for load16J. These are full-support sums, not expectations in one-head states. Their neighbor degrees are20,20,8 respectively.

Each diamond endpoint has load4a_d+2J=(2sqrt(2)+2)J after its single exterior bond; gated arms have4a_d+2J, identity u the same, and identity v only4a_d. Hadamard ports have the same(2sqrt(2)+2)J bound. Permutation heads have4J+mu=(3+sqrt(2))J. An ordinary exterior head with two ordinary bonds and its supplied mu n has4J+mu. Thus J<=Lambda/40 satisfies an incident full-support cap Lambda before any permitted endpoint modification whose load is separately checked below. No balancing or scalar subtraction reduces these physical loads.

A finite-range cubic-lattice placement is explicit. Put the299 internal qubits in {0,...,6}^3, reserving eight ports(i mod4,floor(i/4),6), i=0,...,7 in left/right lexicographic(a,b) order. Assign291 remaining graph vertices to291 of335 remaining cube sites in a fixed order, leaving44 unused sites. Every internal pair has Manhattan length at most18, since each coordinate difference is at most6. Attach ray i at(i mod4,floor(i/4),6+n); the eight distinct horizontal coordinate pairs make them disjoint, and n>=1 puts them outside the cube. Consecutive ray bonds are nearest neighbor. This supplies range18 by exact qubit permutation. It is not a nearest-neighbor graph realization: Q/P degree20 exceeds six. Spatial crossings do not create interactions; absence of undeclared nearby couplings is still supplied. No optimality or native coefficient claim follows from this elementary embedding.

## 7. A finite scalar extension identity, without performance inheritance

One concrete finite installation illustrates the boundary bookkeeping. For integer ell>=1, put a source at M=ell+1 on each selected left a=1 ray. Install ell ordinary Q_J bonds followed by

    Q_gamma(ell,M)+(J-gamma)n_ell+(2J-gamma)n_M,
    0<gamma<J.                                         (22)

On the two unused left rays and all four right rays install ell ordinary bonds and cap J n_ell. Add mu n to EVERY added exterior head, including both emitters and all six cap heads. Do not add it again on diamond/Hadamard ports; the permutation ports already have their separately counted mu terms. Every added head then has one-head diagonal2J+mu, and the only source-modified hopping is -gamma. Full-support source norm is3J, before the separate mu onsite term.

Counts for this particular extension are

    physical heads=298+8ell, qubits=301+8ell,
    positive blocks=478+16ell.                          (23)

The added source/cap blocks contribute8ell+8 and the added mu terms8ell+2, on top of468. Sources replace their final ordinary bond. Source emitter load3J+mu, source neighbor5J+mu=(4+sqrt(2))J, and cap load3J+mu all remain below40J; thus the same J<=Lambda/40 suffices. All these terms have zero vacuum energy.

Equation(12) remains exact with this finite scalar operator, but its left a=0 and a=1 terminations differ. It would be inaccurate to call all four finite chains identical. After the gauge, the two selected a=1,b chains are identical scalar chains with the compensated weak source on the left and a cap on the right; the unused a=0 chains have different scalar left caps. The scalar operator does not mix rails. For input restricted to a=1, the latter chains stay vacant in the gauged representation. The right boundaries are identical on all four rails, and U_f preserves a, so the gauge is compatible with the finite endpoints.

Hence for the selected coherent two-emitter input the exact common scalar profile is generated by one finite chain h_fin, with emitter coordinate -ell-1, left origin0, final origin73 and right cap73+ell. Its distance from source to final cap is2ell+74. Define h_fin WITHOUT mu, with diagonal2J, the one weak source edge -gamma and all other edges -J. Then all complete-state and event identities above hold with f=exp(-it h_fin)|-ell-1> and the SINGLE factor exp(-i mu t). This is a finite-dimensional unitary identity, not an approximation with omitted localized states or a normalized incoming-packet assumption.

No asymptotic packet, finite output probability, observation window, epsilon-dependent ell/gamma policy or runtime is derived here. Such a calculation may now be a purely scalar finite-chain problem, but it must be proved for the actual endpoints(22), lengths and output sets. Old approximate-router or direct-loader performance bounds are not transferred. The algebra also does not prepare the coherent emitter input, R0 or the rest vacuum, nor does it prove a combined receiving-apparatus interface.

## 8. Exact premises, review status and exposure

N is /Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934.

- `exact_two_body_gate_diamond/PROPOSAL.md`:7fa888681833216ded21fab0028f18ad079fde94b7f884a391c83196fb5a3e33; accepted distinct `exact_two_body_gate_diamond_check/REVIEW.md`:da5cbc9bcb0f66442da600191c4b863ed7c22a5a4bba0d024a0c683cf71b1945. Both complete texts were read here. Only the exact physical diamond and its one-head conjugacy/full-support norms are adopted, not a finite performance theorem.
- `exact_two_body_gate_matched_extension/PROPOSAL.md`:a1157d95d06e7eeced6217ec2fb7b43247619a74cd9aded3eeb811a68ba6075e, with accepted distinct `exact_two_body_gate_matched_extension_check/REVIEW.md`:36a1f3585c9ddde455078c72e7f48dc2b2cd8bfd1165026f4d3f60c6dbc6c77f, read completely and hash verified before this freeze. The original75a0a4a77db138f4ee2bbd1cc5b1c42ecf2a4e9f767573e352f2b72478d8a2f6 is retained as `PROPOSAL_original_75a0.md`. The full original argument and exact correction were read; the correction defines h_uniform with diagonal2J and forbids double-counting exp(-i mu t). The corrected convention is explicitly reconstructed in sections1,3,7.
- Original direct-loader source89489c13a6450f142c8ac2212ee680bc7272addcff30c53fcb01e52dff4ee7a9 and checked finite1b168c4ac2e606ee3905c104f90879fe5731c9113318e37566add92f681dd77b are prior full-read context for the desired U_f and the supplied endpoint block family. Their approximate gate matrices, packet, resource and branch bounds are NOT premises of this exact construction. The finite block identity(22) and all changed counts are directly rebuilt here.

ROOT supplied the matched-diamond/mixer route and requested a full ordinary SWAP composition after the base diamond review. ROOT also suggested the range18 cube after the299-qubit count was established; section6 verifies its injection and rays directly. The author has substantial prior core/writer, source, jet and finite-resource ancestry. This is exposed same-model author work, not an independent check of ROOT's primitive or blind discovery. In particular the new ordered word, all-arm gauge, full finite-domain matching, record projection and counts need a distinct check. Acceptance of an exact primitive does not by itself accept their composition.

Only this PROPOSAL.md was created. No scientific executable, solver, simulation, sweep, delegation, W/Git/checkpoint/axiom/editable-prompt/model change or publication occurred. No editable prompt changed. The proof is analytical; no numerical PASS evidence is claimed. No native Hamiltonian, robustness, physical initialization, cooling, permanent halt, capture/reset or active old-processor theorem is asserted.
