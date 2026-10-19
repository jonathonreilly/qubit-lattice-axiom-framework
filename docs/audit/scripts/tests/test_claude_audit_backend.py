"""Claude API auditor seat for scripts/codex_audit_runner.py.

Unactivated proposal: synthetic fixtures explicitly opt into proposed
role logic without activating any production transport. These tests
use a fake client; nothing here calls the API or spends credit.
"""
from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from unittest import mock
from pathlib import Path
from types import SimpleNamespace


SCRIPTS_DIR = Path(__file__).resolve().parents[1]
PROJECT_ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(SCRIPTS_DIR))
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

import codex_audit_runner as runner  # noqa: E402

HAS_SDK = importlib.util.find_spec("anthropic") is not None
VERDICT_JSON = json.dumps({"compute_required": None, "claim_id": "row"})


def _usage(input_tokens=1000, output_tokens=500):
    return SimpleNamespace(
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        cache_creation_input_tokens=0,
        cache_read_input_tokens=0,
    )


def _message(*, text=VERDICT_JSON, stop_reason="end_turn",
             model="claude-opus-5-5", stop_details=None):
    content = [SimpleNamespace(type="thinking", thinking="")]
    if text is not None:
        content.append(SimpleNamespace(type="text", text=text))
    return SimpleNamespace(
        id="msg_fixture",
        model=model,
        stop_reason=stop_reason,
        stop_details=stop_details,
        usage=_usage(),
        content=content,
    )


def _status_error(cls_name: str, status: int, message: str):
    import anthropic
    import httpx

    request = httpx.Request("POST", "https://api.anthropic.com/v1/messages")
    response = httpx.Response(status, request=request)
    return getattr(anthropic, cls_name)(message, response=response, body=None)


class _FakeStream:
    def __init__(self, outcome):
        self.outcome = outcome

    def __enter__(self):
        if isinstance(self.outcome, Exception):
            raise self.outcome
        return self

    def __exit__(self, *exc):
        return False

    def get_final_message(self):
        return self.outcome


class _FakeClient:
    """Records every request; returns the next scripted outcome per key."""

    def __init__(self, script: dict[str, list], calls: list):
        self.script = script
        self.calls = calls
        self.key = None
        self.beta = SimpleNamespace(messages=SimpleNamespace(stream=self._stream))

    def _stream(self, **params):
        self.calls.append((self.key, params))
        return _FakeStream(self.script[self.key].pop(0))


def _backend(script: dict[str, list], *, keys=("KEY_A", "KEY_B"), cap=None):
    calls: list = []
    environ = {name: f"secret-{name}" for name in keys}

    def factory(api_key, timeout_sec):
        client = _FakeClient(
            {f"secret-{name}": outcomes for name, outcomes in script.items()},
            calls,
        )
        client.key = api_key
        return client

    pool = runner.ClaudeKeyPool(list(keys), environ=environ)
    backend = runner.ClaudeAuditBackend(
        pool, runner.ClaudeSpend(cap), client_factory=factory
    )
    return backend, calls


class ClaudeModelPolicyTest(unittest.TestCase):
    def test_family_for_model(self):
        self.assertEqual(runner.claude_family_for_model("claude-opus-5-5"), "claude-opus-5.5")
        self.assertEqual(runner.claude_family_for_model("claude-opus-4-8"), "claude-opus-4.8")
        self.assertEqual(runner.claude_family_for_model("claude-sonnet-5"), "claude-sonnet-5")
        self.assertEqual(runner.claude_family_for_model("claude-fable-5-1"), "claude-fable-5.1")
        for bad in ("gpt-5.6-sol", "claude-opus", "claude-5-opus", "claude-opus-5-5x"):
            with self.assertRaises(ValueError):
                runner.claude_family_for_model(bad)

    def test_effort_by_criticality_and_override(self):
        self.assertEqual(runner.claude_effort_for_row({"criticality": "leaf"}), "medium")
        self.assertEqual(runner.claude_effort_for_row({"criticality": "medium"}), "medium")
        self.assertEqual(runner.claude_effort_for_row({"criticality": "high"}), "high")
        self.assertEqual(runner.claude_effort_for_row({"criticality": "critical"}), "xhigh")
        self.assertEqual(runner.claude_effort_for_row({}), "medium")
        self.assertEqual(
            runner.claude_effort_for_row({"criticality": "critical"}, "max"), "max"
        )

    def test_schema_drops_unsupported_keywords_recursively(self):
        schema = runner.claude_compatible_schema(runner.audit_verdict_output_schema())
        rendered = json.dumps(schema)
        for keyword in runner.CLAUDE_UNSUPPORTED_SCHEMA_KEYWORDS:
            self.assertNotIn(f'"{keyword}"', rendered)
        self.assertIn("premises_used", schema["properties"])

    def test_spend_cost_and_cap(self):
        spend = runner.ClaudeSpend(0.05)
        cost = spend.add("claude-opus-5-5", "claude-opus-5-5", _usage(1000, 1000))
        self.assertAlmostEqual(cost, (1000 * 4 + 1000 * 20) / 1e6)
        self.assertFalse(spend.exhausted())
        unknown = spend.add("claude-opus-5-5", "claude-unlisted-9", _usage(1000, 1000))
        self.assertAlmostEqual(unknown, (1000 * 10 + 1000 * 50) / 1e6)
        spend.add("claude-opus-5-5", "claude-opus-5-5", _usage(0, 2000))
        self.assertTrue(spend.exhausted())
        self.assertFalse(runner.ClaudeSpend(None).exhausted())

    def test_key_pool_skips_missing_keys_and_retires_in_order(self):
        pool = runner.ClaudeKeyPool(
            ["A", "MISSING", "B"], environ={"A": " key-a ", "B": "key-b", "MISSING": ""}
        )
        self.assertEqual(pool.labels, ["A", "B"])
        self.assertEqual(pool.current(), ("A", "key-a"))
        pool.retire("A", "credit_balance_exhausted")
        self.assertEqual(pool.current(), ("B", "key-b"))
        pool.retire("B", "credit_balance_exhausted")
        self.assertIsNone(pool.current())


class ClaudeRequestShapeTest(unittest.TestCase):
    def test_request_is_the_prompt_alone(self):
        params = runner.ClaudeAuditBackend.request_params(
            "PROMPT", "claude-opus-5-5", "medium"
        )
        self.assertEqual(params["messages"], [{"role": "user", "content": "PROMPT"}])
        self.assertNotIn("system", params)
        self.assertNotIn("tools", params)
        self.assertEqual(params["output_config"]["effort"], "medium")
        self.assertEqual(params["output_config"]["format"]["type"], "json_schema")
        self.assertEqual(params["fallbacks"], "default")
        self.assertEqual(params["betas"], [runner.CLAUDE_FALLBACK_BETA])

    def test_request_digest_is_stable_and_input_bound(self):
        digest = runner.ClaudeAuditBackend.request_digest
        params = runner.ClaudeAuditBackend.request_params("P", "claude-opus-5-5", "high")
        same = runner.ClaudeAuditBackend.request_params("P", "claude-opus-5-5", "high")
        other = runner.ClaudeAuditBackend.request_params("Q", "claude-opus-5-5", "high")
        self.assertEqual(digest(params), digest(same))
        self.assertNotEqual(digest(params), digest(other))


@unittest.skipUnless(HAS_SDK, "anthropic SDK not installed")
class ClaudeBackendRunTest(unittest.TestCase):
    def test_success_returns_json_reply_and_logs_no_secret(self):
        backend, calls = _backend({"KEY_A": [_message()], "KEY_B": []})
        ok, reply, stderr = backend.run("PROMPT", None, 60, "medium", "claude-opus-5-5")
        self.assertTrue(ok, stderr)
        self.assertEqual(reply, VERDICT_JSON)
        self.assertEqual(len(calls), 1)
        self.assertEqual(backend.last_call["key_label"], "KEY_A")
        self.assertEqual(backend.last_call["served_model"], "claude-opus-5-5")
        self.assertGreater(backend.last_call["estimated_cost_usd"], 0)
        self.assertNotIn("secret-", json.dumps(backend.last_call))

    def test_exhausted_key_rotates_to_next(self):
        exhausted = _status_error(
            "BadRequestError", 400,
            "Your credit balance is too low to access the Anthropic API.",
        )
        backend, calls = _backend({"KEY_A": [exhausted], "KEY_B": [_message()]})
        ok, reply, _ = backend.run("PROMPT", None, 60, "medium", "claude-opus-5-5")
        self.assertTrue(ok)
        self.assertEqual([key for key, _ in calls], ["secret-KEY_A", "secret-KEY_B"])
        self.assertEqual(backend.pool.retired, {"KEY_A": "credit_balance_exhausted"})
        self.assertEqual(backend.pool.current()[0], "KEY_B")

    def test_all_keys_exhausted_stops_the_run(self):
        def exhausted():
            return _status_error(
                "BadRequestError", 400, "Your credit balance is too low."
            )

        backend, _ = _backend({"KEY_A": [exhausted()], "KEY_B": [exhausted()]})
        with self.assertRaises(runner.ClaudeCreditsExhausted):
            backend.run("PROMPT", None, 60, "medium", "claude-opus-5-5")

    def test_bad_key_is_retired(self):
        backend, _ = _backend({
            "KEY_A": [_status_error("AuthenticationError", 401, "invalid x-api-key")],
            "KEY_B": [_message()],
        })
        ok, _, _ = backend.run("PROMPT", None, 60, "medium", "claude-opus-5-5")
        self.assertTrue(ok)
        self.assertEqual(backend.pool.retired, {"KEY_A": "authentication_failed"})

    def test_other_api_errors_fail_the_row_without_retiring_the_key(self):
        backend, _ = _backend({
            "KEY_A": [_status_error("InternalServerError", 500, "overloaded")],
            "KEY_B": [],
        })
        ok, _, stderr = backend.run("PROMPT", None, 60, "medium", "claude-opus-5-5")
        self.assertFalse(ok)
        self.assertIn("500", stderr)
        self.assertEqual(backend.pool.retired, {})

    def test_refusal_and_truncation_fail_the_row(self):
        refusal = _message(
            text=None, stop_reason="refusal",
            stop_details=SimpleNamespace(category="cyber"),
        )
        backend, _ = _backend({"KEY_A": [refusal], "KEY_B": []})
        ok, _, stderr = backend.run("PROMPT", None, 60, "medium", "claude-opus-5-5")
        self.assertFalse(ok)
        self.assertIn("refusal", stderr)
        backend, _ = _backend({"KEY_A": [_message(stop_reason="max_tokens")], "KEY_B": []})
        ok, _, stderr = backend.run("PROMPT", None, 60, "medium", "claude-opus-5-5")
        self.assertFalse(ok)
        self.assertIn("max_tokens", stderr)

    def test_fallback_served_model_is_recorded(self):
        backend, _ = _backend({
            "KEY_A": [_message(model="claude-opus-4-8")], "KEY_B": [],
        })
        ok, _, _ = backend.run("PROMPT", None, 60, "medium", "claude-opus-5-5")
        self.assertTrue(ok)
        self.assertEqual(backend.last_call["served_model"], "claude-opus-4-8")


class ClaudeIndependenceTest(unittest.TestCase):
    def setUp(self):
        proposal = mock.patch.object(runner, "CLAUDE_AUDIT_ENABLED", True)
        proposal.start()
        self.addCleanup(proposal.stop)

    FAMILY = "claude-opus-5.5"

    def test_first_pass_is_fresh_context(self):
        self.assertEqual(
            runner.determine_audit_role({"audit_status": "unaudited"}, self.FAMILY),
            ("first", "fresh_context"),
        )

    def test_known_non_claude_author_is_cross_family(self):
        self.assertEqual(
            runner.determine_audit_role(
                {"audit_status": "unaudited", "author_family": "codex-gpt-5.6"},
                self.FAMILY,
            ),
            ("first", "cross_family"),
        )

    def test_prior_codex_auditor_is_not_evidence_of_authorship(self):
        row = {
            "audit_status": "unaudited",
            "previous_audits": [{"auditor_family": "codex-gpt-5.6"}],
        }
        self.assertEqual(
            runner.determine_audit_role(row, self.FAMILY, is_reaudit_candidate=True),
            ("reaudit", "fresh_context"),
        )

    def test_dispatch_with_unknown_author_is_not_weak(self):
        self.assertEqual(
            runner.determine_audit_role(
                {"audit_status": "unaudited"},
                self.FAMILY,
                is_reaudit_candidate=True,
                is_dispatch_target=True,
            ),
            ("first", "fresh_context"),
        )

    def test_second_seat_follows_same_family_rule(self):
        row = {
            "audit_status": "audit_in_progress",
            "cross_confirmation": {
                "status": "awaiting_second",
                "first_audit": {"auditor_family": "claude-opus-5.5"},
            },
        }
        self.assertEqual(
            runner.determine_audit_role(row, self.FAMILY),
            ("second", "fresh_context"),
        )
        row["cross_confirmation"]["first_audit"]["auditor_family"] = "codex-gpt-5.6"
        self.assertEqual(
            runner.determine_audit_role(row, self.FAMILY),
            ("second", "cross_family"),
        )

    def test_settled_rows_are_skipped(self):
        role, _ = runner.determine_audit_role(
            {"audit_status": "audited_clean"}, self.FAMILY
        )
        self.assertEqual(role, "skip")

    def test_codex_first_pass_is_unchanged(self):
        self.assertEqual(
            runner.determine_audit_role({"audit_status": "unaudited"}, "codex-gpt-5.6"),
            ("first", "cross_family"),
        )


class PremiseUnitPromptTest(unittest.TestCase):
    def test_prompt_lists_every_declarable_unit(self):
        text = runner.premise_units_prompt_text(PROJECT_ROOT)
        for unit in (
            "minimal_axioms:lattice",
            "minimal_axioms:qubit",
            "minimal_axioms:admissibility",
            "minimal_axioms:record",
            "scale_reference_primitive",
            "kinetic_isotropy_primitive",
            "realized_state_primitive",
        ):
            self.assertIn(f"`{unit}`", text)
        self.assertIn("## Qualification", text)
        self.assertIn("do not list it", text)

    def test_template_carries_the_premise_units_token_once(self):
        template = (PROJECT_ROOT / "docs/audit/AUDIT_AGENT_PROMPT_TEMPLATE.md").read_text()
        self.assertEqual(template.count("{{PREMISE_UNITS}}"), 1)
        self.assertIn('"premises_used"', template)

    def test_output_schema_enumerates_premise_units(self):
        schema = runner.audit_verdict_output_schema(allow_compute_required=False)
        items = schema["properties"]["premises_used"]["items"]
        self.assertIn("minimal_axioms:record", items["enum"])
        self.assertNotIn("minimal_axioms:qualification", items["enum"])

    def test_validator_rejects_unknown_premise_unit(self):
        error = runner.validate_verdict(
            {
                "claim_id": "row",
                "load_bearing_step": "x",
                "load_bearing_step_class": "A",
                "claim_type": "positive_theorem",
                "claim_scope": "x",
                "chain_closes": True,
                "chain_closure_explanation": "x",
                "verdict": "audited_clean",
                "verdict_rationale": "x",
                "negative_assertion_classes": [],
                "premises_used": ["minimal_axioms:gravity"],
            },
            "row",
        )
        self.assertIsNotNone(error)
        self.assertIn("unknown premise unit", error)


if __name__ == "__main__":
    unittest.main()
