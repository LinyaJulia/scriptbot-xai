def getPrompts(audience, problem, solution, objective, learningObjectives):

    userMessageContent = (
            f"Target Audience: {audience}\n"
            f"Problem: {problem}\n"
            f"Solution: {solution}\n"
            f"Video Objective: {objective}\n"
            f"{learningObjectives}\n"
        )
    
    messages = [
            {
            "role": "system",
            "content": "You are an expert prompt engineer creating prompts for ChatGPT. These prompts follow the best practices for prompt engineering. These best practices include be specific and clear, provide context, define a role (expert marketer, master HR recruiter), specify a desired format, be concise, and use automatic prompts that end with \"Ask me as many questions as you need until you have enough information to provide me with the desired output.\"\n\nYour current task is to create the best prompts for each learning objective found in the learning objective summary provided. For more context, you can review the video objective found in the brief. "
            },
            {
            "role": "user",
            "content": "Topic: Using ChatGPT to create email templates for diverse sales scenarios.\nTarget Audience: members of the sales team.\nProblem: Members of the sales team often spend a lot of time creating personalized emails for customers in different sales scenarios. \nSolution: With ChatGPT, they can use a prompt and create email templates for different sales scenarios. \nVideo Objective: The objective of the video is to teach the viewer how to use ChatGPT to create email templates for customers and various sales scenarios, so they no longer need to write emails from scratch every single time.\n\nBy the end of this tutorial, you will be able to:\n1. Use ChatGPT to identify different sales scenarios;\n2. Generate personalized email templates for these scenarios using ChatGPT. "
            },
            {
            "role": "assistant",
            "content": "Prompt for Learning Objective 1: Identifying Different Sales Scenarios with ChatGPT\n\nYou are a sales expert advisor. Consider the [Your Company]'s popular product/service range. Based on the buyer persona [provide some characteristics of your typical customer], could you suggest some different sales scenarios that our sales team should be prepared for? Ask me as many questions as you need until you have enough information to provide me with the desired output.\n\nPrompt for Learning Objective 2: Generating Personalized Email Templates for Different Sales Scenarios Using ChatGPT\n\nGiven the sales scenario of [provide a specific sales scenario - e.g., following up with a prospect after a meeting, answering a query, etc.], could you help me create a personalized email template to address this? Remember, our brand voice is [describe brand voice - e.g., professional, friendly, informative, casual, etc.]. Ask me as many questions as you need until you have enough information to provide me with the desired output."
            },
            {
                "role": "user",
                "content": userMessageContent
            }
        ]
    
    return messages