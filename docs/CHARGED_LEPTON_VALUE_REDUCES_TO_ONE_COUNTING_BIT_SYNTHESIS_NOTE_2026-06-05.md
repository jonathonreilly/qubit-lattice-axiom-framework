# Koide model: supplied coefficient balances and a doublet complex structure

**Type:** bounded_theorem
**Review scope:** supplied finite algebra under the stated hypotheses; no
physical state, generation-space identification, or audit status is derived.

Date: 2026-06-05. Claim type: conditional algebraic synthesis.
Primary runner: `scripts/charged_lepton_value_one_counting_bit.py`.
No audit outcome or physical charged-lepton value is established here.

## Supplied carrier and signed readout

On a supplied C³ label carrier let C be the real three-cycle and
H=aI+bC+conjugate(b)C², with real a!=0. Then

    Tr H=3a, Tr H²=3a²+6|b|²,
    Q_signed=Tr H²/(Tr H)²=1/3+2r/3, r=|b|²/a².

If the mass prescription is m_k=lambda_k², its usual positive-square-root
ratio has denominator(sum|lambda_k|)². It equals Q_signed only when the
nonzero eigenvalues have one sign. The phase of b changes the spectrum at
fixed r. A physical mass readout and three-generation identification are
separate assumptions, not consequences of this finite matrix family.

## Complex structure on the label doublet

Ps=(I+C+C²)/3 is the rank-one label singlet projector, Pd=I−Ps the
rank-two complement. J=(C−C²)/sqrt3 is real antisymmetric,
J²=−Pd,J⁴=Pd and[J,H]=0. On Pd it is a complex structure; on the whole
three-dimensional real space it has a kernel and is not a complex structure.
The rotation exp(sJ)=Ps+cos(s)Pd+sin(s)J preserves real volume and the
modulus of complex volume on Pd. These identities do not select a statistical
measure or a balance condition. The opposite orientation−J is also possible.

## Two different decompositions must not be conflated

The real group algebra R[C3] has central ideals R plus C, with projectors
Ps and Pd. But the previously used energies 3a² and 6|b|² are NOT the HS
energies of H restricted to these two central blocks. Writing b=u+iv,

    ||H Ps||_HS²=(a+2u)²,
    ||H Pd||_HS²=2(a-u)²+6v².

Their sum is 3a²+6(u²+v²). Neither is individually 3a² or 6|b|² in general.

Instead, the latter quantities arise from the orthogonal coefficient
subspaces span_R{I} and span_R{C+C²,i(C−C²)} in the Hermitian circulant
space. Define H0=aI and H1=bC+conjugate(b)C². Then

    ||H0||_HS²=3a²=:E0, ||H1||_HS²=6|b|²=:E1,
    Tr(H0 H1)=0.

Choosing the additional coefficient-energy balance E1=t E0 for t>0 yields
r=t/2 and Q_signed=(1+t)/3. The examples t=1,2,3/2 give 2/3,1,5/6.
This continuous family is not a binary exhaustive reduction. Calling t=1
'complex count' and t=2 'real count' is a proposed interpretation; it does not
follow from the central-idempotent decomposition or the existence of J.
Equal coefficient-space dimension weighting alone is not an ensemble,
expectation rule, or per-sample energy constraint.

## What remains open

A fixed H has fixed eigenvalues and fixed Q_signed; changing a balance changes
H in general. Counting cannot change that readout while keeping H fixed.
The algebra leaves the measure, balance principle, phase, physical mass map,
and underlying dynamics unspecified. A grading or index may be explored,
but is not proved to be the unique route or sufficient for these obligations.

Earlier no-go-route tables and the 'one counting bit' filename are historical
motivation. They do not supply a universal exclusion or physical default Q=1.
The valid content retained here is the matrix identities and the explicitly
supplied continuous coefficient-balance family. No claim that all invariant
forms, dynamics or possible readouts were exhausted is made.
