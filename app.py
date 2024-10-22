import streamlit as st
import random

# IPA Data from your original dictionary
ipa_data = {
    'p': {'Voicing': 'voiceless', 'Place': 'bilabial', 'Manner': 'stop','Oro-nasal': '(oral)','Centrality':'(central)'},
    'b': {'Voicing': 'voiced', 'Place': 'bilabial', 'Manner': 'stop','Oro-nasal': '(oral)','Centrality':'(central)'},
    't': {'Voicing': 'voiceless', 'Place': 'alveolar', 'Manner': 'stop','Oro-nasal': '(oral)','Centrality':'(central)'},
    'd': {'Voicing': 'voiced', 'Place': 'alveolar', 'Manner': 'stop','Oro-nasal': '(oral)','Centrality':'(central)'},
    'k': {'Voicing': 'voiceless', 'Place': 'velar', 'Manner': 'stop','Oro-nasal': '(oral)','Centrality':'(central)'},
    'g': {'Voicing': 'voiced', 'Place': 'velar', 'Manner': 'stop','Oro-nasal': '(oral)','Centrality':'(central)'},
    'f': {'Voicing': 'voiceless', 'Place': 'labio-dental', 'Manner': 'fricative','Oro-nasal': '(oral)','Centrality':'(central)'},
    'v': {'Voicing': 'voiced', 'Place': 'labio-dental', 'Manner': 'fricative','Oro-nasal': '(oral)','Centrality':'(central)'},
    'θ': {'Voicing': 'voiceless', 'Place': 'dental', 'Manner': 'fricative','Oro-nasal': '(oral)','Centrality':'(central)'},
    'ð': {'Voicing': 'voiced', 'Place': 'dental', 'Manner': 'fricative','Oro-nasal': '(oral)','Centrality':'(central)'},
    's': {'Voicing': 'voiceless', 'Place': 'alveolar', 'Manner': 'fricative','Oro-nasal': '(oral)','Centrality':'(central)'},
    'z': {'Voicing': 'voiced', 'Place': 'alveolar', 'Manner': 'fricative','Oro-nasal': '(oral)','Centrality':'(central)'},
    'ʃ': {'Voicing': 'voiceless', 'Place': 'palato-alveolar', 'Manner': 'fricative','Oro-nasal': '(oral)','Centrality':'(central)'},
    'ʒ': {'Voicing': 'voiced', 'Place': 'palato-alveolar', 'Manner': 'fricative','Oro-nasal': '(oral)','Centrality':'(central)'},
    'tʃ': {'Voicing': 'voiceless', 'Place': 'palato-alveolar', 'Manner': 'affricate','Oro-nasal': '(oral)','Centrality':'(central)'},
    'dʒ': {'Voicing': 'voiced', 'Place': 'palato-alveolar', 'Manner': 'affricate','Oro-nasal': '(oral)','Centrality':'(central)'},
    'h': {'Voicing': 'voiceless', 'Place': 'glottal', 'Manner': 'fricative','Oro-nasal': '(oral)','Centrality':'(central)'},
    'm': {'Voicing': 'voiced', 'Place': 'bilabial', 'Manner': 'stop','Oro-nasal': 'nasal','Centrality':'(not applicable)'},
    'n': {'Voicing': 'voiced', 'Place': 'alveolar', 'Manner': 'stop','Oro-nasal': 'nasal','Centrality':'(not applicable)'},
    'ŋ': {'Voicing': 'voiced', 'Place': 'velar', 'Manner': 'stop','Oro-nasal': 'nasal','Centrality':'(not applicable)'},
    'ɹ': {'Voicing': 'voiced', 'Place': 'alveolar', 'Manner': 'approximant','Oro-nasal': '(oral)','Centrality':'(central)'},
    'l': {'Voicing': 'voiced', 'Place': 'alveolar', 'Manner': 'approximant','Oro-nasal': '(oral)','Centrality':'lateral'},
    'j': {'Voicing': 'voiced', 'Place': 'palatal', 'Manner': 'approximant','Oro-nasal': '(oral)','Centrality':'(central)'},
    'w': {'Voicing': 'voiced', 'Place': 'labio-velar', 'Manner': 'approximant','Oro-nasal': '(oral)','Centrality':'(central)'}
}


# Initialize session state for keeping track of correct answers and attempts
if "correct_count" not in st.session_state:
    st.session_state.correct_count = 0
if "attempts" not in st.session_state:
    st.session_state.attempts = 0

def select_random_symbol():
    """ Select a random IPA symbol """
    symbol = random.choice(list(ipa_data.keys()))
    return symbol, ipa_data[symbol]

def validate_selections(ipa_symbol, user_voicing, user_place, user_manner, user_oronasal, user_centrality):
    """ Check user's selections against the actual IPA symbol properties """
    correct_data = ipa_data[ipa_symbol]
    correct = (correct_data['Voicing'] == user_voicing and
               correct_data['Place'] == user_place and
               correct_data['Manner'] == user_manner and
               correct_data['Oro-nasal'] == user_oronasal and
               correct_data['Centrality'] == user_centrality)
    
    st.session_state.attempts += 1
    if correct:
        st.session_state.correct_count += 1
        return "Correct!"
    else:
        return f"Incorrect! Correct values are: Voicing: {correct_data['Voicing']}, Place: {correct_data['Place']}, Manner: {correct_data['Manner']}, Oro-nasal: {correct_data['Oro-nasal']}, Centrality: {correct_data['Centrality']}"

# Main interface with Streamlit
st.title("🐇 IPA Practice App")

# Start quiz or display new symbol
if 'current_symbol' not in st.session_state or st.button("Start Quiz"):
    symbol, _ = select_random_symbol()
    st.session_state.current_symbol = symbol

st.text(f"IPA Symbol: {st.session_state.current_symbol}")

# User interaction for symbol characteristics using columns
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    voicing = st.radio("Voicing", ['voiceless', 'voiced'], key="voicing")
with col2:
    place = st.radio("Place", ['bilabial', 'labio-dental', 'labio-velar', 'dental', 'alveolar', 'palato-alveolar', 'palatal', 'velar', 'glottal'], key="place")
with col3:
    manner = st.radio("Manner", ['stop', 'fricative', 'affricate', 'approximant'], key="manner")
with col4:
    oronasal = st.radio("Oro-nasal", ['(oral)', 'nasal'], key="oronasal")
with col5:
    centrality = st.radio("Centrality", ['(central)', 'lateral', '(not applicable)'], key="centrality")

# Submit button
if st.button("Submit"):
    result = validate_selections(st.session_state.current_symbol, voicing, place, manner, oronasal, centrality)
    st.write(result)
    # Refresh the symbol immediately after submission
    new_symbol, _ = select_random_symbol()
    st.session_state.current_symbol = new_symbol

# Show the total score
if st.button("See the total score"):
    st.write(f"Final Score: {st.session_state.correct_count}/{st.session_state.attempts}")
