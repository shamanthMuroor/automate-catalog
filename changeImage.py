from PIL import Image
import os

dir = "D:\\Python Project Files\\Capstone Final Project\\supplier-data\\images\\"
for infile in os.listdir(dir):
    f, e = os.path.splitext(infile)
    infilepath = os.path.join(dir, infile)
    outfile = f + ".jpg"
    #print("infile: {}, outfile: {}".format(infile, outfile))
    if infile != outfile:
        try:
            with Image.open(infilepath) as im:
                if not im.mode == 'RGB':
                    im = im.convert('RGB')
                im.resize((600,400)).save(outfile)
                print("Convertion successful: {} -> {} [ mode:{} ]".format(infile, outfile, im.mode))
        except OSError:
            print("cannot convert", file)
