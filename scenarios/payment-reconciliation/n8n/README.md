# Reconciliation agent in n8n (Day 3)

`reconciliation-agent.json` is an n8n workflow export: Manual Trigger → Read
the three CSVs from disk → Bundle rows (Code) → AI Agent with the contract
from [`../contract.md`](../contract.md) as system message, Anthropic chat
model attached.

Status: `OPEN — not yet run against a live n8n instance`. Import it, fix any
node version the import complains about, and record the observed settings.
If the import fails, rebuild it by hand in ten minutes:

1. **Manual Trigger**.
2. **Read/Write Files from Disk** · operation Read · file selector
   `scenarios/payment-reconciliation/data/*.csv` (absolute path on the
   training laptop). Output binary property `data`.
3. **Code** · paste `bundle-rows.js`. It parses the three CSVs and emits one
   item with `ledger`, `psp`, `bank`, `cutoff` and `fee_rule`.
4. **AI Agent** · prompt "Reconcile the batches in {{ JSON.stringify($json) }}"
   · system message = the full text of `../contract.md`.
5. **Anthropic Chat Model** connected to the agent. Use the model the
   facilitator names; record it on the evidence card.

Save the output table, the model name, the temperature and the time of the
run. Then compare with your Day 2 hand worksheet.
