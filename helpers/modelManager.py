import streamlit as st
from helpers import chatGptClient
from prompts import getHookPrompt, getTitleAndIntroPrompt, getLearningObjectives, getPrompts, getTutorialSectionPrompt

class ModelManager():

    st.session_state.audience = ""
    st.session_state.problem = ""
    st.session_state.solution = ""
    st.session_state.objective = ""
    st.session_state.review = ""
    st.session_state.reviewText = ""
    st.session_state.hook = ""
    st.session_state.titleAndIntroduction = ""
    st.session_state.learningObjectives = ""
    st.session_state.prompts = ""
    st.session_state.tutorialSection = ""
    st.session_state.chatGptClient = ""

    def __init__(self):
        st.session_state.chatGptClient = chatGptClient.ChatGPTClient()

    def setInputs(self, audience, problem, solution, objective):
        st.session_state.audience = audience
        st.session_state.problem = problem
        st.session_state.solution = solution
        st.session_state.objective = objective

    def setReview(self):
        st.session_state.review = "Pass"
        st.session_state.reviewText = "Review text"
    
    def getReview(self):
        return st.session_state.review, st.session_state.reviewText

    def setHook(self):
        message = getHookPrompt.getHookPrompt(
            st.session_state.audience,
            st.session_state.problem,
            st.session_state.solution,
            st.session_state.objective
        )
        st.session_state.hook = st.session_state.chatGptClient.chat(message)

    def getHook(self):
        return st.session_state.hook
    
    def setTitleAndIntroduction(self):
        message = getTitleAndIntroPrompt.getTitleAndIntroPrompt(
            st.session_state.audience,
            st.session_state.problem,
            st.session_state.solution,
            st.session_state.objective
        )
        st.session_state.titleAndIntroduction = st.session_state.chatGptClient.chat(message)

    def getTitleAndIntroduction(self):
        return st.session_state.titleAndIntroduction
    
    def setLearningObjectives(self):
        message = getLearningObjectives.getLearningObjectives(
            st.session_state.audience,
            st.session_state.problem,
            st.session_state.solution,
            st.session_state.objective
        )
        st.session_state.learningObjectives = st.session_state.chatGptClient.chat(message)

    def getLearningObjectives(self):
        return st.session_state.learningObjectives
    
    def setPrompts(self):
        message = getPrompts.getPrompts(
            st.session_state.audience,
            st.session_state.problem,
            st.session_state.solution,
            st.session_state.objective,
            st.session_state.learningObjectives
        )
        st.session_state.prompts = st.session_state.chatGptClient.chat(message)

    def getPrompts(self):
        return st.session_state.prompts
    
    def setTutorialSection(self):
        message = getTutorialSectionPrompt.getTutorialSectionPrompt(
            st.session_state.objective,
            st.session_state.learningObjectives,
            st.session_state.prompts
        )
        st.session_state.tutorialSection = st.session_state.chatGptClient.chat(message)

    def getTutorialSection(self):
        return st.session_state.tutorialSection
    
    def getFinalScript(self):
        finalScript = st.session_state.hook + st.session_state.titleAndIntroduction + st.session_state.learningObjectives + st.session_state.tutorialSection
        return finalScript