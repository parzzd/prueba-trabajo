from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')


# Obtener lista de países únicos
countries = df["country"].unique()

app = Dash(__name__)

app.layout = html.Div([
    html.H2("Selecciona el país"),
    dcc.Dropdown(
        id="country-dropdown",
        options=[{"label": country, "value": country} for country in countries],
        multi=True,
        placeholder="Elige un país"
    ),
    dcc.Graph(id="country-graph")
])

@app.callback(
    Output("country-graph", "figure"),
    [Input("country-dropdown", "value")]
)
def update_graph(selected_countries):
    if not selected_countries:
        filtered_df = df
    else:
        filtered_df = df[df["country"].isin(selected_countries)]
    
    fig = px.line(filtered_df, x="year", y="lifeExp", color="country", markers=True,
                  title="Esperanza de Vida a lo Largo del Tiempo")
    

    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
