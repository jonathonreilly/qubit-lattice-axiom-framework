# Repo search

FINISH row 1435, pin `45a4ff04184a0f8f7c4ab2cb6fd12080185c08b1`. The November 8 search covers thirteen earlier targets. The closer search is row 1425's comparison on main and PRs 10114, 10133, 10134 and 10141. I checked main's two T6 entries (character duality and a finite-loop bootstrap), its planar Gram form (6.2), and PR 10114's single-loop transfer estimate and finite ribbon tests. None computes this marked four-cube contraction. The exact proposed theorem names had no Lean hit on fetched main, those four local PR refs or PR 10144. The registry's Haar change-of-variables row concerns a different operation. There is no target-specific prior note. [Lead's digest](prior/repo-search-2026-11-08.md) · [Row 1425 and its sources](gap-rg-ring-sign-astra62.md)

Rows 1341 and 1424 supply the sphere-coordinate moments and rooted trace observable. Row 1425 supplies the paths, phase convention and expected table. Row 1432 already kernel-checked interval arithmetic and rational addition on the literal histograms. Row 1433 independently decoded all 1,897 marked and 96 vacuum rows, including thirteen signed zeros, and explicitly left Stage 2 open. I use their targets for comparison. [Row 1424](gap-rg-two-cycle-astra62.md) · [Row 1432](gap-rg-ring-lean-replay-astra62.md) · [Row 1433](gap-rg-ring-lean-replay-check-opus.md)

Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, give the product-Haar, reversed-bond and Wilson conventions at outline 238–278, the character coefficients at 2195–2243 and the unit-quaternion trace at 2773–2781. CA-I 43099–43109 defines the constrained Wilson action. I checked the outline index, neighbouring rows, obligations and CA index before consulting these passages. These sources supply conventions. The finite contractions below are for the row-1425 graph. [Outline index](sa-index/README.md) · [Outline at 31a47c543775](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2773-L2781) · [Complete account I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L43099-L43109)

## Finite result

The kernel checked the marked orbit histogram through face degree 46 (Taylor degree 42) and the vacuum through degree 28. The marked census contains **3,748,591 labelled assignments, 1,897 rows and 13 signed-zero rows**. The vacuum contains **30,034 labelled assignments, 96 rows and zero signed-zero rows**. Both histograms use the nine literal fields of row 1432. The separate positive transfer counts every marked shell through face degree 46.

The signed local recoupling comparison covers 1,846 ordinary and 1,242 marked entries. The independent quaternion-moment calculation gives eleven labelled degree-16 supports, the orbit multiplicities $4,4,2,1$ and total $15655/169075682574336$. This is finite research evidence. The integral identifications and analytic estimates below remain open. [Lean source](../lean/haar/Haar.lean) · [Kernel receipt and replay](../lean/haar/RECEIPT.md)

The executable replay reconstructed 429 temporary declaration groups from the one delivered Lean file. Each group passed the kernel, including the theorem joining every shell. The bounded enumeration and signed table comparisons are closed Lean statements. The pruning and equal-cardinality arguments relating them to the unrestricted triangle formulation are given below.

The separate single-process run of the delivered source took 368.46 s and reached 2,214,871,040 bytes peak RSS. The 2 GiB process guard stopped it before completion.

## Marked shell comparisons

| Face degree | Taylor degree | Labelled assignments | Histogram rows | Signed-zero rows |
|---:|---:|---:|---:|---:|
| 20 | 16 | 11 | 4 | 0 |
| 22 | 18 | 62 | 7 | 0 |
| 24 | 20 | 178 | 10 | 0 |
| 26 | 22 | 466 | 14 | 0 |
| 28 | 24 | 1,329 | 23 | 0 |
| 30 | 26 | 3,522 | 39 | 0 |
| 32 | 28 | 8,733 | 49 | 1 |
| 34 | 30 | 21,080 | 80 | 1 |
| 36 | 32 | 48,152 | 113 | 0 |
| 38 | 34 | 105,962 | 138 | 3 |
| 40 | 36 | 227,239 | 209 | 1 |
| 42 | 38 | 472,658 | 293 | 1 |
| 44 | 40 | 959,331 | 373 | 3 |
| 46 | 42 | 1,899,868 | 545 | 3 |

Each shell checks both the integer coefficients and equality of its orbit-weighted cardinality with the independent positive transfer. A signed-zero row has at least one nonzero summand. Assignments with an individually vanishing weight still participate in the cardinality. At face degree 20 the four geometric weights in row 1432 literal order are $10,40,-160/3,60$.

The signed-zero keys below give the multiplicities $(e_1,\ldots,e_7)$ of twice-spins 1 through 7. Their literal denominators are all one.

| Face degree | Multiplicity keys |
|---:|---|
| 32 | `(13,5,3,0,0,0,0)` |
| 34 | `(1,9,5,0,0,0,0)` |
| 38 | `(0,15,0,2,0,0,0)` · `(5,5,1,5,0,0,0)` · `(6,4,4,3,0,0,0)` |
| 40 | `(6,5,5,1,1,0,0)` |
| 42 | `(4,0,8,2,0,1,0)` |
| 44 | `(7,5,3,3,0,1,0)` · `(9,3,0,2,3,1,0)` · `(9,7,0,4,1,0,0)` |
| 46 | `(6,2,6,3,0,1,0)` · `(6,5,7,1,1,0,0)` · `(7,0,7,3,0,1,0)` |

## Construction record

### Initial plan

1. Record the toolchain, source revisions, and the Stage 2 obligations that remain open.
2. Reconstruct the finite assignment count, recoupling weights, and sphere moments from definitions. Compare them with the row 1432 literals and test the requested incorrect fixtures.
3. Run Lean with one worker, retain its axiom output and resource measurements, and distinguish finite equalities from their identifications with integrals.
4. Record any remaining proof obligations and the decisive outcomes for the next two rows.

### Completed checks

1. The first kernel checks fixed the local sign and the leading orbit sizes. Splitting the local test at $(a,b)=(4,4)$ by $t$ brought the exhaustive polynomial comparison within the memory limit.
2. Direct recursive normalization of a sphere trace exceeded the limit. Sharing 872 trace-word contractions gave a typed proof for every child of all 55 input products.
3. The independent native cap-first traversal agreed with all 1,897 marked and 96 vacuum reference rows. It located the thirteen marked signed cancellations and checked the input window. The finite proofs below use their own triangle, local-weight and moment definitions.
4. The labelled vacuum transfer passed. The initial full-file process crossed the 2 GiB guard, and the densest marked cap in its segmented repeat exceeded the per-declaration limit. The direct kernel orbit calculation with all cap intervals passed for the whole vacuum and for the first 146 marked rows, through face degree 32. The successful higher-degree construction reused verified directed slices and closed each shell against its own exact count. The receipt records failed attempts alongside successful runs.

## Finite definitions and bounds

Write $D$ for the face-degree cutoff and $r$ for the floor at the two rooted caps. The marked calculation uses $(D,r)=(46,2)$ and the vacuum uses $(28,0)$. In column $i$ let $m_{ij}$ be the four mixed spins. Horizontal cap $a_j$ couples $m_{i,j-1},m_{ij}$ and vertical cap $b_i$ couples $m_{i-1,j},m_{ij}$. Every index is cyclic. A permitted triangle satisfies $|x-y|\le c\le x+y$ and $x+y+c$ even. Also $a_0,b_0\ge r$. All labels are twice-spins. [Row 1425, four-dimensional contraction](gap-rg-ring-sign-astra62.md#four-dimensional-contraction-on-a-smaller-graph)

**Exhaustive bounds.** Put $A=\sum_j a_j$ and $L=\max(\max_j a_j,\lceil A/2\rceil)$. Every mixed column costs at least $L$. Each cap is bounded by the sum of two column entries and summing the four inequalities counts each column entry twice. The four parity constraints imply $A$ even. Thus $3A+r\le D$, and one column costs at most $D-A-r-3L$. The generator starts at its zeroth entry, takes all three successive Clebsch–Gordan intervals, and closes the remaining horizontal triangle. These choices specify that column uniquely.

Write $x,y,z,w$ for columns 0 through 3. With $a,x,z$ fixed, $y,b_1,b_2$ form one path and $w,b_3,b_0$ form the return path. For each pair of adjacent columns the vertical choices are the intersection of four triangle intervals of common parity, with the stipulated floor. Let $g=\max_j|x_j-z_j|$ and $p=(x_0+z_0)\bmod 2$. The sum of cap spins on each path is at least $g$, by the triangle inequality, and has parity $p$. The return path also costs at least $r+p$ in caps. These inequalities justify the endpoint filter in `usable`. Each intermediate path reserves the minimum possible cost of the other side. The final product tests the actual sum against $D$. Every surviving choice gives one labelled assignment and every labelled assignment has precisely these six path choices and fixed columns.

**Signed sums and zero rows.** A histogram key stores the seven multiplicities in base 25. A face list has length 24, so no digit carries. The half-path sums store their labelled counts, their signed integer sums and a flag for the existence of a nonzero summand. Joining two paths multiplies their counts and signed sums. A key enters the result when both sides contain a nonzero summand, even if their sums cancel. This is the convention used by the source tables. The fixed local denominator is $10080$. A four-vertex cut carries its fourth power and a complete configuration its sixteenth power. Every final target denominator must divide that number.

**Orbit multiplicities.** A reflection sends face index $i$ to $3-i$ and circuit index $i$ to $-i\pmod 4$. Transposition exchanges the two factors. For a mixed-array orbit $O$, each group element taking its representative to $m\in O$ gives a bijection on the cap choices preserving the histogram key. For the weight, multiplying the signed overlaps removes one square root per copy of each edge triangle. The factors in the two squared path normalizations consist of exactly the same 32 triangles and the same mixed dimensions. The sum of twice the local phase exponents is $4\sum a+12\sum b+2\sum m$. The resulting global phase is $(-1)^{\sum m}$. In `graph_incidence` the 24 face positions have distinct symbolic labels. The theorem checks the factor multisets, exponent coefficients and the corner permutations for the two reflections and the transpose. In `local_table_and_symmetries` the dephased coefficient is invariant under all three corner permutations throughout the checked spin window, including at the marked vertex. Consequently summing the cap fibre over $O$ multiplies its representative's fibre sum by $|O|$, including when the representative has a stabilizer. The vacuum has both a labelled transfer and an explicit mixed-array orbit calculation. The marked shell calculation below uses mixed-array orbit multiplicities directly. The four leading orbit sizes and their weighted sum are also checked in `leading_orbits` and `leading_orbit_histogram`.

## Orbit census and independent cardinality

The vacuum has two checks. The first fixes a horizontal cap vector and contracts the two paths between opposite columns. The second takes the least packed mixed array in each rooted orbit, generates all eight cap intervals, takes every allowed cap tuple under the degree bound, and weights it by the number of distinct images of the mixed array. The same direct orbit calculation through marked face degree 32 exercises the first signed cancellation.

All 56,991 distinct directed slices used in the marked census have kernel-checked local factors. For the higher marked shells, a proposed record consists of a canonical mixed array, an ordered pair of four-cap vectors, and four indices into a table of directed slices. `verifyArc` reconstructs all four signed local factors from the checked Racah table. It verifies all four triangle and parity constraints at each vertex, the local spin bounds, the marked floors, the contributed degree and histogram key. The cap dimension product occurs once on the rooted slice. `recordedTerm` requires each retrieved signature to match its actual two mixed columns, cap vector, vertical spin and traversal position. It checks the exact face degree. The computation therefore tests individual zero-weight assignments as well as the contributions that enter a histogram.

The proposed arrays are strictly ordered within and between pages. Their cap tuples are strictly ordered for each array. Each accepted contribution uses the cardinality of the distinct rooted images of its mixed array. The permutations act on four-bit spin positions. `mixed_digit_actions` checks every nibble value in each position against the geometric reflections and transpose. `rooted_orbit_multiplicities` checks the eight permutations on all 24 face positions, their composition table, the rooted caps and the coset partition for every possible stabilizer. To count a fibre, take one transformation sending its representative to each image. This transformation maps the cap labels bijectively, even when the representative has a stabilizer. Distinct listed cap tuples thus generate disjoint sets of labelled assignments. The phase, triangle and local-symbol identities in `graph_incidence` and `local_table_and_symmetries` preserve their signed contributions.

A second enumeration covers all 811 admissible horizontal cap vectors. It fixes the horizontal caps $a$, their opposite mixed columns $x,z$, and generates allowed cut intervals directly from the triangle inequalities. Put $B=2^{144}$ and $E_{xy}=\sum_{b\in I(x,y)}B^b$. The positive transfer for one middle column is $F_{xz}=\sum_y B^{|y|} E_{xy} E_{zy}$. In the return transfer $R_{xz}$ the edge at $x$ has the marked floor. Summing $B^{|a|+|x|+|z|}F_{xz}R_{xz}$ through face degree 46 gives the counts by degree. At every block the computed product evaluated at one is bounded above, and the sum of these upper bounds is checked to be smaller than $B-1$. Each occupied base-$B$ digit therefore equals the number of assignments at its degree. The construction reserves the same lower bounds on the two unfinished columns as the signed transfer. This proof has no recoupling weights, orbit catalogue or signed target values.

For each checked marked shell, the size of the admitted disjoint union equals that independent digit. An omitted admissible labelled assignment would make its size smaller. The integer histogram from the covered union is compared field by field with the literal table. A row survives whenever an individual contribution at its key is nonzero, including when their signed sum vanishes. The reference comparison also checks positivity and divisibility of every denominator. The ordinary census and the alternative marked degree-32 calculation use separate mixed-array and cap enumerations.


The Lean statements are closed checks for this graph and these cutoffs. The inequalities above identify the bounded column generator with the unrestricted triangle formulation. The finite cardinality argument identifies an equal-sized disjoint family of admissible labelled assignments with the whole set. Those two general statements are supplied here as mathematical arguments.


The target literals are ordered by the base-25 key within each marked face degree. An independent decoder compared all seven multiplicities, signed numerator and positive denominator with the pinned `Ring.lean`, checking uniqueness as well as equality of the row multisets. The kernel compares its computed scores with these target literals. [Row 1432 source](../lean/ring/Ring.lean)


For the two largest shells, `OrderedPages` certifies the first and last mixed identifiers of each subtotal. A leaf checks its own pages and each binary join checks the strict inequality across the adjoining boundary. The signed sums use the same page lists.

## Signed recoupling

For the left path take $(a,t;r),(b,r;s)$ and for the right take $(b,t;u),(a,u;s)$. If $D_r,E_u$ are their squared products of triangle factors including dimensions, the overlap is $F_{ru}\sqrt{D_r E_u}$. The code evaluates the alternating Racah factorial sum with the phase $(-1)^{(a+2t+3b+r-u)/2}$. With $C_j=j(j+2)/4$, the mixed matrix of $X=J_a\cdot J_b$ is $(C_s+C_t-C_r-C_u)O_{ru}/2$. Inserting both resolutions of the identity in $X^2$ gives `Vertex.mark` for $K=X^2+X/2-C_aC_b/3$. The second calculation expands $(x_1y_2-y_1x_2)^{(a+b-c)/2}$ times its highest-weight monomial and distributes the lowering operators. It computes $4X$ by its three magnetic-index shifts and $48K=3(4X)^2+6(4X)-a(a+2)b(b+2)$. Comparing signs and squared magnitudes with positive norms also tests zero overlaps. The factorial and polynomial constructions follow the conventions of the row-1425 producers `recouple.py` and `magnetic_check.py`. The latter's values were never read into either side of a Lean equality.

For clarity, the factorial sum evaluated by the kernel uses
\[
x=\tfrac12(a+t+r,b+s+r,b+t+u,a+s+u),\qquad
y=\tfrac12(a+t+b+s,a+r+b+u,t+r+s+u).
\]
With $p=(a+2t+3b+r-u)/2$ its signed rational part is
\[
F_{ru}=(-1)^p\sum_{z=\max x}^{\min y}
 \frac{(-1)^z(z+1)!}{\prod_i(z-x_i)!\prod_j(y_j-z)!}.
\]
The four triangle tests select integral factorial arguments. For a triangle with semiperimeter $h$, its squared factor is $(h-a)!(h-b)!(h-c)!/(h+1)!$. Signs and squared magnitudes are compared separately in the magnetic-index calculation.


The checked domain has $a,b\le6$, $t,s,r,u\le7$ and $a+b+t+s+r+u\le22$. Both path orders are constructed anew for every admissible entry. The 1,689 distinct flagged tuples from the row-1425 input lists lie inside this domain (1,394 ordinary and 295 marked). In the final census each locally used tuple also satisfies the window check.

## Sphere-coordinate calculation

For one bond and coordinate exponents $2k_0,\ldots,2k_3$, write $h=\sum k_i$. The monomial value is $\prod_i(2k_i-1)!!/[2^h(h+1)!]$. An odd exponent gives zero. Choosing the first occurrence of a coordinate gives coefficient $(e_i-1)/(n+2)$ for its remaining equal partners at total degree $n$. This also gives the sphere relation used in word cancellation, since the four ratios $(2k_i+1)/(2h+4)$ sum to one. In `quaternion_trace_pairing` the second-order contractions are verified on $1,i,j,k$, independently for the two traversal signs. Bilinearity in the two intervening quaternion words gives the gluing identities. A pair in different normalized traces contributes one joined trace in units of $1/4$. In the same trace, equal signs contribute $-2$ times the joined trace and opposite signs give $4$ times the split product in the same units. The factor $4/(n+2)$ converts this pair average to the sphere recursion. Every child loses two letters before free and cyclic reduction. At the root the five terms have integer weights $3,1,-4,-4,4$ on denominator $6\prod_f n_f!$. This calculation uses the row-1424 sphere formula and the trace expansion of row 1425. [Row 1424](gap-rg-two-cycle-astra62.md) · [Row 1425, leading coefficient and independent contraction](gap-rg-ring-sign-astra62.md#how-to-reproduce-the-finite-sums)

The unit-norm relation for every monomial on which a cancellation can act is checked in `sphere_word_identities`. The same theorem checks the quaternion basis identities for conjugation, cyclicity, associativity and cancellation of mixed norm terms. The trace recursion on the 55 products produces the following values.

All eleven configurations come from `leadingSupports`. In the table each value includes its Taylor factorials.

| Representative in Lean | Labelled supports | Contribution per support |
|---|---:|---:|
| `mixedRep` | 4 | $-5/195689447424$ |
| `evenRep` | 4 | $5/1320903770112$ |
| `oddRep` | 2 | $5/86973087744$ |
| `torusRep` | 1 | $5/77309411328$ |

Each four-character string below lists the four twice-spins in increasing index order. The four mixed columns appear in the order $m_0,m_1,m_2,m_3$.

| Support | $a$ | $b$ | Mixed columns | Orbit |
|---:|---|---|---|---|
| 0 | `2000` | `2000` | `1111 1111 1111 1111` | `torusRep` |
| 1 | `2002` | `2002` | `0002 0002 0002 2220` | `evenRep` |
| 2 | `2002` | `2101` | `1111 0002 0002 1111` | `mixedRep` |
| 3 | `2002` | `2200` | `2220 0002 0002 0002` | `evenRep` |
| 4 | `2101` | `2002` | `1001 1001 1001 1221` | `mixedRep` |
| 5 | `2101` | `2101` | `0112 1001 1001 2110` | `oddRep` |
| 6 | `2101` | `2101` | `2110 1001 1001 0112` | `oddRep` |
| 7 | `2101` | `2200` | `1221 1001 1001 1001` | `mixedRep` |
| 8 | `2200` | `2002` | `2000 2000 2000 0222` | `evenRep` |
| 9 | `2200` | `2101` | `1111 2000 2000 1111` | `mixedRep` |
| 10 | `2200` | `2200` | `0222 2000 2000 2000` | `evenRep` |

## Negative fixtures and trusted base

Setting the phase-flipped spin-half overlap with $(r,u)=(0,2)$ to pass was rejected. Removing `oddRep` and asserting full coverage was also rejected. Lean identified both propositions as false in isolated error runs. The delivered file contains positive rejection theorems and guarded copies of both failing fixtures.

The source imports `Init` and uses Lean 4.36.0. Arithmetic leaves reduce by `decide` or definitional equality. Every recorded module was compiled with one worker. The recoupling theorem reports no axioms. The named sphere fixture reports `propext`. Its auxiliary word identities and the complete census report `propext`, `Classical.choice` and `Quot.sound`. Untrusted generators supply only proposed words, indices, intermediate integers and targets. The required initial version command has no isolated resource measurement. One guard-terminated preliminary run has an estimated wall time and a sampled lower bound on peak memory. The exact source reconstruction, input fingerprints, measurements and verbatim axiom output are in the [receipt](../lean/haar/RECEIPT.md).

## Integral identifications still open

| Finite statement | Identification required for the row-1425 integral |
|---|---|
| Spin census | Expand the product of 24 Wilson factors on the open four-cube, identify the two positive rooted circuits on $C_4\times C_4$, and justify coefficient extraction. The labels in Lean are natural numbers on this graph. The integral argument must identify the nonnegative twice-spin labels, the two marked degree shifts, and the Schur link projectors with those choices. |
| Recoupling | Identify the stated polynomial paths with the normalized SU(2) intertwiners for probability Haar, including inverse traversal, complex conjugation and dimension factors. Derive the twice-differentiated trace-free character insertion and its prefactor $16/\beta^4$. |
| Sphere fixture | Identify $SU(2)$ with the unit quaternions as a measured group, normalized link Haar with independent uniform $S^3$ variables, and identify $T$ with the five-term rooted trace polynomial. Prove the sphere-coordinate integral, for example by separating a radial four-dimensional Gaussian. For the Taylor coefficient, also show by the link selection rules that every degree-16 term outside the eleven triangle-admissible supports vanishes. The finite theorem evaluates the resulting moment functional on those supports. |

## Analytic plan

1. **`wilson_bessel_coefficients`.** Apply Weyl integration and Schur orthogonality to $e^{\beta q(g)}/A(\beta)$. Match the index $n=2j$, the factor $n+1$ and the positive series $L_n/L_0$. Prove its differentiated series, termwise majorants and remainder over $[2,513/256]$. The starting GL3–GL4 argument is in outline 2195–2243. A Lean formalization needs real integration, infinite series and differentiation under a dominated limit. Mathlib would supply the analytic infrastructure. The SU(2) normalization and the specific estimates still need proofs.
2. **`temporal_circle_and_even_remainder`.** Prove the temporal-gauge change of variables and the three-cube convolution on probability Haar. Derive the two Hilbert-space norm bounds with the high-spin convolution correction. Show that the temporal generating functions are entire and even, then apply Cauchy's estimate at radii $11/4$ and $9/4$ with first omitted powers 48 and 30. This calls for Haar products, $L^2$ estimates, complex power series and Cauchy's integral formula from mathlib or a replacement library.
3. **`conditional_quadrupole_bounds`.** Derive the four-link conditional law, the boundary integrands and derivative tails for $Z,W_1,D$. Justify both minimum-principle steps on the two staple balls and integration against the same positive exterior law. This needs measure theory, differentiation of parameter integrals and the precise maximum or minimum principle for the differential operator in use.
4. **`ring_routings_common_vacuum`.** Identify the numerator with $z_{B_4}\mathbb E_4T$ and the ordinary denominator with $z_{B_4}$. Prove positivity, identify both routings of row 1424 (7), and handle the fixed-charge scalar and inadmissible cases. Compose with the two tail bounds and the conditional estimates. Normalized integration uses real measure theory. The finite trace and fixed-charge algebra can be developed in core. The $1-1$ computation from row 1432 does not establish the group identity.

Mathlib is absent from this checkout. These are proposed uses of its measure and analysis libraries. This research grants no audit or scientific status.

## Next two proposed rows

1. **Identify the finite calculation with the oriented Haar coefficient.** Prove the Wilson–Bessel coefficient formula with its normalization, the oriented link projector and both marked derivatives. Identify the unit-quaternion moment functional and rooted trace polynomial with the same product-Haar integral. The decisive outcome is a coefficient identity with the exact shifts, signs and $16/\beta^4$, including the degree-16 value.
2. **Close the analytic estimate and match the routings.** Prove the temporal convolution and Cauchy tails, the conditional quadrupole estimates, and the common positive vacuum for both routings. The decisive outcome is the stated signed four-dimensional estimate on the full coupling interval with every omitted order controlled. A failed bound identifies the precise term still open.
