from googletrans import Translator
import argparse, googletrans

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--output_language', type=str, default='fr')
    parser.add_argument('--inputfilepath', type=str)
    parser.add_argument('--outputfolder', type=str)
    args = parser.parse_args()
    if args.output_language not in googletrans.LANGCODES and args.output_language not in googletrans.LANGUAGES:
        print("invalid destination language code, must be part of")
        print(googletrans.LANGUAGES)
        exit(1)
    lang = args.output_language
    input_f = args.inputfilepath
    ouput_f = args.outputfolder + 'output.txt'
    translator = Translator()
    with open(input_f, 'r') as file:
        lines = file.readlines()
        res = translator.translate(lines, dest=args.output_language)
        with open(ouput_f, 'w') as ofile:
            for line in res:
                ofile.writelines(str(line.text))
