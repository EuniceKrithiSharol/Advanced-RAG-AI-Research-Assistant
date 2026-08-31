from src.text_chunker import create_chunks


def test_create_chunks():

    text = (

        "Artificial intelligence is transforming industries. "

        * 200
    )


    chunks = create_chunks(

        text,

        chunk_size=100,

        overlap=20
    )


    assert len(

        chunks

    ) > 1


    assert all(

        len(

            chunk

        ) > 0

        for chunk in chunks
    )
