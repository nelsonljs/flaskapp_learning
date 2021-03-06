import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go

app_site = '/'
gapingvoid_img = app_site + 'assets/gapingvoid.jpg'
#######
## Sidebars

search_bar = dbc.Row(
    [
        dbc.Col(dbc.Input(type="search", placeholder="Search")),
        dbc.Col(
            dbc.Button("Search", color="primary", className="ml-2"),
            width="100%",
        ),
    ],
    no_gutters=True,
    className="ml-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)

nav_item = dbc.NavItem(dbc.NavLink("Home", href="/", external_link=True))
nav_item1 = dbc.NavItem(dbc.NavLink("Ticker Info", href="/dashboard1", external_link=True))
nav_item2 = dbc.NavItem(dbc.NavLink("Ticker Trends", href="/dashboard2", external_link=True, disabled = True))
nav_item3 = dbc.NavItem(dbc.NavLink("My Blog", href="https://nelsonljs.github.io/myblog/"),
                        style = {"background-color": "#fffbe0"})
# dropdown = dbc.DropdownMenu(
#     children=[
#         dbc.DropdownMenuItem("Ticker Info", href = "/dashboard1", external_link=True),
#         dbc.DropdownMenuItem("Ticker Trends", href = "https://github.com"),
#         dbc.DropdownMenuItem(divider=True),
#         dbc.DropdownMenuItem("Home", href = "/", external_link=True),
#     ],
#     nav=True,
#     in_navbar=True,
#     label="Menu",
# )

text_input = html.Div(
    [
        dbc.FormGroup(
            [
                dbc.Label("Input Ticker"),
                dbc.Input(id="ticker_input", value="AAPL"),
                dbc.FormText("Please enter a ticker like MSFT or AAPL."),
                html.P(id = "ticker_output"),
                dbc.Button("Get Stock Info", id = "get_info", color="primary", className="mr-1"),
                dbc.FormFeedback(
                    "That ticker is valid!", valid=True
                ),
                dbc.FormFeedback(
                    "That ticker is invalid!",
                    valid=False,
                ),
            ]
        )
    ]
)

sidebar_header = dbc.Row(
    [
        dbc.Col(html.H4("Ticker Info", className="display-4")),
        dbc.Col(
            html.Button(
                # use the Bootstrap navbar-toggler classes to style the toggle
                html.Span(className="navbar-toggler-icon"),
                className="navbar-toggler",
                # the navbar-toggler classes don't set color, so we do it here
                style={
                    "color": "rgba(0,0,0,.5)",
                    "border-color": "rgba(0,0,0,.1)",
                },
                id="toggle",
            ),
            # the column containing the toggle will be only as wide as the
            # toggle, resulting in the toggle being right aligned
            width="auto",
            # vertically align the toggle in the center
            align="center",
        ),
    ]
)

sidebar = html.Div(
    [
        sidebar_header,
        # we wrap the horizontal rule and short blurb in a div that can be
        # hidden on a small screen
        html.Div(
            [
                html.Hr(),
                html.P(
                    "This is my Navigation Bar",
                    className="lead",
                ),
            ],
            id="blurb",
        ),
        # use the Collapse component to animate hiding / revealing links
        dbc.Collapse(
            dbc.Nav(
                [nav_item,nav_item1,nav_item2,nav_item3],
                vertical=True,
                pills=True,
            ),
            id="collapse",
        ),
    ],
    id="sidebar",
)

content = html.Div([
        dbc.Row([
            dbc.Col([
                    html.Img(src=gapingvoid_img, height = "600px")
                    ], width = 4)
            ]
        ),
        html.Div(id='intermediate-value', style={'display': 'none'})

        ],id="page-content")

homelayout = html.Div([
        sidebar,
        content
    ]
)
