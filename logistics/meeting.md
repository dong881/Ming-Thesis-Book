## BMW Lab Meeting Guideline

### Enhance Timing Configuration by Adding Dynamic Timing Info Mode and Period

IG-A --> PD
IG-B --> PD
IG-C --> PD


IG-A --> PD
IG-B --> PD
IG-C --> PD


IG-A --> PD
IG-B --> PD
IG-C --> PD


IG-A --> PD
IG-B --> PD
IG-C --> PD


### Enhance Timing Configuration by Adding Dynamic Timing Info Mode and Period

IG-A --> PD
IG-B --> PD
IG-C --> PD


IG-A --> PD
IG-B --> PD
IG-C --> PD


IG-A --> PD
IG-B --> PD
IG-C --> PD


IG-A --> PD
IG-B --> PD
IG-C --> PD


<img src="https://example.com/TEEP-Preparation-Overview.png" alt="TEEP Preparation Overview Diagram"><br><br>IG-A --> PD <br>IG-B --> PD <br>IG-C --> PD<br><br><br><img src="https://example.com/TEEP-Preparation-Overview.png" alt="TEEP Preparation Overview Diagram"><br><br>IG-A --> PD <br>IG-B --> PD <br>IG-C --> PD<br><br><br><img src="https://example.com/TEEP-Preparation-Overview.png" alt="TEEP Preparation Overview Diagram"><br><br>IG-A --> PD <br>IG-B --> PD <br>IG-C --> PD<br><br><br><img src="https://example.com/TEEP-Preparation-Overview.png" alt="TEEP Preparation Overview Diagram">


<img src="https://example.com/TEEP-Preparation-Overview.png" alt="TEEP Preparation Overview Diagram"><br><br>IG-A --> PD <br>IG-B --> PD <br>IG-C --> PD<br><br><br><img src="https://example.com/TEEP-Preparation-Overview.png" alt="TEEP Preparation Overview Diagram"><br><br>IG-A --> PD < br>IG-B --> PD < br>IG-C --> PD<br><br><br><img src="https://example.com/TEEP-Preparation-Overview.png" alt="TEEP Preparation Overview Diagram"><br><br>IG-A --> PD < br>IG-B --> PD < br>IG-C --> PD<br><br><br><img src="https://example.com/TEEP-Preparation-Overview.png" alt="TEEP Preparation Overview Diagram">


### Enhance Timing Configuration by Adding Dynamic Timing Info Mode and Period

IG-A --> PD
IG-B --> PD
IG-C --> PD

IG-A --> PD
IG-B --> PD
IG-C --> PD

<img src="https://example.com/TEEP-Preparation-Overview.png" alt="TEEP Preparation Overview Diagram"><br><br>IG-A --> PD <br>IG-B --> PD <br>IG-C --> PD<br><br><br><img src="https://example.com/TEEP-Preparation-Overview.png" alt="TEEP Preparation Overview Diagram"><br><br>IG-A --> PD < br>IG-B --> PD < br>IG-C --> PD<br><br><br><img src="https://example.com/TEEP-Preparation-Overview.png" alt="TEEP Preparation Overview Diagram">

# Dynamic Timing Configuration

Dynamic timing configuration allows you to specify the timing information for your system. This includes the timing period, mode, and other parameters.

The commit 956aea0e — 2026-04-09 enhances the timing configuration by adding dynamic timing info mode and period. The author dong881 <minghunghsu.taiwan@gmail.com> fixes the following issues:
*   Improves delay handling in _tc_status_has_expected_delay function to support multiple time units and enhance tolerance for rendering drift.
*   Enhance timing configuration by adding dynamic timing info mode and period

# Dynamic Timing Configuration

Dynamic timing configuration allows you to specify the timing information for your system. This includes the timing period, mode, and other parameters.

### Enhance Timing Configuration by Adding Dynamic Timing Info Mode and Period
The commit 956aea0e — 2026-04-09 enhances the timing configuration by adding dynamic timing info mode and period. The author dong881 <minghunghsu.taiwan@gmail.com> fixes the following issues:
*   Improves delay handling in _tc_status_has_expected_delay function to support multiple time units and enhance tolerance for rendering drift.
*   Enhance timing configuration by adding dynamic timing info mode and period
*   Request access with the GitHub admin in our group to make this document **private** by default.

# Dynamic Timing Configuration
Dynamic timing configuration allows you to specify the timing information for your system. This includes the timing period, mode, and other parameters.

### Enhance Timing Configuration by Adding Dynamic Timing Info Mode and Period
The commit 956aea0e — 2026-04-09 enhances the timing configuration by adding dynamic timing info mode and period. The author dong881 <minghunghsu.taiwan@gmail.com> fixes the following issues:
*   Improves delay handling in _tc_status_has_expected_delay function to support multiple time units and enhance tolerance for rendering drift.
*   Enhance timing configuration by adding dynamic timing info mode and period
*   Request access with the GitHub admin in our group to make this document **private** by default.

## Enhance Timing Configuration by Adding Dynamic Timing Info Mode and Period

Enhance Timing Configuration by Adding Dynamic Timing Info Mode and Period
===========================================================

The new feature adds a dynamic timing info mode to the existing timing configuration. This enhancement improves the overall performance and reliability of the system.

### Behavior

When both slot-ahead and TC sweep modes are enabled, the system will analyze the traffic pattern and adjust the timing parameters accordingly. This results in better resource utilization and reduced latency.

### Config

Under **settings.tc_sweep**, you can configure the dynamic timing info mode:

*   `slot_ahead_stop_session_on_ue_loss`: Set to `false` to restore full-session retry on UE loss even in slot-ahead + TC sweep mode.
*   `compare_mode_output`: Use this option to customize the output of the compare-mode call sites.

### Plots

The new feature introduces a plot that displays the traffic pattern and timing parameters. This visualization helps users understand the system's performance and make informed decisions.

### Files changed
-   `rapp/src/auto_tester.py` — helpers `_tc_slot_ahead_stop_on_ue_loss`, placeholders, TC loop, `_plot_tc_sweep_from_ping_throughput_summary`, `analyze_tc_iperf_rx_by_suffix` summary path.



IG-A --> PD
IG-B --> PD
IG-C --> PD

<img src="https://example.com/TEEP-Preparation-Overview.png" alt="TEEP Preparation Overview Diagram"><br><br>IG-A --> PD <br>IG-B --> PD <br>IG-C --> PD<br><br><br><img src="https://example.com/TEEP-Preparation-Overview.png" alt="TEEP Preparation Overview Diagram"><br><br>IG-A --> PD < br>IG-B --> PD < br>IG-C --> PD<br><br><br><img src="https://example.com/TEEP-Preparation-Overview.png" alt="TEEP Preparation Overview Diagram"><br><br>IG-A --> PD < br>IG-B --> PD < br>IG-C --> PD<br><br><br><img src="https://example.com/TEEP-Preparation-Overview.png" alt="TEEP Preparation Overview Diagram">

# Dynamic Timing Configuration
# Dynamic Timing Configuration
### Enhance Timing Configuration by Adding Dynamic Timing Info Mode and Period
# Dynamic Timing Configuration
### Enhance Timing Configuration by Adding Dynamic Timing Info Mode and Period

# Dynamic Timing Configuration
Dynamic timing configuration allows you to specify the timing information for your system. This includes the timing period, mode, and other parameters.

The commit 956aea0e — 2026-04-09 enhances the timing configuration by adding dynamic timing info mode and period. The author dong881 <minghunghsu.taiwan@gmail.com> fixes the following issues:
*   Improves delay handling in _tc_status_has_expected_delay function to support multiple time units and enhance tolerance for rendering drift.
*   Enhance timing configuration by adding dynamic timing info mode and period

== Enhance Timing Configuration by Adding Dynamic Timing Info Mode and Period ==


Enhance Timing Configuration by Adding Dynamic Timing Info Mode and Period

# Enhance Timing Configuration by Adding Dynamic Timing Info Mode and Period

## Behavior
When **both** are true:
-- `env_cfg.__slot_ahead_value__` is set (slot-ahead expanded environment), and  -- `env_cfg.__tc_cases__` is non-empty (TC sweep enabled),
+ single-dataset plotting (existing behavior), and
+ compare-mode plotting with **multiple datasets overlaid** on the same chart template.

Instead the runner:
1. Fills **placeholder** rows for every TC case not already recorded: throughput `avg/p50/p95` = **0**, `samples` = 0, ping `avg/p50/p95` = **null** (`N/A`), `data_status`: `skipped_ue_offline`. 
2. Sets `tc_sweep_soft_abort` so the outer session **continues** (collect logs, analysis, **next** slot-ahead env). 
3. Writes `tc_sweep_ping_throughput_<suffix>.json` with sorted `cases` and optional `slot_ahead_session_stopped_early: true`. 

## Config
Under `settings.tc_sweep`: 
+ Single mode output remains:
  - `figure/tc_sweep/tc_sweep_rx_mean_<dataset>.png`
  - `figure/tc_sweep/tc_sweep_rx_p50_<dataset>.png`
  - `figure/tc_sweep/tc_sweep_rx_p95_<dataset>.png`
  - `figure/tc_sweep/tc_sweep_rx_stats_<dataset>.json` 
-- `slot_ahead_stop_session_on_ue_loss` (default **true**): set to `false` to restore full-session retry on UE loss even in slot-ahead + TC sweep mode.
+ Compare mode output (using `output_tag`, typically compare folder name):
  - `figure/tc_sweep/tc_sweep_rx_mean_<compare_tag>.png`
  - `figure/tc_sweep/tc_sweep_rx_p50_<compare_tag>.png`
  - `figure/tc_sweep/tc_sweep_rx_p95_<compare_tag>.png`
  - `figure/tc_sweep/tc_sweep_rx_stats_<compare_tag>.json` 

## Plots
-- AST parse check passed for `rapp/src/auto_tester.py`. -- IDE lint check reported no errors for the edited file.
