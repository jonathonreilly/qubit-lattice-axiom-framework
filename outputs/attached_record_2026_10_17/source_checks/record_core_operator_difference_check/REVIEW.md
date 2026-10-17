# Complete-core record difference: selective independent check

Disposition: conditional mathematical support for the ordered identity, two-lip spectral interface, all-time absolute bound and stated sufficient scaling. No blocking algebraic or normalization defect found. This does not establish those hypotheses for the attached record apparatus, normalized herald correctness, a success lower bound or downstream output accuracy.

## Source and exposure

Read the COMPLETE ../record_core_operator_difference/PROPOSAL.md and verified SHA256 69aa54015825bd6e240b1da5f856cb062157e2686d5403698592315fa4d529ac. I did not author this source. The source argument and requested checks were exposed before reconstruction. I authored a separate attached-kernel proposal; this review neither checks that proposal independently nor imports its unreviewed estimates. The present operator result can be reconstructed from its explicit block hypotheses without relying on the author's scalar ancestor, which is consequently not recertified here.

Applicable unchanged local instructions/workflow are reused. No scientific execution, solver, experiment, delegation, Git/W/model/prompt/checkpoint change or publication occurred. Only reading, hash bookkeeping and this report were performed. This is source-exposed independent checking, not blind discovery, execution evidence or audit status.

## Ordered block calculation

For nonreal z, self-adjointness makes R_b,s well-defined. In z-H_s the off-diagonal blocks are +kappa V* and +kappa V. Eliminating the background gives D_s=z-H_e-kappa squared V*R_b,sV and the emitter column

    [T_s; -kappa Q R_b,s V T_s].

The sign is therefore negative in the background block. The full block inverse guarantees the finite emitter Schur complement is invertible here; no commutativity is needed. Since D_--D_+=kappa squared DeltaG,

    T_+-T_-=kappa squared T_+ DeltaG T_-.

Expanding L_+T_+-L_-T_- as DeltaL T_-+L_+(T_+-T_-) proves both blocks of equation(1) in exactly their stated order. Expanding the other way produces the indicated alternative with DeltaL T_+ and L_-. A varying H_e or V would add terms, so their equality across sectors is genuinely necessary for this formula as written.

For a common input vector, the emitter and background components occupy orthogonal ranges. Bounding their norms by e and b gives total norm at most sqrt(e squared+b squared). The two terms inside the background component have only a triangle bound; their signs or ranges do not supply orthogonality. The proposed b correctly pays both the direct |kappa| DeltaL T term and the |kappa| cubed recovery/self-energy term. A small DeltaG alone does not control the full core.

The |0>-to-|1> record matrix element is exactly one half of the sector evolution difference because |0>=(|+>+|->)/sqrt(2) and |1>=(|+>-|->)/sqrt(2). This is an amplitude factor, not a probability factor. It applies to the complete old-input map.

## Rectangular spectral jump and remainders

For resolvent convention (z-H)^-1, the lower-minus-upper jump divided by 2pi i has the positive spectral sign. Composing that identity with Pi on the left and E_e S0 on the right gives the stated cross-measure formula. The measure is rectangular and need not be positive; scalar seed-density reasoning alone cannot establish it. Absolute continuity and Bochner-integrable density with this boundary identification are explicit assumptions in the proposal, not consequences smuggled in through Schur inversion.

The lower core-to-emitter column is the adjoint of the upper emitter-to-core ROW. It is not the adjoint of the upper column, which even has the wrong domain/codomain. On the finite emitter fiber G_down=G_up* and T_down=T_up*, transferring u and g norm bounds. For L, adjunction instead produces the reverse recovery row V*R_b,up Q*. The proposal correctly requires independent control of this row or both lips. With compatible real H_b,V,Q and fixed conjugations, complex conjugation gives the lower COLUMN from the upper column, allowing equal norms; that is an additional real-structure argument, not the rectangular-adjoint fallacy.

Integrating the difference of the two jumps costs at most the integral of r_up+r_down. Multiplying the spectral 1/(2pi) by the record amplitude factor 1/2 gives exactly 1/(4pi). Each omitted sector contribution is bounded by ||E_s(R outside I)S|| because Pi is contractive and its own spectral projection commutes with its unitary evolution. The sector sum therefore contributes (epsilon_++epsilon_-)/2. All-time uniformity follows from |exp(-itE)|=1, without differentiating or commuting K.

For a projection E, ||ES|| squared=||S*ES|| exactly. Thus an operator seed-mass bound m_s yields amplitude sqrt(m_s); a single favorable scalar expectation does not. If atoms or singular spectrum remain inside the nominal window, the assumptions as written fail until they are removed by a corresponding projection/decomposition or explicitly included in a remainder. The source makes this limitation clear. It is not enough to redefine epsilon verbally while continuing to integrate an incomplete density over all of I.

The alternate separate emitter/background integrals also check: bound each integrated component by Ecore and Bcore and then use orthogonality of their ranges, adding the omitted amplitude remainder by triangle inequality. Capping either bound by one is valid directly from one half the difference of two isometries followed by a contraction. It requires no claimed success probability lower bound. Tensoring the same maps with a passive-reference identity preserves all operator norms and does not introduce a new old-column aggregation factor.

## Exact integrals and scaling

Direct integration on [-d,d] gives

    integral (a_G+b_G|delta|)/(delta squared+gamma squared)
      =2a_G arctan(d/gamma)/gamma+b_G log(1+d squared/gamma squared),
    integral (a_L+b_L|delta|)/sqrt(delta squared+gamma squared)
      =2a_L asinh(d/gamma)+2b_L(sqrt(d squared+gamma squared)-gamma).

Both lips use the same sufficient envelope, so the 1/(4pi) jump factor becomes 1/(2pi). This gives Ecore<=kappa squared I_G/(2pi c squared) and Bcore<=|kappa| I_L/(2pi c)+|kappa| cubed L0 I_G/(2pi c squared), exactly as stated. No extra velocity Jacobian belongs in these ENERGY integrals. An application starting in momentum coordinates must supply its own dE conversion before invoking them.

For gamma=eta kappa squared with eta uniformly bounded below, arctan<=pi/2 implies kappa squared/gamma is uniformly bounded. With bounded d, log(1+d squared/gamma squared) and asinh(d/gamma) are O(log(1/|kappa|)) as kappa tends to zero. Also sqrt(d squared+gamma squared)-gamma<=d. These prove all four displayed background terms and the two emitter terms as upper-bound scales. An upper bound on eta is not needed for these sufficient estimates: a larger gamma only reduces these integrals. Uniform lower c and controlled coefficients are necessary. A nonzero a_G retains an O(a_G) emitter floor, and a worsening L0 or omitted spectral amplitude can eliminate any useful small-kappa conclusion.

At resonance the direct term can scale like a_L/|kappa| when gamma is proportional to kappa squared with fixed proportionality and conditioning; its integral still has the weaker kappa-log scale. These are envelope mechanisms, not sharp asymptotics or values certified for the new device. At kappa=0 the exact common emitter block decouples, giving zero record-1 core map directly; substituting gamma=0 into the resonant integral formulas is not legitimate.

All bounds are for the full operator at one common physical energy. For several old energies, a union of intervals and appropriate full-fiber envelopes are required. Taking a maximum over unrelated scalar columns would not reproduce the operator hypothesis where errors overlap. The note avoids that shortcut and keeps K inside the actual blocks.

## Finite sign-gauge discriminator

For H_b,+ with off-diagonal h and H_b,- with -h, the background sign gauge U=diag(1,-1) fixes V=|b> and flips the y row. Inverting the two by two matrices gives common G=(z-b1)/[(z-b0)(z-b1)-h squared] and L_+=h/[(z-b0)(z-b1)-h squared], L_-=-L_+. Thus DeltaG=0 but DeltaL=2L_+, and the exact source difference is -2kappa L_+T. It is nonzero for generic nonreal z and nonzero kappa h.

In real time the plus-sector emitter-to-y entry of H squared is -kappa h, so its evolution amplitude starts at +kappa h t squared/2. The minus-sector entry has the opposite sign. Taking the record half-difference leaves +kappa h t squared/2+O(t cubed), as claimed. This is a direct dynamical discriminator against using identical endpoint self-energy to infer identical full source amplitude. Its spectrum is finite and pure point; it is correctly not offered as a model satisfying the absolutely continuous synthesis assumptions.

## Application boundary

The formula supplies an all-time ABSOLUTE upper bound for the chosen finite core, conditional on actual full-fiber inverse/recovery estimates, both lips, cross-spectral synthesis and omitted seed amplitudes. It is not a bound on a conditional normalized success state or on downstream wrong-output amplitude, and finite Q does not include infinite closed tails automatically. It gives no probability of eventual record success and no proof that the attached geometry meets its envelopes. The separate attachment needs premise-matched estimates and spectral regularity; publication or prior local scattering checks do not supply them. Within the stated abstract interface, the proof and constants are supported without correction.
