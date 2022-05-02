import sys
import numpy as np

def extract_action_frames(path):
    """ Ritorna la lista degli indici dei frame in cui 
        compare un oggetto. 
    """
    with open(path, 'r') as csvfile:
        lines = csvfile.readlines()[3:]
        action_frames = []
        for line in lines:
            frame = line.split(',')[0]
            action_frames.append(int(frame))
        return action_frames


def build_frame_binary_array(nframes, action_frames):
    """ Crea un array binario in cui l'i-esimo bit 
        è 1 se accade qualcosa (il frame è un action frame), 
        altrimenti è 0 
    """
    return [ 1 if i in action_frames else 0 for i in range(nframes) ]


if __name__ == '__main__': 

    if len(sys.argv) != 3:
        print("error, usage: python generate_user_sum.py <file_with_summaries.csv> <nframes>")

    _, path, nframes = sys.argv 
    
    user_summ = build_frame_binary_array(int(nframes), extract_action_frames(path))
    print(user_summ)