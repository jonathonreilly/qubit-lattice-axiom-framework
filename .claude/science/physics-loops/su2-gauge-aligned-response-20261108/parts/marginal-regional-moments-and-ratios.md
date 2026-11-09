# Regional radial moments and buffered ratios for the seven-edge marginal

Pure-proof author draft, 2026-11-09; independent mathematical check pending.
Source HEAD: `fbdfb3c1b8852e5de302fab6f0f7cfc70ba04cac`. This proves a
conditional implication from the pinned compact-coercivity and reader-template
suppliers to estimates for the actual deleted-kernel law. It confers no audit
or retained status. All mathematical inputs and read scopes are in §8.

## 1. Exact law, coordinates and uniformity

Fix odd L>=3, kappa>0, m>=3, beta=u>=1 and both kernel strengths kappa*u.
The fine torus has side L^2 m. Let J be the seven independent positive
terminal edges forming the boundaries of two distinct elementary terminal
plaquettes sharing one edge, and O=E2\J. All surviving terminal outputs are
I. Use the centered terminal-block forest of the compact-coercivity supplier,
with arbitrary internal spanning trees. Write a for all fine non-tree and
intermediate compact coordinates. Tree links are I. The density, up to a
constant independent of a, is precisely

    rho_J(a) = q_u(a0,T=I) product_(e in E1) K0,e(a1,e|a0)
                              product_(c in O) K1,c(I|a1).       (1)

Each K=exp(kappa*u <v,M>)/Z(kappa*u |M|). Integrating the seven terminal
outputs against their probability Haar measures yields one for each deleted
kernel. In particular neither its numerator nor its radial normalizer remains.
Every K0 normalizer and every O terminal normalizer DOES remain. We never
compare probabilities under (1) with an all-terminal law.

Each terminal cell x owns the fine non-tree and intermediate links whose
tails lie in x. There are M0=3L^8+1+4L^4 owned coordinates per cell: a fine
block has 4L^8 fine tails, L^8-1 internal tree edges, and 4L^4 intermediate
tails. Put b_e=1-w(a_e)=|a_e-I|^2/2 in [0,2], T_x=sum_(e owned by x)b_e,
and T_A=sum_(x in A)T_x. Let Q_A denote the owned coordinate set, to avoid
confusing it with the deleted terminal set J.

Select P_A to contain every fine plaquette whose full syntactic reduced
hidden readers meet Q_A. Select C_A^J to contain every SURVIVING kernel
with such a reader. Its readers include all mean inputs, the hidden output
for K0, and every reader of its normalizer, even when the normalizer happens
to be constant under this conditioning. Tree variables are set to I after
making this full selection; retaining extra syntactically selected constant
factors is harmless and is our convention. Factors having no reduced reader
in Q_A cancel between conditional numerator and denominator. The supplied
actual path reader templates put all remaining exterior readers in
B_A=N_1(A)\A, for terminal-cell periodic l-infinity distance. Deleting
kernels only removes reader sets and cannot enlarge this radius. The forest
substitution reduces readers; original-variable pullback uses only internal
trees of endpoint blocks. We condition on quotient exterior coordinates,
not on original individual links.

For every exterior z, define

    E_A^J(a,z) = sum_(p in P_A)(1-w(U_p))
            + kappa sum_(c in C_A^J)(r_c-<v_c,M_c>),
    r_c=|M_c| in [0,1],  H(t)=exp(t)/Z(t),
    W_A^J(a,z) = exp(-u E_A^J(a,z))
                              product_(c in C_A^J) H(kappa*u*r_c).  (2)

The regional conditional is W_A^J da_QA / D_A^J(z), where D_A^J is its
integral against product probability Haar. Equation (2) is exact: each
kernel is exp[-kappa*u(r_c-<v_c,M_c>)]H(kappa*u*r_c), and the constant
exp(u) per selected Wilson factor cancels. All factors in (2) are strictly
positive. Zero means create no exception.

By the pinned two-plaquette compact theorem,

    E_J >= c_J sum_e b_e,   c_J=1/C(L,kappa)>0,                (3)

for every compact configuration, with C as in its equation (12). This
constant is uniform in volume, pair position/orientation and allowed trees.
The all-terminal energy appearing internally in that supplier is only a
deterministic auxiliary function; (3) is used directly for E_J here.

## 2. Whole-factor regional energy estimates

We spell out the hypotheses needed to apply the radial-cap mechanism to
(1). For a unitary word of length ell, telescoping and Cauchy--Schwarz give

    1-w(A1...Aell) <= ell sum_j b_(Aj).                    (4)

Inverse occurrences have the same b, multiplicities are counted, and fixed
identity factors cost zero. For an average M of paths of length at most
p=5L, with unitary output v,

    0 <= |M|-<v,M> <= average_P [1-w(v^*P)],
    0 <= 1-|M| <= average_P [1-w(P)].                     (5)

Use (4) on the right sides. The inherited templates bound the number of
plaquette incidences of a link by six and output-inclusive kernel incidences
by nine. Thus constants valid for every selected subfamily are

    K_E=24+9*kappa*(p+1)^2,   K_r=9*kappa*p^2,
    sum selected energy factors <= K_E sum reader coordinates b_e,
    kappa sum selected kernels (1-r_c) <= K_r sum readers b_e. (6)

The conservative squares account for repeated occurrences within words.
These estimates count only present factors; deletion cannot increase either
incidence. They also hold for omitted subfamilies in the argument below.
Their uniformity concerns reduced compact coordinates, so long internal tree
paths do not increase these reduced word lengths.

Given a on Q_A and arbitrary z, set all coordinates outside A union B_A to
I, leaving A and B_A unchanged, and call the resulting full field a-tilde.
Every selected factor is unchanged. Every omitted surviving factor reads no
coordinate in Q_A; any nonidentity reader it has is in B_A. Its total energy
is at most K_E T_BA by (6). Apply (3) to a-tilde and subtract just these
omitted nonnegative energy factors. Consequently

    E_A^J(a,z) >= c_J T_A - K_E T_BA(z).                  (7)

Also directly from (6),

    E_A^J <= K_E(T_A+T_BA),
    kappa sum_(c in C_A^J)(1-r_c) <= K_r(T_A+T_BA).       (8)

This works for disconnected or wrapped A and the whole torus; empty collars
cause no exception. It proves the localized lower bound without needing the
coercivity recovery detours to lie inside A. Their bounded template constants
have already supplied the global c_J. No deleted gamma_1 is inserted into
E_A^J, no normalizer is removed, and no smallness of z is assumed.

## 3. Uniform radial-profile box and exact cancellation

Allow an arbitrary cell profile 0<=theta_x<=t_*=c_J/2 and multiply (1) by
exp[u sum_x theta_x T_x]. On further conditioning to A, profile terms outside
A are constants; the conditional energy is

    E_A^(J,theta)=E_A^J-sum_(x in A)theta_x T_x,
    E_A^(J,theta)>=(c_J/2)T_A-K_E T_BA,
    E_A^(J,theta)<=E_A^J.                                (9)

The tilted energy need not be nonnegative. Only (9) is used.

For t>=0, differentiating the one-link Haar normalizer gives

    (log H)'(t)=1-E_t w in [0,1].

The lower bound E_t w>=0 follows by pairing the symmetric Haar values w
and -w, since w sinh(tw)>=0; E_t w<=1 is pointwise. Hence for 0<=r<=1,

    H(kappa*u) exp[-kappa*u(1-r)] <= H(kappa*u*r)
                                           <= H(kappa*u). (10)

Take fixed 0<d<=1, n=|Q_A|=M0|A|, and k=|C_A^J|, the ACTUAL surviving
selected kernel count. The product cap |a_e-I|<=d/sqrt(u) has Haar mass at
least (c_cap*d^3)^n u^(-3n/2), with c_cap>0 independent of all parameters.
This follows directly from Haar radial density (2/pi)sin^2 alpha d alpha
and chord 2 sin(alpha/2) on SU(2); on a fixed small angular interval these
are bounded below by constant multiples of alpha^2 and alpha respectively.
On the cap T_A<=nd^2/(2u). Equations (8)--(10) give the exact denominator
bound, uniformly over the entire theta box,

    D_A^(J,theta) >= H(kappa*u)^k
        exp[-(K_E+K_r)u T_BA -(K_E+K_r)nd^2/2]
        (c_cap*d^3)^n u^(-3n/2).                        (11)

For lambda_*=c_J/4 the unnormalized exponential-moment numerator is at most

    H(kappa*u)^k exp(K_E u T_BA)
        product_(e in Q_A) integral exp[-(c_J*u/4)b(Q)]dQ
    <= H(kappa*u)^k exp(K_E u T_BA) K_H^n u^(-3n/2).    (12)

To verify finite K_H directly, write b=1-cos alpha, use
1-cos alpha>=2alpha^2/pi^2 and sin^2 alpha<=alpha^2 on [0,pi], and
extend the radial Gaussian integral to infinity. This works for every
c_J>0 and u>=1. Dividing (12) by (11) cancels H(kappa*u)^k and
u^(-3n/2) exactly. No asymptotic estimate of H, lower bound on individual
r_c, or undeleted kernel count is used. Thus

    log E_(J,theta)[exp(lambda_* u T_A)|z]
                                <= A_*|A|+B_*u T_BA,   (13)
    B_*=2K_E+K_r,
    A_*=max(0, M0[log(K_H/(c_cap*d^3))+(K_E+K_r)d^2/2]).

Selected normalizers that are conditionally constant appear in both (11)
and (12), with their contribution to the same k. This is why they introduce
no unmatched powers. The statement also holds for A empty with both sides
zero, using empty products.

## 4. Same-law tower, interior moments and tilt integration

Write a_*=A_*/lambda_*, b_*=max(1,B_*/lambda_*) and q=b_*/(1+b_*) in
(0,1). Jensen applied to (13) yields

    E_(J,theta)[T_A|z] <= a_*|A|/u+b_*T_BA(z).           (14)

Fix a region Omega, an arbitrary quotient exterior z_Omega, and one fixed
profile theta. The conditional of this tilted regional measure on a smaller
A subset Omega is exactly (2),(9): unselected surviving factors and all
outside profile terms cancel. In particular this is the SAME deleted law
and the SAME profile, not a change of law at each tower step.

For a cell x with N_s(x) subset Omega, let m_r=E T_Nr(x), 0<=r<=s. For
r<s the collar is N_(r+1)(x)\N_r(x); applying (14) then taking expectations
under the fixed regional measure gives

    m_r <= a_*|N_r(x)|/u+b_*(m_(r+1)-m_r),
    m_r <= q m_(r+1)+a_*|N_r(x)|/((1+b_*)u).           (15)

Since |N_r(x)|<=(2r+1)^4 and m_s<=2M0(2s+1)^4,

    E_(Omega,J,theta) T_x <= C_*/u+C_*(2s+1)^4 q^s,     (16)
    C_*=max(2M0, [a_*/(1+b_*)]sum_(r>=0)q^r(2r+1)^4).

The series converges. At s=0 this follows from the elementary compact bound;
when balls saturate the torus, the collar is empty and (15) still holds.
On the whole torus arbitrarily large s are allowed, giving E_theta T_x<=C_*/u.
All constants are independent of theta, Omega, its arbitrary exterior and the
placement/orientation of J and allowed forest trees. No independence of
collar variables or translation invariance has been used.

For A subset Omega and radii s_x with N_sx(x) subset Omega, define under the
UNTILTED regional law

    f(t)=log E_(Omega,J) exp(tu T_A),  0<=t<=t_*.

Compact integration and bounded integrands give differentiability. Its exact
derivative is u sum_(x in A) E_(Omega,J,theta=t 1_A)T_x. Apply (16) along
this entire allowed profile path and integrate from f(0)=0:

    log E_(Omega,J) exp(tu T_A)
      <= t C_* |A|+t C_*u sum_(x in A)(2s_x+1)^4 q^s_x. (17)

Overlapping balls create no issue because this is a sum of expectations.
On the full torus the second term is absent. Integration from a nonzero
background profile likewise works as long as the entire profile path remains
inside the box. This proves the radial-profile moment transfer.

For completeness, on the whole torus every coordinate e and p>0 satisfy,
for any 0<t<=t_*,

    P(|a_e-I|>=h) <= min(1,exp(C_*t-tu h^2/2)), 0<=h<=2,
    E|a_e-I|^p <= exp(C_*t) Gamma(1+p/2)(2/(tu))^(p/2). (18)

The second statement follows by integrating p h^(p-1) times the first tail
bound, extending to infinity. It is a radial statement, not a covariance or
signed-coordinate centering statement.

## 5. Buffered rough-core rarity under every exterior

Fix 0<delta<=2 and a deterministic nonempty cell set S. Define B_S to be
the event that EVERY cell of S owns at least one retained hidden coordinate
with |a_e-I|>=delta. This is the entire-core-rough event; it does not assert
that S is a maximal rough component. Distinct cells have distinct witnesses.
Choose a finite integer h=h(L,kappa,delta) such that

    C_*(2h+1)^4 q^h <= delta^2/4,                       (19)

possible since q<1, and let R=N_h(S). For arbitrary quotient exterior z to
R, use (17) with Omega=R, A=S, s_x=h and t=t_*. On B_S,
T_S>=delta^2|S|/2. Markov's inequality gives, in the SAME actual regional
law (2),

    p_S(z):=P_(R,J)(B_S|z)
       <= min(1,exp[t_*C_*|S|-t_*u delta^2|S|/4]).     (20)

For u>=max(1,8C_*/delta^2), consequently

    p_S(z)<=eta(u)^|S|,   eta(u)=exp(-t_*u delta^2/8)<1. (21)

Uniformity includes every compact exterior, disconnected S, wrapped sets and
R equal to the torus. The buffer is fixed once delta,L,kappa are fixed.
If delta depends on u, the proof instead requires the stated (19) and (20)
with its corresponding buffer; a uniform fixed buffer is not asserted then.

## 6. Exact normalized ratio and general original sources

Keep R,S and their fixed indicator B_S as above. For surviving terminal
outputs V_O near I, let W_R^J(a_R,z;V_O) be the product of selected whole
factors in (1), with every selected normalizer present. It differs from (2)
only by constants that cancel in every ratio below. Let h_orb be all the
root-fixed orbit variables of the forest disintegration, with product
probability Haar dh_orb. Given bounded real original hidden-chain sources
F,G independent of terminal V, define

    Z_R(V;s,t) = integral da_R dh_orb W_R^J(a_R,z;V)
                      exp[sF(U(a_R,z,h_orb))+tG(U(a_R,z,h_orb))],
    Z_bad = same integral with indicator 1_(B_S),
    Z_good = same integral with indicator 1_(B_S^c).     (22)

The fixed exterior is z in quotient coordinates, and original sources can
read any reconstructed hidden variable. These definitions explicitly retain
all orbit variables, including those appearing only in sources. At s=t=0
the orbit integral is one, recovering (2). No separate source projection is
performed. Equivalently, integrating the orbit once yields
A_st(a)=integral exp(sF+tG)dh_orb, for which

    partial_s partial_t log A_st(a)=Cov_(h_orb|a,s,t)(F,G),
    partial_s partial_t log Z_R
      = E_(a,s,t) Cov_(h_orb|a,s,t)(F,G)
           + Cov_(a,s,t)(E[F|a],E[G|a]).                (23)

This conditional orbit covariance is not dropped. The same formula holds
with the good-event restriction. It includes gauge-variant original sources;
no invariant-source premise is required.

Let p(V;s,t)=Z_bad/Z_R. Positivity and the identity cap imply Z_good>0:
there is an open product cap making all links owned by S have chord<delta,
and every weight in (22) is positive. Exactly,

    Z_R=Z_bad+Z_good,
    z_S=Z_bad/Z_good=p/(1-p),
    L_S=log(Z_R/Z_good)=-log(1-p).                      (24)

Here good is the complement of the event that every cell of S is rough.
It is NOT the all-good chart; neither R\S nor all of S are constrained to
be small. Common exterior factors cancel even if they depend on V. At the
zero-source identity point, (21) and eta(u)<=1/2 imply

    0<=z_S<=2eta(u)^|S|,  0<=L_S<=2eta(u)^|S|.          (25)

A sufficient u range for everything in (25) and the jet bound below is

    u>=max(1,8C_*/delta^2,8 log(2)/(t_*delta^2)).        (26)

## 7. Full two-source/two-distinct-terminal jet

Take distinct terminal links c,d and tangent vectors v_c,v_d at I. Use
separate smooth local parameters V_c(epsilon_c),V_d(epsilon_d) with those
tangents. Each appears in at most its own selected terminal factor. Labels
1,2,3,4 denote partial_s, partial_t, D_c, D_d. Their log-weight insertions
at s=t=0,V=I in the joint (a_R,h_orb) measure are respectively

    X1=F, X2=G,
    X3=A_c=kappa*u <v_c,M1,c> if c in O and K1,c selected,
              =0 otherwise,
    X4=A_d=kappa*u <v_d,M1,d> if d in O and K1,d selected,
              =0 otherwise.                            (27)

For a deleted link, (22) has no V_c dependence at all. For an unselected
surviving terminal link, its outside factor cancels from (24). Both scores
are therefore exactly zero, not merely bounded. Normalizers are independent
of their terminal output, explaining their absence from (27) but never their
removal from the measure. Hidden K0 factors remain and affect expectations.
Each mixed derivative of log weight involving two DISTINCT labels is zero:
F,G have no explicit V dependence; different outputs occur in different
kernels; and s,t enter linearly. Pure repeated-output derivatives would not
have this property and are not covered.

For every nonempty subset I of these labels, k=|I|, differentiation of the
normalized probability gives the exact mixed-cumulant identity

    D_I p = Cum(1_(B_S),(X_i)_(i in I)).                 (28)

One way to verify every term is to adjoin a new scalar zeta to the exponent
as zeta 1_(B_S). Then p=partial_zeta log Z|_(zeta=0); differentiate once
in each label. As all mixed distinct-label derivatives of the log weight
vanish, only the ordinary joint cumulant survives. Nonlinear dependence on
a single epsilon has degree >=2 and cannot enter a derivative using that
label only once. Compactness and bounded sources justify all derivatives.

For explicit partition accounting, with Y0=1_(B_S), Y_i=X_i, the right side
of (28) is

    sum_(pi partition of {0} union I)
       (-1)^(|pi|-1)(|pi|-1)! product_(B in pi) E product_(j in B)Y_j. (29)

Set ell=(||F||_infinity,||G||_infinity,kappa*u|v_c|,kappa*u|v_d|).
The unique block containing label 0 has expectation bounded in absolute
value by p times the product of its other ell factors. All other blocks
are bounded by their corresponding ell products. Thus at the base point

    |D_I p|<=b_k p product_(i in I)ell_i,
    b_k=sum_(j=1)^(k+1) S(k+1,j)(j-1)!,
    (b1,b2,b3,b4)=(2,6,26,150).                         (30)

Here S(n,j) are Stirling numbers of the second kind. This argument retains
all conditional covariance and higher connected terms; their absolute values
are bounded only after the full partition formula is written.

For g(p)=-log(1-p), g^(j)(p)=(j-1)!/(1-p)^j. The exact distinct-label
chain rule is

    D_1234 L_S = sum_(pi partition of {1,2,3,4})
          (|pi|-1)!/(1-p)^|pi| product_(B in pi)D_B p.  (31)

For p<=1/2, use (30), p^|pi|<=p, and (21). This proves

    |D_c D_d partial_s partial_t L_S|
       <= C4 kappa^2 u^2 |v_c||v_d| ||F||_infinity||G||_infinity
                                                       eta(u)^|S|, (32)
    C4=sum_(pi partition of {1,2,3,4})
                (|pi|-1)! 2^|pi| product_(B in pi)b_|B| = 5404.

For an explicit arithmetic check by partition sizes, the contributions to
C4 are 300 from (4), 1264 from (3,1) and (2,2), 2304 from (2,1,1), and
1536 from (1,1,1,1), respectively, summing to 5404.

Equivalently the left side of (32) is the absolute difference of the full
fourth cumulant of F,G,A_c,A_d under the full regional measure and that under
its B_S^c restriction. This follows by differentiating the two logarithms in
(24) separately. It is the full normalized response difference, not the
fourth derivative of an unnormalized rare-event weight. If either score is
zero, the actual mixed derivative vanishes identically. No nonidentity
rarity estimate is assumed: all differentiation identities hold locally by
positive finite integration, and the estimate is evaluated only at V=I,
s=t=0.

## 8. Source identities, author checks and limits

Mathematical sources, relative to this pack, read at the stated HEAD:

| Source and actual read scope | SHA-256 |
|---|---|
| `parts/two-plaquette-compact-coercivity.md`, full §§1--5 | `b77fdb722d19c96594cddded301d9dd019c412b875721f5c28d1461415bb246e` |
| `parts/arbitrary-boundary-interior-moments.md`, full §§1--7.3 | `c58acdf2d0391847c631a358fcad2bd280e8f563c19947f976118272a4426d11` |
| `parts/buffered-core-conditional-ratio.md`, full §§1--4 | `204f48f463fb69eebb6b309996c663698dadd5969728f2a311176e21b53b42c7` |
| `parts/compact-forest-exchange.md`, §§1--5 (lines 1--205), not later sections | `b0d3a76a94a8cd43de186b1c93deb38327ea2b29aa2b1bbc16e1caa2e22ecef2` |
| `sources/marginal-regional-chart-prior-art-20261109.md`, full | `0f2365732c9c48e923a16bf0a78fb7821776f3e77fe9102c0812573c0f6a7c76` |

The prior-art source and logs remain unchanged. Its search was reused; no
new external theorem is imported. The radial cap/tower method is the pinned
repository supplier's construction, whose reference-cap antecedents credit
Bałaban/Dimock; no novelty claim is made. The new-law match is explicit in
(1)--(12), and the buffered/cumulant mechanism is rederived for that law in
(19)--(32). Source SHA identities establish provenance, not correctness.
The two-plaquette coercivity and actual reader/incidence templates are
inherited premises; this bounded author assignment does not independently
reprove their upstream geometry. The algebraic/Haar/tower/cumulant steps are
written out here for a fresh decisive check.

Current checkpoint: the proposed transfer closes at author-proof level with
c_J, the actual selected surviving k, arbitrary quotient exterior, the entire
radial-profile box, and the precise complementary rough-core ratio. Constants
are uniform in volume, region, exterior, pair placement/orientation and allowed
trees to the extent supplied by (3) and the reader-template bounds. Buffer
width and the final u threshold also depend on delta. No spatial connected-four
response decay, immediate-neighbor conditional mixing, nonidentity compact
extension, all-good-chart comparison, overlapping-buffer composition, or
exterior-averaged derivative bound has been proved. No source prompts, input
notes, logs, Git state, audit status or physical premises were changed; only
this deliverable was written. Parent full read and fresh checking remain due.
