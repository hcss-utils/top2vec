import umap
import umap.plot
import streamlit as st
import matplotlib.pyplot as plot
from pathlib import Path
from top2vec import Top2Vec

st.set_option('deprecation.showPyplotGlobalUse', False)
root = Path(__file__).resolve().parent

@st.cache(allow_output_mutation=True)
def load_model(path="models/210205 - top2vec.model"):
    return Top2Vec.load(root.parent / path)


@st.cache(allow_output_mutation=True)
def reduce_topics(model, num_topic):
    return model.hierarchical_topic_reduction(num_topic)

@st.cache(allow_output_mutation=True)
def build_umap(
    model,
    n_neighbors=15,
    n_components=2,
    metric="cosine",
    random_state=42
):
    return umap.UMAP(
        n_neighbors=n_neighbors, 
        n_components=n_components, 
        metric=metric, 
        random_state=random_state
    ).fit(model._get_document_vectors(norm=False))


def plot_umap(umap_model, t2v_model):
    return umap.plot.points(umap_model, labels=t2v_model.doc_top_reduced)


st.title("Hierarchical topic reduction [top2vec]")
st.write("Sample text explaining something")

t2v_model = load_model()
umap_model = build_umap(model=t2v_model)

num_topic = st.sidebar.slider("number of topics", min_value=2, max_value=50, step=1)
reduce_topics(t2v_model, num_topic)

ax = plot_umap(umap_model, t2v_model)
st.pyplot()
