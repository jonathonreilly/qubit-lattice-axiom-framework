# Independent preliminary reconstruction — before target read

This record is frozen before opening POSITIVE_READER_COVARIANCE_ASTRA.md or its
checks/positive_reader_covariance_* evidence. It is a mathematical reconstruction,
not a verdict. Requested dispatch: Astra/max; available system self-description is
generic GPT-6, so this is not backend attestation. Fresh restricted reviewer context,
same model family; no authorship and no predecessor review used as a premise.

Procedure revision: 01589af3faf806b736c42dc2f3bd625e9edead9f.
Observed worktree HEAD: 97e5a0329f86c8f7581da7878243e3309e657d0f.
No Git, audit, ledger, lock or scientific-producer mutations were performed.

## Exposure and actual producer reads

The coordinator supplied a neutral candidate mechanism and risk list. The target
filename appeared in a file inventory, but its bytes and author evidence have not
been opened. During reconstruction the coordinator announced a source freeze and
reported target labels PC6–PC31, beta=(16R)^(-4), an accretivity number 13c0/16,
endpoint factorization and changed precision lower bound a_C/U^2. Those statements
are exposure only; none is evidence or used below to certify the source.

Complete source reads (line-numbered, including incidental headers/evidence summaries):

* COVARIANT_SOFT_BACKGROUND_ASTRA.md 1–568, SHA256
  87119008ccf754022b5da0836bb1bea8e0455a5535e589a4207ee49193682b74.
* COVARIANT_SOURCE_ACTIVITY_ASTRA.md 1–722, SHA256
  da22fc28cff8f822426ccd0458959dc24668f3d8854848f8ff83dbcda9f2ba54.
* PROBABILITY_SENSITIVE_RETURN_ASTRA.md 1–544, SHA256
  6ef027d54bd0ca1948444c9b82c673ed0cae2e23cd59b25f0c53498194e9b18b.

Only the actual formulas/proofs and declared domains are premises; quoted reviews,
receipts and numerical successes are not. No external literature theorem is used.
The elementary matrix/geometry arguments below require no numerical experiment.

## Actual incoming interface

Use K=F_0''(0;V), not the shifted K_*=F_0''(a_u(V);V). CB 153–267,
SA 65–79 and PS 112–131 retain the finite-u spread, Haar Hessian and Wilson
curvature correction. K is real symmetric, fully colour coupled, range at most
two coarse-block steps, with gamma I<=K<=B I and uniform absolute scalar
row/column bounds after the explicit D conversion. Its entries have finite
original-V readers (SA radius-three stencil); K_* has nonlocal reader dependence
through a_u, so the same finite-reader assertion cannot be inferred for it.
All n0=D(3L^4+1) scalar coordinates per coarse block, root/harmonic modes and
periodic labels remain. The Wilson/kernel law is supplied model input.

For complex original coarse data, CB 223–267 provides local analytic radii and
joint derivative bounds at fixed a. A quantitative scalar row/column Lipschitz
bound on K(z)-K(V), uniform in volume, is still required at the actual target's
domain; positivity of real K alone supplies no complex-tube theorem.

PS5 (149–160) is a normalized Gaussian identity with covariance K^-1 and all
Haar, determinant, vacuum and finite-u factors. PS9–PS13 prove a quadratic
interaction regulator on the auxiliary product of link balls for endpoint-Schur
weakening, using precision >=gamma. PS14–PS17 retain covariance/coefficient
chain rules and chart/selected-cube boundary distributions. None proves an
all-order connected derivative sum or interacting normalization.

## Independent matrix construction

Let chi_A be real, parameter-independent diagonal functions with sum_A chi_A^2=I,
0<=chi_A<=1, bounded overlap M, coarse Lipschitz constant Lchi/R, and support
inside a principal patch A. Full labels must include A, the interaction-range
collar and every coefficient reader of K used in K_A and the commutator. Their
coarse-block sizes should be <=c_s R^4 and their marked overlap bounded uniformly
in T (with constants permitted to depend on fixed R). Small tori can use a single
full-torus patch; periodic seams need an explicit geometry construction.

Every principal K_A has the same spectral interval. Exponential conjugation:
for a 1-Lipschitz coarse distance f, the scalar absolute row/column norm of
exp(mf) K_A exp(-mf)-K_A is <=b_abs(exp(2m)-1). Choosing this <=gamma/2 gives
|(K_A^-1)ij| <=(2/gamma) exp(-m d(i,j)). Summing the finite-torus distance shells
and n0 modes supplies a uniform scalar row/column inverse bound C_G; no patch
volume factor is needed. The argument works for arbitrary principal patches.

With G_A the zero extension of K_A^-1, define P_A=chi_A G_A chi_A, P=sum P_A.
The zero-extension boundary is exact: chi_A K G_A chi_A=chi_A^2, even though
K G_A has rows outside A. Consequently

  K P = I + sum_A [K,chi_A] G_A chi_A,
  Rcal = I-KP = -sum_A [K,chi_A] G_A chi_A.

This fixes sign and ordering: K^-1=P sum_(n>=0) Rcal^n. It is not sum Rcal^n P.

The commutator entry is Kij(chi_A(j)-chi_A(i)). For a fixed row i, only labels
nonzero at i or at a range-two neighbor j occur; at most 2M labels per pair.
After summing the inverse row this gives absolute ATOM row norm <=C/R.
For a fixed final column k, only <=M patches with chi_A(k)!=0 occur. Sum
first over the commutator's first index, then the principal inverse column;
this separately gives absolute ATOM column norm <=C/R. A norm bound on the
cancellation sum Rcal is insufficient; both absolute atom sums are essential.

Choose c0=1/(2B) and H_A=chi_A(G_A-c0 I_A)chi_A. Each H_A is PSD and
P=c0 I+sum_A H_A. For independent t_A in [0,1], c0 I+sum t_A H_A lies between
c0 I and gamma^-1 I. The tail products P_(A0) R_(A1)...R_(An), n>=1, have
absolute two-sided norm <=p r/(1-r), where p=M_abs(P), r=M_abs(Rcal)<1.
Symmetrize each product with its TRANSPOSE, keeping the same full reader label;
this preserves its total two-sided absolute bound and sums to K^-1-P.
Every nonzero product has connected union of full labels through the summed
matrix index. Independent unit-disc coefficients on these symmetric tail atoms
have operator norm at most that same total absolute mass. Choosing it <c0/4
therefore leaves a uniform Hermitian-part lower bound for the deformed covariance.

Support weights cost exp(beta c_s R^4) per atom. Choosing beta <=constant/R^4
keeps that cost bounded while the residual is O(1/R), so R can be selected
first from fixed model constants and beta afterward. Positive core marked
incidence can be large finite O(n0 R^4); it need not be small. For tails, the
marked product inequality B(AB)<=B(A)M(B)+M(A)B(B) makes the complete marked
series finite when r<1. This construction alone provides only a small positive
support rate. A consumer that spends two whole exponential-weight units cannot
be invoked unchanged.

## Complex deformation and factorization checks required

If ||K(z)-K(V)||<=epsilon<gamma/2 then
||K_A(z)^-1-K_A(V)^-1||<=2epsilon/gamma^2 for all principal patches.
Using sum chi_A^2=I and Cauchy–Schwarz over A bounds the operator change of
sum t_A H_A by the same maximum inverse perturbation; bounded-overlap scalar
bounds are an alternative. This can preserve the core margin quantitatively.
The commutator tail must also have uniform complex-domain absolute bounds.
If Re C>=a_C I and ||C||<=U, then

  Re C^-1 = C^{-*}(Re C)C^-1 >= (a_C/U^2) I.

Thus Gaussian integrability follows with the NEW precision constant a_C/U^2;
it does not inherit the original PS gamma lower bound. PS regulator radii must
be shrunk to fit it if that envelope is claimed for this reader deformation.
A complex symmetric covariance requires an analytic determinant square-root
branch (e.g. accretive-cone continuation). Real SPD is obtained only for real
weakening parameters; complex unit-disc tails give an accretive complex density.

At a coarse component partition, an atom whose complete reader label crosses
components must vanish under the chosen support-tree weakener. Every surviving
matrix entry then has both endpoints and coefficient readers within one
component. c0 I is local. This gives block-diagonal covariance AND component-local
coefficient dependence. Only after checking both can the normalized Gaussian
and its determinant factor exactly. Gaussian expectation of 1 is one, including
all modes; factorization of an interacting/hard-history numerator additionally
needs its actual local factors. No source-dependent normalization is to be
discarded.

A forest-parameter derivative differentiates every changed atom. The Gaussian
heat identity is (1/2) sum_ij (dCij/dt) partial_i partial_j density, including
diagonal covariance pairs and every scalar colour. There is a separate derivative
of each weakened interaction/source coefficient. On the fixed product chart,
integration by parts retains both boundary terms; repeated derivatives retain
corners. A single endpoint covariance pair formula cannot replace this chain
rule for full-reader weakening.

## Scope of this preliminary reconstruction

The proposed mechanism appears capable of a finite-u, finite-volume, full-mode
covariance localization/weakening theorem with small positive support rate and
a narrowed complex tube, subject to checking the actual geometry and constants.
This is not a verdict on the unopened source. All-order derivative-tree sums,
boundary trace summation, interacting/reference normalizer cancellation, return
of the selected-sector complement, arbitrary histories/effective iteration,
continuum existence and a physical continuum gap remain distinct obligations.
Failure of an estimate would not be a no-go theorem for the framework.

Freeze UTC: 2026-10-30T01:38:30.232975+00:00
