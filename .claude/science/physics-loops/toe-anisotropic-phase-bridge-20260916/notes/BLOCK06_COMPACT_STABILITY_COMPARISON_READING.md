# Compact stability comparison: a source check and its limited repair

Working source-application check, 2026-09-16. The purpose is to decide
whether a massive Gaussian cluster expansion supplies the missing
fixed-coupling Hamiltonian phase estimate. It does not currently do so.
The calculation below concerns one displayed comparison, not a verdict
on the cited paper's main theorem and not a phase or axiom obstruction.

## 1. Source and domain

Chatterjee and Yakir, [Correlation decay for U(1) lattice Higgs theory:
the case of small mass, arXiv2509.19176v1](https://arxiv.org/abs/2509.19176v1),
study the classical compact link action on a free cubic box

    H_m(theta)=sum_p[1-cos(C theta)_p]+m sum_e[1-cos(theta_e)],
    S_m(theta)=(||C theta||^2+m||theta||^2)/2, m>0,
    theta_e in [-pi,pi].

Here C is the ordinary real oriented edge-to-face incidence matrix. The
paper defines this raw curl on page1. Its Claim5.1, page22, asserts
H_m>=S_m/5 for all link configurations, by applying a scalar inequality
valid on [-pi,pi]. Raw plaquette curls need not belong to that interval.

The downloaded 38-page v1 PDF has SHA256
`a5d2d2afb15915b3f89b49ba8f10707f1f7d83c1539965681d300eef7c012ecb`.
All38 extracted pages were read; page22 was also rendered and inspected.
The source's main result holds m fixed and allows its large-beta threshold
to depend on m. It is not a statement uniform down to m=0 at fixed beta.
The paper's additional slowly decreasing-m remark is not such a statement
either. Its model and time prescription also differ from our Hamiltonian.

## 2. Counterexample inside an actual square box

Use the nine vertices {-1,0,1}^2, with edges in the two positive coordinate
directions. Put vertex phases phi/pi equal to

    phi(1,0)/pi=1/2, phi(1,1)/pi=1, phi(0,1)/pi=-1/2,

and zero at all other vertices. On each positive edge x->y, let theta_e be
the principal representative of phi(y)-phi(x). Six edge angles are
nonzero, all equal to plus or minus pi/2. The four raw face curls are
0,0,0,2pi, with the nonzero face based at (0,0). Consequently

    sum_p[1-cos(C theta)_p]=0,
    sum_e[1-cos(theta_e)]=6,
    ||theta||^2=3pi^2/2, ||C theta||^2=4pi^2.

At m=1/10 the asserted comparison would require

    3/5 >= (83/200) pi^2,

which is false (pi>3 already suffices). Every link lies strictly within
the scalar comparison's interval, so this is not a link-boundary ambiguity.
The compact connection is pure gauge. Taking the principal representative
of its *face* curl would make that curl zero, but that is a nonlinear
operation and is not the Gaussian quadratic S_m printed in the claim.

This is a counterexample to the stated constant in Claim5.1 for its stated
raw-curl domain. It does not show that the paper's final exponential-decay
theorem is false or that the argument cannot be repaired at each fixed m.

## 3. A valid mass-dependent replacement for the full free-box action

For a principal link angle, 1-cos(theta)>=2theta^2/pi^2. Also, each face
has four edges and each edge belongs to at most2(d-1) faces. Cauchy-Schwarz
therefore gives

    ||C theta||^2 <= 8(d-1)||theta||^2.

Keeping just the nonnegative link potential proves

    H_m(theta) >= [4m/(pi^2(8(d-1)+m))] S_m(theta).       (1)

This coefficient is positive at each fixed m, uniform in the free-box
volume. No restriction to a small-field set is required. The preceding
explicit configuration also forces any coefficient a(m) in a universal
comparison H_m>=a(m)S_m to obey

    a(m) <= 12m/[pi^2(4+3m/2)].                         (2)

Thus a positive m-independent raw-curl comparison cannot hold as m tends
to zero. The lower bound(1) and the upper restriction(2) have the same
linear dependence on m at small mass, up to constants.

Equation(1) concerns the full free-box action. It does not automatically
repair the source's restricted-block, fixed-boundary or partition-function
estimates; those require checking which edges and boundary terms remain.
No claim to have repaired or revalidated the entire paper is made here.

## 4. Consequence for the campaign

The compact action must retain its winding sectors when compared with an
unwrapped Gaussian. A valid massive comparison can deteriorate as the
mass is removed. This calculation rules out importing the displayed
mass-independent raw-curl bound as the missing massless estimate. It does
not exclude compact large-field expansions, gauge-fixed comparisons with
explicit integer sectors, or a physical-time block construction.

The Hamiltonian target is unchanged: control the actual fixed-g
transverse electric response, or prove a full compact physical-source
limit, uniformly in growing spatial volume. The ground-state comparison
in BLOCK05 supplies equal-time limits but does not supply that response.
No axiom, primitive, phase assignment, retained status or external paper
has been changed.

## Review and proposal status

The [claim-status contract](../CLAIM_STATUS_CERTIFICATE.md) and
[premise inventory](../ASSUMPTIONS_AND_IMPORTS.md) apply to this author
proposal. The [negative-claim checklist](../NO_GO_DISCIPLINE_CHECKLIST.md)
records the scoped comparison restrictions and untested alternatives.
Independent review, formal registration and retained landing are pending.
