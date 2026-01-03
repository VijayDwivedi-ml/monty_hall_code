import streamlit as st
import random
import plotly.graph_objects as go

# -----------------------------
# Simulation Logic
# -----------------------------

def play_game_host_knows():
    doors = ["goat", "goat", "car"]
    random.shuffle(doors)

    player_choice = random.randint(0, 2)

    possible_doors = [
        i for i in range(3)
        if i != player_choice and doors[i] == "goat"
    ]
    host_opens = random.choice(possible_doors)

    final_choice = [
        i for i in range(3)
        if i not in (player_choice, host_opens)
    ][0]

    return 1 if doors[final_choice] == "car" else 0


def play_game_host_does_not_know():
    doors = ["goat", "goat", "car"]
    random.shuffle(doors)

    player_choice = random.randint(0, 2)
    remaining_doors = [i for i in range(3) if i != player_choice]
    host_opens = random.choice(remaining_doors)

    if doors[host_opens] == "car":
        return 0, False

    final_choice = [
        i for i in range(3)
        if i not in (player_choice, host_opens)
    ][0]

    return (1 if doors[final_choice] == "car" else 0), True


def run_simulation(n_simulations, host_knows):
    wins = 0
    valid_trials = 0

    iterations = []
    probabilities = []

    while valid_trials < n_simulations:
        if host_knows:
            win = play_game_host_knows()
            valid_trials += 1
        else:
            win, valid = play_game_host_does_not_know()
            if not valid:
                continue
            valid_trials += 1

        wins += win
        iterations.append(valid_trials)
        probabilities.append(wins / valid_trials)

    return iterations, probabilities


# -----------------------------
# Streamlit UI
# -----------------------------

st.set_page_config(page_title="Monty Hall Experiment", layout="centered")

st.title("🎲 The Monty Hall Experiment")
st.subheader("When assumptions change, outcomes change")

st.write(
    """
    This experiment uses **simulation** to show how changing just one assumption
    can completely alter outcomes.
    
    Instead of trusting intuition, we let **data converge**.
    """
)

# -----------------------------
# Controls (Minimal)
# -----------------------------

st.markdown("### 🔍 Experiment Setup")

host_knowledge = st.radio(
    "What does the host know?",
    [
        "Host knows what's behind the doors",
        "Host does NOT know what's behind the doors"
    ]
)

n_simulations = st.slider(
    "Number of simulations",
    min_value=500,
    max_value=10000,
    step=500,
    value=5000
)

host_knows = host_knowledge == "Host knows what's behind the doors"

# -----------------------------
# Contextual Explanation
# -----------------------------

st.markdown("### 🧠 Key Assumption")

if host_knows:
    st.info(
        "The host **knows** where the prize is and deliberately avoids revealing it.\n\n"
        "This creates **conditional probability**."
    )
    true_probability = 2 / 3
else:
    st.warning(
        "The host **does not know** where the prize is and opens a door at random.\n\n"
        "Only trials where the prize is not revealed are observed."
    )
    true_probability = 0.5

# -----------------------------
# Run Simulation
# -----------------------------

iterations, probabilities = run_simulation(
    n_simulations=n_simulations,
    host_knows=host_knows
)

final_empirical = probabilities[-1]

# -----------------------------
# Metrics
# -----------------------------

st.markdown("### 📊 Empirical Outcome")

st.metric(
    label="Winning Probability (Always Switch)",
    value=f"{final_empirical:.4f}"
)

st.caption(
    f"True theoretical probability: {true_probability:.3f}"
)

# -----------------------------
# Interactive Convergence Chart
# -----------------------------

st.markdown("### 📈 Convergence of Winning Probability")

fig = go.Figure()

# Empirical line
fig.add_trace(
    go.Scatter(
        x=iterations,
        y=probabilities,
        mode="lines",
        name="Empirical Probability (Simulation)",
        hovertemplate="Iteration: %{x}<br>Probability: %{y:.4f}<extra></extra>"
    )
)

# True probability reference line
fig.add_trace(
    go.Scatter(
        x=[iterations[0], iterations[-1]],
        y=[true_probability, true_probability],
        mode="lines",
        name="True Theoretical Probability",
        line=dict(dash="dash"),
        hoverinfo="skip"
    )
)

fig.update_layout(
    xaxis_title="Number of Valid Simulations",
    yaxis_title="Winning Probability (Always Switch)",
    yaxis=dict(range=[0, 1]),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    margin=dict(l=40, r=40, t=40, b=40)
)

st.plotly_chart(fig, use_container_width=True)

st.caption(
    "As simulations increase, randomness fades and the probability stabilizes. "
    "The dashed line represents the true value derived from conditional probability."
)

# -----------------------------
# Reflection Prompts
# -----------------------------

st.markdown("### 💡 Pause & Reflect")

st.write(
    """
    - What changed here — the data or the assumption?
    - Would a small sample size have misled you?
    - Can outcomes be trusted without understanding the process?
    """
)

# -----------------------------
# Cross-Domain Insight
# -----------------------------

st.markdown("### 🌍 Why this matters")

st.write(
    """
    **🎓 Students**  
    Simulation reveals why intuition often fails in probability.
    
    **👩‍🏫 Educators**  
    A live demonstration of convergence and conditional probability.
    
    **💼 Business & Management**  
    Data without process knowledge can converge to the wrong conclusion.
    """
)

# -----------------------------
# Disclaimer
# -----------------------------

st.markdown("---")
st.caption(
    "📌 **Disclaimer**: This application is built purely for educational purposes. "
    "The simulation logic and methodology will be made openly available. "
    "Feedback, questions, and discussions are welcome."
)
