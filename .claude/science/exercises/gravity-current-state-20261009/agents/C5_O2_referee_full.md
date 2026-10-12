# VERDICT: CONFIRMED WITH CORRECTIONS

The exact bounded mathematics is mostly sound: the soft-residue argument, the
low-momentum scaling, the band-bottom fall law, Lemma S, the one-dimensional
GNVW obstruction, and the Reeh--Schlieder application all have valid cores.
The report nevertheless overstates several scopes.  In particular, Spohn does
not prove a no-go for all interacting lattice matter; MICROSCOPE compares two
test-body compositions rather than measuring a common beta for every species;
"exact or tuned" is a naturalness dichotomy rather than a theorem from finite
precision; Lemma G is not an infinite-transverse-volume Z^3 theorem; and the
candidate list and prices are not exhaustive or uniquely forced.

Both worker scripts rerun byte-for-byte against their stored outputs.  A
separate analytic/asymptotic and arithmetic check is in
`o2_referee_checks.py:1-95` and `o2_referee_checks.out:1-13`.

## 1. Weinberg, Lemma W, and the time/space split

- **Weinberg's soft theorem is correctly restated, with two qualifications.**
  The gauge variation of the leading spin-2 soft factor is indeed
  `2 xi . V`, where `V = sum eta_i kappa_i p_i`; requiring decoupling for all
  admissible soft null directions makes `V=0` (`O2_report.md:55-67`).  Equality
  of all `kappa_i` follows only within sectors connected by nonzero scattering
  amplitudes; disconnected superselection sectors are not related merely by
  momentum conservation.  This is consistent with Weinberg's original
  S-matrix statement.  [Weinberg 1964](https://journals.aps.org/pr/abstract/10.1103/PhysRev.135.B1049)
- **Weinberg--Witten is a separate theorem, not literally a corollary of the
  soft theorem.**  A Lorentz-covariant conserved stress tensor whose charge is
  the four-momentum is incompatible with a massless helicity greater than one,
  whether the excitation is elementary or composite.  Gravity evades the
  premise because no gauge-invariant local gravitational stress tensor has the
  required Lorentz-covariant status.  The escape list at
  `O2_report.md:69-70` is directionally right, but “elementary” is not itself
  what the theorem concludes.  [Weinberg--Witten 1980](https://www.sciencedirect.com/science/article/pii/0370269380902129)
- **Lemma W's load-bearing implication is correct only after promoting its
  Ward-residue form to an explicit hypothesis.**  If the external pole and
  vertex obey
  `q_mu V^{mu nu} = Delta D^{-1} Q^nu + O(q)`, cancellation of the pole gives
  `xi_nu sum eta_i Q^nu(k_i)`, so exact decoupling makes `Q` additive on the
  support of every nonzero amplitude (`O2_report.md:74-86`).  Continuity of the
  vertex and observational absence of extra polarizations do not by themselves
  derive that exact Ward--Takahashi identity; Cassini and a graviton-mass bound
  are finite bounds, not exact gauge redundancy.
- **The time component is conditional, not automatic.**  Exact time
  translation makes energy an additive invariant, but `Q^0=E` additionally
  identifies the soft vertex with the time-translation energy current.  Given
  that identification, the time statement at `O2_report.md:88-89` is correct,
  again sector by sector.
- **The spatial no-go is overstated.**  Spohn proves that an integrable periodic
  collision invariant is `a omega+c` for a single-band, four-phonon collision
  equation in `d>=2`, under regularity and nondegenerate-Hessian assumptions;
  it is not a theorem about every interacting lattice theory.  The supplied RS
  referee is likewise explicitly bounded to perturbative staggered QED with a
  taste-universal slope (`RS_S2_referee.md:18-21`), while RG leaves singular,
  network, and matrix-band loopholes (`RG_G3_referee.md:5,15-17`).  Therefore
  `O2_report.md:91-99` and the class-wide conclusion at
  `O2_report.md:168-172` must be narrowed to the cited collision classes.
  [Spohn 2006](https://arxiv.org/html/math-ph/0605069)

**Finding:** the additive-collision-invariant core is DERIVED conditional on
the exact Ward-residue hypothesis.  `Q^0=E` is DERIVED conditional on the
energy-current identification.  Failure of a regular spatial vector charge is
DERIVED only in the cited bounded model classes and is not a general
`d>=2` lattice-matter theorem.

## 2. The tree-level REFUTED claim

- The worker output reproduces (`o2_soft_ward_defect.out:1-24`).  Independently,
  `sin k = k-k^{\odot3}/6+O(k^5)` and exact linear-momentum conservation make
  the charge defect `D=O(kappa^3)`, hence `D/kappa=O(kappa^2)`.  A deterministic
  elastic configuration gives coefficient `0.05478`, independently of the
  worker's random solver (`o2_referee_checks.out:1`).
- For `p=0.25 GeV` and `a^{-1}=1.22e19 GeV`, `(pa)^2=4.199e-40`, not
  `2e-41` by itself.  The worker's median coefficient is about `0.0574`, which
  gives `2.41e-41`; its resampled table gives `2.2e-41`
  (`o2_soft_ward_defect.py:57-64`, `o2_referee_checks.out:2-3`).  Thus the
  reported relative-defect number is right at the stated one-significant-digit
  level, but it is a sampled typical coefficient, not a universal bound.
- The valid scope is nearest-neighbour scalar KG, low-energy, non-umklapp,
  on-shell `2->2` kinematics, with the chosen charge `Q=sin k`.  The umklapp
  example is correctly order one (`o2_soft_ward_defect.py:66-80`).  The script
  does not construct a consistent lattice massless spin-2 theory, calculate a
  MICROSCOPE observable, or prove that all tree-level soft/EP tests pass.
  Accordingly `O2_report.md:114-116` is too broad.

**Finding:** REFUTED is correct for the narrow assertion that present finite
precision, through this low-energy tree-level Ward defect, forces the defect to
vanish exactly.  It is not a counterexample to exact Ward identities required
for a fully consistent two-polarization massless spin-2 theory.

## 3. Lemma F, composition bounds, and the 3.5e-5 number

- For the supplied projected Hamiltonian `H=(1+Phi(x))E_B(k)`, Hamilton's
  equations give
  `dot x_i=(1+Phi)E_i`, `dot k_j=-E Phi_j`, and therefore
  `ddot x_i=-(1+Phi)(E E_ij-E_i E_j)Phi_j`.  At a stationary band bottom,
  `E_i=0`, so to first order in the weak field and in the local frame
  `Phi=0`,
  `ddot x_i=-[Hess(E^2/2)]_ij Phi_j`.  The formula at
  `O2_report.md:120-126` is therefore correct at the band bottom and to leading
  weak-field order, not “exact semiclassically” at arbitrary `k` and `Phi`.
  It also assumes an isolated adiabatic band, a narrow wavepacket, a potential
  varying slowly compared with the packet/composite, and no load-bearing
  multiband or Berry correction.
- “The rest energy cancels” is misleading.  The coefficient is
  `beta=E_B(0) Hess E_B(0)`, i.e. rest/gravitational energy divided by inertial
  curvature mass.  It becomes independent of `E_0` in the toy bands only
  because `E^2=E_0^2+beta*2 sum(1-cos k)` hard-codes that relation
  (`o2_ep_beta.py:14-19`).  The leapfrog output is correct but is a consistency
  check of that chosen dispersion, not an independent derivation
  (`o2_ep_beta.out:1-4`).
- Within this model MICROSCOPE constrains `beta_Ti-beta_Pt`; it does not by
  itself measure one common beta for all elementary species and composites.
  The latter requires one-channel-at-a-time/no-cancellation assumptions.
  The actual mission used Pt--Rh and Ti--Al--V alloys, whereas the report
  explicitly uses pure-isotope proxies (`O2_report.md:135-143`).  The quoted
  MICROSCOPE central value and errors are correct.
  [MICROSCOPE final result](https://doi.org/10.1103/PhysRevLett.129.121102)
- The harmonic sector formula
  `beta_B^{-1}=sum_s f_s/beta_s` follows if sector rest energies and inertial
  masses add and all sectors co-move.  Binding-energy signs, virial response,
  interaction energy, and actual alloy composition are not derived.  The
  `SUGGESTED` label at `O2_report.md:135` is therefore essential.
- The arithmetic is correct under those proxies: the four one-channel bounds
  are `3.44e-12`, `5.94e-12`, `2.19e-10`, and `1.20e-13`
  (`o2_referee_checks.out:4-8`).  With the further reading
  `delta beta/beta=2(c_e-c_gamma)=0.0171` and with the electron--photon result
  used as a photon--bulk-matter split, `eta=0.0171*0.0020326=3.476e-5`, an
  excess `4.97e9` over `7e-15` (`o2_referee_checks.out:9`).  The number is
  right; the physical identification is not derived (`O2_report.md:144-146`).

**Finding:** Lemma F is DERIVED only as a leading weak-field, stationary-band,
semiclassical tensor law under the supplied energy coupling.  The universal-
all-species reading, sector decomposition, per-channel limits, and QED
translation remain SUGGESTED.  The arithmetic, including `3.5e-5`, is correct.

## 4. Lemma S

- The spectral-halving step is correct.  Exact covariance makes all `2^d`
  half-cells unitarily equivalent, so a nonzero cell spectral subspace cannot
  have finite dimension (`O2_report.md:180-182`).
- The box constant at `O2_report.md:183-184` is correct only if the omitted
  definition is
  `box_B={-B,-B+1,...,B+1}^d`, the integer box centered at `1/2`.  It then has
  rank `n(2B+2)^d`, and the nearest outside site is distance `B+3/2` from
  `1/2` (`o2_referee_checks.out:10-12`).  For the conventional symmetric box
  `[-B,B]^d`, the displayed lower bound would instead be `B+1/2`.  With the
  centered definition inserted, the finite-rank projection is injective and
  the contradiction is valid.
- “Site-bounded” is a sufficient and physically clear hypothesis: each
  coordinate difference `X^j-N^j` has a bounded operator extension.  It is not
  a consequence of finite `n`.  Since all infinite separable Hilbert spaces
  are abstractly isomorphic, one can transport the usual `L^2(R^d)` position
  and momentum pair to `l^2(Z^d) tensor C^n`; then `X-N` is necessarily
  unbounded and the continuous action is violently nonlocal relative to the
  sites.  Such an operator escapes the theorem.  To exclude weaker notions of
  geometric/quasi-local position would require an additional localization
  theorem.
- The no-go withstands the five natural attacks only by keeping its scope
  explicit: infinite fibre, unbounded site displacement, POVM/noncommuting
  coordinates, merely discrete translations, and composite infinite relative
  coordinates all leave its domain.  Its relation to the C3 face delta at
  `O2_report.md:191` is an analogy, not a derivation of C3.

**Finding:** DERIVED after defining the centered box.  It is a sharp no-go for
finite fibre plus exact Weyl translations plus uniformly site-tied commuting
position, not for arbitrary unbounded or non-geometric position operators.

## 5. Lemma G

- The one-dimensional argument is correct.  For `a in [0,1]`, every `alpha_a`
  is a nearest-neighbour QCA with one uniform range.  Point-norm (“strong” in
  C*-dynamics terminology) continuity gives the continuous QCA path required
  by GNVW, whose index is constant on connected components
  (`O2_report.md:195-200`).  [GNVW](https://arxiv.org/abs/0910.3675)
- At `a=1`, the support inclusion and the corresponding inclusion for
  `alpha_{-1}` give equality with the translated interval algebra.  Thus
  `V=T^{-1}alpha_1` preserves every single-site algebra and is on-site, so its
  index is one.  Multiplicativity then makes `ind(alpha_1)=ind(T)`, equal to
  `2` or `1/2` depending on shift convention, never one.  The contradiction is
  sound.
- A finite transverse `L x L` torus can be grouped into a one-dimensional
  chain of supersites of dimension `2^(L^2)`; the shift index is that number
  or its reciprocal (`o2_referee_checks.out:13`).  This does **not** prove the
  infinite-transverse-volume Z^3 statement.  The earlier N1 referee explicitly
  left the required dimension-uniform higher-dimensional index lemma open
  (`C4_N1_referee.md:26-30`).
- It closes the I1 commutant loophole only under the new strict geometric
  isotony assumption, because that assumption forces the residual `V` to be
  on-site.  It does not close quasi-local flows with tails, an action confined
  to an asymptotic sector, an action with unbounded intermediate range, the
  infinite-transverse limit, or the non-geometric index-carrying symmetry that
  `O2_report.md:204` correctly leaves open.

**Finding:** DERIVED conditional on GNVW in one dimension and on finitely thick
cylinders.  “Closes the I1 loophole” is correct only for the strictly geometric
subclass; it is not the missing general d>=2 result.

### No-go discipline gate for Lemmas S and G

- **N1, alternative routes.**  Five materially distinct attacks on Lemma S
  were checked: an infinite cell fibre, unbounded `X-N`, a POVM or
  noncommuting coordinate, only discrete/approximate Weyl covariance, and a
  composite with infinitely many relative-coordinate states.  Each is a real
  escape but violates an explicit hypothesis, so none falsifies the scoped
  theorem.  Five attacks on Lemma G were also checked: a non-geometric
  asymptotic-sector action, a quasi-local flow with tails, unbounded
  intermediate range, a discontinuous interpolation, and infinite transverse
  volume.  Again these escape the stated 1D/finitely-thick theorem; the last is
  precisely why the broad Z3 extrapolation is not approved.
- **N2, independence.**  No inflated count of independent walls is used.  For
  S, finite fibre, uniform site-boundedness, commuting sharp position, and
  exact continuous covariance are separate hypotheses.  For G, finite local
  dimension, strict uniform locality, point-norm continuity, and the one-site
  shift endpoint are separate hypotheses.  Removing any one can change the
  problem, but no non-implication theorem beyond the explicit counter-routes
  above is claimed.
- **N3, hidden hypotheses.**  “Geometric” means the displayed bounded-site or
  strict-isotony condition; it is not a synonym for all intuitive notions of
  locality.  The finite-transverse-torus restriction is load-bearing and is
  promoted explicitly above.  “On-site” in Lemma G follows from preservation
  of every single-site matrix algebra rather than being assumed.
- **N4, residual matching.**  The I1 commutant residual matches Lemma G only
  after strict geometric isotony forces `V` on-site.  C3's face delta is a
  related canonical-commutator residual, not the residual proved by Lemma S;
  it is therefore treated only as analogy (`O2_report.md:191-204`).
- **N5, resolution/rhetoric.**  Lemma S is one-particle; Lemma G is a 1D
  many-body theorem and a finite-cylinder corollary; Reeh--Schlieder is a
  relativistic-net theorem.  None individually establishes an unrestricted
  microscopic Z3 no-go.  The report's broader “no finite-information-per-cell
  substrate” language is narrowed accordingly.
- **N6, partial closure.**  The theorems do not imply that a new axiom is the
  only exit.  Non-geometric actions, unbounded site displacement, quasi-local
  flows, continuum reformulations, or explicit tuning are different routes;
  Pi-A--Pi-E are prices, not ratified necessities.
- **N7, steelman.**  A continuous action can be transported abstractly from
  `L^2(R^d)` to the lattice Hilbert space with unbounded `X-N`, and a
  many-body fractional translation could conceivably be quasi-local rather
  than strictly locality-preserving.  These are convincing attacks on the
  broad substrate claim but not on S or G as formally stated.  Hence the
  scoped no-gos pass and the broad claim is demoted.
- **N8, cross-cycle echo.**  The supplied I1 referee already warned that an
  index-carrying commutant symmetry survives (`C4_I1_referee.md:15`), and the
  N1 referee left the dimension-uniform d>=2 tube lemma open
  (`C4_N1_referee.md:26-30`).  Lemma G retires the first issue only under
  strict isotony and does not retire the second.  No broader closure is
  inherited from those earlier cycles.

**Gate result:** PASS for Lemma S in its stated site-bounded domain and for
Lemma G in 1D/finitely thick cylinders; FAIL for the unrestricted Z3 or
all-geometric-positions extrapolations.

## 6. Reeh--Schlieder

- The standard application is valid for a local relativistic net with a
  translation-invariant vacuum, the positive-energy spectrum condition, and
  weak additivity/global cyclicity (the report's irreducibility condition is a
  sufficient route).  The vacuum is then cyclic for each nonempty local
  algebra (`O2_report.md:206-210`).  In a nontrivial infinite-dimensional
  vacuum representation, a finite-dimensional local algebra cannot have a
  dense orbit, so local algebras are infinite-dimensional.
  [Fewster--Rejzner AQFT review](https://arxiv.org/abs/1904.04051)
- Exact Lorentz covariance alone does not supply the spectrum condition;
  positive energy is also needed.  Moreover Reeh--Schlieder alone does not
  prove that the algebras are type III.  The type-III claim at
  `O2_report.md:235-239` requires additional standard AQFT hypotheses and must
  not be attributed to Lemma RS.
- The theorem excludes finite-dimensional bounded-region algebras under these
  AQFT assumptions.  It does not exclude a finite number of states below a
  finite energy, nor does it cover nonlocal/minimal-length nets after the
  spectrum or locality assumptions are dropped.

**Finding:** DERIVED with the positive-energy-vacuum and weak-additivity scope;
the stronger automatic type-III and no-spectrum extrapolations are not derived.

## 7. Candidate table and prices

- The table is a useful map of the named options, but “yes, two” means only two
  rows in this non-exhaustive table are marked untested (`O2_report.md:214-231`).
  The asymptotic-sector qubit-grid row is itself only partly tested, and the
  table cannot exclude other dynamical, relational, noncommutative, holographic,
  or quasi-local constructions.  Snyder's translation law and soccer-ball
  estimate are correctly marked SUGGESTED/model-dependent.  Relativistic flash
  models are legitimate covariant-in-law candidates, but their gravity,
  energy-conservation, and record bridges remain open rather than established.
- **Pi-A** is a sufficient escape from lattice-specific obstructions, not a
  uniquely forced minimal change.  The no-gos still allow non-geometric
  asymptotic translations and Lemma S allows unbounded site displacement
  (`O2_report.md:247-250`).  Saying continuum replacement “removes” prior walls
  should mean that their lattice hypotheses no longer apply, not that a UV
  completion has been constructed.
- **Pi-B conflates levels.**  A finite `M_2(C)` fibre at each continuum point,
  an infinite-dimensional bounded-region algebra, and an infinite per-cell Zak
  fibre are related representations but are not the same axiom statement.
  Reeh--Schlieder forces infinite-dimensional region algebras, not an
  infinite-dimensional point fibre; the current Qubit axiom is explicitly
  per-site `M_2(C)` (`MINIMAL_AXIOMS_2026-06-29.md:43-53`).  Nor does Lemma G
  force this in full Z^3 (`O2_report.md:250`).
- **Pi-C** is the natural continuum replacement for the nearest-neighbour rule.
  **Pi-D** is a proposed downstream formation/content rule, not wholly an axiom
  consequence: formation site/rate and physical-observable bridges are outside
  the four axioms (`MINIMAL_AXIOMS_2026-06-29.md:85-95,173-190`).  **Pi-E** is a
  consequence only if the continuum construction supplies no other UV
  regulator (`O2_report.md:251-253`).
- **P0-prime** correctly carries the old shear and speed costs from the price
  note (`PRICE_NOTE.md:354-368`), but its beta summary at
  `O2_report.md:254` omits the weaker `2.2e-10` electron-channel proxy and must
  say that all beta bounds are one-channel-at-a-time, composition-model
  estimates.  The claim that the stricter O1 bounds subsume them is a
  naturalness reading, not an extra theorem.

**Finding:** the table and Pi-A--Pi-E/P0-prime are acceptable as SUGGESTED
design prices after these corrections; they are neither exhaustive nor forced
as a unique minimum.

## 8. Evidence labels

| Claim and source | Referee label |
|---|---|
| Weinberg soft theorem, `O2_report.md:55-70` | **DERIVED (standard), conditional on its S-matrix hypotheses;** universality is sectorwise.  Weinberg--Witten is a separate standard theorem. |
| Lemma W residue implication, `O2_report.md:72-86` | **DERIVED conditional** on the exact Ward-residue identity. |
| `Q^0=E`, `O2_report.md:88-89` | **DERIVED conditional** on identifying the vertex charge with Noether energy. |
| Class-wide spatial contradiction, `O2_report.md:91-99,168-172` | **Not DERIVED as written; DERIVED only for cited bounded classes, otherwise SUGGESTED/open.** |
| Tree-level precision necessity, `O2_report.md:101-116` | **REFUTED only in the stated low-energy nearest-neighbour KG proxy scope.** |
| Lemma F, `O2_report.md:118-134` | **DERIVED conditional** at a stationary isolated band bottom, leading weak-field/semiclassical order. |
| Per-channel beta bounds and QED split, `O2_report.md:135-146` | **SUGGESTED; arithmetic confirmed.** |
| “Exact Ward identity/structural cancellation or tuning” is observationally necessary, `O2_report.md:148-156,171` | **SUGGESTED naturalness, not DERIVED.**  The packet itself lists non-gauge mechanisms and naturalness qualifications at `PRICE_NOTE.md:113-148`. |
| Local stress is necessary, `O2_report.md:162` | **REFUTED as a logical consequence of W1--W5;** the cited SLAC construction is a bounded nonlocal witness. |
| TDiff/unimodular soft row, `O2_report.md:163` | **DERIVED conditional** on exact transverse gauge redundancy and a q-independent hard `V`; the gradient-current statement is the allowed longitudinal residual. |
| Conservation only in law, `O2_report.md:164` | **REFUTED only in the cited bounded event models, not universally.** |
| Snyder/deformed composition, `O2_report.md:166` | **SUGGESTED**, correctly. |
| Lemma S, `O2_report.md:176-191` | **DERIVED in its site-bounded finite-fibre domain** after defining the box. |
| Lemma G, `O2_report.md:193-204` | **DERIVED conditional on GNVW in 1D/finitely thick cylinders;** not full Z^3. |
| Reeh--Schlieder, `O2_report.md:206-212` | **DERIVED under standard AQFT positive-energy assumptions;** type III and the no-spectrum extension are not derived. |
| Minimal rule and candidate/prices, `O2_report.md:214-254` | **SUGGESTED**, but “two untested,” “minimal,” and “each leg derived” are too strong. |
| Final campaign summary, `O2_report.md:258-265` | **Needs narrowing:** asymptotic additive charge and the three bounded no-gos are derived under their separate hypotheses; the universal exactness/minimal-continuum conclusion is SUGGESTED. |

## Strongest correct statement

Assuming an exact two-polarization soft spin-2 gauge redundancy and the stated external-pole Ward identity, its residue defines a charge that must add in every nonzero scattering channel; continuous time can identify its time component with conserved energy, while regular real-valued spatial invariants are excluded only in the specified single-band or taste-universal umklapp collision classes, not in every interacting lattice theory.  For nearest-neighbour scalar KG at low non-umklapp momentum, the relative spatial defect is `C(pa)^2` with a typical `C about 0.05`, giving about `2e-41` at `0.25 GeV`, so finite tree-level precision cannot force exact zero.  Under the supplied slowly varying energy coupling, an isolated narrow wavepacket at a stationary band minimum falls with acceleration `-beta_B grad Phi` to leading weak-field order, where `beta_B=Hess(E_B^2/2)`; MICROSCOPE constrains the difference of the two test bodies' effective beta tensors, and the reported one-channel bounds and `3.5e-5` QED proxy are arithmetically correct but model-dependent.  Exact continuous geometric translation is rigorously incompatible with a finite site fibre when position stays uniformly tied to the sites (Lemma S), and with a strictly local continuous interpolation of the one-site shift on a qubit chain or finite-thickness cylinder (Lemma G); a positive-energy relativistic local net also has infinite-dimensional bounded-region algebras by Reeh--Schlieder.  These results do not exclude unbounded/non-geometric positions, quasi-local or asymptotic-sector actions, the infinite-transverse many-body case, or other exact-cancellation mechanisms, and therefore support--but do not uniquely derive--the proposed continuum/record rule and its prices.
