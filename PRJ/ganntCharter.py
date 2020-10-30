import plotly.express as px
import pandas as pd

df = pd.DataFrame([
    dict(Task="Identify the concepts to teach ", Start='2020-10-30', Finish='2020-11-15'),
    dict(Task="Create the basic website ", Start='2020-10-30', Finish='2020-11-29'),
    dict(Task="Add interactive/animated examples ", Start='2020-11-30', Finish='2021-02-28'),
    dict(Task="Write report ", Start='2020-10-30', Finish='2021-04-08')
])

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task")
fig.update_yaxes(autorange="reversed") # otherwise tasks are listed from the bottom up
fig.show()