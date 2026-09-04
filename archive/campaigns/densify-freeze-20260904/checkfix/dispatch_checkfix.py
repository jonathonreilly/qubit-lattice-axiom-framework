import json, subprocess, time, os
AT = os.path.dirname(os.path.abspath(__file__))
P3 = os.path.dirname(AT)
SEATS = {
 's1': ['WH-found','WH-camp','WH-comp','WH-late','WH-mass','WH-src'],
 's2': ['D-gauge','D-misc','D-rk','D-theta','WH-car'],
 's3': ['D-meta','D-frame','D-kcpt','D-born','D-qca'],
 's4': ['D-acl','D-flav','D-mass','D-rec','D-ker'],
}
def spec(seat, lanes):
    lane_lines = '\n'.join(
        f"- {l}: blocks {AT}/blocks_{l.replace('-','').lower()}.json (may be absent if this lane had memo-only fixes), memo {P3}/memos/{l}.md, staged primaries /tmp/lane_{l.replace('-','').lower()}.txt"
        for l in lanes)
    return f"""You are the fix-layer CHECKER seat {seat} (read-only; write ONLY {AT}/findings_{seat}.jsonl).
1. Read COMPLETELY: {AT}/CHECKFIX_BRIEF.md
2. Your lanes and files:
{lane_lines}
3. Execute the brief for every lane, writing findings incrementally to {AT}/findings_{seat}.jsonl.
4. Finish with the check_done JSON line; stdout final message is that line only."""
def launch(seat, lanes):
    s = spec(seat, lanes)
    open(f'{AT}/spec_{seat}.md','w').write(s)
    return subprocess.Popen(
        ['/Users/jonBridger/.local/bin/codex','exec','-s','workspace-write','-C',AT,'-m','gpt-5.6-sol',
         '-c','model_reasoning_effort=xhigh','-o',f'{AT}/last_{seat}.txt', s],
        stdin=subprocess.DEVNULL,
        stdout=open(f'{AT}/full_{seat}.log','w'), stderr=subprocess.STDOUT)
procs = {seat: launch(seat, lanes) for seat, lanes in SEATS.items()}
print('launched', list(procs), flush=True)
while procs:
    for seat, p in list(procs.items()):
        if p.poll() is not None:
            del procs[seat]
            ok = False
            try: ok = any('check_done' in l for l in open(f'{AT}/findings_{seat}.jsonl'))
            except FileNotFoundError: pass
            print(('DONE ' if ok else 'FAILED ') + seat, flush=True)
    time.sleep(20)
print('ALL_SEATS_FINISHED', flush=True)
