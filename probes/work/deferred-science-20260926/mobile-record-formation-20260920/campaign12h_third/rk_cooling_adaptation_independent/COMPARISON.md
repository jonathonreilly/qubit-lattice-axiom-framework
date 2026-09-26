# Bounded author-source comparison: adaptation of record cooling

The three frozen author arguments agree with the independent reconstruction,
subject to one narrow prose correction F1 below. I found no further mathematical
repair in the specified finite models. This is a source-bound scientific
comparison, not a formal audit or publication decision.

## 1. Read boundary and preserved evidence

The independent reconstruction was completed and sealed before author adaptation
access in `PRE_COMPARISON_SEAL.json`, SHA-256
`6776ebe9567241e0d32f3ff16db4512cc9e78e0325eb0b766ce8b86886726570`.
Its report, three scientific checkers, all outputs and preserved bookkeeping
failure remain unchanged. That seal's five source and 34 artifact bindings were
authenticated again in this comparison.

After explicit authorization, I read all three author notes, all three complete
runner sources, all result fields, all run streams and receipts, the separate
optimum certificate, and the context receipt. The 20 artifacts bound by
`RK_COOLING_ADAPTATION_AUTHOR_SEAL.json`, SHA-256
`4b707760dab45089bda59645caadc1a3d7bdc6e9ee3cc730a3be5c48a29b3937`,
all authenticate. No author runner was executed here. Authentication of an
author run is distinguished from independent mathematical verification.

Complete source identities are in `COMPARISON_RESULTS.json` and `FINAL_SEAL.json`.
The three note and three runner identities are:

| Source | SHA-256 |
|---|---|
| ADAPTING_RECORD_COOLING_AWAY_FROM_THE_RK_POINT.md | 791875b79af460884cb30802f4a454eaabc4ec6514a82fbc0c09e56573f4fd71 |
| FINITE_CUBIC_RECORD_COOLING_AND_RETUNED_GROUND_PREPARATION.md | e6cc8029beca2c290935ccac94147b3c679a7bfef8db521c972a055514624d63 |
| LOCAL_WEIGHTED_RECORD_COOLING_AND_FINITE_GROUND_APPROXIMATION.md | f7fec2a31f61a020ff7b305617c98ca9b397bb408b3902472b24b40406233d4c |
| rk_cooling_hamiltonian_change_check.py | df1f1793afb5e84fb5811225c9a7d43451be4d246b56067fa2c72158334e869e |
| cubic_record_cooling_stationary_screen.py | 39a8b1d908145576238b3171e4736c7254e1493b436a73afcc270f67df473419 |
| local_weighted_record_ground_screen.py | 5712326ef62ff7b93c6c772a5473b2745addf08c7ef123ea1f29a9fab32e5124 |

The unchanged unweighted theorem and previously checked evidence are reused at
the PRE identities. The author geometry runner's direct dependency hash
`9faf0f87d0574368feb0f656308308c269d3df922bfff7576a8d6d10182b5552`
also matches its previously reviewed source. Newer hard-core ring/density,
coherent-ramp, checkpoint and registry sources were not opened. The adaptation
context receipt's literature/repository-history statements were read as
provenance, not independently certified as additional theorem imports.

## 2. F1: repeat the nonzero-detuning condition in the negative conclusion

`ADAPTING_RECORD_COOLING_AWAY_FROM_THE_RK_POINT.md`, lines 37–38, says:

> For nonconstant d(c), the unchanged cooling generator has no pure stationary
> state.

The source defines real delta, including zero. At delta=0 the uniform vector is
annihilated by every jump and is an eigenvector of the RK Hamiltonian even when
d(c) is nonconstant. The independent exact five-state countercontrol already
sealed in `FINITE_COOLER_RESULTS.json` records this positive exception.

The preceding line 35 has the right condition. The required correction is to
repeat it in the conclusion, for example:

> For nonconstant d(c) and nonzero delta, the unchanged cooling generator has no
> pure stationary state.

No equation, numerical value or runner calculation needs changing. The second
author note explicitly assumes nonzero delta and positive flippability variance,
and the author finite controls correctly label their no-pure-state test as being
at nonzero delta. F1 is a statement-scope repair, not a failure of those proofs.
The reviewed source remains frozen and unedited in this packet; a later repair
requires a separate acknowledgment.

## 3. Unchanged cooler under the detuned Hamiltonian

Write P0=|u><u| for the uniform state, D for the diagonal flippability count,
and K_loss=sum gamma_p L_p^dag L_p. Nilpotency of every L_p forces its only
possible pure-state eigenvalue to be zero. The purity derivative then implies
that a pure stationary state belongs to the common dark kernel. Connectedness
makes that kernel span(u). Consequently pure stationarity is equivalent to
delta=0 or constant d(c). This verifies the main argument and both exceptions.

The exact residual is

    G_delta(P0)=i delta[D,P0],
    ||G_delta(P0)||_HS^2=2 delta^2 Var_u(d),
    ||G_delta(P0)||_1=2|delta| sqrt(Var_u(d)).

The path comparison in the finite-cubic note gives the conservative but valid
loss gap gamma_min/(Ddim-1)^2. Multiple flip channels between the same two
configurations only increase the form. Its superoperator norm bound

    c=2 m (2J+|delta|+gamma_max)

dominates the Hamiltonian commutator and all dissipators on arbitrary trace-class
matrices. Combining it with pure-state trace-distance control gives exactly the
stated positive stationary jump-rate bound. Compactness of Cesaro averages then
proves the expected long-time rate bound without stationary-state uniqueness.
The assertion is finite dimensional, within one connected flip component, and
requires positive rates on every active plaquette.

The independent pre-source report proves a stronger, separate fact: for the
specified jump unraveling, nonzero detuning and nonconstant d imply that the
effective no-jump Hamiltonian has no real eigenvalue. Its finite propagator
decays exponentially, uniformly over initial unit vectors. There is almost
surely a subsequent jump after every finite history, and bounded intensity
prevents explosion; hence the total number of jumps is almost surely infinite.
This is independent additional support, not a result attributed to the author
notes, and it is not a trajectorywise positive-rate law of large numbers.

## 4. Retuning to an exact finite ground vector

Section 3 of the finite-cubic note goes beyond the neutral pre-source brief. I
checked it after source access. For J>0, connected nonpositive off-diagonal flip
amplitudes give a strictly positive unique finite-component ground vector psi by
the elementary shifted-matrix Perron argument. Ground-amplitude ratios are
explicitly supplied to the proposed channels.

For each full configuration edge e=(a,b), the normalized pair vectors s_e,d_e
are orthogonal, A_e=|s_e><d_e| annihilates psi, and

    A_e^dag |psi><psi| A_e = w_e |d_e><d_e|,
    w_e=psi_a^2+psi_b^2.

The original H_delta commutes with |psi><psi|. Its fidelity derivative is
therefore Tr(M rho), M=sum eta_e w_e |d_e><d_e|. Strictly positive amplitudes
and connectedness imply ker M=span(psi), so M>=mu(I-|psi><psi|). The claimed
exponential fidelity/trace-distance bound follows. Since K_ad annihilates psi,
K_ad<=||K_ad||(I-|psi><psi|); integration yields the finite expected jump-count
bound ||K_ad||(1-f(0))/mu. This checks the rate and weight normalization in
equations (5)–(7).

The new independent exact control uses seven configurations on a cycle with two
chords, target amplitudes (1,3,2,5,4,7,6), and nine unequal rational rates. It
checks the dual fidelity identity, nilpotency, projector normalization and
rank-six kernel exactly. A numerical positive mu is only supplementary; the
kernel and positivity argument are exact. This control does not use the
author's finite-cubic ground vector.

The source correctly warns that edge resolution includes spectator
configurations and can require volume-size controls. A small plaquette
difference between a,b does not make A_e a local operator. Its fidelity bound
also contains the weight w_e, equal to 2/Ddim at the uniform vector. The
construction supplies no efficient local ground-state compiler.

## 5. Weighted local cooler: locality and attraction

The author weighted theorem is the resolved (p,m) generator, with finite real
theta, strictly positive rates on every active class, and Hamiltonian exactly a
real linear combination of the corresponding minus projectors. It does not
claim to be the detuned H_delta evolution during preparation.

Only plaquettes sharing a link with p can change their flippability when p
flips. There are at most twelve other such plaquettes on the stipulated cubic
link lattice. The conservative support bound 4+12*3=40 links is valid. A fresh
independent link-set construction gives overlap/support counts (11,20),
(13,30), and (13,32) on sides 2,3,4, matching the author controls. The side-two
model retains 24 distinct positive-axis links; it is not collapsed to a simple
undirected graph with twelve edges. The random author backgrounds are finite
locality controls, not the proof of the uniform support bound.

The exact pair identity is

    Pminus v(t)=g(t)L^dag v(t),
    g(t)=r(1-exp(t Delta))/(1+r^2 exp(t Delta)),
    v(t)=exp(tF)psi_theta.

It holds with one scalar g throughout a (p,m) jump because r and the fixed
plaquette displacement Delta are constant on that class. A symbolic two-state
control independently verifies the identity. Reversing the pair orientation
and replacing r by 1/r changes L only by an overall minus sign; the dissipator
and minus projector are unchanged. Arbitrary class rates are allowed in the
attraction theorem; cubic covariance of the whole generator additionally
requires the corresponding covariant choice of rates and Hamiltonian weights.

For a putative invariant subspace W perpendicular to psi_theta, the compressed
effective loss operator has strictly positive Hermitian part. Equation (5) is
thus invertible at t=0 and near zero. The weighted exponential vectors span the
full finite configuration space by a separating F and the Vandermonde argument.
The author's exclusion of W is valid. This checks its proof, rather than merely
appealing to uniqueness of a common dark vector.

My sealed proof uses a different construction: a finite geometric-series
inverse of I+r^2 T_p lowers the degree of the weighted polynomial difference,
and induction forces every polynomial vector into the orthogonal complement
of W. That independent degree-lowering proof is retained unchanged. Both
arguments require the resolved class coefficient. The previously sealed
countercontrol also remains relevant: even at theta=0, retaining distinct
m-outcomes can give a different CP generator from recombining them coherently
into one L_p. The author does not claim equality of those generators.

The finite absorbing-sector argument gives model-dependent exponential
attraction and finite expected total jumps. Neither proof gives a volume-uniform
rate, a theta-to-infinity assertion, or robustness under arbitrary extra
Hamiltonian terms. Fresh probes, export of the outcome, and control/timing are
still supplied resources.

## 6. Gaussian diagnostic

With a=Ks, b=U+Ws, r=sqrt(K/W), nu=gamma s, and Delta=a/r-br, the independently
derived stationary covariance is

    Q=r/2+a Delta/(nu^2+4ab),
    P=1/(2r)-b Delta/(nu^2+4ab),
    C=nu Delta/[2(nu^2+4ab)].

The author's exact covariance, determinant, energy, old-mode occupation,
retuned-ground occupation, purity and jump intensity agree. In particular,
energy=(a/r+br)/4 is independent of positive gamma, while the density itself
and jump output need not be. For U>0, stationarity followed by s down to zero
gives Q->r/4, sP->U/(4sqrt(KW)), C->-gamma/(8sqrt(KW)), energy->Ur/4, and
jump intensity->gamma U/(8W). Setting U=0 restores the pure old vacuum.
Retuning r to sqrt(a/b) removes the mismatch and prepares the supplied
oscillator ground state.

The order of limits is essential: s=0 and gamma=0 are not members of the
positive-damping convergence statement. The mean photon count and covariance
claims require the corresponding finite initial moments where time evolution
of those unbounded observables is invoked. Stationary Gaussian purity is not
being inferred from arbitrary non-Gaussian second moments.

I independently reduced all five author parameter rows to these formulas and
recomputed their reported covariance errors. The finite-Fock controls are
numerical convergence checks, with the largest final reported covariance error
9.4651e-8. The two matched-bath final errors are 3.33e-15 and 1.121e-12. Tiny
negative numerical occupations or probabilities at that roundoff level are
not exact physical statements. The symbolic oscillator calculation supplies
the proof; no thermodynamic spin-to-Gaussian derivation or native realization
of gamma s is supplied or inferred.

## 7. Finite cubic and variational evidence

The independently enumerated 864 configurations, degree census and all 3456
flip pairs agree with the author's geometry identity. The 24-link convention,
flippability mean 8 and variance 16/3 match exactly. The author stationary
runner enumerates 384 translation/proper-rotation/complement actions and 2723
ordered-pair orbits, checks jump covariance, solves the reduced equation and
checks the resulting full density against the full generator. Its code's
row/column signs, coherent spectator terms and unit-rate loss normalization
agree with the stipulated generator. A comment mentions group closure; the
implemented direct checks are enumeration of the explicit group actions and
invariance of every orbit under them, which suffice here. I do not attribute an
additional unimplemented group-closure routine to the run.

The finite-cubic density screen is authenticated author numerical evidence,
with inspected complete code and full residual/positivity controls. I did not
independently repeat all 864-dimensional stationary solves or certify them
with interval arithmetic. The source explicitly avoids inferring global
stationary uniqueness from the symmetry-reduced solve. I found no such
overclaim elsewhere in these notes.

For the weighted variational family, the independent sealed census reconstructs
all four author energy numerators and normalization polynomials exactly. Here
the author uses x=exp(theta), whereas my pre-source derivation uses
q=exp(theta/2); x=q^2. The comparison checker computes all four derivative
polynomials afresh, verifies each reported rational isolating interval and
proves by exact root counting that there is exactly one positive critical
root. The derivative starts negative and ends positive in each case, and
both endpoint energies agree. Thus the claimed global minimum is within the
stated one-parameter family, not over all states.

At delta=1/5, the two independent calculations give

    theta*=0.0619383884167354...,
    E_trial=-1.634159908484452...,
    E0=-1.64244259196795...,
    1-fidelity=0.0025601041635... .

The author value of E0 lies inside my independently constructed exact rational
ground-energy enclosure. Its quoted optimizer differs only within its rational
root interval. The other three energy-polynomial minima are independently
verified here, while their full numerical ground spectra/overlaps remain
authenticated author computations rather than independent full diagonalizations.

The inequality 1-fidelity<=(E_trial-E0)/gap is the finite spectral theorem.
The source's later trace-distance bound follows because H_delta fixes its
ground projector and unitary evolution preserves trace distance. It requires
turning off the preparation bath or explicitly changing the subsequent model.
For all four reported rows, I checked the bound and its factor of two from the
reported finite spectrum. No thermodynamic fidelity or phase conclusion follows
from this component calculation.

## 8. Reproduction, failures and final limits

Run `comparison_check.py` with Python 3.13 and the NumPy/SymPy versions recorded
in the preserved runtime evidence. It authenticates all 20 author bindings and
39 PRE bindings, checks all receipts and stream correspondences, and performs
the selective exact and numerical reductions described above. Its first
execution returned zero; full stdout equals `COMPARISON_RESULTS.json` and
stderr is empty. The author Gaussian and cubic runs each have one preserved
SciPy integer-to-float FutureWarning; their streams are not described as empty.
The weighted author run has empty stderr. The cubic log contains progress rows
that match the result fields, rather than the entire final result document.

The old pre-seal helper failure remains under
`failed_attempts/seal_stderr_assumption/`: it wrongly assumed all independent
scientific stderr streams were empty despite a benign SciPy warning. It did
not change a scientific target, parameter, tolerance, checker or result. There
was no new failed comparison execution.

No author source, old evidence, Git state or governance data was changed. F1 is
the sole requested repair against these frozen identities. Unchanged finite
proofs, fresh-resource assumptions, external context limits, numerical-vs-exact
boundaries and open thermodynamic/implementation obligations are retained.
