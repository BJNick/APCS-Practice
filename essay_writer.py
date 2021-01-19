import random
import wikipedia
import re

author = "Andreas Schroeder"
title = "The Late Man"

lit_devices = ["Allegory", "Alliteration", "Allusion", "Anachronism",
               "Anaphora", "Anastrophe", "Anthropomorphism", "Aphorism",
               "Archetype", "Chiasmus", "Colloquialism",
               "Cumulative sentence", "Dramatic irony", "Euphemism",
               "Exposition", "Flashback", "Foreshadowing", "Frame story",
               "Hyperbole", "Hypophora", "Imagery", "Irony", "Isocolon",
               "Juxtaposition", "Litotes", "Malapropism", "Metaphor",
               "Metonymy", "Motif", "Onomatopoeia", "Oxymoron", "Paradox",
               "Personification", "Point of view", "Polysyndeton",
               "Repetition", "Satire", "Simile", "Soliloquy", "Symbolism",
               "Synecdoche", "Tautology", "Tmesis", "Tone", "Tragicomedy",
               "Zoomorphism"]


def remove_braces(text):
    regex = re.compile(".*?\((.*?)\)")
    braces = re.findall(regex, text)
    for b in braces:
        text = text.replace(b, "")
    return text


def lit_function(device):
    text = wikipedia.summary(device + " literature device", sentences=1)
    #snip = "to " + " to ".join(text.split(" to ")[1:])
    snip = "is " + "is ".join(text.split("is ")[1:])
    snip = remove_braces(snip)
    return snip

device = lit_devices[random.randint(0, len(lit_devices))]

print(author, "uses", device.lower(), 'in \"' + title + '\" which',
      lit_function(device), end=" ")

device_2 = lit_devices[random.randint(0, len(lit_devices))]


print(device_2.capitalize(), 'is vitally important in the short story as it',
      lit_function(device_2))



