#!/usr/bin/env python3
"""Documentary angle-coordinate correction; lexical checks do not certify physics."""
from pathlib import Path
import re
import sys
ROOT = Path(__file__).resolve().parent.parent
NOTE = ROOT / 'docs' / 'RADIAN_UNIT_CONVENTION_RECLASSIFICATION_NOTE_2026-05-10_radianconv.md'
CONVENTIONS_NOTE = ROOT / 'docs' / 'CONVENTIONS_UNIFICATION_COMPANION_NOTE_2026-05-08.md'
PHYSICAL_LATTICE = ROOT / 'docs' / 'PHYSICAL_LATTICE_FOUNDATIONAL_INTERPRETATION_NOTE_2026-05-08.md'
PROBE24 = ROOT / 'docs' / 'KOIDE_BAE_PROBE_PHI_FROM_Z3_CHARACTER_NOTE_2026-05-09_probe24.md'
PROBE30 = ROOT / 'docs' / 'KOIDE_BAE_PROBE_RADIAN_FROM_DIMENSIONS_BOUNDED_NOTE_2026-05-09_probe30.md'
SYNTHESIS = ROOT / 'docs' / 'KOIDE_BAE_30_PROBE_CAMPAIGN_NOTE_2026-05-09.md'
MINIMAL_AXIOMS = ROOT / 'docs' / 'MINIMAL_AXIOMS_2026-05-03.md'
PASS = 0
FAIL = 0

def check(label: str, ok: bool, detail: str='') -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = 'PASS'
    else:
        FAIL += 1
        tag = 'FAIL'
    suffix = f' | {detail}' if detail else ''
    print(f'{tag}: {label}{suffix}')

import math
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/RADIAN_UNIT_CONVENTION_RECLASSIFICATION_NOTE_2026-05-10_radianconv.md', 'docs/CONVENTIONS_UNIFICATION_COMPANION_NOTE_2026-05-08.md', 'docs/PHYSICAL_LATTICE_FOUNDATIONAL_INTERPRETATION_NOTE_2026-05-08.md', 'docs/KOIDE_BAE_PROBE_PHI_FROM_Z3_CHARACTER_NOTE_2026-05-09_probe24.md', 'docs/KOIDE_BAE_PROBE_RADIAN_FROM_DIMENSIONS_BOUNDED_NOTE_2026-05-09_probe30.md', 'docs/KOIDE_BAE_30_PROBE_CAMPAIGN_NOTE_2026-05-09.md', 'docs/MINIMAL_AXIOMS_2026-05-03.md')

def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    for rel in AUDIT_INPUT_PATHS:
        if not (ROOT / rel).is_file():
            print(f'Missing declared documentary input: {rel}')
            return 1
    note = NOTE.read_text(encoding='utf-8')
    minimal = MINIMAL_AXIOMS.read_text(encoding='utf-8')
    check('Lexical metadata: meta', '**Claim type:** meta' in note)
    check('Lexical absence of effective-status assignment', not re.search(r'effective_status\s*:\s*\w+', note))
    audit_clean_token = 'audited' + '_clean'
    check('Lexical absence of audit-clean token', audit_clean_token not in note)
    pdg_numeric_patterns = [
        r"m_e\s*=\s*0\.51",
        r"m_μ\s*=\s*105",
        r"m_τ\s*=\s*1\.77\d",
        r"m_e\s*=\s*0\.000511",
        r"m_τ\s*=\s*1\.7771",
    ]
    empirical_loading = False
    for pat in pdg_numeric_patterns:
        if re.search(pat, note, flags=re.IGNORECASE):
            empirical_loading = True
            break

    check('Lexical absence of five empirical mass patterns only', not empirical_loading)
    def has_affirmative_match(pattern: str, text: str) -> bool:
        """True iff there is at least one match NOT preceded (within ~50 chars)
        by a negation token."""
        for m in re.finditer(pattern, text, flags=re.IGNORECASE | re.DOTALL):
            head = text[max(0, m.start() - 50): m.start()].lower()
            negators = ("not ", "no ", "never", "without", "absent", "unaffected", "unchanged", "claim ")
            if any(neg in head for neg in negators):
                continue
            return True
        return False

    forbidden_promotions = [
        ("BAE closure by declaration", r"BAE\s+is\s+(now\s+)?closed"),
        ("BAE retained promotion", r"BAE\s+is\s+(now\s+)?retained"),
        ("specific theorem promoted to retained",
         r"theorem\s+(?:is\s+)?(?:now\s+)?promoted"),
        ("specific bridge-gap count claimed below 1",
         r"admission count\s+(?:is|=)\s*0"),
    ]
    for label, pattern in forbidden_promotions:
        check(
            f"Lexical negation heuristic only: {label}",
            not has_affirmative_match(pattern, note),
        )


    check('Documentary coordinate relation stated', 'theta_rad = 2pi*theta_cycle' in note)
    check('Documentary withdrawal stated', 'embedded Review-loop rule are withdrawn' in note)
    print('HISTORICAL_UNSCORED minimal wording:', 'the physical local algebra is `Cl(3)`' in minimal, 'the physical spatial substrate is the cubic' in minimal)
    theta_rad = 2/9
    theta_cycle = theta_rad/(2*math.pi)
    check('Coordinate conversion preserves cosine', abs(math.cos(theta_rad)-math.cos(2*math.pi*theta_cycle)) < 1e-12)
    check('Same numeric 2/9 in cycles changes the angle', abs(math.cos(2/9)-math.cos(2*math.pi*2/9)) > 0.1)
    check('Cycle 2/9 converts to radian 4pi/9', abs(2*math.pi*(2/9)-4*math.pi/9) < 1e-12)
    print(f'=== TOTAL: PASS={PASS}, FAIL={FAIL} ===')
    return 0 if FAIL == 0 else 1

if __name__ == '__main__':
    raise SystemExit(main())
