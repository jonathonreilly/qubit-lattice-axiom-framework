lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-29T01:52Z

# Strategy mining inside mathematical physics, mapped to (PUR-io) (FINISH row 1686)

Started 2026-11-28T13:52:13Z (date -u), pinned at commit 5cbbee36f, branch claude/ym4d-hard-route.
Worker: Mac mini Claude worker 1, Claude Fable 5.2, effort high. No subagents. Row 1682's file is not read.

Status of this file: research-stage working state. Nothing here is a public claim. Labels on every claim:
PROVED (written in full here), CITED (exact reference), ARGUED (my judgement), GUESSED. A reference I
could not confirm in this session carries UNVERIFIED.

## 0. Plan (save protocol: this file is written step by step)

- Step 0. Read the crux card and the Lean statements it cites (Purity, PurIo, Stage0, Transfer, Offset statement).
  Write the target in my own notation. [section 1]
- Part 1 (closed folder). At least fifteen hard problems of mathematical physics that fell. Ten lines each:
  hardness, decisive move, new object, one idea or chain, reference, why the move fails or is untried for the
  4D non-abelian infrared. [section 2, written in three batches]
- Part 2 (closed folder). At most ten strategy types. For each: the (PUR-io) analogue with object, statement,
  first estimate, the step that reads non-abelian structure and dimension, the U(1) failure, the likely place
  it dies. [section 3]
- Part 3 (Phase 2, folder open). Compare each candidate with library/open-registry.md and the files of crux
  card section 3. Mark new or on file. [section 4]
- Part 4. Rank the five best new candidates. First buildable component for the top three: an exact lemma.
  Reading list of at most fifteen papers with the question each read must answer. [section 5]
- RESULT line. [section 6]

Closed-folder rule for Parts 1 and 2: besides the crux card and the Lean files it cites, no file of this lane
is read before section 4. Sections 1 to 3 are written from the crux card, the Lean statements and the
published literature only.

## Progress log

- 2026-11-28T13:52Z: file created; crux card, GOAL.md, FINISH head and row 1686 read.
- 2026-11-28T14:11Z: Lean statements read (Purity.lean in full; PurIo.lean; Stage0 definitions; Transfer
  L548-L666; Offset L701 statement). Section 1 written.

## 1. The target in working notation (from the crux card and the Lean files only)

Notation. n = side of the spatial periodic cube, n = ℓ L^K. T = T_β = Wilson SU(2) transfer operator on
L²(SU(2)^links of the n³ slice) (`Transfer.lean` L548-L666: T = e^{-βV/2} · (temporal convolution, averaged
over the gauge group) · e^{-βV/2}; positive). P₀ = `neutralProj` = average of the eight centre translations
(`Stage0.lean` L71). u = n/512. Purity p = Tr(P₀T^{2u}) / (Tr P₀T^u)².

Facts used below. Each is one line; (F1)-(F4) are PROVED here, (F5) is ARGUED.

- (F1) With λ_0 ≥ λ_1 ≥ ... ≥ 0 the eigenvalues of T on Ran P₀ and w_i = λ_i^u / Σ_j λ_j^u:
  p = Σ w_i². So w_0² ≤ p ≤ w_0. With D(t) = Σ_i (λ_i/λ_0)^t: D(u) − 1 ≤ 25/√457 − 1 = 0.1694...
  implies p ≥ 457/625. Proof: p ≥ w_0² = D(u)^{-2}; and Σ w_i² ≤ max w_i.
- (F2) p is non-decreasing in u at fixed (n, β). Proof: d/du log p = 2(⟨log λ⟩_{2u} − ⟨log λ⟩_u) ≥ 0, since
  the mean of log λ under weights λ^t is non-decreasing in t (its derivative is a variance).
- (F3) Trial-vector form. For every unit vector φ in Ran P₀: p ≥ 2⟨φ, ρ φ⟩ − 1, ρ = P₀T^u / Tr P₀T^u.
  Proof: 0 ≤ Tr(ρ − |φ⟩⟨φ|)² = p − 2⟨φ,ρφ⟩ + 1.
- (F4) Coupling-integral form. For fixed (n, u): d/dβ log p = E_{2u}[A] − 2 E_u[A], where A is the β-derivative
  of the exponent (A = −Σ_p (1 − ½ tr U_p) on the torus n³ × t) and E_t is the expectation in the normalised
  measure whose partition function is Tr P₀T^t (the sum of the eight temporally twisted Wilson measures on
  n³ × t, each positive). At β = 0 the operator T has rank one, so p = 1. Hence
  −log p(n,u,β) = ∫_0^β ( 2E_u[A] − E_{2u}[A] )(b) db. The integrand compares the total action on the long
  torus with twice that on the short torus, at every coarser coupling b ≤ β on the same lattice.
- (F5) Channel exchange (ARGUED; the lattice is hypercubic). Tr T^t on n³ equals Tr (T_slab(t))^n, with
  T_slab(t) the transfer operator in a spatial direction on the slice n × n × t. So p ≈ 1 says that the
  ground energy of the slab of thickness 2u is twice that of thickness u up to 0.3/n in lattice units:
  no Casimir energy at plate distance ℓ/512. For free massless vector bosons the defect is of order
  (n/u)³ = 512³ times a constant. This is a restatement. It is not progress.

Physical reading (crux card section 2): a thermal state at temperature 512/ℓ in a box of side ℓ, with ℓ far
above the confinement length. The same statement fails for weak four-dimensional compact U(1).

## 2. Part 1 (closed folder). Twenty-eight hard problems that fell

Format per problem: H = what made it hard. M = the decisive move, as a pattern. O = the new object.
C = one idea or a chain. R = reference. YM = why the move fails, or is untried, for the 4D non-abelian infrared.
References are CITED from memory of the published record; a reference I could not confirm carries UNVERIFIED.

### 2.1 Constructive field theory and the renormalisation group

**P1. Mass gap of weakly coupled P(φ)₂ (Glimm, Jaffe, Spencer).**
H: infinitely many degrees of freedom; no convergent perturbation series. M: perturb around a massive
Gaussian measure in finite-range pieces; decouple far regions by interpolating the covariance; resum with
a tree bound (cluster expansion). The gap of the free part survives. O: the cluster expansion with
interpolated covariances. C: one idea, after the ultraviolet work of Nelson and Glimm-Jaffe.
R: J. Glimm, A. Jaffe, T. Spencer, "The Wightman axioms and particle structure in the P(φ)₂ quantum field
model", Ann. Math. 100 (1974) 585-632.
YM: the reference measure must already have a gap. Pure Yang-Mills has no massive Gaussian part at any scale
where the coupling is small. The move starts only after a mass exists.

**P2. Ultraviolet stability of 4D lattice Yang-Mills (Balaban; Lean release of Sussman and Alpoge).**
H: gauge invariance forbids a momentum cutoff; large fields have no perturbative control. M: block averaging
that commutes with gauge transformations; split each step into small-field regions (perturbative, exact
effective action with running coupling) and large-field regions (suppressed by the action, summed by a
polymer expansion). O: gauge-covariant block averages, background-field minimisers, the R operation.
C: a long chain of disparate tools. R: T. Balaban, "Renormalization group approach to lattice gauge field
theories I, II", CMP 109 (1987) 249-301 and CMP 116 (1988) 1-22; "Large field renormalization I, II",
CMP 122 (1989) 175-202 and 355-392.
YM: it is the base of this lane. It controls each scale while the running coupling is small. It stops at the
scale where the coupling is of order one. It proves no infrared property.

**P3. Dynamical mass in the large-N Gross-Neveu model (Kopper, Magnen, Rivasseau).**
H: an asymptotically free model whose mass is exp(−c/g²), invisible to every order of perturbation theory.
M: an exact change of variables (the intermediate field σ) after which the mass is the position of a saddle
point; then 1/N controls the fluctuations uniformly through the crossover. O: a multiscale expansion around
a non-perturbative vacuum of the auxiliary field. C: a chain: intermediate field, saddle, 1/N, cluster
expansion with the new mass. R: C. Kopper, J. Magnen, V. Rivasseau, "Mass generation in the large N
Gross-Neveu model", CMP 169 (1995) 121-180.
YM: this is the only rigorous proof known to me of an exponentially small dynamical mass in an asymptotically
free model on a non-hierarchical lattice (ARGUED). It needs a vector-like large N and an auxiliary field in
which the mass is classical. SU(2) has N = 2 and no known local auxiliary field with a positive weight.

**P4. Infrared end of the hierarchical O(N) σ-model (Gawędzki, Kupiainen).**
H: follow one renormalisation-group flow from the asymptotically free region through the crossover into the
high-temperature (massive) region. M: use a model where the block-spin map is an exact single-site integral
operator (hierarchical lattice), and take N large so that the crossover is uniform. O: the exact recursion
for a single-site density. C: exactness plus 1/N. R: K. Gawędzki, A. Kupiainen, "Continuum limit of the
hierarchical O(N) non-linear σ-model", CMP 106 (1986) 533-550.
YM: a hierarchical (Migdal-Kadanoff type) recursion for gauge theory treats the four-dimensional gauge
theory like a two-dimensional spin model. It then confines compact U(1) in four dimensions as well, which is
false (Guth; Fröhlich-Spencer, P7). An argument of this type cannot be right as it stands. The published
attempt along this line (Tomboulis 2007, arXiv:0707.2179) was shown incomplete (Ito, Seiler, arXiv:0711.4930).

**P5. Mass gap and confinement at strong coupling (Osterwalder, Seiler).**
H: none after Wilson's idea; the point was rigour with reflection positivity. M: expand around the product
Haar measure (β = 0); polymers are connected plaquette sets; the Wilson loop needs a tiling surface, so it
obeys the area law, and the transfer matrix has a gap. O: lattice gauge theory as a reflection-positive
statistical system. C: one idea. R: K. Osterwalder, E. Seiler, "Gauge field theories on a lattice",
Ann. Phys. 110 (1978) 440-471.
YM: valid for β below a fixed constant, for every compact group and dimension. It reads neither the group
nor the dimension. On the calibrated trajectory β_K tends to infinity.

**P6. Confinement and mass in 3D compact U(1) at every coupling (Göpfert, Mack; Brydges, Federbush).**
H: weak coupling, no small parameter for confinement; the mass is exp(−c/g²). M: an exact duality maps the
model to a Coulomb gas of monopoles (a sine-Gordon field); the gas is dilute at weak coupling; Debye
screening gives the mass; a block-spin step first renormalises the monopole activity. O: the monopole gas
representation with positive weights. C: a chain: duality, renormalisation of activities, expansion around
the screened (mean-field) Gaussian. R: M. Göpfert, G. Mack, "Proof of confinement of static quarks in
3-dimensional U(1) lattice gauge theory for all values of the coupling constant", CMP 82 (1982) 545-606;
D. Brydges, P. Federbush, "Debye screening", CMP 73 (1980) 197-246.
YM: the dual of a non-abelian theory has signed weights (recoupling coefficients), so the gas has no
probability meaning. In four dimensions monopoles are loops, not points; their gas does not screen at weak
coupling (that is the U(1) Coulomb phase). A version for SU(2) needs monopoles defined at the scale where the
coupling is of order one.

**P7. The massless phases: Kosterlitz-Thouless and 4D compact U(1) (Fröhlich, Spencer; Guth).**
H: prove that a gas of topological defects stays bound at every scale. M: a multiscale partition of defect
configurations into neutral clusters with scale-dependent entropy and energy bounds; each neutral cluster
renormalises the spin-wave Gaussian only slightly. O: the multiscale neutral-multipole expansion.
C: one idea, heavy combinatorics. R: J. Fröhlich, T. Spencer, "The Kosterlitz-Thouless transition in
two-dimensional abelian spin systems and the Coulomb gas", CMP 81 (1981) 527-602; "Massless phases and
symmetry restoration in abelian gauge theories and spin systems", CMP 83 (1982) 411-454; A. Guth, "Existence
proof of a nonconfining phase in four-dimensional U(1) lattice gauge theory", Phys. Rev. D 21 (1980) 2291.
YM: this is the control case. It is a proof that the target statement is false for abelian groups. A correct
attack on (PUR-io) must contain a step that this proof contradicts when the group is U(1).

### 2.2 Critical phenomena and correlation inequalities

**P8. Infrared bounds and continuous symmetry breaking (Fröhlich, Simon, Spencer).**
H: prove long-range order for continuous spins in d ≥ 3 with no small parameter and no contours.
M: reflection positivity gives Gaussian domination, Z(h) ≤ Z(0); this bounds the two-point function in
momentum space by the free propagator; a sum rule then forces a condensate at k = 0. O: the infrared bound.
C: one idea plus a sum rule. R: J. Fröhlich, B. Simon, T. Spencer, "Infrared bounds, phase transitions and
continuous symmetry breaking", CMP 50 (1976) 79-95.
YM: the bound is an upper bound on fluctuations and it proves order. The gap needs the opposite: disorder at
long distance. For the Wilson action the shift trick works only across one time layer in temporal gauge. It
then bounds the Fourier transform of the 1 × t Wilson loop, an ultraviolet quantity (ARGUED).

**P9. Sharpness of the phase transition (Aizenman, Barsky; Menshikov; Duminil-Copin, Tassion) and finite
criteria (Simon; Lieb; Dobrushin, Shlosman).**
H: show exponential decay in the whole disordered phase, up to the critical point, with no expansion.
M: a finite criterion: one inequality on one finite set S (the sum over the boundary of S of the two-point
function inside S is less than 1) implies exponential decay; a differential inequality in the coupling
shows the criterion holds at every coupling below the critical one. O: the quantity φ_β(S); earlier, partial
differential inequalities in two variables (coupling and field). C: two links: finite criterion, then
differential inequality. Both need a positive representation (percolation or random currents).
R: M. Aizenman, D. Barsky, CMP 108 (1987) 489-526; M. Aizenman, D. Barsky, R. Fernández, J. Stat. Phys.
47 (1987) 343-374; H. Duminil-Copin, V. Tassion, "A new proof of the sharpness of the phase transition for
Bernoulli percolation and the Ising model", CMP 343 (2016) 725-745; B. Simon, CMP 77 (1980) 111-126;
E. Lieb, CMP 77 (1980) 127-135; R. Dobrushin, S. Shlosman, "Constructive criterion for the uniqueness of
Gibbs field", in Statistical Physics and Dynamical Systems, Birkhäuser 1985.
YM: the consumer of (PUR-io) is already a finite criterion. The missing half is the differential
inequality. It rests on Griffiths-type inequalities. The Wilson plaquette is a positive-definite function on
the product group only when the group is abelian (section 3, S1). And where the inequalities hold (U(1)),
the answer is "massless". So this engine cannot be the one that reads the non-abelian structure.

**P10. Sharpness for dependent models by decision trees (Duminil-Copin, Raoufi, Tassion).**
H: no independence, no BK inequality, no random currents for the random-cluster model. M: import the OSSS
inequality from theoretical computer science: the variance of a Boolean function is at most the sum over
bits of (revealment by a randomised algorithm) × (influence). An exploration algorithm with small
revealment turns it into a differential inequality. O: OSSS for monotone measures. C: one imported tool.
R: H. Duminil-Copin, A. Raoufi, V. Tassion, "Sharp phase transition for the random-cluster and Potts models
via decision trees", Ann. Math. 189 (2019) 75-99.
YM: the pattern "import a variance inequality that needs only monotonicity" is untried for gauge theory.
It needs a monotone (FKG) measure on a lattice of events. No such structure is known for SU(2).

**P11. Marginal triviality of φ⁴ in four dimensions (Aizenman, Duminil-Copin; Aizenman; Fröhlich).**
H: the marginal case, where the logarithm decides. M: write the truncated four-point function as an
intersection probability of random currents (switching lemma); prove by a multiscale argument that the
intersection clusters are sparse on a logarithmic scale. O: random currents and intersection clusters.
C: a chain: exact geometric representation, then multiscale analysis of the geometry.
R: M. Aizenman, H. Duminil-Copin, "Marginal triviality of the scaling limits of critical 4D Ising and φ⁴₄
models", Ann. Math. 194 (2021) 163-235; M. Aizenman, CMP 86 (1982) 1-48; J. Fröhlich, Nucl. Phys. B200
(1982) 281-296.
YM: this is the infrared-free marginal case, the opposite sign. The pattern is: turn the non-Gaussian
quantity into a probability of a geometric event. For SU(2) the known surface or current representations
carry signs (P20).

**P12. p_c = 1/2 and the self-dual point (Kesten; Beffara, Duminil-Copin).**
H: locate a non-perturbative threshold exactly. M: a duality symmetry pins the value of a crossing
observable at one parameter value (probability 1/2 by symmetry); a sharp-threshold theorem then moves off
that point. O: Russo-Seymour-Welsh box crossings. C: symmetry, then sharp threshold.
R: H. Kesten, "The critical probability of bond percolation on the square lattice equals 1/2", CMP 74 (1980)
41-59; V. Beffara, H. Duminil-Copin, "The self-dual point of the two-dimensional random-cluster model is
critical for q ≥ 1", Probab. Theory Related Fields 153 (2012) 511-542.
YM: 't Hooft's electric-magnetic relation on the torus is an exact Fourier transform of the twisted
partition functions, and the hypercubic group exchanges electric and magnetic twists. But the theory is not
self-dual: no parameter value is fixed by the duality. The pattern would need a size at which a duality-odd
combination is forced to vanish. None is known (ARGUED).

**P13. Rounding of first-order transitions by disorder in d = 2 (Aizenman, Wehr; Imry-Ma).**
H: prove absence of a phase with no expansion. M: a soft contradiction between two scalings: the free-energy
difference between two boundary conditions is at most a surface term, but, if the phases differed, its
random fluctuation would be at least (volume)^{1/2}. In d ≤ 2 the second exceeds the first.
O: a metastate-free definition of the order parameter through free-energy differences. C: one idea.
R: M. Aizenman, J. Wehr, "Rounding effects of quenched randomness on first-order phase transitions",
CMP 130 (1990) 489-528.
YM: the pattern is "two bounds on one free-energy difference with different scaling laws". The twisted
free energies are the natural candidates. A soft contradiction cannot exclude a scale-invariant infrared
limit: asymptotically free SU(2) theories with adjoint matter share all the soft structure and are believed
massless in the infrared (section 3, test (g7)).

### 2.3 Spectral gaps of quantum spin systems

**P14. The AKLT gap, in one dimension and on the hexagonal lattice (Affleck, Kennedy, Lieb, Tasaki; Knabe;
Lemm, Sandvik, Wang; Pomata, Wei).**
H: a gap for a non-commuting Hamiltonian, in two dimensions with no exact solution. M: frustration-freeness
gives H² ≥ γH as the target; a finite-size criterion (Knabe) reduces it to the gap of one finite patch being
above an explicit threshold; in two dimensions the patch gap is certified by a numerical computation with
error control. O: the finite-size criterion; weighted versions that lower the threshold. C: a chain: exact
ground-state structure, finite criterion, certified computation.
R: I. Affleck, T. Kennedy, E. Lieb, H. Tasaki, CMP 115 (1988) 477-528; S. Knabe, J. Stat. Phys. 52 (1988)
627-638; M. Lemm, A. Sandvik, L. Wang, Phys. Rev. Lett. 124 (2020) 177204; N. Pomata, T.-C. Wei,
Phys. Rev. Lett. 124 (2020) 177203.
YM: the lane already has a finite criterion with an explicit threshold (the κ-seed). The certified
computation is the missing link. It is out of reach at β_K: the lattice side is at least 2^70. A carry
from a coarse lattice to the cutoff K is a non-perturbative universality statement (crux card section 2).

**P15. Stability of a gap under perturbation (Bravyi, Hastings, Michalakis; Michalakis, Zwolak; Hastings).**
H: a gap is not stable under extensive perturbations in general. M: local topological order makes local
perturbations relatively bounded with respect to the unperturbed Hamiltonian, after a quasi-adiabatic
unitary that is quasi-local by Lieb-Robinson bounds. O: quasi-adiabatic continuation; the local
indistinguishability condition. C: a chain of three tools.
R: S. Bravyi, M. Hastings, S. Michalakis, J. Math. Phys. 51 (2010) 093512; S. Michalakis, J. Zwolak,
CMP 322 (2013) 277-302; M. Hastings, Phys. Rev. B 69 (2004) 104431.
YM: stability needs a gapped starting point. The only one is strong coupling (P5). The path from there to
β_K passes the crossover with no bound on the gap along it. The pattern "a gap persists along a path while
no local order parameter can change" has no rigorous form without a uniform lower bound on the gap.

**P16. Hidden order made local (Kennedy, Tasaki).**
H: the Haldane phase has no local order parameter. M: a non-local unitary maps the hidden string order to
ordinary breaking of a Z₂ × Z₂ symmetry; standard methods then apply. O: the non-local transformation.
C: one idea. R: T. Kennedy, H. Tasaki, "Hidden symmetry breaking and the Haldane phase in S = 1 quantum spin
chains", CMP 147 (1992) 431-484.
YM: the analogue is the exchange of SU(2) for SO(3) by summing over centre twists (gauging the centre
one-form symmetry). The eight-fold twist average in `neutralProj` and the 64-fold signed sum in the κ-weight
are of this type. The map is exact on the torus but it does not create a small parameter.

### 2.4 Stochastic PDE, functional inequalities, random geometry

**P17. KPZ and the dynamic Φ⁴₃ model (Hairer; Gubinelli, Imkeller, Perkowski; Gubinelli, Hofmanová;
Chandra, Chevyrev, Hairer, Shen for Yang-Mills).**
H: the equation contains products of distributions; no fixed-point space existed. M: lift the noise to a
finite list of renormalised polynomial objects; the solution map is continuous in the lifted data; all
probability sits in the lift, all analysis is deterministic. O: regularity structures; paracontrolled
calculus; for gauge theory, a state space of gauge orbits of distributional connections.
C: a chain (algebra, analysis, renormalisation, probability). R: M. Hairer, "Solving the KPZ equation",
Ann. Math. 178 (2013) 559-664; "A theory of regularity structures", Invent. Math. 198 (2014) 269-504;
M. Gubinelli, M. Hofmanová, "A PDE construction of the Euclidean Φ⁴₃ quantum field theory", CMP 384 (2021)
1-75; A. Chandra, I. Chevyrev, M. Hairer, H. Shen, "Langevin dynamic for the 2D Yang-Mills measure",
Publ. Math. IHES 136 (2022) 1-147.
YM: these are short-distance, short-time theories for super-renormalisable models. Four-dimensional
Yang-Mills is critical for them. They give no long-time or large-volume bound. In Φ⁴ the long-time bounds
come from the damping term −φ³ ("coming down from infinity"); Yang-Mills has no damping term.

**P18. Log-Sobolev inequalities along a renormalisation flow (Bauerschmidt, Bodineau, Dagallier), and the
strong-coupling Yang-Mills gap from curvature (Shen, Zhu, Zhu).**
H: uniform relaxation rates up to a critical point, where no single-scale convexity holds. M: run the
Polchinski flow; if the renormalised potential V_t has Hess V_t ≥ −(dλ_t/dt) scale by scale, the Bakry-Émery
argument integrates over scales. For the Ising model the Hessian bound is a covariance bound for the
fluctuation measure, uniform in the external field. For lattice Yang-Mills at small β the single-scale
criterion already holds, because the Ricci curvature of the group is positive. O: the multiscale
Bakry-Émery criterion. C: a chain: scale decomposition, convexity per scale, semigroup interpolation.
R: R. Bauerschmidt, T. Bodineau, J. Funct. Anal. 276 (2019) 2582-2588; Comm. Pure Appl. Math. 74 (2021)
2064-2113; R. Bauerschmidt, B. Dagallier, "Log-Sobolev inequality for the φ⁴₂ and φ⁴₃ measures" and
"Log-Sobolev inequality for near critical Ising models", Comm. Pure Appl. Math. 77 (2024) (pages UNVERIFIED);
H. Shen, R. Zhu, X. Zhu, "A stochastic analysis approach to lattice Yang-Mills at strong coupling",
CMP 400 (2023) 805-851.
YM: the curvature term reads the non-abelian group (Ricci = 0 for U(1)). But the criterion is pointwise in
the field. At weak coupling the Hessian of the Wilson action at a rough configuration is as negative as
−cβ. The multiscale form needs convexity of the effective action at the scale where the running coupling
is of order one. That convexity is the mass gap in another form. It also needs a Gaussian reference
measure, hence a gauge fixing.

**P19. Conformal invariance of critical planar models (Smirnov; Schramm).**
H: identify a scaling limit with no exact solution of the full model. M: find one observable that is
discretely holomorphic with a boundary-value problem; its limit is then forced. A characterisation theorem
(conformal invariance plus the domain Markov property leave a one-parameter family) identifies the rest.
O: the parafermionic observable; SLE. C: observable, then characterisation.
R: S. Smirnov, C. R. Acad. Sci. Paris 333 (2001) 239-244; Ann. Math. 172 (2010) 1435-1467; O. Schramm,
Israel J. Math. 118 (2000) 221-288.
YM: the pattern is "one exactly solvable observable inside an unsolvable model, plus a rigidity theorem".
The exact relations in lattice Yang-Mills are the loop equations. They do not close on a finite family for
N = 2. No rigidity theorem for massive four-dimensional theories is known.

**P20. Gauge-string duality on the lattice at strong coupling (Chatterjee; Cao, Park, Sheffield).**
H: give Wilson loop expectations a convergent geometric expansion. M: solve the loop (Makeenko-Migdal)
equations recursively at small β; the solution is a sum over string trajectories or surfaces.
O: lattice string trajectories; surface sums with Weingarten weights. C: one idea plus combinatorics.
R: S. Chatterjee, "Rigorous solution of strongly coupled SO(N) lattice gauge theory in the large N limit",
CMP 366 (2019) 203-268; S. Cao, M. Park, S. Sheffield, "Random surfaces and lattice Yang-Mills",
arXiv:2307.06790.
YM: convergence needs small β. At finite N the surface weights have both signs, so no probability
argument (percolation, coupling, monotonicity) applies to the surfaces.

**P21. The DOZZ formula for Liouville theory (Kupiainen, Rhodes, Vargas).**
H: prove an exact formula for a non-Gaussian, non-perturbative three-point function. M: build the theory
probabilistically (Gaussian multiplicative chaos); insert degenerate fields; the resulting second-order
differential equations give shift relations in the parameter; analyticity then fixes the answer uniquely.
O: degenerate-field insertions in a probabilistic construction. C: a chain: construction, exact
differential equations, uniqueness of the solution of the functional equations.
R: A. Kupiainen, R. Rhodes, V. Vargas, "Integrability of Liouville theory: proof of the DOZZ formula",
Ann. Math. 191 (2020) 81-166.
YM: the pattern is "derive closed functional equations for one quantity, then prove uniqueness". It needs
an infinite symmetry (Virasoro). Pure Yang-Mills in four dimensions has none known.

### 2.5 Many-body quantum mechanics and disorder

**P22. Ground-state energy of the dilute Bose gas (Dyson; Lieb, Yngvason).**
H: a lower bound for a strongly interacting many-body ground state, with a hard potential. M: Dyson's lemma
trades part of the kinetic energy for a soft potential with the same scattering length; the box is cut into
cells of an intermediate size with Neumann conditions, so that each cell is perturbative.
O: the scattering-length substitution; sliding localisation in later work. C: two moves.
R: E. Lieb, J. Yngvason, "Ground state energy of the low density Bose gas", Phys. Rev. Lett. 80 (1998)
2504-2507; F. Dyson, Phys. Rev. 106 (1957) 20.
YM: the pattern is "replace the hard microscopic interaction by its exact low-energy parameter, then
localise at an intermediate scale". The first half is what the renormalisation group does for the coupling.
The second half fails: cells of the size where the coupling is small are not independent, and the cell
energy has no sign that survives the gluing (no frustration-free form).

**P23. Anderson localisation (Fröhlich, Spencer; Aizenman, Molchanov).**
H: resonances at every scale; the resolvent has no moments. M: (a) multiscale induction with a probability
bound for resonant boxes; (b) fractional moments: the s-th moment of the Green function, s < 1, is finite
and obeys a one-step decoupling inequality that closes. O: multiscale analysis; the fractional-moment
criterion. C: (a) a chain, (b) one idea.
R: J. Fröhlich, T. Spencer, CMP 88 (1983) 151-184; M. Aizenman, S. Molchanov, CMP 157 (1993) 245-278.
YM: both work at large disorder or at spectral edges, that is, perturbatively around a localised limit.
The useful pattern is (b): pick a functional that is finite a priori and closes under one step. For a
ratio of twisted partition functions no such closing inequality is known.

### 2.6 Lattice gauge theory and its infrared

**P24. Flux sectors, vortex free energy, and confinement from centre symmetry ('t Hooft; Tomboulis, Yaffe;
Borgs, Seiler; Chatterjee).**
H: say what confinement is without quarks, and bound the Wilson loop without an expansion. M: twisted
boundary conditions define electric and magnetic flux sectors; their partition functions are related by a
finite Fourier transform; reflection positivity turns the free energy of one flux unit into a bound on the
Wilson loop. Chatterjee: unbroken centre symmetry plus decay of correlations uniform in the boundary
condition implies the area law. O: the twisted partition functions; the "strong mass gap" hypothesis.
C: one idea each. R: G. 't Hooft, Nucl. Phys. B153 (1979) 141-160; E. Tomboulis, L. Yaffe, "Finite
temperature SU(2) lattice gauge theory", CMP 100 (1985) 313-341; C. Borgs, E. Seiler, CMP 91 (1983)
329-380; S. Chatterjee, "A probabilistic mechanism for quark confinement", CMP 385 (2021) 1007-1039.
YM: this is the frame of the lane's own consumer (crux card: the eight-fold and 64-fold twist sums). These
results turn one infrared input into another. None produces the input at weak coupling.

**P25. The small-volume spectrum (Lüscher; Simon), and semiclassics on a twisted torus.**
H: in a small periodic box the quadratic form has flat directions (constant commuting potentials).
M: reduce to quantum mechanics of the constant modes; the non-abelian term Σ|[c_i,c_j]|² confines the
flat valleys quantum-mechanically, so the spectrum is discrete with gap of order g^{2/3}/L. Simon proved
the discreteness for such x²y² potentials. With a centre twist the flat directions are absent and the gap
is π/L at tree level. O: the effective zero-mode Hamiltonian; twist-eating vacua.
C: one idea. R: M. Lüscher, "Some analytic results concerning the mass spectrum of Yang-Mills gauge theories
on a torus", Nucl. Phys. B219 (1983) 233-261; B. Simon, "Some quantum operators with discrete spectrum but
classically continuous spectrum", Ann. Phys. 146 (1983) 209-220; Y. Tanizaki, M. Ünsal, "Center vortex and
confinement in Yang-Mills theory and QCD with anomaly-preserving compactifications", PTEP 2022, 04A108
(physics level, not rigorous).
YM: Lüscher's analysis is not a theorem (the reduction to constant modes is formal). It covers boxes where
the running coupling is small. In the geometry of (PUR-io) the box needs m ℓ of about 12,000. The pattern
that is untried rigorously: keep two directions small and twisted, let the other two be long (S6 below).

**P26. Renormalisation fixed points by certified computation (Lanford; Koch, Wittwer).**
H: a non-perturbative fixed point with no small parameter. M: find an approximate solution numerically;
prove a contraction in a ball around it by interval arithmetic on a Banach space of analytic functions.
O: computer-assisted proof for a functional equation. C: one method.
R: O. Lanford, "A computer-assisted proof of the Feigenbaum conjectures", Bull. Amer. Math. Soc. 6 (1982)
427-434; H. Koch, P. Wittwer, "A non-Gaussian renormalization group fixed point for hierarchical scalar
lattice field theories", CMP 106 (1986) 495-532.
YM: it works when the map acts on a function of one or few variables. A non-hierarchical block-spin map at
coupling of order one acts on functions of infinitely many variables with no small norm.

**P27. Bounds from the Gribov region (Dell'Antonio, Zwanziger).**
H: say anything rigorous about gauge-fixed non-abelian fields at all couplings. M: the minimal Landau gauge
puts every configuration in a convex bounded region where the Faddeev-Popov operator is positive;
positivity alone bounds low-momentum components of the field, for every measure on that region.
O: the fundamental modular region and its ellipsoid bound. C: one idea.
R: G. Dell'Antonio, D. Zwanziger, "Every gauge orbit passes inside the Gribov horizon", CMP 138 (1991)
291-299; D. Zwanziger, "Vanishing of zero-momentum lattice gluon propagator and color confinement",
Nucl. Phys. B364 (1991) 127-161.
YM: this is a rare infrared inequality that holds at every β and is void for U(1) (the abelian
Faddeev-Popov operator is the plain Laplacian, always positive). It does not read the dimension, and it
concerns a gauge-variant quantity. No link to gauge-invariant spectra is proved.

**P28. Irreversibility of the renormalisation flow (Zamolodchikov; Casini, Huerta; Komargodski, Schwimmer;
Casini, Testé, Torroba). Physics-level proofs.**
H: a quantity monotone along the whole flow, through strong coupling. M: positivity (reflection positivity
of the stress-tensor two-point function, or strong subadditivity of entanglement entropy, or unitarity of
dilaton scattering) plus the symmetry of the vacuum gives a differential inequality in the scale.
O: the c-function; the entropic inequality r S″(r) − 3 S′(r) ≤ 0 in d = 4. C: one idea each.
R: A. Zamolodchikov, JETP Lett. 43 (1986) 730; H. Casini, M. Huerta, Phys. Lett. B600 (2004) 142;
Z. Komargodski, A. Schwimmer, JHEP 12 (2011) 099; H. Casini, E. Testé, G. Torroba, Phys. Rev. Lett. 118
(2017) 261602.
YM: this is the only known class of exact inequalities that hold through a crossover with no small
parameter. They need continuum Lorentz invariance. They bound the count of degrees of freedom. They do not
force a gap: a free photon in the infrared satisfies them.

### 2.7 What Part 1 shows (ARGUED)

Every proof above that controls a system far from a perturbative regime uses one of six engines:

- E1 exactness (a solvable recursion, a duality to a positive gas, an infinite symmetry): P4, P6, P19, P21;
- E2 a second small parameter that stays small through the crossover (1/N): P3, P4;
- E3 a sign: a correlation inequality, a monotone or positive representation, a monotone flow quantity:
  P8-P13, P28;
- E4 a finite criterion closed by a certified computation: P14, P26;
- E5 convexity (Bakry-Émery, Brascamp-Lieb), single-scale or along a flow: P18;
- E6 a perturbative start plus stability (cluster expansion, Peierls, quasi-adiabatic): P1, P2, P5, P15.

I know of no rigorous proof of a dynamically generated mass in an asymptotically free bosonic lattice model
that does not use E1, E2 or (for hierarchical models) both. For SU(2) in four dimensions: E2 is void (N = 2).
E6 and E5 stop where the running coupling is of order one. So a new attack must supply a new instance of
E1, E3 or E4. This is the sorting rule for Part 2: each strategy type names its engine.

## 3. Part 2 (closed folder). Nine strategy types and their analogues for (PUR-io)

Written 2026-11-28 from sections 1 and 2 only. Notation: Z_k = partition function of the torus with centre
twist k ∈ Z₂⁶ (one bit per plane, as `twistedPartition`, `Stage0.lean` L97); z_k = Z_k / Z_0;
P_p = ½ tr U_p. Per type: Object, Statement, First estimate, Reading step (the step that reads the
non-abelian structure and the dimension, with the U(1) failure), Death (the likely place it dies).

### 3.0 A sharper control test, used below: (g7) (ARGUED)

The crux card requires failure for weak 4D compact U(1). Part 1 suggests a second control that is closer:
SU(2) lattice gauge theory with an adjoint scalar of fixed length and hopping κ (the lattice Georgi-Glashow
model), in its Coulomb regime (large β, large κ). It has the same gauge group, the same centre symmetry, the
same 64 twisted partition functions and 't Hooft relations, a positive local measure and reflection
positivity. Its infrared limit is expected to contain a massless photon. So:

- (g7) An argument that uses only the group SU(2), the centre twists and their Fourier relations,
  reflection positivity, hypercubic symmetry and positivity of the measure is void: it would also apply in
  the Coulomb regime of the adjoint-scalar model. A valid argument must use something that changes when κ
  grows: either the exact form of the pure-gauge local action, or a quantitative input (the size of the
  running coupling at a named scale).

I label this ARGUED: the existence of the Coulomb regime of that lattice model is standard lore, not a
theorem that I can cite. A second control of the same kind is SU(2) with two massless adjoint Dirac
fermions, believed infrared-conformal from lattice studies (L. Del Debbio, B. Lucini, A. Patella, C. Pica,
A. Rago, Phys. Rev. D 80 (2009) 074507). Consequence used below: types S2, S7 and S8 cannot close without a
quantitative link.

### 3.1 S1. Sharpness in two variables: finite criterion plus a differential inequality (engine E3; P9, P10)

Object. For a fixed torus, y_k(n, β) = −log(1 − z_k(n, β)) (a flux free energy), and x(n, β) = −log p.
Statement wanted. A partial differential inequality in the two variables (log n, β) whose characteristic
direction is the calibrated trajectory: with b = 11/(3π²) the slope of β_K in log(L^K) (`PurIo.lean`,
`coupling_limits_at_offset`),

  (CS≥)  y_k(Ln, β + b log L) ≥ y_k(n, β) − (small, summable in K),

together with growth in n at fixed β from the consumer side (reflection positivity). Then a strong-coupling
start (P5) is carried along the trajectory.
First estimate (PROVED, same computation as (F4)). For every finite torus and twist k,

  log z_k(n, β) = −∫_0^β ΔS_k(n, b) db,   ΔS_k = E_0[Σ_p P_p] − E_k[Σ_p s_p^k P_p],

where s_p^k = −1 on the twist stack and +1 elsewhere, E_k is the twisted Wilson expectation. Proof: both Z_k
and Z_0 are smooth in β, their logarithmic derivatives are the stated means, and z_k = 1 at β = 0.
Conditional lemma (PROVED given the hypothesis). Call (MON-β) the inequality ΔS_k(n, b) ≥ 0 for all n, b.
If (MON-β) holds, then z_k(n, β) is non-increasing in β on every torus. Hence, for cutoffs K < K′ and one
lattice side n, z_k(n, β_K) ≥ z_k(n, β_K′): at a fixed number of lattice sites, the box that is physically
larger has the larger twist ratio. If in addition the limits z_k^phys(ℓ) = lim_K z_k(ℓ L^K, β_K) exist, then
z_k^phys is non-decreasing in ℓ. Proof: β_K < β_K′ and the integral formula; in the limit, compare the pairs
(ℓ L^{K+1}, β_K) and (ℓ L^{K+1}, β_{K+1}), which have physical sides Lℓ and ℓ.
Reading step. (MON-β) itself does not read the group: for Z₂ and U(1) it follows from Griffiths-Ginibre
inequalities. The reading must sit in the constant of (CS≥). In the form ∂_β log y ≥ −2/b at fixed n, the
number b is the one-loop coefficient: it is 0 for U(1), where the inequality would need an infinite rate.
So the non-abelian structure and d = 4 enter as the threshold constant of a differential inequality.
Death. (a) No Griffiths-type inequality is known for SU(2). Reason (PROVED in one line): a function f on
a group is positive definite only if f(g⁻¹) is the complex conjugate of f(g); for the plaquette function
f(U₁,..,U₄) = tr(U₁U₂U₃⁻¹U₄⁻¹) on G⁴, f(g⁻¹) = tr(U₁⁻¹U₂⁻¹U₃U₄), which equals the conjugate
tr(U₄U₃U₂⁻¹U₁⁻¹) for all arguments only when G is abelian. So Ginibre's cone argument has no start.
(MON-β) is in the family of the open question whether Wilson loops are monotone in β. (b) (CS≥) with the
sharp constant b is the classical statement "the lattice string tension is bounded below by the
asymptotic-freedom scaling law". In that form S1 is equivalent to the known formulation of the problem.
Only (MON-β) is a separate, weaker statement.

### 3.2 S2. A monotone flow on the flux simplex (engine E3; P12, P13, P28)

Object. On the symmetric torus of physical side ℓ, the 64 sector weights π_ℓ(e, m) = Z(e; m) / Σ Z, with
Z(e; m) = (1/8) Σ_{k₀ ∈ Z₂³} (−1)^{e·k₀} Z_{(k₀, m)} (temporal twists k₀, spatial twists m). Each Z(e; m) is a
trace of a positive operator on a sector, so π_ℓ is a probability vector. The hypercubic group permutes the
planes, so π_ℓ obeys linear identities that mix e and m.
Statement wanted. A functional Φ on the simplex, strictly monotone along ℓ ↦ π_ℓ unless π_ℓ is one of the
three "gapped" vertices: π(e; m) ∝ δ_{e,0} (confined), ∝ δ_{m,0} (free flux, the small-ℓ end), or
∝ δ_{e,m} (oblique).
First estimates. (i) (PROVED) Pf(k) = k₀₁k₂₃ + k₀₂k₁₃ + k₀₃k₁₂ = k₀·m is a non-degenerate quadratic form on
Z₂⁶ with 36 zeros and 28 ones. Its polar form is ⟨k, j⟩ = Pf(k + j) − Pf(k) − Pf(j). Hence
(1/8) Σ_k (−1)^{Pf(k) + ⟨k,j⟩} = (−1)^{Pf(j)}: the sign (−1)^{Pf} is a fixed vector of the Z₂⁶ Fourier
transform. Proof: Σ_k (−1)^{Pf(k+j)} = 36 − 28 = 8. (ii) (PROVED) The κ-weight of `Stage0.lean` L116 is
(1/8) Σ_k (−1)^{Pf(k)} Z_k = Σ_m Z(e = m; m), a sum of eight non-negative sector traces. Proof: insert
Pf(k) = k₀·m in the definition of Z(e; m). In the language of P16 this is the partition function of the
SO(3) theory with the discrete theta term (O. Aharony, N. Seiberg, Y. Tachikawa, JHEP 08 (2013) 115).
(iii) (ARGUED) Small-ℓ end. For ℓ → 0 on the trajectory, z_k → 0 for every k ≠ 0: twisted sectors with a
twist-eating flat connection have no constant modes and lose a positive power of g(ℓ) against the untwisted
sector, which has four constant-mode moduli; sectors with odd Pf lose exp(−4π²/g²(ℓ)), that is a factor
(Λℓ)^{11/3} at one loop. So π_ℓ starts at the free-flux vertex and must end at the confined vertex.
Reading step. In four dimensions the flux energies of a free Maxwell field on a symmetric torus are
independent of ℓ (flux energy × ℓ is dimensionless only for d = 4). So for U(1) the flow is a fixed point
in the interior and every strictly monotone Φ is contradicted. The power 11/3 reads SU(2) and d = 4.
Death. No monotone Φ is known. By (g7) none can follow from positivity, the Fourier relations and symmetry
alone, because the adjoint-scalar control has the same simplex and a flow that stops in the interior.
A quantitative link is needed at the scale where g(ℓ) is of order one. Without it this type gives only
exclusion statements ("if the neutral sector has a gap, then ..."), which are 't Hooft's.

### 3.3 S3. An exact change of variables to a positive gas or a fibre model (engine E1; P3, P6, P16, P20)

Object. The Z₂ fibre over SO(3). Haar measure is invariant under U_ℓ ↦ σ_ℓ U_ℓ, σ_ℓ = ±1.
First estimate (PROVED). For every torus and twist k,

  Z_k = ∫ dU Z^{Z₂}_k(βP(U)),   Z^{Z₂}_k(J) = 2^{−|E|} Σ_σ exp(Σ_p s_p^k J_p σ_{∂p}),

so z_k = E_ν[ Z^{Z₂}_k(βP) / Z^{Z₂}_0(βP) ] with dν = Z^{Z₂}_0(βP(U)) dU / Z_0. The SU(2) twist ratio is an
average of twist ratios of Z₂ gauge theories with couplings J_p = βP_p(U). Where all J_p can be made
non-negative by a choice of σ, the fibre is a ferromagnetic Z₂ gauge theory; it obeys Griffiths
inequalities and its twist ratio is monotone in each |J_p|.
Statement wanted. A block version: a positive fibre model on a coarse lattice whose couplings are below the
self-dual value ½ log(1 + √2) of the four-dimensional Z₂ gauge theory; then the fibre confines and z_k is
near 1 (the pattern of P12: a threshold known exactly by duality).
Reading step. The fibre exists because the centre is a proper subgroup: for U(1) the same construction with
the full group gives no residual SO(3) field, and the fibre theory is the whole (Villain-type) model, which
deconfines at weak coupling.
Death (ARGUED, immediate). At β_K the fibre couplings are about β_K: the fibre is frozen and
ν-almost surely carries no thin vortex. Blocking the signs on coarse faces gives fibre couplings
β × (number of fine plaquettes in the hinge stack), still larger. The relevant objects are thick vortices of
the SO(3) field (its second Stiefel-Whitney class). They are not the orbit of an exact Z₂ symmetry of Haar
measure, so they have no positive fibre representation. The dual (spin-foam) representation has signed
weights. No auxiliary field is known in which the mass is a saddle (P3).

### 3.4 S4. Convexity on the orbit space (engine E5; P18)

Object. M = SU(2)^E with the product bi-invariant metric, the gauge group 𝒢 = SU(2)^V acting by isometries,
μ ∝ e^{−S} vol with S the Wilson action, L = Δ − ∇S·∇, Γ₂(f) = |Hess f|² + (Ric + Hess S)(∇f, ∇f).
First estimate (PROVED below; the constant 1/(2d) is PROVED, the value 0.37 is a computed number, ARGUED).
Lemma OG (orbit gain). Let f be smooth and gauge invariant. Let K_a be Killing fields of the gauge action
whose values at U form an orthonormal basis of the tangent space of the orbit. Then

  Γ₂(f) ≥ (Ric + Hess S)(∇f, ∇f) + Q_U(∇f),   Q_U(X) = Σ_a |∇_X K_a|².

For a Killing field K_ξ(U)_ℓ = (ξ_x − Ad_{U_ℓ} ξ_y) U_ℓ, ℓ = (x, y): (∇_X K_ξ)_ℓ = −½ [X_ℓ, ξ_x + Ad_{U_ℓ} ξ_y] U_ℓ.
With d_U ξ = (ξ_x − Ad ξ_y)_ℓ, s_U ξ = (ξ_x + Ad ξ_y)_ℓ and Δ_U = d_U* d_U:
Q_U(X) = ¼ Σ_ℓ Σ_b ⟨[X_ℓ, e_b], (s_U Δ_U^{−1} s_U*)_{ℓℓ} [X_ℓ, e_b]⟩ ≥ (1/(2d)) Ric(X, X), since Δ_U ≤ 4d and the
diagonal block of s_U s_U* is 2 (this bound is for U with discrete stabiliser, a set of full measure).
At U = 1 in d = 4 the factor is 2G(0,0) + 2G(0,e) ≈ 0.37 instead of 1/8 (G = lattice Green function).
Proof. For invariant f and a Killing field K: Kf = 0, so for every vector X,
0 = X(Kf) = Hess f(X, K) + ⟨∇_X K, ∇f⟩, and ⟨∇_X K, ∇f⟩ = −⟨∇_{∇f} K, X⟩ because ∇K is antisymmetric. So
Hess f(K, ·) = ⟨∇_{∇f} K, ·⟩. Summing the squares of the rows of Hess f that belong to the orthonormal
vertical vectors K_a(U) gives |Hess f|² ≥ Σ_a |∇_{∇f} K_a|². The formula for ∇_X K_ξ follows from
∇_X R_ξ = −½[X, ξ] for right-invariant fields and ∇_X L_η = +½[X, Ad_U η] for left-invariant fields on a
group with bi-invariant metric. Orthonormality of K_a means ξ_a = Δ_U^{−1/2} e_a, which gives the block
formula. The bound uses Δ_U^{−1} ≥ (4d)^{−1} on the range, and Ric(X, X) = ¼ Σ_ℓ Σ_b |[X_ℓ, e_b]|². ∎
Corollary (PROVED given Lemma OG, by the integrated Bakry-Émery argument ∫(Lf)² = ∫Γ₂(f) on the invariant
subspace): if (1 + 1/(2d)) Ric + Hess S ≥ κ > 0 on horizontal vectors, the Poincaré inequality holds with
constant 1/κ for gauge-invariant functions. This improves the single-scale criterion of Shen-Zhu-Zhu by the
factor 1 + 1/(2d) in the curvature term.
Reading step. For an abelian group Ric = 0 and Q = 0 (the Killing fields are parallel). The gain Q is the
curvature of the orbit space (the O'Neill term); it is the square of a commutator.
Death. The criterion is pointwise in U. At a rough configuration Hess S is as negative as −cβ. So the
corollary holds only for β below a constant: it never reaches the trajectory. A multiscale form needs the
effective action at the scale where g is of order one, which the account does not control.
The dimension is read only through 1/(2d). Not a gate instance.

### 3.5 S5. A finite criterion closed by a certified computation, with an exact carry (engine E4; P14, P26)

Object. The consumer's threshold (purity ≥ 457/625, or the κ-seed below 2^{−18}) as the finite criterion;
an exact block-spin identity as the carry: for a block map that respects the torus and the twists,
Z_k(β_K; n³ × t) = Z_k^{eff}(S_K^{(j)}; (n/L^j)³ × (t/L^j)), with S_K^{(j)} the effective action after j steps.
Statement wanted. A compact, explicitly described set 𝒜 of unit-lattice actions that contains S_K^{(K−K₀)} for
all large K (K₀ fixed), and a certified evaluation of the criterion, uniform over 𝒜, on the box of ℓ L^{K₀} sites.
First estimate. None with a number. The account gives 𝒜 only while the running coupling is below its small
constant; the box then has about exp(c/g²) sites per side.
Reading step. The trajectory β_K and the set 𝒜 read the one-loop coefficient. For U(1) the criterion is
false on 𝒜.
Death (ARGUED). At coupling of order one, 𝒜 is not finitely parametrised and has no small norm. The 2D AKLT
proofs had an exact ground state and a patch of about 30 sites. Here a patch must hold several correlation
lengths of a four-dimensional SU(2) field. A certified integral of that size has no known method. This
type is listed for completeness. It is not a candidate from this row.

### 3.6 S6. Semiclassical start on a twisted thin tube (engines E6 and E1; P1, P2, P6, P25)

Object. The Wilson law at β_K on a torus with two short sides and two long sides, physical sides
ℓ_s × ℓ_s × ℓ₃ × ℓ₀, with one unit of centre twist in the short plane (k₁₂ = 1). The short side ℓ_s is inside
the range where the account has a small running coupling g(ℓ_s). The long sides are arbitrary.
Statement wanted (TT), uniform in K and in ℓ₃, ℓ₀:
 (a) truncated correlations of gauge-invariant local functions decay along the long directions at a rate
     at least c/ℓ_s; the neutral purity of the tube at time t tends to 1 when t/ℓ_s exceeds C log(ℓ₃/ℓ_s);
 (b) the free energy of one unit of electric centre flux along direction 3 is at least σ_t ℓ₃ ℓ₀ with
     σ_t ≥ c ℓ_s^{−2} exp(−C/g²(ℓ_s)) > 0 (a string tension for the tube), and at most the same form with
     the exponent 4π²/g²(ℓ_s).
First estimate (PROVED). Lemma TT1 (twist gap). Let L₁, L₂ ≥ 2 and N₃, N₀ ≥ 1. On the lattice torus
Z_{L₁} × Z_{L₂} × Z_{N₃} × Z_{N₀} take su(2)-valued cochains with the boundary rule
A(x + L₁e₁) = Γ₁ A(x) Γ₁⁻¹, A(x + L₂e₂) = Γ₂ A(x) Γ₂⁻¹, Γ₁ = iσ₁, Γ₂ = iσ₂, periodic in directions 3 and 0.
Then (1) d: C⁰ → C¹ is injective; (2) every 1-cochain with dA = 0 is exact; (3) for every 1-cochain with
d*A = 0: ‖dA‖² ≥ λ_tw ‖A‖², λ_tw = 4 min( sin²(π/(2L₁)), sin²(π/(2L₂)) ), independent of N₃ and N₀.
Proof. Ad(Γ₁) = diag(+,−,−) and Ad(Γ₂) = diag(−,+,−) in the basis σ₁, σ₂, σ₃. So the colour component a has
momenta k₁ ∈ (2π/L₁)(Z + s₁/2), k₂ ∈ (2π/L₂)(Z + s₂/2) with (s₁, s₂) = (0,1), (1,0), (1,1) for a = 1, 2, 3. No
component admits k₁ = k₂ = 0. The boundary rule commutes with lattice shifts, so dd* + d*d acts on each
Fourier mode as k̂² = Σ_μ 4 sin²(k_μ/2) ≥ λ_tw. (1): d*d on C⁰ is ≥ λ_tw. (2) and (3): on C¹,
‖dA‖² + ‖d*A‖² = Σ_k k̂² |Â(k)|² ≥ λ_tw ‖A‖². ∎
Consequence: the configuration U ≡ 1 with this boundary rule is a non-degenerate minimum of the Wilson
action modulo gauge, with Hessian at least c₀ β λ_tw on the gauge-orthogonal complement, uniformly in the
long sides. The only other flat configurations differ by the centre holonomies ±1 in directions 3 and 0.
Chain. Link 1: Lemma TT1 and the list of twisted flat connections (hand or Lean). Link 2: the account on
the tube: effective action at scale ℓ_s, uniform in K, with twist (the exact twist identity of the lane) and
with long sides. Link 3 (P1): the scale-ℓ_s theory on the tube is a two-dimensional system of unit cells,
a massive Gaussian by TT1 plus a small perturbation plus rare large-field cells; a cluster expansion along
the two long directions gives (a). Link 4 (P6): cells that carry half-integer topological charge (twist
k₁₂ = 1 with k₀₃ = 1 has odd Pf) form a dilute gas with positive weights, because they are regions of the
positive Wilson measure; a crude lower bound on their activity gives (b). No existence theorem for a
fractional instanton solution is needed for the lower bound; a trial configuration is enough.
Reading step. (a) is void for U(1): U(1) has no centre twist of this kind, and with integer flux through
the short plane the constant modes of A₃, A₀ and the holonomies around the short sides stay massless. The
twist gap needs Γ₁Γ₂ = −Γ₂Γ₁, a non-commuting pair. Untwisted SU(2) on the same tube has constant modes and
no perturbative gap. (b) reads d = 4: the gas exists because the pair of orthogonal twists has odd
Pfaffian, and its activity exp(−4π²/g²(ℓ_s)) = (Λℓ_s)^{11/3} carries the one-loop coefficient.
(g7), a correction made while writing: the test is NOT passed. With an adjoint scalar in the Coulomb
regime the unbroken direction in colour space is flipped by Ad(Γ₁) or Ad(Γ₂), so the photon is antiperiodic
in a short direction and has the same kinematic gap π/ℓ_s. Statement (a) is therefore true in the control
model too. Statement (b) is also expected there: a two-dimensional effective theory with any positive
vortex activity confines. So (TT) separates SU(2) from U(1), but it does not separate confinement from a
Coulomb phase. It is a statement about thin geometry. It carries no evidence for the gap at large ℓ_s.
Death. (TT) lives at short ℓ_s. The consumer needs clustering of the infinite-volume states, or the seed on
a cube with all sides long. The bridge is "no transition as ℓ_s grows" (adiabatic continuity, Tanizaki and
Ünsal, P25). It has no rigorous form: reflection positivity gives only Z_k ≤ Z_0-type bounds between tubes
of different widths (ARGUED). So S6 can give a gate-type estimate in two long directions. It cannot reach
(PUR-io) without a new monotonicity in ℓ_s.

### 3.7 S7. Variational gluing and localisation (engine E3; P22)

Object. A trial vector for (F3), or a gluing map from two tori of time extent u to one of extent 2u.
First estimate (PROVED, negative). Jensen's inequality for the gluing of two independent periodic copies
A, B at one time cut gives p ≥ exp(−β E[Σ_{x,i} (P^{AA} + P^{BB} − P^{AB} − P^{BA})]), where P^{AB} is the temporal
plaquette built from the copy A below the cut and the copy B above it, after any gauge alignment. The
exponent is of order n³: the two copies have independent ultraviolet fluctuations on every link. So
p ≥ exp(−c n³), which is useless. Purity is an exact cancellation of ultraviolet fluctuations.
Statement wanted. A "Dyson lemma" for gauge fields: an operator inequality T_β^{L^j} ≥ B* T_j^{eff} B between
fine and coarse transfer operators, so that trial vectors can be built at the coarse scale.
Reading step. None at the first link.
Death. The coarse effective law is not a product over time steps, so there is no coarse transfer operator
with a sign. Box localisation fails because the cell energies are not frustration-free. By (g7) no soft
variational argument closes. Not a candidate.

### 3.8 S8. One closed functional equation plus rigidity (engine E1; P19, P21)

Object. The loop equation at one link. For a loop C through the link ℓ once, W_C = ½ tr U_C, integration by
parts with the Laplacian of SU(2) on U_ℓ gives (ARGUED: derivation done once here, constants to recheck)

  (3/4) ⟨W_C⟩ = (β/8) Σ_{p ∋ ℓ} ⟨W_{C∘p⁻¹} − W_{C∘p}⟩,

where 3/4 is the Casimir of the fundamental representation and the SU(2) identity tr A tr B =
tr AB + tr AB⁻¹ removes the product terms for such loops.
Statement wanted. A finite family of quantities closed under these equations, plus a uniqueness theorem.
Reading step. The Casimir and the SU(2) trace identity read the group. The dimension enters only as the
number 2(d − 1) of plaquettes at a link.
Death. The crude bound |⟨W_C⟩| ≤ (β (d − 1)/3) max |⟨W_{C′}⟩| contracts only for β < 3/(d − 1) (the pattern of
Aizenman and Simon, CMP 77 (1980) 137-143, for O(N) spins). The family does not close for loops with
self-intersections. Positivity added to the loop equations is the lattice bootstrap; the crux card assigns
it to other lanes. Not a candidate from this row.

### 3.9 S9. Gauge-fixed positivity carried to a gauge-invariant statement (engines E3, E5; P27)

Object. The minimal Landau or Coulomb gauge. On the Gribov region Ω (where the Faddeev-Popov operator
M(A) = −∂·D(A) is positive) the weight is det M(A) e^{−S(A)}.
First estimate (PROVED in the continuum notation). M(A) is affine in A, and log det is concave on positive
operators. So Ω is convex and W(A) = −log det M(A) is convex on Ω, with
Hess W(a, a) = tr(M⁻¹ M′(a) M⁻¹ M′(a)) ≥ 0, M′(a) = −∂·[a, ·].
Statement wanted. A Brascamp-Lieb bound for a gauge-invariant quantity, from the convex factor W.
Reading step. For U(1), M = −∂² does not depend on A: Ω is the whole space and W is constant. The convexity
is a commutator effect.
Death. S(A) is not convex, and Hess W is smaller than Hess S by a factor g²; in perturbation theory W is
the ghost loop. The bound that exists (Zwanziger's on the zero-momentum propagator) is gauge-variant and
reads no dimension. No theorem links it to the spectrum of the transfer operator. Not a candidate.

### 3.10 Candidates that go to Phase 2

- C1 (S1): the monotonicity (MON-β) of twist ratios in β, with its consequence, monotonicity of the
  continuum twist ratios in the physical size.
- C2 (S2): the flux simplex with its three gapped vertices; the search for a monotone functional; facts
  (i)-(iii), including the reading of the κ-weight as Σ_m Z(e = m; m) and as the SO(3) theory with theta term.
- C3 (S3): the Z₂ fibre identity z_k = E_ν[fibre ratio] and the self-dual threshold of the fibre.
- C4 (S4): Lemma OG (orbit gain in Γ₂) and the improved single-scale Poincaré criterion.
- C5 (S6): the twisted thin tube: Lemma TT1, statement (TT), the four-link chain.
- C6 (3.0): the control test (g7) by the adjoint-scalar model.
- C7 (2.7): the six-engine sorting rule: a new attack must name a new instance of E1, E3 or E4.
- Not candidates (they die at the first link, recorded so that they are not retried): S5, S7, S8, S9.
