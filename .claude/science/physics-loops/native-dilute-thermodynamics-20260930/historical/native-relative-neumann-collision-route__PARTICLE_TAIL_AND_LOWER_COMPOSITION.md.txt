# Actual total-particle tails and a conditional lower composition

The tail lemma below is a separate exact consequence of the already checked
global bad-particle estimate and elementary packing. The subsequent lower
composition is explicitly CONDITIONAL on CENTERED_RESIDUAL_PROOF.md976cfb69
surviving independent checking. It is not an established EOS, phase result,
or a claim that an unchecked chain has been adopted. No computation is used.
This file does not presume a uniform growing-n cell theorem.

## 1. An actual total-cell-count tail lemma

Let the physical torus have side L, fix disjoint vertex cubes Lambda_j of
side ell with L>=10ell, and write N_j for their actual particle numbers.
For an integer b>=10, let B_b count global particles outside b-isolated
actual graph dimers. The checked unchanged-law estimate is

                         B_b <= (C_B b^3/a) H0,
 C_B=28000322,       a=min(tau,mu/12),       L>=10b.               (1)

Choose one endpoint as an anchor of each global b-isolated dimer. Distinct
anchors have Chebyshev separation greater than b. If a dimer has an endpoint
inside Lambda_j, its anchor is in its width-two enlargement. Grid boxes of
side b+1 therefore contain at most one such anchor. When b<=ell/8 and ell
is sufficiently large, at most8ell^3/b^3 grid boxes meet that enlargement.
The number of particles in Lambda_j belonging to globally b-isolated dimers
is consequently at most

                             16ell^3/b^3.                       (2)

This explicitly includes dimers crossing the cell face. Local coordinates
on the width-two enlargement are unambiguous since L>=10ell; periodic
seams do not alter the packing. The estimate uses actual occupation sets,
not a bosonic particle count.

Fix K>=2^18 and take

              b=ceil[(64ell^3/K)^(1/3)].                        (3)

For fixed K and sufficiently large ell, b>=10, b<=ell/8, and
b^3<=128ell^3/K. By(2), each cell has at most K/4 good particles. Thus on
every occupation, N_j>K implies that at least N_j/2 of its particles are
counted by B_b. Disjoint cells give the exact diagonal inequality

 sum_j N_j 1_(N_j>K) <=2 B_b.

For every quantum state, including coherent states and number fluctuations,

 sum_j <N_j 1_(N_j>K)>
            <= C_tail (ell^3/K) E,
 C_tail=256 C_B/a,       E=<H0>.                                (4)

The statement holds for every translation of the cell family. It controls
lost particles, not lost energy or a global no-defect norm. High-number
cell energies may be discarded only because the comparison cell operators
are positive. Boundary singleton sectors forbid silently replacing this
argument by a uniform N_j^2/ell^3 coercivity of H_plus.

## 2. The exact low-sector hypothesis needed for composition

Put E_*=||T0|| and t0=min_(||z||=1)<z^2,T0 z^2>. Both are finite and positive
for the supplied model, with the already checked full15 normalization.
Fix0<eta<=1/2 and the finite K above. The NEW centered-residual candidate,
if correct, implies that gamma>0 can be fixed sufficiently small and then
ell sufficiently large so that the actual positive cell operator obeys
for every physical particle number0<=M<=K,

 H_plus|_(N_j=M)
   >= [c_eta M^2-C_* M]/ell^3,
 c_eta=(1-eta)t0/8,       C_*=16 E_*.                            (5)

Here gamma may depend on eta,K but not ell or the state; assume gamma<=1.
The thresholds in ell can depend on all these fixed parameters. No estimate
uniform as K increases is presumed.

For precision, here is the derivation of(5) from that one conditional input.
For even M=2n, finite5-mode sphere moments give for every internal n-pair
state, including fragmented and complex states,

 <sum_(i<j)T_eta^(ij)>
       >= [t_coh(T_eta)/2] n(n-1)-27 E_* n.

One may verify this without a dilute-gas theorem: the normalized two-body
coherent-mixture density is

 [n(n-1)gamma2+4n P_sym(gamma1 tensor I)P_sym+2P_sym]
                                      /[(n+5)(n+6)].

The positive added terms have the complementary trace. The resulting trace
norm bound gives the displayed27 E_* n error. This is the exact finite
sphere identity previously proved and checked in compatible REPORT04e13444,
not an assumption that an energy-minimizing state is coherent.

Since (1-eta)T0<=T_eta<=T0, the right side is at least
c_eta M^2-14 E_* M. Choose gamma so that the candidate Schur error is at
most E_* simultaneously for the FINITELY many n<=K/2. Its actual low-energy
spectral comparison has relative error tending to zero as ell grows; choose
ell large enough to price that too by E_*. For M>=1 these two absolute errors
are bounded by2E_* M. This yields(5). The M=0 vacuum is exact. For odd M,
the checked physical-cell gap c(eta,gamma)ell^-2 eventually exceeds the
right side of(5) for every fixed M<=K, so the same bound holds. Odd sectors
are not silently projected away.

Thus the sole unverified new mathematical dependency in(5) is the actual
centered-residual coefficient theorem. The finite-mode identity, odd-sector
gap and physical boundary comparison have separate earlier checks.

## 3. Particle-number cutoff and all-state Jensen

Each H_plus preserves its own TOTAL physical particle number. Define the
commuting diagonal variable Y_j=N_j 1_(N_j<=K). Its high-number sector may
be dropped by positivity, and(5) gives the full-cell operator lower form

                 H_plus,j >= [c_eta Y_j^2-C_* Y_j]/ell^3.        (6)

No restriction on a state's support or probability of having defects is
made. The physical cell may be entangled with all other cells.

For any fixed tiling of J cells, state Cauchy and scalar Jensen give

 sum_j <Y_j^2> >=(sum_j <Y_j>)^2/J.

The same inequality holds after averaging translated tilings: apply Jensen
also to that average. For divisible tori J ell^3=L^3. For general L, use
J=floor(L/ell)^3 disjoint complete cubes and a translated remainder. The
covered fraction is at least1-3ell/L. Translation averaging therefore
loses at most3ell Nmean/L particles to the remainder. Safe diagonals optimize
all omitted neighbors, including this remainder, so the original positive
row comparison remains valid. No state is cut or replaced.

A site's probability of belonging to a retained cell boundary is at most
12/ell. Consequently the exact original-law penalty debit is still at most
12 gamma Nmean/ell^3. Since J ell^3<=L^3, the averaged Jensen lower term is
at least c_eta (Ymean/L^3)^2 L^3, where Ymean is the averaged retained count.
Equations(4),(6) imply for every state

 Ymean/L^3 >= (1-3ell/L)rho-C_tail(ell^3/K) E/L^3,
 E/L^3 >= c_eta (Ymean/L^3)^2
                              -(C_*+12gamma)rho/ell^3.          (7)

Use the positive part of the first lower bound when necessary. Here
rho=Nmean/L^3. These estimates apply to arbitrary particle-number mixtures,
not just canonical or translation-invariant states. The added boundary term
has been explicitly subtracted, not treated as part of the original law.

## 4. Conditional dilute lower coefficient, with all ordered limits

Take a fixed finite energy ceiling C_E>t0/8; states with E/L^3>C_E rho^2
already satisfy the desired asymptotic lower comparison. For the remaining
states suppose E/L^3<=C_E rho^2. Choose a fixed mesoscopic mean parameter
m>0 and, at each small density, an integer ell such that

                            rho ell^3 -> m.                     (8)

Choose K fixed, as large as desired compared with m, before letting rho
shrink. With eta fixed, choose gamma and the cell threshold as in section2.
Then rho->0 makes ell->infinity and eventually satisfies every fixed-K,
fixed-R0 and fixed-parameter cell hypothesis. Taking L->infinity first
removes the remainder fraction in(7). It follows conditionally that

 liminf_(rho->0) liminf_(L->infinity) E/(rho^2 L^3)
 >= c_eta [1-C_tail C_E m/K]_+^2 -(C_*+12gamma)/m.               (9)

This is uniform over the states under the stated energy ceiling. All limits
use the actual original H0. There is no hidden n~sqrt(log ell) or other
uniform growing-n assumption: for each chosen K there are only finitely
many particle sectors, and rho is taken small after their thresholds.

Finally choose m arbitrarily large, K/m arbitrarily large, and eta
arbitrarily small, in that order of parameter selection before the dilute
limit; gamma is chosen for the selected finite K,eta. Since0<gamma<=1,
its final debit is bounded by12/m. Equation(9) then yields the CONDITIONAL
full-carrier dilute LOWER bound

             liminf E/(rho^2 L^3) >= t0/8.                      (10)

The coefficient is not assumed from a coherent ansatz: it arises from the
full15 pair form and the exact finite5-mode density-matrix identity, allowing
fragmentation and different cell states. This is a lower bound only. It does
not supply a canonical upper construction, condensate, ODLRO, channel
selection, phase diagram, or equality of a separately defined EOS.

Equation(10) must not be advertised as established until the new coefficient
proof and this composition have survived their own focused checks. At this
freeze the centered-residual theorem is an author candidate awaiting that
check. The exact tail estimate(4) and the explicit conditional implication
are the present durable outputs; no unverified downstream claim is adopted.
