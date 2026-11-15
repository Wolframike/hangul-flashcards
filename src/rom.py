"""Romanize a pronounced-form Hangul string with Revised Romanization letters (the page's ローマ字 column)."""
import re

ONSET = ['g', 'kk', 'n', 'd', 'tt', 'r', 'm', 'b', 'pp', 's', 'ss', '', 'j', 'jj', 'ch', 'k', 't', 'p', 'h']
VOWEL = ['a', 'ae', 'ya', 'yae', 'eo', 'e', 'yeo', 'ye', 'o', 'wa', 'wae', 'oe', 'yo', 'u', 'wo', 'we', 'wi', 'yu', 'eu', 'ui', 'i']
CODA = {0: '', 1: 'k', 4: 'n', 7: 't', 8: 'l', 16: 'm', 17: 'p', 21: 'ng'}  # pronounced forms only have these 7 codas


def roman_word(word):
    out, prev_coda = '', None
    for ch in word:
        code = ord(ch) - 0xAC00
        if not 0 <= code < 11172:
            out += ch
            prev_coda = None
            continue
        onset, vowel, coda = code // 588, code % 588 // 28, code % 28
        if onset == 5 and prev_coda == 8:
            initial = 'l'                     # ㄹ after ㄹ: ll
        else:
            initial = ONSET[onset]
            if onset == 11 and prev_coda == 21:
                out += '-'                    # ㅇ coda before a vowel: goyang-i
        out += initial + VOWEL[vowel] + CODA[coda]
        prev_coda = coda
    return re.sub(r'(.)\1\1', r'\1\1', out)   # hak + kkyo -> hakkyo


def roman(text):
    return ' '.join(roman_word(w) for w in text.split(' '))
