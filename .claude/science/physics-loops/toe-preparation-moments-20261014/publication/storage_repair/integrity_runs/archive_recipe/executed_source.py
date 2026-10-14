from pathlib import Path
import argparse,json,runpy,sys
p=argparse.ArgumentParser();p.add_argument('--runner',required=True);p.add_argument('--repo',required=True);a=p.parse_args()
try:
 scope=runpy.run_path(a.runner,run_name='source_integrity_fixture')
 result=scope['verify'](Path(a.repo).resolve())
except Exception as error:
 print(json.dumps({'status':'rejected','type':type(error).__name__,'reason':str(error)},sort_keys=True));sys.exit(1)
print(json.dumps(result,sort_keys=True))
