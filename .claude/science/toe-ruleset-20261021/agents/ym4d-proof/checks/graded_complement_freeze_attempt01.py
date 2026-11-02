#!/usr/bin/env python3
"""Freeze analytic author evidence; no numerical or theorem checker.

Run once from the assigned worktree. Refuses to overwrite any output.
The receipt excludes its own hash; the printed digest binds that receipt.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path('/Users/jonBridger/Toy Physics/.claude/worktrees/yang-mills-proof-df9972')
L = Path('.claude/science/toe-ruleset-20261021/agents/ym4d-proof')
PREFIX = L / 'checks/graded_complement_'
SOURCE = L / 'GRADED_COMPLEMENT_ASTRA.md'
OUT = {k: Path(str(PREFIX)+k+'.json') for k in ['read_manifest','process','verification','receipt']}
assert Path.cwd().resolve() == ROOT, 'Use the explicitly assigned worktree'
assert not any(p.exists() for p in OUT.values()), 'Frozen or partial outputs exist; do not restamp'


def pin(path):
    p = Path(path)
    b = p.read_bytes()
    return dict(path=str(p), bytes=len(b), sha256=hashlib.sha256(b).hexdigest())


def write(path, data):
    with path.open('x', encoding='utf-8') as stream:
        json.dump(data, stream, indent=2, ensure_ascii=False, sort_keys=True)
        stream.write('\n')


def check(old):
    now = pin(old['path'])
    assert now['sha256'] == old['sha256'], f"Changed frozen input: {old['path']}"
    assert now['bytes'] == old['bytes'], f"Changed byte count: {old['path']}"
    return now

now = datetime.now(timezone.utc).isoformat()
old_manifest = json.loads((L/'checks/cut_sector_coercivity_read_manifest.json').read_text())
old_inputs = {Path(x['path']).name:x for x in old_manifest['source_inputs']}
methodology = []
for old in old_manifest['reused_methodology_reads']+old_manifest['new_methodology_reads']:
    item = check(old)
    item['read_coverage'] = old['read_coverage']
    item['reuse'] = 'Same continuous worker session, unchanged bytes reverified. Coverage retained exactly; no new full-read assertion.'
    methodology.append(item)

predecessor_specs = [
 ('checks/covariant_complement_receipt.json','a9536686abb45d8f5fae790fd0c7685ce159a1a0f961cd8cdcd5145fb31d22d4','artifacts'),
 ('checks/review_covariant_complement_receipt.json','75a01dfe36e64f83db7886528169cddac63bfd2e12258d40313b4504dc05e6bd','owned_files'),
 ('checks/cut_sector_coercivity_receipt.json','c1b64e10e94c7dedd0e73195f46e8235f83bbda6665d9a739626ae44eef6fcac','owned_files'),
 ('checks/review_cut_sector_coercivity_receipt.json',None,'owned_files'),
]
predecessors = []
for rel, expected, key in predecessor_specs:
    rp = L/rel
    rpin = pin(rp)
    if expected:
        assert rpin['sha256'] == expected, f'Changed predecessor receipt: {rp}'
    data = json.loads(rp.read_text())
    records = [check(x) for x in data[key]]
    predecessors.append(dict(receipt=rpin, frozen_owned_count=len(records), frozen_owned_verified=records))

reads = []
def add(name, coverage, use, inherited=False):
    p = L/name
    record = pin(p)
    if inherited:
        assert Path(name).name in old_inputs
        prior = old_inputs[Path(name).name]
        assert record['sha256'] == prior['sha256'], f'Changed reused scientific input {name}'
        record['inherited_coverage'] = prior['read_coverage']
    record.update(read_coverage=coverage, use=use)
    reads.append(record)

add('PROCESS_LIGHT.md','Complete; reread for current assignment and at freeze.','Applicable lane process.',True)
add('briefs_return/AUTHOR_BRIEF_GRADED_COMPLEMENT.md','Complete at assignment and freeze.','Research suggestions only; not accepted lemmas.')
add('ASSUMPTIONS_AND_IMPORTS.md','Complete unchanged prior CC read reused.','Supplied mathematical model, not derivation or primitive adoption.',True)
add('CUT_SECTOR_COERCIVITY_ASTRA.md','Complete617-line source authored and self-read in prior unit; frozen exact bytes verified.','Actual original-cut action/quotient/reference and remaining boundary obligations; no new independent review claim.')
add('REVIEW_CUT_SECTOR_COERCIVITY_ASTRA.md','Complete fresh independent review read.','Bounded LAND only; not review of this new source.')
add('COVARIANT_SOFT_BACKGROUND_ASTRA.md','Current1-330 assembled without remaining gaps, exact185-330 reread; unchanged prior410-490 reused.','CB8-CB14 finite-u phase, full chart Hessian, actual critical branch; CB21-CB24 optional G-to-chart margin.',True)
add('REVIEW_COVARIANT_SOFT_BACKGROUND_ASTRA.md','Complete unchanged prior review reused.','Reviewed bounded background/chart domain only.',True)
add('COVARIANT_SOURCE_ACTIVITY_ASTRA.md','Current1-180,270-338, exact98-112,108-180,187-220,267-287 and targeted stencil searches; inherited1-316,337-375,508-635.','Actual scalar atoms/full-reader norms, fixed cube, actual complement interface. No whole-paper or numeric rereview.',True)
add('REVIEW_COVARIANT_SOURCE_ACTIVITY_ASTRA.md','Complete unchanged prior review reused.','Selected-sector and source-activity scope only.',True)
add('COVARIANT_COMPLEMENT_ASTRA.md','Complete527-line source read during completed prior independent review; unchanged bytes verified.','Original-cut, positive returned gas and raw complex-envelope domains retained.',True)
add('REVIEW_COVARIANT_COMPLEMENT_ASTRA.md','Complete own prior review reused; packet verified unchanged.','Exposure disclosed; no independent review of new graded source.',True)
add('SOURCE_LOCAL_HISTORY_RETURN_ASTRA.md','Complete mathematical source1-730 through H28 read in prior CC review; unchanged bytes reused.','H8 joint replacement and H24 positive conditional oscillation, only exact source/u/completion and failure-reader domain.',True)
add('REVIEW_SOURCE_HISTORY_RETURN_ASTRA.md','Complete unchanged prior review reused.','No enlarged history or integrated return domain.',True)
add('SOURCE_SEA_CONSTRUCTION_ASTRA.md','Unchanged prior1-365 and390-431 coverage reused.','Actual exterior/sea consumer mismatch; no fixed-V tail normalization imported.',True)
add('FIXED_SOURCE_RADIUS_ASTRA.md','Corrected source1-210 and412-550; FR9 polynomial-domain correction included. Full intermediate forest proof not reread.','Only fixed-source selected-sector scope and parameter compatibility; no general full-Gaussian bounded-holomorphic comparison.')
assert reads[-1]['sha256']=='6304245bdf27afa6c7f364da9bc41d8971cc0f2058c1e3484edef84df44cff86'
add('REVIEW_FIXED_SOURCE_RADIUS_ASTRA.md','Complete review read.','Original bounded verdict and stated limitations; affected confirmation separately bound.')
add('checks/fixed_source_radius_domain_correction.json','Complete receipt metadata and exact before/after identity.','Preserve original source/evidence; corrected source is current.')
add('checks/review_fixed_source_radius_domain_confirmation.json','Complete exact affected confirmation, reread at freeze.','FR-DOMAIN-1 resolved at bounded polynomial/U=0 scope, no new independent fresh review implied.')
confirmation=json.loads((L/'checks/review_fixed_source_radius_domain_confirmation.json').read_text())
check(confirmation['current_source'])
check(confirmation['author_correction_receipt'])
add('RD.md','169-248,365-478 and519-570 plus relevant denominator/consumer searches.','Requested mixed return remains HOLD. No generic theorem imported as actual model representation.')
add('REVIEW_RD.md','Disposition and B1-B3 read; bounded recovery rereads85-115 and110-169 after one truncated batch.','Supremum-defect versus integrated-tail mismatch; actual history/effective-level and interacting-reference gaps.')
add('INTERACTING_SELECTED_CORE_ASTRA.md','1-112 and446-493; exact440-500 reread for IC20 inequalities.','Context only: cutoff compatibility with sigma*p^3 and sigma^2*p^12 bounds. No IC theorem consumed, no sphere replacing cube.')

source_pin=pin(SOURCE)
manifest=dict(
    created_utc=now,
    author_source=source_pin,
    source_inputs=reads,
    reused_methodology_reads=methodology,
    methodology_reference='Previous continuous-session fetched snapshot ca2bc7ddf64790da96cd43d42017d000fbfe4808; coordinator reports current main01589af3faf806b736c42dc2f3bd625e9edead9f and unchanged methodology. All27 reused local instruction/reference identities checked unchanged. No Git in this unit.',
    exposure='Same worker authored CS and reviewed CC; SA/CB/H/FR/RD reports read at the declared scope. This is author self-review, not independent review. Astra/max requested by user; serving backend not independently attested. No nested workers.',
    inherited_read_manifest=pin(L/'checks/cut_sector_coercivity_read_manifest.json'),
    immutable_predecessor_packets=predecessors,
    external_primary_reads=[
      dict(title='J. Dimock, The Renormalization Group According to Balaban - II. Large Fields, arXiv1212.5562v2',url='https://arxiv.org/html/1212.5562v2#S3.SS13',coverage='Fresh HTML1907-2105 covered by overlapping visible reads1897-1967,1952-1994,1984-2012,2013-2040,2030-2074,2071-2101,2082-2125. Complete Lemma3.15 statement/proof and preceding normalization portion; only next lemma opening. Not complete paper.',use='Attribution and explicit comparison: product normalization; analytic weakening of covariance/propagator and background; bulk/boundary split; full exterior components with distance modulo holes. No cardinality/indicator theorem imported.',binary_downloaded=False,coordinator_exposure='Root separately pointed to the same localization and hole mismatch; this author performed the bounded primary read.'),
      dict(title='T. Balaban, Large Field Renormalization II: Localization, Exponentiation, and Bounds for the R Operation, CMP122 (1989)',url='https://scispace.com/pdf/large-field-renormalization-ii-localization-exponentiation-h8b7ih93xo.pdf',coverage='Fresh web-extracted lines0-167, printed355-358 plus opening359. Previous1.90-1.94 context remains in CS manifest. No complete38-page or PDF-visual read asserted.',use='Attribution for denominator action, stationarity and localized quadratic comparison; no OCR formula or external constant carries proof weight.',binary_downloaded=False,binary_hash_claimed=False),
    ],
    not_consumed=['An arbitrary-exterior or outside-chart concentration theorem','An IC white-ball substitution for the actual SA cube','Unrestricted FR9 full-Gaussian action on bounded or arbitrary entire holomorphic readers','RD18 as a probability-sensitive hard-indicator theorem','Any nonlinear multilevel RG, continuum or physical mass-gap conclusion','Shared current status fronts or literature-register edits as scientific premises'],
)
write(OUT['read_manifest'],manifest)

process=dict(
    created_utc=now,
    task='Analytic graded original-law witness and conditional-reference author unit',
    new_numerical_experiments=0,
    preregistration='Not required for written proofs by PROCESS_LIGHT; no new numerical criteria or tests invented.',
    resource_gate='No scientific numeric worker was launched. Only bounded text/hash/JSON packaging operations. Coordinator lock read-only, owner ym4d-full-proof, holder01a1873f-103a-7f01-b924-4455238d8a86; last supplied expiry2026-10-30T00:33:21.302218Z.',
    analytic_refinements_before_freeze=[
      'Use support-size grades of complete SA atom labels, not just shortest paths or decay distance.',
      'Constrained conditional minimizer may lie on chart boundary; retain KKT normal term and use a sigma^2 cap paying linear cost.',
      'The main cover is on C_ch=C_(r/2). The older G is unchanged; G subset C_ch needs an explicit additional fixed-threshold margin. Missing G outside this chart is not silently reclassified as proved.',
      'Pay O(log(u)^5) cap entropy with log-power alpha>5/2; retain support multiplicities and separated-witness packing loss.',
      'Hard integrated probabilities are not RD18 small supremum defects or local analytic activities; integrated probabilities retain global dependence.',
    ],
    operational_failures_preserved=[
      dict(kind='locator',attempt='INTERACTING_CORE_ASTRA.md',outcome='No such file; corrected via scoped inventory to INTERACTING_SELECTED_CORE_ASTRA.md. No scientific result.'),
      dict(kind='locator',attempt='SOURCE_ACTIVITY_ASTRA.md',outcome='rg reported no such file; corrected via scoped inventory to COVARIANT_SOURCE_ACTIVITY_ASTRA.md. No scientific result.'),
      dict(kind='output',attempt='Combined SA/RD reads exceeded available output/context',outcome='Missing passages were not counted as read; needed scoped ranges reread and coverage limited in manifest.'),
    ],
    prior_failures='All CC author23/24, six controls, failed broad shell ratio at u40, separate narrower post-hoc probe, resource-only RLIMIT_RSS/parser failures; CS original parser-attempt artifacts; and FR corrected polynomial-domain failure/correction remain immutable. None is relabelled a check of this new unit.',
    author_self_review='Entire new source read in bounded chunks; exact original action/Haar, source, gauge, normalizer, KKT, cap, full-reader multiplicities and remaining interfaces checked analytically. This is not hostile independent review.',
    prohibited_edits_performed=[],
    git_commands_in_this_unit=0,
    next_gate='Fresh separate-context hostile independent review, LAND or HOLD at exact bounded scope. Parent owns publication and shared statuses.',
)
write(OUT['process'],process)

text=SOURCE.read_text()
tags=[int(x) for x in re.findall(r'\(GC(\d+)\)',text)]
assert tags == list(range(1,33)), ('Equation labels',tags)
assert text.endswith('\n') and not any(line.rstrip()!=line for line in text.splitlines())
# Skip fenced and indented equation blocks so array brackets are not links.
prose=[]
in_fence=False
for line in text.splitlines():
    if line.startswith('```'):
        in_fence=not in_fence
        continue
    if not in_fence and not line.startswith('    '):
        prose.append(line)
links=re.findall(r'\[[^\]\n]+\]\(([^)\n]+)\)', '\n'.join(prose))
link_checks=[]
for target in links:
    if target.startswith(('https://','http://')):
        link_checks.append(dict(target=target,kind='external URL syntax; availability/reading recorded separately'))
    else:
        path=SOURCE.parent/target.split('#',1)[0]
        assert path.exists() or path in OUT.values(), f'Missing link {target}'
        link_checks.append(dict(target=target,kind='local exists or this frozen output'))
verification=dict(
    created_utc=now,
    evidence_kind='Mechanical identities only; not numerical evidence or proof validation',
    source=source_pin,
    equation_labels=tags,
    complete_final_new_source_self_read=True,
    all27_reused_methodology_identities_unchanged=len(methodology)==27,
    predecessor_owned_counts=[p['frozen_owned_count'] for p in predecessors],
    predecessor_receipts_checked=4,
    frozen_predecessor_owned_total=sum(p['frozen_owned_count'] for p in predecessors),
    input_pins_verified=len(reads),
    corrected_fr_source_and_confirmation_match=True,
    local_and_external_link_checks=link_checks,
    newline_and_trailing_space_check='PASS',
    no_numerical_run=True,
    no_scientific_verdict_assigned=True,
)
write(OUT['verification'],verification)
owned=[SOURCE,Path(__file__).relative_to(ROOT),OUT['read_manifest'],OUT['process'],OUT['verification']]
receipt=dict(
    created_utc=now,
    format='analytic-author-source-freeze-v1; not canonical integration or audit receipt',
    author_source=source_pin,
    owned_files=[pin(p) for p in owned],
    input_pins=reads,
    predecessor_receipt_pins=[p['receipt'] for p in predecessors],
    immutability='Freeze all five bound owned artifacts plus this receipt. No automatic restamp. Receipt self-hash is reported separately.',
    evidence='Analytic source; no new numerical diagnostics. Mechanical checks preserve exact identities only.',
    scope='Support-local graded cover, actual original-cut conditional chart probabilities with paid KKT cap and boundary displacement, full-reader expectation summability and separated-event bounds; optional H24/raw complex interfaces only at exact domains.',
    unproved=['Whole outside-chart complement including any G outside C_ch','Selected-sector normalized connected complement logarithm','Probability-sensitive interacting hard-indicator expansion','Complex complement nonvanishing and source/history/full-hole interfaces','Nonlinear multilevel flow, continuum existence and physical mass gap'],
    author_review_status='PENDING_NEW_INDEPENDENT_REVIEW',
)
write(OUT['receipt'],receipt)
print(json.dumps(dict(source=source_pin,receipt=pin(OUT['receipt']),read_manifest=pin(OUT['read_manifest']),owned_artifacts_including_receipt=6,predecessor_owned_verified=verification['frozen_predecessor_owned_total'],scientific_inputs=len(reads)),indent=2))
