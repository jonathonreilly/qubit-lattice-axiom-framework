# Independent check: BKSF bare-permutation rotation note (C8)

A fresh-context agent (same model family) wrote this check. It wrote its own code from the definitions,
without reading the C8 runner. The agent's tooling could not write `.md` files, so the main session saved
this report from the agent's hand-back text, condensed.

## Verdicts on the first version of the note

| # | Claim | Verdict |
|---|---|---|
| 1 | All 8 sign sectors of all 60 codes are valid | CONFIRMED (L = 4 and L = 6) |
| 2 | Exactly one flux-0 and one flux-pi sector | CONFIRMED; true by construction (wording) |
| 3 | Bare permutation preserves the signed group in those sectors | CONFIRMED (L = 4 all generators; L = 6) |
| 4 | Mixed sectors: 44 of 60 codes need a sign correction | CONFIRMED (L = 4, L = 6) |
| 5 | eta_f(C2, C2) = +1 ("not spinorial") | **REFUTED** |

**Claims 1–4.**
- The hop product around a plaquette is always plus or minus a Hermitian Pauli, never ±i times one.
- Structural reason for claim 3: P_R A^o_e P_R^-1 = A^{Ro}_{Re} exactly. The flux-0 and flux-pi signed
  groups do not depend on the ordering within a class (660/660 each).
- A rotation fails in a mixed sector exactly when it swaps two axes that carry different fluxes.

**Claim 5, method A: pair test** (`pair_test*.py`).
- Put fermions at x and Rx and compute lambda = the sign of S^dag S^R in the signed group. Then
  lambda = theta_f eta_f.
- Calibrations:
  - toric-code boson: +1;
  - toric code in pi background flux: -1 for C2 axes piercing perpendicular plaquettes (Aharonov–Bohm);
  - naive scalar fermion with c_v -> c_{Rv}: -1.
- BKSF: lambda = +1 in all 72 computable (code, C2) pairs. This holds in both sectors, for every tested
  x, and also for C2 axes through edge midpoints and cube centres. So eta_f = -1.

**Claim 5, method B: Majorana form** (`fermion_action.py`).
- In all 72 cases, P_R(A_e) = ± A_{Re} B_tail B_head × (plaquettes).
- This gives c_v -> -i s_v c_{Rv}, so C2^2 = (-1)^F.

**Where the first version's proof failed** (`restriction_test.py`).
- P_R restricted to a region D does not preserve the vacuum: about 500 generators straddling the boundary
  break at L = 8.
- So the restriction is not a valid localization of the symmetry.

**Realization dependence** (`clifford_dressing.py`).
- W = prod_v exp(-i pi B_v/4) is a function of the stabilizers, constant on the code space.
- With it, P_R W gives lambda = -1, so eta_f = +1: the scalar rotation.
- P_R is not a symmetry of the Majorana hopping sum t_e A_e; P_R W is.
- Pauli dressings that respect the group law cannot change the class.

**Coverage.** 36 of the 108 (code, C2) pairs have no ordering whose plaquette span P_R preserves:
- the axis C2 of the order-4 codes;
- the other edge C2 of each order-4 code;
- the edge C2 of 12 single-C2 codes.

There eta_f is not determined (`which_nonsymmetric.py`, `plaquette_span_symmetry.py`).

**Addendum (C8 caveat).**
- For all 144 orderings of the D3 codes, P_R preserves span(S^o) exactly for the identity and one edge C2.
  Each edge C2 serves 4 of the 12 orderings in a class.
- Span preservation always means an exact permutation of the plaquette supports.

**Dirac nodes** (`dirac_nodes.py`).
- Pi-flux complex hopping: E = ±2 sqrt(sum cos^2 k), with 2 nodes and 4 linearly crossing bands each.
  This is two four-component Dirac fermions.
- For the Majorana hopping sum A_e there is one Dirac fermion.

**Citations.**
- The five references were checked by web search and are correct.
- Suggested additions: Susskind PRD 16, 3031 (1977), and the published reference for arXiv:2501.10862,
  PRD 113, 014504 (2026).

## Outcome
The note was rewritten (and renamed) to state eta_f(C2, C2) = -1 under the bare permutation, with the
realization dependence and the coverage made explicit. The C8 runner reproduces the pair test with
independent code: PASS=7.
