import time
import pyautogui
import pyperclip
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")


# Give yourself a few seconds to switch to the target window
time.sleep(3)

# Click the icon
pyautogui.click(1322, 1050)

# Wait for the window to become active
time.sleep(1)

def is_last_message_from_sender(chat_text, sender="Mummy"):
    if not chat_text.strip():
        return False

    lines = [line.strip() for line in chat_text.splitlines() if line.strip()]

    if not lines:
        return False

    last_message = lines[-1]

    print("LAST LINE =", last_message)

    return f"] {sender}:" in last_message

while(True):
    pyautogui.moveTo(703, 193, duration=0.2)

    pyautogui.dragTo(1876, 922, duration=1.0, button='left')

        # Small delay to ensure selection is complete
    time.sleep(0.3)

    # Copy selected text (Ctrl+C)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(1403, 876)

    # Wait for clipboard to update
    time.sleep(0.2)

    # Read clipboard into a variable
    copied_text = pyperclip.paste()

    print("Copied Text:")
    print(copied_text)

    if is_last_message_from_sender(copied_text):

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
                    You are Aman.

                    This is a WhatsApp conversation.

                    Analyze all the chat but reply only to the last message.
                    Reply in a short-medium, natural WhatsApp style.
                    Don't mention that you are an AI.
                    {copied_text}
                    """
        )

        final=response.text
        pyperclip.copy(final)

        pyautogui.click(1242, 968)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)

        pyautogui.press('enter')



