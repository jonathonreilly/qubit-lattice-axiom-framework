# Output-energy selection in the supplied ring and cube targets

Independent reconstruction before new-author access, September 23, 2026.
The new energy-selected author packet remains unopened. The permitted prior
prepared theorem, ring spectrum, and already checked cube sources are reused
at their recorded identities; none is promoted to formal audit status.

**Result.** Every moving energy interval of width o(eta) has vanishing weight
in each fixed input belonging to the continuous spectral subspace of the
rotor H2. The conclusion is uniform in the center and on norm-compact input
families, but not on the whole unit ball. For the eight-site ring,
`g(H6,S+4 eta)` converges strongly to `P0 g(h_flat) P0` for every g in C0(R).
Centered sharp windows with half-width R_S tending to infinity and
R_S/eta tending to zero converge strongly to P0.

If those projections are explicitly inserted into the *first* jump and its
loss is changed consistently, the full target from a fixed normalizable
original N4 input has a trace-norm limit. On the ring the limiting first and
second rates are 8 kappa and 4 kappa. On the cube, any such moving sublinear
window suppresses first formation; the limiting density stays in N4 and
evolves unitarily. These statements concern a changed instrument. They are
not a native selection mechanism, a derived reservoir, a microscopic filter
theorem, or a conclusion for increasing graph size.

## 1. Contract, spaces and reused premises

Work on the fixed alternating eight-site ring or the supplied eight-vertex
cube, with hard-core charges 0,+1,-1, total charge four, the stated Gauss
background, and the full physical spin spaces. P requires all A sites
occupied. The target has N=4,6,8 number sectors, with N8 absorbing. The
Hamiltonians use the supplied two/four-hop rules and

```
C_S=S(S+1),  eta=K C_S,  K,delta,kappa>0 fixed,
H6,S=eta H2,S+delta H4,S.
```

The common rotor N6 spaces are l2(Z) tensor C36 on the ring and l2(Z5)
tensor C36 on the cube. Spin states are embedded by their physical charge
and integer fields; each physical box contains every state with all links
in [-S,S]. Use the whole-box zero extensions for bounded operators. A fixed
vector is replaced by any physical sequence converging in norm, and an
initial density by any physical sequence converging in trace norm.

The prior checked inputs are:

* The normalized link shifts and finite path counts give uniform bounds on
  H2,S, H4,S, first and second B_mu,S, and their losses. These operators and
  their adjoints converge strongly to the rotor versions on finite-field
  vectors, hence strongly on the whole common space by uniform boundedness.
* The ring's only physical N6 rotor point eigenvalue is -4, with projection
  P0 and a finite-range orthonormal compact frame. Write Q0=I-P0. Its other
  branches are dispersive; isolated special-angle eigenvectors are not
  normalizable point eigenvectors.
* The cube's physical N6 rotor H2 has empty point spectrum. Its prior
  spectral FINAL/comparison dependency has already been checked; no new
  cube spectral proof is made here.
* The ring prepared theorem controls the original no-event evolution on P0
  after removal of its common fast phase. The limiting generator is
  `-i h_flat-2 kappa`, where

  `h_flat=K P0 D2 P0+delta P0 H4 P0`.

  It is self-adjoint on the flat-space domain D(f²). In the compact frame
  its electric diagonal is quadratic with leading term 4K f² and its H4
  term is bounded and of finite circulation range. The original next loss
  satisfies `Gamma6 P0=4 kappa P0`. The finite-spin theorem includes the
  nonzero D2 leakage, embedded dispersive crossings and the physical
  boundary; it does not assume exact flat invariance at finite S.
* On the original N4 sector the checked cube identity is
  `eta(H2,4,S+12I)=K sum_e E_e²`, and its rotor H4 is
  `60I-2 sum_faces(W_p+W_p*)`. Its original first loss is uniformly at most
  48 kappa. On the ring the corresponding identities are derived below.

The deliverable is a bounded theorem/control packet under these supplied
premises. It does not assert formal retained status. The proof obligations
are: static moving-window concentration, the purely Hamiltonian extension
of the prepared theorem, spectral projection convergence, and a changed-loss
semigroup/source composition. None is replaced by a numerical fit.

## 2. A statewise moving-window theorem

Put `A_S=H6,S/eta=H2,S+(delta/eta)H4,S`. There is a constant M independent
of S with `||A_S||<=M`, and A_S converges strongly to the bounded
self-adjoint rotor H2. Polynomial approximation on a common compact
spectral interval shows that `f(A_S)->f(H2)` strongly for every continuous
f on that interval. Consequently the spectral measures of a fixed vector
psi converge weakly to its H2 spectral measure mu_psi.

Let r_S>=0 tend to zero. If mu_psi has no atoms, then

```
sup_(c in R) || 1_[c-r_S,c+r_S](A_S) psi || ->0.       (1)
```

Proof: a contrary sequence has centers c_S and interval weights bounded
below by some a>0. Centers outside a fixed enlargement of [-M,M] contribute
zero, so extract c_S tending to c. For any fixed d>0 the moving intervals
eventually lie inside [c-d,c+d]. A continuous majorant of that fixed interval
and weak convergence bound the limsup by mu_psi([c-2d,c+2d]). Let d decrease
to zero. The result is mu_psi({c})=0, a contradiction. Equivalently, this is
uniform absence of concentration for a weakly converging sequence whose
limit measure is nonatomic. No absolute-continuity or density bound is used.

Returning to original energy units, for arbitrary centers a_S and half-widths
w_S with w_S/eta tending to zero,

```
||1_[a_S-w_S,a_S+w_S](H6,S) psi|| ->0                 (2)
```

for every psi in the continuous spectral subspace of H2. The supremum may
be taken over all centers at every S. Thus no assumption about convergence
of a_S/eta is required. The same proof, localized to c=-4, only needs absence
of an atom at -4 when the centers are fixed to -4 eta.

For a norm-compact family C of such inputs, choose a finite epsilon net.
Each spectral projection has norm at most one. Apply (1) to the finitely
many net points, then let epsilon decrease to zero. This proves uniformity
on C and allows uniformly converging families of physical approximants.
The density version follows from finite-rank approximation: for a fixed
positive trace-class rho supported in the continuous spectral subspace,
`tr(rho 1_I(H6,S))->0`, uniformly in the moving center. This also holds
uniformly on trace-norm-compact families of such densities. For arbitrary
fixed trace-class operators supported in that continuous subspace, strong
convergence of uniformly bounded projections gives the corresponding
compressed trace-norm convergence.

On the cube (2) holds for every fixed N6 input. On the ring it holds on Q0.
The zero extension outside the physical spin box does not introduce an
exception: the norm of the exterior part of each fixed input tends to zero,
uniformly on compact families.

There is deliberately no claim of operator-norm convergence or uniformity
over arbitrary spin-dependent inputs. For example, on L2([0,1]) let A_N be
multiplication by the midpoint of the cell of width 1/N containing x. Then
`||A_N-x||<=1/(2N)` and the limit has no point spectrum. A window with
half-width 1/(3N) around a selected cell midpoint has constant-input
probability 1/N but probability one in that cell's normalized indicator.
Its projection norm is one. Likewise o(eta) cannot be replaced by O(eta):
for H_eta=eta x and psi=1, the interval centered at eta/2 with half-width
eta/4 has probability one half. These are explicit counterexamples to
stronger statements, not claims about actual cube outputs.

## 3. Removing the prepared theorem's bounded loss

Set `G_S=H6,S+4 eta I`, a self-adjoint operator (bounded for each finite S),
and let

```
V_S(t)=exp[t(-i G_S-Gamma6,S/2)],
V(t)=exp(-2 kappa t) exp(-i t h_flat) on P0 H6.
```

The checked prepared theorem gives V_S(t)psi tending to V(t)psi for every
psi in P0, uniformly for t in [0,T]. Its extension to arbitrary normalizable
psi uses contraction and density, so it has no uniform moment requirement.
The domain D(f²) concerns the self-adjoint generator, not the availability
of its unitary on an arbitrary normalizable vector.

It would be unjustified to identify this nonunitary semigroup directly with
Hamiltonian spectral calculus. The needed extension follows from a separate
bounded perturbation argument. Restore the bounded loss by the Dyson series
for `-iG_S=(-iG_S-Gamma6,S/2)+Gamma6,S/2`. Every term consists of products
of V_S at nonnegative time increments and Gamma6,S/2. On a flat limiting
vector, Gamma6,S converges strongly to the scalar 4 kappa, and V preserves
P0. Induction therefore gives the limit of each fixed Dyson term. The norms
are bounded by `(M T/2)^n/n!`, independently of S. Summing the terms gives

```
exp(-it G_S) psi -> exp(-it h_flat) psi,  psi in P0,  (3)
```

uniformly on [0,T]. Convergence is uniform over the compact vector orbits
used at each induction step by finite nets. No invariance of P0 under the
finite-spin Hamiltonian or loss has been inserted into this reasoning.

For t>=0, unitarity gives

```
||exp(+it G_S)psi-exp(+it h_flat)psi||
 = ||psi-exp(-it G_S)exp(+it h_flat)psi||.
```

The compact orbit of exp(+it h_flat)psi lies in P0. Equation (3) therefore
also holds uniformly on negative compact time intervals. This proves the
purely Hamiltonian statement needed for Fourier functional calculus. An
alternative is to repeat the prior cutoff-corrector proof with zero loss;
the Dyson route above avoids assuming a parameter extension of that theorem.

For g Schwartz, Fourier inversion and dominated convergence now give
`g(G_S)psi -> g(h_flat)psi` for psi in P0. Schwartz functions are dense in
C0(R) in uniform norm, and functional calculus is contractive in that norm.
Thus the same result holds for every g in C0(R).

For psi in Q0, first choose a large fixed residual-energy cutoff L so that
g is uniformly small outside [-L,L]. The norm on that interval vanishes by
(2), since its original center is -4 eta and width 2L=o(eta). Then let L
increase. Combining both components proves the full-space strong limit

```
g(H6,S+4 eta I) -> P0 g(h_flat) P0,  g in C0(R).       (4)
```

The right side acts as zero on Q0. It is not functional calculus of a
self-adjoint operator on the entire original space with g=1 appended: the
continuous component escapes every bounded residual-energy set. In
particular (4) does not imply full-space unitary convergence.

## 4. Expanding sharp windows select the physical flat space

On the ring define the physical spectral projection

```
Pi_S=1_[-R_S,R_S](H6,S+4 eta I),
R_S -> infinity,  R_S/eta ->0.                        (5)
```

For psi in P0, equation (4) implies tightness of the shifted spectral
measures: choose a continuous compactly supported bump b with 0<=b<=1
and `||b(h_flat)psi||` arbitrarily close to `||psi||`. Eventually Pi_S
contains its support, and

```
||(I-Pi_S)psi||² <= ||psi||²-||b(G_S)psi||².
```

Equation (4) makes the limsup arbitrarily small. This holds for any speed
of R_S tending to infinity; no electric moment or convergence-rate bound
is needed. On Q0, (2) with w_S=R_S gives Pi_S psi tending to zero. Hence

```
Pi_S -> P0 strongly,                                 (6)
```

uniformly on every norm-compact input family and for norm-convergent physical
approximants. This is an output-Hamiltonian energy measurement statement,
not a claim that P0 commutes with the finite-spin dynamics.

Both width conditions matter. A fixed residual-energy window need not
contain all the flat limiting energy distribution; at endpoints meeting
point spectrum of h_flat, sharp projection limits require additional
analysis. Arbitrary centers cannot be substituted in the ring conclusion:
alternate centers -4 eta and 0 with half-width sqrt(eta). A fixed flat input
is selected along the first subsequence and rejected along the second,
so the projections have no statewise limit on that input. The earlier
arbitrary-center assertion is precisely for continuous-spectrum inputs.

## 5. The changed first instrument and its loss

Now stipulate a different target instrument. Only its first N4-to-N6 maps
are replaced by

```
L_mu,S=sqrt(kappa) Pi_S B4,mu,S,
Gamma4,S^sel=kappa sum_mu B4,mu,S* Pi_S B4,mu,S.        (7)
```

Use the same resolved channels as the parent, or for a coherent edge use
`B4,e,+,S+B4,e,-,S` before Pi_S. Keep the original N4 and N6 Hamiltonians,
the original N6-to-N8 jumps and their losses, and the absorbing N8 sector.
Equation (7), including its anticommutator loss, defines a trace-preserving
changed Lindblad target at each finite S. It does not append rejected
outcomes or renormalize an old trajectory. Keeping the old first loss while
discarding output amplitudes would be a different, trace-decreasing model.

Initialize all A plus and all B vacant with a fixed trace-one normalizable
physical field density rho0, and physical trace-norm-convergent spin
approximants. Zero field is included. Such evolution remains number-block
diagonal; common scalar fast phases cancel within each density block.
No theorem is asserted for initial number-sector coherences or an arbitrary
continuous-spectrum N6 preparation.

On the cube let Pi_S be any moving interval projection as in (2). Then
Pi_S tends strongly to zero. On the ring use (5); Pi_S tends strongly to P0.
The first B_mu,S and their adjoints converge strongly with uniform norms.
Therefore (7) converges strongly, with uniform bounds, to zero on the cube
and to

```
Gamma4^sel=kappa sum_mu B4,mu* P0 B4,mu                (8)
```

on the ring. The range of Pi_S B_mu,S is physical; the zero extension causes
no new output sectors. The bounds are at most the original losses, separately
for each stipulated instrument, because 0<=Pi_S<=I: 16 kappa on the ring
and 48 kappa on the cube. No equality of their filtered finite-S losses is
assumed.

For the ring, each resolved rotor first output has one old-hop/birth path.
Its occupied B pair is adjacent. In every fixed adjacent-pair block the
compact flat projection has diagonal block exactly I/2; its partner block
has a different B pair. Consequently, as operators on the whole original
N4 field space,

```
B4,e,sigma* P0 B4,e,sigma = I/2,
B4,e,+* P0 B4,e,- = 0.                               (9)
```

The second identity holds because the same-edge first outputs have the
same occupied B pair but distinct minus positions. Distinct input
circulations remain orthogonal within that fixed block. There are sixteen
resolved channels, or eight coherent edges. Thus (8) equals `8 kappa I`
for both. Their recycling densities generally differ; zero cross-Gram
does not imply a zero cross-output operator.

There is a crucial finite-S qualification. Opposite newborn matter patterns
are orthogonal *before* filtering. An output energy projection is nonlocal
in that basis, so `B_+* Pi_S B_-` need not vanish. The new controls establish
an exact rational counterexample for the smooth filter
`g(G)=(I+G²)^(-1)` at S=1,K=delta=1: the coherent-minus-resolved first-loss
matrix entry from f=0 to f=-1, without kappa, is

```
-71329283816438226197657 / 592355905079662832198438881,
```

which is nonzero. The normalized physical input
`(|f=-1>+|f=0>)/sqrt(2)` has this same nonzero expectation of the difference.
Since

```
g(x)^2 = integral_0^infinity [4r/(1+r²)^3] 1_(|x|<=r) dr,
```

this also proves that at least one centered sharp-window radius at that
spin has a nonzero coherent/resolved loss difference. Independently, the
complete floating S=2 control at K=.4,delta=.25,R=sqrt(eta) finds difference
norm about .381645. That radius is a numerical countercontrol; the rational
argument is the exact existence witness. There is no conflict with the
prior clarification that the *unfiltered* finite-spin losses are equal, or
with their shared strong limiting selected loss in (9).

## 6. Original first-sector field and limiting density on the ring

In N4 the sole matter word is q=1_A. The physical ring field is E_e=f on
every link. Only undoing the first hop returns a two-hop path to P. Four
oriented hops shift by +1 and four by -1, so exactly, including boundaries,

```
H2,4,S=-8I+8 f²/C_S,
eta(H2,4,S+8I)=8K f².                                (10)
```

The unit-rotor H4 is 24I. There are eight first hops and twenty unordered
disjoint outward-hop pairs, with two orderings each; thus M² diagonal 64
and Z*Z diagonal 80 give 64-40=24. The eight-site ring has no four-edge
cycle that would produce an off-diagonal circulation shift at this order.
The new exact local control verifies (10) over each full N4 spin interval
at S=1,2,4 and the rotor H4 identity.

Let `h4^ring=8K f²+24 delta I`. Extend the spin first-sector generators on
the whole field space using this common unbounded diagonal electric
operator, plus the uniformly bounded finite-spin H4 and selected-loss
terms. Physical spin boxes reduce these extensions. Bounded-perturbation
Duhamel/iteration gives strong semigroup convergence uniformly on compact
times, first on any vector and then on trace-class densities. Only strong
convergence of the bounded perturbations on compact vector orbits is
needed. Their limiting selected loss is 8 kappa, so

```
rho4(t)=exp(-8 kappa t) U4(t) rho0 U4(t)*,
U4(t)=exp(-it h4^ring).                               (11)
```

The limiting first source is the trace-norm continuous positive curve

```
F(t)=kappa sum_mu P0 B4,mu rho4(t) B4,mu* P0,
tr F(t)=8 kappa exp(-8 kappa t).                       (12)
```

The exact finite-S sources converge to it in trace norm uniformly on
compact time intervals. They need not be a fixed output times an exact
finite-S exponential: the filtered first loss can mix field states. Even
where finite-spin zero-field diagonal rates coincide across instruments,
their full loss operators can differ.

Let U6(t)=exp(-it h_flat) on P0, and let B6,nu be the original second rotor
jumps, with the chosen resolved or coherent interpretation used consistently.
The limiting full density is specified by the orthogonal number blocks

```
rho6(t)=integral_0^t exp[-4 kappa(t-s)]
                    U6(t-s) F(s) U6(t-s)* ds,
rho8(t)=kappa sum_nu integral_0^t
                    B6,nu rho6(s) B6,nu* ds,          (13)
rho(t)=rho4(t) direct_sum rho6(t) direct_sum rho8(t).
```

To justify full trace-norm convergence, replace the finite-S first source
by F in the exact triangular N6 source formula, incurring at most
`T sup_s ||F_S(s)-F(s)||_1`. The compact range of F consists of flat-supported
positive trace-class operators. The prepared no-event theorem, finite-rank
approximation and finite nets give uniform trace-norm convergence of its
propagation over this compact range and compact ages. Integrate. The second
jumps are uniformly bounded and converge strongly, so their recycling maps
converge on the now trace-norm-convergent N6 curve; integrate again to obtain
N8. No assumption that Pi_S reduces the no-event loss is needed.

Tracing (11)-(13), using (9) and the original flat loss 4 kappa, gives

```
p4(t)=exp(-8 kappa t),
p6(t)=2[exp(-4 kappa t)-exp(-8 kappa t)],
p8(t)=[1-exp(-4 kappa t)]².                           (14)
```

These limits hold uniformly on compact ordinary-time intervals for any
fixed initial field density in the stated class, including zero field.
Both stipulated resolutions have these same number probabilities, although
their density matrices in (12)-(13) need not agree. The first rate is half
the original unfiltered rate; it has been derived from the changed loss,
not imported from postselection of an already occurring old event.

## 7. Changed-instrument limit on the cube

Here (2) gives Pi_S tending strongly to zero for every moving sublinear
window center. The selected first loss tends strongly to zero, and the
same bounded-perturbation argument with the checked common electric
operator gives

```
rho4,S(t) -> U_cube(t) rho0 U_cube(t)* in trace norm,
h_cube=K sum_e E_e²-2 delta sum_faces(W_p+W_p*),
U_cube(t)=exp(-it h_cube).                            (15)
```

The scalar 60 delta is omitted because it cancels in densities. This
self-adjoint operator has domain D(sum E²); the magnetic term is bounded.
The result extends to every normalizable initial field density without
requiring any field moment. The selected first source tends to zero in
trace norm uniformly on compact times. Positivity and trace preservation
then imply the sum of the N6 and N8 traces tends to zero. Therefore the
*entire* density, not merely its fixed-window compression, converges in
trace norm to (15), and

```
p4(t)->1,  p6(t)->0,  p8(t)->0.                       (16)
```

This holds for either channel resolution. The original second instrument
can do nothing in the limiting density because the total probability of
reaching it vanishes. No limit for arbitrary unprepared N6 propagation is
assumed. In contrast to the previously checked unfiltered cube consequence,
there is no time-averaging argument in the static filter theorem: strong
spectral convergence and nonatomic measures suffice. Compact-time control
of the evolving first-source family is still needed for composition and
is supplied by the first-sector semigroup convergence.

## 8. Fixed smooth filters, limits of selection, and counterchecks

Equation (4) also permits a fixed bounded smooth filter g in C0(R) in place
of the expanding sharp window. On the ring its limiting first map is
`sqrt(kappa) g(h_flat) P0 B4,mu`, and its limiting loss is

```
kappa sum_mu B4,mu* P0 |g(h_flat)|² P0 B4,mu.
```

The same arguments give a full target density limit from the original N4
initial state, with this bounded loss in its first no-event generator and
the corresponding flat source in (13). In general it is field dependent
and resolution dependent. Formula (14) is not asserted for a fixed g. If
J(s) denotes that limiting first-source trace, then the valid count formulas
are `p6(t)=integral_0^t exp[-4 kappa(t-s)]J(s)ds` and
`p8=1-p4-p6`, with p4 from its changed first no-event semigroup. On the cube
a fixed C0 energy filter about any moving center tends strongly to zero
and again gives (15)-(16). This optional extension clarifies why C0
functional calculus alone does not justify treating every filter as P0.

The following potential overclaims were tested or excluded explicitly:

* Uniformity over the whole unit ball fails by the normalized shrinking-cell
  example. Arbitrary S-dependent eigenvectors can also concentrate in
  moving finite-spin eigenvalue windows. This does not defeat compact-family
  uniformity, which is exactly what the first-source proof uses.
* The flat H2 eigenvalue is embedded. No gap estimate or assumed finite-spin
  invariant flat sector is used; the checked prepared theorem supplies the
  difficult crossing control, and the new bounded-loss argument preserves
  its domain hypotheses.
* A sharp fixed-width residual window is not automatically the full flat
  preparation; an alternating center can destroy even a statewise flat
  limit. The specified expanding centered window is essential to (14).
* Original unfiltered coherent/resolved loss equality cannot be copied after
  a nonlocal energy filter. The exact rational and complete-spin controls
  give counterexamples. Equality in the limiting P0 first loss is proved
  separately by its compact-frame block structure.
* The selected instrument changes the law, not just a description of the
  original output. No microscopic approximation theorem for these new
  nonlocal jumps is provided by the old deterministic target estimate.
  There is no rejection record, reservoir construction, locality proof,
  native selection rule or volume-uniform statement here.

## 9. Evidence, failures, source independence and recovery

The new `filter_controls.py` imports only the two previously frozen
independent ring rule/frame helpers. It checks the projected first-channel
Grams on fields -2,...,2 (with the all-field translation argument given in
Section 5), and constructs complete physical N6 matrices at S=2,4,8,16.
The largest dimension is 1,128. The chosen new control parameters are
K=.4,delta=.25,R_S=sqrt(eta); they were not supplied as author targets.

At S=2,4,8,16 the maximum first-source projection errors are approximately
.831,.668,.145,.101. The tested flat-vector smooth-functional-calculus
errors for g(x)=1/(1+x²) are .00740,.00766,.00298,.000904. These values are
not monotonic at the smallest spins and are preserved as measured. The
reference flat resolvent uses circulation cutoff8. Applying the infinite
finite-range Hamiltonian to its extended finite-support solution gives a
resolvent residual about2.25e-16; the norm bound follows from the imaginary
resolvent parameter. This is floating residual corroboration, not an
interval certificate. No numerical rate or all-state convergence constant
is inferred from these data.

`exact_instrument_control.py` supplies rational N4 electric checks and the
rotor H4 identity. Its spin-one shifted characteristic factors were an
exploratory attempt to find a simple sharp-projection witness; they are
preserved but are not load-bearing spectral evidence. The simpler
`exact_cross_gram.py` computes the nonzero rational smooth-filter witness
and the exact integral implication for sharp windows. The count ODE and
normalization in (14) are checked symbolically, and an unchanged first rate16
is rejected by the independently reconstructed projected rate8.

The main filter run and exact cross-Gram run exited zero. The first exact
instrument run reached JSON serialization and failed because a SymPy Integer
in factor metadata was not converted to a Python int. The original script,
full failed streams and actual receipt are retained. The repaired run changes
only metadata serialization and exits zero. No mathematical assertion was
removed or weakened. `run.py` records actual commands, times, environments,
source hashes, exit codes and complete stream hashes. No failed result is
silently replaced.

The prepared note remains SHA
`94cef6093e754d59cf11ca07c1124f6ee8becd944c07865af21b1c6dd05ec2a9`,
its author seal `dfc55f6eac748bb11130fe3a8e5544194c6babd810c0c06d45e177c56c72df7e`,
and the ring spectrum note
`b9c30d8418cb4d4c577ea193dee8482d2d0c92125823593feb2a7c01b8310bf5`.
Other exact identities and matched prior-manifest rows are in
`SOURCE_IDENTITIES.json`. These checks reuse prior premises openly; the new
Hamiltonian/filter/source bridges were derived before any new author access.
Progress findings were sent to root during reconstruction, and root's draft
was stated in the dispatch to have been frozen beforehand. No reciprocal
author independence beyond that timeline is inferred.

The compact recovery state is this report: all bounded obligations above
are discharged under the listed checked premises; the candidate-source
comparison is the next authorized phase after PRE. The exact changed-target
conclusion remains separate from any reservoir, microscopic realization,
native selection or larger-volume question. No checkpoint file, Git state,
claim registry, formal audit or publication surface was edited. All writes
are confined to the assigned independent packet. The restricted reviewer
skill was used for proof/domain/instrument scrutiny, not to start a generic
review loop or confer formal retained/no-go status.
