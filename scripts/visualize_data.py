import pandas as pd
import plotly.express as px

def visualize_data():
    df = pd.read_csv("../data/dataset_clean.csv", index_col=0, parse_dates=True)

    fig = px.line(df, x=df.index, y=["New Cases", "Deaths"],
                  labels={"value": "Count", "variable": "Category"},
                  title="Évolution des cas et décès du COVID-19")

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Count",
        legend_title="Category",
        template="plotly_dark"
    )

    fig.write_html("../reports/covid_trend.html")
    print("✅ Visualisation enregistrée en HTML.")

if __name__ == "__main__":
    visualize_data()
