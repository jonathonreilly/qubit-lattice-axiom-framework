# Native compass spatial correlation hierarchy — independent check

I independently reconstructed the local derivative using binary symplectic Pauli masks and integer coefficients. This does not import the root's multiplication-table functions. Coordinates are embedded injectively in [−5,5]^3 only for bit indexing; there are no periodic identifications or boundary truncations. Starting from neighbors at distance1, four nearest-neighbor commutators cannot leave this box, and the code computes no further derivative. Code/results: `independent_transport.py` and `independent_transport.json` in this pack (output destination adapted; algebra unchanged).

## Exact results

For D=i[H,.], K=1, C0=sum_a sigma_(−e_a)^a sigma_(+e_a)^a, all term counts and translation overlaps agree with the root:

| n | terms in D^n C0 | onsite squared norm | offsite overlaps |
|---|---:|---:|---|
|0|3|3|none|
|1|24|96|none|
|2|207|9216|none|
|3|1704|1499136|none|
|4|14427|352124928|six nearest neighbors, each247808; twelve face diagonals, each16896|

All values are exact integers. Here overlap at r means tr[(D^n C0)(D^n Cr)] in the normalized tracial state, with Hermitian inputs. Consequently

    m6=1499136/3=499712,
    m8(q)=[352124928+495616 sum_a cos(q_a)
                 +67584 sum_(a<b)cos(q_a)cos(q_b)]/3.

The denominator3 is the q-independent zeroth structure norm per cell. The cosine factors count both directions of each nearest-neighbor displacement and all four sign choices of each face diagonal. Restoring H=K H1 multiplies m_(2n) by K^(2n).

## Sign and odd orders

D is skew-adjoint in normalized HS inner product, since [H,.] is self-adjoint and D=i[H,.]. Therefore

    tr[(D^(2n) Cr) C0]=(-1)^n tr[(D^n Cr)(D^n C0)].

All odd translation moments vanish. One direct structural proof uses Pauli-word weight parity: commutating a two-site Pauli bond with an anticommuting word changes its weight by +1 or −1. Hence D flips weight parity. C contains only weight-two words; D^(odd)C has odd weights and is orthogonal to any translated C. The same follows from the declared T-even C, T-even H and tracial time-reversal invariance. Odd moments cannot hide an earlier overlap between the reported even orders.

## What the time-domain result actually establishes

Define the unnormalized-in-C, normalized-in-Hilbert-space unequal-time correlation

    S_r(t)=tr[C_r(t) C0], C_r(t)=exp(tD) C_r.

At nonzero r there is no zeroth-order correlation, all odd terms vanish, and the computed even terms through t6 vanish. At nearest neighbors and face diagonals,

    S_r(t)= K^8 c_r t^8/8! + O(t^10),
    c_nearest=247808, c_face=16896.

For S_r/3, divide these coefficients by3. The sign is positive because n=4. For finite-range bounded spin interactions, the needed local time derivatives exist; Taylor's remainder justifies this local asymptotic. A positive leading coefficient proves nonzero unequal-time overlap for sufficiently small nonzero t. The computation has not supplied a numerical time interval where a remainder bound is smaller than the leading term.

This is a real spatial operator-correlation result in the existing unperturbed Hamiltonian. It does not require adding a physical interaction. It is not a change of equal-time tracial correlations: tr[C_r(t)C0(t)] is unchanged by unitary evolution. It also does not yet determine a propagation velocity, an isolated pole, a scalar field equation or electromagnetic/cosmological coupling.

## First high-temperature retarded coefficient

For the convention in the root's question,

    chi_r(t)=i theta(t)<[C_r(t),C0]>_beta,

corresponding to a linear probe perturbation −f(t)C0, expand the normalized Gibbs state about beta=0. Trace cyclicity gives

    chi_r(t)=−i beta theta(t) tr[H[C_r(t),C0]]+O(beta²)
            =−beta theta(t) S'_r(t)+O(beta²).

Thus the first beta coefficient has

    chi_r(t)=−beta theta(t) K^8 c_r t^7/7!
                 +O(beta t^9)+O(beta²),

with the last remainder interpreted at fixed t. At exactly beta=0, retarded response is identically zero even though S_r(t) is nonzero. The high-temperature expansion is a state/preparation assumption, not an inferred physical temperature.

Important ordering caveat: this is the leading time term in the **linear-in-beta coefficient**. Higher beta orders can have lower powers of t. Without checking them, do not call t7 the leading short-time behavior of the full response at a fixed nonzero temperature. Likewise, introducing a formal probe source to define response is not an autonomous added microscopic interaction in the unperturbed model.

## Jacobi coefficients

For the symmetric HS structure measure normalized by m0=1, its odd moments vanish, so the Lanczos/Jacobi diagonal coefficients are zero. Writing a=b1²,b=b2²,c=b3²,d=b4², the moment identities give

    m2=a,
    m4=a(a+b),
    m6=a[(a+b)²+bc],
    m8=a^4+3a³b+3a²b²+2a²bc+ab³+2ab²c+abc²+abcd.

At K=1, the first three squared coefficients are32,64,100, and the last identity becomes

    m8=88113152+204800 b4².

Substitution of the independently checked m8(q) gives exactly

    b4²=3572/25 +(121/150)sum_a cos(q_a)
                    +(11/100)sum_(a<b)cos(q_a)cos(q_b).

All four b_j² acquire the common factor K² when K is restored. These are finite hierarchy coefficients, not an inferred isolated-mode dispersion. Momentum dependence first appearing at this hierarchy depth establishes spatial structure of the operator spectrum without determining a scalar pole.
