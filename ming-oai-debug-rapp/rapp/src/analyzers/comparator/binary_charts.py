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
