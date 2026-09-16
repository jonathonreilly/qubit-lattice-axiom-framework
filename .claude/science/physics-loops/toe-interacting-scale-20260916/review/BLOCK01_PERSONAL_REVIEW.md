# Personal adversarial pass: uniform field and soft response

2026-09-16 UTC. Same author as the derivation; not independent review.
Input hashes before the pass are in BLOCK01_AUTHOR_REVIEW_INPUTS.json.

Disposition: a provisional bounded theorem about the supplied finite-volume
Hamiltonian and its normalized ground-space trace. No fixed-g phase, photon
pole or independently accepted result. No axiom, primitive or prompt changed.

Load-bearing checks:

1. The trial state lies on the entire integer cycle lattice, including
   harmonic loops. Its paired onsite product has exact zero charge and the
   correct N_+=N_-=V filling for the Wilson example. Hopping expectation is
   zero, without assuming that hopping vanishes as an operator.
2. Poisson differentiation has the correct sign: the dual correction lowers
   the electric quadratic moment. The arbitrary positive electric metric
   enters both the lattice covolume and its dual. Rank is E-V+1=2V+1.
3. The magnetic overlap uses a shift in the SAME affine lattice and Jensen.
   It does not replace compact angles by real coordinates or omit wraparound.
4. The operator lower bound for paired hopping uses twice the NUCLEAR norm.
   A literal CAR calculation detects the operator-norm mistake for the z
   hopping, whose two singular values are each1/2.
5. Translation invariance belongs to the normalized finite ground trace.
   The proof never assumes that an infinite-volume pure ground state has it.
   The bound for each plaquette orientation uses V copies, not all3V at once.
6. The low-energy lower bound uses the full ground projection. Ground-block
   commutator trace vanishes by finite trace cyclicity. It need not vanish
   in a pure ground vector; that failure is preserved in the finite checker.
7. The charged f-sum includes both squared charges. The magnetic f-sum retains
   spatial fluctuations of cos(theta). The plane-wave calculation is checked
   against a literal sparse cubic curl and an exactly translated ensemble,
   not a synthetic diagonal photon kernel.
8. The finite wavepacket includes the endpoint terms of its discrete second
   difference. Literal cubes challenge its curl and double-curl norms. Its
   support requirement is L>=R+3, explicitly independent of other volumes.
9. The added explicit constant60 is a relaxed analytic consequence of the
   stated inequalities for R=ceil(2/g), g<=1/10. It is not a measured energy
   and was not obtained by fitting the checker.
10. The route reaches k much larger than g, or energy of order g. It supplies
    no estimate vanishing as k tends to zero at fixed g. A thermodynamic
    inelastic statement is also not automatic because excitation weight
    can accumulate at zero. These remain open, not named axiomatic walls.

Review-driven changes: specified the Wilson zeta range; added a concrete local
wavepacket corollary to make the uniformity checkable; added a submaximal-energy
spectral challenge and an actually constructed two-level counterexample to a
missing factor of two. No theorem formula failed in the checks. The initial
checker and current checker both ran successfully; the reruns were justified
by these new discriminators. No tolerance was weakened.

Verification limits: finite theta sums are floating-point challenges with
explicit truncations, not interval certificates. The checker does not solve a
three-dimensional interacting ground state or certify an infinite-volume
limit. The proof remains the source of the general inequalities. No external
agent or independent referee has reviewed it.

The pre-pass note, runner and output have been recovered byte-for-byte under
BLOCK01_PREFLIGHT_* and verified against the previously captured SHA256 values.
They are historical review inputs; current evidence/ files are the active runner.
