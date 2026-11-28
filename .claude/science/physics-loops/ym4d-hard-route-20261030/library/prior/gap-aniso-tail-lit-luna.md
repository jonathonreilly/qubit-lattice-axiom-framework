
## Repo search

The lead's `library/prior/repo-search-2026-11-08.md` searched
`origin/main`, PRs #10114, #10133, #10134 and #10141 for earlier
construction questions. Its anisotropic hits concern different currents,
operators and winding constructions. It does not search this new tail target.
The target's own `gap-newmath-astra62-max3.md` records nearer work: row 1656
and check 1659 study individual masses from an anisotropic endpoint; row 1660
changes a one-slice observation; neither carries the purity sign to the
isotropic point. The closest repo analogue is BR-2's face leg, not an
anisotropic-to-isotropic theorem. `open-registry.md` assigns the carry
integral and the seed-between-two-ends question to `ANISO-TAIL`, owned by row
1661. Row 1664 is its requested literature search, not another proof lane.

# Literature reading: anisotropic tail route

Research note for FINISH row 1664. This is not a proof, computation, audit,
or status change. Checkout: `b31d9c96bcf7e1239c748eb3f2a6cca2affca6af`.
Only this note is a repository output.

## Source retrieval

Fetched once from commit `31a47c543775` into the fresh directory
`/tmp/sa-gap-aniso-tail-lit-luna.0qtNAb/`: `sa_ym4.tex` (32,992 lines) and
`sa_ca_I.tex` (166,711 lines). No paper is stored in this checkout.

## Sussman–Alpoge index check

I searched all `sa-index/chunk-*.md` and the supplied
`sa-index/ca-4.12-4.19/chunk-*.md` for `anisotrop`, `toron`, `Polyakov`,
`winding`, `flat connection`, `Kogut`, `Hamiltonian`, `temporal coupling`,
and `spatial coupling`. The only substantial outline hits are its separate
continuum coordinate-anisotropy discussion, SA 7008–7014; those are not
lattice-coupling comparison results. The CA 4.12–4.19 hits are unrelated
stage/creation-set material. The index does not identify a proof of this
route. I am not treating index search as proof of absence.

Index attribution: the outline and complete account are Ethan Sussman and
Levent Alpoge's project; Claude and Codex authored their text. I used their
index as a locator and do not reproduce or rely on their scientific claims
here.

## Early literature findings

- **Anisotropy/Hamiltonian matching:** Frithjof Karsch, “SU(N) gauge theory
  couplings on asymmetric lattices,” *Nucl. Phys. B* 205 [FS5] (1982),
  285–300. Eqs. (1.1)–(1.6) define separate space/time couplings and
  ξ=a/aτ; the Hamiltonian limit is ξ→∞. The paper computes perturbative
  coupling matching, not a gap or transfer from anisotropic to isotropic
  confinement. Its limit has β_s→0, β_t→∞ at fixed Hamiltonian
  coupling, opposite to the row's β_s=s→∞, β_t=a fixed.
- **Finite-temperature effective Polyakov action:** M. Billó, M. Caselle,
  A. D'Adda, S. Panzeri, “Effective actions for finite temperature Lattice
  Gauge Theories,” *Nucl. Phys. B Proc. Suppl.* 53 (1997), 785–788,
  arXiv:hep-lat/9609027. It constructs an order-by-order β_s expansion,
  exact in β_t; this is the β_s small/zero expansion, not the flat-spatial
  β_s→∞ limit. Their SU(2) example is 4D. The paper formulates a general
  (d+1)-dimensional construction, hence also a formal d=4 spatial (5D)
  specialization, but does not prove the row's 5D selective threshold.
- **Compact U(1):** O. Borisenko, M. Gravina, A. Papa, “Critical behavior of
  the compact 3d U(1) theory in the limit of zero spatial coupling,”
  arXiv:0806.2081 (2008). Its Eqs. (3), (5)–(11) show β_s=0 factorization
  and a two-dimensional XY-like Polyakov-spin model, then it studies that
  model numerically. This is a different spatial dimension and opposite
  coupling endpoint from the row.
- **Torus finite volume:** M. Lüscher, “Some analytic results concerning the
  mass spectrum of Yang-Mills gauge theories on a torus,” *Nucl. Phys. B*
  219 (1983), 233–261. It studies 4D SU(n) periodic small boxes, center
  electric-flux sectors and a weak-coupling expansion; the free nonzero-mode
  spectrum has gap 2π/L (p. 244). Its zero modes/tori do not establish
  Haar-distributed commuting spatial windings in the lattice limit.
- **Flat-moduli measure, related but not the claimed toron law:** Ambar N.
  Sengupta, “The volume measure for flat connections as limit of the
  Yang–Mills measure,” *J. Geom. Phys.* 47 (2003), 398–426. Theorem 1
  (for genus g≥2) identifies the zero-area heat-kernel Yang–Mills limit,
  for conjugation-invariant tests, with symplectic volume on the moduli of
  flat G-connections. This is a genuine flat-moduli limit, but not a 4D
  Wilson-lattice theorem and not product Haar on the three SU(2) winding
  matrices. Keep this distinction explicit.

## 1. Spatial-coupling endpoint, transfer matrix, and spectrum

**Verdict: (b) related results exist, but I found no result that is the
specified β_s=s→∞, β_t=a fixed flat-spatial reduced transfer matrix and its
full spectrum.** At a formal classical level β_s→∞ suppresses every spatial
plaquette with nontrivial holonomy; on a simply connected spatial lattice
this is pure gauge, while on a spatial torus the remaining commuting
holonomies are global zero modes. The sources below do not establish a
probability law for these moduli in the finite-β_t lattice Gibbs measure.

- Karsch, cited above, Eqs. (1.1)–(1.6), gives the standard anisotropic
  coupling/spacing matching and the continuous-time Hamiltonian limit
  ξ→∞. In that scaling β_s→0 and β_t→∞ with a matched Hamiltonian coupling;
  this is the opposite endpoint from the frozen-spatial proposal.
- Kogut and Susskind, “Hamiltonian formulation of Wilson’s lattice gauge
  theories,” *Phys. Rev. D* 11 (1975), 395–408,
  [doi:10.1103/PhysRevD.11.395](https://doi.org/10.1103/PhysRevD.11.395),
  Eq. (6.6), give the electric-Casimir plus magnetic-plaquette Hamiltonian.
  Section VII develops strong-electric-coupling flux-loop perturbation
  theory (the lowest gauge-invariant excitation begins as a plaquette loop).
  This is a perturbative spectrum, not a theorem for a gap uniform in
  volume.
- A rigorous related gap theorem can be obtained in that Hamiltonian
  strong-electric-coupling regime by matching to D. A. Yarotsky, “Ground
  states in relatively bounded quantum perturbations of classical lattice
  systems,” *Commun. Math. Phys.* 261 (2006), 799–819,
  [arXiv:math-ph/0412040](https://arxiv.org/abs/math-ph/0412040), Theorem 1.
  The theorem gives a nondegenerate ground state and a positive volume-
  independent gap for small relatively bounded finite-range perturbations
  of a classical product-ground-state Hamiltonian. The electric KS term
  supplies the linkwise Casimir ground state and gap; the magnetic plaquette
  term is bounded and becomes a small perturbation at sufficiently large
  electric coupling. This is an application of Yarotsky’s hypotheses, not
  the theorem’s named gauge-theory example, and it is the opposite coupling
  direction from β_s→∞ at fixed β_t. It therefore gives no bridge to the
  requested reduced spectrum or to the isotropic point.
- Borgs and Seiler, “Lattice Yang-Mills theory at nonzero temperature and
  the confinement problem,” *Commun. Math. Phys.* 91 (1983), 329–380,
  [doi:10.1007/BF01208780](https://doi.org/10.1007/BF01208780), §II,
  construct the positive transfer operator; their Theorem II.2 treats its
  temporal-continuum limit. Their conclusions concern finite-temperature
  string tensions and critical-coupling bounds, not a spectrum of the
  β_s→∞ flat-holonomy transfer operator.

**Search terms:** `anisotropic lattice gauge theory spatial coupling
infinity flat connections`; `temporal coupling zero`; `Karsch asymmetric
lattices Hamiltonian limit`; `Kogut Susskind strong coupling Hamiltonian
gap theorem`; `Borgs Seiler transfer operator anisotropic lattice`.

## 2. Anisotropic/isotropic comparison and inequalities

**Verdict: (b) there are related finite-temperature inequalities and
Hamiltonian-limit results; I found no theorem transferring a mass gap or
the row’s confinement/purity conclusion from its spatial-strong regime to
the isotropic Wilson point.** A monotonicity statement for a selected
Wilson-loop expectation would not alone imply a spectral mass-gap bound or
the neutral-purity threshold in the row.

- Borgs–Seiler (1983), above, establish inequalities among Wilson,
  Polyakov, and ’t Hooft string tensions, and use the finite-temperature
  gauge/spin-model relation for bounds on critical couplings and a weak-
  coupling nonconfining regime at nonzero temperature in three or more
  spatial dimensions. These are rigorous but not an interpolation theorem
  in β_s at fixed β_t to β_s=β_t, and not a zero-temperature mass-gap
  theorem.
- C. Borgs, “Area law for spatial Wilson loops in high-temperature lattice
  gauge theories,” *Nucl. Phys. B* 261 (1985), 455–460,
  [doi:10.1016/0550-3213(85)90582-6](https://doi.org/10.1016/0550-3213(85)90582-6),
  proves a spatial area law at sufficiently high temperature by cluster
  expansion; its abstract also states the Abelian correlation-inequality
  implication from confinement of the corresponding d-dimensional
  zero-temperature theory to a spatial area law in (d+1) dimensions. This
  does not compare the row’s two anisotropic couplings or carry its gap to
  isotropy. The result remains valid in the temporal-continuum limit.
- Tomboulis and Yaffe, “Finite Temperature SU(2) Lattice Gauge Theory,”
  *Commun. Math. Phys.* 100 (1985), 313–341, prove a high-temperature
  deconfinement/nonconfinement result for finite-temperature SU(2); it is
  a temperature statement, not an anisotropy-to-isotropy implication.
- I did not locate a non-Abelian Ginibre-type inequality that orders the
  relevant SU(2) observables in the two bare couplings, nor a theorem whose
  hypotheses match β_t=a fixed and β_s varying from a large value down to
  a. This is a bounded literature search, not a proof that no such result
  exists.

**Search terms:** `anisotropic Wilson lattice monotonicity beta_s beta_t`;
`SU(2) correlation inequalities anisotropic gauge theory`; `Ginibre
inequality non-Abelian lattice gauge Wilson loops`; `anisotropic to
isotropic mass gap confinement theorem`; `finite temperature SU(2)
Tomboulis Yaffe theorem`.

## 3. Polyakov/winding effective models in large-coupling regimes

**Verdict: (b) effective spin descriptions are published at the opposite
endpoint β_s=0 (and in related high-temperature/strong-coupling expansions).
I found no exact dimensional-reduction theorem for β_s→∞ at fixed β_t that
gives the row’s SU(2), U(1), and five-dimensional threshold comparison.**

- Billó, Caselle, D’Adda, Panzeri, above, derive an effective Polyakov-loop
  action order by order in β_s and exactly in β_t (general (d+1)
  dimensions); the paper works out its first nonzero order for 4D SU(2).
  Its β_s expansion controls β_s small, with β_s=0 as the factorized
  starting point. It neither asserts Haar-distributed winding angles at
  β_s→∞ nor gives a neutral-purity threshold. The citation has arXiv
  identifier `hep-lat/9609027`.
- Borisenko, Gravina, Papa, above, derive the exact β_s=0 compact 3D U(1)
  reduction to a 2D Polyakov-spin/XY-like model (Eqs. (3), (5)–(11)); their
  phase-transition discussion is numerical. It is neither 4D compact U(1)
  nor the β_s→∞ limit.
- For five-dimensional SU(2), F. Knechtli, M. Luz, A. Rago, “On the phase
  structure of five-dimensional SU(2) gauge theories with anisotropic
  couplings,” *Nucl. Phys. B* 856 (2012), 74–95,
  [arXiv:1110.4210](https://arxiv.org/abs/1110.4210), use Monte Carlo with
  anisotropic Wilson couplings. Their static potential in hyperplanes
  orthogonal to the extra dimension hints at dimensional reduction; this
  is explicitly numerical evidence, not a rigorous effective-model or
  threshold theorem. General (d+1)-dimensional formalisms such as Billó et
  al. can be specialized formally to d=4, but that does not prove the
  5D-specific claim.
- Svetitsky and Yaffe, “Critical Behavior at Finite-Temperature
  Confinement Transitions,” *Nucl. Phys. B* 210 (1982), 423–447,
  [doi:10.1016/0550-3213(82)90172-9](https://doi.org/10.1016/0550-3213(82)90172-9),
  give the universality argument relating continuous deconfinement
  transitions to center-symmetry spin models. This is a critical-universality
  correspondence, not an exact reduction at the row’s coupling endpoint.

**Search terms:** `beta_s zero Polyakov loop effective action SU(2)`;
`finite temperature lattice gauge effective action exact beta_t expansion
beta_s`; `compact U(1) zero spatial coupling Polyakov spin model`;
`five-dimensional SU(2) anisotropic couplings dimensional reduction`;
`Svetitsky Yaffe effective spin model theorem`.

## 4. Torons, Haar laws, twists, and small boxes

**Verdict: (b) flat-moduli and toron analyses are extensive, but I found no
statement that the three commuting spatial SU(2) winding matrices in the
4D anisotropic Wilson model become jointly Haar distributed in the claimed
limit.** Haar measure on the original link variables is not by itself a
Haar law on the quotient of mutually commuting torons.

- Lüscher (1983), above, §2, Eqs. (12)–(15), parameterizes constant
  commuting gauge fields by Cartan angles modulo 2π shifts and Weyl
  permutations; these toron variables form a compact moduli region with
  boundary. The weak-coupling finite-volume spectrum is organized around
  these zero modes and center electric-flux sectors. The free nonzero-mode
  gap 2π/L is a finite-box perturbative statement, not a uniform
  infinite-volume Yang–Mills mass gap or a Haar law on torons.
- P. van Baal, “Gauge theory in a finite volume,” *Acta Phys. Pol. B* 20
  (1989), 295–312 (review), Eq. (5) and Eqs. (7)–(8), describes the vacuum
  valley of constant commuting fields as a quotient/orbifold by large gauge
  shifts and Weyl transformations and discusses the induced quantum
  mechanics of zero modes. It does not identify that quotient measure with
  product Haar on SU(2)^3.
- ’t Hooft, “Some twisted self-dual solutions for the Yang-Mills equations
  on a hypertorus,” *Commun. Math. Phys.* 81 (1981), 267–275,
  [doi:10.1007/BF01208900](https://doi.org/10.1007/BF01208900), studies
  twisted bundle boundary conditions and self-dual solutions. Twists change
  global sectors and can remove constant commuting zero modes in selected
  finite-volume setups; this is not a distribution theorem for untwisted
  torons. Lüscher’s central-sector discussion cites the related ’t Hooft
  electric-flux construction.
- Sengupta (2003), above, is the closest precise measure result found:
  Theorem 1 gives the 2D zero-area Yang–Mills limit as symplectic volume on
  flat-connection moduli for genus at least two. This is a quotient-moduli
  measure in 2D, not 4D lattice product Haar.

**Search terms:** `toron Haar measure lattice Yang Mills`; `van Baal finite
volume flat connections toron measure`; `Luscher 1983 toron equations 12
15`; `'t Hooft twisted boundary conditions hypertorus zero modes`; `flat
connections volume measure Yang Mills limit Sengupta theorem`; `constant
commuting SU(2) holonomies product Haar`.

## Scope and limits

The four requested targets are not reported as proven absent from all
literature. The verdicts describe the sources and searches above. In
particular, endpoint conventions matter: the established Polyakov-spin
expansions start at small/zero spatial plaquette coupling, while the row’s
flatness heuristic uses large spatial plaquette coupling; the usual
Hamiltonian limit also sends the spatial plaquette coupling to zero while
rescaling the temporal coupling. Neither family supplies the claimed
large-s-to-isotropic carry. The exact computation/Lean owner rule is
recorded in GOAL.md but no computation was run or proof written in this
literature-only task. No Sussman–Alpoge scientific text is quoted.
