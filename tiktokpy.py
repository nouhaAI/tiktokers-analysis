import numpy as np
import pandas as pd
import seaborn as sns
from sklearn import metrics
import plotly.express as px
from matplotlib import pyplot
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.figure_factory as ff

def convert_k_m(data:pd.DataFrame):
    zip_doc=zip(data['Subscribers count'],
                data['Views avg.'],
                data['Likes avg'],
                data['Comments avg.'],
                data['Shares avg'])
    subscribers_count= []
    views_avg=[]
    likes_avg=[]
    comments_avg=[]
    shares_avg=[]
    for subscribers, views, likes, comments, shares in zip_doc:
        if 'K' in subscribers :
            subscrib=subscribers.strip('K')
            subscrib=float(subscrib)*1000
            subscribers_count.append(round(subscrib))
        if 'M' in subscribers :
            subscrib=subscribers.strip('M')
            subscrib=float(subscrib)*1000000
            subscribers_count.append(round(subscrib))
        if 'K' in views :
            view=views.strip('K')
            view=float(view)*1000
            views_avg.append(round(view))
        if 'M' in views :
            view=views.strip('M')
            view=float(view)*1000000
            views_avg.append(round(view))
        if 'K' in likes :
            like=likes.strip('K')
            like=float(like)*1000
            likes_avg.append(round(like))
        if 'M' in likes :
            like=likes.strip('M')
            like=float(like)*1000000
            likes_avg.append(round(like))
        if 'K' in comments :
            comment=comments.strip('K')
            comment=float(comment)*1000
            comments_avg.append(round(comment))
        elif 'M' in comments :
            comment=comments.strip('M')
            comment=float(comment)*1000000
            comments_avg.append(round(comment))
        else:
            comment=float(comment)
            comments_avg.append(round(comment))        
        if 'K' in shares :
            share=shares.strip('K')
            share=float(share)*1000
            shares_avg.append(round(share))
        elif 'M' in shares :
            share=shares.strip('M')
            share=float(share)*1000000
            shares_avg.append(round(share))
        else:
            share=float(share)
            shares_avg.append(round(share)) 
    return subscribers_count, views_avg, likes_avg, comments_avg, shares_avg

def add_columns(data:pd.DataFrame,
                list1:list,
                list2:list,
                list3:list,
                list4:list,
                list5:list):
    data['followers']=list1
    data['views']=list2
    data['likes']=list3
    data['comments']=list4
    data['shares']=list5
    return data

def histogram(data:pd.DataFrame,
              column1:str,
              column2:str,
              title:str
              ):
    sorted_df=data.sort_values(by=column2)
    fig = px.histogram(sorted_df.tail(10), 
                       y=column1, 
                       x=column2,
                       title=title)
    fig.show()

def heatmap(data:pd.DataFrame):
    fig = px.imshow(round(data.corr(),1),
                    title='Correlation Heatmap')
    fig.show()
