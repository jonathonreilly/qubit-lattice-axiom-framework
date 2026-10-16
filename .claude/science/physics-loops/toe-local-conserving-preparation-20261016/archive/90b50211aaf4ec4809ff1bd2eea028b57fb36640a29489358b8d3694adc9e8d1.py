"""Metadata-only source capture for the bounded exposed review. No science run."""
from pathlib import Path
import hashlib
import json
import shutil
from datetime import datetime, timezone
from pypdf import PdfReader

OUT = Path('/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/local_conserving_control_root_exposed_check')
SRC = OUT.parent / 'local_conserving_control_root_proposal'
EXPECTED = {
    'PROPOSED_LEMMAS.md': 'be48d2010c68561df8d2a48a924602cd797625345b8e7934e50ac05cd99c3bde',
    'FREEZE.json': '1ea6d4edcfff8d4c098f1318ce046da667f831749a16880b53ccb926f26fcb13',
    'Bai_Marvian_2309.11051v3.pdf': 'add4e97c6c0a1939d159924088c45481d54c2c54646d5cfebbbc7faa471154e8',
}
def digest(raw):
    return hashlib.sha256(raw).hexdigest()

target = OUT / 'sources'
target.mkdir(exist_ok=False)
rows = []
for name, expected in EXPECTED.items():
    origin = SRC / name
    raw = origin.read_bytes()
    actual = digest(raw)
    if actual != expected:
        raise RuntimeError(f'Identity mismatch: {name}: {actual}')
    dest = target / name
    dest.write_bytes(raw)
    if digest(dest.read_bytes()) != expected:
        raise RuntimeError(f'Capture mismatch: {name}')
    rows.append({'original_path': str(origin), 'captured_path': str(dest.relative_to(OUT)), 'bytes': len(raw), 'sha256': actual})

pdf = target / 'Bai_Marvian_2309.11051v3.pdf'
reader = PdfReader(pdf)
if len(reader.pages) != 38:
    raise RuntimeError('Unexpected primary PDF page count')
pages = [3, 4, 16]
selected = '\n'.join(f'=== PDF PAGE {p} ===\n{reader.pages[p-1].extract_text()}\n' for p in pages)
(OUT / 'PRIMARY_SCOPE.txt').write_text(selected, encoding='utf-8')

render = {'attempted': True, 'purpose': 'Resolve typography of displayed sector-determinant formulas; not a scientific simulation.'}
try:
    import fitz
    doc = fitz.open(pdf)
    pix = doc.load_page(15).get_pixmap(matrix=fitz.Matrix(1.5, 1.5))
    pix.save(str(OUT / 'PRIMARY_PAGE16.png'))
    render.update({'status': 'success', 'path': 'PRIMARY_PAGE16.png', 'page': 16})
except ImportError as exc:
    render.update({'status': 'unavailable', 'detail': str(exc)})

manifest = {
    'utc': datetime.now(timezone.utc).isoformat(),
    'kind': 'metadata_only_source_identity_capture',
    'scientific_executions': 0,
    'sources': rows,
    'primary_page_count': len(reader.pages),
    'nonlayout_extraction_pages': pages,
    'render': render,
    'root_freeze_third_member_not_opened_or_validated': 'SOURCE_AND_EXPOSURE.json',
    'separate_author_files_read': False,
    'all_requested_identity_checks_match': True,
}
(OUT / 'SOURCE_MANIFEST.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
print(json.dumps(manifest, indent=2))
