# Ground energy versus original formation activity — personal working derivation

2026-09-25. Unsealed root candidate, no independent check or empirical claim.
This investigates whether a global energetic vacuum can be stationary under
the same supplied original birth-only common dynamics. The full magnetic
Hamiltonian, actual gated electric term, Gauss space and instrument remain.
The half-filled trial and vacant-site row bound below provisionally depend
on the sealed root35 argument, whose independent PRE is still running.

Let L>=6 be even, n=|A|=|B|=L^3/2, and write

    h = K D - 2 delta Q,
    Q = sum_(a<c sharing B) (F_c F_a P)* F_c F_a P,
    Gamma = sum_j L_j* L_j.

Use the full physical charge/electric basis. Every F and original jump has
nonnegative real entries in that basis. D is diagonal and nonnegative.
Q and Gamma are bounded nonnegative-entry matrices at fixed graph. Entrywise
comparison below is NOT an operator-order claim.

For either all resolved signs or the unnormalized coherent sum of the two
signs on each edge, define

    M_ab = P F_a* 1_(q_b=0) F_a P.

The exact identity j_(ab,sigma)* j_(ab,sigma)=1_(q_a=0,q_b=0)
on rotor space and orthogonality of the two created A charges give

    Gamma = 2 kappa sum_(a,b~a) M_ab.                 (A)

For any other A site c~b, the term with F_c hopping out and back along
the same edge (c,b) in Q_ac equals M_ab. A is fully occupied initially,
F_a does not alter q_c, and rotor shifts have unit amplitude. All other
terms in Q_ac have nonnegative matrix entries. Hence M_ab<=Q_ac
ENTRYWISE, including the exact electric shift words.

Every B site has five other A neighbours, so

    5 sum_ab M_ab
      = sum_(a<c sharing B) sum_(b common) (M_ab+M_cb)
      <= sum_(a<c) 2 r_ac Q_ac <= 4Q

because r_ac<=2 on these cubic tori. Therefore

    Gamma <= (8 kappa/5) Q                         (B)

entrywise. This comparison is not generally Loewner order.

For a normalized pure state psi of finite electric form energy, let phi
be its componentwise absolute value in the full electric basis. The
electric expectation is unchanged. Every pairwise phase deficit

    |psi_i||psi_j| - Re(conj(psi_i) psi_j)

is nonnegative. Thus

    E(psi)-E(phi) = 2 delta [<Q>_phi-<Q>_psi] >= 0,
    <Gamma>_phi-<Gamma>_psi
      <= (8 kappa/5) [<Q>_phi-<Q>_psi].              (C)

All sums converge because Q and Gamma are bounded and have nonnegative
entries; |psi| is in the same electric form domain.

In a sector with m occupied B sites, let h_a denote the number of empty
B neighbours of a. The diagonal original loss is exactly

    Gamma_xx=2 kappa sum_a h_a(h_a-1).

There are 6(n-m) empty-neighbour incidences. For integer k>=0,
k(k-1)>=2(k-1), including k=0. Thus

    Gamma_xx >= 4 kappa (5n-6m).                    (D)

Nonnegative off-diagonal entries give <Gamma>_phi>=the same bound.
If e_m=inf spec h in that sector, E(phi)>=e_m. Equations (B)-(D) give

    <Gamma>_psi >= 4 kappa(5n-6m)
                   - (4 kappa/(5 delta))(E(psi)-e_m). (E)

In particular a formation-dark finite-energy state in m<5n/6 must lie
at least 5 delta(5n-6m) above that sector's spectral infimum. No positive
ground-state choice, nondegeneracy, irreducibility or normalizable
ground eigenvector is assumed. This fixes the earlier weaker idea of
arguing only for nonnegative ground vectors: destructive phases are
controlled explicitly by their energy cost.

For a global consequence use ONLY two explicit root35 estimates:

    e_m >= -2 delta*3004(n-m),
    e_0_global <= -2 delta R_half + o_L(delta),
    R_half > (1905/2)n

as eta=K/delta tends to zero at fixed graph. The notation e_0_global here
means the global infimum, not the m=0 sector.
For m>7n/10 these bounds give

    e_m-e_global >= (513/5) delta n - o_L(delta).

For sufficiently small eta, the right side is at least 4 delta n.
For m<=7n/10, (E) gives the rate bound with first term at least
(16/5) kappa n and with e_m replaced by e_global. For m>7n/10 the same
bound follows from <Gamma>>=0 and the preceding energy gap.

Consequently, for every normalized finite-energy state, including mixtures
and coherences between number sectors,

    <Gamma> >= (16/5) kappa n
                 - (4 kappa/(5 delta))(<h>-e_global).  (F)

Decompose by N, since h and Gamma preserve N, then into pure states.
Finite h energy is equivalent to finite D form energy up to a bounded
term. The same inequality therefore holds for normal densities.
It implies

    <Gamma>=0  =>  <h> >= e_global + 4 delta n.        (G)

For infinite positive energy the inequality is interpreted as the trivial
extended-energy statement. The formation-balance main theorem already
proves that every normal stationary state has <Gamma>=0, since bounded
N satisfies d<N>/dt=2<Gamma>. Hence any finite-energy normal stationary
state lies strictly above the Hamiltonian ground infimum in this regime.
Near-global-ground states must keep forming records at an extensive rate.

This does not prove a physical vacuum is the Hamiltonian ground, does not
show spontaneous unitary decay, and does not rule out a driven/metastable
or other nonequilibrium physical vacuum. The Hamiltonian conserves N;
the supplied birth process changes it. No relaxation time, autonomous
energy source, laboratory photon identification, experimental exclusion,
uniform thermodynamic limit or new axiom follows.

Next checks: reconstruct (A) from full primitive jumps, and (B) from exact
four-hop paths with explicit Gauss/electric shifts, including interference.
Check all cubic overlap multiplicities and the phase-deficit logic. Use
small physical graphs as bounded controls, not field-only occupation
matrices or a replacement formation law. Then write and seal a full note.
