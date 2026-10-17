# Energy-weighted loaded two-site source and complete seed mass

ROOT author derivation, distinct check pending. This is a conditional interface: it does not yet certify installation of the changed emitter in the old apparatus or import its old runtime. Dependencies: two_site_loaded_inverse/PROPOSAL.md 33b4f11058bd8953f6ea1cc03e85fde8f884f2ac2cf2eadd22f509f0b390ca4d; two_site_product_source/PROPOSAL.md 8892741e6a14bca4565aef77d5913a3afca43a850c202c43dc2afb8ed3d9e303 (scalar distinct check pending when written). No novelty claim for a Schur or resolvent identity.

## Contract

Take .0027<j<.003, 0<lambda<=1e-8, kappa²=2jlambda, and 0<d<=2.4e-8. Write r=lambda/j and s=1-2r>0. In each old-energy physical window E=c+2j+a+delta, a=1 or3, |delta|<=d, let D=E-c-2j-B. In each parity/record sector suppose its selected eigenvalue is delta with projection P; all complementary eigenvalues have modulus at least .185. Retain the full fiber, including the other prepared vacuum column on each window. G0=m_j(D) uses the physical open/closed halfline root on every channel, as in the inverse lemma.

Assume the actual pre-emitter boundary kernel has continuous upper/lower boundary values and

 ||G-G0||<=a0+b0|delta|,
 a0>=0, b0>=0.

Assume also the finite matching/recovery inverses that construct this G are nonzero on neighborhoods of both closed windows and all channel roots avoid thresholds there. These assumptions must be verified for the actual changed attachment before asserting its absolute continuity. They are not supplied by a scalar Markov model.

The existing unloaded endpoint derivation slow_lead_wide_endpoint/PROPOSAL.md c4c99408686166ba4d80bc973f5c22afdd1185bbf38e4539512dc26afd5cd5e3 has the candidate envelope a0=8e-18,b0=46000/.0053+290/g. Sections1–2 contain no emitter kappa in their kernel calculation; their matching geometry/domain and current source identities must nevertheless be checked before reuse. Its later one-site emitter, mass and runtime are NOT premises here, and its stated kappa<=1e-8 domain is not silently extended.

## Weighted inverse

Set A=D-kappa²G, Q=D A-lambda²I, A0=D-kappa²G0, Q0=D A0-lambda²I. The previous all-channel polynomial estimate on P gives

 |q0(delta)|>=sqrt(s)(delta²+lambda²).

On the complement, the physical real root obeys |m_j(x)|<=1/j, so

 q0(x)>=x²-2lambda|x|-lambda²,
 |1/q0(x)|<30, |x/q0(x)|<6, |x|>=.185.

The inequalities follow at the minimum modulus .185 and lambda<=1e-8; both scalar expressions decrease thereafter. Since sqrt(s)(delta²+lambda²)<7e-16, the selected upper envelope also dominates the complementary inverse. Thus

 ||Q0^-1||<=1/[sqrt(s)(delta²+lambda²)],
 ||Q0^-1 D||<= |delta|/[sqrt(s)(delta²+lambda²)]+6.

Do not replace the energy-dependent kernel deviation by its maximum first. Its exact ordered factor is Q=Q0(I-kappa²Q0^-1 D(G-G0)). Using |delta|/(delta²+lambda²)<=1/(2lambda) and delta²/(delta²+lambda²)<=1 yields

 ||kappa²Q0^-1 D(G-G0)||<=Theta,
 Theta=(j a0+kappa² b0)/sqrt(s)+6kappa²(a0+b0 d).

If Theta<1, both lips have invertible Q and

 ||Q^-1||<=1/[(1-Theta)sqrt(s)(delta²+lambda²)].

Each lip is treated in its actual order; Qminus is not identified with Qplus-adjoint. The full two-source Schur matrix is invertible because a kernel vector would give Q psi1=0 and then psi0=0. Source recovery and the existing nonzero downstream matching therefore supply complete finite-coordinate boundary values.

## Seed resolvent difference and genuine reference

Let R be the full two-source Schur inverse and R0 its reference. The load perturbation occurs only in the second-source diagonal. The ordered resolvent identity gives exactly

 R00-R00,0 = kappa² R01,0 (G-G0) R10
           = kappa²lambda² Q0^-1(G-G0)Q^-1.

Here R01,0=-lambda Q0^-1 and R10=-lambda Q^-1. There is no commuting actual G with D and no inversion of D at delta=0. Consequently

 ||R00-R00,0|| <= kappa²lambda²(a0+b0|delta|)
                  /[(1-Theta)s(delta²+lambda²)^2].

The reference is a genuine direct sum of the exact two-site scalar halflines shifted by every B eigenvalue and c, not a fictitious flat imaginary selfenergy. Its prepared vacuum seed channels have the two disjoint supports centered at a=1 and3 and common mass p0 on their own width-d interval. The scalar source derivation establishes total normalization and

 1-p0<=min(1,4lambda³/[3pi s d³]).

All other reference rows, including real opposite-window resolvents, stay in the subtraction.

For the actual model, assume the previously stated complete matching regularity. Appending the proved nonzero two-source denominator reconstructs every finite coordinate with continuous boundary values on neighborhoods of the windows. Therefore its seed matrix measure there is absolutely continuous with density -Im(R00)/pi; this local conclusion does not exclude outside atoms or give a complex strip/time bound.

Imaginary-part and vacuum compression are contractions. Integrating the full-fiber difference on EACH physical window and extending its nonnegative bound to the real line gives

 eta_mass <= [j a0+kappa² b0/pi]/[(1-Theta)s].

Indeed integral lambda²/(delta²+lambda²)^2 ddelta=pi/(2lambda), while integral lambda²|delta|/(delta²+lambda²)^2 ddelta=1. These exact integrals are the reason there is no logarithmic H=d/lambda loss in this interface.

There are two physical windows in the common union I. Combining the operator measures, parity blocks and the initial coherent record0 gives

 0<=V*E_H(R outside I)V
    <=min(1, 4lambda³/[3pi s d³]+2eta_mass) I,
 ||E_H(R outside I)V||
    <=sqrt(min(1,4lambda³/[3pi s d³]+2eta_mass)).

This is a full old-input operator bound, not just bounds on diagonal probabilities; passive references are retained. It pays each physical window once and retains any actual outside singular mass. No orthogonality of omitted old-input outputs is assumed.

## Scope and next decision

The interface permits larger kappa than an earlier source theorem only IF the unchanged pre-emitter kernel/geometry is independently confirmed to have the stated envelope and regularity; no such extension is declared by this conditional calculation. Literal B/K/W, record-sector common phase, actual outgoing row, source/core escape, normalized target, finite duration/cut and coefficient robustness still require their own changed-source proof. Positivity of the algebraic emitter is covered by the inverse lemma, not a complete collision inventory. No numerical operating point, full apparatus speed or resource advantage is claimed. No physical axiom, editable prompt or canonical source changed.
