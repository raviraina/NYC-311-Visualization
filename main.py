from bokeh.layouts import column
from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource, Select
import pandas as pd

# import our csv files into dataframes
df_zip = pd.read_csv('/home/rraina1/nyc_dash/zip_avg.csv')
df_month = pd.read_csv('/home/rraina1/nyc_dash/all_monthly_avg.csv')

# define x and y axis
x = df_month['month'].tolist()
y = df_month['response_time'].tolist()

# set menu items to our zip codes
zip_menu = df_zip['zip'].unique()
stringList = [str(zip_code) for zip_code in zip_menu]

# set values for x and y
check_value = df_zip['zip'].tolist()[0]
df = df_zip[df_zip['zip'] == check_value]
x_values_1 = df['month'].tolist()
x_values_2 = df['month'].tolist()
y_values_1 = df['response_time'].tolist()
y_values_2 = df['response_time'].tolist()

# set source to values
source_1 = ColumnDataSource(data={'x1': x_values_1, 'y1': y_values_1})
source_2 = ColumnDataSource(data={'x2': x_values_1, 'y2': y_values_2})

# set graph attributes for our lines
line_dash = 'solid'
all_line_color = 'purple'
zip1_line_color = 'orange'
zip2_line_color = 'green'
all_legend = 'All Zipcodes Response Average'
zip1_legend = 'Zipcode 1 Response Average'
zip2_legend = 'Zipcode 2 Response Average'

# start bokeh plot
TOOLTIPS = [
    ("Month", "$x"),
    ("Avg Response Time", "$y hours")
]

title = "311 Average Response Time by Zipcode"
plot = figure(title=title, tooltips=TOOLTIPS)
plot.line(x='x1', y='y1', source=source_1, line_color=zip1_line_color,
          line_dash=line_dash, legend_label=zip1_legend)
plot.line(x='x2', y='y2', source=source_2, line_color=zip2_line_color,
          line_dash=line_dash, legend_label=zip2_legend)

#name axis'
plot.xaxis.axis_label = 'Month'
plot.yaxis.axis_label = 'Average Reponse Time (Hours)'

# set zipcode menus
menu_1 = Select(options=stringList, title='Zipcode 1')
menu_2 = Select(options=stringList, title='Zipcode 2')

# define callbacks to update from menus
def callback(attr, old, new):
    df = df_zip[df_zip['zip'] == int(menu_1.value)]
    x_values_1 = df['month'].tolist()
    y_values_1 = df['response_time'].tolist()
    source_1.data = {'x1': x_values_1, 'y1': y_values_1}


def callback2(attr, old, new):
    df = df_zip[df_zip['zip'] == int(menu_2.value)]
    x_values_2 = df['month'].tolist()
    y_values_2 = df['response_time'].tolist()
    source_2.data = {'x2': x_values_2, 'y2': y_values_2}


# update values with callback
menu_1.on_change('value', callback)
menu_2.on_change('value', callback2)

# plot graph of selected value
plot.line(x, y, line_color = all_line_color,
          line_dash = line_dash, legend_label = all_legend)

# publish
curdoc().add_root(column(menu_1, menu_2, plot))





