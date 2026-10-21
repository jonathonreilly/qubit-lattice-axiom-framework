<!-- Owning original: PR9752; source SHA256 e01e6e5160c07d2b20295d5d102d207a4ffa40032aaf98de0ffe344eff3bcb8a. -->
**Source boundary:** Complete mathematical source follows. Original review dispositions, execution stories, provisional questions and PASS labels are historical annotations, not current certification. Later explicit addenda supersede earlier provisional statements. Mathematical hypotheses and conclusions are retained; terminal exclusion interpretations require separate admission and are not promoted by this source enclosure.

# Independent conserved-energy and source-overlap check

Checked 2026-10-18. State is the supplied normalized infinite-temperature trace unless explicitly stated otherwise. No retarded response, ground state, or cosmological state is inferred from that choice.

## Energy fluctuation moments

For bond-center E_q=V^(-1/2) sum_b exp(-iq r_b) h_b, distinct two-site Pauli strings give m0=sum_a J_a^2. Only incident perpendicular bonds anticommute. For each site and unordered axis pair there are four such pairs. Their commutators have magnitude 2J_aJ_b and distinct three-site strings. Summing the four squared phase differences gives 8[1-cos(q_a/2)cos(q_b/2)]. Therefore

    m2=32 sum_(a<b) J_a^2 J_b^2
           [1-cos(q_a/2)cos(q_b/2)].

The stated expansion and isotropic m2/m0=(8/3)J^2 |q|^2+O(q^4) follow. On large periodic lattices the Fourier convention is understood consistently across the boundary; local support counting has no short-wrap alias for lengths at least five.

The normalized positive HS spectral measure consequently concentrates in shrinking windows |omega|<=J |q|^alpha, 0<alpha<1. This proves low-frequency fluctuation weight and slow operator variation, not a sharp pole, sound speed, diffusion constant, or nonzero beta=0 retarded susceptibility.

## Exact Q norm and conserved fraction

Using Q=sum_a [H_a,[H,H_a]], the known local expression yields the two-spin part -32J^2 H and 36V distinct four-spin strings, each coefficient magnitude 8J^3, on a non-aliased cubic lattice. The latter consist of 12V same-end/T-shaped strings and 24V cross-end strings. They are orthogonal to all two-spin bond strings. Thus

    <H^2>/V=3J^2,
    <Q H>/V=-96J^4,
    <Q^2>/V=3072J^6+2304J^6=5376J^6.

The projection of Q onto conserved H has weight per site 3072J^6, giving the exact fraction 4/7 of the total HS norm. This is a lower bound on the total zero-frequency weight, since other conserved components can exist. At q=0 the remainder orthogonal to H stays orthogonal dynamically because H is conserved.

Independent `/private/tmp/neutral_energy_source_independent.py` constructs nested commutators directly with binary physical Pauli strings. Exact L5 and L6 calculations give 39V total strings (3V two-spin, 36V four-spin), norm/site5376, QH/site-96 at J=1, and fraction4/7. Output is `/private/tmp/neutral_energy_source_independent.json`.

## Finite-q source proposed by root

Define H_(a,q) with the same bond-center Fourier normalization and Q_q=sum_a[H_a,[H,H_(a,q)]]. The only two-spin term arises when the outer a-bond equals the inner a-bond. Its contribution is -4J_a^2 h_b times the inner phase. Around a fixed b-bond, its four adjacent a-bond phases sum to

    4 exp(-iq r_b) cos(q_a/2) cos(q_b/2).

Consequently the two-spin coefficient multiplying h_b is

    -16 sum_(a!=b) J_a^2 cos(q_a/2) cos(q_b/2),

and the exact overlap ratio is

    g(q)=<E_q,Q_q>/<E_q,E_q>
        =-32 sum_(a<b) J_a^2J_b^2 cos(q_a/2)cos(q_b/2)
          /sum_a J_a^2.

At q=0 isotropy this reduces to -32J^2. At nonzero q the full two-spin part need not be proportional to E_q; an additional orientation-dependent orthogonal bond component is allowed. Q_q dagger=Q_-q. Because its real-space density has finite support, its HS norm per Fourier mode is a finite trigonometric polynomial and therefore tends continuously to5376J^6 as q->0.

To transfer energy's low-window concentration to Q, let P be the Liouvillian spectral projection onto that window. Cauchy-Schwarz gives

    ||P Q_q|| >=
      (|<E_q,Q_q>|-||(1-P)E_q|| ||Q_q||)/||E_q||,

when the numerator is positive. Thus the limiting low-window fraction of Q_q is at least4/7 in the isotropic case. One must use such an inequality rather than assume that an orthogonal remainder at finite q cannot interfere inside a spectral window. No isolated mode is implied.

## Original C_z at high temperature

For C_z=sum_r Z_r Z_(r+2e_z), distinct Pauli support makes <C_z H>_0=0. In H^2 each length-two z path occurs in two orders; it multiplies to the corresponding C_z string with coefficient J_z^2. Hence

    <C_z H^2>_0/V=2J_z^2,
    <C_z>_beta/V=beta^2 J_z^2+O(beta^3).

Differentiating the Gibbs expectation with respect to beta gives exactly minus Cov_beta(C_z,H), because H commutes with the Gibbs state. Therefore

    Cov_beta(C_z,H)/V=-2beta J_z^2+O(beta^2),
    Var_beta(H)/V=sum_a J_a^2+O(beta),
    g_C(beta)=-2beta J_z^2/sum_a J_a^2+O(beta^2).

These signs, factors, and units agree with the draft. Since Var_0(C_z)/V=1, the corresponding leading conserved energy fraction is 4beta^2 J_z^4/(sum_a J_a^2)+higher orders, equal to (4/3)beta^2 J^2 at isotropy. This differs from the sum-over-all-directions C, whose leading projection coefficient is -2beta.

These Taylor coefficients are exact finite-volume local counts. Uniform thermodynamic remainders require a high-temperature convergence/clustering argument. Small odd-period tori can have extra higher-order winding terms; the displayed loose error orders remain appropriate. The Gibbs state, temperature, and operational identification of C_z remain supplied inputs. C_z is directional and need not be a cubic scalar.

Conclusion: the fluctuation concentration and Q/energy overlap are constructive exact statements in the supplied state, with exact Q fraction4/7. They do not derive the physical detector/environment bridge or replace the need for a state-selection argument.
