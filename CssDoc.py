#!/usr/bin/env python
# encoding: utf-8

import sublime
import sublime_plugin
import webbrowser
from sys import version_info
import urllib


# CSS Documentation Command
class CssDocCommand(sublime_plugin.TextCommand):
    def run(self, selected_text):
        try:
            selections = self.view.sel()
            if selections:
                needle = self.view.substr(selections[0])
                if len(needle) == 0:
                    print("cssDOC Plugin Error: There was no selected string for the CSS documentation search.  Please select a string in your document and try again.")
                else:
                    needle = clean_query(needle) # clean the query string
                    if version_info[0] == 2:     # Python 2 (ST 2)
                        if is_a_css_entity(needle):
                            needle_escaped = urllib.quote(needle)
                            url = "http://developer.mozilla.org/en-US/docs/Web/CSS/" + needle_escaped
                        else:
                            needle_escaped = urllib.quote(needle)
                            url = "http://developer.mozilla.org/en-US/search?q=" + needle_escaped + "&topic=css" # url encode Python 2 interpreter
                    else:                        # Python 3 (ST 3)
                        if is_a_css_entity(needle):
                            url = "http://developer.mozilla.org/en-US/docs/Web/CSS/" + needle
                        else:
                            url = "http://developer.mozilla.org/en-US/search?q=" + needle + "&topic=css"
                        url = urllib.parse.urlparse(url).geturl() # url encode Python 3 interpreter
                    print("cssDOC: Performing search for CSS documentation on the query, '" + needle + "'")
                    webbrowser.open(url)
            else:
                print("cssDOC Plugin Error: There was no selected string for the search.  Please select a string in your document and try again.")
        except Exception as e:
            print("cssDOC Plugin Error: There was an error during the execution of the plugin.\n")
            raise e

def clean_query(query_string):
    strip_string = query_string.strip()
    if strip_string.endswith(':'):
        strip_string = strip_string[:-1]
        strip_string = strip_string.rstrip()
    return strip_string

def is_a_css_entity(query_string):
    css_set = set([
    ':active', '::after', 'align-content', 'align-items', 'align-self', 'all', 'angle', 'animation', 'animation-delay',
    'animation-direction', 'animation-duration', 'animation-fill-mode', 'animation-iteration-count', 'animation-name',
    'animation-play-state', 'animation-timing-function', 'attr', 'auto',
    'backface-visibility', 'background', 'background-attachment', 'background-blend-mode', 'background-clip',
    'background-color', 'background-image', 'background-origin', 'background-position', 'background-repeat',
    'background-size', '::before', 'border', 'border-bottom', 'border-bottom-color', 'border-bottom-left-radius',
    'border-bottom-right-radius', 'border-bottom-style', 'border-bottom-width', 'border-collapse', 'border-color',
    'border-image', 'border-image-outset', 'border-image-repeat', 'border-image-slice', 'border-image-source',
    'border-image-width', 'border-left', 'border-left-color', 'border-left-left-radius', 'border-left-right-radius',
    'border-left-style', 'border-left-width', 'border-radius', 'border-right', 'border-right-color',
    'border-right-left-radius', 'border-right-right-radius', 'border-right-style', 'border-right-width',
    'border-spacing', 'border-style', 'border-top', 'border-top-color', 'border-top-left-radius',
    'border-top-right-radius', 'border-top-style', 'border-top-width', 'border-width', 'bottom', 'box-shadow',
    'box-sizing', 'break-after', 'break-before', 'break-inside',
    'calc', 'caption-side', 'ch', '@charset',':checked', '::choices', 'clear', 'clip', 'clip-path', 'cm', 'color',
    'columns', 'column-count', 'column-fill', 'column-gap', 'column-rule', 'column-rule-color', 'column-rule-style',
    'column-rule-width', 'column-span', 'column-width', 'content', 'counter-increment', 'counter-reset',
    'counter-style', 'cursor',
    ':default', 'deg', ':dir', 'direction', ':disabled', 'display', '@document', 'dpcm', 'dpi', 'dppx',
    'element', 'em', ':empty', 'empty-cells', ':enabled', 'ex',
    'filter', ':first', ':first-child', '::first-letter', '::first-line', ':first-of-type', 'flex', 'flex-basis',
    'flex-direction', 'flex-flow', 'flex-grow', 'flex-shrink', 'flex-wrap', 'float', ':focus', 'font', '@font-face',
    'font-family', 'font-feature-settings', 'font-size', 'font-size-adjust', 'font-stretch', 'font-style',
    'font-variant', 'font-variant-ligatures', 'font-weight', 'frequency', ':fullscreen',
    'grad', 'gradient',
    'height', ':hover', 'hyphens', 'hz',
    'image', 'image-rendering', 'image-orientation', 'ime-mode', '@import', 'in', ':indeterminate', ':in-range',
    'inherit', 'initial', 'integer', ':invalid',
    'justify-content',
    '@keyframes', 'khz',
    ':last-child', ':last-of-type', 'left', ':left', 'length', 'letter-spacing', ':link', 'line-height', 'list-style',
    'list-style-image', 'list-style-position', 'list-style-type',
    'margin', 'margin-bottom', 'margin-left', 'margin-right', 'margin-top', 'marks', 'mask', 'mask-type', 'max-height',
    'max-width', '@media', 'min-height', 'min-width', 'mix-blend-mode', 'mm', 'ms',
    '@namespace', 'none', 'normal', ':not', ':nth-child', ':nth-last-child', ':nth-last-of-type', ':nth-of-type',
    ':only-child', ':only-of-type', 'opacity', ':optional', 'order', 'orphans', 'outline', 'outline-color',
    'outline-offset', 'outline-style', 'outline-width', ':out-of-range', 'overflow', 'overflow-wrap', 'overflow-x',
    'overflow-y', 'overflow-clip-box',
    'padding', 'padding-bottom', 'padding-left', 'padding-right', 'padding-top', '@page', 'page-break-after',
    'page-break-before', 'page-break-inside', 'pc', 'percentage', 'perspective', 'perspective-origin',
    'pointer-events', 'position', 'pt', 'px',
    'quotes',
    'rad', 'radial-gradient', ':read-write', 'rem', 'repeating-linear-gradient', 'repeating-radial-gradient',
    ':required', 'resize', 'resolution', 'right', ':right', ':root',
    ':scope', '::selection', 'shape', 'string', '@supports',
    'table-layout', 'tab-size', ':target', 'text-align', 'text-align-last', 'text-decoration',
    'text-decoration-color', 'text-decoration-line', 'text-decoration-style', 'text-indent', 'text-overflow',
    'text-rendering', 'text-shadow', 'text-transform', 'text-underline-position', 'time', 'timing-function',
    'top', 'transform', 'transform-origin', 'transform-style', 'transition', 'transition-delay',
    'transition-duration', 'transition-property', 'transition-timing-function',
    'unicode-bidi', 'unicode-range', 'unset', 'uri', 'url',
    ':valid', 'vertical-align', 'vh', 'visibility', ':visited',
    'white-space', 'widows', 'width', 'word-break', 'word-spacing', 'word-wrap', 'writing-mode',
    'z-index'
])

    if query_string in css_set:
        return True
    else:
        return False

