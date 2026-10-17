# Full-fiber three-site source denominator

ROOT author derivation; distinct check pending. This is a conditional algebraic interface for a third source site, not a completed output theorem. Use the same full finite self-adjoint internal D, physical reference G0=m_j(D), and old-window interpretation as two_site_loaded_mass/PROPOSAL.md f2b34e07c37ee4a72b1a0301eb6f364431c71055a0a1a5b2ade90159dee9c39f. That mass theorem is not imported: the source matrix here changes.

Take .0027<j<.003,0<lambda<=1e-8, a1=lambda/sqrt3,a2=lambda sqrt(8/3),kappa²=3jlambda, r=lambda/j. On each physical window selected D=delta with |delta|<=d<=2.4e-8; complementary eigenvalues have modulus>=.185. Assume ||G-G0||<=a0+b0|delta|, a0,b0>=0, with actual continuous physical boundary values and full background matching. No commutation of G and D is assumed.

For A=D-kappa²G the three-source Schur matrix is

 S=[[D,a1 I,0],[a1 I,D,a2 I],[0,a2 I,A]].

Define P(D)=D²-a1²I and Q=P(D)A-a2²D. For forcing(f,0,0), its exact last-source column is

 psi2=a1 a2 Q^-1 f,
 psi1=-a1 A Q^-1 f,
 psi0=(D A-a2²I)Q^-1 f.

Direct substitution in all three rows proves this, including delta=0. Invertibility of Q implies invertibility of S: for a homogeneous solution use row3 to write psi1=-A psi2/a2, then row2 to write psi0=(D A-a2²)psi2/(a1 a2), and row1 gives Q psi2=0. This uses a1,a2>0, not any inverse of D or A.

Reference Q0=P(D)(D-kappa²G0)-a2²D is a scalar function of D. In an open reference channel let y=x/lambda and s_x=sqrt(1-x²/(4j²)). Its scalar value is

 q0(x)=x³-3lambda²x-(3r/2)x(x²-lambda²/3)
                  +i3lambda s_x(x²-lambda²/3).

Squaring, the r² terms cancel exactly:

 |q0(x)|²/lambda^6
   =(1+y²)^3-r(3y^6-10y^4+3y²)
   >=(1-3r)(1+y²)^3.

Indeed the difference has coefficients19r*y^4+6r*y²+3r, all nonnegative. The reference denominator is nonzero, and

 |P(x)/q0(x)|<=|x²-lambda²/3|
             /[sqrt(1-3r)(x²+lambda²)^(3/2)].

A useful sharper identity is

 (1+y²)^3-9(y²-1/3)^2=y²(y²-3)^2>=0.

Thus the last ratio is at most1/[3lambda sqrt(1-3r)]. Also |x| times the ratio is at most1/sqrt(1-3r), because |x²-lambda²/3|<=x²+lambda² and |x|<=sqrt(x²+lambda²).

For complementary |x|>=.185 the physical m_j(x) is real, |m_j(x)|<=1/j. The exact q0 is x(x²-3lambda²)-kappa²m_j(x)(x²-lambda²/3). Its absolute value is at least

 |x|³-3lambda²|x|-3lambda(x²+lambda²/3)>.99|x|³.

The last inequality follows after division by |x|³ from lambda/|x|<=1e-8/.185. Therefore |1/q0|<170 and |P(x)/q0(x)|<6. These are closed-channel estimates with the physical real reference, not an imaginary bath on every B eigenvalue.

The full norm envelopes can consequently be taken as

 ||Q0^-1||<=1/[sqrt(1-3r)(delta²+lambda²)^(3/2)],
 ||Q0^-1 P(D)||<=|delta²-lambda²/3|
        /[sqrt(1-3r)(delta²+lambda²)^(3/2)]+6.

For the first, the selected envelope is larger than170 throughout the stated narrow window. The ordered factorization is

 Q=Q0[I-kappa²Q0^-1 P(D)(G-G0)].

Its norm perturbation is at most

 Theta3=(j a0+kappa² b0)/sqrt(1-3r)
                         +6kappa²(a0+b0 d).

The constant term uses kappa²/(3lambda)=j; the slope uses the separate |delta| estimate. If Theta3<1, Q and S are invertible on both lips, in their actual order, with

 ||Q^-1||<=1/[(1-Theta3)sqrt(1-3r)(delta²+lambda²)^(3/2)].

For the selected source forcing,

 ||psi2-psi2,ref||<=Theta3/(1-Theta3) ||psi2,ref||,
 psi2,ref=a1a2 f/q0(delta).

This controls the full internal column, not just one selected entry. Actual lower Q is not upper Q-adjoint; reapply the ordered factorization to the lower boundary kernel.

The exact seed-block subtraction is also available without commuting actual factors:

 R00-R00,0=kappa²(a1a2)² Q0^-1(G-G0)Q^-1,

since the reference R02,0=a1a2 Q0^-1 and actual R20=a1a2 Q^-1. It gives the norm majorant

 kappa²(a1a2)²(a0+b0|delta|)
 /[(1-Theta3)(1-3r)(delta²+lambda²)^3].

No scalar normalization, full spectral-mass theorem, local-moment theorem or temporal output is asserted here. A separate genuine scalar source and an installed three-site geometry are required. This algebra is compatible with charging actual outside mass by a valid local moment instead of integrating a coarse resolvent difference, but does not establish that moment by itself.

No old one-/two-source temporal or performance claim is transferred. Actual complete waveform/common W/phase/aging, all local rows/closed tails, finite window/cut, coefficient robustness and native identification remain open. No canonical file, editable prompt or physical axiom changed.
