import plotly.graph_objects as go

fig = go.Figure(data=[go.Table(
    header=dict(values=['k', '0', '1', '2', '3'],
                line_color='darkslategray',
                fill_color='lightskyblue',
                align='left'),
    cells=dict(values=[['Pr(k)'],['1/8'],['3/8'],['3/8'],['1/8']],
               line_color='darkslategray',
               fill_color='lightcyan',
               align='left'))
])

fig.update_layout(width=500, height=300)
fig.show()