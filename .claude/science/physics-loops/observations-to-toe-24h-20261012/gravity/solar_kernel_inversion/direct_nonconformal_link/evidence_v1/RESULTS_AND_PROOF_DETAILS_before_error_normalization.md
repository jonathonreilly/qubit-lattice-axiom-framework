# Source-linked prediction and verification

Status: conditional-support; direct parent computation. Independent check
pending. All36 frozen radiation controls pass. Direct angular and anomaly
integration of the uncompleted source/quadrupole amplitude agrees with the
closed ratio within5.33e-15 relative. At eccentricity.8, changing the anomaly
quadrature from128 to256 points changes the power by6.09e-14 relative.
The normalized orbit has c=1000, G_N=M=a=1 and reduced mass1/4; at e=.8 its
largest speed/c=.003, speed/min(c_s)=.005 and orbital potential/c²<=5e-6.
These satisfy the declared weak/slow regime as far as orbital variables go;
unresolved self-body structure is not bounded by those numbers.

The illustrative circular comparator fixes c_s/c=.6988271187715792. For
lambda=1, the computed same-orbit power ratios are:

| Eccentricity | Candidate / supplied GR power |
|---|---|
| 0 | 1.0000000000000004 |
| .2 | 1.0113930227251993 |
| .6 | 1.0578991166213056 |
| .8 | 1.0756835941092573 |

Eliminating the leading corrected monopole instead requires
lambda=.1587212481534634 at that same speed. All four eccentricities then
give ratio1 within the declared tolerance. This alternative differs from
the leading light-bending calibration lambda=1. Neither choice is an
independent observation test; the two calibrated quantities and predictive
eccentric dependence are labelled separately.

The eight null-ray quadratures pass the frozen series controls. For the
exponential index the cubic-scaled remainder approaches6 as a/b decreases;
for the supplied Schwarzschild comparison it approaches128/3. Those cubic
values are diagnostics here, not separately proved series coefficients.
The proved quadratic coefficients are pi for a/b and15pi/4 for m_g/b,
respectively. At lambda=1, a=2m_g and the candidate coefficient is4pi.

The first execution succeeded. Its note hash precedes a prose-only accidental
plus-sign correction; the exact executed note is preserved in evidence_v1
and NOTE_TYPO_CORRECTION.json binds both identities. No scientific result or
runner changed and no execution was relabelled.

## Schwarzschild comparison derived separately

For the usual Schwarzschild null orbit, write u=b/r in areal radius and
delta=m_g/b. The orbit polynomial is1-u²+2delta u³. At the weak turning
point u0, set h=delta u0 and u=u0 sin chi. The regularized half-angle
integrand is[1-2h S(chi)]^(-1/2), where

    S=sin chi+1/(1+sin chi),
    integral_0^(pi/2) S dchi=2,
    integral_0^(pi/2) S² dchi=5pi/4-4/3.

Expanding gives deflection4h+(15pi/4-4)h²+O(h³). Since
u0=1+delta+O(delta²), h=delta+delta²+O(delta³), the result is
4delta+15pi delta²/4+O(delta³). Both metrics' b is the asymptotic impact
parameter, so the comparison does not mistake closest-approach radius for b.
The candidate r is its isotropic coordinate; no equality of the two closest
approach radii is assumed. The paired runner solves both separate root
equations and regularized angular integrals.

The primary derivation in
[Gibbons and Vyska, arXiv:1110.6508v2](https://arxiv.org/html/1110.6508v2),
sections2 and2.3, also defines b=angular momentum/energy and distinguishes
the closest-radius expansion from the impact-parameter expansion. Its
formula is a theory comparator, not data used to construct this candidate.

## Elementary eccentric integrals

Let I_n be the E-average of(1-e cos E)^(-n), d=1-e². Contour integration
or differentiating the elementary I_1=d^(-1/2) gives

    I_3=(2+e²)/(2d^(5/2)),
    I_4=(2+3e²)/(2d^(7/2)),
    I_5=(8+24e²+3e^4)/(8d^(9/2)).

One explicit recurrence avoiding an unstated integration step is
I_(n+1)=I_n+(e/n) dI_n/de. Starting from I_1, it produces these expressions.
Using cos E=[1-(1-e cos E)]/e then gives

    J=<sin²E/(1-e cos E)^5>=[(e²-1)I_5+2I_4-I_3]/e²
      =(4+e²)/(8d^(7/2)),

with e=0 obtained continuously. The third-moment average is
(8/3)m_red² a^4 Omega^6[12(2I_4-I_3)-11e²J]; substitution gives32f(e)
times that mass/orbit scale. The independent numerical quadrature uses the
Cartesian jerk tensor and scalar source derivative, not this recurrence.

## Exact scope of the algebraic obstruction (N1–N8)

1. Target: one fixed isotropic N=D scalar sector and the exponential
   temporal/spatial metric, with the declared weak separated-body limit.
2. Domain: positive speed, small v/c and v/c_s, small external potential,
   self terms discarded and zero residual body-dependent sensitivities,
   Kepler eccentricity0<=e<1. No compact-body assertion.
3. Quantifier: at lambda=1 and circular power matching, the leading
   same-orbit ratio is strictly above1 for each0<e<1.
4. Load-bearing inputs: new metric and matter/Maxwell action, homogeneous
   scalar field dynamics, weak pair approximation and supplied GR comparator.
5. Obstruction: the residual nonnegative monopole square has coefficient
   (s²+1/3)² at lambda=1; it cannot vanish for a positive real speed.
6. Positive counter-route: lambda=(1-1/(3s²))/2 cancels that monopole, but
   changes the leading bending coefficient. Other sectors/metrics are open.
7. Checks: symbolic exact-source/energy expansion; direct sphere/time
   radiation integrals; beam-independent optical orbit quadrature; all
   controls are synthetic. The e=.6 example is not a selected pulsar.
8. Resolution: retain a linked conditional model and this narrow comparator
   mismatch. Derive the next gravitational degree of freedom or changed
   action from observations; do not announce a class-wide empirical no-go.

## Independent finding and parent correction

The original constant-self-term wording did not exclude unequal constant
charge/mass ratios and hence a leading dipole. The main result is now
explicitly conditional on a formal self-term-discarded point action with
zero residual body sensitivities. BODY_CHARGE_SENSITIVITY.md derives the
otherwise omitted positive dipole and its order hierarchy. Original notes,
runner, results and correction receipt are preserved. The four new supplied
charge controls do not supply an extended-body or compact-star model.
