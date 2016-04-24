from flask import render_template, flash, redirect, request
from app import app, rake
from .forms import TextForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    text = None
    sortedKeywords = None
    keywordcandidates = None
    stoppath = "app/SmartStoplist.txt"
    form = TextForm()
    if form.validate_on_submit():
        text = form.text.data
        sentenceList = rake.split_sentences(text)
        sentences = []
        for sent in sentenceList:
            if sent == '':
                continue
            else:
                sentences.append(sent.strip())

        stopwordpattern = rake.build_stop_word_regex(stoppath)
        phraseList = rake.generate_candidate_keywords(sentences, stopwordpattern)

        wordscores = rake.calculate_word_scores(phraseList)
        keywordcandidates = rake.generate_candidate_keyword_scores(phraseList, wordscores)

        sortedKeywords = sorted(keywordcandidates.items(), key=lambda x: (-x[1], x[0]))
        form.text.data = ''
    return render_template('index.html', form=form, text=sortedKeywords)


