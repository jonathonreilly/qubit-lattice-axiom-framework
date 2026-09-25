# Blind PRE: low common-Hamiltonian energy and original formation stationarity

25 September 2026. Bounded independent reconstruction in the inherited
model/effort, before access to the ground-formation-incompatibility author
packet. This is conditional mathematics of the supplied finite rotor model,
not an audit verdict, a physical-vacuum selection, or a microscopic
finite-spin energy convergence theorem.

The new result is an operator inequality for the original formation
intensity. It has an additive constant; a stronger inequality without that
constant is false. Combining it with the explicitly permitted,
**provisional** half-occupancy variational estimate gives a positive
formation-rate lower bound for globally near-ground states at fixed finite
volume and sufficiently small coupling. Every normal stationary state has
zero formation intensity, and so cannot have that low energy. Proximity to
an arbitrary sector's own infimum alone does not have this implication.

## 1. Exact premises and provenance

The graph is the nearest-neighbour even cubic torus of side \(L\ge6\).
Write \(n=|A|=|B|=L^3/2\), and orient all edges from \(A\) to \(B\).
The full effective space \(P\) has \(q_a=\pm1\) at every \(A\), and
\(q_b\in\{0,\pm1\}\) at every \(B\). Keep the full integer electric basis
and the physical constraint
\[
 \operatorname{div}E=q-\mathbf1_A.
\]
Matter is the supplied unsigned tensor hard-core algebra. An outward hop
from \(a\) to a vacant \(b\) moves charge \(q_a\), empties \(a\), and shifts
\(E_{ab}\) by \(-q_a\). The reverse returns the actual charge at \(b\);
that charge can be an old record, not just a charge that has recently left
an \(A\) site. The outward sum is \(F_a\).

The retained magnetic and electric operators are
\[
 Q=\sum_{\{a,c\}:\,N(a)\cap N(c)\ne\varnothing}
                S_{ac}^*S_{ac},\qquad S_{ac}=F_cF_aP,
 \qquad H_4=-2Q,
\]
\[
 D(q,E)=\sum_{a\to b:\,q_b=0}E_{ab}(E_{ab}-q_a)\ge0,
 \qquad h=KD-2\delta Q,\qquad K,\delta,\kappa>0.             \tag{1}
\]
The inequality for \(D\) holds term by term on integer fields. Its
empty-\(B\) gates are retained. It can have unconfined electric directions.

For every oriented birth edge \((a,b)\) and sign \(\sigma=\pm1\),
\(j_{ab,\sigma}\) acts when both endpoints are vacant, creates
\((q_a,q_b)=(\sigma,-\sigma)\), and shifts \(E_{ab}\) by \(+\sigma\).
The original resolved channel is
\[
 L_{ab,\sigma}=\sqrt\kappa\,Pj_{ab,\sigma}F_aP.              \tag{2}
\]
The specified unnormalized coherent instrument instead has one channel
\[
 L_{ab,\mathrm{coh}}
   =\sqrt\kappa\,P(j_{ab,+}+j_{ab,-})F_aP                  \tag{3}
\]
per edge. There is no coherent combination of different edges here. No
factor \(1/\sqrt2\) is inserted. Define the complete intensity
\(\Gamma=\sum_\mu L_\mu^*L_\mu\), summing all marks and all output sectors.

The three frozen main notes in SOURCE_PINS.json supply (1), (2), the
common semigroup, and finite-graph number balance. They are exact bytes at
main 60c5f194d940a7bbaf1cdd545296e31d74a02f1a, with SHA256 values

- local pair form: 7c5bc10d0ca1127c2a1ef6f5cf9269caf6e8f023a09a061c2da0d8e033e35a7a;
- common limit: c63db3296e5705c57693c2deb109e506f336fae4848d3ab0926d13a98929802b;
- formation balance: 2ae8d264eaff3ab47ecf4ec41fa21178ff444546bcc2e36d885d092732e30516.

The provisional filling note is frozen at
aef82e905d9270ae543501dd7548687fae93fda806cc8dd7b7c8861aafe8cadb;
its author seal is
0b72c3cd4dd5404a53de9808a5bf99fab48eab182defedba729b695ff4202066.
Its complete note and seal were read, but its controls, other seal members,
and independent PRE were not read or run. Only the half-occupancy trial
estimate is used below, explicitly as a conditional premise. Its vacancy
row bound is permitted background but is not needed in this proof.
No independent verification of its ground-filling theorem is claimed.
Prior one-pair PRE/POST exposure is historical context, not fresh
independence. No other active author/checker packet was accessed.

## 2. An exact intensity identity on one star

Let
\[
 v_a=\sum_{b\sim a}(1-n_b),\qquad M_a=PF_a^*F_aP.
\]
The observable \(v_a\) counts vacant \(B\) neighbours before the hop. On
the range of \(F_aP\), the \(A\) site is empty. Hence
\[
 \sum_{b\sim a,\sigma}j_{ab,\sigma}^*j_{ab,\sigma}
 =2v_a
\]
on that intermediate space: either sign can form at each empty neighbour,
with unit rotor-shift norm. An outward hop lowers \(v_a\) by one. Its
adjoint preserves all other \(A\) occupations, and \(M_a\) preserves the
number of occupied \(B\) neighbours. Consequently
\[
 [M_a,v_a]=0,\qquad
 \boxed{\ \Gamma_a=2\kappa(v_a-1)M_a\ },\qquad
 \Gamma=\sum_a\Gamma_a.                                  \tag{4}
\]
The \(v_a=0\) block has \(M_a=0\); thus no negative intensity arises from
the formal factor \(v_a-1\).

The ranges of \(j_{ab,+}\) and \(j_{ab,-}\) are orthogonal, because their
final charge at \(a\) differs. In particular \(j_{ab,+}^*j_{ab,-}=0\)
before any assumption about the incoming field or matter coherence.
Expanding (3) therefore gives exactly the same \(\Gamma_a\) as (2).
Their gain maps can differ, and the output is not dephased in this
argument. Equality of the full losses is sufficient for the conclusions
below. A normalized coherent channel would have a different intensity
and is outside these constants.

## 3. A uniform local operator bound, with phases and all colors

On the input block \(v_a=v\), each physical basis word has exactly \(v\)
legal outward paths. An intermediate output word has \(7-v\) occupied
\(B\) neighbours, and can have at most \(7-v\) reverse predecessors.
The returning charge is fixed by the selected occupied neighbour.
The electric shift is also fixed by that path. Cauchy–Schwarz, followed
by summing the output words, gives
\[
 \|F_a\psi\|^2\le v(7-v)\|\psi\|^2.                        \tag{5}
\]
Equivalently, this is the rectangular Schur bound from column absolute
sums \(v\) and row absolute sums at most \(7-v\). It works on the full
electric basis and hence on the invariant physical Gauss subspace.
It also works after a cycle Fourier transform: phases cannot increase
these absolute sums. Neither setting phases to zero nor an entrywise
ordering of Hermitian matrices is used to infer operator order.

The values for \(v=0,\ldots,6\) are
\[
        v(7-v)=0,6,10,12,12,10,6.
\]
Different \(v\) input blocks have orthogonal output vacancy-number blocks,
so \(\|F_a\|^2\le12\) on the central-occupied space, including when another
\(A\) site is vacant.

Combining (4) and (5) gives the useful affine estimate
\[
 \boxed{\ M_a\le6I+\frac{\Gamma_a}{5\kappa}\ }.             \tag{6}
\]
For completeness, the difference on block \(v\) is
\[
 M_a-\frac{\Gamma_a}{5\kappa}=\frac{7-2v}{5}M_a.
\]
For \(v=1,2,3\), (5) bounds this above by \(6,6,12/5\),
respectively. The \(v=0\) block is zero, and for \(v\ge4\) the coefficient
is nonpositive, so positivity of \(M_a\) bounds it above by zero.
This last step does not multiply an upper spectral bound by a negative
number. It establishes actual operator order on each commuting block.
The same argument gives the optional check
\(0\le\Gamma_a\le80\kappa I\), and hence \(\Gamma\le80\kappa nI\).

## 4. Energy–intensity inequality

Outward hops from distinct \(A\) sites commute; if they attempt the same
vacant destination, both orders vanish by exclusion. Thus
\[
 \|S_{ac}\psi\|^2
 \le12\|F_a\psi\|^2,\qquad
 \|S_{ac}\psi\|^2
 \le12\|F_c\psi\|^2.
\]
Averaging these two scalar inequalities proves
\[
 S_{ac}^*S_{ac}\le6(M_a+M_c).
\]
For \(L\ge6\), each \(A\) has exactly 18 distinct overlapping \(A\)
partners: the six displacements \(\pm2e_i\) and the twelve
\(\pm e_i\pm e_j\), \(i<j\). They have no wrap identifications at these
sizes. Summing the pair inequality and then (6) yields
\[
 \boxed{\quad Q\le108\sum_a M_a
       \le648nI+\frac{108}{5\kappa}\Gamma.\quad}            \tag{7}
\]
No commutation of different star or pair operators is assumed.

Since \(D\ge0\), (1) and (7) imply the quadratic-form inequality
\[
 \boxed{\quad
 h\ge E_{\rm d}I-\frac{216\delta}{5\kappa}\Gamma,\qquad
 E_{\rm d}:=-1296\delta n.\quad}                           \tag{8}
\]
For any normalized state \(\rho\) of finite energy, \(E=\operatorname{Tr}h\rho\),
\[
 \boxed{\quad
 \operatorname{Tr}\Gamma\rho
 \ge\frac{5\kappa}{216\delta}(E_{\rm d}-E)_+.\quad}        \tag{9}
\]
Here \(x_+=\max(x,0)\). This is a one-sided low-energy constraint, not a
formula identifying intensity from energy.

There is no domain manipulation of \(Dh\), \(DL_\mu\), or a commutator with
the unbounded energy. The bounded \(Q,\Gamma,M_a\) inequalities hold
everywhere. \(D\) is its nonnegative diagonal multiplication operator,
\(h\) is self-adjoint on \(\mathcal D(D)\), and (8) holds on
\(\mathcal D(D^{1/2})\). For densities, finite energy means
\(\operatorname{Tr}D\rho<\infty\) when \(K>0\), equivalently finite mean of
the semibounded \(h\). Infinite positive mean energy does not constitute
a low-energy counterexample. Degeneracy of the electric quadratic form
does not affect the argument.

If \(e_m=\inf\sigma(h|_{N=n+m})\), then for a state in that sector with
energy excess \(\varepsilon=E-e_m\),
\[
 \operatorname{Tr}\Gamma\rho
 \ge\frac{5\kappa}{216\delta}
          (E_{\rm d}-e_m-\varepsilon)_+.                 \tag{10}
\]
The identical formula holds with the full infimum \(e_*=\inf\sigma(h)\)
and global energy excess, whether or not the state has a definite
number. The formula becomes informative when the relevant infimum is
below \(E_{\rm d}\). It does not assert this for every sector or every
coupling. No sector-dependent shift of the Hamiltonian's zero is made.

## 5. Stationarity and darkness are different statements

Let \(N=nI+\sum_b n_b\), a bounded observable. Every Hamiltonian term
preserves \(N\), strongly including the electric diagonal, and each
original channel raises \(N\) by two. The mild common evolution gives
\[
 \operatorname{Tr}N\rho_t-\operatorname{Tr}N\rho_0
       =2\int_0^t\operatorname{Tr}\Gamma\rho_s\,ds.         \tag{11}
\]
This uses bounded number and bounded jumps and needs no electric moment.
It is also directly obtained by the unitary interaction-picture Dyson
equation, since the Hamiltonian part leaves \(N\) invariant.

Every normal stationary density therefore has
\(\operatorname{Tr}\Gamma\rho=0\). Positivity implies
\(L_\mu\rho^{1/2}=0\) for each channel, so the dissipator vanishes on
\(\rho\). The mild equation then shows that a stationary density must
also be invariant under the \(h\)-unitary group. Conversely a dark
density invariant under that group is stationary. Merely vanishing
instantaneous intensity is insufficient.

In particular every stationary normal density with finite energy obeys
\[
                       E\ge E_{\rm d}.                  \tag{12}
\]
This is an instantaneous energy/stationarity obstruction in the
specified common law. It supplies no convergence to a stationary state,
pointwise late-time decay rate, or infinite-volume assertion.

## 6. Conditional global small-coupling consequence

Now specialize to the supplied parameterization
\[
 K=\frac{g^2}{2\tau},\qquad
 \delta=\frac1{4\tau g^2},\qquad \tau>0
\]
with fixed \(L,\tau,\kappa\) and \(g\downarrow0\). The physical sectors
have even \(m\in\{0,2,\ldots,n\}\), since total charge is \(n\) and the
number of minus charges is \(m/2\). The finite set of sector infima has
a minimum, without requiring a ground eigenvector.

**Explicit provisional import.** The permitted filling note supplies a
Gauss-compatible smooth trial, including all cycle and harmonic angles,
in the physical sector \(m=n/2\), with
\[
 e_*(g)\le e_{n/2}(g)
       \le-\frac{R}{2\tau g^2}+C_{L,\tau},                 \tag{13}
\]
\[
 \frac Rn=\frac{1905}{2}+\frac{378}{n-1}
                  +\frac{414(2n-3)}{(n-1)(n-3)}
           >\frac{1905}{2}.                              \tag{14}
\]
Take \(C_{L,\tau}\ge0\) finite and independent of sufficiently small \(g\).
The trial uses a full color vector and a width-\(g\) smooth angle bump.
Its existence and \(O_L(1)\) energy remainder are imported provisionally
here; they are not established by this packet's star/fixture controls.
The filling note's independently checked status remains open to its
separate checker. An initial integer-field state's Haar harmonic fiber
is not being replaced in a claimed dynamical trajectory: (13) is only a
variational upper bound for the full spectral infimum.

In this parameterization
\[
 E_{\rm d}(g)=-\frac{324n}{\tau g^2}.
\]
Since \(R>952.5n>648n\), (13) eventually places the global infimum below
this dark-state floor. Equations (12)–(14) imply that every stationary
normal density with finite energy has the global excess
\[
 \boxed{\quad
 E-e_*(g)\ge\frac{R-648n}{2\tau g^2}-C_{L,\tau}
          >\frac{609n}{4\tau g^2}-C_{L,\tau}.\quad}         \tag{15}
\]
For a state satisfying \(E\le e_*(g)+\varepsilon\), (9) instead gives
\[
 \boxed{\quad
 \operatorname{Tr}\Gamma\rho
 \ge\frac{5\kappa}{108}
       \left[R-648n-2\tau g^2(C_{L,\tau}+\varepsilon)\right]_+.
 \quad}                                                  \tag{16}
\]
For globally near-ground families with \(\tau g^2\varepsilon\to0\),
\[
 \liminf_{g\downarrow0}\frac{\operatorname{Tr}\Gamma\rho_g}{\kappa n}
 \ge\frac5{108}\left(\frac Rn-648\right)
 >\frac{1015}{72}.                                       \tag{17}
\]
The bound is sufficient, not optimized. A fixed sufficiently small \(g\)
also gives a positive lower bound for every sufficiently accurate
minimizing sequence. If a normalizable ground state exists, any density
supported in its possibly degenerate ground space has energy \(e_*\),
and therefore positive intensity; it is not stationary. If no ground
eigenvector exists, the statement is about minimizing sequences and the
energy gap of normal stationary states, not a nonexistent vector.
There is no uniform-in-\(L\) small-\(g\) threshold or thermodynamic claim.

## 7. Exact obstructions to stronger interpretations

**A constant is needed in (7).** On \(L=6\), leave only the two \(B\)
vacancies \((1,0,0)\) and \((3,2,0)\). Their torus distance is four,
so no \(A\) has both as neighbours. All original jumps therefore kill
every basis word of this vacancy pattern. Put all \(A\) charges at
plus, and put half the 106 occupied \(B\) charges at each sign, in the
coordinate-lexicographic convention recorded by the control. Their
total charge is \(108=n\). An integer spanning-tree flow solves Gauss.

The exact own primitive control retains every intermediate and returning
charge, and every electric shift. For its normalized finite-electric word
\(\psi\) it gives
\[
 \Gamma\psi=0,\qquad
 \langle D\rangle_\psi=2,\qquad
 \langle Q\rangle_\psi=4,\qquad
 \langle h\rangle_\psi=2K-8\delta.                         \tag{18}
\]
Thus \(Q\le c\Gamma\) fails for every finite \(c\), and even negative
Hamiltonian mean does not by itself imply positive instantaneous rate.
This is a physical, finite-electric counterexample, not just a
zero-angle nonnormalizable color vector.

It is not a stationary counterexample to (12). The same full primitive
calculation gives
\[
 \sum_j\|B_jQ\psi\|^2=1240,\qquad
 \sum_\mu\|L_\mu h\psi\|^2=4960\kappa\delta^2>0.            \tag{19}
\]
Here \(B_j=L_j/\sqrt\kappa\). There are 115 electric/matter words in
\(Q\psi\), and all 328 marked output words are preserved. The electric
term on the incoming basis word is scalar and drops out after \(L_\mu\).
The finite-basis input belongs to \(\mathcal D(h)\), so the strong
no-event derivative gives
\[
 \Pr_\psi(\text{first birth by }t)
   =\frac{4960}{3}\kappa\delta^2t^3+o(t^3).
                                                               \tag{20}
\]
This also follows from the permitted parent balance companion argument.
Both instrument conventions have the same sum in (19), by their
identical full loss. It does not assert that their post-event states agree.

**Sector-ground proximity alone is insufficient.** In the saturated
sector \(m=n\), all \(B\) sites are occupied. The original empty-\(B\)
gates give \(D=0\), while every \(F_a,S_{ac},L_\mu\) vanishes. Thus
\(h=0\), \(e_n=0\), and every normal physical density in that sector is
stationary, including states exactly at their sector infimum. Global
near-ground and sector-near-ground must therefore be separated.
The parent also constructs unsaturated stationary words with vacancies
farther apart than four; this proof does not remove them.

**No full energy reconstruction from intensity.** In the all-\(A\)-plus,
\(B\)-empty sector, (4) gives
\(\Gamma=60\kappa nI\), independent of the divergence-free electric
field. Divergence-free integer circulations of arbitrarily large
amplitude make the electric mean arbitrarily large while leaving this
rate fixed. There is no upper energy control by intensity alone.

## 8. Own controls, complete logs, and boundaries

No parent or author program was imported or executed. Two independently
written primitive controls were used.

- star_primitive_control.py enumerates all 1458 central-occupied
  six-leaf charge words and 2916 outward paths. It preserves exact
  six-edge Laurent shifts in the complete 11050-entry \(M_a\) and
  8746-entry \(\Gamma_a/\kappa\) tables. It compares the resolved
  channel Grams with coherent sums formed before the Gram, verifies
  (4), checks the vacancy blocks and the constants in (5)–(6), and
  keeps all table entries in STAR_LAURENT_ENTRIES.json.
- physical_dark_fixture_control.py builds its own cubic graph, integer
  Gauss flow, outward and reverse hops, births, and complete \(Q\psi\).
  It checks all 1507 distinct generated words for Gauss, verifies 18
  pair partners per \(A\) and the 324/648 pair counts, and records the
  full counterexample and reactivation outputs in DARK_FIXTURE_PATHS.json.

verify_evidence.py separately reads every stored Laurent row and every
stored fixture row, checks exact local/global Gauss changes and
Hermitian adjoints, validates all norms and integer summaries, and
rechecks source identities and executable/stdout/stderr bindings.
EVIDENCE_VERIFICATION.json records that scope. These exact bounded
calculations corroborate the analytic argument; they do not compute a
global many-body spectrum, prove the imported filling estimate, or
simulate a late-time evolution.

All four executions (source freeze, two controls, and read-only verifier)
completed with exit code zero and empty stderr. Full receipts and stdout
are retained. No failed computational run was deleted; none occurred.
The rejected unshifted inequality is retained above as an explicit exact
counterexample, not hidden as an unsuccessful route. Current procedures
are frozen with the sources. This report and its evidence are sealed
before scientific disclosure to the parent.

The supported content is (4)–(12) and the exact fixture for the supplied
finite common law, and (15)–(17) conditionally on the labelled trial
premise. The remaining boundaries include physical selection/preparation,
which sectors actual histories reach, stationarity versus approach to
stationarity, microscopic finite-spin energy limits, thermodynamic
limits, and empirical identification. A selected nonequilibrium
preparation, an energy-constrained sector, or a supplied external drive
is not excluded by this calculation. No total heat, absorption, energy
flux, or observed-vacuum conclusion follows from the formation intensity.
