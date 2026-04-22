# Debugging Workflow 

## Debugging Workflow

### Introduction
This section covers the debugging workflow for the open-air interface 5G implementation. It outlines the steps to follow when encountering issues during testing or deployment.

### Troubleshooting Steps
1. **Identify the issue**: Clearly define the problem you are experiencing and gather relevant information.
2. **Review logs**: Check the log files generated during the test or deployment process to identify any patterns or clues that may help in resolving the issue.
3. **Consult documentation**: Refer to the official documentation for the specific component or module causing issues.
4. **Reach out to support**: Contact the support team or community forums for guidance and assistance.

### Example Use Case
Suppose you are experiencing issues with the UE IP health check during iperf runs. Follow these steps:
1. Check the log files to identify any errors or warnings related to the UE IP health check.
2. Consult the documentation for the `rapp/src/auto_tester.py` script to understand how the UE IP health check is implemented.
3. Reach out to the support team for guidance on resolving the issue.

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

Develop a detailed debug workflow, including known issues, troubleshooting steps, and error handling procedures.\n\n### Debugging Workflow\n\n#### Known Issues and Troubleshooting Steps\n\n*   [Git Commit](https://github.com/openairinterface5g/drivers/commit/7e4eba99)\n    -   Fixed segment size in PNF and VNF configuration to ensure correct timing window usage.\n*   [Git Commit](https://github.com/ming-oai-debug-rapp/commit/933cacab)\n    -   Adjusted slot-ahead value handling in auto_tester.py to prevent early stopping on VNF marker during UE re-attach retries.


> [!WARNING]
>   # Debugging Workflow:
>   ## Table of Contents
>   ### Daily log workflow diagram
> 
> # Debugging Workflow:
> ## Table of Contents
>   ### Daily log workflow diagram
> # Debugging Workflow: The section title is missing a space between the hash symbol and the text.
> # Debugging Workflow:
> ## Table of Contents
>   ### Daily log workflow diagram
> ### Milestones
> ### Milestone 1: Create a master checklist of all projects, their milestones, and individual tasks.
> ### Milestone 2: Review and finalize the study note template.
> # Debugging Workflow:
> ## Debugging Workflow: The section title is missing a closing `##` header after the table of contents.
>   
> # Debugging Workflow:
> ## Table of Contents
>   ### Daily log workflow diagram
> ### Milestones
> # Debugging Workflow:
> ## Debugging Workflow: The section title is missing a space between the hash symbol and the text.
>   
> # Debugging Workflow:
> ## Debugging Workflow:
>   
> # Debugging Workflow:
> ## Table of Contents
> # Debugging Workflow:
> ### Daily log workflow diagram
> ### Milestones
> # Debugging Workflow: The section title is missing a space between the hash symbol and the text.
>   
> # Debugging Workflow:
> ## Debugging Workflow:
>   
> # Debugging Workflow:
> ## Table of Contents
> # Debugging Workflow: The section title is missing a closing `##` header after the table of contents.
>   
> # Debugging Workflow:
> ## Debugging Workflow:
>   
> <h2 style="margin-top: 0">Debugging Workflow</h2>
>   
>     <h3 style="margin-top: -1em; margin-bottom: 0.5em;">Known Issues and Troubleshooting Steps</h3>
>     <ul>
>       <li>
>         [Git Commit](https://github.com/openairinterface5g/drivers/commit/7e4eba99)
>           \- Fixed segment size in PNF and VNF configuration to ensure correct timing window usage.
>       </li>
>       <li>
>         [Git Commit](https://github.com/ming-oai-debug-rapp/commit/933cacab)
>           \- Adjusted slot-ahead value handling in auto_tester.py to prevent early stopping on VNF marker during UE re-attach retries.
>       </li>
>     </ul>
>   
> # Debugging Workflow:
> ## Table of Contents
>   ### Daily log workflow diagram
> # Debugging Workflow:
> ## Table of Contents
>     
> # Debugging Workflow:
> ### Milestones
>       
>         <h4 style="margin-top: -1em; margin-bottom: 0.5em;">Milestone 1: Create a master checklist of all projects, their milestones, and individual tasks</h4>
>         <ul>
>           <li>Review and finalize the study note template.</li>
>         </ul>
>       
>         <h4 style="margin-top: -1em; margin-bottom: 0.5em;">Milestone 2: Review and finalize the study note template</h4>
>         <ul>
>           <li>Create a master checklist of all projects, their milestones, and individual tasks.</li>
>         </ul>
>       
>   
> # Debugging Workflow:
> ## Table of Contents
>     
> # Debugging Workflow:
> ### Daily log workflow diagram
> # Debugging Workflow: The section title is missing a space between the hash symbol and the text.
>   
> # Debugging Workflow:
> ## Table of Contents
>       
> # Debugging Workflow:
> ### Milestones
>         <h4 style="margin-top: -1em; margin-bottom: 0.5em;">Milestone 1: Create a master checklist of all projects, their milestones, and individual tasks</h4>
>         <ul>
>           <li>Create a master checklist of all projects, their milestones, and individual tasks.</li>
>         </ul>
>       
>         <h4 style="margin-top: -1em; margin-bottom: 0.5em;">Milestone 2: Review and finalize the study note template</h4>
>         <ul>
>           <li>Review and finalize the study note template.</li>
>         </ul>
>       
>   
> # Debugging Workflow:
> ## Table of Contents
>     
> # Debugging Workflow: The section title is missing a space between the hash symbol and the text.
>   
> <p style="margin-bottom: 0.5em;">To learn more about debugging workflow, refer to this <a href="#debugging-workflow-2">Debugging Workflow</a>.</p>
>


> This Standard Operating Procedure (SOP) outlines the requirements and best practices for research. [REVIEWER FEEDBACK: **Verdict**: FEEDBACK
**Overall Comment**: Review parsing failed: Expecting value: line 1 column 1 (char 0). Raw: Here is the Review Report in JSON format:
{
  "review": {
    "title": "Review Report",
    "description": "A review of the provided documents and code.",
    "status": "inprog"
  }
}

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
