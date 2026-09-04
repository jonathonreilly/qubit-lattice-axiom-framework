#!/usr/bin/env python3
"""Archive-release attacker dispatcher: 4 concurrent gpt-5.6-sol xhigh
seats, one per lane, with completeness check and one retry."""
import json, subprocess, time, os, sys
AT = os.path.dirname(os.path.abspath(__file__))
LANES = ['dflav','dkcpt','dacl','dmass','dgauge','whsrc','whmass','whcar','whcomp','whfound']
MAXJ = 4
os.makedirs(f"{AT}/logs", exist_ok=True)
os.makedirs(f"{AT}/findings", exist_ok=True)

def spec(slug):
    s = f"""You are an independent archive-release ATTACKER (read-only everywhere; write ONLY {AT}/findings/attack_{slug}.jsonl).
1. Read COMPLETELY: {AT}/ATTACK_BRIEF.md (your instructions and output format).
2. Read COMPLETELY: {AT}/LIVE_SURFACES.md (the live-surface reference).
3. Read COMPLETELY: {AT}/rows_{slug}.json (your lane packet; it names the lane memo path and the staged primary-text path).
4. Execute every check in the brief (A-D) with the stated read duty, writing findings incrementally to {AT}/findings/attack_{slug}.jsonl.
5. Finish with the attack_done JSON line; stdout final message is that line only."""
    p = f"{AT}/logs/spec_{slug}.md"; open(p,'w').write(s); return s

def launch(slug):
    return subprocess.Popen(
        ['/Users/jonBridger/.local/bin/codex','exec','-s','workspace-write','-C',AT,'-m','gpt-5.6-sol',
         '-c','model_reasoning_effort=xhigh','-o',f'{AT}/logs/last_{slug}.txt', spec(slug)],
        stdin=subprocess.DEVNULL,
        stdout=open(f'{AT}/logs/full_{slug}.log','w'), stderr=subprocess.STDOUT)

def done_ok(slug):
    try:
        with open(f'{AT}/findings/attack_{slug}.jsonl') as f:
            return any('attack_done' in l for l in f)
    except FileNotFoundError:
        return False

queue = list(LANES); running = {}; tries = {}
while queue or running:
    for slug, p in list(running.items()):
        if p.poll() is not None:
            del running[slug]
            if done_ok(slug):
                print(f"DONE {slug}", flush=True)
            else:
                tries[slug] = tries.get(slug, 0) + 1
                if tries[slug] <= 1:
                    print(f"RETRY {slug}", flush=True)
                    queue.append(slug)
                else:
                    print(f"FAILED {slug}", flush=True)
    while queue and len(running) < MAXJ:
        slug = queue.pop(0)
        running[slug] = launch(slug)
        print(f"LAUNCH {slug}", flush=True)
    time.sleep(20)
print("ALL_SEATS_FINISHED", flush=True)
