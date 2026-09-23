import subprocess,time,pathlib,json,os
p=pathlib.Path(__file__).parent;t=time.monotonic();peak=0
with (p/'finite.stdout').open('w') as out,(p/'finite.stderr').open('w') as err:
 proc=subprocess.Popen(['python3',str(p/'finite.py')],stdout=out,stderr=err,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})
 while proc.poll() is None:
  rss=subprocess.run(['ps','-o','rss=','-p',str(proc.pid)],capture_output=True,text=True).stdout.strip();peak=max(peak,int(rss or 0))
  if peak>524288 or time.monotonic()-t>110:proc.kill();raise RuntimeError('resource limit exceeded')
  time.sleep(.02)
 result={'exit':proc.wait(),'wall_seconds':time.monotonic()-t,'peak_rss_kib_observed':peak,'limits':{'cpu_seconds':90,'wall_seconds':110,'rss_kib':524288,'rss_poll_seconds':.02}}
 (p/'finite-receipt.json').write_text(json.dumps(result,indent=2));print(result)
