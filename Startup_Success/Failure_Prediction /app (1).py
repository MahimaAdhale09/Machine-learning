import pandas as pd
import pickle
import streamlit as st

st.set_page_config(page_title="Startup Success Predictor", page_icon="🚀", layout="centered")
model = pickle.load(open("model.pkl", "rb"))

st.image("banner.png", width=700)
st.caption("Fill in your startup's details to get an AI-powered success prediction")

sector = st.selectbox("Sector", ["AI/ML", "AgriTech", "CleanTech", "Cybersecurity", "E-commerce",
                                  "EdTech", "FinTech", "FoodTech", "Gaming", "HealthTech", "Logistics", "SaaS"])
country = st.selectbox("Country", ["Canada", "Germany", "India", "Israel", "Singapore", "UAE", "UK", "USA"])
city_tier = st.selectbox("City Type", ["Remote/Distributed", "Tier-1 Hub", "Tier-2 City"])
funding_stage = st.selectbox("Funding Stage", ["Pre-Seed", "Seed", "Series A", "Series B", "Series C+"])
founder_avg_experience_years = st.slider("Avg Founder Experience (years)", 0.0, 30.0, 5.0)
has_prior_startup_experience = st.checkbox("Founder has prior startup experience")
has_technical_cofounder = st.checkbox("Has technical co-founder", value=True)
team_size = st.slider("Team Size", 2, 300, 15)
total_funding_usd_million = st.number_input("Total Funding (USD million)", 0.0, 500.0, 1.5)
num_funding_rounds = st.slider("Number of Funding Rounds", 1, 8, 1)
monthly_burn_rate_usd_k = st.number_input("Monthly Burn Rate (USD thousand)", 1.0, 2000.0, 100.0)
num_active_competitors = st.slider("Active Competitors", 0, 30, 6)
mom_revenue_growth_pct = st.number_input("MoM Revenue Growth (%)", -50.0, 200.0, 8.0)
customer_retention_rate_pct = st.slider("Customer Retention Rate (%)", 0.0, 100.0, 70.0)
nps_score = st.slider("NPS Score", -100, 100, 30)
num_patents_filed = st.slider("Patents Filed", 0, 10, 0)

st.divider()

if st.button("🔮 Predict", type="primary", use_container_width=True):
    input_df = pd.DataFrame([{
        "sector": sector, "country": country, "city_tier": city_tier, "funding_stage": funding_stage,
        "founder_avg_experience_years": founder_avg_experience_years,
        "has_prior_startup_experience": int(has_prior_startup_experience),
        "has_technical_cofounder": int(has_technical_cofounder), "team_size": team_size,
        "total_funding_usd_million": total_funding_usd_million, "num_funding_rounds": num_funding_rounds,
        "monthly_burn_rate_usd_k": monthly_burn_rate_usd_k, "num_active_competitors": num_active_competitors,
        "num_patents_filed": num_patents_filed, "mom_revenue_growth_pct": mom_revenue_growth_pct,
        "customer_retention_rate_pct": customer_retention_rate_pct, "nps_score": nps_score,
    }])

    prediction = model.predict(input_df)
    if prediction == 1:
        st.success("Your startup will be successful! 🎉")
        st.balloons()
        
    else:
        st.error("Your startup is likely to fail")
