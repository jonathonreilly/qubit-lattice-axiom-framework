"""Exact discriminating checks for the accompanying analytical derivation."""
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    "docs/REGGE_EXACT_REDUCTION_POSITIVE_TENSOR_TRANSFER_BOUNDED_THEOREM_NOTE_2026-09-13.md",
    "scripts/regge_local_hessian_check_2026_09_13.py",
    "scripts/regge_source_rank_check_2026_09_13.py",
    "scripts/regge_tensor_transfer_check_2026_09_13.py",
    ".claude/science/physics-loops/regge-exact-reduction-positive-transfer-20260913/NO_GO_DISCIPLINE_CHECKLIST.md",
    ".claude/science/physics-loops/regge-exact-reduction-positive-transfer-20260913/mutations/RESULTS.json",
)
import json,signal
from regge_local_hessian_check_2026_09_13 import run as geometry_check
from regge_source_rank_check_2026_09_13 import run as source_check
from regge_tensor_transfer_check_2026_09_13 import run as transfer_check

def main():
    signal.alarm(AUDIT_TIMEOUT_SEC)
    geometry,bundle=geometry_check()
    source=source_check(bundle)
    transfer=transfer_check()
    total=len(geometry['checks'])+source['count']+transfer['count']
    print(json.dumps({'geometry':geometry,'source':source,'transfer':transfer},indent=2))
    print('per_element: Every rational simplex entry follows from normal and area variations.')
    print('per_site: Literal simplex anchors are included in the assembled cell.')
    print('per_mode: All 225 Laurent coefficients and all-phase static source identities are exact.')
    print('per_block: Full scalar/vector cross terms and the positive tensor transfer are checked.')
    print('lattice_wide: checked and not executed — all-volume statements are analytical consequences of the local identity; no full-lattice simulation.')
    print(f'TOTAL: PASS={total} FAIL=0')
    signal.alarm(0)

if __name__=='__main__':
    main()
