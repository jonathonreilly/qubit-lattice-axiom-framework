# Exact positive two-body diamond: distinct algebra check

Disposition: SUPPORT for the exact one-head conjugacy and its stated left-to-right conditional channel. No required algebraic correction found. This is an exact supplied-component identity, not a transmission-probability, finite-window, geometric realization, or composed-circuit theorem.

## Source, exposure and scope

Completely read and hash-verified `exact_two_body_gate_diamond/PROPOSAL.md`, SHA256 `7fa888681833216ded21fab0028f18ad079fde94b7f884a391c83196fb5a3e33`, under `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934`. ROOT authored the proposed matrix before this review. I saw that proposal and independently reconstructed the physical-coordinate matrix, transformed entries, operator conjugacy and event map below. This is source-exposed, same-model checking, not blind replication or formal retained audit.

I previously checked the direct-loader stationary and finite constructions and authored or reviewed related writer/router ancestors. Those finite/scattering results are NOT premises of this identity. The older writer `autonomous_record_route/PROPOSAL.md`, SHA256 `93445d7d52e32859c980f0a0ebc6024238bedc7571d09e145ab1b128d8292f56`, has a complete prior read; its relevant signed-junction/contact argument was inspected again for overlap. It supplies context, not a needed lemma. The present proof is direct finite-dimensional algebra.

The equation involving W is a statement on the one-head sector, where B and C are head-position basis vectors. It is not an all-head physical basis change or a claim that W is itself an installed local operation. Full-support positivity and norms are separate assertions checked next. X is the stipulated real Hermitian involution, in particular X_D or Z_D; the norm equalities for both contact blocks use the presence of both eigenvalues. The separate identity specialization is addressed below.

## 1. Full-support six-block construction

In the ordered head-pair basis 00,10,01,11,

    Q_s = 0 direct-sum a[[1,-s],[-s,1]] direct-sum 2a.

The one-head eigenvalues are 0 and 2a, for either sign s. Thus Q_s is positive on the whole two-qubit support, with norm 2a, and annihilates the local vacuum. In particular changing the hopping sign does not create a negative full-support block.

For a contact g n_u(I+X), the n_u=0 block vanishes and the n_u=1 block has eigenvalues 0 and 2g. The minus contact has the same spectrum with the two X eigenspaces exchanged. Both are positive of norm 2g, real for the stipulated X, and act on exactly one head qubit and D. They do not supply a three-body head-head-data hopping. Every block commutes with total head number, and every block annihilates the entire head vacuum for every data/reference vector. There is no scalar vacuum energy or unmentioned free data evolution in this inventory.

There are four head-head blocks and two head-data blocks on five physical qubits. Summing actual full-support norms at each vertex gives 4a at L and R, 4a+2g at u and v, and 4g at D. These are incident sums, not the norm of their combined restriction to one head. External blocks add their own incident norms; no cap is automatic without choosing a,g and the extension loads. The supplied graph is not by itself a demonstrated cubic nearest-neighbor layout. No such embedding is claimed by the source.

## 2. Reconstruction before and after the arm rotation

In physical head coordinates L,u,v,R the one-head operator is

    H1 = [[2a I, -a I, -a I, 0],
          [-a I, (2a+g)I+gX, 0, -a I],
          [-a I, 0, (2a+g)I-gX, +a I],
          [0, -a I, +a I, 2a I]].

Each diagonal 2a is the sum of its two incident Q-block occupations. The positive v-R hopping comes from Q_-, while both L-arm hoppings and u-R are negative. These signs are decisive.

Use the real orthogonal arm change B=(u+v)/sqrt(2), C=(u-v)/sqrt(2). The L-B coupling is -sqrt(2)a and L-C is zero. The R-B coupling is zero and R-C is -sqrt(2)a. Conjugating diag(gI+gX,gI-gX) by this arm rotation gives gI on both central diagonals and gX on both off-diagonals. This yields precisely the proposed four-site matrix, including the common central g term.

In the following conjugacy formulas H1 denotes this same operator represented in the L,B,C,R basis. Writing W_L=W_B=I and W_C=W_R=X, a transformed block is W_i* H1_ij W_j. The B-C block becomes g X X=gI; the C-R block becomes -sqrt(2)a X X=-sqrt(2)a I. The L-B block is unchanged. All four diagonals are scalar and unchanged. Hence

    W* H1 W = h tensor I_D,
    H1 W = W(h tensor I_D),

with h's links -sqrt(2)a,+g,-sqrt(2)a and diagonals 2a,2a+g,2a+g,2a. W is unitary and self-adjoint. This is exact for every a,g>0, with no expansion or chosen energy. Tensoring an arbitrary passive reference identity preserves it. Exponentiating gives exp(-itH1)=W(exp(-ith) tensor I)W* for every real time.

The identity genuinely depends on the displayed symmetry. For example, an extra physical delta*n_u adds delta/2 to both transformed arm diagonals and delta/2 I to their off-diagonal. That extra central term becomes delta/2 X under W and destroys the scalar conjugacy for nontrivial X. Equivalently it adds a^2 delta I to the third-order R-L matrix element. Thus the calculation is not an identity that would survive arbitrary arm perturbations, and it is not a fabrication-robustness certificate.

## 3. Short-time sign and phase

There is no L-R edge. The two length-two contributions are (-a)(-a)=a^2 and (+a)(-a)=-a^2, so (H1^2)_RL=0. At third order, endpoint diagonal contributions cancel because they multiply the same two opposite path products. The central occupations give

    (H1^3)_RL
       = a^2[(2a+g)I+gX] - a^2[(2a+g)I-gX]
       = 2a^2 g X.

This also equals the three links of the transformed Jacobi chain. The evolution amplitude therefore begins

    <R|exp(-itH1)|L> = i a^2 g t^3 X/3 + O(t^4).

The sign is positive i because (-i)^3=i. The order-zero, order-one and order-two amplitudes vanish. The leading small-time right-terminal probability is a^4 g^2 t^6/9. This last observation establishes nonzero transfer at sufficiently small nonzero times in the isolated finite component, but says nothing useful about large success probability or a transfer window.

The exact scalar amplitude retains the full h evolution, including its endpoint and central diagonal phases. There is no freedom to drop the g diagonals, fit a separate column phase, or identify this amplitude with a uniform-chain propagator.

## 4. Allowed extensions and complete state

An added scalar onsite term at an extension coordinate commutes with its W factor. A scalar hopping between two left-extension coordinates transforms with I on both ends; a hopping between two right-extension coordinates transforms with X on both ends and remains scalar. The attachment to L or R has the same property. Thus finite data-independent extensions on their indicated sides preserve the conjugacy, with h enlarged by precisely those scalar terms. An infinite bounded/self-adjoint lead extension also permits the same identity on its operator domain; no unbounded arbitrary extension is needed for the finite claim.

A direct scalar link between an I-gauged coordinate and an X-gauged coordinate instead transforms to a link carrying X. It is an excluded bypass. Arbitrary additional data terms or asymmetrical terms on the physical arms are likewise not licensed by the extension sentence. The source's scalar onsite/coupling permission concerns the extensions attached to L and R; it does not authorize arbitrary independent u/v onsite changes. This preserves the stated restrictions without treating spatially nearby but uninstalled couplings as present.

For an initial left coordinate x, W* acts identically on the input. Write f(t)=exp(-ith)|x>. The complete state is then

    sum_left f_y |y> tensor psi
      + f_B |B> tensor psi + f_C |C> tensor X psi
      + sum_right f_y |y> tensor X psi,

with internal endpoints grouped consistently and passive references left untouched. In physical arm coordinates the two internal vectors are (f_B psi+f_C X psi)/sqrt(2) and (f_B psi-f_C X psi)/sqrt(2), exactly as claimed. These vectors can entangle head position and data. The complete apparatus is not generally a common head factor times X psi, and internal head occupancy is not a success event supplied by this identity.

The same statement holds for an initially supplied fixed coherent left-head profile independent of the data, by linearity. No such profile preparation or endpoint-launch quality is proved here.

## 5. Exact rare right-event statement

Let Pi_right be the physical head-position projector onto the designated right extension including R, tensored with identity on D and the passive reference. It is not a separately chosen record-bit projector. Then

    Pi_right exp(-itH1)(|x> tensor psi)
      = f_right(t) tensor (X tensor I_ref)psi.

Its probability p_right=||f_right(t)||^2 is independent of psi. If p_right>0, division by its positive square root gives the common normalized head profile f_right/sqrt(p_right) and EXACT data/reference action X tensor I_ref. For arbitrary mixed data/reference input rho the unnormalized output is

    |f_right><f_right| tensor
        (X tensor I_ref) rho (X tensor I_ref).

Thus the normalized data channel is exactly unitary whenever the event is nonzero, even if its probability is very small. This is stronger than a small absolute branch-error estimate precisely because the branch factors exactly; there is no division of an approximate error bound by a tiny success probability. At zero probability the conditional channel is undefined, as the source specifies. Tracing or retaining the normalized right-head profile leads to the same data channel. The left sector similarly carries I. No physical measurement implementation, successful-event frequency, or permanent later isolation is implied.

## 6. Identity lane, primitive overlap and open performance

For X=I the u contact is 2g n_u and the v contact is zero and can be omitted. The surviving contact has norm 2g; the omitted block must not still be counted as a nonzero norm-2g block. The physical head operator is data-free, but its B/C rotation has exactly the same scalar h, now with W=I. This proves algebraic equality of scalar gated and identity lane dynamics at their L/R coordinates. It does not prove a multi-rail global word, because shared data operations and intermediate branch bases may not admit one compatible global W.

The older 24-head writer already uses positive signed exchange bonds, a Hadamard arm rotation and positive n_T(I+X_R) contacts. The present n_v(I-X) contact belongs to the same supplied positive contact family, with the sign reversed by a data basis conjugation for X_D. Therefore the broad use of interference and head-conditioned positive two-body contacts is not new merely because this component is called a diamond. The new bounded calculation here is the exact four-coordinate scalar Jacobi conjugacy and resulting all-time spatial-event action. The old writer's center-energy scattering and finite-band bounds neither prove nor are required for this identity.

The source correctly leaves scalar matching open. If a=j/sqrt(2), g=j, the central diagonal is (sqrt(2)+1)j, whereas the uniform chain value would be 2j. Uniform lead attachment adds its own endpoint diagonal as well. No exact matched transmission, common multi-stage delay, finite product-seed theorem, normalized outgoing-window theorem, readout/capture/reset, native block realization or continuously coupled receiving-device interface follows without additional analysis. The given algebra is compatible with reflection and arbitrarily small right-sector probability.

Only this REVIEW.md was written. Work was analytical reconstruction plus source reading, text search and deterministic SHA256/directory bookkeeping. No scientific executable, simulation, solver, sweep, Git/publication/W/checkpoint/axiom/editable-prompt change, delegation or model override occurred. No editable prompt file changed.
