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


def select_random_symbol():
    """Select a random IPA symbol"""
    symbol = random.choice(list(ipa_data.keys()))
    return symbol, ipa_data[symbol]

def validate_selections(ipa_symbol, user_voicing, user_place, user_manner, user_oronasal, user_centrality):
    """Check user's selections against the actual IPA symbol properties"""
    correct_data = ipa_data[ipa_symbol]
    correct = (correct_data['Voicing'] == user_voicing and
               correct_data['Place'] == user_place and
               correct_data['Manner'] == user_manner and
               correct_data['Oro-nasal'] == user_oronasal and
               correct_data['Centrality'] == user_centrality)
    
    return correct, correct_data

# Main interface with Streamlit
st.title("🐇 IPA Practice App")

if 'new_symbol' not in st.session_state:
    st.session_state.new_symbol = True

if st.button("Start Quiz") or st.session_state.new_symbol:
    st.session_state.correct_count = 0
    st.session_state.attempts = 0
    st.session_state.new_symbol = False
    symbol, symbol_data = select_random_symbol()
    st.session_state.current_symbol = symbol
    st.session_state.current_symbol_data = symbol_data

if "current_symbol" in st.session_state:
    st.write(f"IPA Symbol: {st.session_state.current_symbol}")
    
    # Using columns to organize the options
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

    if st.button("Submit"):
        correct, correct_data = validate_selections(st.session_state.current_symbol, voicing, place, manner, oronasal, centrality)
        st.session_state.attempts += 1
        if correct:
            st.session_state.correct_count += 1
            result_text = "Correct!"
        else:
            result_text = f"Incorrect! Correct values are: Voicing: {correct_data['Voicing']}, Place: {correct_data['Place']}, Manner: {correct_data['Manner']}, Oro-nasal: {correct_data['Oro-nasal']}, Centrality: {correct_data['Centrality']}"
        st.write(result_text)
        st.session_state.new_symbol = True  # Trigger a new symbol on the next cycle
        # Update to new symbol immediately for continuous quiz experience
        new_symbol, new_symbol_data = select_random_symbol()
        st.session_state.current_symbol = new_symbol
        st.session_state.current_symbol_data = new_symbol_data

if st.button("Show Score"):
    if "attempts" in st.session_state:
        st.write(f"Final Score: {st.session_state.correct_count} out of {st.session_state.attempts}")
        st.session_state.new_symbol = True  # Allow restarting the quiz
