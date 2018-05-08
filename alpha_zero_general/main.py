# Colorful Traceback
try:
    import colored_traceback.auto
except ImportError:
    pass

try :
    from .Coach import Coach
    from .dotsandboxes.DnBGame import DnBGame as Game
    from .dotsandboxes.pytorch.NNet import NNetWrapper as nn
    from .utils import *
except Exception:
    from Coach import Coach
    from dotsandboxes.DnBGame import DnBGame as Game
    from dotsandboxes.pytorch.NNet import NNetWrapper as nn
    from utils import *


args = dotdict({
    'numIters': 100, # Changed from 1000
    'numEps': 50, # Changed from 100
    'tempThreshold': 15,
    'updateThreshold': 0.55, # Changed from 0.6
    'maxlenOfQueue': 200000,
    'numMCTSSims': 25, # Changed from 25
    'arenaCompare': 41, # Changed from 40
    'cpuct': 1,

    'checkpoint': './models/',
    'load_model': False,
    'load_folder_file': ('/dev/models/8x100x50','best.pth.tar'),
    'numItersForTrainExamplesHistory': 20,

    # OUR PARAMETERS
    'sequential_training': True, #Starting from smaller boards and going upwards,
    'max_board': 10,
    'time_limit': 0, # Zero means no time limit
    'rows': 4,
    'columns': 4
})

if __name__=="__main__":

    g = Game(args.rows,args.columns)
    nnet = nn(g)

    args.checkpoint += "dim" + str(args.rows) + 'x' + str(args.columns) + "/"

    print("Rows: " + str(args.rows))
    print("Columns: " + str(args.columns))


    if args.load_model:
        nnet.load_checkpoint(args.load_folder_file[0], args.load_folder_file[1])

    c = Coach(g, nnet, args)
    if args.load_model:
        print("Load trainExamples from file")
        c.loadTrainExamples()
    c.learn()

    # flag=False # Initial load
    #
    #
    # # Change so we train in a seq manner
    # for n in range(2,args.max_board+1):
    #     for m in range(2,i+1):
    #         print("Training on boards " + n + "x" + m + "...\n\n")
    #         g = Game(n,m, args.max_board)
    #         nnet = nn(g)
    #
    #         args.numEps= n*m
    #
    #         if args.load_model:
    #           nnet.load_checkpoint(args.load_folder_file[0], args.load_folder_file[1])
    #
    #         c = Coach(g, nnet, args)
    #         if flag or args.load_model:
    #             print("Load trainExamples from file")
    #             c.loadTrainExamples()
    #         c.learn()
    #
    #         flag=True # From now on we read the prev level