# Block 6 working derivation: complement and incidence structure

Status: author conditional algebra, checked by193 same-agent groups. No native alpha value or sign is claimed.
Conventions and upstream sources are in BLOCK06_EXERCISE.md. All inverses
below are the negative inverses with the original vacuum energy subtracted.

## 1. Complement formula with the Ward correction retained

Let B_star=sum over the six individual signed bond reversals. Since the
center Majorana g flips all incident quadratic terms,

    g H g = H+B_star,
    g B_A g = -B_A,
    D_barA = g D_A g = H+B_star-B_A,
    R_barA = g R_A g.

The four-link complement is unitarily equivalent to the two-link impurity;
it has the same full-active gap. The CAR give g J_A=2B_A. Consequently

    p_A = 2 R_barA B_A R_A Omega.

For negative inverses the resolvent identity has the sign

    R_barA-R_A = R_barA(D_barA-D_A)R_A
                  = R_barA(B_star-2B_A)R_A.

Therefore the exact vector identity is

    x_A-p_A = R_barA(I-B_star R_A)Omega,

and the complete scalar may be rewritten as

    8 alpha = Re sum_(C disjoint A)
        <Omega, R_C R_barA (I-B_star R_A) Omega>.       (6.1)

Every displayed factor is bounded. This uses no unbounded zero-mode operator
and needs no domain manipulation with H. It neither removes the last term
nor turns the ordered inverse product into a positive form. Equation(6.1)
is a representation of the same target, not a positivity theorem.

## 2. Exact incidence commutators

Use the existing bounded fields W_A with

    {W_A,g}=4,  [W_A,D_A]=-J_A,
    V_A=W_A-2g.

V_A has zero center coefficient and lies on the white sublattice. Thus
[V_A,B_C]=0 for every C. Since [g,B_A]=J_A,

    [W_A,B_A]=2J_A,
    [W_A,H]=-3J_A,
    [V_A,H]=-3J_A-2[g,H].

Furthermore [g,H]=B_star g and

    J_star=[g,B_star]=-2[g,H].

Hence the useful uniform relation is

    [V_A,D_C]=J_star-3J_A      for every A,C.           (6.2)

The sum of the fifteen J_A is 5J_star, because each leg belongs to five
pairs. V_A is linear in the centered pair-incidence row and consequently
T V=-3V. Neither statement asserts that the vector family R_A Omega lies
only in that incidence channel. The source already identified V_A and its
commutation with every B_C; (6.2) merely makes its numerator explicit.

All unbounded-H identities are first computed on the finite local CAR core;
their right sides are bounded local fields. They then define bounded
commutators. Passing to inverse commutators is justified by D_C>=h/4.

## 3. Perfect-matching Clifford and cavity structure

For a perfect matching A,C,D of the six legs, the three real neighbor
vectors have disjoint support, norm squared 2h^2, and are orthogonal to g.
The literal CAR give

    B_A^2=B_C^2=B_D^2=2h^2 I,
    {B_A,B_C}={B_A,B_D}={B_C,B_D}=0,
    B_star=B_A+B_C+B_D,  B_star^2=6h^2 I.              (6.3)

Define the center-decoupled comparison

    C_0=(H+gHg)/2=H+B_star/2.

It is positive as a quadratic form because H and gHg are positive, and it
commutes with g. The reference and the three pair impurities are

    H   = C_0-(B_A+B_C+B_D)/2,
    D_A = C_0+(B_A-B_C-B_D)/2,
    D_C = C_0+(-B_A+B_C-B_D)/2,
    D_D = C_0+(-B_A-B_C+B_D)/2.                       (6.4)

The four Clifford perturbations in(6.4) have equal operator norm
sqrt(6)h/2. The actual bath C_0 generally does not commute with them.
Replacing C_0 by a scalar or declaring these four resolvents equivalent
would change the native model. The matching sum obeys

    D_A+D_C+D_D=2H+gHg>=0,
    D_barA=D_C+D_D-H.

These identities expose a possible common-bath comparison route. They
supply neither a strict lower bound on C_0 nor a Neumann parameter below1.
Even a strict cavity gap alone would not justify such a parameter.

## 4. Present endpoint

Sections1–3 retain all Ward terms and suggest a more structured search than
independent inverse norm bounds. An argument that the remaining expression
in(6.1) is positive is still target-equivalent unless an actual comparison
mechanism is supplied. The exact checker now verifies the complement and
cavity identities on synthetic16-dimensional matrices and the W/V current
identities by polynomial CAR on the literal64-site L4 AP native matrix.
No2^32-dimensional Fock space or native alpha was evaluated. L4 is outside
the source's large-volume spectral theorem.

Two checker failures are preserved: structural SymPy equality failed to
expand a true Clifford square, and an overly strong fixture assertion
required every pair to fail to commute with the cavity. Three pairs in the
chosen toy do commute. The corrected fixture checks the actual mixed
pattern; no theorem required universal noncommutation. A prose sign in
[g,H]=B_star g was corrected during derivation before the passing check.
The checker explicitly rejects its wrong negative sign. The final run
passed193 groups in about13.13seconds.

The substantive continuation is BLOCK06_CHART_DERIVATION.md: a joint
rank-two metric gives a sharper all-time native chart and uniform
normalized-state compression. It still does not close the alpha sign.
