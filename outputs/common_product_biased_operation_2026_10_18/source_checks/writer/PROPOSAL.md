# Local inelastic scattering of the positively biased record writer

New bounded author proposal requiring distinct review. For the literal 24-head writer, a small positive record bias has a controlled full-channel stationary effect proportional to kappa/j, independently of elapsed time. The outgoing record-1 channel has a different momentum and must be compared with an inelastic target. This is only a local stationary component result: no finite-seed, complete-router, initialization-temperature improvement or runtime result is asserted.

## 1. Literal physical object and energy convention

Retain writer93445 exactly: two 11-head arms, two port heads, ordinary hopping -j, arm1 phase bonds -sqrt(2)j at edges 2 and 5, their positive occupations, the signed attachment-port matrix -jU with U=2^-1/2[[1,1],[1,-1]], four junction vacancies, and terminal contacts j n_T(I+X_R). There is one shared record R. Append infinite ordinary positive j leads at both ports for this scattering calculation. Add the single physical onsite positive block kappa n_R, kappa>=0, ONCE. It is not a sum of one bias block per head or per lead.

The actual common vacancy scalar remains c_R=4(sqrt(2)-1)j. The head-vacuum action is now c_R I+kappa n_R, NOT a scalar on the record. We subtract only c_R I. If this writer is used inside an apparatus with uniform head chemical potential mu N, then on its one-head space mu is a further common energy shift: physical total energy is c_R+mu+j e. The formulas below use the relative dimensionless energy e after these stated scalar shifts. The bias is never absorbed into a common scalar.

Let H_int be the dimensionless 48-by-48 internal head/record matrix at zero bias, with external lead hoppings removed but their occupation contribution 1 retained at each port. Its 24 head indices are arm0 0..10, arm1 11..21 and ports 22,23. Ordinary diagonals are 2, phase-site diagonals 3, terminal diagonals 2I+X_R; the hoppings and junction signs are as above. This is the full record matrix. The zero-bias X_R decomposition is used only to import its proved inverse bound, not to diagonalize the biased problem.

Let E_P embed the two-port/record space C^2_port tensor C^2_R into the internal space. Let P=E_P E_P*, and let R_int=I_24 tensor n_R. Write r=kappa/j. The internal bias is r R_int, while the external leads have the same record threshold r. Both contributions must be included.

## 2. Controlled two-open-channel domain

Take

    |k-pi/2|<=h<=10^-3,  0<=r<=10^-3,
    e=2(1-cos k),
    k_0=k,  k_1=q=arccos(cos k+r/2),  0<q<pi.           (1)

Thus e=2(1-cos q)+r. Both record thresholds are open; explicitly e and e-r lie strictly between 0 and 4. Since |cos k|<=.001 and r/2<=.0005, |cos q|<=.0015. In particular both momenta lie within .002 of pi/2 and their sines exceed .99. The entire interval between them has sine above .99. The mean-value theorem then gives

    0<=k-q<=r/(2*.99)<r,
    |exp(iq)-exp(ik)|<=r,
    |sin q-sin k|<=r.                                    (2)

These deliberately loose constants cover endpoints uniformly. Define diagonal channel operators, identical on both ports,

    Z=I_port tensor diag(exp(ik),exp(iq)),
    J=I_port tensor diag(sin k,sin q),
    Z_0=exp(ik)I_4, J_0=sin(k)I_4.

Thus .99I<J<=I. The incoming R=0 kinetic energy is E_0(k)=2j(1-cos k), while the outgoing R=1 kinetic energy is E_0(q)=E_0(k)-kappa. It would violate energy conservation to keep q=k at positive kappa.

## 3. Exact finite outgoing matrix and scattering formula

The four-component lead wave at radius n>=0 is

    psi_n = diag(exp(-ik_a n)) f + diag(exp(ik_a n)) b.

Its boundary value is psi_0=f+b, and the exact lead relation is

    psi_1=Z psi_0+(Z^*-Z)f.

Therefore the full biased outgoing matrix and solution are

    L_r(k)=H_int+r R_int-eI-E_P Z E_P*,
    G_r=L_r^-1,
    u=-2i G_r E_P J f,
    b=E_P* u-f.                                          (3)

The sign is -Z, as in the pinned zero-bias outgoing convention. The matrices in (3) act on all 48 internal coordinates; no conserved X_R sector is presumed.

Flux is proportional to f*Jf or b*Jb, since the physical velocities are v_a=2j sin k_a. With a=J^(1/2)f and b_flux=J^(1/2)b, the exact flux-normalized scattering matrix is

    S_r(k)=-I_4-2i J^(1/2) E_P*G_r E_P J^(1/2).           (4)

The omitted common factor sqrt(2j) in both flux amplitudes cancels. The corresponding internal map for this convention is -2i G_r E_P J^(1/2). Self-adjointness of the internal matrix and Im L_r=-E_P J E_P* imply conservation of total incoming/outgoing current; equivalently the inverse identity for G_r and G_r* inserted in (4) gives S_r*S_r=I_4. Thus (4) is unitary on all four open channels. This is not ordinary unweighted amplitude unitarity when k differs from q.

## 4. Explicit full-matrix perturbation bound

At r=0 the record-X unitary diagonalization gives the two checked L_x(k) matrices. Their inverse norms are each below 10 on |k-pi/2|<=.001. Orthogonal recombination therefore yields ||G_0||<=10 on the full 48-dimensional space, with no record dimension factor. No biased-sector decomposition is made.

The actual perturbation includes both the internal bias and external threshold:

    L_r-L_0 = r R_int-E_P(Z-Z_0)E_P*,
    ||L_r-L_0||<=2r.                                     (5)

Neumann inversion and the resolvent identity give, uniformly on (1),

    ||G_r|| <= 10/(1-20r) <= 500/49 <11,
    ||G_r-G_0|| <= ||G_r|| 2r ||G_0|| <=220r.              (6)

Every denominator is positive. This establishes invertibility for the actual noncommuting 48-by-48 matrix, rather than extrapolating from scattering unitarity. For D=J^(1/2), D_0=J_0^(1/2), the scalar square-root identity and (2) give ||D-D_0||<=r, while ||D||,||D_0||<=1. Expanding

    D E_P*G_r E_P D-D_0 E_P*G_0 E_P D_0
      =D E_P*(G_r-G_0)E_P D
       +(D-D_0)E_P*G_0 E_P D
       +D_0 E_P*G_0 E_P(D-D_0)

yields the explicit conservative estimate

    ||S_r(k)-S_0(k)|| <= 480r.                            (7)

All norms here are operator norms, also valid after tensoring any passive reference. An optional internal bound in this flux convention is ||-2iG_r E_P D||<=22 and its difference from -2iG_0 E_P D_0 is at most 460r. These are stationary amplitudes only, not finite-time integrated internal occupations.

The pinned zero-bias writer has the coherent full-port/record bound

    ||S_0(k)-phi(k)X_port tensor X_R||<=33|k-pi/2|,
    phi(k)=-i exp(22ik).

Consequently the new exact local inelastic matrix obeys

    ||S_r(k)-phi(k)X_port tensor X_R||
       <=33|k-pi/2|+480 kappa/j.                          (8)

The port-origin phases are the same as the pinned writer. At k=pi/2, phi=i. Equation (8) compares flux-channel coefficient spaces at the SAME total energy; it does not identify their spatial waves or dispersions. The estimate is sufficient, not optimal, and becomes loose near the top of the displayed r domain. To make the additional local stationary coefficient error at most a chosen d, it suffices that r<=min{.001,d/480}. This local statement alone does not authorize such a choice in the finite apparatus.

## 5. Correct outgoing inelastic packet candidate

For an R=0 incident column with ordinary incoming amplitude one, the ideal record-flipped outgoing coefficient in ordinary spatial amplitude is

    b_1(k)=sqrt(v_0(k)/v_1(q(k))) phi(k),
    v_0=2j sin k, v_1=2j sin q.

Thus a smooth compact-band incident spectral amplitude g(k), including any supplied launch phase, would have ideal outgoing R=1 radial sequence

    B_n^(inel)(t)=(1/sqrt(2pi)) integral
       exp(i n q(k)-it E_0(k))
       sqrt(v_0(k)/v_1(q(k))) phi(k) g(k) dk.             (9)

The overall exp[-it(c_R+mu)] is restored when relevant. Formula (9) already contains the record's energy cost: E_0(k)=E_0(q)+kappa, so it could instead be written with exp(-it kappa) and the output kinetic energy, but q remains different. Such rewriting is not a global phase fit that recovers the old packet. The launch phase is expressed in the INCOMING k coordinate and must not silently be replaced by q.

Differentiation of the energy relation gives q'(k)=v_0/v_1>0. Under p=q(k), the Fourier coefficient of (9) is phi(k(p))g(k(p))/sqrt(q'(k(p))). Its L2 norm on the full integer lead is exactly ||g||_2 by change of variables and Parseval. This explains the velocity square root and its direction. Using its reciprocal, or omitting it, would give the wrong spectral normalization. Applying the same argument to each outgoing record channel shows that (8) integrates into the same coefficient-error bound for outgoing full-line asymptotic packets, with no phase fitting, when identified by their channel Fourier transforms.

This elementary normalization of a proposed outgoing sequence is NOT normalization/completeness of the complete physical packet containing incoming and internal pieces. A physical packet theorem must construct those pieces from (3), verify exact Schrödinger evolution and norm, and prove the relevant early/late separation in the new channel coordinates. It must also specify the coherent incoming-channel spectral representation if both record channels are populated. Only the R=0 incidence formula is displayed in (9); the full stationary matrix (4) already covers both incoming channels at fixed total energy.

## 6. Positivity, cap, scalar and remaining obligations

The original writer's full positive blocks, signed Hadamard junction, sqrt(2) phase cells and scalar c_R are unchanged. Adding kappa n_R is one additional positive onsite block; no negative compensator or new interaction support is introduced. On a standalone writer its shared-R incident load becomes 4j+kappa, and for the two-writer shared-R apparatus it would be 8j+kappa, counting the bias ONCE. Head incident loads do not change from this bias. With r<=.001 and the nominal single-control cap j<Lambda/1024 these loads fit comfortably below Lambda. If the exact head chemical potential mu=Lambda/4 is also installed, the earlier nominal head-load ceiling 25Lambda/64 remains valid. The bias is not part of a scalar-vacuum robustness class: its vacuum action on R is genuinely nonscalar.

The local inverse bound excludes a singular outgoing reconstruction on the controlled open-channel band. It is not a global spectral completeness result or an assertion of no bound states elsewhere. A compactly supported embedded state at these energies would have zero port values and produce a kernel vector of L_r, which (6) excludes for this local graph; this does not settle threshold or off-band point spectrum. No finite-seed overlap with such spectrum has been estimated.

The staged core and full packet sources were derived with degenerate record thresholds and/or conserved record-X sectors. Their cable propagation, core scattering, feedback inverses and source matching must be rederived at fixed total energy with record-dependent momenta. In particular a returned R=1 amplitude sees a different core/cable kinetic energy; a small local writer error does not control repeated global feedback automatically. The finite chain cuts, actual source state, all output vacancies, common controlled phase and entire-horizon flag target all remain obligations. Derivative bounds through the needed orders for q(k), G_r(k) and the channel-dependent reconstructed packet are also needed before importing integration-by-parts envelopes. Thresholds are avoided here, not analyzed.

The candidate suggests that a future full stationary/packet proof might tolerate kappa of order epsilon*j rather than epsilon/T, but (8) alone proves no such operational or temperature improvement. A larger bias makes the earlier Duhamel method insufficient; that failure is not a physical impossibility theorem. Nor does this local calculation validate an arbitrary strong bias: as a channel threshold is approached, the open-channel and flux bounds used here fail. The earlier weak-bias ground-preparation proposal and its pending distinct review remain unchanged.

## 7. Exact source identities, exposure and verification

N is `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934`. The initiating `common_product_record_ground_preparation/PROPOSAL.md` is `aaa0786b19ec5b0c37923e712fe8f9b80c3490a1c495a7bb5f2482c97402a1bc`, authored by this worker. It supplies the question, not independently checked evidence for the present stationary claim.

The actual writer and its check under `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/correlation_worktree/outputs/attached_record_2026_10_17/source_checks/` are:

- `autonomous_record_route/PROPOSAL.md`: `93445d7d52e32859c980f0a0ebc6024238bedc7571d09e145ab1b128d8292f56`.
- `autonomous_record_route_check/REVIEW.md`: `c5f3e1d7cef939e1bfa95df19f970e4da454cd12a74f068147b6cd50cdf51d5a`.

The exact local inverse premise under N is:

- `common_product_writer_resolvent_sharpening/PROPOSAL.md`: `22bca57ebcbfb8cfabebbe044cd5302e784e585b503cee28d6172afc72e54cf0`.
- Its `certify_inverse.py`: `f1deb1c3200ca89e287f92ea69acbdf0ac02442ef84795717c795c0aa4b62a7d`.
- Its `certificate.txt`: `218168f4038232b24f2daa861b8adb37fe6eecc9845bf0c30bc4bb1338e58dda`.
- `common_product_writer_resolvent_sharpening_check/REVIEW.md`: `d96ed6b26856490d802ceed2009f75aa9c0919eb8760bcfffe0389807965d1b5`.

These hashes and the initiating proposal hash were refreshed unchanged. The writer source, inverse source and inverse check were fully reread for this derivation; the actual writer check and exact program/certificate had been completely read in the preceding coherent work and are reused at those refreshed pins. The inverse calculation is not rerun or reclassified as independently checked by its author.

The staged core `c91300a5eb6db28e67e4b494398c57c3c53bc39d2da8c800a12c284cc5d6c729` and staged packet `3477197cdf54d18ab538c517726d64f3dbc556f6ddb7a6d4b2608b458d34eeb9`, with checks `61de4ee29dd3838c4fc7c3bd19c49bf0cd4cb4bacf5ad3e8e10ca06c864e27c1` and `17029fa32989bae3869c4ffee81def65201edc0f0b996013ede8996ca8cf1453`, are unchanged previously fully read interfaces. They identify the open composition obligations; their degenerate-channel results are not imported for the biased network. Nominal cap references remain single-control76b5 and integrated note02b432 at their previously pinned hashes.

ROOT proposed the inelastic stationary route and requested this bounded test. I authored the inverse sharpening and several earlier components and reviewed staged composition; this is exposed same-model/effort author continuation. A distinct reviewer must check the full 48-dimensional reconstruction, outgoing sign, threshold perturbation, flux factors, constants, scalar accounting and packet variable change. Only this proposal was created. No scientific executable, parameter sweep, W/Git/checkpoint/axiom/editable-prompt/model change, delegation or publication occurred.
