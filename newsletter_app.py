# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import dash_bootstrap_components as dbc

### Local modules
# from data_loader import load_newsletter_data
# from newsletter_filters import filters_section
from block1 import block1
from block2 import block2
from block3 import block3
from racial_equity_block import accordion_block
# from racial_equity_filters import re_filters_section

import requests
from io import StringIO

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
###
# | data_loader.py
###
base_url = 'https://raw.githubusercontent.com/cdeleonc/newsletter-app/main/assets/'

newsletter_counts_url = base_url + 'newsletter_counts.csv'
newsletter_counts_df = pd.read_csv(StringIO(requests.get(newsletter_counts_url).text))

active_counts_by_proj_type_url = base_url + 'newsletter_active_counts_by_proj_type.csv'
active_counts_by_proj_type_df = pd.read_csv(StringIO(requests.get(active_counts_by_proj_type_url).text))

newsletter_housed_counts_by_destination_url = base_url + 'newsletter_housed_counts_by_destination_by_race.csv'
newsletter_housed_counts_by_destination_df = pd.read_csv(StringIO(requests.get(newsletter_housed_counts_by_destination_url).text))

newsletter_counts_by_race_url = base_url + 'newsletter_counts_by_race.csv'
newsletter_counts_by_race_df1 = pd.read_csv(StringIO(requests.get(newsletter_counts_by_race_url).text))
old_cols = [x for x in newsletter_counts_by_race_df1.columns if 'by Race' in x]
new_cols = [x.split(" by ")[0] for x in newsletter_counts_by_race_df1 if 'by Race' in x]
newsletter_counts_by_race_df1 = newsletter_counts_by_race_df1.rename(columns=dict(zip(old_cols, new_cols)))

newsletter_active_counts_by_proj_type_by_race_url = base_url + 'newsletter_active_counts_by_proj_type_by_race.csv'
newsletter_active_counts_by_proj_type_by_race = pd.read_csv(StringIO(requests.get(newsletter_active_counts_by_proj_type_by_race_url).text))

# 
binary_race_data_counts_url = base_url + 'binary_race_data_counts_df.csv'
binary_race_data_counts_df = pd.read_csv(StringIO(requests.get(binary_race_data_counts_url).text))
binary_race_data_percent_by_pop_url = base_url + 'binary_race_data_percent_by_pop_df.csv'
binary_race_data_percent_by_pop_df = pd.read_csv(StringIO(requests.get(binary_race_data_percent_by_pop_url).text))
binary_race_likeliness_data_url = base_url + 'binary_race_likeliness_data_df.csv'
binary_race_likeliness_data_df = pd.read_csv(StringIO(requests.get(binary_race_likeliness_data_url).text))

#
active_binary_race_data_counts_url = base_url + 'active_binary_race_data_counts_df.csv'
active_binary_race_data_counts_df = pd.read_csv(StringIO(requests.get(active_binary_race_data_counts_url).text))
active_binary_race_data_percent_by_pop_url = base_url + 'active_binary_race_data_percent_by_pop_df.csv'
active_binary_race_data_percent_by_pop_df = pd.read_csv(StringIO(requests.get(active_binary_race_data_percent_by_pop_url).text))
active_binary_race_likeliness_data_url = base_url + 'active_binary_race_likeliness_data_df.csv'
active_binary_race_likeliness_data_df = pd.read_csv(StringIO(requests.get(active_binary_race_likeliness_data_url).text))

#
housed_binary_race_data_counts_url = base_url + 'housed_binary_race_data_counts_df.csv'
housed_binary_race_data_counts_df = pd.read_csv(StringIO(requests.get(housed_binary_race_data_counts_url).text))
housed_binary_race_data_percent_by_pop_url = base_url + 'housed_binary_race_data_percent_by_pop_df.csv'
housed_binary_race_data_percent_by_pop_df = pd.read_csv(StringIO(requests.get(housed_binary_race_data_percent_by_pop_url).text))
housed_binary_race_likeliness_data_url = base_url + 'housed_binary_race_likeliness_data_df.csv'
housed_binary_race_likeliness_data_df = pd.read_csv(StringIO(requests.get(housed_binary_race_likeliness_data_url).text))

#
binary_pit_data_url = base_url + 'binary_pit_data_df.csv'
binary_pit_data_df = pd.read_csv(StringIO(requests.get(binary_pit_data_url).text))
calc_pit_data_url = base_url + 'calc_pit_data_df.csv'
calc_pit_data_df = pd.read_csv(StringIO(requests.get(calc_pit_data_url).text))
pit_data_likely_url = base_url + 'pit_data_likely_df.csv'
pit_data_likely_df = pd.read_csv(StringIO(requests.get(pit_data_likely_url).text))
pit_data_url = base_url + 'pit_data_df.csv'
pit_data_df = pd.read_csv(StringIO(requests.get(pit_data_url).text))

race_picklist = sorted(list(newsletter_counts_by_race_df1['static_demographics.race_text'].unique()))
###
# | END
# | data_loader.py
###


###
# | newsletter_filters.py
###
radio_button_group = html.Div([
    dcc.Dropdown(
        id='report-window',
        options=[{'label': window, 'value': window} for window in newsletter_counts_df["Reporting Window"].unique()],
        value='Monthly',
        placeholder="Select a reporting window",
    ),
    html.Div(id="output"),
], className="radio-group")


dropdown_options = [{'label': race, 'value': race} for race in race_picklist]
dropdown_value = [x for x in race_picklist if x not in ["Client doesn't know", "Client refused", "Data not collected"]]

checkbox_button_group = html.Div(
    [
        dcc.Dropdown(
            id="race_option",
            options=dropdown_options,
            value=dropdown_value,
            multi=True,
        ),
        html.Div(id="output1"),
    ],
    className="radio-group",
)

filters_section = dbc.Card(
    [
        dbc.CardHeader("Filters"),
        dbc.CardBody(
            [
                dbc.Row(
                    [
                        dbc.Col([
                            html.P("Select Reporting Window", className='filter_titles'),
                            radio_button_group],
                            width=12, sm=12, md=12, lg=4, xl=4
                        ),
                        dbc.Col([
                            html.P("Select Reporting Period", className='filter_titles'),
                            dcc.Dropdown(
                                options=['Jan-2023', 'Dec-2022', 'Nov-2022', 'Oct-2022', 'Sep-2022'],
                                value='Jan-2023',
                                id='year-slider'
                            )],
                            width=12, sm=12, md=12, lg=4, xl=4
                        ),
                        dbc.Col([
                            html.P("Race Filter", className='filter_titles'),
                            checkbox_button_group],
                            width=12, sm=12, md=12, lg=4, xl=4
                        ),
                    ]
                ),
            ]
        ),
    ],
    className="mb-3"
)
###
# | END |
# | newsletter_filters.py
###

###
# | racial_ewuity_filters.py
###
years_list = sorted(list(set(binary_race_data_counts_df['Year']).union(set(binary_race_data_percent_by_pop_df['Year'])).union(set(binary_race_likeliness_data_df['Year']))))
proj_type_list = sorted([x for x in list(set(binary_race_data_counts_df.columns).union(set(binary_race_data_percent_by_pop_df.columns)).union(set(binary_race_likeliness_data_df.columns))) if x not in ['Binary Race Variable',  'Unnamed: 0', 'Year']])
race_variable_list = sorted(list(set(binary_race_data_counts_df['Binary Race Variable']).union(set(binary_race_data_percent_by_pop_df['Binary Race Variable'])).union(set(binary_race_likeliness_data_df['Binary Race Variable']))))

re_filters_section = dbc.Card(
    [
        dbc.CardHeader("Filters"),
        dbc.CardBody(
            [
                dbc.Row(
                    [
                        dbc.Col([
                            html.P("Select Reporting Year", className='filter_titles'),
                            dcc.Dropdown(
                                options=years_list,
                                value=years_list[-1],
                                id='racial-equity-select-year'
                            )],
                            width=12, sm=12, md=12, lg=4, xl=4
                        ),
                        dbc.Col([
                            html.P("Select Project Type", className='filter_titles'),
                            dcc.Dropdown(
                                options=proj_type_list,
                                value=proj_type_list[0],
                                id='racial-equity-select-project-type'
                            )],
                            width=12, sm=12, md=12, lg=4, xl=4
                        ),
                        dbc.Col([
                            html.P("Select Race", className='filter_titles'),
                            dcc.Dropdown(
                                options=race_variable_list,
                                value=race_variable_list[0],
                                id='racial-equity-select-race'
                            )],
                            width=12, sm=12, md=12, lg=4, xl=4
                        ),                        
                    ]
                ),
            ]
        ),
    ],
    className="mb-3"
)
###
# | END
# | racial_ewuity_filters.py
###


color_dict = {}
color_palette = px.colors.qualitative.Plotly

app.layout = dbc.Tabs([
    dbc.Tab(
        dbc.Container(
            children=[
                filters_section,
                html.Div(
                    className="container",
                    children=[
                        html.Div(
                            children=[block1]
                        ),
                        html.Div(
                            children=[block2]
                        ),
                        html.Div(
                            children=[block3]
                        ),
                    ]
                )
            ]
        ), label="HMIS Data Newsletter", active_label_style={'color':'grey', 'font-weight':'bolder'}, label_style={'color': 'white'}),
    dbc.Tab(
        dbc.Container(
            children=[
                re_filters_section,
                accordion_block
            ]
        ),
        label='Racial Equity Statements',active_label_style={'color':'grey', 'font-weight':'bolder'}, label_style={'color': 'white'}),
    ]
)

###
# | callbacks.py
###
color_dict = {}
color_palette = px.colors.qualitative.Plotly

@app.callback(
    Output('active_counts_pie', 'figure'),
    Input('year-slider', 'value'),
    Input('report-window', 'value'),
    Input('race_option', 'value'),)
def update_figure(selected_year, report_window, race_option):
    filtered_df = newsletter_active_counts_by_proj_type_by_race[(newsletter_active_counts_by_proj_type_by_race['Reporting Month'] == selected_year) & (newsletter_active_counts_by_proj_type_by_race['Reporting Window'] == report_window) & (newsletter_active_counts_by_proj_type_by_race['static_demographics.race_text'].isin(race_option))].reset_index(drop=True)
    
    fig = px.pie(filtered_df, names="Project Type", values="Active Clients Count", labels='abbrev', hole=.7, color_discrete_sequence=px.colors.qualitative.Vivid[:len(filtered_df)],)
    active_client_count = filtered_df['Active Clients Count'].sum()
    fig.update_layout({
        "margin_l":0,
        "margin_r":120,
        'plot_bgcolor': 'rgba(0,0,0,0)',
        'paper_bgcolor': 'rgba(0,0,0,0)',
        'legend_font': {"color":"rgba(255,255,255,0.95)"},
        "legend_title_text":"HMIS Project Types",
        "legend_title_side":"top",
        "legend_yanchor":"top",
        "legend_y":.85,
        "legend_xanchor":"right",
        "legend_x":2.1})

    fig.update_traces(
        textposition="auto",
        insidetextorientation="horizontal", 
        insidetextfont_color="white",
        outsidetextfont_color="white",
    )

    return fig
# @app.callback(
#     Output('active_counts_pie', 'figure'),
#     Input('year-slider', 'value'),
#     Input('report-window', 'value'),
#     Input('race_option', 'value'),)
# def update_figure(selected_year, report_window, race_option):
#     filtered_df = newsletter_active_counts_by_proj_type_by_race[(newsletter_active_counts_by_proj_type_by_race['Reporting Month'] == selected_year) & (newsletter_active_counts_by_proj_type_by_race['Reporting Window'] == report_window) & (newsletter_active_counts_by_proj_type_by_race['static_demographics.race_text'].isin(race_option))].reset_index(drop=True)
    
#     fig = px.pie(filtered_df, names="Project Type", values="Active Clients Count", labels='abbrev', hole=.7)
#     fig.update_layout({
#         "margin_l":0,
#         "margin_r":120,
#         'plot_bgcolor': 'rgba(0,0,0,0)',
#         'paper_bgcolor': 'rgba(0,0,0,0)',
#         'legend_font': {"color":"rgba(255,255,255,0.95)"},
#         "legend_title_text":"HMIS Project Types",
#         "legend_title_side":"top",
#         "legend_yanchor":"top",
#         "legend_y":.85,
#         "legend_xanchor":"right",
#         "legend_x":2.1})

#     fig.update_traces(
#         textposition="auto",
#         insidetextorientation="horizontal", 
#         insidetextfont_color="white",#"rgba(255,255,255,1)",
#         outsidetextfont_color="white"#"rgba(255,255,255,1)"
#         )

#     return fig

@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value'),
    Input('report-window', 'value'),
    Input('race_option', 'value'),)
def update_figure(selected_year, report_window, race_option):
    filtered_df = newsletter_housed_counts_by_destination_df[(newsletter_housed_counts_by_destination_df['Reporting Month'] == selected_year) & (newsletter_housed_counts_by_destination_df['Reporting Window'] == report_window) & (newsletter_housed_counts_by_destination_df['static_demographics.race_text'].isin(race_option))].reset_index(drop=True)

    # Sort the dataframe by 'clients.unique_identifier' in descending order
    filtered_df = filtered_df.sort_values('clients.unique_identifier', ascending=True)

    # Create color_dict and assign a color to each category in names argument
    for i, name in enumerate(filtered_df['static_demographics.race_text'].unique()):
        if name not in color_dict:
            color_dict[name] = color_palette[i % len(color_palette)]

    fig = px.bar(filtered_df, y='Permanent Destination', x='clients.unique_identifier', orientation='h', color='static_demographics.race_text', text_auto=True, color_discrete_map=color_dict)
    fig.update_layout({
    'plot_bgcolor': 'rgba(0,0,0,0)',
    'paper_bgcolor': 'rgba(0,0,0,0)',
    'legend_bgcolor': "rgba(1,1,1,1)",
    "showlegend":False,
    'yaxis_title':"",
    'uniformtext_minsize': 12,
    'uniformtext_mode': 'hide',
    })
    fig.update_xaxes(visible=False)
    fig.update_yaxes(
        tickmode="array",
        categoryorder="total ascending",
        ticklabelposition="outside",
        tickfont=dict(color="white"), matches=None, showticklabels=True, visible=True
    )

    return fig

@app.callback(
    Output(component_id='fth_count', component_property='children'),
    Output(component_id='housed_count', component_property='children'),
    Output(component_id='new_entries_count', component_property='children'),
    Output(component_id='new_referrals_count', component_property='children'),
    Output(component_id='seniors_active_count', component_property='children'),
    Output(component_id='tay_active_count', component_property='children'),
    Output(component_id='families_active_count', component_property='children'),
    Output(component_id='veterans_active_count', component_property='children'),
    Output(component_id='housed_count_1', component_property='children'),
    Output(component_id='senior_housed_count', component_property='children'),
    Output(component_id='tay_housed_count', component_property='children'),
    Output(component_id='families_housed_count', component_property='children'),
    Output(component_id='veterans_housed_count', component_property='children'),
    Output(component_id='active_count', component_property='children'),
    Input('year-slider', 'value'),
    Input('report-window', 'value'),
    Input('race_option', 'value'),)
def update_metrics(selected_year, report_window, race_option):
    temp_df = newsletter_counts_by_race_df1[(newsletter_counts_by_race_df1['Reporting Month']==selected_year) & (newsletter_counts_by_race_df1['Reporting Window']==report_window) & (newsletter_counts_by_race_df1['static_demographics.race_text'].isin(race_option))]
    d = {col: temp_df[col].sum() for col in temp_df if 'Count' in col}
    return (
        d['FTH Count'], 
        d['Housed Count'], 
        d['New Program Entries Count'], 
        d['New Referrals Count'],
        d['Active Seniors Count'], 
        d['Active TAY Count'],
        d['Active Families Count'],
        d['Active Veterans Count'],
        d['Housed Count'], 
        d['Housed Seniors Count'],
        d['Housed TAY Count'],
        d['Housed Families Count'],
        d['Housed Veterans Count'],
        d['Active Count'],
        )

@app.callback(
    Output('fth_race_plot', 'figure'),
    Output('housed_race_plot', 'figure'),
    Output('new_entries_race_plot', 'figure'),
    Output('new_referrals_race_plot', 'figure'),
    Input('year-slider', 'value'),
    Input('report-window', 'value'),
    Input('race_option', 'value'),
)
def update_(selected_year, report_window, race_option):
    temp_df = newsletter_counts_by_race_df1[(newsletter_counts_by_race_df1['Reporting Month']==selected_year) & (newsletter_counts_by_race_df1['Reporting Window']==report_window) & (newsletter_counts_by_race_df1['static_demographics.race_text'].isin(race_option))].reset_index(drop=True)

    donut_plot_d = {}
    for col in [x for x in temp_df.columns if 'Count' in x]:
        count_by_race_df = temp_df[['static_demographics.race_text',col]].copy()

        # Create color_dict and assign a color to each category in names argument
        for i, name in enumerate(count_by_race_df['static_demographics.race_text'].unique()):
            if name not in color_dict:
                color_dict[name] = color_palette[i % len(color_palette)]

        fig = px.pie(count_by_race_df, names='static_demographics.race_text', values=col, hole=0.7, color_discrete_map=color_dict)
        fig.update_layout({
            'showlegend':False,
            'plot_bgcolor': 'rgba(0,0,0,0)',
            'paper_bgcolor': 'rgba(0,0,0,0)',
            'margin_b':0,
            'margin_l':0,
            'margin_t':0,
            'margin_r':0,
            'uniformtext_minsize': 12,
            'uniformtext_mode': 'hide',
        })
        fig.update_traces(textposition='inside', hovertemplate='%{label}: %{value:.2f}')

        donut_plot_d[col] = fig
    return donut_plot_d['FTH Count'], donut_plot_d['Housed Count'], donut_plot_d['New Program Entries Count'], donut_plot_d['New Referrals Count']

@app.callback(
    Output('senior_active_race_plot', 'figure'),
    Output('veteran_active_race_plot', 'figure'),
    Output('families_active_race_plot', 'figure'),
    Output('tay_active_race_plot', 'figure'),
    Output('senior_housed_race_plot', 'figure'),
    Output('veteran_housed_race_plot', 'figure'),
    Output('tay_housed_race_plot', 'figure'),
    Output('families_housed_race_plot', 'figure'),
    Input('year-slider', 'value'),
    Input('report-window', 'value'),
    Input('race_option', 'value'),
)
def update_housed_race_plots(selected_year, report_window, race_option):

    
    temp_df = newsletter_counts_by_race_df1[(newsletter_counts_by_race_df1['Reporting Month']==selected_year) & (newsletter_counts_by_race_df1['Reporting Window']==report_window) & (newsletter_counts_by_race_df1['static_demographics.race_text'].isin(race_option))].reset_index(drop=True)
    
    bar_plot_d = {}
    for col in  [x for x in temp_df.columns if ('Housed' in x or 'Active' in x) and x!='Housed Count' and x!='Active Count']:
        count_by_race_df = temp_df[['Reporting Month', 'static_demographics.race_text', col]].copy()

        count_by_race_df = count_by_race_df.sort_values(col, ascending=True)

        # Create color_dict and assign a color to each category in names argument
        for i, name in enumerate(count_by_race_df['static_demographics.race_text'].unique()):
            if name not in color_dict:
                color_dict[name] = color_palette[i % len(color_palette)]

        fig = px.bar(count_by_race_df, x=col, y='Reporting Month', orientation='h', color='static_demographics.race_text', text_auto=True, color_discrete_map=color_dict)
        fig.update_layout({
            'plot_bgcolor': 'rgba(0,0,0,0)',
            'paper_bgcolor': 'rgba(0,0,0,0)',
            'margin_b':0,
            'margin_l':0,
            'margin_t':0,
            'margin_r':0,
            'xaxis': {
            #     'range': [0, 1],
                'showgrid': False, # thin lines in the background
                'zeroline': False, # thick line at x=0
                'visible': False,  # numbers below
            }, # the same for yaxis
            'yaxis': {
            #     'range': [0, 1],
                'showgrid': False, # thin lines in the background
                'zeroline': False, # thick line at x=0
                'visible': False,  # numbers below
            }, # the same for yaxis
            'barmode':'stack',
            # 'barnorm':'percent',
            'showlegend':False,
            'uniformtext_minsize':16, 
            "uniformtext_mode":'hide', 
            "autosize":False,
            # 'config': {'displayModeBar': False}
        })

        bar_plot_d[col] = fig
    return (
        bar_plot_d['Active Seniors Count'], 
        bar_plot_d['Active Veterans Count'], 
        bar_plot_d['Active TAY Count'], 
        bar_plot_d['Active Families Count'],
        bar_plot_d['Housed Seniors Count'], 
        bar_plot_d['Housed Veterans Count'], 
        bar_plot_d['Housed TAY Count'], 
        bar_plot_d['Housed Families Count'])

# Define callback to update options of year-slider based on report-window value
@app.callback(
    Output('year-slider', 'options'),
    Input('report-window', 'value')
)
def update_year_slider_options(report_window):
    if report_window == 'Monthly':
        option1 = ['Jan-2023', 'Dec-2022', 'Nov-2022', 'Oct-2022', 'Sep-2022']
    elif report_window == 'Quarterly':
        option1 = ['Nov 2022 - Jan 2023', 'Oct 2022 - Dec 2022', 'Sep 2022 - Nov 2022', 'Aug 2022 - Oct 2022', 'Jul 2022 - Sep 2022']
    elif report_window == '6 - Month':
        option1 = ['Aug 2022 - Jan 2023', 'Jul 2022 - Dec 2022', 'Jun 2022 - Nov 2022', 'May 2022 - Oct 2022', 'Apr 2022 - Sep 2022']
    elif report_window == 'Annual':
        option1 = ['Feb 2022 - Jan 2023', 'Jan 2022 - Dec 2022', 'Dec 2021 - Nov 2022', 'Nov 2021 - Oct 2022', 'Oct 2021 - Sep 2022']
    options = dict(zip(['Jan-2023', 'Dec-2022', 'Nov-2022', 'Oct-2022', 'Sep-2022'], option1))
    return [{'label': options[option], 'value': option} for option in options]

@app.callback(
Output(component_id='fth_likely_statement', component_property='children'),
Output(component_id='fth_compare_pop_percent', component_property='children'),
Output(component_id='active_likely_statement', component_property='children'),
Output(component_id='active_compare_pop_percent', component_property='children'),
Output(component_id='housed_likely_statement', component_property='children'),
Output(component_id='housed_compare_pop_percent', component_property='children'),
Input('racial-equity-select-year', 'value'),
Input('racial-equity-select-project-type', 'value'),
Input('racial-equity-select-race', 'value')
)
def racial_equity_data(selected_year, project_type, race_option):
    population_percent = {
        "White":.746,
        "Black, African American, or African":.056,
        'American Indian, Alaska Native, or Indigenous':.014,
        'Asian or Asian American':.129,
        'Native Hawaiian or Pacific Islander':0.006,
        'Multi-Racial':.049
    }
    #First Time Homeless
    likely_metric = binary_race_likeliness_data_df[(binary_race_likeliness_data_df['Year']==selected_year) & (binary_race_likeliness_data_df['Binary Race Variable']==race_option)][project_type].values[0]
    compare_pop_percent = binary_race_data_counts_df[(binary_race_data_counts_df['Year']==selected_year) & (binary_race_data_counts_df['Binary Race Variable']==race_option)][project_type].values[0]/(binary_race_data_counts_df[(binary_race_data_counts_df['Year']==selected_year) & (binary_race_data_counts_df['Binary Race Variable']==race_option)][project_type].values[0] + binary_race_data_counts_df[(binary_race_data_counts_df['Year']==selected_year) & (binary_race_data_counts_df['Binary Race Variable']==f"Non-{race_option}")][project_type].values[0])
    likely_metric_statement = f"{race_option} clients are {'{:.2f}'.format(likely_metric)} times more likely to be First Time Homeless in {project_type} than Non-{race_option} clients"
    compare_pop_percent_statement = f"{race_option} clients make up {'{:.0%}'.format(population_percent[race_option])} of the general population in San Diego County but make up {'{:.0%}'.format(compare_pop_percent)} in {project_type} programs in HMIS."
    
    # Active 
    active_likely_metric = active_binary_race_likeliness_data_df[(active_binary_race_likeliness_data_df['Year']==selected_year) & (active_binary_race_likeliness_data_df['Binary Race Variable']==race_option)][project_type].values[0]
    active_compare_pop_percent = active_binary_race_data_counts_df[(active_binary_race_data_counts_df['Year']==selected_year) & (active_binary_race_data_counts_df['Binary Race Variable']==race_option)][project_type].values[0]/(active_binary_race_data_counts_df[(active_binary_race_data_counts_df['Year']==selected_year) & (active_binary_race_data_counts_df['Binary Race Variable']==race_option)][project_type].values[0] + active_binary_race_data_counts_df[(active_binary_race_data_counts_df['Year']==selected_year) & (active_binary_race_data_counts_df['Binary Race Variable']==f"Non-{race_option}")][project_type].values[0])
    active_likely_metric_statement = f"{race_option} clients are {'{:.2f}'.format(active_likely_metric)} times more likely to be Active in an HMIS {project_type} program than Non-{race_option} clients"
    active_compare_pop_percent_statement = f"{race_option} clients make up {'{:.0%}'.format(population_percent[race_option])} of the general population in San Diego County but make up {'{:.0%}'.format(active_compare_pop_percent)} in {project_type} programs in HMIS."

    #Housed
    housed_likely_metric = housed_binary_race_likeliness_data_df[(housed_binary_race_likeliness_data_df['Year']==selected_year) & (housed_binary_race_likeliness_data_df['Binary Race Variable']==race_option)][project_type].values[0]
    housed_compare_pop_percent = housed_binary_race_data_counts_df[(housed_binary_race_data_counts_df['Year']==selected_year) & (housed_binary_race_data_counts_df['Binary Race Variable']==race_option)][project_type].values[0]/(housed_binary_race_data_counts_df[(housed_binary_race_data_counts_df['Year']==selected_year) & (housed_binary_race_data_counts_df['Binary Race Variable']==race_option)][project_type].values[0] + housed_binary_race_data_counts_df[(housed_binary_race_data_counts_df['Year']==selected_year) & (housed_binary_race_data_counts_df['Binary Race Variable']==f"Non-{race_option}")][project_type].values[0])
    housed_likely_metric_statement = f"{race_option} clients are {'{:.2f}'.format(housed_likely_metric)} times more likely to be Housed through a {project_type} than Non-{race_option} clients"
    housed_compare_pop_percent_statement = f"{race_option} clients make up {'{:.0%}'.format(population_percent[race_option])} of the general population in San Diego County but make up {'{:.0%}'.format(housed_compare_pop_percent)} in {project_type} programs in HMIS."

    return likely_metric_statement,compare_pop_percent_statement, active_likely_metric_statement, active_compare_pop_percent_statement, housed_likely_metric_statement, housed_compare_pop_percent_statement

@app.callback(
Output(component_id='sheltered_pit_1', component_property='children'),
Output(component_id='sheltered_pit_2', component_property='children'),
Output(component_id='unsheltered_pit_1', component_property='children'),
Output(component_id='unsheltered_pit_2', component_property='children'),
Input('racial-equity-select-year', 'value'),
Input('racial-equity-select-race', 'value')
)
def racial_equity_pit_data(selected_year, race_option):
    population_percent = {
        "White":.746,
        "Black, African American, or African":.056,
        'American Indian, Alaska Native, or Indigenous':.014,
        'Asian or Asian American':.129,
        'Native Hawaiian or Pacific Islander':0.006,
        'Multi-Racial':.049
    }
    sheltered_pit_1 = pit_data_likely_df[(pit_data_likely_df['Year']==selected_year) & (pit_data_likely_df['Race']==race_option) & (pit_data_likely_df['index']=='Sheltered')]['Likely Metric'].values[0]
    sheltered_likely_metric_statement = f"{race_option} clients are {'{:.2f}'.format(sheltered_pit_1)} times more likely to be Sheltered Homeless than Non-{race_option} clients"
    sheltered_pit_2 = pit_data_df[(pit_data_df['Year']==selected_year) & (pit_data_df['static_demographics.race_text']==race_option)]['Sheltered'].values[0]/pit_data_df[(pit_data_df['Year']==selected_year)]['Sheltered'].sum()
    sheltered_compare_pop_percent_statement = f"{race_option} clients make up {'{:.0%}'.format(population_percent[race_option])} of the general population in San Diego County but make up {'{:.0%}'.format(sheltered_pit_2)} of the Sheltered Homeless population."
    unsheltered_pit_1 = pit_data_likely_df[(pit_data_likely_df['Year']==selected_year) & (pit_data_likely_df['Race']==race_option) & (pit_data_likely_df['index']=='Unsheltered')]['Likely Metric'].values[0]
    unsheltered_likely_metric_statement = f"{race_option} clients are {'{:.2f}'.format(unsheltered_pit_1)} times more likely to be Unsheltered Homeless than Non-{race_option} clients"
    unsheltered_pit_2 = pit_data_df[(pit_data_df['Year']==selected_year) & (pit_data_df['static_demographics.race_text']==race_option)]['Unsheltered'].values[0]/pit_data_df[(pit_data_df['Year']==selected_year)]['Unsheltered'].sum()
    unsheltered_compare_pop_percent_statement = f"{race_option} clients make up {'{:.0%}'.format(population_percent[race_option])} of the general population in San Diego County but make up {'{:.0%}'.format(unsheltered_pit_2)} of the Unsheltered Homeless population."
    return sheltered_likely_metric_statement, sheltered_compare_pop_percent_statement, unsheltered_likely_metric_statement, unsheltered_compare_pop_percent_statement


if __name__ == '__main__':
    app.run_server(debug=True, port=8050)