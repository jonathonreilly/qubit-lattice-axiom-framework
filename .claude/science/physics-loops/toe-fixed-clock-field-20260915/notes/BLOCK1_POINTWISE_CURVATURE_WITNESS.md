# A negative pointwise-curvature witness for the actual hybrid generator

Personal derivation and finite check, 2026-09-15. This rejects one sufficient
proof criterion for the generator in BLOCK1_POSITIVE_HYBRID_GENERATOR.md.
It does not reject a spectral gap, integrated Bochner estimate, a Gaussian
field limit, another dynamics, the clock model, or the framework axioms.
No public no-go or independently reviewed theorem is being submitted here.

## Geometry and test function

Take the single free four-dimensional unit cube: 32 edges, 24 faces, and
rank(D)=17. Its signed coordinate symmetries act transitively on faces,
so the exact orthogonal projection P has P_pp=17/24. Direct incidence gives
H=DD*, H_pp=4 and (H^2)_pp=24: each face shares an edge with eight others,
with off-diagonal H entries +/-1. Put tau=1/64 and A=I+tau H. Therefore

    p0=P_pp=17/24,
    d=(PAP)_pp=37/48,
    e=(APA)_pp=1289/1536,
    A_pp=17/16.                                         (1)

Fix beta>=1, h=2pi sqrt(beta), a face p, and the allowed carrier point
z0=h e_p. Put q=h^2 A_pp, mu=exp(q/4), lambda=exp(-3q/4),
r=exp(-q/2). The p-directed jump rates at z0 are c_-=mu and c_+=lambda.

Let f(z)=F(z_p), choosing the following finite jets:

| z_p | -h | 0 | h | 2h | 3h |
|---|---:|---:|---:|---:|---:|
| F | 2 | 1 | 0 | 0 | 0 |
| F' | 0 | a0 | a0 | a0 | 0 |
| F'' | 0 | 0 | 0 | 0 | 0 |

Here a0=h mu/2, and also F'''(h)=0. Finite disjoint smooth bumps, each
equal to one near its center, times the displayed constant/linear local
polynomial realize these jets with compact support. Thus f is an actual
smooth bounded test on the carrier, not inconsistent independent values.

At z0,

    Gamma(f)=p0 a0^2 + mu/2.                            (2)

## Direct scalar reduction with V_e=0

Write L=L_c+L_j and Gamma=Gamma_c+Gamma_j. For the Gaussian reference,
the continuous contribution to Gamma2=(L Gamma)/2-Gamma(f,Lf) is
d a0^2. The mixed contribution from the p jumps is

    -d h mu a0 - e h^2 mu/16.                           (3)

The terms involving F'(z_p+/-h)-F'(z_p) vanish by the chosen jets; the
second term in (3) comes from L_c acting on the p jump rate. It must not
be omitted even though the second derivatives of F at these points vanish.

For a one-dimensional paired exponential jump, minimizing over the second
neighbor values with Delta_+f=u and Delta_-f=v gives the local expression

 (1/4)[(1-r)(lambda^2 u^2+mu^2 v^2)
          +lambda mu(3/r-1)(u^2+v^2)+4lambda mu u v].   (4)

It follows by substituting the rates at the two neighboring points in
the definitions of Gamma and Gamma2. The minimizing second-neighbor
values are 2u and 2v relative to f(z0). Our u=0,v=1 uses precisely these
values. Since lambda mu=r and mu^2 r=1, its contribution is

    mu^2(1-r)/4+(3-r)/4.                               (5)

Other face jumps also change the p jump rate. Their differences of f are
zero, but their contribution to (L_j Gamma_j)/2 is not zero. For any of
the eight neighboring faces k it is

    (1/2)mu exp(-q/4)[1-cosh(h^2 A_pk/2)].

Since A_pk=+/-tau and mu exp(-q/4)=1, these terms sum to
4[1-cosh(tau h^2/2)]<=0. All other faces contribute zero.

Combining (3)-(5) with a0=h mu/2 gives the exact reference value

 Gamma2_0(f)(z0)
   =mu^2(1-r-d h^2)/4+(3-r)/4
       -e h^2 mu/16 +4[1-cosh(tau h^2/2)].              (6)

The negative mixed term in (3) is the reason convexity of the continuous
quadratic action does not give a positive pointwise curvature bound for
this sum of diffusion and jump generators.

## Keep the actual finite-clock correction

The exact electric extension is even and h Z^faces-periodic. Its gradient
therefore vanishes at z0 and all one- and two-jump points used above.
The jump rates are unchanged by the correction. Only the continuous
curvature Hessian term changes:

 Gamma2(f)(z0)-Gamma2_0(f)(z0)
     =-a0^2 (P e_p).Hess V_e(0)(P e_p).                 (7)

If ||Hess V_e||_op<=delta_e, then its absolute value is at most
delta_e p0 h^2 mu^2/4. Main's smoothing construction supplies

    delta_e=3 g^2 C0 exp(-g^2/1024),
    g^2=N^2/beta, C0=58,320,000,000,
    g^2>=65536 ==> delta_e<2e-12.                      (8)

This is a theorem input with its supplied law, free-cube and extension
hypotheses kept. It is not a numerical evaluation of the full potential.
No new primitive is used. For beta>=1 and N^2/beta>=65536 one has
h^2(d-delta_e p0)>4 and q>4. Equations (6)-(8) then give

    Gamma2(f)(z0) <= -3 mu^2/4+3/4 < 0.                (9)

The two remaining explicit terms in (6) are nonpositive. Thus a uniform
positive pointwise Gamma2/Gamma estimate for this particular generator
is unavailable in the intended small-electric-correction range, including
arbitrarily large fixed beta with sufficiently large fixed N.

## Independent calculation path and the preserved numerical issue

`../evidence/block1_hybrid_curvature_check.py` builds the full four-cube D
and P, then evaluates L Gamma and Gamma(f,Lf) using their vector/tensor
definitions and the bump-compatible jets. It separately compares with (6).
For beta=1,2,4 the ratios Gamma2_0/Gamma are about -1.05248, -1.07036,
and -1.07930. The finite-clock Hessian allowance leaves all three negative.
The direct/scalar relative differences are at most 4.04e-16.

An initial floating-point evaluation failed at beta=2: forming the full
Gamma before subtracting neighboring values erased its exponentially
smaller jump component. The original source, output and failure are
preserved under `../review/block1_curvature_initial/`. The corrected
evaluation subtracts the continuous and jump components separately; no
tolerance was loosened. This is an arithmetic implementation repair,
not a change to the analytical expression or its target.

These are author checks. They do not independently review the upstream
extension theorem, certify all infinite-volume claims, or establish the
absence of other functional inequalities.

## Consequence for the campaign

Keep the positive generator and its mean-rate identity. Drop only the
unqualified pointwise positive-curvature route. A rare high-energy point
can spoil that criterion even though its invariant probability is tiny.
An integrated estimate can still exploit the actual probability weights.
In particular integral Gamma2 = integral (Lf)^2 is nonnegative under
reversibility; (9) does not contradict it or prove that its positive
spectral-gap strengthening fails. Weighted large-field control, a different
reversible dynamics, and the signed defect expansion remain live routes.
