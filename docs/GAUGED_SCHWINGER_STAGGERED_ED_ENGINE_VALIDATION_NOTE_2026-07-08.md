# Gauged Schwinger Staggered Exact-Diagonalization Engine Validation

**Date:** 2026-07-08
**Type:** meta
**Claim scope:** Machinery validation for one imported finite Hamiltonian
comparator. This note is infrastructure and carries no physics-status
promotion.

**Primary runner:**
[`scripts/gauged_schwinger_staggered_ed_engine_2026_07_08.py`](../scripts/gauged_schwinger_staggered_ed_engine_2026_07_08.py)

**Runner cache:**
[`logs/runner-cache/gauged_schwinger_staggered_ed_engine_2026_07_08.txt`](../logs/runner-cache/gauged_schwinger_staggered_ed_engine_2026_07_08.txt)

## Purpose

The runner validates bookkeeping for a declared \(d=1\) Hamiltonian staggered
fermion comparator with \(U(1)\) links, an electric term, and a ring Gauss-law
reduction to a finite Wilson-line rotor. The model definition is imported. The
checks establish agreement between independent implementations of that finite
model; they do not derive the model from the framework or validate its physical
adequacy.

## Convention Split

The implemented Hamiltonian one-body band is
\[
E(p)=\sqrt{m^2+\sin^2p}.
\]
The two-step transfer band
\(\operatorname{arsinh}\sqrt{m^2+\sin^2p}\) is a different convention.
The runner checks the Hamiltonian band only.

## Machinery Checks

The runner checks:

- charge-zero ring Gauss bookkeeping with staggered charge;
- a finite Wilson-line rotor cutoff;
- two-site magnetic translation on vectors whose support and image remain in
  the cutoff interior;
- the explicitly decoupled \(U_{\rm holo}=1\) free comparator;
- momentum-sector reassembly against the unprojected finite spectrum;
- construction of the finite two-body truncation projector.

The printed sector-energy and projection numbers are non-gating regression
data for those implementations. They are not source-note physics claims or
particle/channel identifications.

## Open Dependencies and Engineering Flags

The following remain explicit:

- the finite Hamiltonian comparator is supplied rather than derived;
- the charge-zero ring sector does not represent every Fock sector;
- finite rotor translation is checked only on its interior domain;
- the exact \(g=0\) holonomy still shifts the rotor, so the free-band test uses
  the decoupled comparator;
- any downstream physical use needs its own source note, dependencies, and
  independent audit.

## Boundaries

- `claim_type: meta`; no theorem, no-go, or bounded physics status is
  proposed by this validation note.
- Sizes and cutoffs are exactly those printed by the runner.
- No equivalence, gravity, WEP, causal attribution, Fock-channel attribution,
  or framework-dynamics derivation is claimed.
- No audit result is predicted.

## Dependencies

None. The finite Hamiltonian is supplied as the object of this machinery test;
the convention comparison is explanatory only and is not a citation-graph
premise.

## Reproduction

```bash
python3 scripts/gauged_schwinger_staggered_ed_engine_2026_07_08.py
```

The cache is regenerated only after the machinery runner is green.
