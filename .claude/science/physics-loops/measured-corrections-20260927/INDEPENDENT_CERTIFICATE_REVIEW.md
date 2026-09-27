# Independent finite-case spectral certificate review

**Disposition:** the finite-spin and infinite-rotor enclosures are supported for the specified cases. No material defect was found in eliminated-block positivity, positive Schur scaling, global spectral indexing within the supplied two-positive-record sector, or the rotor-tail negative-index sandwich. This is a selective independent certificate check, not a formal repository audit or a uniform asymptotic theorem.

## Finite-spin argument

The dimensionless eliminated block is Q(H−lambda)Q with diagonal blocks (1−lambda)I and (2−lambda)I and off-diagonal sqrt(x)B. The conditions lambda<1 and (1−lambda)(2−lambda)>4x imply positive definiteness because BB*=4diag(d_m), 0<=d_m<=1. This does not assume positivity of the full Hamiltonian or that a chosen eigenvalue is already in the low branch.

Its Schur complement, multiplied by delta(1−lambda)/x², is exactly the stated F(E). This factor is positive under the checked conditions, so it preserves inertia. Block congruence then says the negative count of F(E) is the negative count of the full finite H_phys−E. Thus the accepted counts are global labels in this fixed matter/charge sector, rather than labels assigned by a floating root guess. They are not labels across unrelated matter or charge sectors.

The two exterior d coefficients vanish at the actual finite-spin endpoints. The author's diagonal formula includes them with zero numerator and positive denominator; the independent reconstruction omits the nonexistent W2 rows entirely and gives the same result. The rational LDL recursion computes inertia correctly whenever its nonzero-pivot requirement holds. All inputs to the accepted arithmetic are Fraction values or integers. Trial energies originated in floating calculations, but conversion to rational endpoints and exact recounting remove reliance on the proposal's numerical accuracy.

## Infinite-rotor argument

For K,delta>0, the excluded diagonal is at least 4K(L+1)²−4delta. The norm of its hopping part is at most 4delta, giving the declared tail lower bound t_L. For E<t_L the tail resolvent is a bounded positive operator. The two disjoint half-lines couple to two distinct retained boundary sites, so B*B=4delta² Pi_boundary and 0<=Sigma(E)<=4delta²/(t_L−E) Pi_boundary. This use of distinct sites requires L>=1, satisfied by L=20.

The unbounded diagonal has compact resolvent; bounded hopping preserves it. Schur form factorization with the positive, invertible tail block therefore preserves the finite negative index. The operator-order sandwich is in the correct direction: subtracting the largest allowed boundary term gives the largest possible negative count. If the two rational finite comparison counts coincide, the true count equals them. Nonzero leading pivots also ensure neither comparison matrix is singular; coincident counts then place zero strictly outside the corresponding ordered-eigenvalue bounds of the exact finite Schur operator. This justifies strict enclosure, not merely a weak endpoint inequality.

## Fresh evidence and independent reconstruction

Both author certificate scripts were freshly rerun. All six finite-spin records (S20,50,120 at both rational parameters) and both rotor records reproduce their saved rational intervals exactly, ignoring elapsed-time metadata. These reruns test reproducibility, not independence of implementation.

The separate `independent_certificate_check.py` imports no author code. For finite S20, K=1, delta=15803623/500000 it constructs F(E) from explicit W2 row outer products Z*R^-1Z. It then counts sign changes of exact leading principal determinants, avoiding the author's LDL pivot-division implementation. All fourteen endpoint counts are [j,j+1], j=0…6. For the infinite rotor, the same independent determinant recursion checks both boundary comparison matrices at all twenty-eight endpoints across both delta values. Every count agrees. It also independently checks energy widths 2e−9 and the gap-subtraction arithmetic producing widths 4e−9.

Fault injections against the frozen correct intervals were rejected:

- Moving the finite-spin ground bracket upward by 0.001 gives counts [1,1], not [0,1].
- Reducing its Schur off-diagonal magnitude by 1% gives [0,0].
- Reducing rotor hopping magnitude by 1% gives [0,0] at the original ground bracket, for both delta values.

These tests show sensitivity to those specified faults. They do not establish detection of every coefficient error, especially a coherently changed model and freshly changed brackets. Correct operator reduction remains load-bearing evidence.

Fresh outputs are `independent_certificate_check.json`, `independent_fresh_finite_certificate.jsonl`, and `independent_fresh_rotor_certificate.jsonl`. The independently reconstructed finite case is S20 at the larger ratio; the S50/S120 counts were freshly rerun through the reviewed author implementation, not independently reimplemented for those sizes.

## Limits

The accepted claims are finite-case energy and gap intervals for exact rational mathematical parameters in the supplied closed square model and its infinite scalar-rotor reference. Exact rational arithmetic here is a checked Python computation, not a proof-assistant or hardware-verification certificate. The source prerequisites include integer spin, the two-positive-record Gauss sector, closed kappa=0 specialization and zero offset. The code is scoped to the declared positive Fraction inputs and L20; it should not be treated as a general validated API for arbitrary argument types or L=0.

Nothing in these counts proves a uniform O(x²) remainder, certified perturbation coefficients, physical uncertainty bounds, empirical calibration, or a resonator/preparation/readout map. A rigorous finite-case difference interval can be formed by interval subtraction, but an asymptotic conclusion requires additional estimates. No author file was edited, publication attempted or audit status assigned.

## Exact checked source identities

- `SPECTRAL_CERTIFICATES_DRAFT.md`: `31c9be4c0369a7ebda425823d19fd253b8d0161d0403b21e218be4dd6ee6eec7`
- `rational_spectral_certificate.py`: `6e788389854ff64be410b78127b88ec73af99b654ae83b502e29fac71ece662d`
- `rotor_tail_certificate.py`: `1f88a9489f8bb555d67943a0d82c41b1c93e7b746262c1faf580252cfb417fed`
- `rational_spectral_certificate.jsonl`: `cca2365d0e2a88a7d12c1ee1bff4d7b9a9a247637cbe575ae7b501643290ed18`
- `rotor_tail_certificate.jsonl`: `a4f2928393227d140eaa8f9083eabc887e426b53ed304b7a6e519557f9d8bc8a`
- `EXACT_SCHUR_AND_CALIBRATION_DRAFT.md`: `3e08732c58187985cf3a132c5ef3ba60072264e3ef2f8b5c8225e14de4f91f2e`
- `exact_schur_square.jsonl`: `f4c33bfa645c125f05b7340cde43a69aa03482ebfbf1d1494cdeed7e7f258cb5`
