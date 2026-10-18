# Focused check: uniform compressed few-spin bound

A quadratic-form argument gives the requested O(L) operator bound without a local matrix-entry 1-norm or an exponential support-dimension factor.

## Required local decomposition

Write the fixed-order Hermitian coefficient as D_n=sum_X d_X with each d_X Hermitian, supported on X, and commuting with H0. Such a decomposition can be obtained by applying the zero-frequency H0 filter term by term to a Hermitian local decomposition: because [D_n,H0]=0, its sum is unchanged. For commuting longitudinal H0 bonds, conjugation/filtering enlarges a support only by the neighboring longitudinal spins needed by the incident bonds. A fixed-order finite-range coefficient remains finite range; a suitable quasilocal interaction norm is likewise preserved up to fixed support/decay constants.

Assume the all-up reference has no distinct zero-energy configuration reachable by an operator supported on X. This holds for finite supports on the infinite longitudinal lattice or with fixed-up longitudinal exterior. It also holds for finite periodic systems when each relevant support cannot wrap an entire longitudinal column. It does not hold automatically for arbitrary supports on a finite periodic system, since whole-column flips are degenerate with the vacuum; those wrapping terms need separate treatment.

Under this assumption, [d_X,H0]=0 implies d_X|Omega>=c_X|Omega>. Since d_X is supported on X, its local all-up vector is an eigenvector. Set b_X=d_X-c_X I_X and Q_X=I_X-|up_X><up_X|. Hermiticity then gives the exact annihilator identity

b_X=Q_X b_X Q_X,  ||b_X||<=2||d_X||.

It is crucial to filter the individual terms, or otherwise establish this identity. Commutation of the total sum alone would not suffice.

## Quadratic-form estimate

Let n_i=(1-Z_i)/2 count down spins and Ndown=sum_i n_i. Since Q_X projects onto at least one down spin in X,

Q_X <= sum_(i in X) n_i.

For any vector psi,

|<psi|sum_X b_X|psi>|
<=2 sum_X ||d_X|| <psi|Q_X|psi>
<=2 a_0(D_n) <psi|Ndown|psi>,

where a_0(D_n)=sup_i sum_(X containing i)||d_X||. The same inequality holds in finite volumes with the same interaction bound. In infinite volume it defines the vacuum-subtracted form on finite-excitation vectors; the extensive scalar sum itself need not be assigned an independent infinite value.

Let P_L project onto the stated compact E8 configurations with two columns sharing an interval of length at most L, or onto any subspace with Ndown<=2L. Then

||P_L (D_n-Evac,n) P_L|| <= 4 L a_0(D_n).

This is a bound on the full Hermitian compressed operator, not merely its diagonal. It handles arbitrary coherent superpositions of configurations and is independent of spatial volume. If the adopted a_mu includes a positive exponential weight, a_0<=a_mu. No factor 2^|X| appears, because the proof uses operator norms and positive projectors rather than absolute matrix-row sums.

## Fixed-order tail and limits

For a fixed finite truncation order m and sufficiently small lambda,

||P_L sum_(k=5)^m lambda^k(D_k-Evac,k) P_L||
<=4 L sum_(k=5)^m |lambda|^k a_0(D_k)
=O_m(|lambda|^5 L).

At L=O(lambda^(-2/3)), this is O_m(lambda^(13/3)) as a compressed coefficient bound. Constants may depend strongly on m; this does not justify summing an infinite perturbation series.

The argument does not bound the uncompressed leakage norm ||(1-P_L)D_n P_L||, does not control the actual SW remainder outside E8, and does not establish a resonance weight or long-time correlation approximation. It also does not include states with macroscopic column flips or a different asymptotic reference. Exact finite-order locality avoids periodic wrapping once the longitudinal circumference exceeds the fixed support bound; genuinely quasilocal wrapping tails require an explicit separate estimate rather than being silently treated as vacuum-annihilating terms.

## Extension: exact control of length-cutoff leakage

The proposed extension is valid for the exact fixed-order canonical coefficient. Each order-n word has n transverse V insertions, so it changes at most 2n spins. It preserves E8 and the relative parity of every longitudinal plane. Within the finite-excitation reference sector these constraints classify its output as another matching two-column interval. Starting with ell<=L, its down-spin count is at most 2L+2n, so its output interval has ell'<=L+n. Therefore

(D_n-Evac,n)P_L = P_(L+n)(D_n-Evac,n)P_(L+n)P_L,

and the previously proved compressed bound gives

||(D_n-Evac,n)P_L|| <=4(L+n)a_0(D_n).

Here P_L must include all compact E8 configurations up to that length, including every allowed transverse column pair. It cannot mean only the active axial arm or one selected channel.

For a finite sum through order m, the output lies in P_(L+m), and summing the individual bounds yields

||sum_(k=5)^m lambda^k(D_k-Evac,k)P_L||
<=4 sum_(k=5)^m |lambda|^k (L+k)a_0(D_k)
=O_m(|lambda|^5(L+m)).

Thus this controls leakage across the chosen length cutoff as well as the compression. It supersedes the earlier statement that such leakage was unbounded by the form estimate alone: the added exact flip-support property supplies the missing step. The actual SW remainder need not preserve E8 or have a finite insertion count and remains uncontrolled by this argument. The finite-excitation reference and periodic-wrap qualifications also remain unchanged.
