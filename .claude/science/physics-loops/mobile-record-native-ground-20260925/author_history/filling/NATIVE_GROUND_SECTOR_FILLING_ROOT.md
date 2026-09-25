# Native ground-sector filling in the supplied common Hamiltonian

Root candidate, 2026-09-25. Personally derived; not yet independently checked.
This is conditional mathematics about the supplied compensated model. It
does not select the physical vacuum or identify an observed particle.

## Premises and provenance

Use an even cubic torus of side \(L\ge6\), with nearest-neighbour bipartition
\(A\cup B\), \(n=|A|=|B|=L^3/2\), integer rotor electric fields, the original
unsigned tensor hard-core matter, and Gauss law
\(\operatorname{div}E=q-\mathbf1_A\). The \(P\) space has every \(A\) site
occupied by a charge \(q_a=\pm1\), and each \(B\) site empty or occupied by
\(\pm1\). Keep the full original formation channels and every output sector.

The load-bearing main sources are the local-pair/general-graph magnetic
dynamics and local-compensation common-field-record limit notes, pinned in
SOURCE_PINS.json. Their supplied Hamiltonian is
\[
h_g=\frac{g^2}{2\tau}D+\frac{1}{4\tau g^2}H_4,\qquad
D=\sum_{a\to b}\mathbf1_{\{q_b=0\}}E_{ab}(E_{ab}-q_a),\qquad
H_4=-2\sum_{\{a,c\}}(F_cF_aP)^*F_cF_aP.                 \tag{1}
\]
The sum is over distinct overlapping \(A\) stars. Fix \(\tau>0\), then take
\(g\downarrow0\) at fixed \(L\). The empty-\(B\) gate in \(D\) is essential;
no field-only replacement is made. On the electric basis \(D\ge0\), because
each integer \(e\) obeys \(e(e-1)\ge0\) and \(e(e+1)\ge0\).

The earlier personally derived one-pair calculation supplied a local row
polynomial. The independently reconstructed PRE for that calculation, read
before this extension, supplied a general two-particle uniform trial. These
motivated asking about arbitrary occupancy. This note proves its general
occupancy identities and estimates explicitly; the earlier work is
provisional context, not a retained audit or an independent check of this
extension. This convention uses \(H_4=-2Q\) in the occupation representation,
as in that PRE; the earlier root's \(Q\) was twice this \(Q\).

## Claim

Let \(m\) be the number of occupied \(B\) sites. A physical \(P\) sector has
\[
N=n+m,\qquad m\in\{0,2,\ldots,n\},\qquad
\#\{\hbox{minus charges}\}=m/2.                         \tag{2}
\]
Let \(e_m(g)\) be the spectral infimum of (1) in this sector, over all
allowed charge assignments and electric flows. For every fixed even
\(L\ge6\), there is \(g_0(L,\tau)>0\) such that, for \(0<g<g_0\), every
sector satisfying \(e_m(g)=\min_k e_k(g)\) obeys
\[
\boxed{\quad \frac{421}{2640}<\frac mn<
                    \frac{4103}{6008}\quad}             \tag{3}
\]
(approximately \(0.1594697<m/n<0.6829228\)).

The finite set of sectors has at least one minimizing spectral infimum.
This does not assert a normalizable ground eigenvector. The bound proves
that both occupied and vacant \(B\) sites have a finite fraction in any
energetically minimizing sector of this specified regime. The threshold
is not uniform in \(L\); there is no fixed-\(g\) thermodynamic conclusion.

## Physical color space and occupation representation

Summing Gauss law gives total charge \(n\), proving (2). Conversely every
assignment satisfying (2) admits an integer Gauss flow: route its
zero-total divergence along a spanning tree. For each matter word choose
one such flow. All other flows are an affine integer cycle lattice. Fourier
transformation in the full cycle lattice, including harmonic winding
directions, gives a finite matter matrix for \(H_4\) at each angle \(\theta\).

Every legal four-hop path in (1) moves occupied charge slots bijectively:
two distinct \(A\) charges leave for vacant \(B\) sites, and two occupied
\(B\) charges return to the vacant \(A\) sites. The returning charges may
be pre-existing records. Allowedness depends on occupancy, not charge sign.
At \(\theta=0\), every path has a positive integer coefficient. For a
fixed occupied set \(X\subset B\), \(|X|=m\), there are exactly
\(\binom{n+m}{m/2}\) allowed minus assignments, independent of \(X\).
Their normalized uniform sum gives an isometry \(J_m\) from occupation
space into the full color space.

Write the full magnetic matrix as \(-2K_m(\theta)\). The path bijections
give \(K_m(0)J_m=J_mQ_m\). Here \(Q_m\) is a Gram matrix of auxiliary
unordered-pair creation maps on \(m\)-element subsets of \(B\).
This is only a combinatorial representation of the Hamiltonian.
It does not replace the physical matter or formation instrument.
Full colored row sums equal occupation row sums, independently of the
minus assignment. Moreover
\[
|K_m(\theta)_{\eta\xi}|\le K_m(0)_{\eta\xi}.
\]
For any vector, the quadratic-form modulus bound and the symmetric
nonnegative row-sum bound therefore give
\[
\lambda_{\max}(K_m(\theta))
 \le\max_X\operatorname{rowsum}_X Q_m.                  \tag{4}
\]
No irreducibility or full color-spectrum reduction is needed here.

## Uniform-occupation trial

For one overlapping pair of \(A\) stars, define
\[
w(D)=\#\{(b,d):b\in N(a),\,d\in N(c),\,b\ne d,\,
                         \{b,d\}=D\}.
\]
If \(u_m=\binom nm^{-1/2}\sum_{|X|=m}|X\rangle\), the pair-creation map
has amplitude \(\binom nm^{-1/2}\sum_{D\subset R}w(D)\) at an intermediate
set \(R\) of size \(m+2\). Squaring and summing over \(R\) gives three
terms, according to whether \(D,D'\) coincide, share one site, or are
disjoint. With ordered pairs \(D,D'\), define
\[
v=\sum_Dw(D)^2,\quad
a=\sum_{|D\cap D'|=1}w(D)w(D'),\quad
d=\sum_{D\cap D'=\varnothing}w(D)w(D').
\]
The contribution is exactly
\[
\frac{v\binom{n-2}{m}+a\binom{n-3}{m-1}
                    +d\binom{n-4}{m-2}}{\binom nm}.     \tag{5}
\]
Binomial coefficients outside their range are zero.

For two degree-six stars with overlap \(r=1,2\), the total weight is
\(36-r\). Each common vertex has weighted incidence 10 and each exclusive
vertex incidence 6. Thus
\[
v=36+r^2-2r,\quad
a=100r+36(12-2r)-2v,\quad d=(36-r)^2-v-a.
\]
For \(r=1\), these are \((35,390,800)\); for \(r=2\),
\((36,416,704)\). An even cubic torus \(L\ge6\) has \(3n\) overlap-one
pairs (axial displacement two) and \(6n\) overlap-two pairs (two unit
coordinate displacements). There are no side-four wrap coincidences.
Summing (5), put
\[
V=321n,\quad A=3666n,\quad D_4=6624n,\qquad
R_m=\langle u_m,Q_mu_m\rangle
 =\frac{V\binom{n-2}{m}+A\binom{n-3}{m-1}
                         +D_4\binom{n-4}{m-2}}{\binom nm}. \tag{6}
\]

Since \(n=4(L/2)^3\), \(m=n/2\) is an allowed even occupancy. Direct
rational simplification of (6) gives
\[
\begin{split}
\frac{R_{n/2}}n
 &=\frac{321(n-2)}{4(n-1)}
   +\frac{3666n}{8(n-1)}
   +\frac{414n(n-2)}{(n-1)(n-3)}\\
 &=\frac{1905}{2}+\frac{378}{n-1}
                  +\frac{414(2n-3)}{(n-1)(n-3)}
 >\frac{1905}{2}.                                      \tag{7}
\end{split}
\]
This is a variational quotient, not a computed Perron eigenvalue.

## Uniform row bounds at arbitrary occupancy

For a fixed occupied set \(X\), define
\[
s_a=|X\cap N(a)|,\ s_c=|X\cap N(c)|,\ t=|X\cap N(a)\cap N(c)|,
\quad n_a=6-s_a,\ n_c=6-s_c,\ n_i=r-t.
\]
There are \(n_an_c-n_i\) legal ordered outward pairs. After an outward
pair \(b\in N(a)\setminus X,d\in N(c)\setminus X\), the return multiplicity
is
\[
(s_a+1+\mathbf1_{\{d\in N(a)\}})
(s_c+1+\mathbf1_{\{b\in N(c)\}})
-t-\mathbf1_{\{b\in N(c)\}}-\mathbf1_{\{d\in N(a)\}}.
\]
The subtraction excludes returning the same occupied \(B\) charge twice.
Summing this expression over distinct \(b,d\) gives the exact row polynomial
\[
P_r=(n_an_c-n_i)[(s_a+1)(s_c+1)-t]
       +s_an_i(n_c-1)+s_cn_i(n_a-1)+n_i(n_i-1).          \tag{8}
\]
The term with product of the two indicators counts distinct vacant
common neighbours. In particular, (8) retains all returns of old records.

Put \(\ell=s_a+s_c-t\), \(z=12-r-\ell\), the occupied and vacant sites in
the two-star union. The complete pattern set is
\[
0\le t\le r,\qquad 0\le s_a-t,s_c-t\le6-r.
\]
It has 72 patterns for \(r=1\) and 75 for \(r=2\). Substitution into (8)
gives the following exact maxima, excluding a zero denominator:

| overlap \(r\) | common occupancy \(t\) | patterns | maximum \((P_r-v)/\ell\) | maximum \(P_r/z\) |
|---|---|---|---|---|
| 1 | 0 | 36 | \(69/2\) | \(28\) |
| 1 | 1 | 36 | \(40\) | \(24\) |
| 2 | 0 | 25 | \(37\) | \(104/3\) |
| 2 | 1 | 25 | \(44\) | \(80/3\) |
| 2 | 2 | 25 | \(38\) | \(23\) |

When \(\ell=0\), \(P_r=v\); when \(z=0\), \(P_r=0\).
Thus the finite substitutions, also preserved individually in the exact
certificate, prove
\[
P_1\le35+40\ell,\quad P_2\le36+44\ell,\qquad
P_1\le28z,\quad P_2\le(104/3)z.                         \tag{9}
\]
This is a finite exhaustive proof with explicit domain, not a
floating-point search. The source program also compares (8) to direct
intermediate-set Gram counting for every one of the \(2^{11}+2^{10}=3072\)
local occupied subsets; the two calculations have distinct counting forms.
This root control is not an independent review.

Translation transitivity on \(B\), the pair counts above, and union sizes
11 and 10 show that every \(B\) site belongs to exactly 33 overlap-one
and 60 overlap-two unions. Hence
\[
\max_X\operatorname{rowsum}_XQ_m
 \le B_m:=\min\{321n+3960m,\;3004(n-m)\}.                \tag{10}
\]
The coefficients are \(33(40)+60(44)=3960\) and
\(33(28)+60(104/3)=3004\). Equations (4), (10) and \(D\ge0\) imply
\[
e_m(g)\ge-\frac{B_m}{2\tau g^2}.                       \tag{11}
\]

## Physical variational comparison and proof of (3)

The occupation-color vector \(J_{n/2}u_{n/2}\) at zero angle is not a
normalizable rotor state. Multiply it by a normalized smooth real even
bump \(\phi_g\), supported in a width-\(g\) chart about zero in all cycle
angles. This is a legitimate Gauss-compatible finite-graph trial.
Every chosen reference flow is finite, every relevant cycle shift is finite,
and the matter fiber is finite. In this representation each electric
operator is an affine first derivative. Therefore
\[
\langle D\rangle_{\phi_gJ u}=O_L(g^{-2}).
\]
The finite Laurent magnetic matrix is analytic in the angles. Its scalar
expectation in the real vector \(Ju\) is even in \(\theta\), so
\[
\langle K\rangle_{\phi_gJ u}=R_{n/2}+O_L(g^2).
\]
The trial belongs to the electric operator domain. Substitution in (1)
gives, at fixed \(\tau\),
\[
e_{n/2}(g)\le-\frac{R_{n/2}}{2\tau g^2}+C_{L,\tau},     \tag{12}
\]
for a finite constant independent of sufficiently small \(g\).
Localizing harmonic angles is permitted for this variational comparison;
it is not an assertion about the initial zero-electric-winding state,
whose harmonic-angle distribution is Haar.

If \(m/n\le421/2640\), the first bound in (10) is at most
\((1905/2)n\). If \(m/n\ge4103/6008\), the second bound is at most the
same quantity. Equation (7) leaves a strictly positive gap
\(R_{n/2}-(1905/2)n\) for every fixed graph. For sufficiently small \(g\),
this gap divided by \(2\tau g^2\) exceeds the finite error in (12).
Equations (11) and (12) then imply \(e_m(g)>e_{n/2}(g)\) in either
excluded range, proving (3), including strict endpoint exclusion.

## Exact controls and scope

The root program and complete output verify all 147 pattern rows with their
multiplicities, all 3072 local subsets, 26 uniform-occupancy averages for
artificial 12-site ambient sets, and the actual torus geometry for
\(L=6,8,10,12\). The artificial ambient sets check (5); they are not
physical torus simulations. Seven even occupancies per torus check (6),
(7), (10), including zero and full occupancy. These are not full many-body
diagonalizations. Timers, exact fractions and source hashes are preserved.
No scientific numerical failure occurred in this control. The unsealed
working derivation is retained verbatim, including a typographical artifact.

## Consequence for the observational bridge

If a physical identification requires the energy-minimizing vacuum of
(1), the empty sector cannot be repaired merely by adding a fixed small
number of pairs in this fixed-graph small-\(g\) regime. A collective
matter-field sector with appreciable records and vacancies must be treated
before assigning its excitation energies to observed particles.

The conditional premise is not adopted here. A prepared metastable sector
can be physically relevant without minimizing the entire Hamiltonian.
The original unitary dynamics conserves \(N\), while the formation channels
raise it; neither (3) nor a lower energy proves spontaneous unitary decay,
relaxation to the minimum, or a stationary source. No reservoir, physical
scale, laboratory vacuum, photon absorption, observed mass or empirical
exclusion is established. A selected nonequilibrium preparation and a
justified observation functional remain alternative routes.

## No-Go Discipline Gate — bounded claim audit

- N1, alternatives: retain the original model and distinguish a selected
  metastable preparation, a different supplied Hamiltonian, and the
  global spectral minimum. Only the last is constrained by (3).
- N2, wall independence: this estimate concerns number-sector energetics.
  It does not strengthen count identifiability or optical calibration
  bounds merely because those also leave observation work open.
- N3, hidden assumptions: even \(L\ge6\), exact degree six, unsigned
  hard-core paths, full Gauss/color/cycle space, the actual gated \(D\),
  and fixed graph before small \(g\) are explicit.
- N4, residual matching: all sectors use the same \(g,\tau\), Hamiltonian
  and zero of energy. No number-dependent energy offset is introduced.
  A finite variational \(O_L(1)\) remainder is beaten at each fixed graph;
  no uniform macroscopic error is asserted.
- N5, resolution: per-element and local-pattern counting is exact; all
  sites of four finite tori are checked for incidence. No full energy
  spectrum, fast-generator spectrum, large-volume convergence or
  experimental dataset is executed by this runner.
- N6, partial closure: (3) bounds possible minimizing sectors but does
  not identify their phases, degeneracy, excitations or dynamics.
- N7, strongest alternative: an observed vacuum or detector could be a
  stable prepared or driven state in a conserved-number sector. The
  present proof does not exclude that identification; its preparation,
  stability and response would still need derivation.
- N8, prior-result boundary: the previous one-pair edge is not counted
  as another independent reason. The new content is the arbitrary
  occupancy average, two all-occupancy row bounds and their finite
  fraction consequence. No framework no-go or TOE completion follows.
