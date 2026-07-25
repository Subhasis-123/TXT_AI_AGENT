import os
import time
import streamlit as st

from agents.orchestrator import Orchestrator

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="TXT Schema Extraction Agent",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------
with st.sidebar:

    st.title("⚙ AI Settings")

    st.metric("Model", "Gemma 3:4B")
    st.metric("Runtime", "Ollama")
    st.metric("Execution", "Local")

    st.divider()

    st.markdown("## 🤖 AI Pipeline")

    st.success("📄 Template Reader")
    st.success("📂 File Reader")
    st.success("🧠 Gemma Extractor")
    st.success("📊 Excel Writer")

    st.divider()

    st.info(
        """
### About

This AI agent extracts schema details from TXT files and
generates Excel documentation automatically.

**Features**

- Multiple TXT files
- AI Extraction
- Excel Generation
- Local LLM
        """
    )

# ---------------------------------------------------
# Header
# ---------------------------------------------------
st.title("🤖 TXT Schema Extraction Agent")

st.caption("Powered by Gemma 3:4B + Ollama")

st.write(
    """
Automatically extract schema definitions from TXT files and
generate structured Excel documentation using AI.
"""
)

st.divider()

# ---------------------------------------------------
# Upload Section
# ---------------------------------------------------
left, right = st.columns(2)

with left:

    st.subheader("📄 Excel Template")

    template_file = st.file_uploader(
        "",
        type=["xlsx"],
        label_visibility="collapsed"
    )

with right:

    st.subheader("📂 TXT Files")

    txt_files = st.file_uploader(
        "",
        type=["txt"],
        accept_multiple_files=True,
        label_visibility="collapsed"
    )

st.divider()

# ---------------------------------------------------
# Generate Button
# ---------------------------------------------------
generate = st.button(
    "🚀 Generate Excel Files",
    use_container_width=True
)

# ---------------------------------------------------
# Processing
# ---------------------------------------------------
if generate:

    if template_file is None:

        st.error("Please upload an Excel template.")

    elif not txt_files:

        st.error("Please upload one or more TXT files.")

    else:

        start_time = time.time()

        progress = st.progress(0)

        status = st.empty()

        try:

            status.info("📄 Reading Excel Template...")
            progress.progress(15)

            status.info("📂 Reading TXT Files...")
            progress.progress(30)

            status.info("🤖 Initializing AI Agent...")
            progress.progress(45)

            orchestrator = Orchestrator(
                template_file,
                txt_files
            )

            status.info("🧠 Extracting Schema using Gemini...")
            progress.progress(70)

            output_files = orchestrator.run()

            status.info("📊 Creating Excel Files...")
            progress.progress(95)

            progress.progress(100)

            status.success("✅ Processing Completed Successfully")

            elapsed = round(time.time() - start_time, 2)

            # ---------------------------------------------------
            # Summary
            # ---------------------------------------------------
            st.divider()

            st.subheader("📊 Processing Summary")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "TXT Files",
                    len(txt_files)
                )

            with col2:
                st.metric(
                    "Excel Files",
                    len(output_files)
                )

            with col3:
                st.metric(
                    "Time Taken",
                    f"{elapsed} sec"
                )

            # ---------------------------------------------------
            # Downloads
            # ---------------------------------------------------
            st.divider()

            st.subheader("📥 Download Generated Files")

            for output_file in output_files:

                with open(output_file, "rb") as file:

                    st.download_button(
                        label=f"📄 {os.path.basename(output_file)}",
                        data=file,
                        file_name=os.path.basename(output_file),
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                        use_container_width=True
                    )

        except Exception as e:

            st.error(f"❌ {str(e)}")

# ---------------------------------------------------
# Footer
# ---------------------------------------------------
st.divider()

st.caption(
    "Built with ❤️ using Python • Streamlit • Ollama • Gemma 3 • OpenPyXL"
)