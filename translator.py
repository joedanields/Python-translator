from googletrans import Translator, LANGUAGES

def translate_text(text, target_language):
    translator = Translator()
    try:
        translation = translator.translate(text, dest=target_language)
        return translation.text, translation.src
    except Exception as e:
        return "Translation failed: " + str(e), None

def main():
    print("Welcome to the Advanced Language Translator Chatbot!")
    print("Type 'languages' to see the list of supported languages or 'exit' to quit.")
    
    while True:
        user_input = input("\nEnter text to translate (or 'exit' to quit): ")
        
        if user_input.lower() == "exit":
            print("Goodbye! Have a great day!")
            break
        
        if user_input.lower() == "languages":
            for code, language in LANGUAGES.items():
                print(f"{code}: {language}")
            continue
        
        target_language = input("Enter the target language code (e.g., 'en' for English, 'ta' for Tamil): ").lower()
        
        if target_language not in LANGUAGES:
            print("Invalid language code. Type 'languages' to see the supported options.")
            continue
          
        translated_text, source_language_code = translate_text(user_input, target_language)
        
        if source_language_code:
            source_language_name = LANGUAGES.get(source_language_code, "Unknown")
            print(f"Detected Source Language: {source_language_name}")
        print(f"Translated Text: {translated_text}")

if __name__ == "__main__":
    main()
