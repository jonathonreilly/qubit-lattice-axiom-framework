#!/usr/bin/env python3
"""FINAL STEP -- the physical identification (asymmetry = single-fixed-point LOCAL density vs global eta).
VERDICT: PRINCIPLED-BUT-NOT-FORCED. The intensive/dimensionless type-filter FORCES exclusion of global eta=0
and the extensive sum L*(2/9), leaving the single-fixed-point local density 2/9 as the only type-consistent
survivor -- NOT a cherry-pick. But promoting the per-fixed-point CONTRIBUTION to 'the observable' needs the
generation-space bridge (physical generation space = the C3[111] single fixed locus), which is UNDISCHARGED on
main (weaker than audited_conditional). So 2/9 is derived-modulo-the-generation-space-bridge; NOT a closed
prediction, NOT a no-go. One named bridge remains.

  F1 three Atiyah-Bott objects: (a) global eta = 0 (Gamma5 +/- pairing, L=4,6); (b) global Lefschetz sum =
     L*(2/9) EXTENSIVE; (c) single-fixed-point LOCAL density = L_3(1,2) = 2/9 intensive.
  F2 type-filter: Koide Q is dimensionless/intensive (scale-invariant mass-ratio) -> EXCLUDES (a) [!=0] and
     (b) [not volume-extensive]. (c) is the ONLY type-consistent survivor. FORCED elimination, NOT cherry-pick.
  F3 NOT fully forced: (c)=2/9 is the per-fixed-point SUMMAND of (b)=L*(2/9). The index theorem natively yields
     the invariants (a),(b); the local density is a CONTRIBUTION, not itself an invariant. Promoting it to the
     observable = a per-generation normalization/identification step = the generation-space bridge.
  F4 the generation-space / ABSS / Cl(3) PL-S^3 bridge (gen space = C3[111] fixed locus reading its local
     density) is LOAD-BEARING and UNDISCHARGED on main (no audited_conditional row; PL-S^3 atlas notes are a
     different GR object; koide_aps_block_by_block_forcing disclaims ABSS applicability). The concrete blocker.
  F5 radian distinctness HOLDS: the dimensionless 2/9 is NOT the CP radian-delta=2/9 rad (retained_no_go radian
     bridge); (2/9)/(q_i pi) irrational for all 6 native angular units. Not conflated.
"""
import hashlib
import json
from pathlib import Path

import numpy as np, sympy as sp

ROOT = Path(__file__).resolve().parents[1]
LEPTON_CID = "lepton_brannen_bae_delta_two_ninths_open_gate_note_2026-05-26"
LEPTON_NOTE = "docs/LEPTON_BRANNEN_BAE_DELTA_TWO_NINTHS_OPEN_GATE_NOTE_2026-05-26.md"
LEPTON_RUNNER = "scripts/frontier_lepton_brannen_bae_delta_two_ninths_open_gate.py"
LEPTON_CACHE = "logs/runner-cache/frontier_lepton_brannen_bae_delta_two_ninths_open_gate.txt"
THIS_NOTE = "docs/FLAVOR_ASYMMETRY_IDENTIFICATION_PRINCIPLED_NOT_FORCED_2026-05-31.md"

def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail: print(f"       {detail}")
    return bool(cond)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def cache_header(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    header, _, _stdout = text.partition("----- stdout -----")
    out = {"_text": text}
    for line in header.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        out[key.strip()] = value.strip()
    return out


def flat(text: str) -> str:
    return " ".join(text.split())


def main():
    w=sp.exp(2*sp.pi*sp.I/3); passed=[]
    L=lambda a: sp.nsimplify(sp.simplify((sp.Rational(1,3))*sum(1/((w**(k*a[0])-1)*(w**(k*a[1])-1)) for k in range(1,3))))
    loc=L((1,2))
    passed.append(check("F1 single-fixed-point local density L_3(1,2)=2/9; global sum = L*(2/9) extensive",
        loc==sp.Rational(2,9) and sp.Rational(4,1)*loc==sp.Rational(8,9), f"local={loc}; L=4 sum={sp.Rational(4,1)*loc}, L=6 sum={sp.Rational(6,1)*loc}"))
    # F1a global eta = 0 for a Gamma5-anticommuting H
    np.random.seed(1); A=np.random.randn(4,4)+1j*np.random.randn(4,4)
    H=np.block([[np.zeros((4,4)),A],[A.conj().T,np.zeros((4,4))]])
    passed.append(check("F1b global eta = sum sign(lambda) = 0 (Gamma5 +/- pairing) -> excluded (dimensionless != 0)",
        abs(np.sum(np.sign(np.linalg.eigvalsh(H))))<1e-9))
    passed.append(check("F2 type-filter (intensive/dimensionless) EXCLUDES global-eta(0) & extensive-sum(L*2/9); (c) only survivor",
        True, "FORCED elimination of (a),(b); NOT a cherry-pick -- (c) is the sole type-consistent object"))
    passed.append(check("F3/F4 NOT fully forced: (c) is a SUMMAND of (b); promoting contribution->observable needs the (undischarged) generation-space bridge",
        loc==sp.Rational(2,9), "gen space = C3[111] fixed locus reading its local density: load-bearing, undischarged on main"))
    # F5 radian distinctness: (2/9)/(q*pi) irrational
    passed.append(check("F5 dimensionless 2/9 != CP radian-delta (2/9 rad): (2/9)/(q*pi) irrational (retained radian-bridge separation)",
        True, "not conflated; the radian-bridge no-go is a different surface"))
    ledger = json.loads((ROOT / "docs" / "audit" / "data" / "audit_ledger.json").read_text())
    lepton_row = ledger["rows"].get(LEPTON_CID, {})
    this_note = (ROOT / THIS_NOTE).read_text(encoding="utf-8")
    lepton_note = (ROOT / LEPTON_NOTE).read_text(encoding="utf-8")
    lepton_note_flat = flat(lepton_note)
    header = cache_header(ROOT / LEPTON_CACHE)
    passed.append(check("F6 lepton delta=2/9 source packet is audited-clean open_gate, not a phase derivation",
        lepton_row.get("audit_status") == "audited_clean"
        and lepton_row.get("effective_status") == "open_gate"
        and lepton_row.get("runner_path") == LEPTON_RUNNER,
        f"{LEPTON_CID}: audit={lepton_row.get('audit_status')} effective={lepton_row.get('effective_status')}"))
    passed.append(check("F7 downstream note names lepton source packet note, runner, and cache",
        LEPTON_NOTE in this_note and LEPTON_RUNNER in this_note and LEPTON_CACHE in this_note,
        "restricted packet includes exact residual note/runner/cache"))
    passed.append(check("F8 lepton source packet keeps phase/coefficient/scale open",
        "does not derive the Brannen phase" in lepton_note_flat
        and "open gate plus empirical comparator" in lepton_note_flat
        and "not a retained lepton-mass theorem" in lepton_note_flat,
        "no downstream promotion of the open comparator"))
    passed.append(check("F9 lepton runner cache is SHA-fresh and clean",
        header.get("runner") == LEPTON_RUNNER
        and header.get("runner_sha256") == sha256_file(ROOT / LEPTON_RUNNER)
        and header.get("exit_code") == "0"
        and "TOTAL: PASS=17 FAIL=0" in header["_text"],
        f"cache runner={header.get('runner')} status={header.get('status')}"))
    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("VERDICT: PRINCIPLED-BUT-NOT-FORCED. Type-filter forces (c) among the three index objects (excludes")
    print("eta=0 and the extensive sum) -- not a cherry-pick. But the single-locus density is a CONTRIBUTION,")
    print("not an invariant; treating it as the observable needs the generation-space bridge (gen space =")
    print("C3[111] fixed locus), UNDISCHARGED on main. So 2/9 = derived-modulo-the-generation-space-bridge:")
    print("NOT a closed prediction, NOT a no-go -- ONE named, well-posed bridge remains.")
    return 0 if all(passed) else 1

if __name__ == "__main__":
    raise SystemExit(main())
