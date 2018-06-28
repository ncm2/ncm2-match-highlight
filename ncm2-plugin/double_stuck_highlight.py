# -*- coding: utf-8 -*-

from ncm2_core import ncm2_core


def wrap(ncm2_core):
    from ncm2 import getLogger

    logger = getLogger(__name__)

    replace_map = [('0', '𝟘'),
                   ('1', '𝟙'),
                   ('2', '𝟚'),
                   ('3', '𝟛'),
                   ('4', '𝟜'),
                   ('5', '𝟝'),
                   ('6', '𝟞'),
                   ('7', '𝟟'),
                   ('8', '𝟠'),
                   ('9', '𝟡'),
                   ('A', '𝔸'),
                   ('B', '𝔹'),
                   ('C', 'ℂ'),
                   ('D', '𝔻'),
                   ('E', '𝔼'),
                   ('F', '𝔽'),
                   ('G', '𝔾'),
                   ('H', 'ℍ'),
                   ('I', '𝕀'),
                   ('J', '𝕁'),
                   ('K', '𝕂'),
                   ('L', '𝕃'),
                   ('M', '𝕄'),
                   ('N', 'ℕ'),
                   ('O', '𝕆'),
                   ('P', 'ℙ'),
                   ('Q', 'ℚ'),
                   ('R', 'ℝ'),
                   ('S', '𝕊'),
                   ('T', '𝕋'),
                   ('U', '𝕌'),
                   ('V', '𝕍'),
                   ('W', '𝕎'),
                   ('X', '𝕏'),
                   ('Y', '𝕐'),
                   ('Z', 'ℤ'),
                   ('a', '𝕒'),
                   ('b', '𝕓'),
                   ('c', '𝕔'),
                   ('d', '𝕕'),
                   ('e', '𝕖'),
                   ('f', '𝕗'),
                   ('g', '𝕘'),
                   ('h', '𝕙'),
                   ('i', '𝕚'),
                   ('j', '𝕛'),
                   ('k', '𝕜'),
                   ('l', '𝕝'),
                   ('m', '𝕞'),
                   ('n', '𝕟'),
                   ('o', '𝕠'),
                   ('p', '𝕡'),
                   ('q', '𝕢'),
                   ('r', '𝕣'),
                   ('s', '𝕤'),
                   ('t', '𝕥'),
                   ('u', '𝕦'),
                   ('v', '𝕧'),
                   ('w', '𝕨'),
                   ('x', '𝕩'),
                   ('y', '𝕪'),
                   ('z', '𝕫'), ]

    old_matches_filter = ncm2_core.matches_filter

    def new_matches_filter(data, sr, base, matches):
        matches = old_matches_filter(data, sr, base, matches)

        for i in range(len(matches)):
            m = matches[i]
            if m['abbr'] != m['word']:
                continue
            if 'word_highlight' not in m['user_data']:
                continue
            hl = m['user_data']['word_highlight']
            for b, e in hl:
                sub = m['abbr'][b:e]
                for k, v in replace_map:
                    sub = sub.replace(k, v)
                a = m['abbr']

                # somehow the last highligted character is not properly
                # displayed in the terminal, append a space as workaround
                matches[i]['abbr'] = a[:b] + sub + (a[e:] or ' ')

            logger.info('new abbr [%s]', matches[i]['abbr'])

        logger.info('matches [%s]', matches)

        return matches

    ncm2_core.matches_filter = new_matches_filter


wrap(ncm2_core)
