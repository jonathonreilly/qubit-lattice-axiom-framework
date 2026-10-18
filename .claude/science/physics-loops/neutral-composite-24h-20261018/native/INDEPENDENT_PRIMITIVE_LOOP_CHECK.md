# Independent primitive rectangle coefficient derivation

Disposition: PASS. The candidate law follows exactly from the distinct-edge imaginary-time cumulant. A Gaussian or free-fermion assumption is unnecessary: each independent physical spin is inserted exactly twice in this particular monomial.

## Precise coefficient being computed

Fix a simple, nonwrapping transverse rectangle with N=2(a+b) distinct boundary edges in a single longitudinal layer. Give each edge an independent coupling g_e and retain only the squarefree monomial product_e g_e. In the aligned-column sector, flipping a spin in this layer costs d=4J_z. Restricted to this monomial, the unperturbed intermediate energy is exactly d times the number of flipped spins. Thus the auxiliary independent-spin H0=-(d/2) sum_v Z_v computes precisely these native denominators. It is a calculation of a coefficient, not an assumption that the full interacting native model is Gaussian.

Every proper nonempty subset of the cycle edges has a vertex of odd degree. Its vacuum time-ordered expectation vanishes because that vertex receives one X or Y insertion. Consequently all proper-partition terms in the connected cumulant vanish. The complete squarefree cycle coefficient in log Z equals its ordinary time-ordered expectation. This also explains why there are no folded vacuum-return terms for this primitive cycle.

## Local correlators and the loop integral

For the reference up spin, let tau be the time of the first listed operator minus the time of the second. With Fourier transform integral exp(i omega tau),

    G_XX(omega)=G_YY(omega)=2d/(d^2+omega^2),
    G_XY(omega)=-2omega/(d^2+omega^2),
    G_YX(omega)=+2omega/(d^2+omega^2).

For example G_XY(tau)=i sign(tau) exp(-d|tau|). A reversed reference spin changes the mixed correlators' sign, not the same-axis ones.

There are N-4 straight vertices and four corners. Around a rectangle the corners comprise two XY and two YX vertices. Their product therefore has positive sign, with numerator (2omega)^4. The time integrals enforce one common loop frequency; translation of all times gives the total imaginary-time interval, which is divided out in the ground-energy limit. The energy is minus the logarithm per unit time. Hence the exact coefficient is

    c_N(d) = - integral_R [domega/(2pi)]
                (2d)^(N-4) (2omega)^4 / (d^2+omega^2)^N
             = - [2^(N-1)/pi] d^(1-N) B(5/2,N-5/2).

There is no additional orientation factor of two. Each edge has an independent label: in the exponential expansion, differentiation once in each coupling cancels the 1/N! against the assignments of those labels. The single real-frequency integral already includes both frequency signs. Counting two directed traversals in addition would double the N=4 answer incorrectly.

For a background column pattern s_v, the four corner mixed correlators contribute product_corner s_v. Straight vertices contribute no background sign. The resulting native operator is the product of Z column labels at the four corners.

## Closed law and recurrence

Set d=4J_z and g_e=J_z lambda for the isotropic transverse coupling. The energy contribution is J_z lambda^N c_N times the corner product, with dimensionless

    c_N = -3 Gamma(N-5/2) / [2^(N+1) sqrt(pi) Gamma(N)].

This is exactly the proposed formula, derived without fitting. Its exact recurrence is

    c_(N+2)/c_N = (N-5/2)(N-3/2) / [4N(N+1)].

It starts at c_4=-1/128 and yields

    c_6=-3/8192,
    c_8=-9/262144,
    c_10=-143/33554432,
    c_12=-663/1073741824,
    c_14=-6783/68719476736.

The aspect ratio drops out because the frequency product depends only on the number of straight vertices and four corners, not their spacing around the cycle. This holds also for a one-cell-wide simple rectangle: its boundary vertices remain distinct. The argument fails for self-intersecting walks, repeated edges, or periodic aliases unless their vertex insertion multiplicities are treated anew.

## Scope and checks against overinterpretation

This proves the primitive, single-layer, squarefree rectangle monomial. It does not prove that the complete order-N coefficient of the same corner operator equals this number: shorter cycles dressed by repeated edges, folds from other words, and other native processes can renormalize that operator at higher orders. Nor does it prove convergence of the whole native expansion, a long-range force, a selected state, or a collective pole.

The stated N<2L and nonwrapping native geometry are safe restrictions for integration with the existing column normal form. The integral itself proves the isolated cycle coefficient whenever the single-layer intermediate states have the independent flip costs and no proper projected return; it should not be used to bypass separate classification of other words at that order. For nonuniform longitudinal flip gaps the vertex propagators have different d_v and the simple aspect-independent Gamma expression no longer follows.

## Addendum: arbitrary simple orthogonal cycle with m turns

PASS. For a simple planar orthogonal cycle, write its cyclic sequence of edge axes as X or Y. A turn is a change of axis. The number m of changes is even, and exactly m/2 are XY changes and m/2 are YX changes. This counts axis changes, not signed left/right geometric turns; concavity causes no extra sign. At straight vertices the reference-spin sign drops out; at each turned vertex the mixed correlator supplies its local background s_v. Thus the operator is exactly product_(turn vertices) s_v (the corresponding column-Z product).

The frequency product has sign (-1)^(m/2) and numerator (2d)^(N-m)(2omega)^m. Including the ground-energy minus sign gives

    c_(N,m)(d) = (-1)^(m/2+1) [2^(N-1)/pi] d^(1-N)
                 B((m+1)/2, N-(m+1)/2).

At d=4J, extracting J^(1-N), the dimensionless coefficient is

    c_(N,m) = (-1)^(m/2+1) 2^(1-N)/pi
              * Gamma((m+1)/2) Gamma(N-(m+1)/2) / Gamma(N).

Both Gamma arguments are positive for a nondegenerate simple lattice cycle (m<=N, N>=4), so the displayed parity supplies its entire sign. In particular four-turn loops are negative, six-turn loops positive, and eight-turn loops negative. Therefore the primitive family is not uniformly attractive. For a nontrivial background, the corner-Z eigenvalue can additionally change the sign of its energy contribution.

The same no-proper-subset argument proves that the squarefree connected cumulant equals the full moment; no Wick/Gaussian assumption is used and no folded term with a proper projected return occurs inside this specific monomial. The expression does not cover repeated-edge walks, self-intersections, multiple loops, periodic identifications, or other words contributing to the same operator. A momentum-marked insertion would require distributing numerator and denominator marks over the actual geometry; N and m alone do not determine that Fourier kernel. Likewise this primitive coefficient alone is not the full canonical coefficient at its order.
