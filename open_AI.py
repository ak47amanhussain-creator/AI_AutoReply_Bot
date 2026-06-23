from google import genai

client = genai.Client(api_key="YOUR_API_KEY")  # AIza se shuru honi chahiye key


Conversation= """
[20:02, 16/6/2026] +91 79870 49061: Company se number mil jata hai
[20:02, 16/6/2026] amanhussain1308: konsi company?
[20:02, 16/6/2026] +91 79870 49061: konsi company?
Apne kuch bhi online game me login Kiya hoga
[20:02, 16/6/2026] +91 79870 49061: Use
[20:03, 16/6/2026] +91 79870 49061: Time ni bro kr n hai ya ni abhi ful profit hai isme is game ke bare me sab batuga
[20:03, 16/6/2026] +91 79870 49061: Aapko
[20:03, 16/6/2026] +91 79870 49061: Kaha se ho
[20:03, 16/6/2026] amanhussain1308: nahi kar sakta , abhi  pesa nahi hai account mai itna
[20:04, 16/6/2026] +91 79870 49061: nahi kar sakta , abhi  pesa nahi hai account mai itna
Kitna hai
[20:04, 16/6/2026] amanhussain1308: 80
[20:04, 16/6/2026] +91 79870 49061: 80 se 230
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"""
            You are Aman.

            This is a WhatsApp conversation.

            Analyze all the conversation.
            Reply in a medium, natural WhatsApp style.
            Don't mention that you are an AI.
            {Conversation}
            """
)

print(response.text)

