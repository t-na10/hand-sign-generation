import streamlit as st
import subprocess
import os

st.title("Handwriting-Diffusion-App")
st.markdown("This app generates handwriting using the Handwriting Diffusion model.")
textstring = st.text_input("Text to generate handwriting:")
writersource = st.selectbox("Choose a writer source image:",
                            options=[None, "a02-050-03.tif", "g06-150z-03.tif", "j07-370z-01.tif", "k04-274z-01.tif", "n04-255z-01.tif", "r06-412z-04.tif"])
expander = st.expander("See examples of writer source images")
expander.image("assets/a02-050-03.png", caption="a02-050-03.tif")
expander.image("assets/g06-150z-03.png", caption="g06-150z-03.tif")
expander.image("assets/j07-370z-01.png", caption="j07-370z-01.tif")
expander.image("assets/k04-274z-01.png", caption="k04-274z-01.tif")
expander.image("assets/n04-255z-01.png", caption="n04-255z-01.tif")
expander.image("assets/r06-412z-04.png", caption="r06-412z-04.tif")

btn = st.button(label="Submit")


if btn:
    if textstring:
        if writersource:
            result = subprocess.run(
                ["python3.7","inference.py","--textstring", textstring,"--writersource", f"assets/{writersource}","--name", "output/sample"],
                )
        else:
            result = subprocess.run(
                ["python3.7","inference.py","--textstring", textstring,"--name", "output/sample"],
                )
        if result.returncode == 0:
            if os.path.exists("output/sample.png"):
                st.image("output/sample.png")
                with open("output/sample.png", "rb") as f:
                    st.download_button("Download png", f, "sample.png", "image/png")
            else:
                st.error("Output image not found.")
        else:
            st.error(f"Error in subprocess: {result.stderr}")
    else:
        st.error("Please input textstring.")

