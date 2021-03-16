import plotly.graph_objects as go

fig = go.Figure(data=[go.Table(
    header=dict(values=['n (no of coins)', 'k (no of required outcome)', '0', '1', '2', '3', '4'],
                line_color='darkslategray',
                fill_color='lightskyblue',
                align='left'),
    cells=dict(values=[[2,3,4],
                       ['Pr(X=k)','Pr(X\'=k)','Pr(X=k)'],
                       ['1/4','1/8','1/16'],
                       ['1/2','3/8','1/4'],
                       ['1/4','3/8','3/8'],
                       ['0','1/8','1/4'],
                       ['0','0','1/16']],
               line_color='darkslategray',
               fill_color='lightcyan',
               align='left'))
])

fig.update_layout(width=650, height=350)
fig.show()