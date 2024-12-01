import streamlit as st

image = 'assets/a.jpg'
song1 = 'assets/audio/1.mp3'
song2 = 'assets/audio/2.mp3'

with st.sidebar:
    st.title("Thông tin về Sơn Tùng M-TP")
    st.image(image,caption="Sơn Tùng M-TP")
    st.write("""**Sơn Tùng M-TP** là ca sĩ nổi tiếng nhất Việt Name, với nhiều bài hát hit và nổi tiếng. Được biết đến như những bài hát nổi tiếng sau đây "Chạy Ngay Đi" , "Hãy Trao Cho Anh", "Lạc Trôi" .""")

st.header("Bài Hát Yêu Thích")
songs = [
    {"name": "Chạy Ngay Đi", "audio": song1}, 
    {"name": "Hãy Trao Cho Anh", "audio": song2}
]

for song in songs:
    st.write(f"- {song['name']}")
    st.audio(song["audio"], format = "audio/mp3")

mvs = [
    {"name": "Hãy Trao Cho Anh", "video": "https://www.youtube.com/watch?v=knW7-x7Y7RE"},
    {"name": "Lạc Trôi", "video": "https://www.youtube.com/watch?v=Llw9Q6akRo4"},
]

for mv in mvs:
    st.write(f"- {mv['name']}")
    st.video(mv["video"])