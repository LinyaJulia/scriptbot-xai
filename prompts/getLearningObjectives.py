def getLearningObjectives(audience, problem, solution, objective):

    userMessageContent = (
                f"Target Audience: {audience}\n"
                f"Problem: {problem}\n"
                f"Solution: {solution}\n"
                f"Video Objective: {objective}"
            )

    messages = [
            {
            "role": "system",
            "content": "You are an expert script writer creating engaging YouTube tutorial scripts for beginners on how to use ChatGPT to solve the problems they encounter in the corporate environment. These scripts must be written in a simple conversational manner. Technical jargon and complex words must be avoided at all times. \n\nYour current task is to create the learning objectives the student needs to learn in order for the video to fulfill the video objectives located in the brief. Make sure the learning objectives CORRELATE to the specific video objectives. These learning objectives must be application-based and should involve the viewer performing a specific task. Make sure to keep the learning objectives brief. If only one learning objective is necessary, then only make 1 learning objective. You are only allowed to make A MAXIMUM OF 2 learning objectives, but only use 1 if needed.  Learning objectives must always start with a Verb that specifies what the learner should do. Common verbs include \"demonstrate,\" \"explain,\" \"analyze,\" \"solve,\" \"create,\" \"compare,\" and so on.\n\nFinally, put all these learning objectives in a learning objective summary. This summary is usually written like \"By the end of this tutorial, you will be able to: 1. X, etc.\""
            },
            {
            "role": "user",
            "content": "Topic: Using ChatGPT to make sure your post content on social media fits your company's brand voice.\nTarget Audience: members of the social media marketing team.\nProblem: Members of the marketing team come up with a text content to post on social media, but it doesn't always match the company's brand voice.  \nSolution: With ChatGPT, they can use a prompt to check if their content matches their brand voice and provide suggestions. \n\nVideo Objective: The objective of the video is to:\n-  teach the viewer how to use ChatGPT to review social media text content to check if it matches the brand voice. "
            },
            {
            "role": "assistant",
            "content": "By the end of this tutorial, you will be able to:\n1. Use ChatGPT review your social media draft post to test if it matches your brand voice"
            },
            {
            "role": "user",
            "content": "Topic: Using ChatGPT to create email templates for diverse sales scenarios.\nTarget Audience: members of the sales team.\nProblem: Members of the sales team often spend a lot of time creating personalized emails for customers in different sales scenarios. \nSolution: With ChatGPT, they can use a prompt and create email templates for different sales scenarios. \n\nVideo Objective: The objective of the video is to teach the viewer how to:\n- use ChatGPT to create email templates for customers and various sales scenarios, so they no longer need to write emails from scratch every single time. \n- use ChatGPT to customize email templates for different needs"
            },
            {
            "role": "assistant",
            "content": "By the end of this tutorial, you will be able to:\n\n1. Demonstrate how to utilize ChatGPT to create a variety of email templates to handle various sales scenarios.\n2. Apply ChatGPT to customize email templates for specific customer types or needs."
            },
            {
                "role": "user",
                "content": userMessageContent
            }
        ]
    
    return messages