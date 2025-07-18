import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import requests
import json
import os

# Page configuration
st.set_page_config(
    page_title="Wind Tunnel Data Explorer",
    page_icon="🌪️",
    layout="wide"
)

# App title
st.title("🌪️ Wind Tunnel Data Explorer with AI Analysis")
st.markdown("Analyze wind tunnel test data with interactive visualizations and AI insights using Gemma3 1B")

# Load CSV data
@st.cache_data
def load_data():
    """Load the wind tunnel test data from CSV file"""
    csv_path = "wind_tunnel_test_data.csv"
    if os.path.exists(csv_path):
        return pd.read_csv(csv_path)
    else:
        st.error(f"CSV file not found at {csv_path}")
        return None

# Function to call Ollama API
def query_ollama(prompt, data_summary):
    """Send query to local Ollama API with Gemma3 1B model"""
    try:
        # Prepare the full prompt with data context
        full_prompt = f"""You are analyzing wind tunnel test data. Here is the dataset summary:

{data_summary}

User question: {prompt}

Please provide a clear, technical analysis based on this aerodynamic data. Focus on relationships between angle of attack (AoA), lift, drag, and aerodynamic coefficients (Cl, Cd)."""

        # Ollama API call
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "gemma2:2b",  # Updated to use Gemma2 2B as it's more common
                "prompt": full_prompt,
                "stream": False
            },
            timeout=30
        )
        
        if response.status_code == 200:
            return response.json()["response"]
        else:
            return f"Error: API returned status code {response.status_code}"
    
    except requests.exceptions.ConnectionError:
        return "Error: Could not connect to Ollama. Make sure Ollama is running locally on port 11434."
    except requests.exceptions.Timeout:
        return "Error: Request timed out. The model might be taking too long to respond."
    except Exception as e:
        return f"Error: {str(e)}"

# Load the data
data = load_data()

if data is not None:
    # Display basic info
    st.subheader("📊 Dataset Overview")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Data Points", len(data))
    with col2:
        st.metric("AoA Range", f"{data['AoA (deg)'].min()}° to {data['AoA (deg)'].max()}°")
    with col3:
        st.metric("Max Lift Coefficient", f"{data['Cl'].max():.3f}")
    
    # Data table
    st.subheader("📋 Raw Data")
    st.dataframe(data, use_container_width=True)
    
    # Interactive visualizations
    st.subheader("📈 Interactive Visualizations")
    
    # Create tabs for different visualizations
    tab1, tab2, tab3, tab4 = st.tabs(["Lift vs AoA", "Drag vs AoA", "Lift/Drag Polar", "Coefficients"])
    
    with tab1:
        fig1 = px.scatter(data, x="AoA (deg)", y="Lift (mN)", 
                         title="Lift vs Angle of Attack",
                         hover_data=["Cl"])
        fig1.add_scatter(x=data["AoA (deg)"], y=data["Lift (mN)"], 
                        mode="lines", name="Trend Line")
        st.plotly_chart(fig1, use_container_width=True)
    
    with tab2:
        fig2 = px.scatter(data, x="AoA (deg)", y="Drag (mN)", 
                         title="Drag vs Angle of Attack",
                         hover_data=["Cd"])
        fig2.add_scatter(x=data["AoA (deg)"], y=data["Drag (mN)"], 
                        mode="lines", name="Trend Line")
        st.plotly_chart(fig2, use_container_width=True)
    
    with tab3:
        fig3 = px.scatter(data, x="Cd", y="Cl", 
                         title="Lift-Drag Polar Diagram",
                         hover_data=["AoA (deg)"])
        st.plotly_chart(fig3, use_container_width=True)
    
    with tab4:
        fig4 = make_subplots(specs=[[{"secondary_y": True}]])
        fig4.add_trace(
            go.Scatter(x=data["AoA (deg)"], y=data["Cl"], name="Lift Coefficient (Cl)"),
            secondary_y=False,
        )
        fig4.add_trace(
            go.Scatter(x=data["AoA (deg)"], y=data["Cd"], name="Drag Coefficient (Cd)"),
            secondary_y=True,
        )
        fig4.set_xaxis_title("Angle of Attack (degrees)")
        fig4.set_yaxis_title("Lift Coefficient (Cl)", secondary_y=False)
        fig4.set_yaxis_title("Drag Coefficient (Cd)", secondary_y=True)
        fig4.update_layout(title_text="Aerodynamic Coefficients vs Angle of Attack")
        st.plotly_chart(fig4, use_container_width=True)
    
    # AI Analysis Section
    st.subheader("🤖 AI Analysis with Gemma3")
    st.markdown("Ask questions about the wind tunnel data and get AI-powered insights!")
    
    # Prepare data summary for AI
    data_summary = f"""
    Wind Tunnel Test Data Summary:
    - Data Points: {len(data)}
    - Angle of Attack Range: {data['AoA (deg)'].min()}° to {data['AoA (deg)'].max()}°
    - Lift Range: {data['Lift (mN)'].min():.1f} to {data['Lift (mN)'].max():.1f} mN
    - Drag Range: {data['Drag (mN)'].min():.1f} to {data['Drag (mN)'].max():.1f} mN
    - Lift Coefficient Range: {data['Cl'].min():.3f} to {data['Cl'].max():.3f}
    - Drag Coefficient Range: {data['Cd'].min():.3f} to {data['Cd'].max():.3f}
    
    Key Data Points:
    {data.to_string(index=False)}
    """
    
    # Example questions
    st.markdown("**Example Questions:**")
    example_questions = [
        "What is the optimal angle of attack for maximum lift?",
        "At what angle does stall occur?",
        "What is the lift-to-drag ratio at different angles?",
        "Explain the aerodynamic behavior shown in this data",
        "What angle of attack gives the best efficiency?"
    ]
    
    for i, question in enumerate(example_questions):
        if st.button(f"📝 {question}", key=f"example_{i}"):
            st.session_state.user_question = question
    
    # User input
    user_question = st.text_input(
        "Enter your question about the wind tunnel data:",
        value=st.session_state.get('user_question', ''),
        placeholder="e.g., What is the relationship between angle of attack and lift coefficient?"
    )
    
    # AI Query button
    if st.button("🚀 Send test data to AI", type="primary"):
        if user_question:
            with st.spinner("🧠 AI is analyzing your data..."):
                ai_response = query_ollama(user_question, data_summary)
            
            st.subheader("🤖 AI Response")
            st.markdown(ai_response)
            
            # Add to chat history
            if "chat_history" not in st.session_state:
                st.session_state.chat_history = []
            
            st.session_state.chat_history.append({
                "question": user_question,
                "response": ai_response
            })
        else:
            st.warning("Please enter a question first!")
    
    # Chat History
    if "chat_history" in st.session_state and st.session_state.chat_history:
        st.subheader("📜 Chat History")
        for i, chat in enumerate(reversed(st.session_state.chat_history)):
            with st.expander(f"Q: {chat['question'][:50]}..."):
                st.markdown(f"**Question:** {chat['question']}")
                st.markdown(f"**Response:** {chat['response']}")
    
    # Technical Details
    with st.expander("ℹ️ Technical Information"):
        st.markdown("""
        **Data Structure:**
        - AoA (deg): Angle of Attack in degrees
        - Lift (mN): Lift force in millinewtons
        - Cl: Lift coefficient (dimensionless)
        - Drag (mN): Drag force in millinewtons
        - Cd: Drag coefficient (dimensionless)
        
        **AI Model:** Gemma3 1B running locally via Ollama
        **Visualization:** Interactive Plotly charts
        **Framework:** Streamlit
        """)

else:
    st.error("Unable to load wind tunnel data. Please check that the CSV file exists.")

# Footer
st.markdown("---")
st.markdown("*Wind Tunnel Data Explorer - Powered by Streamlit and Gemma3 1B*")
