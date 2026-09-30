# Independent check of the native four-particle threshold reduction

No blocking mathematical error was found in the frozen report at its stated scope. The physical open/closed split, complete nine-component free-pair exterior, compact-source threshold inverse, strict positivity of the finite core Schur matrix, and positive semidefinite relaxed threshold form check. The exact E-channel witness proves a strictly nonzero relaxation of the bare pulse coefficient. It does not evaluate the relaxed form or establish an on-shell positive-energy scattering matrix.

Coverage binds `native-scattering-route/REPORT.md`, SHA256 `9030dd11df3269de46237457ef4809911e94b5e60c71032b1c501d2e1871d434`, and manifest `75b5a1cde77ded01f7a75e5c1b2218d6d982f7b52e62edbb0e836d24872f60ed`. No author correction was requested. This is focused independent evidence, not formal review, an audit/PASS, physical selection or a phase/scattering-completeness claim.

## Independence and actual source

Before opening the author's report or evidence, I read only its contract and reread the actual native-stability law. I froze `PRECOMPARISON.md` at 02:32:46 UTC, SHA256 `8ae4360ee69515a82b326af3a8ce576c5dd102cfff8ae9af900743f9d0e95574`. It independently derives the Q gap, fixed-number norm bound, finite-contact/free-exterior criterion, form-inverse distinction, and a decay/SOS route excluding a zero resonance, conditional on the physical exterior identification. It explicitly keeps strict positivity of a nondecaying incoming-channel form separate. The author packet had become available but had not been read when that file was frozen.

I then read the complete frozen author proof, source inventory, bindings and numerical evidence. No author implementation was read, imported or executed. The independent computation uses direct occupation sets and integer coefficients scaled by twelve, generated from annihilating each occupied pair and creating each actual local pair. Its expected reported counts were known after the precomparison freeze, so it is not described as a blind numerical test.

The supplied operator source is `native-stability-route/REPORT.md` (`7eba7d0092eb4990f5ae1a46825e015c6edc18692c09cab69ad5cd3ed4d24ca9`), with the actual five Q operators and the full-carrier SOS. The prior independent native Gram check is reused within its two-particle scope. The bare coefficient is reused from my complete independent interaction check (`da8a9081fb1e81ad4678dca076e16f0211260c573f9c6a3f020ae9ac13a94aaa`); its normalization is reconstructed below rather than interpreted as a scattering result. The density/coercivity theorem is not needed for this threshold proof.

Current observed main is `d31bbef9a83a4994129106efa1e8c1aa7c31c4b0`, with selected campaign procedure `7146fe17a76de41badcaca3c3c7cac6d11eb2a00`. The frozen supplied law is not replaced by a moving source. Framework bytes and prior native inputs are bound separately in `SOURCE_BINDINGS.json`. The author's comparison sources on other carriers and its prior-work search are not premises of the proof checked here; no independent priority/novelty conclusion is asserted.

## Physical fixed-number operator and the closed gap

The actual law is

`H0=mu N-2mu sum P_E-mu sum P_T+V3+W_tau=A+mu D+W_tau`,

on unordered sets of occupied physical M2 sites, with commuting different-site hard-core operators. In N=4, D counts degree-zero and degree-three vertices of the induced eighteen-neighbor graph. If D=0, every degree is one or two. A four-vertex graph with that property is a four-cycle, a four-vertex path, or two disjoint edges; it has a perfect matching. Thus on the orthogonal nonmatching occupation subspace Q,

`QH0Q>=mu Q`.

The independent enumeration gives precisely 27 nonmatching labeled graphs: twenty with D=1, six with D=2 and one with D=4. The graph classification proves the bound for every geometric realization; the finite enumeration is a control, not a fitted gap estimate.

An independent norm argument avoids a two-body lifting theorem. The actual SOS gives

`2 sum P_E+sum P_T <=2 sum_edges n_x n_y<=12`,

so `sum Q_A†Q_A<=12`. The three translation-gradient directions give `W_tau<=12tau sum Q_A†Q_A<=144tau`. Also `A<=12mu` and `mu D<=4mu`. Therefore `0<=H0<=C=16mu+144tau`. This proves the bounded self-adjoint realization in the fixed-number space. Positivity and bounds hold in the K=0 orbit fiber directly by the local quadratic forms, or by large translated-wavepacket limits; an almost-everywhere direct-integral statement alone would not establish a specified exceptional fiber.

Finite occupation sets have no nonzero translation stabilizer, so the physical translation-orbit basis has ordinary orthonormal normalization. P and Q remain occupation projections in this basis. Multiple perfect matchings of one configuration never become multiple physical basis vectors.

Every off-diagonal term removes one graph edge and creates one graph edge. A disconnected P graph is exactly two disjoint edges. Removing either leaves the other edge intact; a nonzero hard-core creation leaves a perfect matching. Hence P-to-Q coupling starts only at connected P configurations. Connected four-site shapes have graph diameter at most three and physical l1 diameter at most six, so the input core is finite modulo translations.

The independent spanning-tree growth gives 9, 113 and 1,647 connected shapes at particle counts two, three and four. Of the last, exactly 1,487 have a perfect matching. Direct reconstruction of all those core columns gives 143,672 nonzero mu/tau coefficient pairs, 25,645 Q boundary shapes, 8,298 separated-pair boundary shapes and maximum coordinate span seven. These independently reproduce the reported counts and support claims. I did not equate a matching count or a printed digest with entrywise comparison of two stored matrices; the author does not supply the full coefficient array separately, and its code was not read.

## Complete free pair cell and the physical exterior

The actual graph-edge two-particle subspace has nine orthonormal anchored bond types. Three are opposite axial endpoints centered at x. Six are `{x,x+e_i+eta e_j}` for i<j and eta=+/-1. These are physical two-site configurations, not an orthonormalization of the five collective Q's.

For a diagonal bond, the two shell centers are `x+e_i` and `x+eta e_j`; their Q coefficients are both `-eta/2`. Fourier transforming gives exactly

`v_(ij,eta)(q)=-(eta/2)(exp(i q_i)+exp(i eta q_j))`.

Its squared two-component norm is `S_ij=1+cos q_i cos q_j`. The axial collective frame is the rank-two traceless projector. Thus the full symbol is the author's 9-by-9 expression, retaining four high components at energy 2mu and treating a null T frame vector as a missing vector rather than a new band state. The independent literal action matches all 5,184 matrix entries at 64 quarter-period momenta using exact Gaussian integers; the preceding Fourier derivation establishes the formula for general momentum.

For `a=min(tau,mu/6)`, every band obeys `h2(q)>=a ell(q)I`. For T, minimize its affine dependence on S in [0,2] to obtain `epsilon_T>=2min(mu,tau ell)`; use `ell<=12`. E has energy `tau ell` and the remaining directions have energy 2mu. Hence the actual free two-pair symbol at K=0 satisfies

`h_f(q)=h2(q) tensor I+I tensor h2(-q)>=2a ell(q)I`.

Only q=0 can be a zero pocket when mu,tau>0. In particular the old pi,pi zeros at tau=0 are lifted, and the null-Gram loci remain high energy. This is a bound on the complete cell, not on a selected low-band projection. Breakup or possible internal trimer dynamics remains in the Q compression, whose gap was proved without a trimer assumption.

Remove from the exchange-symmetric two-bond reference all overlaps and all cross-graph edges. Each endpoint is within sup-distance one of its anchor; any cross edge therefore has relative anchor sup-distance at most four. This is a genuinely finite hole. I independently obtain 3,543 ordered indices, nine exchange-fixed identical-bond indices, and 1,776 normalized symmetric hole coordinates. The disjoint members of the hole map onto exactly the 1,487 physical core shapes, with the expected many-to-one contact matching map. They are not the same space as the physical core.

Outside the hole, the unique physical matching gives an isometry between normalized exchange-orbit bond states and occupation states. Each local operator acts on one of the two separated edges. Hard-core-blocked creations into overlap or contact are precisely the deleted reference transitions. The diagonal term there is the sum of two single-pair diagonal terms; V3 vanishes. Therefore the exact exterior block is the Dirichlet compression of h_f. The Q-to-exterior block is zero by the matching argument. This discharges the geometric hypotheses left explicit in my precomparison.

The threshold constant internal space is `Sym² C⁵`, of dimension fifteen. This counts only constant incoming profiles. It does not remove odd-relative, angular or positive-energy channels. At zero momentum T has Gram two, so its normalized one-pair vector is T/sqrt2. Pair exchange follows from the isometric separated-cluster tensor construction and commuting physical creators, not an assumed pair-boson commutator at overlap.

## Threshold Green forms and core invertibility

The Q inverse has the uniformly convergent series in the report. Its ratio bound is `(C-mu)/(C-z)<1` for z<mu; summing the geometric remainder yields exactly the denominator `(mu-z)` and the stated power. Multiplication by `||B||²<=C²` prices its contribution to the finite core. Every finite order on a compact boundary is a finite sparse calculation, though high orders may be impractical.

On the Brillouin cube, `ell(q)>=4|q|²/pi²`. Thus the free inverse symbol is integrable in three dimensions. With the specified measure, enclosing the cube in the ball of radius sqrt3*pi gives the stated ordered-cell bound `sqrt3*pi/(16a)`. The difference of the free resolvents at -epsilon and zero is bounded by integrating

`epsilon/[c |q|²(c |q|²+epsilon)]`, `c=8a/pi²`,

over R³, which gives `sqrt(epsilon)/(4pi c^(3/2))`. For finite matrix compressions the source coefficient and exchange-normalization factors must still be included, as the report says. These are not free conditioning estimates for the large finite matrices.

The L1 inverse symbol has Fourier coefficients tending to zero. Compressing to the finite symmetric hole gives a strictly positive matrix G_II: a nonzero compact vector has nonzero Fourier transform on a set of positive measure, and h_f is positive almost everywhere. The finite-hole Dirichlet resolvent identity first holds below threshold. Passing to zero gives the reported finite-matrix subtraction, with finite compact-source entries and decaying exterior kernels.

This is an inverse quadratic form/kernel on compact sources. It is not a bounded inverse on l2. A nonzero soft monopole can have a 1/r response, which has finite energy in dimension three but is not square-summable. The report preserves that distinction correctly.

The exact physical core/Q/exterior blocks then yield the finite core Schur matrix S(z) below threshold. Its zero limit S0 is positive semidefinite by variational minimization. The proof of strict positivity requires more than H>=0 and absence of a usual eigenvector; a positive operator can have a zero resonance.

Here the additional local-SOS argument works. If S0u=0, choose the regularized Q and exterior minimizers with fixed core u. Their total H energy is the regularized Schur form minus epsilon times the two outer squared norms, so it is nonnegative and tends to zero. The Q part converges in l2 by its gap. Exterior coordinates converge by the finite-hole Green identity, and the limit tends to zero when the two pairs separate. If the fixed residual pair is not a graph edge, the distant configuration instead lies in Q, and its coefficient tends to zero along distinct orbit indices. The required pointwise limits therefore exist in every local row.

Each positive SOS row has finite occupation support. Vanishing total energy forces every row to vanish on the limit. The gradient rows imply that `(Q_A(x)psi)({y,z})` is independent of x. Sending x away from the fixed residual pair makes each term tend to zero, by the preceding exterior/Q distinction. Thus all Q_A annihilate the limit. In the original, not just completed-square, expression for H, all attractive and gradient terms disappear, leaving

`(4mu+V3(S))psi(S)=0`.

Positive mu forces every coefficient to vanish, contradicting nonzero core u. This proves S0>0. It excludes a core-coupled decaying zero pole and supplies the full compact-source resolvent through the block reconstruction. It is not a spectral gap above the two-pair threshold and does not exclude positive-energy resonances, different total momenta or nondecaying incoming zero-energy profiles.

No numerical smallest eigenvalue of S0 or G_II has been computed. Their entries have a controlled series/integral approximation, and their proven finite-dimensional strict positivity permits eventual interval certification at fixed computable positive couplings. This is an existence/termination statement; it supplies no resource-efficient algorithm or bound uniform as a coupling tends to zero.

## The relaxed form, normalization and strict correction

Let Phi be a specified constant incoming soft profile, extended to physical four-site configurations by the actual sum over disjoint matchings. Far from contact, each local SOS row kills the complete zero-energy pair factors. Therefore its SOS row vector has finite relative support and energy, and F=H Phi is compactly supported. This checks a stronger statement than merely setting a projected band eigenvalue to zero.

For an l2 correction u, the affine energy is

`E(Phi)+2 Re<F,u>+<u,Hu>`.

It is the sum of the actual nonnegative row norms. Spectral minimization gives

`T0=E(Phi)-<F,G_H(0)F>`.

The regularized minimizers `-(H+epsilon)^-1F` justify the limit: finiteness of the inverse form implies `epsilon||(H+epsilon)^-1F||² ->0` by dominated spectral integration. There is no claim of an l2 limiting minimizer. The pointwise response exists, solves the stationary equation and decays in the exterior. A compact change of the initial extension is absorbed into the allowed corrections, so it does not change the relaxed form. Its positivity comes from the finite affine SOS energy, not from an unjustified inference that every positive Feshbach matrix is a repulsive scattering amplitude. Only semidefiniteness of this fifteen-channel form is claimed.

The identical-pair normalization is correct. If `C_E=sum_x Q_E1(x)†`, the normalized single-pair q=0 vector on volume V is `C_E Omega/sqrt(V)`. Two separated identical normalized pair states have normalization `C_E² Omega/(sqrt2 V)` to leading volume order; the physical occupation and free symmetric basis agree in the exterior. In the translation-zero fiber the constant profile is therefore `Phi_E=C_E² Omega/sqrt2`. The independent pulse calculation gives `[t⁴]<H>/V=<C_E²Omega,H C_E²Omega>/(4V)=52mu+120tau`. Consequently the bare threshold form has coefficient twice that number, `104mu+240tau`, not the quartic coefficient itself.

For the reported four-site word S and shifted target T, the only contributing shifted term removes the middle x-axis pair centered at (3,0,0) and creates the y-axis pair centered at (3,0,1). The gradient contributes -tau times the off-diagonal axial traceless-projector element -1/3. Therefore `<T,H S>=tau/3`. The unshifted coefficient is `(6tau-2mu)(-1/3)=(2mu-6tau)/3`, explaining why it would be a poor coupling-independent witness.

For `C_E²Omega`, each matching has integer weight: the two creator orders cancel the two factors 1/sqrt2. At T only the returned x-axis matching contributes, giving the same `tau/3`. My independent literal action verifies both statements, without treating a generic occupation vector as an incoming channel. Dividing by the identical-pair sqrt2 gives `F_E(T)=tau/(3sqrt2)`.

Since H<=C and the compact-source inverse form is finite, `G_H(0)>=1/C` on those sources. The one nonzero physical orbit coefficient therefore bounds the subtraction from below by `tau²/(18C)`. This proves exactly

`0<=T0_EE<=104mu+240tau-tau²/[18(16mu+144tau)]<104mu+240tau`.

It does not give the value of T0_EE, positivity away from zero in every incoming direction, or a cross section. At mu=tau=1 the separate literal-state control gives twenty Q outputs with squared norm 68/9 and checks their twenty Hermiticity columns. The self-energy interval `[17/360,68/9]` follows from `1/160<=DQ^-1<=1`; this norm is for the literal full-space occupation vector, not the orbit-normalized incoming profile. The report makes that distinction correctly.

## Actual verification and limits

One independent sparse job was priced at at most thirty CPU seconds, 120 wall seconds and 150 MB. It used 6.873 seconds of measured Python wall time, 6.768 CPU seconds and 33,292,288 bytes peak RSS. BLAS/OpenMP thread caps were one. The deadline and absent STOP_REQUESTED sentinel were checked before work, at script entry and during the core traversal. No assertion failed. No author code, dense N=4 torus, dense core inverse, background worker or external mutation was used.

The proof checks close the particular mathematical obligations left conditional in the precomparison: actual exterior isometry, finite-hole Green form, decaying resonance exclusion, and correctly normalized nonzero relaxation. They do not numerically evaluate the Brillouin matrices, closed-sector infinite series, S0 conditioning or the final fifteen-by-fifteen form. Those remain explicit further tasks. Positive-energy limiting absorption, flux/group-velocity normalization, anisotropic scattering-length conventions and asymptotic completeness are not obtained from this threshold quadratic form.

The one-M2 carrier, occupation axis, quantum amplitudes, vacuum, couplings, Hamiltonian and infinite-lattice fixed-number/fixed-momentum problem remain supplied choices. No finite-density condensate, excitation phase, two linear tensor modes, common gravitational source/action, actual record instrument or foundational adoption follows. The check grants no formal review or audit status.
