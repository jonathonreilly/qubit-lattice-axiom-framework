# Campaign results by rung — toe-scale-ladder-20261018

Base: main `584755767`. Every entry below is unaudited author work, reviewed in a separate
agent context by the same model (not an independent audit). Claim types and full scope
are in each block's `NOTE.md`; findings and corrections in its `REVIEW.md`. Formal audit
remains deferred (owner setting). No new axiom or primitive was adopted.

| Rung / bridge | Block | Result (honest status) | Review |
|---|---|---|---|
| R1→R2 records | C3 | Covariant formation with local clocks (incl. neighbour-dependent rates with bounded ratio κ) is a finitary factor of iid: P(R ≥ n+1) ≤ D(D−1)^{n−1} κ^{n+1}/(n+1)!, superexponential mixing, no LRO/criticality for local observables. Map's earlier constant corrected (XOR counterexample). | ready |
| R1→R2 records | C3b | Ergodicity is the wrong hypothesis (checkerboard clock orders trivially). Internal-symmetry order needs infinite ancestries (Thm K); mixing clock + finite ancestries ⇒ mixing record (M); power-law/fractional Gaussian clocks (d=2, H<1), two-stage clocks and λmin=0 bounded-rate clocks give finite ancestries ⇒ no LRO. Open: deterministic-delay mixing clocks; sites that never form. | ready |
| R1→R2 dynamics | C4 | One-qubit, translation-invariant, O-covariant Clifford QCAs (27-cell): counts per action (trivial 528, sign 176, sign-f 32, axis 1, full 1 signed); axis/full: identity only at range 1, identity + 3 periodic involutions at range 2; no gliders under O or T at any range (trace-polynomial theorem). | ready (counts reproduced by independent code; reviewer saw headline counts) |
| R1→R2 dynamics | C4b | Range-4 composite of C4's circuits spreads operators ballistically (radius 4n) — C4's freeze is range ≤ 2 only. Index lemma: O-covariance (any subgroup fixing no vector) ⇒ trivial GNVW flow across every plane. U(1)-charged single particles frozen. | ready |
| R1→R2 dynamics | C4c | Vertex lemma: commuting U(1) gates act diagonally at hull corners; products of O-covariant commuting U(1) layers (covered shapes) are diagonal/identity — every k-magnon sector and density frozen, 13 pair bands flat. Symmetry still allows six face-diagonal pair moves under T (unrealized). | ready |
| R1→R2 dynamics | C4d | Spectator lemma (any range); **P1:** at range 1, T-covariant (axis) or O-covariant U(1) one-qubit QCAs have diagonal pair sectors — pairs exactly static, Observation M unrealizable at range 1 (blind exact elimination reproduced). Range 2: a speed-1 face-diagonal pair glider passes the exact 3-magnon test — open. k=3 clusters at range 1: near-solutions only (‖r‖≈5.5e−7), open. | ready |
| R1→R2 fermion phase | C6 | Twisted BKSF/Majorana/spinful codes satisfy TQO-1/TQO-2 for all L (homological lemma); frustration-free iff L even or flux 0 (F1–F4, all L); emergent point charge is a fermion (−1 exchange); ⇒ BHM uniform gap (conditional on recalled BHM wording) and scoped no-go: no photon / massless fermion by small perturbation. Corner code F5 conditional. | ready (F1–F4) |
| R2→R3 photon | C1 | Stoquastic gauge proved (per sign of g, even L only) and validated at L=2. Winding gap at V=0, L=4–12: pure string tension rejected (rests on L=4), σ = −0.010(15), 1/L consistent but not established; structure-factor/Bragg criteria not evaluable (middle-of-path mixing failure). **Inconclusive.** Follow-up C1b running. | ready (inconclusive) |
| R2→R3 fermions | C7 | Massive 3+1D continuum limit of the two-qubit Dirac walk with explicit O(a·t) error (O(a²) at b_gold / maximal twist); all nodes at TRIMs (under adjacency condition); first genuine Lorentz violation O(a²), cubic anisotropy +0.040/0/0.049. **Repaired main runner defect 8/45→4/45** (commit `f46a89b7b`). | ready |
| R3 chirality | C5 | **Theorem K:** every finite-range translation-invariant unitary walk on Z³ has total three-winding W3 = 0 (K₁(C[Z³]) = C^* ⊕ Z³; second proof via Toeplitz index bundles). Covariant W3 ≠ 0 maps exist only at infinite range. | ready |
| R3 chirality | C5b | **Theorem L / Cor. NN:** at every quasienergy ε, W3 = −Σ_nodes χ + Σ_sheets Φ; with K, node chiralities at each level are balanced by Fermi-sheet flux at that same level — a finite-range walk cannot hide the anomaly partner of a low-energy Weyl node at the cutoff π/a. Free chiral fermions from walks excluded; chirality must come from interactions. | ready |
| R3→R4 Lorentz | C2 | Registered premises do not tie c_γ and c_ψ (explicit witnesses, matter-only reading of kinetic isotropy); full-action hypercubic invariance would (T_tie) but is unregistered primitive content (owner decision). One-loop flow: δ_IR/δ_UV = (α_IR/α_UV)^{(N_f+2)/N_f}, 0.781 over 51 e-folds (N_f=1) ⇒ equality must hold at the cutoff. | ready |
| R3→R4 gravity | C8 | Exact lattice Sakharov coefficient for the Dirac walk under declared (supplied) coupling M1: c_G = 7.3667e-3 (b*), positive TT stiffness; a/l_P = 0.43–0.69 √N_f across four couplings; caveats: ρ_vac −4.03 a⁻⁴, TT q⁰ term −2.39 a⁻⁴, cubic anisotropy, conformal channel not computed. **Repaired main induced-G note** (half-factor: G = 6π/(N_f Λ²); addendum commit `68a504d`). | ready |

## Movement on the ladder (what changed)

- **R1→R2:** record phases under covariant formation are now pinned down: local/mixing clocks
  give no order; order needs infinite ancestries. One-qubit cubic-covariant dynamics: no
  net flow across any plane (all QCAs), no gliders (Clifford), frozen charge sectors for
  commuting U(1) circuits; ballistic operator spreading does exist at range 4.
- **R2→R3:** photon-phase question remains open (C1 inconclusive; C1b in progress). The
  fermion continuum limit is established for the supplied two-qubit walk.
- **R3:** a sharp new obstruction: free finite-range walks cannot carry net chirality,
  not even with the partner parked at the cutoff (K + L). Combined with C6 (emergent
  fermions in stabilizer codes hop by finite-range operators), chiral matter in this
  framework requires interacting dynamics.
- **R3→R4:** light-cone equality and Newton's constant both reduce to cutoff-scale data:
  c_γ = c_ψ must be imposed at the cutoff (or derived from a stronger symmetry the
  owner has not adopted); a/l_P is O(1)·√N_f with an explicit coupling dependence.

## Open decisions for the owner
1. Whether to extend kinetic isotropy to the gauge sector (would tie light cones, T_tie).
2. Whether to accept the two main-surface repairs (`f46a89b7b`, `68a504d`) in a PR.
