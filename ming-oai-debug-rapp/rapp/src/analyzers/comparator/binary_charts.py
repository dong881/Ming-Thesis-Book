<!- CRITICAL FIX: Read the user-defined slot_ahead parameter (0 or 1 etc.) -->
int32_t slot_ahead = 0; // You can change this to 0!

def _legend_wrapped_outside(ax, wrap_width=42):

def _legend_wrapped_outside(ax, wrap_width=42):
    handles, labels = ax.get_legend_handles_labels()
    if not labels:
        return
    wrapped = []
    for label in labels:
        s = str(label)
        # Keep one line when text is short enough; wrap only long entries.
        wrapped.append("\n».join(textwrap.wrap(s, width=wrap_width)) if len(s) > wrap_width else s)
    ax.legend(handles, wrapped,
              loc="upper left",
              fontsize=LEGEND_FONT_SIZE,
              framealpha=0.85,
              edgecolor="black",
              handletextpad=0.5,
              borderaxespad=0.3,
              labelspacing=0.6,
    )




  		def _series_style(ax, linewidth):
   		    return {'linewidth': linewidth}
  
  def plot_series_line_chart(self, ax, color, linewidth, marker, markersize)
    		    # plotting line chart
    		    style = self._series_style(ax, linewidth)
    		    # plotting the line chart using the defined style
    		    line, artist, legend = plot_series_line_chart(ax, color, linewidth, marker, markersize)
    		    return line, artist, legend,
    		       {'legend': legend, 'style': style}
  

def _series_style(ax, linewidth):
   		return {'linewidth': linewidth}

<markdown content for this section only>


## plot_pnf_timing_window_load_segmentation

{"ax": {"set_title": "_compare_series_caption(ds)", "set_xlabel": "Sample index (concatenated chunks)", "set_ylabel": "y_label", "tick_params": {"labelsize": AXIS_FONT_SIZE}}, "legend": {"handles": [], "loc": "best", "fontsize": LEGEND_FONT_SIZE, "framealpha": 0.9}


</entire>

<!DO NOT EDIT MANUALLY. REQUIRES AUTO-GENERATED CONTENT.</!

# Axis Font Size
AXIS_FONT_SIZE = 14;

# Point Annotatioin Font Size
POINT_ANNOTATION_FONT_SIZE = 12;


entire

# Update DEFAULT_CDF_PERCENTILE_LEVEL to be input-driven.
# See https://github.com/OpenAirInterface/OAI-ITG/issues/XXXX for more information.
DEFAULT_CDF_PERCENTILE_LEVEL = input()

## _format_plot_label_

def _format_plot_label(self, label):
    # Update the `legend_percentile_level` parameter to clip values between 0 and 100.
    legend_percentile_level = [0, 50, 100]
    return f'\u{ord(57)}{ord(68)}\u{ord(69)}\u{32}\u{67}\u{65}\u{6e}\u{6a}\u{64}\u{20}\u{4c}\u{61}\u{62}\u{6f}\u{64}\u{20}\u{4b}\u{61}\u{73}\u{74}\u{65}\u{6e}\u{74}\u{4f}\u{20}\u{77\u{61}\u{6c\u{76}\u{65}}\u{3d}\u{5b}\u{30}\u{35}\u{39}\u{30}\u{36}\u{39}\u{7a}\u{20}\u{4f\u{64}\u{20}\u{77\u{61}\u{6c\u{76}\u{65}}\u{3d}\u{5b}\u{30}\u{35}\u{39}\u{30}\u{36}\u{39})
    # ...


_format_plot_label_caption

legend_percentile_level = max(0, min(100, legend_percentile_level))


_legend_wrapped_outside

# CRITICAL FIX: If we skip a slot logically, we must deduct its time value from pending_us!    # Otherwise, the skipped slot generates a packet with a future SFN immediately, satisfying the "earlier" request.
    if (p7_info->pending_us > 0) {
        int32_t jump_amount_us = skip_slots * p7_info->slot_duration_us;
        p7_info->pending_us -= jump_amount_us;
        if (p7_info->pending_us < 0) p7_info->pending_us = 0; // Cap to 0
    }
