# Actual rotor phase observability: partial continuation result and the remaining full module

The full fixed-torus actual-source strong-stability question remains open. This attempt proves a narrower, complete-charge result: for almost every physical cycle phase, the actual canceled one-hole rotor Hamiltonian has no dark eigenvector whose hole positions fit into a slab omitting four consecutive y+z layers. It applies to coherent superpositions of the original B masks, charges and fields under that support restriction. In particular it excludes a dark eigenbranch that stays confined to the previously constructed seven-layer B strip plus parity site. It does NOT prove decay of a state initially supported there, because its dark spectral projection could extend around the torus.

This is an author discovery packet awaiting focused reconstruction, not a formal review, retained theorem, audit, milestone PR or physical-law selection. Its actual scientific control checks a primitive monodromy identity; it does not certify the full theorem.

## Exact carrier, law and ordered scope

Fix an even cubic torus L>=8, n=L³/2, supplied q=0,+1,−1 matter and integer link rotors with div E=q−1_A, global W=1, odd occupied-B count k<=n−1, and total charge n. There are M=n−1+k occupied sites, r=(k−1)/2 negative charges, and the full physical matter fiber has dimension n*binomial(n,k)*binomial(M,r). No charge-symmetric or scalar-walker replacement is made. The leading supplied rotor coefficients are H=C+[F,F*], C=sum F_a*F_a Q_gate,a and G=sum j_mu*j_mu=2 times the number of empty B neighbors of the hole. The original resolved or unnormalized coherent j_mu retain their distinct output maps.

The actual process tested here is S(u)=exp[u(−i delta H−kappa G/2)] at fixed finite graph and positive delta,kappa. The bare-Omega full effective-history source is B_mu^+ rho_eff(s) B_mu^+*, B_mu^+=−F_a j_mu F_a, with the actual electric/H4 no-event motion and all later ordinary original births inside rho_eff. Source input is not replaced by a phase packet. An eventual rotor theorem would still require a separate uniform passage to the epsilon-dependent dressed microscopic source, full neutral recycling and finite-spin long-age behavior. For any use of the older safe-torus microscopic circuit, L>=64 must be imposed separately.

## New partial proof

The exact canceled blocks retain the same-hole B reshuffles and the shared-B commutator off diagonal. On a dark input a hole move preserves the B mask and consists of two allowed charge/field transports. Between adjacent y+z planes the two inward matchings U_y,U_z have relative unitary W=U_y*U_z. Around their 2L-vertex staircase cycle, L(2L−1) shifts restore every charge and add Q_loop times the ring circulation. The ring has exactly2L−1 occupied charges, so Q_loop is odd and nonzero. Therefore

    W^[L(2L−1)] = exp(i Q_loop Phi_loop).

The finite geometric identity for I+W gives its lower singular-value bound min_odd_q |1−exp(i q Phi_loop)|/[L(2L−1)]. A flat pi z holonomy is a simultaneous ACTUAL physical witness: every such ring winds once in z, so the power is−I for every charge assignment. Missing occupied-B sites break the ring into chains, where end-row elimination gives the independent bound1/L.

The original B mask is retained only as a temporary direct-sum proof tag in the already canceled off-diagonal block. Thus no false global F* factorization or invariant-mask assumption enters. The exact highest-layer map factors into two injective matching maps. Its lower bound is eta(theta)², positive away from finitely many odd-holonomy character zero sets of Haar measure zero. The outer row then eliminates the highest occupied hole layer of a slab-confined dark eigenvector. Four omitted layers are required to prevent an opposite-side periodic two-hop contribution. All charge inverses, broken-chain rows and arbitrary mask coherences are included in STAIRCASE_AND_SLAB.md.

The result is a necessary spatial property of a persistent eigenbranch. It neither removes an extended dark subspace nor proves that a local source is orthogonal to that subspace. The phase value where the old strip mode exists lies in the exceptional set, consistently with this result.

## Exact full-sector and actual-source tests

A physical spanning-tree representation gives d_c=2L³+1 cycle phases and actual finite Laurent matrices H(z),G. For d_f equal to the full fiber dimension, the stack O(z)=[G;GH;...;GH^(d_f−1)] has kernel equal to the maximal invariant dark space on the unit torus. Terminal no-original-event mass is exactly Tr(P_kerO rho), by finite-dimensional spectral decay on the complement and direct-integral dominated convergence. This statement retains field coherence; no phase dephasing is applied.

Full almost-everywhere strong stability is equivalent to a nonzero maximal Laurent minor. If generic rank fails, fraction-field elimination and denominator clearing instead produce a nonzero Laurent vector v with G H^m v=0 for every m. Its inverse Fourier transform is a normalizable finite-field physical invariant dark input. No such minor or null vector was found. This is an exact target-strength criterion, not a solved observability lemma.

To turn a null vector into an actual sourced counterexample one would additionally need nonzero Laurent overlap with a COMPLETE legal original source word B_mu^+ b_mu_m ... b_mu_1 Omega. A scalar Laurent shift selects a nonzero global overlap; strong waiting-time continuity and the positive original history expansion then give genuine positive source weight. No such pair was found. Conversely, checking a collection of zero-waiting words for orthogonality does not control the interspersed actual electric/H4 evolution.

There is an exact resource discriminator against copying the cube's short stack. At k=n−1 the bright space has dimension6n*binomial(2n−2,(n−2)/2), while d_f=n² times that binomial. Full observability therefore needs Krylov depth at least ceil(n/6)−1. Lower-depth stacks have Laurent null vectors by dimension alone, but these certify only finite dark prefixes. No enormous matrix was assembled, no rank was sampled and no generic weighted-graph theorem was imported.

## Closest prior and failed extensions

The landed cube strong-decay and five-angle-tail arguments were read in full. They use a96-dimensional physical fiber, a72-by24 bright/dark block, zero dark-dark block, a nonzero exact minor and120 rational Laurent identities on five cycle variables. Their block compensation and preparation differ from the present torus. The actual cube full-source tail also assumes its own canonical smooth preparation and weighted source inputs. None is silently promoted to a bare-Omega torus result.

The checked finite-global-k theorem on Z³ and periodic L>=4k uses a clipped height. The checked periodic dark packet and actual-source polynomial lower tail rule out certain uniform exponential estimates but do not decide almost-everywhere absorption. The known strip mode is a particular flat-phase family; it does not prove a positive-measure dark branch. ATTEMPTS.md records the unresolved periodic recurrence, actual same-hole mask-changing word, failed independent-weight/complex-phase shortcut and full-source orbit obligation.

## Actual execution and limitations

The standalone check_staircase_monodromy.py tracks each primitive inward/outward charge hop, exact integer electric increments and endpoint Gauss identity in independent formal charge symbols. For L=8,16,24,32 it verifies the complete charge permutation, every ring-edge circulation coefficient and the−1 pi-z sign. The formal coefficient identity specializes to every physical ± assignment; it is not an independent-charge distribution or an enumeration of the physical Hilbert space.

Frozen budget was5 CPU seconds,30 wall seconds and100 MiB, with BLAS1. CPU was hard-limited, wall time managed, and peak RSS postchecked (not an OS memory cap). Actual result: exit0, TOTAL PASS=4 FAIL=0,0.535318 child CPU seconds,0.549306 wall seconds and15,532,032 bytes peak RSS. Original deadline/STOP checks passed in the wrapper. stdout SHA27966722fdb69bd865a80e18f1d44c901cd0fe52f48d480f1608d338b09d22a6. An earlier setup command used absent python and exited127 before creating the wrapper or running science; LAUNCH_FAILURE.json preserves that actual failure. The corrected executable was python3. No scientific retry or expectation change occurred.

The theorem remains analytic. No all-charge Hilbert matrix, full rank, actual Omega probability, finite-spin survival, uniform rate, quadratic UI or physical-time work estimate was computed or claimed. The exact open consumer remains full actual phase observability OR dark-projector orthogonality to the complete actual source orbit, followed by the separate quantitative microscopic crossover obligations.
