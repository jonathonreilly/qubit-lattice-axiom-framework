# Positive hopping blocks remove source compensation dependence

ROOT original algebraic construction candidate, requiring distinct checking. This is a re-expression of the complete source operator up to an explicit scalar identity on the FULL qubit space. It does not derive a native interaction or coefficient supplier. It does not change the physical axiom stack.

## Exact blocks and full-space equality

For head qubits u,v define X_uv=|10><01|+|01><10|, extended by identity on every other subsystem. Its spectrum on the pair is {1,-1,0,0}. The identity I_uv is the full pair identity, hence extends to the full apparatus identity. For any positive amplitude a,

 P_a(u,v)=a(I_uv-X_uv)

is a two-qubit positive block with eigenvalues {0,2a,a,a} and norm2a. It preserves head number. Its diagonal contribution is a times GLOBAL identity, rather than a(n_u+n_v). It has nonzero vacuum energy a; this must be retained.

Use p,s2,s1,s0 and real positive a1,a2,kappa exactly as in the checked perturbed attachment f32b28aba669d09933c9c22052b2abce4d68339f43faa5beac8f3dc4d8ee978d and its distinctcheck0fd4a54559c48af641f9c90baa326e78a7bcc51f9428d0384ab6c7cc0252447d. That source operator, before adding unchanged background terms, is the sum of six blocks

 j(n2+np)-kappa X_2p,
 a2(n1+n2-X_12), a1(n0+n1-X_01),
 (j+d2-a2)n2,(2j+d1-a1-a2)n1,(2j+d0-a1)n0.

Collecting number operators is an identity on the FULL qubit space, not merely its one-head sector:

 Hsrc_old=j np+sum_(i=0)^2 (2j+di)ni
                            -kappa X_2p-a2 X_12-a1 X_01.

Replace the source block decomposition by the following SEVEN positive blocks:

 P_kappa(s2,p), P_a2(s1,s2), P_a1(s0,s1),
 j np, (2j+d2)n2, (2j+d1)n1, (2j+d0)n0.

All occupations are strictly positive under the stated perturbed-source domain. Their sum is exactly

 Hsrc_new=Hsrc_old+Csrc I, Csrc=kappa+a1+a2.

This equality holds in every head-number sector, including vacuum and multiple-head configurations, and with shared source/old/record/passive-reference degrees of freedom. It does not require [H,K]=0. The unchanged background is added only once. Thus Hnew=Hold+Csrc I as full operators and

 exp(-it Hnew)=exp(-it Csrc)exp(-it Hold)

at every real time. No rotating-frame approximation, discarded phase or physical time rescaling occurs.

## Fixed geometry and source variations

The three hopping edges and all sites are unchanged. The construction only uses two-site positive head-number-preserving blocks and on-site positive occupations. Fullspace positivity of P_a needs only a>0; the existing performance theorem still retains its stronger kappa/j and source-domain conditions. No broader performance domain follows from the algebra.

In this NEW decomposition, a1,a2,kappa may vary independently of the occupation coefficients. Keeping the three occupations exactly2j (or explicitly2j+di) and j np fixed leaves centered source diagonals and background port load fixed. In particular one need not change an occupation by minus delta(a1), minus delta(a2) or any correlated compensation when changing a hopping amplitude. Those numerical compensations belong only to the OLD positive-block decomposition.

For each actual amplitude tuple, define Csrc(actual)=kappa(actual)+a1(actual)+a2(actual). Then Hnew(actual)-Csrc(actual)I is exactly the checked old perturbed source FAMILY with its compensating occupations, even though the NEW implementation contains no such subtractive compensation parameters. The source precision assumptions |ei|<=epsilon and |di|<=epsilon lambda, including differential detuning, remain. This removes a correlation requirement between supplied hopping and occupation coefficients; it does not remove small absolute linewidth, small diagonal disorder or the need to realize the new blocks.

Compression off the three source heads leaves j np+Csrc I, so after accounting for the explicit global scalar it is the SAME emitter-free background. In the source vacuum the new blocks add Csrc to the old vacancy scalar. Therefore all inherited matching/density/time formulae are used for Hnew-Csrc I, and the physical comparison target must be multiplied by exp(-it Csrc). Its scalar is c_att_new=c_att_old+Csrc. Literal K,W and old aging are otherwise unchanged.

If coefficients are uncertain and Csrc is not known, the exact full-state norm theorem is a family theorem with its ACTUAL scalar, not a bound to a single nominal global-phase target. Channel predictions ignore a global identity, but the campaign's phase-sensitive vector-map comparison must retain this qualification. A claim that the new device stays close to the old nominal vector WITHOUT this phase factor would be false at generic long times.

## Resource and finite-cut consequences

This source uses seven positive blocks instead of six and changes no qubits, head edges, geometry or preparation. Hence the full three-source inventory becomes M+238 heads, M+243 physical qubits, M+239 head edges and 2M+282 unmerged positive blocks, if each of the listed three source occupations and j np is counted separately. The other counts remain unchanged. This block count is for this explicit decomposition, not a minimum.

Conservative incident block-norm sums for the replaced source terms are:

 at s0: (2j+d0)+2a1,
 at s1: (2j+d1)+2a1+2a2,
 at s2: (2j+d2)+2a2+2kappa,
 at p: j+2kappa.

These are sums of norms of the NEW blocks and are not inherited old source load constants. Background incident blocks at p must be added separately; unchanged source-free sites retain their old loads. The identity contribution is assigned to both incident vertices in this conservative bookkeeping even though its dynamics is global. Absolute value of2j+di is unnecessary within the positive domain. Outside that domain positivity must be rechecked.

For finite and infinite receiver versions, the SAME Csrc occurs, because only the finite source block decomposition changed. Consequently their exact unitary-difference norms are identical after multiplying by a common phase. The previously checked finite-cut bound and source moments around the shifted physical centers transfer exactly. This is an algebraic interface; it does not rederive their analytical premises or justify any unpublished numerical tolerance.

The product seed is unchanged. No supplied wavepacket, switching schedule, interaction with a fresh environment or measurement has been introduced. Permanent halt, capture and reset/reuse remain unresolved. This may be useful physical architecture freedom, but realization of I-X blocks within the native framework remains an explicitly supplied positive-local-Hamiltonian premise, not a new empirical derivation.

## Evidence and exposure

ROOT authored this identity after reading the full perturbedsource construction/check, local/core extension and outgoing check. A distinct reader must inspect all four pair-head sectors, the vacuum scalar and full operator equality, source compression, actual-versus-nominal phase, independent amplitude variation and changed resource loads. No scientific simulation, parameter sweep, code test, Git/PR, editable prompt, axiom or model mutation occurred. Only this research candidate was written.
