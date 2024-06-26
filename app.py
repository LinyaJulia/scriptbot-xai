import streamlit as st
from helpers import modelManager, buttonManager, texts, style

def main():

    style.local_css("helpers/style.css")

    if 'modelManager' not in st.session_state:
        st.session_state.modelManager = None
    if 'buttonManager' not in st.session_state:
        st.session_state.buttonManager = None

    st.session_state.modelManager = modelManager.ModelManager()
    st.session_state.buttonManager = buttonManager.ButtonManager()

    text = texts.MainPageText()
    st.markdown(text.title)

    with st.expander(text.stepOneTitle):
        st.markdown(text.stepOneText)
        stepOneDropdown = st.popover(text.stepOneSampleText)
        with (stepOneDropdown): 
            st.markdown(text.stepOneSampleTable)

        st.divider()
        audienceInput = st.text_input(text.audienceInputText)
        problemInput = st.text_input(text.problemStatementText)
        solutionInput = st.text_area(text.solutionText)
        objectiveInput = st.text_area(text.videoObjectiveText)

        reviewAnswerButton = st.button(text.reviewButtonText)
        if(reviewAnswerButton):
            st.session_state.modelManager.setInputs(audienceInput, problemInput, solutionInput, objectiveInput)
            st.session_state.modelManager.setReview()
            st.session_state.buttonManager.reviewButtonStates()
        review, reviewText = st.session_state.modelManager.getReview()                      
        st.markdown(review)
        st.markdown(reviewText)

    with st.expander(text.stepTwoTitle):
        st.markdown(text.stepTwoText)


        # Hook
        with st.container(height=150):
            hookCol1, hookCol2 = st.columns([2, 1])
            with hookCol1:
                st.markdown("""**Hook**""")
            with hookCol2:
                regenerateButtonHook = st.button(
                    "Generate/Regenerate", 
                    use_container_width=True, 
                    key="reg1", 
                    disabled=st.session_state.buttonManager.getButtonDisabledState("hook")
                    )
            with st.spinner(text.loadingText):
                if (regenerateButtonHook):
                    st.session_state.modelManager.setHook()
                    st.session_state.buttonManager.reviewButtonStates() 
            
            st.text_area(
                label="Hook", 
                key='hook_text_area', 
                value=st.session_state.modelManager.getHook()
                )
            


        # Title and Introduction 
        with st.container(height=150):
            titleCol1, titleCol2 = st.columns([2, 1])
            with titleCol1:
                st.markdown("""**Title And Introduction**""")
            with titleCol2:
                regenerateButtonTitle = st.button(
                    "Generate/Regenerate", 
                    use_container_width=True, 
                    key="reg2", 
                    disabled=st.session_state.buttonManager.getButtonDisabledState("titleAndIntroduction")
                    )
                
            with st.spinner(text.loadingText):
                if (regenerateButtonTitle):
                    st.session_state.modelManager.setTitleAndIntroduction()
                    st.session_state.buttonManager.reviewButtonStates()
            st.text_area(
                label="Title and Introduction", 
                key="title_and_intro_text_area",
                value=st.session_state.modelManager.getTitleAndIntroduction())


        # Learning Objectives
        with st.container(height=150):
            learningObjectivesCol1, learningObjectivesCol2 = st.columns([2, 1])
            with learningObjectivesCol1:
                st.markdown("""**Learning Objectives**""")
            with learningObjectivesCol2:
                regenerateButtonlearningObjectives = st.button(
                    "Generate/Regenerate", 
                    use_container_width=True, 
                    key="reg3",
                    disabled=st.session_state.buttonManager.getButtonDisabledState("learningObjectives")
                    )
            with st.spinner(text.loadingText):
                if (regenerateButtonlearningObjectives):
                    st.session_state.modelManager.setLearningObjectives()
                    st.session_state.buttonManager.reviewButtonStates()
            st.text_area(
                label="Learning Objectives",
                key="learning_objectives_text_area",
                value=st.session_state.modelManager.getLearningObjectives()
                )


        # Prompts
        with st.container(height=150):
            promptsCol1, promptsCol2 = st.columns([2, 1])
            with promptsCol1:
                st.markdown("""**Prompts**""")
            with promptsCol2:
                regenerateButtonPrompts = st.button(
                    "Generate/Regenerate", 
                    use_container_width=True, 
                    key="reg4",
                    disabled=st.session_state.buttonManager.getButtonDisabledState("prompts")
                    )
            with st.spinner(text.loadingText):
                if (regenerateButtonPrompts):
                    st.session_state.modelManager.setPrompts()
                    st.session_state.buttonManager.reviewButtonStates()
            st.text_area(
                label="Prompts", 
                key="prompts_text_area",
                value=st.session_state.modelManager.getPrompts())


        # Tutorial Section and Conclusion
        with st.container(height=150):
            tutorialSectionCol1, tutorialSectionCol2 = st.columns([2, 1])
            with tutorialSectionCol1:
                st.markdown("""**Tutorial Section and Conclusion**""")
            with tutorialSectionCol2:
                regenerateButtonTutorialSection = st.button(
                    "Generate/Regenerate", 
                    use_container_width=True, 
                    key="reg5",
                    disabled=st.session_state.buttonManager.getButtonDisabledState("tutorialSection")
                    )
            with st.spinner(text.loadingText):
                if (regenerateButtonTutorialSection):
                    st.session_state.modelManager.setTutorialSection()
                    st.session_state.buttonManager.reviewButtonStates()
            st.text_area(
                label="Tutorial Section",
                key="tutorial_section_text_area", 
                value=st.session_state.modelManager.getTutorialSection()
                )
    
    with st.expander(text.stepThreeTitle):
        st.markdown(text.stepThreeText)
        generateScript = st.button("Generate Final Script")
        if(generateScript):
            finalScript = st.session_state.modelManager.getFinalScript()
            st.text_area("Final Script", value=finalScript)
            st.download_button("Export", data=finalScript)


    # Test for Course Description Creator
    with st.expander("Step 4. Create a Course Description (testing)"):
        st.markdown("Create a Course Descirption")
        generateCourseDescription = st.button("Generate Course Description")
        if(generateCourseDescription):
            st.session_state.modelManager.setCourseDescription()
            st.text_area("Course Description", value=st.session_state.modelManager.getCourseDescription())


if __name__ == '__main__':
    main()