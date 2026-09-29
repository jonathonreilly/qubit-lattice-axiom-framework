# Affine-lapse mixed-bracket obstruction for the supplied kinetic seed

Discovery checkpoint, 2026-09-29. Author mathematical status: proved below;
focused independent reconstruction complete. Formal review/audit: not run.
This is an optional-comparator failure, not an inconsistency of the axioms.
The negative-claim submission gates are not yet certified.

## Exact claim and inputs

Keep the block112/block62 flat canonical seed, with the canonical sign fixed
in NONLINEAR_CONTRACT.md. On the axial diagonal sector write A=h_xx,
B=h_yy,C=h_zz and their conjugate momenta P,Q,R. The relevant functionals are

    C1[N] = K sum_x N_x Delta(B+C)_x,
    T2[N] = sum_x N_x [P_x²+Q_x²+R_x²-2P_x Q_x-2P_x R_x-2Q_x R_x]/(8 alpha),
    G1[X] = 2 sum_x X_x (P_x-P_(x+1)).

Here alpha is nonzero. No value of K is needed for the obstruction. The
canonical bracket is {h_i(x),p_j(y)}=delta_ij delta_xy. Continuous tensor
variables and this specific kinetic lapse density are supplied hypotheses.
They are not registered primitives and are not derived from the four axioms.
The larger normalized face-timing family does not enter this diagonal sector.

Let C=C1+V2+T2+C3+... and G=G1+G2+G3+..., with regular analytic jets at the
flat origin and the stated time reversal (C even, G odd in momentum).
V2 is any quadratic coordinate potential; G2 is any bilinear hP functional.
C3 may contain all hhh,hPP terms; G3 may contain all hhP,PPP terms. Each proposed jet and kernel has finite total support, with no common fixed
upper radius across the class in the theorem. No symmetry reduction, uniform V2 normalization or continuum
cubic ADM normalization is needed.

Require the ordinary mixed constraint-valued identity through field degree2:

    {G[X],C[N]} = C[U0(X,N)+U1(h;X,N)+...] + G[W1(p;X,N)+...] .

U0 is a translation-covariant bilinear finite-range kernel. On constant shift
and affine lapse its first lapse moment is normalized to the continuum Lie
bracket: U0(1,x)_0=1. Explicitly, if

    U0(X,N)_z = sum_(a,b) u_ab X_(z+a) N_(z+b),

then sum b*u_ab=1. Bond half-offsets in X are immaterial when X=1. The zeroth
moment may be arbitrary for the test below. The h-dependent U1 and arbitrary
momentum-dependent mixing W1 are allowed. Other bracket obligations, including
CC/GG/Jacobi, can only impose additional conditions; they cannot repair a
failure of this necessary equation.

**Claim.** No such jet exists with these inputs. The obstruction is independent
of support radius. It does not exclude different quadratic kinetic densities,
additional clock/embedding carriers, noncanonical phase spaces, singular
structure functions, or emergent rather than exact microscopic mixed closure.

## Proof by one phase-space evaluation

The degree-two, momentum-quadratic part of the mixed equation is

    {G1[X],T3[N]} + {G2[X],T2[N]} + {G3_PPP[X],C1[N]}
        = T2[U0(X,N)] + G1[W1(p;X,N)].

Choose X_x=1 and N_x=x, and the field configuration

    h=0, P_x=0, Q_x=q delta_(x,0), R_x=0,   q != 0.

First, G1[1] is identically zero by telescoping, so its bracket with every
T3 vanishes. Second, C1[x] is identically zero because Delta x=0 (summation
by parts for finite-support fields), so its bracket with every cubic generator
vanishes. Third, the differential of T2[x] at the chosen phase point is zero:
it has no h derivative, and every momentum derivative contains x times a
momentum at that same site. The only occupied site is x=0. Therefore its
bracket with any differentiable G2 is zero, regardless of G2's coefficients.

The complete left side is consequently zero. On the right, G1[W1] vanishes
at the phase point because P=0 everywhere, even for field-dependent W1.
But T2[U0(1,x)] equals q²/(8 alpha), since U0(1,x)_0=1. Thus the necessary
identity says 0=q²/(8 alpha), which is false.

No omitted higher Taylor coefficient contributes at degree2: G1[1] and C1[x]
are identically zero, and all remaining higher brackets have larger field
degree. No equation was evaluated only after incorrectly discarding a
nonzero canonical derivative; the two linear functionals vanish identically,
and the entire differential of the kinetic functional vanishes at the point.

## Compact-support and three-dimensional scope

Affine lapse and constant shift are a convenient algebraic notation. For
any proposed finite-support jet and finite-range U0,W1, replace them by compact
smearings equal to x and1 on a sufficiently large neighborhood of the occupied
momentum plane. The only potentially relevant derivatives of T3 or G3 are
within twice their density support radius of that plane. The cutoff derivatives of
G1 and C1 lie outside this region. All four evaluations in the proof remain
exact. Thus an unbounded smearing is not a load-bearing assumption.

For the full staggered three-dimensional seed use a cylinder with periodic
transverse directions and fields uniform in those directions. Take xi along
x and let only P_yy be supported on the x=0 plane. All linear momentum
constraints vanish: P_xx and shear momenta are zero, while the y derivative
of P_yy is zero. The affine x lapse has zero diagonal and face curvature
variation. The kinetic differential again vanishes, and the nonzero right
side is the transverse area times q²/(8 alpha). A translation-covariant local
identity on the infinite cubic lattice would descend to this sector, so it
must pass this necessary test. This is not a sufficiency argument for a
three-dimensional construction.

The chosen point has T2 nonzero, hence is not on the full scalar-constraint
surface. The claim concerns the declared off-shell constraint-valued mixed
identity with a regular continuum-normalized U0. It is not a proof that every
weakly first-class ideal or every singular/redefined constraint set fails.

## Exact coefficient controls

On the already serialized radius-one and radius-two full mixing systems,
the phase evaluation defines a dual certificate without solving equations.
For each GC2_P2 row containing two Q factors at the same site, weight it by
8 times (the N position minus the Q position); give continuum_U0_dN weight1.
All other rows receive weight0. Recombining gives identically zero on every
unknown coefficient and RHS1. The resulting certificates have11 and33 rows,
respectively, and are saved in nonlinear-evidence/axial_r{1,2}_affine_lapse_certificate.json.

This exact control confirms the evaluation against all620/2920 columns,
including unrestricted cubic-momentum and mixing contributions. The general
proof, not extrapolation from these two radii, supplies radius independence.
Independent verification is recorded in independent-axial-check/
AFFINE_LAPSE_CHECK.md. It reconstructs the direct duals, supplies a finite-torus
proof for every finite radius, checks the full3D embedding, and independently
tests a cross-site kinetic mutation. Root controls also test five seam sizes
and the load-bearing U0 moment. Formal delivery checks remain pending.

## Consequence and live escapes

The supplied ultralocal quadratic kinetic lapse term and exact continuum-form
mixed clock/shift covariance cannot both be retained in this regular jet class.
The earlier large finite-radius certificates were valid but obscured this
simpler cause. This does not establish a problem with lattice or qubit axioms.
A changed kinetic pairing with cross-site momentum terms can give T2[x] a
nonzero differential at the test point and therefore escapes this proof;
whether it preserves the leading lapse bracket must be derived anew.
Augmented clocks, a modified constraint interpretation, approximate infrared
closure, and native collective dynamics also require their own explicit laws.
