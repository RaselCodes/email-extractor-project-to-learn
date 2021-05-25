import pyperclip, re


def promptToContinueOrExit():
    print("\n" * 2)
    print('*' * 20)
    print('\n\nTo proceed, copy or cut some text; after copying/cutting, Simply press Enter Key.')
    print('\nTo exit the program, type anything and press Enter key.\n')


def takeInput():
    fromKeyboard = input('Respond: ')
    return fromKeyboard


def shouldContinue(fromKeyboard):
    if(fromKeyboard == ''):
        return True
    return False




promptToContinueOrExit()

while shouldContinue(takeInput()):
    text = pyperclip.paste()

    #print(text)

    emailRegex = re.compile(r'''(
                    [a-zA-Z0-9._%+-]+ # username
                    @ # @ symbol
                    [a-zA-Z0-9.-]+ # domain name
                    (\.[a-zA-Z]{2,4}) # dot-something
                    )''', re.VERBOSE)

    matches = []
    for groups in emailRegex.findall(text):
        matches.append(groups[0])

    if len(matches) > 0 :
        pyperclip.copy('\n'.join(matches))
        print('Extracted Emails are Copied to Clipboard; Paste Anywhere to see.')
    else:
        print('The text you copied has NO email address.')


    promptToContinueOrExit() 


print('\n\nGood Bye!\n\n')
