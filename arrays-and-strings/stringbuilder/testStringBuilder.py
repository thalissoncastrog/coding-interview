import unittest
from stringbuilder import StringBuilder

class TestStringBuilder(unittest.TestCase):
    
    def testAppend(self):
        text = StringBuilder()
        text.append("My")
        text.append(" ")
        text.append("Name")
        text.append(" ")
        text.append("is")
        text.append(":")
        text.append(" ")
        text.append("Adão")
        text.append(" ")
        text.append("Thalisson")
        text.append(" ")
        text.append("Castro")
        text.append(" ")
        text.append("Guimarães")

        result = str(text)

        assert result == "My Name is: Adão Thalisson Castro Guimarães"

    def testAppendLine(self):
        text = StringBuilder()
        text.appendLine('My')
        text.appendLine('Name')
        text.appendLine('is')
        text.appendLine(':')
        text.appendLine('Adão')
        text.appendLine('Thalisson')
        text.appendLine('Castro')
        text.appendLine('Guimarães')

        result = str(text)

        assert result == 'My\nName\nis\n:\nAdão\nThalisson\nCastro\nGuimarães\n'

