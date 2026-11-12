import streamlit as st 

st.title("Input your files (image)",anchor=False)
st.divider()

image = st.file_uploader ( "Upload your Image : ",
                    type=["jpg","jpeg","png"],
                    accept_multiple_files=True,
                    key="file_uploader"
                    )
if image:
    col = st.columns( len(image))
    for i, img in enumerate(image):
        col[i].image(img)

#storage
#st.image("Images/IMG_2020.png")

#url
#st.image("https://cdn.pixabay.com/photo/2015/04/19/08/32/flower-729510_1280.jpg")

