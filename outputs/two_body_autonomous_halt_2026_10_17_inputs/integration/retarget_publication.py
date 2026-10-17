from pathlib import Path
import datetime
import hashlib
import json
import shutil

N = Path(__file__).resolve().parents[1]
W = N.parent / 'correlation_worktree'
D = N / 'two_body_integration'
F = W / 'outputs/two_body_autonomous_halt_2026_10_17_inputs'
Q = W / '.claude/science/physics-loops/toe-two-body-autonomous-halt-20261017'
main = '69cf6a289b2ec06213473f1549c51a57c29b6d70'

def pin(p):
    b = p.read_bytes()
    return {'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}

# Preserve earlier actual outputs and metadata as historical evidence.
archive = F / 'integration/pre_main_publication'
shutil.copytree(D / 'pre_main_publication', archive)
shutil.copytree(D / 'prepublication_refresh', F / 'integration/prepublication_refresh')
for name in ['graph_build.stdout', 'graph_build.stderr', 'graph_manifest.stdout', 'graph_manifest.stderr']:
    shutil.copyfile(D / name, archive / name)
shutil.copyfile(D / 'prepublication_refresh/SCOPE.json', F / 'integration/current_main_scope.json')

p = W / 'docs/TWO_BODY_AUTONOMOUS_HALT_BOUNDED_THEOREM_NOTE_2026-10-17.md'
before = p.read_bytes()
replacements = [
('records ten unchanged instruction sources and the unchanged original target\nbody followed by portable-provenance prose. No science was merged into this\nbranch, and no audit verdict was adopted.',
 'records ten unchanged instruction sources, the unchanged original target\nbody and the complete narrow publication-provenance changes. No science was\nmerged or pushed to main by this campaign, and no audit verdict was adopted.'),
('This milestone is packaged on a child branch of PR9659 with its own\nwrapper review and execution; the previous result is unchanged.',
 'This milestone is packaged against current main at\n69cf6a289b2ec06213473f1549c51a57c29b6d70 after PR9659 was landed externally\nand its branch deleted. Only this new milestone was rebased; its original\nscience parent and prior execution remain preserved historical sources.')]
text = before.decode()
for old, new in replacements:
    assert text.count(old) == 1, old
    text = text.replace(old, new)
p.write_text(text)
after = p.read_bytes()
sm_path = Q / 'SOURCE_MANIFEST.json'
sm = json.loads(sm_path.read_text())
sm['note'].update(pin(p))
sm['original_science_parent'] = sm['publication_parent']
sm['publication_parent'] = main
sm['current_main_instruction_revision'] = main
sm['publication_wrapper_refinements'] = [{'old': a, 'new': b} for a, b in replacements]
for body in sm['unchanged_bodies']:
    raw = (W / body['source']).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == body['sha256']
    assert after.count(raw) == 1
    start = after.index(raw)
    body.update(body_byte_start_inclusive=start, body_byte_end_exclusive=start + len(raw))
sm_path.write_text(json.dumps(sm, indent=2) + '\n')

p = Q / 'HANDOFF.md'
s = p.read_text()
old = '''checkpoint. The science parent is PR9659 at
f5f5eda7427453aac726b394381c965f9e28ac03. Current-main instruction authority
was refreshed at 2bb6c1a54721e70512922fb10d4495adf8ea3042; this branch did not
merge that science. Review the new child delta separately from inherited work.'''
new = '''checkpoint. The original science parent is PR9659 at
f5f5eda7427453aac726b394381c965f9e28ac03. That PR was landed externally and
its branch deleted. Only this new milestone was rebased onto current main at
69cf6a289b2ec06213473f1549c51a57c29b6d70; ten relevant instruction sources
are unchanged. Review the new milestone delta against that main revision.
No science was merged or pushed to main by this campaign. Original source
arguments and earlier execution evidence remain pinned and preserved.'''
assert old in s
p.write_text(s.replace(old, new))

p = Q / 'REVIEW_HISTORY.md'
p.write_text(p.read_text() + '''
Before publication, PR9659 had been landed externally at main revision
69cf6a289b2ec06213473f1549c51a57c29b6d70 and its remote branch deleted.
Only this new milestone was rebased onto that main. The sole conflict was
the generated citation manifest; it was reset to that exact main manifest
and regenerated for this note. Ten relevant instruction files are unchanged;
the complete narrow parent wrapper/publication changes were inspected.
No external audit verdict is adopted, and this campaign did not merge or
push science to main. All four mathematical bodies and both programs remain
byte-identical. The new wrapper changes only publication provenance.
The original note, cache, result and actual execution remain archived under
integration/pre_main_publication; the refreshed execution has its own receipt.

The full initial staged whitespace check reported six warnings confined to
three byte-preserved historical artifacts: two unified diffs whose blank
context lines contain a meaningful space, and one original draft's blank EOF.
Their bytes are retained for source identity. Final checks record this scope
explicitly; no blanket whitespace pass is asserted for these raw archives.
''')
record = {'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'reason': 'External parent landing and remote branch deletion require a current-main publication base.',
          'original_note_sha256': hashlib.sha256(before).hexdigest(),
          'current_note': pin(W / sm['note']['path']),
          'replacements': sm['publication_wrapper_refinements'],
          'unchanged_mathematical_bodies': len(sm['unchanged_bodies']),
          'source_programs_changed': False,
          'root_review': 'Complete two replacement paragraphs and companion provenance read; four bodies reverified byte for byte. No scientific argument changed. New execution and graph checks are separate.'}
(D / 'RETARGET_REVIEW.json').write_text(json.dumps(record, indent=2) + '\n')
shutil.copyfile(D / 'RETARGET_REVIEW.json', F / 'root/RETARGET_REVIEW.json')
shutil.copyfile(Path(__file__), F / 'integration/retarget_publication.py')
mp = F / 'ARTIFACT_MANIFEST.json'
m = json.loads(mp.read_text())
m['files'] = {str(p.relative_to(F)): pin(p) for p in sorted(F.rglob('*')) if p.is_file() and p != mp}
mp.write_text(json.dumps(m, indent=2) + '\n')
print(json.dumps({'note': sm['note'], 'artifact_count': len(m['files']), 'publication_base': main}, indent=2))
