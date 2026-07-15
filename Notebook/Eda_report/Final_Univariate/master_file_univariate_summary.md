<style>
:root{--navy:#0b1635;--blue:#2563eb;--violet:#7c3aed;--cyan:#0891b2;--green:#059669;--amber:#d97706;--red:#dc2626;--ink:#172033;--muted:#667085;--line:#dce4f0;--soft:#f4f7fb;--white:#fff}
*{box-sizing:border-box}.uni{max-width:1250px;margin:18px auto;padding:8px;font-family:Inter,Segoe UI,Arial,sans-serif;color:var(--ink);line-height:1.65}.uni h1,.uni h2,.uni h3,.uni p{margin-top:0}.uni h2{font-size:1.48rem;margin-bottom:6px}.uni h3{font-size:1rem}.uni p{color:#475569}.hero{position:relative;overflow:hidden;padding:38px;border-radius:26px;color:#fff;background:radial-gradient(circle at 90% 10%,rgba(255,255,255,.24),transparent 23%),radial-gradient(circle at 5% 100%,rgba(34,211,238,.22),transparent 28%),linear-gradient(130deg,#08132f,#1746a2 55%,#6d28d9);box-shadow:0 22px 55px rgba(15,23,42,.23)}.hero:after{content:"";position:absolute;right:-80px;bottom:-120px;width:280px;height:280px;border:1px solid rgba(255,255,255,.16);border-radius:50%}.eyebrow{display:inline-flex;padding:6px 12px;margin-bottom:14px;border:1px solid rgba(255,255,255,.24);border-radius:999px;background:rgba(255,255,255,.1);font-size:.72rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase}.hero h1{max-width:900px;margin-bottom:12px;font-size:clamp(2rem,5vw,3.5rem);line-height:1.05;letter-spacing:-.045em}.hero p{max-width:900px;margin:0;color:rgba(255,255,255,.86);font-size:1rem}.file-chip{display:inline-flex;margin-top:20px;padding:9px 14px;border-radius:10px;background:rgba(3,10,31,.45);box-shadow:inset 0 0 0 1px rgba(255,255,255,.17);font-family:Consolas,monospace;font-size:.86rem}
.nav{display:flex;flex-wrap:wrap;gap:8px;margin:16px 0;padding:12px;border:1px solid var(--line);border-radius:15px;background:rgba(255,255,255,.86);box-shadow:0 8px 25px rgba(15,23,42,.06);backdrop-filter:blur(10px)}.nav a{padding:6px 11px;border-radius:8px;color:#334155;background:#edf2f8;text-decoration:none;font-size:.78rem;font-weight:700;transition:.2s}.nav a:hover{color:#fff;background:linear-gradient(135deg,var(--blue),var(--violet));transform:translateY(-2px)}
.panel{margin:18px 0;padding:25px;border:1px solid transparent;border-radius:19px;background:linear-gradient(#fff,#fff) padding-box,linear-gradient(135deg,#dbeafe,#ede9fe,#cffafe) border-box;box-shadow:0 12px 34px rgba(15,23,42,.07)}.title{display:flex;gap:13px;align-items:flex-start;margin-bottom:17px}.num{display:grid;flex:0 0 42px;width:42px;height:42px;place-items:center;border-radius:12px;color:#fff;background:linear-gradient(135deg,var(--blue),var(--violet));font-weight:850;box-shadow:0 8px 18px rgba(37,99,235,.25)}.title p{margin:0;color:var(--muted)}
.note{display:grid;grid-template-columns:38px 1fr;gap:12px;margin:15px 0;padding:15px 17px;border-radius:13px;border:1px solid #bfdbfe;background:linear-gradient(135deg,#eff6ff,#f5f3ff)}.note b{display:block;margin-bottom:2px}.note p{margin:0;font-size:.88rem}.icon{display:grid;width:34px;height:34px;place-items:center;border-radius:10px;background:#fff;box-shadow:0 5px 14px rgba(15,23,42,.1)}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(175px,1fr));gap:13px}.stat{position:relative;overflow:hidden;min-height:126px;padding:17px;border:1px solid #e2e8f0;border-radius:15px;background:linear-gradient(145deg,#fff,#f7f9fc);transition:.22s}.stat:hover{transform:translateY(-4px);box-shadow:0 14px 28px rgba(15,23,42,.11)}.stat:after{content:"";position:absolute;right:-28px;top:-28px;width:85px;height:85px;border-radius:50%;background:color-mix(in srgb,var(--accent) 13%,transparent)}.value{margin-bottom:6px;color:var(--accent);font-size:1.82rem;font-weight:900;line-height:1}.label{color:#46546a;font-size:.82rem;font-weight:720}.mini{margin-top:10px;height:5px;border-radius:99px;background:#e8edf4;overflow:hidden}.mini span{display:block;width:var(--p);height:100%;border-radius:99px;background:linear-gradient(90deg,var(--accent),color-mix(in srgb,var(--accent) 48%,white))}
.table-wrap{overflow-x:auto;border:1px solid var(--line);border-radius:14px}.tbl{width:100%;min-width:660px;border-collapse:collapse;font-size:.85rem}.tbl th{padding:12px 14px;color:#fff;background:linear-gradient(135deg,#122554,#2563eb);text-align:left;font-size:.73rem;letter-spacing:.045em;text-transform:uppercase}.tbl td{padding:11px 14px;border-bottom:1px solid #e7edf5;color:#334155}.tbl tr:last-child td{border-bottom:0}.tbl tbody tr:nth-child(even){background:#f8fafc}.tbl tbody tr:hover{background:#eef5ff}.tbl .count{text-align:right;font-weight:850}.barcell{min-width:190px}.bar{height:7px;border-radius:99px;background:#e8edf4;overflow:hidden}.bar span{display:block;width:var(--w);min-width:4px;height:100%;border-radius:99px;background:linear-gradient(90deg,#2563eb,#7c3aed,#0891b2)}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px}.insight{padding:17px;border:1px solid #e2e8f0;border-radius:14px;background:linear-gradient(145deg,#fff,#f8fafc)}.insight h3{display:flex;gap:8px;align-items:center;margin-bottom:6px}.insight p{margin:0;font-size:.86rem}.badge{display:inline-flex;padding:5px 9px;border-radius:999px;font-family:Consolas,monospace;font-size:.7rem;font-weight:750}.b-purple{color:#6d28d9;background:#ede9fe}.b-blue{color:#1d4ed8;background:#dbeafe}.b-green{color:#047857;background:#d1fae5}.b-gray{color:#475569;background:#e2e8f0}.b-orange{color:#b45309;background:#fef3c7}.b-red{color:#b91c1c;background:#fee2e2}
details{margin:12px 0;border:1px solid var(--line);border-radius:13px;background:#fff;overflow:hidden}summary{padding:14px 17px;cursor:pointer;color:#183b82;background:linear-gradient(90deg,#f8fafc,#eff6ff);font-weight:780;list-style:none}summary::-webkit-details-marker{display:none}summary:after{content:"＋";float:right;font-size:1.1rem}details[open] summary:after{content:"－"}.inside{padding:17px}.sources{padding:13px;border-radius:11px;background:#0f172a;color:#dbeafe;font-family:Consolas,monospace;font-size:.76rem;line-height:1.8;word-break:break-word}
.problem-list{display:grid;gap:10px}.problem{display:grid;grid-template-columns:minmax(165px,1.4fr) 3fr 65px;gap:12px;align-items:center;padding:10px 12px;border:1px solid #e3e9f1;border-radius:11px;background:#fafcff}.problem b{font-size:.82rem}.problem em{text-align:right;color:#334155;font-style:normal;font-weight:850}.meter{height:8px;border-radius:99px;background:#e7ecf3;overflow:hidden}.meter span{display:block;width:var(--w);min-width:3px;height:100%;border-radius:99px;background:linear-gradient(90deg,var(--c),color-mix(in srgb,var(--c) 50%,white))}
.timeline{position:relative;display:grid;gap:14px;margin-top:15px}.timeline:before{content:"";position:absolute;left:20px;top:15px;bottom:15px;width:2px;background:linear-gradient(var(--blue),var(--violet),var(--cyan))}.step{position:relative;display:grid;grid-template-columns:42px 1fr;gap:13px}.dot{z-index:1;display:grid;width:42px;height:42px;place-items:center;border:4px solid #fff;border-radius:50%;color:#fff;background:linear-gradient(135deg,var(--blue),var(--violet));box-shadow:0 5px 15px rgba(37,99,235,.3);font-weight:850}.step-body{padding:15px 17px;border:1px solid #e2e8f0;border-radius:13px;background:#f8fafc}.step-body h3{margin-bottom:4px}.step-body p{margin:0;font-size:.86rem}.chips{display:flex;flex-wrap:wrap;gap:7px;margin-top:10px}.chip{padding:6px 10px;border:1px solid #c7d2fe;border-radius:999px;color:#4338ca;background:#eef2ff;font-size:.74rem;font-weight:700}
.flow{display:grid;grid-template-columns:1fr auto 1fr auto 1fr auto 1fr;gap:9px;align-items:center}.flow-box{display:grid;min-height:104px;place-items:center;padding:13px;border:1px solid #cfd9e7;border-radius:14px;background:radial-gradient(circle at top right,#e0e7ff,transparent 48%),linear-gradient(145deg,#fff,#f8fafc);text-align:center;font-size:.86rem;font-weight:800}.arrow{color:var(--blue);font-size:1.5rem;font-weight:900}.codeflow{margin-top:15px;padding:17px;border:1px solid #263654;border-radius:13px;color:#dbeafe;background:#0f172a;font-family:Consolas,monospace;text-align:center;line-height:1.8}
.finish{position:relative;overflow:hidden;margin:19px 0;padding:30px;border-radius:23px;color:#fff;background:radial-gradient(circle at 90% 15%,rgba(255,255,255,.18),transparent 24%),linear-gradient(135deg,#064e3b,#059669,#0891b2);box-shadow:0 18px 42px rgba(5,150,105,.22)}.finish h2,.finish p{color:#fff}.finish p{max-width:950px;color:rgba(255,255,255,.9)}.final-chip{display:inline-flex;padding:9px 13px;border:1px solid rgba(255,255,255,.22);border-radius:10px;background:rgba(0,0,0,.16);font-family:Consolas,monospace;font-weight:800}.foot{text-align:center;color:#94a3b8;font-size:.75rem}
@media(max-width:800px){.hero{padding:28px 22px}.panel{padding:20px}.flow{grid-template-columns:1fr}.arrow{transform:rotate(90deg);text-align:center}.problem{grid-template-columns:1fr}.problem em{text-align:left}}
</style>

<div class="uni">

<div class="hero">
<div class="eyebrow">Univariate Analysis · Final Consolidation</div>
<h1>Master Univariate Decision Summary</h1>
<p>A single feature-level evidence source for target relationship analysis, multivariate screening and final feature-engineering decisions.</p>
<div class="file-chip">Single source of truth → master_file_univariate.csv</div>
</div>

<div class="nav">
<a href="#overview">Overview</a><a href="#categories">Categories</a><a href="#problems">Problems</a><a href="#status">Decision Status</a><a href="#columns">CSV Structure</a><a href="#next">Next Stage</a><a href="#workflow">Workflow</a><a href="#conclusion">Conclusion</a>
</div>

<div class="note">
<div class="icon">◎</div>
<div><b>Purpose</b><p>Do not reopen the previous 8–10 univariate reports repeatedly. From this point onward, use <code>master_file_univariate.csv</code> as the single consolidated univariate evidence base.</p></div>
</div>

<section class="panel" id="overview">
<div class="title"><div class="num">1</div><div><h2>What Has Been Consolidated</h2><p>Universal, numeric, categorical, binary, ordinal, nominal, temporal/manual and special-case evidence have been merged into one feature-level CSV.</p></div></div>

<div class="stats">
<div class="stat" style="--accent:#2563eb;--p:100%"><div class="value">2,568</div><div class="label">Total dataset columns/features</div><div class="mini"><span></span></div></div>
<div class="stat" style="--accent:#7c3aed;--p:99.9%"><div class="value">2,566</div><div class="label">Candidate predictors</div><div class="mini"><span></span></div></div>
<div class="stat" style="--accent:#dc2626;--p:1%"><div class="value">2</div><div class="label">Technical role columns</div><div class="mini"><span></span></div></div>
<div class="stat" style="--accent:#0891b2;--p:92.6%"><div class="value">2,378</div><div class="label">Numeric-profiled features</div><div class="mini"><span></span></div></div>
<div class="stat" style="--accent:#059669;--p:6.6%"><div class="value">170</div><div class="label">Binary flag features</div><div class="mini"><span></span></div></div>
<div class="stat" style="--accent:#d97706;--p:1%"><div class="value">4</div><div class="label">Categorical binary features</div><div class="mini"><span></span></div></div>
<div class="stat" style="--accent:#8b5cf6;--p:1%"><div class="value">10</div><div class="label">Nominal categorical features</div><div class="mini"><span></span></div></div>
<div class="stat" style="--accent:#be123c;--p:1%"><div class="value">3</div><div class="label">Ordinal categorical features</div><div class="mini"><span></span></div></div>
<div class="stat" style="--accent:#4f46e5;--p:7.1%"><div class="value">183</div><div class="label">Manual decisions merged</div><div class="mini"><span></span></div></div>
<div class="stat" style="--accent:#c026d3;--p:78.9%"><div class="value">2,025</div><div class="label">Special-case features carried forward</div><div class="mini"><span></span></div></div>
</div>

<details>
<summary>Source reports consolidated into the master file</summary>
<div class="inside"><div class="sources">2.1_universal_feature_analysis.xlsx · 2.1_universal_feature_decisions.csv · 2.2_numeric_feature_analysis.xlsx · 2.2_numeric_feature_decisions.csv · 2.3_binary_categorical_information_report.xlsx · 2.3.2_binary_flag_temporal_logic.csv · 2.3.5_nominal_categorical_temporal_logic.csv · 2.3.6_ordinal_categorical_temporal_logic.csv · 2.3.2_binary_flag_manual_final_decisions.csv · 2.3.5_nominal_manual_final_decisions.csv · 2.3.6_ordinal_manual_final_decisions.csv · 2.4_special_feature_type_review.xlsx · 2.5_final_univariate_evidence_report.xlsx · 2.feature_category_map.csv · 2.pre_feature_category_info.csv</div></div>
</details>
</section>

<section class="panel" id="categories">
<div class="title"><div class="num">2</div><div><h2>Feature Category Overview</h2><p>The dataset is heavily numeric. Ratio/rate, count, amount, delay, duration and statistical aggregate features dominate the dataset.</p></div></div>

<div class="table-wrap">
<table class="tbl">
<thead><tr><th>Feature Category</th><th>Relative Volume</th><th class="count">Count</th></tr></thead>
<tbody>
<tr><td>ratio_rate_numeric</td><td class="barcell"><div class="bar"><span style="--w:100%"></span></div></td><td class="count">933</td></tr>
<tr><td>discrete_count_numeric</td><td><div class="bar"><span style="--w:64.3%"></span></div></td><td class="count">600</td></tr>
<tr><td>continuous_amount_numeric</td><td><div class="bar"><span style="--w:47.9%"></span></div></td><td class="count">447</td></tr>
<tr><td>binary_flag</td><td><div class="bar"><span style="--w:18.2%"></span></div></td><td class="count">170</td></tr>
<tr><td>overdue_delay_numeric</td><td><div class="bar"><span style="--w:15.4%"></span></div></td><td class="count">144</td></tr>
<tr><td>continuous_stat_numeric</td><td><div class="bar"><span style="--w:12.3%"></span></div></td><td class="count">115</td></tr>
<tr><td>date_duration_numeric</td><td><div class="bar"><span style="--w:9.8%"></span></div></td><td class="count">91</td></tr>
<tr><td>property_normalized_numeric</td><td><div class="bar"><span style="--w:4.6%"></span></div></td><td class="count">43</td></tr>
<tr><td>categorical_nominal</td><td><div class="bar"><span style="--w:1.1%"></span></div></td><td class="count">10</td></tr>
<tr><td>categorical_binary</td><td><div class="bar"><span style="--w:.5%"></span></div></td><td class="count">4</td></tr>
<tr><td>score_index_numeric</td><td><div class="bar"><span style="--w:.4%"></span></div></td><td class="count">3</td></tr>
<tr><td>categorical_ordinal</td><td><div class="bar"><span style="--w:.4%"></span></div></td><td class="count">3</td></tr>
<tr><td>cyclical_time</td><td><div class="bar"><span style="--w:.4%"></span></div></td><td class="count">3</td></tr>
<tr><td>target</td><td><div class="bar"><span style="--w:.15%"></span></div></td><td class="count">1</td></tr>
<tr><td>id</td><td><div class="bar"><span style="--w:.15%"></span></div></td><td class="count">1</td></tr>
</tbody>
</table>
</div>
</section>

<section class="panel" id="problems">
<div class="title"><div class="num">3</div><div><h2>Main Problems Found</h2><p>These issues indicate validation requirements. They are not automatic instructions to remove, cap, transform or encode features.</p></div></div>

<div class="problem-list">
<div class="problem"><b>High missingness</b><div class="meter"><span style="--w:51.8%;--c:#dc2626"></span></div><em>1,331</em></div>
<div class="problem"><b>Extreme missingness</b><div class="meter"><span style="--w:8.2%;--c:#be123c"></span></div><em>211</em></div>
<div class="problem"><b>Large missing gap</b><div class="meter"><span style="--w:4.5%;--c:#d97706"></span></div><em>116</em></div>
<div class="problem"><b>High numeric skew</b><div class="meter"><span style="--w:65.9%;--c:#7c3aed"></span></div><em>1,693</em></div>
<div class="problem"><b>High numeric outlier</b><div class="meter"><span style="--w:4.2%;--c:#f97316"></span></div><em>109</em></div>
<div class="problem"><b>Zero-heavy features</b><div class="meter"><span style="--w:30.7%;--c:#0891b2"></span></div><em>789</em></div>
<div class="problem"><b>Rare binary / near constant</b><div class="meter"><span style="--w:3.5%;--c:#ca8a04"></span></div><em>89</em></div>
<div class="problem"><b>Rare nominal mass</b><div class="meter"><span style="--w:.15%;--c:#9333ea"></span></div><em>1</em></div>
<div class="problem"><b>Categorical shift</b><div class="meter"><span style="--w:0%;--c:#059669"></span></div><em>0</em></div>
<div class="problem"><b>Special-case features</b><div class="meter"><span style="--w:78.9%;--c:#c026d3"></span></div><em>2,025</em></div>
<div class="problem"><b>Manually reviewed</b><div class="meter"><span style="--w:7.1%;--c:#2563eb"></span></div><em>183</em></div>
</div>

<div class="grid" style="margin-top:18px">
<div class="insight"><h3>◌ High missingness</h3><p>Many features contain more than 50% missing values. This does not automatically justify dropping them because history-source missingness may represent no previous record or unavailable history.</p></div>
<div class="insight"><h3>↗ Skewed and zero-heavy values</h3><p>These patterns are expected in credit-history and transaction aggregations. Transformations, binning, robust scaling or tree-based models may be more suitable later.</p></div>
<div class="insight"><h3>◇ Numeric outliers</h3><p>Outliers should not be capped blindly during EDA. Handling must depend on target relationship, business validity and model validation.</p></div>
<div class="insight"><h3>⚑ Rare binary flags</h3><p>Rare positive document and application flags may still carry credit-risk signal and should not be removed only because they are rare.</p></div>
<div class="insight"><h3>⌘ Categorical meaning</h3><p>Nominal, ordinal and binary categorical variables require encoding decisions based on semantic meaning, not frequency alone.</p></div>
<div class="insight"><h3>◆ Special values</h3><p><code>365243</code>, <code>-1</code>, <code>XNA</code> and <code>Unknown</code> should be handled as sentinel or special-label candidates.</p></div>
<div class="insight"><h3>∅ Structured missingness</h3><p>Bureau, credit-card, POS, installment and previous-application missingness may mean no-history or unknown-record rather than random missingness.</p></div>
<div class="insight"><h3>⧉ Potential redundancy</h3><p>Document flags, external scores, status aggregates and history-source groups may contain overlapping information requiring multivariate validation.</p></div>
</div>

<div class="note"><div class="icon">!</div><div><b>Core interpretation rule</b><p>Univariate problems identify features requiring deeper validation. They do not provide sufficient evidence for final dropping, imputation, transformation, capping or encoding decisions.</p></div></div>
</section>

<section class="panel" id="status">
<div class="title"><div class="num">4</div><div><h2>Current Univariate Decision Status</h2><p>Each feature now has a consolidated route indicating what evidence is still required.</p></div></div>

<div class="table-wrap">
<table class="tbl">
<thead><tr><th>Final Decision Status</th><th class="count">Feature Count</th></tr></thead>
<tbody>
<tr><td><span class="badge b-purple">special_case_carry_forward</span></td><td class="count">1,869</td></tr>
<tr><td><span class="badge b-blue">relationship_validation_needed</span></td><td class="count">395</td></tr>
<tr><td><span class="badge b-green">manual_univariate_route_available</span></td><td class="count">183</td></tr>
<tr><td><span class="badge b-gray">standard_candidate_for_next_stage</span></td><td class="count">99</td></tr>
<tr><td><span class="badge b-orange">high_priority_validation_candidate</span></td><td class="count">20</td></tr>
<tr><td><span class="badge b-red">structural_column_exclude_from_predictors</span></td><td class="count">2</td></tr>
</tbody>
</table>
</div>

<details open>
<summary>Meaning of each decision route</summary>
<div class="inside">
<div class="table-wrap">
<table class="tbl">
<thead><tr><th>Status</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td><span class="badge b-red">structural_column_exclude_from_predictors</span></td><td>ID and TARGET are role-based exclusions from model input.</td></tr>
<tr><td><span class="badge b-green">manual_univariate_route_available</span></td><td>A reviewed manual categorical or binary decision is available and should guide later stages.</td></tr>
<tr><td><span class="badge b-purple">special_case_carry_forward</span></td><td>The feature has a sentinel value, structured missingness, external-score role, rare-flag issue or group-level consideration.</td></tr>
<tr><td><span class="badge b-orange">high_priority_validation_candidate</span></td><td>The feature has extreme missingness, severe outliers, near-constant behaviour or rare-side binary patterns.</td></tr>
<tr><td><span class="badge b-blue">relationship_validation_needed</span></td><td>The feature requires target or relationship validation before feature engineering.</td></tr>
<tr><td><span class="badge b-gray">standard_candidate_for_next_stage</span></td><td>No major univariate issue was found, but relationship and multivariate review are still required.</td></tr>
</tbody>
</table>
</div>
</div>
</details>
</section>

<section class="panel" id="columns">
<div class="title"><div class="num">5</div><div><h2>Information Inside <code>master_file_univariate.csv</code></h2><p>Each feature appears once, with evidence arranged under clearly prefixed column groups.</p></div></div>

<div class="table-wrap">
<table class="tbl">
<thead><tr><th>Column Group</th><th>Information Included</th></tr></thead>
<tbody>
<tr><td><code>master_*</code></td><td>Final consolidated route, problem flags, next-stage decision and summary reason.</td></tr>
<tr><td><code>universal_profile_*</code></td><td>Train/test presence, dtype, missingness, uniqueness, constant and all-null information.</td></tr>
<tr><td><code>universal_decision_*</code></td><td>Universal priority, action, issue reasons and next analysis route.</td></tr>
<tr><td><code>numeric_profile_*</code></td><td>Missingness, unique count, zero/positive/negative rates, quantiles, skewness, kurtosis, IQR outliers and numeric-family evidence.</td></tr>
<tr><td><code>numeric_decision_*</code></td><td>Numeric temporal/statistical route, priority, modeling note and transformation or validation suggestion.</td></tr>
<tr><td><code>binary_info_*</code></td><td>Binary balance, rare side, one-rate, zero-rate and constant train/test information.</td></tr>
<tr><td><code>binary_temporal_*</code></td><td>Statistical route, balance route, stability route, risk score and possible encoding route.</td></tr>
<tr><td><code>binary_manual_*</code></td><td>Final manual binary decision, missing handling, risk level and next-stage use.</td></tr>
<tr><td><code>nominal_info_*</code></td><td>Category count, rare mass, dominance, overlap, entropy, diversity and Jensen-Shannon stability.</td></tr>
<tr><td><code>nominal_temporal_*</code></td><td>Temporal/statistical risk score, route, modifiers and encoding candidate.</td></tr>
<tr><td><code>nominal_manual_*</code></td><td>Final manual nominal decision and next-step use.</td></tr>
<tr><td><code>ordinal_info_*</code></td><td>Ordinal levels, numeric-like evidence, order-support evidence, dominance and stability.</td></tr>
<tr><td><code>ordinal_temporal_*</code></td><td>Order route, special-level route, risk score and possible encoding route.</td></tr>
<tr><td><code>ordinal_manual_*</code></td><td>Final manual ordinal mapping and special-handling decisions.</td></tr>
<tr><td><code>special_*</code></td><td>Sentinel values, structured missingness, external-score role, rare flags, labels and watchlist actions.</td></tr>
</tbody>
</table>
</div>

<div class="note"><div class="icon">⌁</div><div><b>Intentional empty fields</b><p>Unrelated evidence fields remain empty. For example, skewness and kurtosis are empty for categorical features, while categorical-level fields are empty for numeric features.</p></div></div>
</section>

<section class="panel" id="next">
<div class="title"><div class="num">6</div><div><h2>What Should Be Done Next</h2><p>The next stage should build relationship and multivariate evidence before feature-engineering implementation.</p></div></div>

<div class="timeline">
<div class="step"><div class="dot">1</div><div class="step-body"><h3>Target Relationship Analysis</h3><p>Test whether missingness, numeric ranges, binary flags, categorical levels, sentinel values and ordinal orders have meaningful relationships with <code>TARGET</code>.</p></div></div>
<div class="step"><div class="dot">2</div><div class="step-body"><h3>Statistical Multivariate Screening</h3><p>Evaluate correlation, redundancy, grouped feature overlap, feature-family duplication and train-test stability.</p></div></div>
<div class="step"><div class="dot">3</div><div class="step-body"><h3>Human-Led Relationship Analysis</h3><p>Use business-focused visual analysis to understand interactions between important feature families.</p><div class="chips"><span class="chip">Loan burden × Income</span><span class="chip">External score × Age</span><span class="chip">External score × Employment</span><span class="chip">Annuity pressure × Contract type</span><span class="chip">Credit-history availability × Risk</span><span class="chip">Region × Occupation × Income type</span></div></div></div>
<div class="step"><div class="dot">4</div><div class="step-body"><h3>Final Decision Before Feature Engineering</h3><p>Produce the feature-engineering plan only after combining relationship, multivariate, business and model-validation evidence.</p></div></div>
</div>

<div class="note"><div class="icon">×</div><div><b>Do not jump directly to feature engineering</b><p>Univariate evidence alone cannot reliably determine what should be removed, imputed, transformed, capped, grouped or encoded.</p></div></div>
</section>

<section class="panel" id="workflow">
<div class="title"><div class="num">7</div><div><h2>Feature-Engineering Rule</h2><p>Feature engineering should become an implementation notebook, not another review notebook.</p></div></div>

<div class="flow">
<div class="flow-box"><code>master_file_<br>univariate.csv</code></div><div class="arrow">→</div>
<div class="flow-box">Relationship +<br>Multivariate Evidence</div><div class="arrow">→</div>
<div class="flow-box">Final Feature-<br>Engineering Plan</div><div class="arrow">→</div>
<div class="flow-box">Feature-Engineering<br>Implementation</div>
</div>

<div class="codeflow">master_file_univariate.csv &nbsp;→&nbsp; relationship + multivariate evidence &nbsp;→&nbsp; final feature-engineering plan &nbsp;→&nbsp; feature-engineering implementation</div>

<details open>
<summary>Decisions that should already be finalized before implementation</summary>
<div class="inside"><div class="chips"><span class="chip">What to impute</span><span class="chip">What to encode</span><span class="chip">What to transform</span><span class="chip">What to cap or bin</span><span class="chip">What to treat as a special value</span><span class="chip">What remains binary</span><span class="chip">What remains ordinal</span><span class="chip">What remains nominal</span><span class="chip">What requires model validation</span><span class="chip">What can finally be removed</span></div></div>
</details>
</section>

<section class="finish" id="conclusion">
<h2>Final Univariate Conclusion</h2>
<p>The univariate-analysis stage is complete. No final model-feature dropping was applied except the role-based exclusion of ID and TARGET from predictor input. The dataset now has one consolidated feature-level evidence source that can support target relationship analysis, multivariate screening and final feature-engineering decisions without reopening the previous reports.</p>
<div class="final-chip">Use → master_file_univariate.csv</div>
</section>

<div class="foot">Master Univariate Decision Dashboard · Relationship and multivariate validation must precede feature-engineering implementation.</div>

</div>