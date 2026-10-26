# Hubble Lane 5 C2: Supplied CKM/PMNS Sign Witnesses

**Date:** 2026-04-29; scope corrected 2026-10-23
**Type:** open_gate
**Status:** finite conditional toy-data separation; physical selector and yield remain open.
**Runner:** `scripts/frontier_hubble_lane5_c2_ckm_pmns_right_sensitive_selector_stretch.py`

## 1. Historical question and current scope

The historical eta candidate gate is a right-sensitive 2-real `Z_3`
doublet-block point-selection law on `dW_e^H = Schur_{E_e}(D_-)`.
The corrected `HUBBLE_LANE5_ETA_RETIREMENT_GATE_AUDIT_NOTE_2026-04-26.md`
withdraws eta retirement and complete C2 closure: selector, supported branch,
and physical yield/readout remain separate obligations. A sign choice is not
a proof that this cascade supplies the observed yield.

The earlier argument promoted this residual to a one-bit physical problem
and asserted that the repository had no cross-sector law. Both claims are
withdrawn here. The complete earlier note, runner and cache are recoverable
at commit `56474903716b057082172f24f00c3dd78373d75b` under the same paths.
The historical negative claim is unproved; it is not a current no-go theorem.

## 2. Explicit supplied data

For real delta and q and a supplied magnitude a > 0, define the toy data

```text
E(delta,q,a) = (delta^2 + q^2, delta^2 q^2, a),
O(delta,a) = (sign(delta), sign(delta) a),  delta != 0.
```

The executable `even_pmns_data` rounds these three numbers to 12 decimals.
They are a minimal stand-in, not a computed PMNS matrix, transport map, or
complete inventory of physical observables. The two executed witnesses use
`delta = +/-sqrt(6)/3`, `q = sqrt(6)/3`, and `a = 2 sqrt(6)/3`.
The even functions agree exactly under delta reversal; the odd sign reverses.
The zero-delta case is excluded from this sign argument.

The independent CKM-side fixture is supplied as
`rho = 1/6`, `eta_CKM = sqrt(5)/6`, `delta_CKM = atan(sqrt(5))`,
on its positive branch. The cited CKM identity has its own imported projector
and radius premises. This runner checks the fixture's arithmetic, not those
physical identifications. It imports no CKM-to-PMNS coupling.

## 3. Conditional implication and its limit

Hold the CKM sign fixed in both witnesses. The ordered input consisting only
of that sign and E is identical, whereas O differs. Therefore a deterministic
function of precisely those identical inputs cannot reproduce both signs.
This is a statement about the supplied data restriction, not all framework
laws or all physically available data.

If the extra rule `sign(A13) = sign(eta_CKM)` is supplied, its defined readout
`sign(eta_CKM) a` selects the positive witness. This rule is a premise, not
an output of the even-data comparison. The code's
`coupling_law_present = False` is a stipulated configuration flag; checking
it proves neither global law absence nor a physical impossibility.

## 4. What the runner checks

The existing numerical expressions, witness values and tolerances are retained.
Documentary checks record phrases in five named input notes, including the
parent's unresolved selector/yield obligation. They do not certify those
notes' broader historical claims. Algebraic checks compare the two witnesses
and the supplied CKM fixture. Configuration checks report the stipulated
absence of a coupling in this toy construction only.

```bash
python3 scripts/frontier_hubble_lane5_c2_ckm_pmns_right_sensitive_selector_stretch.py
```

The declared cap is 120 seconds. PASS counts describe these checks, not a
physical selector, yield, eta retirement, C2 closure or a no-go result.

## 5. Open physical questions

The physical domain, complete data map, cross-sector relation (if any),
selected branch and transport/readout bridge remain unresolved. No uniqueness
or exhaustion claim is made about possible laws. No numerical baryon
asymmetry, Omega_Lambda or H_0 follows from the two-witness calculation.
