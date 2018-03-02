
from bhtsne import bhtsne
import numpy

def main(args):

    vectors=numpy.load(args.input)
    v2d=bhtsne.run_bh_tsne(vectors, no_dims=3, perplexity=50, theta=0.5, randseed=-1, verbose=True, initial_dims=50, use_pca=True, max_iter=1000)
    numpy.save(args.output,v2d)

    

if __name__=="__main__":

    import argparse

    parser = argparse.ArgumentParser(description='')
    g=parser.add_argument_group("Reguired arguments")
    
    g.add_argument('--input', type=str, help='Input file name')
    g.add_argument('--output', type=str, help='Input file name')
    
    args = parser.parse_args()

    main(args)


