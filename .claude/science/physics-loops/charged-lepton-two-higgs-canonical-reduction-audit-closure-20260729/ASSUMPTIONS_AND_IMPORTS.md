# Assumptions and Imports

| Item | Role | Class | Load-bearing? | Disposition |
|---|---|---|---:|---|
| `C`, distinct `a,b in Z_3`, diagonal `D_a,D_b` | theorem domain | supplied finite data | yes | explicit hypothesis |
| diagonal `U(1)^3_left x U(1)^3_right` action | defines quotient | specified mathematical equivalence | yes | explicit hypothesis |
| exact integer arithmetic | proves lattice and torus statements | standard mathematical machinery | yes | implemented twice |
| SymPy rank/nullspace/Smith routines | first certificate route | local software machinery | no for the independent route | cross-checked |
| physical charged-lepton/Higgs/gauge interpretation | would broaden theorem | unsupported physical import | no | expressly excluded |
| observation, fit, literature value, or normalization | none | absent | no | not used |

Counterfactual pass:

- Changing the relative permutation from a nontrivial 3-cycle exits the
  theorem and is tested by identity and transposition controls.
- Removing the all-nonzero condition moves to one of 63 separately enumerated
  support strata; it does not preserve the product-phase coordinate.
- Replacing the specified torus action changes the incidence matrix and would
  require a different theorem; no physical equivalence is inferred.
- Relabeling the two cycle orientations only permutes diagonal coefficients
  and is handled by the displayed conjugator.

There are no open imports inside the quantified formal claim.
