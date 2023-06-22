from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc

block3 = html.Div(
            className="block-3",
            children=[
                dbc.Card(
                    style={'background-color': '#3C7681', 'border': 'solid 1px white', 'color':'white'},
                    children=[
                        dbc.CardHeader(html.H2(children="Who found housing?", className='display-4')),
                        dbc.CardBody(
                            children=[
                                dbc.Row(
                                    children=[
                                        dbc.Col(
                                            width={"xl": 4, "md": 6, "sm": 12},
                                            children=[
                                                html.Div(
                                                    # className="card",
                                                    children=[
                                                        html.H3(
                                                            id="housed_count_1",
                                                            className="metric display-4",
                                                        ),
                                                        html.H3(children="Persons Housed", className='display-4'),
                                                    ],
                                                )
                                            ],
                                        ),
                                        dbc.Col(
                                            width={"xl": 4, "md": 6, "sm": 12},
                                            children=[
                                                html.Div(
                                                    className="section-3-subsection-2-top",
                                                    children=[
                                                        html.Div(
                                                            className="house-card",
                                                            children=[
                                                                html.Div(
                                                                    className="arrow-up",
                                                                    children=""
                                                                ),
                                                                html.Div(
                                                                    className="housed-metrics",
                                                                    children=[
                                                                        html.H4(
                                                                            className='display-5',
                                                                            id="senior_housed_count"
                                                                        ),
                                                                        html.H4(
                                                                            className="bar display-5",
                                                                            children="|",
                                                                        ),
                                                                        html.H4(
                                                                            className='display-5',
                                                                            children="Seniors"
                                                                            ),
                                                                    ],
                                                                ),
                                                                html.Div(
                                                                    className="housed_plots",
                                                                    children=dcc.Graph(
                                                                        id="senior_housed_race_plot"
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                        html.Div(
                                                            className="house-card",
                                                            children=[
                                                                html.Div(
                                                                    className="arrow-up",
                                                                    children=""
                                                                ),
                                                                html.Div(
                                                                    className="housed-metrics",
                                                                    children=[
                                                                        html.H4(
                                                                            id="tay_housed_count",
                                                                            className="display-5"
                                                                        ),
                                                                        html.H4(
                                                                            className="bar display-5",
                                                                            children="|",
                                                                        ),
                                                                        html.H4(
                                                                            children="Families",
                                                                            className="display-5"
                                                                        ),
                                                                    ],
                                                                ),
                                                                html.Div(
                                                                    className="housed_plots display-4",
                                                                    children=dcc.Graph(
                                                                        id="families_housed_race_plot"
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                )
                                            ],
                                        ),
                                        dbc.Col(
                                            width={"xl": 4, "md": 12, "sm": 12},
                                            children=[
                                                html.Div(
                                                    className="section-3-subsection-2-bottom",
                                                    children=[
                                                        html.Div(
                                                            className="house-card",
                                                            children=[
                                                                html.Div(
                                                                    className="arrow-up",
                                                                    children=""
                                                                ),
                                                                html.Div(
                                                                    className="housed-metrics",
                                                                    children=[
                                                                        html.H4(
                                                                            className='display-5',
                                                                            id="families_housed_count"
                                                                        ),
                                                                        html.H4(
                                                                            className="bar display-5",
                                                                            children="|",
                                                                        ),
                                                                        html.H4(
                                                                            className='display-5',
                                                                            children="TAY 18-24"
                                                                        ),
                                                                    ],
                                                                ),
                                                                html.Div(
                                                                    className="housed_plots",
                                                                    children=dcc.Graph(
                                                                        id="tay_housed_race_plot",
                                                                        style={
                                                                            "width": "auto",
                                                                            "height": "10vh",
                                                                        },
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                        html.Div(
                                                            className="house-card",
                                                            children=[
                                                                html.Div(
                                                                    className="arrow-up",
                                                                    children=""
                                                                ),
                                                                html.Div(
                                                                    className="housed-metrics",
                                                                    children=[
                                                                        html.H4(
                                                                            className='display-5',
                                                                            id="veterans_housed_count"
                                                                        ),
                                                                        html.H4(
                                                                            className="bar display-5",
                                                                            children="|",
                                                                        ),
                                                                html.H4(className='display-5', children="Veterans"),
                                                            ],
                                                        ),
                                                        html.Div(
                                                            className="housed_plots",
                                                            children=dcc.Graph(
                                                                id="veteran_housed_race_plot"
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                dbc.Row(
                                    children=[
                                        dbc.Col(
                                            width={"xl": 12, "md": 12, "sm": 12},
                                            children=[
                                                html.Div(
                                                    className="body-section-3-subsection-3",
                                                    children=[dcc.Graph(id="graph-with-slider")],
                                                )
                                            ],
                                        )
                                    ],
                                    className="mt-3",
                                ),
                            ]
                        ),
                    ],
                    className="w-100",
                )
            ]   
        )
    ]
)


# from dash import Dash, html, dcc, Input, Output
# import dash_bootstrap_components as dbc

# block3 = html.Div(
#     className="block-3",
#     children=[
#         html.Div(
#             className="title-section-3",
#             children=[html.H2(children="Who found housing?")]
#         ),
#         html.Div(
#             className="body-section-3",
#             children=[
#                 html.Div(
#                     className="body-section-3-subsection-1",
#                     children=[
#                         html.Div(
#                             className="card",
#                             children=[
#                                 html.H3(id='housed_count_1',className="metric"),
#                                 html.H3(children="Persons Housed"),
#                             ]
#                         )
#                     ]
#                 ),
#                 html.Div(
#                     className="body-section-3-subsection-2",
#                     children=[
#                         html.Div(
#                             className='section-3-subsection-2-top',
#                             children=[
#                                 html.Div(
#                                     className="house-card",
#                                     children=[
#                                         html.Div(
#                                             className="arrow-up",
#                                             children=""
#                                         ),
#                                         html.Div(
#                                             className="housed-metrics",
#                                             children=[
#                                                 html.H4(id="senior_housed_count"),
#                                                 html.H4(className="bar",children="|"),
#                                                 html.H4(children="Seniors"),   
#                                             ]
#                                         ),
#                                         html.Div(
#                                             className='housed_plots',
#                                             children=dcc.Graph(id='senior_housed_race_plot'),
#                                         ),
#                                     ]
#                                 ),
#                                 html.Div(
#                                     className="house-card",
#                                     children=[
#                                         html.Div(
#                                             className="arrow-up",
#                                             children=""
#                                         ),
#                                         html.Div(
#                                             className="housed-metrics",
#                                             children=[
#                                                 html.H4(id="tay_housed_count"),
#                                                 html.H4(className="bar",children="|"),
#                                                 html.H4(children="Families"),
#                                             ]
#                                         ),
#                                         html.Div(
#                                             className='housed_plots',
#                                             children=dcc.Graph(id='families_housed_race_plot'),
#                                             ),
#                                     ]
#                                 ),
#                             ]
#                         ),
#                         html.Div(
#                             className='section-3-subsection-2-bottom',
#                             children=[
#                                 html.Div(
#                                     className="house-card",
#                                     children=[
#                                         html.Div(
#                                             className="arrow-up",
#                                             children=""
#                                         ),
#                                         html.Div(
#                                             className="housed-metrics",
#                                             children=[
#                                                 html.H4(id="families_housed_count"),
#                                                 html.H4(className="bar",children="|"),
#                                                 html.H4(children="TAY 18-24"),
#                                             ]
#                                         ),
#                                         html.Div(
#                                             className='housed_plots',
#                                             children=dcc.Graph(id='tay_housed_race_plot', style={'width': 'auto', 'height': '10vh'}),
#                                         ),
#                                     ]
#                                 ),
#                                 html.Div(
#                                     className="house-card",
#                                     children=[
#                                         html.Div(
#                                             className="arrow-up",
#                                             children=""
#                                         ),
#                                         html.Div(
#                                             className="housed-metrics",
#                                             children=[
#                                                 html.H4(id="veterans_housed_count"),
#                                                 html.H4(className="bar",children="|"),
#                                                 html.H4(children="Veterans"),
#                                             ]
#                                         ),
#                                         html.Div(
#                                             className='housed_plots',
#                                             children=dcc.Graph(id='veteran_housed_race_plot'),
#                                         ),
#                                     ]
#                                 ),
#                             ]
#                         )                                                                                                                        
#                     ]
#                 ),
#                 html.Div(
#                     className="body-section-3-subsection-3",
#                     children=[
#                         dcc.Graph(id='graph-with-slider'),
#                     ]
#                 ),
#             ]
#         )
#     ]
# )