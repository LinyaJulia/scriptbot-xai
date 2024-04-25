def getTitleAndIntroPrompt(audience, problem, solution, objective):

    userMessageContent = (
            f"Target Audience: {audience}\n"
            f"Problem: {problem}\n"
            f"Solution: {solution}\n"
            f"Video Objective: {objective}"
        )

    messages = [
            {
            "role": "system",
            "content": "You are an expert script writer creating engaging YouTube tutorial scripts for beginners on how to use ChatGPT to solve the problems they encounter in the corporate environment. These scripts must be written in a simple conversational manner. Technical jargon and complex words must be avoided at all times. Do not use words like \"intricacy,\" \"robust,\" \"daunting,\" \"crucial,\" or \"compelling\" and other similar words. \n\nYour current task is to create a title and introduction based on the script brief that consist of a target audience, problem, solution, and video objective. \n\nThe title should be visualizing in an engaging way the video's objective. The title must be straight to the point, consist of a maximum of two phrases. It must not use abstract phrasing. \n\nThe intro should start by describing and explaining the key topic of the tutorial. For example, if the tutorial is about Brand Voice on social media, then it must start by explaining what brand voice is and why it's important. Make sure not to greet the specific target audience as this has already been done in a previous section. Technical jargon and complex words must be avoided at all times. Do not use words like \"intricacy,\" \"robust,\" \"daunting,\" \"crucial,\" or \"compelling\" and other similar words. \n\nAfter this description, it then must proceed with explaining what task is to be performed related to the key topic and why it's important to perform that task in a certain way. \n\nAnd finally, the intro wraps up with how the task can be performed with the help of ChatGPT. However, make sure not to say anything like \"In this tutorial, you will learn how to...\" because this is going to be covered in the next section. "
            },
            {
            "role": "user",
            "content": "Target Audience: members of the social media marketing team.\nProblem: Members of the marketing team come up with a text content to post on social media, but it doesn't always match the company's brand voice.  \nSolution: With ChatGPT, they can use a prompt to check if their content matches their brand voice and provide suggestions. \nVideo Objective: The objective of the video is to teach the viewer how to use ChatGPT to review social media text content to check if it matches the brand voice. "
            },
            {
            "role": "assistant",
            "content": "Title: Ensuring Consistent Brand Voice on Social Media with ChatGPT\n\nWelcome to our guide on keeping your brand's voice consistent across social media, with a little help from ChatGPT.\n\nLet's start with the basics: your brand voice. Think of it as the personality of your company in words. It's how you talk to your audience, making your brand feel familiar and unique. Whether it's fun, serious, or something in between, your brand voice helps you connect with people in a meaningful way.\n\nBut here's the challenge: making sure this voice stays the same across all your social media posts can be tough. Ever been about to post something and stopped to wonder, \"Does this really sound like us?\" This is a common issue in social media marketing, where being consistent is important but not always easy.\n\nThat's where ChatGPT comes in. It's like your behind-the-scenes helper that can make sure every tweet, post, or update sounds exactly like your brand. With ChatGPT, you can make sure your brand's personality is always the star of the show on social media. Let's dive in."
            },
            {
            "role": "user",
            "content": "Target Audience: members of the sales team.\nProblem: Members of the sales team often spend a lot of time creating personalized emails for customers in different sales scenarios. \nSolution: With ChatGPT, they can use a prompt and create email templates for different sales scenarios. \nVideo Objective: The objective of the video is to teach the viewer how to use ChatGPT to create email templates for customers and various sales scenarios, so they no longer need to write emails from scratch every single time. "
            },
            {
            "role": "assistant",
            "content": "Title: Create Sales Email Templates with ChatGPT\n\nWelcome to this tutorial, where we address a common challenge faced by sales professionals: the time-consuming task of writing personalized emails for different sales scenarios. Personalizing emails is crucial because it helps build stronger connections with your customers. It shows that you see them as individuals with unique needs and preferences, which can significantly increase the effectiveness of your communication and boost your chances of making a sale.\n\nHowever, the catch is that crafting these personalized emails for various scenarios demands a considerable amount of time and effort. For example, you might need to create a warm introduction email for new leads, a detailed proposal email for interested prospects, a follow-up email after a meeting, or a thank-you email post-purchase. Each of these scenarios requires a different approach, tone, and content, making the task even more daunting.\n\nBut what if there was a way to streamline this process? That's where ChatGPT comes in. ChatGPT is an AI tool that can assist you in creating customized email templates for any sales situation. By leveraging intelligent prompts, ChatGPT helps generate relevant, personalized content, saving you time and effort. Stay with us as we dive into how ChatGPT can transform the way you handle sales emails, making your daily tasks smoother and more productive."
            },
            {
            "role": "user",
            "content": userMessageContent
            }
        ]
    
    return messages