const files = {};
const items = $input.all();
for (let i = 0; i < items.length; i++) {
  const name = items[i].binary.data.fileName.replace(/\.csv$/, '').replace(/-/g, '_');
  const text = (await this.helpers.getBinaryDataBuffer(i, 'data')).toString('utf8').trim();
  const [head, ...rows] = text.split(/\r?\n/);
  const cols = head.split(',');
  files[name] = rows.map(r => Object.fromEntries(r.split(',').map((v, k) => [cols[k], v])));
}
return [{ json: {
  cutoff: '2026-09-10 12:00 Europe/Amsterdam',
  fee_rule: 'expected_fee_minor = round_half_up(gross_minor * 0.02); expected_net_minor = gross_minor - expected_fee_minor',
  ...files,
}}];
