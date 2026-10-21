<!-- Original PR9773 source SHA256 028012faa66d9c4dc7b109b68a93c3c1fdf2efda13a5d08944cca3d3177e10a1. -->
**Source boundary:** Complete mathematical argument follows. Historical verdicts, execution narratives and provisional instructions are provenance only. Exact identities and conditional mathematical implications remain live; no audit status or additional physical premise is conferred. Earlier exploratory statements are read with their explicit later corrections.

# Four-column finite interval: separated-end channel check

Scope: four specified adjacent columns in an up exterior, each occupied on [l_c+1,u_c], within the original wall-conserving first-order coefficient. The supplied single-interface band epsilon(k)=-8cos(k/2)/sqrt(3) is used as an input. The result below does not certify an invariant paired-end subspace or a physical pole.

## Exact separation condition

For the lower boundary, wall-preserving flips occur at z=l_c (extension downward) or z=l_c+1 (contraction upward). For the upper boundary they occur at z=u_c (contraction downward) or z=u_c+1 (extension upward).

A sufficient exact domain is

min_c u_c-max_c l_c >=2.

Then every column interval has length at least two and the sets of possible lower and upper flip layers are disjoint, even between different columns. No single transverse bond can simultaneously act on a lower endpoint and an upper endpoint. A flip preserving total wall number must preserve each affected column's wall count: there are no isolated down spins or one-site holes available to annihilate two walls while another flip creates two. A bond to an unoccupied exterior column creates extra walls there and cannot preserve the total in this domain.

Consequently all first-order N=8-preserving transitions inside this domain are either upper-height moves or lower-height moves on the same four-column induced transverse graph. Their XX/YY signs are identical to those of the previously checked single-interface problem; reversing the down/up sides exchanges equal spins or mixed spins but does not change those bond signs.

The exact statement is a compressed matrix identity

P_sep K1 P_sep=P_sep(K_upper+K_lower)P_sep.

The geometric projector P_sep does not factor into independent upper/lower projectors, so this is not a global tensor-product decomposition. From a state with separation at least three, a single endpoint move remains in the stated domain; at its boundary a permitted move can approach the collision region. Bound-interface wavefunctions have tails in their internal heights, so inserting their tensor product at a finite mean separation also needs a quantitative tail estimate, not just a large average length.

## Conditional relative kinetic scale

Let U=(sum u_c)/4 and L=(sum l_c)/4, and let ell=U-L. At zero total longitudinal momentum, a relative plane wave exp(iq ell) assigns upper/lower momenta +q and -q. The additive band energy is

epsilon(q)+epsilon(-q)=-16cos(q/2)/sqrt(3)
=-16/sqrt(3)+(2/sqrt(3))q^2+O(q^4).

Thus the leading physical relative kinetic coefficient is a=(2/sqrt(3))Jz lambda. This coefficient multiplies -d^2/dell^2 in a continuum approximation; it is not twice that value. For four columns the bare eight-wall energy is 16Jz in the convention H0=2Jz N.

On a flat two-by-two rectangle, the checked bulk diagonal plaquette tension is b=Jz lambda^4/16. Combining these two leading ingredients gives

length scale (a/b)^(1/3)=(32/sqrt(3))^(1/3)lambda^-1,
Airy energy scale (a b^2)^(1/3)
=Jz lambda^3 (2/sqrt(3))^(1/3)16^(-2/3).

The numerical Airy root and even the existence of an isolated Airy level require a boundary/scattering condition supplied by the collision problem. They are not fixed by this scaling argument. Higher coefficient terms, especially K2 energies of order Jz lambda^2, are larger than this lambda^3 scale; one cannot call lambda^3 the next term in the full native energy expansion without accounting for them. For fluctuating endpoint states, translating the flat-rectangle bulk tension into a projected channel also requires control of endpoint offsets/tails and the corresponding bounded corrections.

## Collision and reconnection channels

When upper and lower endpoint layer sets meet, a transverse pair flip can involve an upper end of one column and a lower end of another. The two height graphs then couple directly at K1. If a column shrinks to one down spin, removing that spin annihilates two walls; a simultaneous spin flip in an empty or different column can create two walls, preserving N=8 while changing the occupied column set. One-site gaps and multiple intervals provide further annihilation/creation possibilities. Thus fixed columns, one interval per column, and two independent interface bands are not global invariants of the full eight-wall sector.

Those channels can be parametrically faster than the K4 tension. Their asymptotic thresholds and coupling to the separated channel must be computed before asserting binding, a resonance, or a lifetime. A negative single-interface binding energy alone does not eliminate competing eight-wall fragmentation channels.

## Original source phases

For a finite interval of length at least two, the distance-two readout has two mismatched pairs at each boundary. With bond-center phase exp[ip(j+1)], its exact excess is

-4cos(p/2)exp(ip/2)[exp(ip u_c)+exp(ip l_c)].

Summing the four columns gives separate upper and lower contributions, each with its own COM phase and internal height form factor. The signs are the same at the two ends. At p=0 the total is -8 times four=-32, independent of length and endpoint shape throughout this domain. Thus the bare uniform projected diagnostic is constant and cannot drive internal paired-end dynamics. A finite-p observable can transfer total momentum and resolve endpoint phases, but its matrix elements must be projected onto actual channel states; it should not be replaced by an assumed scalar source. Dressing and collisions can alter the uniform-source conclusion and must be derived explicitly.

Conclusion: the relative kinetic coefficient and conditional lambda^-1/lambda^3 Airy scales follow from the stated separated-end band. The exact local separation identity has a clear domain, but does not close that channel under the full eight-wall operator.
