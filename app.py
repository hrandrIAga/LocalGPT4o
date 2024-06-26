import streamlit as st
import openai
from PIL import Image
import PyPDF2
import io

# Définissez votre clé API OpenAI ici
openai.api_key = ""

def get_gpt4_response(messages):
    # Fonction pour obtenir une réponse de GPT-4
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=messages,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = response.choices[0].message['content'].strip()
    return message

def add_message(role, content):
    # Fonction pour ajouter un message à l'état de session
    st.session_state.messages.append({"role": role, "content": content})

def display_file(file):
    # Fonction pour afficher le contenu d'un fichier téléchargé
    file_type = file.type
    if file_type.startswith("image/"):
        # Affichage des images
        image = Image.open(file)
        st.image(image, caption=file.name)
    elif file_type == "application/pdf":
        # Affichage du contenu des fichiers PDF
        reader = PyPDF2.PdfFileReader(file)
        num_pages = reader.getNumPages()
        text = ""
        for page_num in range(num_pages):
            page = reader.getPage(page_num)
            text += page.extract_text()
        st.text_area("Contenu du PDF", text, height=300)
    elif file_type.startswith("text/") or file_type in ["application/json", "application/javascript"]:
        # Affichage du contenu des fichiers texte, JSON et JavaScript
        content = file.getvalue().decode("utf-8")
        st.text_area(f"Contenu du fichier ({file.name})", content, height=300)
    else:
        # Gestion des types de fichiers non pris en charge
        st.write(f"Type de fichier non pris en charge : {file_type}")

# Titre de l'application
st.title("Chat avec GPT-4")

if 'messages' not in st.session_state:
    # Initialisation de l'état des messages si ce n'est pas déjà fait
    st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]

# CSS pour styliser les bulles de conversation
bubble_css = """
<style>
.user-bubble, .assistant-bubble {
    border-radius: 25px;
    padding: 10px 20px;
    margin: 10px;
    display: inline-block;
    max-width: 60%;
}
.user-bubble {
    background-color: #d1e7dd;
    color: #0f5132;
    align-self: flex-end;
}
.assistant-bubble {
    background-color: #cff4fc;
    color: #055160;
    align-self: flex-start;
}
.bubble-container {
    display: flex;
    flex-direction: column;
}
</style>
"""

# Application du CSS pour les bulles de conversation
st.markdown(bubble_css, unsafe_allow_html=True)

def display_message(message):
    # Fonction pour afficher un message avec détection du type
    content = message["content"]

    if "```" in content or any(keyword in content.lower() for keyword in ["dear", "sincerely", "regards", "best"]):
        # Affichage hors des bulles pour le code ou les e-mails structurés
        st.markdown(f"**{message['role'].capitalize()}:**")
        st.markdown(content)
    else:
        # Affichage dans les bulles
        if message['role'] == 'user':
            st.markdown(f'<div class="bubble-container"><div class="user-bubble">Hrandria: {content}</div></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="bubble-container"><div class="assistant-bubble">GPT-4: {content}</div></div>', unsafe_allow_html=True)

# Affichage des messages de la conversation
for message in st.session_state.messages:
    display_message(message)

# Entrée utilisateur pour la conversation
user_input = st.text_input("Hrandria :", key="input_text")

if st.button("Envoyer"):
    if user_input:
        # Ajout du message utilisateur et obtention de la réponse de GPT-4
        add_message("user", user_input)
        response = get_gpt4_response(st.session_state.messages)
        add_message("assistant", response)
        st.experimental_rerun()

# Sous-titre pour l'upload de fichiers
st.subheader("Upload files (images or pdf")
uploaded_files = st.file_uploader("Choose files", accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        st.write(f"**Fichier téléchargé :** {uploaded_file.name}")
        display_file(uploaded_file)

def chat_with_gpt4():
    # Fonction pour une conversation interactive avec GPT-4 via la console
    conversation_history = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    while True:
        # Entrée utilisateur
        user_input = input("Utilisateur : ")

        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Fin de la conversation.")
            break

        # Ajout de l'entrée utilisateur à l'historique de conversation
        conversation_history.append({"role": "user", "content": user_input})

        # Obtention de la réponse de GPT-4
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=conversation_history
        )

        # Extraction et affichage de la réponse de l'assistant
        assistant_response = response['choices'][0]['message']['content']
        print(f"Assistant : {assistant_response}")

        # Ajout de la réponse de l'assistant à l'historique de conversation
        conversation_history.append({"role": "assistant", "content": assistant_response})

if __name__ == "__main__":
    # Exécution de la fonction de chat interactif si le script est exécuté directement
    chat_with_gpt4()
