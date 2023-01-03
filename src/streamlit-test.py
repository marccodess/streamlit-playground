import streamlit as st
import plotly.express as px

# Load the gapminder dataset from the Plotly library
df = px.data.gapminder()

# Create a title for the app
st.title("Gapminder Data Exploration")

# Create a sidebar with various filters
year_min = st.sidebar.slider("Year Min", 1952, 2007, 1952)
year_max = st.sidebar.slider("Year Max", 1952, 2007, 2007)
continent = st.sidebar.multiselect("Continent", df["continent"].unique())
log_y = st.sidebar.radio("Y-axis Scale", ["Linear", "Log"])

# Display the selected options
st.write("Continent(s) selected:", continent)

# Filter the dataset based on the selected values
filtered_df = df[
    (df["year"] >= year_min)
    & (df["year"] <= year_max)
    & df["continent"].isin(continent)
]

# Create a scatter plot of GDP per capita vs life expectancy
fig1 = px.scatter(
    filtered_df,
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    title="Life Expectancy vs GDP",
)

# Set the y-axis scale to log if selected
if log_y == "Log":
    fig1.update_layout(yaxis_type="log")

# Display the plot
st.plotly_chart(fig1)

# Display some text explaining the chart
st.markdown(
    "This chart shows the relationship between GDP per capita and life expectancy for different countries and continents. You can use the filters in the sidebar to adjust the year range and continent, and to change the y-axis scale."
)


# Create a bar chart of GDP per capita by continent
fig2 = px.bar(
    filtered_df, x="continent", y="gdpPercap", title="GDP per Capita by Continent"
)

# Display the plot
st.plotly_chart(fig2)

# Display some text explaining the chart
st.markdown(
    "This chart shows the GDP per capita for different continents. You can use the filters in the sidebar to adjust the year range and continent."
)

# Create a line chart of population by year
fig3 = px.line(
    filtered_df, x="year", y="pop", color="continent", title="Population by Year"
)

# Display the plot
st.plotly_chart(fig3)

# Display some text explaining the chart
st.markdown(
    "This chart shows the population for different continents over time. You can use the filters in the sidebar to adjust the year range and continent."
)

# Create a bar chart of the countries
fig = px.bar(df, x="country", y="gdpPercap", title="GDP per Capita by Country")

# Display the plot
st.plotly_chart(fig)
