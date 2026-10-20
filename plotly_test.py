import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
import dtg
import datetime
#d,c=input('輸入').split()
def plot_show(d,c):
    if d==None:
        return 2
    if c==None:
        return 3
    try :
        line1,line2,d1,vol,clos,op,high,low=dtg.dg(d,c)
    except ValueError:
        return 1
    
    fig=make_subplots(rows=2, cols=1,shared_xaxes=True,vertical_spacing=0.1,subplot_titles=(c,))
    fig.add_trace(go.Scatter(x=d1,y=line1,mode='lines+markers',name='VWMA',line=dict(color='blue')),row=1,col=1)
    fig.add_trace(go.Scatter(x=d1,y=line2,mode='lines+markers',name='SMA',line=dict(color='red')),row=1,col=1)
    fig.add_trace(go.Candlestick(x=d1,close=clos,open=op,high=high,low=low,name='Price',
                                increasing=dict(line=dict(color='red'),fillcolor='rgba(217, 35, 35,0.5)'),
                                decreasing=dict(line=dict(color='green'),fillcolor='rgba(127, 245, 180,0.5)')),
                                row=1,col=1)
    fig.add_trace(go.Bar(x=d1,y=vol,name='成交量'),row=2,col=1)
    fig.update_layout(title='VWMA & SMA',xaxis_title='Date',yaxis_title='Value',xaxis_rangeslider_visible=True,height=600)
    print('high=', max(high))
    print('low =', min(low))
    fig.show(renderer='browser')
    return 0
