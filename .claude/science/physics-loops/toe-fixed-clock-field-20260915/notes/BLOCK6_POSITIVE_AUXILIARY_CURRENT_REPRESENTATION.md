# A positive auxiliary field with both clock defect sectors

Personal derivation, 2026-09-15. Conditional on the supplied finite-clock
Villain law, this is an exact finite-volume representation. It does not
establish its infinite-volume state, a Gaussian scaling limit, or a native
selection of the law. General lattice Poisson duality is already used on
main; the delta here is its resolved Gaussian/current representation,
including the full physical source and an explicit filling-change check.

## 1. Finite free complex and normalization

Use the contractible free cubic complex with D=d1, B=d2, and C=d3.
Counting inner products and positive cell orientations are understood.
Let P project onto im D and Q=I-P=B*G B, where G=(BB*)^-1 on
V=ran B=ker C. Only this subspace is integrated below. Set

    b=2pi sqrt(beta), g=N/sqrt(beta), bg=2pi N,
    0<c<1/16, A0=G-cI on V, T=(I-c BB*)^-1 on V,
    R=I+c B*T B=(I-c B*B)^-1 on face fields.

The free cubic incidence has squared norm at most16, so A0 is positive.
The choices c=1/32 and fixed finite N,beta will be used in the checks.
The identities used repeatedly are

    A0 T=G,
    B*T A0 T B=R-P,
    RP=P, RQ=QR, R>=I.                               (1)

Magnetic charges range over the lattice L_m=B Z^faces in V. This avoids
silently replacing an integer image lattice by a real kernel or introducing
torus harmonic sectors. Define

    Theta_c(eta)=sum_(q in L_m)
          exp[-b^2 c ||q||^2/2] exp[i b q.eta].

Finite-dimensional Poisson summation on the full-rank lattice L_m in V
proves Theta_c(eta)>0 for real eta. All its derivatives are legitimate
finite-dimensional Gaussian theta series. Put

    mu(deta)=Z_m^-1 Theta_c(eta) gamma_A0(deta),
    Z_m=sum_q exp[-b^2 q.Gq/2].                       (2)

This is a positive probability, since Gaussian integration of Theta_c
gives Z_m. No assertion that its potential is uniformly convex is needed
for the representation.

## 2. Haar source identity, derived on the same finite complex

The continuous Haar link/image flux decomposes as

    X_H=P W-b B*G q,

where W is a standard face Gaussian, q has weight proportional to
exp[-b^2 q.Gq/2], and the two are independent. Free contractibility and
constant fiber multiplicity justify the image quotient. Consequently

    chi_H(v)=exp[-v.Pv/2]
       Z_m^-1 sum_q exp[-b^2 q.Gq/2-i b q.GBv].       (3)

For real face v, Gaussian integration and (1) give the alternative identity

    chi_H(v)=exp[-v.Rv/2]
                E_mu exp[-eta.TBv].                 (4)

Indeed the integrand's q term has Gaussian expectation

    exp[ (TBv).A0(TBv)/2
          -i b q.A0 TBv-b^2 q.A0q/2].

The cross term is -i b q.GBv; cI+A0=G; and
R-B*T A0 T B=P. This proves (4), rather than presuming a random
Gaussian decomposition of X_H. Its right side uses a real moment
generating function. It is not a convolution of two real independent
random fields with covariances of opposite sign.

## 3. Impose the actual clock through conserved currents

Let J={j in Z^edges:d0*j=0}. For each j choose any integer face filling
S_j with D*S_j=j. Fourier expansion of the link clock comb, followed by
gauge integration, gives for the original lifted clock flux X

    chi_clock(h)=sum_(j in J) chi_H(h+g S_j)
                    /sum_(j in J) chi_H(g S_j).      (5)

The same identity follows by Poisson summation on the clock flux lattice
(b/N)(D Z^edges+N Z^faces). Gauge multiplicities are constant and cancel.
For each fixed finite complex these sums converge absolutely: the real
Haar representation (3) bounds the q sum by Z_m, while the electric
Gaussian factor is coercive in j, including the fixed linear source.
The expression is independent of S_j: an integer difference U with
D*U=0 has U.X_H in b Z, so exp[i g U.X_H]=1.

Substitute (4) in (5). Each term is positive for real h. Tonelli now
produces a positive joint probability on (eta,j):

    nu(deta,j) proportional gamma_A0(deta) Theta_c(eta)
       exp[-g^2 S_j.R S_j/2-g eta.TB S_j].           (6)

Set Y=-B*T eta-g R S_j. The full source identity is

    chi_clock(h)=exp[-h.Rh/2] E_nu exp[h.Y].         (7)

There are no discarded defect species and no interpretation of a complex
pair weight as a probability. Finiteness of (6) follows from (5), or from
the change of variables in the next section. The same calculations with
real linear sources give all required exponential moments. Reflection
of both eta and j centers Y. In particular,

    Cov(X)=R-Cov(Y),
    cumulant_(2k)(X)=(-1)^k cumulant_(2k)(Y), k>=2,   (8)

with the tensor identity interpreted by polarization. Odd cumulants
vanish. These are relations, not bounds that make the higher cumulants
small. They are consistent with the general positive dual-lattice formula
already present in the repository.

## 4. Translate the Gaussian instead of paying a filling-area factor

In (6) set xi=eta+g G B S_j. Completing the square, using (1), gives

    nu'(dxi,j) proportional gamma_A0(dxi)
        exp[-g^2 ||P S_j||^2/2]
        Theta_c(xi-g G B S_j),                      (9)

and the source variable simplifies to

    Y=-B*T xi-g P S_j.                              (10)

The quadratic filling norm in (6) has disappeared from the activity in
(9); the remaining electric energy depends only on the current. Equation
(9) is positive and exact, not a most-probable-point replacement.

It is also pointwise independent of the integer filling. If U is an
integer face field with D*U=0 and q=B n is an allowed magnetic charge,

    q.GB U=n.Q U=n.U in Z.

Thus Theta_c(xi-gGB(S_j+U))=Theta_c(xi-gGB S_j), because bg=2pi N.
Also P(S_j+U)=P S_j. Consequently the right sides of both (9) and
(10) need no preferred integer filling, although a filling can be used
to calculate them. This exact periodicity is lost if N is treated as a
generic real parameter or if the current lattice is replaced by its span.

One can describe the carrier geometrically. Put

    U=B*xi+g P S_j.

Then Y=-R U. Its carrier is im B*+g P Z^faces, equivalently
im B*+g Z^faces, with Lebesgue measure on each coexact fiber and
counting measure on the discrete exact quotient. This is the exchanged
electric/magnetic support; no claim of matched free/relative boundary
self-duality is made merely from that description.

In a local magnetic filling representation, the phase in Theta_c is

    exp[i b n.B*xi-i bg n.Q S_j]
      =exp[i b n.(B*xi+g P S_j)].                   (11)

The integer phase bg n.S_j is the reason for the equality. Thus the
usual real magnetic extension can be evaluated at U, subject to its own
proved extension and locality bounds. Its argument contains P S_j;
the current/field coupling has not become a local independent product.

## 5. Identify the resulting field: a smoothed dual clock lattice

The positive representation should not be mistaken for an easier theory
merely because its variables look different. It can be identified exactly.
The original X is the centered unit-precision Gaussian on the full-rank
lattice Lambda=(b/N)(D Z^edges+N Z^faces). Let Z_d be the centered
unit-precision Gaussian on Lambda_d=2pi Lambda*. Ordinary Poisson
summation, with every finite normalization canceled, gives

    chi_X(h)=exp[-||h||^2/2] E exp[-h.Z_d].          (12)

Compare (12) with (7). Uniqueness of finite-dimensional moment generating
functions gives

    Y has law -Z_d+W, W independent Gaussian(R-I).  (13)

Here R-I is positive semidefinite, and degenerate Gaussian directions
are permitted. This is an actual real independent-noise identity for Y;
it does not turn (7) into a real independent decomposition of X.

For clarity, integer character annihilation gives

    Lambda_d=(1/sqrt(beta)) L_N,
    L_N={n in Z^faces:D*n in N Z^edges}
       =N Z^faces+B* Z^three-cells.                 (14)

For the last equality, write D*n=N j. Conservation makes j an integer
cycle; free integral homology supplies S with D*S=j. Then n-N S is
an integer two-cycle and hence B* of an integer three-chain. The reverse
inclusion is immediate. The factor is 1/sqrt(beta), not g. Under Hodge
duality this is the exchanged clock coupling with the matched relative
boundary structure, not an automatic equality to the original free-box
ensemble. No boundary-state independence is assumed.

Put K=R^-1=I-cB*B. Equations (10) and (13) identify U in law as

    U=K(Z_d+W), W independent Gaussian(R-I),        (15)

changing the harmless sign of W if needed. Centered lattice Gaussian
domination gives Cov(Z_d)<=I, so this coupling obeys

    Cov(U)<=K,
    E |h.(U-Z_d)|^2<=h.(I-K)h=c||Bh||^2.           (16)

Indeed the two independent errors contribute at most
(I-K)^2+K(R-I)K=I-K. For smooth four-dimensional tests
h_a(p)=a^2 f_p(a x), ||B h_a||^2=O(a^2), away from the free boundary.
Thus U and this specific dual flux have the same possible limiting
finite source laws. Fixed c,N,beta suffice. The representation closes
back onto the dual clock problem; it has not removed the need for its
infrared analysis. This is a useful exact route comparison rather than
a new proof of Gaussianity.

## 6. What the representation changes and what it leaves

The real-tilt form (6) is a candidate entry to an auxiliary Gaussian
expansion. The translated form (9) avoids its explicit large real tilt,
and retains positivity and exact filling independence. The companion
note tests the simplest fixed quadratic regulator for (6) and shows why
large planar loops defeat that particular estimate. That failure does
not defeat (9), adaptive shifts, an expansion in blocks, or a direct
response argument on the positive support.

To use (9) for the full field one still needs a uniform estimate on the
coupled current/field measure and its diffuse-source higher cumulants,
then the same physical state and quadratic limit. Conditional Gaussian
integration or a small magnetic extension alone does not supply those
steps. No new axiom, phase assertion, or independent retained grade is
introduced here.

## Finite author checks

The checker constructs a free three-cube, with its five independent
integer current coordinates, as a finite cochain normalization challenge.
It compares the original 32,243,1024 gauge-fixed clock configurations and
positive image sums with independent Gaussian quadrature of (9), at
(beta,N)=(.25,2),(.5,3),(.8,4). It checks complete six-face source and
covariance identities and projected/mixed fourth cumulants. These
three-cubes are not thermodynamic four-dimensional evidence. Integer
cutoffs3/4, image cutoffs8/10 and quadrature orders120/160 are compared,
without an interval certificate. Exact rational cochains check (1),
the square completion and the allowed filling change. A noninteger-N
control loses that periodicity. The written proof carries the general
finite-dimensional statement.
