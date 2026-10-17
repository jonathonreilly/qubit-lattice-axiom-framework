"""Source/provenance/record comparison only; executes no scientific checker."""
import datetime,hashlib,json,os
from pathlib import Path
R=Path(__file__).resolve().parent
A=R.parent/'resonant_family_candidate'

def h(data):return hashlib.sha256(data).hexdigest()
def ident(p,withpath=False):
    p=Path(p).resolve();data=p.read_bytes();st=p.stat()
    result=dict(sha256=h(data),bytes=len(data),device=st.st_dev,inode=st.st_ino,mtime_ns=st.st_mtime_ns)
    if withpath:result={'path':str(p),**result}
    return result
def j(p):return json.loads(p.read_text())
def same(x,p):
    got=ident(p)
    return got['sha256']==x['sha256'] and got['bytes']==x['bytes']
def date(x):return datetime.datetime.fromisoformat(x.replace('Z','+00:00'))

ind=j(R/'INDEPENDENT_FREEZE.json')
assert h((R/'INDEPENDENT_FREEZE.json').read_bytes())=='aaaeb80e889b8d6de92af607a0d7d912d9d8e4c36b98480d451e54dc251ac1ad'
for x in ind['entries']:assert same(x,R/x['path']),x['path']
initial=j(R/'INITIAL_SOURCE_BINDINGS.json')
for x in initial['entries']:
    assert same(x,R/x['snapshot']) and same(x,Path(x['original'])),x['snapshot']
    if 'upstream_original' in x:assert same(x,Path(x['upstream_original']))
capture=j(R/'AUTHOR_CAPTURE_BINDINGS.json')
assert date(capture['created_utc'])>date(ind['frozen_utc'])
for x in capture['entries']:
    assert same(x,R/x['snapshot']) and same(x,Path(x['original'])),x['snapshot']

am=j(A/'FILE_MANIFEST.json');af=j(A/'FREEZE.json');sm=j(A/'SOURCE_MANIFEST.json')
assert ident(A/'CANDIDATE.md')['sha256']=='401e5c2389ef99bd9980898ec118f2476e49dd627d3cf9f32deb812ffc5498f0'
assert ident(A/'FREEZE.json')['sha256']=='8cdf10121e4c42247d4aba730a48413817a62b9ada420adfc6bc70df7df64879'
for x in am['files']:assert same(x,A/x['path'])
for x in sm['entries']:assert same(x,A/x['snapshot']) and same(x,Path(x['original']))
assert {str(p.relative_to(A)) for p in A.rglob('*') if p.is_file()}=={x['path'] for x in am['files']}|{'FILE_MANIFEST.json','FREEZE.json'}
assert same(af['file_manifest'],A/'FILE_MANIFEST.json')

op=j(R/'run01/PRELAUNCH.json');orr=j(R/'run01/RECEIPT.json');oo=j(R/'run01/stdout.json')
for x in op['bindings']:assert ident(x['path'],withpath=True)==x,x['path']
assert ident(R/'run01/PRELAUNCH.json',True)==orr['prelaunch']
assert ident(R/'run01/stdout.json',True)==orr['stdout']
assert ident(R/'run01/stderr.txt',True)==orr['stderr']
assert (R/'check_independent.py').read_bytes()==(R/'run01/executed_source.py').read_bytes()
assert orr['returncode']==0 and not orr['timeout'] and all(x['unchanged'] for x in orr['postlaunch_bindings'])
assert date(orr['prelaunch_fsync_completed_utc'])<date(orr['post_fsync_pre_popen_utc'])<date(oo['completed_utc'])<date(orr['completed_utc'])<date(ind['frozen_utc'])
assert oo['caps']==[30,30] and oo['unchanged_bindings']==len(op['bindings'])
assert not (R/'run01/stderr.txt').read_bytes() and not (R/'launcher_stderr.txt').read_bytes()
assert j(R/'launcher_stdout.json')==orr

ap=j(A/'run01/PRELAUNCH.json');ar=j(A/'run01/RECEIPT.json');ao=j(A/'run01/stdout.json')
for x in ap['bindings']:
    p=Path(x['path']);p=p if p.is_absolute() else A/p
    assert ident(p)==x['identity'],x['label']
    aft=next(y for y in ar['bindings_after'] if y['label']==x['label'])
    assert aft['identity']==x['identity'] and aft['unchanged']
assert ident(A/'run01/PRELAUNCH.json')==ar['prelaunch_identity']
assert ident(A/'run01/stdout.json')==ar['stdout'] and ident(A/'run01/stderr.txt')==ar['stderr']
assert (A/'check_bounds.py').read_bytes()==(A/'run01/executed_source.py').read_bytes()
assert ao['source_identity']['executed_sha256']==ident(A/'check_bounds.py')['sha256']
assert ao['source_identity']['prelaunch_sha256']==ident(A/'run01/PRELAUNCH.json')['sha256']
assert ar['returncode']==0 and not ar['timed_out'] and all(ao['checks'].values())
assert date(ap['created_before_subprocess_utc'])<date(ar['prelaunch_fsync_completed_utc'])<date(ar['subprocess_created_after_utc'])<date(ao['started_utc'])<date(ar['finished_utc'])<date(af['frozen_utc'])
assert ao['resources']['cpu_soft_hard_seconds']==ap['cpu_soft_hard_seconds']==[20,21]
assert not (A/'launch01.stderr').read_bytes() and not (A/'run01/stderr.txt').read_bytes()

mapping={
'v0':'v0','b0':'b0','E0':'E0','density_L1':'density_L1_floor',
'half_line_edges_and_cutoff':'uniform_directional_cutoff_plus_vertical',
'incoming_bottom':'uniform_incoming_bottom','residue_onset':'uniform_pole_ceiling',
'incoming_ceiling':'qin','outgoing_ceiling':'qout','common_emitter_scalar':'emitter_reference_amplitude',
'incoming_scalar':'scalar_incoming_amplitude','Cg_center':'constant_background_clock',
'Cg_variation':'varying_background_clock','Kloc_center':'constant_localized_response_clock',
'Kloc_variation':'varying_localized_response_clock','Kloc_delta_y':'all_emitter_error_coordinates_clock',
'full_clock_column':'localized_clock_per_column','full_clock_operator':'localized_clock_operator',
'full_localized':'complete_localized_operator','escape_only':'complete_escape_remainder',
'complete_infinite':'complete_infinite_upper_expression','minimum_T':'minimum_onset',
'minimum_M':'upper_coupling_clock_sites','minimum_distance_margin':'minimum_finite_buffer',
'finite_correction':'finite_extra','complete_finite':'complete_finite_upper_expression',
'actual_upper_scalar':'actual_scalar_upper_endpoint','emitter_load':'maximum_new_emitter_incident_load',
'failed_fixed_cutoff_allowance':'failed_old_cutoff_L2_single','failed_absolute_clock_allowance':'failed_old_absolute_clock'}
matched=[]
for review,author in mapping.items():
    assert oo['values'][review]['exact']==ao['values'][author]['rational'],(review,author)
    matched.append(dict(review_key=review,author_key=author,exact=oo['values'][review]['exact']))

record=dict(validated_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    purpose='Bookkeeping and exact saved-result string comparison, no scientific replay or additional scientific attempt.',
    independent_frozen_files=len(ind['entries']),initial_snapshot_pairs=len(initial['entries']),
    initial_upstream_pairs=sum('upstream_original' in x for x in initial['entries']),
    author_captured_snapshot_pairs=len(capture['entries']),author_packet_files=len(am['files'])+2,
    author_upstream_pairs=len(sm['entries']),own_prelaunch_bindings=len(op['bindings']),author_prelaunch_bindings=len(ap['bindings']),
    own_runtime_bindings=4,author_runtime_bindings=5,all_sources_and_bound_metadata_unchanged=True,
    all_chronologies_consistent=True,author_replayed=False,scientific_attempts_review=1,scientific_attempts_author=1,
    exact_saved_values_matched=matched,
    caveats=['Partial runtime byte binding only.','No formal verification of the analysis.','Final candidate authored/frozen after the author scalar run; it was not an input to that run.','Same-model and substantial source exposure persist.'])
with (R/'EVIDENCE_VALIDATION.json').open('x') as out:
    json.dump(record,out,indent=2);out.write('\n');out.flush();os.fsync(out.fileno())
print(json.dumps({k:v for k,v in record.items() if k!='exact_saved_values_matched'},indent=2))
print('Saved exact-value comparisons:',len(matched))
