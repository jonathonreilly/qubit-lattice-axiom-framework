<!-- Original PR9801 source SHA256 25bd01f6790a9a7a184a6553889a0baa5b0b57785d4025bc87acd7f6d4c4dc38. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Independent check: finite-energy outgoing fixed-flux scattering

The sign, logarithmic coefficient and six-site source limit are correct for the stated static-background coefficient Hamiltonian. This is not a full microscopic emission or dynamical-environment calculation.

## Resolvent convention

For L0=4-adjacency and G_plus(epsilon)=(L0-epsilon-i0)^-1, the imaginary part is positive. The conventional outgoing resolvent (epsilon-L0+i0)^-1 is -G_plus. Therefore the scattering equation for L0+V is

u=phi-G_plus V u,  (I+G_plus V)u=phi,

with phi_x=exp(i k dot x) and epsilon=4-2cos(kx)-2cos(ky). The plus sign in the finite matrix is correct; reversing the resolvent convention without reversing this sign would be wrong.

Put z=4-epsilon-i0. The Brillouin-zone diagonal integral gives g=2 K(16/z^2)/(pi z), where K takes its argument as the elliptic parameter, not modulus. Near the lower edge, 1-16/z^2=-epsilon/2-i0+O(epsilon^2). Thus the logarithm in K is continued from below its negative-real argument, and

g=(1/(4pi))log(32/epsilon)+i/4+o(1).

The positive i/4 also agrees with the lower-edge density of states 1/(4pi). A numerical elliptic implementation must approach z from the lower half-plane; substituting a bare real parameter greater than one may select the opposite boundary value.

## Potential-kernel reduction

For fixed separations, G_plus(x,y)=g-A(x-y)+o(1). The real potential-kernel values used here are A10=1/4, A11=1/pi, A20=1-2/pi and A21=2/pi-1/4. The latter two follow from the discrete harmonic recurrence once A10,A11 are fixed. The kernel normalization is that of 4-adjacency, not a random-walk Green function multiplied by four.

For the two middle sites let the asymptotic symmetric amplitude be a, and for the four outer sites b. With V=+2 on the four altered vertical bonds, the six-site equations reduce to

(8g-4/pi)a+(8g-1)b=1,
(8g-2)a+(8g-4/pi)b=1.

Their difference gives a=r b with r=(4-pi)/(4-2pi), and hence

a+a = 2r/[8g(1+r)-1-4r/pi].

This is the proposed expression. Inserting the outgoing g gives

log(1/epsilon)(u_0+u_1) -> pi r/(1+r) = -1.89276244... .

The negative leading source is allowed: u is a scattering amplitude in a signed-hopping background, not a nonnegative density.

## Controlling the nonsymmetric incident wave

The actual plane-wave vector on the fixed six-site set is 1+O(sqrt(epsilon)); it need not have the exact reflection symmetries of the constant vector. This does not change the limit. I independently formed the full six by six matrix M=I+(g11^T-A)V and obtained

det M = 4(pi^2-4pi+8)(12g pi^2-32g pi-pi^2+8)/pi^4.

Its coefficient of g is nonzero. Every cofactor is at most linear in g because the g-dependent part has rank one. Thus M^-1 remains uniformly bounded as Re g tends to infinity, including the finite imaginary part i/4. The small nonsymmetric incident term and the o(1) potential-kernel corrections therefore remain controlled. More specifically the fixed-distance Green differences have error O(epsilon log(1/epsilon)); combined with the O(sqrt(epsilon)) incident correction, these are o(1/log(1/epsilon)). They do not change the stated scaled source limit.

## Scope

The changed-bond perturbation is an off-diagonal signed-hopping perturbation, not a positive onsite potential. The derivation uses its exact six-site matrix, so it does not rely on positivity of V. It describes a prescribed, static column-sign background and the coefficient heavy-particle hopping operator. The outgoing convention determines a scattering boundary condition; it does not by itself give a native decay rate, a relaxed-heavy matrix element, a universal coupling or a cosmological identification. The energy variable here belongs to that coefficient operator, and any conversion to physical energies requires the separately specified microscopic scaling.
