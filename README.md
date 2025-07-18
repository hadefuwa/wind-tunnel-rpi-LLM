# Wind Tunnel Data Explorer with AI Analysis

A web application for analyzing wind tunnel test data with AI-powered insights using Gemma3 1B model via Ollama. Available in both Streamlit and Flask versions for maximum compatibility.

## Features

- 📊 Interactive data visualizations with Plotly
- 🤖 AI analysis using Gemma3 1B model
- 📈 Multiple chart types (lift/drag curves, polar diagrams, coefficients)
- 💬 Chat interface for data exploration
- � Responsive web interface
- 🎯 Flask version optimized for Raspberry Pi compatibility

## Requirements

- Python 3.8+
- Ollama with Gemma3 1B model installed
- Internet connection for initial setup

## Setup Instructions

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Install and Setup Ollama

#### On Raspberry Pi:
```bash
curl -fsSL https://ollama.ai/install.sh | sh
ollama pull gemma3:1b
```

#### On Windows/Mac/Linux:
1. Download Ollama from https://ollama.ai
2. Install and run: `ollama pull gemma3:1b`

### 3. Run the Application

#### Option A: Streamlit Version (Windows/Mac/Linux)
```bash
streamlit run app.py
```

#### Option B: Flask Version (All platforms, especially Raspberry Pi)
```bash
python flask_app.py
```

Both apps will be available at: http://localhost:8501

## Usage

1. **Data Visualization**: Explore interactive charts showing aerodynamic relationships
2. **AI Analysis**: Use the AI chat section to ask questions about the data
3. **Sample Questions**:
   - "What is the optimal angle of attack for maximum lift?"
   - "At what angle does stall occur?"
   - "What is the lift-to-drag ratio at different angles?"
   - "Explain the aerodynamic behavior shown in this data"

## Data Format

The CSV file should contain columns:
- `AoA (deg)`: Angle of Attack in degrees
- `Lift (mN)`: Lift force in millinewtons
- `Cl`: Lift coefficient
- `Drag (mN)`: Drag force in millinewtons  
- `Cd`: Drag coefficient

## Raspberry Pi Deployment

### SSH Setup
```bash
# Copy files to Pi
scp -r . pi@your-pi-ip:/home/pi/wind-tunnel-app/

# SSH into Pi
ssh pi@your-pi-ip

# Navigate and setup
cd /home/pi/wind-tunnel-app/
python3 -m venv venv
source venv/bin/activate
pip install flask pandas requests

# Run Flask app (recommended for Pi)
python3 flask_app.py
```

## Troubleshooting

- **Streamlit "Illegal instruction" on Pi**: Use Flask version instead
- Ensure Ollama is running: `ollama list`
- Check model availability: `ollama list | grep gemma3`
- Verify port 11434 is not blocked

## Technical Stack

- **Frontend**: Streamlit or Flask + HTML/CSS/JavaScript
- **Charts**: Plotly (Streamlit) or Plotly.js (Flask)
- **AI Model**: Gemma3 1B (via Ollama)
- **Data Processing**: Pandas

## App Versions

- **app.py**: Full-featured Streamlit version with advanced UI components
- **flask_app.py**: Lightweight Flask version optimized for Raspberry Pi compatibility

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
