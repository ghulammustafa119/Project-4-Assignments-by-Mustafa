import streamlit as st
import random

NUM_ROUNDS = 5

# Initialize session state on first load
if "score" not in st.session_state:
    st.session_state.score = 0
if "round" not in st.session_state:
    st.session_state.round = 1
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "user_number" not in st.session_state:
    st.session_state.user_number = random.randint(1, 100)
if "computer_number" not in st.session_state:
    st.session_state.computer_number = random.randint(1, 100)

st.title("🎯 High-Low Game")
st.markdown("Welcome to the High-Low Game!")
st.markdown("---")

# Show current round
if not st.session_state.game_over:
    st.subheader(f"Round {st.session_state.round} of {NUM_ROUNDS}")
    st.write(f"Your number is: **{st.session_state.user_number}**")

    # Buttons for "Higher" and "Lower"
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔼 Higher"):
            guess = "higher"
            correct = st.session_state.user_number > st.session_state.computer_number
        else:
            guess = None
    with col2:
        if st.button("🔽 Lower"):
            guess = "lower"
            correct = st.session_state.user_number < st.session_state.computer_number
        else:
            guess = None

    # Game logic
    if guess:
        if (guess == "higher" and correct) or (guess == "lower" and correct):
            st.success(f"✅ You were right! The computer's number was {st.session_state.computer_number}")
            st.session_state.score += 1
        else:
            st.error(f"❌ That's incorrect. The computer's number was {st.session_state.computer_number}")

        st.session_state.round += 1

        if st.session_state.round > NUM_ROUNDS:
            st.session_state.game_over = True
        else:
            # Prepare next round
            st.session_state.user_number = random.randint(1, 100)
            st.session_state.computer_number = random.randint(1, 100)

    st.info(f"**Your score:** {st.session_state.score}")

else:
    # Game Over Section
    st.subheader("🎉 Game Over!")
    st.write(f"Your final score is: **{st.session_state.score} / {NUM_ROUNDS}**")

    if st.session_state.score == NUM_ROUNDS:
        st.success("🌟 Wow! You played perfectly!")
    elif st.session_state.score >= NUM_ROUNDS // 2:
        st.info("👍 Good job, you played really well!")
    else:
        st.warning("😅 Better luck next time!")

    # Play Again or Exit
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔁 Play Again"):
            for key in st.session_state.keys():
                del st.session_state[key]
            st.rerun()
    with col2:
        if st.button("❌ Exit Game"):
            st.write("Thanks for playing! 👋")
