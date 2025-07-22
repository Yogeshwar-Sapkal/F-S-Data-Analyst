import streamlit as st
from utils import load_excel_data
from plots import generate_population_distribution , generate_age_wise_distribution
from insights import generate_llm_insight, gender_insight , age_wise_insight

st.title("🏗️ Highest & Best Use Analyzer")

uploaded_file = st.file_uploader("📤 Upload Census/NAICS Excel", type="xlsx")
if uploaded_file:
    year, city, df = load_excel_data(uploaded_file)
    st.subheader(f"**Data Year:** {year}")
    st.subheader(f"**City:** {city}")
    # st.dataframe(df)

    st.header("📊 Demographic Analysis")
    fig , totalPopulation = generate_population_distribution(df,city,year)
    st.dataframe(totalPopulation)
    st.pyplot(fig, use_container_width=True)
    insight = gender_insight(totalPopulation, city, year)
    st.markdown(f"**Insight:** {insight}")
    # st.pyplot(generate_age_wise_distribution(df,city,year),use_container_width=True)
    fig1, fig2, age = generate_age_wise_distribution(df, city, year)
    st.pyplot(fig1, use_container_width=True)
    st.pyplot(fig2, use_container_width=True)
    insight = age_wise_insight(age, city, year)
    st.markdown(f"**Insight:** {insight}")

    