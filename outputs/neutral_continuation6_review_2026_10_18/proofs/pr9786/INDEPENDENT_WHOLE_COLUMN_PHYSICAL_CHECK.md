<!-- Original PR9786 source SHA256 61a71d0476416d49f762a702bc96b5edeb31d130fd0228983286ec0366488a44. -->
**Source boundary:** Complete mathematical argument follows. Historical verdicts, execution narratives and provisional instructions are provenance only. Exact identities and conditional mathematical implications remain live; no audit status or additional physical premise is conferred. Earlier exploratory statements are read with their explicit later corrections.

# Whole-column features: actual connected low-energy readout check

Focused independent check of the actual connected-readout argument in `/tmp/neutral_whole_column_root.md`. The separate rectangle-energy and many-spin quasimode construction is not rederived here. Inputs retained explicitly: the fixed-order local normal form, its positive wall/bad-plaquette lower bound, the exact P0 ground manifold of B_n, and locality/plane equivariance of the transformed source coefficients.

## 1. Ground approximation and the relevant gaps

Set r_n=||R_n||<=C_n V lambda^(n+1), and measure energies in units J. For even L~lambda^(-p), 0<p<4, the stated normal-form ground gap is g0>=c lambda^4 L. This is compatible with an order-one gap in every N>=1 sector and the order-lambda^4 L minimum bad-plaquette cost in N=0. The positivity proof must supply this actual ground gap; diagonality of N=0 by itself would not.

For any normalized exact ground state u of B_n+R_n, its ground energy epsilon satisfies |epsilon-Evac|<=r_n. The resolvent on P0-perp then gives

    ||(1-P0)u|| <= r_n/(g0-r_n).

This uses no equality of ground-space ranks. An arbitrarily small splitting within P0 can select a smaller exact ground space without spoiling the estimate. For n large enough and small lambda, r_n/g0=O(lambda^(n-3-2p)).

## 2. Source diagonality on the wall-free sector

Let D=C_n be the order-n transformed source polynomial. For fixed n and L eventually larger than all coefficient supports, a local term cannot change one N=0 aligned-column configuration into another: that would flip a complete column. Consequently Q0 D Q0 is diagonal. Plane equivariance and transitivity on P0 make its restriction there a single complex scalar c=c_Q (the source need not be Hermitian at nonzero Q). Thus

    Q0(D-c)P0=0.

The non-N-preserving terms of D are not being discarded; they are precisely what remain in Qh D P0, Qh=1-Q0. A claim that D is diagonal on the entire Hilbert space would be false and is unnecessary.

The source polynomial has global norm <=C_n sqrt(V), including the Q=0 case. The exact transformed-source remainder obeys ||C'-D||<=C_n sqrt(V) lambda^(n+1), as assumed from the prior local expansion. The scalar satisfies |c|<=||D||.

## 3. Cross-projection bound despite dense low N=0 levels

Let P be the exact spectral projector for (B_n+R_n)-epsilon in [0,1]. Its upper spectral endpoint is epsilon+1. On Qh, B_n has lower endpoint at least Evac+1.5 for small lambda. Thus the two operators have an ordered spectral separation at least 0.5-r_n, irrespective of how dense the N=0 spectrum is.

The cross operator X=P Qh obeys a Sylvester equation between the exact operator on Ran P and B_n on Ran Qh, with forcing P R_n Qh. For example, shifting by a number between their spectra and integrating the two decaying semigroups yields

    ||P Qh|| <= r_n/(0.5-r_n).

This is a dimension-free operator-norm bound. No gap within the exact low subspace, no nondegeneracy, and no rank matching are needed. The same statement in physical units has forcing J r_n and gap of order J, so J cancels.

## 4. Connected source and arbitrary exact ground

Write u=g+e with g=P0u. The previous steps give

    (C'-c)u = Qh D g + d,
    ||d|| <= C_n sqrt(V) [r_n/g0 + lambda^(n+1)].

Because g lies in P0, <g,Qh Dg>=0. Hence the expectation shift obeys

    |<u,C'u>-c| <= C_n sqrt(V) [r_n/g0 + lambda^(n+1)].

This establishes the centering correction explicitly; it is not necessary to assume the exact expectation equals c. Projecting the connected vector and using the cross-projection estimate yields

    ||P (C'-<C'>)u||
      <= C_n sqrt(V) [r_n + r_n/g0 + lambda^(n+1)].

Returning through U_n preserves this norm. The inclusion of the exact ground state in P is harmless: centering removes its self component exactly. Other degenerate ground components, if present, are covered by the same bound rather than silently excluded.

All constants are uniform in the choice of normalized exact ground vector. For a ground-supported density matrix, apply the same estimate to a pure-state decomposition and include the difference between each pure expectation and the common mixture expectation; both differ from c by the displayed uniform error. Thus the connected positive spectral weight bound extends to arbitrary ground mixtures. It is a bound on a positive structure/spectral measure, not an unqualified equality with a retarded response.

No translation eigenstate is required. Any allowed Fourier Q is covered, including Q=0 after centering. Plane equivariance supplies the common scalar; translation invariance of a selected pure ground is not used.

## 5. Exponents and all-algebraic statement

Using V~lambda^(-3p),

    sqrt(V) r_n/g0 = O(lambda^(n-3-(7/2)p)).

This dominates the other two displayed errors for p<4 and small lambda. Squaring gives a weight bound O(lambda^(2n-6-7p)). For n=40 the amplitude and weight exponents are 37-3.5p and 74-7p, respectively, as proposed.

For each desired fixed amplitude power K, choose a fixed integer n>K+3+3.5p. The normal-form construction and positive-gap statement must hold at that fixed n, with their n-dependent constants and small-lambda threshold. This proves all-algebraic smallness in the conventional sense, not convergence of the normal-form series or an optimized exponential bound. Taking n to grow with lambda without new estimates would be unjustified.

## Conclusion

The actual connected low-energy source bound is valid with the stated normal-form/gap inputs. Its Sylvester step remains valid in a dense low N=0 spectrum, and centering and arbitrary ground rank do not create an omitted contribution. The result is darkness of the specified original connected readout below a fixed order-one excitation cutoff on this volume family. It does not rule out the separately constructed macroscopic quasimodes, another detector operator, non-ground preparation, or other coupling/volume regimes.
