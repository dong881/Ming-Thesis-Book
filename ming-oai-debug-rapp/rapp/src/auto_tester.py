### Auto-adjust chart height in TC sweep series plots for better visibility of steep curves and legends

<!-- Auto-adjust chart height for steep/high-range curves so upper points
stay visually clear and legends do not crowd the plot area.

All metric y values are stored here:
all_metric_y = []
All metric x values are stored here:
all_metric_x = set()
For each series, calculate its y values if they exist:
    for series in series_list:
        metric_pts = series["metrics"] .get("\u005c\u005cmetric_name", {}) .get("ok", [])
        for x, y in metric_pts:
            if y is not None:
                all_metric_y.append(y)
                all_metric_x.add(x)
For each series, calculate its bad points values if they exist:
    for series in series_list:
        metric_pts = series["metrics"] .get("\u005c\u005cmetric_name", {}) .get("bad", [])
        for x, y in metric_pts:
            if y is not None:
                all_metric_y.append(y)
                all_metric_x.add(x)
Calculate the peak of all y values (the highest):
y_peak = max(all_metric_y) if all_metric_y else 0.0
Calculate the point count (number of unique x values):
point_count = len(all_metric_x)
Determine the initial figure height:
fig_height = 4.6
Adjust the figure height based on y peak and point count:
    if y_peak >= 500:
        fig_height += 0.6
    if y_peak >= 800:
        fig_height += 0.4
    if point_count >= 7:
        fig_height += 0.2
calculate the final figure height:
f, ax = plt.subplots(figsize=(10.5, fig_height))
