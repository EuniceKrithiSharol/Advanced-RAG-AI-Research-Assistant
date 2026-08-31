def retrieve_relevant_chunks(

    query,

    embedding_model,

    vector_store,

    chunks,

    top_k=3
):

    query_embedding = (

        embedding_model
        .generate_query_embedding(
            query
        )
    )


    distances, indices = (

        vector_store.search(

            query_embedding,

            top_k
        )
    )


    retrieved_chunks = []


    for index in indices[0]:

        if index < len(chunks):

            retrieved_chunks.append(

                chunks[index]
            )


    return retrieved_chunks
