# Affected-only review of the REC tensor norm correction

**Confirmed: the correction resolves the Cartesian tensor boost constant
identified in [REVIEW_REC_LIB.md](REVIEW_REC_LIB.md).** This confirms only
the changed estimate and its affected quantitative dependencies. It is not a
fresh review or approval of the entire reconstruction library.

The checked [REC_LIB.md](REC_LIB.md) has SHA256
`90e38f069ee9d52c02bcef6024b579b95d752408267763cd6b446f96679f6533`.
The original source, SHA256
`79e570f5c21c0ceceb4dc076fabb1e7ce696afa1bbd4630da036456d3de53b13`, is
preserved at `8e9ab9cadbaa62f40beb7a64e68ff4c246d0011b`. I verified that the
sole change is exactly the paragraph replacement recorded in the
[coordinator receipt](checks/full_proof_rec_tensor_fix.json), and that the
initial 5,169 bytes remain identical, SHA256
`8c90178454da5d5a19643cf615105d5aef6d4ebf2bde7650b64098602102809c`.
This is a byte-preservation check, not a new investigation of the original
preregistration chronology. The earlier report remains unchanged, including
its HOLD against the original source.

For real `v` with `||v||2=1`, the four column sums of
`K(v)=[[0,v^T],[v,0]]` are `||v||1, |v1|, |v2|, |v3|`. Thus

    ||K(v)||1 = ||v||1 <= sqrt(3).

For every complex rapidity u, absolute convergence of the exponential
series and submultiplicativity give

    ||exp(uK(v))||1 <= sum_k |u|^k ||K(v)||1^k/k!
                    = exp(||v||1 |u|).

This is the specified fixed Cartesian induced norm, not a rotation-adapted
norm. For matrices A and B the absolute column sum of `A tensor B` at
column `(j,l)` is the product of the corresponding column sums, proving
`||A tensor B||1=||A||1||B||1`. A block diagonal direct sum has norm equal
to the maximum of its block norms. Therefore the finite direct sum of
Cartesian tensor powers of ranks `0<=r<=r_max` satisfies

    ||D_M(exp(uK(v)))||1 <= exp(r_max ||v||1 |u|),
    ||D_M(exp(uK(v)))^(tensor n)||1
        <= exp(r_max ||v||1 n |u|)
        <= exp(sqrt(3) r_max n |u|).

Rank zero, zero rapidity, and zero slots give the correct identity factors.
For a coordinate-axis direction `||v||1=1`, this recovers the earlier
`exp(r_max n |u|)` estimate. Inverses change u to −u, and `K(v)^T=K(v)`;
hence the same constants cover the inverse-transpose boost action on tests.
No complex spatial direction or arbitrary abstract representation is included.

I independently reconstructed the old counterexample analytically. For
`v=(3/5,4/5,0)` and `u=log 2`, `K^3=K` gives the vector boost

    [ 5/4   9/20    3/5   0 ]
    [ 9/20 109/100  3/25  0 ]
    [ 3/5   3/25  29/25  0 ]
    [  0      0      0    1 ].

Its absolute column sums are `23/10, 83/50, 47/25, 1`, so its induced norm
is exactly `23/10>2=exp(|u|)`. This refutes the original general-direction
bound already at rank one and one slot. The corrected directional bound is
`2^(7/5)`; indeed `(23/10)^5=6436343/100000<128=2^7`. This exact calculation
uses no floating-point sampling or numerical runner.

The unchanged adjacent estimates also match the stated norm: J, C and its
inverse are diagonal phases/signs of norm one; a four-dimensional real
orthogonal matrix has column l1 norms at most two, yielding the recorded
rotation factors. Finite component aggregation remains `m^n`. In section15,
the Wick/reflection identities, phase change of positive kernels, and
Lorentz representation (15.2) depend on those exact matrices, not on the
false constant. Their definitions and conditional domain clauses are
unchanged. L-LOCAL's imaginary boosts are coordinate-axis boosts, for which
the sharper constant is retained. The real arbitrary-direction boosts in
the spectrum and conditional mass-gap arguments remain finite Lorentz
transformations; replacing their finite component bound changes no
geometric domain or spectral premise. This checks effects of the correction,
not the complete proofs of those arguments.

I read the complete original review, the complete current tensor section15,
the actual L-BOOST and L-LOCAL passages, the norm and L-HILB chain-rule
conventions, L-ID/SPEC and L-GAP, and the assembled/open-residue clauses.
The [artifact/read receipt](checks/review_rec_tensor_fix_receipt.json) binds
those exact ranges, both source versions, the sole delta, and this report.
I did not rereview the whole REC source, its original chronology, REC_LIB_LOG,
external reconstruction literature, or the actual Yang–Mills producers.

The requested configuration remains Astra/max; independent backend metadata
is unavailable, and no cross-family independence is claimed. The already
read review-loop/physics-loop procedures at immutable current-main
`ca2bc7ddf64790da96cd43d42017d000fbfe4808` govern this affected pass. I edited
only this report and its own receipt artifacts. The earlier covariance
review packet and the original REC review were left untouched.

There are no remaining findings in this correction. R-CONT, the general
abstract tensor bridge, unconditional moment production, actual Yang–Mills
reconstruction, and the physical continuum mass gap remain OPEN. No whole-PR,
audit, retention, or reconstruction-completion verdict is issued.
