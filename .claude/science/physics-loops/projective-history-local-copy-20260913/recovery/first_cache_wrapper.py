from pathlib import Path
import json,sys
root=Path('/Users/jonreilly/Projects/Physics-worktrees/projective-history-local-copy-20260913')
sys.path.insert(0,str(root/'scripts'))
import runner_cache
result,path=runner_cache.execute_and_write_cache('scripts/projective_history_local_copy_record_process_2026_09_13.py',timeout_sec=180)
print(json.dumps(result,default=str))
print(path)
assert result.get('status')=='pass',result.get('status')
