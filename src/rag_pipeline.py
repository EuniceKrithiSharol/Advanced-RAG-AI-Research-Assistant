from src.retriever import retrieve_relevant_chunks


def generate_answer(

    question,

    embedding_model,

    vector_store,

    chunks
):

    relevant_chunks = (

        retrieve_relevant_chunks(

            question,

            embedding_model,

            vector_store,

            chunks,

            top_k=3
        )
    )


    if not relevant_chunks:

        return (

            "I could not find relevant information "
            "in the uploaded document.",

            []
        )


    context = "\n\n".join(

        relevant_chunks
    )


    answer = (

        "Based on the retrieved document context:\n\n"

        +

        context
    )


    return (

        answer,

        relevant_chunks
    )
