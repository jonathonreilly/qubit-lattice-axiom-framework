# Competing native orders and a column collective mode

Claim type: bounded_theorem.
Primary runner: [native_column_collective_mode.py](../scripts/native_column_collective_mode.py).


Status: conditional-support; fixed-order effective-mode derivation. The same one-qubit Hamiltonian produces both the plaquette interaction and the terms that change its collective spectrum. The simpler two-term truncation gives a misleading lower bound mode for long columns. A corrected order-six operator for open length-six columns retains an upper mode with a derived original-readout coupling, but negative small-momentum curvature. These calculations do not establish a relativistic scalar or an exact native pole.

Premises: supplied directional Hamiltonian, Jx=Jy=Jperp=lambda Jz, open longitudinal length L=6, and an even-by-even periodic transverse array with both circumferences greater than six (excluding extra short winding loops). The calculation follows [native plaquette selection and readout](NATIVE_COLUMN_PLAQUETTE_SELECTION_NOTE_2026-10-18.md) and [column tunneling](NATIVE_LARGE_COLUMN_DYNAMICS_NOTE_2026-10-18.md). All computations are exposed model development. No physical calibration or empirical test is made.

## The omitted term is larger than tunneling for longer columns

A transverse2x1 rectangle has six perimeter edges. Exact summation of all720 signed orderings gives the connected coefficient

-3 Jx^4 Jy^2/(8192 Jz^5) times the product of its four corner column signs

per interior longitudinal slice, and -3 Jx^4 Jy^2/(256 Jz^5) per end slice. The corner product is P_p P_(p+x), a product of neighboring elementary plaquette parities. Rotation exchanges x and y. Sitewise return again forces the six distinct edges onto one slice. Folded terms cannot change this six-distinct-edge monomial: lower returning subgraphs do not partition that perimeter.

Thus open columns acquire

-K6 sum_<p,q> P_p P_q,
K6=3(L+62) Jperp^6/(8192 Jz^5).

The pair-column tunneling scale is t=Jperp^L/(2Jz)^(L-1). For L>6, K6 precedes t in the small-lambda expansion. Keeping t while omitting K6 is not a consistent native asymptotic approximation. The earlier exploratory star result without K6 is preserved only as a diagnostic of that truncation.

For L=6, t=lambda^6 Jz/32 and K6/t=51/64. Through order six, diagonal closed walks produce constants, single-plaquette renormalizations and these adjacent-plaquette products. At each longitudinal slice the return graph has even degree. A six-edge simple cycle is a2x1 rectangle; repeated-edge walks reduce to a square or a constant. Mixed-slice returning walks can renormalize a square but cannot create an additional six-edge perimeter monomial. The first off-diagonal aligned-column process is reversal of two adjacent complete columns, also at order six. For even L its X and Y edge projections both give -t Xbar Xbar.

A common single-plaquette order-six correction has not been evaluated here. It shifts all four-defect energies equally and does not determine the binding gap, eigenvectors or leading readout computed below. Consequently this note reports energy relative to that common four-defect reference, not an absolute mass through order six.

## The complete four-defect geometry and visible component

The finite defect matrices are restricted to the simultaneous +1 eigenspace of every logical row and column X-flip symmetry. This is a declared sector/state choice, not a derivation of the vacuum. The kernel of the map from column signs to plaquette signs consists of row/column flips and has size 2^(Nx+Ny-1). For each allowed plaquette pattern P, use the normalized equal superposition of its entire kernel fiber. A pair-column X flip maps one such fiber state to another with unit amplitude, and all diagonal plaquette terms are constant on the fiber. This proves the defect quotient used below within this symmetry sector; it is not the full logical Hilbert space. For even L=6 and even transverse periods these logical symmetries agree with the inherited physical plane-flip symmetries, with the Y-column phase canceling across an even row. The P=+ vacuum is this sector-selected superposition. Global logical Z parity is well-defined in the quotient because every row/column has even length, and the source stays in its even sector. Translation orbit states are then normalized by the square root of their distinct defect-pattern orbit size, giving the size-ratio factors in the runner.

Plaquette signs on a periodic array obey even parity in every row and column. Four defects therefore occupy the corners of a rectangle. In the even logical-flip sector reached from the chosen vacuum by pair-column flips, the rectangle area is even. A pair-column flip changes the four plaquettes at the corners of a2x1 or1x2 rectangle.

At first order within the four-defect sector, two such masks must share exactly two corners to preserve defect number. Starting from the original readout source, the connected component consists of a central2x2 rectangle and four arms. Two A arms contain width-one rectangles of even length; two B arms contain width-two rectangles of length at least three. Each move changes one edge of the rectangle. At zero momentum the hopping magnitude along every arm and from the hub to each arm is2t.

Other rectangles with both sides at least three are frozen at this order. They remain in the complete four-defect sector but outside this source component. Finite periodic arms eventually fold and join; those effects are included in the finite-orbit calculation, not confused with the infinite-arm limit.

Four isolated plaquette defects cost32K6 from the neighbor interaction. Each adjacent defect pair saves4K6. A-arm rectangles have two such pairs and cost24K6; the hub and B arms cost32K6. Subtract24K6 and express energies in units t. The hub and B arms then have offset delta=8K6/t=51/8, while A arms have zero offset.

## Bound modes after including the competing term

For a halfline of hopping2, define g(E)=(E-sgn(E)sqrt(E^2-16))/8 outside its band. Eliminating the four arms yields

E-delta = 8 g(E) + 8 g(E-delta).

Without the native neighbor term, delta=0 gives roots +/-8/sqrt(3). The separate lower-root exclusion at the actual offset is preserved with the complete secular proof as deferred scientific source pending promotion. The constructive upper root at delta=51/8 lies above delta+4:

E_upper=10.453351015278818,
E_upper-(delta+4)=0.078351015278818.

These are numbers of the derived order-six operator, not fitted masses. The complete translation-zero finite-orbit matrices at transverse sizes12,20,40,60 converge toward this root and its source residue, while their lowest source-component energies approach the A continuum edge -4.

Let ga=g(E_upper), gb=g(E_upper-delta). The hub probability is

Zhub=[1+8ga^2/(1-4ga^2)+8gb^2/(1-4gb^2)]^(-1).

For the source with equal unit amplitude on the two A endpoints, norm squared2, the mode weight is16ga^2 Zhub=0.0303796635305604. The normalization is retained explicitly below.

## The original readout needs both direct and induced terms

Use O=C/sqrt(Ncolumns), where C is the original sum of longitudinal distance-two Z products. This is a per-column normalization; normalizing by the number of physical sites instead divides the final weight by L.

The order-four diagonal coefficient is c4=-3(L+13)Jperp^4/(128Jz^4), multiplying sum P. Ground-state mixing by the inherited pair tunneling gives a source amplitude -c4 t/K4 on each elementary rectangle. That is not the whole answer: the original readout also has a direct off-diagonal contribution at order L.

Use H+sC only as a derivative device. A subset S of flipped sites in the two-column tunneling process has denominator4Jz w1(S)-4s w2(S), with w1 and w2 its nearest- and distance-two wall counts. Exact subset recursion differentiated at s=0 gives t'_6=6t/Jz. The direct projected readout is therefore -t'_6 times the pair-flip operator. The projected canonical connection cannot mix aligned configurations before order L; its lower diagonal real anti-Hermitian terms vanish, and commutators with lower scalar energies do not alter this coefficient.

Combining the direct and mixing terms at L=6 gives

a_source = -t'_6 - c4 t/K4 = -(63/20)t/Jz.

Thus the original normalized readout weight in the surviving upper mode is

(63/20)^2 (t/Jz)^2 [16ga^2 Zhub]
=0.3014422113819855 (t/Jz)^2.

No detector coupling was supplied. This is a matrix-element coefficient for a declared microscopic observable; identifying that observable with a physical apparatus or cosmological field remains open. The small scale and weak weight follow together from the same microscopic expansion.

## Propagation is not relativistic scalar dynamics

At general small transverse momentum, arm hoppings are ax=2cos(qx/2), ay=2cos(qy/2), bx=2cos(qx), by=2cos(qy). The A arms change their long side by two sites, whereas the B arms change by one. With g_b the halfline resolvent of hopping b, the secular equation becomes

E-delta = ay^2 g_bx(E)+ax^2 g_by(E)+ay^2 g_ay(E-delta)+ax^2 g_ax(E-delta).

The upper branch expands as E(q)=E_upper-0.26355763230115514(qx^2+qy^2)+higher terms. Its zero-momentum point is a local maximum. One cannot interpret this as a positive-gradient relativistic scalar action merely because the excitation is neutral and square symmetric. Direct translation-orbit matrices at transverse size60 and momentum indices (1,0), (1,1), (2,0) agree with this halfline equation to within6.2e-6 in energy. Further native order control remains open.

## Claim boundary

The six-edge coefficient, finite-L source derivative and leading visible operator are derived from the supplied Hamiltonian. The isolated root belongs to that order-six source component; it is not yet an exact native infinite-array eigenmode. Higher native orders, transitions between defect sectors, the uncomputed common mass shift, prepared-state selection, isotropic continuation and physical observation bridge remain open. For L>6 still more diagonal orders may precede tunneling, so the length-six result must not be extrapolated by substituting a larger L into t alone.

## Reproduction

Run `python scripts/native_column_collective_mode.py`. It repeats exact signed six-edge paths, finite-column source derivatives and complete finite translation-orbit matrices, including momentum checks. The source-bound result distinguishes coefficient-operator calculations from full microscopic diagonalization. Independent checks are recorded in the campaign pack.

## Source and promotion boundary

The signed six-cycle coefficient and constructive upper star root/readout remain live. The lower-root criterion applies to the displayed quotient and source component; its negative promotion is packet-pending and its full secular proof remains inspectable. Negative small-momentum curvature identifies a local maximum of this branch only.

Full supporting mathematics and provenance are indexed in `outputs/neutral_composite_continuation_review_2026_10_18/INPUT_CLOSURE.json`. The scope register is `docs/work_history/repo/review_feedback/NEUTRAL_CONTINUATION_BOUNDARIES_2026-10-18.md`. The primary binds literal source/input identities, stages owning-head helpers and frozen inputs in a temporary directory, and captures their diagnostics. Frozen expensive producers are provenance only and are not rerun. Historical reports and executions do not supply a fresh verdict.
