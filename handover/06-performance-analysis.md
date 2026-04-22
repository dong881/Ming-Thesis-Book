## Performance Analysis and Measurement Results

# Performance Analysis and Measurement Results

This document provides guidelines and examples for performance analysis and measurement results.

To ensure systematic completion of project milestones, track your daily progress and record work performed through two essential documents:

1. **Milestones** (milestones.md): Project roadmap with all tasks, deadlines, and completion status
2.  **Daily Logs** (daily-logs.md): Time-stamped record of work performed, linking tasks to study notes

## Application Deadline

**Application Deadline:** The date before the registration deadline for the next semester. (Please follow the school calendar.)


- [ ] 6.11 Upload digital thesis and submit one printed copy to the library
- [ ] 6.12 Download and complete the [School Leaving Application Form](https://www.academic.ntust.edu.tw/p/412-1048-8234.php?Lang=en) via the Student Information System
- [ ] 6.13 Submit a soft and yellow cover of the thesis to the department office
- [ ] 6.14 Submit a printed copy of the thesis and the signed e-Thesis Authorization Form (NTUST & NCL) to the library
- [ ] 6.15 Complete all steps in the School Leaving Application Form and collect your diploma at the Office of Graduate Studies

## Performance Analysis and Measurement Results

# Performance Analysis and Measurement Results
This document provides guidelines and examples for performance analysis and measurement results.
To ensure systematic completion of project milestones, track your daily progress and record work performed through two essential documents:
1. **Milestones** (milestones.md): Project roadmap with all tasks, deadlines, and completion status
2.  **Daily Logs** (daily-logs.md): Time-stamped record of work performed, linking tasks to study notes
## Application Deadline
**Application Deadline:** The date before the registration deadline for the next semester. (Please follow the school calendar.)
- [ ] 6.11 Upload digital thesis and submit one printed copy to the library
- [ ] 6.12 Download and complete the [School Leaving Application Form](https://www.academic.ntust.edu.tw/p/412-1048-8234.php?Lang=en) via the Student Information System
- [ ] 6.13 Submit a soft and yellow cover of the thesis to the department office
- [ ] 6.14 Submit a printed copy of the thesis and the signed e-Thesis Authorization Form (NTUST & NCL) to the library
- [ ] 6.15 Complete all steps in the School Leaving Application Form and collect your diploma at the Office of Graduate Studies


## Debugging Workflow

Update performance analysis and measurement results with reviewer feedback.

**Debugging Workflow"
## Table of Contents
### Daily log workflow diagram
![Daily log workflow diagram](./assets/daily-log.png)

## Known Issues and Troubleshooting Steps
*   [Git Commit](https://github.com/openairinterface5g/drivers/commit/7e4eba99)
    -   Fixed segment size in PNF and VNF configuration to ensure correct timing window usage.
*   [Git Commit](ht
    
    -   feat(rlc): add logging for RLC hold delay and average time to transmit
    
    ```diff
    diff --git a/executables/nr-softmodem.c b/executables/nr-softmodem.c
    index a57c464d1f..d779605300 100644
    --- a/executables/nr-softmodem.c
    +++ b/executables/nr-softmodem.c
    @@ -845,6 +845,8 @@ static void init_vnf_mmap_loggers(void)
      init_mmap_logger("vnf_harq_buffer");
      init_mmap_logger("vnf_harq_rtt");
      init_mmap_logger("vnf_rlc_runtime");
      ```

    +      init_mmap_logger("vnf_rlc_hol_delay");
+      init_mmap_logger("vnf_rlc_avg_to_tx");
      // Track continuous VNF-PNF latency measurements and advance timing
      init_mmap_logger("vnf_advance_time");
      init_mmap_logger("vnf-pnf-latency");
    diff --git a/openair2/LAYER2/nr_rlc/nr_rlc_oai_api.c b/openair2/LAYER2/nr_rlc/nr_rlc_oai_api.c
    index b63328b5de..fb10abcfb5 100644
    --- a/openair2/LAYER2/nr_rlc/nr_rlc_oai_api.c
    +++ b/openair2/LAYER2/nr_rlc/nr_rlc_oai_api.c
    @@ -292,6 +292,7 @@ static mac_rlc_status_resp_t _nr_rlc_status_ind(nr_rlc_ue_t *ue, frame_t frame,

      if (rb != NULL) {
        nr_rlc_entity_buffer_status_t buf_stat;
+        nr_rlc_statistics_t rlc_stats;
        rb->set_time(rb, get_nr_rlc_current_time());
        /* 38.321 deals with BSR values up to 81338368 bytes, after what it
         * reports '> 81338368' (table 6.1.3.1-2). Passing 100000000 is thus
@@ -300,6 +301,9 @@ static mac_rlc_status_resp_t _nr_rlc_status_ind(nr_rlc_ue_t *ue, frame_t frame,
        // Fix me: temproary reduction meanwhile cpu cost of this computation is optimized
        buf_stat = rb->buffer_status(rb, 1000 \* 1000);
        ret.bytes_in_buffer = buf_stat.status_size + buf_stat.retx_size + buf_stat.tx_size;
+        rb->get_stats(rb, &rlc_stats);
+        log_mmap_entry("vnf_rlc_hol_delay", (long)rlc_stats.txsdu_wt_us);
+        log_mmap_entry("vnf_rlc_avg_to_tx", (long)rlc_stats.txsdu_avg_time_to_tx);
      } else {
        if (!(frame % 128) || channel_idP == 0) //to suppress this warning message
          LOG_W(RLC, \
              "Radio Bearer (channel ID %d) is NULL for UE %d\n", channel_idP, ue->ue_id);
    ```
