# import streamlit as st



# def clear_input_field():
#     st.session_state.user_question = st.session_state.user_input
#     st.session_state.user_input = ""
    
# def set_send_input():
#     st.session_state.send_input = True
#     clear_input_field()


# def main():
    
#     st.title("Agent for Honne ")
#     chat_container = st.container()
    
#     if "send_input" not in st.session_state:
#         st.session_state.send_input = False
#         st.session_state.user_question = ""
    
#     user_input = st.text_input("Type your message here", key="user_input", on_change=set_send_input)
    
#     send_button =  st.button("Send", key="send_button")
    
#     if send_button or st.session_state.send_input:
        
#         if st.session_state.user_question != "":
#             llm_response = "this is the response of the llm model"
            
#             with chat_container:
#                 st.chat_message("user").write(st.session_state.user_question)
#                 st.chat_message("ai").write("Here is the answer") 

# if __name__ == "__main__":
#     main()


# codigo 2


# import streamlit as st

# def clear_input_field():
#     st.session_state.user_input = ""

# def main():
#     st.title("Agent for Honne")

#     # Inicializar la lista de mensajes si no existe
#     if "messages" not in st.session_state:
#         st.session_state.messages = []

#     # Mostrar todos los mensajes guardados
#     for message in st.session_state.messages:
#         with st.chat_message(message["role"]):
#             st.write(message["content"])

#     # Input del usuario
#     user_input = st.chat_input("Type your message here", key="user_input")

#     if user_input:
#         # Agregar mensaje del usuario a la lista
#         st.session_state.messages.append({"role": "user", "content": user_input})
        
#         # Simular respuesta del modelo LLM
#         llm_response = "This is the response of the llm model"
        
#         # Agregar respuesta del AI a la lista
#         st.session_state.messages.append({"role": "assistant", "content": llm_response})

#         # Mostrar los nuevos mensajes
#         with st.chat_message("user"):
#             st.write(user_input)
#         with st.chat_message("assistant"):
#             st.write(llm_response)

#         # Limpiar el input después de procesar
#         clear_input_field()

# if __name__ == "__main__":
#     main()

## codigo 3

import streamlit as st
import tools

# # test answer_query
# query = "Que ha realizado Honne en DevOps"
# print("\n",tools.answer_query(query))

def main():
    # st.title("Honne IA HUB 🤖")
    st.markdown("<h1 style='text-align: center;'> 🤖 Honne IA HUB 🤖</h1>", unsafe_allow_html=True)


    # Inicializar la lista de mensajes si no existe
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Mostrar todos los mensajes guardados
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Input del usuario
    user_input = st.chat_input("Type your message here")

    if user_input:
        # Agregar mensaje del usuario a la lista
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Simular respuesta del modelo LLM
        llm_response = tools.answer_query(user_input)
        
        # Agregar respuesta del AI a la lista
        st.session_state.messages.append({"role": "assistant", "content": llm_response})

        # Forzar la actualización de la interfaz
        st.rerun()

if __name__ == "__main__":
    main()