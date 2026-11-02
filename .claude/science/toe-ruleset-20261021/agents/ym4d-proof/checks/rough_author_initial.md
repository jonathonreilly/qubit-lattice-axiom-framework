# ROUGH — joint rough-core charging and its inherited-law remainder

**The requested uniform inherited-law joint moment remains OPEN.** A new
finite-depth sufficient certificate is proved below for arbitrary rough
fields: explicit nonnegative incidence matrices move all curvature and
kernel-regulator demands to original plaquettes and distinct kernel gaps.
They retain every overlap multiplicity. The certificate gives an actual
forward-chain integral bound when its capacity inequalities hold. Its
depth-uniform capacities and its local comparison with the actual inherited
reference are not established. The exact insufficient inequalities are
identified in section 7; none proves that the desired moment diverges.

| Result | Status |
|---|---|
| Quadratic nonabelian ribbon bound and backward demand propagation, Q4–Q10 | **PROVEN**, arbitrary real fields, finite depth, actual paired contours. |
| One-use original-action and forward gap integration, Q11–Q16 | **PROVEN** under displayed capacity and charge hypotheses; no filled-family restriction. |
| Four source labels and six field jets in the actual quotient, Q17–Q20 | **PROVEN** finite calculus with explicit score costs and fixed sectors; uniform local costs **OPEN**. |
| History/type/support summation, Q21–Q24 | **PROVEN conditional arithmetic** with a common envelope and explicit encoding; actual all-history inputs **OPEN**. |
| Inherited-law local comparison Q25 and the all-history target | **OPEN**. Forward normalization, positivity and individual RM23 payments do not establish it. |

PROVEN means the assertion with its hypotheses, ARGUED a proposed
construction, and OPEN an unmet obligation. No retained/audit status,
continuum existence or mass gap is asserted. Sources and independent review
are recorded in [ROUGH_LOG.md](ROUGH_LOG.md). All existing science files
and editable prompts are unchanged.

Credit: Tadeusz Balaban's organization of large fields; Jonathan Dimock's
[large-field exposition](https://arxiv.org/abs/1212.5562); and
Brydges–Slade's [normed-algebra methods](https://arxiv.org/abs/1403.7244).
These are method attributions. Needed inequalities are rebuilt here;
no recalled [m] statement or literature citation carries proof weight.

## 1. Exact law, target and permitted inputs

Use the supplied finite periodic SU(N) chain, N>=2, odd L>=3, probability
Haar, positive u_j and t_j=kappa u_j. The actual paired contour mean is
M_c=(24 L^4)^(-1) sum_gamma T_(c,gamma). Set

    f_(j,p)=s(U_(j,p))=||I-U_(j,p)||HS^2/(2N),
    S_0=u_0 sum_p f_(0,p),
    h_M(V)=Re tr(V* M)/N,
    k_t(V;M)=exp(t h_M(V))/Z_t(M),
    delta_c=1-max_W h_(M_c)(W),
    psi_c(V)=max_W h_(M_c)(W)-h_(M_c)(V).
    1-h_(M_c)(V)=delta_c+psi_c(V).                    (Q1)

Both delta and psi are nonnegative. They are used for inequalities only;
no differentiability of a chosen maximizer is assumed. All kernel
normalizers and original source coordinates remain present.

At an effective step the required quotient is still

    R_h(V;J)=int rho_(j,h)(U;J) K_j(V,U)dU,
    Z_A(V)=int chi_A(U) exp(-u_j sum_p f_(j,p)) K_j(V,U)dU,
    Q_h=R_h/Z_A.                                      (Q2)

Opening rho means retaining its actual earlier fields, action, kernels,
cuts and absence predicates. It does not turn it into a fresh Wilson
density. A normalized inherited fiber has its own normalizer, which is
not generally Z_A. The cases are distinguished in Q17–Q20.

Use REALRGA's T^(6;[4]): at most six total fine/coarse derivatives and
every subset B of four original source labels. Weights h_j=sqrt(N/u_j)
and r_i are frozen. Mixed total order ten occurs. Complete supports include
every original source, inactive root, exterior variable, normalizer reader,
history predicate and required hull. The target is the joint bound for
every selected atom set I, including overlaps, and its full rooted sum:

    sup_y T(A_I)<=product_(i in I) alpha_i,
    sup_x sum_(i:x in H_i) exp((mu+2)|H_i|) alpha_i<=1/4. (Q3)

Exact factorization across complete components is separately necessary
before a logarithm. FR (domain/selector regularity), KR (interaction and
finite-coupling estimates) and TC (original-law local coercivity/tails)
are named coordinator inputs at their actual scopes. No general version
of those inputs is assumed or rederived here.

## 2. An arbitrary-field quadratic ribbon inequality — PROVEN

Let S_c be the length-L straight transporter between centered block roots.
For each paired contour gamma, choose the ribbon obtained by moving the
straight leg along its endpoint axial path in the prescribed coordinate
order. Moving past a transverse edge attaches L plaquettes; parallel
edges cancel. Its number n_(c,gamma) of plaquette occurrences is at most
A_L=3L(L-1)/2. Let n_(c,gamma,p) count occurrences of p in this ribbon.
Projection to the torus retains multiplicities; s(P^-1)=s(P).

Each attachment inserts a conjugated plaquette. Unitary invariance of the
HS norm and telescoping give
||T_(c,gamma)-S_c||HS <= sum_occurrences ||I-U_p||HS.
Cauchy–Schwarz on the n occurrences then proves

    W_(c,p)=(24 L^4)^(-1) sum_gamma
                         n_(c,gamma) n_(c,gamma,p),
    d_c:=1-h_(M_c)(S_c)
        =(24 L^4)^(-1) sum_gamma ||T_(c,gamma)-S_c||HS^2/(2N)
        <= sum_p W_(c,p) f_(j,p),
    0<=delta_c<=d_c,       sum_p W_(c,p)<=A_L^2.         (Q4)

The n=0 term is zero. This squared-action estimate permits large,
noncommuting plaquettes and uses no small-chart hypothesis.

For any output link V_c, average
||V_c-S_c||HS^2<=2||V_c-T_gamma||HS^2+2||T_gamma-S_c||HS^2.
The first average divided by 2N equals delta_c+psi_c(V_c). Hence

    ||V_c-S_c||HS^2/(2N)<=2 psi_c+4 sum_p W_(c,p)f_(j,p). (Q5)

For a coarse plaquette P, the product S_P of its four straight
transporters bounds an L by L square. Let q_(P,p) count occurrences
in its surface, with sum_p q_(P,p)=L^2. Telescope the four output links
and the square, then square the sum of these five terms. The inequality
(sum_(k=1)^5 a_k)^2<=5 sum_k a_k^2 proves

    f_(j+1,P)<=sum_p A_(j;P,p) f_(j,p)+sum_c B_(j;P,c) psi_(j,c),
    A_(j;P,p)=5L^2 q_(P,p)+20 sum_(c in boundary P) W_(j;c,p),
    B_(j;P,c)=10 times the occurrence count of c in boundary P. (Q6)

The straight-square term before the factor five is
L^2 sum_p q_(P,p) f_(j,p); each link term is Q5. This verifies every
coefficient and retains repeated readers. The row sum of A is at most
5L^4+80 A_L^2. These constants are conservative.

If ||I-V_P||op>=epsilon, then f_(j+1,P)>=epsilon^2/(2N).
Either sum_p A_(P,p)f_(j,p)>=epsilon^2/(4N), or the four boundary
occurrences have sum psi_c>=epsilon^2/(40N), so one has
psi_c>=epsilon^2/(160N). Thus this route improves the particular
rough-input action threshold from squaring JMBRB B16's linear
mean-distance estimate. Current-level action is still not original action.

## 3. Joint demands and original ownership — PROVEN

Fix finite horizon R. Nonnegative deterministic vectors xi_j on
plaquettes and eta_j on kernel links describe the product regulator:

    Ecal=sum_(j=0)^R xi_j.f_j
                    +sum_(j=0)^(R-1) eta_j.(delta_j+psi_j). (Q7)

For REALRGA G_m, xi_(j,p)=a u_j m_(j,owner(p)) and
eta_(j,c)=a t_j m_(j,owner(c)). Add multiplicities of ALL selected
atoms before Q7. Optional chart-distance regulators require a separate
transport inequality and are excluded from this certificate.

Define backward, without matrix inversion,

    v_R=xi_R,
    v_j=xi_j+W_j^T eta_j+A_j^T v_(j+1),
    g_j=eta_j+B_j^T v_(j+1),          j=R-1,...,0.
    Ecal<=v_0.f_0+sum_j g_j.psi_j.                      (Q8)

Substitute Q4 and Q6 at the last level and repeat. Nonnegative
coefficients preserve each inequality, proving Q8 by finite induction.
Superposing demands superposes v and g exactly. Grouping overlapping
cores after integration cannot reduce that incurred load. All ancestor
readers remain; no backward cone is called a set of rough witnesses.

For each rough core G choose omega_(G,p)>=0 and put
D_G=u_0 sum_p omega_(G,p) f_(0,p). If previous uses spent fractions
z_p, the original capacity test is

    z_p+v_(0,p)/u_0+sum_G omega_(G,p)<=1  for EVERY p.   (Q9)

Nonnegative real-source costs and further original reserves must also
be included. Kernel fluctuation capacity is

    b_(j,c):=g_(j,c)/t_j<=1,                            (Q10)

with b<=1-epsilon_b needed to retain a fixed fraction of a gap price.
Q9 is the once-only constraint: an action fraction used for a jet,
regulator, rare event or earlier use cannot serve twice.

For proposed original witness sets P_G, let d_p count sets containing p
and let r_p be its available fraction after other uses. Equal sharing
omega_(G,p)=r_p/d_p on P_G is feasible. On an event where
f_(0,p)>=ell_p on these witnesses it yields

    D_G>=tau_G:=u_0 sum_(p in P_G) r_p ell_p/d_p.        (Q11)

The price decreases with overlap. Geometric ancestry alone supplies no
positive ell_p. Alternatively a lower bound for the allocated SUM
suffices; individual bad witnesses are not required by the algebra.

## 4. Forward integration and the exact tilted-kernel bill

### 4.1 Kernel moments — PROVEN

For t>=1 put C_N(t)=e(1+4Nt)^(2N^2). Cover the 2N^2 real matrix
coordinates by cubes of side 1/(2Nt), choose group representatives in
occupied cubes, and translate Haar balls. A 1/t cap has mass at least
(1+4Nt)^(-2N^2). The trace bound makes h_M 1-Lipschitz in operator
norm, so the cap about a maximizer has exponent loss at most one.
Consequently A_t(M)=int exp(-t psi_M)dV>=1/C_N(t). For
0<=b<=1 and a_c>=0,

    int 1_(psi>=a_c) exp(b t psi) k_t(V;M)dV
                  <= C_N(t) exp[-(1-b)t a_c].           (Q12)

This follows by dividing the numerator exp(-(1-b)t psi) by A_t.
At b=0,a_c=0 the exact integral is one; use that sharper value.
The remaining gap price is

    q_c^(b)=(1-b)t a_c-log C_N(t).                     (Q13)

A gap used to integrate a regulator loses b of its exponential price;
JMBRB's full q_gap cannot also be spent unchanged.

For fixed M and b>=0, multiplying the original exponent gives exactly

    int exp[b t(1-h_M(V))] k_t(V;M)dV
                  =exp(b t) Z_((1-b)t)(M)/Z_t(M)
                  =exp(b t delta_M) A_((1-b)t)(M)/A_t(M). (Q14)

Negative parameters in Z and A are finite compact integrals too;
Q12 uses b<=1 for its useful bound. The factor exp(b t delta_M)
is a debit. Q4/Q9 can charge it to original action.

### 4.2 Joint finite-chain bound — PROVEN conditional theorem

Let dP=dU_0 product_(j<R) K_j(dU_(j+1)|U_j), with ALL outputs
integrated and t_j>=1. Supply deterministic demands Q7, fractions satisfying Q9
with z=0, Q10, and an event E on which all D_G>=tau_G. Choose distinct
required gap cells and thresholds a_c. For the displayed product bound
use a fixed schedule; past-adapted schedules are allowed if the same
deterministic per-step product bounds hold uniformly in the past.
Let C consist of cells with b_c>0 or a required positive-gap event.
Then

    int 1_E product_(required cells)1_(psi_c>=a_c)
               exp(-S_0+Ecal) dP
       <=exp(-sum_G tau_G)
           product_(c in C) C_N(t_c) exp[-(1-b_c)t_c a_c]. (Q15)

For a regulator cell without a required gap use a_c=0. This bound
need not be small. Q8/Q9 imply
-S_0+Ecal<=-sum_G D_G+sum_c b_c t_c psi_c.
Extract charges on E, drop that indicator, integrate the last output
cells using Q12 uniformly in the inputs, and repeat backward. Product
kernels justify simultaneous integration, without fine-field or core
independence. Unused outputs and finally probability Haar integrate
to one. This proves Q15 for arbitrary rough fields at finite depth
under the simultaneous capacities.

A smooth insertion bounded by B times another regulator can be included
by adding its demands. For original sources O_i=sum_p f_(i,p)s(U_(0,p)),
the real factor exp(-sum_i J_i O_i) is bounded by adding
|sum_i J_i f_(i,p)|/u_0 to Q9. Kernels and couplings stay fixed.

For a disjoint complete history partition sum_h I_h=1, a common
nonnegative F and pointwise costs w_h<=exp(s n),

    sum_h int I_h w_h F dP<=exp(s n) int F dP.           (Q16)

This follows pointwise before integration. Use it before dropping
history restrictions. History-dependent certificates instead require
their actual summed multiplicity or a common envelope. Q16 does not
justify summing independently optimized history suprema.

A fixed terminal field, noncreator reader, retained cut or all-cut
denominator is not a normalized output of this proof. Such factors
remain in the paired integral below. Q15 does not replace Q2 by a
forward probability law.

## 5. Six field derivatives and all four original sources — PROVEN calculus

Work on a fixed positive real sector, smooth through the indicated orders,
with dominated differentiation on compact subsets of the open domain.
Hard cuts in integrated coordinates are fixed. Cuts involving retained
parameters must first be summed or accompanied by their boundary terms;
this is FR's named input, not a consequence of positivity.

Write the completely opened numerator density w_y=w_0 exp(H_y), w_0>=0
fixed, and the actual positive denominator
D_y=int v_0 exp(H_y^-)d lambda^-. For a normalized inherited reference
D=int w; for Q2 it is the different Z_A. Supply bounds b_I^+ and b_I^-
for ordered derivatives of H and H^- on their respective complete
supports. Source derivatives already include r_i. For each ordered word
I, preserving order within every block, define

    M_empty^sign=I_empty^-=1,
    M_I^sign=sum_(pi partition I) product_(B in pi)b_B^sign,
    I_I^-=sum_(pi partition I) |pi|! product_(B in pi)M_B^-,
    C_I^(+,-)=sum_(S subset positions I) M_S^+ I_(I\S)^-,
    P_(6;[4])=sum_(a+b<=6) sum_(B subset {1,2,3,4})
                        C_(word(a,b,B))^(+,-)/(a! b!).  (Q17)

The empty partition occurs only for the empty word. Partitioning ordered
positions in exp(H) proves |D_I w|<=w M_I^+. Differentiating
D times D^-1=1, or expanding reciprocal derivatives, gives
D |D_I D^-1|<=I_I^- with coefficient |pi|!. Leibniz then proves
T(w/D)<=(w/D)P_(6;[4]). Score bounds are uniform over the direction
choices in that T. This is RM14–RM17 with separate numerator and
denominator scores. All sixteen source subsets, including the empty
subset, occur. There is no extra 4! in the four-label coefficient.

The b_I can be calculated from the actual opened factors. A read Wilson
plaquette with coefficient c contributes at field order r>=1 at most
|c|(4h_max)^r. A read kernel contributes at most
lambda_c^r[t_c+L_r(t_c)] to a log-density score, where
lambda_c=ell h_f+h_c, ell=5L-4, and L_r is RM14's log polynomial;
use only the field species it actually reads. Each earlier kernel has
its own term. A weighted original-source score contributes
sum_p r_i |f_(i,p)|s(U_(0,p)); its field derivatives have the same
plaquette-path bounds. Two pure source derivatives of H vanish for a
linear tilt; mixed field/source and reciprocal-normalizer derivatives
do not. Kernel source scores are zero. These rules give explicit finite
arrays, possibly growing with complete reader count and coupling.
They do not establish a uniform local bound.

Pure numerator-source jets display every label directly:

    partial_B w=(-1)^|B| product_(i in B) O_i w,
    sum_B r_B |partial_B w|<=w product_(i=1)^4(1+r_i|O_i|). (Q18)

If r_i|O_i|<=c_i S_0 and unused fractions epsilon_i>0 are available,
then (1+c_i S_0)exp(-epsilon_i S_0)<=1+c_i/(e epsilon_i), by
maximizing x exp(-epsilon_i x) for x>=0. Multiplication pays the four
numerator-source jets with total fraction sum epsilon_i. Denominator
jets remain in Q17. Add these fractions and any real-source changes
to Q9; no reserve is duplicated.

For coefficient c_I and insertions with T f_i<=a_i exp(Ecal_i),
ordered Leibniz and differentiation under the SAME integral give

    T[c_I int I_h product_i f_i w_y/D_y]
       <=(T c_I) product_i a_i M_(h,I)(y),
    M_(h,I)(y)=D_y^-1 int I_h w_y P_(6;[4])
                                      exp(sum_i Ecal_i). (Q19)

The regulators bound already differentiated factors and are not
differentiated. Their multiplicities add before Q8. Separately
integrating a regulator per core and multiplying the answers does
not prove Q19. Disjoint geometric cores can share original readers
and the interacting reference. An estimate with a different
denominator is not this estimate.

If D_G>=tau_G throughout the selected sector, extract the charge once:

    M_(h,I)(y)<=exp(-sum_G tau_G) C_(h,I)(y),
    C_(h,I)(y)=D_y^-1 int I_h w_y exp(sum_G D_G)
                         P_(6;[4]) exp(sum_i Ecal_i).  (Q20)

C is an uncharged integral divided by the UNCHANGED actual denominator.
It is not declared a probability or bounded by one. Q15 bounds a
special raw version when its factors and capacities match. It supplies
no local bound on C for every inherited fiber.

## 6. Histories, complete readers and explicit entropy

At fixed y, physical disjoint history indicators sum to one, as Q16
proves. The norm instead needs sum_h sup_y T(A_h). A pointwise
partition does not bound this by the supremum of its sum: arbitrarily
many smooth disjoint bumps can each have supremum one while their sum
has pointwise value at most one.

A sufficient envelope is the following. For each rooted geometric
skeleton Gamma, supply y-independent nonnegative masses m_(Gamma,h)
for its refinements such that

    sup_y T(A_(Gamma,h))<=m_(Gamma,h) exp(-nu n_Gamma),
    sum_h m_(Gamma,h)<=1.                              (Q21)

Summing proves the bound exp(-nu n_Gamma) for their sum of suprema.
MIXSMALL MS23 constructs an envelope for the filled family; an arbitrary
history cannot use it outside that scope. If instead sum_h m<=exp(s_h n),
subtract s_h from nu. This retains history entropy explicitly.

Here is one fully explicit possible spatial/type encoding. Suppose a
graph of degree Delta>=2 contains every skeleton reader, each skeleton
is a connected n-vertex set, its complete support has size <=c_H n,
and all non-source history refinements not paid by Q21 have at most
D choices per vertex in an injective encoding. This last hypothesis
must include times, mergers, absences, boundary/return types and reader
decorations; a bad/good label alone is insufficient.

Order graph neighbors. A deterministic spanning tree and its depth-first
walk of length 2(n-1) recover the visited set. Thus there are at most
Delta^(2(n-1)) connected sets through a fixed vertex. If the four fixed
labels are each absent or placed on one of n vertices, there are at most
(n+1)^4<=16^n choices; n+1<=2^n follows by induction for n>=1.
Multiple labels on one vertex are included. For roots IN the skeleton,
this proves

    A_type=16 Delta^2 D,
    r=A_type exp((mu+2)c_H-nu),
    Q_rough,core<=sum_(n>=1) r^n=r/(1-r),   r<1.        (Q22)

To identify this with the full rooted norm require that the skeleton
contain every possible output root. More generally, supply for each
output root x a fixed set R(x) of at most C_root skeleton vertices,
such that every term reading x has Gamma intersect R(x). Charging to
these vertices gives Q_rough<=C_root r/(1-r).
For instance complete skeletons with H_Gamma=Gamma have C_root=1
and c_H=1. In the general displayed sufficient test,

    nu >= (mu+2)c_H+log(16 Delta^2 D)+log(1+8 C_root)   (Q23)

gives Q_rough<=1/8. A further separately bounded small-atom budget
of 1/8 leaves total 1/4. The four-label factor is conservative and
can be omitted if those locations were already included in Q21;
jet sizes in Q17–Q19 must still be paid. nu is the residual after
ALL source, reference, jet, boundary, regulator and Q13 gap debits.

For a history with a long original reader, |H|<=c_H n or the root
charging premise may fail. The replacement is the actual full sum

    sup_x sum_(Gamma,h:x in H_(Gamma,h))
          exp((mu+2)|H_(Gamma,h)|) sup_y T(A_(Gamma,h))<=1/8. (Q24)

Deleting readers to use Q22 is forbidden. RM11–RM12 or JMBRB's
connected construction requires its common joint majorants and exact
factorization hypotheses. Counting does not create factorization on
an interacting reference. Uniform encoding, complete root assignment
and Q21 for the general family are OPEN here.

## 7. Exact failure points and the persistent-flux test

### 7.1 The local inherited comparison remains OPEN

The proposed assembly requires

    sup_y C_(h,I)(y)<=m_(Gamma,h) exp(c_ref n_Gamma),
    sum_h m_(Gamma,h)<=exp(s_h n_Gamma),               (Q25)

with complete readers, charge minus c_ref and all other costs meeting
Q23 (or Q24 directly), and simultaneous allocations for every selected
overlap family. C is exactly Q20 on D=int w or D=Z_A as actually
consumed. This remaining estimate contains substantial parts of the
original target; it is not claimed to be a strictly weaker solved
reduction. This is the named TC/matching interface still needed.

The whole-volume cap method yields only the insufficient bill

    log Q_core<=-tau m+d_j n_j,
    d_j=48u_j zeta^2+8N^2 log(1+4N/zeta)+16kappa u_j/L^4, (Q26)

where m is a localized original witness count, n_j the whole current
volume, 0<zeta<=1, and 4zeta is below all retained cuts. To rebuild it, bound the
last numerator kernels by exp(2t_j), integrate earlier normalized
outputs, and lower-bound Z_A on a product identity cap. Its 4n_j
links cost 8N^2 log(1+4N/zeta)n_j, its 6n_j plaquettes cost
48u_j zeta^2 n_j, and the last numerator/denominator kernels together
cost 16kappa u_j n_j/L^4. This is CHARGE C9/C13 on its actual real
all-cut denominator; original-source changes add their own debit.

The sufficient local-price inequality

    tau m>d_j n_j+required jet/support/type bills       (Q27)

fails as n_j/m grows with fixed local data. Q26 is an upper bound.
Failure of Q27 is a **technique failure**, not a lower bound on the true
Q_core or an obstruction to a local paired comparison. All field and
source derivatives still require Q17; omitting them does not repair
the extensive term.

### 7.2 Unrestricted depth fails this capacity certificate

Q6 has A_(P,p)>=5L^2 for every occurrence in the straight square.
On compatible sufficiently large tori choose a nested sequence of
plaquettes, each in the next coarser square. Choose one occurrence
at each step; larger finite tori avoid wrapping. The corresponding
entry of A_0^T...A_(R-1)^T is at least (5L^2)^R. With only
xi_R=a u_R at that final plaquette, Q9 requires at least

    a (u_R/u_0) (5L^2)^R<=1.                           (Q28)

For u_j=u>=1 this fails at large R for every a>0. It also fails if
u_0/u_R grows only polynomially in R. These are explicit coupling
classes for the test, not a derived running trajectory. Gap capacity
Q10 can fail too; Q28 already suffices.

This is failure of the conservative telescoping certificate to yield
a uniform depth estimate, **not** failure of the actual moment.
Its positive matrix entries overestimate transport; they are not lower
bounds on physical curvature. Sharper transport, weighted demands,
integration or extraction can change the conclusion.

### 7.3 Restricted obstruction: a regulator is not a gap price

The actual SU(2) field U_1(x)=diag(exp(i theta x_2),exp(-i theta x_2)),
theta=2pi/L^2, U_2=U_3=U_4=I on a side divisible by L^2 has a
direction-one mean zero. Its axial legs cancel and the straight-leg
average is L^-1 sum_(r=0)^(L-1) exp(2pi i r/L)=0. At this fine
input k_t is Haar, delta=1 and psi=0. For any positive integer
overlap multiplicity m,

    int exp[a m t(1-h_0(V))] k_t(V;0)dV=exp(a m t).    (Q29)

There is no C^m bound with C independent of unbounded t when a>0
for this **stand-alone conditional kernel moment**. This is a proved
restricted obstruction with an actual contour witness. It does not
refute Q25, which integrates original fields with their original
charges. RM23 pays polynomial jets in a divided seminorm; Q29 explains
why its integral is a separate cost. Larger overlap magnifies that
cost and supplies no new original reserve.

Likewise a future reweighting H gives K^H(E)=K(1_E H)/K(H).
For H=1_E with K(E)>0, K^H(E)=1. Thus
K^H(E)<=exp(-q_gap)<1 is false without a bound on that same H/K(H).
This tests a changed conditional law. In a raw numerator its mass
is still K(E) and can be spent once. It does not identify every
actual all-cut reference with this particular future tilt.

### 7.4 RENEW is retained and CHARGE's positive result survives

For the actual persistent-flux family g=diag(-1,-1,1,...),
U_1=g^(x_2+a), U_2=g^d, the paired means are W P with
P=diag(1/L,1/L,1,...). Expanding the trace gives
psi_M(V)=tr[(I-W*V)*P(I-W*V)]/(2N), so W is the unique maximizer.
The odd-block sign sum is one, giving another member of the same
rough family at output. At W,

    psi=0,    delta=2(1-1/L)/N

on directions 1 and 2. The kernel-energy regulator therefore has
a deterministic positive expense even on the zero-gap tower.
RENEW R13–R15 gives positive-measure persistence at every FIXED finite
horizon as couplings increase. That limit is not exchanged with an
infinite history sum here. Replacing every rough sector by a new gap
event would miss this actual branch.

An original tube of radius delta_0<1/4 has each 12 plaquette at
distance at least 2-4delta_0, and S_0>=c_delta u_0 n_0 with
c_delta=(2-4delta_0)^2/(2N). CHARGE's fractions
(1-L^-4)L^(-4l) sum to less than one and pay filled per-level
volumes n_l=n_0 L^(-4l). Under its explicit coupling/cut/depth
hypotheses C9–C11, the real all-cut ratio is at most
exp(-c_delta u_0 n_0/2). If further justified costs are exp(s n_0)
and B^R, the residual B^R exp[-lambda L^(4R)n_R], lambda>0,
is summable: successive ratios are
B exp[-lambda(L^4-1)L^(4R)n_R], tending to zero.
MS23 adds output/source jets with its output-weight condition and
common history envelope. These are alternative accounts of the same
reserve, not additional factors to multiply by Q20.

They do not show that arbitrary persistent local cores have filled
ancestors, bounded complete readers or Q21 envelopes. Q4–Q8 treat
their geometry without asserting these missing facts. The requested
extension of CHARGE remains OPEN.

## 8. No-Go Discipline Gate — partial construction, no exhaustion claim

**N1, routes.** ATTEMPTED: (i) squared ribbon propagation and one-use
capacities, Q4–Q16; (ii) exact kernel tilting, Q14/Q29; (iii) paired
normalization with jet/history envelopes, Q17–Q27. The first proves
finite sufficient bounds but fails Q28 uniformly; the second exposes
an unpaid conditional deficit; the third retains the local comparison.
These are three mechanisms, not five exhausted routes. No negative-claim
packet PASS is asserted. Interacting local references, sharper nonlinear
transport and extracted creation/accumulation envelopes remain live.
The no-commit instruction also precludes a landed no-go packet.

**N2, dependencies.** Let C be this transport-capacity certificate,
M the matched differentiated estimate and H the full history/root sum.
C alone does not establish M (Q26 retains the denominator bill); M
does not assert C and can use cancellations. M alone does not establish
H without envelopes/counts; H may be proved directly without the
proposed M factorization. C alone gives no H, and H asserts no
coefficientwise capacities. These are limitations of the displayed
implications, not proofs of logical independence or independent-wall
counts. A single stronger joint construction could supply M and H.

**N3, conditions.** The model, couplings, fixed real sectors, score and
domination bounds, simultaneous capacities, distinct gap ownership,
complete graph/encoding and common envelopes are explicit. Moving
selectors and source-dependent field transports are not silently
included in p=6. No background smallness, Gaussian coercivity or new
physical primitive is used in Q4–Q8.

**N4, residual matching.** RM23 is a divided seminorm; Q29 tests its
conditional integral. These are compatible. CHARGE C13 tests the
same global-cap majorant as Q26. RENEW R-TUBE tests forward uniform
curvature return, not charged normalized moments. MIXSMALL MS23
supplies the filled envelope, not Q21 for arbitrary cores. None of
these witnesses is used outside that scope.

**N5, resolutions.** Q4/Q29 concern actual link readers; Q5/Q6 are
plaquette inequalities; Q8–Q10 cover finite overlapping families;
Q28 concerns coefficients on nested ancestry, not a physical eigenmode;
Q22 is conditional full-lattice/root arithmetic. Numerics are NOT RUN.
No all-history divergence, continuum or spectral conclusion follows.

**N6, partial closure.** Changing the reference, grouping regulators
before estimates, weighting readers and extracting returned coefficients
are mathematical constructions, requiring no new axiom. Coordinator
inputs are not automatically promoted beyond their proved scopes.

**N7, strongest counter-route.** A local interacting reference could
cancel Q26's exterior volume before absolute values. Integrate coherent
sectors with their original masses, propagate only returned residuals
in a sharper action norm, and bound the creation envelope together
with all labelled jets. This could bypass Q28 and prove Q24.
CHARGE C25/C25a and REFMATCH RM7–RM13 leave this mechanism open;
its local estimate and fixed-terminal accumulation must be constructed.
The present calculation does not exclude it.

**N8, echo.** Complete reads of the six notes retain the earlier
corrections: old mass is not renewed, reference support must match,
original source tails remain, and sum-of-suprema needs a common
envelope. Search failures and scope limits are in the log. No
exhaustive novelty or route-exhaustion claim is made.

## 9. Deliverable and next decision

The constructive addition is Q4–Q8's arbitrary-field transport and
Q15's joint finite-chain certificate, with derivative, overlap and
entropy interfaces. Q27/Q28 are failing sufficient inequalities of
this method. Q29 obstructs only its specified unpaid conditional
kernel bound. The inherited-law Q25/Q24 target remains OPEN.

**ARGUED next work:** on one genuinely local nonfilled core construct
the paired integral cancelling the exterior reference, then evaluate
Q19 with a retained field derivative and all four original-source
labels. Use Q4 on its short-mean part where Q9/Q10 are feasible.
For deeper coherent continuation replace conservative Q6 transport
by a proved integrated/extracted bound, retaining all complementary
histories. This new input would reopen the failed uniform-capacity
route; another global-cap estimate would not.

The numerical guard failed at `nice`; no numerical result is offered.
Written proofs and fresh hostile review, with exact final source
identities in the log, provide the evidence at their stated scopes.
