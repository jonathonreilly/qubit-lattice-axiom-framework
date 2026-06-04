# Assumptions And Imports

## Load-Bearing Inputs

- Finite even periodic lattice coordinates already used by the source note.
- Wilson plaquette enumeration already implemented by the verifier.
- Existing SU(3) link construction and temporal-gauge helpers already used by the verifier.

## Retired Import / Blocker Surface

- The source no longer treats `P_mixed` as only the reflection-plane temporal plaquettes on finite periodic `Lambda = (Z/L)^4`.
- The verifier no longer hides the periodic endpoint-sign wraparound family behind the aggregate mixed count.

## New Axioms

None.

## Literature / Textbook Imports

None added. The change is a direct finite-lattice endpoint classification and count check inside the existing framework.
