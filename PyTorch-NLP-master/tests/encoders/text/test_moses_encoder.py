import pickle
import sys

import pytest

from torchnlp.encoders.text import MosesEncoder


@pytest.fixture
def input_():
    return ("This ain't funny. It's actually hillarious, yet double Ls. | [] < > [ ] & " +
            "You're gonna shake it off? Don't?")


@pytest.fixture
def encoder(input_):
    return MosesEncoder([input_])


@pytest.mark.skipif(
    sys.version_info >= (3, 7), reason="Running NLTK moses with Python 3.7 halts on travis.")
def test_moses_encoder(encoder, input_):
    # TEST adapted from example in http://www.nltk.org/_modules/nltk/tokenize/moses.html
    expected_tokens = [
        'This', 'ain', '&apos;t', 'funny', '.', 'It', '&apos;s', 'actually', 'hillarious', ',',
        'yet', 'double', 'Ls', '.', '&#124;', '&#91;', '&#93;', '&lt;', '&gt;', '&#91;', '&#93;',
        '&amp;', 'You', '&apos;re', 'gonna', 'shake', 'it', 'off', '?', 'Don', '&apos;t', '?'
    ]
    expected_decode = ("This ain't funny. It's actually hillarious, yet double Ls. | [] < > [] & " +
                       "You're gonna shake it off? Don't?")
    tokens = encoder.encode(input_)
    assert [encoder.index_to_token[i] for i in tokens] == expected_tokens
    assert encoder.decode(tokens) == expected_decode


@pytest.mark.skipif(
    sys.version_info >= (3, 7), reason="Running NLTK moses with Python 3.7 halts on travis.")
def test_is_pickleable(encoder):
    pickle.dumps(encoder)
