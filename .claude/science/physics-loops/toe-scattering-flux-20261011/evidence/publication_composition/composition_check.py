"""Read-only composition and namespace replay; no new analytic verification."""
from pathlib import Path
from hashlib import sha256
import ast, contextlib, gzip, io, json, re, sys

S=Path('/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/resume_20261011')
W=S.parent/'walk_worktree'
OUT=S/'flux_publication_review'
NOTE=W/'docs/EXCLUDED_WALK_SCATTERING_FLUX_TRANSPORT_FORM_BOUNDED_THEOREM_NOTE_2026-10-11.md'
PRIMARY=W/'scripts/excluded_walk_scattering_flux_transport_form_2026_10_11.py'
MAP=W/'.claude/science/physics-loops/toe-scattering-flux-20261011/SOURCE_COMPOSITION.json'

def identity(p):
    b=p.read_bytes()
    return {'path':str(p),'sha256':sha256(b).hexdigest(),'bytes':len(b),'lines':len(b.splitlines())}

assert identity(NOTE)['sha256']=='c70ad03ede2a01c0b49282043a4b20824f64a6b42c3440facae1b6c5e231c0bc'
assert identity(PRIMARY)['sha256']=='f8bdf9f014eae164ab283d73910ff38968933637ff25349f5e9c5d1f974dff2a'
parent=W/'docs/EXCLUDED_WALK_LOW_ENERGY_ENERGY_CURRENT_BOUNDED_THEOREM_NOTE_2026-10-11.md'
assert identity(parent)['sha256']=='9f551fc8d3592e83d15a007495a8f9165a5ddb9bc1e98d9dd3f51b6a2584f401'
manifest=json.loads(MAP.read_text());note=NOTE.read_text();runner=PRIMARY.read_text()
starts=[note.index('## Probability flux and normalized beams\n'),note.index('## Scattering-flux transport form\n'),note.index('## Review record and scoped formal verification\n')]
originals=['EXCLUDED_WALK_FLUX_BRIDGE_PROBE.md','EXCLUDED_WALK_FLUX_TRANSPORT_FORM_PROBE.md']
coverage=[]
for i,(scope,original) in enumerate(zip(('flux','form'),originals)):
    p=S/original;source=p.read_text();assert identity(p)['sha256']==manifest['input_hashes'][original]
    replacements=[r for r in manifest['exact_prose_replacements'] if r['scope'].startswith(scope+' ')]
    changed=source
    for r in replacements:
        assert changed.count(r['before'])==1,r['scope']
        changed=changed.replace(r['before'],r['after'])
    changed=re.sub(r'^## (?=\d+\.)','### ',changed,flags=re.M)
    segment=note[starts[i]:starts[i+1]]
    assert segment.rstrip('\n')==changed.rstrip('\n')
    coverage.append({'source':identity(p),'prose_replacements':len(replacements),'entire_body_matches_after_declared_prose_edits':True})
print('Entire flux and form bodies match the frozen sources after exactly 11 declared prose replacements and heading nesting; no mathematical edit.')

copies=[]
for row in manifest['evidence_copies']:
    stored=W/row['repository_path'];b=stored.read_bytes()
    assert sha256(b).hexdigest()==row['stored_sha256'],str(stored)
    raw=gzip.decompress(b) if row['encoding']=='gzip' else b
    assert sha256(raw).hexdigest()==row['original_sha256'],str(stored)
    assert raw==Path(row['original_path']).read_bytes(),str(stored)
    copies.append(identity(stored))
print('All',len(copies),'declared evidence representations match their original bytes and both stored and original hashes.')

parent_sources=[]
for name,expected in {
'EXCLUDED_WALK_TRANSPORT_PROBE.md':'8bc423b2d5adf368f4ae09a2bb87730517be243a050b4289dad3a0b217f09526',
'EXCLUDED_WALK_COOK_BRIDGE_DRAFT.md':'2c54b891deeb43a19c5f41de5059aadac7fc8d672dfb68e0b8aa575d27eb3fc7',
'EXCLUDED_WALK_CANONICAL_CURRENT_DRAFT.md':'79bc9fb3b9fd9b703f12de0a4ca4ebd62644c81bd6e15c07f723b6b7a1c977fe',
'EXCLUDED_WALK_COHERENT_PACKET_DRAFT.md':'b4ae921cc065fb2f38c1caee5aca3a1cf69bac317a6f6f0f537becd393b6cd38',
}.items():
    p=W/'.claude/science/physics-loops/toe-excluded-walk-20261011/evidence'/(name+'.gz')
    raw=gzip.decompress(p.read_bytes());assert sha256(raw).hexdigest()==expected
    assert raw==(S/name).read_bytes()
    parent_sources.append({'stored':identity(p),'original_sha256':expected})
print('All four named parent research-source representations retain the exact threshold, Cook, canonical and coherent-packet identities.')

programs=[]
for label,path in [('FLUX',S/'flux_bridge/flux_controls.py'),('TRANSPORT FORM',S/'flux_transport_form/transport_controls.py')]:
    block=runner.split('# BEGIN VERBATIM '+label+' AUTHOR CONTROLS\n')[1].split('# END VERBATIM '+label+' AUTHOR CONTROLS\n')[0]
    assert block==path.read_text()
    programs.append((label,path,block))
print('Both embedded Python programs are byte-for-byte original helpers.')

# Fresh-namespace standalone runs and the actual combined primary distinguish
# composition behavior from reusing old PASS lines. They are author replays.
standalone=[]
for label,path,block in programs:
    capture=io.StringIO()
    with contextlib.redirect_stdout(capture):
        exec(compile(block,str(path),'exec'),{'__name__':'__main__','__file__':str(path)})
    output=capture.getvalue();log=OUT/(label.lower().replace(' ','_')+'_replay.log');log.write_text(output)
    old=path.with_suffix('.log').read_text();assert output==old
    standalone.append(output)
    print(label+' fresh-namespace replay matches its entire frozen author log.')
capture=io.StringIO()
with contextlib.redirect_stdout(capture):
    exec(compile(runner,str(PRIMARY),'exec'),{'__name__':'__main__','__file__':str(PRIMARY)})
combined=capture.getvalue();(OUT/'primary_replay.log').write_text(combined)
body=''.join(standalone);assert combined.count(body)==1
assert all(identity(p)['sha256']==expected for p,expected in [(NOTE,'c70ad03ede2a01c0b49282043a4b20824f64a6b42c3440facae1b6c5e231c0bc'),(PRIMARY,'f8bdf9f014eae164ab283d73910ff38968933637ff25349f5e9c5d1f974dff2a')])
print('Actual combined primary replay completed and contains exactly the two complete standalone outputs in order.')
summary={'note':identity(NOTE),'primary':identity(PRIMARY),'parent':identity(parent),'composition_map':identity(MAP),'body_coverage':coverage,'evidence_copies':copies,'parent_sources':parent_sources,'runtime':sys.version,'source_assertion_nodes':{label:sum(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(block))) for label,_,block in programs},'replay_logs':[identity(OUT/x) for x in ('flux_replay.log','transport_form_replay.log','primary_replay.log')],'replay_scope':'Author controls replayed for namespace/composition consistency only; no independent science, new Lean compilation, mutation or canonical-cache certification.'}
(OUT/'composition_checks.json').write_text(json.dumps(summary,indent=2)+'\n')
print('Composition checks complete; analytic proof and separate compiler/mutation/cache claims are not inferred from these replays.')
