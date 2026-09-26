# Three-note quantum-interface review

No unresolved mathematical finding was identified at the frozen source
identities below. No source correction is requested. The conclusions concern
the specified encodings, channels and finite local operators; they do not
supply a native quantum dynamics or a phase theorem. This is independent
scientific scrutiny, not an audit or retained-status decision.

## Source and independence boundary

All three notes were read completely before the new author checkers or results:

| Source | SHA-256 |
|---|---|
| `GEOMETRIC_SINGLET_FIBER_AND_LOCAL_HAMILTONIANS.md` | `106f126b17231b6a859cb5c47ee59ff969a32b299244524e152b43ecbce8e468` |
| `GEOMETRIC_SINGLET_CHANNEL_AND_COHERENT_FILTER.md` | `20c2429ad7e86e44ff7a5dc07f716420057d023615d6a2899fc08ea3a7e29864` |
| `DIMER_COLOR_OPERATIONAL_MOMENT_MAP.md` | `042961d86c6d67ee521b1c9695126baf63a8ae6718cfcbdf586d067abc29c25c` |

The corrected routed note and earlier orthogonal-fiber review were reused at
the identities in `PRE_COMPARISON_SOURCES.json`. The derivation and three
independently written controls were sealed in `PRE_COMPARISON_SEAL.json`,
SHA-256 `3f569df2704a057bb24399c0b948c8f4a4c38e735da93cda455bdc59aa2a1d02`,
with 24 artifacts and 12 source/dependency bindings. Only after that seal were
the new author code, outputs and preserved attempts opened. The complete
precomparison derivation is `INDEPENDENT_DERIVATION.md`; it remains unchanged.

## Operational moment map

The decisive ensemble claim reconstructs with the actual tilted birth law.
In the singlet/vector Bell basis, the stipulated antipodal product state is

`rho_n = 1/2 [[1,n^T],[n,n n^T]]`.

Every quartic color class is even under n -> -n. The reference density is
proper-cubic invariant and even, so the class mass and second moment are
unchanged by the factor `1+epsilon n.delta`, while the first moment becomes
`mu_{a,delta}=epsilon M_a delta`. Omitting this first moment would be wrong;
the source retains it. Positivity on an open spherical patch gives positive
covariance and a rank-four averaged pair density for the stated interior
parameters.

The A stabilizer forces `M_(A,+x)=diag(a,b,b)`. The B111 stabilizer forces
`M_(B,111)=(1/3-c)I+c11^T`. Proper rotations carrying each representative
color to its opposite preserve these matrices. Hence, at the same fixed
delta, `rho_(a,delta)=rho_(-a,delta)`, including the tilt. The proof uses the
proper 24-element cubic action; it does not require an invalid polar-vector
transformation of the even quartic code under inversion.

All seven odd opposite-color population directions are in the quantum
moment-map kernel. The six classical vector fields have rank six on that
space. The affine quantum image has at most five tangent dimensions, so the
kernel on the thirteen-dimensional population simplex has dimension at least
eight; the source does not claim the displayed seven directions exhaust it.
The even A-versus-B orbit-mass contrast supplies another invisible direction.

This is a conditional comparison at fixed within-class birth ensembles and
fixed edge directions. Under independent pair preparation, tensor products
and common quantum channels preserve the indistinguishability. It is not a
statement about arbitrary correlated late-time key ensembles or about many
copies of one fixed unknown n. The source explicitly distinguishes these
resources and does not identify its classical label-reading dynamics with a
quantum channel. The nontrivial propagating-mode reference inherits the
nonzero coupling/mode and isotropic hypotheses of the checked routed theorem.

The guessing bounds also reconstruct: at zero tilt `rho_a<=I_4/2`, and the
tilted density is at most `(1+|epsilon|)rho_a`. Uniform fourteen priors therefore
give upper bounds `1/7` and `(1+|epsilon|)/7`. These are not asserted optimal.

`quantum_core_check.py` independently checks all 24 polynomial covariance
identities, proper stabilizers, explicit open-class witnesses, exact finite
even-orbit densities at a nonzero tilt, positivity, opposite-density equality,
and the population kernel. The finite orbit moments are explicitly controls
of the symmetry/algebra, not estimates of the continuous class moments.

## Channel and coherent-filter boundary

For bipartitely oriented singlet covers, every Gram entry is positive. If a
trace-preserving channel maps each orthonormal matching basis input to its
specified pure cover output, its Stinespring vectors have form
`D_M tensor e_M`. Input orthogonality and nonzero cover overlaps force the
environment vectors to be orthogonal. The channel consequently erases every
input off-diagonal and is exactly the stated measure-and-prepare channel.
This reasoning remains valid when the cover columns are linearly dependent.

On the square, the coherent equal-cover state and this channel's output have
trace distance 1/4. A supplied scalar coherent filter `aD` is an allowed
success operator exactly when `|a|^2 G<=I`; the optimal scale is
`1/lambda_max(G)`. Basis success and success on an arbitrary superposition
must be distinguished. A top Gram eigenvector succeeds with probability one;
kernel inputs have zero success. A complementary failure effect completes
the instrument.

The tiled-torus principal Gram argument is correct: P=N^3/4 disjoint
plaquettes yield a tensor-product Gram with top eigenvalue `(3/2)^P`, hence
basis success at most `(2/3)^P` for this scalar map on all matching inputs.
This is not a lower bound on the cost of directly preparing one selected
coherent state. Orthogonal markers, modified output targets, approximation
and different preparations remain outside that obstruction, as the source
states. None of these mathematical operations is supplied by the classical
record process itself.

The independent checks include actual square spin columns, channel Kraus
operators, trace distance, complete success/failure effects, a singular-Gram
countercontrol, an orthogonal-marker isometry, product Grams, and three actual
matchings in an N=8 tiled torus. The exponentially large full torus Gram was
not enumerated.

## Signed fibers, physical metric and finite local operators

The signed fiber contains `2^K K!` assignments, with the product of the
black-sublattice record signs. Each elementary plaquette rotation reverses
two pair orientations and preserves that sign. The two half-amplitude
rotations give the claimed QDM intertwiner. Antisymmetrizing each SU(2) key
frame and summing its K! assignments gives physical image `sqrt(K!) D_M`.
Independent rephasing of the fixed record representatives contributes a
common inventory phase, rather than a matching-dependent change.

The exact overlap is `G_MP=2^(ell(M,P)-K)`, with common edges counted as
doubled overlay loops. Hermitian physical intertwining requires
`[G,H_QDM]=0`; invertible G makes the displayed nonlocal lift sufficient.
Compressed operators are self-adjoint in the G metric. This does not make
their coefficient matrices ordinarily symmetric or prove locality.

The square imposes no condition on v,t. The six-site ladder requires v=t/2.
The cube has two independent metric conditions, leaving only v=t=0 in the
specified two-parameter QDM family. The finite parent includes every cover
because its star projector annihilates the antisymmetric singlet pair, but
its kernel can be larger. On the open cube the exact kernel dimension is 19,
with ten singlets and three spin-one multiplets, versus cover dimension nine.
The smallest positive eigenvalue, about 0.6125741132772056, is a finite
numerical quantity, not an infinite-volume gap.

Independent exact leakage results for `W_ring+alpha W_NN` are:

| Open patch | Cover rank | NN / ring leakage ranks | Best alpha | Minimum squared leakage |
|---|---:|---:|---:|---:|
| 2x2 square | 2 | 0 / 0 | unrestricted | 0 |
| 2x3 ladder | 3 | 1 / 1 | -1 | 0 |
| 2x2x2 cube | 9 | 1 / 1 | -2 | 0 |
| 2x4 ladder | 5 | 3 / 3 | -21/23 | 33/46 |
| 2x2x3 patch | 32 | 24 / 27 | -29041/21729 | 348331597/3911220 |

The twelve-site separate NN and ring squared norms are 7243/120 and 1575/8,
and their leakage inner product is 29041/360. The eight-site ladder residual
at alpha=-1 is 3/4. On the cube the leakage of either operator is outside the
entire parent kernel, not merely outside the nine-dimensional cover span.
These checks confirm both the small-graph cancellations and the stated
boundary of this two-operator family. They do not exclude other local models.

`singlet_local_check.py` constructs signed integer spin columns and actual
qubit permutations independently of author code. Exact rational small-Gram
calculations use the 924-dimensional zero-magnetization sector for twelve
sites. All nine cube magnetization sectors are separately checked. The square
singlet-edge expectations are 3/4 coherent, 5/8 incoherent and 1/2 as classical
matching occupation. `extra_pair_controls.py` separately rephases individual
record vectors and reconstructs the antipodal separable mixture spectrum
`1/2,1/6,1/6,1/6`.

## Author comparison, failures and verification limits

After sealing, all seven relevant current checker sources were read in full:
the fiber, parent, dense combination, original Gram, fast Gram, channel and
moment checkers. The five completed result files and all corresponding logs
were read completely. `compare_author.py` authenticates 13 recorded result
source bindings and compares the five local patch results, integer overflow
bounds, cover Grams, parent sectors, compressed-operator spectra, channel
filter quantities, tiled spectra and all twelve moment LDL pivot rows. Its
moment pivot check uses leading-principal-minor ratios, rather than rerunning
the author's LDL routine. No author checker was executed.

The five completed result hashes are:

| Result directory | SHA-256 of RESULTS.json |
|---|---|
| `geometric_singlet_fiber_checks` | `984d2154b73e270be8059985b04d9bdd5f703022d9b89d8be937fa9006145d10` |
| `geometric_klein_parent_checks` | `bd2fa94f5f4715fc36c929097be5d7770e6bd903a280814d4a93641e840e39e7` |
| `geometric_local_quantum_gram_fast_checks` | `907a15ef424ec3a14a72755e229b5e85d0ba688526daa6f293e2c21676e0fc58` |
| `geometric_singlet_channel_checks` | `f473f516f21f12713aa3e1e24e3cf8f9925e064f35ad62a78738a424c5ab9388` |
| `dimer_color_operational_moment_checks` | `aede8caa88a4ed4c4fcac9967c5fd678285c605691eb4eea3578c0e51a3b9c63` |

The dense and original Gram attempts completed four patches before their
twelve-site step was stopped. They were not treated as five-patch results.
The fast-Gram list/tuple assertion repair and channel symbolic-equality repair
were checked by complete before/after source equality under the single stated
replacement. Neither changes its scientific definitions. All completed
author stderr files are empty; preserved historical errors remain intact.

Our own first local-spin attempt was stopped after 236 seconds without an
assertion failure. The preserved source/logs show the completed earlier
groups; exact rational-domain rank/nullspace elimination then completed the
same matrices in about twelve seconds. The postcomparison helper first had
a missing bracket and did not parse; that source and failure are also
preserved. The corrected comparison passed. All 24 precomparison artifacts
were reauthenticated unchanged afterward.

Only version-specific abstracts/bibliographic pages of the three contextual
papers were checked, after the independent seal. They support the stated
decoration premise, numerical coexistence result and anisotropic trial-state
setting: [Raman–Moessner–Sondhi v2](https://arxiv.org/abs/cond-mat/0502146v2),
[Albuquerque–Alet–Moessner v2](https://arxiv.org/abs/1204.3195v2), and
[Xu–Beach v1](https://arxiv.org/abs/1311.0004v1). This review does not verify
their full proofs or simulations, nor exhaustively verify the contextual
statement that the last paper supplies no parent Hamiltonian. None is a
theorem import for the checked finite algebra. The precise read boundary is
recorded in `EXTERNAL_CONTEXT_RECEIPT.json`.

Reproduction instructions, complete commands, stdout/stderr, receipts and
source manifests are preserved beside this report. No production source,
older sealed packet, Git state, publication, or audit status was modified.
The separately queued alternative mixed encoding remains outside this packet.
