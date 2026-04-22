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

When **both** are true:
-- `env_cfg.__slot_ahead_value__` is set (slot-ahead expanded environment), and
-- `env_cfg.__tc_cases__` is non-empty (TC sweep enabled),
+ single-dataset plotting (existing behavior), and
+ compare-mode plotting with **multiple datasets overlaid** on the same chart template.


<img src="https://example.com/TEEP-Preparation-Overview.png" alt="TEEP Preparation Overview Diagram"><br><br>IG-A --> PD <br>IG-B --> PD <br>IG-C --> PD<br><br><br>

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


Packed log 拆分公式

raw_value = signed 64-bit
sfn = (raw_value >> 48) & 0xFFFF
slot = (raw_value >> 32) & 0xFFFF
payload = (int32_t)(raw_value & 0xFFFFFFFF)


Dynamic Config and SLOT_AHEAD Parameter

> ### Dynamic Config and SLOT_AHEAD Parameter
>
> The SLOT_AHEAD parameter is used to pass a value with the VNF for dynamic config.
>
> It must be passed as a command line argument when starting the VNF.
>
> The default value of SLOT_AHEAD is 8, but it can be modified according to the specific use case.


2. Lab Formatting Guidelines (excerpt)

1. [Milestone 1: <Milestone Title>](<GitHub Plan Link>)

**Daily Logs:**
- `hh:mm–hh:mm`: [1.1 <Task 1 Title>](<GitHub Task Link>)
- `hh:mm–hh:mm`: [1.2 <Task 2 Title>](<GitHub Task Link>)
- `hh:mm–hh:mm`: [1.m <Task m Title>](<GitHub Task Link>)


Technical Research Compendium (Deep search results)

[!NOTE]
> Our servers are put in the server room. Please contact the admin for VPN access.
