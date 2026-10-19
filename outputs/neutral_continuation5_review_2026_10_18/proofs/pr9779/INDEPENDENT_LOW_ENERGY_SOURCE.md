<!-- Original PR9779 source SHA256 48e9957bb3cd1639051b4140c2ca6883ce331781ee4dadcaf2878b7a09fab7be. -->
**Source boundary:** Complete mathematical argument follows. Historical verdicts, execution narratives and provisional instructions are provenance only. Exact identities and conditional mathematical implications remain live; no audit status or additional physical premise is conferred. Earlier exploratory statements are read with their explicit later corrections.

# Original Fourier source on the low-energy band: independent check

Disposition: PASS with the local-decomposition conventions below, and one explicit extension needed when applying the lemma to unprojected quasimodes. Read /tmp/neutral_low_energy_source_root.md and reused the termwise construction in native/MICROSCOPIC_GROUND_WINDOW_PROOF.md. No shared/canonical edits.

## Diagonal sampled functional and energy control

The existing decomposition can be used as B-Evac=2N+F+W. Take F to be the SUM of the wall-free sampled diagonal terms after common anchor-slice grouping and vacuum subtraction. Its leading order-four plaquette term and the pointwise higher-order bound give F>=c lambda^4 Pbad>=0. Individual sampled summands need not be positive; the claim is for their grouped sum. The remainder W is N-preserving and obeys |<psi,Wpsi>|<=C lambda<psi,Npsi>. Since it is Hermitian and preserves N, its norm on N<=n* is at most C lambda n*.

On the coefficient low-energy projector Q_B, the positive form bound and [B,N]=0 force N<=n* with n* fixed. Also 0<=B-Evac<=E* on this projector. Therefore

 ||F Q_B||<=E*+2n*+C lambda n*=O(1).

F and Pbad are pointwise diagonal. Their pointwise inequality consequently implies ||Pbad Q_B||<=C lambda^-4 ||F Q_B||, even though Q_B need not commute with F. This is a valid vector-norm upgrade; a mere expectation bound without diagonal domination would not suffice.

## Source-grade counts

For a nonzero allowed Fourier momentum, the scalar vacuum Fourier sum vanishes. The bare distance-two readout differs from its uniform value at no more than 2N bonds. Each difference has magnitude 2, giving ||C_Q P_(N<=n*)||<=4n*/sqrt(V).

For each finite local dressed-source coefficient, filter into N grades and include incident vertical neighbors in the support. The commuting-N filter and plane averaging preserve bounded locality, as in the earlier proof. For a positive grade, a configuration has at most O(V) possible translated outputs, while each output of bounded N has only O(n*+j) reverse transitions: removing walls requires touching an existing broken bond. Fixed local support bounds the number of spin patterns per translate. The absolute row/column Schur bound is therefore O(sqrt(V)) before the Fourier normalization. Negative grades have the exchanged estimate. The same argument is valid for complex Fourier phases because it uses absolute values, and does not require Hermiticity of an individual grade.

For grade zero, the wall-supported remainder t-f_t=Q(t-f_t)Q has at most O(n*) relevant anchors in either row or column. Its normalized norm is O(n*/sqrt(V)). The sampled diagonal part obeys a pointwise absolute bound by C Pbad after its constant Fourier contribution cancels. Thus its action on Q_B is O(lambda^-4/sqrt(V))=O(lambda^2). Multiplication by source order lambda^j, j>=1, makes this O(lambda^3). The nonzero grades dominate with O(lambda). The fixed finite sum through order40 and the global O(lambda^35) tail give

 ||C'_Q Q_B||<=C lambda.

The identical estimate holds for C'_-Q=(C'_Q)^dagger. Constants depend on the fixed cutoff/order, not on V or the allowed Fourier momentum. At Q=0 one must subtract the extensive vacuum scalar explicitly; the stated uncentered nonzero-Q lemma should not silently include Q=0.

## Transfer to the actual low-energy subspace

With coefficient cutoff 30 and actual cutoff 24 (in Jz units above their respective ground energies), the spectral sets are separated by a fixed gap after accounting for Eg-Evac=O(Jz lambda^29). The bounded perturbation R has global norm O(lambda^29). The standard separated-spectral-subspace/Sylvester estimate gives leakage O(lambda^29), independently of the dimensions of the two projectors. Multiplying by the global source norm O(sqrt(V))=O(lambda^-6) costs O(lambda^23). Hence

 ||C_Q P_H,low||<=C lambda,
 ||C_Q^dagger P_H,low||<=C lambda.

This is an operator bound on the whole low-energy band, not only on exact ground vectors. It does not require that the band consist of isolated particles or one symmetry background.

## Application to projected quasimodes

One must also establish ||C Xi1||=O(lambda) for the UNPROJECTED first quasimode; it does not follow solely by applying the low-band bound to a vector with O(lambda^2) spectral leakage, because the global source norm would be too large. The same proof does supply it directly in the intended construction: in the normal-form frame Xi1 has bounded N and ||(B-Evac)Xi1||=O(1) from its coefficient residual. The equation F=B-Evac-2N-W then gives ||F Xi1||=O(1), and all source-grade estimates above apply unchanged. Thus state this stronger input explicitly rather than infer it from an actual-band projection. The dressed trial used previously satisfies it.

Let e_i=(1-P_i)Xi_i, with ||e_i||=O(lambda/delta). Then the exact decomposition

 <Xi2,C Xi1>-<P2 Xi2,C P1 Xi1>
 =<e2,C Xi1>+<P2 Xi2,C e1>

bounds the error by O(lambda^2/delta), using ||C Xi1||=O(lambda) and ||C^dagger P2||=O(lambda). There is no uncontrolled double-error term. Normalizing P_i Xi_i changes the matrix element by an additional O(lambda*(lambda/delta)^2), which is smaller in the proposed regime.

Conditional on the separately established unprojected two-rung vertex sqrt(2)lambda sqrt(W0 delta)log(1/delta), the relative projection error is O(lambda/[delta^(3/2)log(1/delta)]). Thus alpha<2/3 transfers a nonzero matrix element to normalized states in the two actual energy windows. The source-bound lemma does not itself prove the two-rung vertex or its combinatorial normalization. The conclusion concerns spectral-window vectors; no isolated eigenstates, stable particles, lifetime, or full-H ladder algebra follows.
