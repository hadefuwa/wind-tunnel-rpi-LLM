# Wind Tunnel Data Explorer with AI Analysis

A Streamlit application for analyzing wind tunnel test data with interactive visualizations and AI-powered insights using Gemma3 1B via Ollama.

## Features

- 📊 **Interactive Data Visualization**: Multiple chart types using Plotly
- 🤖 **AI Analysis**: Query your data using natural language with Gemma3 1B
- 📈 **Aerodynamic Analysis**: Specialized visualizations for lift, drag, and coefficients
- 💬 **Chat Interface**: Ask questions and get technical insights about your data
- 🚀 **Real-time Processing**: Fast analysis powered by local AI model

## Installation

### Prerequisites

1. **Python 3.8+**
2. **Ollama** installed and running locally
3. **Gemma3 1B model** pulled in Ollama

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/hadefuwa/wind-tunnel-rpi-LLM.git
   cd wind-tunnel-rpi-LLM
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install and setup Ollama:**
   ```bash
   # Install Ollama (Linux/macOS)
   curl -fsSL https://ollama.ai/install.sh | sh
   
   # For Windows, download from https://ollama.ai/download
   ```

4. **Pull the Gemma3 model:**
   ```bash
   ollama pull gemma2:2b
   ```

5. **Start Ollama service:**
   ```bash
   ollama serve
   ```

## Usage

1. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser** to `http://localhost:8501`

3. **Explore the data:**
   - View raw data in the table
   - Interact with the visualizations
   - Ask questions in the AI chat interface

## Data Structure

The application expects a CSV file named `wind_tunnel_test_data.csv` with the following columns:

- `AoA (deg)`: Angle of Attack in degrees
- `Lift (mN)`: Lift force in millinewtons
- `Cl`: Lift coefficient (dimensionless)
- `Drag (mN)`: Drag force in millinewtons
- `Cd`: Drag coefficient (dimensionless)

## Example Questions for AI Analysis

- "What is the optimal angle of attack for maximum lift?"
- "At what angle does stall occur?"
- "What is the lift-to-drag ratio at different angles?"
- "Explain the aerodynamic behavior shown in this data"
- "What angle of attack gives the best efficiency?"

## Visualization Features

### 1. Lift vs Angle of Attack
Interactive scatter plot showing lift force relationship with AoA.

### 2. Drag vs Angle of Attack
Drag force analysis across different angles.

### 3. Lift-Drag Polar Diagram
Classical aerodynamic polar plot for performance analysis.

### 4. Aerodynamic Coefficients
Dual-axis plot showing both Cl and Cd variations.

## Technical Architecture

- **Frontend**: Streamlit for web interface
- **Visualization**: Plotly for interactive charts
- **Data Processing**: Pandas for data manipulation
- **AI Backend**: Ollama with Gemma3 1B model
- **API**: REST calls to local Ollama instance

## Configuration

### Ollama Settings
The app connects to Ollama at `http://localhost:11434` by default. Modify the `query_ollama()` function in `app.py` to change the endpoint or model.

### Model Configuration
Currently configured for `gemma2:2b`. To use a different model, update the model name in the API call:

```python
"model": "your-model-name"
```

## Raspberry Pi Deployment

This application is optimized for Raspberry Pi deployment:

1. **Install dependencies** as above
2. **Use lightweight model** (Gemma3 1B is ideal for Pi 4 with 8GB RAM)
3. **Consider resource limits** when running both Streamlit and Ollama

### Performance Tips for Raspberry Pi

- Close unnecessary applications
- Use a fast SD card (Class 10 or better)
- Ensure adequate cooling
- Monitor memory usage with `htop`

## Troubleshooting

### Common Issues

1. **"Could not connect to Ollama"**
   - Ensure Ollama is running: `ollama serve`
   - Check if the service is accessible: `curl http://localhost:11434`

2. **"CSV file not found"**
   - Ensure `wind_tunnel_test_data.csv` is in the same directory as `app.py`

3. **Slow AI responses**
   - Normal for Raspberry Pi - Gemma3 1B takes 10-30 seconds per query
   - Consider using a smaller model for faster responses

4. **Memory issues on Raspberry Pi**
   - Close other applications
   - Restart Ollama service
   - Use swap memory if needed

## Development

### Adding New Visualizations

Add new tabs in the visualization section:

```python
with tab_new:
    fig_new = px.scatter(data, x="column1", y="column2")
    st.plotly_chart(fig_new, use_container_width=True)
```

### Customizing AI Prompts

Modify the `query_ollama()` function to adjust how data is presented to the AI model.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

For issues and questions:
- Open an issue on GitHub
- Check the troubleshooting section above
- Ensure all dependencies are properly installed

---

*Built with ❤️ for aerodynamic analysis and AI exploration*
