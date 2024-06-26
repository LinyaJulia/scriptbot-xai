import streamlit as st
from helpers import chatGptClient
from prompts import getHookPrompt, getTitleAndIntroPrompt, getLearningObjectives, getPrompts, getTutorialSectionPrompt, getCourseDescription

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
    st.session_state.courseDescription = ""

    def __init__(self):
        st.session_state.chatGptClient = chatGptClient.ChatGPTClient()
        if 'audience' not in st.session_state:
            st.session_state.audience = ""
        if 'problem' not in st.session_state:
            st.session_state.problem = ""
        if 'solution' not in st.session_state:
            st.session_state.solution = ""
        if 'objective' not in st.session_state:
            st.session_state.objective = ""
        if 'review' not in st.session_state:
            st.session_state.review = ""
        if 'reviewText' not in st.session_state:
            st.session_state.reviewText = ""
        if 'hook' not in st.session_state:
            st.session_state.hook = ""
        if 'titleAndIntroduction' not in st.session_state:
            st.session_state.titleAndIntroduction = ""
        if 'learningObjectives' not in st.session_state:
            st.session_state.learningObjectives = ""
        if 'prompts' not in st.session_state:
            st.session_state.prompts = ""
        if 'tutorialSection' not in st.session_state:
            st.session_state.tutorialSection = ""
        if 'tutorialSection' not in st.session_state:
            st.session_state.courseDescription = ""

    def setInputs(self, audience, problem, solution, objective):
        st.session_state.audience = audience
        st.session_state.problem = problem
        st.session_state.solution = solution
        st.session_state.objective = objective

    def setReview(self):
        if(st.session_state.audience and st.session_state.problem and st.session_state.solution and st.session_state.objective):
            st.session_state.review = "Pass"
            st.session_state.reviewText = "You may now proceed to the next step."
        else: 
            st.session_state.review = "Fail"
            st.session_state.reviewText = "_Please make sure to fill in all missing fields._"
    
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
            st.session_state.learning_objectives_text_area
        )
        st.session_state.prompts = st.session_state.chatGptClient.chat(message)

    def getPrompts(self):
        return st.session_state.prompts
    
    def setTutorialSection(self):
        message = getTutorialSectionPrompt.getTutorialSectionPrompt(
            st.session_state.objective,
            st.session_state.learning_objectives_text_area,
            st.session_state.prompts_text_area
        )
        st.session_state.tutorialSection = st.session_state.chatGptClient.chat(message)

    def getTutorialSection(self):
        return st.session_state.tutorialSection
    
    def getFinalScript(self):
        finalScript = st.session_state.hook_text_area + st.session_state.title_and_intro_text_area + st.session_state.learning_objectives_text_area + st.session_state.tutorial_section_text_area
        return finalScript
    
    def setCourseDescription(self):
        courseDescription = getCourseDescription.getCourseDescription(
            st.session_state.hook_text_area,
            st.session_state.title_and_intro_text_area
        )
        st.session_state.courseDescription = st.session_state.chatGptClient.chat(courseDescription)
    
    def getCourseDescription(self):
        return st.session_state.courseDescription