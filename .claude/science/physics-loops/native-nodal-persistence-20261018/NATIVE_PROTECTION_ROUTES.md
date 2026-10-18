# Native protection routes: a constructive symmetry-sector test

As-of 2026-10-18; repository HEAD and local origin/main both `584755767deb8dfb670f07211d8446873fd0999b`, unchanged from the prior-art task. No fetch, repository edit, PR, audit verdict or checkpoint change. Same selected model/effort. This is a proposed mathematical route with a complete short finite proof and an exact same-author control, not an independently reviewed new result or physical selection claim.

## Outcome

There is a concrete positive invariant-sector construction within the **same homogeneous Heisenberg member** of the candidate nearest-neighbour family. It needs no onsite penalties, bath, Zeno operation, exceptional edge couplings, or PHP evolution. A reflection-odd one-excitation sector on a periodic cubic lattice leaves entire mirror planes in a fixed pure local qubit state while nontrivial quantum dynamics continues elsewhere. This retires a compression mechanism for that explicitly prepared sector. It does not retire the supplied state preparation/symmetry sector, derive record formation, protect arbitrary live inputs, or realize the strict compass carving.

No independently controlled **protecting gap** for the original arbitrary-live product-record interface was found in the closest inspected native sources. The invariant-sector construction below is the sharper constructive next test, rather than adding a pinning Hamiltonian and calling its effect native. It is distinct from the active neutral-composite anisotropic normal-form, transport and binding work through #9776.

## Exact proposed construction: mirror-plane records by interference

Take the simple cubic torus G=C_(2m) x C_Ly x C_Lz with m>=2 and Ly,Lz>=3. Every ordinary nearest-neighbour edge is present with identical coupling. Supply the candidate

    H=J sum_{edges {x,y}} sigma_x.sigma_y, J nonzero,

which is K=D=0 in the source's full-soldering family and the entire possibility-covariant family. No sign selection is needed for the invariant-sector statement. Choose a common unit Bloch direction q and the product vacuum Omega_q=|q>^tensor |G|. These are supplied initial-state data, not an inferred thermodynamic phase or measurement outcome. Choose its perpendicular local state, and write |v> for the state with that one flipped qubit at vertex v.

The one-excitation subspace is exactly invariant because each bond is J(2 SWAP-I). On it, direct bond action gives

    H_1=J|E| I - 2J L_G,

where L_G is the unweighted graph Laplacian. The graph has N=2m Ly Lz vertices, degree6 and |E|=3N, so the background energy is E0=3JN; in the |v> basis the full diagonal is E0-12J and each of the six neighbour hoppings is +2J. No vacuum scalar is silently subtracted from the physical evolution. Unlike-spin edges contribute diagonal -2J and exchange amplitude +2J relative to the vacuum energy; like-spin edges retain the vacuum scalar. This is an exact sector restriction of the full qubit Hamiltonian.

Let F permute sites by (x,y,z)->(-x,y,z). It is a graph automorphism. The homogeneous Heisenberg H commutes with this permutation, independently of any interpretation of improper spatial rotations as framework axioms. Its one-excitation odd subspace

    D={sum_v f(v)|v>: f(Fv)=-f(v)}

is invariant. At a fixed vertex of F the coefficient equals its negative and is zero. The fixed set consists of the two planes R={x=0 or x=m}. Thus every state of D has every qubit in R **exactly** in |q>, and time evolution keeps that true forever. Equivalently, with P_R the product |q> record projector on R and identity elsewhere,

    D subset ran P_R,  exp(-itH)D subset D subset ran P_R for every real t.

One may also include Omega_q, since it is an eigenvector with those same records. Arbitrary superpositions, mixtures and passive references within span{Omega_q} direct-sum D retain the pure record factors. The condition is a supplied code-subspace preparation, not a postselection performed during evolution.

This sector carries real dynamics. Its dimension is (m-1)LyLz. Functions sin(pi l x/m) exp(i ky y+i kz z), l=1,...,m-1, have Laplacian eigenvalues

    lambda=2[1-cos(pi l/m)]+2[1-cos ky]+2[1-cos kz].

Superpositions of different eigenvalues evolve nontrivially; localized antisymmetric pairs propagate while maintaining nodes on R. The boundary cancellation is between amplitudes arriving from mirror partners. It is not the invalid inference that a zero compressed mean field implies no transition. This is exactly the special-live-state loophole preserved by the preceding QHP covariance check: the full arbitrary-live record subspace is not invariant, but this explicitly identified proper subspace is.

This does not implement the previous arbitrary-input operation W or provide its program, timing, loading or complete-output guarantees. The proof removes D-perm as an externally supplied projection mechanism only for persistence of these already prepared plane records on the declared encoded sector, using the unchanged H and initial geometry/state. D-dyn/selection of the Heisenberg member, the common polarized background, torus geometry, encoded one-excitation preparation, record formation and the physical record/readout identification remain premises or open suppliers. No Born/trace rule is needed for the exact factorization statement; interpreting measurements still needs its separate readout bridge. The proof removes the supplied projection mechanism on the declared sector using only the unchanged H and initial geometry/state. It preserves the original local physical qubits as records; no nonlocal decoding is used for the record readout. The live information is, however, encoded across mirror-related sites. That encoding and the polarized background remain substantial state suppliers.

## What is actually checked

The adjacent `native_protection_route_controls/check.py` uses exact integer computational-basis bond actions on a 6x3x3 torus, including all162 homogeneous edges on54 sites. It tests all18 independent odd one-excitation columns, not a sample of modes. Each full-generator image has zero occupation on the18 recorded-plane sites and remains odd. This is a same-author control derived from the bond action, not an independent verification of the above proof.

The control also retains a concrete two-excitation challenge. Start with the normalized odd vector built from flipped sites a=(1,0,0), b=(1,1,0), minus its reflected pair. Initially every plane record is intact, but the full Hamiltonian produces recorded-site leakage with squared norm8 at J=1. There are four distinct plane-reaching configurations, each with coefficient2/sqrt(2), so the exact control value has a separate elementary count. Reflection oddness alone therefore does not extend the one-excitation result to many excitations. This counterexample is preserved in `result.json`; it does not exclude a more restrictive many-body dark code.

The dark odd modes and corresponding even cosine modes can have identical eigenvalues. No nonzero spectral gap isolating this code is claimed. Exact symmetry, sector conservation and encoded preparation carry the result. An uncontrolled small symmetry-breaking perturbation can couple it to bright states. A finite-time Duhamel allowance t||delta H|| is available, but does not yield permanent robust records or a volume-uniform noise threshold.

## Closest native and apparatus source arguments

**Native classifier**, `DYNAMICS_CLAUSE_COVARIANT_NEAREST_NEIGHBOUR_TWO_QUBIT_GENERATORS_HEISENBERG_UNDER_POSSIBILITY_COVARIANCE_THREE_COUPLINGS_UNDER_FULL_SOLDERING_BOUNDED_THEOREM_NOTE_2026-09-24.md`: read lines1–219, including all four theorem arguments and their premise/scope section. Theorem3 gives J sigma.sigma=J(2 SWAP-I); Theorem4 gives the J,K,D family. It derives neither the dynamics clause nor state/phase selection. The mirror construction stays inside its J family and uses no additional interaction.

**Current dynamics synthesis**, `DYNAMICS_CLAUSE_CAMPAIGN_SYNTHESIS_WHAT_ONE_LOCAL_DYNAMICS_CLAUSE_BUYS_AND_WHAT_IT_LEAVES_OPEN_BOUNDED_THEOREM_NOTE_2026-09-24.md`: full read. It explicitly distinguishes PHP from autonomous invariance and lists autonomous dynamics/records and physical realization as obligations. The parent Record-field and compass-carving notes were fully read in the previous report. Their protected-looking Majorana gaps occur after supplied compression, so cannot supply the missing full-generator record protection without a new bridge.

**Restricted static ferromagnetic source**, `RESTRICTED_STATIC_FERROMAGNETIC_SPIN_SOURCE_BOUNDED_THEOREM_NOTE_2026-10-15.md`: read the publication wrapper sections1–8, including full-space gap proof and actual weak-port reduction; the appended immutable author/check bodies were truncated and are not claimed fully read. Its protecting source chain has L_F=J_F sum(I-SWAP), with proven all-sector gap at least2J_F/N^2 above its symmetric sector. But a separate weak port q, source onsite resonance and selected product source are supplied. Its error is of order q/gamma_N+tq^2/gamma_N plus collective-source fluctuation. That is good existing proof machinery for a supplied apparatus. It does not automatically yield protection when all native bonds have the same J: no small q/gamma_N follows, and growing the chain decreases the stated gap. Reusing its gap proof alone would not retire native port/seed suppliers. This report does not evaluate its unaccepted general-plant architectures.

**Formation-balance/dark-state source**, `FORMATION_BALANCE_AND_UNSATURATED_DARK_STATES_BOUNDED_THEOREM_NOTE_2026-09-24.md`: its complete note and companion dark-state argument were visible/read in the second part of the concatenated output. The model is the supplied rotor/hard-capacity birth instrument, not the homogeneous J,K,D qubit Hamiltonian. Its stationary vacancy patterns and its warning that an instantaneously dark state can be reactivated are useful methodological precedents, but neither is imported as a native qubit-sector theorem.

## Ranked next obligations

1. **Independent proof check of the mirror-plane sector**, preserving exact scalar/sign, finite periodic geometry and the one-excitation restriction. Then decide whether a sector-specific retirement of D-perm is worth a coherent milestone. The short calculation alone is not substantial TOE closure or a novelty claim.
2. **Native preparation/interface lemma.** Find a local initial-state or naturally generated symmetry constraint that loads useful quantum data into D while leaving the physical records pure, using the same H. No external phase-programmed paired excitation is silently free. This is the exact supplier relocated by the positive construction. A proposed loader must account for its preparation and its whole input/output map; the conditional encoded input is already a mathematically valid route witness.
3. **Interacting-code extension.** Seek a genuinely invariant many-excitation subspace with the same fixed local records and nontrivial internal dynamics. Use the full boundary annihilator equations B_r psi=0 together with invariance under H_U+compressed boundary fields, not parity alone. A one-time kernel is insufficient: its orbit under the full generator must stay in the kernel. The preserved two-excitation witness rejects the simplest extension before resource-intensive work. This is different from neutral-composite binding or anisotropic normal-form work.
4. **Gap route only with a specified native mechanism.** If a collective ordered region is proposed, prove its true complement gap and boundary loading bound in the actual homogeneous lattice, not the isolated source-chain gap with an artificially weak port. If a different symmetry sector or correlated record is proposed, spell out its local record readout. No general gap impossibility is asserted here.

For comparison, the already checked product-record leakage identity immediately distinguishes the full arbitrary-live interface from this route: its nonnegative edge contributions need to vanish separately. One cannot claim that the mirror code makes QHP zero on all of ran P_R. The report deliberately makes the weaker, useful exact statement and identifies the missing preparation/interaction obligations.

## Search and limits

Filename searches included ferromagnet, compass, Heisenberg, magnon, dark-state, protected, collective-spin, domain-wall and record-sector variants. Content searches included nodal-plane, reflection-odd, antisymmetric-magnon, dark-Heisenberg and one-excitation/reflection variants. No matching native mirror-record theorem was found in those bounded searches. This is not exhaustive literature or branch novelty verification. No external paper theorem is needed for the displayed finite argument; no textbook spin-wave approximation or thermodynamic limit is used. Open neutral branches were not reread or modified. No retained/audit status is assigned, and no platform or editable prompt file changed.

## Source identities

- `docs/DYNAMICS_CLAUSE_COVARIANT_NEAREST_NEIGHBOUR_TWO_QUBIT_GENERATORS_HEISENBERG_UNDER_POSSIBILITY_COVARIANCE_THREE_COUPLINGS_UNDER_FULL_SOLDERING_BOUNDED_THEOREM_NOTE_2026-09-24.md`: SHA256 `c12156bc89754069fbcdca1ccdb0748be8fc37d73a420b944a70a9865c138179`.
- `docs/DYNAMICS_CLAUSE_CAMPAIGN_SYNTHESIS_WHAT_ONE_LOCAL_DYNAMICS_CLAUSE_BUYS_AND_WHAT_IT_LEAVES_OPEN_BOUNDED_THEOREM_NOTE_2026-09-24.md`: SHA256 `0a54de58e9b64b059046bb8f85a156e5b7f4ff915b432adcfde13919eb7c040c`.
- `docs/RESTRICTED_STATIC_FERROMAGNETIC_SPIN_SOURCE_BOUNDED_THEOREM_NOTE_2026-10-15.md`: SHA256 `ed8bb424c2d856aa162f9f5f2d4ab2eda051118422504dcc6a68c88dd81162fe`.
- `docs/FORMATION_BALANCE_AND_UNSATURATED_DARK_STATES_BOUNDED_THEOREM_NOTE_2026-09-24.md`: SHA256 `2ae8d264eaff3ab47ecf4ec41fa21178ff444546bcc2e36d885d092732e30516`.
