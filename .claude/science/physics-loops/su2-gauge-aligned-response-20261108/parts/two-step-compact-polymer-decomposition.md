# Exact compact insertions in the common two-step chart measure

Author proof, 2026-11-09; independent check pending. This is an adaptation
of the first-successful-shell partition and simultaneous common-chart
resummation in `HOLOMORPHIC_COMPACT_RETURN_ASTRA.md`, HC10–HC21, lines
200–397, at `89faef229ff6e6bde42baad15ed8270c2f4087d8`. Those passages
were read together with their setup; their author receives credit for this
architecture and its annular bookkeeping. Bałaban localization and Dimock's
exposition are the constructive antecedents credited there. No holomorphic,
source, transported-chart or Gaussian consumer theorem from that work is
imported. This proof concerns real fields, zero sources, terminal identity,
and no cut (χ_cut=1), with the actual two-hidden-layer chain throughout.

The local energy and normalizer estimates are §§1–4 of
`arbitrary-boundary-interior-moments.md`, SHA-256
`c58acdf2d0391847c631a358fcad2bd280e8f563c19947f976118272a4426d11`.
They include global E≥c_E Σ_e b_e, reader radius one, whole-factor ownership,
and constants K_E,K_r. This proof rechecks their specific uses below. No
intermediate Wilson action is introduced. No prior proof is edited. Read-only
access to the pinned historical source is the only Git operation; there are
no Git/network mutations or numerical jobs. This is a bounded real compact
decomposition, not a connected-log or response estimate.

## 1. Parameters, chart and actual density

Keep fixed odd L≥3 and κ>0, with terminal-cell periodic l-infinity distance.
Each cell owns M=3L^8+1+4L^4 retained SU(2) coordinates, all fine non-tree
and all intermediate links. For such a coordinate set b_e=1−w(a_e), and
T_X=Σ_(e owned by X)b_e, T_A=Σ_(X∈A)T_X. Thus 0≤T_X≤2M.
The unnormalized actual quotient density, relative to product Haar, is

    w(a)=exp[−u E(a)] Π_(both kernel levels c) H(κu r_c(a)),
    H(t)=exp(t)/Z(t),  r_c=|M_c|,
    E=W(U0)+κΣ_c (r_c−<output_c,M_c>).                  (P1)

Every hidden output and every input-dependent normalizer is retained.
Terminal outputs are I. No division by r_c is used, so zero means are allowed.

Fix a>5/2 and put σ=u^(−1/2), p(u)=log(2+u)^a, ρ=σp(u).
For u≥u0 chosen below, define the product chart C on every retained link by
principal exponential coordinates a_e=exp(i z_e·σ_Pauli), |z_e,k|<ρ
for k=1,2,3. Require sqrt(3)ρ<π and ρ sufficiently small for a unique
chart; this holds for all sufficiently large u. Write

    q=c_q ρ²,  c_q=1/(2π²),
    good(X) iff T_X<q; bad(X) iff T_X≥q.                (P2)

Indeed, for principal angle θ∈[0,π], θ≤(π/2)|a_e−I|, hence
θ²≤(π²/2)b_e. If T_X<q, every owned logarithm has norm <ρ/2 and lies
inside C. Therefore every all-good configuration is in the global chart.
The reverse implication is not used and is generally false.

Fix d0∈(0,1]. Increase u0 so (π/2)d0<p(u), q<1 and the preceding
chart conditions hold. The product chord cap |a_e−I|≤d0/sqrt(u) then
lies inside the regional chart, up to immaterial Haar-null chart boundaries.
Its Haar mass is at least (c_cap d0³)^n u^(−3n/2) on n links.

Let C_shell=2K_E+K_r and fix

    α=min(1,c_E/(4C_shell))>0.

Choose K to be the least positive integer satisfying

    (1+α)^K q>2M(4K+1)^4,                              (P3)

This is a deterministic volume-independent choice. Such K exists
because exponential growth dominates a polynomial. It can be chosen with
K=O(1+log(1/q)) as q→0: for example K=ceil[Cα(1+log(1/q))]
works for all sufficiently small q when Cα>2/log(1+α), after increasing
the fixed threshold to dominate the fourth power and constants. Put

    d_conn=4K+4,  V_K=(4K+1)^4.

The exact identities and bounds through (P19) hold for any K satisfying (P3),
including tori smaller than these neighborhoods. The asymptotic simplification
(P20) uses the prescribed least-K choice and its O(log(1/q)) bound. Periodic
coincidences only decrease volumes.

## 2. Unique first-successful-shell partition

Call a nonempty cell set A connected if connected in the graph joining cells
at distance at most d_conn. For every such A and 0≤j<K define

    I_j(A)=N_(2j)(A),  R_j(A)=N_(2j+1)(A),
    S_j(A)=N_(2j+2)(A)\R_j(A).

Define the local selector

    ell_(A,j)=1_(T_X≥q for X∈A)
       ·1_(T_X<q for X∈R_j(A)\A)
       ·1_(T_(S_j)≤α T_(I_j))
       ·Π_(0≤i<j)1_(T_(S_i)>α T_(I_i)).                (P4)

All failure tests for i<j lie inside R_j; the sole possible exterior test
is the successful shell S_j. A history h is a finite unordered collection
of pairs (A,j), whose cores are nonempty connected sets at pairwise distance
strictly greater than d_conn, with 0≤j<K. Include the empty history. Set
R_h=union_(h)R_j(A), O_h=torus\R_h and

    Π_h=1_good(O_h) Π_(h) ell_(A,j).                    (P5)

Then pointwise on the full compact configuration space,

    Σ_h Π_h=1.                                        (P6)

Proof: take the actual bad-cell set and its d_conn-connected components.
For a component A, every cell in N_(2K)(A)\A is good, since 2K<d_conn.
If all K shell tests failed, then I_(j+1)=N_(2j+2)(A) contains disjoint
I_j and S_j, so T_(I_(j+1))>(1+α)T_(I_j). Thus
T_(I_K)>(1+α)^K q|A|. But T_(I_K)≤2M|N_(2K)(A)|≤2M V_K|A|,
contradicting (P3). There is exactly one first successful j. The resulting
history satisfies (P5). Conversely, any nonzero (P5) identifies exactly the
bad set as the union of its cores; separation and connectedness identify
these as its components, and the failed tests identify each first j uniquely.
The all-good configuration belongs only to the empty history. T_X=q is
unambiguously bad. Empty shells and whole-torus regions cause no exception.

## 3. Regional compact difference and one energy payment

For (A,j), write R=R_j(A), I=I_j(A), S=S_j(A). Fix exterior z that is
q-good on every cell of S. Let w_R(a_R,z) be the product of ALL actual
plaquette and whole normalized-kernel factors whose syntactic retained
readers meet J_R. Hidden outputs and every normalizer are included even
when their input dependence is constant under this conditioning. Exterior
factors are absent only because they are the identical W_out in the exact
factorization. With n=M|R| and k=|C_R|,

    w_R=exp[−uE_R] Π_(c∈C_R)H(κu r_c).

Every exterior reader belongs to N_1(R)\R=S. Define

    I_R(z)=integral_(C on J_R) w_R(a_R,z) dH_(J_R),
    N^c_(A,j)(z)=integral_(SU(2)^J_R) ell_(A,j) w_R dH_(J_R),
    N^a_(A,j)(z)=integral_(C on J_R) ell_(A,j) w_R dH_(J_R),
    N^out_(A,j)=N^c_(A,j)−N^a_(A,j),
    B^c=N^c/I_R,  B^a=N^a/I_R,  D=N^out/I_R.           (P7)

The denominator is strictly positive for every real exterior, since the
chart is a nonempty open product set and all original factors are positive.
The difference N^out is one integral over the compact regional complement
of the product chart with the SAME selector and exterior. Thus D≥0 and
B^c=B^a+D, without a factor two. For bookkeeping define B^c,B^a,D to be
zero when S is not q-good. Their identities are then still true pointwise.
The unextended integral definitions are used only on the admitted q-good
exterior domain. No complex continuation or zero-mean exclusion is involved.

The inherited lower bound and normalizer comparison are

    E_R≥c_E T_R−K_E T_S,
    H(κu)exp[−κu(1−r_c)]≤H(κu r_c)≤H(κu).             (P8)

The inherited upper bounds E_R≤K_E(T_R+T_S) and
κΣ_(c∈C_R)(1−r_c)≤K_r(T_R+T_S), integrated on the cap from §1,
give the CHART denominator bound

    I_R(z)≥H(κu)^k exp[−(K_E+K_r)uT_S−(K_E+K_r)nd0²/2]
                     (c_cap d0³)^n u^(−3n/2).         (P9)

All H factors are retained exactly, including constant normalizers.
On the selector, T_S≤α T_I and T_I≥q|A|, with T_I≤T_R. After dividing
by (P9), the energy in the compact numerator is bounded below by

    c_E T_R−(2K_E+K_r)T_S
       ≥(c_E/2)T_R+(c_E/2)T_I−C_shell T_S
       ≥(c_E/2)T_R+(c_E/4)T_I
       ≥(c_E/2)T_R+(c_E/4)q|A|.                        (P10)

The shell budget uses T_I BEFORE extracting its fixed core charge. Replacing
T_I prematurely by q|A| would not justify absorbing an arbitrarily larger
T_S. Conversely the residual (c_E/2)T_R is kept for integration rather than
spent a second time as a core charge.

The compact Haar estimate integral exp[−(c_Eu/2)b(Q)]dQ≤K0 u^(−3/2)
now applies independently to every active coordinate. Both H(κu)^k and
u^(−3n/2) cancel their exact denominator factors, so for C≥1 fixed by
L,κ,d0 and the supplied geometry, independent of u,K,A,j and volume,

    0≤B^c, B^a, D ≤ C^|R| exp[−c_E u q|A|/4]
                     ≤exp[(log C)V_K|A|−c_E u q|A|/4]. (P11)

For example take C=max(1,[exp((K_E+K_r)d0²/2)
K0/(c_cap d0³)]^M). The same estimate for B^a and D follows either by the
same restricted integral or by their nonnegativity and domination by B^c.
No numerator means, second-layer measures, or fine-field normalizers were
replaced. Their reader support is the actual regional S, bounded uniformly
by the stated neighborhoods, even though each coefficient is defined by
integrating all of R.

## 4. The two common-chart history identities

Let Z_c=integral_(all compact coordinates)w dH and Z_a=integral_C w dH.
Both are finite and strictly positive. Let <·>_a denote expectation in the
ONE normalized global chart law w1_C/Z_a, not a product of regional laws.
If two cores have distance >d_conn, their regions have distance at least

    (d_conn+1)−2(2K−1)=7.

Since every original factor's owned reader diameter is at most one, no
factor touches two active regions. Assign each touching plaquette and each
whole kernel to its unique region once; all other factors form W_out,h.
This gives the exact factorization

    w=W_out,h Π_(h)w_(R_j).                            (P12)

The same statement includes every normalizer and all hidden outputs.
On the support of a history, all cells in O_h are good, hence their
coordinates lie in the chart. Regional integrations in the compact
partition therefore leave only a chart exterior. Conversely, conditional
integration over the dummy active chart regions produces exactly Π_h I_Rj
from this same w. Applying (P6) and (P7) gives

    Z_c/Z_a=Σ_h <1_good(O_h) Π_(h)B^c_(A,j)>_a,
          1=Σ_h <1_good(O_h) Π_(h)B^a_(A,j)>_a.         (P13)

The q-good zero extension is harmless because S_j⊂O_h for separated active
regions. The empty-history contribution in BOTH sums is

    <1_good(all cells)>_a=Z_good/Z_a,

not one in general: the chart also contains cells with T_X≥q. Every active
regional chart integral has its full domain and has not been additionally
normalized or capped. Equations (P13) retain all vacuum factors.

## 5. Resumming unselected chart histories exactly

Expand each B^c=B^a+D in the first line of (P13). A selected family s is
any separated family of pairs (A,j) occurring as a subset of a history;
it need not be the actual bad set of the dummy chart coordinates. Define

    R_s=union_(s) R_j(A),
    H_s=(union_(s)N_(d_conn)(A))\R_s.                  (P14)

Then the exact finite identity is

    Σ_(h contains s)<1_good(O_h) Π_(s)D_(A,j)
                                      Π_(h\s)B^a_(A,j)>_a
       =<1_good(H_s) Π_(s)D_(A,j)>_a.                  (P15)

For s empty it is the second line of (P13), so its resummed value is one,
although the individual empty history in (P13) is not one.

Here is the conditional-domain proof of (P15). First integrate the selected
regions as dummy chart variables. Each selected D reads only its S_j,
disjoint from every selected R; H_s also excludes all selected R. The
factorization (P12) supplies Π_(s)I_Rj on this marginal. Those integrals
are uncapped: no condition on a selected core is imposed on its dummy
variables, because its entire compact-minus-chart selector integral has
already been put into D.

On the remaining real chart coordinates impose good(H_s). Any remaining
bad cell is outside R_s and outside every N_(d_conn)(A) for A selected.
Its connected bad component is therefore at distance >d_conn from each
selected core. Conversely those are precisely the additional cores allowed
in a history containing s. The full first-shell test of an additional core
uses N_(2K) of that core, disjoint from every selected region (their active
regions are separated by at least seven). Thus its first successful j is
determined wholly by the remaining variables and is unchanged by the dummy
integration. Summing all such additional chart histories partitions those
remaining variables exactly, by the same shell-growth argument as §2.
The selected marginal factors I_Rj and D are constant in each additional
active region, since even their shells cannot meet those regions. This
justifies restoring each unselected B^a to its actual local selector integral.

An annular intersection must be handled explicitly. N_(d_conn)(A) for a
selected core can meet the ACTIVE region of an additional core, although it
cannot meet that additional bad core. Its intersection is therefore in that
region minus its core, where ell already requires good cells. This gives the
same predicate on either side after restoring its selector integral. In
contrast, N_(d_conn)(A) may meet ANOTHER SELECTED active region whose chart
variables are dummy. Such a condition must be removed, not imposed: otherwise
its I_R would be replaced by a capped integral and (P15) would be false.
The subtraction of ALL R_s in (P14), not only each core's own region,
implements exactly this requirement. No residual all-exterior good cap is
left after this resummation.

All sums here are finite for each finite torus, so exchanging sums and real
integrals needs no convergence theorem. The proof uses the actual conditional
factorization; it assigns no independence to the global chart measure.

## 6. Exact gas grouped by complete reader overlap

For a core A set Γ_A=N_(d_conn+2)(A). A polymer label g is a nonempty
finite family of pairs (A,j) with pairwise core distance >d_conn, such that
the overlap graph of the Γ_A is connected. The whole list of cores and
indices is retained in the label; distinct lists with the same union support
are distinct labels. Put

    Γ_g=union_(g)Γ_A,  n_g=|union_(g)A|=Σ_(g)|A|,
    H_g=(union_(g)N_(d_conn)(A))\(union_(g)R_j(A)),
    Θ_g=1_good(H_g) Π_(g)D_(A,j).                      (P16)

Define this function to be zero off good(H_g) before evaluating its regional
ratios. On that domain each selected shell is good, since it lies in H_g.
All its remaining coordinate arguments are real chart variables. Its native
reader is Γ_g: this deliberately retains the original regional factor,
normalizer, membership, absence and failed-shell labels, even though after
regional integration its live exterior coordinate arguments lie in H_g.
No smaller support is assigned merely from a critical-point or covariance
representation, neither of which is used here.

Two polymers are compatible precisely when their Γ_g are disjoint. Any
selected family s splits uniquely into the overlap-connected components of
its Γ_A. Conversely, a compatible family of polymer labels reconstructs a
unique selected s. Indeed, a cross-group core distance ≤d_conn would force
Γ overlap; cross-group annular/active-region intersections would also force
Γ overlap. Thus all the required separations hold and H_s is the disjoint
union of the H_g. Products of their good predicates and D factors agree
exactly with the right side of (P15). Consequently

    Z_c/Z_a = < Σ_(Γ-compatible families F) Π_(g∈F)Θ_g >_a.       (P17)

The empty polymer family contributes one; it is the RESUMMED all-chart
history contribution, not the unresummed empty history in (P13). Every
possible field-independent Θ_g, including H_g empty, is retained with its
nonempty labeled reader Γ_g. Such a term is not dropped as a vacuum.

The regional estimate (P11), with |R_j(A)|≤V_K|A|, gives

    0≤Θ_g≤exp[(log C)V_K n_g−c_Eu q n_g/4].            (P18)

Also

    |H_g|≤(8K+9)^4 n_g,
    |Γ_g|≤(8K+13)^4 n_g.                              (P19)

These are union-volume upper bounds, valid with periodic overlaps. All
constants C,c_E are fixed independently of u and volume; K,q depend on u
as explicitly prescribed. Since K=O(log(1/q))=O(log u), while
u q=c_q log(2+u)^(2a), a>5/2 implies, for sufficiently large u,
(log C)V_K≤c_Eu q/8. On that domain (P18) simplifies to

    0≤Θ_g≤exp[−c_Eu q n_g/8].                          (P20)

No optimal exponent threshold is claimed; a>5/2 is the chosen scale.
Equations (P17)–(P20) give an exact real gas of bounded compact insertions
inside the actual normalized global chart expectation. They do not factor
that expectation over polymers. In particular (P17) is not a numerical
hard-core gas with independently assigned scalar activities.

## 7. What has and has not been closed

Author-proof closures: the exact all-compact first-successful-shell partition;
the compact-minus-chart regional insertion with all normalized two-layer
factors; its uniform bound by one retained energy charge and matched Haar
powers; simultaneous resummation of all unselected chart histories; and the
exact common-chart expectation gas with complete reader labels.

The independent gate must examine the conditional-domain proof of (P15),
the factor/reader allocation and the shell-energy split in (P10), together
with the inherited coercivity and normalizer inputs. The construction is a
checked-hypothesis adaptation of the pinned prior architecture, not a claim
of architectural novelty or imported historical theorem status.

No derivatives in sources or terminal tangents have been taken. Such marked
extensions must check their own normalized regional integrals, original-source insertions on their actual
readers, the full coarse log Q subtraction, and reader enlargement. No complex domain, transported chart, Gaussian forest,
connected-log norm, connected-response decay, arbitrary-boundary clustering,
or physical gap is proved here. The full compact connected-log consumer
remains a separate obligation; (P17) alone does not close it.
