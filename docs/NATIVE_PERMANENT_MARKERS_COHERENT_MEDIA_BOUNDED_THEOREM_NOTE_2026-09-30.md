---
claim_id: native_permanent_markers_coherent_media_bounded_theorem_note_2026-09-30
claim_type: bounded_theorem
claim_scope: "Two explicitly changed local Hamiltonian/GKSL laws on full one-qubit site factors: vacuum-compressed fixed corridors support paid permanent markers beside prepared coherent negative-grand-energy cells for all times; a translation/proper-cubic-covariant isolated-motif law supports permanent motifs and a volume-uniform positive interval of positive mean motif density and negative grand energy. Basis, preparation, mask/motif, law, clock and instrument remain supplied. No phase, physical source selection or complete framework realization."
upstream_dependencies: [minimal_axioms, native_qubit_pair_density_onset_bounded_theorem_note_2026-09-30]
runner: scripts/native_permanent_markers_coherent_media_2026_09_30.py
---

# Permanent qubit markers beside prepared coherent media

**Status:** conditional-support (supplied models; unaudited).
**Type:** bounded_theorem
**Primary runner:** `scripts/native_permanent_markers_coherent_media_2026_09_30.py`.
**Paired cache:** `logs/runner-cache/native_permanent_markers_coherent_media_2026_09_30.txt`.

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
conditional_surface_status: "Two supplied local laws, preparations and formation/readout instruments"
hypothetical_axiom_status: "none proposed"
admitted_observation_status: "none used"
claim_type_reason: "Complete conditional finite-volume/all-volume operator and dynamical estimates"
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Independent complete source review; physical record/law/source bridges remain separate"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

The target is conditional coexistence of permanent sharp markers and a
prepared coherent many-particle medium on the same M2 site factors under
explicitly changed finite-range laws. The two constructions trade spatial
and temporal conditions: fixed corridors isolate quantum cells and pay all
marker costs at saturation; the motif law uses no external record sublattice
but its negative-grand-energy guarantee is an initial finite-time interval.
Neither construction selects the framework's actual law or physical records.

The [actual native parent](NATIVE_QUBIT_PAIR_DENSITY_ONSET_BOUNDED_THEOREM_NOTE_2026-09-30.md)
is the mathematical input: its full-carrier positivity, coercivity and exact
normalized pulse are used at their stated L>=5, mu,tau>0 domain. All new
boundary, pinching, packet, persistence and time estimates are proved below.
The [current minimal memo](MINIMAL_AXIOMS_2026-06-29.md) fixes the premise
boundary; it supplies neither Hamiltonian/GKSL/clock nor this readout encoding.
Current registered primitives keep their actual grants, without selecting
these structures. No open EOS, spectrum or threshold proposal is a premise.

## Fixed-corridor construction

### 1. Result and resource statement

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

### 2. Actual H0 and the local changed law

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

### 3. Exact active-cell factorization and its physical boundary

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

### 4. A normalized many-particle witness that pays all record costs

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

### 5. The medium cannot be a classical occupation mixture

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

### 6. Actual permanent-marker dynamics and observation

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

### 7. Formation energy and what changed

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

Here (10) explicitly removes transport coefficients at R and changes the
stabilizer there. Every conclusion is about that changed law; no unchanged-H0
permanence result is asserted.
The present D factor supports a negative coherent grand medium and retains
every original interaction deep inside each large active cell. Unlike a full physical record bridge, designated positions,
finite-density preparation, guards, basis, time and jumps are not derived.

No claim extends permanence to occupied D sites. The R designation does not
follow particles or grow in response to medium events. It is an externally
fixed mask even though the actual record population on it grows dynamically.
Intercell quantum transport is absent. The construction does not preserve the
unmodified full translation-covariant H0, prove its phase survives dilute
obstacles, or make all potential local M2 possibilities readable permanent
contents. A law-selected and spatially covariant dynamically expanding record
set coupled to a connected quantum medium is a different remaining obligation.


## Covariant isolated-motif construction

Equation numbers restart within this construction. Its H'_0 and H'_nu are
different supplied laws from the corridor operators H0^R and Hnu^R.

### 1. Literal definitions and local modification

Use precisely the native parent H0 defined above, with the same mu,tau and physical site factors. On a cubic torus with L>=18 let b_x=|0><1|, n_x=b_x* b_x, N=sum n_x. The parameters mu,tau,gamma are positive, and 0<nu<mu/3. Let B_r(x) denote the coordinate cube of radius r in the torus metric, and v=|B_2|=125. Supply

    P_x=n_x product_(y in B_2(x),y!=x)(1-n_y),
    Q_x=product_(y in B_2(x))(1-n_y),
    J_x=sqrt(gamma) b_x* product_(y in B_2(x),y!=x)(1-n_y).       (1)

P_x marks an isolated occupied center with an empty radius-two collar. Its content is the fixed occupation |1> at x. This is a finite-block presence encoding; n_x=1 alone does not identify a formed record. Its basis/content choice and readout identification are supplied. Blank or mobile occupations are not declared readable records.

All P_x commute. Define their simultaneous pinching on the finite torus by composing

    E_x(A)=P_x A P_x+(1-P_x)A(1-P_x),  E=product_x E_x.

The order is immaterial. Define a NEW Hamiltonian and a NEW formation law

    H'_0=E(H0),  H'_nu=H'_0-nu N,
    L(rho)=-i[H'_nu,rho]+sum_x D[J_x](rho).                     (2)

E is a mathematical definition of Hamiltonian coefficients. It is not an actual measurement, extra grade observation, added site factor or intermediate physical operation. The jumps in (1) are the observed site labels of this new model. They are not substituted for any original compensated rotor jump.

The whole local law is translation and proper-cubic covariant. No record sublattice or distinguished position appears in it. The internal basis, motif radius, quantum tensor realization, expectation/Born rule, clock and parameters are nevertheless additional choices; no nearest-neighbor admissibility distribution or complete framework realization is derived.

The landed source groups H0=sum_x h_x, supp h_x subset B_2(x), ||h_x||<=J=182mu+240tau. A projector P_y disjoint from supp h_x commutes with h_x. Since all the pinches commute, its action remains irrelevant after applying the other pinches. Only y in B_4(x) can act, and their supports lie in B_6(x). Thus h'_x=E(h_x) has support in B_6(x) and norm at most J. Equation(2) is uniformly finite range, despite using a convenient global formula for E. L>=18 suffices for these support/count upper bounds without creating distinct-site assumptions across a seam.

E is positive, unital, and fixes every function of N and every diagonal occupation operator. Consequently the actual landed inequalities pass unchanged:

    H'_0>=0,  H'_0>=c N(N-2)/V,
    c=min(tau,mu/12)/99090432,  V=L^3.                         (3)

Also [H'_nu,N]=[H'_nu,P_x]=0. These are full-carrier identities.

The completion H0=S+mu Ddiag+Wtau in the source gives a useful record debit. Ddiag=(1/2)sum_x n_x(m_x-1)(m_x-2), with m_x the eighteen-neighbor pair-graph occupation. Each summand is nonnegative; on P_x, m_x=0 and that summand equals1. Therefore Ddiag>=M:=sum_x P_x, and

    H'_0>=mu M,  H'_nu>=mu M-nu N.                            (4)

No record energy has been subtracted or hidden in a changed energy zero.

### 2. Full-state persistence and exact formation balances

If x=y, P_x J_x=J_x, J_x P_x=0 and J_x*J_x=gamma Q_x. If 0<dist_infinity(x,y)<=2, both P_y J_x and J_x P_y vanish: a jump whose empty collar contains an existing occupied y is blocked, and its output occupied x is incompatible with P_y's empty collar. If dist_infinity(x,y)>2, the offdiagonal factor at x is outside supp P_y and all remaining factors are diagonal, so J_x commutes with P_y. These statements include overlapping empty collars.

Every jump preserves each already formed marker. The no-event generator -iH'_nu-(gamma/2)sum_x Q_x commutes with every P_y. Hence every range P_y is invariant under the full quantum semigroup, including arbitrary input correlations and mixtures. Along the usual finite-volume quantum-jump realization, marker patterns can only gain the jump's site. There is at most one such event at each site, and total rate is at most gamma V, so no finite-volume explosion occurs. An all-blank start is not asserted to generate the prepared quantum medium below.

The adjoint generator obeys the exact operator identities

    L*(P_x)=gamma Q_x,
    L*(M)=L*(N)=gamma sum_x Q_x,
    L*(N-M)=0.                                                (5)

Thus the number of non-motif particles is conserved in expectation and, from a simultaneous definite N/M input, along each trajectory. This does not prove that they remain mobile or in a phase. Because the Q_x are all-empty projectors, the elementary union bound on each occupation word gives

    sum_x Q_x >= V-v N,  0<=sum_x Q_x<=V.                      (6)

The lower bound may be negative at high density, where it says nothing useful. It is an operator inequality since all its terms are diagonal.

### 3. Explicit quantum preparation with no markers

Choose integer ell>=10 large enough that

    3 pi^2 tau/(ell+1)^2 <= nu.

Set D=ell+8, and require L to be a positive multiple of D. Partition the torus into D-cubes. Inside each choose center cube {1,...,ell}^3, with coordinates relative to that cell. On this center cube take the normalized Dirichlet sine function

    f(x)=[2/(ell+1)]^(3/2) product_(i=1,2,3) sin(pi x_i/(ell+1)),

and extend it by zero. In each cell prepare

    phi_f=sum_x f(x) Q_E1(x)* Omega,
    Q_E1(x)=(b_(x+e1)b_(x-e1)-b_(x+e2)b_(x-e2))/sqrt(2).

Its physical occupied support lies in {0,...,ell+1}^3. The opposite axial pairs have unique centers and are mutually distinct at L>=5. Therefore ||phi_f||=1, N phi_f=2 phi_f, and Q_A(y)phi_f=delta_(A,E1)f(y)Omega. The source's D0 singlet and all plane-difference squares kill it; each configuration is a pair-graph edge so Ddiag also kills it. Thus its exact isolated energy is

    <phi_f,H0 phi_f>=tau sum_(x,i)|f(x+e_i)-f(x)|^2
                   =12tau sin^2(pi/[2(ell+1)]) <=nu.           (7)

This is an exact qubit two-particle calculation, not a bosonic replacement or numerical spectral estimate.

Tensor these states over the disjoint cells, with every remaining site empty, obtaining Phi_L. Neighboring occupied supports are separated by at least seven lattice spacings. H0 has interaction diameter at most four; no interaction term meets two occupied supports. Every local term vanishes in the empty product, so the expectation is exactly the sum of the isolated packet expectations. The particle density is exactly rho0=2/D^3.

Every occupied particle in every basis configuration has its pair partner at coordinate distance at most two. Consequently P_x Phi_L=0 for every x. The entire state lies in the zero-marker block of E, whence <H'_0>=<H0>. With eta=nu/D^3,

    <Phi_L,H'_nu Phi_L>/V <=-eta<0,
    <M>_0=0,  <N>_0/V=2/D^3 <=1/(2v).                        (8)

The last bound follows from D>=18. No global small-particle-number approximation is used: Phi_L has 2V/D^3 actual qubits occupied. Averaging its density matrix over all torus translations gives a translation-invariant preparation with exactly the same bounds and no markers. Proper-cubic averaging is also possible. This averaging is a supplied preparation, not a typicality or realized-state assertion.

### 4. Actual positive-time coexistence, with energy cost retained

Evolve that literal initial density matrix by(2); no trajectory conditioning or postselection is used. From(5)-(6),

    <N>_t/V <=rho0+gamma t,
    d<M>_t/dt >=gamma[V-v<N>_t].                              (9)

For 0<=t<=1/(4v gamma), rho0<=1/(2v) gives

    gamma t/4 <= <M>_t/V <=gamma t.                           (10)

For the energy set h'_(nu,x)=h'_x-nu n_x, with norm at most J+nu and support B_6(x). D[J_y]*h'_(nu,x) vanishes when dist_infinity(x,y)>8; at most17^3=4913 jump centers can contribute per x. Each individual dissipator norm is at most2gamma||h'_(nu,x)||. The Hamiltonian part cancels in L*(H'_nu). Therefore, defining C=9826(J+nu),

    |d<H'_nu>_t/dt|/V <=gamma C.                              (11)

This includes complete gain and loss; it is not a per-click energy formula or an energy-conserving reservoir model. Fix the positive volume-independent time

    T_*=min(1/(4v gamma), eta/(2gamma C)).                      (12)

For every 0<t<=T_* the actual evolving state satisfies

    <M>_t/V >=gamma t/4>0,
    <H'_nu>_t/V <=-eta/2<0.                                   (13)

Existing and newly created motif records remain permanent for all later times, even though the negative-energy estimate is asserted only on this interval. There is no promise of a stationary birth flux or indefinitely sustained negative-energy medium. Equation(4) explicitly charges record creation and is consistent with the finite-time restriction.

### 5. Why this is a quantum-medium witness, and its precise limits

There is a simple coherence discriminator that needs no phase assumption. On a classical occupation word, the diagonal of S_E gives2mu/3 per axial pair edge, while the diagonal of S_T gives3mu/2 per plane pair edge. Since Wtau is positive its diagonal is nonnegative. Thus, writing m for each occupied site's pair degree,

    <word,H0 word> >=mu sum_x n_x[(m_x-1)(m_x-2)/2+m_x/3]
                    >=(mu/3)N(word).                          (14)

For integer m=0,...,18 the bracket has minimum1/3 at m=1 (m=0 gives1, m=2 gives2/3, m>=3 gives at least2). Pinching leaves all occupation-basis diagonal entries unchanged. Every occupation-diagonal state consequently has <H'_nu>>=(mu/3-nu)<N>>=0. The strictly negative expectation in(13) proves that the actual evolving state retains occupation coherences. It does not establish entanglement, a thermodynamic phase, ODLRO, a sound pole, homogeneous susceptibility or a gravitational mode.

The construction supplies an extensive permanent one-content motif density at actual positive times together with an extensive quantum low-energy witness on the same M2 factors. It preserves positivity/coercivity but changes native transport near motifs. No claim is made that H'_0 has the original H0 kernel, equation of state, scattering, spectrum or record incompatibility theorem. Here P_x is a finite-block presence projector, not the common rank-one site projector n_x on the whole carrier. No statement about unchanged-H0 record realizations is needed.

Open physical obligations: select/derive this changed law or another law; relate motif presence and the fixed local content to the actual admissibility/readout rule; supply meaningful multiple contents and a physical preparation; include an apparatus/source conserving physical energy; identify a physical clock; prove longer-time/thermodynamic collective behavior and any coupling to gravity. The nearest-neighbor admissibility distribution and content variation are not supplied by(1). This is a conditional feasibility result for an optional mechanism, not a completed framework realization or evidence of axiom inconsistency.

### Blank-input invariant and preparation domain

The products used in the persistence proof give [M,J_x]=J_x, while
[N,J_x]=J_x. Hence N−M commutes with every jump and the complete no-event
generator. Starting from the empty vector, the actual state stays in N=M.
The record debit then gives <H'_nu>>=(mu−nu)<N>>=0 for that preparation.
This is a positive invariant and energy lower bound for the displayed law.
The negative-energy conclusion uses the specified coherent pair preparation;
no preparation from blank input is established by the formation process.

The energy floor H'_0>=mu M is distinct from a per-click work equality.
For motifs only the proved full gain/loss energy-rate bound is claimed.
For the decoupled corridor law, the stronger exact formation increment mu
per marker was separately derived. Neither statement supplies an autonomous
apparatus or a physical energy source.

## Proof scope, inputs and evidence

The obligation chain is explicit. The native parent proves positivity,
coercivity and the all-volume normalized pulse. The corridor proof establishes
positive local compression, physical surface control, paid saturation, sector
bounds and full channel factorization. The motif proof establishes finite-range
pinching, full-carrier persistence, an actual physical N2 packet, finite-volume
packing, birth balances and a uniform finite-time energy estimate. The
occupation-diagonal inequalities establish only a coherence discriminator.
All new steps are proved here; no terminal lemma is deferred inside either
conditional theorem.

The remaining physical task is a supplied-to-physical bridge for law, record
meaning, admissibility, source, clock and preparation. It is not asserted to
follow from negative grand energy or a conserved marker projector. The
corridor medium is disconnected and uses an external mask; the motif medium
has only the displayed finite-time expectation estimate. Neither conclusion
is an EOS, phase, ODLRO, sound, gravitational or original-rotor theorem.

The new primary tests literal finite occupation-word actions, marker pinching,
packet normalization, full gain/loss projector identities, positive diagonal
bounds, vacuum compression and physical cell counts. Its finite fixtures do
not prove the all-volume/time statements; those are the analytic arguments
above. Expected values and independent derivations, actual execution records,
source-bound cache and scratch mutations are in the owned pack
[historical author packet](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/30fddd97f8909d791d4e116c4635b25122487862/.claude/science/physics-loops/native-record-medium-20260930/).
The primary and cache are not independent evidence from the reused root motif
control. Its general-coupling stabilizer uses exact rational multiplication
with division of the integer combinatorial factor, avoiding the historical
0/1-only floor-division convention.

Two prior focused reconstructions checked the constructions separately:
corridor proof0a213ecd / root receipt d3f98bbe, and motif proof04f94960 /
receipt492d65f2. Exact original bytes and manifests are preserved under the
pack's `provenance/`. They are focused source-bound checks, not formal review
of this combined source or audit authority. Prior author roles and mechanism
exposure are recorded there. The combined unit needs a fresh complete source
review; integration and audit remain separate requirements.

Historical author preparation, actual failed controls, mutation results and source-review provenance remain recoverable through [PR #9415](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/9415) at frozen head `30fddd97f8909d791d4e116c4635b25122487862`. They are provenance, not current proof premises or audit authority. The canonical argument and its linked current supporting proofs own the theorem; finite runner controls do not supply its analytic quantifiers.
