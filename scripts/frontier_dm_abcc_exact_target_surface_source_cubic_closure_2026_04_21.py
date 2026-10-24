#!/usr/bin/env python3
"""Finite supplied basin-table comparison; positivity and completeness are not derived."""

from __future__ import annotations

import math
import sys

import numpy as np

from frontier_dm_pmns_upper_octant_source_cubic_selector_theorem_2026_04_20 import (
    H_mat,
    source_cubic,
)
from frontier_dm_wilson_direct_descendant_projected_source_branch_discriminant_theorem_2026_04_18 import (
    delta_src,
    pack_from_h,
)

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ['docs/DM_ABCC_EXACT_TARGET_SURFACE_SOURCE_CUBIC_CLOSURE_THEOREM_NOTE_2026-04-21.md', 'docs/DM_LEPTOGENESIS_NE_PROJECTED_SOURCE_LAW_DERIVATION_NOTE_2026-04-16.md', 'docs/DM_LEPTOGENESIS_NE_PROJECTED_SOURCE_TRIPLET_SIGN_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_PERTURBATIVE_UNIQUENESS_THEOREM_NOTE_2026-04-17.md', 'docs/DM_PMNS_UPPER_OCTANT_SOURCE_CUBIC_SELECTOR_THEOREM_NOTE_2026-04-20.md', 'docs/DM_WILSON_DIRECT_DESCENDANT_FLAGSHIP_FRONTIER_COLLAPSE_THEOREM_NOTE_2026-04-18.md', 'scripts/frontier_dm_pmns_upper_octant_source_cubic_selector_theorem_2026_04_20.py', 'scripts/frontier_dm_wilson_direct_descendant_projected_source_branch_discriminant_theorem_2026_04_18.py', 'scripts/frontier_pmns_theta23_upper_octant_chamber_closure_prediction.py', 'scripts/frontier_sigma_hier_uniqueness_theorem.py']

PASS_COUNT = 0
FAIL_COUNT = 0

E1 = math.sqrt(8.0 / 3.0)

BASINS = {
    "Basin 1": (0.6570613422097703, 0.9338063437590336, 0.7150423295873919),
    "Basin N": (0.501997, 0.853543, 0.425916),
    "Basin P": (1.037883, 1.433019, -1.329548),
    "Basin 2": (28.006188289564736, 20.721831213931072, 5.011599458304925),
    "Basin X": (21.128263668693783, 12.680028023619366, 2.08923480586059),
}


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition




def chamber_margin(point: tuple[float, float, float]) -> float:
    _m, delta, q_plus = point
    return float(delta + q_plus - E1)


def basin_data() -> dict[str, dict[str, float]]:
    out: dict[str, dict[str, float]] = {}
    for name, point in BASINS.items():
        h = H_mat(*point)
        out[name] = {
            "margin": chamber_margin(point),
            "I_src": float(source_cubic(h)),
            "Delta_src": float(delta_src(pack_from_h(h))),
            "det": float(np.linalg.det(np.asarray(h, dtype=complex)).real),
        }
    return out




def main() -> int:
    data=basin_data()
    inside={name for name,row in data.items() if row['margin']>=0}
    selected={name for name in inside if data[name]['I_src']>0}
    check('The supplied table chamber members are 1,2,X', inside=={'Basin 1','Basin 2','Basin X'})
    check('An imposed positive cubic selects Basin 1 in this finite table',selected=={'Basin 1'})
    check('Supplied chamber candidates have matching nonzero cubic/determinant signs',all(data[n]['I_src']*data[n]['det']>0 for n in inside))
    check('Projected scalar matches direct determinant at the supplied chamber rows',abs(data['Basin 1']['Delta_src']-data['Basin 1']['det'])<1e-10 and all(abs(data[n]['Delta_src']-data[n]['det'])<1e-8 for n in ['Basin 2','Basin X']))
    check('N preserves the opposite-sign control',data['Basin N']['I_src']<0 and data['Basin N']['Delta_src']>0)
    check('P preserves the opposite-sign control',data['Basin P']['I_src']>0 and data['Basin P']['Delta_src']<0)
    for n,row in data.items(): print(n,row)
    print('Completeness, physical positivity and chamber selection are not proved by this table.')
    print(f'SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}')
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    sys.exit(main())
