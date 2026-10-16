# Post-exposure action-reconstruction working-note comparison, v1

This is a separately labeled comparison after the independent proof and42 controls were frozen. I read the complete242-line action_selection/WORKING_v1.md, copied immutably as AUTHOR_WORKING_v1.md, SHA256 bd8b22a0343fafad71a38028cefa005d16ffa46114e2eace64b66fb60dd25e2c,12298bytes. I did not open the new author implementation, numerical outputs, canonical note, raw observations, GW papers or distance posteriors. The independent proof/report is aa6f275dd043529fc824a00b0ebdbb190abf610a6ddfb9fc1e4ecad81edaa21a and remains unchanged. Root retains authorship; this is not a formal audit.

## Core reconstruction correspondence

The note uses omega=F Z rather than the independent proof's Z. Its D is the independent T_rec. With that mapping, equations(1)–(3) for D,V and omega agree exactly, including the curvature sign, Fddot term,5/2 H Fdot coefficient and source action's no-half K normalization. Conservation plus both metric equations implies the scalar equation only after division by nonzero Fdot, as derived explicitly in the independent proof. The note correctly separates monotone-chart intervals, isolated turning-point compatibility and constant plateaus.

The candidate constants F_c and c are the independent B and beta. Their inverse affine relation Y=Fdot²/D=(F-F_c)/c, the two-epoch parameter recovery, allowed quadratic root, and all stated positivity/domain gates agree. The normalization formulas Q0=4a_c F_c/(1+k)² and Q=4a_c F_c/(1+k) equal the independent formulas B(1+s)/(s(1+k)) and B(1+s)/s. The original supplied k range is essential to selecting the inverse root.

The potential representation V/F²=L B0+T B1 with L=2Hv²/Q and T=L nu is equivalent to the independent V=theta0 L0+theta1 L1 basis. The determinant, positive coefficients, residual checks and vacuum nu degeneracy are correctly stated. Ratio-only normalization gives Q0/F_ref and retains physical-time Hv while leaving Hv²/Q0 uncalibrated. This is a conditional calibration result, not a derivation of a quantum hierarchy or of the supplied action family.

The full-field kinetic inequality agrees with the independent result. Equality at one instant fixes only transverse velocities; it does not locate the fields. If exact equality for the same candidate parameters holds on an open interval, positivity forces both transverse coordinates to be constant; their independent equations then force x=y=0. The copied working note says their equations must be checked separately. The independent report contains the complete open-interval argument, and root reports adding it explicitly in the canonical adaptation. That forthcoming source is outside this v1 snapshot.

The dust-plus-Lambda plateau example is valid within its stated constant-F exact domain: D=0 then forces every velocity to vanish under the positive supplied kinetic metric. A fixed scalar gradient cannot balance a changing nonzero matter trace while the coupling remains nonzero. Equivalently the one-field equation requires2F V_F-4V=rho-3p, whose left side is constant. This is a failure of the attempted inverse domain, not an exclusion based on measured LambdaCDM fits. The independent de Sitter/constant-potential counterexample separately demonstrates how metric equations alone can miss the scalar condition.

## Two actionable distinctions found

1. Background ratio versus gradient coupling. In the one-field reconstruction q_rec=1/(2omega_rec+3) is obtained from D. The candidate field-space gradient norm q_geom=|d ln A|_K²=a_c/J remains well defined even when transverse fields move. Substituting D=Z0 Fdot²+2F T_perp, where T_perp=Kxx xdot²+Kyy ydot², gives

       1/q_rec = 1/q_geom + 4F² T_perp/Fdot².

   Thus q_rec<=q_geom on the supplied positive domain, with equality only for zero transverse velocity at that instant. Reusing a single q without this qualification risks interpreting an along-history ratio as the full local coupling. This is a necessary scope distinction; the correct radial inverse itself is unaffected.

2. Canonical-distance normalization. The formula dchi=+/-d lnF/(2sqrt(q_rec)) is dimensionless K-metric distance with Einstein kinetic term -Q(dchi)². In the conventional dimensionful normalization -1/2(dvarphi)², varphi=sqrt(2Q)*chi up to orientation and translation. The original wording “Einstein canonical distance” did not specify this convention. Its numerical factor is correct with the dimensionless convention, but the normalization needs to be explicit.

Root accepted both findings. AUTHOR_NOTE_FINDINGS_v1.json preserves the original scope/line references and proposed repairs. No author file was edited by this checker. At this freeze, the corrected canonical bytes have not yet been read, so this report does not assert their closure.

## Other mathematical statements read and limits

The note adds a conditional tensor-transport argument not part of the pre-exposure reconstruction target. As a separately post-exposure formal check, variation of its specified quadratic wave action gives nabla_mu(F nabla^mu h)=0. Inserting a geometric-optics ansatz yields k²=0 at leading order and nabla_mu(F A_h² k^mu)=0 at transport order. Under the stated equal beam geometry, emission normalization and negligible/bounded conversion/reflection/absorption assumptions, the amplitude transfer has sqrt(F_source/F_observer), so the propagation-only luminosity-distance ratio has the reciprocal sqrt(F_observer/F_source). Smooth endpoint factors telescope; equal local endpoints cancel an intervening varying prescribed coefficient. These are conditional transport algebra, not a verified generation model, astrophysical screening solution or measured F history. This calculation is not relabeled as part of the pre-exposure independent oracle.

The input-domain rejection of a single published distance pair is appropriate: it supplies none of the required differentiable F,H histories or their controlled endpoint identification by itself. The note does not report inferred k,nu,Q0,Hv from that pair. Its distinction between conditional reconstruction and a chosen physical initial state, unique action or TOE is consistent with the independent proof. I did not verify the referenced publication/data statements, their exposure history or any numerical likelihood.

Parent messages disclosed an author case9 recovery failure and later conditioning diagnosis. I have not inspected those files or checked the numerical repair. They are not replaced by the42 independent controls, and no claim about99 author passes or the preserved90/1 run is made as independently verified evidence here. Only the supplied action, independent mathematical artifacts and complete working note listed above were read. No aggregate, root code, process, state, graph, cache, git/index or publication action was performed.
