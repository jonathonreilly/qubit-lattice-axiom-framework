"""Portable replay entry point for six qualified emitter calculation bodies.

Portability review and actual execution are separate gates. Importing this
module does not execute a scientific body or change the process CPU limit.
Only main() starts the planned shared CPU120/wall120 canonical calculation.
Historical reports and caps remain explicitly historical; canonical execution
reproduces their finite checks and supplies no new independent theorem review.
"""
from pathlib import Path
from fractions import Fraction
import hashlib
import json
import resource
import time

from product_seed_emitter_local_2026_10_17 import run_local_author, run_local_reviewer
from product_seed_emitter_installed_2026_10_17 import run_installed_author, run_installed_reviewer
from product_seed_emitter_weighted_2026_10_17 import run_weighted_author, run_weighted_reviewer

AUDIT_TIMEOUT_SEC = 120
REPO = Path(__file__).resolve().parents[1]

# Current landing identities are separate from immutable historical artifact pins.
LANDING_BINDING = 'outputs/control_landing_2026_10_17/LANDING_SOURCE_BINDING.json'
def landing_artifact_bytes(path):
    rel = path.resolve().relative_to(REPO.resolve()).as_posix()
    binding = json.loads((REPO / LANDING_BINDING).read_text())
    raw = path.read_bytes()
    if rel not in binding['files']:
        return raw
    row = binding['files'][rel]
    assert len(raw) == row['current']['bytes'] and hashlib.sha256(raw).hexdigest() == row['current']['sha256'], rel
    original = REPO / row['original_snapshot']
    original.resolve().relative_to(REPO.resolve())
    old = original.read_bytes()
    assert len(old) == row['original']['bytes'] and hashlib.sha256(old).hexdigest() == row['original']['sha256'], rel
    return old

INPUT_ROOT = REPO / 'outputs/product_seed_emitter_2026_10_17_inputs'


class FrozenInputs:
    """Resolve only declared logical identities to hash-checked local bytes.

    Historical absolute strings are lookup keys, never filesystem fallbacks.
    read_text decodes the exact checked bytes as UTF-8. The class has no write
    method, no network access and no directory or undeclared-path fallback.
    """

    def __init__(self, repo, table_path):
        self.repo = Path(repo).resolve()
        self.table = json.loads(Path(table_path).read_text(encoding='utf-8'))
        self.reads = []

    def read_bytes(self, role, logical):
        row = self.table['roles'][role]['aliases'][str(logical)]
        rel = Path(row['path'])
        assert not rel.is_absolute() and '..' not in rel.parts and rel.as_posix() == row['path']
        path = self.repo / rel
        assert path.is_file() and not path.is_symlink(), row['path']
        assert not any(parent.is_symlink() for parent in path.parents if parent != self.repo and self.repo in parent.parents)
        path.resolve().relative_to(self.repo)
        raw = landing_artifact_bytes(path)
        assert len(raw) == row['bytes'], row['path']
        assert hashlib.sha256(raw).hexdigest() == row['sha256'], row['path']
        self.reads.append({'role': role, 'logical_identity': str(logical), 'path': row['path'], 'sha256': row['sha256']})
        return raw

    def read_text(self, role, logical):
        return self.read_bytes(role, logical).decode('utf-8')

    def original_program_bytes(self, role):
        return self.read_bytes(role, '__original_program__')

    def shared_limits(self):
        return {'cpu_soft_hard_seconds': list(resource.getrlimit(resource.RLIMIT_CPU)),
                'external_wall_cap_seconds': AUDIT_TIMEOUT_SEC,
                'wall_enforcement': 'Required canonical runner_cache execution; this class does not enforce wall time.'}

    def execution_metadata(self, role):
        return {'source_role': role,
                'historical_source_run_limits': self.table['roles'][role]['historical_limits'],
                'actual_shared_process_limits': self.shared_limits(),
                'source_statement_scope': 'Original report scope/limitations strings retain their historical scientific meaning. This is a portable replay, not a new review.',
                'original_program_sha256': self.table['roles'][role]['aliases']['__original_program__']['sha256']}


def verify_artifacts():
    manifest = json.loads((INPUT_ROOT / 'ARTIFACT_MANIFEST.json').read_text())
    for row in manifest['files']:
        rel = Path(row['path'])
        assert not rel.is_absolute() and '..' not in rel.parts
        path = REPO / rel
        assert path.is_file() and not path.is_symlink(), row['path']
        path.resolve().relative_to(REPO)
        raw = landing_artifact_bytes(path)
        assert len(raw) == row['bytes'] and hashlib.sha256(raw).hexdigest() == row['sha256'], row['path']


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
    started = time.monotonic()
    landing_artifact_bytes(REPO / 'docs/PRODUCT_SEED_EMITTER_BOUNDED_THEOREM_NOTE_2026-10-17.md')
    verify_artifacts()
    inputs = FrozenInputs(REPO, INPUT_ROOT / 'INPUT_MAP.json')
    reports = {
        'local_author': run_local_author(inputs),
        'local_reviewer': run_local_reviewer(inputs),
        'installed_author': run_installed_author(inputs),
        'installed_reviewer': run_installed_reviewer(inputs),
        'weighted_author': run_weighted_author(inputs),
        'weighted_reviewer': run_weighted_reviewer(inputs),
    }
    # New wrapper consistency guards compare independently returned exact
    # quantities; they do not replace the complete preserved calculations.
    initial = reports['installed_author']['conditional_complete_output']
    initial_check = reports['installed_reviewer']['independent_uniform_enclosures']
    weighted = reports['weighted_author']['weighted_constants']
    weighted_check = reports['weighted_reviewer']['derived_bounds']
    assert initial['onset'] == 10**72 and initial['finite_horizon'] == 2*10**72
    assert initial['finite_clock_sites'] == 5*10**73
    assert Fraction(initial['complete_isometry_error']['exact_rational']) == Fraction(initial_check['all_future_error']['exact'])
    assert Fraction(initial['complete_isometry_error']['exact_rational']) < Fraction(4, 1000)
    assert reports['weighted_author']['time_and_clock']['onset'] == 10**36
    assert reports['weighted_author']['time_and_clock']['Tobs'] == 2*10**36
    assert reports['weighted_author']['time_and_clock']['M'] == 5*10**37
    assert Fraction(weighted['complete_isometry_at_onset']['exact_rational']) == Fraction(weighted_check['complete_at_T']['exact'])
    assert Fraction(weighted['finite_complete_isometry_upper']['exact_rational']) == Fraction(weighted_check['finite_complete']['exact'])
    assert Fraction(weighted['complete_isometry_at_onset']['exact_rational']) < Fraction(4, 1000)
    assert Fraction(weighted['finite_complete_isometry_upper']['exact_rational']) < Fraction(5, 1000)
    assert len(reports['installed_author']['physical_point_diagnostics_not_interval_proof']) == 12
    output = {
        'scope': 'Canonical replay of six source-exposed finite calculation bodies; original source qualifications and complete analytical proofs remain separate.',
        'reports': reports,
        'actual_combined_process_limits': inputs.shared_limits(),
        'elapsed_seconds': time.monotonic()-started,
        'input_sha256': {name: hashlib.sha256((REPO/name).read_bytes()).hexdigest() for name in AUDIT_INPUT_PATHS},
        'resolved_reads': inputs.reads,
        'limits': 'No calibration/joint coefficient box, new preparation assumption, optimizer, time evolution, resonance quadrature, hardware realization or independent retained audit.'}
    (REPO / 'outputs/product_seed_emitter_2026_10_17.json').write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps({'scope': output['scope'], 'function_bodies_completed': len(reports),
                      'initial_onset': initial['onset'], 'weighted_onset': 10**36,
                      'initial_complete_error': initial['complete_isometry_error'],
                      'weighted_complete_error': weighted['complete_isometry_at_onset'],
                      'weighted_finite_complete_error': weighted['finite_complete_isometry_upper'],
                      'actual_combined_process_limits': output['actual_combined_process_limits']}, indent=2))


AUDIT_INPUT_PATHS = ('docs/EMITTER_COUPLING_FAMILY_BOUNDED_THEOREM_NOTE_2026-10-17.md', 'docs/PRODUCT_SEED_EMITTER_BOUNDED_THEOREM_NOTE_2026-10-17.md', 'docs/REAL_CONTROL_AUTONOMOUS_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md', 'docs/STRUCTURAL_COEFFICIENT_BOX_BOUNDED_THEOREM_NOTE_2026-10-17.md', 'docs/THERMAL_RESONANCE_HALT_BOUNDED_THEOREM_NOTE_2026-10-17.md', 'docs/TWO_BODY_AUTONOMOUS_HALT_BOUNDED_THEOREM_NOTE_2026-10-17.md', 'outputs/control_landing_2026_10_17/LANDING_SOURCE_BINDING.json', 'outputs/control_landing_2026_10_17/originals/EMITTER_COUPLING_FAMILY_BOUNDED_THEOREM_NOTE_2026-10-17.md', 'outputs/control_landing_2026_10_17/originals/PRODUCT_SEED_EMITTER_BOUNDED_THEOREM_NOTE_2026-10-17.md', 'outputs/control_landing_2026_10_17/originals/REAL_CONTROL_AUTONOMOUS_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md', 'outputs/control_landing_2026_10_17/originals/STRUCTURAL_COEFFICIENT_BOX_BOUNDED_THEOREM_NOTE_2026-10-17.md', 'outputs/control_landing_2026_10_17/originals/THERMAL_RESONANCE_HALT_BOUNDED_THEOREM_NOTE_2026-10-17.md', 'outputs/control_landing_2026_10_17/originals/TWO_BODY_AUTONOMOUS_HALT_BOUNDED_THEOREM_NOTE_2026-10-17.md', 'outputs/control_landing_2026_10_17/originals/emitter_coupling_family_2026_10_17.py', 'outputs/control_landing_2026_10_17/originals/product_seed_emitter_2026_10_17.py', 'outputs/control_landing_2026_10_17/originals/real_control_autonomous_output_2026_10_17.py', 'outputs/control_landing_2026_10_17/originals/structural_coefficient_box_2026_10_17.py', 'outputs/control_landing_2026_10_17/originals/thermal_resonance_halt_2026_10_17.py', 'outputs/control_landing_2026_10_17/originals/two_body_autonomous_halt_2026_10_17.py', 'outputs/product_seed_emitter_2026_10_17_inputs/ARTIFACT_MANIFEST.json', 'outputs/product_seed_emitter_2026_10_17_inputs/EMBEDDED_SOURCE_MAP.json', 'outputs/product_seed_emitter_2026_10_17_inputs/INPUT_MAP.json', 'outputs/product_seed_emitter_2026_10_17_inputs/SOURCE_INVENTORY.json', 'outputs/product_seed_emitter_2026_10_17_inputs/SOURCE_INVENTORY.md', 'outputs/product_seed_emitter_2026_10_17_inputs/draft_history/DRAFT_VERIFICATION.json', 'outputs/product_seed_emitter_2026_10_17_inputs/draft_history/EMBEDDED_SOURCE_MAP.json', 'outputs/product_seed_emitter_2026_10_17_inputs/draft_history/FREEZE.json', 'outputs/product_seed_emitter_2026_10_17_inputs/draft_history/INTEGRATION_PLAN.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/draft_history/PROGRAM_INPUTS.json', 'outputs/product_seed_emitter_2026_10_17_inputs/draft_history/SOURCE_INVENTORY.json', 'outputs/product_seed_emitter_2026_10_17_inputs/draft_history/SOURCE_INVENTORY.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_context/CLAIM_STATUS.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_context/REVIEW_LOOP_PR_CONFORMANCE_SPEC.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_context/SCIENCE_WORKFLOW.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_context/TWO_BODY_AUTONOMOUS_HALT_BOUNDED_THEOREM_NOTE_2026-10-17.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/autonomous_emitter_route/ALGEBRA_CERTIFICATE.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/autonomous_emitter_route/EXECUTION.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/autonomous_emitter_route/FREEZE.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/autonomous_emitter_route/LITERATURE_NOTES.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/autonomous_emitter_route/ROUTE.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/autonomous_emitter_route/SOURCE_MANIFEST.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/autonomous_emitter_route/algebra.stderr', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/autonomous_emitter_route/algebra.stdout', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/autonomous_emitter_route/emitter_algebra_check.py', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/autonomous_emitter_route/inputs/INTERVAL_CANDIDATE.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/autonomous_emitter_route/inputs/PREPARATION_NEXT_DECISION.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/autonomous_emitter_route/inputs/PREPARATION_SOURCE_SEARCH.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/autonomous_emitter_route/inputs/THEOREM_V2.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_independent_review/EXECUTION.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_independent_review/FILE_MANIFEST.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_independent_review/FREEZE.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_independent_review/REPORT.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_independent_review/RESULTS.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_independent_review/SOURCE_PINS.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_independent_review/check.stderr', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_independent_review/check.stdout', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_independent_review/check_emitter.py', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_independent_review/run_check.py', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_independent_review/sources/author/ALGEBRA_CERTIFICATE.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_independent_review/sources/author/EXECUTION.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_independent_review/sources/author/FREEZE.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_independent_review/sources/author/LITERATURE_NOTES.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_independent_review/sources/author/ROUTE.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_independent_review/sources/author/SOURCE_MANIFEST.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_independent_review/sources/author/algebra.stderr', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_independent_review/sources/author/algebra.stdout', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_independent_review/sources/author/emitter_algebra_check.py', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_independent_review/sources/author/inputs/INTERVAL_CANDIDATE.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_independent_review/sources/author/inputs/PREPARATION_NEXT_DECISION.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_independent_review/sources/author/inputs/PREPARATION_SOURCE_SEARCH.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_independent_review/sources/author/inputs/THEOREM_V2.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_independent_review/sources/generic_review/REVIEW.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_independent_review/sources/interval_review/FREEZE.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_independent_review/sources/interval_review/REVIEW.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_independent_review/sources/process/SCIENCE_WORKFLOW.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_independent_review/sources/root/QUALIFICATION.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_certificate/CANDIDATE.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_certificate/CAPS.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_certificate/CERTIFICATE.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_certificate/FREEZE.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_certificate/RUNTIME_IDENTITIES.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_certificate/SOURCE_MANIFEST.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_certificate/certify_installed_emitter.py', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_certificate/inputs/autonomous_emitter_route__FREEZE.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_certificate/inputs/autonomous_emitter_route__ROUTE.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_certificate/inputs/finite_channel_wavepacket_bridge__THEOREM_V2.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_certificate/inputs/two_body_interval_bridge__CANDIDATE.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_certificate/inputs/two_body_interval_bridge__CERTIFICATE.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_certificate/inputs/two_body_interval_bridge__inputs__rational_point_certificate.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_certificate/run01.stderr', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_certificate/run01.stdout', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_certificate/run01_execution.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_certificate/run01_script.py', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_review/CAPS.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_review/EXECUTION.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_review/FILE_MANIFEST.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_review/FREEZE.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_review/REPORT.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_review/RESULTS.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_review/SOURCE_PINS.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_review/attempt_01/EXECUTION.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_review/attempt_01/check_installed.py', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_review/attempt_01/stderr.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_review/attempt_01/stdout.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_review/check_installed.py', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_review/run_check.py', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_review/sources/author/CANDIDATE.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_review/sources/author/CAPS.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_review/sources/author/CERTIFICATE.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_review/sources/author/FREEZE.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_review/sources/author/RUNTIME_IDENTITIES.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_review/sources/author/SOURCE_MANIFEST.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_review/sources/author/certify_installed_emitter.py', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_review/sources/author/inputs/autonomous_emitter_route__FREEZE.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_review/sources/author/inputs/autonomous_emitter_route__ROUTE.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_review/sources/author/inputs/finite_channel_wavepacket_bridge__THEOREM_V2.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_review/sources/author/inputs/two_body_interval_bridge__CANDIDATE.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_review/sources/author/inputs/two_body_interval_bridge__CERTIFICATE.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_review/sources/author/inputs/two_body_interval_bridge__inputs__rational_point_certificate.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_review/sources/author/run01.stderr', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_review/sources/author/run01.stdout', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_review/sources/author/run01_execution.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_review/sources/author/run01_script.py', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_review/sources/autonomous_emitter_route/ROUTE.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_review/sources/emitter_independent_review/REPORT.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_review/sources/emitter_root_qualification/ACCEPTANCE.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_review/sources/emitter_root_qualification/QUALIFICATION.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_review/sources/process/SCIENCE_WORKFLOW.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_review/sources/process/SKILL_FRESHNESS_CHECK.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_review/sources/process/physics-claim-reviewer/SKILL.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_review/sources/process/proof-search-governance.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_review/sources/process/review-loop/SKILL.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_root_review/ACCEPTANCE.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_root_review/QUALIFICATION.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_root_review/SOURCE_READ.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_root_review/qualify.py', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_root_qualification/ACCEPTANCE.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_root_qualification/QUALIFICATION.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_candidate/BOUNDS.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_candidate/CANDIDATE.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_candidate/EXECUTION.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_candidate/FREEZE.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_candidate/SOURCE_PINS.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_candidate/check_bounds.py', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_candidate/inputs/EMITTER_ROUTE.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_candidate/inputs/INSTALLED_CANDIDATE.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_candidate/inputs/INSTALLED_CERTIFICATE.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_candidate/inputs/PACKET_THEOREM.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_candidate/run_check.py', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_candidate/stderr', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_candidate/stdout', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_review/FILE_MANIFEST.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_review/FREEZE.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_review/REPORT.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_review/RESOURCE_PLAN.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_review/SOURCE_PINS.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_review/SOURCE_RECHECK.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_review/check_weighted_escape.py', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_review/run_check.py', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_review/runs/attempt_1/EXECUTION.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_review/runs/attempt_1/RESULT.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_review/runs/attempt_1/SOURCE_PINS_AT_LAUNCH.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_review/runs/attempt_1/executed_source.py', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_review/runs/attempt_1/stderr', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_review/runs/attempt_1/stdout', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_review/sources/author/BOUNDS.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_review/sources/author/CANDIDATE.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_review/sources/author/EXECUTION.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_review/sources/author/FREEZE.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_review/sources/author/SOURCE_PINS.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_review/sources/author/check_bounds.py', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_review/sources/author/inputs/EMITTER_ROUTE.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_review/sources/author/inputs/INSTALLED_CANDIDATE.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_review/sources/author/inputs/INSTALLED_CERTIFICATE.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_review/sources/author/inputs/PACKET_THEOREM.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_review/sources/author/run_check.py', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_review/sources/author/stderr', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_review/sources/author/stdout', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_review/sources/instructions/SCIENCE_WORKFLOW.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_review/sources/prior_review/REPORT.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_root_qualification/ACCEPTANCE.json', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_root_qualification/QUALIFICATION.md.txt', 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_root_qualification/qualify.py', 'scripts/emitter_coupling_family_2026_10_17.py', 'scripts/product_seed_emitter_2026_10_17.py', 'scripts/product_seed_emitter_installed_2026_10_17.py', 'scripts/product_seed_emitter_local_2026_10_17.py', 'scripts/product_seed_emitter_weighted_2026_10_17.py', 'scripts/real_control_autonomous_output_2026_10_17.py', 'scripts/structural_coefficient_box_2026_10_17.py', 'scripts/thermal_resonance_halt_2026_10_17.py', 'scripts/two_body_autonomous_halt_2026_10_17.py')

if __name__ == '__main__':
    main()
