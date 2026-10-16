"""Metadata-only fallback rendering of one authorized primary PDF page."""
from pathlib import Path
from pypdf import PdfReader, PdfWriter
from datetime import datetime, timezone
import hashlib
import json
import subprocess
import sys

OUT = Path('/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/local_conserving_control_root_exposed_check')
run = OUT / 'runs' / 'page16_render'
run.mkdir(parents=True, exist_ok=False)
raw = Path(__file__).read_bytes()
(run / 'executed_source.py').write_bytes(raw)
start = datetime.now(timezone.utc).isoformat()
original = OUT / 'sources' / 'Bai_Marvian_2309.11051v3.pdf'
original_raw = original.read_bytes()
assert hashlib.sha256(original_raw).hexdigest() == 'add4e97c6c0a1939d159924088c45481d54c2c54646d5cfebbbc7faa471154e8'
reader = PdfReader(original)
writer = PdfWriter()
writer.add_page(reader.pages[15])
selected = OUT / 'PRIMARY_PAGE16.pdf'
with selected.open('wb') as f:
    writer.write(f)
argv = ['/usr/bin/sips', '-s', 'format', 'png', str(selected), '--out', str(OUT / 'PRIMARY_PAGE16.png')]
result = subprocess.run(argv, cwd=str(OUT), capture_output=True, timeout=60)
(run / 'stdout').write_bytes(result.stdout)
(run / 'stderr').write_bytes(result.stderr)
receipt = {
    'kind': 'actual_metadata_only_pdf_derivative_render',
    'scientific_execution': False,
    'start_utc': start,
    'end_utc': datetime.now(timezone.utc).isoformat(),
    'outer_argv': [sys.executable, '-B', str(Path(__file__))],
    'actual_render_argv': argv,
    'cwd': str(OUT),
    'source_at_launch_path': str(run / 'executed_source.py'),
    'source_sha256': hashlib.sha256(raw).hexdigest(),
    'input_pdf_sha256': hashlib.sha256(original_raw).hexdigest(),
    'selected_page': 16,
    'exit_code': result.returncode,
    'stdout_bytes': len(result.stdout),
    'stdout_sha256': hashlib.sha256(result.stdout).hexdigest(),
    'stderr_bytes': len(result.stderr),
    'stderr_sha256': hashlib.sha256(result.stderr).hexdigest(),
}
(run / 'EXECUTION.json').write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps(receipt, indent=2))
sys.exit(result.returncode)
