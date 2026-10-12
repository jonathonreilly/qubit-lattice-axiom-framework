# R5-1 independent referee report

## VERDICT: CONFIRMED WITH CORRECTIONS

The worker has a valid, nontrivial bounded FAIL under the fixed reading, most cleanly from Lemma K plus Theorem W for finite-dimensional families supported on points, spacelike lines, or spacelike planes. The open finite-stabilizer link-cell class does not force INCONCLUSIVE because the fixed FAIL criterion expressly permits a no-go "in a stated class" (`TESTS.md:2870-2873`). The claimed union of classes must nevertheless be narrowed: Theorem Q proves condition-independence for retarded continuous kernels but does not by itself make an arbitrary retarded joint law a product, and its application to the actual Admissibility axiom needs an additional bridge from the axiom's `Z^3` nearest-neighbor/cubic setting to `L_7` events with full Gamma covariance. Proposition L is valid only with its extra `(SC_m)` assumption. Example D is a sound continuum-field escape indexed by lattice links, not an LRL-generated law.

## 1. Lemma K and the explicit loxodromic

**Confirmed.** For a rational span `W`, anisotropy of `Q_7` makes `W` nondegenerate. The pointwise stabilizer is the arithmetic subgroup acting on `W^perp`. It is infinite for spacelike `dim W = 0,1,2` and finite when `W` is Lorentzian or is a spacelike 3-plane, exactly as claimed in `R5-1_report.md:101-108`. The spacelike-plane case uses the infinite unit group of an indefinite anisotropic rational binary form; the spacelike-line case uses the cocompact arithmetic lattice in `SO(1,2)`.

The supplied off-axis construction is also exact (`scripts/r51_stab_offaxis.py:17-25`; `scripts/r51_stab_offaxis.out:1-2`). Independently multiplying the displayed basis change gives

```text
M = [[ 64, -21, 12, 0],
     [147, -48, 28, 0],
     [ 84, -28, 15, 0],
     [  0,   0,  0, 1]],
charpoly(M) = (t-1)^2 (t^2-30t+1).
```

Thus `M^T Q_7 M = Q_7`, `det M = 1`, `M_00 > 0`, and it fixes both `(1,3,0,0)` and `e_3`. Its eigenvalues include `15 +/- 4 sqrt(14)`, so it is loxodromic and has infinite order. The BFS counts reproduce exactly, but are illustrative rather than proofs (`scripts/r51_stabilizers.out:1-10`).

## 2. Theorem W(i)-(iii)

### (i) Mass-shell component

**Confirmed, with one omitted justification easily repaired.** The invariant finite measure `nu_V` and the invariant sigma-finite shell measure `lambda = pi_* Omega_m` have an invariant absolutely continuous component (`R5-1_report.md:119-129`). If `nu_ac = h lambda`, then

```text
pi_*[(h o pi) Omega_m] = h lambda,
```

so the pulled-back measure is finite and invariant. This change of variables is correct and does not require injectivity of `pi`. Sigma-finiteness of `lambda`, asserted at `R5-1_report.md:126` but not proved there, follows because distinct shell lifts meet only on the countable union of codimension-one shell sections; hence `pi` is injective off an `Omega_m`-null set, as proved for the massive shell in `R4-2_report_unrefereed.md:190-205` (and the same argument works on the punctured null cone).

The cyclic loxodromic action is proper on `H_m^+`. It is also proper on the punctured null cone; excluding the two null eigenrays at `R5-1_report.md:128` is unnecessary because the loxodromic scales nonzero vectors on those rays. A proper infinite cyclic action with no finite orbit admits no nonzero finite invariant measure. Therefore the claimed shell-a.c. component vanishes.

### (ii) Haar-a.c. correlations

**Confirmed with a wording limit.** After bounded spectral truncation, the entries of the density matrix span a finite-dimensional invariant subspace of `L^2(T^4)` (`R5-1_report.md:130-134`). If `E` is such a subspace and

```text
m(a) = sup_{f in E, ||f|| <= 1} |f_hat(a)|^2,
```

then `m` is orbit-constant and `sum_a m(a) = dim E`. Hence it vanishes on every infinite Delta-orbit. Passing from the truncations to the original `L^1` density preserves each Fourier coefficient. A finite-orbit lattice displacement is fixed by a finite-index subgroup, which contains a loxodromic; its fixed space lies in that loxodromic's spacelike transverse plane. For `Delta = Gamma_S`, Zariski density makes the common fixed space exactly `W`, so the allowed lattice displacements are `W intersect L_7`.

The correction is semantic but important: only the **Haar-absolutely-continuous part** of the correlations is confined. The singular part is not controlled by W(ii). The broad prose at `R5-1_report.md:45` should retain the qualifier present in the theorem statement at `R5-1_report.md:121`.

### (iii) Covariant charge

**Confirmed under the stated `(Dec/C)` and spectrum hypotheses.** Conservativity of each loxodromic on the finite invariant measure `nu_V` makes the recurrence argument at `R5-1_report.md:135-137` valid. For the expanding and contracting null eigenvectors `e_+` and `e_-`, covariance gives exponential rescaling of the fibre seminorm; recurrence forces both contractions to vanish. Thus the charge lies in the spacelike plane transverse to that loxodromic's Lorentzian axis. A joint spectrum in the closed future cone intersects this spacelike plane only at zero, so `(SC)` forces the charge to vanish on `V`. One loxodromic already suffices for the last implication; using all loxodromics gives the stronger annihilation statement.

## 3. Theorem Q

### Neumann step

**Confirmed.** For every nonzero `x in L_7`, the orbit `Gamma x` is infinite, so `[Gamma:Gamma_x]` is infinite. For finite `F,F'`, each collision set `{gamma: gamma x = y}` is either empty or one coset of `Gamma_x`. B. H. Neumann's lemma therefore supplies a `gamma` with `gamma F'` disjoint from `F`. This validates `R5-1_report.md:154-158`, including on the invariant past cone.

### Conclusion and retarded rules

**Partly corrected.** Uniform continuity, the Neumann displacement, and density of finite-modification classes do prove that every continuous equivariant one-event function is constant (`R5-1_report.md:148-158`). For a full DLR one-site specification, constant conditional distributions do force the unique i.i.d. product measure, so that part of `R5-1_report.md:152` is correct.

For a merely retarded, past-cone kernel, constancy says only that the law at an event is independent of that event's causal past. It does not by itself rule out correlations among incomparable/spacelike events, common external randomness, or other joint extensions. A product conclusion needs an additional independently-driven generative construction, or a full conditional specification. Thus the retarded form of Theorem Q is condition-independence, not the unconditional product/no-composite conclusion.

### Admissibility

**The direct axiom claim is not established.** The actual axiom has sites `Z^3`, finite nearest-neighbor adjacency, and only translations plus proper cubic rotations (`MINIMAL_AXIOMS_2026-06-29.md:35-41`). Its rule is required to be determined by and vary with those nearest-neighbor conditions (`MINIMAL_AXIOMS_2026-06-29.md:55-61`, reiterated at `MINIMAL_AXIOMS_2026-06-29.md:114-123`). Theorem Q instead assumes conditions on `L_7\{0}` (or its causal past) and exact full `Gamma` covariance. Consequently `R5-1_report.md:164-166` is valid only after supplying a bridge that replaces the axiom's lattice/neighbor structure with LRL events and imposes full `Gamma` covariance. Without that bridge, Q does not refute Admissibility as written. Moreover, a tail-dependent escape would no longer be a nearest-neighbor rule in the literal axiom wording.

## 4. Proposition L

### Commutator and spectral measure

**Confirmed.** When `a` is outside the finite collision set `F-F`, strict locality gives `[B*,alpha_a(B)] = 0`. Translation invariance then identifies the Fourier coefficients of `nu_B` and `R_*nu_{B*}` outside `F-F` (`R5-1_report.md:170-175`). A finite signed measure with only finitely many nonzero Fourier coefficients is Haar measure times a trigonometric polynomial. Its singular part is therefore zero, yielding `nu_B^s = R_*nu_{B*}^s`.

### Shell classes

**Confirmed.** Each projected shell is the countable-chart image of a three-dimensional smooth manifold in a four-torus and is Haar-null. For the two signs, a common torus point requires `q_+ - q_- = G` for a reciprocal-lattice vector `G`. For each fixed `G`, the two mass-shell equations cut a set of dimension at most two; the countable union is null for both shell measures. Hence `[pi_*Omega_m^+]` and `[pi_*Omega_m^-]` are mutually singular, as asserted at `R5-1_report.md:176`.

### Status of `(SC_m)`

**The conditional proposition is valid, but `(SC_m)` is an added, strong hypothesis.** Reflection transfers a positive-sheet singular component created by `B` to the negative projected shell for `B*`. If the same global charge is future-causal and has invariant mass `m` on both projected sign classes, a negative-shell lift can land on `H_m^+` only on the null intersections just described, giving the contradiction at `R5-1_report.md:177`.

Neither the minimal axioms nor the ordinary positive-energy spectrum condition supplies the "same mass on the reflected class" clause. A measurable reciprocal-lattice/Bragg relift with variable invariant mass is outside `(SC_m)`, exactly as the worker concedes at `R5-1_report.md:182`. Therefore Proposition L is not an unconditional no-go for all strictly local nets; it is a no-go for the explicitly stated `mathfrak L + (SC_m)` class.

## 5. Lemma H

**Confirmed with the stated disintegration qualification.** The cocompact lattice `Gamma` acts properly on `H^3`, every orbit is infinite, and a measurable fundamental domain has infinitely many disjoint translates. An invariant finite measure would assign the domain both zero mass and full-orbit coverage, so no invariant probability exists (`R5-1_report.md:184-192`). Pushing forward an invariant probability through a measurable equivariant frame map gives the forbidden probability on `H^3`.

The one-realization and ensemble conclusions are correct when the branch decomposition/conditional law is measurable and equivariant, as the worker explicitly labels. They do not exclude symmetry-breaking branch spaces that define no measurable covariant rest frame; that limitation is already acknowledged at `R5-1_report.md:196-198`.

## 6. Example D and reruns

**The supplied computations reproduce exactly.** Running all three scripts again produced byte-for-byte identical output files. In particular:

- exact group membership and stabilizer-growth illustrations reproduce (`scripts/r51_stabilizers.py:21-52`; `scripts/r51_stabilizers.out:1-10`);
- the off-axis loxodromic reproduces (`scripts/r51_stab_offaxis.py:17-25`; `scripts/r51_stab_offaxis.out:1-2`);
- Gaussian-profile covariance is at `9.11e-54` and `1.67e-53` in the sampled tests (`scripts/r51_diamond_link.out:1-3`);
- the timelike and spacelike decay tables reproduce (`scripts/r51_diamond_link.out:4-18`);
- the independent boosted-frame quadrature agrees within `1.48e-14` of `W(0)` (`scripts/r51_diamond_link.out:23-28`);
- the first Hermite-chaos weight is `2/pi`, and the printed partial sums reproduce (`scripts/r51_diamond_link.out:29-37`).

The analytic construction at `R5-1_report.md:200-227` is sound: for the real Gaussian smearing, `sign Phi(f_l)` is bounded, its first Wiener/Fock chaos has norm fraction `2/pi`, and the nonvanishing Gaussian shell profile gives the massive positive-energy one-particle class with its continuum four-momentum. The covariance identity follows exactly from the Lorentz-scalar profile; the numerical samples are checks, not the proof.

Two labels should be narrowed. Despite its filename, `scripts/r51_diamond_link.py:69-135` tests only the rest-frame Gaussian, not the compact causal-diamond profile described at `R5-1_report.md:206-210`. Also, the unequal correlations at `scripts/r51_diamond_link.out:19-22` show that `g_1` does not fix the link; they do not numerically prove that the whole stabilizer is finite. Finiteness instead follows analytically from Lemma K. Neither point damages the Gaussian Example D.

Example D imports the continuum Fock space, continuum shell, and continuum momentum and merely labels smeared observables by LRL links (`R5-1_report.md:239-247`). It therefore verifies the consistency of the escape and literally realizes the requested spectral behavior, but it is not an LRL-native law and should not be counted as a PASS for the intended campaign target.

## 7. Class statement and fixed reading

**FAIL (bounded), with corrections, is the right fixed reading.** The fixed rubric does not demand an exhaustive no-go: it explicitly accepts a no-go for bounded-support multi-site operators "in a stated class" (`TESTS.md:2862-2873`). Theorem W supplies such a class without relying on Q, L, or H: finite-dimensional covariant families whose support has infinite stabilizer, including qubit operators on spacelike links and spacelike planar supports (`R5-1_report.md:139-142`). The open finite-stabilizer class at `R5-1_report.md:261-266` therefore prevents an exhaustive LRL no-go, but does not change the preregistered bounded FAIL to INCONCLUSIVE.

The corrected union is: `mathfrak W` as stated, with "confined" restricted to the Haar-a.c. correlations; `mathfrak Q` giving products for full DLR specifications but only condition-independence for arbitrary retarded kernels, and making no direct axiom claim absent an LRL/Admissibility bridge; `mathfrak L` only together with `(SC_m)`; and `mathfrak H` only for measurable equivariant frame-selecting branch families. The finite-dimensional, finite-stabilizer link-cell class with noncommuting timelike structure under a genuinely LRL-generated covariant law remains open.

## Strongest correct statement

On `L_7`, every finite-dimensional covariant operator family with an infinite pointwise support stabilizer--hence, for qubit degrees of freedom, every bounded support contained in a point, spacelike line, or spacelike plane--has no standard massive or massless shell component; its Haar-absolutely-continuous correlations occur only along the stabilizer-fixed spacelike sublattice, and every decomposable covariant four-charge obeying positive energy vanishes on that family. Continuous full-`Gamma` one-event rules are condition-independent (and full DLR specifications are products), strict all-cell locality excludes fixed-mass shell creation only under the extra `(SC_m)` hypothesis, and measurable frame-picking symmetry breaking cannot be restored by an invariant probability. A continuum free field smeared onto timelike links realizes the spectral escape but imports set A. No theorem here excludes finite-dimensional degrees of freedom on finite-stabilizer timelike/link cells with noncommuting timelike structure under a genuinely LRL-generated covariant law; that class remains open, while the preregistered result is nevertheless **FAIL, bounded to the corrected stated classes**, not INCONCLUSIVE.
