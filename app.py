from flask import Flask, render_template
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import squarify as sq
import plotly.io as pio
pio.templates
import seaborn as sns
import resample as rs

app = Flask(__name__)

def load_data():
    df = pd.read_csv('dataset/cleaned_funding.csv')
    return df

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/graphs/1')
def graphs1():
   df=load_data()
   fig1 = px.pie(df[:15], values='Amount in USD', names='Industry Vertical', title='Amount in USD by Industry Vertical',
            color='Industry Vertical',
            labels={'Industry Vertical':'Industry Vertical'},
            width=1000, height=600,
            color_discrete_sequence=px.colors.sequential.RdBu)
   fig1.update_traces(textposition='inside', textinfo='percent+label', hole=0.4, marker=dict(line=dict(color='#000000', width=2)),
                   opacity=0.8, rotation=45, textfont_size=15, texttemplate='%{label}<br>%{value:$,.2f}'and '%{percent}')
   
   
   fig2 = px.histogram(df[:20], x="Amount in USD", y="Industry Vertical", color="Industry Vertical", hover_name="Startup Name", log_x=True,width=1000, height=600,
                title="Amount in USD by Industry Vertical", labels={"Amount in USD": "Amount in USD", "Industry Vertical": "Industry Vertical"}, template='plotly_white',
                color_discrete_sequence=px.colors.qualitative.Dark24, nbins=100, )
   
   fig3 = px.box(df[21:1000], y="Amount in USD", x="Industry Vertical", color= "Industry Vertical", hover_name="Startup Name", log_y=True, points=False,
             width=1000, height=600, title="Amount in USD by Industry Vertical", labels={"Amount in USD": "Amount in USD", "Industry Vertical": "Industry Vertical"},
             color_discrete_sequence=px.colors.qualitative.Dark24, template='plotly_white')
   
   fig4 = px.funnel(df[:30], x="Industry Vertical", y="Amount in USD", color="Industry Vertical",title="Amount in USD by Industry Vertical",  width=1100, height=600,
                labels={"Amount in USD": "Amount in USD", "Industry Vertical": "Industry Vertical"}, template='ggplot2',
                color_discrete_sequence=px.colors.qualitative.Dark24,)
   
   fig5 = px.density_contour(df[:25], x="Amount in USD", y="Industry Vertical", color="Industry Vertical", marginal_x="rug", marginal_y="histogram",
                         hover_data=df.columns, title='Amount in USD by Industry Vertical', width=1100, height=600, template='plotly_white')
   
   return render_template('graphs1.html',fig1=fig1.to_html(), fig2=fig2.to_html(), fig3=fig3.to_html(), fig4=fig4.to_html(), fig5=fig5.to_html())

@app.route('/graphs/2')
def graphs2():
   df=load_data()
   fig1 = px.area(df[:50], x="Amount in USD", y="City  Location", color="City  Location",
            template='plotly_white', width=1000, height=600, hover_data=df.columns, title='Amount in USD by City  Location',
            labels={'Amount in USD':'Amount in USD', 'City  Location':'City  Location', 'Startup Name':'Startup Name'},
            pattern_shape="Startup Name", pattern_shape_sequence=[".", "x", "+"])
   
   fig2 = px.bar(df[:30], x="City  Location", y="Amount in USD", color="City  Location", text="Amount in USD",
             color_discrete_sequence=px.colors.sequential.Plasma_r, template='plotly_white', width=1000, height=600, hover_data=df.columns,
             labels={'Amount in USD':'Amount in USD', 'City  Location':'City  Location'},
             title='Amount in USD by City  Location'
             )
   
   fig3 = px.bar(df[400:420], y="City  Location", x="Amount in USD", color="Amount in USD", text="Amount in USD",
             color_discrete_sequence=px.colors.sequential.Plasma_r, template='plotly_white', width=1000, height=600, hover_data=df.columns,
             labels={'Amount in USD':'Amount in USD', 'City  Location':'City  Location'},
             title='Amount in USD by City  Location'
             )
   
   fig4 = px.funnel(df[:50], y="City  Location", x="Amount in USD", color="City  Location",title="Amount in USD by City Location",  width=1000, height=600,
                labels={"Amount in USD": "Amount in USD", "Industry Vertical": "Industry Vertical"}, template='ggplot2',
                color_discrete_sequence=px.colors.qualitative.Dark24)
   
   fig5 = px.bar_polar(df[:228], r="City  Location", theta="Amount in USD", color="City  Location",
                    template="none", title='Amount in USD by City Location ', height=600, width=1000,
                     labels={"Amount in USD": "Amount in USD", "Industry Vertical": "Industry Vertical"},
                    color_discrete_sequence= px.colors.sequential.Plasma_r)
   
   fig6 =  px.line_polar(df[:100], theta="Amount in USD", r="City  Location", color="Industry Vertical", line_close=True,
                    color_discrete_sequence=px.colors.sequential.Plasma_r,
                    template="plotly_white", title='Amount in USD by City  Location',
                    height=600, width=1000, hover_data=df.columns, labels={'City  Location':'City  Location', 'Amount in USD':'Amount in USD'})
   return render_template('graphs2.html',fig1=fig1.to_html(), fig2=fig2.to_html(), fig3=fig3.to_html(), fig4=fig4.to_html(), fig5=fig5.to_html())
   
@app.route('/graphs/3')
def graphs3():
   df=load_data()
   fig1 = px.area(df[:45], x="Amount in USD", y="Startup Name", color="Industry Vertical",
            template='plotly_white', width=1000, height=600, hover_data=df.columns, title='Amount in USD by Startup Name',
            labels={'Amount in USD':'Amount in USD', 'City  Location':'City  Location', 'Startup Name':'Startup Name'},
            pattern_shape="Startup Name", pattern_shape_sequence=[".", "x", "+"])
   
   fig2 = px.bar(df[:30], y='Amount in USD', x='Startup Name', color='Industry Vertical', title='Amount in USD by Startup Name',
                color_discrete_sequence=px.colors.sequential.Plasma_r, template='plotly_white', width=1000, height=600, hover_data=df.columns,
                labels={'Amount in USD':'Amount in USD', 'City  Location':'City  Location'})
   
   fig3 = px.pie(df[:20], values='Amount in USD', names='Startup Name', title='Amount in USD by Startup Name', width=1000, height=600,
             color='Startup Name', labels={'City  Location':'City  Location', 'Amount in USD':'Amount in USD', 
                                           'Startup Name':'Startup Name', 'Industry Vertical':'Industry Vertical', },
             template='none', color_discrete_sequence=px.colors.sequential.Plasma_r
        )
   
   fig4 = px.line_polar(df[:750], theta="Amount in USD", r="Startup Name",color='Startup Name', symbol="Startup Name", line_close=True,
                    color_discrete_sequence=px.colors.sequential.Plasma_r,
                    template="plotly_white", title='Amount in USD by Startup Name',
                    height=600, width=1000, hover_data=df.columns, labels={'City  Location':'City  Location', 'Amount in USD':'Amount in USD'})
   
   fig5 = px.funnel(df[:25], y="Startup Name", x="Amount in USD", color="Startup Name",title="Amount in USD by City Location",  width=1000, height=600,
                labels={"Amount in USD": "Amount in USD", "Industry Vertical": "Industry Vertical"}, template='ggplot2',
                color_discrete_sequence=px.colors.qualitative.Dark24)
   return render_template('graphs3.html',fig1=fig1.to_html(), fig2=fig2.to_html(), fig3=fig3.to_html(), fig4=fig4.to_html(), fig5=fig5.to_html())
   
@app.route('/graphs/4')
def graphs4():
   df=load_data()
   fig1 = px.bar(df[:50], x="Startup Name", y="InvestmentnType", color="InvestmentnType", text="Amount in USD", 
                 width=1000, height=600)
   
   fig2 =  px.treemap(df[400:500], path=['Startup Name', 'InvestmentnType'], values='Amount in USD',
                       title='Amount in USD by Startup Name and InvestmentnType', width=1000, height=600)
   
   fig3 = px.pie(df[10:25], values='Amount in USD', names='InvestmentnType', title='Amount in USD by InvestmentnType', width=1000, height=600,
                color='InvestmentnType')
   
   fig4 = px.histogram(df[:50], x="Amount in USD", y="InvestmentnType", color="InvestmentnType", marginal="rug", hover_data=df.columns,
                     title='Amount in USD by InvestmentnType', width=1000, height=600, template='plotly_white')
   
   #fig5 = 
         

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 