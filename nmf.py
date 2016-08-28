from sklearn.decomposition import NMF
from sklearn.feature_extraction.text import TfidfVectorizer
import collections


def top_words(text, n_topics, n_top_words):

    words = collections.OrderedDict()

    vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, stop_words="english")

    tfidf = vectorizer.fit_transform(text)

    nmf = NMF(n_components=n_topics, random_state=101).fit(tfidf)

    feature_names = vectorizer.get_feature_names()

    for topic_idx, topic in enumerate(nmf.components_):
        key = "Topic " + str((topic_idx+1))
        value = " ".join([feature_names[i] for i in topic.argsort()[:-n_top_words-1:-1]])
        words[key] = value

    return words

