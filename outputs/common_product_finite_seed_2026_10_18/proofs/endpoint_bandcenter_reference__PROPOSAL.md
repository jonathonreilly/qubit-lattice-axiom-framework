# Band-center endpoint reference: conditional interface and path-parity obstruction

Status: new analytical discovery assessment, not an independently checked construction or new runtime theorem. A shared structural emitter diagonal 2J gives a useful band-center reference contract. It does not yet remove the physical supplier obligation. The suggested one-extra-step phase replacement fails within the current shared-source cubic-nearest-neighbor Hadamard-square architecture because the relevant path lengths must have equal parity. This is a restricted geometry obstruction, not a no-go for other real positive scattering structures.

## Sources and exposure

Current canonical note read for exact internal B/K/W, bare matching, filter, shared-system junction and physical layout definitions: /Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/correlation_worktree/docs/REAL_ENDPOINT_AUTONOMOUS_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md, refreshed SHA256 d17d5e32f3f44f162aff15ced734238ba1543212525d618d36dc95511095c4be. Root reports PR9668 milestone 7dcc98203477cf9868dc9b7f7dd2aeccffeda9a3; this task did not verify the Git association. Earlier endpoint/spectral and precision sections were read in preceding tasks; this task does not independently certify concurrently added material.

This is source-exposed development. I authored the older weighted estimate and reviewed component/precision arguments. No scientific execution, parameter sweep, numerical matching, new agent, model/effort change or W/Git/PR/checkpoint/prompt edit occurred. Only source reads/hashing and this proposal write occurred. The existing interval calibration at k0=2 arctan(1/4.510351185997098) is not imported at pi/2.

## 1. What band center would accomplish algebraically

Take the real lead dispersion E(k)=2J(1-cos k), k*=pi/2 and E*=2J. Suppose a structural implementation enforces the emitter diagonal to equal the SAME 2J as the lead center while allowing a weak real hopping -kappa to vary. A positive local block can express the required correlation:

    B_local=2J|10><10|+J|01><01|
      -kappa(|10><01|+|01><10|)+3J|11><11|,
    B_local|00>=0.

For 0<kappa<sqrt(2)J this is positive on the entire two-qubit space: the one-excitation determinant is 2J^2-kappa^2>0 and both diagonals are positive. It equals Q(-kappa)+(2J-kappa)n_e+(J-kappa)n_end when kappa<J. The endpoint's other bond supplies its second J. The block is real, number conserving and nearest neighbor; no new ancilla or rotated seed is required.

This is an exact supplied matrix family, not proof that separately uncertain occupation terms will obey the correlation. If its 2J diagonal and the lead's 2J originate from independent controls, their mismatch remains an emitter detuning. A single shared symbol J in a Hamiltonian is not by itself a physical primitive enforcing a common reference. Moreover arbitrary changes in J would change propagation, source ratios, old relative phases and the nominal waveform; no complete fixed-target robustness to such changes follows.

For an ideal free endpoint reference,

    D_ref(k)=E(k)-2J+(kappa^2/J)exp(ik),
    D_ref(pi/2)=i kappa^2/J.

The real resonance shift vanishes at the center for every kappa. Writing k=pi/2+s gives Re D_ref=(2J-kappa^2/J)sin s and Im D_ref=(kappa^2/J)cos s. Thus the centered line remains narrow, with momentum scale approximately kappa^2/(2J^2), even though its center can be structurally tied to the lead. A residual independent emitter offset Delta still enters as -Delta; its ratio to kappa^2/J still controls fixed-waveform sensitivity. Band center removes the need to choose an unrelated nominal E0 only IF the common diagonal relation is supplied exactly or with an appropriate correlated error contract. It does not broaden the resonance.

The actual endpoint self-energy is not automatically the free value. With an input termination of length ell its scalar comparison is

    g=-(z/J)(1+R_bg z^(2ell))/(1+R_bg z^(2ell+2)).

At z=i, even nonzero R_bg can create a real self-energy part. A new reflection-cancellation theorem is therefore still required, as are bounds for the full eight-coordinate Schur correction. Small or zero free real shift cannot be substituted for a proof about actual Gjj.

## 2. Why a one-step delay looks attractive on an abstract graph

For two otherwise identical reflecting arms viewed at the same port planes, a free path-length change d multiplies their reflection ratio by exp(2ikd). With d=1, at pi/2 this equals -1. Equivalently the one-way free phase is i. Under the real Hadamard mixer U, exact opposite reflections give

    U diag(r_g,-r_g) U^T=[[0,r_g],[r_g,0]].

Near pi/2 the ratio differs from -1 by O(|k-pi/2|), with no cos(k) denominator. This is the correct round-trip mechanism; merely changing a hopping sign on a tree is a gauge change and does not give it. Absolute reference planes still matter, including the phase of the transmitted common waveform.

If realizable, this would remove the present singular phase-filter parameterization u=-J/cos k0, t=J sin k0/cos k0. Neither that formula nor its inverse constants can be evaluated or continued to pi/2. The delay is a genuinely different architecture, not its limiting filter.

## 3. Exact parity obstruction in the present cubic layout

Color the cubic lattice by x+y+z modulo2. Every allowed nearest-neighbor edge reverses color. Hence every path between fixed endpoint colors has the same length parity, regardless of detours, edge signs or positive diagonal compensation.

Both arm c0 contacts couple to the SAME physical source A by nearest-neighbor interactions. They are therefore both neighbors of A and have the same color. The two arm-end sites in the real Hadamard junction are each connected to both port-start sites: its graph is K2,2, physically the square specified in the note. Thus the two arm ends also have the same color. Every arm path from its c0 to its arm end consequently has the same parity as the other arm's path. Their length difference d must be even.

At k=pi/2 an even d yields exp(2ikd)=exp(i pi d)=+1. Any ordinary detour retaining these contact and mixer incidences cannot supply the required opposite reflection. Inserting one extra vertex along only one arm edge is not a cubic-NN embedding with the endpoints fixed: that would replace an odd-length connection by an even one between opposite colors. Hopping signs do not change this parity and a tree sign cancels on the return trip. Two extra steps give one-way -1 but round-trip +1, so they do not fix the issue.

This argument uses the shared A contact and K2,2 mixer incidence, not the particular long coordinate route or its 45-site count. Moving the sites while preserving those incidences does not avoid it. Source B's corresponding shared c1 contact is consistent with the same constraint. It does not prohibit a different real positive scattering cell, changed mixer topology, altered contact architecture, or a non-cubic/non-NN model. Such changes need their own proof and cannot be described as the current graph plus one delay step.

## 4. Shared-source and old-operation interfaces still missing

Even an abstract successful delay supplies only opposite arm reflections. It does not supply the desired old W. The retained literal identities are

    K=2I+Z1Z2,
    B=K+Csrc+Gsrc, B iota=iota K,
    W=[(9+12i)I+(-16+12i)X1X2]/25,
    omega_+=(-7+24i)/25, omega_-=1.

The source vacuum must remain |00> and the four real old vectors retain energies b_j=1,3 and parity p. One shared old pair and one source pair must serve both clock arms; duplicating internal registers would change the comparator. The head-coordinate mixer may commute with B because it acts only on head positions, but [full H,K]=0 is neither true nor required.

At band center the exact four matching matrices would instead be evaluated at lambda_j=b_j+2J:

    M16=[[lambda-2J-B-VA, JI8],
         [JI8, -JQ^-1-VB]],
    Q_open=i, q_l+q_l^-1=(2J+b_l-lambda)/J.

The new load-bearing requirement is a single common scalar phase rho_*(k) such that all four bare reflections satisfy r_j(k) approximately rho_*(k) omega_p, with explicit complex errors on a nonzero interval around pi/2. Four separately fitted phases would not implement the same W. No value, inverse bound, derivative bound or central residual from the old k0 certificate establishes this new calibration. Real Hamiltonians can have complex scattering phases at a positive interior-band energy, so reality alone is not an obstruction to W; conversely positivity alone does not enforce the required phase ratios.

Threshold separation must be rechecked. The old source positivity suggests room: nonvacuum B>=1+Delta_min>3.1868, while the higher vacuum channel's center lambda is 3+2J<3.062. This is only a starting free-channel separation, not the old .17 gap or an interacting-core inverse bound. Every closed root and seven-coordinate complement still needs its band-center enclosure.

After successful bare calibration and a physically admissible opposite-reflection cell, reconstruct: the shared-system two-port kernel at consistent planes; terminated input Green matrix and outgoing row; actual scalar and complementary emitter Schur inverses; local Stone normalization/synthesis and all omitted mass; common complete complex target; full localized core/source/emitter and closed-tail escape; both hard-cutoff sides; old-column/reference aggregation; and finite radius/geometry transfer. No T/M or error from the current device transfers merely by replacing E0 with2J.

## 5. Decisive next obligation and limited candidate

The useful surviving candidate is the fixed-diagonal positive endpoint family in section1, conditional on a genuine shared 2J reference. Its precise endpoint reference algebra can be reused if a band-center gate/scatterer is built. It does not yet solve the scattering construction or native precision supply.

The simplest proposed phase implementation, a one-extra-step path under the present shared contacts and Hadamard square, is ruled out by the exact parity argument. A resource-consuming recalibration of that unchanged-delay proposal would therefore be premature. The next load-bearing design obligation is to exhibit a real positive cubic-NN two-port cell with matched transmission and relative phase i at pi/2 while respecting the shared internal contacts, or to explicitly change the incidence architecture and prove what that change preserves. This is a finite exact scattering/geometry obligation, not a parameter sweep. A candidate should first provide its exact physical block, common reference planes and band-center scattering matrix, including closed-channel coupling; only then should the four-column W calibration be reconstructed.

No general impossibility or optimality claim is made. In particular this assessment neither grants a structural supplier for 2J nor proves that every band-center architecture fails. It identifies exactly why the proposed path shortcut fails in the current layout and which independent interfaces a useful successor must supply.
