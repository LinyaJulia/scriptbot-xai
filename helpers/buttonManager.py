import streamlit as st

class ButtonManager(): 
    
    st.session_state.buttonStates = {
        "hook" : False,
        "titleAndIntroduction" : False,
        "learningObjectives" : False,
        "prompts" : False, 
        "tutorialSection" : False,
        "generateScript" : False
    }

    def __init__(self):
        if "buttonStates" not in st.session_state:
            st.session_state.buttonStates = {
                "hook" : False,
                "titleAndIntroduction" : False,
                "learningObjectives" : False,
                "prompts" : False, 
                "tutorialSection" : False,
                "generateScript" : False
            }

    def getButtonDisabledState(self, buttonName):
        return not st.session_state.buttonStates[buttonName]
    
    def setButtonState(self, buttonName, state):
        st.session_state.buttonStates[buttonName] = state

    def reviewButtonStates(self):
        if st.session_state.review == "Pass":
            self.setButtonState("hook", True)

        if st.session_state.hook:
            self.setButtonState("titleAndIntroduction", True)

        if st.session_state.titleAndIntroduction:
            self.setButtonState("learningObjectives", True)

        if st.session_state.learningObjectives:
            self.setButtonState("prompts", True)

        if st.session_state.prompts:
            self.setButtonState("tutorialSection", True)

        if st.session_state.tutorialSection:
            self.setButtonState("generateScript", True)
