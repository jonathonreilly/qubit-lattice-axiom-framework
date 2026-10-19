"""Reviewer harness for C3b (independent of the author's c3b_common.py; nothing imported from ../scripts)."""
PASS = 0
FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        print(f"PASS  {name}  {detail}", flush=True)
    else:
        FAIL += 1
        print(f"FAIL  {name}  {detail}", flush=True)


def total():
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}", flush=True)
