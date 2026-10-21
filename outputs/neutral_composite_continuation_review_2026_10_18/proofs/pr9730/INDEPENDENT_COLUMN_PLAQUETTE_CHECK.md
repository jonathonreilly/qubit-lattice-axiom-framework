# Supporting mathematical source

Original: `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_COLUMN_PLAQUETTE_CHECK.md`, SHA256 `bbb79ed6935817b95afadb8fecd54fd62ebcc457bbbd0f92a3ceb9e55a7359ef`. This extract preserves the mathematical argument and its limitations; historical execution descriptions are not fresh evidence. Current promotion boundaries: `docs/work_history/repo/review_feedback/NEUTRAL_CONTINUATION_BOUNDARIES_2026-10-18.md`. Original report and verdict history are recoverable in the archive manifest.

# Independent aligned-column plaquette check

This is a focused derivation check, not a formal audit or a nonperturbative phase-selection result. No repository files were changed.

Assume H0=-Jz sum longitudinal ZZ with Jz>0, V=-Jx sum transverse XX-Jy sum transverse YY, a simple square transverse nearest-neighbor graph, and aligned column manifold P. No four-column parity restriction is imposed. Couplings are uniform along a column and the same for the corresponding edge orientations. Different boundary conditions or duplicate transverse bonds require separate counting.

## Exact signed paths

I independently enumerated all24 orders of the four distinct edges X01,X23,Y02,Y13 using exact Fraction arithmetic, for all16 aligned computational spin assignments. For -XX the action coefficient is -1. For -YY it is +s_a*s_b evaluated on the CURRENT spins, including earlier flips. An intermediate flipped physical spin costs4Jz at a bulk slice and2Jz at an open end. Thus the denominator after each proper subset is minus that cost times the number of flipped spins; for the second step the subset may contain two or four flipped spins. The enumeration keeps these differences and noncommuting signs.

Every case gives

    bulk: -Jx² Jy²/(128 Jz³) * Zbar0 Zbar1 Zbar2 Zbar3,
    end:  -Jx² Jy²/(16 Jz³)  * Zbar0 Zbar1 Zbar2 Zbar3.

The control is neutral-column-plaquette-independent.py/json. It is not a numerical rational fit.

## Mixed longitudinal positions

For L>=5, a four-operation process cannot flip an entire column: each transverse operation changes at most one spin in any particular column, so at least L operations would be required. Therefore returning to P at order4 requires an even number of flips at every individual physical site, not merely every column.

In a four-distinct-edge plaquette process, each participating column has degree two. Its two incident edge operations must occur at the same longitudinal site. Following the connected square forces all four operations to share one slice. Thus there are no mixed-slice contributions to this four-edge plaquette monomial. This argument also applies at open ends and does not assume a positive plaquette parity. Repeated-edge processes can occur at different slices, but they carry no four-distinct-edge coupling monomial and their original aligned-spin factors cancel in pairs.

## Canonical folded term

PVP=0. At second order, the only return is the same physical edge at the same slice twice: no entire column can flip, and two distinct edges leave a physical site flipped. Both K2=PVRVP and N2=PVR²VP are therefore scalar on the aligned-column manifold; the denominators depend on location but not on aligned column signs. Consequently -{N2,K2}/2 changes only the scalar fourth-order energy. It cannot change the plaquette product coefficient. All proper subsets in the four-distinct-edge direct process remain outside P, so the direct resolvents used above are appropriate.

On a simple square transverse graph, a four-edge connected even-degree graph with four distinct edges is an elementary plaquette. This excludes an uncounted distinct-edge geometry at this order under the graph assumption. Exceptional transverse periodic identifications/small circumferences should not be silently included.

## Counting and scope

An open column of L>=5 has L-2 bulk slices and two ends, yielding -(L+14)Jx²Jy²/(128Jz³) per plaquette. A periodic column of L>=5 has L bulk slices and yields -L Jx²Jy²/(128Jz³). Positive plaquette parity is energetically favored by this leading nonconstant fourth-order effective term when both transverse couplings are nonzero. Pair-column tunneling requires at least L transverse operations, so at fixed L>=5 and sufficiently small common transverse scale it enters after this fourth-order splitting.

This statement does not prove an exact parity constraint, a unique ground state, a uniform-in-L perturbation remainder, a large-array phase, or a three-dimensional scalar. Multiple plaquette constraints can leave degeneracy. Selection at leading order must be distinguished from imposing positive parity as an input. The coefficient is derived from the supplied native bonds and introduces no new interaction premise.

## SHA-256 identities

- `/private/tmp/neutral-column-plaquette-independent.py`: `fe413e063d7c6594f7aefacd20bf053c0157409dede583b5fcb4c663b227af25`

- `/private/tmp/neutral-column-plaquette-independent.json`: `a13ac1598bd8bd1f3f6225df60b2b64c31b609e29e0567bbaf6f19cf2bce49ce`
