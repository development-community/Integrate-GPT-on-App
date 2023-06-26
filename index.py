import speech_recognition as sr
import customtkinter
import openai


class App:
    def __init__(self) -> None:
        customtkinter.set_appearance_mode("dark")

        self.app = customtkinter.CTk()
        self.messages = []

        self.define_app()
        self.app.mainloop()

    def define_app (self) -> None:
        self.app.geometry("750x540")
        self.app.title("Integration GPT")

        self.dialog = customtkinter.CTkTextbox(master=self.app, width=700, height=300)
        self.dialog.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

        self.input = customtkinter.CTkTextbox(master=self.app, width=500, height=100)
        self.input.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)

        self.send = customtkinter.CTkButton(master=self.app, text="Send", width=50, command=self.write_input_user)
        self.send.place(relx=0.9, rely= 0.9, anchor=customtkinter.CENTER)

        self.launch_voice = customtkinter.CTkButton(master=self.app, text="Voice", width=50, command=self.voice_input_user)
        self.launch_voice.place(relx=0.1, rely=0.9, anchor=customtkinter.CENTER)

    def write_input_user (self) -> None:
        text_user = self.input.get("0.0", "end")

        if text_user == "" or text_user == "\n":
            return
        
        if text_user == "clear_text()\n":
            self.dialog.delete("0.0", "end")
            self.input.delete("0.0", "end")
            self.messages.clear()
        else:
            self.messages.append({
                "role": "user",
                "content": text_user
            })
            self.dialog.insert("end", f"USER: {text_user}")
            self.input.delete("0.0", "end")

            self.get_answer()

    def voice_input_user (self) -> None:
        recognizer = sr.Recognizer()

        with sr.Microphone(device_index=3) as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)

            print('Listening')
            voice_input = recognizer.listen(source)

            try:
                print('Recognizing')
                input = recognizer.recognize_google(voice_input, language='fr-FR')

                print(input)
                self.messages.append({
                    "role": "user",
                    "content": input,
                })
                self.dialog.insert("end", f"USER: {input}\n")
                self.get_answer()
            except:
                " "

    def get_answer (self) -> None:
        openai.api_key = "OPENAI KEY"

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages
        )

        answer = str(response.choices[0].message.content)

        self.messages.append({
            "role": "assistant",
            "content": answer
        })
        self.dialog.insert("end", f"AI: {answer}\n")

if __name__ == '__main__':
    App()