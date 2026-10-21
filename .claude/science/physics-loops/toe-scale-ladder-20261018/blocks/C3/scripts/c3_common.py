"""Shared PASS/FAIL bookkeeping for the C3 block scripts."""
import sys

class Checker:
    def __init__(self, name):
        self.name = name
        self.npass = 0
        self.nfail = 0

    def check(self, label, cond, detail=""):
        ok = bool(cond)
        if ok:
            self.npass += 1
        else:
            self.nfail += 1
        print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""))
        sys.stdout.flush()
        return ok

    def finish(self):
        print(f"{self.name}: PASS={self.npass} FAIL={self.nfail}")
        return self.npass, self.nfail
