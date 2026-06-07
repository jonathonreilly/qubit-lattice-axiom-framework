# Mathematics sector search (Exercise Four) + (iii) shared-substrate / (iv) Record

| Sector | reframe | tool/theorem | how it bounds δv | first artifact |
|---|---|---|---|---|
| representation theory of the lattice/gauge symmetry | classify O_c under the residual symmetry | invariant-ring / Schur | NONE — O_c is a Lorentz SCALAR; only t↔x forbids it (RUN, excluded #3129) | the closure-(i) map |
| single-band tight-binding / "one medium → one sound speed" | all excitations share ONE dispersion | coupled velocity-RG (Chadha–Nielsen; Giuliani et al.) | bounds the COMMON mode (tree degeneracy) but NOT the species difference (loop, Casimir-dependent) | attractor-note Part A |
| spectral graph theory | Z³ has ONE Laplacian → ONE dispersion | graph spectrum | tree-level velocity degeneracy only | the Z³ adjacency spectrum |
| operator algebra (finite Cl(3,0) per site) | finite per-site algebra bounds operator content | finite-dim vN algebra | bounds the basis/support, NOT the mean of a marginal coupling (parallel to Record #3126) | — |
| Ward identities | does gauge invariance tie c_t to c_s? | Ward/Slavnov–Taylor | NO — ties spatial-vertex↔spatial-kinetic and temporal↔temporal separately; the LV direction is outside the constraint row space | rank check (residual 1) |
| KAM/rigidity | is there a torus/integrable structure protecting δv? | KAM | no integrable structure to protect | — |

## TOP-2 (with verdicts)
- **#1 Representation theory — RUN, EXCLUDED (#3129).** O_c is a Lorentz scalar; the only forbidding
  transformation is t↔x (the absent 4th lattice axis). Rep theory cannot bound a singlet.
- **#2 Single-band "one medium → one sound speed" — the compositeness lead, FAILS for the difference.**
  The real condensed-matter fact (all modes share the sound speed) holds for the TREE-level common mode —
  which is the unprotected marginal direction (the overall c is set by the scale primitive). The SPECIES
  splitting rides on `C_F ≠ C_B` (loop, Casimir-dependent): different reps flow at different rates.
  Compositeness equalizes the TREE velocity, not the radiative one.

## (iii) shared-substrate verdict
**Partially — at tree level only, and that part is unobservable.** The one-Z³/one-kernel structure is
STRICTLY STRONGER than generic multi-field (it forces tree-level velocity degeneracy where generic fields
split at tree level), but that degeneracy is the marginal common mode (unprotected anyway). The species
splitting is purely loop-induced and rep-dependent; the shared substrate gives NO extra suppression there.
Net: beats generic at tree level, ties at loop level.

## (iv) Record verdict
**δv IS a genuine record — the "common-c-only" escape fails.** Species-to-species time-of-flight (GRB
photon dispersion, Hughes–Drever nucleon comparison) is a realized finite-sector outcome; it is RELATIONAL
between two species, needs no external frame, and survives the quotient that kills a global phase. #3126
confirms from the other side: Record acts on basis/support/fluctuations, not the mean of a marginal
coupling — and δv IS that mean.
