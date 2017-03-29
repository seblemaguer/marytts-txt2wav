#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# HTTP + URL packages
import json, requests

# To play wave files
import pygame
import math # For ceiling


# Mary server informations
mary_host = "localhost"
mary_port = "59125"

# Input text
input = "Mary python client test"

# Configuration
configuration = """
# How to extract the input
input_serializer=marytts.io.TextSerializer

# How to render the output
# output_serializer=marytts.io.HTSLabelSerializer
# output_serializer=marytts.io.XMLSerializer
output_serializer=marytts.io.ROOTSJSONSerializer

# Current locale
locale=en_US

# List of modules
modules=marytts.language.en.Preprocess \
        marytts.language.en.JTokenizer \
        marytts.modules.nlp.OpenNLPPosTagger \
        marytts.modules.nlp.JPhonemiser \
        marytts.language.en.Prosody \
        marytts.modules.nlp.PronunciationModel \
        marytts.modules.acoustic.TargetFeatureLister
"""

# Build the query
query = {"input":"input","configuration":configuration}

# Run the query to mary http server
headers = {"Content-type": "application/x-www-form-urlencoded"} # FIXME: mandatory but why ?
r = requests.post("http://%s:%s/process/" % (mary_host, mary_port),
                      headers = headers,
                      data = query)

r = r.json()
if (r["exception"] is not None):
    print("cause: %s" % r["exception"]["embeddedException"]["cause"])
    for line in r["exception"]["embeddedException"]["stackTrace"]:
        print("\t%s:%s (%s.%s)" % (line["fileName"], line["lineNumber"], line["className"], line["methodName"]))

else:
    print(r["result"])
