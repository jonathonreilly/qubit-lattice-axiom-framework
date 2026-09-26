#!/usr/bin/env python3
"""Stop our original launcher only after a complete-case boundary is recorded."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,signal,subprocess,time

HERE=Path(__file__).resolve().parent
PID=12120
MARKER='"starting_case": "balanced_r025_L64"'


def main():
    log=HERE/'AXIS_BALANCED_SCREEN_RUN.log';destination=HERE/'axis_balanced_screen'
    receipt=HERE/'AXIS_SCREEN_RESOURCE_HANDOFF.json'
    assert not receipt.exists()
    while datetime.now(timezone.utc)<datetime(2026,9,21,10,30,tzinfo=timezone.utc):
        command=subprocess.run(['ps','-p',str(PID),'-o','command='],capture_output=True,text=True)
        if command.returncode!=0:
            print('Original launcher already ended; no signal sent.',flush=True);return
        assert 'campaign12h/run_axis_balanced_screen.py' in command.stdout
        if MARKER not in log.read_text():
            time.sleep(.25);continue
        completed=json.loads((destination/'COMPLETED_CASES.json').read_text())
        assert len(completed)==5 and completed[-1]['case']=='balanced_growth_L48'
        assert not (destination/'balanced_r025_L64.npz').exists()
        event=dict(utc=datetime.now(timezone.utc).isoformat(),pid=PID,
            reason='Reallocate free computation threads and checkpoint batches for the three queued side64 cases within the fixed campaign deadline. Scientific parameters, sample counts and seeds remain the declared ones.',
            interrupted_case='balanced_r025_L64',interrupted_case_has_no_saved_samples=True,
            completed_cases=[r['case'] for r in completed],
            original_launcher_sha256=hashlib.sha256((HERE/'run_axis_balanced_screen.py').read_bytes()).hexdigest(),
            original_plan_sha256=hashlib.sha256((destination/'PLAN.json').read_bytes()).hexdigest())
        os.kill(PID,signal.SIGTERM)
        event['signal_sent']='SIGTERM';receipt.write_text(json.dumps(event,indent=2)+'\n')
        print(json.dumps(event),flush=True);return
    print('Resource handoff deadline reached; no signal sent.',flush=True)


if __name__=='__main__': main()
