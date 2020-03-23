import os
import subprocess
import argparse
import glob
import random
import sys

command_sample = 'python zad7.py trackmix --source "album" --count 5 --frame 15 -l -e'

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('-s', '--source', required='True')
        parser.add_argument('-d', '--destination')
        parser.add_argument('-c', '--count')
        parser.add_argument('-f', '--frame', default='10')
        parser.add_argument('-l', '--log', action='store_true')
        parser.add_argument('-e', '--extended', action='store_true')

        args = sys.argv[2:]
        parsed = parser.parse_args(args)

        if parsed.destination is None:
            parsed.destination = os.path.join(parsed.source, 'mix.mp3')

        tracklist = list(glob.glob(os.path.join(parsed.source, '*.mp3')))
        if parsed.count is None:
            parsed.count = len(tracklist)

        FNULL = open(os.devnull, 'w')
        parts = []
        for track_num in range(int(parsed.count)):
            each_track = tracklist[track_num]
            track_name = os.path.basename(each_track)
            if parsed.log:
                print('--- processing file {}: {}'.format(
                    track_num + 1, track_name
                ))

            part_name = 'part' + str(track_num) + '.mp3'
            start_sec = str(random.randint(30, 60))
            subprocess.call(['ffmpeg', '-ss', start_sec, '-t',
                             str(parsed.frame), '-i', each_track,
                             '-acodec', 'copy', part_name],
                            stdout=FNULL, stderr=subprocess.STDOUT)
            final_part_name = 'final_' + part_name
            if parsed.extended:
                out = str(int(parsed.frame) - 2)
                fade_line = 'afade=t=in:ss=0:d=2,afade=t=out:st=' \
                            + out + ':d=2'
                subprocess.call(['ffmpeg', '-i', part_name,
                                 '-af', fade_line, final_part_name],
                                stdout=FNULL, stderr=subprocess.STDOUT)
                os.remove(part_name)
            else:
                os.rename(part_name, final_part_name)

            parts += [final_part_name]

        concat_line = 'concat:' + '|'.join(parts)
        subprocess.call(['ffmpeg', '-i', concat_line,
                         '-acodec', 'copy', parsed.destination],
                        stdout=FNULL, stderr=subprocess.STDOUT)
        for part in parts:
            os.remove(part)

        print('--- done!\n')

    except:
        print('Error!')


