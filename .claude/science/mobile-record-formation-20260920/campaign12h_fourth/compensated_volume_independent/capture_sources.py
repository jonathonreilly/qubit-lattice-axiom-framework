"""Authenticate permitted fixed sources and primary-literature read identities."""
import datetime
import hashlib
import json
from pathlib import Path
import urllib.request

base = Path(__file__).resolve().parent
fourth = base.parent
sources = {
    'local_compensation_author/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT.md':
        '42ec5430a0f49c9b6e70577be601df72e23d881b7ef152186de2cdb1ff3faba4',
    'local_compensation_locality_author/LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS.md':
        '5539bbe3171ba21933aa42c4cc191b787029e5f5c9220dc8c3ee255e4906f582',
    'local_compensation_independent/REPORT.md':
        'bb92e2a7367db959390d29c3ee9724fdafd25a200ea7ad6a66ac3f2433ae0312',
    'local_compensation_independent/COMPARISON.md':
        '9d383919f5edc32ba827bef8155c1c1878744d3c5171fcd8a71f776b957c81da',
    'local_compensation_independent/FINAL_SEAL.json':
        '1686e2d2eb412524644552abf02726d7d3f65c862ba2d541801e96397f60ea09',
}
rows = []
for relative, expected in sources.items():
    path = fourth/relative
    data = path.read_bytes()
    observed = hashlib.sha256(data).hexdigest()
    assert observed == expected, (relative, observed, expected)
    rows.append({'path': str(path), 'bytes': len(data), 'sha256': observed,
                 'role': 'previously fully checked fixed dependency; not a new author volume source'})

external = []
for arxiv, title, sections, scope in [
    ('1111.4210v2', 'Barthel and Kliesch: Quasi-locality and efficient simulation of Markovian quantum dynamics',
     ['II', 'III', 'V', 'Appendix B'],
     'Read these sections via arXiv HTML; use the bounded-generator path argument after electric cutoff. No blanket invocation for strongly continuous unbounded-rotor coefficients.'),
    ('1103.1122v2', 'Nachtergaele, Vershynina and Zagrebnov: Lieb-Robinson Bounds and Existence of the Thermodynamic Limit for a Class of Irreversible Quantum Dynamics',
     ['Section 2 setup', 'Assumption 1', 'Theorems 1, 2, 3'],
     'Checked cb-norm setup and explicit norm-continuity hypothesis. Theorems are not applied directly to the uncapped electric interaction picture.'),
]:
    url = 'https://arxiv.org/html/'+arxiv
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    request = urllib.request.Request(url, headers={'User-Agent': 'Independent bounded mathematical review'})
    with urllib.request.urlopen(request, timeout=60) as response:
        data = response.read()
        status = response.status
        final_url = response.url
    external.append({'version': arxiv, 'title': title, 'requested_url': url,
                     'resolved_url': final_url, 'http_status': status,
                     'retrieved_utc': started, 'bytes': len(data),
                     'retrieved_html_sha256': hashlib.sha256(data).hexdigest(),
                     'read_sections': sections, 'read_scope': scope,
                     'full_html_saved_or_redistributed': False})

target = base/'SOURCE_BINDINGS.json'
if target.exists():
    raise FileExistsError(target)
target.write_text(json.dumps({'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                              'fixed_dependencies': rows, 'primary_literature': external,
                              'forbidden_new_author_volume_sources_opened': False,
                              'other_new_frontier_or_checkpoint_accessed': False}, indent=2)+'\n')
print(json.dumps({'verified_fixed_dependencies': len(rows), 'literature_version_receipts': len(external),
                  'output': str(target)}, indent=2))
