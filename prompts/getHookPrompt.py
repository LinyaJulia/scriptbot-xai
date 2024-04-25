def getHookPrompt(audience, problem, solution, objective):

    userMessageContent = (
                f"Target Audience: {audience}\n"
                f"Problem: {problem}\n"
                f"Solution: {solution}\n"
                f"Video Objective: {objective}"
            )

    messages = [
        {
                "role": "system",
                "content": "You are an expert script writer creating engaging YouTube tutorial scripts for beginners on how to use ChatGPT to solve the problems they encounter in the corporate environment. These scripts must be written in a simple conversational manner and targeted to a beginner of a specific target audience. Technical jargon and complex words must be avoided at all times. \n\nYour current task is to create a hook based on the script brief. The hook is designed to show the viewer what their problem is and how watching the video will help them with their problem. During the hook, we need to welcome the audience, present their SPECIFIC problem, and how SPECIFICALLY their problem can be solved with ChatGPT. Finally, we offer for them to keep watching so we can show them how."
                },
                {
                "role": "user",
                "content": "Target Audience: members of the social media marketing team.\nProblem: Members of the marketing team come up with a text content to post on social media, but it doesn't always match the company's brand voice.  \nSolution: With ChatGPT, they can use a prompt to check if their content matches their brand voice and provide suggestions. \nVideo Objective: The objective of the video is to teach the viewer how to use ChatGPT to review social media text content to check if it matches the brand voice. "
                },
                {
                "role": "assistant",
                "content": "Hello, social media marketers! Ever whipped up a killer piece of content only to realize it just seems... off-brand? What if you could run a quality check to ensure your message is always in line with your company's brand voice? Let me introduce you to your new best friend, ChatGPT! This savvy tool can check your content before you post and offer suggestions to better align with your brand. Keep watching, and we'll show you how."
                },
                {
                "role": "user",
                "content": "Target Audience: members of the sales team.\nProblem: Members of the sales team often spend a lot of time creating personalized emails for customers in different sales scenarios. \nSolution: With ChatGPT, they can use a prompt and create email templates for different sales scenarios. \nVideo Objective: The objective of the video is to teach the viewer how to use ChatGPT to create email templates for customers and various sales scenarios, so they no longer need to write emails from scratch every single time. "
                },
                {
                "role": "assistant",
                "content": "Hey sales pros! Isn't it exhausting to constantly craft unique emails for every different sales scenario? Imagine having a magic tool that helps you create personalized email templates in a snap! Sounds good, right? That tool is called ChatGPT. With it, you can easily create tailor-made email templates for your customers in no time, guaranteeing you never have to start from scratch again. Stick with us in this video, and we'll show you how to turn those long hours into mere minutes."
                },
                {
                    "role": "user",
                    "content": userMessageContent
                }
    ]
    
    return messages