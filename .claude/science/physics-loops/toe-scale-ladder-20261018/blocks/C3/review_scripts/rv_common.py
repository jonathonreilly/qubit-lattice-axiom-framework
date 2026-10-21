"""Reviewer-side tiny check harness (independent of the author's c3_common)."""
class Checks:
    def __init__(self, name):
        self.name, self.p, self.f = name, 0, 0
    def ok(self, msg, cond):
        cond = bool(cond)
        print(("[PASS] " if cond else "[FAIL] ") + msg, flush=True)
        if cond: self.p += 1
        else: self.f += 1
    def done(self):
        print(f"{self.name}: PASS={self.p} FAIL={self.f}")
        print(f"TOTAL: PASS={self.p} FAIL={self.f}")
