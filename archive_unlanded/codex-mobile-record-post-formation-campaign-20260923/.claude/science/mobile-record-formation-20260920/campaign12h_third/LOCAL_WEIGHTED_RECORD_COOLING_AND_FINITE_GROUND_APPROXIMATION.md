# Local weighted record cooling and a finite ground-state approximation

Status: personally derived conditional extension and finite variational test;
independent verification pending. The proposed local reservoir prepares an
explicit state. The quality of its approximation to another Hamiltonian's
ground state is a separate, finite calculation. No thermodynamic photon
vacuum follows from finite fidelity.

## 1. A local alternative to full-configuration targeting

The preceding exact retuned construction requires every ground-amplitude
ratio on the whole configuration graph. A simpler trial family on a connected
finite plaquette component is

    psi_theta(c)=Z_theta^(-1/2) exp[theta d(c)/2],
    d(c)=number of flippable plaquettes, theta real.             (1)

Its squared amplitudes are a classical local weight exp(theta d). This is a
chosen variational family, not an assertion that it is the exact ground
state of H_delta or that the axioms select theta.

For an oriented p-flip a->b, define m=d(b)-d(a). Only plaquettes sharing an
edge with p can contribute to m. On a nondegenerate cubic lattice there are
at most12 other such plaquettes; their union with p uses at most40 link
qubits. Thus m is determined by a bounded neighborhood, independent of total
volume. The p plaquette stays flippable at both endpoints and contributes
zero to the difference. Periodic small lattices can identify some neighbors;
the actual support is counted directly by the finite checker.

For fixed p and m group its disjoint flippable pairs. Let r_m=exp(theta m/2)
and for each pair define

    s=(|a>+r_m|b>)/sqrt(1+r_m^2),
    d_minus=(r_m|a>-|b>)/sqrt(1+r_m^2),
    L_(p,m)=sum_(pairs with this m)|s><d_minus|,
    P_(p,m)^-=L_(p,m)^dag L_(p,m).                              (2)

There is one coherent jump per p,m class, not one jump per spectator
configuration. Pairs within a class have disjoint source and target support.
The class condition is itself local, so the operators in (2) have bounded
support. They preserve Gauss charges. A proper rotation or translation
permutes the plaquette/context labels. Reversing a plaquette orientation
interchanges its endpoints, sends m to -m and changes L by at most a sign.
Uniform rates over the corresponding labels therefore give a covariant law.
This is still a supplied many-qubit interaction, not a one-site M2 nearest-
neighbor physical compiler.

## 2. Conditional all-finite-component preparation theorem

Consider exactly

    G_theta(rho)=-i[H_theta,rho]+sum_(p,m) gamma_(p,m) D[L_(p,m)]rho,
    H_theta=sum_(p,m) h_(p,m) P_(p,m)^-,
    gamma_(p,m)>0, h_(p,m) real.                               (3)

All nonempty local classes have positive rates. The common dark kernel is
span(psi_theta): along every connected edge the kernel condition fixes the
ratio of the two amplitudes to r_m, and (1) satisfies every cycle condition.

The separating-observable proof in LOCAL_GAUGE_RECORD_COOLING_TO_RK_STATES.md
extends as follows. Let F(c)=sum_l3^lE_l(c), which has distinct values, and
Delta_p=F(b)-F(a), constant on all p pairs. For v(t)=exp(tF)psi_theta,

    P_(p,m)^- v(t)=g_(p,m)(t) L_(p,m)^dag v(t),
    g_(p,m)(t)=r_m[1-exp(t Delta_p)]/[1+r_m^2 exp(t Delta_p)].   (4)

The coefficient is constant throughout that whole jump and g_(p,m)(0)=0.
For a subspace W perpendicular to psi_theta, invariant under the jumps and
R=K_loss/2+iH_theta, compression of (4) yields

    [R_W^dag-sum_(p,m)(gamma_(p,m)/2-i h_(p,m))
          g_(p,m)(t) L_(p,m;W)^dag] P_W v(t)=0.                (5)

At t=0 the bracket is invertible because its Hermitian part is strictly
positive on W. It stays invertible near zero. Analyticity and the Vandermonde
span of F^n psi_theta therefore force W=0. The finite transient semigroup
argument in the earlier note then proves convergence from every initial
density to |psi_theta><psi_theta|, with model-dependent exponential
constants and finite expected total jump output. Those qualitative constants
are not asserted to be uniform or efficient as volume grows.

One must not omit the m resolution when r_m varies between spectator
backgrounds: equation(4) would then have no single scalar coefficient for
that jump. The theorem proves the explicitly resolved local model (2)-(3),
not an arbitrary target-weighted coherent plaquette operator.

Each L_(p,m) is a partial isometry from its minus to plus subspace. The same
fresh-fuel collision gives A0=I+(cos(theta_gate)-1)Pminus and
A1=-i sin(theta_gate)L_(p,m), with new permanent records in A1. The variational
parameter theta and collision angle theta_gate are different quantities.
Fresh resources, export, controllable interactions and timing remain supplied.

## 3. Finite variational selection and its operational error bound

For the actual periodic2x2x2,864-state component, evaluate the Rayleigh energy
of (1) under H_delta=J sum(P-X)-delta sum P, with J=1. Choose theta by
minimizing that energy within this one-parameter family, not by fitting to
the exact ground vector. All d values on this component are even; with
x=exp(theta), the energy is the rational function

    E(x)=N(x)/Z(x),
    Z(x)=sum_c x^d(c),
    N(x)=sum_c(1-delta)d(c)x^d(c)
         -2 sum_(configuration graph edges, with multiplicity)
                       x^[(d(a)+d(b))/2].                    (6)

The finite checker isolates all positive critical roots of N'Z-NZ' using
rational arithmetic, and compares energies with both x->0 and x->infinity
limits. A separate exact polynomial root-count certificate verifies one
positive critical root, a negative derivative at small x and a positive
derivative at large x, so it is the unique global minimum for x>0. This
supplies the optimum within the declared family on this finite component.
It is not an optimization over all local reservoirs or states.

Separately, diagonalizing that finite H_delta gives its ground energy E0,
normalized ground vector psi0 and gap Delta>0 within the component. For any
normalized prepared trial state,

    1-|<psi0|psi_theta>|^2 <= [E(theta)-E0]/Delta.              (7)

After the preparation bath is turned off, evolution with H_delta preserves
its distance from the stationary ground state. Thus for all later times,

    ||rho_trial(t)-|psi0><psi0|||_1
       <=2sqrt([E(theta)-E0]/Delta).                          (8)

If the preparation itself has trace error epsilon, add epsilon to the right
side. Equation(8) is a finite-model bound using the actual spectral gap,
not a thermodynamic claim or a timescale inferred from the variational fit.
Switching from the preparation generator to H_delta is an additional control
step. Continuing (3)'s bath under an unrelated H_delta does not invoke the
preparation theorem, as the previous mismatch calculation demonstrated.

The first full runner execution passed. Its finite results are:

| delta | optimal theta | ground-state infidelity | energy/gap upper bound |
|---|---:|---:|---:|
| 0.05 | 0.0160076 | 0.00019553 | 0.00056596 |
| 0.2 | 0.0619384 | 0.00256010 | 0.00682167 |
| 0.5 | 0.1481539 | 0.01143117 | 0.02665257 |
| 1 | 0.2894125 | 0.02960519 | 0.06150157 |

All168 local class jumps on the864-state component annihilate their stated
target within7e-18 in the floating check. An independent algebra assembly
within the author runner checks the general two-state identity symbolically
and a nontrivial eight-state, five-channel model with coherent spectators
exactly: its common dark kernel has dimension1 and its rational-complex
Liouvillian has nullity1. This is not an independent-agent review.
The support check counts20,30,32 links on periodic side2,3,4 examples and
verifies384 flippable backgrounds with arbitrary fixed Gauss charges. The
general40-link bound follows from the overlap geometry, not random sampling.

## 4. What remains for the physical objective

This construction makes the proposed state preparation local at the level
of supplied link qubits and finite-range many-body interactions. It replaces
a global ground-amplitude oracle with a definite local trial family. Its
quality must still be established as size and observables change. Classical
local weights do not automatically have the nonanalytic electric covariance
of a Maxwell quantum vacuum. No such thermodynamic identification, native
record-content compiler, autonomous apparatus switch, or complete TOE is
claimed. The finite test is meant to decide whether this local preparation
route deserves further work, including comparison with other ansatz families.
