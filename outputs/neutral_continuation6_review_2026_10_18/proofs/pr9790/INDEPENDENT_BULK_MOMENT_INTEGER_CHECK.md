<!-- Original PR9790 source SHA256 9dfdab1c97336f99bea908d5bb376267808b1b9c72251a4feedfab8236239fdf. -->
**Source boundary:** Complete mathematical argument follows. Historical verdicts, execution narratives and provisional instructions are provenance only. Exact identities and conditional mathematical implications remain live; no audit status or additional physical premise is conferred. Earlier exploratory statements are read with their explicit later corrections.

# Independent native slab moment and integer-Pauli check

Reviewed the two scratch integer scripts and native `BULK_SLAB_RESPONSE_PROOF.md`, including its first-moment argument. No repository edits or formal audit. Independent scratch implementation: `/private/tmp/neutral_bulk_moment_independent.py`, with output `.json`.

## 1. Independent local algebra

The root X^x Z^z multiplication sign (-1)^(z dot x') is correct. Its commutator coefficient is 2ab when z dot x' is even and the reverse sign is odd, and -2ab in the opposite case. Thus the root integer implementation has the correct sign and factor two.

I independently used infinite integer lattice coordinates, Hermitian single-site X/Y/Z labels, and the explicit multiplication table XY=iZ, YZ=iX, ZX=iY with reversed signs in the opposite order. For each word, only native bonds/plaquettes meeting its support were generated. No periodic lattice, modulo coordinates, or XZ-bit sign implementation was reused.

Starting from the two positive-direction Z edges at the origin, three commutators with K=-5E-4P give word counts 8, 76, 524. The final commutator with E gives 3336 nonzero Hermitian Pauli words. Its coefficient absolute sum divided by two is exactly 9,003,008. All final coefficients are real integers. This reproduces the proposed bound independently.

Every coordinate in the union of final supports lies in [-4,5] in each axis. Therefore a sufficiently large torus, in particular R>=13, introduces no local identification in this expression. The R9 agreement alone would not be the proof of no-wrap locality; the infinite-coordinate calculation supplies it.

## 2. Moment identity and bound

For a ground vector g with energy e0, the positive excitation measure of E satisfies

    M3=<E(K-e0)^3 E>
      =(1/2)<[E,[K,[K,[K,E]]]]>.

The sum of translations of B0=(1/2)[E,[K,[K,[K,E0]]]] is exactly the operator on the right, since sum_translates E0=E. Each Pauli word has operator norm one, so ||B0||<=9,003,008. Translation invariance of the state is not needed for the norm sum; it gives M3<=9,003,008 N for any ground state to which the excitation-moment identity applies.

A separate dense R3 physical coefficient-model control gave spectral M3=2271921.2605029508 and nested-commutator expectation 2271921.2605029405, relative discrepancy about 4.6e-15. R3 is only a sign/factor control, not a use of the R>=13 local bound.

## 3. First-moment lower bound checked

In the selected positive row/column block the connected plaquette-flip graph has a strictly positive ground. For fixed plaquette p, set r(s)=a(ps)/a(s). At a minimizing configuration, subtracting the two ground equations gives precisely

    [D(ps)-D(s)] r(s)
       =h sum_q [r(qs)-r(s)] a(qs)/a(s).

The q=p term equals h(1-r(s)^2); all other terms are nonnegative. Reciprocity r(ps)=1/r(s) ensures the minimum is <=1. The eight boundary edges give |D(ps)-D(s)|<=16g, hence

    r(s)>=m=2h/[sqrt((16g)^2+4h²)+16g].

No Gaussian, clustering, or small-h premise is used. With Bp the sum of the eight boundary Z-edge products,

    M1=(h/2) sum_(p,s) a(s)a(ps)[E(ps)-E(s)]²
       >=2hm sum_p <Bp²>.

The all-plus diagonal-basis configuration has trial energy -2gN. Combining the variational bound with <P><=N yields <E>>=N(2-h/g). Every edge occurs in exactly four plaquette boundaries, so sum_p Bp=4E. Two applications of Cauchy/Jensen then give

    sum_p <Bp²> >=16<E>²/N
       >=N(8-4h/g)²,

where h/g<2 permits the last squaring. Thus a=2hm(8-4h/g)²=9.193074485002494 is valid at g=5,h=4. The use of a positive ground in this block is essential to this proof; extension to every global ground relies on the separate already stated response-equivalence result.

## 4. Spectral inequalities and numerical constants

Holder gives M1<=M0^(2/3) M3^(1/3). Combining M1>=aN and M3<=bN yields

    M0/N >= a^(3/2)/sqrt(b)=0.009289607191145714.

The tail first moment above Omega obeys M1(omega>Omega)<=M3/Omega². At Omega=sqrt(2b/a)=1399.5177997395106, the remaining first moment is >=aN/2. Dividing by Omega gives

    mu_E((0,Omega])/N >=0.003284372119709225.

These inequalities remain useful even if a separate zero-frequency elastic contribution exists: the positive-window bound follows directly from M1 and M3. In the unique selected-block ground, the connected E source has no same-block elastic component, giving the stated variance interpretation.

The original coefficient source O=3K-3E has connected ground vector -3(E-<E>)g, hence its positive measure is nine times mu_E. In microscopic normalization C_eff=lambda^4 O/(128 sqrt(V)), V=4N, the bound on the normalized C window is lambda^8 times 9/(4*128²) times the displayed E-density constant. There should be no additional division by area after this normalization. The coefficient O weight itself is extensive.

## Conclusion

The integer norm bound, no-wrap locality, first-moment lower bound, and positive-window inequalities check out. This is a nonzero integrated response density at the native coefficient ratio, without the auxiliary small-u expansion. It does not locate a sharp line, provide a positive lower frequency edge, or establish a uniform joint microscopic lambda/area limit.
