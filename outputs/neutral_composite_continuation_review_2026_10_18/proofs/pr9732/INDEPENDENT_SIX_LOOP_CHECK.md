# Supporting mathematical source

Scope of this supporting source: exact constructive identities retain their stated mathematical validity. Any terminal exclusion developed below is preserved as deferred science, pending its required promotion packet; it is not promoted by this extract or used to strengthen the active canonical claim.

Original: `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_SIX_LOOP_CHECK.md`, SHA256 `550b4ec45e5b5d7be39dff26b637d900cb55f42fa749b5368e5742a51f0b5450`. This extract preserves the mathematical argument and its limitations; historical execution descriptions are not fresh evidence. Current promotion boundaries: `docs/work_history/repo/review_feedback/NEUTRAL_CONTINUATION_BOUNDARIES_2026-10-18.md`. Original report and verdict history are recoverable in the archive manifest.

# Independent six-edge column-loop check

Not a complete sixth-order effective Hamiltonian or an isolated-defect-mode proof.

An independent subset dynamic program accumulates the signed amplitudes of paths indexed by used-edge subsets, rather than enumerating720 permutations. Exact Fraction arithmetic over all64 original spin assignments and both cost choices gives -3/8192 times the four-corner parity for cost4Jz, and -3/256 times that parity for cost2Jz. The original-spin factor is Zbar0 Zbar2 Zbar3 Zbar5, since only the two Y edges contribute those four original Z signs. The instantaneous-spin signs from earlier flips are retained. Every nonempty proper subset of a simple cycle has flipped sites, so no direct-path denominator is zero.

The independent controls are neutral-six-loop-independent.py/json. Root coefficient arithmetic is confirmed without reusing its permutation implementation.

## Locality and folded terms

Each vertex of this six-edge rectangle is incident to exactly two operations. For column length greater than2, these cannot flip the whole column. To return to the aligned manifold, the two flips on each column must therefore occur at the same longitudinal site. Connectedness propagates this equality around the rectangle, so all six distinct edges must lie on one slice. Mixed-slice six-distinct-edge rectangle paths do not contribute. This claim is narrower than saying that all sixth-order virtual processes lie in one slice; repeated-edge processes need not do so.

Any canonical folded contribution factors through a lower-order P return. A proper subset of the six distinct cycle edges cannot return to P: it leaves a vertex with odd physical flip parity. Consequently no folded term has the monomial containing each of these six distinct physical edges once. Repeated-edge folded terms cannot contribute to that edge-resolved multiaffine coefficient. Equivalently, for sufficiently long columns the second-order metric/Hamiltonian are scalar and their fourth-order products only dress scalar or elementary-plaquette terms, not this six-edge rectangle monomial.

This reasoning is safest stated with separate edge couplings until the coefficient is identified. Equal Jx/Jy powers alone are not enough to distinguish diagrams: other sixth-order paths with repeated edges can also have Jx^4 Jy^2 and renormalize other operators. On the simple nearest-neighbor square graph, obtaining the four rectangle-corner Z factor with the two separated odd Y edges requires the two length-two horizontal connections, so the six-step minimal cycle is precisely this rectangle. There are nonetheless other sixth-order operator terms, and their absence has not been established.

## Counting and interpretation

The corner product equals the product of the two neighboring elementary plaquette operators, since their shared middle-column Z factors square to one. There are L-2 bulk slices and two ends for an open column, so this contribution is

    -[3(L+62) Jx^4 Jy^2/(8192 Jz^5)] P_p P_(p+x).

For periodic longitudinal boundary conditions it is -3L Jx^4 Jy^2/(8192 Jz^5). The rotated rectangle exchanges Jx and Jy. The slice count assumes ordinary distinct longitudinal neighbors; L>=5 is safely within that convention. At short column lengths there may be additional lower-order or same-order tunneling processes even though the particular degree-two rectangle coefficient remains locally identifiable.

At fixed L>6 with both transverse couplings scaled by lambda, this nonconstant term is orderlambda^6 while pair-column tunneling is orderlambda^L. It therefore dominates tunneling asymptotically unless the relevant matrix element vanishes in the specific subspace being studied. Such a vanishing must be checked, not assumed. At L6 both effects compete at the same order; at L5 tunneling appears earlier. For a quantitative four-defect spectrum, all terms through the controlling order and their defect-subspace action must be retained. The earlier K4-plus-tunneling star bound and residue are not automatically native predictions for L>6.

No complete effective Hamiltonian, convergence bound, native stable particle, scalar interpretation, or uniform large-L conclusion is certified by this local coefficient check. No repository edits or formal audit were performed.

## SHA-256 identities

- `/private/tmp/neutral_rectangle_six.py`: `84b42554b4ec39dadd3085b63d7559ee0993e0a364e71f9ec45427626a7e579d`

- `/private/tmp/neutral_rectangle_six.json`: `da2941544b5c96802374e52f9e2c94520bdeb0e926e972bce3811a0db83c3a5b`

- `/private/tmp/neutral-six-loop-independent.py`: `74cea23ff2dd1945a61536467cfe3d2702d1a5e131141d7597488ae4dec65c93`

- `/private/tmp/neutral-six-loop-independent.json`: `b0c47a335c4b553872954124aed72f65e153b9779507e276c33e81dee27215a5`
