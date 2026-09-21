# Final independent review of the loop diagnostic and local-curl/native construction

Date: 2026-09-21. This is mathematical source review, not a blind derivation
of an unseen proposal: I fully read both requested new notes, then
reconstructed their arguments and wrote the accompanying checks without
opening their author checkers or results. The earlier independent proof
dependencies retain their sealed identities. No production source, Git,
PR, audit status or unrelated file was changed.

**Final result:** no actionable mathematical correction or source/code drift
was found in the reviewed revisions. The collective-loop conditional-law
obstruction, the alternative local-curl encoding, the full fourteen-field
reaction/current linearization, the native entropy extension, and Section
8's ordered late-state/canonical covariance argument are supported under
the stated hypotheses. This does not prove native finite-time Gaussian
fluctuations, uniform mixing rates, a simultaneous time/volume limit, or a
physical electromagnetic identification.

The initial proof reconstruction and twelve exact independent controls
were sealed before the three author checkers/results were opened. Those
sources and complete logs have now been read and authenticated; none was
executed merely to reproduce its PASS count. Sections 2-7 reproduce the
independently reconstructed mathematics. Section 9 records the subsequent
source comparison. No audit/retention verdict is applied.

## 1. Sources, premises and read boundary

The two new sources were read completely:

- NEAREST_NEIGHBOR_LOOP_FORMATION_DIAGNOSTIC.md, 95 lines, SHA-256
  f1d5234bbff516995f2ec445c889fb9bc4eaccf381274b382d3206b2dec33d3f.
- LOCAL_CURL_READOUT_AND_NATIVE_FORMATION.md, 326 lines, SHA-256
  a300dc4f0095cc274b6b9f4d82f0466e0cad55011c48b94e644617c4ee18280f.

The unchanged model and earlier independent Euler, native-formation,
transverse, stationary and growing-fluctuation reports were authenticated.
I reread the entire native Euler and transverse independent reports, and
the full current minimal-axiom memo. The other unchanged proofs are reused
by identity, not rederived for a new PASS count. SOURCE_IDENTITIES.json
records the complete source and instruction hashes. In particular, the
four-site context model uses simple cubic tori N>=4, a fixed strictly
positive exchange floor, bounded fixed finite-range rates, and immutable
whole-label swaps. The loop counterexample uses N>=7.

The new construction has fifteen states (vacancy, six A axes, eight B cube
corners), unlike the thirteen-state unit-axis loop construction. For the
native theorem the macroscopic generator is N L_N + R_N, with per-label
macroscopic insertion beta times the six-neighbor weight product. This
corresponds to microscopic beta/N; fixed microscopic beta would be a
different scaling. The source labels beta>0 and 0<|j|<1 for native growth,
then explicitly treats j=0 as a separate inherited case. Gamma may be zero,
but propagating-mode assertions already require gamma!=0 and K!=0.

The Fourier convention is V^{-1/2} sum_x exp(-ik.x) f(eta_x), V=N^3.
For a continuum mode K=2pi m, k=K/N. Negative modes are conjugates for
real-valued features. Equal-time covariances below are conjugated ones.

## 2. Collective-loop conditional-law counterexample

Fix a label of species s, sign +/- and axis i at x. In each of the two
planes containing i, x can be either of the two opposite i-record sites.
Once the label at x is specified the circulation is fixed. Thus there are
four candidate loop events, whose other sites are, for j!=i and sigma=+/-,

    x+2 sigma e_j, x+sigma e_j+e_i, x+sigma e_j-e_i.

Each has rate beta/N when all four sites are vacant. This derives h_i.
There are four signed/species labels of each axis, so the total event rate
seen at x is 4 sum_i h_i, and the conditional single-label probability is
h_i/(4 sum_i h_i). Simultaneity of the other three births creates no extra
factor at x: an event contains exactly one target record there.

In empty space all twelve probabilities are 1/12. The supplied yz-loop
centered at (2,0,1) has exactly zero D2 divergence. Its only intersection
with any candidate birth through 0 is the record at 2e_1; none of the
six nearest neighbors of 0 is occupied. This removes one event for axes 2
and 3, and none for axis 1. The counts are therefore (4,3,3) and the
probabilities are 1/10 for each signed/species x label and 3/40 for each
signed/species y or z label. The total event counts are 48 versus 40.

The checker enumerates all centers, planes, circulations and species on
the N=7 torus independently of the displayed h_i expression. It obtains
exactly these template counts and checks the two divergence/neighbor
claims. A common rate multiplier cancels in the conditional probabilities.
This is a counterexample to this particular formation law under the
current conditional-on-formation reading of Admissibility, not to every
Gauss-preserving nearest-neighbor law.

The final geometric restriction is valid on Z^3: at a maximal first
coordinate M of a finite support, an E_1 record at r would make an
uncancelled charge at r+e_1, since all other possible contributing sites
have first coordinate larger than M. Hence E_1 vanishes at every occupied
site in that extremal plane. A fixed finite footprint cannot give every
axis positive marginal probability at every one of its sites. This does
not apply to arbitrary winding periodic configurations or prove that
random-footprint alternatives fail.

## 3. New local readout and positive native weights

Let raw features be e=+/-e_i on A and b in {+/-1}^3 on B, with the other
feature zero. Put U=2e, V=b. For centered d_i, the discrete curl C=d cross
has d.C=0 because the differences commute. Therefore

    E_lat=C V, B_lat=-C U

obey both Gauss identities for every configuration, and hence for every
allowed exchange or birth. No probabilistic closure is involved. The
checker verifies the convolution identity on all thirty e/b elementary
label impulses on N=7; linearity proves the configuration statement.

If U is polar and V axial, E_lat is polar and B_lat axial. The new weight
W_ab=1+j[e_a.e_b+b_a.b_b/4] is invariant under all 48 signed cubic actions
with that polar/axial convention. Its bracket lies in [-1,1], its occupied
row sum is 14, and 1-|j|<=W<=1+|j|. The checker verifies every pair under
all 48 actions, including reflections. For j!=0 the normalized birth
odds vary with the six nearest-neighbor labels; no remote acceptance
factor is present.

This is an additional, local derived field readout. It does not turn the
raw longitudinal, scalar or higher moments into inaccessible quantities,
identify a physical electric/magnetic observable, derive the menu from a
qubit algebra, or create a gauge equivalence. Mathematical zero features
at vacancy are bookkeeping, not a new readable empty-site record. Every
periodic curl has zero total flux; even tori also have the centered-symbol
high-frequency zeros. The note states these limits correctly.

## 4. Entropy extension: the load-bearing steps

For independent local label law p, write X=<e>, Y=<b>, p0=1-sum p_a and

    m_a(p)=1+j[e_a.X+b_a.Y/4],
    B_a(p)=beta p0 m_a(p)^6.

The center and its six distinct neighbors are independent in the
local-equilibrium average. This is the product reaction used in the
hydrodynamic equation, not a statement that the actual finite native law
evolves through products.

The conservative current is the unchanged fourteen-species current

    J_a=gamma p_a[e_a cross Y+X cross b_a-2X cross Y].

Its nonlinear entropy compatibility follows from
Psi=gamma X cross Y and J_i=C(p) grad Psi_i,
C=diag(p)-pp^T, H=C^{-1}; thus H D J_i is symmetric in the fifteen-label
interior. The positive exchange floor connects every finite count sector.
The finite-alphabet Euler hypotheses already checked for this current
therefore remain available.

At a uniform fifteen-label reference pi, the birth adjoint at an occupied
center contributes one incoming rate beta product W; at a vacancy its
contribution is the negative sum of fourteen rates. Consequently

    R_N^*1 <= beta(1+|j|)^6 V.

There is no missing factor 14 in this upper bound. If
f_t=d mu_t/d pi and D_N(f)=sum_edges E_pi( sqrt(f^edge)-sqrt(f) )^2, the
conservative entropy dissipation and initial H(mu_0|pi)<=V log15 give
the displayed integrated D_N(f_t) bound (5), conservatively with N kappa
in the denominator. D_N is applied to f, not to its square root again.

The exact local source-adjoint term relative to an inhomogeneous product,
averaged under a block product q with the reference center p frozen, is

    F(p,q)=beta sum_a [q_a p0/p_a-q0] m_a(q)^6.

At q=p every central bracket vanishes, so F(p,p)=0 and derivatives of
the neighbor factors cancel. In occupied coordinate b,

    D_b F(p,p)
      = beta[p0 m_b(p)^6/p_b+sum_a m_a(p)^6]
      = [H(p)B(p)]_b.

The checker obtains the same derivative from the center and all six
neighbor score contributions at a biased fifteen-label rational reference.
This is not a pointwise source cancellation; the one-block step is needed.

For completeness, that replacement does extend. On an ell^3=M block,
count sectors remain connected, the crude canonical Poincare constant
M^2 15^M is sufficient, and marginal square-root-density energy contracts.
A fixed seven-site footprint sampled without replacement differs from
product sampling at the empirical frequencies by O(1/M). Two disjoint
footprints give covariance O(1/M); overlapping anchor pairs are O(M).
Block boundary loss is O(1/ell). These facts and the integrated energy
budget give the same per-volume replacement error, with alphabet constant
15 replacing 7, bounded by constants times

    ell^(-1)+sqrt(M^3 15^M/N).

Smooth reference coefficients introduce O(ell/N). For reference p in a
compact interior set, the Hessian in q of F is bounded on the entire
closed q-simplex, since m_a(q)^6 is polynomial and only reference p_a
occurs in denominators. Thus count blocks near a boundary do not require
an additional positivity assumption. The entropy inequality controls the
remaining quadratic empirical-density term, and Gronwall closes after
N grows and ell grows slowly, for example M<=log N/(2 log15).

The target must be a given C^2 solution of the displayed reaction-
conservation law, uniformly interior on the fixed interval, and initial
relative entropy must be o(V). Those hypotheses are stated. No exact
product evolution, global nonlinear smoothness, native fluctuation theorem
or estimate uniform as T grows follows from this argument.

## 5. Full fourteen-field linearization and covariance witness

Use the invertible feature basis

    rho; d=4rhoA-3rhoB; U_1,U_2,U_3; V_1,V_2,V_3;
    r_1,r_2; M_12,M_13,M_23,M_123,

where r_i=qA_i-rhoA/3 and M_S are B Walsh moments. This is fourteen
independent fields (the omitted r_3 is -r_1-r_2). The checker assembles
this basis directly from all labels; its determinant is -1835008.

Along equal-per-label homogeneous products p_a=rho/14, the PDE background is

    rho'=14 beta(1-rho), rho(t)=1-v0 exp(-14 beta t).

It is globally smooth and interior on every fixed finite interval if
0<rho0<1. Differentiating all fourteen species sources gives, in the
displayed feature basis,

    D B=diag(-14beta,0,lambda I_6,0 I_6),
    lambda=12 beta j(1-rho).

The zero fields total seven: d, two A quadrupoles, three B pair characters,
and the B triple character. Both vector species have the same eigenvalue
because sum_A e_i e_j=2delta_ij and sum_B b_i b_j=8delta_ij, combined
with the deliberate factor 1/4 in W.

The full directional current matrix vanishes on the other eight fields.
On (U,V), with C_K w=K cross w and c=2gamma rho/7, it is

    A(K)=[[0,-c C_K],[c C_K,0]].

The evolution generator on that block is lambda I-i A(K). Its complete
fourteen-field characteristic polynomial is

    z^7 (z+14beta) (z-lambda)^2
          [(z-lambda)^2+c^2 |K|^2]^2.

Thus for nonzero K and gamma, the four transverse modes have drifts
lambda+/-i c|K|, the two raw longitudinal components have drift lambda,
density has drift -14beta and seven fields have zero drift. If gamma=0
or K=0 the wave splitting degenerates. No field has been discarded.

All temporal matrices commute on this homogeneous equal-label trajectory:
the vector scalar reaction and the fixed curl matrix commute, while
density/spectators are separate blocks. Integrating lambda gives exactly

    exp[(6j/7)(rho(t)-rho(s))].

The phase is |K| times the integral of c. This is a justified
nonautonomous solution, not integration of unrelated frozen eigenvalues.
Curling gives exactly the signs in (9); the coefficients must be spatially
homogeneous, as the note states.

To test finite-native product preservation directly, take adjacent x,y.
At a birth at x, its five other neighbor factors have exact product mean
one. Summing the marked new U_i over the fourteen labels leaves
2j U_i(y); its current product variance is 4rho/7. The contribution is
8 beta j rho(1-rho)/7, and the other endpoint doubles it. The same holds
for V. Therefore the connected derivative is exactly

    16 beta j rho(1-rho)/7.

The checker sums the marked local generator, subtracts the mean-drift
terms, and checks the entire 14x14 adjacent connected-covariance
derivative: only these six vector diagonal entries are nonzero. A
separate exact witness beta=2/3, rho=3/5, j=-1/2 gives -32/175.
The exchange contribution is zero by its product stationarity, even with
N acceleration. This rules out exact native growing product evolution;
it does not invalidate Euler local equilibrium.

## 6. Uniform births, Fourier normalization and comparator scope

Only at j=0 does the inherited exact growing-product finite-mode theorem
apply directly. Under its equal-per-label trajectory,

    C_U=C_V=(4rho/7)I, C_UV=0,
    Q_U=Q_V=8beta(1-rho)I, Q_UV=0.

The birth bracket is a sum of marked jump squares, not the covariance of
a fixed number of categorical draws. The earlier theorem covers fixed
finitely many modes/times on a fixed horizon; it gives the Gaussian
diffusion including formation noise. Empty/full endpoints, where used,
come from the earlier separately proved boundary/restricted-model
arguments, not inversion of the interior fifteen-state entropy metric.

For exp(-ik.x), centered curl has symbol i sin(k) cross. Thus the
correct continuum readout is N times the microscopic derived field.
With K fixed and k=K/N, N sin(K/N) tends to K, giving

    S_E=S_B=(4rho/7)(|K|^2 I-KK^T),
    Q_E=Q_B=8beta(1-rho)(|K|^2 I-KK^T).

The cross covariance is zero. Omitting the factor N makes the fixed-mode
covariance vanish. The derived noise is exactly transverse, unlike the
raw U/V birth noise. This says nothing about ultraviolet tightness or a
native-j fluctuation theorem.

For a finite-range linear encoding of arbitrary underlying features,
the analytic Fourier matrix A(k) obeys sin(k)^T A(k)=0. Substituting
k=t v and taking the leading coefficient proves v^T A(0)=0 for every v,
hence A(0)=0 and A(k)=O(|k|). A bounded underlying spectral density then
gives O(|k|^2) derived covariance. These are essential hypotheses;
constrained inputs, nonlinear encodings and unbounded spectral densities
are not ruled out.

The two comparator shapes are correctly distinguished: transverse
potential covariance proportional to |k|^-2 produces constant projector
field covariance under curl; proportional to |k|^-1 produces |k|
projector covariance. For the additional canonical oscillator
H=(p^2+omega^2 q^2)/2, [q,p]=i, its Gaussian ground-state density gives
Var(q)=1/(2omega), Var(p)=omega/2; with omega=|k| both electric p and
magnetic |k|q have variance |k|/2. Neither that Hamiltonian nor that
commutator is supplied by the stochastic record model.

## 7. Ordered late-state selection and exact canonical Fourier covariance

This argument is distinct from a native fluctuation theorem.

Let M_t be the vacancy count on a fixed torus. Every vacant site has total
birth rate at least

    r_min=14 beta(1-|j|)^6>0.

Motion preserves M; each birth reduces it by one. For
F(m)=H_m/r_min, with H_0=0, the generator satisfies

    L F(M) <= -1 whenever M>0.

Optional stopping after truncation and then monotone convergence give
E tau_full<=H_M0/r_min. Thus absorption into full occupancy occurs almost
surely at each finite N. The checker verifies the exact harmonic
Lyapunov identity. This does not make the entire configuration absorbing:
whole-record exchanges continue at full occupancy.

For each label a, subsequent births after a fixed T add at most M_T records,
while exchanges never alter counts. Consequently

    P_N,a(T) <= P_N,a(final) <= P_N,a(T)+V_N(T)

pathwise. The finite-T Euler law of large numbers gives
P_N,a(T)->(1-v(T))/14 and V_N(T)->v(T), where
v(T)=v0 exp(-14beta T). Given a desired accuracy choose a large but fixed
T, then use the finite-T theorem as N grows. This proves every final
fraction tends in probability to 1/14. No hydrodynamic theorem at a
volume-dependent saturation time is used.

For each final count vector, the positive-floor nearest-neighbor swaps
connect all arrangements. The uniform sector law is invariant by the
pointwise periodic telescoping identity of the context drive, also at
full occupancy. The finite continuous-time chain is irreducible and
converges to that law; reversibility is unnecessary. Conditioning on the
absorption state and using the finite-state convergence therefore gives
the mixture of these uniform sector laws as the finite-N long-time law.
The checker assembles an actual nonreversible four-site context count
sector and verifies its row/column balance and connectivity. The general
N^3 statement follows from the exact telescoping identity and the
positive floor, not from that small control.

Under a uniform count sector, sampling finitely many distinct sites is
sampling without replacement. Its falling-factorial probabilities converge
to iid uniform occupied labels when the empirical counts converge to 1/14.
Hence the ordered long-time-then-volume local limit is the full-occupancy
fourteen-label product. Full occupancy removes the independent total
density field; the one-site fourteen-feature covariance has rank thirteen.

The nonzero-mode covariance needs more than that local limit, but it has
an exact finite-volume identity. If mu_f and C_f are the empirical one-site
mean/covariance in a sector, exchangeability and the fixed total give

    Cov(f_x,f_y)=-C_f/(V-1), x!=y.

For torus characters, sum_x exp(-ik.x)=0 at every nonzero mode, and
sum_x exp[-i(k-l).x]=V 1_(k=l). In the double covariance sum the
off-diagonal phase sum is the negative of the diagonal one. Therefore

    Cov(fhat(k),fhat(l)^*)=V/(V-1) C_f 1_(k=l)

for nonzero k,l. The conditional means vanish exactly. Averaging over
random counts adds no between-sector mean covariance at these modes.
Since C_f(p) is continuous and bounded on the simplex, convergence in
probability of final empirical p gives convergence of its expectation.

The checker enumerates two complete four-site count sectors (24 and 12
arrangements), every pair of their three nonzero Fourier modes, and all
14 feature covariances. It also checks a nontrivial mixture of the
sectors. At the zero mode the mixture has additional nonzero count-history
variance; applying the nonzero-mode formula there would be false.

For the uniform final occupied law, C_U=C_V=4I/7 and C_UV=0. Applying the
scaled curls thus proves (18) at fixed nonzero continuum K, without
a Gaussian limit or a count-fluctuation central limit theorem. No
mixing-rate bound, simultaneous N/t limit, native finite-time fluctuation
law or initially empty Euler theorem is claimed. The assumptions
beta>0, |j|<1 and a fixed positive conservative floor are material.
The finite-time interior theorem covers the stated initial 0<rho0<1;
its constants may deteriorate with T, which the squeeze does not forbid.

## 8. Independent execution and unresolved boundaries

The independently written checker completed twelve exact symbolic,
finite-state or finite-combinatorial groups in one execution; the full
stdout/stderr log is retained. No failed execution was discarded and no
author checker was imported or run. These controls are selective
normalization/counterexample tests. The entropy limit and the ordered
late-state passage rest on the reconstructed arguments above.

I found no unresolved mathematical defect in the two notes at the bound
identities. The following remain unproved and are appropriately outside
their claims: native finite-time Gaussian fluctuations/centering,
uniform large-time/volume mixing control, a late-state Gaussian limit
for random global counts, empty-start native hydrodynamics by the
interior theorem, a singular Coulomb/quantum-vacuum spectral state,
field-readout selection, and physical quantum or electromagnetic
identification. A positive result about this supplied readout does not
close those separate obligations.

The initial reconstruction is preserved unchanged as INITIAL_RECONSTRUCTION.md
(SHA-256 ae102c6e5cdaf108c435cce0eecf14972a1467679a6d2dc16127a39de3e4be20).
PRE_COMPARISON_SEAL.json (SHA-256
6aa16724081ff1d271883722e2ca0506477c0a8e725eaae84d75c3e324804a22)
binds it, the checker, complete raw output and thirteen source identities
before any associated new author-checker/result access. All its bound
artifacts and dependencies were reauthenticated after that comparison.


## 9. Complete author-source comparison after the initial seal

All three author checkers, all three result JSON files and all three raw
execution logs were read completely. The comparison also inspected the
preserved initial local-curl checker failure and its complete source delta.
SOURCE_COMPARISON.json gives full paths, sizes and hashes for all eleven
files. Its source/result/log authentication is reproducible with
compare_sources.py, whose complete output is SOURCE_COMPARISON.log.
Neither comparison script executes an author checker or changes its output.

The compared checker identities are:

| Source | SHA-256 |
|---|---|
| loop_birth_locality_check.py | e501e4c931a8ce9df577d3ba70a2f7706df154e5763c2b0c1021f78724e499b4 |
| local_curl_native_formation_check.py | 6e84604fbf5c0366dc0b6eac063bb5539fcbb2e9d600628150111936b91829ed |
| late_state_canonical_check.py | 5a970b6be91b112ae2a147c253062d7cb519d56c257c31a47b25489553580cdb |

The result JSON files bind those actual checker hashes. Their named checks
agree with the complete static call inventory and with every raw PASS line
and final total. The recorded totals are respectively 5, 13 and 7; these
are evidence-inventory counts, not measures of proof completeness.

The loop checker independently enumerates all templates through the origin
and agrees with the reconstructed conditional probabilities. Its additional
total-variation difference is exactly 1/15, also checked directly from the
independent odds. Its scope explicitly excludes a general impossibility
theorem.

The local-curl checker retains every species in the fourteen-by-fourteen
reaction and current matrix. Its two A quadrupoles use a different
invertible basis from the independent checker, with the same zero block.
Its vector normalization, signs, six reaction rates, marked adjacent
covariance and 48 polar/axial curl transformations agree. Its finite
configuration test uses an integer-valued fixed-seed sample and all fourteen
birth labels; the general identity is established by its symbolic curl
matrix and by the proof, not by that one sample. It does not numerically
certify the Euler replacement or assert a native fluctuation theorem.

The late-state checker enumerates all configurations in small count
sectors, all sixteen ordered pairs of four-cycle Fourier modes, repeated
label sectors and a random count mixture. It correctly gives zero
conditional covariance at the global mode but nonzero between-sector
mixture variance there. Its fourteen-label covariance check sums the U/V
features over all occupied labels; it is not a full fourteen-field
fluctuation theorem. The independent checker additionally tests the full
fourteen-field covariance identity and the rank-thirteen full-occupancy
constraint. Both implementations obtain the same 4/7 U/V covariance and
scaled-curl tensor. The deterministic count-completion and harmonic
waiting-time controls agree with the separate mathematical arguments;
the source explicitly says they do not establish entropy replacement or
an infinite-volume mixing rate.

The preserved first local-curl execution passed its first twelve groups,
then stopped at a structural SymPy equality for equivalent probabilities.
The complete correction changes only that equality to simplification of
its algebraic difference. Applying the one-line replacement to the
preserved source reproduces the final checker byte for byte. The formulas,
parameters, model and scientific targets are unchanged. Its failed source
and log remain in the author's existing development folder; their hashes
are bound in SOURCE_COMPARISON.json rather than silently ignored.

The new notes stayed unchanged through this final comparison. The inherited
corrected acoustic, transverse and native-formation publication notes also
match the identities of the earlier reviews. There is no requested source
correction from this review. The pending-review phrase in the working
note is simply metadata to update after receiving this report; it is not
a mathematical defect or an authorization to alter any source here.

## 10. Reproduction, seal and scientific scope

From this independent directory:

    OPENBLAS_NUM_THREADS=1 python3 independent_check.py
    python3 compare_sources.py

Both independent executions completed without a failed assertion. Their
full raw logs are retained; no attempt or failure was discarded. The first
script's checks were executed before primary-checker access. The second
only authenticates the subsequently inspected evidence and checks the
additional exact TV value and preserved structural-equality repair.

FINAL_SEAL.json binds this complete report, the initial seal and all review
artifacts, the unchanged mathematical dependencies, all final author source
and evidence hashes, and the already verified instruction identities. The
review is bounded mathematical scrutiny of these supplied constructions,
not a formal retained-status audit, a proof of physical electromagnetism,
or a claim that the named unproved extensions have been closed. No editable
prompt, production source, publication file, Git state, PR or audit record
was changed. No agent was spawned and no outside communication was sent.
