# Mass-gap crossover reduction (conditional; closes no MG row)

Author checkpoint, 1 November 2026; editorial restatement (definitions, status labels, dependency table, isolation of
computer-assisted steps) on the same date. **The four-dimensional continuum existence and physical mass-gap target remains
open.** This unit states a conditional theorem (Theorem H) that reduces MG1 and MG3 of [MASS_GAP_TARGET.md](MASS_GAP_TARGET.md)
to one named open estimate, the crossover-window clustering bound (CW), plus MG2, an unwritten bookkeeping step (H6) and
literature inputs. It proves no new inequality on the Wilson measure. It also records scope tests that any CW producer must pass.
No MG row changes status. The editorial pass changed no mathematical content; gaps found are listed in §10 as open items.

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: conditional-support
independent_review: pending
MG_rows_closed: []
```

Companion notes: [MASS_GAP_CW_CROSSOVER_ATTACK.md](MASS_GAP_CW_CROSSOVER_ATTACK.md) (cited as ATT: Prop. S, Theorem H′, open
lemmas OL-S1 and OL-DS) and the long-form background [MASS_GAP_RECORD_RG_HYBRID_SKETCH.md](MASS_GAP_RECORD_RG_HYBRID_SKETCH.md)
(narrative; every mathematical statement in it is restated here with status). Pinned inputs: this branch at `f76f6c649cff`;
main-repo notes as cited below, all `audit_status: unaudited` in `docs/audit/data/ledger/**`.

## 0. Status labels

**[proved here]** complete argument in this note (whole note: independent review pending); **[outline]** argument given at
the level of a proof outline, standard, not written in full; **[cited: ref]** literature, exact reference in §References;
**[repo, unaudited]** main-repo or branch note, not independently audited; **[open]** not proved; **Open Lemma** a precise
open statement isolated because only computer-assisted evidence exists; **Conjecture**; **Remark / Heuristic** explanation, no
claim of proof. No proved statement in this unit depends on a computation.

## 1. Definitions

**Definition 1.1 (lattice, measure).** Fix N ≥ 2, spacing a > 0 and a periodic lattice Λ = (Z/LZ)³ × (Z/L_t Z) (the original
text takes L_t = L; the fourth direction is Euclidean time). E is the set of links, U = (U_e)_{e∈E} ∈ SU(N)^E. The Wilson measure is
  dμ_{β,Λ}(U) = Z^{-1} exp{ (β/N) Σ_p Re Tr U_p } Π_{e∈E} dU_e,   β = 2N/g_0²,
with dU_e normalized Haar measure and the sum over unoriented plaquettes. The fourth direction, the action and the trajectory
below are supplied; none is derived from the framework axioms (`docs/MINIMAL_AXIOMS_2026-06-29.md` lists them as open gates).

**Definition 1.2 (trajectory).** A trajectory is a function a ↦ g_0(a) with g_0(a) → 0 as a → 0 following the two-loop
asymptotic-freedom relation at fixed lattice Λ-parameter Λ_L.

**Definition 1.3 (reflection, observables, RP).** Θ is the time reflection in a lattice plane through sites or through links,
acting on functions by (ΘF)(U) = conj F(θU). 𝔄_+ is the algebra of bounded gauge-invariant functions of finitely many links in
the positive-time half. μ is *reflection positive* (RP) for Θ if ⟨Θ(F) F⟩_μ ≥ 0 for all F ∈ 𝔄_+.

**Definition 1.4 (transfer operator, Hamiltonian).** ℋ_0 = L²(SU(N)^{E_s}, Haar), E_s the links of one time slice;
T = P_G M^{1/2} K M^{1/2} P_G, where K is the integral operator with kernel ⊗_{e∈E_s} k_β(U_e V_e^†), k_β(W) = exp[(β/N) Re Tr W],
M is multiplication by exp{(β/N) Σ_{p ⊂ slice} Re Tr U_p}, and P_G is the projection onto gauge-invariant functions. On the
gauge-invariant subspace, H_a := −a^{-1} log(T/‖T‖) (defined on the closure of the range of T), with ground state Ω_a.

**Definition 1.5 (reflected correlation; gap).** For F ∈ 𝔄_+ with ⟨F⟩ = 0 and n ∈ N, C_F(n) := ⟨Θ(F) τ_n F⟩, τ_n the time
translation by n lattice steps. H_a has *gap ≥ m* if spec(H_a) ⊂ {0} ∪ [m, ∞) and ker H_a = span{Ω_a}.

**Definition 1.6 (volume-uniform reflected decay).** A family 𝔉 ⊂ 𝔄_+ has *volume-uniform reflected decay at rate m* if for every
F ∈ 𝔉 there are A_F, n_F such that for every Λ and every n ≥ n_F, 0 ≤ C_F(n) ≤ A_F e^{−m n a}; m is independent of F and Λ.

**Definition 1.7 (clustering).** Truncated correlations ⟨A; B⟩ := ⟨AB⟩ − ⟨A⟩⟨B⟩ of gauge-invariant local observables *cluster
at rate μ uniformly in volume* if |⟨A; B⟩| ≤ C_{A,B} e^{−μ d(A,B)} with μ independent of A, B, Λ.

**Definition 1.8 (Bałaban effective actions).** For block factor L_b and k ≥ 0, S_k denotes the effective action on the lattice
of spacing a_k = L_b^k a produced by Bałaban's gauge-covariant block-spin transformation, with running coupling g_k, as defined
in Bałaban (CMP 1984–89). It is not reproduced here.

**Definition 1.9 (MG rows).** MG0–MG5 are the ledger rows of [MASS_GAP_TARGET.md](MASS_GAP_TARGET.md) (MG0 existence and
reconstruction; MG1 infrared estimate; MG2 source transport; MG3 cutoff/volume passage; MG4 non-trivial excited sector; MG5
final scope), quoted in the sketch §0.8.

**Definitions of CW, CW′, landing.** CW: §3 below. CW′ and the landing clause: ATT §4 (Theorem H′); block coefficient α_V and
CW_ℓ: ATT Definitions 1.3–1.4.

## 2. Hypotheses and their status

| Tag | Statement | Status |
|---|---|---|
| H1 | For every β ≥ 0 and periodic Λ, μ_{β,Λ} is RP for site- and link-plane reflections | [cited: Osterwalder–Seiler 1978]. [repo, unaudited]: two-slice temporal-gauge Gram PSD; one-link kernel coefficients c_λ(β) ≥ 0 |
| H2 | T is bounded, self-adjoint, positive and compact on the gauge-invariant subspace of ℋ_0, with a simple top eigenvalue | [cited: Lüscher 1977; Osterwalder–Seiler 1978]. Assembly from the repo pieces: Lemma A1 [outline] |
| H3 | For a family 𝔉 whose OS vectors are dense: volume-uniform reflected decay at rate m ⇔ gap ≥ m | ⇐: Lemma A2 [proved here; also MASS_GAP_TARGET §2, independently checked]. ⇒: standard spectral theorem; [repo, unaudited] finite-block version |
| H4 | There is β_sc > 0 such that for 0 < β ≤ β_sc truncated correlations cluster uniformly in volume (Def. 1.7) | [cited: Osterwalder–Seiler 1978, cluster expansion; constants not extracted here]. SU(2), 0 < β ≤ 1/32: [MASS_GAP_LOCAL_BLOCK_ASTRA.md](MASS_GAP_LOCAL_BLOCK_ASTRA.md), same-family review. SU(2), β < 1/9: ATT Prop. S, **conditional on Open Lemma OL-S1** |
| H5 | For g_0 small and a fixed finite physical torus, the effective actions S_k exist while g_k ≤ ḡ, of the form (1/g_k²)·(Wilson-like) + polymers, with small-field analyticity, large-field suppression and asymptotic-freedom flow of g_k | [cited: Bałaban CMP 1984–89], **finite volume, partition-function/effective-action bounds only**. Not: infinite volume, general correlators, a gap |
| H6 | There is k_1(a) → ∞ with g_{k_1} ≈ ḡ and a_{k_1} → ℓ_1 = c_1/Λ_L, c_1 independent of a | **[open]**: plausible bookkeeping from H5; not written |
| MG2 | Source transport of original observables through the RG, with F-dependent prefactor and onset only | **[open]**. [MASS_GAP_CONSTRUCTION_ASTRA.md](MASS_GAP_CONSTRUCTION_ASTRA.md) covers its stated sectors only |
| **CW** | §3 | **[open]** |

## 3. The open estimate CW

**Definition 3.1 (CW, crossover-window clustering).** CW holds for a trajectory if there exist ḡ ≤ g_* (the H5 range),
n_* ∈ N, μ_* > 0 and a_0 > 0 such that for every a ≤ a_0 and every volume, the effective measure at scale
ℓ_* = L_b^{n_*} ℓ_1 satisfies, for all gauge-invariant local block observables A, B,
  |⟨A; B⟩_eff| ≤ C_{A,B} e^{−μ_* d(A,B)/ℓ_*},
with μ_* independent of a, the volume, A and B; and this bound transports to the original observables (MG2) with
F-dependent prefactor and onset only. *Variant:* the same bound proved directly for the original measure, without RG steps.

**Status: open.** **Remark 3.2.** CW is the "quantitative crossover theorem" of MASS_GAP_TARGET §3 written as one estimate:
no bulk transition between Bałaban's ḡ and a provable cluster regime, with a finite correlation length made quantitative.
For SU(2) the cluster regime proved in the branch starts at β ≤ 1/32 (g² ≥ 128); conditional on OL-S1 it starts at β < 1/9
(g² > 36). No theorem covers the window. The fixed positive handoff interval of Kirk v4 (Zenodo 21765806) is a candidate CW
supplier; [CROSSOVER_LITERATURE_BRIDGE_ASTRA.md](CROSSOVER_LITERATURE_BRIDGE_ASTRA.md) and
[its review](REVIEW_CROSSOVER_LITERATURE_BRIDGE_ASTRA.md) find that its Lemma 3.26 operator-norm hypothesis does not give the
displayed core-size-independent determinant bound. A size-aware repair remains possible; no checked import supplies CW.

## 4. Theorem H (conditional)

**Theorem H [conditional on H1–H6, MG2 and CW; proof outline below; independent review pending].** Let N ≥ 2, d = 4, and let
g_0(a) follow a trajectory (Def. 1.2). Assume H1–H6, MG2 and CW. Then there is a_0 > 0 such that for every a ≤ a_0 and every
volume, H_a has gap ≥ m_* (Def. 1.5), with
  m_* = μ_*/ℓ_* = c·Λ_L,   c = μ_*/(c_1 L_b^{n_*}),
and c independent of a and the volume. If moreover MG0 holds, the bound passes to the continuum Hamiltonian H by the
fixed-t-first rule of MASS_GAP_TARGET §3. MG4 (a non-empty Ω-perp) is a separate input.

**Remark 4.1.** Without CW the statement is empty as a → 0: H1–H4 give only the fixed-spacing strong-coupling gap already in
MASS_GAP_LOCAL_BLOCK_ASTRA (and, conditional on OL-S1, ATT Cor. S′).

### Steps (each a lemma with its status)

- **Lemma A1 (RP ⇒ positive compact transfer operator) [outline; cited: Lüscher 1977].** In temporal gauge the weight factorizes
  as Π_t M^{1/2} K M^{1/2}. c_λ(β) ≥ 0 makes convolution by k_β a positive operator; k_β ∈ L² makes it Hilbert–Schmidt. Tensor
  products, sandwiching by the bounded positive M^{1/2}, and the commuting Gauss projector keep positivity and compactness;
  k_β > 0 gives a simple top eigenvalue (Jentzsch). The repo pieces [repo, unaudited] are exactly the inputs.
- **Lemma A2 (decay ⇒ gap) [proved here; = MASS_GAP_TARGET §2 at fixed a].** C_F(n) = ⟨v_F, T̂^n v_F⟩ = ∫ λ^n dν_F(λ) with
  T̂ = T/‖T‖ on the OS space. If C_F(n) ≤ A_F e^{−m n a} for n ≥ n_F, then ν_F is supported in [0, e^{−ma}]. Density of
  {v_F} gives H_a ≥ m on Ω-perp. A_F, n_F may depend on F; m may not.
- **Lemma A3 (volume passage) [outline].** Volume-uniform fixed-n bounds and RP are preserved under weak limits of μ_{β,Λ}
  (compactness of SU(N)^E); reconstruct and reapply A2. Uniqueness of the limit is known only in the strong-coupling regime;
  in the window CW must supply it.
- **Lemma A4 (strong coupling) = H4 [cited].** Gives A2's hypothesis at β ≤ β_sc: the wrong end of the trajectory.
- **B0 (inductive hypothesis; Definition).** IH(k): (i) small-field analyticity with polymer bounds |E_k(X)| ≤ g_k^{κ_0} e^{−κ|X|};
  (ii) large-field suppression; (iii) coupling flow. **Not** (iv) block-unit clustering at every scale (flag C1).
- **B1 (one step preserves IH) = H5 [cited].** RP of S_k is not needed: A1–A2 use RP of the original Wilson measure only
  [proved here: logical structure of the argument].
- **B2 (flow to ḡ) = H6 [open].**
- **B3 (crossover) = CW [open].** Possible routes (Remark): continue the RG past ḡ to a cluster regime; a Dobrushin/Doob
  contraction for the effective one-block kernel at ℓ_1 (ATT: CW′); an external import (none checked).
- **B4 (transport back) = MG2 [open].** Write C_F(n) as an effective expectation of a source-dependent block functional;
  F-dependent A_F, t_F are allowed.
- **B5 (conclude) [proved here from A2, B2–B4].** A2 gives H_a ≥ m_* on Ω-perp uniformly in a and volume; MG0 carries it to the
  continuum.

## 5. Further statements

**Proposition 5.1 (MG1 + MG3 ⇐ CW + MG2) [= Theorem H; conditional on H5 (finite volume) and H6].**

**Remark 5.2 (RP of effective actions not required) [proved here].** Theorem H uses RP only for μ_{β,Λ} (H1), via A1–A2.

**Heuristic 5.3 (inductive RG hypotheses must not include block-unit clustering at every scale; flag C1).** At weak coupling
the effective correlation length in block units is ~ 1/(Λ a_k) and diverges, so such a hypothesis is false, or, stated in
physical units, is MG1.

**Remark 5.4 (scope test for CW producers; not a no-go).** Compact U(1) Wilson theory in d = 4 has a proved massless phase at
weak coupling [cited: Guth 1980; Fröhlich–Spencer 1982]. Hence any argument that yields CW without using a property that fails
for U(1) in d = 4 (e.g. non-abelian structure, d = 4 marginality) would also yield a gap for that theory and cannot be correct as
stated. This is a test a candidate must pass, not a route-exhaustion or global no-go claim. A d = 5 analogue is Heuristic only
(based on numerics, not proved).

**Lemma 5.5 (Observation P: time-invariant observables cannot be in the MG1 family) [proved here].** Let R ∈ 𝔄_+ satisfy
τ_n R = R for all n ≥ 0 under the measure (as for a permanent record readout). Then ⟨R; τ_n R⟩ = Var(R) for all n. Hence, if R is
not a.s. constant, no estimate C_R(n) → 0 holds, and if [R − ⟨R⟩] ≠ 0 in the OS space then it is a nonzero vector fixed by T̂,
so ker H_a ⊋ span{Ω_a}. *Proof.* Immediate from τ_n R = R and the definitions. ∎
*Remark.* Records are therefore superselection labels and cannot be the dense MG1 family; the Record axiom
(`docs/MINIMAL_AXIOMS_2026-06-29.md`) contains no decay clause.

## 6. Circularity flags (Remarks)

- **C1.** Block-unit decay at every RG scale: false at weak coupling, or MG1 (Heuristic 5.3).
- **C2.** "Record clustering uniformly in a" in physical units is MG1 + MG3; adopting it would adopt the gap as an axiom.
- **C3.** A gap at β ≤ β_sc is at the wrong end of the trajectory.
- **C4.** Main-repo `SU3_BETA6_GAP_BULK_CRITICALITY_REDUCTION_BOUNDED_THEOREM_NOTE_2026-06-09.md` assumes no bulk critical
  point on 0 < β ≤ 6. CW contains that premise, uniformly along the trajectory. It is not evidence for CW.
- **C5.** The ASTRA mass-gap units cited here have pending or same-family review; they are used as supported, not verified.
- **C6–C9.** ATT §4.

## 7. Relation to PR #10132 (Remark)

`.claude/science/physics-loops/ym4d-hard-route-20261030/` (branch `claude/ym4d-hard-route`, read at `5ad46ff72b19`) targets SU(2)
existence and non-triviality (NT1, NT2) and lists the mass gap as a later target. On a common trajectory and observable family:
a gap with non-empty Ω-perp gives NT1; its NT1/NT2 witnesses give MG4 non-emptiness. Interface note on that branch:
`library/mass-gap-interface.md`. Trajectories and blocking differ (hard-constraint vs soft kernel); the interface holds only on a
common hierarchy.

## 8. Update: Proposition S and Theorem H′ (statements in ATT; summary only)

**CW remains open; no MG row changes status.**

- **Open Lemma OL-S1 (ATT §2).** For κ ∈ (0, 2/3], 1 − R(κ)² − 3R(κ)/κ ≤ 1/4 with R = I₂/I₁. Proved for κ ≤ κ₀ ≈ 0.0263;
  reduced on [κ₀, 2/3] to finitely many inequalities; only computer-assisted evidence (arb, 29,602 cells on (0, 1.2]) exists
  for those. **This is the only computer-assisted input of Prop. S, and it is not used as proved.**
- **Proposition S (ATT §2) [conditional on OL-S1; review pending].** SU(2), d = 4, 0 < β < 1/9: C_ij ≤ β/2 and q ≤ 9β < 1.
  **Corollary S′** [conditional on OL-S1, ATT Theorem 2.0 (form: OI-6), H1, A2]: volume-uniform gap ≥ −log(9β) in lattice units.
  If OL-S1 is proved and the note reviewed, H4 for SU(2) extends from β ≤ 1/32 to β < 1/9 (g² > 36), with a weaker mass than
  the Doob bound at very small β.
- **Conjecture S♯ (ATT §2).** Single-link threshold π/24 ≈ 0.131; computed observation O-MAD gives β_D ≥ 0.1173 (not certified).
- **Computed observation O-KP (ATT §3).** A simple Kotecký–Preiss sufficient condition holds only for β ≲ 0.0078 (counting
  D = 80) or β ≲ 0.0109 (D = eΔ). Below 1/32; not used.
- **Computed observation O-τ (ATT §3).** The truncation-error bound τ_½(β) for the MDTN/ASQR j_max = ½ truncation (Chandrasekharan–
  Siew–Bhattacharya 2025) exceeds 1 for β ≳ 1.5 (computed partial sums, not certified). That means this bound gives no control
  there; it does not prove the truncation fails. Not used.
- **Theorem H′ (ATT §4) [conditional].** Theorem H with CW replaced by **CW′**: a block criterion α_V(γ_0) ≤ 1 − 2η for a
  reference specification γ_0 (verification half) plus landing of the effective specification within δ(η, V) of γ_0 uniformly
  in a and volume (landing half), plus MG2; also conditional on Open Lemma OL-DS and on Lemma 1.7 (stated, proof not written).
  Flags C6–C9.
- **Numerical evidence (ATT Appendix N; not used in any proof).** SU(2) 4⁴/6⁴/8⁴ Monte Carlo (Wilson action, C4).
- **Status delta.** H4 (SU(2)): β_sc from 1/32 to 1/9 *only once OL-S1 is proved and Prop. S reviewed*. CW unchanged (open),
  restated as CW′. MG1/MG3 unchanged (conditional). MG_rows_closed: [].

## 9. Consolidated dependency table

Legend: **P** proved here (review pending); **C** cited (exact reference in §References); **R** repo/branch note, unaudited or
same-family review; **OL** open lemma (computer-assisted evidence only or form unchecked); **O** open; **CW** the open estimate CW
(or CW′); **C8** CW′ landing half; **OI-n** open item from the editorial pass (§10 here, or ATT §6).

| Result | Depends on | Status of result |
|---|---|---|
| Lemma A1 (positive compact T) | H1 [C, R], H2 [C] | outline / C |
| Lemma A2 (decay ⇒ gap) | spectral theorem; OS reconstruction at fixed a | P (also MASS_GAP_TARGET §2) |
| Lemma A3 (volume passage) | A2; weak compactness; RP closed under limits | outline |
| H4 / Lemma A4 | Osterwalder–Seiler [C]; SU(2) ≤ 1/32 [R] | C / R |
| Lemma 5.5 (Observation P) | definitions only | P |
| Remark 5.4 (U(1) scope test) | Guth [C]; Fröhlich–Spencer [C] | scope test, not a no-go |
| Theorem H | H1 [C], H2 [C], H3 (A2) [P], H4 [C], H5 [C, finite volume], H6 [O], MG2 [O], CW [CW] | conditional |
| Prop. 5.1 (MG1+MG3 ⇐ CW+MG2) | Theorem H | conditional |
| Lemmas ATT 2.1–2.5 | elementary; Bessel identities | P |
| Prop. S | OL-S1 [OL]; Lemmas 2.1–2.5 [P]; Pinsker [C, standard] | conditional on OL-S1 |
| Cor. S′ (gap ≥ −log 9β) | Prop. S; Dobrushin/Föllmer Theorem 2.0 [C; form OI-6]; H1 [C]; A2 [P] | conditional on OL-S1 (+ OI-6) |
| Conjecture S♯ | computed observation O-MAD only | conjecture; not used |
| Lemma ATT 1.7 (openness) | not written | stated; OI-3 |
| Theorem H′ | H1–H6, MG2 [O], OL-DS [OL], Lemma 1.7 [OI-3], CW′ verification half (for γ_0 = Wilson: Prop. S ⇒ OL-S1), CW′ landing [C8] | conditional |
| O-KP, O-τ, O-MAD, Appendix N | scripts only | computed observations / evidence; nothing depends on them |
| MG0, MG1, MG2, MG3, MG4, MG5 | — | **unclosed** |

## 10. Open items recorded in the editorial pass (not fixed)

* **OI-9.** H6 is unwritten bookkeeping; MG2 is open. Theorem H depends on both.
* **OI-10.** H3 "⇒" was described as "standard" here and as a repo finite-block result in the sketch; both are recorded, neither is
  used by Theorem H (which uses only ⇐, Lemma A2).
* **OI-11.** The H4 constant ("m_sc(β) ≥ −log(c·β)" in the sketch) is not explicit; it is cited, not derived.
* **OI-12.** The previous §9 called the τ_J values a "certified tail" and the variance bound "arb-certified"; relabelled as a
  computed observation and as evidence for Open Lemma OL-S1. See also ATT §6 (OI-1 to OI-8).
* **OI-13.** Lemma A1's assembly and Lemma A3 are outlines; the passage from torus-distance decay to the transfer-operator gap at
  finite time extent L_t (needed for Cor. S′) is not written out (see ATT OI-6).
* **OI-14.** The sketch's former "two no-go checks" wording conflicted with the registry rule; relabelled as scope tests.

## 11. Not claimed

No MG row is closed. The fixed-spacing endpoint of MASS_GAP_LOCAL_BLOCK_ASTRA is unchanged. H5 is used at its finite-volume
literature scope. CW is open and is the Clay-level step. Proposition S is conditional on Open Lemma OL-S1. No computation
supports a proved statement in this unit.

## References (verified in the editorial pass unless flagged)

- K. Osterwalder, E. Seiler, Gauge field theories on a lattice, Ann. Phys. 110 (1978) 440–471.
- M. Lüscher, Construction of a selfadjoint, strictly positive transfer matrix for Euclidean lattice gauge theories,
  Commun. Math. Phys. 54 (1977) 283–292.
- K. Osterwalder, R. Schrader, Commun. Math. Phys. 31 (1973) 83; 42 (1975) 281.
- T. Bałaban, series in Commun. Math. Phys. 95, 96, 98, 99, 102, 109, 116, 119, 122 (1984–1989). (Volumes as listed in PR #10132;
  individual titles and pages not re-checked in this pass.)
- J. Dimock, The renormalization group according to Balaban, I. Small fields, Rev. Math. Phys. 25 (2013) 1330010,
  arXiv:1108.1335 (exposition; later parts of the series not re-checked).
- A. Guth, Existence proof of a nonconfining phase in four-dimensional U(1) lattice gauge theory, Phys. Rev. D 21 (1980) 2291.
- J. Fröhlich, T. Spencer, Massless phases and symmetry restoration in abelian gauge theories and spin systems,
  Commun. Math. Phys. 83 (1982) 411.
- R. L. Dobrushin, The description of a random field by means of conditional probabilities and conditions of its regularity,
  Theory Probab. Appl. 13 (1968) 197–224.
- H. Föllmer, A covariance estimate for Gibbs measures, J. Funct. Anal. 46 (1982) 387–395.
- H.-O. Georgii, Gibbs Measures and Phase Transitions, de Gruyter, 1988, Ch. 8 (theorem numbers not pinned; OI-6).
- R. L. Dobrushin, S. B. Shlosman, Constructive criterion for the uniqueness of Gibbs field, in: J. Fritz, A. Jaffe, D. Szász (eds.),
  Statistical Physics and Dynamical Systems, Progress in Physics 10, Birkhäuser, Boston, 1985, pp. 347–370; and Completely
  analytical Gibbs fields, same volume, p. 371 ff. (Applicability to the present setting unchecked: OL-DS.)
- R. Kotecký, D. Preiss, Cluster expansion for abstract polymer models, Commun. Math. Phys. 103 (1986) 491–498.
- F. Martinelli, E. Olivieri, Approach to equilibrium of Glauber dynamics in the one phase region, I and II, Commun. Math. Phys. 161
  (1994) 447–486 and 487–514.
- S. Chandrasekharan, R. X. Siew, T. Bhattacharya, Monomer-dimer tensor-network basis for qubit-regularized lattice gauge
  theories, Phys. Rev. D 111 (2025) 114502, arXiv:2502.14175. (Author initials corrected from "H. Siew".)
- A. D. Kennedy, B. J. Pendleton, Improved heatbath method for Monte Carlo calculations in lattice gauge theories,
  Phys. Lett. B 156 (1985) 393 (Appendix N only).
- H. D. Kirk, v4 (2 Aug 2026), Zenodo 21765806, as examined in CROSSOVER_LITERATURE_BRIDGE_ASTRA (record existence verified;
  content not re-read in this pass).
