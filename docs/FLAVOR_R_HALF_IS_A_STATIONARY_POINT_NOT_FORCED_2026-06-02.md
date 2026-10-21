# Flavor: stationary points of supplied entropy functionals

**Type:** bounded_theorem
**Review scope:** supplied finite algebra under the stated hypotheses; no
physical state, generation-space identification, or audit status is derived.

Date: 2026-06-02. Claim type: bounded mathematical statement.
Companion: `scripts/flavor_r_half_is_a_stationary_point_not_forced_2026_06_02.py`.

## Carrier and readout assumptions

Supply a Hermitian circulant H=aI+bC+conjugate(b)C† on C³, with real a!=0
and the three-cycle C. Define r=|b|²/a²>=0. Its eigenvalues are
lambda_k=a+2|b|cos(arg(b)+2pi k/3), hence

    Tr(H)=3a, Tr(H²)=3a²+6|b|²,
    Q_signed=Tr(H²)/(Tr(H))²=1/3+2r/3.

This is a signed-trace ratio. If masses are lambda_k², the physical
positive-square-root ratio instead has denominator(sum|lambda_k|)².
Equality requires a common eigenvalue sign. Fixed r does not fix individual
masses: arg(b) matters, even within a common-sign region.

The [three-label premise](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md)
is an algebra theorem on a supplied C³ carrier. Its explicit boundary excludes
physical species and full-carrier multiplicity. Nothing here derives physical
chiral generations or a mass readout.

## Exact entropy statements

Define sector fractions ps=1/(1+2r), pd=2r/(1+2r) and
S_sector=−ps log ps−pd log pd, with 0 log 0=0. Binary entropy is bounded by
log2, attained only at ps=pd=1/2, equivalently r=1/2. For r>0,

    S_sector'(r)=−2 log(2r)/(1+2r)².

It increases before 1/2 and decreases afterwards. The imbalance|3−6r| has
its minimum 0 there; fraction exchange r→1/(4r) has the same fixed point.
The affine reflection r→1−r is a different map and not a derived symmetry.

If instead the supplied probabilities are(ps,pd/2,pd/2), their Shannon
entropy has maximum log 3 at equality, r=1, and derivative

    S_dof'(r)=−2 log(r)/(1+2r)².

Thus the chosen coarse graining changes which point maximizes entropy.
The numerical runner samples and differentiates these functions; these
analytic derivative/sign arguments supply the global statement.

## Distinguished algebraic values, open physical assignment

r=0,1/2,1 give Q_signed=1/3,2/3,1 respectively. r=0 gives H=aI.
At r=1 and phase 0 with a>0, eigenvalues are(3a,0,0); generic phase does
not have two zero eigenvalues. r=1 is not the endpoint of the allowed r>=0
family, nor an enhanced-symmetry endpoint for every phase.

Calling these points different physical 'lanes' is a proposed interpretation,
not evidence that charged leptons occupy the sector-entropy maximum. A
stationary point of a selected entropy is not a vacuum extremum unless a
physical dynamical principle relates them. It does not establish absence of
fine tuning, select the functional, fix phase, or resolve the positive-mass
readout. Those obligations remain open. Negative selection results under
other premises are not erased by this reframing.

The previous source's claims that there was nothing left to select and that
the charged-lepton lane sits at r=1/2 are therefore withdrawn as conclusions.
The valid content is the two conditional entropy maxima and phase/readout
boundaries, not a derivation of Q_physical=2/3.
