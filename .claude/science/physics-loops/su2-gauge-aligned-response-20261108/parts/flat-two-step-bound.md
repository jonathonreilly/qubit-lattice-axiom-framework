# Exact two-step flat Gaussian diagnostic

Research proof with a fresh-context mathematical check recorded in
`../gates/forest-flat-check.md`; no retained or nonlinear claim.

## Provenance and scope

Main checkout: `1e0d3b58dcda7f83152b0bb51729260247454d65`, initially clean.
Read current SCIENCE_WORKFLOW, main two-region note §§1,7, draft
`89faef229ff6e6bde42baad15ed8270c2f4087d8` MANUSCRIPT_RG §4.9
(lines 1012–1117) and shared-gauge passage (3875–3915), and the root's
`kernel-match-extraction.md`. These are the four initial source documents.
The worker's initial comparison was the draft's first-step F1–F6; the step below
checks the actual composed Q rather than importing a successor gap. No
additional literature search was made by this bounded worker; the method
is the finite-fiber compactness and finite-range Neumann argument explicitly
rederived below. Source credit: the pinned draft's authors for that method.

Subsequent Luna inventory and supervisor source reads also located
GLOBAL_RETURN_HISTORY_ASTRA section 16, GH64–GH70, at the same draft revision.
It already proves actual inherited second-chart convexity, variance and tails
using first-step critical-action/determinant suppliers. This proof instead
keeps both hidden layers in a single terminal-root forest and directly checks
their joint flat precision and Schur complement. The earlier second-chart
result remains credited; this is not a first-ever two-step gap claim.

Preflight ran before proof work: disk 110 GB free, memory 33% free, load 5.5,
nice and origin connectivity passed; model floor not checked because no
preflight target was named; memory cap unavailable. No numerical jobs ran.
Host subagent launched at medium reasoning; inherited model identifier is
not exposed by the tool. No commit, push, audit, or source edit outside this
file is performed.

Take odd L≥3, fine torus side N=L²m, m≥3, three layers with spacings
1,L,L², terminal links U2=I, u>0 and κ>0. The chain is exactly
exp(−u W(U0)) Kκu(U1|U0) Kκu(I|U1), relative to product Haar.
Both kernels use the paired coordinate-order arithmetic contour means
of the main note, with all input-dependent normalizers retained.
The diagnostic is the Taylor Hessian at U0=U1=I, not an assertion that
the chain is Gaussian, concentrated in this chart, or globally convex.
All norms below sum independent positive links (and three color components).

## 1. Hessian including the normalizers

Write Uh,e=exp(i ε ah,e·σ). For a kernel output write similarly b.
For each contour γ let Pγa be its signed link sum, Q a=averageγ Pγa,
and define the nonnegative operator V by

    <a,V a> = Σc [averageγ |Pγa|² − |(Qa)c|²].

Write R for the weighted contour reader, so V=R*R−Q*Q≥0.
The quaternion mean has scalar part 1−ε² average|Pγa|²/2+O(ε³),
vector part ε Qa+O(ε²), and norm
1−ε²(average|Pγa|²−|Qa|²)/2+O(ε³).
The scalar product with the output quaternion is
1−ε²[|b|²+average|Pγa|²−2b·Qa]/2+O(ε³).
Consequently, with t=κu and b(t)=Z'(t)/Z(t), the quadratic energy of
−t<output,M>+log Z(t|M|) is exactly

    (t/2)||b−Qa||² + (t/2)(1−b(t)) <a,V a>.       (1)

Here b(t)∈[0,1]: it is the tilted expectation of a coordinate in [−1,1],
and pairing opposite coordinates proves nonnegativity for t≥0.
Thus the normalizer variance correction is nonnegative. Setting output
b=0 recovers F1: t b(t)||Qa||²+t(1−b(t))||Ra||² for the Hessian.
The symbol b(t) in (1) is a scalar and the output vector b is unrelated.

For the two-step chain, put x=(a0,a1), η=κ(1−b(κu)). Its quadratic
energy is u<x,Hx>/2, where

    <x,Hx> = ||d0 a0||² + κ||a1−Q0a0||²
             + κ||Q1a1||² + η(<a0,V0a0>+<a1,V1a1>).       (2)

This is the action relative to Haar. The output is terminal zero.
No intermediate Wilson term has been added. Formula (2) is valid for
every finite u>0, not just asymptotically at large u.

## 2. One shared gauge and an exact local gauge slice

Partition the original sites into centered L² cubes about terminal
vertices. In each cube choose a nearest-neighbor rooted tree by moving
one coordinate at a time toward its center. Set only these fine tree
links to I. Gauge transformations on original sites are I at terminal
vertices, and act on intermediate links by restriction to their embedded
original endpoints. No intermediate tree links are separately set to I.
The number of free coordinates per terminal cube and color is

    n = [4L⁸−(L⁸−1)] + 4L⁴ = 3L⁸+1+4L⁴.

This is an exact compact gauge parametrization. Fine tree variables
determine the unique root-fixed site transformation by recursion. Fine
non-tree links are transformed by left/right multiplication; conditional
on the tree variables, the same holds for intermediate links. Product
Haar invariance gives Jacobian one; tree variables integrate to one.
Wilson plaquettes, every arithmetic contour mean and every normalizer
transform covariantly, and terminal links remain I. Thus this fixes the
actual shared symmetry, while retaining all relative-layer modes.
Its linear slice sets a0=0 only on those fine tree edges.

## 3. Actual-Q volume-uniform coercivity

On this slice define

    <x,Hmin x> = ||d0a0||² + κ||a1−Q0a0||² + κ||Q1a1||².

Use Fourier transform in terminal-cube translations. Each fiber Hmin(k)
is a continuous n×n Hermitian matrix, k∈[−π,π]^4, by finite range.
We prove its nullspace is zero for every k.

A zero vector obeys d0a0=0, a1=Q0a0, and Q1Q0a0=0. For nonzero Bloch
momentum k, any closed fine one-form is a gradient a0=dψ. To verify
this, diagonalize fine translations inside the L² cell: each frequency
p obeys exp(iL²pμ)=exp(ikμ); not all exp(ipμ)−1 can vanish when k≠0.
The curl equations sμaν−sνaμ=0 then give a=sψ for any nonzero sμ.
Every contour telescopes, hence

    Q0 dψ = d1(ψ restricted to intermediate vertices),
    Q1Q0 dψ = d2(ψ restricted to terminal vertices).       (3)

At least one exp(ikμ)−1 is nonzero, so the terminal-root value of ψ
vanishes. The fine tree condition makes ψ constant throughout its
terminal cube, hence zero. Therefore a0=0 and a1=0.

At k=0, Fourier decomposition instead gives a0=c+dψ, with c a constant
fine link form and ψ L²-periodic. Each level-zero contour has net signed
displacement L eμ, and each level-one contour L such coarse steps.
Therefore Q1Q0 c=L² c, whereas (3) vanishes for periodic terminal-root
values. Thus c=0. The tree condition again gives a0=0, hence a1=0.
This proves positive definiteness for every fiber, using the actual
path average, including its orientation and endpoints.

Compactness now defines a strictly positive, volume-independent number

    g(L,κ) = min_k λmin(Hmin(k)) > 0.                      (4)

This is an exact variational definition, not a sampled eigenvalue or
an explicit numerical lower estimate. Finite tori sample these momenta.
Since η≥0, H≥Hmin≥g I uniformly in m and u>0.

For a bound above, each contour has at most ℓ=5L−4 occurrences. A link
belongs to at most eight coarse-edge footprints, so C=8ℓ² bounds both
||Rh||² and ||Qh||². This loose bound follows by Cauchy–Schwarz in each
word and counting occurrences, and includes repeated edges. Also
||d0||²≤16 by the Fourier curl symbol. From (2), η≤κ and
||a1−Q0a0||²≤2||a1||²+2C||a0||², giving

    g I ≤ H ≤ M I,       M=16+κ(2+3C).                    (5)

Restriction to the fine-tree slice preserves this upper bound.

## 4. Weighted inverse and Gaussian sources

Assign intermediate positive links to the terminal cube containing their
initial embedded vertex, and fine positive links likewise. A level-zero
contour lies in neighboring L blocks, and a level-one contour spans
neighboring L² blocks. A factor in (2) therefore meets terminal cubes
at graph distance at most two. Deleting tree coordinates adds no range.
For terminal-cube sets A,B at distance r, let ρ=1−g/M∈[0,1). The series
H⁻¹=M⁻¹Σj≥0(I−H/M)^j proves

    ||1A H⁻¹ 1B|| ≤ g⁻¹ ρ^ceil(r/2).                    (6)

When ρ=0 the inverse is diagonal and the off-diagonal bound is zero.
For 0<ρ<1 and 0<α<−(log ρ)/2, a weighted block-row bound follows:

    sup_X ΣY exp(α dist(X,Y)) ||(H⁻¹)XY||
      ≤ g⁻¹[1+Σr≥1 (2r+1)^4 exp(αr) ρ^(r/2)] < ∞.     (7)

The shell bound deliberately overcounts periodic cubes and is independent
of volume. For the Gaussian covariance multiply (6),(7) by u⁻¹.
For linear sources supported on fine-link sets, their covariance is
u⁻¹<J,(H⁻¹)00 K>, with the corresponding localization estimate.
These statements do not assert Gaussian control of nonlinear plaquette
sources or the exact compact hidden-chain covariance.

If one includes exponential-coordinate Haar density, each retained link
adds 2/3 times identity to the action Hessian. For u≥1, replace M by
M+2/3 and retain g; this gives the same claims for that flat reference.
The compact tree change itself had no Jacobian determinant.

## 5. Schur complement, determinant, and endpoint response

In the slice coordinates, with restriction maps implicit, write

    A=d0*d0+κQ0*Q0+ηV0,
    D=κI+κQ1*Q1+ηV1,
    H = [ A, −κQ0* ; −κQ0, D ].

D≥κI. Integrating a1 in the flat Gaussian gives the fine precision

    S=A−κ²Q0*D⁻¹Q0,       S≥gI,
    (H⁻¹)00=S⁻¹,          det H=det D det S.               (8)

Indeed <a0,Sa0> minimizes <(a0,a1),H(a0,a1)> and is at least
 g||a0||². For q real coordinates the unnormalized Gaussian integral
with source J on a0 is

    (2π/u)^(q/2)(det H)^(-1/2)
       exp[J*S⁻¹J/(2u)],                                 (9)

up to the flat source-independent compact-action constant. Thus the
normalization determinant and the source covariance use the actual Q0,
V0,Q1,V1. Formula (9) is for the reference Gaussian only.
The normalized source generating function divides (9) by its value at J=0.

Allowing a terminal infinitesimal link vector v replaces κ||Q1a1||² by
κ||v−Q1a1||². Gaussian integration gives terminal quadratic precision

    u[κI−κ² Q1(H⁻¹)11 Q1*],                              (10)

the exact Schur subtraction for this flat diagnostic. Determinants in
(9) are v-independent at this quadratic order. No positivity claim for
a successor Wilson action is needed or inferred from (10).

## Current checkpoint

Closed at author-proof level: normalized two-input kernel Hessian (1),
shared terminal-root forest slice, actual two-step Q coercivity (4),
volume-uniform localized inverse (6),(7), and Gaussian Schur/source
formulas (8)–(10). The constants are variational but strictly positive
for each fixed L,κ>0. Degenerate u=0 or κ=0 is excluded. The decisive
new input is the actual telescoping identity for Q1Q0 and its L² action
on harmonic constants. Pending: independent checking of this proof;
no nonlinear concentration, all-boundary estimate, arbitrary-depth
uniformity, or continuum/source-return theorem follows. No failed
numeric route or discarded numerical evidence exists in this worker.
