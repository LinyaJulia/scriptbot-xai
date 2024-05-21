def getCourseDescription(hook, titleAndIntro):

    userMessageContent = (
        f"Title and Intro: {hook} {titleAndIntro}\n")
    
    messages=[
        {
        "role": "system",
        "content": [
            {
            "type": "text",
            "text": "Your task is to write Course Descriptions based on an introduction script of a video according to a specific structure. Here are the step-by-step instructions for writing course descriptions: \n1. Identify the Problem or Challenge: Start with a question or statement that clearly identifies a common issue the audience might be facing. For example: \"Struggling to create invoices that reflect your brand's sophistication?\"\n2. Introduce the Solution: Introduce the tool or solution that will help address the problem. For example: \"In this tutorial, you'll discover how ChatGPT-4 can help you design professional, streamlined invoices effortlessly.\"\n3. Highlight Key Learning Points or Benefits: Mention the main benefits or key points the audience will learn from the tutorial. Focus on the practical and actionable insights they will gain. For example: \"Master the art of crafting well-structured, brand-aligned invoices with industry standards, optimal color schemes, and strategic component placements.\"\n4. Encourage Engagement with a Call to Action: End with a strong call to action that encourages the audience to join the tutorial and emphasizes the value they'll get from it. For example: \"Let's elevate your invoicing game together!\"\n\nThe total description should be 4 sentences long. \n\nHere is an example breakdown\n1, Identify the Problem or Challenge: \"Struggling to create invoices that reflect your brand's sophistication?\"\n2. Introduce ChatGPT as the Solution: \"In this tutorial, you'll discover how ChatGPT-4 can help you design professional, streamlined invoices effortlessly.\"\n3. Highlight Key Learning Points or Benefits: \"Master the art of crafting well-structured, brand-aligned invoices with industry standards, optimal color schemes, and strategic component placements.\"\n4. Encourage Engagement with a Call to Action: \"Let's elevate your invoicing game together!\""
            }
        ]
        },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "\"Do you find yourself overwhelmed with the process of data visualization? Many professionals struggle to turn raw data into meaningful insights. In today's fast-paced world, having the ability to quickly and effectively visualize data is crucial. In this video, we will explore how you can use ChatGPT-4 to simplify and enhance your data visualization process. You'll learn how to create clear, impactful visualizations that can help you make informed decisions and communicate your findings effectively. We'll cover best practices, common pitfalls, and advanced techniques to take your data visualization skills to the next level. Join us and transform the way you see and use data!\""
            }
        ]
        },
        {
        "role": "assistant",
        "content": [
            {
            "type": "text",
            "text": "Do you find yourself overwhelmed with the process of data visualization? In this tutorial, we will explore how you can use ChatGPT-4 to simplify and enhance your data visualization process. You'll learn how to create clear, impactful visualizations that can help you make informed decisions and communicate your findings effectively. We'll cover best practices, common pitfalls, and advanced techniques to take your data visualization skills to the next level. Join us and transform the way you see and use data!"
            }
        ]
        },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": userMessageContent
            }
        ]
        }
    ]

    return messages
    

