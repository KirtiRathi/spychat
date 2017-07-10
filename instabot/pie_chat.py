#import plotly
#import plotly.plotly as py
#import plotly.graph_objs as go

#labels = ['negative','positive']
#values = [40,60]

#trace = go.Pie(labels=labels, values=values)

#py.iplot([trace], filename='basic_pie_chart')



import plotly.plotly as py
import plotly.graph_objs as go

labels = ['negative','positive']
values = [40,60]
colors = ['#FEBFB3', '#E1396C']

trace = go.Pie(labels=labels, values=values,
               hoverinfo='label+percent', textinfo='value',
               textfont=dict(size=20),
               marker=dict(colors=colors,
                           line=dict(color='#000000', width=2)))

py.iplot([trace], filename='styled_pie_chart')
