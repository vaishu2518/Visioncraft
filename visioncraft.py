import streamlit as st
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import io
st.set_page_config(
    page_title="CreatorHub",
    layout="wide"
)
st.title("CreatorHub – Content Creator Toolkit")
st.markdown("""
CreatorHub helps content creators with:
- Thumbnail Editing
- Image Enhancement
- Caption Ideas
- Hashtag Suggestions
""")
menu = st.sidebar.selectbox(
    "Choose Tool",
    [
        "Thumbnail Editor",
        "Image Enhancer",
        "Caption Generator",
        "Hashtag Generator"
    ]
)
if menu == "Thumbnail Editor":

    st.header("Thumbnail Editor")

    uploaded_image = st.file_uploader(
        "Upload Image",
        type=["jpg", "png", "jpeg"]
    )

    if uploaded_image:

        image = Image.open(uploaded_image).convert("RGB")

        image = image.resize((1280, 720))

        draw = ImageDraw.Draw(image)

        title_text = st.text_input(
            "Enter Thumbnail Text",
            "MY AWESOME VIDEO"
        )

        text_size = st.slider(
            "Text Size",
            20,
            120,
            70
        )

        text_color = st.selectbox(
            "Text Color",
            ["white", "yellow", "red", "black"]
        )

        x = st.slider("Text X Position", 0, 1000, 100)
        y = st.slider("Text Y Position", 0, 600, 500)

        try:
            font = ImageFont.truetype(
                "arial.ttf",
                text_size
            )
        except:
            font = ImageFont.load_default()

        draw.text(
            (x, y),
            title_text,
            fill=text_color,
            font=font
        )

        st.image(
            image,
            caption="Thumbnail Preview",
            use_container_width=True
        )

        buffer = io.BytesIO()
        image.save(buffer, format="PNG")

        st.download_button(
            label="Download Thumbnail",
            data=buffer.getvalue(),
            file_name="thumbnail.png",
            mime="image/png"
        )

elif menu == "Image Enhancer":

    st.header("Image Enhancer")

    uploaded_image = st.file_uploader(
        "Upload Image",
        type=["jpg", "png", "jpeg"]
    )

    if uploaded_image:

        image = Image.open(uploaded_image)

        brightness = st.slider(
            "Brightness",
            0.5,
            3.0,
            1.0
        )

        contrast = st.slider(
            "Contrast",
            0.5,
            3.0,
            1.0
        )

        sharpness = st.slider(
            "Sharpness",
            0.5,
            3.0,
            1.0
        )

        image = ImageEnhance.Brightness(image).enhance(brightness)
        image = ImageEnhance.Contrast(image).enhance(contrast)
        image = ImageEnhance.Sharpness(image).enhance(sharpness)

        st.image(
            image,
            caption="Enhanced Image",
            use_container_width=True
        )

elif menu == "Caption Generator":

    st.header("Caption Generator")

    topic = st.text_input("Enter Topic")

    if st.button("Generate Captions"):

        captions = [
            f"Leveling up my {topic} journey 🚀",
            f"New {topic} content dropping soon 🔥",
            f"Consistency + {topic} = Success 💯",
            f"Creating something amazing with {topic} ✨",
            f"Stay tuned for more {topic} updates 🎯"
        ]

        for caption in captions:
            st.success(caption)
elif menu == "Hashtag Generator":

    st.header("Hashtag Generator")

    keyword = st.text_input("Enter Keyword")

    if st.button("Generate Hashtags"):

        hashtags = [
            f"#{keyword}",
            f"#{keyword}creator",
            f"#{keyword}editing",
            f"#{keyword}reels",
            f"#{keyword}video",
            f"#{keyword}content",
            f"#viral{keyword}",
            f"#trending{keyword}"
        ]

        st.write(" ".join(hashtags))