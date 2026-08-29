import streamlit as st
import ollama

st.title("AI Writing Assistant")

user_request = st.text_area("What do you want to write about?")

tone = st.selectbox("Choose a tone :",["Formal", "Informal", "Professional", "Friendly"])

length = st.selectbox("Choose the length of the content :",["Short", "Medium", "Long"])

format = st.selectbox("Choose the format of the content :",["Paragraph", "Email", "Blog post", "Social media post"])

audience = st.selectbox("Choose the target audience :",["Manager", "Professor", "Students", "Researchers","Child","Friend","General public"])

if length == "Short":
    length_instruction = "Keep the response concise, around 80-100 words."
elif length == "Medium":
    length_instruction = "Write a moderate-length response, around 150-200 words.Do not exceed 200 words"
else:
    length_instruction = "Write a detailed response, around 250-350 words."

if format == "Paragraph":
    format_instruction = "Write the content in a single paragraph. Do not add subject line or greeting or closing."
elif format == "Email":
    format_instruction = "Write the content in the form of an email. Include a subject line, greeting, and closing."
elif format == "Blog post":
    format_instruction = "Write the content in the form of a blog post. Include a title, introduction, body, and conclusion."
else:
    format_instruction = "Write the content in the form of a social media post. Keep it engaging and concise."

if st.button("Generate"):
    prompt = f"""
    You are an AI writing assistant. 
    Write content based on the user's request
    Use the selected tone.
    User request : {user_request}
    Selected tone : {tone}
    Selected length : {length_instruction}
    Selected format : {format_instruction}
    Selected audience : {audience}
    Never use bracketed placeholders like [manager's name], [user's name] or [any personal information].
    Use generic wording to fill in the content.
    Dont assume any specific details about the user or their request.
    """
    # st.write(prompt)

    try:
        # with st.spinner("Generating content..."):
        response = ollama.chat(model = "qwen2.5:3b-instruct",
                        messages =[
                            {
                                "role" : "user",
                                "content" : prompt
                            }
                        ],
                        stream = True
                        )

        st.subheader("Generated Content:")

        generated_content = ""
        output = st.empty()

        for chunk in response:
            generated_content += chunk["message"]["content"]
            output.write(generated_content)

    except Exception as e:
        st.error("Something went wrong while generating your content. Please wait a moment and try again.")
