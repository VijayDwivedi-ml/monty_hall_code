# 🎲 Monty Hall Probability Simulator

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://monty-hall-simulator.streamlit.app/)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An interactive educational simulator that demonstrates the famous Monty Hall probability paradox through real-time visualization and experimentation.

## 📖 What is the Monty Hall Problem?

The Monty Hall problem is a famous probability puzzle based on the American game show "Let's Make a Deal." The paradox demonstrates how our intuition about probability can often be wrong, and how conditional probability works in practice.

**The Setup:**
- 3 doors: 1 car (prize) and 2 goats
- You pick a door
- Host opens a different door revealing a goat
- You're offered the chance to switch doors

**The Paradox:** Switching doors gives you a **2/3 chance** of winning, while staying gives only **1/3** — contrary to the common intuition that it should be 50/50.

## 🚀 Live Demo

Try the interactive simulator: **[Launch App](https://monty-hall-simulator.streamlit.app/)**

## ✨ Features

- **Interactive Simulation**: Run thousands of Monty Hall trials in seconds
- **Host Knowledge Toggle**: Compare scenarios where the host knows vs. doesn't know what's behind the doors
- **Real-time Visualization**: Watch probabilities converge to their theoretical values
- **Educational Design**: Clear explanations, reflection prompts, and real-world applications
- **Cross-domain Insights**: Applications for data science, business, and education

## 🧮 Key Concepts Demonstrated

1. **Conditional Probability**: How new information changes probabilities
2. **Law of Large Numbers**: Probabilities stabilize with more trials
3. **Assumption Impact**: How hidden assumptions affect conclusions
4. **Data Convergence**: Empirical vs. theoretical probability

## 📊 What You'll Discover

### When Host KNOWS the Prize Location:
- **Stay strategy**: Wins ≈ 33.3% of the time
- **Switch strategy**: Wins ≈ 66.7% of the time

### When Host DOESN'T Know the Prize Location:
- **Both strategies**: Win ≈ 50% of the time (when prize isn't accidentally revealed)

## 🛠️ Installation & Local Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/monty-hall-simulator.git
cd monty-hall-simulator
```

2. **Create virtual environment (recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
streamlit run app.py
```

5. **Open your browser** and go to `http://localhost:8501`

## 📁 Project Structure

```
monty-hall-simulator/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md           # This file
├── .gitignore          # Git ignore file
└── assets/             # Optional: Images and resources
    └── screenshot.png
```

## 🧪 How It Works

### Simulation Logic
- **Scenario 1 (Host Knows)**: Host always reveals a goat, never the car
- **Scenario 2 (Host Doesn't Know)**: Host randomly opens any remaining door
- **Data Collection**: Tracks win rates for switching strategy
- **Convergence Tracking**: Records probability after every trial

### User Interface
1. **Experiment Setup**: Choose host knowledge and simulation count
2. **Live Results**: See empirical probability vs. theoretical expectation
3. **Interactive Chart**: Watch convergence in real-time
4. **Educational Content**: Reflection prompts and applications

## 📈 For Educators

This simulator is perfect for teaching:
- **Probability theory** in high school/college
- **Data science concepts** like empirical convergence
- **Critical thinking** about assumptions
- **Statistical intuition** development

### Classroom Activities
1. **Prediction Exercise**: Have students predict outcomes before running simulations
2. **Assumption Analysis**: Discuss how host knowledge changes the game
3. **Real-world Applications**: Connect to A/B testing, medical trials, etc.
4. **Extension Projects**: Modify the code to explore variations

## 🏢 For Business & Data Science

The Monty Hall problem illustrates critical concepts for professionals:

- **Hidden assumptions** in data analysis
- **Conditional probability** in decision-making
- **Importance of process knowledge** in interpreting results
- **Distinction between correlation and causation**

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Report bugs** or suggest features via Issues
2. **Submit pull requests** with improvements
3. **Share educational use cases** or classroom experiences
4. **Improve documentation** or translations

### Development Setup
```bash
# Install development dependencies
pip install -r requirements.txt

# Run tests (if available)
pytest

# Format code
black app.py
```

## 📚 Learn More

### Further Reading
- [Monty Hall Problem - Wikipedia](https://en.wikipedia.org/wiki/Monty_Hall_problem)
- [The Monty Hall Problem - Numberphile](https://www.youtube.com/watch?v=4Lb-6rxZxx0)
- [Conditional Probability - Khan Academy](https://www.khanacademy.org/math/ap-statistics/probability-ap/stats-conditional-probability)

### Related Concepts
- Bayesian inference
- Conditional probability
- Game theory
- Behavioral economics

## 🎯 Learning Objectives

After using this simulator, you should be able to:

1. Explain why switching doors gives better odds when the host knows
2. Describe how assumptions change probability calculations
3. Recognize similar "hidden information" scenarios in real life
4. Understand the difference between empirical and theoretical probability
5. Apply conditional probability thinking to data analysis

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by the original Monty Hall problem and its many explainers
- Built with [Streamlit](https://streamlit.io/) for interactive visualization
- Uses [Plotly](https://plotly.com/) for dynamic charts
- Thanks to all the educators who use probability puzzles to teach critical thinking

## 📬 Contact & Support

- **Issues**: [GitHub Issues](https://github.com/vijaydwivedi-ml/monty-hall-simulator/issues)
- **Educational inquiries**: For classroom use or curriculum integration
- **Feedback**: Suggestions for improving the educational value

---

<div align="center">
  
**⭐ If you find this project useful, please star it on GitHub!**

*"Probability is not just about numbers—it's about understanding the game being played."*

</div>

---

**Happy Learning!** Explore, experiment, and embrace the power of probability! 🎲✨
