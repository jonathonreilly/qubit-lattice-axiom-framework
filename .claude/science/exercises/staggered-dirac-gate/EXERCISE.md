# Exercise (full) — staggered-Dirac realization gate

5-subagent fan-out per `docs/ai_methodology/skills/exercise/SKILL.md`. Each agent did
the framework refresher (MINIMAL_AXIOMS_2026-06-05, tier_a_admissions, scale-primitive,
review-loop, controlled-vocab). Condensed below; runner reproduces the verified facts.

## Exercise One — Assumptions ledger (hidden admissions surfaced)
Climbing axioms→blocker, the hidden/implicit assumptions NOT in the 4-substep
decomposition:
- **A4 fermionic statistics (implicit):** substep-1 no-go is statistics-AGNOSTIC
  (hard-core boson = same ungraded M₂(ℂ), dim 2) → FS is an admission, not forced.
- **A5 Euclidean signature/time + Hodge metric (implicit):** d−δ presupposes a
  derivative direction + inner product; no time axiom in {Lattice,Quantum,Record}.
- **A9 chiral ε(x) (implicit):** substep-2/BZ notes mark chirality "out of scope".
- **A7 d=3 vs d=4 fracture:** the 4-taste (16=4·4) reduction is a d=4 fact; the
  substrate is Z³ (8 corners = 1+3+3+1). Conflation flagged.
- **A3 "matter IS the qubit":** forces dim-2 carrier; consistent with #2956.
Routes: R1 signature/time origin; R2 d=3/d=4 fracture; R3 statistics-is-admitted;
R4 reprove Kähler–Dirac natively.

## Exercise Two — Elon reduction (open atom)
Requirement stated too strongly. DELETE: continuum Dirac (permanent lattice),
Kähler–Dirac-equivalence-as-open (now retained_bounded), η-phase-as-atom
(deterministic from spin-diagonalization), Grassmann-from-statistics (no-go).
Smallest object: a single nearest-neighbour link on the Z³ bipartition
(M₂(ℂ)⊗M₂(ℂ)). Problem type: **selector** (which local graded frame). Open atom:
the chirality selector ε(x). Lemma to prove/refute: "{Lattice,Quantum,Record} +
retained graded-locality/spin-statistics force ε(x)=(−1)^{Σx} up to global U(1)/axis
gauge." Presupposes the *unaudited* spin-statistics theorem. Decisive artifact:
one-link chirality-selector enumerator (≥2 survivors ⇒ ε admission; =1 ⇒ forcing).

## Exercise Three — Literature (inspiration only; cited)
- **Nielsen–Ninomiya** (NPB 185/193 1981): NO-GO — translation-invariant local
  bilinear "1 component ⇒ single chiral" is forbidden; staggering evades it by
  breaking single-site translation invariance. Any repo proof must break a premise.
- **Kogut–Susskind** (PRD11 1975; Kawamoto–Smit 1981): spin-diagonalization
  ψ=∏γ^{x}χ ⇒ η_μ(x)=(−1)^{Σ_{ν<μ}x_ν}; 1 Grassmann/site.
- **Becher–Joos** (Z.Phys.C 15:343 1982): staggered ≅ Dirac–Kähler (forms on the
  hypercube). NB d=3 gives 8 (not 16) components — taste count is dimension-specific.
- **Jordan–Wigner**: one qubit = one fermion mode (EXACT) — cleanest one-qubit/site
  bridge; but the JW Z-string is nonlocal (needs an ordering).
- **Catterall (reduced/chiral staggered, arXiv:2010.02290, 2405.03037):**
  ε(x)=(−1)^{Σx} is the U(1)_ε chiral generator, broken to Z₄ (matches the repo
  "chirality grounds structure not magnitude").
- **Karsten–Wilczek (2502.16500):** minimally-doubled, su(2) spin-taste.

## Exercise Four — Math-sector (two verified leads)
- **Lead 1 (group/simplicial cohomology):** η is a Z₂ 1-cochain; curvature dη=−1
  (Clifford 2-cocycle) on every plaquette; unique mod coboundary. VERIFIED (192
  plaquettes). Sidesteps the JW/CAR no-go (η is a c-number cochain).
- **Lead 2 (discrete exterior calculus + Cl(3)):** γ_μ=e∧−ι on Λ(ℂ³), dim
  8=Cl(3)_ℂ, {γ,γ}=−2δ, grading 1,3,3,1, ω²=chirality. VERIFIED. Dirac = the
  qubit's own Clifford action; one qubit = one chiral block.
- Other lenses: Rabin lattice-doubling homology; ABS Cl(n)→KO index; signed-graph
  balance (η = frustrated edge-signing); fermionization functor (universality).

## Exercise Five — Reframing (Record-axiom frame)
Most promising: **D_KS = the durable RECORD of lattice adjacency** (a hop
χ̄_{x+μ}χ_x = the K/CPT-orbit imprint that two sites neighbour) ⇒ the Dirac
operator is record-native, not admitted dynamics; η_μ = the JW recording-ORDER
phase; taste = central-sector read ONCE (like the charged-lepton singlet/doublet),
spin = within-sector. Decisive test: the C₃-equivariant index/character of D_KS on
the hw=1 corner triplet — every irrep multiplicity = 1 (read once → record-native)
vs a plain dimension-trace (taste stays admitted). This is the same
first-order-index vs second-order-modulus fork the Koide-r½ meta-note localized.
