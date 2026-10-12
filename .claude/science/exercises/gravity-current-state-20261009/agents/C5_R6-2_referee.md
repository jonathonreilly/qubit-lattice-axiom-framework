# VERDICT: NOT CONFIRMED

The report contains several correct and useful bounded results, but two central steps fail: Set A does not satisfy the fixed `SUPPLIED-FORCED` criterion on the packet's own content, and Lemma A is false at its stated scope. The B′ Zariski/umklapp discussion also promotes coefficient-wise Lorentz covariance into the full Weinberg--Witten premises without proving exact continuous translations or a conserved stress tensor. The defensible per-set readings are therefore **A OPEN, B OPEN, B′ OPEN, C OPEN**. What is established is absence of a demonstrated `PRODUCIBLE` mechanism in this packet, not a no-go against every rule set.

## 1. Set A and the Weinberg--Witten conclusion

**Finding: not confirmed.** The fixed definition requires all Weinberg--Witten premises to be *shown* for the set's low-energy content before `SUPPLIED-FORCED` may be assigned (`TESTS.md:3094-3097`). Set A is only fixed here as “a continuum base with discreteness only in records” (`TESTS.md:2424-2429`). Its more concrete flash setting is a continuum QFT plus a **supplied** linearized graviton (`TESTS.md:2533-2537`), and the worker itself records that the flashes obey a sourced, not conserved, stress equation and that a covariant conserved (T^{\mu\nu}) is unproved outside a narrower Lagrangian subclass (`R6-2_report.md:179-183`, `R6-2_report.md:312`). Moreover, “covariant in law” for a stochastic collapse/flash process does not establish the unitary Poincaré representation posited in W1 (`R6-2_report.md:70-74`, `R6-2_report.md:179`). W2 is likewise listed only as “the would-be graviton,” not as an established massless one-particle pole (`R6-2_report.md:180`). Thus A's full content does not establish W1--W3. The flash rate being small does not restore an exact premise.

There is also a logical error in the fixed inference as used. Weinberg--Witten theorem 2 says that a theory possessing the specified covariant conserved stress tensor cannot contain *elementary or composite* massless particles of spin (>1); it does not say that such a particle must instead be elementary or “supplied.” GR evades the theorem because gravitational stress is not represented by such a Lorentz-covariant tensor. This is already the packet's prior referee warning (`B_referee.md:44-50`) and is explicit in the [original paper](https://hep.physics.uoc.gr/Erasmus-IP-2013/files/lectures/chiral-symmetry/Weinberg-Witten.pdf) and [Jenkins](https://arxiv.org/abs/0904.0453). The original proof needs a nonzero nearly-forward limit fixed by the charge normalization; a separate assumption of continuity at exactly zero transfer is not required in the form stated by Weinberg and Witten, so W4 at `R6-2_report.md:74` should be phrased more carefully.

The required independent-referee step is satisfied by this report, but it does **not** ratify A's reading. Under the fixed buckets A is **OPEN**, not `SUPPLIED-FORCED`.

## 2. Order lemma and momentum pairs

**Finding: confirmed with a proof repair.** The discrete character calculation is right: for helicity (h=2), the state phase has character (4\bmod n), and the rank-two tensor restriction contains it for (n=1,2,3,4,6), first failing at (n=7) (`scripts/r62_little_group.py:25-36`; independent check `referee_independent_checks.out:1`). The explicit (C_3) and (C_4) elements also check (`scripts/r62_little_group.py:66-76`).

The exact group argument should be stated as follows. If a nonidentity (\gamma\in SO^+(Q,\mathbb Z)) fixes two non-collinear null momenta pointwise, their span is a Lorentzian two-plane (P), and (\gamma) acts as the identity on (P). Its fixed eigenspace is rational because it is the kernel of the integer matrix (\gamma-I); for a nontrivial rotation this eigenspace is exactly (P). The restriction to the positive-definite rational lattice in (P^\perp) is an orientation-preserving crystallographic rotation, hence has order (2,3,4,) or (6); the identity supplies order (1). The sentence “the eigenspace is rational, so (P) can be taken rational” at `R6-2_report.md:101-107` skips the needed nonidentity/equality step but reaches the correct result. The three-squares argument for anisotropy is also correct.

The pair-orbit claim is correct in its stated non-collinear, fixed-invariant sector. Such pairs form (G/K) with compact (K\simeq SO(2)), and a discrete subgroup acts properly on (G/K); its orbits are discrete. Hence the single-null-orbit density result at `TESTS.md:2923-2926` does not propagate an off-forward form factor across pair space (`R6-2_report.md:111-116`). This only empties the **microscopic discrete phase argument**. It does not exclude a genuinely emergent continuous Lorentz symmetry, as the report later acknowledges (`R6-2_report.md:303-305`).

## 3. Tensor form counts

**Finding: confirmed, with interpretation bounded.** Exact character sums give

- (W(B_4)): 1 invariant in (\mathrm{Sym}^2V), 3 mass forms, 9 two-derivative (kkhh) forms;
- (B_4^+): the same (1,3,9);
- (SO(4)): (1,2,4).

The worker's implementation uses the correct symmetric-power characters (`scripts/r62_tensor_lv_counts.py:13-23`), and a separate exact enumeration reproduces the finite-group counts (`referee_independent_checks.out:2-3`) while the (SO(4)) decomposition gives the exact (2,4) result (`referee_independent_checks.out:8`). Thus `R6-2_report.md:118-129` is correct as an invariant-form count.

The count alone does not prove a healthy two-helicity spectrum, stability, universal coupling, or that exactly one of the nine kinetic forms is gauge invariant. The separate K1 result is needed for the gauge-restoration codimension (3+(9-1)=11) (`TESTS.md:1663-1667`). The report is acceptable where it cites that result, but “1 extra mass and 5 extra kinetic forms” should not itself be presented as the derivation of 11 tunings.

## 4. Lemma A and the `43 = 31 + 15` check

**Finding: the numerical example is confirmed; the general lemma is false as stated.** On the tested (L=4) commuting (\mathbb Z_2) gauge chain, the dimensions really are

\[
\dim W=43,\qquad \dim S=31,\qquad \dim Z=15,
\]

with a **three-dimensional overlap**, so the precise relation is

\[
\dim(S+Z)=31+15-3=43.
\]

The worker output reports the three raw dimensions and the span dimension (`scripts/r62_averaging_lemma.out:1-7`); an independent exact rational sparse-Pauli computation finds `(43,31,15,3,43)` (`referee_independent_checks.out:4-6`). The script also explicitly assumes mutually commuting Gauss generators (`scripts/r62_averaging_lemma.py:35-40`).

The theorem at `R6-2_report.md:131-138` does not follow. Finite-dimensional sites make the unitary group compact only at fixed finite total volume; averaging over the full generated group can spread a local operator across that whole volume. The claim that only group factors touching the original support matter fails when overlapping generators do not commute.

A concrete counterexample is a finite qubit chain with local generators (G_j=\mathrm{SWAP}_{j,j+1}), compact closure (S_L), and (H=\sum_j Z_j). Then ([H,G_j]=0) for every (j), but the group average of the local density (Z_1) is (H/L), supported on every site. For (L=5), direct enumeration gives coefficients ((1/5,1/5,1/5,1/5,1/5)) (`referee_independent_checks.out:7`). No non-scalar operator with support bounded independently of (L) is invariant under all adjacent swaps. Thus weak invariance has not been converted into a uniformly local strong density.

The valid scope is narrower: the averaging proof works for a compact **support-preserving local gauge action**, for example a direct product of onsite/local gauge groups whose factors outside a fixed finite neighborhood commute with the local term. This includes the commuting (\mathbb Z_2) example and standard sitewise non-Abelian gauge actions when distinct site groups commute, but not an arbitrary group generated by bounded-support operators. On a generic finite system the average is strongly invariant but need not remain local; on an infinite system the generated norm-closure need not be compact. Consequently the combined A+HWW upgrade at `R6-2_report.md:157-162` is not proved for general finite-site emergent gauge structures.

## 5. Dispersion checks

**Finding: the executed Gaussian checks reproduce; the theorem must say a bound, not an equality.** The local invariant symbols scale as (O(k^2)), the random strong examples have their largest physical frequency scaling as (k^2), and the weak Einstein control scales linearly (`scripts/r62_hww_dispersion.out:1-21`). The larger boxes reproduce the (1.999) exponent (`scripts/r62_hww_box5.out:1-2`). The analytic reason is the same moment/Taylor argument in the 09-14 note: local vector-gauge-invariant (h)-functionals begin at (k^2) (`LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md:197-207`). With a nonsingular (k^0) momentum block, a strong quadratic potential beginning at (k^4) yields frequencies **at most of order (k^2)**; a nonzero coefficient and nondegenerate stable branch are needed for (\omega\sim k^2). Cancellations or absent stiffness can be softer or zero.

Two further scope points matter. First, the vector-law physical subspace used by the script is three-dimensional (`scripts/r62_hww_dispersion.py:90-93`), so the maximum-frequency fit is not by itself a two-helicity graviton theorem. Second, with both vector and scalar compact symmetries the landed result is (O(k^3)), but only in its expressly regular compact-character class, with nonlinear/strongly interacting routes left open (`LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md:186-223`). The report's own final scope note is substantially correct (`R6-2_report.md:303-310`), whereas “strongly invariant local energy gives (\omega\propto k^2)” and the broad combined implication are too strong.

Calling this “WW's Hamiltonian face” (`R6-2_report.md:169-171`) is an analogy, not a theorem identification. [Marolf's result](https://arxiv.org/abs/1409.2509) is distinct: nonlinear universal coupling makes the gravitational Hamiltonian a boundary term on shell, which conflicts with microscopic local kinematics unless bulk dynamics freezes. It applies without Lorentz or translation invariance, subject to its compatibility assumptions.

## 6. B′: Zariski density and umklapp

**Finding: the coefficient statement is right; the Weinberg--Witten upgrade is not established.** Zariski density does imply that every exactly (\Gamma_L)-invariant polynomial tensor, and every polynomially equivariant tensor law, is invariant/equivariant under the algebraic Lorentz group. For a genuinely analytic law this applies coefficient by coefficient to its Taylor series. This supports the form-count statement recorded at `TESTS.md:2784-2791` and the conditional sentence at `R6-2_report.md:191-195`.

It does **not** by itself supply an exact continuum local action, exact continuous translations, a Poincaré representation, a conserved Lorentz-covariant (T^{\mu\nu}) whose charge is (P^\nu), or the required one-particle pole/near-forward limit. A finite derivative truncation or formal Taylor series is not an exact symmetry theorem for the full lattice theory. The phrase “its Noether (T) is covariant at every polynomial order” at `R6-2_report.md:193` silently assumes both an action and continuous translations.

The umklapp conclusion at `R6-2_report.md:196-200` is half-right. The reciprocal gap can protect the narrow (1\to1), small-(q) matrix element, so multiparticle umklapp need not directly alter that form factor. But exact conservation of (T^{\mu\nu}) and (P^\nu=\int T^{0\nu}) is a global operator premise. The packet's established multiparticle umklapp and absence of an additive covariant charge (`TESTS.md:2784-2791`, `TESTS.md:2914-2917`) therefore obstruct W3 as well as soft universality. “Umklapp attacks universality, not WW” is too strong.

Accordingly B′ is **OPEN**, without a justified “leaning `SUPPLIED-FORCED`.” Weinberg--Witten would bind only after adding the stronger exact continuum-EFT premises that are currently missing; Zariski density alone does not add them.

## 7. Set C and the speed-tuning numbers

**Finding: OPEN is correct; several numerical counts are branch-specific or naturalness estimates.** The exact-constraint weak VS/N-type comparator has two positive linear TT modes and an attractive inverse-Laplacian response to a **supplied** scalar source, while the physical lattice stress/source bridge remains open (`R2_referee.md:19`, `R2_referee.md:40-45`; `LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md:290-295`). Hence C-N* does not meet `PRODUCIBLE`, exactly as `R6-2_report.md:266-282` concludes. But Lemma A cannot be used to exclude all finite-site microscopic realizations, and the packet expressly leaves nonlinear/nonregular strong-coupling phases open (`TESTS.md:736-759`; `R6-2_report.md:313-316`). The momentum obstruction is bounded, not class-wide: RN-L2 lists matrix-valued, gauge-mediated, nonperturbative, and zero-scattering routes as open (`TESTS.md:856-862`).

For speeds:

- The GW170817/GRB 170817A band (-3\times10^{-15}\le(c_g-c)/c\le7\times10^{-16}) is correctly quoted; the [primary multimessenger paper](https://arxiv.org/abs/1710.05834) gives those values. Comparing it with an assumed order-one bare mismatch is an approximately 15-decade **naturalness estimate**, not a derived tuning theorem (`R6-2_report.md:242-245`; independent arithmetic `referee_independent_checks.out:9`).
- The local codimension (3), or (4) without P/T, belongs to the tested **S/S-tl scalar-charge branch**: two isotropy conditions, one matter-cone match, and optionally one parity-odd relation (`R2_report.md:124-130`; `R2_referee.md:27-30`). The same table explicitly says V, V-tl, and VS were not counted. It cannot be added to C-N* as though it were its tuning count.
- “Matter's (N-1) speeds” is not proved here. The (3.1\times10^{-17}) number is one regulator-specific electron--photon counterterm example, and `TESTS.md:2377-2384` expressly rejects a universal one-tuning-per-species theorem.

Thus the minimal defensible statement is: any Lorentz-violating C mechanism with independently set matter and tensor cones needs at least one relative cone match unless another symmetry/flow enforces it; no exact total count has been derived for C-N*.

## 8. Readings

| Set | Referee reading | Reason |
|---|---|---|
| A | **OPEN** | Exact W1--W3 are not shown for the set's flash content, and Weinberg--Witten does not imply “elementary/supplied.” |
| B | **OPEN** | The (3/9) hypercubic form count confirms that matter-sector dimension-four protection does not establish the graviton-sector premises; no stable universally coupled producing model is constructed (`R6-2_report.md:206-221`). |
| B′ | **OPEN** | The per-copy discrete WW phase argument is empty; Zariski density controls polynomial coefficients but does not supply the full exact WW premises, and umklapp obstructs exact W3 (`R6-2_report.md:189-205`). |
| C | **OPEN** | Exact weak N-type and strong-coupling routes remain open; no exact physical stress/source bridge or universal lattice momentum has been constructed (`R6-2_report.md:223-250`). |

No set is shown `PRODUCIBLE` in the supplied packet. That is an evidence-status statement, not proof that no rule set can produce a universally coupled graviton.

## No-go discipline check

- **N1:** The relevant distinct routes are ordinary continuum compositeness (A), Lorentz-violating hypercubic tensor dynamics (B), discrete arithmetic symmetry and analytic emergence (B′), weak exact-constraint N-type dynamics (C), nonregular strong-coupling emergence, and kinematic nonlocality/holography. Several remain unclosed.
- **N2:** Dispersion, exact momentum/source identification, and locality are not proved independent universal walls; their implications depend on branch and regularity assumptions.
- **N3:** Hidden premises include a Lagrangian A-subclass, a support-preserving gauge action in Lemma A, an exact continuum action and translation symmetry in the B′ Zariski step, and order-one bare speed mismatch.
- **N4:** Weinberg--Witten addresses a covariant conserved stress tensor; Marolf addresses nonlinear universal energy coupling plus boundary Hamiltonians and local kinematics; the 09-14 note addresses a regular compact-character class. None is a witness against all rule sets.
- **N5:** The per-realization discrete phase result does not lift to an all-effective-law statement, and the finite-box averaging identity does not lift to uniformly local thermodynamic dynamics.
- **N6:** No approved primitive supplies a graviton dynamics or Lorentz-closure theorem. Kinetic isotropy does not fix the independent graviton cone or the stress/source bridge.
- **N7:** The exact weak N-type theory with a yet-unbuilt conserved stress bridge, and a nonregular strongly coupled qubit phase, are concrete counterroutes. The universal no-go is therefore premature.
- **N8:** The 09-14 note itself preserves noncompact, nonlinear, singular, additional-field, and strongly interacting escapes (`LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md:215-223`, `:254-258`).

The broad negative claim fails N3, N5, and N7. It must be narrowed to absence of a demonstrated mechanism in the packet.

## Strongest correct statement

Within the supplied C5 packet, no set has an explicit mechanism that simultaneously yields a massless helicity-2 pole, exact universal coupling to matter's energy-momentum, and the stated prices, so none is presently `PRODUCIBLE`; however, Weinberg--Witten only excludes a massless spin-2 state in a theory that actually possesses the exact Lorentz/Poincaré and covariant conserved-stress premises, and it neither forces such a state to be elementary nor proves it must be supplied. The discrete (\Gamma_L) little-group and pair-orbit results are sound, as are the (3/9) versus (2/4) invariant-form counts and the bounded regular-Gaussian dispersion results, but Zariski density alone does not create an exact stress tensor or continuous translations, multiparticle umklapp obstructs that premise, and finite-dimensional sites do not make weak and strong local invariance equivalent without a support-preserving gauge action. Therefore A, B, B′, and C are all `OPEN`; the live producing routes remain exact weak N-type with a derived stress/source bridge, nonregular strong-coupling emergence, or an explicitly nonlocal/holographic mechanism.
