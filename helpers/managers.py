import streamlit as st

class ModelManager():

    st.session_state.audience = ""
    st.session_state.problem = ""
    st.session_state.solution = ""
    st.session_state.review = ""
    st.session_state.reviewText = ""
    st.session_state.hook = ""
    st.session_state.titleAndIntroduction = ""
    st.session_state.learningObjectives = ""
    st.session_state.prompts = ""
    st.session_state.tutorialSection = ""

    def setInputs(self, audience, problem, solution):
        st.session_state.audience = audience
        st.session_state.problem = problem
        st.session_state.solution = solution

    def setReview(self):
        st.session_state.review = "Pass"
        st.session_state.reviewText = "Review text"
    
    def getReview(self):
        return st.session_state.review, st.session_state.reviewText

    def setHook(self):
        st.session_state.hook = "Hook is set"

    def getHook(self):
        return st.session_state.hook
    
    def setTitleAndIntroduction(self):
        st.session_state.titleAndIntroduction = "Title and Introduction is set"

    def getTitleAndIntroduction(self):
        return st.session_state.titleAndIntroduction
    
    def setLearningObjectives(self):
        st.session_state.learningObjectives = "Learning Objectives is set"

    def getLearningObjectives(self):
        return st.session_state.learningObjectives
    
    def setPrompts(self):
        st.session_state.prompts = "Prompts is set"

    def getPrompts(self):
        return st.session_state.prompts
    
    def setTutorialSection(self):
        st.session_state.tutorialSection = "Tutorial Section is set"

    def getTutorialSection(self):
        return st.session_state.tutorialSection
            


class ButtonManager(): 

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
