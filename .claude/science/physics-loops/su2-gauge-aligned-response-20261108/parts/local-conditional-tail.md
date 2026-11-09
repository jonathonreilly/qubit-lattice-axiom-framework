# Local conditional reference-cap tail for the two-step compact quotient

Research proof extension, 2026-11-08. Mathematical check and exact scope are
recorded in `../gates/final-scope-and-local-tail-check.md`; final header/hash
reconciliation is in `../gates/relative-component-check.md`. No retained status.
Prior art: `CUT_SECTOR_COERCIVITY_ASTRA.md` at
`89faef229ff6e6bde42baad15ed8270c2f4087d8`, §§1,3,5, specifically
CS6, CS15 and CS22–CS29. This proof adapts that author's one-step conditional
reference-cap method, which credits Bałaban and Dimock for antecedents.
It does not claim a new normalization method. The changes are two hidden
levels, whole output-inclusive kernel readers, no cut, and terminal V=I.
The compact quotient and local energy witnesses are those of this pack's
`compact-forest-exchange.md` and `compact-energy-coercivity.md`.

## 1. Exact local conditional, with every normalizer

Use their two-step SU(2) model, odd L>=3, kappa>0, u>=0, beta=u,
lambda_0=lambda_1=kappa u, and terminal V=I. All distances below are
quaternion chord distances, so d(A,B)²=2[1-w(A*B)]. Tree links are fixed I.
A retained link is owned by the terminal cell containing its tail vertex.
Each terminal cell owns

    m=3L^8+1+4L^4

retained coordinates: fine non-tree links plus all intermediate links.
For a nonempty terminal-cell set R let J_R contain ALL its owned coordinates;
n=|J_R|=m|R|. Fix all others to z. Let P_R contain every fine plaquette
whose full word reads J_R. Let C_R contain every level-zero or level-one
kernel whose FULL factor reads J_R: input words AND its output, if hidden.
Retain each such kernel whole, including its normalizer even if that
normalizer is constant under this particular conditioning. Exterior factors
cancel. Full readers are syntactic readers; cancellations need not be used.

For c at either level set r_c=|M_c|, psi_c=r_c-<output_c,M_c>, and
H_u(r)=exp(kappa u r)/Z(kappa u r). The exact conditional is

    mu_R(da|z)=D_R(z)^(-1) exp[-u E_R(a,z)]
                         product_(c in C_R) H_u(r_c(a,z)) da_J,
    E_R=sum_(p in P_R) [1-w(U0,p)] + kappa sum_(c in C_R) psi_c. (1)

This is a conditional in the quotient coordinates, not a fine-link exterior
conditional. All terms of E_R are nonnegative; D_R>0 for every z.
An intermediate link is an output reader of its own level-zero kernel,
and an input of at most eight level-one kernels. A fine coordinate is an
input of at most eight level-zero kernels. Fine plaquettes per fine link
number six. Consequently the conservative counts

    |P_R|<=6m|R|,       q:=|C_R|<=9m|R|                 (2)

hold. The eight-kernel incidence follows because a path is in its two
endpoint blocks: an internal edge can appear only in incident kernels,
and a crossing edge only in its face kernel. Tree substitutions cannot
increase incidence. Counts are local, with no total-volume factor.

## 2. Uniform compact normalizer and Haar cap

On SU(2)=S³ normalized Haar, a chord cap of radius 0<r<=1 has mass at
least c_H r³, where c_H=8/(3 pi³). Indeed it contains the angular cap
0<=theta<=r, whose mass is (2/pi)integral_0^r sin²(theta)dtheta;
sin(theta)>=2theta/pi proves the bound. Left/right translations preserve it.
For any mean M with r_M<=1, at its maximizing unitary M/r_M (arbitrary
when M=0), the centered gap to a point at chord distance s is r_M s²/2.
Integrating the cap of radius (1+u)^(-1/2) proves, including M=0,

    1<=H_u(r_M)<=C_H (1+u)^(3/2),
    C_H=c_H^(-1) exp(kappa/2).                           (3)

Thus every intermediate and final kernel normalizer remains in the estimate.
There is no chart restriction or selected small-field law.

## 3. Reference cap and the exact boundary cost

Let a^ref set all J_R coordinates to I and retain z outside. Define

    phi_c=1-<output_c,M_c>
         =average_tau d(output_c,P_c,tau)²/2,
    A_R=sum_(p in P_R)[1-w(U0,p)]+kappa sum_(c in C_R)phi_c,
    A_ref(z)=A_R(a^ref,z).                              (4)

Since |M|<=1, E_R<=A_R; A_R is only a comparison energy for a denominator
lower bound, never a replacement density. Put p_L=5L as a uniform bound
on each paired-path word length. Output-inclusive words have length at most
p_L+1, including inverse occurrences; terminal output factors are fixed.

Fix zeta>0 and 0<b<=1. On the product chord cap
K_r={d(a_e,I)<=r for all e in J_R}, r=b/sqrt(1+u), telescoping unitary
products changes each plaquette word by at most 4r and each complete
output/path word by at most (p_L+1)r. Applying
(x+y)²<=(1+zeta)x²+(1+zeta^(-1))y² termwise gives

    E_R<=A_R<=(1+zeta)A_ref + C_zeta |R| r²,
    C_zeta=(1+zeta^(-1)) m [48+(9kappa/2)(p_L+1)²].      (5)

There is no cut whose indicator could exclude this cap. Using H>=1 and
product Haar cap mass yields

    D_R >= exp[-u(1+zeta)A_ref-C_zeta b²|R|]
                (c_H b³)^n (1+u)^(-3n/2).             (6)

For any measurable event B with E_R>=Lambda pointwise on B, (1),(3),(6)
therefore imply

    mu_R(B|z)<=min{1, Pi_R(u) exp[-u(Lambda-(1+zeta)A_ref(z))]},
    Pi_R(u)=exp[C_zeta b²|R|](c_H b³)^(-n) C_H^q
                                (1+u)^(3(n+q)/2).      (7)

For fixed L,kappa,b,zeta, log Pi_R(u)<=C|R|[1+log(1+u)]. This counts
only selected readers, including constant normalizers, never total volume.
Empty R is the trivial no-coordinate conditional and can be treated separately.

For an explicit boundary estimate let P_b and C_b denote factors in P_R,C_R
having at least one exterior retained-coordinate reader. Their complete
exterior reader set includes hidden output links, inverse occurrences,
and all mean/normalizer inputs. Suppose every such exterior coordinate
satisfies d(z_e,I)<=beta_col. At reference, every other link, including V, is I.
Telescoping words, without assuming commutation, gives

    A_ref <= beta_col² [8 |P_b| + (kappa/2)(p_L+1)² |C_b|].  (8)

Thus one may call |P_b|+|C_b| the number of boundary factor readers, with
constant max(8,kappa(p_L+1)²/2). If instead counting distinct exterior
coordinate readers B_ext, incidence gives |P_b|<=6|B_ext| and
|C_b|<=9|B_ext|, hence the explicit alternative

    A_ref <= beta_col² [48+(9kappa/2)(p_L+1)²] |B_ext|.      (9)

A factor with no exterior readers contributes zero at reference. This uses
terminal V=I; a general V requires its additional reference mismatch cost.

## 4. Local coercivity witnesses and what absorption requires

The preceding compact-coercivity proof supplies finite positive linear
witnesses expressing 1-w(a_e) in actual fine plaquette and two-level gap
summands, with a finite uniform incidence constant. Call S_e the COMPLETE
set of energy factors used by the chosen witness, after all substitutions
and fillings; it includes the fine-plaquette and kernel-gap factors produced
by reducing intermediate plaquettes and eliminating the terminal straight
path. S_e contains energy-factor labels, not path objects. Use a set I of distinct
retained links only when every S_e lies in P_R,C_R. Then the same global
stencil incidence argument, restricted to these witnesses, gives

    E_R >= c_E sum_(e in I) [1-w(a_e)]                  (10)

with c_E>0 depending only on L,kappa. A witness may use coordinates outside
J_R; their energy factors must still belong completely to the selected
factor sets. No partially present brick or truncated witness is admissible.
If the event imposes 1-w(a_e)>=epsilon_delta for all e in I, then
Lambda=c_E epsilon_delta |I| is valid in (7). For chord threshold delta,
epsilon_delta=delta²/2. If only some witnesses meet the support condition,
only those witnesses may be counted.

For example an actual verified inequality
(1+zeta)A_ref <= Lambda/2 gives Pi_R(u)exp(-u Lambda/2).
Absorbing Pi_R needs a further explicit size/rate comparison. Excluding
cells declared delta-rough supplies neither the smaller beta_col required by
(8) nor this budget: complete exterior word readers must satisfy the stated
collar bound. No absorbing-collar theorem is proved here.

An integrated form follows with no exterior independence assumption:
for bounded nonnegative exterior-measurable Q and a fixed b_ref>=0,

    E[Q 1_(A_ref<=b_ref) 1_B]
       <=Pi_R(u) exp[-u(Lambda-(1+zeta)b_ref)]
                                  E[Q 1_(A_ref<=b_ref)]. (11)

This is disintegration of (7); exterior weights remain in both expectations.

## 5. Optional real-source identities, including the normalization

Let F,G be bounded real observables of the original chain invariant under
the root-fixed gauge group, hence genuine bounded functions on the quotient.
Write F_inf=||F||infinity and G_inf=||G||infinity. Fix z and tilt the FULL
conditional (1) by exp(sF+tG), s,t real, dividing by its conditional
expectation. For an event B fixed independently of s,t,V,

    mu_R,s,t(B|z)<=exp[2|s|F_inf+2|t|G_inf] mu_R(B|z).   (12)

The numerator is bounded above by exp(|s|F_inf+|t|G_inf)mu_R(B),
and the denominator below by its reciprocal. Thus this is a normalized
real-source bound, not an unnormalized numerator estimate.

For the following derivative identity assume also F,G are fixed functions
of the hidden chain, independent of V, and vary one terminal link V_c along
a smooth real SU(2) path. At the evaluation point its tangent is dot V_c.
If its terminal kernel belongs to C_R, the log-density derivative before
normalization is

    A_c=kappa u <dot V_c,M_1,c>,
    ||A_c||infinity<=kappa u ||dot V_c||.                (13)

The radial normalizer has no V derivative. If c is not in C_R, the factor
cancels from the conditional and take A_c=0; equivalently its original
score is a constant in the conditional variables and all relevant cumulants
vanish. Differentiation of normalized finite compact integrals then gives

    partial_s partial_t D_(V_c) mu_R,s,t(B|z)
         = kappa_4,mu_R,s,t(1_B,F,G,A_c).               (14)

In detail a first derivative of a normalized expectation is covariance
with the score; successive source derivatives give the third and fourth
joint cumulants. All observables and the score are source independent.
This retains the conditional covariance and the source normalizing
partition function. No projection onto separate source means is made.

Using the partition formula for the fourth cumulant, the sum of absolute
combinatorial coefficients is

    sum_(partitions pi of four labels) (|pi|-1)!
       =1+7+2*6+6*1=26.

Every partition has exactly one block containing 1_B. Its expectation is
bounded by mu_R,s,t(B) times the sup norms of the other variables in that
block; all other blocks are bounded by their remaining sup norms. Hence

    |partial_s partial_t D_(V_c) mu_R,s,t(B|z)|
      <=26 kappa u ||dot V_c|| F_inf G_inf mu_R,s,t(B|z). (15)

Combine (12),(7) for a real local tail bound on this derivative at V=I.
The event must remain fixed when differentiating: a V- or source-dependent
energy threshold/collar indicator is not covered. No complex-source norm,
analytic-domain estimate, full source response closure, or global conditional
covariance decay follows from (12)–(15).

## Limitations and provenance

The reference boundary cost must actually be paid. The selected local
witness supports must be complete. This note proves neither absorbing
collars nor their probabilities, nor summability of connected rough sectors,
nor the nonlinear full response. It provides finite real conditional estimates
for the actual normalized two-step quotient. Model: inherited supervisor
model, exact host identifier unavailable; launch effort medium. No numerical,
network, or Git mutation was performed. The pinned prior-art source was read
with read-only git show, as required by the task. Only this deliverable was
written; original source and previous drafts are unchanged.
