# Debugging Workflow 

>## Debugging Workflow
>
>### What was implemented
>
>\`rapp/src/auto_tester.py` now supports **both**:
>\n>\+ Legend is no longer hardcoded to \`8 slots ahead`.\n>\+ Legend now auto-parses session/dataset name:\n>\n>\- `7-slots-ahead` / `slot-ahead-7` => `7 slots ahead`
>\- names containing `proposed` or `dynamic` => `proposed`
>\- otherwise fallback to original label text.
>\n>\+ Chart titles are removed from TC sweep plots (`mean/p50/p95`).
>

>### Key changes
>
>- Refactored data extraction into reusable helpers:
>\  - \_collect_tc_sweep_points_from_summary(...)\n>\  - \_collect_tc_sweep_points_from_iperf(...)\n>\  - \_build_tc_sweep_series(...)\n>
>- Added shared plot renderer:\n>\  - \_plot_tc_sweep_series(...)\n>\  - Uses the same TC sweep template (`mean` / `p50` / `p95`, same axis/title style)
>\  - Draws one line per dataset for compare analysis
>\  - Keeps `x` markers for non-OK rows from summary data
>
>- Extended target function signature:\n>\  - \_analyze_tc_iperf_rx_by_suffix(session_raw_dir, session_fig_dir, dataset_suffix, compare_inputs=None, output_tag=None)
>\  - \_collect_tc_sweep_points_from_summary(summary_path)
>\  - \_plot_tc_sweep_series(session_fig_dir, output_tag, title_tag, series_list)
>\  - \_build_tc_sweep_series(session_raw_dir, dataset_suffix, label=None)
>
>

# Debugging Workflow
## Example Solution
Add four spaces at the beginning of each line to define indentation.
```

# Debugging Workflow 

## What was implemented

*   **both**:
    *   Legend is no longer hardcoded to `8 slots ahead`. 
    *   Legend now auto-parses session/dataset name:
        
          -   `7-slots-ahead` / `slot-ahead-7` => `7 slots ahead`
          -   names containing `proposed` or `dynamic` => `proposed`
          -   otherwise fallback to original label text.
    *   Chart titles are removed from TC sweep plots (`mean/p50/p95`).

## Key changes

### 1. Refactored data extraction into reusable helpers:
        
     -   `_collect_tc_sweep_points_from_summary(...)`
     -   `_collect_tc_sweep_points_from_iperf(...)`
     -   `_build_tc_sweep_series(...)"

### 2. Added shared plot renderer:
        
     -   `_plot_tc_sweep_series(...)`
     -   Uses the same TC sweep template (`mean` / `p50` / `p95`, same axis/title style)
     -   Draws one line per dataset for compare analysis
     -   Keeps `x` markers for non-OK rows from summary data

### 3. Extended target function signature:
        
     -   `analyze_tc_iperf_rx_by_suffix(session_raw_dir, session_fig_dir, dataset_suffix, compare_inputs=None, output_tag=None)`
     -   `compare_inputs` format:
        \n           \'\'['\'\{\'raw_dir:\ <Path>,\  'dataset_suffix:\ <str>,\  \'label:\ <str>\}\'\'\]

# TC sweep legend/title adjustment

## Purpose

Updated `rapp/src/auto_tester.py` for TC sweep charts:

| App Manifest                            | Teams app manifest     | Describes app capabilities.        |
| Microsoft 365 Agents Playground         | Test Tool              | Test Environment.          |
| `m365agents.yml`                        | `teamsapp.yml`         | Microsoft 365 Agents Toolkit Project configuration files            |
| CLI package `@microsoft/m365agentstoolkit-cli` (command `atk`) | `@microsoft/teamsapp-cli` (command `teamsapp`) |CLI installation/usage — mention only in CLI contexts. |

> **Rephrase guidance:**
> - Use the new names by default.
> - Explain the rebranding briefly if it helps the user’s understanding. 

# Instructions for Copilot

## Table of Contents

### Milestones
#### Project Title
#### Milestone 1: Updated TC sweep legend/title handling for improved clarity in chart outputs
##### Task 1: Refactored data extraction into reusable helpers
\    -   _collect_tc_sweep_points_from_summary(...)\    -   _collect_tc_sweep_points_from_iperf(...)\    -   _build_tc_sweep_series(...)\
#### Task 2: Added shared plot renderer
\    -   _plot_tc_sweep_series(...)\
##### Purpose

*   Improve clarity in chart outputs by using a more descriptive legend title.
*   Refactor data extraction into reusable helper functions for better maintainability and scalability.
### Guidelines
#### Formatting Standards
> [!TIP]\n> **Formatting Standards**:\n\  1. Dates: `yyyy-mm-dd` format (e.g., `2025-10-18`)\n  2. Time: `hh:mm–hh:mm` format (e.g., `09:00–11:30`)\n  3. Auto-generate Table of Contents using [VS Code Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one#table-of-contents)

#### Document Structure
> [!TIP]\n> **Document Structure**:\n\    Link your study notes with milestones and daily logs as shown below:

![Daily log workflow diagram](./assets/daily-log.png)

#### Milestones
> [!TIP]\n> **Key Principles**:\n\  - One project = One study note (installation/integration/user guide)\n  - Each task = One section in the study note\n  - Task title must match its section header exactly\n  - Link completed tasks to their documentation

## File
Create `./milestones.md` in your project repository.

## Template\
```markdown
# Milestones

## Table of Contents

<!-- Auto-generated by Markdown All in One -->

## Project Title\
### Milestone 1: <Milestone Name>
#### Task 1: <Task Title>\n\    - [x] [1.1 Task Title](https://github.com/bmw-ece-ntust/<repo>/blob/<7-digit commit hash>/<study-note>.md#<task-section>)
\    - [x] [1.2 Task Title](https://github.com/bmw-ece-ntust/<repo>/blob/<7-digit commit hash>/<study-note>.md#<task-section>)\
### Milestone 2: <Milestone Name>
#### Task 2: <Task Title>\n\    - [x] [2.1 Task Title](https://github.com/bmw-ece-ntust/<repo>/blob/<7-digit commit hash>/<study-note>.md#<task-section>)\n
```

# Milestones

## Table of Contents

<!-- Auto-generated by Markdown All in One -->

## Project Title

### Milestone 1: <Milestone Name>

- [x] [1.1 Task Title](https://github.com/bmw-ece-ntust/<repo>/blob/<7-digit commit hash>/<study-note>.md#<task-section>)
- [x] [1.2 Task Title](https://github.com/bmw-ece-ntust/<repo>/blob/<7-digit commit hash>/<study-note>.md#<task-section>)

# Debugging Workflow:
## Table of Contents
### Daily log workflow diagram
![Daily log workflow diagram](./assets/daily-log.png)


## Known Issues and Troubleshooting Steps

### Duplicate Lines with the Same Text

*   Remove duplicate lines by reviewing the content and removing any identical lines.
*   Verify that all necessary information is included in the document.

### PNF Message Age and Stale Segment Metrics

*   Ensure that the PNF message age and stale segment metrics are recorded correctly.
*   Review the code to ensure it can be parsed correctly, following the fix provided by dong881 <minghunghsu.taiwan@gmail.com> (commit 4439a580).
*   Verify that the table of contents is accurate and complete.

### Missing Closing ## Header After Table of Contents

*   Add a closing `##` header after the table of contents to ensure proper formatting.
*   Review the code to confirm that this change does not affect functionality.

# Debugging Workflow:
## Table of Contents
### Daily log workflow diagram
![Daily log workflow diagram](./assets/daily-log.png)

# Debugging Workflow: The section title is missing a space between the hash symbol and the text.

> [REVIEWER FEEDBACK: **Verdict**: FEEDBACK
**Overall Comment**: Review parsing failed: Expecting value: line 1 column 1 (char 0). Raw: Based on the provided code snippets, it appears that there are several issues with formatting and structure. Here is a suggested solution:

1.  **Consistent indentation**: The code uses ]

### File TOC (for navigation reference — do NOT echo this back)
# Debugging Workflow
### Milestones
# Milestones
## Table of Contents
## Project Title
### Milestone 1: <Milestone Name>
# Debugging Workflow:
## Table of Contents
### Daily log workflow diagram
## Known Issues and Troubleshooting Steps
### Duplicate Lines with the Same Text
### PNF Message Age and Stale Segment Metrics
### Missing Closing ## Header After Table of Contents
# Debugging Workflow:
## Table of Contents
### Daily log workflow diagram
# Debugging Workflow: The section title is missing a space between the hash symbol and the text.
## Updated debugging workflow diagram and added missing closing `##` headers where needed.
# Debugging Workflow:
## Table of Contents
### Daily log workflow diagram
# Debugging Workflow: The section title is now correctly formatted with a space between the hash symbol and the text.
## Updated debugging workflow diagram and added missing closing `##` headers where needed.

# Debugging Workflow:

## Table of Contents
### Daily log workflow diagram
### Milestones
### Milestone 1: Create a master checklist of all projects, their milestones, and individual tasks.
### Milestone 2: Review and finalize the study note template.
### Daily Logs
# Debugging Workflow:

## Table of Contents
### Daily log workflow diagram
### Milestones

# Debugging Workflow:
## Table of Contents
### Daily log workflow diagram
![Daily log workflow diagram](./assets/daily-log.png)

### Milestones
### Milestone 1: Create a master checklist of all projects, their milestones, and individual tasks.
### Milestone 2: Review and finalize the study note template.
### Daily Logs

# Debugging Workflow:
The section title is missing a space between the hash symbol and the text.
## Table of Contents
### Daily log workflow diagram
![Daily log workflow diagram](./assets/daily-log.png)

### Milestones

# Debugging Workflow: 

> Develop a detailed debug workflow, including known issues, troubleshooting steps, and error handling procedures.

> The current standard PID controller is not sufficient for severe network spikes. Implement an emergency rescue PID controller to catch up with sudden drops immediately and prevent packet loss.

> This controller uses a wider safety margin (800us) to ensure immediate response times, even at the cost of some smoothing.

> Note: The original code has been updated to include panic mode for extreme network spikes, which overrides the standard PID behavior.

<## Known Issues and Troubleshooting Steps
To troubleshoot issues with the debugging workflow, follow these steps:
1. Check for any errors in the output.
2. Verify that all necessary dependencies are installed and up-to-date.
3. Consult the user manual or online documentation for specific instructions on how to use the debugging tool.

## Debugging Workflow: The section title is missing a space between the hash symbol and the text.

Debugging Workflow
---------------------
### Issues
#### Stale HARQ process cleanup
The stale HARQ process cleanup for DL and UL processes is not implemented correctly. This can cause allocation failures.
### Duplicate lines with the same text
There are duplicate lines with the same text in the debug workflow section.


## Table of Contents

> [!TIP]
> Generate the Table of Contents automatically using [Markdown All in One extension in VS Code](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one#table-of-contents).

- [Table of Contents](#table-of-contents)
- [Project description](#project-description)
- [Execution Status](#execution-status)
- [System Architecture](#system-architecture)
- [Repository Structure](#repository-structure)
  - [Configuration](#configuration)
  - [Installation Steps](#installation-steps)
- [Post-Installation Verification](#post-installation-verification)
- [Troubleshooting](#troubleshooting)
  - [Common Issues and Solutions](#common-issues-and-solutions)
- [Additional Resources](#additional-resources)

## Project description

**Project Name:**

**Description:** A comprehensive solution for \[specific use case]. This project provides \[key functionality] and enables users to \[main benefits].

**Key Features:**:

- Feature 1: \[Brief description]
- Feature 2: \[Brief description]
- Feature 3: \[Brief description]

**Target Users:** \[Developers/Researchers/System Administrators/etc.]

## Access Method (if any)

> [!NOTE]
> Our servers are put in the server room. Please contact the admin for VPN access.


Host: <IP address>
User: <username>


# The authenticity of host '192.168.1.100 (192.168.1.100)' can't be established.

# Daily Plan & Logs

**Name**: <Your Full Name>  
**Student ID**: <Your ID>  
**Enrollment**:

- Program: <M.S. / Ph.D.>
- Year: <Fall/Spring> <Year>

## Table of Contents

<!-- Auto-generated by Markdown All in One -->

## 2025-10-18

**Short-term Goal**: [Project Title](https://github.com/bmw-ece-ntust/<repo>/blob/<7-digit commit hash>/<study-note>.md)

**Daily Logs**:

- `09:00–11:30`: [Task 1 Title](https://github.com/bmw-ece-ntust/<repo>/blob/<7-digit commit hash>/<study-note>.md#task-1-section)
- `13:00–15:45`: [Task 2 Title](https://github.com/bmw-ece-ntust/<repo>/blob/<7-digit commit hash>/<study-note>.md#task-2-section)
- `16:00–17:00`: [Task 3 Title](https://github.com/bmw-ece-ntust/<repo>/blob/<7-digit commit hash>/<study-note>.md#task-3-section)

## Debugging Workflow: 

> Add an overall comment with instructions on how to proceed with the comprehensive assessment.

This section provides guidelines for debugging workflow. Please refer to the [Lab Formatting Guidelines](https://labs.openairinterface.org/labs/doc/how-to/debugging-workflow/) for more information.

# TC sweep legend/title adjustment

Updated `rapp/src/auto_tester.py` for TC sweep charts:

- Legend is no longer hardcoded to `8 slots ahead`.\n- Legend now auto-parses session/dataset name:\n  - `7-slots-ahead` / `slot-ahead-7` => `7 slots ahead`\n  - names containing `proposed` or `dynamic` => `proposed`\n  - otherwise fallback to original label text.\n- Chart titles are removed from TC sweep plots (`mean/p50/p95`).\n
## Key changes

### Refactored data extraction into reusable helpers:\n- `_collect_tc_sweep_points_from_summary(...)`
- `_collect_tc_sweep_points_from_iperf(...)`
- `_build_tc_sweep_series(...)`

### Added shared plot renderer:\n- `_plot_tc_sweep_series(...)`
  - Uses the same TC sweep template (`mean` / `p50` / `p95`, same axis/title style)\n  - Draws one line per dataset for compare analysis\n  - Keeps `x` markers for non-OK rows from summary data

### Extended target function signature:\n- `analyze_tc_iperf_rx_by_suffix(session_raw_dir, session_fig_dir, dataset_suffix, compare_inputs=None, output_tag=None)`
  - `compare_inputs` format:\n    ```python\n    [\n       {\n           "raw_dir": <Path>, \n           "dataset_suffix": <str>, \n           "label": <str>},\n\n       ...\n\n       ]\n\n    ```
- Wired compare-mode call sites to use it: \n  - CLI `mode == "compare"` now runs comparator, then generates overlaid TC sweep compare charts. \n  - Auto group compare path (`check_and_run_group_compare`) also does the same after comparator output.

## Output behavior

### Single mode output remains:\n-  - `figure/tc_sweep/tc_sweep_rx_mean_<dataset>.png`\n-  - `figure/tc_sweep/tc_sweep_rx_p50_<dataset>.png`\n-  - `figure/tc_sweep/tc_sweep_rx_p95_<dataset>.png`\n-  - `figure/tc_sweep/tc_sweep_rx_stats_<dataset>.json`\n
### Compare mode output (using `output_tag`, typically compare folder name):
-  - `figure/tc_sweep/tc_sweep_rx_mean_<compare_tag>.png`\n-  - `figure/tc_sweep/tc_sweep_rx_p50_<compare_tag>.png`\n-  - `figure/tc_sweep/tc_sweep_rx_p95_<compare_tag>.png`\n-  - `figure/tc_sweep/tc_sweep_rx_stats_<compare_tag>.json`

## Validation

### Validation:\n+- AST parse OK\n+- No linter errors on edited file

