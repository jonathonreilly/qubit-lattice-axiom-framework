# Small CKM vs Large PMNS as Readout-Context Misalignment — Conditional Linear-Algebra Observation

**Date:** 2026-06-06
**Type:** bounded_theorem
**Status:** source-note proposal awaiting independent audit; audit and effective
status are pipeline-owned.
**Primary runner:**
[`scripts/ckm_small_from_record_readout_context_runner.py`](../scripts/ckm_small_from_record_readout_context_runner.py)
**Cache:**
[`logs/runner-cache/ckm_small_from_record_readout_context_runner.txt`](../logs/runner-cache/ckm_small_from_record_readout_context_runner.txt)

## Purpose

The framework has recorded, but not derived, a possible structural contrast
behind small CKM and large PMNS mixing in
[`FLAVOR_BOTH_READINGS_CHARGE_SELECTS_NOTE_2026-05-30`](FLAVOR_BOTH_READINGS_CHARGE_SELECTS_NOTE_2026-05-30.md).
This note isolates the exact conditional linear algebra. It does not convert
finite character profiles into a physical detection, localization, carrier,
or readout theorem.

## Conditional observation

Supply both quark mass operators as diagonal in the same ordered basis,
`U_up = U_dn = I`, and supply the charged-lepton operator in that ordered
basis while the neutrino operator is `C_3`-structured. Then:

- `V_CKM = U_up^dagger U_dn = I` in the exactly aligned case;
- a supplied small rotation of one quark basis gives a near-diagonal Cabibbo
  block;
- a supplied Hermitian circulant neutrino matrix with simple spectrum has the
  full `C_3` character basis as its eigenbasis; relative to the supplied
  charged-lepton basis, every squared-modulus PMNS entry is `1/3` (and hence
  every column is trimaximal).

The shared-circulant permutation result is the exact upstream algebraic fact in
[`QUARK_C3_CIRCULANT_SOURCE_LAW_BOUNDARY_NOTE_2026-04-28`](QUARK_C3_CIRCULANT_SOURCE_LAW_BOUNDARY_NOTE_2026-04-28.md).
The aligned case used here is the identity member of that permutation family.

## Finite character-profile context

The runner also constructs a three-point discrete Fourier basis. For each
Fourier character `f_k` and each coordinate projector `P_j`, it verifies the
positive equality

```text
<f_k, P_j f_k> = 1/3.
```

This is the three-point analogue of the exact `(1/8,...,1/8)` profiles in the
finite translation-character construction consumed through
[`FLAVOR_CARRIER_FROM_AXIOMS_MOMENTUM_FORCED_2026-05-31`](FLAVOR_CARRIER_FROM_AXIOMS_MOMENTUM_FORCED_2026-05-31.md).
The parent is used only for its positive finite profile/projector data and its
open physical-identification boundary.

The equality above compares two explicitly defined finite bases. A physical
generation locus, detector basis, propagation basis, gauge-to-recording map,
or readout observable would require its own authority. The physical identity
of the monitored `C_3` family likewise remains separately scoped in
[`FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02`](FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md).
This note neither supplies nor rules out any such bridge.

## Authority limit

- The quark-basis alignment and neutrino `C_3` structure are supplied
  hypotheses. The theorem is conditional on them.
- The runner establishes exact finite matrix relations only. It assigns no
  physical particle, detector, localization, propagation, or record role to
  either basis.
- Cabibbo/Wolfenstein parameters, CP phases, quark `r` values, and the physical
  PMNS/CKM identification remain outside the proved finite algebra.
- The note adds no axiom, approved primitive, selector, convention, fitted
  value, or physical carrier.

## Runner check map

The runner verifies seven positive finite statements:

1. two supplied circulant eigenbases give a permutation matrix;
2. aligned quark eigenbases give the identity;
3. a supplied small rotation gives the displayed Cabibbo block;
4. the displayed CKM matrix has the reported column profiles;
5. the supplied Hermitian circulant neutrino matrix commutes with `C_3`, has
   simple spectrum, and its eigenbasis consists of three trimaximal columns
   relative to the supplied charged-lepton basis;
6. every squared-modulus entry of the displayed PMNS matrix is `1/3`;
7. every coordinate-projector expectation on the three Fourier characters is
   `1/3` to numerical precision.

Run:

```bash
PYTHONPATH=scripts python3 scripts/ckm_small_from_record_readout_context_runner.py
```

Expected:

```text
TOTAL: PASS=7 FAIL=0
```
