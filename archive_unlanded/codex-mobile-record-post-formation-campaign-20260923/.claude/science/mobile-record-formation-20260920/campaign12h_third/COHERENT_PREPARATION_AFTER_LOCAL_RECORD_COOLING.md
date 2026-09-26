# Coherent ground preparation after local record cooling

Date: 2026-09-22. Status: conditional finite-component construction, exact
integer spectral certificate, and converged numerical controls; independent
reconstruction pending. The adiabatic theorem and the general preparation
method are established machinery. This is their checked application to the
specified record-assisted cubic field model, not a new general adiabatic
principle, an efficient thermodynamic preparation theorem, or native closure.

## 1. A preparation route with a finite cooling-output stage

The preceding local RK cooler prepares the uniform vector u on any fixed
finite connected physical flip component C. Its expected total jump output
is finite under its stated parent Hamiltonian. Keeping that same cooler on
while replacing the Hamiltonian by H_delta generally produces continued
output and a mixed stationary state. The weighted local cooler instead
prepares a nearby variational state, whose mismatch with the target ground
state is small in one finite example but not zero.

A third supplied protocol is to stop the cooling apparatus after a chosen
preparation time, then use only a coherent ramp

    H(s)=J(D-A)-delta_f f(s)D,     0<=s<=1,             (1)
    i d_s psi(s)=tau H(s)psi(s).

A is the symmetric flip adjacency matrix with multiplicities, D=diag(d(c))
its degree matrix, J>0 and 0<=delta_f<=J. Each term in (1) is still a local
plaquette flip or flippability projector. No amplitudes of the final ground
state are used as control inputs. Supply the classical control schedule f,
its clock, and the ability to turn off these additional cooling couplings.
At delta_f=J the endpoint is the pure kinetic ring Hamiltonian -JA.

Turning off an auxiliary cooler here does not turn off a fundamental record
formation law. This note treats the supplied field/control subsystem. The
live microscopic motion-and-birth construction has not been compiled with
this protocol, its apparatus placements, or its diagonal control term.

If the finite cooling stage leaves a trace-norm error eta_0 from |u><u|,
unitarity preserves that error relative to the ideal ramped state. It adds
at most eta_0/2 to the final failure probability for the ground projector.
Exact finite-time stopping at the dark state is not presumed. The finite
expected number of cooling clicks does not count no-click probes or supply
a deterministic finite storage bound. There are no further clicks from this
switched-off cooler during the ramp; unrelated record processes are outside
this subsystem claim.

## 2. Finite ground uniqueness and a constructive gap bound

For a nontrivial finite connected C with M states, -H(s) has irreducible
nonnegative off-diagonal entries. Adding a sufficiently large scalar makes
the whole matrix nonnegative. Perron-Frobenius then gives a strictly positive
unique ground vector psi_s. This is uniqueness within C; other winding
sectors or disconnected components are not included.

One can also give an elementary, conservative uniform gap bound without
assuming a large-volume phase. Let d_max be the largest degree and let ell
be the graph diameter. Since J(D-A)>=0 and 0<=delta<=J,

    -delta d_max <= E_0(delta) <= 0.

The ground-vector equation at a vertex x is

    J sum_y A_xy psi_y=[(J-delta)d_x-E_0]psi_x
                      <= J d_max psi_x.

Along each graph edge, both amplitude ratios are at most d_max. Hence
psi_min^2>=1/[M d_max^(2ell)]. Ground-state transformation gives

    <psi f,(H-E_0)psi f>
       =J sum_{unordered xy} A_xy psi_x psi_y |f_x-f_y|^2.

For pi_x=psi_x^2, connect each pair by a path of at most ell edges. The
Schwarz inequality bounds Var_pi(f) by
`(ell/2) sum_{unordered xy}|f_x-f_y|^2`. Therefore

    gap(delta) >= 2J psi_min^2/ell
                >= 2J/[M ell d_max^(2ell)] > 0.         (2)

M=1 is a trivial constant-state case. Bound (2) can become extremely small
with system size; it proves finite reachability, not efficient scaling.
Positive finite-component gaps do not rule out a thermodynamic transition.

## 3. Adiabatic theorem and a complete finite path certificate

We apply [Jansen, Ruskai and Seiler, arXiv:quant-ph/0603175v3](https://arxiv.org/html/quant-ph/0603175v3),
Theorem 3. The complete hypotheses used here are a fixed finite-dimensional
Hilbert space, a twice continuously differentiable Hamiltonian family, and
an isolated nondegenerate ground eigenvalue along the path. Equation (2)
checks the gap hypothesis for each component. For a lower gap g, after
subtracting any scalar Hamiltonian function, its bound specializes to

    failure_probability <= min(1, B^2/tau^2),
    B=(||H'(0)||+||H'(1)||)/g^2
       +integral_0^1 [||H''(s)||/g^2+7||H'(s)||^2/g^3] ds.  (3)

Primes in (3) are derivatives in the dimensionless ramp parameter; H' here
is not the energy-reference notation used in the separate density note.
For a linear ramp, let v=delta_f(d_max-d_min)/2. Centering D removes its
scalar midpoint and gives B=2v/g^2+7v^2/g^3. For f(s)=3s^2-2s^3,
B=3v/g^2+(42/5)v^2/g^3. These bounds include their endpoint contributions;
no informal instantaneous slowness criterion is substituted for (3).

The actual periodic 2x2x2 component has 864 states, 24 distinct link qubits,
24 plaquettes, and degrees from 4 to 16. We checked J=delta_f=1 along the
whole interval. The spectral certificate works as follows.

At delta=j/16, the exact matrix is an integer matrix B_j divided by 16.
A floating eigensolver only proposes a full basis. Quantize that basis to
an integer matrix Q_i with denominator S=2^22, and its sorted eigenvalues
to an integer diagonal D_i with the same denominator. Compute exactly

    G_i=Q_i^T Q_i-S^2 I,
    R_i=S B_j Q_i-16 Q_i D_i.

All products and sums are integer arithmetic. Explicit upper bounds on the
absolute sum of every possible product exclude int64 overflow before the
products are evaluated. With m=864 put

    e=m max|G_i|/S^2,
    r=m max|R_i|/(16S^2),
    L=max|D_i|/S,
    eta=(r+2Le)/(1-e).                                  (4)

The checked e<1/2 makes Q=Q_i/S invertible. In its polar decomposition Q=US,
`||S-I||<=e` and `sigma_min(S)>=1-e`. Consequently
`||H-U diag(D_i/S) U^dagger||<=eta`. Weyl's inequality bounds each ordered
eigenvalue error by eta, so each grid-point ground gap is at least
`(D_i[1]-D_i[0])/S-2eta`. All these expressions are exact rational numbers;
floating eigenvalues are not accepted as gap certificates by themselves.

The centered derivative norm is six. Between grid points, the ground gap
is Lipschitz with constant twelve. Every parameter value is at distance at
most 1/32 from a grid point, so subtracting 6/16 from the least certified
grid gap covers the complete path. The first complete run gives

    g >= 107282299149033/280763026112512
       > 0.3821097.                                    (5)

This deliberately loose bound is positive over the full interval, rather
than just at the sampled endpoints. The rounded basis/eigenvalue hashes,
integer residual maxima, exact fractions, and overflow checks are in the
result file. Reproduction may propose another degenerate eigenbasis, but
must verify its own integer certificate by the same algebra. No unproved
claim about the accuracy of a library eigensolver is needed for (5).

## 4. Actual coherent controls and their precision

The runner integrates the full 864-component Schrodinger equation using
DOP853 for both a linear and a smoothstep ramp. Every duration is rerun at
relative tolerances 2e-10 and 2e-12, with absolute tolerance thirty times
smaller. These are numerical evolution controls, distinct from (3)-(5).

For the smooth ramp to -A, selected results are:

| tau, in units J^-1 | Ground infidelity | Excess energy, in units J |
| --- | --- | --- |
| 2 | 0.01787946846 | 0.06573733981 |
| 4 | 0.001897350030 | 0.006528262024 |
| 8 | 0.00006806988236 | 0.0002388947332 |
| 16 | 0.000007740338697 | 0.00002655622703 |

The target component ground energy is numerically -9.026720913531113. The
largest phase-aligned state discrepancy between the two tolerances over
all controls is below 1.42e-8, and the tight-run norm errors are below 8.1e-12.
The conservative theorem bound in (3) remains trivial at these short
durations. It guarantees eventual accuracy, while the converged computation
measures the much better performance in this finite model. They must not
be described as the same numerical guarantee.

## 5. What this adds and what still needs a derivation

This gives a local-control route from the exactly specified RK preparation
target to the actual finite-component ground state of the pure ring model,
without an operational oracle for its amplitudes and without leaving the
old cooler continuously active. It does require an externally prescribed
Hamiltonian ramp and preparation time. The theorem does not supply a
system-size-uniform gap, efficient cooling time, a native control compiler,
or a preparation of every winding sector's global ground state.

The cubic quantum-link literature is relevant context, not a phase
certificate for this packet. [Banerjee, Huffman and Rammelmueller,
arXiv:2201.07171](https://arxiv.org/pdf/2201.07171), section V.A, studies
small three-dimensional tubes and treats the Coulomb interpretation as a
candidate requiring larger-system evidence. The present one-component ramp
cannot settle that thermodynamic question either. A separate Gaussian ramp
diagnostic can quantify a possible soft-mode cost, but identifying it with
this microscopic model would require additional work.
