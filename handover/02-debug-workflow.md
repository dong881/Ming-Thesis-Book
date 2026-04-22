# Debugging Workflow

Develop a detailed debug workflow, including known issues, troubleshooting steps, and error handling procedures.


### Debugging Workflow

#### Known Issues and Troubleshooting Steps

*   [Git Commit](https://github.com/openairinterface5g/drivers/commit/7e4eba99)
    -   Fixed segment size in PNF and VNF configuration to ensure correct timing window usage.
*   [Git Commit](https://github.com/ming-oai-debug-rapp/commit/933cacab)
    -   Adjusted slot-ahead value handling in auto_tester.py to prevent early stopping on VNF marker during UE re-attach retries.

# Debugging Workflow:
## Table of Contents
### Daily log workflow diagram
![Daily log workflow diagram](./assets/daily-log.png)

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

<p>Add known issues and troubleshooting steps to the existing section.</p>


## Debugging Workflow: 

> Add an overall comment with instructions on how to proceed with the comprehensive assessment.

This section provides guidelines for debugging workflow. Please refer to the [Lab Formatting Guidelines](https://labs.openairinterface.org/labs/doc/how-to/debugging-workflow/) for more information.
