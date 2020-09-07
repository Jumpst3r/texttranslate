## Dockerized text file translation (raw text, txt)

### Description

Translate text files into a given language, auto-detecting source language.

### Usage

To use the docker image, first pull the image using

`docker pull jumpst3r/texttranslate`

And then execute 
```
docker run -it --rm -v /FULL_PATH_TO/example.txt:/input/example.txt -v /FULL_PATH_TO_OUTPUT_FOLDER/:/output/ jumpst3r/texttranslate sh /input/script.sh /input/example.txt LANG_CODE /output/
```

where `/FULL_PATH_TO/example.txt` corresponds to the local path of the document you'd like to translate. LANG_CODE should be replaced with the code corresponding to the target language. An exhaustive list of language codes can be found in the `install.json` file.

The output consists of:

- The translated document (same filetype as the input document)

The docker image is also compatible with [DIVAServices](https://github.com/lunactic/DIVAServices) a web-based framework providing streamlined access to DOI methods.

### Sources / Comments

Uses public (unofficial) google-translate API and as such might be limited in terms of numbers of numbers of words to be translated. For details on this issue, refer to [this link](https://github.com/ssut/py-googletrans)

For a similar project that supports translating formatted documents (odt, doc, docx), check out this [link](https://github.com/Jumpst3r/doctranslate)
