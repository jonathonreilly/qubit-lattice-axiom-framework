# Blind PRE: number-sector filling at the spectral bottom of the supplied common Hamiltonian

This is an independent bounded reconstruction from the two expressly permitted notes. No author candidate, other active checker packet, campaign checkpoint, or parent scientific runner was read. No claim is made about physical vacuum selection, formation dynamics approaching a ground state, a thermodynamic phase, or observed masses. The source parents are conditional supplied-model results, not consequences of minimal axioms re-established here.

The supported conclusion is stronger than exclusion of full filling but weaker than identification of an exact minimizer. On each fixed simple degree-six rectangular cubic torus with even side lengths at least four, every number sector attaining the global spectral infimum has a finite, non-full fraction of B sites occupied when K/delta is sufficiently small. One explicit eventual interval is

    23/148 <= m/|B| <= 209/336.                         (A)

The endpoints are sufficient bounds, approximately 0.1554 and 0.6220; they are not a predicted filling fraction or optimal bounds. The threshold depends on the graph. Full B occupancy is excluded at every K,delta>0. No normalizable vector at the global infimum, unique minimizing sector, or limiting phase is established.

## 1. Sources, target, and exact model

The only scientific parents are the files at main `60c5f194d940a7bbaf1cdd545296e31d74a02f1a`:

- `LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md`, SHA256 `7c5bc10d0ca1127c2a1ef6f5cf9269caf6e8f023a09a061c2da0d8e033e35a7a`.
- `LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md`, SHA256 `c63db3296e5705c57693c2deb109e506f336fae4848d3ab0926d13a98929802b`.

Their current bytes were compared with those exact Git objects and copied into `sources/`. Both complete arguments were read. Their canonical local-pair identity, supplied tensor-product hard-core record algebra, unit rotor shifts, physical Gauss constraint, common Hilbert space, and self-adjoint domain are imported with their stated hypotheses. No transitive numerical result is imported or re-certified.

Let G be the simple nearest-neighbour torus with side lengths L1,L2,L3, each even and at least four. Put M=|A|=|B|=L1 L2 L3/2 and orient each edge from A to B. There are 6M edges. On P every A site is occupied, each site has q=0,+1,-1, and

    div E = q-1_A,       E in Z^(6M).

The Hamiltonian under examination is exactly

    h = K D - delta Q,
    Q = -H4_infinity^C = 2 sum_{a<c, N(a) intersect N(c) nonempty} S_ac* S_ac,
    S_ac = F_c F_a P,
    D(q,E) = sum_{a~b, q_b=0} E_ab(E_ab-q_a).          (1)

Here F is the original unsigned outward charge-preserving hop, with hard-core exclusion, and K,delta>0. D is the actual gated nonnegative integer multiplication operator. It is not replaced by sum E^2 after B occupation. Q is bounded and nonnegative on each fixed graph; h is self-adjoint on D(D).

Let m be the number of occupied B sites. The number sector is N=M+m. Summing Gauss on the torus gives sum q=M, so exactly m/2 of the N occupied sites have negative charge. Thus the nonempty physical number sectors are m=0,2,...,M. Each is nonempty: any such charge word has zero-sum integer Gauss demand and an integer flow solution on a spanning tree. Hamiltonian hops preserve the two color counts and total number; on P they therefore preserve m. Write

    eta=K/delta,   E_m(eta)=inf spec((eta D-Q)|_m),
    E_*(eta)=min_{m even} E_m(eta).                    (2)

This finite minimum exists as a minimum over sector infima; it need not be an eigenvalue. Statements about a sector attaining E_* are statements about this finite minimum. Calling m/2 a number of formed pairs is only number accounting here, not a proof that each state is reachable from a chosen formation history.

The two parents do not themselves define g. A narrow definition-only clarification supplied by the root after dispatch, preserved verbatim in `SUPPLIED_PARAMETERIZATION.md`, is K=g^2/(2 tau), delta=1/(4 tau g^2), tau>0 fixed. Hence eta=2g^4. All proofs below are in eta; that supplied reparameterization yields the g statement without additional physical units or identifications.

## 2. Full filling, small tori, and the empty-sector baseline

For m=M there is no empty B site, hence D=0 and every F_a P=0. Therefore

    h|_(m=M)=0                                             (3)

on the entire physical full-occupancy sector, for every color word and electric field. In contrast, q=1_A with E=0 is a normalizable physical basis vector with D=0 and nonzero S_ac. Its energy is strictly negative for delta>0. Consequently full occupancy never attains the global spectral infimum for any positive K,delta. This argument does not use a weak-coupling limit.

The short even torus requires care. Let s be the number of side lengths equal to four. For each A site there are n1=6-2s A partners with one common B neighbour and n2=12+s with two common neighbours. There are no other overlap types. Length-four axial partners contribute two common neighbours and include the corresponding winding four-cycles. For equal side length L, s=3 when L=4 and s=0 when L>=6. A length-two simple torus has degree three and is outside the degree-six premise; a parallel-edge substitute is outside the simple-graph parents.

For r=1,2 the two-hop diagonal path count is 36-r. Thus the E=0 empty-B trial used above has

    <Q> = M(618-36s) > 0.                              (4)

At zero link angles the corresponding empty-sector magnetic row sum includes the exchange paths and is

    Q0=M(642-34s).                                    (5)

This distinction matters: Q0 is the empty-sector magnetic spectral supremum, not the expectation of Q in the zero-electric basis vector. Section 5 justifies the zero-angle supremum without treating a delta function in angles as a physical state.

## 3. Exact local row bounds, uniform in colors, Gauss flows, and winding

Consider one overlapping A pair. Let u_a,u_c be its numbers of occupied B neighbours, w its number of occupied common neighbours, and r its total number of common neighbours. Set h_a=6-u_a, h_c=6-u_c, t=r-w. The possible triples are

    w=0,...,r;  u_a=w,...,w+6-r;  u_c=w,...,w+6-r.     (6)

In the physical charge/electric basis all matrix coefficients of Q are nonnegative: the F's are unsigned unit rotor shifts with the tensor-product record algebra. For a fixed input basis word, the column sum of S_ac* S_ac is exactly the number of outward two-hop paths followed by legal return paths. There are h_a h_c-t outward choices. After an outward choice (b,d), the occupied-neighbour numbers are u_a+1+1_(d common) and u_c+1+1_(b common); the occupied common count is w+1_(b common)+1_(d common). Subtracting equal return destinations gives

    R_r(u_a,u_c,w)
      =(h_a h_c-t)[(u_a+1)(u_c+1)-w]
        +u_a t(h_c-1)+u_c t(h_a-1)+t(t-1).             (7)

Every counted return is legal regardless of the charges carried by its occupied B sites. Charge signs determine the output colors and electric shifts, not the unit path weight or number of choices. Different paths may produce the same basis word; their positive multiplicities add. Hence this counts the row/column sum, not just distinct outputs. All shifts preserve Gauss. No electric cutoff or winding restriction is used.

The following finite integer inequalities hold on every triple (6):

| r | a_r=R_r(0,0,0) | c_r | d_r | inequalities |
|---|---:|---:|---:|---|
| 1 | 35 | 69/2 | 24 | R_r<=a_r+c_r(u_a+u_c), R_r<=d_r(h_a+h_c) |
| 2 | 36 | 37 | 23 | the same two inequalities |

These are supported by an exhaustive exact certificate, not floating fits. The independently written control enumerates all 2048 and 1024 local occupation masks, directly executes all hop/return choices, and checks (7). The 72 and 75 symmetry-group rows retain exact nonnegative slacks for both bounds in `LOCAL_CERTIFICATE_REVIEW.tsv` and the full JSON. The slopes are the exact maxima over this finite domain. The first bound is saturated at (u_a,u_c,w)=(1,1,0) for both r. The second is saturated at (4,4,1) for r=1 and at (3,3,0) or (4,4,2) for r=2. An intentionally omitted common-neighbour/exchange contribution is rejected, so the check is discriminating.

Summing these inequalities over A pairs and using sum_a u_a=6m and sum_a h_a=6(M-m) gives the all-sector row bounds

    ||Q|_m|| <= Q0 + C_m m,     C_m=7812-384s,
    ||Q|_m|| <= C_h (M-m),      C_h=5040-300s.          (8)

For example, C_m=12[n1*(69/2)+n2*37]. To pass from row sums to operator bounds, for finite-support psi use symmetry and positivity of the matrix entries together with 2|psi_x psi_y|<=|psi_x|^2+|psi_y|^2; the row bound then bounds <psi,Q psi>. Density extends the inequality. This argument is uniform over every physical color and electric word in the m sector, including all winding coordinates. D>=0 therefore implies

    E_m(eta) >= -min(Q0+C_m m, C_h(M-m)).              (9)

The local constants are sharp for those two elementary row inequalities. No optimality of the resulting global filling bounds is claimed.

## 4. A fixed-number magnetic trial and its exact gain

At zero link angles take the normalized uniform positive matter vector over all words with m occupied B sites and exactly m/2 negative colors among the M+m occupied sites. Its dimension is binom(M,m) binom(M+m,m/2). This is a finite matter vector, not yet a physical rotor trial; Section 5 supplies the physical embedding.

For one A pair, the squared-path union counts for two ordered outward paths are

    (A_2,A_3,A_4)=(35,390,800) for r=1,
    (A_2,A_3,A_4)=(36,416,704) for r=2.                (10)

Indeed A_2=36+r^2-2r. The sum of squared incidence degrees of the path multigraph is 432+28r, so A_3=432+28r-2A_2, and A_4=(36-r)^2-A_2-A_3. Direct ordered-path enumeration independently checks these integers.

Writing (n)_j for a falling factorial, the pair Rayleigh value is

    t_r(M,m)=sum_(ell=2)^4 A_ell
                   (m)_(ell-2) (M-m)_2 / (M)_ell.    (11)

One derivation counts output B sets of size m+2. Each such output gets one amplitude for each valid ordered assignment into its two newly vacated A sites; squaring those amplitudes gives (10) and the binomial ratio in (11). Color assignments cancel because every output has the same total occupied number M+m and negative count m/2. Equivalently, averaging the exact input row count (7) over uniform size-m B subsets gives (11). The control checks these two different count organizations by exact rational arithmetic for 48 (M,m,r) cases.

Since M is divisible by four, m=M/2 is a legal even sector. At this filling the three factors in (11) are

    (M-2)/(4(M-1)),   M/(8(M-1)),
    M(M-2)/(16(M-1)(M-3)).                            (12)

They imply strictly

    t_1(M,M/2)>215/2,    t_2(M,M/2)>105.              (13)

For clarity, combining the first two deviations from their limiting values gives (A_3-2A_2)/(8(M-1))>0; the third deviation is also positive. Therefore the full trial value

    T=M[n1*t_1(M,M/2)+n2*t_2(M,M/2)]
      > M(1905-110s),
    T-Q0 > M(1263-76s)>0.                            (14)

This is an extensive magnetic improvement over the entire empty-B magnetic band bottom. It is not a claim that half filling is optimal: it is one trial sector.

## 5. Physical finite-support realization and the actual electric term

A zero-angle matter vector alone would not establish a variational bound on the physical Hamiltonian. Fix a spanning tree of G. For every allowed matter word q choose the unique tree-supported integer flow E^q with divergence q-1_A. Its edge values satisfy |E^q_e|<=M: total positive Gauss demand is the number of positive B charges and is at most M.

The integer divergence-free flow lattice has rank beta=|E|-|V|+1=4M+1. Its fundamental-cycle basis C_i may be chosen with entries in {-1,0,1} and identity coordinates on the non-tree edges. Every physical field has a unique representation

    E=E^q+sum_i z_i C_i,   z in Z^beta.               (15)

This includes the three torus winding directions. No harmonic direction is projected out and no zero-flux condition is added. The complete physical space is therefore the finite direct sum of copies of l2(Z^beta), indexed by allowed q. All constructions below are in that physical space.

For an integer R>=1 let f_R be the normalized indicator of the box [-R,R]^beta. Embed a normalized nonnegative matter vector v by

    Psi_R=sum_q v_q sum_z f_R(z)|q,E^q+sum_i z_i C_i>.(16)

It has finite electric support and belongs to the finite-support core of D. A monomial contributing to S_ac* S_ac has four charge-preserving hops. In coordinates (15), its cycle translation has l1 norm at most four: z is simply the electric value on each non-tree edge, and each hop changes one electric edge by one. Thus

    <f_R,T_t f_R>=product_i (1-|t_i|/(2R+1))_+
                     >=1-4/(2R+1).                  (17)

For the uniform trial in Section 4, positivity of all coefficients yields

    <Psi_R,Q Psi_R> >= T[1-4/(2R+1)].                 (18)

Every field in its support satisfies |E_e|<=M+beta R. Retaining the actual empty-B gate, and merely overestimating its nonnegative terms, gives

    <Psi_R,D Psi_R> <= B_G(R)
       :=6M[(M+beta R)^2+(M+beta R)].                 (19)

Consequently, for every eta>0 and R>=1,

    E_*(eta) <= -T + r_G(eta,R),
    r_G(eta,R)=4T/(2R+1)+eta B_G(R).                 (20)

Choosing R=ceil(eta^(-1/3)) for 0<eta<=1 gives r_G=O_G(eta^(1/3)) and tends to zero. This is a finite-support, normalizable, Gauss-compatible variational proof with the full original D. Its constants grow with the graph; no uniform thermodynamic estimate is implied.

A useful exact fixed-graph characterization follows by Fourier transforming (15). Q has a finite Hermitian matrix symbol Q_m(theta) with Laurent entries whose coefficients are nonnegative. Entrywise |Q_m(theta)|<=Q_m(0), so

    ||Q|_m||=lambda_m:=lambda_max(Q_m(0)).             (21)

The upper inequality follows by replacing a vector with its componentwise absolute value. For the reverse inequality use (16)--(18) with a normalized nonnegative maximizing eigenvector of the finite real matrix Q_m(0), which exists by the finite-dimensional variational principle and absolute-value inequality. The same electric bound then proves

    lim_(eta->0) E_m(eta)=-lambda_m.                  (22)

This is a reduction to a finite magnetic matrix, not its diagonalization here. Because there are finitely many m, sectors with lambda_m strictly below max_k lambda_k are excluded from the global spectral minimum for sufficiently small eta. Degenerate maxima can still be distinguished by the positive electric contribution. Neither (21) nor (22) supplies a normalizable ground vector at finite eta or an exact preferred m.

## 6. Filling bounds and the order of limits

Combining (9) and (20), every m attaining E_*(eta) obeys, for every R>=1,

    [T-Q0-r_G(eta,R)]/C_m <= m
                  <= M-[T-r_G(eta,R)]/C_h.           (23)

This is a finite-parameter sufficient bound. With R as above, its limiting lower and upper fractions are (T-Q0)/(C_m M) and 1-T/(C_h M), respectively. The exact rational values for five finite graphs appear in `CONTROL_RESULTS.json`; they are bounds on minimizing sectors, not computed minimizers.

Using (14), the coarser lower fraction is

    (1263-76s)/(7812-384s) >=23/148,

and the excluded hole fraction obeys

    (1905-110s)/(5040-300s) >=127/336.                (24)

The first ratio decreases with s=0,1,2,3 and the second increases. The finite-M strictness in (14) leaves a positive margin even in the extremal cases. Since r_G tends to zero, (A) therefore holds for every minimizing sector once eta<eta_0(G) for some positive graph-dependent threshold.

For example, the exact trial bounds eventually allow only even m from 6 through 18 on the 4x4x4 graph, 8 through 28 on 4x4x6, 12 through 44 on 4x6x6, 18 through 66 on 6x6x6, and 42 through 158 on 8x8x8. These lists only discard impossible minimizers; they do not identify which remaining sector wins.

The quantifier is: fix G, then take eta->0 (equivalently the supplied g->0), and compare all its finitely many number-sector infima. Along any later sequence of larger such tori, the eventual lower bound is extensive, m>=23M/148. A fixed bound on the number m/2 of pairs cannot describe these weak-coupling global minimizing sectors once M is sufficiently large. This does not interchange the weak-coupling and volume limits or provide a single g threshold valid for all volumes.

All colors and integer Gauss flows were included in the lower bounds. The upper trial legitimately superposes their allowed configurations and all cycle coordinates. This is a global spectral comparison on the specified physical Hilbert space, not a claim that an arbitrarily prescribed additional winding superselection restriction has the same trial or infimum. No such extra restriction is silently imposed or removed.

## 7. Exact evidence and preserved unsuccessful shortcuts

`ground_filling_control.py` is independently written standard-library code. It imports no parent or author implementation. The final source SHA256 is `1406d17665162aad66dcd35b0010626ec9b89db9ebdfc075afcdaa7702918d90`. It checks all 3072 local occupation masks, retaining 147 exact grouped rows; 48 independent rational Rayleigh comparisons; incidence and geometric constants for five tori; and ten actual physical charge/electric hop-and-return examples on 4x4x4 and 6x6x6 tori. The latter cover both overlap types, several number sectors, negative colors on A or B, integer Gauss flows, the full cycle basis, all three winding cycles, and cycle displacements of the actual four-hop paths.

The full-filling physical controls give D=0 while sum E^2 is respectively 278 and 1608. They decisively reject the proposed shortcut of using the empty-B electric Hamiltonian unchanged after filling. The initial zero-electric state and the zero-angle magnetic supremum are also distinguished by exact return multiplicities. Treating the zero-angle matrix vector as normalizable was not used; the finite-support construction in Section 5 is the required replacement.

The first control run succeeded. A second run added only the explicit cycle-displacement and three-winding checks needed for the quantitative physical trial; the first complete source, results, stdout, stderr and receipt are preserved in `control_attempt01/`, and the final set in `control_attempt02/`. Both exit zero with empty stderr. All earlier local, Rayleigh and geometry scientific data are exactly unchanged. No parent runner, large sparse diagonalization, electric cutoff extrapolation, author control or independent agent was used.

An initial batched source display was truncated by the tool-output budget. It was not counted as a completed read; the affected parent and workflow were reread completely in bounded outputs. This was a read-completeness issue, not a scientific failure. No scientific computational failure has been omitted or rewritten. `READ_AND_FAILURE_LOG.md` states the complete scope and recovery.

## 8. What is established and what remains open

The conclusions are conditional spectral statements about the supplied compensated common Hamiltonian (1). They show that full occupancy has zero energy, that the global bottom is negative, and that global minimizing number sectors have finite fractional filling in the stated fixed-graph weak-coupling regime. They do not show full filling, a specific filling fraction, translation-breaking order, a unique minimizer, ground-state attainment, spontaneous formation/decay, equilibration, a physical vacuum, thermodynamic uniformity, or a measured mass scale.

The common-model density-limit theorem in the parent is not a theorem about convergence of microscopic spectral infima. No such transfer is attempted. No chemical potential, number-sector offset, new axiom, field-only model, postbirth projection, or apparatus has been introduced. Exact control coverage is local/combinatorial and finite; it supports the inequalities used, not an empirical or phase identification. The root's unreleased candidate remains unread until this PRE is sealed.
