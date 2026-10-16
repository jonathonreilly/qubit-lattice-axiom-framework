import ast,json,sys
from common import N,W,read_json,write_json,pin,check_pin,now,require_campaign_active
D=N/'publication_integration/preparation';P=N/'preparation_moment_publication_components';r=read_json(D/'PREPARED_SOURCE.json');c=read_json(P/'INPUTS.json');helper=c['helper'];packet=c['packet']
require_campaign_active()
for path,expected in r['installed_pins'].items():check_pin(W/path,expected)
text=(W/helper).read_text();tree=ast.parse(text);values={n.targets[0].id:ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id in ['AUDIT_INPUT_PATHS','MANIFEST_PATH','MANIFEST_SHA256']}
expected=(P/'templates/identity_runner.py.in').read_text().replace('@AUDIT_INPUT_PATHS@',repr(values['AUDIT_INPUT_PATHS'])).replace('@MANIFEST_PATH@',repr(values['MANIFEST_PATH'])).replace('@MANIFEST_SHA256@',repr(values['MANIFEST_SHA256']))
for key,value in r['scope_lines'].items():expected+='    print('+repr(key+': '+value)+')\n'
assert text==expected
assert values['AUDIT_INPUT_PATHS']==r['canonical_inputs']
sys.path.insert(0,str(W/'scripts'));import runner_cache
result,cache=runner_cache.execute_and_write_cache(helper,timeout_sec=60)
write_json(D/'CANONICAL_RESULT.json',result)
assert result['exit_code']==0 and result['status']=='ok' and cache and runner_cache.cache_status(helper)=='fresh'
stdout=result['stdout'];data,end=json.JSONDecoder().raw_decode(stdout.lstrip());assert data['status']=='source_identity_verified' and data['mathematical_predicates']==0
lines=stdout.lstrip()[end:].strip().splitlines();assert lines==[key+': '+value for key,value in r['scope_lines'].items()]
for path,expected in r['installed_pins'].items():check_pin(W/path,expected)
write_json(D/'CANONICAL_EXECUTION.json',{'utc':now().isoformat(),'result':pin(D/'CANONICAL_RESULT.json'),'cache':pin(cache),'helper':pin(W/helper),'cache_status':runner_cache.cache_status(helper),'inputs':len(r['canonical_inputs']),'identity_result':data,'scope_lines':lines,'canonical_child_streams':'runner_cache merges child stderr into stdout; empty result.stderr is not separate child stderr evidence','root_wrapper_separate_streams':'recorded by outer N/run.py','mathematical_predicates_executed':0})
print({'cache':pin(cache),'status':result['status'],'source_identity':data})
