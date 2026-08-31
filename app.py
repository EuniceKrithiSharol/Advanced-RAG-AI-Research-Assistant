import streamlit as st
import tempfile

from src.document_loader import extract_text_from_pdf
from src.text_chunker import create_chunks
from src.embeddings import EmbeddingModel
from src.vector_store import VectorStore
from src.retriever import retrieve_relevant_chunks
from src.rag_pipeline import generate_answer


# -------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------

st.set_page_config(
    page_title="Advanced RAG AI Research Assistant",
    page_icon="🤖",
    layout="wide"
)


# -------------------------------------------------
# SESSION STATE
# -------------------------------------------------

if "vector_store" not in st.session_state:

    st.session_state.vector_store = None


if "chunks" not in st.session_state:

    st.session_state.chunks = []


if "embedding_model" not in st.session_state:

    st.session_state.embedding_model = EmbeddingModel()


# -------------------------------------------------
# TITLE
# -------------------------------------------------

st.title(
    "🤖 Advanced RAG AI Research Assistant"
)


st.markdown(
    "Upload research documents, build a semantic knowledge base, "
    "and ask context-aware questions using Retrieval-Augmented Generation."
)


# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

st.sidebar.header(
    "🧠 RAG Architecture"
)


st.sidebar.info(
    """
    1. Upload PDF document

    2. Extract document text

    3. Split text into chunks

    4. Generate embeddings

    5. Store embeddings in vector index

    6. Retrieve relevant context

    7. Generate context-aware answer
    """
)


# -------------------------------------------------
# FILE UPLOAD
# -------------------------------------------------

st.header(
    "📄 Upload Research Document"
)


uploaded_file = st.file_uploader(

    "Upload a PDF document",

    type=["pdf"]
)


if uploaded_file is not None:

    if st.button(
        "📚 Build Knowledge Base"
    ):

        with st.spinner(

            "Processing document and building vector knowledge base..."
        ):

            with tempfile.NamedTemporaryFile(

                delete=False,

                suffix=".pdf"

            ) as temp_file:

                temp_file.write(

                    uploaded_file.getvalue()
                )


                temp_file_path = temp_file.name


            document_text = extract_text_from_pdf(

                temp_file_path
            )


            chunks = create_chunks(

                document_text,

                chunk_size=500,

                overlap=100
            )


            embeddings = (

                st.session_state.embedding_model
                .generate_embeddings(
                    chunks
                )
            )


            vector_store = VectorStore(

                embeddings.shape[1]
            )


            vector_store.add_embeddings(

                embeddings
            )


            st.session_state.vector_store = (

                vector_store
            )


            st.session_state.chunks = (

                chunks
            )


        st.success(
            "Knowledge base created successfully!"
        )


        col1, col2 = st.columns(2)


        col1.metric(
            "Document Chunks",
            len(chunks)
        )


        col2.metric(
            "Embedding Dimension",
            embeddings.shape[1]
        )


# -------------------------------------------------
# QUESTION ANSWERING
# -------------------------------------------------

st.divider()


st.header(
    "💬 Ask Questions About Your Document"
)


question = st.text_input(

    "Ask a question",

    placeholder=(
        "Example: What are the main findings in this research?"
    )
)


if st.button(
    "🔍 Search Knowledge Base"
):

    if (

        st.session_state.vector_store is None

    ):

        st.warning(
            "Please upload and process a document first."
        )


    elif question.strip() == "":

        st.warning(
            "Please enter a question."
        )


    else:

        with st.spinner(

            "Retrieving relevant research context..."
        ):

            answer, sources = generate_answer(

                question,

                st.session_state.embedding_model,

                st.session_state.vector_store,

                st.session_state.chunks
            )


        st.subheader(
            "🤖 Research Assistant Response"
        )


        st.success(
            answer
        )


        st.subheader(
            "📚 Retrieved Source Context"
        )


        for index, source in enumerate(

            sources,

            start=1
        ):

            with st.expander(

                f"Source Chunk {index}"
            ):

                st.write(
                    source
                )


# -------------------------------------------------
# SYSTEM INFORMATION
# -------------------------------------------------

st.divider()


st.header(
    "📊 System Information"
)


col1, col2, col3 = st.columns(3)


col1.metric(
    "AI Architecture",
    "RAG"
)


col2.metric(
    "Embedding Model",
    "Sentence Transformers"
)


col3.metric(
    "Vector Search",
    "FAISS"
)


# -------------------------------------------------
# HOW IT WORKS
# -------------------------------------------------

st.divider()


st.header(
    "⚙️ How It Works"
)


st.code(
    """
PDF Document
      ↓
Text Extraction
      ↓
Document Chunking
      ↓
Embedding Generation
      ↓
FAISS Vector Index
      ↓
Semantic Retrieval
      ↓
Relevant Context
      ↓
Context-Aware Response
    """,
    language="text"
)


# -------------------------------------------------
# FOOTER
# -------------------------------------------------

st.divider()


st.caption(
    "Advanced RAG AI Research Assistant | "
    "Python • Generative AI • NLP • "
    "Embeddings • Semantic Search • FAISS"
)
