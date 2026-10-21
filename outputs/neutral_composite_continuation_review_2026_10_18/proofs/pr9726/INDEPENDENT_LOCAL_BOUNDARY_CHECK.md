# Supporting mathematical source

Original: `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_LOCAL_BOUNDARY_CHECK.md`, SHA256 `fcfce465cc7d3cfd674cafc2cc9903f0a2862dfd6984c8a20c1b0b643acc1564`. This extract preserves the mathematical argument and its limitations; historical execution descriptions are not fresh evidence. Current promotion boundaries: `docs/work_history/repo/review_feedback/NEUTRAL_CONTINUATION_BOUNDARIES_2026-10-18.md`. Original report and verdict history are recoverable in the archive manifest.

# Local short-domain canonical check

No full-channel closure or native pole is certified.

## Independent exact computation

I implemented sequential four-operation path propagation with Fraction arithmetic, separately from the root bilinear w/y/wb implementation. The direct term is PVRVRVRVP. I construct the entire energy-8 P-space columns K2=PVRVP and N2=PVR²VP, then subtract (K2_left·N2_right+N2_left·K2_right)/2. Ground energy is calculated by the same exact canonical prescription in the energy-zero sector. All eight backgrounds at both N=6 and N=8 give, after ground subtraction,

    [[47/192, -5/8], [-5/8, 47/192]].

The symmetric and antisymmetric color combinations therefore have matrix eigenvalues -73/192 and 167/192. These are eigenvalues of this submatrix, not a claim that either vector is an eigenvector of the complete K4. Both nontrivial bright second-order columns are retained. This confirms that the exploratory scalar-RS -1/192 result must not be used as the canonical boundary diagonal.

I also replayed the supplied full-wall kernel into a separate output file. All 16 oriented diagonal-color pairs give shifts ±2 equal -3/64 and shifts ±1 equal zero. The raw patch diagonal -7/48 includes its finite-patch vacuum energy; it is not the vacuum-subtracted wall excess.

## Local extension argument

K1 annihilates the diagonal-color short-domain endpoint states. Consequently the additional general canonical K4 terms containing K1 at an external endpoint vanish; the direct-minus-half-anticommutator formula is appropriate even though K2 is not diagonal.

For the boundary diagonal, a four-operation return has at most two active rungs, since every active rung must be acted on at least twice and h has no diagonal entries. Single-site and adjacent two-site contributions are local. Nonadjacent active sites have independent Hamiltonians with fixed neighbors; disconnected direct and folded energy terms cancel. Subtraction of the vacuum removes contributions wholly remote from the domain. The nontrivial K2/N2 endpoint columns connecting the two-rung domain to bright configurations are themselves supported at the short domain, so their folded correction does not grow with the remote arc.

For changing the two-rung color B6 to B9, neither rung has a one-operation matrix element between those two colors. Exactly four operations are required and all must be on the two domain rungs. Both direct and folded paths therefore fit the local patch. These observations justify the same 2×2 matrix on longer periodic chains with a sufficiently long background arc (conservatively at least four rungs), where no local connected patch reaches around that arc. This is a support argument, not finite-size extrapolation. No claim is made here about the minimal allowable circumference or small wrapping exceptions.

For the isolated-wall kernel, a two-rung shift similarly exhausts four operations. A one-rung shift can include a local loop; contributions disconnected from the moving site cancel in the canonical expansion. Thus its connected support remains in the wall neighborhood tested by the full-wall patch. Translation kernels at different nearby walls must not simply be combined when their neighborhoods overlap.

## Limits

Neither the local color matrix nor the isolated-wall kernel enumerates every output channel of the full energy-8 band. In particular, the symmetric matrix eigenvalue does not alone establish invariant half-line dynamics or absence of coupling to other dark/bright configurations. No native pole, resonance width, continuum limit, or physical scalar identification follows from this check. Root source files were not edited.

## SHA-256 identities

- `/private/tmp/neutral_domain_boundary_local.py`: `e8d802841878b611205527928405a92214932628525ba861b356ab854fa861d2`

- `/private/tmp/neutral_domain_boundary_local.json`: `d63302e4977810bf44f57df9ac282f02380520fde582599a38c5dc5f8635d41e`

- `/private/tmp/neutral_wall_full_kernel.py`: `079deaf70affd09ad6bd01b2bd790949f2a9e9c5567d2049126d5f0d8d080540`

- `/private/tmp/neutral_wall_full_kernel.json`: `1a99e7263696fdc620d2fec38d240ce73a74982f3dffeaa256cbc960dec69bbe`

- `/private/tmp/neutral-domain-boundary-independent.py`: `0fd2e1a8cd7b5cfead671709f284e6c14afbdb6e13ee11d38b05d6e9d3e99a16`

- `/private/tmp/neutral-domain-boundary-independent.json`: `d65d2c3443e56454345808b0417c89059843d35c16170a1f0d9b4c38ca4e4a95`

- `/private/tmp/neutral-wall-kernel-replay.json`: `1a99e7263696fdc620d2fec38d240ce73a74982f3dffeaa256cbc960dec69bbe`
