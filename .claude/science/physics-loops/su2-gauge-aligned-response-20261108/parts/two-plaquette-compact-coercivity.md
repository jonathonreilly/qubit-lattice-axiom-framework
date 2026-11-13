# Compact coercivity after deleting two adjacent plaquette boundaries

Pure-proof author draft, 2026-11-09; independent checking pending.
Assigned source: `551840d63d189573688c763445b2eff9f99559d1`.
This is a two-step compact energy theorem, with no probability-decay claim.

## 1. Statement and source contract

Fix odd L>=3, kappa>0, and a four-dimensional periodic fine lattice of
side N=L²m, m>=3. Use the nested lattices, actual 24L^4 paired-root-leg
paths at each step, and centered terminal-root fine forest of the supplier
`compact-energy-coercivity.md`. All intermediate links remain variables.
Internal spanning trees of the terminal cubes are arbitrary. Let J be the
seven independent positive terminal edges in the union of the boundaries
of two distinct elementary terminal plaquettes sharing exactly one edge.
Set O=E2\J, take zero sources and V_O=I, and define

    W_p=1-w(U0,p), gamma_0,e=|M0,e|-<U1,e,M0,e>,
    gamma_1,c=|M1,c|-<I,M1,c>,
    E_J=sum_p W_p+kappa sum_e gamma_0,e+kappa sum_(c in O) gamma_1,c.

For c in J, gamma_1,c is an auxiliary nonnegative function, not a factor
in E_J. Then there is a finite C(L,kappa), uniform in m, position,
orientation and the internal trees, such that

    sum_(e in E0\T) [1-w(a0,e)] + sum_(e in E1) [1-w(a1,e)]
        <= C(L,kappa) E_J.                                      (T)

The exact deleted-output law is rho_J from `partial-terminal-normalization.md`
(P1)-(P2): its density contains q(U0), every normalized level-zero kernel,
and every normalized terminal kernel in O. No surviving radial normalizer
is dropped. The theorem is a deterministic estimate of its leading energy.

Mathematical sources read (paths below are relative to this `parts` directory):

| File and coverage | SHA-256 |
|---|---|
| compact-energy-coercivity.md, full | 7e8e798759239aadfc8c137125bf23f6d1de2cac18b714ddca70ea294cbaa4aa |
| compact-forest-exchange.md, §§1–3 | b0d3a76a94a8cd43de186b1c93deb38327ea2b29aa2b1bbc16e1caa2e22ecef2 |
| partial-terminal-normalization.md, §1 | 722e622dd64763e7f85461ef037f78810ec1c96d5bb71ddc7d60647c858b9867 |
| released-terminal-gauge-directions.md, §4 | a8271fb33178da46f747075f8b98f266cb06833ae900b99ef0544f36adcb403b |

The closest supplied result is the all-terminal compact energy theorem;
its path-filling/centered-mismatch method credits the earlier repo
CUT_SECTOR_COERCIVITY_ASTRA work. Parent-reported first repo/literature pass
found no imported sparse-removal theorem. This proof uses no such theorem;
supplemental searches and any external consultation are not premises.

## 2. Positive local estimates, retaining every discrepancy

Use quaternion chord distance d(A,B)=|A-B|, so d(I,A)^2=2[1-w(A)].
For products of n unitary factors, telescoping gives

    d(product A_i,product B_i)^2 <= n sum_i d(A_i,B_i)^2.       (1)

For a mean M=average P, unitary V,T, and gamma=|M|-<V,M>,

    d(V,T)^2 <= 4 gamma+3 average d(P,T)^2.                    (2)

Indeed |V-M|²=(1-|M|)²+2gamma, Jensen bounds |M-T|² by the
average D, and (1-|M|)²<=1-|M|<=D/2; the squared triangle
inequality proves (2), including M=0.

For two paths with equal lifted endpoints in a finite rectangular lattice
box, choose a finite plaquette-move/backtrack witness between them. Such
a witness exists because the box's cubical 2-skeleton is simply connected.
If it has n plaquette moves p_j, put

    Phi(P,Q;W)=2n sum_(j=1)^n W_(p_j).                       (3)

Then d(U(P),U(Q))²<=Phi, by telescoping the plaquette changes; each
change is a conjugate/translate of a plaquette holonomy. Backtracks cost
zero. Use Phi=0 for the zero-move witness. Multiplicities are never erased.
All paths and witnesses below are lifted first and then periodically
projected. Their paired lifted endpoints agree; no winding loop is filled.

Let R0,e be the straight length-L fine path for intermediate edge e.
For each actual paired path P0,e,i fix a witness to R0,e in its bounded
box. Define the positive linear forms

    D_e=4 gamma_0,e+3 average_i Phi(P0,e,i,R0,e;W).

Equation (2) gives delta_e=d(U1,e,U0(R0,e))²<=D_e. For an
intermediate plaquette P, let Sq(P) be its L-by-L fine square and set

    A_P=4 sum_(e in boundary P) D_e+2L² sum_(p in Sq(P)) W_p. (4)

Replacing four intermediate factors by straight fine paths, followed by
the L²-plaquette square filling, gives W1,P<=A_P. Reversed edges use
the same D_e. This is an inequality, not an intermediate Wilson law.

For terminal edge c let R1,c be the straight length-L intermediate path,
and let T_c be the straight length-L² fine transporter. Fix witnesses
between every actual P1,c,i and R1,c in their intermediate boxes. Put

    F_c=average_i Phi(P1,c,i,R1,c;A),
    H_c=2 F_c+2L sum_(e in R1,c) D_e,
    B_c=8 gamma_1,c+6 F_c+2L sum_(e in R1,c) D_e.             (5)

Here Phi with A means the positive form (3) with W1,P replaced by A_P;
thus F_c,H_c involve only W and gamma_0. Equations (1)-(4) imply

    average_i d(U1(P1,c,i),T_c)² <= H_c,
    d(I,T_c)² <= B_c.                                      (6)

For the second inequality first apply (2) with output I and reference
U1(R1,c), giving 4gamma_1,c+3F_c; then replace the L intermediate
links, whose squared error is at most L sum D_e, and use the squared
triangle inequality. The first uses the same replacement and F_c.
Consequently (6) uses only actual energy summands whenever c is in O.

For a deleted c, the upper bound |M1,c|<=1 yields, solely as an
upper bound on the auxiliary gap,

    gamma_1,c <= 1-<I,M1,c>
       = (1/2) average_i d(I,U1(P1,c,i))²
       <= H_c+d(I,T_c)².                                  (7)

In particular every path discrepancy introduced in (7) is paid by (5).
There is no substitution of an uncentered gap in E_J.

## 3. Restoring the seven missing constraints

Each elementary plaquette uses two coordinate directions. Since the pair
shares an edge, the union uses at most three. Choose a coordinate rho
unused by both. Every vertex and edge of J lies in one rho-coordinate
slice, say x_rho=b, and no edge of J has direction rho. For each positive
edge c=(x,x+e_mu) in J, in terminal lattice units use the oriented detour

    D(c): x -> x+e_rho -> x+e_rho+e_mu -> x+e_mu.           (8)

The two rho edges are outside J; the mu edge is in slice b+1, hence
outside J for m>=3. The last edge is traversed backwards. The detour
therefore has exactly three retained independent terminal edges. Denote
its fine straight-segment product by S_c. On the infinite fine lattice,
S_c and T_c bound the L²-by-L² rectangle in directions (rho,mu).
The standard square peeling has L^4 moves, giving

    d(T_c,S_c)² <= 2L^4 sum_(p in Rect(c)) W_p,
    d(I,T_c)² <= 4L^4 sum_(p in Rect(c)) W_p
                      +6 sum_(d in D(c)) B_d.             (9)

The second line uses the squared triangle inequality and (1) for three
segments; d(I,T_d^(-1))=d(I,T_d). Define the positive recovery form

    R_c=H_c+4L^4 sum_(p in Rect(c)) W_p
                    +6 sum_(d in D(c)) B_d.               (10)

It contains W, gamma_0 and only retained gamma_1. Equations (7)-(9)
prove gamma_1,c<=R_c for each of the seven missing edges.

This construction covers hinged plaquettes using three directions as well
as coplanar pairs. For seam edges choose the adjacent lifted endpoints;
the rectangle's two compared paths have precisely those same endpoints.
For m=3, slice b+1 remains different from b and a length-one terminal
segment still has its specified adjacent lift. Neither noncontractible
holonomy nor a choice of global periodic gauge is discarded.

## 4. Finite constants, congestion and the forest sum

Here is an explicit finite definition, without optimized numeric constants.
For each pair of different directions (mu,rho), anchor c at the origin
of the infinite terminal lattice. Choose the finite witnesses in §§2–3
once, translate them elsewhere, and expand (10) completely. Let Q(L)
be the maximum, over this finite direction list, of the sum of every
coefficient in that expansion, including repeated inputs. Replace it by
max(1,Q(L)). The actual 24L^4 paths give finite averages; their lengths,
boxes and fillings depend only on L. Thus Q(L)<infinity. The edge c's
membership in a particular pair of plaquettes does not change its recovery
form, except for which unused direction is chosen.

After periodic projection the sum of coefficients in each R_c is still
at most Q(L): coincident inputs add their coefficients. There are exactly
seven c's, so every input receives total coefficient at most 7Q(L),
even when some of the 21 detour-edge occurrences coincide. In particular,
with S_J=sum W+sum gamma_0+sum_O gamma_1,

    sum_(c in J) gamma_1,c <= sum_(c in J) R_c <= 7Q(L) S_J.
    E_all:=E_J+kappa sum_(c in J) gamma_1,c
      <= [1+7kappa Q(L) max(1,kappa^(-1))] E_J.             (11)

This bounds projected plaquette multiplicities as well as detour overlaps;
it does not assume disjoint rectangles or a volume-dependent incidence cap.

Let K(L)>=1 be exactly the finite coefficient-mass constant defined in
§6 of `compact-energy-coercivity.md`: list all fine/intermediate output
links with tail in one centered terminal block, all allowed internal trees
in endpoint blocks, and the filling templates in its (5)-(10). Expand
into W,gamma_0,gamma_1, take coefficientwise maxima over trees, sum the
coefficients, with the factor 1/2 converting squared distance to 1-w.
This is finite since a terminal block has L^8 vertices and finitely many
spanning trees; every simple tree path has length at most L^8-1.
For a fixed input and a fixed template offset there is at most one output
root translate modulo the torus. Hence the incoming coefficient is at
most K(L), including projected offset coincidences. The supplier's
forest-link comparisons therefore give, for auxiliary terminal output I
on all edges,

    sum_retained [1-w(a_e)] <= K(L) max(1,kappa^(-1)) E_all.

Here “retained” means all non-tree fine links and all intermediate links,
not terminal links. Combining with (11) proves (T) with the finite choice

    C(L,kappa)=K(L) max(1,kappa^(-1))
                    [1+7kappa Q(L) max(1,kappa^(-1))].     (12)

The auxiliary E_all is only a deterministic function used for comparison;
no all-terminal probability law is substituted for rho_J.

For explicit bounded recovery locality, define the recovery stencil to be
the union of the supports of the expanded R_c templates just used, together
with their actual paired-path readers and filling boxes. Its radius in
terminal-block distance is the maximum distance from the anchor to an
endpoint block in this finite union. This defines a finite number r(L)
independent of volume; the same construction with the finitely many
forest comparison templates defines a finite r_forest(L). Thus restoring
a deleted constraint reads only this bounded translate, and applying it
to a forest-link comparison enlarges its radius by at most r(L).
Surviving normalized-kernel readers include every input of their radial
normalizers. By `compact-forest-exchange.md` §3, their reduced readers
are the original readers minus tree variables; pulling back to original
variables adds only the internal trees in endpoint blocks. Arbitrary tree
shape changes neither this endpoint-block locality nor the constants above.

## 5. Consumer and limit

All steps hold at zero means and throughout the compact configuration space.
In particular E_J=0 forces all forest coordinates to I; this conclusion
comes from (T), not merely from complement-graph connectivity. The separate
eight-edge isolated-root counterexample is outside this seven-edge geometry.
The exact consumer is the identity-exterior, zero-source two-plaquette
marginal's compact leading-energy estimate on the unchanged forest slice.
The estimate alone proves no rough-sector probability bound, normalized-law
Hessian bound, connected-cumulant decay, physical gap, or all-depth theorem.
No numerical jobs, Git writes, or prompt edits were performed. This draft
requires the parent's full mathematical read and the assigned fresh checker.
