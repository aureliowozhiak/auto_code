import openai

#open text file
text_file = open("key", "r")

#read file
key = text_file.read()

#close file
text_file.close()

# Insert Open AI key account
openai.api_key = key


class AutoCode:

    # Função para obter respostas da API OpenAI
    def get_openai_response(self, text):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=text,
            max_tokens=4000,
        )
        return response

    def get_openai_response_text(self, text):
        return self.get_openai_response(text).choices[0].text

    def create_file(self, file_name, file_content):

        #open text file
        text_file = open(file_name, "w")

        #write string to file
        text_file.write(file_content)

        #close file
        text_file.close()

    def create_class(self, class_name, class_main_function, code_lang = "Python", extension = ".py"):
        text = f"in {code_lang} create a class with the name {class_name} and methods that makes {class_main_function}"
        response_content = self.get_openai_response_text(text)
        self.create_file(f"{class_name.lower()}{extension}", response_content)

