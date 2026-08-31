import faiss

import numpy as np


class VectorStore:


    def __init__(

        self,

        embedding_dimension
    ):

        self.index = faiss.IndexFlatL2(

            embedding_dimension
        )


    def add_embeddings(

        self,

        embeddings
    ):

        embeddings = np.array(

            embeddings
        ).astype(

            "float32"
        )


        self.index.add(

            embeddings
        )


    def search(

        self,

        query_embedding,

        top_k=3
    ):

        query_embedding = np.array(

            query_embedding
        ).astype(

            "float32"
        )


        distances, indices = self.index.search(

            query_embedding,

            top_k
        )


        return distances, indices
