# Permanent designated qubits beside a coherent negative-grand-energy medium

**Status:** conditional-support author construction, not formal review or audit.
This changes the supplied Hamiltonian. The original H0 local-commutant and
Markov-repair theorems remain untouched. No mask, dynamics, record meaning or
physical clock is selected by the framework axioms.

## 1. Result and resource statement

Fix the actual native one-qubit tensor carrier, its occupation basis and
positive mu,tau. Define the landed constants

    A=10199347200(182mu+240tau), B=3870720,
    a=min(tau,mu/12), c=a/99090432,
    c_read=min(mu,mu/3+2tau).

Choose a supplied chemical potential and rate

    0<nu<c_read, gamma>0,
    g=nu^2/(A+nu B), h_*=160mu+240tau,
    C_nu=30h_*+25(mu-nu).                                  (1)

Choose any integer

    ell>=max(5,2 C_nu/g), p=ell+4, L in p N, V=L^3.          (2)

Partition the torus into p-cubes. In each retain an active cube of ell^3
sites; designate the complementary width-four corridors R as marker sites.
Let D be the union of active cubes, with fractions

    r_D=(ell/p)^3, r_R=1-r_D>0.                             (3)

We construct below a strictly local changed Hamiltonian H0^R>=0 on the SAME
M2 site factors. Its grand Hamiltonian is Hnu^R=H0^R-nu N with N over ALL
sites; records are charged mu-nu>0 each, not assigned free negative energy.
There is an explicit normalized medium preparation on D such that, for
EVERY occupation pattern or density matrix on R,

    <Hnu^R>/V<=-g r_D/2,
    g r_D/nu<=<N_D>/V<=3g r_D/nu.                          (4)

The supplied onsite formation channels J_r=sqrt(gamma)b_r^dagger, r in R,
make every already formed rank-one projector n_r=1 absorbing on the full
carrier. From blank R the records form at their actual sites, never move or
erase, and at time t have mean density

    <N_R(t)>/V=r_R(1-exp(-gamma t)).                        (5)

The exact dynamics leaves the medium energy and number unchanged, and (4)
holds for every time, even after all R sites have formed. The full expected
system-energy increment is paid explicitly in section7. A sharp occupation
readout confined to R has exactly zero energy injection. This statement
prices a particular supplied instrument, not every physical record.

The medium is quantum in a concrete energetic sense: every occupation-diagonal
state on D has nonnegative grand energy at the chosen nu. Thus (4) cannot be
a diagonal independent-set memory dressed up as a quantum medium. It does not
prove phase, ODLRO, polarization, sound, transport across cells, or a physical
meaning for Hnu^R. The active cells here are deliberately disconnected.

At any fixed pattern on R, the exact sector ground medium also has extensive
negative grand energy. Its density satisfies

    r_D g/(2nu)<=<N_D>/V<=nu/c+2/p^3.                     (6)

These are record-sector grounds. Since mu-nu>0, the unrestricted grand ground
of Hnu^R has R blank. The construction does NOT identify filled memories with
the absolute equilibrium ground state across all record patterns.

## 2. Actual H0 and the local changed law

At each site b_x=|0><1|, n_x=b_x^dagger b_x, with commuting distinct tensor
factors. The native graph offsets are +/-2e_i and +/-e_i+/-e_j, eighteen in
all. Set m_x=sum_(y~_G x)n_y. The bare words and five collective components are

    d_i(x)=b_(x+e_i)b_(x-e_i),
    v_ij^(s,t)(x)=st b_(x+s e_i)b_(x+t e_j),
    Q_E1=(d1-d2)/sqrt2, Q_E2=(d1+d2-2d3)/sqrt6,
    Q_Tij=(1/2)sum_(s,t) v_ij^(s,t).

The actual parent is

    H0=mu N-2mu sum_x P_E(x)-mu sum_x P_T(x)
           +mu sum_x n_x binom(m_x,2)
           +tau sum_(x,k,A)|Q_A(x+e_k)-Q_A(x)|^2,
    P_E=sum_E Q_A^dagger Q_A, P_T=sum_T Q_A^dagger Q_A.    (7)

The complete landed proof gives the full-carrier positive decomposition

    H0=sum_x h_x^+,
    h_x^+=(2mu/3)|d1(x)+d2(x)+d3(x)|^2
      +(mu/4)sum_(i<j,r<s)|v_ij^r(x)-v_ij^s(x)|^2
      +mu n_x f(m_x)
      +tau sum_(k,A)|Q_A(x+e_k)-Q_A(x)|^2,
    f(m)=(m-1)(m-2)/2.                                    (8)

Every h_x^+ is positive, kills the vacuum and is supported in the nearest-neighbor lattice ball
of radius two about x, of diameter at most four. This includes the full
physical neighbor set in f; no monotonicity of f under deleting neighbors
is true or used. A useful norm bound follows directly: the singlet costs
at most6mu, the18 plane differences at most18mu, n_x f(m_x) at most136,
and the15 gradients at most240tau, since each ||Q_A||<=2. Thus

    ||h_x^+||<=h_*=160mu+240tau.                           (9)

The older trial constant A uses the parent's different, signed grouping
bound182mu+240tau. Both constants retain their actual derivations.

Let chi_x=1 on D, zero on R. Define Phi_R^0(O) by taking the product vacuum
matrix element at the R factors of O and tensoring the result with identity
on those factors. On local operators this is a unital completely positive
contraction with no support enlargement. Define the CHANGED law by

    H0^R=Phi_R^0(H0)+mu N_R,
    Hnu^R=H0^R-nu(N_D+N_R).                               (10)

Equation(10) is termwise local; it does not require a global measurement or
postselection. An equivalent explicit polynomial is obtained by replacing
b_x with chi_x b_x, n_x with chi_x n_x in the normally ordered parent (7),
and adding mu N_R. For every pair-annihilation row R_alpha,

    Phi_R^0(R_alpha^dagger R_alpha)
                      =(R_alpha with all R-touching words removed)^dagger
                       (R_alpha with all R-touching words removed).

Any annihilation word meeting R kills its vacuum factor, so no hidden constant
or surviving cross word is omitted. For a diagonal term, vacuum expectation
simply sets each n_r to zero. In particular its exact new expression is
chi_x n_x f(sum_(y~_G x) chi_y n_y), not an assertion that this expression
is below the old physical one at occupied R sites. Positivity follows from
Phi_R^0 applied to (8), not from a false neighbor-deletion inequality.

Every coupling to an R quantum factor has thus been turned off except its
onsite mu n_r. The mask is a supplied classical designation, held fixed even
when n_r later becomes one. It is not a dynamical test of n_r, a substitute
third site state, or an unmodelled memory factor. Relative to the original H0,
both transport and density couplings touching R have changed. At sites whose
radius-two support avoids R, the original h_x^+ is exactly unchanged.

Strict locality survives with diameter at most four, and every microscopic
site still has exactly M2. The mask breaks the original one-site translation
symmetry; translating/rotating the mask gives a covariant family of supplied
laws, not a derivation of a preferred mask or of the axioms' fixed nearest-
neighbor Admissibility rule.

## 3. Exact active-cell factorization and its physical boundary

The distance between distinct active cubes is at least five, including
periodic wrap. No support of diameter at most four meets two cubes. Since
h_x^+ kills the all-vacuum state, its compression is zero if its support misses
D altogether. Therefore, as an identity on the entire carrier,

    Phi_R^0(H0)=sum_(cells j) K_ell^(j),
    Hnu^R=sum_j (K_ell^(j)-nu N_j)+(mu-nu)N_R,             (11)

with disjoint cell factors. K_ell is the EXACT vacuum compression of the
original H0 on a p=ell+4 torus onto its ell-cube and vacuum corridor. It includes
all source terms based in the corridor whose surviving words act inside the
cell. It is not obtained by discarding every row based outside the cube.

This p-torus realizes the infinite vacuum boundary without aliasing: its
four guard sites per coordinate separate opposite active faces by distance
five, exceeding the interaction diameter. Its padding centers within two
steps of either face are distinct. On tori L=mp the same cell operator occurs
at every cell. In particular

    K_ell>=0, [K_ell,N_j]=0.                               (12)

Compare K_ell on its ell^3 factors with the original periodic H0,ell on the
same factors. Centers at coordinate distance at least two from each face,
(ell-4)^3 in number, have identical complete h_x^+ in the two operators.
All other terms are positive. At most p^3-(ell-4)^3 compressed centers remain;
(9) bounds each by h_*. Dropping the positive periodic boundary terms gives

    K_ell <=H0,ell +h_*[(ell+4)^3-(ell-4)^3]I
            =H0,ell+h_*(24ell^2+128)I
            <=H0,ell+30h_*ell^2 I, ell>=5.              (13)

Only the required upper comparison is asserted. No equality of open and
periodic spectra, boundary pin theorem, zero boundary kernel or unrestricted
Hamiltonian monotonicity is assumed. Formula(13) pays every surviving boundary
term by its actual operator norm. It remains valid with arbitrary many-particle
coherences and hard-core exclusions inside the active cell.

Compressing the parent's coercivity on that p-torus supplies a second useful
operator inequality, without a scalar-gas replacement:

    K_ell>=c N_j(N_j-2)/p^3.                              (14)

The vacuum compression preserves the right-hand diagonal polynomial in N;
its R contributions vanish exactly. This is the parent bound on actual physical
states, not a conjecture that independent pair fibers can all be attained.

## 4. A normalized many-particle witness that pays all record costs

The complete landed onset theorem supplies the actual periodic ell-cube state

    psi_ell(u)=exp(-iu G_ell)Omega_ell,
    G_ell=sum_x i(Q_E1(x)^dagger-Q_E1(x)),
    <H0,ell>/ell^3<=A u^4,
    |<N_j>/ell^3-2u^2|<=B u^4.                           (15)

It is the full unitary state on every occupation sector, not a bosonic ansatz
or a two-particle truncation. Its commutator remainder holds at every volume;
no ell^3 u^2<<1 hypothesis is used. Set u^2=nu/(A+nu B). Then Bu^2<1,

    <H0,ell-nu N_j>/ell^3<=-g,
    g/nu<=<N_j>/ell^3<=3g/nu.                             (16)

Put a copy of this exact state in each active cube. Equations(13),(16) give

    <K_ell-nu N_j><=-g ell^3+30h_*ell^2.                  (17)

Every cell has p^3-ell^3 marker sites. Since mu-nu>0, any state on them costs
at most (mu-nu)(p^3-ell^3). The exact count satisfies

    p^3-ell^3=12ell^2+48ell+64<=25ell^2, ell>=5.

Therefore, for arbitrary marker states (including all sites occupied),

    <Hnu^R>/number_of_cells
                  <=-g ell^3+C_nu ell^2<=-g ell^3/2.     (18)

Dividing by p^3 proves (4). This is an extensive negative GRAND energy with
positive bare H0^R. In particular it does not obtain the sign by assigning a
negative bare energy to recorded sites, removing their onsite cost, or setting
a free chemical potential only on those recorded sites.

There are 2^|R| mutually orthogonal sharp record patterns, all compatible with
the same medium trial and the bound. If ell is the smallest integer allowed
by(2), the record capacity is explicitly of order g for small nu. For example,

    r_R>=4/(ell+4)>=2g/(C_nu+5g),
    r_R<=12/ell<=6g/C_nu.                                 (19)

For the first bound, ell<=6+2C_nu/g; for the second use the elementary
1-(1+x)^-3<=3x with x=4/ell. At fixed mu,tau and nu decreasing to zero,
g is asymptotic to nu^2/A, so the required spacing ell is O(nu^-2), the
available extensive record fraction is of order nu^2, and the constructed
medium particle fraction is at least order nu. These are explicit sufficient
resource scales for this family, not optimized or necessary thresholds.
At every fixed nu in the stated interval, both fractions are strictly positive
and independent of the number of cells.

Replacing the trial by any ground density matrix of K_ell-nu N_j only lowers
(17), so its energy is at most -g ell^3/2. Positivity(12) implies
<N_j>>=g ell^3/(2nu). Combining its nonpositive grand energy with (14) and
Jensen gives <N_j><=nu p^3/c+2. Summing over cells proves (6). The same bounds
hold for mixtures or entangled states in the full ground eigenspace of the
sum of cell grand Hamiltonians, since its support is the tensor product of
the local ground eigenspaces. Degeneracy requires no state selector.

For any fixed sharp pattern on R, its additive onsite term is a constant,
so this cell medium is the exact ground within that invariant record sector.
Across DIFFERENT record sectors that constant increases with record number.
Thus the unrestricted grand ground has blank R; permanent formed records are
metastable sectors under the stipulated write-only dynamics, not claimed global
equilibrium minimizers. The new result is their coexistence with a genuine
negative-grand-energy quantum medium even after paying their costs.

## 5. The medium cannot be a classical occupation mixture

The earlier checked native readout computation has a short direct verification
useful here. For an occupation diagonal, distinct removed pairs are orthogonal.
In (8) an axial edge has one center and singlet weight2mu/3. Each plane edge
has two centers and appears in three differences at each, for weight3mu/2.
The six occurrences of each center in the gradient squares add4tau per axial
edge and3tau per plane edge. Adjacent centers never represent the same physical
pair, so cross-gradient terms have no diagonal. Thus

    Delta(H0)=mu Ddiag+(2mu/3+4tau)E_axial
                         +(3mu/2+3tau)E_plane >=c_read N. (20)

To see the last bound without independent-pair assumptions, allocate half of
each positive edge weight to each endpoint. An occupied vertex of degree zero
costs mu f(0)=mu. At positive degree it costs at least half the smaller edge
weight, while f(m)>=0 for every actual integer m. The resulting minimum is
min(mu,mu/3+2tau); the plane alternative never lowers it. This holds as a
diagonal operator inequality on the full carrier.

Vacuum compression commutes with occupation pinching on D. Apply (20) on the
p-torus and take the actual corridor vacuum matrix element:

    Delta_D(K_ell)>=c_read N_j.                            (21)

Hence any occupation-diagonal medium has
<K_ell-nu N_j>>=(c_read-nu)<N_j>>=0. Its positive-cost marker sector cannot
make the total grand energy negative. Every state in (4), and every sector
ground above, consequently has genuine occupation coherence in its D marginal.
No condensate or long-distance phase inference is required for that statement.

For any medium state with cell grand energy <=-g ell^3/2 and number at least
g ell^3/(2nu), full occupation dephasing on D injects at least

    c_read<N_j>-<K_ell>
          >=(c_read-nu)<N_j>+g ell^3/2
          >=c_read g ell^3/(2nu)>0.                       (22)

This gives an extensive quantum-energy discriminator. Conversely the record-
only pinching obeys Delta_R(H0^R)=H0^R and Delta_R(Hnu^R)=Hnu^R exactly. The
coexistence construction avoids the original-H0 full-readout cost by changing
the Hamiltonian and reserving different, decoupled sites for markers; it does
not falsify that cost or make a sharp readout of D harmless.

## 6. Actual permanent-marker dynamics and observation

Supply the finite-volume GKSL law

    dot rho=-i[Hnu^R,rho]+sum_(r in R) D[J_r]rho,
    J_r=sqrt(gamma)b_r^dagger.                             (23)

Its Hamiltonian is time independent and finite range; each jump is onsite.
It uses precisely the original one-qubit factors, with no extra pointer or
register Hilbert space. The mathematical jump-record outcome law and its
classical reporting are additional supplied Born/Markov structure.

For any r in R, P_r=n_r commutes with Hnu^R. J_r P_r=0, while every J_s with
s!=r commutes with P_r. The no-event operator is

    K=-iHnu^R-(gamma/2)sum_(s in R)(1-n_s),

and also commutes with P_r. Thus each gain and the full no-event propagation
preserve ran P_r. Equivalently (1-P_r)J_s P_r=(1-P_r)K P_r=0. This proves
absorbing permanence on ALL states already supported in P_r, with arbitrary
correlations and spectators. It checks the no-event loss, not merely the
commutator of Hnu^R with n_r. All already formed markers persist along every
allowed trajectory and after arbitrary further record-only sharp readouts.

From blank R and the product medium trial, the total law factorizes exactly.
The medium evolves under the sum of K_ell-nu N_j, conserving its mean number
and energy. Each R qubit has the independent solution

    rho_r(t)=exp(-gamma t)|0><0|+(1-exp(-gamma t))|1><1|.

There is exactly one possible formation at each r. Its timestamp is exponential
with rate gamma and its post-event state is the same-site |1>; after that the
site cannot jump or erase. These are the actual supplied channel outcomes,
not counts attached to medium particles or a proxy conserved observable.
The finite classical record consists of these site labels and timestamps.
Equation(5) follows, and

    Var(N_R(t)/V)<=r_R/(4V).

Chebyshev therefore gives the stated positive record density in probability
as the number of cells grows for every fixed t>0. At each finite set of sites
the total rate is at most gamma times its cardinality. There is no assumption
of a globally first event on the infinite lattice. Finite capacity is explicit:
records saturate R, with no renewal or erasure process asserted.

The supplied sharp readout on R is the occupation Lüders instrument. On a
formed branch its sole content is the locked |1> possibility, unaffected by
the readout; the blank branch is declared a no-readout outcome, not a readable
zero-content Record. This is a one-content marker construction. It does not
encode arbitrary different contents, choose a framework probability law, or
prove that laboratory absence detection is the framework's allowed readout.
The pointer basis, available-site mask and reporting convention are supplied.

Because the initial R state is a product vacuum and (23) factorizes, every
record history leaves precisely the same evolving medium state. This stronger
history-independence uses that preparation. For correlated initial states only
the unconditional medium marginal evolves autonomously; conditioning on R
can reveal those prior correlations. Permanence itself did not require the
product preparation.

## 7. Formation energy and what changed

Both energies have an exact finite-volume balance. The medium contribution is
constant, and each newly formed record adds bare energy mu. Thus

    d<H0^R>/dt=mu gamma sum_(r in R)<1-n_r>,
    d<Hnu^R>/dt=(mu-nu)gamma sum_(r in R)<1-n_r>.             (24)

From blank R the total respective increments are mu|R|(1-exp(-gamma t)) and
(mu-nu)|R|(1-exp(-gamma t)). The uniform worst-case allowance in (18) pays the
entire latter increment, so the total grand energy stays negative throughout
formation and at saturation. The bare Hamiltonian remains nonnegative.
A chemical-potential subtraction is not a source of physical energy.

The GKSL law supplies an external formation source. It is not an autonomous
positive-energy apparatus construction. If an apparatus implements it, its
endpoint energy and interaction ledger must pay (24); neither negative grand
energy nor zero record-readout injection makes formation free. Readout-only
Delta_R changes neither displayed energy, while readout of the medium has the
positive price(22). These statements keep source cost and readout cost separate.

The original H0 has a scalar strictly local commutant on its full carrier and
cannot be repaired into a common sharp marker law by arbitrary GKSL noise
without changing its Hamiltonian. Here (10) explicitly removes the exterior
four-ladder transport coefficients at R and changes the stabilizer there.
There is no contradiction: the theorem's unchanged-H0 hypothesis is gone.
Unlike its independent-set memory, the present D factor supports a negative
coherent grand medium and retains every original interaction deep inside each
large active cell. Unlike a full physical record bridge, designated positions,
finite-density preparation, guards, basis, time and jumps are not derived.

No claim extends permanence to occupied D sites. The R designation does not
follow particles or grow in response to medium events. It is an externally
fixed mask even though the actual record population on it grows dynamically.
Intercell quantum transport is absent. The construction does not preserve the
unmodified full translation-covariant H0, prove its phase survives dilute
obstacles, or make all potential local M2 possibilities readable permanent
contents. A law-selected and spatially covariant dynamically expanding record
set coupled to a connected quantum medium is a different remaining obligation.

## 8. Source, proof and verification boundary

The complete landed H0/coercivity/onset proof at mainfb5 (SHA7180c065) was
freshly read. The complete earlier native record-compatibility derivation,
sharp-readout proof and their focused root receipts were read, including their
positive escape and non-ground-medium limits. The earlier dilute-phase proof
was read for scope; no phase, many-pair threshold or open EOS theorem is used.
Current memo, registry/classification and three primitive sources were verified
at their unchanged actual main identities and retain their precise grants.

The new proof is analytic. It uses a positive local vacuum compression, an
actual finite-cell norm comparison, the landed exact unitary trial, and exact
factorization/GKSL invariance. No numerical result, unproved cell kernel,
independent-dimer embedding or monotonic deleted-neighbor bound is needed.
No science runner has been executed. File/hash operations are not experiments.

Prior exposure: root suggested designated sites, guards and cells; this agent
previously authored the record/readout packets and participated in onset and
thermodynamic work. The contract was frozen first; the present complete mechanism is frozen
with this proof before opening any root alternative PRE. That PRE has not
been read. This is
an author route, not independent review of its reused inputs. The frozen result
requires focused independent reconstruction before downstream use.
