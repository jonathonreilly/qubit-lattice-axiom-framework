# Homogeneous charged-record model: bounded author-source comparison

2026-09-22. This is a post-seal mathematical comparison, not a new blind
reconstruction, publication decision or formal audit. **No material error or
required correction was found in the authorized frozen packet.** The second
and fourth coefficients, actual charge transport, and sufficient local-limit
scaling agree with the independently sealed derivation after the normalization
conversion below. The volume-uniform conclusion remains conditional on the
specified model, moment bound and finite-circuit preparation.

The blind report and every PRE-bound file remain unchanged. Its report SHA256
is `88bef2c7814bacb3864eee220e245365b3207c9d8f189298f8e8ddf1e13a3582`, and its
PRE seal is `1678d9365ac5c3460d70a13d16b8b3fbeedd0f09b658a023c5ee515e4e213b48`.
This comparison does not retroactively give its new controls blind status.

## 1. Exact sources and read boundary

The authorized author seal is
`HOMOGENEOUS_CHARGED_RECORDS_AUTHOR_SEAL.json`, SHA256
`ec6d68f95a67c810e442fe52d8e453183f4d9723e55e52df36a0d8010727b9b0`.
All 18 named bindings authenticate. The principal source is
`HOMOGENEOUS_MOBILE_CHARGED_RECORDS_AND_FIELD_DYNAMICS.md`, SHA256
`8598d411c9837c4a97ac217de3058803386e83875ea62d0f707f6b9e32fd9b59`.
The complete 527-line note, both complete current scientific checkers, all
result fields, source context and working specification were read. Current
receipts and complete streams authenticate; the successful stdout files equal
the results byte-for-byte. The historical failed trace, disposition, receipt
and complete source delta were inspected. Author evidence authentication is
not counted as an independent calculation.

The checkers are:

- `homogeneous_charged_records_check.py`:
  `efe021123b87d11fa35d3d3472423c4107ed49bebb3d374abbb13b4b97d3894d`.
- `homogeneous_occupancy_penalty_check.py`:
  `3f5b2f601b078c5618ce976e3a0ce1b991539d6bd873c63f03a76677bcba7d3d`.

The two complete result identities are respectively
`3caee8f0d605e3a3f4d50935c015f6f1d96eece588f0f67492e329542034de0d` and
`e89e885e12688e1a47bb9fd7379c82de45b621e2aaa2cbe17689011237fe080d`.

The two mathematical predecessor notes and prior independent final seals in
the context match their already-reviewed identities. Their unchanged
finite-circuit, local propagation and weighted spin-to-rotor machinery was
reused, with the changed hypotheses checked below. The fifth contextual
binding is a PR 8626 source receipt: its bytes were authenticated only. No
scientific result from that unrelated static-gas source was read or imported.
The newer charged-band/phase, finite-rate formation, campaign checkpoint,
registry and other frontier sources remain unopened. No new literature theorem
was imported. The historical “independent reconstruction pending” text in the
frozen author source records its pre-comparison status; this report supplies
the separate subsequent comparison.

## 2. Normalization and coefficient reconciliation

Put alpha=2d-1 and C=S(S+1). The independent report uses

    epsilon_i = t/V0,

whereas the author uses

    Delta = alpha V0,   epsilon_a = t/Delta = epsilon_i/alpha.

The physical coefficients are identical:

    K = t^2/(alpha V0 C),
    J = 2 t^4/[V0^3 alpha^2(alpha-1)]
      = gamma_d t^4/Delta^3,   gamma_d=2alpha/(alpha-1).

Consequently both parameterizations give

    V0 = 2 K^2 C^2/[J(alpha-1)],
    epsilon_i^2 C = J alpha(alpha-1)/(2K),
    epsilon_a^2 C = J(alpha-1)/(2alpha K).

The birth schedules have the same sufficient exponent 3d. Their prefactors
must differ by the fixed factor alpha^(3d) if the schedules are to describe the
same numerical beta. Equality of the exponent alone is not equality of beta0.

The blind diagonal fourth-order coefficient is in units t^4/V0^3; the author's
is in units t^4/Delta^3. Multiplying the blind dimensionless coefficient by
alpha^3 gives the author's Eq. (7), including the folded contribution. For a
disjoint pair with r=1,2 cross-neighbor contacts the coefficient is

    2 - 4alpha/(2alpha-r) = -2r/(2alpha-r).

Pairs sharing an endpoint contribute the folded coefficient 2 because two
simultaneous outward hops are blocked. Disjoint r=0 pairs cancel. This gives
the two displayed negative coefficients -2/(2z-3) and -2/(z-2). The scalar
unit-shift limit has

    c_d = alpha^3 ell_d = 8 d^2(d-1)/(4d-3).

For the 6^2 and 6^3 controls, author scalars 1152/5 and 3456 become the blind
values 128/15 and 3456/125 after dividing by alpha^3. The exact symbolic
conversion is executed in `comparison_check.py`.

The one-hop and two-outward-hop energy costs are alpha and 2alpha-r in V0
units. Four legal time orderings per plaquette orientation have costs
alpha, 2(alpha-1), alpha. Their signs and amplitudes give the stated J.
The four-hop operator swaps the charges at the two A vertices while shifting
the links conditionally on those charges. It is not a pure field plaquette
operator for arbitrary charge configurations. For opposite charges the two
circulations have the same joint matter/field target and add; for equal charges
they give distinct field targets. These distinctions agree with the PRE proof
and are represented correctly in the author runner.

The uniform-Gauss second-order cancellation is also correct:

    sum_e sigma_e q_a(e) E_e = sum_a q_a div E_a = N0,

so H2 is a scalar plus positive K sum E^2. A fixed Gauss background or a uniform
same-sign charge state was not smuggled into this identity. Periodicity requires
zero total signed charge. The author's explicit bounded-field preparation
satisfies that condition on all the stated even tori.

## 3. The finite bases differ for a physical reason

The author's guarded square has **zero frozen external electric divergence**,
so q_i=E_i-E_(i-1). Its two-record physical dimensions are 24,48,72 at S=1,2,3,
with code dimensions 4,8,12. The blind controls instead fixed external electric
divergences corresponding to background tuples (1,0,-1,0) and (1,0,1,0) in the
square restriction. These arise from frozen exterior fields, not a change to
the full lattice's homogeneous Gauss law. They produce different finite state
sets: at S=1 the blind opposite-charge and equal-charge examples had dimensions
18 and 13, with code dimensions 4 and 3. Merely rescaling those matrix entries
cannot turn them into the author's zero-external-divergence matrices.

Both controls retain the outside **occupation** guards at the B vertices. The
local penalty is the sum of internal squared occupation defects and the fixed
external squared defects. In the two-record sector it reduces to

    sum_internal_edges n_i n_j + (z-2) N_B.

These occupation guards are distinct from the chosen electric boundary data.
An isolated C4 with no guards would reach its second checkerboard after two
hops and would not be a valid gapped control of the bulk fourth-order formula.
Neither source claims otherwise.

For a decisive like-for-like comparison, the new independent checker enumerates
all four electric values first and infers matter charges from their divergence.
It builds every microscopic legal hop and the original sum-of-squared-defects
penalty, without importing either author runner. It then forms the Q-block
resolvent and both unfolded and folded fourth-order matrices. Reordering only
at the final comparison step gives exact equality for every entry in two
independently selected author sectors:

- S=1,z=6: full dimension 24, code dimension 4. Delta H2=-4I;
  Delta^3 H4 has diagonal 11 and swapped-state off-diagonal -5.
- S=2,z=4: full dimension 48, code dimension 8. Delta H2 has diagonal
  -8/3 or -4; Delta^3 H4 has diagonal 40/9 or 10 and the corresponding
  swapped-state entries -8/3 or -6. This includes nontrivial spin weights.

The earlier blind controls remain useful independent tests on different
boundary fields, including equal-charge transport. They were not replaced or
relabelled as checks on an identical finite sector.

## 4. Changed local-limit proof obligations

The complete proof's changed obligations agree with the blind reconstruction:

1. **Commuting bond penalty and finite circuit.** B is integral and is a sum of
   bounded commuting occupation terms. Conjugation of a supported operator by
   exp(i theta B) involves only penalty terms touching its original support,
   enlarging it by one halo. Terms touching the new halo but not the original
   support still cancel. Thus the explicit Fourier grade inverse is local,
   with dimension-independent norm. Its denominators involve occupations, not
   a growing enumeration of electric levels. Fixed-order colored gates give
   an exact finite-depth preparation and a controlled local remainder.
2. **Code protection.** The circuit preserves Gauss and record number.
   Hop parity removes odd code orders. At order n=3d+6 the opposite
   checkerboard cannot be reached because N0>n on every allowed torus. This
   proves invariance for the retained finite-order normal form, not exact
   checkerboard invariance of the bare microscopic Hamiltonian.
3. **Actual excited-sector speed.** Zero B-grade hops exist away from the code.
   The O(t) first normal-form term must be kept. The proof correctly uses
   v=O(epsilon_a^-3), after removing the large commuting penalty. It does not
   reuse the older O(epsilon^-2) speed from the different onsite-penalty model.
4. **Full formation source.** Dressed jumps annihilate the code only to
   O(epsilon_a). Their jump term is O(epsilon_a^2), but the dissipator's
   anticommutator is controlled only to O(epsilon_a). The proof retains the
   latter source and multiplies it by beta; it does not condition on no births.
5. **Volume amplification.** With Delta=O(epsilon_a^-4), the local remainder
   has strength O(epsilon_a^(n-3)). Multiplication by the conservative spatial
   cone volume O(epsilon_a^-3d) gives O(epsilon_a^3) at n=3d+6. The formation
   source beta epsilon_a times that volume is O(epsilon_a) for
   beta=beta0 epsilon_a^(3d). Fixed time and fixed observable support are
   essential to these estimates.
6. **Finite-S block coordinates.** The author's finite-circuit D4 may differ
   from its canonical D4 by a within-code gauge. This is explicitly allowed.
   The blind report chooses a circuit coordinate where this ambiguity can be
   removed at the relevant order. These are compatible choices, not two
   competing values for the same fixed-basis matrix. In the unit-shift
   coefficient limit D2=-M I and D1=0, so the first nonscalar fourth-order
   coefficient is invariant under the permitted near-identity block change.
   The finite-S circuit's fixed-length words then have the same rotor limit.
7. **Unbounded rotor and moments.** The target includes the common unbounded
   onsite term K sum E^2 and bounded conditional shifts/charge permutations.
   Spin shifts do not converge in uniform operator norm. The state-weighted
   O(1/C) estimate uses the supplied uniform fourth moments and their finite
   time propagation. The stated 24J(d-1) moment-growth constant is a valid
   conservative bound. Capped weights justify passage to unbounded moments;
   the strongly continuous onsite interaction-picture Dyson construction and
   commutator bounds avoid assuming norm-continuous unbounded onsite motion.

The resulting sufficient local expectation bound is the same in both proofs:

    C_(X,T) ||O_X|| [epsilon + C^-1(1+log C)^d].

Here epsilon may be either convention after adjusting constants by fixed
alpha. Constants may depend on d,K,J,beta0, the uniform moment bound, T and
observable support, but not the torus volume or S. The initial microscopic
state is the explicitly dressed code state; arbitrary entanglement and
charge/field correlations within that code are permitted. This is a
comparison to the target started from the same embedded code family, not a
claim that every sequence of such initial states converges to one universal
state. A separately specified limiting initial family would be needed for
that formulation.

A subtle but correct distinction is retained in the source: taking the
unit-shift coefficient limit before multiplying the large second-order
physical scale does not discard the physical electric term. The latter was
already extracted exactly as K sum E^2 in Eq. (6). The coefficient limit is
used only to identify the fourth-order interaction; its finite-S corrections
are bounded by the subsequent weighted estimate.

## 5. Selective execution and historical failure

`comparison_check.py` ran once successfully. It authenticates 28 PRE bindings,
18 author bindings and five contextual bindings, independently reconstructs
the two full guarded-square controls, checks the normalization symbolically,
and compares the cubic combinatorics and all recorded route denominators with
the independent formulas. No author module is imported or executed.

A separate closed halo count validates the occupancy runner's selected-edge
statistics without enumerating its 65,536 configurations again. Conditioning
on source occupied and destination empty leaves two disjoint three-site
neighbor halos and eight free sites. Thus grade g occurs

    2^8 sum_(j-i=g) binom(3,i) binom(3,j)

of the 16,384 legal selected-edge configurations. This gives
256,1536,3840,5120,3840,1536,256 for grades -3 through 3, agreeing exactly.
The 5,120 zero-grade cases are a substantive control of the full-speed issue.
The complete penalty histogram was read and its total authenticated, but was
not independently re-enumerated here. The all-size checkerboard-kernel claim
follows directly from the edge constraints, not that histogram.

All five author guarded-square outputs and both cubic outputs were read.
Only the two specified finite sectors were rebuilt in this post-seal run;
there was no broad author-suite replay or production simulation. The author's
cubic preparation has outward weights all equal to one, so equality of its
weighted and unit-shift diagonal numbers is not an independent test of
nontrivial weight dependence. Its S=2,3 guarded-square controls and the blind
nontrivial-field controls supply that additional coverage.

The preserved author failure was an `UnboundLocalError` from a missing
`for a in range(d)` in the edge-index comprehension. The complete old/current
source comparison confirms that adding precisely that clause was the only
change. The archived receipt's source/stdout/stderr were authenticated against
their archived basenames, not mistakenly against the overwritten live paths.
The failure did not change a scientific assertion. It was not replayed.
There were no new failed executions in this comparison. The invalid
old-velocity shortcut and its physical countercontrol remain in the PRE packet.

## 6. Remaining limits and disposition

No source correction is requested. This is agreement on the stated conditional
construction and bounded mathematical proof, not on a phase or a native
microscopic interpretation. The following remain outside the result:

- bare undressed quenches, automatic preparation or cooling, and arbitrary
  initial occupation patterns;
- a positive limiting birth rate, growing-time uniformity, or a claim that
  no formation event occurs anywhere in a large volume;
- a pure-gauge replacement of the actual transported charges, or transfer of
  the earlier neutral photon-packet theorem to this interacting target;
- thermodynamic phase selection, charged-band physics, an infinite-volume
  quantum field theorem or native finite-site closure;
- autonomous energy accounting for the supplied preparation and formation
  reservoir. Subtracting perturbative scalar energies does not establish it.

The independent exact controls support the load-bearing coefficients and
normalizations. The local convergence assessment rests on the reconstructed
proof with its explicit hypotheses and the identity-matched preceding
machinery. It is not inferred from finite PASS counts.

Reproduction, from this directory:

    /opt/homebrew/opt/python@3.13/bin/python3.13 comparison_check.py

The checker deliberately refuses to overwrite its existing result. To rerun,
copy the packet to a sibling directory under the same campaign root, or
preserve the existing result first; its source locations intentionally continue to name the frozen
scientific dependencies. The recorded complete execution is
`COMPARISON_CHECK.stdout`, `COMPARISON_CHECK.stderr`, and
`COMPARISON_CHECK_RECEIPT.json`. `FINAL_SEAL.json` binds this comparison and its
new evidence separately from the unchanged PRE seal.
