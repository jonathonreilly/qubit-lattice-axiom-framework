<!-- Original PR9814 source SHA256 589605ab2ef6e7beeff07d0a457cf17f6de7aa48f637503b649dec1c71621084. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Independent native energy-current and pole Ward check

Disposition: PASS. The current is an exact construction from the original bond Hamiltonian, with no additional interaction. Its kinematic implications must remain separate from gravity or a full stress tensor.

## Exact identity and Hermiticity

Write H=sum_a h_a, with Hermitian bond terms and centers r_a, and

    E_q=V^(-1/2) sum_b exp(-iq.r_b) h_b.

Use an ORDERED sum over a,b, and d_ab=r_b-r_a. Antisymmetry of the commutator gives

    [H,E_q]
      = (1/(2sqrt(V))) sum_ab
         [exp(-iq.r_b)-exp(-iq.r_a)] [h_a,h_b]
      = -(i/sqrt(V)) sum_ab exp(-iq.(r_a+r_b)/2)
                             sin(q.d_ab/2) [h_a,h_b].

Therefore the proposed definition

    J_q= i/(2sqrt(V)) sum_ab d_ab sinc(q.d_ab/2)
                         exp(-iq.(r_a+r_b)/2) [h_a,h_b]

satisfies [H,E_q]=-q.J_q EXACTLY, including q=0 by sinc(0)=1. A sum over unordered pairs would require twice the displayed coefficient. Also E_q^dagger=E_-q and J_q^dagger=J_-q.

Only overlapping, noncommuting native bonds contribute. Thus each current term has bounded local support. The sinc factor is the Fourier transform of distributing this local energy transfer along the segment between bond centers:

    d sinc(q.d/2) exp(-iq.mid)
      = integral_(-1/2)^(1/2) ds d exp[-iq.(mid+s d)].

This is a legitimate exact finite-range current convention, though it need not be the unique choice of current; transverse/divergence-free additions leave the Ward identity unchanged. On a periodic grid choose local unwrapped bond centers/displacements consistently for each overlapping pair. The allowed Fourier momenta make shifts by whole periods harmless. An arbitrary large wrapped difference between nearby centers would be an incorrect local convention.

The Heisenberg equation is dE_q/dt=-i q.J_q (hbar=1), consistent with this Fourier convention.

## Matrix element at the Q4 pole

For a ground state g and an excited eigenstate p with excitation energy omega_p>0,

    omega_p <p|E_q|g> = -q.<p|J_q|g>.

Consequently the longitudinal component obeys

    <p|J_parallel,q|g> = -omega_p <p|E_q|g>/|q|.

The root's negative energy-source amplitude therefore gives a positive longitudinal-current amplitude in the same eigenstate phase convention. Inserting omega_p~J Delta lambda^4 and the checked energy amplitude gives

    <p|J_q|g> = J^2 Delta gamma (L+2)/(8sqrt(2L))
                  lambda^(L+4) q |q|^0 + higher terms,

where the displayed vector is proportional to q itself (its magnitude is proportional to |q|). This leading vector form uses the transverse C4-even mode and mirror symmetries, not the scalar Ward identity alone. Those symmetries force the leading analytic vector coefficient to be a common multiple of (qx,qy). Higher-order anisotropic/transverse pieces are not fixed by the Ward identity. This does not construct the other components of a stress tensor.

## Positive static susceptibility

For a real source coupled as -f E (or conjugate Fourier components combined to make the perturbation Hermitian), the positive zero-temperature pole contribution is

    chi_pole(0)=2 W_E/omega_p.

For generic q, this notation means the E_q,E_-q response, with equal opposite-momentum weights by inversion, or the normalized real mode (E_q+E_-q)/sqrt(2). Coupling only -f E_q with real f would not be a Hermitian Hamiltonian at generic q; it should not be the literal source definition.

The checked W_E gives

    chi_pole(0) = J gamma^2 (L+2)^2/(64 L Delta)
                    lambda^(2L-4) |q|^4 [1+o(1)].

The factor of J is correct for the susceptibility of an energy operator to a dimensionless modulation. This is the isolated pole's contribution; other modes can contribute to the full static susceptibility. At q=0, E_0=H/sqrt(V) has no inelastic eigenstate matrix elements, so the isolated-system dynamical response vanishes exactly. A thermal isothermal derivative of the equilibrium energy under a changed temperature/coupling is a different question.

## Error and interpretation scope

The Ward identity itself is exact, so it transfers a controlled energy matrix element to the longitudinal current without a new microscopic approximation. For the asymptotic coefficient, retain the existing matched energy-source estimates: relative O(lambda^2) and momentum-dependent orientation errors O(q^2/lambda^2) in the regime |q|<<lambda, plus the separately bounded actual-H/source remainder. Since the leading energy amplitude is O(J lambda^L q^2), a bare absolute error estimate independent of q does not suffice on a shrinking momentum grid. The exact q=0 identity, inversion, displacement-moment bounds, and high-order microscopic transfer must provide the q-dependent control already required by the energy-source note.

The positive gap approximation adds its own relative o(1), normally O(lambda^2), to the susceptibility. Dividing the Ward identity by |q| does not authorize a finite nonzero q=0 current transition; the controlled leading longitudinal amplitude tends to zero.

This construction establishes an original-H energy transport operator and its relation to one model pole. It is neither a Newtonian response nor a universal-force coupling, and it proves no general obstruction to gravity. A common causal velocity, full stress tensor, detector identification, and cosmological interpretation are not obtained from this Ward identity.
