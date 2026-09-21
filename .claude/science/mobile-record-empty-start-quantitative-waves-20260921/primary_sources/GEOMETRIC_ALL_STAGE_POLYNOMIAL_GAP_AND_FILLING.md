# Polynomial relaxation at every stage and a fixed-rate filling bound

2026-09-21. Root conditional proof candidate; independent check pending.
This completes a quantitative comparison left open in the all-stage clock
note, for bipartite graphs with a perfect matching and a controlled final-pair
matching-count ratio. The microscopic process is unchanged. Auxiliary dummy
vertices, deletions and nonlocal exchanges are proof devices only.

## 1. Definitions, dependencies and results

Let G be a connected simple bipartite graph with K vertices in each part,
K>=2, m edges and at least one perfect matching. Let a_r be its number of
r-edge matchings, with a_r=0 outside 0<=r<=K, and put R=a_(K-1)/a_K.
The physical geometric slide generator S_j has rate kappa>0 for every
legal replacement {b,c}->{a,b} when a is vacant. It preserves rank j.
Birth adds a vacant edge at rate beta>0. Both are the rules of the earlier
geometric formation notes. Additional symmetric conservative moves may be
included; they improve the Dirichlet lower bounds used here.

For 1<=j<K, write k=j+1, h=K-k and

    m_hat = m+2hK,
    R_hat = (h+1)^2 a_j/a_k + 2h + a_(k+1)/a_k,
    U_j = (h+1)R + 2h + m/(k+1),
    C_j = 1+(2K-2)(m+m^2)(k-1)(k+1+2m).

Then R_hat<=U_j, and the following sufficient slide-gap bound holds:

    gap(S_j) >= kappa/[256 m_hat^2 (h+2) R_hat^4 C_j]
              >= kappa/[256 m_hat^2 (h+2) U_j^4 C_j].     (1)

For the even cubic nearest-neighbor torus N>=8, K=N^3/2 and m=6K. Importing
the same explicitly identified Taggi v3 monomer bound R<=K^2/6 gives the
deliberately coarse uniform consequence

    gap(S_j) >= kappa/(2^23 K^22),  1<=j<K.              (2)

The established Jerrum--Sinclair Broder-chain bound, including its exact
continuous-time normalization, is reused from
GEOMETRIC_POLYNOMIAL_RELAXATION_AND_FORMATION.md. Its primary Theorems 2.2
and 3.6 had already been checked at the pinned source identity. The
all-cardinality connectivity, counting injection and slide/adjacent-rank
comparison are reused from GEOMETRIC_ALL_STAGE_FORMATION_CLOCK.md. Those
dependencies remain explicit; no new proof of the 1989 theorem is claimed.

Section 5 gives a uniform killed-chain estimate at every beta>0. In
particular, the cubic process satisfies

    E_empty T_fill <= 2 K^3/beta + 2^27 K^26/kappa.        (3)

This is a conservative mathematical upper bound on the supplied process.
It is not a measured growth exponent, sharp time scale, assertion of fast
practical preparation or fixed-rate uniform-matching selection. The large
power results from several loose comparisons.

## 2. A padded bipartite graph and its exact fibers

For a fixed stage j, adjoin h labeled dummy vertices to each part of G.
Connect every left dummy to every original right vertex and every right
dummy to every original left vertex. Add no dummy--dummy edges. Call this
graph G_hat. It is connected and simple, has 2(K+h) vertices and m_hat
edges, and has perfect matchings because a_k>0.

Use the ordinary continuous-time Broder chain on its perfect and near-
perfect matchings, with rate kappa per legal slide, completion or deletion
from a perfect matching. Its invariant law is uniform on that combined
space. Project a matching to the edges joining two original vertices.
Write f0=(h!)^2. The exact fiber counts are:

| Augmented state | Original rank | Fiber count per original matching |
| --- | ---: | ---: |
| Perfect | k | f0 |
| Near-perfect, both holes original | j=k-1 | (h+1)^2 f0 |
| Near-perfect, one original and one dummy hole | k | 2h f0 |
| Near-perfect, both holes dummy | k+1 | f0, when h>=1 |

For a perfect augmented matching, the h unmatched original vertices in
each part are assigned bijectively to the opposite dummy set. This gives
(h!)^2 possibilities. For two original holes, choose one unassigned
original vertex out of h+1 on each side, then assign the other h. For one
original and one dummy hole, one side has h choices of original hole, h
choices of dummy hole and (h-1)! assignments, while the other side has h!
assignments. Its count is h f0; there are two orientations. For two dummy
holes, the count is h^2((h-1)!)^2=f0. When h=0 this last class is absent
and a_(k+1)=0.

Thus the augmented near-perfect/perfect ratio is exactly R_hat. The
earlier injection gives a_j/a_k<=R/(K-j)=R/(h+1). Counting possible next
edge additions gives (k+1)a_(k+1)<=m a_k. These establish R_hat<=U_j.
They do not require an oracle or sampling of a uniform matching.

The imported Broder result applies to G_hat and yields

    gap(Broder_hat) >= kappa/(256 m_hat R_hat^4).          (4)

This chain contains no physical interpretation of a dummy vertex or record
deletion. The following comparison removes those auxiliary states.

## 3. Compare with the already defined adjacent-rank chain

Let B_j be the auxiliary chain of the all-stage note on
Omega_j union Omega_k: rate kappa for each single-edge addition/deletion
between levels and each valid single-edge exchange within either level.
The exchange may replace disjoint edges. It has the uniform invariant law.
Let Z_B=a_j+a_k, and write D_B(g)=kappa/Z_B times the sum of squared
differences over its unoriented transition edges.

Call augmented states with original rank j or k good; the remaining states
have original rank k+1 and two dummy holes. For a function g on B_j, define
F on the full augmented Broder space by

    F(eta)=g(M),                     if eta is good with projection M;
    F(eta)=(1/(k+1)) sum_(e in U) g(U-e),
                                     if its projection U has rank k+1. (5)

All augmented transitions between two states with two dummy holes leave U
unchanged. Indeed a slide adds an edge incident to a dummy hole; it can
only remove a dummy edge (unchanged U) or an original edge (exit to rank k).
There is no edge between the two dummy holes for completion. Every exit
from such a state has original projection U-e for an edge e of U.

A transition between good states either leaves the projection fixed or
projects to one B_j edge. An original/original deletion or addition changes
rank by one; replacing two original edges sharing the slide center is a
single-edge exchange. A slide involving only dummy edges leaves the
original matching unchanged. These cases exhaust the Broder moves.

Every augmented state has at most m_hat outgoing nontrivial transitions:
each graph edge supplies at most one legal proposal. Put

    f_min=(2h+1)f0,    f_max=(h+1)^2 f0.

These are the minimum and maximum good fiber sizes, including h=0. Let
Z_hat be the total augmented state count. For every constant c,

    (1/Z_hat) sum_eta |F(eta)-c|^2
       >= (f_min/Z_hat) sum_(M in B_j) |g(M)-c|^2.

Taking minima over c gives

    Var_hat(F) >= w Var_B(g),    w=f_min Z_B/Z_hat.       (6)

For a fixed projected B_j edge, at most f_max m_hat good-to-good
augmented transitions lie over it. Their normalized Dirichlet energy is
therefore bounded by kappa f_max m_hat/Z_hat times the B_j squared-edge
sum. For a fixed rank-(k+1) matching U and one parent U-e, at most
f0 m_hat augmented transitions connect that parent fiber to the two-dummy-
hole fiber over U. All internal edges of the latter have zero F increment.

Using the complete-graph variance identity,

    sum_(e in U) |g(U-e)-average|^2
        = (1/(k+1)) sum_(unordered e,f in U)
                                      |g(U-e)-g(U-f)|^2,

its boundary energy is at most kappa f0 m_hat/[Z_hat(k+1)] times the
last sum. Each pair U-e,U-f is one upper-level B_j exchange, and its union
uniquely specifies U. Hence these pairs are not duplicated across U.
Combining both energy bounds gives

    D_hat(F) <= w m_hat [f_max/f_min + f0/((k+1)f_min)] D_B(g)
              <= w m_hat(h+2) D_B(g).                   (7)

For h=0 there is no two-dummy boundary; the extra positive term is simply
an unused upper bound. The last inequality follows from
(h+1)^2/(2h+1)<=h+1 and 1/[(k+1)(2h+1)]<=1.

The Rayleigh inequality for (4), together with (6)-(7), yields

    gap(B_j) >= gap(Broder_hat)/[m_hat(h+2)].              (8)

No Markov property for the projected augmented trajectory is assumed.
In particular, the perfect and mixed-hole fibers at rank k need not have
identical projected transition rates. The function-extension comparison
is sufficient, and its fiber mass cancels explicitly in (6)-(7).

## 4. Return to physical slides and bound the cubic constants

The already proved empty-corridor comparison gives

    gap(S_j) >= gap(B_j)/C_j.

Its paths contain only actual immutable-record slides. Applying (4) and
(8) proves (1). The graph padding is bipartite; no analogous assertion is
made for a nonbipartite graph by this argument.

On the cubic torus, K>=256 and m=6K. Since j>=1,
h<=K-2 and h+2<=K. The following deliberately loose bounds suffice:

    m_hat <= 4K^2,
    U_j <= K^3/6 + 4K <= K^3,
    C_j <= 2^11 K^5.

For the last inequality use 2K-2<=2K, m+m^2<=42K^2,
k-1<=K and k+1+2m<=14K; adding the leading one stays below 2^11 K^5.
Substituting into (1) gives (2), since
256*(4K^2)^2*K*(K^3)^4*(2^11K^5)=2^23K^22.

## 5. A killed-chain estimate at arbitrary positive birth rate

This elementary estimate does not require rare births. In one nonempty
rank-j layer let L=-S be its positive symmetric generator, pi uniform,
g>0 a lower bound on its gap, n=a_j, and h(M) its vacant-edge count.
Assume 0<=h<=m and pi(h)=p>0. For a real or complex f=c+v with
c=pi(f) and pi(v)=0, the weighted triangle and square inequalities give

    p|c|^2 <= 2 pi(h|f|^2)+2m ||v||_2^2.

Thus, with E(f)=<f,Lf>+beta pi(h|f|^2),

    ||f||_2^2 <= [2/(beta p)+(1+2m/p)/g] E(f).           (9)

The smallest eigenvalue of L+beta H is consequently at least the reciprocal
of the bracket. The survival probability from a point is
(exp[-t(L+beta H)]1)(M). Its L2 norm decays at that rate and evaluation at
a point costs sqrt(n), so survival is at most min(1,sqrt(n)e^(-lambda t)).
Integrating gives the uniform mean bound

    E_M tau_j <= (1+(1/2)log a_j)
                  [2/(beta p_j)+(1+2m/p_j)/g_j].         (10)

For a singleton layer no gap is needed; its constant hazard gives the
exact exponential waiting time. The empty layer has mean 1/(beta m).
The formula is only used where the uniform sector has positive variance;
one may give a singleton an infinite gap and use (10) as an upper bound.

The strong Markov property and uniformity in the entrance matching permit
summing (10) across stages. On the cubic torus, the earlier counting
injection implies

    p_j=(j+1)a_(j+1)/a_j >= (j+1)(K-j)/R >= 6/K.

Also log a_j<=log(2^m)<=6K, so 1+(1/2)log a_j<=4K,
m/p_j<=K^2 and 1+2m/p_j<=3K^2. Each term (10) is at most

    (4/(3beta))K^2 + (12*2^23/kappa)K^25.

There are fewer than K such terms. Adding 1/(6beta K) and using
12*2^23<2^27 proves (3). Extra symmetric geometry motion can be retained:
it preserves the uniform layer law and increases the conservative gap.
The full birth/slide process remains irreversible because births add records.

## 6. One explicit simultaneous uniform-selection schedule

The fixed-rate filling bound does not make the first completed geometry
uniform. For that stronger selection goal the earlier rare-killing estimates
can now use a polynomial bound at every stage. From (2) and log a_j<=6K,

    B_j=(1+log a_j)/g_j <= 2^26 K^23/kappa.

Choose, as an explicitly volume-dependent auxiliary family,

    beta_K = kappa 2^(-32) K^(-27).                       (11)

Then delta_j=beta_K m B_j<=3/(32K^3). The total-variation distance between
the entire sequence of postbirth geometries and independent uniform
matchings of their respective ranks is at most

    sum_j 2delta_j <= 3/(16K^2).                          (12)

This follows by composing the uniform conditional exit-kernel bounds;
the empty stage has its exact uniform first edge. For normalized stage
clocks W_j=beta_K p_j tau_j, the joint Laplace transform at any fixed
vector 0<=lambda_j<=Lambda differs from the product of independent
unit-exponential transforms by at most 3(1+Lambda)/(16K^2). This uses the
earlier bounded killed-transform kernels and their telescoping composition.
It does not assert total-variation convergence for the continuous waiting
times in a dimension changing with K.

The stage conditional means satisfy

    sup_M |E_M W_j-1| <= 3/(13K^3).

Hence beta_K E_empty T_fill/C(G) has the same relative error bound, where
C(G)=sum_j 1/p_j. Together with C(G)<=K H_K/3 this supplies an expected
time O(K^28 log K/kappa) for the special selection family (11).
It is an ordered family of supplied rates, not a volume-independent law
or a claim that the fixed-beta process selects uniform matchings.

## 7. Connection to formed-state waves and remaining limits

At fixed positive beta and kappa, the color-coded paired formation rule has
the same autonomous geometric process and now the explicit expected filling
bound (3). Its final color counts remain multinomial, independently of the
geometric trajectory. The separately checked O(N^5) color-preparation time
and arbitrary-matching wave theorem can therefore follow a polynomially
bounded expected empty-start formation phase. A simulation need not approach
the enormous worst-case bound for the proof to apply.

If near-uniform full geometry is also required, (11)-(12) provide it; later
symmetric plaquette motion preserves the uniform reference law. The colors
and geometric Gauss field remain distinct. None of these improvements
derives the microscopic rates, exact content recognition, quantum coherence,
a propagating geometric photon or a physical theory of everything.

Finite controls must verify every padded fiber class, actual augmented
transition projection and the variance/energy normalization. The killed-
operator estimate requires separate matrix controls. These are tests of
the proof, not evidence of an empirical filling exponent. Independent
checking and publication integration remain pending.
