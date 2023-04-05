# Matplotlib pie chart

Beloved and hated pie chart :D many people want it 

ChatGPT:

The `matplotlib` `pie()` function has a number of parameters that can be used to customize the appearance and behavior of the resulting pie chart. Below is a list of the most common settings:

* `x`: The data to be plotted as a pie chart, typically a 1D array-like object (e.g. list, pandas series).
* `labels`: A list of strings to use as labels for the wedges of the pie chart. The length of this list must match the length of the `x` array.
* `explode`: A list or array of values to specify the extent to which each wedge of the pie chart is offset from the center of the chart. This can be used to highlight a particular section of the chart.
* `colors`: A list or array of colors to use for the wedges of the pie chart. The length of this list must match the length of the `x` array.
* `autopct`: A string or function used to format the autopct labels. If a string is provided, it should contain a percent sign ("%") followed by a format specifier (e.g. "%.2f%%"). If a function is provided, it should take a single value and return a string to be used as the label.
* `startangle`: The angle at which the first wedge of the pie chart begins, measured in degrees clockwise from the 12 o'clock position.
* `shadow`: A boolean indicating whether or not to display a shadow behind the pie chart.
* `radius`: The radius of the pie chart as a fraction of the plot size. By default, the radius is set to 1, which means the chart will fill the available space.
* `counterclock`: A boolean indicating whether the wedges are drawn counterclockwise or clockwise. By default, wedges are drawn counterclockwise.
* `wedgeprops`: A dictionary of properties to be applied to the wedges of the pie chart, such as edge color or width.
* `textprops`: A dictionary of properties to be applied to the autopct labels, such as font size or color.
* `center`: A tuple specifying the (x, y) coordinates of the center of the pie chart. By default, the center is set to (0, 0), which means the chart is centered in the middle of the plot.
