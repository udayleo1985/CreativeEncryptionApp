import streamlit as st
from cryptography.fernet import Fernet

st.set_page_config(page_title="🔐 Creative Encryptor", layout="centered")

st.title("🔐 Creative Text Encryptor & Decryptor")

# Generate a key
key = Fernet.generate_key()
cipher = Fernet(key)

st.code(f"Generated Key: {key.decode()}", language='text')

text = st.text_area("Enter your message")

if st.button("Encrypt & Decrypt"):
    encrypted = cipher.encrypt(text.encode())
    st.success(f"🔒 Encrypted: {encrypted.decode()}")

    decrypted = cipher.decrypt(encrypted).decode()
    st.info(f"🔓 Decrypted: {decrypted}")