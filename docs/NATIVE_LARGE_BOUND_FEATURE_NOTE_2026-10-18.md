# A large neutral feature without a new interaction

**Status:** bounded-support.
**Claim type:** bounded_theorem.
**Primary runner:** [scripts/native_large_bound_feature.py](../scripts/native_large_bound_feature.py)

The existing one-qubit Hamiltonian's complete compact four-wall first-order graph has a unique binding threshold at b=cos(Qy/2) in the certified interval (0.2347569009270,0.2347569009271), for Qx=Qz=0. Approaching that momentum from the bound side gives an exponentially small binding gap and a diverging transverse size. No extra interaction or prescribed binding potential is used.

The original bond readout also has a derived nonzero overlap. Its positive coefficient-model weight shrinks as lambda² W0 delta log²(1/delta), with W0 approximately0.02574494 and delta the binding gap. The large feature is mainly two spin flips coherently separated across many sites; it is not a growing number of constituent flips. Its physical rest excitation remains near8J, and this is not yet a relativistic or gravitational scalar.

The proof and assumption ledger (`outputs/neutral_continuation5_review_2026_10_18/proofs/pr9776/LARGE_BOUND_FEATURE_PROOF.md`) give the exact cavity reduction, interval threshold/source certificate, size and weight asymptotics, and focused independent checks. Inputs and numerical controls are exposed development material. Selection of the Hamiltonian, weak ordered regime, momentum and physical measurement interpretation remains conditional. Full-H transfer near the shrinking gap requires a separate controlled joint limit.


## Source and execution boundary

The full mathematical sources and owning-head helpers are portable literal inputs. Supplied Hamiltonian, state and momentum families, observable interpretation and limits remain explicit. The primary performs only its stated finite controls, with an enforced aggregate cap, immediate child diagnostics and fresh isolated outputs. Historical saved numbers and reviewer verdicts are provenance, never fresh execution or audit authority. No full-H pole, lifetime, universal force or empirical identification follows merely from a finite control.
