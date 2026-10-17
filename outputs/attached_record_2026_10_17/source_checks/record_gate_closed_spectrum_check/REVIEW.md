# Isolated record-gate spectrum: selective independent check

Disposition: conditional mathematical support. The scalar-subtracted isolated one-head gate is nonnegative in both conserved record-X sectors; its spectral bottom is zero without a zero eigenvector. For every E<0 its full resolvent norm is exactly 1/|E|, with the stated compressed/recovery bounds. No correction requested. This does not establish an attached source/emitter inverse, above-band control or a herald theorem.

## Sources and exposure

Read the entire ../record_gate_closed_spectrum/PROPOSAL.md at verified SHA256 9450be53fb37c9971618218a4e806d0d3a01e94914df69932673ef5c66679646. Also read the full actual local construction ../autonomous_record_route/PROPOSAL.md, SHA256 93445d7d52e32859c980f0a0ebc6024238bedc7571d09e145ab1b128d8292f56, and its full check ../autonomous_record_route_check/REVIEW.md, SHA256 c5f3e1d7cef939e1bfa95df19f970e4da454cd12a74f068147b6cd50cdf51d5a. These hashes were verified. I authored none of these three sources. I have prior record-interface/operator-difference exposure, and the parent's intended checking targets and proposal were exposed before reconstruction. This is a selective analytical check, not blind discovery or an audit of the stationary source's entire ancestry.

Previously read applicable local AGENTS/workflow and physics-claim-reviewer instructions are reused. No scientific execution, solver, numerical experiment, parameter sweep, subagent, external literature, W/Git/publication/model/prompt/checkpoint modification occurred. Only source reads/hashes and this report were performed.

## Actual coefficients after subtraction

The four junction vacancies contribute 4gamma I-gamma sum_v n_v with gamma=(sqrt(2)-1)j. Subtracting the declared c_R=4gamma leaves -gamma n_v at each junction vertex. Thus positivity of the original physical blocks cannot itself justify the new kinetic lower bound; the proposal correctly does a fresh calculation.

Each square vertex has two Q bonds of magnitude j/sqrt(2) and one external ordinary j bond. Its occupation coefficient after subtraction is sqrt(2)j+j-gamma=2j. The square is bipartite between the two arm attachments and two port origins, with block -jU; there are no additional installed arm-arm or port-port links. The actual supplied geometry and selective-zero-coupling convention support this coefficient matrix.

At each terminal, its one inward Q(-j) contributes j and the shared contact j n_T(I+X_R) contributes j(1+x) in sector x. Its exact diagonal is therefore 2j+jx, namely j for x=-1 and 3j for x=+1. Both terminals couple to the SAME X_R; no independent sector choice at opposite terminals is permitted or used.

At each phase-cell endpoint the adjacent ordinary bond contributes j, the strengthened bond sqrt(2)j, and the explicit occupation (2-sqrt(2))j. Their sum is 3j. The two cells lie on arm1 bonds y=2--3 and y=5--6; their four endpoints are distinct, nonterminal and nonjunction vertices with ordinary neighboring bonds. Hence the displayed diagonal inventory has no overlapping-site correction. All other vertices have ordinary diagonal 2j.

## Full lead unitary and exact form

On l2(N_0) tensor C² of the physical input/output leads, apply I tensor U with the SAME U at each coordinate m, leaving both arms unchanged. Since U is orthogonal, this is a genuine bounded unitary on both complete infinite leads, not just a rotation of their port amplitudes. The lead diagonals 2jI and inter-slice couplings -jI remain unchanged. The arm-port coupling becomes -jUU^T=-jI. Consequently the two arms decouple into separate half-line continuations, each with terminal n=0, arm endpoint n=10 and first transformed lead site n=11.

The transformed lead labels need not retain their physical input/output meaning. Unitary equivalence suffices for this spectral claim. It uses the two ordinary identical isolated leads; an asymmetric source attachment would not be unchanged under this transformation.

For either chain, let w_n be j on ordinary bonds and sqrt(2)j at that chain's phase bonds, and let C be its phase endpoints. Expanding

    sum_n w_n |u_n-u_(n+1)|²
       +(2-sqrt(2))j sum_(n in C)|u_n|²
       +j(1+x)|u_0|²

gives exactly every diagonal and hopping calculated above. In particular, the ordinary terminal graph-Laplacian diagonal is j, not 2j. Adding j(1+x) supplies precisely the terminal remainder; for x=-1 it is zero, not a negative defect. At each cell endpoint the Laplacian diagonal is (1+sqrt(2))j and its positive remainder supplies 3j. This is equality with the entire reduced chain, not a comparison dropping a troublesome term.

All weights and remainders are nonnegative for j>0. Bounded finite-degree coefficients define bounded self-adjoint operators, so equality on finitely supported vectors extends to all l2 vectors. More explicitly the difference map u->(sqrt(w_n)(u_n-u_(n+1))) is bounded, so its squared norm and the finite onsite sums define the same continuous quadratic form. This proves positivity for each chain and hence both sectors of the original graph. Before resolving the record, the terminal remainder is j|0><0| tensor(I+X_R), itself positive; coherent record superpositions are covered.

The result concerns the full isolated ONE-head Hilbert space with all record components and both infinite leads. It is not an asserted lower bound for every many-head sector of the scalar-subtracted physical qubit Hamiltonian.

## Bottom, absence of a zero atom and resolvent norm

Choose a normalized vector constant on N consecutive sites of a lead beyond all modified sites, zero elsewhere. Its two boundary differences contribute total 2j/N and no onsite remainder contributes. Thus inf spectrum<=2j/N for every N. Positivity then gives inf spectrum=0; closedness of the bounded self-adjoint spectrum implies 0 is in the spectrum.

If an l2 vector had eigenvalue zero, its nonnegative quadratic form would vanish. Every positive-weight edge difference must then vanish, so it is constant on each entire half-line. No nonzero constant is square summable. Thus the kernel is zero and there is no spectral atom at zero. This argument does not assert absence of positive bound states, nor does it require a claimed global scattering completeness theorem. It distinguishes a threshold in the spectrum from a normalizable zero mode.

For E<0 the distance to this spectrum is exactly |E|. The self-adjoint resolvent identity therefore gives ||(E-H_x)^-1||=1/|E|. Equivalently H_x-E>=|E|I gives the upper bound; spectral bottom zero makes it exact. In the specified convention (E-H_x)^-1 is negative definite, so the sign statement is also correct.

Isometric input-coordinate inclusions and output restrictions cannot increase the norm. Thus both compressed blocks I_y*(E-H_x)^-1 I_b and complete recovered columns (E-H_x)^-1 I_b obey <=1/|E|. The latter retains both whole leads and arms, not merely a sitewise collection requiring an uncounted aggregation factor. For E<=-Delta the uniform ceiling 1/Delta follows. For z outside [0,infinity), spectral inclusion gives <=1/dist(z,[0,infinity)); this is an upper bound and is not generally claimed exact for complex z. It supplies a genuine below-threshold analytic region without continuation through the positive spectrum.

## Compression and attachment boundaries

Exact orthogonal compression of a nonnegative operator is nonnegative. At a physical finite lead cut, removing Q(-j) and adding j n_last restores precisely the retained diagonal contribution, realizing this compression. Arbitrary changed boundary loads do not follow from that observation.

For a spectator internal eigenvalue beta, the shifted kinetic argument E=lambda-beta is legitimate only when the isolated gate acts as identity on that internal fiber and the common scalar has been handled correctly. A supplied strictly negative margin then permits this gate estimate. It does not cover a closed channel above the ordinary lead band [0,4j], does not exclude positive localized modes from the phase cells, and does not bound an on-shell propagating resolvent inside that band. A generalized growing/decaying-wave reflection coefficient has separate normalization/reference-plane factors and cannot be assigned the same bound without conversion.

Finally, invertibility of an isolated nonnegative block does not make a coupled Schur complement invertible at the same total energy. Attachment can change onsite terms, coupling self-energies and the relevant energy margins. The simultaneous infinite-lead rotation is not asserted to diagonalize a one-sided attached source. The proposed lemma is therefore a valid isolated below-threshold input to a future full attachment analysis, with exactly the stated limits. No further closed-channel, complete-output, false-herald or success guarantee is established by this check.
