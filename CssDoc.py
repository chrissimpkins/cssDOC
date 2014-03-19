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
            if selections and (len(selections[0]) > 1): # text was selected in the editor
                needle = self.view.substr(selections[0])
                needle = clean_query(needle) # clean the query string
                if is_a_css_entity(needle):
                    self.launch_doc_browser(needle) # launch the documentation page
                else:
                    self.launch_search_browser(needle) # launch a search page
            else: # 'hover' handling (cursor located in the CSS element substring)
                parsed_string = self.find_query_hover()
                cleaned_string = clean_query(parsed_string)
                if is_a_css_entity(cleaned_string):
                    self.launch_doc_browser(cleaned_string)
                else:
                    if cleaned_string.startswith(':'): # attempt to add second colon and test for CSS pseudoelement
                        pseudoelement = ':' + cleaned_string
                        if is_a_css_entity(pseudoelement):
                            self.launch_doc_browser(pseudoelement)
                        else:
                            print('cssDOC Plugin Error: Unable to identify the requested text as a CSS element')
                            status_message = "cssDOC: Unable to match the selected substring"
                            sublime.status_message(status_message) # print error message to status bar
                    else:
                        print('cssDOC Plugin Error: Unable to identify the requested text as a CSS element')
                        status_message = "cssDOC: Unable to match the selected substring"
                        sublime.status_message(status_message) # print error message to status bar
        except Exception as e:
            print("cssDOC Plugin Error: There was an error during the execution of the plugin.\n")
            raise e

    # launch documentation URL in browser
    def launch_doc_browser(self, needle):
        if version_info[0] == 2:   # Python 2 (ST 2)
            # needle_escaped = urllib.quote(needle)
            url = "http://developer.mozilla.org/en-US/docs/Web/CSS/" + needle
        else: # Python 3 (ST 3)
            url = "http://developer.mozilla.org/en-US/docs/Web/CSS/" + needle
            # url = urllib.parse.urlparse(url).geturl() # url encode Python 3 interpreter
        print("cssDOC: Opening CSS documentation for '" + needle + "'")
        webbrowser.open(url)

    # launch search URL in browser
    def launch_search_browser(self, needle):
        if version_info[0] == 2: # Python 2 (ST 2)
            # needle_escaped = urllib.quoste(needle)
            url = "http://developer.mozilla.org/en-US/search?q=" + needle + "&topic=css" # url encode Python 2 interpreter
        else: # Python 3 (ST 3)
            url = "http://developer.mozilla.org/en-US/docs/Web/CSS/" + needle
            # url = urllib.parse.urlparse(url).geturl() # url encode Python 3 interpreter
        print("cssDOC: Performing search for CSS documentation on '" + needle + "'")
        webbrowser.open(url)

    # find the query term if 'hover' over the element
    def find_query_hover(self):
        the_selection = self.view.sel()
        start = the_selection[0].begin()
        begin_test = start
        end_test = start
        doc_end_point = self.view.size()

        # find end of the CSS entity
        for x in range(50):
            if end_test < doc_end_point:
                end_test += 1
                end_region = sublime.Region(start, end_test)
                end_test_string = self.view.substr(end_region)
                if end_test_string.endswith(':'): # the end of the CSS element before assignments
                    end_test -= 1 # remove the colon at the end of the assignment
                    break
                elif end_test_string.endswith(';'): # the end of a CSS statement
                    end_test -= 1 # remove the semicolon at the end of the CSS statement
                    break
                elif end_test_string.endswith('{'): # before beginning of a CSS block
                    end_test -= 1 # remove the opening { from the CSS block
                    break
                elif end_test_string.endswith(' '): # ends with a space (likely an element prior to the {} block declaration)
                    end_test -= 1
                    break
                elif end_test_string.endswith('\n'): # end of line
                    end_test -= 1
                    break
                elif end_test_string.endswith(','): # comma between elements
                    end_test -= 1
                    break
                elif end_test_string.endswith('('): # beginning of a parenthesis block
                    end_test -= 1
                    break
                elif end_test_string.endswith('+'): # + operator
                    end_test -= 1
                    break
                elif end_test_string.endswith('>'): # > operator
                    end_test -= 1
                    break
                elif end_test_string.endswith('~'): # ~ operator
                    end_test -= 1
                    break
            else:
                end_test = self.view.size() # end of buffer text

        # find beginning of the CSS entity
        for x in range(50):
            if begin_test > 0:
                begin_test -= 1
                begin_region = sublime.Region(begin_test, start)
                begin_test_string = self.view.substr(begin_region)
                if begin_test_string.startswith(':'):
                    begin_test2 = begin_test - 1 # test for a second colon at beginning of the element
                    if begin_test2 > 0:
                        begin_region_doublecolon = sublime.Region(begin_test2, start)
                        begin_test_string_doublecolon = self.view.substr(begin_region_doublecolon)
                        if begin_test_string_doublecolon.startswith(':'):
                            begin_test = begin_test2 # assign the start point at the beginning of the first colon and return
                            break
                elif begin_test_string.startswith(';'): # the previous CSS statement
                    break
                elif begin_test_string.startswith('{'): # the beginning of the CSS block
                    begin_test += 1 # remove the opening { of the CSS block
                    break
                elif begin_test_string.startswith('}'): # the end of another CSS block
                    begin_test += 1 # remove the closing } of previous block
                    break
                elif begin_test_string.startswith('\n'): # the beginning of line/end of prior line
                    begin_test += 1 # remove the newline
                    break
                elif begin_test_string.startswith('('): # likely inline CSS / advanced media queries / etc
                    begin_test += 1
                    break
                elif begin_test_string.startswith('@'):
                    break # maintain the @ character in the string
                elif begin_test_string.startswith(' '):
                    begin_test += 1
                    break
            else:
                begin_test = 0 # beginning of buffer text
                break
        # return the parsed substring to the calling code
        return self.view.substr(sublime.Region(begin_test, end_test))

# clean the CSS query string
def clean_query(query_string):
    strip_string = query_string.strip()
    if strip_string.endswith(':'):
        strip_string = strip_string[:-1]
        strip_string = strip_string.rstrip()
    if ';' in strip_string:
        strip_string = strip_string.replace(';', '')
        strip_string = strip_string.strip()
    if ':' in strip_string and not strip_string.startswith(':'):
        if '::' in strip_string:
            after_string = strip_string.split('::')[1] # it is a pseudo-element
            strip_string = '::' + after_string
        elif ':' in strip_string: # must remain after the above test logic
            after_string = strip_string.split(':')[1]
            strip_string = ':' + after_string
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

